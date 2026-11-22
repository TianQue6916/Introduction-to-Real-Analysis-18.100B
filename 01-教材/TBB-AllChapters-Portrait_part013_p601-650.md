# <span style="color:#c0392b;">Elementary Real Analysis（初等实分析）</span>

> <span style="color:#7f8c8d;">行内双语翻译 · Part013（书页 585–634）</span>
> <span style="color:#7f8c8d;">范围：第 13 章 Metric Spaces（度量空间）§13.9–§13.15（压缩映射应用、Picard 定理、紧致性、Arzelà-Ascoli、Baire 纲定理、无处可微函数、Cantor 集）</span>
> <span style="color:#7f8c8d;">源文件：TBB-AllChapters-Portrait_part013_p601-650.pdf（书页 = PDF 页 + 584）</span>
> <span style="color:#7f8c8d;">Second Edition (2008) · Brian S. Thomson, Judith B. Bruckner, Andrew M. Bruckner</span>
> <span style="color:#7f8c8d;">**格式：** 中文主体 + `English term（中文翻译）` 嵌入 · 深红标题 · 蓝色标签 · fenced math block · 无英文原句</span>
> <span style="color:#7f8c8d;">**习题区**（各节 Exercises、挑战性习题 §13.15、Notes 提示区 p.630–634 等）按约定跳过不收录</span>

---



<!-- ===== W1 ===== -->

<span style="color:#7f8c8d">书页 585 · 第 13 章 §13.9 Contraction Maps（压缩映射）收尾</span>

图 **Figure 13.5**：方程 $\cos x = x$ 的近似求解。<span style="color:#7f8c8d">（注：图中绘制的）“螺旋”曲线不断趋近 $y=\cos x$ 与 $y=x$ 两者图像的交点。</span>

并且我们已经确立了该序列是 Cauchy 序列（Cauchy sequence）。既然 $X$ 是完备的，于是存在 $x\in X$ 使得 $x_n\to x$。由引理 13.73（Lemma 13.73）可知，这个点 $x$ 正是映射 $A$ 的一个不动点（fixed point）。而其唯一性（uniqueness）已在引理 13.72 中给出。$\square$

观察可知，定理 13.75（Theorem 13.75）的证明同时还提供了近似求解形如 $A(x)=x$ 的方程的一种实用方法。这一方法通常被称作逐次逼近法（method of successive approximations）。

我们可以选取 $x_0$ 为 $X$ 中的任意一点。于是序列 $\{A^n(x_0)\}$ 将收敛到方程 $A(x)=x$ 的唯一解。事实上，不等式 (10) 表明这种收敛的速度与某个几何级数（geometric progression）$\{C\alpha^n\}$ 一样快。

> <span style="color:#7f8c8d;">TBB §13.9, p.585</span>

<span style="color:#2471a3;">**[example]**</span> **例 13.76**：让我们求解方程 $\cos x = x$。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 课文说迭代相当迅速地逼近 $0.73908513$，但“迅速”究竟是几步？在没有给数量级之前，这只是一个心理安慰。用第一性原理把它拆开：把误差的演化写成递推，而不是盯着 $x_n$ 本身。设 $x_*$ 是不动点，即 $x_*=\cos x_*$，定义误差 $e_n=x_n-x_*$。由中值定理（mean value theorem），存在 $\xi_n$ 夹在 $x_n$ 与 $x_*$ 之间，使得 $e_{n+1}=\cos x_n-\cos x_*=\cos'(\xi_n)\,e_n=-\sin(\xi_n)\,e_n.$ 这里的关键不是 $\xi_n$ 具体是谁，而是它永远落在 $x_n$ 与 $x_*$ 之间，所以当 $x_n$ 已接近 $x_*$ 时，$\cos'(\xi_n)\approx\cos'(x_*)=-\sin(x_*)\approx-0.674$。于是每走一步，误差的绝对值大约被乘上 $0.674$。这正是压缩映射误差按几何级数衰减的直观版本：下一代的误差是上一代误差的一个固定比例，而不是“碰运气地变小”。它对应定理 13.75 证明中的不等式 (10)： $d(A^n(x_0),x)\le\frac{\alpha^n}{1-\alpha}\,d(x_0,A(x_0)),$ 其中 $\alpha$ 是压缩因子。注意这个公式里的 $\alpha^n$ 才是主角，前面的 $1/(1-\alpha)$ 只是把初始距离 $d(x_0,A(x_0))$ 放大成一个一次性常数，不影响衰减速度的数量级。
>
> 这种“每步误差乘一个小于 $1$ 的常数”的收敛，数值分析里叫线性收敛（linear convergence），那个常数 $\alpha$ 叫收敛比（convergence ratio）。命名模板要记住：这里的“线性”不是指误差是 $n$ 的线性函数，而是指误差的指数（对数）随步数线性下降——把 $e_n\approx\alpha^n e_0$ 两边取对数得 $\ln|e_n|\approx n\ln\alpha+\ln|e_0|$，对数误差是步数 $n$ 的一次函数。$\alpha$ 越接近 $0$，$\ln\alpha$ 越负，直线越陡，收敛越快；$\alpha$ 越接近 $1$，$\ln\alpha$ 越接近 $0$，直线越平，收敛越慢；$\alpha=1$ 时直线水平，误差不再下降，就完全不收敛了。这个“对数误差—步数”的图像，比任何公式都更直观，日后见到“线性收敛”四个字，脑中应浮现这条斜率为负的直线。
>
> 再把停机判据也算出来。若初始误差为 $e_0$、目标精度为 $\varepsilon$，令 $e_0\,\alpha^n\approx\varepsilon$，取对数解得 $n\approx\frac{\ln(\varepsilon/e_0)}{\ln\alpha}.$ 注意 $\ln\alpha<0$（因为 $0<\alpha<1$），而 $\varepsilon\lt e_0$ 时 $\ln(\varepsilon/e_0)$ 也为负，所以分子分母同号，$n$ 为正。这个“负负得正”不是细节，它提醒你：精度要求越苛刻，$\varepsilon/e_0$ 越小，分子绝对值越大，步数越多；收敛比越接近 $1$，分母绝对值越小，步数爆炸。代入具体数：从 $x_0=1$ 出发，$e_0\approx 1-0.73908513\approx0.26$，$\alpha=0.674$，$\varepsilon=10^{-7}$，则 $n\approx\frac{\ln(3.85\times10^{-7})}{\ln0.674}\approx\frac{-14.77}{-0.394}\approx37.5.$ 于是“相当迅速”的精确含义是：三十来次按键后落定到六七位有效数字。若目标精度放宽到 $10^{-3}$，$n$ 立刻降到大约 $15$ 步；若要求双精度的 $10^{-16}$，也就一百步上下——这就是几何级数收缩的力量，步数只随精度要求的对数值增长，而不是随精度本身增长。
>
> 最后把它放进算法复杂度的框架里。这与你 CLRS 里算复杂度是同一件事：迭代算法的每步成本是 $O(1)$（按一次余弦键，或用一次浮点硬件指令），而总迭代次数由收敛比决定。循环不变量（loop invariant）的语言在这里同样适用：每一步结束后，误差满足 $|e_{n+1}|\le\alpha|e_n|$，这个不等式在循环的每次迭代前都成立，因此归纳到底便得到 $|e_n|\le\alpha^n|e_0|$——这正是 6.042J 的归纳法思想：证明一个性质在每步循环后被保持，再推出任意多步后的全局结论。收敛比就是迭代算法的“底数”：底数远小于 $1$，误差指数衰减；底数贴着 $1$，算法慢吞吞地爬。日后凡见误差按几何级数收缩，都可以直接用 $n\approx|\ln(\varepsilon/e_0)|/|\ln\alpha|$ 估算迭代预算，不必真跑完才知道要几步。这套公式的本质是把“算法会不会停、什么时候停”从经验猜测升级为对数计算——先估收敛比，再算总预算，这是你在设计任何迭代程序之前都应该做的第一件事。

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 例 13.76 揭示的是解方程与找不动点这两副面孔其实是同一件事。方程 $\cos x=x$ 没有封闭的代数解，任何三角恒等式也不能直接开出解来；第一性原理给出的出路是：与其正面硬解，不如把方程改写成可以反复执行的操作——输入 $x_0$，重复 $x_{n+1}=\cos x_n$，让误差按固定比例挤到真解。改写之所以可行，是因为 $\cos x=x$ 这个方程本身就在说“$x$ 是余弦函数的不动点”；硬解是静态地求一个数，迭代是动态地让一个过程收敛到这个数，两者目标相同，只是工作方式不同。$|(\cos x)'|=|\sin x|<1$ 正是压缩性的来源：在区间 $[1/2,1]$ 上，$\sin x$ 的最大值为 $\sin1\approx0.84<1$，于是任意两点的距离被缩短至少 $0.84$ 倍。更精细地，若只关心不动点 $x_*\approx0.739$ 附近，导数约为 $-\sin x_*\approx-0.674$，实际收敛更快；但 $\alpha=0.84$ 是覆盖整个区间的保守估计，它保证无论起点怎么取，迭代都收敛且不重不散。这里要区分清楚：$0.84$ 是“在整段区间上绝对安全的压缩因子”，$0.674$ 是“在不动点附近的局部收缩率”，前者保证全局收敛，后者给出实际速度。
>
> 几何上看，这个过程就是著名的蛛网图（cobweb diagram）：从 $(x_0,0)$ 竖直向上碰到曲线 $y=\cos x$，再水平移到对角线 $y=x$，再竖直向上……每一步都像织蛛网一样把点赶向两条线的交点。具体画法值得亲手做一次：取 $x_0=1$，先在 $x$ 轴找到 $x=1$，竖直向上到曲线得到点 $(1,\cos1)$，其纵坐标是 $\cos1\approx0.540$；再水平移到对角线上，得到点 $(\cos1,\cos1)$，横坐标就是下一步的 $x_1$；然后竖直上下、水平左右交替，折线便一步步盘向曲线与对角线的交点。这个图像会直观显示压缩为什么能保证收敛：曲线在对角线附近的斜率绝对值小于 $1$，每次“竖直—水平”的往返就相当于把一段水平距离按斜率比例缩短，网眼一圈圈收紧；若斜率绝对值大于 $1$，往返一次距离被放大，网眼越张越大、迭代发散。蛛网图的价值在于，它把“中值定理保证误差缩小”这条代数论证变成了可以看见的几何事实。
>
> 把这个不动点迭代放进你已有的算法工具箱里对比，会看得更清楚。二分法（bisection）只要求 $f$ 连续且在端点变号：设 $f(x)=\cos x-x$，在 $[0,1]$ 上 $f(0)=1>0$、$f(1)=\cos1-1\approx-0.460<0$，于是中点 $0.5$ 处 $f(0.5)\approx0.378>0$，根必在 $[0.5,1]$，每次砍半。它也是线性收敛，收敛比 $\alpha=\tfrac12$，而且不需要导数信息；但它每步要算一次 $f$ 并判断符号，且只能处理函数穿过零点的方程。不动点迭代要求压缩性（更强的条件），但每步只算一次 $\cos x$，且对方程形式几乎没有要求——把 $x=\cos x$ 两边随便怎么挪都能迭代，只要挪完后的函数是压缩的。至于牛顿法（Newton's method）：解 $\cos x=x$，即 $f(x)=\cos x-x=0$，迭代格式为 $x_{n+1}=x_n-\tfrac{\cos x_n-x_n}{-\sin x_n-1}$。它在好初值下是二次收敛（quadratic convergence），误差按平方级缩小——若第 $n$ 步有 $k$ 位正确数字，下一步大约有 $2k$ 位；但代价是每步要算 $f(x)$ 和 $f'(x)$ 并做一次除法，还要选好初值，否则可能发散或震荡。三种方法的比较正好构成一张“收敛速度 vs 每步成本 vs 适用条件”的权衡表，工程上的经典取舍就是：迭代简单但次数多，与每步昂贵但收敛快。
>
> 选哪种方法，正是 CSAPP 的计算资源观与 CLRS 的复杂度分析交给你判断的问题：先估每步成本与收敛比，再算总预算。CSAPP 教你的是资源视角——每次函数求值都要消耗 CPU 周期、访存带宽，浮点除法与超越函数 $\cos$ 在硬件上的延迟远比一次加减法高，所以“每步便宜”在真实机器上意味着更短的指令序列；CLRS 教你的是把步数与每步成本乘起来算总量。二分法每步一次 $f$ 求值、收敛比 $\tfrac12$，到 $10^{-7}$ 约需 $\log_2(10^7)\approx24$ 步；不动点迭代约 $38$ 步但每步只按一次余弦键；牛顿法可能只要 $5$ 到 $6$ 步，但每步贵得多。三种算法没有绝对优劣，只有“在给定机器与精度要求下，谁的每步成本乘以迭代次数最小”的具体判断——这正是把实分析收敛率翻译成工程预算的动作。
>
> 另一个值得点破的直觉是"为什么迭代方向天然正确"：把 $x=\cos x$ 改写为迭代时，你并没有引入任何额外的猜测，迭代格式本身就编码了方程。第一性原理地看，解方程 $F(x)=0$ 有三种策略：直接求逆（代数方法，往往不存在）、区间收缩（二分，只吃连续性）、以及把方程重排成 $x=T(x)$ 后反复代入（不动点迭代，吃压缩性）。第三种策略的适用范围最广——它不要求 $F$ 单调，不要求零点唯一，只要求你找得到一个压缩的 $T$；而"找得到一个压缩的 $T$"这件事，恰恰等价于"这个方程有某种良态结构"。用 6.042J 的语言说，二分法像归纳地砍半区间（每一步都把不确定区间长度减半，步数与精度成对数关系），不动点迭代像递推地逼近极限（每一步都应用同一个规则，收敛性由规则本身的收缩性保证）——两种都是"把无穷过程组织成可数步骤"的典范，只是收敛的担保来源不同：一个来自区间套定理，一个来自压缩映射定理。日后你在数值分析课里遇到的几乎所有迭代法——Jacobi、Gauss–Seidel、牛顿法、共轭梯度——都能放进"找压缩算子 $T$、验证压缩性、按几何/超线性率收敛"这个统一框架里，而例 13.76 就是这个框架最朴素的第一课。

---

通常的微积分技巧应使你确信存在唯一解，但又有哪种实用方法能够给出近似答案呢？没有任何代数方法或三角恒等式能径直导出解。取而代之，让我们将此问题理解为求函数 $f(x)=\cos x$ 的不动点。

在区间 $[1/2, 1]$ 上，这显然是一个压缩。因此，若我们从任意值 $x_0\in [1/2,1]$ 出发，并循着序列 $x_n=\cos x_{n-1}$ 对 $n=1,2,3,\ldots$ 继续下去，定理 13.75 的证明将保证该序列必收敛到那个不动点。

事实上，这一过程可以在任何计算器上试验：先（比方说）输入数字 $1$，然后反复按下余弦键。你将看到这些数字相当迅速地逼近 $0.73908513$。从图形上观察正在发生的这一切是颇有教益的（参见图 13.5）。$\square$

> <span style="color:#7f8c8d;">TBB §13.9, p.585</span>

<span style="color:#2471a3;">**[example]**</span> **例 13.77**：设 $X=\mathscr{C}[0,1/2]$，一如既往地配备上确界度量（sup metric）$d(f_1,f_2)=\max_{x\in[0,1/2]}|f_1(x)-f_2(x)|$。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 例 13.77 把本章前半的收敛工具全部串了起来：$X=\mathscr{C}[0,1/2]$ 配上确界度量（sup metric）后是完备空间，因为一致收敛的极限函数仍连续——这正是你在第 9 章学一致收敛时埋下的伏笔：逐点收敛不保证连续性，但按 $\|f-g\|_\infty=\sup_{x\in[0,1/2]}|f(x)-g(x)|$ 收敛则保证极限连续，所以 $\mathscr{C}[0,1/2]$ 在这个度量下没有“收敛到外面去”的洞。$A$ 是压缩映射（压缩因子 $\tfrac12$），于是定理 13.75 一次性给出唯一不动点。这里的关键在于压缩因子 $\tfrac12$ 从哪来：$A(f)(x)=\int_0^x f(t)\,dt$，两点 $f,g$ 的距离按确界度量计算，积分上下限区间长 $1/2$，于是 $\|Af-Ag\|_\infty=\sup_x\left|\int_0^x(f-g)\right|\le\sup_x\int_0^x|f-g|\le\|f-g\|_\infty\cdot\frac12,$ 长度 $1/2$ 自动成为压缩因子。
>
> 这里的可复用招式值得命名：积分算子求压缩模板。要估计 $\left|\int_{x_0}^{x}g\right|$，就用基本不等式链 $|\int_{x_0}^{x}g|\le\int_{x_0}^{x}|g|\le\sup|g|\cdot(x-x_0),$ 三步各有一句直觉：绝对值移进积分（三角不等式保证每一步都只可能放大不会缩小）、被积函数换成它在区间上的最大值、积分长度变成区间长度。于是积分号自动贡献一个区间长度作为压缩因子：积分是把函数磨平的运算，每积一次，函数的高频起伏就被长度因子压下去一截。这正是可用脚手架里“$\|g\|_\infty$ 乘以长度界”那句直觉的形式化，也是 CSAPP 数值分析、Strang 数值线代里反复出现的范数控制误差思想的雏形：CSAPP 里浮点舍入误差的界就是“相对误差单位 $\epsilon$ 乘以操作次数”，Strang 里 Jacobi 迭代的误差界就是“谱半径的 $n$ 次方乘以初始误差的范数”——三者都是同一个母题：用一个范数（或相对误差单位）把局部误差抓出来，再乘以一个几何因子，得到全局误差上界。区别在于：CSAPP 的舍入误差是机器强加的，$\epsilon$ 是硬件字长决定的常数；Strang 的谱半径是矩阵迭代的收敛比；而这里的压缩因子来自积分区间长度，是问题本身的几何尺寸。
>
> 更妙的是结论里那个迭代序列 $t,\ \tfrac{t^2}{2},\ \tfrac{t^3}{6},\ldots,\tfrac{t^n}{n!},\ldots$：它正是 $t^n/n!$，是 $e^t$ 幂级数的各项。把逐次逼近法从常数函数 $f\equiv1$ 跑一遍，恰好吐出了 $e^t$ 的泰勒展开——积分方程 $f(x)=\int_0^x f$ 的唯一解是 $f\equiv0$，而逐次逼近的中间产物却在重演 $e^x$ 的级数。这不是巧合：$A^n(1)=\tfrac{x^n}{n!}$，因为 $A$ 每作用一次就把 $x^k/k!$ 变成 $x^{k+1}/(k+1)!$，正好是“积分是微分的逆”的离散版本——逐次逼近在解一个“解为零”的方程时，竟把 $e^x$ 的幂级数一项一项打印出来，然后又在取极限时把这些项全部加回到零。这个过程像一个自举的证明：幂级数本身满足递推，逐次逼近只是让这个递推自己跑起来。
>
> 愿意多看一眼还会发现：零函数并非“看起来唯一”的候选——$\sinh x$、$\cosh x-1$ 等一大堆函数都满足 $f(0)=0$ 且 $f'=f$ 之类与积分方程相关的边界条件，仅凭 $f(0)=0$ 根本无法区分它们。但例 13.77 中唯一性把 $\sinh x$ 这类候选全部锁死：注意 $f(x)=\int_0^x f$ 两边求导得 $f'=f$，通解是 $Ce^x$，代入 $f(0)=0$ 得 $C=0$，所以只有零函数满足整个积分方程；$\sinh x$ 满足 $f''=f$ 而不是 $f'=f$，故根本不在候选之列。这正说明压缩映射定理唯一性三个字的分量：你不需要逐一排除候选者，一个完备空间加上一个压缩条件，就替你把所有候选者判了死刑。这里的论证动作是：先证“至多一个”，再证“至少一个”，合起来就是“恰好一个”——与 6.042J 中“唯一性证明”的标准结构一致。这种由唯一性免去枚举的论证，与你 CLRS 里由循环不变量免去逐例检查是同一个思维动作：不变量告诉你“无论循环跑多少轮，某性质恒成立”，唯一性告诉你“无论候选者有多少个，满足条件的至多一个”；两者都是用一个一次性的形式论证，替代了对无穷多种情况的逐一检查。真正的力量不在于“有一个解”，而在于“解被完全锁定，谁来了都一样”。

---

<span style="color:#7f8c8d">书页 586 · §13.9 续 + 习题区开始</span>

在 $X$ 上定义一个函数 $A$，它由 $(A(f))(x)=g(x)=\int_0^x f(t)\,dt$ 给出，这里 $0\le x\le 1/2$。由于 $g$ 在 $[0,1/2]$ 上连续，故 $g\in X$，从而 $A:X\to X$。

对 $f_1,f_2\in X$，令 $g_1=A(f_1)$，$g_2=A(f_2)$。于是有
```math
\begin{aligned}
d(g_1,g_2)&=\max_{x\in[0,1/2]}\,|g_1(x)-g_2(x)|
=\max_{x\in[0,1/2]}\left|\,\int_0^x [f_1(t)-f_2(t)]\,dt\,\right|\\
&\le \max_{x\in[0,1/2]}\int_0^x |f_1(t)-f_2(t)|\,dt
\le \max_{x\in[0,1/2]} x \cdot \max_{t\in[0,1/2]}|f_1(t)-f_2(t)|\\
&\le \tfrac12\,d(f_1,f_2).
\end{aligned}
```
因此 $A$ 是一个压缩映射（contraction map）。

由定理 13.75 我们可得出：存在唯一的函数 $f\in\mathscr{C}[0,1/2]$ 满足 $A(f)=f$，亦即满足对所有 $x\in[0,1/2]$ 都有 $f(x)=\int_0^x f(t)\,dt$。

由于零函数 $f(x)=0$（对所有 $x\in[0,1/2]$）满足这一方程，而解又唯一，我们看到零函数是唯一解。假若我们没有觉察到这一点，原本也可以尝试逐次逼近法。

例如从 $f(t)=1$ 出发，我们得到序列 $t,\ \tfrac{t^2}{2},\ \tfrac{t^3}{6},\ldots,\tfrac{t^n}{n!},\ldots$，它在空间 $\mathscr{C}[0,1/2]$ 中收敛（即一致收敛）到不动点 $f\equiv 0$。$\square$

在下一节（§13.10）中，我们将会看到定理 13.75 的一系列应用。

<span style="color:#7f8c8d">*（本页余下部分为 §13.9 习题区 Exercises 13.9.1–13.9.4，按约定跳过。）*</span>

<span style="color:#7f8c8d">题 13.9.1 证连续且满足 Lipschitz 条件 $|f(x)-f(y)|\le \alpha|x-y|$（$0<\alpha<1$）的 $f:\mathbb{R}\to\mathbb{R}$ 有唯一不动点；题 13.9.2 考察 $f(x)=x+1/x$ 在选点后迭代的后果、定理证明何处失效；题 13.9.3 证 $\cos x$ 在 $[1/2,1]$ 上是压缩映射但不在 $[0,\pi]$ 上；题 13.9.4 证 $\cos x$ 在 $\mathbb{R}$ 上不是压缩映射但其某次迭代是。</span>


<!-- ===== W2 ===== -->

> <span style="color:#7f8c8d">书页 587 · §13.9 压缩映射（Contraction Maps）· 习题区</span>

<span style="color:#2471a3">**[section]**</span>

# §13.9 压缩映射（Contraction Maps）——第 13.9.5–13.9.12 小节（习题区）

本页全部为 §13.9 一节的课后习题（Exercises 13.9.5–13.9.12），按约定跳过，不翻译、不收录。

> <span style="color:#7f8c8d">*（本页第 13.9.5–13.9.12 为 §13.9 压缩映射一节的习题区，按约定跳过。习题内容覆盖：**13.9.5** 证明度量空间上的压缩映射是连续的；**13.9.6** 说明若不要求 Theorem 13.75 中 $X$ 完备则结论失效；**13.9.7** 以 $f_0=e^x$ 与 $\sin x$ 为初始逼近的连续逼近序列；**13.9.8** 算子 $A(f)(x)=\int_0^x f(t)\,dt$ 的压缩性质与不动点判别；**13.9.9** 估计两个压缩映射不动点之间的距离 $d(a,b)$；**13.9.10** 迭代序列收敛率的估计 $d(A^n(x_0),x)\le \frac{\alpha^n}{1-\alpha}d(x_0,A(x_0))$；**13.9.11** 一族压缩映射 $\{A_n\}$ 的不动点极限；**13.9.12** Hilbert 空间 $\ell_2$ 上映射族的反例。）*</span>

> <span style="color:#7f8c8d">书页 588 · 第 13 章 度量空间（Metric Spaces）</span>

本页起始的第 13.9.13 为 §13.9 习题区之尾，按约定跳过。

> <span style="color:#7f8c8d">*（书页 588 开头的 13.9.13 为 §13.9 习题区的最后一道习题，讨论序列 $\{A_n\}$ 一致收敛时不动点的计算 $a=\lim_{n\to\infty}a_n$，按约定跳过。）*</span>

<span style="color:#2471a3">**[section]**</span>

# §13.10 压缩映射的应用（I）（Applications of Contraction Maps (I)）

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> §13.10 开篇传达的是一个真正的第一性原理动作：把看似各不相干的代数方程 $ax=b$、线性方程组 $Ax=b$、无穷线性方程组、Fredholm integral equation（Fredholm 积分方程）、常微分方程初值问题，全部重写成同一个格式——求算子 $A$ 的不动点 $A(x)=x$。这个动作的机制在于：解方程本质上就是找一个输入 $x$，让它被算子作用一次之后"等于没变"；比如任给方程 $f(x)=0$，只要定义 $A(x)=x+f(x)$，那么 $f(x)=0$ 与 $A(x)=x$ 就完全等价，解方程被翻译成了找不动点。为什么值得这么绕？因为一旦进入这个框架，三个问题被一次性打包解决：存在性（有没有解）、唯一性（解有几个）、近似解（怎么算出来），全部统一交给定理 13.75（Banach fixed point theorem，Banach 不动点定理）管辖。你的工具箱就从"每种方程一个窍门"浓缩成一个通用的 successive approximation（逐次逼近法）：任取初值 $x_0$，迭代 $x_{k+1}=A(x_k)$，定理保证它收敛到唯一不动点。这与你在 CLRS 里反复见到的 reduction（归约）是同一个思维动作：不解决新问题，而是把新问题翻译成已解决问题。归约要求翻译函数保持实例与解之间的对应，这里则要求翻译之后的算子满足压缩三条件；两者共同点是"换一个表示，不换问题的本质"。
>
> 这个框架的输入是固定的三件套。第一，选一个 complete metric space（完备度量空间）当战场，保证每个 Cauchy 列都有极限且极限仍留在战场内；否则迭代序列可能"越来越接近某个不存在于空间里的点"，定理无处发力。第二，验证算子把空间映进自身，保证每步迭代都有定义、序列永不越界。第三，验证算子是 contraction mapping（压缩映射），即存在常数 $\alpha<1$ 使 $d(A(x),A(y))\le \alpha d(x,y)$，保证误差按 $\alpha^k$ 几何衰减。可以把这三步记成模板"战场三件套核对清单"：完备性管极限、自映管定义、压缩管收缩。§13.10 接下来的例 13.78–13.82 就是逐个演示这三件套怎么配齐。也正因如此，这与你学线代时 Strang 反复强调的"把高维问题压成矩阵运算，把不同的力统一到同一个线性框架里求解"一脉相承——Strang 用矩阵统一，这里用不动点统一。区别在于：Strang 的统一发生在代数对象层面（消元、特征值、子空间），这里的统一发生在存在性与构造性层面（解是否存在、是否唯一、迭代是否收敛）。
>
> 但别忘了代价：把方程改写为 $A(x)=x$ 后，$A$ 是否压缩、压缩常数多大，取决于你选取的度量空间；同一个算子换一个度量就可能从压缩变成非压缩。机制在于，压缩常数是距离函数 $d$ 的函数，距离的"刻度"变了，Lipschitz 收缩关系就可能被破坏。一个具体例子：$x=\cos x$ 在闭区间 $[0,1]$ 上，$\cos$ 把区间映进自身，且 $\cos$ 的导数上确界是 $\sin 1\approx 0.84<1$，所以它是压缩；但把战场换成整个 $\mathbb{R}$，$\cos$ 虽然仍 1-Lipschitz，却凑不出任何 $\alpha<1$，压缩性就丢了。这就是 §13.10 反复强调必须明确值域的深层原因，例 13.80、13.81 都在此处留了话头。用 CSAPP 的语言说：你不是在变魔术，而是在挑一个有利的表示来打同一场仗——选对度量空间，就像选对 data structure（数据结构），决定后续一切操作的复杂度。读这一节时请带着这张战场选择的眼镜，你会看到每个例子其实都在回答同一个问题：这场仗，我该把棋盘摆在哪？

---

> <span style="color:#7f8c8d">*（本小节为拓展小节，可省略。）*</span>

分析中的大量问题（a variety of problems in analysis）都涉及对某种方程（equations）的求解。这些方程可以是关于数的，也可以是关于数的 $n$ 元组（$n$-tuples）的，或是关于序列（sequences）、函数（functions）以及各种其他数学对象（mathematical objects）的。通常，这类问题都可以表述成如下形式：我们观察到，某个算子（operator）在求解这一问题的过程中自然而然地出现，并且该问题的一个解恰好可以表示为这个算子的一个不动点（fixed point）。

让我们来看几个例子。在下一节之前，我们暂且不处理它们的解；现在，我们只是把每个问题重新解释为一个不动点问题（fixed point problem）。我们从一个平凡的例子（trivial example）开始，仅以之说明这一方法（approach）。

> <span style="color:#7f8c8d;">TBB §13.10, p.588</span>

<span style="color:#c0392b">**[example]**</span>

**例 13.78：（一个简单的线性方程 A Simple Linear Equation）** 考虑简单线性方程（simple linear equation）
```math
ax = b, \quad (a \neq 0). \tag{12}
```
我们可以把该方程改写为 $x = (1 - a)x + b$。现在考虑算子 $A(x) = (1 - a)x + b$。于是，(12) 的一个解（solution to (12)）恰好就是算子 $A$ 的一个不动点（fixed point）。

> <span style="color:#7f8c8d;">TBB §13.10, p.588</span>

<span style="color:#c0392b">**[example]**</span>

**例 13.79：（线性方程组 Systems of Linear Equations）** 考虑如下线性方程组（system of linear equations）

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 例 13.79 里把 $Ax=b$ 改写成 $x=(I-A)x+b$ 并令 $A:\mathbb{R}^n\to\mathbb{R}^n$，这个变形你在线代 Strang 里应该一见如故——它就是解线性方程组的 iterative method（迭代法）的出发点。机制是：把"一次解出"改成"反复修正"。设不动点为 $x^*$，则 $x^*=(I-A)x^*+b$ 展开后正是 $Ax^*=b$，所以不动点与解一一对应。教科书只在 $\mathbb{R}^n$ 上做重写，但数值线代（你 CSAPP 和 Strang 都沾过边）会当场把它变成可执行的算法：选初值 $x^{(0)}$，反复迭代 $x^{(k+1)}=(I-A)x^{(k)}+b$。这一格式最朴素的形式可视为 Jacobi iteration（Jacobi 迭代）型方法；严格说，若先把系数矩阵按对角元归一，$I-A$ 对应的正是 Jacobi 的迭代矩阵，而其变体 Gauss–Seidel iteration（Gauss–Seidel 迭代）则把刚算出的新分量立即投入使用，而不是等一整轮结束，通常省存储且常加速收敛。一个具体数值例子：取方程组 $x_1-0.2x_2=2$，$-0.1x_1+x_2=3$，即迭代 $x_1^{(k+1)}=2+0.2x_2^{(k)}$，$x_2^{(k+1)}=3+0.1x_1^{(k)}$。从 $(0,0)$ 出发得到 $(2,3)$、$(2.6,3.2)$、$(2.64,3.26)$，逐步逼近真解 $(132/49,\,160/49)\approx(2.653,\,3.265)$，误差肉眼可见地收缩。
>
> 判定收敛的条件也在这节给出了线索：§13.11.1 选 $d_\infty$ 度量后，要求每行满足 $\sum_j|c_{ij}|\le\alpha<1$，即行和小于 1；习题 13.11.1 再给一个列和条件。机制是：$d_\infty$ 下的压缩条件等价于迭代矩阵的无穷范数不超过 1，即 $\max_i\sum_j|c_{ij}|\le\alpha$，这就是"行和闸门"；换成 $d_1$ 度量，压缩条件就变成 $\max_j\sum_i|c_{ij}|\le\alpha$，即"列和闸门"。这两个闸门合起来正是 operator norm（算子范数）在不同度量下的两种具体计算，可以命名为"矩阵范数闸门法"：先选度量，再把压缩条件翻译成相应范数不等式。行和、列和这两个门槛，严格说正是线性代数里 row diagonal dominance（行对角占优）、column diagonal dominance（列对角占优）能让迭代收敛的雏形：Jacobi 迭代矩阵 $D^{-1}(L+U)$ 的行和条件恰好就是 $\sum_{j\ne i}|a_{ij}|<|a_{ii}|$，即对角元绝对值严格大于同行非对角元绝对值之和。机制是第一性原理式的：对角元足够大，意味着每次修正都把误差乘以一个小于 1 的因子。
>
> 这里可以补上 Strang 的精确判据作对照：迭代 $x^{(k+1)}=Gx^{(k)}+c$ 收敛的充要条件是迭代矩阵 $G$ 的 spectral radius（谱半径，即特征值模的最大值）满足 $\rho(G)<1$；而任何矩阵范数都是谱半径的上界，所以 $\|G\|_\infty\le\alpha<1$ 是 $\rho(G)<1$ 的充分条件。区别在于：Strang 的谱半径是精确但难算的判据，本节的范数闸门是手算即可的充分条件，两者说的是同一件事——误差向量按 $G$ 的谱行为收缩。于是你看到一条贯穿线：Strang 的矩阵语言加度量空间的压缩性加数值迭代的收敛判据，说的是同一件事。这也体现了本章精神——不动点不只是存在性工具，更是构造性的：它保证你那条迭代序列真的走到解。用 CLRS 的 loop invariant（循环不变量）视角看，误差估计 $d(x^{(k)},x^*)\le\alpha^k d(x^{(0)},x^*)$ 就是迭代的循环不变量：初始化时 $k=0$ 成立，保持步骤由压缩性质推出，终止时给出先验误差界。最后提醒 CSAPP 的浮点现实：每步迭代都带 floating-point rounding（浮点舍入），理论收缩到机器精度附近就会被舍入噪声淹没，所以停止准则应看残差 $\|b-Ax^{(k)}\|$ 是否足够小，而不是要求 $x^{(k)}$ 完全不再变化。

---
```math
\begin{aligned}
a_{11} x_1 + a_{12} x_2 + \cdots + a_{1n} x_n &= b_1 \\
a_{21} x_1 + a_{22} x_2 + \cdots + a_{2n} x_n &= b_2 \\
&\;\;\vdots \\
a_{n1} x_1 + a_{n2} x_2 + \cdots + a_{nn} x_n &= b_n
\end{aligned} \tag{13}
```
我们可以把这个方程组改写为如下形式
```math
\begin{aligned}
x_1 &= c_{11} x_1 + c_{12} x_2 + \cdots + c_{1n} x_n + b_1 \\
x_2 &= c_{21} x_1 + c_{22} x_2 + \cdots + c_{2n} x_n + b_2 \\
&\;\;\vdots \\
x_n &= c_{n1} x_1 + c_{n2} x_2 + \cdots + c_{nn} x_n + b_n
\end{aligned} \tag{14}
```
其中（where），当 $j \neq i$ 时 $c_{ij} = -a_{ij}$，且 $c_{ii} = 1 - a_{ii}$。于是，我们可以通过求解等价的方程组 (14)，来得到方程组 (13) 的解（solutions）。


<!-- ===== W3 ===== -->

# 书页 589–590 翻译：§13.10 压缩映射的应用（一）

<span style="color:#7f8c8d">书页 589 …</span>

## <span style="color:#c0392b">§13.10 压缩映射的应用（一）</span>

<span style="color:#2471a3;">**[section]**</span> 本节标题为 Contraction Maps 的应用（一），即 Applications of Contraction Maps (I)，开启第 13 章后半关于压缩映射不动点的若干经典应用。

<span style="color:#2471a3;">**[note]**</span> 开篇承接上一节例 13.79（有限线性方程组）的收尾叙述。此时我们已经可以很方便地借助算子的不动点（fixed point）来审视该问题：对于 $x = (x_1, \ldots, x_n) \in \mathbb{R}^n$，令 $y = A(x)$，其中 $y = (y_1, \ldots, y_n)$ 且

```math
y_i = \sum_{j=1}^{n} c_{ij} x_j + b_i .
```

由此 $A : \mathbb{R}^n \to \mathbb{R}^n$。于是方程 (14) 的一个解正是算子 $A$ 的一个不动点。

<span style="color:#2471a3;">**[note]**</span> 文献中常用记号 $\blacksquare$（黑方块）表示一个示例的结束。以下为本页的三个重要例子。

> <span style="color:#7f8c8d;">TBB §13.10, p.589</span>

<span style="color:#2471a3;">**[example]**</span> **例 13.80（无穷线性方程组, Infinite Systems of Linear Equations）**：上述这些想法可以进一步应用于无穷（infinite）线性方程组。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 例 13.80 的关键教训是选择正确的完备空间。从 $\mathbb{R}^n$ 跳到无穷序列后，所有 $x_i$ 之和收敛之类要求让算子的定义域与值域不再自动封闭，于是教科书列出一串候选国王：$\ell^1,\ \ell^2,\ \ell^\infty$（参见例 13.7–13.9）。机制在于：有限维线性空间里线性算子是自动连续的，闭性几乎免费；但到了无穷维序列空间，逐坐标给出的公式完全可能把有界序列映成无界序列，或把平方可和序列映成非平方可和序列，所以"映进自身"必须先验证。三个候选空间分别装备范数 $\|x\|_1=\sum_i|x_i|$、$\|x\|_2=\bigl(\sum_i|x_i|^2\bigr)^{1/2}$、$\|x\|_\infty=\sup_i|x_i|$，它们都完备：Cauchy 列收敛且极限仍留在同一空间。$A$ 是否为压缩、以及解落在哪个空间，完全取决于你的选择——这正是 §13.11.2 里"抉择是决定性的"一句的含义：定理 13.84 承诺的解在 $\ell^\infty$ 里，它不保证解也落在 $\ell^1$ 或 $\ell^2$ 里；换个空间，同一个算子可能连自映都做不到。
>
> 若你学过 6.042J，还可以补一层认识：$\ell^\infty$ 里的元素是 bounded sequence（有界序列），而可数无穷多坐标本身是 6.042J 里 countable set（可数集）的概念：坐标的指标集是 $\mathbb{N}$，可数。但注意区分：指标集可数并不意味着空间本身可数；$\ell^\infty$ 作为序列全体是不可数的，因为 $\{0,1\}^{\mathbb{N}}$ 已不可数，这正是 6.042J 的 diagonal argument（对角线论证）给出的结论。一个管"坐标位置的个数"，一个管"可能的序列总数"，两者别混。无穷方程组之所以比有限方程组棘手，在于连一个解的指标个数都是可数无穷：有限情形你还能把解写成有限长的列向量，无穷情形解本身就是一条序列，它的"形状"必须由所选的序列空间来规定。
>
> 直觉上可这样理解：有限情形 $|c_{ij}|$ 若控制不当至多局部爆掉，而无穷情形必须对各坐标一致地有界，这正是 sup metric（上确界度量）出场的原因。有限矩阵的行和是有限和，最大行和天然存在，它就是整体闸门；无穷矩阵每行的行和是无穷级数，可能出现"每一行都收敛，但各行和的上确界不存在"的坏情形，此时一个有界输入 $x$ 会被逐行放大成无界输出，自映直接失败。所以需要 uniform boundedness（一致有界性）：$\sup_i\sum_j|c_{ij}|\le\alpha<1$ 是对所有行同时生效的闸门，可以命名为"一致有界闸门"。定理 13.84 表格里那两个条件（$\{b_i\}$ 有界加上每行 $\sum_j|c_{ij}|\le\alpha<1$）合起来干两件事：让 $A$ 把 $\ell^\infty$ 映进自身，并让 $A$ 成为压缩——缺一不可。机制逐条验证：由 $|A(x)_i|\le|b_i|+\sum_j|c_{ij}|\,|x_j|\le M+\alpha\|x\|_\infty$ 得到自映；对两个有界序列 $x,y$，$|A(x)_i-A(y)_i|\le\sum_j|c_{ij}|\,|x_j-y_j|\le\alpha\|x-y\|_\infty$，取上确界得 $d_\infty(Ax,Ay)\le\alpha\,d_\infty(x,y)$，得到压缩。若 $\{b_i\}$ 无界，连常序列 $x=0$ 的像都无界，自映失败；若行和条件破坏，压缩失败，Banach 定理无法启动。
>
> 一个具体函数例子：取 $c_{ij}=2^{-(i+j)}$，$b_i=1$，即 $A(x)_i=1+\sum_{j=1}^{\infty}2^{-(i+j)}x_j$。每行行和 $\sum_j2^{-(i+j)}=2^{-i}\le 1/2$，所以 $\alpha=1/2$，且 $|A(x)_i|\le1+2^{-i}\|x\|_\infty\le1+\tfrac12\|x\|_\infty$，自映与压缩同时成立。从 $x^{(0)}=0$ 迭代一步得 $x^{(1)}_i=1$，两步得 $x^{(2)}_i=1+2^{-i}$；直接解不动点方程可得唯一有界解 $x^*_i=1+\tfrac32\,2^{-i}$，它在 $\ell^\infty$ 中趋于 1，但显然不属于 $\ell^1$，因为坐标不趋于零。这个例子把本节全部教训压缩在一个算式里：空间选对，三件套齐活，Banach 定理连具体解的闭形式都帮你逼近出来。

---

> <span style="color:#7f8c8d">**[footnote]**</span> 在十九世纪末期，多位作者曾考虑过这类方程组，它们出现在例如代数方程与天体力学（celestial mechanics）的研究之中。

> <span style="color:#7f8c8d">**[footnote]**</span> 有趣的是，第一个遇到无穷线性方程组的人是 Joseph Fourier（傅里叶，1768–1830），见其 1822 年的经典研究。他的方法简单却缺乏严格论证；此后这个主题沉寂了整整半个世纪。

假设我们有如下形式的无穷方程组：

```math
x_i = \sum_{j=1}^{\infty} c_{ij} x_j + b_i \qquad (i = 1, 2, 3, \ldots).
\tag{15}
```

我们寻求满足 (15) 的一个序列 $x = \{x_i\}$。类似例 13.79，我们可以考虑由 $y = A(x)$ 定义的算子 $A$，其中 $x = \{x_i\}$、$y = \{y_i\}$ 且 $y_i = \sum_{j=1}^{\infty} c_{ij} x_j + b_i$。与前面一样，(15) 的一个解可看作算子 $A$ 的不动点，但此处我们必须更加小心。

在例 13.79 中，算子的定义域与值域显然都是 $\mathbb{R}^n$；而这里我们有若干可能考虑的序列空间（sequence spaces），例如 $\ell^1$、$\ell^2$、$\ell^\infty$（这些空间在例 13.7–13.9 中已有描述）。我们在下一节继续讨论这个例子。

> <span style="color:#7f8c8d;">TBB §13.10, p.589</span>

<span style="color:#2471a3;">**[example]**</span> **例 13.81（Fredholm 积分方程, Fredholm's Integral Equation）**：你可能对数学物理中的某些"边值问题"（boundary value problems）较为熟悉，例如 Dirichlet 问题（狄利克雷问题）与 Neumann 问题（诺伊曼问题）。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 这个方程的标准名称是 Fredholm integral equation of the second kind（第二类 Fredholm 积分方程），以瑞典数学家 Erik Ivar Fredholm（1866–1927）命名，他在约 1900–1903 年把这类方程解的存在性判据与行列式技巧整理成系统理论。所谓“第二类”，指未知函数 $f$ 既单独出现在等号左边、又藏在积分号里面；若 $f$ 只出现在积分号内而左边为零，则叫第一类，它面对的是积分算子把信息抹平后带来的病态困难。把未知函数塞进积分号的想法其实更早，Fredholm 的贡献在于把散落的技巧收编为一套可复用的理论。所以记名字不如记结构：一个未知函数等于“对它做一次积分变换”再加上“一个已知函数”。
>
> 用你在 Strang 线性代数里练出的直觉看，积分算子 $f\mapsto \int_a^b K(x,\cdot)f$ 很像无穷维的矩阵乘向量。有限维时 $(Au)_i=\sum_j A_{ij}u_j$，把行指标 $i$ 换成连续变量 $x$、列指标 $j$ 换成连续变量 $y$、求和换成积分，就得到 $(Kf)(x)=\int_a^b K(x,y)f(y)\,dy$：$K$ 是无穷维矩阵，$f$ 是无穷维向量，解方程 $f-\lambda Kf=\varphi$ 与解 $(I-\lambda A)u=\varphi$ 形式完全一致。这里还回响着 6.042J 的可数性结论：你曾用对角线论证知道 $[a,b]$ 不可数，所以当有限矩阵的指标集 $\{1,\dots,n\}$ 推广为连续区间时，对不可数多列的“求和”只有积分这一种合理含义——连续指标的矩阵天生就该用积分来乘。
>
> §13.11.3 将证明只要 $|\lambda|<\tfrac{1}{M(b-a)}$，该算子就是压缩，逐次逼近成立。先用一个具体例子把结构摸实：取 $[a,b]=[0,1]$、$K(x,y)=1$、$\varphi(x)=x$，则 $M=1$、$b-a=1$，条件退化为 $|\lambda|<1$。从 $f_0=\varphi=x$ 出发，$K\varphi=\int_0^1 y\,dy=1/2$，而 $K(1/2)=\int_0^1 (1/2)\,dy=1/2$，由 6.042J 的归纳法一步即得 $K^n\varphi=1/2$ 对所有 $n\ge 1$ 成立，于是 $f=x+\lambda/2+\lambda^2/2+\cdots=x+\tfrac{\lambda}{2}(1+\lambda+\lambda^2+\cdots)=x+\tfrac{\lambda}{2(1-\lambda)}$。代回验证：$\int_0^1 f\,dy=\tfrac{1}{2(1-\lambda)}$，方程两边相等。分母中的 $1-\lambda$ 正是 geometric series（几何级数）的求和结果，条件 $|\lambda|<1$ 的本质被这个例子完全暴露。
>
> 这个例子背后是一条通往 Carl Neumann 级数的小径：把逐次逼近序列逐项展开并让 $n\to\infty$，得到 $f=\varphi+\lambda K\varphi+\lambda^2 K^2\varphi+\cdots$，即解关于 $\lambda$ 的幂级数（power series）展开。它收敛的原因与几何级数完全相同：只要 $|\lambda|\cdot\|K\|\le |\lambda|M(b-a)<1$，第 $n$ 项就按公比 $q<1$ 衰减，尾部必然趋于零。请把这个观察固化成模板，可命名为“几何级数判据”：以后凡看到“参数足够小才收敛”，先问一句“它是不是某个 $\sum q^n$ 的抽象版”。这级数还反过来约束可和性：交换逐项积分与求和需要第 9 章的一致收敛（uniform convergence）——尾部必须与 $x$ 无关地一致小；而压缩条件恰好给出与 $x$ 无关的界，套用 Weierstrass M 判别法（魏尔斯特拉斯 M 判别法：若 $|u_n(x)|\le M_n$ 且 $\sum M_n<\infty$，则级数一致收敛）即可逐项操作。这正是“$\lambda$ 小才收敛”的深层含义。
>
> 把这一收敛机制放到 CSAPP 的有限精度世界里看会更具体：IEEE 754 的 round-to-nearest（就近舍入）保证单次算术运算只引入不超过机器精度 $\varepsilon$ 的相对误差，但当把 $f=\varphi+\lambda K\varphi+\cdots$ 截断成有限项求和时，几何级数的尾巴就是舍入补不回的解析误差；公比 $q=|\lambda|M(b-a)<1$ 保证尾巴按 $q^n$ 衰减，截断误差有先验上界，而 $q$ 越接近 $1$，达到给定精度所需的迭代步数越多、累积的舍入误差越大。区别在于：CSAPP 关心的是有限位模式编码下逐次运算的精度损失，这里关心的是实值迭代在理想算术下是否收敛——一个管“机器上的近似”，一个管“数学上的存在”。

---

我们的下一个例子涉及一个积分方程（integral equation），它与它的若干近亲在处理这类问题时扮演重要角色。考虑方程

```math
f(x) = \lambda \int_a^b K(x, y)\, f(y)\, dy + \varphi(x),
\tag{16}
```

其中 $\lambda \in \mathbb{R}$，$\varphi$ 在 $[a,b]$ 上连续，且 $K$ 在 $[a,b] \times [a,b]$ 上连续。我们寻求满足 (16) 的一个函数 $f \in C[a, b]$。

自然而然可以考虑定义在 $C[a, b]$ 上的算子 $A$，令 $A(f) = g$，其中

```math
(A(f))(x) = g(x) = \lambda \int_a^b K(x, y)\, f(y)\, dy + \varphi(x).
```

这个算子的一个不动点即给出 (16) 的一个解。与例 13.80 一样，我们必须明确此算子的值域。我们在下一节继续讨论。

> <span style="color:#7f8c8d;">TBB §13.10, p.589</span>

<span style="color:#2471a3;">**[example]**</span> **例 13.82（微分方程, Differential Equations）**：设 $D$ 是 $\mathbb{R}^2$ 中的开集，且 $f : D \to \mathbb{R}$。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 例 13.82 的等价变形值得拆开两个方向看。若 $\varphi$ 是初值问题 $y'=f(x,y),\ y(x_0)=y_0$ 的解，对等式两边从 $x_0$ 到 $x$ 积分，fundamental theorem of calculus（微积分基本定理）立刻给出 $\varphi(x)=y_0+\int_{x_0}^{x}f(t,\varphi(t))\,dt$；反过来，若连续函数 $\varphi$ 满足积分方程，右端被积函数 $t\mapsto f(t,\varphi(t))$ 连续，积分上限函数可微，求导即得 $\varphi'(x)=f(x,\varphi(x))$，再把 $x=x_0$ 代入，上下限重合使积分为零，初值 $\varphi(x_0)=y_0$ 自动成立。两个方向的桥梁都是微积分基本定理，但真正的价值在反方向：微分方程被翻译成了一个不含导数的方程。
>
> 为什么非绕到积分形式不可？第一性原理的回答是：积分是平滑运算，微分是破坏运算。微分定义为差商的极限，先把两个相近点的函数值相减、再除以趋于零的 $h$，等于把函数的微小粗糙放大；连续函数可以处处不可导，说明求导对正则性要求极高。积分则相反，它本质上是 Riemann sum（黎曼和）取极限，是对函数值做平均：只要 $|f(t)|\le M$，就有 $|\int f|\le M\cdot(\text{区间长度})$，剧烈震荡在平均之后被抹平，积分把 $f$ 变成至少同样光滑、通常更光滑的对象。对 $f(x,y)=x^2\sin(xy)+ye^{xy}$ 这种右端，你没法用初等技巧把 $y$ 从导数里解出来，但“对两边积分”这步恒等式永远合法——这把难题从“求导反演”挪到了“压缩不动点”。
>
> 积分形式的另一个隐蔽好处是：它把初值 $y_0$ 直接焊进公式。候选解 $\varphi(x)=y_0+\int_{x_0}^{x}\cdots$ 无论怎么迭代，代入 $x=x_0$ 时积分都为零，所以候选解必然穿过点 $(x_0,y_0)$，初值条件从“额外约束”变成“自动满足”。用最简单的例子看全貌：$y'=y,\ y(0)=1$ 改写为 $\varphi(x)=1+\int_0^x\varphi(t)\,dt$。从 $\varphi_0=1$ 出发做逐次逼近（Picard iteration，皮卡迭代）：$\varphi_1=1+x$，$\varphi_2=1+x+x^2/2$，$\varphi_3=1+x+x^2/2+x^3/6$，每一步都过 $(0,1)$，序列的极限是 $e^x$。你看到的不只是逼近生效，而是每步多出的 $x^n/n!$ 正是把初值焊住后自然长出来的泰勒系数。这里也有 6.042J 归纳法的影子：$\varphi_{n+1}=A\varphi_n$ 是一条递归定义（recursive definition），归纳只保证每一步迭代结果都有定义且连续，而“极限存在且满足方程”要靠压缩映射的解析论证补上，这正是离散归纳与连续极限的分工。
>
> 但真正让积分方程优于微分方程的，是下一步的职业选择：左边不再含 $\varphi'$，于是可以把 $\varphi$ 当普通未知函数直接喂给 contraction mapping theorem（压缩映射定理）——那个定理只认识完备度量空间和其上的自映射，完全不认识导数。把“带导数的约束”翻译成“带积分的约束”，再翻译成不动点方程 $\varphi=A\varphi$，这是可复用的模板，可命名为“先积分、后压缩”：遇到微分条件先积分成不动点形式，再验证压缩，最后调用不动点定理。这个动作与 Strang 里把 $Ax=b$ 改写成 $x=Tx+c$ 再迭代是同一套路，区别在于 Strang 的 $T$ 是有限矩阵、判据是 spectral radius（谱半径）小于 $1$，这里的 $A$ 是积分算子、判据是 Lipschitz constant（利普希茨常数）小于 $1$。若回想 CSAPP 里浮点舍入误差会在长求和中累积，这里的压缩条件 $q<1$ 恰好是让每步误差不累积、反而按比例衰减的数学保证——区别在于 CSAPP 处理的是有限精度位模式下的舍入，这里给出的是实值迭代的结构稳定性。你在第 12 章学的微积分基本定理和本节的积分算子，让定积分完成了从“算累计量”的计算工具到“证明解存在”的存在性工具的角色跃迁——这本身就是分析学里微积分基本定理分量有多重的最好注脚。

---

我们希望求出微分方程的一个局部解（local solution）：

```math
\frac{dy}{dx} = f(x, y), \qquad y(x_0) = y_0 .
```

<span style="color:#7f8c8d">书页 590 …</span>

<span style="color:#2471a3;">**[example]**</span> **例 13.82（续）**：作为一个具体且熟悉的例子，我们可以要求出如下方程的解

```math
\frac{dy}{dx} = x^2 \sin(xy) + y e^{xy},
```

它"穿过"点 $(0, 0)$。

我们能确定这样的解一定存在吗？自然需要对 $f$ 施加某些条件。眼下我们仅看看如何把问题转化为算子（operator）的语言。

我们首先把问题改写成积分方程的形式。我们在某个包含 $x_0$ 的开区间上寻求一个函数 $\varphi$，使得

```math
\varphi'(x) = f(x, \varphi(x)) \quad \text{且} \quad \varphi(x_0) = y_0 .
```

我们可以把问题重新表述为：寻求 $\varphi$ 使得

```math
\varphi(x) = y_0 + \int_{x_0}^{x} f(t, \varphi(t))\, dt .
```

一个恰当形式的算子 $A$ 即

```math
(A(\varphi))(x) = y_0 + \int_{x_0}^{x} f(t, \varphi(t))\, dt
```

对本问题而言是自然的。我们必须小心地对 $f$ 施加条件，以便能在某个合适的函数空间上定义 $A$；这将在下一节完成。

我们已呈现了几个历史上重要的问题示例，其解都归结为算子的不动点。在每一种情形下，对所要考虑的序列类或函数类施加恰当限制，使我们得以利用 Banach 不动点定理（Banach fixed point theorem, 定理 13.75）来证明在该空间中存在一个不动点——事实上是唯一的不动点。

我们在下一节得到的每一个定理，都分别针对本节提到的这若干例子中的一个。

<span style="color:#2471a3;">**[note]**</span> 本节到此结束。§13.10 主要的工作是建立"把问题化为算子 A 的不动点"这一统一视角，具体的存在唯一性证明则留待下一节 §13.11。

<span style="color:#7f8c8d">*（本页其余部分为 §13.10 节习题区 Exercises 13.10.1–13.10.3，按约定跳过，不翻译、不收录。）*</span>


<!-- ===== W4 ===== -->

# TBB《Elementary Real Analysis》第 13 章 · 书页 591–592 双语翻译

<span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">**13.11 压缩映射的应用 (II)（Applications of Contraction Maps (II)）**</span>

<span style="color:#7f8c8d">*（本节为拓展小节，可省略。）*</span>

在本节中我们回看 §13.10 中的每一个例子，求出使相应算子成为压缩映射（contraction maps）的条件。

在 §13.10 中我们看到，各种方程或方程组（systems of equations）的解都对应于与该方程相关联的算子的不动点（fixed points）。

§13.9 的不动点定理（fixed point theorem）有时可以用来保证解的存在性，事实上是唯一解（unique one）。

当这些条件成立时，解将是唯一的。

并且我们可以用逐次逼近法（method of successive approximations）求得这些解。

注意在每一种情形下，我们都必须得到一个完整的度量空间，使得算子在该空间上是压缩映射。

这样，Theorem 13.75 的结论才会在该空间中适用。

> <span style="color:#7f8c8d;">TBB §13.11, p.591</span>

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">**例 13.83：**</span>（重访例 13.78。）（Example 13.78 Revisited）

方程 $ax = b$ 的一个解无非就是算子
```math
A(x) = (1 − a)x + b
```
的一个不动点。

这里我们在度量空间 $\mathbb{R}$（带上通常的度量）中考虑。

我们发现 $A : \mathbb{R} \to \mathbb{R}$。

为了判断 $A$ 是否是一个压缩映射，对 $x, y \in \mathbb{R}$，我们计算：
```math
d(A(x), A(y)) = |A(x) − A(y)| = |(1 − a)(x − y)|
= |1 − a||x − y| = |1 − a|\,d(x, y).
```
因此，$A$ 是压缩映射当且仅当 $|1 − a| < 1$。

根据 Theorem 13.75，只要 $|1 − a| < 1$，即只要 $0 < a < 2$，方程 $ax = b$ 就在 $\mathbb{R}$ 中有唯一解。

初等代数的学生都知道：只要 $a \neq 0$，方程 $ax = b$ 就有唯一解 $x = b/a$；若 $a = 0$ 且 $b \neq 0$ 则无解；若 $a = b = 0$ 则每个实数 $x$ 都是解。

这里的要点在于：压缩映射原理（contraction mapping principle）的应用，仅在受限条件 $|1 − a| < 1$ 下才是可行的。$\square$

我们给出这个例子，部分地是作为一个热身（warm-up），部分地是为了强调：Theorem 13.75 给出的是唯一不动点的充分条件（sufficient condition），而非必要条件（necessary condition）。

下面我们继续讨论几个在历史上很重要、可以应用 Banach 不动点定理（Banach fixed-point theorem）的例子。

还有众多其他有趣的应用。

你可以找到一个涉及平面紧致子集空间 $K$（配上 Hausdorff 度量（Hausdorff metric））的应用$^3$。

它与"分形图像压缩"（fractal image compression）技术有关，该技术可用于在计算机中编码和存储图形图像。

另一个应用，见习题 13.11.3，它给出隐函数定理（implicit function theorem）的一个证明。

<hr style="border:none;border-top:1px dashed #7f8c8d;"/>

<span style="color:#7f8c8d">书页 591 … 本节开头为 §13.11 引言，随后依次为例 13.83、§13.11.1 小节标题。注脚 3：关于"拼贴定理"（collage theorem）的材料见 Bruckner, Bruckner, and Thomson, op. cit., p. 432。</span>

<span style="color:#1e8449">**[note]**</span> 注（脚注 3）：关于"拼贴定理"（collage theorem）的材料，见 Bruckner、Bruckner 及 Thomson 所著引书第 432 页。

<span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">**13.11.1 方程组（Systems of Equations）（重访例 13.79）**</span>

<span style="color:#7f8c8d">*（本小节为拓展小节，可省略。）*</span>

<span style="color:#7f8c8d">书页 592 …（Metric Spaces，第 13 章页眉）</span>

在例 13.79 中我们看到，方程组
```math
a_{11} x_1 + a_{12} x_2 + \cdots + a_{1n} x_n = b_1
```
```math
a_{21} x_1 + a_{22} x_2 + \cdots + a_{2n} x_n = b_2
```
```math
\vdots \qquad\qquad\qquad\qquad (17)
```
```math
a_{n1} x_1 + a_{n2} x_2 + \cdots + a_{nn} x_n = b_n
```
可以通过求算子 $A : \mathbb{R}^n \to \mathbb{R}^n$（由 $y = A(x)$ 定义）的一个不动点来求解，其中
```math
y_i = \sum_{j=1}^{n} c_{ij} x_j + b_i
```
这里 $x = (x_1, \ldots, x_n)$，$y = (y_1, \ldots, y_n)$。

为了应用 Theorem 13.75，我们必须指定 $\mathbb{R}^n$ 上的度量——$A$ 是否为压缩映射将取决于我们对度量的选择。

让我们选择度量
```math
d_\infty(x, y) = \max_{1 \leq i \leq n} |x_i − y_i|.
```
（见习题 13.2.6。）

在这种情形下，设 $x, x^{*} \in \mathbb{R}^n$，其中 $y = A(x)$、$y^{*} = A(x^{*})$，并计算：
```math
d(A(x), A(x^{*})) = d(y, y^{*}) = \max_{i} |y_i − y^{*}_i|
```
```math
= \max_{i} \left| \sum_{j} c_{ij} (x_j − x^{*}_j) \right|
```
```math
\leq \max_{i} \sum_{j} |c_{ij}| \, |x_j − x^{*}_j|
```
```math
\leq \left( \max_{i} \sum_{j} |c_{ij}| \right) \left( \max_{j} |x_j − x^{*}_j| \right)
```
```math
\leq \max_{i} \sum_{j} |c_{ij}| \; d(x, x^{*}).
```
因此，若存在一个数 $\alpha$，使得对一切 $i = 1, \ldots, n$ 都有
```math
\sum_{j} |c_{ij}| \leq \alpha < 1,
```
则 $A$ 将是一个压缩映射。

注意，只要存在这样的 $\alpha$，使得对一切 $i = 1, \ldots, n$ 都有 $\sum_{j} |c_{ij}| \leq \alpha < 1$，Theorem 13.75 就保证度量空间 $(\mathbb{R}^n, d_\infty)$ 中有一个唯一解。

习题 13.11.1 提供了一个不同的条件，其中用到的是列和（column sums）而非行和（row sums）。

<span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">**13.11.2 无限方程组（Infinite Systems）（重访例 13.80）**</span>

<span style="color:#7f8c8d">*（本小节为拓展小节，可省略。）*</span>

这里我们在考虑无限方程组
```math
x_i = \sum_{j=1}^{\infty} c_{ij} x_j + b_i \qquad (i = 1, 2, 3, \ldots). \qquad\qquad (18)
```


<!-- ===== W5 ===== -->

<span style="color:#7f8c8d">书页 593 — 第 13 章 §13.11 Applications of Contraction Maps (II)（压缩映射的应用 II 续）</span>

<span style="color:#2471a3;">**[section]**</span> 本节系统（18）引出算子 $y = A(x)$，其中 $x = \{x_i\}$、$y = \{y_i\}$，且

```math
y_i = \sum_{j=1}^{\infty} c_{ij} x_j + b_i .
\tag{19}
```

<span style="color:#2471a3;">**[note]**</span> 若我们希望找出 $A$ 成为压缩映射（contraction map）的条件，与前文一样，必须指明我们考虑的是哪一个度量空间（metric space），而这里的抉择是决定性的。

<span style="color:#2471a3;">**[example]**</span> 例如，假设我们选择有界序列空间（space of bounded sequences），即 $m$ 或 $\ell^\infty$，并配上度量

```math
d_\infty(x, y) = \sup_i (|x_i - y_i|) .
```

（参见例 13.9。）

<span style="color:#2471a3;">**[note]**</span> 由于我们希望 $A$ 把 $\ell^\infty$ 映到自身（map $\ell^\infty$ into itself），故施加要求 $\{b_i\} \in \ell^\infty$，即存在 $B < \infty$ 使得

```math
|b_i| < B \quad \text{对一切 } i \in \mathbb{N}.
\tag{20}
```

上一例的工作提示我们加上限制

```math
\sum_{j=1}^{\infty} |c_{ij}| \leq \alpha < 1 \quad \text{对一切 } i \in \mathbb{N}.
\tag{21}
```

<span style="color:#2471a3;">**[proof]**</span> 现假设系统（18）满足条件（20）与（21），且 $A$ 由（19）定义，我们要证明 $A$ 是 $\ell^\infty$ 上的压缩映射。首先验证 $A$ 把 $\ell^\infty$ 映到 $\ell^\infty$。对空间 $\ell^\infty$ 的元素 $x = \{x_1, x_2, \dots\}$，记 $\|x\|_\infty = \sup_j |x_j|$。由（18）、（20）、（21）可得

```math
|y_i| \leq \sum_{j=1}^{\infty} |c_{ij}| \|x\|_\infty + |b_i| \leq \alpha \|x\|_\infty + B .
\tag{22}
```

由于（22）对一切 $i \in \mathbb{N}$ 成立，我们看到

```math
\|A(x)\|_\infty = \|y\|_\infty = \sup_i |y_i| \leq \alpha \sup_j |x_j| + B,
```

故 $A(x) \in \ell^\infty$。于是 $A$ 把 $\ell^\infty$ 映到 $\ell^\infty$。

接下来我们证明 $A$ 是压缩映射。设 $x, x^* \in \ell^\infty$，$y = A(x)$、$y^* = A(x^*)$，则

```math
y_i^* - y_i = \sum_{j=1}^{\infty} c_{ij} (x_j^* - x_j) .
```

利用（21）可断定 $|y_i^* - y_i| \leq \alpha \|x^* - x\|_\infty$，于是

```math
\|A(x^*) - A(x)\|_\infty = \sup_i |y_i^* - y_i| \leq \alpha \|x^* - x\|_\infty .
```

但这意味着

```math
d(A(x^*), A(x)) \leq \alpha d_\infty (x^*, x),
```

于是可见 $A$ 是压缩映射。我们将此讨论总结为一条定理。

> <span style="color:#7f8c8d;">TBB §13.11, p.593</span>

<span style="color:#c0392b;">**[theorem]**</span> 定理 13.84：若方程组

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 定理 13.84 的完整证明是一个值得命名的模板，可称为“Banach 三步法”，今后所有不动点应用都照此清单执行。第①步：选定一个 complete metric space（完备度量空间）作战场——完备指其中每个 Cauchy sequence（柯西序列，项与项之间距离最终任意小）都有极限；本例选的是 $\ell^\infty$，即全体有界实数列配上 supremum norm（上确界范数）。第②步：验证算子 $A$ 把该空间映进自身，即 $A(X)\subseteq X$。第③步：验证 $A$ 是压缩——存在常数 $\alpha<1$ 使 $d(Ax,Ay)\le\alpha\,d(x,y)$，随即调用定理 13.75（压缩映射定理）得到唯一不动点。三步是一份完整清单，顺序不可乱：先有战场，再有子弹不出界的保证，最后才是误差收缩。
>
> 第②步在本定理里由条件 (20) 与 (21) 联合完成。设 $Ax=(b_i+\sum_j a_{ij}x_j)_i$，要证 $A$ 把有界序列映成有界序列：对任意 $x\in\ell^\infty$，$|\sum_j a_{ij}x_j|\le\sum_j |a_{ij}|\cdot\|x\|_\infty$，而条件 (21) 说每行的 row sum（行和）$\sum_j |a_{ij}|\le\alpha<1$，于是 $\|Ax\|_\infty\le\|b\|_\infty+\alpha\|x\|_\infty<\infty$，其中 $\|b\|_\infty<\infty$ 来自条件 (20)。行和在这里扮演的角色与 Strang 里矩阵范数相同：它是无穷维矩阵对“最坏方向”放大倍数的上界；行和 $\le\alpha<1$ 意味着矩阵把任何有界向量放大不超过 $\alpha$ 倍。条件 (20) 单独保证常数项有界，条件 (21) 单独保证线性部分增益有界，二者合起来才是完整的自映射保证。
>
> 第③步与第②步共享同一条行和估计：$\|Ax-Ay\|_\infty=\sup_i|\sum_j a_{ij}(x_j-y_j)|\le\alpha\|x-y\|_\infty$，$\alpha<1$ 即压缩。三步缺一不可，各有各的失败模式。空间不完备：在开区间 $(0,1)$ 上，映射 $A(x)=x/2$ 是压缩（常数 $1/2$），但唯一可能的不动点 $0$ 不在空间里，逐次逼近得到的柯西序列没有空间内的极限。自映射被破坏：在 $[0,1]$ 上取 $A(x)=x/2+1$，它仍是压缩，但 $A([0,1])=[1,3/2]$ 越界，第一次迭代就出局，不动点 $2$ 在战场之外。非压缩：在 $[0,1]$ 上取 $A(x)=1-x$，距离不收缩（$\alpha=1$），迭代 $x_0,1-x_0,x_0,\dots$ 来回震荡，除非起点恰为不动点 $1/2$ 否则永不收敛。
>
> 定理给出的反例恰好是第①步的注脚。把方程 $x_1=\tfrac12 x_2,\ x_2=\tfrac12 x_3,\dots$ 写成 $x_i=\tfrac12 x_{i+1}$，对任意常数 $c$，序列 $\{c,2c,4c,\dots\}$ 即 $x_i=2^{i-1}c$ 都满足它：代入得 $2^{i-1}c=\tfrac12\cdot 2^i c$。当 $c\neq 0$ 时该序列无界，根本不属于 $\ell^\infty$；只有 $c=0$ 的解留在战场内，而它正是定理保证的唯一不动点。所以“无穷多个解”并不与定理矛盾——它们生活在更大的序列空间里，而压缩映射定理只在自己选定的完备空间内发言。这正是第①步“选战场”的威力：同一个方程在更大的空间里可能有多解，完备空间的选取限定了唯一性论断的管辖范围。
>
> 这套纪律呼应 CLRS 里先定好 loop invariant（循环不变量）、再写循环的工程做法。CLRS 的不变量有三件事：初始化（第一次迭代前为真）、保持（本次为真则下次为真）、终止（循环结束时推出正确性），这三件事的证明依赖 6.042J 的数学归纳法——对离散的迭代计数 $n$ 做归纳。Banach 三步法的“不变量”是 $x_n\in X$ 且压缩不等式成立；归纳只保证序列每一项都有定义、都不出界，却推不出极限存在，极限存在需要解析层面的距离按公比 $\alpha$ 几何衰减。这正是分析与离散归纳的分工：归纳管“每步合法”，完备性与压缩管“极限存在”。与 Strang 的 Jacobi iteration（雅可比迭代）相比，把 $Ax=b$ 改写为 $x=D^{-1}(b-(L+U)x)$ 后判断 spectral radius（谱半径）小于 $1$ 是有限维的精确判据；这里的行和条件给出的是 $\infty$-范数下的 operator norm（算子范数）判据，更粗糙但在无穷维依然可用——有限维用谱半径，无穷维用压缩，这是同一个迭代思想在两个世界的不同落地方式。

---

```math
x_i = \sum_{j=1}^{\infty} c_{ij} x_j + b_i , \qquad i = 1, 2, 3, \dots
```

<span style="color:#7f8c8d">（转下页续）</span>

<span style="color:#7f8c8d">书页 594 — Metric Spaces（度量空间）</span>

满足以下两个条件：

```math
1. \; \text{存在 } B < \infty \text{ 使 } |b_i| < B \quad (i = 1, 2, \dots),
```

```math
2. \; \sum_{j=1}^{\infty} |c_{ij}| \leq \alpha < 1 \quad (i = 1, 2, \dots),
```

则该系统在 $\ell^\infty$ 中有唯一解（unique solution）。

<span style="color:#1e8449;">**[note]**</span> 定理 13.84 的结论保证该系统在空间 $\ell^\infty$ 中具有唯一解。例如考虑系统

```math
x_1 = \tfrac{1}{2} x_2, \quad x_2 = \tfrac{1}{2} x_3, \quad x_3 = \tfrac{1}{2} x_4, \dots
```

对任意 $c \in \mathbb{R}$，序列 $\{c, 2c, 4c, \dots\}$ 都是该系统的解。但这并不与定理 13.84 相矛盾，因为这样一个序列落在 $\ell^\infty$ 中当且仅当 $c = 0$。

<span style="color:#2471a3;">**[section]**</span> 13.11.3 积分方程（Integral Equations）（重访 Example 13.81）

<span style="color:#7f8c8d">*（本小节为拓展小节，可省略。）*</span>

这里我们寻求下述积分方程（integral equation）的解

```math
f(x) = \lambda \int_a^b K(x, y) f(y)\, dy + \varphi(x)
\tag{23}
```

相应的算子 $A$ 定义在 $C[a,b]$ 上：$A(f) = g$，其中

```math
(A(f))(x) = g(x) = \lambda \int_a^b K(x, y) f(y)\, dy + \varphi(x).
```

我们把「$A : C[a,b] \to C[a,b]$，即对每个 $f \in C[a,b]$，$A(f) = g$ 也在 $[a,b]$ 上连续」这一事实留作习题 13.11.2。

<span style="color:#2471a3;">**[proof]**</span> 我们想找出 $A$ 成为压缩映射的条件。设 $f_1, f_2 \in C[a,b]$，令 $g_1 = A(f_1)$、$g_2 = A(f_2)$，并令

```math
M = \max\{ |K(x, y)| : a \leq x \leq b, \; a \leq y \leq b \}.
```

（参见习题 13.6.18。）则

```math
d(g_1, g_2) = \max_{a \leq x \leq b} |g_1(x) - g_2(x)|
```

```math
\leq |\lambda| M \max_{a \leq x \leq b} |f_1(x) - f_2(x)|\, (b - a)
```

```math
\leq |\lambda| M (b - a)\, d(f_1, f_2) .
```

由此推出，只要 $|\lambda| < \dfrac{1}{M(b-a)}$，$A$ 就是压缩映射。

<span style="color:#2471a3;">**[note]**</span> 因此，只要 $|\lambda|$ 不过大，就可以用逐次逼近法（method of successive approximations）获得（23）的唯一解。$\square$


<!-- ===== W6 ===== -->

<span style="color:#7f8c8d">书页 595 §13.11 Applications of Contraction Maps (II) 续</span>

## <span style="color:#2471a3;">**[section]**</span> §13.11.4 Picard 定理（Picard's Theorem）

<span style="color:#2471a3;">**[subsection]**</span> **13.11.4 Picard 定理（Picard's Theorem，重访 Example 13.82）**

<span style="color:#7f8c8d">*（本小节为拓展小节，可省略。）*</span>

<span style="color:#2471a3;">**[section]**</span> 我们的目标在于证明经典的 Picard 定理（Picard's Theorem）——它正是把压缩映射（contraction mapping）应用于微分方程（differential equation）问题的一个实例。为此我们首先需要一个定义。

你会记得函数 $f : \mathbb{R} \to \mathbb{R}$ 满足某种 Lipschitz 条件（Lipschitz condition）是什么意思。我们现在把这个含义加以推广，让它适用于两个变量的实值函数。

> <span style="color:#7f8c8d;">TBB §13.11, p.595</span>
<span style="color:#2471a3;">**[definition]**</span> **定义 13.85**：设 $D$ 是 $\mathbb{R}^2$ 中的开集（open set），并设 $f : D \to \mathbb{R}$。我们称 $f$ 在 $D$ 上关于 $y$ 满足 Lipschitz 条件、具有 Lipschitz 常数（Lipschitz constant）$M$，是指每当 $(x, y_1)$ 与 $(x, y_2)$ 都在 $D$ 中时，有

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 定义 13.85 把第 12 章你已熟悉的一元 Lipschitz condition（Lipschitz 条件）沿第二变量搬进二元函数：对每个固定的 $x$，把 $f(x,\cdot)$ 看成只关于 $y$ 的一元函数，要求存在与 $x$ 无关的常数 $M$，使对一切 $y_1,y_2$ 都有 $|f(x,y_2)-f(x,y_1)|\le M|y_2-y_1|$。第一性原理：它只追问一件事——输出增量能否被输入增量线性控制，即沿 $y$ 方向所有割线斜率被同一个 $M$ 压住。具体例子：$f(x,y)=y\cos(x^2)$。固定 $x$ 时 $|f(x,y_2)-f(x,y_1)|=|\cos(x^2)|\,|y_2-y_1|\le|y_2-y_1|$，取 $M=1$ 即可；与此同时 $\partial f/\partial x=-2xy\sin(x^2)$ 随 $|x|$ 增长而无界。这个函数在 $x$ 方向抖得再凶，也不影响它满足定义 13.85——这就是“单方向条件”的直觉。
>
> 为什么不用更强的 $\partial f/\partial y$ 连续来替代？若偏导连续，它在闭矩形上有界，一元中值定理（端点差等于中间某点导数乘区间长）立即给出 Lipschitz 估计——Lipschitz 只是这条推理链消费的终点，导数连续只是充分条件之一。但把假设钉死在可微上会排除许多 Picard 论证仍能处理的函数：$f(x,y)=|y|$ 满足 $M=1$ 的 Lipschitz 条件，但 $\partial f/\partial y$ 在 $y=0$ 处不存在。反过来，有界变差 bounded variation（有界变差：摆动的总账有限）又太弱：$f(x,y)=\sqrt{y}$（$y\in[0,1]$）对每个固定 $x$ 单调故有界变差，但增量比 $|f(x,y)-f(x,0)|/|y-0|=1/\sqrt{y}$ 在 $0$ 附近发散，任何常数 $M$ 都压不住，压缩估计(27)所需的几何衰减无从谈起。于是偏导连续 $\Rightarrow$ Lipschitz $\Rightarrow$ 有界变差，两个箭头都不可逆。Lipschitz 恰好把证明要消费的那行估计直接写成假设：不多要光滑性，也不少要控制力。
>
> 工具箱对照：§13.9 习题 13.9.1 的一维 contraction mapping（压缩映射）假设是 $|g(y_2)-g(y_1)|\le\alpha|y_2-y_1|$ 且 $\alpha<1$，由 Banach fixed point theorem（Banach 不动点定理：完备度量空间上的压缩映射有唯一不动点）保证。定义 13.85 正是同一行估计按第二变量重写：对每个固定 $x$，$f(x,\cdot)$ 是以 $x$ 为参数的一族 Lipschitz 映射，公共常数 $M$ 扮演一维情形里 $\alpha$ 的角色。唯一区别：Picard 定理中 $M$ 不必小于 $1$，因为进入压缩估计(27)的是 $M$ 乘积分区间长度，只要区间取得足够短，$M\delta<1$ 的收缩因子就出现——这是把“全局收缩”改装成“局部收缩”的标准操作。这和 Strang 的 Linear Algebra（线性代数）里矩阵迭代法机制同构：Jacobi 迭代解 $Ax=b$ 时把 $A$ 分裂为 $D-L-U$，迭代矩阵的 spectral radius（谱半径：特征值模的最大值）$\rho(D^{-1}(L+U))<1$ 保证收敛且速率由 $\rho$ 决定；这里的 $M\delta$ 就是函数空间版的“谱半径替身”。区别：有限维时 $\rho<1$ 是充要判据，而函数空间无限维、谱难以计算，我们改用 $\sup$ 范数下的 Lipschitz 界——它只给充分条件，但恰好够用。
>
> 理解二元 Lipschitz 的关键是逐点冻结 $x$、只沿 $y$ 方向切片：把 $x$ 当成参数指标而不是活动变量。机制上，Picard iteration（Picard 迭代）的算子 $T(\varphi)(x)=y_0+\int_{x_0}^{x}f(s,\varphi(s))\,ds$ 在比较两次迭代时，差异只从 $f(s,\varphi(s))-f(s,\psi(s))$ 进入，Lipschitz 界把它压成 $M|\varphi(s)-\psi(s)|$，积分后变成 $M$ 乘区间长度再乘 $\|\varphi-\psi\|_\infty$。所以 $x$ 方向再粗糙也被积分平滑掉；唯一幸存进入收缩因子的是 $y$ 方向斜率界 $M$。可复用命名模板：我称之为「$x$-冻结切片法」——先把 $x$ 冻结成切片参数，再对整族切片验证一个公共常数 $M$；若每个切片各有 $M(x)$ 而 $\sup_x M(x)=\infty$，积分后的估计就失效，“一致”二字是初学者最容易漏的。
>
> 迭代过程是 6.042J 离散数学里熟悉的结构：$\varphi_0,\varphi_1,\varphi_2,\dots$ 由归纳定义生成，是可数序列，每步构造合法（对应 6.042J 的归纳与可数性）；但“序列收敛到不动点”不是离散归纳能推出的，它需要度量空间的 completeness（完备性：柯西列必收敛）——这是分析在离散骨架之上补的极限闭合一步。而估计 $\|\varphi_{n+1}-\varphi_n\|\le(M\delta)^n\|\varphi_1-\varphi_0\|$ 又是 CLRS《算法导论》loop invariant（循环不变量）的实分析翻版：初始化（$n=0$）、保持（压缩步）、终止（容差到达）三段齐全，几何衰减给出 $n\approx\log(1/\varepsilon)/\log(1/(M\delta))$ 的对数级迭代次数，与 CLRS 分析二分查找的复杂度同型；区别是 CLRS 的不变量活在离散循环里，这里的不变量是函数空间 $\sup$ 范数下的一条不等式。
>
> 最后把理论搬上机器：若按 CSAPP 的 IEEE 754 浮点实现这个循环，每次求 $f$ 的舍入误差约为 machine epsilon（机器精度）$\varepsilon_{\text{mach}}$，于是几何衰减 $(M\delta)^n$ 只在下探到噪声地板 $\approx\varepsilon_{\text{mach}}/(1-M\delta)$ 之前有效；CSAPP 强调浮点加法不可结合、误差逐次累积，在这里就表现为纸面上的精确压缩保证退化成机器上的一圈邻域保证。同时 $M$ 直接决定达到容差所需的迭代次数，也就是 CSAPP 意义上的计算资源预算。总之，定义 13.85 的要点一句话：$f$ 在 $x$ 方向可以随便野，$y$ 方向的斜率被同一个 $M$ 管住，才是唯一性（连同存在性）证明要的全部弹药。

---

```math
| f(x, y_2) - f(x, y_1) | \leq M |y_2 - y_1| \qquad (24)
```

> <span style="color:#7f8c8d;">TBB §13.11, p.595</span>
<span style="color:#c0392b;">**[theorem]**</span> **定理 13.86（Picard）** 设 $f$ 是 $D$ 上的连续函数，并在 $D$ 上关于 $y$ 以 Lipschitz 常数 $M$ 满足 Lipschitz 条件，又设 $(x_0, y_0) \in D$。则存在 $\delta > 0$，使得微分方程

```math
\frac{dy}{dx} = f(x, y) \qquad (25)
```

在区间 $[x_0 - \delta, \; x_0 + \delta]$ 上有唯一的解 $y = \varphi(x)$，且满足 $\varphi(x_0) = y_0$。

<span style="color:#2471a3;">**[proof]**</span> **证明**：如同在 Example 13.82 中指出的那样，我们把问题用积分方程（integral equation）的形式来表述：

```math
\varphi(x) = y_0 + \int_{x_0}^{x} f(t, \varphi(t))\, dt , \qquad (26)
```

该方程应当在区间 $[x_0 - \delta, \; x_0 + \delta]$ 上成立。由于 $D$ 是开集，故存在一个以 $(x_0, y_0)$ 为中心的闭球（closed sphere）$S$，它完全含于开集 $D$ 内部。由于 $f$ 在 $D$ 上连续，可令 $K$ 为 $| f(x, y) |$ 在球 $S$ 中诸点 $(x, y)$ 上取到的最大值。

现在利用 Lipschitz 常数 $M$〔定义如不等式 (24)〕。选取 $\delta > 0$，使得 $\delta < 1/M$，并使满足

```math
|x - x_0| \leq \delta \quad \text{且} \quad |y - y_0| \leq K\delta
```

的每一点 $(x, y)$ 都属于球 $S$。由此我们得到一个矩形（rectangle）

```math
N = [x_0 - \delta, \; x_0 + \delta] \times [y_0 - K\delta, \; y_0 + K\delta]
```

它完全位于开集 $D$ 内部（Fig. 13.6）。

<span style="color:#7f8c8d">书页 596 继续证明及图 13.6</span>

<span style="color:#2471a3;">**[figure]**</span> **图 13.6**：Picard 定理证明中 $\delta$ 的选取。图中矩形 $N \subset D$，且在 $N$ 上有 $| f | \leq K$，横轴自 $x_0 - \delta$ 经 $x_0$ 至 $x_0 + \delta$，纵轴自 $y_0 - K\delta$ 经 $y_0$ 至 $y_0 + K\delta$。

现在考察算子 $A$，将其定义为对 $x_0 - \delta \leq x \leq x_0 + \delta$ 成立

```math
(A(\varphi))(x) = \psi(x) = y_0 + \int_{x_0}^{x} f(t, \varphi(t))\, dt,
```

注意：此式未必能定义成空间 $C[x_0 - \delta, \; x_0 + \delta]$ 上的一个算子，因为函数 $\varphi(t)$ 的取值未必能保证 $(t, \varphi(t))$ 落在 $D$ 中，从而未必能保证 $f(t, \varphi(t))$ 有定义。因此我们转而考虑一个子空间。

设 $C_1$ 由 $C[x_0 - \delta, \; x_0 + \delta]$ 中满足 $\varphi(x_0) = y_0$、并且对一切 $x \in [x_0 - \delta, x_0 + \delta]$ 有

```math
|\varphi(x) - y_0| \leq K\delta
```

的那些成员构成。

那么 $C_1$ 是空间 $C[x_0 - \delta, x_0 + \delta]$ 的一个闭子空间（closed subspace），因而由定理 13.64 知它是完备的（complete）。我们要证明前面定义的算子 $A$ 把 $C_1$ 映入自身。设 $x \in [x_0 - \delta, x_0 + \delta]$，并设 $\varphi \in C_1$。于是

```math
| \psi(x) - y_0 |
= \left| \int_{x_0}^{x} f(t, \varphi(t))\, dt \right|
\leq \int_{x_0}^{x} | f(t, \varphi(t)) |\, dt
\leq K |x - x_0| \leq K\delta,
```

所以 $\psi = A(\varphi) \in C_1$，从而 $A : C_1 \to C_1$。

下面证明 $A$ 是 $C_1$ 上的压缩映射。为验证压缩条件，设 $\varphi_1, \varphi_2 \in C_1$，令 $\psi_1 = A(\varphi_1)$、$\psi_2 = A(\varphi_2)$。于是对一切 $x \in [x_0 - \delta, x_0 + \delta]$，

```math
|\psi_1(x) - \psi_2(x)|
\leq \int_{x_0}^{x} | f(t, \varphi_1(t)) - f(t, \varphi_2(t)) |\, dt \qquad (27)
\leq M\delta \max_{x} | \varphi_1(x) - \varphi_2(x) | .
```

最后一个不等式是 $f$ 的 Lipschitz 条件与不等式 $|x - x_0| \leq \delta$ 推出来的。由于 (27) 对区间 $[x_0 - \delta, x_0 + \delta]$ 内的一切 $x$ 都成立，故

```math
d(\psi_1, \psi_2) \leq M\delta \, d(\varphi_1, \varphi_2).
```

因 $M\delta < 1$，故 $A$ 是压缩映射，于是方程 $\varphi = A(\varphi)$ 在 $C_1$ 中有唯一解。换言之，方程 (26) 及其等价的方程 (25) 都具有唯一的局部解（local solution）。$\square$

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> Picard iteration（Picard 迭代）不只是存在性证明，它本身就是一台可执行的 constructive machine（构造机器）：从常数函数 $\varphi_0(x)\equiv y_0$ 出发，逐次计算 $\varphi_{n+1}(x)=y_0+\int_{x_0}^x f(t,\varphi_n(t))dt$。它的第一性原理藏在一句话里：若真解 $\varphi$ 满足 $\varphi'=f(x,\varphi)$ 且 $\varphi(x_0)=y_0$，两边从 $x_0$ 积分到 $x$ 就得到等价积分方程 $\varphi(x)=y_0+\int_{x_0}^x f(t,\varphi(t))dt$，也就是说真解正是积分算子 $A(\varphi)=y_0+\int f$ 的 fixed point（不动点）。迭代 $\varphi_{n+1}=A(\varphi_n)$ 就是反复把当前猜测解塞回方程右边，让方程自己修正自己：上一轮输出变成下一轮被积函数里的输入。这台机器可命名为"积分算子自修正迭代"：先猜、代入、积分、再猜，直到猜与算出的结果重合。
>
> 对线性方程 $y'=y,\ y(0)=1$ 跑一遍：$\varphi_0=1$，$\varphi_1=1+\int_0^x 1\,dt=1+x$，$\varphi_2=1+\int_0^x(1+t)\,dt=1+x+\tfrac{x^2}{2}$，归纳一步得 $\varphi_n(x)=1+x+\tfrac{x^2}{2}+\cdots+\tfrac{x^n}{n!}$，收敛到 $e^x$。这正是 Taylor series（泰勒级数）与幂级数解法的元算法：逐次逼近每转一圈就多精确一项，把泰勒展开从"凑出来的公式"变成"机器吐出来的序列"；而 $f(x,y)=y$ 正是例 13.77 里那个通用构造的最简特例，等于把同一台机器在最小输入上又跑了一次。这个归纳步骤可以照搬 6.042J 的 mathematical induction（数学归纳法）模板：基底 $\varphi_0$ 成立；归纳假设 $\varphi_n$ 是前 $n$ 项部分和；把假设代入积分并逐项积出第 $n+1$ 项，机器就自动产出了全部项。区别在于归纳对象：6.042J 里归纳的是自然数上的谓词，这里归纳的是函数序列上的逐项恒等式。
>
> 放到数值计算（CSAPP 的领域）里，$e^x$ 的级数、Euler method（欧拉折线法）与 Runge–Kutta 方法是同一族思路：用离散的 approximate integration（近似积分）去逼近真解。CSAPP 第 2 章的 floating point（浮点）与 rounding（舍入）教你：有限 bit pattern（位模式）只能近似实数，误差必须被追踪；数值解微分方程同样是拿有限步离散计算逼近连续对象，误差同样必须被追踪。区别在于，CSAPP 的近似生活在 $\mathbb{R}$ 的有限子集里，度量是相对误差；Picard 迭代的近似生活在函数空间 $C$ 里，度量是上确界范数。TBB 的做法比数值分析更"奢侈"：它不逐点控制截断误差，而是用 uniform convergence（一致收敛）把整列 $\varphi_n$ 作为函数整体捧成极限 $\varphi$。
>
> 这也解释了为什么 completeness（完备性）与一致收敛必须同时在场：完备性保证 Cauchy 列（项与项的距离最终任意小）有极限可收；一致收敛（即 $\sup_x|\varphi_n(x)-\varphi(x)|\to 0$，误差不随点逃逸）保证极限仍在连续函数空间 $C$ 里，且逐点极限 $\varphi=\lim\varphi_n$ 连续——这正是第 9 章上确界度量 $\|f-g\|_\infty=\sup_x|f(x)-g(x)|$ 的用处。而要让 $\varphi$ 仍是积分方程的解，还需要 $f$ 的连续性：它保证 $f(t,\varphi_n(t))\to f(t,\varphi(t))$，从而极限与积分可以交换。构造性、一致收敛、完备性在此第一次齐声亮相：全章由此从"证明存在"升级为"制造解"。可复用的直觉模板：凡是要证明"极限对象满足某个方程"，都依次问三件事——迭代是否良定义、序列是否 Cauchy、极限与算子是否可交换。
>
> 把 Picard 迭代放进你的"可执行算法"心智模型里再看一层：它和数值分析里求解常微分方程的 Euler 折线法、Runge–Kutta 法共享同一个骨架——都是把"连续的真解"替换成"一串离散的近似函数"，再用某种收敛性把近似序列的极限认作真解。区别只在于取极限的场所：Euler 法在 $\mathbb{R}$ 里取极限，每一步只更新一个数值；Picard 迭代在函数空间 $\mathscr{C}$ 里取极限，每一步更新一整条函数曲线。这正是函数空间观点（你从度量空间第 13 章开头就在建立的视角）第一次显示出它的威力：把"解一个微分方程"这个看起来无法机械化的问题，翻译成"在函数空间中跑一个压缩迭代"这个可以机械化的问题。对智能科学与技术专业的你，这个翻译动作本身就是最值得带走的东西——CSAPP 教会你程序是把数据从一种表示变换到另一种表示，而 Picard 迭代展示的是数学里同构的技艺：换一个空间（从实数换到函数），同一个不动点框架就同时管住了代数方程、积分方程和微分方程。日后你在信号处理里做迭代去噪、在优化里做 proximal iteration（近端迭代：每步求解一个带正则项的邻近算子），本质都是 Picard 式的"重复一个压缩步、让误差几何衰减"，只是算子从积分算子换成了梯度或邻近算子。

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 定理 13.86 以法国数学家 Charles Émile Picard（1856–1941）命名：存在性成果于 1890 年发表，1893 年他在《分析教程》(Traité d'Analyse) 中给出更系统的叙述，故常标作 Picard（1890/1893）；后来 Lindelöf 补强，故又称 Picard–Lindelöf theorem（Picard–Lindelöf 定理）。
>
> 但 successive approximation（逐次逼近）这一工具远早于此：先有 Cauchy 在 1820–30 年代给出存在性论证（当时只要求 $f$ 连续大致足够）；Liouville 于 1838 年把 Cauchy 的证明简化成逐次逼近——正是你在例 13.76、13.77 亲身体验的那个迭代；1876 年 Lipschitz 把连续偏导放宽成 Lipschitz condition（Lipschitz 条件，即函数值差被自变量差线性控制：$|f(x,y_1)-f(x,y_2)|\le M|y_1-y_2|$）；Picard 1890 年再把它系统化成一个通用的构造性方法。底层的抽象化发生在 1922 年：Banach 在《Fundamenta Mathematicae》发表不动点定理（Fund. Math. 3 (1922) 133–181），把某个可微方程或积分方程的具体迭代一举收编为：任何完备空间上的压缩映射都有唯一不动点，也就是本章的定理 13.75。
>
> 这条时间线的第一性原理是：逐次逼近之所以能工作，关键不在"微分"而在"压缩"。Cauchy 与 Liouville 手里的是具体方程的具体积分；Lipschitz 提取出让迭代收缩的那个条件。为什么是 Lipschitz 条件而不是仅仅连续？因为压缩估计 $d(A\varphi_1,A\varphi_2)\le M\delta\,d(\varphi_1,\varphi_2)$ 要求 $f$ 在第二个变量上的变化被线性控制，仅仅连续给不出严格小于 $1$ 的收缩系数；1876 年的放宽本质上是把压缩系数的来源从"导数有界"降级为"割线斜率有界"。Banach 再看到：只要空间完备、映射压缩，具体方程是什么根本不重要。
>
> 这正像 6.042J 里的 diagonal argument（对角线论证）：从证明实数不可数到证明停机问题不可判定，是同一个证明模板换战场。区别在于，对角线论证是"反驳存在"的模板，Banach 不动点是"构造存在"的模板——后者不仅断言唯一，还顺手给出制造解的迭代。在 Strang 的线性代数里你见过它的有限维亲戚：解 $Ax=b$ 写成迭代 $x_{k+1}=Mx_k+c$，当 spectral radius（谱半径，特征值绝对值的最大值）$\rho(M)<1$ 时收敛；Banach 定理把它推广成非线性、无限维版本。区别是，矩阵迭代的收敛速度由一个数 $\rho(M)$ 刻画，Picard 迭代则由 Lipschitz 常数与区间长度之积 $M\delta$ 刻画。
>
> 看懂这条时间线，你就明白教材为何把几十年前的 Picard 定理放在压缩映射之后当应用案例来兜售：历史是先有具体算法、后有抽象定理，而你读书的正确顺序恰是反过来的。可复用的阅读模板是"算法—定理倒置"：教材先给抽象定理，再把旧算法当作应用案例；读的时候要认出来，那个看似"只是例子"的算法，在历史上才是抽象的源头。
>
> 这条时间线还有一层值得单独挑明的认识论教训：教材的叙述顺序（先 Banach 压缩映射定理，再把它套到 Picard 定理上）与历史的发现顺序（先有 Cauchy、Liouville、Picard 的逐次逼近算法，近一个世纪后 Banach 才提炼出抽象不动点定理）正好相反。为什么教材要倒着讲？因为抽象定理一旦成立，就成了一把万能钥匙：你不再需要为每一个具体方程（代数方程、积分方程、微分方程）分别发明收敛性证明，而只需验证三件事——空间完备、算子映内、算子压缩。这就是"抽象化的经济学"：前期花成本提炼一般框架，后期用统一框架批量收割具体问题。这与你在 6.042J 里见过的"先证明一般引理、再套到具体题目"是同一个思维动作，只是抽象层级更高——6.042J 的引理抽象的是同一类题目的共同结构，Banach 定理抽象的却是横跨数论、几何、分析的"迭代求不动点"这一共同机制。也正因如此，当你日后读到泛函分析里 Hahn–Banach、开映射、闭图像等一批"大定理"时，会再次看到这种"历史滞后于逻辑"的叙述方式：先有具体问题催生技巧，后有抽象框架统一技巧，而课本永远按后者排版。

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 定理 13.86 的证明把 §13.11.4 之前的积木全用上了，值得抽成一份"Picard 迭代三步"operation template（操作模板）。第一步：把初值问题转成等价积分方程 $\varphi(x)=y_0+\int_{x_0}^x f(t,\varphi(t))dt$。这一步的合法性就是微积分基本定理：微分方程两边积分，把"求导"翻译成"积分"，于是解方程变成求积分算子 $A$ 的不动点，例 13.82 已经铺过路。
>
> 第二步：划定战场。因为 $D$ 是 open set（开集，每个点都带一个完全落在集合内的小邻域），必须先画一个含于 $D$ 的闭球，在它上面取定 $|f|\le K$ 与 Lipschitz 常数 $M$，再选一个足够小的 $\delta$，要求 $\delta<1/M$ 且矩形 $N=\{|x-x_0|\le\delta,\ |y-y_0|\le K\delta\}\subset D$。然后构造闭子空间 $C_1=\{\text{连续}\ \varphi:\ \varphi(x_0)=y_0,\ \|\varphi-y_0\|_\infty\le K\delta\}$，并验证 $A(\varphi)(x)=y_0+\int_{x_0}^x f(t,\varphi(t))dt$ 把 $C_1$ 映进 $C_1$：对任意 $\varphi\in C_1$，被积的 $f(t,\varphi(t))$ 取值在矩形里，故 $|f|\le K$ 给出 $\sup|A\varphi-y_0|\le K\delta$。
>
> 第三步：验证压缩性。对 $\varphi_1,\varphi_2\in C_1$，用 Lipschitz 条件与积分线性性得 $d(A\varphi_1,A\varphi_2)\le M\delta\,d(\varphi_1,\varphi_2)$；因 $M\delta<1$，$A$ 是 $C_1$ 上的 contraction mapping（压缩映射，即存在 $\alpha<1$ 使 $d(Au,Av)\le\alpha\,d(u,v)$），由定理 13.75 得 $C_1$ 中唯一不动点，也就是局部唯一解。
>
> 举一个具体数值例子把三个数对上：$y'=y,\ y(0)=1$，取 $D=\mathbb{R}^2$。若选 $\delta=1/2$，要保证 $C_1$ 里函数值落在 $[0,2]$（因为 $\|\varphi-1\|_\infty\le K\delta=1$），取 $K=2$ 时在该矩形上 $|f|=|y|\le 2$；Lipschitz 常数 $M=1$，于是 $M\delta=1/2<1$，压缩系数就是 $1/2$。注意 $1/2$ 只是最坏情形的误差收缩因子，真实迭代 $\varphi_n$ 的误差衰减得快得多，因为 $e^x$ 的泰勒余项是阶乘级小量。
>
> 最值得反复咀嚼的是那个小包围（small enclosure）——$C_1$ 的选取。$f$ 只在开集 $D$ 上有定义，$|f|\le K$ 与 Lipschitz 常数 $M$ 都只在闭矩形内成立，因此你只能证明局部唯一解；必须用 $\delta$ 把邻域压进 $D$，并让 $C_1$ 成为 $A$ 的 invariant set（不变集，即 $A(C_1)\subseteq C_1$，任何在圈内的对象被映射后仍在圈内），迭代才永远不越界。这正是 $y'=f(x,y)$ 一般只有局部解、而 $\cos x=x$ 全局唯一的对比来源：$\cos$ 把整个 $\mathbb{R}$ 压进 $[-1,1]$，且在 $[-1,1]$ 上 $|(\cos)'|=|\sin|\le\sin 1<1$，全局压缩所以全局唯一；微分方程的 $f$ 则未必在一个全局矩形上有界且 Lipschitz。
>
> 这套三步模板与 CLRS 的 loop invariant（循环不变量）证明法同构：初始化是 $\varphi_0\in C_1$；保持是 $A(C_1)\subseteq C_1$，保证每轮迭代仍留在包围圈内；终止由压缩映射定理给出。区别在于，CLRS 的不变量通常是离散状态上的布尔性质，而这里的不变量是度量空间里的一个闭球。模板可命名为"δ-包围压缩"：先等价改写、再圈出不变闭球、最后验压缩系数。
>
> 这个"δ-包围压缩"模板最容易被初学者略过、却最值得咀嚼的是第一步里"等价积分方程"的双向性：它不只是证明技巧，还揭示了微分方程与积分方程在存在性理论上的本质差异。微分方程陈述的是"每一点的瞬时斜率约束"（局部、逐点），积分方程陈述的是"整段区间上的累积约束"（整体、区间平均）；把前者积分成后者，等于把无穷多条逐点约束打包成一条整体约束——而压缩映射定理恰好擅长处理整体约束，因为它比较的是整条函数曲线的距离（上确界度量），不是单个点的值。这也是为什么 Picard 定理要假设 $f$ 关于 $y$ 满足 Lipschitz 条件而非仅仅连续：连续性只保证解存在（那是 Peano 定理的领地，§13.12 会讲到），Lipschitz 条件才保证迭代映射是压缩、从而解唯一且能被逐次逼近实际算出来。换句话说，Lipschitz 条件是为"压缩"服务的，而压缩是为"唯一性 + 可计算性"服务的——整条逻辑链的每一环都服务于一个明确的设计目标，读证明时若能随时问"这一步是为哪个结论服务的"，就不会在细节里迷路。

---

<span style="color:#7f8c8d">*（本页其余部分为 §13.11 习题区，按约定跳过。）*</span>


<!-- ===== W7 ===== -->

# TBB《Elementary Real Analysis》第 13 章 · 书页 597–598 双语翻译

---

<span style="color:#7f8c8d">*（书页 597 — 页首为该节末尾的一个未编号定理，随后进入 §13.12。）*</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> §13.12 的引言值得当成一次定义哲学（definition philosophy）的示范来读，它与 §13 前半段定义完备性用的是同一种动作——把实直线 $\mathbb R$ 上某个工具的必要条件升格为他处定义。回顾你已掌握的：在 $\mathbb R$ 上 Cauchy 判别法是序列收敛的充要条件，"收敛必 Cauchy"在任何度量空间都成立，是必要条件；教材把这个必要条件单独拎出来，在一般度量空间里规定"凡 Cauchy 列必有极限"，于是必要与充分在定义中合二为一，这就是完备空间的来历。现在紧致性走同一条路，只是要先做一次抉择：把实直线上闭且有界集的哪个性质当种子？是 Bolzano-Weierstrass（任意点列有收敛子列，即列紧），还是 Heine-Borel（任意开覆盖有有限子覆盖）？教材在 §13.12.1 先用 Bolzano-Weierstrass 性质定义紧致，到 §13.12.3 再证明它与 Heine-Borel 等价，可以任选其一作为出发点。
>
> 第一性原理上，这种升格能成立的条件只有一个：被选中的性质必须只用度量语言就能写出来——距离、球、序列、极限——而不借用 $\mathbb R$ 特有的序结构、四则运算或确界存在性。Cauchy 条件只用距离；列紧只用序列与极限，两者都是纯度量概念，所以能原封不动搬到任何度量空间。而"闭且有界"虽然也是度量语言，却只是列紧的一个推论而非等价物：你在第 12 章学到的"闭且有界 $\iff$ 紧致"，在一般度量空间里会断成两截——紧致 $\Rightarrow$ 闭且有界仍然成立（即后面的定理 13.90），但闭且有界 $\Rightarrow$ 紧致不再成立，两者从此分家。
>
> 具体例子能把断裂看得一清二楚：在 $\mathbb R$ 里 $[0,1]$ 闭且有界，Bolzano-Weierstrass 定理保证任何点列都能抽出收敛子列，所以紧致。但在由平方可和数列构成的度量空间 $\ell^2$ 里，闭单位球 $\{x:\|x\|_2\le 1\}$ 闭且有界却不紧：取标准单位向量列 $e_1=(1,0,0,\dots)$，$e_2=(0,1,0,\dots)$，依此类推，任意两项距离都是 $\sqrt{2}$，任何子列都保持这个间距，压不出收敛子列。这就是"闭且有界 $\neq$ 紧致"的活标本，也解释了教材为何不肯沿用 $\mathbb R$ 上的外形描述来定义紧致。
>
> 可复用的命名模板叫「必要条件升格法」：第一步，在具体对象上找一个定理中"必要且充分"的条件；第二步，检查该条件是否不依赖这个对象的额外结构；第三步，把通过检查的那一半升格为一般定义；第四步，原来定理的其余部分降级为推论去证明。你在 CSAPP 见过同款思维：IEEE 754 定义浮点数时拒绝"十进制近似"这种外形描述，改用位模式（bit pattern）与舍入规则给出可操作定义——但区别要看清：IEEE 754 用有限位模式表示实数必然产生舍入误差，是"有损压缩"；Heine-Borel 的有限子覆盖却是"无损压缩"，它从无穷多个开集中挑出有限个仍能盖住整个集合，一个点都不漏。
>
> 这条模板在 6.042J 也出现过：可数集不定义成"能一个一个列出来"的直觉，而定义成"存在到 $\mathbb N$ 的双射"，随后对角线论证再证明 $\mathbb R$ 不可数——那正是"任何列表都必然漏掉"的无穷逃逸。紧致性要说的恰好是反面：在紧空间里无穷过程逃不出去，任何点列都必须留下收敛的足迹。区别在于可数性分类的是集合的"大小"，紧致性刻画的是空间的"致密程度"。教材最后那句拓扑学预告也埋在这里：在一般拓扑空间里，Bolzano-Weierstrass 与 Heine-Borel 并不等价，通常只用 Heine-Borel 定义紧致。你现在不必深究，只需记住一句话：紧致性是一种禁得起任何无穷逼近、逃不出定手心的强有限性，它比有界严格得多。

---

> <span style="color:#7f8c8d;">TBB §13.11, p.597</span>
<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">**定理（未编号，接前页）：**</span>设 $D = [a, b] \times \mathbb{R}$，并设 $F : D \to \mathbb{R}$。

假设 $F$ 在 $D$ 上连续，且偏导数（partial derivative）$\partial F/\partial y$ 在 $D$ 上存在。

若存在正实数（positive real numbers）$\alpha$ 与 $\beta$，使得在 $D$ 上恒有
```math
\alpha \le \frac{\partial F}{\partial y} \le \beta,
```
则存在唯一的函数 $f \in C[a, b]$，使得对一切 $x \in [a, b]$ 有
```math
F(x, f(x)) = 0.
```

也就是说，方程 $F(x, y) = 0$ 可以在 $[a, b]$ 上唯一地把 $y$ 解成 $x$ 的连续函数。

<span style="color:#7f8c8d">*（注：该定理的证明提示见书末 Notes 区 Note 355，按约定不在正文展开。）*</span>

---

<span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">**13.12 紧致性（Compactness）**</span>

像度量空间研究这样的抽象学科，其目标之一就是把我们先前的思想与方法提升到这一抽象框架之中。

我们已经见到 Cauchy 判别法（Cauchy criterion）是如何进入度量空间的一般理论的。

在实直线上，Cauchy 判别法是序列收敛的充分必要条件（necessary and sufficient condition）。

在我们的新理论中，当且仅当某个空间具有这一同一性质时，我们才把它定义为完备的（complete）。

因此，我们可以把方法从实直线提升到度量空间理论：我们验证所研究的某个空间是完备的，于是 Cauchy 序列理论就可供我们使用。

以类似的方式，我们现在希望把 §4.5 中的紧致性论证（compactness arguments）提升到度量空间理论。

你会记得，Bolzano-Weierstrass 定理与 Heine-Borel 定理在连续函数性质的研究中提供了强有力的工具。

在实直线上，这些工具可用于任何闭且有界（closed and bounded）的集合。

然而，它们并非在每个度量空间中都可使用，因为闭且有界集未必具有这些性质。

反之，我们将在一个集合恰好在 Bolzano-Weierstrass 与 Heine-Borel 定理都可用时，把它定义为紧致的。

在 §13.12.1 中，我们取 Bolzano-Weierstrass 性质作为紧致性的定义，并推出一些推论。

在 §13.12.2 中，我们说明实函数初等分析中的某些定理可以推广到定义在度量空间中紧致集上的连续函数。

在 §13.12.3 中，我们说明在任何度量空间中，Heine-Borel 性质与 Bolzano-Weierstrass 性质是等价的，因此二者都可取作紧致性的定义。

如果你打算走向更抽象、更一般的层面，我们应当提醒你：在那里——即在拓扑学这一学科中——这两个概念并不等价。

并且紧致性通常只用 Heine-Borel 性质来定义。

---

<span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">**13.12.1 Bolzano-Weierstrass 性质（The Bolzano-Weierstrass Property）**</span>

实数的每个有界序列（bounded sequence）都有收敛子序列（convergent subsequence）。

这一命题在一般度量空间中是错误的。

> <span style="color:#7f8c8d;">TBB §13.12, p.597</span>
<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">**例 13.87：**</span>设 $X$ 是赋予离散度量（discrete metric）的无限集。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 例 13.87 是一个短小却致命的 counterexample（反例）：把任意无限集 $X$ 配上离散度量（discrete metric）——任意两个不同点的距离定义为 $1$，同点距离为 $0$——整个空间 $X$ 的 diameter（直径），即全体点对距离的上确界，只有 $1$。于是 $X$ 的一切子集都有界，甚至全空间都被一个半径大于 $1$ 的球整个套住（例如 $B(x_0,2)$ 就等于 $X$；而半径小于 $1$ 的球只含球心一个点）。但"有界"在这里彻底失灵：从互异点列 $\{x_n\}$ 里抓不出任何收敛子序列，因为任意两点的距离恒为 $1$，根本压不紧。
>
> 机制的第一性解释在于离散度量下"收敛"的判据苛刻到几乎不可能：一个序列收敛到 $x$，当且仅当它 eventually constant（最终常值）——存在指标 $N$，使所有 $n\ge N$ 的项都等于 $x$。理由只需一步：一旦 $x_n\neq x$，就有 $d(x_n,x)=1$，它永远落不进以 $x$ 为心、半径为 $1/2$ 的小球。因此任何由互异点组成的序列及其任何子序列都保持互异，每项离任何候选极限至少 $1$，收敛子序列无从谈起。具体取 $X=\mathbb N$，$x_n=n$ 即可：序列 $1,2,3,\dots$ 有界（直径 $1$）却无收敛子列，是有界不紧的最小标本。
>
> 这个反例的第一性含义是：compactness（紧致性）测的不是集合的"大小"，而是集合能否承受无穷的信息压缩。有界只做一次粗测量——所有点对距离的上确界有限，回答"装得下吗"；紧致却要求对任意精度 $\varepsilon>0$，都能用有限个半径为 $\varepsilon$ 的球盖住整个集合，回答"任意细的格子下能否用有限条信息概括"。离散度量的无限集在 $\varepsilon<1$ 时，每个点都得独占一个球，所需球数与点数一样多，无穷信息一丁点都压不掉——这就是"学院派的装得下，紧致却要求连细到 $\varepsilon$ 的格子都装得下但盖得住"的精确含义。
>
> 它与你 6.042J 里可数/不可数的直觉暗合但方向不同：$\mathbb N$ 配离散度量依然可数，却不可紧；可数性回答"有多少个点"，紧致性回答"点与点靠得有多近"，两个坐标轴互不决定。6.042J 的对角线论证教过你，某些无穷过程可以永远逃逸——对任意列出的实数表，总能对角构造出一个不在表中的实数；这里点列 $1,2,3,\dots$ 的逃逸更原始：度量本身把每个点隔成孤岛，任何子列都保持分离状态，无需自指构造就已注定不收敛。
>
> 用 CSAPP 的语言说：IEEE 754 的有限位模式只能精确表示有限个实数，这是表示层的有限性；离散度量的无限集里每个点都是半径为 $1/2$ 的开球（单点集），盖住无限个孤点需要无限个单点球，这是拓扑层的不可压缩性。区别在于前者是硬件寄存器宽度的计算资源约束，后者是度量几何强加的隔离结构。可复用的反例模板叫「恒距隔离法」：想证"某个看似足够的条件其实不够"时，给对象配上所有点两两相距某个固定正数 $\delta$ 的度量，让任何无穷子列都被隔离，收敛自动破产。这个反例还预告了定理 13.90：紧致 $\Rightarrow$ 有界成立，但反过来不成立，所以有界永远成不了紧致性的充分条件——这正是定义 13.88 改换门庭、改用列紧性质定义紧致的直接动机。

---

设 $\{x_n\}$ 是 $X$ 中任意一个由互异元素组成的序列。

则 $\{x_n\}$ 是有界的；事实上，整个空间 $X$ 的直径（diameter）仅为 1。

---

<span style="color:#7f8c8d">*（书页 598 — 例 13.87 的收尾，继而给出紧致性的定义。）*</span>

<span style="color:#7f8c8d">*（接上页：）*</span>……因此 $X$ 的每一个子集都是有界的。

但 $\{x_n\}$ 不可能有任何收敛子序列。$\square$

由此可知，$\mathbb{R}$ 的闭有界子集的一个特殊性质——即 Bolzano-Weierstrass 性质——在一般度量空间中失效。

该性质断言：若 $K \subset \mathbb{R}$ 是闭且有界（closed and bounded）的，则 $K$ 中每个点列的某个子序列收敛到 $K$ 中的某点。

我们把 $\mathbb{R}$ 的闭有界子集称为紧致的，但过去实际需要的主要正是这类集合的这一性质。

在一般度量空间中，自然的做法是认识到「闭且有界」不再扮演重要角色，而是把 Bolzano-Weierstrass 性质本身转变成「紧致」之含义的定义。

> <span style="color:#7f8c8d;">TBB §13.12, p.598</span>
<span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">**定义 13.88：**</span>度量空间中的集合 $K$ 称为紧致的（compact），当且仅当该集合具有 Bolzano-Weierstrass 性质。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 定义 13.88 把 compact set（紧致集）直接定义为具有 Bolzano-Weierstrass 性质：$K$ 中每个点列都有收敛到 $K$ 中某点的子序列。请把这句话拆成两个隐含要求来读：其一，任意点列都必须能抽出一个收敛子列，这是"压得紧"的部分；其二，子列的极限必须落回 $K$ 本身，这是"闭得严"的部分。两条要求被打包进同一条定义里，这正是它比"闭且有界"这个外形描述高明的地方。
>
> 两个具体例子能立刻让你看见这两个要求各自在防什么：$K=(0,1)$ 在 $\mathbb R$ 中不是紧集，因为点列 $x_n=1/n$ 收敛（自然有收敛子列），但极限 $0\notin(0,1)$，第二条失败——边界上有洞，点列从洞里漏出去；$K=[0,\infty)$ 也不是紧集，因为点列 $x_n=n$ 的任何子列都趋向无穷，在 $\mathbb R$ 中没有收敛极限，第一条失败——集合无界，点列从无穷远处逃逸。对照之下 $K=[0,1]$ 两条都满足，是紧集。这两个失败模式恰好对应定理 13.90 的两半：紧致 $\Rightarrow$ 闭，堵住"漏出去"；紧致 $\Rightarrow$ 有界，堵住"逃到无穷"。
>
> 这是定义重构的一课：教材不肯再用 $\mathbb R$ 上"闭且有界"这样的描述性写照来定义，因为作为定义条款，它在一般度量空间里既非必要也非充分（对照例 13.87）。说"非必要"是指：列紧性自己就会推出闭与有界，不必把"闭且有界"写进定义当额外要求；说"非充分"是指：离散度量的全空间闭且有界，却不列紧。教材做的是一个反客为主的升格——让"收敛子序列"这一本质属性本身当定义，把实直线上的具体刻画（闭且有界）降级为推论。逻辑方向被整个调转：原先的定理说"闭且有界 $\Rightarrow$ 有收敛子列"，新定义把"有收敛子列"立为公理，再反手证明"紧致 $\Rightarrow$ 闭且有界"（定理 13.90）。
>
> 这个把性质转成定义的手法你并不陌生。TBB 把 Cauchy 判别升格为完备性：在 $\mathbb R$ 上"Cauchy"只是收敛的必要条件，升格后"凡 Cauchy 列收敛"成为完备空间的公理。6.042J 把"存在到 $\mathbb N$ 的双射"升格为可数：不定义成"能一个一个列出来"的模糊直觉，而定义成双射存在性，对角线论证等性质随后全变成定理。Strang 把线性无关加生成升格为基：先用这两个操作性质定义基，再证"所有基大小相同"从而维数良定义。共同模板是「反客为主的升格法」：第一步，挑一个不依赖额外结构的核心性质；第二步，把它当公理；第三步，把其余性质降级为定理来证。区别在于：线性代数里基必须同时声明"无关"与"生成"两个条件，缺一不可；而紧致只声明"列紧"这一个条件，"闭"与"有界"自动跟出来——因为度量空间里的序列与极限机制已经暗中携带了边界信息与延展信息，这是度量结构比裸集合结构更富饶之处。
>
> CSAPP 给过你同款思维训练：IEEE 754 拒绝"十进制近似"这种外形描述，用位模式（bit pattern）与舍入规则定义浮点数，因为只有行为规则才经得起实现与验证；区别是位模式是人为约定的编码，列紧性却是被后续定理反推出来的必然选择。定义 13.88 同理：紧致不是"长得像闭区间"的外形，而是"任何点列都能被压出收敛到自身的子列"这套禁得起怎样折腾的规则。对你这种喜欢追问"为什么这么定义"的读者，这是理解抽象分析的关键开关：定义的价值不在它画了什么样的像，而在它承诺了什么样的推理接口——输入任意点列，输出一个极限留在 $K$ 内的收敛子列。后续定理（连续函数把紧集映成紧集、紧集上连续函数一致连续）都只是这个接口的稳定输出。

---

所谓 Bolzano-Weierstrass 性质，即 $K$ 中每个点列都有收敛到 $K$ 中某点的子序列。

若 $(X, d)$ 是度量空间，且集合 $X$ 本身是紧致的（即 $X$ 具有 Bolzano-Weierstrass 性质），则我们称该度量空间是紧致的（compact）。

让我们首先指出每个紧致集都必定具备的一些性质。

其中第一条已留作习题 13.12.2（Exercise 13.12.2）。

> <span style="color:#7f8c8d;">TBB §13.12, p.598</span>
<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">**定理 13.89：**</span>紧致性是拓扑性质（topological property，即在同胚下保持的不变量）。

> <span style="color:#7f8c8d;">TBB §13.12, p.598</span>
<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">**定理 13.90：**</span>设 $K$ 是度量空间 $(X, d)$ 中的紧致集。

则 $K$ 满足以下四条：

&nbsp;&nbsp;1. $K$ 是闭的（closed）。

&nbsp;&nbsp;2. $K$ 是有界的（bounded）。

&nbsp;&nbsp;3. $K$ 是完备的（complete）。

&nbsp;&nbsp;4. $K$ 是可分的（separable）。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 定理 13.90 一次性给出紧致集的四条性质——闭、有界、完备、可分，证明里藏着四把可复用的剑。先回顾前提：这里的紧致是列紧（每列都有收敛子列），四条性质全部由列紧推出，所以四把剑本质上是把“子列”这个工具分别劈向极限、距离、Cauchy 列和覆盖四种目标。逐把拆开看机制，每把剑都配一个可命名的模板。
>
> 闭性这把剑可命名为封口。设 $(x_n)$ 在 $K$ 中收敛到 $x$，要证 $x\in K$。列紧性保证 $(x_n)$ 有子列收敛到 $K$ 中某点 $y$；而收敛序列的任意子列只能收敛到同一个极限，所以 $x=y\in K$。这把剑的直觉是：极限唯一，子列逃不掉，极限点被锁在 $K$ 内。为什么子列极限一定等于全列极限？因为子列下标 $n_k\ge k$，只要 $k$ 大到超过收敛定义里的 $N$，子列项就同样落在极限的任意小邻域内。
>
> 有界性用反证法，可命名为放逐法：若 $K$ 无界，则对每个 $N$ 存在 $x_N\in K$ 使 $d(x_0,x_N)>N$。任何子列 $(x_{N_k})$ 都满足 $d(x_0,x_{N_k})>N_k\to\infty$，于是子列无界；而收敛序列必有界（极限附近用三角不等式 $d(x_0,x_n)\le d(x_0,L)+d(L,x_n)$ 控制尾部，前有限项取最大），所以任何子列都不能收敛。这把剑的模板是：假设存在任意远的点，再证明它毒死一切子列。
>
> 完备性这把剑可命名为子列锚定法：$K$ 中的 Cauchy 列 $(x_n)$ 由列紧性抽出收敛子列 $(x_{n_k})\to L$。习题 13.8.6 的引理正是：有收敛子列的 Cauchy 列本身收敛到同一极限。机制是半 $\varepsilon$ 夹逼：对任意 $\varepsilon>0$，先由 Cauchy 性取 $N_1$ 使 $m,n\ge N_1$ 时 $d(x_m,x_n)<\varepsilon/2$；再由子列收敛取 $k$ 足够大使 $n_k\ge N_1$ 且 $d(x_{n_k},L)<\varepsilon/2$；于是对任意 $n\ge N_1$，$d(x_n,L)\le d(x_n,x_{n_k})+d(x_{n_k},L)<\varepsilon$。子列像一根钉子，把整个 Cauchy 列钉在极限上：Cauchy 性负责让同批项彼此靠近，子列负责提供一根伸向极限的绳子。
>
> 可分性最精巧，用的是贪婪选点法。先定义有限 $\varepsilon$-网：$K$ 中有限个点 $F$，使 $K\subseteq\cup_{x\in F}B(x,\varepsilon)$，即任意点离 $F$ 中某点距离小于 $\varepsilon$。反设对某个 $\varepsilon$ 没有有限 $\varepsilon$-网，就递推地选 $x_1\in K$，再选 $x_n\notin\cup_{i\lt n}B(x_i,\varepsilon)$。选择规则保证任意 $i\lt j$ 有 $d(x_i,x_j)\ge\varepsilon$，所以这个序列没有 Cauchy 子列（Cauchy 列要求尾部任意两项距离趋于零，而这里尾部任意两项都保持 $\varepsilon$ 以上）。这与 CLRS 的贪心算法同构：每步抓当前能抓到的、离已选点都至少 $\varepsilon$ 远的点，贪心选择性质由已选点两两 $\varepsilon$-分离这个循环不变量保证——初始时已选集合两两分离，每次插入新点后仍两两分离，正像 CLRS 用循环不变量证明贪心正确性；递推定义无穷序列又是 6.042J 的归纳构造（给定了 $x_1,\ldots,x_{n-1}$ 就唯一决定下一步的选法）。具体到 $[0,1]$ 取 $\varepsilon=1/2$，贪婪选点停在 $\{1/4,3/4\}$：$B(1/4,1/2)$ 与 $B(3/4,1/2)$ 已盖满 $[0,1]$，选不出第三点。紧致性正是保证这个贪婪过程对每个 $\varepsilon$ 都必然停机。
>
> 停机之后还要把有限网缝成可数稠密集：对每个 $n$ 取 $1/n$-网 $F_n$，并集 $\cup_n F_n$ 是可数多个有限集的并，由 6.042J 的可数性（$\mathbb{N}\times\mathbb{N}$ 枚举）仍是可数的，且对任意 $x\in K$、任意 $n$ 都有 $F_n$ 中的点离 $x$ 不到 $1/n$，所以稠密。教材第 599 页把紧致推出存在有限 $\varepsilon$-网单独标注为有独立价值的点子：这套边挑边盖的构造直接通向 §13.12.4 的全有界性（每个 $\varepsilon$ 都有有限 $\varepsilon$-网）。读懂这一步，你就握住了紧致约等于列紧加全有界这条通往泛函分析的核心直觉的一半。

<span style="color:#2471a3;">**[proof]**</span> <span style="color:#c0392b">**证明。**</span>若 $K$ 具有 Bolzano-Weierstrass 性质，则 $K$ 中每个收敛到某点 $z$ 的点列都必须满足 $z \in K$。

于是，$K$ 必定是闭的。

其次，$K$ 必定有界。

若不然，则对每个整数 $N$ 与任一固定点 $x_0$，必有点 $x_N \in K$ 满足 $d(x_0, x_N) > N$。

这构造出一个每个子序列都无界、从而不可能有收敛子序列的序列。

因此，若 $K$ 具有 Bolzano-Weierstrass 性质，则 $K$ 不可能无界。

再次，$K$ 必定完备。

若 $\{x_n\}$ 是 $K$ 中的 Cauchy 序列，则由 Bolzano-Weierstrass 性质，存在收敛到某点 $z \in K$ 的子序列 $\{x_{n_k}\}$。

但任何具有收敛子序列的 Cauchy 序列，其本身收敛（习题 13.8.6）。

最后，让我们证明 $K$ 是可分的。

我们只需在度量空间 $(K, d)$ 中工作。

假设 $K$ 不可分。

则对某个 $\varepsilon > 0$，不存在有限点集 $x_1, x_2, x_3, \dots, x_p$，使得
```math
K \subset \bigcup_{i=1}^{p} B(x_i, \varepsilon).
```

<span style="color:#7f8c8d">*（证明在此处被页边界截断，下一页接续。）*</span>


<!-- ===== W8 ===== -->

<span style="color:#7f8c8d">书页 599 · §13.12</span>

<span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">§13.12　紧致性（Compactness）</span>

（本节为前一定理之证明的延续部分。）

<span style="color:#2471a3;">**[proof]**</span> **证明（续）**

（此结论可由 Exercise 13.7.1 推出。）

于是我们可在 $K$ 中选取一列点 $x_1, x_2, x_3, \ldots$，满足性质：

```math
x_n \notin \bigcup_{i=1}^{n-1} B(x_i, \varepsilon).
```

这样的一列点不可能含有 Cauchy 子序列，

因为对所有 $n > M$ 都有 $d(x_N, x_m) > \varepsilon$。

因而它也没有收敛子序列。

由于这与 Bolzano-Weierstrass 性质相矛盾，

故集合 $K$ 必是可分的（separable）。$\square$

---

<span style="color:#2471a3;">**[note]**</span> <span style="color:#1e8449">**注（Note）**</span>　在我们的证明中遇到一个具有独立价值的技术思想。

若 $K$ 紧致，则已证得它具有一种强意义上的有界性。

给定任意半径 $\varepsilon$，我们都能用有限多个该半径的球覆盖 $K$。

更确切地说，对每个 $\varepsilon > 0$，存在 $n \in \mathbb{N}$ 与开球 $B(x_1, \varepsilon), \ldots, B(x_n, \varepsilon)$ 使得：

```math
K \subset \bigcup_{i=1}^{n} B(x_i, \varepsilon).
```

集合 $\{x_1, x_2, \ldots, x_n\}$ 称为 $K$ 的一个 $\varepsilon$-网（ε-net, epsilon-net）。

它具有这样的性质：若 $x \in K$，则存在某个 $i$ 使得 $d(x_i, x) < \varepsilon$。

显然，这比有界性（boundedness）更强。

不仅 $K$ 包含在某个大球中（即有界），

而且 $K$ 包含在有限多个任意给定直径的球之并中。

这一点将在 §13.12.4 中发挥作用。

---

我们或许曾希望定理 13.90 中列出的那些性质，

即紧致集的各种显然必要条件，同时也是充分条件。

定理 13.89 给出了一个线索。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 定理 13.89 说紧致性是拓扑性质——在同胚（homeomorphism，连续双射且逆也连续）下保持不变。先把为什么成立的机制拆开：设 $f:K\to f(K)$ 连续，$K$ 紧致，任取 $f(K)$ 的开覆盖 $\{U_\alpha\}$。连续性的定义正是开集的原像是开集，所以 $\{f^{-1}(U_\alpha)\}$ 是 $K$ 的开覆盖；由 $K$ 紧致，抽出有限子覆盖 $f^{-1}(U_{\alpha_1}),\ldots,f^{-1}(U_{\alpha_n})$；再映回去，$U_{\alpha_1},\ldots,U_{\alpha_n}$ 盖住 $f(K)$。这招可命名为原像拉回法：把像空间的覆盖沿连续映射拉回定义域，用定义域的紧致性收成有限，再推回像空间。注意这里只用了连续性，所以连续映射也保持紧致性；同胚要求逆也连续，是为了两个空间互为对方的像，紧致性才能双向保持，这是拓扑性质的标准含义。
>
> 现在看它如何剔除有界这个伪候选人。若用闭且有界当紧致的定义，问题出在有界性依赖具体度量，而拓扑性质只依赖开集族。标准例子：在通常度量 $d(x,y)=|x-y|$ 上定义等价度量 $d'(x,y)=\frac{d(x,y)}{1+d(x,y)}$。它产生完全相同的开集（$d'\le d$，且 $d$ 小时 $d'$ 与 $d$ 同阶），因此收敛序列、开集、闭集全部不变；但 $d'$ 把整条实数轴压缩到直径 $1$ 以内，例如 $d'(0,10^6)=\frac{10^6}{1+10^6}\approx 0.999999$。于是 $\mathbb{R}$ 在 $d'$ 下有界，任何集合都有界，有界彻底失效。这就是习题 13.2.1 那类等价度量变体的杀伤力：同样的拓扑、不同的尺子，有界性整体蒸发。另一个更直观的例子：$(0,1)$ 与 $\mathbb{R}$ 同胚（$f(x)=\tan(\pi(x-1/2))$ 连续双射且反函数 $\arctan$ 连续），前者有界后者无界，可见有界连同胚都扛不住。
>
> 这彻底解释了为什么必须另选定义：紧致性要能在捏成橡皮泥但不撕破、不粘连的同胚变形下幸存，而有界会被这么一捏就搓变形。用你尚未学拓扑学的脚手架式直觉：在同胚眼中，距离的绝对大小毫无意义，只有收敛或不收敛、覆盖得住或盖不住这类拓扑语才保留。从 6.042J 的视角看，度量等价和同胚都是等价关系：前者按产生相同开集把度量划分成等价类，后者按存在保持拓扑结构的双射把空间划分成等价类；紧致性是等价类的不变量——同一等价类里所有成员共享，这正是“拓扑性质”在 6.042J 语言里的定义。这与 Strang 里相似变换 $A\mapsto P^{-1}AP$ 保持谱是同一个思维：特征值不变是因为相似不改变特征多项式 $\det(\lambda I-A)$，紧致不变是因为同胚不改变开覆盖结构；区别在于相似是基变换，同胚是连续形变，谱是相似不变量，紧致性是同胚不变量。
>
> 这也呼应 §13.12 引言你对完备性的类比——完备性关心的是收敛，有界性关心的只是尺度。将来学拓扑时，教材那句 Bolzano-Weierstrass 与 Heine-Borel 不再等价的预言会兑现：在更一般（非度量化）的拓扑空间里，列紧与紧致分道扬镳。现在你只需记住：紧致是拓扑的，有界不是，这就是为什么定义必须落在前者而非后者。

尽管紧致性是一个拓扑性质（topological property），有界性却不是。

一个简单的例子也能说明问题。

考虑实直线 $\mathbb{R}$，但装备一个与通常度量不同的度量，

即习题 13.2.1(c) 或 13.2.1(d) 中的度量。

由于该度量与通常度量等价，$\mathbb{R}$ 的每个闭子集都具有定理 13.90 的全部性质。

这里唯一的区别是，在新度量下所有集合都是有界的。

但在任一度量下，$\mathbb{R}$ 中仅有的紧致闭子集，

恰是在通常度量下那些有界的集合。

---

<span style="color:#7f8c8d">*（本页其余部分为 §13.12 习题区，含习题 13.12.1–13.12.4，按约定跳过：证明紧致集合的每个闭子集仍紧致、证明紧致性为拓扑性质、证明度量空间的每个有限子集紧致、并判别离散度量空间中的紧致子集等。）*</span>

---

<span style="color:#7f8c8d">书页 600</span>

<span style="color:#7f8c8d">*（本页前半部分为 §13.12 习题区，按约定跳过。其中习题包括：13.12.5 证明收敛序列连同其极限构成的集合紧致；13.12.6 证明 $\mathbb{R}^n$ 中子集紧致当且仅当闭且有界；13.12.7 证明 Hilbert 立方体是 $\ell_2$ 的紧致子集；13.12.8 证明 $C[a,b]$ 中的单位球面非紧致；13.12.9 关于紧致集上最近点的存在性；13.12.10 关于两闭集的最近点存在性；13.12.11 证明装备乘积度量的两个紧致度量空间之积仍为紧致度量空间。）*</span>

---

<span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">§13.12.2　紧致集上的连续函数（Continuous Functions on Compact Sets）</span>

关于 $\mathbb{R}$ 或 $\mathbb{R}^n$ 的紧致子集上连续函数的许多标准定理，

都可推广到一般度量空间。

若 $f : [a,b] \to \mathbb{R}$ 连续，则：

1. $f$ 在 $[a,b]$ 上一致连续（uniformly continuous）。

2. $f$ 有界。

3. $f$ 取得其最大值与最小值。

现在我们问，对于连续函数 $f : X \to Y$，其中 $X$ 为紧致度量空间，

这些结论的对应物（analogue）是什么？

> <span style="color:#7f8c8d;">TBB §13.12, p.600</span>

<span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">**定义 13.91**　若 $f : (X, d) \to (Y, e)$，且对每个 $\varepsilon > 0$ 存在 $\delta > 0$，

使得只要 $d(x, x_0) < \delta$ 就有 $e(f(x), f(x_0)) < \varepsilon$，

则称 $f$ 在 $X$ 上一致连续。</span>


<!-- ===== W9 ===== -->

<span style="color:#7f8c8d">书页 601（§13.12 紧致性 Compactness 续，接上页）。</span>

# §13.12 紧致性 Compactness（续）

<span style="color:#2471a3;">**[section]**</span> 本节延续 §13.12 关于紧致性及其在连续函数上应用的内容，重点处理一致连续（uniform continuous）与像集紧致性。

我们首先处理一致连续。正如对定义在 $\mathbb{R}$ 的紧致子集上的连续函数所证明的那样，我们要证明定义在紧致空间上的连续函数必定一致连续。由于这些证明并不需要新的方法，它们被留作习题 13.12.17 与 13.12.18。

> <span style="color:#7f8c8d;">TBB §13.12, p.601</span>
<span style="color:#c0392b">**[theorem]**</span> **定理 13.92**：若 $X$ 紧致且 $f : X \to Y$ 连续，则 $f$ 一致连续。

<span style="color:#2471a3;">**[section]**</span> 接下来我们推广那个基本定理：它断言定义在紧致区间 $[a, b]$ 上的连续实值函数在 $[a, b]$ 上取得绝对最大最小值。若记得对于连续函数 $f : [a, b] \to \mathbb{R}$，其像集 $f([a, b])$ 必为 $\mathbb{R}$ 中的一个紧致区间，我们便能预料这一结论在一般度量空间中会具何种形式。

> <span style="color:#7f8c8d;">TBB §13.12, p.601</span>
<span style="color:#c0392b">**[theorem]**</span> **定理 13.93**：若 $f : X \to Y$ 连续且 $X$ 紧致，则集合 $f(X)$ 在 $Y$ 中紧致。

关于上述定理的进一步推广——即连续、一一且映上的映射为同胚（homeomorphism）等结论，连同紧致空间自映射迭代等性质，均在本页习题中体现。

<span style="color:#7f8c8d">*（本页其余部分为 §13.12 习题 13.12.12–13.12.20 区，涉及离散度量下的连续性、压缩映射的一致连续性、距离函数 $f(x)=\operatorname{dist}(x,A)$ 的一致连续性、一致连续函数保持 Cauchy 序列、紧致空间上连续函数的一致连续性、像集紧致性、紧致空间上连续双射为同胚、自映射迭代集 $X_1=f(X), X_{n}$ 的紧致不动性等，按约定跳过。）*</span>

<span style="color:#7f8c8d">书页 602（§13.12 末 + §13.12.3 The Heine-Borel Property 前段）。</span>

<span style="color:#2471a3;">**[section]**</span> 本页先是本节的尾题，随后进入拓展小节 §13.12.3 关于 Heine-Borel 性质的讨论。

<span style="color:#7f8c8d">*（本页起始部分为 §13.12 习题 13.12.21–13.12.22 区：其中 13.12.21 定义弱压缩（weak contraction），要求证明其一致连续、未必为压缩、紧致时有唯一不动点、完备但非紧致时的重要性，并与 Banach 不动点定理比较（提示见 Note 360）；13.12.22 要求表述并证明 Dini 定理（定理 9.24）在紧致度量空间上连续实值函数序列的推广。均按约定跳过。）*</span>

# §13.12.3 Heine-Borel 性质（The Heine-Borel Property）

<span style="color:#2471a3;">**[note]**</span> <span style="color:#7f8c8d">*（本节为拓展小节，可省略。）*</span>

我们回顾：在实数轴上，紧致集可以用几种不同的方式刻画。对于紧致性论证的目的而言，其中最有用的刻画之一是 Heine-Borel 性质，即闭且有界集的任何由一族开区间构成的覆盖，都能约化为有限子覆盖。这一性质在一般度量空间中同样可用。不过它不再对一切闭且有界集成立，而是对所有紧致集成立——正如我们在前面各节中所定义的紧致集那样。

> <span style="color:#7f8c8d;">TBB §13.12, p.602</span>
<span style="color:#2471a3;">**[definition]**</span> **定义（开覆盖 open cover）**：设 $X$ 为度量空间，$K \subset X$。一族集合 $\mathcal{U}$ 若满足

```math
K \subset \bigcup_{U\in\mathcal{U}} U,
```

则称 $\mathcal{U}$ 为 $K$ 的**开覆盖**，其中每个 $U \in \mathcal{U}$ 均为开集。

> <span style="color:#7f8c8d;">TBB §13.12, p.602</span>
<span style="color:#c0392b">**[theorem]**</span> **定理 13.94**：设 $K$ 为度量空间 $X$ 中的集合，则下列条件彼此等价。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 紧致性在这里呈现第三种相貌：除你熟悉的有界闭（在 $\mathbb{R}^n$ 中有效）与每列都有收敛子列（列紧，sequential compactness）之外，现在多了 Heine-Borel 性质——任一开覆盖都能约出有限子覆盖。三种说法在一般度量空间里都不等价于有界闭，却又彼此等价，这正是定理 13.94 的价值：紧致性不是某个偶然的度量巧合，而是一种稳定的结构。
>
> 为什么三种相貌会合一？用第一性原理追问，紧致性的本质是有限性：无穷个开集可以缩减成有限个子覆盖，无穷点列可以凝聚出一个极限。一个具体的反例先划清边界：在无限集上装离散度量 $d(x,y)=1\ (x\ne y)$，每个单点集 $\{x\}$ 都是开集，全体单点构成开覆盖却没有有限子覆盖（少一个点就盖不住那个点）；序列 $(x_n)$ 中任意两项距离恒为 $1$，没有收敛子列；同时每个子集都有界（直径不超过 $1$）且闭。可见闭加有界在一般度量空间里完全不够，紧致必须另立门户。放回 CSAPP 语境很好举一反三：缓存（cache）只有有限个槽位，却要服务无穷的地址空间；紧致集正像一个永不抖动的缓存——任意开覆盖（无穷多个访问需求）总能找到有限子覆盖（有限工作集）兜住。但区别要讲清楚：缓存的有限容量可能装不下工作集而抖动，浮点的有限位模式只能保证相对误差（指数每加一，间距翻倍），而紧致的有限 $\varepsilon$-网保证的是均匀的绝对精度。
>
> 证明的骨架可命名为逐层有限化法，分两层把无穷逐层化成有限。第一层用 Lindelöf 定理把任意开覆盖缩成可数子覆盖，机制是有理半径贴片：由可分性取可数稠密集 $\{q_n\}$，对覆盖中每个点 $x$，找一个包含 $x$ 的开集 $U$，再选一个以某 $q_n$ 为心、有理数 $1/m$ 为半径的球夹在 $x$ 与 $U$ 之间；所有这种球只有可数个（下标 $(n,m)\in\mathbb{N}\times\mathbb{N}$，6.042J 的可数性），每个球再配一个包含它的 $U$，就得到可数子覆盖。第二层靠 Bolzano-Weierstrass 性质把可数子覆盖坍缩成有限：若 $\{U_n\}$ 无有限子覆盖，则每个 $n$ 都可取 $x_n\in K\setminus(U_1\cup\cdots\cup U_n)$；列紧性抽出 $x_{n_k}\to x\in K$，而 $x\in U_N$ 对某个 $N$ 成立，于是当 $n_k>N$ 时 $x_{n_k}\in U_N\subseteq U_1\cup\cdots\cup U_{n_k}$，与 $x_{n_k}$ 的选法矛盾。这就是反证序列法：假设没有有限子覆盖，就构造一条永远逃出前 $n$ 个覆盖成员的序列，再用极限把它逼进某个成员，自相矛盾。
>
> 这套任意到可数再到有限的逐层坍缩，与 6.042J 存在性证明里的有限化技巧同气连枝：归纳把无穷多条命题压成基例加归纳步两步，抽屉原理把无穷只鸽子压进有限个盒子，这里则把无穷覆盖压成有限证书。Strang 的矩阵迭代也有同款有限证书思维：Jacobi 迭代 $x^{(k+1)}=Mx^{(k)}+c$ 收敛，只需一个数——谱半径 $\rho(M)<1$——作为证书，因为误差 $e_k=M^ke_0$ 的范数按 $\rho(M)^k$ 衰减；紧致性则给开覆盖发一张有限子覆盖证书。区别在于：谱半径证书管的是线性迭代的全程收敛，而列紧只保证子列凝聚，要把子列升级为全列收敛还需 Cauchy 或压缩条件。这个统一骨架支撑着 §13.12 后半的一切论证。

---

1. （Bolzano-Weierstrass 性质）$K$ 紧致。
2. （Heine-Borel 性质）$K$ 的每个开覆盖都能约化为有限子覆盖。

<span style="color:#2471a3;">**[proof]**</span> **证明**：全程可假设 $X = K$。设 $K$ 满足条件 (2)，并设 $\{x_n\}$ 为 $K$ 中的序列。对每个 $N \in \mathbb{N}$，令 $A_N = \{x_n : n \geq N\}$，并令 $U_N = X \setminus A_N$。注意 $\{U_N\}$ 形成一列递增的开集，且对任何 $N$ 都有 $U_N \ne K$。特别地，每个集合 $U_N$ 都是开集，并且 $\{U_N\}$ 的任何有限子族都不覆盖 $K$。由于 $K$ 满足条件 (2)，故 $\{U_N\}$ 不能构成 $K$ 的开覆盖，从而有

```math
\bigcup_{N=1}^{\infty} U_N \ne X;
```

也就是说，

```math
\bigcap_{N=1}^{\infty} A_N \ne \varnothing.
```

（证明后续部分将利用这一非空交集与紧致性的关系，续于下页。)


<!-- ===== W10 ===== -->

<span style="color:#7f8c8d">书页 603 · §13.12 Compactness（紧致性）· 接上页的定理证明尾部</span>

<span style="color:#c0392b">**§13.12　紧致性（Compactness）**</span>

<span style="color:#2471a3;">**[proof]**</span> **（上页定理的证明结尾）**

设 $x_0 \in \bigcap_{N=1}^{\infty} A_N$。由集合族 $A_N$ 的定义直接可知，$x_0$ 是序列 $\{x_n\}$ 的某个子序列（subsequence）的极限。这就完成了 (2) ⇒ (1) 的证明。

现在假设 $K$ 满足条件 (1)。我们需要从定理 13.90 回忆起 $K$ 是可分的（separable），因为要证明 $K$ 具有 Heine-Borel 性质需要用到这一点。现在设 $\mathcal{U}$ 是 $X$ 的一个开覆盖（open cover）。由 Lindelöf 定理（Lindelöf's theorem，见习题 13.12.30）可知，$\mathcal{U}$ 可被缩减为一个可数子覆盖（countable subcover）$\{U_1, U_2, U_3, \ldots\}$。

我们现在证明这个子覆盖还可进一步被缩减为一个有限子覆盖（finite subcover）。若不然，则对每个 $N \in \mathbb{N}$ 都存在 $x_N \in X \setminus \bigcup_{i=1}^{N} U_i$，因为否则集族 $\{U_1, U_2, \ldots, U_N\}$ 就会覆盖 $X$。由于 $X$ 具有 Bolzano-Weierstrass 性质（Bolzano-Weierstrass property），集合 $\{x_1, x_2, \ldots\}$ 有一个聚点 $x_0$。但 $X = \bigcup_{i=1}^{\infty} U_i$，所以存在 $j \in \mathbb{N}$ 使得 $x_0 \in U_j$。这意味着对无穷多个 $i \in \mathbb{N}$ 都有 $x_i \in U_j$。这是不可能的，因为我们对点 $x_N$ 的选取方式决定了当 $N \geq j$ 时 $x_N \in X \setminus U_j$。这一矛盾说明集族 $U_1, U_2, \ldots$ 可被缩减为有限子覆盖，从而完成了 (1) ⇒ (2) 的证明。$\square$

<span style="color:#7f8c8d">*（本页其余部分为 §13.12 的习题区，覆盖习题 13.12.23–13.12.30，按约定跳过。）*</span>

---

<span style="color:#7f8c8d">书页 604 · §13.12 习题续 + §13.12.4 Total Boundedness（全有界性）</span>

<span style="color:#7f8c8d">*（本页开头为 §13.12 的习题区，覆盖习题 13.12.31–13.12.34，按约定跳过。）*</span>

<span style="color:#c0392b">**§13.12.4　全有界性（Total Boundedness）**</span>

<span style="color:#7f8c8d">**[note]**</span> 本节为拓展小节，可省略（may be omitted）。

在 $\mathbb{R}^n$ 中，一个集合是紧致的（compact）当且仅当它既闭又有界。我们已看到，这一说法在一般的度量空间中是不成立的。与其完全抛弃这个想法，我们仍可追求这样一种思路：对集合而言，若它在某种更强的意义下是闭的且"有界的"，或许就足以保证它是紧致的。

关键的想法已经出现在定理 13.90 的证明之中。在那里我们证明了：若 $X$ 是紧致的，那么对每个 $\varepsilon > 0$ 都存在一个 $\varepsilon$-网（$\varepsilon$-net），即存在一个有限集 $\{x_1, x_2, \ldots, x_n\} \subset X$，使得球的有限集族 $\{B(x_i, \varepsilon)\}$ 覆盖 $X$。当一个空间 $X$ 对每个 $\varepsilon > 0$ 都拥有 $\varepsilon$-网时，我们就说 $X$ 是全有界的（totally bounded）。我们将其正式表述如下。

> <span style="color:#7f8c8d;">TBB §13.12, p.604</span>
<span style="color:#2471a3;">**[definition]**</span> **定义 13.95（Definition 13.95）：**设 $X$ 是度量空间。我们说集合 $S \subset X$ 是全有界的，若对每个 $\varepsilon > 0$ 都存在一个有限集 $\{x_1, x_2, \ldots, x_n\} \subset X$，使得

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> total boundedness（全有界）给出的是一副"逐尺度有限化"的骨架：对每个 $\varepsilon>0$，都存在有限个 $\varepsilon$-球盖住整个集合，这组球心就构成一个 $\varepsilon$-net（$\varepsilon$-网）。先看最朴素的机制：闭区间 $[0,1]$ 在通常度量下是全有界的，对任意 $\varepsilon$，取球心 $0,\varepsilon,2\varepsilon,\dots,k\varepsilon$（直到覆盖住 $1$），球数不超过 $\lceil 1/\varepsilon\rceil+1$，永远有限。反过来，无限维空间里的单位闭球会打破这个直觉：在平方可和序列空间 $\ell^2$（所有满足 $\sum x_i^2<\infty$ 的实数列）里，标准单位向量 $e_1,e_2,\dots$ 两两距离为 $\sqrt{2}$，当 $\varepsilon<\sqrt{2}/2$ 时一个 $\varepsilon$-球至多装下一个 $e_i$（否则两个 $e_i$ 同球，距离不超过 $2\varepsilon<\sqrt{2}$，矛盾），于是有限个球只能盖住有限个 $e_i$，单位闭球有界却全无界。这就是"有界"与"全有界"的分水岭：有界只保证存在一个大球包住全体，全有界则要求在任意小的尺度上都能用有限个球逼近，是"可被有限采样"的均匀逼近性质。
>
> 定理 13.97 把本章前面的成果浓缩成一句漂亮话：度量空间紧致 $\Longleftrightarrow$ 完备且全有界。用第一性原理拆开看：完备性负责"极限一定存在"，任何 Cauchy sequence（柯西列，指项与项之间的距离随下标增大而趋于零的序列）的极限不会跑出集合；全有界负责"总有有限覆盖"，让无穷多个候选者能被有限个球分层管理。二者合起来，可以看作有限维里"有界闭必紧致"（Heine–Borel 定理）在无限维的正确替身：在无限维里，有界闭不再自动给出紧致性，必须把"有界"加强成"全有界"，把"闭"加强成"完备"。
>
> 证明里蕴含一个值得命名并反复使用的模板：diagonal extraction（对角线抽取子列）。机制是"逐层套叠、沿对角线取公共子列"：第一层按 $\varepsilon=1$ 的有限网选出一个装了无穷多项的球，取出子列；第二层按 $\varepsilon=1/2$ 的网在这个子列里再选一个球，取出更细的子列；依此类推。令 $x^{(k)}$ 表示第 $k$ 层子列，把 $x^{(k)}_k$（第 $k$ 层的第 $k$ 项）拼起来，就得到对角线子列；当 $m,n\ge N$ 时，$x^{(m)}_m$ 与 $x^{(n)}_n$ 都落在第 $N$ 层被选中的那个 $1/N$-球里，距离不超过 $2/N$，所以它是 Cauchy 列。注意这与 6.042J 的 Cantor 对角线论证形似而神不同：Cantor 是对角线上"逐位取反"构造出一个不在任何一行里的新对象，本质是反证构造；这里是对角线"从第 $k$ 行取第 $k$ 项"的抽取选择，本质是子列选取。二者共同的底座是 6.042J 的可数性：指标集 $\mathbb{N}$ 可数，才允许把层层子列排成一个方阵。
>
> 这个手法在 §13.14 定理 13.116 的证明（对点列与斜率各取一次子列）、以及你日后读的泛函分析（研究无穷维空间上算子的分析学）里会反复出现，值得现在就先养成肌肉记忆。它与 CSAPP 的浮点网格有一处值得对比：IEEE754 在每个尺度上的可表示数都是有限的，但相邻可表示数的间距随指数增长，是"相对精度"网格；$\varepsilon$-网要求的是每个固定绝对尺度上的有限覆盖，是"绝对精度"网格。Strang 里把 $[0,1]$ 离散成有限差分格点之所以可行，正是全有界性保证的：有限采样可以无限加密。这是同一个"逐尺度有限化"思想在离散计算与连续分析之间的桥梁。

---

```math
S \subset B(x_1, \varepsilon) \cup B(x_2, \varepsilon) \cup \cdots \cup B(x_n, \varepsilon).
```

我们还可以用 Cauchy 序列来刻画全有界性。注意，下述定理的表述语言与 Bolzano-Weierstrass 性质的表述语言十分接近。

> <span style="color:#7f8c8d;">TBB §13.12, p.604</span>
<span style="color:#2471a3;">**[theorem]**</span> **定理 13.96（Theorem 13.96）：**度量空间 $X$ 是全有界的，当且仅当它的每个序列都拥有一个 Cauchy 子序列。


<!-- ===== W11 ===== -->

<span style="color:#7f8c8d">书页 605 —— §13.12 Compactness（紧致性），承接上一页证明的中段。</span>

上一页正在证明的为定理 13.96（其精确表述见书页 604，此处是该证明的收尾部分）。

<span style="color:#2471a3;">**[proof]**</span> **证明（续，定理 13.96）。** 若假设 $X$ 不是全有界（totally bounded），则存在某 $\varepsilon > 0$，使得找不到有限点集 $x_1, x_2, x_3, \ldots, x_p$ 满足
```math
K \subset \bigcup_{i=1}^{p} B(x_i, \varepsilon).
```
于是我们可以在 $K$ 中选出一列点 $x_1, x_2, x_3, \ldots$，使其满足
```math
x_n \notin \bigcup_{i=1}^{n-1} B(x_i, \varepsilon).
```
这样的序列不可能含有 Cauchy 子序列（Cauchy subsequence），因为对一切满足 $m > n$ 的项都有
```math
d(x_n, x_m) > \varepsilon ,
```
即任意两个不同的项之间距离都超过 $\varepsilon$，故任何子序列两点间距都不会趋于零。

反过来，若 $X$ 是全有界的，且 $\{x_n\}$ 是任意一列点，则可如下构造一个 Cauchy 子序列：$X$ 可表示为有限个半径为 $1$ 的开球之并，于是 $\{x_n\}$ 必有一个子序列完全落在其中某个球里。这个球又可用有限个半径为 $1/2$ 的球再作细分；在该子序列中再抽取合适的子序列，便可得到一个直径不超过 $1/2$ 的球内的子序列。不断重复这一过程，并逐步取出套叠的子序列，最终得到一个逐步收敛的子序列。我们将在习题 13.12.43 中请你对这一过程给出精确描述，并验证所构造出的序列确实是 $\{x_n\}$ 的一个 Cauchy 子序列。 $\square$

现在我们可以重新解释已有的标准结论：$\mathbb{R}^n$ 中的紧致等价于闭且有界。$\mathbb{R}^n$ 的闭子集是完备的（complete）；$\mathbb{R}^n$ 的有界子集是全有界的。于是我们同样可以说：$\mathbb{R}^n$ 的紧致子集正是那些既完备又全有界的子集。改述成这样之后，我们就得到了一条在任意度量空间中都成立的定理。

> <span style="color:#7f8c8d;">TBB §13.12, p.605</span>

<span style="color:#c0392b">**定理 13.97：**</span> 一个度量空间是紧致的，当且仅当它既完备又全有界（compact if and only if it is complete and totally bounded）。

<span style="color:#2471a3;">**[proof]**</span> **证明。** 设 $X$ 是紧致的，取 $X$ 中任一 Cauchy 序列 $\{x_n\}$。由 Bolzano-Weierstrass 性质，$\{x_n\}$ 含有收敛子序列；而带有一个收敛子序列的 Cauchy 序列本身必收敛（见习题 13.8.6）。故 $X$ 是完备的。

同理可证 $X$ 是全有界的：若 $\{x_n\}$ 是 $X$ 中任意一列点，则它必有收敛子序列；该子序列为 Cauchy 序列，据此并直接由定理 13.94 立即推出 $X$ 是全有界的。

反过来，设 $X$ 完备且全有界。若 $\{x_n\}$ 是 $X$ 中的任意一列点，则由定理 13.96 知 $\{x_n\}$ 有一个 Cauchy 子序列；又因 $X$ 完备，该子序列收敛。于是按定义 $X$ 即为紧致。 $\square$

<span style="color:#7f8c8d">书页 606 —— Metric Spaces（第 13 章）习题区。</span>

<span style="color:#7f8c8d">*（书页 606 全部为 §13.12 的 Exercises 习题区 13.12.35 — 13.12.47，按约定跳过，不译、不收录。）*</span>

<span style="color:#7f8c8d">习题 13.12.35 — 13.12.47 大致内容（供回顾）：13.12.35 证明 $S \subset X$ 全有界当且仅当对每个 $\varepsilon > 0$ 存在有限集 $\{x_1,\ldots,x_n\} \subset S$ 使 $S \subset \bigcup_{i=1}^n B(x_i, \varepsilon)$（见 Note 364）；13.12.36 解释 Herman Weyl 关于「紧致城市可由有限个任意近视警察守卫」的玩笑；13.12.37 全有界集的任意子集仍全有界；13.12.38 全有界集的闭包仍全有界；13.12.39 离散度量空间中哪些集是全有界的；13.12.40 每个全有界集都有界而反之不然；13.12.41 直接证明 $\mathbb{R}^n$ 中全有界当且仅当有界（见 Note 365）；13.12.42 全有界性在连续映射下不变吗、是否为拓扑性质、在一致连续映射与等距映射下是否不变；13.12.43 补全定理 13.96 证明的所有细节（见 Note 366）；13.12.44 用定理 13.97 证明 $C[a,b]$、$M[a,b]$、$\ell^\infty$ 中的闭球不紧致；13.12.45 证明全有界的度量空间必定可分（separable）（见 Note 367）；13.12.46 比较度量空间可能具有的若干性质；13.12.47 证明 $\ell^2$ 中闭且有界的集合 $E$ 紧致当且仅当 $\lim_{N\to\infty}\sum_{i=N}^{\infty} x_i^2 = 0$ 对 $x = (x_1, x_2, \ldots) \in E$ 一致成立，并在 $\ell^1$ 中陈述并证明相应版本。</span>


<!-- ===== W12 ===== -->

<span style="color:#7f8c8d">书页 607 — 第 13 章 §13.12 Compactness（紧致性）</span>

<span style="color:#c0392b;">**13.12.5 区间 $C[a,b]$ 中的紧致集（Compact Sets in $C[a,b]$）**</span>

<span style="color:#7f8c8d">*（本小节为拓展小节，可省略。）*</span>

在任何一个对我们重要的度量空间（metric space）中，确定哪些集合是紧致的（compact）同样至关重要。分析学中的许多存在性与唯一性定理都能从紧致性论证（compactness argument）中得出最佳结论。因此，我们需要知道在所处的空间中哪些集合容许这种论证。

配置上确界度量（supremum metric）

```math
d(f, g) = \max_{x \in [a,b]} |f(x) - g(x)|
```

的区间 $[a,b]$ 上连续函数空间 $C[a,b]$，是一个完备可分度量空间（complete separable metric space）。它的哪些子集是紧致的呢？

尽管所有紧致集都必然是有界闭集，但在这一空间中，并非所有有界闭集都是紧致的。我们这里的目的，是获得 $C[a,b]$ 的紧致子集的一个有用刻画。这一刻画涉及 $[a,b]$ 上一族函数可能具备也可能不具备的两个性质。就第一个性质来说，我们不妨追问：是什么刻画了 $C[a,b]$ 中的有界子集？因为每个紧致集也必然是有界的。

> <span style="color:#7f8c8d;">TBB §13.12, p.607</span>
<span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f;">**定义 13.98：**</span>区间 $[a,b]$ 上的一族函数 $\mathcal{F}$ 称为在 $[a,b]$ 上一致有界（uniformly bounded），如果存在 $M > 0$，使得对所有 $x \in [a,b]$ 与所有 $f \in \mathcal{F}$ 都有 $|f(x)| \leq M$。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> equicontinuous（等度连续）的核心是让一致性从单个函数扩展到整族函数：全体成员共享同一个 $\delta$。理解它为何不平凡，最好搭一条"依赖性梯子"。连续函数在一点的 $\delta$ 依赖三元组 $(x_0,\varepsilon,f)$：对每个点、每个精度、每个函数都要单独配一个 $\delta$。uniform continuity（一致连续）因为 $[a,b]$ 紧致（定理 5.48：紧区间上的连续函数必一致连续）去掉对 $x_0$ 的依赖：同一个 $\delta$ 对整个区间处处有效，但仍随函数而变。等度连续更进一步去掉对 $f$ 的依赖，让 $\delta$ 只由 $\varepsilon$ 决定、对族内所有 $f$ 同时成立。用 6.042J 的一阶逻辑量词顺序看，这条梯子就是"谁能先选 $\delta$"的问题：逐点连续是 $\forall f\,\forall x_0\,\forall\varepsilon\,\exists\delta$（$\delta$ 最后选，依赖前面全部变量）；一致连续把 $x_0$ 挪到 $\delta$ 后面，变成 $\forall f\,\forall\varepsilon\,\exists\delta\,\forall x_0$；等度连续再进一步变成 $\forall\varepsilon\,\exists\delta\,\forall f\,\forall x_0$。6.042J 教过，$\forall x\,\exists y$ 一般推不出 $\exists y\,\forall x$，量词交换不免费；紧致性就是买下第一次交换的货币，而"全族共享 $\delta$"正是第二次交换的定义本身。
>
> 例 13.101 是温温柔柔的开胃菜：携带一个公共 Lipschitz 常数 $M$ 的函数族就是等度连续的，直接取 $\delta=\varepsilon/M$ 即可，因为 $|f(x)-f(y)|\le M|x-y|$ 保证只要 $|x-y|<\varepsilon/M$ 就有 $|f(x)-f(y)|<\varepsilon$。具体例子：函数族 $f_n(x)=\sin(nx)/n$（$n=1,2,\dots$）在 $[0,1]$ 上导数 $\cos(nx)$ 的绝对值不超过 $1$，公共 Lipschitz 常数 $M=1$，因此 $\delta=\varepsilon$ 全族通用。反过来，族 $g_n(x)=x^n$ 在 $[0,1]$ 上每个成员单独看都一致连续（定理 5.48 对每个 $n$ 都适用），但整族不等度连续：取 $x=1$、$y=1-\delta$，$|g_n(1)-g_n(1-\delta)|=1-(1-\delta)^n$ 随 $n\to\infty$ 趋于 $1$，任何固定 $\delta$ 都无法把所有 $n$ 同时压到 $\varepsilon<1$ 以下。这个小例子说明"去掉对 $f$ 的依赖"是实质性的一步，不是文字游戏。
>
> 它与 uniform boundedness（一致有界，定义 13.98）配合，恰好分别在 $C[a,b]$ 里扮演"值域有界"与"变化率受控"两个角色：一致有界管住所有函数值落在有限区间 $[-M,M]$ 内，等度连续管住 $x$ 方向的变化足够均匀。为什么两个条件缺一不可，可以从"点"与"坡度"两个自由度看：值域一致有界是竖直方向的控制，保证函数值只在有限高度内取值；等度连续是水平方向的控制，保证所有成员在统一窗口 $|x-y|<\delta$ 内竖直漂移不超过 $\varepsilon$。二者合起来，一族函数就被锁进一个"有限高、有限陡"的矩形网格里。注意一致有界与逐点有界的差别：逐点有界只要求每个 $x$ 处所有 $f(x)$ 被某个常数压住，但该常数可以随 $x$ 变化；一致有界要求同一个 $M$ 对所有 $x$ 和所有 $f$ 同时成立。这又是一次量词交换——把"对每个 $x$ 存在界"升级为"存在一个公共界对所有 $x$"，与等度连续里"对每个 $f$ 存在 $\delta$"升级为"公共 $\delta$ 对所有 $f$"是同一类操作。
>
> 这个 Lipschitz 视角你在 CSAPP 的数值分析与 Strang 线性代数里反复逼近解的语境中都见过：CSAPP 的舍入误差分析里，若函数满足 $|f(x)-f(y)|\le M|x-y|$，则输入表示误差 $\delta_x$ 最多被放大成输出误差 $M\delta_x$，$M$ 就是前向误差的放大倍数；Strang 里 Jacobi 迭代 $x_{k+1}=Bx_k+c$ 收敛要求谱半径（迭代矩阵 $B$ 的特征值最大模）$\rho(B)<1$，本质是要求迭代映射在某个范数下成为压缩，即 Lipschitz 常数小于 $1$。区别在于：Strang 需要 $M<1$ 才能收缩到不动点，管的是收敛速度；等度连续只要求 $M<\infty$ 存在即可，管的是全族的紧致性描述。
>
> 形象地说，等度连续保证一族函数整体上不会太陡，因而能在统一尺度下被有限描述，这正是 Arzelà–Ascoli 定理把一族函数当作一个点来处理的依据。

---

这一概念刻画了度量空间 $C[a,b]$ 中的有界子集。其证明直截了当，留给习题。

> <span style="color:#7f8c8d;">TBB §13.12, p.607</span>
<span style="color:#2471a3;">**[lemma]**</span> <span style="color:#c0392b;">**引理 13.99：**</span>设 $\mathcal{F}$ 是 $[a,b]$ 上一族连续函数。则 $\mathcal{F}$ 在 $[a,b]$ 上一致有界，当且仅当 $\mathcal{F}$ 是度量空间 $C[a,b]$ 的有界子集。

另一个相关的概念，涉及 $C[a,b]$ 中紧致子集内连续函数之连续性行为的一致性问题。设 $f \in C[a,b]$、$x_0 \in X$、$\varepsilon > 0$。则存在 $\delta > 0$，使得当 $|x - x_0| < \delta$ 时有 $|f(x) - f(x_0)| < \varepsilon$。数 $\delta$ 依赖于 $x_0$、$\varepsilon$ 与 $f$，或许应当写作 $\delta = \delta(x_0, \varepsilon, f)$。由于 $[a,b]$ 上任何连续函数也都是一致连续的（uniformly continuous，定理 5.48），我们知道对于给定的 $\varepsilon$ 与 $f$，$\delta$ 可选取得与 $x_0$ 无关。若 $\mathcal{F} \subset C[a,b]$，且我们能把 $\delta$ 选取得同时与 $f \in \mathcal{F}$ 无关，则称 $\mathcal{F}$ 为等度连续族（equicontinuous family）。这一概念归功于 Giulio Ascoli（1843–1896）。

> <span style="color:#7f8c8d;">TBB §13.12, p.607</span>
<span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f;">**定义 13.100：**</span>度量空间 $(X, d)$ 上一族函数 $\mathcal{F}$ 是等度连续的（equicontinuous），如果对每个 $\varepsilon > 0$ 存在 $\delta > 0$，使得只要 $x, y \in X$ 且 $d(x, y) < \delta$，就有对所有 $f \in \mathcal{F}$ 成立 $|f(x) - f(y)| < \varepsilon$。

举个简单的例子：注意，凡满足一致 Lipschitz 条件（uniform Lipschitz condition）的函数收集都是等度连续的。

> <span style="color:#7f8c8d;">TBB §13.12, p.607</span>
<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b;">**例 13.101：**</span>设 $M > 0$，且

```math
\mathcal{F} = \{\, f : [a,b] \to \mathbb{R} : |f(x) - f(y)| \leq M|x - y| \ \ \text{对所有 } x, y \in [a,b] \,\} .
```

<span style="color:#7f8c8d">书页 608 — 第 13 章 §13.12 Compactness（紧致性）续</span>

<span style="color:#7f8c8d">*（接上页例 13.101 的翻译。）*</span>

则 $\mathcal{F}$ 是 $[a,b]$ 上一族等度连续函数。只需取 $\delta = \varepsilon / M$ 即可。$\square$

我们接下来的主要定理通常同时归功于 Ascoli 与 Cesare Arzelà（1847–1912）。该定理如今运用一致有界与等度连续这两个概念，获得了空间 $C[a,b]$ 中紧致性（compactness）的一个刻画。

> <span style="color:#7f8c8d;">TBB §13.12, p.608</span>
<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**定理 13.102（Arzelà-Ascoli 定理）：**</span>设 $K$ 是度量空间 $C[a,b]$ 的一个闭子集。则 $K$ 是紧致的，当且仅当 $K$ 一致有界且等度连续。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 这条定理回答在无穷维空间 $C[a,b]$ 里哪些集合是紧致的这一大问题，它最反直觉的一句是：在 $C[a,b]$ 中有界闭并不保证紧致（习题 13.12.44 想让你亲自撞一下这面墙），必须再加上等度连续。撞墙的现成例子是 $C[0,1]$ 里的闭单位球 $\{f:\|f\|_\infty\le 1\}$：它显然有界且闭，但其中的序列 $f_n(x)=x^n$ 没有一致收敛子列——它的逐点极限是 $x<1$ 处为 $0$、$x=1$ 处为 $1$ 的不连续函数，任何一致收敛子列都必须以这个不连续函数为极限，而 $C[0,1]$ 里的元素都是连续函数，矛盾。这说明有限维的 Heine–Borel 经验（有界闭必紧致）在函数空间里失效了。
>
> 用第一性原理拆开看十分清晰：紧致 $\Longleftrightarrow$ 完备且全有界（定理 13.97），而对 $C[a,b]$ 的闭子集，完备性自动成立（连续函数的一致极限仍连续），于是问题归结为"一族函数什么时候全有界"。单靠同一个 $M$ 压住还不够：值域有界只保证所有函数值落在 $[-M,M]$ 这个竖直条带里，但函数可以在 $x$ 方向上任意疯狂地上下抖动，无法被有限个简单模板函数逼近。必须再加上等度连续，让它们在 $x$ 方向上变化足够均匀，才能被有限个折线网盖住。证明正是借 $[-M,M]\times[a,b]$ 上的细分网格加分段线性函数构造出 $\varepsilon$-网（图 13.7）：先由等度连续取出 $\delta$，把 $[a,b]$ 切成若干长度小于 $\delta$ 的小区间；再把 $[-M,M]$ 切成若干长度为 $\varepsilon/3$ 的小段；取所有"节点处取值落在网格点上、节点之间线性连接"的分段线性函数，它们只有有限多个（节点数有限、每个节点的取值层数有限，组合数有限），却能把族里每个函数逼近到误差 $\varepsilon$ 以内。
>
> 证明里反复出现的 $\varepsilon/3$ 拆分是把中间项夹出的小技巧，值得命名为 $\varepsilon/3$ 技巧（误差预算三等分法）：先把总误差拆成三个来源——节点处函数值被网格点取整的误差、区间内部由等度连续控制的漂移、分段线性插值相对真值的摆动——每个来源分配 $\varepsilon/3$ 的预算，再用三角不等式把三项加起来。其中关键一步是凸组合估计：分段线性函数在节点之间是两端取值的凸组合，所以取整误差经过插值后不会放大，仍被 $\varepsilon/3$ 压住。这个"先列误差清单、再均分预算"的模板在数值分析与算法分析里到处能复用。
>
> 从计算视角看，这个 $\varepsilon$-网构造本质上是一次"有限化"：网格节点有限，每个节点的取值层数有限，组合出的分段线性函数总数虽然巨大（层数的节点数次方量级），但有限性本身已足够保证全有界。CLRS 教你关心多项式与指数的复杂度鸿沟，这里恰恰相反：Arzelà–Ascoli 是存在性定理，只在乎"网是有限的"，不在乎网有多大——这是存在性证明与构造性算法之间的分工。6.042J 的可数性也在此接上：对 $\varepsilon=1,1/2,1/3,\dots$ 各取一个有限网，可数个有限集的并仍是可数集（6.042J 的可数并定理），于是 $C[a,b]$ 存在可数稠密子集，即函数空间是 separable（可分）的；这与 6.042J 里实数不可数的对角线论证形成对照：$C[a,b]$ 本身不可数，却存在可数稠密子集，不可数与可分并不矛盾。
>
> 历史上等度连续性概念由 Ascoli（1843–1896）在 1880 年代引入，紧致性刻画由 Arzelà（1847–1912）约在 1889 年完成，故合称 Arzelà–Ascoli。对智能科学与技术专业的你，有界 + 等度连续 $\Longrightarrow$ 有收敛子列正是许多逼近定理论证与优化算法收敛性证明的数学底座。

---

<span style="color:#2471a3;">**[proof]**</span> <span style="color:#c0392b;">**证明：**</span>首先注意到，由于 $K$ 被假定为我们已知之所处的完备空间的一个闭子集，$K$ 本身是完备的。由定理 13.97，$K$ 是紧致的当且仅当 $K$ 是全有界的（totally bounded）。因此，我们只需证明：$K$ 一致有界且等度连续，当且仅当 $K$ 全有界。

先假设 $K$ 在 $C[a,b]$ 中全有界。则 $K$ 在 $C[a,b]$ 中有界，因而是函数的一族一致有界族。我们来证明 $K$ 是等度连续的。设 $\varepsilon > 0$，并令 $f_1, f_2, \ldots, f_n$ 为 $K$ 中的一个 $(\varepsilon/3)$-网（$(\varepsilon/3)$-net）。设 $f \in K$。存在 $j \leq n$，使得

```math
\max_{z \in [a,b]} |f(z) - f_j(z)| < \tfrac13 \varepsilon .
\tag{28}
```

于是，对 $x, y \in [a,b]$，

```math
|f(x) - f(y)| \leq |f(x) - f_j(x)| + |f_j(x) - f_j(y)| + |f_j(y) - f(y)| .
\tag{29}
```

每个函数 $f_i$ 都是一致连续的。因此，由于它们只有有限多个，存在 $\delta > 0$，使得

```math
|x - y| < \delta, \ \ 1 \leq i \leq n \ \ \Rightarrow \ \ |f_i(x) - f_i(y)| < \varepsilon/3 .
\tag{30}
```

现在由 (28)、(29)、(30) 推出，对所有满足 $|x - y| < \delta$ 的 $x, y \in [a,b]$ 以及所有 $f \in K$，都有 $|f(x) - f(y)| < \varepsilon$。这表明 $K$ 是等度连续的。

为证其逆，假设 $K$ 一致有界且等度连续。我们要证明 $K$ 是全有界的。设 $\varepsilon > 0$。我们将在空间中为 $K$ 找一个 $\varepsilon$-网 $\mathcal{F}$。这意味着 $\mathcal{F}$ 必须是 $C[a,b]$ 中函数的一个有限收集，使得 $K$ 的每个成员都距离 $\mathcal{F}$ 的某个成员小于 $\varepsilon > 0$。（注意，我们并不必须从 $K$ 当中选取 $\mathcal{F}$ 的成员，尽管这样做是可能的。）

选取 $M \in \mathbb{N}$，使得对所有 $x \in X$ 与 $g \in K$ 有 $|g(x)| \leq M$。设 $\varepsilon > 0$。由于 $K$ 等度连续，存在 $\delta > 0$，使得

```math
|x - y| < \delta, \ \ g \in K \ \ \Rightarrow \ \ |g(x) - g(y)| < \varepsilon/4 .
\tag{31}
```

利用此数 $\delta$，我们用足够靠近的点 $x_1, x_2, \ldots, x_n$ 来细分 $[a,b]$，使得 $[a,b]$ 中每个点都落在这些点某一点的 $\delta$ 邻域之内。（注意，这将构成紧致度量空间 $[a,b]$ 的一个 $\delta$-网。）

选取 $m \in \mathbb{N}$ 使 $1/m < \varepsilon/4$，并把区间 $[-M, M]$ 剖分为 $2Mm$ 个全等的小区间（congruent intervals）：

```math
-M = y_0 < y_1 < \cdots < y_{2Mm} = M .
```

现在考察矩形 $[a,b] \times [-M, M]$ 中的所有格点（grid of points），其第一坐标取自点 $x_1, x_2, \ldots, x_n$，第二坐标取自纵轴 $y$ 序列中的点。

```math
\text{（证明的下一部分接下一页书页，构建所需的 } \varepsilon \text{-网并完成论证。）}
```


<!-- ===== W13 ===== -->

<span style="color:#7f8c8d">书页 609 · §13.12 Compactness（紧致性）续 · Theorem 13.102 证明收尾</span>

<span style="color:#2471a3;">**[figure]**</span> **图 13.7** 在定理 13.102 的证明中，将区间 $[-M, M]$ 与 $[a,b]$ 加以划分（Partitioning the intervals $[-M, M]$ and $[a, b]$）的情形示意。

<span style="color:#2471a3;">**[proof]**</span>（承接前页）具分割节点 $y_0, y_1, \ldots, y_{2Mm}$，即上述坐标点。

图 13.7 正是对这一情形的刻画（illustrates the situation）。

设 $F$ 表示 $[a,b]$ 上所有连续、分段线性（piecewise linear），且其图象上的拐点（corner point）恰好落在网格节点处的函数所组成的集合。

显然，这样的函数只有有限多个（finitely many）。

任取 $g \in K$。由于网格（grid）的构造特性，至少存在一个函数 $f \in F$，使得

```math
|g(x_j) - f(x_j)| < \varepsilon/4 \qquad (j = 1, 2, \ldots, n).
```
（32）

考虑任意一点 $x \in [a,b]$。存在某个区间使得 $x \in [x_j, x_{j+1}]$，其中 $1 \le j < n$。

由 (31) 我们知道

```math
|g(x_j) - g(x_{j+1})| < \varepsilon/4.
```

于是，结合 (32)，还可推出

```math
|f(x_j) - f(x_{j+1})| < \varepsilon/2.
```

由于 $f$ 在区间 $[x_j, x_{j+1}]$ 上是线性的（linear），对所有 $x \in [x_j, x_{j+1}]$，我们同样得到不等式

```math
|f(x_j) - f(x)| < \varepsilon/2.
```

将这些不等式综合起来可知

```math
|g(x) - f(x)| \le |g(x) - g(x_j)| + |g(x_j) - f(x_j)| + |f(x_j) - f(x)| < \varepsilon,
```

这进一步蕴含

```math
\max_{x \in [a,b]} |f(x) - g(x)| < \varepsilon.
```

至此我们证明了 $F$ 是一个 $\varepsilon$-网（ε-net），于是 $K$ 是全有界（totally bounded）的，定理得证。$\square$

<span style="color:#7f8c8d">*（本页自 §13.12 习题 13.12.48 起的其余部分为习题区，按约定跳过，不翻译不收录。）*</span>

<span style="color:#7f8c8d">书页 610 · §13.12 习题区（Exercises, 13.12.50–13.12.56 前半）</span>

<span style="color:#7f8c8d">*（书页 610 全部为 §13.12 习题区——包含 13.12.50（一致连续函数的平移族等度连续）、13.12.51（$x^n$ 在 $[0,1]$ 与 $[0,1/2]$ 的等度连续性）、13.12.52（积分算子对 $C[a,b]$ 有界子集的作用）、13.12.53（积分算子 $A$ 的象集等度连续）、13.12.54（连续模 modulus of continuity 与 $C(\sigma)$、$\sqrt{x}$ 相关紧致性）、13.12.55（$C[a,b]$ 子空间 $\mathrm{Lip}_1[a,b]$ 中点态收敛等价收敛性强弱）以及 13.12.56 的 (a) 小题——按约定整体跳过，不翻译不收录。）*</span>


<!-- ===== W14 ===== -->

<span style="color:#7f8c8d">书页 611 · §13.12 Compactness（承前，续 §13.12 末）</span>

<span style="color:#7f8c8d">*（本页开头至 §13.12.6 之前为 §13.12 的习题区，含上题的 (b)(c) 小问及习题 13.12.57、13.12.58 等，按约定跳过。）*</span>

<span style="color:#7f8c8d">（跳过部分摘要：习题 13.12.56 之 (b) 问——若序列 $\{f_n\}$ 等度连续（equicontinuous），则对每个 $x\in[a,b]$ 极限 $\lim_{k\to\infty} f_{n_k}(x)$ 均存在且一致收敛（uniform convergence）；(c) 问要求借此给出 Arzelà-Ascoli 定理的另一证明。习题 13.12.57 用 Arzelà-Ascoli 定理证明集合 $\{f\in C[0,1]:\,|f(x)|\le 1\}$ 不能被一列紧致集覆盖；习题 13.12.58 证明 Arzelà-Ascoli 定理的更一般版本，即紧致度量空间 $X$ 上的连续函数空间 $C(X)$ 的闭子集 $K$ 紧致当且仅当 $K$ 一致有界（uniformly bounded）且等度连续。）</span>

<span style="color:#2471a3;">**[section]**</span>

<span style="color:#c0392b">**§13.12.6 Peano 定理**</span>

<span style="color:#7f8c8d">*（本节为拓展小节，可省略。）*</span>

在 §13.11.4 中我们见到压缩映射原理（contraction mapping principle）如何被用来证明微分方程（differential equation）$y'=f(x,\,y)$ 解的存在性与唯一性定理（existence and uniqueness theorem）。

当时为应用压缩映射原理所需的假设，是函数 $f$ 必须满足一个 Lipschitz 条件（Lipschitz condition）。

要在更弱的假设下（这一次不再有唯一性）获得一个存在性定理，我们需要换一种途径。

为此我们要回到 Euler 在 1768 年提出的一个简单想法。

为在一个区间 $[x_0,\,b]$ 上数值求解如下的初值问题（initial value problem）

```math
y' = f(x,\,y),\qquad y(x_0)=y_0,
```

可把该区间划分为 $n$ 个等距点（等分并非本质要求，但在数值方法里是传统做法）

```math
x_0 < x_1 < x_2 < \cdots < x_n = b,
```

再用一条分段线性函数（piecewise linear function）来近似解。

写出

```math
y_1 = y_0 + f(x_0,\,y_0)(x_1-x_0),
```

```math
y_2 = y_1 + f(x_1,\,y_1)(x_2-x_1),
```

如此类推直到

```math
y_n = y_{n-1} + f(x_{n-1},\,y_{n-1})(x_n-x_{n-1}).
```

可以令 $k_n(x)$ 表示 $[x_0,\,b]$ 上这样定义的函数：它连续，穿过点 $(x_0,y_0),(x_1,y_1),\ldots,(x_n,y_n)$，在相邻两点之间是线性的。

注意若 $x$ 落在第 $i$ 个区间 $(x_i,\,x_{i+1})$ 内，则 $k_n'(x)=f(x_i,\,k_n(x_i))$，而在那些折点（corner point）处没有导数。

在实际操作中，这个方法能给出解的一个合理近似。

若我们能证明序列 $\{k_n\}$ 一致收敛到一个函数 $k$、且这个函数 $k$ 确实解出了该初值问题，就可把它作为存在性证明的基础。

<span style="color:#7f8c8d">书页 612 · Metric Spaces · Chapter 13</span>

<span style="color:#2471a3;">**[figure]**</span>

<span style="color:#c0392b">**图 13.8（Figure 13.8）**</span> 集合 $W$ 及其在 $x$ 轴上的投影到 $[a,b]$，即 Theorem 13.103 证明中所用到的情形。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> Peano existence theorem（佩亚诺存在定理）是本小节的高潮之一：它把微分方程解的存在性从 Lipschitz condition（利普希茨条件）放宽到只要求 $f$ 连续，代价是失去唯一性。第一性原理地看，§13.11 的 contraction mapping（压缩映射）能同时给出存在与唯一，是因为压缩映射自带一个小于 1 的收缩因子，让 Picard 迭代每走一步都把误差乘以这个因子，几何级数式地挤向唯一不动点；这与 Strang 的 Jacobi 迭代收敛判据——谱半径 $\rho(B)<1$——同源：收缩因子小于 1 是离散迭代收敛的充分条件，压缩映射只是把这套判据搬到度量空间中，把范数压缩换成度量压缩。连续性只保证 $f$ 不跳跃，不保证两条解曲线彼此靠拢，所以存在与唯一在这里第一次分家。这值得当成一条思维模板：存在性问“至少有一个”，唯一性问“至多有一个”，它们是两条独立的问题线，不能默认打包处理。
>
> 证明的骨架是 Euler method（欧拉折线法，Euler 1768 年提出，即今天数值解 ODE 的前向 Euler 方法）。取步长 $\varepsilon>0$，在节点 $t_n=t_0+n\varepsilon$ 上用递推 $k_\varepsilon(t_{n+1})=k_\varepsilon(t_n)+\varepsilon f(t_n,k_\varepsilon(t_n))$ 搭出逐段线性的近似解 $k_\varepsilon$。这条递推可用 6.042J 的归纳法读：给定 $k_\varepsilon(t_n)$，下一步被唯一确定，整条折线由归纳定义；也可用 CLRS 的 loop invariant（循环不变量）读：第 $n$ 步循环开始前，折线已在 $[t_0,t_n]$ 上定义好且相邻节点满足递推式。区别在于，CLRS 的循环不变量服务于有限步停机后的正确性，而这里的归纳只负责造近似对象，真正的结论要靠后面的取极限，归纳本身并不终结。CSAPP 的资源视角同样精确：真实硬件上 $\varepsilon$ 越小截断误差越小，但步数 $1/\varepsilon$ 越多，IEEE 754 浮点舍入逐步累积，$\varepsilon$ 不能无限小；Peano 证明里 $\varepsilon\to 0$ 发生在精确算术的数学世界，没有舍入——这是数值实验与存在性证明的关键区别。
>
> 技术核心是把一族 $\{k_\varepsilon\}$ 装进一个有界且 equicontinuous（等度连续）的集合 $K$。有界来自 $f$ 在紧集 $W$ 上有最大模 $M$，于是斜率 $|k_\varepsilon'|\le M$ 被统一控制；等度连续的意思是全族的振荡速度被同一块表控制，不会出现某些成员抖得越来越快。Arzelà–Ascoli theorem（阿尔泽拉–阿斯科利定理）随即抽出一致收敛子列 $k_{1/n_i}\to k$。这个抽取动作内部用的是 6.042J 的对角线论证：先在可数稠密点集上逐点抽子列，再用等度连续把逐点收敛升级为一致收敛；区别在于，6.042J 的对角线用于制造矛盾（实数不可数），这里用于制造对象（一条子列），可命名为“对角线抽取法”。
>
> 最后把 $k_\varepsilon$ 写成积分形式再取极限。每个折线段上，$k_\varepsilon(t)$ 与 $y_0+\int_{t_0}^{t}f(s,k_\varepsilon(s))\,ds$ 只差一个小区间内的积分误差项，随 $\varepsilon\to 0$ 一致趋于零；又因 $f$ 在 $W$ 上 uniform continuity（一致连续），$k_{1/n_i}\to k$ 一致收敛，故 $f(s,k_{1/n_i}(s))\to f(s,k(s))$ 一致收敛，极限号穿过积分号，得到 $k(t)=y_0+\int_{t_0}^{t}f(s,k(s))\,ds$，即 $k$ 是真解。整条证明可命名为“近似造族—紧性抽子列法”：先造一簇近似解，再从近似解中抽取收敛子列得到真解，这比硬凑一个解万能得多，也是日后泛函分析中紧性、弱紧性证存在性的雏形。
>
> 仅连续时解不必唯一。Peano 自己 1890 年举出 $y'=3y^{2/3},\ y(0)=0$（习题 13.12.59）：$f(y)=3y^{2/3}$ 在 $0$ 附近连续，但导数 $2y^{-1/3}$ 爆炸，故非 Lipschitz。该方程有 $y\equiv 0$ 与 $y=x^3$（$x\ge 0$）两个解，更有无穷多个“先停在零、再从任意 $c\ge 0$ 处起飞”的解 $y=\max\{0,(x-c)^3\}$。数值上，从 $y(0)=0$ 出发的 Euler 方法因 $f(0)=0$ 会永远停在零解，看不见其他解。这正与 §13.11 压缩映射的“存在且唯一”形成对照：连续性买到存在，Lipschitz 才买到唯一。
>
> 把"先造近似解、再取极限"这条 Peano 证明路线与 Picard 的"迭代收敛到不动点"路线并排看，能看到两种完全不同的存在性证明哲学。Picard 走的是**构造性路线**：显式给出一个迭代序列，证明它收敛，极限自动是解——好处是顺带拿到近似算法（逐次逼近可以直接跑），代价是需要压缩性这种强假设。Peano 走的是**紧性路线**：不去构造单一收敛序列，而是造出一整族近似解 $k_\varepsilon$，证明这族函数在某个函数空间里是"预紧"的（有界 + 等度连续，Arzelà–Ascoli 定理的条件），于是必然存在一个收敛子列，其极限就是解——好处是只需连续性这种弱假设，代价是只告诉你解存在、不告诉你哪个子列收敛、也没有显式算法。这两条路线你日后会反复遇到：泛函分析里证明变分问题解的存在性，几乎都是紧性路线的变体（先证能量泛函有下界、再证极小化序列有收敛子列）；而数值分析里的迭代法全是构造性路线的子孙。对智能科学与技术专业来说，这个分野尤其重要：**你要"算得出解"还是只要"知道有解"？** 机器学习里证明某个损失函数有全局最优、却给不出到达它的算法，就是紧性路线的困境；而梯度下降类方法能实际跑出结果，靠的正是构造性路线的压缩/收缩性质。Peano 定理因此不只是实分析的一个存在性结果，它还是"存在性证明的两种哲学"这一永恒主题的第一次正式亮相。

---

遗憾的是，我们想采用的假设——函数 $f$ 的连续性——实在太弱，不足以证明序列 $\{k_n\}$ 一致收敛。

但我们可以用紧致性论证（compactness argument）来获得一个一致收敛的子序列（subsequence）。

关键在于利用 $f$ 的连续性来设计一个区间 $[x_0,\,b]$，使得这样的函数序列 $\{k_n\}$ 在其中既有界又等度连续。

于是 Arzelà-Ascoli 定理便提供了那个子序列。

这一对 Cauchy 与 Lipschitz 经典存在性定理的改进，是 Peano 在 1886 年取得的。

在 1890 年他又指出，这种假设的放宽是以牺牲唯一性为代价的——他给出的例子就是我们将在

习题 13.12.59 中考察的例子。

<span style="color:#2471a3;">**[theorem]**</span>

<span style="color:#c0392b">**Theorem 13.103（Peano）**</span> 设 $f$ 在 $\mathbb{R}^2$ 的一个开子集 $D$ 上连续，且设 $(x_0,\,y_0)\in D$。则微分方程

> <span style="color:#7f8c8d;">TBB §13.12, p.612</span>

```math
y' = f(x,\,y)
```

存在一个局部解（local solution），且该解通过点 $(x_0,\,y_0)$。

<span style="color:#2471a3;">**[proof]**</span>

**证明。** 我们寻求一个精确解，它在某个包含 $x_0$ 的区间上成立。

于是我们要找到一个包含 $x_0$ 的区间 $[a,\,b]$，以及一个定义在 $[a,\,b]$ 上的可微函数 $k$，使得

```math
k(x_0)=y_0,\qquad k'(x)=f(x,\,k(x))\ \text{ 对所有 } x\in[a,\,b].
\tag{33}
```

我们的策略实质上是：在 $[a,\,b]$ 上构造一簇穿过 $(x_0,\,y_0)$ 的近似解（approximate solution），称此簇为 $K$。

然后我们证明该集合 $K$ 在 $C([a,\,b])$ 中是紧致的，并利用紧致性来证明作为 $K$ 中一点的函数 $k$ 的存在性。

我们首先选取区间 $[a,\,b]$。

设 $R$ 是包含在 $D$ 内的一个闭矩形（closed rectangle），其各边平行于坐标轴，且以 $(x_0,\,y_0)$ 为中心。

设 $M\ge 1$ 为 $|f|$ 在 $R$ 上的一个上界（upper bound）。

令

```math
W=\{(x,\,y)\in R : |y-y_0|\le M|x-x_0|\},
```

并令 $[a,\,b]$ 为 $W$ 到 $x$ 轴的投影（projection），正如图 13.8 所示。

接下来我们得到一众定义在 $[x_0,\,b]$ 上的函数 $K$，它们可被视为 (33) 的近似解。

由于 $W$ 在 $\mathbb{R}^2$ 中紧致，故 $f$ 在 $W$ 上一致连续（uniformly continuous）。


<!-- ===== W15 ===== -->

<span style="color:#7f8c8d">书页 613 · §13.12 Compactness（承前，续 Theorem 13.103 Peano 定理之证明收尾）</span>

于是对每个 $\varepsilon>0$，都存在某个 $\delta\in(0,1)$，使得只要 $(x,y)\in W$ 与 $(x',y')\in W$ 且 $|x-x'|<\delta$、$|y-y'|<\delta$，就有

```math
|f(x,\,y)-f(x',\,y')|<\varepsilon .
```

选取点 $x_1,\,x_2,\ldots,x_n$ 使之满足

```math
x_0<x_1<x_2<\cdots<x_n=b,\qquad |x_i-x_{i-1}|<\delta/M\ \text{ 对所有 } i=1,\ldots,n .
```

如下在 $[x_0,\,b]$ 上定义一个函数 $k_\varepsilon$：设 $k_\varepsilon(x_0)=y_0$，并在 $[x_0,\,x_1]$ 上令 $k_\varepsilon$ 为具有斜率 $f(x_0,\,y_0)$ 的线性函数。

在 $[x_1,\,x_2]$ 上再令 $k_\varepsilon$ 为具有斜率 $f(x_1,\,k_\varepsilon(x_1))$ 的线性函数。

按这种方式继续下去，我们把 $k_\varepsilon$ 的定义延拓到整个区间 $[x_0,\,b]$。

<blockquote>
我们由此得到定义在 $[x_0,\,b]$ 上的一个函数 $k_\varepsilon$，其图像是一条经过点 $(x_0,\,y_0)$ 且包含在 $W$ 内的折线弧（polygonal arc）。
</blockquote>

由于构成 $k_\varepsilon$ 之图像的各个线段的斜率，都由函数 $f$ 在 $W$ 内的取值所决定，我们看到对所有 $x,\,x'\in[x_0,\,b]$ 都有

```math
|k_\varepsilon(x)-k_\varepsilon(x')|\le M|x-x'| .\tag{34}
```

现在设 $x\in[x_0,\,b]$ 且 $x\ne x_i$（$i=0,1,\ldots,n$）。于是存在某个 $j\in\{1,2,\ldots,n\}$ 使得 $x_{j-1}\lt x\lt x_j$。

注意到 $|x_j-x_{j-1}|<\delta/M$，并利用 (34)，我们看到

```math
|k_\varepsilon(x)-k_\varepsilon(x_{j-1})|\le M|x-x_{j-1}|<\delta .
```

这意味着

```math
|f(x_{j-1},\,k_\varepsilon(x_{j-1}))-f(x,\,k_\varepsilon(x))|<\varepsilon .
```

但

```math
k_\varepsilon'(x)=f(x_{j-1},\,k_\varepsilon(x_{j-1})) ,
```

所以

```math
|k_\varepsilon'(x)-f(x,\,k_\varepsilon(x))|<\varepsilon .\tag{35}
```

不等式 (35) 对所有 $x\in[x_0,\,b]$ 都成立，除非 $x$ 落在有限集 $\{x_0,\ldots,x_n\}$ 中——在这些点处 $k_\varepsilon$ 未必可微。

由 (35) 我们看到，这些函数 $k_\varepsilon$ 都是 (33) 的近似解（approximate solution）。

我们构造了一个函数族 $K$，其中每一个 $\varepsilon>0$ 都对应一个函数，且该族中每个函数都以 $k_\varepsilon$ 的形式出现。

函数族 $K$ 在 $[x_0,\,b]$ 上一致有界（uniformly bounded），因为每个函数 $k_\varepsilon$ 的图像都包含在 $W$ 内。

由 (34) 可知 $K$ 是一个等度连续（equicontinuous）的函数族。

于是 Arzelà-Ascoli 定理推出 $K$ 在 $C([x_0,\,b])$ 中紧致。

我们现在可以完成定理的证明了。

对所有 $x\in[x_0,\,b]$，我们都有

```math
k_\varepsilon(x)=y_0+\int_{x_0}^{x} k_\varepsilon'(t)\,dt
=y_0+\int_{x_0}^{x}\Bigl(f(t,\,k_\varepsilon(t))+\bigl(k_\varepsilon'(t)-f(t,\,k_\varepsilon(t))\bigr)\Bigr)\,dt .\tag{36}
```

$k_\varepsilon'$ 在集合 $\{x_0,\,x_1,\ldots,x_n\}$ 上可能不存在，这一事实并不影响上述积分。

由于序列 $\{k_{(1/n)}\}$ 含于 $K$ 且 $K$ 紧致，故该序列包含一个一致收敛到某个函数 $k\in K$ 的子序列 $\{k_{(1/n_i)}\}$。

<span style="color:#7f8c8d">书页 614 · Metric Spaces · Chapter 13</span>

注意 $k$ 在 $[x_0,\,b]$ 上必然连续。

由于 $f$ 在 $W$ 上一致连续，函数 $f(t,\,k_{(1/n_i)}(t))$ 在 $[x_0,\,b]$ 上一致收敛到函数 $f(t,\,k(t))$。

注意到 (35)，我们现在可从 (36) 推出

```math
k(x)=y_0+\int_{x_0}^{x} f(t,\,k(t))\,dt
```

对所有 $x\in[x_0,\,b]$ 成立。

由此可知，$k$ 是 (33) 在 $[x_0,\,b]$ 上的一个解。

用类似的方式，我们在 $[a,\,x_0]$ 上得到一个解 $k$。

由

```math
y(x)=
\begin{cases}
k(x), & x\in[x_0,\,b];\\
k(x), & x\in[a,\,x_0],
\end{cases}
```

给出的函数 $y$ 满足 (33) 在整个 $[a,\,b]$ 上成立，正如所要求的那样。

$\square$

<span style="color:#7f8c8d">*（接着是 §13.12 的习题区，含定理相关证明题；本页下方的习题部分按约定跳过。）*</span>

<span style="color:#7f8c8d">**Exercises 13.12.59 ·（Peano 的例子 Peano's Example）**——按约定跳过，仅作参考：本题要求证明 Theorem 13.103 中给出的假设不足以保证方程 $y'=f(x,\,y)$ 解的唯一性，所举例子为 $y'=3y^{2/3},\ y(0)=0$，并问该例是否与 Theorem 13.86 的唯一性论断相冲突（见 Note 373）。</span>

<span style="color:#2471a3;">**[section]**</span>

<span style="color:#c0392b">**§13.13 Baire 纲定理（Baire Category Theorem）**</span>

在 §6.4 中，我们证明了关于度量空间 $\mathbb{R}$ 的 Baire 纲定理（Baire category theorem）。

现在我们完全有能力对任意完备度量空间（complete metric space）建立同样这一定理。

我们介绍该定理所依托的若干基本思想，并在此节中证明这个定理。

然后，在 §13.14 中，我们给出这个定理的一些应用。

在你继续进行同一套思想在抽象度量空间中的展开之前，也许应当复习一下 §6.3 与 §6.4，看看这些思想在实直线这一特殊背景下是如何表现的。

我们首先回顾度量空间中无处稠密集（nowhere dense set）的定义（该定义见于 §13.5，且已在习题 13.5.21 与 13.6.21 中使用过）。

在给出一些无处稠密集的例子之后，我们转而给出 Baire 纲定理的证明——它断言：一个完备空间不能是任一序列的无处稠密集的并。

<span style="color:#2471a3;">**[section]**</span>

<span style="color:#c0392b">**§13.13.1 无处稠密集（Nowhere Dense Sets）**</span>

在实直线上，集合 $A$ 是无处稠密的，如果它不在任何区间内稠密。

这意味着，给定任意一个区间 $(a,\,b)$，总存在一个子区间 $(c,\,d)\subset(a,\,b)$ 它不含 $A$ 的任何点。

在度量空间中，开区间的角色由开球（open ball）来扮演。

下面是其正式定义。

<span style="color:#2471a3;">**[definition]**</span>

<span style="color:#00838f">**Definition 13.104.** 设 $(X,\,d)$ 是一个度量空间。集合 $A\subset X$ 称为无处稠密的（nowhere dense），如果给定 $X$ 中的任意开球 $B(x,\,\varepsilon)$，总存在一个开球 $B(y,\,\delta)\subset B(x,\,\varepsilon)$ 使得 $A\cap B(y,\,\delta)=\varnothing$。</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> nowhere dense（无处稠密）是一把度量稀疏的尺子：集合 $E$ 无处稠密，指它在每个开球里都留下一个不含它的子球，等价于闭包内部为空 $\operatorname{int}(\overline E)=\varnothing$。第一性原理地拆开：稠密刻画“处处有它的点”，无处稠密刻画“处处有避开它的洞”——连闭包都装不下任何开球。一个具体例子：$\{1/n:n\in\mathbb N\}$ 在 $\mathbb R$ 中无处稠密，因为其闭包 $\{0\}\cup\{1/n:n\in\mathbb N\}$ 内部为空；而 $\mathbb Q$ 在 $\mathbb R$ 中稠密却并不无处稠密，因为 $\overline{\mathbb Q}=\mathbb R$ 内部非空。可见“稠密”与“无处稠密”不是简单反义词：$\mathbb Q$ 是处处有点的厚集，$\{1/n\}$ 是处处有洞的薄集，二者度量的是不同维度。
>
> 例 13.105 提醒一个易翻车的细节：同一个 Cantor set（康托集）放进 $[0,1]$ 无处稠密，因为它是闭集且内部为空，任何小区间里都有它的空隙；放进它自己（取子空间度量）却是稠密的，因为任何空间对自身都稠密。第一性原理：无处稠密永远是集合与环境空间的二元关系，不是集合的固有属性，换环境空间结论可以翻转。这里可与 6.042J 的可数性精确对照：康托集不可数（对角线论证），却在 $[0,1]$ 中无处稠密；$\mathbb Q$ 可数，却在 $\mathbb R$ 中稠密。基数（数数）与拓扑（厚薄）是两把正交的尺子，谁也不能推出谁。Strang 的线性代数也提供对照：$\mathbb R^n$ 上所有范数等价、拓扑唯一，环境空间的选择不影响收敛与稠密；而 $C[a,b]$ 与 $M[a,b]$ 是无限维函数空间，换环境空间后稠密性判断就可能翻转。
>
> 真正冲击直觉的是例 13.106：所有连续函数 $C[a,b]$ 作为所有有界函数 $M[a,b]$ 的子集竟无处稠密，即在所有有界函数里连续函数是极稀有的窄带。证明机制：取任意 $f\in C[a,b]$ 和任意 $\varepsilon>0$，在区间内部取点 $c$，构造 $g$：当 $x\le c$ 时 $g(x)=f(x)$，当 $x>c$ 时 $g(x)=f(x)+\varepsilon/2$，也就是把 $f$ 在 $c$ 右侧整体抬升 $\varepsilon/2$。$g$ 有界且 $\|g-f\|_\infty=\varepsilon/2<\varepsilon$，落在开球内；但 $g$ 在 $c$ 处左极限为 $f(c)$、右极限为 $f(c)+\varepsilon/2$，上下极限之差为 $\varepsilon/2\ne 0$，故 $g$ 在 $c$ 不连续。于是每个开球都装不进 $C[a,b]$；又 $C[a,b]$ 在 $M[a,b]$ 中闭（一致收敛的连续函数列极限仍连续），所以无处稠密。落地例子：取 $f\equiv 0$ 于 $[0,1]$、$\varepsilon=2$、$c=1/2$，则 $g$ 是 $x\le 1/2$ 取 $0$、$x>1/2$ 取 $1$ 的阶跃函数，$\|g-f\|_\infty=1<2$ 却在 $c$ 处跳跃。这个证明的精髓可命名为“跳板编码法”：把“在 $c$ 连续”这个逐点性质编码成上下极限之差是否为零这个数值量，用一次 $\varepsilon/2$ 抬升制造出可比较的差。这正可比拟 CSAPP 里用位模式把布尔性质编码成可比较数值：IEEE 754 把符号、阶码、尾数拼进 32 位或 64 位模式，使浮点数可以按位比较和舍入；这里把连续性编码成极限差，使稠密性论证可以动手构造。区别在于位模式是有限精度编码，必有舍入误差；极限差是精确数学量，不损失信息。
>
> 这些例子是为 Baire 纲定理铺路：既然连续函数都如此小众，则大多数有界函数可以很坏。这里“大多数”是纲意义——坏集的补集稠密——而不是 6.042J 的计数意义，也不是测度意义。这正是下一条定理在哲学上担保的事实。
>
> 真正冲击直觉的是例 13.106：所有连续函数 $C[a,b]$ 作为所有有界函数 $M[a,b]$ 的子集，竟是无处稠密的——也就是说，在"所有有界函数"这个巨大的空间里，连续函数是极端稀有的"窄带"，随便一个开球里都挤满了不连续的函数。这个结论的反直觉程度值得停下来体会：你在微积分课里接触的函数几乎全是连续的，直觉上会觉得连续函数"到处都是"；但一旦把视野放到"所有有界函数"（绝大多数是病态的、处处振荡甚至不可积的函数），连续函数反而成了沧海一粟。这正是 Baire 纲定理登场前的"哲学预热"：数学对象的"典型性"与你在课本里遇到的"代表性"可以完全相反——课本选给学生的都是性质良好的函数，但那只是冰山一角，纲意义下的"绝大多数"函数都坏得超乎想象。对智能科学与技术专业，这个认知对"为什么需要正则化"提供了一个纯数学的注脚：机器学习里你假设目标函数光滑、可微（这是连续性的加强版），但若把目光放到"所有可能的函数"这一整体上，光滑函数和连续函数一样是无处稠密的窄带——任何光滑性假设都是在从一个极端稀有的子集里挑对象，正则化（限制范数、限制复杂度）本质上就是在做同一件事：把搜索空间从"绝大多数都很坏"的全空间，收缩到一个性质良好的窄带上。这一层类比在 §13.13 的纲论证里还会反复出现。

---

> <span style="color:#7f8c8d;">TBB §13.13, p.614</span>

<span style="color:#7f8c8d">书页 614 结束</span>


<!-- ===== W16 ===== -->

<span style="color:#7f8c8d">书页 615 · §13.13　Baire 纲定理（Baire Category Theorem）· 本节开端</span>

<span style="color:#c0392b">**§13.13　Baire 纲定理（Baire Category Theorem）**</span>

承接上一页刚确立的无处稠密（nowhere dense）定义，我们直接由此定义看到：若集合 $A$ 在任何开球（open ball）中都称不上稠密（dense），则 $A$ 就是无处稠密的。容易验证（见习题 13.13.6）：$A$ 是无处稠密的，当且仅当 $A$ 具有空内部（empty interior）。因此，一个闭集（closed set）是无处稠密的，当且仅当它的补集（complement）是稠密的。

让我们来看一些例子。

<span style="color:#2471a3;">**[example]**</span> **例 13.105（Example 13.105）：**设 $K$ 是区间 $[0,1]$ 中的 Cantor 集（Cantor set）。把它看作 $[0,1]$ 的子集时，它显然是无处稠密的。〔此地要小心：若改取度量空间（metric space）$(K,d)$，其中 $d$ 是通常度量，则 $K$ 就不再是无处稠密集了，恰恰相反，它是稠密的。〕 $\square$

> <span style="color:#7f8c8d;">TBB §13.13, p.615</span>

<span style="color:#2471a3;">**[example]**</span> **例 13.106（Example 13.106）：**我们要证明：所有连续函数（continuous function）构成的集合 $A = C[a,b]$，作为有界函数空间 $M[a,b]$ 的子集时，是无处稠密的。（再次强调，我们是在空间 $M[a,b]$ 中考察这一点，而非在 $C[a,b]$ 中。）设 $B(f,\varepsilon)$ 是 $M[a,b]$ 中的任意一个开球。我们将找出另一个开球 $B(g,\delta)$，它包含在 $B(f,\varepsilon)$ 之内，却不含 $A$ 的任何成员，也就是说，这个球 $B(g,\delta)$ 必须不含任何连续函数。

> <span style="color:#7f8c8d;">TBB §13.13, p.615</span>

现在 $f$（即 $B(f,\varepsilon)$ 的球心）可能属于 $A$，也可能不属于 $A$。我们按如下方式选取 $g$。若
```math
\limsup_{t\to a} f(t) = \liminf_{t\to a} f(t),
```
则令
```math
g(t) = \begin{cases} f(t) + \varepsilon/2, & \text{若 } t \in [a,b] \cap \mathbb{Q}, \\ f(t) - \varepsilon/2, & \text{若 } t \in [a,b] \setminus \mathbb{Q}, \end{cases} \tag{37}
```
由此得到
```math
\limsup_{t\to a} g(t) - \liminf_{t\to a} g(t) = \varepsilon. \tag{38}
```
反之，若
```math
\limsup_{t\to a} f(t) - \liminf_{t\to a} f(t) = \gamma > 0, \tag{39}
```
则对所有 $t \in [a,b]$ 令
```math
g(t) = f(t). \tag{40}
```
现在我们来确定 $\delta$，使得 $B(g,\delta)$ 恰为所需的那个球。当 (37) 适用时，取 $\delta = \varepsilon/3$；当 (39) 适用时，取 $\delta = \gamma/3$。我们必须证明
```math
B(g,\delta) \subset B(f,\varepsilon) \tag{41}
```
以及
```math
B(g,\delta) \cap A = \varnothing.
```
为验证 (41)，我们只需注意到：当 (38) 适用时，对所有 $t \in [a,b]$ 有
```math
|g(t) - f(t)| = \varepsilon/2 < \varepsilon,
```
而当 (40) 适用时，对所有 $t \in [a,b]$ 有
```math
|g(t) - f(t)| = 0 < \varepsilon.
```

---

<span style="color:#7f8c8d">书页 616 · 例 13.106 证明续 + 例 13.107　（第 13 章　度量空间 Metric Spaces）</span>

为验证 (42)，设 $h \in B(g,\delta)$。我们通过证明
```math
\limsup_{t\to a} h(t) - \liminf_{t\to a} h(t) > 0
```
来证明 $h \notin A$。由于 $h \in B(g,\delta)$，故对所有 $t \in [a,b]$ 有 $|g(t) - h(t)| < \delta$。于是
```math
\limsup_{t\to a} h(t) \geq \limsup_{t\to a} g(t) - \delta, \tag{43}
```
并且
```math
\liminf_{t\to a} h(t) \leq \liminf_{t\to a} g(t) + \delta. \tag{44}
```
用 (43) 减去 (44)，我们得到
```math
\limsup_{t\to a} h(t) - \liminf_{t\to a} h(t) \geq \limsup_{t\to a} g(t) - \liminf_{t\to a} g(t) - 2\delta.
```
当 (38) 适用时，$2\delta = 2\varepsilon/3 < \varepsilon$；当 (40) 适用时，$2\delta = 2\gamma/3 < \gamma$。现在由 (37)、(38)，或由 (39)、(40) 即可推出
```math
\limsup_{t\to a} h(t) - \liminf_{t\to a} h(t) > 0,
```
因此 $h \notin A$。 $\square$

我们注意到，本来可以给出一个略为简单的证明：只需表明 $A$ 在 $M[a,b]$ 中是闭的，且集合 $A$ 的补集在 $M[a,b]$ 中稠密即可。我们把这一做法留作习题 13.13.8。我们在下一个例子中将提供这样的论证。

<span style="color:#2471a3;">**[example]**</span> **例 13.107（Example 13.107）：**回忆有界序列空间 $\ell_\infty$，其元素为有界序列 $\{x_i\}$，度量为
```math
d_\infty(x,y) = \sup_i |x_i - y_i|
```
（参见例 13.9）。我们要证明：收敛序列（convergent sequence）构成的子集 $c$ 在 $\ell_\infty$ 中是无处稠密的。为此，我们证明 $c$ 是闭的，并且它的补集是稠密的。

> <span style="color:#7f8c8d;">TBB §13.13, p.616</span>

为验证 $c$ 是闭的，我们证明它的补集 $\ell_\infty \setminus c$ 是开的。设 $x \in \ell_\infty \setminus c$，则
```math
L = \limsup_i x_i > \liminf_i x_i = l.
```
取 $\varepsilon = (L - l)/3$。若 $d_\infty(x,y) < \varepsilon$，则
```math
\limsup_i y_i \geq L - \varepsilon/3 > l + \varepsilon/3 \geq \liminf_i y_i,
```
于是 $y \in \ell_\infty \setminus c$。这就证明了 $\ell_\infty \setminus c$ 是开的：每个 $x \in \ell_\infty \setminus c$ 都有一个包含在 $\ell_\infty \setminus c$ 中的邻域。

还需检验 $c$ 的补集是稠密的。设 $B(x,\varepsilon)$ 是 $\ell_\infty$ 中的一个开球，我们希望证明 $B(x,\varepsilon)$ 含有 $\ell_\infty \setminus c$ 中的点。若 $x \notin c$，则无须再证，故假设 $x \in c$。设 $L = \lim_i x_i$，则存在 $N \in \mathbb{N}$，使得当 $i \geq N$ 时 $|x_i - L| < \varepsilon/2$。考虑这样的序列 $y = \{y_i\}$：
```math
y_i = \begin{cases} x_i, & \text{若 } i < N, \\ L + \varepsilon/2, & \text{若 } i \geq N \text{ 且 } i \text{ 为奇数}, \\ L - \varepsilon/2, & \text{若 } i \geq N \text{ 且 } i \text{ 为偶数}. \end{cases}
```

<span style="color:#7f8c8d">*（本页在此处翻页，例 13.107 的论证在下一页继续。）*</span>


<!-- ===== W17 ===== -->

<span style="color:#7f8c8d">书页 617 · §13.13　Baire 纲定理（Baire Category Theorem）· 例 13.107 收尾 + §13.13.2 开端</span>

于是 $d_\infty(x,y) = \sup_i |x_i - y_i| < \varepsilon$，故 $y \in B(x,\varepsilon)$。但
```math
\limsup_i y_i = L + \varepsilon/2 > L - \varepsilon/2 = \liminf_i y_i,
```
于是 $y \notin c$。显然 $y \in \ell_\infty$，因此 $\ell_\infty \setminus c$ 在 $\ell_\infty$ 中是稠密（dense）的。

我们已经证明 $c$ 是闭的，并且 $\ell_\infty \setminus c$ 是稠密的，由此即知 $c$ 在 $\ell_\infty$ 中是无处稠密（nowhere dense）的。 $\square$

<hr>

<span style="color:#7f8c8d">*（本页中间部分为习题 13.13.1–13.13.10 区，按约定跳过。）*</span>

<hr>

<span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">**13.13.2　Baire 纲定理（The Baire Category Theorem）**</span>

在实直线（real line）上，Baire 纲定理断言：任意可数个无处稠密集（nowhere dense set）的并集都是"小"的，小到其补集（complement）在实直线上是稠密的。我们或可预期这一结论能推广到一般的度量空间（metric space）。

事实上只需要补充一个假设：该空间是完备的（complete）。

这样我们便得到一般度量空间中 Baire 纲定理的陈述。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">**定理 13.108（Baire）**</span>设 $(X,d)$ 是完备度量空间，并设 $S$ 是 $X$ 中可数个无处稠密集的并集。那么 $X \setminus S$ 在 $X$ 中是稠密的。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> Baire category theorem（贝尔纲定理）是全章最深刻的断言之一：完备度量空间不能被可数个无处稠密集的并集盖满；更精确地说，这些集合并集的补集仍然稠密。第一性原理：完备空间是厚实的，因为每个 Cauchy 列都有极限，没有缝隙；无处稠密集是薄片，因为每个开球里都挖得出避开它的子球；可数无穷个薄片叠起来依旧盖不住一块厚实空间。为表述方便引入术语：first category（第一纲，又称贫集）指可数个无处稠密集的并集，其补集称为 residual set（剩余集）。Baire 定理即：完备空间中剩余集稠密。
>
> 证明的精髓是嵌套闭球加完备性只用一次。任取开球 $B_0$，目标是证明 $B_0$ 碰到补集。因为 $\overline{S_1}$ 内部为空，$B_0\setminus\overline{S_1}$ 是非空开集，可取开球 $B_1$ 使 $\overline{B_1}\subset B_0\setminus\overline{S_1}$ 且半径 $<1$；归纳地，第 $n$ 步取 $B_{n+1}$ 使 $\overline{B_{n+1}}\subset B_n\setminus\overline{S_{n+1}}$ 且半径 $<1/(n+1)$。这一步可命名为“冻结切片法”：每一步把已选好的球冻结住，再针对下一张薄片 $S_{n+1}$ 切出一个更小的洞，保证新球同时避开所有已处理的薄片。归纳不变量是“$B_n$ 避开前 $n$ 张薄片”，这形似 CLRS 的 loop invariant（循环不变量）；区别在于 CLRS 的循环有限步停机、由算法本身保证终止，而这里的循环可数无限，终止由完备性这个外部引擎提供。球心列 $\{x_n\}$ 因直径趋于零而成为 Cauchy sequence（柯西列），完备性只用在这里：$x_n\to x$；对每个 $n$，$x\in\overline{B_{n+1}}\subset B_n\setminus\overline{S_{n+1}}$，所以 $x$ 落在所有 $B_n$ 里，而 $B_n$ 又避开 $\overline{S_n}\supset S_n$，故 $x$ 落在每个 $S_n$ 之外，同时 $x\in B_0$，于是 $B_0$ 与补集相交。可数多个薄片之所以盖不住，正因每个薄片只挡住一个阶段，球列却把“避开已处理薄片”这件事一路继承下去。
>
> 一个具体例子把定理落到地面：取 $\mathbb R$ 与有理数枚举 $\{q_n\}$，令 $S_n=\{q_n\}$。每个单点集无处稠密，故 $\mathbb Q=\bigcup_n S_n$ 是第一纲集；Baire 定理推出 $\mathbb R\setminus\mathbb Q$（无理数集）稠密，且 $\mathbb R$ 本身不是第一纲。这与 6.042J 形成漂亮的对照：对角线论证证明 $\mathbb R$ 不可数、$\mathbb Q$ 可数；Baire 定理证明 $\mathbb Q$ 是薄片之并、其补集稠密。两者都说“$\mathbb R$ 比 $\mathbb Q$ 大”，但“大”的含义不同：一个是基数意义（数数），一个是纲意义（厚薄），互不替代。
>
> 与前面的紧致性论证互补：紧致性靠 finite subcover（有限子覆盖），用有限多个开集控制全局，是“有限资源”型论证；这里靠完备性给极限，把一列越来越小的球的描述兑换成一个真实存在的点，是“极限”型论证。两者是分析里两座取之不尽的宝库。Strang 的 Jacobi 迭代也消费完备性：谱半径 $\rho(B)<1$ 时迭代序列是 Cauchy 列，靠 $\mathbb R^n$ 完备收敛到线性方程组的不动点解；Baire 定理同样消费完备性，但极限点不是迭代不动点，而是球套共同夹住的点。区别：Jacobi 的收敛由谱半径小于 1 驱动，Baire 的收敛由直径趋于零驱动。
>
> 历史上，René Baire（1874–1932）在 1899 年的博士论文中于实直线上建立该定理，本书把它推广到任意完备度量空间。对智能科学与技术专业，这条定理是“大多数性质 = 补集成第一纲”这套证明的源头：要证某性质对大多数对象成立，只需把坏集证成可数个无处稠密集的并，Baire 自动保证好对象的补集稠密。可命名为“坏集第一纲法”。§13.14 的诸多存在性结论几乎都从它出发；这类论证的通用套路是构造第一纲坏集再引用 Baire，例如连续但处处不可导函数的存在性就是经典一例。

---

> <span style="color:#7f8c8d;">TBB §13.13, p.617</span>

<hr>

<span style="color:#7f8c8d">书页 618 · 定理 13.108 证明 + 定义 13.109　（第 13 章　度量空间 Metric Spaces）</span>

<span style="color:#2471a3;">**[proof]**</span> <span style="color:#c0392b">**证明：**</span>设 $S = \bigcup_{n=1}^\infty S_n$，其中每个集合 $S_n$ 都是无处稠密的，并设 $B_0$ 是 $X$ 中的一个非空开球（open ball）。为证明 $X \setminus S$ 在 $X$ 中稠密，我们必须证明
```math
(X \setminus S) \cap B_0 \neq \varnothing.
```
归纳地选取一族套嵌（nested）的球
```math
B_n = B_n(x_n, r_n) \qquad (r_n < 1/n)
```
使得
```math
B_{n+1} \subset B_n \setminus \overline{S_{n+1}}.
```
为看出这是可行的，首先注意到 $B_n \setminus \overline{S_{n+1}} \neq \varnothing$，因为 $S_{n+1}$、从而 $\overline{S_{n+1}}$，都是无处稠密的。由此我们可选取 $x_{n+1} \in B_n \setminus \overline{S_{n+1}}$。

由于 $\overline{S_{n+1}}$ 是闭的，故 $\mathrm{dist}(x_{n+1}, \overline{S_{n+1}}) > 0$，因此我们能按所需选取 $B_{n+1}$。

序列 $\{x_n\}$ 是 Cauchy 序列（Cauchy sequence），因为当 $n, m \geq N$ 时，
```math
d(x_n, x_m) \leq d(x_n, x_N) + d(x_N, x_m) < 2/N.
```
由于 $X$ 是完备的，存在 $x \in X$ 使得 $x_n \to x$。但对所有 $n$ 都有 $x_{n+1} \in B_{n+1}$，于是
```math
x \in \bigcap_{n=1}^\infty B_n \subset B_0 \cap (X \setminus S),
```
正如我们所要证明的。 $\square$

下列术语是标准的：

<span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">**定义 13.109：**</span>设 $(X,d)$ 是度量空间。

> <span style="color:#7f8c8d;">TBB §13.13, p.618</span>

1. 若集合 $A \subset X$ 是可数个无处稠密集的并集，则称 $A$ 为第一纲集（first category set）。
2. 不属于第一纲的集合称为第二纲集（second category set）。
3. 第一纲集的补集称为剩余集（residual set）。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> category（纲）这套词汇真正的野心，是造一把不靠概率的大小标尺。先看零件：一个集合 $A$ 在空间 $X$ 中无处稠密（nowhere dense），指它的闭包 $\overline{A}$ 没有内点，等价地说，任何开球里都能再找到一个更小的开球与 $A$ 不相交；直觉上它是薄片，任何局部都盖不满一丁点体积。第一纲（first category）等于可数个无处稠密集之并，形象地说就是把至多可数层薄片叠起来；第二纲就是非第一纲；剩余集（residual set）等于第一纲集的补集。这条标尺有一项厚集不动的性质：剩余集的超集仍是剩余集，且剩余集的可数交仍是剩余集——正因为如此它才当得起尺子，否则补集一放大就失效。
>
> 这里最关键的认识是：剩余集并非体积意义上的大半，而是稠密加可数交之下仍大的两栖性大，这正是定理 13.108 直接赋予的结果。其第一性原理在于：在完备度量空间里，可数个稠密开集的交仍然稠密。构造上，你从任意开球出发，逐层在每个稠密开集 $G_n$ 里选一个半径越来越小的闭球，球心序列成为 Cauchy 列；完备性保证它收敛，极限点落在所有 $G_n$ 里，也落在出发球里。换句话说，稠密性负责处处都有，完备性负责可数次也不丢，二者合起来才保证剩余集在可数交下仍大。这是一种拓扑势序上的 genericity（一般性），没有概率分布、没有随机抽样；数学里普遍成立可以出自完全不同的理由——这与你熟悉的那种靠测度或计数的多数是两把尺子。
>
> 看一个具体例子：平面 $\mathbb{R}^2$ 中至少有一个坐标是有理数的点集 $(\mathbb{Q}\times\mathbb{R})\cup(\mathbb{R}\times\mathbb{Q})$，它是可数条竖直线与可数条水平线的并，每条线都是闭而无内的薄片，所以它是第一纲；于是它的补集——两个坐标都为无理数的点——是剩余集。注意这个断言不依赖面积，只依赖开球结构，这正是纲的尺度和体积尺度的分野。
>
> 这把尺子在计算机科学里同样吃香。6.042J 的可数性告诉我们，可数个可数集之并仍可数，所以可数并在规模上是可控的；但纲的精细之处在于，被并的对象必须是无处稠密的薄片，而不是随便什么小集。CSAPP 的 IEEE 754 浮点数集在 $\mathbb{R}$ 中只有有限个元素，每个浮点数都是孤立点，整个格点集闭而无内，因而无处稠密；于是几乎所有实数都不能被任何 bit pattern（位模式）精确编码，舍入（rounding）本质上就是把一个剩余集意义上的典型实数投影到这个无处稠密的格点上。CLRS 的 average-case（平均情形）复杂度需要一个显式的输入分布，而纲给出的 genericity 不靠分布，只靠拓扑结构——这是两种典型的区别，也正是用一般情形论证算法性能、随机初始化鲁棒性时纲可以兜底的缘故。
>
> 务必记住它的相对性（见例 13.112）：同一个集合在甲空间是第一纲、在乙空间可以是第二纲，因为无处稠密始终默认了所在空间。这也为日后接触测度论中的 almost everywhere（几乎处处）预先埋线：那将是另一把尺子，同一集合在纲和测度下可以给出相反的结论。可复用的命名模板是“可数薄片—补集取大”三步法：先锚定所在空间，再把坏集写成可数层无处稠密薄片之并，最后宣布补集为剩余集。

对于完备度量空间而言，按纲（category）的意义，第一纲集是"小"集，而剩余集是"大"集。第二纲集仅仅是"不小"。

剩余集之所以"大"，是因为它们是稠密的，且一列剩余集的交集仍是稠密的。第一纲集之所以"小"，是因为（尽管它们可能稠密）它们的补集总是稠密的，并且一列第一纲集的并集的补集仍然稠密。

对于不完备的空间，剩余集可能为空。还要注意，所有这些关于空间中集合的陈述都是相对于所考察的空间而言的。一个集合


<!-- ===== W18 ===== -->

<span style="color:#7f8c8d">书页 619 · §13.13：Baire 纲定理（续，接前一书页）</span>

（承上页）某个集合可能作为某个空间的子集是第一纲（first category）的，但作为另一个空间的子集却不是如此。

<span style="color:#2471a3;">**[example]**</span> <span style="color:#cd6155;">**例 13.110**</span>：有理数集 $\mathbb{Q}$ 作为 $\mathbb{R}$ 的子集是稠密的（dense）。

> <span style="color:#7f8c8d;">TBB §13.13, p.619</span>

它同时也是第一纲的，因为对每个 $q\in\mathbb{Q}$，单点集 $\{q\}$ 都是 $\mathbb{R}$ 的无处稠密（nowhere dense）子集，并且

```math
\mathbb{Q}=\bigcup_{q\in\mathbb{Q}}\{q\}
```

式 (45) 把 $\mathbb{Q}$ 表示为可数个无处稠密集的并。

注意这一点也意味着无理数集是剩余集（residual）。$\square$

<span style="color:#2471a3;">**[example]**</span> <span style="color:#cd6155;">**例 13.111**</span>：整个不完备度量空间 $\mathbb{Q}$（赋以通常实度量）属于第一纲。

> <span style="color:#7f8c8d;">TBB §13.13, p.619</span>

式 (45) 再次可用来把这个空间表示为在其中对 $\mathbb{Q}$ 无处稠密的集合的可数并。

于是 $\mathbb{Q}$ 在 $\mathbb{Q}$ 中的补集，即空集 $\varnothing$，按我们的定义将是一个剩余集。（在不完备度量空间中，剩余集不一定是"大的"。）$\square$

<span style="color:#2471a3;">**[example]**</span> <span style="color:#cd6155;">**例 13.112**</span>：考虑 $\mathbb{R}$ 的子空间 $\mathbb{N}$。

> <span style="color:#7f8c8d;">TBB §13.13, p.619</span>

作为 $\mathbb{R}$ 的子集，$\mathbb{N}$ 属于第一纲，因为对每个 $n$，$\{n\}$ 在 $\mathbb{R}$ 中都是无处稠密的，且

```math
\mathbb{N}=\bigcup_{n=1}^{\infty}\{n\}
```

式 (46) 把 $\mathbb{N}$ 表示为可数个无处稠密集的并。

但若把 $\mathbb{N}$ 视为一个空间本身，它是一个完备度量空间。

由 Baire 纲定理，它不能被表示为可数个无处稠密集的并。

然而这怎么可能呢？式 (46) 不是把 $\mathbb{N}$ 表示为可数个无处稠密集的并吗？

事实上请注意，在空间 $\mathbb{N}$ 中，每个集合 $\{n\}$ 在 $B(n,\tfrac12)$ 中都是稠密的。

$\mathbb{N}$ 中唯一的剩余集就是 $\mathbb{N}$ 本身，而只有空集 $\varnothing$ 才是无处稠密的或第一纲的。$\square$

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 三个例子看似重复，实则在用具体空间澄清同一件事——纲的一切断言都相对所含空间而成立。先看 $\mathbb{Q}$ 在 $\mathbb{R}$ 中。稠密性的机制是：任给两个实数，总能取足够大的整数 $n$，使区间长度超过 $1/n$，从而在两个实数之间夹进一个有理数。第一纲的机制是：把 $\mathbb{Q}$ 写成可数个单点 $\{q\}$ 的并（例 13.110）；在 $\mathbb{R}$ 中每个单点闭而无内，因为任何开区间都装不下一个点，所以无处稠密；可数并给出第一纲。于是无理数集 $\mathbb{R}\setminus\mathbb{Q}$ 是剩余集：无理数是绝大多数实数这个反直觉判断被严格化，而且它同时稠密，这正是注释 26 说的两栖性大。换句话说，单点薄片的可数并盖不出任何开区间，但它的补集却处处有据点。
>
> 同一套计数还能把代数数也判成极少。6.042J 的可数性给出：整系数多项式按次数加系数的配对编码可数，每个多项式只有有限个根，可数个有限集的并仍可数，所以代数数可数；在 $\mathbb{R}$ 里可数集就是可数个单点的并，从而是第一纲，于是超越数集是剩余集。这呼应书页 620 追忆的 Cantor 论证，但要注意区别：Cantor 原证用的是 6.042J 的对角线论证，得到的是基数意义上的多——超越数不可数而代数数可数；这里用的是 Baire 纲，得到的是拓扑意义上的多——超越数剩余。两把尺子可以打架：Cantor set（Cantor 集）在 $\mathbb{R}$ 中不可数，却无处稠密、从而是第一纲，基数大不等于拓扑厚。这正是需要把纲和计数分开的原因。
>
> 例 13.111 用不完备的 $\mathbb{Q}$ 本身当空间，给出致命警示：把空间从 $\mathbb{R}$ 换成 $\mathbb{Q}$，同一个集合的纲可以反转，因为剩余集是相对给定空间取的。在 $\mathbb{Q}$ 里，单点 $\{q\}$ 的闭包还是 $\{q\}$，而它的内部仍空，因为任何有理区间都含无穷多个有理数，装不下单点，所以 $\mathbb{Q}$ 在自己的空间里仍可写成可数个无处稠密单点之并；于是 $\mathbb{Q}$ 作为空间是第一纲，它的补集——在 $\mathbb{Q}$ 内部的剩余集——是空集。完备性在这里缺席，定理 13.108 的嵌套球构造会卡在 Cauchy 列没有极限：比如 $\sqrt{2}$ 的十进制截断列 $1.4,1.41,1.414,\ldots$ 是 $\mathbb{Q}$ 中的 Cauchy 列，却无处收敛。所以剩余集必大是完备空间的特权，不是纲定义免费送的。
>
> 例 13.112 最精妙：把 $\mathbb{N}$ 当作独立空间，它完备，因为任意两个自然数距离至少 $1$，Cauchy 列最终常数，按定理 13.108 不该是第一纲。可它作为集合仍可写成可数个单点之并，矛盾吗？不矛盾，因为每个单点在自己空间里并不无处稠密：半径 $1/2$ 的球里只有它自己，单点是开集，闭包有非空内部。相对性的机制是：子空间里的开集是原空间开集与子空间的交，闭包与内部也都要回到所在空间计算；同一个集合换空间后，薄片可能变厚块。可复用的命名模板是“锚定空间三步”：先问在哪个空间、再用 $\operatorname{int}_X(\overline{A})=\emptyset$ 检验无处稠密、最后才谈纲；这正是 §13.13 最容易踩空的地方。

---

<span style="color:#7f8c8d">*（本页其余部分为 §13.13 习题区 Exercises 13.13.11–13.13.17，按约定跳过。）*</span>

<span style="color:#7f8c8d">书页 620 · §13.13 习题收尾 + §13.14 Baire 纲定理的应用</span>

<span style="color:#7f8c8d">*（书页 620 开头为习题区 Exercises 13.13.18–13.13.19，内容涉及 $c_0$、$c_{\mathbb{Q}}$ 序列空间，按约定跳过。）*</span>

## <span style="color:#2471a3;">**[section]**</span> 13.14 Baire 纲定理的应用（Applications of the Baire Category Theorem）

<span style="color:#7f8c8d">*（本章为拓展小节，可省略。）*</span>

Baire 纲定理有大量应用。

纲论证（category arguments）与紧致性论证（compactness arguments）相结合，是数学分析中最有力、最常用的工具之一。

我们已经在前面遇到过 Baire 纲定理的一些简单应用（定理 6.13、习题 6.4.7 与 13.13.17）。

前两个是展示某些"逐点"（pointwise）条件实际上在某个开集上"一致"（uniformly）成立的定理。

第三个表明，没有一个孤立点（isolated points）的完备度量空间不可能是可数的。

在本节中，我们强调运用 Baire 纲定理来证明一些难以想象或难以构造的对象的存在性。

其方法是将这些对象视为某个适当完备度量空间的成员，然后说明具有所需性质的对象在该空间中构成一个剩余子集。

在这里我们会想起 Cantor 的一个论证。

超越实数（transcendental real numbers）是否存在？

非超越数（即代数数，algebraic numbers）构成一个可数的实数集合。

剩下的是一个很大的稠密数集，因此超越实数不仅存在，而且极其丰富（详见习题 2.3.10）。

此处我们本质上把同样的推理运用于完备度量空间：我们力图证明其存在的那些对象，正是该空间中移除一个第一纲集合后余下的对象。

由 Baire 纲定理，它们必然大量存在，在该空间中构成一个既稠密又剩余（residual）的集合。

### <span style="color:#2471a3;">**[section]**</span> 13.14.1 图形"不穿过任何直线"的函数（Functions Whose Graphs "Cross No Lines"）

我们先从一个对象为连续函数的例子开始。

我们在初等微积分中遇到的连续函数具有这样的性质：存在许多穿（cross）过函数图形的直线。

让我们把"穿过直线"（crossing lines）这个概念精确化。

我们指的无非是：直线在某个点的一侧位于图形上方，在另一侧位于图形下方。

这个形式化定义看起来相当吓人，但它只是表达了这一基本想法。

<span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f;">**定义 13.113**：设 $f:[a,b]\to\mathbb{R}$，并设 $L:\mathbb{R}\to\mathbb{R}$ 是一个图形为直线的函数。我们说 $L$ 穿过 $f$（或 $f$ 穿过 $L$）是指：存在 $x_0\in[a,b]$ 与 $\delta>0$，使得 $f(x_0)=L(x_0)$ 且要么……</span>

> <span style="color:#7f8c8d;">TBB §13.14, p.620</span>

<span style="color:#7f8c8d">*（定义 13.113 中"要么"后的两种情形在书页 620 末尾截断，接续至下一书页 621。）*</span>


<!-- ===== W19 ===== -->

<span style="color:#7f8c8d">书页 621</span>

# <span style="color:#c0392b">§13.14 Baire 纲定理的应用</span>

<span style="color:#2471a3;">**[figure]**</span> 图 13.9：$f(x) = \sqrt{|x|}\sin(1/x)$ 与 $g(x) = |f(x)|$ 的图像。渐近线 $y = \pm\sqrt{|x|}$ 也一并画出。

我们说直线 $y = f(x_0) + \gamma(x - x_0)$ 在点 $x_0$ 处**穿过（crosses）**函数 $f$ 的图像，

如果对某个 $\delta > 0$，以下两种情形之一成立：

(i) 对所有 $x \in [x_0 - \delta, x_0] \cap [a, b]$ 有 $L(x) \leq f(x)$，且对所有 $x \in [x_0, x_0 + \delta] \cap [a, b]$ 有 $L(x) \geq f(x)$，或者

(ii) 对所有 $x \in [x_0 - \delta, x_0] \cap [a, b]$ 有 $L(x) \geq f(x)$，且对所有 $x \in [x_0, x_0 + \delta] \cap [a, b]$ 有 $L(x) \leq f(x)$。

<span style="color:#2471a3;">**[example]**</span> **例 13.114**：考虑函数 $f(x) = \sin x$。在点 $x = 0$ 处，$x$ 轴（即水平线 $y = 0$）穿过 $f$，

> <span style="color:#7f8c8d;">TBB §13.14, p.621</span>

这是因为在区间 $(-\pi, \pi)$ 中，直线在左侧 $(-\pi, 0)$ 位于 $f$ 的图像上方，在右侧 $(0, \pi)$ 位于下方。

实际上，每条过 $(0, 0)$ 的直线都穿过 $f$。在点 $(\pi/2, 1)$ 处，除了水平线 $y = 1$ 外，每条过该点的直线都穿过 $f$。

由于直线 $y = 1$ 始终保持在 $f$ 的图像上方，它不穿过。

$\square$

这个例子中的情况是微积分中我们熟悉的函数的典型情形。

对这类函数而言，几乎每条直线都穿过图像，可能只有切线不穿过。

<span style="color:#2471a3;">**[example]**</span> **例 13.115**：我们很容易给出连续函数的例子，它们在特定点附近"摆动"得如此剧烈，

> <span style="color:#7f8c8d;">TBB §13.14, p.621</span>

以至于不可能有任何直线在该点穿过图像。函数

```math
f(x) = \sqrt{|x|}\sin(1/x),\quad f(0) = 0
```

以及 $g(x) = |f(x)|$ 在点 $(0, 0)$ 处说明了这一点。

注意在 $f$ 或 $g$ 图像上的所有其他点，都有许多直线穿过（图 13.9）。

$\square$

尽管很难想象一个不被任何直线穿过的连续函数，而且构造它更加困难，

但我们将看到，"大多数"（在纲的意义下）连续函数都具有这个性质。

在 §13.14.2 和 §13.14.3 小节中，我们将利用这一点来证明，"大多数"连续函数在任意区间上都不是单调的，且在任意点都不可导。

在陈述定理 13.116 之前，我们先引入一些记号，这会方便我们的证明。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 本节用纲论证证明一连串反直觉的绝大多数：绝大多数连续函数的图像不被任何直线穿过（定理 13.116），绝大多数连续函数在任何区间上都不单调（定理 13.118），绝大多数连续函数处处不可导（定理 13.119）。这里的绝大多数全部是注释 26 的 genericity 意义：在 $C[0,1]$（配备一致范数 $\|f\|=\sup_{x\in[0,1]}|f(x)|$，完备）里取剩余集。先拆解这套论证的发动机——“纲论证三步模板”：第一步，把想排除的坏对象按坏的程度用一个自然数参数 $n$ 分层，写成可数个集合 $A_1,A_2,\ldots$ 的并；第二步，逐层证明每个 $A_n$ 是闭的且无处稠密的，闭性保证取极限不会逃出，无处稠密保证它薄到不占任何开球；第三步，调用 Baire 纲定理（定理 13.108）断言这个可数并是第一纲，于是它的补集——好对象的集合——是剩余集，即纲意义下的绝大多数。
>
> 模板的迷你版先跑一遍：在 $\mathbb{R}$ 中把坏集 $\mathbb{Q}$ 编号成 $A_n=\{q_n\}$，每个 $A_n$ 闭而无处稠密，可数并第一纲，补集无理数剩余。函数空间里的定理 13.116 只是把同样的三层结构搬过去，但每层的证明要动用一致收敛。这里直线穿过图像理解为 cross（横穿）：在交点两侧图像分别落在直线的两侧。若 $f$ 在 $[c,d]$ 上单调且 $f(c)\neq f(d)$，则任一介于 $f(c)$ 与 $f(d)$ 之间的水平线都被图像从下穿到上，介值定理加单调性保证恰有一次横穿；若 $f$ 在 $x_0$ 可微，则过 $(x_0,f(x_0))$ 的任一条非切线，其斜率 $m\neq f'(x_0)$，在局部一阶展开里差为 $(f'(x_0)-m)(x-x_0)+o(|x-x_0|)$，符号在 $x_0$ 两侧变号，于是横穿图像。反过来，不被任何直线横穿的函数必不单调于任何区间、也必不可微于任何点；常值函数这类退化情形单独处理，它们显然不构成开球，同样落进第一纲。这就是定理 13.118 与 13.119 几乎白手起家的原因：Z 集（不被任何直线横穿的函数族）是剩余集，而它包含在无处单调函数族和无处可微函数族里，剩余集的超集仍是剩余集——一旦定理 13.116 得证，比它更坏的两族函数自动跟着变成剩余集，一个子列抽取都不用重做。
>
> 定理 13.116 的证明本身还有个值得单独圈出的招式：对点列 $x_k$ 与斜率 $\gamma_k$ 各用一次 Bolzano-Weierstrass 抽取收敛子列——这就是注 13.97 提过的 diagonal extraction（对角线抽取）的又一实例。注意它和 6.042J 的 Cantor 对角线论证是两回事：后者是构造反例，前者是把二维的逃逸（既换点又换斜率）拆成两次一维的压缩——先在紧区间 $[0,1]$ 上抽 $x_{k_j}\to x$，再在斜率的有界区间 $[-n,n]$ 上沿该子列抽 $\gamma_{k_{j_l}}\to\gamma$，同一组指标让两坐标同时收敛；最后一致收敛把横穿关系原封不动地传到极限函数。类比 Strang 里 Jacobi 迭代：那里收敛判据是 spectral radius（谱半径）$\rho(B)<1$，因为误差满足 $e_{k+1}=Be_k$，范数按谱半径收缩；这里函数列的收敛用一致范数度量，是同一套范数加极限思想的连续版本，区别在于一个在有限维向量空间、一个在无穷维函数空间。
>
> 历史侧写值得较真一次：Weierstrass 是在 1872 年 7 月 18 日向柏林科学院演讲中给出那个著名的处处连续、处处不可微的函数（级数形式 $W(x)=\sum a^n\cos(b^n\pi x)$，取 $ab>1+\tfrac32\pi$ 的奇数 $b$），该例直到 1875 年才由 du Bois-Reymond 公开发表——注意不是 1875 年构造。而真正在纲的意义上证明绝大多数连续函数处处不可微的，是 Banach 与 Mazurkiewicz 于 1931 年各自独立用 Baire 纲定理完成的，距 Weierstrass 的例子已近六十年。这条时间线本身就是本节的注脚：一个 19 世纪被当作病态怪物的个例，要等 Baire 纲这套大小理论成熟后，才被翻案成典型长相。

---

设 $f \in C[a, b]$，且 $\gamma \in \mathbb{R}$，定义函数 $f_{-\gamma}$ 为

```math
f_{-\gamma}(x) = f(x) - \gamma x.
```

因此，$f_{-\gamma}$ 是通过从 $f$ 中减去线性函数 $L(x) = \gamma x$ 得到的。

不难发现，斜率为 $\gamma$ 的直线在 $x_0$ 处穿过 $f$ 的图像当且仅当相应的水平线在 $x_0$ 处穿过 $f_{-\gamma}$ 的图像。

---

<span style="color:#7f8c8d">书页 622</span>

<span style="color:#2471a3;">**[theorem]**</span> **定理 13.116**：集合

> <span style="color:#7f8c8d;">TBB §13.14, p.622</span>

```math
Z = \{f \in C[a, b] : f \text{ 不被任何直线穿过}\}
```

是 $C[a, b]$ 中的一个剩余集（residual subset）。

<span style="color:#2471a3;">**[proof]**</span> 我们希望将 $X \setminus Z$ 表示为可数个无处稠密集的并。注意到如果 $f \in X \setminus Z$，

则至少存在一条直线在某点 $x$ 处穿过 $f$。用专业术语来说，$f$（或 $-f$）属于如下定义的集合 $A_n$ 之一。

对每个 $n \in \mathbb{N}$，令 $A_n$ 表示所有满足以下条件的函数 $f \in C[a, b]$：存在 $\gamma \in [-n, n]$ 和 $x \in [a, b]$，使得

```math
f_{-\gamma}(t) \leq f_{-\gamma}(x) \quad \text{当} \quad t \in [a, b] \cap (x - 1/n, x)
```

且

```math
f_{-\gamma}(t) \geq f_{-\gamma}(x) \quad \text{当} \quad t \in [a, b] \cap (x, x + 1/n).
```

事实上，如果 $f \in A_N$，则对所有 $n > N$ 也有 $f \in A_n$。

注意数 $n$ 在这个定义中扮演两个角色。要使一个函数属于 $A_n$，必须至少存在一条斜率在 $-n$ 和 $+n$ 之间的直线穿过该函数。

此外，$1/n$ 指定了一个区间的长度，直线必须在该区间内（再次穿过之前）保持在函数的上方或下方。

令 $A = \bigcup_{n=1}^\infty A_n$。我们将证明对每个 $n \in \mathbb{N}$，$A_n$ 是闭集且 $A_n$ 的补集是稠密的。

由此可得每个 $A_n$ 都是无处稠密的，因此 $A$ 是 $C[a, b]$ 中的第一纲（first category）子集。

为了验证 $A_n$ 是闭集，设 $\{f_k\}$ 是 $A_n$ 中满足 $f_k \to f$（在空间 $C[a, b]$ 中）的函数序列。我们必须证明 $f \in A_n$。

对每个 $k \in \mathbb{N}$，函数 $f_k$ 是 $A_n$ 的成员，因此存在 $\gamma_k \in [-n, n]$ 和 $x_k \in [a, b]$，使得

```math
f_{k-\gamma_k}(t) \leq f_{k-\gamma_k}(x_k) \quad \text{当} \quad t \in [a, b] \cap (x_k - 1/n, x_k)
```

且

```math
f_{k-\gamma_k}(t) \geq f_{k-\gamma_k}(x_k) \quad \text{当} \quad t \in [a, b] \cap (x_k, x_k + 1/n).
```

对点列 $\{x_k\}$ 应用 Bolzano-Weierstrass 定理（定理 2.40），存在子列 $\{x_{k_i}\}$ 收敛到 $[a, b]$ 中的某点 $x_0$。

再次应用 Bolzano-Weierstrass 定理，我们从该序列中得到一个子列 $\{x_{k_{i_j}}\}$，使得 $\{\gamma_{k_{i_j}}\}$ 收敛到某个 $\gamma_0 \in [-n, n]$。

不难验证（习题 13.14.1）

```math
f_{-\gamma_0}(t) \leq f_{-\gamma_0}(x_0) \quad \text{当} \quad t \in [a, b] \cap (x_0 - 1/n, x_0)
```

且

```math
f_{-\gamma_0}(t) \geq f_{-\gamma_0}(x_0) \quad \text{当} \quad t \in [a, b] \cap (x_0, x_0 + 1/n).
```

因此 $f \in A_n$。由于对从 $A_n$ 中选取的所有收敛序列这都成立，我们得出结论：$A_n$ 在 $C[a, b]$ 中是闭集。

为了证明 $A_n$ 是无处稠密的，我们验证 $C[a, b]$ 中的每个开球都包含不属于 $A_n$ 的点。

设 $B(g, \varepsilon)$ 是 $C[a, b]$ 中的一个开球。我们不难直观看出（尽管解析验证很繁琐），

可以选取一个具有许多陡峭齿的适当锯齿函数 $f$，使得 $f \in B(g, \varepsilon) \setminus A_n$。

<span style="color:#7f8c8d">*（本页剩余为证明后半部分与后续内容。）*</span>


<!-- ===== W20 ===== -->

<span style="color:#7f8c8d">书页 623 — Section 13.14 Applications of the Baire Category Theorem（接上一页）</span>

<span style="color:#2471a3;">**[section]**</span> **§13.14 应用 Baire 纲定理（Baire Category Theorem）收尾**

图中标注的 $g+\varepsilon$、$g$、$f$、$g-\varepsilon$ 四条水平线，刻画了锯齿函数与带状邻域 $B(g,\varepsilon)$ 的几何关系。

<span style="color:#2471a3;">**[figure]**</span> 图 13.10（Figure 13.10）：锯齿函数（sawtooth function）$f$ 在一个长度为 $1/n$ 的区间上的图像。

直觉上说，构成 $f$ 图像的那些线段斜率如此陡峭，且线段又多到如此程度，以致任何斜率介于 $-n$ 与 $n$ 之间的直线，都无法像要求 $f\in A_n$ 那样去穿过该图像。[参见图 13.10：图中所示区间长度为 $1/n$。这些"牙齿"的斜率极大，使得斜率介于 $+n$ 与 $-n$ 之间的任何直线都无法在此区间内恰好穿过 $f$ 一次。这说明 $f\in B(g,\varepsilon)\setminus A_n$。]

因此 $A_n$ 无处稠密（nowhere dense），于是 $A$ 为第一纲（first category）集合。

完全相同的论证可表明集合 $B=\{\,f\in C[a,b] \,:\, -f\in A\,\}$ 也是第一纲的。

从而 $A\cup B$ 是第一纲的，由此可知 $Z=C[a,b]\setminus(A\cup B)$ 是剩余集（residual）。

可以验证，$Z$ 中每一成员都穿过不了任何直线（crosses no lines）。

$\square$

<span style="color:#7f8c8d">*（书页 623 其余部分为 §13.14 Exercises 习题区（13.14.1、13.14.2），按约定跳过。）*</span>

<span style="color:#2471a3;">**[section]**</span> **§13.14.2 无处单调函数（Nowhere Monotonic Functions）**

在微积分课程中我们遇到的一切连续函数，要么是单调的，要么就是分段单调的（piecewise monotonic）：它们在某些区间上不递减，而在其余的区间上不递增。

事实上，要想象一个行为与此不同的连续函数是极其困难的。

那么，是否可能证明存在如以下定义所表达的那种意义上的连续无处单调函数（nowhere monotonic functions）呢？

<span style="color:#7f8c8d">书页 624 — Metric Spaces，Chapter 13（续 §13.14.2）</span>

<span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">**定义 13.117（Definition 13.117）**：区间 $[a,b]$ 上的函数 $f$ 被称为**无处单调**，如果不存在子区间 $[c,d]\subset[a,b]$ 使得 $f$ 在 $[c,d]$ 上单调。</span>

> <span style="color:#7f8c8d;">TBB §13.14, p.624</span>

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">**定理 13.118（Theorem 13.118）**：连续且无处单调的函数类构成 $C[a,b]$ 的一个剩余子集（residual subset）。</span>

> <span style="color:#7f8c8d;">TBB §13.14, p.624</span>

<span style="color:#2471a3;">**[proof]**</span> **证明**：当一个连续函数 $f$ 在区间 $[c,d]$ 上单调时，显然会有许多直线穿过 $f$。

事实上，对于介于 $f(c)$ 与 $f(d)$ 之间的每一水平线 $y=k$，都必须穿过 $f$。

因此，上一节（定理 13.116）所讨论的函数类 $Z$ 中的任一成员，都不可能在任何区间上单调。

于是，由于无处单调函数之集**包含**剩余集 $Z$，从而也必为剩余集，本定理便可直接由定理 13.116 推出。

$\square$

<span style="color:#2471a3;">**[section]**</span> **§13.14.3 连续无处可微函数（Continuous Nowhere Differentiable Functions）**

至此，我们已借助直线穿过论证（line crossing arguments）连同 Baire 纲论证，证明了一类难以形象化的、具有几何性质的连续函数的存在性。

下面让我们转向一个同样难以形象化的分析性质。

构造一个处处没有导数的函数其实很容易：只需取一个处处不连续的函数即可。

但能否存在一个处处没有导数的**连续**函数呢？

函数 $f(x)=|x|$ 说明了如何安排至少一个不可微点。

任意有限多个点也能同样容易地处理。

十九世纪早期，不少数学家颇为确信事情不可能比这更进一步。

事实上，他们中有些人还"证明"了连续函数必定存在可微点。

到十九世纪中叶，许多数学家已意识到存在处处没有可微点的连续函数。

这类函数的构造涉及对无穷级数求和，其相继各项越来越多地贡献于其和的不可微性（nondifferentiability）。

此类构造中最著名的之一，由 Weierstrass 约在 1875 年给出。

而运用 Baire 纲定理来证明此类函数的存在，则须等到 1931 年，当时两位波兰数学家 Stefan Banach（1892–1945）与 Stefan Mazurkiewicz（1888–1945），在《Studia Mathematica》期刊上各自独立的论文中，给出了这样的证明。

我们称一个函数为无处可微（nowhere differentiable）的，如果它在任何点处都没有有限导数。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">**定理 13.119（Theorem 13.119）**：连续且无处可微的函数类构成 $C[a,b]$ 的一个剩余子集。</span>

> <span style="color:#7f8c8d;">TBB §13.14, p.624</span>

<span style="color:#2471a3;">**[proof]**</span> **证明**：注意，若一个连续函数在点 $x_0\in(a,b)$ 处可微，且 $f'(x_0)=\gamma$，那么任何斜率不等于 $\gamma$ 且通过点 $(x_0,f(x_0))$ 的直线都将穿过 $f$。

这蕴含定理 13.116 中所讨论的函数类 $Z$ 的每个成员都在任何点处不可微。

于是，由于无处可微函数之集包含剩余集 $Z$，从而也必为剩余集，本定理便直接由定理 13.116 推出。

$\square$


<!-- ===== W21 ===== -->

<span style="color:#7f8c8d">书页 625 — Section 13.14 Applications of the Baire Category Theorem（接上一页）</span>

<span style="color:#2471a3;">**[section]**</span> **§13.14 应用 Baire 纲定理（Baire Category Theorem）续**

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> Baire category（纲）说"大多数"时，用的是一把和"个数"完全不同的尺子：一个集合若能被表成可数个 nowhere dense（无处稠密）集的并，就称为 first category（第一纲），在纲的天平上视为"瘦"。Cantor 三分集无处稠密，所以它瘦到可以忽略，可它偏偏不可数。这个反直觉与 CSAPP 第 2.4 节的 floating point（浮点）世界惊人地同构。
>
> IEEE 754 的 single precision（单精度）float 与 double precision（双精度）double 用固定位数的 sign（符号位）、exponent（阶码）、fraction（尾数）编码：单精度 32 位、双精度 64 位，因此全体可表示浮点数只是有限个 bit pattern（位模式）的集合，当然可数（双精度至多 $2^{64}$ 个，还要扣除 NaN（非数）、无穷大等特殊值）。于是单位区间 $[0,1]$ 中能被精确表出的只有极少数 binary rational（二进制有理数，分母为 $2$ 的幂），绝大多数实数是机器里不可表示的。你写下的 $0.1$（即 $\frac{1}{10}$，分母含因子 $5$，不是 $2$ 的幂，二进制下必然无限循环），其二进制展开是 $0.0001100110011\ldots_2$，"$0011$"无限循环，而双精度尾数只有 $52$ 位，存进去的其实是它的最近二进制近似 $0.1000000000000000055511151231257827021181583404541015625$，误差约 $5.55\times10^{-18}$；在 $1$ 附近，相邻双精度数的间距约 $2^{-52}\approx2.22\times10^{-16}$，这就是 rounding（舍入）的量子。任何有限编码都必然如此：有限个位模式只能给出有限个精确值，其余实数只能被舍入到最近的可表示点。
>
> 这与 Cantor 三分集几乎完全平行：一个实数若三进制展开含数字 $1$，就在挖洞时被删掉——含 $1$ 被排斥；浮点世界则被有限尾数卡住——二进制展开无限长的数被排斥出可表示集。两种排斥机制不同：一个是三进制符号禁忌，一个是位宽截断；但结构性结论相同：一个在集合论上巨大（不可数）的类，在度量/测度天平上渺小到可以忽略。更具体地，三分构造挖掉的区间总长 $\frac{1}{3}+\frac{2}{9}+\frac{4}{27}+\cdots=1$，所以 Cantor 集的 Lebesgue measure（勒贝格测度）为零；浮点可表示集作为有限集更是测度为零。
>
> 从第一性原理看，这不是浮点实现的缺陷，而是实数不可数（6.042J）的必然代价。6.042J 的 diagonal argument（对角线论证）证明：任何把实数编码进可数符号表的方案，必然漏掉不可数多个实数；CSAPP 的浮点把"可数资源"具体化为 $2^{64}$ 个双精度位模式，可数份资源永远喂不满不可数的连续统——哪怕把字长从 $64$ 位提到任意有限位，漏掉的仍是"几乎所有"实数。区别在于：6.042J 只保证存在漏网之鱼，而测度与纲进一步说漏掉的不是个别，而是绝大多数——可数集同时是 Lebesgue measure zero（勒贝格测度零）集与第一纲集。
>
> 这个论证可以命名复用：bit-pattern fence argument（位模式栅栏论证）——任何有限或可数编码都竖起一道栅栏，栅栏内至多可数，栅栏外是不可数连续统，于是"精确表示"永远只能覆盖可忽略子集；再配一把"基数—测度双标尺"：基数尺说可表示集至多可数而实数不可数，测度尺说可数集测度为零。反过来看，罕见却被反复依赖恰是这些数学结构"少即是力量"的另一注脚：浮点正是靠有限个精确点加舍入规则，把不可数连续统压缩进 $64$ 位，撑起了整个数值计算。

---

<span style="color:#2471a3;">**[note]**</span> <span style="color:#1e8449">**注**：事实上，更细致的分析表明，对每个 $f\in Z$，$+\infty$ 与 $-\infty$ 都是 $f$ 在每个点处的导出数（derived numbers）。</span>

关于 Dini 导数（Dini derivatives）与导出数的讨论参见第 7.8 节。

我们把这一分析留作习题 13.14.2。

<span style="color:#2471a3;">**[section]**</span> **§13.14.4 Cantor 集（Cantor Sets）**

现在我们转向一个研究对象是闭集的例子。

回忆关于实数的 Cantor 三进位（ternary）集合，即"三分集"（middle-third set），它是最早的非空、无处稠密（nowhere dense）且无孤立点的实数集例子。

对十九世纪的数学家而言，这样的集合极难形象化，在 Cantor 的构造为人所知之前，人们犯过许多错误。

为向 Cantor 致敬，让我们以其名字来称呼这类集合。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> Cantor 三分集的出生地，并非人们以为的抽象集合论练习，而是实分析的硬核问题——trigonometric series（三角级数）表示的唯一性：一个函数若可展成三角级数 $\sum_{n\ge0}(a_n\cos nx+b_n\sin nx)$，表示是否唯一？这个问题是 Heine 建议 Cantor 去做的。等价地问：若一个三角级数在每点收敛到 $0$，是否所有系数 $a_n,b_n$ 必为零？若成立，两个级数表示同一函数时逐项相减即得唯一性。
>
> 机制的难点在第一性原理上很清楚：三角级数是无限项求和，pointwise convergence（点态收敛）不像有限和那样可以逐项比对系数。有限个三角函数的线性组合为零，由线性无关性立即推出系数全零；无限级数的点态极限却可能吞掉信息。这套论证的武器是把级数形式地积分两次，得到连续函数 $F$：若级数处处收敛到 $0$，$F$ 的 generalized second derivative（广义二阶导数）为零，$F$ 必为线性函数，反推系数全零。Cantor 1870 年据此证明级数处处收敛到零则系数全为零。经典例子 $\sum_{n=1}^{\infty}\frac{\sin nx}{n}$ 在 $(0,2\pi)$ 上等于 $\frac{\pi-x}{2}$，说明非平凡表示确实存在，唯一性问题并非空转。
>
> 1872 年他再大刀阔斧地推广：至多在一个可数紧集上例外（即级数允许在一个可数紧集上不收敛到零），唯一性依然成立。正是这一步迫使他刻画可数集、limit point（聚点）、聚点的聚点——即 derived set（导出集）$E',E'',\ldots$ 的迭代。这里的证明策略可以命名复用：derived-set peeling（导出集剥皮法）——对例外集 $E$ 逐层取导出集，$E'$ 是 $E$ 的聚点集，$E''$ 是聚点的聚点集，每剥一层就删掉一层孤立的极限信息；只要某层剥空，例外集就薄到无害，唯一性随之成立。这套薄度分层后来也成为 transfinite ordinal（超限序数，即在有限层之外还能继续计数的序型）概念的出发点之一。最终在 1883 年关于无限线性点流形的长篇回忆录第五部分写成三分集构造，当时他称之为 perfect nowhere dense set（完备的无处稠密集）。
>
> 需要诚实标注的是：H. J. S. Smith 早在 1875 年就已印出过类似的挖孔构造——一个不可数却任意小 outer content（外包容量，测度的前身）的集合的先例，只是因无人重视而被长期埋没。同年（1883 年）11 月 Cantor 又在信中定义了 Cantor function（Cantor 函数）——在挖掉区间上取常值的连续增函数：在 $(\frac13,\frac23)$ 上取 $\frac12$，在 $(\frac19,\frac29)$ 上取 $\frac14$，在 $(\frac79,\frac89)$ 上取 $\frac34$，逐层如此。它后来成为 almost everywhere（几乎处处）可导却与原函数无关一类反例的源头：$F$ 连续递增，在挖掉区间的并（测度为 $1$）上导数为零，于是 $F'=0$ 几乎处处，但 $F(1)-F(0)=1\ne\int_0^1 F'=0$——微积分基本定理在"仅几乎处处可导"下失效，根源是 $F$ 不是 absolutely continuous（绝对连续）函数，其变化无法由导数积分回收。
>
> 这段数学史提醒我们：最深奥的抽象集合，往往诞生于最具体的逼近问题。跨课程的呼应也精确：6.042J 里当作分类工具的可数性，在这里变成唯一性定理的薄度阈值——例外集从处处收敛放宽到至多可数例外依然成立；区别在于 6.042J 只问集合能否与 $\mathbb{N}$ 一一对应，实分析要问数不完的例外集是否还薄到不破坏唯一性。Strang 的线性代数把唯一性建立在 null space（零空间）平凡上：$Ax=0$ 只有零解；这里同样在证"零空间"平凡——收敛到零的三角级数必为零级数。区别在于 $\mathbb{R}^n$ 里线性无关靠有限消元检验，而三角系 $\{1,\cos nx,\sin nx\}$ 是无限维正交系，点态收敛不是有限线性代数概念，于是唯一性从习题变成深刻定理。

<span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">**Definition 13.120**：一个非空、无处稠密、紧致（compact）且无孤立点的实数集合，被称为 Cantor 集（Cantor set）。</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 定义 13.120 用一个对象同时打包了四个看似互斥的要求：nonempty（非空）、nowhere dense（无处稠密）、compact（紧致）、no isolated point（无孤立点）。先拆解每个词的独立含义。无处稠密：任意开区间内都能挖出一个不含集合点的更小区间，即集合不占据任何处所的长度；等价地说，集合的闭包没有内点。无孤立点：每个点都是集合内别的点的极限，没有孤魂野点；形式化地说，对每个 $x$ 与每个 $\varepsilon>0$，$(x-\varepsilon,x+\varepsilon)$ 里都有集合中异于 $x$ 的点。紧致：在 $[0,1]$ 里就是闭有界子集（Heine–Borel theorem，海涅–博雷尔定理），序列取极限逃不出去，紧守疆域不逸出。非空则排除空集这个退化情形——空集无处稠密、紧致、无孤立点都平凡成立，若不加非空，整个定义就白打包了。
>
> 直觉上，无处稠密应当意味着集合很小，而无孤立点仿佛要求点连成片，二者似乎互斥。第一性原理式的提问是：矛盾究竟在哪一环被化解？答案是长度与极限是两把不同的尺子：无处稠密封锁的仅是占据长度的可能——任何开区间都要被挖出空隙；无孤立点要求的只是处处为自身极限点——每点周围都要有同集合的邻居，至于这些邻居是否隔着被挖空的中途区间，毫不相干。
>
> 具体到 Cantor 集，$0\in C$ 是极限点的活标本：点列 $\frac{2}{3^n}\to0$ 的每一项都在 $C$ 中（三进制只含 $0$ 与 $2$），所以 $0$ 不是孤魂野点。非端点也如此：$\frac14=0.\overline{02}_3\in C$，截断列 $0.02_3,0.0202_3,0.020202_3,\ldots$ 全在 $C$ 中且趋于 $\frac14$。更一般地，把任意 $x\in C$ 的三进制展开第 $n$ 位在 $0$ 与 $2$ 之间翻转，就得到一列 $C$ 中的点趋于 $x$。同时，被挖掉的开区间全体在 $[0,1]$ 中稠密，任何开区间里都能找到一段挖掉的区间，它不含 $C$ 的点——这正是无处稠密的机制：洞稠密地布满全区间，封死了 $C$ 包含任何开区间的可能。两件事并行不悖：洞稠密（封死长度），点也稠密于自身（每个点都有邻居）。
>
> 于是 Cantor 集既能像尘埃般稀疏，又能似链条般连而不封。这里"连而不封"要小心：它不是 connected（连通）的——$C$ 完全不连通，任何两点之间都有洞隔开；它是 perfect（完备）的——闭集且无孤立点。还要防一个术语陷阱：完备集的 perfect 与 complete metric space（完备度量空间）的 complete 是两个词，前者说"每个点都是聚点"，后者说 Cauchy sequence（柯西列）都收敛。紧致加无孤立点恰好给出 perfect：紧致提供闭性，无孤立点提供聚点性，两者合起来就是"闭且无孤立点"。
>
> 跨课程的呼应非常精确。6.042J 的 diagonal argument（对角线论证）：把 $C$ 中点的三进制数字串 $\{0,2\}$ 映成二进制数字串 $\{0,1\}$，得到与全体二进制序列的一一对应，故 $C$ 不可数——区别在于，6.042J 用它证 $[0,1]$ 不可数，这里同一个编码证明连这个测度为零的"尘埃"都不可数，可见基数尺完全不理会拓扑与测度。CSAPP 的 bit pattern（位模式）编码：$C$ 的点就是无限长的三进制位串，挖洞规则就是"禁字符过滤"——含 $1$ 的串全部删掉；区别在于 CSAPP 的有限位模式制造舍入间隙，而 Cantor 的无限位串制造拓扑空洞。Strang 的矩阵迭代与 spectral radius（谱半径）：三分集满足自相似方程 $C=\frac13 C\cup(\frac23+\frac13 C)$，两个压缩映射 $x\mapsto x/3$ 与 $x\mapsto x/3+2/3$ 构成一个 iterated function system（迭代函数系，一组压缩映射的联合迭代），其 Lipschitz constant（利普希茨常数，即拉伸比）都是 $\frac13<1$；由 contraction mapping theorem（压缩映射定理），$C$ 是唯一的 fixed point（不动点）吸引子。区别在于 Strang 里 Jacobi 迭代的收敛条件是 $\rho(M)<1$（$\rho(M)$ 是迭代矩阵特征值模的最大值）且作用对象是向量，这里 $\frac13<1$ 作用于区间的两个仿射压缩，但"系数小于 $1$ 的迭代必有唯一不动点"是同一根主线。
>
> 这个并存使 Cantor 集在过去一百多年里既是反直觉的考题，又是屡试不爽的反例试金石。可复用的命名模板是 length–limit dual-ruler separation（长度尺与极限尺分离法）：凡遇到"既小又密"的结构，先把"占据长度的能力"与"成为极限点的能力"拆到两把尺子上分别检验，再合起来下结论；这四件套打包，正是这把双尺的完整封装。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> Cantor 三分集最透彻的理解，不在几何上反复挖空的动作，而在一句ternary（三进制）刻画：$[0,1]$ 中恰能写成三进制展开、且展开里不出现数字 $1$ 的那些数，全体正是 Cantor 集。要看清这一点，只需把构造逐位翻译。第一步删除开区间 $(1/3,2/3)$，而一个数落在该开区间内，当且仅当其每个三进制展开的第一位都是 $1$：$0.1d_2d_3\ldots$ 的取值范围正是闭区间 $[1/3,2/3]$，两个端点由替身写法排除。第二步在每个剩余闭区间 $[0,1/3]$、$[2/3,1]$ 里再删中段，这恰好筛掉那些第一位是 $0$ 或 $2$、第二位是 $1$ 的数。归纳下去，第 $k$ 步删除的中间三分之一，正是三进制第 $k$ 位取 $1$ 的cylinder set（柱集，指前若干位固定、其余位任意的数构成的区间）。于是挖洞与筛数成为同一件事：幸存者恰好是三进制每一位都属于 $\{0,2\}$ 的数。可以把这套思路命名为“按位过滤法”：构造删除什么，等价于在数字展开的每一位上设卡，把含某个禁用符号的对象全部淘汰。
>
> 这条刻画最震撼之处在于它与可数性（6.042J 的对角线论证）直接接轨。把数字 $2$ 映成 $1$（即对每个三元位执行 $c_k\mapsto c_k/2$），Cantor 集的元素就与二值无限序列全体 $\{0,1\}^{\mathbb{N}}$ 一一对应；后者与二进制小数全体一样多，正是对角线论证证明不可数的对象：假设存在序列 $x_1,x_2,\ldots$ 枚举全部二值序列，沿对角线取反构造 $y$，$y$ 在第 $n$ 位与 $x_n$ 不同，故 $y$ 不在表内。因此 Cantor 集是（严格）不可数的。这里有一个关键小细节：三进制有理端点拥有两种展开，例如 $1/3=0.1=0.0222\ldots$。若机械地取第一种展开，$1/3$ 会被误判为含 $1$；好在它以 $2$ 收尾的替身写法存在，端点处“不含 $1$”的结论依然成立。一般地，形如 $k/3^n$ 的三进制有理数至多有一个展开不含 $1$：有限终止于全 $0$ 尾与以全 $2$ 尾收场二者必居其一。因此每个 Cantor 点对应唯一一条 $\{0,2\}$ 序列，上述映射是well-defined（良定义的）。
>
> 一个常被忽略的具体例子是 $1/4$。它的三进制展开是 $0.020202\ldots=(0.\overline{02})_3$，数字 $0$ 与 $2$ 交替出现，永不出现 $1$，所以 $1/4$ 属于 Cantor 集。更妙的是 $1/4$ 不是任何被挖区间的端点：端点对应有限终止或全 $2$ 尾的展开，而 $1/4$ 的展开无限交替，因而它每一步都落在剩余闭区间的内部附近，永远不被删除却也不是边界。这说明 Cantor 集远不止可数个挖洞端点，还装着不可数个像 $1/4$ 这样的内部幸存者——这与 6.042J 里“有理数可数但实数不可数”的结构呼应：可数族删除过程留下的边界只是骨架，真正填满集合的是不可数的展开。
>
> 于是我们看到一个惊人并存：一个nowhere dense（无处稠密）、瘦到没有长度的集合，却装着与整条实轴一样多的点。长度为零来自几何级数：被删总长度为 $\frac13+2\cdot\frac19+4\cdot\frac1{27}+\cdots=\frac13\sum_{k\ge0}(\frac23)^k=1$，这正是 6.042J 学过的几何级数求和。无处稠密则因为任意非空开区间都包含某个被删的中段，故 $C$ 不含任何区间，又因 $C$ 是闭集，闭包即自身，内部为空。可与 Strang 的矩阵迭代作一精确对照：三分构造可写成集合迭代 $F(S)=\frac13 S\cup(\frac13 S+\frac23)$，从 $S_0=[0,1]$ 出发得 $S_{k+1}=F(S_k)$，$C=\bigcap_k S_k$ 是唯一不动点。对任意两个闭集 $A,B$，$F$ 的 Hausdorff 距离满足 $d_H(F(A),F(B))=\frac13 d_H(A,B)$，压缩系数 $\frac13<1$；这恰是 Strang 中矩阵迭代 $x_{k+1}=Mx_k+b$ 收敛条件的非线性版本：那里要求spectral radius（谱半径）$\rho(M)<1$，这里要求 Lipschitz 常数小于 $1$。区别在于前者的不变对象是有限维空间里的单个向量，后者是闭子集空间里的整体分形形状。

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 先把概念定义摆齐：Cantor 集指非空、无处稠密、紧致、无孤立点的 $[0,1]$ 闭子集。逐个拆开：非空即至少有一个点；无处稠密指闭包的内部为空，直观上“不填满任何一小段”；紧致在 $[0,1]$ 的闭子集情形自动等价于闭且有界；无孤立点指集合的每一点都能被集合中其他点任意逼近，点与点之间没有断层。配上本节最惊艳的结论：在所有闭子集构成的空间 $\mathcal{K}$（以 Hausdorff metric 为距离，中文称 Hausdorff 度量）里，大多数闭集竟都是 Cantor 集（定理 13.121）。所谓“大多数”，精确含义是 Baire 纲意义下的典型：坏集合的并只占第一纲，好集合的补集是剩余集。这是对 19 世纪数学家认知的一次彻底翻案——当初 Cantor 三分集（约 1883 年构造）被当作病态怪物，如今在纲的意义下，Cantor 集恰是 $[0,1]$ 之闭子集的典型长相，怪物反而是常态。
>
> 证明的分量在于把两个逐点担心分别翻译成可数个无处稠密集。担心一：闭集含有内点，即包含某个非退化闭区间。用端点取有理数的区间族 $\{I_k\}$ 枚举全部闭区间——有理端点保证只有可数个，这是 6.042J 可数性提供的记账工具：$\mathbb{Q}$ 可数，故 $\mathbb{Q}\times\mathbb{Q}$ 可数——令 $A_k=\{K\in\mathcal{K}:K\supset I_k\}$。担心二：闭集有孤立点，即某点 $x\in K$ 落在 $K$ 中但附近没有 $K$ 的其他点；按有理半径的球条件把孤立点情形拆成 $B=\bigcup_n B_n$。若每个 $A_k$、$B_n$ 无处稠密，则 $A=\bigcup_k A_k$ 与 $B$ 都是first category（第一纲，即可数个无处稠密集的并），由 (47)、(48) 两式其并集仍是第一纲；于是补集是剩余集，其中的闭集同时无处稠密且无孤立点。
>
> 这里要与 6.042J 的可数性作一次精确区分：第一纲是拓扑意义上的“小”，与基数意义上的“少”是两把尺子。可数集在无孤立点的完备度量空间里必是第一纲，但反过来不对：Cantor 集本身无处稠密，在 $[0,1]$ 中属第一纲，却不可数。所以“典型”不等于“概率一”，也不等于“测度一”。一个具体提醒来自fat Cantor set（胖 Cantor 集）：若删中段时改用越来越小的比例，使删除总长严格小于 $1$，得到的集合仍是拓扑意义上的 Cantor 集（非空、无处稠密、紧致、无孤立点），却有正长度。这说明定理 13.121 说典型闭集是 Cantor 集，并不承诺它们测度为零，测度与纲再次分道扬镳。
>
> Hausdorff 度量是翻案的技术支点：它用 $\varepsilon$-邻域的双向包含定义两个闭集的距离 $d_H(A,B)=\inf\{\varepsilon>0:A\subseteq B^{(\varepsilon)}\ \text{and}\ B\subseteq A^{(\varepsilon)}\}$，让“两个集合整体上有多像”成为可计算、可比较的实数。一个具体例子：$A=\{0\}$，$B=\{\varepsilon\}$，则 $d_H(A,B)=\varepsilon$；而 $A=[0,1]$，$B=[0,1+\varepsilon]$ 的距离也是 $\varepsilon$。这可比拟 CSAPP 中把对象当作整体来比较度量的思想：比较两个 IEEE 754 浮点数的位模式时，我们不是逐位叙述每个比特的来历，而是把整个 32 位或 64 位字看成一个对象；Hausdorff 度量同样不逐点比较，而是问“把 $A$ 加厚 $\varepsilon$ 能否盖住 $B$，且把 $B$ 加厚 $\varepsilon$ 能否盖住 $A$”。区别在于：CSAPP 的位模式是有限长、可精确相等的对象，而闭集是无限对象，Hausdorff 距离是上下确界构造出的实数，两个不同闭集的距离可以严格为正但不等于任意点的距离。
>
> 对尚未学拓扑的你，这一小节是绝佳跳板：它示范把集合本身当成度量空间的点来研究——点的“坐标”不再是数，而是整个集合。这正是日后泛函分析与hyperspace theory（超空间理论）的入口，也是本章压缩映射定理的自然延伸：先把完备性从数轴搬到 $\mathcal{K}$，Baire 纲定理才能在“闭集空间”里开工。

> <span style="color:#7f8c8d;">TBB §13.14, p.625</span>

假设我们像十九世纪数学家那样，尚未听说过 Cantor 集，但与十九世纪数学家不同的是，我们已经知道了 Baire 纲定理，并且知道了 $[0,1]$ 的闭子集全体配上 Hausdorff 度量 $d$ 所构成的空间 $K$ 是完备的（习题 13.8.13 与 13.3.9）。

我们不妨问一句："$[0,1]$ 的大多数非空闭子集看起来是什么样子的呢？"

<span style="color:#2471a3;">**[question]**</span> **问题 1**：$[0,1]$ 的大多数非空闭子集是否包含内点（interior points）？

若一个闭集含有内点，则存在一个端点取有理数的闭区间 $I$ 含于该集合之中。

于是，每个确实含有内点的闭集，对某个这样的区间 $I$，都属于族
```math
\{K\in K : K\supset I\}.
```

任取 $F\in K$，并令 $\varepsilon>0$。

由习题 13.7.3（及其提示）可知，存在一个有理数的有限集 $S$，使得 $d(S,F)<\varepsilon$。

我们可以选择 $S$，使得 $S\cap I$ 至少含有两个成员。

设 $S=\{s_1,\ldots,s_n\}$，其中 $s_1$ 与 $s_2$ 都在 $I$ 中，且 $s_1$ 与 $s_2$ 之间没有 $S$ 的其他点。

令 $\delta$ 小于 $|s_1-s_2|/3$，并且足够小以使得
```math
B(S,\delta)\subset B(F,\varepsilon).
```

若 $T\in B(S,\delta)$，那么 $T$ 不能含有点 $m=(s_1+s_2)/2$（图 13.11）。

<span style="color:#2471a3;">**[figure]**</span> 图 **Figure 13.11**：在证明 $K$ 中"大多数"成员无处稠密时的区间 $I$。

图中标注了 $s_1$、$s_1+\delta$、$s_1-\delta$、$s_2$ 等刻度，其中点 $m$ 位于 $s_1$ 与 $s_2$ 的中点，这一几何背景将用于证明球 $B(S,\delta)$ 中的任一元都不能包含区间 $I$。

从而 $T$ 不能含有 $I$。

于是球 $B(F,\varepsilon)$ 含有球 $B(S,\delta)$，而 $B(S,\delta)$ 中没有任何一点落在集合 $\{K\in K : K\supset I\}$ 之中。

<span style="color:#7f8c8d">书页 626 — Metric Spaces，Chapter 13（§13.14.4 续）</span>

由此可知，对区间 $I$ 的任何选择，后一集合在 $K$ 中都是无处稠密的。

现在令 $\{I_k\}$ 为 $[0,1]$ 的端点取有理数的闭子区间的一个枚举。

对每个 $k\in\mathbb{N}$，令
```math
A_k=\{K\in K : K\supset I_k\}.
```

我们已经说明每一个集合 $A_k$ 在 $K$ 中都是无处稠密的，因此
```math
A=\bigcup_{k=1}^{\infty}A_k
```
是一个第一纲（first category）集合。

这表明集合 $\{K\in K : K \text{ 含有非空内部}\}$ 是第一纲的。

于是我们已回答了第一个问题，并可以断言：

> $K$ 中的大多数成员都是无处稠密的。（47）

接下来我们探讨孤立点。

<span style="color:#2471a3;">**[question]**</span> **问题 2**：$K$ 中的大多数成员是否有孤立点（isolated points）？

若 $K\in K$ 有一个孤立点 $x$，则存在 $n\in\mathbb{N}$ 使得
```math
\operatorname{dist}(x,K\setminus\{x\})\ge 1/n.
```
（函数"dist"的定义参见习题 13.6.11。）

令
```math
B_n=\{K\in K : \exists\, x\in K\ \text{使得}\ \operatorname{dist}(x,K\setminus\{x\})\ge 1/n\}.
```

我们容易验证（习题 13.14.3）每一个集合 $B_n$ 在 $K$ 中都是无处稠密的。

令 $B=\bigcup_{n=1}^{\infty}B_n$，则 $B$ 在 $K$ 中是第一纲的。

若 $K$ 有任何孤立点，则 $K\in B$。

于是我们已回答了第二个问题，并可以断言：

> $K$ 中的大多数成员都没有孤立点。（48）

把（47）与（48）结合起来，我们看到我们已证明了如下定理。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">**Theorem 13.121**：设 $K$ 为 $[0,1]$ 的非空闭子集配上 Hausdorff 度量所成的度量空间，并设 $S$ 由 $[0,1]$ 中的 Cantor 集组成，则 $S$ 在 $K$ 中是剩余集（residual）。</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 定理 13.121 的证明是一台教科书级的 Baire 纲机器，值得提炼成可反复套用的三步骤模板，给它起名为“坏对象可数并 + 逐项无处稠密 + Baire 收口”。第一步，把坏集合（不满足目标性质的对象）写成可数并 $\bigcup_k A_k$。坏对象是含有内点的闭集：只要 $K$ 有内点，就包含某个端点取有理数的闭区间，于是用可数族 $\{I_k\}$ 枚举全部这种区间，得到 $A_k=\{K\in\mathcal{K}:K\supset I_k\}$。用有理端点是为了把不可数的连续选择压成可数枚举，这正是 6.042J 可数性的记账功能：$\mathbb{Q}$ 可数保证区间族可数，否则后续“并集仍是第一纲”的句法根本不合法——Baire 纲定理只接受可数并。孤立点情形则化作 $B=\bigcup_n B_n$，把“存在孤立点”这一存在量词拆成可数个带参数的有理球判定条件。这一步的直觉模板是“坏性质 = 存在一个可数测试证伪”：只要坏对象能被某个可数族成员作证，坏集合就被这个可数并一网打尽。
>
> 第二步，逐个证明 $A_k$、$B_n$ 在 $\mathcal{K}$ 中无处稠密。固定一个 $A_k$，任取非空开球 $B(F,\varepsilon)$（以闭集 $F$ 为心、$\varepsilon$ 为半径的 Hausdorff 球）。先用有限有理点集 $S$ 逼近 $F$（习题 13.7.3 保证有限集在 $\mathcal{K}$ 中稠密，正如 $\mathbb{Q}$ 在 $\mathbb{R}$ 中稠密），使 $d_H(S,F)$ 足够小。再构造一个不含任何 $A_k$ 元素的更小球 $B(S,\delta)$：让 $S$ 在目标区间 $I_k$ 内部留出一个洞，取相邻点中点（图 13.11 的技巧），这个动作可命名为“中点戳洞法”。洞的中点距 $S$ 的距离等于洞长的一半，取 $\delta$ 小于这个距离，则任何与 $S$ 的 Hausdorff 距离小于 $\delta$ 的闭集 $K$ 必整体落在 $S$ 的 $\delta$-邻域内，从而 $K$ 不含那个中点，更不可能包含整个 $I_k$。于是 $B(S,\delta)\cap A_k=\varnothing$，$A_k$ 在每个开球里都不稠密，闭包无内点，即无处稠密。这里的机制是：用有限网格去近似无限对象，误差由 $\delta$ 控制，正如 CSAPP 里浮点数网格逼近实数、舍入误差由 ULP（unit in the last place，末位单位）控制——区别是浮点网格固定，而这里网格 $S$ 按证明需要自适应加细。
>
> 用一个具体数值例子走一遍这套动作。取六等分网格 $F=\{0,\frac16,\frac13,\frac12,\frac23,\frac56,1\}$，半径 $\varepsilon=\frac14$，目标坏族取 $I_k=[\frac13,\frac23]$。令 $S=F\setminus\{\frac12\}$，则 $d_H(S,F)=\frac16<\frac14$，由三角不等式 $d_H(K,F)\le d_H(K,S)+d_H(S,F)$，对足够小的 $\delta$ 有 $B(S,\delta)\subseteq B(F,\varepsilon)$。$S$ 在 $[\frac13,\frac23]$ 内留下以 $\frac12$ 为中点、长 $\frac13$ 的洞，取 $\delta=\frac1{12}$，则 $\frac12$ 到 $S$ 的距离为 $\frac16>\delta$，任何 $K\in B(S,\delta)$ 都不含 $\frac12$，自然不含 $[\frac13,\frac23]$。于是开球 $B(F,\frac14)$ 里被戳出一个与 $A_k$ 不交的子球 $B(S,\frac1{12})$。这就是无处稠密的操作化定义：每个开球里都能再戳一个避开坏族的洞。
>
> 第三步，调用 Baire 纲定理收口：$\mathcal{K}$ 完备（习题 13.8.13/13.3.9），完备度量空间不能表成自身中可数个无处稠密集的并，故 $A=\bigcup_k A_k$ 与 $B=\bigcup_n B_n$ 的并仍是第一纲，其补集是residual（剩余集）。剩余集非空且稠密，所以“大多数闭集”有了严格含义。注意完备性是整台机器的燃料，这与 Strang 里 Jacobi 迭代需spectral radius（谱半径）小于 $1$ 才能收敛到唯一不动点异曲同工：压缩映射定理与 Baire 定理都要求空间完备，区别在于前者产出唯一不动点，后者产出稠密的剩余集。这一步与 CLRS 的loop invariant（循环不变量）思维也能对上：枚举坏集族对应“初始化”，逐项证无处稠密对应“保持”，Baire 定理收口对应“终止”时整体性质成立——机器每前进一步都维护一个可数并结构，最后一次性兑换成纲的结论。
>
> 这套坏对象 = 可数并 + 逐项无处稠密的论证，正是前几页证明大多数函数在某点不可微、大多数函数无处单调的同一台机器：把函数空间里的坏性质同样拆成可数并，再逐项戳洞。今后凡见“大多数成员具有性质 P”的题（如 13.14.4、13.14.5），照此三步执行即可：先写坏集合并，再逐项戳洞，最后 Baire 收口。

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> Cantor 集是 fractal geometry（分形几何）的原型，而它的维数恰好可以只靠读者手头的一维直觉一步步推出来。先回忆构造：$C_0=[0,1]$，每步把每个小区间挖掉中间三分之一，第 $k$ 步剩下 $2^k$ 个小区间，每个长度为 $3^{-k}$。这里已藏着 self-similarity（自相似性）：整体 $C$ 等于它自己的左三分之一拷贝 $\frac{1}{3}C$ 与右三分之一拷贝 $\frac{1}{3}C+\frac{2}{3}$ 之并，即 $C=\frac{1}{3}C\cup(\frac{1}{3}C+\frac{2}{3})$。补一句史实：据本机知识库检索结果，该集由 Henry John Stephen Smith 于 1874 年先发现，Cantor 于 1883 年在《Über unendliche, lineare Punktmannigfaltigkeiten V》（Math. Ann. 21:545–591）中提及；Cantor 本人是被 trigonometric series（三角级数）唯一性问题（uniqueness of trigonometric series）引导到点集与导集研究的。
>
> 下面做量级实验。若某集合的维数是 $s$，它的 $s$ 维总大小应当近似按 $2^k\cdot(3^{-k})^s=(2/3^s)^k$ 变化。第一性原理是：维数 $s$ 的定义就是“缩放因子 $\lambda$ 使 $s$ 维测度乘 $\lambda^s$”——长度乘 $\lambda$、面积乘 $\lambda^2$、体积乘 $\lambda^3$，非整数 $s$ 正是这串指数在中间插值出来的。当 $s=0$（数点）时，$2^k\to\infty$，因为 $C$ 里有不可数（cardinality of the continuum，连续统基数）那么多点；当 $s=1$（长度）时，$(2/3)^k\to 0$，这正是 Lebesgue measure（勒贝格测度）为零的机制：总长度每步乘 $2/3$。给个具体数：$k=10$ 时有 $2^{10}=1024$ 段，每段长 $3^{-10}=1/59049$，总长约 $0.0173$；到 $k=20$ 总长只剩 $(2/3)^{20}\approx 0.0003$，塌向零肉眼可见。
>
> 于是要这个量级既不发散也不塌缩，必须 $2/3^s=1$，解得 $s=\log 2/\log 3\approx 0.6309$。可顺手验证临界性：$s=0.5$ 时 $2/\sqrt{3}\approx 1.155>1$，量级按 $1.155^k$ 发散；$s=0.7$ 时 $2/3^{0.7}\approx 0.927<1$，量级按 $0.927^k$ 塌缩；只有 $s=0.6309$ 恰好收支平衡。这个介于 $0$ 与 $1$ 之间的数就是 Cantor 集的 Hausdorff dimension（豪斯多夫维数；Hausdorff 正是本章 Hausdorff 度量那位）。我把这套算法命名为“临界指数判据”（不塌不散原则）：写出覆盖函数 $N_k\ell_k^{s}$，要求它上下有界，解出的 $s$ 就是自相似维数。模板可复用：一般挖掉中间比例 $\alpha$ 的 Cantor 集留下两段，每段长 $(1-\alpha)/2$，维数方程是 $2\cdot((1-\alpha)/2)^s=1$；代回 $\alpha=1/3$ 即得 $s=\log 2/\log 3$。
>
> 要点是区分两种维数。topological dimension（拓扑维数，在同胚下不变）看连通结构：$C$ 是 totally disconnected（全不连通）的，任意两点之间都被挖掉的洞隔开，每个点都有任意小的既开又闭邻域，故拓扑维数为 $0$；几何维数却是非整数 $0.6309$，因为它度量的是缩放时质量如何变化，依赖距离本身——Hausdorff 维数在双向 Lipschitz 变换（两个方向的距离伸缩都有界）下不变，在同胚下却未必不变。所以维数并非单一的拓扑量，而随你度量物体的方式不同而不同。
>
> 跨课程连接把它钉得更牢。6.042J 的 cardinality（基数）与测度在这里并置：$C$ 的每个点对应一个只含数字 $0,2$ 的三进制展开，与二进制序列集 $\{0,1\}^{\mathbb{N}}$ 一一对应，故按 6.042J 的 diagonal argument（对角线论证）它是不可数的；同时它 Lebesgue 测度为零——基数说“点多”，测度说“没长度”，两把尺子不矛盾。CSAPP 的回响在递归：构造 Cantor 集就像 C 语言递归函数 cantor(x, len, depth)，深度为零画一段，否则对左右三分之一各自递归，自相似结构就是递归树；区别是 CSAPP 关心栈帧与机器码，这里递归定义的是极限对象与集合间 Hausdorff 度量。Strang 的回响在迭代：两个映射 $T_1(x)=x/3$、$T_2(x)=x/3+2/3$ 都是压缩比为 $1/3$ 的 contraction mapping（压缩映射），正如矩阵幂 $A^k\to 0$ 当且仅当 spectral radius（谱半径，特征值绝对值的最大值）小于 $1$；$C$ 正是集合映射 $T(A)=T_1(A)\cup T_2(A)$ 在紧集空间的 Hausdorff 度量下的唯一不动点，而方程 $2\cdot 3^{-s}=1$ 就是“拷贝数乘缩放比的 $s$ 次幂等于 $1$”的收支平衡。这个按步覆盖、求不塌不散的比例的算法，往后正是动力系统与泛函分析里维数与压缩迭代（呼应 13.9 节压缩映射）的前奏。

---

> <span style="color:#7f8c8d;">TBB §13.14, p.626</span>

现在，对十九世纪的数学家（以及对初等微积分的学生）来说，$[0,1]$ 中的闭集相当简单。

它们由区间、孤立点及孤立点的极限所组成。

再多花些力气，或许还能想象出含有限点的极限、或极限点的极限点的集合（习题 4.2.24）。

我们的定理说明：事实上，当"大多数"按"纲"（category）的意义来理解时，大多数闭集都是 Cantor 集。

<span style="color:#7f8c8d">*（本页其余部分为 §13.14 Exercises 习题区（13.14.3），按约定跳过。）*</span>


<!-- ===== W22 ===== -->

<span style="color:#7f8c8d">书页 627 — Section 13.15（第 13 章挑战性习题区）</span>

<span style="color:#2471a3;">**[section]**</span> **§13.15 第 13 章挑战性习题（Challenging Problems for Chapter 13）**

本页顶部为 **§13.14 习题区**的收尾，其下为 **§13.15 挑战性习题**。两道 §13.14 习题的内容如下（均为习题区，按约定跳过）：

> <span style="color:#7f8c8d">13.14.4　证明集合 $Y=\{\,f\in M[a,b]\,:\,f$ 是一对一的 $\}$ 是有界函数空间 $M[a,b]$ 的一个剩余子集（residual subset）。[参见 Note 376。]</span>

> <span style="color:#7f8c8d">13.14.5　证明集合 $Z=\{\,f\in M[a,b]\,:\,f$ 的值域（range）无处稠密（nowhere dense） $\}$ 是有界函数空间 $M[a,b]$ 的一个剩余子集。</span>

<span style="color:#7f8c8d">*（书页 627 上引部分为 §13.14 习题区余留，按约定跳过。）*</span>

> <span style="color:#7f8c8d">**§13.15 挑战性习题（Challenging Problems for Chapter 13）**——本页为 §13.15 挑战性习题区，含习题 13.15.1–13.15.12，按约定跳过，不翻译、不收录。</span>

<span style="color:#7f8c8d">*（本页全部为 §13.15 挑战性习题 13.15.1–13.15.12，按约定跳过，不翻译、不收录。）*</span>


<!-- ===== W23 ===== -->

<span style="color:#7f8c8d">书页 629 · §13.15 Challenging Problems for Chapter 13（第 13 章难题）</span>

<span style="color:#7f8c8d">本节 §13.15 为第 13 章的整组选作难题（Challenging Problems），全部内容均属习题区 Exercises，按约定跳过、不逐句翻译，仅作灰色结构标注如下。</span>

<span style="color:#7f8c8d">*（本页为 §13.15 习题区，习题编号 13.15.12(g)–13.15.16，按约定跳过。）*</span>

<span style="color:#7f8c8d">题 13.15.12(g)：在 $(X,d)$ 中验证 Baire 纲定理（Baire category theorem）即使空间不完备也成立（提示见 Note 385）。</span>

<span style="color:#7f8c8d">题 13.15.13：引续习题 13.15.12 的 $(X,d)$（并非完备），该题已表明此空间可重新度量（remetrized）为完备的 $(X,e)$。这意味着 $d$ 与 $e$ 是等价度量（equivalent metrics），$(X,d)$ 与 $(X,e)$ 是拓扑等价（即同胚 homeomorphic）的度量空间。此类空间称为拓扑完备（topologically complete）。本小题要求：(a) 验证 Baire 纲定理在每个拓扑完备的度量空间中都成立；(b) 给出一个非拓扑完备的度量空间的例子。</span>

<span style="color:#7f8c8d">题 13.15.14（Urysohn 引理 Urysohn's Lemma）：证明如下的定理，它归功于 Pavel Urysohn（1898–1924）：设 $A,B$ 是度量空间 $(X,d)$ 中互不相交（disjoint）的非空闭子集，则存在连续函数 $g:X\to\mathbb{R}$，满足对所有 $x\in A$ 有 $g(x)=0$，对所有 $x\in B$ 有 $g(x)=1$，并对所有 $x\in X\setminus(A\cup B)$ 有 $0\lt g(x)<1$（提示见 Note 386）。</span>

<span style="color:#7f8c8d">题 13.15.15：本题需要一些关于复数和超越数（transcendental numbers）的知识。要在 $\mathbb{R}^2$ 中构造两个集合 $R$ 与 $T$，使 $R$、$T$ 全等（congruent）且它们各自的并集 $S=R\cup T$ 也与之全等。对每个复数 $z$ 令 $t(z)=z+1$、$r(z)=e^{i}z$，于是 $t$ 是右移 1 单位、$r$ 是旋转 1 弧度。令 $S$ 为从原点出发经有限次应用 $t$、$r$ 所能到达的点，其每个成员可表为 $e^i$ 的多项式且系数为正整数（例如平移五次、旋转两次、再平移一次所得点可表为 $5e^{2i}+1$）。因 $e^i$ 是超越数，该表示唯一。令 $R$ 为表示中不含常数项的点，$T=S\setminus R$。要求证明 $t(S)=T$ 且 $r(S)=R$，从而 $R$、$T$ 与 $S=R\cup T$ 两两等距（isometric）。注意所涉等距是 $\mathbb{R}^2$ 到自身的等距映射，而非仅在 $R,S,T$ 之间。</span>

<span style="color:#7f8c8d">题 13.15.16：设 $(X,d)$ 为度量空间，$M(X)$ 表示 $X$ 上一切有界实值函数配上上确界度量（sup metric）所成的集合。取定 $x_0\in X$，定义映射 $h:X\to M(X)$，令 $h(x)$ 为函数 $(h(x))(y)=d(x,y)-d(y,x_0)$（$y\in X$）。要求：(a) 证明每个 $h(x)$ 都是 $X$ 上的有界函数；(b) 证明 $h$ 是 $X$ 到 $M(X)$ 的某个子空间的一个等距（isometry）；(c) 证明每个度量空间都等距于某个完备函数空间（即定义在某个集上、配上上确界度量的实值函数所成的完备度量空间）的一个子空间。</span>

<span style="color:#7f8c8d">书页 630 · Notes（第 13 章习题提示）</span>

<span style="color:#7f8c8d">本页为第 13 章 NOTES（Notes 提示区），内容是对前面各节习题的提示，按约定跳过、不逐句翻译，仅作灰色结构标注如下。</span>

<span style="color:#7f8c8d">*（本页为 Notes 习题提示区，覆盖题号 288–299，按约定跳过。）*</span>

<span style="color:#7f8c8d">提示 288（题 13.1.2）：向量空间公理在任何初等线性代数课程或教材中都有讲述，此前已在定理 11.1 用它描述 $\mathbb{R}^n$ 的向量空间结构；注意本例中 (d) 是 (b) 的特殊情形，但一般而言标量乘法并非空间中元素乘法的特殊情形（此处标量可视作常值函数）。</span>

<span style="color:#7f8c8d">提示 289（题 13.1.4）：例如可定义 $f\preceq g$，当 $g-f$ 在 $[0,1]$ 上既非负又可微。</span>

<span style="color:#7f8c8d">提示 290（题 13.2.1）：前两个并非度量；(d)、(e) 中的度量较有意思，因它们有界（即对所有 $x,y$ 有 $d(x,y)\le 1$），却仍与通常度量密切相关：在这些度量下开集、闭集、收敛序列等皆相同。验证 (e) 的三角不等式时，先证 $f(t)=t/(1+t)$ 在 $[0,\infty)$ 上递增，再使用 $f(|x-y|)\le f(|x-y|+|y-z|)$；最后注意 (f) 是离散度量（discrete metric）。</span>

<span style="color:#7f8c8d">提示 291（题 13.2.7）：这一想法已用于 $X=\mathbb{R}$ 上的度量 $d(x,y)=|x-y|$，参见题 13.2.1。</span>

<span style="color:#7f8c8d">提示 292（题 13.3.5）：验证度量诸性质除条件 (2) 外全部成立。</span>

<span style="color:#7f8c8d">提示 293（题 13.3.6）：此处虽有子集关系，却无子空间关系，因为三个空间中的度量并不一致。</span>

<span style="color:#7f8c8d">提示 294（题 13.3.7）：本题只需判断所给集合中哪一个属于 $M(\mathbb{R})$ 的子集（这些类中哪一个可能含有无界函数）。</span>

<span style="color:#7f8c8d">提示 295（题 13.4.1）：注意 $d(x_n,x)<1$ 当且仅当 $x_n=x$。</span>

<span style="color:#7f8c8d">提示 296（题 13.4.2）：使用我们在例 13.16 中采用的同样想法与方法。</span>

<span style="color:#7f8c8d">提示 297（题 13.4.3）：记号 $x^{(n)}=(x^{(n)}_1,x^{(n)}_2,x^{(n)}_3,\ldots)$ 起初可能有些费解；此处是空间 $\ell^2$ 中的点序列 $x^{(1)},x^{(2)},x^{(3)},\ldots$，而其中每个点本身又都是实数列。题中仅有一个方向为真：证明该条件必要但不充分，并找使得 $x^{(n)}=(x^{(n)}_1,x^{(n)}_2,x^{(n)}_3,\ldots)$ 逐坐标收敛到零却在度量下不收敛的反例。</span>

<span style="color:#7f8c8d">提示 298（题 13.4.5）：这是错误的。构造一个连续函数序列，使 $d(f_n,0)\to 0$ 但不逐点收敛到零函数。</span>

<span style="color:#7f8c8d">提示 299（题 13.4.6）：(a)、(b) 的证明可相当接近地照抄实数列的相应证明；此处还可利用实数列理论这一便利。例如证 (a) 可直接由不等式 $d(x,y)\le d(x,x_n)+d(y,x_n)$ 推出。进一步推广要小心：一般度量空间没有加法、乘法与序。即便度量空间确有加法等额外结构，仍须对空间上的度量添加某些特殊性质，才能获得诸如 $\lim_{n\to\infty}(x_n+y_n)=\lim_{n\to\infty}x_n+\lim_{n\to\infty}y_n$ 一类的性质。</span>


<!-- ===== W24 ===== -->

<span style="color:#7f8c8d">书页 631 — NOTES（第 13 章习题提示区开始）</span>

<span style="color:#2471a3;">**[section]**</span> **第 13 章 Notes——习题提示（Exercise Hints）**

本页及后续页属于全书的 Notes（提示）区，集中给出第 13 章各节习题的解答提示，供读者在自行完成习题后对照参考。

<span style="color:#7f8c8d">*（本页为 §13.4–§13.6 Exercises 的 NOTES 提示区，按约定跳过。摘自其内容的概要——提示编号 300–315：涉及由 $t/(1+t)$ 的不等式在度量 $d$ 与 $e_2$ 之间推导等价收敛性（Exercise 13.4.9）、复用度量构造（13.4.10）、等价度量下的收敛判据（13.4.12）、多项式序列均匀收敛（13.4.17）、$(0,1)$ 中子空间上的 Cauchy 序列（13.4.18）、反例 $e^x$ 与 $-e^x$（13.5.4）、离散空间（13.5.7）、借助第 9 章定理（13.5.12）、包含聚点 $(0,0,0,\dots)$ 的开球（13.5.15）、Heine-Borel 定理的沿 Bolzano-Weierstrass 式证明（13.5.20）、连续性与常值函数（13.6.1）、沿路径 $f(x,x^2)$ 取序列（13.6.7）、逐点连续的 $\varepsilon$-$\delta$ 表述及其一致版本（13.6.8）、距离函数比式 $dist(x,E)[dist(x,E)+dist(x,F)]^{-1}$（13.6.11）。）*</span>

<span style="color:#7f8c8d">书页 632 — NOTES（习题提示，续）</span>

<span style="color:#7f8c8d">*（本页为 §13.6 Exercises 的 NOTES 提示区，按约定跳过。摘自其内容的概要——提示编号 316–327：先由 (g) 推 (h)，并告诫 $E$、$F$ 不必相距正距离（13.6.11/h）；意大利数学家 Giuseppe Peano（1858–1932）于 1890 年给出填满单位正方形的连续曲线，Hausdorff 1914 年称之为"集合论最卓越结果之一"，并指出一条单射连续曲线不可能填满单位正方形（13.6.12）；可用 Bessel 不等式，F. W. Bessel（1784–1846）（13.6.15）；$R^2$ 中有界闭集与实数闭集有相同紧致性质，可仿 Section 4.5、习题 5.6.12/13 证一致连续（13.6.18）；借助 Example 13.36 的同胚证明 $R$ 与 $(0,1)$ 同胚、$R$ 与 $[0,1]$ 不同胚（13.6.26）；同胚 $h:[0,\infty)\to R$ 必单调（13.6.27）；子空间 $X=\{1,1/2,1/3,1/4,\dots\}$ 拓扑等价于离散空间但 $\inf\{|x-y|\}=0$（13.6.29）；连通集讨论参见 Section 11.10（13.6.37）；借助 13.6.11(d) 构造非平凡连续实值函数（13.6.38）；$R^2$ 子空间中逆命题失效，用集合 $\{(x,\sin(1/x))\mid 0\lt x<1\}\cup\{(0,x)\mid -1\le x\le 1\}$（13.6.40）；映到 $x$ 轴的集合（13.6.41）；函数 $h:K\times K\to K$（13.6.42）。）*</span>

<span style="color:#7f8c8d">书页 633 — NOTES（习题提示，续）</span>

<span style="color:#7f8c8d">*（本页为 §13.6–§13.8 Exercises 的 NOTES 提示区，按约定跳过。摘自其内容的概要——提示编号 328–339：对 $a,b\in K$ 的三进制表示交错置位定义 $h(a,b)=\text{.}\,a_1b_1a_2b_2\dots$（13.6.42）；$b_k=2a_k$（13.6.43）；左/右单侧聚点的对比（13.6.44）；集合 $A=\{2,3,4,\dots\}$ 与 $B=\{0\}\cup\{2,3,4,\dots\}$ 彼此各自等距同构于对方的子集却不等距同构（13.6.47）；$(0,1)\subset X$ 映至直径为 1 的集合（13.6.52）；$[0,1]$ 中有限有理集族构成 $K$ 的可数稠密子集（13.7.3）；多边形函数（polygonal function）逐点用一致连续性逼近并证其可数（13.7.4）；提示：已知的可数稠密子集未必是子空间的子集（13.7.5）；若干空间不可分可作反例（13.7.8）；借助 $C[0,1]$ 的可分性构造嵌入（13.7.11）；由三角不等式直接得（13.8.1）；仿定理 2.11 的证明（13.8.2）；Cauchy 序列蕴含 $\lim d(x_n,x_{n+1})=0$ 而逆命题不真，如 $x_n=\sqrt{n}$（13.8.3）；用三角不等式证 $\{d(x_n,y_n)\}$ 为实数 Cauchy 序列（13.8.4）。）*</span>

<span style="color:#7f8c8d">书页 634 — NOTES（习题提示，续，本卷 PDF 末页/PDF 页 50）</span>

<span style="color:#7f8c8d">*（本页为 §13.8–§13.9 Exercises 的 NOTES 提示区，按约定跳过。摘自其内容的概要——提示编号 340–350（编号 340 在原书概要中无对应记载；书页 633 概要以 339 收尾、本案以 341 起始，故 340 在此补注备查）：对 $\varepsilon_k=2^{-k}$ 取 $n_k$ 使 $d(x_m,x_n)<\varepsilon_k$（13.8.5）；仿定理 2.41 的证明（13.8.6）；一方向检验 $\sum_{k=1}^{\infty}d(x_k,x_{k+1})$ 收敛则序列 Cauchy，另一方向 Cauchy 序列必含某性质子序列（13.8.7）；用闭球序列选取 Cauchy 序列（13.8.8）；$[0,1]$ 中递减非空闭集族 $H_n\to H$（13.8.13）；强调完备性并非拓扑性质，联系 Example 13.36 的 $X=\mathbb{R}$ 与 $Y=(-1,1)$（13.8.16）；应用定理 13.66（13.8.18）；$A$ 非压缩但 $A^2$ 为压缩，不动点易求（13.9.8）；由 $d(A(x),A(y))\le\alpha d(x,y)$ 或 $d(B(x),B(y))\le\alpha d(x,y)$ 推 $d(a,b)<\varepsilon/(1-\alpha)$（13.9.9）；与 13.9.11/13.9.12 对照并使用 $d(a_n,A(a_n)) = d(A_n(a_n),A(a_n))\to 0$（13.9.13）。）*</span>

<span style="color:#7f8c8d">*（以上即为第 13 章全部 Notes 提示内容，本卷随书页 634 结束。）*</span>

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 第 13 章至此收官，把走过的路线串成一张知识地图会更通透。起点是 metric space（度量空间）（13.1–13.4）：把实数轴、$\mathbb{R}^n$ 与函数空间中“距离”的本质抽象为度量公理——nonnegativity（非负性）、symmetry（对称性）、triangle inequality（三角不等式）、$d(x,y)=0$ 当且仅当 $x=y$；有了距离，开/闭集、收敛、Cauchy sequence（柯西序列）、completeness（完备性）逐一登场。三角不等式是灵魂，因为它保证逐段估计能拼接成整体估计，这是所有 $\varepsilon$-论证的骨架。这一步是第 1–2 章实数完备性从数到空间的迁移：$\mathbb{R}$ 上 $|x-y|$ 的性质被提炼成任意集合上的公理。一个反例能钉住完备的实质：$\mathbb{Q}$ 中序列 $x_n=(1+1/n)^n$ 是 Cauchy 序列，极限却是 $e\notin\mathbb{Q}$，可见 $\mathbb{Q}$ 有洞；$\mathbb{R}$ 正是把洞填上之后的完备化。
>
> 接着靠 Heine–Borel condition（海涅–博雷尔条件）与 Bolzano–Weierstrass 提炼出 compactness（紧致性）（13.5），成为第 4 章闭区间上极值定理与一致连续定理在一般空间的化身。第一性原理是有限性原理：开覆盖的无限可能被压成 finite subcover（有限子覆盖），局部性质于是升级为全局性质。这正像 CSAPP 里计算机只有有限精度、有限内存，一切计算只能动用有限资源；区别是 CSAPP 的有限是硬件强制的近似，而有限子覆盖是严格保真的压缩。在 Strang 的有限维 $\mathbb{R}^n$ 里三件事等价：闭有界、紧致、sequential compactness（列紧，任何序列有收敛子列，即 Bolzano–Weierstrass 性质）；但到无穷维（平方可和序列空间 $\ell^2$ 的单位闭球）闭有界不再紧致，标准基 $e_n$ 满足 $\|e_n-e_m\|=\sqrt{2}$，无收敛子列——这是本章与线性代数最该记住的分界线。
>
> 随后是 separability（可分性）与 uniform continuity（一致连续）。可分性要求存在可数稠密子集，即用可数个简单对象就能任意逼近全体对象：$\mathbb{Q}^n$ 在 $\mathbb{R}^n$ 中稠密，多项式（Weierstrass approximation theorem，魏尔斯特拉斯逼近定理）在 $C[a,b]$ 中稠密；这就是“计算友好”的拓扑化表达。一致连续则要求同一个 $\delta$ 对所有点同时生效。配套证明模板可命名“有限子覆盖取最小 $\delta$”：先给每点一个局部 $\delta$，再用紧致性取有限子覆盖，最后取有限个 $\delta$ 的最小值；Lebesgue number lemma（勒贝格数引理，紧度量空间存在统一正数，凡直径小于它的集合必落在某个覆盖成员内）正是这把统一尺子。
>
> 此后 completion（完备化）与 Baire category theorem（贝尔纲定理）登场：完备是纲论证的前提，因为 Baire 定理断言完备空间中可数个稠密开集的交仍稠密。纲把集合量化为小集合（nowhere dense（无处稠密），即闭包的内部为空；first category（第一纲），即可数个无处稠密集的并）与大集合（residual set（剩余集），即第一纲集的补），一举导出“大多数连续函数处处不可微”“大多数闭集都是 Cantor 型集”这类存在性结论。这里要跟 6.042J 的基数大小划清界限：纲是拓扑意义下的“几乎”，与基数、测度是三把不同的尺子——$\mathbb{Q}$ 可数（基数小）却稠密、在 $\mathbb{R}$ 中属第一纲（拓扑小）；挖掉比例递减的“肥 Cantor 集”无处稠密（拓扑小）却可以有正长度（测度不小）。Baire 定理的证明本身就是对角线变体：在完备空间逐层取闭球套住一个点，与 6.042J 对角线论证共享“逐位规避”的思想。
>
> 有了完备骨架，13.9 的不动点定理，即 Banach contraction mapping theorem（巴拿赫压缩映射定理），顺理成章成为迭代逼近与方程解存在的利器。模板三步：取完备度量空间、验证压缩常数 $q<1$、从任意初值迭代，误差按 $d(x_n,x^*)\le\frac{q^n}{1-q}d(x_1,x_0)$ 收缩。具体例子：解 $x=\cos x$，在 $[0,1]$ 上 $|\cos'|=|\sin|\le\sin 1<1$，任意初值迭代都收敛到约 $0.739$。这呼应 Strang 的矩阵迭代：$x_{k+1}=Ax_k+b$ 收敛当且仅当 spectral radius（谱半径，特征值绝对值的最大值）小于 $1$，压缩常数正是谱半径的非线性推广；区别是 Strang 在线性有限维，Banach 定理覆盖非线性与函数空间（如积分方程）。回首全章其实只有一句话：从距离出发，用紧致与完备两条腿撑起整个度量世界的分析大厦，而 Baire 纲与不动点，是这座大厦上两扇最惊艳的窗。
