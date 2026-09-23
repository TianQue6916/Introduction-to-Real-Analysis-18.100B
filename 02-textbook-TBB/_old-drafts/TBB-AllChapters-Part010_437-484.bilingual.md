# <span style="color:#c0392b;">Elementary Real Analysis（初等实分析）</span>

> <span style="color:#7f8c8d;">行内双语翻译 · Part010（书页 437–484）</span>
> <span style="color:#7f8c8d;">范围：第 11 章 The Euclidean Spaces R^n（欧几里得空间）全书正文 + 第 12 章 Differentiation on R^n（R^n 上的微分）§12.1–§12.4</span>
> <span style="color:#7f8c8d;">源文件：TBB-AllChapters-Portrait_part010_p451-500.pdf（书页 437–484 = PDF 页 453–500，即 书页 = PDF 页 − 16）</span>
> <span style="color:#7f8c8d;">Second Edition (2008) · Brian S. Thomson, Judith B. Bruckner, Andrew M. Bruckner</span>
> <span style="color:#7f8c8d;">**格式：** 中文主体 + `English term（中文翻译）` 嵌入 · 深红标题 · 蓝色标签 · fenced math block · 无英文原句</span>
> <span style="color:#7f8c8d;">**习题区**（各节 Exercises、Notes 提示区 p.435–436、466）按约定跳过不收录</span>
> <span style="color:#7f8c8d;">**译者注**：全书共 34 条，分散插入于对应定理/定义/例子之后（跨课程连接 · 第一性原理 · 证明模板 · 历史 · 拓展前沿）</span>
> <span style="color:#7f8c8d;">**波次流程**：24 翻译 worker → flashauto 审计 4 份 → dsh pro 写注 34 条 → flashauto 交叉引用 167 条 → dsh pro+max 超强审计（31 处意见已修复）→ flashauto 格式审计</span>

---

# 第 11 章 欧几里得空间 $\mathbb{R}^n$

<span style="color:#2471a3;">**[section]**</span> 在我们对分析学（analysis）的研究中已经观察到，实数系 $\mathbb{R}$ 不仅仅是一堆点的集合。

它具有各种代数（algebraic）、度量（metric）与序（order）结构，这些结构在学科的发展中扮演着角色。

许多其他重要的数学对象集合也是如此。

其中最重要的当属欧几里得空间（euclidean space）$\mathbb{R}^n$，这正是本章要研究的对象。

集合 $\mathbb{R}^n$ 的元素集合很容易描述：它就是所有实数的 $n$ 元组（n-tuple）构成的集合
```math
x = (x_1, \ldots, x_n).
```

我们将花一些时间建立一种自然的代数结构（空间 $\mathbb{R}^n$ 构成一个向量空间 vector space），以及一种自然的度量结构（其中有自然的距离 distance 概念），并会在本章与下一章中加以利用。

（虽然我们也可以在这些空间上施加序结构，但这类结构对我们的目的而言并不自然，因此不会进入我们的讨论。）

## 11.1 $\mathbb{R}^n$ 的代数结构

<span style="color:#2471a3;">**[section]**</span> 空间 $\mathbb{R}^n$ 由所有实数的 $n$ 元组 $x = (x_1, \ldots, x_n)$ 组成。

也就是说，$\mathbb{R}^n$ 是 $\mathbb{R}$ 的 $n$ 个副本的笛卡尔积（cartesian product）：
```math
\mathbb{R}^n = \mathbb{R} \times \mathbb{R} \times \cdots \times \mathbb{R}
```
（共 $n$ 个因子。）

$\mathbb{R}^n$ 的元素 $x$ 被称为 $\mathbb{R}^n$ 的点。

它们也可以被看作向量（vector），而 $\mathbb{R}$ 则可视为标量域（field of scalars）。

我们在 $\mathbb{R}^n$ 中把向量的加法定义为逐坐标加法（coordinate-wise addition）：若 $x = (x_1, \ldots, x_n)$，$y = (y_1, \ldots, y_n)$，则
```math
x + y = (x_1 + y_1, \ldots, x_n + y_n). \tag{1}
```

对于 $\alpha \in \mathbb{R}$ 与 $x = (x_1, \ldots, x_n) \in \mathbb{R}^n$，我们定义
```math
\alpha x = (\alpha x_1, \ldots, \alpha x_n). \tag{2}
```

我们将这种以标量乘以向量的乘法称为数乘（scalar multiplication）。

凭借这些加法与数乘的概念，$\mathbb{R}^n$ 便具有了向量空间（vector space）的代数结构。

这意味着定理 11.1 中所指出的那些性质均成立。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**定理 11.1（Theorem 11.1）.**</span> 若 $\mathbb{R}^n$ 上的加法与数乘分别由 (1) 与 (2) 定义，则对一切 $x, y, z \in \mathbb{R}^n$ 与一切 $\alpha, \beta \in \mathbb{R}$，下列结论成立：

> <span style="color:#1e8449;">**[note]**</span> **注 1** 把九个"显然"的性质编号成一条定理，是为了把逐坐标定义 (1)(2) 的"实现细节"换成"契约"：§11.2 定理 11.5–11.7 的证明只调用这九条与点积三性质，从不回头展开坐标。九条里的每一条你都能用一行坐标计算验证，但让它们同时出现在同一条定理里才是关键——这正是你在 6.042 学过的 closure（封闭性）加上八条运算律共同组成的"向量空间"接口。Strang 教材第 3 章用同一组公理把向量空间从 $\mathbb{R}^n$ 推广到矩阵空间与函数空间：公理不变，对象换了，定理照旧成立。你在 6.006 写的 element-wise（逐元素）数组加法与数乘，正是 (1)(2) 的机器实现，NumPy 的向量化运算就是这套代数结构的工程化身。所以这九条不是哲学装饰，而是"后续定理不依赖坐标系"的许可证：定理 11.5 的证明连坐标都没有展开。

- $x + y$ 与 $\alpha x$ 均在 $\mathbb{R}^n$ 中（$\mathbb{R}^n$ 关于加法与数乘的封闭性 closure）
- $x + y = y + x$（交换律 commutative law）
- $(x + y) + z = x + (y + z)$（结合律 associative law）
- $x + 0 = x$，其中 $0 = (0, \ldots, 0)$
- $\alpha(x + y) = \alpha x + \alpha y$（分配律 distributive law）
- $(\alpha + \beta)x = \alpha x + \beta x$（分配律）
- $\alpha(\beta x) = (\alpha \beta)x$
- $0x = 0$
- $1x = x$

<span style="color:#2471a3;">**[note]**</span> 定理 11.1 的证明只不过是对每条陈述逐一核验的简单练习。

我们把它留作 Exercise 11.1.1。

我们还注意到，若通过
```math
x - y = x + (-1)y
```
定义减法，则 $x - x = 0$。

我们还可以用 $-x$ 表示 $(-1)x$，用 $x/\alpha$ 表示 $(1/\alpha)x$。

## 点积（The Dot Product）

> <span style="color:#1e8449;">**[note]**</span> **注 2** dot product（点积）$x\cdot y=\sum_i x_i y_i$ 用一个公式同时编码两件事：长度（$x\cdot x=\|x\|^2$，定义 11.3 直接用它）与夹角（下一节的定理 11.5 会证明比值 $x\cdot y/(\|x\|\|y\|)$ 落在 $[-1,1]$，那正是 $\cos\theta$ 的合法定义）。定理 11.2 的三条性质全部可以机械展开和式验证，其中分配律用到的只是 6.042 里的有限双重求和重排——有限性保证求和次序随便换，不需要任何分析条件。定义里最反直觉的一句是 $x\cdot y$ 可以在 $x,y$ 都非零时为 0，如 $(1,1)\cdot(1,-1)=0$：inner product（内积）不是普通乘法，实数的"零因子律"（乘积为 0 必有一个因子为 0）在这里失效，所以不能从 $x\cdot y=0$ 两边"约去" $x$。orthogonal vectors（正交向量）的价值在于它把"垂直"从画得出来的二、三维推广到画不出的高维：判据只剩一条代数等式 $x\cdot y=0$。Strang 4.4 节的 Gram-Schmidt（格拉姆-施密特正交化）与机器上的 QR 分解，正是靠这条判据在任意维数里制造正交基。

<span style="color:#2471a3;">**[section]**</span> 我们将需要两个向量 $x$ 与 $y$ 的点积（dot product）概念。

它由下式定义：
```math
x \cdot y = x_1 y_1 + \cdots + x_n y_n, \tag{3}
```
其中 $x = (x_1, \ldots, x_n)$，$y = (y_1, \ldots, y_n)$。

注意点积 (3) 是一个标量。

正因为如此，$x \cdot y$ 有时被称为 $x$ 与 $y$ 的标量积（scalar product）。

它有时也被称为 $x$ 与 $y$ 的内积（inner product）。

点积满足某些条件，我们将这些条件总结在定理 11.2 中。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**定理 11.2（Theorem 11.2）.**</span> 若 $x, y, z \in \mathbb{R}^n$ 且 $\alpha \in \mathbb{R}$，则

- $x \cdot y = y \cdot x$（交换律）
- $x \cdot (y + z) = x \cdot y + x \cdot z$（分配律）
- $(\alpha x) \cdot y = \alpha (x \cdot y)$。

我们把这个证明留作 Exercise 11.1.2。

<span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f;">注意 $0 \cdot x = 0$，但 $x \cdot y$ 可以在 $x$ 与 $y$ 都非零时等于 $0$【例如在 $\mathbb{R}^2$ 中，$(1, 1) \cdot (1, -1) = 1 - 1 = 0$】。</span>

<span style="color:#00838f;">满足 $x \cdot y = 0$ 的两个非零向量 $x$ 与 $y$ 被称为正交向量（orthogonal vectors）。</span>

从几何上看，$\mathbb{R}^n$ 中两个正交向量是垂直（perpendicular）的。

<span style="color:#7f8c8d">*（本页其余部分为 11.1 节习题区，按约定跳过。）*</span>

---

<span style="color:#7f8c8d">*（本页顶部行 2–28 为 §11.1 习题区，含习题 11.1.6 等小题，按约定跳过；该区内的 Figure 11.1 图为 §11.2 正文所引用，其说明文字照常翻译如下。）*</span>

<span style="color:#2471a3;">**[figure]**</span> **Figure 11.1.** 向量、距离与 $\mathbb{R}^2$ 中的范数（Vectors, distance, and norm in $\mathbb{R}^2$）：图中自原点出发的向量 $x$ 与 $y$ 以箭头示出，其长度即范数 $\|x\|$ 与 $\|y\|$；向量差 $y - x$ 由 $x$ 指向 $y$，其长度 $\|y - x\| = d(x, y)$ 正是两点之间的欧几里得距离。

### <span style="color:#2471a3;">**[section]**</span> §11.2 空间 $\mathbb{R}^n$ 的度量结构（The Metric Structure of $\mathbb{R}^n$）

空间 $\mathbb{R}^n$ 拥有两点之间距离（distance）的自然概念。

距离这一概念对于序列收敛（convergence）、极限（limit）、连续性（continuity）以及微分（differentiation）等概念而言是基础性的。

我们的出发点是 $\mathbb{R}^n$ 中向量的范数（norm）$\|x\|$。

<span style="color:#2471a3;">**[definition]**</span> **定义 11.3（Definition 11.3）**：<span style="color:#00838f;">设 $x = (x_1, \ldots, x_n) \in \mathbb{R}^n$，我们定义其欧几里得范数（euclidean norm）为</span>

```math
\|x\| = \sqrt{\sum_{i=1}^{n} x_i^2}.
```

注意，对一切 $x \in \mathbb{R}^n$ 都有 $\|x\| \geq 0$。

在熟悉的 $n = 1, 2, 3$ 情形中，$\|x\|$ 恰好就是 $x$ 与零向量 $0$ 之间的距离。

[例如在 $\mathbb{R}^2$ 中，若 $z = (x, y)$，则 $\|z\| = \sqrt{x^2 + y^2}$。]

这提示了 $\mathbb{R}^n$ 中向量 $x$ 与 $y$ 之间距离的如下定义（图 11.1）。

<span style="color:#2471a3;">**[definition]**</span> **定义 11.4（Definition 11.4）**：<span style="color:#00838f;">对于 $x, y \in \mathbb{R}^n$，$x$ 与 $y$ 之间的欧几里得距离（euclidean distance）定义为</span>

```math
d(x, y) = \|x - y\|.
```

用坐标表示，设 $x = (x_1, \ldots, x_n)$、$y = (y_1, \ldots, y_n)$，则

```math
\|x - y\| = \sqrt{(x_1 - y_1)^2 + \cdots + (x_n - y_n)^2}.
```

注意，我们能够通过点积（dot product）来表达范数：

```math
\|x\|^2 = x \cdot x \quad \text{或} \quad \|x\| = \sqrt{x \cdot x}.
```

---

<span style="color:#2471a3;">**[section]**</span> **书页 440（接上页，§11.2 续）**

正因如此，许多范数计算通过使用点积而得到简化。

点积与范数之间的一个重要关系由 Cauchy-Schwarz 不等式（Cauchy-Schwarz inequality）给出。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**定理 11.5（Theorem 11.5，Cauchy-Schwarz）**</span>：对于 $x, y \in \mathbb{R}^n$，

> <span style="color:#1e8449;">**[note]**</span> **注 4** 把定理 11.5 两边同除以 $\|x\|\|y\|$（$x,y$ 非零）得 $-1\le x\cdot y/(\|x\|\|y\|)\le 1$：一个夹在 $[-1,1]$ 里的数，衡量两个方向的一致程度，这就是注 2 预告的夹角定义；等号成立当且仅当 $x,y$ 共线（成比例）。这个结构可以原样移植到你大二上的 6.431 概率论（Bertsekas & Tsitsiklis 第 4.2 节 Covariance and Correlation，协方差与相关系数）：把有限和 $x\cdot y=\sum_i x_i y_i$ 换成中心化变量的期望 $\langle X,Y\rangle=E[XY]$，三条点积性质照常成立。于是 $|E[XY]|\le\sqrt{E[X^2]E[Y^2]}$ 就是定理 11.5 的逐字变体，相关系数 $\rho(X,Y)\in[-1,1]$ 的证明在 6.431 里会与你在这里读到的完全同构——学到那里时可以回来对照这一页。同一结构在信息检索里就是 cosine similarity（余弦相似度）：把文档编码成词频向量，用夹角余弦度量两篇文档的相似程度，这是你日后机器学习课程的常客。为什么一个有限维不等式能远征到概率与检索？因为证明只用内积三公理、从不依赖坐标——注 1 的接口设计在跨领域复用中兑现。

> <span style="color:#1e8449;">**[note]**</span> **注 3** Cauchy-Schwarz inequality（柯西-施瓦茨不等式）的证明值得存为模板："二次非负判别式法"。要证 $|x\cdot y|\le\|x\|\|y\|$，构造辅助二次式 $p(t)=(x-ty)\cdot(x-ty)=\|x\|^2-2(x\cdot y)t+\|y\|^2t^2$；由定义 $p(t)\ge 0$ 对一切 $t$ 成立，于是开口向上的抛物线至多有一个根，判别式 $\Delta=4(x\cdot y)^2-4\|x\|^2\|y\|^2\le 0$，移项开方即得（$y=0$ 时结论平凡，可先排除）。这个模板的通用步骤只有两步：把要证的内积不等式翻译成"某个 $p(t)\ge 0$"，再用判别式收口——日后凡遇到含 $\|x\pm ty\|^2$ 的估计都可照搬。历史上它是三次独立发现：Cauchy（柯西）1821 年在《Cours d'analyse》中给出有限和形式；Bunyakovsky（布尼亚科夫斯基）1859 年用极限过渡陈述积分形式；Schwarz（施瓦茨）1888 年重新发现一般形式，故西方称 Cauchy-Schwarz，俄语文献则称 Bunyakovsky 不等式。注意这个证明连坐标都没有展开——注 1 的公理打包在这里第一次兑现回报。

```math
|x \cdot y| \leq \|x\| \, \|y\|.
```

<span style="color:#2471a3;">**[proof]**</span> **证明**：首先观察，若 $t \in \mathbb{R}$，则

```math
p(t) = (x - ty) \cdot (x - ty) \geq 0. \tag{4}
```

利用定理 11.2，可将 (4) 改写为

```math
p(t) = x \cdot x - 2(x \cdot y)t + (y \cdot y)t^2 \geq 0. \tag{5}
```

函数 $p(t)$ 是关于 $t$ 的二次多项式（quadratic）。

由于它对一切 $t$ 非负，它不可能有两个不同的根（distinct roots）。

因此其判别式（discriminant）不可能为正，即

```math
4(x \cdot y)^2 - 4(x \cdot x)(y \cdot y) \leq 0. \tag{6}
```

现在由 (6) 推出

```math
(x \cdot y)^2 \leq (x \cdot x)(y \cdot y),
```

于是

```math
|x \cdot y| \leq \|x\| \, \|y\|,
```

正如所要证明的。$\square$

Cauchy-Schwarz 不等式使我们可以获得范数以及距离（distance，通常也称为度量 metric）的一些重要性质。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**定理 11.6（Theorem 11.6，范数性质 Norm Properties）**</span>：设 $x, y \in \mathbb{R}^n$，$\alpha \in \mathbb{R}$，则

> <span style="color:#1e8449;">**[note]**</span> **注 5** norm（范数）的三条公理——(i) 正定性、(ii) 齐次性、(iii) triangle inequality（三角不等式）——是"长度"的最小契约，一条都不能删：删 (i) 就无法用 $\|x-y\|=0$ 判定两点重合；删 (ii) 缩放图形就会改变形状；删 (iii) 则 $\varepsilon$ 论证无处安身，因为收敛证明全靠三角不等式把总误差拆成可控的小块。为什么长度取平方和开方，而不是 $|x_1|+\cdots+|x_n|$？两者都满足三公理（习题 11.2.6 与 11.2.7 会验证 $\|x\|_1=\sum_i|x_i|$ 与 $\|x\|_\infty=\max_i|x_i|$ 也是范数），但只有平方和版本由点积 $x\cdot x$ 生成，因而携带夹角信息，且旋转不改变长度——这就是 Strang 里正交矩阵满足 $\|Qx\|=\|x\|$ 的 $n$ 维来源。定理 11.6(iii) 的证明示范了"平方去根号法"：两边非负，$\|x+y\|\le\|x\|+\|y\|$ 等价于 $\|x+y\|^2\le(\|x\|+\|y\|)^2$，平方后根号消失，Cauchy-Schwarz 一步收口，高数里所有含根号的不等式都走这条路。$n=1$ 时三公理退化为绝对值的性质（$|x|\ge0$、$|\alpha x|=|\alpha||x|$、$|x+y|\le|x|+|y|$），所以 $\mathbb{R}^n$ 的收敛理论是 $\mathbb{R}$ 的直接复制。该不等式对 $p$ 范数 $\|x\|_p=(\sum_i|x_i|^p)^{1/p}$ 的推广以 Hermann Minkowski（明可夫斯基，1864–1909）命名，$p=2$ 时就是三角不等式。

(i) $\|x\| \geq 0$，且 $\|x\| = 0$ 当且仅当（if and only if）$x = 0$。

(ii) $\|\alpha x\| = |\alpha| \, \|x\|$。

(iii) $\|x + y\| \leq \|x\| + \|y\|$（三角不等式 triangle inequality）。

<span style="color:#2471a3;">**[proof]**</span> **证明**：(i) 与 (ii) 的证明是直接的。

为证明 (iii)，我们计算

```math
\|x + y\|^2 = (x + y) \cdot (x + y) = \|x\|^2 + 2x \cdot y + \|y\|^2 \leq \|x\|^2 + 2\|x\|\|y\| + \|y\|^2 = (\|x\| + \|y\|)^2,
```

其中的不等式由 Cauchy-Schwarz 不等式得出【译者注：原文此处印作 $(\|x\|^2+\|y\|^2)^2$，应为 $(\|x\|+\|y\|)^2$】。$\square$

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**定理 11.7（Theorem 11.7，度量性质 Metric Properties）**</span>：距离函数

> <span style="color:#1e8449;">**[note]**</span> **注 6** 定理 11.7 把距离抽象成三条公理：非负且 $d(x,y)=0$ 当且仅当 $x=y$、对称、三角不等式——注意第 11.3 节的全部拓扑概念只认这三条，不认 $\|x-y\|$ 的具体公式，这是把"实现"换成"接口"的又一次实操。欧几里得距离还有一个许多度量没有的隐藏性质：平移不变性 $d(x+z,y+z)=d(x,y)$，它来自 $d(x,y)=\|x-y\|$ 的"差结构"，也是整个理论可以随处搬家的原因。度量公理并不只属于连续世界：Hamming distance（汉明距离）——两个二进制串相异位的个数——满足这三条，非负、对称、三角不等式都可逐位验证。Richard Hamming（汉明，1915–1998）1950 年在《Error detecting and error correcting codes》中用"以码字为中心的开球互不相交"量化纠错能力：码字间最小距离 $\ge 2t+1$ 就能纠正 $t$ 位错误。你在 CSAPP 第 6 章「存储层次结构」读到的 ECC（error-correcting code，纠错码）——磁盘与内存用冗余位检测并纠正比特翻转——背后的几何正是这套汉明球，拓扑语言原封不动变成编码语言。

```math
d : \mathbb{R}^n \times \mathbb{R}^n \to \mathbb{R}
```

对一切 $x, y, z \in \mathbb{R}^n$ 满足下列条件。

(i) $d(x, y) \geq 0$，且 $d(x, y) = 0$ 当且仅当 $x = y$。

<span style="color:#7f8c8d">*（本页原文至此结束，定理 11.7 的其余条件与证明见下一页。）*</span>

---

# 书页 441 — 第 11.2 节（定理 11.7 证明收尾与正文段落）

### 第 11.2 节 $\mathbb{R}^n$ 的度量结构（The Metric Structure of $\mathbb{R}^n$）

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**定理 11.7（续，定理完整陈述始于上一页）**</span>

（ii）$d(x,y)=d(y,x)$（对称性，symmetry）。

（iii）$d(x,z)\le d(x,y)+d(y,z)$（三角不等式，triangle inequality）。

<span style="color:#2471a3;">**[proof]**</span> **证明。**

同样地，（i）与（ii）的证明都是显然的。为验证（iii），令 $u=x-y$，$v=y-z$。于是 $u+v=x-z$。由定理 11.6 的（iii）可见
```math
\|u+v\|\le\|u\|+\|v\|
```
即
```math
\|x-z\|\le\|x-y\|+\|y-z\|
```
而这正是陈述 $d(x,z)\le d(x,y)+d(y,z)$。$\square$

在习题 11.2.6 与 11.2.7 中，我们将在 $\mathbb{R}^n$ 上引入另外两种范数，并找出它们之间的一些比较关系。稍后，习题 11.3.8 与 11.4.1 将展示，在处理与开集（open set）、闭集（closed set）及收敛直接相关的概念时，这些范数可以互换使用的若干途径。因此，尽管本节所遇到的欧几里得范数（euclidean norm）是我们的主要关注点，其他范数也可以同时使用，以便简化并澄清论证。

<span style="color:#7f8c8d">*（本页其余部分为 §11.2 习题区，含 Exercises 11.2.1–11.2.6，按约定跳过。）*</span>

---

# 书页 442 — 第 11.3 节正文

<span style="color:#7f8c8d">*（本页前部为 §11.2 习题区，含 Exercises 11.2.7 与 11.2.8，按约定跳过。）*</span>

### 第 11.3 节 $\mathbb{R}^n$ 的初等拓扑（Elementary Topology of $\mathbb{R}^n$）

到目前为止，你已经理解距离（distance）概念在研究 $\mathbb{R}$ 时所起的基础性作用。事实上，开集的概念正是直接依据距离概念来定义的。其他各种重要概念，例如闭集、稠密集（dense set）与聚点（accumulation point），都直接或间接地依赖于距离概念。在 $\mathbb{R}^n$ 中，情形同样如此。在本节中，我们将定义其中一些重要概念。我们将看到，只要把 $\mathbb{R}$ 上通常的距离函数替换为 $\mathbb{R}^n$ 上的欧几里得距离函数（euclidean distance function），$\mathbb{R}^n$ 中的定义就与 $\mathbb{R}$ 中的完全相同。

设 $x_0\in\mathbb{R}^n$，并设 $r>0$。集合
```math
B(x_0,r)=\{x:\|x-x_0\|<r\}
```
称为以 $x_0$ 为中心、半径为 $r$ 的开球（open ball）。它也称为 $x_0$ 的 $r$-邻域（$r$-neighborhood）。它显然由 $\mathbb{R}^n$ 中那些到 $x_0$ 的距离小于 $r$ 的点组成。我们将以这一简单概念为基础，定义若干在我们研究 $\mathbb{R}$ 时已经熟悉的概念。

<span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f;">**1. 开集。** $\mathbb{R}^n$ 中的集合 $E$ 是开集，如果对每个 $x_0\in E$ 都存在一个对应的 $\varepsilon>0$，使得 $B(x_0,\varepsilon)\subset E$。</span>

包含点 $x_0$ 的开集也称为 $x_0$ 的邻域（neighborhood）。

<span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f;">**2. 闭集。** $\mathbb{R}^n$ 中的集合 $E$ 是闭集，如果 $\mathbb{R}^n\setminus E$ 是开集。</span>

<span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f;">**3. 聚点。** 设 $E\subset\mathbb{R}^n$。若点 $x_0\in\mathbb{R}^n$【原文作 $x_0\in E$，与定理 11.17、11.44 允许聚点位于 $E$ 外的用法矛盾，疑为原著笔误】满足：每个以 $x_0$ 为中心的开球都包含 $E$ 中异于 $x_0$ 的点，则称 $x_0$ 为 $E$ 的聚点（accumulation point），或称极限点（limit point）。</span>

> <span style="color:#1e8449;">**[note]**</span> **注 7** open set（开集）的定义"每个点 $x_0$ 都有 $\varepsilon>0$ 使 $B(x_0,\varepsilon)\subset E$"翻译成白话：每个点在自己的集合里都有"转身余地"，边界上没有站人，其中 $B(x_0,\varepsilon)$ 就是 open ball（开球）。closed set（闭集）被定义为"补集是开集"而不是"包含所有聚点"，这是定义经济学——让开集承担全部工作，闭集由补集免费获得，直到定理 11.18（闭当且仅当含全部聚点）两条路线才合流。用 $\mathbb{R}$ 里的老朋友验证：开区间 $(a,b)$ 开、闭区间 $[a,b]$ 闭、半开区间 $(a,b]$ 既不开也不闭；Example 11.11 的环 $1<x^2+y^2\le 2$ 正是 $(a,b]$ 的二维版，内圈一侧开、外圈一侧闭，边界由两个圆组成。Example 11.10 的 $\mathbb{Q}\times\mathbb{Q}$ 最值得亲手验证：它既不开也不闭，且 $\mathbb{R}^2$ 中每个点都是它的 accumulation point（聚点）与 boundary point（边界点），原因是你已学过的 $\mathbb{Q}$ 在 $\mathbb{R}$ 中稠密——任何开球里同时有有理点与无理点。6.042 的可数性结论在这里与"稠密"并存而不矛盾：$\mathbb{Q}$ 可数（对角线计数），却无处不在——"小"（基数意义）与"密"（拓扑意义）是两个正交的量度。本节末预告的 compactness（紧致性）要等 §11.8 才登场，届时它等价于"闭且有界"，而本节的三个概念正是那一定理的全部原材料。

我们将交替使用"聚点"与"极限点"这两个术语。

---

<span style="color:#2471a3;">**[section]**</span> §11.3 $\mathbb{R}^n$ 的基本拓扑学（Elementary Topology of $\mathbb{R}^n$）

<span style="color:#2471a3;">**[definition]**</span> **定义 4（Definition 4）。** 一个点 $x_0 \in \mathbb{R}^n$ 称为集合 $E \subset \mathbb{R}^n$ 的<span style="color:#00838f;">边界点（boundary point）</span>，如果对每个 $\varepsilon > 0$ 都有：

```math
B(x_0, \varepsilon) \cap E \ne \varnothing \quad \text{且} \quad B(x_0, \varepsilon) \setminus E \ne \varnothing
```

<span style="color:#2471a3;">**[definition]**</span> **定义 5（Definition 5）。** 集合 $E \subset \mathbb{R}^n$ 称为<span style="color:#00838f;">有界（bounded）</span>，如果存在 $M > 0$ 使得 $E \subset B(0, M)$。

我们在接下来的四个例子中列出 $\mathbb{R}^2$ 的一些子集，并指出它们分别具有前面哪些性质，验证留给你。

<span style="color:#2471a3;">**[example]**</span> **例 11.8（Example 11.8）.** x 轴 $E_1 = \{(x, y) \in \mathbb{R}^2 : y = 0\}$。$E_1$ 不是开集；$E_1$ 是闭集；$E_1$ 的每个点都是 $E_1$ 的聚点（accumulation point）和边界点；$E_1$ 无界。

<span style="color:#2471a3;">**[example]**</span> **例 11.9（Example 11.9）.** 令 $E_2 = \{(x, y) : x^2 + y^2 \le 1\}$。这个集合不是开集；它是闭集；$E_2$ 的每个点都是 $E_2$ 的聚点；$E_2$ 的边界点是那些满足 $x^2 + y^2 = 1$ 的点；$E_2$ 有界。

<span style="color:#2471a3;">**[example]**</span> **例 11.10（Example 11.10）.** 集合 $E_3 = \mathbb{Q} \times \mathbb{Q} = \{(x, y) : x, y \in \mathbb{Q}\}$ 既不是开集也不是闭集；$\mathbb{R}^2$ 中的每个点都是 $E_3$ 的聚点和边界点；$E_3$ 在 $\mathbb{R}^2$ 中无界。

<span style="color:#2471a3;">**[example]**</span> **例 11.11（Example 11.11）.** 环状区域（annular region）$E_4 = \{(x, y) : 1 < x^2 + y^2 \le 2\}$ 既不是开集也不是闭集；$\{(x, y) : 1 \le x^2 + y^2 \le 2\}$ 中的每个点都是 $E_4$ 的聚点；$E_4$ 的边界点是满足 $x^2 + y^2 = 1$ 或 $x^2 + y^2 = 2$ 的那些点 $(x, y)$；$E_4$ 有界。

我们在 $\mathbb{R}$ 中定义的其他术语可以用同样的方式在 $\mathbb{R}^n$ 中定义。

例如，孤立点（isolated point）、稠密集（dense set）和无处稠密集（nowhere dense set）这些概念，可以完全按照在 $\mathbb{R}$ 中相同的方式在 $\mathbb{R}^n$ 中定义。

我们在本章余下部分以及下一章中的展开，将主要处理 $\mathbb{R}^n$ 中的开集或闭集。

我们把这些概念以及其他概念的讨论留给习题。

紧致性（compactness）的概念对我们的展开同样重要。

我们将在第 11.8 节讨论紧致性。

若干把本节各概念联系起来的结论出现在习题中，它们与我们为 $\mathbb{R}$ 已经指出的那些结论相类似。

<span style="color:#7f8c8d">*（本页其余部分为 §11.3 习题区（Exercises 11.3.1–11.3.3），按约定跳过。）*</span>

---

<span style="color:#7f8c8d">*（书页 444 为 §11.3 习题区，含习题 11.3.4–11.3.8，按约定跳过。）*</span>

## <span style="color:#2471a3;">**[section]**</span> 11.4 $\mathbb{R}^n$ 中的序列（Sequences in $\mathbb{R}^n$）

> <span style="color:#1e8449;">**[note]**</span> **注 8** $|x_j|\le\|x\|\le\sum_i|x_i|$ 是全节最重要的一行，值得追问它为什么必须成立：左半是"单个坐标的平方不超过平方和"再开方，右半是 $(a+b)^2\ge a^2+b^2$（$a,b\ge0$）的归纳推广。它把向量范数夹在"坐标大小"两杆之间，而全部力量来自 $n$ 有限：有限项的和与最大项只差常数倍，所以"每个坐标都小"与"范数小"等价——这就是下一小节定理 11.15 的引擎。把 $n$ 换成无穷会怎样？考察 $e_k=(0,\dots,0,1,0,\dots)$（第 $k$ 位为 1）：$k\to\infty$ 时每个坐标都趋于 0，但 $\|e_k\|=1$ 恒不趋于 0——逐坐标收敛不再推出范数收敛。这个反例不需要任何超出本节的概念，只需写出序列逐项验证，却精确标记了有限维与无限维的分界线：无限维里三明治的右端（无穷和 $\sum_i|x_{ki}-x_i|$）不再随 $k$ 自动趋于 0，上杆失效。学分析的正确习惯就是每次证明后追问一句："哪一步用到了有限性？"——这一问正是日后进入泛函分析时一切新工具的起点。

<span style="color:#1e8449">**[note]**</span> 我们关于实数序列所研究的许多结果都会推广到 $\mathbb{R}^n$ 中序列的情形。

事实上，$\mathbb{R}^n$ 中序列的许多证明与 $\mathbb{R}$ 中相应命题的证明几乎是完全相同的。

我们将这些证明的大部分留给习题处理。

只有当某个证明需要新的想法时，我们才会给出详细的证明。

<span style="color:#2471a3;">**[definition]**</span> <span style="color:#c0392b;">**定义 11.12（Definition 11.12）**</span>（$\mathbb{R}^n$ 中的点序列，sequence of points）：<span style="color:#00838f">$\mathbb{R}^n$ 中的点序列是一个函数 $f:\mathbb{N}\to\mathbb{R}^n$。</span>

与 $\mathbb{R}$ 中序列的情形相同，我们经常使用诸如 $\{x_k\}$ 这样的记号来表示 $\mathbb{R}^n$ 中的序列。

注意 $x$ 是粗体（表示向量），而 $k$ 不是粗体，因为它表示自然数。

如果更方便，我们也可以用双下标记号（double subscript notation）把序列改写成一个 $n$ 元组（n-tuple）：

```math
x_k=(x_{k1},\ldots,x_{kn}).
```

<span style="color:#2471a3;">**[definition]**</span> <span style="color:#c0392b;">**定义 11.13（Definition 11.13）**</span>（$\mathbb{R}^n$ 中的有界序列，bounded sequence）：<span style="color:#00838f">$\mathbb{R}^n$ 中的序列 $\{x_k\}$ 是有界的（bounded），如果存在 $M\in\mathbb{N}$，使得对所有 $k\in\mathbb{N}$ 都有 $\|x_k\|\le M$。</span>

我们可以像对实数序列（见定义 2.6）那样，以完全相同的方式定义 $\mathbb{R}^n$ 中序列 $\{x_k\}$ 的收敛。

注意，在这里范数（norm）所起的作用与前面绝对值所起的作用相同。

<span style="color:#2471a3;">**[definition]**</span> <span style="color:#c0392b;">**定义 11.14（Definition 11.14）**</span>（收敛，convergence）：设 $\{x_k\}$ 是 $\mathbb{R}^n$ 中的序列。

<span style="color:#00838f">若对每个 $\varepsilon>0$ 都存在 $N\in\mathbb{N}$，使得当 $k\ge N$ 时总有 $\|x_k-x\|<\varepsilon$，则称 $\{x_k\}$ 收敛到（converges to）点 $x$，并记作</span>

```math
\lim_{k\to\infty}x_k=x \quad\text{或}\quad x_k\to x\ (k\to\infty).
```

这个定义等价于如下要求：每个以 $x$ 为中心的开球（open ball）都包含该序列除有限项以外的所有项。

即对每个 $\varepsilon>0$ 存在 $N$，使得对所有 $k\ge N$ 都有 $x_k\in B(x,\varepsilon)$。

它也等价于当 $k\to\infty$ 时 $\|x_k-x\|\to 0$ 或 $d(x_k,x)\to 0$ 这一要求，其中 $d$ 是欧几里得距离（euclidean distance）。

**坐标方式收敛（Coordinate-Wise Convergence）** 我们还可以用坐标方式收敛来描述 $\mathbb{R}^n$ 中的收敛。

为了看清这一点，首先注意到，对 $x=(x_1,\ldots,x_n)$ 以及 $j=1,\ldots,n$ 有

```math
x_j^2 \le \sum_{i=1}^n x_i^2=\|x\|^2 \le \left(\sum_{i=1}^n |x_i|\right)^2.
```

于是

```math
|x_j|\le\|x\|\le\sum_{i=1}^n |x_i|.\tag{7}
```

现在设 $\{x_k\}=\{(x_{k1},\ldots,x_{kn})\}$ 是 $\mathbb{R}^n$ 中的序列，并设 $x=(x_1,\ldots,x_n)$ 是 $\mathbb{R}^n$ 中的点。

由 (7) 可得

```math
|x_{kj}-x_j|\le\|x_k-x\|\le\sum_{i=1}^n |x_{ki}-x_i|.\tag{8}
```

若当 $k\to\infty$ 时 $x_k\to x$，即当 $k\to\infty$ 时 $\|x_k-x\|\to 0$，那么由 (8) 可见，对每个 $j=1,\ldots,n$，当 $k\to\infty$ 时 $|x_{kj}-x_j|\to 0$。

反过来，若对每个 $j=1,\ldots,n$ 都有当 $k\to\infty$ 时 $|x_{kj}-x_j|\to 0$，则当 $k\to\infty$ 时 $\sum_{i=1}^n |x_{ki}-x_i|\to 0$，于是再次由 (8) 可见当 $k\to\infty$ 时 $\|x_k-x\|\to 0$。

我们把这番讨论总结为如下定理。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**定理 11.15（Theorem 11.15）**</span>：设 $\{x_k\}=\{(x_{k1},\ldots,x_{kn})\}$ 是 $\mathbb{R}^n$ 中的序列，$x=(x_1,\ldots,x_n)\in\mathbb{R}^n$。

> <span style="color:#1e8449;">**[note]**</span> **注 9** coordinate-wise convergence（逐坐标收敛）说：向量序列收敛当且仅当 $n$ 个坐标序列分别收敛。判定一个 $n$ 维问题被拆成 $n$ 个一维判定、再用注 8 的三明治合并——这正是 6.006 分治策略在分析里的原型：规模 $n$ 拆成 $n$ 个规模 1 的子问题。你在 6.006 写过的逐元素数组操作就是逐坐标结构的机器实现，于是定理 11.16 的极限算律 (i)(ii) 等价于"极限可逐元素计算"，(iii) 则是"先逐项相乘再加总"的两层循环。定义 11.14 还给出收敛的第三个等价说法——每个以 $x$ 为中心的开球包含除有限项外的全部项——这是"尾项全部落袋"的拓扑表述，日后推广到一般度量空间靠的就是这一版。数值提醒：机器上判 $\|x_k-x\|<\varepsilon$ 时不要天真地平方求和再开方，大坐标平方溢出、小坐标平方下溢是 CSAPP 第 2 章浮点表示的教训；C 标准库（C99 起）的 hypot() 函数正是为安全计算 $\sqrt{x^2+y^2}$ 而设，自己写范数代码应先除以最大坐标再开方。

则 $\lim_{k\to\infty}x_k=x$ 当且仅当对每个 $j=1,\ldots,n$ 都有 $\lim_{k\to\infty}x_{kj}=x_j$。

**代数性质（Algebraic Properties）** 我们的下一个结果表明，极限关于加法、数乘（scalar multiplication）以及点积（dot product）运算按预期方式组合。

我们把证明留给习题 11.4.2。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**定理 11.16（Theorem 11.16）**</span>：设 $\{x_k\}$ 与 $\{y_k\}$ 是 $\mathbb{R}^n$ 中的序列，$\alpha\in\mathbb{R}$。

若 $\lim_{k\to\infty}x_k=x$ 且 $\lim_{k\to\infty}y_k=y$，则

```math
\begin{aligned}
\text{(i)}\quad \lim_{k\to\infty}(\alpha x_k)&=\alpha x,\\
\text{(ii)}\quad \lim_{k\to\infty}(x_k+y_k)&=x+y,\\
\text{(iii)}\quad \lim_{k\to\infty}(x_k\cdot y_k)&=x\cdot y.
\end{aligned}
```

**聚点（Limit Points）** 与在 $\mathbb{R}$ 中一样，在 $\mathbb{R}^n$ 中我们也可以借助序列的语言来刻画聚点。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**定理 11.17（Theorem 11.17）**</span>：设 $E\subset\mathbb{R}^n$，$x\in\mathbb{R}^n$。

> <span style="color:#1e8449;">**[note]**</span> **注 10** 定理 11.17 的证明值得存为模板："半距离收缩选取法"。先取 $x_1$ 使 $0<\|x_1-x\|<1$，之后每步取 $x_{k+1}$ 使 $0<\|x_{k+1}-x\|<\tfrac12\|x_k-x\|$，则 $\|x_k-x\|<2^{-(k-1)}$ 按几何级数收缩到 0。每步把到目标的距离减半，与 6.006 二分搜索每轮把搜索区间减半是同一个循环结构，你对 halving 的收敛速度（$k$ 轮后误差约为 $2^{-k}$）早已有直觉。为什么必须取"互异点"序列？这是定义强制：聚点可以不属于 $E$——例如 $E=\{1/k:k\in\mathbb{N}\}$ 的聚点 $0\notin E$——若允许重复项，常数序列只能落在 $E$ 内，永远到不了 $E$ 外面的聚点；Example 11.10 中 $\mathbb{R}^2$ 的每个点都是 $\mathbb{Q}^2$ 的聚点，同样是"外面的点也能被逼近"的例子。不等式 $0<\|x_{k+1}-x\|<\tfrac12\|x_k-x\|$ 一处严格小于同时完成三件事：新点异于 $x$、离 $x$ 更近、且异于之前所有点（到 $x$ 的距离严格递减）。用 6.042 的归纳法表述：假设已选出 $x_1,\dots,x_k$，聚点定义保证第 $k+1$ 步可选——归纳假设与存在性断言严丝合缝。

则 $x$ 是 $E$ 的聚点，当且仅当存在一个由 $E$ 中互异点组成的序列 $\{x_k\}$，使得 $\lim_{k\to\infty}x_k=x$。

---

<span style="color:#2471a3;">**[proof]**</span> 证明。设 $x$ 是 $E$ 的一个聚点（limit point）。

则对每个 $\varepsilon>0$，$E$ 中都存在一点 $x_k\neq x$，使得 $\|x_k-x\|<\varepsilon$。

选取 $x_1\in E$，使得 $0<\|x_1-x\|<1$。

归纳地进行：在选定 $x_k$ 之后，在 $E$ 中选取 $x_{k+1}$，使得
```math
0<\|x_{k+1}-x\|<\tfrac12\|x_k-x\|.
```
于是当 $k\to\infty$ 时 $\lim_{k\to\infty}x_k=x$，且 $x_k\neq x$，并且若 $k\neq j$，则 $x_k\neq x_j$。

其逆命题是显然的。$\square$

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**定理 11.18（Theorem 11.18）**</span>：集合 $E\subset\mathbb{R}^n$ 是闭集（closed set），当且仅当它包含其全部聚点。

其证明留作习题 11.4.3。

**Bolzano-Weierstrass 定理（Bolzano-Weierstrass Theorem）** 一维情形下的 Bolzano-Weierstrass 定理断言：有界实数序列（bounded sequence of real numbers）必然含有收敛子序列（convergent subsequence）。

这一定理可以推广到 $\mathbb{R}^n$，并且在我们研究 $\mathbb{R}^n$ 上的连续函数（continuous function）时发挥重要作用。

其证明需要 $n$ 次运用一维版本。

虽然证明的思想直截了当，但记号却相当繁杂，涉及子序列（subsequence）的子序列的子序列，共 $n$ 层。

我们将采用更紧凑的记号，以避免多层下标。

仔细研读这个证明是值得的，可以看到恰当的记号如何简化那些繁琐的细节。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**定理 11.19（Theorem 11.19，Bolzano-Weierstrass）**</span>：在 $\mathbb{R}^n$ 中，每个有界序列 $\{x_k\}$ 都含有收敛子序列。

> <span style="color:#1e8449;">**[note]**</span> **注 11** Bolzano-Weierstrass theorem（波尔查诺-魏尔斯特拉斯定理）的证明值得存为模板："逐坐标取子列法"。bounded（有界）性 $\|x_k\|\le M$ 经注 8 的左半传给每个坐标 $|x_{kj}|\le M$，先对坐标 1 取收敛 subsequence（子序列）$k(1,i)$，再在 $k(1,i)$ 内对坐标 2 取子列，直到第 $n$ 个坐标，取对角线 $k_i=k(n,i)$，定理 11.15 保证 $x_{k_i}$ 收敛。整个构造只靠一个关键引理：收敛序列的任意子序列收敛到同一极限，所以每层细化都不破坏前面坐标已取得的收敛——这也是不能对各坐标各自取子列再合并的原因。一维 BW 可用二分法证明：有界区间不断对半，无穷多项必落入某一半，逐半取点即得收敛子列，与 6.006 二分搜索同构；另一条路径先证"任何实数列必有单调子列"（峰值选取论证），单调加有界即收敛，这正是 selection（选择，找第 $k$ 小元素）一类算法思想的原型：从无穷序列中保序地挑出想要的项。双下标 $k(j,i)$ 的对角抽取与你 6.042 学过的 Cantor 对角线论证（1891）共用同一记号技巧，用途却相反：Cantor 造出不在任何一行中的对象以反证，BW 摘出每行都收敛的共同子列。历史上 Bolzano（波尔查诺）1817 年在《Rein analytischer Beweis》中证明有界无穷实数集必有聚点，Weierstrass（魏尔斯特拉斯）约 1860 年代在柏林讲义中独立给出；Bolzano 的贡献生前几乎无人注意，直到 20 世纪才恢复双人命名。

<span style="color:#2471a3;">**[proof]**</span> 证明。设 $\{x_k\}$ 是 $\mathbb{R}^n$ 中的有界序列，比方说对所有 $k\in\mathbb{N}$ 都有 $\|x_k\|\le M$。

对每个 $k$，记 $x_k=(x_{k1},\ldots,x_{kn})$。

则对每个 $k\in\mathbb{N}$ 与 $j=1,\ldots,n$，都有 $|x_{kj}|\le M$。

因此，对所有 $j$，实数序列 $\{x_{kj}\}$ 都是有界的。

先取 $j=1$。

将 Bolzano-Weierstrass 定理应用于有界序列 $\{x_{k1}\}$（$k=1,2,3,\ldots$），则存在一个整数序列
```math
1\le k(1,1)<k(1,2)<\cdots
```
以及一个数 $x_1$，使得当 $i\to\infty$ 时
```math
x_{k(1,i),1}\to x_1.
```
注意，序列 $\{x_{k(1,i),1}\}$ 正是序列 $\{x_{k1}\}$ 的一个子序列。

接下来取 $j=2$。

序列 $\{x_{k(1,i),2}\}$ 也以 $M$ 为界，所以再次运用 Bolzano-Weierstrass 定理，存在 $\{k(1,i)\}$ 的一个子序列 $\{k(2,i)\}$，使得 $\{x_{k(2,i),2}\}$ 收敛。

令
```math
x_2=\lim_{i\to\infty}x_{k(2,i),2}.
```
现在，序列 $\{x_{k(1,i),1}\}$ 收敛到 $x_1$，因此该序列的任何子序列也都收敛到 $x_1$。

特别地，当 $i\to\infty$ 时，$\{x_{k(2,i),1}\}\to x_1$。

我们继续这一过程。

在得到序列 $\{x_{k(j,i),j}\}$，且对所有 $m\le j$ 都有 $\{x_{k(m,i),m}\}\to x_m$ 之后，我们再次运用 Bolzano-Weierstrass 定理，得到更进一步子序列 $\{x_{k(j+1,i),j+1}\}$，它收敛到一点 $x_{j+1}\in\mathbb{R}$。

当 $j+1=n$ 时，这一过程停止。

令 $k_i=k(n,i)$，$x=(x_1,\ldots,x_n)$，则由定理 11.15 可知 $\lim_{i\to\infty}x_{k_i}=x$。$\square$

---

> <span style="color:#7f8c8d">*（本页第 4–39 行为 §11.4 节习题区（习题 11.4.1–11.4.10），按约定跳过。）*</span>

## <span style="color:#2471a3;">**[section]**</span> 11.5 函数与映射（Functions and Mappings）

在前几章处理函数（function）时，我们主要关注的是定义域（domain）为 $\mathbb{R}$ 的子集、值域（range）在 $\mathbb{R}$ 中的函数。

这类函数历来被称为「实变量的实值函数」（real-valued functions of a real variable）。

定义域通常是区间（interval）。

在本章与下一章中，我们将关注……

<span style="color:#7f8c8d">*（原句在页尾截断，于下一页继续。）*</span>

---

<span style="color:#2471a3;">**[section]**</span> **Section 11.5. 函数与映射（Functions and Mappings）**

（承接上文）这些函数的定义域与值域都位于空间 $\mathbb{R}^n$ 中。通常，其定义域（domain）是 $\mathbb{R}^n$ 的一个开子集（open subset）。与实变量的实值函数（real functions of a real variable）的情形一样，我们的研究聚焦于极限（limits）、连续性（continuity）与可微性（differentiability）相关的问题。在本节中，我们只处理一些定义、一些例子，以及少量关于记号（notation）的内容。

<span style="color:#2471a3;">**[section]**</span> **11.5.1 从 $\mathbb{R}^n$ 到 $\mathbb{R}$ 的函数（Functions from $\mathbb{R}^n$ to $\mathbb{R}$）**

让我们从函数 $f : E \to \mathbb{R}$ 开始，其中 $E$ 是 $\mathbb{R}^n$ 的子集（subset）。这样的函数有时被称为"多元实函数（real functions of several variables）"。下面我们给出一些例子。

对于 $n = 2$ 的情形（即函数 $f : \mathbb{R}^2 \to \mathbb{R}$），有一个特殊而传统的记号约定（notational feature）：表示点 $(x_1, x_2) \in \mathbb{R}^2$ 所需的两个变量被写作 $(x, y)$。在所有讨论中，$x$ 指第一个变量，$y$ 指第二个变量。类似地，对于函数 $f : \mathbb{R}^3 \to \mathbb{R}$，我们常用 $(x, y, z)$ 而非 $(x_1, x_2, x_3)$ 来表示 $\mathbb{R}^3$ 中的点。我们通常会采用这一约定，尤其是在下一章讨论导数（derivatives）的时候。对于 $n \geq 4$，则使用下标记号（subscript notation）。

<span style="color:#2471a3;">**[example]**</span> **例 11.20（Example 11.20）：** 设 $f(x, y) = x^2 + xy + y^2 + 5$。$f$ 的一个自然定义域（natural domain）是整个 $\mathbb{R}^2$，因此 $f : \mathbb{R}^2 \to \mathbb{R}$ 是一个二元函数（function of two variables）。函数 $f$ 是二元多项式（polynomial in two variables）的一个例子。一般的二元多项式可以写成

```math
f(x, y) = \sum_{i, j} a_{ij} x^i y^j \tag{9}
```

其中系数（coefficients）$a_{ij}$ 是实数，指数 $i$ 与 $j$ 是非负整数（nonnegative integers），且该求和只有有限多项。Figure 11.2 展示了这个多项式 $f$ 在 $\mathbb{R}^3$ 中的图形（graph）；你应该已经从微积分课程中熟悉这类表示。在我们研究的大部分内容中，都将无法依赖任何有意义的图像，因为我们研究的是多变元函数，而在 $\mathbb{R}^2$ 与 $\mathbb{R}^3$ 之外，图像是不可能的。即便如此，我们仍依靠这些特殊情况来帮助培养直觉，理解更一般的情形中发生了什么。

<span style="color:#2471a3;">**[example]**</span> **例 11.21（Example 11.21）：** 设 $g(x_1, x_2, x_3) = \sqrt{1 - x_1^2 - x_2^2 - x_3^2}$。这里 $g$ 的一个自然定义域是集合

```math
E = \{(x_1, x_2, x_3) : x_1^2 + x_2^2 + x_3^2 \leq 1\}
```

你可以认出 $E$ 正是空间 $\mathbb{R}^3$ 中的闭单位球（closed unit ball）。

<span style="color:#2471a3;">**[example]**</span> **例 11.22（Example 11.22）：** 设 $h(x, y) = \ln(xy)$。$h$ 的一个自然定义域是集合 $E = \{(x, y) : xy > 0\}$。因此 $E$ 由 $xy$ 平面的第一与第三开象限（open quadrants）的并集（union）构成。

<span style="color:#2471a3;">**[example]**</span> **例 11.23（Example 11.23）：** 对于 $\mathbb{R}^2$ 中的每个三角形 $T$，设 $A(T)$ 表示该三角形的面积。我们可以把 $A$ 看作定义域为 $\mathbb{R}^2$ 中所有三角形之集合的函数。但我们也可以把 $A$ 表示成六变量函数（function of six variables）的公式。若 $(a, b)$、$(c, d)$、$(e, f)$ 是 $T$ 的顶点（vertices），则我们可以把面积表示成函数 $g : \mathbb{R}^6 \to \mathbb{R}$，其中 $g(a, b, c, d, e, f) = A(T)$。（习题 11.5.2 要求给出面积的解析公式（analytic formula）。）

---

<span style="color:#2471a3;">**[figure]**</span> <span style="color:#2471a3;">**Figure 11.2. 多项式 $f(x, y) = x^2 + xy + y^2 + 5$ 的图形**</span>

有时，不直接参照坐标（coordinates）来表示一个函数会更为方便。

<span style="color:#2471a3;">**[example]**</span> **例 11.24（Example 11.24）：** 设 $a \in \mathbb{R}^n$，并定义 $f : \mathbb{R}^n \to \mathbb{R}$ 为 $f(x) = a \cdot x$。若 $a = (a_1, \ldots, a_n)$ 且 $x = (x_1, \ldots, x_n)$，则

```math
f(x) = f(x_1, \ldots, x_n) = a_1 x_1 + \cdots + a_n x_n
```

这类函数是线性函数（linear functions）。这意味着它们满足条件：对所有 $\alpha, \beta \in \mathbb{R}$ 及所有 $x, y \in \mathbb{R}^n$，都有

```math
f(\alpha x + \beta y) = \alpha f(x) + \beta f(y)
```

事实上，每个线性函数 $f : \mathbb{R}^n \to \mathbb{R}$ 都可以表示为 $f(x) = a \cdot x$ 的形式，其中 $a$ 是某个属于 $\mathbb{R}^n$ 的向量，且该表示对所有 $x \in \mathbb{R}^n$ 成立。我们把这一验证留作习题 11.5.3。

<span style="color:#2471a3;">**[example]**</span> **例 11.25（Example 11.25）：** 对每个 $x \in \mathbb{R}^n$，设 $f(x) = \|x\|$。于是 $f : \mathbb{R}^n \to \mathbb{R}$。用坐标表示为

```math
f(x) = f(x_1, \ldots, x_n) = \sqrt{x_1^2 + \cdots + x_n^2}
```

<span style="color:#7f8c8d">*（本页其余部分为 11.5 节习题区（Exercises 11.5.1–11.5.3），按约定跳过。）*</span>

---

### Section 11.5. Functions and Mappings（函数与映射）

### <span style="color:#2471a3;">**[section]**</span> 11.5.2 从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的函数（Functions from $\mathbb{R}^n \to \mathbb{R}^m$）

当处理定义域在 $\mathbb{R}^n$ 中、值域在 $\mathbb{R}^m$ 中的函数时，我们常用术语 mapping（映射）或 transformation（变换）或 operator（算子）来代替 function（函数）。
术语 vector-valued function（向量值函数）也很常用。

我们一直用粗体字母来表示 $\mathbb{R}^m$（$m \geq 2$）中的向量或点。
我们也用粗体字母来表示值域在 $\mathbb{R}^m$（$m \geq 2$）中的函数。
设 $E \subset \mathbb{R}^n$，且 $f: E \to \mathbb{R}^m$。
则对所有 $x \in E$，都有 $f(x) \in \mathbb{R}^m$。
若用坐标来表示 $x$ 与 $f(x)$，比如 $x = (x_1, \ldots, x_n)$、$f(x) = (y_1, \ldots, y_m)$，则 $f(x_1, \ldots, x_n) = (y_1, \ldots, y_m)$。
数 $y_1, \ldots, y_m$ 当然依赖于 $x = (x_1, \ldots, x_n)$。
因此存在函数 $f^1, \ldots, f^m: E \to \mathbb{R}$，称为 coordinate functions（坐标函数），使得
```math
\begin{aligned}
y_1 &= f^1(x) = f^1(x_1, \ldots, x_n) \\
y_2 &= f^2(x) = f^2(x_1, \ldots, x_n) \\
&\vdots \\
y_m &= f^m(x) = f^m(x_1, \ldots, x_n)
\end{aligned}
```
我们对函数 $f^j$ 使用上标而非下标，目的是避免与第 12 章中用于 partial derivatives（偏导数）的下标记号混淆。

<span style="color:#2471a3;">**[example]**</span> **例 11.26（Example 11.26）：** 定义 $f: \mathbb{R}^2 \to \mathbb{R}^2$ 为 $f(r, \theta) = (r \cos \theta, r \sin \theta)$，其中 $r, \theta \in \mathbb{R}$。
则 $f^1(r, \theta) = r \cos \theta$，$f^2(r, \theta) = r \sin \theta$。
当 $r \geq 0$ 时，这个映射 $f$ 在把 polar coordinates（极坐标）变换为 rectangular coordinates（直角坐标）的场合为我们所熟悉。
这里我们通常把 $f^1$ 记作 $x$、把 $f^2$ 记作 $y$，于是得到 $x = r \cos \theta$，$y = r \sin \theta$。$\square$

<span style="color:#2471a3;">**[example]**</span> **例 11.27（Example 11.27）：（线性函数 Linear functions）** 设 $A: \mathbb{R}^n \to \mathbb{R}^m$ 由下列方程给出：
```math
\begin{aligned}
y_1 &= a_{11}x_1 + \cdots + a_{1n}x_n \\
y_2 &= a_{21}x_1 + \cdots + a_{2n}x_n \\
&\vdots \\
y_m &= a_{m1}x_1 + \cdots + a_{mn}x_n
\end{aligned}
```
其中 $a_{ij} \in \mathbb{R}$，$i = 1, \ldots, m$，$j = 1, \ldots, n$，且 $x = (x_1, \ldots, x_n)$。
变换 $A$ 可以用一个 matrix（矩阵）$A = (a_{ij})$ 来表示，即由系数构成的 $m \times n$ 系数矩阵（matrix of coefficients）。
于是我们有 $A(x) = Ax$，其中的乘积是矩阵乘法（matrix multiplication）：
```math
A(x) = Ax =
\begin{pmatrix}
a_{11} & \cdots & a_{1n} \\
\vdots &        & \vdots \\
a_{m1} & \cdots & a_{mn}
\end{pmatrix}
\begin{pmatrix}
x_1 \\ \vdots \\ x_n
\end{pmatrix}
```
容易检验 $A$ 是线性的（linear），即对一切 $\alpha, \beta \in \mathbb{R}$ 与一切 $x_1, x_2 \in \mathbb{R}^n$ 都成立 $A(\alpha x_1 + \beta x_2) = \alpha A(x_1) + \beta A(x_2)$。（见习题 11.5.4。）$\square$

注意在 Example 11.27 中，我们用大写字母来表示从 $\mathbb{R}^n \to \mathbb{R}^m$ 的线性变换（linear transformation）。
这是一种常见做法，在处理其他向量空间（vector space）上的线性变换时也经常使用（见第 13 章）。
即使函数不是线性的，有时人们也更喜欢用大写字母来表示从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的变换。
我们将根据需要来使用任何方便的记号。
关于记号再多说一句：有时，特别是在处理线性变换时，用 $Ax$ 这样的记号来代替 $A(x)$ 会很方便。
我们将在当时使用这两种记号中任何一种方便的写法。

<span style="color:#2471a3;">**[example]**</span> **例 11.28（Example 11.28）：** 设 $T(x, y) = (u, v)$，其中 $u = e^x \cos y$，$v = e^x \sin y$。

> <span style="color:#1e8449;">**[note]**</span> **注 12** Example 11.24 断言每个 linear function（线性函数）$f:\mathbb{R}^n\to\mathbb{R}$ 都是 $f(x)=a\cdot x$，证明模板只有两步："基展开+线性延拓"——把 $x=\sum_j x_j e_j$ 代入，线性性给出 $f(x)=\sum_j x_j f(e_j)$，取 $a=(f(e_1),\dots,f(e_n))$ 即得。这是整个线性代数的发动机：线性映射由基上的取值唯一决定，Strang 第 7 章"矩阵的列就是基向量的像"是同一句话的矩阵版，Example 11.27 的 $A(x)=Ax$ 中 $A$ 的第 $j$ 列正是 $Ae_j$。§11.5.2 用上标记坐标函数 $f^1,\dots,f^m$ 而非下标 $f_j$，是因为第 12 章偏导数记号 $\partial f/\partial x_j$ 将占用下标位置——记号系统要提前规划命名空间，与代码里避免变量名冲突是同一纪律。检验非线性最快的办法是算一个反例：polar coordinates（极坐标）映射 $f(r,\theta)=(r\cos\theta,r\sin\theta)$ 满足 $f(1,0)+f(0,\pi/2)=(1,0)$ 而 $f((1,0)+(0,\pi/2))=f(1,\pi/2)=(0,1)$，两者不等，加法被破坏，故非线性。Example 11.28 的 $T(x,y)=(e^x\cos y,e^x\sin y)$ 是复指数 $e^{x+iy}$ 的实部与虚部：高数里的 Euler's formula（欧拉公式）$e^{iy}=\cos y+i\sin y$（Euler 于 1748 年系统给出）说明虚轴每前进 $2\pi$ 绕圆一圈，"直线 $x=x_0$ 无限次绕圈"由此而来，也直接证明该映射不是一对一的。
于是 $u = T^1(x, y) = e^x \cos y$，$v = T^2(x, y) = e^x \sin y$。
我们可以研究映射 $T$ 的一些几何性质。
注意 $u^2 + v^2 = e^{2x}$，且 $v \cos y = u \sin y$。
对固定的 $x_0$，$(u, v)$ 是圆心在 $(0, 0)$、半径为 $e^{x_0}$ 的圆上的一个点。
当 $y$ 在长度为 $2\pi$ 的区间上增大时，$(u, v)$ 将绕这个圆转一周。
因此 $T$ 把直线 $x = x_0$ 无限多次地映绕到该圆上。
类似地，$T$ 把直线 $y = y_0$ 映到一条 slope（斜率）为 $\tan y_0$、从原点发出的 ray（射线）上。
我们把这个性质以及 $T$ 的其他一些映射性质的验证留给习题 11.5.5。
注意，如果我们想要一个图形表示，这个函数会给我们带来一些麻烦。
它的图形将是 $\mathbb{R}^4$ 的一个子集，超出了我们表示它的能力。
可以用 Figure 11.3 来研究这个函数；你们应当从微积分课程中熟悉这样的表示。
这幅图承载了前面讨论过的关于直线映射为圆的信息。$\square$

在第 12 章中，我们将关注多变量函数与映射的 differentiability（可微性）。
我们工作的核心是用线性变换来逼近这样的函数或映射。

<span style="color:#7f8c8d">*（本页其余部分为 Exercises 11.5.4–11.5.6 习题区，按约定跳过。）*</span>

---

**<span style="color:#2471a3;">[figure]</span> <span style="color:#c0392b;">Figure 11.3</span>.** 函数 $T(x, y) = (u, v)$ 的示意图（representation），其中 $u = e^x \cos y$，$v = e^x \sin y$。

<span style="color:#7f8c8d">*（图下方为习题区：问题 (a) 要求描述 $H$ 把 $xy$ 平面中的集合映到 $uv$ 平面的水平线与竖直线上的集合，并同样处理竖直线；问题 (b) 要求确定集合 $S \subset \mathbb{R}^2$ 使 $H(S) = [1, 2] \times [4, 5]$，按约定跳过。）*</span>

### <span style="color:#2471a3;">**[section]**</span> §11.6 从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的函数的极限

函数 $f: E \to \mathbb{R}^m$（其中 $E \subset \mathbb{R}^n$）的极限（limit）概念，与实函数 $f: E \to \mathbb{R}$（其中 $E \subset \mathbb{R}$）的极限概念完全类似。

我们希望捕捉这样的思想：当 $x$ 在 $E$ 中接近 $x_0$ 时，$f(x)$ 接近 $y_0 \in \mathbb{R}^m$。

我们的定义以及一些基本结果及其证明，本质上与它们在实函数情形中的对应物完全相同。

#### <span style="color:#2471a3;">**[section]**</span> 11.6.1 定义（Definition）

我们以从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的函数的极限的 $\varepsilon$-$\delta$ 定义（$\varepsilon$-$\delta$ definition）开始。

它与序列版本的等价性将在随后的 引理 11.30 中证明。

**<span style="color:#2471a3;">[definition]</span> <span style="color:#c0392b;">定义 11.29（Definition 11.29）</span>：** <span style="color:#00838f;">设 $f: E \to \mathbb{R}^m$，其中 $E$ 是 $\mathbb{R}^n$ 的子集，并设 $x_0$ 是 $E$ 的聚点（limit point）。我们说

> <span style="color:#1e8449;">**[note]**</span> **注 13** Definition 11.29 把第 5 章单变量的 ε-δ 定义原样搬到 $\mathbb{R}^n\to\mathbb{R}^m$，唯一改动是把绝对值换成范数：对每个 $\varepsilon>0$ 存在 $\delta>0$，使得 $0<\|x-x_0\|<\delta$ 且 $x\in E$ 时恒有 $\|f(x)-y_0\|<\varepsilon$。量词嵌套顺序（先 $\varepsilon$ 后 $\delta$）是定义的心脏：$\delta$ 可以依赖 $\varepsilon$ 与 $x_0$，唯独不能依赖具体的 $x$——这正是 6.042 第 3 章 Logical Formulas 里谓词公式的量词次序，而"证明极限不存在"无非是写出它的否定 $\exists\varepsilon\,\forall\delta\,\exists x$，一条量词换位规则。为什么要刺穿 $x_0$（要求 $0<\|x-x_0\|$）？因为极限问的是 $f$ 在 $x_0$ 附近、而非在 $x_0$ 处的行为：Example 11.31 里 $f(0,0)=7$ 而极限是 $0$，$x_0$ 处的取值对极限毫无发言权。为什么还要求 $x_0$ 是 $E$ 的聚点？若 $x_0$ 是孤立点，刺穿的小球里没有 $E$ 的点，条件对任何 $y_0$ 都空真（vacuously true），极限的唯一性（Exercise 11.6.2）立即破产。结尾的邻域翻译——$y_0$ 的每个邻域 $V$ 都对应 $x_0$ 的邻域 $U$ 使 $f((U\cap E)\setminus\{x_0\})\subset V$——只谈"邻域"不谈数值，日后向一般拓扑空间推广极限时用的正是这一版。
```math
\lim_{x \to x_0} f(x) = y_0
```
如果对每个 $\varepsilon > 0$ 存在 $\delta > 0$，使得当 $0 < \|x - x_0\| < \delta$ 且 $x \in E$ 时，有 $\|f(x) - y_0\| < \varepsilon$。</span>

注意，极限的存在性以及它的值，并不依赖于 $f$ 是否在 $x_0$ 处有定义，也不依赖于它在 $x_0$ 处的值。

用宽松的几何语言说，$\lim_{x \to x_0} f(x) = y_0$ 意味着：对 $y_0$ 的每个邻域（neighborhood）$V$，无论多小，都对应着 $x_0$ 的一个充分小的邻域 $U$，使得 $f$ 把 $(U \cap E) \setminus \{x_0\}$ 映入 $V$。

（这个定义和这段讨论应当与第 5 章中对单实变量函数的极限的处理作比较。）

---

我们的引理把这个极限概念与序列版本（sequential version）联系起来（后者是第 5.1.2 节中单变量函数相应内容的类比）。

**<span style="color:#2471a3;">[lemma]</span> <span style="color:#c0392b;">引理 11.30</span>：** 设 $E \subset \mathbb{R}^n$，并设 $x_0$ 是 $E$ 的一个聚点（accumulation point）。设 $f: E \to \mathbb{R}^m$。则 $\lim_{x \to x_0} f(x) = y_0$ 当且仅当对每个满足 $x_k \to x_0$、$x_k \neq x_0$ 的序列 $\{x_k\} \subset E$，都有 $f(x_k) \to y_0$。

> <span style="color:#1e8449;">**[note]**</span> **注 14** Lemma 11.30 在 ε-δ 极限与序列极限之间架起双向桥：$\lim_{x\to x_0}f(x)=y_0$ 当且仅当每条满足 $x_k\to x_0$、$x_k\neq x_0$ 的序列 $\{x_k\}\subset E$ 都有 $f(x_k)\to y_0$。正方向是两段套接：ε-δ 给出 $\delta$，收敛给出 $N$，把 $k\ge N$ 的项塞进 $\delta$ 球即可。逆方向才是模板——"否定机器"：若 $y_0$ 不是极限，存在固定 $\varepsilon_0>0$ 打败一切 $\delta$，于是逐次取 $\delta=1/k$ 得到 $x_k$ 满足 $0<\|x_k-x_0\|<1/k$ 却 $\|f(x_k)-y_0\|\ge\varepsilon_0$，自变量收敛而像不收敛，一条反例序列自动出炉。这台机器是全章证明极限不存在的总引擎，Theorem 11.49 证非一致连续时还会原样出场；它的近亲是"极限存在则局部有界"（Exercise 11.6.3：对 $\varepsilon=1$ 用定义再套三角不等式即得 $M$）。Example 11.31 演示正方向的标准操作：用 $|x^2-y^2|\le x^2+y^2$ 与 $|xy|\le x^2+y^2$ 两处放大把 $|f(x,y)|$ 压进 $x^2+y^2$；严格核对会发现书中 $\delta=\varepsilon$ 的写法只在 $0<\varepsilon\le1$ 时链条成立（此时 $x^2+y^2<\varepsilon^2\le\varepsilon$），对 $\varepsilon>1$ 改取 $\delta=1$ 即可——"ε-δ 验证只需处理小 ε"是全书的简化惯例，遇到这类随手写下的 $\delta$ 值得按这个眼光复查一遍。

<span style="color:#2471a3;">**[proof]**</span> 证明。假设 $\lim_{x \to x_0} f(x) = y_0$。设 $x_k \to x_0$（$x_k \neq x_0$），$x_k \in E$，并设 $\varepsilon > 0$。则存在 $\delta > 0$，使得若 $x \in E$ 且 $0 < \|x - x_0\| < \delta$，则
```math
\|f(x) - y_0\| < \varepsilon.
```
由于 $x_k \to x_0$，存在 $N \in \mathbb{N}$ 使得当 $k \geq N$ 时 $\|x_0 - x_k\| < \delta$。于是，对 $k \geq N$ 有
```math
\|f(x_k) - y_0\| < \varepsilon,
```
从而 $f(x_k) \to y_0$。

为证明逆命题，假设 $y_0$ 不是 $f(x)$ 当 $x \to x_0$ 时的极限。则存在 $\varepsilon > 0$，使得对每个 $k \in \mathbb{N}$ 都存在 $x_k \in E$ 满足
```math
0 < \|x_k - x_0\| < \frac{1}{k}
```
且
```math
\|f(x_k) - y_0\| \geq \varepsilon.
```
序列 $\{x_k\}$ 收敛到 $x_0$，但序列 $f(x_k)$ 不收敛到 $y_0$。$\square$

**<span style="color:#2471a3;">[example]</span> <span style="color:#c0392b;">Example 11.31</span>：** 设
```math
f(x, y) = xy\,\frac{x^2 - y^2}{x^2 + y^2}, \qquad f(0, 0) = 7.
```
则 $f: \mathbb{R}^2 \to \mathbb{R}$。我们证明 $\lim_{(x,y) \to (0,0)} f(x, y) = 0$。设 $\varepsilon > 0$。当 $(x, y) \neq (0, 0)$ 时，有
```math
|f(x, y) - 0| \leq |xy|\,\frac{|x^2 - y^2|}{|x^2 + y^2|} \leq |xy|.
```
现在对一切 $(x, y) \in \mathbb{R}^2$ 有 $|xy| \leq x^2 + y^2$，所以当 $\sqrt{x^2 + y^2} < \delta = \varepsilon$、$(x, y) \neq (0, 0)$ 时，$|f(x, y)| < \varepsilon$【译者注：由 $|f|\le|xy|\le x^2+y^2$ 只得到 $|f|<\varepsilon^2$；书中的 $\delta=\varepsilon$ 仅对 $0<\varepsilon\le1$ 成立，一般情形取 $\delta=\min(\varepsilon,1)$，参见注 14】。因此
```math
\lim_{(x,y) \to (0,0)} f(x, y) = 0.
```
注意 $f(0, 0) = 7$ 这一事实并不影响极限。$\square$

当极限存在时，它必定是唯一的（Exercise 11.6.2）。我们有时可以利用这一事实来证明某个极限不存在。

**<span style="color:#2471a3;">[example]</span> <span style="color:#c0392b;">Example 11.32</span>：** 设
```math
f(x, y) = \frac{2xy}{x^2 + y^2}, \qquad f(0, 0) = 0.
```
（本页至此结束，本例的后续部分见下一书页。）

---

# TBB《Elementary Real Analysis》§11.6 译文（书页 455–456）

---

## 书页 455

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">**例 11.32（Example 11.32）（接前页续）**</span> 这里 $\lim_{y\to 0} f(0,y) = \lim_{x\to 0} f(x,0) = 0$，但 $\lim_{(x,y)\to(0,0)} f(x,y)$ 不存在。

为看清这一点，注意到 $\lim_{(t,t)\to(0,0)} f(t,t) = \lim_{t\to 0} \frac{2t^2}{2t^2} = 1$。

因此，沿坐标轴（coordinate axes）趋于 $(0,0)$ 时，极限必须为 $0$；

而沿直线 $y = x$ 趋于 $(0,0)$ 时，极限必须为 $1$。

其结果是，对 $0 < \varepsilon < 1$，不存在 $y_0 \in \mathbb{R}$ 和 $\delta > 0$ 使得当 $0 < \sqrt{x^2 + y^2} < \delta$ 时总有 $|f(x,y) - y_0| < \varepsilon$。

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">**例 11.33（Example 11.33）**</span> 令 $f(r, \theta) = (r\cos\theta, r\sin\theta)$，于是 $f: \mathbb{R}^2 \to \mathbb{R}^2$。

我们来证明 $\lim_{(r,\theta)\to(0,0)} f(r,\theta) = (0,0)$。

这里 $\|f(r,\theta) - (0,0)\| = \sqrt{r^2\cos^2\theta + r^2\sin^2\theta} = |r|$。

因此，无论 $\theta$ 如何，只要 $|r| < \varepsilon$ 就有 $\|f(r,\theta) - (0,0)\| < \varepsilon$。

特别地，若 $0 < \|(r,\theta)\| = \sqrt{r^2 + \theta^2} < \delta = \varepsilon$，

则 $|r| < \varepsilon$，从而 $\lim_{(r,\theta)\to(0,0)} f(r,\theta) = (0,0)$。

<span style="color:#7f8c8d">*（本页 11.6 节习题区 Exercises 11.6.1–11.6.3，按约定跳过，不翻译、不收录。）*</span>

<span style="color:#2471a3;">**[section]**</span>

### 11.6.2 逐坐标收敛（Coordinate-Wise Convergence）

我们之前在习题 11.2.6、11.2.7、11.3.8 与 11.4.1 中已经看到，$\mathbb{R}^n$ 上还存在更多可用于研究收敛性的范数（norm）。

让我们简要讨论范数 $\|\cdot\|_\infty$ 与极限概念（limit concept）的联系。

这将让我们对极限概念的本质获得一些洞见，尤其能使我们证明收敛可以逐坐标（coordinate-wise）地解释。

---

## 书页 456

<span style="color:#2471a3;">**[figure]**</span> **Figure 11.4.** 三种范数 $\|\cdot\|_1$、$\|\cdot\|$ 与 $\|\cdot\|_\infty$ 下以原点为中心的三个单位球（由内到外）。

我们先回顾无穷范数（infinity norm）的定义，并将其与欧几里得范数（euclidean norm）作比较。

对 $x = (x_1, \ldots, x_n) \in \mathbb{R}^n$ 我们定义

```math
\|x\|_\infty = \max\{|x_1|, |x_2|, \ldots, |x_n|\}.
```

为简单起见，先考虑 $\mathbb{R}^2$ 的情形，用记号 $(x,y)$ 表示 $\mathbb{R}^2$ 中的元素。

此时 $\|(x,y)\| = \sqrt{x^2 + y^2}$，而 $\|(x,y)\|_\infty = \max\{|x|, |y|\}$。

欧几里得开球（open euclidean ball）$B((0,0), r)$ 是以 $(0,0)$ 为中心、半径为 $r$ 的开圆盘（open disk）。

开球 $B_\infty((0,0), r)$ 是以 $(0,0)$ 为中心、各边平行于坐标轴且边长为 $2r$ 的开正方形（open square）。

注意 $B((0,0), r) \subset B_\infty((0,0), r)$，并且存在 $s > 0$ 使得 $B_\infty((0,0), s) \subset B((0,0), r)$。

从 Figure 11.4 可以看到，三种范数 $\|\cdot\|_1$、$\|\cdot\|$ 与 $\|\cdot\|_\infty$ 下以原点为中心的三个单位球。

类似的说明也适用于以 $\mathbb{R}^2$ 中其他点为中心的球。

对任意的 $n \in \mathbb{N}$，类似的结果依然成立。

对每个 $r > 0$ 和 $x_0 \in \mathbb{R}^n$，我们有

```math
\{x \in \mathbb{R}^n : \|x - x_0\| < r\} \subset \{x \in \mathbb{R}^n : \|x - x_0\|_\infty < r\} \tag{10}
```

并且存在 $s > 0$ 使得

```math
\{x \in \mathbb{R}^n : \|x - x_0\|_\infty < s\} \subset \{x \in \mathbb{R}^n : \|x - x_0\| < r\}. \tag{11}
```

从这些包含关系可以看出，在定义 11.14 与定义 11.29 中，我们可以用 $\|\cdot\|_\infty$ 替换 $\|\cdot\|$ 而不改变任何结论。

也就是说，序列极限（sequence limit）的定义等价于下面这个换用不同范数的版本。

<span style="color:#2471a3;">**[lemma]**</span> <span style="color:#c0392b">**引理 11.34（Lemma 11.34）**</span> 极限 $x_k \to x$ 在范数 $\|\cdot\|$ 意义下成立，当且仅当对一切 $\varepsilon > 0$，存在整数 $N$ 使得当 $k \geq N$ 时总有 $\|x_k - x\|_\infty < \varepsilon$。

> <span style="color:#1e8449;">**[note]**</span> **注 15** Figure 11.4 的三个单位球说完了本节全部内容：$\|\cdot\|_1$ 球是菱形、$\|\cdot\|$ 球是圆盘、$\|\cdot\|_\infty$ 球是边长 $2r$ 的正方形，一个套一个。包含 (10)（$r$ 半径的欧几里得球落入同半径的 $\infty$ 球）依据 $\|x\|_\infty\le\|x\|$；包含 (11)（存在 $s$ 使 $s$ 半径的 $\infty$ 球落入 $r$ 半径的欧几里得球）显式取 $s=r/\sqrt{n}$ 即可，因为 $n$ 个坐标都不超过 $\|x\|_\infty$ 时 $\|x\|\le\sqrt{n}\|x\|_\infty$。两行夹出的三明治 $\|x\|_\infty\le\|x\|\le\sqrt{n}\|x\|_\infty$ 是本小节全部结论的来源：换范数不改变收敛与极限，这正是 Boyd《Convex Optimization》附录 A.1.4「Equivalence of norms」有限维范数等价定理（存在常数 $\alpha,\beta$ 使 $\alpha\|x\|_a\le\|x\|_b\le\beta\|x\|_a$）在 $\|\cdot\|_\infty$ 与 $\|\cdot\|$ 这对范数上的实例，Boyd 同处明言无穷维不再成立，与 part1 注 8 的 $e_k$ 反例互证——三明治两端全靠 $n$ 有限。Lemma 11.34 的证明只有一步值得存：反方向先用 (11) 选 $\varepsilon_0<\varepsilon$，让 $\varepsilon_0$ 半径的 $\infty$ 球整个装进 $\varepsilon$ 半径的欧几里得球，再对 $\varepsilon_0$ 取 $N$——"换范数前先把球调小一号"。Boyd 附录 A.1.2 还证明单位球必是凸、对称、闭且有界的集合（反之亦然），§2.2.4（Polyhedra）把 $\ell_\infty$ 单位球写成 $2n$ 条线性不等式，即优化里的 box constraint（盒约束）。

<span style="color:#2471a3;">**[proof]**</span> 证明。

设 $x_k \to x$ 且 $\varepsilon > 0$。

则存在 $N \in \mathbb{N}$ 使得对所有 $k \geq N$ 有 $\|x_k - x\| < \varepsilon$。

由 (10) 可见，对所有 $k \geq N$ 有 $\|x_k - x\|_\infty < \varepsilon$。

因此 $x_k \to x$ 对 $\|\cdot\|_\infty$ 成立。

反过来，设 $x_k \to x$ 对 $\|\cdot\|_\infty$ 成立。

取 $\varepsilon > 0$。

利用 (11)，选取 $\varepsilon_0 < \varepsilon$ 使得若 $\|z - x\|_\infty < \varepsilon_0$，则 $\|z - x\| < \varepsilon$。

现在，存在 $N \in \mathbb{N}$ 使得若 $k \geq N$，则 $\|x_k - x\|_\infty < \varepsilon_0$。

于是由 $\varepsilon_0$ 的选取可知 $\|x_k - x\| < \varepsilon$，从而 $x_k \to x$。$\square$

---

### 书页 457（§11.6 极限算律与逐坐标收敛）

<span style="color:#2471a3;">**[section]**</span> **§11.6 从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的函数的极限（Limits of Functions from $\mathbb{R}^n$ to $\mathbb{R}^m$）**（承接前页）

类似地，函数极限（function limit）也可以用另一种范数来表述。

<span style="color:#2471a3;">**[lemma]**</span> **引理 11.35（Lemma 11.35）**：设 $E \subset \mathbb{R}^n$，$f: E \to \mathbb{R}^m$。

设 $x_0 = (x_1, \ldots, x_n)$ 为 $E$ 的一个聚点（limit point），并设 $y_0 = (y_1, \ldots, y_m) \in \mathbb{R}^m$。

<span style="color:#00838f">**$\lim_{x \to x_0} f(x) = y_0$ 当且仅当：对每个 $\varepsilon > 0$，都存在 $\delta > 0$，使得只要 $0 < \|x - x_0\|_\infty < \delta$ 且 $x \in E$，就有 $\|f(x) - y_0\|_\infty < \varepsilon$。**</span>

我们将证明留作习题 11.6.5。

<span style="color:#2471a3;">**[section]**</span> **逐坐标收敛（Coordinate-Wise Convergence）**

作为前面论述的一个应用，我们证明：从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的映射的收敛性可以归结为逐坐标收敛（coordinate-wise convergence）。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">**定理 11.36（Theorem 11.36）**</span>：设 $E \subset \mathbb{R}^n$，$f: E \to \mathbb{R}^m$，$f = (f^1, \ldots, f^m)$。

> <span style="color:#1e8449;">**[note]**</span> **注 16** Theorem 11.36 断言：$f=(f^1,\dots,f^m)$ 的极限存在且等于 $y_0$ 当且仅当 $m$ 个坐标函数（coordinate function）$f^j$ 分别以 $y^j$ 为极限——一个 $m$ 维判定被拆成 $m$ 个一维判定。引擎是 Lemma 11.35 加观察 $\|z\|_\infty\to0$ 等价于每个 $z_i\to0$；后者用到"有限多个趋于 $0$ 的序列的最大值仍趋于 $0$"，恰恰依赖 $m$ 有限，坐标换成无穷多时逐坐标收敛推不出范数收敛（part1 注 8 的 $e_k$ 反例）——这条定理是一张"有限维优惠券"。注意书中证明的压缩句跳了一步：$|z_i|\le\|z\|$ 只给单向，反向要靠 $\|z\|\le\sqrt{p}\|z\|_\infty$（即 (11)），三明治两端合起来才是等价。从算法看这是 6.006 分治策略的分析版：规模 $m$ 拆成 $m$ 个规模 $1$ 的子问题、各自解决、再打包；CSAPP 第 5 章的 Web Aside OPT:SIMD「Achieving Greater Parallelism with SIMD Instructions」讲的 SIMD（单指令多数据）指令——一条指令同时处理向量的多个分量——正是逐坐标结构在硬件上的兑现：分析说可以分开算，处理器就真的并行算。对线性映射 $f(x)=Ax$，坐标函数 $f^j(x)$ 是 $A$ 的第 $j$ 行与 $x$ 的点积（Strang 第 2 章行观点），逐坐标收敛在此退化为"每个行函数分别取极限"。

设 $x_0 = (x_1, \ldots, x_n)$ 为 $E$ 的一个聚点，设 $y_0 = (y_1, \ldots, y_m) \in \mathbb{R}^m$。

<span style="color:#00838f">**$\lim_{x \to x_0} f(x) = y_0$ 当且仅当对所有 $j = 1, \ldots, m$ 都有 $\lim_{x \to x_0} f^j(x) = y^j$。**</span>

<span style="color:#2471a3;">**[proof]**</span> 证明：本证明可直接由 引理 11.35 与如下观察推出。

对任意 $p \in \mathbb{N}$ 和任意向量 $z = (z_1, \ldots, z_p) \in \mathbb{R}^p$，对一切 $i = 1, \ldots, p$ 都有 $|z_i| \le \|z\|$，因此 $\|z\|_\infty \to 0$ 等价于：对所有 $i = 1, \ldots, p$ 都有 $z_i \to 0$【译者注：原文此处作 $\lim_{z \to z_0} z_i = 0$，且仅给出 $|z_i| \le \|z\|$ 的单向估计；等价性还需 $\|z\| \le \sqrt{p}\,\|z\|_\infty$ 收口，见注 16】。

于是，例如 $\lim_{x \to x_0} \|f(x) - y_0\|_\infty = 0$ 就等价于对所有 $j = 1, \ldots, m$ 有 $\lim_{x \to x_0} |f^j(x) - y^j| = 0$。$\square$

习题 11.2.6、11.2.7、11.3.8 与 11.4.1 都与比较 $\mathbb{R}^n$ 上的几种范数有关。

本质上，这些习题表明：在处理与开集（open set）和收敛直接相关的概念时，范数 $\|\cdot\|$、$\|\cdot\|_1$ 与 $\|\cdot\|_\infty$ 可以互换使用。

<span style="color:#7f8c8d">*（本页其余部分为 §11.6 习题区（Exercises 11.6.4–11.6.5），按约定跳过。）*</span>

### 书页 458（§11.6.3 代数性质 与 §11.7 连续性）

<span style="color:#2471a3;">**[section]**</span> **11.6.3 代数性质（Algebraic Properties）**

由定理 11.36 可直接得到一个推论：我们在 5.2.3 节为单实变量实值函数得到的若干极限代数性质，在当前的背景下依然成立。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">**定理 11.37（Theorem 11.37）**</span>：设 $E \subset \mathbb{R}^n$，$f: E \to \mathbb{R}^m$，$g: E \to \mathbb{R}^m$，$\alpha \in \mathbb{R}$，且 $x_0$ 为 $E$ 的一个聚点（accumulation point）。

若 $\lim_{x \to x_0} f(x) = y_0$ 且 $\lim_{x \to x_0} g(x) = z_0$，则：

1. $\lim_{x \to x_0} (f(x) + g(x)) = y_0 + z_0$，且

2. $\lim_{x \to x_0} (\alpha f)(x) = \alpha y_0$【译者注：原文作 $\lim_{x\to x_0} f(\alpha x)=\alpha y_0$，此处应为 $(\alpha f)(x)$】。

我们把证明留给习题。

至于乘积，点积（dot product）情形下预期的乘积法则也是成立的。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">**定理 11.38（Theorem 11.38）**</span>：设 $E \subset \mathbb{R}^n$，$x_0$ 为 $E$ 的一个聚点，并设 $f, g: E \to \mathbb{R}^m$。

> <span style="color:#1e8449;">**[note]**</span> **注 17** Theorem 11.38 的证明只有四行，值得存为"序列搬运"模板。第一步，用 Lemma 11.30 把函数极限命题翻译成序列命题：取任意 $x_k\to x_0$（$x_k\in E$，$x_k\neq x_0$）；第二步，令 $u_k=f(x_k)$、$v_k=g(x_k)$，由假设得 $u_k\to y_0$、$v_k\to z_0$；第三步，调用 §11.4 已证的序列点积算律 Theorem 11.16(iii)；第四步，用 Lemma 11.30 反向搬回函数极限。桥是双向的：凡对"一切靠近 $x_0$ 的序列"成立的结论都自动升级为函数极限的结论，序列世界的重活已在 §11.4 干完，函数极限的算律全是白送。Theorem 11.37 的和与数乘用同一模板配 Theorem 11.16(i)(ii)，书把它留作习题正是让你亲手跑一遍；下一页连续性的和、数乘、点积法则也只是"援引"这两条定理——一次证明、两处调用。从代数看，定理 11.37 两条恰好说明"在固定 $x_0$ 处有极限的函数全体"关于点态加法与数乘封闭，这是 Strang 第 3 章函数空间的两条封闭性公理，极限算子 $f\mapsto\lim_{x\to x_0}f(x)$ 是线性映射——分析的向量空间实例。Exercise 11.6.7 问叉积是否同理：$x\times y$ 对两个变量双线性，模板逐字照搬仍成立。

若 $\lim_{x \to x_0} f(x) = y_0$ 且 $\lim_{x \to x_0} g(x) = z_0$，则 $\lim_{x \to x_0} (f(x) \cdot g(x)) = y_0 \cdot z_0$。

<span style="color:#2471a3;">**[proof]**</span> 证明：我们应用 引理 11.30。

设 $x_k \to x_0$，$x_k \in E$，$x_k \neq x_0$。

对 $k \in \mathbb{N}$，令 $u_k = f(x_k)$，$v_k = g(x_k)$。

则 $u_k \to y_0$ 且 $v_k \to z_0$，从而由定理 11.16(iii) 得 $u_k \cdot v_k \to y_0 \cdot z_0$。$\square$

<span style="color:#7f8c8d">*（Exercises 11.6.6–11.6.7 为 §11.6 习题区，按约定跳过。）*</span>

<span style="color:#2471a3;">**[section]**</span> **11.7 从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的函数的连续性（Continuity of Functions from $\mathbb{R}^n$ to $\mathbb{R}^m$）**

既然我们已经有了向量值函数（vector-valued function）的极限概念，就可以用与 5.4.2 节中对实值函数完全相同的方式来引入连续（continuity）的概念。

本节中的证明与单变量情形中的相应证明几乎完全相同，因此我们将它们省略。

<span style="color:#2471a3;">**[definition]**</span> **定义 11.39（Definition 11.39）**：设 $E \subset \mathbb{R}^n$，$f: E \to \mathbb{R}^m$，$x_0 \in E$。

<span style="color:#00838f">**我们说 $f$ 在 $x_0$ 处连续（continuous），如果对每个 $\varepsilon > 0$ 存在 $\delta > 0$，使得对所有满足 $\|x - x_0\| < \delta$ 的 $x \in E$，都有 $\|f(x) - f(x_0)\| < \varepsilon$。**</span>

---

### §11.7 从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的函数的连续性

<span style="color:#2471a3;">**[section]**</span> Section 11.7 Continuity of Functions from $\mathbb{R}^n$ to $\mathbb{R}^m$（从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的函数的连续性）

注意，按照这一定义，每个函数 $f$ 在 $E$ 的每个孤立点（isolated point）处都连续，也就是说在 $E$ 中任何不是 $E$ 的聚点（limit point）的点处都连续。

对于 $E$ 的一个聚点 $x_0$，容易看出 $f$ 在 $x_0$ 处连续当且仅当

```math
\lim_{x \to x_0} f(x) = f(x_0)
```

由于 引理 11.30，用序列来表述的连续性定义也立即可用：$f$ 在 $x_0$ 处连续当且仅当对每个序列 $\{x_k\} \to x_0$（其中 $x_k \in E$），都有

```math
\lim_{k \to \infty} f(x_k) = f(x_0)
```

用邻域（neighborhood）来表述，我们发现 $f$ 在 $x_0$ 处连续的条件是：对 $f(x_0)$ 的每个邻域 $V$，都存在 $x_0$ 的某个邻域 $U$，使得 $f(U \cap E) \subset V$。

简言之，以上这些连续性的定义都是等价的，并且用精确的语言阐明了：$E$ 中所有靠近 $x_0$ 的点都被映到 $\mathbb{R}^m$ 中靠近 $f(x_0)$ 的点。

<span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f;">**定义 11.40（Definition 11.40）**</span>：设 $E \subset \mathbb{R}^n$，并设 $f : E \to \mathbb{R}^m$。若 $f$ 在 $E$ 的所有点处都连续，则称 $f$ 在 $E$ 上连续（continuous on $E$）。当 $E$ 能从上下文理解时，我们就简单地说 $f$ 是连续的（continuous）。

与 $\mathbb{R}$ 的子集上实值函数的 定理 5.37 相类似，连续性的一种全局刻画（global characterization）也是可得的。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**定理 11.41（Theorem 11.41）**</span>：设 $E \subset \mathbb{R}^n$，并设 $f : E \to \mathbb{R}^m$。则 $f$ 在 $E$ 上连续当且仅当对 $\mathbb{R}^m$ 中的每个开集 $V$，集合

> <span style="color:#1e8449;">**[note]**</span> **注 18** 本节把连续性写成四种等价说法：ε-δ 定义（Definition 11.39）、极限式 $\lim_{x\to x_0}f(x)=f(x_0)$（只对聚点成立）、序列式（Lemma 11.30 免费赠予）、邻域式（$f(x_0)$ 的每个邻域 $V$ 都对应 $x_0$ 的邻域 $U$ 使 $f(U\cap E)\subset V$），共同内核是"靠近 $x_0$ 的点被送到靠近 $f(x_0)$ 的点"。孤立点自动连续靠的是空真：取 $\delta$ 小于 $x_0$ 到 $E$ 中其余点的最小距离，满足 $\|x-x_0\|<\delta$ 的 $x\in E$ 只有 $x_0$ 自己，条件无对象可违反——6.042 里的 vacuous truth（空真）在此正面出场。Theorem 11.41 的全局刻画"连续当且仅当每个开集 $V$ 的原像 $f^{-1}(V)$ 相对 $E$ 开"最值得记：证明两步（把 $f(x)$ 周围的 $\varepsilon$ 球塞进 $V$，再把 $x$ 周围的 $\delta$ 球拉回其中），而它只谈开集、不谈度量与序列，日后推广到一般拓扑空间时原句照抄即可——这就是拓扑学选它当连续性定义的原因；"相对 $E$ 开"（$f^{-1}(V)=E\cap O$）在 $E$ 非开时不可省略。Example 11.42 演示最危险的陷阱：$f(x,y)=2xy/(x^2+y^2)$ 对每个固定的 $x_0,y_0$，单变量函数 $f(x_0,\cdot)$ 与 $f(\cdot,y_0)$ 都连续，$f$ 在 $(0,0)$ 却不连续——逐变量连续（continuous in each variable separately）推不出联合连续，因为每个切片都看不见 Example 11.32 中沿不同方向逼近得到不同极限的事实。这与 6.431（Bertsekas & Tsitsiklis 第 3.4 节 Joint PDFs of Multiple Random Variables）里"边缘分布确定不了联合分布"是同一结构：固定变量后的一维信息拼不回二维全貌。

```math
f^{-1}(V) = \{x \in E : f(x) \in V\}
```

是（相对于 $E$ 的）开集。［这意味着 $f^{-1}(V)$ 是 $E$ 与 $\mathbb{R}^n$ 中某个开子集的交集。］特别地，若 $E$ 是开集，则 $f$ 连续当且仅当对 $\mathbb{R}^m$ 中的每个开集 $V$，集合 $f^{-1}(V)$ 在 $\mathbb{R}^n$ 中是开集。

关于函数的和（sum）、数乘（multiplication by a scalar）以及点积（dot product）的预期连续性法则，对向量值函数（vector-valued function）仍然成立；它们的证明只需援引 定理 11.37 和 定理 11.38 中相应的极限法则即可。

由定理 11.36 我们推知：向量值函数 $f$ 在点 $x_0$ 处连续当且仅当它的所有坐标函数（coordinate function）$f^i$ 都是 $x_0$ 处连续的实值函数。这一断言不应与下述错误的断言相混淆：一个多变量实值函数若「逐变量分别连续」（continuous in each variable separately），则它连续。

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b;">**例 11.42（Example 11.42）**</span>：再次考虑 Example 11.32，

```math
f(x, y) = \frac{2xy}{x^2 + y^2}, \quad f(0, 0) = 0
```

对每个固定的 $x = x_0$，$f(x_0, \cdot)$ 在 $\mathbb{R}$ 上连续；函数 $f(\cdot, y_0) : \mathbb{R} \to \mathbb{R}$ 也是如此。但 $f$ 在 $(0, 0)$ 处不连续，因为极限 $\lim_{(x,y) \to (0,0)} f(x, y)$ 不存在。另请参见 Exercises 11.7.12 与 11.7.13。$\square$

---

### 书页 460（习题区）

<span style="color:#7f8c8d;">*（本页为 §11.7 节习题区，按约定跳过。）*</span>

---

<span style="color:#7f8c8d">*（本页起始部分为前一节 §11.7 习题区的延续：一道讨论"函数逐变量连续时二重极限与累次极限"的 (a)(b)(c) 小题，附 SEE NOTE 271，按约定跳过。）*</span>

### §11.8 $\mathbb{R}^n$ 中的紧致集（Compact Sets in $\mathbb{R}^n$）

<span style="color:#2471a3;">**[section]**</span>
在 §4.5 中，我们为 $\mathbb{R}$ 的子集引入了紧致性（compactness）这一重要概念。
本节中，我们将此概念推广到 $\mathbb{R}^n$ 的子集。
在下一节我们将看到，定义于 $\mathbb{R}$ 的紧致子集上的连续函数所具有的性质，可以推广到定义于 $\mathbb{R}^n$ 的紧致子集上的连续函数。
在 $\mathbb{R}^n$ 的框架下，我们可以为"紧致集（compact set）"给出许多等价的定义。
（在 §4.5 中我们看到，$\mathbb{R}$ 中的一个集合若是闭且有界，或者具有 Bolzano-Weierstrass 性质，或者具有 Heine-Borel 性质，它就是紧致的。）
由于我们已经得到了 Bolzano-Weierstrass 定理（Theorem 11.19），自然应以序列概念为基础来给出我们的定义。

<span style="color:#2471a3;">**[definition]**</span> **<span style="color:#c0392b">定义 11.43</span>**
<span style="color:#00838f">集合 $E \subset \mathbb{R}^n$ 称为紧致集（compact），如果 $E$ 中的每个序列都有一个收敛子序列（convergent subsequence），其极限仍在 $E$ 中。</span>

<span style="color:#2471a3;">**[theorem]**</span> **<span style="color:#c0392b">定理 11.44</span>** 集合 $E \subset \mathbb{R}^n$ 是紧致的，当且仅当 $E$ 是闭且有界的。

> <span style="color:#1e8449;">**[note]**</span> **注 19** §4.5 为 $\mathbb{R}$ 的紧致性备好三种等价定义：闭且有界、Bolzano-Weierstrass 性质、Heine-Borel 性质；§11.8 推广到 $\mathbb{R}^n$ 时挑了序列版（Definition 11.43：$E$ 中每个序列都有收敛到 $E$ 中点的子序列），原因只有一个——Theorem 11.19（$\mathbb{R}^n$ 的 BW 定理）在 §11.4 已证好，定义贴着现成工具选，Theorem 11.44（紧致当且仅当闭且有界）便几乎白拿。正方向两段各司其职：有界性喂给 Theorem 11.19 得收敛子列，闭性（Exercise 11.3.1：闭集含全部聚点）把子列极限收进 $E$。反方向是两条一行反例机：不闭则存在聚点 $x_0\notin E$，按 Theorem 11.17 的半距离收缩取出 $E$ 中收敛到 $x_0$ 的序列，其一切子列也收敛到 $x_0\notin E$，定义当场破产；无界则存在 $\|x_k\|\ge k$ 的序列，而收敛序列必有界，故无收敛子列。开覆盖版（Heine-Borel 性质）留给 Exercise 11.8.2，那正是历史顺序：Heine（海涅，1821–1881，MacTutor 生平词条）1872 年在《Die Elemente der Functionenlehre》（J. reine angew. Math. 74）中用覆盖论证证明闭区间上连续函数一致连续；Borel（博雷尔，1871–1956，MacTutor 生平词条）1895 年博士论文《Sur quelques points de la théorie des fonctions》陈述并证明可数覆盖版本；Cousin 1895、Lebesgue 1898、Schoenflies 1900 相继推广到任意覆盖，Heine-Borel 之名随之固定。选序列版而非覆盖版是教学经济学：一维覆盖证明（Theorem 4.33）搬到 $\mathbb{R}^n$ 要重写，序列版则复用 §11.4 全部家当。

<span style="color:#2471a3;">**[proof]**</span> 证明。设 $E$ 是闭且有界的，设 $\{x_k\}$ 是 $E$ 中点的序列。
因 $E$ 有界，由 §11.4 的定理 11.19 知 $\{x_k\}$ 有收敛子序列 $\{x_{k_j}\}$。
令 $x_0 = \lim_{j\to\infty} x_{k_j}$。
那么 $x_0$ 是 $E$ 的聚点（limit point）。
因 $E$ 是闭的，故 $x_0 \in E$（由 Exercise 11.3.1）。
反之，设 $E$ 紧致。
我们用反证法证明 $E$ 是闭且有界的。
若 $E$ 不是闭的，则 $E$ 有一个聚点 $x_0 \notin E$。
这意味着存在 $E$ 中收敛到 $x_0$ 的序列 $\{x_k\}$。
该序列的每个子序列也都收敛到 $x_0$，因此 $\{x_k\}$ 不存在收敛到 $E$ 中某点的子序列。
所以 $E$ 必为闭集。
若 $E$ 无界，则存在 $E$ 中的序列 $\{x_k\}$，使得对所有 $k \in \mathbb{N}$ 有 $\|x_k\| \geq k$。
该序列没有收敛子序列。
因此 $E$ 必有界。$\square$

<span style="color:#2471a3;">**[corollary]**</span> **<span style="color:#c0392b">推论 11.45</span>** 集合 $E \subset \mathbb{R}^n$ 是闭且有界的，当且仅当 $E$ 的每个无限子集都有一个属于 $E$ 的聚点（point of accumulation）。

该证明由 定理 11.44 立即得出。
同样地，Heine-Borel 定理（Heine-Borel Theorem）也可以推广到 $\mathbb{R}^n$ 上。
我们将其留作 Exercise 11.8.2。

<span style="color:#7f8c8d">*（本页中部为 §11.8 习题区：Exercise 11.8.1、11.8.2 及 SEE NOTE 272，按约定跳过。）*</span>

### §11.9 紧致集上的连续函数（Continuous Functions on Compact Sets）

<span style="color:#2471a3;">**[section]**</span>
现在我们转向定义于 $\mathbb{R}^n$ 的紧致集上的连续函数的性质。
定义于 $\mathbb{R}$ 的紧致子集上的每个实值连续函数都具有三个基本性质：
函数的值域有界、函数达到其最大值与最小值、以及连续性是一致（uniform）的。
这些性质每一条都能以很少的周折推广到向量值函数（vector-valued functions）。

<span style="color:#2471a3;">**[theorem]**</span> **<span style="color:#c0392b">定理 11.46</span>** 若 $E \subset \mathbb{R}^n$ 紧致且 $f: E \to \mathbb{R}^m$ 在 $E$ 上连续，则集合 $f(E)$ 是紧致的。

<span style="color:#2471a3;">**[proof]**</span> 证明。设 $\{y_k\}$ 是集合 $f(E)$ 中的一个序列。
我们要证明 $\{y_k\}$ 有一个极限在 $f(E)$ 中的收敛子序列。
对每个 $k \in \mathbb{N}$，存在 $x_k \in E$ 使得 $f(x_k) = y_k$。
由于 $E$ 紧致，序列 $\{x_k\}$ 有收敛子序列 $\{x_{k_j}\}$，收敛到某点 $x_0 \in E$。
因 $f$ 在 $x_0$ 处连续，故 $f(x_0) = \lim_{j\to\infty} f(x_{k_j})$；又因 $x_0 \in E$，故 $f(x_0) \in f(E)$。
于是序列 $\{y_{k_j}\} = \{f(x_{k_j})\}$ 就是 $\{y_k\}$ 的一个收敛子序列，收敛到点 $f(x_0) \in f(E)$。$\square$

<span style="color:#2471a3;">**[corollary]**</span> **<span style="color:#c0392b">推论 11.47</span>** 设 $E \subset \mathbb{R}^n$ 紧致，设 $f: E \to \mathbb{R}$ 连续。

> <span style="color:#1e8449;">**[note]**</span> **注 20** Theorem 11.46 的证明值得存为"拉回—提子—推前"模板：要证 $f(E)$ 紧致，取 $f(E)$ 中任意序列 $\{y_k\}$；对每个 $k$ 在 $E$ 中挑一个原像 $x_k$（$f(x_k)=y_k$，原像未必唯一，任选其一即可，存在性选择不改变结论）；$E$ 紧致给出子列 $x_{k_j}\to x_0\in E$；$f$ 在 $x_0$ 连续把收敛推前到像空间：$y_{k_j}=f(x_{k_j})\to f(x_0)\in f(E)$。三步中紧致性只在定义域用一次、连续性只在极限点用一次，两个假设各自只干一件事——好证明的接口设计。Corollary 11.47 由此得到极值定理：紧致集上连续实函数达到绝对最大值与最小值，链条是"$f(E)$ 紧致 $\Rightarrow$ 闭且有界（Theorem 11.44）$\Rightarrow$ 最小包含区间 $[c,d]$ 存在 $\Rightarrow$ 闭性把 $c,d$ 收回 $f(E)$"。这条定理是整个最优化理论的存在性条款：Boyd《Convex Optimization》§4.1.1（Basic terminology）定义最优值 $p^*=\inf f_0$ 时强调，只有存在可行点 $x^*$ 使 $f_0(x^*)=p^*$ 才称最优值 attained（可达）、问题 solvable（可解）——紧致可行集正是保证可达的充分条件；可行集不紧致时下确界可以永远够不着：在 $x>0$ 上最小化 $1/x$，下确界 $0$ 却无点可取。凸优化里"最优解存在"的假设，本质是借这条分析定理。
那么 $f$ 在 $E$ 上达到绝对最大值（absolute maximum）与绝对最小值（absolute minimum）。

<span style="color:#2471a3;">**[proof]**</span> 证明。由 定理 11.46，集合 $f(E)$ 是 $\mathbb{R}$ 的紧致子集。
因此由 定理 11.44，$f(E)$ 是闭且有界的。
设 $[c, d]$ 是包含 $f(E)$ 的最小闭区间。
由于 $f(E)$ 有界，这样的区间存在。
因 $f(E)$ 是闭的，故 $c \in f(E)$ 且 $d \in f(E)$。
数 $c$ 是 $f$ 在 $E$ 上的绝对最小值，数 $d$ 是 $f$ 在 $E$ 上的绝对最大值。$\square$

---

<span style="color:#7f8c8d">*（书页 463 译文，§11.10 开头。）*</span>

# §11.10 补充说明（Additional Remarks）

> <span style="color:#1e8449;">**[note]**</span> **注 22** 本节从结构反差开场：$\mathbb{R}$ 的开集被 Theorem 4.15（可数个两两不交开区间的并）管得规规矩矩，而 $\mathbb{R}^n$（$n\ge2$）里一个圆周就能同时充当内外两个不相交开集的公共边界——维数加一，边界复杂度暴涨。文中追问三个、五个、无穷多个不相交开集共边界的构造，答案是可以且自然出现：Lakes of Wada（和田湖，1917 年发表于《Tôhoku Mathematical Journal》第 12 卷的构造）给出三个互不相交区域共享一条连通却不含任何弧的边界；脚注 1 指向 Hubbard 1999 年的短文（Amer. Math. Monthly 106:8, 745–747），说明受迫阻尼摆等动力学系统的吸引盆边界会自然产生这类集合。四色问题正是被边界现象逼出严谨表述的：1852 年 Francis Guthrie 向 De Morgan 提问，后者当天写信给 Hamilton（MacTutor 专题文章《The Four Colour Theorem》）；Kempe（肯佩，1849–1922）1879 年用 Kempe chain（肯佩链）给出证明，十一年后被 Heawood（希伍德，1861–1955）1890 年找出漏洞、退而证明五色足够；1976 年 Appel（1932–2013，MacTutor 生平词条）与 Haken（1928–2022，AMS Notices 2023 年 10 月号讣告）用上千小时机时完成证明，成为第一个靠计算机验证、人力无法逐行核查的重大定理。文中的反例逻辑值得存：五个有界开集若共享边界 $B$ 则两两相邻，松散陈述下必须五色——所以真定理必须限制区域类型与边界形状，6.042 图论部分把它严格化为 planar graph（平面图）4-可着色。1996 年 Robertson–Sanders–Seymour–Thomas 给出只需 633 个构形的新证明（Electron. Res. Announc. AMS 2），把机器证明的规模缩小两个数量级。

<span style="color:#2471a3;">**[section]**</span> **11.10 补充说明（Additional Remarks）**

**一致连续性（Uniform Continuity）**

我们关于一致连续性（uniform continuity）的定义把 §5.6 中的概念推广到了向量值函数（vector-valued functions）。

<span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f;">**定义 11.48.**</span> 设 $E \subset \mathbb{R}^n$，并设 $f : E \to \mathbb{R}^m$。若对每一个 $\varepsilon > 0$ 都存在 $\delta > 0$，使得只要 $x, y \in E$ 且 $\|x - y\| < \delta$，就有 $\|f(x) - f(y)\| < \varepsilon$，则称 $f$ 在 $E$ 上一致连续。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**定理 11.49（Theorem 11.49）**</span> 若 $E \subset \mathbb{R}^n$ 是紧致集（compact set），且 $f : E \to \mathbb{R}^m$ 在 $E$ 上连续，则 $f$ 在 $E$ 上一致连续。

> <span style="color:#1e8449;">**[note]**</span> **注 21** Definition 11.48 与 Definition 11.39 只差一个量词换位：点连续是"先给 $x_0$，后选 $\delta(x_0,\varepsilon)$"，一致连续是"先给 $\varepsilon$，选一个 $\delta(\varepsilon)$ 服务全体点对"——$\delta$ 与位置无关，uniform（一致）二字的全部含义在此。换位是实质加强：$f(x)=1/x$ 在 $(0,1]$ 处处连续却不一致连续，因为 $|1/x-1/y|=|x-y|/(xy)$ 的分母在原点附近趋于 $0$，同样的 $\delta$ 能引起的像差可以任意大，各点所需的 $\delta$ 越靠左越小、无一致下限。Theorem 11.49 说紧致性恰好把逐点依赖整体压平，证明（与 Theorem 5.48 逐字相同）仍是 Lemma 11.30 那台否定机器：假设非一致连续，则存在 $\varepsilon_0>0$ 与点对 $x_k,y_k$ 满足 $\|x_k-y_k\|<1/k$ 却 $\|f(x_k)-f(y_k)\|\ge\varepsilon_0$；先对 $x_k$ 用 BW 抽收敛子列，再在对应子列里对 $y_k$ 抽一次，因 $\|x_k-y_k\|\to0$ 两者极限同为 $x_0$；连续性要求两串像都趋于 $f(x_0)$，与恒 $\ge\varepsilon_0$ 的间距矛盾。$\delta$ 与位置无关在数值上就是"误差界全局统一"：Exercise 11.9.1（一致连续于有界集 $\Rightarrow$ 有界）正说明一致连续把局部估计升级成全域估计，数值算法要的正是这种不随位置缩水的误差承诺。同一个否定机器也顺手验证 $x^2$ 在 $\mathbb{R}$ 上不一致连续：取 $x_k=k$、$y_k=k+1/k$，则 $|x_k-y_k|=1/k\to0$ 而 $|x_k^2-y_k^2|=2+1/k^2\ge2$，间距永远压不进 $\varepsilon_0=1$。

<span style="color:#2471a3;">**[proof]**</span> 证明与 定理 5.48 的证明完全相同，只需把绝对值号替换为范数 $\|\cdot\|$ 即可。$\square$

> <span style="color:#7f8c8d">*（本页其余部分为 §11.9 的习题区（Exercises 11.9.1–11.9.6），按约定跳过。）*</span>

<span style="color:#2471a3;">**[section]**</span> **11.10 补充说明（Additional Remarks）**

> <span style="color:#1e8449;">补充性章节（Enrichment section），可以略过。</span>

在本节中，我们提及一些内容，它们在下一章中不会用到，但或许会引起读者的兴趣。

<span style="color:#7f8c8d">*（以下为书页 464 的内容。）*</span>

<span style="color:#2471a3;">**[note]**</span> **关于 $\mathbb{R}^n$ 中的开集与闭集（On Open and Closed Sets in $\mathbb{R}^n$）**

我们在第 4 章已经看到，$\mathbb{R}$ 中的开集（open set）具有特别简单的结构。
在 $\mathbb{R}$ 中，每一个非空开子集都可以表示成有限个或可数无穷多个两两不相交（pairwise disjoint）开区间（open interval）的并集（Theorem 4.15）。
而 $\mathbb{R}$ 中的闭集（closed set）则相对容易想象。
它们由区间、孤立点（isolated point）、孤立点的极限等对象组成，此外还有 Cantor 集（Cantor set）。

而相比之下，$\mathbb{R}^n$（$n \ge 2$）中的开集或闭集就可能复杂得多了。
例如，要构想一个同时充当两个不相交开集的公共边界（common boundary）的闭集是很容易的——一个圆周就能胜任。
把圆的内部和外部视为那两个不相交的开集即可。
你能否构造出一个闭集，使其成为三个两两不相交开集的公共边界？五个呢？无穷多个呢？
这类集合的构造并不容易，但它们确实存在，而且能以自然的方式产生。$^1$

这些开集必然是非常"蜿蜒"（wiggly）的集合，它们的公共边界 $B$ 是连通的（connected，其意义由 定义 11.50 引入），然而 $B$ 却不含任何弧（arc）！
你能想象出这样的集合 $B$ 吗？

<span style="color:#2471a3;">**[note]**</span> **四色问题（The Four-Color Problem）**

这个著名的问题$^2$ 最终于 1976 年以肯定的方式得到解决，而在那之前的一百多年里，许多数学家都曾徒劳地尝试求解它。

用松散的语言来说，最初于 1852 年提出的四色问题（four-color problem）问的是：平面上任意地图的各区域能否用至多四种颜色着色，使得凡是公共边界包含多于一个点的区域都各具不同的颜色。

然而，1976 年最终宣布的该问题的解答至今仍有争议，因为其证明需要数百页的篇幅以及数千小时的计算机验证。

我们前面关于高维空间中集合边界的评注，说明了精确陈述问题的重要性。
假设 $E_1, E_2, \ldots, E_5$ 是以 $B$ 为公共边界的有界开集。
那么给由此得到的地图着色就需要五种颜色。
这会违背我们以松散方式陈述的四色定理。
当然，真正的四色定理（four-color theorem）是被严谨陈述的，因此所允许的区域类型以及它们的公共边界都被恰当地加以限制。

<span style="color:#2471a3;">**[note]**</span> **叉积（Cross Products）**

我们已大量使用了 $\mathbb{R}^n$ 中两个向量的点积（dot product）$x \cdot y$。
在特殊情形 $n = 3$ 下，还有另一种重要的乘积，即叉积（cross product）或向量积（vector product），记作 $x \times y$。
对任意两个向量 $x = (x_1, x_2, x_3)$ 与 $y = (y_1, y_2, y_3)$，我们定义

```math
x \times y = (x_2 y_3 - x_3 y_2,\ x_3 y_1 - x_1 y_3,\ x_1 y_2 - x_2 y_1)
```

叉积在数学和物理的许多分支中都很重要。
在后续章节中我们不会用到它，因此这里就不作展开了。
我们只提及一点：$x \times y$ 是垂直于由 $x$ 与 $y$ 所确定的平面的一个向量。

> 脚注 $^1$：一段有趣的简短讨论及原始参考文献可见 J. H. Hubbard, *The Forced Damped Pendulum: Chaos, Complication and Control*, Amer. Math. Monthly, 106, No. 8 (Oct. 1999), pp. 745–747。

> 脚注 $^2$：关于该主题有一本面向普通读者的有趣著作：R. 与 G. Fritsch 合著，*The Four Color Theorem*（Springer-Verlag, 1998）。

---

<span style="color:#2471a3;">**[section]**</span> **§11.10 补充说明（Additional Remarks）**（续）

向量 x 与 y 的叉积（cross product）$x\times y$ 垂直于由 x 与 y 张成的平面，其长度由公式

```math
\|x\times y\| = \|x\|\,\|y\|\,\sin\theta,
```

给出，其中 $0\le\theta\le\pi$ 是向量 x 与 y 所确定的夹角（angle）。

从几何上看，$\|x\times y\|$ 就是以 x 与 y 为相邻两边的平行四边形（parallelogram）的面积（area）。

<span style="color:#2471a3;">**[section]**</span> **$\mathbb{R}^n$ 中的连通性（Connectedness in $\mathbb{R}^n$）**

在习题 11.3.7 中，我们为 $\mathbb{R}^n$ 中的开集定义了连通性（connectedness）。

开集 $D\subset\mathbb{R}^n$ 是连通的，条件是 D 中每一对点都能用一条完全位于 D 内的折线路径（polygonal path）连接起来。

连通性这一概念所刻画的，正是集合「连成一块」（one piece）这一性质。

那么对于那些并非开集的集合又该如何？闭圆盘（closed disk）、连续函数 $f:\mathbb{R}\to\mathbb{R}$ 的图像，以及集合 $A=\{(x,y):x^2\le y\le 2x^2\}$

都是 $\mathbb{R}^2$ 中并非开集、但看起来确乎连成一整块的子集。

涉及折线路径的那个定义适用于闭圆盘，也适用于某些——但并非全部——连续函数的图像。

它并不适用于集合 A，因为没有任何折线路径能够把原点与 A 中其他某个点连接起来。

下面给出 $\mathbb{R}^n$ 中连通性的一个更具一般性的定义。

<span style="color:#2471a3;">**[definition]**</span> **<span style="color:#c0392b;">定义 11.50（Definition 11.50）</span>**：

> <span style="color:#1e8449;">**[note]**</span> **注 23** Exercise 11.3.7 为开集定义的连通（折线路径连接任意两点）对闭圆盘有效，却在 $A=\{(x,y):x^2\le y\le 2x^2\}$ 上失效：从原点出发的任意直线段 $(t,mt)$ 要留在 $A$ 里就必须对所有小 $t$ 满足 $t^2\le mt\le 2t^2$，即 $t\le m\le 2t$ 对所有小 $t$ 成立，固定斜率 $m$ 做不到，而折线由有限段直线组成，第一段就出局。Definition 11.50 改用"分离"定义连通：存在不相交开集 $U,V$ 使 $S\subset U\cup V$ 且各自与 $S$ 相交时，$U,V$ 分离 $S$；不存在分离则 $S$ 连通。为什么分离必须用开集？因为分离必须发生在"空隙"处——若允许任意集合，$[0,1]$ 也会被 $\{0\}$ 与 $(0,1]$ 这类切法"分离"，连成一片的集合就被切碎；开集条件强制两半之间留出真正的间隙。这与 6.042 图论章连通分量的两条等价刻画一一对应：路径连通对应"任意两顶点间有 walk"，分离对应"顶点集无法分成两个无跨边的非空部分"；6.006 第 9–10 讲的 BFS/DFS 正是用搜索找出连通分量。Exercise 11.10.3（连续映射保持连通）与 11.10.4（连通集上的介值性质）说明这个拓扑概念是 Intermediate Value Theorem（介值定理）背后的通用引擎。

<span style="color:#00838f;">设 $S\subset\mathbb{R}^n$。若存在不相交的开集（disjoint open sets）U 与 V，使得 $S\subset U\cup V$，且 $S\cap U\neq\varnothing$ 与 $S\cap V\neq\varnothing$，</span>

<span style="color:#00838f;">则称 U 与 V 分离（separate）集合 S。</span>

<span style="color:#00838f;">若不存在任何能够分离 S 的开集 U、V，则称集合 S 是连通的（connected）。</span>

有了这个定义，前面提到的那些集合便全部都是连通的。

关于更多的例子，以及该定义与此前为开集所给出定义之间的一致性，请参见本节的习题。

> <span style="color:#7f8c8d">*（本页其余部分为 §11.10 习题区（习题 11.10.1–11.10.7），按约定跳过。）*</span>

---

### 书页 466（Notes 提示区）

> <span style="color:#7f8c8d">*（本页顶部为 §11.10 习题区（习题 11.10.8），下方为 Notes 262–274 提示区，全部属习题区/提示区，按约定整体跳过。）*</span>

---

# TBB《Elementary Real Analysis》§12.1–12.2 译文（书页 467–468）

---

## 书页 467

# 第 12 章 $\mathbb{R}^n$ 上的微分（Differentiation on $\mathbb{R}^n$）

### <span style="color:#2471a3;">**[section]**</span> 12.1 引言（Introduction）

> <span style="color:#1e8449;">**[note]**</span> **注 24** §12.1 引言是一张教学地图：它坦率指出初学微积分者会算偏导数，却说不清 differentiability（可微性）在 $n=2$ 时"切平面存在"之外的含义，也说 differential（微分）与链式法则难掌握——全章围绕这个认知缺口展开。书中自述的写作策略可直接挪用为学习策略：难主题先开"铺垫"节、把证明推迟到下一节；特例先行、一般情形后置；涉线性代数的 Section 12.8 标 $*$ 可跳过——先建概念图像，再补抽象骨架。历史上的先驱（Newton 1643–1727、Leibniz 1646–1716，均见 MacTutor 生平词条）确实只是"把每个变量分别求导"就把微积分搬到多元函数上，但这种逐变量操作缺少统一理论；记号也走过弯路：偏导符号 $\partial$ 由 Legendre（勒让德，1752–1833）1786 年在变分法论文中首用后弃用，Jacobi（雅可比，1804–1851）1841 年在《De determinantibus functionalibus》（Crelle J. 22）中重新引入并推广，而 Condorcet 1770 年已用 $\partial$ 表示偏差分（MacTutor「Earliest Uses of Symbols of Calculus」词条）。本章终点是把逐变量求导升级为一条线性映射：$f(x_0+h)\approx f(x_0)+L(h)$，其中 $L$ 就是 Strang 第 1 章"$Ax$ 是 $A$ 的列的线性组合"里的那种映射——可微性即局部可被线性映射逼近，链式法则即复合映射的导数矩阵相乘。这套产物是后续课程的直接依赖：Boyd《Convex Optimization》§9.3 梯度下降法靠 gradient（梯度）迭代，§9.5 牛顿法靠 Hessian（海塞矩阵）做二阶修正，都是本章偏导数与微分概念在优化中的落地。

我们假定你已经熟悉与多元函数（functions of several variables）的微分相关的各种概念。

这种熟悉应当包括对偏导数（partial derivative）和方向导数（directional derivative）的一定理解，包括在处理二元函数时它们如何用于得到切线（tangent line）和切平面（tangent plane），并且包括对偏导数的计算相当熟练。

初等微积分课程的学生通常能掌握多元函数微分中一些较简单的概念，但在理解可微性（differentiability）的含义方面却可能有更多困难——除了知道对 $n = 2$ 它意味着切平面存在之外。

与微分（differential）或各种链式法则（chain rule）相关的概念往往难以把握。

在本章中，我们研究多元函数微分的相关概念。

我们从固定偏导数与方向导数的记号开始，然后从容地讨论若干专题。

当我们的经验告诉我们学生对某个专题感到困难时，我们就用一整节来「铺垫」该材料，把证明留给下一节；

或者，我们以特殊情形开篇，推迟一般情形，直到我们相信你已经对这一专题感到自如为止。

微分正是一个恰当的例子。

如果你基础扎实，你可以迅速前进到 12.8 节，只快速浏览前面的大部分材料。

一个更为循序渐进的办法是：先用前面的各节让自己熟悉可微性、微分和链式法则这些概念，然后再去攻克从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的映射（mapping）这一更抽象的设定。

我们用 `*` 号标记了那一节，表示它可以省略，因为它涉及一点线性代数（linear algebra）——而前面各节只用到极少的线性代数。

### <span style="color:#2471a3;">**[section]**</span> 12.2 偏导数与方向导数（Partial and Directional Derivatives）

对于二元函数 $f(x, y)$，研究导数有一个显而易见的初步尝试。

本学科的先驱们（牛顿 Newton、莱布尼茨 Leibniz 等人）仅仅按照微积分的通常法则、把每个变量单独处理来求导，就把微积分技巧推广到了这类函数上。

这个例子及其记号，学生应当从先前的课程中就已熟悉。

---

## 书页 468

<span style="color:#2471a3;">**[figure]**</span> **Figure 12.1.** 函数 $f(x, y) = \frac{1}{3}\sqrt{36 - 4x^2 - y^2}$ 在点 $(1, 3, \sqrt{23}/3)$ 处的切线

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">**例 12.1（Example 12.1）.**</span> 设 $f(x, y) = \left(\sqrt{36 - 4x^2 - y^2}\right)/3$。

你可能会认出，这个函数对应的曲面是半个椭球面（ellipsoid）。

$f$ 的偏导数为

```math
\frac{\partial}{\partial x} f(x, y) = \frac{-4x}{3\sqrt{36 - 4x^2 - y^2}} \qquad\text{以及}\qquad \frac{\partial}{\partial y} f(x, y) = \frac{-y}{3\sqrt{36 - 4x^2 - y^2}}.
```

更正式地说，这里发生的事情可以拿来与一元函数 $f(x)$ 的导数的通常定义作比较：

```math
\frac{d}{dx} f(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}.
```

对 $f(x, y)$ 来说，过程就是进行同样的计算，但全程把 $y$ 当作固定常数：

```math
\frac{\partial}{\partial x} f(x, y) = \lim_{h \to 0} \frac{f(x + h, y) - f(x, y)}{h},
```

然后再把 $x$ 当作固定常数：

```math
\frac{\partial}{\partial y} f(x, y) = \lim_{h \to 0} \frac{f(x, y + h) - f(x, y)}{h}.
```

这就是我们取作二元函数导数的定义；对于更多变量的情形，推广是类似的。

当变量多于两三个时，我们宁愿用下标记号（subscript notation）来代替 $\frac{\partial}{\partial x}$ 这种记号。

在点 $(x_0, y_0)$ 处，偏导数 $f_1 = \frac{\partial f}{\partial x}$ 和 $f_2 = \frac{\partial f}{\partial y}$ 提供了曲面 $z = f(x, y)$ 上两条特定切线的斜率。

它们分别是平面 $x = x_0$ 和 $y = y_0$ 中过点 $(x_0, y_0, z_0)$ 且与曲面相切的那两条直线。

图 12.1 展示了例 12.1 中的函数在点 $(x_0, y_0, z_0) = (1, 3, \sqrt{23}/3)$ 处的这些切线。

建立两个或更多变量函数微分理论的这些最初简单步骤，曾很好地服务于微积分学的先驱们。

然而，正如我们将要看到的，要想进一步深入，就需要对微分作更深刻的考察。

---

---

<span style="color:#2471a3;">**[section]**</span>

### 12.2 节 偏导数与方向导数（Partial and Directional Derivatives）

<span style="color:#2471a3;">**[section]**</span>

### 12.2.1 偏导数（Partial Derivatives）

设 $f: D \to \mathbb{R}$，其中 $D$ 是 $\mathbb{R}^n$ 的一个开子集（open subset）。令 $x = (x_1, \ldots, x_n) \in D$。

若我们允许 $x$ 的某一个坐标，比如说 $x_i$，在其余坐标保持固定的情形下变动，便得到关于单变量 $x_i$ 的一个函数。可将此函数记为

```math
f(x_1, x_2, \ldots, x_{i-1}, \cdot, x_{i+1}, \ldots, x_n) \tag{1}
```

第 $i$ 个位置上的点号表示：$x_i$ 可以变动，但须满足约束，即点 $(x_1, x_2, \ldots, x_{i-1}, x_i, x_{i+1}, \ldots, x_n)$ 必须位于 $D$ 之中。

<span style="color:#00838f;">若函数（1）在 $x$ 处的导数存在，便得到 $f$ 在 $x$ 处关于 $x_i$ 的偏导数（partial derivative）。</span> 我们把这一偏导数记为 $f_i(x)$ 或 $f_i(x_1, \ldots, x_n)$。于是

```math
f_i(x) = \lim_{h \to 0} \frac{f(x_1, \ldots, x_i + h, \ldots, x_n) - f(x_1, \ldots, x_i, \ldots, x_n)}{h}. \tag{2}
```

<span style="color:#1e8449;">**[note]**</span> 注记。正如一元导数（ordinary derivative）的情形一样，这里也是不同场合有时需要不同记法，因此如今已有多种记法在使用。例如 $f_i(x)$ 常写作 $\frac{\partial f}{\partial x_i}(x)$ 或 $f_{x_i}(x)$。若记 $u = f(x_1, \ldots, x_n)$，我们常以 $u_i$、$\frac{\partial u}{\partial x_i}$ 或 $u_{x_i}$ 取代 $f_i$、$\frac{\partial f}{\partial x_i}$ 或 $f_{x_i}$。当然，当只涉及少数几个变量时，用 $x, y, z$ 而不用 $x_1, x_2, x_3$ 来命名这些变量，往往更加方便。

<span style="color:#2471a3;">**[section]**</span>

### 二阶偏导数（Second-Order Partial Derivatives）

函数 $f(x)$ 的偏导数 $f_i$ 自身也是 $x$ 的函数。若它们在 $x$ 的某个邻域（neighborhood）内所有点处均有定义，则它们在 $x$ 处也可能拥有自己的偏导数。这些偏导数称为 $f$ 在 $x$ 处的二阶偏导数（second partial derivatives），即第二阶的偏导数。

二阶偏导最多可有 $n^2$ 个。例如当 $n = 2$ 时，可定义四个二阶偏导数：

```math
\frac{\partial}{\partial x}\left(\frac{\partial f}{\partial x}\right) = \frac{\partial^2 f}{\partial x^2}, \qquad
\frac{\partial}{\partial y}\left(\frac{\partial f}{\partial y}\right) = \frac{\partial^2 f}{\partial y^2},
```

```math
\frac{\partial}{\partial x}\left(\frac{\partial f}{\partial y}\right) = \frac{\partial^2 f}{\partial x\,\partial y}, \qquad
\frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right) = \frac{\partial^2 f}{\partial y\,\partial x}.
```

同时涉及 $x$ 与 $y$ 的两个偏导数常称为交叉偏导数（cross partials）或混合偏导数（mixed partials）。我们很快会看到，混合偏导数 $\frac{\partial^2 f}{\partial y\partial x}$ 与 $\frac{\partial^2 f}{\partial x\partial y}$ 相等这一结论常常成立，但并非总是成立。无论如何，务必领会它们表示两种不同的对象，并且要能从记号中分辨出哪个导数先被求取。

对 $n$ 元函数 $f$ 而言，其一个典型二阶偏导数可记为

```math
\frac{\partial}{\partial x_i}\left(\frac{\partial f}{\partial x_j}\right) = \frac{\partial^2 f}{\partial x_i\,\partial x_j}.
```

再次注意先执行的是哪一个求导。若用 $f_1$ 表示 $\frac{\partial f}{\partial x}$，那么二阶偏导数该用什么记号呢？自然的做法是用 $f_{12}$ 表示 $\frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right)$，因为我们希望 $f_{12}$ 是 $(f_1)_2$ 的简写。若如此约定，则在一种意义上保持了顺序；但在另一种意义上却把它颠倒了，因为对 $f_{12}$ 我们是从左到右复合（即 $(f_1)_2$），而在 $\frac{\partial^2 f}{\partial y\partial x}$ 中则是从右到左复合。尽管如此，我们仍采用 $f_{12}$ 表示 $(f_1)_2$，因为它在操作上略微简单一些。无论如何不会产生混淆，因为同时使用"$f_{ij}$"记号与"$\frac{\partial^2 f}{\partial x_i\partial x_j}$"记号的地方很少。

<span style="color:#1e8449;">**[note]**</span> 注记。我们顺带指出，有些作者采用相反的记号，例如以 $\frac{\partial^2 f}{\partial x\partial y}$ 表示 $\frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right)$。我们偏爱自己的记号，因为它保持了复合的次序；但在阅读涉及混合偏导数的材料（其他书籍）时，你应当意识到那里可能通行另一套约定。

<span style="color:#2471a3;">**[section]**</span>

### 高阶偏导数（Higher-Order Partial Derivatives）

我们还可以考虑更高阶的偏导数。例如 $\frac{\partial^3 f}{\partial x\partial y\partial y}$ 将表示 $\frac{\partial}{\partial x}\left(\frac{\partial^2 f}{\partial y^2}\right)$，也可写作 $f_{221}$，即 $(f_{22})_1$。与先前一样，求导的次序由记号本身给出，这一约定必须牢记。

<span style="color:#7f8c8d">*（本页其余部分为 12.2 节习题区，按约定跳过。）*</span>

---

## 书页 471

<span style="color:#7f8c8d">*（本页顶部为 §12.2.1 偏导数习题区 Exercises 的延续，按约定跳过。）*</span>

### <span style="color:#2471a3;">**[section]**</span> 12.2.2 方向导数（Directional Derivatives）

考虑一个二元函数 $f$。

偏导数（partial derivative）$f_1$ 和 $f_2$ 在点 $(x_0, y_0)$ 处给出了曲面在两个方向上的两条切线（tangent line）的斜率（再次参见 Figure 12.1）。

过点 $(x_0, y_0, z_0)$ 还可能有对应其他竖直平面的切线，这些平面不平行于坐标平面 $x = 0$ 或 $y = 0$。

这些切线在点 $(x_0, y_0, z_0)$ 处的斜率可以通过计算方向导数（directional derivative）来获得。

<span style="color:#2471a3;">**[definition]**</span> <span style="color:#c0392b">**定义 12.2.**</span> 设 $f: \mathbb{R}^2 \to \mathbb{R}$，并设 $u = (u_1, u_2)$ 是 $\mathbb{R}^2$ 中的一个单位向量（unit vector），即

> <span style="color:#1e8449;">**[note]**</span> **注 25** Definition 12.2 把二维问题化为一维：固定一个 unit vector（单位向量）$u$，构造切片函数 $\varphi(t)=f(x_0+tu_1,y_0+tu_2)$，directional derivative（方向导数）$D_u f$ 就是 $\varphi'(0)$——先沿直线走、再求普通一元导数，定义本身不引入任何新机器。要求 $\|u\|=1$ 的原因值得亲手验证：把 $u$ 换成 $cu$，同一个极限整体乘上常数 $c$；只有单位化后分母 $t$ 才等于实际走过的距离 $|t|$，商才是「单位长度上的增量」，即真正的变化率（rate of change）。偏导数是它的特例：$f_1=D_{(1,0)}f$、$f_2=D_{(0,1)}f$，方向导数把偏导数吸收进一个统一框架。既然 $D_u f$ 就是切片函数在 $0$ 点的一元导数，一元微积分的全部定理都可以沿这条直线调用——这是后续证明多元命题的标准杠杆。但方向导数只携带一条直线上的信息：§11.7 的 Example 11.42 已展示「每个切片连续推不出整体连续」，书页 482–483 的 Example 12.15 还将给出偏导存在却不可微的类似教训，多方向的一维信息拼不回二维全貌——这正是本章要另立可微性概念的原因。最优化里这条定义是选方向的原语：Boyd《Convex Optimization》§9.3 梯度下降每步就是选一个方向 $u$、沿 $x+tu$ 前进，方向导数就是比较各候选方向增长快慢的标尺。

```math
\|u\| = \sqrt{u_1^2 + u_2^2} = 1.
```

<span style="color:#00838f;">$f$ 在点 $(x_0, y_0)$ 处沿方向 $u$ 的方向导数定义为</span>

```math
D_u f(x_0, y_0) = \lim_{t \to 0} \frac{f(x_0 + t u_1, y_0 + t u_2) - f(x_0, y_0)}{t}, \tag{4}
```

若该极限存在。

正如偏导数度量 $f$ 在 $x$ 方向与 $y$ 方向上的变化率一样，$D_u f(x_0, y_0)$ 度量的是 $f$ 沿向量 $u$ 方向的变化率。

事实上，我们应当意识到，偏导数本身就是方向导数：$f_1$ 和 $f_2$ 分别是方向 $(1, 0)$ 与 $(0, 1)$ 上的方向导数，

即 $f_1 = D_{(1,0)}$，$f_2 = D_{(0,1)}$。

---

## 书页 472

<span style="color:#2471a3;">**[figure]**</span> **Figure 12.2.** 函数 $f(x, y) = x^2 + xy + 2$ 在点 $(1, 1)$ 处沿方向 $(1/2, \sqrt{3}/2)$ 的方向导数

甚至存在某种意义上的逆命题（converse）：稍后我们将看到，在适当的附加假设之下，只要知道了偏导数，就能写出所有方向上的导数。

注意，若 $D_u f(x_0, y_0)$ 存在，则反方向（opposite direction）上的导数 $D_{-u} f(x_0, y_0)$ 也存在，并且

```math
D_{-u} f(x_0, y_0) = -D_u f(x_0, y_0).
```

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">**例 12.3（Example 12.3）.**</span> 设 $f(x, y) = x^2 + xy + 2$，$u = (1/2, \sqrt{3}/2)$。

> <span style="color:#1e8449;">**[note]**</span> **注 26** Example 12.3 用两种算法算出同一个数：直接把 $f(1+\tfrac12 t,1+\tfrac{\sqrt3}{2}t)$ 展开除以 $t$，线性项 $\tfrac32+\tfrac{\sqrt3}{2}$ 留下、二次项 $(\tfrac14+\tfrac{\sqrt3}{4})t$ 随 $t\to0$ 消失；再用预告公式 $D_u f=(f_1,f_2)\cdot(u_1,u_2)$ 得 $(3,1)\cdot(\tfrac12,\tfrac{\sqrt3}{2})$，结果一致。展开式中 $t$ 的系数恰好是 $f_1u_1+f_2u_2$ 不是巧合：多项式沿直线代入后只剩线性项与 $t^2$ 阶余项，除以 $t$ 后余项归零——对多项式，方向导数公式就是「展开、取 $t$ 的系数」。向量 $(f_1,f_2)$ 称为 gradient（梯度）$\nabla f$；公式为什么必是点积？固定点后映射 $u\mapsto f_1u_1+f_2u_2$ 对 $u$ 是线性的，而 Example 11.24 证明过 $\mathbb{R}^2$ 上每个线性函数都是与某个固定向量的点积，这个向量正是 $\nabla f$。用定理 11.5（Cauchy-Schwarz）还能顺手求出最优方向：$D_u f=\nabla f\cdot u\le\|\nabla f\|\|u\|=\|\nabla f\|$，等号当且仅当 $u$ 与 $\nabla f$ 同向——梯度指向最陡上升方向、$\|\nabla f\|$ 是最大斜率，这正是 Boyd §9.3 梯度法 $x_{k+1}=x_k-t_k\nabla f(x_k)$ 选 $-\nabla f$ 为最陡下降方向的理论依据。$D_{-u}f=-D_u f$ 只需在极限中把 $t$ 换成 $-t$ 即可验证。最后盯住书中「适当假设」四字：公式需要比偏导存在更强的条件（§12.4 的可微性），Example 12.15 将给出偏导存在而公式失效的反例。

为计算 $D_u f(1, 1)$，我们计算

```math
\frac{f(1 + \frac{1}{2}t, 1 + \frac{\sqrt{3}}{2}t) - f(1, 1)}{t}
= \frac{(\frac{3}{2} + \frac{\sqrt{3}}{2})t + (\frac{1}{4} + \frac{\sqrt{3}}{4})t^2}{t}
\to \frac{3}{2} + \frac{\sqrt{3}}{2} \qquad (t \to 0).
```

稍后我们将看到，在合适的假设之下，我们可以按下式来计算方向导数：

```math
D_u f = (f_1, f_2) \cdot (u_1, u_2) = f_1 u_1 + f_2 u_2.
```

本例中 $f_1(1, 1) = 3$，$f_2(1, 1) = 1$，所以

```math
(3, 1) \cdot \left(\frac{1}{2}, \frac{\sqrt{3}}{2}\right) = \frac{3}{2} + \frac{\sqrt{3}}{2},
```

与我们先前计算的结果一致。

图 12.2 展示了 $f$ 的图像，并画出了点 $(1, 1)$ 处沿方向 $(1/2, \sqrt{3}/2)$ 的切线。$\square$

<span style="color:#7f8c8d">*（本页其余部分为 12.2 节习题区 Exercises，按约定跳过。）*</span>

---

### <span style="color:#2471a3;">**[section]**</span> 12.2.3 交叉偏导（Cross Partials）

设 $f$ 定义在区域（region）$D \subset \mathbb{R}^2$ 上，并假定两个偏导数（partial derivative）$\frac{\partial f}{\partial x}(x,y)$ 与 $\frac{\partial f}{\partial y}(x,y)$ 在 $D$ 中每一点 $(x,y)$ 处都存在。

这两个偏导数本身是 $D$ 上的函数，因此它们可能又拥有偏导数。

在这种情况下，存在四个可能的二阶偏导数（second-order partial derivative）：

```math
\frac{\partial^2 f}{\partial x^2}=\frac{\partial}{\partial x}\Bigl(\frac{\partial f}{\partial x}\Bigr),\qquad
\frac{\partial^2 f}{\partial y\partial x},\qquad
\frac{\partial^2 f}{\partial x\partial y},\qquad
\frac{\partial^2 f}{\partial y^2}=\frac{\partial}{\partial y}\Bigl(\frac{\partial f}{\partial y}\Bigr).
```

我们回忆一下，例如，我们的记号要求

```math
\frac{\partial^2 f}{\partial y\partial x}=\frac{\partial}{\partial y}\Bigl(\frac{\partial f}{\partial x}\Bigr).
```

两个偏导 $\frac{\partial^2 f}{\partial y\partial x}$ 与 $\frac{\partial^2 f}{\partial x\partial y}$ 常常被称为交叉偏导（cross partials）或混合偏导（mixed partials）。

初等微积分课程中的学生常常相信二阶偏导只有三个，因为通常成立

```math
\frac{\partial^2 f}{\partial y\partial x}=\frac{\partial^2 f}{\partial x\partial y}. \tag{5}
```

在本节中我们要确定 (5) 在何种条件下成立。我们从一个例子开始，它说明 (5) 并非总是成立。

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b;">**例 12.4（Example 12.4）**</span>：设

> <span style="color:#1e8449;">**[note]**</span> **注 27** Example 12.4 的计算值得逐行亲手重做：$f_1(0,y)=\lim_{h\to0}y(h^2-y^2)/(h^2+y^2)=-y$、$f_2(x,0)=x$，于是 $f_{12}(0,0)=\lim_{k\to0}(-k-0)/k=-1$ 而 $f_{21}(0,0)=1$——同一函数的两个 cross partials（交叉偏导，亦称 mixed partials 混合偏导）不相等。为什么可以不相等？$f_{12}$ 是先令 $h\to0$ 再令 $k\to0$，$f_{21}$ 顺序相反；两个 iterated limit（迭代极限）是两次一元极限的串联，而极限运算不满足交换律。书页 474 的表达式 (6)(7) 揭示根因：两者是同一个双重差分按两种顺序取极限，而 double limit（双重极限）$\lim_{(h,k)\to(0,0)}$ 根本不存在——这个现象你在 Example 9.7 的二重序列 $\{s_{nm}\}$ 与 Exercise 9.2.8 已经见过。对照 6.042 里的有限双重求和：$\sum_i\sum_j a_{ij}$ 的换序无条件成立（part1 注 2 用过），一旦「有限」换成「极限」，换序就必须用额外条件重新挣得——本书定理 12.5 与高数里绝对收敛级数的重排定理都是在挣这张许可证。机器上还要更小心：CSAPP 第 2 章指出浮点加法不满足结合律，用有限差分在计算机上数值计算 $f_{12}$ 与 $f_{21}$ 时，换序与舍入的差异会让两个本应相等的数出现微小不等，不能用数值结果反推数学结论。

```math
f(x,y)=\begin{cases}
\dfrac{xy(x^2-y^2)}{x^2+y^2}, & \text{若 }(x,y)\neq(0,0),\\[4pt]
0, & \text{若 }(x,y)=(0,0).
\end{cases}
```

利用下标记号，我们在点 $(0,0)$ 处计算偏导数

```math
f_1=\frac{\partial f}{\partial x},\qquad f_2=\frac{\partial f}{\partial y},\qquad
f_{12}=\frac{\partial^2 f}{\partial y\partial x},\qquad f_{21}=\frac{\partial^2 f}{\partial x\partial y}.
```

现在

```math
f_1(0,y)=\lim_{h\to0}\frac{f(h,y)-f(0,y)}{h}
=\lim_{h\to0}\frac{\dfrac{hy(h^2-y^2)}{h^2+y^2}}{h}=-y.
```

类似地，$f_2(x,0)=x$。由此推出

```math
f_{12}(0,0)=\lim_{k\to0}\frac{f_1(0,k)-f_1(0,0)}{k}=\frac{-k-0}{k}=-1,
```

以及

```math
f_{21}(0,0)=\lim_{h\to0}\frac{f_2(h,0)-f_2(0,0)}{h}=\lim_{h\to0}\frac{h-0}{h}=1.
```

因此这两个交叉偏导并不相等。

---

（以下为书页 474 的译文）

这里究竟「出了什么错」？考虑涉及 Example 12.4 中函数 $f$ 的两个相同的表达式：

```math
\frac{1}{k}\left[\frac{f(h,k)-f(0,k)}{h}-\frac{f(h,0)-f(0,0)}{h}\right], \tag{6}
```

```math
\frac{1}{h}\left[\frac{f(h,k)-f(h,0)}{k}-\frac{f(0,k)-f(0,0)}{k}\right]. \tag{7}
```

如果在 (6) 中先令 $h\to0$，然后再令 $k\to0$，我们就得到 $f_{12}(0,0)$。另一方面，在 (7) 中先令 $k\to0$，然后再令 $h\to0$，我们得到 $f_{21}(0,0)$。正如我们所见，这两个迭代极限（iterated limit）并不相等。

<span style="color:#2471a3;">**[note]**</span> 注解（Note）。你也许记得我们以前见过这一现象：以不同顺序求两个极限时，它们可能不同。在 Example 9.7 中我们看到，一个二重序列（double sequence）$\{s_{nm}\}$ 的两个迭代极限可能不相等。关于这一现象的讨论，还可参见 Exercise 9.2.8 及其提示。在这里我们再次遇到一个涉及迭代极限的情形。

我们现在可以解释我们的例子中究竟出了什么错：两个混合偏导 $f_{12}$ 与 $f_{21}$ 不相等，其原因可以追溯到当 $(h,k)\to0$ 时（即取双重极限（double limit）时）这些表达式 (6) 或 (7) 的极限不存在。

这个双重极限存在的一个简单充分条件出现在下面的定理中。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**定理 12.5（Theorem 12.5）**</span>：设 $f$ 定义在 $(x_0,y_0)\in\mathbb{R}^2$ 的一个邻域（neighborhood）中。假定 $f$ 在该邻域中具有偏导数 $f_1$、$f_2$、$f_{12}$ 与 $f_{21}$，并且混合偏导 $f_{12}$ 与 $f_{21}$ 在 $(x_0,y_0)$ 处连续。则 $f_{12}(x_0,y_0)=f_{21}(x_0,y_0)$。

> <span style="color:#1e8449;">**[note]**</span> **注 28** Theorem 12.5 的证明值得存为模板「同一个双重差分、两条中值定理路径」。考察矩形四角差分 $D_{hk}=f(x_0+h,y_0+k)-f(x_0+h,y_0)-f(x_0,y_0+k)+f(x_0,y_0)$：(10) 把相邻角沿 $x$ 配对，两次应用 mean value theorem（中值定理，定理 7.20）得 $D_{hk}=f_{12}(\xi,\zeta)hk$；重排四角沿 $y$ 配对则得 $D_{hk}=f_{21}(\sigma,\tau)hk$。两个式子的左边是同一个数，所以 $f_{12}(\xi,\zeta)=f_{21}(\sigma,\tau)$ 对每个 $(h,k)$ 成立——代数免费给出「两族逼近值相等」。连续性假设此刻只干一件事：$(h,k)\to(0,0)$ 时中间点 $(\xi,\zeta)$、$(\sigma,\tau)$ 都趋于 $(x_0,y_0)$，连续性把 $f_{12}(\xi,\zeta)$ 压向 $f_{12}(x_0,y_0)$、把 $f_{21}(\sigma,\tau)$ 压向 $f_{21}(x_0,y_0)$，两个共同极限必相等；Example 12.4 恰好死在 $f_{12}$ 于原点不连续。书页 475 的 Note 强调证明其实建立了更强的结论：双重极限 $\lim_{(h,k)\to(0,0)}D_{hk}/(hk)$ 存在。条件是充分的而非必要的：Example 12.6 的 $f(x,y)=yx^2\sin(1/x)$ 两个混合偏导在原点都不连续、定理不适用，却仍有 $f_{12}(0,0)=f_{21}(0,0)=0$；若三阶以内偏导全部连续，还有 $f_{221}=f_{212}=f_{122}$。历史上 Euler（欧拉，1707–1783，MacTutor 生平词条）最先证明混合偏导相等（Higgins《A note on the history of mixed partial derivatives》，《Scripta Mathematica》7 (1940) 59–62），法国教材按 Clairaut（克莱罗，1713–1765，MacTutor）称之为克莱罗定理，Schwarz（施瓦茨，1843–1921，MacTutor/DSB）在混合偏导连续的假设下给出严格证明，故亦称 Schwarz 定理。

<span style="color:#2471a3;">**[proof]**</span> 证明（Proof）。考虑两个相等的表达式

```math
\frac{1}{k}\left[\frac{f(x_0+h,y_0+k)-f(x_0,y_0+k)}{h}-\frac{f(x_0+h,y_0)-f(x_0,y_0)}{h}\right], \tag{8}
```

```math
\frac{1}{h}\left[\frac{f(x_0+h,y_0+k)-f(x_0+h,y_0)}{k}-\frac{f(x_0,y_0+k)-f(x_0,y_0)}{k}\right]. \tag{9}
```

如果在 (8) 中先令 $h\to0$ 再令 $k\to0$，我们就得到 $f_{12}(x_0,y_0)$。另一方面，在 (9) 中先令 $k\to0$ 再令 $h\to0$，我们得到 $f_{21}(x_0,y_0)$。我们将证明这两个迭代极限相等。

首先注意到，表达式 (8) 中方括号内的分子 $D_{hk}$ 可以写成如下形式

```math
\bigl(f(x_0+h,y_0+k)-f(x_0+h,y_0)\bigr)-\bigl(f(x_0,y_0+k)-f(x_0,y_0)\bigr). \tag{10}
```

对 (10) 应用中值定理（mean value theorem，定理 7.20），我们得到

```math
D_{hk}=\bigl(f_1(\xi,y_0+k)-f_1(\xi,y_0)\bigr)h, \tag{11}
```

其中 $\xi$ 位于 $x_0$ 与 $x_0+h$ 之间。再次应用中值定理，我们得到

```math
D_{hk}=f_{12}(\xi,\zeta)hk,
```

其中 $\zeta$ 位于 $y_0$ 与 $y_0+k$ 之间。

> <span style="color:#7f8c8d">*（本页译文至此为止；定理 12.5 的证明将在下页继续，完整证明最终以 $\square$ 收束。）*</span>

---

## 书页 475

<span style="color:#2471a3;">**[proof]**</span> 证明（续）。我们可以把 (10) 改写成如下形式：
```math
(f(x_0+h,y_0+k)-f(x_0,y_0+k))-(f(x_0+h,y_0)-f(x_0,y_0)).
```
应用与之前相同的论证，我们得到
```math
D_{hk}=f_{21}(\sigma,\tau)kh,
```
其中 σ 介于 $x0$ 与 $x0$+h 之间，τ 介于 $y0$ 与 $y0$+k 之间。

现在令 (h,k)→(0,0)，于是 (ξ,ζ)→($x0$,$y0$)，且 (σ,τ)→($x0$,$y0$)。由于（依假设）函数 f12 与 f21 在 ($x0$,$y0$) 处连续，我们得到
```math
\lim_{(h,k)\to(0,0)}\frac{D_{hk}}{hk}=f_{21}(x_0,y_0)=f_{12}(x_0,y_0)
```
正如所要求的那样。$\square$

<span style="color:#2471a3;">**[note]**</span> <span style="color:#1e8449;">**Note（注解）**</span>。注意，我们的证明实际上表明，二重极限（double limit）
```math
\lim_{(h,k)\to(0,0)}\frac{D_{hk}}{hk}=f_{21}(x_0,y_0)=f_{12}(x_0,y_0)
```
成立。这是比定理结论更强的陈述。我们将在后面讨论可微性（differentiability）时再回到这一思想。

定理 12.5 表明，偏导数的连续性是 f12 等于 f21 的充分条件（sufficient condition）。这一条件常常得到满足，但它并不是必要条件（necessary condition）。

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b;">**例 12.6（Example 12.6）（Example 12.6）**</span>。我们可以利用函数
```math
g(x)=x^2\sin\frac{1}{x},\qquad g(0)=0
```
来构造一个例子，它在 $\mathbb{R}$ 上可微（differentiable），但其导数 $g'$ 在 $x=0$ 处不连续。由此可知，函数
```math
f(x,y)=yx^2\sin\frac{1}{x},\qquad f(0,y)=0
```
的两个混合偏导 f12 与 f21 都在 (0,0) 处不连续。因此 定理 12.5 在此并不适用，然而偏导
```math
f_{21}(0,0)=f_{12}(0,0)=0
```
却是相等的。

关于混合偏导相等还有其他已知的充分条件。例如，只需假设两个混合偏导都存在、且其中仅一个在 ($x0$,$y0$) 处连续，或者假设 f1 与 f2 在 ($x0$,$y0$) 处可微即可。我们略去这些证明。

定理 12.5 可以容易地推广到高阶导数（higher-order derivatives）。例如，若 f 具有一阶、二阶与三阶偏导数，且所有这些偏导数都在 ($x0$,$y0$) 处连续，则
```math
f_{221}=(f_2)_{21}=(f_2)_{12}=f_{212}=(f_{21})_2=(f_{12})_2=f_{122}.
```

<span style="color:#7f8c8d">*1 此处的"可微"按第 12.4 节稍后给出的意义理解。*</span>

## 书页 476

<span style="color:#2471a3;">**[section]**</span> **$f:\mathbb{R}^n\to\mathbb{R}$ 的偏导数（Partial Derivatives of $f:\mathbb{R}^n\to\mathbb{R}$）**

定理 12.5 也推广到多于两个变量的函数。下述定理通过在证明中固定除第 i 个与第 j 个之外的全部变量，归结为 定理 12.5；只是记号（notation）变得更加复杂。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**定理 12.7（Theorem 12.7）**</span>：设 f 定义在 $\mathbb{R}^n$ 中点 $x_0$ 的某个邻域（neighborhood）内。假设 f 在该邻域内具有偏导数 $f_i$、$f_j$、$f_{ij}$ 与 $f_{ji}$，且混合偏导 $f_{ij}$ 与 $f_{ji}$ 在 $x_0$ 处连续；则 $f_{ij}(x_0)=f_{ji}(x_0)$。

> <span style="color:#1e8449;">**[note]**</span> **注 29** Theorem 12.7 的证明模板是「冻结坐标归约」：要证 $f_{ij}(x_0)=f_{ji}(x_0)$，把除 $i,j$ 以外的全部坐标冻结在 $x_0$，构造二元切片 $g(s,t)=f(x_0+s e_i+t e_j)$（$e_i,e_j$ 是标准基向量）；偏导数是沿坐标轴的一元导数，所以 $g_{12}(0,0)=f_{ij}(x_0)$、$g_{21}(0,0)=f_{ji}(x_0)$，对 $g$ 调用定理 12.5 即得。模板的威力在于把高维断言无损降成二维断言：凡只涉及有限个坐标的命题都可照此办理。归约的代价是零，因为偏导数定义本身就是沿坐标轴的一元极限、与其余坐标无关；本书后续链式法则的证明也靠冻结变量。它的直接报酬是二阶导数的对称性：若 $f$ 的全部二阶偏导连续，则 Hessian matrix（海塞矩阵）$H=(f_{ij})$ 是对称矩阵。对称性立刻接通你的线性代数：Strang 第 6 章证明实对称矩阵必有实特征值与正交特征向量，因此二次型 $h^{\top}Hh$ 可以对角化——多元微积分里靠 $H$ 的特征值判别极值、Boyd §9.5 牛顿法解 $H\Delta x=-\nabla f$（对称性保证分解可行）都依赖这一步；6.431（Bertsekas 第 4.2 节）里 covariance matrix（协方差矩阵）$\Sigma=E[(X-\mu)(X-\mu)^{\top}]$ 的对称性正是同一现象的统计版。

<span style="color:#7f8c8d">*（习题 12.2.8–12.2.11 按约定跳过。）*</span>

<span style="color:#2471a3;">**[section]**</span> **12.3 Integrals Depending on a Parameter（含参变量积分）**

设 g 在 [a,b] 上连续，并令
```math
G(y)=\int_a^y g(x)\,dx. \tag{12}
```
由微积分基本定理（fundamental theorem of calculus），我们记得对一切 $y\in[a,b]$ 都有 $G'(y)=g(y)$。这体现了微分与积分互逆性质的一半。

现在让我们把情形稍加复杂化。设 f 在矩形
```math
R=\{(x,y)\in\mathbb{R}^2: a\le x\le b,\ c\le y\le d\}
```
上连续。定义函数 $F:[c,d]\to\mathbb{R}$ 为
```math
F(y)=\int_a^b f(x,y)\,dx. \tag{13}
```

---

<span style="color:#2471a3;">**[section]**</span> **12.3 含参变量积分（Integrals Depending on a Parameter）**

<span style="color:#7f8c8d;">*（书页 477）*</span>

为了看出 $F$ 是良定义的（well defined），我们只需注意到：对每个固定的 $y\in[c,d]$，$f(\cdot,y)$ 无非是 $[a,b]$ 上的一个连续函数（continuous function），因此该积分确实存在。

我们可以把 (13) 视作一种"偏积分"（partial integral），正如我们把导数视作偏导数（partial derivative）那样：在两种情形下，运算都只作用于一个变量，而另一个变量保持固定（held fixed）。

关于函数 $F$ 我们能说些什么呢？
$F$ 在 $[c,d]$ 上连续吗？
$F$ 可微（differentiable）吗？若可微，我们又该如何计算 $F'$？
本节就来处理这类问题。

请注意 (12) 与 (13) 之间的两处差异。
在 (12) 中我们处理的是单变量函数 $g$；而在 (13) 中，$f$ 是双变量函数。
此外，在 (12) 中积分上限是变量 $y$，而在 (13) 中积分上限是常数 $b$。

形如 $\int_a^b f(x,y)\,dx$ 的积分在实践中频繁出现。
我们把 $y$ 看作一个参数（parameter），并常常关心这样的问题："参数的小小改变会如何影响所得积分？"
我们先就 $F$ 的连续性来讨论这个问题，然后再讨论它的可微性。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**定理 12.8（Theorem 12.8）**</span>

若 $f$ 在 $R=[a,b]\times[c,d]$ 上连续，且 $F(y)=\int_a^b f(x,y)\,dx$，则 $F$ 在 $[c,d]$ 上连续。

<span style="color:#2471a3;">**[proof]**</span>

设 $y_0\in[c,d]$。
我们来证明 $F$ 在 $y_0$ 处连续。
由于 $R$ 是闭且有界的（closed and bounded），因而紧致（compact），由 定理 11.49 知 $f$ 在 $R$ 上一致连续（uniformly continuous）。
因此，对 $\varepsilon>0$ 存在 $\delta>0$，使得每当 $|y-y_0|<\delta$ 时，对每个 $x\in[a,b]$ 都有
```math
|f(x,y)-f(x,y_0)|<\frac{\varepsilon}{b-a}.
```
对 $|y-y_0|<\delta$，我们计算
```math
|F(y)-F(y_0)|=\left|\int_a^b\bigl(f(x,y)-f(x,y_0)\bigr)\,dx\right|\le\int_a^b|f(x,y)-f(x,y_0)|\,dx\le\int_a^b\frac{\varepsilon}{b-a}\,dx=\varepsilon.
```
因此 $\lim_{y\to y_0}\bigl(F(y)-F(y_0)\bigr)=0$，于是 $F$ 在 $y_0$ 处连续。$\square$

现在我们转向 $F$ 的可微性问题。
我们希望找到一条公式，通过"积分号下求导"（differentiation under the integral sign）来得到 $F'$。
但这里的 $f$ 是双变量函数，因此需要动用偏导数。
定理 12.9 常被称为莱布尼茨法则（Leibniz's rule）。

<span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">**定理 12.9（莱布尼茨法则，Leibniz's Rule）**</span>

> <span style="color:#1e8449;">**[note]**</span> **注 30** §12.3 的两条定理共用一套模板「中值定理搬运＋一致连续压平」。以定理 12.9 为例：把差商写进积分，对每个固定 $x$ 用中值定理（定理 7.20）得 $f(x,y+h)-f(x,y)=h\,\partial f/\partial y(x,y+\xi h)$，误差化为 $\int[\partial f/\partial y(x,y+\xi h)-\partial f/\partial y(x,y)]\,dx$。假设「$\partial f/\partial y$ 在闭矩形 $R$ 上连续」此时只干一件事：$R$ 闭且有界故 compact（紧致，定理 11.44），紧致集上的连续函数一致连续（定理 11.49），于是同一个 $\delta$ 对一切 $x$ 同时压住被积差，误差 $\le\int\varepsilon/(b-a)\,dx=\varepsilon$。为什么必须是一致连续而非点连续？点连续给出的 $\delta$ 依赖 $x$，可能沿 $x$ 无限缩小，就穿不过积分号——「对 $x$ 均匀」正是 differentiation under the integral sign（积分号下求导）的命门。定理 12.8 是同一模板的降级版：只需 $f$ 本身连续，一致连续性直接压住 $|f(x,y)-f(x,y_0)|$。历史上这条规则出现在 Leibniz（莱布尼茨，1646–1716，MacTutor）1697 年致 Johann Bernoulli 的信中，是其正交轨线问题（1694 年提出）通信的副产品，Bernoulli 当年 8 月随即用它攻克超越曲线族（Engelsman《Families of Curves and the Origins of Partial Differentiation》1984 第 3 章）；Euler 在《De Infinitis Curvis Eiusdem Generis》（约 1734 年写就、1740 年刊行）中借混合偏导相等给出另一证明。Feynman（费曼，1918–1988）从 Woods 1934 年教材《Advanced Calculus》学得此法并终生爱用（自传《Surely You're Joking, Mr. Feynman!》1985「A Different Box of Tools」）：引入参数、积分号下求导、再积分回去——例如 $G(t)=\int_0^1(x^t-1)/\ln x\,dx$ 求导得 $G'(t)=\int_0^1 x^t dx=1/(t+1)$，故 $G(t)=\ln(t+1)$。

设 $f$ 在矩形 $R=[a,b]\times[c,d]$ 上连续，并令 $F(y)=\int_a^b f(x,y)\,dx$。

<span style="color:#7f8c8d;">*（书页 478）*</span>

对每个 $y\in[c,d]$，若偏导数 $\frac{\partial f}{\partial y}$ 存在且在 $R$ 上连续，则 $F$ 在 $[c,d]$ 上可微，且
```math
F'(y)=\int_a^b\frac{\partial}{\partial y}f(x,y)\,dx.
```

<span style="color:#2471a3;">**[proof]**</span>

只需证明对每个 $y\in[c,d]$ 都有
```math
\lim_{h\to 0}\left(\frac{F(y+h)-F(y)}{h}-\int_a^b\frac{\partial}{\partial y}f(x,y)\,dx\right)=0.\tag{14}
```
现在对 $y+h\in[c,d]$ 有
```math
F(y+h)-F(y)=\int_a^b\bigl[f(x,y+h)-f(x,y)\bigr]\,dx.\tag{15}
```
由中值定理（mean value theorem，定理 7.20）可知：对固定的 $x$、$y$ 和 $h$，存在数 $\xi\in(0,1)$ 使得
```math
f(x,y+h)-f(x,y)=h\,\frac{\partial}{\partial y}f(x,y+\xi h).\tag{16}
```
把 (16) 代入 (15)，我们得到
```math
\frac{F(y+h)-F(y)}{h}-\int_a^b\frac{\partial}{\partial y}f(x,y)\,dx=\int_a^b\left(\frac{\partial}{\partial y}f(x,y+\xi h)-\frac{\partial}{\partial y}f(x,y)\right)dx.\tag{17}
```
由于 $\frac{\partial f}{\partial y}$ 连续（按假设），它在紧致集 $R$ 上一致连续。
因此，对 $\varepsilon>0$ 存在 $\delta>0$，使得若 $(x,y)\in R$、$(x_0,y_0)\in R$ 且 $|x-x_0|<\delta$、$|y-y_0|<\delta$，则
```math
\left|\frac{\partial}{\partial y}f(x,y)-\frac{\partial}{\partial y}f(x_0,y_0)\right|<\frac{\varepsilon}{b-a}.
```
特别地，若 $|h|<\delta$，则
```math
\left|\frac{\partial}{\partial y}f(x,y+\xi h)-\frac{\partial}{\partial y}f(x,y)\right|<\frac{\varepsilon}{b-a}.\tag{18}
```
由 (17) 与 (18) 可推出：对 $|h|<\delta$ 有
```math
\left|\frac{F(y+h)-F(y)}{h}-\int_a^b\frac{\partial}{\partial y}f(x,y)\,dx\right|\le\int_a^b\frac{\varepsilon}{b-a}\,dx=\varepsilon,
```
于是 (14) 成立。$\square$

<span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b;">**例 12.10（Example 12.10）**</span>

若 $F(y)=\int_a^b\sin(xy)\,dx$，则由 定理 12.9 可以得出结论 $F'(y)=\int_a^b x\cos(xy)\,dx$。
我们只需"穿过"积分号进行微分即可。

---

# 书页 479（§12.3 正文续）

<span style="color:#2471a3;">**[section]**</span>
## Section 12.3. 含参变量积分（Integrals Depending on a Parameter）

在此情形下，式中出现的两个积分（integral）都可以用初等方法轻松求积，莱布尼茨法则（Leibniz's rule）也因此得以直接验证，但这一点在一般情况下并不成立。通常我们无法用初等函数（elementary function）求出下面两个积分中的一个或同时两个：

```math
\int_a^b \frac{\partial f}{\partial y}(x,y)\,dx \qquad \text{或} \qquad \int_a^b f(x,y)\,dx .
```

我们继续看一些将莱布尼茨法则与其他技巧结合使用的例子。

<span style="color:#2471a3;">**[example]**</span>
**例 12.11（Example 12.11）.** 为了计算函数

```math
F(y) = \int_0^{\pi/2} \frac{dx}{\sqrt{1-y^2\sin^2 x}} \qquad (0<y<1)
```

的导数，我们只需直接应用莱布尼茨法则，即可得到

```math
F'(y) = \int_0^{\pi/2} \frac{y\sin^2 x}{(1-y^2\sin^2 x)^{3/2}}\,dx .
```

这是以 $y$ 为参数的一个椭圆积分（elliptic integral）的例子【译者注：原文分母印作 $\sqrt{1-y^2\sin^2 x}$，按 $\frac{d}{dy}(1-y^2\sin^2 x)^{-1/2}=y\sin^2 x\,(1-y^2\sin^2 x)^{-3/2}$ 应为 $(1-y^2\sin^2 x)^{3/2}$】。$\square$

<span style="color:#2471a3;">**[example]**</span>
**例 12.12（Example 12.12）.** 积分

> <span style="color:#1e8449;">**[note]**</span> **注 31** Example 12.11 的 $F(y)=\int_0^{\pi/2}dx/\sqrt{1-y^2\sin^2 x}$ 就是第一类完全椭圆积分 $K(y)$：计算椭圆 $x^2/a^2+y^2/b^2=1$ 的弧长时，弧长元 $\sqrt{a^2\sin^2\theta+b^2\cos^2\theta}\,d\theta$ 代换后正是 $\sqrt{1-k^2\sin^2\theta}\,d\theta$ 的形状，这类从椭圆弧长冒出来的积分因此得名 elliptic integral（椭圆积分）。定理 12.9 给出的 $F'$ 仍是一个椭圆积分——求导出不了这个家族。这正是选例的深意：$F$ 不是 elementary function（初等函数），Legendre（勒让德，1752–1833，MacTutor）耗费四十年在《Exercices du Calcul Intégral》（1811/1817/1819）与《Traité des Fonctions Elliptiques》（1825/1826/1830）中分类它们，Liouville（刘维尔，1809–1882，MacTutor）于 1833–1835 年证明椭圆积分不能用初等函数表出（Lützen 传记与 Siu 1996 综述）——「先积出来再求导」这条路不存在，积分号下求导是唯一通道。Example 12.12 演示参数同时出现在积分限与被积函数的情形：把 $F(y)=\int_0^{y^2}yx^3\,dx$ 看成复合 $F(y)=G(y^2,y)$，其中 $G(u,v)=\int_0^u vx^3\,dx$；微积分基本定理给 $\partial G/\partial u=vu^3$，定理 12.9 给 $\partial G/\partial v=\int_0^u x^3 dx=u^4/4$，再用链式法则（§12.5.4 定理 12.34 将证明）得 $F'=\partial G/\partial u\cdot 2y+\partial G/\partial v\cdot 1=2y^8+y^8/4=9y^8/4$。这正是高数里变限积分莱布尼茨公式 $\frac{d}{dy}\int_{a(y)}^{b(y)}f(x,y)dx=f(b(y),y)b'(y)-f(a(y),y)a'(y)+\int_{a(y)}^{b(y)}\partial f/\partial y\,dx$ 的第一性原理拆解：上限项来自基本定理、被积项来自莱布尼茨法则、两项相加来自链式法则。

```math
F(y) = \int_0^{y^2} yx^3\,dx  \tag{19}
```

及其导数可以用初等方法轻易算出。作为练习，我们运用莱布尼茨法则来计算 $F'$。我们首先注意到，这里的积分上限（upper limit of integration）是一个变量，因此所需的不只是对莱布尼茨法则的直接应用。

在这种情况下，参数既出现在积分限（limit of integration）之中，也出现在被积函数（integrand）之中，所以除了莱布尼茨法则之外，我们还需要使用微积分基本定理（fundamental theorem of calculus）与链式法则（chain rule）。（链式法则将在第 12.5.4 节的 定理 12.34 中给出证明。）

设

```math
u = y^2,\quad v = y, \quad\text{并令}\quad G(u,v) = \int_0^u vx^3\,dx .
```

于是微积分基本定理给出

```math
\frac{\partial G}{\partial u} = vu^3 ,
```

莱布尼茨法则给出

```math
\frac{\partial G}{\partial v} = \int_0^u x^3\,dx = \frac{u^4}{4} ,
```

而我们由二元函数微积分（calculus of functions of two variables）所记住的链式法则给出

```math
\frac{d}{dy}F(y) = \frac{\partial G}{\partial u}\frac{du}{dy} + \frac{\partial G}{\partial v}\frac{dv}{dy}
= vu^3\cdot 2y + \frac{u^4}{4}\cdot 1
= 2y^8 + \frac{y^8}{4} = \frac{9}{4}\,y^8 ,
```

这与我们直接求积分 (19) 再求导所得的结果完全相同。$\square$

# 书页 480（§12.3 末尾 + §12.4 开头）

某些习题会用到微积分中的链式法则（chain rule）。这些链式法则以及其他链式法则将在第 12.5、12.5.4、12.5.6 与 12.8 节中作更详细的讨论，并给出证明。

<span style="color:#7f8c8d">*（本页第 8 行起为 §12.3 习题区（Exercises 12.3.1–12.3.5），按约定跳过。）*</span>

<span style="color:#2471a3;">**[section]**</span>
## Section 12.4. 可微函数（Differentiable Functions）

当一个单实变量函数 $f$ 在点 $x_0$ 处具有有限导数时，我们就说 $f$ 在 $x_0$ 处可微（differentiable）。这其实就是可微性（differentiability）的定义本身。单变量可微函数具有许多有用的性质，其中最根本的一条是：$x_0$ 处的切线（tangent line）是函数在 $x_0$ 附近的一个良好近似（close approximation）。

我们也许想把这种说法直接搬到更高维的情形，称一个对每个变量都具有有限偏导数（partial derivative）的多变量函数为"可微的"。但这样的定义并不实用。况且，它也无法推广"切线是可微函数的一个良好近似"这一思想。

---

# 书页 481（§12.4.1 线性函数逼近 + §12.4.2 可微性的定义）

<span style="color:#2471a3;">**[section]**</span>
### 12.4.1 线性函数逼近（Approximation by Linear Functions）

> <span style="color:#1e8449;">**[note]**</span> **注 32** §12.4.1 用「除什么」的对比讲清可微性的本质。连续性只保证 (20)：误差 $|f(x)-L(x)|$ 除以常数 $1$ 趋于 $0$——误差消失，但消失速度未知；可微性要求 (22)：误差除以 $|x-x_0|$（一个自身趋于 $0$ 的量）仍趋于 $0$——误差必须比位移消失得更快。把 $h=x-x_0$ 代入整理成 (23)：$f(x_0+h)-f(x_0)=f'(x_0)h+\varepsilon h$ 且 $\varepsilon\to0$；线性部分 $f'(x_0)h$ 是 $h$ 的真 linear transformation（线性映射），满足 $L(h_1+h_2)=L(h_1)+L(h_2)$ 与 $L(ch)=cL(h)$，余项 $\varepsilon h$ 吸收一切非线性残留。脚注 2 的 affine function（仿射函数）之辨不是咬文嚼字：$L(x)=a_0x+a_1$ 不满足 $L(0)=0$，按 Strang 第 1 章线性映射的定义它并非线性；只有把坐标中心平移到 $x_0$、研究增量 $f(x_0+h)-f(x_0)$，仿射切线才退化为线性映射——因为第 12 章的终点正是「导数即线性映射」。(23) 就是 6.006/CLRS 第 3 章渐近记号里的 little-o（小 $o$）：$f(x_0+h)=f(x_0)+f'(x_0)h+o(h)$，$o(h)$ 意为「被 $h$ 打败」，你熟悉的算法复杂度记号在这里变成误差大小的记号。Boyd §9.3 梯度法每步极小化的模型 $f(x_0+t\Delta x)\approx f(x_0)+t\nabla f(x_0)^{\top}\Delta x$ 正是这条一阶近似的多元版预告。

让我们通过更仔细地考察一元的情形，来看看这里究竟涉及什么。

假设 $f: \mathbb{R} \to \mathbb{R}$，$x_0 \in \mathbb{R}$，且 $L(x) = a_0 x + a_1$ 是任意一个满足 $L(x_0) = f(x_0)$ 的仿射函数（affine function）。

若 $f$ 在 $x_0$ 处连续，则当 $x$ 靠近 $x_0$ 时，$f(x)$ 将靠近 $L(x)$。

更精确地说，

```math
\lim_{x \to x_0} | f(x) - L(x)| = 0. \tag{20}
```

我们可以说，$L$ 在 (20) 的意义下于 $x_0$ 附近逼近 $f$。

因此，若 $f$ 在 $x_0$ 处连续，则任何通过点 $(x_0, f(x_0))$ 的仿射函数都在 $x_0$ 附近逼近 $f$。

若 $f$ 在 $x_0$ 处可微，我们就能借助切线（tangent line）$T$ 得到更好的逼近。

该直线的方程为 $T(x) = f(x_0) + f'(x_0)(x - x_0)$。

现在，$f$ 在 $x_0$ 处的可微性（differentiability）意味着

```math
\left| \frac{f(x) - f(x_0)}{x - x_0} - f'(x_0) \right| \to 0 \quad \text{当 } x \to x_0. \tag{21}
```

我们可以把 (21) 写成如下形式

```math
\left| \frac{f(x) - T(x)}{x - x_0} \right| \to 0 \quad \text{当 } x \to x_0. \tag{22}
```

将 (22) 与 (20) 作比较，我们就能看到在使用切线（当它存在时）后逼近所获得的改进。

在 (20) 中，我们用常数 $1$ 去除 $| f(x) - L(x) |$ 并得到极限 $0$。

在 (22) 中，我们用 $|x - x_0|$ 去除 $| f(x) - T(x) |$，而 $|x - x_0|$ 在 $x \to x_0$ 时趋于 $0$，却仍然得到极限 $0$。

因此，当 $x$ 靠近 $x_0$ 时，不仅 $T(x)$ 靠近 $f(x)$，而且 $T(x)$ 与 $f(x)$ 之间的距离与 $x$ 和 $x_0$ 之间的距离相比也是小的。

最后，我们把 (22) 改写成一种便于推广到多元函数（functions of several variables）的形式。

若令 $h = x - x_0$ 并对 (22) 稍作整理，我们就得到等价的表述

```math
f(x_0 + h) - f(x_0) = f'(x_0)h + \varepsilon h, \tag{23}
```

其中当 $h \to 0$ 时 $\varepsilon \to 0$。

这里的 $\varepsilon$ 依赖于 $h$（以满足 (23) 中的等式），而可微性条件 (21) 的要求正是：当 $h \to 0$ 时 $\varepsilon \to 0$。

<span style="color:#2471a3;">**[section]**</span>
### 12.4.2 可微性的定义（Definition of Differentiability）

我们将对多元函数模仿上述做法。

为了暂时保持记号简单，我们先从定义于某点 $(x_0, y_0) \in \mathbb{R}^2$ 的一个邻域（neighborhood）上的二元函数开始讨论。

> <span style="color:#7f8c8d">**脚注 2**：一个实变量的实值函数 $L$ 若其图像（graph）是一条直线，则称它是仿射的。于是 $L(x) = a_0 x + a_1$。在微积分课程中，这样的函数通常被称为"线性"的，但我们的用语必须相当精确，因为在本节的叙述中要用到一些线性代数。请注意，能够被线性函数 $a_0 x$ 逼近的，正是函数 $f(x) - f(x_0)$。</span>

# 书页 482（§12.4.2 可微性的定义 续）

我们希望表述这样的条件：由方程 $z = f(x, y)$ 所对应的曲面（surface）在 $(x_0, y_0)$ 处具有切平面（tangent plane）。

于是，切平面 $T$ 取代了一元函数情形中的切线。

回顾初等微积分可知，切平面若存在，可由线性方程 $T(x, y) = f(x_0, y_0) + f_1(x_0, y_0)(x - x_0) + f_2(x_0, y_0)(y - y_0)$ 表示。

为了使这个平面成为切平面，我们要求 (22) 的类比形式成立，即

```math
\frac{| f(x, y) - T(x, y) |}{\sqrt{(x - x_0)^2 + (y - y_0)^2}} \to 0 \quad \text{当 } (x, y) \to (x_0, y_0). \tag{24}
```

如同我们对 (22) 所做的那样处理 (24)，并令 $h = x - x_0$、$k = y - y_0$，我们就得到二元情形的正确表述。

<span style="color:#2471a3;">**[definition]**</span> **<span style="color:#c0392b">定义 12.13</span>**

> <span style="color:#1e8449;">**[note]**</span> **注 33** Definition 12.13 两条合起来才叫可微：条件 1 偏导存在只提供线性映射的候选系数；条件 2 要求 $f(x_0+h,y_0+k)-f(x_0,y_0)=f_1h+f_2k+\varepsilon(h,k)\sqrt{h^2+k^2}$ 且 $\varepsilon\to0$——误差比距离 $\sqrt{h^2+k^2}$ 消失得更快，这就是 (24) 的改写，即 tangent plane（切平面）在「误差/距离趋于 $0$」意义下逼近曲面。为什么分母用欧几里得距离而不用 $|h|$ 或 $|k|$？逼近质量要对一切逼近路径一视同仁：沿对角线逼近时 $h,k$ 同时变小，只有距离能统一度量所有路径。书中 Note 给出等价写法 (26)：借三明治 $\sqrt{h^2+k^2}\le|h|+|k|\le\sqrt2\sqrt{h^2+k^2}$（part2 注 15 的范数等价），余项换成 $\varepsilon(|h|+|k|)$ 只差一个被 $\varepsilon$ 吸收的有界因子——用哪个范数定义可微性都一样，$\|\cdot\|_1$ 版本日后更省事。线性部分 $L(h,k)=f_1h+f_2k$ 是行向量 $[f_1\ f_2]$ 与列向量 $[h,k]^{\top}$ 的乘积，这个 $1\times2$ 矩阵就是 Jacobian matrix（雅可比矩阵）——以 Jacobi（雅可比，1804–1851，其 1841 年《De determinantibus functionalibus》见 part2 注 24）命名；对 $f:\mathbb{R}^n\to\mathbb{R}^m$（§12.8）它将成长为 $m\times n$ 矩阵，链式法则就是矩阵乘法。Example 12.15 的 $\sqrt{|xy|}$ 演示条件 2 的杀伤力：偏导在原点都为 $0$，但沿 $h=-k$ 有 $\sqrt{|hk|}=|h|$，定义强制 $\varepsilon=1/2$ 不趋于 $0$——「折痕」沿对角线以距离的一阶速度升起，任何一阶平面都追不上它，此时沿 $(-1/\sqrt2,1/\sqrt2)$ 的方向导数甚至不存在。
<span style="color:#00838f">函数 $f: \mathbb{R}^2 \to \mathbb{R}$ 在 $(x_0, y_0)$ 处可微（differentiable），</span>如果

1. 偏导数（partial derivatives）$f_1$ 与 $f_2$ 在 $(x_0, y_0)$ 处存在。
2. 能够写成

```math
f(x_0 + h, y_0 + k) - f(x_0, y_0) = f_1(x_0, y_0)h + f_2(x_0, y_0)k + \varepsilon(h, k)\sqrt{h^2 + k^2}, \tag{25}
```

其中当 $\sqrt{h^2 + k^2} \to 0$ 时 $\varepsilon(h, k) \to 0$（并规定 $\varepsilon(0, 0) = 0$）。

<span style="color:#2471a3;">**[note]**</span> **<span style="color:#1e8449">Note（注）</span>**

通过观察对 $(h, k) \in \mathbb{R}^2$ 成立的不等式

```math
\sqrt{h^2 + k^2} \le |h| + |k| \le \sqrt{2}\,\sqrt{h^2 + k^2},
```

我们就可以把定义中的陈述 (2) 改写为更简单的形式。

于是新陈述 $2'$ 为：能够写成

```math
f(x_0 + h, y_0 + k) - f(x_0, y_0) = f_1(x_0, y_0)h + f_2(x_0, y_0)k + \varepsilon(h, k)(|h| + |k|), \tag{26}
```

其中当 $|h| + |k| \to 0$ 时 $\varepsilon(h, k) \to 0$。

条件 $|h| + |k| \to 0$ 等价于 $h \to 0$ 且 $k \to 0$，而这又等价于 $\sqrt{h^2 + k^2} \to 0$。

让我们暂时回到切平面作用背后的初等几何。

该平面应在 (24) 的意义下逼近 $(x_0, y_0)$ 附近的 $f$。

粗略地说，这要求当 $(x, y)$ 靠近 $(x_0, y_0)$ 时，$| f(x, y) - T(x, y) |$ 与 $(x, y)$ 和 $(x_0, y_0)$ 之间的距离相比是小的。

仅仅偏导数在 $(x_0, y_0)$ 处存在并不能保证这一点。

那只能保证当 $(x, y)$ 靠近 $(x_0, y_0)$ 且 $x = x_0$（或 $y = y_0$）时，所期望的比较量是小的。

适当的切线存在于曲面 $z = f(x, y)$ 与平面 $x = x_0$（或 $y = y_0$）的交线中，但当 $(x, y)$ 以其他方式趋于 $(x_0, y_0)$ 时，(24) 未必成立。

---

<span style="color:#2471a3;">**[section]**</span> §12.4 可微函数（Differentiable Functions）

<span style="color:#2471a3;">**[figure]**</span> **Figure 12.3.** 函数 $f(x,y)=\frac{1}{3}\sqrt{36-4x^2-y^2}$ 在点 $(1,3,\sqrt{23}/3)$ 处的切平面（tangent plane）。

<span style="color:#2471a3;">**[example]**</span> **例 12.14（Example 12.14）.** 让我们再次考察来自 Example 12.1 的函数
```math
f(x,y)=\frac{\sqrt{36-4x^2-y^2}}{3}.
```
在 Figure 12.1 中，我们演示了点 $(x_0,y_0,z_0)=(1,3,\sqrt{23}/3)$ 处的切线（tangent line）。
再花一些力气，我们现在就能通过完成定义中的计算，证明该函数在该点可微（differentiable），从而说明切平面在正确意义下逼近（approximate）该函数。
图 12.3 展示了这个切平面，并说明这种逼近是合理的（plausible）。
在实践中，我们通常会应用某个定理（例如 定理 12.21），据此直接断定可微性，而无需求助这类计算。$\square$

<span style="color:#2471a3;">**[example]**</span> **例 12.15（Example 12.15）.** 设 $f(x,y)=\sqrt{|xy|}$。
（这个函数使人想起函数 $|x|=\sqrt{x^2}$，后者在 $x=0$ 处连续但不可微（nondifferentiable）。）
显然 $f$ 在 $(0,0)$ 处连续（见 Exercise 12.4.1）。
由于 $f$ 在坐标轴上等于 $0$，因此
```math
f_1(0,0)=f_2(0,0)=0. \tag{27}
```
要使 $f$ 在 $(0,0)$ 处可微，当 $|h|+|k|\to 0$ 时必须有 $\varepsilon(h,k)\to 0$，其中 $\varepsilon(h,k)$ 由下式定义：
```math
\sqrt{|hk|}=f_1(0,0)h+f_2(0,0)k+\varepsilon(h,k)(|h|+|k|).
```
由 (27) 得 $\sqrt{|hk|}=\varepsilon(|h|+|k|)$。
例如令 $h=-k$，可得 $|h|=2\varepsilon|h|$，于是 $\varepsilon(h,-h)=\frac{1}{2}$。
因此，当 $|h|+|k|\to 0$ 时 $\varepsilon(h,k)\to 0$ 并不成立。
（令 $h=-k$ 等价于让 $(x,y)$ 沿直线 $x+y=0$、$z=0$ 逼近 $(x_0,y_0)$。）
图 12.4 展示了函数 $f$ 的图形，其形状显然像一张沿两条坐标轴折叠的餐巾（folded napkin）。
请特别留意，沿「折痕」处的信息 $f_1(0,0)=f_2(0,0)=0$ 并不能帮助计算方向 $(-1/\sqrt{2},1/\sqrt{2})$ 上的方向导数（directional derivative）（图中已示出），而这正对应前面讨论的 $h=-k$ 情形。$\square$

<span style="color:#2471a3;">**[section]**</span> 函数 $f:\mathbb{R}^n\to\mathbb{R}$ 的可微性（Differentiability for $f:\mathbb{R}^n\to\mathbb{R}$）。
有了这些准备，我们现在可以给出函数 $f:\mathbb{R}^n\to\mathbb{R}$ 可微性的正式定义（formal definition）。
这就是我们刚刚针对二元函数可微性给出的 定义 12.13 的明显推广（obvious generalization）。

<span style="color:#2471a3;">**[figure]**</span> **Figure 12.4.** 函数 $f(x,y)=\sqrt{|xy|}$ 的图形，它在 $(0,0)$ 处连续但不可微。

<span style="color:#2471a3;">**[definition]**</span> **定义 12.16.** 设 $f$ 定义在开集（open set）$D\subset\mathbb{R}^n$ 上，并令 $x=(x_1,\ldots,x_n)\in D$。

> <span style="color:#1e8449;">**[note]**</span> **注 34** Definition 12.16 把二元定义逐字抬到 $n$ 元：条件 1 要求 $n$ 个偏导全部存在，条件 2 要求 $f(x+h)-f(x)=\sum_{i=1}^n f_i(x)h_i+\varepsilon\|h\|$ 且 $\|h\|\to0$ 时 $\varepsilon\to0$（规定 $\varepsilon(0)=0$）。线性部分 $\sum_i f_i h_i=\nabla f(x)\cdot h$ 把 $n$ 个偏导打包成向量 $\nabla f=(f_1,\dots,f_n)$，于是可微性写作 $f(x+h)\approx f(x)+\nabla f\cdot h$：$f$ 的增量约等于梯度与位移的点积——这就是行向量乘列向量的形状（Strang 第 1–2 章），也是后半程一切一阶逼近的标准形式。书中 Note 指出欧几里得范数只是约定：借 $n$ 维三明治 $\|h\|\le\|h\|_1\le\sqrt n\,\|h\|$，条件 2 等价于 $2'$ 的 $\varepsilon(|h_1|+\cdots+|h_n|)$ 版本（习题 12.4.2），范数选择只改变 $\varepsilon$ 的有界倍数，$\|\cdot\|_1$ 版本在证明里更省事。为什么定义域要求开集？$h$ 必须能朝每个方向都走一小步，边界点无法接受全方向检验——可微是「点的邻域」级概念，不是「沿曲线」级概念。由定义可直接推出可微蕴含连续：$\|h\|\to0$ 时 (2) 右端逐项趋于 $0$（反向的「连续但不可微」已由 Example 12.15 在书页 482–483 演示）。这条定义是后文的总闸门：链式法则（定理 12.34）与 §12.8 的 $f:\mathbb{R}^n\to\mathbb{R}^m$ 情形都是把同一模板用到向量值函数上，雅可比矩阵的每一行就是一个坐标函数的梯度。
则 <span style="color:#00838f;">$f$ 在 $x$ 处可微（differentiable）</span>如果：

1. 偏导数（partial derivative）$f_1,\ldots,f_n$ 在 $x$ 处全部存在且为有限值，并且

2. 当 $\varepsilon=\varepsilon(h_1,\ldots,h_n)$ 由 $\varepsilon(0,\ldots,0)=0$ 及下式定义时，
```math
f(x_1+h_1,\ldots,x_n+h_n)-f(x_1,\ldots,x_n)=\sum_{i=1}^{n}f_i(x_1,\ldots,x_n)h_i+\varepsilon\sqrt{h_1^2+\cdots+h_n^2},
```
当 $\sqrt{h_1^2+\cdots+h_n^2}\to 0$ 时，我们有 $\varepsilon(h_1,\ldots,h_n)\to 0$。

若 $f$ 在 $D$ 中每一点都可微，则称 $f$ 在 $D$ 上可微（differentiable on $D$）。

<span style="color:#2471a3;">**[note]**</span> <span style="color:#1e8449;">**Note.**</span> 定义中的陈述 (2) 采用的是通常的欧几里得范数（euclidean norm）。
正如我们在 定义 12.13 之后（即 $\mathbb{R}^2$ 情形）的注解中已经看到的，使用 $\|\cdot\|_1$ 范数往往会简化涉及可微性的证明。
由 Exercise 12.4.2 可知这样做是可行的。
采用 $\|\cdot\|_1$ 范数后，陈述 (2) 变为：

$2'$。当 $\varepsilon=\varepsilon(h_1,\ldots,h_n)$ 由下式定义：
```math
f(x_1+h_1,\ldots,x_n+h_n)-f(x_1,\ldots,x_n)=\sum_{i=1}^{n}f_i(x_1,\ldots,x_n)h_i+\varepsilon(|h_1|+\cdots+|h_n|),
```
其中 $\varepsilon(0,\ldots,0)=0$，则当 $|h_1|+\cdots+|h_n|\to 0$ 时 $\varepsilon\to 0$。

另请参见 Exercise 12.4.3。
