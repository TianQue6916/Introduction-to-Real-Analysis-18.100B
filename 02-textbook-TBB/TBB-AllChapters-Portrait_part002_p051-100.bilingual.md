# <span style="color:#c0392b;">Elementary Real Analysis（初等实分析）</span>

> 行内双语翻译 · Part002（第2章 §2.6–§2.14 + 第3章 §3.2–§3.4）
> Second Edition (2008) · Brian S. Thomson, Judith B. Bruckner, Andrew M. Bruckner

<span style="color:#7f8c8d">**格式：** 中文主体 + `English term（中文翻译）` 嵌入 · 深红标题 · 蓝色标签 · fenced math block · 无英文原句</span>

---

## <span style="color:#c0392b;">Chapter 2. Sequences（序列）</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 本节翻译基于 PDF 实际包含的文本内容。原始 PDF（第 51–100 页，对应书本第 35–100 页）在提取过程中，第 2.7 节的部分内容（Theorem 2.14–2.16 的完整陈述与证明）以及第 2.8 节的前半部分内容（Theorem 2.18–2.21、Squeeze Theorem 等）在跨页时未被完整提取。这些内容已从 PDF 布局模式重新提取并补全。当前翻译从现有文本的起始处开始。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b;">2.6 Boundedness Properties of Limits（极限的有界性）</span>

<span style="color:#2471a3;">**[exercise]**</span> **2.5.8** 设正数 sequence（序列）$\{s_n\}$ 满足对所有 $n$ 有 $s_{n+1} > \alpha s_n$，其中 $\alpha > 1$。证明 $s_n \to \infty$。

<span style="color:#2471a3;">**[exercise]**</span> **2.5.9** 序列 $s_n = (-1)^n$ 并不 diverge to $\infty$（发散到无穷）。问：对于怎样的 $M$ 值，仍然存在整数 $N$ 使得当 $n \ge N$ 时 $s_n > M$？

<span style="color:#2471a3;">**[exercise]**</span> **2.5.10** 证明序列

```math
n^p + \alpha_1 n^{p-1} + \alpha_2 n^{p-2} + \cdots + \alpha_p
```

diverge to $\infty$（发散到无穷），其中 $p$ 是正整数，$\alpha_1, \alpha_2, \ldots, \alpha_p$ 是实数（正数或负数）。

---

<span style="color:#c0392b">**[section] 2.6 Boundedness Properties of Limits（极限的有界性）</span>

一个 sequence（序列）被称为 bounded（有界）的，如果其 range（值域）是一个 bounded set（有界集）。因此，一个序列 $\{s_n\}$ 是 bounded（有界）的，如果存在一个数 $M$ 使得序列中的每一项都满足

```math
|s_n| \le M.
```

对于这样的序列，每一项都属于区间 $[-M, M]$。

很直观地，一个无界的序列不可能收敛。这一点足够重要，值得将其陈述并证明为一个定理。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">Theorem 2.11（定理 2.11）</span> 每一个 convergent sequence（收敛序列）都是 bounded（有界）的。

> <span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.* 假设 $s_n \to L$。那么对每个数 $\varepsilon > 0$，存在整数 $N$ 使得当 $n \ge N$ 时 $|s_n - L| < \varepsilon$。特别地，我们可以取 $\varepsilon$ 的一个值，例如 $\varepsilon = 1$，并找到一个数 $N$ 使得当 $n \ge N$ 时 $|s_n - L| < 1$。由此我们看到对所有 $n \ge N$，
> 
> ```math
> |s_n| = |s_n - L + L| \le |s_n - L| + |L| < |L| + 1.
> ```
> 
> 这个数 $|L| + 1$ 将成为所有 $|s_n|$ 的一个 upper bound（上界），只是我们还没有关于 $|s_1|, |s_2|, \ldots, |s_{N-1}|$ 取值的信息。
> 因此，如果我们记
> 
> ```math
> M = \max\{|s_1|, |s_2|, \ldots, |s_{N-1}|, |L| + 1\},
> ```
> 
> 那么对每个 $n$ 值，必有
> 
> ```math
> |s_n| \le M.
> ```
> 
> 这就是一个 upper bound（上界），从而证明了定理。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这里使用的证明技巧是实分析中的基本手法：利用极限定义固定一个具体的 $\varepsilon$（此处取 $\varepsilon=1$）来控制尾部项，再单独处理前有限项。这种「拆分尾部 + 处理有限项」的思路贯穿第 2 章全部收敛性证明，是读者需要掌握的核心技能。

作为该定理的一个推论，我们可以得出结论：一个 unbounded sequence（无界序列）必定 diverge（发散）。因此，尽管这是一个相当粗糙的检验方法，但只要我们能以某种方式证明一个序列是 unbounded（无界）的，就可以证明它发散。下一个例子展示了这一技巧。

<span style="color:#2471a3;">**[example]**</span> **例 2.12：** 我们将证明序列

```math
s_n = 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \cdots + \frac{1}{n}
```

发散。最简便的证明是说明它是 unbounded（无界）的，从而由定理 2.11 可知它不能收敛。
我们只观察步点 $1, 2, 4, 8, \ldots$ 并对 $s_1, s_2, s_4, s_8, \ldots$ 做出粗略的下界估计，以证明该序列不可能有界。经过一些算术运算，我们看到

```math
\begin{aligned}
s_1 &= 1,\\
s_2 &= 1 + \frac{1}{2},\\
s_4 &= 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} > 1 + \frac{1}{2} + 2\left(\frac{1}{4}\right),\\
s_8 &= 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8}
      \ge 1 + \frac{1}{2} + 2\left(\frac{1}{4}\right) + 4\left(\frac{1}{8}\right),
\end{aligned}
```

并且一般情况下，对所有 $n = 0, 1, 2, \ldots$ 有

```math
s_{2^n} \ge 1 + n/2.
```

因此该序列不是 bounded（有界）的，从而必须 diverge（发散）。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 例 2.12 中的序列 $s_n$ 正是著名的**调和级数（harmonic series）**的部分和。其发散性的证明采用了经典的「分组放缩」技巧：将 $2^n$ 项分为一组，每组之和至少为 $1/2$，因此当 $n$ 增大时部分和可以任意大。这一方法也可用于证明更一般的结论：若 $p \le 1$，则 $p$-级数 $\sum 1/n^p$ 发散；若 $p > 1$，则收敛（后者需用积分判别法或在 §3.4 中证明）。

<span style="color:#2471a3;">**[example]**</span> **例 2.13：** 作为前一例中序列的一个变体，考虑序列

```math
t_n = 1 + \frac{1}{2^p} + \frac{1}{3^p} + \frac{1}{4^p} + \cdots + \frac{1}{n^p},
```

其中 $p$ 是任意正实数。$p=1$ 的情形我们已经发现是发散的。对于 $p < 1$，该序列比 $p=1$ 时更大，因此发散的理由更加充分。对于 $p > 1$，该序列更小，我们无法立即看出它是否 bounded（有界）；事实上，经过一些努力我们可以证明这样的序列是 bounded（有界）的。我们能得出什么结论？暂时无法得出结论。一个 unbounded sequence（无界序列）发散。而有界序列可能收敛也可能发散。

---

<span style="color:#2471a3;">**[exercise]**</span> **习题 2.6.1** 判断下列说法是否正确：

- (a) 如果 $\{s_n\}$ 是 unbounded（无界）的，那么要么 $\lim_{n\to\infty} s_n = \infty$，要么 $\lim_{n\to\infty} s_n = -\infty$。
- (b) 如果 $\{s_n\}$ 是 unbounded（无界）的，那么 $\lim_{n\to\infty} |s_n| = \infty$。
- (c) 如果 $\{s_n\}$ 和 $\{t_n\}$ 都是 bounded（有界）的，那么 $\{s_n + t_n\}$ 也是有界的。
- (d) 如果 $\{s_n\}$ 和 $\{t_n\}$ 都是 unbounded（无界）的，那么 $\{s_n + t_n\}$ 也是无界的。
- (e) 如果 $\{s_n\}$ 和 $\{t_n\}$ 都是 bounded（有界）的，那么 $\{s_n t_n\}$ 也是有界的。
- (f) 如果 $\{s_n\}$ 和 $\{t_n\}$ 都是 unbounded（无界）的，那么 $\{s_n t_n\}$ 也是无界的。

---

---

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">Theorem 2.14: Multiples of Limits（极限的数乘）</span>

设 $\{s_n\}$ 是一个 convergent sequence（收敛序列），$C$ 是一个 real number（实数）。则

```math
\lim_{n\to\infty} C s_n = C \lim_{n\to\infty} s_n.
```

> <span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.* 令 $S = \lim_{n\to\infty} s_n$。需证：对任意 $\varepsilon > 0$，存在 $N$ 使得当 $n \ge N$ 时 $|C s_n - C S| < \varepsilon$。
> 由 absolute value（绝对值）性质，$|C s_n - C S| = |C|\,|s_n - S|$。先设 $C \neq 0$。
> 给定 $\varepsilon > 0$，取 $N$ 使当 $n \ge N$ 时 $|s_n - S| < \varepsilon/|C|$。则当 $n \ge N$ 时，
> 
> ```math
> |C s_n - C S| = |C|\,|s_n - S| < |C| \cdot (\varepsilon/|C|) = \varepsilon.
> ```
> 
> 证毕。$C = 0$ 情形平凡。∎

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">Theorem 2.15: Sums/Differences of Limits（极限的和与差）</span>

设 $\{s_n\}$ 和 $\{t_n\}$ 是 convergent sequences（收敛序列）。则

```math
\lim_{n\to\infty} (s_n + t_n) = \lim_{n\to\infty} s_n + \lim_{n\to\infty} t_n
```

且

```math
\lim_{n\to\infty} (s_n - t_n) = \lim_{n\to\infty} s_n - \lim_{n\to\infty} t_n.
```

> <span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.* 令 $S = \lim_{n\to\infty} s_n$，$T = \lim_{n\to\infty} t_n$。
> 需证对任意 $\varepsilon > 0$ 存在 $N$ 使当 $n \ge N$ 时 $|(s_n + t_n) - (S + T)| < \varepsilon$。
> 由 triangle inequality（三角不等式），$|(s_n + t_n) - (S + T)| \le |s_n - S| + |t_n - T|$。
> 取 $N_1$ 使当 $n \ge N_1$ 时 $|s_n - S| < \varepsilon/2$，取 $N_2$ 使当 $n \ge N_2$ 时 $|t_n - T| < \varepsilon/2$。
> 令 $N = \max\{N_1, N_2\}$，则当 $n \ge N$ 时 $|(s_n + t_n) - (S + T)| < \varepsilon$。∎

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">Theorem 2.16: Products of Limits（极限的积）</span>

设 $\{s_n\}$ 和 $\{t_n\}$ 是 convergent sequences（收敛序列）。则

```math
\lim_{n\to\infty} (s_n t_n) = \left(\lim_{n\to\infty} s_n\right) \left(\lim_{n\to\infty} t_n\right).
```

> <span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.* 令 $S = \lim_{n\to\infty} s_n$，$T = \lim_{n\to\infty} t_n$。
> 关键不等式：$|s_n t_n - S T| \le |s_n|\,|t_n - T| + |T|\,|s_n - S|$。
> 由 Theorem 2.11，$\{s_n\}$ 有界：存在 $M > 0$ 使 $|s_n| \le M$。
> 给定 $\varepsilon > 0$，取 $N_1$ 使 $|s_n - S| < \varepsilon/(2|T|+1)$（分母加 1 防 $T=0$）。
> 取 $N_2$ 使 $|t_n - T| < \varepsilon/(2M)$。令 $N = \max\{N_1, N_2\}$，则
> 
> ```math
> |s_n t_n - S T| \le |s_n|\,|t_n - T| + |T|\,|s_n - S| < M\cdot\frac{\varepsilon}{2M} + |T|\cdot\frac{\varepsilon}{2|T|+1} < \varepsilon.
> ```
> 
> 证毕。∎

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">Theorem 2.17: Quotients of Limits（极限的商）</span>

设 $\{s_n\}$ 和 $\{t_n\}$ 是 convergent sequences（收敛序列），且 $t_n \neq 0$，$\lim t_n \neq 0$。则

```math
\lim_{n\to\infty} \frac{s_n}{t_n} = \frac{\displaystyle \lim_{n\to\infty} s_n}{\displaystyle \lim_{n\to\infty} t_n}.
```

> <span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.* 先证 $\lim (1/t_n) = 1/T$。需证 $\left|\frac{1}{t_n} - \frac{1}{T}\right| < \varepsilon$。
> 
> $\left|\frac{1}{t_n} - \frac{1}{T}\right| = \frac{|t_n - T|}{|t_n|\,|T|}$。取 $N_1$ 使 $|t_n - T| < |T|/2$，则 $|t_n| \ge |T|/2$。
> 再取 $N_2$ 使 $|t_n - T| < \varepsilon|T|^2/2$。令 $N = \max\{N_1, N_2\}$，则
> 
> ```math
> \left|\frac{1}{t_n} - \frac{1}{T}\right| < \frac{\varepsilon|T|^2/2}{(|T|/2)\,|T|} = \varepsilon.
> ```
> 
> 故 $\lim (1/t_n) = 1/T$。再由 Theorem 2.16，$\lim (s_n/t_n) = (\lim s_n)(\lim 1/t_n) = (\lim s_n)/(\lim t_n)$。∎

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b;">2.7 Algebra of Limits（极限的代数运算）</span>

<span style="color:#c0392b">**[section] 2.7 Algebra of Limits（极限的代数运算）</span>

（本节开头部分涉及 Theorem 2.15——Sum Theorem（和的极限定理）、Theorem 2.16——Product Theorem（积的极限定理）以及 Theorem 2.17——Quotient Theorem（商的极限定理）的陈述与证明前半部分在原文本中缺失，以下从 Theorem 2.17 证明的中间部分开始。）

<span style="color:#2471a3;">**[proof]**</span>

> **（定理 2.17 证明续）** …当 $n \ge N_1$ 时成立。令 $N = \max\{N_1, N_2\}$，注意当 $n \ge N$ 时必有
> 
> ```math
> \left|\frac{1}{t_n} - \frac{1}{T}\right| = \frac{|t_n - T|}{|t_n|\,|T|} < \frac{\varepsilon |T|^2 / 2}{|T|^2 / 2} = \varepsilon.
> ```
> 
> 这正是 $\lim_{n\to\infty} (1/t_n) = 1/T$ 的表述。
> 现在我们通过应用 product theorem（积的极限定理）以及刚刚证明的结果来完成定理的证明，得到
> 
> ```math
> \lim_{n\to\infty} \frac{s_n}{t_n} = \left(\lim_{n\to\infty} s_n\right)\left(\lim_{n\to\infty} \frac{1}{t_n}\right) = \frac{\lim_{n\to\infty} s_n}{\lim_{n\to\infty} t_n},
> ```
> 
> 证毕。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 商的极限定理（Theorem 2.17）要求分母的极限 $T \neq 0$ 且分母项 $t_n$ 最终非零，这两个条件缺一不可：若 $T=0$，则 $s_n/t_n$ 可能发散（如 $s_n=1$、$t_n=1/n$），也可能收敛（如 $s_n=1/n$、$t_n=1/n^2$），须具体分析。证明中先证明 $\lim (1/t_n) = 1/T$，再结合积的极限定理，这种「分而治之」的策略在分析中十分典型。

---

<span style="color:#2471a3;">**[exercise]**</span> **习题 2.7.1** 通过模仿定理 2.15 第一部分的证明，证明

```math
\lim_{n\to\infty} (s_n - t_n) = \lim_{n\to\infty} s_n - \lim_{n\to\infty} t_n.
```

<span style="color:#2471a3;">**[exercise]**</span> **2.7.2** 使用积的定理以及直接从 limit（极限）定义出发，证明 $\lim_{n\to\infty} (s_n)^2 = (\lim_{n\to\infty} s_n)^2$。

<span style="color:#2471a3;">**[exercise]**</span> **2.7.3** 解释需要哪些定理来证明本节开头引入的极限计算：

```math
\lim_{n\to\infty} \frac{n^2}{2n^2 + 1}.
```

<span style="color:#2471a3;">**[exercise]**</span> **2.7.4** 证明定理 2.16，但验证并使用不等式

```math
|s_n t_n - ST| \le |(s_n - S)(t_n - T)| + |S(t_n - T)| + |T(s_n - S)|
```

代替不等式 (1)。你更喜欢哪种证明？

<span style="color:#2471a3;">**[exercise]**</span> **2.7.5** 判断下列说法是否正确：

- (a) 如果 $\{s_n\}$ 和 $\{t_n\}$ 都 diverge（发散），那么 $\{s_n + t_n\}$ 也发散。
- (b) 如果 $\{s_n\}$ 和 $\{t_n\}$ 都 diverge（发散），那么 $\{s_n t_n\}$ 也发散。
- (c) 如果 $\{s_n\}$ 和 $\{s_n + t_n\}$ 都 converge（收敛），那么 $\{t_n\}$ 也收敛。
- (d) 如果 $\{s_n\}$ 和 $\{s_n t_n\}$ 都 converge（收敛），那么 $\{t_n\}$ 也收敛。
- (e) 如果 $\{s_n\}$ 是 convergent（收敛）的，那么 $\{1/s_n\}$ 也是收敛的。
- (f) 如果 $\{s_n\}$ 是 convergent（收敛）的，那么 $\{(s_n)^2\}$ 也是收敛的。
- (g) 如果 $\{(s_n)^2\}$ 是 convergent（收敛）的，那么 $\{s_n\}$ 也是收敛的。

<span style="color:#2471a3;">**[exercise]**</span> **2.7.6** 注意 quotient theorem（商的极限定理，定理 2.17）中有一些 product theorem（积的极限定理，定理 2.16）中没有的额外 hypothesis（假设）。解释为什么这两个假设都是必需的。

<span style="color:#2471a3;">**[exercise]**</span> **2.7.7** 一个粗心的学生给出了如下对定理 2.16 的证明。找出其中的 flaw（错误）：

> "假设 $\varepsilon > 0$。选择 $N_1$ 使得当 $n \ge N_1$ 时 $|s_n - S| < \dfrac{\varepsilon}{2|T| + 1}$，再选择 $N_2$ 使得当 $n \ge N_2$ 时 $|t_n - T| < \dfrac{\varepsilon}{2|s_n| + 1}$。如果 $n \ge N = \max\{N_1, N_2\}$，那么
> 
> ```math
> |s_n t_n - ST| \le |s_n|\,|t_n - T| + |T|\,|s_n - S| \le |s_n|\frac{\varepsilon}{2|s_n| + 1} + |T|\frac{\varepsilon}{2|T| + 1} < \varepsilon.
> ```
> 
> 瞧，这样就行得通！"

<span style="color:#2471a3;">**[exercise]**</span> **2.7.8** 为什么定理 2.15 和 2.16 对处理以下极限没有帮助？

```math
\lim_{n\to\infty} \left(\sqrt{n+1} - \sqrt{n}\right) \quad\text{和}\quad \lim_{n\to\infty} \sqrt{n}\left(\sqrt{n+1} - \sqrt{n}\right).
```

你还能用什么方法？

<span style="color:#2471a3;">**[exercise]**</span> **2.7.9** 在微积分课程中，我们知道一个函数 $f : \mathbb{R} \to \mathbb{R}$ 在 $y$ 处 continuous（连续），如果对每个 $\varepsilon > 0$ 存在 $\delta > 0$ 使得对所有 $|x - y| < \delta$ 有 $|f(x) - f(y)| < \varepsilon$。证明：如果 $f$ 在 $y$ 处 continuous（连续）且 $s_n \to y$，则 $f(s_n) \to f(y)$。利用这一结论证明 $\lim_{n\to\infty} (s_n)^2 = (\lim_{n\to\infty} s_n)^2$。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b;">2.8 Order Properties of Limits（极限的序性质）</span>

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">Theorem 2.18</span>

设 $\{s_n\}$ 和 $\{t_n\}$ 是 convergent sequences（收敛序列），且对所有 $n$ 有 $s_n \le t_n$。则

```math
\lim_{n\to\infty} s_n \le \lim_{n\to\infty} t_n.
```

> <span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.* 令 $S = \lim s_n$，$T = \lim t_n$。给定 $\varepsilon > 0$，
> 取 $N_1$ 使 $|s_n - S| < \varepsilon/2$，取 $N_2$ 使 $|t_n - T| < \varepsilon/2$。
> 令 $N = \max\{N_1, N_2\}$，则当 $n \ge N$ 时 $0 \le t_n - s_n < T - S + \varepsilon$，
> 故 $-\varepsilon < T - S$。这对任意 $\varepsilon > 0$ 成立，因此 $T - S \ge 0$。∎

> <span style="color:#1e8449;">**[note] Note（注意）:**</span> 条件 $s_n \le t_n$ 只能推出 $\lim s_n \le \lim t_n$，
> 不能推出严格不等式。即使 $s_n < t_n$，极限可能相等（如 $s_n=0$，$t_n=1/n$）。见 Exercise 2.8.1。

### <span style="color:#2471a3;">**[corollary]**</span> <span style="color:#c0392b;">Corollary 2.19（推论 2.19）</span>

设 $\{s_n\}$ 是 convergent sequence（收敛序列），且 $\alpha \le s_n \le \beta$。则

```math
\alpha \le \lim_{n\to\infty} s_n \le \beta.
```

> *Proof（证明）.* 将 $\alpha$ 和 $\beta$ 视为 constant sequences（常数列），应用 Theorem 2.18。∎

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">Theorem 2.20: Squeeze Theorem（夹逼定理）</span>

设 $\{s_n\}$ 和 $\{t_n\}$ 是 convergent sequences（收敛序列），$\lim s_n = \lim t_n = L$，
且对所有 $n$ 有 $s_n \le x_n \le t_n$。则 $\{x_n\}$ 也收敛，且 $\lim x_n = L$。

> <span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.* 给定 $\varepsilon > 0$，取 $N_1$ 使 $|s_n - L| < \varepsilon$，
> 取 $N_2$ 使 $|t_n - L| < \varepsilon$。令 $N = \max\{N_1, N_2\}$，则
> $s_n - L \le x_n - L \le t_n - L$，故 $-\varepsilon < x_n - L < \varepsilon$，即 $|x_n - L| < \varepsilon$。∎

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b;">Example 2.21（例 2.21）</span>

考察 $\displaystyle \lim_{n\to\infty} \frac{\sin n\theta}{n}$。由于 $-1 \le \sin n\theta \le 1$，
故 $-\frac{1}{n} \le \frac{\sin n\theta}{n} \le \frac{1}{n}$。两侧序列均收敛到 $0$，由 Squeeze Theorem 知原序列收敛到 $0$。

---

#### 绝对值（Absolute Values）

关于序结构主题的另一条定理常常被用到。我们回忆一下，absolute value（绝对值）是直接根据序结构定义的。极限运算是否保持绝对值呢？

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**定理 2.22（绝对值的极限 Limits of Absolute Values）**</span> 设 $\{s_n\}$ 是一个 convergent sequence（收敛序列）。则序列 $\{|s_n|\}$ 也是收敛的，且

```math
\lim_{n\to\infty} |s_n| = \left|\lim_{n\to\infty} s_n\right|.
```

<span style="color:#2471a3;">**[proof]**</span> **证明**

> 令 $S = \lim_{n\to\infty} s_n$ 并设 $\varepsilon > 0$。选择 $N$ 使得当 $n \ge N$ 时 $|s_n - S| < \varepsilon$。注意到，由 triangle inequality（三角不等式），这意味着对所有 $n \ge N$ 有 $||s_n| - |S|| \le |s_n - S| < \varepsilon$。由定义可得 $\displaystyle\lim_{n\to\infty} |s_n| = |S|$，证毕。$\blacksquare$

由于最大值和最小值可以用绝对值表示，有一个推论有时很有用。

#### 最大值与最小值（Maxima and Minima）

<span style="color:#2471a3;">**[corollary]**</span> <span style="color:#c0392b;">**推论 2.23（极限的最大/最小值 Max/Min of Limits）**</span> 设 $\{s_n\}$ 和 $\{t_n\}$ 是收敛序列。则序列 $\{\max\{s_n, t_n\}\}$ 和 $\{\min\{s_n, t_n\}\}$ 也是收敛的，且

```math
\lim_{n\to\infty} \max\{s_n, t_n\} = \max\left\{\lim_{n\to\infty} s_n,\; \lim_{n\to\infty} t_n\right\}
```

和

```math
\lim_{n\to\infty} \min\{s_n, t_n\} = \min\left\{\lim_{n\to\infty} s_n,\; \lim_{n\to\infty} t_n\right\}.
```

<span style="color:#2471a3;">**[proof]**</span> **证明**

> 第一个结论可由恒等式 $\displaystyle\max\{s_n, t_n\} = \frac{s_n + t_n}{2} + \frac{|s_n - t_n|}{2}$ 以及关于和的极限定理与绝对值的极限定理推出。同样地，第二个结论可由 $\displaystyle\min\{s_n, t_n\} = \frac{s_n + t_n}{2} - \frac{|s_n - t_n|}{2}$ 推出。$\blacksquare$

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 极限的序性质（Order Properties）包括 Theorem 2.18（不等式保序性）、Theorem 2.19（夹逼定理/Squeeze Theorem）以及 Theorem 2.20/2.21（与无穷极限有关的序结论）。其中夹逼定理是求极限最常用的工具之一，特别适用于处理含有振荡或复杂表达式的序列：只需将目标序列夹在两个极限已知且相等的序列之间即可。推论 2.23 给出了 $\max$ 和 $\min$ 的极限公式，可通过绝对值恒等式直接从定理 2.15 和 2.22 导出，体现了代数性质与序性质的结合。

<span style="color:#2471a3;">**[exercise]**</span> **习题 2.8**

**2.8.1** 证明条件 $s_n < t_n$ 并不意味着 $\displaystyle\lim_{n\to\infty} s_n < \lim_{n\to\infty} t_n$。（如果在试图证明这个错误命题时修改 Theorem 2.18（定理 2.18）的证明，修改会在哪里失败？）[参见注释 20]

**2.8.2** 若 $\{s_n\}$ 是一个所有值都落在区间 $[a, b]$ 内的序列，证明 $\{s_n/n\}$ 是收敛的。

**2.8.3** 一位粗心的学生给出了以下作为 Squeeze Theorem（夹逼定理）的证明。找出其中的漏洞：
"如果 $\displaystyle\lim_{n\to\infty} s_n = \lim_{n\to\infty} t_n = L$，则在不等式 $s_n \le x_n \le t_n$ 中取极限，得到 $L \le \lim_{n\to\infty} x_n \le L$。这只有当 $\displaystyle\lim_{n\to\infty} x_n = L$ 时才可能成立。"

**2.8.4** 假设对所有 $n$ 有 $s_n \le t_n$，且 $s_n \to \infty$。你能得出什么结论？

**2.8.5** 假设 $\displaystyle\lim_{n\to\infty} \frac{s_n}{n} > 0$。证明 $s_n \to \infty$。

**2.8.6** 设 $\{s_n\}$ 和 $\{t_n\}$ 是正数序列，且 $\displaystyle\lim_{n\to\infty} \frac{s_n}{t_n} = \alpha$，且 $s_n \to \infty$。你能得出什么结论？

**2.8.7** 设 $\{s_n\}$ 和 $\{t_n\}$ 是正数序列，且 $\displaystyle\lim_{n\to\infty} \frac{s_n}{t_n} = \infty$，且 $t_n \to \infty$。你能得出什么结论？

**2.8.8** 设 $\{s_n\}$ 和 $\{t_n\}$ 是正数序列，且 $\displaystyle\lim_{n\to\infty} \frac{s_n}{t_n} = \infty$，且 $\{s_n\}$ 有界。你能得出什么结论？

**2.8.9** 设 $\{s_n\}$ 是一个正数序列。证明条件 $\displaystyle\lim_{n\to\infty} \frac{s_{n+1}}{s_n} < 1$ 蕴含 $s_n \to 0$。[参见注释 21]

**2.8.10** 设 $\{s_n\}$ 是一个正数序列。证明条件 $\displaystyle\lim_{n\to\infty} \frac{s_{n+1}}{s_n} > 1$ 蕴含 $s_n \to \infty$。[参见注释 22]

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b;">2.9 单调收敛准则（Monotone Convergence Criterion）</span>

> 在 sequence theory（序列理论）的许多应用中，我们发现所涉及的 sequences（序列）总是朝着一个方向变化：项 steadily（稳定地）越来越大或越来越小。这类序列的分析比 general sequences（一般序列）容易得多。

<span style="color:#2471a3;">**[definition]**</span> **Definition 2.24: (Increasing, 递增)** 若

```math
s_1 < s_2 < s_3 < \cdots < s_n < s_{n+1} < \cdots
```

则称序列 $\{s_n\}$ 是 increasing（递增）的。

<span style="color:#2471a3;">**[definition]**</span> **Definition 2.25: (Decreasing, 递减)** 若

```math
s_1 > s_2 > s_3 > \cdots > s_n > s_{n+1} > \cdots
```

则称序列 $\{s_n\}$ 是 decreasing（递减）的。

<span style="color:#2471a3;">**[definition]**</span> **Definition 2.26: (Nondecreasing, 不减)** 若

```math
s_1 \le s_2 \le s_3 \le \cdots \le s_n \le s_{n+1} \le \cdots
```

则称序列 $\{s_n\}$ 是 nondecreasing（不减）的。

<span style="color:#2471a3;">**[definition]**</span> **Definition 2.27: (Nonincreasing, 不增)** 若

```math
s_1 \ge s_2 \ge s_3 \ge \cdots \ge s_n \ge s_{n+1} \ge \cdots
```

则称序列 $\{s_n\}$ 是 nonincreasing（不增）的。

因此，每个 increasing（递增）序列也是 nondecreasing（不减）的，但反之不成立。具有上述四种性质（increasing、decreasing、nondecreasing 或 nonincreasing）之一的序列称为 monotonic（单调）的。Monotonic sequences（单调序列）通常比可以上下波动的序列更容易处理。

<span style="color:#2471a3;">**[theorem]**</span> **Theorem 2.28 (Monotone Convergence Theorem, 单调收敛定理)** 设 $\{s_n\}$ 是一个 monotonic sequence（单调序列）。则 $\{s_n\}$ 是 convergent（收敛）的当且仅当 $\{s_n\}$ 是 bounded（有界）的。具体地：

1. 若 $\{s_n\}$ 是 nondecreasing（不减）的，则要么 $\{s_n\}$ 有界且收敛到 $\sup\{s_n\}$，要么 $\{s_n\}$ 无界且 $s_n \to \infty$。
2. 若 $\{s_n\}$ 是 nonincreasing（不增）的，则要么 $\{s_n\}$ 有界且收敛到 $\inf\{s_n\}$，要么 $\{s_n\}$ 无界且 $s_n \to -\infty$。

> <span style="color:#2471a3;">**[proof]**</span> **Proof（证明）.** 若序列无界，则它发散——这对任何序列都成立，不仅限于 monotonic sequences（单调序列）。
> 
> 因此，只需证明：对任意有界 monotonic sequence（单调序列）$\{s_n\}$，若序列是 nondecreasing（不减）的则极限为 $\sup\{s_n\}$，若序列是 nonincreasing（不增）的则极限为 $\inf\{s_n\}$。我们证明第一种情况。
> 
> 设 $\{s_n\}$ 是 nondecreasing（不减）且有界的，令 $L = \sup\{s_n\}$。则对所有 $n$ 有 $s_n \le L$，且若 $\beta < L$，则必存在某一项 $s_m$ 使得 $s_m > \beta$。取任意 $\varepsilon > 0$。存在 $m$ 使得对所有 $n \ge m$ 有 $s_n \ge s_m > L - \varepsilon$。又已知每项 $s_n \le L$。综合得到 $L - \varepsilon < s_n \le L < L + \varepsilon$，即对所有 $n \ge m$ 有 $|s_n - L| < \varepsilon$。由定义得 $s_n \to L$，证毕。∎

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> **单调收敛定理（Monotone Convergence Theorem）**在证明中使用了实数系的 supremum（上确界）性质，这是实数完备性的体现。该定理将收敛性的判定简化为两个更容易验证的条件——单调性和有界性，无需事先知道极限值。在第 2.9 节中，该定理被反复用于判定递归定义序列的收敛性。

我们通常如何应用这一定理？假设给定一个序列 $\{s_n\}$，我们已知它是 increasing（递增）的（或者至少是 nondecreasing（不减）的）。那么要证明 $\{s_n\}$ 收敛，只需证明该序列是 bounded above（上有界）的——即找到一个数 $M$ 使得对所有 $n$ 有 $s_n \le M$。任何粗略的上界估计都能验证收敛性。

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b;">Example 2.29（例 2.29）</span>

证明序列 $s_n = 1/\sqrt{n}$ 收敛。该序列显然是 decreasing（递减）的。能否找到 lower bound（下界）？可以，所有项均为正，因此 $0$ 是一个下界。由 Monotone Convergence Theorem（单调收敛定理）可知该序列必收敛。若想进一步证明 $\displaystyle\lim_{n\to\infty} 1/\sqrt{n} = 0$，还需做更多工作；但仅就收敛性而言，只需一个粗略的下界估计就已足够。

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b;">Example 2.30（例 2.30）</span>

考察序列 $s_n = 1 + 1/2 + 1/3 + \cdots + 1/n$。该序列明显是 increasing（递增）的。若能找到 upper bound（上界）则收敛，否则发散。我们在例 2.12 中已考察过该序列——它是无界的，因此发散到无穷。

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b;">Example 2.31（例 2.31）</span>

直接用极限定义处理这样一个序列似乎相当不可能。这个序列可以递归地（recursively）定义为

```math
x_1 = \sqrt{2}, \qquad x_n = \sqrt{2 + x_{n-1}}.
```

计算前几项表明序列是递增的，因此应该可以用本节的方法来处理。

我们通过 induction（归纳法）来证明这一点。$x_1 < x_2$ 是一个简单的计算（请自行验证）。假设对某个 $n$ 有 $x_{n-1} < x_n$，并证明由此必然推出 $x_n < x_{n+1}$。但

```math
x_n = \sqrt{2 + x_{n-1}} < \sqrt{2 + x_n} = x_{n+1},
```

其中中间步骤使用了归纳假设（即 $x_{n-1} < x_n$）。由归纳法可知序列是递增的。

现在我们用归纳法证明序列是上有界的（bounded above）。任何粗略的上界都可以。显然 $x_1 < 10$。若 $x_{n-1} < 10$，则

```math
x_n = \sqrt{2 + x_{n-1}} < \sqrt{2 + 10} < 10,
```

因此再次由归纳法可知序列的所有项都小于 $10$。

由 Theorem 2.28: Monotone Convergence Theorem（单调收敛定理）可知该序列收敛。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> **单调收敛定理（Monotone Convergence Theorem）**是分析中最古老且最基本的定理之一。其本质可追溯至 Cauchy（柯西，1821）在《Cours d'Analyse》中对单调有界序列收敛性的论述。该定理表明：单调有界序列必收敛，且收敛到其上确界（递增时）或下确界（递减时）。它的重要性在于：仅通过单调性和有界性即可判定收敛，无需事先知道极限值。在 §2.9 中，该定理被反复用于判定递归定义序列的收敛性。

但收敛到多少呢？（显然它不收敛到 $10$，因为那个估计非常粗略。）这似乎不那么容易确定。但也许可以：我们知道序列收敛到某个值，设为 $L$。在等式

```math
(x_n)^2 = 2 + x_{n-1}
```

（通过对给定的递推公式两边平方得到）中，我们可以令 $n \to \infty$ 取极限。由于 $x_n \to L$，同样有 $x_{n-1} \to L$ 且 $(x_n)^2 \to L^2$。因此

```math
L^2 = 2 + L.
```

该二次方程的解只可能是 $L = -1$ 或 $L = 2$。我们知道极限 $L$ 存在且只能是 $-1$ 或 $2$。显然可以排除 $-1$，因为序列中的所有数都是正的。因此 $x_n \to 2$。$\blacksquare$

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 本例展示了处理递归定义序列的经典三步法：**(1)** 利用单调有界准则证明收敛（此处通过归纳法证明递增且有上界）；**(2)** 对递推关系两边取极限，设极限为 $L$，得到关于 $L$ 的方程；**(3)** 解方程并根据已知信息（如符号）舍去不合理解。这种方法广泛适用于形如 $x_{n+1}=f(x_n)$ 的递归序列，前提是 $f$ 连续。对方程 $L=f(L)$ 的解需结合序列的实际范围进行筛选。

<span style="color:#2471a3;">**[exercise]**</span> **习题 2.9**

**2.9.1** 通过令 $s_1 = \alpha$ 并定义

```math
s_n = \frac{(s_{n-1})^2 + \beta}{2s_{n-1}}
```

来递归地定义一个序列 $\{s_n\}$，其中 $\alpha, \beta > 0$。

(a) 证明对 $n = 1, 2, 3, \ldots$ 有

```math
\frac{(s_n - \sqrt{\beta})^2}{2s_n} = s_{n+1} - \sqrt{\beta}.
```

(b) 证明对所有 $n = 2, 3, 4, \ldots$ 有 $s_n > \sqrt{\beta}$，除非 $\alpha = \sqrt{\beta}$。如果 $\alpha = \sqrt{\beta}$ 会怎样？

(c) 证明 $s_2 > s_3 > s_4 > \cdots > s_n > \cdots$，除非 $\alpha = \sqrt{\beta}$。

(d) 该序列收敛吗？收敛到什么？

(e) 这个序列与第 2.1 节中介绍的 Newton's method（牛顿法）序列有何关系？

**2.9.2** 通过令 $t_1 = 1$ 并定义 $t_n = \sqrt{t_{n-1} + 1}$ 来递归地定义一个序列 $\{t_n\}$。该序列收敛吗？收敛到什么？

**2.9.3** 考虑序列 $s_1 = 1$ 和 $s_n = \dfrac{(s_{n-1})^2}{2}$。我们论证：若 $s_n \to L$，则 $L = \dfrac{L^2}{2}$，因此 $L^3 = 2$ 或 $L = \sqrt[3]{2}$。我们的结论是 $\displaystyle\lim_{n\to\infty} s_n = \sqrt[3]{2}$。你对这个论证有什么批评吗？

**2.9.4** 序列

```math
\frac{1 \cdot 3 \cdot 5 \cdot \ldots \cdot (2n-1)}{2 \cdot 4 \cdot 6 \cdot \ldots \cdot (2n)}
```

收敛吗？

**2.9.5** 序列

```math
\frac{2 \cdot 4 \cdot 6 \cdot \ldots \cdot (2n) \cdot 1}{1 \cdot 3 \cdot 5 \cdot \ldots \cdot (2n-1) \cdot n^2}
```

收敛吗？

**2.9.6** 几位十九世纪的数学家在其证明中使用了一个未经证明的原理，后来被称为 Nested Interval Property（嵌套区间性质）：

> 给定一个闭区间序列 $[a_1, b_1] \supset [a_2, b_2] \supset [a_3, b_3] \supset \ldots$，每个区间都是前一个区间的子区间，且区间长度收缩到零，则存在恰好一个点属于序列中的每一个区间。

证明这个陈述。对于开区间 $(a_1, b_1) \supset (a_2, b_2) \supset (a_3, b_3) \supset \ldots$ 的递降序列，这个结论还成立吗？

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b;">2.10 极限的例子（Examples of Limits）</span>

序列极限的理论现在已经发展得足够深入，我们可以研究一些有趣的极限了。本节中的每个极限都有一定的文化意义。大多数学生应该知道并识别这些极限，因为它们相当常规地出现。对我们来说，它们也是展示我们方法的机会。我们主要需要建立不等式并使用我们的一些理论。我们不需要使用 $\varepsilon$-$N$ 论证，因为我们现在拥有更精细和强大的工具。

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b;">Example 2.32: Geometric Progressions（例 2.32，几何级数）</span>

设 $r$ 是一个实数。序列

```math
1,\; r,\; r^2,\; r^3,\; r^4,\; \ldots,\; r^n,\; \ldots
```

构成一个 geometric progression（几何级数）。其极限行为是什么？

若 $r > 1$，则不难证明 $r^n \to \infty$。

若 $r \le -1$，该序列显然 diverge（发散）。

若 $r = 1$，则这只是常数序列。

有趣的情形是：若 $-1 < r < 1$，则 $\displaystyle\lim_{n\to\infty} r^n = 0$。

为证明这一点，我们使用一个简单的不等式。设 $x > 0$ 且 $n$ 为正整数。由 binomial theorem（二项式定理）（或归纳法），可证得

```math
(1 + x)^n > nx.
```

**Case (i):** 设 $0 < r < 1$。则

```math
r = \frac{1}{1+x}
```

（其中 $x = 1/r - 1 > 0$），因此

```math
0 < r^n = \frac{1}{(1+x)^n} < \frac{1}{nx} \to 0 \quad (n \to \infty).
```

由 Squeeze Theorem（夹逼定理）得 $r^n \to 0$。

**Case (ii):** 若 $-1 < r < 0$，则令 $r = -t$，其中 $0 < t < 1$。于是

```math
-t^n \le r^n \le t^n.
```

由 Case (i) 知 $t^n \to 0$。再由 Squeeze Theorem 得 $r^n \to 0$。$\blacksquare$

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b;">Example 2.33: Roots（例 2.33，根）</span>

一个有趣且常用的极限是 $\displaystyle \lim_{n\to\infty} \sqrt[n]{n} = 1$。

证明：对 $n \ge 2$，由二项式展开，若 $x > 0$ 则 $(1+x)^n > n(n-1)x^2/2$。
令 $\sqrt[n]{n} = 1 + x_n$（其中 $x_n > 0$），则 $n = (1+x_n)^n > n(n-1)x_n^2/2$，
故 $0 < x_n^2 < \frac{2}{n-1} \to 0$。由 Squeeze Theorem 得 $x_n \to 0$，从而 $\sqrt[n]{n} \to 1$。

特例：对任意正常数 $C$ 有 $\sqrt[n]{C} \to 1$（若 $C>1$ 则夹逼于 $1$ 与 $\sqrt[n]{n}$ 之间；
若 $0\lt C<1$ 则考虑 $\sqrt[n]{C} = 1/\sqrt[n]{1/C} \to 1$）。$\blacksquare$

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b;">Example 2.34: Sums of Geometric Progressions（例 2.34，几何级数的和）</span>

对区间 $(-1, 1)$ 中的所有 $x$ 值，有

```math
\lim_{n\to\infty} \left(1 + x + x^2 + x^3 + \cdots + x^n\right) = \frac{1}{1-x}.
```

这个结果初看令人惊讶，但一旦验证了恒等式

```math
(1 - x)\left(1 + x + x^2 + x^3 + \cdots + x^n\right) = 1 - x^{n+1},
```

（只需直接相乘即可），就变得相当显然。因此

```math
\lim_{n\to\infty} \left(1 + x + x^2 + x^3 + \cdots + x^n\right)
= \lim_{n\to\infty} \frac{1 - x^{n+1}}{1 - x}
= \frac{1}{1-x},
```

其中我们使用了之前证明的结论：若 $|x| < 1$ 则 $x^{n+1} \to 0$。

一个值得记住的特例是 $x = 1/2$：

```math
\lim_{n\to\infty} \left(1 + \frac{1}{2} + \frac{1}{2^2} + \frac{1}{2^3} + \cdots + \frac{1}{2^n}\right) = 2.
```

$\blacksquare$

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b;">Example 2.35: Decimal Expansions（例 2.35，小数展开）</span>

无限十进制展开 $x = 0.d_1 d_2 d_3 d_4 \ldots d_n \ldots$（其中 $0 \le d_i \le 9$）的数学含义是什么？循环小数（Repeating decimals）总可以化为分数，因此可以避免无限过程。但如果小数模式不重复，就需要不同的解释。

最直接的解读是：$x$ 是有限小数序列 $\lim_{n\to\infty} 0.d_1 d_2 d_3 \ldots d_n$ 的极限。
但如何保证该极限存在？我们的理论提供了即时答案：该序列是非递减的（nondecreasing），且每一项都小于 $1$，
由 Monotone Convergence Theorem（单调收敛定理）可知该序列收敛——无论小数位的选择如何。$\blacksquare$

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b;">Example 2.36: Expansion of $e^x$（例 2.36，$e^x$ 的展开）</span>

设 $x > 0$，考虑两个密切相关的序列：

```math
s_n = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots + \frac{x^n}{n!},
\qquad t_n = \left(1 + \frac{x}{n}\right)^n.
```

在更高等的数学中，可以证明两个序列都收敛到 $e^x$。

首先证明 $\{s_n\}$ 收敛。取整数 $N > 2x$，则对 $n \ge N$ 有

```math
s_n = s_{N-1} + \frac{x^N}{N!} + \frac{x^{N+1}}{(N+1)!} + \cdots
\le s_{N-1} + \frac{x^N}{N!}\left(1 + \frac{x}{N+1} + \frac{x^2}{(N+1)(N+2)} + \cdots\right).
```

由于 $N > 2x$，分母增长快于分子，括号内的几何级数收敛。故 $\{s_n\}$ 递增且有上界，由 Monotone Convergence Theorem（单调收敛定理）知其收敛。

为处理 $\{t_n\}$，先应用二项式定理：

```math
\begin{aligned}
t_n &= \left(1 + \frac{x}{n}\right)^n \\
&= 1 + x + \frac{1 - 1/n}{2!}x^2 + \frac{(1 - 1/n)(1 - 2/n)}{3!}x^3 + \cdots \\
&\le s_n.
\end{aligned}
```

由此 $\{t_n\}$ 递增且有上界 $s_n$，再次由单调收敛定理知 $\{t_n\}$ 收敛，且

```math
\lim_{n\to\infty} t_n \le \lim_{n\to\infty} s_n.
```

为证相反不等式，固定 $m$ 且取 $n > m$，则

```math
t_n > 1 + x + \frac{1 - 1/n}{2!}x^2 + \cdots + \frac{(1 - 1/n)(1 - 2/n)\cdots(1 - [m-1]/n)}{m!}x^m.
```

固定 $m$ 并令 $n \to \infty$，得

```math
\lim_{n\to\infty} t_n \ge s_m
```

对每个 $m$ 成立，故

```math
\lim_{n\to\infty} t_n \ge \lim_{n\to\infty} s_n.
```

因此 $\lim s_n = \lim t_n$，记为该公共值即 $e^x$。$\blacksquare$
<span style="color:#2471a3;">**[exercise]**</span> **习题 2.10**

**2.10.1** 既然我们知道

```math
1 + x + x^2 + x^3 + \cdots + x^n \to \frac{1}{1-x},
```

这就暗示了公式

```math
1 + 2 + 4 + 8 + 16 + \cdots = \frac{1}{1-2} = -1.
```

你有什么批评意见吗？[参见注释 23]

**2.10.2** 设 $\alpha$ 和 $\beta$ 为正数。讨论序列 $\dfrac{\alpha\beta^n}{\beta\alpha^n}$ 的收敛行为。

**2.10.3** 定义

```math
e = \lim_{n\to\infty}\left(1 + \frac{1}{n}\right)^n.
```

证明 $2 < e < 3$。

**2.10.4** 证明

```math
\lim_{n\to\infty}\left(1 + \frac{1}{2n}\right)^n = \sqrt{e}.
```

**2.10.5** 验证简单的恒等式

```math
\left(1 + \frac{2}{n}\right) = \left(1 + \frac{1}{n+1}\right)\left(1 + \frac{1}{n}\right),
```

并利用它证明

```math
\lim_{n\to\infty}\left(1 + \frac{2}{n}\right)^n = e^2.
```

<span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b;">2.11 Subsequences（子序列）</span>

序列

```math
1,\,-1,\,2,\,-2,\,3,\,-3,\,4,\,-4,\,5,\,-5,\ldots
```

在其内部似乎包含了两个序列

```math
1,\,2,\,3,\,4,\,5,\ldots\quad\text{和}\quad-1,\,-2,\,-3,\,-4,\,-5,\ldots
```

以及许多其他的序列。为了对此进行表述，我们引入 subsequence（子序列）这一术语。我们会说后两个序列是第一个序列的 subsequences（子序列）。通常，研究序列的最佳方式之一就是考察它的某些子序列。但这一术语的恰当定义是什么？我们需要一种正式的数学语言来表达"通过划掉原序列中的一些项得到子序列"这一模糊概念。

<span style="color:#2471a3;">**[definition]**</span> **Definition 2.37: (Subsequences, 子序列).**
设 $\{s_n\}$ 为一个 sequence（序列），并设 $\{n_k\}$ 为 natural numbers（自然数）的一个 increasing sequence（递增序列），即 $n_1 < n_2 < n_3 < \cdots$。那么序列 $\{s_{n_k}\}$ 被称为 $\{s_n\}$ 的一个 **subsequence（子序列）**。

换句话说，一个 subsequence 是从原序列中选取无限多项而得到的新序列，选取时保持它们在原序列中的相对顺序。

<span style="color:#2471a3;">**[example]**</span> **Example 2.38（例 2.38）.** 对于序列 $s_n = (-1)^n n$，考虑由 $n_k = 2k-1$（奇数下标）给出的子序列 $s_{2k-1} = -(2k-1)$，以及由 $n_k = 2k$（偶数下标）给出的子序列 $s_{2k} = 2k$。这些都是原序列的子序列。

<span style="color:#2471a3;">**[theorem]**</span> **Theorem 2.39（子序列与收敛性）.**
一个序列 $\{s_n\}$ converges（收敛）到 $s$ 当且仅当它的每一个 subsequence（子序列）都收敛到 $s$。

> <span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.* 假设 $s_n \to s$，且设 $\{s_{n_k}\}$ 为任意子序列。对任意 $\varepsilon > 0$，存在 $N$ 使得当 $n \ge N$ 时 $|s_n - s| < \varepsilon$。由于 $n_k \ge k$（习题 2.11.10），当 $k \ge N$ 时也有 $n_k \ge N$，因此 $|s_{n_k} - s| < \varepsilon$ 对所有 $k \ge N$ 成立，故 $s_{n_k} \to s$。
> 
> 反之，如果 $\{s_n\}$ 的每一个子序列都收敛到 $s$，那么特别地，$\{s_n\}$ 本身（作为自身的子序列）也收敛到 $s$。$\blacksquare$

#### 单调子序列的存在性（Existence of Monotonic Subsequences）

在序列的许多应用中，需要研究的就是子序列。例如，关于单调子序列、有界子序列、发散子序列或收敛子序列的存在性，我们能说些什么？这些问题的答案有重要的应用。第一个问题对任何特定序列都很容易回答，但要在一般情况下解决则困难得多。给定一个序列，我们能否总能选出 monotonic（单调）的子序列——无论是 nondecreasing（不减）的还是 nonincreasing（不增）的？

<span style="color:#2471a3;">**[theorem]**</span> **Theorem 2.39b（单调子序列的存在性）.**
每一个 sequence（序列）都包含一个 monotonic subsequence（单调子序列）。

> <span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.* 称下标 $n$ 为"peak（峰点）"，如果对所有 $m > n$ 都有 $s_n \ge s_m$。考虑两种情况：
> 
> **情况 1：** 存在无限多个峰点。将这些峰点记为 $n_1 < n_2 < n_3 < \cdots$。那么子序列 $\{s_{n_k}\}$ 是 decreasing（递减）的（因为 $s_{n_k} \ge s_{n_{k+1}}$），因此是一个单调子序列。
> 
> **情况 2：** 只有有限多个峰点（或没有）。设 $N$ 为最后一个峰点之后的下标。那么对任意 $n > N$，$n$ 不是峰点，因此存在 $m > n$ 使得 $s_m > s_n$。这允许我们归纳地构造一个 strictly increasing（严格递增）的子序列，从而得到一个单调子序列。
> 
> 因此，每个序列都包含一个单调子序列。$\blacksquare$

> <span style="color:#1e8449;">**[note] Note（注）.**</span> 上述证明中的"峰点论证"（peak argument）是一种标准的技巧。此外，每个有界序列都有单调子序列（这也是一个有用的观察）。

#### 收敛子序列的存在性（Existence of Convergent Subsequenc[proof]**</span> <span style="color:#c0392b;">Proof（证明）</span>

假设 $a_n$ 是有界序列。为简单起见，假设 $a_n \in [0, 1]$（换成任何有界区间论证完全一样，取 $[0,1]$ 只是让写法更干净）。

**构造子列 $a_{n_k}$。** 在区间 $[0, 1]$ 中，要么有无穷多个 $n$ 使得 $a_n \in [0, \frac{1}{2}]$，要么有无穷多个 $a_n$ 落在 $[\frac{1}{2}, 1]$ 中（也可能两者同时成立）。假设 $[0, \frac{1}{2}]$ 中含有无穷多个项。令 $a_{n_1} = a_1$，再取**原序列中 $a_1$ 之后**第一个满足 $a_n \in [0, \frac{1}{2}]$ 的项作为 $a_{n_2}$。于是

```math
n_2 > n_1 = 1, \qquad a_{n_1} \in [0, 1], \qquad a_{n_2} \in \left[0, \frac{1}{2}\right].
```

下一步：在 $[0, \frac{1}{2}]$ 中，要么有无穷多个 $a_n$ 落在 $[0, \frac{1}{4}]$，要么有无穷多个落在 $[\frac{1}{4}, \frac{1}{2}]$。（讲义原文此处误写为「$[\frac{1}{2}, \frac{1}{4}]$」，这是排印笔误——该区间为空区间，正确的两个半区间是 $[0, \frac{1}{4}]$ 与 $[\frac{1}{4}, \frac{1}{2}]$，视频中 Colding 讲的就是正确版本。）假设 $[\frac{1}{4}, \frac{1}{2}]$ 中含无穷多个项。取一个 $n > n_2$ 使得 $a_n \in [\frac{1}{4}, \frac{1}{2}]$，令 $a_{n_3} = a_n$。如此继续下去。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 构造的关键细节是：**$a_{n_2}$ 必须是原序列中 $a_1$ 之后的下一个落进新区间的元素**。Colding 在课上专门强调了这一点：如果两个下标相同，得到的就不是子列了——子列要求下标 $n_1 < n_2 < n_3 < \cdots$ 严格递增。值可以重复（比如 $a_2 = a_5 = 0.3$ 都落在同一个区间里），但**下标必须来自不同位置**。🎥 *Colding 强调:* "We don't want to have a1 again. We need another element, because otherwise it's not going to be a subsequence. You can't pick the A1. I mean, it could be the same value. But it will have to come from a different subscript."（翻译：我们不能再把 $a_1$ 选一次，需要另一个元素，否则就不是子列了。你不能重复选 $a_1$——值可以相同，但必须来自不同的下标。）
> 
> 这里「二分之后必有一半含无穷多个点」的事实，正是你在 6.042J 学过的 **infinite pigeonhole principle（无限鸽笼原理）**：把无穷多个物体放进有限个盒子，至少有一个盒子装无穷多个。离散数学里它是组合计数工具，在这里它是分析学证明的发动机——每一次二分都靠它保证「下一步有得选」，从而让构造能无限进行下去。这是同一个原理在两个学科中的不同面孔。

**$a_{n_k}$ 的收敛性。** 注意对 $k_1, k_2 \ge k$，有

```math
|a_{n_{k_1}} - a_{n_{k_2}}| \le 2^{1-k}.
```

（直观理由：从第 $k$ 步开始，子列的所有项都落在长度为 $2^{1-k}$ 的同一个区间内，区间内任意两点的距离至多等于区间长度。）由于 $2^{-k} \to 0$（当 $k \to \infty$），这说明子列 $a_{n_k}$ 是 Cauchy sequence——由 Cauchy convergence theorem 它已收敛。**但还可以说得更多。**

**夹逼。** 子列 $a_{n_k}$ 被夹在两个序列之间：$b_k \le a_{n_k} \le c_k$。定义 $b_k$ 为「第 $k$ 步所选区间」的左端点，$c_k$ 为同一区间的右端点——即所有 $i \ge k$ 的 $a_{n_i}$ 都落在长为 $2^{1-k}$ 的区间 $[b_k, c_k]$ 内。于是 $b_k$ 单调递增，$c_k$ 单调递减，而 $a_{n_k}$ 始终被夹在两者之间。由单调收敛定理（$b_k$ 递增且有界，$c_k$ 递减且有界），$b_k$ 与 $c_k$ 都收敛。又因为 $c_k - b_k = 2^{1-k} \to 0$，两者的极限是**同一个数**；既然所有足够靠后的 $a_{n_k}$ 都被夹在 $b_k$ 与 $c_k$ 之间（即夹在两个趋于同一极限的序列之间），$a_{n_k}$ 也收敛到这个数。$\square$

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Colding 在课上用一幅「动态图」讲这个夹逼结构：$b_k$ 从左向右移动（递增），$c_k$ 从右向左移动（递减），子列的点被夹在中间，随着 $k$ 增大两侧像钳子一样合拢，最终把子列「逼」到同一个极限上。🎥 *Colding 在视频中描述:* "the b's are always moving in this direction... And the ck's are moving to the left... they're coming together like this."（翻译：$b$ 序列一直往这个方向移动……$c_k$ 向左移动……它们像这样合拢。）
> 
> 注意证明的**双层结构**：先证 $a_{n_k}$ 是 Cauchy 序列（这是「够用」的），再用夹逼证它收敛到 $b_k$、$c_k$ 的共同极限（这是「更强的结论」——我们甚至知道了极限是多少的构造方式）。讲义把两步都写出来，因为夹逼这一步展示了分析学的经典套路：**要证明一个难搞的序列收敛，就找两个好搞的序列把它夹住**——这个「夹逼法」在 L05 已经出现过（squeeze 论证），在后面求各种极限时会反复用到。
> 
> 还有一个值得注意的细节：$b_k$、$c_k$ 本身并不需要是 $a_n$ 的子列——它们只是「区间端点」构成的辅助序列。这提示了一个一般方法：**证明时不要只盯着原序列，可以主动构造辅助序列来「夹」它。**

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 回顾整个 B-W 定理的证明，你会发现一个比定理本身更深刻的模式：**在 ℝ 中，「有界」和「存在收敛子列」在闭区间上是等价的。** 换句话说，B-W 定理实际上刻画了闭有界区间 $[a,b]$ 的一个深层性质——任何无穷点集在它里面都「无处可逃」，必然在某处堆积。这个性质在更高级的框架里叫 **sequential compactness（序列紧致性）**：一个集合是序列紧致的，当且仅当其中每个序列都有收敛到该集合内某点的子列。B-W 定理说「ℝ 中的闭有界区间是序列紧致的」——这是 ℝ 区别于 ℚ（有理数集）的关键特征之一：你可以构造一个有理数序列（比如十进制逼近 $\sqrt{2}$ 的序列 $1, 1.4, 1.41, 1.414, \ldots$），它在 ℝ 中收敛到无理数 $\sqrt{2}$，因此在 ℚ 内**没有任何**收敛子列。L14 会把这个概念推广到一般的 metric space（度量空间），届时「闭 + 有界」不再自动蕴含紧致性——你会在那里看到，恰好是 ℝ 的完备性（Cauchy 序列必收敛）让 B-W 定理成立。现在你不需要知道度量空间是什么，只需要记住一个心态模型：**B-W 定理 = ℝ 中「有限空间装不下无穷多个彼此远离的点」的形式化**——这个直觉在后面讨论连续函数在闭区间上的性质（最大值定理、一致连续性）时会反复兑现，那些证明几乎全是以 B-W 定理为发动机的。[proof]**</span> <span style="color:#c0392b;">Proof（证明）</span>
> 
> 假设 $a_n$ 是有界序列。为简单起见，假设 $a_n \in [0, 1]$（换成任何有界区间论证完全一样，取 $[0,1]$ 只是让写法更干净）。
> 
> **构造子列 $a_{n_k}$。** 在区间 $[0, 1]$ 中，要么有无穷多个 $n$ 使得 $a_n \in [0, \frac{1}{2}]$，要么有无穷多个 $a_n$ 落在 $[\frac{1}{2}, 1]$ 中（也可能两者同时成立）。假设 $[0, \frac{1}{2}]$ 中含有无穷多个项。令 $a_{n_1} = a_1$，再取**原序列中 $a_1$ 之后**第一个满足 $a_n \in [0, \frac{1}{2}]$ 的项作为 $a_{n_2}$。于是
> 
> ```math
> n_2 > n_1 = 1, \qquad a_{n_1} \in [0, 1], \qquad a_{n_2} \in \left[0, \frac{1}{2}\right].
> ```
> 
> 下一步：在 $[0, \frac{1}{2}]$ 中，要么有无穷多个 $a_n$ 落在 $[0, \frac{1}{4}]$，要么有无穷多个落在 $[\frac{1}{4}, \frac{1}{2}]$。（讲义原文此处误写为「$[\frac{1}{2}, \frac{1}{4}]$」，这是排印笔误——该区间为空区间，正确的两个半区间是 $[0, \frac{1}{4}]$ 与 $[\frac{1}{4}, \frac{1}{2}]$，视频中 Colding 讲的就是正确版本。）假设 $[\frac{1}{4}, \frac{1}{2}]$ 中含无穷多个项。取一个 $n > n_2$ 使得 $a_n \in [\frac{1}{4}, \frac{1}{2}]$，令 $a_{n_3} = a_n$。如此继续下去。
> 
> > <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 构造的关键细节是：**$a_{n_2}$ 必须是原序列中 $a_1$ 之后的下一个落进新区间的元素**。Colding 在课上专门强调了这一点：如果两个下标相同，得到的就不是子列了——子列要求下标 $n_1 < n_2 < n_3 < \cdots$ 严格递增。值可以重复（比如 $a_2 = a_5 = 0.3$ 都落在同一个区间里），但**下标必须来自不同位置**。🎥 *Colding 强调:* "We don't want to have a1 again. We need another element, because otherwise it's not going to be a subsequence. You can't pick the A1. I mean, it could be the same value. But it will have to come from a different subscript."（翻译：我们不能再把 $a_1$ 选一次，需要另一个元素，否则就不是子列了。你不能重复选 $a_1$——值可以相同，但必须来自不同的下标。）
> > 
> > 这里「二分之后必有一半含无穷多个点」的事实，正是你在 6.042J 学过的 **infinite pigeonhole principle（无限鸽笼原理）**：把无穷多个物体放进有限个盒子，至少有一个盒子装无穷多个。离散数学里它是组合计数工具，在这里它是分析学证明的发动机——每一次二分都靠它保证「下一步有得选」，从而让构造能无限进行下去。这是同一个原理在两个学科中的不同面孔。
> 
> **$a_{n_k}$ 的收敛性。** 注意对 $k_1, k_2 \ge k$，有
> 
> ```math
> |a_{n_{k_1}} - a_{n_{k_2}}| \le 2^{1-k}.
> ```
> 
> （直观理由：从第 $k$ 步开始，子列的所有项都落在长度为 $2^{1-k}$ 的同一个区间内，区间内任意两点的距离至多等于区间长度。）由于 $2^{-k} \to 0$（当 $k \to \infty$），这说明子列 $a_{n_k}$ 是 Cauchy sequence——由 Cauchy convergence theorem 它已收敛。**但还可以说得更多。**
> 
> **夹逼。** 子列 $a_{n_k}$ 被夹在两个序列之间：$b_k \le a_{n_k} \le c_k$。定义 $b_k$ 为「第 $k$ 步所选区间」的左端点，$c_k$ 为同一区间的右端点——即所有 $i \ge k$ 的 $a_{n_i}$ 都落在长为 $2^{1-k}$ 的区间 $[b_k, c_k]$ 内。于是 $b_k$ 单调递增，$c_k$ 单调递减，而 $a_{n_k}$ 始终被夹在两者之间。由单调收敛定理（$b_k$ 递增且有界，$c_k$ 递减且有界），$b_k$ 与 $c_k$ 都收敛。又因为 $c_k - b_k = 2^{1-k} \to 0$，两者的极限是**同一个数**；既然所有足够靠后的 $a_{n_k}$ 都被夹在 $b_k$ 与 $c_k$ 之间（即夹在两个趋于同一极限的序列之间），$a_{n_k}$ 也收敛到这个数。$\square$
> 
> > <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Colding 在课上用一幅「动态图」讲这个夹逼结构：$b_k$ 从左向右移动（递增），$c_k$ 从右向左移动（递减），子列的点被夹在中间，随着 $k$ 增大两侧像钳子一样合拢，最终把子列「逼」到同一个极限上。🎥 *Colding 在视频中描述:* "the b's are always moving in this direction... And the ck's are moving to the left... they're coming together like this."（翻译：$b$ 序列一直往这个方向移动……$c_k$ 向左移动……它们像这样合拢。）
> > 
> > 注意证明的**双层结构**：先证 $a_{n_k}$ 是 Cauchy 序列（这是「够用」的），再用夹逼证它收敛到 $b_k$、$c_k$ 的共同极限（这是「更强的结论」——我们甚至知道了极限是多少的构造方式）。讲义把两步都写出来，因为夹逼这一步展示了分析学的经典套路：**要证明一个难搞的序列收敛，就找两个好搞的序列把它夹住**——这个「夹逼法」在 L05 已经出现过（squeeze 论证），在后面求各种极限时会反复用到。
> > 
> > 还有一个值得注意的细节：$b_k$、$c_k$ 本身并不需要是 $a_n$ 的子列——它们只是「区间端点」构成的辅助序列。这提示了一个一般方法：**证明时不要只盯着原序列，可以主动构造辅助序列来「夹」它。**
> 
> > <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 回顾整个 B-W 定理的证明，你会发现一个比定理本身更深刻的模式：**在 ℝ 中，「有界」和「存在收敛子列」在闭区间上是等价的。** 换句话说，B-W 定理实际上刻画了闭有界区间 $[a,b]$ 的一个深层性质——任何无穷点集在它里面都「无处可逃」，必然在某处堆积。这个性质在更高级的框架里叫 **sequential compactness（序列紧致性）**：一个集合是序列紧致的，当且仅当其中每个序列都有收敛到该集合内某点的子列。B-W 定理说「ℝ 中的闭有界区间是序列紧致的」——这是 ℝ 区别于 ℚ（有理数集）的关键特征之一：你可以构造一个有理数序列（比如十进制逼近 $\sqrt{2}$ 的序列 $1, 1.4, 1.41, 1.414, \ldots$），它在 ℝ 中收敛到无理数 $\sqrt{2}$，因此在 ℚ 内**没有任何**收敛子列。L14 会把这个概念推广到一般的 metric space（度量空间），届时「闭 + 有界」不再自动蕴含紧致性——你会在那里看到，恰好是 ℝ 的完备性（Cauchy 序列必收敛）让 B-W 定理成立。现在你不需要知道度量空间是什么，只需要记住一个心态模型：**B-W 定理 = ℝ 中「有限空间装不下无穷多个彼此远离的点」的形式化**——这个直觉在后面讨论连续函数在闭区间上的性质（最大值定理、一致连续性）时会反复兑现，那些证明几乎全是以 B-W 定理为发动机的。[proof]**</span> <span style="color:#c0392b;">Proof（证明）</span>
> > 
> > 假设 $a_n$ 是有界序列。为简单起见，假设 $a_n \in [0, 1]$（换成任何有界区间论证完全一样，取 $[0,1]$ 只是让写法更干净）。
> > 
> > **构造子列 $a_{n_k}$。** 在区间 $[0, 1]$ 中，要么有无穷多个 $n$ 使得 $a_n \in [0, \frac{1}{2}]$，要么有无穷多个 $a_n$ 落在 $[\frac{1}{2}, 1]$ 中（也可能两者同时成立）。假设 $[0, \frac{1}{2}]$ 中含有无穷多个项。令 $a_{n_1} = a_1$，再取**原序列中 $a_1$ 之后**第一个满足 $a_n \in [0, \frac{1}{2}]$ 的项作为 $a_{n_2}$。于是
> > 
> > ```math
> > n_2 > n_1 = 1, \qquad a_{n_1} \in [0, 1], \qquad a_{n_2} \in \left[0, \frac{1}{2}\right].
> > ```
> > 
> > 下一步：在 $[0, \frac{1}{2}]$ 中，要么有无穷多个 $a_n$ 落在 $[0, \frac{1}{4}]$，要么有无穷多个落在 $[\frac{1}{4}, \frac{1}{2}]$。（讲义原文此处误写为「$[\frac{1}{2}, \frac{1}{4}]$」，这是排印笔误——该区间为空区间，正确的两个半区间是 $[0, \frac{1}{4}]$ 与 $[\frac{1}{4}, \frac{1}{2}]$，视频中 Colding 讲的就是正确版本。）假设 $[\frac{1}{4}, \frac{1}{2}]$ 中含无穷多个项。取一个 $n > n_2$ 使得 $a_n \in [\frac{1}{4}, \frac{1}{2}]$，令 $a_{n_3} = a_n$。如此继续下去。
> > 
> > > <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 构造的关键细节是：**$a_{n_2}$ 必须是原序列中 $a_1$ 之后的下一个落进新区间的元素**。Colding 在课上专门强调了这一点：如果两个下标相同，得到的就不是子列了——子列要求下标 $n_1 < n_2 < n_3 < \cdots$ 严格递增。值可以重复（比如 $a_2 = a_5 = 0.3$ 都落在同一个区间里），但**下标必须来自不同位置**。🎥 *Colding 强调:* "We don't want to have a1 again. We need another element, because otherwise it's not going to be a subsequence. You can't pick the A1. I mean, it could be the same value. But it will have to come from a different subscript."（翻译：我们不能再把 $a_1$ 选一次，需要另一个元素，否则就不是子列了。你不能重复选 $a_1$——值可以相同，但必须来自不同的下标。）
> > > 
> > > 这里「二分之后必有一半含无穷多个点」的事实，正是你在 6.042J 学过的 **infinite pigeonhole principle（无限鸽笼原理）**：把无穷多个物体放进有限个盒子，至少有一个盒子装无穷多个。离散数学里它是组合计数工具，在这里它是分析学证明的发动机——每一次二分都靠它保证「下一步有得选」，从而让构造能无限进行下去。这是同一个原理在两个学科中的不同面孔。
> > 
> > **$a_{n_k}$ 的收敛性。** 注意对 $k_1, k_2 \ge k$，有
> > 
> > ```math
> > |a_{n_{k_1}} - a_{n_{k_2}}| \le 2^{1-k}.
> > ```
> > 
> > （直观理由：从第 $k$ 步开始，子列的所有项都落在长度为 $2^{1-k}$ 的同一个区间内，区间内任意两点的距离至多等于区间长度。）由于 $2^{-k} \to 0$（当 $k \to \infty$），这说明子列 $a_{n_k}$ 是 Cauchy sequence——由 Cauchy convergence theorem 它已收敛。**但还可以说得更多。**
> > 
> > **夹逼。** 子列 $a_{n_k}$ 被夹在两个序列之间：$b_k \le a_{n_k} \le c_k$。定义 $b_k$ 为「第 $k$ 步所选区间」的左端点，$c_k$ 为同一区间的右端点——即所有 $i \ge k$ 的 $a_{n_i}$ 都落在长为 $2^{1-k}$ 的区间 $[b_k, c_k]$ 内。于是 $b_k$ 单调递增，$c_k$ 单调递减，而 $a_{n_k}$ 始终被夹在两者之间。由单调收敛定理（$b_k$ 递增且有界，$c_k$ 递减且有界），$b_k$ 与 $c_k$ 都收敛。又因为 $c_k - b_k = 2^{1-k} \to 0$，两者的极限是**同一个数**；既然所有足够靠后的 $a_{n_k}$ 都被夹在 $b_k$ 与 $c_k$ 之间（即夹在两个趋于同一极限的序列之间），$a_{n_k}$ 也收敛到这个数。$\square$
> > 
> > > <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Colding 在课上用一幅「动态图」讲这个夹逼结构：$b_k$ 从左向右移动（递增），$c_k$ 从右向左移动（递减），子列的点被夹在中间，随着 $k$ 增大两侧像钳子一样合拢，最终把子列「逼」到同一个极限上。🎥 *Colding 在视频中描述:* "the b's are always moving in this direction... And the ck's are moving to the left... they're coming together like this."（翻译：$b$ 序列一直往这个方向移动……$c_k$ 向左移动……它们像这样合拢。）
> > > 
> > > 注意证明的**双层结构**：先证 $a_{n_k}$ 是 Cauchy 序列（这是「够用」的），再用夹逼证它收敛到 $b_k$、$c_k$ 的共同极限（这是「更强的结论」——我们甚至知道了极限是多少的构造方式）。讲义把两步都写出来，因为夹逼这一步展示了分析学的经典套路：**要证明一个难搞的序列收敛，就找两个好搞的序列把它夹住**——这个「夹逼法」在 L05 已经出现过（squeeze 论证），在后面求各种极限时会反复用到。
> > > 
> > > 还有一个值得注意的细节：$b_k$、$c_k$ 本身并不需要是 $a_n$ 的子列——它们只是「区间端点」构成的辅助序列。这提示了一个一般方法：**证明时不要只盯着原序列，可以主动构造辅助序列来「夹」它。**
> > 
> > > <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 回顾整个 B-W 定理的证明，你会发现一个比定理本身更深刻的模式：**在 ℝ 中，「有界」和「存在收敛子列」在闭区间上是等价的。** 换句话说，B-W 定理实际上刻画了闭有界区间 $[a,b]$ 的一个深层性质——任何无穷点集在它里面都「无处可逃」，必然在某处堆积。这个性质在更高级的框架里叫 **sequential compactness（序列紧致性）**：一个集合是序列紧致的，当且仅当其中每个序列都有收敛到该集合内某点的子列。B-W 定理说「ℝ 中的闭有界区间是序列紧致的」——这是 ℝ 区别于 ℚ（有理数集）的关键特征之一：你可以构造一个有理数序列（比如十进制逼近 $\sqrt{2}$ 的序列 $1, 1.4, 1.41, 1.414, \ldots$），它在 ℝ 中收敛到无理数 $\sqrt{2}$，因此在 ℚ 内**没有任何**收敛子列。L14 会把这个概念推广到一般的 metric space（度量空间），届时「闭 + 有界」不再自动蕴含紧致性——你会在那里看到，恰好是 ℝ 的完备性（Cauchy 序列必收敛）让 B-W 定理成立。现在你不需要知道度量空间是什么，只需要记住一个心态模型：**B-W 定理 = ℝ 中「有限空间装不下无穷多个彼此远离的点」的形式化**——这个直觉在后面讨论连续函数在闭区间上的性质（最大值定理、一致连续性）时会反复兑现，那些证明几乎全是以 B-W 定理为发动机的。es）

回答了关于单调子序列存在性的问题后，我们现在也可以回答关于收敛子序列存在性的问题。乍看这似乎只是一个有趣的追问，但它将为我们提供分析学中最重要的工具之一。

<span style="color:#2471a3;">**[theorem]**</span> **Theorem 2.40（Bolzano–Weierstrass 定理）.**
每一个 bounded sequence（有界序列）都有一个 convergent subsequence（收敛子序列）。

> <span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.* 由 Theorem 2.39b 知，每个序列都有单调子序列。对于有界序列，该单调子序列既有界又单调，因此由 monotone convergence theorem（单调收敛定理****）可知它收敛。$\blacksquare$

该定理由两位 19 世纪的重要数学家——Karl Theodor Wilhelm Weierstrass（卡尔·魏尔斯特拉斯，1815–1897）和 Bernard Bolzano（伯纳德·波尔查诺，1781–1848）提出，前者是德国人，后者是捷克人，他们与 Cauchy 并列为我们学科的奠基人之一。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> **Bolzano–Weierstrass 定理**的历史颇具戏剧性。该定理最早由捷克数学家 Bernard Bolzano（伯纳德·波尔查诺，1781–1848）在其 1817 年的论文中提出并证明（作为介值定理证明的引理），但他的工作在生前未获广泛认可。约 50 年后，德国数学家 Karl Weierstrass（卡尔·魏尔斯特拉斯，1815–1897）在柏林大学的讲座中重新发现并推广了这一结果，使其成为分析标准课程的一部分。该定理的证明方式不止一种：除了上述基于峰点论证的方法，还可以通过 nested interval property（区间套性质）来证明（见习题 2.11.25）。

<span style="color:#2471a3;">**[exercise]**</span> **Exercises（习题）**

**2.11.1** 证明每个序列都是自身的子序列。想排除这种情况，该如何修改定义？

**2.11.2** 证明子序列的子序列仍是原序列的子序列。

**2.11.3** 如果 $\{s_{n_k}\}$ 是 $\{s_n\}$ 的子序列，$\{t_{m_k}\}$ 是 $\{t_n\}$ 的子序列，那么 $\{s_{n_k} + t_{m_k}\}$ 是否是 $\{s_n + t_n\}$ 的子序列？

**2.11.4** 如果 $\{s_{n_k}\}$ 是 $\{s_n\}$ 的子序列，那么 $\{(s_{n_k})^2\}$ 是否是 $\{(s_n)^2\}$ 的子序列？

**2.11.5** 描述只有有限多个不同子序列的序列。

**2.11.6** 判断以下各陈述的真伪：
(a) 若序列 $\{s_n\}$ 的所有子序列都收敛，则 $\{s_n\}$ 收敛。
(b) 若序列 $\{s_n\}$ 的所有子序列都有界，则 $\{s_n\}$ 有界。
(c) 若序列 $\{s_n\}$ 的所有子序列都单调，则 $\{s_n\}$ 单调。
(d) 若 $\{s_n\}$ 发散，则它包含两个收敛到不同极限的子序列。

**2.11.7** 判断以下各陈述的真伪：
(a) 若序列 $\{s_n\}$ 的所有 monotone subsequences（单调子序列）都 convergent（收敛），则 $\{s_n\}$ 是 bounded（有界）的。
(b) 若序列 $\{s_n\}$ 的所有单调子序列都收敛，则 $\{s_n\}$ 是收敛的。
(c) 若序列 $\{s_n\}$ 的所有收敛子序列都收敛到 $0$，则 $\{s_n\}$ 收敛到 $0$。
(d) 若序列 $\{s_n\}$ 的所有收敛子序列都收敛到 $0$ 且 $\{s_n\}$ 有界，则 $\{s_n\}$ 收敛到 $0$。

**2.11.8** 尽可能找出以下各序列的 monotonic（单调）子序列和 convergent（收敛）子序列：
(a) $\{(-1)^n n\}$
(b) $\{\sin (n\pi/8)\}$
(c) $\{n \sin (n\pi/8)\}$
(d) $\left\{\dfrac{n+1}{n} \sin (n\pi/8)\right\}$
(e) $\{1 + (-1)^n\}$
(f) $\{r_n\}$，其中 $\{r_n\}$ 由区间 $(0,1)$ 中的所有 rational numbers（有理数）按某种顺序排列而成。

**2.11.9** 描述序列

```math
1,\,0,\,1,\,0,\,1,\,0,\,1,\,0,\,1,\,0,\,1,\,0,\ldots
```

的所有子序列。描述所有收敛子序列。描述所有单调子序列。

**2.11.10** 若 $\{s_{n_k}\}$ 是 $\{s_n\}$ 的一个子序列，证明对所有 $k = 1, 2, 3, \ldots$ 有 $n_k \ge k$。

**2.11.11** 给出一个序列的例子，该序列包含收敛到每一个 natural number（自然数）的子序列（且没有其他收敛值）。

**2.11.12** 给出一个序列的例子，该序列包含收敛到 $[0,1]$ 中每一个数的子序列（且没有其他收敛值）。

**2.11.13** 证明不存在这样的序列：它包含收敛到 $(0,1)$ 中每一个数的子序列，且没有其他收敛值。
<span style="color:#7f8c8d">SEE NOTE 24</span>

**2.11.14** 证明：若 $\{s_n\}$ 没有收敛子序列，则 $|s_n| \to \infty$（当 $n \to \infty$）。

**2.11.15** 若序列 $\{x_n\}$ 满足 $\displaystyle\lim_{n\to\infty} x_{2n} = \lim_{n\to\infty} x_{2n+1} = L$，证明序列 $\{x_n\}$ 收敛到 $L$。

**2.11.16** 若序列 $\{x_n\}$ 满足 $\displaystyle\lim_{n\to\infty} x_{2n} = \lim_{n\to\infty} x_{2n+1} = \infty$，证明序列 $\{x_n\}$ 发散到 $\infty$。

**2.11.17** 设 $\alpha$ 和 $\beta$ 为正实数，定义序列 $s_1 = \alpha$，$s_2 = \beta$，且对 $n = 1, 2, 3, \ldots$ 有 $s_{n+2} = \frac12(s_n + s_{n+1})$。证明子序列 $\{s_{2n}\}$ 和 $\{s_{2n-1}\}$ 是单调且收敛的。序列 $\{s_n\}$ 是否收敛？收敛到什么值？

**2.11.18** 不借助本节中的任何理论，证明每个 unbounded sequence（无界序列）都有一个 strictly monotonic（严格单调）的子序列（即递增或递减）。

**2.11.19** 证明：若序列 $\{x_n\}$ 收敛到一个有限极限或发散到 $\pm\infty$，则每个子序列的行为完全相同。

**2.11.20** 假设序列 $\{x_n\}$ 具有以下性质：每个子序列都有一个进一步子序列收敛到 $L$。证明 $\{x_n\}$ 收敛到 $L$。

**2.11.21** 设 $\{x_n\}$ 是一个有界序列，令 $x = \sup\{x_n : n \in \mathbb{N}\}$。此外，假设对所有 $n$ 有 $x_n < x$。证明存在一个子序列收敛到 $x$。

**2.11.22** 设 $\{x_n\}$ 是一个有界序列，令

```math
y = \inf\{x_n : n \in \mathbb{N}\}\quad\text{和}\quad x = \sup\{x_n : n \in \mathbb{N}\}.
```

此外，假设对所有 $n$ 有 $y < x_n < x$。证明存在一对收敛子序列 $\{x_{n_k}\}$ 和 $\{x_{m_k}\}$，使得

```math
\lim_{k\to\infty} |x_{n_k} - x_{m_k}| = x - y.
```

**2.11.23** 每个 divergent sequence（发散序列）是否都包含一个发散的单调子序列？

**2.11.24** 每个发散序列是否都包含一个发散的有界子序列？

**2.11.25** 利用 nested interval property（区间套性质）且不依赖于单调子序列的存在性，构造一个关于有界序列的 Bolzano–Weierstrass 定理的证明。

**2.11.26** 直接证明以下断言：每个 convergent sequence（收敛序列）都有一个收敛的单调子序列（即不借助 Theorem 2.39b）。

**2.11.27** 设 $\{x_n\}$ 是一个我们不知道是否收敛的有界序列。假设它满足：它的每一个收敛子序列都收敛到同一个数 $L$。你能得出什么结论？

**2.11.28** 设 $\{x_n\}$ 是一个发散的有界序列。证明存在一对收敛子序列 $\{x_{n_k}\}$ 和 $\{x_{m_k}\}$，使得

```math
\lim_{k\to\infty} |x_{n_k} - x_{m_k}| > 0.
```

**2.11.29** 设 $\{x_n\}$ 是一个序列。满足以下性质的数 $z$ 被称为该序列的一个 **cluster point（聚点）**：对任意 $\varepsilon > 0$，区间 $(z-\varepsilon, z+\varepsilon)$ 中包含序列的无穷多项。证明 $z$ 是序列的一个聚点当且仅当存在一个子序列 $\{x_{n_k}\}$ 收敛到 $z$。
<span style="color:#2471a3;">**[section]**</span> **2.12 Cauchy Convergence Criterion（柯西收敛准则）**

序列的什么性质刻画了 convergence（收敛）？作为一个"characterization（刻画）"，我们想要一个序列收敛的某种 necessary and sufficient condition（充要条件）。我们可以直接写下定义并将其视为一种刻画。因此，以下技术性陈述确实可以说是序列 $\{s_n\}$ 收敛的一种刻画：

> 序列 $\{s_n\}$ 收敛当且仅当存在 $L$ 使得对任意 $\varepsilon > 0$ 存在 $N$，满足当 $n \ge N$ 时 $|s_n - L| < \varepsilon$。

在数学中，当我们要求对某个性质进行刻画时，可以预期会有许多答案，有些比其他的更有用。这种特定刻画的局限性在于，它要求我们预先知道作为序列极限的数 $L$。将其与单调序列 $\{s_n\}$ 的收敛性刻画进行比较：

> 单调序列 $\{s_n\}$ 收敛当且仅当它是有界的。

这是一个精彩且最有用的刻画。但它只适用于 monotonic sequences（单调序列）。

一个适用于所有序列的正确且有 useful characterization（有用刻画）是由 Cauchy（柯西）发现的。这就是下一个定理的内容。注意它的优点在于，它在描述收敛序列时完全不涉及极限的实际值。粗略地说，它断言：一个序列收敛当且仅当该序列的项最终可以任意地接近彼此。

<span style="color:#2471a3;">**[theorem]**</span> **Theorem 2.41（Cauchy Criterion，柯西准则）.**
序列 $\{s_n\}$ 收敛当且仅当对每个 $\varepsilon > 0$ 存在一个整数 $N$，满足当 $n \ge N$ 且 $m \ge N$ 时 $|s_n - s_m| < \varepsilon$。

> <span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.* 定理中的这个性质非常重要，值得给它一些 terminology（术语）。如果一个序列满足此性质，则称其为 **Cauchy sequence（柯西序列）**。于是定理断言：一个序列收敛当且仅当它是一个柯西序列。这个术语在更高级的情境中最为重要，在那里，是柯西序列并不一定等价于收敛。
> 
> 我们的证明稍显冗长，需要应用 Bolzano–Weierstrass 定理。
> 
> 然而，一个方向的证明是容易的。假设 $\{s_n\}$ 收敛到某个数 $L$。设 $\varepsilon > 0$。则存在整数 $N$ 使得当 $k \ge N$ 时 $|s_k - L| < \varepsilon/2$。因此，若 $m$ 和 $n$ 都大于 $N$，
> 
> ```math
> |s_n - s_m| \le |s_n - L| + |L - s_m| < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon,
> ```
> 
> 这表明 $\{s_n\}$ 是一个 Cauchy sequence（柯西序列）。
> 
> 现在我们来证明相反（且更困难）的方向。
> 
> 第一步，我们证明每个 Cauchy sequence 都是有界的。由于此证明可以通过复制和修改 Theorem 2.11 的证明来得到，我们将其留作练习。（柯西序列有界这个事实其实并不那么有趣，因为当证明完成后，我们知道所有柯西序列都收敛，因而必然是有界的。）
> 
> 第二步，我们将 Bolzano–Weierstrass 定理应用于有界序列 $\{s_n\}$，得到一个收敛子序列 $\{s_{n_k}\}$。
> 
> 最后一步是 Cauchy sequences 的一个特性。一旦我们知道 $s_{n_k} \to L$ 且 $\{s_n\}$ 是柯西序列，我们就可以证明 $s_n \to L$ 也成立。设 $\varepsilon > 0$，选取 $N$ 使得对所有 $m, n \ge N$ 有 $|s_n - s_m| < \varepsilon/2$。选取 $K$ 使得对所有 $k \ge K$ 有 $|s_{n_k} - L| < \varepsilon/2$。假设 $n \ge N$。将 $m$ 取为某个大于 $N$ 且满足 $k \ge K$ 的 $n_k$ 值。对于这个值 $s_m = s_{n_k}$，我们有
> 
> ```math
> |s_n - L| \le |s_n - s_{n_k}| + |s_{n_k} - L| < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.
> ```
> 
> 由定义，$\{s_n\}$ 收敛到 $L$，证明完成。∎

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> **Cauchy 收敛准则（Cauchy Criterion）**由法国数学家 Augustin-Louis Cauchy（奥古斯丁-路易·柯西，1789–1857）在其 1821 年的经典著作《Cours d'Analyse》中提出。该准则的伟大之处在于：它给出了序列收敛的一个**内蕴刻画**——只需考察序列自身项之间的接近程度，而无需事先知道极限值 $L$。这在泛函分析和完备空间理论中尤为重要：一个度量空间称为**完备的**，当且仅当其中的每个 Cauchy 序列都收敛。实数系 $\mathbb{R}$ 的完备性正是 Cauchy 准则成立的根本原因。该准则的证明依赖于 Bolzano–Weierstrass 定理（或与之等价的实数完备性公理），这体现了实分析基本定理之间的深刻联系。

<span style="color:#2471a3;">**[example]**</span> **Example 2.42.**
Cauchy criterion（柯西准则）在理论发展中最为有用，而不是用于具体的例子中。即便如此，有时它是证明收敛的最快途径。例如，考虑由 $x_1 = 1$，$x_2 = 2$ 递归定义的序列 $\{x_n\}$：

```math
x_n = \frac{x_{n-1} + x_{n-2}}{2}.
```

从第二项之后，每一项都是前两项的 average（平均值）。$x_1$ 和 $x_2$ 之间的距离是 $1$，$x_2$ 和 $x_3$ 之间的距离是 $1/2$，$x_3$ 和 $x_4$ 之间的距离是 $1/4$，依此类推。因此我们看到，在 $N$ 阶段之后，所有距离都小于 $2^{-N+1}$，也就是说，对所有 $n \ge N$ 和 $m \ge N$，

```math
|x_n - x_m| \le \frac{1}{2^{N-1}}.
```

这正是 Cauchy criterion（柯西准则），因此这个序列收敛。注意柯西准则并未提供该序列收敛到什么值的信息。你需要用另一种方法去发现它。

---

<span style="color:#2471a3;">**[exercise]**</span> **Exercises（习题）**

**2.12.1** 直接证明序列 $s_n = 1/n$ 是一个 Cauchy sequence（柯西序列）。

**2.12.2** 直接证明 Cauchy 序列的任意倍数仍然是 Cauchy 序列。

**2.12.3** 直接证明两个 Cauchy 序列的和仍然是 Cauchy 序列。

**2.12.4** 直接证明每个 Cauchy 序列都是有界的。

**2.12.5** 下列准则比 Cauchy criterion（柯西准则）更弱。证明它不等价：

> 对每个 $\varepsilon > 0$，存在 $N$ 使得当 $n \ge N$ 时 $|s_{n+1} - s_n| < \varepsilon$。
> 
> 考虑序列 $s_n = 1 + 1/2 + 1/3 + \cdots + 1/n$。
> <span style="color:#7f8c8d">SEE NOTE 25</span>

**2.12.6** 一个粗心的学生认为以下陈述就是 Cauchy criterion（柯西准则）：

> 对每个 $\varepsilon > 0$，存在 $N$ 使得当 $n \ge N$ 时 $|s_n - s_{n+1}| < \varepsilon$。

这个陈述是 weaker（更弱）、stronger（更强）还是 equivalent（等价）于 Cauchy criterion（柯西准则）？

**2.12.7** 直接证明若 $\{s_n\}$ 是 Cauchy sequence（柯西序列），则 $\{|s_n|\}$ 也是 Cauchy 序列。由此推出只要 $\{s_n\}$ 收敛，$\{|s_n|\}$ 就收敛。

**2.12.8** 证明：$\{s_n\}$ 是 Cauchy sequence（柯西序列）当且仅当它的每一个 subsequence（子序列）都是 Cauchy 序列。

**2.12.9** 证明每个 bounded monotonic sequence（有界单调序列）都是 Cauchy 序列。（不要使用 monotone convergence theorem（单调收敛定理）或任何与之等价的结果。）

**2.12.10** 证明 Example 2.42 中的序列收敛到 $5/3$。
<span style="color:#7f8c8d">SEE NOTE 26</span>
<span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b;">2.13 Upper and Lower Limits（上极限与下极限）</span>

<span style="color:#7f8c8d">*本节为进阶内容，初学时可以跳过。*</span>

如果原序列 $\{x_n\}$ 收敛到 $L$，那么我们当然有

```math
\limsup_{n\to\infty} x_n = \liminf_{n\to\infty} x_n = L.
```

但若不收敛，这两个量可能会有所不同，而这个差异可以在某些情形下替代极限的概念。

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b;">Example 2.43（例 2.43）</span>
设 $\{x_n\}$ 为正数序列。为证明 $x_n \to 0$，只需证明 $\displaystyle\limsup_{n\to\infty} x_n = 0$。
事实上，若 $\limsup x_n = 0$，则对任意 $\varepsilon > 0$，存在 $N$ 使得 $\sup\{x_k : k \ge N\} < \varepsilon$，
从而对所有 $n \ge N$ 有 $0 < x_n < \varepsilon$，故 $x_n \to 0$。这里我们只需处理序列的"一半"——上极限——即可得出结论。$\blacksquare$

> <span style="color:#1e8449;">**[note] Note（注）.**</span> 这个例子表明，极限的定义可以被"弱化"为仅需处理不等式的一侧。这对某些应用更为便捷。

<span style="color:#2471a3;">**[definition]**</span> **Definition 2.44: (Upper Limit / Limit Superior, 上极限).**
设 $\{x_n\}$ 为一个实数序列。定义

```math
\limsup_{n\to\infty} x_n = \inf\{\beta : 存在 N 使得对所有 n \ge N 有 x_n < \beta\}.
```

换句话说，$\limsup x_n$ 是序列最终不再超过的"最小界限"。

<span style="color:#2471a3;">**[definition]**</span> **Definition 2.45: (Lower Limit / Limit Inferior, 下极限).**
设 $\{x_n\}$ 为一个实数序列。定义

```math
\liminf_{n\to\infty} x_n = \sup\{\alpha : 存在 N 使得对所有 n \ge N 有 x_n > \alpha\}.
```

即 $\liminf x_n$ 是序列最终始终高于的"最大界限"。

> <span style="color:#1e8449;">**[note] Note（注）.**</span> 有些教科书采用另一种等价定义：$\limsup x_n = \lim_{n\to\infty} \sup\{x_k : k \ge n\}$，$\liminf x_n = \lim_{n\to\infty} \inf\{x_k : k \ge n\}$。两者完全等价（见定理 2.47）。使用哪种定义取决于具体问题的便利性。

上述定义中的一个微妙之处在于：当我们考虑 $\limsup x_n$ 时，集合 $\{\beta : 存在 N 使得对所有 n \ge N 有 x_n < \beta\}$ 可能为空（例如序列 $x_n = n$）。此时 $\limsup x_n = \infty$。类似地，若 $\liminf x_n$ 的定义中的集合为空，则 $\liminf x_n = -\infty$。此外，若 $\limsup x_n = -\infty$，则意味着对任意 $\beta$，序列最终都小于 $\beta$，这要求 $x_n \to -\infty$；反之，若 $\liminf x_n = \infty$，则 $x_n \to \infty$。这些情形在 extended real numbers（广义实数）的框架下是一致的。

<span style="color:#2471a3;">**[theorem]**</span> **Theorem 2.46（$\liminf \le \limsup$）.**
对任意序列 $\{x_n\}$，有

```math
\liminf_{n\to\infty} x_n \le \limsup_{n\to\infty} x_n.
```

> <span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.* 设 $\alpha < \liminf x_n$。则存在 $N$ 使得对所有 $n \ge N$ 有 $x_n > \alpha$。因此，对任意 $\beta < \alpha$，当 $n \ge N$ 时不可能有 $x_n < \beta$。这意味着 $\limsup x_n \ge \alpha$。由于这对所有 $\alpha < \liminf x_n$ 成立，取上确界即得 $\liminf x_n \le \limsup x_n$。$\blacksquare$

<span style="color:#2471a3;">**[theorem]**</span> **Theorem 2.47（上极限的尾端 sup 刻画）.**
对任意序列 $\{x_n\}$，有

```math
\limsup_{n\to\infty} x_n = \lim_{n\to\infty} \sup\{x_k : k \ge n\}.
```

> <span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.* 设 $L = \limsup x_n$（依定义 2.44）。记 $u_n = \sup\{x_k : k \ge n\}$。则 $\{u_n\}$ 递减。令 $U = \lim_{n\to\infty} u_n$（作为广义实数）。
> 
> 先证 $U \le L$。取任意 $\beta > L$。由定义 2.44，存在 $N$ 使得对所有 $n \ge N$ 有 $x_n < \beta$。从而对所有 $n \ge N$ 有 $u_n \le \beta$。由于 $\{u_n\}$ 递减，$U \le \beta$。这对所有 $\beta > L$ 成立，故 $U \le L$。
> 
> 再证 $L \le U$。取任意 $\gamma < L$。则对任意 $N$，存在 $n \ge N$ 使得 $x_n \ge \gamma$（否则 $\gamma$ 将成为定义 2.44 中的上界，与 $\gamma < L$ 矛盾）。因此，对所有 $N$ 有 $u_N \ge \gamma$，从而 $U \ge \gamma$。这对所有 $\gamma < L$ 成立，故 $U \ge L$。综合得 $U = L$。$\blacksquare$

类似地，$\displaystyle\liminf_{n\to\infty} x_n = \lim_{n\to\infty} \inf\{x_k : k \ge n\}$。

<span style="color:#2471a3;">**[theorem]**</span> **Theorem 2.48（极限存在与上下极限的关系）.**
序列 $\{x_n\}$ 收敛（到某个有限极限 $L$）当且仅当

```math
\liminf_{n\to\infty} x_n = \limsup_{n\to\infty} x_n = L.
```

更一般地，$\liminf x_n \le \limsup x_n$，且等号成立当且仅当序列收敛（允许极限为 $\pm\infty$）。

> <span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.* 设 $L = \liminf x_n = \limsup x_n$。对任意 $\varepsilon > 0$，由定义 2.44 和 2.45 可得，存在 $N$ 使得对所有 $n \ge N$ 有 $L - \varepsilon < x_n < L + \varepsilon$，故 $|x_n - L| < \varepsilon$，即 $x_n \to L$。
> 
> 反之，若 $x_n \to L$，则对任意 $\varepsilon > 0$，存在 $N$ 使得当 $n \ge N$ 时有 $|x_n - L| < \varepsilon$。于是 $\limsup x_n \le L + \varepsilon$ 且 $\liminf x_n \ge L - \varepsilon$。由于 $\varepsilon$ 是任意的，$\liminf x_n = \limsup x_n = L$。$\blacksquare$

在练习中，你将被要求计算一些 $\limsup$ 和 $\liminf$。这只是为了熟悉这些概念。计算本身并不那么重要。重要的是这些概念在理论发展中的使用。更关键的是这些极限运算如何与算术或序性质相关联。和的极限等于两个极限之和。这对 $\limsup$ 和 $\liminf$ 是否成立？（见习题 2.13.9。）不要跳过这些练习。
<span style="color:#2471a3;">**[exercise]**</span> **Exercises（习题）**

**2.13.1** 完成 Example 2.43，证明：若 $\{x_n\}$ 是正数序列，且满足 $\displaystyle\limsup_{n\to\infty} \sqrt[n]{x_n} < 1$，则 $x_n \to 0$。证明：若 $\displaystyle\liminf_{n\to\infty} \sqrt[n]{x_n} > 1$，则 $x_n \to \infty$。若 $\displaystyle\limsup_{n\to\infty} \sqrt[n]{x_n} > 1$，你能得出什么结论？若 $\displaystyle\liminf_{n\to\infty} \sqrt[n]{x_n} < 1$，你能得出什么结论？

**2.13.2** 计算以下各序列的 $\limsup$ 和 $\liminf$：
(a) $\{(-1)^n n\}$
(b) $\{\sin (n\pi/8)\}$
(c) $\{n \sin (n\pi/8)\}$
(d) $\{[(n+1) \sin (n\pi/8)]/n\}$
(e) $\{1 + (-1)^n\}$
(f) $\{r_n\}$，其中 $r_n$ 由区间 $(0,1)$ 中的所有 rational numbers（有理数）按某种顺序排列而成。

**2.13.3** 给出有理数序列 $\{a_n\}$ 的例子，使其满足：
(a) upper limit（上极限）为 $\sqrt{2}$，lower limit（下极限）为 $-\sqrt{2}$，
(b) upper limit 为 $+\infty$，lower limit 为 $\sqrt{2}$，
(c) upper limit 为 $\pi$，lower limit 为 $e$。

**2.13.4** 证明 $\displaystyle\limsup_{n\to\infty} (-x_n) = -(\liminf_{n\to\infty} x_n)$。

**2.13.5** 若两个序列 $\{a_n\}$ 和 $\{b_n\}$ 对所有足够大的 $n$ 满足 $a_n \le b_n$，证明：

```math
\limsup_{n\to\infty} a_n \le \limsup_{n\to\infty} b_n \quad\text{且}\quad \liminf_{n\to\infty} a_n \le \liminf_{n\to\infty} b_n.
```

**2.13.6** 证明 $\displaystyle\lim_{n\to\infty} x_n = \infty$ 当且仅当

```math
\limsup_{n\to\infty} x_n = \liminf_{n\to\infty} x_n = \infty.
```

**2.13.7** 证明：若 $\displaystyle\limsup_{n\to\infty} a_n = L$（$L$ 为有限实数）且 $\varepsilon > 0$，则 $a_n > L + \varepsilon$ 只对有限多个 $n$ 成立，而 $a_n > L - \varepsilon$ 对无限多个 $n$ 成立。

**2.13.8** 证明：对任意 monotonic sequence（单调序列）$\{x_n\}$，

```math
\limsup_{n\to\infty} x_n = \liminf_{n\to\infty} x_n = \lim_{n\to\infty} x_n
```

（包含无穷极限的可能性）。

**2.13.9** 证明：对任意有界序列 $\{a_n\}$ 和 $\{b_n\}$，

```math
\limsup_{n\to\infty} (a_n + b_n) \le \limsup_{n\to\infty} a_n + \limsup_{n\to\infty} b_n.
```

给出一个例子说明等号不一定成立。

**2.13.10** 习题 2.13.9 关于 $\liminf$ 的正确版本是什么？

**2.13.11** 证明：对任意有界的正数序列 $\{a_n\}$ 和 $\{b_n\}$，

```math
\limsup_{n\to\infty} (a_n b_n) \le (\limsup_{n\to\infty} a_n)(\limsup_{n\to\infty} b_n).
```

给出一个例子说明等号不一定成立。

**2.13.12** 通过将论证中的 $\lim$ 替换为 $\limsup$ 和 $\liminf$，修正习题 2.8.3 中不严谨的学生证明（关于 squeeze theorem（夹逼定理））。

**2.13.13** 对于一个序列 $\{a_n\}$ 及其一个子序列 $\{a_{n_k}\}$，你能陈述 $\limsup$ 和 $\liminf$ 之间的什么关系（如果存在的话）？

**2.13.14** 如果一个序列 $\{a_n\}$ 没有收敛子序列，你对该序列的 $\limsup$ 和 $\liminf$ 能得出什么结论？

**2.13.15** 设 $S$ 表示所有具有以下性质的实数 $t$ 的集合：给定序列 $\{a_n\}$ 的某个子序列收敛到 $t$。集合 $S$ 与序列 $\{a_n\}$ 的 $\limsup$ 和 $\liminf$ 之间有什么关系？
<span style="color:#7f8c8d">SEE NOTE 27</span>

**2.13.16** 证明以下关于正实数序列 $\{a_n\}$ 的上极限和下极限的断言：

```math
\liminf_{n\to\infty} \frac{a_{n+1}}{a_n} \le \liminf_{n\to\infty} \sqrt[n]{a_n} \le \limsup_{n\to\infty} \sqrt[n]{a_n} \le \limsup_{n\to\infty} \frac{a_{n+1}}{a_n}.
```

给出一个例子说明这些不等式中的每一个都可能是严格的。

**2.13.17** 对任意序列 $\{a_n\}$，记 $s_n = (a_1 + a_2 + \cdots + a_n)/n$。证明：

```math
\liminf_{n\to\infty} a_n \le \liminf_{n\to\infty} s_n \le \limsup_{n\to\infty} s_n \le \limsup_{n\to\infty} a_n.
```

给出一个例子说明这些不等式中的每一个都可能是严格的。

---

<span style="color:#7f8c8d">*§2.11–§2.13 行内双语翻译完成。*</span>

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b;">2.14 Challenging Problems for Chapter 2（第 2 章挑战题）</span>

<span style="color:#2471a3;">**[section]**</span> **2.14.3**

设 $a_1 = 1$ 并递归定义一个 sequence（序列）：

```math
a_{n+1} = \sqrt{a_1 + a_2 + \cdots + a_n}.
```

证明 $\displaystyle\lim_{n\to\infty} \frac{a_n}{n} = 1/2$。

---

<span style="color:#2471a3;">**[section]**</span> **2.14.4**

设 $x_1 = \theta$ 并递归定义一个 sequence（序列）：

```math
x_{n+1} = \frac{x_n}{1 + x_n / 2}.
```

对于哪些 $\theta$ 值有 $x_n \to 0$？

---

<span style="color:#2471a3;">**[section]**</span> **2.14.5**

设 $\{a_n\}$ 是区间 $(0, 1)$ 中的一个 sequence of numbers（数列），满足性质：

```math
a_n < \frac{a_{n-1} + a_{n+1}}{2}
```

对所有 $n = 2, 3, 4, \ldots$ 成立。证明该 sequence（序列）是 convergent（收敛的）。

---

<span style="color:#2471a3;">**[section]**</span> **2.14.6**

对任意 convergent sequence（收敛序列）$\{a_n\}$，定义

```math
s_n = \sqrt[n]{a_1 a_2 \ldots a_n},
```

即 geometric averages（几何平均）的 sequence（序列）。证明 $\displaystyle\lim_{n\to\infty} a_n = \lim_{n\to\infty} s_n$。给出一个例子说明 $\{s_n\}$ 可能在 $\{a_n\}$ 发散时仍收敛。

---

<span style="color:#2471a3;">**[section]**</span> **2.14.7**

如果

```math
\lim_{n\to\infty} \frac{s_n - \alpha}{s_n + \alpha} = 0,
```

你能得出关于 sequence $\{s_n\}$ 的什么结论？

---

<span style="color:#2471a3;">**[section]**</span> **2.14.8**

一个 function（函数）$f$ 定义为

```math
f(x) = \lim_{n\to\infty} \frac{1}{x^n + x^{-n}}
```

对每个使得该 limit（极限）存在的 $x$ 值。该 function（函数）的 domain（定义域）是什么？

---

<span style="color:#2471a3;">**[section]**</span> **2.14.9**

一个 function（函数）$f$ 定义为

```math
f(x) = \lim_{n\to\infty} \left(\frac{1 - x^2}{1 + x^2}\right)^n
```

对每个使得该 limit（极限）存在的 $x$ 值。该 function（函数）的 domain（定义域）是什么？

---

<span style="color:#2471a3;">**[section]**</span> **2.14.10**

假设 $f : \mathbb{R} \to \mathbb{R}$ 是一个 positive function（正函数），其 derivative（导数）$f'$ 处处连续且为负。应用 Newton's method（牛顿法）得到 sequence（序列）：

```math
x_1 = \theta, \quad x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}.
```

证明对于任何起始值 $\theta$，有 $x_n \to \infty$。[本题假设读者有微积分基础。]

---

<span style="color:#2471a3;">**[section]**</span> **2.14.11**

设 $f(x) = x^3 - 3x + 3$。应用 Newton's method（牛顿法）得到 sequence（序列）：

```math
x_1 = \theta, \quad x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}.
```

证明对于任意正整数 $p$，存在一个起始值 $\theta$ 使得该 sequence（序列）$\{x_n\}$ 是 periodic with period $p$（周期为 $p$ 的周期序列）。

<span style="color:#2471a3;">**[详见 NOTE 28]**</span>

---

<span style="color:#2471a3;">**[section]**</span> **2.14.12**

确定 sequence $x_n = \cos n$ 的所有 subsequential limit points（子序列极限点）。

<span style="color:#2471a3;">**[详见 NOTE 29]**</span>

---

<span style="color:#2471a3;">**[section]**</span> **2.14.13**

一个 sequence $\{s_n\}$ 被称为 contractive（压缩的），如果存在一个正数 $0 < r < 1$ 使得

```math
|s_{n+1} - s_n| \le r |s_n - s_{n-1}|
```

对所有 $n = 2, 3, 4, \ldots$ 成立。

(a) 证明由 $s_1 = 1$ 和 $s_n = (4 + s_{n-1})^{-1}$（$n = 2, 3, \ldots$）定义的 sequence（序列）是 contractive（压缩的）。

(b) 证明每一个 contractive sequence（压缩序列）都是 Cauchy（柯西序列）。

(c) 证明一个 sequence（序列）可以满足条件

```math
|s_{n+1} - s_n| < |s_n - s_{n-1}|
```

对所有 $n = 2, 3, 4, \ldots$ 成立，却不是 contractive（压缩的），甚至不 convergent（收敛）。

(d) 是否每一个 convergent sequence（收敛序列）都是 contractive（压缩的）？

<span style="color:#2471a3;">**[详见 NOTE 30]**</span>

---

<span style="color:#2471a3;">**[section]**</span> **2.14.14**

递归定义的 sequence（序列）

```math
f_1 = 1,\quad f_2 = 1,\quad f_{n+2} = f_n + f_{n+1}
```

称为 Fibonacci sequence（斐波那契数列）。设

```math
r_n = f_{n+1} / f_n
```

为 Fibonacci sequence（斐波那契数列）连续项之比的 sequence（序列）。

(a) 证明 $r_1 < r_3 < r_5 < \cdots < r_6 < r_4 < r_2$。

(b) 证明 $r_{2n} - r_{2n-1} \to 0$。

(c) 推断 sequence $\{r_n\}$ 是 convergent（收敛的）。你能找到确定该 limit（极限）的方法吗？（这与方程 $x^2 - x - 1 = 0$ 的根有关。）

---

<span style="color:#2471a3;">**[section]**</span> **2.14.15**

一个实数 sequence（序列）$\{x_n\}$ 满足性质

```math
(2 - x_n)x_{n+1} = 1.
```

证明 $\displaystyle\lim_{n\to\infty} x_n = 1$。

<span style="color:#2471a3;">**[详见 NOTE 31]**</span>

---

<span style="color:#2471a3;">**[section]**</span> **2.14.16**

设 $\{a_n\}$ 是任意一个 positive real numbers（正实数）的 sequence（序列）。证明

```math
\limsup_{n\to\infty} \left(\frac{a_1 + a_{n+1}}{a_n}\right)^n \ge e.
```

<span style="color:#2471a3;">**[详见 NOTE 32]**</span>

---

<span style="color:#2471a3;">**[section]**</span> **2.14.17**

假设第 $n$ 项为 $s_n + 2s_{n+1}$ 的 sequence（序列）是 convergent（收敛的）。证明 $\{s_n\}$ 也收敛。

<span style="color:#2471a3;">**[详见 NOTE 33]**</span>

---

<span style="color:#2471a3;">**[section]**</span> **2.14.18**

证明 sequence（序列）

```math
\sqrt{7},\quad \sqrt{7 - \sqrt{7}},\quad \sqrt{7 - \sqrt{7 + \sqrt{7}}},\quad \sqrt{7 - \sqrt{7 + \sqrt{7 - \sqrt{7}}}},\quad \ldots
```

收敛并求其 limit（极限）。

<span style="color:#2471a3;">**[详见 NOTE 34]**</span>

---

<span style="color:#2471a3;">**[section]**</span> **2.14.19**

设 $a_1$ 和 $a_2$ 为正数，假设 sequence $\{a_n\}$ 递归定义为

```math
a_{n+2} = \sqrt{a_n} + \sqrt{a_{n+1}}.
```

证明该 sequence（序列）收敛并求其 limit（极限）。

<span style="color:#2471a3;">**[详见 NOTE 35]**</span>

---

#### Notes（注释）

<span style="color:#2471a3;">**[note]**</span> **9** 习题 2.2.2。对于该 sequence（序列）的下一项，有些人可能期望得到 1。大多数数学家会期望得到 9。

<span style="color:#2471a3;">**[note]**</span> **10** 习题 2.2.3。这里有一个公式能生成 sequence（序列）$0, 0, 0, 0, c, \ldots$ 的前五项：

```math
f(n) = \frac{c(n-1)(n-2)(n-3)(n-4)}{4!}.
```

<span style="color:#2471a3;">**[note]**</span> **11** 习题 2.2.10。公式为

```math
f_n = \frac{1}{\sqrt{5}} \left\{ \left(\frac{1+\sqrt{5}}{2}\right)^n - \left(\frac{1-\sqrt{5}}{2}\right)^n \right\}.
```

可用 induction（归纳法）验证。

<span style="color:#2471a3;">**[note]**</span> **12** 习题 2.3.1。找一个 one-to-one onto（一一对应）的函数 $f: (a,b) \to (0,1)$，并考虑 sequence $f(s_n)$，其中 $\{s_n\}$ 是一个声称以 $(a,b)$ 全体为值域的 sequence（序列）。

<span style="color:#2471a3;">**[note]**</span> **13** 习题 2.3.4。我们可以考虑每个集合 $S_i$ 的元素可以列出，例如

```math
S_1 = \{x_{11}, x_{12}, x_{13}, \ldots\},\quad S_2 = \{x_{21}, x_{22}, x_{23}, \ldots\},
```

依此类推。现在尝试思考一种方法列出所有这些条目，即制作一个包含它们全部的大列表。

<span style="color:#2471a3;">**[note]**</span> **14** 习题 2.3.6。我们需要 (i) 每个数都有 decimal expansion（十进制展开）；(ii) 十进制展开是唯一的，除非展开以一串 0 或一串 9 结尾 [例如 $1/2 = 0.5000000\ldots = 0.49999999\ldots$]，因此如果 $a$ 和 $b$ 是两个数，在第 $n$ 位小数上一个是 5（或 6）而另一个不是，那么要么 $a \ne b$，要么其中一个以一串 0 结尾而另一个以一串 9 结尾；(iii) 每一串由 5 和 6 组成的字符串都定义了一个具有该十进制展开的实数。

<span style="color:#2471a3;">**[note]**</span> **15** 习题 2.3.10。尝试找到一种方法，以与有理数排序相同的方式对 algebraic numbers（代数数）进行排序。

<span style="color:#2471a3;">**[note]**</span> **16** 习题 2.4.6。你需要用到恒等式 $1 + 2 + 3 + \cdots + n = n(n+1)/2$。

<span style="color:#2471a3;">**[note]**</span> **17** 习题 2.4.7。你需要找到一个与 $1 + 2 + 3 + \cdots + n = n(n+1)/2$ 类似的平方和恒等式。为建立正确的逆命题，重新表述为：如果所有 $x_n > 0$ 且 $x_{n+1}/x_n \to 1$，则 $x_n \to \infty$。证明这是正确的。习题中所述语句的逆命题是假的（例如 $x_n = 1/n$）。

<span style="color:#2471a3;">**[note]**</span> **18** 习题 2.5.6。

<span style="color:#2471a3;">**[note]**</span> **19** 习题 2.6.5。使用与 Theorem 2.11（定理 2.11）证明中相同的方法。

<span style="color:#2471a3;">**[note]**</span> **20** 习题 2.8.1。给出一个 counterexample（反例）。也许找到两个 sequences（序列）使得对所有 $n$ 有 $s_n < 0 < t_n$，但 $\lim_{n\to\infty} s_n = \lim_{n\to\infty} t_n = 0$。

<span style="color:#2471a3;">**[note]**</span> **21** 习题 2.8.9。取任意严格介于 1 和该 limit（极限）之间的数 $r$。证明存在某个 $N$，当 $n \ge N$ 时 $s_{n+1} < r s_n$。由此推出 $s_{N+2} < r^2 s_N$ 且 $s_{N+3} < r^3 s_N$。继续。

<span style="color:#2471a3;">**[note]**</span> **22** 习题 2.8.10。取任意严格介于 1 和该 limit（极限）之间的数 $r$。证明存在某个 $N$，当 $n \ge N$ 时 $s_{n+1} > r s_n$。由此推出 $s_{N+2} > r^2 s_N$ 且 $s_{N+3} > r^3 s_N$。继续。

<span style="color:#2471a3;">**[note]**</span> **23** 习题 2.10.1。按照我们的 convergence（收敛）理论，这个陈述没有意义，因为（你应该证明）该 sequence（序列）发散。即便如此，包括 Euler（欧拉）在内的许多伟大数学家也曾接受并使用过这个公式。它之所以有用，说明存在将此类陈述解释为收敛断言之外的其他方式。

<span style="color:#2471a3;">**[note]**</span> **24** 习题 2.11.13。如果一个 sequence（序列）包含收敛到 $(0,1)$ 中每个数的 subsequences（子序列），证明它也包含一个收敛到 0 的 subsequence（子序列）。

<span style="color:#2471a3;">**[note]**</span> **25** 习题 2.12.5。考虑 sequence $s_n = 1 + 1/2 + 1/3 + \cdots + 1/n$。

<span style="color:#2471a3;">**[note]**</span> **26** 习题 2.12.10。与 $1 + 1 - 1/2 + 1/4 - 1/8 + 1/6 - \cdots$ 比较，这是一个 geometric progression（等比级数）的和。

<span style="color:#2471a3;">**[note]**</span> **27** 习题 2.13.15。分别考虑 sequence（序列）有界和无界的情况。

<span style="color:#2471a3;">**[note]**</span> **28** 习题 2.14.11。一个 sequence $\{x_n\}$ 是 periodic with period $p$（周期为 $p$ 的周期序列），如果 $x_{n+p} = x_n$ 对所有 $n$ 成立且没有更小的 $p$ 值满足此性质。（注意如果 $\{x_n\}$ 是周期为 $p$ 的周期序列，则 $x_n = x_{n+p} = x_{n+2p} = x_{n+3p} = \ldots$。）

<span style="color:#2471a3;">**[note]**</span> **29** 习题 2.14.12。显然，没有大于 1 或小于 -1 的数能成为这样的 limit（极限）。证明实际上区间 $[-1, 1]$ 就是所有这样的 limit points（极限点）的集合。如果 $x \in [-1, 1]$，则必存在数 $y$ 使得 $\cos y = x$（为什么？）。现在考虑集合

```math
G = \{n + 2m\pi : n, m \in \mathbb{Z}\}.
```

利用 Exercise 1.11.6（习题 1.11.6）或其他方法证明这是 dense（稠密的）。因此存在整数对 $n, m$ 使得 $|y - n + 2m\pi| < \varepsilon$。由此推出 $|\cos y - \cos(n + 2m\pi)| < \varepsilon$，从而 $|x - \cos n| < \varepsilon$。

<span style="color:#2471a3;">**[note]**</span> **30** 习题 2.14.13。对于 (a)，证明对所有 $n = 2, 3, 4, \ldots$ 有 $|s_{n+1} - s_n| \le \frac{1}{17}|s_n - s_{n-1}|$。对于 (b)，你需要用到 geometric progression（等比级数）的和是有界的这一事实，实际上如果 $0 < r < 1$，则 $1 + r + r^2 + \cdots + r^n < (1 - r)^{-1}$。对于 $m > n$，将 $|s_m - s_n| \le |s_{n+1} - s_n| + |s_{n+2} - s_{n+1}| + \cdots + |s_m - s_{m-1}|$ 表示出来，然后使用 contractive（压缩）假设。注意 $|s_4 - s_3| \le r|s_3 - s_2| \le r^2|s_2 - s_1|$。对于 (d)，你可能需要等到学习 series（级数）时才能找到合适的 convergent but not contractive（收敛但不压缩）的序列的例子。

<span style="color:#2471a3;">**[note]**</span> **31** 习题 2.14.15。本题出自 1947 年 Putnam 数学竞赛。

<span style="color:#2471a3;">**[note]**</span> **32** 习题 2.14.16。本题出自 1949 年 Putnam 数学竞赛。

<span style="color:#2471a3;">**[note]**</span> **33** 习题 2.14.17。本题出自 1950 年 Putnam 数学竞赛。

<span style="color:#2471a3;">**[note]**</span> **34** 习题 2.14.18。本题出自 1953 年 Putnam 数学竞赛。

<span style="color:#2471a3;">**[note]**</span> **35** 习题 2.14.19。问题由 A. Emerson 在《Amer. Math. Monthly》, 85 (1978), p. 496 中提出。

---

## <span style="color:#c0392b;">Chapter 3. Infinite Sums（无穷和）</span>

> 本章关于 infinite sums（无穷和）与 series（级数）的内容在课程设计时可以跳过，或根据需要稍后学习。第 3.4 节、第 3.5 节及第 3.6 节部分的基本材料在未来需要用到，但不会早于第 9 章函数项级数的学习。所有 enrichment（拓展）或 advanced（高级）小节均可省略，后续内容不依赖它们。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b;">3.1 Introduction（引言）</span>

Infinite sums（无穷和）的使用在时间上显然远早于 sequences（序列）的研究。求和

```math
1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \frac{1}{16} + \frac{1}{32} + \frac{1}{64} + \cdots = 2
```

早已为人所知。通过算术或几何"推理"，很容易说服自己这是正确的。毕竟，只需开始逐步相加并跟踪总和：

```math
1,\; 1\frac{1}{2},\; 1\frac{3}{4},\; 1\frac{7}{8},\; 1\frac{15}{16},\; \ldots.
```

图 3.1 使这一点看起来一目了然。

但这里存在一个严重的含义问题。finite sum（有限和）是有明确定义的，infinite sum（无穷和）则不是。无论是人类还是计算机，都无法将一列无穷多个数字相加。通常赋予上述求和的含义出现在以下计算中：

```math
1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \cdots = \lim_{n\to\infty} \left(1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \cdots + \frac{1}{2^n}\right)
= \lim_{n\to\infty} \left[2\left(1 - \frac{1}{2^{n+1}}\right)\right] = 2.
```

这将 infinite sum（无穷和）的计算归结为有限和加上 limit operation（极限运算）。事实上，这正是我们在计算 $1, 1\frac{1}{2}, 1\frac{3}{4}, 1\frac{7}{8}, 1\frac{15}{16}, \ldots$ 时所做的事情，并认为这是将总和视为 2 的令人信服的理由。

就本教材理论发展而言，这看起来完全自然且不足为奇。我们在第 2 章掌握了 sequences（序列），现在利用 sequences（序列）的方法进入第 3 章关于 infinite sums（无穷和）的内容。但从历史上看，情况并非如此。Infinite summations（无穷求和）似乎在人们对 sequences（序列）进行任何严格研究之前就已经被研究和使用很久了。事实上，即使要像之前那样形成无穷和的概念，似乎也需要我们先对序列有所了解，但这并非历史发展的实际路径。

直到 Cauchy 时代，才借助 sequence limits（序列极限）作为基础建立了 infinite summation（无穷求和）的现代理论。我们可以将 sequence limits（序列极限）方面的大量专业知识迁移到 infinite sums（无穷和）问题中。即便如此，本章的研究也有其独特的风格和魅力。在许多方面，infinite sums（无穷和）比 sequences（序列）更有趣、对分析学也更重要。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 无穷级数的研究历史远早于严格的极限理论。早在古希腊时期，Archimedes（阿基米德，约公元前 287–212）就已通过穷竭法计算抛物线弓形面积，本质上涉及几何级数求和。17–18 世纪，Euler（欧拉，1707–1783）等数学家大胆运用无穷级数获得了大量深刻结果，但当时缺乏严格的收敛概念，甚至出现了 $1+2+4+8+\cdots = -1$ 之类的悖论（习题 2.10.1）。直到 19 世纪，Cauchy、Abel（阿贝尔）和 Riemann（黎曼）等人建立了严格的极限理论和级数收敛判别法，才为无穷和奠定了坚实的基础。本书第 2 章对序列的严格处理，正是为第 3 章的级数理论做准备。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b;">3.2 Finite Sums（有限和）</span>

我们应首先从 finite sums（有限和）开始对 infinite sums（无穷和）的讨论。关于 finite sums（有限和）并没有太多需要说明的。任意有限个实数的集合都可以按任何顺序、以任何分组方式求和。这并不是说我们不会在实际问题中遇到困难——例如，前 $10^{100}$ 个 prime numbers（素数）的和是多少？在宇宙的剩余寿命内，没有计算机或人类能算出这个值。但数学上没有问题：它是一个有限个实数的和，因而是良定义的。

我们需要掌握一些 notations（记法）和技巧，以便为后续无穷和的学习做好准备。求和符号（summation notation）可能较为新颖。如何最好地写出表示某个数字集合 $\{a_1, a_2, a_3, \ldots, a_n\}$ 已被求和的符号？显然

```math
a_1 + a_2 + a_3 + \cdots + a_n
```

是一种过于冗长的写法。以下记法已被证明沟通效果更好：

```math
\sum_{i\in I} a_i
```

其中 $I$ 是集合 $\{1, 2, 3, \ldots, n\}$，或

```math
\sum_{i=1}^{n} a_i \quad\text{或}\quad \sum_{1\le i\le n} a_i.
```

这里希腊字母 $\Sigma$（对应大写字母 S）用于表示求和。正是 Leonhard Euler（莱昂哈德·欧拉，1707–1783）为我们引入了这一 sigma 记法（他于 1755 年首次使用）。函数符号 $f(x)$、$\sqrt{\phantom{x}}$、$e$、$\pi$、$\mathrm{i}$（表示 $\sqrt{-1}$）同样出自欧拉。仅此即可看出他的影响力之深远。他一生撰写了 886 篇论文和著作，被认为是有史以来最多产的数学家。

初等算术的通常规则同样适用于有限和。交换律（commutative law）、结合律（associative law）和分配律（distributive law）在 Euler 的记法下呈现为：

```math
\sum_{i\in I} a_i + \sum_{i\in I} b_i = \sum_{i\in I} (a_i + b_i), \qquad
\sum_{i\in I} c a_i = c \sum_{i\in I} a_i,
```

以及

```math
\left(\sum_{i\in I} a_i\right)\left(\sum_{j\in J} b_j\right) = \sum_{i\in I}\sum_{j\in J} a_i b_j.
```

以及

```math
\sum_{i=1}^{n} a_i = \sum_{i=1}^{m} a_i + \sum_{i=m+1}^{n} a_i \quad (m < n).
```

这些规则很简单，我们将在整章中使用它们。接下来的习题主要是为了让你熟悉这种记法。

<span style="color:#2471a3;">**[section]**</span> **3.2.10**
 求以下式子的 formula（公式）：

```math
\sqrt{2} + 2\sqrt{2} + 4 + 4\sqrt{2} + 8 + 8\sqrt{2} + \cdots + 2^m.
```

---

<span style="color:#2471a3;">**[section]**</span> **3.2.11** 推导公式：

```math
\sin\theta + \sin 2\theta + \sin 3\theta + \sin 4\theta + \cdots + \sin n\theta = \frac{\cos\theta/2 - \cos(2n+1)\theta/2}{2\sin\theta/2}.
```

如果公式中分母为零，应如何解释？

<span style="color:#2471a3;">**[详见 NOTE 39]**</span>

---

<span style="color:#2471a3;">**[section]**</span> **3.2.12** 推导公式：

```math
\cos\theta + \cos 3\theta + \cos 5\theta + \cos 7\theta + \cdots + \cos(2n-1)\theta = \frac{\sin 2n\theta}{2\sin\theta}.
```

---

<span style="color:#2471a3;">**[section]**</span> **3.2.13** 如果

```math
s_n = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \cdots + (-1)^{n+1}\frac{1}{n},
```

证明对所有 $n$ 有 $1/2 \le s_n \le 1$。

---

<span style="color:#2471a3;">**[section]**</span> **3.2.14** 如果

```math
s_n = 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \cdots + \frac{1}{n},
```

证明对所有 $n$ 有 $s_{2^n} \ge 1 + n/2$。

---

<span style="color:#2471a3;">**[section]**</span> **3.2.15** 求以下式子的 closed form（闭式）：

```math
\sum_{k=1}^{n} \frac{1}{k(k+2)(k+4)}.
```

---

<span style="color:#2471a3;">**[section]**</span> **3.2.16** 求以下式子的 closed form（闭式）：

```math
\sum_{k=1}^{n} \frac{\alpha k + \beta}{k(k+1)(k+2)}.
```

---

<span style="color:#2471a3;">**[section]**</span> **3.2.17** 设 $\{a_k\}$ 和 $\{b_k\}$ 是 sequences（序列），其中 $\{b_k\}$ 递减且对所有 $k$ 有 $|a_1 + a_2 + \cdots + a_k| \le K$。证明对所有 $n$ 有

```math
\left|\sum_{k=1}^{n} a_k b_k\right| \le K b_1.
```

---

<span style="color:#2471a3;">**[section]**</span> **3.2.18** 如果 $r$ 是年 interest rate（利率）（例如 $r = 0.06$），则

```math
P(1+r)^{-1} + P(1+r)^{-2} + \cdots + P(1+r)^{-n}
```

是每年支付 $P$ 美元、从明年开始持续 $n$ 年的 annuity（年金）的 present value（现值）。给出该式的更简洁公式。（Perpetuity（永续年金）有几乎相同的公式，但支付持续到永远。参见 Exercise 3.4.12（习题 3.4.12）。）

---

<span style="color:#2471a3;">**[section]**</span> **3.2.19** 定义 finite product（有限乘积）（有限个实数的乘积）为

```math
\prod_{k=1}^{n} a_k = a_1 a_2 a_3 \ldots a_n.
```

你能确定 products（乘积）的哪些基本性质？

---

<span style="color:#2471a3;">**[section]**</span> **3.2.20** 求以下式子的 closed form expression（闭式表达式）：

```math
\prod_{k=1}^{n} \frac{k^3 - 1}{k^3 + 1}.
```

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b;">3.3 Infinite Unordered Sums（无穷无序和）</span>

> <span style="color:#2471a3;">**[advanced]**</span> 高级小节。可省略。

我们现在转向 infinite sums（无穷和）的研究。我们希望解释

```math
\sum_{i\in I} a_i
```

对于无限 index set（指标集）$I$ 的含义。Finite sums（有限和）的研究不涉及 analysis（分析）、limits（极限）、$\varepsilon$，简言之，不涉及分析所特有的任何过程。要定义和研究 infinite sums（无穷和）则需要我们在 analysis（分析）中的许多技能。

为开始研究，设想我们有一个由 numbers（数）$a_i$ 组成的集合，以无限集 $I$ 为指标集（即存在一个函数 $a: I \to \mathbb{R}$），我们希望求出所有这些数的和。如果集合 $I$ 具有某种结构，我们就可以利用该结构来决定如何开始加总这些数。例如，如果 $a$ 是一个 sequence（序列），从而 $I = \mathbb{N}$，那么我们很可能会从 sequence（序列）的开头开始相加：

```math
a_1,\; a_1 + a_2,\; a_1 + a_2 + a_3,\; a_1 + a_2 + a_3 + a_4,\; \ldots
```

从而将该和定义为这个 partial sums（部分和）序列的 limit（极限）。

另一个集合 $I$ 会提示不同的顺序。例如，如果 $I = \mathbb{Z}$（所有整数的集合），则一种流行的求和方法是从以下开始：

```math
a_0,\; a_{-1} + a_0 + a_1,\; a_{-2} + a_{-1} + a_0 + a_1 + a_2,\; a_{-3} + a_{-2} + a_{-1} + a_0 + a_1 + a_2 + a_3,\; \ldots
```

同样地，将该和定义为该 sequence（序列）的 limit（极限）。

似乎求和的方法——从而定义表达式 $\sum_{i\in I} a_i$ 对于无限集 $I$ 的含义——必须依赖于集合 $I$ 的性质，因而依赖于所研究课题的具体问题。这在某种程度上是正确的。但这并不妨碍我们发明一种适用于所有无限集 $I$ 的方法。我们必须做出一个定义，该定义不考虑集合 $I$ 的额外结构或顺序，而仅将其视为一个集合。这被称为 unordered sum（无序和），符号 $\sum_{i\in I} a_i$ 总是表示正在考虑的是一个 unordered sum（无序和）。关键在于如何从 finite sums（有限和）过渡到 infinite sums（无穷和）。前面的两个例子都使用了取某些有限和（以系统的方式）然后取 limit（极限）的想法。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 本书区分了两种无穷和：**无序和（unordered sum）**与**有序和（ordered sum，即级数）**。无序和的收敛定义不依赖指标集的任何顺序结构：无论以何种顺序取有限项相加，部分和都必须一致地趋近于同一个值。定理 3.5 表明，若一个无序和收敛，则非零项至多可数多个，因此其理论本质上是可数集合上的理论。相比之下，级数（§3.4）利用 $\mathbb{N}$ 的自然顺序逐项累加，更贴合实际应用。两者的关键区别在于：条件收敛级数的 Riemann 重排定理表明，改变求和顺序可以改变和的值，而这在无序和（其定义本身就要求与顺序无关）中不可能发生。

<span style="color:#c0392b">**Definition 3.2（定义 3.2）**</span>：设 $I$ 是一个无限集，$a$ 是一个函数 $a: I \to \mathbb{R}$。那么我们记

```math
\sum_{i\in I} a_i = c
```

并称该和 **converges（收敛）**，如果对于每个 $\varepsilon > 0$，存在一个有限集 $I_0 \subset I$，使得对于每个满足 $I_0 \subset J \subset I$ 的有限集 $J$，有

```math
\left|\sum_{i\in J} a_i - c\right| < \varepsilon.
```

---

**定理继续——** 按照定义，有 $\sum_{i\in I} a_i = c$，定理得证。

```math
\blacksquare
```

我们的下一个定理表明，需要相加的数"太多"会导致问题。如果集合 $I$ 是 uncountable（不可数的），那么如果要使和存在，大多数要相加的 $a_i$ 应为零。这也表明，sums（和）的理论本质上局限于对 countable sets（可数集）求和。

**<span style="color:#2471a3;">收敛和中的非零项至多可数个 — All But Countably Many Terms in a Convergent Sum Are Zero.</span>**

在符号上可以有求和 $\sum_{x\in[0,1]} f(x)$，但除非 $f(x)$ 大部分为零且仅有可数多个例外，否则该和无法定义。

<span style="color:#c0392b">**Theorem 3.5（定理 3.5）**</span>：假设 $\sum_{i\in I} a_i$ 收敛。那么除了 $I$ 的某个 countable subset（可数子集）外，对所有 $i \in I$ 都有 $a_i = 0$。

> **Proof（证明）.** 我们将使用 Exercise 3.3.2（习题 3.3.2），其中证明了：对于任何 convergent sum（收敛和），存在一个正整数 $M$，使得对任意有限集 $I_0 \subset I$ 都有 $\left|\sum_{i\in I_0} a_i\right| \le M$。设 $m$ 为一个整数。我们问有多少个满足 $a_i > 1/m$ 的元素 $a_i$？易见最多有 $Mm$ 个，因为如果有更多，我们的和将超过 $M$。类似地，最多有 $Mm$ 个项满足 $-a_i > 1/m$。因此 $\{a_i : i \in I\}$ 中每个非零元素都可以赋予一个"等级"$m$，取决于 $1/m < a_i \le 1/(m-1)$ 或 $1/m < -a_i \le 1/(m-1)$。由于每个等级上只有有限多个元素，这为我们提供了一种列出 $\{a_i : i \in I\}$ 中所有非零元素的方法，因此该集合是 countable（可数的）。$\blacksquare$

Unordered sums（无序和）的基本性质在 exercises（习题）中展开。这些和在 analysis（分析）中作用较小，远小于我们将在后续小节中考虑的 ordered sums（有序和）。然而，其证明方法非常值得研究，因为它们以某种形式在 analysis（分析）的许多部分中被使用。这些习题提供了一个有趣的场景来测试你在 analysis（分析）中的技能，这些技能将在你后续的所有学习中发挥作用。

### Exercises（习题）

<span style="color:#2471a3;">**[exercise]**</span> **3.3.1** 证明如果 $\sum_{i\in I} a_i$ 收敛，则该和是唯一的。

<span style="color:#2471a3;">**[详见 NOTE 40]**</span>

<span style="color:#2471a3;">**[exercise]**</span> **3.3.2** 证明如果 $\sum_{i\in I} a_i$ 收敛，则存在一个正数 $M$ 使得对任意有限集 $I_0 \subset I$ 有 $\left|\sum_{i\in I_0} a_i\right| \le M$。

<span style="color:#2471a3;">**[详见 NOTE 41]**</span>

<span style="color:#2471a3;">**[exercise]**</span> **3.3.3** 假设和 $\sum_{i\in I} a_i$ 中的所有项都是 nonnegative（非负的），并且存在一个正数 $M$ 使得对任意有限集 $I_0 \subset I$ 有 $\sum_{i\in I_0} a_i \le M$。证明 $\sum_{i\in I} a_i$ 必收敛。

<span style="color:#2471a3;">**[详见 NOTE 42]**</span>

<span style="color:#2471a3;">**[exercise]**</span> **3.3.4** 证明如果 $\sum_{i\in I} a_i$ 收敛，则对每个子集 $J \subset I$，$\sum_{i\in J} a_i$ 也收敛。

<span style="color:#2471a3;">**[exercise]**</span> **3.3.5** 证明如果 $\sum_{i\in I} a_i$ 收敛且每个 $a_i \ge 0$，则

```math
\sum_{i\in I} a_i = \sup\left\{\sum_{i\in J} a_i : J \subset I,\ J \text{ finite}\right\}.
```

<span style="color:#2471a3;">**[exercise]**</span> **3.3.6** 第 3.2 节中有限和运算的每一条规则都可以考虑用于 infinite unordered sums（无穷无序和）。阐述正确的陈述并证明你认为对有限和成立的这些陈述的类比：

```math
\sum_{i\in I} a_i + \sum_{i\in I} b_i = \sum_{i\in I} (a_i + b_i)
```

```math
\sum_{i\in I} c a_i = c \sum_{i\in I} a_i
```

```math
\sum_{i\in I} a_i \times \sum_{j\in J} b_j = \sum_{i\in I} \sum_{j\in J} a_i b_j = \sum_{j\in J} \sum_{i\in I} a_i b_j.
```

<span style="color:#2471a3;">**[exercise]**</span> **3.3.7** 在适当的收敛假设下，证明

```math
\sum_{i\in I\cup J} a_i + \sum_{i\in I\cap J} a_i = \sum_{i\in I} a_i + \sum_{i\in J} a_i.
```

<span style="color:#2471a3;">**[exercise]**</span> **3.3.8** 设 $\sigma: I \to J$ 是一一对应（one-to-one and onto）。在适当的收敛假设下，证明

```math
\sum_{j\in J} a_j = \sum_{i\in I} a_{\sigma(i)}.
```

<span style="color:#2471a3;">**[exercise]**</span> **3.3.9** 求和

```math
\sum_{i\in \mathbb{N}} \frac{1}{2^i}.
```

<span style="color:#2471a3;">**[详见 NOTE 43]**</span>

<span style="color:#2471a3;">**[exercise]**</span> **3.3.10** 证明

```math
\sum_{i\in \mathbb{N}} \frac{1}{i}
```

发散。是否存在无限子集 $J \subset \mathbb{N}$ 使得 $\sum_{i\in J} \frac{1}{i}$ 收敛？

---

<span style="color:#2471a3;">**[exercise]**</span> **3.3.11** 证明 $\sum_{i\in I} a_i$ 收敛当且仅当 $\sum_{i\in I} [a_i]^+$ 和 $\sum_{i\in I} [a_i]^-$ 都收敛，并且

```math
\sum_{i\in I} a_i = \sum_{i\in I} [a_i]^+ - \sum_{i\in I} [a_i]^-.
```

**3.3.12** 计算

```math
\sum_{i=1}^{\infty} \frac{1}{2^i}\quad\text{和}\quad\sum_{i=1}^{\infty} \frac{1}{2^i}
```

按照本节 unordered sum（无序和）的定义进行。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b;">3.4 Ordered Sums: Series（有序和：级数）</span>

 证明 $\sum_{i\in I} a_i$ 收敛当且仅当 $\sum_{i\in I} [a_i]^+$ 和 $\sum_{i\in I} [a_i]^-$ 都收敛，并且

```math
\sum_{i\in I} a_i = \sum_{i\in I} [a_i]^+ - \sum_{i\in I} [a_i]^-
```

且

```math
\sum_{i\in I} |a_i| = \sum_{i\in I} [a_i]^+ + \sum_{i\in I} [a_i]^-.
```

<span style="color:#2471a3;">**[详见 NOTE 44]**</span>

<span style="color:#2471a3;">**[exercise]**</span> **3.3.12** 计算

```math
\sum_{(i,j)\in \mathbb{N}\times\mathbb{N}} 2^{-i-j}.
```

这里什么样的 ordered sum（有序和）显得自然（如同本节中考虑 $\mathbb{N}$ 和 $\mathbb{Z}$ 上的有序和那样）？

<span style="color:#2471a3;">**[详见 NOTE 45]**</span>

---

现在进入本节主题。

对于绝大多数应用，我们想要求和的不是任意一个数的集合，而是最常见的某个 sequence of numbers（数列）：

```math
a_1 + a_2 + a_3 + \ldots.
```

自然数集 $\mathbb{N}$ 具有 order structure（顺序结构），忽略这个顺序不符合我们的最佳利益，因为这是 sequence（序列）呈现给我们的顺序。最自然的加总一个数列的方法是从头开始累加：

```math
a_1,\; a_1 + a_2,\; a_1 + a_2 + a_3,\; a_1 + a_2 + a_3 + a_4,\; \ldots
```

并将该和定义为这个 sequence（序列）的 limit（极限）。这就是我们将要做的。

如果你学习了第 3.3 节关于 unordered summation（无序求和）的内容，还应将这种"ordered（有序）"方法与 unordered（无序）方法进行比较。sequence（序列）的 ordered sum（有序和）称为 **series（级数）**，符号

```math
\sum_{k=1}^{\infty} a_k
```

专门用于此概念。

<span style="color:#c0392b">**Definition 3.6（定义 3.6）**</span>：设 $\{a_k\}$ 是一个实数 sequence（序列）。则我们记

```math
\sum_{k=1}^{\infty} a_k = c
```

并称该 **series（级数）converges（收敛）**，如果 sequence（序列）

```math
s_n = \sum_{k=1}^{n} a_k
```

（称为该 series（级数）的 **partial sums（部分和）** sequence（序列））收敛到 $c$。如果该 series（级数）不收敛，则称其 **divergent（发散）**。

该定义将 series（级数）的研究归结为 sequences（序列）的研究。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 将级数 $\sum a_k$ 的研究归结为部分和序列 $\{s_n\}$ 的研究，是分析中化归思想的典型体现。第 2 章建立的所有序列理论（极限的代数运算、单调收敛准则、Cauchy 准则、上下极限等）均可直接应用于级数。例如，级数收敛的 Cauchy 准则为：对任意 $\varepsilon>0$，存在 $N$ 使得当 $m>n\ge N$ 时 $|a_{n+1}+a_{n+2}+\cdots+a_m|<\varepsilon$。然而，级数理论也发展出了自身的独特方法，如比较判别法、比值判别法和积分判别法，这些已超出了单纯的序列理论范畴。

我们在第 2 章已经有了高度发展的 convergent sequences（收敛序列）理论，可以应用于发展 series（级数）的理论。因此，我们可以从已知知识迅速产生相当深入的 series（级数）理论。然而，随着理论的发展，我们将看到它开始具有自己的特征，而不再仅仅是对 sequence（序列）思想的简单应用。

#### 3.4.1 Properties（性质）

以下是从我们的 sequence（序列）理论直接获得的一组定理。series（级数）$\sum_{k=1}^{\infty} a_k$ 的 convergence（收敛）或 divergence（发散）取决于 partial sums（部分和）sequence（序列）$s_n = \sum_{k=1}^{n} a_k$ 的收敛或发散，而 series（级数）的值就是该 sequence（序列）的 limit（极限）。要证明下面列出的每个定理，只需从第 2 章中找到关于 sequences（序列）的正确定理。这留作 Exercise 3.4.2（习题 3.4.2）。

<span style="color:#c0392b">**Theorem 3.7（定理 3.7）**</span>：如果 series（级数）$\sum_{k=1}^{\infty} a_k$ 收敛，则该和是唯一的。

<span style="color:#c0392b">**Theorem 3.8（定理 3.8）**</span>：如果 series（级数）$\sum_{k=1}^{\infty} a_k$ 和 $\sum_{k=1}^{\infty} b_k$ 都收敛，则 series（级数）$\sum_{k=1}^{\infty} (a_k + b_k)$ 也收敛，且

```math
\sum_{k=1}^{\infty} (a_k + b_k) = \sum_{k=1}^{\infty} a_k + \sum_{k=1}^{\infty} b_k.
```

<span style="color:#c0392b">**Theorem 3.9（定理 3.9）**</span>：如果 series（级数）$\sum_{k=1}^{\infty} a_k$ 收敛，则对任意实数 $c$，series（级数）$\sum_{k=1}^{\infty} c a_k$ 也收敛，且

```math
\sum_{k=1}^{\infty} c a_k = c \sum_{k=1}^{\infty} a_k.
```

<span style="color:#c0392b">**Theorem 3.10（定理 3.10）**</span>：如果 series（级数）$\sum_{k=1}^{\infty} a_k$ 和 $\sum_{k=1}^{\infty} b_k$ 都收敛，且对每个 $k$ 有 $a_k \le b_k$，则

```math
\sum_{k=1}^{\infty} a_k \le \sum_{k=1}^{\infty} b_k.
```

<span style="color:#c0392b">**Theorem 3.11（定理 3.11）**</span>：设 $M \ge 1$ 为任意整数。则 series（级数）

```math
\sum_{k=1}^{\infty} a_k = a_1 + a_2 + a_3 + a_4 + \ldots
```

收敛当且仅当 series（级数）

```math
\sum_{k=1}^{\infty} a_{M+k} = a_{M+1} + a_{M+2} + a_{M+3} + a_{M+4} + \ldots
```

收敛。

---

*Translation completed / 翻译完成*
