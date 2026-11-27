# -*- coding: utf-8 -*-
"""backward induction 三断言验证器（无第三方依赖）。

[1] 硬币行：值与 tie-break 无关（值唯一），策略与 tie-break 有关（策略可多解）
[2] 奇数 n 时先手拿不到一半的反例
[3] 通用 extensive-form 博弈的纯策略暴力枚举 + SPNE 判定（反例：SPNE 不唯一）
[4] maximin（保证值）与 BI 值在非零和时分离
"""
import itertools, random

# ---------------- [1][2] 硬币行 ----------------
def solve(coins, tie="left"):
    """返回 (值, 策略表)。tie 只影响策略，不影响值。"""
    n = len(coins)
    pre = [0] * (n + 1)
    for i, c in enumerate(coins):
        pre[i + 1] = pre[i] + c
    V = [[0] * n for _ in range(n)]
    choice = [[None] * n for _ in range(n)]
    for L in range(1, n + 1):                      # 归纳变量是区间长度 L
        for i in range(0, n - L + 1):
            j = i + L - 1
            if L == 1:
                V[i][j], choice[i][j] = coins[i], 'both'
                continue
            tot_l = pre[j + 1] - pre[i + 1]        # 剩 coins[i+1..j]
            tot_r = pre[j] - pre[i]                # 剩 coins[i..j-1]
            take_l = coins[i] + (tot_l - V[i + 1][j])   # 零和才有这个减法
            take_r = coins[j] + (tot_r - V[i][j - 1])
            if take_l > take_r:
                V[i][j], choice[i][j] = take_l, 'L'
            elif take_r > take_l:
                V[i][j], choice[i][j] = take_r, 'R'
            else:
                V[i][j] = take_l                   # 值不受 tie-break 影响
                choice[i][j] = 'L' if tie == "left" else 'R'
    return V[0][n - 1], choice

random.seed(7)
diff_val = bad_even = bad_odd = 0
for _ in range(300):
    n = random.randint(1, 9)
    c = [random.randint(1, 9) for _ in range(n)]
    v1, _ = solve(c, "left")
    v2, _ = solve(c, "right")
    if v1 != v2:
        diff_val += 1
    if n % 2 == 0 and v1 * 2 < sum(c):
        bad_even += 1
    if n % 2 == 1 and v1 * 2 < sum(c):
        bad_odd += 1
print("[1] 300 组随机硬币行：值随 tie-break 变化 =", diff_val, "(期望 0)")
print("[2] 偶数 n 先手拿不到一半 =", bad_even, "| 奇数 n =", bad_odd, "反例 [1,9,1] ->", solve([1, 9, 1])[0])
c = [100, 1, 1, 100, 1, 1, 100]
print("    ", c, "-> 先手", solve(c)[0], "/ 总", sum(c))

# ---------------- [3] 通用 SPNE 枚举 ----------------
class N:
    def __init__(self, nid, player=None, actions=None, payoff=None):
        self.id, self.player, self.actions, self.payoff = nid, player, actions or {}, payoff

def walk(node, prof):
    while node.actions:
        node = node.actions[prof[node.id]]
    return node.payoff

def all_nodes(node):
    yield node
    for a in node.actions.values():
        yield from all_nodes(a)

def strategies(root):
    dec = [x for x in all_nodes(root) if x.actions]
    for combo in itertools.product(*[list(x.actions) for x in dec]):
        yield {x.id: a for x, a in zip(dec, combo)}

def is_spne(root, prof):
    """子博弈完美：对每个决策 node（作子博弈根）、每个玩家、每个替代行动，检查能否改善"""
    for sub in all_nodes(root):
        if not sub.actions:
            continue
        base = walk(sub, prof)
        for p in {x.player for x in all_nodes(sub) if x.actions}:
            for cand in all_nodes(sub):
                if not cand.actions or cand.player != p:
                    continue
                for a in cand.actions:
                    alt = dict(prof)
                    alt[cand.id] = a
                    if walk(sub, alt)[p] > base[p]:
                        return False
    return True

def build_tie_tree():
    """2 人、非零和、完美信息、有限：玩家1 在 sub 上对 A/B 完全 indifferent"""
    return N('root', 0, {
        'L': N('sub', 1, {'A': N('la', payoff=(0, 5)), 'B': N('lb', payoff=(10, 5))}),
        'R': N('right', payoff=(3, 0)),
    })

root = build_tie_tree()
spnes = [(p, walk(root, p)) for p in strategies(root) if is_spne(root, p)]
print("\n[3] tie 树的所有 SPNE：")
for p, u in spnes:
    print("     profile =", p, "-> payoff =", u)
vals = {u for _, u in spnes}
print("     SPNE 个数 =", len(spnes), "| payoff 是否唯一:", len(vals) == 1)

# ---------------- [4] maximin vs BI ----------------
def maximin(node, me):
    """me 视角的保证值：对手 indifferent 时选对 me 最不利的一边"""
    if not node.actions:
        return node.payoff[me]
    v = [maximin(c, me) for c in node.actions.values()]
    return max(v) if node.player == me else min(v)

print("\n[4] 玩家0 取 L：玩家1 倒向 B ->", walk(root, {'root': 'L', 'sub': 'B'})[0],
      "| 倒向 A ->", walk(root, {'root': 'L', 'sub': 'A'})[0],
      "| maximin 保证值 =", maximin(root, 0))
