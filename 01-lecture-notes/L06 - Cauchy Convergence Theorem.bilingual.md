# 18.100B / 18.1002 Real Analysis（实分析）

## <span style="color:#c0392b">Lecture 6 — Cauchy Convergence Theorem（柯西收敛定理）</span>

<span style="color:#7f8c8d;">Instructor: Tobias Holck Colding · Spring 2025 · MIT</span>

---

### <span style="color:#2471a3;">**[lecture]**</span> <span style="color:#c0392b">Last Time（上节回顾）</span>

上节课我们讨论了 limits（极限）的基本 algebraic properties（代数性质）、monotone convergence theorem（单调收敛定理）以及 Cauchy sequence（柯西序列）。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Colding 在视频开头快速回顾了 monotone convergence theorem（MCT，单调收敛定理）的完整陈述：若一个序列单调递增（或递减）且有界，则它收敛——递增时收敛到 supremum（上确界），递减时收敛到 infimum（下确界）。这个回顾自然地引出今天的主题：**MCT 要求单调性，但 Cauchy convergence theorem 不要求任何单调条件**——它只用序列项彼此靠近的程度来刻画收敛性。这是分析学中一个深刻的转折：从「知道极限在哪」（MCT 收敛到确界）到「不需要知道极限在哪也能判断收敛」（Cauchy criterion）。🎥 *Colding 在视频中说:* "the third thing we talked about, and that's where we will continue today, is Cauchy sequence."（翻译：我们讨论的第三件事，也是今天要继续的，就是柯西序列。）
> 
> 你在 L05 已经学过的 MCT 和今天要学的 Cauchy 收敛定理是实分析中刻画收敛性的两大支柱——理解它们的互补关系比孤立记忆每个定理更重要。

---

### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f;">**Cauchy Sequence（柯西序列）**</span>

一个序列 $a_n$ 称为 **Cauchy sequence（柯西序列）**，如果对任意 $\epsilon > 0$，存在 $N$，使得当 $m, n \ge N$ 时，有

```math
|a_n - a_m| < \epsilon.
```

（直观理解：序列的 tail（尾部）挤在一起。）

> <span style="color:#7f8c8d;">TBB §2.11, p.74</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Cauchy 序列的核心直觉是「尾巴挤在一起」——Colding 教授在视频中反复用这个口语化表达：*"the Cauchy sequence just meant that the tail of the sequence bunched together."*（翻译：柯西序列就意味着序列的尾巴挤在一起。）这里的 "tail" 指序列中足够靠后的所有项（$n \ge N$ 的那些 $a_n$）。条件 $|a_n - a_m| < \epsilon$ 说的是**尾部中任意两项**的距离都小于 $\epsilon$——不只是相邻项，而是所有项彼此靠近。这是 Cauchy 条件比单纯的「相邻项距离趋于零」更强的关键所在：相邻项收敛于零（$|a_{n+1} - a_n| \to 0$）**不足以保证**序列收敛（反例：调和级数的部分和序列），但 Cauchy 条件可以。
> 
> 在 TBB 教材中，Cauchy 序列的定义出现在 §2.11。TBB 用 Cauchy criterion（柯西准则）来叙述 $\mathbb{R}$ 的完备性：一个序列收敛当且仅当它是 Cauchy 序列。这与 L04 中「$\mathbb{R}$ 是完备有序域」的公理是等价的表述方式。
> 
> 另一个理解角度：你在 6.042J 离散数学中学过的「等价关系」在这里隐形出现——如果把「最终距离任意小」的关系形式化，Cauchy 序列的集合可以构成一个等价类，每个等价类对应一个实数。这是用 Cauchy 序列构造实数系（Cantor 的构造方法）的核心思想。不过现在你只需要把它当作刻画收敛性的条件即可。

---

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">Cauchy Convergence Theorem（柯西收敛定理）</span>

一个序列 convergent（收敛）当且仅当它是 Cauchy sequence（柯西序列）。

> <span style="color:#7f8c8d;">TBB §2.11, p.75</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这是本节的核心定理，也是实分析中最重要的等价性之一。先拆解两个方向：
> 
> **（⇒）** 收敛 ⇒ Cauchy：这在上节课已经证明——若 $a_n \to a$，则 $|a_n - a_m| \le |a_n - a| + |a - a_m| < \epsilon/2 + \epsilon/2 = \epsilon$（三角不等式 + 收敛定义）。这个方向在任何度量空间中都成立，不依赖于 $\mathbb{R}$ 的特殊性质。
> 
> **（⇐）** Cauchy ⇒ 收敛：这才是真正深刻的逆命题。它在有理数集 $\mathbb{Q}$ 中**不成立**——例如，取 $\mathbb{Q}$ 中逼近 $\sqrt{2}$ 的十进制序列：$1, 1.4, 1.41, 1.414, \ldots$，它在 $\mathbb{Q}$ 中是 Cauchy 序列但不收敛（因为在 $\mathbb{Q}$ 中没有 $\sqrt{2}$ 这个极限）。Cauchy ⇒ 收敛等价于实数系的 **completeness（完备性）**——这正是 $\mathbb{R}$ 区别于 $\mathbb{Q}$ 的本质性质。
> 
> 🎥 *Colding 在视频中解释了这个逻辑关系:* "the Cauchy convergence theorem is just a converse."（翻译：柯西收敛定理就是逆命题。）这里的 "converse" 指：已经知道收敛一定推出 Cauchy，现在要证明 Cauchy 也能推出收敛。
> 
> 在 CSAPP 中你见过类似的完备性思想：浮点数系 $\mathbb{F}$ 不是完备的（两个浮点数之间的运算结果可能不在 $\mathbb{F}$ 中，需要舍入），而实数系 $\mathbb{R}$ 是完备的。完备性是数学对象「封闭性」的最强形式。

---

### <span style="color:#2471a3;">**[application]**</span> <span style="color:#c0392b;">Application: Existence of Fixed Points（应用：不动点的存在性）</span>

考虑 map（映射）$T : \mathbb{R} \to \mathbb{R}$。点 $x_0 \in \mathbb{R}$ 称为 **fixed point（不动点）**，如果

```math
T(x_0) = x_0.
```

---

### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f;">**Contracting Map（压缩映射）**</span>

一个 **contracting map（压缩映射）** 是映射 $T : \mathbb{R} \to \mathbb{R}$，满足存在 $c < 1$，使得对所有 $x, y \in \mathbb{R}$，有

```math
|T(x) - T(y)| \le c \, |x - y|.
```

（直观理解：映射后，points（点）被挤压得更加靠近。）

> <span style="color:#7f8c8d;">TBB §2.11, p.76（作为 Cauchy 序列的应用引入）</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Contracting map 的定义包含一个关键常数 $c < 1$。注意：必须是**严格小于 1** 的常数，且对所有 $x, y$ 一致成立（uniformly）。如果对每对 $(x, y)$ 存在一个依赖它们的 $c_{x,y} < 1$ 但无统一上界，则不是 contracting map——这是初学者容易忽略的微妙点。
> 
> 🎥 *Colding 用极其形象的语言解释:* "under the map, the images are squeezed more together."（翻译：在这个映射下，像被挤压得更靠近了。）注意他用 "squeezed"（挤压）这个动词——它暗示 mapping 是一种主动的、统一的「收缩」操作。配合常数 $c\lt 1$ 的几何意义：任意两点经 $T$ 映射后，距离至少缩小到原来的 $c$ 倍（$< 1$），因此反复应用 $T$（迭代）会让距离以几何级数 $c^n$ 的速度指数衰减。
> 
> 这个概念是后续 metric spaces（度量空间）中 Banach fixed point theorem（巴拿赫不动点定理，也即 contraction mapping principle）的特例。在 100B 后续的 metric space 部分（L12-L14）会推广到一般的完备度量空间。

---

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">Contracting Mapping Theorem（压缩映射定理）</span>

任何 contracting map（压缩映射）都有一个 fixed point（不动点）。

> <span style="color:#7f8c8d;">TBB §2.11, p.76</span>

---

### <span style="color:#2471a3;">**[proof]**</span> <span style="color:#c0392b;">Uniqueness（唯一性）</span>

首先证明：对于 contracting map，fixed point（不动点）是 **unique（唯一的）**。

假设 $x$ 和 $y$ 是两个 fixed points（不动点），我们要证明 $x = y$。

```math
|x - y| = |T(x) - T(y)| \le c \, |x - y|.
```

由于 $c < 1$，这推出 $|x - y| = 0$，因此 $x = y$。$\square$

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 唯一性的证明非常简洁——它只用了 contracting map 的定义和 fixed point 的定义，三步即完成。核心技巧是注意到 $|x-y| = |T(x)-T(y)|$（因为 $x,y$ 都是不动点），然后代入压缩条件得到 $|x-y| \le c|x-y|$。由于 $c\lt 1$，唯一满足这个不等式的非负数是 $0$——这就是典型的「自举不等式」技巧（self-bounding inequality）：一个量被自身的一个严格缩小倍数所控制，迫使它为零。
> 
> 这个证明的美感在于它**不需要 Cauchy 收敛定理**——唯一性只依赖于压缩常数 $c\lt 1$ 和不动点的定义。不动点的**存在性**才需要 Cauchy 收敛定理（下面会展示）。存在 + 唯一 = 完整的不动点定理。这种将「存在性」和「唯一性」分而治之的证明策略在数学分析中非常普遍。

---

### <span style="color:#2471a3;">**[proof]**</span> <span style="color:#c0392b;">Existence（存在性）— 概略</span>

在 Problem Set 3 中，你将要求证明：对于 contracting map $T$ 和任意初始值 $a_1 \in \mathbb{R}$，由迭代关系 $a_{n+1} = T(a_n)$ 定义的序列是 Cauchy sequence（柯西序列）。由 Cauchy convergence theorem（柯西收敛定理），$a_n$ 收敛。

记其 limit（极限）为 $a$。我们断言 $T(a) = a$。

注意到 $T(a_n) = a_{n+1} \to a$。若我们能证明「当 $x_n \to x$ 时，有 $T(x_n) \to T(x)$」，则

```math
T(a_n) \to T(a),
```

但我们已有 $T(a_n) = a_{n+1} \to a$，因此 $T(a) = a$，即 $a$ 是 fixed point（不动点）。

于是我们只需证明：若 $x_n \to x$，则 $T(x_n) \to T(x)$。为此，观察

```math
|T(x_n) - T(x)| \le c \, |x_n - x|.
```

由于 $x_n \to x$，我们有 $|x_n - x| \to 0$，因此 $|T(x_n) - T(x)| \to 0$。于是 $T(x_n) \to T(x)$。

将此结论应用于序列 $a_n$，即证明 $a$ 是 $T$ 的 fixed point（不动点）。$\square$

<span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这个存在性证明的架构非常精巧，值得拆解为四个层次：

> **层次 1（迭代生成序列）**：$a_{n+1} = T(a_n)$。这利用映射本身来生成候选解——不需要猜极限在哪，映射会自动把序列「挤压」到不动点。
> 
> **层次 2（证明是 Cauchy）**：这是技术的核心。PSet 3 中你要做的是利用 $|T(x)-T(y)| \le c|x-y|$ 迭代，得到 $|a_{n+1} - a_n| \le c^{n-1} |a_2 - a_1|$，然后用几何级数求和得出对任意 $m>n$，$|a_m - a_n| \le \frac{c^{n-1}}{1-c}|a_2 - a_1|$——由于 $c\lt 1$，尾部任意两项距离可以任意小。🎥 *Colding 在视频中特别警告:* "That's not enough to prove that's a Cauchy sequence, right, because I need to prove that for all n and m sufficiently large."（翻译：那还不够证明它是柯西序列，对吧？因为我需要证明对所有充分大的 n 和 m 都成立。仅证相邻项不够——必须把几何级数扩展到任意两项。）
> 
> **层次 3（Cauchy ⇒ 收敛）**：直接调用 Cauchy convergence theorem，得到极限 $a$ 的存在性。
> 
> **层次 4（极限 = 不动点）**：这里用了一个重要引理——contracting map 是连续的（因为 $|T(x_n)-T(x)| \le c|x_n-x|$ 表明 $T$ 满足更强的 Lipschitz 条件）。连续性保证了「极限可以穿过函数」：$T(\lim a_n) = \lim T(a_n)$。结合 $T(a_n) = a_{n+1} \to a$，得到 $T(a) = a$。
> 
> 整个过程是分析学中不动点论证的范式：迭代 → Cauchy → 收敛 → 连续性传递极限 → 不动点。这个范式在 ODE 和 PDE 理论中反复出现。

---

### <span style="color:#2471a3;">**[application]**</span> <span style="color:#c0392b;">Applications of the Contracting Mapping Theorem（压缩映射定理的应用）</span>

#### <span style="color:#2471a3;">**[application]**</span> Existence of Solutions to ODEs（常微分方程解的存在性）

我们稍后会回到这个话题——届时需要把 contracting mapping theorem（压缩映射定理）推广到比实数更一般的空间上。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Colding 在此给了一个重要的预告：ODE（常微分方程）的解的存在性可以通过 contracting mapping theorem 来证明。这是著名的 Picard-Lindelöf 定理（皮卡-林德勒夫定理）的核心思想——将微分方程转化为积分方程，然后在适当的函数空间上构造一个 contracting map，其不动点就是微分方程的解。🎥 *Colding 在视频中强调:* "The contracting mapping theorem is actually extremely powerful. It can be used to solve what's called ODE, Ordinary Differential Equations. But it can also be used to solve PDEs."（翻译：压缩映射定理实际上极其强大。它可以用来求解常微分方程，甚至偏微分方程。）
> 
> 100B 的最后几讲（L22-L23）会详细展开这个应用。现在只需记住：**一个关于实数序列的定理，经过「空间升级」（函数空间 + 度量），可以证明微分方程解的存在唯一性**——这是 20 世纪分析学的核心方法论。

---

#### <span style="color:#2471a3;">**[application]**</span> Newton's Method（牛顿法）

Newton's method（牛顿法）的目标：寻找函数 $f : \mathbb{R} \to \mathbb{R}$ 的 **zero（零点）**——即求解 $f(x) = 0$。

假设 $x_1$ 是一个 "good" initial guess（足够好的初始猜测），即 $f(x_1)$ 充分小。另假设 $f' \neq 0$。定义映射

```math
T(x) = x - \frac{f(x)}{f'(x)}.
```

计算其导数：

```math
T'(x) = 1 - \frac{f'(x)}{f'(x)} + \frac{f(x) f''(x)}{[f'(x)]^2}
      = \frac{f(x) f''(x)}{[f'(x)]^2}.
```

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这里 $T'(x)$ 的计算过程比讲义中显示的更详细。原推导：$T'(x) = 1 - \frac{f'}{f'} + \frac{f f''}{(f')^2}$——第一项 $1$ 来自 $x$ 的导数，第二项使用商的导数公式 $(f/f')' = (f' \cdot f' - f \cdot f'')/(f')^2 = 1 - f f''/(f')^2$（注意这里假设 $f' \neq 0$）。两项相减时 $1$ 被抵消，留下 $f f'' / (f')^2$。🎥 *Colding 在板书上一项一项推导，然后指出:* "So you see that this thing here cancel with that. So these here cancel."（翻译：你看，这一项和那一项抵消了。）
> 
> 化简结果为 $T'(x) = \frac{f(x) f''(x)}{[f'(x)]^2}$，这是理解 Newton 方法为何是 contracting map 的关键：**在 $f(x) \approx 0$ 的附近（即根附近），$T'(x)$ 也非常接近 $0$，从而 $|T'(x)| < 1$**，由 mean value theorem（中值定理）推出 $T$ 在局部是压缩映射。

因此，只要 $x$ 保持在 initial guess（初始猜测）附近，且对于 initial guess 有 $f(x)$ 远小于 $\frac{[f'(x)]^2}{f''(x)}$（即 $|T'(x)| < 1$），则 $T$ 是一个 contracting map（压缩映射）。由 contracting mapping theorem（压缩映射定理），序列 $x_{n+1} = T(x_n)$ 是 Cauchy sequence（柯西序列），收敛到 $T$ 的一个 fixed point（不动点）。

对于 $T$ 的 fixed point，我们有 $T(x) = x$，即 $x - \frac{f(x)}{f'(x)} = x$，因此 $f(x) = 0$。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这是本节最精彩的「应用套娃」——用 Cauchy 收敛定理证明 contracting mapping theorem，再用 contracting mapping theorem 解释 Newton 方法的收敛性。关键逻辑链：
> 
> 1. **构造 T**：$T(x) = x - f/f'$。不动点 $T(x)=x \iff f(x)=0$，所以求根等价于找不动点。
> 2. **验证压缩性**：$|T'(x)| = |f f''/(f')^2|$。若初始猜测 $x_1$ 使得 $|T'(x_1)| < 1$，则由连续性，在 $x_1$ 的某个邻域内 $|T'| \le c < 1$（一致上界），中值定理确保 $T$ 在该邻域内是 contracting。
> 3. **迭代收敛**：Contracting mapping theorem ⇒ 迭代序列收敛到不动点 ⇒ 不动点 = 原函数的根。
> 
> 🎥 *Colding 完整地走完了这个逻辑，并在收敛回推时总结:* "But that, of course, means f of x at 0 is equal to 0."（翻译：但那当然意味着 $f(x_0) = 0$。）
> 
> 这里有一个容易被忽视的技术点：讲义中提到的「$f(x)$ 远小于 $\frac{[f'(x)]^2}{f''(x)}$」实际上等价于 $|T'(x)| < 1$。严格表述是：如果在一个区间 $I$ 上 $|T'(x)| \le c < 1$ 一致成立，则 $T$ 在 $I$ 上是 contracting map（常数 $c$ 由中值定理给出：$|T(x)-T(y)| = |T'(\xi)| \cdot |x-y| \le c|x-y|$）。
> 
> 你在 L16 会学到的 mean value theorem（中值定理）正是连接「导数有界」和「函数是压缩映射」的桥梁。这与 CSAPP 中的数值分析思想相通：Newton 方法的每次迭代在「根附近」具有 **quadratic convergence（二次收敛）**——比一般的 contracting map 收敛快得多，但分析其收敛性仍然依赖 contracting map 框架作为第一步。

---

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">Bolzano-Weierstrass Theorem（波尔查诺-魏尔斯特拉斯定理）</span>

任何 bounded sequence（有界序列）都有一个 convergent subsequence（收敛子列）。

> <span style="color:#7f8c8d;">TBB §2.12, p.78</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Bolzano-Weierstrass theorem（简称 B-W 定理）是实分析中最重要的紧性结果之一。它的直观含义是：在任何有界序列中，你总能挑出一个收敛的子序列——就像从一堆乱点里总能找出一条趋于某一点的路径。
> 
> 🎥 *Colding 用极简洁的语言陈述:* "the Bolzano-Weierstrass theorem says that every bounded sequence has a convergent subsequence."（翻译：波尔查诺-魏尔斯特拉斯定理说，每个有界序列都有一个收敛子列。）没有任何符号，纯粹用英语句子，强调这是一个存在性工具。
> 
> 注意讲义中的幽默：Colding 先陈述 B-W 定理，然后用它来证明 Cauchy convergence theorem——但 B-W 的证明要等到下一讲（L07）。🎥 *他坦诚地说:* "we're going to cheat just a little bit, because we are going to deduce it from another theorem that I will prove next time."（翻译：我们要稍微作弊一下，因为我们要用另一个定理来推导它，那个定理我下周才会证明。）这种「先给工具再证工具」的迂回策略让学生先看到全局画面，是 MIT 数学课常见的教学技巧。
> 
> B-W 定理的证明思路（L07 会详细讲）：利用实数的 completeness（完备性），通过不断二分区间的方法（nested interval / bisection method）构造收敛子列。你在 6.006 算法导论中学过的二分搜索（binary search）思想与此同出一源——每次把搜索空间减半。B-W 定理本质上是一个「无限二分」的过程：由于序列有无穷多项，至少有一半区间包含无穷多项，不断取那一半即可。

---

### <span style="color:#2471a3;">**[proof]**</span> <span style="color:#c0392b;">Proof of the Cauchy Convergence Theorem（柯西收敛定理的证明）</span>

有了 Bolzano-Weierstrass theorem（波尔查诺-魏尔斯特拉斯定理），我们就可以证明 Cauchy convergence theorem（柯西收敛定理）。

> <span style="color:#7f8c8d;">TBB §2.11, p.75</span>

**Proof（证明）.** 假设 $a_n$ 是 Cauchy sequence（柯西序列）。

**第一步：证明 $a_n$ 有界。** 由 Cauchy 序列的定义，存在 $N$，使得对 $m, n \ge N$，有

```math
|a_n - a_m| < 1.
```

特别地，对所有 $n \ge N$，有

```math
|a_n - a_N| < 1,
```

因此

```math
|a_n| = |(a_n - a_N) + a_N| \le 1 + |a_N|.
```

于是

```math
|a_n| \le \max \{|a_N| + 1, |a_1|, \cdots, |a_{N-1}|\}.
```

所以序列有界。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 第一步「Cauchy ⇒ 有界」是一个精妙的技巧。核心思路：由于 Cauchy 条件对**任意** $\epsilon$ 都成立，我们直接**取 $\epsilon = 1$**（一个具体的数）来获得一个「粗糙」的有界估计。$N$ 由 Cauchy 定义保证存在。对于 $n \ge N$（尾部），所有项满足 $|a_n| \le |a_N| + 1$；对于 $n < N$（前面有限项），直接取有限个数的最大值。最终用 $\max$ 统一上界。
> 
> 🎥 *Colding 在视频中特别强调这个技巧:* "in the definition of it being a Cauchy sequence, you can take epsilon to be equal to 1."（翻译：在柯西序列的定义中，你可以取 epsilon 等于 1。）这句话的精髓在于：**Cauchy 条件的威力不在于对某个特定的 epsilon 成立，而在于它对所有 epsilon 都成立**——这意味着你可以任意挑选一个方便的 epsilon（这里挑 1）来工作。
> 
> 这个证明策略可以命名为「**具体化 epsilon 技巧**」：当你只需要「存在某个上界」而不在乎它有多精确时，Cauchy 条件让你可以随意固定一个 epsilon 值。这种「从任意到具体」的降维打击在分析证明中反复出现。

**第二步：用 Bolzano-Weierstrass 取收敛子列。** 由 Bolzano-Weierstrass theorem，$a_n$ 有一个 convergent subsequence（收敛子列）$a_{n_k}$，记其 limit（极限）为 $a$。

**第三步：证明原序列也收敛到 $a$。** 我们需要证明 $a_n \to a$。

给定 $\epsilon > 0$，存在 $N_1$，使得当 $m, n \ge N_1$ 时，

```math
|a_n - a_m| < \frac{\epsilon}{2}.
```

（这是 Cauchy 条件的直接应用——取 $\epsilon/2$ 作为 Cauchy 定义中的 $\epsilon$。）

此外，存在 $N_2$，使得当 $k \ge N_2$ 时，$|a_{n_k} - a| < \frac{\epsilon}{2}$。

令 $N = \max\{N_1, N_2\}$。则当 $n \ge N$ 且 $k \ge N$ 时，

```math
|a_n - a| \le |a_n - a_{n_k}| + |a_{n_k} - a| < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon.
```

这证明了 $a_n \to a$，即序列收敛。$\square$

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 第三步是整个证明的精华所在，使用的策略可以命名为「**ε/2 三角夹逼法**」——这是分析学中最常用的证明模板之一。拆解如下：
> 
> **策略模板：「ε/2 三角夹逼法」**
> 
> **(1) 识别三个对象**：目标项 $a_n$、已知收敛的参考项 $a_{n_k}$（子列）、极限 $a$。
> 
> **(2) 拆分为两段**：$|a_n - a| \le |a_n - a_{n_k}| + |a_{n_k} - a|$。第一段由 Cauchy 条件控制（全序列内部靠近），第二段由子列收敛控制（子列趋近极限）。
> 
> **(3) 各分配 ε/2**：Cauchy 条件保证第一段 $< \epsilon/2$（对所有足够大的 $n, n_k$）；子列收敛保证第二段 $< \epsilon/2$（对所有足够大的 $k$）。两段之和 $< \epsilon$。
> 
> 为什么要用 ε/2 而不是 ε？因为三角不等式会产生两段距离的和——如果两段各用 ε，那么总和 $< 2\epsilon$，虽然也能推出收敛（只需在最后缩放），但在证明的流畅度上不如直接分配 ε/2。🎥 *Colding 在视频中一步步展示:* 先用 Cauchy 定义得到 $|a_n - a_m| < \epsilon/2$，再用子列收敛得到 $|a_{n_k} - a| < \epsilon/2$，然后三角不等式相加。
> 
> 这个「ε/2 技巧」在实分析中会出现无数次——从极限的唯一性、极限的代数运算到一致收敛的证明，它是处理「同时存在多个逼近源」问题的标准手法。你在 L04 的极限代数性质证明中已经见过类似的思想。
> 
> 整个 Cauchy 收敛定理的证明可以概括为三步走的「战略」：
> 
> 1. Cauchy ⇒ 有界（「具体化 epsilon 技巧」）
> 2. 有界 ⇒ 有收敛子列（Bolzano-Weierstrass 定理）
> 3. Cauchy + 有收敛子列 ⇒ 原序列收敛到同一极限（「ε/2 三角夹逼法」）
> 
> 这三步各自独立，组合起来形成了实分析中最优雅的「存在性证明」之一：**你不需要事先知道极限是什么**（与 MCT 不同），仅从序列内部的一致性就能确保极限的存在。

---

### <span style="color:#2471a3;">**[application]**</span> <span style="color:#c0392b;">Another Application of Bolzano-Weierstrass: Extreme Value Theorem（波尔查诺-魏尔斯特拉斯定理的另一个应用：极值定理）</span>

在陈述 Extreme value theorem（极值定理）之前，我们需要另一个关键概念。

> <span style="color:#7f8c8d;">TBB §5.1, p.215 & §5.6, p.250</span>

---

### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f;">**Continuity（连续性）**</span>

函数 $f : \mathbb{R} \to \mathbb{R}$ 称为在点 $x_0 \in \mathbb{R}$ **continuous（连续）**，如果对任意 $\epsilon > 0$，存在 $\delta > 0$，使得当

```math
|x - x_0| < \delta \implies |f(x) - f(x_0)| < \epsilon.
```

一个函数称为 **continuous（连续的）**，如果它在定义域中的每一点都 continuous（连续）。

> <span style="color:#7f8c8d;">TBB §5.1, p.215</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 连续性的 $\epsilon$-$\delta$ 定义是实分析中最重要的定义之一。讲义中只给出了形式化定义，但在视频中 Colding 用画图的方式给出了精彩的直觉解释。
> 
> 🎥 *Colding 边画图边解释:* "If you take a little interval around here — this is an epsilon interval — around here, then there should be some delta interval around here so that if you're looking at images here, then it will map into here. That's what it means to be continuous."（翻译：如果你在这里取一个小区间——这是一个epsilon区间——在这周围，那么应该存在某个delta区间在这周围，使得如果你看这里的像，它们会映射到这里面。这就是连续的含义。）
> 
> 这个直觉可以总结为「小框框测试」：**任何以 $f(x_0)$ 为中心、高度为 $2\epsilon$ 的水平带，都能找到一个以 $x_0$ 为中心、宽度为 $2\delta$ 的竖直带，使得函数图像在该竖带内的部分完全落在水平带内。** 换句话说：输入的小变化只产生输出的小变化。
> 
> 对比你在 L04-L05 学过的**序列收敛的 $\epsilon$-$N$ 定义**：$|a_n - a| < \epsilon$ 对所有 $n \ge N$。两者结构完全相同（$\forall \epsilon > 0, \exists \text{阈值}, \forall \text{足够接近} \ldots$），区别在于：(1) 序列用的是 $N$（自然数阈值），连续用的是 $\delta$（实数阈值）；(2) 序列的 $a_n$ 只与 $n$ 有关，连续的 $f(x)$ 对所有满足 $|x-x_0|<\delta$ 的 $x$ 都要成立（即在整个邻域内成立，而非仅在离散点上）。这种结构性对应是分析学中「序列语言」与「函数语言」之间的翻译表。
> 
> 你在 CSAPP 中见过的 floating-point（浮点数）的连续性问题是另一个交叉连接：浮点运算不连续（$a + b$ 可能需要舍入），而实数运算连续——这正是数值分析中误差分析的基础。

---

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">Sequential Continuity（序列连续性）</span>

若 $f : \mathbb{R} \to \mathbb{R}$ 是 continuous（连续的），且 $x_n$ 是满足 $x_n \to x_0$ 的序列，则 $f(x_n) \to f(x_0)$。

> <span style="color:#7f8c8d;">TBB §5.1, p.217</span>

**Proof（证明）.** 给定 $\epsilon > 0$。由于 $f$ 连续，存在 $\delta > 0$，使得当 $|x - x_0| < \delta$ 时，$|f(x) - f(x_0)| < \epsilon$。由于 $x_n \to x_0$，存在 $N$，使得当 $n \ge N$ 时，$|x_n - x_0| < \delta$，因此 $|f(x_n) - f(x_0)| < \epsilon$。这证明了 $f(x_n) \to f(x_0)$。$\square$

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这个定理建立了 $\epsilon$-$\delta$ 连续性定义与序列收敛之间的桥梁，在分析学中被称为 **sequential continuity（序列连续性）**。证明极其简洁——几乎是「用序列收敛定义中的 $N$ 替换了连续定义中的 $\delta$」：
> 
> 1. 连续性给你 $\delta$：$\forall \epsilon, \exists \delta$ 使得「输入距离 $< \delta$ ⇒ 输出距离 $< \epsilon$」
> 2. 序列收敛给你 $N$：$\exists N$ 使得「$n \ge N$ ⇒ 输入距离 $< \delta$」
> 3. 链式传递：$n \ge N$ ⇒ $|x_n - x_0| < \delta$（从2）⇒ $|f(x_n) - f(x_0)| < \epsilon$（从1）
> 
> 这个证明体现了分析学中的「层叠式逻辑」（cascading logic）：每个定义提供一个阈值（$\delta$ 或 $N$），然后在一串 $\forall\exists$ 语句中传递。这种推理模式在后续课程中会越来越频繁地出现。
> 
> 这个定理还意味着：在 $\mathbb{R}$ 上，$\epsilon$-$\delta$ 连续性和序列连续性是**等价的**（逆命题也成立，但需要稍复杂的论证）。在更一般的拓扑空间中，这两种连续性的等价性不一定成立——这是 point-set topology（点集拓扑）的起点。不过对目前而言，只需记住：连续函数保持序列的收敛性。

---

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">Extreme Value Theorem（极值定理）</span>

设 $f$ 是区间 $[a, b]$ 上的连续函数。Extreme value theorem（极值定理）断言：**supremum（上确界）和 infimum（下确界）被达到**。即存在 $x \in [a, b]$ 使得 $f(x) = \sup f$；同理，存在 $x \in [a, b]$ 使得 $f(x) = \inf f$。

> <span style="color:#7f8c8d;">TBB §5.6, p.250</span>

**Proof（证明）.** 我们证明 supremum（上确界）被达到。infimum（下确界）的证明只需做明显的对称修改即可。

取序列 $x_n \in [a, b]$，使得 $f(x_n) \to \sup f$。

由于该序列包含在 $[a, b]$ 中，它是有界的，因此由 Bolzano-Weierstrass theorem（波尔查诺-魏尔斯特拉斯定理），存在 convergent subsequence（收敛子列）$x_{n_k} \to x$。注意 $x \in [a, b]$。

由上面的定理（连续函数保持序列收敛），有 $f(x_{n_k}) \to f(x)$。又因为 $f(x_{n_k}) \to \sup f$（作为 $f(x_n) \to \sup f$ 的子列），由极限的唯一性，得 $\sup f = f(x)$。

这证明了 supremum（上确界）被达到。$\square$

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 极值定理的证明是本节三个核心定理（Contracting mapping theorem → Cauchy convergence theorem → Extreme value theorem）的逻辑终点，可以看作前面所有工具的「集大成应用」。拆解证明结构：
> 
> **证明策略模板：「确界可达性论证」（Supremum Attainment Argument）**
> 
> **(1) 构造逼近序列**：由确界的定义，存在序列 $x_n$ 使得 $f(x_n) \to \sup f$。这一步使用了确界的性质——确界不一定是函数值，但总存在函数值无限逼近它。
> 
> **(2) 紧性 ⇒ 子列收敛**：$[a, b]$ 是有界闭区间，因此 $x_n$ 有界 ⇒ B-W 定理 ⇒ 存在收敛子列 $x_{n_k} \to x$。$x \in [a,b]$ 是因为闭区间包含其所有极限点（闭性）。
> 
> **(3) 连续性传递极限**：$x_{n_k} \to x$，$f$ 连续 ⇒ $f(x_{n_k}) \to f(x)$（连续函数保持收敛）。
> 
> **(4) 极限唯一性闭合**：$f(x_{n_k})$ 有两个极限：一是 $f(x)$（从连续性），二是 $\sup f$（从构造——子列的极限与原序列相同）。由极限的唯一性，$f(x) = \sup f$，即确界被达到。
> 
> 这个证明包含了本节几乎所有核心工具：确界、有界序列、B-W 定理、子列收敛、连续性、极限唯一性——一个完美的「综合复习」。🎥 *Colding 在视频中把这个定理作为 Cauchy convergence theorem 的第二个重大应用来呈现，强调理论体系的一体性。*
> 
> 注意证明中一个关键条件：**$[a, b]$ 是闭区间**。如果换成开区间 $(a, b)$，$x_{n_k}$ 的极限 $x$ 可能等于端点 $a$ 或 $b$，此时 $x \notin (a,b)$——函数在开区间上的 supremum 不一定能被达到。例如 $f(x) = x$ 在 $(0,1)$ 上的 supremum 是 $1$，但 $1$ 不是任何 $x \in (0,1)$ 的函数值。这解释了为什么 EVT 要求「闭区间」——闭性保证了极限点仍在定义域内。
> 
> 这个定理在 CSAPP 中没有直接对应，但它与优化理论（你在凸优化 Boyd 中会见到）有深刻联系：EVT 保证了连续函数在紧集上**一定存在最大值和最小值**——这是所有优化算法寻找最优解的理论基础。没有 EVT，你永远不知道最值是否真的存在。

---

## <span style="color:#2471a3;">**[reference]**</span> <span style="color:#7f8c8d;">References（参考文献）</span>

[TBB] B.S. Thomson, J.B. Bruckner, and A.M. Bruckner, *Elementary Real Analysis*, 2nd edition

TBB 可下载于：

- [Landscape（横版，屏幕优化）](https://classicalrealanalysis.info/com/documents/TBB-AllChapters-Landscape.pdf)
- [Portrait（竖版，打印优化）](https://classicalrealanalysis.info/com/documents/TBB-AllChapters-Portrait.pdf)

<span style="color:#7f8c8d;">MIT, Dept. of Math., 77 Massachusetts Avenue, Cambridge, MA 02139-4307.</span>

---

<span style="color:#7f8c8d;">*MIT OpenCourseWare · 18.100B Real Analysis · Spring 2025 · https://ocw.mit.edu*</span>
