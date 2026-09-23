# <span style="color:#c0392b;">Elementary Real Analysis（初等实分析）</span>

> <span style="color:#7f8c8d;">行内双语翻译 · Part007（书页 285–334）</span>
> <span style="color:#7f8c8d;">范围：第 7 章 Differentiation（微分）§7.3 后半–§7.12（反函数/幂法则/导数连续性/局部极值/中值定理/单调性/Dini 导数/Darboux 性质/凸性/洛必达法则/泰勒多项式）· §7.13 挑战题与 Notes 提示区（p.323–330）按约定跳过 · 第 8 章 The Integral（积分）§8.1–§8.2 开头</span>
> <span style="color:#7f8c8d;">源文件：TBB-AllChapters-Portrait_part007_p301-350.pdf（书页 = PDF 页 + 284）</span>
> <span style="color:#7f8c8d;">Second Edition (2008) · Brian S. Thomson, Judith B. Bruckner, Andrew M. Bruckner</span>
> <span style="color:#7f8c8d;">**格式：** 中文主体 + `English term（中文翻译）` 嵌入 · 深红标题 · 蓝色标签 · fenced math block · 无英文原句</span>
> <span style="color:#7f8c8d;">**习题区**（各节 Exercises、§7.13 Challenging Problems、Notes 提示区 p.325–330 等）按约定跳过不收录</span>
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这里对恒等式 g(f(x))=x 用链式法则，得到 g′(f(x))=1/f′(x)，背后藏着一条贯穿全书的第一性原理：导数是函数在某点「伸缩」的倍数，而反函数就是在「往回看」时把这个伸缩倒过来。用放大镜直觉记最顺：f 在 x 处把微小线段放大 f′(x) 倍，g 再把结果缩回原样，两步相乘必等于 1，这正是链式法则写出的乘积。跨课程连接：这与 Strang《线性代数》中 $A\cdot A^{-1}=I$ 完全同构——导数是「一维的雅可比」，反函数对应「矩阵求逆」。但要留一个卡点诊断：链式法则只保证「若反函数存在且可微」时公式成立，并不证明 ln z 这样的反函数真的存在；确认存在性与可微性的依据是本段所预告的定理 7.32。建议把这条记为命名模板「反函数法」：凡是对「逆过来」定义的函数（√x、arcsin、ln）求导，先写出 f(g(x))=x 这张「身份证」，再给两边戴链式法则。可做一个费曼式检验：若在某点 f′(x)=0，为什么上面的除法公式会破产？答案正是反函数在那点处退化为非光滑的映射。


---



<!-- ===== W1 ===== -->

<!-- ===== W1 · 书页 285–286 · §7.3.3 Inverse Functions / 例 7.12 / §7.3.4 The Power Rule ===== -->

<span style="color:#7f8c8d">书页 285 · §7.3 Computations of Derivatives</span>

<span style="color:#7f8c8d">*（本页开头为习题 7.3.16 及图 7.3.16（Figure 7.5，函数 $f$ 与 $g$ 在若干点处的取值表），按约定跳过。）*</span>

### <span style="color:#2471a3;">**[subsection]**</span> <span style="color:#c0392b">7.3.3 Inverse Functions（反函数）</span>

设函数 $f:I\to J$ 具有一个反函数（inverse function）。

这仅仅意味着存在一个逆转该映射的函数 $g$（称为 $f$ 的反函数）：若 $f(a)=b$，则 $g(b)=a$。

我们可以假设 $I$ 与 $J$ 均为区间。

于是 $f$ 将区间 $I$ 映满（onto）区间 $J$，而反函数 $g$ 再将 $J$ 映回 $I$。

并非所有函数都有反函数，但我们此刻正假设这里的这一函数确实具有反函数。

再假设 $f$ 在点 $x_0\in I$ 处可微（differentiable）。

那么基于几何上的考虑，我们会预期反函数 $g$ 在像点（image point）$z_0=f(x_0)\in J$ 处应当可微。

这是完全初等的。

函数 $f$ 与其反函数 $g$ 之间的联系由下式给出：对所有 $x\in J$ 有 $f(g(x))=x$，或者对所有 $x\in I$ 有 $g(f(x))=x$。

对第二个恒等式运用链式法则（chain rule），立刻得到
```math
g'(f(x))\,f'(x)=1,
```
从而得到关系式
```math
g'(f(x))=\frac{1}{f'(x)},
```
这一结果本也可由几何论证得出。

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 7.12（例 7.12）</span>
> <span style="color:#7f8c8d;">TBB §7.3, p.285</span>

假设指数函数（exponential function）$e^x$ 已被建立，且我们已证明它对所有 $x$ 值都可微，并有通常的公式 $\frac{d}{dx}e^x=e^x$。

那么，只要我们能确信存在反函数，就可求出该反函数导数的公式。

设 $L(x)$ 为 $f(x)=e^x$ 的反函数。

于是，既然我们已知 $f'(x)=f(x)$，就有
```math
L'(f(x))=\frac{1}{f'(x)}=\frac{1}{f(x)}.
```

<span style="color:#7f8c8d">*（例 7.12 于此跨页，其余部分续于书页 286。）*</span>

---

<!-- ===== 书页 286 ===== -->

<span style="color:#7f8c8d">书页 286</span>

<span style="color:#7f8c8d">*（接前页，例 7.12 继续。）*</span>

或者，用另一个字母（比方说 $z$）替换 $f(x)$，我们有
```math
L'(z)=\frac{1}{z}.
```
这必须对 $L$ 的定义域中的每一个值 $z$ 成立，也就是对 $f$ 的值域中的每一个值成立。

你应当在此认出函数 $\ln z$ 的导数。

即便如此，在我们能够恰当地宣称已经证明这一公式之前，我们仍然需要论证反函数的存在性。

$\blacksquare$

我们希望有比这里所介绍的方法更好的办法来处理反函数。

我们这里的观察使我们能够计算某个反函数的导数，但并不保证某个反函数一定存在。

至于能够让我们仅仅通过考察导数来判断某反函数是否存在并具有导数的定理，请参见定理 7.32。

<span style="color:#7f8c8d">*（本页此余部分为习题 7.3.17–7.3.20 区，按约定跳过。）*</span>

### <span style="color:#2471a3;">**[subsection]**</span> <span style="color:#c0392b">7.3.4 The Power Rule（幂法则）</span>

幂法则（power rule）就是公式 $\frac{d}{dx}x^p=px^{p-1}$，它是许多微积分问题的基础。

我们已在（习题 7.3.5 中）证明，对 $n=1,2,3,\ldots$ 以及每个 $x$ 值，都有 $\frac{d}{dx}x^n=nx^{n-1}$。

将其推广到负整数是相当容易的。

只需对 $n=1,2,3,\ldots$ 以及每个满足 $x\ne 0$ 的值解释
```math
\frac{d}{dx}x^{-n}=\frac{d}{dx}\frac{1}{x^n},
```

<span style="color:#7f8c8d">*（本句于此跨页，其余部分续于书页 287。）*</span>
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 幂法则 x^p 的推广本质是一条「扩展定义但保持算律」的工程链：先用商法则把指数扩到负整数，再用反函数法（例 7.13 对 $f(x)=x^2$ 用 g′(f(x))=1/f′(x)）拿下 p=1/2，最后对 p=m/n 组合链式法则与反函数法一次推广。值得点破的第一性原理：每次扩展不是「新发现一条规则」，而是「要求旧规则在新领域继续成立」——把 x^{m/n} 理解为 (x^{1/n})^m，导数公式由内导乘外导自然推出。这与 CSAPP 中「扩展语义必须兼容原语义」的思路一致，也与离散数学里递归定义要求「良基性与保持性」一脉相承。一个卡点诊断：例 7.13 之所以绕道平方函数的反函数，是因为直接对 x^{1/2} 用整数幂法则不够格——p 为有理数时 (p·x^{p−1}) 还只是「猜想」而未被验证，这正是教材反复强调「先证明再运用」的原因。至于无理 p（如 2^π），习题引导你用上确界/连续性走「e^{p ln x}」这条路，那根脚手架要等第 8 章指数函数才真正搭好。



<!-- ===== W2 ===== -->

<span style="color:#7f8c8d">书页 287 · §7.3.4 幂法则（The Power Rule）续</span>

<span style="color:#2471a3;">**[section]**</span>

## <span style="color:#c0392b;">§7.3 导数的计算（Computations of Derivatives）</span>

进而使用商法则（quotient rule），我们发现幂法则（power rule）公式对 $p = -1, -2, -3, \ldots$ 以及所有 $x \neq 0$ 的值再次成立。

该公式对 $p = 0$ 亦成立，因为我们把 $x^0$ 解释为常数 $1$（不过对于 $x = 0$ 我们宁愿不作任何断言）。那么，该公式是否真的对 $p$ 的每一个值都成立，而不仅仅是对整数值？

<span style="color:#2471a3;">**[example]**</span>

### <span style="color:#c0392b;">例 7.13</span>
> <span style="color:#7f8c8d;">TBB §7.3, p.287</span>

我们可以验证幂法则公式对 $p = 1/2$ 成立；也就是说，我们证明

```math
\frac{d}{dx}\sqrt{x} = \frac{d}{dx} x^{1/2} = \frac{1}{2}\, x^{1/2-1} = \frac{1}{2\sqrt{x}} .
```

首先我们必须坚持 $x > 0$，否则 $\sqrt{x}$ 以及我们公式中的那个分式都将没有定义。现在把 $\sqrt{x}$ 解释为平方函数 $f(x) = x^2$ 的反函数（inverse）。具体地，令 $x > 0$ 时 $f(x) = x^2$，令 $x > 0$ 时 $g(x) = \sqrt{x}$，并注意 $f(g(x)) = g(f(x)) = x$。因此

```math
\frac{d}{dx} f(g(x)) = \frac{d}{dx} x = 1 ,
```

又由于 $f'(x) = 2x$ 且 $f'(g(x))g'(x) = 1$，我们得到 $2\sqrt{x}\, g'(x) = 1$，最后得出

```math
g'(x) = \frac{1}{2\sqrt{x}} ,
```

若幂法则公式成立，此即所求的结论。$\blacksquare$

幂法则

```math
\frac{d}{dx} x^p = p\, x^{p-1}
```

对 $p$ 的一切有理值是否都成立？我们可以用本质上相同的方法处理 $p = m/n$（$m$、$n$ 为整数）的情形。我们把这陈述为一个定理，其证明留作习题。至于无理的 $p$，习题中也有相应讨论。

<span style="color:#2471a3;">**[theorem]**</span>

### <span style="color:#c0392b;">Theorem 7.14</span>
> <span style="color:#7f8c8d;">TBB §7.3, p.287</span>

令 $x > 0$，$m$、$n$ 为整数，设 $f(x) = x^{\frac{m}{n}}$。则

```math
f'(x) = \frac{m}{n}\, x^{\frac{m}{n} - 1} .
```

<span style="color:#2471a3;">**[example]**</span>

### <span style="color:#c0392b;">例 7.15</span>
> <span style="color:#7f8c8d;">TBB §7.3, p.287</span>

每个多项式都在 $\mathbb{R}$ 上可微，且其导数可借助逐项求导（term by term differentiation）来计算；也就是说，

```math
\frac{d}{dx}\left(a_0 + a_1 x + a_2 x^2 + \cdots + a_n x^n\right) = a_1 + 2a_2 x + \cdots + n a_n x^{n-1}.
```

这可由幂法则公式与和法则（rule for sums）推出。注意，一个多项式的导数仍是一个多项式。$\blacksquare$

<span style="color:#2471a3;">**[example]**</span>

### <span style="color:#c0392b;">例 7.16</span>
> <span style="color:#7f8c8d;">TBB §7.3, p.287</span>

有理函数（rational function）是指可以表示为两个多项式之商的函数 $R(x)$，

```math
R(x) = \frac{p(x)}{q(x)} .
```

<span style="color:#7f8c8d">*（例 7.16 续于下页 288。）*</span>

<span style="color:#7f8c8d">书页 288 · §7.3 续 · Example 7.16 · §7.4 开头（Continuity of the Derivative?）</span>

<span style="color:#7f8c8d">*（承接上页 287 之例 7.16。）*</span>

该函数在分母 $q(x)$ 不等于零的每一点处都有定义。除分母（denominator）为零的那些点之外，每个有理函数都处处可微。这可从前例（它演示了如何对多项式求导）以及商法则推出。因此

```math
\frac{d}{dx}\left(\frac{p(x)}{q(x)}\right) = \frac{p'(x)q(x) - p(x)q'(x)}{q^2(x)}.
```

注意该导数仍是具有相同定义域的有理函数，因为分子（numerator）与分母（denominator）同为多项式。$\blacksquare$

<span style="color:#7f8c8d">*（本页其余部分为 §7.3 节习题区，按约定跳过。）*</span>

<span style="color:#2471a3;">**[section]**</span>

## <span style="color:#c0392b;">§7.4 导数的连续性？（Continuity of the Derivative?）</span>

我们已经观察到（定理 7.6）：若函数 $f$ 在区间 $I$ 上可微，则 $f$ 在 $I$ 上也连续。此陈述不应与另一条（不正确的）陈述相混淆，那条陈述说导数 $f'$ 是连续的。

<span style="color:#2471a3;">**[example]**</span>

### <span style="color:#c0392b;">例 7.17</span>
> <span style="color:#7f8c8d;">TBB §7.4, p.288</span>

考虑在 $\mathbb{R}$ 上定义的函数 $f$：

```math
f(x) = \begin{cases}
x^{2} \sin x^{-1}, & \text{if } x \neq 0,\\
0, & \text{if } x = 0.
\end{cases}
```

由于对一切 $x \neq 0$ 都有 $|\sin x^{-1}| \le 1$，所以对所有 $x \in \mathbb{R}$ 有 $|f(x)| \le x^2$。我们现在可以（例如由例 7.5）推出 $f'(0) = 0$。对于 $x \neq 0$，我们可以像初等微积分那样计算出

```math
f'(x) = -\cos x^{-1} + 2x \sin x^{-1}.
```

这个函数 $f'$ 在每个点 $x_0 \neq 0$ 处都是连续的。在 $x_0 = 0$ 处它却不连续。要看出这一点，我们只需考虑一个适当的序列 $x_n \to 0$，看看会发生什么……

<span style="color:#7f8c8d">*（例 7.17 续于下页 289。）*</span>


<!-- ===== W3 ===== -->

<span style="color:#7f8c8d">书页 289 · §7.4 Continuity of the Derivative?</span>
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 例 7.17 的可微却导函数不连续，是分析里最著名的「反直觉标本」。第一性原理是夹逼：$|f(x)|\le x^2$ 把 x=0 处的差商 (f(x)−f(0))/(x−0) 逼进零，故 f′(0)=0；但 f′(x)=−cos(1/x)+2x·sin(1/x) 中那个 −cos(1/x) 在原点附近无限频率振荡，沿 x_n=1/(πn) 取值交错为 ±1，极限根本不存在。这里有个经典卡点可诊断：「可微⇒连续」说的是 f 连续，而这里的「导函数不连续」说的是 f′ 连续——两者针对的对象不同，切勿混淆。命名证明策略模板「振荡夹逼法」：用快速振荡项（cos(1/x)）制造不连续，用衰减因子（$x^2$）保证可微，一乘一减恰到好处。跨课程连接：$x^2$·(高速振荡) 与信号处理中「包络×载波」同构——包络衰减快则平滑、慢则毛糙。向前张望一步：教材预告尽管 f′ 可在稠密格点上振荡，它仍保有介值性质（即 Darboux 性质，第 7.9 节），这正解释了「每一点都不连续」其实不可能。


<span style="color:#7f8c8d">（接上页：继续示例 Example 7.17 关于 $x^2\sin(1/x)$ 的可微性验证。）</span>

<span style="color:#2471a3;">**[example]**</span> **示例 Example 7.17（续）**
> <span style="color:#7f8c8d;">TBB §7.4, p.288</span>

……这部分将趋近于 $f'(x_n)$。例如，试取序列

```math
x_n=\frac{1}{\pi n}.
```

由于

```math
\cos\frac{1}{x_n}=\cos(\pi n),
```

而这一串数值将交替地等于 $+1$ 与 $-1$，由此可见 $f'(x_n)$ 不可能收敛。于是 $f'$ 在点 $0$ 处不连续。$\blacksquare$

从函数 $f$ 我们可以看到这样一个实例：一个在整个 $\mathbb{R}$ 上处处可微（differentiable）的函数，其导数 $f'$ 仍可能在某个点处不连续。我们还可以改动该函数，构造一个可微函数 $g$，使它的导数 $g'$ 在无穷多个点处不连续，甚至在 Cantor 集的每一个点处都不连续（参见习题 Exercise 7.4.2）。

那么你或许会追问：关于导数 $f'$ 的性质，是否还能说出任何积极的结论。事实上，一个可微函数的导数有可能在某个稠密集（dense set）上不连续¹，第 9.7 节稍后将给出这样的例子。我们还会在第 7.9 节证明，尽管 $f'$ 可能不连续，它仍与连续函数共享一项重要性质：即介值性质（intermediate value property），也就是 Darboux 性质（Darboux property）。

<span style="color:#7f8c8d">¹ 导数不可能在每一个点处都不连续，参见推论 Corollary 9.40。</span>

<span style="color:#7f8c8d">*（本页其余部分为 §7.4 习题区（Exercises 7.4.1–7.4.2），按约定跳过。）*</span>

---

<span style="color:#7f8c8d">书页 290 · §7.5 Local Extrema（局部极值）</span>
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定理 7.18 是微分通优化的大门钥匙，其结论——局部极值处 f′(x0)=0——是必要条件而非充分条件。证明的骨架可提炼成可复用的命名模板「两侧斜率夹逼法」：因为 x0 是局部极大点，左邻域差商 (f(x)−f(x0))/(x−x0)≥0，右邻域差商≤0；若 f′(x0) 是导数，它须同时等于左、右极限，一侧≥0、一侧≤0，唯有撞成 0。这个论证第一次把「导数符号」与「极值」这两个看似无关的概念焊在一起。跨课程连接：CLRS 里最优化常说「局部最优必是候选最优」，Strang 的梯度下降以驻点（∇f=0）为目标；反方向，如习题 7.5.1 所示，$f(x)=x^3$ 在 0 处 f′(0)=0 却非极值，所以驻点只是「候选集」。第一性原理一句话：极值点正是斜率符号复合的支点。配合随后的端点分析，你得到寻找全局极值的完整三件套：驻点、不可微点、端点。


## §7.5 局部极值

<span style="color:#2471a3;">**[section]**</span> 局部极值（Local Extrema）

我们在第 5.7 节已经看到，定义在闭区间 $[a,b]$ 上的连续函数必在该区间上取得绝对最大值（absolute maximum value）与绝对最小值（absolute minimum value）。这些值即所谓极值（extreme values），或简称 extrema。最大值与最小值必在某个点处取得，但我们应当如何着手去寻找这样的点呢？一种途径是先找出所有未必自身就是极值、却属于局部极值点（local extreme point）的点。

对于定义于区间 $I$ 上的函数 $f$，若存在 $\delta>0$，使得 $[x_0-\delta,x_0+\delta]\subset I$，并且对该较小闭区间内的所有 $x$ 都有 $f(x)\le f(x_0)$，则称 $f$ 在 $I$ 内部的点 $x_0$ 处取得局部最大值（local maximum）。局部最小值（local minimum）的定义与之类似。

当函数在 $(a,b)$ 上可微时，初等微积分中习得的一种熟悉方法对定位这类极值往往颇为有用：即寻找临界点（critical point），也就是导数等于零的点。我们先来陈述为这一方法奠定基础的定理。

<span style="color:#2471a3;">**[theorem]**</span> **定理 Theorem 7.18**
> <span style="color:#7f8c8d;">TBB §7.5, p.290</span>

设 $f$ 定义于区间 $I$ 上。若 $f$ 在 $I$ 内部的一点 $x_0$ 处取得局部极值（local extremum），并且 $f$ 在 $x_0$ 处可微，则必有 $f'(x_0)=0$。

<span style="color:#2471a3;">**[proof]**</span> **证明**（Proof） 设 $f$ 在 $I$ 内部的点 $x_0$ 处取得局部最大值（局部最小值的情形证明类似）。于是存在 $\delta>0$，使得

```math
[x_0-\delta,x_0+\delta]\subset I,\qquad f(x)\le f(x_0)
```

对所有 $x\in[x_0-\delta,x_0+\delta]$ 都成立。因此

```math
\frac{f(x)-f(x_0)}{x-x_0}\le 0,\qquad x\in(x_0,x_0+\delta),\tag{8}
```

以及

```math
\frac{f(x)-f(x_0)}{x-x_0}\ge 0,\qquad x\in(x_0-\delta,x_0).\tag{9}
```

若 $f'(x_0)$ 存在，则

```math
f'(x_0)=\lim_{x\to x_0^-}\frac{f(x)-f(x_0)}{x-x_0}=\lim_{x\to x_0^+}\frac{f(x)-f(x_0)}{x-x_0}.\tag{10}
```

由 (8) 可知，(10) 中第一个左极限至多为零；由 (9) 可知，第二个右极限至少为零。再由 (10)，这两个极限相等，故它们都等于零。$\blacksquare$

由定理 Theorem 7.18 可得，在 $[a,b]$ 上连续的函数 $f$ 必在其中某一类（或某一组）点处取得其最大值，这类点的类型不外乎以下三种：

1. 满足 $f'(x_0)=0$ 的内点 $x_0\in(a,b)$；
2. $f$ 在其中不可微的内点 $x_0\in(a,b)$；
3. 端点 $a$ 或 $b$。

上述三种可能性各自的简单实例，留给你自行构造。

于是，初等微积分定位极值的通常流程，就是先找出 $f$ 导数为零的诸点，再比较 $f$ 在这些点处的取值……

<span style="color:#7f8c8d">（接下页：续 §7.5。）</span>


<!-- ===== W4 ===== -->

---
> Part007 · 第 7 章 · 书页 291–292 行内双语翻译
---

---
<!-- ===== 书页 291（PDF 页 7）===== -->
---

<span style="color:#7f8c8d">书页 291 · §7.5 Local Extrema（局部极值）</span>

<span style="color:#7f8c8d">*（本页开头承接书页 290 关于「如何寻找局部极值」的讨论，自句中段跨页续接。）*</span>

……以及不可微点（nondifferentiability，若有的话），以及端点（endpoint）$a$ 与 $b$。

在初等微积分（elementary calculus）的框架内，情况通常相对简单：函数是可微的，使得 $f'(x)=0$ 的点集是有限的（或包含某一区间），而且方程 $f'(x)=0$ 易于求解。

当然，也可能出现远为复杂的情形。

下面的习题提供了一些例子和定理，用以说明极值（extremum，复数 extrema）之集究竟可以多么复杂。

<span style="color:#7f8c8d">*Figure 7.6（图 7.6）：习题 7.5.3 中函数图像的一部分。*</span>

> <span style="color:#7f8c8d">*（本页其余部分为 §7.5 的 Exercises（习题）区 7.5.1–7.5.5，按约定全部跳过。）*</span>
>
> <span style="color:#7f8c8d">*其中题目要点：7.5.1 给出 $\mathbb{R}$ 上可微、$f'(0)=0$ 但 $0$ 非极值点的例；7.5.2 考察 $f(x)=x^4(2+\sin x^{-1})$ 在 $x\ne 0$、$f(0)=0$ 的逐点可微性、绝对极小值与 $f'$ 的符号振荡；7.5.3 基于 Cantor 集 $K$ 构造连续锯齿函数（对应图 7.6），要求写出方程并验证其极小值零与诸 $c_k$ 处的局部极大值；7.5.4 求 Dirichlet 函数在 $[0,1]$ 上的全部局部极值；7.5.5 证明 7.5.3 与 7.5.4 的函数有无穷多个严格极大值，且这些点集可数。*</span>

---
<!-- ===== 书页 292（PDF 页 8）===== -->
---
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 弦的斜率 (f(b)−f(a))/(b−a) 是一个平均数，这是理解整个 §7.6 的方便先导。你在 6.042J 里学会均值不外乎「总量÷份数」：弦斜率就是把函数在 a 到 b 间的总增量 f(b)−f(a) 平摊到长度 b−a 上。MVT 于是几乎变得显然：若平均值是 M，就必有某点瞬时变化率恰等于 M——这正是「若每天平均走 100 公里，则途中某时刻瞬时速度必为 100 公里/小时」的数学版（移动平均必被瞬时值穿过，是介值思想的胚胎）。跨课程连接：这个「平均值必被穿过」与 Cauchy 中值、积分第一中值定理一脉相承，也是 CLRS 二分法里「连续函数值被等分区间」直觉的严格化。做一个费曼注：把这句话换成人话——「一栋楼的总高度变化量，等于某一层处搬运队的瞬时速率乘以层高差」。你也可以暂停，先自己试着把 MVT 译回去；若还能顺带指出「为什么只要求 (a,b) 内可微、端点仅需连续」，说明你已吃透条件设定的意义。


<span style="color:#7f8c8d">书页 292 · Differentiation（微分）· Chapter 7（第 7 章）· §7.6 开头</span>

> <span style="color:#7f8c8d">*（本页开头为 §7.5 Exercises（习题）区 7.5.6–7.5.8，按约定跳过；其中涉及：7.5.6 证明 $f:\mathbb{R}\to\mathbb{R}$ 的严格极大值点之集可数（见 Note 181）；7.5.7 对在每个点取到局部极大值的 $f:\mathbb{R}\to\mathbb{R}$ 证其值域可数（见 Note 182）；7.5.8 论类的无处单调（nowhere monotonic）连续甚至可微函数，其极大值与极小值之集在 $\mathbb{R}$ 中稠密，此类构造见后文 13.14.2。*</span>

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">7.6 Mean Value Theorem（中值定理）</span>

函数的值与其导数的值之间存在着密切的联系。

在一个方向上，这一点是平凡的，因为导数本身正是由函数的值定义的。

另一个方向则要微妙得多。

关于导数的信息究竟如何为我们提供关于函数的信息呢？

提供这类信息的一把关键钥匙，就是中值定理（Mean Value Theorem，后文简称 MVT）。

设 $f$ 在区间 $[a,b]$ 上连续，并在开区间 $(a,b)$ 上可微。

考虑 $(a,b)$ 中的一点 $x$。

对 $y \in (a,b)$、$y \ne x$，差商（difference quotient）

```math
\frac{f(y)-f(x)}{y-x}
```

表示由点 $(x,f(x))$ 与 $(y,f(y))$ 确定的弦（chord）的斜率。

这个斜率或许是 $f'(x)$ 的良好近似，或许不是。

若 $y$ 充分靠近 $x$，近似会是良好的；否则就未必。

中值定理断言：在由 $x$ 与 $y$ 确定的区间内某处，必存在一个点，使得该点的导数恰好等于给定弦的斜率。

正是这样一点的存在，在函数的值（此情形下为 $\frac{f(y)-f(x)}{y-x}$）与导数的值（此情形下为介于 $x$ 与 $y$ 之间某点处的值）之间建立了联系。

### <span style="color:#2471a3;">**[subsection]**</span> <span style="color:#c0392b">7.6.1 Rolle's Theorem（Rolle 定理）</span>

我们从一个预备定理开始，它给出中值定理的一个特例。

它得名于 Michel Rolle（1652–1719），此人除这一成就外几乎无所称道。

事实上，Rolle 之名之所以被冠于这个定理，仅仅是因为他于 1691 年在一本书中发表过它；而定理所蕴含的方法本身，并非他所发现。

也许他真正最大的实际贡献，是发明了记号 $\sqrt[n]{x}$ 来表示 $x$ 的 $n$ 次方根。

<span style="color:#2471a3;">**[theorem]**</span> **<span style="color:#c0392b">Theorem 7.19（Rolle 定理）</span>** 设 $f$ 在 $[a,b]$ 上连续，且在 $(a,b)$ 上可微。
> <span style="color:#7f8c8d;">TBB §7.6, p.292</span>

若 $f(a)=f(b)$，则存在 $c \in (a,b)$ 使得 $f'(c)=0$。

<span style="color:#7f8c8d">*（本定理的证明续于书页 293。）*</span>
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Rolle 定理的出名带点历史反讽，值得作为史料准确改写。Michel Rolle（1652–1719）在 1690 年的《代数论》（Traité d'algèbre）里首次用极限论证处理代数方程实根之间的定位，这可视为先于微积分体系的极限思想雏形，「Rolle 定理」正是那次工作的投影；但他本人随后却激烈抨击当时的无穷小方法，可说给这个定理冠名的人自己并不完全信任驾驭它的工具。教材说「除这一成就外几乎无所称道」，此外还应正名：他真正留给后世的是 n 次方根的记号 √[n]x。证明策略是一个可复用命名模板「极值定位法」：先由闭区间连续必取最大值（定理 5.50）保证某点 c 处 f(c)=M，再由 f(a)=f(b) 推 c 落于开区间内，最后套定理 7.18 得 f′(c)=0。跨课程连接：这条脉络与 6.042J 中的存在性证明同构——先保证存在（最值定理），再导出所需性质。动手题：对 g(x)=x·sin(1/x)（g(0)=0）在 [0,1/π] 上用 Rolle，体会「端点不需可微、只要求连续」到底放宽了什么。



<!-- ===== W5 ===== -->

<span style="color:#7f8c8d">书页 293 · §7.6 Mean Value Theorem（中值定理）</span>

<span style="color:#7f8c8d">（本页承接书页 292，续定理 7.19 Rolle 定理的证明。）</span>

<span style="color:#2471a3">**[figure]**</span> **图 7.7**：Rolle 定理（注意此处 $f(a)=f(b)$）。

<span style="color:#2471a3;">**[proof]**</span> **证明**（续定理 7.19）。

若函数 $f$ 在 $[a,b]$ 上恒为常数，则对所有 $x \in (a,b)$ 都有 $f'(x)=0$，此时可把 $c$ 取为 $(a,b)$ 中的任意一点。

现设 $f$ 并非常数函数。由于 $f$ 在紧区间 $[a,b]$ 上连续，由定理 5.50，$f$ 在 $[a,b]$ 上取得最大值 $M$ 与最小值 $m$。又因为 $f$ 并非恒定，$M$ 与 $m$ 中必有一个不同于 $f(a)$ 与 $f(b)$，不妨设 $M>f(a)$。选取 $c \in (a,b)$ 使得 $f(c)=M$。由于 $M>f(a)=f(b)$，故 $c \ne a$ 且 $c \ne b$，于是 $c \in (a,b)$。由定理 7.18，得 $f'(c)=0$。$\blacksquare$

可以观察到，Rolle 定理断言：在我们这些假设之下，总存在一点，使得函数图像在该点的切线是水平的，因而这条切线与由点 $(a,f(a))$ 和 $(b,f(b))$ 所确定的弦具有相同的斜率（见图 7.7）。

当然，这样的点可能有许多个；Rolle 定理只是保证至少存在一个这样的点。还可以观察到这里并未要求 $f$ 在端点 $a$ 与 $b$ 处可微。该定理适用于诸如 $f(x)=x\sin x^{-1}$（$f(0)=0$）在区间 $[0,1/\pi]$ 上这类函数；此函数在零处并不可微，但在 $0$ 与 $1/\pi$ 之间确实存在无穷多个导数为零的点。

---

<span style="color:#7f8c8d">*（本页下半部为 §7.6 的习题区，即习题 7.6.1–7.6.5，按约定跳过。）*</span>

---

<span style="color:#7f8c8d">书页 294 · §7.6 Mean Value Theorem（续）</span>

<span style="color:#7f8c8d">（本页承接书页 293，先续习题区尾部，再进入 §7.6.2。）</span>

<span style="color:#2471a3">**[figure]**</span> **图 7.8**：中值定理（$f'(c)$ 为弦的斜率）。

<span style="color:#7f8c8d">*（本页顶部为 §7.6 习题区尾部，即习题 7.6.6–7.6.7，按约定跳过。）*</span>

<span style="color:#2471a3;">**[subsection]**</span> ## 7.6.2 中值定理（Mean Value Theorem）

若我们去掉 Rolle 定理中 $f(a)=f(b)$ 这一要求，便能得到如下结果：存在 $c \in (a,b)$ 使得

```math
f'(c)=\frac{f(b)-f(a)}{b-a}.
```

从几何上看，这表明：存在一点 $c \in (a,b)$，使得函数图像在点 $(c,f(c))$ 处的切线平行于由点 $(a,f(a))$ 和 $(b,f(b))$ 所确定的弦（见图 7.8）。

这正是中值定理，亦称均值定理（law of the mean）或第一中值定理（first mean value theorem），因为还存在其他的中值定理。

<span style="color:#c0392b">**[theorem]**</span> **定理 7.20（中值定理，Mean Value Theorem）** 设 $f$ 为闭区间 $[a,b]$ 上的连续函数，且在开区间 $(a,b)$ 上可微。则存在 $c \in (a,b)$ 使得
> <span style="color:#7f8c8d;">TBB §7.6, p.294</span>

```math
f'(c)=\frac{f(b)-f(a)}{b-a}.
```

<span style="color:#2471a3;">**[proof]**</span> **证明**：我们这样证明本定理——从 $f$ 中减去一个其图像恰为所论弦所确定的直线的函数，然后应用 Rolle 定理。设

```math
L(x)=f(a)+\frac{f(b)-f(a)}{b-a}\,(x-a).
```

<span style="color:#7f8c8d">（证明续至书页 295。）</span>
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> MVT 证明最该学的是「化归」这个动作：从 f 减掉弦所在的直线 L(x)，端点值立即被拉平到 0，于是把问题交给已证的 Rolle 定理。这是可反复套用的命名模板「去势/化归法」（算法语境即 CLRS 的 reduce to a known problem）。第一性原理：导数是平移不变的——对 g(x)=f(x)−L(x) 求导，L′(x)=(f(b)−f(a))/(b−a) 是常数，故 g′(c)=0 直接等价于 f′(c)=弦斜率；减掉一条直线只是把参照系「整体转到与弦平行」，几何上不损失任何信息。这正是后世数学「先化到最简情形、证明一次后让一般情形免费继承」的降维艺术雏形。跨课程连接：与 Strang「先解齐次再特解」同构，也与 CSAPP 把新问题归约到精简指令集的抽象一致。一个小提醒：Rolle 只要求端点连续、内部可微，被化归后的 g 同样满足，这正是整个证法能平移的前提。



<!-- ===== W6 ===== -->

<span style="color:#7f8c8d">书页 295 · §7.6 中值定理（续）</span>

<span style="color:#2471a3;">**[proof · 续]**</span> 紧接上一页 Theorem 7.20（中值定理 Mean Value Theorem，MVT）的证明。

我们看到 $L(a) = f(a)$ 且 $L(b) = f(b)$。现在令
```math
g(x) = f(x) - L(x). \tag{11}
```

于是 $g$ 在 $[a,b]$ 上连续、在 $(a,b)$ 上可微，并满足条件 $g(a) = g(b) = 0$。由 Rolle 定理，存在 $c \in (a,b)$ 使得 $g'(c) = 0$。对 (11) 求导，我们看到 $f'(c) = L'(c)$。但
```math
L'(c) = \frac{f(b) - f(a)}{b - a},
```
因此
```math
f'(c) = \frac{f(b) - f(a)}{b - a},
```

正如所要证明的。$\blacksquare$

Rolle 定理与中值定理都易于证明，它们的证明依赖于这些定理的几何内涵。我们建议你花时间去理解这些定理的几何解释。

<span style="color:#7f8c8d">*（本页其余 7.6.8–7.6.11 为本节习题区，按约定跳过。）*</span>

---

<span style="color:#7f8c8d">书页 296 · §7.6 中值定理（习题区）</span>

<span style="color:#7f8c8d">*（本页 7.6.12–7.6.18 为本节习题区，按约定跳过。）*</span>


<!-- ===== W7 ===== -->

<span style="color:#7f8c8d">书页 297 · §7.6 Mean Value Theorem（中值定理）</span>
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Cauchy MVT 是 MVT 的参数化升级：把曲线写成 (x,y)=(g(t),f(t))，弦的斜率变成 (f(b)−f(a))/(g(b)−g(a))。🎥 讲者 Tobias Colding 在课上用一句话点破它——他说中值定理有两种版本，一种是普通 MVT，另一种「更高配的版本」是同时摆弄两个函数，那就是 Cauchy 中值定理（原文：the other is like a fancy version of it, where you have two functions in play at the same time. And that's called the Cauchy mean value theorem.）。核心第一性原理是「两变量共用同一个参数 t」：导数不再只告诉你「陡不陡」，而告诉你曲线沿 (g′,f′) 的方向如何铺展。式 (12) 特意写成跨乘形式而非直接相除，是为了规避 g(a)=g(b) 或 g′(c)=0 时除零的退化，这是「用乘法代替除法以免踩空」的工程智慧，也直接为 §7.11 的 L'Hôpital 法则铺路。跨课程连接：把 t 当作时间，(x,y) 是质点轨迹，Cauchy MVT 说的正是「平均速度向量必在某时刻被瞬时速度向量平行穿过」。一个自检路标：把 g 替换成恒等函数 t，你会自动回到普通 MVT。


### <span style="color:#2471a3;">**[subsection]**</span> <span style="color:#c0392b">7.6.3 Cauchy's Mean Value Theorem（Cauchy 中值定理）</span>

<span style="color:#7f8c8d">*（本节为扩展内容 Enrichment section，可略过。）*</span>

我们可以把中值定理推广到以参数形式（parametrically）给出的曲线上。

设 $f$ 与 $g$ 在 $[a,b]$ 上连续，并在 $(a,b)$ 上可微（differentiable）。

考虑由下式以参数形式给出的曲线

```math
x=g(t),\qquad y=f(t)\qquad (t\in [a,b]).
```

当 $t$ 在区间 $[a,b]$ 上变化时，点 $(x,y)$ 描出一条曲线 $C$，它连接分别由参数 $a$ 与 $b$ 决定的两点 $(g(a),f(a))$ 与 $(g(b),f(b))$。

若 $g(a)\neq g(b)$，则由这些点确定的弦（chord）的斜率为

```math
\frac{f(b)-f(a)}{g(b)-g(a)}.
```

Cauchy 形式的中值定理断言：在 $C$ 上存在一点 $(x,y)$，使得该点处的切线（tangent）与所论弦平行。

我们陈述并证明这一定理。

#### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 7.21（Cauchy 中值定理，Cauchy Mean Value Theorem）</span>
> <span style="color:#7f8c8d;">TBB §7.6, p.297</span>

> 设 $f$ 与 $g$ 在 $[a,b]$ 上连续，并在 $(a,b)$ 上可微，则存在 $c\in(a,b)$，使得
>
> ```math
> [f(b)-f(a)]\,g'(c)=[g(b)-g(a)]\,f'(c). \qquad (12)
> ```

#### <span style="color:#2471a3;">**[proof]**</span> <span style="color:#c0392b">证明（Proof）</span>

设

```math
\varphi(x)=[f(b)-f(a)]\,g(x)-[g(b)-g(a)]\,f(x).
```

则 $\varphi$ 在 $[a,b]$ 上连续，并在 $(a,b)$ 上可微。

进一步有

```math
\varphi(a)=f(b)g(a)-f(a)g(b)=\varphi(b).
```

由 Rolle 定理（Rolle's theorem），存在 $c\in(a,b)$，使得 $\varphi'(c)=0$。

显然，这一 $c$ 满足 (12)。$\blacksquare$

<span style="color:#7f8c8d">*（本页其余部分为 §7.6 的习题区（练习 7.6.19–7.6.21），按约定跳过。）*</span>

---

<span style="color:#7f8c8d">书页 298 · §7.7 Monotonicity（单调性）</span>

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">7.7 Monotonicity（单调性）</span>

在初等微积分中我们学到：若 $f'\ge 0$ 在区间 $I$ 上成立，则 $f$ 在 $I$ 上是不减（nondecreasing）的。

我们出于多种目的使用这一结论及相关结果：描绘函数图形、定位极值（extrema）等等。

在本节中，我们将更为仔细地考察其中所涉及的内容。

我们先回顾若干定义。

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">Definition 7.22（定义 7.22）</span>
> <span style="color:#7f8c8d;">TBB §7.7, p.298</span>

> 设 $f$ 在区间 $I$ 上取实数值（real valued）。
>
> 1. 若当 $x_1,x_2$ 为 $I$ 中的点且 $x_1<x_2$ 时总有 $f(x_1)\le f(x_2)$，则称 $f$ 在 $I$ 上**不减**。
> 2. 若严格不等式 $f(x_1)<f(x_2)$ 成立，则称 $f$ **递增**（increasing）。

对不增（nonincreasing）函数与递减（decreasing）函数，已给出了类似的定义。

#### <span style="color:#2471a3;">**[note]**</span> <span style="color:#1e8449">注（Note）</span>

某些作者倾向于把「递增」与「严格递增」这两个术语，用于我们所说的不减与递增。

这带来一个不幸的结果：此时常值函数（constant function）会被认为既是递增的又是递减的。

而按照我们的定义，我们必须说它们既是不减的又是不增的，这听起来更为合理——若某物保持不变，那么它既没有上升也没有下降。

我们这种用法的缺点是：在最初使用这些术语时你可能会感到不适，但这种不适会随着练习而消失。

用「严格递增」来代替「递增」也总是稳妥的，尽管根据定义这样做是多余的。

所谓单调（monotonic）函数，我们指的是递增、递减、不减或不增的函数。

在初等微积分中遇到的涉及函数单调性（monotonicity）的定理，通常都是对可微函数来陈述的。

但单调函数未必可微，甚至未必连续。

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">例 7.23（Example 7.23）</span>
> <span style="color:#7f8c8d;">TBB §7.7, p.298</span>

例如，若

```math
f(x)=\begin{cases} x, & x<0\\ x+1, & x\ge 0,\end{cases}
```

则 $f$ 在 $\mathbb{R}$ 上递增，但在 $x=0$ 处并不连续。

（关于单调函数不连续点的更多讨论，参见 5.9.2 节。）$\blacksquare$

现在让我们来探讨导数在单调性研究中的作用。

我们证明一条熟悉的定理，它是许多微积分应用的基础。

注意，这一定理的证明是中值定理的一个简单推论。

#### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 7.24（定理 7.24）</span>
> <span style="color:#7f8c8d;">TBB §7.7, p.298</span>

> 设 $f$ 在区间 $I$ 上可微，则
>
> (i) 若对所有 $x\in I$ 有 $f'(x)\ge 0$，则 $f$ 在 $I$ 上不减；
>
> (ii) 若对所有 $x\in I$ 有 $f'(x)>0$，则 $f$ 在 $I$ 上递增；
>
> (iii) 若对所有 $x\in I$ 有 $f'(x)\le 0$，则 $f$ 在 $I$ 上不增。

<span style="color:#7f8c8d">*（定理 7.24 的其余部分与证明续于书页 299。）*</span>
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定理 7.24 是 MVT 最趁手的日常工具，它把「导数符号」翻译成「函数单调性」。证明只用一步：任取 x1<x2，由 MVT 得 f(x2)−f(x1)=f′(c)(x2−x1)。若导数恒≥0，右端与 x2−x1 同号，故 f 不减；这种「把每点符号变成两点差」的手法建议命名为模板「符号推断法」。第一性原理：不看全区间总和，而看增量 f(x2)−f(x1) 的正负——这正是积分的雏形，把长段切成无数小段，每段由导数符号定走向。顺带留意术语：西方不少教材把我们的「递增」叫 strictly increasing，把「不减」叫 increasing，于是常数函数既增又减，听着矛盾；本书特意区分「增/不减」「减/不增」，让「不变」的单位处得更自然。跨课程连接：单调性是二分搜索（CLRS）可行的前提，也是单调栈/单调队列这类结构的本质；而「f′=0 ⟹ 常值」正是「零速度 ⟹ 原地不动」的严格版。费曼检验：若只假设 f′≥0 几乎处处成立，结论会退化，这留给第 7.8 节 Dini 导数那条更柔软的路去补齐。



<!-- ===== W8 ===== -->

<span style="color:#7f8c8d">书页 299 · §7.7 单调性</span>

<span style="color:#7f8c8d">（本页承接书页 298，续 Theorem 7.24 的陈述与证明；定理第一部分的 (i)–(iii) 已在上一页给出。）</span>

**(iv)** 若对所有 $x \in I$ 都有 $f'(x)<0$，则 $f$ 在 $I$ 上递减（decreasing）。

**(v)** 若对所有 $x \in I$ 都有 $f'(x)=0$，则 $f$ 在 $I$ 上为常值函数（constant）。

<span style="color:#2471a3;">**[proof]**</span> **证明（Proof）.** 为证 (i)，设 $x_1,x_2\in I$ 且 $x_1<x_2$。由中值定理 (7.20)，存在 $c\in(x_1,x_2)$，使得

```math
f(x_2)-f(x_1)=f'(c)(x_2-x_1).
```

若 $f'(c)\ge 0$，则 $f(x_2)\ge f(x_1)$。因此，若对所有 $x\in I$ 都有 $f'(x)\ge 0$，则 $f$ 在 $I$ 上不减（nondecreasing）。

部分 (ii)、(iii) 与 (iv) 的论证类似，而 (v) 直接由部分 (i) 与 (iii) 推出。$\blacksquare$

<span style="color:#7f8c8d">*（本页其余部分为 §7.7 的习题区，即习题 7.7.1–7.7.4，按约定跳过。）*</span>

---

<span style="color:#7f8c8d">书页 300 · 第 7 章 微分（Differentiation）</span>

<span style="color:#7f8c8d">（本页承接书页 299，先给出图 7.9，其后为本节习题区尾部，再进入 §7.8。）*</span>

<span style="color:#2471a3;">**[figure]**</span> <span style="color:#2471a3">**图 7.9**</span>：函数 $f(x)=|x\cos x^{-1}|$ 的图形（Graph）。

<span style="color:#7f8c8d">*（本页顶部为 §7.7 习题区尾部，即习题 7.7.5–7.7.6，按约定跳过。）*</span>

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">7.8 Dini Derivates（Dini 导数）</span>

<span style="color:#2471a3;">**[note]**</span> <span style="color:#1e8449;">高级进阶章节（Advanced section），可略读（May be omitted）。</span>

我们在例 7.4 中观察到，函数 $f(x)=|x|$ 在点 $x=0$ 处并没有导数，但它确实拥有单侧导数（one-sided derivative）$f'_+(0)=1$ 与 $f'_-(0)=-1$。

要构造出在一点处甚至连单侧导数都不存在的连续函数，并不困难。

<span style="color:#2471a3;">**[example]**</span> **例 7.25（Example 7.25）**
> <span style="color:#7f8c8d;">TBB §7.8, p.300</span>

考察函数

```math
f(x)=
\begin{cases}
|x|\,\bigl|\cos x^{-1}\bigr|, & \text{若 } x\neq 0,\\[2pt]
0, & \text{若 } x=0.
\end{cases}
```

（见图 7.9；原书此处误引作 Figure 7.25，按本页图 7.9 修正。）

由于对所有 $x\neq 0$ 都有 $|\cos x^{-1}|\le 1$，

```math
\lim_{x\to 0}f(x)=0=f(0),
```

所以 $f$ 在 $x=0$ 处连续。

显然 $f$ 在 $\mathbb{R}$ 中的其余所有点处也都是连续的，因此 $f$ 是连续函数。

$f$ 的振荡行为使得集合

```math
\bigl\{x:\ |\cos x^{-1}|=1\bigr\} \quad \text{与} \quad \bigl\{x:\ |\cos x^{-1}|=0\bigr\}
```

<span style="color:#7f8c8d">（本句跨页，其余内容续于书页 301。）*</span>
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Dini 导数的设计思路是「当极限不够用时，退而求其次用上下确界兜底」，这正是你手里「上确界」脚手架的一次漂亮复用。当单侧导数的极限 (f(x)−f(x0))/(x−x0) 不存在时，limsup/liminf 仍各自给出确定值（可能为无穷），于是四个 Dini 导数 $(D^+,D_+,D^-,D_-)$ 对每个可定义区间上的函数、在每个点都忠实记录「斜率族」的上、下包络。第一性原理：f 有普通导数的充要条件是四者相等（习题 7.8.2）——此时「替换物」回落到「本金」；如例 7.25 的 |x||cos(1/x)| 在 0 处给出 $D^+=1$、$D_+=0$，说明右斜率在 0 与 1 之间无限震荡，故右导数不存在。跨课程连接：这种「极限退化就用上下极限保持信息」的做法，与离散数学在 6.042J 里对有序集取上界的思想同源，也和 CSAPP 中「数值溢出退化为饱和钳位」的容错策略形似——都是「保留最坏/最好情形」的稳健退档。定理 7.30 说明即使只有 $D^+f>0$ 函数仍递增，本质是把单调性定理「去导数化」，使处处不可微的连续函数（如 Besicovitch 的构造）仍有章可循。



<!-- ===== W9 ===== -->

## §7.8 Dini 导数（Dini Derivates）

<span style="color:#7f8c8d">书页 301 · §7.8 Dini Derivates</span>

<span style="color:#7f8c8d">（续接上一页例 7.25 的讨论。）</span>

<span style="color:#2471a3;">**[example]**</span> **例 7.25：** 两者都把零作为双侧极限点（two-sided limit point），因此集合 $\{x : f(x) = |x|\}$ 与 $\{x : f(x) = 0\}$ 都以零为双侧极限点。考察差商（difference quotient）可见
> <span style="color:#7f8c8d;">TBB §7.8, p.300</span>

```math
\limsup_{x\to 0^+}\frac{f(x)-f(0)}{x-0}=1,\qquad
\liminf_{x\to 0^+}\frac{f(x)-f(0)}{x-0}=0,
```

因此右导数 $f'_+(0)$ 在 $x=0$ 处不存在。同理，左导数 $f'_-(0)$ 也不存在。为使 $f$ 具有导数或单侧导数所必需的这些极限，在 $x=0$ 处都不存在。$\blacksquare$

<span style="color:#2471a3;">**[example]**</span> **例 7.26：** 定义在区间 $I$ 上的一个函数，可能处处都没有导数，甚至连单侧导数都没有。令
> <span style="color:#7f8c8d;">TBB §7.8, p.301</span>

```math
g(x)=
\begin{cases}
0, & \text{若 } x \text{ 为有理数},\\[2pt]
1, & \text{若 } x \text{ 为无理数}.
\end{cases}
```

由于 $g$ 在两侧的每一点都不连续，$g$ 在任何点都没有导数，也没有任何单侧导数。$\blacksquare$

此外，还存在这样的连续函数：它们在哪怕单单一个点处也缺失单侧导数（无论有限还是无穷）。这类函数很难构造，最早的构造是由 Besicovitch 于 1925 年给出的。

现在，导数在它存在时于分析中扮演着重要角色；而当它不存在时，准备一个替代物会十分有用。人们针对某些情形发展出了许多良好的替代物。也许最简单的这类替代物就是 Dini 导数（Dini derivates）。对于定义在某个开区间上的每个函数，它在每一点都存在。它们以意大利数学家 Ulisse Dini（1845–1918）的名字命名。

<span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f;">**定义 7.27：**</span> 设 $f$ 在 $x_0$ 的某个邻域上取实值。我们将 $f$ 在 $x_0$ 处的四个 Dini 导数定义如下。
> <span style="color:#7f8c8d;">TBB §7.8, p.301</span>

1. **右上 Dini 导数（upper right Dini derivate）**

```math
D^+ f(x_0)=\limsup_{x\to x_0^+}\frac{f(x)-f(x_0)}{x-x_0}
```

2. **右下 Dini 导数（lower right Dini derivate）**

```math
D_+ f(x_0)=\liminf_{x\to x_0^+}\frac{f(x)-f(x_0)}{x-x_0}
```

3. **左上 Dini 导数（upper left Dini derivate）**

```math
D^- f(x_0)=\limsup_{x\to x_0^-}\frac{f(x)-f(x_0)}{x-x_0}
```

<span style="color:#7f8c8d">书页 302 · §7.8 定义 7.27 续接</span>

<span style="color:#7f8c8d">*（定义 7.27 的第 4 项续接下一页。）*</span>

1. **左下 Dini 导数（lower left Dini derivate）**

```math
D_- f(x_0)=\liminf_{x\to x_0^-}\frac{f(x)-f(x_0)}{x-x_0}.
```

<span style="color:#2471a3;">**[example]**</span> **例 7.28：** 对于函数 $f(x)=|x|\,|\cos x^{-1}|$，$f(0)=0$，我们算得
> <span style="color:#7f8c8d;">TBB §7.8, p.302</span>

```math
D^+ f(0)=1,\quad D_+ f(0)=0,\quad D^- f(0)=0,\quad D_- f(0)=-1.
```

在其他各处 $f'(x)$ 都存在，且全部四个 Dini 导数都取该值。$\blacksquare$

<span style="color:#2471a3;">**[example]**</span> **例 7.29：** 函数
> <span style="color:#7f8c8d;">TBB §7.8, p.302</span>

```math
g(x)=
\begin{cases}
0, & \text{若 } x \text{ 为有理数},\\[2pt]
1, & \text{若 } x \text{ 为无理数}.
\end{cases}
```

在每个有理数 $x$ 处有

```math
D^+ g(x)=0,\quad D_+ g(x)=-\infty,\quad D^- g(x)=\infty,\quad D_- g(x)=0.
```

对无理数 $x$，Dini 导数有类似的值（见习题 7.8.1a）。$\blacksquare$

容易验证：函数 $f$ 在点 $x_0$ 处有导数的充分必要条件是，该点处全部四个 Dini 导数都相等；而 $f$ 在 $x_0$ 处有单侧导数的条件是，源自该侧的这两个 Dini 导数相等（见习题 7.8.2）。

我们以对一个情形的说明来结束本节：关于某个 Dini 导数的知识，能在何种意义下替代对普通导数的了解。我们证明一个关于单调性（monotonicity）的定理。你熟悉如下事实：若 $f$ 在区间 $[a,b]$ 上可微，且对所有 $x\in[a,b]$ 有 $f'(x)>0$，则 $f$ 是 $[a,b]$ 上的递增函数。（我们在第 7.7 节中给出了一个形式化证明。）

下面是该定理的一个推广。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**定理 7.30：**</span> 设 $f$ 在 $[a,b]$ 上连续。若对每个点 $x\in[a,b)$ 有 $D^+ f(x)>0$，则 $f$ 在 $[a,b]$ 上递增。
> <span style="color:#7f8c8d;">TBB §7.8, p.302</span>

<span style="color:#2471a3;">**[proof]**</span> **证明：** 我们首先证明 $f$ 在 $[a,b]$ 上不减（nondecreasing）。我们用反证法来证明。若 $f$ 在 $[a,b]$ 上并非不减，则存在点 $c$ 和 $d$ 满足 $a\leq c<d\leq b$ 且 $f(c)>f(d)$。令 $y$ 为区间 $(f(d),f(c))$ 内任意一点。由于 $f$ 在 $[a,b]$ 上连续，它具备介值性质（intermediate value property）。于是由定理 5.53 [或更确切地说，由该定理经习题 5.8.8(a) 给出的那个版本] 可知，存在点 $t\in(c,d)$ 使得 $f(t)=y$。从而集合 $\{x:f(x)=y\}\cap[c,d]$ 非空。令

```math
x_0=\sup\,\{x:\,c\leq x\leq d \text{ 且 } f(x)=y\}.
```

现在，$f(d)<y$ 且 $f$ 连续，由此可得 $x_0<d$。于是当 $x\in(x_0,d]$ 时 $f(x)<y$。再者，集合 $\{x:f(x)=y\}$ 是闭集（因为 $f$ 连续），所以 $f(x_0)=y$。

<span style="color:#7f8c8d">*（定理 7.30 的证明续接下一页。）*</span>


<!-- ===== W10 ===== -->

---
---
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定理 7.30 的收尾值得单独立一条注。它把 §7.8 那套 Dini 导数的机器拧出了果实：即便不知道 $f'$ 是否存在，只要「右上 Dini 导数」$D^+ f > 0$ 处处成立，$f$ 就必在 $[a,b]$ 上递增。整个推导是两步反证，骨架可提炼成命名模板「包络否证法」：若递增失败，必存在 $x_1<x_2$ 使 $f(x_1)>f(x_2)$，此时从峰值向右的差商族其上包络只会 $\le 0$，与 $D^+ f>0$ 撞车；若递增但不严格，则必有一段常值区间，其内部每点 $f'=0$，又令 $D^+ f>0$ 落空。第一性原理一目了然：$D^+f>0$ 的意思是「连斜率族里最悲观的那一支也仍然为正」，这股向前看的下行阻力一旦处处为正，曲线就无从下坡。跨课程连接：这正是 6.042J「对最坏情形取上界」在函数空间的翻版，也与 CSAPP 的「条件变弱时仍能给出保证」同构——Dini 导数让「处处不可微」这类病态函数也能被谈论斜率和单调，是后面 Darboux、凸性诸章的序曲。


<span style="color:#7f8c8d">书页 303 · §7.8 Dini Derivates（Dini 导数），接上一页 302</span>

<span style="color:#2471a3;">**[proof]**</span>（接上页，定理 7.30 证明之收尾）

但这蕴含 $D^+ f(x_0) \leq 0$，此与我们假设的 $D^+ f(x) > 0$（对所有 $x \in [a, b)$ 成立）相矛盾。

这一矛盾完成了 $f$ 为非递减（nondecreasing）函数的证明。

现在我们还想证明它事实上是递增的。

若不然，则必存在某个子区间，使得函数在其上恒为常数。

但在此区间内部的每一点处，我们都会有 $f'(x)=0$，因此在这样的点上，$D^+ f(x) > 0$ 便不可能成立。

$\blacksquare$

<span style="color:#7f8c8d">*（本页其余部分为 §7.8 习题区 Exercises 7.8.1–7.8.4，按约定跳过。）*</span>

---
<span style="color:#7f8c8d">书页 304 · §7.9 The Darboux Property of the Derivative（导数的 Darboux 性质）</span>
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定理 7.31 是全书最「反直觉却又必然」的结论之一：可微函数 $f$ 的导数 $f'$ 不必连续，却一定具备介值性质（Darboux 性质）。第一性原理在于「斜率是差商族的极限」：若在 $a$ 处斜率为负、在 $b$ 处斜率为正，那么沿曲线从 $(a,f(a))$ 走到 $(b,f(b))$，为了完成「由下转上」，途中必有一点斜率为零——这条曲线必须水平地翻转方向，无法凭空跳过水平态。其证明手法与连续函数介值定理相通，差别只在对象：$f$ 的连续靠「值没有裂缝」，而 $f'$ 的介值靠「差商族极限没有沟壑」。由此可推出 $f'$ 只能有振荡型间断，不能有跳跃或可去间断。这正好回应 §7.4 例 7.17 的 $x^2\sin(1/x)$：它的 $f'$ 在原点附近无限振荡、极限不存在，却又处处穿过任意给定值 $\gamma$——振荡得越密，越把「每个中间值都被取到」执行得越彻底。命名模板「微分不连续却保介值」；跨结构上与你泛函地体会的「场的方向由负转正必遇零」同出一辙，也解释了为什么「每一点都不连续」的导函数在数学上不可能出现。


<span style="color:#7f8c8d">*（本页前半仍为 §7.8 习题区 Exercises 7.8.4(c) 起及 7.8.5–7.8.10 的续文，按约定跳过。）*</span>

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">7.9 The Darboux Property of the Derivative（导数的 Darboux 性质）</span>

设 $f$ 在区间 $[a, b]$ 上可微。

我们在 Rolle 定理（Theorem 7.19）的证明中论证过：若 $f(a)=f(b)$，则存在一点 $c \in (a, b)$，使得 $f$ 在 $c$ 处取得一个极值（extremum）。

在这一点 $c$ 处，我们得到 $f'(c)=0$。

一个不同的假设同样能导向相同的结论。

设 $f$ 在 $[a, b]$ 上可微，且 $f'(a) < 0 < f'(b)$（或 $f'(b) < 0 < f'(a)$）。

再一次地，$f$ 所取得的最值（extreme value）必在 $[a, b]$ 内部的某一点 $c$ 处达到（为什么？），而在这一点处我们必得 $f'(c)=0$。

这一观察是下面这条定理的一个特例，该定理由 Darboux 于 1875 年首次证明。

#### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">定理 7.31</span>
> <span style="color:#7f8c8d;">TBB §7.9, p.304</span>

设 $f$ 在区间 $I$ 上可微。

设 $a, b \in I$、$a < b$，且 $f'(a) \neq f'(b)$。

令 $\gamma$ 为介于 $f'(a)$ 与 $f'(b)$ 之间的任意一个数。

则存在 $c \in (a, b)$，使得 $f'(c)=\gamma$。

<span style="color:#2471a3;">**[proof]**</span> **证明。**

令 $g(x)=f(x)-\gamma x$。

若 $f'(a) < \gamma < f'(b)$，则 $g'(a)=f'(a)-\gamma < 0$ 且 $g'(b)=f'(b)-\gamma > 0$。

定理陈述之前的讨论表明，存在 $c \in (a, b)$ 使得 $g'(c)=0$。

对这个 $c$，我们得到
```math
f'(c)=g'(c)+\gamma=\gamma,
```
从而完成了 $f'(a) < f'(b)$ 这一情形的证明。

$\blacksquare$

<span style="color:#7f8c8d">*（定理 7.31 证明的其余部分续于书页 305。）*</span>
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定理 7.32 圆上了 §7.3.3 例 7.12 留下的「缺口」：在那里我们只对「已知反函数存在」的函数（如 $\sqrt{x}$、$\ln z$）借用恒等式 $f(g(x))=x$ 求导，却从没证明反函数真的存在、更没证明它可微。现在靠 Darboux 性质补上关键的 (i)：$f'\neq 0$ 处处成立，由介值性推出 $f'$ 必在 $I$ 上恒正或恒负，从而 $f$ 严格单调、一一映射；再由「连续且严格单调 ⟹ 反函数连续」（习题 5.9.16），就可对差商取极限，干净利落地得到 $(f^{-1})'(f(x))=1/f'(x)$。第一性原理一句话：求反函数导数就是把「伸缩比」倒过来，而 Darboux 性质保证了这幅图景可行——$f'$ 不跨零，伸缩方向和大小在定义区间内不会忽正忽负地反转漂移。给这条留下命名模板「先证合法再求导」：凡依赖反函数的公式，都要先确认存在性与可微性，这正是 §7.3 那一步所欠的证明。跨课程对称：与 Strang「矩阵可逆 ⟺ 行列式非零」同构——$f'=0$ 恰似矩阵奇异，反函数在导数为零处宣告失效。



<!-- ===== W11 ===== -->


<span style="color:#7f8c8d">书页 305 · §7.9 The Darboux Property of the Derivative（导数的 Darboux 性质）</span>

<span style="color:#7f8c8d">*（本页承接书页 304：Theorem 7.31 关于导数 Darboux 性质的证明在此收尾。）*</span>

当 $f'(a) > f'(b)$ 时的证明是类似的。

$\blacksquare$

你也许已经注意到，Theorem 7.31 恰恰断言：可微函数（differentiable function）的导数具有 Darboux 性质（Darboux property），也就是我们在第 5.8 节为连续函数（continuous function）所建立的介值性质（intermediate value property）。

当然，可微函数 $f$ 的导数 $f'$ 不必是连续的。

然而，该结果确实蕴涵着：$f'$ 不能有跳跃间断（jump discontinuity），也不可能有可去间断（removable discontinuity）。

中值定理（mean value theorem）与 Theorem 7.31 二者都给出了关于可微函数 $f$ 的导数 $f'$ 的值域（range）的信息。

中值定理蕴涵着：$f'$ 的值域包含由 $f$ 在定义区间上的图像所确定的所有弦（chord）的斜率。

定理 7.31（Theorem 7.31）则告诉我们，这个值域实际上是一个区间。

该区间可能是无界的（unbounded）；若它有界，则它可能包含也可能不包含其端点。

（见 Exercise 7.9.1。）

定理 7.31（Theorem 7.31）使我们可以建立一条关于对反函数求导的熟悉定理。

### <span style="color:#2471a3;">**[subsection]**</span> <span style="color:#c0392b">Derivative of an Inverse Function（反函数的导数）</span>

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 7.32：反函数的导数</span>
> <span style="color:#7f8c8d;">TBB §7.9, p.305</span>

设 $f$ 在区间 $I$ 上可微，并且对每个 $x \in I$ 都有 $f'(x) \neq 0$。

则

(i) $f$ 在 $I$ 上是一一映射（one-to-one），

(ii) $f^{-1}$ 在 $J = f(I)$ 上可微，

(iii) 对所有 $x \in I$，成立

```math
(f^{-1})'(f(x)) = \frac{1}{f'(x)}.
```

### <span style="color:#2471a3;">**[proof]**</span> <span style="color:#c0392b">证明</span>

由 Theorem 7.31，要么对所有 $x \in I$ 有 $f'(x) > 0$，要么对所有 $x \in I$ 有 $f'(x) < 0$。

无论哪种情形，$f$ 在 $I$ 上要么递增要么递减，从而是一一映射，这就确立了 (i)。

为验证 (ii) 与 (iii)，首先注意 $f^{-1}$ 是连续的，因为 $f$ 连续且严格单调（见 Exercise 5.9.16）。

设 $y_0 \in J$，并令 $x_0 = f^{-1}(y_0)$。

我们想证明 $(f^{-1})'(y_0)$ 存在且取值等于 $1/(f'(x_0))$。

对 $x \in I$，记 $y = f(x)$，从而 $x = f^{-1}(y)$。

考虑差商：

```math
\frac{f^{-1}(y) - f^{-1}(y_0)}{y - y_0}
= \frac{x - x_0}{f(x) - f(x_0)}.
```

当 $y \to y_0$ 时，由于函数 $f^{-1}$ 连续，所以 $x \to x_0$。

因此

```math
\lim_{y \to y_0} \frac{f^{-1}(y) - f^{-1}(y_0)}{y - y_0}
= \lim_{x \to x_0} \frac{1}{\frac{f(x)-f(x_0)}{x-x_0}}
= \frac{1}{f'(x_0)}.
```

$\blacksquare$

<span style="color:#7f8c8d">书页 306 · §7.9 习题区</span>

> <span style="color:#7f8c8d">*（书页 306 为 §7.9 习题区 Exercises 7.9.1–7.9.5，按约定整页跳过。）*</span>


<!-- ===== W12 ===== -->

<!-- ===== W12 · 书页 307–308 · §7.10 Convexity / 定义 7.33 / 弦的几何意义 / 推论 (14) ===== -->
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定义 7.33 把「凸」从初等微积分的 $f''\ge 0$ 提升为不依赖可微性的弦不等式，这里藏着贯穿优化的第一性原理：$f(\alpha x_1+(1-\alpha)x_2)\le \alpha f(x_1)+(1-\alpha)f(x_2)$——左边是函数在凸组合点上的值，右边是端点值的同名线性组合，翻译成人话就是「曲线上任意两点间的弦不会低于曲线本身」。最该建立的是与 Strang 优化直觉的联系：若 $f$ 可微且凸，则图像位于每一点切线上方，即 $f(y)\ge f(x)+f'(x)(y-x)$。这使任意点的切线都是整个函数的全局下界（global lower bound），于是 $f'(x_0)=0$ 直接从 §7.5 的「驻点候选」升级成「全局极小点」——局部即全局，这正是凸性让机器学习与数值优化「白赚」的地方。可对照定理 7.18：那里导数归零只是必要条件，正是凸性把「候选」改判为「唯一最优」。命名模板「切线下界判定全局最优」；跨课程上，凸集「两点连线仍在集内」与向量空间「线性组合仍落闭包」同构，为后续线性规划、对偶、以及 $f''\ge 0$ 对应的半正定二次型铺好路。


<span style="color:#7f8c8d">书页 307 · §7.10 Convexity（凸性）</span>

#### <span style="color:#2471a3;">**[figure]**</span> <span style="color:#c0392b">Figure 7.10（图 7.10）</span>

图 7.10　上凹、下凹、上凹（concave up/down/up）三种情形的图示。

<span style="color:#7f8c8d">*（本页顶部为 §7.9 习题区的末尾，含题目 7.9.6 与 7.9.7，按约定跳过。）*</span>

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">7.10 Convexity（凸性）</span>

在初等微积分（elementary calculus）中，人们研究函数在某个区间上是上凹（concave-up）还是下凹（concave-down）。

了解一个函数在哪些区间上凹、在哪些区间下凹，对于诸如画方程 $y = f(x)$ 的草图、以及研究函数的极值（extrema）等目的都很有用（见图 7.10）。

在初等微积分的情境下，所涉区间上的函数通常都具有二阶导数（second derivative）。

在此情境中我们这样定义：若在区间 $I$ 上满足 $f'' \ge 0$，则称 $f$ 在 $I$ 上上凹；若 $f'' \le 0$ 则称其下凹。

也可以给出只涉及一阶导数（first derivative）、而不涉及二阶导数的定义：若 $f'$ 在 $I$ 上递增（increasing），则 $f$ 在 $I$ 上上凹；若 $f'$ 在 $I$ 上递减（decreasing），则 $f$ 下凹。

等价地说，$f$ 上凹当且仅当 $f$ 的图像位于它的每条切线（tangent line）“之上”（更精确地说是“不低于”）；$f$ 下凹当且仅当图像位于每条切线之下（不高于）。

当我们称一个函数上凹或下凹时，想要捕捉的那些几何性质并不依赖于可微性（differentiability）。

这一条件应当是：图像位于它的所有弦（chord）之下（或之上）。

下面这些定义把这一概念精确化。

我们将遵循常见做法，用“凸”（convex）与“凹”（concave）这两个术语替代“上凹”与“下凹”。

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#c0392b">Definition 7.33（定义 7.33）</span>
> <span style="color:#7f8c8d;">TBB §7.10, p.307</span>

<span style="color:#00838f">设 $f$ 定义在区间 $I$ 上。若对所有 $x_1, x_2 \in I$ 及 $\alpha \in [0, 1]$，不等式</span>

```math
f(\alpha x_1 + (1-\alpha) x_2) \le \alpha f(x_1) + (1-\alpha) f(x_2)  \tag{13}
```

<span style="color:#00838f">成立，我们就称 $f$ 在 $I$ 上是凸的（convex）。若 (13) 中的反向不等式成立，则称 $f$ 在 $I$ 上是凹的（concave）。若对所有 $\alpha \in (0, 1)$ 这些不等式都是严格的，则称 $f$ 在 $I$ 上是严格凸（strictly convex）或严格凹（strictly concave）的。</span>

---

<span style="color:#7f8c8d">书页 308 · Differentiation 第 7 章（续）</span>

#### <span style="color:#2471a3;">**[figure]**</span> <span style="color:#c0392b">Figure 7.11（图 7.11）</span>

图 7.11　不等式 (14) 中三个斜率（slope）的比较。

例如，函数 $f(x) = |x|$ 在 $\mathbb{R}$ 上是凸的，但并不是严格凸。

严格凸性意味着 $f$ 的图像中不含有任何直线段（line segment）。

注意：函数 $f(x) = |x|$ 在 $x = 0$ 处并不可微（differentiable）。

定义凸性的几何条件确实蕴含了函数很大程度的正则性（regularity）。

我们的首要目标正是处理这一问题。

我们先从一些简单的几何考察（geometric consideration）入手。

设 $f$ 在开区间（open interval）$I$ 上凸，并设 $x_1, x_2$ 为 $I$ 中满足 $x_1 < x_2$ 的两点。

由点 $(x_1, f(x_1))$ 与 $(x_2, f(x_2))$ 所确定的弦在 $[x_1, x_2]$ 上定义一个线性函数（linear function）$M$：若 $x = \alpha x_1 + (1-\alpha)x_2$，则

```math
M(x) = \alpha f(x_1) + (1-\alpha) f(x_2).
```

“凸”的定义表明：对所有 $x \in [x_1, x_2]$ 都有 $f(x) \le M(x)$，并且 $M(x_1) = f(x_1)$、$M(x_2) = f(x_2)$。

现在令 $z \in (x_1, x_2)$，则

```math
\frac{f(z) - f(x_1)}{z - x_1} \le \frac{M(z) - M(x_1)}{z - x_1} = \frac{M(x_2) - M(z)}{x_2 - z} \le \frac{f(x_2) - f(z)}{x_2 - z}  \tag{14}
```

（见图 7.11）。

于是，由 $f$ 及点 $x_1$、$x_2$ 确定的弦，其斜率介于——由 $x_1$ 与 $z$ 确定的弦的斜率、以及由 $z$ 与 $x_2$ 确定的弦的斜率——之间。

不等式 (14) 有一系列有用的推论：

1. 对固定的 $x \in I$，差商 $\frac{f(x+h) - f(x)}{h}$ 在某个区间 $(0, \delta)$ 上是 $h$ 的不减函数（nondecreasing function）。

因此

```math
\lim_{h \to 0^+} \frac{f(x+h) - f(x)}{h} = \inf_{h > 0} \frac{f(x+h) - f(x)}{h}.
```

<span style="color:#7f8c8d">*（本处推论 1 的结论在书页 309 继续，此处结束。）*</span>
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定理 7.34 揭示「凸」这个看似温和的词蕴含的巨大正则性：不加可微假设，仅凭弦不等式，函数就在区间内部处处有有限单侧导数，且左、右导数都单调不减，彼此间还满足 $f'_-(x)\le f'_+(x)$，甚至直接推出 $f$ 连续。证明的命名模板是「差商单调钳形」：由前页不等式 (14)，固定左端点、把右端增量 $h$ 缩小，差商族 $\frac{f(x+h)-f(x)}{h}$ 随 $h$ 递减，于是 $h\to 0^+$ 时该差商族单调下降、收敛到其下确界，右导数存在，左导数同理。据此推论 7.35 给出最顺手的判别规则：可微时凸 ⟺ $f'$ 不减；二阶可微时凸 ⟺ $f''\ge 0$——这正接回初等微积分的「上凹」。值得点破：定义 7.33 是缺省条件下仍能运作的通用幕布，推论 7.35 是可微世界里的捷径，二者层级不同、各司其职。第一性原理可浓缩成「凸性 = 增长率的增长率非负」，与你在 Strang 处体会的「二次型半正定」语义相通；命名模板「斜率单调 ⇔ 凸」务必留给未来的优化讲义复用。



<!-- ===== W13 ===== -->

<span style="color:#7f8c8d">书页 309 · §7.10 Convexity（凸性）（续）</span>

> <span style="color:#1e8449;">**[note] Note（译者注）**</span>

本节从书页 308 续起：上一页已就凸函数建立了若干条观察，本页将完成其论证，并把它们归结为可微性、连续性层面的严密结论。

---

**前提延续**：设 $f$ 在开区间 $I$ 上凸，$x$ 固定于 $I$ 内，$h$ 为（可正可负的）充分小的增量，使得 $x+h \in I$。

上一页已证明一个重要不等式，记之为 (14)，它刻画了差商随 $h$ 增加的单调变化。

---

#### 观察 1（续）：右导数与左导数存在且有限

<span style="color:#7f8c8d">*（接前页：本句从书页 308 续起。）*</span>……其极限存在，或者可能为 $-\infty$。

实际上可以证明该极限值是有限的，方法是用 (14) 再来一次，以取得一个有限下界，因为对任意满足 $x_0 < x$ 的 $x_0 \in I$，有

```math
\frac{f(x_0)-f(x)}{x_0-x} \le \frac{f(x+h)-f(x)}{h},
```

由此即得 $f$ 在 $x$ 处存在有限数值的右导数（right-hand derivative）$f'_+(x)$。

类似地，$f$ 在 $x$ 处也存在有限数值的左导数。

#### 观察 2：单侧导数不减

<span style="color:#1e8449;font-weight:bold;">若 $x, y \in I$ 且 $x < y$，则</span>

```math
f'_+(x) \le f'_+(y).
```

由观察 1 我们推得：只要 $h > 0$ 且 $x+h$、$y+h$ 都在 $I$ 中，就有

```math
\frac{f(x+h)-f(x)}{h} \le \frac{f(y+h)-f(y)}{h}.
```

因此 $f'_+$ 是一个不减（nondecreasing）函数。

同理，$f'_-$ 也是一个不减函数。

#### 观察 3：左、右导数之间的大小关系

由 (14) 同样清楚地看出

```math
f'_-(x) \le f'_+(x)
```

对所有 $x \in I$ 成立。

#### 观察 4：$f$ 在 $I$ 上连续

$f$ 在 $I$ 上连续。

为看出这一点，注意由于在每一点处两个单侧导数都存在，函数在两侧都必定连续，因而整体连续。

---

我们将上述讨论总结为一条定理。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 7.34（定理 7.34）</span>
> <span style="color:#7f8c8d;">TBB §7.10, p.309</span>

**定理 7.34**：设 $f$ 在开区间 $I$ 上凸。则

<span style="color:#c0392b">(i)</span> $f$ 在 $I$ 的每一点处都有有限的左导数和右导数。

这些单侧导数在 $I$ 上都是 $x$ 的不减函数，并且

```math
f'_-(x) \le f'_+(x) \quad \text{对所有 } x \in I, \qquad (15)
```

<span style="color:#c0392b">(ii)</span> $f$ 在 $I$ 上连续。

> <span style="color:#1e8449;">**[note] Note（注）**</span>

注：若 $f$ 在闭区间 $[a,b]$ 上凸，则某些结论在端点 $a$ 与 $b$ 处并不适用（参见习题 7.10.8）。

还要注意，相应的结论对 $I$ 上的凹函数（concave function）依然成立，只不过此时单侧导数是 $x$ 的不增（nonincreasing）函数，且 (15) 中的不等式反向。

---

现在我们可以得到初等微积分中熟知的凸函数特征刻画。

### <span style="color:#2471a3;">**[corollary]**</span> <span style="color:#c0392b">Corollary 7.35（推论 7.35）</span>
> <span style="color:#7f8c8d;">TBB §7.10, p.309</span>

**推论 7.35**：设 $f$ 定义在开区间 $I$ 上。

<span style="color:#c0392b">(i)</span> 若 $f$ 在 $I$ 上可微，则 $f$ 在 $I$ 上凸当且仅当 $f'$ 在 $I$ 上不减。

<span style="color:#c0392b">(ii)</span> 若 $f$ 在 $I$ 上二阶可微，则 $f$ 在 $I$ 上凸当且仅当 $f'' \ge 0$ 在 $I$ 上成立。

我们将推论 7.35 的验证留作习题 7.10.9。

---

<span style="color:#7f8c8d">书页 310 · Differentiation（微分）· 第 7 章</span>

<span style="color:#7f8c8d">*（书页 310 为 §7.10 的习题区 Exercises 7.10.1–7.10.12，按约定跳过，不翻译、不收录。）*</span>

> <span style="color:#7f8c8d">*(本页其余部分为 §7.10 习题区 Exercises 7.10.1–7.10.12，按约定跳过。)*</span>


<!-- ===== W14 ===== -->

<!-- ===== W14 · 书页 311–312 · §7.10 习题边界 / §7.11 L'Hôpital's Rule 开头 + 例 7.36、7.37 ===== -->

<span style="color:#7f8c8d">书页 311 · §7.10 Convexity（凸性）（续）</span>

<span style="color:#7f8c8d">*（书页 311 为 §7.10 的习题区 Exercises 7.10.13–7.10.16，按约定跳过，不翻译、不收录。）*</span>

<span style="color:#7f8c8d">*（本页习题覆盖：7.10.13 可数集上的凸函数与不可微点集；7.10.14 Inflection Points（拐点）的定义 A/B/C 及其关系；7.10.15 Jensen's Inequality（Jensen 不等式）$f\!\big(\sum\alpha_k x_k\big) \le \sum\alpha_k f(x_k)$；7.10.16 Jensen 不等式等号成严的刻画。按约定跳过。）*</span>

> <span style="color:#7f8c8d">*(本页其余部分为 §7.10 习题区 Exercises 7.10.13–7.10.16，按约定跳过。)*</span>

<span style="color:#7f8c8d">*（§7.10 凸性至此结束，下一页转入 §7.11 洛必达法则。）*</span>

---

<span style="color:#7f8c8d">书页 312 · Differentiation（微分）· 第 7 章 · §7.11</span>
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 例 7.36 与例 7.37 是洛必达法则的思想启蒙课：当分子分母都趋零时，比值不再由「极限之比」（$0/0$ 无意义）决定，而取决于「谁更快地趋零」。例 7.36 里 $6x/3x$ 恒等于 $2$，是两条直线速率的纯比；例 7.37 的 $\frac{6x+x^2}{3x+5x^3}$ 则把高阶小项 $x^2$、$5x^3$ 当作可忽略的噪声，主导项系数之比 $6/3=2$ 就是极限。第一性原理是「一次近似用线性主导」：在原点近旁 $f(x)=6x+x^2\approx 6x$，因为 $x^2$ 比 $x$ 小得多；而 $f'(0)=6$ 正是这一点的局部伸缩率，分子分母的速率比也就是它俩在原点的斜率之比。命名模板「线性主导定比率」：任何 $0/0$ 型都在悄悄比较一阶 Taylor 系数。跨课程连接：这就是你在 CSAPP 里见惯的「首项决定渐近」的数学版，也是级数与积分里「主导收敛项」判断的原型——速率之争，实为整条实分析的潜台词。


### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">7.11 L'Hôpital's Rule（洛必达法则）</span>

> <span style="color:#1e8449;">**[note] Note（注）**</span>

本节为富集章节（enrichment section），可以省略。

设 $f$ 与 $g$ 定义在 $x_0$ 的某个去心邻域（deleted neighborhood）中，并且

```math
\lim_{x\to x_0} f(x) = A, \qquad \lim_{x\to x_0} g(x) = B.
```

按照我们通常的极限理论，于是有

```math
\lim_{x\to x_0}\frac{f(x)}{g(x)} = \frac{\lim_{x\to x_0} f(x)}{\lim_{x\to x_0} g(x)} = \frac{A}{B},
```

除非 $B = 0$。

但当 $B = 0$（这是经常遇到的情形）时又会怎样呢？存在多种可能：

若 $B = 0$ 且 $A \neq 0$，则极限不存在。

最有趣的情形是这样：若 $A$ 与 $B$ 都为零，则极限行为（limiting behavior）取决于 $f(x)$ 与 $g(x)$ 各自趋近于零的速率。

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 7.36（例 7.36）</span>
> <span style="color:#7f8c8d;">TBB §7.11, p.312</span>

考虑

```math
\lim_{x\to 0}\frac{6x}{3x} = \lim_{x\to 0}\frac{6}{3} = 2.
```

从几何上看这个简单例子。

对 $x \neq 0$，高度 $6x$ 是高度 $3x$ 的两倍。

直线 $y = 6x$ 趋近于零的速率，是直线 $y = 3x$ 趋近于零的速率的两倍。

$\blacksquare$

#### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 7.37（例 7.37）</span>
> <span style="color:#7f8c8d;">TBB §7.11, p.312</span>

现在考虑一个稍复杂的极限

```math
\lim_{x\to 0}\frac{f(x)}{g(x)} = \lim_{x\to 0}\frac{6x + x^2}{3x + 5x^3}.
```

若用 $x \neq 0$ 去除分子和分母（numerator and denominator），我们会看到该极限与

```math
\lim_{x\to 0}\frac{6 + x}{3 + 5x^2}
```

相同。

这最后一个极限可以用我们通常的初等方法算出等于 $6/3 = 2$。

这里，对靠近零的 $x \neq 0$，高度 $f(x) = 6x + x^2$ 近似为 $6x$，而 $g(x) = 3x + 5x^3$ 的高度近似为 $3x$，也就是说，所求比值近似为 $2$。

于是，分子再次以约两倍于分母的速率趋近于零。

我们可以通过精确地计算这些速率，使上面的说法更严格。

设 $f(x) = 6x + x^2$ 且 $g(x) = 3x + 5x^3$，则

```math
f'(x) = 6 + 2x, \quad f'(0) = 6;\qquad g'(x) = 3 + 5x^2, \quad g'(0) = 3.
```

这就使我们的陈述——分子以两倍于分母的速率趋近于零——精确化了。

（参见图 7.12，其中给出函数 $f$ 与 $g$ 的图形与直线 $y = 6x$、$y = 3x$ 相对照的示意图。）

$\blacksquare$


<!-- ===== W15 ===== -->

<span style="color:#7f8c8d">书页 313 · §7.11 L'Hôpital's Rule（洛必达法则）</span>
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 洛必达法则是数学史上最著名的一桩「名实不符」。G. de L'Hôpital（1661–1704）是法国贵族数学家，1696 年出版《无穷小分析》（Analyse des Infiniment Petits），这是首部系统化的微积分教材，其中便载有此法则；但这条法则其实源自 Johann Bernoulli（1667–1748）的讲授。史实：1694 年 Bernoulli 与 L'Hôpital 签下每年 300 里弗尔（livres）的协议，把研究成果卖给后者供其出版获名。而直到 1921 年，Schafheitlin 在巴塞尔大学图书馆发现 Bernoulli 1691–92 年的微分学讲义手稿，学者方据此确认法则确系出自 Bernoulli 的讲授——一项延宕二百余载的历史正名就此落定（该手稿后于 1922–23 年作为《Lectiones de calculo differentialium》出版）。工程视角上看，$0/0$ 型是「分子分母同时趋于零」的消隐之争，$\infty/\infty$ 型则是「双雄竞速」的比率赛：两者都要先改写为能套 Cauchy 中值定理的标准形，再取极限。还要记牢方向性：法则只保证「若 $f'/g'$ 收敛，则 $f/g$ 同极限」，反过来说并不成立——定理 7.38 的注与习题 7.11.5 正提醒这一点，滥用方向会踩空。


## §7.11 L'Hôpital's Rule

<span style="color:#2471a3;">**[figure]**</span> 图 7.12 对（例 7.37 中两个函数的）变化速率作了对比。

我们试着从上面两个例子中作推广。假设 $f$ 与 $g$ 在 $x=a$ 的某个邻域内均可微，且 $f(a)=g(a)=0$。请考察下面的计算过程，以及为了让这些计算成立，需要对 $f$、$g$ 施加的条件。

```math
\frac{f(x)}{g(x)}
= \frac{f(x)-f(a)}{g(x)-g(a)}
= \frac{\frac{f(x)-f(a)}{x-a}}{\frac{g(x)-g(a)}{x-a}}
\to \frac{f'(a)}{g'(a)}
= \lim_{x\to a}\frac{f'(x)}{g'(x)}. \tag{16}
```

若这些计算成立，它们表明在此种假设（$f(a)=g(a)=0$，且 $f'(a)$ 与 $g'(a)$ 均存在）之下，我们应能断言下式成立：$\lim_{x\to a}\dfrac{f(x)}{g(x)}=\lim_{x\to a}\dfrac{f'(x)}{g'(x)}$。

你应当核对为使这些计算成立所必须具备的各项条件：$g(x)$ 在所考察邻域内的任何一点（$a$ 除外）都不能等于零；$g(x)$ 也不能等于 $g(a)$（当 $x\ne a$ 时）；$f(a)$ 与 $g(a)$ 必须等于零（这是第一个等号所需的）；并且 $f'/g'$ 在 $x=a$ 处必须连续（这是最后一个等号所需的）。

计算式 (16) 为一种名为洛必达法则（L'Hôpital's rule）的求极限方法提供了一个基本形式的简单证明。之所以称其"基本"，是因为我们所假设的某些条件对最终结论 $\lim_{x\to a}\dfrac{f(x)}{g(x)}=\lim_{x\to a}\dfrac{f'(x)}{g'(x)}$ 并非必要。

### 7.11.1 L'Hôpital's Rule: 0/0 Form（洛必达法则：0/0 型）

<span style="color:#1e8449">*(增补小节（Enrichment section），可略过。)*</span>

我们的第一个定理给出了与引言表述一致、但假设更弱的一个版本的法则。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">**定理 7.38（L'Hôpital's Rule: 0/0 Form，洛必达法则：0/0 型）**</span> 假设函数 $f$ 与 $g$ 在 $x=a$ 的某个去心邻域（deleted neighborhood）$N$ 内均可微。再假设
> <span style="color:#7f8c8d;">TBB §7.11, p.313</span>

(i) $\lim_{x\to a}f(x)=0$，

(ii) $\lim_{x\to a}g(x)=0$，

<span style="color:#7f8c8d">书页 314 · §7.11 L'Hôpital's Rule（续）</span>

(iii) 对每个 $x\in N$，都有 $g'(x)\ne 0$，且

(iv) $\lim_{x\to a}\dfrac{f'(x)}{g'(x)}$ 存在。

那么 $\lim_{x\to a}\dfrac{f(x)}{g(x)}=\lim_{x\to a}\dfrac{f'(x)}{g'(x)}$。

<span style="color:#2471a3;">**[proof]**</span> <span style="color:#c0392b">**证明。**</span> 我们的各项假设并不要求 $f$、$g$ 在 $x=a$ 处有定义。但无论如何我们都可以令 $f(a)=g(a)=0$ 来定义（或重新定义）$f$、$g$ 在 $x=a$ 处的取值。由假设 (i) (ii)，这会在点 $x=a$ 的整个邻域 $N\cup\{a\}$ 上得到两个连续函数。现在我们可以应用 Cauchy 形式的中值定理 (7.21)。设 $x\in N$ 且 $a<x$。由定理 7.21，存在某个 $c=c_x\in(a,x)$ 使得

```math
\bigl[f(x)-f(a)\bigr]g'(c_x)=\bigl[g(x)-g(a)\bigr]f'(c_x). \tag{17}
```

由于 $f(a)=g(a)=0$，式 (17) 化为

```math
f(x)g'(c_x)=g(x)f'(c_x). \tag{18}
```

式 (18) 对 $N$ 中满足 $x>a$ 的一切 $x$ 成立。我们希望把式 (18) 改写为如下形式：

```math
\frac{f(x)}{g(x)}=\frac{f'(c_x)}{g'(c_x)}. \tag{19}
```

为证式 (19)，我们指出 $g(x)$ 在 $N\cap\{x:x>a\}$ 中恒不等于零。（至于 $g'(c_x)$ 在 $N$ 中恒不为零，则由假设 (iii) 保证。）若对某个 $x\in N$ 且 $x>a$ 有 $g(x)=0$，则由 Rolle 定理，必存在一点 $t\in(a,x)$ 使 $g'(t)=0$，这与假设 (iii) 矛盾（原书此处笔误写作 (ii)，按逻辑应为结论 (iii)，即 $g'\ne 0$）。从而等式 (19) 对 $N\cap\{x:x>a\}$ 中的一切 $x$ 成立。类似的论证表明：若 $x\in N$ 且 $x<a$，则存在 $c_x\in(x,a)$ 使 (19) 成立。

现在当 $x\to a$ 时，由于 $c_x$ 位于 $a$ 与 $x$ 之间，$c_x$ 也趋近于 $a$。因此

```math
\lim_{x\to a}\frac{f(x)}{g(x)}=\lim_{x\to a}\frac{f'(c_x)}{g'(c_x)}=\lim_{x\to a}\frac{f'(x)}{g'(x)},
```

其中最后一个极限由假设 (iv) 保证存在。$\blacksquare$

<span style="color:#2471a3;">**[note]**</span> <span style="color:#1e8449">**注。**</span> 注意我们并未要求 $f$ 在 $x=a$ 处有定义，也未要求 $f'/g'$ 在 $x=a$ 处连续。还需特别留意：洛必达法则并不意味着，在满足定理 7.38 的假设 (i) (ii) (iii) 时，只要 $\lim_{x\to a}f(x)/g(x)$ 存在，$\lim_{x\to a}f'(x)/g'(x)$ 就一定也存在。习题 7.11.5 给出了一个例子来说明这一点。

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">**例 7.39：**</span> 我们用洛必达法则来求 $\lim_{x\to 0}\ln(1+x)/x$。取 $f(x)=\ln(1+x)$，$g(x)=x$。那么 $\lim_{x\to 0}f(x)=\lim_{x\to 0}g(x)=0$，且 $f'(x)=\dfrac{1}{1+x}$，$g'(x)=1$。
> <span style="color:#7f8c8d;">TBB §7.11, p.314</span>

<span style="color:#7f8c8d">*（本页其余部分为 §7.11 洛必达法则内容续接至书页 315，跨页断句处由后续 worker 承接。）*</span>


<!-- ===== W16 ===== -->

---
<!-- ===== 书页 315（PDF 页 31）===== -->
---
<span style="color:#7f8c8d">书页 315 · §7.11 L'Hôpital's Rule（洛必达法则·续）</span>

于是

```math
\lim_{x\to 0}\frac{\ln(1+x)}{x} = \lim_{x\to 0}\frac{1}{1+x} = 1.
```

$\blacksquare$

我们把该定理称为「$\frac{0}{0}$ 型」（the "$0/0$" form）不定型，理由显而易见。

此外还有一种 $\frac{\infty}{\infty}$ 型的版本（见 Theorem 7.42）。

还有可能作其他形式的修改。

点 $a$ 可以换成 $a=\infty$ 或 $a=-\infty$（Theorem 7.41），且结论对单侧极限（one-sided limits）同样成立。

（我们对 Theorem 7.38 的证明其实已经确立了这一点，因为我们分别考虑了 $x>a$ 与 $x<a$ 的情形。）

还有形形色色的其他「不定型」（indeterminate form）——它们正是那些极限依赖于各组成部分接近各自极限时的速率（rate）的情形——都可以通过变形处理，从而得以运用洛必达法则。

下面是一个「$1^\infty$ 型与 $1^{-\infty}$ 型」登场的例子。

注意：我们欲求其极限的那个函数具有 $f(x)^{g(x)}$ 的形式，其中当 $x\to a$ 时 $f(x)\to 1$，但当 $x\to a^+$ 时 $g(x)\to\infty$，而当 $x\to a^-$ 时 $g(x)\to -\infty$。

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">例 7.40</span>
> <span style="color:#7f8c8d;">TBB §7.11, p.315</span>

求极限 $\lim_{x\to 0}(1+x)^{2/x}$。

这个表达式属于 $1^\infty$ 型（当 $x>0$ 时）。

为计算 $\lim_{x\to 0}(1+x)^{2/x}$，令

```math
y=(1+x)^{2/x},\qquad z=\ln y = \frac{2}{x}\ln(1+x).
```

函数 $z$ 的分子与分母满足洛必达法则的假设。

于是

```math
\lim_{x\to 0}z = \lim_{x\to 0}\frac{2\ln(1+x)}{x} = \lim_{x\to 0}\frac{2}{1+x}=2 .
```

由于 $\lim_{x\to 0}z=2$，故 $\lim_{x\to 0}y=e^2$。$\blacksquare$

<span style="color:#2471a3;">**[subsection]**</span> <span style="color:#c0392b">7.11.2 洛必达法则（当 $x\to\infty$ 时）</span>

<span style="color:#7f8c8d">*（本节为拓展内容 Enrichment section，可略读 May be omitted。）*</span>

我们在 $a\in\mathbb{R}$ 的假设下证明了 Theorem 7.38，但该定理在 $a=-\infty$ 或 $a=+\infty$ 时同样成立。

在这种情况下，我们当然是在处理单侧极限。

与前面一样，关系式

```math
\lim_{x\to\infty}\frac{f'(x)}{g'(x)}=L
```

蕴含着当 $x\to\infty$ 时函数 $f(x)$ 与 $g(x)$ 相对增长速度（relative rates of growth）的某些信息。

通过对 Theorem 7.38 作一个简单的变换，我们就可为 $a=\infty$（或 $-\infty$）时的洛必达法则各版本建立证明。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">定理 7.41</span>
> <span style="color:#7f8c8d;">TBB §7.11, p.315</span>

设 $f,g$ 在某个区间 $(-\infty,b)$ 上可微。

假设

(i) $\lim_{x\to-\infty}f(x)=0$，

(ii) $\lim_{x\to-\infty}g(x)=0$，

(iii) 对每个 $x\in(-\infty,b)$，$g'(x)\ne 0$，且

(iv) $\lim_{x\to-\infty}f'(x)/g'(x)$ 存在。

则

```math
\lim_{x\to-\infty}\frac{f(x)}{g(x)} = \lim_{x\to-\infty}\frac{f'(x)}{g'(x)} .
```

若在这些假设中用 $+\infty$ 替换 $-\infty$，也有类似的结果成立。

<span style="color:#2471a3;">**[proof]**</span> <span style="color:#c0392b">证明</span>

令 $x=-1/t$。

于是当 $t\to0^+$ 时 $x\to-\infty$，反之亦然。

定义函数 $F$ 与 $G$ 如下：

```math
F(t)=f\!\left(-\frac{1}{t}\right),\qquad G(t)=g\!\left(-\frac{1}{t}\right) .
```

函数 $F$ 与 $G$ 都定义在某个区间 $(0,\delta)$ 上。

我们容易验证

```math
\lim_{t\to0^+}F(t)=\lim_{t\to0^+}G(t)=0
```

且

```math
\lim_{t\to0^+}\frac{F'(t)}{G'(t)} = \lim_{x\to-\infty}\frac{f'(x)}{g'(x)} . \qquad (20)
```

利用 Theorem 7.38，我们推得

```math
\lim_{x\to-\infty}\frac{f(x)}{g(x)} = \lim_{t\to0^+}\frac{F(t)}{G(t)} = \lim_{t\to0^+}\frac{F'(t)}{G'(t)} = \lim_{x\to-\infty}\frac{f'(x)}{g'(x)} . \qquad (21)
```

结论由 (20) 与 (21) 推出。$\blacksquare$

---
<!-- ===== 书页 316（PDF 页 32）===== -->
---
<span style="color:#7f8c8d">书页 316 · 第 7 章 Differentiation（微分）· §7.11 续</span>
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定理 7.41、7.42 把洛必达法则从 $0/0$ 一贯推广到两个新战场：极点逃到 $a=\pm\infty$，或分母 $g(x)\to\infty$。第一性原理是「换元把无穷远拉回有限点」：定理 7.41 用代换 $x=-1/t$ 把「$x\to-\infty$」翻译回「$t\to 0^+$」，将无穷原点的问题压缩回原点邻域，从而复用已证的定理 7.38；定理 7.42 则在 $\infty/\infty$ 情形下改用 Cauchy 中值定理，借助 $p<f(x)/g(x)<q$ 的夹逼——本质上就是极限定义的 $\varepsilon$-$\delta$——把结论压进去心邻域。工程视角恰似「把每种异常输入归一化为标准输入」：所谓不定型并非真歧义，而是「零点形如 $0/0$ 时谁主导速率」的标准化；本书把这四种直觉（$0/0$、$\infty/\infty$、$1^\infty$、$0\cdot\infty$）逐一归约到可求导的基础脚手架。跨课程连接：与 CSAPP 把特殊情形归一化到通用路径、Strang 先解标准形再回代同构；命名模板「换元归约到基础情形」可留给以后的级数与积分判据复用。


<span style="color:#2471a3;">**[subsection]**</span> <span style="color:#c0392b">7.11.3 洛必达法则：$\frac{\infty}{\infty}$ 型</span>

<span style="color:#7f8c8d">*（本节为拓展内容 Enrichment section，可略读 May be omitted。）*</span>

当 $x\to a$ 时 $f(x)\to\infty$ 且 $g(x)\to\infty$，我们就得到不定型 $\frac{\infty}{\infty}$。

此时洛必达定理取 Theorem 7.42 中所给出的形式。

不过请注意，我们并不要求在假设中 $f(x)\to\infty$，甚至不要求 $f(x)$ 趋于任何极限。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">定理 7.42</span>
> <span style="color:#7f8c8d;">TBB §7.11, p.316</span>

设 $f$ 与 $g$ 在 $x=a$ 的某个去心邻域（deleted neighborhood）$N$ 上可微。

假设

(i) $\lim_{x\to a}g(x)=\infty$。

(ii) 对每个 $x\in N$，$g'(x)\ne 0$。

(iii) $\lim_{x\to a}f'(x)/g'(x)$ 存在。

则

```math
\lim_{x\to a}\frac{f(x)}{g(x)} = \lim_{x\to a}\frac{f'(x)}{g'(x)} .
```

若 $a=\pm\infty$，或若 $\lim_{x\to a}g(x)=-\infty$，相应的结论仍然成立。

<span style="color:#2471a3;">**[proof]**</span> <span style="color:#c0392b">证明</span>

我们在假设 $\lim_{x\to a}f'(x)/g'(x)$ 存在之下，来证明 Theorem 7.42 的主要部分。

<span style="color:#7f8c8d">*（定理 7.42 的证明续于书页 317。）*</span>


<!-- ===== W17 ===== -->

<span style="color:#7f8c8d">书页 317 · §7.11 洛必达法则</span>

### 定理 7.42 之证明（续）

<span style="color:#2471a3;">**[proof]**</span> ……该极限是有限的。极限为无穷的情形以及各种变式留作习题 7.11.6 与 7.11.7。只需考虑右极限的情形即可，左极限的证明与之类似。

令

```math
L=\lim_{x\to a+}\frac{f'(x)}{g'(x)}.
```

我们将证明：若 $p<L<q$，则存在 $\delta>0$，使得当 $x\in(a,a+\delta)$ 时，有

```math
p<\frac{f(x)}{g(x)}<q.
```

由于 $p$ 与 $q$ 是任意的（只需满足限制 $p<L<q$），我们便能据此得出如所需的结论

```math
\lim_{x\to a+}\frac{f(x)}{g(x)}=L.
```

选取 $r\in(L,q)$。由 (iii) 以及 $L$ 的定义，存在 $\delta_1$，使得当 $x\in(a,a+\delta_1)$ 时，有 $\frac{f'(x)}{g'(x)}<r$。若 $a<x<y<a+\delta_1$，则由定理 7.21，即 Cauchy 形式的中值定理，结合我们的假设 (ii)，可推知存在 $c\in(x,y)$，使得

```math
\frac{f(x)-f(y)}{g(x)-g(y)}=\frac{f'(c)}{g'(c)}<r.
\tag{22}
```

在 (22) 中固定 $y$。由于 $\lim_{x\to a+} g(x)=\infty$，故存在 $\delta_2>0$，使得 $a+\delta_2<y$，并且当 $a<x<a+\delta_2$ 时，有 $g(x)>g(y)$ 且 $g(x)>0$。于是当 $x\in(a,a+\delta_2)$ 时，有

```math
\frac{g(x)-g(y)}{g(x)}>0,
```

因此我们可以在不等式 (22) 的两边同乘 $\frac{g(x)-g(y)}{g(x)}$，得到

```math
\frac{f(x)}{g(x)}<r-r\frac{g(y)}{g(x)}+\frac{f(y)}{g(x)},\quad x\in(a,a+\delta_2).
\tag{23}
```

现在令 $x\to a+$。由假设 (i)，当 $x\to a+$ 时 $g(x)\to\infty$。由于 $r$、$g(y)$ 与 $f(y)$ 均为常数，故 (23) 右端的第二项与第三项趋于零。于是由不等式 $r<q$，存在 $\delta_3\in(0,\delta_2)$，使得当 $a<x<a+\delta_3$ 时，有

```math
\frac{f(x)}{g(x)}<q.
```

同理，我们可找出 $\delta_4>0$，使得当 $a<x<a+\delta_4$ 时，有

```math
\frac{f(x)}{g(x)}>p.
```

若令 $\delta=\min(\delta_3,\delta_4)$，则我们已经证明：当 $x\in(a,a+\delta)$ 时，有

```math
p<\frac{f(x)}{g(x)}<q.
```

由于 $p$ 与 $q$ 是满足 $p<L<q$ 的任意数，故我们的结论成立：

```math
\lim_{x\to a+}\frac{f(x)}{g(x)}=L=\lim_{x\to a+}\frac{f'(x)}{g'(x)}.
\tag{24}
```

<span style="color:#7f8c8d">书页 318 · §7.11 洛必达法则（续）</span>

<span style="color:#2471a3;">**[proof]**</span> ……于是上述结论随之成立。$\blacksquare$

<span style="color:#7f8c8d">> *（本页其余部分为 §7.11 习题区 Exercises 7.11.1–7.11.8，按约定跳过，不翻译不收录。）*</span>

> 本 worker 按规范跳过习题区（习题 7.11.1 至 7.11.8），其中 7.11.6 与 7.11.7 正是要求读者补证定理 7.42 中极限无穷及 $a=\pm\infty$ 或 $\lim_{x\to a} g(x)=-\infty$ 的情形。


<!-- ===== W18 ===== -->

<span style="color:#7f8c8d">书页 319 · §7.12 Taylor Polynomials（泰勒多项式）</span>

<span style="color:#7f8c8d">*（本页页首为 §7.11 L'Hôpital 法则的习题区末尾——习题 7.11.8 的末两小题与 7.11.9、7.11.10，按约定跳过。）*</span>

## §7.12 Taylor Polynomials（泰勒多项式）

<span style="color:#1e8449">*（增补小节（Enrichment section），可略读。）*</span>

设 $f$ 在开区间 $I$ 上连续，且 $c\in I$。常值函数 $g(x)=f(c)$ 在 $x$ 充分接近点 $c$ 时能够很好地逼近 $f$，但在别处却未必能提供良好的近似。

若 $f$ 在 $I$ 上可微，那么由中值定理（Theorem 7.20）可知：对每个 $x\in I$（$x\ne c$），在 $x$ 与 $c$ 之间都存在 $z$，使得 $f(x)=f(c)+f'(z)(x-c)$。

表达式 $R_0(x)=f'(z)(x-c)=f(x)-f(c)$ 给出了用常值函数 $P_0(x)=f(c)$ 逼近函数 $f$ 时所产生误差的大小。我们可以把这视为用零次多项式（zero-degree polynomial）进行的逼近。

一般而言，我们并不指望常值函数能成为给定连续函数的良好逼近。但我们对泰勒级数（Taylor series，初等微积分课程中已有介绍）的了解提示我们：只要一个函数可微次数足够多，它就能被次数足够高的多项式很好地逼近。

假设我们想用一个 $n$ 次多项式 $P_n$ 来逼近 $f$。为了使多项式 $P_n$ 有机会在点 $c$ 的某个邻域内很好地逼近 $f$，我们应当要求

```math
P_n(c)=f(c),\quad P_n'(c)=f'(c),\quad \ldots,\quad P_n^{(n)}(c)=f^{(n)}(c).
```

在这种情况下，我们至少保证 $P_n$ 以正确的取值、正确的变化率等作为"起点"，从而有机会在 $c$ 的某个邻域 $I$ 内很好地逼近 $f$。然而检验标准是这样的：写出 $f(x)=P_n(x)+R_n(x)$，当 $x\in I$ 时，这个"误差"或"余项"（remainder）$R_n(x)$ 是否确实很小呢？

为了回答这类问题，为误差项 $R_n(x)$ 找到便于使用的形式将会很有用。我们将给出余项的两种形式，其中第一种归功于...

<span style="color:#7f8c8d">（本页到此为止，内容续至下页。）</span>

<span style="color:#7f8c8d">书页 320 · §7.12 泰勒多项式（续） · 第 7 章 Differentiation（微分）</span>
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定理 7.43 陈说的背后是全书最漂亮的一种「造多项式再压缩误差」策略：要求 $n$ 次多项式 $P_n$ 在点 $c$ 处与前 $n$ 阶导数全部对齐，于是只需管控余项 $R_n=f-P_n$ 的大小。证明骨架是命名模板「Rolle 定理递归定位」：先取常数 $M$ 使 $g(t)=f(t)-P_n(t)-M(t-c)^{n+1}$ 在 $x$ 处也取零；因端点 $c$、$x$ 处 $g$ 皆零，对 $g$ 用 Rolle 得 $z_1$ 使 $g'(z_1)=0$，再把 Rolle 套到 $g'$ 上得 $g''(z_2)=0$，如此反复 $n+1$ 次，最终敲出 $g^{(n+1)}(z)=0$，即 $f^{(n+1)}(z)=(n+1)!M$。🎥 Colding 在 V16 里一句话点破本质：「它就是反复套用 Rolle 定理（特殊情形套两次）……其实你可以套用 k 次，套 k 次你就得到 k 阶泰勒展开」（原文：it's applying Rolle's theorem twice… you can actually apply Rolle's theorem k times—getting the k Taylor expansion）。当 $n=0$ 时 $M$ 恰回落到普通 MVT：Lagrange 余项是中值定理的 $n$ 次推广；你把它当作「在某个正确取点 z 处求 $n+1$ 阶导」的普适表达式即可。


约瑟夫-路易·拉格朗日（Joseph-Louis Lagrange，1736–1813）于 1797 年得到定理 7.43。他当初是用积分方法来证明这条定理的，而我们这里将给出一个基于中值定理的、流行且更现代的证明。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">**定理 7.43（Lagrange，拉格朗日）**</span> 设 $f$ 在开区间 $I$ 上至少具有 $n+1$ 阶导数，且 $c\in I$。令
> <span style="color:#7f8c8d;">TBB §7.12, p.320</span>

```math
P_n(x)=f(c)+f'(c)(x-c)+\frac{f''(c)}{2!}(x-c)^2+\cdots+\frac{f^{(n)}(c)}{n!}(x-c)^n
```

并令 $R_n(x)=f(x)-P_n(x)$。那么对每个 $x\in I$，在 $x$ 与 $c$ 之间存在 $z$（若 $x=c$ 则取 $z=c$），使得

```math
R_n(x)=\frac{f^{(n+1)}(z)}{(n+1)!}(x-c)^{n+1}.
```

<span style="color:#2471a3;">**[proof]**</span> <span style="color:#c0392b">**证明。**</span> 固定 $x\in I$。于是存在某个数 $M$（它当然依赖于 $x$），使得 $f(x)=P_n(x)+M(x-c)^{n+1}$。

我们希望证明：对介于 $x$ 与 $c$ 之间的某个 $z$，有 $M=\dfrac{f^{(n+1)}(z)}{(n+1)!}$。

考虑定义在 $I$ 上的函数 $g$：

```math
g(t)=f(t)-P_n(t)-M(t-c)^{n+1}=R_n(t)-M(t-c)^{n+1}.
```

由于 $P_n$ 是次数至多为 $n$ 的多项式，所以对所有 $t\in I$ 都有 $P_n^{(n+1)}(t)=0$。于是对所有 $t\in I$，有

```math
g^{(n+1)}(t)=f^{(n+1)}(t)-(n+1)!\,M. \tag{25}
```

此外，由于对 $k=1,2,\ldots,n$ 有 $f^{(k)}(c)=P_n^{(k)}(c)$，我们很快得到

```math
g^{(k)}(c)=0,\quad \text{对 } k=0,1,2,\ldots,n.\tag{26}
```

现在假设 $x>c$（$x<c$ 的情形证明类似，$x=c$ 的情形则是显然的）。我们选取 $M$ 的方式使得 $g(x)=0$，并且由 (26) 可知 $g(c)=0$。因此 $g$ 在区间 $[c,x]$ 上满足 Rolle 定理（Rolle's theorem）的全部假设，于是存在点 $z_1\in(c,x)$ 使得 $g'(z_1)=0$。

现在把 Rolle 定理应用于区间 $[c,z_1]$ 上的 $g'$，得到点 $z_2\in(c,z_1)$ 满足 $g''(z_2)=0$。

照此继续，我们反复使用 (26) 与 Rolle 定理，得到点 $z_n\in(c,z_{n-1})$ 满足 $g^{(n)}(z_n)=0$。最后，我们把 Rolle 定理应用于区间 $[c,z_n]$ 上的函数 $g^{(n)}$，得到点 $z\in(c,z_n)$ 满足 $g^{(n+1)}(z)=0$。

由 (25) 我们推出 $f^{(n+1)}(z)=(n+1)!\,M$，证明完成。$\blacksquare$

<span style="color:#2471a3;">**[note]**</span> <span style="color:#1e8449">**备注。**</span> 函数 $P_n$ 称为 $f$ 的第 $n$ 个泰勒多项式（$n$th Taylor polynomial）。你会认出 $P_n$ 就是初等微积分中所学泰勒级数的第 $n$ 个部分和（partial sum）。（亦参见 Chapter 10，续于书页 321。）

<span style="color:#7f8c8d">（本页到此为止，内容续至下页。）</span>


<!-- ===== W19 ===== -->

---
<!-- ===== 书页 321（PDF 页 37）===== -->
---
<span style="color:#7f8c8d">书页 321 · §7.12 Taylor Polynomials（泰勒多项式·续）</span>
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 例 7.44 展示 Lagrange 余项最常被使用的场景——给误差一个只依赖「界」而不依赖「到底选中哪个 $z$」的上限。对 $f(x)=\sin x$ 在 $c=0$ 处展开至三阶，得 $P_3(x)=x-x^3/6$，余项 $R_3(x)=\frac{\sin z}{4!}x^4$ 中那个神秘的 $z$ 我们并不知道，但 $|\sin z|\le 1$ 对一切 $z$ 成立，于是立即得到 $|R_3(x)|\le a^4/24$，逼近误差被牢牢锁住。第一性原理是「不知道精确定位没关系，只要知道 $f^{(n+1)}$ 的整体上界」——这是控误差（bound the error）而非追误差的工程思维，正如 CSAPP 只在乎最坏情形复杂度、不在乎具体输入。🎥 Colding 在 V17 里把它讲得最抓人：「泰勒多项式说到底只是多项式，求值很容易，剩下的误差就被这个余项界定住」（原文：that's, after all, just a polynomial, so that's easy to evaluate… you get within this remainder term of the right answer）。跨课程上，$|R_3|\le a^4/24$ 是大 O 直觉的严格版模板「上界控余项」；当 $a$ 增大，更高次多项式的阶乘衰减 $|x^{n+1}|/(n+1)!$ 能补救精度，指向泰勒级数「余项趋于零才收敛」的方向。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定理 7.45 给出余项的积分型形式：$R_n(x)=\frac{1}{n!}\int_c^x f^{(n+1)}(t)(x-t)^n\,dt$。它与 Lagrange 形式各有千秋——Lagrange 把误差压在一个看不见的 $z$ 上，积分形式则把误差摊成一条连续累加。第一性原理是：积分型余项正是「反复运用微积分基本定理」的产物——对 $R_n$ 每次求导还原一步，其骨髓就是 FTC 的「积分还原导数」。它的出现强烈预告第 8 章：一旦积分机器就位，泰勒余项就能用积分累计误差表达，而不再需要那个神秘的 $z$。教学上请把它当作承前启后的公告板：教材特地「不加证明地陈述」并假定你已熟悉积分（习题侧更暗示读者到第 8 章可自行完成证明）。🎥 同讲 Colding 转到积分时预告：「这就是所谓的 Riemannese，以德国数学家 Riemann 命名积分的定义」（原文：this is what's called Riemannese—after German mathematician Riemann）。跨课程上，权重因子 $1/n!$ 说明高阶项影响随阶数锐减，呼应 6.042J 的组合阶乘直觉；本条可作为正式进入积分前的待办桩。


<span style="color:#7f8c8d">*（承接书页 320 括号内语段补全。）*</span>

……参见第 10 章（Chapter 10）。

函数 $R_n$ 被称为 $f$ 与 $P_n$ 之间的余项（remainder）或误差函数（error function）。

若 $P_n$ 要成为 $f$ 的好的近似，那么 $R_n$ 的绝对值就必须很小。

注意到 $P_n(c)=f(c)$，并且对 $k=0,1,2,\ldots,n$ 有

```math
P_n^{(k)}(c)=f^{(k)}(c).
```

还注意到，中值定理（mean value theorem）正是 Theorem 7.43 在取 $n=0$ 时的特殊情形：在区间 $[c,x]$ 上存在一点 $z$，使得

```math
f(x)-f(c)=f'(z)(x-c).
```

Lagrange 的结果以某一种特定的方式表达了误差项 $R_n$。

它给出了用 $P_n$ 逼近 $f$ 时关于误差的一种认识。

注意，我们并不能得到误差项的精确表达式，因为它是以某个点 $z$ 处的值 $f^{(n+1)}(z)$ 来表示的。

但若我们在所讨论的区间上对函数 $f^{(n+1)}$ 稍有了解，或许就能断言这个误差不会太大。

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">例 7.44</span>
> <span style="color:#7f8c8d;">TBB §7.12, p.321</span>

假设我们要在区间 $[-a,a]$ 上用 $c=0$、次数为 3 的泰勒多项式来逼近函数 $f(x)=\sin x$。

此处

```math
f'(x)=\cos x,\qquad f''(x)=-\sin x,\qquad f'''(x)=-\cos x,\qquad f^{(4)}(x)=\sin x.
```

于是

```math
P_3(x)=\cos(0)\,x-\frac{\sin(0)}{2!}x^2-\frac{\cos(0)}{3!}x^3=x-\frac{x^3}{3!},
```

且

```math
R_3(x)=\frac{\sin z}{4!}x^4,
```

其中某个 $z$ 位于 $[-a,a]$ 之中。

确切误差取决于究竟是哪一个 $z$ 使这一切成立。

但既然对一切 $z$ 都有 $|\sin z|\le 1$，我们便立即得到

```math
|R_3(x)|\le a^4/4! = a^4/24,
```

因此 $P_3$ 在区间 $[-a,a]$ 上对 $f$ 的逼近精度在 $a^4/24$ 之内。

当 $a$ 较小时，这个逼近对眼前的目的应当已经足够。

当 $a$ 较大时，更高次的多项式能够产出所需的精度，因为

```math
|R_n(x)|\le \frac{|x^{n+1}|}{(n+1)!}.
```

$\blacksquare$

误差项 $R_n$ 的其他各种形式也是有用的。

积分型（integral form）就是其中之一。

我们不加证明地陈述这一形式。

我们假定你已熟悉微积分课程中所学的积分。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">定理 7.45（积分型余项 Integral Form of Remainder）</span>
> <span style="color:#7f8c8d;">TBB §7.12, p.321</span>

设函数 $f$ 在开区间 $I$ 上具有至少 $n+1$ 阶导数，且 $f^{(n+1)}$ 在 $I$ 所含的每一个闭区间上都是 Riemann 可积（Riemann integrable）的。

设 $c\in I$。

则对一切 $x\in I$，

```math
R_n(x)=\frac{1}{n!}\int_c^x f^{(n+1)}(t)(x-t)^n\,dt .
```

---
<!-- ===== 书页 322（PDF 页 38）===== -->
---
<span style="color:#7f8c8d">书页 322 · 第 7 章 Differentiation（微分）· §7.12 收尾与 §7.13 过渡</span>

我们将在第 10 章研究 Taylor 级数（Taylor series）时再次见到这一形式的余项。

<span style="color:#7f8c8d">*（本页其余部分为 §7.12 的 Exercises 习题区：习题 7.12.1–7.12.6，按约定跳过。）*</span>

<span style="color:#7f8c8d">*（§7.13 Challenging Problems for Chapter 7 第 7 章挑战题自此起整区跳过，详见书页 323–324。）*</span>


<!-- ===== W20 ===== -->

> <span style="color:#7f8c8d;font-style:italic;">书页 323–324：§7.13 Challenging Problems for Chapter 7（第 7 章挑战性习题区），按约定整页跳过、不翻译。</span>


<!-- ===== W21 ===== -->

> <span style="color:#7f8c8d;font-style:italic;">书页 325–326：第 7 章 NOTES（习题提示区），按约定整页跳过、不翻译。</span>


<!-- ===== W22 ===== -->

> <span style="color:#7f8c8d;font-style:italic;">书页 327–328：第 7 章 NOTES（习题提示区），按约定整页跳过、不翻译。</span>


<!-- ===== W23 ===== -->

<span style="color:#7f8c8d">书页 329 · NOTES</span>

<span style="color:#7f8c8d">*（书页 329 为第 7 章 NOTES 习题提示区，按约定整页跳过。）*</span>

<span style="color:#7f8c8d">书页 330 · NOTES</span>

<span style="color:#7f8c8d">*（书页 330 为第 7 章 NOTES 习题提示区，按约定整页跳过。）*</span>


<!-- ===== W24 ===== -->

<span style="color:#7f8c8d">书页 331 · 第 8 章 章题页 + §8.1 Introduction（导言）</span>
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 两种积分共用一个符号 ∫，却分属两套含义——不定积分是「反导数」（输出一族函数，如 $\int x^3\,dx = x^4/4 + C$），定积分是「面积极限」（输出一个数，如 $\int_1^2 x^3\,dx = 15/4$）。细究对象完全不同：前者给函数、后者给数，只因记号、术语几乎一致，二者才被搅成一团。这正是 Cauchy 要修的历史性的「分」：此前许多十八世纪数学家直接把定积分定义成原函数，对这个认知分裂不加分辨。历史注：1823 年，Cauchy 在巴黎综合理工的《无穷小演算课程概要》（Résumé des leçons sur le calcul infinitésimal）中首次把定积分定义为「和的极限」，完全独立于反导数概念，从而为严格化铺路。这恰好呼应本节原文点破的「归功于 Newton」：Newton 的功绩是发现面积可由反导数算出，而 Cauchy 的功绩恰是反手把定积分从反导数手里「赎」回来——两位大师各自补上了链条的一半。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 穷竭法并非 Cauchy 首创，源头可溯至古希腊。Antiphon 与 Eudoxus 最早用它讨论圆面积；Archimedes 则用穷竭法精确算出抛物线弓形的面积恰为内接三角形面积的 4/3，堪称古代分析的巅峰。第一性原理一句话：全部积分理论的 DNA 就是「用已知去逼近未知」——把矩形面积（已知）叠加起来，逼近曲边图形的面积（未知），再取极限。🎥 讲者 Colding 在引入 Riemann 积分时把这个原理讲得极凝练：「你唯一有把握的，就是矩形的面积等于长乘宽……那就是我们手里仅有的东西」（原文：The only thing that you know for sure is—if you take a right angle—then you know that the area here is d times e. That's the only thing we have.）。他紧接着反问「那我们怎么定义曲线下方的面积?」——先确立唯一已知物，再设法用它去度量未知，这正是 Cauchy 借希腊几何重建定积分的同一思路。跨课程连接：这与 CSAPP 的「离散化」同源——计算机只能处理有限个矩形方块，把连续曲线切成 n 块矩形再求和，就是数值积分（矩形法、梯形法等）的原型；本节稍后正是这块脚手架的严格升级版。


### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Chapter 8 The Integral（第 8 章 积分）</span>

> <span style="color:#1e8449;">**[note] Note（序言引文）**</span>

为一门短课程，可就 Cauchy 所构想的意义引入积分，并将 Riemann 积分的内容省略或压缩。

对 Riemann 积分的研究引入了某些课程未必需要的新技巧与新思想。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">8.1 Introduction（导言）</span>

微积分学生要学习两种过程，而这两者都被称为「积分」（integration）。

下面这两个例子应当很熟悉：

```math
\int x^3\,dx = x^4/4 + C
```

以及

```math
\int_1^2 x^3\,dx = 2^4/4 - 1^4/4 = 16/4 - 1/4 = 15/4.
```

前者称为不定积分（indefinite integral）或原函数（antiderivative），后者称为定积分（definite integral）。

几乎相同的记号、术语与计算方法的使用，很容易让人混淆两者背后的含义（underlying meaning）。

许多微积分学生都会难以作出这种区分。

事实上，即便对许多十八世纪的数学家而言，这两种不同的过程也没有被多加区分。

认识到"计算面积可以通过求原函数来完成"是一项重大发现。

这一发现归于 Newton，但在更早作者的思考中也能找到沿着这条思路的模糊观念。

对这些数学家来说，定积分是直接用原函数来定义的。

正如 Cauchy 所认识到的那样，这对严格理论的发展是极为不幸的。

他清楚地看到，至关重要的是把定积分的含义与不定积分分离开来，并给它一个独立于后者之外的精确定义。

为此他转向希腊人的几何，后者很久以前就描述过一种计算由曲线围成的区域面积的方法。

这种被称作穷竭法（method of exhaustion）的方法，涉及计算若干更简单图形（正方形、三角形、矩形）的面积，以逼近该区域的面积。

我们回到那个例子：

```math
\int_1^2 x^3\,dx
```

把它解释为一种面积。

该区域左右由直线 $x=1$ 与 $x=2$ 界定，下方由直线 $y=0$ 界定，上方由曲线 $y=x^3$ 界定。

（见图 8.1。）

<span style="color:#7f8c8d">*（本句跨页，其余部分续于书页 332。）*</span>
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 用穷竭法把区间 [1,2] 切成 n 个等长子区间（每个长 1/n），取右端点为矩形高度得到上估计，取左端点得下估计——但 Cauchy 走得更远：允许在每个子区间内任意选取 ξₖ，只要上、下估计都收敛到同一个数，积分就与「抽样点怎么选」无关。关键洞察是 $f(x)=x^3$ 的连续性保证这些极限必然一致。第一性原理：连续性在这里绝非装饰，而是「曲线上没有裂缝」的保证——无论从上方、下方还是在内部任取一点逼近，矩形堆叠的总面积都被逼向同一个值。跨课程连接：这正是数值积分里「采样方式五花八门、极限值由函数本身唯一决定」的严格表述；对计算机而言，「任取 ξₖ」等价于「只要触到的小区间足够细，离散化误差就被界住」。一个自检：若 f 在 [1,2] 上某处有跳跃间断，上估计与下估计还会趋同吗？答案是不会——这正是后续转向上/下和、乃至进阶到 Lebesgue 判据的伏笔。


---

<span style="color:#7f8c8d">书页 332 · §8.1 Introduction（导言，续）</span>


<span style="color:#2471a3;">**[figure]**</span> <span style="color:#2471a3">Figure 8.1（图 8.1）：由 $x=1$、$x=2$、$y=x^3$ 与 $y=0$ 界定的区域。</span>

图中标注的 $x=1$、$x=2$、$y=x^3$、$y=0$ 与顶点 $8$（曲线在 $x=2$ 处的高度）标识出该区域的边界。

<span style="color:#2471a3;">**[figure]**</span> <span style="color:#2471a3">Figure 8.2（图 8.2）：穷竭法（$n=4$）。</span>

图中显示的 $n=4$ 个矩形说明了区间以至点 $1,2$ 的划分。

利用穷竭法，我们可以把区间 $[1,2]$ 划分成 $n$ 个大小相等的子区间，每个长度为 $1/n$，从而把这个图形放进一个矩形集合之内。

这意味着选取下列诸点：

```math
1,\; 1+1/n,\; 1+2/n,\; \dots,\; 1+(n-1)/n
```

并构造矩形，矩形的高度由右端点（right hand endpoint）确定。

这些矩形的总面积超过真实面积，且精确地等于

```math
\sum_{k=1}^{n}\,(1+k/n)^3\,(1/n).
```

穷竭法也要求一个下估计，该区域的真实面积必须大于

```math
\sum_{k=1}^{n}\,(1+(k-1)/n)^3\,(1/n).
```

（关于 $n=4$ 的图示见图 8.2。）

穷竭法要求我们说明：当 $n$ 增大时，上估计与下估计这两个近似值趋向同一个数。

由于函数 $f(x)=x^3$ 的连续性，Cauchy 看出这些极限必定相同。

不仅如此，在区间 $[1+(k-1)/n,\;1+k/n]$ 中任意选取的点 $\xi_k$

<span style="color:#7f8c8d">*（本句跨页，其余部分续于书页 333。）*</span>
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 本页给定积分的地基铺上两块基石：划分（partition）与 Riemann 和。划分把 [a,b] 切成若干互不重叠的子区间，各子区间是否等长并不重要，重要的是随细化它们都「变得很小」——这是与穷竭法「等分」截然不同的地方，也是理论得以覆盖任意连续函数的关键。第一性原理：把「整段求和」这件无法一步完成的事，归约为「把区间越分越细、每块取一个代表值、再累加」，正是 divide-and-conquer。一处命运的反讽值得记下：式 (1) 的求和明明由 Cauchy 首创，却因 Riemann（晚得多）用它定义自己的积分而被冠名「Riemann 和」。原文那句「计算积分的容易 vs 意义靠更难的这条路」极其关键：$\int_1^2 x^3\,dx = 15/4$ 用微积分基本定理一算即得，但「这个等式到底意味着什么」必须回到 Riemann 和的极限才能说清——这种「先意义、后算法」的顺序，正是理论分析区别于计算课程的分水岭。



<!-- ===== W25 ===== -->

<span style="color:#7f8c8d">书页 333 · §8.1 结尾（穷竭法·续）+ §8.2 Cauchy's First Method（Cauchy 第一方法）</span>

<span style="color:#7f8c8d">*（本页开头承接上页 §8.1 关于极限的讨论，续写"分割求和"的思路。）*</span>

（接上页）它理应具有这样的性质：极限

```math
\lim_{n\to\infty}\sum_{k=1}^{n}\xi_k^{3}\cdot\frac{1}{n}
```

要存在。

这一方法大量借鉴了古希腊人的思想（borrowed heavily from the Greeks），能够对任何连续函数奏效，从而给 Cauchy 提供了一条途径，为任意在区间 $[a,b]$ 上连续的函数 $f$ 定义积分

```math
\int_a^b f(x)\,dx
```

而丝毫不必借助导数或原函数（antiderivative）的概念。

这里的关键成分，首先是借助一列有限个分点

```math
a = x_0 < x_1 < x_2 < x_3 < \cdots < x_{n-1} < x_n = b
```

把区间 $[a,b]$ 划分开。

从而形成一列互不重叠的子区间，这样的子区间族被称作 $[a,b]$ 的一个划分（partition）：

```math
[x_0,x_1],\ [x_1,x_2],\ \dots,\ [x_{n-1},x_n],
```

（各子区间是否等长并不重要，重要的是它们都要变得很小）。

然后我们关于这一划分构造和式

```math
\sum_{k=1}^{n}f(\xi_k)(x_k-x_{k-1}) \qquad (1)
```

对 $\xi_k$ 的选取，唯一的约束在于其中每一个都要取自划分中相应的区间 $[x_{k-1},x_k]$ 内；这些点常被称作关联点（associated points）。

命运一个不凑巧的安排是：那些源自 Cauchy 的和式 (1)，却因 Riemann 后来（晚得多）在定义其积分时使用了它们，而被冠以 Riemann 和（Riemann sums）之名。

在本章中，我们从 Cauchy 的积分方法出发，再逐步过渡到 Riemann 的积分。

你需要始终把握的重点是：这一理论以一种与微积分课程中"计算积分"截然不同的方式发展起来，为各类函数的积分逐步赋予含义。

用熟悉的方式算出 $\int_1^2 x^3\,dx = 15/4$，比视作 Riemann 和的极限要容易得多；但这一等式真正的含义，却必须借助这条更困难的方式才能恰当地给出。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">8.2 Cauchy's First Method（Cauchy 第一方法）</span>

Cauchy 定义积分时的首要目标，是为连续函数（continuous function）的积分给出含义。

积分被定义为 Riemann 和的极限（limit of Riemann sums）。

在这样的定义成立之前，我们必须先证明该极限确实存在。

因此，第一步就是证明如下的定理。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 8.1（Cauchy 定理）</span>
> <span style="color:#7f8c8d;">TBB §8.2, p.333</span>

设 $f$ 是区间 $[a,b]$ 上的连续函数。

于是存在一个数 $I$，称为 $f$ 在 $[a,b]$ 上的定积分（definite integral），使得对每个 $\varepsilon>0$，都存在一个 $\delta>0$，满足

```math
\left|\sum_{k=1}^{n}f(\xi_k)(x_k-x_{k-1}) - I\right|<\varepsilon
```

<span style="color:#7f8c8d">*定理陈述跨页，其余部分续于书页 334。*</span>
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 证明进入核心：对每个划分 π 定义上和 M(π)（用每块子区间内函数最大值的矩形堆出）与下和 m(π)（用最小值堆出），而任意 Riemann 和必夹在二者之间。要证积分存在，只需证明随划分变细，上和与下和的差趋于 0。一致连续（定理 5.48）在此是命门：连续函数在闭区间上一致连续，意味着能用同一个 δ 同时控制整条曲线——只要每个子区间短于 δ(ε)，各块内的 max−min 便小于 ε/(b−a)，于是对应划分的 M(π)−m(π)<ε。第一性原理：一致连续把「每点局部的小抖动」升级为「全区间步调一致的小抖动」，这正是夹逼得以成功的保证。命名证明策略模板「夹逼+一致连续出极限」：上、下和夹住目标，一致连续迫使缝隙趋于 0，积分值由此被唯一锁定。🎥 Colding 在课上用同款语言定义 Riemann 可积：「若下和等于上和，那么 Riemann 积分就是这个公共值」（原文：if the lower sum is equal to the upper sum… then this is just this common value.），并预告「如果 f 连续，二者就相等」（if f is continuous, then they're equal）——TBB 在本页证明的正是这句话。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 本条只画路线图，不展开细节。定理 8.1 证明的收尾依赖一个技术环节：向划分添加分点时，上和不会增大、下和不会减小，于是 {M(πₙ)} 单调不增、{m(πₙ)} 单调不减，再借定理 5.48 的一致连续保证二者被同一个数夹住——这正是你在第 7 章反复练过的「单调有界收敛」的又一次复现，只不过对象从数列换成了划分序列。而且这座「Cauchy 第一方法」只是第 8 章的开端：后续同样的上、下和机器会把积分逐步推广到逐段连续、乃至带跳跃间断的函数，从而过渡到 Riemann 可积性判据；§8.5–§8.8 更将走向 Lebesgue 判据，给出「一个函数究竟何时可积」的本质刻画（Riemann 可积当且仅当它的不连续点构成一个零测集）。跨课程视角：这三步是从「处处光滑」到「容忍少量坏点」的递进，与离散数学把「总能成立」放宽到「几乎处处成立」的思维方式一脉相承。现在只需记住：连续⇒可积只是第一站，后面还有更广阔的领土在等你。


---

<span style="color:#7f8c8d">书页 334 · §8.2 续（Theorem 8.1 陈述收尾 + Definition 8.2 + 定理 8.1 的证明开头）</span>

<span style="color:#7f8c8d">*（延续书页 333 的定理陈述。）*</span>

（接上页）只要 $[x_0,x_1],\ [x_1,x_2],\ \dots,\ [x_{n-1},x_n]$ 是区间 $[a,b]$ 的一个划分，且各个子区间长度都小于 $\delta$，并且每个 $\xi_k$ 都是区间 $[x_{k-1},x_k]$ 中的点。

一旦该定理得证，我们便可以把连续函数的定积分安全地定义为定理所保证的那个数 $I$。

概括地说，我们说积分被定义为 Riemann 和 (1) 的极限。

### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">Definition 8.2（定义 8.2）</span>
> <span style="color:#7f8c8d;">TBB §8.2, p.334</span>

设 $f$ 是区间 $[a,b]$ 上的连续函数。

于是我们定义

```math
\int_a^b f(x)\,dx
```

为定理 8.1 中证明其存在性的那个数 $I$。

现在我们必须证明定理 8.1。

### <span style="color:#2471a3;">**[proof]**</span> <span style="color:#c0392b">证明</span>

对区间 $[a,b]$ 的任意一个特定划分（我们称之为 $\pi$）

```math
[x_0,x_1],\ [x_1,x_2],\ \dots,\ [x_{n-1},x_n]
```

写

```math
M(\pi)=\sum_{k=1}^{n}\max\{f(x):x\in[x_{k-1},x_k]\}(x_k-x_{k-1})
```

以及

```math
m(\pi)=\sum_{k=1}^{n}\min\{f(x):x\in[x_{k-1},x_k]\}(x_k-x_{k-1}).
```

这里的 $M(\pi)$ 与 $m(\pi)$ 都依赖于划分 $\pi$，它们分别被称为该划分的上和（upper sum）与下和（lower sum）。

注意，关于这一划分的任意 Riemann 和，必定介于下和与上和之间。

由于 $f$ 在 $[a,b]$ 上连续，它在 $[a,b]$ 上还是一致连续（uniformly continuous）的（定理 5.48）。

因此，对每个 $\varepsilon>0$，都存在一个依赖于 $\varepsilon$ 的 $\delta>0$，使得当 $|x-y|<\delta$ 时，有

```math
|f(x)-f(y)|<\frac{\varepsilon}{b-a}.
```

由于对许多不同的 $\varepsilon$ 我们都需要去找不同的 $\delta$，不妨把它写成 $\delta(\varepsilon)$。

于是，若我们所用的划分具有"每个子区间都短于 $\delta(\varepsilon)$"的性质，则必有

```math
\max\{f(x):x\in[x_{k-1},x_k]\}-\min\{f(x):x\in[x_{k-1},x_k]\}<\frac{\varepsilon}{b-a}.
```

由此推出，对这样的划分有 $0\le M(\pi)-m(\pi)<\varepsilon$。

选取一个划分序列 $\{\pi_n\}$，其中每一个都包含其前一个划分的全部点，并且第 $n$ 个划分 $\pi_n$ 中的每个子区间都短于 $\delta(1/n)$。

若用 $M(\pi_n)$ 与 $m(\pi_n)$ 表示我们这一划分序列中第 $n$ 个划分所对应的和，那么就有

```math
0\le M(\pi_n)-m(\pi_n)<1/n.
```

还有一点技术性的细节需要提出。

当我们向一个划分添加分点时，上和不可能增大，下和也不可能减小。

因此 $M(\pi_n)\ge M(\pi_{n+1})$，……

<span style="color:#7f8c8d">*（定理 8.1 的证明尚未结束，其余部分续于后续书页。）*</span>
