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
