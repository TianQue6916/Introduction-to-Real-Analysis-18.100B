# <span style="color:#c0392b;">Elementary Real Analysis（初等实分析）</span>

> <span style="color:#7f8c8d;">行内双语翻译 · Part010（书页 435–484）</span>
> <span style="color:#7f8c8d;">范围：第 11 章 The Euclidean Spaces $\mathbb{R}^n$（欧几里得空间）全书正文 + 第 12 章 Differentiation on $\mathbb{R}^n$（$\mathbb{R}^n$ 上的微分）§12.1–§12.4</span>
> <span style="color:#7f8c8d;">源文件：TBB-AllChapters-Portrait_part010_p451-500.pdf（书页 = PDF 页 + 434）</span>
> <span style="color:#7f8c8d;">Second Edition (2008) · Brian S. Thomson, Judith B. Bruckner, Andrew M. Bruckner</span>
> <span style="color:#7f8c8d;">**格式：** 中文主体 + `English term（中文翻译）` 嵌入 · 深红标题 · 蓝色标签 · fenced math block · 无英文原句</span>
> <span style="color:#7f8c8d;">**习题区**（各节 Exercises、Notes 提示区 p.435–436、444、448、450 等）按约定跳过不收录</span>

---



<!-- ===== W1 ===== -->

<span style="color:#2471a3;">**[section]**</span>
# 第 11 章 欧几里得空间 $\mathbb{R}^n$

在 analysis（分析）的研究中，我们已经观察到实数系 $\mathbb{R}$ 远不止是一个 point（点）的集合。

它还拥有各种 algebraic（代数）、metric（度量）与 order（序）结构，这些结构在学科的发展中扮演着重要角色。

许多其他重要的数学对象集合也是如此。

其中最重要的就是我们在本章要研究的欧几里得空间（euclidean space）$\mathbb{R}^n$。

集合 $\mathbb{R}^n$ 中的元素极易描述：它就是所有实数 n-tuple（n 元组）

```math
x = (x_1, \ldots, x_n)
```

所构成的集合。

我们将花费一些时间发展一种自然的代数结构（空间 $\mathbb{R}^n$ 构成一个 vector space（向量空间））与一种自然的度量结构（存在自然的 distance（距离）概念），并在本章与下一章中加以利用。

（虽然我们也能在这些空间上强加序结构，但这样的结构对我们的目的并不自然，因而不会进入我们的讨论。）

<span style="color:#2471a3;">**[section]**</span>
# 11.1 $\mathbb{R}^n$ 的代数结构

空间 $\mathbb{R}^n$ 由实数的一切 n 元组 $x = (x_1, \ldots, x_n)$ 组成。

也就是说，$\mathbb{R}^n$ 是 $\mathbb{R}$ 的 n 个副本的 cartesian product（笛卡尔积）：

```math
\mathbb{R}^n = \mathbb{R} \times \mathbb{R} \times \cdots \times \mathbb{R} \quad (\text{n 个因子}).
```

$\mathbb{R}^n$ 中的成员 $x$ 被称为 $\mathbb{R}^n$ 的 point（点）。

它们也可以被视作 vector（向量），并把 $\mathbb{R}$ 当作 field of scalars（标量域）。

我们在 $\mathbb{R}^n$ 中按坐标逐项相加来定义向量的加法：若 $x = (x_1, \ldots, x_n)$、$y = (y_1, \ldots, y_n)$，则

```math
x + y = (x_1 + y_1, \ldots, x_n + y_n). \tag{1}
```

对 $\alpha \in \mathbb{R}$ 与 $x = (x_1, \ldots, x_n) \in \mathbb{R}^n$，我们定义

```math
\alpha x = (\alpha x_1, \ldots, \alpha x_n). \tag{2}
```

我们将这种以标量乘向量的运算称为 scalar multiplication（数乘，标量乘法）。

凭借加法与数乘这两种概念，$\mathbb{R}^n$ 具备了 vector space（向量空间）的代数结构。

这意味着 Theorem（定理）11.1 中所指出的那些性质都是成立的。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 把「逐坐标相加、逐坐标数乘」上升为「向量空间」，是线性代数史上最关键的一次抽象。你在 Strang 的教材里早已见过这八条公理（封闭、交换、结合、分配、零元、数乘等），但那是把 $\mathbb{R}^n$ 当作给定对象来用；这里 TBB 反过来问：到底哪些性质保证了「加减缩放向量」的运算合理？答案正是定理 11.1。留意两点：其一，运算 (1)(2) 是刻意按坐标逐项定义的，若换成「神秘加法」，封闭性立刻崩坏——正如 CSAPP 中数据必须有统一内存布局才能做批量运算；其二，这份公理清单由德国数学家 Hermann Grassmann 在 1844 年《线性扩张理论》中首次系统提出，直到 1888 年 Peano 才给出严格公理化，比微积分晚了近两个世纪，因为「空间可以不依赖坐标」这个观念本身需要时间成熟。未来在 6.042J 你学过的抽象化套路会再次出现：向量空间只是「带可逆加法与缩放运算的集合」，这正是第 13 章函数空间、序列空间的伏笔。


<span style="color:#2471a3;">**[theorem]**</span>
<span style="color:#c0392b;">**定理 11.1（Theorem 11.1）**</span>：若 $\mathbb{R}^n$ 上的加法与数乘分别由 (1) 与 (2) 定义，则对一切 $x, y, z \in \mathbb{R}^n$ 及一切 $\alpha, \beta \in \mathbb{R}$，下列各条全部成立：

---

<span style="color:#c0392b;">**定理 11.1（续）**</span>：所列性质如下：

```math
\begin{aligned}
x + y \in \mathbb{R}^n,\ \alpha x \in \mathbb{R}^n \quad & (\text{对加法与数乘封闭 closure})\\
x + y = y + x \quad & (\text{交换律 commutative law})\\
(x + y) + z = x + (y + z) \quad & (\text{结合律 associative law})\\
x + 0 = x \quad & (\text{其中 } 0 = (0, \ldots, 0))\\
\alpha(x + y) = \alpha x + \alpha y \quad & (\text{分配律 distributive laws})\\
(\alpha + \beta)x = \alpha x + \beta x \quad & \\
\alpha(\beta x) = (\alpha\beta)x \quad & \\
0x = 0 \quad & \\
1x = x. \quad &
\end{aligned}
```

这里 0 表示零向量 $0 = (0, \ldots, 0)$。

定理 11.1 的证明只是逐一检验每条陈述的简单练习。

我们把它留作 Exercise（习题）11.1.1。

我们还观察到，只要把减法定义为 $x - y = x + (-1)y$，便可得到 $x - x = 0$。

我们也可以把 $(-1)x$ 记作 $-x$，把 $(1/\alpha)x$ 记作 $x/\alpha$。

<span style="color:#2471a3;">**[section]**</span>
# 点积（The Dot Product）

我们将需要两个向量 $x$ 与 $y$ 之间的点积（dot product）概念。

它由下式定义：

```math
x \cdot y = x_1 y_1 + \cdots + x_n y_n, \tag{3}
```

其中 $x = (x_1, \ldots, x_n)$，$y = (y_1, \ldots, y_n)$。

注意到点积 (3) 是一个 scalar（标量）。

正因如此，$x \cdot y$ 有时被称为 $x$ 与 $y$ 的 scalar product（标量积）。

它有时也被称为 $x$ 与 $y$ 的 inner product（内积）。

点积满足某些条件，我们将其总结在 Theorem 11.2 中。

<span style="color:#2471a3;">**[theorem]**</span>
<span style="color:#c0392b;">**定理 11.2（Theorem 11.2）**</span>：若 $x, y, z \in \mathbb{R}^n$ 且 $\alpha \in \mathbb{R}$，则

```math
\begin{aligned}
x \cdot y &= y \cdot x \quad (\text{交换律 commutative law})\\
x \cdot (y + z) &= x \cdot y + x \cdot z \quad (\text{分配律 distributive law})\\
(\alpha x) \cdot y &= \alpha(x \cdot y).
\end{aligned}
```

我们把证明留作 Exercise 11.1.2。

注意到 $0 \cdot x = 0$，但 $x \cdot y$ 却可能在 $x$ 与 $y$ 都非零时等于 0 [例如，在 $\mathbb{R}^2$ 中，$(1, 1) \cdot (1, -1) = 1 - 1 = 0$]。

<span style="color:#00838f;">**定义（正交向量 orthogonal vectors）**</span>：两个非零向量 $x$ 与 $y$，若满足 $x \cdot y = 0$，则称它们为 orthogonal vectors（正交向量）。

从几何上看，$\mathbb{R}^n$ 中两个正交向量是垂直（perpendicular）的。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 点积看似只是"对应分量相乘再求和"的机械运算，却藏着整个欧氏几何：在 $\mathbb{R}^2$ 中 $x \cdot y = \|x\|\|y\|\cos\theta$，其中 $\theta$ 是两向量夹角。Strang 会告诉你这等价于"投影长度乘被投影向量长度"——把 $x$ 投影到 $y$ 方向，投影长为 $\|x\|\cos\theta$。于是"正交 ⇔ 点积为零"不是新公理，而是 $\cos(\pi/2)=0$ 的直接推论。为什么 TBB 不直接谈夹角而绕道点积？因为夹角公式需要余弦与反三角，点积却只含四则运算，能在任意维 $\mathbb{R}^n$ 机械计算——这是"用代数语言编码几何"的典范。定理 11.2 只要求对称、分配与数乘，刻意不保证"非零向量点积必非零"（如 $(1,1)\cdot(1,-1)=0$），正是把"垂直"这种几何关系精确化为可验证的代数条件。工程上你在 CSAPP 浮点章节后的向量检索里会再见到它：余弦相似度 $\cos\theta = x\cdot y/(\|x\|\|y\|)$，分母正是范数——为下一节 Cauchy-Schwarz 埋下伏笔。

<span style="color:#7f8c8d">*（本页其余部分为 §11.1 节习题区，按约定跳过。）*</span>


<!-- ===== W2 ===== -->

# 11.2 The Metric Structure of $\mathbb{R}^n$（$\mathbb{R}^n$ 的度量结构）

<span style="color:#2471a3;">**[figure]**</span> **图 11.1（Figure 11.1）：$\mathbb{R}^2$ 中的向量、距离与范数。**
图中绘出向量 $x$ 与 $y$，以及它们之差 $y - x$；同时标出范数 $\|x\|$、$\|y\|$ 与关系 $\|y - x\| = d(x, y)$，即两向量之差的范数正是两点间的距离。

<span style="color:#7f8c8d">*（本页中部为 §11.1 的习题区：习题 11.1.6，讨论 $\mathbb{C}[0, 2\pi]$ 上由 $f \cdot g = \int_0^{2\pi} f(t)g(t)\,dt$ 定义的点积，求证其满足定理 11.2 的条件，并构造正交函数集 $T = \{\sin nx, \cos mx : n = 1, 2, \dots, m = 1, 2, \dots\}$（即 $f, g \in T$ 且 $f \neq g$ 时 $f \cdot g = 0$），另附注 SEE NOTE 263。按约定跳过。）*</span>

<span style="color:#2471a3;">**[section]**</span> $\mathbb{R}^n$ 空间在任意两点之间天然具有一种距离（distance）的概念。
距离这一概念是许多分析概念的根基，例如序列收敛（convergence of sequences）、极限（limit）、连续性（continuity）与微分（differentiation）。
我们的出发点是 $\mathbb{R}^n$ 中向量 $x$ 的范数（norm）$\|x\|$。

<span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f;">**定义 11.3（Definition 11.3）：**</span>设 $x = (x_1, \ldots, x_n) \in \mathbb{R}^n$。
我们如下定义欧几里得范数（euclidean norm）：

```math
\|x\| = \sqrt{\sum_{i=1}^{n} x_i^2}.
```

<span style="color:#1e8449;">**[note]**</span> 注意对所有 $x \in \mathbb{R}^n$ 均有 $\|x\| \geq 0$。
在 $n = 1, 2, 3$ 这些熟悉的情形下，$\|x\|$ 恰好就是 $x$ 与零向量 $0$ 之间的距离。
例如在 $\mathbb{R}^2$ 中，$z = (x, y)$ 的范数为 $\|z\| = \sqrt{x^2 + y^2}$。

这启发我们对 $\mathbb{R}^n$ 中向量 $x$ 与 $y$ 之间的距离给出如下定义（见图 11.1）。

<span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f;">**定义 11.4（Definition 11.4）：**</span>对 $x, y \in \mathbb{R}^n$，$x$ 与 $y$ 之间的欧几里得距离（euclidean distance）定义为

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定义 11.3-11.4 把一维的「两数之差的大小 $|x-y|$」推广成多维的「向量差的长短 $\|x-y\|$」，这是本章最关键的一步「升维」。为什么用平方和的平方根，而不直接用 $\sum|x_i|$？因为只有这个定义让距离与点积绑定（$\|x\|^2 = x \cdot x$），从而保住「夹角、正交、投影」整套几何工具；$\|x\|_1=\sum|x_i|$ 虽也是合法长度，却会丢掉几何。从第一性原理看，范数不过是对「长度」提出三条最低要求：非负且零向量才零长、缩放即缩放长度、三角不等式——任何满足这三条的映射都配叫范数（定理 11.6）。CSAPP 里你早已用过它的离散版本：测量浮点误差、机器学习中 L1/L2 正则化，都是在换「长度标尺」。注意一维 $\mathbb{R}$ 上「绝对值」几乎是唯一的长度概念，而 $\mathbb{R}^n$ 上有无限多种范数——这种「测量自由」正是 §11.6 引出多种范数等价性的根源。


```math
d(x, y) = \|x - y\|.
```

用坐标表示，设 $x = (x_1, \ldots, x_n)$ 且 $y = (y_1, \ldots, y_n)$，则

```math
\|x - y\| = \sqrt{(x_1 - y_1)^2 + \cdots + (x_n - y_n)^2}.
```

注意我们还可以借助点积（dot product，即内积 inner product）来表达范数：

```math
\|x\|^2 = x \cdot x \quad \text{或} \quad \|x\| = \sqrt{x \cdot x}.
```

# 11 The Euclidean Spaces $\mathbb{R}^n$（欧几里得空间 $\mathbb{R}^n$）

<span style="color:#2471a3;">**[section]**</span> 正因为范数可由点积表达，许多范数的计算都可以借助点积（dot product）来化简。
点积与范数之间的一条重要关系，由 Cauchy-Schwarz 不等式（柯西-施瓦茨不等式）给出。

<span style="color:#2471a3;">**[theorem]**</span> **定理 11.5（Theorem 11.5，Cauchy-Schwarz）**对 $x, y \in \mathbb{R}^n$，有

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这个证明值得逐字背诵，它是「非负量构造」技巧的原型，我命名为「判别式夹逼」：要证 $|x\cdot y| \le \|x\|\|y\|$，就故意构造恒非负的二次函数 $p(t)=\|x-ty\|^2\ge 0$，展开成 $At^2+Bt+C$，再借用代数事实「恒非负二次式的判别式 $\le 0$」，$B^2-4AC\le 0$ 恰好直接吐出待证不等式。妙处全在第一步：把「乘积关系」编码成「平方后的长度」，而长度非负是免费的天然资源。历史：Cauchy 1821 年在《分析教程》（Cours d'Analyse）证明有限和版本，Bunyakovsky 1859 年给出积分版本，Schwarz 1888 年独立重证积分形式，故全称 Cauchy-Bunyakovsky-Schwarz 不等式。几何上它就是 $|\cos\theta|\le 1$ 的代数化身，等号当且仅当 $x$、$y$ 平行。它是下一节三角不等式证明的唯一引擎，重要性怎么强调都不过分；Rudin 第 1 章会把它推广到一般内积空间。


```math
|x \cdot y| \leq \|x\| \, \|y\|.
```

<span style="color:#2471a3;">**[proof]**</span> **证明（Proof）**首先注意，若 $t \in \mathbb{R}$，则

```math
p(t) = (x - ty) \cdot (x - ty) \geq 0. \tag{4}
```

利用定理 11.2（Theorem 11.2，点积的线性与对称性质），可将式 (4) 改写为

```math
p(t) = x \cdot x - 2(x \cdot y)t + (y \cdot y)t^2 \geq 0. \tag{5}
```

函数 $p(t)$ 是关于 $t$ 的二次式。由于它对所有 $t$ 均非负，它不可能有两个不同的实根。
因此其判别式不能为正，即

```math
4(x \cdot y)^2 - 4(x \cdot x)(y \cdot y) \leq 0. \tag{6}
```

由式 (6) 立即推出

```math
(x \cdot y)^2 \leq (x \cdot x)(y \cdot y),
```

于是

```math
|x \cdot y| \leq \|x\| \, \|y\|.
```

此即所要证明的结论。$\square$

<span style="color:#2471a3;">**[section]**</span> Cauchy-Schwarz 不等式使我们得以导出范数与距离（distance，亦常称为度量 metric）的一系列重要性质。

<span style="color:#2471a3;">**[theorem]**</span> **定理 11.6（Theorem 11.6，范数性质 Norm Properties）**设 $x, y \in \mathbb{R}^n$，$\alpha \in \mathbb{R}$。则
(i) $\|x\| \geq 0$，且 $\|x\| = 0$ 当且仅当 $x = 0$。
(ii) $\|\alpha x\| = |\alpha| \, \|x\|$。
(iii) $\|x + y\| \leq \|x\| + \|y\|$（三角不等式 triangle inequality）。

<span style="color:#2471a3;">**[proof]**</span> **证明** (i) 与 (ii) 的证明是显然的。为证 (iii)，我们计算

```math
\|x + y\|^2 = (x + y) \cdot (x + y) = \|x\|^2 + 2x \cdot y + \|y\|^2 \leq \|x\|^2 + 2\|x\| \|y\| + \|y\|^2 = (\|x\| + \|y\|)^2,
```

其中最后一个不等式由 Cauchy-Schwarz 不等式得出。$\square$

<span style="color:#2471a3;">**[theorem]**</span> **定理 11.7（Theorem 11.7，度量性质 Metric Properties）**距离函数

```math
d : \mathbb{R}^n \times \mathbb{R}^n \to \mathbb{R}
```

对所有 $x, y, z \in \mathbb{R}^n$ 满足下列条件：
(i) $d(x, y) \geq 0$，且 $d(x, y) = 0$ 当且仅当 $x = y$。
（其余条件 (ii)、(iii) 续于下一页。）


<!-- ===== W3 ===== -->

# <span style="color:#c0392b;">Section 11.2. The Metric Structure of $\mathbb{R}^n$（$\mathbb{R}^n$ 的度量结构）</span>

<!-- 书页 441：承接前页，本节 Theorem 11.7 之后半部分及其证明，随后为定理后说明文字 -->

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定理 11.6(iii) 三角不等式的证明是「展开-套不等式」模板的标准示范：先把 $\|x+y\|^2$ 用点积展开成 $\|x\|^2+2x\cdot y+\|y\|^2$，再把中间的 $2x\cdot y$ 用 Cauchy-Schwarz 放大到 $2\|x\|\|y\|$，最后开方收尾。这套「平方→展开→套不等式→开方」四步曲，是你今后证明一切范数三角不等式时的肌肉记忆。定理 11.7 把距离的四条性质（非负、零点、对称、三角）单独提炼出来，是抽象化的教科书级动作。1906 年 Fréchet 发现，只要集合上有满足这四条的 $d(x,y)$，「开集、收敛、连续」等全部分析概念都能原样展开——度量空间（metric space）由此诞生。这也是你未来泛函分析的起点。证明 (iii) 时令 $u=x-y$、$v=y-z$ 使 $u+v=x-z$ 的换元也很关键：把「经中间点 $y$ 绕路」翻译成「向量分解」，这是连接度量与向量结构的枢纽。


<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**定理 11.7（Theorem 11.7，度量性质 metric properties）**</span>（续前页）

（ii）$d(x, y) = d(y, x)$

（对称性 symmetry）。

（iii）$d(x, z) \leq d(x, y) + d(y, z)$

（三角不等式 triangle inequality）。

<span style="color:#2471a3;">**[proof]**</span> <span style="color:#c0392b;">**证明 Proof**</span>

证明（proof）再次指出，

（i）与（ii）的证明都是直接的（immediate）。

为验证（iii），

令 $u = x - y$，$v = y - z$。

于是 $u + v = x - z$。

由 Theorem 11.6 的（iii）我们看出

$\|u + v\| \leq \|u\| + \|v\|$，

即 $\|x - z\| \leq \|x - y\| + \|y - z\|$，

而这正是语句 $d(x, z) \leq d(x, y) + d(y, z)$。

$\square$

<span style="color:#2471a3;">**[note]**</span> <span style="color:#1e8449;">**定理之后的说明文字**</span>

在习题 11.2.6 与 11.2.7 中，

我们引入 $\mathbb{R}^n$ 上的另外两种范数（norm），

并在它们之间找出一些比较（comparison）。

稍后，习题 11.3.8 与 11.4.1 会展示

这些范数可以以某些方式互换使用，

当涉及与开集（open set）、闭集（closed set）以及收敛（convergence）直接相关的概念时。

因此，即使本节所遇到的欧几里得范数（euclidean norm）是我们的主要焦点，

其他范数也可以同时使用，

以简化并澄清论证。

<span style="color:#7f8c8d">*（本页其余部分为 §11.2 节习题区 Exercises，按约定跳过。）*</span>

<!-- 书页 442：§11.3 开篇，开头为习题 11.2.7–11.2.8 -->

<span style="color:#7f8c8d">*（本页开头为习题 11.2.7 与 11.2.8 习题区，按约定跳过。）*</span>

# <span style="color:#c0392b;">Section 11.3. Elementary Topology of $\mathbb{R}^n$（$\mathbb{R}^n$ 的初等拓扑）</span>

<span style="color:#2471a3;">**[section]**</span> 本节引言

到了现在，你已经理解距离（distance）这一概念

在研究 $\mathbb{R}$ 的过程中所扮演的根本角色。

确实，开集（open set）的概念是直接用距离概念来定义的。

其他各种重要概念，如闭集（closed set）、

稠密集（dense set）与聚点（accumulation point），

都直接或间接地依赖于距离概念。

在 $\mathbb{R}^n$ 中，情形同样如此。

在本节中，我们定义这些重要概念中的一部分。

我们将看到，只要把 $\mathbb{R}$ 上通常的距离函数

替换为 $\mathbb{R}^n$ 上的欧几里得距离函数（euclidean distance function），

$\mathbb{R}^n$ 中的定义就与 $\mathbb{R}$ 中的定义相同。

<span style="color:#2471a3;">**[definition]**</span> 开球与 $r$-邻域（open ball and $r$-neighborhood）

设 $x_0 \in \mathbb{R}^n$，并设 $r > 0$。

集合

```math
B(x_0, r) = \{x : \|x - x_0\| < r\}
```

称为以 $x_0$ 为中心、半径为 $r$ 的开球（open ball）。

它也被称为 $x_0$ 的 $r$-邻域（$r$-neighborhood）。

显然，它由 $\mathbb{R}^n$ 中那些到 $x_0$ 的距离小于 $r$ 的点组成。

我们以这个简单的概念为基础，

定义若干在 $\mathbb{R}$ 的研究中已经熟悉的术语。

<span style="color:#2471a3;">**[definition]**</span> 定义 1：开集（open set）

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 注意教材把开集定义为「每点含一个 $\varepsilon$ 球」，闭集定义为「补集是开集」，而不是用坐标不等式。这是被逼出来的：$\mathbb{R}$ 上有全局序 $\le$，开区间能写成 $\{x: a<x<b\}$；但 $\mathbb{R}^n$ 没有自然的「序」，只能退回局部语言——「$x_0$ 的某个球整体落在 $E$ 里」。这是把一维直觉迁移到多维时的关键范式转换。更要警惕一个陷阱：开与闭不是逻辑否定关系！空集与整个 $\mathbb{R}^n$ 既开又闭（彼此互为补集且都是开集），例 11.10 的 $\mathbb{Q}\times\mathbb{Q}$ 则既不开也不闭。6.042J 里你熟悉「$P$ 与非 $P$」的排中律，但「开/闭」对应的是「圈内/圈外/跨界」的三分，边界让这对词失效。而「边界点（每个球同时撞到 $E$ 内与外）」这个概念，将在第 12 章判断多元函数的连续与可微时反复出现。

若对每个 $x_0 \in E$ 都存在一个 $\varepsilon > 0$

<span style="color:#00838f;">使得 $B(x_0, \varepsilon) \subset E$，</span>

<span style="color:#00838f;">则 $\mathbb{R}^n$ 中的集合 $E$ 称为开集（open）。</span>

包含点 $x_0$ 的开集也称为 $x_0$ 的邻域（neighborhood）。

<span style="color:#2471a3;">**[definition]**</span> 定义 2：闭集（closed set）

<span style="color:#00838f;">若 $\mathbb{R}^n \setminus E$ 是开集，则 $\mathbb{R}^n$ 中的集合 $E$ 称为闭集（closed）。</span>

<span style="color:#2471a3;">**[definition]**</span> 定义 3：聚点 / 极限点（accumulation point / limit point）

若每个以 $x_0$ 为中心的开球都含有 $E$ 中异于 $x_0$ 的点，

<span style="color:#00838f;">则点 $x_0 \in E \subset \mathbb{R}^n$ 称为 $E$ 的聚点（accumulation point），或极限点（limit point）。</span>

我们将互换地使用「聚点」与「极限点」这两个术语。


<!-- ===== W4 ===== -->

# <span style="color:#c0392b;">书页 443 — §11.3 $\mathbb{R}^n$ 的初等拓扑（例 11.8–11.11）</span>

<span style="color:#2471a3;">**[section]**</span> §11.3 $\mathbb{R}^n$ 的初等拓扑（Elementary Topology of $\mathbb{R}^n$）。

<span style="color:#2471a3;">**[definition]**</span> **定义（续 4：边界点，boundary point）。** 若对每个 $\varepsilon > 0$，既有 $B(x_0, \varepsilon) \cap E \neq \varnothing$，又有 $B(x_0, \varepsilon) \setminus E \neq \varnothing$，
则称点 $x_0 \in \mathbb{R}^n$ 是集合 $E \subset \mathbb{R}^n$ 的一个<span style="color:#00838f">边界点（boundary point）</span>。

<span style="color:#2471a3;">**[definition]**</span> **定义（续 5：有界，bounded）。** 若存在 $M > 0$ 使得 $E \subset B(0, M)$，
则称集合 $E \subset \mathbb{R}^n$ 是<span style="color:#00838f">有界（bounded）</span>的。

在接下来的四个例子中，我们列出 $\mathbb{R}^2$ 的一些子集，并指出它们各自具有上述哪些性质。
这些性质的验证就留给你们完成。

<span style="color:#2471a3;">**[example]**</span> **例 11.8（x 轴）。** 设 $E_1 = \{(x, y) \in \mathbb{R}^2 : y = 0\}$，即 $\mathbb{R}^2$ 中的 x 轴。
$E_1$ 不是开集，但它是闭集；
$E_1$ 的每一点都是 $E_1$ 的聚点（accumulation point），同时也是 $E_1$ 的边界点；
并且 $E_1$ 不是有界集。

<span style="color:#2471a3;">**[example]**</span> **例 11.9（闭圆盘）。** 设 $E_2 = \{(x, y) : x^2 + y^2 \le 1\}$。
这个集合不是开集，但它是闭集；
$E_2$ 的每一点都是 $E_2$ 的聚点；
$E_2$ 的边界点正是那些满足 $x^2 + y^2 = 1$ 的点；
并且 $E_2$ 是有界集。

<span style="color:#2471a3;">**[example]**</span> **例 11.10（$\mathbb{Q} \times \mathbb{Q}$）。** 集合 $E_3 = \mathbb{Q} \times \mathbb{Q} = \{(x, y) : x \text{ 与 } y \text{ 均为有理数}\}$。
$E_3$ 既不是开集也不是闭集；
$\mathbb{R}^2$ 中的每一点都是 $E_3$ 的聚点，也都是 $E_3$ 的边界点；
并且 $E_3$ 在 $\mathbb{R}^2$ 中不是有界集。

<span style="color:#2471a3;">**[example]**</span> **例 11.11（环形区域）。** 环形区域（annular region）$E_4 = \{(x, y) : 1 < x^2 + y^2 \le 2\}$。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 例 11.8-11.11 是同一套「剥壳法」判定模板的四次演练。判断开集，就检查每个点脚下是否踩着一小块完全属于 $E$ 的领地（存在 $\varepsilon$ 球 $\subset E$）。判断闭集，就检查边界那层「壳」是否被包含——闭圆盘 $E_2$ 的壳是 $x^2+y^2=1$ 的圆周，壳被含住所以闭；环形 $E_4=\{1<x^2+y^2\le 2\}$ 外壳含住、内壳（$x^2+y^2=1$）漏掉，故不开不闭。这四个例子的设计近乎穷举典型形态：x 轴（一维对象嵌进二维）、闭圆盘（有界闭集）、$\mathbb{Q}\times\mathbb{Q}$（处处稠密却内部为空）、环形（开一半闭一半）。它们都在为 §11.8 紧致性埋伏笔——尤其 $E_2$ 这类「有界且闭」的集合将成为最重要的紧致集。也可以用 6.042J 的关系思维重看：开集定义是「对每个元素都成立某个局部性质」的全称命题。它与图论中「每点度 $\ge 2$」这类判定结构同构。
$E_4$ 既不是开集也不是闭集；
$\{(x, y) : 1 \le x^2 + y^2 \le 2\}$ 中的每一点都是 $E_4$ 的聚点；
$E_4$ 的边界点是那些满足 $x^2 + y^2 = 1$ 或 $x^2 + y^2 = 2$ 的点 $(x, y)$；
并且 $E_4$ 是有界集。

我们为 $\mathbb{R}$ 定义的其他术语，也可以用完全相同的方式在 $\mathbb{R}^n$ 中定义。
例如，孤立点（isolated point）、稠密集（dense set）与无处稠密集（nowhere dense set）这些概念，
在 $\mathbb{R}^n$ 中的定义方式与它们在 $\mathbb{R}$ 中的定义方式完全一致。
本章其余部分以及下一章的发展，将主要围绕 $\mathbb{R}^n$ 中的开集与闭集展开。
我们把这些概念以及其他相关概念的讨论留给习题。
紧致性（compactness）这一概念对我们的发展同样至关重要，
我们将在 §11.8 专门讨论紧致性。

在本节的习题中，会出现许多把本节各个概念彼此联系起来的结论，
它们与我们先前在 $\mathbb{R}$ 中已经注意到的那些结论是类似的。

<span style="color:#7f8c8d">*（本页其余部分为 §11.3 习题区，含习题 11.3.1–11.3.3，按约定跳过。）*</span>

# <span style="color:#c0392b;">书页 444 — §11.3 习题区（跳过）</span>

<span style="color:#7f8c8d">*（书页 444 为 §11.3 习题区，含习题 11.3.4–11.3.8，按约定跳过。）*</span>


<!-- ===== W5 ===== -->

# <span style="color:#c0392b;">书页 445 — §11.4 $\mathbb{R}^n$ 中的序列（定义 11.12–11.14）</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定义 11.12 把「序列」规定为函数 $f: \mathbb{N}\to\mathbb{R}^n$，绝非咬文嚼字：一维序列 $\{x_k\}$ 你已熟练，但高维序列的每一项是向量，黑体 $\mathbf{x}_k$ 提醒你「这是整体替换，不是并列 $n$ 条一维序列」。为什么必须用函数来定义？因为无穷多个元素无法一一列举，$\mathbb{N}$ 充当「计数器」给出访问顺序——这与数组下标是同一件事，只是 CSAPP 的数组必须有限，数学的序列可以无限。定义 11.14 中 $\|\mathbf{x}_k-\mathbf{x}\|<\varepsilon$ 的范数，精确扮演绝对值在 $|x_k-x|<\varepsilon$ 中的角色：把「逐项接近」从数轴上靠拢升级为多维空间中靠拢。它还有三种等价说法：进入每个含 $\mathbf{x}$ 的开球、$\|\mathbf{x}_k-\mathbf{x}\|\to 0$、$d(\mathbf{x}_k,\mathbf{x})\to 0$。记住这套「一鱼三吃」，后面引理 11.30 会证明函数极限与序列极限正因为这些等价说法而互通。

<span style="color:#2471a3;">**[section]**</span> §11.4 $\mathbb{R}^n$ 中的序列（Sequences in $\mathbb{R}^n$）。

我们在实数序列（sequences of real numbers）方面研究过的大部分内容，
都可以原样移植到 $\mathbb{R}^n$ 中序列的情形。
事实上，$\mathbb{R}^n$ 中序列的许多证明，与 $\mathbb{R}$ 中相应结论的证明几乎是完全相同的。
我们把这些证明中的大部分留给习题。
当某个证明需要新的想法时，我们会给出完整的详细证明。

<span style="color:#2471a3;">**[definition]**</span> **定义 11.12（$\mathbb{R}^n$ 中的点序列）。**
<span style="color:#00838f">$\mathbb{R}^n$ 中的点序列（sequence of points）是一个函数 $f : \mathbb{N} \to \mathbb{R}^n$。</span>

与 $\mathbb{R}$ 中序列的情形一样，我们经常使用诸如 $\{\mathbf{x}_k\}$ 这样的记号来表示 $\mathbb{R}^n$ 中的序列。
请注意，这里的 $\mathbf{x}$ 是黑体（表示一个向量），而 $k$ 不是黑体，因为它表示一个自然数。
如果更方便，我们也可以用双下标记号（double subscript notation）把该序列改写成一个 n 元组（n-tuple）：
$\mathbf{x}_k = (x_{k1}, \ldots, x_{kn})$。

<span style="color:#2471a3;">**[definition]**</span> **定义 11.13（有界序列）。**
<span style="color:#00838f">若存在 $M \in \mathbb{N}$，使得对所有 $k \in \mathbb{N}$ 都有 $\|\mathbf{x}_k\| \le M$，则称 $\mathbb{R}^n$ 中的序列 $\{\mathbf{x}_k\}$ 是有界（bounded）的。</span>

我们可以用与实数序列相同的方式来定义 $\mathbb{R}^n$ 中序列 $\{\mathbf{x}_k\}$ 的收敛（convergence）（参见定义 2.6）。
注意，在这里范数（norm）所扮演的角色，正是此前绝对值（absolute value）所扮演的角色。

<span style="color:#2471a3;">**[definition]**</span> **定义 11.14（收敛序列）。**
<span style="color:#00838f">设 $\{\mathbf{x}_k\}$ 是 $\mathbb{R}^n$ 中的序列。若对每个 $\varepsilon > 0$ 都存在 $N \in \mathbb{N}$，使得当 $k \ge N$ 时总有 $\|\mathbf{x}_k - \mathbf{x}\| < \varepsilon$，则我们说 $\{\mathbf{x}_k\}$ 收敛（converges）到点 $\mathbf{x}$，并记作 $\lim_{k \to \infty} \mathbf{x}_k = \mathbf{x}$，或当 $k \to \infty$ 时 $\mathbf{x}_k \to \mathbf{x}$。</span>

该定义等价于如下要求：每个以 $\mathbf{x}$ 为中心的开球（open ball）都包含该序列除有限项以外的全部项——
即对每个 $\varepsilon > 0$ 都存在 $N$，使得对所有 $k \ge N$ 都有 $\mathbf{x}_k \in B(\mathbf{x}, \varepsilon)$。
它同样等价于如下的要求：当 $k \to \infty$ 时，$\|\mathbf{x}_k - \mathbf{x}\| \to 0$，
或者当 $k \to \infty$ 时 $d(\mathbf{x}_k, \mathbf{x}) \to 0$，其中 $d$ 是欧几里得距离（euclidean distance）。

<span style="color:#c0392b;">**逐坐标收敛（Coordinate-Wise Convergence）。**</span> 我们还可以用逐坐标收敛来描述 $\mathbb{R}^n$ 中的收敛。
为了看出这一点，首先注意：对 $\mathbf{x} = (x_1, \ldots, x_n)$ 以及 $j = 1, \ldots, n$，有

```math
x_j^2 \le \sum_{i=1}^{n} x_i^2 = \|\mathbf{x}\|^2 \le \left( \sum_{i=1}^{n} |x_i| \right)^2.
```

# <span style="color:#c0392b;">书页 446 — §11.4（续：定理 11.15–11.17）</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定理 11.17 证明里最精彩的一步是「归纳取半」：先选 $x_1$ 满足 $0<\|x_1-x\|<1$，之后每次要求 $0<\|x_{k+1}-x\|<\frac12\|x_k-x\|$。这一步双保险——距离每步至少减半保证收敛，同时严格小于一半保证 $x_{k+1}\neq x_k$，从而构造的点互异。为什么非「互异」不可？因为聚点定义要求「每个开球含 $E$ 中异于 $x_0$ 的点」，若允许重复，任何单点集都「收敛」于自身，定理就失去意义——这个细节自学时极易忽略。序列刻画之所以重要，在于它把「每个开球都要撞到」这种几何条件翻译成可操作的「存在一串点逼近 $x$」的算法语言，与定义 11.14 格式一致。反过来想，6.042J 中「$\mathbb{Q}$ 在 $\mathbb{R}$ 中稠密」正是靠这种构造证明的：每给一个 $\varepsilon$ 区间都能用有理点去填。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 不等式链 $|x_j|\le\|x\|\le\sum|x_i|$（(7)式）是本章第二个值得背的「夹逼」工具，我称它「逐分量夹逼」：每个坐标的绝对值都不超过欧几里得范数，而欧几里得范数又不超过一范数（各分量绝对值之和）。它立刻把「向量接近」翻译成「每个坐标都接近」（(8)式），于是定理 11.15 的逐坐标收敛判定几乎是免费的。这背后是典型的分治思想——你在 CLRS 里见过无数次：把 $n$ 维整体问题拆成 $n$ 个独立的一维子问题，分别验证再合并。工程上的对应同样直接：CSAPP 中判断多维数据是否足够接近，往往就是对每个坐标设容差逐一检查。更深一层，(7)式是「不同范数互相控制」的第一个具体证据，图 11.4 与引理 11.34 将系统化这一点：在有限维 $\mathbb{R}^n$ 中换一把「长度标尺」不会改变收敛与否，这就是范数等价（norm equivalence）观念的萌芽。

于是得到

```math
|x_j| \le \|\mathbf{x}\| \le \sum_{i=1}^{n} |x_i|.   \tag{7}
```

现在设 $\{\mathbf{x}_k\} = \{(x_{k1}, \ldots, x_{kn})\}$ 是 $\mathbb{R}^n$ 中的序列，
并设 $\mathbf{x} = (x_1, \ldots, x_n)$ 是 $\mathbb{R}^n$ 中的一点。
由 (7) 式得

```math
|x_{kj} - x_j| \le \|\mathbf{x}_k - \mathbf{x}\| \le \sum_{i=1}^{n} |x_{ki} - x_i|.   \tag{8}
```

若当 $k \to \infty$ 时 $\mathbf{x}_k \to \mathbf{x}$，即当 $k \to \infty$ 时 $\|\mathbf{x}_k - \mathbf{x}\| \to 0$，
则从 (8) 式可知，对每个 $j = 1, \ldots, n$，都有当 $k \to \infty$ 时 $|x_{kj} - x_j| \to 0$。
反之，若对每个 $j = 1, \ldots, n$ 都有当 $k \to \infty$ 时 $|x_{kj} - x_j| \to 0$，
则当 $k \to \infty$ 时，$\sum_{i=1}^{n} |x_{ki} - x_i| \to 0$，
于是再次由 (8) 式看出，当 $k \to \infty$ 时 $\|\mathbf{x}_k - \mathbf{x}\| \to 0$。
我们把上述讨论总结为一条定理。

<span style="color:#2471a3;">**[theorem]**</span> **定理 11.15（逐坐标收敛的判定）。**
设 $\{\mathbf{x}_k\} = \{(x_{k1}, \ldots, x_{kn})\}$ 是 $\mathbb{R}^n$ 中的序列，
并设 $\mathbf{x} = (x_1, \ldots, x_n) \in \mathbb{R}^n$。
则 $\lim_{k \to \infty} \mathbf{x}_k = \mathbf{x}$ 当且仅当对每个 $j = 1, \ldots, n$ 都有 $\lim_{k \to \infty} x_{kj} = x_j$。

<span style="color:#c0392b;">**代数性质（Algebraic Properties）。**</span> 我们的下一个结果说明，
极限在加法、标量乘法（scalar multiplication）与点积（dot product）运算下会按预期方式组合。
我们把证明留作习题 11.4.2。

<span style="color:#2471a3;">**[theorem]**</span> **定理 11.16（极限的代数性质）。**
设 $\{\mathbf{x}_k\}$ 与 $\{\mathbf{y}_k\}$ 是 $\mathbb{R}^n$ 中的序列，并设 $\alpha \in \mathbb{R}$。
若 $\lim_{k \to \infty} \mathbf{x}_k = \mathbf{x}$ 且 $\lim_{k \to \infty} \mathbf{y}_k = \mathbf{y}$，则

(i) $\lim_{k \to \infty} (\alpha \mathbf{x}_k) = \alpha \mathbf{x}$；

(ii) $\lim_{k \to \infty} (\mathbf{x}_k + \mathbf{y}_k) = \mathbf{x} + \mathbf{y}$；

(iii) $\lim_{k \to \infty} (\mathbf{x}_k \cdot \mathbf{y}_k) = \mathbf{x} \cdot \mathbf{y}$。

<span style="color:#c0392b;">**聚点（Limit Points）。**</span> 正如在 $\mathbb{R}$ 中那样，
我们可以用序列的语言来刻画 $\mathbb{R}^n$ 中的聚点（limit point）。

<span style="color:#2471a3;">**[theorem]**</span> **定理 11.17（用序列刻画聚点）。**
设 $E \subset \mathbb{R}^n$ 且 $\mathbf{x} \in \mathbb{R}^n$。
则 $\mathbf{x}$ 是 $E$ 的聚点，当且仅当存在由 $E$ 中互不相同的点组成的序列 $\{\mathbf{x}_k\}$，
使得 $\lim_{k \to \infty} \mathbf{x}_k = \mathbf{x}$。


<!-- ===== W6 ===== -->

# <span style="color:#c0392b;">书页 447 — §11.4 $\mathbb{R}^n$ 中的序列（定理 11.17 证明收尾、11.18、11.19）</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这个定理的名字就是一部数学史：Bernard Bolzano 在 1817 年的《纯粹分析的证明》中为证介值定理首次使用它；半个多世纪后，Karl Weierstrass 在 1860 年代的柏林讲义中重新证明并系统传播，才有今天的命名——它是 Weierstrass「分析算术化」（用 $\varepsilon$-$\delta$ 语言重铸微积分）工程的一部分。一维版本「有界数列必有收敛子列」的本质是抽屉原理＋二分：把有界区间对半分，无穷多项总有一半含无穷多项，递归下去正如 CLRS 二分搜索锁定目标。本书把证明升到 $n$ 维用的是「逐坐标筛选」：先对第一坐标抽子列，再在子列上对第二坐标抽子列……共抽 $n$ 层，最后用定理 11.15 逐坐标收敛合并。留意教材强调「记号如何简化细节」——第 $k$ 层子列用 $k(1,i), k(2,i), \ldots, k(n,i)$ 记录，把「子序列的子序列」压缩成一条下标链，这正是你写递归算法时「状态压缩」的同款思维。Rudin 第 2 章会给出等价于紧致性的表述。

<span style="color:#2471a3;">**[section]**</span> §11.4 $\mathbb{R}^n$ 中的序列（Sequences in $\mathbb{R}^n$）。

<span style="color:#1e8449">注：定理 11.15、11.16 及定理 11.17 的陈述位于上一页（书页 446）；本页以定理 11.17 的证明收尾开始，随后给出定理 11.18 与定理 11.19（Bolzano-Weierstrass 定理）。</span>

<span style="color:#2471a3;">**[proof]**</span> **证明（定理 11.17，承上页）。** 设 $x$ 是集合 $E$ 的聚点（limit point）。
则对每个 $\varepsilon > 0$，存在 $E$ 中满足 $x_k \neq x$ 的点 $x_k$，使得 $\|x_k - x\| < \varepsilon$。
先选取 $x_1 \in E$，使得 $0 < \|x_1 - x\| < 1$。
归纳地，在已经选取 $x_k$ 之后，再选取 $E$ 中的 $x_{k+1}$，使得 $0 < \|x_{k+1} - x\| < \tfrac{1}{2}\|x_k - x\|$。
于是 $\lim_{k \to \infty} x_k = x$，$x_k \neq x$，且当 $k \neq j$ 时 $x_k \neq x_j$。
逆命题是显然的。$\square$

<span style="color:#2471a3;">**[theorem]**</span> **定理 11.18。** 集合 $E \subset \mathbb{R}^n$ 是<span style="color:#00838f">闭集（closed set）</span>，当且仅当它包含它的全部聚点。
其证明留作习题 11.4.3（按约定习题跳过）。

一维情形的 Bolzano-Weierstrass 定理（Bolzano-Weierstrass theorem）断言：有界实数序列（bounded sequence of real numbers）必含有收敛子序列（convergent subsequence）。
这条定理可以推广到 $\mathbb{R}^n$，并将在我们研究 $\mathbb{R}^n$ 上的连续函数时扮演重要角色。
其证明需要把一维版本使用 $n$ 次。
虽然证明的想法直截了当，但记号却相当凌乱——它涉及"子序列的子序列的子序列"，共 $n$ 层。
我们将采用更紧凑的记号，以避免多层的下标。
这个证明值得仔细研读，从中可以看到：恰当的记号如何把原本杂乱的细节简化。

<span style="color:#2471a3;">**[theorem]**</span> **定理 11.19（Bolzano-Weierstrass 定理）。** $\mathbb{R}^n$ 中的每个有界序列 $\{x_k\}$ 都含有一个收敛子序列。

<span style="color:#2471a3;">**[proof]**</span> **证明。** 设 $\{x_k\}$ 是 $\mathbb{R}^n$ 中的有界序列，即对所有 $k \in \mathbb{N}$ 都有 $\|x_k\| \le M$。
对每个 $k$，把 $x_k$ 写为 $x_k = (x_{k1}, \ldots, x_{kn})$。
则对每个 $k \in \mathbb{N}$ 及 $j = 1, \ldots, n$，都有 $|x_{kj}| \le M$。
因此，对一切 $j$，实数序列（sequence of real numbers）$\{x_{kj}\}$ 都是有界的。
令 $j = 1$。把 Bolzano-Weierstrass 定理应用于有界序列 $\{x_{k1}\}$（$k = 1, 2, 3, \ldots$），
就存在一个整数序列 $1 \le k(1,1) < k(1,2) < \cdots$，
以及一个数 $x_1$，使得当 $i \to \infty$ 时 $x_{k(1,i),1} \to x_1$。
注意，序列 $\{x_{k(1,i),1}\}$ 正是序列 $\{x_{k1}\}$ 的一个子序列。
下一步令 $j = 2$。序列 $\{x_{k(1,i),2}\}$ 同样以 $M$ 为界，
于是再次运用 Bolzano-Weierstrass 定理，存在 $\{k(1,i)\}$ 的一个子序列 $\{k(2,i)\}$，使得 $\{x_{k(2,i),2}\}$ 收敛。
令 $x_2 = \lim_{i \to \infty} x_{k(2,i),2}$。
现在，序列 $\{x_{k(1,i),1}\}$ 收敛于 $x_1$，故该序列的任何子序列也都收敛于 $x_1$。
特别地，当 $i \to \infty$ 时，$\{x_{k(2,i),1}\} \to x_1$。
我们继续这一过程。
在已经得到满足 $\{x_{k(m,i),m}\} \to x_m$（对所有 $m \le j$ 成立）的序列 $\{x_{k(j,i),j}\}$ 之后，
我们再次使用 Bolzano-Weierstrass 定理，进一步得到一个子序列 $\{x_{k(j+1,i),j+1}\}$，它收敛于一点 $x_{j+1} \in \mathbb{R}$。
当 $j + 1 = n$ 时，这一过程终止。
令 $k_i = k(n,i)$，$x = (x_1, \ldots, x_n)$，则由定理 11.15 知 $\lim_{i \to \infty} x_{k_i} = x$。$\square$

---

# <span style="color:#c0392b;">书页 448 — §11.4 习题区（跳过）与 §11.5 开头</span>

<span style="color:#7f8c8d">*（本页其余部分为 §11.4 习题区，含习题 11.4.1–11.4.10，按约定跳过，不翻译、不收录。）*</span>

<span style="color:#2471a3;">**[section]**</span> §11.5 函数与映射（Functions and Mappings）。

在前几章处理函数时，我们主要关心这样的函数：其定义域（domain）是 $\mathbb{R}$ 的子集，其值域（range）落在 $\mathbb{R}$ 中；
这些函数传统上被称为"实变量的实值函数（real-valued function of a real variable）"。
这些函数的定义域通常都是区间（interval）。
在本章与下一章中，我们关心的是……（原文到此换页，此句在书页 449 继续）。


<!-- ===== W7 ===== -->

# <span style="color:#c0392b;">书页 449 — §11.5 函数与映射（开篇，例 11.20–11.23）</span>

<span style="color:#2471a3;">**[section]**</span> §11.5 Functions and Mappings（函数与映射）。

（接上页）这些函数，其定义域与值域都位于空间 $\mathbb{R}^n$ 中。
通常，其定义域是 $\mathbb{R}^n$ 的一个开子集（open subset）。
与我们研究单实变量的实值函数（real functions of a real variable）时的情况一样，
我们的研究聚焦于极限、连续性（continuity）与可微性（differentiability）等问题。
在本节中，我们只处理若干定义、若干例子，以及一点关于记法（notation）的内容。

<span style="color:#2471a3;">**[section]**</span> **11.5.1 从 $\mathbb{R}^n$ 到 $\mathbb{R}$ 的函数（Functions from $\mathbb{R}^n \to \mathbb{R}$）。**

让我们从函数 $f : E \to \mathbb{R}$ 开始，其中 $E$ 是 $\mathbb{R}^n$ 的一个子集。
这类函数有时被称为「多变量实值函数」（real functions of several variables）。
我们给出一些例子。
对于 $n = 2$ 的情形，即对函数 $f : \mathbb{R}^2 \to \mathbb{R}$，有一个特殊而传统的记法特点：
表示点 $(x_1, x_2) \in \mathbb{R}^2$ 所需的两个变量被写作 $(x, y)$。
在所有讨论中，x 指第一个变量，y 指第二个变量。
类似地，对于函数 $f : \mathbb{R}^3 \to \mathbb{R}$，我们常常用 $(x, y, z)$ 而非 $(x_1, x_2, x_3)$ 来表示 $\mathbb{R}^3$ 中的点。
我们通常都会采用这一约定，尤其是在下一章讨论导数（derivative）时。
对于 $n \ge 4$，则使用下标记法。

<span style="color:#2471a3;">**[example]**</span> **例 11.20（双变量多项式）。** 设 $f(x, y) = x^2 + xy + y^2 + 5$。
$f$ 的一个自然定义域（natural domain）是全部的 $\mathbb{R}^2$，因此 $f : \mathbb{R}^2 \to \mathbb{R}$ 是一个双变量函数。
函数 $f$ 是双变量多项式（polynomial in two variables）的一个例子。
一般的双变量多项式可以写成

```math
f(x, y) = \sum_{i, j} a_{ij} x^i y^j \qquad (9)
```

其中系数 $a_{ij}$ 是实数，指数 $i$ 与 $j$ 是非负整数，且求和只含有限多项。
图 11.2（Figure 11.2）展示了这个多项式 $f$ 在 $\mathbb{R}^3$ 中的图像（graph），
你应该从微积分课程中熟悉这样的表示。
在我们的大部分研究中，我们将无法依赖任何有意义的图形，
因为我们研究的是多变量函数，而在 $\mathbb{R}^2$ 与 $\mathbb{R}^3$ 之外的图形是不可能的。
即便如此，我们仍依赖这些特殊情形，来帮助我们建立对更一般情形中发生之事的直觉。

<span style="color:#2471a3;">**[example]**</span> **例 11.21（闭单位球）。** 设 $g(x_1, x_2, x_3) = 1 - x_1^2 - x_2^2 - x_3^2$。
这里 $g$ 的一个自然定义域是集合 $E = \{(x_1, x_2, x_3) : x_1^2 + x_2^2 + x_3^2 \le 1\}$。
你会认出 $E$ 就是空间 $\mathbb{R}^3$ 中的闭单位球（closed unit ball）。

<span style="color:#2471a3;">**[example]**</span> **例 11.22（对数函数）。** 设 $h(x, y) = \ln xy$。
$h$ 的一个自然定义域是集合 $E = \{(x, y) : xy > 0\}$，因此 $E$ 由 xy 平面的第一与第三开象限（open quadrants）之并构成。

<span style="color:#2471a3;">**[example]**</span> **例 11.23（三角形面积）。** 对 $\mathbb{R}^2$ 中的每个三角形 $T$，令 $A(T)$ 表示该三角形的面积。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这四个例子教你同一件事：多变量函数的第一步永远是找「自然定义域」。$f(x,y)=x^2+xy+y^2+5$ 定义域是整个 $\mathbb{R}^2$，很平凡；但 $\ln(xy)$ 要求 $xy>0$，即 $x$、$y$ 同号——第一、三象限；$1-x_1^2-x_2^2-x_3^2$ 则要求三坐标平方和 $\le 1$（闭单位球）。这与你写程序时检查输入合法性如出一辙：函数公式只告诉你「怎么算」，自然定义域告诉你「对哪些输入公式有意义」，两者缺一不可——CSAPP 中非法输入常导致未定义行为，数学里同理。注意 $f(x,y)=x^2+xy+y^2$ 这类二次多项式正是 Strang 教材中二次型与对称矩阵的原料，它恒正（正定）与否将决定几何形状。教材还提醒：$n\ge 4$ 时图像是 $\mathbb{R}^{n+1}$ 的子集、无法画出——人眼只能感知三维投影，这迫使你放弃图形、依赖代数直觉，这是分析学家与工程师思维分道扬镳的关键一课。
我们可以把 $A$ 看作一个函数，其定义域是 $\mathbb{R}^2$ 中所有三角形构成的集合。
但我们也可以把 $A$ 的公式表示为六个变量的函数：若 $(a, b), (c, d), (e, f)$ 是 $T$ 的顶点，
那么我们就能把面积表示为函数 $g : \mathbb{R}^6 \to \mathbb{R}$，其中 $g(a, b, c, d, e, f) = A(T)$。
（习题 11.5.2 要求给出该面积的解析公式。）

# <span style="color:#c0392b;">书页 450 — §11.5 函数与映射（续，图 11.2，例 11.24–11.25）</span>

<span style="color:#2471a3;">**[figure]**</span> **图 11.2（Figure 11.2）：** 多项式 $f(x, y) = x^2 + xy + y^2 + 5$ 的图像（坐标轴为 z、y、x）。

有时，不直接引用坐标来表示一个函数会更加方便。

<span style="color:#2471a3;">**[example]**</span> **例 11.24（线性函数）。** 设 $a \in \mathbb{R}^n$，并令 $f : \mathbb{R}^n \to \mathbb{R}$ 由 $f(x) = a \cdot x$ 定义（其中 $\cdot$ 表示点积，dot product）。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 例 11.24 是 Strang 线性代数与本章的第一次正面握手：$f(x)=a\cdot x$ 就是「行向量 $a^T$ 乘列向量 $x$」，是矩阵乘法的 $1\times n$ 特例。教材断言「每个线性函数 $\mathbb{R}^n\to\mathbb{R}$ 都能写成某个 $a$ 的点积」（习题 11.5.3），这个结论值得停下来细想：它意味着「线性函数」与「向量 $a$」一一对应——函数是抽象的规则，向量是可算的数据，二者通过点积互相编码。这是对偶空间（dual space）观念的第一印象：所有线性函数本身也构成一个向量空间，只是你现在还不知道这个名字，第 13 章或泛函分析会正式登场。为什么这重要？因为第 12 章可微性定义正是「用线性函数局部逼近 $f$」：$f(x_0+h)\approx f(x_0)+a\cdot h$，那个 $a$ 就是梯度。可以说，线性函数是多元微积分的「零件」，例 11.24 就是在拆解这个零件。
若 $a = (a_1, \ldots, a_n)$ 且 $x = (x_1, \ldots, x_n)$，
则 $f(x) = f(x_1, \ldots, x_n) = a_1 x_1 + \cdots + a_n x_n$。
这类函数就是线性函数（linear functions）。
这意味着它们满足条件：对一切 $\alpha, \beta \in \mathbb{R}$ 以及一切 $x, y \in \mathbb{R}^n$，
有 $f(\alpha x + \beta y) = \alpha f(x) + \beta f(y)$。
事实上，每个线性函数 $f : \mathbb{R}^n \to \mathbb{R}$ 都可以表示为 $f(x) = a \cdot x$ 的形式，
对某个 $a \in \mathbb{R}^n$ 以及一切 $x \in \mathbb{R}^n$ 成立。
我们把这一验证留作习题 11.5.3。

<span style="color:#2471a3;">**[example]**</span> **例 11.25（欧几里得范数函数）。** 对每个 $x \in \mathbb{R}^n$，令 $f(x) = \|x\|$。
于是 $f : \mathbb{R}^n \to \mathbb{R}$。
用坐标来表示，$f(x) = f(x_1, \ldots, x_n) = \sqrt{x_1^2 + \cdots + x_n^2}$。

<span style="color:#7f8c8d">*（本页其余部分为 §11.5 习题区，含习题 11.5.1–11.5.3，按约定跳过。）*</span>


<!-- ===== W8 ===== -->

# <span style="color:#c0392b;">书页 451 — §11.5 函数与映射（例 11.26–11.27）</span>

<span style="color:#2471a3;">**[section]**</span> §11.5 函数与映射（Functions and Mappings）。

<span style="color:#c0392b;">**11.5.2 从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的函数（Functions from $\mathbb{R}^n$ → $\mathbb{R}^m$）**</span>

当处理定义域在 $\mathbb{R}^n$、值域在 $\mathbb{R}^m$ 的函数时，我们常使用映射（mapping）或变换（transformation）或算子（operator）来代替“函数”一词。
术语<span style="color:#00838f">向量值函数（vector-valued function）</span> 也同样常用。

我们一直用粗体字母表示 $\mathbb{R}^m$（$m \ge 2$）中的向量或点。
我们也将用粗体字母表示值域在 $\mathbb{R}^m$（$m \ge 2$）中的函数。
设 $E \subset \mathbb{R}^n$ 且 $f : E \to \mathbb{R}^m$，那么对一切 $x \in E$，都有 $f(x) \in \mathbb{R}^m$。
若用坐标表示 $x$ 与 $f(x)$，比如说 $x = (x_1, \ldots, x_n)$、$f(x) = (y_1, \ldots, y_m)$，则

```math
f(x_1, \ldots, x_n) = (y_1, \ldots, y_m).
```

当然，这些数 $y_1, \ldots, y_m$ 依赖于 $x = (x_1, \ldots, x_n)$。
因此存在函数 $f^1, \ldots, f^m : E \to \mathbb{R}$，称为<span style="color:#00838f">坐标函数（coordinate functions）</span>，使得

```math
\begin{aligned}
y_1 &= f^1(x) = f^1(x_1, \ldots, x_n)\\
y_2 &= f^2(x) = f^2(x_1, \ldots, x_n)\\
&\vdots\\
y_m &= f^m(x) = f^m(x_1, \ldots, x_n)
\end{aligned}
```

我们对函数 $f^j$ 使用上标而不是下标，这是为了避免与我们在第 12 章中用于偏导数（partial derivative）的下标记号相混淆。

<span style="color:#2471a3;">**[example]**</span> **例 11.26：** 定义 $f : \mathbb{R}^2 \to \mathbb{R}^2$ 为

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 例 11.26-11.28 展示了向量值映射的三个原型。例 11.26 的极坐标变换 $(r,\theta)\mapsto(r\cos\theta, r\sin\theta)$ 说明同一函数既可看作几何坐标变换，也可看作两个坐标函数的打包。例 11.27 把线性映射与矩阵乘法接通——Arthur Cayley 1858 年正式定义矩阵乘法，从此线性映射有了紧凑的数据表示，这正是 Strang 全书的主线；$A(\alpha x_1+\beta x_2)=\alpha Ax_1+\beta Ax_2$ 就是线性性的矩阵写法。例 11.28 的 $T(x,y)=(e^x\cos y, e^x\sin y)$ 最有味道：它就是复指数 $e^{x+iy}=e^x(\cos y+i\sin y)$（欧拉公式，Euler 1748 年提出），CSAPP 复数章节里你已见过它的单位圆旋转形态。几何上 $T$ 把竖直线 $x=x_0$ 卷到半径为 $e^{x_0}$ 的圆上（无限缠绕），把水平线 $y=y_0$ 映成从原点出发的射线——一幅「把平面网格变形」的活地图。教材特意说图像在 $\mathbb{R}^4$ 里画不出，逼我们用「网格如何变形」理解映射，这为第 12 章 Jacobian 行列式（面积缩放因子）埋下伏笔。

```math
f(r, \theta) = (r\cos\theta, \; r\sin\theta), \qquad r, \theta \in \mathbb{R}.
```

于是 $f^1(r, \theta) = r\cos\theta$，$f^2(r, \theta) = r\sin\theta$。
对 $r \ge 0$，这个映射 $f$ 在把极坐标（polar coordinates）变换为直角坐标（rectangular coordinates）时为我们所熟悉。
这里我们通常把 $f^1$ 写作 $x$、把 $f^2$ 写作 $y$，于是得到

```math
x = r\cos\theta, \qquad y = r\sin\theta.
```

$\blacksquare$

<span style="color:#2471a3;">**[example]**</span> **例 11.27（线性函数，linear functions）：** 设 $A : \mathbb{R}^n \to \mathbb{R}^m$ 由下列方程给出

```math
\begin{aligned}
y_1 &= a_{11}x_1 + \cdots + a_{1n}x_n\\
y_2 &= a_{21}x_1 + \cdots + a_{2n}x_n\\
&\vdots\\
y_m &= a_{m1}x_1 + \cdots + a_{mn}x_n
\end{aligned}
```

其中 $a_{ij} \in \mathbb{R}$，$i = 1, \ldots, m$，$j = 1, \ldots, n$，且 $x = (x_1, \ldots, x_n)$。
变换 $A$ 可以用一个矩阵 $A = (a_{ij})$ 来表示，它是系数组成的 $m \times n$ 矩阵。
于是我们得到 $A(x) = Ax$。

# <span style="color:#c0392b;">书页 452 — §11.5 函数与映射（例 11.27 续–例 11.28）</span>

这个乘积就是矩阵乘法（matrix multiplication）：

```math
\begin{pmatrix}
a_{11} & \cdots & a_{1n}\\
\vdots &        & \vdots\\
a_{m1} & \cdots & a_{mn}
\end{pmatrix}
\begin{pmatrix}
x_1\\ \vdots\\ x_n
\end{pmatrix}
```

容易检验 $A$ 是线性的（linear），也就是说

```math
A(\alpha x_1 + \beta x_2) = \alpha A(x_1) + \beta A(x_2)
```

对一切 $\alpha, \beta \in \mathbb{R}$ 以及一切 $x_1, x_2 \in \mathbb{R}^n$ 成立。（见习题 11.5.4。）$\blacksquare$

注意，在例 11.27 中我们用大写字母表示从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的线性变换（linear transformation）。
这是一种常见做法，在处理其他向量空间（vector space）上的线性变换时也经常这样用（见第 13 章）。
即使函数并非线性，有时人们也倾向于用大写字母来表示从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的变换。
我们将采用对当前目的而言方便的任何记号。
关于记号再说一句：有时，特别是处理线性变换时，用 $Ax$ 这样的记号代替 $A(x)$ 会很方便。
我们将在各场合使用当时方便的记号。

<span style="color:#2471a3;">**[example]**</span> **例 11.28：** 设 $T(x, y) = (u, v)$，其中 $u = e^x\cos y$，$v = e^x\sin y$。
于是 $u = T^1(x, y) = e^x\cos y$，$v = T^2(x, y) = e^x\sin y$。
我们可以研究映射 $T$ 的一些几何性质。
注意 $u^2 + v^2 = e^{2x}$，且 $v\cos y = u\sin y$。
对固定的 $x_0$，$(u, v)$ 是圆心在 $(0, 0)$、半径为 $e^{x_0}$ 的圆上的一个点。
当 $y$ 在长度为 $2\pi$ 的区间上增加时，$(u, v)$ 恰好绕那个圆一周。
于是 $T$ 把直线 $x = x_0$ 无限多次地绕到那个圆上。
类似地，$T$ 把直线 $y = y_0$ 映满一条从原点出发、斜率为 $\tan y_0$ 的射线（ray）。
关于这一点以及 $T$ 的其他一些映射性质的验证，我们留到习题 11.5.5。
注意，倘若我们想要对这个函数作图形表示，它会给我们带来一些问题。
该函数的图像将是 $\mathbb{R}^4$ 的子集，因而超出了我们所能表示的能力。
图 11.3 可以用来研究这个函数；你应该已经熟悉微积分课程中这样的表示。
这幅图承载了先前讨论过的关于直线映到圆的信息。$\blacksquare$

在第 12 章中，我们将关心多变量函数以及映射的可微性（differentiability）。
我们工作的核心将是利用线性变换来逼近这样的函数或映射。

<span style="color:#7f8c8d">*（本页其余部分为 §11.5 习题区，含习题 11.5.4–11.5.6，按约定跳过。）*</span>


<!-- ===== W9 ===== -->

# <span style="color:#c0392b;">书页 453 — §11.5 末尾（例 11.28 收尾）＋ §11.6 从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的函数极限开篇</span>

<span style="color:#2471a3;">**[figure]**</span> **图 11.3（Figure 11.3）：函数 $T(x, y) = (u, v)$ 的一个图示，其中 $u = e^x \cos y$，$v = e^x \sin y$。**

图中分别标出 xy-平面上的坐标轴 $x$、$y$ 与 uv-平面上的坐标轴 $u$、$v$。

该图用以表示映射 $T$ 把 xy-平面中的点送到 uv-平面中的点。

（承接例 11.28 极坐标映射的收尾部分：）

<span style="color:#7f8c8d;">*（本页顶部为 §11.5 习题区，含习题 11.5.6 的跨页延续——关于 $H(x, y) = (x^2 - y^2, 2xy)$ 的问题，按约定跳过不收录。）*</span>

<span style="color:#2471a3;">**[section]**</span>
# §11.6 从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的函数极限（Limits of Functions from $\mathbb{R}^n \to \mathbb{R}^m$）

对函数 $f : E \to \mathbb{R}^m$ 而言，极限（limit）这一概念与一元实函数的情形是完全类似的。

这里 $E \subset \mathbb{R}^n$，而一元情形下则是 $f : E \to \mathbb{R}$，其中 $E \subset \mathbb{R}$。

我们想要把握这样一层意思：当 $x$ 在 $E$ 中靠近 $x_0$ 时，$f(x)$ 靠近 $y_0 \in \mathbb{R}^m$。

我们的定义、若干基本结果及其证明，本质上与一元实函数的对应内容完全相同。

<span style="color:#2471a3;">**[section]**</span>
# 11.6.1 定义（Definition）

我们从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的函数之极限的 $\varepsilon$-$\delta$ 定义开始。

它与序列版本的等价性，将在随后的 Lemma（引理）11.30 中证明。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 引理 11.30 是把「连续语言」翻译成「离散语言」的翻译机：函数极限（$\varepsilon$-$\delta$，涉及无穷多个点）⇔ 序列极限（$x_k\to x_0$ 则 $f(x_k)\to y_0$，只涉及可数个点）。这个翻译极其值钱，因为序列工具更丰富——定理 11.16 的代数性质、BW 定理都能直接引用，定理 11.38 的证明正是这么「偷懒」成功的。正向是「连续性继承」：若 $\varepsilon$-$\delta$ 极限存在，任何趋近 $x_0$ 的序列都被强制押进 $y_0$ 的任意 $\varepsilon$ 邻域。反向是证明模板「反证构造数列」：假设极限不存在，就取出 $\varepsilon_0$ 和坏点 $x_k$（满足 $0<\|x_k-x_0\|<1/k$ 但 $\|f(x_k)-y_0\|\ge\varepsilon_0$），$x_k$ 明明收敛到 $x_0$，$f(x_k)$ 却赖着不走——矛盾。这与 CSAPP 的「采样」思想共鸣：反证法就是在通往 $x_0$ 的所有道路中，故意挑出最能暴露问题的那条。Rudin 第 4 章会把此引理推广成判定连续性的标准工具。

<span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f;">**定义 11.29（Definition 11.29）：**</span>设 $f : E \to \mathbb{R}^m$，其中 $E$ 是 $\mathbb{R}^n$ 的一个子集。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定义 11.29 有个常被忽略却关键的设定：$x_0$ 必须是 $E$ 的聚点。为什么？因为极限描述的是「$x$ 逼近 $x_0$ 时 $f(x)$ 的趋势」，若 $x_0$ 是孤立点（周围没有 $E$ 的其他点），「逼近过程」无从谈起，定义会退化成空洞的真命题。这与你写数值程序的直觉一致：想在 $x_0$ 附近采样，前提是附近有样本点可采。还要注意两条「无所谓」：极限值与 $f$ 在 $x_0$ 处是否有定义无关，也与 $f(x_0)$ 的值无关——例 11.31 中 $f(0,0)=7$ 却照样有极限 0。这就是可去间断点（removable discontinuity）的雏形：函数在某点打了个洞，我们仍能问洞外的行为。CSAPP 里浮点计算的病态输入类似：极限关心的永远是「趋近过程」而非「到达那一点」。邻域语言的等价描述（对 $y_0$ 的每个邻域 $V$，存在 $x_0$ 的邻域 $U$ 使 $f((U\cap E)\setminus\{x_0\})\subset V$）则把 $\varepsilon$-$\delta$ 几何化，是通向拓扑学的最短桥梁。

再设 $x_0$ 是 $E$ 的一个 limit point（聚点，极限点）。

若对每个 $\varepsilon > 0$，都存在 $\delta > 0$，使得当 $0 < \|x - x_0\| < \delta$ 且 $x \in E$ 时，恒有 $\|f(x) - y_0\| < \varepsilon$，则我们说

```math
\lim_{x \to x_0} f(x) = y_0.
```

注意到：极限的存在性以及它的取值，与 $f$ 在 $x_0$ 处是否有定义，都没有关系。

同样地，它也与 $f(x_0)$ 的值是什么无关。

用粗略的几何语言来说，$\lim_{x \to x_0} f(x) = y_0$ 意味着：对 $y_0$ 的每个 neighborhood（邻域）$V$，无论多么小，都对应着 $x_0$ 的一个充分小的邻域 $U$。

这个邻域 $U$ 满足：$f$ 把 $(U \cap E) \setminus \{x_0\}$ 映入 $V$。

（这个定义以及这段讨论，应当与第 5 章中对一元实函数极限的处理相对照。）

# <span style="color:#c0392b;">书页 454 — §11.6 引理 11.30（序列刻画）＋ 例 11.31、例 11.32</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这个例子真正值得背下来的不是"极限等于 0"这个结论，而是核心估计 $|xy| \le x^2 + y^2$。它其实是二维均值不等式的特例：由 $(|x|-|y|)^2 \ge 0$ 展开得 $2|xy| \le x^2+y^2$，比你需要的那条还强一倍。代回原函数，注意到 $|x^2-y^2|/(x^2+y^2) \le 1$，就有 $|f(x,y)| \le |xy| \le r^2$，其中 $r=\sqrt{x^2+y^2}$——这告诉我们 $f$ 沿任何方向都是"二阶小"（$O(r^2)$ 量级），极限为 0 只是最浅层的收获，第 12 章你甚至会看到它在原点可微。我把这套手法命名为「有界因子夹逼」：把分式拆成"有界因子 × 可控制因子"，再用 $r$ 衡量阶数，是多元极限里最常用的万能钥匙。拿它对比例 11.32 的 $2xy/(x^2+y^2)$，后者沿径向是常数（$O(1)$ 量级，分子分母同阶），阶数对比能一眼看穿两个例子的本质差异。

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 例 11.31 与 11.32 是多元分析最反直觉的一幕，务必反复咀嚼。一元时 $x$ 只能从左右两侧逼近 $x_0$，两侧极限一致极限即存在；多元时「逼近」的路径有无穷多条（任意曲线皆可），极限存在要求沿所有路径极限相同。例 11.32 中 $f(x,y)=2xy/(x^2+y^2)$：沿 x 轴或 y 轴逼近极限是 0，沿直线 $y=x$ 逼近却是 1——同一函数、同一目标点、不同路径给不同极限，故二重极限不存在。这是「路径法」判据的首次亮相：要证极限不存在，只需找两条极限不同的路径；但反过来，找一万条路径一致也不能证明极限存在——要证存在只能正面 $\varepsilon$-$\delta$ 或换元化简（例 11.31 用 $|xy|\le x^2+y^2$ 夹逼）。「正面证明难、反证找茬易」的不对称，在 6.042J 逻辑课程里你已遇过：全称命题（所有路径）的否定就是存在性构造。CSAPP 中多线程竞争复现困难与此神似——结果依赖执行路径。

我们的引理把这个极限概念与序列版本（sequential）的极限概念联系起来。

后者正是一元函数情形下 §5.1.2 中内容的类比。

<span style="color:#2471a3;">**[lemma]**</span> <span style="color:#c0392b;">**引理 11.30（Lemma 11.30）：**</span>设 $E \subset \mathbb{R}^n$，并设 $x_0$ 是 $E$ 的一个 accumulation point（聚点）。

假设 $f : E \to \mathbb{R}^m$。

则 $\lim_{x \to x_0} f(x) = y_0$ 当且仅当：对满足 $x_k \to x_0$ 且 $x_k \neq x_0$ 的每个序列 $\{x_k\} \subset E$，都有 $f(x_k) \to y_0$。

<span style="color:#2471a3;">**[proof]**</span> **证明（Proof）**假设 $\lim_{x \to x_0} f(x) = y_0$。

设 $x_k \to x_0$（$x_k \neq x_0$），$x_k \in E$，并任取 $\varepsilon > 0$。

则存在 $\delta > 0$，使得若 $x \in E$ 且 $0 < \|x - x_0\| < \delta$，就有

```math
\|f(x) - y_0\| < \varepsilon.
```

由于 $x_k \to x_0$，存在 $N \in \mathbb{N}$，使得当 $k \geq N$ 时 $\|x_0 - x_k\| < \delta$。

于是对 $k \geq N$，有 $\|f(x_k) - y_0\| < \varepsilon$。

从而 $f(x_k) \to y_0$。

为证反方向，假设 $y_0$ 不是 $f(x)$ 在 $x \to x_0$ 时的极限。

则存在 $\varepsilon > 0$，使得对每个 $k \in \mathbb{N}$，都存在 $x_k \in E$，满足

```math
0 < \|x_k - x_0\| < \frac{1}{k}
```

且 $\|f(x_k) - y_0\| \geq \varepsilon$。

此时序列 $\{x_k\}$ 收敛到 $x_0$，但序列 $f(x_k)$ 不收敛到 $y_0$。$\square$

<span style="color:#2471a3;">**[example]**</span> **例 11.31（Example 11.31）：**设

```math
f(x, y) = xy\,\frac{x^2 - y^2}{x^2 + y^2}, \qquad f(0, 0) = 7.
```

则 $f : \mathbb{R}^2 \to \mathbb{R}$。

我们来证明

```math
\lim_{(x, y) \to (0, 0)} f(x, y) = 0.
```

任取 $\varepsilon > 0$。

当 $(x, y) \neq (0, 0)$ 时，我们有

```math
|f(x, y) - 0| \leq |xy| \, \frac{|x^2 - y^2|}{|x^2 + y^2|} \leq |xy|.
```

现在对一切 $(x, y) \in \mathbb{R}^2$ 都有 $|xy| \leq x^2 + y^2$。

因此当 $\sqrt{x^2 + y^2} < \delta = \varepsilon$（且 $(x, y) \neq (0, 0)$）时，就有 $|f(x, y)| < \varepsilon$。

于是

```math
\lim_{(x, y) \to (0, 0)} f(x, y) = 0.
```

<span style="color:#1e8449;">**[note]**</span> 注意：$f(0, 0) = 7$ 这一事实并不影响上述极限。

当极限存在时，它必然是唯一的（Exercise 11.6.2）。

我们有时可以利用这一事实来证明某个极限不存在。

<span style="color:#2471a3;">**[example]**</span> **例 11.32（Example 11.32）：**设

```math
f(x, y) = \frac{2xy}{x^2 + y^2}, \qquad f(0, 0) = 0.
```

（本函数在该点极限不存在的讨论，续于下一页。）


<!-- ===== W10 ===== -->

# <span style="color:#c0392b;">书页 455 — §11.6 函数极限（续）：例 11.32 尾声、例 11.33、§11.6.2 坐标式收敛</span>

<span style="color:#2471a3;">**[section]**</span> §11.6 从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的函数极限（Limits of Functions from $\mathbb{R}^n$ to $\mathbb{R}^m$），承接前页内容。

<span style="color:#2471a3;">**[example]**</span> **例 11.32（续）**：设 $f(x, y) = \dfrac{2xy}{x^2 + y^2}$，$f(0, 0) = 0$。

这里 $\lim_{y \to 0} f(0, y) = \lim_{x \to 0} f(x, 0) = 0$，
但二重极限 $\lim_{(x,y) \to (0,0)} f(x, y)$ 并不存在。

要看清这一点，只需观察
$\lim_{t \to 0} f(t, t) = \lim_{t \to 0} \dfrac{2t^2}{2t^2} = 1$。

于是，沿坐标轴趋近 $(0, 0)$ 要求极限为 0，
而沿直线 $y = x$ 趋近 $(0, 0)$ 又要求极限为 1。

由此可知，对 $0 < \varepsilon < 1$，
不存在 $y_0 \in \mathbb{R}$ 与 $\delta > 0$，
使得当 $0 < \sqrt{x^2 + y^2} < \delta$ 时
恒有 $|f(x, y) - y_0| < \varepsilon$。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 例 11.32 用极坐标可以一眼看穿。令 $x = r\cos\theta$、$y = r\sin\theta$，则 $f(r\cos\theta, r\sin\theta) = 2\cos\theta\sin\theta = \sin 2\theta$——结果与 $r$ 无关！这意味着从原点出发沿不同射线逼近，$f$ 分别趋向不同的常数 $\sin 2\theta$：沿 $y=x$（$\theta=\pi/4$）得 1，沿 $x$ 轴（$\theta=0$）得 0，沿 $y=-x$（$\theta=-\pi/4$）得 $-1$。于是 $f$ 在原点附近的值"铺满"整段 $[-1,1]$，像一把没有闭合的扇子。这给出可复用的判据，我命名为「极坐标扇形法」：若 $f$ 在极坐标下只依赖 $\theta$（或依赖 $\theta$ 的方式随 $\theta$ 跳跃），则二重极限必不存在。反过来要警惕：沿所有直线极限都相同也推不出二重极限存在——抛物线路径 $y=x^2$ 往往能戳穿这种假象（习题 11.7.12 就是陷阱）。CSAPP 里多线程竞争的结果依赖调度路径，与此是同一哲学：整体收敛要求"与路径无关"。

<span style="color:#2471a3;">**[example]**</span> **例 11.33**：设 $f(r, \theta) = (r \cos \theta, r \sin \theta)$。

于是 $f: \mathbb{R}^2 \to \mathbb{R}^2$。
我们要证明 $\lim_{(r, \theta) \to (0,0)} f(r, \theta) = (0, 0)$。

此时有
$\|f(r, \theta) - (0, 0)\| = \sqrt{r^2 \cos^2 \theta + r^2 \sin^2 \theta} = |r|$。

因此只要 $|r| < \varepsilon$，就有 $\|f(r, \theta) - (0, 0)\| < \varepsilon$，
且该结论与 $\theta$ 无关。

特别地，若 $0 < \|(r, \theta)\| = \sqrt{r^2 + \theta^2} < \delta = \varepsilon$，
则 $|r| < \varepsilon$，
故 $\lim_{(r, \theta) \to (0,0)} f(r, \theta) = (0, 0)$。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 例 11.33 是全书第一次展示"向量值映射的极限可以直接算范数"：$f(r,\theta)=(r\cos\theta, r\sin\theta)$ 的差范数 $\|f(r,\theta)-(0,0)\| = \sqrt{r^2\cos^2\theta + r^2\sin^2\theta} = |r|$，一步消掉 $\theta$。这里没有走定理 11.36 的"逐坐标"路线，而是正面用定义——因为 $\|f\|$ 恰好有干净表达式，直接逼近比拆坐标更快。注意 $f$ 就是书页 451-452 例 11.26 的极坐标映射本身：例 11.26 强调它"把平面网格扭曲"（几何视角），这里强调它在原点连续（解析视角）——这两个视角正是你理解一切向量值映射的双通道，第 12 章研究 Jacobian 行列式（面积缩放因子）时二者会合流。还要留意"该结论与 $\theta$ 无关"这句话的分量：它在说 $f$ 从所有方向逼近原点的行为一致，这正是多维极限存在性的灵魂。Strang 会告诉你，$f$ 在这里就是把"极坐标输入"转成"直角坐标输出"的坐标变换，连续意味着"小扰动的输入只引起小扰动的输出"——数值计算里坐标系转换的稳定性问题，本质就是问这个映射是否连续。

<span style="color:#7f8c8d">*（本页其余部分为 §11.6 习题区，含习题 11.6.1–11.6.3，按约定跳过。）*</span>

<span style="color:#2471a3;">**[section]**</span> §11.6.2 坐标式收敛（Coordinate-Wise Convergence）。

我们此前（习题 11.2.6、11.2.7、11.3.8 与 11.4.1）已经看到，
$\mathbb{R}^n$ 上还有更多范数（norm）可用于研究收敛（convergence）。

下面我们简要讨论范数 $\|\cdot\|_\infty$ 与极限概念之间的联系。

这将使我们更深入地洞察极限概念的本质，
尤其能让我们证明：收敛可以按坐标逐分量地（coordinate-wise）加以解释。

# <span style="color:#c0392b;">书页 456 — §11.6.2 坐标式收敛：图 11.4、$\|\cdot\|_\infty$ 与引理 11.34 及其证明</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 引理 11.34 的证明骨架是「双包含论证」模板，请把它和 CLRS 里证明"两个复杂度函数同阶"（$f=\Theta(g)$ 需 $f=O(g)$ 且 $g=O(f)$）对照记忆：欧氏球与无穷范数方块互相夹逼，等价于"换一把尺子测收敛，收敛性不变"。具体说，(10) 式 $B(\cdot,r)\subset B_\infty(\cdot,r)$ 给出"欧氏收敛 ⇒ 无穷范数收敛"（更紧的球含在更松的方块里），(11) 式给出反向。证明里那个"取 $\varepsilon_0 < \varepsilon$ 使方块落进球里"的小技巧，本质是"留出余量再收紧"，和你在 CLRS 二分搜索里"取中点缩区间"的余量思想同源。为什么这个引理重要？因为它把"收敛"从具体范数中解放出来——收敛性是几何性质，不依赖你选哪把尺子。但要记住这是有限维特权：第 13 章的函数空间里范数不再等价，收敛会真的随范数改变，届时这条引理就是你对比记忆的锚点。

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 图 11.4 把三种范数的几何差异画得淋漓尽致：欧几里得范数的单位球是圆（圆盘），无穷范数 $\|\cdot\|_\infty$ 的单位球是与坐标轴平行的正方形，一范数 $\|\cdot\|_1$ 的单位球是菱形。关键不在形状不同，而在于它们互相咬合——(10)(11) 式表明：任意一个欧氏球都含有一个无穷范数方块，反之任意无穷范数方块也含有一个欧氏球。这种「夹逼」保证收敛概念不随范数改变，引理 11.34 正是把这一观察形式化。这就是有限维范数等价观念的第一印象：在 $\mathbb{R}^n$ 中，无论选用哪种「长度标尺」，「哪些序列收敛、哪些集合开」都纹丝不动。但这是有限维的特权——你未来在泛函分析遇到的无限维函数空间里，范数等价不再成立，收敛性会真的随范数而变，所以教材在这里刻意铺垫，是给你埋下对比的记忆点。CSAPP 的类比：换一把尺子测同一根杆，数值变了，但「谁长谁短」的相对关系不变。

<span style="color:#2471a3;">**[figure]**</span> **图 11.4**：三种范数 $\|\cdot\|_1$、$\|\cdot\|$ 与 $\|\cdot\|_\infty$
下、以原点为中心的三个单位球（unit ball），自内而外排列。

我们首先回顾无穷范数（infinity norm）的定义，
并将其与欧几里得范数（euclidean norm）作比较。

对 $x = (x_1, \ldots, x_n) \in \mathbb{R}^n$，我们曾定义
$\|x\|_\infty = \max\{|x_1|, |x_2|, \ldots, |x_n|\}$。

为简单起见，先考察 $\mathbb{R}^2$ 的情形，
用 $(x, y)$ 表示 $\mathbb{R}^2$ 中的元素。

于是 $\|(x, y)\| = \sqrt{x^2 + y^2}$，
而 $\|(x, y)\|_\infty = \max\{|x|, |y|\}$。

欧几里得开球（open euclidean ball）$B((0,0), r)$
是以 $(0, 0)$ 为圆心、半径为 $r$ 的开圆盘（open disk）。

开球 $B_\infty((0,0), r)$ 则是以 $(0, 0)$ 为中心、
边与坐标轴平行、边长为 $2r$ 的开正方形（open square）。

注意 $B((0,0), r) \subset B_\infty((0,0), r)$，
并且存在 $s > 0$ 使得 $B_\infty((0,0), s) \subset B((0,0), r)$。

图 11.4 给出了三种范数 $\|\cdot\|_1$、$\|\cdot\|$ 与 $\|\cdot\|_\infty$
下以原点为中心的三个单位球。

对以 $\mathbb{R}^2$ 中其他点为中心的球，也有类似的结论。

对任意的 $n \in \mathbb{N}$，类似情形同样成立。

对每个 $r > 0$ 与 $x_0 \in \mathbb{R}^n$，我们有

```math
\{x \in \mathbb{R}^n : \|x - x_0\| < r\} \subset \{x \in \mathbb{R}^n : \|x - x_0\|_\infty < r\} \tag{10}
```

并且存在 $s > 0$ 使得

```math
\{x \in \mathbb{R}^n : \|x - x_0\|_\infty < s\} \subset \{x \in \mathbb{R}^n : \|x - x_0\| < r\}. \tag{11}
```

由这些包含关系可以看出，
在定义 11.14 与定义 11.29 中，我们可将 $\|\cdot\|_\infty$ 替换 $\|\cdot\|$，
而不会改变任何结论。

也就是说，序列极限（sequence limit）的定义
等价于下面这个使用不同范数的版本。

<span style="color:#2471a3;">**[lemma]**</span> <span style="color:#c0392b;">**引理 11.34**</span>：

极限 $x_k \to x$ 在范数 $\|\cdot\|$ 的意义下成立，
当且仅当对一切 $\varepsilon > 0$，存在整数 $N$，
使得只要 $k \geq N$ 就有 $\|x_k - x\|_\infty < \varepsilon$。

<span style="color:#2471a3;">**[proof]**</span> <span style="color:#c0392b;">**证明 Proof**</span>

设 $x_k \to x$，并取 $\varepsilon > 0$。

则存在 $N \in \mathbb{N}$，使得对所有 $k \geq N$ 都有 $\|x_k - x\| < \varepsilon$。

由 (10) 可见，对所有 $k \geq N$ 都有 $\|x_k - x\|_\infty < \varepsilon$。

因此 $x_k \to x$ 在 $\|\cdot\|_\infty$ 的意义下成立。

反之，设 $x_k \to x$ 在 $\|\cdot\|_\infty$ 的意义下成立。

取 $\varepsilon > 0$，利用 (11)，选取 $\varepsilon_0 < \varepsilon$，
使得若 $\|z - x\|_\infty < \varepsilon_0$，则 $\|z - x\| < \varepsilon$。

现在，存在 $N \in \mathbb{N}$，使得当 $k \geq N$ 时，……
（本页在证明中途截断，证明剩余部分续于书页 457。）


<!-- ===== W11 ===== -->

# <span style="color:#c0392b;">书页 457 — §11.6 函数极限（续）：引理 11.34 证明收尾、引理 11.35、坐标式收敛与定理 11.36</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定理 11.36 是第 12 章 Jacobian 的伏笔。把 $f=(f^1,\ldots,f^m)$ 想成一个 $m$ 元函数组，其极限存在当且仅当每个坐标函数 $f^j$ 的极限存在——这正是 Strang 线性代数里"矩阵按行理解"的翻版：$m$ 维输出看成 $m$ 个独立的一维输出，整体性质由各行拼装。到了第 12 章，$f$ 在一点可微意味着它被一个线性映射（Jacobian 矩阵 $J_f$）局部逼近，而 $J_f$ 的第 $j$ 行恰好是坐标函数 $f^j$ 的梯度 $\nabla f^j$——逐坐标视角从极限一路贯穿到微分。这里还有个必须区分的微妙点：定理 11.36 说的是"输出"逐坐标（$f$ 的分量分别收敛），输入 $x$ 仍是整体逼近；这与"输入"逐坐标（沿坐标轴方向逼近，即偏导数）完全不同——后者恰恰是例 11.42 会粉碎的错觉。分清"输出的逐坐标"与"输入的逐坐标"，是你接下来不踩坑的关键，也是理解第 12 章可微性定义的前提。

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 引理 11.35 的洞察在于"证明的稳定性"：把定义 11.29 里的 $\|\cdot\|$ 换成 $\|\cdot\|_\infty$，极限概念完全没变。为什么可以这么大胆？因为 (10)(11) 说明两种范数在"谁接近谁"的意义上不可区分——差别只是常数因子，而 $\varepsilon$-$\delta$ 语言天然容忍常数因子（$\varepsilon$ 可以任意取小）。这与你在 CSAPP 里用不同范数评估浮点误差（L1/L2/无穷范数）是同一个思路：量纲不同，收敛判定一致。证明留作习题 11.6.5，提示就藏在引理 11.34 的证明里——把"序列"换成"函数"，把 $k\ge N$ 换成 $0<\|x-x_0\|_\infty<\delta$，其余照抄。做完这道题你会意识到：$\varepsilon$-$\delta$ 证明是"模板化"的，换范数、换空间，骨架不变。正因为引理 11.30（序列刻画）、11.34、11.35 三个工具层层叠套，定理 11.36 的证明才能一句话带过——这正是分层抽象在数学里的样子。

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定理 11.36 是全书「降维打击」的典范：一个 $\mathbb{R}^n\to\mathbb{R}^m$ 的映射极限存在，当且仅当它的 $m$ 个坐标函数 $f^1,\ldots,f^m$ 分别作为普通实值函数极限存在且极限取对应坐标。这是一次彻头彻尾的分治——CLRS 里「把大问题拆成可独立解决的小问题再合并」的套路，在这里把「向量值极限」分解成 $m$ 个「一元实值极限」，后者你在第 5 章已炉火纯青。证明只用引理 11.35 加上观察 $|z_i|\le\|z\|_\infty$（无穷范数逐分量夹逼），干净利落。为什么要费这个劲？因为坐标函数极限可调用全部一元工具（夹逼、代数性质、BW），而直接处理向量值极限会陷入多维 $\varepsilon$-$\delta$ 的泥潭。这与 CSAPP 中处理多维数组的优化如出一辙：逐维分解、逐维优化、最后合并。更抽象地看，它揭示了欧氏空间收敛结构的「可分性」：整体信息完全包含在分量信息中，这是欧氏空间区别于一般度量空间（如函数空间）的重要属性，第 13 章你会看到该性质失效的案例。

<span style="color:#2471a3;">**[section]**</span> §11.6 从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的函数极限（Limits of Functions from $\mathbb{R}^n$ to $\mathbb{R}^m$），续接书页 456。

<span style="color:#2471a3;">**[proof]**</span> <span style="color:#c0392b;">**证明 Proof（引理 11.34 收尾）**</span>

现在，存在 $N \in \mathbb{N}$，使得当 $k \geq N$ 时
有 $\|x_k - x\|_\infty < \varepsilon_0$。

于是对一切 $k \geq N$，都有 $\|x_k - x\| < \varepsilon$。

这便表明 $x_k \to x$ 在范数 $\|\cdot\|$ 的意义下成立。$\square$

<span style="color:#2471a3;">**[note]**</span> <span style="color:#1e8449;">类似地，函数极限（function limit）也可以用另一种范数来表述。</span>

<span style="color:#2471a3;">**[lemma]**</span> <span style="color:#c0392b;">**引理 11.35**</span>：

设 $E \subset \mathbb{R}^n$，$f: E \to \mathbb{R}^m$。
设 $x_0 = (x_1, \ldots, x_n)$ 是 $E$ 的一个聚点（limit point），
并设 $y_0 = (y_1, \ldots, y_m) \in \mathbb{R}^m$。则

```math
\lim_{x \to x_0} f(x) = y_0
```

当且仅当对一切 $\varepsilon > 0$，存在 $\delta > 0$，
使得只要 $0 < \|x - x_0\|_\infty < \delta$ 且 $x \in E$，
就有 $\|f(x) - y_0\|_\infty < \varepsilon$。

我们把证明留作习题 11.6.5。

<span style="color:#2471a3;">**[section]**</span> §11.6.2 坐标式收敛（Coordinate-Wise Convergence），续。

作为前面论述的一个应用，我们将证明：
从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的映射的收敛（convergence）
可归结为按坐标（coordinate-wise）的收敛。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**定理 11.36**</span>：

设 $E \subset \mathbb{R}^n$，$f: E \to \mathbb{R}^m$，$f = (f^1, \ldots, f^m)$。
设 $x_0 = (x_1, \ldots, x_n)$ 是 $E$ 的一个聚点，
并设 $y_0 = (y_1, \ldots, y_m) \in \mathbb{R}^m$。

则 $\lim_{x \to x_0} f(x) = y_0$ 当且仅当
对一切 $j = 1, \ldots, m$ 都有
$\lim_{x \to x_0} f^j(x) = y_j$。

<span style="color:#2471a3;">**[proof]**</span> <span style="color:#c0392b;">**证明 Proof**</span>

本证明可由引理 11.35 与下面这个观察立即得出：
对任意 $p \in \mathbb{N}$ 与任意向量 $z = (z_1, \ldots, z_p) \in \mathbb{R}^p$，
对一切 $i = 1, \ldots, p$ 都有 $|z_i| \leq \|z\|$，
从而 $\|z - z_0\|_\infty \to 0$ 等价于
对一切 $i = 1, \ldots, p$ 都有 $z_i \to z_{0i}$。

因此，例如

```math
\lim_{x \to x_0} \|f(x) - y_0\|_\infty = 0
```

等价于对一切 $j = 1, \ldots, m$ 都有

```math
\lim_{x \to x_0} |f^j(x) - y_j| = 0.
```

$\square$

<span style="color:#2471a3;">**[note]**</span> <span style="color:#1e8449;">习题 11.2.6、11.2.7、11.3.8 与 11.4.1 都与比较 $\mathbb{R}^n$ 上的几种范数有关。

这些习题实质上表明：在讨论与开集（open set）及收敛直接相关的概念时，
范数 $\|\cdot\|$、$\|\cdot\|_1$ 与 $\|\cdot\|_\infty$ 可以互换使用。</span>

<span style="color:#7f8c8d">*（本页其余部分为 §11.6 习题区，含习题 11.6.4–11.6.5，按约定跳过。）*</span>

# <span style="color:#c0392b;">书页 458 — §11.6 代数性质：定理 11.37、定理 11.38 与 §11.7 连续函数开端（定义 11.39）</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定义 11.39 与一元第 5 章的定义只差一个记号：绝对值 $|x-x_0|$ 换成范数 $\|x-x_0\|$，其余逐字相同。这个"只换范数"的动作正是本章的方法论宣言——凡是一元里只用绝对值本质（三角不等式）就能证的东西，升到 $\mathbb{R}^n$ 只需机械替换。紧接着教材指出"孤立点处函数自动连续"，值得单独想想：若 $x_0\in E$ 不是聚点，就存在 $\delta_0$ 使球 $B(x_0,\delta_0)$ 里没有 $E$ 的其他点，此时对任何 $\varepsilon$ 取 $\delta=\delta_0$ 即满足定义——这是空真（vacuously true）命题，与 CSAPP 里"对空输入任何行为都不算错误"的逻辑同构。连续性还有两个等价刻画：$\lim_{x\to x_0}f(x)=f(x_0)$（极限刻画，要求 $x_0$ 是聚点）与序列刻画（$x_k\to x_0 \Rightarrow f(x_k)\to f(x_0)$）。三句话描述同一件事——"$E$ 中靠近 $x_0$ 的点都被映到靠近 $f(x_0)$ 的点"——分别适合不同场景：$\varepsilon$-$\delta$ 用于理论、序列用于反证、邻域用于拓扑推广。

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定理 11.37-11.38 回答一个设计问题：到底哪些代数运算能和极限交换顺序？答案藏在"运算本身要连续"里——加法、数乘、点积都是连续运算（§11.7 会正式证明），所以 $\lim(f+g)=\lim f+\lim g$ 成立。这正是 1821 年 Cauchy《分析教程》首次系统陈述的极限代数法则，他把"极限穿过四则运算"当作分析算术化的基石，两百年来支撑着几乎所有极限计算。注意乘积法则只能以"点积"形式出现（定理 11.38）而非逐分量相乘：两个向量没有天然的"逐分量乘积"语义，$f\cdot g$ 才是 $\mathbb{R}^m$ 里继承自一元乘积的自然推广。定理 11.38 的证明值得品味：先用引理 11.30 把函数极限降维成序列极限，再引用定理 11.16(iii) 一步到位——先降维、再套旧定理，是最干净的证明工程学，和你 CSAPP 里"复用已验证的底层模块搭建上层"是同一套分层哲学。

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定理 11.37 与 11.38 把第 5 章 5.2.3 节的极限代数性质（和的极限 = 极限的和，数乘、点积同理）原样搬到向量值函数。这并非理所当然，而是因为加法、数乘、点积都是「连续运算」——§11.7 会看到，正是这种连续性保证了「极限与运算可交换顺序」。证明路线是「序列化归约」：定理 11.38 先用引理 11.30 把函数极限翻译成序列极限，再用定理 11.16(iii)（序列点积的极限 = 极限的点积）一步到位——脏活都被提前的引理干掉了，这就是「分层抽象」的威力，与你在 CSAPP 中把复杂系统按层级模块化的习惯完全同构。注意定理 11.37 只对加法与数乘成立，乘积法则必须以点积（而非分量相乘）的形式出现：因为两个向量值的分量乘积没有自然的「向量」含义，这正是 $\mathbb{R}^n$ 与 $\mathbb{R}$ 的本质差异之一。Rudin 第 4 章会以「极限的线性性」统一表述这一切，届时回看这两条定理会有「一以贯之」的痛快感。

<span style="color:#2471a3;">**[section]**</span> §11.6 代数性质（Algebraic Properties）。

定理 11.36 的一个直接推论（immediate consequence）是：
我们在 5.2.3 节为单实变量的实值函数（real functions of one real variable）
所建立的若干极限的代数性质（algebraic properties），
在我们当前的设定（setting）下依然成立。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**定理 11.37**</span>：

假设 $E \subset \mathbb{R}^n$，
$f: E \to \mathbb{R}^m$，$g: E \to \mathbb{R}^m$，
$\alpha \in \mathbb{R}$，且 $x_0$ 是 $E$ 的一个聚点（accumulation point）。
若 $\lim_{x \to x_0} f(x) = y_0$ 且 $\lim_{x \to x_0} g(x) = z_0$，则

1. $\lim_{x \to x_0} (f(x) + g(x)) = y_0 + z_0$，且
2. $\lim_{x \to x_0} \alpha f(x) = \alpha y_0$。

我们把证明留作习题。

<span style="color:#2471a3;">**[note]**</span> <span style="color:#1e8449;">关于乘积（product），对点积（dot product）而言，
预期的乘积法则（product rule）是成立的。</span>

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**定理 11.38**</span>：

设 $E \subset \mathbb{R}^n$，设 $x_0$ 是 $E$ 的一个聚点，
并设 $f, g: E \to \mathbb{R}^m$。若

```math
\lim_{x \to x_0} f(x) = y_0 \quad \text{且} \quad \lim_{x \to x_0} g(x) = z_0,
```

则

```math
\lim_{x \to x_0} (f(x) \cdot g(x)) = y_0 \cdot z_0.
```

<span style="color:#2471a3;">**[proof]**</span> <span style="color:#c0392b;">**证明 Proof**</span>

我们应用引理 11.30。
设 $x_k \to x_0$，$x_k \in E$，$x_k \neq x_0$。
对 $k \in \mathbb{N}$，令 $u_k = f(x_k)$，$v_k = g(x_k)$。
则 $u_k \to y_0$，$v_k \to z_0$，
于是由定理 11.16(iii) 得 $u_k \cdot v_k \to y_0 \cdot z_0$。$\square$

<span style="color:#7f8c8d">*（本页中间部分为 §11.6 习题区，含习题 11.6.6–11.6.7，按约定跳过。）*</span>

# <span style="color:#c0392b;">§11.7 从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的函数的连续性（Continuity of Functions from $\mathbb{R}^n$ to $\mathbb{R}^m$）</span>

既然我们已经有了向量值函数（vector-valued function）的极限概念，
就可以像 5.4.2 节对实值函数（real functions）所做的那样，
引入连续（continuity）的概念。

本节中的证明与单变量情形下的对应证明几乎完全一致，
因此我们将这些证明略去。

<span style="color:#2471a3;">**[definition]**</span> **定义 11.39**：

设 $E \subset \mathbb{R}^n$，$f: E \to \mathbb{R}^m$，$x_0 \in E$。

<span style="color:#00838f;">我们说 $f$ 在 $x_0$ 处连续（continuous at $x_0$），
如果对每个 $\varepsilon > 0$ 都存在 $\delta > 0$，
使得对所有满足 $\|x - x_0\| < \delta$ 的 $x \in E$，
都有 $\|f(x) - f(x_0)\| < \varepsilon$。</span>


<!-- ===== W12 ===== -->

# <span style="color:#c0392b;">书页 459 — §11.7 从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的函数的连续性（续）：等价刻画、定义 11.40、定理 11.41 与例 11.42</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 例 11.42 是全书最重要的反直觉警示：$f(x,y)=2xy/(x^2+y^2)$ 对每个固定 $x$ 是关于 $y$ 的连续函数，对每个固定 $y$ 也是关于 $x$ 的连续函数，但 $f$ 作为二元函数在 $(0,0)$ 根本不连续（例 11.32 已证极限不存在）。这对第 12 章是致命预告：如果"偏导数存在"就能推出连续，那这个 $f$ 在原点两个偏导都存在（沿坐标轴 $f$ 恒为 0，偏导都是 0）却照样不连续——说明"逐变量可导"远弱于"可微"。你的直觉陷阱（卡点）在于误以为"分别固定每个变量都连续"就像"每条路都好走"，但多元里路径有无穷多条，坐标方向只是其中两条（$y=0$ 与 $x=0$），沿 $y=x$ 这条斜路就翻车。第 12 章可微性定义会要求"联合"的线性逼近成立（不只是每条坐标方向的差商），正是为了排除这类病态函数。Rudin 第 9 章用 $C^1$（偏导存在且连续）这个更强的条件修复漏洞，届时你会看到完整的因果链。

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定理 11.41 是本章最深刻的转折点：连续 ⇔ 开集的原像还是开集。注意方向是"原像"不是"像"——连续映射不一定把开集映成开集（常数映射把开集映成单点），但一定把开集的原像拉回成开集。为什么这值得欢呼？因为一旦接受它，"开集"就成了定义连续性的唯一原料：你可以完全忘掉 $\varepsilon$-$\delta$ 和距离，只用"哪些集合是开集"来描述整个分析。这正是 1906 年 Fréchet 的度量空间思想（距离定义开集、开集定义连续）的终极形态——1914 年 Hausdorff 进一步把"开集"本身当作公理，拓扑学就此诞生。对你来说这像 CSAPP 里的接口抽象：底层换实现（换范数、换度量），上层行为（连续性）不变。作为脚手架：把 $f$ 想成"把 $x$ 坐标发往 $y$ 坐标的转换器"，开集 $V$ 是 $y$ 侧的"允许集合"，$f^{-1}(V)$ 问的是"哪些 $x$ 会落进 $V$ 里"——连续就是说这个反向查询永远把"好的集合"映射回"好的集合"。

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定义 11.40 把"每点连续"打包成"在 $E$ 上连续"，但这里埋着一个精妙的陷阱：每点连续只保证"对每个 $x$ 存在各自的 $\delta_x$"，而 $\delta_x$ 可以随 $x$ 剧烈变化——这正是下一节一致连续要收紧的地方。用一阶逻辑看，逐点连续是 $\forall\varepsilon\,\forall x\,\exists\delta$（$\delta$ 可依赖 $x$），一致连续是 $\forall\varepsilon\,\exists\delta\,\forall x$（同一个 $\delta$ 全局通行），交换 $\forall x$ 与 $\exists\delta$ 的顺序就是两概念的全部差异。这与你在第 9 章学过的逐点收敛 vs 一致收敛是同一个量化词结构：$N$ 可依赖 $x$，还是统一取一个。事实上这对"逐点/一致"对偶会在整个分析学反复出现（连续性、收敛性、可微性），学会用"谁在 $\exists$ 里面"来判断强度，是你读证明最快的解码器。Rudin 第 4 章会把这套对应关系讲透，届时回看这里会有"一以贯之"的痛快感。

---

承接上一页的定义 11.39，我们继续展开对连续性的讨论。

<span style="color:#2471a3;">**[section]**</span>
# §11.7 从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的函数的连续性（Continuity of Functions from $\mathbb{R}^n$ to $\mathbb{R}^m$），续

注意到：按照定义 11.39，每个函数 $f$ 在 $E$ 的每个孤立点（isolated point）处都是连续的；

这里孤立点指的是 $E$ 中那些不是 $E$ 的聚点（limit point，极限点）的点。

对 $E$ 的聚点 $x_0$ 而言，容易看出 $f$ 在 $x_0$ 处连续，当且仅当

```math
\lim_{x \to x_0} f(x) = f(x_0).
```

由于引理 11.30，我们也立即得到一个用序列（sequence）表述的连续性定义：
$f$ 在 $x_0$ 处连续，当且仅当对每个收敛到 $x_0$ 的序列 $\{x_k\}$（其中 $x_k \in E$），都有

```math
\lim_{k \to \infty} f(x_k) = f(x_0).
```

换用邻域（neighborhood）的语言，我们发现：

只要对 $f(x_0)$ 的每个邻域 $V$，都存在 $x_0$ 的某个邻域 $U$，使得 $f(U \cap E) \subset V$，则 $f$ 在 $x_0$ 处连续。

简言之，上面给出的所有这些连续性定义都是等价的，

它们以精确的语言表达了同一层意思：$E$ 中所有靠近 $x_0$ 的点，都被 $f$ 映射为 $\mathbb{R}^m$ 中靠近 $f(x_0)$ 的点。

<span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f;">**定义 11.40（Definition 11.40）：**</span>设 $E \subset \mathbb{R}^n$，并设 $f : E \to \mathbb{R}^m$。

若 $f$ 在 $E$ 的所有点处都连续，我们就说 $f$ 在 $E$ 上连续（continuous on $E$）。

当 $E$ 可由上下文推出时，我们就简称为 $f$ 连续。

与一元实函数在 $\mathbb{R}$ 的子集上成立的定理 5.37 相类似，这里也有一个连续性的整体刻画（global characterization）可用。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**定理 11.41（Theorem 11.41）：**</span>设 $E \subset \mathbb{R}^n$，并设 $f : E \to \mathbb{R}^m$。

则 $f$（在 $E$ 上）连续，当且仅当对每个开集（open set）$V \subset \mathbb{R}^m$，集合

```math
f^{-1}(V) = \{x \in E : f(x) \in V\}
```

都是（相对于 $E$ 的）开集。

【这意味着 $f^{-1}(V)$ 是 $E$ 与 $\mathbb{R}^n$ 的某个开子集的交集。】

特别地，若 $E$ 是开集，则 $f$ 连续，当且仅当对每个开集 $V \subset \mathbb{R}^m$，集合 $f^{-1}(V)$ 在 $\mathbb{R}^n$ 中都是开集。

关于函数的和、数乘（scalar multiplication）与点积（dot product）的那些预期的连续性运算规则，对向量值函数（vector-valued function）依然成立；

它们的证明无非是援引定理 11.37 与 11.38 中相应的极限法则（limit law）而已。

由定理 11.36 我们推知：向量值函数 $f$ 在点 $x_0$ 处连续，当且仅当它的所有坐标函数（coordinate function）$f^i$ 在 $x_0$ 处都是连续的实值函数。

这一结论不应与下面这个错误的说法相混淆：

一个多元实值函数若"对每个变量分别连续（continuous in each variable separately）"，则它连续。

<span style="color:#2471a3;">**[example]**</span> **例 11.42（Example 11.42）：**再次考虑例 11.32 中的函数

```math
f(x, y) = \frac{2xy}{x^2 + y^2}, \qquad f(0, 0) = 0.
```

对每个固定的 $x = x_0$，$f(x_0, \cdot)$ 在 $\mathbb{R}$ 上连续。

对函数 $f(\cdot, y_0) : \mathbb{R} \to \mathbb{R}$，也有同样的结论。

但 $f$ 在 $(0, 0)$ 处并不连续，因为极限

```math
\lim_{(x, y) \to (0, 0)} f(x, y)
```

并不存在。

另见习题 11.7.12 与 11.7.13。

（本页末尾的记号 $J$ 为原书的排版符号。）

# <span style="color:#c0392b;">书页 460 — §11.7 习题区</span>

<span style="color:#7f8c8d">*（本页为 §11.7 习题区，含习题 11.7.1–11.7.13，按约定跳过。其中 11.7.1 要求证明各连续性定义等价，11.7.3 要求证明定理 11.41，11.7.13 辨析"逐变量连续则连续"这一错误命题的证明。）*</span>


<!-- ===== W13 ===== -->

# <span style="color:#c0392b;">书页 461 — §11.8 紧致集：引言、定义 11.43、定理 11.44 及其证明</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定理 11.44（$\mathbb{R}^n$ 中紧致 ⇔ 闭且有界）的名字是 Heine-Borel 定理，但历史比名字曲折得多。1852 年 Dirichlet 在柏林讲义里证明"闭区间上连续函数一致连续"时，已隐式用到"开覆盖有有限子覆盖"的性质；1872 年 Heine 发表同一证明却未提及 Dirichlet；1895 年 Borel 首次以定理形式陈述（限于可数覆盖），Cousin、Lebesgue（1898）、Schoenflies 随后推广到任意覆盖——所以叫"Heine-Borel"其实两头都不完全准确。定理 11.44 的证明把两个条件的分工讲得极清楚："有界"调用 Bolzano-Weierstrass 保证子列收敛（序列逃不出去），"闭"保证子列极限落在集合内（终点不被截断）——一个管"存在收敛"，一个管"极限归属"。反方向更有味道：若 $E$ 不闭，就有序列收敛到集外的聚点，所有子列都跟着跑到外面；若 $E$ 无界，就能构造 $\|x_k\|\ge k$ 的序列，任何子列都不可能收敛。理解"闭"与"有界"的分工，比背结论值钱一百倍。

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定义 11.43 值得先问一个设计问题：为什么 TBB 用"每个序列都有收敛子序列"定义紧致，而不用开覆盖？答案在书页 461 开头就交代了——因为 Bolzano-Weierstrass 定理（定理 11.19）已到手，序列工具在 $\mathbb{R}^n$ 里最趁手。历史上正是如此：Fréchet 1906 年推广 Bolzano-Weierstrass 定理到函数空间时引入的就是序列版本（sequential compactness），而"任意开覆盖有有限子覆盖"的版本要等 1920 年代 Alexandrov 与 Urysohn 才定型。有趣的是两种定义在度量空间（含 $\mathbb{R}^n$）里完全等价，在一般拓扑空间里却会分道扬镳——你未来学拓扑时这是"等价性退化"的经典案例。作为脚手架：紧致性是"有限集性质"的无穷版——有限集里任何序列必有一个值重复无穷多次（6.042J 抽屉原理），紧致集则保证任何序列至少有个收敛子列，二者都让"无穷中的收敛"免于失控。🎥 *Rodriguez 在 18.100B 视频中用开覆盖定义紧致*："And we say that A is compact if for every open cover of A there is a finite subcover."（翻译：我们说集合 A 是紧致的，是指 A 的每个开覆盖都存在一个有限子覆盖。）

---

<span style="color:#7f8c8d">*（本页开头为 §11.7 末道习题的收尾，含 (a)(b)(c) 三问，讨论「f 在 $\mathbb{R}^2$ 上分别对每个变量连续」时累次极限 $\lim_{x \to x_0}\lim_{y \to y_0} f(x, y)$ 与 $\lim_{y \to y_0}\lim_{x \to x_0} f(x, y)$ 的存在性及其与二重极限 $\lim_{(x,y) \to (x_0,y_0)} f(x, y)$ 的关系，属习题区，按约定跳过。）*</span>

<span style="color:#2471a3;">**[section]**</span> §11.8 紧致集（Compact Sets in $\mathbb{R}^n$）

在第 4.5 节中，我们为 $\mathbb{R}$ 的子集引入了
compactness（紧致性）这一重要概念。

本节我们将这一概念推广到 $\mathbb{R}^n$ 的子集。

我们将在下一节看到，定义在 $\mathbb{R}$ 的紧致子集上的
continuous functions（连续函数）所具有的那些性质，
同样可以推广到定义在 $\mathbb{R}^n$ 的紧致子集上的连续函数。

在 $\mathbb{R}^n$ 的框架下，我们可以为「compact set（紧致集）」
给出许多等价的定义。

（在第 4.5 节我们曾看到，$\mathbb{R}$ 中的一个集合
当且仅当它是 closed（闭的）且 bounded（有界的）、
或具有 Bolzano-Weierstrass 性质（property）、
或具有 Heine-Borel 性质时，才是紧致的。）

由于我们已经得到了 Bolzano-Weierstrass 定理（定理 11.19），
很自然地可以基于 sequence（序列）的概念来建立我们的定义。

<span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f;">**定义 11.43（Definition 11.43）：**</span>一个集合 $E \subset \mathbb{R}^n$ 称为紧致的，
如果 $E$ 中的每一个序列都有一个
收敛的（convergent）子序列（subsequence），
且该子序列的极限（limit）位于 $E$ 中。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**定理 11.44（Theorem 11.44）**</span>：一个集合 $E \subset \mathbb{R}^n$ 是紧致的，
当且仅当 $E$ 是闭且有界的。

<span style="color:#2471a3;">**[proof]**</span> <span style="color:#c0392b;">**证明 Proof**</span>

设 $E$ 是闭且有界的，且 $\{x_k\}$ 是 $E$ 中点的序列。

由于 $E$ 有界，由第 11.4 节的定理 11.19，
$\{x_k\}$ 有一个收敛的子序列 $\{x_{k_j}\}$。

令 $x_0 = \lim_{j \to \infty} x_{k_j}$，
则 $x_0$ 是 $E$ 的一个极限点（limit point）。

由于 $E$ 是闭集，故 $x_0 \in E$（由习题 11.3.1）。

反之，设 $E$ 是紧致的，
我们用反证法（contradiction）证明 $E$ 是闭且有界的。

若 $E$ 不是闭集，则 $E$ 有一个聚点 $x_0 \notin E$。

这意味着存在 $E$ 中的序列 $\{x_k\}$ 收敛到 $x_0$。

该序列的每一个子序列也都收敛到 $x_0$，
因此 $\{x_k\}$ 不存在收敛到 $E$ 中某点的子序列。

故 $E$ 必为闭集。

若 $E$ 无界，则存在 $E$ 中的序列 $\{x_k\}$，
使得对所有 $k \in \mathbb{N}$ 都有 $\|x_k\| \geq k$。

这个序列没有收敛的子序列，故 $E$ 必有界。$\square$

# <span style="color:#c0392b;">书页 462 — 推论 11.45、§11.9 紧致集上的连续函数：定理 11.46、推论 11.47 及其证明</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 推论 11.47 就是大名鼎鼎的极值定理（Extreme Value Theorem）：紧致集上的连续实值函数必取得最大值与最小值。它由 Weierstrass 在 1860 年代的柏林讲义中证明并系统传播（1877 年正式发表），一维版本可上溯到 Bolzano 1817 年——为了证明介值定理，他被迫先确立"连续函数在有界闭区间上取到最值"。🎥 *Rodriguez 在视频中强调*："This means in particular that the maximum and the minimum is achieved. It also means that the function is actually bounded on that interval."（翻译：这特别意味着最大值和最小值都被取到了，也意味着函数在该区间上确实有界。）证明链条很优雅：定理 11.46 先让 $f(E)$ 成为紧致集，定理 11.44 再说它闭且有界，闭集保证 $\sup$ 与 $\inf$ 落在集合内，于是 $c,d\in f(E)$。对你日后学 Boyd 凸优化和数值方法，这是"存在性"的黄金保证：只要目标连续、可行域紧致，最优解一定存在——不用算出来也知道它在那里。

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定理 11.46 说"连续映射把紧致集映成紧致集"（$f(E)$ 紧致），这是"连续映射保持结构"的第一个实例，也是你理解"态射"概念的最小样本：数学里"好的映射"就是把源对象的性质遗传给像对象的映射——就像 6.042J 里图同构保持顶点度数、群同态保持运算结构一样，连续映射保持紧致性。证明是典型的"序列搬运"：把 $f(E)$ 里的任意序列拉回成 $E$ 里的序列（选 $x_k$ 使 $f(x_k)=y_k$），在 $E$ 里抽收敛子列（紧致性），再用连续性把收敛性"推"回 $f(E)$。注意这里甚至不需要 $f$ 一一对应——任选一个前像就够用，这是连续映射比同构宽松得多的地方。推论：紧致性是拓扑不变量——同胚的空间要么都紧致、要么都不紧致。这为你第 13 章在度量空间/函数空间里追问"哪些性质在连续像下存活"埋下第一块砖。

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 推论 11.45 把紧致性换成一句更"集合论"的说法：闭且有界 ⇔ 每个无穷子集都有聚点。这正是 Bolzano-Weierstrass 定理的另一种表述——把"序列有收敛子列"翻译成"无穷点集必堆积出一处聚点"，与你在 6.042J 里熟悉的抽屉原理是同一思想的两个化身：无穷多个点塞进有限空间，必有一处"拥挤"。证明只需从无穷子集里挑出一个互异的序列，用定义 11.43 的紧致性抽出收敛子列，其极限就是聚点。这里"无穷"是关键限定：有限子集自然不保证聚点，但它也不需要聚点——聚点是为"极限过程"服务的，有限集合根本没有极限过程可谈。反过来，这条推论给了你一个判定紧致性的廉价工具：想证 $E$ 紧致，只需检查"任何无穷多个点是否必然挤出一处属于 $E$ 的极限"。Rudin 第 2 章习题常用此版本做桥接，下次看到"无限子集必有极限点"要立刻联想到紧致性。

---

<span style="color:#2471a3;">**[corollary]**</span> <span style="color:#c0392b;">**推论 11.45（Corollary 11.45）**</span>：一个集合 $E \subset \mathbb{R}^n$ 是闭且有界的，
当且仅当 $E$ 的每一个无穷子集（infinite subset）
都有一个属于 $E$ 的聚点（point of accumulation）。

该推论的证明可由定理 11.44 立即推出。

Heine-Borel 定理（Heine-Borel Theorem）同样可以推广到 $\mathbb{R}^n$。

我们把这部分内容留作习题 11.8.2。

<span style="color:#7f8c8d">*（本页 §11.8 习题区按约定跳过：习题 11.8.1 要求证明推论 11.45；习题 11.8.2 要求为 $\mathbb{R}^n$ 的子集给出「开覆盖（open cover）」与「Heine-Borel 性质」的定义，使它们与第 4.5.4 节的一维版本一致，并叙述、证明定理 4.33 在 $\mathbb{R}^n$ 子集上的类比。）*</span>

<span style="color:#2471a3;">**[section]**</span> §11.9 紧致集上的连续函数（Continuous Functions on Compact Sets）

现在我们转而讨论定义在 $\mathbb{R}^n$ 的紧致集上的
连续函数的行为（behavior）。

定义在 $\mathbb{R}$ 的紧致子集上的每一个连续的实值函数
都具有三个基本性质：

函数的 range（值域）是有界的；
函数能取到它的最大值（maximum）与最小值（minimum）；
以及连续性是一致的（uniform）。

这三个性质中的每一个都能推广到
向量值函数（vector-valued functions），
几乎不增加什么复杂性。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**定理 11.46（Theorem 11.46）**</span>：若 $E \subset \mathbb{R}^n$ 是紧致的，
且 $f: E \to \mathbb{R}^m$ 在 $E$ 上连续，
则集合 $f(E)$ 是紧致的。

<span style="color:#2471a3;">**[proof]**</span> <span style="color:#c0392b;">**证明 Proof**</span>

设 $\{y_k\}$ 是集合 $f(E)$ 中的一个序列。

我们证明 $\{y_k\}$ 有一个收敛的子序列，且其极限位于 $f(E)$ 中。

对每个 $k \in \mathbb{N}$，存在 $x_k \in E$ 使得 $f(x_k) = y_k$。

由于 $E$ 是紧致的，序列 $\{x_k\}$ 有一个收敛的子序列
$\{x_{k_j}\}$，它收敛到某点 $x_0 \in E$。

由于 $f$ 在 $x_0$ 处连续，
故 $f(x_0) = \lim_{j \to \infty} f(x_{k_j})$；
又因 $x_0 \in E$，所以 $f(x_0) \in f(E)$。

于是序列 $\{y_{k_j}\} = \{f(x_{k_j})\}$
就是 $\{y_k\}$ 的一个收敛子序列，
它收敛到点 $f(x_0) \in f(E)$。$\square$

<span style="color:#2471a3;">**[corollary]**</span> <span style="color:#c0392b;">**推论 11.47（Corollary 11.47）**</span>：设 $E \subset \mathbb{R}^n$ 是紧致的，
且 $f: E \to \mathbb{R}$ 连续。

则 $f$ 在 $E$ 上取得绝对最大值（absolute maximum）
与绝对最小值（absolute minimum）。

<span style="color:#2471a3;">**[proof]**</span> <span style="color:#c0392b;">**证明 Proof**</span>

由定理 11.46，集合 $f(E)$ 是 $\mathbb{R}$ 的一个紧致子集。

再由定理 11.44，$f(E)$ 是闭且有界的。

设 $[c, d]$ 是包含 $f(E)$ 的最小闭区间（smallest closed interval）。

由于 $f(E)$ 有界，这样的区间是存在的。

因为 $f(E)$ 是闭集，故 $c \in f(E)$ 且 $d \in f(E)$。

数 $c$ 就是 $f$ 在 $E$ 上的绝对最小值，
数 $d$ 就是 $f$ 在 $E$ 上的绝对最大值。$\square$


<!-- ===== W14 ===== -->

# <span style="color:#c0392b;">书页 463 — §11.9 收尾：一致连续（定义 11.48、定理 11.49）＋ §11.10 补充注记开篇</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 教材追问"三个不相交开集能否共有一条边界"，答案不仅存在，而且有正式名字：Wada 湖（Lakes of Wada）。1917 年日本数学家米山国藏（Kunizo Yoneyama）在导师和田武雄（Takeo Wada）启发下构造出三个两两不相交的连通开集，它们共享同一条边界；这条公共边界是"连通的却不含任何弧"的怪物——连通得比任何曲线都"抱团"，却又细碎到不含任何一段弧。构造算法本身极富教学价值：在单位正方形里轮流开挖蓝/红/绿三条运河，第 $n$ 天让第 $n \bmod 3$ 号湖逼近到所有剩余陆地 $1/n$ 以内，无限天后三条湖各自连通、共享同一边界——教科书级的"无限迭代取极限"例证，与 Cantor 集（Cantor 1883 年引入，Smith 1875 年已构造）是同一血统的病态构造。注意教材脚注 1 引的 Hubbard《强迫阻尼摆》正是这一现象的动力学版本：混沌系统里三个吸引盆共享边界（Wada 盆地），初值微小扰动可落入任意吸引子——CSAPP 里你体会过对初值极端敏感的浮点混沌，这里在纯拓扑层面重现了它。6.042J 里"平面曲线分隔平面"的约当曲线直觉在此被彻底打破。

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定理 11.49 是"紧致性最漂亮的酬劳"：紧致集上的连续函数自动一致连续，逐点的 $\delta$ 可以统一。它和第 9 章的 Dini 定理构成一对"紧致性双雄"：Dini 定理（1878 年 Ulisse Dini 在比萨出版的书中提出）说紧致集上单调收敛到连续函数的函数列，逐点收敛自动升级为一致收敛；这里说紧致集上连续函数自动一致连续——两处都是"紧致性把逐点性质升级为一致性质"。Dini 定理的证明核心正是"开覆盖 + 有限子覆盖"：让每个点的小邻域里 $f_n$ 与 $f$ 足够接近，紧致性保证有限个邻域盖住全空间，取最大 $N$ 即得一致收敛。可见"局部信息 → 有限覆盖 → 全局结论"是紧致性最深的用途，Borel-Lebesgue 有限子覆盖性质（§11.8 习题）就是它的引擎。Heine 1872 年发表的正是这条定理的一维版本。第 13 章你会看到这个模式反复出现（一致逼近、Arzelà-Ascoli 定理），现在打好"紧致性 = 有限性"的直觉，届时事半功倍。

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 一致连续与逐点连续的唯一差别是量化词顺序，我把它做成对照表方便刻进记忆：逐点连续是"先给 $\varepsilon$，再给点 $x$，最后找 $\delta(x,\varepsilon)$"（$\delta$ 依赖点），一致连续是"先给 $\varepsilon$，一口气找到一个全局 $\delta$，对所有 $x$ 通用"（$\delta$ 不依赖点）。一句话：一致连续保证"误差控制"在定义域上同步生效，逐点连续只保证"每个点附近"有效。这与你在第 9 章学过的逐点收敛 vs 一致收敛是完全相同的结构——那个 $N$ 可不可以不依赖 $x$，这个 $\delta$ 可不可以不依赖 $x$，本质是同一道题。为什么一致连续有用？因为只有同步的误差控制才能让"整体"操作（如积分、交换极限与运算）成立——Cauchy 当年证明连续函数可积时就卡在这里，他需要的正是均匀的 $\delta$。从 CSAPP 视角看，这像"单点优化"（每处各自微调）与"全局 worst-case 保证"（一个 $\delta$ 管所有）的区别，后者才是工程上可验证的质量承诺。

---

<span style="color:#2471a3;">**[section]**</span> §11.9 补充注记（Additional Remarks）——一致连续（Uniform Continuity）。

我们的一致连续（uniform continuity）定义，
把 §5.6 中的相应概念推广到了向量值函数（vector-valued functions）。

<span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f;">**定义 11.48（Definition 11.48）：**</span>设 $E \subset \mathbb{R}^n$，并设 $f : E \to \mathbb{R}^m$。

我们说 $f$（在 $E$ 上）一致连续（uniformly continuous），是指：

对每个 $\varepsilon > 0$，都存在 $\delta > 0$，

使得只要 $x, y \in E$ 且 $\|x - y\| < \delta$，

就有 $\|f(x) - f(y)\| < \varepsilon$。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**定理 11.49（Theorem 11.49）：**</span>若 $E \subset \mathbb{R}^n$ 是紧致集（compact set），

且 $f : E \to \mathbb{R}^m$ 在 $E$ 上连续（continuous），

则 $f$ 在 $E$ 上一致连续。

<span style="color:#2471a3;">**[proof]**</span> **证明（Proof）：**该证明与定理 5.48 的证明完全相同，

只需把其中的绝对值符号（absolute value signs）替换为范数（norm）即可。$\square$

<span style="color:#7f8c8d">*（本页其余部分为 §11.9 习题区，含习题 11.9.1–11.9.6，按约定跳过。）*</span>

<span style="color:#2471a3;">**[section]**</span> §11.10 补充注记（Additional Remarks）。

本小节属于拓展性小节（enrichment section），可以略去。

在本小节中，我们提到一些条目（items），

它们在下一章中不会被用到，但或许值得读者关注。

# <span style="color:#c0392b;">书页 464 — §11.10 补充注记（续）：$\mathbb{R}^n$ 中的开集与闭集、四色问题、叉积</span>

<span style="color:#2471a3;">**[section]**</span> §11.10 $\mathbb{R}^n$ 中的开集与闭集（On Open and Closed Sets in $\mathbb{R}^n$）。

我们在第 4 章看到，$\mathbb{R}$ 中的开集（open set）具有特别简单的结构。

$\mathbb{R}$ 的每个非空开子集，都可以表示为
有限个或可数无穷多个两两不相交（pairwise disjoint）开区间（open intervals）的并（定理 4.15）。

$\mathbb{R}$ 中的闭集（closed set）相对容易想象。

它们由区间、孤立点（isolated points）、
孤立点的极限点（limits of isolated points）等，以及 Cantor 集（Cantor sets）所构成。

相比之下，$\mathbb{R}^n$（$n \geq 2$）中的开集或闭集可能复杂得多。

例如，很容易想出一个闭集，
它是两个不相交开集的公共边界（common boundary）——一个圆周就能胜任。

把圆的内部与外部看作那两个不相交的开集。

你能否构造一个闭集，使其成为三个两两不相交开集的公共边界？

五个呢？无穷多个呢？

这类集合的构造并不容易，但它们确实存在，并且能以自然的方式出现。$^1$

那些开集必定是"蜿蜒曲折"（wiggly）的集合，

而它们的公共边界 $B$ 是连通的（connected，按定义 11.50 引入的意义理解），

然而 $B$ 却不包含任何弧（arc）！

你能想象出这样一个集合 $B$ 吗？

<span style="color:#2471a3;">**[section]**</span> 四色问题（The Four-Color Problem）。

这个著名的问题最终于 1976 年得到了肯定的解决，

此前一百多年间，许多数学家都曾徒劳地尝试求解它。

用松散（loose）的语言来说，四色问题最初于 1852 年提出，

它问的是：平面中任何地图（map）的各区域，
是否都能用不超过四种颜色着色，

使得凡是具有由多于一个点构成的公共边界的两个区域，都被涂上不同的颜色。

然而，1976 年最终宣布的该问题的解法至今仍存争议（controversial），

因为其证明需要数百页篇幅，以及数千小时的计算机验证（computer verification）。

我们前面对高维空间中集合边界的论述，

表明在陈述问题时保持精确（precise）是多么重要。

假设 $E_1, E_2, \ldots, E_5$ 是有公共边界 $B$ 的有界开集（bounded open sets），

那么给所得地图着色将需要五种颜色。

这将违反我们以松散方式陈述的四色定理。

当然，真正的四色定理是经过精心陈述的，

使得所允许的区域类型及其公共边界都受到适当限制。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 四色定理是你 6.042J 图论知识的完美接棒点：地图着色翻译成图论就是"平面图的色数 $\chi(G)\le 4$"，其中每个区域是顶点、共享边界段的区域连边。历史时间线值得记住：1852 年 Francis Guthrie 着色英格兰郡县地图时提出猜想；1879 年 Kempe 发表"证明"后被 Heawood 于 1890 年发现漏洞，但 Heawood 顺势修出了更弱的五色定理（$\chi\le 5$，证明简洁到高中竞赛水平）；1976 年 Appel 与 Haken 用计算机穷举 1482 个"不可约构型"完成证明，成为首个依赖计算机的重大数学定理，也因此引发"程序算不算证明"的世纪争论；1997 年 Robertson-Sanders-Seymour-Thomas 把构型精简到 633 个；2005 年 Gonthier 用 Coq 证明助手形式化验证整条证明链，争论才算告一段落。对你来说，这既是 6.042J 里平面图、欧拉公式、图着色的巅峰应用，也是 CSAPP 的延伸思考：计算机验证（Coq）如何把"枚举不可靠"变成"形式化可靠"。教材那段"5 个开集共边界就要 5 色"的讨论，正是提醒你：四色定理对区域形状有精确假设，松散陈述会撞上 Wada 湖这类病态反例。

<span style="color:#2471a3;">**[section]**</span> 叉积（Cross Products）。

我们已相当多地使用了 $\mathbb{R}^n$ 中两个向量的点积（dot product）$x \cdot y$。

对 $n = 3$ 这一特殊情形，还有另一种重要的积，
即叉积或向量积（cross product / vector product），记作 $x \times y$。

对任意两个向量 $x = (x_1, x_2, x_3)$ 与 $y = (y_1, y_2, y_3)$，我们定义

```math
x \times y = (x_2 y_3 - x_3 y_2, \ x_3 y_1 - x_1 y_3, \ x_1 y_2 - x_2 y_1).
```

叉积在数学与物理的许多分支中都十分重要。

在接下来的各章中我们不会用到它，因此这里不提供展开论述（development）。

我们只提一点：$x \times y$ 是一个垂直于（perpendicular）由 $x$ 与 $y$ 所确定的平面的向量。

<span style="color:#1e8449;">**[note]**</span> 原句在页边截断，此处补全其意，句子续于书页 465。

<span style="color:#1e8449;">**[note]**</span> 脚注 1：一份有趣而简短的讨论及原始文献，见 J. H. Hubbard
所著《The Forced Damped Pendulum: Chaos, Complication and Control》，
载于《Amer. Math. Monthly》106 卷 第 8 期（1999 年 10 月），第 741–758 页。

<span style="color:#1e8449;">**[note]**</span> 脚注 2：一本为普通读者撰写的有趣著作是《四色定理》（The Four Color Theorem），
作者为 R. and G. Fritsch（Springer-Verlag，1998 年）。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 叉积的历史是数学史上最著名的"灵感时刻"之一：1843 年 10 月 16 日，Hamilton 在都柏林散步至皇家运河上的 Brougham 桥时突然悟出四元数，当场把公式 $i^2=j^2=k^2=ijk=-1$ 刻在桥石上——叉积正是从四元数乘积的"向量部分"剥离出来的（两个纯四元数 $[0,u]$、$[0,v]$ 相乘得 $[-u\cdot v,\ u\times v]$，点积与叉积同时出现）。1880 年代 Gibbs 与 Heaviside 分别从四元数中提取出独立的"向量分析"，Wilson 1901 年的教材定型了今天的记法，从此点积+叉积成为物理与工程的标准工具。Strang 视角下叉积是"行列式的几何化"：$\|x\times y\|$ 恰是以 $x,y$ 为邻边的平行四边形面积，而 $x\times y$ 的三个分量分别是对应坐标平面上的 $2\times2$ 符号行列式（删去某坐标后）。教材只说"垂直于平面"，你可以自己验证 $x\cdot(x\times y)=y\cdot(x\times y)=0$——这正是 Strang 里"向量正交"的代数检验。注意叉积本质上只在 $\mathbb{R}^3$ 存在（除 $\mathbb{R}^0$、$\mathbb{R}^1$ 与源于八元数的 $\mathbb{R}^7$ 特例外，高维不再有类似的叉积，通常的推广是外积），这是它最容易被忽视的"维度怪癖"，也是它和点积最大的不对称之处。


<!-- ===== W15 ===== -->

# 第465页 · §11.10——连通性（Connectedness）与页顶叉积补充说明

<span style="color:#2471a3;">**[section]**</span> **Additional Remarks（补充说明）** ▸ 本页顶部承接上一页关于叉积的补充说明，在给出"连通性"定义之前先收尾了叉积（cross product）的相关几何性质。

在由向量 $x$ 与 $y$ 张成的平行四边形中，成立
```math
\|x \times y\| = \|x\|\,\|y\| \sin\theta ,
```
其中 $0 \leq \theta \leq \pi$ 是由 $x$ 与 $y$ 所决定的夹角（angle）。几何上（geometrically），$\|x \times y\|$ 正是以 $x$ 与 $y$ 为相邻两边（adjacent sides）的平行四边形的面积（area）。

---

<span style="color:#2471a3;">**[section]**</span> **Connectedness in $\mathbb{R}^n$（$\mathbb{R}^n$ 中的连通性）**

在习题 11.3.7 中，我们对 $\mathbb{R}^n$ 中的开集（open set）定义了连通性（connectedness）。一个 $\mathbb{R}^n$ 中的开集 $D$ 被称为连通，是指 $D$ 中任意两点都能被一条完全落在 $D$ 内部的多边形路径（polygonal path）所连接。

"连通性"这一概念捕捉到的直观想法，是集合"连成一片"（in one piece）的性质。那么对于那些并非开集的集合又该如何？一个闭圆盘（closed disk）、一个连续函数（continuous function）$f : \mathbb{R} \to \mathbb{R}$ 的图像（graph），以及集合
```math
A = \{\,(x,y) : x^2 \leq y \leq 2x^2\,\}
```
都是 $\mathbb{R}^2$ 的子集，它们虽非开集，却看起来确实连成一片。

上述那种基于多边形路径的定义，只适用于闭圆盘以及一部分——但并非全部——连续函数的图像。它并不适用于集合 $A$，因为不存在任何一条多边形路径能把原点（origin）连接到 $A$ 中的另一些点。下面给出 $\mathbb{R}^n$ 中一个更一般的连通性定义。

<span style="color:#2471a3;">**[definition]**</span> **定义 11.50**：设 $S \subset \mathbb{R}^n$。若存在两个不相交的开集（disjoint open sets）$U$ 与 $V$，使得 $S \subset U \cup V$，且 $S \cap U \neq \varnothing$、$S \cap V \neq \varnothing$，则称 $U$ 与 $V$ 分离（separate）$S$。集合 $S$ 被称为**连通**（connected），是指不存在任何开集 $U$、$V$ 能够分离 $S$。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定义 11.50 的连通性和你 6.042J 里图的连通性有本质差别：图的连通是"存在一条路径"（过程性、可构造），这里的拓扑连通是"不存在一种分离"（否定式、不可构造）——一个正着说、一个反着说。教材先给"多边形路径"版本（习题 11.3.7，只适用于开集），再用集合 $A=\{(x,y):x^2\le y\le 2x^2\}$ 说明它的局限：原点与 $A$ 中其他点之间没有任何多边形路径（曲线在原点有个越来越陡的尖，任何折线一出原点就滑出 $A$），但 $A$ 在拓扑意义下确实连通。这个例子的设计意图是逼出"不依赖路径"的更一般定义——分离版本正是这种"纯集合"语言。第一性原理地想：连通的本质是"不能把集合干净地劈成两半"，用两个不相交开集 $U,V$ 分离 $S$ 就是在问"能否用开集把 $S$ 切成两块"。这条定义还和第 9 章中间值定理暗中联手：连通集上的连续实值函数值域必是区间（习题 11.10.4），这正是"图像连成一片"的精确化身。

---

<span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定义 11.50 中"不存在任何开集 $U$、$V$ 能分离 $S$"这一否定式条件，其正面含义是：你无法把 $S$ 拆成两个被开集隔开的非空部分。用拓扑学（topology）的行话来说，这等价于"$S$ 不能分解为两个非空相对开（relatively open）子集之并"——所谓相对开，是指子集在 $S$ 继承而来的"相对拓扑"中看起来是开的（即它等于某个 $\mathbb{R}^n$ 开集与 $S$ 的交）。为什么用"开集包住两边"来刻画分离，而不直接用线段或路径？因为"连成一片"（connected）必须把曲折离散的集合也涵盖进来：闭圆盘、连续函数的图像乃至 §11.10 开头那个集合 $A = \{x^2 \le y \le 2x^2\}$ 都满足"无法被两个开集分离"，却未必存在把任意两点连起来的线段。这正是教材在前面提到的习题 11.3.7 多边形弧（polygonal arc）定义的局限——它只适用于开集，而这里的定义对任意集合都适用。还要注意，定义要求的是"开集 $U$、$V$"，不是随意两个子集：如果不是开集，那么任何非空集合 $S$ 总能被 $S$ 本身和空集拆开，定义就失去了意义。这也是"连通"这一概念最精妙的地方——它用外部空间的开集来探测集合内部的整体性，与你 6.042J 里用顶点不可分割性刻画图连通是同一思路，只不过分析学用"开集"取代了"路径"作为探测工具。

按照这一定义，前面提到的那些集合（闭圆盘、连续函数的图像以及集合 $A$）全都是连通的。至于更多例子，以及这一定义与先前针对开集给出的定义之间的一致性（consistency），请参见习题部分。

---

<span style="color:#7f8c8d">*（本页余下部分为 §11.10 习题区 Exercise 11.10.1–11.10.7，按约定跳过。题 11.10.1 要求证与习题 11.3.7 中开集连通性定义等价；11.10.2 验证三类集合连通；11.10.3 证连通集在连续映射下的像是连通的；11.10.4 阐述并证明连通集上连续实值函数的中值性质；11.10.5 讨论 $f$ 连续当且仅当图像闭且连通；11.10.6 证紧致连通集降序列的交连通并给反例；11.10.7 引用 Hubbard 论文观察公共边界，仅作查阅。这些题目本体均按约定整体跳过。）*</span>

---

# 第466页 · Notes（注释 262–274）

<span style="color:#2471a3;">**[note]**</span> **注释（Notes）** ▸ 本页为作者对前文各习题（Exercise）的提示性注释（hints），编号自 262 至 274，逐条给出解题线索或进一步说明。另含习题 11.10.8（验证叉积 $x \times y$ 的正交性等性质）的跳过标注。

<span style="color:#1e8449;">**[note]**</span> **262 · 习题 11.1.5**：关于中值性质（intermediate value property）的定义，参见定义 5.27。该节中的习题同样为回答本节这一问题提供了线索。

<span style="color:#1e8449;">**[note]**</span> **263 · 习题 11.1.6**：关于第（b）部分，参见习题 10.8.3。

<span style="color:#1e8449;">**[note]**</span> **264 · 习题 11.2.7**：你对（b）与（c）两部分的作答，恰好揭示了欧几里得范数（euclidean norm）的一个独特性质。该范数与点积（dot product）之间以若干有用的方式相互关联。本人在本章及下一章中对范数的使用并不依赖这层关联，因此在某些时刻使用 $\|\cdot\|_1$ 与 $\|\cdot\|_\infty$ 将会更为方便。关于这一主题在以无穷序列（infinite sequences）替代 $n$ 元组（$n$-tuples）的背景下更深入的讨论，参见第 13 章的例子 13.7、13.8 与 13.9。所谓赋范线性空间（normed linear space），就是任意带有满足定理 11.6 条件的范数的向量空间（vector space）。当该范数经由 $\|x\|^2 = x \cdot x$ 由某个点积导出时，此空间被称为 Hilbert 空间（Hilbert space），并享有许多特殊性质。

<span style="color:#1e8449;">**[note]**</span> **265 · 习题 11.2.8**：事实上，在 $\mathbb{R}^n$ 上唯一使得该恒等式成立的范数就是欧几里得范数。

<span style="color:#1e8449;">**[note]**</span> **266 · 习题 11.3.7**：关于一种不同于此处多边形弧（polygonal arc）定义、且适用于未必是开集的集合的连通性概念，参见 §11.10 中的讨论。

<span style="color:#1e8449;">**[note]**</span> **267 · 习题 11.3.8**：本题要点在于，既然开集完全相同，那么所有那些仅用开集即可完全定义其概念的其他性质也将完全一致。当我们在后续各节中讨论序列的收敛/极限（convergence of sequences or limits）、连续性（continuity）以及函数的可微性（differentiability）时，同样会成立这一事实。

<span style="color:#1e8449;">**[note]**</span> **268 · 习题 11.6.5**：请运用引理（Lemma）11.34 证明中的思想。

<span style="color:#1e8449;">**[note]**</span> **269 · 习题 11.7.11**：请使用习题 11.7.10。

<span style="color:#1e8449;">**[note]**</span> **270 · 习题 11.7.12**：证明 $\lim_{t\to 0} f(t, t^2) = 1$。

<span style="color:#1e8449;">**[note]**</span> **271 · 习题 11.7.13**：对于（a）部分，请结合习题 11.7.12 的例子来审视提纲。（b）部分的假设应当涉及某种恰当形式的"关于另一变量的均匀连续性（uniform continuity in one of the variables with respect to the other variable）"。对于（c）部分，§11.6 的例子 11.32 以及习题 11.7.12 说明，这并不蕴含二重极限（double limit）必然存在。

<span style="color:#1e8449;">**[note]**</span> **272 · 习题 11.8.2**：§13.12.3 在度量空间（metric spaces）这个更一般的背景下，建立了 Bolzano-Weierstrass 性质与 Heine-Borel 性质的等价性。

<span style="color:#1e8449;">**[note]**</span> **273 · 习题 11.9.4**：对于反例，你可以使用
```math
f(x) = (\cos x , \; \sin x) ,\qquad 0 \leq x < 2\pi .
```

<span style="color:#1e8449;">**[note]**</span> **274 · 习题 11.10.6**：令
```math
A_k = \{(0,0)\} \cup \{(1,0)\} \cup \Big\{\,(x,y) : 0 < y < \tfrac{1}{k}\,\Big\} .
```
该构造给出一个降序列，用以说明在去掉紧致性（compactness）假设后原命题不真。

---
<span style="color:#7f8c8d">▸ 本页（bp466）为习题提示性注释页，逐条按 Note 翻译如上。bp465 之 §11.10 正文与定义 11.50 均已完整翻译，习题区按约定跳过。</span>


<!-- ===== W16 ===== -->

# <span style="color:#c0392b;">第 12 章　$\mathbb{R}^n$ 上的微分（Differentiation on $\mathbb{R}^n$）</span>

*（本译本涵盖书页 467–468，即第 12 章开篇 §12.1 引言、§12.2 偏导数与方向导数开头部分，以及例 12.1 与图 12.1。以下为逐句行内双语翻译。）*

---

<span style="color:#2471a3;">**[section]**</span> ## 12.1　引言（Introduction）

我们假设你已经熟悉与多变量函数（functions of several variables）微分相关的各种概念。

这种熟悉应当包括对偏导数（partial derivatives）与方向导数（directional derivatives）的一定理解。

它还应包括了解这些导数在处理二元函数时用于获得切线（tangent lines）与切平面（tangent planes）所起的作用。

并且对用偏导数进行各种计算感到得心应手。

基础微积分的学生通常能够掌握与多变量函数微分相关的某些较简单的概念。

但他们在理解可微性（differentiability）的含义上可能会遇到更多困难——除了知道在 $n=2$ 时它意味着存在一个切平面之外。

与微分（differential）或各种链式法则（chain rules）相关的概念往往难以把握。

在本章中我们研究多变量函数微分相关的各种概念。

我们首先固定偏导数与方向导数的记号，然后以从容的方式着手讨论一系列主题。

当经验告诉我们学生觉得某个主题困难时，我们就专门用一节来"铺垫"这些材料，把证明留到下一节进行。

或者我们也可以先讨论特殊情况，把一般情形推迟到我们确信你对该主题感到自如为止。

一个典型的例子是微分。

如果你准备充分，就可以快速推进到第 12.8 节，匆匆浏览前面的大部分材料。

一种更加温和的方式，是利用前面的各节作为熟悉可微性、微分与链式法则这些概念的手段。

然后再去攻取从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的映射这一更抽象的情形。

我们已用星号标记了那一节，表明它可以省略。

因为它涉及一点线性代数，而前面各节只用到最少的线性代数（linear algebra）。

---

### <span style="color:#2471a3;">**[section]**</span> 12.2　偏导数与方向导数（Partial and Directional Derivatives）

对于二元函数 $f(x, y)$，在导数的研究上有一个显而易见的首次尝试。

我们这门学科的奠基人（Newton、Leibniz 及其它人）仅仅通过按照惯常的微积分规则对每个变量分别求导（treating each variable separately），就把微积分技巧推广到了这类函数。

这个例子及其记号应当是学生从更早的课程中就很熟悉的。

> *（书页 467 至此结束，续接书页 468 的图 12.1 与例 12.1。）*

---

<span style="color:#2471a3;">**[figure]**</span> 图 12.1（Figure 12.1）　对于函数 $f(x, y) = \tfrac{1}{3}\sqrt{\,36 - 4x^2 - y^2\,}$ 在点 $\left(1,\,3,\,\tfrac{\sqrt{23}}{3}\right)$ 处的切线（Tangent lines）。（图中 $x$、$y$、$z$ 轴如图所示。）

<span style="color:#2471a3;">**[example]**</span> 例 12.1（Example 12.1）：设 $f(x, y) = \big(\sqrt{36 - 4x^2 - y^2}\big)/3$。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 第 12 章开篇是给读者打预防针：Newton 与 Leibniz 当年把微积分"对每个变量分别求导"地推广到多元函数，偏导数就此诞生，但这条路走到头就是例 11.42 的陷阱——偏导数全部存在，函数仍可能不可微（例 11.42 的 $f$ 在原点两个偏导都等于 0，却不连续、更不可微）。这就是教材说的"可微性含义上的更多困难"：可微不是"每条坐标方向的差商存在"，而是"存在一个线性映射（Jacobian 矩阵 $J_f$）同时逼近所有方向"，即 $f(x_0+h)\approx f(x_0)+J_f h$ 的误差是 $o(\|h\|)$。用 Strang 的脚手架看：一元可微是"用直线（导数）逼近曲线"，多元可微是"用切平面（线性映射）逼近曲面"——偏导数只是这个线性映射沿坐标轴方向的作用（Jacobian 的第 $i$ 列是 $\partial f/\partial x_i$），就像矩阵的一列不能代表整个矩阵。例 12.1 的椭球面 $\frac13\sqrt{36-4x^2-y^2}$ 与图 12.1 的两条切线正是在展示：两个偏导数给出两个坐标平面里的切线，但"真正的可微"要求这两个方向的信息拼成一个连续的切平面。教材承诺后面会证明更强的 $C^1$ 条件（偏导连续）保证可微，那正是对例 11.42 漏洞的正式修复。

你可能认出这个表面对应的是半个椭球面（half of an ellipsoid）。

$f$ 的偏导数为

```math
\frac{\partial}{\partial x}f(x,y)=\frac{-4x}{3\sqrt{36-4x^2-y^2}}
\qquad\text{以及}\qquad
\frac{\partial}{\partial y}f(x,y)=\frac{-y}{3\sqrt{36-4x^2-y^2}}.
```

要更正式地表述这里正在发生的事情，可以与函数 $f(x)$ 导数的通常定义相比较：

```math
\frac{d}{dx}f(x)=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}.
```

此处对于 $f(x, y)$ 的过程，是执行同样的计算，但在整个过程中都把 $y$ 当作固定的常数来对待：

```math
\frac{\partial}{\partial x}f(x,y)=\lim_{h\to 0}\frac{f(x+h,\,y)-f(x,\,y)}{h},
```

随后再把 $x$ 当作固定的常数：

```math
\frac{\partial}{\partial y}f(x,y)=\lim_{h\to 0}\frac{f(x,\,y+h)-f(x,\,y)}{h}.
```

正是这条式子，我们将它采纳为二元函数的定义。

对于更多变量，推广方式是类似的。

当变量超过两三个时，我们倾向于采用下标记号（subscript notation）来代替 $\frac{\partial}{\partial x}$ 这种记号。

在点 $(x_0, y_0)$ 处的偏导数 $f_1 = \frac{\partial f}{\partial x}$ 与 $f_2 = \frac{\partial f}{\partial y}$，提供了曲面 $z = f(x, y)$ 上两条特定的切线（tangent lines）的斜率。

这两条直线分别位于平面 $x = x_0$ 与 $y = y_0$ 之中，经过点 $(x_0, y_0, z_0)$ 且与曲面相切。

图 12.1（Figure 12.1）显示了例 12.1 中函数在点 $(x_0, y_0, z_0) = \left(1,\,3,\,\tfrac{\sqrt{23}}{3}\right)$ 处的这些切线。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 函数 $f(x, y) = \tfrac{1}{3}\sqrt{36 - 4x^2 - y^2}$ 在 $(1, 3)$ 处的值为 $z = \tfrac{1}{3}\sqrt{36-4-9} = \tfrac{\sqrt{23}}{3} \approx 1.60$。原书图 12.1 的题注与正文在部分版本排版中写作 $23/3 \approx 7.67$，该数值并不落在曲面上，应理解为排版笔误；此处统一采用正确的 $\sqrt{23}/3$（与图 12.3、例 12.14 一致）。

这些为二元或更多元函数微分理论迈出的最初简单步伐，曾经很好地服务于微积分的先驱者们。

然而，正如我们将要看到的，要前进到更远的地方，就需要对微分做出更深入的考察。


<!-- ===== W17 ===== -->

# <span style="color:#c0392b;">书页 469 — §12.2 开篇：偏导数（Partial Derivatives）的定义与记号、二阶偏导数</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 偏导数的本质是一个"降维采样"动作：把 $f$ 的第 $i$ 个坐标松开、其余全部冻结，得到一条一元曲线再求斜率。这与 Strang 里"把矩阵按某一行/列切片来理解"是同一策略——多元对象信息量太大，切片是第一个可操作的抓手。但要记住例 11.42 的警告：偏导数只测坐标方向，两条坐标方向都正常，也可能掩盖斜方向的崩溃。历史上 Newton 的流数法（1665-66 年发明、1736 年出版）处理多变量变化率时已隐含"冻结其余变量"，但偏导数作为独立概念要到 Euler 1755 年《微分学原理》才系统化；记号 $\partial$ 由 Condorcet 1770 年首创、Legendre 1786 年用于偏导数、Jacobi 1841 年推广普及。二阶偏导最多 $n^2$ 个：因为下标 $(i,j)$ 是有序对，这正是 6.042J 里的"有放回排列"（从 $n$ 个坐标有序取两次）。$f_{12}$ 与 $f_{21}$ 这对"交叉偏导"被单列讨论，就是为定理 12.5 埋的引线。

---

<span style="color:#2471a3;">**[section]**</span> §12.2 偏导数与方向导数（Partial and Directional Derivatives）。

## 偏导数（Partial Derivatives）

设 $f : D \to \mathbb{R}$，其中 $D$ 是 $\mathbb{R}^n$ 的开子集（open subset）。

令 $x = (x_1, \ldots, x_n) \in D$。

如果我们允许 $x$ 的某个坐标（比如 $x_i$）变化，而其余坐标保持固定（fixed），

我们就得到一个关于单变量 $x_i$ 的函数，这个函数可记为

$f(x_1, x_2, \ldots, x_{i-1}, \cdot, x_{i+1}, \ldots, x_n)$。

(1)

第 $i$ 个位置上的圆点表示：$x_i$ 可以在约束条件之下变化，

即要求点 $(x_1, x_2, \ldots, x_{i-1}, x_i, x_{i+1}, \ldots, x_n)$ 属于 $D$。

如果函数 (1) 的导数（derivative）在 $x$ 处存在，

我们就得到 $f$ 关于 $x_i$ 在 $x$ 处的偏导数（partial derivative）。

我们将这个在 $x$ 处的偏导数记为 $f_i(x)$ 或 $f_i(x_1, \ldots, x_n)$。

于是有

```math
f_i(x) = \lim_{h \to 0} \frac{f(x_1, \ldots, x_i + h, \ldots, x_n) - f(x_1, \ldots, x_i, \ldots, x_n)}{h}.
```

(2)

<span style="color:#2471a3;">**[note]**</span> <span style="color:#1e8449;">注（Note）：</span>与普通导数（ordinary derivatives）的情形一样，这里也是不同记号各有各的用处，而且实际使用的记号相当多。

例如，$f_i(x)$ 常被记为 $\frac{\partial f}{\partial x_i}(x)$ 或 $f_{x_i}(x)$。

若写 $u = f(x_1, \ldots, x_n)$，我们常用 $u_i$、$\frac{\partial u}{\partial x_i}$ 或 $u_{x_i}$

来代替 $f_i$、$\frac{\partial f}{\partial x_i}$ 或 $f_{x_i}$。

当然，当只涉及少数几个变量时，

用 $x, y, z$ 来代替 $x_1, x_2, x_3$ 往往更方便。

函数 $f(x)$ 的偏导数 $f_i$ 本身也是 $x$ 的函数。

如果它们在 $x$ 的某个邻域（neighborhood）的所有点处都有定义，

那么它们自己在 $x$ 处可能也有偏导数，

这些偏导数称为 $f$ 在 $x$ 处的二阶偏导数（second partial derivatives），或二阶偏导。

二阶偏导最多可以有 $n^2$ 个；例如，当 $n = 2$ 时，可以定义四个二阶偏导：

```math
\frac{\partial}{\partial x}\left(\frac{\partial f}{\partial x}\right) = \frac{\partial^2 f}{\partial x^2}, \qquad
\frac{\partial}{\partial y}\left(\frac{\partial f}{\partial y}\right) = \frac{\partial^2 f}{\partial y^2},
```

```math
\frac{\partial}{\partial x}\left(\frac{\partial f}{\partial y}\right) = \frac{\partial^2 f}{\partial x \partial y}, \qquad
\frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right) = \frac{\partial^2 f}{\partial y \partial x}.
```

## 二阶偏导数（Second-Order Partial Derivatives）

同时涉及 $x$ 和 $y$ 的那两个偏导，常常被称为交叉偏导（cross partials）或混合偏导（mixed partials）。

我们很快会看到：混合偏导 $\frac{\partial^2 f}{\partial y \partial x}$ 与 $\frac{\partial^2 f}{\partial x \partial y}$ 相等这一事实经常（但不是总是）成立。

无论如何，务必弄清它们表示两种不同的事物，

并要从记号中辨别出到底哪一个导数先被求（performed first）。

# <span style="color:#c0392b;">书页 470 — §12.2 续：二阶偏导记号 $f_{12}$、高阶偏导（Higher-Order Partial Derivatives）</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这里有一个必须绕开的记号陷阱：$f_{12}$ 表示 $(f_1)_2$——先对 $x$ 再对 $y$；按 TBB 约定，它对应的分数记号是 $\frac{\partial^2 f}{\partial y\,\partial x}$，其中求导从右往左复合。于是同一操作在两种记号里书写方向相反：$f_{12}$ 从左往右读，分数记号从右往左读。TBB 花两页强调"看清哪个导先求"，因为不同教材的约定可能相反（有的把 $\frac{\partial^2 f}{\partial x\,\partial y}$ 定义为 $(f_x)_y$）。这就像 CSAPP 里大端/小端存储：字节序列相同、解释顺序相反，跨平台读代码前必须先确认约定。用 6.042J 的组合语言说：$n$ 元函数 $k$ 阶偏导最多 $n^k$ 个（从 $n$ 个坐标有放回取 $k$ 次），因为每次求导都独立地"任选一个坐标"，例如 $f_{221}$ 就是"先两次 $y$ 再一次 $x$"的有序序列。规则一句话：用哪套记号都行，但自己写 $\frac{\partial^2 f}{\partial x\,\partial y}$ 时必须明确它是 $(f_x)_y$ 还是 $(f_y)_x$——这正是例 12.4 混合偏导不等问题的伏笔。

---

<span style="color:#2471a3;">**[section]**</span> §12.2 偏导数与方向导数（续）。

对 $n$ 个变量的函数 $f$，一个典型的二阶偏导可记为

```math
\frac{\partial^2 f}{\partial x_i \partial x_j} = \frac{\partial}{\partial x_i}\left(\frac{\partial f}{\partial x_j}\right).
```

再次注意：到底哪个求导先进行。

如果我们用 $f_1$ 表示 $\frac{\partial f}{\partial x}$，那么二阶偏导又该用什么记号呢？

自然的写法是：用 $f_{12}$ 表示 $\frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right)$，

因为我们希望 $f_{12}$ 成为 $(f_1)_2$ 的简写（short for）。

如果这样约定，我们就在一种意义上保持了顺序（order），

但在另一种意义上又把它颠倒过来了：

因为对 $f_{12}$ 而言，我们是从左到右复合（compose）的，即 $(f_1)_2$，

而在 $\frac{\partial^2 f}{\partial y \partial x}$ 中，我们是从右到左复合的。

尽管如此，我们仍用 $f_{12}$ 表示 $(f_1)_2$，因为它操作起来稍微简单一点。

无论如何，都不会产生混淆，

因为很少有地方会同时使用 "$f_{ij}$" 记号与 "$\frac{\partial^2 f}{\partial x_i \partial x_j}$" 记号。

<span style="color:#2471a3;">**[note]**</span> <span style="color:#1e8449;">注（Note）：</span>我们顺便提到，有些作者把记号颠倒过来使用，

例如 $\frac{\partial^2 f}{\partial x \partial y}$ 在他们那里表示 $\frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right)$。

我们偏好自己的记号，因为它保持了复合的顺序（order of composition）；

但你在阅读（其他书中）涉及混合偏导的材料时，应当意识到另一种约定（convention）可能正在起作用。

## 高阶偏导数（Higher-Order Partial Derivatives）

我们还可以考虑更高阶的偏导数。

于是，例如 $\frac{\partial^3 f}{\partial x \partial y \partial y}$ 表示

```math
\frac{\partial}{\partial x}\left(\frac{\partial^2 f}{\partial y^2}\right),
```

它也可以写成 $f_{221}$，即 $(f_{22})_1$。

与之前一样，各导数被求取的先后顺序由记号给出，而这个约定必须牢记（remembered）。

<span style="color:#7f8c8d">*（本页其余部分为 §12.2 习题区，含习题 12.2.1–12.2.3，按约定跳过。）*</span>


<!-- ===== W18 ===== -->

# §12.2 Partial and Directional Derivatives（偏导数与方向导数）

><span style="color:#7f8c8d">*（本页上半部为上一节尾部遗留的习题区——含 12.2.4 "Cauchy-Riemann 方程组"、12.2.5 "调和函数" 等，按约定跳过，以下直接进入方向导数小节正文。）*</span>

### 方向导数 Directional Derivatives

- 考虑一个二元函数 f（function of two variables）。
- 函数在点 $(x_0, y_0)$ 处的偏导数 $f_1$ 与 $f_2$（partials）给出曲面沿两个方向的切线的斜率（再次参见 Figure 12.1）。
- 还可能存在对应于经过 $(x_0, y_0, z_0)$ 的其他垂直平面（vertical plane）的切线，这些平面并不平行于坐标平面 $x = 0$ 或 $y = 0$。
- 这些切线在点 $(x_0, y_0, z_0)$ 处的斜率，可以通过计算方向导数（directional derivative）得到。

<span style="color:#2471a3;">**[definition]**</span><span style="color:#00838f;">**Definition 12.2**</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定义 12.2 把"沿方向 $u$ 的变化率"翻译成一个具体动作：沿直线 $\gamma(t)=(x_0+tu_1,\,y_0+tu_2)$ 走，测复合函数 $f\circ\gamma$ 在 $t=0$ 处的导数。这是彻头彻尾的"降维"——把二元函数限制到一条直线上，变成你早已熟练的一元求导。为什么要求 $u$ 是单位向量？因为变化率要按"每单位距离"计量：若 $\|u\|=2$，同样的斜率会被放大两倍，归一化保证 $D_u f$ 只依赖方向、不依赖行进速度。这里有两个"免费"事实：其一，偏导数就是方向导数的特例（$f_1=D_{(1,0)}$、$f_2=D_{(0,1)}$），方向导数不是新概念而是统一；其二，$D_{-u}f=-D_uf$ 直接由定义成立（令 $t\mapsto -t$），这是方向导数的齐次性，不需要任何可微性假设。教材预告的"已知偏导就能写出所有方向导数"（即 $D_uf=\nabla f\cdot u$）要等 §12.4 可微性定理，届时你会看到梯度把全部方向的信息打包成一个向量——这正是 Strang 里梯度下降的起点。

---

- 设 $f : \mathbb{R}^2 \to \mathbb{R}$，并设 $u = (u_1, u_2)$ 为 $\mathbb{R}^2$ 中的一个单位向量（unit vector），即
```math
\|u\| = \sqrt{u_1^2 + u_2^2} = 1.
```
- f 在点 $(x_0, y_0)$ 处沿方向 u 的方向导数定义为
```math
D_u f(x_0, y_0) = \lim_{t \to 0}
\frac{f(x_0 + t u_1, \, y_0 + t u_2) - f(x_0, y_0)}{t},\tag{4}
```
- 前提是此极限（limit）存在。

- 正如偏导数度量 f 沿 x 方向与 y 方向的变化率，$D_u f(x_0, y_0)$ 度量的是 f 沿向量 u 方向的变化率。
- 事实上，我们应该意识到，偏导数本身就是方向导数：$f_1$ 与 $f_2$ 分别是沿方向 $(1, 0)$ 和 $(0, 1)$ 的方向导数，
- 即有 $f_1 = D_{(1,0)}$ 与 $f_2 = D_{(0,1)}$。

---

# §12.2（续）Differentiation on $\mathbb{R}^n$（$\mathbb{R}^n$ 上的微分）

> Figure 12.2 的插图用 $z$、$y$、$x$ 轴标出。

<span style="color:#2471a3;">**[figure]**</span>**Figure 12.2**：函数 $f(x, y) = x^2 + xy + 2$ 在点 $(1, 1)$ 处沿方向 $(1/2, \sqrt{3}/2)$ 的一个方向导数。

- 甚至存在某种意义上的逆命题（converse）：稍后我们会看到，在适当的附加假设之下，一旦知道偏导数，就能写出所有方向上的导数。
- 注意，若 $D_u f(x_0, y_0)$ 存在，那么反方向上的导数 $D_{-u} f(x_0, y_0)$ 也存在，并且
```math
D_{-u} f(x_0, y_0) = -D_u f(x_0, y_0).
```

<span style="color:#2471a3;">**[example]**</span><span style="color:#c0392b;">**Example 12.3**</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 例 12.3 的计算藏着两层深意。第一层：直接按定义做——把 $f(x,y)=x^2+xy+2$ 沿方向 $u=(\frac12,\frac{\sqrt3}{2})$ 参数化后代入，分子展开成 $t$ 的多项式，极限就是"取 $t$ 的一次项系数"。这是多项式函数的特权：沿直线参数化后仍是多项式，差商极限自动等于最低次项系数，无需 $\varepsilon$-$\delta$ 苦战。第二层：教材随后给出快捷公式 $D_uf=(f_1,f_2)\cdot(u_1,u_2)=f_1u_1+f_2u_2$，本例 $(3,1)\cdot(\frac12,\frac{\sqrt3}{2})=\frac32+\frac{\sqrt3}{2}$ 与定义计算完全吻合——这就是 Strang 线性代数里"梯度与单位方向向量的点积"，也是你以后做梯度下降（机器学习最优化）反复用的公式：函数上升最快的方向正是梯度方向。注意公式目前只是"预告"，它要等 §12.4 可微性定义才成为定理——这是教材的叙事节奏：先给直觉，再补证明。历史注记：梯度与 nabla 记号（$\nabla$）成形于 19 世纪（Hamilton 1853 年引入、Maxwell 1870-73 年命名相关微分算子）。

---

- 设 $f(x, y) = x^2 + xy + 2$，且 $u = (1/2, \sqrt{3}/2)$。
- 为计算 $D_u f(1, 1)$，我们计算
```math
\frac{f(1 + \tfrac12 t, \, 1 + \tfrac{\sqrt{3}}{2} t) - f(1, 1)}{t}
= \frac{(\tfrac32 + \tfrac{\sqrt{3}}{2})t + (\tfrac14 + \tfrac{\sqrt{3}}{4})t^2}{t}
\to \tfrac32 + \tfrac{\sqrt{3}}{2} \quad \text{当 } t \to 0.
```
- 稍后我们会看到，在合适的假设之下，我们可以按下式计算方向导数：
```math
D_u f = (f_1, f_2) \cdot (u_1, u_2) = f_1 u_1 + f_2 u_2.
```
- 在本例中，$f_1(1, 1) = 3$，$f_2(1, 1) = 1$，因此
```math
(3, 1) \cdot (\tfrac12, \tfrac{\sqrt{3}}{2}) = \tfrac32 + \tfrac{\sqrt{3}}{2},
```
- 这与我们先前的计算结果一致。
- Figure 12.2 展示了 f 的图像（graph），并在点 $(1, 1)$ 处沿方向 $(1/2, \sqrt{3}/2)$ 画出了切线（tangent line）。

><span style="color:#7f8c8d">*（本页其余部分为 §12.2 习题区——含 12.2.6"为 n 元实值函数定义方向导数"、12.2.7"验证 f1 与 f2 分别沿 (1,0)、(0,1) 为方向导数"等，按约定跳过。）*</span>


<!-- ===== W19 ===== -->

# <span style="color:#c0392b;">书页 473 — §12.2 续：交叉偏导（Cross Partials）与 Example 12.4</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 例 12.4 是一个必须背下来的反例：$f_{12}(0,0)=-1$ 而 $f_{21}(0,0)=1$，混合偏导不相等。为什么能这样？沿坐标轴计算时 $f_1(0,y)=-y$、$f_2(x,0)=x$ 看起来非常规整，但函数在轴外 $xy(x^2-y^2)/(x^2+y^2)$ 剧烈扭曲，二阶差商的两种取法给出不同极限——本质是两个累次极限不相等。历史上，1867 年芬兰数学家 Lindelöf 正是用这类反例终结了"混合偏导总相等"的朴素信念；此前 Euler（1740）、Clairaut（1740）等人的证明都因某个分析细节不严格而留下隐患。这个构造可命名为「轴外病态」模板：让函数在坐标轴上"装死"（取值 0 或简单），在轴外放振荡与扭曲，专门戳穿"只看坐标方向"的直觉。它与例 11.42 的 $2xy/(x^2+y^2)$ 同族——都是"轴上的正常掩盖轴外的疯狂"。记住：沿坐标轴的信息永远是采样，永远可能漏掉斜方向。

---

<span style="color:#2471a3;">**[section]**</span> §12.2 偏导数与方向导数（Partial and Directional Derivatives）。

## 交叉偏导（Cross Partials）

- 设 f 定义在区域（region）$D \subset \mathbb{R}^2$ 上，并假设两个偏导数
```math
\frac{\partial f}{\partial x}(x, y) \quad \text{与} \quad \frac{\partial f}{\partial y}(x, y)
```
在 D 中每一点 $(x, y)$ 处都存在。
- 这些偏导数自身也是 D 上的函数（functions），因此它们本身也可能拥有偏导数。
- 在这种情况下，总共有四个可能的偏导数（partial derivatives）：
```math
\frac{\partial^2 f}{\partial x^2} = \frac{\partial}{\partial x}\!\left(\frac{\partial f}{\partial x}\right), \quad
\frac{\partial^2 f}{\partial y \partial x}, \quad
\frac{\partial^2 f}{\partial x \partial y}, \quad
\frac{\partial^2 f}{\partial y^2} = \frac{\partial}{\partial y}\!\left(\frac{\partial f}{\partial y}\right).
```
- 例如，我们回想一下，我们的记号（notation）要求
```math
\frac{\partial^2 f}{\partial y \partial x} = \frac{\partial}{\partial y}\!\left(\frac{\partial f}{\partial x}\right).
```
- 两个偏导 $\frac{\partial^2 f}{\partial y \partial x}$ 与 $\frac{\partial^2 f}{\partial x \partial y}$ 常被称为交叉偏导（cross partials）或混合偏导（mixed partials）。
- 初等微积分的学生们常常认为二阶偏导只有三个，因为通常成立
```math
\frac{\partial^2 f}{\partial y \partial x} = \frac{\partial^2 f}{\partial x \partial y}. \tag{5}
```
- 在本节中，我们将确定使 (5) 成立的条件（conditions）。
- 我们从一个例子作为开端，它说明 (5) 并不总是成立。

<span style="color:#2471a3;">**[example]**</span><span style="color:#c0392b;">**Example 12.4**</span>

- 设
```math
f(x, y) =
\begin{cases}
\dfrac{xy(x^2 - y^2)}{x^2 + y^2}, & \text{若 } (x, y) \neq (0, 0),\\[8pt]
0, & \text{若 } (x, y) = (0, 0).
\end{cases}
```
- 使用下标记号（subscript notation），我们计算偏导数
```math
f_1 = \frac{\partial f}{\partial x}, \quad f_2 = \frac{\partial f}{\partial y}, \quad f_{12} = \frac{\partial^2 f}{\partial y \partial x}, \quad f_{21} = \frac{\partial^2 f}{\partial x \partial y}
```
在点 $(0, 0)$ 处的值。
- 现在
```math
f_1(0, y) = \lim_{h \to 0} \frac{f(h, y) - f(0, y)}{h}
= \lim_{h \to 0} \frac{\frac{hy(h^2 - y^2)}{h^2 + y^2}}{h} = -y.
```
- 类似地，$f_2(x, 0) = x$。
- 由此推出
```math
f_{12}(0, 0) = \lim_{k \to 0} \frac{f_1(0, k) - f_1(0, 0)}{k} = \frac{-k - 0}{k} = -1,
```
```math
f_{21}(0, 0) = \lim_{h \to 0} \frac{f_2(h, 0) - f_2(0, 0)}{h} = \lim_{h \to 0} \frac{h - 0}{h} = 1.
```
- 于是两个交叉偏导并不相等。$\square$

---

# <span style="color:#c0392b;">书页 474 — §12.2 续：混合偏导不等的原因与 Theorem 12.5</span>

<span style="color:#2471a3;">**[section]**</span> §12.2（续）$\mathbb{R}^n$ 上的微分（Differentiation on $\mathbb{R}^n$）。

- 这里究竟"出了什么错"（went wrong）呢？
- 考虑涉及 Example 12.4 中函数 f 的两个恒等表达式（identical expressions）：
```math
\frac{1}{k}\left[\frac{f(h, k) - f(0, k)}{h} - \frac{f(h, 0) - f(0, 0)}{h}\right], \tag{6}
```
```math
\frac{1}{h}\left[\frac{f(h, k) - f(h, 0)}{k} - \frac{f(0, k) - f(0, 0)}{k}\right]. \tag{7}
```
- 如果我们在 (6) 中先令 $h \to 0$，然后再令 $k \to 0$，就得到 $f_{12}(0, 0)$。
- 另一方面，在 (7) 中先令 $k \to 0$，再令 $h \to 0$，就得到 $f_{21}(0, 0)$。
- 正如我们所看到的，这两个累次极限（iterated limits）并不相等。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这一页的洞察可浓缩成一个判据：「两个累次极限不等 ⟹ 二重极限不存在」。$f_{12}$ 与 $f_{21}$ 本质上是同一个二阶差分沿"先 $h\to0$ 再 $k\to0$"与"先 $k\to0$ 再 $h\to0$"两条路径求极限；教材指出，两者不等的根源是表达式 (6)(7) 作为 $(h,k)\to(0,0)$ 的**二重极限**不存在。这与第 9 章 Example 9.7 的二重序列 $\{s_{nm}\}$ 完全同构——你在 100B 已见过"交换累次极限需谨慎"，这里在多元微分里重逢。第一性原理：$h\to0$ 与 $k\to0$ 是两个**独立的变化过程**，除非有一个"均匀"的联合极限镇住场面，否则谁先谁后产生不同结果——就像 CSAPP 里浮点加法不满足结合律、交换操作顺序会改变最终值，也像 6.042J 里 $\forall x\,\exists y$ 与 $\exists y\,\forall x$ 不可交换。定理 12.5 给出的偏导连续条件，正是保证二重极限存在的"均匀性"条件。这套"差商分解 + 累次极限对比"的手法，我命名为「二重极限判据」，是多元分析的通用诊断工具。

---

<span style="color:#2471a3;">**[note]**</span> <span style="color:#1e8449;">注（Note）：</span>你或许记得，我们以前就见过这种现象——以不同的顺序（order）求两个极限，结果可能不同。
- 在 Example 9.7 中我们看到，二重序列（double sequence）$\{s_{nm}\}$ 的两个累次极限可能不相等。
- 关于这一现象的讨论，还可参见 Exercise 9.2.8 及其提示（hint）。
- 这里我们又一次遇到了涉及累次极限的情形。

- 现在我们可以解释例子中到底出了什么问题：
- 两个混合偏导 $f_{12}$ 与 $f_{21}$ 不相等这一事实，可以追溯到表达式 (6) 或 (7) 当 $(h, k) \to 0$ 时的极限（即二重极限 double limit）不存在。
- 保证这个二重极限存在的一个简单的充分条件（sufficient condition），出现在下面的定理中。

<span style="color:#2471a3;">**[theorem]**</span><span style="color:#c0392b;">**Theorem 12.5**</span>

- 设 f 定义在点 $(x_0, y_0) \in \mathbb{R}^2$ 的一个邻域（neighborhood）上。
- 假设 f 在这个邻域内有偏导数 $f_1, f_2, f_{12}$ 与 $f_{21}$，并且混合偏导 $f_{12}$ 与 $f_{21}$ 在 $(x_0, y_0)$ 处连续（continuous）。
- 则 $f_{12}(x_0, y_0) = f_{21}(x_0, y_0)$。

<span style="color:#2471a3;">**[proof]**</span><span style="color:#c0392b;">**证明（Proof）**</span>

- 考虑两个恒等的表达式
```math
\frac{1}{k}\left[\frac{f(x_0 + h, y_0 + k) - f(x_0, y_0 + k)}{h} - \frac{f(x_0 + h, y_0) - f(x_0, y_0)}{h}\right], \tag{8}
```
```math
\frac{1}{h}\left[\frac{f(x_0 + h, y_0 + k) - f(x_0 + h, y_0)}{k} - \frac{f(x_0, y_0 + k) - f(x_0, y_0)}{k}\right]. \tag{9}
```
- 如果我们在 (8) 中先令 $h \to 0$，然后再令 $k \to 0$，就得到 $f_{12}(x_0, y_0)$。
- 另一方面，在 (9) 中先令 $k \to 0$，再令 $h \to 0$，就得到 $f_{21}(x_0, y_0)$。
- 我们将证明这两个累次极限相等。
- 首先注意，表达式 (8) 方括号中的分子（numerator）$D_{hk}$ 可以写成如下形式：
```math
\bigl(f(x_0 + h, y_0 + k) - f(x_0 + h, y_0)\bigr) - \bigl(f(x_0, y_0 + k) - f(x_0, y_0)\bigr). \tag{10}
```
- 将中值定理（mean value theorem，Theorem 7.20）应用于 (10)，我们得到
```math
D_{hk} = \bigl(f_1(\xi, y_0 + k) - f_1(\xi, y_0)\bigr)h, \tag{11}
```
其中 $\xi$ 位于 $x_0$ 与 $x_0 + h$ 之间。
- 再次应用中值定理，我们得到
```math
D_{hk} = f_{12}(\xi, \zeta)\, hk,
```
其中 $\zeta$ 位于 $y_0$ 与 $y_0 + k$ 之间。

><span style="color:#7f8c8d">*（本页原文止于证明中段，证明在下一页继续。）*</span>


<!-- ===== W20 ===== -->

# §12.2（续）Partial and Directional Derivatives（偏导数与方向导数）

><span style="color:#7f8c8d">*（本页承接第 474 页：先完成定理 12.5（Clairaut/Schwarz 定理——混合偏导相等）证明的收尾，随后是注记、混合偏导相等的充分条件讨论、例 12.6、其他充分条件与高阶推广。）*</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 例 12.6 说明连续性只是充分条件、不是必要条件：$f(x,y)=yx^2\sin(1/x)$ 的两个混合偏导在 $(0,0)$ 都不连续，但 $f_{12}(0,0)=f_{21}(0,0)=0$ 依然相等。其材料是单变量经典函数 $g(x)=x^2\sin(1/x)$——它在 $\mathbb{R}$ 上可导，但导函数 $g'$ 在 0 处不连续（$g'$ 在 0 附近以 $\cos(1/x)$ 的振幅剧烈振荡）。这个单变量事实本身值得单独记住：**可导函数的导函数不必连续**。顺带一提，导函数并非毫无约束——Darboux 定理说导函数必具有介值性（取到介于两值之间的一切值），只是不保证连续。构造二维反例的手法我命名为「单变量抬升」：取一维病态函数 $g$，令 $f(x,y)=y\cdot g(x)$（乘一个线性因子），使病态只沿 $x$ 方向保留、$y$ 方向保持温和，再检查混合偏导恰好躲过连续性要求。这与 CSAPP 里"用最小可复现用例定位 bug"的思路同构：把最坏行为隔离到最小维度，其余维度尽量平凡。

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定理 12.5 的名字之争本身就是一部数学史：它常被称为 Clairaut 定理或 Schwarz 定理。事实是——Nicolaus Bernoulli 早在 1721 年就隐含假设过混合偏导相等；Euler 1740 年首次给出证明，Clairaut 同年也独立给出证明，但 Clairaut 的证明隐含假设了"定积分可在积分号下求导"（正是 §12.3 的内容，一个漂亮的自我循环）；可惜这些证明都有缺陷，1867 年 Lindelöf 构造反例后，Schwarz 1873 年给出第一个严格证明，Peano、Jordan、Young 随后给出更弱条件版本。证明骨架是「差商分解 + 中值定理夹逼」：把二阶差分 $D_{hk}$ 沿两条路径各用两次一元中值定理（定理 7.20），得 $D_{hk}=f_{12}(\xi,\zeta)hk=f_{21}(\sigma,\tau)kh$；关键一步是 $(h,k)\to(0,0)$ 时中间点 $(\xi,\zeta)$、$(\sigma,\tau)$ 都被"吸"向 $(x_0,y_0)$，连续性恰好允许把 $f_{12}$、$f_{21}$ 在这些中间点的值替换成点 $x_0$ 处的值——中值定理给出"点不确定"，连续性把不确定性吸收。这个"中值定理 + 连续性"组合拳，你在 Rudin 第 9 章还会再见。

---

<span style="color:#2471a3;">**[proof]**</span> <span style="color:#c0392b;">**定理 12.5 证明（续）**</span>

- 我们可以把 (10) 改写为如下形式：
```math
( f(x_0 + h,\, y_0 + k) - f(x_0,\, y_0 + k) ) - ( f(x_0 + h,\, y_0) - f(x_0,\, y_0) ).
```
- 再次运用与之前相同的论证（argument），我们得到
```math
D_{hk} = f_{21}(\sigma, \tau) \, kh,
```
- 其中 $\sigma$ 介于 $x_0$ 与 $x_0 + h$ 之间，$\tau$ 介于 $y_0$ 与 $y_0 + k$ 之间。
- 现在令 $(h, k) \to (0, 0)$。于是 $(\xi, \zeta) \to (x_0, y_0)$ 且 $(\sigma, \tau) \to (x_0, y_0)$。
- 由于函数 $f_{12}$ 与 $f_{21}$ 在 $(x_0, y_0)$ 处连续（由假设 hypothesis），我们得到
```math
\lim_{(h,k) \to (0,0)} \frac{D_{hk}}{hk} = f_{21}(x_0, y_0) = f_{12}(x_0, y_0),
```
- 这正是所要证的。$\square$

<span style="color:#2471a3;">**[note]**</span> <span style="color:#1e8449;">**注**</span>

- 注意，我们的证明实际上还表明，下述二重极限（double limit）成立：
```math
\lim_{(h,k) \to (0,0)} \frac{D_{hk}}{hk} = f_{21}(x_0, y_0) = f_{12}(x_0, y_0).
```
- 这是一个比定理结论更强的陈述（stronger statement）。
- 我们将在后面讨论可微性（differentiability）时再回到这一思想。

- 定理 12.5 表明，偏导数的连续性（continuity of the partials）是 $f_{12}$ 等于 $f_{21}$ 的一个充分条件（sufficient condition）。
- 这一条件经常得到满足，但它并非必要条件（necessary condition）。

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b;">**Example 12.6**</span>

- 我们可以利用如下函数来构造一个例子：
```math
g(x) = x^2 \sin\frac{1}{x},\qquad g(0) = 0,
```
- 该函数在 $\mathbb{R}$ 上可微（differentiable），但其导数 $g'$ 在 $x = 0$ 处不连续。
- 由此可知，函数
```math
f(x, y) = yx^2 \sin\frac{1}{x},\qquad f(0, y) = 0
```
- 的两个混合偏导 $f_{12}$ 与 $f_{21}$ 在 $(0, 0)$ 处都不连续。
- 因而定理 12.5 在此并不适用，然而这两个偏导
```math
f_{21}(0, 0) = f_{12}(0, 0) = 0
```
- 却是相等的。

- 关于混合偏导（mixed partials）相等，人们还知道其他充分条件。
- 例如，只需假设两个混合偏导都存在，并且其中某一个在 $(x_0, y_0)$ 处连续；或者假设 $f_1$ 与 $f_2$ 在 $(x_0, y_0)$ 处可微$^1$。
- 我们略去这些证明。

- 定理 12.5 很容易推广到高阶导数（higher-order derivatives）。
- 例如，若 $f$ 具有一阶、二阶与三阶偏导数，且所有这些偏导数在 $(x_0, y_0)$ 处都连续，则
```math
f_{221} = (f_2)_{21} = (f_2)_{12} = f_{212} = (f_{21})_2 = (f_{12})_2 = f_{122}.
```

---

$^1$ 此处"可微"指 §12.4 中稍后定义的意义。

---

# §12.2（续）Differentiation on $\mathbb{R}^n$（$\mathbb{R}^n$ 上的微分）

><span style="color:#7f8c8d">*（本页上半部为 §12.2 收尾：定理 12.7 把定理 12.5 推广到 n 元函数；随后为 §12.2 习题区，按约定跳过；下半部进入 §12.3 含参变量积分。）*</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> §12.3 引入的"含参积分"观念值得停下来品一品：$F(y)=\int_a^b f(x,y)dx$ 把 $y$ 当参数、对 $x$ 积分，这与偏导数"冻结一个变量、对另一个求导"是完全对称的"偏运算"——一个是"偏积分"，一个是"偏微分"。第一性原理：这里在做一次"流水线加工"——输入二元函数 $f$，第一步对 $x$ 做积分（消掉 $x$），输出只依赖 $y$ 的一元函数 $F$，再问 $F$ 连续吗？可微吗？怎么算 $F'$？教材特意区分两类对象：$G(y)=\int_a^y g(x)dx$ 是"变上限积分"（用微积分基本定理），而 $F(y)=\int_a^b f(x,y)dx$ 是"含参积分"（参数在上限之外，需要新工具）。你在 100B 已学的一致收敛在这里悄悄登场：定理 12.9 证明里交换"积分"与"求导"两个无限过程的合法性，靠的正是 $\partial f/\partial y$ 的一致连续性——与"一致收敛才敢交换极限与积分"是同一哲学。历史背景：含参积分是 18 世纪 Euler、Clairaut 等人的日常工具，严格化要等 19 世纪分析算术化（Cauchy、Weierstrass 体系）之后。

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定理 12.7 的证明是教科书级的分治：把 $n$ 元函数 $f$ 中除第 $i$、$j$ 个变量外的所有变量固定（冻结），就得到一个二元函数，直接套用定理 12.5 即可——唯一的代价是记号变复杂。我命名这套手法为「冻结变量归约」：凡是只涉及两个变量（或两条方向）的多元性质，先冻结其余变量把维度降到 2，用完二元结论再解冻，最后对每个 $(i,j)$ 组合分别应用。这与 CLRS 里"把大问题分解成可独立求解的子问题再合并"的思想完全一致，也像 CSAPP 里处理多维数组时"固定其他维、遍历某一维"的循环结构。注意定理 12.7 只要求"某一对 $(i,j)$ 的混合偏导连续"，结论也只对这对下标成立——所以它是"逐对"的，不是"全自动"的。把定理 12.5、12.7 连起来看：Clairaut/Schwarz 的核心机制是"二阶差分 + 中值定理"，它对任意两个坐标方向都成立，维度本身只是外壳。

---

### 多变量函数的偏导数（Partial Derivatives of $f: \mathbb{R}^n \to \mathbb{R}$）

- 定理 12.5 也可以推广到多于两个变量的函数（functions of more than two variables）。
- 下面的定理通过在证明中把除第 $i$ 个与第 $j$ 个变量以外的所有变量都固定，从而归结为定理 12.5。
- 只是记号（notation）变得更复杂而已。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**Theorem 12.7**</span>

- 设 $f$ 定义在 $\mathbb{R}^n$ 中某点 $x_0$ 的一个邻域（neighborhood）内。
- 假设 $f$ 在此邻域内具有偏导数 $f_i$、$f_j$、$f_{ij}$ 与 $f_{ji}$。
- 并且混合偏导 $f_{ij}$ 与 $f_{ji}$ 在 $x_0$ 处连续；
- 则 $f_{ij}(x_0) = f_{ji}(x_0)$。

><span style="color:#7f8c8d">*（本页其余部分为 §12.2 习题区——含 12.2.8"三阶混合偏导的个数"、12.2.9"调和函数验证 $f_{12}=f_{21}$ 与 $f_{112}=f_{121}=f_{211}$"、12.2.10"计算 $f_{12}(0,0)$ 与 $f_{21}(0,0)$"、12.2.11"二重极限与累次极限"等，按约定跳过。）*</span>

# §12.3 Integrals Depending on a Parameter（含参变量积分）

<span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b;">**含参变量积分（Integrals Depending on a Parameter）**</span>

- 设 $g$ 在 $[a, b]$ 上连续，并设
```math
G(y) = \int_a^y g(x)\,dx .\tag{12}
```
- 我们从微积分基本定理（fundamental theorem of calculus）回忆起：$G'(y) = g(y)$ 对所有 $y \in [a, b]$ 成立。
- 这代表了微分与积分互为逆运算（inverse nature of differentiation and integration）的一半。

- 现在让我们把事情稍微复杂化一点。
- 设 $f$ 在矩形（rectangle）
```math
R = \{ (x, y) \in \mathbb{R}^2 : a \le x \le b,\ c \le y \le d \}
```
- 上连续。
- 定义函数 $F : [c, d] \to \mathbb{R}$ 为
```math
F(y) = \int_a^b f(x, y)\,dx .\tag{13}
```


<!-- ===== W21 ===== -->

><span style="color:#7f8c8d">*（本页为书页 477，进入 §12.3 正文；此处无习题区。）*</span>

# §12.3 Integrals Depending on a Parameter（含参变量积分）

<span style="color:#2471a3;">**[section]**</span><span style="color:#c0392b;">**12.3 含参变量积分**</span>

- 要看出 $F$ 是良好定义的（well defined），我们只需注意到：对每个固定的 $y \in [c, d]$，$f(\cdot, y)$ 不过是 $[a, b]$ 上的一个连续函数，因此该积分确实存在。
- 我们可以把 (13) 视为一种"偏积分"（partial integral），正如我们对待导数那样来看待偏导数：在这两种情形中，都是对一个变量施行某种运算，而另一个变量保持固定。
- 关于函数 $F$ 我们能说些什么？$F$ 在 $[c, d]$ 上连续吗？$F$ 可微（differentiable）吗？如果可微，我们又该如何计算 $F'$？
- 我们将在本节讨论诸如此类的问题。
- 观察 (12) 与 (13) 之间的两点差异：在 (12) 中，我们处理的是单变量函数 $g$；而在 (13) 中，$f$ 是二元函数。
- 此外，在 (12) 中积分上限是变量 $y$，而在 (13) 中积分上限是常数 $b$。
- 形如 $\int_a^b f(x, y)\, dx$ 的积分在实践中频繁出现。
- 我们把 $y$ 看作一个参数（parameter），并且常常关心这样的问题："参数的一个微小变化会如何影响所得的积分？"
- 我们先就 $F$ 的连续性来回答这个问题，然后再讨论其可微性。

<span style="color:#2471a3;">**[theorem]**</span><span style="color:#c0392b;">**Theorem 12.8**</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定理 12.8 证明的精髓是「紧致性统一误差」模板：想让 $F(y)=\int_a^b f(x,y)dx$ 随参数 $y$ 连续，第一反应是"每个 $x$ 处 $f$ 都连续"，但逐点的小误差经积分累积后可能失控——于是借用紧致性（矩形 $R$ 闭且有界）把 $f$ 升级为一致连续（定理 11.49），得到一个对所有 $x$ 同时成立的 $\delta$，误差被压到 $\varepsilon/(b-a)$，积分后恰好转回 $\varepsilon$。分母 $b-a$ 的设计尤其精妙：它是"把积分区间长度除出来"的余量，保证 $\int_a^b\frac{\varepsilon}{b-a}dx=\varepsilon$ 恰好闭环——先定"每点上的容差"，再让积分器把误差线性放大回总容差。这与 CLRS 里"先证局部界、再取全局界"的套路同源，也与你在 100B 学一致收敛时"先局部后一致"的手感一致。对比一下：若 $f$ 只是逐点连续而非一致连续，$\delta$ 会随 $x$ 变化，证明立刻失效——这正是定理 11.49 价值所在。

---

- 若 $f$ 在矩形 $R = [a, b] \times [c, d]$ 上连续，且
```math
F(y) = \int_a^b f(x, y)\, dx,
```
- 则 $F$ 在 $[c, d]$ 上连续。

<span style="color:#2471a3;">**[proof]**</span><span style="color:#c0392b;">**证明（定理 12.8）**</span>

- 取 $y_0 \in [c, d]$，我们证明 $F$ 在 $y_0$ 处连续。
- 由于 $R$ 是闭且有界的，因而是紧致的（compact），故由定理 11.49 知 $f$ 在 $R$ 上一致连续（uniformly continuous）。
- 于是，对 $\varepsilon > 0$ 存在 $\delta > 0$，使得对每个 $x \in [a, b]$，只要 $|y - y_0| < \delta$，就有
```math
|f(x, y) - f(x, y_0)| < \frac{\varepsilon}{b-a}.
```
- 对 $|y - y_0| < \delta$，我们计算
```math
|F(y) - F(y_0)| = \left|\int_a^b (f(x, y) - f(x, y_0))\, dx\right|
\le \int_a^b |f(x, y) - f(x, y_0)|\, dx
\le \int_a^b \frac{\varepsilon}{b-a}\, dx = \varepsilon.
```
- 因此 $\lim_{y \to y_0}(F(y) - F(y_0)) = 0$，故 $F$ 在 $y_0$ 处连续。$\square$

- 现在我们转向 $F$ 的可微性问题。
- 我们希望找到一个公式，通过"积分号下求导"（differentiation under the integral sign）得到 $F'$。
- 但这里的 $f$ 是二元函数，因而需要调用偏导数（partial derivative）。
- 定理 12.9 常被称为 Leibniz 法则（Leibniz's rule）。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Leibniz 法则（积分号下求导）的历史很有趣：方法可上溯到 Leibniz 本人 1697 年（微积分共同创始人，1646-1716；微分学论文 1684 年发表），但在大学课程中长期被边缘化，直到 20 世纪被物理学家 Feynman 当作"秘密武器"在自传《别闹了，费曼先生》中公开——他自述靠反复用"积分号下求导"解出 MIT 与普林斯顿同学搞不定的积分，从此被称为"费曼技巧"。证明核心是「中值定理交换」模板：先对差商 $\frac{F(y+h)-F(y)}{h}$ 中的被积函数用一元中值定理（定理 7.20），把 $f(x,y+h)-f(x,y)$ 改写成 $h\cdot\frac{\partial f}{\partial y}(x,y+\xi h)$，于是差商变成 $\int_a^b[\frac{\partial f}{\partial y}(x,y+\xi h)-\frac{\partial f}{\partial y}(x,y)]dx$；再用 $\partial f/\partial y$ 的一致连续性（紧致矩形 + 定理 11.49）把 $\xi h$ 这个残余误差抹平，最后把极限搬进积分号。两大支柱——中值定理定位、一致连续抹平——与第 9 章一致收敛交换极限共享同一骨架：凡"交换两个无限过程"都需条件，CSAPP 里交换浮点操作顺序会改变结果亦是同理。

---

<span style="color:#2471a3;">**[theorem]**</span><span style="color:#c0392b;">**Theorem 12.9（Leibniz 法则）**</span>

- 设 $f$ 在矩形 $R = [a, b] \times [c, d]$ 上连续，并设对每个 $y \in [c, d]$ 有
```math
F(y) = \int_a^b f(x, y)\, dx.
```
- 若偏导数 $\frac{\partial f}{\partial y}$ 存在且在 $R$ 上连续，则 $F$ 在 $[c, d]$ 上可微，且
```math
F'(y) = \int_a^b \frac{\partial}{\partial y} f(x, y)\, dx.
```

---

><span style="color:#7f8c8d">*（本页为书页 478；定理 12.9 的陈述跨页至此页顶部收尾，以下直接进入其证明。）*</span>

<span style="color:#2471a3;">**[proof]**</span><span style="color:#c0392b;">**证明（定理 12.9）**</span>

- 只需证明：对每个 $y \in [c, d]$，有
```math
\lim_{h \to 0}\left[\frac{F(y+h) - F(y)}{h} - \int_a^b \frac{\partial}{\partial y} f(x, y)\, dx\right] = 0. \tag{14}
```
- 现在对 $y + h \in [c, d]$，有
```math
F(y+h) - F(y) = \int_a^b [f(x, y+h) - f(x, y)]\, dx. \tag{15}
```
- 由中值定理（mean value theorem，定理 7.20）可知：对固定的 $x, y, h$，存在数 $\xi \in (0, 1)$，使得
```math
f(x, y+h) - f(x, y) = h\, \frac{\partial f}{\partial y}(x, y + \xi h). \tag{16}
```
- 将 (16) 代入 (15)，我们得到
```math
\frac{F(y+h) - F(y)}{h} - \int_a^b \frac{\partial}{\partial y} f(x, y)\, dx
= \int_a^b \left[\frac{\partial f}{\partial y}(x, y + \xi h) - \frac{\partial f}{\partial y}(x, y)\right] dx. \tag{17}
```
- 由于（依假设）$\frac{\partial f}{\partial y}$ 连续，故它在紧致集 $R$ 上一致连续。
- 于是，对 $\varepsilon > 0$ 存在 $\delta > 0$，使得若 $(x, y) \in R$ 且 $(x', y') \in R$ 满足 $|x - x'| < \delta$ 与 $|y - y'| < \delta$，则
```math
\left|\frac{\partial f}{\partial y}(x, y) - \frac{\partial f}{\partial y}(x', y')\right| < \frac{\varepsilon}{b-a}.
```
- 特别地，若 $|h| < \delta$，则
```math
\left|\frac{\partial f}{\partial y}(x, y + \xi h) - \frac{\partial f}{\partial y}(x, y)\right| < \frac{\varepsilon}{b-a}. \tag{18}
```
- 由 (17) 与 (18) 我们推断：对 $|h| < \delta$，有
```math
\left|\frac{F(y+h) - F(y)}{h} - \int_a^b \frac{\partial}{\partial y} f(x, y)\, dx\right|
\le \int_a^b \frac{\varepsilon}{b-a}\, dx = \varepsilon,
```
- 于是 (14) 得证。$\square$

<span style="color:#2471a3;">**[example]**</span><span style="color:#c0392b;">**Example 12.10**</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 例 12.10 是 Leibniz 法则最平凡的应用：$F(y)=\int_a^b\sin(xy)dx$ 的导数就是"把求导穿过积分号"得到 $\int_a^b x\cos(xy)dx$。教材特意指出：这里两个积分都能用初等函数算出来，所以法则只是"验证"而非"必需"——真正展现威力的是例 12.11 那种"原积分算不出、求导后的积分却能处理"的情形。第一性原理：Leibniz 法则是一个**反着用**的工具——常规思路是先算出 $F(y)$ 再求导，但很多 $F(y)$ 根本没有初等原函数；法则让你绕道：先对参数求导得到更简单的积分，再通过积分"求回来"，配合一个特值定常数。这与 CSAPP 里"直接求解困难就变换问题域（查表、变换、递归下降）"的算法思想同构。另注意一个细节：这里的 $x$ 是积分变量、$y$ 是参数，$\frac{\partial}{\partial y}$ 与 $\int_a^b dx$ 作用的变量不同——Leibniz 法则本质是"两个不同变量的操作交换顺序"，这正是它为什么需要偏导连续这个交换条件。

---

- 若
```math
F(y) = \int_a^b \sin(xy)\, dx,
```
- 则可由定理 12.9 得出结论
```math
F'(y) = \int_a^b x \cos(xy)\, dx.
```
- 我们不过是"穿过"（through）积分号求导罢了。$\blacksquare$


<!-- ===== W22 ===== -->

# <span style="color:#c0392b;">书页 479 — §12.3 续：积分号下求导（Differentiation under the Integral Sign）之 Leibniz 法则应用例</span>

<span style="color:#2471a3;">**[section]**</span> §12.3 含参变量积分（Integrals Depending on a Parameter）续。

在刚才这个例子中，出现的两个积分都能用初等方法（elementary methods）容易地求出来（于是 Leibniz 法则 Leibniz's rule 也就随之得到验证）。

但一般而言，这种情形并不总能成立。

常常无法用初等函数（elementary functions）来表示以下两个积分中某一个或全部的精确值：

```math
\int_a^b \frac{\partial f}{\partial y}(x, y)\, dx \qquad \text{或} \qquad \int_a^b f(x, y)\, dx.
```

下面我们继续考察几个把 Leibniz 法则与其他技巧结合起来使用的例子。

<span style="color:#2471a3;">**[example]**</span><span style="color:#c0392b;">**Example 12.11**</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 例 12.11 的 $F(y)=\int_0^{\pi/2}\frac{dx}{\sqrt{1-y^2\sin^2x}}$ 是第一类椭圆积分，它背后的故事值得知道：椭圆积分因"求椭圆弧长"而生（Wallis 1655 年已研究椭圆弧长；Fagnano 1718 年发现双纽线弧长加倍公式；Euler 1757 年给出加法定理），Legendre 1793-1828 年把它系统分类为三类并命名（第一类记 $F$、第二类记 $E$，习题 12.3.4 里的第二类正来自椭圆弧长）。关键事实：这类积分**不能用初等函数表出**——Legendre 与 Jacob Bernoulli 早有此猜测，Liouville 1833 年严格证明。于是 Leibniz 法则的价值凸显：算不出原函数，却能求导数，绕道微分方程研究它。脚手架：把"定义新函数"想成 CSAPP 里"抽象新数据结构"——当 $\int\frac{dx}{\sqrt{1-y^2\sin^2x}}$ 无法闭式表达，数学家不硬拼，而是宣布"这是新函数 $F$"再研究其性质。后来 Abel（1826-27）与 Jacobi（1827-29）反其道而行，研究椭圆积分的反函数，催生了"双周期"的椭圆函数，最终通向椭圆曲线——费马大定理证明的核心对象。

---

要计算函数

```math
F(y) = \int_0^{\pi/2} \frac{dx}{\sqrt{1 - y^2 \sin^2 x}} \qquad (0 < y < 1)
```

的导数（derivative），

我们只需直接应用 Leibniz 法则，便可得到

```math
F'(y) = \int_0^{\pi/2} \frac{y \sin^2 x}{(1 - y^2 \sin^2 x)^{3/2}}\, dx.
```

这就是带参数 $y$ 的椭圆积分（elliptic integral）的一个例子。

<span style="color:#2471a3;">**[example]**</span><span style="color:#c0392b;">**Example 12.12**</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 例 12.12 是"参数以多种身份出现"时的标准解法：$F(y)=\int_0^{y^2}yx^3dx$ 中 $y$ 既在被积函数里、又在积分上限里，直接套 Leibniz 法则不够。解法分三步：把上限改造成第二个变量 $u=y^2$，构造二元函数 $G(u,v)=\int_0^u vx^3dx$；对 $u$ 用微积分基本定理（$\partial G/\partial u=vu^3$），对 $v$ 用 Leibniz 法则（$\partial G/\partial v=u^4/4$）；最后用链式法则把它们"叠加"：$F'(y)=G_uu'+G_vv'=vu^3\cdot2y+\frac{u^4}{4}\cdot1=\frac94y^8$。第一性原理：当一个量以多种身份出现，就把每种身份升级成独立变量，各算各的偏导，再用链式法则合成——这是"变量分离 + 合成"的教科书示范。跨课程：$G_uu'+G_vv'$ 正是 Strang 里"链式法则 = 矩阵乘法"的最小实例：$[G_u\ G_v]\begin{bmatrix}u'\\v'\end{bmatrix}$ 是一个 $1\times2$ 行向量乘 $2\times1$ 列向量。直接验证：$F(y)=y\cdot\frac{y^8}{4}=\frac{y^9}{4}$，求导同样得 $\frac94y^8$——殊途同归。

---

积分

```math
F(y) = \int_0^{y^2} y x^3\, dx \tag{19}
```

及其导数都可以用初等的方法轻易算出。

作为练习，我们尝试用 Leibniz 法则来计算 $F'$。

首先我们注意到：这里的积分上限（upper limit of integration）是变量，

所以仅仅直接套用 Leibniz 法则是不够的。

在本例中，参数既出现在被积函数（integrand）中，又出现在积分限里。

因此，除了 Leibniz 法则之外，我们还需要用到微积分基本定理（fundamental theorem of calculus）以及链式法则（chain rule）。

（链式法则的证明见 §12.5.4 的定理 12.34。）

令

```math
u = y^2, \qquad v = y, \qquad G(u, v) = \int_0^u v x^3\, dx.
```

于是微积分基本定理给出

```math
\frac{\partial G}{\partial u} = v u^3,
```

而 Leibniz 法则提供

```math
\frac{\partial G}{\partial v} = \int_0^u x^3\, dx = \frac{u^4}{4},
```

再由二元函数微分学中我们熟知的链式法则，得到

```math
\frac{d}{dy} F(y) = \frac{\partial G}{\partial u}\frac{du}{dy} + \frac{\partial G}{\partial v}\frac{dv}{dy}
= v u^3 \cdot 2y + \frac{u^4}{4} \cdot 1
= 2y^8 + \frac{y^8}{4} = \frac{9}{4} y^8.
```

这与我们先求积分 (19)、再对结果求导所得的结论完全一致。

# <span style="color:#c0392b;">书页 480 — §12.3 收尾 + §12.4 可微函数（Differentiable Functions）开篇</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> §12.4 开篇是一个"设计决策"现场：为什么不能把"每个变量都有有限偏导"定义为可微？答案在前面的例 11.42：那个函数在原点两个偏导都是 0，却不连续、更不可微。第一性原理：可微性的本质不是"每条坐标方向都能求导"，而是"存在一个线性映射同时拟合所有方向"——偏导数只是这个线性映射沿坐标方向的"采样值"，正如 Strang 里矩阵的一行或一列代表不了整个矩阵。所以教材不直接下定义，而是先退回一元情形，看清"切线比连续性给出更好的逼近"这个核心（(20) 与 (22) 的对比），再把"误差是 $o(|x-x_0|)$ 的线性逼近"翻译成多元语言。这是构建主义的写法：定义不是天降的公理，是从"我们需要什么样的逼近"倒推出来的需求。这也解释了为什么下一节要从 $L(x)=a_0x+a_1$ 这样最简单的仿射函数开始——切平面就是"所有过点且仿射的平面"里最贴合的那个。

---

<span style="color:#2471a3;">**[section]**</span> §12.3（续）Differentiation on $\mathbb{R}^n$（$\mathbb{R}^n$ 上的微分）。

本章的部分习题会用到微积分里的各种链式法则（chain rule）。

这些链式法则以及其他链式法则，

将在 §12.5、§12.5.4、§12.5.6 与 §12.8 中，

得到更为详细的讨论，并给出相应的证明。

<span style="color:#7f8c8d">*（本页中间部分为 §12.3 习题区——含 12.3.1"用初等微积分的方法直接验证例 12.12 的结果"、12.3.2"计算下列各函数 $F$ 的 $F'(y)$"（其中被积函数均为 $e^{-x^2 y^2}$ 一类）、12.3.3"当 $u$、$v$ 在 $\mathbb{R}$ 上有连续导数、$f$ 及其偏导数在 $\mathbb{R}^2$ 上连续时，推导 $F'(y) = \int_{u(y)}^{v(y)} f(x, y)\, dx$ 的求导公式"、12.3.4"对第二类椭圆积分 elliptic integral of the second kind $F(y) = \int_0^y \sqrt{1 - k^2 \sin^2 t}\, dt$ 计算 $F'(y)$"（它出现在椭圆弧长的计算中）、12.3.5"用初等微积分技巧证明：由 $x = a\cos t$、$y = b\sin t$（$0 < a < b$）参数化给出的椭圆之弧长，等于积分 $\int_0^{2\pi} \sqrt{1 - k^2 \sin^2 t}\, dt$，其中 $k^2 = (b^2 - a^2)/b^2$"等，按约定跳过。）*</span>

<span style="color:#2471a3;">**[section]**</span> §12.4 可微函数（Differentiable Functions）。

当一元实函数 $f$ 在点 $x_0$ 处具有有限导数（finite derivative）时，

我们就说 $f$ 在 $x_0$ 处可微（differentiable at $x_0$）。

这不过是可微性（differentiability）的定义本身。

一元可微函数具有许多有用的性质。

其中最基本的一条是：在 $x_0$ 处的那条切线（tangent line），

是函数 $f$ 在 $x_0$ 附近的一个很好的近似（close approximation）。

我们或许会想把这套说法照搬到更高维的情形中：

于是便声称，一个对每个变量都具有有限偏导数的多元函数，

就应当被称为"可微"（differentiable）的。

但这样的定义并不实用。

而且，它也并不能推广"切线是可微函数的良好近似"这一核心概念。


<!-- ===== W23 ===== -->

<!-- ===== 书页 481 ===== -->

# <span style="color:#c0392b;">§12.4 可微函数（Differentiable Functions）</span>

## <span style="color:#c0392b;">12.4.1 用线性函数逼近（Approximation by Linear Functions）</span> <span style="color:#2471a3;">**[section]**</span>

让我们更仔细地考察一下单变量情形，看看其中究竟涉及什么。

设 $f : \mathbb{R} \to \mathbb{R}$，$x_0 \in \mathbb{R}$，并且 $L(x) = a_0 x + a_1$ 是任意一个满足 $L(x_0) = f(x_0)$ 的仿射函数（affine function）。

若 $f$ 在 $x_0$ 处连续，那么当 $x$ 靠近 $x_0$ 时，$f(x)$ 就会靠近 $L(x)$。

更精确地说，

```math
\lim_{x \to x_0} |f(x) - L(x)| = 0. \tag{20}
```

我们可以说，在 (20) 的意义下，$L$ 在 $x_0$ 附近逼近 $f$。

因此，若 $f$ 在 $x_0$ 处连续，则任何过点 $(x_0, f(x_0))$ 的仿射函数都在 $x_0$ 附近逼近 $f$。

若 $f$ 在 $x_0$ 处可微（differentiable），我们就能利用切线（tangent line）$T$ 得到更好的逼近。

这条线具有方程

```math
T(x) = f(x_0) + f'(x_0)(x - x_0).
```

现在，$f$ 在 $x_0$ 处可微意味着当 $x \to x_0$ 时

```math
\left|\frac{f(x) - f(x_0)}{x - x_0} - f'(x_0)\right| \to 0. \tag{21}
```

我们可以把 (21) 写成当 $x \to x_0$ 时

```math
\left|\frac{f(x) - T(x)}{x - x_0}\right| \to 0 \tag{22}
```

的形式。

将 (22) 与 (20) 相比较，我们看到了当使用切线（在它存在时）时逼近所获得的改进：

在 (20) 中，我们把 $|f(x) - L(x)|$ 除以常数 1，得到极限 0；

在 (22) 中，我们把 $|f(x) - T(x)|$ 除以 $|x - x_0|$——后者随 $x \to x_0$ 而趋于 0——却仍然得到极限 0。

因此，当 $x$ 靠近 $x_0$ 时，不仅 $T(x)$ 靠近 $f(x)$，而且 $T(x)$ 与 $f(x)$ 之间的距离相对于 $x$ 与 $x_0$ 之间的距离而言也是小的。

最后，我们把 (22) 改写为一种便于推广到多变量函数的形式。

若记 $h = x - x_0$，并对 (22) 稍加整理，就得到等价的表述

```math
f(x_0 + h) - f(x_0) = f'(x_0)h + \varepsilon h, \tag{23}
```

其中当 $h \to 0$ 时 $\varepsilon \to 0$。

此处 $\varepsilon$ 依赖于 $h$（以满足 (23) 中的等式），而可微性的要求 (21) 正是当 $h \to 0$ 时 $\varepsilon \to 0$。

> <span style="color:#7f8c8d">**脚注：** 一个实变量的实值函数 $L$ 若其图像为一条直线，则称为仿射的；于是 $L(x) = a_0 x + a_1$。在微积分课程中这类函数通常被称为"线性的（linear）"，但我们的语言必须更为精确，因为我们的表述中用到了线性代数。注意，能被线性函数 $a_0 x$ 逼近的是 $f(x) - f(x_0)$ 这一函数。</span>

## <span style="color:#c0392b;">12.4.2 可微性的定义（Definition of Differentiability）</span> <span style="color:#2471a3;">**[section]**</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> (20) 与 (22) 的对比是本节灵魂：连续性只保证 $|f(x)-L(x)|\to0$（误差与常数 1 比），可微性要求 $\frac{|f(x)-T(x)|}{|x-x_0|}\to0$（误差与 $|x-x_0|$ 比）——误差的"阶"从"趋于 0"升级为"比 $|x-x_0|$ 还小"，即 $o(|x-x_0|)$。第一性原理：数学里"逼近的强度"由"除以什么"决定——除以常数是连续，除以 $|x-x_0|$ 是可微，除以 $|x-x_0|^2$ 就是二阶（Taylor）逼近。这与 CLRS 的渐近记号 $O/o$ 精神一脉相承：$o(h)$ 就是说"误差相对 $h$ 可忽略"。教材把可微改写成 $f(x_0+h)-f(x_0)=f'(x_0)h+\varepsilon h$（$\varepsilon\to0$）——"线性主部 + 高阶小余项"——这是定义 12.13 的直接模板，也是你以后理解 Taylor 展开、数值微分误差分析的锚点（CSAPP 数值方法里截断误差的语言与此完全相同）。顺带注意脚注：$L(x)=a_0x+a_1$ 是"仿射"而非"线性"（线性要求 $a_1=0$），可微性线性逼近的是**增量** $f(x)-f(x_0)$ 而非 $f$ 本身——这个区分在 Strang 里同样重要（线性映射 vs 平移）。

---

我们将为多变量函数模仿上述做法。

为了暂时简化记号，我们先考虑在点 $(x_0, y_0) \in \mathbb{R}^2$ 的某个邻域内定义的两个变量的函数。

我们希望表达这样的条件：与方程 $z = f(x, y)$ 对应的曲面在 $(x_0, y_0)$ 处有一个切平面（tangent plane）。

于是切平面 $T$ 取代了单变量函数情形中的切线。

<!-- ===== 书页 482 ===== -->

从初等微积分回忆起，切平面（若存在）可以用线性方程

```math
T(x, y) = f(x_0, y_0) + f_1(x_0, y_0)(x - x_0) + f_2(x_0, y_0)(y - y_0)
```

来表示。

为了使这个平面成为切平面，我们要求 (22) 的类比成立，即当 $(x, y) \to (x_0, y_0)$ 时

```math
\frac{|f(x, y) - T(x, y)|}{\sqrt{(x - x_0)^2 + (y - y_0)^2}} \to 0. \tag{24}
```

像处理 (22) 那样处理 (24)，并记 $h = x - x_0$，$k = y - y_0$，我们便得到二变量版本的正确表述。

<span style="color:#2471a3;">**[definition]**</span> **<span style="color:#00838f;">定义 12.13：函数 $f : \mathbb{R}^2 \to \mathbb{R}$ 在 $(x_0, y_0)$ 处可微（differentiable），若满足</span>**

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定义 12.13 是本章最重要的定义：$f(x_0+h,y_0+k)-f(x_0,y_0)=f_1h+f_2k+\varepsilon(h,k)\sqrt{h^2+k^2}$，其中 $\varepsilon\to0$。它的话翻译过来是：**增量 = 梯度点积位移（线性主部）+ 高阶小余项**。我命名验证方法为「$o(\|h\|)$ 判据」：要证可微，就把 $\varepsilon$ 定义为"（增量 − 线性主部）除以范数"，再证这个商趋于 0。三个即时推论值得记牢：可微 ⟹ 连续（令 $h,k\to0$ 余项消失）；可微 ⟹ 偏导存在（令 $k=0$ 只剩 $f_1$ 的差商）；但反过来都不行——例 11.42 展示"偏导存在却不连续"，例 12.15 展示"连续且有偏导却不可微"。注记中 (2') 用 $|h|+|k|$ 代替 $\sqrt{h^2+k^2}$ 之所以合法，是因为 $\sqrt{h^2+k^2}\le|h|+|k|\le\sqrt2\sqrt{h^2+k^2}$——这正是引理 11.34 范数等价在二维的具体化，也是教材说"用 $\|\cdot\|_1$ 范数能简化证明"的原因。跨课程：$f_1h+f_2k$ 就是梯度 $\nabla f$ 与位移 $(h,k)$ 的点积，Strang 会把它解读为"可微 = 梯度给出的最佳线性逼近"。

---

1. **<span style="color:#00838f;">偏导数（partial derivatives）$f_1$ 与 $f_2$ 在 $(x_0, y_0)$ 处存在。</span>**

2. **<span style="color:#00838f;">可以写成</span>**

```math
f(x_0 + h, y_0 + k) - f(x_0, y_0) = f_1(x_0, y_0)h + f_2(x_0, y_0)k + \varepsilon(h, k)\sqrt{h^2 + k^2}, \tag{25}
```

其中当 $\sqrt{h^2 + k^2} \to 0$ 时 $\varepsilon(h, k) \to 0$（并规定 $\varepsilon(0, 0) = 0$）。

<span style="color:#2471a3;">**[note]**</span> **<span style="color:#1e8449;">注（Note）。</span>** 观察到对 $(h, k) \in \mathbb{R}^2$ 有

```math
\sqrt{h^2 + k^2} \le |h| + |k| \le \sqrt{2}\,\sqrt{h^2 + k^2},
```

由此我们可以把定义中的条件 (2) 改写成更简单的形式：

<span style="color:#7d3c98;">$2'$：可以写成</span>

```math
f(x_0 + h, y_0 + k) - f(x_0, y_0) = f_1(x_0, y_0)h + f_2(x_0, y_0)k + \varepsilon(h, k)(|h| + |k|), \tag{26}
```

其中当 $|h| + |k| \to 0$ 时 $\varepsilon(h, k) \to 0$。

条件 $|h| + |k| \to 0$ 等价于 $h \to 0$ 且 $k \to 0$，而这又等价于 $\sqrt{h^2 + k^2} \to 0$。

让我们暂时回到切平面作用背后的初等几何。

这个平面应当在 (24) 的意义下在 $(x_0, y_0)$ 附近逼近 $f$。

粗略地说，这要求当 $(x, y)$ 靠近 $(x_0, y_0)$ 时，$|f(x, y) - T(x, y)|$ 相对于 $(x, y)$ 与 $(x_0, y_0)$ 之间的距离而言是小的。

仅仅在 $(x_0, y_0)$ 处存在偏导数并不能保证这一点；

那只能保证当 $(x, y)$ 靠近 $(x_0, y_0)$ 且 $x = x_0$（或 $y = y_0$）时，所期望的比较是小的。

在曲面 $z = f(x, y)$ 与平面 $x = x_0$（或 $y = y_0$）的交线中，恰当的切线确实存在，但当 $(x, y)$ 以其他方式趋于 $(x_0, y_0)$ 时，(24) 未必成立。


<!-- ===== W24 ===== -->

# W24 · 书页 483–484 译文（§12.4 可微函数结尾）

> 本部分为全 PDF 的最后两页（书页 483–484，对应 PDF 页 499–500），覆盖 §12.4 收尾：图 12.3、例 12.14、例 12.15、§12.4 末段「对 $f: \mathbb{R}^n \to \mathbb{R}$ 的可微性」及定义 12.16 与随后的注记。经核验，这两页均为正文、定义、例子与定义性注记，**不含习题区**，故无需灰色跳过标注；文中对习题的交叉引用（习题 12.4.1 / 12.4.2 / 12.4.3）照常翻译。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定义 12.16 把可微性推广到 $n$ 元：$f(x+h)-f(x)=\sum_{i=1}^n f_i(x)h_i+\varepsilon\|h\|$，$\varepsilon\to0$。对照定义 12.13，只做了两处机械替换：二维的 $f_1h+f_2k$ 变成和式 $\sum f_ih_i=\nabla f\cdot h$（梯度与位移的内积），$\sqrt{h^2+k^2}$ 变成欧氏范数 $\|h\|$。注记再次强调可用 $\|\cdot\|_1$ 范数（$|h_1|+\cdots+|h_n|$）替代，因为有限维范数等价（引理 11.34 之后）——"换尺子不换可微性"，这与第 11 章"换范数不换收敛"一脉相承。第一性原理：可微 = "存在线性映射 $L=\nabla f(x)$（梯度看作 $1\times n$ 矩阵，是 Jacobian 的特例）使 $f(x+h)\approx f(x)+Lh$ 且误差是 $o(\|h\|)$"——这正是 Strang"微分是线性映射"的严格化，也是你未来学微分流形、泛函分析时"导数 = 线性算子"观念的种子。注意 $n=1$ 时定义自动退化为普通导数（$\sum f_ih_i=f'(x)h$），所以定义 12.16 是"统一"而非"新"——数学里最好的推广，是让旧定义变成新定义的特例。

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 例 12.15 是"采样不足"的完美标本：$f(x,y)=\sqrt{|xy|}$ 在原点连续、$f_1=f_2=0$，但不可微。检验方法是沿直线 $x+y=0$（即 $h=-k$）逼近：$\sqrt{|hk|}=\varepsilon(|h|+|k|)$ 强制 $\varepsilon=\frac12$ 恒成立，永远不 $\to0$。几何直觉：图像像"沿两条坐标轴折叠的餐巾"，折痕上的信息（$f_1=f_2=0$）只告诉你沿两条轴方向是平的，却测不到对角方向的陡峭褶皱——沿 $(\frac1{\sqrt2},-\frac1{\sqrt2})$ 方向的方向导数甚至不存在（差商 $\frac{|t|/\sqrt2}{t}$ 在 $t>0$ 与 $t<0$ 时分别趋向 $\pm\frac1{\sqrt2}$，双侧极限不存在）。这个例子连着两层教训：其一，**偏导存在推不出方向导数存在**（方向导数是更强的对象）；其二，**可微 ⟹ 所有方向导数存在且 $D_uf=\nabla f\cdot u$**（线性地依赖方向），所以定义 12.13 的"所有方向同时拟合"正是为杜绝这种折痕而设。与 CSAPP 类比：只沿坐标轴采样，就像只测两个极端输入的性能，永远无法推断一般行为。

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 例 12.14 的价值不在计算本身，而在它揭示的"成本—收益"规律：椭球面 $f(x,y)=\frac13\sqrt{36-4x^2-y^2}$ 按定义验证可微是"繁琐计算"（教材明说"只要我们再稍加努力"），实践中我们更想用自动工具——教材预告了定理 12.21：**偏导数连续（$C^1$）⟹ 可微**，这正是对例 11.42 漏洞的正式修复，也是 Rudin 第 9 章的核心武器。第一性原理：数学发展遵循"先用定义建立真理，再总结自动工具替代手工劳动"的规律——就像 CSAPP 里先用指令集原语、再构建高级语言抽象，层层封装。为什么 $C^1$ 就够？因为连续偏导让切平面两侧的误差被"均匀控制"，避免了例 12.15 那种"折痕"。跨课程：这个椭球面是 Strang 二次型几何的实例，你可以手算 $f_1=\frac{-4x}{3\sqrt{36-4x^2-y^2}}$、$f_2=\frac{-y}{3\sqrt{36-4x^2-y^2}}$ 在 $(1,3)$ 处的值，验证切平面 $z=z_0+f_1(x-1)+f_2(y-3)$ 确实是"最佳仿射逼近"——(24) 式把"切"字精确化为"误差比距离更快趋于 0"。

---

---

## 第 483 页（书页 483 · §12.4 可微函数 Differentiable Functions）

<span style="color:#2471a3;">**[figure]**</span> **图 12.3**：函数 $f(x, y) = \frac{1}{3}\sqrt{36 - 4x^2 - y^2}$ 在点 $\left(1, 3, \frac{\sqrt{23}}{3}\right)$ 处的 tangent plane（切平面）。

<span style="color:#2471a3;">**[example]**</span> **例 12.14**：再次考虑来自例 12.1 的函数

```math
f(x, y) = \frac{\sqrt{36 - 4x^2 - y^2}}{3}
```

在图 12.1 中，我们展示了该函数在点 $(x_0, y_0, z_0) = \left(1, 3, \frac{\sqrt{23}}{3}\right)$ 处的 tangent lines（切线）。

现在，只要我们再稍加努力，通过按定义逐步完成那些计算，验证切平面以正确的意义逼近该函数，就可以证明此函数在该点是 differentiable（可微）的。

图 12.3 展示了这个切平面，并说明这种逼近是合理的。

在实践中，我们通常会援引某个定理（例如 Theorem 12.21（定理 12.21）），从而不必诉诸此类繁琐计算即可断定可微性。

$\square$

<span style="color:#2471a3;">**[example]**</span> **例 12.15**：设 $f(x, y) = \sqrt{|xy|}$。

（这个函数让人联想到函数 $\sqrt{|x|} = \sqrt{|x^2|}$，后者在 $x = 0$ 处 continuous（连续）但不可微。）

> <span style="color:#7f8c8d">*译者注：原书此处「$\sqrt{|x|} = \sqrt{|x^2|}$」并非严格等式——事实上 $\sqrt{|x^2|} = |x|$。作者意在借单变量函数「$\sqrt{|x|}$（或 $|x|$）在 $x = 0$ 处连续但不可微」这一事实作类比，读者不必拘泥于该等号本身。*</span>

显然 $f$ 在 $(0, 0)$ 处连续（习题 12.4.1）。

由于 $f$ 在 coordinate axes（坐标轴）上处处为零，因此

```math
f_1(0, 0) = f_2(0, 0) = 0.  \tag{27}
```

要使 $f$ 在 $(0, 0)$ 处可微，必须当 $|h| + |k| \to 0$ 时有 $\varepsilon(h, k) \to 0$，其中 $\varepsilon(h, k)$ 由下式定义：

```math
\sqrt{|hk|} = f_1(0, 0)h + f_2(0, 0)k + \varepsilon(h, k)(|h| + |k|).
```

由 (27) 可得 $\sqrt{|hk|} = \varepsilon(|h| + |k|)$。

例如令 $h = -k$，我们便得到 $|h| = 2\varepsilon|h|$，所以 $\varepsilon(h, -h) = \frac{1}{2}$。

由此可见，并不存在 $\varepsilon(h, k) \to 0$（当 $|h| + |k| \to 0$ 时）。

（令 $h = -k$ 等价于让 $(x, y)$ 沿着直线 $x + y = 0$（即 $z = 0$）趋近 $(x_0, y_0)$。）

图 12.4 展示了函数 $f$ 的 graph（图形），它显然形如一条沿两条轴折叠的餐巾（folded napkin）。

特别要注意，沿这些「折痕」所提供的信息——即 $f_1(0, 0) = f_2(0, 0) = 0$——并不能帮助我们计算方向 $\left(-\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$ 上的 directional derivative（方向导数）（图中已示出）。

而这一方向恰好对应于前面讨论过的 $h = -k$ 情形。

$\square$

## §12.4 结尾段：Differentiability for $f: \mathbb{R}^n \to \mathbb{R}$

<span style="color:#2471a3;">**[section]**</span> **对 $f: \mathbb{R}^n \to \mathbb{R}$ 的可微性（Differentiability for $f: \mathbb{R}^n \to \mathbb{R}$）**

有了这些准备工作，我们现在可以给出函数 $f: \mathbb{R}^n \to \mathbb{R}$ 可微性的正式定义。

这显然是把我们刚刚针对二元函数情形给出的 Definition 12.13（定义 12.13）加以直接推广。

---

## 第 484 页（书页 484 · 第 12 章 在 $\mathbb{R}^n$ 上的微分 Differentiation on $\mathbb{R}^n$）

<span style="color:#2471a3;">**[figure]**</span> **图 12.4**：函数 $f(x, y) = \sqrt{|xy|}$ 的图形，该函数在 $(0, 0)$ 处连续但 nondifferentiable（不可微）。

（接上页，继续定义 12.16 的陈述。）

<span style="color:#2471a3;">**[definition]**</span> **定义 12.16**：设 $f$ 定义在 open set（开集）$D \subset \mathbb{R}^n$ 上，并设 $x = (x_1, \ldots, x_n) \in D$。

若满足下列条件，则称 $f$ 在 $x$ 处可微：

**1.** partial derivatives（偏导数）$f_1, \ldots, f_n$ 在 $x$ 处全部存在（且有限）；且

**2.** 当 $\varepsilon = \varepsilon(h_1, \ldots, h_n)$ 由 $\varepsilon(0, \ldots, 0) = 0$ 及下式定义时：

```math
f(x_1 + h_1, \ldots, x_n + h_n) - f(x_1, \ldots, x_n) = \sum_{i=1}^{n} f_i(x_1, \ldots, x_n)h_i + \varepsilon\sqrt{h_1^2 + \cdots + h_n^2}
```

当 $\sqrt{h_1^2 + \cdots + h_n^2} \to 0$ 时，有 $\varepsilon(h_1, \ldots, h_n) \to 0$。

若 $f$ 在 $D$ 中所有点处都可微，则称 $f$ 在 $D$ 上可微。

<span style="color:#2471a3;">**[note]**</span> **注记**：定义中的陈述 (2) 是借助通常的 euclidean norm（欧几里得范数）给出的。

正如我们在定义 12.13 之后的注记中已经看到的（该注记针对 $\mathbb{R}^2$ 情形），使用 $\|\cdot\|_1$ norm（范数）往往能简化涉及可微性的证明。

习题 12.4.2 表明这样做是可行的。

改用 $\|\cdot\|_1$ 范数后，陈述 (2) 变为：

**$2'$** 当 $\varepsilon = \varepsilon(h_1, \ldots, h_n)$ 由下式定义时：

```math
f(x_1 + h_1, \ldots, x_n + h_n) - f(x_1, \ldots, x_n) = \sum_{i=1}^{n} f_i(x_1, \ldots, x_n)h_i + \varepsilon(|h_1| + \cdots + |h_n|)
```

且 $\varepsilon(0, \ldots, 0) = 0$，则当 $|h_1| + \cdots + |h_n| \to 0$ 时有 $\varepsilon \to 0$。

另见习题 12.4.3。

---

*（全 PDF 到此结束。以上为 W24 书页 483–484 的完整行内双语译文。）*
