# <span style="color:#c0392b;">Elementary Real Analysis（初等实分析）</span>

> <span style="color:#7f8c8d;">行内双语翻译 · Part014（书页 635–638 Notes + 附录 A 全部 + 主题索引 A-20–A-29）</span>
> <span style="color:#7f8c8d;">范围：第 13 章 Notes 习题提示区收尾（提示 351–386）+ 附录 A：Background（背景）A.1–A.9（记号、什么是分析学、证明方法、间接证明、逆否、反例、归纳、量词）+ 附录 Notes（提示 387–393）+ 全书 Subject Index（主题索引，跳过）</span>
> <span style="color:#7f8c8d;">源文件：TBB-AllChapters-Portrait_part014_p651-683.pdf（书页 635–638 = PDF 页 1–4；附录页 A-N = PDF 页 N+4；A-20–A-29 = PDF 页 24–33）</span>
> <span style="color:#7f8c8d;">Second Edition (2008) · Brian S. Thomson, Judith B. Bruckner, Andrew M. Bruckner</span>
> <span style="color:#7f8c8d;">**格式：** 中文主体 + `English term（中文翻译）` 嵌入 · 深红标题 · 蓝色标签 · fenced math block · 无英文原句</span>
> <span style="color:#7f8c8d;">**跳过区**：第 13 章 Notes 提示区（灰摘要）、附录习题 A.2.1–A.2.13 / A.5.1–A.5.2 / A.6.1 / A.7.1–A.7.3 / A.8.1–A.8.9 / A.9.1–A.9.4（灰注）、附录 Notes 提示 387–393（灰摘要）、Subject Index（灰注）</span>

---

<!-- ===== t00 ===== -->

<span style="color:#7f8c8d">书页 635 · NOTES（第 13 章习题提示区，承接上一卷）</span>

<span style="color:#2471a3;">**[section]**</span> **第 13 章 Notes——Exercise Hints（习题提示）·续**

<span style="color:#7f8c8d">本页及后续 3 页（书页 635–638）属于全书 Notes（提示）区，集中给出第 13 章 §13.10–§13.15 各节习题的解答提示，供读者在自行完成习题后对照参考。按约定跳过逐句翻译，以下为各页提示的灰色摘要。</span>

---

<span style="color:#7f8c8d">书页 635 · NOTES（习题提示，续）</span>

<span style="color:#7f8c8d">*（本页为 §13.10–§13.12 Exercises 的 NOTES 提示区，按约定跳过逐句翻译。页面开头先接续上一卷提示 350 的收尾文字：由迭代可得 $|d(a_m, a_n) - d(A(a_m), A(a_n))| \to 0$，利用 $A$ 是压缩映射（contraction）来证明 $\{a_n\}$ 为 Cauchy 序列，再说明该序列的极限就是 $A$ 的不动点（fixed point），并记住 $A$ 只有一个不动点。以下为提示编号 351–362（对应题 13.10.1 至 13.12.33）的逐条概要。）*</span>

<span style="color:#7f8c8d">*提示 351（题 13.10.1）：充要条件是 $|1 - a| < 1$，并建议仿照图 13.5 的方案用图象展示各次迭代。*</span>

<span style="color:#7f8c8d">*提示 352（题 13.10.2）：条件取决于在 $\mathbb{R}^2$ 上所选的度量，本题可使用通常的欧氏度量（euclidean metric）。*</span>

<span style="color:#7f8c8d">*提示 353（题 13.10.3）：只需证明 $F$ 在 $[a, b]$ 上是压缩映射、且 $F$ 的不动点就是 $f$ 的零点；定理 13.75 保证从 $[a, b]$ 任一点出发的迭代序列必收敛到该不动点。*</span>

<span style="color:#7f8c8d">*提示 354（题 13.11.1）：提醒此处使用的是度量 $d$。*</span>

<span style="color:#7f8c8d">*提示 355（题 13.11.3）：设 $(A(g))(x) = g(x) - cF(x, g(x))$，其中 $c \in \mathbb{R}$ 且 $c \neq 0$，注意 $A$ 的不动点就给出问题的解；设法选 $c$ 使 $A$ 成为压缩映射——对 $|(A(g))(x) - (A(f))(x)| = |g(x) - f(x) - c[F(x, g(x)) - F(x, f(x))]|$ 应用中值定理（mean value theorem），并在 $c = 1/\beta$ 时化简所得表达式。*</span>

<span style="color:#7f8c8d">*提示 356（题 13.12.2）：先证若两空间 $(X, d)$ 与 $(Y, e)$ 拓扑等价（topologically equivalent），则 $X$ 紧致当且仅当 $Y$ 紧致。*</span>

<span style="color:#7f8c8d">*提示 357（题 13.12.4）：证明该空间中的集合紧致当且仅当它是有限集。*</span>

<span style="color:#7f8c8d">*提示 358（题 13.12.7）：参见习题 13.4.4。*</span>

<span style="color:#7f8c8d">*提示 359（题 13.12.9）：对 $K$ 闭而非紧的情形，反例可用通常实数度量下的空间 $X = \{-1, 1, 1/2, 1/3, 1/4, \ldots\}$；对 $K$ 完备（complete）而非紧的情形，则试用空间 $\ell_\infty$。*</span>

<span style="color:#7f8c8d">*提示 360（题 13.12.21）：指出弱压缩（weak contraction）这一假设弱于 Banach 不动点定理（Banach fixed point theorem）中对函数的假设，并问还有哪些假设上的差别；对 (c) 考虑实值连续函数 $h(x) = d(x, f(x))$，解释 $h$ 为何在 $X$ 中取得最小值点 $z$、为何 $h(z) = 0$，由此便得到一个不动点。*</span>

<span style="color:#7f8c8d">*提示 361（题 13.12.30）：取在度量空间中稠密（dense）的序列 $x_1, x_2, x_3, \ldots$，证明开球族 $\{B(x_i, 1/n)\}$ 可数，并可排成 $B_1, B_2, B_3, \ldots$；对覆盖该空间的开集族 $\mathcal{G}$，在可能时选取 $G_k \in \mathcal{G}$ 使 $B_k \subset G_k$（无法选取时跳过该 $k$），从而选出可数子覆盖；任取空间中一点 $x$，它属于某个 $G \in \mathcal{G}$，须解释为何存在某个阶段 $k$ 使所选的 $G_k$ 满足 $x \in G_k$。*</span>

<span style="color:#7f8c8d">*提示 362（题 13.12.33）：本条引 Kasahara 在 1956 年证明的结果：度量空间具有这一“Lebesgue 性质”当且仅当它是紧致集与离散集（discrete set）的并。*</span>

---

<span style="color:#7f8c8d">书页 636 · NOTES（习题提示，续）</span>

<span style="color:#7f8c8d">*（本页为 §13.12–§13.13 Exercises 的 NOTES 提示区，按约定跳过逐句翻译。以下为提示编号 363–374（对应题 13.12.34 至 13.13.4）的逐条概要。）*</span>

<span style="color:#7f8c8d">*提示 363（题 13.12.34）：考虑由取补得到的集族 $\mathcal{G} = \{X \setminus F : F \in \mathcal{F}\}$。*</span>

<span style="color:#7f8c8d">*提示 364（题 13.12.35）：须细读题意方能看出所述条件并非就是定义本身——通常说 $S$ 完全有界（totally bounded），是指总能找到含于 $X$ 的 $\varepsilon$-网（$\varepsilon$-net）$\{x_1, x_2, \ldots, x_n\}$，而本题要求 $\varepsilon$-网本身含于 $S$；办法是先在 $X$ 中取一个 $\varepsilon/2$-网，再在 $S$ 中适当选点，构造出含于 $S$ 的 $\varepsilon$-网。*</span>

<span style="color:#7f8c8d">*提示 365（题 13.12.41）：直接从定义证明，不要使用本节的任何定理。*</span>

<span style="color:#7f8c8d">*提示 366（题 13.12.43）：记号尽量从简——每一阶段把第 $n$ 个子序列写作 $\{x_{n_k}\}$，安排它成为 $\{x_{(n-1)k}\}$ 的子序列且落在半径 $1/n$ 的球内；最终的子序列取对角线序列 $\{x_{11}, x_{22}, x_{33}, \ldots\}$，并解释它为何必是 Cauchy 序列。*</span>

<span style="color:#7f8c8d">*提示 367（题 13.12.45）：定理 13.90 的证明中已含所需论证。*</span>

<span style="color:#7f8c8d">*提示 368（题 13.12.46）：证明 (a) 与 (c) 等价、(b) 与 (d) 等价，并想一想还能进一步说出什么。*</span>

<span style="color:#7f8c8d">*提示 369（题 13.12.49）：答案是否定的——原文此处仅一词 “No”。*</span>

<span style="color:#7f8c8d">*提示 370（题 13.12.55）：使用 Arzelà-Ascoli 定理。*</span>

<span style="color:#7f8c8d">*提示 371（题 13.12.56）：先取 $[a, b]$ 中有理数的一个枚举 $\{r_1, r_2, r_3, \ldots\}$；选 $\{f_n\}$ 的子序列 $\{f_{1_k}\}$ 使 $\{f_{1_k}(r_1)\}$ 收敛（为何可能？），再选 $\{f_{1_k}\}$ 的子序列 $\{f_{2_k}\}$ 使 $\{f_{2_k}(r_2)\}$ 收敛，如此继续，最后选对角线序列 $\{f_{11}, f_{22}, f_{33}, \ldots\}$ 并验证它可行；对 (b)，把该子序列记作 $\{g_k\}$，按等度连续（equicontinuity）假设选 $\delta$，再选 $M$ 使 $[a, b]$ 上每点都在 $\{r_1, r_2, r_3, \ldots, r_M\}$ 中某点的 $\delta$ 范围内，选 $N$ 使得当 $i, j \geq N$ 且 $x \in \{r_1, r_2, r_3, \ldots, r_M\}$ 时 $|g_i(x) - g_j(x)| < \varepsilon/3$，进而证明 $\{g_k\}$ 是一致 Cauchy 的。*</span>

<span style="color:#7f8c8d">*提示 372（题 13.12.58）：直接模仿 Arzelà-Ascoli 定理的证明，但小心不要用到 $[a, b]$ 的任何特殊性质，因为这里 $[a, b]$ 已换成紧致度量空间 $X$。*</span>

<span style="color:#7f8c8d">*提示 373（题 13.12.59）：两个解都容易猜出；证明 $f(x, y) = 3y^{2/3}$ 不满足定理 13.86 的假设。*</span>

<span style="color:#7f8c8d">*提示 374（题 13.13.4）：答案为否，请给出反例（counterexample）。*</span>

---

<span style="color:#7f8c8d">书页 637 · NOTES（习题提示，续）</span>

<span style="color:#7f8c8d">*（本页为 §13.13–§13.15 Exercises 的 NOTES 提示区，按约定跳过逐句翻译。以下为提示编号 375–383（对应题 13.13.5 至 13.15.9）的逐条概要；其中提示 383 的文字延续到下一页。）*</span>

<span style="color:#7f8c8d">*提示 375（题 13.13.5）：所需的性质是空间自身稠密（dense in itself），参见习题 13.5.21。*</span>

<span style="color:#7f8c8d">*提示 376（题 13.14.4）：以 $\mathcal{I}$ 记 $[a, b]$ 中端点为有理数的开区间族；对满足 $I \cap J = \emptyset$ 的 $I, J \in \mathcal{I}$，令 $A_{I,J}$ 为由一切满足“$x_1 \in I$、$x_2 \in J$ 且 $f(x_1) = f(x_2)$”的 $f \in X$ 组成的集合，证明 $A_{I,J}$ 无处稠密（nowhere dense）。*</span>

<span style="color:#7f8c8d">*提示 377（题 13.15.1）：若 $E$ 不是 $\mathcal{A}$ 中成员的可数并，则 $E$ 是闭集。*</span>

<span style="color:#7f8c8d">*提示 378（题 13.15.2）：对 (b) 的提示：以适当方式定义 $A : C[a, b] \to C[a, b]$，并取得 $n \in \mathbb{N}$ 与 $M > 0$ 使 $\frac{|\lambda|^n M^n}{(b - a)^n \, n!} < 1$，然后应用 (a)。*</span>

<span style="color:#7f8c8d">*提示 379（题 13.15.3）：若 $[0, 1] = \bigcup_k E_k$ 且各 $E_k$ 闭、两两不相交（pairwise disjoint），则这些集合中必有一个含区间；据此得到一族可数个闭区间，每个含于某个 $E_n$，其并在 $[0, 1]$ 中稠密；去掉这些区间的内部，证明剩下的部分是一个 Cantor 集（Cantor set）$H$；对 $H$ 应用 Baire 纲定理（Baire category theorem）即导出矛盾。*</span>

<span style="color:#7f8c8d">*提示 380（题 13.15.4）：此题即 Kuratowski 十四集问题（Kuratowski fourteen set problem），由 K. Kuratowski（1896–1980）提出并解决，题名本身已暗示正确答案；参见 J. H. Fife 论 Kuratowski 闭包-补集问题的文章（Mathematics Magazine 第 64 卷第 3 期，180–182 页，1991 年），文中给出一个易读的证明，与 Kuratowski 1922 年的原始版本相似但不完全相同。*</span>

<span style="color:#7f8c8d">*提示 381（题 13.15.5）：参见题 13.15.3 的提示。*</span>

<span style="color:#7f8c8d">*提示 382（题 13.15.6）：取离散度量下的 $X = \mathbb{N}$，证明 $f(n) = n + 1$ 是等距映射（isometry）却不是到上的（onto）；若 $X$ 紧致，任取 $x \in X$ 并定义 $x_1 = f(x)$，$x_2 = f(x_1)$，……；由紧致性，存在收敛子序列 $\{x_{n_k}\}$；注意对一切 $n$ 与 $m$ 有 $d(x, x_n) = d(x_m, x_{n+m})$，用它证明 $d(x, f(X)) = 0$，从而推出 $f(X) = X$。*</span>

<span style="color:#7f8c8d">*提示 383（题 13.15.9）：紧致性是拓扑性质，且每个紧致空间都完备，故一个方向是容易的；另一方向，若 $X$ 不紧致，则需在 $X$ 上构造一个等价度量（equivalent metric）$\rho$ 使 $(X, \rho)$ 不完备（可设 $d$ 有界，否则改用有界的等价度量）；利用“若 $X$ 不紧致，必有交为空的闭集递降序列 $C_1 \supset C_2 \supset C_3 \supset \cdots$”这一事实，定义 $\rho_i(x, y) = |d(x, C_i) - d(y, C_i)| + d(x, y)\min\{d(x, C_i), d(y, C_i)\}$，最后令 $\rho(x, y) = \sum_{i=1}^{\infty} 2^{-i}\rho_i(x, y)$；本条提示的其余部分延续到下一页。*</span>

---

<span style="color:#7f8c8d">书页 638 · NOTES（习题提示，续）</span>

<span style="color:#7f8c8d">*（本页为 §13.15 Exercises 的 NOTES 提示区，按约定跳过逐句翻译。页面开头先承接上一页提示 383 的收尾：还需验证三件事——其一，$d$ 与 $\rho$ 等价；其二，$(X, \rho)$ 中的闭集列 $\{C_i\}$ 是直径趋于零的递降闭集列；其三，$\bigcap_{i=1}^{\infty} C_i = \emptyset$ 违反 Cantor 交性质（Cantor intersection property），故该空间不可能完备。以下为提示编号 384–386（对应题 13.15.11、13.15.12、13.15.14）的逐条概要。）*</span>

<span style="color:#7f8c8d">*提示 384（题 13.15.11）：对 $h \in M[a, b]$，令 $H$ 为由一切 $h - g$（其中 $g$ 为一对一函数，one-to-one）组成的 $M[a, b]$ 的子集；证明 $H$ 在 $M[a, b]$ 中是剩余集（residual set），从而含有一个一对一函数 $f$；写出 $h = f + (h - f)$。*</span>

<span style="color:#7f8c8d">*提示 385（题 13.15.12）：对 (f)：证明 $(X, d)$ 中不收敛的 Cauchy 序列在 $(X, e)$ 中不再是 Cauchy 序列。*</span>

<span style="color:#7f8c8d">*提示 386（题 13.15.14）：令 $g(x) = \frac{\operatorname{dist}(x, A)}{\operatorname{dist}(x, A) + \operatorname{dist}(x, B)}$。*</span>

---

<span style="color:#7f8c8d">*（第 13 章 Notes 提示至此结束（提示 386 收尾），本卷自此进入附录 A（Appendix: Background）。）*</span>

<!-- ===== t01 ===== -->

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">附录 A：背景（Appendix: Background）</span>
> <span style="color:#7f8c8d;">TBB App A, p.A-1</span>

<span style="color:#7f8c8d">书页 A-1 · 附录开篇；A.1 要不要读这一章？；A.2 记号开篇与 A.2.1 集合记号前半（空集、自然数）</span>

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">A.1 Should I Read This Chapter?（要不要读这一章？）</span>

> <span style="color:#7f8c8d;">TBB App A.1, p.A-1</span>

这一章背景材料不是为教师写的，而是为学生写的。
它以基本非正式的方式讲述那些你要想在elementary course in analysis（初等分析课程）中顺利过关所必需的思想。
教材正文的各章要更形式化一些，包含的是真正的数学内容。
而本章是围绕数学来谈的，读起来应当更容易。
你可以前后跳读，挑选那些你觉得自己真正需要阅读的主题。
例如，你可以通览讲记号的那一节（A.2 节），以便确认自己熟悉许多数学思想——比如set（集合）与 function（函数）——的常规书写方式。
如果你从未上过任何要求具备书写证明能力的课程，那么讲证明的几节（A.4、A.5、A.6、A.7 与 A.8 节）就应当读一读。
对许多学生而言，这门real analysis（实分析）课程是初次接触这些思想，你也许会发现这几节颇有帮助。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 先回答一个设计问题：正文第 1–13 章的证明已经相当正式，为什么作者还要专门写一章「非正式」的背景？
> 原因在于，正式的证明只回答「论证是否成立」，却不回答「该用什么语言书写、按什么套路构造」。
> 前一件事由 A.2 节负责——统一集合与函数的记号；后一件事则由 A.4 至 A.9 节集中回答——为什么要证明（A.4）、间接证明与逆否命题（A.5、A.6）、反例（A.7）、归纳（A.8）、量词（A.9），这是全书写证明方法论最集中的地方。
> 你在第 1–13 章的习题里其实已经反复使用这些套路，只是从未被系统点名，按本节建议跳读、缺什么补什么即可。
> 你在 6.042J（离散数学课）学过的等价关系、归纳与量词逻辑，会在这里以分析学的面孔重逢；A.4 把证明比作自然科学的实验，也正对应你在 CSAPP（《深入理解计算机系统》）中「代码必须通过测试才算正确」的工程直觉。
> 如果你正在为 100B 的 PS（习题集）写作发愁，A.4–A.9 就是为这个场景准备的，建议从 A.4 与 A.9 读起。

---

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">A.2 Notation（记号）</span>

> <span style="color:#7f8c8d;">TBB App A.2, p.A-1</span>

如果你正准备不再做任何进一步的预备就直接开始阅读正文，那么有一些记号是我们应当先复习的。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">A.2.1 Set Notation（集合记号）</span>

> <span style="color:#7f8c8d;">TBB App A.2.1, p.A-1</span>

set（集合）不过就是一些对象组成的汇集而已。
在开头阶段，我们主要感兴趣的是由实数组成的集合。
如果 set 这个词重复得过于频繁，你会发现书中会改用 collection（汇集）、family（族）或 class（类）这样的词。
于是，一个由集合组成的集合可能就改称为family of sets（集合族）。
（这样的变异在日常语言中也能见到，例如 a flock of sheep（一群羊）、a gaggle of geese（一群鹅）、a pride of lions（一群狮）。）

命题 $x \in A$ 的意思是：$x$ 是属于 $A$ 的那些数中的一个。
命题 $x \notin A$ 的意思是：$x$ 不是属于 $A$ 的那些数中的一个。
（在符号 $\in$ 上加一道斜线这种手法是大家熟悉的，连路标或禁止吸烟标志上都在用它。）

<span style="color:#2471a3;">**[definition]**</span> 下面给出一些常见的集合及其记号。

**The Empty Set（空集）**　用 $\emptyset$ 来表示那个不含任何元素的集合，即the empty set（空集）。

**The Natural Numbers（自然数）**　用 $\mathbb{N}$ 来表示由the natural numbers（自然数）——即positive integers（正整数）$1, 2, 3, 4$ 等等——组成的集合。

---

<span style="color:#7f8c8d">书页 A-2 · A.2.1 集合记号后半：整数、有理数、实数、闭/开/无限区间、列举法与描述法</span>

**The Integers（整数）**　用 $\mathbb{Z}$ 来表示由the integers（整数）——正整数、负整数与零——组成的集合。

**The Rational Numbers（有理数）**　用 $\mathbb{Q}$ 来表示the rational numbers（有理数）组成的集合，也就是所有形如 $m/n$ 的分数，其中 $m$ 与 $n$ 是整数（且 $n \neq 0$）。

**The Real Numbers（实数）**　用 $\mathbb{R}$ 来表示全体the real numbers（实数）。

**Closed Intervals（闭区间）**　用 $[a, b]$ 来表示介于 $a$ 与 $b$ 之间的全体数组成的集合，并且把 $a$ 与 $b$ 本身也包含在内。
我们假设 $a < b$。
这称为以 $a$ 与 $b$ 为endpoints（端点）的closed interval（闭区间）。
（有些作者允许 $a = b$ 的可能性，在这种情形下 $[a, b]$ 必须解释成只含单独一点 $a$ 的集合，并称之为degenerate interval（退化区间）；我们避免了这种用法。）

**Open Intervals（开区间）**　用 $(a, b)$ 来表示介于 $a$ 与 $b$ 之间但不把 $a$ 与 $b$ 包含在内的全体数组成的集合。
这称为以 $a$ 与 $b$ 为端点的open interval（开区间）。

**Infinite Intervals（无限区间）**　用 $(a, \infty)$ 来表示严格大于 $a$ 的全体数组成的集合。
符号 $\infty$ 并不被解释成一个数。
［对大多数学生来说，如果当初采用的是 $(a, \rightarrow)$ 这种记号，情况也许会更好些，因为它传达了同样的含义，而且初学的学生也就不会臆断在实数线的最右端“尽头”处真有某个叫做 $\rightarrow$ 的无穷大数了。］
其他的无限区间还有 $(-\infty, a)$、$[a, \infty)$、$(-\infty, a]$ 以及 $(-\infty, \infty) = \mathbb{R}$。

**Sets as a List（集合的列举法）**　用 $\{1, -3, \sqrt{7}, 9\}$ 来表示恰好包含 $1$、$-3$、$\sqrt{7}$ 与 $9$ 这四个实数的集合。
这是一种描述集合的有用方式（在可行时）：只需把属于该集合的元素一一列举出来。
注意在集合的世界里次序无关紧要，所以这份清单可以按我们希望的任何顺序给出。

**Set-Builder Notation（描述法，构造式记号）**　用 $\{x : x^2 + x < 0\}$ 来表示满足不等式 $x^2 + x < 0$ 的全体数 $x$ 组成的集合。
要认清这一点可能得花些时间<span style="color:#7f8c8d">（参见习题 A.2.1，原书习题按约定跳过不译）</span>，但如果你熟练掌握不等式与二次方程，就能认出这个集合恰好是开区间 $(-1, 0)$。
这是描述集合的又一种有用方式（在可行时）：只需用方程或不等式把属于该集合的元素描述出来。
一般地，如果 $C(x)$ 是关于对象 $x$ 的某种assertion（断言），那么 $\{x : C(x)\}$ 就是使 $C(x)$ 恰好为真的那些对象 $x$ 组成的集合。
还可以使用其他表述方式，例如

```math
\{x \in A : C(x)\}
```

它描述的是属于集合 $A$ 并且使 $C(x)$ 为真的那些元素 $x$ 组成的集合。
例子 $\{1/n : n \in \mathbb{N}\}$ 说明：对一个集合的成员施行运算，同样可以得到一个集合。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 这一套集合记号你在 6.042J 里早已天天使用：子集 $A \subset B$、交集 $A \cap B$、并集 $A \cup B$ 正是当时证明 De Morgan 律（德摩根律）用到的操作，描述法 $\{x : C(x)\}$ 也与那里「用谓词 $C$ 筛选满足条件的对象」的组合方式一致——谓词逻辑提供性质，集合负责收集使性质成立的全体对象。
> 所以本小节对你更像一次方言核对，而不是新知识。
> 但请留一个心眼：$C(x)$ 不能是任意性质。
> 习题 A.2.13（提示 388）埋了 Russell's paradox（罗素悖论）：取 $C(S)$ 为「$S \notin S$」，则 $R = \{S : S \notin S\}$ 若属于自身便违反自己的定义，若不属于自身又恰好符合定义，两个方向互相矛盾。
> 你在 6.042J 的集合部分见过这个悖论，此处它借描述法再次现身。
> 它说明「任意性质都能收集出一个集合」的朴素想法有漏洞，必须先限定哪些性质合法；严格处理属于公理集合论，本课程记住这条边界即可。

---

集合的语言需要一些专门的记号，这些记号想必你已经熟悉。
如果你发现自己需要复习，那就花些时间把这些记号学好，因为在你后续的所有数学课程中都会用到它们。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Subsets, Unions, Intersection, and Differences（子集、并集、交集与差集）</span>

> <span style="color:#7f8c8d;">TBB App A.2.1, p.A-2</span>

> <span style="color:#7f8c8d;">本小节的编号清单（子集、并集、交集、集合的差等记号的定义）从下一书页 A-3 开始，由后续译文继续。</span>

<!-- ===== t02 ===== -->

<span style="color:#7f8c8d">书页 A-3 · A.2.1 集合记号（Set Notation，续）：集合运算记号清单 · De Morgan 律 · 有序对与笛卡尔积</span>

---

1. 记号 $A \subset B$：若 $A$ 的每个 element（元素）同时也是 $B$ 的元素，则称 $A$ 是 $B$ 的 subset（子集）。
2. 记号 $A \cap B$ 是 $A$ 与 $B$ 的 intersection（交集），它是由同时属于这两个集合的元素组成的集合。
3. 记号 $A \cup B$ 是集合 $A$ 与 $B$ 的 union（并集），它是由属于其中任何一个集合的元素组成的集合。
4. 记号 $A \setminus B$ 是集合 $A$ 与 $B$ 的 difference（差），它是由属于 $A$ 但不属于 $B$ 的元素组成的集合。

> <span style="color:#7f8c8d">原书脚注 1：不要用 $A - B$ 来表示 set difference（集合的差），因为这会让人联想到 subtraction（减法），而减法是另一回事。</span>

---

在正文中我们还需要对由大量集合构成的 family of sets（集合族）构造并集与交集，而不仅仅是对两个集合。这类思想的进一步展开可参见习题。<span style="color:#7f8c8d">（所指为附录 A.2 习题 A.2.1–A.2.13，按约定跳过不译。）</span>

对集合的许多处理需要同时进行两个或更多个运算。或许应当记住的最简单情形就是 De Morgan's Laws（De Morgan 律）：

```math
A \setminus (B_1 \cup B_2) = (A \setminus B_1) \cap (A \setminus B_2)
```

以及一个对称的版本：

```math
A \setminus (B_1 \cap B_2) = (A \setminus B_1) \cup (A \setminus B_2).
```

只要你勾勒几幅图形，这两条规则便一目了然。没有任何特殊的理由要求这些「律」必须局限于两个集合 $B_1$ 与 $B_2$ 的情形。事实上，取自任意 indexing set（索引集）$I$ 的任何集合族 $\{B_i : i \in I\}$ 都必须服从同样的定律：

```math
A \setminus \left( \bigcup_{i \in I} B_i \right) = \bigcap_{i \in I} (A \setminus B_i)
```

以及

```math
A \setminus \left( \bigcap_{i \in I} B_i \right) = \bigcup_{i \in I} (A \setminus B_i).
```

这里的 $\bigcup_{i \in I} B_i$ 只不过是把诸集合 $B_i$ 的全部元素合并成一个大的集合所得到的集合（也就是说，构成一个大的并集）。类似地，$\bigcap_{i \in I} B_i$ 是同时处在所有集合 $B_i$ 之中的点组成的集合，也就是它们的公共交集。

> 这些定律正是以 Augustus De Morgan（1806–1871）的名字命名的，他在伦敦担任教授，生涯颇为体面，尽管人们记住他并非因为任何深刻的工作。
> 他是「mathematical induction（数学归纳法）」这一表述在 1838 年的首创者，也是第一个对它给出严格论述的人。
> 除了这些「律」之外，他还有一处有趣的名声来源：他曾担任 Lady Ada Lovelace 的家庭教师，有人说她是世界上第一位计算机程序员。
> 他的一则趣谜流传至今：他声称自己「在 $x^2$ 那一年恰好 $x$ 岁」。

---

#### <span style="color:#2471a3;">**[section]**</span> Ordered Pairs（有序对）

> <span style="color:#7f8c8d;">TBB App A.2.1, p.A-3</span>

给定两个集合 $A$ 与 $B$，我们常常需要讨论形如 $(a, b)$ 的 pair（对），其中 $a \in A$ 且 $b \in B$。
这个对的第一项来自第一个集合，第二项来自第二个集合。
由于在这里次序至关重要，它们被称为 ordered pairs（有序对）。
由满足 $a \in A$ 且 $b \in B$ 的全体有序对 $(a, b)$ 组成的集合记作

```math
A \times B
```

而这个集合被称为 $A$ 与 $B$ 的 Cartesian product（笛卡尔积）。

---

<span style="color:#7f8c8d">书页 A-4 · Relations（关系）· A.2.2 函数记号与定义 A.1</span>

#### <span style="color:#2471a3;">**[section]**</span> Relations（关系）

> <span style="color:#7f8c8d;">TBB App A.2.1, p.A-4</span>

在数学中我们经常需要在某个集合 $S$ 上定义 relation（关系）。
集合 $S$ 的元素可以通过共享某个共同特征而相互关联，也可以通过其中一者比另一者「更大」这一事实而相互关联。
例如，命题 $A \subset B$ 就是诸集合族上的一种关系，而 $a < b$ 则是某个数集上的一种关系。
分数 $\frac{p}{q}$ 与 $\frac{a}{b}$ 在它们定义同一个数时便是相关的；于是我们可以在全体分数组成的集合上定义一种关系：当 $pb = qa$ 时，就规定 $\frac{p}{q} \sim \frac{a}{b}$。

于是，集合 $S$ 上的关系 $R$ 就是用来判定命题 $xRy$（读作 x is related to y，即「$x$ 与 $y$ 相关」）是否为真的某种方法。
如果我们仔细审视这件事的形式，就会看到它完全可以由构造有序对的集合

```math
R = \{(x, y) : x \text{ is related to } y\}
```

来完整描述。
因此，某集合上的关系并不是一个新概念：它仅仅是有序对的一个汇集。
设 $R$ 是由 $S$ 中元素的有序对组成的任意集合，那么 $(x, y) \in R$、$xRy$ 与「$x$ 与 $y$ 相关」这三种说法可以被赋予相同的含义。
这就把关系化归为有序对。
在实践中，我们通常从最直观的视角来看待关系。
［例如，real line（实数轴）上的 order relation（序关系）$x < y$ 在技术上与有序对集合 $\{(x, y) : x < y\}$ 是同一回事，但几乎没有人会以这种方式来思考这个关系。］

---

### <span style="color:#2471a3;">**[section]**</span> A.2.2 Function Notation（函数记号）

> <span style="color:#7f8c8d;">TBB App A.2.2, p.A-4</span>

analysis（分析学）研究的是 function（函数），事实上大部分数学也是如此。
你还记得在初等 calculus（微积分）课程中，你常常会在 maxima and minima（极大值与极小值）问题、或者 derivative（导数）与 integral（积分）的背景下，讨论诸如 $f(x) = x^2 + x + 1$ 这样的某个函数吗？
在微积分中理解函数最重要的方式就是借助 graph（图像）：对这个函数而言，其图像就是由实数 $x$ 组成的全部数对 $(x, x^2 + x + 1)$ 构成的集合，而这个图像常常被勾画成二维空间中的一组点。

函数究竟是什么？
微积分课程的学生通常能把公式 $f(x) = x^2 + x + 1$ 理解为对一个函数的定义，但当 function 这个术语以不那么具体的方式被使用时，他们就开始感到困惑了。
例如，这里的函数 $f(x) = x^2 + x + 1$ 与诸如 $f(x^2 + x + 1)$ 这样的表述之间的区别究竟是什么？

#### <span style="color:#2471a3;">**[section]**</span> Definition of a Function（函数的定义）

> <span style="color:#7f8c8d;">TBB App A.2.2, p.A-4</span>

<span style="color:#2471a3;">**[definition]**</span> **<span style="color:#c0392b">Definition A.1（定义 A.1）</span>**：<span style="color:#00838f">从集合 $A$ 到集合 $B$ 内的函数 $f$（有时也称 map（映射））是一条规则，它为每个元素 $a \in A$ 指派一个值 $f(a) \in B$。</span>
输入集合 $A$ 被称为该函数的 domain（定义域）。
注意，$f$ 才是函数，而 $f(x)$（它并不是函数）是函数在元素 $x \in A$ 处所指派的值。
全部输出值组成的集合写作

```math
f(A) = \{b \in B : f(a) = b \text{ for some } a \in A\}
```

并被称为该函数的 range（值域）。

于是，上面这个微积分例子实际上断言：我们被给定了一个名为 $f$ 的函数，它的定义域是全体实数组成的集合，并且它把任何数 $a$ 指派为值 $f(a) = a^2 + a + 1$。
值域从定义本身来看并不清楚，如果有需要就必须把它计算出来。（要确定值域就是区间 $[3/4, \infty)$，这只是一个简单的练习。）

<!-- ===== t03 ===== -->

<span style="color:#7f8c8d">书页 A-5 · A.2.2 Function Notation（函数记号）续前页——函数作为有序对的集合、定义域与值域</span>

> <span style="color:#7f8c8d;">TBB App A.2.2, p.A-5（小节标题与定义 A.1 见上页 A-4）</span>

数学家们早已注意到，函数的 graph（图像）承载着描述该函数所需的全部信息。
的确，由于图像恰好是由全部ordered pair（有序对）$(x,f(x))$ 组成的一个集合，函数这一概念完全可以在集合的语言之内得到解释，而不需要发明任何新概念。
于是，函数就是图像，而图像就是一个集合。
因此，你应当料想到会看到如下这种更正式的函数定义。

<span style="color:#2471a3;">**[definition]**</span> <span style="color:#c0392b">**Definition A.2（定义 A.2）**</span>：设 $A$ 与 $B$ 是nonempty sets（非空集合）。

<span style="color:#00838f">由有序对 $(a,b)$ 组成的一个集合 $f$，其中 $a\in A$ 且 $b\in B$，若满足对每个 $a\in A$ 在 $f$ 中恰有一对 $(a,b)$，就称 $f$ 为从 $A$ 到 $B$ 的 function（函数），符号上记作 $f:A\to B$。</span>

记号 $(a,b)\in f$ 在 advanced mathematics（高等数学）中经常使用，但在表达calculus（微积分）与 analysis（分析）中的思想时却颇为笨拙。
作为替代，我们使用大家熟悉的表达式 $f(a)=b$。
此外，当我们希望把函数当作图像来思考时，通常会借助于 “graph” 这个词来提醒你。
因此，分析或微积分课程的学生预期看到的提问方式会是这样的：

> 求函数 $f(x)=x^{2}+x+1$ 的图像上使其tangent line（切线）为 horizontal（水平）直线的点。

而不是下面这种在技术上正确、看上去却笨拙的写法：

> 设 $f$ 为函数 $f=\{(x,\;x^{2}+x+1):x\in\mathbb{R}\}$，并求 $f$ 中使其切线为水平直线的点。

---

<span style="color:#2471a3;">**[definition]**</span> **Domain of a Function（函数的定义域）**

定义中的点集 $A$ 称为函数的 domain（定义域）。
它是任何函数的定义中一个必不可少的组成部分。
下面这种写法应当被认为是不正确的：设函数 $f$ 由 $f(x)=\sqrt{x}$ 定义。
相反，我们应当说：设函数 $f$ 由 $f(x)=\sqrt{x}$ 定义，其定义域为 $[0,\infty)$。
第一种断言是马虎的；它要求你去猜测这个函数的定义域是什么。
然而，微积分课程常常提出这种要求，把“从公式推究出应当给函数指派怎样的定义域”这件事留给你来完成。
我们也常常会同样地要求你这样做。

---

<span style="color:#2471a3;">**[definition]**</span> **Range of a Function（函数的值域）**

定义中的点集 $B$ 有时被称为 range（值域）或 codomain（对应域）。
大多数作者不喜欢把“值域”一词用在这里，而更愿意把“值域”这个词留给集合

```math
f(A)=\{f(x):x\in A\}\subset B
```

它由函数 $f$ 的实际输出值组成，而不是某个仅仅包含所有这些值的更大集合。

---

<span style="color:#7f8c8d">书页 A-6 · A.2.2 Function Notation（函数记号）续——单射、满射、双射、反函数、特征函数与函数的复合</span>

> <span style="color:#7f8c8d;">TBB App A.2.2, p.A-6</span>

<span style="color:#2471a3;">**[definition]**</span> **One-To-One and Onto Function（一对一与到上的函数）**

如果对 $f$ 的值域中的每个元素 $b$，在定义域中都恰有一个元素 $a$ 使得 $f(a)=b$，那么就称 $f$ 是 one-to-one（一对一函数）或 injective（单射的）。
关于函数的值域 $f(A)$，我们有时说，$f$ onto（到上）地把 $A$ 映到 $f(A)$ 上。
如果 $f:A\to B$，那么当 $B$ 恰是 $f$ 的值域时——也就是说，当对每个 $b\in B$ 都存在某个 $a\in A$ 使得 $f(a)=b$ 时——就称 $f$ 到上映到 $B$。
到上的函数有时被称为 surjective（满射的）。
既是一对一又是到上的函数有时被称为 bijective（双射）。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 双射在 6.042J 里承担过最重的一役：countability（可数性）——你正是通过在 $\mathbb{N}$ 与 $\mathbb{Q}$ 之间构造双射，数清了全体有理数。
> 本书在此把 one-to-one（一对一）、onto（到上）、bijective（双射）当作函数记号的基本词汇重新引入，术语与那时一致，但用途转向分析学：往后判定换元是否合法、级数能否重排，第一步常是检查映射是否一对一。
> 紧随其后出现的特征函数 $\chi_E$（在 $E$ 上取 $1$、其余处取 $0$）则有一个现成的编程对应物：flag（标志位）变量。
> 用 CSAPP（《深入理解计算机系统》）的眼光看，$\chi_E$ 就是用一个整数承载「是/否」信息的布尔指示变量，区别只在于它是真正的函数，可以参与极限与积分运算，而不只是放在 if 语句里被测试。
> 正文里你已经见过它最著名的例子 $\chi_{\mathbb{Q}}$（Dirichlet 函数，狄利克雷函数）：处处不连续，Riemann 积分不存在。
> 下一回遇到「把集合翻译成函数」的论证，不妨立刻认出这位老朋友。

---

<span style="color:#2471a3;">**[definition]**</span> **Inverse of a Function（函数的反函数）**

有些函数允许一个 inverse function（反函数）存在。
如果 $f:A\to B$ 是一个函数，那么有时会存在一个函数 $f^{-1}:B\to A$，它在下述意义上是 $f$ 的反向过程：对每个 $a\in A$ 以及每个 $b\in B$，分别有

```math
f^{-1}(f(a))=a,
\qquad\qquad
f(f^{-1}(b))=b.
```

于是 $f$ 把 $a$ 送到 $f(a)$，而 $f^{-1}$ 把 $f(a)$ 送回 $a$；同时 $f^{-1}$ 把 $b$ 送到 $f^{-1}(b)$，而 $f$ 把 $f^{-1}(b)$ 送回 $b$。
这种情况只有当 $f$ 是一对一的且到上映到 $B$ 时才可能发生。
关于这些概念的某些练习可参见习题部分。

---

<span style="color:#2471a3;">**[definition]**</span> **Characteristic Function of a Set（集合的特征函数）**

设 $E\subset\mathbb{R}$。
于是，为了讨论集合 $E$ 的各种性质，一个便利的函数是 $\chi_E$，它被定义为在 $E$ 上取值 $1$，而在其余每一点处取值 $0$。
这个函数被称为 $E$ 的 characteristic function（特征函数），有时也被称为 indicator function（指示函数）。

---

<span style="color:#2471a3;">**[definition]**</span> **Composition of Functions（函数的复合）**

设 $f$ 与 $g$ 是两个函数。
对 $x$ 的某些值而言，把这两个函数一个接一个地先后施用，所得的 $f(g(x))$ 可能是有意义的。
如果这样，这个新值就记作 $f\circ g(x)$ 或 $(f\circ g)(x)$，而这个函数被称为 $f$ 与 $g$ 的 composition（复合）。
$f\circ g$ 的定义域是所有那些使 $g(x)$ 有意义、并且随后 $f(g(x))$ 也有意义的 $x$ 值构成的集合；也就是说，$f\circ g$ 的定义域是

```math
\{\,x : x\in \mathrm{dom}(g)\ \text{and}\ g(x)\in \mathrm{dom}(f)\,\}.
```

注意这里的次序是有影响的，因此 $f\circ g$ 与 $g\circ f$ 通常有着截然不同的意义。
这很可能是初等数学中最早出现的一类运算：它不是 commutative（可交换的），并且需要人们加以某种小心对待。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 复合 $f \circ g$ 的记号藏着一个小陷阱：它读作「先 $g$ 后 $f$」，却把后执行者写在左边，与从左往右的书写习惯正好相反。
> 一个可靠的解法是用 pipeline（流水线）的视角代替死记：$f \circ g$ 就是数据先流过 $g$ 这一级、再流过 $f$ 这一级，正如 CSAPP（《深入理解计算机系统》）里指令流水线的各阶段按序推进，也像 CLRS（《算法导论》）归并排序递归展开时最内层的子问题先执行——写在里层的 $g$ 恰恰先于外层的 $f$ 运行。
> 把复合想成数据流经两级处理，「先里后外」便成了直觉而非口诀。
> 反函数的存在条件是同一主题的另一面：$f^{-1}$ 存在当且仅当 $f$ 是双射，这正是「操作可逆」的数学表述——整数加法可逆，减法就能恢复原值；而取模 $x \bmod n$ 不可逆，因为多个不同的输入被压成同一个输出。
> 浮点舍入同样如此：CSAPP 第 2 章讲过，舍入把多个实数压进同一个浮点数，信息就此丢失——这正是「不是一对一」的硬件版本。
> 要判定一个操作能否撤销，等价于判定它是否单射。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">A.2 Exercises（习题）</span>

> <span style="color:#7f8c8d;">TBB App A.2 Exercises, p.A-6</span>

<span style="color:#7f8c8d">*（此处为附录习题 A.2.1–A.2.13（Exercises）的起点，共 13 题，自本页 A-6 起延续至后续数页；习题 A.2.1 引入集合相等（set equality）的观念，其余习题涉及集合相等、区间表示、映射、单射/满射/双射、反函数、等价关系等练习，按约定跳过不收录。如需练习请读原书；练习时阅读英文原题是必要的学术技能。）*</span>

<!-- ===== t04 ===== -->

<span style="color:#7f8c8d">书页 A-7 · Section A.2（Notation 记号）习题页——本页自上而下均为附录习题，无正文段落</span>

> <span style="color:#7f8c8d;">TBB App A.2, p.A-7</span>

<span style="color:#1e8449;">**[note]**</span> 译者注：本页承接书页 A-6 末尾开始的 Section A.2 Exercises（习题区），页面顶部原有页眉噪音（Section A.2. / A-7 / Notation）已按约定剥离。本页自上而下依次为习题 A.2.1 之第 (f)、(g) 两小问的续文，以及习题 A.2.2、A.2.3、A.2.4、A.2.5（前半），全部按约定跳过不译，仅以下列灰注逐题标注范围与主题，便于读者对照原书定位练习。

---

<span style="color:#7f8c8d">*（此处为附录习题 A.2.1 之 (f)、(g) 两小问（Exercises，续书页 A-6），涉及集合恒等式 $(A\cap B)\setminus C=(A\setminus C)\cap(B\setminus C)$ 的证明，以及集合等式 $\{x\in\mathbb{R}:x^2+x<0\}=(-1,0)$ 的验证，按约定跳过不收录。）*</span>

---

<span style="color:#7f8c8d">*（此处为附录习题 A.2.2（Exercises），引入 $N$ 个集合 $A_1,A_2,\dots,A_N$ 的有限并与有限交记号 $\bigcup_{n=1}^{N}A_n$、$\bigcap_{n=1}^{N}A_n$，要求描述三组区间族 $\left(-\frac{1}{n},\frac{1}{n}\right)$、$(-n,n)$、$[n,n+1]$ 各自的有限并 $\bigcup$ 与有限交 $\bigcap$，按约定跳过不收录。）*</span>

---

<span style="color:#7f8c8d">*（此处为附录习题 A.2.3（Exercises），引入集合序列 $A_1,A_2,\dots$ 的无穷并与无穷交记号 $\bigcup_{n=1}^{\infty}A_n$、$\bigcap_{n=1}^{\infty}A_n$，并对同样三组区间族作无穷并与无穷交的描述练习，按约定跳过不收录。）*</span>

---

<span style="color:#7f8c8d">*（此处为附录习题 A.2.4（Exercises），考查「下列各式中哪些可算作函数 $f$ 的恰当定义」（定义域未指定，须自行寻找可行定义域）：五个候选含 $f(x)=1/\sqrt{1-x}$；有理数时 $f(x)=x$ 而无理数时 $f(x)=-x$；十进制展开中含数字 $9$（或 $7$）时取 $1$ 否则取 $0$；素数（prime number）示性定义等，题末标注参见附录 Note 387，按约定跳过不收录。）*</span>

---

<span style="color:#7f8c8d">*（此处为附录习题 A.2.5 之前半（Exercises，至第 (a) 小问为止），推广 mapping（映射）一词在函数研究中的用法：若 $f:X\to Y$ 且 $E\subset X$，则 $f(E)=\{y:\exists\,x\in E,\ f(x)=y\}\subset Y$ 称为 $E$ 在 $f$ 下的 image（像），并称 $f$ 把 $E$ 映到集合 $f(E)$；第 (a) 小问要求举出使 $f(A\cap B)\neq f(A)\cap f(B)$ 的集合 $A,B$ 的例子，按约定跳过不收录。）*</span>

---

<span style="color:#7f8c8d">书页 A-8 · Section A.2（Notation 记号）习题页（续）——本页自上而下仍均为附录习题，无正文段落</span>

> <span style="color:#7f8c8d;">TBB App A.2, p.A-8</span>

<span style="color:#1e8449;">**[note]**</span> 译者注：本页页面顶部原有页眉噪音（A-8 / Appendix: Background / Appendix A）已按约定剥离。本页自上而下依次为习题 A.2.5 之后半，以及习题 A.2.6、A.2.7、A.2.8、A.2.9、A.2.10（前半），全部按约定跳过不译，仅以下列灰注逐题标注范围与主题。

---

<span style="color:#7f8c8d">*（此处为附录习题 A.2.5 之后半（Exercises）：第 (b) 小问追问 $f(A\cup B)=f(A)\cup f(B)$ 是否一般成立，第 (c) 小问要求求出函数 $f:\mathbb{R}\to\mathbb{R}$ 使 $f([0,1])=\{1,2\}$，按约定跳过不收录。）*</span>

---

<span style="color:#7f8c8d">*（此处为附录习题 A.2.6（Exercises），考查 one-to-one function（一对一函数，即 injective 单射）的两个刻画：第 (a) 小问证明 $f:\mathbb{R}\to\mathbb{R}$ 为一对一当且仅当对一切集合 $A,B$ 有 $f(A\cap B)=f(A)\cap f(B)$；第 (b) 小问证明一对一当且仅当对一切满足 $A\cap B=\emptyset$ 的集合 $A,B$ 有 $f(A)\cap f(B)=\emptyset$，按约定跳过不收录。）*</span>

---

<span style="color:#7f8c8d">*（此处为附录习题 A.2.7（Exercises），考查 preimage（原像）概念：若 $f:X\to Y$ 且 $E\subset Y$，则 $f^{-1}(E)=\{x:\exists\,y\in E,\ f(x)=y\}\subset X$ 称为 $E$ 在 $f$ 下的原像；原题方括号内强调此处未必存在 inverse function（反函数），$f^{-1}(E)$ 即使在没有反函数时仍有意义；五个小问含 $f(f^{-1}(E))\subset E$、$f^{-1}(f(E))\supset E$、化简 $f^{-1}(A\cup B)$ 与 $f^{-1}(A\cap B)$、「一对一当且仅当对任意 $b\in\mathbb{R}$，$f^{-1}(\{b\})$ 至多含一点」以及「到上当且仅当对每个 $E\subset\mathbb{R}$ 有 $f(f^{-1}(E))=E$」，按约定跳过不收录。）*</span>

---

<span style="color:#7f8c8d">*（此处为附录习题 A.2.8（Exercises），考查 composition of functions（函数的复合）：第 (a) 小问举出 $f\circ g$ 与 $g\circ f$ 相异的例子，第 (b) 小问举出二者并不相异的例子，第 (c) 小问追问复合虽不交换、但是否满足结合律 $(f\circ g)\circ h=f\circ(g\circ h)$，第 (d) 小问要求给出若干满足 $f\circ f=f$ 的函数例子，按约定跳过不收录。）*</span>

---

<span style="color:#7f8c8d">*（此处为附录习题 A.2.9（Exercises），考查 onto function（到上映射，即 surjective 满射）：下列六个函数中哪些把 $[0,1]$ 映到 $[0,1]$ 上——$f(x)=x$、$f(x)=x^2$、$f(x)=x^3$、$f(x)=2\left|x-\frac{1}{2}\right|$、$f(x)=\sin\pi x$、$f(x)=\sin x$，按约定跳过不收录。）*</span>

---

<span style="color:#7f8c8d">*（此处为附录习题 A.2.10 之前半（Exercises，至第 (c) 小问为止，第 (d)、(e) 两小问续于书页 A-9），考查 one-to-one and onto function（一对一且到上的函数，即 bijection 双射）：第 (a) 小问问习题 A.2.9 诸函数中哪些是 $[0,1]$ 到 $[0,1]$ 的双射，第 (b) 小问问 $f(x)=x^2$ 是否为 $[-1,1]$ 到 $[0,1]$ 的双射，第 (c) 小问求 $[0,1]$ 到区间 $[3,6]$ 上的线性双射，按约定跳过不收录。）*</span>

---

<span style="color:#7f8c8d">*（本页至此习题区未完：书页 A-9 续有习题 A.2.10 之 (d)、(e) 两小问，以及习题 A.2.11–A.2.13，涉及反函数、等价关系（equivalence relation）与借助描述法的自指集合（罗素悖论式）练习，由后续书页的翻译按同一约定处理。）*</span>

<!-- ===== t05 ===== -->

<span style="color:#7f8c8d">书页 A-9 · A.2 习题收尾（A.2.10 后半至 A.2.13）与 A.3 什么是分析学（开头）</span>

---

<span style="color:#7f8c8d">*（此处为附录习题 A.2.10（Exercises）的后半部分，即第 (d)、(e) 两小题：要求构造 $[0,1]$ 到区间 $[3,6]$ 的一个非线性 bijection（双射），以及构造 $\mathbb{N}$ 到 $\mathbb{Z}$ 的一个双射，按约定跳过不收录。）*</span>

<span style="color:#7f8c8d">*（此处为附录习题 A.2.11（Exercises），涉及 inverse function（反函数）概念：为习题 A.2.9 中的每一个函数选取一个使该函数存在反函数的区间 $[a,b]$，并写出反函数的显式公式，且务必陈述反函数的定义域，按约定跳过不收录。）*</span>

<span style="color:#7f8c8d">*（此处为附录习题 A.2.12（Exercises），涉及 equivalence relation（等价关系）概念：集合 $S$ 上的关系 $x\sim y$ 若满足 (a) 对一切 $x\in S$ 有 $x\sim x$；(b) $x\sim y$ 蕴含 $y\sim x$；(c) $x\sim y$ 且 $y\sim z$ 蕴含 $x\sim z$，则称为等价关系；习题要求证明正文在分数集合上定义的关系 $p/q\sim a/b$（其中 $pb=qa$）是等价关系，并要求构造只满足其中两条要求的关系以及 $\mathbb{N}$、$\mathbb{Z}$ 上的非平凡等价关系，按约定跳过不收录。）*</span>

<span style="color:#7f8c8d">*（此处为附录习题 A.2.13（Exercises），涉及用 set builder notation（描述法/构造式记号）“描述”奇异集合所引出的悖论：$S_1=\{S : S \text{ is a set}\}$ 具有奇特性质 $S_1\in S_1$（好比加入一个俱乐部，却发现俱乐部的名字作为成员出现在会员名单上）；更糟的是 $S_2=\{S : S \text{ is a set and } S\notin S\}$，它具有悖论性质：若 $S_2\in S_2$ 则 $S_2\notin S_2$，而若 $S_2\notin S_2$ 则 $S_2\in S_2$——这正是与 Russell's paradox（罗素悖论）同源的集合论悖论；原书此处标注参见 Note 388。按约定跳过不收录。）*</span>

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">A.3 What Is Analysis?（什么是分析学？）</span>

> <span style="color:#7f8c8d;">TBB App A.3, p.A-9</span>

---

术语 “analysis”（分析学）如今覆盖着数学的绝大部分版图。

你几乎得成为一名职业数学家，才能弄明白这个词究竟意味着什么。

不过，对于这个层次的课程而言，real analysis（实分析）主要指的还是你在微积分课程里已经学过的那些内容：limits（极限）、continuity（连续性）、derivatives（导数）、integrals（积分）、sequences（序列）与 series（级数）。

---

微积分作为一门学科，可以看作十八世纪的发展成果；而分析学，则是十九世纪的创造。

微积分的种种观念，没有一个曾建立在十分牢固的基础之上，而这种基础的缺乏被证明是继续前进的障碍。

数学家与哲学家曾对微积分的基本观念（尤其是极限）提出过大量批评；而且，当新的、有争议的方法（例如 Fourier series（傅里叶级数））被提出来时，当时的数学家往往无法就这些方法是否有效达成一致。

---

进入十九世纪的最初几十年，这门学科的基础被重新打造，其中贡献最著者是 Cauchy（柯西）——这个名字将在本书中频繁出现——与此同时，新的、强有力的方法也发展了起来。

我们在这里研究的，正是这一切。

---

<span style="color:#7f8c8d">书页 A-10 · A.3 什么是分析学（续）与 A.4 为什么要证明（开头）</span>

---

我们将再一次考察 sequence limit（序列极限）、function limit（函数极限）等概念——它们都是我们在微积分课堂上已经见过的——但这一次要从一个更严格的观点出发。

我们想要精确地知道这些概念究竟是什么意思，以及如何证明这门学科中各种技术的有效性。

---

初看上去，你也许会对此感到疑惑：我们难道只是在复习微积分，只不过这一回不许跳过证明的细节了吗？

然而，只要你坚持下去，你就会看到，我们进入的其实是一个全新而不同的世界。

通过仔细审视“某些事情为何成立”的种种细节，我们获得了一种新的洞见。

不仅如此，我们还能做新的事情——那些在单纯的微积分层次上根本无法想象的事情。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 本节是全书的自我定位宣言：「微积分是十八世纪的成果、分析学是十九世纪的创造」，划出的是计算技术与奠基工程的分界。前文的批评并非抬杠：Fourier series（傅里叶级数）这类新方法逼得数学家必须说清「极限究竟是什么」，Cauchy（柯西）的基础重构正是对此的回应。分析学与代数的分界线只有一条——是否出现无穷过程：代数处理的是有限步能算完的对象，而 limit（极限）本质上是无穷过程，「$s_n \to s$」一句话压缩了无穷多次逼近，有限次代入永远验证不了它。你在 100B 前 13 章走的路线——实数 completeness（完备性）、序列、级数、连续、度量空间——正是「把极限改造成可计算的严格对象」的历程：第 1 章的 Dedekind cut（戴德金分割）与 supremum（上确界）公理给无穷逼近提供了必须有着落点的地基，$\varepsilon$-$N$ 语言把「无限接近」翻译成有限步可检验的不等式。带着这个视角回读本节末段，「我们进入的其实是一个全新而不同的世界」便有了精确含义：跨过有限与无穷的分界，才算从代数走进分析。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">A.4 Why Proofs?（为什么要证明？）</span>

> <span style="color:#7f8c8d;">TBB App A.4, p.A-10</span>

---

难道我们不能不做证明就去从事数学吗？

当然，现实中有许多数学应用，是由没有能力、或者不愿尝试证明的人推进的。

但是，数学最核心、最灵魂的东西恰恰是 proof（证明）——那种细致入微的论证，它表明一个 statement（断言）为真。

---

不妨把这一点与 natural sciences（自然科学）比较一下。

在那些学科里，知识的进步依托于 experiment（实验）。

没有任何一位科学家会认真考虑：学生是否可以跳过实验操作、只学结果。

一切科学发现的核心，都是 experimental method（实验方法）。

它太处于这门学科的中心位置了，根本无法被移除。

它正是这门学科取得巨大成功的原因所在。

---

数学家对证明怀有完全相同的感受。

凭借想象力与洞察力，我们能够做出合理的 conjecture（猜想）。

但在把一个猜想证明出来之前，我们无法确定它为真。

数学史上充满了由数学家——甚至是大名鼎鼎的数学家——提出的看似有理（实则错误）的断言。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 这段实验类比可以直接接到你的工程经验上：软件测试之于程序，正如 experiment（实验）之于自然科学——两者都只能在有限个样本上做检验。你在 CLRS 里见过的「随机采样验证」正是这个路数：跑一批测试没有发现失败，只是提高信心，并不构成正确性保证。图灵奖得主 Dijkstra 在 1969 年的手稿 Notes on Structured Programming（结构化编程笔记，即 EWD249）里把这一点说到了根上："Program testing can be used to show the presence of bugs, but never to show their absence."（翻译：程序测试可以用来证明 bug 的存在，却永远无法证明 bug 不存在。）证明不可替代的原因正在于此：它是唯一的「全称量化验证」，一条证明同时覆盖无穷多个输入，而任何测试集都是有限集——这正是本附录 A.9 量词一节里 $\forall$（全称量词）要形式化的那件事。
> 🎥 *Colding 在 V03 讲座中回应「何必形式化」的疑问："It may seem like a formal thing. Why bother with that? But it's really, really useful. And the more complicated things become, the more useful it is."（翻译：形式化看似繁文缛节，何必费这个劲？但它真的非常有用，而且对象越复杂，它就越有用。）*

---

证明是这门学科不可或缺的组成部分。

如果你能掌握阅读证明与书写证明的技艺，你就真正进入了这门学科。

如果不能，你就永远停留在门外向里张望——一个只能学到若干关于数学的肤浅事实、却无力从事数学的旁观者。

---

数学家总是随时准备精确地定义他们这门学科中的每一个事物。

当然，要精确地定义“什么构成一个证明”是可能的。

但那件事最好留给逻辑课程去完成。

---

对于一门分析学课程，你只需这样理解：证明就是或短或长的一系列论证，其目的在于使我们相信某个断言为真。

在你读过一些证明、并且发现自己确实能跟上论证之后，你就会明白什么是证明。

---

证明永远是为特定的读者群而写的。

本书中的证明，是为这样一些读者写的：他们有一定的微积分经验、具备良好的推理能力，但分析学经验尚浅。

更高深教材中的证明会简短得多，动机性的铺垫也更少。

而专业研究期刊上的证明——面向的是其他职业数学家——则可能确实极其简洁而晦涩。

---

传统上，分析学课程开篇并不怎么讨论证明，尽管学生们将被要求亲手写出证明——这也许是他们求学生涯中的头一遭。

最好的建议也许只是：纵身一跃，开始研读……

> <span style="color:#7f8c8d">*（书页 A-10 在此结束：上一句在页末中断，下接书页 A-11 续写。页面底部出现的 “What Is a Proof?” 为下一小节 A.4.1 What Is a Proof?（什么是证明？）的标题起始，其正文由后续译文接续。）*</span>

<!-- ===== t06 ===== -->

<span style="color:#7f8c8d">书页 A-11 · A.4 Why Proofs?（为什么要证明？）末尾的三个建议框（「什么是证明？」框之续、如何阅读证明、如何撰写证明），随后进入 A.5 Indirect Proof（间接证明）</span>

> <span style="color:#7f8c8d;">TBB App A.4/A.5, p.A-11</span>

<span style="color:#1e8449;">**[note]**</span> 译者注：本页顶部原有页眉噪音（Section A.5. / Indirect Proof / A-11）已按约定剥离。本页开头承接书页 A-10 末尾开始的「什么是证明？」（What Is a Proof?）建议框——该框的标题与起始句在上页，其末句 "Start studying…" 恰在页末中断，故本页首句以省略号续接。

---

> **「什么是证明？」框（续书页 A-10）**
>
> ……研读教材中的证明、课堂上给出的证明、以及身边同学们尝试写出的证明。
> 要试着亲手把它们写出来。
> 先读一个证明，弄懂它的主要思想，然后尝试用自己的话把整个论证重新写出来。

---

> **How to Read a Proof（如何阅读证明）**
>
> 虽然一个证明看上去可能像一篇短篇故事，但读起来往往比故事难得多。
> 通常，其中某些计算会显得并不清楚，你必须自己弄清它们当初是怎么做出来的。
> 有些论证（由「这是真的」推出「因此那也是真的」这一类）不会让人一目了然，而需要你动一番脑筋。
> 许多步骤会显得全然怪异，你会觉得这个证明正朝着某个完全莫名其妙的怪异方向走去。
> 从根本上说，你必须把这个证明拆解开来看。
> 要找出证明的主要思想是什么，以及它的各个步骤分别是什么。
> 阅读证明时有一条重要建议：要随时记住有待证明的究竟是什么。
> 在读证明之前，先确定必须证明的到底是哪一件事。
> 问问你自己：「要证明这一点，我需要拿出什么来看？」

---

> **How to Write a Proof（如何撰写证明）**
>
> 多加练习！我们正是通过亲手写证明来学会写证明的。
> 起步时，不妨把教材里一个你觉得有趣的证明几乎逐字照抄一遍。
> 再改动措辞，换用你自己的说法。
> 然后用比原文更多的步骤、更多的细节把这个证明完整写出来。
> 试着为同一个命题另找一个不同的证明，并把你的新证明写出来。
> 如果可能，试着调换论证的先后次序。
> 如果不可能，你很快就会看出原因何在。
> 我们每个人起初都是靠模仿学会证明这门艺术的。

---

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">A.5 Indirect Proof（间接证明）</span>

> <span style="color:#7f8c8d;">TBB App A.5, p.A-11</span>

分析学中的许多证明都是作为 indirect proof（间接证明）来实现的。
这里指的是一种特定的方法。
该方法按如下方式进行论辩。
我希望证明某个陈述 $P$ 为真。
陈述 $P$ 要么为真，要么为假，二者不可兼得。
如果我假设 $P$ 为假，那么或许我能证明：这样一来，某件完全不可置信的事情就必须为真。
既然那件不可置信的事情并不为真，由此可知「$P$ 为假」这种情况不可能成立。
因此，$P$ 为真。

---

这种方法在古典学科 rhetoric（修辞学）中以 reductio ad absurdum（归谬法，拉丁文原义「我把它归约到荒谬」）之名出现。

> 女士们、先生们：我可敬的对手声称 $P$ 成立，而我主张相反的命题，即 $Q$。
> 不妨假设他的主张成立。那么……接着……而那就意味着……。
> 可这太荒谬了，所以他的主张是错的，我的主张必定为真。

---

一切间接证明（也被称为 proof by contradiction，反证法）都遵循这样一个模式：
我们希望证明陈述 $P$ 为真。
为了导出矛盾，姑且假设 $P$ 为假。
这将蕴涵下面一系列陈述。
（随后是一串陈述。）
但这是不可能的。
于是可知 $P$ 为真，此即所要证明的结论。

---

下面是一个简单的例子。
假设我们希望证明：

> 对一切正数 $x$，分数 $1/x$ 也是正数。

一个间接证明将会这样进行。

---

<span style="color:#7f8c8d">书页 A-12 · A.5 Indirect Proof（间接证明）——正数倒数一例的反证、对间接证明的两点评论、A.5 习题（跳过）、A.6 Contraposition（逆否证法）开篇</span>

> <span style="color:#7f8c8d;">TBB App A.5/A.6, p.A-12</span>

<span style="color:#1e8449;">**[note]**</span> 译者注：本页顶部原有页眉噪音（A-12 / Appendix: Background / Appendix A）已按约定剥离。本页承接上页 A-11 末句「一个间接证明将会这样进行」，给出上述例子的证明。

---

<span style="color:#2471a3;">**[proof]**</span> <span style="color:#c0392b">**Proof（证明）**</span>

假设该陈述不真。
于是存在某个正数 $x$，然而 $1/x$ 却不是正数。
这意味着

```math
\frac{1}{x}\leq 0.
```

由于 $x$ 是正数，我们可以用 $x$ 去乘不等式的两边，并且不等号方向保持不变（这是我们在小学里就学到的一条不等式性质，因此无须再作解释）。
于是

```math
x\times\frac{1}{x}\;\leq\; x\times 0
```

亦即

```math
1\leq 0.
```

这是不可能的。
由这个矛盾即可推知，该陈述必定为真。$\blacksquare$

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 把本节的方法钉成一个可复用的命名模板——「反证法（归谬法）三步」：第一步，写出结论的 negation（否定）；第二步，只凭合法推理往前走，不许偷用结论本身；第三步，撞上矛盾即收尾，宣告原结论为真。上面的 $1/x$ 例子把三步各走了一遍，而收尾处宣告矛盾的那句话，在讲座里对应一个专门的记号。
> 🎥 *Colding 在 V03 讲座中指着矛盾处的记号说："This is a standard symbol that means this is a contradiction."（翻译：这是一个标准记号，含义是「此处出现矛盾」。）*
> 他也用 $\sqrt{2}$ 亲自示范过「如何写证明」：
> 🎥 *Colding 在 V03 讲座中说明示范的做法："…by writing a formal proof of why square root of 2 is a real number."（翻译：……通过写出「为什么 $\sqrt{2}$ 是实数」的一个形式证明。）*
> 这两个对象你在 6.042J 都亲手反证过：素数无穷对应习题 A.5.2 背后 Note 390 的欧几里得证明，$\sqrt{2}$ 无理对应习题 A.5.1 的提示 Note 389。提示 389 的「两倍必偶」论证——平方是某数的两倍，则平方为偶、底数必偶——要起步还得先取一个「分子分母不全为偶」的表示，这种「除到不能再除、挑最小代表」的操作正是 well-ordering（良序性）最经典的应用场景之一：任何非空的自然数集必有最小元，「最小反例」式推理全靠它兜底。本附录 A.8 的习题 A.8.8 正要你证明归纳原理与良序性等价，届时可回头对照这条注。

---

间接证明极为有用，在整个分析学中随处可见。
然而在某些方面，它们也可能令人不够满意。
在说出「假设不然」这句话之后，证明便进入了一个幻想世界，其中的一切推演都在为制造矛盾而服务。
在通往矛盾的路上，你写下的任何一个陈述都未必有多大意思，因为它们都建立在一个虚假的前提之上。
相反，在 direct proof（直接证明）中，你写下的每一句话都是真的，其本身就可能饶有趣味，而不只是用来证明当前定理的一个工具。

此外，间接证明栖身于这样一个逻辑系统之中：其中任何不真的陈述就是假的，任何不假的陈述就是真的。
有人曾论证说，我们或许愿意生活在一个这样的数学世界里：在那里，即便你已经证明了某件事不假，你也仍然没有成功地证明它为真。

<span style="color:#1e8449;">**[note]**</span> 译者注：末两句触及的是经典逻辑的二值原则——「不假即真」。在 intuitionism（直觉主义）看来，「$P$ 不假」（即 $\neg\neg P$）并不足以给出「$P$ 为真」的构造性证明；这正是反证法在部分数学家中引起保留的根源，读者可与后文的构造思想相互印证。需要强调，本书（以及主流分析学）采用经典逻辑，反证法是合法且被广泛使用的证明手段；直觉主义的批评与其说是否定结论本身，不如说是在追问「存在」一词的证明论含义——是否必须给出一个具体的构造才算「存在」。你曾在 6.042J 中见过构造性存在证明与纯存在证明的区分，此处正是它在逻辑哲学层面的回声；对课程而言，记住反证法的操作规则即可，不必卷入这场哲学争论。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">A.5 Exercises（习题）</span>

> <span style="color:#7f8c8d;">TBB App A.5 Exercises, p.A-12</span>

<span style="color:#7f8c8d">*（此处为附录习题 A.5.1–A.5.2（Exercises），共 2 题：习题 A.5.1 要求通过给出一个间接证明来证明 $\sqrt{2}$ 是 irrational number（无理数），题末标注参见附录 Note 389；习题 A.5.2 要求证明存在无穷多个 prime number（素数），题末标注参见附录 Note 390；按约定跳过不收录。如需练习请读原书；练习时阅读英文原题是必要的学术技能。）*</span>

---

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">A.6 Contraposition（逆否证法）</span>

> <span style="color:#7f8c8d;">TBB App A.6, p.A-12</span>

我们希望证明的那些最常见的数学assertion（断言），都可以在符号上写成

```math
P\Rightarrow Q,
```

朗读出来便是「陈述 $P$ 蕴含陈述 $Q$」。
附着于其上的真正含义无非是：如果陈述 $P$ 为真，那么陈述 $Q$ 就为真。
对这一含义稍作反思便可看出，下面两种说法

> 若 $P$ 为真，则 $Q$ 必为真

与

> 若 $Q$ 为假，则 $P$ 必为假

<span style="color:#7f8c8d">*（上述句子的谓语在原书中延续至书页 A-13，由后续译文承接。）*</span>

<!-- ===== t07 ===== -->

<span style="color:#7f8c8d">书页 A-13 · A.6 Contraposition（逆否证法）收尾——逆否命题与积分一例、A.6 习题（跳过）——及 A.7 Counterexamples（反例）开篇</span>

> <span style="color:#7f8c8d;">TBB App A.6/A.7, p.A-13</span>

<span style="color:#1e8449;">**[note]**</span> 译者注：本页顶部原有页眉噪音（Section A.7. / A-13 / Counterexamples）已按约定剥离。本页承接书页 A-12 末尾中断的句子——原文刚给出两种等价的说法「若 $P$ 为真，则 $Q$ 必为真」与「若 $Q$ 为假，则 $P$ 必为假」，本页由此续写其谓语。

---

……这两种说法在意义上完全相同。
这两种说法互为 contrapositive（逆否命题）。
任何一个陈述 $P\Rightarrow Q$ 都有一个逆否命题 $\text{not}\ Q \Rightarrow \text{not}\ P$，它与原陈述等价。
要证明一个陈述，有时更好的做法不是直接证明它，而是转而去证明它的逆否命题。

---

这里有一个简单的例子。
假设作为微积分课程的学生，我们被要求证明下面这件事：

> 假设 $\int_0^1 f(x)\,dx \neq 0$，那么必定存在一点 $\xi \in [0,1]$，使得 $f(\xi) \neq 0$。

---

乍一看，仅凭这么少的信息，似乎很难想清楚我们要怎样找出那个点 $\xi \in [0,1]$。
但让我们改为去证明它的 contrapositive（逆否命题）。
这个逆否命题会说：如果在 $[0,1]$ 中不存在使 $f(\xi)\neq 0$ 的点 $\xi$，那么 $\int_0^1 f(x)\,dx \neq 0$ 就不会成立。
让我们把其中的双重否定消去。
重新表述之后，我们现在看到，逆否命题说的是：如果对每一个 $\xi \in [0,1]$ 都有 $f(\xi)=0$，那么 $\int_0^1 f(x)\,dx = 0$。
就连那些成绩为 C- 的学生（他们当中可没有一个人在读这本书）此刻也知道该怎样继续下去了。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 这套操作你在 6.042J 的 propositional logic（命题逻辑）里已有完整工具：$P \Rightarrow Q$ 与 $\neg Q \Rightarrow \neg P$ 的等价，一张 truth table（真值表）四行即可验证完毕。逆否证法没有引入任何新逻辑，只是换一个等价说法切入问题。要紧的是别把它与 converse（逆命题）混为一谈：$Q \Rightarrow P$ 与原命题并不等价，正向定理为真时逆命题可真可假，本附录 A.7 的 The Converse 小节用「可微 $\Rightarrow$ 连续，但连续 $\not\Rightarrow$ 可微」（$f(x)=|x|$）给出了现成对照。实用准则：当结论是否定式时（如习题 A.6.1 的「$x$ 是无理数」），直接证明常常无从下手，因为「无理」只告诉你它不是形如 $p/q$ 的数；反证或逆否却给出可操作的出发点——提示 391 正是这样把命题翻译成「若对某个有理数 $r$ 有 $x+r$ 为有理数，则 $x$ 为有理数」，写下等式就能往下算。记住这个不对称性：肯定式结论宜直接进攻，否定式结论宜先翻译成肯定式再进攻，反证与逆否就是两台翻译机。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">A.6 Exercises（习题）</span>

> <span style="color:#7f8c8d;">TBB App A.6 Exercises, p.A-13</span>

<span style="color:#7f8c8d">*（此处为附录习题 A.6.1（Exercises），共 1 题：要求用 contraposition（逆否证法）证明如下断言——若 $x$ 是 irrational number（无理数），则对一切 rational number（有理数）$r$，$x+r$ 都是无理数；题末标注参见附录 Note 391。按约定跳过不收录。如需练习请读原书；练习时阅读英文原题是必要的学术技能。）*</span>

---

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">A.7 Counterexamples（反例）</span>

> <span style="color:#7f8c8d;">TBB App A.7, p.A-13</span>

---

多项式 $p(x)=x^2+x+17$ 有一个有趣的特性：它能在一段时间内持续生成 prime number（素数）。
例如，$p(1)=19$、$p(2)=23$、$p(3)=29$、$p(4)=37$ 全都是素数。
还可以核验出更多的例子。
在再做了许多次计算之后，我们会忍不住想要提出这样一个主张：

> 对每一个整数 $n=1,2,3,\dots$，数值 $n^2+n+17$ 都是素数。

---

要证明它是真的（如果它确实是真的），我们就必须对任意的 $n$——不论它是多少——都证明数值 $n^2+n+17$ 是素数。
那么，要驳倒这个陈述，也就是说，要证明它为假，需要付出什么？

---

所需的全部东西，只是该陈述失效的一个实例。
仅仅一个！
事实上这样的实例有许多。
只要给出其中一个就够了。
取 $n=17$，并注意到

```math
17^2+17+17=17(17+1+1)=17\cdot 19,
```

它显然不是素数。
这一个例子就足以证明该陈述为假。
我们把这种做法称为proof by counterexample（反例证明）。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 这类「看起来总在产生素数」的多项式有一个更著名的先例：Euler（欧拉）1772 年提出的 $x^2+x+41$，它对 $x=0,1,2,\ldots,39$ 全部给出素数，直到 $x=40$ 才失效——此时 $40^2+40+41=41^2$，恰是 $41$ 的平方。
> 本节的 $x^2+x+17$ 正是同一思路的缩小版，而且它的反例位置并不神秘：把 $x=p-1$ 代入 $x^2+x+p$ 便得 $p^2$，所以 $x=16$ 时就有 $17^2=289$，书里取 $n=17$（得 $17\cdot 19$）只是众多反例之一。
> 方法论上请记住这个模板：单个 counterexample（反例）即可否定一个全称命题，此前验证过多少个正例都无法替代它。
> 这正是 A.9 量词语言将要形式化的事实——要反驳「$\forall n$，$n^2+n+17$ 是素数」，依据否定法则 $\neg\forall=\exists\neg$，只需找到一个使predicate（谓词）为假的 $n$。
> 用你在 6.042J 里的话说：反例就是「找出让命题变假的那个元素」，它与构造证明共享同一套量词逻辑，只是方向相反。

---

<span style="color:#7f8c8d">书页 A-14 · A.7 Counterexamples（反例）续——The Converse（逆命题）小节、A.7 习题（跳过）——及 A.8 Induction（归纳法）开篇</span>

> <span style="color:#7f8c8d;">TBB App A.7/A.8, p.A-14</span>

<span style="color:#1e8449;">**[note]**</span> 译者注：本页顶部原有页眉噪音（A-14 / Appendix: Background / Appendix A）已按约定剥离。本页承接书页 A-13——上页末尾给出了「反例证明」这一说法，本页继续讨论分析学中何时需要亲手构造反例。

---

在 analysis（分析学）中，我们将经常需要构造 counterexample（反例）。
下面是一个经常出现的情形。
假设我们刚刚成功地完成了一个 theorem（定理）的证明，该定理用符号表示为

```math
P\Rightarrow Q,
```

一个自然的问题是：converse（逆命题）是否也为真？
逆命题就是方向相反的implication（蕴含式）：

```math
Q\Rightarrow P.
```

---

> **逆命题（The Converse）**

> <span style="color:#7f8c8d;">TBB App A.7, p.A-14</span>

的确，一旦证明了任何一个定理，接着去追问它的逆命题是否为真，就近乎成了例行动作。
许多逆命题都是假的，而此时的证明通常就在于寻找一个反例。
例如，在微积分课程里（在分析学课程里也同样如此）人们证明了：每一个 differentiable function（可微函数）都是 continuous function（连续函数）。
把它表达成一个蕴含式，就是：

> $f$ 是可微的 $\;\Rightarrow\;$ $f$ 是连续的

因此，其逆命题的陈述便是：

> $f$ 是连续的 $\;\Rightarrow\;$ $f$ 是可微的

这个逆命题是真的吗？
如果它是真的，那么它同样应当得到证明。
如果它是假的，那就必须找到一个反例。
要证明它为假，我们只需给出一个连续却不可微的 function（函数）就够了。
你也许还记得，函数 $f(x)=|x|$ 正是连续却不可微的，因为在点 $0$ 处导数并不存在。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">A.7 Exercises（习题）</span>

> <span style="color:#7f8c8d;">TBB App A.7 Exercises, p.A-14</span>

<span style="color:#7f8c8d">*（此处为附录习题 A.7.1–A.7.3（Exercises），共 3 题：习题 A.7.1 要求反驳如下陈述——对任何 natural number（自然数）$n$，方程 $4x^2+x-n=0$ 都没有 rational root（有理根）；习题 A.7.2 问：每个大于 2 的素数都是奇数，这一陈述的逆命题是否为真？习题 A.7.3 要求写出断言「每个可微函数都是连续函数」的逆命题（converse）与逆否命题（contrapositive），并追问二者之间是否有区别、是否都为真。按约定跳过不收录。如需练习请读原书；练习时阅读英文原题是必要的学术技能。）*</span>

---

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">A.8 Induction（归纳法）</span>

> <span style="color:#7f8c8d;">TBB App A.8, p.A-14</span>

---

对于前 $n$ 个自然数的和，有一个方便的公式：

```math
1+2+3+\cdots+(n-1)+n=\frac{n(n+1)}{2}
```

对它有一个容易的 direct proof（直接证明），可以进行如下。
令 $S$ 表示这个和，使得

```math
S=1+2+3+\cdots+(n-1)+n
```

或者，按相反的顺序把它表达为

```math
S=n+(n-1)+(n-2)+\cdots+2+1
```

把这两个方程相加，便得到

```math
2S=(n+1)+(n+1)+(n+1)+\cdots+(n+1)+(n+1)
```

从而

```math
2S=n(n+1)
```

<span style="color:#7f8c8d">*（书页 A-14 在此结束：上述推导的最后一步 $2S=n(n+1)$ 在页末中断，原文于书页 A-15 续写，由后续译文承接。）*</span>

<!-- ===== t08 ===== -->

<span style="color:#7f8c8d">书页 A-15 · A.8 归纳法（续）：求和公式直接证明的收尾、“检验数百万个值也不是证明”之辨与归纳法三步骤</span>

---

<span style="color:#7f8c8d">*（书页 A-15 承接 A-14 页末中断的公式：前一页已把和式 $S$ 按两种顺序写出并相加，得出 $2S=n(n+1)$；本页开头接排这一行，给出其等价形式并收束这个 direct proof（直接证明）。A.8 Induction（归纳法）大节始于书页 A-14，其节标题与证明的开头部分见前一页译文。）*</span>

---

```math
\text{or}\quad S=\frac{n(n+1)}{2},
```

这正是我们所要求的 formula（公式）。

---

假如我们当初没能构造出这个证明，情形又会怎样？

在拿不出任何更好的主意时，我们本可以干脆把公式逐个代入检验：取 $n=1$、$n=2$、$n=3$……只要耐心尚存，就一直试下去。

最终，我们要么会撞上一个 counterexample（反例）——那便证明这个 theorem（定理）为假——要么会灵光一现，悟出它究竟为何为真。

实际动手算一算，我们确实发现：

```math
1=\frac{1(1+1)}{2},\qquad 1+2=\frac{2(2+1)}{2},\qquad 1+2+3=\frac{3(3+1)}{2},
```

而且这样的验算还可以持续相当长的一段时间。

在计算机上，我们更可以迅速核查数百万个取值，而每一次都会发现该公式成立。

---

那么，这算得上一个 proof（证明）吗？

倘若一个公式对不计其数的数百万个 $n$ 值都如此灵验，我们又怎能设想它竟然是假的？

假如已经在这么多个不同取值上检验过它，我们当然会有强烈的情感理由去相信这个公式；但这并不构成一个 mathematical proof（数学证明）。

---

作为替代，这里给出一个证明——乍看之下，它似乎不过是把检验多做几遍而已。

姑且假设该公式确实会对某个 $n$ 值失效。

那么，失效必有第一次出现之处，设它发生在某个整数 $N$ 上。

我们知道 $N\neq 1$（因为这一情形早已核查过），于是前一个整数 $N-1$ 所对应的公式依然有效。

真正失效的，是紧接着的下一个整数 $N$。

可一旦我们能证明这种情形永远不会发生——也就是说，绝不会出现「$N-1$ 处公式成立而 $N$ 处公式失效」的局面——我们的公式便证明完毕。

---

举例来说，倘若公式 $1+2+3+\cdots+M=\frac{M(M+1)}{2}$ 成立，那么

```math
1+2+3+\cdots+M+(M+1)=\frac{M(M+1)}{2}+(M+1)=\frac{M(M+1)+2(M+1)}{2}=\frac{(M+1)(M+2)}{2},
```

而这恰好就是 $n=M+1$ 时的正确公式。

由此可见，绝不会出现公式在某一阶段正确、却在下一阶段失效的情形。

于是可知，这个公式永远为真。

这就是一个 proof by induction（归纳法证明）。

---

这种方法可用来尝试证明任何关于整数 $n$ 的 statement（断言）。

步骤如下：

- **第 1 步（Step 1）**：验证该断言对 $n=1$ 成立。
- **第 2 步（Step 2，即 induction step（归纳步骤））**：证明无论何时，只要该断言对任一正整数 $m$ 成立，它就必然对下一个整数 $m+1$ 也成立。
- **第 3 步（Step 3）**：依据 principle of induction（归纳原理）断言该公式对一切 $n$ 成立。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 这三步你在 6.042J 里已经反复演练过：简单归纳、强归纳与自然数的well-ordering（良序性）三者互相等价，本节习题 A.8.8 要求证明的正是其中一对——归纳原理 $\Leftrightarrow$ 良序性。
> 换一种你熟悉的效率视角：归纳证明与recursive algorithm（递归算法）的正确性论证同构——基例对应 base case（基准情形），归纳假设对应「相信递归调用返回的子问题已经解决」，归纳步骤对应合并环节。
> 以merge sort（归并排序）为例：单元素序列天然有序；递归时相信左右两半已各自排好；最后一步把两个有序序列合并成整体有序——与本节对求和公式的论证逐层对应。
> 由此也能看清习题 A.8.9 鸟群谬误的病灶：它相当于一个基例正确、但递归关系有 bug（缺陷）的程序——从 $n=1$ 到 $n=2$ 的一步引用了不存在的「另一只鸟」，递归链在第一环就断裂，却假装对一切 $n$ 成立。
> 书末提示 393 的建议（拿 $n=3$ 单独跑一遍归纳步骤）恰好就是针对这类断裂的单点测试。

---

<span style="color:#7f8c8d">书页 A-16 · A.8 归纳法（续完）：习题引入段与 A.8 Exercises（习题 A.8.1–A.8.9，跳过）</span>

---

在习题中，你将被要求对各种不同的断言给出归纳法证明。

你也不妨试着给出 direct proof（直接证明）——也就是不依赖归纳的证明。

这两种方法，你更偏爱哪一种？

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">A.8 Exercises（习题）</span>

> <span style="color:#7f8c8d;">TBB App A.8 Exercises, p.A-16</span>

<span style="color:#7f8c8d">*（原文此处为 A.8 的 Exercises（习题）栏目，共 9 题（A.8.1–A.8.9）；以下逐题给出灰注说明后按约定跳过，不收录原题与译文。如需练习请读原书；练习时阅读英文原题是必要的学术技能。）*</span>

---

<span style="color:#7f8c8d">*（此处为附录习题 A.8.1（Exercises）：要求用归纳法证明平方和公式——对每个 $n=1,2,3,\ldots$ 有 $1^2+2^2+3^2+\cdots+n^2=n(n+1)(2n+1)/6$；原书题后标注 SEE NOTE 392（指向附录末 Notes（注释）的第 392 条）。按约定跳过不收录。）*</span>

<span style="color:#7f8c8d">*（此处为附录习题 A.8.2（Exercises）：涉及前 $n$ 个奇数之和——先对 $n=1,2,3,4,5$ 计算 $1+3+5+\cdots+(2n-1)$ 的值，这些值应当足以让人猜出正确的公式（正是 $n^2$），随后再用归纳法加以验证。按约定跳过不收录。）*</span>

<span style="color:#7f8c8d">*（此处为附录习题 A.8.3（Exercises）：涉及整除性——要求用归纳法证明对每个 $n=1,2,3,\ldots$，数 $7^n-4^n$ 都可被 3 整除（divisible by 3）。按约定跳过不收录。）*</span>

<span style="color:#7f8c8d">*（此处为附录习题 A.8.4（Exercises）：即 Bernoulli inequality（Bernoulli 不等式）——要求用归纳法证明对每个 $n=1,2,3,\ldots$ 及任意 $x>0$ 都有 $(1+x)^n\ge 1+nx$。按约定跳过不收录。）*</span>

<span style="color:#7f8c8d">*（此处为附录习题 A.8.5（Exercises）：涉及 geometric series（几何级数）的部分和——要求用归纳法证明对每个 $n=1,2,3,\ldots$ 及任意实数 $r\neq 1$ 都有 $1+r+r^2+\cdots+r^n=(1-r^{n+1})/(1-r)$。按约定跳过不收录。）*</span>

<span style="color:#7f8c8d">*（此处为附录习题 A.8.6（Exercises）：即立方和公式——要求用归纳法证明对每个 $n=1,2,3,\ldots$ 有 $1^3+2^3+3^3+\cdots+n^3=(1+2+3+\cdots+n)^2$。按约定跳过不收录。）*</span>

<span style="color:#7f8c8d">*（此处为附录习题 A.8.7（Exercises）：涉及高阶导数——要求用归纳法证明对每个 $n=1,2,3,\ldots$ 有 $\frac{d^n(e^{2x})}{dx^n}=e^{2x+n\log 2}$，即 $e^{2x}$ 的 $n$ 阶导数（derivative）为 $2^n e^{2x}$，合并成单一指数便得原式。按约定跳过不收录。）*</span>

<span style="color:#7f8c8d">*（此处为附录习题 A.8.8（Exercises）：要求证明下面两个原理彼此等价（即假设其中任一个成立，证明另一个）——其一为归纳原理：设 $S\subset\mathbb{N}$ 满足 $1\in S$，且对一切整数 $n$，只要 $n\in S$ 便有 $n+1\in S$，则 $S=\mathbb{N}$；其二为 well ordering of $\mathbb{N}$（自然数的良序性，原书页边标注的关键词）——若 $S\subset\mathbb{N}$ 且 $S\neq\emptyset$，则 $S$ 有第一个元素（即 minimal element（极小元））。按约定跳过不收录。）*</span>

<span style="color:#7f8c8d">*（此处为附录习题 A.8.9（Exercises）：要求批判下面这个“证明”——标题为 "Birds of a feather flock together"（物以类聚）：断言任何 $n$ 只鸟构成的集合必全体同种；题给论证走归纳路线——$n=1$ 时显然成立；假设对某个 $n$ 成立，取 $n+1$ 只鸟，先取出一只握在手中，余下 $n$ 只依 induction hypothesis（归纳假设）同种；再从余下的鸟中取出另一只、与手中那只对调，于是手中之鸟便置身于一个由 $n$ 只鸟组成的集合之中，故亦必同种，从而推得 $n+1$ 只鸟全体同种。此题的陷阱在于：从 $n=1$ 到 $n=2$ 的一步中并无“另一只”可换，归纳步骤并非对一切 $n$ 通行。本题自本页起，至书页 A-17 结束，原书在此题末尾标注 SEE NOTE 393。按约定跳过不收录。）*</span>

---

<span style="color:#7f8c8d">*（书页 A-16 在此结束：习题 A.8.9 的题给“证明”在页末一句处中断，下接书页 A-17 续写至该题结束；随后原文进入 A.9 Quantifiers（量词）一节，由后续译文接续。）*</span>

<!-- ===== t09 ===== -->

<span style="color:#7f8c8d">书页 A-17 · A.8.9 习题收尾（“鸟群同种”谬误）与 A.9 Quantifiers 开篇</span>

> <span style="color:#7f8c8d">*（此处为附录习题 A.8.9（Exercises）的最后一段：该题给出“任何一群鸟必属同一物种”这一谬误命题的归纳式“证明”之收尾——取出一只鸟、再放回手中的那只；由于他此刻面对的是 $n$ 只鸟的群体，这只鸟必与它们同种；于是 $n+1$ 只鸟的群体中所有鸟都属同一物种，命题“由归纳法证毕”。此“证明”的漏洞在于归纳步骤中对“群体”的偷换，书末注释 393（SEE NOTE 393）对此谬误有专门批判。习题内容按约定跳过不收录；如需练习请读原书，练习时阅读英文原题是必要的学术技能。）*</span>

---

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">A.9 Quantifiers（量词）</span>

> <span style="color:#7f8c8d;">TBB App A.9, p.A-17</span>

在全部数学之中，当然更在全部analysis（分析学）之中，你会一再遇到以下两个反复出现的短语：

「对所有……，……为真」（For all . . . it is true that . . .）

以及

「存在一个……，使得……为真」（There exists a . . . so that it is true that . . .）

例如，公式 $(x+1)^2=x^2+2x+1$ 对所有实数 $x$ 都为真。

又存在实数 $x$ 使得 $x^2+2x+1=0$（事实上取 $x=-1$ 即可）。

有一种符号化的书写方式来表达这类陈述，是极为有用的。

无论使用何种语言，数学家们都普遍用符号 $\forall$ 表示“对所有”或“对每一个”，用 $\exists$ 表示“存在”。

当初选中这两个符号，只是因为对排字工人来说，把字母 “A” 与 “E” 侧转或上下颠倒过来并不费事。

逻辑学家把它们称为quantifier（量词），因为它们（粗略地）回答了“有多少？”这一问题。

> <span style="color:#1e8449">**[note]**</span> 译者注：$\forall$ 称为universal quantifier（全称量词），$\exists$ 称为existential quantifier（存在量词）。这两个名字回答的是「有多少个 $x$ 使命题成立」：全称量词答「所有」，存在量词答「至少一个」。作者在这里讲了一个很朴素的来历——排字工人把字母 A 倒转得 $\forall$（for All）、把 E 左右颠倒得 $\exists$（Exists）——这与 6.042J 逻辑章节的量词记号完全一致；你在那里学过的否定交换律（$\neg\forall$ 变 $\exists$、$\neg\exists$ 变 $\forall$）将在下一页正文中正式登场。

对多少个 $x$ 而言，$(x+1)^2=x^2+2x+1$ 是真的？答案是“对所有实数 $x$”。用符号写出，就是

```math
\forall x\in\mathbb{R},\ (x+1)^2=x^2+2x+1.
```

对多少个 $x$ 而言，$x^2+2x+1=0$ 是真的？

并不多，但确实存在一些数 $x$ 使它为真。用符号写出，就是

```math
\exists x\in\mathbb{R},\ x^2+2x+1=0.
```

无论这类陈述是用 $\forall$ 与 $\exists$ 作符号表达，还是只用“对所有”与“存在”这样的文字短语，熟悉含有一个或多个量词的陈述都极其重要。

本节习题提供了一些练习。

无论如何，等你深入修读一门分析课程之后，你必定会对此熟悉得多。

---

### <span style="color:#2471a3;">**[section]**</span> Negations of Quantified Statements（量词陈述的否定）

> <span style="color:#7f8c8d;">TBB App A.9, p.A-17</span>

这里有一条实用提示，有助于构造含量词的assertion（断言）的否定形式。

从某种意义上说，两个量词 $\forall$ 与 $\exists$ 是互补的。

命题“所有鸟都会飞”的否定，按日常语言来说就是“有些鸟不会飞”。

更正式地说，对如下陈述

> 对所有鸟 $b$，$b$ 会飞

它的否定应当是

<span style="color:#7f8c8d">书页 A-18 · 量词否定法则收尾与 A.9 习题</span>

> 存在一只鸟 $b$，$b$ 不会飞。

用符号来写，设 $B$ 为所有鸟构成的集合。

那么，这里的形式是

```math
\forall b\in B,\ \text{"statement about } b \text{" is true}
```

而它的否定是

```math
\exists b\in B,\ \text{"statement about } b \text{" is not true.}
```

由此得到一个构造否定式的简便法则。

含 $\forall$ 的陈述，其否定就是把 $\forall$ 换成 $\exists$ 后所得的陈述；

含 $\exists$ 的陈述，其否定就是把 $\exists$ 换成 $\forall$ 后所得的陈述。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 这条法则你在 6.042J 的逻辑章节见过它的标准形式：$\neg(\forall x,\ P(x))=\exists x,\ \neg P(x)$ 与 $\neg(\exists x,\ P(x))=\forall x,\ \neg P(x)$，与本节的「换量词」操作逐字对应。
> 有意思的是，本附录内部也借此形成一道闭环。
> 附录 A.2.1 的 De Morgan 律（德摩根律）$\overline{A\cup B}=\bar A\cap\bar B$ 可以看作量词否定在集合语言中的投影——「$x$ 不属于 $A\cup B$」就是说「既不属于 $A$ 也不属于 $B$」：「或」在否定下变「且」，正如「存在」在否定下变「所有」。
> 反向同理：$\overline{A\cap B}=\bar A\cup\bar B$ 恰对应 $\neg\forall=\exists\neg$。
> 落到编程里，这组法则就是loop invariant（循环不变式）与assertion（断言）的否定书写方式：当程序断言「对所有下标 $i$ 都有 $a[i]>0$」而失败时，调试器递到你手里的正是一个witness（见证元素）——某个满足 $a[i]\le 0$ 的下标。
> 把 $\forall$ 循环的否定写成 $\exists$ 搜索，你就在 A.7 的意义上亲手构造了一个反例。

举一个复杂的例子：

即使不给 $A$、$B$、$C$ 及字母 $a$、$b$、$c$ 赋予任何具体含义，陈述

```math
\exists a\in A,\ \forall b\in B,\ \forall c\in C,\ \text{"statement about } a,\ b \text{ and } c\text{" is true}
```

的否定是什么？它应当是

```math
\forall a\in A,\ \exists b\in B,\ \exists c\in C,\ \text{"statement about } a,\ b \text{ and } c\text{" is not true.}
```

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">A.9 Exercises（习题）</span>

> <span style="color:#7f8c8d;">TBB App A.9, p.A-18</span>

<span style="color:#7f8c8d">*（此处为附录习题 A.9.1–A.9.4（Exercises），共 4 题，按约定跳过不收录；各题主题如下。如需练习请读原书，练习时阅读英文原题是必要的学术技能。）*</span>

> <span style="color:#7f8c8d">**A.9.1**（主题：量词陈述的判真判假）设 $\mathbb{R}$ 为通常的全体实数之集，要求用文字说出七个量词陈述 (a)–(g) 各自的含义，并判断它们是否为真；不要求给出证明，只须就含义与有效性作出判断。七条覆盖 $\forall$、$\exists$ 的单独使用与嵌套搭配，其中 (e) 为 $\forall x\,\exists y$ 型、(f) 为 $\exists x\,\forall y$ 型，二者构成量词次序的对比。</span>

> <span style="color:#7f8c8d">**A.9.2**（主题：量词陈述的否定）写出上一题中各陈述的否定；若你此前判定某陈述为真（假），此刻自然应当同意其否定为假（真）。</span>

> <span style="color:#7f8c8d">**A.9.3**（主题：量词断言的证明与反驳）说明为证明 $\forall s\in S$“关于 $s$ 的陈述”为真、以及 $\exists s\in S$“关于 $s$ 的陈述”为真这两类断言，各须完成什么；再分别说明要反驳（disprove）这两类断言又各须做什么。</span>

> <span style="color:#7f8c8d">**A.9.4**（主题：定义域为空集的情形）在上一题中改设 $S=\emptyset$：此时两个断言还可能为真吗？还必定为真吗？（原书页边附有同样的追问。）</span>

<!-- ===== t10 ===== -->

<span style="color:#7f8c8d">书页 A-19 · 附录 A Notes（注释）习题提示 387–393</span>

---

<span style="color:#7f8c8d">*（附录 A.9 的全部习题 A.9.1–A.9.4 均已在前一文件（书页 A-18）以灰注处理完毕；书页 A-19 自页首即为本附录的 Notes（注释）栏目，以下为提示 387–393 的逐条灰色摘要。如需练习请读原书；练习时阅读英文原题是必要的学术技能。）*</span>

---

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Notes（注释）</span>

> <span style="color:#7f8c8d;">TBB App A, p.A-19</span>

---

<span style="color:#7f8c8d">*（原文此处的 Notes（注释）栏目收录附录全部习题的解答提示（hints），编号 387–393，与附录各习题之后标注的 SEE NOTE 387–393 一一对应；按约定不逐句翻译，以下逐条给出灰色摘要。）*</span>

---

<span style="color:#7f8c8d">提示 387（题 A.2.4）：针对 (c) 与 (d)：并非每个数都有唯一的十进制展开（decimal expansion），例如 $\frac{1}{2}$ 既可以写成 $0.5000000\ldots$，也可以写成 $0.499999999\ldots$。针对 (e)：提示取定义域（domain）为集合 $\mathbb{N}$ 即可。末尾还发问：当 $x$ 非常大时，谁也不知道该如何判定 $x$ 是不是素数（prime number）——这一事实是否会让人感到困扰（有些人可能会）？</span>

---

<span style="color:#7f8c8d">提示 388（题 A.2.13）：本题为一项研究项目（project）：请读者自行调研 Russell's paradox（罗素悖论）这一主题。该悖论以 Bertrand Russell（伯特兰·罗素，1872-1969）命名——他在集合论创立初期发现了这一悖论，并由此引发了一场危机（crisis）。（原书所印生年 1872-1969 有误，Russell 实际在世年代为 1872–1970，此处按原书照录。）</span>

---

<span style="color:#7f8c8d">提示 389（题 A.5.1）：假设结论不成立，于是 $\sqrt{2}$ 是有理数（rational number），即 $\sqrt{2}=m/n$，其中 $m$ 与 $n$ 不全为偶数。两边平方得 $2n^2=m^2$，再沿这条线索继续推演，直到能够证明 $m$ 与 $n$ 其实都是偶数——这便与假设构成矛盾，证明随之完成。</span>

---

<span style="color:#7f8c8d">提示 390（题 A.5.2）：假设不然，那么就可以把全部素数（prime number）列成 $2,3,5,7,11,13,\ldots,P$，其中 $P$ 是最后一个素数。考虑数 $1+(2\times3\times5\times7\times11\times\cdots\times P)$，由此导出矛盾，证明即告完成。（此处要做到完全严谨，还需用到素因子分解定理：每个数都可以写成若干素数的乘积。）这就是一则早在古希腊便已闻名的著名证明（通常归于 Euclid（欧几里得）名下）。</span>

---

<span style="color:#7f8c8d">提示 391（题 A.6.1）：先写出逆否命题（contrapositive）：若 $x+r$ 并非对所有有理数 $r$ 都是无理数（irrational number），则 $x$ 不是无理数。再把这句话翻译成等价的正面表述：若对某个有理数 $r$ 而言 $x+r$ 是有理数，则 $x$ 是有理数。到了这一步，该命题便很容易证明了。</span>

---

<span style="color:#7f8c8d">提示 392（题 A.8.1）：先检验 $n=1$ 的情形。随后假设 $1^2+2^2+3^2+\cdots+n^2=\frac{n(n+1)(2n+1)}{6}$ 对某个固定的 $n$ 成立，并利用这一假设（在这类证明中称为 induction hypothesis（归纳假设））设法求出 $1^2+2^2+3^2+\cdots+n^2+(n+1)^2$ 的表达式。它应当恰好化成前 $n+1$ 个平方数之和的正确公式。之后便可依归纳法（induction）宣称：该公式已对一切 $n$ 得证。</span>

---

<span style="color:#7f8c8d">提示 393（题 A.8.9）：归纳步骤（induction step）要求我们证明：若该断言对 $n$ 为真，则它对 $n+1$ 也为真。这一步必须在 $n=1$ 时成立、在 $n=2$ 时成立、在 $n=3$ 时成立……一言以蔽之，必须对一切 $n$ 都成立。就 $n=3$ 检验这个归纳步骤，你会发现它确实行得通，并无漏洞；那么，它对所有的 $n$ 都行得通吗？</span>

---

<span style="color:#1e8449;">**[note]**</span> <span style="color:#1e8449">译者按：提示 393 的弦外之音值得点破——A.8.9 那个「物以类聚」的归纳论证，其归纳步骤在 $n=1$（即从 1 只鸟推到 2 只鸟）处失效，因为此时并无「另一只」可供交换；而 $n=3$ 处的步骤却无懈可击。这正是「归纳步骤必须对一切 $n$ 成立」这一要求的深意：一个反例便足以推翻整个「证明」。若把归纳证明比作一段对每个 $n$ 都须正确执行的程序，那么 A.8.9 的病灶就是「代码路径在 $n=1$ 处引用了不存在的变量」——与你在 CSAPP 中调试非法内存访问时遇到的症状同构；而提示 393 建议「拿 $n=3$ 单独跑一遍」正是unit test（单点测试）的思路，专门去击穿那个最可能藏着 bug 的环节。</span>

---

<span style="color:#7f8c8d">*（以上为附录 A 全部 Notes 提示；本卷自此进入 Subject Index（主题索引）区。）*</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span>
> 提示 388 请你调研的 Russell's paradox（罗素悖论）有一条值得记住的时间线：Russell（罗素）于 1901 年发现悖论，1902 年写信告知 Frege（弗雷格），恰逢其《算术基本定律》（Grundgesetze der Arithmetik）第二卷付印——弗雷格随后在该卷附录里承认，这一发现动摇了他毕生工作的基石。
> 悖论的结构可以用你已掌握的集合语言两句话讲清：令 $R=\{x\mid x\notin x\}$，问 $R$ 是否属于 $R$——若属于则按定义不属于，若不属于则按定义属于，两头矛盾。
> 流传更广的理发师版本与此同构：「给且只给所有不给自己刮脸的人刮脸」的理发师，给不给自己刮脸？
> 而提示 390 的素数无穷证明可溯源至 Euclid（欧几里得）：约公元前 300 年的《几何原本》卷九命题 20 指出素数多于任何给定的有限多个素数——后世常以反证法转述它，两千三百年来一直是范本。
> 🎥 *Colding 在 V03 讲座中演示了反证法的开场——先假设结论的否定："So assume that alpha squared is strictly less than 2. … we will show this by contradiction."（翻译：所以假设 $\alpha^2$ 严格小于 2……我们将用反证法来证明这一点。）*
> 这与欧几里得假设「素数已列尽」是同一个动作：反证法的起点，永远是先替将被推翻的那一方把话说满。

<!-- ===== t99 ===== -->

<span style="color:#7f8c8d">书页 A-20 · SUBJECT INDEX（主题索引区开始）</span>

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Subject Index（主题索引）</span>

<span style="color:#7f8c8d">书页 A-20 至 A-29（本卷 PDF 末 10 页）为全书 Subject Index（主题索引），按英文字母序列出全书术语词条及其所在书页页码，如 Baire category theorem（Baire 纲定理），245, 617；Cantor set（Cantor 集），249–252, 255, 257, 291, 625；Bolzano-Weierstrass theorem（Bolzano-Weierstrass 定理），56, 447, 598, 602 等。索引属检索工具页，无叙事内容，按约定整块跳过、不翻译。</span>

<span style="color:#7f8c8d">*（提示：使用本双语版阅读全书时，若需检索某术语，可在各卷 .bilingual.md 文件内搜索该术语的中文译名或英文原词；索引中的页码均指原书书页，各卷卷首均标有「书页 = PDF 页 + N」换算式。）*</span>

---

<span style="color:#7f8c8d">书页 A-29 · 本卷（Part014）与全书翻译至此结束。</span>
