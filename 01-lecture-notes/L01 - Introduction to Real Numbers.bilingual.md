# MIT 18.100B/18.1002 实分析 — Lecture 1（第一讲）

**Spring 2025（2025 年春季） — Tobias Holck Colding**

---

## <span style="color:#2471a3;">**[section]**</span> 本课程的两个核心主题

本课程的两个核心主题：
  • 如何书写 mathematical proof（数学证明）。
  • 如何证明 theorems（定理）。

---

## <span style="color:#2471a3;">**[example]**</span> 一个例子：Intermediate Value Theorem（介值定理）

设 $f : [a, b] \to \mathbb{R}$ 是一个 continuous function（连续函数）。
假设 $f(a) < 0$ 且 $f(b) > 0$。

Intermediate value theorem（介值定理）表明：存在某个介于 $a$ 和 $b$ 之间的 $c$，使得 $f(c) = 0$。

• 我们如何证明这一点？
• 如果我们画个图，这似乎很显然，但我们究竟如何严格证明它？

一个函数连续大致意味着，当你绘制函数图像时，笔不允许离开纸面。

• 我们如何将其转化为一个严谨的 proof（证明）？
• 这个 proof（证明）需要用到 real numbers（实数）的哪些性质？

### 引出的问题

这引出了几个问题：
  Q1：什么是 real number（实数）？
  Q2：为什么 $\sqrt{2}$ 是一个 real number（实数）？
  Q3：$\sqrt{2}$ 到底是什么？

这些问题的答案：$\mathbb{R}$ 是一个包含 rational numbers（有理数）$\mathbb{Q}$ 的 **complete ordered field（完备有序域）**。

---

## <span style="color:#2471a3;">**[section]**</span> 基本记号

(1) $\mathbb{N}$ 是 natural numbers（自然数集）。即 $\mathbb{N} = \{1, 2, 3, \dots\}$。
(2) $\mathbb{Z}$ 是 integers（整数集）。即 $\mathbb{Z} = \{0, \pm 1, \pm 2, \pm 3, \dots\}$。
(3) $\mathbb{Q}$ 是 rational numbers（有理数集）。即所有形如 $\frac{m}{n}$ 的数，其中 $m \in \mathbb{Z}$ 且 $n \in \mathbb{N}$。

---

## <span style="color:#2471a3;">**[section]**</span> Rational Numbers（有理数）的性质

Rational numbers（有理数）$\mathbb{Q}$ 是形如 $\frac{m}{n}$ 的数，其中 $m \in \mathbb{Z}$ 且 $n \in \mathbb{N}$。

(1) 两个数何时相等（When are two numbers the same）？
    $\frac{m_1}{n_1} = \frac{m_2}{n_2} \iff m_1 n_2 = m_2 n_1$

(2) 如何相加（How do we add two numbers）？
    $\frac{m_1}{n_1} + \frac{m_2}{n_2} = \frac{m_1 n_2 + m_2 n_1}{n_1 n_2}$

(3) 如何相乘（How do we multiply two numbers）？
    $\frac{m_1}{n_1} \cdot \frac{m_2}{n_2} = \frac{m_1 m_2}{n_1 n_2}$

(4) 一个数何时小于另一个（When is one number less than another）？
    $\frac{m_1}{n_1} < \frac{m_2}{n_2} \iff m_1 n_2 < m_2 n_1$

### <span style="color:#2471a3;">**[section]**</span> 乘法是 well-defined（良定义）的证明

要使这一切成立，我们需要（例如）证明乘法是 **well-defined（良定义的）**。

这意味着，如果同一个 rational number（有理数）有两种表示

```math
\frac{m_1}{n_1} = \frac{m_2}{n_2}
```

以及

```math
\frac{p_1}{q_1} = \frac{p_2}{q_2},
```

那么

```math
\frac{m_1 p_1}{n_1 q_1} = \frac{m_2 p_2}{n_2 q_2}.
```

<span style="color:#2471a3;">**[proof]**</span> **Proof（证明）：** 由假设 $m_1 n_2 = m_2 n_1$ 且 $p_1 q_2 = p_2 q_1$。因此，

```math
m_1 p_1 n_2 q_2 = (m_1 n_2)(p_1 q_2) = (m_2 n_1)(p_2 q_1) = m_2 p_2 n_1 q_1.
```

由 equality（相等）的定义，即得。

这说明了一个 proof（证明）应当细致到什么程度。

---

## <span style="color:#2471a3;">**[section]**</span> Field（域）

### <span style="color:#2471a3;">**[definition]**</span> Definition（定义）

一个 **Field（域）** $F$ 是一个 set（集合），配备了两个 operations（运算），我们暗示性地将其记为 "$+$" 和 "$\cdot$"。这两个 operations（运算）满足以下 axioms（公理）：

### Additive Properties（加法公理）

(1) $x, y \in F$，则 $x + y \in F$（closure，封闭性）
(2) $x + y = y + x$（commutativity，交换律）
(3) $(x + y) + z = x + (y + z)$（associativity，结合律）
(4) 存在一个 element（元素）$0 \in F$，使得对所有 $x \in F$ 有 $0 + x = x$（identity，零元）
(5) 对每个 $x \in F$，存在一个 element（元素）记作 $-x$，使得 $x + (-x) = 0$（inverse，相反元）

### Multiplicative Properties（乘法公理）

(1) $x, y \in F$，则 $x \cdot y \in F$（closure，封闭性）
(2) $x \cdot y = y \cdot x$（commutativity，交换律）
(3) $(x \cdot y) \cdot z = x \cdot (y \cdot z)$（associativity，结合律）
(4) 存在一个 element（元素）记作 $1$，使得对所有 $x \in F$ 有 $1 \cdot x = x$（identity，单位元）
(5) 对每个非零 $x \in F \setminus \{0\}$，存在一个 element（元素）记作 $\frac{1}{x}$，使得 $x \cdot \frac{1}{x} = 1$（inverse，倒数）

### 分配律（Distributive Law）

将 addition（加法）与 multiplication（乘法）联系起来的最后一条 axiom（公理）：

```math
(x + y) \cdot z = x \cdot z + y \cdot z
```

### <span style="color:#2471a3;">**[theorem]**</span> Theorem（定理）：零元是唯一的

**Theorem（定理）：** 在任何 field（域）中，zero（零元）是唯一的。

<span style="color:#2471a3;">**[proof]**</span> **Proof（证明）：** 假设存在两个 zero（零元），分别记作 $0_1$ 和 $0_2$。那么

```math
0_1 + 0_2 = 0_2 \quad (\text{因为 } 0_1 \text{ 是 zero})
```

且

```math
0_1 + 0_2 = 0_1 \quad (\text{因为 } 0_2 \text{ 是 zero}),
```

因此 $0_1 = 0_2$。∎

<span style="color:#2471a3;">**[example]**</span> **Examples（例子）：** $\mathbb{Q}$ 是一个 field（域），而 $\mathbb{N}$ 和 $\mathbb{Z}$ 不是 fields（域）。

---

## <span style="color:#2471a3;">**[definition]**</span> Ordered Set（有序集）

一个 **ordered set（有序集）** $S$ 是一个配备 relation（关系）$<$ 的 set（集合），满足以下 properties（性质）：

(1) 对任意 $x, y \in S$，以下三者必居其一：$x < y$ 或 $y < x$ 或 $x = y$（trichotomy，三分律）。
(2) 如果 $x, y, z \in S$ 满足 $x < y$ 且 $y < z$，则 $x < z$（transitivity，传递性）。

---

## <span style="color:#2471a3;">**[definition]**</span> Ordered Field（有序域）

一个 **ordered field（有序域）** 是一个同时为 ordered set（有序集）和 field（域）的结构，且具有以下两条将 domain operations（域运算）与 ordering（序关系）联系起来的附加 properties（性质）：

(1) 如果 $x < y$，则 $x + z < y + z$（加法保序性）。
(2) 如果 $x > 0$ 且 $y > 0$，则 $x \cdot y > 0$（正数乘法封闭）。

<span style="color:#2471a3;">**[example]**</span> **Example（例子）：** $\mathbb{Q}$ 是一个 ordered field（有序域）。

### <span style="color:#2471a3;">**[theorem]**</span> Theorem（定理）：正数乘不等式的保序性

**Theorem（定理）：** 如果 $x < y$ 且 $z > 0$，则 $x \cdot z < y \cdot z$。

<span style="color:#2471a3;">**[proof]**</span> **Proof（证明）：** 我们需要证明 $x z < y z$，等价地 $y z - x z > 0$。后者可改写为 $y z - x z = (y - x) z$。因为 $y > x$ 我们有 $y - x > 0$，又因 $z > 0$，结论得证。∎

---

## 参考文献

**[TBB]** B.S. Thomson, J.B. Bruckner, and A.M. Bruckner, *Elementary Real Analysis*, 2nd edition.

可于以下网址下载：

- <https://classicalrealanalysis.info/com/documents/TBB-AllChapters-Landscape.pdf>
- <https://classicalrealanalysis.info/com/documents/TBB-AllChapters-Portrait.pdf>

---

MIT, Dept. of Math., 77 Massachusetts Avenue, Cambridge, MA 02139-4307.

---

*MIT OpenCourseWare — <https://ocw.mit.edu>*
*18.100B 实分析 · 2025 年春季*
