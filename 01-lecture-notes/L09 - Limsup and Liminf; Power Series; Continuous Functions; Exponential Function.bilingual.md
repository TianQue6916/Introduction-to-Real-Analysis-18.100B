# 18.100B / 18.1002 Real Analysis（实分析）

## <span style="color:#c0392b">Lecture 9 — Limsup and Liminf; Power Series; Continuous Functions; Exponential Function（上极限与下极限；幂级数；连续函数；指数函数）</span>

<span style="color:#7f8c8d;">Instructor: Tobias Holck Colding · Spring 2025 · MIT</span>

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Power series（幂级数）</span>

假设 $a_n$ 是一个 sequence（序列），那么对每一个 $x$ 我们都可以构造一个级数

```math
\sum_{n=0}^{\infty} a_n x^n .
```

> <span style="color:#7f8c8d;">TBB §10.2, p.404</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 讲义标题虽然包含 "Limsup and Liminf"，但上极限与下极限的定义以及 Cauchy–Hadamard 收敛半径公式已经在你刚学完的 L08 中完整覆盖。本讲实际上是从幂级数的应用出发，进入指数函数的具体构造。幂级数 $\sum a_n x^n$ 的直觉可以这样建立：对每一个固定的 $x$，它就是你在 L05–L07 中已经熟练掌握的普通数值级数——$x$ 在这里扮演"参数"的角色，每换一个 $x$ 就得到一个新级数。你在 L06 学过的比值检验和根值检验就是用来逐个判断这些级数是否收敛的工具，而 L08 的 lim sup 版本则一次性刻画了所有 $x$ 的收敛范围——收敛半径 $R$。本讲选取 $a_n = 1/n!$ 这个特例，展示如何从收敛性一步步走到指数函数的完整定义：先证明对所有 $x$ 都收敛（Step 0），再定义 $e$ 并推广到有理数幂（Step 1），最后用连续性填平有理数与无理数之间的鸿沟（Step 3–4）。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Exponential map as a power series（指数映射的幂级数定义）</span>

将 **exponential map（指数映射）** 定义为幂级数

```math
E(x) = \sum_{n=0}^{\infty} \frac{x^n}{n!} .
```

> <span style="color:#7f8c8d;">TBB §5.2, p.201</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 指数函数至少有三种经典的定义方式。第一种是把它定义为微分方程 $y' = y$ 且满足 $y(0) = 1$ 的唯一解——这个思路你会在后续的 ODE 课程中系统学习。第二种是极限定义 $e^x = \lim_{n\to\infty} (1 + x/n)^n$，直觉清晰但严格处理起来比较繁琐。第三种就是本讲采用的幂级数定义 $E(x) = \sum_{n=0}^\infty x^n/n!$，这是从第一性原理出发最"干净"的方式：幂级数在收敛半径内是良定义的（Step 0 已证明半径 $= \infty$），而且它的代数性质——加法变乘法——可以直接从两个幂级数相乘的公式推出，不需要借助任何关于"指数是什么"的已有知识。Colding 在视频中这样解释选择幂级数的理由：🎥 *Colding:* "There's various ways that you could define the exponential function... One is that you could define it to be a function that's satisfying a certain differential equation... Another way of defining it, which is more relevant to what we're doing here, is defining it as a power series."（翻译：定义指数函数有多种方式……一种是将它定义为满足某个微分方程的函数……另一种与我们当前内容更相关的做法，是把它定义为幂级数。）预告一下：L22 将系统讨论幂级数的逐项微分和逐项积分，届时你可以用微积分工具重新审视这个定义，看到幂级数定义如何自然地与微分方程定义统一。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Step 0: 幂级数对所有 $x$ 收敛</span>

**Step 0:** 这个幂级数对一切 $x$ 都收敛。因为代入 $a_n = \frac{1}{n!}$ 后，

```math
\frac{|a_{n+1} x^{n+1}|}{|a_n x^n|} = \frac{|n! \, x^{n+1}|}{|(n+1)! \, x^n|} = \frac{|x|}{n+1} \to 0,
```

所以由 **ratio test（比值检验）** 立刻得出论断：这个幂级数对一切 $x$ 收敛。

> <span style="color:#7f8c8d;">TBB §3.6.5, p.100（d'Alembert's Ratio Test）</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 讲义中 Step 0 的推导写的是 $\frac{x}{n+1} \to 0$，这里省略了绝对值符号——比值检验要求的是 $|\frac{a_{n+1}}{a_n}|$，所以严谨写法应该是 $\frac{|x|}{n+1} \to 0$。不过因为极限是 $0$，绝对值号不影响结论，讲义为了书写简洁做了省略。$\frac{|x|}{n+1} \to 0$ 这个事实背后藏着一个重要的增长阶比较：对任意固定的 $x$，$n!$ 的增长速度远快于 $|x|^n$。你在 CSAPP 和 CLRS 里已经接触过复杂度记号：阶乘增长 $\Theta(n!)$ 碾压指数 $\Theta(c^n)$，指数又碾压多项式 $\Theta(n^k)$——这里的 $|x|^n/n! \to 0$ 正是"阶乘比指数快"在级数项上的体现，所以无论 $x$ 多大，通项最终都会衰减到零。因此收敛半径 $R = \infty$，$E(x)$ 对所有实数 $x$ 都是良定义的——不管 $x$ 取什么值，级数都收敛到一个确定的实数。🎥 *Colding 也强调了这一点:* "And we know already... that the radius of convergence for this power series... is equal to infinity. We have already seen that, so it's a well-defined function for all x."（翻译：我们已经知道这个幂级数的收敛半径等于无穷大，我们已经看到过这一点，所以它对所有 $x$ 都是一个良定义的函数。）

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Step 1: 定义 $e$ 的整数幂与有理数幂</span>

**Step 1:** 定义 $e = E(1)$，再定义 $e^2 = e \cdot e$、$e^3 = e \cdot e \cdot e$ 等等。这样 $e^k$ 就对一切 $k \in \mathbb{N}$ 都有了定义。

我们还定义 $e^{-k} = \frac{1}{e^k}$。（背后的想法是：我们希望有 $e^{x+y} = e^x e^y$。）

我们规定 $e^0 = 1$。

如果 $q = \frac{m}{n} \in \mathbb{Q}$，其中 $m \in \mathbb{Z}$ 而 $n \in \mathbb{N}$，那么我们就令 $e^q$ 为满足 $\alpha^n = e^m$ 的那个正数 $\alpha$。（再次说明，想法仍是：我们希望有 $e^{x+y} = e^x e^y$。）

这样 $e^q$ 就对一切 rational number（有理数）都有了定义。

那像 $\sqrt{2}$ 这样的 irrational number（无理数）怎么办？

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 注意 Colding 在这里采用的是一种"逆向工程"的逻辑：他先用幂级数定义了 $E(x)$（这个定义本身不需要任何关于"指数"的先验概念），然后令 $e = E(1)$，再以"我们希望 $e^{x+y} = e^x e^y$ 成立"为设计目标，逐步定义 $e$ 的整数幂、负幂、有理数幂。对有理数 $q = m/n$，他把 $e^q$ 定义为满足 $\alpha^n = e^m$ 的唯一正数 $\alpha$——这里用到了一个关键事实：正数的 $n$ 次方根是唯一的。这个唯一性由幂函数 $x \mapsto x^n$ 在 $(0, \infty)$ 上的严格单调递增保证（每个正实数有且仅有一个正 $n$ 次方根），你在中学数学中习以为常，但其严格证明需要实数的完备性——这一事实将在后续课程中正式建立。有理数范围的定义完成了，但 $\sqrt{2}$ 这样的无理数怎么办？$2^{\sqrt{2}}$ 是什么意思？我们无法再用"满足 $\alpha^n = e^m$ 的 $\alpha$"这种形式来定义，因为 $\sqrt{2}$ 不是 $m/n$ 的形式。这就是 Step 3 需要连续性/极限来填补的鸿沟——连续性是把有理数定义延拓到全实数的桥梁。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Step 2: $E(x) > 0$</span>

**Step 2:** 下一次课我们将证明

```math
E(x + y) = E(x) E(y) .
```

这里我们先断言：对所有 $x$ 都有 $E(x) > 0$。如果 $x \ge 0$，那么这是显然的，因为

```math
E(x) = 1 + \frac{x}{1!} + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots \ge 1.
```

如果 $x < 0$，那么利用我们下一次课将要证明的公式，有

```math
1 = E(0) = E(x) E(-x) .
```

因此

```math
E(x) = \frac{1}{E(-x)} > 0.
```

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> $E(x) > 0$ 的证明结构值得仔细拆解，它是一个分段论证的范本。当 $x \ge 0$ 时，直接看级数：$E(x) = 1 + x/1! + x^2/2! + \cdots$，每一项都非负，且第一项是 $1$，所以和 $\ge 1 > 0$，结论唾手可得。当 $x < 0$ 时，级数中正负项交错出现，直接判断和的正负变得困难。🎥 *Colding 在视频中坦然承认了这一困境:* "Now if x is negative, then it's not super clear... some of these numbers that you'll be summing are positive and some of them are negative, so it's not at all clear what happened to the sum."（翻译：如果 $x$ 是负数，情况就不那么清楚了……你求和的一些项是正的一些项是负的，所以完全不清楚级数的和会是什么情况。）于是他转而使用 $E(x)E(-x) = 1$ 这个乘法公式——注意，这个公式是"下一次课才证明"的！这里采用的是一种重要的证明策略模板：先假定一个稍后再证的命题成立，用它来推出当前的结论。我把这种手法命名为"前瞻借用"——在讲义中先给出结论，再在下一次课补上它所依赖的前提的证明。这种顺序在教学中常见：先把整个论证链条的大图景展示出来，再回头填每一个坑。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">$E(q) = e^q$ 对一切有理数成立</span>

利用 $E(x + y) = E(x) E(y)$，我们现在断言：对一切 rational number $q$ 都有 $E(q) = e^q$。

对整数 $m$ 来说，这正是我们定义 $e^m$ 的方式。对 $m = -k$（其中 $k \in \mathbb{N}$），我们定义过

```math
e^{-k} = \frac{1}{e^k} = \frac{1}{E(k)} = E(-k) .
```

对一般的有理数 $q = \frac{m}{n}$，其中 $m \in \mathbb{N}$ 而 $n \in \mathbb{Z}$，我们有

```math
\left( E\left( \frac{m}{n} \right) \right)^n = E\left( \frac{m}{n} \right) \cdots E\left( \frac{m}{n} \right) = E(m) ,
```

并且

```math
E\left( \frac{m}{n} \right) > 0.
```

由此可知：对一切有理数 $q$ 都有 $E(q) = e^q$。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> $E(q) = e^q$ 的证明构成一个清晰的三层递进结构。第一层——正整数 $m$：直接由 $e^m$ 的定义（$e$ 自乘 $m$ 次）和 $E$ 的乘法公式 $E(m) = E(1)^m = e^m$ 得到，这是整个链条的底座。第二层——负整数 $-k$：利用 $E(-k)E(k) = E(0) = 1$ 和 $e^{-k} = 1/e^k$ 的定义完成对接，本质上是用乘法公式把负指数的定义"翻译"成 $E$ 的语言。第三层——一般有理数 $m/n$：$(E(m/n))^n = E(m/n) \cdots E(m/n) = E(m) = e^m$，同时 $E(m/n) > 0$（Step 2 的结果），所以 $E(m/n)$ 是一个正数，它的 $n$ 次幂等于 $e^m$。但 $e^{m/n}$ 的定义正是"满足 $\alpha^n = e^m$ 的那个唯一正数 $\alpha$"——由正数 $n$ 次方根的唯一性，$E(m/n)$ 只能是这个 $\alpha$。注意"唯一性"在这条证明链中扮演了关键角色：如果正 $n$ 次方根不唯一，$E(m/n)$ 就可能不是 $e^q$，整个对接就会失败。这个三层结构是一个可迁移的证明模板：从自然数出发，用代数恒等式推广到整数，再用唯一性定理推广到有理数。（另注意：讲义此处写作 $m \in \mathbb{N}$、$n \in \mathbb{Z}$，与 Step 1 中 $m \in \mathbb{Z}$、$n \in \mathbb{N}$ 的记法不一致——分母 $n$ 严格说应为正整数，这是讲义的一处笔误，不影响论证。）

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Step 3: 我们还想要指数函数有什么性质？</span>

**Step 3:** 到目前为止我们已知：$E(x)$ 对一切 $x$ 都有定义，而 $e^x$ 仅对所有有理数有定义。

我们还希望 exponential function（指数函数）有其他什么性质呢？

我们希望它是 **continuous（连续）** 的！

**Reminder（回顾）:** 一个定义在某个集合 $A \subset \mathbb{R}$ 上的函数 $f : A \to \mathbb{R}$ 被称为连续的，如果对一切 $x_0 \in A$ 都有：

对任意 $\varepsilon > 0$，存在 $\delta = \delta(x_0) > 0$，使得如果 $|x - x_0| < \delta$（且 $x \in A$），则 $|f(x) - f(x_0)| < \varepsilon$。

> <span style="color:#7f8c8d;">TBB §5.4, p.207</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> $\varepsilon$-$\delta$ 定义的直觉可以用一句话概括：输入在 $x_0$ 附近抖动不超过 $\delta$，则输出在 $f(x_0)$ 附近抖动不超过 $\varepsilon$。这里的 $\delta$ 被标注为 $\delta(x_0)$ 是有深意的——它依赖于你选的那个点 $x_0$，这是"逐点连续"的标志：不同点可能需要不同的 $\delta$ 来达到同样的 $\varepsilon$ 精度。后续课程会引入"一致连续"的概念，即存在一个与 $x_0$ 无关的 $\delta$ 对全定义域统一适用，届时你会看到逐点连续和一致连续的关键区别（例如 $f(x) = 1/x$ 在 $(0,1)$ 上逐点连续但不一致连续）。与你 L04 学过的序列收敛的 $\varepsilon$-$N$ 定义做类比很有启发：$\varepsilon$ 在两个定义里都是"容差"，$N$（序列情形）和 $\delta$（函数情形）都是"找到合适的阈值以保证容差被满足"。你还可以用 CLRS 中二分搜索的终止条件或 CSAPP 中浮点运算的误差容限来建立直觉：给定一个允许误差范围 $\varepsilon$，你需要找到让算法在这个范围内工作的参数。

在 **Pset 5** 中，你将证明 $E(x)$ 在一切点都连续。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Pset 5 要求你证明 $E(x)$ 在一切点都连续——这个习题不是孤立的计算练习，而是整个讲义论证链条中的关键一环。回想 Step 1 的结尾：$e^q$ 只对有理数 $q$ 有定义，无理数（如 $\sqrt{2}$）的指数还悬而未决。连续性的作用正是填补这个鸿沟：一旦 $E(x)$ 被证明是连续的，它就在所有实数上被有理数上的取值唯一确定了——这正是 Step 4 的 $f = g$ 定理的精髓。证明 $E$ 的连续性可以从本讲已有的工具出发：利用乘法公式 $E(x+y) = E(x)E(y)$，先证明 $E$ 在 $0$ 点连续（即 $E(x) \to 1$ 当 $x \to 0$），再把任意点 $x_0$ 的连续性化归到 $0$ 点（$E(x) - E(x_0) = E(x_0)(E(x-x_0) - 1)$）。也可以走"幂级数路线"：本讲 Step 0 已证明幂级数对一切 $x$ 收敛，而幂级数的连续性定理（在收敛区间内幂级数定义的函数连续）在后续讲义中会正式建立，届时这也是一条干净的路。做 Pset 5 之前不妨先翻回 Step 0–3，把已有的 $E$ 的性质梳理一遍再动手。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Step 4: 唯一性定理的预告</span>

**Step 4:** 我们下一步将证明：$E(x)$ 是唯一的 continuous function（连续函数），它满足对一切 rational number $q$ 都有 $E(q) = e^q$。

**Theorem（定理）:** 设 $f$ 和 $g$ 是 $\mathbb{R}$ 上的两个连续函数，它们在所有有理数上取值一致，则 $f = g$。

> <span style="color:#7f8c8d;">TBB §5.4, p.207</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这个"$f = g$"定理的威力远超它看起来的简短陈述。它说的是：如果两个连续函数在有理数集 $\mathbb{Q}$ 上取值一致，那么它们在全部实数 $\mathbb{R}$ 上也必须一致。背后的原理是有理数在实数中"足够密"——任意一个实数都可以被一列有理数任意逼近（即 $\mathbb{Q}$ 在 $\mathbb{R}$ 中稠密，稠密性的正式定义和系统讨论将在后续讲义中登场）。连续性把"接近"变成了"相等"：因为 $f$ 和 $g$ 在每一个有理点 $q$ 上都相等，而对任意无理点 $x$，你取一列有理数 $q_n \to x$，由连续性得 $f(x) = \lim f(q_n) = \lim g(q_n) = g(x)$。这是一个可复用的思维模板——**"连续性 + 稠密子集上一致 $\to$ 全局一致"**——以后你在概率论（分布函数由有理点上的值唯一决定）、数值分析（网格点上的值加上连续性决定整个函数）中都会反复遇到。🎥 *Colding 在视频中总结道:* "If f and g are two continuous functions on R that agree on all of Q... If they are both continuous, then the function has to be the same. So this implies that f is equal to g everywhere, not just on the rational numbers."（翻译：如果 $f$ 和 $g$ 是 $\mathbb{R}$ 上的两个连续函数，且在 $\mathbb{Q}$ 的所有点上一致……如果它们都连续，那么这两个函数必须完全相同。这意味着 $f$ 等于 $g$ 在所有点上成立，而不仅仅在有理数上。）

我们将在下一次课证明这个定理。现在先看更多关于"一个函数连续意味着什么"的内容。

---

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 1（例 1）: 常值函数连续</span>

**Example 1:** 设 $f(x) = c$，其中 $c$ 是一个 constant（常值）。我们要证明 $f$ 是连续的。给定 $x_0 \in \mathbb{R}$ 和 $\varepsilon > 0$，取 $\delta = 1$。于是如果 $|x - x_0| < \delta = 1$，那么 $|f(x) - f(x_0)| = 0 < \varepsilon$。这表明 $f$ 是连续的。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 常值函数 $f(x) = c$ 的连续性证明中，Colding 选取 $\delta = 1$。这个选择非常"浪费"——因为 $|f(x) - f(x_0)|$ 恒为 $0$，无论 $x$ 和 $x_0$ 距离多远，误差永远小于任意 $\varepsilon$，所以取 $\delta = 1$、$\delta = 100$、甚至 $\delta = 10^6$ 都行，完全不需要依赖 $\varepsilon$ 和 $x_0$。要点在于：$\varepsilon$-$\delta$ 定义只要求"存在至少一个 $\delta$ 满足条件"，不要求它是最优的、最紧的、或者与 $\varepsilon$ 有某种巧妙的函数关系。这个"存在即可、无需最优"的思想在分析学中反复出现——只要你能找到一个满足条件的 $\delta$，不管它多"不经济"，连续性就成立了。你可以类比算法理论中的情形：只要证明存在一个多项式时间算法，问题就归入复杂度类 P，不需要你的算法常数因子是最优的。🎥 *Colding 也点明了这一点:* "And you see that you could pick delta anything you want, and, of course, in particular, it doesn't even depend on x-0. It doesn't depend on epsilon, and it doesn't depend on x-0."（翻译：你可以看到，你随便取什么 $\delta$ 都可以，而且特别地，它甚至不依赖于 $x_0$，也不依赖于 $\varepsilon$，也不依赖于 $x_0$。）

---

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 2（例 2）: 恒等函数连续</span>

**Example 2:** 设 $f(x) = x$，我们要证明 $f$ 是连续的。给定 $x_0 \in \mathbb{R}$ 和 $\varepsilon > 0$，取 $\delta = \varepsilon$。于是如果 $|x - x_0| < \delta = \varepsilon$，那么 $|f(x) - f(x_0)| = |x - x_0| < \varepsilon$。这表明 $f$ 是连续的。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 恒等函数 $f(x) = x$ 取 $\delta = \varepsilon$ 是"最紧"的取法。因为 $|f(x) - f(x_0)| = |x - x_0|$，恰好要 $\delta \le \varepsilon$ 才能保证误差 $< \varepsilon$，而 $\delta = \varepsilon$ 正好饱和了这个不等式——再大一丝就不成立了。恒等函数可以说是"最诚实"的函数：输入抖动多大，输出就抖动多大，没有任何放大或缩小，$\varepsilon$-$\delta$ 定义在这里"饱和"。把 Example 1（常值函数）和 Example 2（恒等函数）放在一起看，它们构成了连续函数世界的两个"原子构件"：前者对输入完全"不敏感"（$\delta$ 可以任意取，甚至可以与 $\varepsilon$ 和 $x_0$ 都无关），后者对输入"一比一敏感"（$\delta$ 必须恰好等于 $\varepsilon$ 才够紧）。配合下一节列出的代数性质（加法、乘法封闭），从这两个原子出发，你可以拼装出所有多项式——这正是 Example 3 的论证逻辑，也是整个连续函数理论大厦的地基。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Algebraic properties of continuous functions（连续函数的代数性质）</span>

- 如果 $f$ 和 $g$ 都是连续的，那么 $f + g$ 也是连续的。
- 如果 $f$ 是连续的而 $c$ 是常数，那么 $c f$ 是连续的。
- 如果 $f$ 和 $g$ 都是连续的，那么 $f g$ 也是连续的。
- 如果 $f$ 是连续的且 $f \neq 0$，那么 $\frac{1}{f}$ 是连续的。
- 如果 $f$ 和 $g$ 都是连续的，那么 $f(g(x))$ 是连续的。

> <span style="color:#7f8c8d;">TBB §5.5, p.218</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 连续函数的五条代数性质与你在 L04 学过的序列极限的代数性质（和的极限 = 极限的和，积的极限 = 极限的积，等等）形成了完全平行的结构。这并非巧合——函数连续性本身就是通过极限定义的（$\lim_{x \to x_0} f(x) = f(x_0)$），所以极限的代数性质自然"遗传"给了连续函数。🎥 *Colding 明确指出:* "And the proofs are very similar to those proofs for limits of sequences."（翻译：这些证明与序列极限的证明非常相似。）值得特别注意的是第五条——复合函数 $f(g(x))$ 的连续性。这是序列版本中没有与之对应的内容，因为序列是 $\mathbb{N} \to \mathbb{R}$ 的函数，定义域 $\mathbb{N}$ 是离散的，无法在其中再嵌入另一个序列。复合连续性的证明思路本质上是一个"$\varepsilon$-$\delta$ 接力"：先用 $g$ 的连续性把 $x$ 靠近 $x_0$ 转化为 $g(x)$ 靠近 $g(x_0)$，再用 $f$ 的连续性把 $g(x)$ 靠近 $g(x_0)$ 转化为 $f(g(x))$ 靠近 $f(g(x_0))$。和与积的连续性证明中还会用到 $\varepsilon/2$ 技巧——把总误差 $\varepsilon$ 分成两份，分别用两个函数的连续性找到各自的 $\delta$，取两者中较小的那个——下一课会展开。

**Proof（证明）:**（这与我们为 limits（极限）的代数性质给出的证明非常相似。）$\square$

---

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem: All polynomials are continuous（多项式都连续）</span>

**Theorem（定理）:** 所有 polynomial（多项式）都是连续的。

> <span style="color:#7f8c8d;">TBB §5.5, p.218</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> "所有多项式都连续"这个定理是代数性质清单的直接推论——它不是一条需要重新从头证明的独立命题，而是从已有的构件和组合规则推导出来的。证明逻辑是：从常值函数（Example 1，连续）和恒等函数（Example 2，连续）这两个"原子"出发，反复使用加法封闭性（$f+g$ 连续）和乘法封闭性（$fg$ 连续），就可以构造出任意多项式 $a_n x^n + \cdots + a_1 x + a_0$。这正是你熟悉的"构建主义"视角：连续函数类在加法、数乘、乘法这三种代数运算下是封闭的，多项式只是这个封闭性带来的第一个"甜头"。后面你还会看到，有理函数在分母不为零处连续、三角函数连续、指数函数连续——这些结论都遵循同一套"从原子出发，用组合规则搭建"的模板。🎥 *Colding 的总结非常精到:* "And the function x, you can get to any polynomial, and using these operations. And so this means that any polynomial is continuous."（翻译：从恒等函数 $x$ 出发，利用这些运算你可以得到任何多项式，因此任何多项式都是连续的。）你可以类比 CLRS 中的体验：从原子操作出发，用顺序、分支、循环组合出任意复杂度的算法——在这里是从两个原子函数出发，用加法和乘法组合出任意多项式。

---

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 3（例 3）: $f(x) = x^2 + 1$ 连续</span>

**Example 3:** 如果 $f(x) = x^2 + 1$，那么 $f$ 是连续的。我们已经证明过 $g(x) = x$ 是连续的，所以由代数性质可得 $x^2 = g \cdot g$ 是连续的。我们也已经证明常值函数是连续的，所以 $h(x) = 1$ 是连续的，从而由代数性质可得 $f = g^2 + h$ 是连续的。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Example 3 是"拼装演示"的最佳范本：$f(x) = x^2 + 1$ 的连续性证明不需要从 $\varepsilon$-$\delta$ 定义从头硬算，而是分三步调用已建立的性质。第一步，$g(x) = x$ 连续（Example 2，恒等函数已证）。第二步，$g \cdot g = x^2$ 连续（调用乘法封闭性，将 $g$ 与自身相乘）。第三步，$h(x) = 1$ 连续（Example 1，常值函数已证），所以 $g^2 + h = x^2 + 1$ 连续（调用加法封闭性）。每一步都有明确的理论依据，整个论证像搭积木一样层层堆叠，没有任何神秘之处。这个"证明脚手架"模式——把复杂对象的性质分解为简单构件的性质组合——会贯穿整个实分析课程。以后你证明 $\sin x$ 连续时，不会去硬算 $|\sin x - \sin x_0|$，而是利用 $\sin$ 的幂级数定义配合幂级数的连续性定理来推（$\sin$ 的幂级数定义要到幂级数理论完备之后才登场，届时你会有这个工具），或者用三角恒等式加 $\sin x$ 在 $0$ 点的连续性来推。学会识别这种模式，你就不是在背一个个孤立定理，而是在掌握一套可迁移的论证语言——Colding 在视频中逐一写出每一步用到的性质，示范的正是这种系统性的思维方式。

---

<span style="color:#7f8c8d;">References（参考文献）:</span>

- [TBB] B.S. Thomson, J.B. Bruckner, A.M. Bruckner, *Elementary Real Analysis*, 2nd edition
- TBB 下载：<https://classicalrealanalysis.info/com/documents/TBB-AllChapters-Landscape.pdf>（屏幕优化版）/ <https://classicalrealanalysis.info/com/documents/TBB-AllChapters-Portrait.pdf>（打印优化版）

<span style="color:#7f8c8d;">MIT, Dept. of Math., 77 Massachusetts Avenue, Cambridge, MA 02139-4307 · MIT OpenCourseWare: https://ocw.mit.edu · 18.100B Real Analysis, Spring 2025</span>
