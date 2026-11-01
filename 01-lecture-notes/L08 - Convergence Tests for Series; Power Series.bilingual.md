# 18.100B / 18.1002 Real Analysis（实分析）

## <span style="color:#c0392b">Lecture 8 — Convergence Tests for Series; Power Series（级数收敛检验；幂级数）</span>

<span style="color:#7f8c8d;">Instructor: Tobias Holck Colding · Spring 2025 · MIT</span>

---

### <span style="color:#2471a3;">**[lecture]**</span> <span style="color:#c0392b">Series（级数）</span>

假设 $a_n$ 是一个 sequence（序列），我们可以如下构造一个新的序列 $s_n$。令

```math
s_1 = a_1, \qquad s_2 = a_1 + a_2, \qquad s_3 = a_1 + a_2 + a_3,
```

一般地，

```math
s_n = a_1 + \cdots + a_n = \sum_{i=1}^{n} a_i.
```

序列 $s_n$ 称为**部分和序列（sequence of partial sums）**。级数 $\sum_{i=1}^{\infty} a_i$ **收敛（converges）**当且仅当序列 $s_n$ 收敛；若收敛，我们也把极限记为 $\sum_{i=1}^{\infty} a_i$。

> <span style="color:#7f8c8d;">TBB §3.4, p.83</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 你在中学把 $\sum_{n=0}^\infty a_n$ 当成"无穷项连加"来写，但分析学里这个符号本身没有独立意义。级数的精确定义是：先有序列 $(a_n)$，构造部分和序列 $s_n = \sum_{k=0}^n a_k$——这是一个新的序列——然后问 $\lim_{n\to\infty} s_n$ 是否存在。若存在，级数"收敛"且这个极限值就是无穷和。换句话说，无穷和从未直接计算过，是先算有限和再取极限。🎥 *Colding 说:* "So series is that you have a sequence. You're starting with a sequence. So a n is a sequence. And then you form a new sequence."（翻译：级数就是你先有一个序列 $a_n$，然后构造一个新序列。）这个两层结构是理解级数一切性质的钥匙——你把对级数的每个问题都翻译成对部分和序列的问题，再调用 L04 的序列收敛概念（如 $\varepsilon$-$N$ 定义）和 L05-L07 的收敛定理（MCT、Cauchy、Bolzano–Weierstrass）。你可以记这个直觉："级数是穿在序列外面的另一件外套"——真正干活的是里面的序列 $s_n$，级数只是外面那层符号皮。为什么必须这样定义？因为"无穷项相加"不是良定义的操作——你不能真的把无穷个数一个一个加起来——而有限和 + 极限的路径每一步都是良定义的。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Geometric Series（几何级数）</span>

```math
\sum_{i=0}^{\infty} c^i
```

这个级数**恰好当 $|c| < 1$ 时收敛**。

> <span style="color:#7f8c8d;">TBB §3.4.2, p.85</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 证明策略模板——我管它叫**"基准级数锚定法"**。几何级数 $\sum c^n$ 是整个级数检验体系的基准（standard of comparison）。它的部分和公式不是天上掉下来的：令 $S_n = 1 + c + c^2 + \cdots + c^n$，乘以 $c$ 得 $cS_n = c + c^2 + \cdots + c^{n+1}$，相减得 $(1-c)S_n = 1 - c^{n+1}$，于是 $S_n = \frac{1-c^{n+1}}{1-c}$（$c \neq 1$）。当 $|c|\lt 1$ 时 $c^{n+1} \to 0$，$S_n \to \frac{1}{1-c}$；当 $|c|\ge 1$ 时 $|c^{n+1}| \ge 1$ 不趋于 0，级数发散。这个"指数衰减决定收敛"的直觉远不止于分析学——你在 CSAPP 的算法分析里见过它：二分搜索每层数据量减半，总比较次数是 $1+1/2+1/4+\cdots = O(1)$ 倍的几何级数；在 6.006（CLRS）的 Master 定理中，递归树每层代价若按几何比率衰减（如 $T(n) = T(n/2) + n$ 中第一层 $n$，第二层 $n/2$，第三层 $n/4$），总和也是几何级数。反过来，算法课里的"几何分布"期望——重复独立试验直到成功——也直接用了 $\sum_{k=1}^\infty k(1-p)^{k-1}p$ 这种几何级数变体（可通过求导从标准几何级数推出——你在离散数学 6.042J 学过生成函数求导技巧，正是这个思路）。几何级数之所以"如此关键"（🎥 *Colding:* "the next two tests, the ratio test and root test, are based on comparison with the geometric series"（翻译：接下来的两个检验——比值检验和根值检验——都基于与几何级数的比较），正是因为它是人类第一个精确求出无穷和的级数，也是唯一一个能同时充当所有其他检验参照物的"原子级数"。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Harmonic Series（调和级数）</span>

```math
\sum_{n=1}^{\infty} \frac{1}{n}
```

这个级数是**发散（divergent）**的。

> <span style="color:#7f8c8d;">TBB §3.4.2, p.85</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 调和级数 $\sum 1/n$ 是分析学最重要的反例制造机——每一项都老老实实趋于 0（满足收敛的必要条件），但全体加起来却发散到无穷。这种"分子听话、总和失控"的行为极其反直觉，也是人类历史上第一次发现"必要条件不等于充分条件"的著名案例。发散的速度有多慢？其部分和 $H_n = 1 + 1/2 + \cdots + 1/n \approx \ln n + \gamma$，其中 $\gamma \approx 0.5772156649$ 是 Euler–Mascheroni 常数（因 Euler 首先系统研究调和级数部分和而得名）。这意味着你要把 $n$ 推到 $e^{100}$ 量级（一个天文数字），部分和才不过 100 左右——发散得极其磨蹭。把调和级数和几何级数并排放：几何级数在 $|c|\ge 1$ 时项不趋于 0，直接 pass（必要条件都不过关）；但调和级数过了"项趋于 0"的安检却仍然发散，说明 $1/n$ 衰减得不够快。从第一性原理追问：为什么不够快？比较 $\sum 1/n^p$：$p>1$ 时收敛，$p \le 1$ 时发散——$p=1$ 是临界点。直觉上，$1/n^2$ 的尾巴"薄"到可以被有限面积包住（像 $\int_1^\infty 1/x^2\,dx$ 收敛），而 $1/n$ 的尾巴刚好"厚"到边界上（$\int 1/x\,dx = \ln x$ 发散）——但你会在 L09 或积分检验里严格看到这个类比，这里先留一个印象。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Absolutely Convergent（绝对收敛）</span>

我们说级数 $\sum_{n=0}^{\infty} a_n$ 是**绝对收敛（absolutely convergent）**的，如果级数 $\sum_{n=0}^{\infty} |a_n|$ 是收敛的。

绝对收敛蕴含收敛，但反过来不成立。

> <span style="color:#7f8c8d;">TBB §3.5.3, p.92</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 绝对收敛 ⟹ 收敛的证明是 L06 Cauchy 收敛准则的教科书级应用。设 $\sum |a_n|$ 收敛，则其部分和序列是 Cauchy 的：对任意 $\varepsilon > 0$，存在 $N$ 使 $m > n \ge N$ 时 $\sum_{k=n+1}^m |a_k| < \varepsilon$。现在看原级数 $\sum a_n$ 的部分和差：$|\sum_{k=n+1}^m a_k| \le \sum_{k=n+1}^m |a_k| < \varepsilon$（三角不等式——你在线性代数 Strang 和 L02 的绝对值性质中都见过），所以 $\sum a_n$ 的部分和也是 Cauchy 的，由 Cauchy 收敛定理（L06）得收敛。🎥 *Colding 的解释直接到粗暴:* "it means that the series where you're slapping on absolute value, so this thing here, means that this series here is convergent."（翻译：它意味着把绝对值符号拍上去之后得到的那个级数是收敛的。）反过来的问题——收敛是否蕴涵绝对收敛——答案是**否**。反例正是交错调和级数 $\sum (-1)^{n+1}/n$：🎥 *Colding:* "If you were slapping an absolute value sign on it... then this here is just $1/n$. And this is the harmonic series. And this is divergent."（翻译：如果给它拍上绝对值符号……就得到 $1/n$，即调和级数，它是发散的。）条件收敛最颠覆直觉的性质在重排上：绝对收敛级数任意重排和不变（有限和的交换律升到了无穷），但条件收敛级数通过巧妙重排可以收敛到任何实数（你在 TBB §3.7 翻译过 Riemann 重排定理——这正是我提醒你别跳过的原因）。无限和与有限和的差别，说到底是"交换律/结合律在无穷面前不再自动成立"。

---

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem: 非负项级数收敛 ⟺ 部分和有上界</span>

一个由非负数组成的级数（$a_n \ge 0$）

```math
\sum_{i=0}^{\infty} a_i
```

**收敛当且仅当**部分和序列 $s_n$ 是**有上界的（bounded from above）**。

> <span style="color:#7f8c8d;">TBB §3.5.1, p.91</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 证明策略模板——**"单调还原法"**。非负项级数（$a_n \ge 0$）的部分和序列 $s_n = \sum_{k=1}^n a_k$ 有一个致命的好性质：$s_{n+1} = s_n + a_{n+1} \ge s_n$，所以 $(s_n)$ 单调递增。这一脚把"级数收敛"这个看起来全新的问题踹回你已经熟练掌握的地盘——L05 单调收敛定理（MCT）：单调递增序列收敛的充要条件是它有上界。于是"级数 $\sum a_n$（$a_n \ge 0$）收敛"等价于"部分和序列 $s_n$ 有上界"，不需要构造极限，只看有没有上界就够了。这是整个非负项级数理论的"大坝"——所有比较检验、比值检验、根值检验，最终都是靠本讲开头的非负项定理兜底的：每个检验本质上都在问"我能不能给部分和找到一个上界？"找不到，就发散。反过来，Cauchy 准则（L06）是另一条道——不依赖单调性，适用于任意项级数——但处理非负项时 MCT 往往更顺手。建议你在本章每看到一个收敛性证明，都心里追问一句"这个证明的最后一步是不是调用了 MCT？"——八九不离十。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Convergence Tests（收敛检验方法一览）</span>

为了帮助判断一个级数是否收敛，有一系列检验方法：

- **Comparison test（比较检验）**。
- **Ratio test（比值检验）**。
- **Root test（根值检验）**。
- 其他检验方法我们以后讨论。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 你可能会问：为什么搞这么多检验？一个统一的"超级检验"不存在吗？答案是：不同级数的"形状"需要用不同工具来抓。比较检验适合项有显式上下界的情形（比如分母是个多项式，你能一眼看出它是 $O(1/n^2)$ 还是 $\Theta(1/n)$——你在 6.006 CLRS 里天天用渐进记号，这里完全是同一个直觉）。但它有一个硬伤：你必须另外找一个已知收敛/发散的级数来比（🎥 *Colding:* "Like in the comparison test, you had to find another series."（翻译：在比较检验里你必须另外找一个级数来比较）。比值检验和根值检验解决了这个问题——它们只靠级数自身的项就能判定，不假外求。共同内核：这三种检验本质上都是"与已知级数比较"的变体，而那个"已知级数"几乎总是几何级数 $\sum c^n$（🎥 *Colding:* "both the ratio test and root test, are based on comparison with the geometric series"（翻译：比值检验和根值检验都基于与几何级数的比较）。预告：后面还会遇到 Cauchy condensation test（柯西凝聚检验，Cauchy 命名，专门对付非负递减序列——比如 $p$ 级数 $\sum 1/n^p$ 的收敛性可以通过它干净地推导出来，而不依赖积分）和积分检验（TBB §3.6.7-3.6.8），它们填补了比值/根值检验在 $r=1$ 边界上"失明"的空白。

---

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Comparison Test; Version 1（比较检验，第 1 版）</span>

假设 $a_n$ 与 $b_n$ 是两个序列，且满足

```math
0 \le a_n \le b_n.
```

如果 $\sum_{n=1}^{\infty} b_n$ 收敛，那么 $\sum_{n=1}^{\infty} a_n$ 也收敛。

> <span style="color:#7f8c8d;">TBB §3.6.2, p.96（Direct Comparison Test I）</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 证明策略模板——**"单向挤压法"**。🎥 *Colding 说得非常直白:* "I'm assuming here that a n and the bn are non-negative numbers. And in fact, I'm assuming that bn is larger or equal to a n."（翻译：我假设 $a_n$ 和 $b_n$ 都是非负数，且 $b_n \ge a_n$。）"If the series based on the bn is convergent, then the series of the a n's is also convergent."（翻译：如果由 $b_n$ 构成的级数收敛，那么 $a_n$ 的级数也收敛。）第一性原理拆解：$0 \le a_n \le b_n$ 意味着 $\sum_{k=1}^n a_k \le \sum_{k=1}^n b_k$——部分和被逐项压制。若 $\sum b_n$ 收敛，其部分和有上界（调用本讲前面的非负项定理——基于 MCT），那么 $\sum a_n$ 的部分和也有上界，再由 MCT 推出 $\sum a_n$ 收敛。这个证明连锁反应极其干净：逐项不等式 → 部分和不等式 → 上界存在 → MCT 出场。注意方向：大级数收敛推小级数收敛（顺向），等价地，小级数发散推大级数发散（逆向——取逆否命题）。你得小心别搞反：如果你只知道大级数发散，对小级数下不了任何结论（大级数发散可能是因为"尾巴太厚"，小级数可能还够薄）；同理，只知道小级数收敛，大级数可能收敛也可能发散。

<span style="color:#2471a3;">**[example]**</span> **Example（例）:** 级数

```math
\sum_{n=1}^{\infty} \frac{2^{-n}}{n}
```

是收敛的。事实上，令

```math
a_n = \frac{2^{-n}}{n}, \qquad b_n = 2^{-n},
```

则 $0 \le a_n \le b_n$，且由于 $\sum_{n=1}^{\infty} b_n = \sum_{n=1}^{\infty} 2^{-n}$ 是一个收敛的几何级数，由比较检验（第 1 版）知 $\sum_{n=1}^{\infty} a_n$ 收敛。

---

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Comparison Test; Version 2（比较检验，第 2 版）</span>

假设 $a_n$ 与 $b_n$ 是两个序列，$b_n \ne 0$，且

```math
\lim_{n \to \infty} \frac{a_n}{b_n} = L \ne 0.
```

则级数 $\sum_{n=1}^{\infty} a_n$ **收敛当且仅当**级数 $\sum_{n=1}^{\infty} b_n$ 收敛。

> <span style="color:#7f8c8d;">TBB §3.6.3, p.98（Limit Comparison Test I）</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 证明策略模板——**"极限同阶法"**。v1 要求 $a_n \le b_n$ 对**每一项**都成立，这在实操中太苛刻——你往往只知道两项"差不多大"，但偶有交叉。v2 放松到只要求 $\lim_{n\to\infty} a_n/b_n = L$（$0 < L < \infty$），即两个序列"最终同阶"。条件 $L > 0$ 为什么不能省？若 $L = 0$（$a_n = o(b_n)$，用你 CLRS 里的小 o 记号），你只能推出 $a_n$ 最终 $\le \varepsilon b_n$，于是 $\sum b_n$ 收敛 ⇒ $\sum a_n$ 收敛（单向），但 $\sum b_n$ 发散时对 $a_n$ 束手无策——$a_n$ 可能薄到收敛也可能刚好在边界。$L \neq 0$ 保证了双向对等：$\frac{L}{2} b_n \le a_n \le \frac{3L}{2} b_n$ 最终成立，两边同时用 v1 的比较检验，两条级数同收敛或同发散。经典例题：$\sum \frac{1}{n^2-1}$。当 $n$ 大时 $\frac{1}{n^2-1} \approx \frac{1}{n^2}$，比值极限为 1，所以和 $\sum 1/n^2$ 同收敛。这本质上就是你在 CLRS 中用 $\Theta$ 记号时的直觉：同阶函数同增长（或同衰减），"同阶同生死"。

<span style="color:#2471a3;">**[example]**</span> **Example（例）:** 级数

```math
\sum_{n=2}^{\infty} \frac{1}{n^2 - 1}
```

是收敛的，因为

```math
\frac{n^2}{n^2 - 1} \to 1,
```

而级数 $\sum_{n=2}^{\infty} \frac{1}{n^2}$ 是收敛的。

---

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Ratio Test（比值检验）</span>

设 $a_n \ge 0$，并假设

```math
\frac{a_{n+1}}{a_n} \to a.
```

则：

- 若 $a < 1$，则级数 $\sum a_n$ **收敛（convergent）**；
- 若 $a > 1$，则级数 $\sum a_n$ **发散（divergent）**；
- 若 $a = 1$，则**无法判定（inconclusive）**。

> <span style="color:#7f8c8d;">TBB §3.6.5, p.100（d'Alembert's Ratio Test）</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 比值检验的第一性原理藏在它的名字里：$\lim |a_{n+1}/a_n| = r < 1$ 意味着**项最终按几何速率衰减**。具体来说，取 $r_0$ 使 $r < r_0 < 1$，最终有 $|a_{n+1}| \le r_0 |a_n|$，迭代下去 $|a_n| \le C \cdot r_0^{\,n}$——恰好是一个几何级数的项。🎥 *Colding 一言蔽之:* "both the ratio test and root test, are based on comparison with the geometric series. And so this is explaining why the geometric series is so crucial."（翻译：比值检验和根值检验都基于与几何级数的比较，这就解释了为什么几何级数如此关键。）所以比值检验的本质是在问一个问题："这个级数的项，最终衰减得像几何级数吗？"——像就收敛，不像就可能是发散。🎥 *Colding 还强调它的便利:* "the ratio test is simply the test that if you're looking at-- so if you have a series. You don't have to look at any other series."（翻译：比值检验很简单——你只需要看这一个级数自己，而在比较检验里你必须另外找一个级数来比较。）历史上，这个检验由 d'Alembert 于 1768 年在 *Opuscules mathématiques* 中首次发表，Waring 也独立得出（*Meditationes Analyticae*）。$r=1$ 无法判定的底层原因：比值趋于 1 说明项的衰减介于指数衰减和常数之间——典型的是多项式衰减（如 $1/n$、$1/n^2$）——此时几何级数这个基准变得太粗糙，需要更精细的工具（积分检验、凝聚检验）来区分"刚好够薄"和"还不够薄"。

<span style="color:#2471a3;">**[example]**</span> **Example 1（例 1）:** $a_n = \frac{1}{n}$。此时

```math
\frac{a_{n+1}}{a_n} \to 1,
```

检验无法判定，但该级数（调和级数）发散。

<span style="color:#2471a3;">**[example]**</span> **Example 2（例 2）:** $a_n = \frac{1}{n^2}$。此时

```math
\frac{a_{n+1}}{a_n} \to 1,
```

检验无法判定，但该级数收敛。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这两个例子是教学上的精准打击——它们被故意选来一起展示比值检验的"盲区"。对 $\sum 1/n$，$\left|\frac{a_{n+1}}{a_n}\right| = \frac{n}{n+1} \to 1$；对 $\sum 1/n^2$，$\left|\frac{a_{n+1}}{a_n}\right| = \frac{n^2}{(n+1)^2} \to 1$。比值检验两次都撞上 $r=1$ 的边界，返回"无法判定"——可实际上一个发散（调和级数）、一个收敛（$p$ 级数 $p=2>1$）。这个反例对是刻意构造来逼你追问"为什么 $r=1$ 挡不住？"答案是：$r=1$ 时比值检验只能告诉你"项衰减的速度不比任何几何级数快"，但几何衰减和多项式衰减之间的差距——就像 CLRS 里 $\Theta(n)$ 和 $\Theta(n \log n)$ 之间的差距一样——在这个尺度上变得致命。你需要更精细的判别工具：积分检验把级数和反常积分绑在一起（$\sum 1/n^p$ 和 $\int_1^\infty 1/x^p\,dx$ 同敛散），柯西凝聚检验把 $p$ 级数凝聚成几何级数（$\sum 2^k a_{2^k}$），两者都能干净地跨过 $p=1$ 这道门槛。更进阶的 Raabe 检验和 Kummer 检验（名字听听即可）本质上是在问"项衰减得比 $1/n^p$ 快还是慢"——把基准从几何级数换成了 $p$ 级数，看得更细，当然代价是计算更麻烦。

---

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Root Test（根值检验）</span>

设 $a_n \ge 0$ 是一个非负数序列。假设 $\lim_{n \to \infty} (a_n)^{\frac{1}{n}} = r$。则：

- 若 $r < 1$，则级数 $\sum_{n=0}^{\infty} a_n$ **收敛**；
- 若 $r > 1$，则级数 $\sum_{n=0}^{\infty} a_n$ **发散**；
- 若 $r = 1$，则**无法判定**。

> <span style="color:#7f8c8d;">TBB §3.6.6, p.101（Cauchy's Root Test）</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 根值检验的第一性原理比比值检验还直接：$(a_n)^{1/n} \to r$ 的意思是，$|a_n|$ 的"第 $n$ 根"趋近 $r$——换言之，$|a_n|$ 最终的量级大约是 $r^n$。这就是在**直接测项的大小量级**，不拐弯。如果 $r\lt 1$，$|a_n|$ 指数衰减，被某个几何级数压住（取 $r_0$ 使 $r < r_0 < 1$，最终 $(a_n)^{1/n} \le r_0$，即 $a_n \le r_0^{\,n}$）。如果 $r>1$，$|a_n|$ 指数爆炸，不仅不趋于 0，绝对值还趋于无穷——🎥 *Colding:* "if the series was converging, the most elementary thing is, the most basic thing is that the a n has to go to 0. Otherwise, it's not going to converge. But in fact, not only do they not go to 0, they actually, in absolute value, go to infinity. So it's very, very far from being convergent."（翻译：级数要收敛，最基本的是 $a_n$ 必须趋于 0，否则不会收敛。但事实上它们不仅不趋于 0，绝对值还趋于无穷大——离收敛差得非常非常远。）与比值检验的关键差异：根值检验对"偶尔跳变"鲁棒。🎥 *Colding:* "you could have-- there could be somewhere where the next one actually went up. But then presumably, after that, they're going down, at least for a long time... And the root test is OK with that, whereas that test wasn't OK with that."（翻译：可能某个地方下一项确实变大了，不过之后它们会下降很久……根值检验对这种情形没问题，而比值检验不行。）历史上，这个检验是 Cauchy 于 1821 年在 *Cours d'Analyse* 中给出的。

### <span style="color:#2471a3;">**[proof]**</span> <span style="color:#c0392b">Proof（根值检验的证明）</span>

**情形 $r < 1$。** 取 $r < r_0 < 1$，则存在 $N$ 使得当 $n \ge N$ 时，

```math
(a_n)^{\frac{1}{n}} \le r_0.
```

因此

```math
0 \le a_n \le r_0^n.
```

然而级数 $\sum_{n=0}^{\infty} r_0^n$ 是一个几何级数，且 $r_0 < 1$，故收敛。由比较检验（第 1 版），级数 $\sum_{n=0}^{\infty} a_n$ 也收敛。

**情形 $r > 1$。** 此时取 $1 < r_0 < r$，则存在 $N$ 使得当 $n \ge N$ 时，

```math
(a_n)^{\frac{1}{n}} \ge r_0.
```

于是对 $n \ge N$，

```math
a_n \ge r_0^n,
```

而 $\sum_{n=0}^{\infty} r_0^n$ 是发散的几何级数。因此由比较检验，原级数发散。 $\square$

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 证明策略模板——**"几何夹逼法"**。这个证明的结构你值得背下来，因为它会在 Cauchy–Hadamard 收敛半径定理中原封不动地复用。分两路：$r\lt 1$ 时，取一个中间值 $r_0$ 使 $r < r_0 < 1$——这里用的是 L04 极限定义中的经典技巧：既然 $(a_n)^{1/n} \to r$，存在 $N$ 使 $n \ge N$ 时 $(a_n)^{1/n} < r_0$，从而 $a_n < r_0^{\,n}$。于是从第 $N$ 项起，$\sum a_n$ 的尾巴被几何级数 $\sum r_0^{\,n}$ 压住，比较检验（v1）和 MCT 直接判收敛。$r>1$ 时，取 $r_0$ 使 $1 < r_0 < r$，类似得到 $a_n > r_0^{\,n} > 1$，项不趋于 0——连收敛的必要条件都垮了，不需要任何检验就知道发散。🎥 *Colding 强调发散程度:* "not only do they not go to 0, they actually, in absolute value, go to infinity."（翻译：不仅不趋于 0，绝对值还趋于无穷大。）$r=1$ 时"几何夹逼法"的两侧夹板一个在收敛侧一个在发散侧——分别对应 $\sum r_0^{\,n}$（$r_0\lt 1$ 收敛）和 $\sum r_0^{\,n}$（$r_0>1$ 发散）——所以判定崩溃。这个模板的灵魂是"取那个夹在极限和边界之间的 $r_0$"——它是 $\varepsilon$ 思想在级数中的变体，你在 L04 的极限定义中第一次见到这个套路（取 $\varepsilon = \frac{1-|a|}{2}$ 之类），后面会在收敛半径证明中第三次见到。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Power Series（幂级数）</span>

- $\displaystyle \sum_{n=0}^{\infty} x^n = \frac{1}{1-x}$。
- $\displaystyle \sum_{n=0}^{\infty} \frac{x^n}{n!} = \exp x$。
- $\displaystyle \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n}}{(2n)!} = \cos x$。
- $\displaystyle \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{(2n+1)!} = \sin x$。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这四个幂级数放在一起不是随意的——$\frac{1}{1-x}$、$e^x$、$\cos x$、$\sin x$ 分别代表四种根本不同的函数类型（有理函数、指数函数、三角函数），却都被同一个形式 $\sum a_n x^n$ 统一表示。一个幂级数同时编码了代数函数、超越函数和周期函数——这件事本身就值得停下来咀嚼。幂级数的设计思路是：把函数"展开"成无限多项式，每一项 $a_n x^n$ 是单项式，系数 $a_n$ 携带函数的全部结构信息。拓展前沿——Borel 定理（Émile Borel）：任何形式幂级数 $\sum a_n x^n$ 都是某个光滑函数 $f \in C^\infty(\mathbb{R})$ 在某点的 Taylor 级数。换句话说，给定任意系数序列 $a_n$（不管增长多快），都存在一个无限可导函数，其 Taylor 展开恰好是这个幂级数——哪怕该幂级数除 $x=0$ 外处处发散。这听起来反直觉：一个处处发散的级数怎么还能是某个函数的 Taylor 展开？答案是那个函数在 $x \neq 0$ 处的 Taylor 级数**不是** $\sum a_n x^n$——Borel 只保证在 0 点匹配所有导数，其他地方函数值和级数值可以毫无关系。这个现象正是 L09-L10 要探讨的"光滑但非解析"函数的入口。

### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#c0392b">Formal Definition（形式定义）</span>

设 $c_n$ 是一个序列，则

```math
\sum_{n=0}^{\infty} c_n x^n
```

是一个 **power series（幂级数）**。

> <span style="color:#7f8c8d;">TBB §10.2, p.404</span>

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">两个问题</span>

- **幂级数何时收敛？**
- **为什么它能给出我们熟悉的函数？**

第二个问题我们下次课对 exponential function（指数函数）回答。

第一个问题的答案来自 root test（根值检验）或 ratio test（比值检验）。

<span style="color:#2471a3;">**[example]**</span> **Example（例）:** 考虑幂级数

```math
\sum_{n=0}^{\infty} \frac{x^n}{n!}.
```

用比值检验，$a_n = \frac{x^n}{n!}$，我们有

```math
\frac{a_{n+1}}{a_n} = \frac{n! \, x^{n+1}}{(n+1)! \, x^n} = \frac{x}{n+1} \to 0.
```

因此该幂级数对**所有** $x$ 都收敛。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 证明策略模板——**"阶乘碾压法"**。对 $e^x$ 的幂级数 $\sum x^n/n!$，比值检验给出 $\left|\frac{a_{n+1}}{a_n}\right| = \frac{|x|}{n+1} \to 0$，不论 $x$ 多大。第一性原理拆解：固定 $x$，分母 $n!$ 的增长最终碾压任何 $x^n$ 的幂增长。为什么？$n! \approx \sqrt{2\pi n}(n/e)^n$（Stirling 公式——你会在概率论 Bertsekas 里正式学到），$n!$ 包含了 $n^n$ 级别的因子，远快于指数 $c^n$。直觉上，分子是固定的长度 $|x|$ 连乘 $n$ 次，分母是 $1,2,3,\dots,n$ 连乘——一旦 $n > |x|$，每个新因子都小于 1，整个比值就加速衰退。结果：收敛半径 $R = \infty$——这是你这节课见到的第一个"处处收敛"的幂级数。这个结论是 L09-L10 指数函数理论的基石：有了处处收敛，你才可以放心地把 $x$ 换成复数 $ix$，逐项比对 $\sum (ix)^n/n!$ 和 $\cos x + i\sin x$ 的展开式，推出 $e^{ix} = \cos x + i\sin x$（欧拉公式）——但这得先建立复数的分析学基础，L09 才会正式动工。顺便说一句：$e^x$ 的幂级数之所以也处处收敛，深层原因是系数 $1/n!$ 衰减得远比任何 $c^{-n}$ 快——阶乘把指数碾压了，这也呼应了根值检验中的 $(1/n!)^{1/n} \approx e/n \to 0$（Stirling 近似给出量级）。

<span style="color:#2471a3;">**[example]**</span> **Example（例）:**

```math
\sum_{n=0}^{\infty} x^n.
```

该级数当 $|x| < 1$ 时收敛，否则发散。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Lim Sup（上极限）</span>

要讨论一般幂级数的收敛性，我们需要序列的 **lim sup（上极限，limit superior）** 概念。定义如下。

设 $a_n$ 是一个序列。如果它不有上界，则我们规定 $\limsup a_n = \infty$。否则，我们由 $a_n$ 定义一个新序列 $b_n$ 如下：

```math
b_n = \sup \{ a_n, a_{n+1}, a_{n+2}, \cdots \}.
```

注意由于我们假设 $a_n$ 们有上界，$b_n$ 们都是实数，且序列 $b_n$ 是**递减（decreasing）**的——它递减是因为

```math
b_n = \sup \{ a_n, a_{n+1}, a_{n+2}, \cdots \} \ge \sup \{ a_{n+1}, a_{n+2}, \cdots \} = b_{n+1}.
```

（对 $b_{n+1}$ 而言，supremum（上确界）是在一个更小的集合上取的。）

由于序列 $b_n$ 递减，它收敛到极限 $b$；若 $b_n$ 不有下界，这个极限可能是 $-\infty$。

### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#c0392b">Definition（lim sup 的定义）</span>

```math
\limsup_{n \to \infty} a_n = \lim_{n \to \infty} b_n = b.
```

> <span style="color:#7f8c8d;">TBB Definition 2.44, §2.13, p.62</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 🎥 *Colding 开门见山给出了动机:* "the reason why we're covering it here is that what if the ratio-- what if these things-- what if the n-th roots-- so you're asking for either the ratio or the n-th root of something to have a limit. But what if it doesn't have a limit?"（翻译：我们在这里讲它的原因是——比值检验和根值检验都要求比值或 $n$ 次根有极限，可如果极限不存在怎么办？）$\limsup$（上极限，拉丁名 *limes superior*）就是"极限不存在时的代替品"。定义一个序列 $x_n$ 的上极限分两步：先取"尾巴集合" $\{x_k: k \ge n\}$ 的上确界，记为 $B_n = \sup_{k\ge n} x_k$；再取 $n\to\infty$ 时 $B_n$ 的极限。关键是：随着 $n$ 增大，尾巴越来越短，上确界 $B_n$ 只能**不增**——你去掉了前面的项，留下的"最大值"不会变大。所以 $(B_n)$ 是一个单调递减（不严格）的序列，由 L05 MCT（更准确地说，单调递减 + 有下界 ⇒ 收敛）它一定有极限——这个极限就是 $\limsup x_n$。我管这个叫**"尾巴上确界"**直觉：$\limsup$ 提取了一个序列"最终能达到的最大聚集水平"。对称地，$\liminf$ 是"尾巴下确界"的单调递增极限，提取"最终能达到的最小聚集水平"。当 $\limsup = \liminf$ 时常规极限存在且等于这个公共值——所以 $\limsup$ 是极限概念的自然推广。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Radius of Convergence（收敛半径）</span>

回到幂级数。假设

```math
\sum_{n=0}^{\infty} a_n x^n
```

是一个幂级数。令

```math
R = \frac{1}{\limsup_{n \to \infty} |a_n|^{\frac{1}{n}}}.
```

$R$ 被称为 **radius of convergence（收敛半径）**。

> <span style="color:#7f8c8d;">TBB §10.2, p.404（Cauchy–Hadamard 公式）</span>

**Convention（约定）:** 若 $\limsup_{n \to \infty} |a_n|^{\frac{1}{n}} = 0$，则称收敛半径为 $\infty$。若 $\limsup_{n \to \infty} |a_n|^{\frac{1}{n}} = \infty$，则令 $R = 0$。

由根值检验现在可以证明：

**幂级数在 $|x| < R$ 时收敛，在 $|x| > R$ 时发散。**

$|x| = R$ 的情形必须**逐例分析（case by case）**。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Cauchy–Hadamard 公式 $R = 1/\limsup |a_n|^{1/n}$ 不是背出来的，它是把根值检验直接喂给幂级数 $\sum a_n x^n$ 的每一项的必然产物。推导：对任意固定的 $x$，根的极限是 $\limsup |a_n x^n|^{1/n} = |x| \cdot \limsup |a_n|^{1/n}$。根值检验说：$|x| \cdot \limsup |a_n|^{1/n} < 1$ 则收敛，$>1$ 则发散。把 $|x|$ 解出来：$|x| < \frac{1}{\limsup |a_n|^{1/n}} = R$ 时收敛，$|x| > R$ 时发散。公式就这样推导出来——它不过是根值检验在幂级数上的直接翻译。历史上，Cauchy 1821 年在 *Cours d'Analyse* 中给出了这个公式但长期被忽视，直到 Hadamard 1888 年独立重新发现（1892 年收入其博士论文），此后才被广泛使用——所以冠名为 Cauchy–Hadamard。🎥 *Colding 的 limsup 动机正指向这个:* "what if it doesn't have a limit?"（翻译：如果极限不存在怎么办？）——$\limsup$ 保证即使 $\lim |a_n|^{1/n}$ 不存在，收敛半径仍然有唯一的确定值。边界 $|x| = R$ 是个微妙地带：同一个 $R=1$，级数 $\sum x^n/n$ 在 $x=1$ 发散（调和级数）但在 $x=-1$ 收敛（交错调和级数）。结论：收敛半径定理只对 $|x| < R$ 和 $|x| > R$ 打包判定，$|x| = R$ 的圆周上必须逐例分析——就像根值检验自己在 $r=1$ 时"失明"一样，收敛半径在边界上也"失明"。

---

<span style="color:#7f8c8d;">References（参考文献）:</span>

- [TBB] B.S. Thomson, J.B. Bruckner, A.M. Bruckner, *Elementary Real Analysis*, 2nd edition
- TBB 下载：<https://classicalrealanalysis.info/com/documents/TBB-AllChapters-Landscape.pdf>（屏幕优化版）/ <https://classicalrealanalysis.info/com/documents/TBB-AllChapters-Portrait.pdf>（打印优化版）

<span style="color:#7f8c8d;">MIT, Dept. of Math., 77 Massachusetts Avenue, Cambridge, MA 02139-4307 · MIT OpenCourseWare: https://ocw.mit.edu · 18.100B Real Analysis, Spring 2025</span>
