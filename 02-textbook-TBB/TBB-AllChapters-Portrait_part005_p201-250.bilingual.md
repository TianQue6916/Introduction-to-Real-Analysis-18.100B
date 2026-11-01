# <span style="color:#c0392b">TBB《Elementary Real Analysis》· Chapter 5: Limits and Continuity（第 5 章：极限与连续）双语精译</span>

> <span style="color:#7f8c8d;">源文件：TBB-AllChapters-Portrait_part005_p201-250.pdf（书页 185–234）| 本文件覆盖 §5.1.3–§5.9（书页 185–232 正文）| 习题区与 NOTES 区（书页 233–234）保持英文原文，未收录</span>

---

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">5.1.3 Limits (Mapping Definition)（极限的映射定义）</span>

> <span style="color:#7f8c8d;">TBB §5.1.3, p.185</span>

> **[note]** 原文标注：**Enrichment section**（加料章节），**May be omitted**（可略去）。

极限 $\lim_{x \to x_0} f(x) = L$ 背后的本质思想是：靠近 $x_0$ 的 $x$ 值被 $f$ 映射为靠近 $L$ 的值。

我们一直能够用表达这种接近性的不等式来刻画这一思想：对 $x$ 值是 $\delta$-接近（$\delta$-close），对 $f(x)$ 值是 $\varepsilon$-接近（$\varepsilon$-close）。

这本质上是一个 mapping property（映射性质），它可以用任意 open set（开集）来表达。

下面的定义与定义 5.1 和定义 5.4 都是等价的。

### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#c0392b">Definition 5.6 (Limit)（定义 5.6：极限）</span>

> <span style="color:#7f8c8d;">TBB §5.1.3, p.185</span>

设 $f : E \to \mathbb{R}$ 是以 $E$ 为 domain（定义域）的函数，并假设 $x_0$ 是 $E$ 的一个 point of accumulation（聚点）。

那么当对每个包含点 $L$ 的开集 $V$，都存在一个包含点 $x_0$ 的开集 $U$，使得 $U$ 中每个属于 $f$ 定义域且 $x \neq x_0$ 的点 $x$，其像 $f(x)$ 都落入 $V$ 中时，我们记作

```math
\lim_{x \to x_0} f(x) = L;
```

即

```math
f : E \cap U \setminus \{ x_0 \} \to V.
```

---‘

同样，我们必须证明这个定义与 ε-δ 定义（ε-δ definition）是等价的。我们现在就来证明这一点。

<span style="color:#2471a3;">**[proof]**</span> **Proof（证明）：定义 5.1 与 5.6 等价**

> 首先假设按照定义 5.1 有 $\lim_{x \to x_0} f(x) = L$。设 $V$ 是包含点 $L$ 的开集。由于 $L$ 是 $V$ 的 interior point（内点），存在正数 $\varepsilon$，使得
> 
> ```math
> (L - \varepsilon, L + \varepsilon) \subset V.
> ```
> 
> 选取 $\delta > 0$，使得只要 $x$ 是 $E$（即 $f$ 的定义域）中的点，并且 $0 < |x - x_0| < \delta$，就有 $|f(x) - L| < \varepsilon$。设 $U$ 为开集 $(x_0 - \delta, x_0 + \delta)$。那么上述不等式表明，$U$ 中每个属于 $f$ 定义域且 $x \neq x_0$ 的点 $x$，其像 $f(x)$ 都落入 $V$ 中。这正是定义 5.6。
> 
> 反过来，假设按照定义 5.6 有 $\lim_{x \to x_0} f(x) = L$。设 $\varepsilon > 0$，取 $V = (L - \varepsilon, L + \varepsilon)$。根据我们的定义，必然存在包含点 $x_0$ 的开集 $U$，使得 $U$ 中每个属于 $f$ 定义域且 $x \neq x_0$ 的点 $x$，其像 $f(x)$ 都落入 $V$ 中。由于 $x_0$ 是 $U$ 的内点，必然存在正数 $\delta$，使得
> 
> ```math
> (x_0 - \delta, x_0 + \delta) \subset U.
> ```
> 
> 这一映射性质蕴含：若 $0 < |x - x_0| < \delta$，则 $|f(x) - L| < \varepsilon$。这正是定义 5.1 中的 ε-δ 定义。

$\square$

由于我们的三个定义彼此等价，在讨论极限时，我们既可以采用 sequential argument（序列论证），也可以采用 mapping argument（映射论证），还可以采用 ε-δ 论证（ε-δ argument）。

---

> <span style="color:#1e8449;">**[note] Note（译者注）——标题：开集语言——从 ε-δ 到拓扑的第一级台阶**</span>
> 
> 定义 5.6 用「对每个包含 $L$ 的开集 $V$，存在包含 $x_0$ 的开集 $U$」来重述极限，这不是换一套说法那么简单。你在 6.042J 离散数学中学过集合论的基本运算，但「开集」这个新概念才是这里真正的跳跃：它是把 $\varepsilon$-$\delta$ 不等式 $(x_0-\delta, x_0+\delta)$ 和 $(L-\varepsilon, L+\varepsilon)$ 抽象为「包含该点的、没有边界的区域」。为什么值得这样做？因为一旦极限定义完全用开集和映射性质来表述，它就摆脱了对实数绝对值度量的依赖——极限概念可以原封不动地搬到任意「拓扑空间」。你目前还不需要理解什么是拓扑空间，但请意识到：定义 5.1（ε-δ）、定义 5.4（序列）和定义 5.6（映射）三个等价定义，分别对应了实分析课程三条分岔的路径——度量论证、序列论证、拓扑论证。后面在 §5.4 讨论连续函数时你会反复看到这三种面孔。一个来自 CSAPP 的脚手架：ε-δ 就像浮点运算中的「精度-范围」权衡——ε 是你要求的输出精度（你最多接受 $|f(x)-L|<\varepsilon$），δ 是你必须找到的输入范围（只要 $x$ 在 $x_0$ 的 δ 邻域内就能保证输出精度）。定义 5.6 则相当于说：输出任意精度的「邻域」，你都存在一个输入「邻域」使得映射落入其中——这正是浮点函数正确舍入（correct rounding）需要的形式化保证。

---

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">5.1.4 One-Sided Limits（单侧极限）</span>

> <span style="color:#7f8c8d;">TBB §5.1.4, p.186</span>

一个函数在某个点处可能不存在极限，却仍可能在某一侧看起来存在极限。

如果我们忽略函数在右侧发生的情况，或许会有 left-hand limit（左极限）。

这一点很容易实现。设 $f$ 在点 $x_0$ 附近处处有定义，并定义一个新函数

```math
g(x) = f(x), \quad x < x_0.
```

这个新函数 $g$ 定义在 $x_0$ 左侧的集合上，对 $f$ 在右侧的取值一无所知。

因此，极限 $\lim_{x \to x_0} g(x)$

---

> <span style="color:#7f8c8d;">TBB §5.1.4, p.187</span>

它可以被看作 f 的 left-hand limit（左极限），并被写为

```math
\lim_{x \to x_0^-} f(x) = L,
```

其中记号 $x_0 -$ 表示这里取的是左极限，而非 ordinary limit（普通极限）。类似地，记号

```math
\lim_{x \to x_0^+} f(x) = L
```

表示 right-hand limit（右极限），其中记号 $x_0 +$ 表示在 $x_0$ 的正侧（即右侧）取极限。

由于这些 one-sided limits（单侧极限）实质上只是针对另一个函数所取的普通极限，它们无需任何额外论证便能满足普通极限的全部理论。我们可以相当自由地使用它们，而不必担心它们需要不同的定义或不同的理论。即便如此，把通常的定义改写成单侧极限的形式仍然很方便，只是为了给它们一个明确的表述。我们给出右极限的版本，左极限的版本由读者自行写出。

### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#c0392b">Definition 5.7（定义 5.7）</span>

> <span style="color:#7f8c8d;">TBB §5.1.4, p.187</span>

**(Right-Hand Limit 右极限)** 设 $f: E \to \mathbb{R}$ 是以 $E$ 为定义域的函数，并设 $x_0$ 是 $E \cap (x_0, \infty)$ 的一个 point of accumulation（聚点）。则我们写

```math
\lim_{x \to x_0^+} f(x) = L
```

如果对每一个 $\varepsilon > 0$ 都存在 $\delta > 0$，使得只要 $x_0 < x < x_0 + \delta$ 且 $x \in E$，就有 $|f(x) - L| < \varepsilon$。

可以建立与之等价的 sequential version（序列版本）。

### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#c0392b">Definition 5.8（定义 5.8）</span>

> <span style="color:#7f8c8d;">TBB §5.1.4, p.187</span>

**(Right-Hand Limit 右极限)** 设 $f: E \to \mathbb{R}$ 是以 $E$ 为定义域的函数，并设 $x_0$ 是 $E \cap (x_0, \infty)$ 的一个聚点。则我们写

```math
\lim_{x \to x_0^+} f(x) = L
```

如果对 $E$ 中每一列满足 $e_n > x_0$ 且当 $n \to \infty$ 时 $e_n \to x_0$ 的 decreasing sequence（递减序列）$\{e_n\}$，都有

```math
\lim_{n \to \infty} f(e_n) = L.
```

---

---

> <span style="color:#1e8449;">**[note] Note（译者注）——标题：单侧极限与跳跃——从「两侧逼近失败」到「分支逻辑」**</span>
> 
> TBB 处理单侧极限的手法极其经济：它不是重写一套新理论，而是把 $f$ 限制在 $x_0$ 的左侧/右侧，构造一个新函数 $g$，然后对 $g$ 套用已经建立好的普通极限理论。这是你在 6.042J 学过的「限制」（restriction）操作在分析中的一次优雅应用——函数的定义域缩小后，原函数在此子集上的行为自然不同。注意到定义 5.7（ε-δ 右极限）的条件是 $x_0 < x < x_0 + \delta$ 而非 $|x - x_0| < \delta$——不等式从对称变成了「只向右看」，这和你写二分搜索（binary search，📖 CLRS §2.3）时只关心左半边或右半边是同构的思想。跳跃不连续（jump discontinuity）的直观定义由此自然浮现：当左极限和右极限都存在但不相等时，函数在这一点「跳」了一下。想一想：Heaviside 阶跃函数 $H(x)$ 在 $x=0$ 处的跳跃不连续，实际上等价于「单位阶跃响应的瞬时切换」——你在 CSAPP 学过的比较指令 cmp 和条件跳转 je/jne（📖 CSAPP §3.6）本质上也是基于这种二进制判别。进一步说，TBB 在 p.201 提出的问题——能否构造一个非降函数在无穷多个点处都有跳跃——在你学过可数性（countability）之后会有惊人答案：是的，但跳跃点集至多可数。这个结论的证明将在后续用有理数在实数中的稠密性来完成，它是实分析中「序结构约束不连续点数量」的经典论证。

---

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">5.1.5 Infinite Limits（无穷极限）</span>

> <span style="color:#7f8c8d;">TBB §5.1.5, p.188</span>

我们容易验证，极限

```math
\lim_{x \to 0^+} \frac{1}{x}
\qquad
\lim_{x \to 0^-} \frac{1}{x}
```

都不存在。看一眼函数 $f(x) = 1/x$ 的图象就会发现，我们不如改写成

```math
\lim_{x \to 0^+} \frac{1}{x} = \infty
\qquad
\lim_{x \to 0^-} \frac{1}{x} = -\infty
```

以此传达更多关于实际情形的信息，而不是仅仅说极限不存在。

在此我们遵循研究 divergent sequences（发散序列）时的一贯做法。有些序列只是 diverge（发散），有些则发散到 $\infty$ 或 $-\infty$。如果我们回头审视序列的定义，并将其与函数极限的定义相比较，就会得出下面的定义。

### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#c0392b">Definition 5.9（定义 5.9）</span>

> <span style="color:#7f8c8d;">TBB §5.1.5, p.188</span>

**(Infinite Limit 无穷极限)** 设 $f: E \to \mathbb{R}$ 是以 $E$ 为定义域的函数，并设 $x_0$ 是 $E \cap (x_0, \infty)$ 的一个聚点。则我们写

```math
\lim_{x \to x_0^+} f(x) = \infty
```

如果对每一个 $M > 0$ 都存在 $\delta > 0$，使得只要 $x_0 < x < x_0 + \delta$ 且 $x \in E$，就有 $f(x) \geq M$。

---

> <span style="color:#7f8c8d;">TBB §5.1.5, p.189</span>

类似地，我们可以定义

```math
\lim_{x \to x_0^+} f(x) = -\infty
```

如果对于每一个 $m < 0$ 都存在一个 $\delta > 0$，使得只要 $x_0 < x < x_0 + \delta$ 且 $x \in E$，就有 $f(x) \leq m$。

从 left-hand side（左侧）趋近的无穷极限也以类似的方式定义，记为 $\lim_{x \to x_0^-} f(x) = \infty$ 与 $\lim_{x \to x_0^-} f(x) = -\infty$。此外，two-sided limit（双侧极限）也以同样的方式定义，只是采用一个 two-sided condition（双侧条件）。

<span style="color:#2471a3;">**[note]**</span> **Note（原文注意）**

正如数列的情形一样，除非极限是有限的，否则我们不称一个函数极限存在。因此，例如我们会说极限 $\lim_{x \to 0^+} 1/x$ 不存在，而事实上 $\lim_{x \to 0^+} 1/x = \infty$。极限是一个实数。符号 $\infty$ 与 $-\infty$ 用来描述某些情形，但它们本身不被当作数来解释。

---

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">5.2 Properties of Limits（极限的性质）</span>

> <span style="color:#7f8c8d;">TBB §5.2, p.190</span>

在微积分课程中，极限的计算依赖于一套极限理论。对大多数简单的计算来说，只需知道如何处理那些由其他函数通过加法、减法、乘法或除法组合而成的函数就足够了。后来，更精细的问题要求更高级的技巧（例如 L'Hôpital 法则（洛必达法则））。下面我们建立 function limit（函数极限）理论的基本原理。

我们首先讨论 uniqueness（唯一性）与 boundedness（有界性）性质，然后继续到 algebraic property（代数性质）。在这方面，我们几乎遵循着当初研究 sequential limit（数列极限）时所走的同一条道路。事实上，数列极限与函数极限的定义如此相似，以至于二者的理论本身也必然相当相似。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">5.2.1 Uniqueness of Limits（极限的唯一性）</span>

> <span style="color:#7f8c8d;">TBB §5.2.1, p.190</span>

当我们写出陈述 $\lim_{x \to x_0} f(x) = L$ 时，我们希望确信：对于某些不同于 $L$ 的其他数，这一陈述不会同样成立。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 5.10 (Uniqueness of Limits)（定理 5.10：极限的唯一性）</span>

> <span style="color:#7f8c8d;">TBB §5.2.1, p.190</span>

假设 $\lim_{x \to x_0} f(x) = L$。那么数 $L$ 是唯一的：没有其他数具有这一同样的性质。

<span style="color:#2471a3;">**[proof]**</span> **Proof（证明）**（虚化显示）:

> 我们假设 $\lim_{x \to x_0} f(x) = L$ 与 $\lim_{x \to x_0} f(x) = L_1$ 都成立。为了证明定理，我们必须证明 $L = L_1$。如果把这个条件转化为关于数列的陈述，那么它断言：任何满足 $x_n \to x_0$、$x_n \neq x_0$ 且所有点都在 $f$ 的 domain（定义域）中的数列 $x_n$，都必须有 $f(x_n) \to L$，同时也必须有 $f(x_n) \to L_1$。为了使这些极限存在，点 $x_0$ 必须是 $f$ 的定义域的一个 point of accumulation（聚点），因此至少存在一个这样的数列。但我们早已为数列极限确立了这样的结论：除非 $L = L_1$，否则这种情况是不可能的（Theorem 2.8，定理 2.8）。
> 
> $\square$

---

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">5.2.2 Boundedness of Limits（极限的有界性）</span>

> <span style="color:#7f8c8d;">TBB §5.2.2, p.191</span>

**Boundedness of Limits（极限的有界性）**

我们回想，convergent sequences（收敛序列）都是有界的。对于函数也有一个类似的 statement（命题）。

如果一个 function limit（函数极限）存在，那么该函数不可能太大；不过，这个命题必须表述得精确，因为它实际上只在靠近取极限的那个点附近才成立。

例如，你会回想起我们在 Section 4.5 中关于 local boundedness（局部有界性）的讨论：函数 $f(x) = 1/x$ 是 unbounded（无界的），但在除 $0$ 以外的每一点处却都是局部有界的。

同样地，我们将看到，极限

```math
\lim_{x \to x_0} \frac{1}{x} = \frac{1}{x_0}
```

对每个 $x_0 \neq 0$ 成立，也同样要求那个 local boundedness（局部有界性）性质。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 5.11 (Boundedness of Limits, 极限的有界性)</span>

> <span style="color:#7f8c8d;">TBB Theorem 5.11, p.191</span>

假设极限

```math
\lim_{x \to x_0} f(x) = L
```

存在。则存在一个区间 $(x_0 - c, x_0 + c)$ 和一个数 $M$，使得对位于该区间内且属于 $f$ 的 domain（定义域）的每一个值 $x$，都有

```math
|f(x)| \le M .
```

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 存在一个 $\delta > 0$，使得只要 $x$ 是 $f$ 的定义域中异于 $x_0$ 且满足 $|x - x_0| < \delta$ 的点，就有 $|f(x) - L| < 1$。
> 
> 如果 $x_0$ 不在 $f$ 的定义域中，那么这意味着对所有位于 $(x_0 - \delta, x_0 + \delta)$ 中且属于 $f$ 的定义域的 $x$，都有
> 
> ```math
> |f(x)| = |f(x) - L + L| \le |f(x) - L| + |L| < |L| + 1 .
> ```
> 
> 这就完成了证明，因为我们可以取 $M = |L| + 1$。
> 
> 如果 $x_0$ 在 $f$ 的定义域中，那么改取
> 
> ```math
> M = |L| + 1 + |f(x_0)| .
> ```
> 
> 于是对所有位于 $(x_0 - \delta, x_0 + \delta)$ 中且属于 $f$ 的定义域的 $x$，都有 $|f(x)| \le M$。$\square$

关于 boundedness away from zero（远离零的有界性）也可以作类似的陈述。这表明：如果一个函数有非零的极限，那么在靠近该点的附近，函数会保持远离零。其证明用到类似的思路，留作习题。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 5.12 (Boundedness Away from Zero, 远离零的有界性)</span>

> <span style="color:#7f8c8d;">TBB Theorem 5.12, p.191</span>

如果极限

```math
\lim_{x \to x_0} f(x)
```

存在且不为零，则存在一个区间 $(x_0 - c, x_0 + c)$ 和一个正数 $m$，使得对位于该区间内、满足 $x \neq x_0$ 且属于 $f$ 的定义域的每一个值 $x$，都有

```math
|f(x)| \ge m > 0 .
```

> <span style="color:#7f8c8d;">（本定理陈述的后半部分续于 p.192；习题 5.2.3–5.2.7 位于 p.192 页首，按约定跳过。）</span>

---

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">5.2.3 Algebra of Limits（极限的代数）</span>

> <span style="color:#7f8c8d;">TBB §5.2.3, p.192</span>

函数可以通过通常的 arithmetic operations（算术运算）——加法、减法、乘法与除法——来组合。事实上，我们在 calculus（微积分）课程中很可能遇到的大多数函数，都可以看作是由更简单的函数以这种方式组合而成的。

<span style="color:#2471a3;">**[example]**</span> **Example 5.13（例 5.13）**

> <span style="color:#7f8c8d;">TBB Example 5.13, p.192</span>

计算

```math
\lim_{x \to 3} \frac{2x^3 + 4}{3x^2 + 1}
= \frac{\lim_{x \to 3} (2x^3 + 4)}{\lim_{x \to 3} (3x^2 + 1)}
= \frac{2(\lim_{x \to 3} x^3) + 4}{3(\lim_{x \to 3} x^2) + 1}
= \frac{2 \times 3^3 + 4}{3 \times 3^2 + 1}
```

应当能唤起人们对微积分课后作业的美好回忆。但这些计算怎样才能被恰当地证明呢？

凭借我们处理 sequence limits（数列极限）的经验，我们可以预期：正如存在数列极限的代数一样，也应当存在一个「函数极限的代数」（algebra of function limits）。其证明既可以模仿我们先前为数列所构造的证明，也可以利用函数极限可以归结为 sequential limits（序列极限）这一事实。

这里有一个额外的 caution（警示）。下面用一个例子来说明。

<span style="color:#2471a3;">**[example]**</span> **Example 5.14（例 5.14）**

> <span style="color:#7f8c8d;">TBB Example 5.14, p.192</span>

我们知道 $\lim_{x \to 0} \sqrt{-x} = 0$，也知道 $\lim_{x \to 0} \sqrt{x} = 0$。由此能否推出

```math
\lim_{x \to 0} \left( \sqrt{x} + \sqrt{-x} \right) = 0
```

呢？

---

> <span style="color:#7f8c8d;">TBB §5.2.3, p.193</span>

（接上页 Example 5.14 的结论）函数 $f(x) = \sqrt{x} + \sqrt{-x}$ 的 domain（定义域）中只有一个点，因此在这里根本谈不上任何极限命题。

$\square$

在上面各定理中出现的 extra hypothesis（额外假设），正是为了避开像上面这样的例子。我们必须假设：函数 $f$ 的 domain（定义域），记作 $\operatorname{dom}(f)$，与函数 $g$ 的 domain（定义域），记作 $\operatorname{dom}(g)$，必须拥有足够多的公共点，从而能够在所考察的点 $x_0$ 处定义极限。在大多数简单的应用中，函数的 domain（定义域）并不会引起任何麻烦。

在证明方面，我们有多种可用的策略。我们既可以把这些 limit theorems（极限定理）化归为关于序列的命题，然后援引我们在第 2 章建立的 sequential limits（序列极限）理论；也可以仿照当初为序列证明的类似命题，构造出相应的 ε-δ 证明。我们并不需要任何真正全新的思想。正因如此，这些定理的证明就留给练习了。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 5.15 (Multiples of Limits)（定理 5.15：极限的倍数）</span>

> <span style="color:#7f8c8d;">TBB §5.2.3, p.193</span>

假设极限 $\lim_{x\to x_0} f(x)$ 存在，且 $C$ 是一个 real number（实数）。那么

```math
\lim_{x\to x_0} C f(x) = C \left( \lim_{x\to x_0} f(x) \right).
```

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 5.16 (Sums and Differences)（定理 5.16：和与差）</span>

> <span style="color:#7f8c8d;">TBB §5.2.3, p.193</span>

假设极限 $\lim_{x\to x_0} f(x)$ 与 $\lim_{x\to x_0} g(x)$ 均存在，且 $x_0$ 是 $\operatorname{dom}(f) \cap \operatorname{dom}(g)$ 的一个 point of accumulation（聚点）。那么

```math
\lim_{x\to x_0} \bigl( f(x) + g(x) \bigr) = \lim_{x\to x_0} f(x) + \lim_{x\to x_0} g(x)
```

并且

```math
\lim_{x\to x_0} \bigl( f(x) - g(x) \bigr) = \lim_{x\to x_0} f(x) - \lim_{x\to x_0} g(x).
```

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 5.17 (Products of Limits)（定理 5.17：极限的乘积）</span>

> <span style="color:#7f8c8d;">TBB §5.2.3, p.193</span>

假设极限 $\lim_{x\to x_0} f(x)$ 与 $\lim_{x\to x_0} g(x)$ 均存在，且 $x_0$ 是 $\operatorname{dom}(f) \cap \operatorname{dom}(g)$ 的一个 point of accumulation（聚点）。那么

```math
\lim_{x\to x_0} f(x) g(x) = \left( \lim_{x\to x_0} f(x) \right) \left( \lim_{x\to x_0} g(x) \right).
```

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 5.18 (Quotients of Limits)（定理 5.18：极限的商）</span>

> <span style="color:#7f8c8d;">TBB §5.2.3, p.193</span>

假设极限 $\lim_{x\to x_0} f(x)$ 与 $\lim_{x\to x_0} g(x)$ 均存在，且后一个极限不为零，并且 $x_0$ 是 $\operatorname{dom}(f) \cap \operatorname{dom}(g)$ 的一个 point of accumulation（聚点）。那么

```math
\lim_{x\to x_0} \frac{f(x)}{g(x)} = \frac{\lim_{x\to x_0} f(x)}{\lim_{x\to x_0} g(x)}.
```

> <span style="color:#7f8c8d;">Exercises 5.2.8–5.2.16（习题区，跳过）（保留英文原文，不收录）</span>

> <span style="color:#7f8c8d;">书页 p.194 Running head（除页眉）外无正文内容；自 Exercises 标题起为习题区（习题 5.2.8–5.2.16，组文件行 111–178），按翻译约定保留英文原文，未收录。</span>

---

---

> <span style="color:#1e8449;">**[note] Note（译者注）——标题：化归序列法——函数极限代数的零成本战略**</span>
> 
> 定理 5.15–5.18 读起来像数列极限代数（定理 2.x）的「复制粘贴」——加、减、乘、除（分母极限非零）全部对函数极限也成立。TBB 说证明可以留作习题，不是因为它不重要，而是因为你有两种不费吹灰之力的证法：（A）**化归序列法**——由定义 5.4（序列版本），$\lim_{x\to x_0}f(x)=L$ 等价于「任何趋于 $x_0$ 的序列 $\{x_n\}$ 都有 $f(x_n)\to L$」，于是需要证明 $\lim (f+g) = \lim f + \lim g$ 时，只需对任意满足条件的 $\{x_n\}$ 写出 $(f+g)(x_n) = f(x_n) + g(x_n)$，然后直接调用你已经证明过的序列极限加法（定理 2.x），一步到位。（B）**ε-δ 直接证法**——像 TBB 正文提示的那样「模仿序列证明」。策略 A 是实分析中最常用的元策略之一：**凡是能用序列极限表述的函数极限命题，先化归到序列、再调用序列极限已有结论**。这和你在 6.006 算法课中学的分治（divide and conquer）精神完全一致：把一个复杂问题（函数极限）归约到已经解决的子问题（序列极限），然后组合子问题的解。但要注意 Example 5.14 的警示：如果 $f$ 和 $g$ 的公共定义域在 $x_0$ 附近太空了（比如只有 $\{x_0\}$ 本身），代数法则的前提就不满足——聚点条件是隐藏的、不可忽视的约束。

---

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">5.2.4 Order Properties（序性质）</span>

> <span style="color:#7f8c8d;">TBB §5.2.4, p.195</span>

正如我们看到 sequence limits（数列极限）同时保持 order structure（代数结构与序结构）一样，我们将会发现 function limits（函数极限）也具有同样的性质。我们刚刚完成了 algebraic properties（代数性质）的讨论。现在我们转而讨论 order properties（序性质）。

如果对所有 $x$ 都有 $f(x) \le g(x)$，那么我们期望能够得出结论：

```math
\lim_{x\to x_0} f(x) \le \lim_{x\to x_0} g(x).
```

我们现在就来证明这一点，以及另外几个直接与实数序结构相关的性质。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 5.19（定理 5.19）</span>

> <span style="color:#7f8c8d;">TBB §5.2.4, p.195</span>

设极限 $\lim_{x\to x_0} f(x)$ 与 $\lim_{x\to x_0} g(x)$ 都存在，且 $x_0$ 是 $\operatorname{dom}(f) \cap \operatorname{dom}(g)$ 的一个 point of accumulation（聚点）。若对所有 $x \in \operatorname{dom}(f) \cap \operatorname{dom}(g)$ 都有 $f(x) \le g(x)$，则

```math
\lim_{x\to x_0} f(x) \le \lim_{x\to x_0} g(x).
```

<span style="color:#2471a3;">**[proof]**</span> **Proof（证明）:**

> 我们给出一个间接证明（indirect proof，即反证法）。设 $L = \lim_{x\to x_0} f(x)$、$M = \lim_{x\to x_0} g(x)$，并反设（与定理结论相反）$L > M$。取 $\varepsilon$ 足够小，使得 $M + \varepsilon < L - \varepsilon$，也就是说，取
> 
> ```math
> \varepsilon < \frac{L - M}{2}.
> ```
> 
> 由极限的定义，存在数 $\delta_1$ 与 $\delta_2$，使得：若 $x \ne x_0$、$x$ 到 $x_0$ 的距离在 $\delta_1$ 以内且 $x$ 位于 $f$ 的定义域中，则 $f(x) > L - \varepsilon$；若 $x \ne x_0$、$x$ 到 $x_0$ 的距离在 $\delta_2$ 以内且 $x$ 位于 $g$ 的定义域中，则 $g(x) < M + \varepsilon$。但定理中的条件保证我们：必然存在至少一个点，比方说 $x = z$，同时满足这两个条件。那将意味着
> 
> ```math
> g(z) < M + \varepsilon < L - \varepsilon < f(z).
> ```
> 
> 这是不可能的，因为它与「$f(x)$ 的一切值都小于 $g(x)$ 的值」这一事实相矛盾。这一矛盾完成了证明。$\square$

<span style="color:#2471a3;">**[note]**</span> **原文注意（Note）**

> 这里有一个我们在讨论 sequence limits（数列极限）时曾经遇到过的 trap（陷阱）。我们记得，条件 $s_n < t_n$ 并不蕴含
> 
> ```math
> \lim_{n\to\infty} s_n < \lim_{n\to\infty} t_n.
> ```

---

> <span style="color:#7f8c8d;">—— 书页 p.196 ——</span>

> 同样地，条件 $f(x) < g(x)$ 也不蕴含
> 
> ```math
> \lim_{x\to x_0} f(x) < \lim_{x\to x_0} g(x).
> ```
> 
> 这一点也要当心。

### <span style="color:#2471a3;">**[corollary]**</span> <span style="color:#c0392b">Corollary 5.20（推论 5.20）</span>

> <span style="color:#7f8c8d;">TBB §5.2.4, p.196</span>

设极限 $\lim_{x\to x_0} f(x)$ 存在，且对所有 $x \in \operatorname{dom}(f)$ 都有 $\alpha \le f(x) \le \beta$。则

```math
\alpha \le \lim_{x\to x_0} f(x) \le \beta.
```

<span style="color:#2471a3;">**[note]**</span> **原文注意（Note）**

> 再次提醒，别忘了这个陷阱。条件「对所有 $x$ 有 $\alpha < f(x) < \beta$」至多蕴含
> 
> ```math
> \alpha \le \lim_{x\to x_0} f(x) \le \beta.
> ```
> 
> 它并不蕴含
> 
> ```math
> \alpha < \lim_{x\to x_0} f(x) < \beta.
> ```

下一个定理是这些主题的另一个有用的变体。这里，一个未知的函数被夹在两个极限行为已知的函数之间，从而使我们能够断定某个极限存在。这个定理常常以「夹逼定理」（the Squeeze Theorem）的名称来讲授，正如定理 2.20 的 version for sequences（数列版本）被如此称呼一样。这里我们要求这些函数具有相同的定义域。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 5.21 (Squeeze Theorem)（定理 5.21 · 夹逼定理）</span>

> <span style="color:#7f8c8d;">TBB §5.2.4, p.196</span>

设 $f, g, h: E \to \mathbb{R}$，且 $x_0$ 是 common domain（公共定义域）$E$ 的一个 point of accumulation（聚点）。设极限

```math
\lim_{x\to x_0} f(x) = L, \qquad \lim_{x\to x_0} g(x) = L
```

都存在，且对所有 $x \in E$（除可能在 $x = x_0$ 处外）都有 $f(x) \le h(x) \le g(x)$。则 $\lim_{x\to x_0} h(x) = L$。

<span style="color:#2471a3;">**[proof]**</span> **Proof（证明）:**

> 最简单的证明是使用 sequential argument（序列论证）。这留作习题 5.2.19（Exercise 5.2.19）。$\square$

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 5.22（例 5.22）</span>

> <span style="color:#7f8c8d;">TBB §5.2.4, p.196</span>

我们来证明极限

```math
\lim_{x\to 0} x\sin(1/x) = 0
```

是成立的。当然，表达式 $\sin(1/x)$ 起初看起来令人棘手。但我们注意到不等式

```math
-|x| \le x\sin(1/x) \le |x|
```

> <span style="color:#1e8449;">**[译者注]** 原文在本页末尾截断，示例 5.22 的后续推导见下一书页。</span>

---

> <span style="color:#7f8c8d;">TBB §5.2.4, p.197</span>

（接上页例 5.22 的证明）这些不等式对所有 $x$ 都成立（除 $x = 0$ 处函数未定义）。由于

```math
\lim_{x\to 0}|x| = \lim_{x\to 0}(-|x|) = 0 ,
```

由定理 5.21（Squeeze Theorem，挤压定理）即得我们的结论。

---

在 order structure（序结构）这一主题上，还常常需要一条最后的定理。我们记得，absolute value（绝对值）是直接依据序结构来定义的。极限运算会保持绝对值吗？由于证明不需要任何新的思想，这一问题被留作习题 5.2.21。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 5.23（定理 5.23）：Limits of Absolute Values（绝对值的极限）</span>

> <span style="color:#7f8c8d;">TBB §5.2.4, p.197</span>

设极限

```math
\lim_{x\to x_0} f(x) = L
```

存在。则

```math
\lim_{x\to x_0}|f(x)| = |L| .
```

由 maxima and minima（最大值与最小值）可以用绝对值来表示，于是有一条有时很有用的推论。

### <span style="color:#2471a3;">**[corollary]**</span> <span style="color:#c0392b">Corollary 5.24（推论 5.24）：Max/Min of Limits（极限的最大值与最小值）</span>

> <span style="color:#7f8c8d;">TBB §5.2.4, p.197</span>

设极限

```math
\lim_{x\to x_0} f(x) = L
```

与

```math
\lim_{x\to x_0} g(x) = M
```

都存在，并且 $x_0$ 是 $\mathrm{dom}(f) \cap \mathrm{dom}(g)$ 的一个 point of accumulation（聚点）。则

```math
\lim_{x\to x_0} \max\{f(x), g(x)\} = \max\{L, M\}
```

且

```math
\lim_{x\to x_0} \min\{f(x), g(x)\} = \min\{L, M\} .
```

<span style="color:#2471a3;">**[proof]**</span> **Proof（证明）**（虚化显示）:

> 其中第一个结论由恒等式
> 
> ```math
> \max\{f(x), g(x)\} = \frac{f(x) + g(x)}{2} + \frac{|f(x) - g(x)|}{2}
> ```
> 
> 以及关于和的 theorem on limits of sums（极限定理）与关于绝对值的 theorem on limits of absolute values（极限定理）推出。第二个结论同样由
> 
> ```math
> \min\{f(x), g(x)\} = \frac{f(x) + g(x)}{2} - \frac{|f(x) - g(x)|}{2}
> ```
> 
> 推出。$\square$

---

> <span style="color:#7f8c8d;">（习题 5.2.17–5.2.22 按约定保留英文原文，未收录。）</span>

---

---

> <span style="color:#1e8449;">**[note] Note（译者注）——标题：ε-剥离法——不等式反证的标准战术**</span>
> 
> 定理 5.19（$f(x) \le g(x)$ 处处成立 $\implies$ $\lim f \le \lim g$）的证明展示了一个值得命名的证明策略模板——我称之为 **ε-剥离法**。战术骨架分三步：（1）**反设极限反转**：假设 $L = \lim f > \lim g = M$；（2）**选 ε 制造隔离带**：取 $\varepsilon < \frac{L-M}{2}$，使得 $M+\varepsilon < L-\varepsilon$——这两个数之间的空隙把 $g$ 的取值上界和 $f$ 的取值下界严格隔开；（3）**用极限定义反向收紧**：由极限定义，足够靠近 $x_0$ 时 $g(x) < M+\varepsilon$ 且 $f(x) > L-\varepsilon$，于是 $g(x) < M+\varepsilon < L-\varepsilon < f(x)$，与 $f(x) \le g(x)$ 矛盾。这个模板的核心是 **ε 选取的算术**——$\frac{L-M}{2}$ 不是随便取的，它精确地创造了 $M+\varepsilon$ 和 $L-\varepsilon$ 之间的隔离区。同样的技巧你在证明数列极限唯一性（定理 2.8）时已经见过。注意定理后面的陷阱提示（p.196）：严格不等式 $f(x) < g(x)$ 推不出严格极限不等式 $\lim f < \lim g$——例：$f(x)=0$, $g(x)=|x|$ 在 $x\to 0$ 时有 $f\lt g$ 处处成立但 $\lim f = \lim g = 0$。这里的本质原因是极限运算把「严格序」降级为「非严格序」，就像你在 6.042J 偏序理论中学过的：序在「取上确界/下确界」这一运算下只能保持非严格方向。

---

---

> <span style="color:#1e8449;">**[note] Note（译者注）——标题：夹逼——分析学中最廉价的存在性证明**</span>
> 
> 夹逼定理（Squeeze Theorem）是实分析中最高效的极限存在性工具之一：你不需要直接处理 $h(x)$ 的复杂表达式，只需找到两个「钳制」它的函数 $f$ 和 $g$，证明它们有共同极限 $L$，$h$ 的极限就自动锁定为 $L$。Example 5.22 中 $x\sin(1/x)$ 的极限堪称经典——$\sin(1/x)$ 在 $x\to 0$ 时振荡得令人绝望（频率趋于无穷），但因为正弦始终在 $[-1,1]$ 之间，乘以 $x$ 后被钳制在 $-|x|$ 和 $|x|$ 之间，而 $\pm|x|$ 的极限是 0。这和你将来在算法课（📖 CLRS §3.1）分析时间复杂度时用渐近界（asymptotic bound）夹逼一个难以精确求解的递推式是同一个哲学：不求精确表达式，只找上下界。🎥 *Colding 教授*（V09 讲到连续函数的代数法则时评注）道出了这种模式的普遍性："together with some algebraic rules that are similar to the algebraic rules that we had for sequences, then we get a huge number of examples."（翻译：配合一些与数列代数法则相似的代数法则，我们就能得到大量例子。）夹逼定理正是这种「批量产出极限」的杠杆之一——一个精心构造的不等式链 + 两条已知极限 = 第三条极限自动得证。

---

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">5.2.5 Composition of Functions（函数的复合）</span>

> <span style="color:#7f8c8d;">TBB §5.2.5, p.198</span>

在研究极限的过程中，你会注意到一个颇具吸引力的模式。下列例子提示出这种模式：

```math
\lim_{x\to x_0}[f(x)]^2 = \left(\lim_{x\to x_0} f(x)\right)^2 ,
```

```math
\lim_{x\to x_0}\sqrt{f(x)} = \sqrt{\lim_{x\to x_0} f(x)} ,
```

```math
\lim_{x\to x_0} e^{f(x)} = e^{\lim_{x\to x_0} f(x)} .
```

第一个例子很容易证明，因为 $[f(x)]^2 = f(x) f(x)$，且我们可以使用 product rule（乘积法则）。平方根的例子要困难一些，但可以用 ε-δ 论证（ε-δ argument）来证明，而且只需假设 $\lim_{x\to x_0} f(x)$ 为正。若 $\lim_{x\to x_0} f(x) = 0$，它可能不成立；若 $\lim_{x\to x_0} f(x) < 0$，则它肯定不成立。

第三个例子需要对 exponential function（指数函数）有一定的熟悉，并且更加困难，不过它总是成立的。

一般模式如下：某个函数 $F$ 与 $f$ composed（复合），而我们希望使用的极限计算是

```math
\lim_{x\to x_0} F(f(x)) = F\left(\lim_{x\to x_0} f(x)\right) .
```

这一点能够被证明吗？更确切地说，在什么样的条件下它能够被证明？

让我们用 sequence argument（序列论证）来分析这个问题，因为它常常能简化函数极限。我们假设 $x_n \to x_0$。于是我们就有假设 $f(x_n) \to L$。我们能否得出结论 $F(f(x_n)) \to F(L)$？

这正是我们试图使用

```math
\lim_{x\to x_0} F(f(x)) = F\left(\lim_{x\to x_0} f(x)\right)
```

时所做的事情。

我们所期望的函数 $F$ 应具有的性质很简单：若 $z_n \to z_0$，则 $F(z_n) \to F(z_0)$。试想 $z_n = f(x_n)$；于是 $z_n \to L$，而所需要的性质就是：只要 $z_n \to L$，就有 $F(z_n) \to F(L)$。

---

> <span style="color:#7f8c8d;">TBB §5.2.5, p.199 —— 承接上一页：复合极限定理 Theorem 5.25 的收官与连续性的引入</span>

<span style="color:#2471a3;">**[paragraph]**</span> 这等价于要求

```math
\lim_{z \to L} F(z) = F(L).
```

<span style="color:#2471a3;">**[paragraph]**</span> 于是我们便证明了下面的定理，它彻底地回答了我们关于如何为前述运算（即把极限运算移入复合函数 $F$ 内部）提供依据的问题。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 5.25（定理 5.25）</span>

> <span style="color:#7f8c8d;">TBB §5.2.5, p.199</span>

设 $F$ 为在点 $L$ 的某 neighborhood（邻域）内有定义、且满足

```math
\lim_{z \to L} F(z) = F(L)
```

的函数。若

```math
\lim_{x \to x_0} f(x) = L,
```

则

```math
\lim_{x \to x_0} F(f(x)) = F\!\left(\lim_{x \to x_0} f(x)\right) = F(L).
```

<span style="color:#2471a3;">**[paragraph]**</span> 对函数 $F$ 所提出的条件

```math
\lim_{z \to L} F(z) = F(L)
```

被称为在点 $L$ 处的 continuity（连续性），这正是第 5.4 节的主题。

---

> <span style="color:#7f8c8d;">习题区（Exercises，书页 p.199）：习题 5.2.23–5.2.30 按约定保留英文原文，不收录。</span>

---

---

> <span style="color:#1e8449;">**[note] Note（译者注）——标题：复合极限——连续性概念诞生的第一性原理现场**</span>
> 
> 定理 5.25 是整个 §5.2 最有哲学意味的结果。TBB 的推导路径是从一个朴素愿望出发的：我们想写 $\lim_{x\to x_0} F(f(x)) = F(\lim f(x))$——把极限号「穿过」外层函数 $F$。序列分析揭示了使此式成立的外层函数 $F$ 必须满足的条件：$\lim_{z\to L} F(z) = F(L)$，即 $F$ 在 $L$ 处连续。这一推理方向是「复合需要连续」——它不是先定义了连续性再推导复合法则，而是反过来：**复合极限的可交换性要求外函数连续，连续性概念正是从这一功能需求中结晶出来的**。这是第一性原理思维的经典案例：不要接受「连续性就是不断开」这样的表面定义，而要追问「什么性质使得 $\lim F(f(x)) = F(\lim f(x))$ 成立？」——答案就是 $\lim_{z\to L}F(z)=F(L)$。🎥 *Colding 教授*（V10 证明复合连续性时）揭示了证明策略：「you sort of to start backwards」（翻译：你得从后面开始。）证明结构是一个 ε-δ 的「接力」：由 $g$ 的连续性得到 $\delta_g$，再把 $\delta_g$ 当作 $f$ 的「目标 ε」，由 $f$ 的连续性得到 $\delta_f$。这是 δ 作为「传递精度」的链式反应——和你在算法课学动态规划（📖 CLRS §15）时的「最优子结构」递推有深层结构上的相似：每一步的精度要求都由上一步的连续性保证来满足。

---

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">5.2.6 Examples（例）</span>

> <span style="color:#7f8c8d;">TBB §5.2.6, p.200</span>

### <span style="color:#c0392b">**Examples（例子）**</span>

<span style="color:#2471a3;">**[paragraph]**</span> 有一批众所周知的极限例子，是每个学生都应该掌握的。这在一定程度上是因为后续课程会期望学生已经见过它们。但更重要的是，需要大量的例子来获得洞察：极限何时存在、何时不存在，以及它们如何表现。

<span style="color:#2471a3;">**[paragraph]**</span> 对任何在点 $x_0$ 附近有定义的函数 $f$，有几种可能性值得我们去寻找。

1. 极限 $\lim_{x \to x_0} f(x)$ 是否存在？
2. 若极限存在，它是否等于最有可能的取值，即

```math
\lim_{x \to x_0} f(x) = f(x_0) ?
```

（这样的函数被称为在点 $x_0$ 处 continuous（连续）的。）
3. 若极限不存在，那么会不会出现这样的情况：one-sided limits（单侧极限）都存在，但恰好彼此不相等，即

```math
\lim_{x \to x_0^+} f(x) \ne \lim_{x \to x_0^-} f(x) ?
```

（这样的函数被称为在点 $x_0$ 处具有 jump discontinuity（跳跃不连续）。）

<span style="color:#2471a3;">**[paragraph]**</span> 最常见的情形，也就是

```math
\lim_{x \to x_0} f(x) = f(x_0),
```

是用连续性的语言来描述的。对连续性的研究将在下一节进行。不过，我们现在就应该意识到：一个函数究竟在何时具有这一性质。

### <span style="color:#c0392b">**Polynomials（多项式）**</span>

<span style="color:#2471a3;">**[paragraph]**</span> 所有 polynomial functions（多项式函数）的极限都是完全可以预测的。若

```math
p(x) = a_0 + a_1 x + a_2 x^2 + \cdots + a_n x^n,
```

则对每一个取值 $x_0$ 都有

```math
\lim_{x \to x_0} p(x) = p(x_0).
```

（用我们随后将采用的语言来说，这些函数都是 continuous（连续的）。）为证明这一点，我们可以利用 $\lim_{x \to x_0} a_0 = a_0$ 与 $\lim_{x \to x_0} x = x_0$ 这两个事实。它们都是容易证明的。然后，多项式就是由这些出发、通过加法与乘法逐步构造起来的。第 5.2.3 节的定理可以用来完成这一验证[例如，由 product rule（乘积法则）可得 $\lim_{x \to x_0} x^2 = x_0^2$；再次运用乘积法则可得 $\lim_{x \to x_0} x^3 = \lim_{x \to x_0} (x)(x^2) = x_0^3$]。

### <span style="color:#c0392b">**Rational Functions（有理函数）**</span>

<span style="color:#2471a3;">**[paragraph]**</span> rational function（有理函数）是形如

```math
R(x) = \frac{p(x)}{q(x)}
```

的函数，其中 $p$ 与 $q$ 都是多项式（即两个多项式之比，其名称也由此而来）。由于我们可以取极限，

```math
\lim_{x \to x_0} R(x) = \frac{\lim_{x \to x_0} p(x)}{\lim_{x \to x_0} q(x)} .
```

---

> <span style="color:#7f8c8d;">TBB §5.2.6, p.201</span>

由于我们可以自由地取 limit（极限）——唯一要排除的是分母为零的情形——我们已经发现 $\lim_{x \to x_0} R(x) = R(x_0)$，但在那些满足 $q(x_0) = 0$ 的点除外。

在这些点处，极限仍有可能存在。不过请注意，它不可能等于 $R(x_0)$，因为 $R(x_0)$ 根本没有被定义。right-hand limit（右极限）和 left-hand limit（左极限）也有可能成为 infinite（无穷大）。习题中有一些例子可以说明这些可能性。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Exponential Functions（指数函数）</span>

可以证明，exponential function（指数函数）$e^x$ 具有我们所预期的极限值，即 $\lim_{x \to x_0} e^x = e^{x_0}$。

要证明这一点，取决于我们最初是如何定义指数函数的。发展这样的理论有多种途径。通常的做法是等待 theoretical apparatus（理论工具）就绪，然后再用一种能够充分利用这些工具的方式来定义指数函数。

回想我们在例 2.36（Example 2.36）中提到过

```math
e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots + \frac{x^n}{n!} + \cdots
```

像这样的和式被称为 power series（幂级数）。作为幂级数理论的一部分，我们将精确地弄清它们何时是连续的。这样一来，就可以把指数函数定义为一个幂级数，并立即断言其连续性。

微积分中的大多数 elementary function（初等函数）——trigonometric function（三角函数）、inverse trigonometric function（反三角函数）等——都可以用这种方式处理。此处我们不再停留下来为这类函数的极限操心。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Characteristic Function of the Rationals（有理数的特征函数）</span>

实数集合 $E$ 的 characteristic function（特征函数）是这样一个函数：它在 $E$ 中的点处取值 $1$，在 $E$ 之外的点处取值 $0$。

有些作者称它为 indicator function（示性函数），因为它确实 indicate（指示）了一个点是否属于该集合。

为了给出一个在微积分早期会被视为 bizarre（怪异）的函数的有趣例子，我们考虑有理数的特征函数：

```math
\chi_{\mathbb{Q}}(x) = 
\begin{cases}
1, & \text{if } x \in \mathbb{Q},\\
0, & \text{if } x \notin \mathbb{Q}.
\end{cases}
```

不难验证，$\lim_{x \to x_0^+} \chi_{\mathbb{Q}}(x)$ 与 $\lim_{x \to x_0^-} \chi_{\mathbb{Q}}(x)$ 两者都不存在。

> <span style="color:#7f8c8d;">TBB §5.2.6, p.202</span>

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Dirichlet Function（狄利克雷函数）</span>

在 $[0, 1]$ 上定义 Dirichlet function（狄利克雷函数）如下：

```math
f(x) = 
\begin{cases}
0, & \text{if } x \text{ is irrational or } x = 0,\\
1/q, & \text{if } x = p/q,\ p, q \in \mathbb{N},\ p/q \text{ in lowest terms}.
\end{cases}
```

要考察这个函数的 limiting behavior（极限行为），我们需要注意到：虽然使函数取正值的点有很多（所有有理数都是），但函数取值大于某个正数 $\varepsilon$ 的点却并不多。

事实上，如果我们去数一数就会发现：对任意正整数 $q$，点集

```math
S_q = \{ x \in [0,1] : f(x) \geq 1/q \}
```

至多含有 $\frac{q(q-1)}{2}$ 个点。这个确切数目并不重要；我们只需观察到，这样的点只有有限多个。

于是任取 $\varepsilon > 0$，并选择一个足够大的整数 $q$，使得 $1/q < \varepsilon$。对任意一点 $x_0$，我们都可以选取 $\delta > 0$，使得两个区间 $(x_0 - \delta, x_0)$ 与 $(x_0, x_0 + \delta)$ 都不含有限集合 $S_q$ 中的点。这就必然意味着，$(x_0 - \delta, x_0)$ 或 $(x_0, x_0 + \delta)$ 中每一点 $x$ 都满足

```math
0 \leq f(x) < 1/q < \varepsilon
```

由此可知，在每一点 $x_0$ 处都有 $\lim_{x \to x_0} f(x) = 0$。

特别地，等式 $\lim_{x \to x_0} f(x) = f(x_0)$ 在每个 irrational point（无理点）$x_0$ 处成立，但在每个 rational point（有理点）处必然不成立。用连续性的语言来说，我们已经证明：这个函数在每一个无理点处连续，但在每一个有理点处不连续。

这是一个奇特的函数：它看起来在几乎每一点处都连续，却又在几乎每一点处都不连续。十九世纪的数学家们对这类函数相当着迷，称它们为 pointwise discontinuous（逐点不连续），这个术语如今似乎已不再使用。

（我们以后会不时回到这个例子。例如，习题 7.5.4 就要求对这个函数的 local extrema（局部极值）作一番说明。）

---

> <span style="color:#1e8449;">**[note] Note（译者注）——标题：狄利克雷函数——稠密性、可数性与连续性的三国演义**</span>
> 
> 狄利克雷函数 $f(p/q)=1/q$（最简分数形式）在每一无理点连续、在每一有理点不连续——这是实分析中最令初学者震惊的例子之一。你可能会想：函数不都该是「差不多连续」的吗？这个例子告诉你：不，连续点和不连续点都可以在 $[0,1]$ 上「密密麻麻」地交错。证明的核心依赖于你在 6.042J 数论中学过的最简分数概念，以及一个关键的组合观察：对任意正整数 $q$，使 $f(x) \ge 1/q$ 的点（即分母不超过 $q$ 的有理数）在 $[0,1]$ 中只有有限多个。这个有限性保证了：任取 $\varepsilon > 0$，只需选 $q$ 使得 $1/q < \varepsilon$，那么在任意 $x_0$ 附近我们总可以找到一个足够小的邻域，完全避开那有限个「大值点」——邻域内所有剩余的 $f(x)$ 都 $< 1/q < \varepsilon$，于是极限为 0。这实际上是一个 **有限避让法**（finite avoidance）的证明模板：用「坏点」的有限性来保证「好邻域」的存在性。对比有理数特征函数 $\chi_{\mathbb{Q}}$（p.201），它处处不连续——因为不管邻域多小，其中总既有有理数（使函数值为 1）又有无理数（使函数值为 0），极限永远不存在。两个函数看似相似（都在有理数处有特殊行为），一个「几乎处处连续」，一个「处处不连续」，差异全在于 $\chi_{\mathbb{Q}}$ 的取值跳跃不会随分母增大而减小。这也为你后续理解勒贝格积分（Lebesgue integral）埋下了伏笔：狄利克雷函数是黎曼不可积但勒贝格可积的典型例子——不过这个话题要等到你学测度论时再展开。

# TBB Ch5 译者注（notes_2）—— §5.3–§5.5

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Nondecreasing Functions with Jumps（带跳跃的非降函数）</span>

具有不连续点的函数的最简单例子，也许就是

```math
H(x) = 
\begin{cases}
0, & \text{if } x < 0,\\
1, & \text{if } x \geq 0.
\end{cases}
```

这个函数在 $x = 0$ 处没有极限，因为 $\lim_{x \to 0^+} H(x) = 1$ 而 $\lim_{x \to 0^-} H(x) = 0$。用本节早先引入的语言来说，我们会称 $H$ 在点 $0$ 处有一个 jump（跳跃），即 jump discontinuity（跳跃不连续）。

这个不连续点可以移到任意位置。函数 $H(x - c)$ 在 $x = c$ 处有一个跳跃。此外，若 $c_1 < c_2 < c_3 < \cdots < c_k$ 是由有限个 distinct points（互异点）组成的序列，则函数

```math
F(x) = \sum_{i=1}^{k} H(x - c_i)
```

是一个 nondecreasing（非降）函数，在点 $c_1, c_2, c_3, \ldots, c_k$ 中的每一个处都有跳跃。在其余每一点 $x_0$ 处，都有 $\lim_{x \to x_0} F(x) = F(x_0)$。

现在出现了一个有趣的问题。我们已经成功地构造出一个非降函数，它在预先指定的有限点集处有跳跃。如果我们希望它在给定的 infinite set（无穷点集）处有跳跃，我们还能构造出这样的函数吗？这是一个我们将会回过来讨论的问题。

---

> <span style="color:#7f8c8d;">TBB §5.2.6, p.203</span>

图 5.2（Figure 5.2）描绘了一个 step function（阶梯函数）的图像。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Step Functions（阶梯函数）</span>

若一个函数 $f$ 只取有限多个值，设为 $b_1, b_2, \ldots, b_N$，且对每个 $1 \le i \le N$，集合

```math
f^{-1}(b_i) = \{x : f(x) = b_i\},
```

即 $f$ 取值 $b_i$ 的那些点所成的集合，是有限多个区间与 singleton point sets（单点集）的并集，则称 $f$ 为 step function（阶梯函数）。

看待此事的另一种方式是：形如

```math
f(x) = \sum_{i=1}^{M} a_i \chi_{A_i}(x)
```

的函数是 step function（阶梯函数），只要所有 $A_i$ 都是区间或单点集即可。（图示可参见图 5.2（Figure 5.2）。）

阶梯函数在 integration theory（积分理论）中发挥着重要作用。

它们提供了一种 approximating（粗略逼近）函数的方式。

我们刚刚见过的函数

```math
H(x) = \begin{cases} 0 & \text{if } x < 0 \\ 1 & \text{if } x \ge 0 \end{cases}
```

就是一个简单的阶梯函数，因为它只取两个值 0 与 1：其中 0 在区间 $(-\infty, 0)$ 上取得，1 在 $[0, \infty)$ 上取得。

阶梯函数的 discontinuities（不连续点）很容易识别。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Distance of a Closed Set to a Point（闭集到某点的距离）</span>

设 $C$ 为 closed set（闭集），并定义函数

```math
d(x,C) = \inf\{|x - y| : y \in C\}.
```

这个函数为"集合 $C$ 与点 $x$ 之间的距离"赋予了确切的含义。

若 $x_0 \in C$，则 $d(x_0, C) = 0$；若 $x_0 \notin C$，则 $d(x_0, C) > 0$。

该函数在每一点都 continuous（连续）；也就是说，它满足性质

```math
\lim_{x \to x_0} d(x,C) = d(x_0, C). \tag{1}
```

我们可以对式 (1) 作出几何解释：若两个点 $x_1$ 与 $x_2$ 彼此靠得很近，则它们到闭集 $C$ 的距离大致相同。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">The Characteristic Function of the Cantor Set（康托集的特征函数）</span>

设 $K$ 为 Cantor set（康托集），$\chi_K$ 为其 characteristic function（特征函数）；也就是说，若 $x \in K$ 则 $\chi_K(x) = 1$，否则 $\chi_K(x) = 0$。

> <span style="color:#7f8c8d;">TBB §5.2.6, p.204</span>

这个函数具有如下性质：

```math
\lim_{x \to x_0} \chi_K(x) = 0
```

只要 $x_0$ 不在康托集中；而在康托集中的任何一点处，该极限都不存在。

若要给出此结论的简便证明，你需要回顾习题 4.3.23 与 4.4.9 中关于康托集及其 complement（补集）的性质。

---

> <span style="color:#7f8c8d;">本页尾部为 §5.2 习题区（Exercises 5.2.31–5.2.38，书页 p.204），按约定跳过，不收录。</span>

---

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">5.3 Limits Superior and Inferior（上极限与下极限）</span>

> <span style="color:#7f8c8d;">TBB §5.3, p.205</span>

> **[note]** 原文标注：**Advanced section**（高级章节），**May be omitted**（可略过）。

如果极限不存在，我们也大可不必放弃讨论 limiting behavior（极限行为）的全部希望。

在 §2.13 研究 sequence limit（序列极限）时，我们就已经见过这种情形。

即使 $\{s_n\}$ 发散、从而 $\lim_{n \to \infty} s_n$ 不存在，仍然有可能由两个极端极限 limit superior (limsup)（上极限）$\limsup_{n \to \infty} s_n$ 与 limit inferior (liminf)（下极限）$\liminf_{n \to \infty} s_n$ 提供一些有意义的信息。

这两个概念总是存在（可能取 $\infty$ 或 $-\infty$）。

对函数而言，也会出现类似的情形。

在许多方面，这一理论几乎是完全相同的。

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#c0392b">Definition 5.26 (Lim Sup and Lim Inf)（定义 5.26：上极限与下极限）</span>

> <span style="color:#7f8c8d;">TBB §5.3, p.205</span>

设 $f : E \to \mathbb{R}$ 是以 $E$ 为 domain（定义域）的函数，并假设 $x_0$ 是 $E$ 的一个 point of accumulation（聚点）。

则我们记

```math
\limsup_{x \to x_0} f(x) = \inf_{\delta > 0} \sup\{ f(x) : x \in (x_0 - \delta, x_0 + \delta) \cap E,\ x \neq x_0 \}
```

以及

```math
\liminf_{x \to x_0} f(x) = \sup_{\delta > 0} \inf\{ f(x) : x \in (x_0 - \delta, x_0 + \delta) \cap E,\ x \neq x_0 \}
```

由于本节面向更高阶的读者，我们已把这一概念的发展与展开留给习题处理。

---

---

> <span style="color:#1e8449;">**[note] Note（译者注）——标题：limsup 的「inf-sup」结构：从序列到函数的统一模板**</span>
> 
> 函数版本的 limsup 定义式 $\limsup_{x \to x_0} f(x) = \inf_{\delta > 0} \sup\{ f(x) : x \in (x_0 - \delta, x_0 + \delta) \cap E, x \neq x_0 \}$ 与序列版本 $\limsup_{n \to \infty} s_n = \inf_{n \ge 1} \sup_{k \ge n} s_k$ 共享完全相同的「外层 inf 夹内层 sup」结构。这不是巧合：序列情形中，$\sup_{k \ge n} s_k$ 是「从第 $n$ 项起的最大上界」，然后令 $n \to \infty$ 取 inf 捕获「最终上界」；函数情形中，$\sup_{x \in (x_0 - \delta, x_0 + \delta)} f(x)$ 是「在以 $x_0$ 为中心、半径 $\delta$ 的窗内的最大上界」，然后令 $\delta \to 0$ 取 inf 捕获「无限逼近 $x_0$ 时的上界」。这一统一模式帮你把已学知识（📖 L04 序列极限）迁移到新情境——你只需把「指标 $n$ 的增大」替换为「邻域半径 $\delta$ 的收缩」。在算法分析中也有类似思想：二分搜索的「上界不断收紧」（📖 6.006 §1.3）本质上也是一种 inf-sup 迭代——每次迭代收紧搜索区间，等价于用越来越小的 $\delta$ 逼近目标。

---

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">5.4 Continuity（连续性）</span>

> <span style="color:#7f8c8d;">TBB §5.4, p.207</span>

对“连续性”一词最早的使用，多少被对 function（函数）本质的误解所遮蔽。

在十八世纪，如果一个函数由单个公式给出，那么就认为它是 continuous（连续的）。

然而，如果函数在公式上出现了“断裂”——在一个区间上这样定义、在另一个区间上又另作定义——那么就认为它是 discontinuous（不连续的）。

随着这门学科的发展，这些观念仍继续遮蔽着真正重要的思想。

奥古斯丁·柯西（Augustin Cauchy，1789–1857）是第一个给出现代定义的人，并把注意力集中到如今在 analysis（分析学）中已占据如此重要地位的那个概念上。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">5.4.1 How to Define Continuity（如何定义连续性）</span>

> <span style="color:#7f8c8d;">TBB §5.4.1, p.207</span>

> <span style="color:#2471a3;">**[note]**</span> **原文注记：** 本节为 Enrichment（提高）部分，可略过。

在我们着手现今的定义之前，让我们先考虑另一个 notion（观念）。

甚至迟至十九世纪中叶，仍有一些数学家相信，这一观念应当构成连续性定义的基础。

这一概念由“图像没有跳跃”这一说法所启示。

虽然一些 calculus（微积分）课程的教师可能会用这类说法向学生传达连续的感觉，但这句话并不精确，也不能完全传达我们所期望的 continuous function（连续函数）应具备的全部含义。

不过，这一观念与连续性有关联，而且它本身就有一定的重要性。

我们将从对它的简要讨论开始。

下面就是使我们的说法精确化的一次尝试。（参见图 5.3。）

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">Definition 5.27（定义 5.27）：(Intermediate Value Property 介值性质)</span>

> <span style="color:#7f8c8d;">TBB §5.4.1, p.207</span>

<span style="color:#00838f">设 $f$ 定义在 interval（区间）$I$ 上。</span>

<span style="color:#00838f">假设对每一对满足 $f(a) \neq f(b)$ 的 $a, b \in I$，以及位于 $f(a)$ 与 $f(b)$ 之间的每一个 $d$，都存在位于 $a$ 与 $b$ 之间的 $c$，使得 $f(c) = d$。</span>

<span style="color:#00838f">这时我们就说，$f$ 在 $I$ 上具有 intermediate value property（介值性质，简称 IVP）。</span>

---

> <span style="color:#7f8c8d;">书页 208（PDF 页 24）</span>

<span style="color:#2471a3;">**[figure]**</span> **Figure 5.3（图 5.3）**：在 $a$ 与 $b$ 之间的某一点处，函数取到介于 $f(a)$ 与 $f(b)$ 之间的任意给定值 $d$。

<span style="color:#2471a3;">**[figure]**</span> **Figure 5.4（图 5.4）**：函数 $F(x) = \sin x^{-1}$ 在 $[-\pi/8, \pi/8]$ 上的图像。

具有这一性质的函数被称为 Darboux functions（达布函数），这一命名源自让·加斯东·达布（Jean Gaston Darboux，1842–1917）；他在 1875 年证明了：对定义在 interval（区间）$I$ 上的每一个 differentiable function（可微函数）$F$，其导数 $F'$ 在 $I$ 上都具有 IVP。

他还因 1875 年用 upper and lower sums（上和与下和）论述 Riemann integral（黎曼积分）而尤为著名；人们常常提到“Darboux integral（达布积分）”，所指正是这一版本的经典黎曼积分。

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">**Example 5.28（例 5.28）**</span>

> <span style="color:#7f8c8d;">TBB §5.4.1, p.208</span>

设

```math
F(x) = \begin{cases}
\sin x^{-1} & \text{if } x \neq 0 \\
0 & \text{if } x = 0.
\end{cases}
```

$F$ 的图像见图 5.4。

你或许希望验证 $F$ 具有 IVP。

特别地，在 $x = 0$ 的每一个 neighborhood（邻域）中，$F$ 都无穷多次地取到区间 $[-1, 1]$ 中的每一个值。$\square$

我们还没有把“图像没有跳跃”这句话弄得精确，不过 IVP 似乎已经足够好地传达了这一想法。

既然这个性质如此易于描述，而且其内容似乎也易于直观想象，那我们何不把它作为连续性的定义呢？

在尝试回答这个问题之前，让我们提出一个与之竞争的表述来把握连续性的想法：“如果 $x$ 靠近 $x_0$，那么 $f(x)$ 就靠近 $f(x_0)$。”

照目前的表述来看，这句话并不精确，但我们可以借助 limit（极限）概念使它变得精确。

这句话实际上可以被解释为断言：

```math
f(x_0) = \lim_{x \to x_0} f(x). \tag{2}
```

---

> <span style="color:#7f8c8d;">TBB §5.4, p.209</span>

<span style="color:#1e8449;">**译者注：**</span> 本页开头这几段是 §5.4.1 "How to Define Continuity（如何定义连续性）" 正文的收尾，紧接上一页的方程 (2) $f(x_0) = \lim_{x \to x_0} f(x)$；随后的习题 5.4.1–5.4.6（含 Figure 5.5）按约定跳过，未收录。

根据这一判据（According to this criterion），例 5.28 中的函数 $F$ 在 $x_0 = 0$ 处就不会是 continuous（连续的），因为 $F(0) = 0$，但 $\lim_{x \to 0} F(x)$ 并不存在。

我们很快就会看到，limit（基于极限）的这一定义能够发展出一套有用的理论。

我们将会看到，class of continuous functions（连续函数类）[正如利用方程 (2) 所定义的那样] 对加法与乘法都是 closed under addition and multiplication（封闭的），并且这类函数还具有许多其他合乎需要的 properties（性质）。

例如，这个函数类对某些类型的 limits of sequences（序列极限）是封闭的，而且 $[a, b]$ 上的每一个连续函数都是 integrable（可积的）。

另一方面（正如习题中所展示的），对于 IVP, 由 intermediate value property（介值性质）所定义的函数类来说，上述论断没有一条是成立的。

因此，基于 limit concept（极限概念）的 continuity（连续性）理论拥有丰富的结构，享有广泛的适用性；而基于 IVP 的理论则相当有限。

此外，极限这一基本概念可以推广到远比 $\mathbb{R}$ 更一般的场合。

相比之下，IVP 的推广虽然也可能实现，但在数学分析中始终处于 peripheral（边缘）地位。

---

---

> <span style="color:#1e8449;">**[note] Note（译者注）——标题：为什么「图像没有跳跃」不是连续性的正确定义**</span>
> 
> TBB 在 §5.4.1 中展示了两条定义连续性的竞争道路：IVP（介值性质，即「图像不该跳过的值都取到了」）和 Cauchy 的极限定义（「$x$ 靠近 $x_0$ 则 $f(x)$ 靠近 $f(x_0)$」）。IVP 直觉极强——甚至达布（Darboux, 1875）证明了一切可微函数的导数都具有 IVP——但 TBB 随即揭示 IVP 作为定义的致命缺陷：具有 IVP 的函数类对加法、乘法不封闭，对序列极限不封闭，甚至不保证可积。这正是一个第一性原理时刻：我们不是在寻找「直觉上像连续」的性质，而是在寻找一个**能使整个理论大厦运作起来的最小公理集合**。Cauchy（1821）选择极限语言，不是因为极限比 IVP 更「直观」，而是因为它使连续函数类成为代数闭的、序列闭的、可积的——这正是「结构优先于直觉」的典范。当你学习 6.006 中数据结构的设计选择时，同样的原则也在起作用：选择 AVL 树而非普通 BST 不是因为 AVL 更「自然」，而是因为它保证 $O(\log n)$ 操作封闭性。

---

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">5.4.2 Continuity at a Point（一点处的连续性）</span>

> <span style="color:#7f8c8d;">TBB §5.4.2, p.210</span>

让我们来看一看 Cauchy（柯西）关于连续函数的概念。

我们从定义 continuity at a point（一点处的连续性）开始，更具体地说，是函数 $f$ 的 domain（定义域）中某个 interior point（内点）处的连续性。

这样一来我们便能确保：如果我们关心的是点 $x_0$ 处所发生的情形，那么 $f$ 就在 $x_0$ 的某个 neighborhood（邻域）内有定义；也就是说，$f$ 在某个区间 $(x_0 - c, x_0 + c)$ 上有定义，其中 $c$ 是一个正数。

这会简化某些计算。

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">Definition 5.29（定义 5.29）</span>

> <span style="color:#7f8c8d;">TBB §5.4.2, p.210</span>

（连续的，Continuous）设 $f$ 在 $x_0$ 的某个邻域内有定义。若 $\lim_{x \to x_0} f(x) = f(x_0)$，则称函数 $f$ 在 $x_0$ 处连续（continuous at $x_0$）。

这意味着：对 $f(x_0)$ 的每一个邻域 $V$，都存在 $x_0$ 的某个邻域 $U$，使得 $f(U) \subset V$；也就是说，若 $x \in U$，则 $f(x) \in V$。

当然，我们也可以用 $\delta$ 与 $\varepsilon$ 的语言来陈述这一定义：$f$ 在 $x_0$ 处连续，当且仅当对每个 $\varepsilon > 0$ 都存在 $\delta > 0$，使得只要 $|x - x_0| < \delta$，就有 $|f(x) - f(x_0)| < \varepsilon$。

在习题中，我们请你验证……（原文此句在下一页继续）

---

> <span style="color:#7f8c8d;">TBB §5.4.2, p.211</span>

**Figure 5.6（图 5.6）**：函数 $f(x)=1/x$ 的连续性的 neighborhood（邻域）定义的图形解释。注意 $a=1/B$，$b=1/A$。

在习题中，我们请你验证三种 formulations（表述）——涉及 limit（极限）的语言、邻域的语言，以及 $\delta$ 与 $\varepsilon$ 的语言——彼此是等价的。我们相信，对尚未对极限概念感到自如的读者来说，这是一道重要的练习。对连续性所呈现的种种形式感到自如，对于掌握随后各节、各章中出现的许多论证，是至关重要的。

注意，函数 $f$ 在 $x_0$ 处不连续可能有三种方式：

1. $f$ 在 $x_0$ 处未定义。
2. $\lim_{x\to x_0} f(x)$ 不存在。
3. $f$ 在 $x_0$ 处有定义，且 $\lim_{x\to x_0} f(x)$ 存在，但 $f(x_0)\neq\lim_{x\to x_0} f(x)$。

这三种可能情形各自的简单例子，我们留给你自己来提供。

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 5.30（例 5.30）</span>

> <span style="color:#7f8c8d;">TBB §5.4.2, p.211</span>

设 $f:(0,\infty)\to\mathbb{R}$ 由 $f(x)=1/x$ 定义。我们要证明：若 $x_0\in(0,\infty)$，则 $f$ 在 $x_0$ 处连续。

<span style="color:#2471a3;">**[proof]**</span> **Proof（证明）:**

> 我们先用连续性的「邻域」定义来尝试。设 $V$ 是 $f(x_0)$ 的一个邻域，比方说 $V=(A,B)$，于是 $A\lt f(x_0)\lt B$。我们必须找到 $x_0$ 的一个邻域 $U=(a,b)$，使得 $f(U)\subset V$。图形提示了我们该怎么做：令 $a=1/B$，$b=1/A$。（见图 5.6。）
> 
> 但在这里我们得稍加小心。在我们关于连续性的邻域定义中，没有任何一条允许我们假设 $A>0$，所以 $b$ 可能没有定义（若 $A=0$），也可能不在 $f$ 的 domain（定义域）内（若 $A<0$）。不过，这仅仅是个小小的麻烦，因此我们在证明中假设 $A>0$。
> 
> 于是我们假设 $A>0$，$a=1/B$，$b=1/A$。由于 $A\lt f(x_0)\lt B$，我们有
> 
> ```math
> b=\frac{1}{A}>\frac{1}{f(x_0)}=x_0>\frac{1}{B}=a,
> ```
> 
> 所以 $x_0\in(a,b)=U$。此外，若 $c\in U$，则 $a\lt c\lt b$，且 $B>1/c=f(c)>A$，于是 $f(c)\in V$。这表明 $f(U)\subset V$，正合所需。$\blacksquare$

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 5.31（例 5.31）</span>

> <span style="color:#7f8c8d;">TBB §5.4.2, p.212</span>

我们再取同一个例子 $f:(0,\infty)\to\mathbb{R}$，由 $f(x)=1/x$ 定义。我们再次证明：若 $x_0\in(0,\infty)$，则 $f$ 在 $x_0$ 处连续。

<span style="color:#2471a3;">**[proof]**</span> **Proof（证明）:**

> 现在我们来看看基于 $\delta$-$\varepsilon$ 定义（即连续性的 $\delta$-$\varepsilon$ 形式）的证明会是怎样一番光景。与我们的第一个证明一样，我们会提供证明中的许多细节。等你对极限与连续性相当熟练之后，你或许会希望把证明适当精简，省去那些「任何读者都觉得显然」的细节。
> 
> 设 $x_0\in(0,\infty)$，并设 $\varepsilon>0$。我们希望找到 $\delta>0$，使得若 $|x-x_0|<\delta$ 且 $x>0$，则 $|1/x-1/x_0|<\varepsilon$。把最后一个不等式改写为
> 
> ```math
> |x-x_0|<\varepsilon xx_0 \tag{3}
> ```
> 
> 这提示我们尝试取 $\delta=\varepsilon xx_0$。但 $\delta$ 应当只依赖于 $\varepsilon$ 与 $x_0$，而不依赖于 $x$。事实上，并不存在这样的 $\delta>0$：对一切 $x\in(0,\infty)$，由 $|x-x_0|<\delta$ 都能推出 $|x-x_0|<\varepsilon xx_0$。我们可以先要求 $x$ 远离 $0$ 来消除这个麻烦。例如，我们首先要求
> 
> ```math
> |x-x_0|<\frac{1}{2}x_0. \tag{4}
> ```
> 
> 于是
> 
> ```math
> \frac{1}{2}x_0<x \tag{5}
> ```
> 
> 且
> 
> ```math
> \frac{1}{2}\varepsilon x_0^2<\varepsilon xx_0. \tag{6}
> ```
> 
> 不等式 (3)、(4) 与 (6) 提示我们取
> 
> ```math
> \delta=\min\left\{\frac{1}{2}x_0,\ \frac{1}{2}\varepsilon x_0^2\right\}.
> ```
> 
> 对这个 $\delta$，我们不难算出：若 $|x-x_0|<\delta$，则
> 
> ```math
> \left|\frac{1}{x}-\frac{1}{x_0}\right|=\frac{|x-x_0|}{|xx_0|}<\frac{\frac{1}{2}\varepsilon x_0^2}{\frac{1}{2}x_0^2}=\varepsilon,
> ```
> 
> 其中最后一个不等式是这样得到的：对分子 $|x-x_0|$ 用 (6)，对分母 $|xx_0|$ 用 (5)。$\blacksquare$

---

---

> <span style="color:#1e8449;">**[note] Note（译者注）——标题：「$\varepsilon$-剥离法」——如何构造正确的 $\delta$**</span>
> 
> Example 5.31 证明 $f(x) = 1/x$ 连续的过程展示了一个关键证明技术：**从目标不等式反向构造 $\delta$，然后用 $\min$ 消去 $x$ 的依赖**。具体而言：
> (1) 目标 $|1/x - 1/x_0| < \varepsilon$ 变形为 $|x - x_0| < \varepsilon x x_0$；
> (2) 但 $\delta$ 不能包含 $x$（$\delta$ 只能依赖 $\varepsilon$ 和 $x_0$），因此先用 $|x - x_0| < \frac{1}{2} x_0$ 把 $x$ 限制在 $(\frac{1}{2}x_0, \frac{3}{2}x_0)$ 内，从而 $\varepsilon x x_0 > \frac{1}{2} \varepsilon x_0^2$；
> (3) 取 $\delta = \min\{\frac{1}{2}x_0, \frac{1}{2}\varepsilon x_0^2\}$ 同时满足两个条件。
> 这个「先用一个约束剥离 $x$，再用 $\min$ 合并多个约束」的流程在 $\varepsilon$-$\delta$ 证明中无处不在，我称它为「$\varepsilon$-剥离法」。在你后续学习一致连续性（§5.6）时，关键区别恰恰在于 $\delta$ 是否允许依赖 $x_0$——这里 $\delta$ 依赖于 $x_0$，所以只得到逐点连续性；要得到一致连续性，必须构造只依赖 $\varepsilon$ 的 $\delta$。

# TBB Chapter 5 译者注（§5.6–§5.9）

---

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">5.4.3 Continuity at an Arbitrary Point（任意点处的连续性）</span>

> <span style="color:#7f8c8d;">TBB §5.4.3, p.213</span>

到目前为止，我们讨论的都是函数在其 interior point（定义域内点）处的 continuity（连续性）。如果 $x_0$ 不是内点，我们应当如何修改这些概念呢？

例如，若 $f: [a,b] \to \mathbb{R}$，我们该如何定义 $f$ 在 $a$ 或 $b$ 处的连续性？由于函数只定义在区间 $[a,b]$ 上，而我们又是用 limit（极限）来定义连续性的，因此看来应当像以前一样要求：对任意内点 $x_0 \in (a,b)$，

```math
\lim_{x \to x_0} f(x) = f(x_0),
```

**Continuity at Endpoints（端点处的连续性）** 而在 endpoint（端点）处，连续性则应由 one-sided limit（单侧极限）来定义，

```math
\lim_{x \to a^+} f(x) = f(a) \quad \text{and} \quad \lim_{x \to b^-} f(x) = f(b).
```

我们还可以改写定义，使其体现出 $f$ 只定义在 $[a,b]$ 上这一事实。在 neighborhood definition（邻域定义）中，我们把 $U$ 解释为 $x_0$ 的 relative neighborhood（相对邻域）：即要求 $f(U \cap [a,b]) \subset V$。这里所谓相对邻域，指的是普通邻域中落在 $f$ 有定义的集合之内的那一部分。

类似地，对于 ε-δ definition（ε-δ 定义），我们的要求变成：只要 $|x - x_0| < \delta$ 且 $x \in [a,b]$，就有 $|f(x) - f(x_0)| < \varepsilon$。这里我们同样是仅仅把注意力限制在 $f$ 有定义的那个集合上。

**Continuity on an Arbitrary Set（任意集上的连续性）** 这些改写对任意集合 $A$ 都适用，而不仅仅是区间。因此我们假定 $f: A \to \mathbb{R}$，即 $f$ 是以 $A$ 为 domain（定义域）的函数，$x_0$ 是 $A$ 中任意一点——它不必是内点，甚至不必是 point of accumulation（聚点），它可能是 $A$ 中的 isolated point（孤立点）。

关于连续性，我们有四种版本的定义。和以前一样，你应该自行验证它们确实彼此等价。由于 $x_0$ 可以是 $A$ 中任意一点，并可能在 $A$ 中孤立，这里需要格外小心。

### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#c0392b">Definition 5.32: (ε-δ Version)（定义 5.32：（ε-δ 版本））</span>

> <span style="color:#7f8c8d;">TBB §5.4.3, p.214</span>

设 $f$ 定义在集合 $A$ 上，$x_0$ 是 $A$ 中任意一点。函数 $f$ 在 $x_0$ 处连续，是指对每个 $\varepsilon > 0$ 都存在一个 $\delta > 0$，使得对所有满足 $|x - x_0| < \delta$ 的 $x \in A$，都有 $|f(x) - f(x_0)| < \varepsilon$。

### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#c0392b">Definition 5.33: (Limit Version)（定义 5.33：（极限版本））</span>

> <span style="color:#7f8c8d;">TBB §5.4.3, p.214</span>

设 $f$ 定义在集合 $A$ 上，$x_0$ 是 $A$ 中任意一点。函数 $f$ 在 $x_0$ 处连续，是指要么 $x_0$ 在 $A$ 中孤立，要么 $x_0$ 是该集合的聚点且

```math
\lim_{x \to x_0} f(x) = f(x_0)
```

### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#c0392b">Definition 5.34: (Neighborhood Version)（定义 5.34：（邻域版本））</span>

> <span style="color:#7f8c8d;">TBB §5.4.3, p.214</span>

设 $f$ 定义在集合 $A$ 上，$x_0$ 是 $A$ 中任意一点。函数 $f$ 在 $x_0$ 处连续，是指对每个包含 $f(x_0)$ 的 open set（开集）$V$，都存在包含 $x_0$ 的开集 $U$，使得 $f(U \cap A) \subset V$。

换言之，邻域版本断言：存在一个相对于 $A$ open relative to A（开）的集合 $U \cap A$，$f$ 把它映入 $V$。我们回忆：若集合 $B \subset A$ 是某个开集（此处即 $U$）与 $A$ 的交集，则称 $B$ 相对于 $A$ 是 relatively open（相对开）的。

### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#c0392b">Definition 5.35: (Sequential Version)（定义 5.35：（序列版本））</span>

> <span style="color:#7f8c8d;">TBB §5.4.3, p.214</span>

设 $f$ 定义在集合 $A$ 上，$x_0$ 是 $A$ 中任意一点。函数 $f$ 在 $x_0$ 处连续，是指对属于 $A$ 且收敛于 $x_0$ 的每个点列 $\{x_n\}$，都有 $f(x_n) \to f(x_0)$。

---

---

> <span style="color:#1e8449;">**[note] Note（译者注）——标题：一个概念，四种语言：连续性的等价定义为何重要**</span>
> 
> Definition 5.32（ε-δ）、5.33（极限）、5.34（邻域/开集）、5.35（序列）给出了连续性的四种等价刻画。它们的等价性之所以不是废话，是因为每种语言适合不同的论证场景：ε-δ 适合具体计算（如 Example 5.31 证明 $1/x$ 连续），序列版本适合借助序列极限的代数性质快速迁移结论（Theorem 5.40 的证明正是利用了这一点），邻域版本适合导出整体拓扑刻画（Theorem 5.37），极限版本在概念上最贴近直观。这与你在 6.042J 中遇到的等价关系不同：那里的等价关系是一种「等于的较弱形式」；这里的四种定义是真正的逻辑等价——给定同一个底层的集合论事实，四种表述可以互相推演。理解它们如何互相推导（习题 5.4.7）是掌握后续 $\S 5.6$–$\S 5.9$ 几乎所有证明的关键，因为那些证明会在不同语言之间反复切换以利用各自优势。

---

---

> <span style="color:#1e8449;">**[note] Note（译者注）——标题：$\varepsilon$-$\delta$ 定义的第一性原理拆解**</span>
> 
> Definition 5.32 值得用第一性原理拆解：「对每个 $\varepsilon > 0$ 都存在 $\delta > 0$，使得对所有满足 $|x - x_0| < \delta$ 的 $x \in A$，都有 $|f(x) - f(x_0)| < \varepsilon$。」这里的每一个量词都在做一件具体的事：
> (1)「对于任意给定的误差容限 $\varepsilon$」——这是对手（adversary）的移动，它可以选择任意小的 $\varepsilon$ 来挑战你；
> (2)「存在 $\delta > 0$」——这是你的回应，你需要找到一个足够小的窗口半径；
> (3)「只要 $x \in A$ 且 $|x - x_0| < \delta$」——你只控制 $x$ 的输入偏差，不能控制 $x$ 是什么；
> (4)「$|f(x) - f(x_0)| < \varepsilon$」——输出偏差就自动被控制住了。
> 这个「对手—回应」博弈结构正是 Weierstrass（~1872）将 Cauchy 的「无限趋近」语言彻底形式化为 $\varepsilon$-$\delta$ 语言的精髓。在计算机科学中，这对应着「对任意输入（$\forall \varepsilon$），存在算法（$\exists \delta$）」的规范——编写正确性证明时的前置条件与后置条件正是这种量词结构的编程版本。

---

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">5.4.4 Continuity on a Set（集合上的连续性）</span>

> <span style="color:#7f8c8d;">TBB §5.4.4, p.215</span>

enrichment section（本节为拓展内容），可以略过不读。

continuity（连续性）是在点上定义的。像 $f(x) = x^2$ 这样的函数可以说在每一个实数 $x_0$ 处都连续，这仅仅意味着对每个实数都有 $\lim_{x \to x_0} x^2 = x_0^2$。在许多情形下，所考虑的函数在其 domain（定义域）的每一点都是连续的。这时我们就简单地说 $f$ 是 continuous（连续的）。但我们必须记住，这是关于 $f$ 有定义处的每一个点的 assertion（断言）。

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">Definition 5.36（定义 5.36）</span>

> <span style="color:#7f8c8d;">TBB §5.4.4, p.215</span>

设 $f: A \to \mathbb{R}$。如果 $f$ 在 $A$ 的每一点都连续，则称 $f$ 是连续的，或者说 $f$ 在 $A$ 上连续（continuous on $A$）。

如果我们想直接依据这个定义来证明 $f$ 是连续的，就必须证明 $f$ 在每一个 $x_0 \in A$ 处都连续。有时，改用下面给出的global characterization（连续性的整体刻画）会更加容易。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 5.37（定理 5.37）</span>

> <span style="color:#7f8c8d;">TBB §5.4.4, p.215</span>

设 $f: A \to \mathbb{R}$。则 $f$ 是连续的，当且仅当对每一个 open set（开集）$V \subset \mathbb{R}$，集合 $f^{-1}(V) = \{x \in A : f(x) \in V\}$ 都是（相对于 $A$ 的）开集。

<span style="color:#2471a3;">**[proof]**</span> **Proof（证明）：**

> 首先设 $f$ 是连续的。设 $V$ 是开集，取 $x_0 \in f^{-1}(V)$，并选取 $\alpha < \beta$ 使得 $(\alpha, \beta) \subset V$，且 $x_0 \in f^{-1}((\alpha, \beta))$。于是 $\alpha < f(x_0) < \beta$。我们将找到 $x_0$ 的一个 neighborhood（邻域）$U$，使得对所有 $x \in U \cap A$ 都有 $\alpha < f(x) < \beta$。令 $\varepsilon = \min(\beta - f(x_0), f(x_0) - \alpha)$。由于 $f$ 在 $x_0$ 处连续，存在 $\delta > 0$，使得若 $x \in A \cap (x_0 - \delta, x_0 + \delta)$，则 $|f(x) - f(x_0)| < \varepsilon$。于是 $f(x) - f(x_0) < \beta - f(x_0)$，从而 $f(x) < \beta$。类似地，$f(x) - f(x_0) > \alpha - f(x_0)$，从而 $f(x) > \alpha$。因此，relative neighborhood（相对邻域）$U = (x_0 - \delta, x_0 + \delta) \cap A$ 是 $f^{-1}((\alpha, \beta))$ 的子集，从而是 $f^{-1}(V)$ 的子集。我们已证明 $f^{-1}(V)$ 中的每个成员在 $f^{-1}(V)$ 内都有一个相对邻域。也就是说，$f^{-1}(V)$ 相对于 $A$ 是开集。
> 
> 为证明逆命题，设 $f$ 满足如下条件：对每个满足 $\alpha < \beta$ 的 open interval（开区间）$(\alpha, \beta)$，集合 $f^{-1}((\alpha, \beta))$ 都相对于 $A$ 是开集。取 $x_0 \in A$，我们必须证明 $f$ 在 $x_0$ 处连续。

> <span style="color:#7f8c8d;">接上页 p.215：定理 5.37 的证明（续）。</span>

<span style="color:#2471a3;">**[proof]**</span> **Proof（证明，续）：**

> 设 $\varepsilon > 0$，令 $\beta = f(x_0) + \varepsilon$，$\alpha = f(x_0) - \varepsilon$。我们的假设蕴含 $f^{-1}((\alpha, \beta))$ 相对于 $A$ 是开集。因此
> 
> ```math
> f^{-1}((\alpha, \beta)) = \bigcup_{i} (a_i, b_i) \cap A,
> ```
> 
> 其中的并是pairwise disjoint open intervals（两两不相交开区间）的一个有限并或可数并。这些区间中有一个，设为 $(a_j, b_j)$，包含 $x_0$。令 $\delta = \min(x_0 - a_j, b_j - x_0)$。对满足 $|x - x_0| < \delta$ 且 $x \in A$ 的 $x$，我们得到 $\alpha < f(x) < \beta$。由于 $\beta = f(x_0) + \varepsilon$ 且 $\alpha = f(x_0) - \varepsilon$，必有 $|f(x) - f(x_0)| < \varepsilon$。这表明 $f$ 在 $x_0$ 处连续。$\square$

我们把定理 5.37 证明的细节完整地写了出来。这可能使它显得相当冗长。但这个证明无非是把一些直观图形所提示的内容以严格的方式写下来而已。你可能会发现，用连续性的 neighborhood notion（邻域观点）来证明这个定理更为自然。我们把这个留作习题 5.4.23。

作为推论，我们指出：可以把开集替换为开区间；因此，要检验函数 $f$ 的连续性，只需证明对每一个区间 $(\alpha, \beta)$，集合 $f^{-1}((\alpha, \beta))$ 都是开集。

### <span style="color:#2471a3;">**[corollary]**</span> <span style="color:#c0392b">Corollary 5.38（推论 5.38）</span>

> <span style="color:#7f8c8d;">TBB §5.4.4, p.216</span>

设 $f: A \to \mathbb{R}$。则 $f$ 是连续的，当且仅当对每一个区间 $(\alpha, \beta)$，$f^{-1}((\alpha, \beta))$ 都是（相对于 $A$ 的）开集。

<span style="color:#2471a3;">**[proof]**</span> **Proof（证明）：**

> 我们验证如下两个条件是等价的：（i）对所有开集 $V \subset \mathbb{R}$，$f^{-1}(V)$ 是 relatively open（相对开集）；（ii）对所有 $\alpha < \beta$，$f^{-1}((\alpha, \beta))$ 是相对开集。但这是显而易见的。若条件 (i) 满足，则条件 (ii) 也满足，因为条件 (ii) 只是条件 (i) 的一个特例。另一方面，若条件 (ii) 满足，且
> 
> ```math
> V = \bigcup (\alpha_i, \beta_i),
> ```
> 
> 则
> 
> ```math
> f^{-1}(V) = \bigcup f^{-1}((\alpha_i, \beta_i)).
> ```
> 
> 由假设，集合 $f^{-1}((\alpha_i, \beta_i))$ 中的每一个都是开集，所以 $f^{-1}(V)$ 也是开集，因为它是开集族的并。$\square$

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 5.39（例 5.39）</span>

> <span style="color:#7f8c8d;">TBB §5.4.4, p.216</span>

设 $f(x) = 1/x$（$x > 0$）。我们求得

```math
f^{-1}((\alpha, \beta)) = \left(\frac{1}{\beta}, \frac{1}{\alpha}\right).
```

由于 $(1/\beta, 1/\alpha)$ 是开集，可推出 $f$ 在 $(0, \infty)$ 上连续。$\blacksquare$

---

---

> <span style="color:#1e8449;">**[note] Note（译者注）——标题：开集原像刻画——点态定义如何升格为整体语言**</span>
> 
> Theorem 5.37 断言：$f: A \to \mathbb{R}$ 连续当且仅当每个开集 $V$ 的原像 $f^{-1}(V)$ 相对于 $A$ 是开集。这是一个华丽的「视角翻转」：我们不再逐点地检查每个 $x_0$ 的连续性，而是用**开集的行为**一次性刻画整个函数的连续性。理解这个定理不需要你先学拓扑——你可以把它视为一种「调试工具」：要验证 $f(x) = 1/x$ 在 $(0, \infty)$ 上连续，只需对任意开区间 $(\alpha, \beta)$ 计算 $f^{-1}((\alpha, \beta)) = (1/\beta, 1/\alpha)$（Example 5.39），而 $(1/\beta, 1/\alpha)$ 显然是开集——一次计算覆盖所有点。这个刻画是点集拓扑的种子：在更一般的拓扑空间中，**连续性的定义本身就是「开集的原像是开集」**，而实分析中的 $\varepsilon$-$\delta$ 不过是这个一般定义在度量空间中的具体展开。你在 18.065 中学到的矩阵范数连续性本质上也是这个模式的特例。

---

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">5.5 Properties of Continuous Functions（连续函数的性质）</span>

> <span style="color:#7f8c8d;">TBB §5.5, p.218</span>

我们现在介绍 continuous functions（连续函数）最基本的一些性质。第一个定理是代数性质的；它断言定义在一个集合上的连续函数族具有 algebra（代数）的许多性质：其中的元素可以相加、相减、相乘，并且在某些条件下可以相除。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 5.40（定理 5.40）</span>

> <span style="color:#7f8c8d;">TBB §5.5, p.218</span>

设 $f, g: A \to \mathbb{R}$，并设 $c \in \mathbb{R}$。假设 $f$ 与 $g$ 在点 $x_0 \in A$ 处连续。则 $cf$、$f+g$ 与 $fg$ 在 $x_0$ 处连续。进一步地，若 $g(x_0) \neq 0$，则 $\frac{f}{g}$ 在 $x_0$ 处连续。

<span style="color:#2471a3;">**[proof]**</span> **Proof（证明）：**

> 这些结论直接由 continuity（连续性）的 limit definition（极限定义）以及 limits（极限）的通常代数性质得出。

$\square$

### <span style="color:#2471a3;">**[corollary]**</span> <span style="color:#c0392b">Corollary 5.41（推论 5.41）</span>

> <span style="color:#7f8c8d;">TBB §5.5, p.218</span>

每个 polynomial（多项式）在 $\mathbb{R}$ 上连续。

<span style="color:#2471a3;">**[proof]**</span> **Proof（证明）：**

> 函数 $f(x) = 1$ 与 $g(x) = x$ 在 $\mathbb{R}$ 上连续。该推论由 Theorem 5.40 得出。

$\square$

### <span style="color:#2471a3;">**[corollary]**</span> <span style="color:#c0392b">Corollary 5.42（推论 5.42）</span>

> <span style="color:#7f8c8d;">TBB §5.5, p.218</span>

每个 rational function（有理函数）在其 domain（定义域）的每一点处都连续（即，在分母不为零的每个 $x \in \mathbb{R}$ 处都连续）。

我们最重要的性质之一是它允许我们把两个连续函数 compose（复合）起来。不过要当心定义域上的条件，因为它们不容忽视。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 5.43（定理 5.43）</span>

> <span style="color:#7f8c8d;">TBB §5.5, p.218</span>

设 $f: A \to \mathbb{R}$，$g: B \to \mathbb{R}$，并假设 $f(A) \subset B$。假设 $f$ 在点 $x_0 \in A$ 处连续，且 $g$ 在点 $y_0 = f(x_0) \in B$ 处连续。则 composite function（复合函数）

```math
g \circ f : A \to \mathbb{R}
```

在 $x_0$ 处连续。

<span style="color:#2471a3;">**[proof]**</span> **Proof（证明）：**

> 这由 Theorem 5.25 得出。

$\square$

一个 global（整体）版本作为推论随之给出。

### <span style="color:#2471a3;">**[corollary]**</span> <span style="color:#c0392b">Corollary 5.44（推论 5.44）</span>

> <span style="color:#7f8c8d;">TBB §5.5, p.218</span>

设 $f: A \to \mathbb{R}$，$g: B \to \mathbb{R}$，并假设 $f(A) \subset B$。若 $f$ 在 $A$ 上连续且 $g$ 在 $B$ 上连续，则复合函数 $g \circ f: A \to \mathbb{R}$ 在 $A$ 上连续。

---

---

> <span style="color:#1e8449;">**[note] Note（译者注）——标题：连续函数构成一个代数——为什么这很重要**</span>
> 
> Theorem 5.40 看似只是「和、差、积、商保持连续性」四条平凡结论，但它揭示了一个深层结构：定义在集合 $A$ 上的全体连续函数 $C(A) = \{f: A \to \mathbb{R} \mid f \text{ 连续}\}$ 构成一个 $\mathbb{R}$-代数（更准确地说是一个交换环上的模）。这意味着你可以像操作数一样操作函数——把两个连续函数相加得到的还是连续函数，乘以标量亦然，两个连续函数的乘积仍是连续函数。这不是空洞的赞美：正因为 $C(A)$ 是一个代数，从两个「种子」函数 $f(x) = 1$ 和 $g(x) = x$（两者显然连续）出发，通过有限次加法、乘法、数乘，就能生成全体多项式函数（Corollary 5.41），进而生成全体有理函数（Corollary 5.42）。这与你在线性代数（📖 Strang §3.1）中见过的「向量空间的基+线性组合生成全体向量」是同一套逻辑——只不过这里的运算是逐点加法与乘法，而生成的对象是函数而非向量。在算法正确性证明中，这种代数封闭性同样关键：复杂程序的正确性可以通过组合基本正确性引理来推导（📖 6.042J §4.4）。

---

---

> <span style="color:#1e8449;">**[note] Note（译者注）——标题：「$\varepsilon$ 传递法」——复合连续性证明的策略模板**</span>
> 
> Theorem 5.43 的证明（在 TBB 中引用 Theorem 5.25 一笔带过，但教授在课堂上有详细展开）揭示了一个可重用的证明策略——我称之为「$\varepsilon$ 传递法」：要证明 $h = g \circ f$ 在 $x_0$ 连续，给定任意 $\varepsilon > 0$：
> (1) 从外层 $g$ 的连续性入手——存在 $\delta_g > 0$ 使得只要 $|y - y_0| < \delta_g$（其中 $y_0 = f(x_0)$），就有 $|g(y) - g(y_0)| < \varepsilon$；
> (2) 把 $\delta_g$ 当作内层 $f$ 的「$\varepsilon$」——由 $f$ 的连续性，存在 $\delta_f > 0$ 使得只要 $|x - x_0| < \delta_f$，就有 $|f(x) - f(x_0)| < \delta_g$；
> (3) 链式代入：若 $|x - x_0| < \delta_f$，则 $|f(x) - y_0| < \delta_g$，进而 $|g(f(x)) - g(y_0)| < \varepsilon$。
> 🎥 *教授*："Given epsilon, you sort of start backwards... from delta g and the continuity of f, there exists delta of f."（翻译：给定 epsilon，你从后往前推……从 delta_g 和 f 的连续性，就存在 delta_f。）这个「把上一个 $\delta$ 当下一个 $\varepsilon$」的技术在后续证明中反复出现，包括一致连续性和链式法则的证明。本质上，它和你编写递归函数时的「外层调用的前置条件即为内层调用的后置条件」是同一思路。

---

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">5.6 Uniform Continuity（一致连续性）</span>

> <span style="color:#7f8c8d;">TBB §5.6, p.219–220 —— 起自 §5.6 开篇正文，止于定理 5.49</span>

<span style="color:#2471a3;">**[paragraph]**</span> 让我们更仔细地审视一下函数 $f$ 在区间 $I$ 上 continuous（连续）的确切含义。

<span style="color:#2471a3;">**[paragraph]**</span> 连续性定义断言:对每个 $x_0 \in I$ 与每个 $\varepsilon > 0$,都存在 $\delta > 0$,使得只要 $x \in I$ 且 $|x - x_0| < \delta$,就有 $|f(x) - f(x_0)| < \varepsilon$。

<span style="color:#2471a3;">**[paragraph]**</span> 现在请仔细考虑下面这个陈述:对每个 $\varepsilon > 0$,都存在 $\delta > 0$,使得只要 $x, x_0 \in I$ 且 $|x - x_0| < \delta$,就有 $|f(x) - f(x_0)| < \varepsilon$。

<span style="color:#2471a3;">**[paragraph]**</span> 乍看之下,这个陈述似乎只是对第一段所表述的连续性含义的重新陈述。如果你察觉不出这两者的差别,那你并不孤单:Cauchy（柯西）当年也没有看出任何差别,并且错误地运用了刚刚引述的这一性质,企图证明区间 $[a, b]$ 上的连续函数必定 integrable（可积）。

<span style="color:#2471a3;">**[paragraph]**</span> 我们需要把注意力集中在这样一个事实上:数 $\delta$ 不仅依赖于 $f$ 和 $\varepsilon$,也依赖于 $x_0$;也就是说,$\delta = \delta(f, \varepsilon, x_0)$。

---

---

> <span style="color:#1e8449;">**[note] Note（译者注）——柯西的"一致性盲区"：一个持续半世纪的混淆：**</span>
> 教材此处指出柯西未能区分连续与一致连续，这绝非苛责——1821 年 Cauchy 在 *Cours d'Analyse* 中陈述的"连续函数必可积"定理，其证明暗中假设了我们现在所说的一致连续性（uniform continuity），而他本人从未意识到这一额外假设。直到 1870 年 Heine 才首次明确区分两者，1872 年 Heine 又证明了闭区间上连续⟹一致连续（即 Theorem 5.48），由此才真正挽救了柯西的积分理论。因此，当你读到 §5.6 那段「柯西无疑认识到了这一事实，却没有把连续性与一致连续性区分开来」时不妨体会：一个概念从模糊到清晰，整整花了五十年。🎥 教授在 V09 中提到："It's called uniform continuity. Uniform continuity has some nice extra properties."（翻译：这称为一致连续性。一致连续性具有一些很好的额外性质。）这里"额外"二字正是指出了 $\delta$ 与 $x_0$ 解耦所带来的力量。

---

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 5.45（例 5.45）</span>

> <span style="color:#7f8c8d;">TBB §5.6, p.219</span>

<span style="color:#2471a3;">**[paragraph]**</span> 考虑定义在区间 $I = (0, 1)$ 上的函数 $f(x) = 1/x$。我们在习题 5.4.10 中看到:如果取 $\varepsilon = 1$,我们可以选择

```math
\delta(f, 1, x_0) = \frac{x_0^2}{1 + x_0},
```

但不能选择更大的值。因此当 $x_0 \to 0$ 时,有 $\delta(f, 1, x_0) \to 0$。没有任何一个数 $\delta$ 会小到足以对所有 $x_0 \in I$ 同时"管用"。

---

<span style="color:#2471a3;">**[paragraph]**</span> 往往有这样的需要:能够选取一个与 $x_0$ 无关的 $\delta$。当这种选取成为可能时,我们就称 $f$ 在 $I$ 上 uniformly continuous（一致连续）。

### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#c0392b">Definition 5.46（定义 5.46）</span>

> <span style="color:#7f8c8d;">TBB §5.6, p.219</span>

<span style="color:#00838f">（一致连续）设 $f$ 定义在集合 $A \subset \mathbb{R}$ 上。我们说 $f$ 在 $A$ 上一致连续:若对每个 $\varepsilon > 0$,都存在 $\delta > 0$,使得只要 $x, y \in A$ 且 $|x - y| < \delta$,就有 $|f(x) - f(y)| < \varepsilon$。</span>

<span style="color:#2471a3;">**[paragraph]**</span> 为了说明 uniform continuity（一致连续性）的用处,我们指出:如果 $f$ 在 bounded interval（有界区间）$I$ 上一致连续,那么 $f$ 在 $I$ 上有 bounded（界）。

---

> <span style="color:#1e8449;">**[note] Note（译者注）——量词顺序：一个逻辑训练的最佳案例：**</span>
> 连续与一致连续的差异可以纯粹地从谓词逻辑的"量词换序"来理解。逐点连续：$\forall x_0\, \forall \varepsilon\, \exists \delta\, \forall x$（$\delta$ 在 $\exists$ 之后，可依赖 $x_0$）。一致连续：$\forall \varepsilon\, \exists \delta\, \forall x_0\, \forall x$（$\delta$ 在 $\forall x_0$ 之前，不可依赖 $x_0$）。用 6.042J 中对偶公式的语言来说，这正是 ∃∀ 与 ∀∃ 的区别——前者强得多。一个具象化的类比：逐点连续好比「每个学生都能找到一本适合自己水平的书」；一致连续则要求「存在一本书，所有学生都适合」。在 Example 5.45 的 $f(x)=1/x$ 中，当 $x_0 \to 0^+$ 时 $\delta$ 被迫趋近于 0，这正是「$\forall x_0$ 在前」与「$\exists \delta$ 在前」的冲突在几何上的体现。

---

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 5.47（定理 5.47）</span>

> <span style="color:#7f8c8d;">TBB §5.6, p.219</span>

如果函数 $f$ 在有界区间 $I$ 上一致连续,那么 $f$ 在 $I$ 上有界。

<span style="color:#2471a3;">**[proof]**</span> **Proof（证明）:**

> 这里我们假定 $I$ 是 $(a, b)$、$[a, b]$、$[a, b)$ 或 $(a, b]$ 中的一种。为了检验 $f$ 有界,选取 $\delta$,使得只要 $x, y \in I$ 且 $|x - y| < \delta$,就有 $|f(x) - f(y)| < 1$。存在一个有限点列 $a = x_0 < x_1 < \cdots < x_n = b$,满足对每个 $i = 1, \ldots, n$ 都有 $|x_i - x_{i-1}| < \delta$。我们对 $\delta$ 的选取意味着 $f$ 在每一个区间 $[x_{i-1}, x_i] \cap I$ 上有界。令
> 
> ```math
> \begin{aligned}
m_i &= \inf\{ f(x) : x_{i-1} \leq x \leq x_i,\ x \in I \},\\
M_i &= \sup\{ f(x) : x_{i-1} \leq x \leq x_i,\ x \in I \},\\
m &= \min\{ m_1, \ldots, m_n \},\\
M &= \max\{ M_1, \ldots, M_n \}.
\end{aligned}
> ```

---

> <span style="color:#7f8c8d;">书页 p.220</span>

> 于是,对每个 $x \in I$,都有 $m \leq f(x) \leq M$,所以 $f$ 在 $I$ 上有界。$\square$

<span style="color:#2471a3;">**[paragraph]**</span> 请注意,如果我们试图对区间 $I = (0, 1)$ 上的函数 $f(x) = 1/x$ 给出一个类似的论证,那么 $f$ 的连续性只能让我们断定:每个 $x \in I$ 都落在某个 $f$ 于其上有界的区间之中,但是我们无法得到有限多个这样的区间来 cover（覆盖）$I$。

<span style="color:#2471a3;">**[paragraph]**</span> 在我们"在 $I$ 上一致连续蕴含 $I$ 上有界"的说明中,我们并没有指明 $I$ 是否包含它的一个或多个端点。我们接下来的目标是证明:当 $I = [a, b]$ 是 closed interval（闭区间）时,$I$ 上每个连续的函数 $f$ 都在 $I$ 上一致连续。(另请注意习题 5.6.14 中给出的更一般的版本。)

<span style="color:#2471a3;">**[paragraph]**</span> 这一结果在许多地方都很重要。特别是,我们日后将要证明的那个重要结果——$[a, b]$ 上的连续函数 $f$ 可积——正是依赖于 $f$ 的一致连续性。柯西无疑认识到了这一事实,却没有把连续性与一致连续性区分开来。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 5.48（定理 5.48）</span>

> <span style="color:#7f8c8d;">TBB §5.6, p.220</span>

设 $f$ 在 $[a, b]$ 上连续。则 $f$ 一致连续。

<span style="color:#2471a3;">**[proof]**</span> **Proof（证明）:**

> 我们的证明运用了一个 compactness（紧致性）论证。回顾我们在 4.5 节对紧致性的研究,那里给出了好几种彼此等价的表述。我们将采用 Bolzano-Weierstrass property（波尔查诺-魏尔斯特拉斯性质）。(习题 5.6.2 要求用库赞引理（Cousin's lemma）给出这同一个定理的另一种证明;习题 5.6.13 则要求你用 Heine-Borel property（海涅-博雷尔性质）来证明它。)
> 
> 我们使用 indirect proof（反证法）。如果 $f$ 不一致连续,那么就存在序列 $\{x_n\}$ 与 $\{y_n\}$,使得 $x_n - y_n \to 0$,但对某个正数 $c$,恒有 $|f(x_n) - f(y_n)| > c$。(这一步骤的验证留给习题 5.6.12。)
> 
> 现在应用波尔查诺-魏尔斯特拉斯性质,得到一个 convergent subsequence（收敛子列）$\{x_{n_k}\}$。把这个新序列 $\{x_{n_k}\}$ 的极限记为 $z$。注意到,由于 $x_n - y_n \to 0$,所以 $x_{n_k} - y_{n_k} \to 0$。于是 $\{x_{n_k}\}$ 与序列 $\{y_n\}$ 的对应子列 $\{y_{n_k}\}$ 收敛于同一个极限 $z$,而 $z$ 必定是区间 $[a, b]$ 中的点。由 $f$ 的连续性,$f(x_{n_k}) \to f(z)$,且 $f(y_{n_k}) \to f(z)$。由于对所有 $n$ 都有 $|f(x_n) - f(y_n)| > c$,于是根据我们关于序列极限的研究,这意味着
> 
> ```math
> |f(z) - f(z)| \geq c > 0
> ```
> 
> 而这不可能。这一矛盾证明了定理。$\square$

<span style="color:#2471a3;">**[paragraph]**</span> 作为定理 5.48 的一个应用,我们现在可以证明:任何在闭有界区间 $[a, b]$ 上连续的函数都有界。事实上,这样的函数在那里必定是一致连续的,而我们已经在定理 5.47 中看到:在有界区间上一致连续的函数是有界的。于是我们得到下面这个有用的定理。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Boundedness of Continuous Functions（连续函数的有界性）</span>

> <span style="color:#7f8c8d;">TBB §5.6, p.220</span>

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 5.49（定理 5.49）</span>

> <span style="color:#7f8c8d;">TBB §5.6, p.220</span>

设 $f$ 在 $[a, b]$ 上连续。则 $f$ 有界。

---

---

> <span style="color:#1e8449;">**[note] Note（译者注）——证明策略模板：「紧致性论证（Bolzano-Weierstrass 反证法）」：**</span>
> Theorem 5.48 的证明是实分析中最重要的一种论证模式之一，值得提取为模板。（1）假设结论不成立（不一致连续），将其否定写成序列形式：∃{xₙ}, {yₙ} s.t. |xₙ−yₙ|→0 但 |f(xₙ)−f(yₙ)|>c>0。（2）运用 Bolzano-Weierstrass 性质（§4.5 紧致性的等价形式之一）从 {xₙ} 中抽出收敛子列 {x_{nₖ}}→z。（3）由 |xₙ−yₙ|→0 推出对应子列 {y_{nₖ}} 也收敛到 z。（4）连续性的序列刻画给出 f(x_{nₖ})→f(z) 且 f(y_{nₖ})→f(z)。（5）由序列不等式取极限得 |f(z)−f(z)|≥c>0，矛盾。这一模板——从否定出发构造序列、用紧致性提取收敛子列、再让两边"夹逼"到同一极限点——在后续定理（5.50, 5.53）中反复出现。📖 对比习题 5.6.2（用 Cousin 引理）和 5.6.13（用 Heine-Borel）的替代证明，体会三种紧致性表述各自的证明风格。

---

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">5.7 Extremal Properties（极值性质）</span>

> <span style="color:#7f8c8d;">TBB §5.7, p.222</span>

我们在 elementary calculus（初等微积分）中研究的一类熟悉问题，涉及在区间 $[a, b]$ 上寻找 continuous function（连续函数）的 extrema（极值）。

其技巧在于检查函数在下列各点的取值：导数为零的点、endpoints（区间的端点）、以及任何 nondifferentiability（不可微）的点。

要使这样的过程可行，我们必须确信函数在该区间上确有 maximum（最大值）（或 minimum（最小值））。

我们现在就来验证这一点。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 5.50（定理 5.50）</span>

> <span style="color:#7f8c8d;">TBB §5.7, p.222</span>

设 $f$ 在 $[a, b]$ 上连续。

则 $f$ 既存在 absolute maximum（绝对最大值），也存在 absolute minimum（绝对最小值）。

<span style="color:#2471a3;">**[proof]**</span> **Proof（证明）：**

> 设 $M = \sup\{ f(x) : a \le x \le b\}$。
> 
> 由定理 5.48，$f$ 在 $[a, b]$ 上 uniformly continuous（一致连续）。
> 
> 因此，由定理 5.49，$M < \infty$。
> 
> 如果存在 $x_0$ 使得 $f(x_0) = M$，那么 $f$ 就达到了最大值 $M$。
> 
> 现在假设对所有 $x \in [a, b]$ 都有 $f(x) < M$，我们证明这是不可能的。
> 
> 令 $g(x) = 1/(M - f(x))$。
> 
> 对每个 $x \in [a, b]$，都有 $f(x) \ne M$；因此 $g$ 连续，并且对所有 $x \in [a, b]$ 有 $g(x) > 0$。
> 
> 从 $M$ 的定义可以看出：
> 
> ```math
> \inf\{ M - f(x) : x \in [a, b] \} = 0,
> ```
> 
> 所以
> 
> ```math
> \sup\left\{ \frac{1}{M - f(x)} : x \in [a, b] \right\} = \infty.
> ```
> 
> 这意味着 $g$ 在 $[a, b]$ 上 unbounded（无界）。
> 
> 这是不可能的，因为正如我们在第 5.6 节所见，定义在 closed interval（闭区间）上的连续函数必有 bounded（界）。
> 
> 类似的证明可以说明 $f$ 在 $A$ 上存在绝对最小值。

$\square$

> <span style="color:#1e8449;">**译者注：** 原文此句写作「on $A$」，依上下文应为「on $[a, b]$」，即「在 $[a, b]$ 上」，当属笔误。</span>

---

---

> <span style="color:#1e8449;">**[note] Note（译者注）——极值定理：为什么 sup 必须被"达到"：**</span>
> 极值定理（Extreme Value Theorem）的证明有一个精妙的迂回：不直接构造最大值点，而是先由 Theorem 5.48/5.49 知道 M=sup f<∞，再假设 f 永远达不到 M，构造 g(x)=1/(M−f(x))。一旦假设 M 达不到，分母恒正，g 在 [a,b] 上连续——但由 M 的定义，g 又必须无界，这与 Theorem 5.49（闭区间上连续函数有界）矛盾。这个「假设达不到→构造倒数→导出无界矛盾」的技巧是分析学中一种以退为进的常用套路。🎥 教授在 V11 中用序列途径证明了同一结论："I'm going to prove that the image...is bounded...f of xM is equal to this."（翻译：我将证明像集有界……f(xM) 等于这个值。）两种证明途迳（序列 vs 确界）恰好对应了构建主义者的直觉：「用序列逼近极值点」vs「从上确界的定义中读出存在性」。📖 定理可推广到紧集（Theorem 5.52），这正是下一章度量空间中讨论的一般框架。

---

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 5.51（例 5.51）</span>

> <span style="color:#7f8c8d;">TBB §5.7, p.223</span>

这个定理能否推广到 more general situations（更一般的情形）？如果把区间 $[a,b]$ 换成某个其他集合，conclusion（结论）是否仍然成立？例如，函数

```math
f(x) = \frac{1}{x} \quad \text{for } x \in (0,1)
```

表明，闭区间不能换成开区间。另一方面，函数

```math
f(x) = x \quad \text{for } x \in [0,\infty)
```

则表明，有界闭区间 $[a,b]$ 不能换成无界闭区间。$\blacksquare$

从这个例子出发，一个想法似乎自然而然地浮现出来：我们需要一个闭且有界的集合，也就是一个 compact set（紧集）。事实上，这正是定理 5.50 的正确 generalization（推广）。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 5.52（定理 5.52）</span>

> <span style="color:#7f8c8d;">TBB §5.7, p.223</span>

设 $f$ 在 closed and bounded（闭且有界）的集合 $A$ 上连续。则 $f$ 在 $A$ 上必取得 absolute maximum（绝对最大值）和 absolute minimum（绝对最小值）。

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">5.8 Darboux Property（达布性质）</span>

> <span style="color:#7f8c8d;">TBB §5.8, p.223–224</span>

我们此前已经观察到，IVP（介值性质）即 Darboux property（达布性质），它与连续性并不是同一回事。不过，如下事实成立：若 $f$ 在 $[a,b]$ 上连续，则 $f$ 具有达布性质。我们以一种便于使用库赞引理（Cousin's lemma）的形式来陈述定理 5.53。（偏好使用 Bolzano-Weierstrass theorem（波尔查诺-魏尔斯特拉斯定理）的读者，可参阅习题 5.8.3 的提示。）

以这种形式表述，定理断言：如果 graph（图像）在某条水平线 $y = c$ 上没有交点，那么图像必完全位于该线的上方或下方。换一种说法（见习题 5.8.8），即函数必须取到其任意两个值之间的每一个值。

---

> <span style="color:#1e8449;">**[note] Note（译者注）——达布性质：比连续更"宽容"的介值条件：**</span>
> 达布性质（Darboux property）得名于法国数学家 Jean-Gaston Darboux（1875 年定理）：任何导函数都具有介值性质，即使该导函数本身并不连续。这意味着 IVP（Intermediate Value Property）是比连续性更弱的条件——连续函数一定满足 IVP（Theorem 5.53），但满足 IVP 的函数不一定连续。教材以"图像若与水平线 y=c 无交点，则必完全位于该线一侧"的等价形式来陈述定理——这种表述在逻辑上比「取到一切中间值」更容易直接证明（只需在每点用连续性局部判断符号，再由 Cousin 引理拼接全局）。📖 习题 5.8.8 则将这种"无交点即完全一侧"重新翻译回熟悉的 IVP 形式，值得对比阅读。🎥 教授在 V11 中介绍 IVT 时简洁地说："All values between f of a and f of b are achieved."（翻译：f(a) 与 f(b) 之间的所有值均被取到。）

---

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 5.53（定理 5.53）</span>

> <span style="color:#7f8c8d;">TBB §5.8, p.224</span>

设 $f$ 在 $[a,b]$ 上连续，并设 $c \in \mathbb{R}$。若对一切 $x \in [a,b]$ 都有 $f(x) \neq c$，则要么对所有 $x \in [a,b]$ 有 $f(x) > c$，要么对所有 $x \in [a,b]$ 有 $f(x) < c$。

<span style="color:#2471a3;">**[proof]**</span> **Proof（证明）:**

> 与定理 5.48 的证明一样，我们再次使用 compactness argument（紧致性论证）。我们将采用库赞引理（Cousin's lemma，引理 4.26）。习题中要求你分别用 Bolzano-Weierstrass property（波尔查诺-魏尔斯特拉斯性质）和 Heine-Borel property（海涅-博雷尔性质）来证明这同一个定理。
> 
> 设 $\mathcal{C}$ 表示满足下述条件的闭区间 $J$ 的全体：对一切 $x \in J$ 有 $f(x) < c$，或对一切 $x \in J$ 有 $f(x) > c$。我们来验证 $\mathcal{C}$ 构成 $[a,b]$ 的一个 Cousin cover（库赞覆盖）。
> 
> 若 $x \in [a,b]$，则 $|f(x) - c| = \varepsilon > 0$，故存在 $\delta > 0$，使得当 $|t - x| < \delta$ 且 $t \in [a,b]$ 时，$|f(t) - f(x)| < \varepsilon$。因此，若 $f(x) < c$，则对所有 $t \in [x - \delta/2,\, x + \delta/2]$ 有 $f(t) < c$；而若 $f(x) > c$，则对所有 $t \in [x - \delta/2,\, x + \delta/2]$ 有 $f(t) > c$。由库赞引理知，存在 $[a,b]$ 的一个 partition（划分）$a = x_0 < x_1 < \cdots < x_n = b$，使得对 $i = 1, \ldots, n$ 有 $[x_{i-1}, x_i] \in \mathcal{C}$。
> 
> 现在设 $f(a) < c$（若 $f(a) > c$，论证类似）。由于 $[a, x_1] = [x_0, x_1] \in \mathcal{C}$，故对所有 $x \in [x_0, x_1]$ 有 $f(x) < c$。类似地，因为 $[x_1, x_2] \in \mathcal{C}$ 且 $f(x_1) < c$，所以对 $x \in [x_1, x_2]$ 有 $f(x) < c$。如此继续下去，我们看到对所有 $x \in [a,b]$ 都有 $f(x) < c$。$\square$

你也许愿意查看习题 5.8.8，那里给出了这个定理的其他表述，它们将 IVP 类比为"connectedness（连通性）"。

---

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">5.9 Points of Discontinuity（不连续点）</span>

> <span style="color:#7f8c8d;">TBB §5.9, p.225</span>

在我们对 continuous functions（连续函数）的讨论中，我们仅仅把 discontinuity（不连续）当作 continuity（连续性）概念的反面才提到它。在数学的许多应用中，出现的函数往往带有不连续点，因此研究这类函数是值得的。我们首先要建立一套关于不连续点的语言。然后我们研究一类重要的函数——monotonic functions（单调函数）——并确定它们的不连续性能坏到何种程度。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">5.9.1 Types of Discontinuity（不连续的类型）</span>

> <span style="color:#7f8c8d;">TBB §5.9.1, p.225</span>

设 $x_0$ 是某个函数 $f$ 的 domain（定义域）中的一点。若 $x_0$ 是一个 point of discontinuity（不连续点），那么这意味着：或者极限 $\lim_{x \to x_0} f(x)$ 不存在，或者该极限存在但 $f(x_0) \ne \lim_{x \to x_0} f(x)$。

<span style="color:#2471a3;">**[note]**</span> **Note（原文注意）：** 当我们讨论不连续点时，我们讨论的只是函数在其中已有定义的那些点。（某些微积分教材可能会把 $x_0$ 称为不连续点，即使 $f(x_0)$ 并未定义。这不是我们这里的用法。）

还要注意，不连续点不可能出现在函数定义域的 isolated point（孤立点）处。

<span style="color:#c0392b">**Removable Discontinuities（可去不连续）**</span>

我们可以把这些情形按严重程度递增来区分。最弱的一种可能是：$\lim_{x \to x_0} f(x)$ 确实存在，但没有等于 $f(x_0)$。我们称此为 $f$ 的 removable discontinuity（可去不连续）。"removable"（可去）一词暗示：只要我们给 $f(x_0)$ 赋予一个新值，就不会再有不连续了。

<span style="color:#c0392b">**Jump Discontinuities（跳跃不连续）**</span>

一个稍微严重些的不连续情形是：极限 $\lim_{x \to x_0} f(x)$ 不存在，但它之所以不存在，仅仅是因为两个 one-sided limits（单侧极限）$\lim_{x \to x_0^+} f(x)$ 与 $\lim_{x \to x_0^-} f(x)$ 存在却不一致。在这种情况下，无论 $f(x_0)$ 取什么值，这总是一个不连续点。

我们称此为 $f$ 的 jump discontinuity（跳跃不连续）。两个极限之差

```math
\lim_{x \to x_0^+} f(x) - \lim_{x \to x_0^-} f(x)
```

是不连续“大小”的一种度量，称为 jump（跳跃）。

<span style="color:#c0392b">**Essential Discontinuities（本质不连续）**</span>

最后，最难对付的一类不连续是这样的情形：$\lim_{x \to x_0} f(x)$ 不存在，并且两个 right-hand and left-hand limits（右极限与左极限）$\lim_{x \to x_0^+} f(x)$ 与 $\lim_{x \to x_0^-} f(x)$ 中至少有一个（也许两个都）也都不存在。同样，无论 $f(x_0)$ 取什么值，这总是一个不连续点。我们称此为 $f$ 的 essential discontinuity（本质不连续）。

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 5.54（例 5.54）</span>

> <span style="color:#7f8c8d;">TBB §5.9.1, p.226</span>

设对所有 $x \ne 0$ 有 $f(x) = 0$，并设 $f(0) = 2$。显然，$0$ 是 $f$ 的一个可去不连续点。或许这个例子显得完全是人为构造的。一个更自然的例子是如下公式给出的函数：

```math
f(x) = \frac{x+1}{x^2 - 1} \quad (x \ne \pm 1), \qquad f(1) = c_1, \quad f(-1) = c_2.
```

这个函数在除 $x = \pm 1$ 以外的每一点显然都连续，但可能有两个不连续点，一个在 $-1$，一个在 $1$。不过，其中有一个并不是严重的不连续，因为它是可去的。你应该试着确定哪一个可去、哪一个本质。

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 5.55（例 5.55）</span>

> <span style="color:#7f8c8d;">TBB §5.9.1, p.226</span>

设 $f(x)$ 在 $x < 0$ 时定义为线性函数 $x + 1$，在 $x \ge 0$ 时定义为另一线性函数 $2x - 1$。那么在 $0$ 处有一个不连续，因为

```math
\lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} (2x - 1) = -1
```

而

```math
\lim_{x \to 0^-} f(x) = \lim_{x \to 0^-} (x + 1) = 1.
```

在这种情况下，跳跃的大小为 $-2$。画一幅图就能精确地显示这个跳跃代表什么。

---

---

> <span style="color:#1e8449;">**[note] Note（译者注）——不连续点的三层分类：一个"可修复性"的谱系：**</span>
> 教材将不连续点按"严重程度"分为三级，其区分依据本质上是极限的存在性。可去不连续（removable）：$\lim f(x)$ 存在但不等于 $f(x_0)$——只需重定义一点即可修复，是最"温和"的断点。跳跃不连续（jump）：两个单侧极限均存在但不相等——无论 $f(x_0)$ 如何定义都无法消除，但在该点左右的行为仍是可控的（例如阶梯函数在整数点的行为）。本质不连续（essential）：至少一个单侧极限不存在——这是真正"不可控"的断裂。用 6.042J 的语言，可去不连续相当于函数在单点上"写错了值"；跳跃不连续则像是「左极限和右极限之间有一个无法弥合的裂缝」；本质不连续则完全超出了极限语言的控制范围。📖 联系 Theorem 5.60：单调函数自动排除了本质不连续和可去不连续，只可能产生跳跃——这是单调性给出的强约束。

---

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">5.9.2 Monotonic Functions（单调函数）</span>

> <span style="color:#7f8c8d;">TBB §5.9.2, p.227–228 —— 书页 227 的习题 5.9.2–5.9.9 按约定跳过；本节含定义 5.56–5.59、定理 5.60 及其证明</span>

一般而言，关于任意函数的 continuity（连续性），并没有太多可说的。一个函数有可能 discontinuous everywhere（处处不连续）。但若函数是 monotonic（单调）的，这种情况就不可能发生。我们先给出一些定义，这些定义无论在此处还是日后许多地方都会用到。

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">Definition 5.56 (Nondecreasing)（定义 5.56（非降））</span>

> <span style="color:#7f8c8d;">TBB §5.9.2, p.227</span>

设 $f$ 是定义在区间 $I$ 上的 real valued（实值）函数。若只要 $x_1$ 与 $x_2$ 是 $I$ 中的点且 $x_1 < x_2$，就有 $f(x_1) \leq f(x_2)$，则称 $f$ 在 $I$ 上是 nondecreasing（非降）的。

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">Definition 5.57 (Increasing)（定义 5.57（递增））</span>

> <span style="color:#7f8c8d;">TBB §5.9.2, p.227</span>

设 $f$ 是定义在区间 $I$ 上的实值函数。若只要 $x_1$ 与 $x_2$ 是 $I$ 中的点且 $x_1 < x_2$，严格不等式 $f(x_1) < f(x_2)$ 就成立，则称 $f$ 在 $I$ 上是 increasing（递增）的。

在相反的方向上，我们相应地定义 nonincreasing（非增）与 decreasing（递减）。<sup>1</sup>

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">Definition 5.58 (Nonincreasing)（定义 5.58（非增））</span>

> <span style="color:#7f8c8d;">TBB §5.9.2, p.227</span>

设 $f$ 是定义在区间 $I$ 上的实值函数。若只要 $x_1$ 与 $x_2$ 是 $I$ 中的点且 $x_1 < x_2$，就有 $f(x_1) \geq f(x_2)$，则称 $f$ 在 $I$ 上是 nonincreasing（非增）的。

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">Definition 5.59 (Decreasing)（定义 5.59（递减））</span>

> <span style="color:#7f8c8d;">TBB §5.9.2, p.227</span>

设 $f$ 是定义在区间 $I$ 上的实值函数。若只要 $x_1$ 与 $x_2$ 是 $I$ 中的点且 $x_1 < x_2$，严格不等式 $f(x_1) > f(x_2)$ 就成立，则称 $f$ 在 $I$ 上是 decreasing（递减）的。

> 脚注 1：有些作者用 "increasing（递增）" 与 "strictly increasing（严格递增）" 来称呼我们所谓的 nondecreasing（非降）与 increasing（递增）。参见第 298 页的评论。

一个函数，若它是 nonincreasing 或 nondecreasing 的，就称为是单调的。有时，为了强调其中的不等式是严格的，我们说一个 increasing 或 decreasing 的函数是 strictly monotonic（严格单调）的。

就连续性而言，单调函数类具有一个特别有趣的结构。这样的函数绝不会出现 essential discontinuity（本质不连续）。这是因为，若 $f$ 是单调非降或单调非增的，那么在任意一点，one-sided limit（单侧极限）$\lim_{x \to x_0^+} f(x)$ 与 $\lim_{x \to x_0^-} f(x)$ 都存在。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 5.60（定理 5.60）</span>

> <span style="color:#7f8c8d;">TBB §5.9.2, p.228</span>

设 $f$ 在区间 $I$ 上单调。若 $x_0$ 是 $I$ 的 interior point（内点），则单侧极限 $\lim_{x \to x_0^-} f(x)$ 与 $\lim_{x \to x_0^+} f(x)$ 都存在。

<span style="color:#2471a3;">**[proof]**</span> **Proof（证明）：**

> 假设 $f$ 在 $I$ 上非降；$f$ 非增的情形随后即可得出，只需注意到此时 $-f$ 是非降的。为证明定理 5.60，设 $x_0$ 是 $I$ 的内点，并设 $\{x_k\}$ 是 $I$ 中一列递增的点，满足 $\lim_{k \to \infty} x_k = x_0$。于是序列 $\{f(x_k)\}$ 是一个以 $f(x_0)$ 为上界的非降数列。因此，根据 monotone convergence principle（单调收敛原理），$\{f(x_k)\}$ 趋近于某个极限 $L$。
> 
> 对满足 $x_k < x < x_0$ 的一切 $x$，有
> 
> ```math
> f(x_k) \leq f(x) \leq L.
> ```
> 
> 设 $\varepsilon > 0$。由于 $f(x_k) \to L$，存在 $N \in \mathbb{N}$ 使得当 $k \geq N$ 时 $L - f(x_k) < \varepsilon$。于是对所有满足 $x_N \leq x \leq x_0$ 的 $x$，我们都有
> 
> ```math
> L - f(x) \leq L - f(x_N) < \varepsilon.
> ```
> 
> 由此推出 $\lim_{x \to x_0^-} f(x) = L$，所以 $f$ 在 $x_0$ 处有 left-hand limit（左极限）。类似的论证表明，$f$ 在 $x_0$ 处也有 right-hand limit（右极限）。$\square$

**Monotonic Functions Have Jump Discontinuities（单调函数只具有跳跃不连续）。** 回顾一下，称函数 $f$ 在 $x_0$ 处有一个 jump（跳跃），是指 $f$ 在 $x_0$ 处既有左极限又有右极限，但这两个极限不同。于是，比方说，若 $f$ 是单调非降的，那么显然

```math
\lim_{x \to x_0^-} f(x) \leq f(x_0) \leq \lim_{x \to x_0^+} f(x).
```

因此，在点 $x_0$ 处出现 discontinuity（不连续）的唯一可能，是跳跃

```math
J(x_0) = \lim_{x \to x_0^+} f(x) - \lim_{x \to x_0^-} f(x)
```

为正。所以单调函数既没有 removable discontinuity（可去不连续），也没有 essential discontinuity（本质不连续）；它们只具有 jump discontinuity（跳跃不连续）。

我们还可以更进一步。我们自然要问：可能出现不连续的那些点所构成的集合是怎样的？我们追问：这个集合能有多大？答案是"并不大"。

**Monotonic Functions Have Countably Many Discontinuities（单调函数只有可数个不连续点）。**

---

> <span style="color:#7f8c8d;">TBB §5.9, p.229</span>

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 5.61（定理 5.61）</span>

> <span style="color:#7f8c8d;">TBB §5.9, p.229</span>

设 $f$ 在区间 $[a, b]$ 上 monotonic（单调）。则 $f$ 在该区间内的 point of discontinuity（不连续点）之集合是 countable（可数的）。特别地，$f$ 必然在 $[a, b]$ 中某个 dense（稠密）集合的所有点处连续。

<span style="color:#2471a3;">**[proof]**</span> **Proof（证明）：**

> 我们再次考虑 $f$ 为 nondecreasing（非降）的情形，因为 nonincreasing（非增）的情形可以通过考虑函数 $-f$ 而得出。若 $f$ 非降，且在 $(a, b)$ 中的某点 $x_0$ 处不连续，则开区间
> 
> ```math
> I(x_0) = \left( \lim_{x \to x_0^-} f(x),\; \lim_{x \to x_0^+} f(x) \right)
> ```
> 
> 要么不含 $f$ 的 range（值域）中的任何点，要么在值域中只含有唯一的一个点 $f(x_0)$。（要检验这一论断，见 Exercise 5.9.12。）于是，$f$ 在区间 $I$ 中的每一个不连续点 $x_0$ 都对应着一个区间 $I(x_0)$。对于两个不同的不连续点 $x_1$ 与 $x_2$，区间 $I(x_1)$ 与 $I(x_2)$ 是 disjoint（不相交的），因为 $f$ 非降。但 $\mathbb{R}$ 中任何一族两两不相交的区间都可以排列成一个序列（Exercise 4.6.10），因此 $f$ 的不连续点至多只能有可数多个。$\square$

构造具有无穷多个不连续点的单调函数是很容易的。例如，若在 $[n, n+1)$ 上 $f(x) = n$，则 $f$ 在一切整数处都有 jump（跳跃）。自然要问：哪些可数集合能够成为某个单调函数 $f$ 的不连续点集合？例如，是否存在一个 increasing（递增）函数，它在 $\mathbb{R}$ 中的每一个有理数处都不连续？（Exercise 5.9.14 给出了答案。）

<span style="color:#2471a3;">**[example]**</span> **Example 5.62（例 5.62）**

> <span style="color:#7f8c8d;">TBB §5.9, p.229</span>

我们的定理表明，一个单调函数可能不连续的点至多构成一个可数集合。若给定的不连续点集合是有限的，那么很容易找到具有这种 prescribed（预先指定的）不连续点集合的单调函数例子。那么，是否可以任意给定一个可数集合，我们就能找到一个单调函数，使其不连续点恰好等于该集合？

答案出人意料地，是肯定的。设 $C$ 是 $(a, b)$ 的一个可数子集。把它的元素列成 $c_1, c_2, c_3, \ldots$。对 $a \le x \le b$，定义函数为

```math
f(x) = \sum_{c_n < x} \frac{1}{2^n}.
```

这个函数难以直观想象，因为它依赖于各项的排列顺序。显然，$f(a) = 0$，$f(b) = 1$。其他取值就远不那么清楚了。但我们能够看到，在点 $c_1$ 处有大小为 $1/2$ 的跳跃，在点 $c_2$ 处有大小为 $1/4$ 的跳跃，在点 $c_3$ 处有大小为 $1/8$ 的跳跃，依此类推。在 $C$ 稠密的任何子区间上，该函数是 strictly increasing（严格递增）的；而在任何不含 $C$ 中点的区间上，它将为常数。可以证明，该函数唯一的不连续点恰出现在 $C$ 的各点处。

---

---

> <span style="color:#1e8449;">**[note] Note（译者注）——单调函数的可数个不连续点：把每个跳跃"装进"一个有理数：**</span>
> Theorem 5.61 的证明运用了一个在分析学中反复出现的技巧：将每个不连续点 $x_0$ 映射到一个与之唯一关联的开区间 $I(x_0)=(\lim_{x \to x_0^-} f,\ \lim_{x \to x_0^+} f)$，由于 $f$ 单调，不同不连续点对应的区间两两不相交。而 $\mathbb{R}$ 中任何一族两两不相交的开区间至多可数（每个区间可独立地包含一个不同的有理数——此处暗中使用了 $\mathbb{Q}$ 的可数性与稠密性，📖 6.042J）。这本质上是在说：单调函数的不连续点集合的"大小"被 $\mathbb{Q}$ 的基数严格限制。注意：这个上界是紧的——Example 5.62 构造了一个严格递增函数，它在任意预先指定的可数集上恰好有跳跃不连续（构造方法：$\sum_{c_n < x} 2^{-n}$）。📖 Theorem 5.64 将这一结论推广到任意函数：即使放弃单调性假设，跳跃不连续和可去不连续的集合仍然是可数的——只有本质不连续才可能"泛滥"到不可数（如 Dirichlet 函数处处本质不连续）。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">5.9.3 How Many Points of Discontinuity?（不连续点知多少？）</span>

> <span style="color:#7f8c8d;">TBB §5.9.3, p.230</span>

> <span style="color:#1e8449;">**[note] 原文标注（Advanced section）:**</span> 本节为 enrichment section（拓展节），可以略过（May be omitted）。

关于一个单调函数可能有多少个不连续点，我们已经给出了回答：这样的点所成的集合必为 countable（可数）集。我们还知道，这些不连续点全部都是 jump discontinuity（跳跃不连续）；一个单调函数既没有 removable discontinuity（可去不连续），也没有 essential discontinuity（本质不连续）。

那么对于任意函数，情况又是怎样的呢？这里有三个问题：可去不连续点可能有多少个？跳跃不连续点可能有多少个？本质不连续点可能有多少个？

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">**Example 5.63（例 5.63）**</span>

> <span style="color:#7f8c8d;">TBB §5.9.3, p.230</span>

我们之前见过的一个例子表明，本质不连续点可能有非常多。设 $f$ 为有理数的 characteristic function（特征函数）；也就是说，当 $x$ 为有理数时 $f(x) = 1$，当 $x$ 为无理数时 $f(x) = 0$。显然，对每一点 $x_0$ 都有

```math
\limsup_{x \to x_0} f(x) = 1
```

且

```math
\liminf_{x \to x_0} f(x) = 0 .
```

（由此推出的结论与后续计算见下页：极限处处不存在，每一点都是本质不连续点。）

---

> <span style="color:#7f8c8d;">书页 p.229 习题 5.9.10–5.9.11 与书页 p.230 习题 5.9.12–5.9.20 按约定保留英文原文，不收录。</span>

---

> <span style="color:#7f8c8d;">TBB §5.9.3, p.231–232</span>

> <span style="color:#7f8c8d;">本文件覆盖书页 p.231–232，续接书页 p.230 页末的 Example 5.63（有理数特征函数例）结论；页眉标题 Points of Discontinuity 见 §5.9 节首（p.229）。</span>

---

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">**Example 5.63（续）**</span>

> <span style="color:#7f8c8d;">TBB §5.9.3, p.231</span>

于是极限处处不存在，每一点都是 essential discontinuity（本质不连续）点。$\blacksquare$

---

然而，出乎意料的是（Surprisingly），removable discontinuity（可去不连续）或 jump discontinuity（跳跃不连续）的情形却并非如此。任何函数都不可能有不可数多个这样的不连续点。

---

---

> <span style="color:#1e8449;">**[note] Note（译者注）——"在不相等的两数之间插入有理数"：一个贯穿全书的隔离技巧：**</span>
> Theorem 5.64 证明的核心技巧是：「在任何跳跃不连续点 $x$ 处，左右极限之间至少存在一个有理数 $r$，使得 $\lim_{y \to x^+} f > r > \lim_{y \to x^-} f$」，然后用 $(r,n)$ 这对参数将全体跳跃点划分为可数多个集合 $J_{r,n}$（每个 $J_{r,n}$ 中的点彼此孤立，故至多可数），最后利用「可数个可数集的并可数」（📖 6.042J）得出全体跳跃点可数。教材在证明末尾特别标注——"请特别留意这种在两个不相等的数之间插入一个有理数的技巧"——这不是客套话。从 Theorem 5.61（不相交区间各含一有理数）到此处的 J_{r,n} 分划，再到后续章节的众多论证，$\mathbb{Q}$ 在 $\mathbb{R}$ 中的稠密性正是将"不可数"的连续统问题转化为"可数"的离散计数问题的关键通道。这同时也是 6.042J 中「$\mathbb{Q}$ 可数而 $\mathbb{R}$ 不可数」这一事实在分析学中发挥威力的经典案例。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 5.64（定理 5.64）</span>

> <span style="color:#7f8c8d;">TBB §5.9.3, p.231</span>

设 $f$ 是定义在区间 $[a, b]$ 上的 real function（实函数）。$f$ 在 $[a, b]$ 中具有可去不连续点的集合，以及 $f$ 在 $[a, b]$ 中具有跳跃不连续点的集合，二者都是 countable（可数的）。

---

<span style="color:#2471a3;">**[proof]**</span> **Proof（证明）:**

> 设 $J$ 为存在跳跃不连续的那些点所成的集合。$J$ 中的每一点都属于下列两个集合之一：
> 
> ```math
> J_+ = \{x \in (a, b) : \lim_{y \to x+} f(y) > \lim_{y \to x-} f(y)\}
> ```
> 
> 或
> 
> ```math
> J_- = \{x \in (a, b) : \lim_{y \to x+} f(y) < \lim_{y \to x-} f(y)\}.
> ```
> 
> 我们将证明 $J_+$ 是可数的。
> 
> 若 $x \in J_+$，则 $\lim_{y \to x+} f(y) > \lim_{y \to x-} f(y)$，于是对任何这样的 $x$，至少存在一个 rational number（有理数）$r$，使得
> 
> ```math
> \lim_{y \to x+} f(y) > r > \lim_{y \to x-} f(y).
> ```
> 
> 此外，此时必定存在某个 integer（整数）$m$（它依赖于 $x$ 与 $r$），使得只要
> 
> ```math
> x - 1/m < y < x < z < x + 1/m,
> ```
> 
> 就有
> 
> ```math
> f(z) > r > f(y).
> ```
> 
> 设 $J_{rn}$（其中 $r$ 为有理数，$n$ 为正整数）表示所有具有如下性质的点 $x$ 所成的集合：只要 $x - 1/n < y < x < z < x + 1/n$，就有 $f(y) < r < f(z)$。
> 
> 我们断言这个集合是可数的。若不然，它必然有一个 point of accumulation（聚点）；特别地，其中必定存在至少三个点 $a < b < c$，满足 $c - a < 1/n$，且它们全部属于 $J_{rn}$。但由于 $J_{rn}$ 的定义方式，且 $a$、$c \in J_{rn}$，这意味着 $f(b) < r$ 与 $r < f(b)$ 同时为真。既然这不可能，$J_{rn}$ 中所有的点便都是 isolated（孤立的），从而 $J_{rn}$ 是可数的。
> 
> 并集
> 
> ```math
> \bigcup_{r \in \mathbb{Q}} \bigcup_{n=1}^{\infty} J_{rn}
> ```
> 
> 是 countable union of countable sets（可数多个可数集的并），因而也是可数的。但这个并集包含了 $J_+$ 的每一点，故 $J_+$ 同样可数。类似地，$J_-$ 也是可数的，从而具有跳跃不连续点的集合便是可数的。
> 
> 至于函数具有可去不连续点的集合同样可数这一点，则留作练习。此处的证明思路可用来以类似的方式证明它。
> 
> 请特别留意这种在两个不相等的数之间插入一个有理数的技巧。
> 
> $\square$

---

顺便说一句（Incidentally），这一定理为关于 monotonic（单调）函数不连续点的那个定理提供了新的视角。在那一证明中，我们利用单调函数的性质来说明不连续点全体是可数的。但我们现在容易看出，此类点只能是跳跃不连续点；而根据我们这里的定理，任何函数——无论是否单调——都只有可数多个这样的点。于是我们便有了看待 Theorem 5.61（定理 5.61）的另一种方式。

---

> <span style="color:#7f8c8d;">本页下方为习题区（Exercises 区，书页 p.232，习题 5.9.21–5.9.23）以及 §5.10 Challenging Problems for Chapter 5（第 5 章挑战题），按约定保留英文原文、不收录。</span>
