# 18.100B/18.1002 Real Analysis（实分析）— Spring 2025

**Instructor（讲师）:** Tobias Holck Colding

## <span style="color:#c0392b">Lecture 4: Sequences（序列）& Convergence（收敛）</span>

---

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem（定理）</span>

$\mathbb{R}$ 是一个包含 $\mathbb{Q}$ 的 complete ordered field（完备有序域）。

---

### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#2471a3">Upper Bound（上界）& Lower Bound（下界）</span>

设 $S$ 是一个 ordered set（有序集）。对于非空 subset（子集）$A \subseteq S$：

- 若存在 $M \in S$ 使得对所有 $a \in A$ 都有 $a \le M$，则称 $A$ 有 **upper bound（上界）**。
- 若存在 $m \in S$ 使得对所有 $a \in A$ 都有 $m \le a$，则称 $A$ 有 **lower bound（下界）**。

**Completeness（完备性）** 是指每个有界的非空 subset 都有 **least upper bound（最小上界）**，即 supremum（上确界）。

我们记 $A$ 的 supremum 为 $\sup A$。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 原文此处写有 "We denote by $\sup A$ the **greatest lower bound** of $A$"，但 $\sup A$ 应为 **least upper bound**（最小上界），而非 greatest lower bound（最大下界）。这应是讲师板书中的笔误——greatest lower bound（最大下界）对应的是 $\inf A$（infimum）。本译文已作纠正。
>
> 这条纠正涉及的不只是一个词，而是"从哪一端取代表元"：supremum（上确界）由 upper bound（上界）那一侧产生，infimum（下确界）由 lower bound（下界）那一侧产生，两侧集合的封闭方向相反，所以"取最小"与"取最大"不能互换。
>
> 机制从 upper bound（上界）集合开始。给定 ordered set（有序集）$S$ 与非空 subset（子集）$A$，令 $U(A) = \{M \in S : \forall a \in A,\ a \le M\}$。这个集合向上封闭：若 $M \in U(A)$ 且 $M \le M'$，则 $M' \in U(A)$ 自动成立。向上封闭有两个直接后果：$U(A)$ 只要非空就必然无穷多；它永远没有最大元，因为把任何候选往上抬一点仍旧是 upper bound（上界）。于是"从 $U(A)$ 里挑一个代表元"只剩一种可能——挑最小元。这就是 least upper bound（最小上界），即 $\sup A$。
>
> 反方向同理。lower bound（下界）集合 $L(A) = \{m \in S : \forall a \in A,\ m \le a \}$ 向下封闭，无穷多且无最小元，唯一可辨认的是最大元，即 greatest lower bound（最大下界）$\inf A$。因此"$\sup A$ 是 greatest lower bound（最大下界）"这句字面上要求 $\sup A$ 同时属于 $U(A)$ 与 $L(A)$；两个集合只在 $A$ 退化为单点 $A = \{a \}$ 时相交，此时 $\sup A = \inf A = a$。$A$ 一旦有两个以上元素，把 $\sup A$ 按下界去读，得到的值至多比真值低 $\sup A - \inf A$ 这么多（$A$ 的直径），还可能根本不属于 $L(A)$。顺带说明 supremum（上确界）不是 max（最大值）的别名：$A = (0,1)$ 时 $\sup A = 1$、$\inf A = 0$，两者都不在 $A$ 里。
>
> supremum（上确界）可操作的刻画只有一条：对任意 $\varepsilon > 0$，存在 $a \in A$ 使 $a > \sup A - \varepsilon$。理由是最小性——若某个 $\varepsilon$ 找不到这样的 $a$，则 $\sup A - \varepsilon$ 本身就是更小的 upper bound（上界），与"最小"矛盾。这条刻画是后面全部关于 supremum（上确界）的论证的入口（构造见证元、夹逼、界估计）；一旦把 $\sup A$ 误当 greatest lower bound（最大下界），它就失效了，因为从"下界"推不出"集合里有元素超过它"。
>
> 算一个具体集合：$A = \{1 - 1/n : n \in \mathbb{N} \}$，即 $0,\ \frac{1}{2},\ \frac{2}{3},\ \frac{3}{4},\ \ldots$。上界集合 $U(A) = [1, +\infty)$，最小元是 $1$，故 $\sup A = 1$；注意 $1 \notin A$，因为 $1 - 1/n = 1$ 等价于 $1/n = 0$，无正整数解。下界集合 $L(A) = (-\infty, 0]$，最大元是 $0$，故 $\inf A = 0$，而 $0 = a_1$ 确实在 $A$ 里。按笔误把 $\sup A$ 读成 greatest lower bound（最大下界），答案变成 $0$，与真值差 $1$，相对误差 $100$ 个百分点。
>
> 把 $\varepsilon$ 的剥离作用落到整数上：取 $\varepsilon = 10^{-6}$，要求 $a_n > 1 - 10^{-6}$，即 $1/n < 10^{-6}$，即 $n > 10^{6}$，最小可用的下标是 $n = 1000001$，此时 $a_n = 1 - 1/1000001 = 0.999999000001$（用 `python` 复算）。量级上的含义是：$\varepsilon$ 每缩小 $10$ 倍，见证元的下标就涨 $10$ 倍——supremum（上确界）只承诺"存在一个"，不承诺"离得近"，这与收敛定义里 $N$ 依赖 $\varepsilon$ 是同一种只保证存在、不保证位置的结构。
>
> 两侧的对偶关系有一条恒等式钉死：$\inf A = -\sup(-A)$，其中 $-A = \{-a : a \in A \}$。代入上面的 $A$：$-A$ 是 $0, -\frac{1}{2}, -\frac{2}{3}, \ldots$，其上界集合是 $[0, +\infty)$，$\sup(-A) = 0$，故 $\inf A = 0$，与直接算的一致。映射 $x \mapsto -x$ 把 order（序）翻了过来，正是它交换了 supremum（上确界）与 infimum（下确界）；所以两者名字混写之后，经这个映射一变换就自相矛盾——这里的记号错误可以当作代数错误被检出，不是排版细节。
>
> 跨课程连接之一：CLRS 二分搜索。令 $E = \{q \in \mathbb{Q} : q^{2} < 2 \}$，它在 $\mathbb{Q}$ 内的 upper bound（上界）集合是 $U(E) = \{q \in \mathbb{Q} : q^{2} > 2 \}$，这个集合在有理数里没有最小元：任取 $u \in U(E)$，令 $u_+ = (2u + 2)/(u + 2)$，则 $u_+^{2} > 2$ 且 $u_+ < u$，即又得到一个更小的 upper bound（上界）。从 $q_1 = 3/2$ 迭代得 $q_2 = 10/7$（$q_2^{2} - 2 = 0.0408\ldots$）、$q_3 = 17/12$（偏差 $0.00694\ldots$）、$q_4 = 58/41$（偏差 $0.00119\ldots$），每一步都仍满足 $q_k^{2} > 2$ 且更靠近 $\sqrt{2}$。二分 $40$ 次后区间宽 $2^{-40} \approx 9.09 \times 10^{-13}$，两端都是有理数，却没有一端等于 $\sqrt{2}$（double 下 $1.4142135623730951^{2} = 2.0000000000000004$）。这正是 completeness（完备性）不可省的可算证据：bounded（有界）的非空集可以没有 supremum（上确界）。
>
> 跨课程连接之二：CSAPP 第 2 章浮点表示。double（双精度）尾数 $52$ 位，在 $1$ 附近相邻可表示数的间距 ulp（末位单位）为 $2^{-52} \approx 2.22 \times 10^{-16}$。在这张离散网格上，"最小上界"退化成上取整到网格，`nextafter` 就是它的算子；它与实数意义下 supremum（上确界）的区别在于：实数侧对分辨率没有任何限制，bounded（有界）非空集一定同时拥有 supremum（上确界）与 infimum（下确界）且各自唯一，浮点侧的一切 supremum（上确界）都带一个 ulp（末位单位）量级的系统误差，溢出到 $+\infty$ 时连有限性都丢了。
>
> 回到正文：L0022 用 least upper bound（最小上界）定义 completeness（完备性），L0028 才单独用 greatest lower bound（最大下界）定义 infimum（下确界）。两行分开写不是重复，而是对偶两侧各定义一次；板书把两半拼在 $\sup A$ 上，等价于在 $x \mapsto -x$ 下让定义自相矛盾。纠正后只记一句：$\sup A = \min U(A)$、$\inf A = \max L(A)$，其中 $U(A)$ 向上封闭、$L(A)$ 向下封闭，各取唯一可辨的那一端。

**Greatest lower bound（最大下界）** 是一个大于或等于所有其他 lower bound 的 lower bound，即 infimum（下确界），记作 $\inf A$。

---

## <span style="color:#c0392b">Sequences（序列）</span>

$\sqrt{2}$ 可以被理解为以下 decimal（十进制小数）序列的 limit（极限）：

```math
1 < 1.4 < 1.41 < 1.414 < \cdots
```

### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#2471a3">Sequence（序列）</span>

A **sequence（序列）** of real numbers（实数）是一个 function（函数）$f: \mathbb{N} \to \mathbb{R}$。

通常使用记号 $a_n = f(n)$。

---

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 1（例 1）</span>

$\sqrt{2}$ 是序列 $a_1 = 1,\; a_2 = 1.4,\; a_3 = 1.41,\; a_4 = 1.414,\; \ldots$ 的 limit。

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 2（例 2）</span>

$a_n = (-1)^n$。该序列 **没有 limit（极限）**，因为 $a_n$ 在 $-1$ 和 $1$ 之间交替。

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 3（例 3）</span>

序列 $a_n = \dfrac{1}{n}$ 的 limit 为 $0$。

---

### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#2471a3">Limit（极限）& Convergence（收敛）</span>

设 $a_n$ 是一个 sequence（序列），$a$ 是一个 real number（实数）。若对任意 $\varepsilon > 0$，存在 $N \in \mathbb{N}$ 使得当 $n \ge N$ 时有

```math
|a_n - a| < \varepsilon,
```

则称 $a_n$ **converges（收敛）** 到 $a$。此时称 $a$ 是序列的 **limit（极限）**，并称序列是 **convergent（收敛的）**。

不 convergent 的序列称为 **divergent（发散的）**。

---

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example: $0.999\ldots = 1$</span>

$0.999999999\ldots = 1$ 是什么意思？

定义 sequence $a_n$ 如下：

```math
a_1 = 0.9,\quad a_2 = 0.99,\quad a_3 = 0.999,\quad a_4 = 0.9999,\quad \ldots
```

等式左边即被定义为该 sequence $a_n$ 的 limit。

<span style="color:#2471a3;">**[claim]**</span> **Claim（断言）：** $\displaystyle \lim_{n\to\infty} a_n = 1$。

> <span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.* 我们需要证明：对任意 $\varepsilon > 0$，存在 $N \in \mathbb{N}$ 使得当 $n \ge N$ 时有 $|a_n - 1| < \varepsilon$。
>
> 由 Archimedean property（阿基米德性质）可取 $N$ 使得 $\dfrac{1}{N} < \varepsilon$。又有 $|a_n - 1| = 10^{-n}$。因此当 $n \ge N$ 时，
>
> ```math
> |a_n - 1| = 10^{-n} < \frac{1}{n} \le \frac{1}{N} < \varepsilon.
> ```
>
> 这就证明了该 claim。 ∎

---

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem: Convergent Sequence Is Bounded（收敛序列必有界）</span>

若 $a_n$ 是 convergent sequence（收敛序列），则集合 $\{a_n\}$ 是 $\mathbb{R}$ 的 bounded subset（有界子集）。

> <span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.* 因为 $a_n$ convergent 到 $a$，可取 $N$ 使得当 $n \ge N$ 时有 $|a - a_n| < 1$。
>
> 集合 $\{a_1, \ldots, a_{N-1}\}$ 是有限的，因此 bounded，故存在 $C \in \mathbb{R}$ 使得对 $n = 1, \ldots, N-1$ 有 $|a_n| \le C$。
>
> 对于 $n \ge N$，由三角不等式得
>
> ```math
> |a_n| \le |a| + |a_n - a| \le |a| + 1.
> ```
>
> 因此对所有 $n$ 有
>
> ```math
> |a_n| \le \max\{C,\; |a| + 1\}.
> ```
>
> 即 $\{a_n\}$ 有界。 ∎

---

## <span style="color:#c0392b">Basic Algebraic Properties of Limits（极限的基本代数性质）</span>

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem: Algebraic Limit Laws（极限运算法则）</span>

设 $a_n$ 和 $b_n$ 是 convergent sequences（收敛序列），$\displaystyle \lim_{n\to\infty} a_n = a$，$\displaystyle \lim_{n\to\infty} b_n = b$，且 $C \in \mathbb{R}$。则

1. **Scalar multiplication（数乘）：** $c_n = C a_n$ 收敛，且 $\displaystyle \lim_{n\to\infty} c_n = C a$。
2. **Sum（加法）：** $c_n = a_n + b_n$ 收敛，且 $\displaystyle \lim_{n\to\infty} c_n = a + b$。
3. **Product（乘法）：** $c_n = a_n b_n$ 收敛，且 $\displaystyle \lim_{n\to\infty} c_n = a b$。
4. **Quotient（除法）：** 若 $b_n \neq 0$ 且 $b \neq 0$，则 $\displaystyle c_n = \frac{a_n}{b_n}$ 收敛，且 $\displaystyle \lim_{n\to\infty} c_n = \frac{a}{b}$。

> <span style="color:#2471a3;">**[proof]**</span> *Proof of 1（性质 1 的证明）.* 若 $C = 0$ 则结论显然，故只需证 $C \neq 0$ 的情形。给定 $\varepsilon > 0$，存在 $N$ 使得当 $n \ge N$ 时有
>
> ```math
> |a - a_n| < \frac{\varepsilon}{|C|}.
> ```
>
> 两边乘以 $|C|$ 得：当 $n \ge N$ 时 $|C a - C a_n| < \varepsilon$。这就证明了性质 1。 ∎
>
> <span style="color:#2471a3;">**[proof]**</span> *Proof of 2（性质 2 的证明）.* 注意到
>
> ```math
> |c_n - (a + b)| = |a_n + b_n - (a + b)| = |(a_n - a) + (b_n - b)| \le |a_n - a| + |b_n - b|.
> ```
>
> 由于 $a_n \to a$，对 $\varepsilon > 0$ 可取 $N_a$ 使得当 $n \ge N_a$ 时有 $|a_n - a| < \dfrac{\varepsilon}{2}$。
>
> 同样由于 $b_n \to b$，可取 $N_b$ 使得当 $n \ge N_b$ 时有 $|b_n - b| < \dfrac{\varepsilon}{2}$。
>
> 令 $N = \max\{N_a, N_b\}$，则当 $n \ge N$ 时
>
> ```math
> |c_n - (a + b)| \le |a_n - a| + |b_n - b| < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.
> ```
>
> 这就证明了性质 2。 ∎
>
> <span style="color:#2471a3;">**[proof]**</span> *Proof sketch of 3（性质 3 的证明概要）.* 使用估计
>
> ```math
> |a b - a_n b_n| \le |a b - a_n b| + |a_n b - a_n b_n| = |b|\,|a - a_n| + |a_n|\,|b - b_n|.
> ```
>
> 结合之前证明的定理（$\{|a_n|\}$ 有界）即可完成证明。核心思想如上，细节需要补充。 ∎
>
> <span style="color:#2471a3;">**[proof]**</span> *Proof sketch of 4（性质 4 的证明概要）.* 先证 $a_n = 1$ 的特殊情况，再结合性质 3 推广到一般情况。使用估计
>
> ```math
> \left|\frac{1}{b_n} - \frac{1}{b}\right| = \frac{|b - b_n|}{|b|\,|b_n|},
> ```
>
> 以及 $|b_n| \le |b| + |b_n - b|$ 和 $|b_n| \ge |b| - |b_n - b|$ 来对分母做下界估计。与性质 3 类似，核心思想如上，细节需要补充。 ∎

---

## <span style="color:#c0392b">Subsequences（子序列）</span>

### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#2471a3">Subsequence（子序列）</span>

回忆 sequence $a_n$ 是一个 function（函数）$f: \mathbb{N} \to \mathbb{R}$，其中 $a_n = f(n)$。序列 $a_n$ 的 **subsequence（子序列）** $b_n$ 是函数的 composition（复合）$f \circ g$，其中 $g: \mathbb{N} \to \mathbb{N}$ 是 strictly increasing function（严格递增函数）。因此 $b_n = f(g(n))$。有时 subsequence 也记作 $a_{n_k}$。

---

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 1（例 1）</span>

设 $a_n = (-1)^n$。该序列在 $-1$ 和 $1$ 之间交替。

- $b_n = 1$（对所有 $n$）是一个 subsequence。
- $c_n = -1$（对所有 $n$）也是 subsequence。
- $c_n = (-1)^{n+1}$ 也是 $a_n$ 的 subsequence。
- 另一个 subsequence 的例子：$1, 1, -1, -1, 1, 1, -1, -1, \ldots$。

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 2（例 2）</span>

设 $a_n = n$，即 $1, 2, 3, 4, 5, 6, \ldots$。

- 递增的奇数序列 $1, 3, 5, 7, 9, \ldots$ 是一个 subsequence。
- 递增的偶数序列 $2, 4, 6, 8, 10, \ldots$ 是另一个 subsequence。
- 序列 $1, 1, 2, 2, 3, 3, 4, 4, 5, 5, \ldots$ **不是** subsequence（因为 $g$ 必须严格递增，不能重复）。

---

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem: Convergence and Subsequences（收敛与子序列）</span>

序列 $a_n$ convergent 到 $a$ **当且仅当** $a_n$ 的所有 subsequences 都 convergent 到 $a$。

> <span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.* 需要证明两个方向。
>
> **方向一：** 若所有 subsequences 都 convergent 到 $a$，则 $a_n$ 本身 convergent 到 $a$。显然成立，因为 $a_n$ 自身就是（平凡的）subsequence。
>
> **方向二：** 任意 convergent sequence 的任一 subsequence 都 convergent 到同一 limit。给定 $\varepsilon > 0$，取 $N$ 使得当 $n \ge N$ 时有 $|a_n - a| < \varepsilon$。对 $k \ge N$，有 $n_k \ge k \ge N$，因此
>
> ```math
> |a_{n_k} - a| < \varepsilon.
> ```
>
> 这就证明了第二个方向。 ∎

---

### <span style="color:#2471a3;">**[reference]**</span> <span style="color:#7f8c8d">References（参考文献）</span>

[TBB] B.S. Thomson, J.B. Bruckner, and A.M. Bruckner, *Elementary Real Analysis*, 2nd edition.
可下载于：

- <span style="color:#2471a3;">Screen-optimized（屏幕优化版）:</span> <https://classicalrealanalysis.info/com/documents/TBB-AllChapters-Landscape.pdf>
- <span style="color:#2471a3;">Print-optimized（打印优化版）:</span> <https://classicalrealanalysis.info/com/documents/TBB-AllChapters-Portrait.pdf>

---

MIT, Dept. of Math., 77 Massachusetts Avenue, Cambridge, MA 02139-4307.

<span style="color:#7f8c8d;">*Source（来源）:* MIT OpenCourseWare, 18.100B Real Analysis, Spring 2025. (<https://ocw.mit.edu>)</span>
