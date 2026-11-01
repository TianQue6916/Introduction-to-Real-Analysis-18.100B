# 18.100B / 18.1002 Real Analysis（实分析）

## <span style="color:#c0392b">Lecture 5 — Monotone Convergence Theorem（单调收敛定理）</span>

<span style="color:#7f8c8d;">Instructor: Tobias Holck Colding · Spring 2025 · MIT</span>

---

<span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f;">**Definition（定义）: Sequence（序列）**</span>

一个 **sequence of real numbers（实数序列）** 是一个函数 $f : \mathbb{N} \to \mathbb{R}$。

我们通常使用记号 $a_n = f(n)$。

---

<span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f;">**Definition（定义）: Limit（极限）**</span>

设 $\{a_n\}$ 是一个 sequence（序列），$a$ 是一个实数。我们说 $a_n$ **converges（收敛）** 到 $a$，如果对任意 $\epsilon > 0$，存在 $N \in \mathbb{N}$，使得当 $n \ge N$ 时，有

```math
|a_n - a| < \epsilon.
```

如果收敛成立，则称 $a$ 是序列的 **limit（极限）**，并称该序列是 **convergent（收敛的）**。不收敛的序列称为 **divergent（发散的）**。

---

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**Theorem（定理）: Convergent Sequence is Bounded（收敛序列必有界）**</span>

若 $\{a_n\}$ 是 convergent sequence（收敛序列），则集合 $\{a_n\}$ 是 $\mathbb{R}$ 的 **bounded subset（有界子集）**。

---

### <span style="color:#2471a3;">**[property]**</span> <span style="color:#c0392b;">**Algebraic Properties of Limits（极限的代数性质）**</span>

<span style="color:#2471a3;">**[theorem]**</span> **Theorem（定理）.** 设 $\{a_n\}$ 和 $\{b_n\}$ 是 convergent sequences（收敛序列），且 $\lim a_n = a$，$\lim b_n = b$，$C \in \mathbb{R}$。则：

1. **Scalar multiplication（数乘）:** $c_n = C a_n$ 收敛，且 $\displaystyle\lim_{n\to\infty} c_n = C a$。
2. **Addition（加法）:** $c_n = a_n + b_n$ 收敛，且 $\displaystyle\lim_{n\to\infty} c_n = a + b$。
3. **Multiplication（乘法）:** $c_n = a_n b_n$ 收敛，且 $\displaystyle\lim_{n\to\infty} c_n = a b$。
4. **Reciprocal（倒数）:** 若 $b_n \neq 0$ 且 $b \neq 0$，则 $c_n = \frac1{b_n}$ 收敛，且 $\displaystyle\lim_{n\to\infty} c_n = \frac1b$。

---

<span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f;">**Definition（定义）: Subsequence（子列）**</span>

序列 $\{b_k\}$ 称为序列 $\{a_n\}$ 的一个 **subsequence（子列）**，如果它是函数的复合 $f \circ g$，其中 $g : \mathbb{N} \to \mathbb{N}$ 是 **strictly increasing function（严格递增函数）**。即 $b_k = f(g(k))$。我们常将 $b_k$ 写作 $a_{n_k}$。

---

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b;">**Example（例）**</span>

**例 1.** 定义序列 

```math
a_n = \frac{n^2 + 1}{n^2 + n + 1}.
```

我们将证明 $a_n$ 收敛且极限为 $1$。我们有

```math
a_n = \frac{1 + \frac1{n^2}}{1 + \frac1n + \frac1{n^2}}.
```

由于 $\frac1n \to 0$ 且 $\frac1{n^2} \to 0$，可得

```math
1 + \frac1{n^2} \to 1 \quad\text{且}\quad 1 + \frac1n + \frac1{n^2} \to 1.
```

由极限的代数性质，$a_n \to 1$。

---

**例 2.** 要证明 $\sqrt{2}$ 是序列 $a_1 = 1,\ a_2 = 1.4,\ a_3 = 1.41,\ a_4 = 1.414,\ \ldots$ 的极限，需要其他工具——我们需要 **Monotone Convergence Theorem（单调收敛定理）**。

---

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**Monotone Convergence Theorem（单调收敛定理）**</span>

**递增版本.** 设 $\{a_n\}$ 是 **monotone increasing sequence（单调递增序列）**，即 $a_1 \le a_2 \le a_3 \le \cdots$（也可写作 $a_n \le a_{n+1}$）。若该序列 **bounded from above（上有界）**，即存在 $A$ 使得 $a_n \le A$ 对所有 $n$ 成立，则 $\{a_n\}$ 收敛，且

```math
\lim_{n\to\infty} a_n = \sup \{a_n\}.
```

---

**递减版本.** 类似地，对于 **monotone decreasing sequence（单调递减序列）** $\{a_n\}$（即 $a_{n+1} \le a_n$），若其下有界，则 $\{a_n\}$ 收敛，且

```math
\lim_{n\to\infty} a_n = \inf \{a_n\}.
```

---

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b;">**Example: $\sqrt{2}$ 的十进制逼近**</span>

利用 Monotone Convergence Theorem（单调收敛定理），我们可以证明 $\sqrt{2}$ 是 $a_1 = 1,\ a_2 = 1.4,\ a_3 = 1.41,\ a_4 = 1.414,\ \ldots$ 的极限。

论证如下：

设

```math
a_n = \frac{b_n}{10^{n-1}},
```

其中 $b_n$ 是满足 $b_n^2 \le 2 \cdot 10^{2n-2}$ 的最大整数。

我们将证明 $\{a_n\}$ 是 increasing and bounded sequence（递增且有界序列），且极限 $a$ 满足 $a^2 = 2$。

假设 $b_n$ 是满足 $b_n^2 \le 2 \cdot 10^{2n-2}$ 的整数，那么显然

```math
(10 b_n)^2 \le 2 \cdot 10^{2(n+1)-2}.
```

这意味着 $b_{n+1} \ge 10 b_n$，因此 $a_{n+1} \ge a_n$，序列递增。

由于 $(2 \cdot 10^{n-1})^2 > 2 \cdot 10^{2n-2}$，显然 $b_n \le 2 \cdot 10^{n-1}$。

因此序列 $a_n = \frac{b_n}{10^{n-1}}$ 有界，由 Monotone Convergence Theorem（单调收敛定理），$a_n \to a$。

---

为证明 $a^2 = 2$，论证如下：

由极限的代数性质，$a^2 = \lim_{n\to\infty} a_n^2$。但对每个 $n$，有 $a_n^2 \cdot 10^{2n-2} = b_n^2 \le 2 \cdot 10^{2n-2}$，故 $a_n^2 \le 2$。

这说明 $a^2 \le 2$。

类似地，由于 $(b_n + 1)^2 > 2 \cdot 10^{2n-2}$，我们有

```math
\left(a_n + 10^{1-n}\right)^2 = \frac{(b_n + 1)^2}{10^{2n-2}} > 2.
```

因此，

```math
2 \le \lim_{n\to\infty} (a_n + 10^{1-n})^2 = \lim_{n\to\infty} a_n^2 = a^2.
```

综合可得 $a^2 = 2$，故 $a = \sqrt{2}$。

---

### <span style="color:#2471a3;">**[proof]**</span> <span style="color:#c0392b;">**Proof of the Monotone Convergence Theorem（单调收敛定理的证明）**</span>

**递增版本.** 递减版本的证明类似。

设序列满足 $a_n \le a_{n+1} \le A$，并令 $a = \sup \{a_n\}$。我们要证明 $a_n \to a$。

对任意 $\epsilon > 0$，因为 $a - \epsilon < a$，所以 $a - \epsilon$ 不是序列的 **upper bound（上界）**，因此存在 $N$ 使得

```math
a_N > a - \epsilon.
```

由于序列递增，对 $n \ge N$ 有

```math
a - \epsilon < a_N \le a_n \le a,
```

最后一项不等式利用了 $a$ 是序列上界的性质。

于是对 $n \ge N$ 有

```math
0 \le a - a_n < \epsilon.
```

这表明序列收敛，且极限为 $a$。$\square$

---

> <span style="color:#1e8449;">**[note] Note（译者注）: 单调收敛定理——完备性的计算面孔**</span>
>
> 单调收敛定理（MCT）的真正力量在于：它让你**无需预先知道极限值**就能证明收敛——这正是 $\sqrt{2}$ 的十进制逼近序列能被严格处理的唯一原因。如果你只有 $\epsilon$-$N$ 定义，你连极限候选都写不出来。MCT 之所以成立，本质上是因为 $\mathbb{R}$ 具备 **least-upper-bound property（最小上界性）**：每个上有界的集合都有 supremum（上确界）。这并非平凡的数学事实——在 $\mathbb{Q}$ 中，集合 $\{x \in \mathbb{Q} : x^2 < 2\}$ 上有界但没有有理数上确界，因此 $\mathbb{Q}$ 上的单调有界序列可以不收敛。MCT 与完备性的等价性正是 $\mathbb{R}$ 区别于 $\mathbb{Q}$ 的核心标识。
>
> 证明中最精巧的一步——"$a = \sup\{a_n\}$，故 $a - \epsilon$ 不是上界，从而存在 $a_N > a - \epsilon$"——我称之为 **$\epsilon$-剥离法（$\epsilon$-stripping）**：你从上确界 $a$ 往回"剥"掉一层 $\epsilon$ 的厚度，发现在这个被剥离的间隙里必然有序列项钻了进去；由于序列单调，后续所有项都被锁死在 $(a-\epsilon, a]$ 这个窄窗内，收敛无可避免。🎥 *Colding 在视频中以极其口语化的方式将这一步讲透了：因为 $a$ 本身就是上界，$a_n \le a$ 自动成立，所以* "you don't need absolute value because I already know this is bigger than that"——*不等式方向天然确定，绝对值完全多余。他指出* "$a - \epsilon$ is not an upper bound"——*正因如此，某个 $a_N$ 必须钻进 $(a-\epsilon, a]$ 这个间隙；序列的尾巴被* "squished in this little interval"（*挤在这个小间隙里*），*而* "this difference from here to here is certainly bounded by the distance to here, which was epsilon"——*整个尾巴与 $a$ 的距离被 $\epsilon$ 牢牢控制。* 这个证明模板——"取极值候选→剥离 $\epsilon$→论证尾巴被困在 $\epsilon$ 邻域内"——在 Rudin *Principles of Mathematical Analysis*（定理 3.14）中仅用五行完成，但它在后续 Bolzano-Weierstrass 和 Heine-Borel 的证明中还将以变体形式反复出现。
>
> 与 **Strang 线性代数**中 Gram-Schmidt 正交化作类比：两者共享 **逐步构造模板（sequential construction template）**——Gram-Schmidt 每次对一个向量投影-减去，逐步逼近正交基；MCT 的序列项则逐项向上逼近 supremum。在你正在学的 **CSAPP 第 8 章异常控制流**中，中断处理器沿中断向量表逐级查询故障源的过程，同样遵循"从初始状态经不可逆步骤序列抵达确定终点"的抽象模式——虽然领域迥异，但底层思维结构是一致的。
>
> 历史上，Bolzano（1817）最早意识到"单调有界序列收敛"需要证明而非视为当然，Cauchy（1821）在 *Cours d'Analyse* 中依赖几何直觉使用它，直到 Weierstrass 和 Dedekind（1872）才将其锚定于实数构造的公理基础。前沿方向：在泛函分析中，MCT 被推广为 **单调收敛定理的测度论版本**（Lebesgue 单调收敛定理），以及在 Banach 格（Banach lattices）中对单调有界序列收敛性的研究。

---

<span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f;">**Definition（定义）: Cauchy Sequence（柯西序列）**</span>

序列 $\{a_n\}$ 称为 **Cauchy sequence（柯西序列）**，如果对任意 $\epsilon > 0$，存在 $N$ 使得当 $m, n \ge N$ 时，有

```math
|a_n - a_m| < \epsilon.
```

（即序列的 tail（尾部）聚集在一起。）

---

#### <span style="color:#7f8c8d;">📜 Historical Note（历史注记）</span>

> Augustin-Louis Cauchy（柯西，1789–1857）是法国数学家、工程师和物理学家。他是最早严格表述并证明微积分关键定理的人之一（从而创立了 real analysis（实分析）），开创了 complex analysis（复分析）领域，并在 abstract algebra（抽象代数）中研究了 permutation groups（置换群）。柯西还对数学物理的诸多课题做出了贡献，特别是 continuum mechanics（连续介质力学）。


---

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**Theorem（定理）: Convergent ⟺ Cauchy**</span>

一个序列是 convergent（收敛的）当且仅当它是 Cauchy sequence（柯西序列）。

---

> <span style="color:#1e8449;">**[note] Note（译者注）: Cauchy 序列与完备性——为什么 ℝ 是"填满的"**</span>
>
> Cauchy 序列定义的核心洞察是：**收敛性可以仅由序列内部项之间的相互距离来表达，完全不依赖外部极限候选**。这看似细微的重新表述带来了巨大的概念解放——它让你能在不"走出"所在空间的情况下谈论一个序列是否"本该"收敛。🎥 *Colding 在课堂上以极为诚实的教学姿态揭示了从 MCT 推进到 Cauchy 序列的逻辑动机：* "sometimes it's hard... if it was a monotone sequence, then you could write down explicitly what the limit was... but in general, you might not be able to write down the limit, but you want to prove that the limit exists"（*有时很难直接写出极限……如果序列是单调的，你当然可以明确写下极限是什么——极限就是 supremum——但一般情况下，你可能写不出极限，却仍想证明极限存在*）。*这正是 Cauchy 准则要填补的空白：MCT 要求单调性作为前提，而 Cauchy 条件将"收敛可判定性"从单调序列推广到了任意序列。Colding 还预告了下一讲的证明策略——* "the proof involved this stuff where we defined these two sequences from that bounded sequence"——*从任意有界序列构造两个单调序列（即 $\limsup$ 和 $\liminf$ 的构造雏形），对其应用 MCT 得到收敛性，进而推出 Cauchy 收敛准则。这揭示了一条深层教学逻辑链：MCT 是引擎，Cauchy 准则是 MCT 在非单调场景下的"适配器"。* 在 $\mathbb{R}$ 中，Cauchy ⇔ 收敛，这个等价性被称为 $\mathbb{R}$ 的 **completeness（完备性）**。然而这个等价并非逻辑必然：它是实数系构造的产物。构造 $\mathbb{R}$ 有两种标准方法——**Dedekind 分割**（每个实数对应有理数集的一个"切口"）和 **Cauchy 完备化**（把 Cauchy 序列的等价类本身定义为实数）。两种方法殊途同归，但前者强调序结构（supremum 性质自然导出），后者强调度量结构（任何度量空间都可以 Cauchy 完备化，你将在泛函分析中系统学习）。
>
> 与 **离散数学（MIT 6.042J）**中学到的 well-ordering principle（良序原理）对照：良序原理断言 $\mathbb{N}$ 的每个非空子集有最小元，支撑了数学归纳法；最小上界性断言 $\mathbb{R}$ 的每个有上界的子集有上确界，支撑了分析学中极限存在性的一切论证。两者都是关于"数系的结构完整性"的公理，一个治理离散，一个治理连续。但注意一个关键区别：良序原理是 $\mathbb{N}$ 的内在性质（Peano 公理的推论），而完备性是 $\mathbb{R}$ 的**定义性特征**——你必须通过构造来保证它。
>
> 前瞻：在一般的 metric space（度量空间）中，Cauchy 序列未必收敛（例如 $\mathbb{Q}$ 中逼近 $\sqrt{2}$ 的序列）——这正是你需要 **compactness（紧致性）**的原因。在紧致度量空间中，每个序列都有收敛子列（Bolzano-Weierstrass 的推广）。TBB 教材（*Elementary Real Analysis*）在第 4 章对此有系统的处理，建议在学完 Cauchy 收敛准则后并行阅读。历史上，Cantor 正是从 Cauchy 序列的角度构造实数（1872），而 Dedekind 同年从序完备性出发——两条路线之争至今仍反映在实分析教材的编排逻辑中（Rudin 取 Dedekind 路线，Apostol 偏 Cauchy 路线）。

---

### <span style="color:#2471a3;">**[application]**</span> <span style="color:#c0392b;">**Application: Fixed Points of Maps（映射的不动点）**</span>

若 $T : \mathbb{R} \to \mathbb{R}$ 是一个映射，则 $x_0 \in \mathbb{R}$ 称为 **fixed point（不动点）**，如果

```math
T(x_0) = x_0.
```

---

<span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f;">**Definition（定义）: Contracting Map（压缩映射）**</span>

**Contracting map（压缩映射）** 是一个映射 $T : \mathbb{R} \to \mathbb{R}$，满足存在 $c < 1$ 使得对所有 $x, y \in \mathbb{R}$ 有

```math
|T(x) - T(y)| \le c\,|x - y|.
```

（即在映射作用下，点被压缩在一起。）

---

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**Contracting Mapping Theorem（压缩映射定理）**</span>

任何一个 contracting map（压缩映射）都有 fixed point（不动点）。

---

> <span style="color:#1e8449;">**[note] Note（译者注）: 压缩映射定理——分析学中的"万能迭代引擎"**</span>
>
> 压缩映射定理（Contracting Mapping Theorem），又称 **Banach 不动点定理（Banach fixed-point theorem，1922）**，是分析学中最具通用性的存在性定理之一。它的证明是 Cauchy 收敛准则的教科书级应用，遵循一个四步 **不动点迭代模板（fixed-point iteration template）**：(1) 从任意起点 $x_0$ 构造迭代序列 $x_{n+1} = T(x_n)$；(2) 利用压缩条件 $|Tx - Ty| \le c|x-y|$（$c\lt 1$）归纳证明 $|x_{n+1} - x_n| \le c^n|x_1 - x_0|$，从而序列是 Cauchy 的；(3) Cauchy 收敛准则给出极限 $x^*$；(4) 在 $x_{n+1} = T(x_n)$ 两边取极限，利用 $T$ 的连续性（压缩映射自动 Lipschitz 连续）得 $x^* = T(x^*)$；唯一性由另一个不动点 $y^*$ 推出 $|x^* - y^*| = |Tx^* - Ty^*| \le c|x^* - y^*|$，迫使 $|x^* - y^*| = 0$。🎥 *Colding 在视频中反复敲打一个看似微不足道却决定一切的条件：* "$c < 1$——that's what makes everything go. If it was equal to 1, you wouldn't get anything."（*c 小于 1——这就是一切运转的关键。如果 c 等于 1，你什么也得不到。*）*压缩映射的几何直觉极为朴素：映射之后，任意两点之间的距离必须按固定比例缩小——* "they have to come closer"（*它们必须靠得更近*）。*正是这个简单到几乎 trivial 的"靠近"条件，与 Cauchy 完备性联手，便生成了不动点的存在性。Colding 还预告了向更抽象空间的推广：* "once you know the more abstract concepts, then it's quite easy; the proof is going to be the same"——*一旦掌握了度量空间和完备性的抽象框架，在一般完备度量空间（而不仅仅是 $\mathbb{R}$）中重证压缩映射定理，证明完全一样。这正是下一讲 Picard-Lindelöf 定理的伏笔——在函数空间上使用完全相同的四步模板。*
>
> 跨课程共振极其丰富。在 **CLRS 算法导论**中，数值算法的 **fixed-point iteration（不动点迭代）**（如 Newton 法求根 $f(x)=0$ 可重写为 $x = x - f(x)/f'(x)$）直接依赖此定理的离散化版本——压缩条件变为导数绝对值小于 1。在 **Boyd 凸优化**中，梯度下降的收敛性分析（对 Lipschitz 梯度、步长足够小）本质上是证明梯度步映射 $T(x) = x - \alpha \nabla f(x)$ 在某种度量下是压缩的——Banach 不动点定理给出了线性收敛率的理论基础。在 **Horn 矩阵论**中，**幂法（power method）** 求主导特征值的过程——反复左乘矩阵 $A$——之所以收敛，是因为当投影到主特征空间后，$A$ 的作用变成一个压缩映射。甚至在你们的 **"方舟计划"** 愿景中，"先实现 AGI 再控制 AI"的迭代策略——"造出来→发现问题→改进→再造"——在抽象层面正是压缩映射的哲学：从一个初始猜想出发，反复施加同一个"改良映射"，信任该映射最终将你带到不动点（安全可控的 AGI）。
>
> 前瞻：下一讲将展示这个定理在 **Picard-Lindelöf 定理**（ODE 解的存在唯一性）中的应用——将微分方程 $y' = f(t, y)$ 改写为积分方程 $y(t) = y_0 + \int_{t_0}^t f(s, y(s))ds$，右端视为函数空间上的映射，在 Lipschitz 条件下该映射是压缩的。这是泛函分析思维的入门关口：**函数本身成为空间中的点，映射作用于函数**。在更远处，Banach 不动点定理被推广到偏序集上的 **Knaster-Tarski 定理**（程序语义学中不动点语义的基础），以及证明隐函数定理和反函数定理的 Newton-Kantorovich 框架。

---

**Application（应用）:** 压缩映射定理可用于证明 ODEs（常微分方程）解的存在性。

> <span style="color:#7f8c8d;">*更多内容将在下次课程中继续讨论……*</span>

---

### <span style="color:#2471a3;">**[reference]**</span> <span style="color:#7f8c8d;">**References（参考文献）**</span>

- **TBB:** B.S. Thomson, J.B. Bruckner, and A.M. Bruckner, *Elementary Real Analysis*, 2nd edition
  - [Screen-optimized version (Landscape)](https://classicalrealanalysis.info/com/documents/TBB-AllChapters-Landscape.pdf)
  - [Print-optimized version (Portrait)](https://classicalrealanalysis.info/com/documents/TBB-AllChapters-Portrait.pdf)

---

> <span style="color:#7f8c8d;">MIT, Dept. of Math., 77 Massachusetts Avenue, Cambridge, MA 02139-4307.</span>
> 
> <span style="color:#7f8c8d;">MIT OpenCourseWare — https://ocw.mit.edu</span>
> 
> <span style="color:#7f8c8d;">18.100B Real Analysis, Spring 2025. For information about citing these materials or our Terms of Use, visit https://ocw.mit.edu/terms.</span>

---

