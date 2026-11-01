# 18.100B 实分析 Midterm Review 双语译注

**课程**：MIT 18.100B / 18.1002 Real Analysis（实分析）
**授课**：Tobias Holck Colding
**学期**：Spring 2025

> 说明：原文为 PDF 提取，公式有损（分式、求和上下标、根号等断裂），本译注已按标准数学内容补全，无法确定的处以 `〔原书此处模糊，疑似 X，待核〕` 标注。每道例题均给出完整解答。

---

## 一、实数的上下确界

**Least upper bound of a bounded set（有界集合的最小上界）** 与 **greatest lower bound of a bounded set（有界集合的最大下界）**。

设 $S\subseteq\mathbb{R}$ 非空。

- **上确界（supremum）** $\sup S$：满足"是 $S$ 的一个上界，且不大于任何其他上界"的最小上界。
- **下确界（infimum）** $\inf S$：最大下界。

实数系的**完备性公理（Completeness Axiom / Least Upper Bound Property）**：任何非空、有上界的实数子集必有上确界。这是全部分析学结论的基石。

---

## 二、数列与极限

**A sequence of real numbers（实数数列）** 是一个函数 $f:\mathbb{N}\to\mathbb{R}$。通常记 $a_n=f(n)$。

**例 1**：$\sqrt{2}$ 是数列

```math
a_1=1,\quad a_2=1.4,\quad a_3=1.41,\quad a_4=1.414,\ \dots
```

的极限（即 $\sqrt 2$ 的十进制截断逼近列）。

**例 2**：数列 $a_n=\tfrac1n$ 以 $0$ 为极限。〔原书此处写作 $a_n=\dfrac{1}{n}$，提取时断裂，已补全〕

### 极限的定义

设 $a_n$ 为数列，$a\in\mathbb{R}$。称 $a_n$ **收敛到（converges to）** $a$，若对任意 $\epsilon>0$，存在 $N\in\mathbb{N}$，使得当 $n\ge N$ 时，

```math
|a_n-a|<\epsilon.
```

此时称 $a$ 为该数列的极限（limit），称数列收敛（convergent）。不收敛的数列称为发散（divergent）。

**定理**：若 $a_n$ 收敛，则集合 $\{a_n\}$ 是 $\mathbb{R}$ 的有界子集。

> **证明**：设 $\lim_{n\to\infty}a_n=a$。取 $\epsilon=1$，则存在 $N$，当 $n\ge N$ 时 $|a_n-a|<1$，即 $a-1\lt a_n\lt a+1$。令

```math
M=\max\{a_1,a_2,\dots,a_{N-1},\,a+1\},\qquad m=\min\{a_1,a_2,\dots,a_{N-1},\,a-1\}.
```

于是对一切 $n$ 都有 $m\le a_n\le M$，故 $\{a_n\}$ 有界。∎

---

## 三、极限的基本代数性质

**定理**：设 $a_n,b_n$ 收敛，$\lim_{n\to\infty}a_n=a$，$\lim_{n\to\infty}b_n=b$，$C\in\mathbb{R}$，则：

1. $c_n=Ca_n$ 收敛，且 $\lim_{n\to\infty}c_n=Ca$。
2. $c_n=a_n+b_n$ 收敛，且 $\lim_{n\to\infty}c_n=a+b$。
3. $c_n=a_nb_n$ 收敛，且 $\lim_{n\to\infty}c_n=ab$。
4. 若 $b_n\ne 0$、$b\ne 0$ 且 $c_n=\dfrac{a_n}{b_n}$，则 $c_n$ 收敛，且 $\lim_{n\to\infty}c_n=\dfrac{a}{b}$。

> 这些用 $\epsilon\text{-}N$ 论证逐一证明。以乘积为例：由于

```math
|a_nb_n-ab|=|a_nb_n-a_nb+a_nb-ab|\le |a_n|\,|b_n-b|+|b|\,|a_n-a|,
```

而收敛数列 $\{a_n\}$ 有界（设 $|a_n|\le M$），故对任意 $\epsilon>0$，取 $N$ 充分大使 $|b_n-b|<\dfrac{\epsilon}{2M}$ 且 $|a_n-a|<\dfrac{\epsilon}{2|b|}$（若 $b=0$ 则后项直接为 $0$，更简单），于是

```math
|a_nb_n-ab|\le M\cdot\frac{\epsilon}{2M}+|b|\cdot\frac{\epsilon}{2|b|}=\epsilon.
```

商的情形由 $b_n\to b\ne0$ 推出当 $n$ 充分大时 $|b_n|\ge \tfrac{|b|}{2}$，再作估计即可。∎

---

## 四、子列

数列 $a_n$ 是函数 $f:\mathbb{N}\to\mathbb{R}$，其中 $a_n=f(n)$。$a_n$ 的**子列（subsequence）** $b_n$ 是函数的复合 $f\circ g$，其中 $g:\mathbb{N}\to\mathbb{N}$ 是**严格递增（strictly increasing）** 函数。即 $b_n=f(g(n))$。子列有时记作 $a_{n_k}$。

**定理**：数列 $a_n$ 以 $a$ 为极限的充要条件是，$a_n$ 的所有子列也都以 $a$ 为极限。

> **证明**：
>
> ($\Rightarrow$) 若 $a_n\to a$，对任意子列 $a_{n_k}$（$n_k$ 严格递增，故 $n_k\ge k$）：任给 $\epsilon>0$，存在 $N$ 使 $n\ge N$ 时 $|a_n-a|<\epsilon$。取 $K=N$，则当 $k\ge K$ 时 $n_k\ge k\ge N$，故 $|a_{n_k}-a|<\epsilon$。即 $a_{n_k}\to a$。
>
> ($\Leftarrow$) 平凡，因为 $a_n$ 本身是它自己的一个子列（取 $g(n)=n$）。∎

---

## 五、单调收敛定理（Monotone Convergence Theorem）

- **递增情形（Increasing version）**：设 $a_n$ 单调递增，即 $a_n\le a_{n+1}$。若数列有上界，则 $a_n$ 收敛，且

```math
\lim_{n\to\infty} a_n=\sup\{a_n\}.
```

- **递减情形（Decreasing version）**：设 $a_n$ 单调递减，即 $a_{n+1}\le a_n$。若 $a_n$ 有下界，则收敛，且

```math
\lim_{n\to\infty} a_n=\inf\{a_n\}.
```

> **证明（递增情形）**：设 $s=\sup\{a_n\}$（由完备性公理，$s$ 存在且有限）。任给 $\epsilon>0$，由 $s-\epsilon$ 不是上界，存在 $N$ 使 $a_N>s-\epsilon$。又因 $\{a_n\}$ 递增，当 $n\ge N$ 时 $a_n\ge a_N>s-\epsilon$，同时 $a_n\le s$。故

```math
s-\epsilon<a_n\le s<s+\epsilon,
```

即 $|a_n-s|<\epsilon$。所以 $a_n\to s$。∎

---

## 六、Cauchy 序列

数列 $a_n$ 称为 **Cauchy 序列（Cauchy sequence）**，若对任意 $\epsilon>0$，存在 $N$，使当 $m,n\ge N$ 时，

```math
|a_n-a_m|<\epsilon.
```

（直观：序列的"尾部"聚在一起。）

**定理（Cauchy 收敛定理，Cauchy Convergence Theorem）**：实数数列收敛的充要条件是它为 Cauchy 序列。

> **证明**：
>
> ($\Rightarrow$) 若 $a_n\to a$，任给 $\epsilon>0$，取 $N$ 使 $n\ge N$ 时 $|a_n-a|<\tfrac{\epsilon}{2}$，则当 $m,n\ge N$ 时

```math
|a_n-a_m|\le |a_n-a|+|a-a_m|<\frac{\epsilon}{2}+\frac{\epsilon}{2}=\epsilon.
```

> ($\Leftarrow$) 设 $\{a_n\}$ 是 Cauchy 序列。先证它有界：取 $\epsilon=1$，存在 $N$ 使 $m,n\ge N$ 时 $|a_m-a_n|<1$，特别 $|a_n-a_N|<1$，故尾部有界，加上前有限项，全列有界。
>
> 由 **Bolzano–Weierstrass 定理**（见下），有界列有收敛子列 $a_{n_k}\to a$。任给 $\epsilon>0$，由 Cauchy 性存在 $N_1$ 使 $m,n\ge N_1$ 时 $|a_m-a_n|<\tfrac{\epsilon}{2}$；由子列收敛存在 $K$ 使 $k\ge K$ 时 $|a_{n_k}-a|<\tfrac{\epsilon}{2}$，且可让 $n_k\ge N_1$。于是当 $n\ge N_1$ 时，取 $k$ 充分大使 $n_k\ge N_1$，有

```math
|a_n-a|\le |a_n-a_{n_k}|+|a_{n_k}-a|<\frac{\epsilon}{2}+\frac{\epsilon}{2}=\epsilon.
```

故 $a_n\to a$。∎

---

## 七、压缩映射

**定义（Contracting map，压缩映射）**：映射 $T:\mathbb{R}\to\mathbb{R}$ 称为压缩映射，若存在 $c<1$，使对一切 $x,y\in\mathbb{R}$ 有

```math
|T(x)-T(y)|\le c\,|x-y|.
```

（直观：映射把点之间的距离"压缩"了。）

**压缩映射定理（Contracting Mapping Theorem）**：任何压缩映射都有不动点（fixed point），即存在 $x^*$ 使 $T(x^*)=x^*$。

> **证明**：任取 $x_0$，定义迭代 $x_{n+1}=T(x_n)$。由压缩性，

```math
|x_{n+1}-x_n|=|T(x_n)-T(x_{n-1})|\le c\,|x_n-x_{n-1}|
\le \cdots \le c^n\,|x_1-x_0|.
```

对 $m>n$，

```math
|x_m-x_n|\le\sum_{k=n}^{m-1}|x_{k+1}-x_k|
\le |x_1-x_0|\sum_{k=n}^{\infty}c^k
=\frac{c^n}{1-c}\,|x_1-x_0|.
```

因 $c<1$，右端随 $n\to\infty$ 趋于 $0$，故 $\{x_n\}$ 是 Cauchy 序列，由 Cauchy 收敛定理收敛到某 $x^*$。对 $x_{n+1}=T(x_n)$ 两边取极限，利用 $T$ 的连续性（压缩映射 Lipschitz，必连续）：

```math
x^*=\lim x_{n+1}=\lim T(x_n)=T(\lim x_n)=T(x^*).
```

故 $x^*$ 是不动点。∎

---

## 八、Bolzano–Weierstrass 定理

**定理（Bolzano–Weierstrass）**：任何有界实数数列都有收敛子列。

> **证明**：设 $\{a_n\}$ 有界，即存在闭区间 $[a_0,b_0]$ 使 $a_n\in[a_0,b_0]$ 对一切 $n$。用二分法：把 $[a_0,b_0]$ 平分为两半，至少一半含无穷多项 $\{a_n\}$，取该半为 $[a_1,b_1]$。归纳构造出嵌套闭区间 $[a_k,b_k]$，每个含无穷多项，且长度 $b_k-a_k=\dfrac{b_0-a_0}{2^k}\to0$。由**闭区间套性质（nested interval property）**，交集为单点 $\{x^*\}$。
>
> 在每个 $[a_k,b_k]$ 中取一个 $a_{n_k}$，且取法保证 $n_k$ 严格递增（因为每段含无穷多项，总能往后取）。则 $a_{n_k}\in[a_k,b_k]$ 且 $a_k,b_k\to x^*$，故 $a_{n_k}\to x^*$。∎

---

## 九、函数的连续性

称函数 $f:\mathbb{R}\to\mathbb{R}$ 在点 $x_0\in\mathbb{R}$ **连续（continuous）**，若对任意 $\epsilon>0$，存在 $\delta>0$，使得当

```math
|x-x_0|<\delta \implies |f(x)-f(x_0)|<\epsilon.
```

若函数在定义域内每点连续，则称该函数连续。

**定理（序列刻画）**：若 $f:\mathbb{R}\to\mathbb{R}$ 连续，且 $x_n\to x_0$，则 $f(x_n)\to f(x_0)$。

> **证明**：任给 $\epsilon>0$，由 $f$ 在 $x_0$ 连续，存在 $\delta>0$ 使 $|x-x_0|<\delta$ 时 $|f(x)-f(x_0)|<\epsilon$。由 $x_n\to x_0$，对此 $\delta$ 存在 $N$ 使 $n\ge N$ 时 $|x_n-x_0|<\delta$。于是当 $n\ge N$ 时 $|f(x_n)-f(x_0)|<\epsilon$，故 $f(x_n)\to f(x_0)$。∎

### 连续函数的代数性质

- 若 $f,g$ 连续，则 $f+g$ 连续。
- 若 $f$ 连续、$c$ 为常数，则 $c f$ 连续。
- 若 $f,g$ 连续，则 $fg$ 连续。
- 若 $f$ 连续且 $f\ne0$，则 $\dfrac1f$ 连续。
- 若 $f,g$ 连续，则复合 $f(g(x))$ 连续。

**定理**：一切多项式（polynomial）连续。

> 由常值函数与恒等函数 $x$ 连续，再用上述加法与乘法性质逐次构造即得。∎

---

## 十、极值定理与介值定理

**极值定理（Extreme Value Theorem）**：设 $f:[a,b]\to\mathbb{R}$ 连续，则存在 $x_M\in[a,b]$ 使对一切 $x\in[a,b]$ 有 $f(x_M)\ge f(x)$；同理存在 $x_m\in[a,b]$ 使对一切 $x$ 有 $f(x_m)\le f(x)$。

> **证明（最大值，最小值同理）**：先证 $f$ 在 $[a,b]$ 上有界。反设 $f$ 无上界，则对每个 $n$ 存在 $x_n\in[a,b]$ 使 $f(x_n)>n$。由 Bolzano–Weierstrass，$\{x_n\}$ 有收敛子列 $x_{n_k}\to x^*\in[a,b]$（闭区间，极限仍在内）。由连续性 $f(x_{n_k})\to f(x^*)$，这与 $f(x_{n_k})>n_k\to\infty$ 矛盾。故 $f$ 有上界。
>
> 设 $M=\sup\{f(x):x\in[a,b]\}$（完备性公理保证存在）。要证 $M$ 被取到。由上确界定义，对每个 $n$ 存在 $x_n\in[a,b]$ 使 $M-\tfrac1n\lt f(x_n)\le M$。取收敛子列 $x_{n_k}\to x_M\in[a,b]$，由连续性

```math
f(x_M)=\lim f(x_{n_k})=M.
```

故 $f(x_M)=M\ge f(x)$ 对一切 $x$ 成立。∎

**介值定理（Intermediate Value Theorem）**：设 $f:[a,b]\to\mathbb{R}$ 连续，则对任何介于 $f(a)$ 与 $f(b)$ 之间的 $y$，存在 $x\in[a,b]$ 使 $f(x)=y$。

> **证明**：不妨设 $f(a)\lt y\lt f(b)$。令 $S=\{t\in[a,b]:f(t)\lt y\}$，则 $S$ 非空（含 $a$）且有上界（$b$），设 $c=\sup S$。下证 $f(c)=y$。
>
> 若 $f(c)\lt y$：由连续性，存在 $\delta>0$ 使 $|t-c|<\delta$ 时 $f(t)\lt y$，故存在 $t>c$ 且 $t\in S$，与 $c$ 是上界矛盾。
>
> 若 $f(c)>y$：由连续性，存在 $\delta>0$ 使 $|t-c|<\delta$ 时 $f(t)>y$，故 $c-\delta$ 也是 $S$ 的上界，与 $c=\sup S$ 矛盾。
>
> 故只能 $f(c)=y$。∎

---

## 十一、级数

设 $a_n$ 为数列，可构造新数列（部分和 partial sums）

```math
s_n=a_1+\cdots+a_n=\sum_{i=1}^{n}a_i.
```

级数 $\sum_{i=1}^{\infty}a_i$ 收敛，指部分和数列 $s_n$ 收敛，并记其极限为 $\sum_{i=1}^{\infty}a_i$。

### 几何级数（Geometric Series）

设 $a_n=c^n$，则

```math
s_n=\sum_{i=0}^{n}c^i
```

为几何级数。当且仅当 $|c|<1$ 时收敛，且此时

```math
\sum_{i=0}^{\infty}c^i=\frac{1}{1-c}.
```

当 $|c|\ge1$ 时发散。

> **证明**：由恒等式 $(1-c)s_n=1-c^{n+1}$，故 $s_n=\dfrac{1-c^{n+1}}{1-c}$。当 $|c|<1$ 时 $c^{n+1}\to0$，故 $s_n\to\dfrac1{1-c}$。当 $|c|\ge1$ 时 $|c^n|\ge1\not\to0$，通项不趋于 $0$，级数发散。∎

### 调和级数（Harmonic Series）

级数 $\sum_{i=1}^{\infty}\dfrac1i$ 称为调和级数，发散。

> **证明**：将项分组

```math
1+\frac12+\underbrace{\frac13+\frac14}_{\ge\frac12}+\underbrace{\frac15+\frac16+\frac17+\frac18}_{\ge\frac12}+\cdots
```

每组的和都不小于 $\tfrac12$，故部分和 $s_{2^k}\ge 1+\tfrac{k}{2}\to\infty$，级数发散。∎

〔原书此处写作 $\sum_{i=1}^{\infty}\dfrac1i$，提取时误显示为 $\dfrac12$，已按调和级数标准定义补全〕

### 绝对收敛（Absolutely Convergent）

称级数 $\sum_{n=0}^{\infty}a_n$ **绝对收敛（absolutely convergent）**，若 $\sum_{n=0}^{\infty}|a_n|$ 收敛。

绝对收敛蕴含收敛，反之不然。

> **证明**：若 $\sum|a_n|$ 收敛，由 Cauchy 收敛准则，对任意 $\epsilon>0$ 存在 $N$ 使 $m>n\ge N$ 时 $\sum_{k=n}^{m}|a_k|<\epsilon$。于是

```math
\left|\sum_{k=n}^{m}a_k\right|\le\sum_{k=n}^{m}|a_k|<\epsilon,
```

故 $\sum a_n$ 的部分和列是 Cauchy 列，收敛。反之，交错级数 $\sum\frac{(-1)^{n}}{n}$ 收敛但不绝对收敛（因 $\sum\frac1n$ 发散）。∎

### 非负级数收敛的充要条件

**定理**：非负项级数 $\sum_{i=0}^{\infty}a_i$（$a_i\ge0$）收敛的充要条件是部分和数列 $s_n$ 有上界。

> **证明**：非负项使 $s_n$ 单调递增。由单调收敛定理，$s_n$ 收敛当且仅当它有上界。∎

**例**：级数 $\sum_{i=1}^{\infty}\dfrac1{i^2}$ 收敛。

> **证明**：$\dfrac1{i^2}\le\dfrac1{i(i-1)}=\dfrac1{i-1}-\dfrac1i$（$i\ge2$），故部分和

```math
s_n=1+\sum_{i=2}^{n}\frac1{i^2}\le1+\sum_{i=2}^{n}\left(\frac1{i-1}-\frac1i\right)
=1+\left(1-\frac1n\right)<2.
```

部分和有上界，故收敛（比较判别法 Version 1，见下）。∎

---

## 十二、收敛判别法

- **比较判别法（Comparison Test）**
- **比值判别法（Ratio Test）**
- **根值判别法（Root Test）**

### 比较判别法

**版本 1**：设 $a_n,b_n$ 满足 $0\le a_n\le b_n$。若 $\sum_{n=1}^{\infty}b_n$ 收敛，则 $\sum_{n=1}^{\infty}a_n$ 收敛。

> **证明**：设 $A_n=\sum_{k=1}^{n}a_k$，$B_n=\sum_{k=1}^{n}b_k$。由 $a_k\le b_k$ 得 $A_n\le B_n$。因 $\sum b_n$ 收敛，$B_n$ 有上界，故 $A_n$ 有上界；又 $a_n\ge0$ 使 $A_n$ 递增，由单调收敛定理 $\sum a_n$ 收敛。∎

**版本 2（极限比较）**：设 $b_n\ne0$ 且 $\lim_{n\to\infty}\dfrac{a_n}{b_n}=L\ne0$，则 $\sum_{n=1}^{\infty}a_n$ 收敛当且仅当 $\sum_{n=1}^{\infty}b_n$ 收敛。

> **证明**：由 $\dfrac{a_n}{b_n}\to L>0$，当 $n$ 充分大时 $\dfrac{L}{2}<\dfrac{a_n}{b_n}<\dfrac{3L}{2}$，即 $\dfrac{L}{2}b_n\lt a_n<\dfrac{3L}{2}b_n$（这里假设 $a_n,b_n\ge0$）。由版本 1，$\sum b_n$ 收敛 $\Leftrightarrow$ $\sum\frac{3L}{2}b_n$ 收敛 $\Rightarrow$ $\sum a_n$ 收敛；反之 $\sum a_n$ 收敛 $\Rightarrow$ $\sum\frac{L}{2}b_n$ 收敛 $\Rightarrow$ $\sum b_n$ 收敛。∎

### 比值判别法（Ratio Test）

设 $a_n\ge0$ 且 $\dfrac{a_{n+1}}{a_n}\to a$。则

- 若 $a<1$，$\sum a_n$ 收敛；
- 若 $a>1$，$\sum a_n$ 发散；
- 若 $a=1$，无法判定（inconclusive）。

> **证明**（$a<1$ 情形）：取 $r$ 使 $a\lt r<1$，则当 $n$ 充分大时 $\dfrac{a_{n+1}}{a_n}\lt r$，故 $a_n\le a_N\,r^{n-N}$。因 $\sum r^n$（几何级数）收敛，由比较判别法 $\sum a_n$ 收敛。$a>1$ 时 $a_n$ 不趋于 $0$，故发散。∎

### 根值判别法（Root Test）

设 $a_n\ge0$，$\lim_{n\to\infty}(a_n)^{1/n}=r$。则

- 若 $r<1$，$\sum_{n=0}^{\infty}a_n$ 收敛；
- 若 $r>1$，$\sum_{n=0}^{\infty}a_n$ 发散；
- 若 $r=1$，无法判定。

> **证明**（$r<1$）：取 $s$ 使 $r\lt s<1$，当 $n$ 充分大时 $(a_n)^{1/n}\lt s$，即 $a_n\lt s^n$，由几何级数收敛与比较判别法得收敛。$r>1$ 时 $a_n>1$ 对无穷多 $n$ 成立，通项不趋于 $0$，发散。∎

---

## 十三、幂级数（Power Series）

设 $c_n$ 为数列，则 $\sum_{n=0}^{\infty}c_n x^n$ 称为幂级数。

---

## 十四、lim sup 与 lim inf

设 $a_n$ 为数列。若它无上界，则定义 $\limsup a_n=\infty$。否则定义新数列

```math
b_n=\sup\{a_n,a_{n+1},a_{n+2},\cdots\}.
```

由于假设 $\{a_n\}$ 有上界，$b_n$ 都是实数，且 $b_n$ 递减。递减是因为

```math
b_n=\sup\{a_n,a_{n+1},\cdots\}\ge\sup\{a_{n+1},a_{n+2},\cdots\}=b_{n+1}
```

（$b_{n+1}$ 的上确界取自更小的集合）。因 $b_n$ 递减，它收敛到极限 $b$（若 $b_n$ 无下界则可能是 $-\infty$）。

**定义（lim sup）**：

```math
\limsup_{n\to\infty}a_n=\lim_{n\to\infty}b_n=b.
```

类似地定义 $\liminf a_n=\lim_{n\to\infty}\left(\inf\{a_n,a_{n+1},\cdots\}\right)$。

---

## 十五、收敛半径（Radius of Convergence）

**定义**：若 $\sum_{n=0}^{\infty}a_n x^n$ 为幂级数，令

```math
R=\frac{1}{\limsup_{n\to\infty}|a_n|^{1/n}}.
```

$R$ 称为收敛半径。

**约定**：若 $\limsup_{n\to\infty}|a_n|^{1/n}=0$，收敛半径记为 $\infty$；若 $\limsup_{n\to\infty}|a_n|^{1/n}=\infty$，令 $R=0$。

由根值判别法可得：

- 幂级数在 $|x|\lt R$ 时收敛，$|x|>R$ 时发散；
- $|x|=R$ 的情形需逐例检验。

### 指数映射（Exponential Map）的幂级数定义

```math
E(x)=\sum_{n=0}^{\infty}\frac{x^n}{n!}.
```

> 该级数对一切实数 $x$ 收敛（收敛半径 $R=\infty$）。可用比值判别法：$\left|\dfrac{x^{n+1}/(n+1)!}{x^n/n!}\right|=\dfrac{|x|}{n+1}\to0<1$，故收敛。∎

---

## 十六、度量空间（Metric Space）

**定义**：度量空间是一个集合 $X$ 连同函数 $d:X\times X\to\mathbb{R}$，满足以下三条：

1. $d(x,y)\ge0$ 对一切 $x,y\in X$，且 $d(x,y)=0$ 当且仅当 $x=y$。（非负性）
2. $d(x,y)=d(y,x)$。（对称性 Symmetric）
3. $d(x,z)\le d(x,y)+d(y,z)$。（三角不等式 Triangle Inequality）

**例**：

1. $X=\mathbb{R}$，$d(x,y)=|x-y|$。
2. $X=\mathbb{R}^2$，$x=(x_1,x_2)$，$y=(y_1,y_2)$，

```math
d(x,y)=\sqrt{|x_1-y_1|^2+|x_2-y_2|^2}.
```

3. $X=\mathbb{R}^3$，$x=(x_1,x_2,x_3)$，$y=(y_1,y_2,y_3)$，

```math
d(x,y)=\sqrt{|x_1-y_1|^2+|x_2-y_2|^2+|x_3-y_3|^2}.
```

4. **区间上的连续函数空间**：$X=C([a,b])$ 是 $[a,b]$ 上连续函数全体，两个连续函数 $f,g$ 的距离定义为

```math
d(f,g)=\max_{x\in[a,b]}|f(x)-g(x)|.
```

〔原书此处写作 $|f(x-g(x)|$，括号有误，应为 $|f(x)-g(x)|$，已订正〕

### 度量空间中的序列

度量空间 $(X,d)$ 中的序列是映射 $f:\mathbb{N}\to X$，记 $f(n)$ 为 $x_n$。子列定义为严格递增映射 $g:\mathbb{N}\to\mathbb{N}$ 与 $f$ 的复合，$x_{n_k}=f(g(k))$。

**定义（度量空间中的收敛）**：若 $(X,d)$ 为度量空间，$x_n$ 为 $X$ 中的序列，称 $x_n$ 收敛到 $x$，记为 $x_n\to x$ 或 $x=\lim_{n\to\infty}x_n$，若对任意 $\epsilon>0$ 存在 $N$，使当 $n\ge N$ 时

```math
d(x,x_n)<\epsilon.
```

这等价于 $d(x_n,x)\to0$。〔原书写 $d(x_n,x_\infty)$，下标笔误，应为 $x$〕

**定义（度量空间中的 Cauchy 序列）**：若对任意 $\epsilon>0$ 存在 $N$，使当 $m,n\ge N$ 时

```math
d(x_m,x_n)<\epsilon.
```

**定理**：在任何度量空间 $(X,d)$ 中，收敛序列必为 Cauchy 序列。

> **证明**：设 $x_n\to x$，任给 $\epsilon>0$，取 $N$ 使 $n\ge N$ 时 $d(x_n,x)<\tfrac{\epsilon}{2}$，则当 $m,n\ge N$ 时

```math
d(x_m,x_n)\le d(x_m,x)+d(x,x_n)<\frac{\epsilon}{2}+\frac{\epsilon}{2}=\epsilon.
```

∎

**反例（逆命题不成立）**：取 $X=(0,1)\subset\mathbb{R}$，$d(x,y)=|x-y|$，则 $x_n=\tfrac1n$ 是 Cauchy 序列，但因 $0\notin X$，它不收敛。此时称 $X$ **不是 Cauchy 完备的（not Cauchy complete）**。

---

## 十七、期中考试可能出现的例题

> 考试允许带一页笔记（one page of notes），但禁止使用任何外部材料（笔记、计算器、电子设备）。请展示过程，论证清晰可读，无依据或难以辨认的论证可能不得满分。

### 例题 1

**证明 $\mathbb{R}^2$ 上的 Box 距离（Box distance，来自第 11 讲）构成度量空间？在 Box 度量中，序列为 Cauchy 序列意味着什么？**

**解**：Box 距离（即 $\ell^\infty$ 距离）定义为：对 $x=(x_1,x_2)$，$y=(y_1,y_2)$，

```math
d_\infty(x,y)=\max\{|x_1-y_1|,\,|x_2-y_2|\}.
```

**验证度量三公理**：

1. **非负性**：$|x_i-y_i|\ge0$，故 $d_\infty(x,y)\ge0$；且 $d_\infty(x,y)=0\iff$ 两分量差都为 $0\iff x=y$。✓
2. **对称性**：$|x_i-y_i|=|y_i-x_i|$，故 $d_\infty(x,y)=d_\infty(y,x)$。✓
3. **三角不等式**：对任意 $x,y,z\in\mathbb{R}^2$ 及 $i=1,2$，由实数绝对值三角不等式

```math
|x_i-z_i|\le|x_i-y_i|+|y_i-z_i|.
```

对 $i$ 取最大，

```math
d_\infty(x,z)=\max_i|x_i-z_i|
\le\max_i\left(|x_i-y_i|+|y_i-z_i|\right)
\le\max_i|x_i-y_i|+\max_i|y_i-z_i|
=d_\infty(x,y)+d_\infty(y,z).
```

✓

故 $(\mathbb{R}^2,d_\infty)$ 是度量空间。

**Cauchy 含义**：序列 $x^{(n)}=(x_1^{(n)},x_2^{(n)})$ 是 Cauchy 序列，指对任意 $\epsilon>0$，存在 $N$，使 $m,n\ge N$ 时

```math
d_\infty(x^{(m)},x^{(n)})=\max\{|x_1^{(m)}-x_1^{(n)}|,\,|x_2^{(m)}-x_2^{(n)}|\}<\epsilon.
```

即**两个坐标分量各自都是 $\mathbb{R}$ 中的 Cauchy 序列**。这也正是 $\max$ 度量的特点：两个分量"同时"趋于 Cauchy。

### 例题 2

**求幂级数 $\sum_{n=0}^{\infty}5^n x^n$ 的收敛半径。求幂级数 $\sum_{n=0}^{\infty}\dfrac{n^5 x^n}{n!}$ 的收敛半径。**

**解**：

（1）对 $\sum_{n=0}^{\infty}5^n x^n=\sum_{n=0}^{\infty}(5x)^n$，系数 $a_n=5^n$。

- **根值法**：$|a_n|^{1/n}=5$，故 $\limsup|a_n|^{1/n}=5$，收敛半径

```math
R=\frac1{\limsup|a_n|^{1/n}}=\frac15.
```

- **等比级数法**（更直接）：这是以 $5x$ 为公比的几何级数，当 $|5x|<1$ 即 $|x|<\tfrac15$ 时收敛，$|x|>\tfrac15$ 时发散。故 $R=\dfrac15$。

（2）对 $\sum_{n=0}^{\infty}\dfrac{n^5 x^n}{n!}$，系数 $a_n=\dfrac{n^5}{n!}$。

用**比值法**（注意是系数比值）：

```math
\left|\frac{a_{n+1}}{a_n}\right|
=\frac{(n+1)^5/(n+1)!}{n^5/n!}
=\frac{(n+1)^5}{n^5}\cdot\frac{1}{n+1}
=\left(1+\frac1n\right)^5\cdot\frac1{n+1}\to 0.
```

故 $R=\infty$，级数对一切实数 $x$ 收敛。

〔等价地用根值：$\limsup|a_n|^{1/n}=\lim\frac{n^{5/n}}{(n!)^{1/n}}=0$，故 $R=\infty$。〕

### 例题 3

**设数列由递推给出：$x_1=a$，$x_{n+1}=\dfrac{x_n}{n}$。问 $a$ 取何值时数列收敛？收敛时极限是多少？**

**解**：直接展开递推，用数学归纳法可得通项

```math
x_n=\frac{x_{n-1}}{n-1}=\frac{x_{n-2}}{(n-1)(n-2)}=\cdots
=\frac{a}{(n-1)!}.
```

即 $x_n=\dfrac{a}{(n-1)!}$。

- 若 $a=0$：$x_n=0$ 对一切 $n$，收敛，极限为 $0$。
- 若 $a\ne0$：$\dfrac1{(n-1)!}\to0$，故 $x_n\to0$。

因此**对任意实数 $a$，数列都收敛，且极限为 $0$**。

〔注意：若按字面 $x_{n+1}=\dfrac{x_n}{n}$，$n$ 从 $1$ 开始（$x_2=\dfrac{x_1}{1}=a$），则 $x_n=\dfrac{a}{(n-1)!}$，恒收敛到 $0$。〕

### 例题 4

**设 $\sum_{n=1}^{\infty}a_n$ 是级数，且 $|a_n|<\dfrac1{n^2}$。证明该级数收敛，或给出一个满足此条件但发散的级数反例。**

**解**：该级数**必收敛**。

由条件 $|a_n|<\dfrac1{n^2}$，即 $0\le |a_n|\le\dfrac1{n^2}$。而 $\sum_{n=1}^{\infty}\dfrac1{n^2}$ 收敛（前面已证，部分和 $<2$ 有上界）。由**比较判别法（版本 1）**，$\sum_{n=1}^{\infty}|a_n|$ 收敛，即原级数绝对收敛，从而收敛。∎

> 要点：$|a_n|<\dfrac1{n^2}$ 给出的是"绝对项"被 $p$-级数（$p=2>1$）控制，因此无论 $a_n$ 取何种符号都绝对收敛。**不存在**满足条件却发散的反例——这正是该题要识别出的陷阱。

---

## 附：原文页码信息

原文共 9 页（Page 1–9），末页为 MIT OpenCourseWare 版权信息：

> MIT OpenCourseWare — https://ocw.mit.edu
> 18.100B Real Analysis, Spring 2025
> 引用与使用条款见 https://ocw.mit.edu/terms
