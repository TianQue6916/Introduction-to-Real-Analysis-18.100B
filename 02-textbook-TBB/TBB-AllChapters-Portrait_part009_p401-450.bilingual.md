# <span style="color:#c0392b;">Elementary Real Analysis（初等实分析）</span>

> <span style="color:#7f8c8d;">行内双语翻译 · Part009（书页 385–434）</span>
> <span style="color:#7f8c8d;">范围：第 9 章 Sequences and Series of Functions（函数列与函数项级数）§9.4 末尾（Dini 定理）– §9.8 + 第 10 章 Power Series（幂级数）§10.1–§10.8</span>
> <span style="color:#7f8c8d;">源文件：TBB-AllChapters-Portrait_part009_p401-450.pdf（书页 = PDF 页 + 384）</span>
> <span style="color:#7f8c8d;">Second Edition (2008) · Brian S. Thomson, Judith B. Bruckner, Andrew M. Bruckner</span>
> <span style="color:#7f8c8d;">**格式：** 中文主体 + `English term（中文翻译）` 嵌入 · 深红标题 · 蓝色标签 · fenced math block · 无英文原句</span>
> <span style="color:#7f8c8d;">**习题区**（各节 Exercises、§9.9 Challenging Problems、NOTES 提示区）按约定跳过不收录</span>

---


<!-- ===== 书页 385（PDF 页 1）===== -->

Part009 · 书页 385 行内双语翻译

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Section 9.4 Uniform Convergence and Continuity（一致收敛与连续性）</span>

### <span style="color:#2471a3;">**[corollary]**</span> <span style="color:#c0392b">Corollary 9.23（推论 9.23）</span>
> <span style="color:#7f8c8d;">TBB §9.4, p.385</span>

若级数 $\sum_{k=1}^{\infty} f_k$ 在区间 $I$ 上uniform convergence（一致收敛）于 $f$，且其中每个函数 $f_k$ 都在 $I$ 上 continuous（连续），则 $f$ 在 $I$ 上连续。

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 本推论直接由 Theorem 9.22（定理 9.22）推出。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">9.4.1 Dini's Theorem（Dini 定理）</span>

> **高级小节（Advanced section）——可略读（may be omitted）。**

请注意，Theorem 9.22 为 limit function（极限函数）$f$ 的连续性提供了一个 sufficient condition（充分条件）。
这一条件并非 necessary（必要）的。
（Example 9.6（例 9.6）中的序列收敛到 zero function（零函数），该函数是连续的，即使该收敛并不是一致的。）
但在某些情形下，一致收敛却是必要的，正如 Theorem 9.24 所示。
（另请参见 Exercise 9.4.6。）
本定理归功于 Ulisse Dini（1845–1918），它给出了一种条件：在此条件下，一列连续函数的 pointwise convergence（逐点收敛）到一个连续函数必为一致收敛。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 9.24 (Dini)（定理 9.24，Dini 定理）</span>
> <span style="color:#7f8c8d;">TBB §9.4, p.385</span>

设 $\{ f_n \}$ 是区间 $[a, b]$ 上的一列连续函数，并假设对每个 $x \in [a, b]$ 以及所有 $n \in \mathbb{N}$ 都有：
```math
f_n(x) \geq f_{n+1}(x),
```
再假设对所有 $x \in [a, b]$ 都有：
```math
f(x) = \lim_n f_n(x).
```
若 $f$ 连续，则该收敛是一致的。

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 假设该收敛不是一致的。
>
> 那么 $\max_{x \in [a,b]} \left( f_n(x) - f(x) \right)$ 当 $n \to \infty$ 时并不趋近于零（参见 Exercise 9.3.12）。
>
> 因此存在 $c > 0$，使得对无穷多个 $n \in \mathbb{N}$ 都有 $\max_{x \in [a,b]} \left( f_n(x) - f(x) \right) > c > 0$。
>
> 现在，对每个 $n \in \mathbb{N}$，$f_n - f$ 是连续的，因此它在某个点 $x_n \in [a, b]$ 处取到最大值。
>
> 由 Bolzano-Weierstrass theorem（Bolzano-Weierstrass 定理），我们可以从序列 $\{ x_n \}$ 中选出 subsequence（子列）$\{ x_{n_k} \}$，使得 $\{ x_{n_k} \}$ 收敛到某点 $x_0 \in [a, b]$。
>
> 注意，我们必然有 $f_{n_k}(x_{n_k}) - f(x_{n_k}) > c$ 对所有 $k \in \mathbb{N}$ 成立。
>
> 由于我们的假设是对所有 $n \in \mathbb{N}$ 与 $x \in [a, b]$ 都有 $f_n(x) \geq f_{n+1}(x)$，我们推出 $f_n(x_{n_k}) - f(x_{n_k}) > c$ 对每个 $n \leq n_k$ 成立。
>
> 现在固定 $n$ 并令 $k \to \infty$。
>
> 利用函数 $f_n - f$ 的连续性，我们得到 $f_n(x_0) - f(x_0) \geq c$ 对所有 $n \in \mathbb{N}$ 成立。
>
> 但这不可能，因为由假设 $f_n(x_0) \to f(x_0)$。
>
> 于是，「收敛不是一致的」这一假设导致了矛盾。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 推论 9.23 表面上是「连续函数的级数之和仍连续」，本质是一条 **极限交换律**：它把 $\lim_{N\to\infty}$（部分和取极限）与「逐点取值」这两个运算的次序颠倒了过来。你在离散数学 6.042J 里已经反复见过同一母题——有限运算与无限运算交换次序是需要证明的特权（级数重排、分配律与无限和）。这里第一性原理地问：为什么逐点收敛不够？因为「每个 $x$ 处级数都收敛」只给了逐点信息，而连续性要求「$x$ 一动、函数值不乱跳」，这需要误差在整段区间上一致地小。一致收敛正是把「逐点小误差」升级为「全局小误差」的机制。从证明策略看，此推论背后是 Theorem 9.22 的 **ε/3 论证**（先取 $N$ 使 $|f_n(x)-f(x)|<\varepsilon/3$ 对一切 $x$ 成立，再利用 $f_n$ 的连续性各控制 $\varepsilon/3$）：这是分析学最重要的「预算分配」模板，你在 CLRS 里做分治复杂度分析时也是同样思路——把总误差预算切给各个来源。🎥 教授在课上强调一致收敛的本质时说的正是：「And again, the uniformness, it holds for all x. You can use the same capital N for all x.」（翻译：再强调一次，这个一致性是对所有 x 成立的——你可以对所有的 x 使用同一个大写 N。）这句话抓住了逐点与一致的全部差别：$N$ 能不能选成与 $x$ 无关。
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Dini 定理（1878 年，由意大利数学家 Ulisse Dini（1845–1918）证明）是本章第一个「反向」定理：通常一致收敛保证极限连续，这里却用「极限连续 + 单调」反过来推出一致收敛。为什么能反过来？三个条件各自堵住一条退路：极限 $f$ 连续，把「极限函数」的形状锁死（没有悬崖）；$\{f_n\}$ 单调递减，把「逼近过程」锁死（函数只能从上往下压，不能上下乱窜）；$[a,b]$ 紧致，把「最坏偏差点」锁死（Bolzano–Weierstrass 保证能取出收敛子列）。三者合起来，逐点收敛就被「升级」成一致收敛。证明走反证：若不一致，则每个 $n$ 处存在「最坏点」$x_n$ 使偏差 $>c$；取子列 $x_{n_k}\to x_0$，由单调性把偏差从 $x_{n_k}$「传染」到 $x_0$（$f_n(x_{n_k})-f(x_{n_k})>c$ 对所有 $n\le n_k$ 成立，令 $k\to\infty$ 得 $f_n(x_0)-f(x_0)\ge c$），与逐点收敛矛盾。单调性为什么不可少？因为去掉它，最坏偏差点可以「追着」$f_n-f$ 的抖动满区间乱跑，逐点收敛仍然可能、但最坏偏差永不消失——例 9.6 的尖峰序列就是「不单调却逐点收敛到 0、且最坏点无穷游走」的活标本。这里可以做 CSAPP 式类比：单调序列像二分查找的区间收缩，每步把「坏位置」范围收窄，最终钉住所有点；普通逐点收敛则像哈希表冲突，坏点散落各处无法统一处理。Dini 定理也是「闭区间分析这么好用」的第一课——紧致性是「存在统一常数/统一 $N$」的发动机。

---

<!-- ===== 书页 386（PDF 页 2）===== -->

Part009 · 书页 386 行内双语翻译

<span style="color:#2471a3;">**[example]**</span> **Example 9.25（例 9.25）**
> <span style="color:#7f8c8d;">TBB §9.4, p.386</span>

一列连续函数 $f_n(x) = x^n$ 在区间 $[0, 1]$ 上

monotone convergence（单调收敛）到某个函数 $f$。

但该函数 $f$——正如我们此前所看到的——在 $x = 1$ 处是 discontinuous（不连续）的，

因此我们立刻可以断定：该收敛不可能是 uniform（一致）的。

不过，由 Dini's theorem（Dini 定理）可知：对任意 $0 < b < 1$，

由于 $f$ 在区间 $[0, b]$ 上连续，

收敛在 $[0, b]$ 上必然是一致收敛的。

<!-- 本页其余部分为 Exercises 9.4.1–9.4.10 习题区，按 worker_spec 约定跳过。-->

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 例 9.25 把上一页的 Dini 定理落到了具体函数上：$f_n(x)=x^n$ 在 $[0,1]$ 上单调递减地逐点收敛到不连续函数 $f$（$x<1$ 时为 0，$x=1$ 时为 1），因此收敛「必然」不可能是一致的——这正是 Theorem 9.22 的逆否命题：若极限函数不连续，则收敛必非一致。同时，限制到 $[0,b]$（$0<b<1$）后 $f\equiv 0$ 连续，Dini 定理立刻断言一致收敛——事实上 $\max_{[0,b]}x^n=b^n\to 0$，用直接计算也能验证。这个例子值得你建立直觉：逐点收敛是「每个固定 $x$ 处数列 $x^n$ 趋于 0」，而一致收敛要求「一整条曲线 $x^n$ 同时贴近横轴」。$x^n$ 在 $x=1$ 附近的「拖尾」（任意靠近 1 的点都要很晚才被压下去）正是逐点收敛与一致收敛之间那道鸿沟的可视化。这与你的二分搜索脚手架有关：检查「$x$ 靠近 1 时收敛变慢」相当于在搜索区间端点的退化情形——算法里你也知道，退化输入（如已排序数组的边界）才是考验最坏情况分析的地方，逐点收敛正是「平均表现好」而一致收敛是「最坏情形可控」。🎥 教授在 V20 中就是用 $x^n$ 引入这个例子的：「So this is my fn and my function f... This is equal to 0 if x is bigger or equal to 0 but strictly less than 1. And it's 1 if x is equal to 1. So of course, this function f is not continuous.」（翻译：这就是我的 fn 和我的函数 f……当 x 大于等于 0 但严格小于 1 时它等于 0，当 x 等于 1 时它等于 1。所以当然，这个函数 f 是不连续的。）

---

<!-- ===== 书页 387（PDF 页 3）===== -->

Part009 · 书页 387 行内双语翻译

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">9.5 Uniform Convergence and the Integral（一致收敛与积分）</span>

<!-- 本页顶部为 Exercises 9.4.11–9.4.12 习题区（含 NOTES 提示），按 worker_spec 约定跳过。-->

微积分课程的学生经常学到下面这个简单计算。
geometric series（几何级数）
```math
\frac{1}{1-t} = \sum_{k=0}^{\infty} t^k \tag{10}
```
在区间 $(-1, 1)$ 上成立。
对任意 $x < 1$，将两边关于 $t$ 在区间 $[0, x]$ 上积分，即得
```math
-\log(1-x) = \int_0^x \frac{1}{1-t}\,dt = \sum_{k=0}^{\infty} \frac{x^{k+1}}{k+1} .
```
事实上这个恒等式是成立的，它为对数函数（logarithm function）提供了一个级数展开式。
但这个做法真的能被严格证明吗？

一般地，我们是否知道：若在区间 $[a, b]$ 上有 $f(x) = \sum_{n=0}^{\infty} f_n(x)$，则
```math
\int_a^b f(x)\,dx = \sum_{n=0}^{\infty} \int_a^b f_n(x)\,dx
```
必然成立吗？

事实上，我们在 Section 9.3（§9.3）中已经观察到：在十九世纪早期，一些杰出的数学家想当然地认为，对收敛的函数无穷级数进行逐项积分（term-by-term integration）是允许的。
Fourier、Cauchy 和 Gauss 都是如此。
以可积函数序列为背景的 Example 9.6（例 9.6）表明，这些数学家错了。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">9.5.1 Sequences of Continuous Functions（连续函数序列）</span>

大约在十九世纪中叶，Weierstrass 证明了：当可积函数的级数一致收敛（uniformly convergent）时，逐项积分是允许的。
让我们首先对连续函数序列验证这一结果。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 本节开头的历史故事值得放慢速度读：十九世纪初，Fourier、Cauchy、Gauss 这些一流数学家都想当然地认为「收敛级数可以逐项积分」。为什么他们会错？因为他们把级数等同于「表达式」——既然 $\frac{1}{1-t}$ 和 $\sum t^k$ 是同一个解析式子，积分就该一回事。错在：等式是逐点成立的，而积分是对整段区间求整体——逐点收敛只保证「每个 $x$ 的值被逼近」，不保证「整块面积被逼近」。第一性原理地问：$\int\sum=\sum\int$ 本质是「取极限」与「取积分」两个线性运算换序，而泛函分析的基本教训是——**无限线性运算换序永远需要额外的「紧致性」条件**，这里的一致收敛正是它。例 9.6 的尖峰序列（$2n$ 高的尖峰压到 $[0,1]$ 上）逐点收敛到 0，但每个 $f_n$ 下的面积恒为 1，$\int f_n\to 1\ne 0=\int 0$。这个「尖峰」意象请刻进脑子：它是「逐点收敛 ≠ 积分收敛」的终极反例，也是你日后学测度论（Fatou 引理、Lebesgue 控制收敛）反复重逢的原形。另注意 $\frac{1}{1-t}=\sum t^k$ 在任意 $[0,x]$（$x<1$）上一致收敛，逐项积分在「局部一致收敛」下安全——很多看似危险的换序，把区间缩紧到一致收敛成立后就合法了，这与 CLRS 分治的「规模归约」同一哲学。

---

<!-- ===== 书页 388（PDF 页 4）===== -->

Part009 · 书页 388 行内双语翻译
### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 9.26（定理 9.26）</span>
> <span style="color:#7f8c8d;">TBB §9.5, p.388</span>

假设对所有 $x \in [a, b]$ 都有 $f(x) = \lim_{n\to\infty} f_n(x)$，且每个函数 $f_n$ 在 $[a, b]$ 上连续，并且该收敛是uniform convergence（一致收敛）。
那么
```math
\int_a^b f(x)\,dx = \lim_{n\to\infty} \int_a^b f_n(x)\,dx .
```

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 由 Theorem 9.22（定理 9.22），$f$ 连续，因此 $\int_a^b f(x)\,dx$ 存在。
> 我们必须证明 $\int_a^b f_n(x)\,dx \to \int_a^b f(x)\,dx$。
> 设 $\varepsilon > 0$，我们希望找到 $N \in \mathbb{N}$，使得对所有 $n \geq N$ 都有 $\left| \int_a^b f_n(x)\,dx - \int_a^b f(x)\,dx \right| < \varepsilon$。
> 对任意 $n \in \mathbb{N}$，我们计算得到
> ```math
> \left| \int_a^b f_n(x)\,dx - \int_a^b f(x)\,dx \right|
> = \left| \int_a^b \left[ f_n(x) - f(x) \right] dx \right|
> \leq \int_a^b \left| f_n(x) - f(x) \right| dx
> \leq \int_a^b \max_{x \in [a,b]} \left| f_n(x) - f(x) \right| dx
> \leq (b-a) \max_{x \in [a,b]} \left| f_n(x) - f(x) \right| .
> ```
> 由于 $f_n \to f$ 在 $[a, b]$ 上一致收敛，存在 $N \in \mathbb{N}$，使得对所有 $n \geq N$ 有
> ```math
> \max_{x \in [a,b]} \left| f_n(x) - f(x) \right| < \frac{\varepsilon}{b-a} .
> ```
> 于是，对 $n \geq N$，我们有
> ```math
> \left| \int_a^b f_n(x)\,dx - \int_a^b f(x)\,dx \right|
> \leq (b-a) \frac{\varepsilon}{b-a} = \varepsilon ,
> ```
> 正如所要证明的。

将该定理应用于级数的部分和（partial sum）$S_n$，我们就可以把这一结果表述为针对级数的形式。

### <span style="color:#2471a3;">**[corollary]**</span> <span style="color:#c0392b">Corollary 9.27（推论 9.27）</span>
> <span style="color:#7f8c8d;">TBB §9.5, p.388</span>

若由连续函数组成的无穷级数 $\sum_{k=0}^{\infty} f_k$ 在区间 $[a, b]$ 上一致收敛到函数 $f$，则 $f$ 也是连续的，并且
```math
\int_a^b f(x)\,dx = \sum_{k=0}^{\infty} \int_a^b f_k(x)\,dx .
```

<span style="color:#2471a3;">**[example]**</span> **Example 9.28（例 9.28）**
> <span style="color:#7f8c8d;">TBB §9.5, p.388</span>

让我们来严格证明在本节引言中做过的那些计算。
几何级数
```math
\frac{1}{1-t} = \sum_{k=0}^{\infty} t^k \tag{11}
```
在区间 $(-1, 1)$ 上逐点收敛（pointwise convergence）。
设 $0 < x < 1$。
由 Weierstrass M-test（Weierstrass M 判别法）可知，该级数在 $[0, x]$ 上一致收敛。
级数中的每一项都是连续的。
因此，我们可以应用定理进行逐项积分，正如在微积分课程中可能看到的那样。
于是
```math
\int_0^x \frac{1}{1-t}\,dt = \sum_{k=0}^{\infty} \frac{x^{k+1}}{k+1} .
```

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Theorem 9.26 的证明是全章最短也最优雅的一个，值得当作「范数控制」模板来读。关键不等式只有一行：$\left|\int_a^b f_n-\int_a^b f\right|\le\int_a^b|f_n-f|\le(b-a)\max_{[a,b]}|f_n-f|$——「积分绝对值 ≤ 绝对值积分 ≤ 长度 × 最大偏差」，一步把函数级偏差化为实数级偏差，而一致收敛恰好保证实数偏差 $<\varepsilon/(b-a)$。第一性原理看，这证明积分是一个 **Lipschitz 线性泛函**：$C[a,b]$（sup 范数）到 $\mathbb{R}$ 的映射 $f\mapsto\int_a^b f$ 满足 $\left|\int f-\int g\right|\le(b-a)\|f-g\|_\infty$，与你 18.065 学的矩阵误差传播 $\|Ax-Ay\|\le\|A\|\|x-y\|$ 完全同构，$b-a$ 就是放大因子。推论 9.27 只是把「序列」翻译成「级数」（取部分和 $S_N$），这是分析学序列↔级数互译的标准套路。Example 9.28 则给你一个可操作的收获：几何级数 $\sum t^k$ 在 $[0,x]$ 上满足 Weierstrass M-test 的条件（$|t^k|\le x^k$ 且 $\sum x^k$ 收敛），因此逐项积分合法，得到 $-\log(1-x)=\sum x^{k+1}/(k+1)$——你在微积分里背过的对数级数，现在终于有了严格依据。🎥 教授预告这种「用一致收敛换积分/求导自由」的思想时说：「if you have uniform convergence, then it becomes very easy... a lot of operations, like integration and differentiation, you can do that over here.」（翻译：如果你有一致收敛，那么事情就变得非常容易……很多运算，比如积分和微分，都可以在这里直接做。）

---

<!-- ===== 书页 389（PDF 页 5）===== -->

Part009 · 书页 389 行内双语翻译

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">9.5 Uniform Convergence and the Integral（一致收敛与积分）</span>

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">9.5.2 Sequences of Riemann Integrable Functions（Riemann 可积函数列）</span>

<span style="color:#7f8c8d">*提高章节（Enrichment section）。可省略不读。*</span>

在 Theorem 9.26 中，我们要求函数 $f_n$ continuous（连续）。
现在我们不妨削弱对这些函数的假设：只要求它们可积（integrable），但仍要求序列 $\{f_n\}$ uniform convergence（一致收敛）到 $f$。
我们注意到，其证明在所有方面都是相同的。
因此，若一个一致收敛的可积函数序列收敛到一个可积函数，我们就可以对该序列逐项积分（term-by-term integration）。
我们的下一个定理表明，可积函数的一致极限（uniform limit）必然可积，于是得到 Theorem 9.26 的如下推广。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 9.29（定理 9.29）</span>
> <span style="color:#7f8c8d;">TBB §9.5, p.389</span>

设 $\{f_n\}$ 是区间 $[a,b]$ 上的 Riemann Riemann integrable（可积）函数序列。
若 $f_n \to f$ 在 $[a,b]$ 上一致收敛，则 $f$ 在 $[a,b]$ 上 Riemann 可积，并且

```math
\int_a^b f(x)\,dx = \lim_{n} \int_a^b f_n(x)\,dx.
```

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 如果我们事先知道 $f$ 可积，那么 Theorem 9.26 的证明可以原样照搬。
> 因此我们只需证明极限函数（limit function）$f$ 在 $[a,b]$ 上可积。
> 一种证法（见 Exercise 9.5.7）是证明 $f$ 有界，并且除一个零测集（set of measure zero）外处处连续。
> 由 Theorem 8.17 即得 $f$ 是 Riemann 可积的。
>
> 我们也可以给出另一种证明：对任意 $\varepsilon > 0$，构造具有 Exercise 8.6.5 所述性质的阶梯函数（step function）。
> 由于这一证明早在十九世纪就为数学家们所掌握——他们当时还不知晓零测集的概念——因此即便仅仅出于历史原因，也值得在此呈现。
>
> 设 $\varepsilon > 0$。我们希望找到阶梯函数 $L$ 与 $U$，使得对所有 $x \in [a,b]$ 成立 $L(x) \le f(x) \le U(x)$，并且
>
> ```math
> \int_a^b [U(x) - L(x)]\,dx < \varepsilon.
> ```
>
> 我们将分三个自然的步骤来构造函数 $L$ 与 $U$：
> 第一步，用某个函数 $f_N$ 来近似 $f$；
> 第二步，得到相应的阶梯函数 $L_N$ 与 $U_N$，用来近似 $f_N$；
> 第三步，对 $L_N$ 与 $U_N$ 作修改，从而得到 $L$ 与 $U$。
> 下面我们就按上述计划进行。
>
> (i) 由于 $f_n \to f$ 一致收敛，存在 $N \in \mathbb{N}$，使得对所有 $x \in [a,b]$ 成立
>
> ```math
> |f_N(x) - f(x)| \le \frac{\varepsilon}{4(b-a)}.
> ```
>
> (ii) 由假设，$f_N$ 可积，因此存在阶梯函数 $L_N$ 与 $U_N$，使得对所有 $x \in [a,b]$ 成立 $L_N(x) \le f_N(x) \le U_N(x)$，并且
>
> ```math
> \int_a^b [U_N(x) - L_N(x)]\,dx < \frac{\varepsilon}{2}.
> ```


---

<!-- ===== 书页 390（PDF 页 6）===== -->

Part009 · 书页 390 行内双语翻译
### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">9.5 Uniform Convergence and the Integral（一致收敛与积分）</span>
> (iii) 我们如下定义阶梯函数 $U$ 与 $L$：对所有 $x \in [a,b]$，令
>
> ```math
> L(x) = L_N(x) - \frac{\varepsilon}{4(b-a)}, \qquad U(x) = U_N(x) + \frac{\varepsilon}{4(b-a)}.
> ```
>
> 于是有
>
> ```math
> L(x) < L_N(x) - |f(x) - f_N(x)| \le f(x) \le U_N(x) + |f(x) - f_N(x)| < U(x),
> ```
>
> 并且
>
> ```math
> \begin{aligned}
> \int_a^b [U(x) - L(x)]\,dx
> &= \int_a^b \left\{ [U_N(x) - L_N(x)] + \frac{\varepsilon}{2(b-a)} \right\} dx \\
> &= \int_a^b [U_N(x) - L_N(x)]\,dx + \int_a^b \frac{\varepsilon}{2(b-a)}\,dx \\
> &< \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon,
> \end{aligned}
> ```
>
> 恰如所要证明的。<span style="color:#7f8c8d">$\blacksquare$</span>
### <span style="color:#2471a3;">**[corollary]**</span> <span style="color:#c0392b">Corollary 9.30（推论 9.30）</span>
> <span style="color:#7f8c8d;">TBB §9.5, p.390</span>
若可积函数的无穷级数（infinite series）$\sum_{k=0}^{\infty} f_k$ 在区间 $[a,b]$ 上一致收敛到函数 $f$，则 $f$ 也可积，并且

```math
\int_a^b f(x)\,dx = \sum_{k=0}^{\infty} \int_a^b f_k(x)\,dx.
```
<span style="color:#2471a3;">**[example]**</span> **Example 9.31（例 9.31）**
> <span style="color:#7f8c8d;">TBB §9.5, p.390</span>

设 $f_n(x) = e^{-nx^2}$。
则对每个 $x \in [1,2]$ 及每个 $n \in \mathbb{N}$，有 $0 < e^{-nx^2} \le e^{-n}$，且 $e^{-n} \to 0$，所以 $f_n \to 0$ 在 $[1,2]$ 上一致收敛。
由此得到

```math
\lim_{n} \int_1^2 e^{-nx^2}\,dx = \int_1^2 0\,dx = 0.
```
**Note（注记）.**

我们以一个简短的注记结束本节，探讨我们的主要定理在比一致收敛更弱的假设下是否依然成立。
一个函数序列 $\{f_n\}$ 有可能在 $[a,b]$ 上逐点收敛（pointwise convergence，但非一致收敛）到函数 $f$，却仍然有

```math
\lim_{n} \int_a^b f_n(x)\,dx = \int_a^b f(x)\,dx. \tag{12}
```
例如，假设我们修改 Example 9.6 中的函数，使 $f_n(1/(2n)) = 1$ 而不是 $f_n(1/(2n)) = 2n$。
此时仍有 $f_n \to 0$ 逐点收敛（但非一致收敛），不过现在

```math
\int_0^1 f_n(x)\,dx \to 0.
```
这些函数构成一个一致有界（uniformly bounded）的函数序列：即存在常数 $M$（本例中 $M = 1$），使得对所有 $n \in \mathbb{N}$ 及所有 $x \in [0,1]$ 都有 $|f_n(x)| \le M$。
一个定理（其证明超出本章范围）断言：若一个一致有界的可积函数序列 $\{f_n\}$ 逐点收敛到……

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Theorem 9.29 把 9.26 从「连续函数」推广到「Riemann 可积函数」，它的证明（构造阶梯函数上下夹逼）是分析学经典的三步法，值得提炼成模板：**近似 → 逼近 → 修正**。（i）先用一致收敛找一个「足够好的」$f_N$ 近似 $f$（误差 $\le\varepsilon/(4(b-a))$）；（ii）利用 $f_N$ 的可积性，用阶梯函数 $L_N\le f_N\le U_N$ 夹逼（积分差 $<\varepsilon/2$）；（iii）把 $L_N,U_N$ 各向外扩一层 $\varepsilon/(4(b-a))$，抵消近似误差。每一步都把总预算 $\varepsilon$ 切一刀，最后加起来正好闭合。这与你 CSAPP 里浮点误差分析的思维同构：总误差预算分摊给每一层的近似，各层互相抵消/叠加都要能兜住。为什么非用阶梯函数不可？因为 Riemann 积分的定义本身就是「阶梯函数上下和逼近」，而定理要证的「$f$ 可积」最直接的证据就是找到一对几乎重合的阶梯函数夹逼——这等于把「$f$ 可积」这个抽象概念翻译成了「可被阶梯函数任意逼近」这个可操作的构造。另注意书中的历史注记：这种证明在十九世纪就已被掌握，因为它的全部工具（一致收敛 + 阶梯函数）都不需要「零测集」这个现代概念——这是理解数学史的一个绝佳剖面：Riemann 可积性理论先于「测度」语言成形，直到 Lebesgue 才彻底换了一副眼镜。例 9.31（$e^{-nx^2}$）则说明定理的威力：一致收敛到 0 立刻给出 $\int_1^2 e^{-nx^2}\to 0$，甚至不必真的算出积分。

---

<!-- ===== 书页 391（PDF 页 7）===== -->

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">9.5 Uniform Convergence and the Integral（一致收敛与积分）</span>

若 $f$ 是 $[a,b]$ 上的 integrable function（可积函数），则恒等式 (12) 成立。我们无法在该定理中去掉 $f$ 可积性的假设。例如，若 $\{r_n\}$ 是 $[0,1]$ 中有理数的一个 enumeration（枚举），并且当 $x = r_1, r_2, \ldots, r_n$ 时 $f_n(x) = 1$、其余情形为 0，则

```math
\lim_{n\to\infty} f_n(x) = f(x) =
\begin{cases}
1, & \text{if } x \in \mathbb{Q}\cap[0,1],\\
0, & \text{if } x \in [0,1]\setminus\mathbb{Q},
\end{cases}
```

且根据 Exercise 9.2.3，$f$ 在 $[0,1]$ 上不可积。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">9.5.3 Sequences of Improper Integrals（反常积分序列）</span>

迄今为止，我们研究的是有限区间 $[a,b]$ 上函数常义积分的极限。如果积分要在无穷区间上取，那会怎样？更具体地说，我们只问下列公式是否成立：

```math
\lim_{n\to\infty}\int_a^\infty f_n(t)\,dt = \int_a^\infty f(t)\,dt \qquad (f_n \to f),
```

以及，在 $f = \sum_{k=1}^{\infty} g_k$ 的情形下，

```math
\sum_{k=1}^{\infty}\int_a^\infty g_k(t)\,dt = \int_a^\infty f(t)\,dt .
```

一个快速而草率的回答是：对于 pointwise convergence（逐点收敛）我们几乎不指望这些成立，但 uniform convergence（一致收敛）当然就足够了。但这些积分涉及一个额外的 limit operation（极限运算），因此我们需要格外小心。事实上，下面的例子表明一致收敛远远不够。这里的问题并不仅仅是收敛的「光滑性」。

<span style="color:#2471a3;">**[example]**</span> **Example 9.32（例 9.32）** 设 $f_n(x)$ 对所有 $x \in [0,n]$ 定义为 $1/n$，而对 $x > n$ 定义为 0。那么序列 $\{f_n\}$ 在区间 $[0,\infty)$ 上一致收敛于零。但积分并不收敛到零（正如我们本会期望的那样），因为对所有 $n$ 都有 $\int_0^\infty f_n(t)\,dt = 1$。
> <span style="color:#7f8c8d;">TBB §9.5, p.391</span>

我们还能附加什么条件，使得连同一致收敛一起，能够把极限运算移入积分号内、处理 $\lim_{n\to\infty}\int_0^\infty f_n(t)\,dt$？定理中所施加的条件只是要求：所有函数都被某个本身可积的函数所控制（controlled）或支配（dominated）。在 Example 9.32 中注意，不可能存在 $[0,\infty)$ 上的可积函数 $g$，使得对所有 $n$ 和 $x$ 都有 $f_n(x) \le g(x)$。这类定理称为 dominated convergence theorems（控制收敛定理）。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 本节末尾的注记预告了整章最深刻的主题：一致收敛并非「积分换序」的必要条件。例 9.6 的改版（把尖峰从 $2n$ 高改为 $1$ 高）说明：只要序列一致有界且逐点收敛到可积函数，$\int f_n\to\int f$ 照样成立——这是「有界逐点收敛」版本，是未来 Lebesgue dominated convergence theorem（控制收敛定理）的雏形。而紧随其后的反例（$f_n$ 在有理数枚举的前 $n$ 个点取 1）则给出极限行为的另一面：逐点极限 $f=\mathbf{1}_{\mathbb{Q}\cap[0,1]}$（有理数指示函数）在 $[0,1]$ 上处处不连续（每个小区间里既有有理数又有无理数），由 §8 的判据不可积。这个函数你以后会反复遇到——Dirichlet 函数，实变函数论的头号反例。第一性原理洞察：**Riemann 积分对「震荡得太多」的函数无能为力，因为 Riemann 和只能捕获「几乎处处」的行为，而 Dirichlet 函数在每一点都在震荡**。它也说明了为什么「逐点极限保持可积性」需要一个更强的条件（有界、支配……）——积分号下的极限交换，本质上是一场「谁先取极限」的博弈：先积分后取极限与先取极限后积分，结果可能不同，而支配/有界条件正是让两者打平的「裁判」。这里埋的种子会在你学 Lebesgue 积分（或学概率论中的期望换序）时爆发，值得现在就在笔记里标记。

---

<!-- ===== 书页 392（PDF 页 8）===== -->

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 9.33（定理 9.33）</span>
> <span style="color:#7f8c8d;">TBB §9.5, p.392</span>

设 $\{f_n\}$ 是区间 $[a,\infty)$ 上的一列 continuous function（连续函数），使得 $f_n \to f$ 在任何区间 $[a,b]$ 上一致收敛。假设存在 $[a,\infty)$ 上的连续函数 $g$，使得对所有 $a \le x$ 与所有 $n$ 都有 $|f_n(x)| \le g(x)$。再假设积分 $\int_a^\infty g(x)\,dx$ 存在。则

```math
\lim_{n\to\infty}\int_a^\infty f_n(t)\,dt = \int_a^\infty f(t)\,dt .
```

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 第一步，让我们证明 $f$ 在 $[a,\infty)$ 上可积。$f$ 当然是连续的，因为它是连续函数列的一致极限。由于每个 $|f_n(x)| \le g(x)$，随之可得 $|f(x)| \le g(x)$。于是我们检验
>
> ```math
> \left|\int_c^d f(t)\,dt\right| \le \int_c^d |f(t)|\,dt \le \int_c^d g(t)\,dt .
> ```
>
> 由于 $g$ 可积，由反常积分的 Cauchy criterion（Cauchy 判别法）（见 Exercise 8.5.11）可知，当 $c$ 与 $d$ 很大时积分 $\int_c^d g(t)\,dt$ 可以任意小；于是 $\int_c^d f(t)\,dt$ 也如此，再次应用反常积分的 Cauchy 判别法即表明 $f$ 可积。（事实上，这个论证还表明 $f$ 是 absolutely integrable（绝对可积）的。）
>
> 现在令 $\varepsilon > 0$。取 $L_0$ 足够大，使得 $\int_{L_0}^\infty g(t)\,dt < \varepsilon/4$。再取 $N$ 足够大，使得当 $n \ge N$ 且 $t \in [a,L_0]$ 时 $|f_n(t) - f(t)| < \varepsilon/(2(L_0-a))$。这是可能的，因为 $f_n \to f$ 在 $[a,L_0]$ 上一致收敛。于是对所有 $n \ge N$ 有
>
> ```math
> \left|\int_a^\infty f_n(t)\,dt - \int_a^\infty f(t)\,dt\right|
> \le \int_a^{L_0}|f_n(t)-f(t)|\,dt + \int_{L_0}^\infty 2g(t)\,dt
> \le \frac{\varepsilon}{2(L_0-a)}(L_0-a) + 2\cdot\frac{\varepsilon}{4} = \varepsilon .
> ```
>
> 这就证明了定理的断言。$\blacksquare$

<span style="color:#7f8c8d">*Exercises 9.5.1–9.5.3 为习题区，按约定跳过。*</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Theorem 9.33（控制收敛，dominated convergence）是本节的高潮，证明结构是分析学「大区间分割」的经典模板，值得拆解成三步：（i）先用 $g$ 可积来证明 $f$ 可积（因为 $|f_n|\le g$ 推出 $|f|\le g$，而 $\int_c^d g$ 在 $c,d\to\infty$ 时可任意小，Cauchy 判据保证 $f$ 可积）；（ii）取 $L_0$ 大，使尾部 $\int_{L_0}^\infty g<\varepsilon/4$——用支配函数「包住尾巴」；（iii）在紧区间 $[a,L_0]$ 上，局部一致收敛给出 $|f_n-f|<\varepsilon/(2(L_0-a))$。整体是「尾部交给 $g$ + 头部交给一致收敛」的分而治之。例 9.32 的意义正在于此：$f_n$ 是高度 $1/n$、宽度 $n$ 的长条，一致收敛到 0 但每个积分都是 1——因为反常积分是「整体量」而一致收敛只约束「局部偏差」，尾巴处 $f_n$ 虽小但区间长，面积不缩；支配条件 $|f_n|\le g$ 且 $g$ 可积则强制尾巴快速衰减，堵死「把质量摊到无穷远」。第一性原理：**反常积分是极限 $\lim_{b\to\infty}\int_a^b$，所以换序变成了「取两个极限」的交换，需要更强的控制**——这就是为什么反常积分的情形比有限区间更微妙。「dominated」一词即指每个 $f_n$ 被同一个可积函数 $g$「罩住」，就像你在 18.065 用范数不等式 $\|x_n\|\le M$ 控制向量序列，单点控制升级为整支序列的统一控制。🎥 教授谈到这一章的核心主题时说：「If you have uniform convergence, then it will say that then a lot of operations... like integration and differentiation, you can do that over here, and then take the limit.」（翻译：如果你有一致收敛，那么它意味着很多运算——比如积分和微分——你都可以在这里进行，然后再取极限。）

---

<!-- ===== 书页 393（PDF 页 9）===== -->

Part009 · 书页 393 行内双语翻译

<!-- 本页上部为 §9.5 习题区（Exercise 9.5.4-9.5.10），按约定跳过 -->

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">9.6 Uniform Convergence and Derivatives（一致收敛与导数）</span>

我们在 Section 9.5 中看到，由连续函数构成的序列（或级数）若 uniform convergence（一致收敛），则可以进行 term-by-term integration（逐项积分）。

这为关于 term-by-term differentiation（逐项求导）的定理提供了一个简便的证明。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 9.34（定理 9.34）</span>
> <span style="color:#7f8c8d;">TBB §9.6, p.393</span>

设 $\{f_n\}$ 是定义在区间 $[a,b]$ 上的函数序列，其中每个函数都具有连续导数。

若导数序列 $\{f_n'\}$ 在 $[a,b]$ 上一致收敛到某个函数，
且序列 $\{f_n\}$ pointwise convergence（逐点收敛）到某个函数 $f$，则 $f$ 在 $[a,b]$ 上可微，并且

```math
f'(x) = \lim_{n\to\infty} f_n'(x) \quad (x \in [a,b]).
```


---

<!-- ===== 书页 394（PDF 页 10）===== -->

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 令 $g = \lim_{n\to\infty} f_n'$。由于每个 $f_n'$ 均假设连续且收敛是一致的，函数 $g$ 也连续（Theorem 9.22）。由 Theorem 9.29 推得：对所有 $x \in [a,b]$，
> 
> ```math
> \int_a^x g(t)\,dt = \lim_{n\to\infty} \int_a^x f_n'(t)\,dt \tag{13}
> ```
> 
> 应用微积分基本定理（fundamental theorem of calculus），我们看到：对所有 $x \in [a,b]$ 和所有 $n \in \mathbb{N}$，
> 
> ```math
> \int_a^x f_n'(t)\,dt = f_n(x) - f_n(a) \tag{14}
> ```
> 
> 但由假设，对所有 $x \in [a,b]$ 有 $f_n(x) \to f(x)$，故在等式 (14) 中令 $n \to \infty$ 并注意 (13)，我们得到
> 
> ```math
> \int_a^x g(t)\,dt = f(x) - f(a),
> ```
> 
> 即 $f(x) = \int_a^x g(t)\,dt + f(a)$。
> 
> 由 $g$ 的连续性与微积分基本定理可知，$f$ 可微，且对所有 $x \in [a,b]$ 有 $f'(x) = g(x)$。
> 
> ¥

对级数而言，该定理具有如下形式：

### <span style="color:#2471a3;">**[corollary]**</span> <span style="color:#c0392b">Corollary 9.35（推论 9.35）</span>
> <span style="color:#7f8c8d;">TBB §9.6, p.394</span>

设 $\{f_k\}$ 是定义在 $[a,b]$ 上的函数序列，其中每个函数都具有连续导数，并设 $f = \sum_{k=0}^{\infty} f_k$ 在 $[a,b]$ 上成立。

若级数 $\sum_{k=0}^{\infty} f_k'$ 在 $[a,b]$ 上一致收敛，则 $f' = \sum_{k=0}^{\infty} f_k'$ 在 $[a,b]$ 上成立。

<span style="color:#2471a3;">**[example]**</span> **Example 9.36（例 9.36）**
> <span style="color:#7f8c8d;">TBB §9.6, p.394</span>

从 geometric series（几何级数）出发：

```math
\frac{1}{1-x} = \sum_{k=0}^{\infty} x^k \quad (x \in (-1,1)) \tag{15}
```

由 Corollary 9.35 我们得到：

```math
\frac{1}{(1-x)^2} = \sum_{k=1}^{\infty} k x^{k-1} \quad (x \in (-1,1)) \tag{16}
```

为证明 (16)，我们先注意到级数 (15) 在 $(-1,1)$ 上逐点收敛；其次（见 Exercise 9.3.17）级数 (16) 在 $(-1,1)$ 上逐点收敛，且在 $(-1,1)$ 内任一闭区间 $[a,b] \subset (-1,1)$ 上一致收敛。

因此，若 $x \in (-1,1)$ 且 $-1 < a < x < b < 1$，则 (16) 在 $[a,b]$ 上一致收敛，从而 (16) 在 $x$ 处成立。



#### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">9.6.1 Limits of Discontinuous Derivatives（不连续导数的极限）</span>

本节为扩展内容（Enrichment section），可省略阅读。Theorem 9.34（定理 9.34） 的假设对于结论成立而言略显苛刻（more restrictive than necessary）。

我们无需假设 $\{f_n\}$ 在 $[a,b]$ 上处处收敛；在单个点处的收敛便已足够。

我们也无需假设每个导数 $f_n'$ 都连续。（不过，我们不能把序列 $\{f_n'\}$ 的一致收敛替换为逐点收敛——

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Theorem 9.34 是「极限与求导换序」的严格版本，它的证明策略非常漂亮，值得提炼成模板：**「先积分再求导」或「基本定理归约」**。（i）令 $g=\lim f_n'$，由一致收敛 $g$ 连续；（ii）由 Theorem 9.29（积分换序）得 $\int_a^x g=\lim\int_a^x f_n'$；（iii）用微积分基本定理（FTC）把 $\int_a^x f_n'=f_n(x)-f_n(a)$ 换成函数值差；（iv）两边取极限得 $f(x)-f(a)=\int_a^x g$，再对 $x$ 求导得 $f'=g$。整个证明的杠杆是「求导的逆运算——积分」，把难以处理的「逐点收敛的函数序列」问题转成「一致收敛的导数序列」问题。第一性原理：**为什么求导比积分更脆弱？** 因为导数是一个「局部」操作（依赖差商在一点的行为），一致收敛的函数序列其导数却可能剧烈震荡（例 9.5）；而积分是「整体」操作，能把局部的疯狂「平均掉」。所以数学上「先证明积分版本，再用 FTC 回到导数」是绕开困难的通用手法。推论 9.35（级数版本）与例 9.36（$\frac{1}{(1-x)^2}=\sum kx^{k-1}$）展示了实战用法：先在 $(-1,1)$ 内任一闭子区间上验证 $\sum kx^{k-1}$ 一致收敛（由 Weierstrass M-test 或几何级数判别），于是逐项求导合法。你可以在笔记里把 9.34 与 9.37 并排对比：9.34 要求「每个 $f_n'$ 连续」且「$\{f_n\}$ 逐点收敛」，9.37 只要求「$f_n'$ 存在 + $\{f_n'\}$ 一致收敛 + 一个点处收敛」——9.37 更弱更强，是更强的工具，我们下一注细看。

---

<!-- ===== 书页 395（PDF 页 11）===== -->

Part009 · 书页 395 行内双语翻译

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">9.6 Uniform Convergence and Derivatives（一致收敛与导数）</span>

正如 Example 9.5（例 9.5）所示。）接下来的定理适用于许多 Theorem 9.34（定理 9.34）无法适用的情形。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 9.37（定理 9.37）</span>
> <span style="color:#7f8c8d;">TBB §9.6, p.395</span>

设 $\{f_n\}$ 是定义在区间 $[a,b]$ 上的一列连续函数（continuous functions）。假设对每个 $n$ 与每个 $x \in [a,b]$，derivative（导数）$f'_n(x)$ 都存在；假设导数序列 $\{f'_n\}$ 在 $[a,b]$ 上一致收敛（uniformly convergent），并且存在一点 $x_0 \in [a,b]$ 使得数列 $\{f_n(x_0)\}$ 收敛。

那么序列 $\{f_n\}$ 在区间 $[a,b]$ 上一致收敛到某个函数 $f$，$f$ 可微，并且在每一点 $x \in [a,b]$ 处有

```math
f'(x) = \lim_{n\to\infty} f'_n(x).
```

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 设 $\varepsilon > 0$。由于导数序列在 $[a,b]$ 上一致收敛，存在整数 $N_1$，使得对所有 $n,m \ge N_1$ 与所有 $x \in [a,b]$ 都有 $|f'_n(x) - f'_m(x)| < \varepsilon$；又由于数列 $\{f_n(x_0)\}$ 收敛，存在整数 $N > N_1$，使得对所有 $n,m \ge N$ 都有 $|f_n(x_0) - f_m(x_0)| < \varepsilon$。
>
> 对任意 $x \in [a,b]$、$x \neq x_0$，我们将中值定理（mean value theorem）应用于函数 $f_n - f_m$ 在区间 $[x_0,x]$ 上（若 $x < x_0$，则在区间 $[x,x_0]$ 上），于是存在介于 $x$ 与 $x_0$ 之间的某一点 $\xi$，使得
>
> ```math
> f_n(x) - f_m(x) - [f_n(x_0) - f_m(x_0)] = (x - x_0)[f'_n(\xi) - f'_m(\xi)]. \tag{17}
> ```
>
> 由此我们推出，对任意 $n,m \ge N$ 有 $|f_n(x) - f_m(x)| \le |f_n(x_0) - f_m(x_0)| + |(x - x_0)(f'_n(\xi) - f'_m(\xi))| < \varepsilon\bigl(1 + (b-a)\bigr)$。由于这个 $N$ 只依赖于 $\varepsilon$，该断言对所有 $x \in [a,b]$ 成立，于是我们验证了连续函数序列 $\{f_n\}$ 在 $[a,b]$ 上是一致 Cauchy（uniformly Cauchy）序列，从而一致收敛到 $[a,b]$ 上的某个连续函数 $f$。
>
> 现在我们证明 $f'(x_0)$ 是导数 $f'_n(x_0)$ 的极限。再次取任意 $\varepsilon > 0$，方程 (17) 表明，对所有 $n,m \ge N$ 及区间 $[a,b]$ 中任意 $x \neq x_0$ 有
>
> ```math
> |f_n(x) - f_m(x) - [f_n(x_0) - f_m(x_0)]| \le |x - x_0|\varepsilon. \tag{18}
> ```
>
> 在此不等式中令 $m \to \infty$，并注意到 $f_m(x) \to f(x)$、$f_m(x_0) \to f(x_0)$，我们得到：当 $n \ge N$ 时有
>
> ```math
> |f_n(x) - f_n(x_0) - [f(x) - f(x_0)]| \le |x - x_0|\varepsilon. \tag{19}
> ```
>
> 设 $C$ 为数列 $\{f'_n(x_0)\}$ 的极限，于是存在 $M > N$ 使得
>
> ```math
> |f'_M(x_0) - C| < \varepsilon. \tag{20}
> ```
>
> 由于函数 $f_M$ 在 $x_0$ 处可微，存在 $\delta > 0$，使得当 $0 < |x - x_0| < \delta$ 时有
>
> ```math
> \left|\frac{f_M(x) - f_M(x_0)}{x - x_0} - f'_M(x_0)\right| < \varepsilon. \tag{21}
> ```

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Theorem 9.37 是本章「一致收敛与求导」的终极版本，它的证明依赖一个你熟悉的中值定理（MVT）技巧：对 $f_n-f_m$ 用 MVT，得到 $f_n(x)-f_m(x)=f_n(x_0)-f_m(x_0)+(x-x_0)(f_n'(\xi)-f_m'(\xi))$。这个公式把「函数值的差」归约为「一个点的函数值差 + 导数值差 × 区间长」，于是一致收敛的 $\{f_n'\}$ 立刻给出 $\{f_n\}$ 的一致 Cauchy 性质（在 $\{f_n(x_0)\}$ 收敛的点上「锚定」）。这是分析学的核心思想：**导数的一致有界性/一致收敛性可以「传播」到函数本身的一致性**。在 CLRS 里你能看到同构：函数值的差异被 Lipschitz 常数（导数上界）放大，正如算法的误差分析里「每步误差 × 迭代次数」累积。证明第二半（证明 $f'(x_0)=C$）用了一个精致的「$3\varepsilon$」收尾：把 $f_M(x)-f_M(x_0)$ 与 $f(x)-f(x_0)$ 的差、$f_M'(x_0)$ 与 $C$ 的差、差商与 $f_M'(x_0)$ 的差分别控制在 $\varepsilon$ 内，三角不等式给出 $3\varepsilon$。推论 9.38 与注记说明「一个点的收敛」就够了，且即使 $\{f_n\}$ 不收敛（如 $f_n\equiv n$），导函数的一致极限仍是某个函数的导数——这说明导数类的「一致极限闭包」比想象中宽。这里推荐你做一个「脚手架迁移」：把 9.37 看作数值分析里「函数列的误差由导数误差控制」的严格化，与你在 CSAPP 里学的浮点误差传播（$\|f(x)-f(y)\|\le L\|x-y\|$）是同一套 Lipschitz 语言。

---

<!-- ===== 书页 396（PDF 页 12）===== -->

Part009 · 书页 396 行内双语翻译

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.（接续）*

> 由方程 (19) 及 $M > N$ 这一事实，我们有
>
> ```math
> \left|\frac{f_M(x) - f_M(x_0)}{x - x_0} - \frac{f(x) - f(x_0)}{x - x_0}\right| < \varepsilon.
> ```
>
> 这连同不等式 (20) 与 (21) 表明，当 $0 < |x - x_0| < \delta$ 时有
>
> ```math
> \left|\frac{f(x) - f(x_0)}{x - x_0} - C\right| < 3\varepsilon.
> ```
>
> 这就证明了 $f'(x_0)$ 存在且等于数 $C$，而我们记得 $C = \lim_{n\to\infty} f'_n(x_0)$。
>
> 在此论证中，$x_0$ 可以取区间 $[a,b]$ 内的任意一点，于是定理得证。$\blacksquare$

对于无穷级数而言，Theorem 9.37（定理 9.37）取如下形式。

### <span style="color:#2471a3;">**[corollary]**</span> <span style="color:#c0392b">Corollary 9.38（推论 9.38）</span>
> <span style="color:#7f8c8d;">TBB §9.6, p.396</span>

设 $\{f_k\}$ 是区间 $[a,b]$ 上的一列可微函数（differentiable functions）。假设级数 $\sum_{k=0}^{\infty} f'_k$ 在 $[a,b]$ 上一致收敛，并且存在 $x_0 \in [a,b]$ 使得级数 $\sum_{k=0}^{\infty} f_k(x_0)$ 收敛。

那么级数 $\sum_{k=0}^{\infty} f_k(x)$ 在 $[a,b]$ 上一致收敛到某个函数 $F$，$F$ 可微，并且对所有 $a \le x \le b$ 有

```math
F'(x) = \sum_{k=0}^{\infty} f'_k(x).
```

<span style="color:#2471a3;">**[note]**</span> **注记（Note）.**

在 Theorem 9.37 的陈述中，我们假设存在唯一点 $x_0$ 使得序列 $\{f_n(x_0)\}$ 收敛，由此推得序列 $\{f_n\}$ 在整个区间 $I$ 上收敛。

若去掉这一要求、但保留序列 $\{f'_n\}$ 在 $I$ 上一致收敛到某个函数 $g$ 的要求，我们便无法断言 $\{f_n\}$ 在 $I$ 上收敛（例如令 $f_n(x) \equiv n$），但仍能断言存在 $f$ 使得在 $I$ 上有 $f' = g = \lim_n f'_n$。

（要看出这一点，可固定 $x_0 \in I$，令 $F_n = f_n - f_n(x_0)$，再对序列 $\{F_n\}$ 应用 Theorem 9.37。）

因此，即使作为原函数（primitive）的序列 $\{f_n\}$ 不收敛，导数序列 $\{f'_n\}$ 的一致极限（uniform limit）仍然是某个函数的导数。

<span style="color:#7f8c8d">*（本页末尾的 Exercises 习题区按约定跳过，不译。）*</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> §9.6.1 的这段接续文字点出 Theorem 9.34 的假设可以放宽成 Theorem 9.37：不需要「处处逐点收敛」而只需「一个点收敛」，不需要「$f_n'$ 连续」而只需「$f_n'$ 存在 + 一致收敛」。关键在于，我们刚才在书页 395 已见过 9.37 的完整证明，9.37 把 9.34 的「$\{f_n\}$ 逐点收敛」替换成「$\{f_n(x_0)\}$ 收敛于一点」，然后用一致 Cauchy 条件把单点收敛「升级」为全区间一致收敛。这里请特别留意 Corollary 9.38 与后面注记的分量：即使去掉「单点收敛」，只要 $\sum f_k'$ 一致收敛，$\sum f_k$ 虽然可能不收敛，但导数的一致极限仍然是某个函数 $F$ 的导数（取 $F_n=f_n-f_n(x_0)$ 再应用定理）。这本质上是在说：**一致收敛的导函数列 $\{g_n\}$ 的极限 $g$ 必是某个函数的导数——导数的一致极限是「可积」的（在 FTC 意义下）**。你可以把它与数字信号处理/滤波的直觉连接：积分是「低通滤波器」，把导数序列的震荡滤平，使极限仍然来自某个「原函数」。这是「求导运算的一致极限闭包」问题的答案，也是通往 §9.8 的桥梁。下一节我们会看到「逐点极限」能造出多病的函数（连续函数的逐点极限可以处处不连续！），而这里的一致极限则永远「守规矩」——这正是本章反复出现的对偶主题：**一致收敛保结构，逐点收敛不保**。

---

<!-- ===== 书页 397（PDF 页 13）===== -->

Part009 · 书页 397 行内双语翻译

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">9.7 Pompeiu's Function（Pompeiu 函数）</span>

*Enrichment section（提高性内容）。可以省略。*

十九世纪末，分析学家们已经积累起足够的工具，开始构造一些挑战当时主流观点的函数例子。著名数学家 Henri Poincaré 曾抱怨道：

> 从前人们发明一个新函数，是为了某种实际目的；如今它们被发明出来，是为了指出我们前辈推理中的错误……

许多数学家对于竟然能构造出在他们看来怪诞而不自然的函数，既感到震惊又感到愤怒。十九世纪优美而典雅的理论，正被一个个 pathological example（病态例子）撕得粉碎。

也许最早的冲击是 Weierstrass 等人构造的处处都没有导数的连续函数。这确实暴露了先前的一些错误，因为不少数学家以为他们已经成功证明了连续函数不可能如此。另一个著名的例子归功于 Vito Volterra（1860–1940），他构造了一个可微函数 $F$，其导数 $F'$ 有界，却不是 Riemann integrable（Riemann 可积）的。

本节我们介绍 D. Pompeiu 在 1906 年给出的一个例子。这个函数 $h$ 是可微的，并且具有如下引人注目的性质：$h'$ 在一个 dense set（稠密集）上不连续，而在另一个稠密集上取值为零。我们将看到，这蕴含 $h$ 是一个可微函数，并且像 Volterra 的例子一样，它的导数不是 Riemann 可积的。事实上，$h'$ 在任何区间上都不是 Riemann 可积的，而 Volterra 的例子在不少子区间上都是 Riemann 可积的。

这个例子用到了我们到目前为止建立的许多定理，因此是对我们各项技巧的绝佳复习。我们分一系列步骤来呈现这个例子，每一步都留作相对容易的习题。（Exercise 9.7.4 看似合理，但验证起来很繁琐，你可能宁愿不去核对其中细节。）

为了开始这个例子，我们注意到函数
```math
f(x) = \sqrt[3]{x - a}
```
在 $x = a$ 处有无穷导数，而在其余各处有有限导数。令 $q_1, q_2, q_3, \ldots$ 为 $\mathbb{Q} \cap [0, 1]$ 的一个枚举。令
```math
f(x) = \sum_{k=1}^{\infty} \frac{\sqrt[3]{x - q_k}}{10^k}.
```
这一函数的反函数正是 Pompeiu 函数，即 $h = f^{-1}$。

细节都出现在习题之中。请特别注意，我们的主要目标是证明：$h$ 可微，$h'$ 有界，$h'$ 在一个稠密集上取值为零，$h'$ 在另一个稠密集上为正且不连续，并且 $h'$ 不是 Riemann 可积的。

为了便于比较，让我们回忆 Exercise 7.4.2：我们在那里给出了一个可微函数 $g$ 的例子，$g'$ 有界，但在一个 nowhere-dense（无处稠密）的完备集 $P$ 上不连续。由 Section 8.6.3 可知，如果 $P$ 的测度不为零，那么这样的函数 $g'$ 就不是 Riemann 可积的。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> §9.7 是「病态函数」的狂欢，Pompeiu 函数（1906 年，罗马尼亚数学家 Dimitrie Pompeiu 构造）是「分析学怪胎」的集大成者。背景：Poincaré 抱怨「为了指出前辈推理的错误而发明函数」，正是十九世纪末分析严格化运动的写照——Weierstrass 1872 年构造处处连续处处不可微函数，粉碎「连续函数几乎处处可微」的旧信念；Volterra 1881 年构造导数有界却 Riemann 不可积的可微函数，戳穿「可微 ⟹ 导数可积」的想当然。Pompeiu 的 $h$ 更强：可微、$h'$ 有界、$h'$ 在一个稠密集上取零、在另一个稠密集上不连续且不可积（$h'$ 在任何区间上都不可积）。构造核心 $f(x)=\sum_{k=1}^\infty\frac{\sqrt[3]{x-q_k}}{10^k}$：每项在 $x=q_k$ 有「无穷导数」，系数 $10^{-k}$ 保证 M-test 一致收敛（$\sum 1/10^k$ 收敛），于是 $f$ 在可数稠密集上处处不光滑，取反函数 $h=f^{-1}$ 即得「导数零又跳」。第一性原理：**Riemann 可积要求不连续点构成零测集，Pompeiu 却把不连续点铺到稠密且非零测**，于是「震荡但仍有界」的导函数令 Riemann 积分无能为力——这正是 Volterra 用「正测度 Cantor 集」制造不可积的原因（对比 Exercise 7.4.2 的零测无处稠密集，其导数仍可积）。「微积分基本定理失效」（$g(x)-g(a)=\int_a^x g'$ 不成立）是 Riemann 框架的致命裂缝，也是 Lebesgue 积分（可积导函数 + 绝对连续）诞生的直接动机。通用武器：**用 $\frac{1}{10^k}$ 快速衰减系数把「局部坏行为」叠加成「处处坏行为」，是构造反例的标准流水线**，与算法中「指数衰减权重惩罚坏样本」同构。

---

<!-- ===== 书页 398（PDF 页 14）===== -->

Part009 · 书页 398 行内双语翻译

<span style="color:#7f8c8d">*§9.7 Pompeiu's Function（Pompeiu 函数）正文之末；本页下半为 Exercise 9.7.1–9.7.16 习题区（按约定跳过）。*</span>

由于 $P$ 的测度不为零，我们不能写成

```math
g(x) - g(a) = \int_a^x g'(t)\, dt,
```
也就是说，若仅限于使用 Riemann 积分，fundamental theorem of calculus（微积分基本定理）对函数 $g$ 及其导数 $g'$ 并不成立。

这正是 Volterra 构造其例子的方式——他确保集合 $P$ 的测度不为零。

我们还在 Section 7.4 中提到，一个可微函数 $f$ 有可能使其导数 $f'$ 在一个稠密集上不连续。

而 Pompeiu 函数恰好印证了这一说法。

<!-- page_014：习题区（Exercise 9.7.1–9.7.16 与 NOTES 提示），按约定跳过 -->


---

<!-- ===== 书页 399（PDF 页 15）===== -->

Part009 · 书页 399 行内双语翻译

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">9.8 Continuity and Pointwise Limits（连续性与逐点极限）</span>

*高级章节（Advanced section），可略过。*

本章的大部分内容都聚焦于 uniform convergence（一致收敛）这一概念，因为它在为我们在 Section 9.1 中提出的问题提供肯定回答方面扮演了核心角色。特别是，我们在 Section 9.2 中看到，连续函数序列的 pointwise limit（逐点极限）未必连续。另一方面，若收敛是 uniform（一致）的，这些麻烦便不会出现。

然而，有许多情形中 pointwise convergence（逐点收敛）会自然地出现，而一致收敛却不会。例如，考虑一个在 $\mathbb{R}$ 上可微的函数 $F$。则对 $x \in \mathbb{R}$，

```math
F'(x) = \lim_{n\to\infty} \frac{F\left(x + \frac{1}{n}\right) - F(x)}{\frac{1}{n}}.
```

若我们定义函数 $f_n$ 为

```math
f_n(x) = \frac{F\left(x + \frac{1}{n}\right) - F(x)}{\frac{1}{n}},
```

则每一个函数 $f_n$ 都在 $\mathbb{R}$ 上连续，且 $f_n \to F'$ 是逐点收敛的。

现在，我们已见过derivative（导数）在许多点不连续的例子。例如，Section 9.7 中的函数 $h'$ 在一个于 $[0,1]$ 中稠密、且不具有 measure zero（零测度）的集合上不连续。类似地，Exercise 7.4.2 给出了一个可微函数 $g$ 的例子，其导数 $g'$ 在一个不具有零测度的 Cantor 集的每一点都不连续。我们或许会问："一个可微函数的导数能否处处不连续？"我们将看到，答案是"不能"。事实上，连续性点的集合在 category（纲）的意义下必定足够大——该集合必须稠密且为 $G_\delta$ 型，因此是 residual（剩余集）（见 Theorem 6.17）。

我们实际上将证明一个更一般的定理。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 9.39（定理 9.39）</span>
> <span style="color:#7f8c8d;">TBB §9.8, p.399</span>

设 $\{g_n\}$ 是定义在区间 $I$ 上的连续函数序列，且在 $I$ 上逐点收敛到函数 $g$。则 $g$ 的连续性点的集合在 $I$ 中构成一个 $G_\delta$ 型的稠密集。

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 我们首先概述证明的思路，暂时把形式化证明放到一边。在 Section 6.7 中，我们定义了函数 $f$ 在点 $x_0$ 处的 oscillation（振幅）$\omega_f(x_0)$，并证明了（Theorem 6.25）$f$ 在 $x_0$ 处连续当且仅当 $\omega_f(x_0) = 0$。我们现在证明，在 Theorem 9.39 的假设之下，$\omega_g(x)$ 将在一个稠密集上为零。这将蕴含 $g$ 在一个稠密集上连续。该集合必为 $G_\delta$ 型（由 Theorem 6.28）。


---

<!-- ===== 书页 400（PDF 页 16）===== -->

Part009 · 书页 400 行内双语翻译

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明，续）.*

> 我们将用反证法（argue by contradiction）来论证。我们假设 $g$ 在某个子区间 $J$ 的每一点都不连续。然后我们利用 Baire category theorem（Baire 纲定理）（Theorem 6.11）证明：存在 $n \in \mathbb{N}$ 与一个区间 $H \subset J$，使得在 $H$ 的每一点都有 $\omega_g(x) \ge 1/n$。（这一论证对任何在区间 $J$ 的每一点都不连续的函数都成立。）随后我们用关于 $g$ 的假设来证明这是不可能的。为此，我们再次应用 Baire 纲定理，得到 $H$ 的一个子区间 $K$，$g$ 将 $K$ 映到一个 diameter（直径）小于 $1/n$ 的集合上。这意味着对每个 $x \in K$ 有 $\omega_f(x) < 1/n$，而这构成矛盾。

> 现在我们可以开始 Theorem 9.39 的形式化证明了。为获得矛盾，我们假设 $g$ 在某个区间 $J \subset I$ 上处处不连续。对每个 $n \in \mathbb{N}$，令

> ```math
> E_n = \{x \in J : \omega_g(x) \ge 1/n\}.
> ```

> 每一个集合 $E_n$ 都是 closed（闭集）（由 Theorem 6.27），并且 $J = \bigcup_{n=1}^{\infty} E_n$。由 Baire 纲定理，存在 $n \in \mathbb{N}$ 和区间 $H \subset J$，使得 $E_n$ 在 $H$ 中稠密。区间 $H$ 具有如下性质：$g$ 把 $H$ 的每个子区间都映到直径至少为 $1/n$ 的集合上。我们现在证明，这对 $g$——连续函数的 pointwise limit（逐点极限）——是不可能的。

> 设 $\{I_k = (a_k, b_k)\}$ 是一个区间序列，其中每个区间的长度小于 $1/n$，且满足 $g(H) \subset \bigcup_{k=1}^{\infty} I_k$。对每个 $k$，令 $H_k = g^{-1}(I_k) \cap H$。则 $H = \bigcup_{k=1}^{\infty} H_k$，但集合 $H_k$ 中没有哪一个能包含一个区间[因为每个 $H_k$ 的长度小于 $1/n$，而对所有 $x \in H$ 都有 $\omega_g(x) \ge 1/n$]。现在

> ```math
> H_k = \{x : g(x) < b_k\} \cap \{x : g(x) > a_k\}.
> ```

> 由 Exercise 9.8.4，这些集合中的每一个都是 $F_\sigma$ 型的，因此 $H_k = \bigcup_{j=1}^{\infty} H_{kj}$，其中每一个集合 $H_{kj}$ 都是闭集。由此可得

> ```math
> H = \bigcup_{k=1}^{\infty} H_k = \bigcup_{k=1}^{\infty} \bigcup_{j=1}^{\infty} H_{kj}.
> ```

> 区间 $H$ 被表示为闭集的 countable union（可数并）。由 Baire 纲定理可知，其中至少有一个集合，设为 $H_{ij}$，在某个区间 $K \subset H$ 中稠密。由于 $H_{ij}$ 是闭集，故 $H_{ij} \supset K$。但这蕴含 $H_i \supset K$，而我们已看到这是不可能的（因为每个集合 $H_k$ 都不包含任何区间）。这个矛盾完成了证明。$\blacksquare$

### <span style="color:#2471a3;">**[corollary]**</span> <span style="color:#c0392b">Corollary 9.40（推论 9.40）</span>
> <span style="color:#7f8c8d;">TBB §9.8, p.400</span>

设 $f$ 在区间 $(a, b)$ 上可微。则 $f'$ 在 $(a, b)$ 的某个 residual（剩余集）子集上连续。因此 $f'$ 的连续性点的集合必在 $(a, b)$ 中稠密。

**Note（注记）.** Theorem 9.39 与 Exercise 9.8.4 描述了作为连续函数序列的 pointwise limit（逐点极限）的函数的两个重要性质。每一个这样的函数 $f$ 是……（接下页）

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> §9.8 的核心问题：「一个可微函数的导数能否处处不连续？」答案是（在 Baire 纲的意义下）不能——导数 $f'$ 的连续点构成稠密 $G_\delta$ 集。Theorem 9.39 是本章的收束：连续函数的逐点极限 $g$，其连续点集在 $I$ 中稠密且为 $G_\delta$ 型。证明用反证法 + Baire 纲定理（Theorem 6.11），这是你第一次正面遭遇「纲方法」：设 $g$ 在某子区间 $J$ 上处处不连续，定义 $E_n=\{x:\omega_g(x)\ge 1/n\}$（振幅分级），由 Theorem 6.27 每个 $E_n$ 是闭集且 $J=\bigcup_n E_n$；Baire 纲定理说完备度量空间不能是可数个无处稠密集之并，于是某个 $E_n$ 在某子区间 $H$ 上稠密，即 $g$ 把 $H$ 的每个子区间映到直径 $\ge 1/n$ 的集合。矛盾来自「Baire 1」结构：$\{x:g(x)<b_k\}$、$\{x:g(x)>a_k\}$ 都是 $F_\sigma$ 型（Exercise 9.8.4），$H$ 写成闭集可数并，再次由纲定理推出某闭集在某子区间 $K$ 稠密，于是 $g$ 在 $K$ 上震荡 $<1/n$，矛盾。这套「振幅分层 → 纲定理 → 矛盾」论证是 Baire 类方法的标准剧本，未来泛函分析（一致有界原理、开映射定理）会重逢。第一性原理：**连续性点的集合不是「随机」的，它受制于「可数级联」结构——Baire 1 函数只能有「小」的不连续集**。Corollary 9.40 把 §9.7 收进同一框架：可微函数的导数自动是 Baire 1，连续点必为稠密 $G_\delta$。注意纲的「大小」与测度（Lebesgue）的「大小」是两个标尺——集合可同时是稠密 $G_\delta$（纲上「大」）又零测（测度上「小」），这种双标尺张力正是实变函数论的魅力。

---

<!-- ===== 书页 401（PDF 页 17）===== -->

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Section 9.8 Continuity and Pointwise Limits（第 9.8 节 连续性与逐点极限）</span>

<span style="color:#7f8c8d">（承上页定理陈述）</span>

该函数在一个 residual set（剩余集）上连续，

并且形如 $\{x : f(x) > a\}$ 或 $\{x : f(x) < a\}$ 的每个集合

都是 type $F_\sigma$（$F_\sigma$ 型）。

定理 9.39（Theorem 9.39）可以被推广。

如果 $P$ 是 $f$ 的定义域的一个非空 closed subset（闭子集），

那么函数 $f|P$ 在 $P$ 的一个稠密 $G_\delta$ 子集上连续。

上述结论的 converse（逆命题）也为真：

一个函数 $f$ 是区间 $I$ 上一列连续函数的 pointwise limit（逐点极限），

当且仅当对每个闭集 $P \subset I$，把 $f$ 看作定义在集合 $P$ 上的函数时，

它在 $P$ 中的一个稠密 $G_\delta$ 集上连续；

而这又当且仅当形如 $\{x : f(x) > a\}$ 或 $\{x : f(x) < a\}$ 的每个集合

都是 $F_\sigma$ 型。

这些定理有许多应用。

作为一列连续函数的逐点极限的函数称为 Baire 1 functions（Baire 1 类函数）。

我们已经看到，这一类函数包含了由导数构成的函数类。

它还包含所有 monotonic functions（单调函数），

以及分析中出现的许多其他重要的函数类。

下面的习题可能颇有启发性。

你可能需要使用本节中某个未证明的命题，

来解答其中的一些习题。

> **注 3.** 这些命题的证明可在 I. P. Natanson 的 *Theory of Functions of a Real Variable*（《实变函数论》）第 II 卷第十五章中找到，Fredrick Ungar Pub. Co., New York（1955）[英译本]。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> page_017 收尾处把「连续函数的逐点极限」正式命名为 **Baire 1 函数**（Baire class 1），并给出两条刻画：(a) 对每个闭集 $P$，$f|_P$ 在 $P$ 的稠密 $G_\delta$ 子集上连续；(b) $\{x:f(x)>a\}$ 与 $\{x:f(x)<a\}$ 都是 $F_\sigma$ 型。这是 Baire（René-Louis Baire，1874–1932，法国数学家，1899 年博士论文）开创的「函数分类学」：Baire 0 = 连续函数，Baire 1 = 连续函数的逐点极限，Baire 2 = Baire 1 函数的逐点极限，……。为什么这个分类重要？因为「逐点极限」运算在每一层都会产生新的函数，但又受控——Baire 1 已经包含了所有导数、所有单调函数（定理 9.39 的推论），而 Dirichlet 函数（有理数指示函数）属于 Baire 2 而非 Baire 1。这与你离散数学的「可数并」直觉高度契合：$F_\sigma$ 就是「闭集的可数并」，$G_\delta$ 是「开集的可数交」；Baire 1 的刻画本质上是说「这类函数的水平集只有可数层级的复杂度」——一阶描述复杂度对应 Baire 1，二阶对应 Baire 2，这正是描述集合论（descriptive set theory）的雏形。第一性原理洞察：**分类的标尺是「为了确定函数值，需要取多少次极限」**——连续函数直接取点（0 次），Baire 1 取一次逐点极限，Baire 2 再取一次。这与你在 6.042J 学的「可数/不可数」层级、在 CLRS 学的「$O(\log n)$ 层归约」是同一母题的三种表达：层级越深，能表达的「病态」越多，但依然有界。这套层级在你未来学泛函分析（Borel 层级）、概率论（可测函数）时是地基。现在只需记住一个口号：**一致收敛保层级（停留 Baire 1），逐点收敛升层级（可能到 Baire 2）**。

---

<!-- ===== 书页 402（PDF 页 18）===== -->

<!-- page_018：习题区，按约定跳过 -->


---

<!-- ===== 书页 403（PDF 页 19）===== -->

<!-- page_019：NOTES/习题区，按约定跳过 -->


---

<!-- ===== 书页 404（PDF 页 20）===== -->

Part009 · 书页 404 行内双语翻译

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Chapter 10 Power Series（幂级数）</span>

若第 2 章 2.13 节关于 limit superior（上极限）与 limit inferior（下极限）的内容此前未学，应在着手研读本章之前补上。

radius of convergence（收敛半径）这一概念天然地依赖于这些概念。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">10.1 Introduction（引言）</span>

最简单、也可以说是最重要的一类 series of functions（函数项级数）就是 power series（幂级数）。

它是如下形式的级数：

```math
\sum_{k=0}^{\infty} a_k x^k
```

或者，更一般地，

```math
\sum_{k=0}^{\infty} a_k (x - c)^k .
```

它体现了「无限长」多项式 $a_0 + a_1 x + a_2 x^2 + \cdots + a_k x^k + \cdots$ 这一概念。

我们在第 9 章建立的材料将使我们在本章能够证明：幂级数在很大程度上可以像真正的多项式那样加以处理，即它们可以被逐项积分（term-by-term integration）与term-by-term differentiation（逐项求导）。

发展这一理论的主要原因在于，它使得函数能够以级数的形式得到表示。

这大大扩充了我们能够处理的函数类。

并非所有在应用中出现的函数都能表示为初等函数（elementary functions）的有限组合，即 $e^x$、$x^p$、$\sin x$、$\cos x$ 等函数的组合。

因此，若我们停留在初等微积分课程的水平，就必然无法解决许多问题，因为我们无法以任何方式表达解题所需的函数。

对于一大类重要的问题而言，能够表示为幂级数的那些函数——即所谓的 analytic function（解析函数）——恰好正是所需要的函数。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">10.2 Power Series: Convergence（幂级数：收敛）</span>

我们从幂级数的形式定义（formal definition）开始。

> <span style='color:#1e8449;'>[note] Note（译者注）:</span> 开章先建立第一性原理直觉：power series（幂级数）就是「无限次多项式」，收敛半径要回答的是——离中心 $c$ 多远以内，系数序列 $\{a_k\}$ 的增长能被因子 $(x-c)^k$ 的几何收缩压住。逐项看，$|a_k(x-c)^k|=|a_k|\cdot|x-c|^k$ 是两个因素的赛跑：系数随 $k$ 的指数增长率 $s=\limsup_k\sqrt[k]{|a_k|}$ 对抗每步乘法 $|x-c|$。若 $|x-c|<1/s$，项最终被几何级数 $\rho^k$（$\rho<1$）支配，绝对收敛；若 $|x-c|>1/s$，项不趋于零，trivial test（平凡检验）判其发散。因此 geometric series（几何级数）$\sum x^k$ 是一切幂级数的「计量单位」，所有判定都归结为与它的比较。这也预告了 Theorem 10.8 的区间结构：收敛与否只依赖距离 $|x-c|$ 这一个标量、与方向无关，收敛集必然是关于中心对称的区间，最多剩两个端点需要单独裁决。整条实数轴的问题被压缩成「一个数 $R$ 加两个边界点」，与二分搜索把问题空间对半折叠是同一哲学。

---

<!-- ===== 书页 405（PDF 页 21）===== -->

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Section 10.2 Power Series: Convergence（幂级数：收敛性）</span>

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">Definition 10.1（定义 10.1）</span>
> <span style="color:#7f8c8d;">TBB §10.2, p.405</span>

设 $\{a_k\}$ 为一个实数序列，并设 $c \in \mathbb{R}$。形如
```math
\sum_{k=0}^{\infty} a_k (x-c)^k = a_0 + a_1 (x-c) + a_2 (x-c)^2 + \cdots
```
的级数称为以 $c$ 为中心的 power series（幂级数）。这些数 $a_k$ 称为该幂级数的 coefficients（系数）。

关于幂级数
```math
\sum_{k=0}^{\infty} a_k (x-c)^k
```
在其上收敛的点的集合，我们能说些什么呢？立即可以清楚看到，该级数在其中心 $c$ 处收敛。还可能有哪些可能的情形呢？一组例子既说明了这些方法，也基本上展示了全部可能的情形。

<span style="color:#2471a3;">**[example]**</span> **Example 10.2（例 10.2）**
> <span style="color:#7f8c8d;">TBB §10.2, p.405</span>

这个简单的例子
```math
\sum_{k=1}^{\infty} k^k x^k = x + 4x^2 + 27x^3 + \cdots
```
表明，幂级数可以在除中心以外的每一个点都发散。注意在本例中 $k^k x^k = (kx)^k$，除非 $x = 0$，否则它不趋于 0，因此由 trivial test（平凡检验）可知该级数对每个 $x \neq 0$ 都发散。于是该级数的收敛集为集合 $\{0\}$。

<span style="color:#2471a3;">**[example]**</span> **Example 10.3（例 10.3）**
> <span style="color:#7f8c8d;">TBB §10.2, p.405</span>

熟悉的 geometric series（几何级数）
```math
\sum_{k=0}^{\infty} x^k
```
应被视为所有幂级数中最基本的一个。我们知道，该级数恰好收敛于区间 $(-1, 1)$ 上，而在其他一切地方发散。

<span style="color:#2471a3;">**[example]**</span> **Example 10.4（例 10.4）**
> <span style="color:#7f8c8d;">TBB §10.2, p.405</span>

级数
```math
\sum_{k=1}^{\infty} \frac{x^k}{k}
```
的系数为 $a_k = 1/k$，root test（根值判别法）给出
```math
s = \limsup_{k \to \infty} \sqrt[k]{|x|^k / k} = |x|.
```
（请验证这一点！）于是该级数在 $(-1, 1)$ 上收敛，并对 $|x| > 1$ 发散。在区间 $(-1, 1)$ 的两个 endpoints（端点）处需要另一种检验方法。我们看到，当 $x = 1$ 时这就是熟悉的 harmonic series（调和级数），因而发散；而当 $x = -1$ 时，这就是熟悉的交错调和级数，因而非绝对地收敛。interval of convergence（收敛区间）为 $[-1, 1)$。注意，该级数在该区间的两个端点中仅在一个端点处收敛。

> **Footnote 1（脚注 1）**：讨论幂级数所需的 root test 形式要用到 limit superior（上极限）；为此可能需要学习 Section 2.13（第 2.13 节）。


---

<!-- ===== 书页 406（PDF 页 22）===== -->

<span style="color:#2471a3;">**[example]**</span> **Example 10.5（例 10.5）**
> <span style="color:#7f8c8d;">TBB §10.2, p.406</span>

级数
```math
\sum_{k=1}^{\infty} \frac{x^k}{k^2}
```
在 $[-1, 1]$ 上收敛，在其他地方发散。这里同样可以借助 root test（或 ratio test，比值判别法）。不过更简单的做法是注意到
```math
\left| \frac{x^k}{k^2} \right| \le \frac{1}{k^2}
```
对所有 $|x| \le 1$ 成立，从而通过与收敛级数 $\sum_{k=0}^{\infty} 1/k^2$ 的 comparison test（比较检验）在 $[-1, 1]$ 上得到收敛性。若 $|x| > 1$，则各项 $|x^k/k^2| \to \infty$，于是平凡地，该级数发散。注意，这里该级数在区间 $[-1, 1]$ 上收敛，并且在那里是 absolutely convergent（绝对收敛）的。

<span style="color:#2471a3;">**[example]**</span> **Example 10.6（例 10.6）**
> <span style="color:#7f8c8d;">TBB §10.2, p.406</span>

将 root test 应用于级数
```math
\sum_{k=1}^{\infty} \frac{x^k}{k^k}
```
得到
```math
\lim_{k \to \infty} \sqrt[k]{\frac{|x|^k}{k^k}} = |x| \lim_{k \to \infty} \frac{1}{k} = 0.
```
（这里也可以使用 ratio test。）由此可知该级数对所有 $x \in \mathbb{R}$ 收敛。或许在这个具体例子中更简单的方法是使用 comparison test 以及下述事实：
```math
\left| \frac{x}{k} \right|^k < \frac{1}{2^k} \quad \text{when } k \ge 2|x|.
```
于是通过与一个几何级数的比较，该级数在任意 $x$ 处收敛。因此该级数的收敛集为 $(-\infty, \infty)$，再次与前面几个例子一样，是一个区间。

一般地，正如这些例子所暗示的，幂级数的收敛点集构成一个区间，而 root test 的应用是确定该区间的关键工具。让我们把这个检验应用于级数
```math
\sum_{k=0}^{\infty} a_k (x-c)^k.
```
设
```math
s = \limsup_{k \to \infty} \sqrt[k]{|a_k|}.
```
那么
```math
\limsup_{k \to \infty} \sqrt[k]{|a_k|\,|x-c|^k} = \limsup_{k \to \infty} \sqrt[k]{|a_k|}\,|x-c| = s|x-c|.
```
由 root test，当 $s|x-c| < 1$ 时该级数绝对收敛，当 $s|x-c| > 1$ 时发散。若 $0 < s < \infty$，则该级数在区间
```math
(c - 1/s, c + 1/s)
```
上收敛，并对区间
```math
[c - 1/s, c + 1/s]
```
之外的 $x$ 发散。


---

<!-- ===== 书页 407（PDF 页 23）===== -->

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">10.2 Power Series: Convergence（幂级数：收敛）</span>

在这些区间的端点 $x = c \pm 1/s$ 处，root test（根值判别法）对收敛性不能给出结论（inconclusive）。

因此 interval of convergence（收敛区间）是以下四种可能之一：$(c - 1/s, c + 1/s)$、$[c - 1/s, c + 1/s)$、$(c - 1/s, c + 1/s]$ 或 $[c - 1/s, c + 1/s]$。

若 $s = 0$，则该级数对所有 $x$ 值都收敛。

此时我们可以说收敛区间是 $(-\infty, \infty)$。

若 $s = \infty$，则该级数除平凡值 $x = c$ 外，对任何 $x$ 值都不收敛。

此时我们可以说收敛区间是退化的「区间」$\{c\}$。

因此该级数的 set of convergence（收敛集）是一个以 $c$ 为中心（centered at $c$）的区间。

这个区间可能是退化的（只由中心构成），也可能是整条实直线，还可能包含其 endpoint（端点）中的零个、一个或两个。

我们的下一个定理将总结到目前为止关于收敛性的讨论。

我们首先给出一个正式的定义。

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">Definition 10.7（定义 10.7）</span>
> <span style="color:#7f8c8d;">TBB §10.2, p.407</span>

设 $\sum_{k=0}^{\infty} a_k (x - c)^k$ 是一个 power series（幂级数）。则数

```math
R = \frac{1}{\limsup_{k\to\infty} \sqrt[k]{|a_k|}}
```

称为该级数的 radius of convergence（收敛半径）。这里我们约定：若 $\limsup_{k\to\infty} \sqrt[k]{|a_k|} = 0$，则解释为 $R = \infty$；若 $\limsup_{k\to\infty} \sqrt[k]{|a_k|} = \infty$，则 $R = 0$。

**Note（注）**：本书讨论 real analysis（实分析），但幂级数的完整理论更自然地适合 complex analysis（复分析）的框架。

在该框架中，幂级数在一个以复平面中的复数 $c$ 为中心、半径为 $R = \frac{1}{\limsup_{k\to\infty} \sqrt[k]{|a_k|}}$ 的「circle of convergence（收敛圆）」内收敛。

这就解释了「radius of convergence（收敛半径）」这一术语的由来。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 10.8（定理 10.8）</span>
> <span style="color:#7f8c8d;">TBB §10.2, p.407</span>

设 $\sum_{k=0}^{\infty} a_k (x - c)^k$ 是一个收敛半径为 $R$ 的幂级数。

1. 若 $R = 0$，则该级数仅在 $x = c$ 处收敛。
2. 若 $R = \infty$，则该级数对所有 $x$ absolutely convergent（绝对收敛）。
3. 若 $0 < R < \infty$，则该级数对所有满足 $|x - c| < R$ 的 $x$ 绝对收敛，并对所有满足 $|x - c| > R$ 的 $x$ 发散。

> <span style='color:#1e8449;'>[note] Note（译者注）:</span> Definition 10.7 的 Cauchy-Hadamard 公式 $R=1/\limsup_k\sqrt[k]{|a_k|}$ 值得先做一次量纲检验：若 $x$ 带长度量纲，$a_k$ 的量纲必含 $x$ 的 $-k$ 次方，于是 $\sqrt[k]{|a_k|}$ 的量纲是长度的倒数，取倒数得长度——半径必须是长度，公式是唯一量纲自洽的写法。注意公式的推导只有一步：$\limsup_k\sqrt[k]{|a_k||x-c|^k}=s|x-c|$，因为常数因子可以提出上极限——收敛与否就被压进这一个不等式。为什么用 limit superior（上极限）而非普通极限？因为 $\sqrt[k]{|a_k|}$ 可以不收敛（奇偶项各走一条轨道震荡），而上极限只追踪「最终最坏轨道」，且对有限个异常系数免疫——正如 CSAPP 浮点运算里，少数低位舍入扰动不改变指数阶，真正的增长率只由尾部决定。两个约定要学会翻译：$s=0$ 表示系数衰减得比任何几何级数都快（如 $a_k=1/k!$ 与 $1/k^k$），半径无穷；$s=\infty$ 表示系数增长快过任何几何级数（如 $k^k$），半径为零。还要注意 root test（根值判别法）在 $s|x-c|=1$ 处恰好「哑火」：全部不确定被压进至多两个端点，这正是下一条定理四种区间类型的来历。

---

<!-- ===== 书页 408（PDF 页 24）===== -->

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 我们首先考虑 $R = 0$ 的情形。
> 此时 $\limsup_{k\to\infty} \sqrt[k]{|a_k|} = \infty$，于是对 $x \neq c$，有
> $\limsup_{k\to\infty} \sqrt[k]{|a_k| \, |x - c|^k} = |x - c| \cdot \limsup_{k\to\infty} \sqrt[k]{|a_k|} = \infty$。
> 由 root test（根值判别法），该级数在 $x \neq c$ 时不可能收敛。
> 其余情形与前述例子之后的讨论类似，同样可由根值判别法建立。$\blacksquare$

一般而言，一个具有有限收敛半径 $R$ 的幂级数 $\sum_{k=0}^{\infty} a_k x^k$，
其收敛集（set of convergence）必须是以下四个区间之一，
即 $(-R, R)$、$[-R, R]$、$(-R, R]$ 或 $[-R, R)$。

正如我们从例子中所看到的，这四种情形每一种都可能发生。

其余的可能性有两种：
一是收敛半径 $R = 0$ 的级数，此时收敛集平凡地为 $\{0\}$；
二是收敛半径 $R = \infty$ 的级数，此时收敛集为整条实直线。

还要注意，若该级数在 $x = R$ 或 $x = -R$ 处absolutely convergent（绝对收敛），
则它必然在整个 $[-R, R]$ 上绝对收敛。

不过，该级数有可能在一个端点非绝对收敛（nonabsolutely convergent），
而在另一个端点却不绝对收敛。

<span style="color:#7f8c8d">（本页 Exercise 10.2.1–10.2.3 为习题区，按约定跳过）</span>

> <span style='color:#1e8449;'>[note] Note（译者注）:</span> Theorem 10.8 把前面的观察提升为结构定理：幂级数的收敛集永远是以 $c$ 为中心的一个区间——退化点 $\{c\}$、整条实直线，或 $(-R,R)$、$[-R,R)$、$(-R,R]$、$[-R,R]$ 四选一。结构为什么如此干净？因为根值判别法算出的 $\limsup\sqrt[k]{|a_k(x-c)^k|}=s|x-c|$ 只依赖距离这一个标量：一旦某点 $x_0$（距离 $r$）收敛，其项必有界，comparison test（比较检验）就把绝对收敛性免费送给所有 $|x-c|<r$ 的点，收敛集自动是「同心实心块」，绝不可能是散点拼盘。例 10.3 到例 10.6 恰好穷举全部四种类型，请逐例核对端点行为。于是得到两步模板——**「先定半径，再验端点」**：第一步 Cauchy-Hadamard 定出 $R$，一锤定音区间主体；第二步只在至多两个端点换用 Leibniz test（Leibniz 判别法）、比较检验等精细工具。这正如 CLRS 分治设计里主干用通用递归、退化边界单独处理的套路，与 6.042J 闭区间套的直觉也同源：结构由内部机制决定，边界只是少数需要单独裁决的例外。

---

<!-- ===== 书页 409（PDF 页 25）===== -->

<!-- page_025：习题区，按约定跳过 -->


---

<!-- ===== 书页 410（PDF 页 26）===== -->

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">10.3 Uniform Convergence（一致收敛）</span>

到目前为止，我们已经对任意幂级数（power series）的收敛集的性质有了完整的认识。为了把第 9 章的许多定理应用于幂级数的逐项积分（term by term integration）或逐项求导（term by term differentiation）等问题，我们需要考察与幂级数的uniform convergence（一致收敛）相关的问题。下一个定理正是要处理这一点，同时也对迄今为止关于收敛的讨论作一个总结。

我们重述 Theorem 10.8（定理 10.8）的收敛结果，但这一次补充关于一致收敛的讨论。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 10.9（定理 10.9）</span>
> <span style="color:#7f8c8d;">TBB §10.3, p.410</span>

设 $\sum_{k=0}^{\infty} a_k (x-c)^k$ 是收敛半径为 $R$ 的幂级数。

1. 若 $R = 0$，则级数仅在 $x = c$ 处收敛。
2. 若 $R = \infty$，则级数在任何紧区间（compact interval）$[a,b]$ 上绝对收敛且一致收敛。
3. 若 $0 < R < \infty$，则级数在完全位于区间 $(c-R, c+R)$ 内部的任何区间 $[a,b]$ 上绝对收敛且一致收敛。

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 要验证 (2) 与 (3)，我们选取 $0 < \rho < R$，使得区间 $[a,b]$ 包含在区间 $(c-\rho, c+\rho)$ 之内。固定 $\rho_0 \in (\rho, R)$。于是
>
> ```math
> \limsup_{k\to\infty} \sqrt[k]{|a_k|} = \frac{1}{R} < \frac{1}{\rho_0}.
> ```
>
> 因此存在 $N \in \mathbb{N}$，使得对所有 $k \geq N$ 均有
>
> ```math
> \sqrt[k]{|a_k|} < \frac{1}{\rho_0}.\tag{1}
> ```
>
> 对于 $k \geq N$ 且 $|x - c| \leq \rho$，我们计算得
>
> ```math
> |a_k (x-c)^k| \leq |a_k| \rho^k < \left(\frac{\rho}{\rho_0}\right)^k,
> ```
>
> 其中最后一个不等式由 (1) 得出。由于 $\rho/\rho_0 < 1$，可知
>
> ```math
> \sum_{k=0}^{\infty} \left(\frac{\rho}{\rho_0}\right)^k < \infty.
> ```
>
> 于是由 Weierstrass M-test（Weierstrass M 判别法）（Theorem 9.16，定理 9.16）可知，该级数在集合 $\{x : |x - c| < \rho\}$ 上绝对收敛且一致收敛，进而在子集 $[a,b]$ 上亦然。∎

若幂级数的收敛区间为 $(-R, R)$，那么 Theorem 10.9（定理 10.9）的断言 (3) 无疑已是能够作出的最佳结论（参见 Exercise 10.3.3，习题 10.3.3）。geometric series（几何级数）$\sum_{n=0}^{\infty} x^n$ 为此提供了最清晰的例证。该级数在 $(-1, 1)$ 上收敛，但在整个收敛区间 $(-1, 1)$ 上并不一致收敛；不过它在任何 $[a, b] \subset (-1, 1)$ 上都一致收敛。

要改进这一点，我们可以提出如下问题：若 $R$ 是某幂级数的收敛半径，且收敛区间为 $[-R, R]$、$(-R, R]$ 或 $[-R, R)$，能否……（原文句子在页末截断，未完待续。）

> <span style='color:#1e8449;'>[note] Note（译者注）:</span> Theorem 10.9 的证明藏着全章最重要的模板，我称之为**「几何余量法」**：先取 $\rho<R$ 使 $[a,b]\subset(c-\rho,c+\rho)$，再固定一个夹在中间的「余量点」$\rho_0\in(\rho,R)$。上极限不等式 $1/R<1/\rho_0$ 是严格的，严格性等价于存在有限 $N$，使 $k\ge N$ 时恒有 $\sqrt[k]{|a_k|}<1/\rho_0$；于是尾项 $|a_k(x-c)^k|\le|a_k|\rho^k<(\rho/\rho_0)^k$，比值 $\rho/\rho_0<1$，几何级数收敛，Weierstrass M-test 给出绝对且一致收敛。第一性原理：极限只承诺「最终趋势」，一致收敛却要求统一 $N$ 控制整段区间，$\rho_0$ 就是把趋势兑换成统一常数的缓冲垫——与 CLRS 复杂度证明里预留常数余量同构。为什么只能落在紧区间？因为最坏点会滑向端点：几何级数在 $(-1,1)$ 上，尾项 $x^n$ 的上确界恒为 1（不趋于 0），而余项 $x^{n+1}/(1-x)$ 的上确界甚至为 $+\infty$——最坏点不断滑向端点，故不能在 $(-1,1)$ 上一致收敛；$[a,b]$ 到端点的距离恒正，最坏点被锁在安全距离之外（这正是 6.042J 闭区间套/紧致的直觉）。🎥 Colding 在 V22 里概括的正是这幅图景：「this here converts to this limit here uniformly on each interval of this form here, where L here is strictly less than 1. And this is, again, is Weinstrass M-test.」（翻译：这个部分和级数在这种形式的每个区间上——其中 L 严格小于 1——一致收敛到这个极限，而这用到的仍然是 Weierstrass M 判别法。）

---

<!-- ===== 书页 411（PDF 页 27）===== -->

Part009 · 书页 411 行内双语翻译

那么，能否把uniform convergence（一致收敛）推广到端点？
如果在某个端点 $R$（或 $-R$）处的收敛是绝对收敛，那么应用 Weierstrass M-test（Weierstrass M 判别法）立即表明：该级数在 $[-R, R]$ 上绝对收敛且一致收敛。
对于非绝对收敛的情形，则需要更精细的判别法，此时需要借助第 9.3.3 节中建立的材料。
为便于查阅，下面的定理重复了 Theorem 10.9 中的第三条断言。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 10.10（定理 10.10）</span>
> <span style="color:#7f8c8d;">TBB §10.3, p.411</span>

设幂级数 $\sum_{k=0}^{\infty} a_k (x-c)^k$ 具有有限正 radius of convergence（收敛半径）$R$ 与 interval of convergence（收敛区间）$I$。

1. 若 $I = [c-R, c+R]$，则该级数在 $[c-R, c+R]$ 上一致收敛（但不一定绝对收敛）。
2. 若 $I = (c-R, c+R]$，则该级数在任意区间 $[a, c+R]$（其中 $c-R < a < c+R$）上一致收敛（但不一定绝对收敛）。
3. 若 $I = [c-R, c+R)$，则该级数在任意区间 $[c-R, b]$（其中 $c-R < b < c+R$）上一致收敛（但不一定绝对收敛）。
4. 若 $I = (c-R, c+R)$，则该级数在任意区间 $[a, b]$（其中 $c-R < a < b < c+R$）上一致收敛且绝对收敛。

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 就证明的目的而言，我们可以取 $c = 0$。
> 让我们考察具有代表性的情形 $I = (c-R, c+R] = (-R, R]$。考虑区间 $[a, 0]$（其中 $-R < a < 0$）与 $[0, R]$。
> 级数在 $[a, 0]$ 上的一致收敛是显然的，因为这个区间完全包含在收敛区间内部。
>
> 现在我们考察 $[0, R]$ 上的一致收敛。我们考虑级数
>
> ```math
> \sum_{k=0}^{\infty} a_k x^k = \sum_{k=0}^{\infty} A_k t^k,
> ```
>
> 其中 $A_k = a_k R^k$，$t = x/R$。
> 由我们的假设，级数 $\sum_{k=0}^{\infty} A_k t^k$ 在 $0 \le t \le 1$ 上收敛。
> 注意 $\sum_{k=0}^{\infty} A_k$ 收敛，而序列 $\{t^k\}$ 在区间 $[0, 1]$ 上单调收敛。
> 由 Theorem 9.19 的一个变体（见 Exercise 9.3.26），该级数在 $t \in [0, 1]$ 上一致收敛。
> 这很容易转化为断言：我们的原级数在 $x \in [0, R]$ 上一致收敛。
> 于是，由于该级数在 $[a, 0]$ 和 $[0, R]$ 上一致收敛，我们就得到 $[a, R]$ 上的一致收敛，正如所要求的那样。
> 其余情形可类似地处理。

¥


---

<!-- ===== 书页 412（PDF 页 28）===== -->

Part009 · 书页 412 行内双语翻译

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">10.4 Functions Represented by Power Series（用幂级数表示的函数）</span>
现在假设幂级数 $\sum_{k=0}^{\infty} a_k (x-c)^k$ 具有正的或无限的 radius of convergence（收敛半径）$R$。那么该级数至少在区间 $(c-R, c+R)$ 上表示一个函数 $f$：

```math
f(x) = \sum_{k=0}^{\infty} a_k (x-c)^k \quad \text{for } |x-c| < R. \tag{2}
```

如果该级数在一个或两个端点处收敛，那么它表示 $[c-R, c+R)$、$(c-R, c+R]$ 或 $[c-R, c+R]$ 上的一个函数。
关于函数 $f$，我们能说些什么？按照贯穿第 9 章一直激励我们的那些问题，我们可以问：

1. 函数 $f$ 在其 domain of definition（定义域）上连续吗？
2. 能否通过对其级数逐项求导（termwise differentiation）来对 $f$ 求导？
3. 能否通过对其级数逐项积分（termwise integration）来对 $f$ 积分？
我们逐一处理这些问题，并发现一般而言每个问题的答案都是肯定的。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">10.4.1 Continuity of Power Series（幂级数的连续性）</span>

一个幂级数可能在一个区间上表示一个函数。这个函数必然连续吗？

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 10.11（定理 10.11）</span>
> <span style="color:#7f8c8d;">TBB §10.4, p.412</span>

由幂级数

```math
f(x) = \sum_{k=0}^{\infty} a_k (x-c)^k \tag{3}
```

表示的函数 $f$ 在其 interval of convergence（收敛区间）上连续。

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 这可由 Theorem 10.10 推出。例如，如果收敛区间是 $(c-R, c+R]$，那么我们可以证明 $f$ 在该区间的每一点处连续。
> 由于收敛在 $[c, c+R]$ 上一致，并且每个函数 $a_k (x-c)^k$ 都在 $[c, c+R]$ 上连续，因此函数 $f$ 也是如此（见 Corollary 9.23，推论 9.23）。对任意点 $x_0 \in (c-R, c)$，我们可以用同样的方式证明 $f$ 在 $x_0$ 处连续，只需注意到该级数在某个区间 $[a, c]$ 上一致收敛，其中 $a$ 的选择满足 $c-R < a < x_0 < c$。

¥

<span style="color:#2471a3;">**[example]**</span> **Example 10.12（例 10.12）**
> <span style="color:#7f8c8d;">TBB §10.4, p.412</span>

级数

```math
f(x) = \sum_{k=1}^{\infty} \frac{x^k}{k}
```

> <span style='color:#1e8449;'>[note] Note（译者注）:</span> Theorem 10.11 断言幂级数在其整个收敛区间上连续，证明策略是**「局部化＋一致收敛」**：连续性是局部性质，只关心每一点附近的行为，所以不需要整个区间上一致收敛，只要每一点的小闭邻域上一致收敛即可。对内部点，Theorem 10.9 在任何 $[a,b]\subset(c-R,c+R)$ 上给出一致收敛；对像 $x=c+R$ 这样被收进收敛区间的端点，Theorem 10.10 的情形 (2) 恰好保证在 $[a,c+R]$（$c-R<a<c+R$）上一致收敛。剩下的只用两条旧结论：部分和是多项式必连续，一致收敛的连续函数列其极限连续（Corollary 9.23）。链条「局部一致收敛 $\Rightarrow$ 逐点连续」是第 9 章机器的标准用法：把全局困难局部化绕开，与算法里「难的全区间问题拆成局部好解的子问题」同一哲学。例 10.12 正为此而来：$\sum x^k/k$ 在 $x=-1$ 条件收敛，连续性将把这个端点的级数和与 $-\ln 2$（注意原书此处符号印错，详见书页 413 译者注）钉在一起（下页完成计算）。

---

<!-- ===== 书页 413（PDF 页 29）===== -->

该级数在区间 $[-1, 1)$ 的每一点处收敛，因此这个函数在该区间的每一点都连续。我们将在下一节证明恒等式

```math
\log(1-x) = \sum_{k=1}^{\infty} \frac{x^k}{k}
```

对所有 $x \in (-1, 1)$ 成立（通过对 geometric series（几何级数）逐项积分）。由于我们还保证了在端点 $x = -1$ 处的连续性，可以得出结论

```math
\log 2 = \sum_{k=1}^{\infty} \frac{(-1)^k}{k}.（原文如此；按 Example 10.14 的正确恒等式 $-\log(1-x)=\sum_{k=1}^{\infty}x^k/k$，取 $x=-1$ 时应得 $\log 2=\sum_{k=1}^{\infty}\frac{(-1)^{k+1}}{k}=1-\frac12+\frac13-\cdots$，原书此处符号与下标有误，详见本页译者注。）
```

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">10.4.2 Integration of Power Series（幂级数的积分）</span>

如果一个函数由 power series（幂级数）表示，能否通过逐项积分该幂级数来对该函数积分呢？

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 10.13（定理 10.13）</span>
> <span style="color:#7f8c8d;">TBB §10.4, p.413</span>

设函数 $f$ 由幂级数

```math
f(x) = \sum_{k=0}^{\infty} a_k (x-c)^k
```

表示，其收敛区间为 $I$。则对区间中的每一点 $x$，$f$ 在 $[c, x]$ 上（若 $x < c$ 则为 $[x, c]$）可积，并且

```math
\int_c^x f(t)\, dt = \sum_{k=0}^{\infty} \frac{a_k}{k+1}(x-c)^{k+1}.
```

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 设 $x$ 为收敛区间中的一点。级数 $\sum_{k=0}^{\infty} a_k (x-c)^k$ 在 $[c, x]$ 上（若 $x < c$ 则为 $[x, c]$）一致收敛，故该级数可以逐项积分（Theorem 9.29）。$\blacksquare$

<span style="color:#2471a3;">**[example]**</span> **Example 10.14（例 10.14）**
> <span style="color:#7f8c8d;">TBB §10.4, p.413</span>

考虑 geometric series（几何级数）

```math
\frac{1}{1-x} = \sum_{k=0}^{\infty} x^k
```

其收敛半径为 $1$，因此只要停留在区间 $(-1, 1)$ 内就可以逐项积分。于是

```math
-\log(1-x) = \int_0^x \frac{1}{1-t}\, dt = \sum_{k=0}^{\infty} \frac{1}{k+1}x^{k+1}
```

对所有 $-1 < x < 1$ 成立。我们不能从这个定理推断该积分可以延拓到 $(-1, 1)$ 的端点。然而，新的级数在 $x = -1$ 处也收敛，因此我们可以应用 Theorem 10.11 来证明刚才证得的恒等式实际上在 $[-1, 1)$ 上成立。

> <span style='color:#1e8449;'>[note] Note（译者注）:</span> Theorem 10.13 是全章最「便宜」的定理：证明只有一句——Theorem 10.10 给出 $[c,x]$ 上的一致收敛，Theorem 9.29 允许逐项积分，微积分基本定理算出 $\int_c^x(t-c)^k\,dt=(x-c)^{k+1}/(k+1)$。便宜是因为苦力在第 9 章已做完：9.29 证明了「一致收敛 $\Rightarrow$ 积分与求和可换序」，幂级数只需按时交出局部一致收敛。第一性原理回顾：积分是极限运算，与无穷求和换序本质是两次极限交换次序，一致收敛就是那张交换许可证。另有一个被低估的事实：积分不改变收敛半径（把 Lemma 10.15 反向套用于积分后的级数即可），却可能「拯救」端点——几何级数在 $\pm1$ 都发散，积分后的 $\sum x^{k+1}/(k+1)$ 在 $x=-1$ 收敛；再借 Theorem 10.11 的端点连续性把等式延拓到 $[-1,1)$，得到 $\ln 2=1-\frac12+\frac13-\cdots$（此处已将原书书页 413 的符号错误修正——原书写作 $\log 2=\sum(-1)^k/k$，那是 $-\ln 2$ 的反式；$\log(1-x)=\sum x^k/k$ 取 $x=-1$ 时左侧为 $\log 2$、右侧为 $-\sum(-1)^k/k$）。模板命名**「区间内等式＋端点连续＝端点等式」**。给 18.065 留个路标：把 $x$ 换成矩阵、$|x|<1$ 换成 spectral radius（谱半径）小于 1，例 10.14 正是 Neumann 级数 $(I-A)^{-1}=I+A+A^2+\cdots$ 的纯量原型。

---

<!-- ===== 书页 414（PDF 页 30）===== -->

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">10.4.3 Differentiation of Power Series（幂级数的求导）</span>

如果一个函数由 power series（幂级数）表示，能否通过逐项求导该幂级数来对该函数求导呢？

注意，对于连续性和积分，我们能够直接从有关 uniform convergence（一致收敛）的一般定理证明 Theorem 10.11 与 Theorem 10.13。要证明逐项求导的定理，我们需要检验导数级数的一致收敛性。下面的 lemma（引理）提供了我们所需的结论。

### <span style="color:#2471a3;">**[lemma]**</span> <span style="color:#c0392b">Lemma 10.15（引理 10.15）</span>
> <span style="color:#7f8c8d;">TBB §10.4, p.414</span>

设 $\sum_{k=0}^{\infty} a_k (x-c)^k$ 的收敛半径为 $R$。则通过逐项求导得到的级数

```math
\sum_{k=1}^{\infty} k a_k (x-c)^{k-1}
```

也具有相同的收敛半径 $R$。

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 该级数的收敛半径为 $R = \frac{1}{\limsup_{k} \sqrt[k]{|a_k|}}$。求导后级数的收敛半径为 $R' = \frac{1}{\limsup_{k} \sqrt[k]{|k a_k|}}$。但由于当 $k \to \infty$ 时 $\sqrt[k]{k} \to 1$，我们立即看出这两个表达式相等。（它们可能都为零，也可能都为无穷大。）$\blacksquare$

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 10.16（定理 10.16）</span>
> <span style="color:#7f8c8d;">TBB §10.4, p.414</span>

设 $\sum_{k=0}^{\infty} a_k (x-c)^k$ 的收敛半径为 $R > 0$，并设

```math
f(x) = \sum_{k=0}^{\infty} a_k (x-c)^k
```

当 $|x-c| < R$ 时成立。则 $f$ 在 $(c-R, c+R)$ 上可微，并且对每个 $x \in (c-R, c+R)$ 有

```math
f'(x) = \sum_{k=1}^{\infty} k a_k (x-c)^{k-1}.
```

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 由前面的引理可知，级数 $\sum_{k=1}^{\infty} k a_k (x-c)^{k-1}$ 的收敛半径为 $R$。因此该级数在包含于 $(c-R, c+R)$ 内的任意 compact interval（紧区间）$[a, b]$ 上一致收敛。由于 $(c-R, c+R)$ 中的每个 $x$ 值都可以放入某个这样的区间 $[a, b]$，由 Corollary 9.35 立即推得当 $|x-c| < R$ 时 $f'(x) = \sum_{k=1}^{\infty} k a_k (x-c)^{k-1}$。$\blacksquare$

我们可以对求导后的级数应用同样的论证，再求导一次。由展开式

```math
f'(x) = \sum_{k=1}^{\infty} k a_k (x-c)^{k-1}
```

> <span style='color:#1e8449;'>[note] Note（译者注）:</span> Lemma 10.15 的全部关键是一句极限事实：$\sqrt[k]{k}\to1$（写成 $e^{(\ln k)/k}$，指数趋于 0）。含义：求导给系数乘上的因子 $k$ 只是多项式增长，在开 $k$ 次方根的「指数率测量仪」下完全隐形——根值判别法只读取系数的指数阶，正如 CLRS 渐进分析里 $n^c$ 因子不改变 $2^n$ 的底数，$\sqrt[k]{\cdot}$ 就是系数序列的「底数分类器」。于是 $\limsup\sqrt[k]{|ka_k|}=\limsup\sqrt[k]{|a_k|}$，半径分毫未动。Theorem 10.16 随即接线：导数级数半径同为 $R$，由 Theorem 10.9 在每个紧区间上一致收敛，Corollary 9.35 准许「先求导后求和」交换。注意半径不变但端点命运可变——$\sum x^k/k^2$ 在 $x=1$ 收敛，逐项求导后该点却是调和级数发散，所以结论只承诺开区间 $(c-R,c+R)$ 内的逐项求导。幂级数类因此对求导封闭，像多项式一样，「可像多项式般操作」的承诺正式兑现。🎥 Colding 在 V22 里正是这样论证的：「So if you take the derivative term by term and you form this new power series, then it has the same radius of convergence as the original.」（翻译：所以如果你逐项求导并组成这个新幂级数，它就和原级数有相同的收敛半径。）

---

<!-- ===== 书页 415（PDF 页 31）===== -->

Part009 · 书页 415 行内双语翻译

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">10.4 Functions Represented by Power Series（幂级数表示的函数）</span>

于是我们得到 $f''(x)$ 的一个公式：
```math
f''(x) = \sum_{k=2}^{\infty} k(k-1)a_k (x-c)^{k-2}.
```

让我们把 $f(x)$、$f'(x)$ 与 $f''(x)$ 的公式明确地写出来：

```math
f(x) = a_0 + a_1 (x-c) + a_2 (x-c)^2 + a_3 (x-c)^3 + \cdots
```
```math
f'(x) = a_1 + 2a_2 (x-c) + 3a_3 (x-c)^2 + \cdots
```
```math
f''(x) = 2a_2 + 3 \cdot 2a_3 (x-c) + \cdots
```

这些表达式在区间 $(c-R, c+R)$ 内成立。在 $x = c$ 处，我们得到 $f(c) = a_0$、$f'(c) = a_1$ 以及 $f''(c) = 2a_2$。

若继续照此进行，我们便可得到 $f$ 的所有阶derivative（导数）的幂级数展开，这就引出了下面的定理。其证明需要用到数学归纳法（mathematical induction），留作 Exercise 10.4.1。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 10.17（定理 10.17）</span>
> <span style="color:#7f8c8d;">TBB §10.4, p.415</span>

设 $\sum_{k=0}^{\infty} a_k (x-c)^k$ 的radius of convergence（收敛半径）为 $R > 0$。则函数
```math
f(x) = \sum_{k=0}^{\infty} a_k (x-c)^k
```
具有所有阶的导数，且这些导数可由反复term-by-term differentiation（逐项求导）得出。系数 $a_k$ 与 $f$ 在 $x = c$ 处的导数之间由公式
```math
a_k = \frac{f^{(k)}(c)}{k!}
```

相联系。

由 Theorem 10.17 我们推出：一个函数的任意两个幂级数表示（power series representation）必然完全相同。注意，要使这一结论成立，两个展开的中心（center）必须相同。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Uniqueness of Power Series（幂级数的唯一性）</span>

### <span style="color:#2471a3;">**[corollary]**</span> <span style="color:#c0392b">Corollary 10.18（推论 10.18）</span>
> <span style="color:#7f8c8d;">TBB §10.4, p.415</span>

设两个幂级数
```math
f(x) = \sum_{k=0}^{\infty} a_k (x-c)^k \qquad \text{与} \qquad g(x) = \sum_{k=0}^{\infty} b_k (x-c)^k
```

在某个以 $c$ 为中心的区间上一致（agree），即对某个正的 $\rho$ 以及所有满足 $|x-c| < \rho$ 的 $x$ 都有 $f(x) = g(x)$。那么对所有 $k = 0, 1, 2, \ldots$ 均有 $a_k = b_k$。

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*
> 结论由 Theorem 10.17 直接得出：
> ```math
> a_k = \frac{f^{(k)}(c)}{k!} = \frac{g^{(k)}(c)}{k!} = b_k
> ```
> 对所有 $k = 0, 1, 2, \ldots$ 成立。¥

> <span style='color:#1e8449;'>[note] Note（译者注）:</span> Theorem 10.17 把「求导一次」迭代成「求导任意次」：$f'$ 仍是半径 $R$ 的幂级数，可以再逐项求导，归纳下去。这正是 Exercise 10.4.1 要你写的证明，模板名**「导数阶归纳」**：$P(k)$ 断言 $f^{(k)}$ 有幂级数表示，基步是 Theorem 10.16，归纳步对 $f^{(k)}$ 再套一次 10.16。第一性原理的看点在于「在 $x=c$ 求值」这一步：$x=c$ 让所有含 $(x-c)^m$（$m>0$）的项清零，只剩常数项；一次求导对系数序列 $(a_0,a_1,a_2,\dots)$ 执行「左移并乘权重」$a_m\mapsto(m+1)a_{m+1}$，执行 $k$ 次后第 0 位恰为 $k!\,a_k$，于是 $a_k=f^{(k)}(c)/k!$ 被强制锁定。用 Strang 已给你的线性代数词汇说：$d/dx$ 作用在幂级数上就是系数空间的一个上移矩阵，$x=c$ 处取值就是读第 0 个坐标——系数与中心处各阶导数互为坐标变换。这同时预告「局部决定整体」：函数在 $c$ 附近的全部局部信息（各阶导数）足以钉死整条级数，唯一性推论就在下一页。

---

<!-- ===== 书页 416（PDF 页 32）===== -->

Part009 · 书页 416 行内双语翻译

<span style="color:#2471a3;">**[example]**</span> **Example 10.19（例 10.19）**
> <span style="color:#7f8c8d;">TBB §10.4, p.416</span>

指数函数（exponential function）的级数

```math
e^x = \sum_{k=0}^{\infty} \frac{x^k}{k!}
```

揭示了关于指数函数的一个关键事实：它就是自身的derivative（导数）。只需注意到

```math
\frac{d}{dx} e^x = \sum_{k=0}^{\infty} \frac{d}{dx} \frac{x^k}{k!} = \sum_{k=1}^{\infty} \frac{x^{k-1}}{(k-1)!} = e^x.
```

<span style="color:#2471a3;">**[example]**</span> **Example 10.20（例 10.20）**
> <span style="color:#7f8c8d;">TBB §10.4, p.416</span>

本节的材料也可用来获得指数函数的幂级数展开（power series expansion）。假设我们已知指数函数 $f(x) = e^x$ 确实具有幂级数展开

```math
f(x) = \sum_{k=0}^{\infty} a_k x^k.
```

那么其系数必然由我们已经得到的公式给出，即

```math
a_k = \frac{f^{(k)}(0)}{k!}.
```

但对 $f(x) = e^x$，显然对所有 $k$ 都有 $f^{(k)}(0) = 1$，因此该级数确实如我们所熟知的那样由 $a_k = 1/k!$ 给出。可是，我们怎样才能确信指数函数确实具有幂级数展开呢？这个论证只表明：若存在一个级数，那么这个级数必定恰好是 $\sum_{k=0}^{\infty} \frac{x^k}{k!}$。仍然存在这种可能——或许根本不存在这样的级数。这正是下一节的主题。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">10.4.4 Power Series Representations（幂级数表示）</span>

Corollary 10.18 表明：如果我们能以任何手段得到函数 $f$ 的一个幂级数表示（power series representation），那么该级数的系数必然由等式 $a_k = f^{(k)}(c)/k!$ 给出。特别地，$f$ 关于给定点的幂级数表示必定是唯一的。

<span style="color:#2471a3;">**[example]**</span> **Example 10.21（例 10.21）**
> <span style="color:#7f8c8d;">TBB §10.4, p.416</span>

例如，geometric series（几何级数）的求和公式可用来证明

```math
\frac{1}{1+x^2} = 1 - x^2 + x^4 - \cdots + (-1)^j x^{2j} + \cdots .
```

因此这个级数在区间 $(-1, 1)$ 上表示函数 $f(x) = \frac{1}{1+x^2}$。注意，当 $k$ 为奇数时系数 $a_k$ 为零，而当 $k = 2j$ 为偶数时 $a_{2j} = (-1)^j$。于是自动地得出：对偶数 $k = 2j$，

```math
\frac{f^{(k)}(0)}{k!} = a_k = (-1)^j
```

而所有奇数阶导数均为零。因此，在 $x = 0$ 处，

```math
\frac{d^k}{dx^k} \frac{1}{1+x^2} = 0.
```

> <span style='color:#1e8449;'>[note] Note（译者注）:</span> Corollary 10.18 的证明只有一行，战略地位却极高：$a_k=f^{(k)}(c)/k!=g^{(k)}(c)/k!=b_k$——在 $c$ 的某个小邻域上相等的两个幂级数，系数必须逐项相同。第一性原理：这等价于 monomial（单项式）族 $\{1,x-c,(x-c)^2,\dots\}$ 在函数空间里线性无关，同一函数的「坐标」唯一——正是 Strang 线性代数「基唯一决定坐标」的无穷维版本。实用上它给你一条「以级数换导数」的捷径：无论用什么合法手段（几何级数代入、乘、加）得到展开式，那一定就是唯一的那一个，系数公式自动生效——例 10.21 中 $1/(1+x^2)$ 的奇数阶导数在 0 处全为零、$f^{(2j)}(0)=(-1)^j(2j)!$，都是从几何级数免费推出的，手算高阶导数会痛苦得多。但例 10.20 同时敲了警钟（模板**「唯一性≠存在性」**）：系数公式只保证「若有展开，必是 Taylor 级数」，并不证明 $e^x$ 真有展开——候选级数 $\sum x^k/k!$ 半径无穷只是定义了一个新函数，它是否等于 $e^x$，要等 10.5 节用 Taylor 定理的余项去证。这正是 6.042J 的论证纪律：唯一解是必要条件，存在性必须单独论证。

---

<!-- ===== 书页 417（PDF 页 33）===== -->

Part009 · 书页 417 行内双语翻译

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">10.4 Functions Represented by Power Series（幂级数表示的函数）</span>

若 $k$ 为奇数，则导数为零；而当 $k = 2j$ 为偶数时，在 $x = 0$ 处有

```math
\frac{d^k}{dx^k}\left(\frac{1}{1+x^2}\right) = (-1)^j (2j)! \quad \text{at } x = 0.
```

**注意。**这里有一个值得深思的奇特事实。公式

```math
\frac{1}{1+x^2} = 1 - x^2 + x^4 - \cdots + (-1)^j x^{2j} + \cdots
```

恰好对 $-1 < x < 1$ 成立。但是这个恒等式左侧的函数对所有 $x$ 的值都有定义。我们本希望得到一个对所有 $x$ 成立的表示，却没有得到！

有时，获得一个函数的 power series（幂级数）展开公式最容易的方法，是使用公式

```math
a_k = \frac{f^{(k)}(c)}{k!}.
```

例如，我们正是用这种方法得到 $f(x) = e^x$ 的幂级数的。我们计算得 $f^{(k)}(x) = e^x$（$k = 0, 1, 2, \ldots$），因此对所有 $k$ 都有 $f^{(k)}(0) = 1$。于是该函数的级数展开（如果它确实有级数展开的话）必定是

```math
e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots = \sum_{k=0}^{\infty} \frac{x^k}{k!} \tag{4}
```

注意，该级数对所有 $x \in \mathbb{R}$ 收敛。在下一节中，我们将说明如何验证该等式对所有 $x$ 成立。

如果我们想要 $g(x) = e^{x^2}$ 的公式，本可以采用同样的思路，确定出所有导数 $g^{(k)}(0)$。然而最简单的方法，是直接把 $x^2$ 代入展开式 (4) 中的 $x$，得到

```math
e^{x^2} = 1 + x^2 + \frac{x^4}{2!} + \frac{x^6}{3!} + \cdots = \sum_{k=0}^{\infty} \frac{x^{2k}}{k!} \tag{5}
```

此外，从这个展开式出发，可用下列两种方式之一轻松得到 $2xe^{x^2}$ 的展开式：我们可以将 (5) 中的展开式乘以 $2x$，得到

```math
2xe^{x^2} = 2x + 2x^3 + \frac{2x^5}{2!} + \frac{2x^7}{3!} + \cdots = \sum_{k=0}^{\infty} \frac{2x^{2k+1}}{k!}.
```

或者，我们可以使用 Theorem 10.16，对 (5) term-by-term differentiation（逐项求导），得到

```math
2xe^{x^2} = \frac{d}{dx}e^{x^2} = 2x + \frac{4x^3}{2!} + \frac{6x^5}{3!} + \frac{8x^7}{4!} + \cdots = \sum_{k=0}^{\infty} \frac{2x^{2k+1}}{k!}.
```

你也许宁愿直接用公式 $a_k = f^{(k)}(c)/k!$ 去尝试得到这些展开式。

<!-- 本页页尾习题 10.4.1 按约定跳过 -->


---

<!-- ===== 书页 418（PDF 页 34）===== -->

Part009 · 书页 418 行内双语翻译

<!-- 本页上部习题 10.4.2–10.4.7 按约定跳过 -->

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">10.5 The Taylor Series（Taylor 级数）</span>

我们已经看到，如果幂级数 $\sum_{k=0}^{\infty} a_k (x-c)^k$ 在某个区间 $I$ 上收敛，那么该级数表示一个具有各阶导数的函数 $f$。
特别地，系数 $a_k$ 与 $f$ 在 $c$ 处的导数通过下式相联系：

```math
a_k = \frac{f^{(k)}(c)}{k!}.
```

于是我们称该级数为 $f$ 关于点 $x = c$ 的 Taylor series（Taylor 级数）。

让我们把问题倒过来问：什么样的函数 $f$ 在其定义域内具有 Taylor 级数表示？


---

<!-- ===== 书页 419（PDF 页 35）===== -->

Part009 · 书页 419 行内双语翻译

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">10.5 The Taylor Series（Taylor 级数）</span>

我们立刻看到，这样的函数必定在 $c$ 的一个 neighborhood（邻域）内是 infinitely differentiable（无穷可微）的，因为要使这样的级数成立，我们知道所有的导数 $f^{(k)}(c)$ 都必须存在。
但这足够吗？
如果我们从一个在包含点 $c$ 的区间 $I$ 上具有任意阶导数的函数出发，并写出级数

```math
\sum_{k=0}^{\infty} \frac{f^{(k)}(c)}{k!}(x-c)^k ,
```

我们或许会期望这正是我们想要的 representation（表示）。
事实上，如果存在一个有效的表示，那么必然就是它，因为这样的表示是唯一的。
但我们能确定该级数在 $I$ 上收敛到 $f$ 吗？
甚至能确定该级数在 $I$ 上收敛吗？
对这两个问题的答案都是"不"。

<span style="color:#2471a3;">**[example]**</span> **Example 10.22（例 10.22）**
> <span style="color:#7f8c8d;">TBB §10.5, p.419</span>

例如，考虑函数 $f(x) = \dfrac{1}{1+x^2}$。
这个函数在整个实数轴上都是无穷可微的。
它在 $x = 0$ 处的 Taylor series（Taylor 级数）为，正如我们在 Example 10.21 中所看到的，

```math
1 - x^2 + x^4 - x^6 + \cdots = \sum_{k=0}^{\infty} (-1)^k x^{2k} .
```

这个级数在 $|x| < 1$ 时收敛，但在 $|x| \geq 1$ 时发散。
它确实在区间 $(-1, 1)$ 上表示 $f$，但并不能在 $f$ 的完整定义域上表示 $f$。
事实上，不可能存在形如 $\sum_{k=0}^{\infty} a_k x^k$ 的级数在 $(-\infty, \infty)$ 上表示 $f$，因为那样的级数在 $(-1, 1)$ 上必与本级数一致，因而不可能与之有任何不同。
更糟的情况也是可能的。
例如，存在这样的无穷可微函数，其 Taylor 级数对每个 $c$ 的 radius of convergence（收敛半径）都为零；对这些函数而言，级数

```math
\sum_{k=0}^{\infty} \frac{f^{(k)}(c)}{k!}(x-c)^k
```

除 $x = c$ 外处处发散，并且这对所有 $c \in \mathbb{R}$ 都成立。
对这些函数来说，Taylor 级数无法表示该函数。
另一种令人不快的情形发生在 Taylor 级数收敛到错误的函数时。
这种可能性似乎更令人震惊！

<span style="color:#2471a3;">**[example]**</span> **Example 10.23（例 10.23）**
> <span style="color:#7f8c8d;">TBB §10.5, p.419</span>

考虑函数

```math
f(x) = \begin{cases} 0, & \text{if } x = 0, \\ e^{-1/x^2}, & \text{if } x \neq 0. \end{cases}
```

Exercise 10.5.4 给出了证明的梗概：$f$ 在实数轴上无穷可微，并且对 $k = 1, 2, 3, \ldots$ 有 $f^{(k)}(0) = 0$。
因此，$f$ 在 $x = 0$ 处的 Taylor 级数取形如 $\sum_{k=0}^{\infty} 0 \cdot x^k$ 的形式，所有系数都等于零。
这个级数在实数轴上收敛到零函数，所以它不能表示 $f$（除非在原点处），即使该级数对所有 $x$ 都收敛。
我们在此发现，在某种意义上"大多数"无穷可微函数都具有这个性质！

<span style="color:#7f8c8d">$^2$ 见 D. Morgenstern, *Math. Nach.*, 12 (1954), 第 74 页。</span>

> <span style='color:#1e8449;'>[note] Note（译者注）:</span> 本节把幂级数唯一性（Corollary 10.18）收束成一条行动纲领：若 $f$ 在 $c$ 附近真有幂级数表示，系数就被导数唯一锁定为 $f^{(k)}(c)/k!$，于是问题从「找一个级数」缩窄为「检验唯一候选——Taylor 级数」。检验有两道互相独立的关卡：级数是否收敛、收敛后是否回到 $f$，两者都可能失败——Example 10.22 在 $|x|\ge 1$ 处连收敛都谈不上，Example 10.23 处处收敛却收敛到零函数。$e^{-1/x^2}$ 反例的机制是「指数衰减压过一切多项式」：对 $x\ne0$，$f^{(k)}(x)$ 形如 $P_k(1/x)e^{-1/x^2}$（$P_k$ 是多项式），$x\to0$ 时趋于 0，故全部 $f^{(k)}(0)=0$——函数在原点比任何幂都「平」，非零信息藏在导数望远镜照不到的指数级深谷里。CSAPP 的呼应很精确：$|x|\le0.01$ 时 $e^{-1/x^2}\le e^{-10^4}\approx10^{-4343}$，小于 IEEE 双精度最小次正规数，直接 underflow（下溢）成 0——这个反例在浮点世界里真的会消失。结论：无穷可微只保证「每点都有各阶导数」，解析却要求这些局部数据能拼回原函数，脚注更提醒——某种意义上「大多数」无穷可微函数都不解析。

---

<!-- ===== 书页 420（PDF 页 36）===== -->

Part009 · 书页 420 行内双语翻译

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">10.5.1 Representing a Function by a Taylor Series（用 Taylor 级数表示函数）</span>

前面的讨论表明，我们不应自动假设函数 $f$ 的 Taylor 级数就表示 $f$。
然而，本章前面各节的发展确实帮助我们认识到，初等微积分中遇到的许多熟悉的 Taylor 级数都是有效的。

<span style="color:#2471a3;">**[example]**</span> **Example 10.24（例 10.24）**
> <span style="color:#7f8c8d;">TBB §10.5, p.420</span>

例如，从 geometric series（几何级数）

```math
\frac{1}{1+x} = \sum_{k=0}^{\infty} (-1)^k x^k
```

出发，我们可以应用 Theorem 10.13（对 power series（幂级数）逐项积分）来得到，对 $|x| < 1$，

```math
\ln(1+x) = \int_0^x \frac{1}{1+t}\,dt = \sum_{k=0}^{\infty} \int_0^x (-1)^k t^k\,dt = \sum_{k=0}^{\infty} \frac{(-1)^k}{k+1} x^{k+1} = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots .
```

我们可以注意到，逐项积分得到的级数在 $x = 1$ 处收敛，因此该收敛在 $[0, 1]$ 上是一致的。
由此可知，该表示对 $x \in (-1, 1]$ 成立，但对其他任何点都不成立。
在这个例子中，我们通过对一个已知有效的级数展开进行积分，得到了一个有效的 Taylor series expansion（Taylor 级数展开）。
为了研究 Taylor 级数一般的收敛性，让我们回到基础。
设 $f$ 在 $c$ 的一个邻域内是 infinitely differentiable（无穷可微）的。
对 $n = 0, 1, 2, \ldots$，令

```math
P_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(c)}{k!}(x-c)^k .
```

多项式 $P_n$ 称为 $f$ 在 $c$ 处的第 $n$ 个 Taylor polynomial（Taylor 多项式）。
差 $R_n(x) = f(x) - P_n(x)$ 称为第 $n$ 个 remainder function（余项函数）。
要使关于 $c$ 的 Taylor 级数在区间 $I$ 上收敛到 $f$，当且仅当 $R_n$ 在 $I$ 上 pointwise（逐点）趋于 $0$。

<span style="color:#2471a3;">**[example]**</span> **Example 10.25（例 10.25）**
> <span style="color:#7f8c8d;">TBB §10.5, p.420</span>

我们知道，geometric series 在区间 $(-1, 1)$ 上表示函数 $f(x) = (1-x)^{-1}$。
我们也可以依靠 remainder term（余项）来证明这个结果。
对 $x \neq 1$ 及 $n = 0, 1, 2, \ldots$，我们有

```math
\frac{1}{1-x} = 1 + x + x^2 + \cdots + x^n + \frac{x^{n+1}}{1-x} .
```

这里 $P_n(x) = 1 + x + x^2 + \cdots + x^n$，且 $R_n(x) = \dfrac{x^{n+1}}{1-x}$。
当 $|x| < 1$ 时，$R_n(x) \to 0$（$n \to \infty$）。
但我们有 $f(x) = P_n(x) + R_n(x)$。

> <span style='color:#1e8449;'>[note] Note（译者注）:</span> Example 10.24 要拆成「半径内」与「端点」两幕读。半径内是 Theorem 10.13 的标准用法：几何级数在 $[0,x]\subset(-1,1)$ 上一致收敛（Theorem 10.10），逐项积分合法，得到 $\ln(1+x)$ 的级数且半径保持为 1。右端点 $x=1$ 处积分后的级数 $\sum_{k=0}^{\infty}(-1)^k/(k+1)$ 由 Leibniz 判别法收敛，再由「端点收敛推出 $[0,1]$ 上一致收敛」把等式延拓，得到 $\ln2=1-\frac12+\frac13-\cdots$；左端点 $x=-1$ 是发散的调和级数，与 $\ln0$ 无定义一致。对比 Example 10.22 的两种端点命运：$1/(1+x^2)$ 的级数在 $\pm1$ 都发散，而逐项积分让一般项多出因子 $1/(k+1)$，端点收敛性只会变好。$1/(1+x^2)$ 在整个实数轴光滑、级数却止步于 $|x|<1$ 的原因在实轴上完全隐形：分母 $1+z^2$ 在 $z=\pm i$ 处为零，0 到 $\pm i$ 的距离恰为 1——收敛半径等于中心到最近奇点的距离。🎥 Colding 在 V21 里把这类「先证换序合法、再逐项算」的操作讲得直白：「if it was just a finite sum, it would be trivial. But it's an infinite sum. And so the natural question is, is it OK? ...is it OK to interchange the infinite sum taking the integral? And the answer is, it's OK.」（翻译：若只是有限和，事情就平凡了；但它是无限和，于是自然要问：可以吗？……把这个无限和与积分交换次序，可以吗？答案是：可以。）

---

<!-- ===== 书页 421（PDF 页 37）===== -->

Part009 · 书页 421 行内双语翻译

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">10.5 The Taylor Series（Taylor 级数）</span>

因此，函数 $f(x) = 1/(1-x)$ 的 Taylor series（Taylor 级数）在区间 $(-1, 1)$ 上表示 $f$。
当 $|x| \geq 1$ 时，remainder term（余项）并不趋于零。
与前文一样，我们看到这一表示被限制在区间 $(-1, 1)$ 内。

在比这个例子更一般的情形中，我们不会有余项的显式公式。
那我们应如何证明余项趋于零呢？
对于在 $c$ 的某个邻域 $I$ 内无穷可微（infinitely differentiable）的函数，我们可以使用在第 7.12 节中为余项函数 $R_n$ 得到的各种表达式。
特别地，余项的 Lagrange 形式（Lagrange's form of the remainder）使我们能够对 $n = 0, 1, 2, 3, \ldots$ 写出

```math
f(x) = P_n(x) + \frac{f^{(n+1)}(z)}{(n+1)!}(x-c)^{n+1},
```

其中 $z$ 位于 $x$ 与 $c$ 之间。
只要对导数 $f^{(n+1)}(z)$ 的大小有所了解，我们或许就能证明这一余项趋于零。
余项的积分形式（integral form of the remainder）则给出

```math
f(x) = P_n(x) + \frac{1}{n!}\int_c^x (x-t)^n f^{(n+1)}(t)\, dt.
```

同样，关于导数 $f^{(n+1)}(t)$ 大小的信息或许也能证明这个余项趋于零。

<span style="color:#2471a3;">**[example]**</span> **Example 10.26（例 10.26）**：让我们来证明 $\sin x$ 这一熟悉的 Taylor 级数：
> <span style="color:#7f8c8d;">TBB §10.5, p.421</span>

```math
\sin x = \sum_{k=0}^{\infty} \frac{(-1)^k}{(2k+1)!} x^{2k+1}.
\tag{6}
```

其余项不能用任何简单的方式表达，但可以用余项的 Lagrange 形式加以估计。
系数 $\frac{(-1)^k}{(2k+1)!}$ 可通过逐次计算 $f(x) = \sin x$ 的各阶导数并利用公式 $a_k = \frac{f^{(k)}(0)}{k!}$ 轻松验证。
为检验该级数的收敛性，我们对 $R_n(x)$ 应用 Lagrange 形式：对每个 $x \in \mathbb{R}$，存在 $z$ 使得

```math
R_n(x) = \frac{f^{(n+1)}(z)}{(n+1)!} x^{n+1}.
```

由于 $|f^{(n+1)}(z)|$ 等于 $|\cos z|$ 或 $|\sin z|$（取决于 $n$），故在任一情形下都有 $|f^{(n+1)}(z)| \leq 1$，从而 $|R_n(x)| \leq |x|^{n+1}/(n+1)!$。
因为对一切 $x \in \mathbb{R}$ 都有 $|x|^{n+1}/(n+1)! \to 0$（当 $n \to \infty$），所以对一切 $x \in \mathbb{R}$，余项 $|R_n(x)| \to 0$（当 $n \to \infty$）。
因此，这一级数表示对一切实数 $x$ 都得到了完全证明。

再注意到我们对 $|R_n(x)|$ 的估计，即 $|R_n(x)| \leq |x|^{n+1}/(n+1)!$，

> <span style='color:#1e8449;'>[note] Note（译者注）:</span> 两个余项公式是同一个 Taylor 定理（§7.12，Theorem 7.45）的两种「记账方式」。Lagrange 形式 $R_n(x)=\frac{f^{(n+1)}(z)}{(n+1)!}(x-c)^{n+1}$（$z$ 介于 $x$ 与 $c$ 之间）是 Rolle 定理连用 $n+1$ 次的产物；积分形式 $R_n(x)=\frac{1}{n!}\int_c^x(x-t)^n f^{(n+1)}(t)\,dt$ 是微积分基本定理的迭代——$n=0$ 时它就是 $f(x)-f(c)=\int_c^x f'(t)\,dt$ 本身。两者共享同一使用模板，命名**「导数受控则余项归零」**：只要 $|f^{(n+1)}|\le M$，Lagrange 形式给出 $|R_n|\le M|x-c|^{n+1}/(n+1)!$；积分形式把 $M$ 提出积分号、精确算出 $\int_c^x(x-t)^n\,dt=(x-c)^{n+1}/(n+1)$，得到完全相同的界——这正是 Theorem 10.28 证明的全部内容。收尾那句「阶乘压过幂」值得单独记住：固定 $x$，$|x-c|^{n+1}/(n+1)!$ 相邻项之比为 $|x-c|/(n+2)\to0$，比任何几何级数收敛得都快。Example 10.26 的 $\sin x$ 是模板的标准范例：导数界 $M=1$ 全球可用，余项对一切 $x$ 归零。这个界还顺手回答了下一页的数值问题：$|x|\le1$ 时 $|R_n(x)|\le1/(n+1)!$，$n=4$ 即 $1/120<0.01$——「五项达到 0.01 精度」的来历。两形式信息等价：有显式导数值用 Lagrange，要做积分放缩用积分形式。

---

<!-- ===== 书页 422（PDF 页 38）===== -->

Part009 · 书页 422 行内双语翻译

（承接上页）这一估计还给出了固定 $x$ 时级数收敛速度（rate of convergence）的某种认识。
例如，当 $|x| \leq 1$ 时，我们得到 $|R_n(x)| \leq 1/(n+1)!$。
因此，若要在 $(-1, 1)$ 上把 $\sin x$ 计算到误差不超过 $0.01$，只需取级数的前五项（$n = 4$）即可达到该精度。
倘若改用 $R_n(x)$ 的积分形式，我们也会得到类似的估计。
我们将这一计算留作 Exercise 10.5.1（习题 10.5.1）。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">10.5.2 Analytic Functions（解析函数）</span>

能够表示为 power series（幂级数）的函数类并不大。
正如我们已经指出的，无穷可微（infinitely differentiable）函数的类要大得多。
对这一非常特殊的函数类，通常使用的术语由下面的定义给出。

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">Definition 10.27（定义 10.27）</span>
> <span style="color:#7f8c8d;">TBB §10.5, p.422</span>

若一个函数 $f$ 的 Taylor 级数在 $c$ 的某个邻域内收敛到 $f$，则称 $f$ 在 $c$ 处解析（analytic at $c$）。

初等微积分（elementary calculus）中常见的函数通常都是解析的，只在某些显然非解析的点除外。
例如，$|x|$ 在 $x = 0$ 处不解析，$1/(1-x)$ 在 $x = 1$ 处不解析。
这两个函数在所论之点甚至连一阶导数都不存在。
类似地，像 $f(x) = |x|^3$ 这样的函数在 $x = 0$ 处不可能解析，因为尽管 $f'(0)$ 与 $f''(0)$ 存在，$f^{(3)}(0)$ 却不存在。
对这样的函数不可能写出完整的 Taylor 级数，因为其中某些导数不存在。
即使一个函数在某一点具有无穷多阶导数，它也未必在该点解析。
我们能写出完整的 Taylor 展开式，但正如我们已经注意到的，所得级数在任一区间上都不一定收敛到 $f$。
在这一点上，做一下 Exercise 10.5.4（习题 10.5.4）是有启发性的。
在 Example 10.26（例 10.26）中，我们证明了 $\sin x$ 的 Taylor 展开式。
证明的一部分用到了 $\sin x$ 及其一切导数都在实轴上有界这一事实。
这启示了一个一般性的结论。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 10.28（定理 10.28）</span>
> <span style="color:#7f8c8d;">TBB §10.5, p.422</span>

设 $f$ 在 $c$ 的一个邻域 $I$ 内无穷可微。
设 $x \in I$，并且存在 $M > 0$ 使得对一切 $m \in \mathbb{N}$ 与 $t \in [c, x]$（若 $x < c$ 则为 $[x, c]$）都有 $|f^{(m)}(t)| \leq M$。
那么 $\lim_{n \to \infty} R_n(x) = 0$。
于是 $f$ 在 $c$ 处解析。

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 我们证明 $x > c$ 的情形，而将 $x < c$ 的情形留作 Exercise 10.5.5（习题 10.5.5）。
> 我们使用余项的积分形式（Theorem 7.45，定理 7.45），得到

```math
|R_n(x)| = \left|\frac{1}{n!}\int_c^x (x-t)^n f^{(n+1)}(t)\, dt\right|.
\tag{7}
```

> <span style='color:#1e8449;'>[note] Note（译者注）:</span> Definition 10.27 的关键词是「收敛到 $f$」：解析要求 Taylor 级数在 $c$ 的某邻域收敛回原函数——光有无穷可微不够（$e^{-1/x^2}$），光有收敛也不够（必须回到 $f$ 本人）。于是函数世界出现严格包含链：可微 ⊃ 无穷可微 ⊃ 解析，每层都真包含：$|x|$ 在 0 处一阶导数不存在（连第一层都进不去）；$|x|^3$ 有前两阶导数但三阶不存在，Taylor 级数连写都写不全；$e^{-1/x^2}$ 无穷可微却不解析。Theorem 10.28 给出最常用的充分条件：各阶导数在 $c$ 与 $x$ 之间的闭线段上被同一常数 $M$ 界住，则 $R_n\to0$。证明策略命名**「M 提出、精确积分、阶乘收尾」**：把 $M$ 提出积分号，积分精确可算，剩 $M|x-c|^{n+1}/(n+1)!\to0$。第一性原理地问：为什么「有界导数」就够了？因为余项中 $f^{(n+1)}$ 只以乘积形式出现，一个界 $M$ 就把对函数的估计折算成对实数列的估计——与 CSAPP 浮点误差分析里「用上界替代逐项误差」同一思想。注意条件只须管住 $c$ 到 $x$ 这一小段，不要求全局有界——下页的 $e^x$ 正靠这一点起死回生。

---

<!-- ===== 书页 423（PDF 页 39）===== -->

> <span style="color:#2471a3;">**[proof]**</span> *Proof（证明，续接 Theorem 10.28 之证明）.*
> 利用我们对所有 $t \in [c, x]$ 均有 $|f^{(n+1)}(t)| \le M$ 的假设，由 (7) 式推知
>
> ```math
> |R_n(x)| \le \left|\frac{M}{n!}\int_c^x (x-t)^n\,dt\right|
> = \left|\frac{M}{n!}\cdot\frac{(x-t)^{n+1}}{n+1}\,\Big|_{t=c}^{x}\right|
> = \left|\frac{M}{(n+1)!}(x-c)^{n+1}\right|.
> ```
> 对于固定的 $x$ 与 $c$，$(x-c)$ 只是一个常数，因此
>
> ```math
> \frac{M(x-c)^{n+1}}{(n+1)!} \to 0.
> ```
> 于是 $|R_n(x)| \to 0$，从而 $f$ 在 $c$ 处解析（analytic at $c$）。

<span style="color:#2471a3;">**[example]**</span> **Example 10.29（例 10.29）**
> <span style="color:#7f8c8d;">TBB §10.5, p.423</span>

我们来证明函数 $f(x) = e^x$ 在 $x = 0$ 处解析（analytic）。它是无穷可微（infinitely differentiable）的，但我们还需要证明更多。$f$ 在 $x = 0$ 处解析这一事实可由前面的定理得出：例如我们选取区间 $[-1, 1]$。我们注意到，对所有 $x \in (-1, 1)$ 与 $n \in \mathbb{N}$ 都有 $|f^{(n)}(x)| = |e^x| \le e$。类似的观察也适用于 $f$ 在任意一点 $c \in \mathbb{R}$ 处的解析性（analyticity）。

习题 10.5.6 将提供另一个与 Theorem 10.28 类似的定理。

<!-- 本页下方 Exercises 10.5.1–10.5.6 为习题区，按约定跳过 -->

> <span style='color:#1e8449;'>[note] Note（译者注）:</span> Example 10.29 的全部技巧藏在一句话里：选取区间 $[-1,1]$，则对 $x\in(-1,1)$ 有 $|f^{(n)}(x)|=e^x\le e$。$e^x$ 在整条实轴上无界，若把 Theorem 10.28 误读成「在 $\mathbb{R}$ 上找统一 $M$」就会当场卡死；但定理只要求在 $c$ 到 $x$ 的闭线段上有界，而 $e^t$ 在任何闭区间上都达到最大值——连续函数最值定理，正是 6.042J 里闭区间紧致性的第一枚果实。模板命名**「局部化有界性」**：先固定目标点 $x$，在 $[0,x]$（或 $[x,0]$）上取 $M=e^{|x|}$，即可证明对该 $x$ 余项归零；$M$ 随 $x$ 变化完全合法，因为「解析」是逐点局部概念。选 $[-1,1]$ 还有传播价值：$M=e$ 顺手给出干净误差界 $|R_n(x)|\le e/(n+1)!$（$|x|\le1$）。注意这里的「局部」有两层：$M$ 可以对每个 $x$ 取不同的值，定理只要求逐点地证余项归零，并不追求一致收敛——这恰好呼应本节开头「解析是局部概念」的设定。把中心平移到任意 $c$（在 $[c-1,c+1]$ 上取 $M=e^{c+1}$），就得到 $e^x$ 在每个实点解析——复分析称这类处处解析的函数为 entire function（整函数），留作路标。

---

<!-- ===== 书页 424（PDF 页 40）===== -->

<!-- 页首 Exercises 10.5.7–10.5.8 为习题区，按约定跳过 -->

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">10.6 Products of Power Series（幂级数的乘积）</span>

假设我们有两个幂级数表示（power series representations）
```math
f(x) = \sum_{k=0}^{\infty} a_k (x - x_0)^k
```
与
```math
g(x) = \sum_{k=0}^{\infty} b_k (x - x_0)^k
```
它们分别在区间 $(-R_f, R_f)$ 与 $(-R_g, R_g)$ 内成立。我们应当如何得到乘积 $f(x)g(x)$ 的幂级数表示呢？我们可以仅仅计算这个函数的所有导数，从而构造它的 Taylor series（Taylor 级数）。但这是最容易或最方便的方法吗？我们如何知道这样的表示会成立呢？

解决这个问题最直接的途径，是运用我们在 Section 3.8 中关于级数乘积（products of series）的研究。我们知道这样的乘积在何时是成立的。事实上，由那一理论我们立即知道
```math
f(x)g(x) = \sum_{k=0}^{\infty} c_k (x - x_0)^k
```
将在区间 $(-R, R)$ 内成立，其中 $R = \min\{R_f, R_g\}$，而系数由下列公式给出
```math
c_k = \sum_{j=0}^{k} a_j b_{k-j}.
```

<span style="color:#2471a3;">**[example]**</span> **Example 10.30（例 10.30）**
> <span style="color:#7f8c8d;">TBB §10.6, p.424</span>

级数
```math
\frac{1}{1-x} = 1 + x + x^2 + x^3 + \cdots
```
与级数
```math
f(x) = \sum_{k=0}^{\infty} a_k x^k
```
的乘积给出表示
```math
\frac{f(x)}{1-x} = \sum_{k=0}^{\infty} (a_0 + a_1 + a_2 + \cdots + a_k) x^k.
```
这个表示在何处成立呢？

<span style="color:#2471a3;">**[example]**</span> **Example 10.31（例 10.31）**
> <span style="color:#7f8c8d;">TBB §10.6, p.424</span>

函数 $e^x \sin x$ 的一个表示可以通过作如下乘积最方便地得到
```math
\left(1 + x + \frac{1}{2!}x^2 + \frac{1}{3!}x^3 + \cdots\right)
\left(x - \frac{1}{3!}x^3 + \frac{1}{5!}x^5 - \cdots\right)
= x + x^2 + \frac{1}{3}x^3 + \cdots（此处 $\sin x$ 系数按正确值 $\frac1{3!},\frac1{5!}$ 处理——原书此处误印为 $\frac13,\frac15$；乘积结果 $\frac13x^3$ 即由 $x^2$ 项与 $\sin x$ 的 $x$ 项相乘给出，勘误详见书页 427 译者注。）
```
并且该级数按照当前应用所需继续展开下去。


---

<!-- ===== 书页 425（PDF 页 41）===== -->

Part009 · 书页 425 行内双语翻译

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">10.6 Products of Power Series（幂级数的乘积）</span>

### <span style="color:#2471a3;">**[subsection]**</span> <span style="color:#c0392b">10.6.1 Quotients of Power Series（幂级数的商）</span>

假设我们有两个函数的 power series（幂级数）表示 $f(x) = \sum_{k=0}^{\infty} a_k x^k$ 与 $g(x) = \sum_{k=0}^{\infty} b_k x^k$，二者至少在某个区间 $(-r, r)$ 内均有效。我们能否找到商函数（quotient function）$f(x)/g(x)$ 的表示呢？当然我们必须要求 $g(0) \ne 0$，这等价于要求 $g$ 的级数中首项系数（leading coefficient）即 $b_0$ 那一项不为零。

如果存在表示，比如说某个级数 $\sum_{k=0}^{\infty} c_k x^k$，那么显然我们要求

```math
\frac{\sum_{k=0}^{\infty} a_k x^k}{\sum_{k=0}^{\infty} b_k x^k} = \sum_{k=0}^{\infty} c_k x^k.
```

这仅仅意味着我们想要

```math
\left(\sum_{k=0}^{\infty} b_k x^k\right)\left(\sum_{k=0}^{\infty} c_k x^k\right) = \sum_{k=0}^{\infty} a_k x^k.
```

上述条件对我们来说并不陌生，因为我们此前已经研究过如何构造两个幂级数的乘积。要使它成立，系数 $\{c_k\}$（目前我们还不知道如何确定它们）应满足如下方程组：

```math
b_0 c_0 = a_0,\qquad b_0 c_1 + b_1 c_0 = a_1,\qquad b_0 c_2 + b_1 c_1 + b_2 c_0 = a_2,
```

并且，一般地，

```math
b_0 c_k + b_1 c_{k-1} + b_2 c_{k-2} + \cdots + b_k c_0 = a_k .
```

由于我们知道所有的 $a_k$ 与 $b_k$，我们能够轻而易举地逐一求解这些方程——从第一个开始，一次解一个——从而得到商级数（quotient series）的各项系数。这种确定 $c_k$ 的算法（它确实就是这样一种算法）正是 long division（长除法）。只要形式地（formally）将表达式（分母）$b_0 + b_1 x + b_2 x^2 + b_3 x^3 + \cdots$ 除入表达式（分子）$a_0 + a_1 x + a_2 x^2 + a_3 x^3 + \cdots$，你就会发现自己求解的正是我们算法中的这些方程。

但是我们究竟确定了什么呢？我们只是证明了：如果 $f(x)/g(x)$ 存在级数表示，那么这个方法就能把它确定出来。然而，我们事先并没有任何保证，足以确保这样的级数一定存在。我们给出下面的定理（不加证明），以便提供这些保证。作为另一种选择，在任何计算中我们都可以构造出商级数（包括全部项！），并确定它具有正的 radius of convergence（收敛半径）。这同样可以为该方法提供依据，尽管它未必是最实用的途径。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 10.32（定理 10.32）</span>
> <span style="color:#7f8c8d;">TBB §10.6, p.425</span>

假设两个函数存在幂级数表示 $f(x) = \sum_{k=0}^{\infty} a_k x^k$ 与 $g(x) = \sum_{k=0}^{\infty} b_k x^k$，二者至少在某个区间 $(-r, r)$ 内均有效，并且 $b_0 \ne 0$。

<span style="color:#7f8c8d">（定理 10.32 的结论部分见书页 426。）</span>


---

<!-- ===== 书页 426（PDF 页 42）===== -->

Part009 · 书页 426 行内双语翻译

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 10.32（续，定理 10.32）</span>
> <span style="color:#7f8c8d;">TBB §10.6, p.426</span>

假设两个函数存在幂级数表示 $f(x) = \sum_{k=0}^{\infty} a_k x^k$ 与 $g(x) = \sum_{k=0}^{\infty} b_k x^k$，二者至少在某个区间 $(-r, r)$ 内均有效，并且 $b_0 \ne 0$。则存在某个正的 $\delta$，使得函数 $f(x)/g(x)$ 在 $(-\delta, \delta)$ 内是 analytic（解析）的，并且在该处可以找到商级数。

证明 Theorem 10.32 的恰当背景是 complex analysis（复分析），在复分析中已经证明：若分母不为零，则复解析函数（complex analytic functions）的商仍是解析的。

<span style="color:#7f8c8d">（书页 426 的 Exercises 10.6.1–10.6.6 为习题区，按约定跳过，不收录。）</span>

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">10.7 Composition of Power Series（幂级数的复合）</span>

假设我们希望利用下面两个级数展开式

```math
e^x = 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \cdots
```

与

```math
\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots
```

来获得函数 $e^{\sin x}$ 的幂级数展开。

> <span style='color:#1e8449;'>[note] Note（译者注）:</span> 乘积的系数公式 $c_k=\sum_{j=0}^{k}a_jb_{k-j}$ 就是你在 6.042J 生成函数里见过的卷积：两个普通生成函数相乘，系数按对角线求和，幂级数只是生成函数换了个名字。商的构造是一次前代（forward substitution）：$b_0c_k+b_1c_{k-1}+\cdots+b_kc_0=a_k$ 是下三角方程组，$b_0\ne0$ 正是 Strang 线性代数里主元非零的条件，逐行回代就是书中的 long division（长除法）。但形式可解只保证系数存在，不保证级数收敛——Theorem 10.32 补上的正是存在性：$b_0\ne0$ 时存在 $\delta>0$ 使 $f/g$ 在 $(-\delta,\delta)$ 内解析。为什么有正半径？一句复分析视角：$g$ 的复延拓在 $z=0$ 连续且 $g(0)=b_0\ne0$，故 $1/g$ 在 0 附近有界，商级数的半径至少延伸到离 0 最近的障碍——$g$ 的复零点或 $f$ 收敛盘的边界（实轴上再次隐形，如 $1/(1+x^2)$ 的 $\pm i$）。模板：**「主元非零 ⇒ 邻域可除」**。

---

<!-- ===== 书页 427（PDF 页 43）===== -->

Part009 · 书页 427 行内双语翻译

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Section 10.7 Composition of Power Series（幂级数的复合）</span>

先不急于判断这样做是否有意义，我们直接把 $\sin x$ 的级数代入 $e^x$ 的级数中相应的位置。于是我们希望能证明

```math
e^{\sin x} = 1 + \left(x - \frac{1}{3}x^3 + \frac{1}{5}x^5 - \cdots\right) + \frac{1}{2}\left(x - \frac{1}{3}x^3 + \frac{1}{5}x^5 - \cdots\right)^2 + \frac{1}{6}\left(x - \frac{1}{3}x^3 + \frac{1}{5}x^5 - \cdots\right)^3 + \cdots
```

再按显然的方式展开并合并同类项，得到（至少作为开头几项）

```math
e^{\sin x} = 1 + x + \frac{1}{2}x^2 - \frac{1}{6}x^3 + \cdots（此结果沿用了原书未经修正的 $\sin x$ 展开 $x-\frac13x^3+\frac15x^5-\cdots$；按正确的 $x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots$ 计算，$x^3$ 项系数为 $-\frac16+\frac16=0$，故应有的展开为 $1+x+\frac12x^2-\frac18x^4-\frac1{15}x^5+\cdots$，详见本页译者注。）
```

这种方法是有效的吗？

为了证明这种方法有效，我们陈述（不加证明）一个定理，给出使这种验证可行的一些条件。注意，这些条件正是我们对函数的复合 $f(g(x))$ 所应预期的。$g(x)$ 的级数关于点 $x_0$ 展开，把它代入一个关于值 $g(x_0)$ 展开的级数中，从而得到 $f(g(x))$ 关于点 $x_0$ 展开的级数。若在复变函数（complex variables）课程中处理，这个证明并不困难；但若试图把它当作实变函数（real variable）定理来证明，则会显得很神秘。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 10.33（定理 10.33）</span>
> <span style="color:#7f8c8d;">TBB §10.7, p.427</span>

假设两个函数存在幂级数表示

```math
g(x) = C + \sum_{k=1}^{\infty} a_k (x - x_0)^k \qquad\text{与}\qquad f(x) = \sum_{k=0}^{\infty} b_k (x - C)^k
```

且两者均在其中心周围的某个非退化区间（nondegenerate interval）内成立。那么 $f(g(x))$ 存在幂级数展开

```math
f(g(x)) = \sum_{k=0}^{\infty} c_k (x - x_0)^k
```

且具有正的radius of convergence（收敛半径），其系数可以通过把 $g(x) - C$ 的级数代入 $f$ 的级数而得到，即形式上展开

```math
f(g(x)) = \sum_{k=0}^{\infty} b_k \left( \sum_{j=1}^{\infty} a_j (x - x_0)^j \right)^k
```

<!-- 习题区 Exercise 10.7.1–10.7.3：按约定跳过 -->

> <span style='color:#1e8449;'>[note] Note（译者注）:</span> Theorem 10.33 的假设要逐字读：$g$ 的级数以 $x_0$ 为中心，$f$ 的级数却以 $C=g(x_0)$ 为中心——$f$ 的展开点是 $g$ 的值，不是 $x$。为什么这样就能代入？因为幂级数在中心处连续（Theorem 10.11），$x\to x_0$ 时 $g(x)\to C$，于是存在 $x_0$ 的小邻域使 $g(x)$ 整体落入 $f$ 的收敛区间——「值域落入收敛盘」是复合合法性的第一性原理条件，命名模板**「值域入盘」**。第二个隐藏条件是计算可行性：第 $m$ 项系数只被 $k\le m$ 的方幂 $(\sum_{j\ge1}a_j(x-x_0)^j)^k$ 贡献（该方幂最低次是 $k$），所以每个系数只需有限步卷积——像 CLRS 里多项式乘法按次数逐层累加，永不触碰无穷项。严格证明书里推给复变课，实变量的信任票来自第 9 章机器：小邻域上 $g(x)-C$ 一致地小且展开绝对可和，重排合法。顺带勘误：示例中 $\sin x$ 的系数 $\frac13,\frac15$ 应为 $\frac1{3!},\frac1{5!}$（与 Example 10.26 自相矛盾），正确展开是 $e^{\sin x}=1+x+\frac12x^2-\frac18x^4-\frac1{15}x^5+\cdots$——$x^3$ 系数 $-\frac16+\frac16=0$ 恰好抵消，这本身就是「代入后合并同类项」机制的活标本。

---

<!-- ===== 书页 428（PDF 页 44）===== -->

Part009 · 书页 428 行内双语翻译

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Section 10.8 Trigonometric Series（三角级数）</span>

> 选学章节，可略过。（*Enrichment section. May be omitted.*）

在本节中，我们简要介绍另一种表示函数的方式，即把它表示为 trigonometric series（三角级数）或 Fourier series（Fourier 级数）。幂级数与 Fourier 级数之间有着深刻的联系，因此这一理论确实属于本章（参见 Exercise 10.8.1）。

这一主题的起源可以追溯到十八世纪中叶。数学物理中的某些问题似乎要求：任意一个具有固定周期（此处取为 $2\pi$）的函数 $f$ 都能表示成三角级数的形式

```math
f(t) = \frac{1}{2}a_0 + \sum_{j=1}^{\infty} (a_j \cos jt + b_j \sin jt), \tag{8}
```

Daniel Bernoulli、d'Alembert、Lagrange 和 Euler 等数学家曾争论这种事情是否应当可能。Bernoulli 坚持认为这总是可能的，而 Euler 与 d'Alembert 则反对这一说法。

Joseph Fourier（1768–1830）看到了这些表示法的用途，虽然他除了作一些具体的计算之外，并没有对他的主张作任何验证，但他宣称 (8) 中的表示对每个函数 $f$ 都可用，并给出了系数的公式

```math
a_j = \frac{1}{\pi}\int_{-\pi}^{\pi} f(t)\cos jt\,dt \qquad\text{与}\qquad b_j = \frac{1}{\pi}\int_{-\pi}^{\pi} f(t)\sin jt\,dt
```

虽然他的数学理由并不很充分，在当时也备受批评，但他的直觉是正确的；以这种方式计算系数、形如上述的级数如今被称为 Fourier series（Fourier 级数）。$a_j$ 与 $b_j$ 称为 $f$ 的 Fourier 系数（Fourier coefficients）。

#### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">10.8.1 Uniform Convergence of Trigonometric Series（三角级数的一致收敛）</span>

> 选学章节，可略过。（*Enrichment section. May be omitted.*）

作为对这一理论的初尝，我们证明一个有趣的定理，它印证了 Fourier 最初的一些直觉。我们将证明：若一个三角级数uniform convergence（一致收敛）于函数 $f$，那么 Fourier 给出的那些系数就必然是正确的那组系数。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 10.34（定理 10.34）</span>
> <span style="color:#7f8c8d;">TBB §10.8, p.428</span>

假设

```math
f(t) = \frac{1}{2}a_0 + \sum_{j=1}^{\infty} (a_j \cos jt + b_j \sin jt), \tag{9}
```

在区间 $[-\pi, \pi]$ 上一致收敛。那么可以推出：函数 $f$ 是连续的，且系数由 Fourier 的公式给出：

```math
a_j = \frac{1}{\pi}\int_{-\pi}^{\pi} f(t)\cos jt\,dt \qquad\text{与}\qquad b_j = \frac{1}{\pi}\int_{-\pi}^{\pi} f(t)\sin jt\,dt
```

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 固定 $j \geq 1$，选取 $n > j$，并写出
>
> ```math
> s_n(t) = \frac{1}{2}a_0 + \sum_{k=1}^{n} (a_k \cos kt + b_k \sin kt)
> ```


---

<!-- ===== 书页 429（PDF 页 45）===== -->

Part009 · 书页 429 行内双语翻译

> <span style="color:#7f8c8d">本页承接上一页，为 Section 10.8 Trigonometric Series（三角级数）的中部：先收束 Theorem 10.34 的证明，随后进入子节 10.8.2 Fourier Series（Fourier 级数）。</span>

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*（续）

> 也就是说，它们正是该级数的 partial sums（部分和）。
> 一个直接但繁琐的计算表明，对于 $j \ge 1$ 且 $n > j$，有
> ```math
> \int_{-\pi}^{\pi} s_n(t)\cos jt\,dt = \int_{-\pi}^{\pi} a_j(\cos jt)^2\,dt = a_j\pi. \tag{10}
> ```
> 请记住，这只不过是一个有限和。
> 其中的 orthogonality relations（正交性关系）（见 Exercise 10.8.3）有助于完成这一计算。
> 我们假设 $s_n \to f$ uniformly（一致），那么由于 $\cos jt$ 有界，可随之推出：在 $t \in [-\pi,\pi]$ 上 $s_n(t)\cos jt \to f(t)\cos jt$ 也一致收敛。
> 又因这里出现的函数全部连续，故有
> ```math
> \lim_{n\to\infty} \int_{-\pi}^{\pi} s_n(t)\cos jt\,dt = \int_{-\pi}^{\pi} f(t)\cos jt\,dt.
> ```
> 结合 (10) 即证明了 $a_j$（$j \ge 1$）的公式。
> 至于 $a_0$ 以及 $b_j$（$j \ge 1$）的公式，则可用完全相同的方法得到。$\blacksquare$

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">10.8.2 Fourier Series（Fourier 级数）</span>

> （扩充内容章节，可略过。）

受我们刚刚证明的定理的鼓舞，我们要迈出戏剧性的一步——正是当年 Fourier 迈出的那一步。
我们从函数 $f$ 出发（而不是从级数出发），利用这些系数公式构造一个 trigonometric series（三角级数）。
请注意这里的逻辑转折。
如果存在一个三角级数一致收敛到连续函数 $f$，那么它必然由 Theorem 10.34 的公式给出。
那么，何不以级数本身为起点呢——即使我们毫无把握它是否会一致收敛，即使我们不知道它是否会一致收敛到我们出发时所用的那个函数，甚至即使该级数根本就是发散的？

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">Definition 10.35（定义 10.35）</span>
> <span style="color:#7f8c8d;">TBB §10.8, p.429</span>

设 $f$ 为区间 $[-\pi,\pi]$ 上的连续函数<sup>3</sup>，并令

```math
a_j = \frac{1}{\pi}\int_{-\pi}^{\pi} f(t)\cos jt\,dt, \qquad b_j = \frac{1}{\pi}\int_{-\pi}^{\pi} f(t)\sin jt\,dt.
```

则称级数

```math
\frac12 a_0 + \sum_{j=1}^{\infty} (a_j \cos jt + b_j \sin jt) \tag{11}
```

为 $f$ 的 Fourier series（Fourier 级数）。

> <span style="color:#7f8c8d">**原书脚注 3：**</span>我们本可以只假设 $f$ 是 Riemann Riemann integrable（可积）的，但事实上我们的定理只涉及连续函数。若仅使用 Riemann 积分（而非更一般的 Lebesgue 积分（Lebesgue integral））来研究 Fourier 级数，其研究范围将受到相当大的限制。

这里有一个隐含的默契：该级数应当以某种方式与 $f$ 相关联，并且人们希望它能用作 $f$ 的一个「表示」（representation）。
但一般而言，一致收敛是不可能的。
事实上，连 pointwise convergence（逐点收敛）都是一种奢望。
为了强调这种关系并非相等，我们通常写作

```math
f(t) \sim \frac12 a_0 + \sum_{j=1}^{\infty} (a_j \cos jt + b_j \sin jt).
```


---

<!-- ===== 书页 430（PDF 页 46）===== -->

Part009 · 书页 430 行内双语翻译

> <span style="color:#7f8c8d">书页 430 顶部为习题区（Exercise 10.8.1–10.8.4，涉及幂级数与三角级数的联系、Fourier 系数的存在性、正交性关系及其平方积分等），按约定跳过。</span>

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">10.8.3 Convergence of Fourier Series（Fourier 级数的收敛）</span>

> （扩充内容章节，可略过。）

如果每个连续函数的 Fourier series（Fourier 级数）都uniformly（一致）到原函数，那么 Fourier 级数理论的发展将会简单得多（尽管也许不那么引人入胜）。

但事实不仅与此相反，一个连续函数的 Fourier 级数甚至可以在一个相当大的点集上发散。

这给我们留下了一个严峻的困难。

一个函数的 Fourier 级数理应表示该函数，但究竟如何表示呢？

如果它不收敛到该函数，它又怎能被用作该函数的一个表示呢？

我们的推理中存在一个错误。

我们知道，如果级数以适当的方式收敛到一个函数，那么可以通过对该级数逐项积分（term-by-term integration）与term-by-term differentiation（逐项求导）来对该函数求积分与求导数。

但即使级数在某些点上发散，它仍有可能以这些方式被处理。

一个表示并不一定非得是逐点或一致意义上的表示才算有用。

在下一个定理中，我们将证明：对适当函数而言，其 Fourier 级数的 Cesàro sums（Cesàro 和）即使在该级数本身发散时也一致收敛到该函数。

你应当复习一下 3.9.1 节中 Cesàro summability（Cesàro 可和性）这一专题。

年轻的匈牙利数学家 Leopold Fejér（1880–1959）于 1900 年得到了这一定理。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 10.36 (Fejér)（定理 10.36，Fejér 定理）</span>
> <span style="color:#7f8c8d;">TBB §10.8, p.430</span>

设 $f$ 为 $[-\pi,\pi]$ 上的连续函数，且满足 $f(-\pi) = f(\pi)$。

则 $f$ 的 Fourier 级数的 partial sums（部分和）的 Cesàro means（Cesàro 平均）所组成的序列在 $[-\pi,\pi]$ 上一致收敛到 $f$。

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 在整个证明中，我们可以认为 $f$ 定义在整个 $\mathbb{R}$ 上，并且是 $2\pi$-周期的。
>
> 我们记
>
> ```math
> s_n(x) = \frac12 a_0 + \sum_{k=1}^{n} (a_k \cos kx + b_k \sin kx).
> ```

> <span style='color:#1e8449;'>[note] Note（译者注）:</span> Theorem 10.34 的计算骨架是你已经会的线性代数：在 $[-\pi,\pi]$ 上定义内积 $\langle f,g\rangle=\int_{-\pi}^{\pi}f(t)g(t)\,dt$，函数族 $\{1,\cos t,\sin t,\cos2t,\cdots\}$ 两两正交（$\int\cos^2 jt\,dt=\pi$、$\int1\,dt=2\pi$），Fourier 系数 $a_j=\frac1\pi\langle f,\cos jt\rangle$ 就是 $f$ 在 $\cos jt$ 方向上的投影系数——与 18.065 最小二乘投影同一个公式，只是从矩阵空间换到函数空间；$\cos jt$ 又是 $d^2/dt^2$ 的特征函数，Fourier 级数即谱分解。常数项写作 $\frac12a_0$ 的动机是让 $a_0=\frac1\pi\int f$ 与其他 $a_j$ 共用一条公式（有的教材写 $\frac1{2\pi}\int f$，同一回事）。系数是频率探测器：内积越大，$f$ 里频率 $j$ 的成分越强。Fejér 的洞察回答「Cesàro 平均为什么比部分和好」：部分和 $s_n$ 的积分核（Dirichlet 核）变号，跳跃点处过冲不消退（Gibbs 现象）；而 $\sigma_n=(s_0+\cdots+s_n)/(n+1)$ 的 Fejér 核 $K_n=\frac{1}{2(n+1)}(\frac{\sin\frac12(n+1)t}{\sin\frac12t})^2$ 非负、积分为 1、质量随 $n$ 集中到 0，故 $\sigma_n(x)$ 是 $f$ 在 $x$ 附近的加权平均，像逐渐聚焦的移动平均滤波器（CSAPP 信号直觉），震荡被抹平——与 CLRS 摊还分析同源：前缀平均驯服波动，代价只是收敛变慢。🎥 Colding 在 V21 里点出的正是这里的命门：「uniform refers to that it's for all x. So it's uniform in x.」（翻译：一致指的是它对所有的 x 都成立，也就是在 x 上是一致的。）

---

<!-- ===== 书页 431（PDF 页 47）===== -->

Part009 · 书页 431 行内双语翻译（Section 10.8 Trigonometric Series）

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">10.8 Trigonometric Series（三角级数）</span>

<span style="color:#7f8c8d">图题（Figure 10.1）：Fejér kernel $K_n(t)$ 在 $[-\pi,\pi]$ 上、$n=1,2,3,4,5$ 时的图像。</span>

承接上页，$f$ 的 Fourier series（Fourier 级数）的 partial sum（部分和）序列记作 $s_n(x)$（这意味着系数 $a_j$、$b_j$ 由 Fourier 公式确定）。于是我们记

```math
\sigma_n(x)=\frac{s_0(x)+s_1(x)+s_2(x)+\cdots+s_n(x)}{n+1}
```

为这一列 average（平均值）的序列，即 Cesàro mean（Cesàro 平均）。

我们的任务是证明 $\sigma_n\to f$ 一致地收敛（uniform convergence）。回顾此前内容可见，每个 $\sigma_n(x)$ 都是若干项 $s_k(x)$ 的有限和，而每个 $s_k(x)$ 又是由系数 $a_j$、$b_j$ 组成的若干项的有限和。进而，这些项中的每一项都可以表示为一个涉及 $f$ 以及 $\sin$、$\cos$ 的积分。

于是，经过一番相当繁重但常规的计算，我们得到如下公式

```math
\sigma_n(x)=\frac{1}{\pi}\int_{-\pi}^{\pi}\frac{1}{2}\bigl(f(x+t)+f(x-t)\bigr)K_n(t)\,dt
```

或者与之等价的公式

```math
\sigma_n(x)=\frac{1}{\pi}\int_0^{\pi}\bigl(f(x+t)+f(x-t)\bigr)K_n(t)\,dt \tag{12}
```

这里的 $K_n$ 称为 Fejér kernel（Fejér 核），且对每个 $n$ 有

```math
K_n(t)=\frac{1}{2(n+1)}\left(\frac{\sin\frac12(n+1)t}{\sin\frac12 t}\right)^2.
```

就我们对这一主题所做的简短介绍而言，你只需接受上述计算即可。

阶数为 $n$ 的 Fejér kernel（Fejér 核）具有下列性质，每一条都可由其定义直接看出：

1. 每个 $K_n(t)$ 都是非负的 continuous function（连续函数）。
2. 对每个 $n$，
```math
\frac{1}{\pi}\int_{-\pi}^{\pi}K_n(t)\,dt=\frac{2}{\pi}\int_0^{\pi}K_n(t)\,dt=1.
```
3. 对每个 $n$ 以及 $0<|t|<\pi$，
```math
0\le K_n(t)\le\frac{\pi}{(n+1)t^2}.
```

图 10.1（Figure 10.1）展示了该函数在 $n=1,2,3,4,5$ 时的图像。

设 $\varepsilon>0$，并选取 $\delta>0$，使得对一切 $0\le t\le\delta$ 都有

```math
|f(x+t)+f(x-t)-2f(x)|<\varepsilon.
```


---

<!-- ===== 书页 432（PDF 页 48）===== -->

Part009 · 书页 432 行内双语翻译（Chapter 10 Power Series，§10.8 续）

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">10.8 Trigonometric Series（三角级数）（续：Fejér 定理的证明）</span>

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*（承接上页）

> 这用到了 $f$ 的 uniform continuity（一致连续性）。我们注意到，由性质 2 可得
>
> ```math
> \frac{2}{\pi}\int_0^{\pi}f(x)K_n(t)\,dt=f(x).
> ```
>
> 于是我们有
>
> ```math
> |\sigma_n(x)-f(x)|\le\frac{1}{\pi}\int_0^{\pi}|f(x+t)+f(x-t)-2f(x)|K_n(t)\,dt\le I_1+I_2,
> ```
>
> 其中 $I_1$ 是在 $[0,\delta]$ 上的积分，$I_2$ 是在 $[\delta,\pi]$ 上的积分。由于 $K_n$ 是非负的，在积分中我们无需把它保留在绝对值符号之内。
>
> $I_1$ 这一部分（对一切 $n$）会很小，因为对于 $t\in[0,\delta]$，绝对值内的表达式很小。$I_2$ 这一部分（对足够大的 $n$）会很小，因为性质 3 对远离 $0$ 的 $t$ 给出了 $K_n$ 取值大小的界。
>
> 细节如下：对于 $I_1$ 我们有
>
> ```math
> I_1\le\frac{\varepsilon}{\pi}\int_0^{\delta}K_n(t)\,dt\le\varepsilon.
> ```
>
> 对于 $I_2$，令
>
> ```math
> \kappa_n=\sup\{K_n(t):\delta\le t\le\pi\},
> ```
>
> 并注意性质 3 为我们提供了如下事实：当 $n\to\infty$ 时 $\kappa_n\to 0$。现在我们有
>
> ```math
> I_2\le\frac{\kappa_n\varepsilon}{\pi}\int_{\delta}^{\pi}\bigl(|f(x+t)|+|f(x-t)|+2|f(x)|\bigr)\,dt,
> ```
>
> 从而只要选取足够大的 $n$，便可使 $I_2$ 任意小。
>
> 由于 $\varepsilon$ 与 $x$ 都是任意的，由此可知 $\lim_{n\to\infty}\sigma_n(x)=f(x)$ 在 $x\in[-\pi,\pi]$ 上一致地成立，正如所要求的那样。

<!-- page_048 习题区（Exercise 10.8.5、10.8.6 及 SEE NOTE 256 提示）按约定跳过 -->


---

<!-- ===== 书页 433（PDF 页 49）===== -->

Part009 · 书页 433 行内双语翻译（本页顶部 (d)–(g) 性质列表与 Figure 10.2 属习题区，按约定跳过）

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">10.8.4 Weierstrass Approximation Theorem（Weierstrass 逼近定理）</span>

本节为**提高小节（Enrichment section）**，可以省略（may be omitted）。

借助 Fejér's theorem（Fejér 定理），我们可以证明著名的 Weierstrass approximation theorem（Weierstrass 逼近定理）。

请注意，Fejér 定理的一个推论是：连续的 $2\pi$-periodic function（$2\pi$ 周期函数）可以被三角多项式（trigonometric polynomials）一致逼近（uniformly approximated）。

此外，Weierstrass 定理断言：紧区间（compact interval）上的连续函数可以被普通多项式（ordinary polynomials）一致逼近。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 10.37 (Weierstrass)（定理 10.37，Weierstrass 定理）</span>
> <span style="color:#7f8c8d;">TBB §10.8, p.433</span>

设 $f$ 是区间 $[a, b]$ 上的 continuous function（连续函数），并设 $\varepsilon > 0$。则存在一个多项式

```math
g(x) = \alpha_n x^n + \alpha_{n-1} x^{n-1} + \cdots + \alpha_1 x + \alpha_0
```

使得对所有 $x \in [a, b]$ 都有

```math
|f(x) - g(x)| < \varepsilon.
```

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 在本证明中，更方便的做法是假设 $[a, b] = [0, 1]$；一般情形可以从这一情形推出。
>
> 设 $f$ 是 $[0, 1]$ 上的连续函数，设 $\varepsilon > 0$，并记 $F(t) = f(|\cos t|)$。
>
> 那么 $F$ 是一个连续的 $2\pi$ 周期函数，并且可以用三角多项式在 $\varepsilon$ 之内逼近。
>
> 这是因为，根据 Theorem 10.36（定理 10.36），当 $n$ 足够大时，Cesàro means（Cesàro 平均）$\sigma_n(F)$ 与 $F$ 一致接近（uniformly close）。


---

<!-- ===== 书页 434（PDF 页 50）===== -->

Part009 · 书页 434 行内双语翻译

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明，续）.*

> 由于 $F$ 是偶函数（even function），即 $F(t) = F(-t)$，
>
> 我们可以确定那个三角多项式可能具有的形式。
>
> 在 $F$ 的 Fourier series（Fourier 级数）中，所有涉及 $\sin kt$ 的系数 $b_k$ 必为零。
>
> 因此，当我们构造 partial sums（部分和）的平均时，得到的只是余弦项之和。
>
> 于是，我们可以找到 $c_0, c_1, c_2, \ldots, c_n$，使得对所有 $t$ 都有：
>
> $\left|F(t) - \sum_{j=0}^{n} c_j \cos jt\right| < \varepsilon.$
>
> 利用初等三角恒等式，每个 $\cos jt$ 都可以写成 $T_j(\cos t)$ 的形式，其中 $T_j$ 是某个 $j$ 阶（ordinary）多项式。
>
> 因此，令 $x = \cos t$，对任意 $x \in [0, 1]$，可得：
>
> $\left|f(x) - \sum_{j=0}^{n} c_j T_j(x)\right| < \varepsilon,$
>
> 这正是我们所需要的多项式逼近（polynomial approximation）。$\blacksquare$

证明中出现的多项式 $T_j$ 就是著名的 Chebychev polynomials（Chebychev 多项式，亦称切比雪夫多项式），

它们很容易生成（参见 Exercise 10.8.9（习题 10.8.9））。

它们以俄罗斯数学家 Pafnuty Lvovich Chebychev（切比雪夫，1821–1894）的名字命名。

本页其余部分（Exercises 10.8.8–10.8.15 及 SEE NOTE 提示）为习题区，按约定跳过。

> <span style='color:#1e8449;'>[note] Note（译者注）:</span> Theorem 10.37 的证明是一条漂亮的归约链，命名**「五步归约」**：把 $[a,b]$ 仿射换成 $[0,1]$；令 $F(t)=f(|\cos t|)$ 把区间函数拉成 $2\pi$ 周期偶函数（$|\cos t|$ 扫遍 $[0,1]$，逼近 $F$ 等于同时逼近 $f$ 在 $[0,1]$ 的全部值）；Fejér 定理给出三角多项式逼近；偶性杀掉全部正弦项，只剩 $\sum_{j=0}^{n}c_j\cos jt$；最后用 $\cos jt=T_j(\cos t)$ 把三角多项式翻译成普通多项式——$T_j$ 就是 Chebyshev 多项式，由余弦倍角公式递归生成：$T_0=1$、$T_1=x$、$T_{j+1}=2xT_j-T_{j-1}$。这条链的本质是归约：复杂目标（任意连续函数）被归约到已解决的 Fejér 定理，其余步骤只是换元与翻译——正如 CLRS 里把新问题归约到已知算法。Chebyshev 多项式在此扮演「圆与区间的词典」：圆上的三角多项式对应区间上的普通多项式。结论读作：多项式全体在 $C[a,b]$ 的 sup 范数下稠密（任何连续函数都能被多项式逼近到任意精度）。Rudin 用 Bernstein 多项式给出另一条构造路线，殊途同归。

---