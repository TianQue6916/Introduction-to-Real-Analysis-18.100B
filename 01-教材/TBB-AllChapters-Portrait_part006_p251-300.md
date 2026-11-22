# <span style="color:#c0392b;">Elementary Real Analysis（初等实分析）</span>

> <span style="color:#7f8c8d;">行内双语翻译 · Part006（书页 239–284）</span>
> <span style="color:#7f8c8d;">范围：第 6 章 More on Continuous Functions and Sets（连续函数与集合的更多内容）全书正文 + 第 7 章 Differentiation（微分）§7.1–§7.3</span>
> <span style="color:#7f8c8d;">源文件：TBB-AllChapters-Portrait_part006_p251-300.pdf（书页 = PDF 页 + 234）</span>
> <span style="color:#7f8c8d;">Second Edition (2008) · Brian S. Thomson, Judith B. Bruckner, Andrew M. Bruckner</span>
> <span style="color:#7f8c8d;">**格式：** 中文主体 + `English term（中文翻译）` 嵌入 · 深红标题 · 蓝色标签 · fenced math block · 无英文原句</span>
> <span style="color:#7f8c8d;">**习题区**（各节 Exercises、6.9 Challenging Problems、Notes 提示区、第 5 章习题提示区 p.235–238）按约定跳过不收录</span>

---

## <span style="color:#c0392b;">Chapter 6. More on Continuous Functions and Sets（第 6 章 连续函数与集合的更多内容）</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 原书在本章开头注明：本章可视作充实材料（enrichment material），包含若干更高级的主题，可以整体跳过，不影响后续导数与积分的学习。但本章内容（Baire 纲定理、Cantor 集、Borel 集、振幅与连续性、零测集）正是测度论与函数论的前奏，建议精读。

<!-- ===== 书页 239（PDF 页 5）===== -->
---
<span style="color:#7f8c8d">*Part006 · 书页 239 行内双语翻译*</span>

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Chapter 6. More on Continuous Functions and Sets（连续函数与集合的更多内容）</span>

本章可视为扩充性材料（enrichment material），其中还包含若干更深入的主题，因而可以整体跳过。你可以直接进入导数（derivative）与积分（integral）的学习，而不会在材料的连续性上产生任何损失。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">6.1 Introduction（引言）</span>

在本章中，我们将对连续函数的分析进行更深入的研究。为此，我们需要一些新的集合论（set theoretic）思想与方法。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">6.2 Dense Sets（稠密集）</span>

<span style="color:#7f8c8d">（本节复习第 1.9 节的内容。）</span>

考虑有理数（rational number）集合 $\mathbb{Q}$，并设 $(a, b)$ 为 $\mathbb{R}$ 中的一个开区间（open interval）。我们如何证明区间 $(a, b)$ 中存在 $\mathbb{Q}$ 的元素，即 $(a, b) \cap \mathbb{Q} \neq \emptyset$？

首先假设 $0 < a$。由于 $b - a > 0$，阿基米德性质（Archimedean property，定理 1.11）蕴含存在一个正整数 $q$ 使得

```math
q(b - a) > 1.
```

于是

```math
qb > 1 + qa.
```

阿基米德性质还蕴含整数集合 $\{m \in \mathbb{N} : m > qa\}$ 是非空的。因此，根据良序原理（well-ordering principle），该集合中存在一个最小的整数 $p$，并且对于这个 $p$，成立 $p - 1 \le qa < p$。由此可得

```math
qa < p \le 1 + qa < qb,
```

这蕴含

```math
a < \frac{p}{q} < b.
```

我们已证明，在假设 $a > 0$ 之下，区间 $(a, b)$ 中存在一个有理数 $r = p/q$。

在假设 $a < 0$ 之下同样成立。为见此，首先注意到若 $a < 0 < b$，则可取 $r = 0$。若 $a < b < 0$，则 $0 < -b < -a$，于是上一段的论证表明存在 $r \in \mathbb{Q}$ 使得 $-b < r < -a$。
---
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 你已在 6.042J 中学过有理数集 $\mathbb{Q}$ 是可数的——存在一个从 $\mathbb{N}$ 到 $\mathbb{Q}$ 的双射，即可以把所有有理数排成 $q_1, q_2, q_3, \ldots$ 的序列。但这只说明了 $\mathbb{Q}$ 的基数特征；稠密性则是拓扑特征——每个开区间无论多短都含有有理数。这两个性质彼此独立：有限集不稠密、无理数集不可数也稠密。值得追问的是：是否存在可数却不稠密的集合？自然数 $\mathbb{N}$ 就是。是否存在不可数却无处稠密的集合？这正是 Cantor 集（6.5 节）。把这两个维度交叉，可以构成一个 2×2 的表：{可数/不可数} × {稠密/无处稠密}，除"不可数且无处稠密"之外的三格你都能立即举出例子——Cantor 集恰好填上最后的缺口。

---
---

---
<!-- ===== 书页 240（PDF 页 6）===== -->
---
<span style="color:#7f8c8d">*Part006 · 书页 240 行内双语翻译*</span>

在此情形下 $a < -r < b$。

上述讨论证明了每个开区间都含有一个有理数。我们常常用「有理数集合是稠密集（dense set）」这一说法来表达这个事实。

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">Definition 6.1（定义 6.1）</span>

> <span style="color:#7f8c8d;">TBB §6.2, p.240</span>

<span style="color:#00838f">若对于每个开区间 $(a, b)$，集合 $A \cap (a, b)$ 均非空，则称实数集合 $A$ 在 $\mathbb{R}$ 中稠密（dense）。</span>

重要的是要引入一个更一般的概念，即集合 $A$ 在集合 $B$ 中稠密（dense in $B$）这一概念。

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">Definition 6.2（定义 6.2）</span>

> <span style="color:#7f8c8d;">TBB §6.2, p.240</span>

<span style="color:#00838f">设 $A$ 与 $B$ 是 $\mathbb{R}$ 的子集。若每个与 $B$ 相交的开区间也与 $A$ 相交，则称 $A$ 在 $B$ 中稠密。</span>

因此，定义 6.1 所陈述的正是定义 6.2 中当 $B = \mathbb{R}$ 时出现的特殊情形。我们应当指出，某些作者在其定义 6.2 的版本中要求 $A \subset B$。我们发现不施加这一限制更为方便。因此，例如在我们的表述中，$\mathbb{Q}$ 在 $\mathbb{R} \setminus \mathbb{Q}$ 中稠密。

容易验证，$A$ 在 $B$ 中稠密当且仅当 $\overline{A} \supset B$（习题 6.2.1）。

<span style="color:#7f8c8d">（按：原文此句的闭包上划线在文本提取时丢失——$\overline{A}$ 误作 $A$——此处按数学意义补正。）</span>

<span style="color:#7f8c8d">（习题 6.2.1–6.2.8 为习题区，按约定跳过，不收录。）</span>

---

---
<!-- ===== 书页 241（PDF 页 7）===== -->
---
<span style="color:#7f8c8d">*Part006 · 书页 241 行内双语翻译*</span>

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">6.3 Nowhere Dense Sets（无处稠密集）</span>

我们不妨把在 $\mathbb{R}$ 中稠密（dense）的集合 $A$ 视为某种意义下「很大」的集合：在每个区间内部，无论区间多么小，都能找到 $A$ 中的点。

与此相反的极端情形是：如果一个集合根本不在任何区间中稠密，就说它是 nowhere dense（无处稠密）的，因而在某种意义上它是「很小」的。

下面就是这个重要的「小」概念的精确定义。

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">Definition 6.3（定义 6.3）</span>

> <span style="color:#7f8c8d;">TBB §6.3, p.241</span>

> 集合 $A \subset \mathbb{R}$ 称为在 $\mathbb{R}$ 中无处稠密，是指每个开区间 $I$ 都包含一个开子区间 $J$，使得 $A \cap J = \emptyset$。

我们还可以换一种方式表述：$A$ 无处稠密，当且仅当 $A$ 不包含任何开区间（参见习题 6.3.4）。

<span style="color:#2471a3;">**[example]**</span> **Example 6.4（例 6.4）**

> <span style="color:#7f8c8d;">TBB §6.3, p.241</span>

构造无处稠密集的例子是很容易的：

1. 任何有限集；
2. $\mathbb{N}$；
3. $\{1/n : n \in \mathbb{N}\}$。

这些集合每一个都是无处稠密的，读者可以自行验证。

例 6.4 中的每一个集合都是 countable（可数的），因而在基数的意义下也是「小」的。

我们很难想象一个无处稠密的 uncountable（不可数）集合，但正如将在 6.5 节看到的，这样的集合确实存在。

我们再建立一条简单的结果，说明任意有限个无处稠密集的并集仍然是无处稠密的。

「可数个无处稠密集的并集仍然是无处稠密的」这一命题并不成立。

事实上，可数个无处稠密集的并集在我们后续的研究中将扮演重要角色。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 6.5（定理 6.5）</span>

> <span style="color:#7f8c8d;">TBB §6.3, p.241</span>

设 $A_1, A_2, \ldots, A_n$ 在 $\mathbb{R}$ 中无处稠密，则 $A_1 \cup \cdots \cup A_n$ 也在 $\mathbb{R}$ 中无处稠密。

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 设 $I$ 是 $\mathbb{R}$ 中的任意开区间，我们要找一个开区间 $J \subset I$，使得对 $i = 1, 2, \ldots, n$ 都有 $J \cap A_i = \emptyset$。
>
> 由于 $A_1$ 无处稠密，所以存在开区间 $I_1 \subset I$，使得 $I_1 \cap A_1 = \emptyset$。
>
> 又因 $A_2$ 也在 $\mathbb{R}$ 中无处稠密，所以存在开区间 $I_2 \subset I_1$，使得 $A_2 \cap I_2 = \emptyset$。
>
> 如此继续下去，我们得到一列开区间 $I_1 \supset I_2 \supset I_3 \supset \cdots \supset I_n$。

<!-- XREF: Example 6.4 → §6.3 p.241 -->
---
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> "nowhere dense（无处稠密）"这个术语容易引起误解：它不是说"这个集合不在任何地方稠密"——从字面上看，$\mathbb{Q}$ 也不在区间 $[2,3]$ 中稠密，但 $\mathbb{Q}$ 显然不满足定义 6.3。正确的理解是：$A$ 无处稠密，当且仅当 $\overline{A}$（$A$ 的闭包）不包含任何开区间——即哪怕你把 $A$ 的极限点全部收纳进来，也填不满任何一个（任意短的）开区间。等价表述（习题 6.3.4）：$\overline{A}$ 的内部是空集。这里涉及你已熟悉的闭包和内部运算：闭包是把极限点"收进来"，内部是"最大的开子集"。无处稠密就是说，经过"收极限点"这道工序之后，$A$ 依然撑不起任何区间。回到 6.042J 的直觉：与稠密集在每个区间都有"代表"相反，无处稠密集在每个区间都有一个"空白子区间"。

---
---

---
<!-- ===== 书页 242（PDF 页 8）===== -->
---
<span style="color:#7f8c8d">*Part006 · 书页 242 行内双语翻译*</span>

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明，续 Theorem 6.5）.*

> 这列开区间满足对 $i = 1, \ldots, n$ 有 $A_i \cap I_i = \emptyset$。
>
> 由于对 $i = 1, \ldots, n$ 均有 $I_n \subset I_i$，由此可推出对 $i = 1, \ldots, n$ 有 $A_i \cap I_n = \emptyset$。
>
> 于是

> ```math
> \left(\bigcup_{i=1}^{n} A_i\right) \cap I_n
> = \bigcup_{i=1}^{n} (A_i \cap I_n)
> = \bigcup_{i=1}^{n} \emptyset
> = \emptyset,
> ```

> 这正是所要证明的（as was to be proved）。

<span style="color:#7f8c8d">*（本页其余部分为 6.3 节习题区 Exercises 6.3.1–6.3.8，按约定跳过。）*</span>
---

---
<!-- ===== 书页 243（PDF 页 9）===== -->
---
<span style="color:#7f8c8d">*Part006 · 书页 243 行内双语翻译*</span>

（本页为书页 243，正文为 6.4 节 The Baire Category Theorem。）

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">6.4 The Baire Category Theorem（Baire 纲定理）</span>

> *标注：Advanced section（高级节），可略过。*

在本节中，我们将建立 Baire category theorem（Baire 纲定理），它给出了无处稠密集可被视为「小」的一种确切含义：一列无处稠密集的并集无法填满一个区间。若我们将 Cantor 定理（Theorem 2.4）解释为断言「一列有限集的并集无法填满一个区间」，那么我们便会把 Baire 纲定理看作一个意义深远的推广。

我们通过一个源于 Stefan Banach（巴拿赫，1892–1945）与 Stanislaw Mazur（马祖尔，1905–1981）的博弈思想来引出这个重要定理。虽然该定理的起源应归功于 René Baire——定理即以他命名——但博弈方法有助于我们看清 Baire 纲定理为何可能是真的。这个 Banach-Mazur game（Banach–Mazur 博弈）只是贯穿整个数学、用来发展有趣概念的众多数学博弈之一。

### <span style="color:#2471a3;">**[subsection]**</span> <span style="color:#c0392b">6.4.1 A Two-Player Game（双人博弈）</span>

> *标注：Advanced section（高级节），可略过。*

我们通过两个玩家 (A) 与 (B) 之间的博弈来引入 Baire 纲定理。

玩家 (A) 被给予 $\mathbb{R}$ 的一个子集 $A$，而玩家 (B) 被给予补集（complement）$B = \mathbb{R} \setminus A$。玩家 (A) 首先选择一个闭区间 $I_1 \subset \mathbb{R}$；随后玩家 (B) 选择一个闭区间 $I_2 \subset I_1$。玩家轮流行动，每一步行动都是在先前选定的区间内部选择一个闭区间。

因此，博弈的进行决定了一个闭区间的下降序列（descending sequence）
```math
I_1 \supset I_2 \supset I_3 \supset \cdots \supset I_n \supset \cdots
```
其中玩家 (A) 选择奇数指标的区间，玩家 (B) 选择偶数指标的区间。若
```math
A \cap \bigcap_{n=1}^{\infty} I_n \neq \varnothing ,
```
则玩家 (A) 获胜；否则玩家 (B) 获胜。

玩家 (A) 的目标显然是确保交集含有 $A$ 中的一点；玩家 (B) 的目标则是确保交集为空或只含有 $B$ 中的点。我们预期：若他的集合 $A$ 很大，玩家 (A) 就应获胜；若他的集合很大，玩家 (B) 就应获胜。然而，对于这个博弈而言，「大」究竟意味着什么，并非一目了然。

<span style="color:#2471a3;">**[example]**</span> **Example 6.6（例 6.6）**

> <span style="color:#7f8c8d;">TBB §6.4, p.243</span>

> 若分配给玩家 (A) 的集合 $A$ 含有一个开区间 $J$，则 (A) 应选择任一满足 $I_1 \subset J$ 的区间。无论博弈如何继续，玩家 (A) 都会获胜。换一种说法：若分配给玩家 (B) 的集合不是稠密的，则他会输。

<span style="color:#2471a3;">**[example]**</span> **Example 6.7（例 6.7）**

> <span style="color:#7f8c8d;">TBB §6.4, p.243</span>

> 为得到一个更有趣的例子，设玩家 (A) 拿到「大」集合——所有无理数，于是玩家 (B) 拿到有理数。（现在两位玩家都拿到了稠密集。）设 $A$ 由无理数组成。玩家 (A) 可按下述策略获胜。令 $q_1, q_2, q_3, \ldots$ 为所有有理数的一个列举，即 $Q = \{q_1, q_2, q_3, \ldots\}$。（未完，接下页）

---
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Banach–Mazur 博弈的思想可以命名为**「区间嵌套博弈法」**。核心策略是：玩家 (A) 若想确保交集捕获 $A$ 中的点，必须在第 $n$ 轮选区间时"前瞻性地"避开前 $n$ 个"障碍"——这正是 Example 6.7 中对付有理数枚举 $\{q_1, q_2, \ldots\}$ 的手法。这一策略的本质类似于你已在 6.042J 中熟悉的**对角线论证**：对方给出一列"威胁"（可数个），你每一步都确保当前选择避开有限个威胁，最终取交集即可避开全部可数个威胁。差异在于，对角线论证通常用于构造一个"不在列表中"的对象，而这里用的是嵌套闭区间的紧性（nested interval property）来保证交集非空——这个推理链条是实数的 completeness（完备性）的体现，也是 Baire 纲定理证明的核心引擎。

---
---

---
<!-- ===== 书页 244（PDF 页 10）===== -->
---
<span style="color:#7f8c8d">*Part006 · 书页 243 行内双语翻译*</span>

（本页为书页 244，接续 Example 6.7 与 6.4.2 节。）

<span style="color:#2471a3;">**[example]**</span> **Example 6.7（续，例 6.7）**

> <span style="color:#7f8c8d;">TBB §6.4, p.244</span>

> （接前页）即 $B$ 为所有有理数 $\mathbb{Q} = \{q_1, q_2, q_3, \ldots\}$。玩家 (A) 选择第一个区间 $I_1$ 为任意满足 $q_1 \notin I_1$ 的闭区间。归纳地假设 $I_1, I_2, \ldots, I_{2n}$ 已按博弈规则选出，现在轮到玩家 (A) 选择 $I_{2n+1}$。集合 $\{q_1, q_2, \ldots, q_n\}$ 是有限的，故存在闭区间 $I_{2n+1} \subset I_{2n}$ 使得
> ```math
> I_{2n+1} \cap \{q_1, q_2, \ldots, q_n\} = \varnothing .
> ```
> 玩家 (A) 就选择这样的区间。由于对每个 $n \in \mathbb{N}$ 都有 $q_n \notin I_{2n+1}$，集合 $\bigcap_{n=1}^{\infty} I_n$ 不含任何有理数；但作为闭区间的下降序列，$\bigcap_{n=1}^{\infty} I_n \neq \varnothing$。于是 $A \cap \bigcap_{n=1}^{\infty} I_n \neq \varnothing$，玩家 (A) 获胜。

在这两个例子中，用非正式的语言说，玩家 (A) 拥有获胜策略：无论玩家 (B) 如何行动，玩家 (A) 都能「回应」每一步并赢得博弈。

在两个例子中，玩家 (A) 都有明显的优势：集合 $A$ 比集合 $B$ 更大。但它究竟在哪一意义下更大？这里起作用的并非「$A$ 不可数而 $B$ 可数」这一事实。而是别的什么：关键在于，给定区间 $I_{2n}$，玩家 (A) 可以在 $I_{2n}$ 内选择 $I_{2n+1}$，使得 $I_{2n+1}$ 避开集合 $\{q_1, q_2, \ldots, q_n\}$。

让我们试着在第二个例子中看出一种在某些情形下对玩家 (A) 应普遍有效的策略。集合 $B$ 是单点集 $\{q_n\}$ 的并。设想相反地，$B$ 是一列「小」集合 $Q_n$ 的并。那么同样的「策略」仍将奏效，只要给定任意区间 $J$ 与任意 $n \in \mathbb{N}$，都存在区间 $I \subset J$ 使得
```math
I \cap (Q_1 \cup Q_2 \cup \cdots \cup Q_n) = \varnothing .
```
集合 $\bigcap_{n=1}^{\infty} I_n$ 将非空，并将避开集合 $\bigcup_{n=1}^{\infty} Q_n$。于是，若 $B = \bigcup_{n=1}^{\infty} Q_n$，玩家 (A) 便拥有获胜策略。正是在这个意义上，集合 $B$ 是「小」的。集合 $A$ 是「大」的，因为集合 $B$ 是「小」的。若我们仔细考察对集合 $Q_k$ 的要求，就会看到它不过是：这些集合中的每一个都在 $\mathbb{R}$ 中无处稠密（nowhere dense）。

因此，玩家 (A) 获胜的关键在于无处稠密集这一概念。但请注意，它还依赖于集合 $B$ 是一列无处稠密集的并这一事实。

### <span style="color:#2471a3;">**[subsection]**</span> <span style="color:#c0392b">6.4.2 The Baire Category Theorem（Baire 纲定理）</span>

> *标注：Advanced section（高级节），可略过。*

我们可以从上述对博弈的讨论中，用多种方式表述我们的结论：

1. $\mathbb{R}$ 不能被表示为一列无处稠密集的可数并（countable union）。
2. 一列无处稠密集的可数并的补集是稠密的。

其中第二条给出了「一列无处稠密集的可数并是『小』的」这一说法的含义：无论我们选取哪一列可数的无处稠密集，它们的并都会留下一稠密集未被覆盖。

---

---
<!-- ===== 书页 245（PDF 页 11）===== -->
---
### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">6.4 The Baire Category Theorem（Baire 纲定理）</span>

为了表述 Baire category theorem（Baire 纲定理），我们需要一些定义。这正是 Baire 最初使用的语言，并且它一直沿用至今；他只是简单地把集合归入两种类型或纲（category）之中。他把那些应当被视为「小」的集合放进第一纲（first category），把其余（不「小」）的集合放进第二纲（second category）。

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">Definition 6.8（定义 6.8）</span>

> <span style="color:#7f8c8d;">TBB §6.4, p.245</span>

设 $A$ 是实数的一个集合。

1. 若 $A$ 可以表示为可数个 nowhere dense set（无处稠密集）的并集，则称 $A$ 属于第一纲（first category）。
2. 若 $A$ 不属于第一纲，则称 $A$ 属于第二纲（second category）。
3. 若补集（complement）$\mathbb{R} \setminus A$ 属于第一纲，则称 $A$ 在 $\mathbb{R}$ 中是 residual set（剩余集）。

第一纲集及其补集——即剩余集——的下列性质很容易证明，故留作习题。

### <span style="color:#2471a3;">**[lemma]**</span> <span style="color:#c0392b">Lemma 6.9（引理 6.9）</span>

> <span style="color:#7f8c8d;">TBB §6.4, p.245</span>

任意一列第一纲集（first category set）的并集仍然是第一纲集。

### <span style="color:#2471a3;">**[lemma]**</span> <span style="color:#c0392b">Lemma 6.10（引理 6.10）</span>

> <span style="color:#7f8c8d;">TBB §6.4, p.245</span>

任意一列剩余集的交集仍然是剩余集。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 6.11 (Baire Category Theorem, Baire 纲定理)</span>

> <span style="color:#7f8c8d;">TBB §6.4, p.245</span>

$\mathbb{R}$ 的每一个剩余子集都在 $\mathbb{R}$ 中稠密（dense）。

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 第 6.4.1 节中的讨论本身就构成一个证明。假设玩家（A）被分到集合 $A = X \cap [a, b]$，其中 $X$ 是剩余集。于是存在一列无处稠密集 $\{ Q_n \}$，使得
>
> ```math
> X = \mathbb{R} \setminus \bigcup_{n=1}^{\infty} Q_n .
> ```
>
> 然后玩家（A）通过选取任意一个避开 $Q_1$ 的区间 $I_1 \subset [a, b]$，并继续遵循第 6.4.1 节的策略而获胜。特别地，$X$ 必定包含区间 $[a, b]$ 的一个点，因而也包含任意区间的一个点。$\blacksquare$

定理 6.11 提供了一种关于集合「大小」的意义，而一般的稠密集并不具有这种意义。两个稠密集的交集可能是空集，但两个乃至可数多个剩余集的交集仍然必须是稠密的。

<!-- XREF: Lemma 6.9 → §6.4 p.245 -->
---
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Baire category theorem（Baire 纲定理）的历史值得了解：William Fogg Osgood 于 1897 年率先对实数线 $\mathbb{R}$ 证明了等价命题；René Baire 在 1899 年的博士论文 *Sur les fonctions de variables réelles* 中将其推广到 $\mathbb{R}^n$ 并建立了"纲"（category）术语体系——first category（第一纲）= 可数个无处稠密集的并，second category（第二纲）= 非第一纲，residual（剩余集）= 第一纲集的补集。Baire 的洞见在于：这给出了一个独立于基数（可数/不可数）的"大小"尺度。$\mathbb{Q}$ 是可数的，却属于第一纲（"小"）；无理数集不可数，却属于剩余集（"大"）。定理 6.11 的陈述——每个剩余集都稠密——等价于"$\mathbb{R}$ 不能表示为可数个无处稠密集的并"。这意味着：可数个"小"集的并无法覆盖 $\mathbb{R}$。这与 Cantor 定理（可数个有限集的并无法覆盖区间）形成精确类比：Cantor 用的是基数论证，Baire 用的是拓扑论证。两个定理共同塑造了实分析中"小"的两套平行概念。

---
---

---
<!-- ===== 书页 246（PDF 页 12）===== -->
---
### <span style="color:#2471a3;">**[subsection]**</span> <span style="color:#c0392b">6.4.3 Uniform Boundedness（一致有界性）</span>

> *Advanced section（进阶章节），可略过。*

Baire 纲定理在分析学中有许多应用。现在，我们只介绍一个应用，它涉及 uniform boundedness（一致有界性）这个概念。假设我们在 $\mathbb{R}$ 上有一族函数 $\mathcal{F}$，其性质是：对每个 $x \in \mathbb{R}$，集合 $\{ |f(x)| : f \in \mathcal{F} \}$ 都是有界的。这意味着对每个 $x \in \mathbb{R}$ 都存在一个数 $M_x \geq 0$，使得对所有 $f \in \mathcal{F}$ 都有 $|f(x)| \leq M_x$。我们可以把这种情形描述为：$\mathcal{F}$ 是 pointwise bounded（逐点有界）的。这是否意味着这族函数是 uniformly bounded（一致有界）的，即存在一个单一的数 $M$，使得对所有 $f \in \mathcal{F}$ 以及每个 $x \in \mathbb{R}$ 都有 $|f(x)| \leq M$ 呢？

<span style="color:#2471a3;">**[example]**</span> **Example 6.12（例 6.12）**

> <span style="color:#7f8c8d;">TBB §6.4, p.246</span>

设 $q_1, q_2, q_3, \ldots$ 是 $\mathbb{Q}$ 的一个 enumeration（枚举）。对每个 $n \in \mathbb{N}$，我们定义一个函数 $f_n$：当 $n \leq k$ 时 $f_n(q_k) = k$，对所有其他的 $x$ 值则 $f_n(x) = 0$。设 $\mathcal{F} = \{ f_n : n \in \mathbb{N} \}$。那么若 $x \in \mathbb{R} \setminus \mathbb{Q}$，则对所有 $f \in \mathcal{F}$ 都有 $f(x) = 0$；而若 $x = q_k$，则对所有 $f \in \mathcal{F}$ 都有 $|f(x)| \leq k$。因此，对每个 $x \in \mathbb{R}$，集合 $\{ |f(x)| : f \in \mathcal{F} \}$ 都是有界的。当 $x \in \mathbb{R} \setminus \mathbb{Q}$ 时，界可以取为 0（即 $M_x = 0$），而我们可以取 $M_{q_k} = k$。但由于 $\mathbb{Q}$ 在 $\mathbb{R}$ 中稠密（dense），这些函数 $f_n$ 中没有一个是任何区间上的有界函数（请验证这一点）。因此，一族函数可以逐点有界，但在任何区间上都不是一致有界的。$\blacksquare$

例 6.12 中的函数 $f_n$ 处处不连续。我们的下一个定理将表明：如果我们取一族连续函数 $\mathcal{F}$，那么不仅每个 $f \in \mathcal{F}$ 都在闭区间上有界（正如定理 5.49 所保证的），而且还会存在一个区间 $I$，整个函数族在该区间上是一致有界的；也就是说，存在一个常数 $M$，使得对所有 $f \in \mathcal{F}$ 以及每个 $x \in I$ 都有 $|f(x)| \leq M$。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 6.13（定理 6.13）</span>

> <span style="color:#7f8c8d;">TBB §6.4, p.246</span>

设 $\mathcal{F}$ 是 $\mathbb{R}$ 上的一族连续函数，使得对每个 $x \in \mathbb{R}$ 都存在一个常数 $M_x > 0$，满足对每个 $f \in \mathcal{F}$ 都有 $|f(x)| \leq M_x$。那么存在一个开区间 $I$ 和一个常数 $M > 0$，使得对每个 $f \in \mathcal{F}$ 以及 $x \in I$ 都有 $|f(x)| \leq M$。

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 对每个 $n \in \mathbb{N}$，设 $A_n = \{ x : |f(x)| \leq n \text{ 对所有 } f \in \mathcal{F} \}$。由假设，$\mathbb{R} = \bigcup_{n=1}^{\infty} A_n$。又由假设，每个 $f \in \mathcal{F}$ 都连续，因此容易验证：每个集合 $\{ x : |f(x)| \leq n \}$ 都必须是闭集（例如见习题 5.4.31）。于是
>
> ```math
> A_n = \bigcap_{f \in \mathcal{F}} \{ x : |f(x)| \leq n \}
> ```

---

---
<!-- ===== 书页 247（PDF 页 13）===== -->
---
<span style="color:#7f8c8d">*Part006 · 书页 247 行内双语翻译*</span>

<span style="color:#7f8c8d">*（承接书页 246，Theorem 6.13 证明收尾续）*</span>

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）· 续*

> （$A_n$）是可数个闭集的交集，因而其自身也是闭集。
> 这把实直线 $\mathbb{R}$ 表示成闭集序列 $\{A_n\}$ 的并。
> 现在由 Baire category theorem（Baire 纲定理）可推出，这些集合中至少有一个，不妨设为 $A_{n_0}$，必定在某个开区间 $I$ 中稠密。
> 由于 $A_{n_0}$ 是闭的且在区间 $I$ 中稠密，所以 $A_{n_0}$ 必定包含 $I$。
> 这意味着对每个 $f \in \mathcal{F}$ 以及所有 $x \in I$，都有 $|f(x)| \le n_0$。$\blacksquare$

<!-- 习题 6.4.6、6.4.7、6.4.8 为习题区，按约定跳过 -->

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">6.5 Cantor Sets（康托集）</span>

*高级节（Advanced section），可略过。*

我们说一个集合是 perfect set（完全集），如果它是一个没有 isolated point（孤立点）的非空闭集。
我们可能想到的唯一例子是有限个区间的并。
要想象 $\mathbb{R}$ 的一个既完全又 nowhere dense（无处稠密）的子集或许并不容易。
在本节中我们就得到这样一个集合，即非常重要的经典 Cantor set（康托集）。
我们还将讨论它的一些变体。
这类集合具有历史意义，并在数学分析的许多领域中都相当重要。

### <span style="color:#2471a3;">**[subsection]**</span> <span style="color:#c0392b">6.5.1 Construction of the Cantor Ternary Set（Cantor 三进制集的构造）</span>

*高级节（Advanced section），可略过。*

我们从闭区间 $[0, 1]$ 出发。
从这个区间中我们将移除一个 dense open set（稠密开集）$G$。
剩下的集合 $K = [0, 1] \setminus G$ 将既是闭集，又在 $[0, 1]$ 中无处稠密。
我们构造 $G$ 的方式使得 $K$ 没有孤立点且非空。
于是 $K$ 将成为 $[0, 1]$ 的一个非空、无处稠密的完全子集。

最容易理解集合 $G$ 的办法是分阶段地构造它。
令 $G_1 = \left(\frac{1}{3}, \frac{2}{3}\right)$，并令 $K_1 = [0, 1] \setminus G_1$。
于是 $K_1 = \left[0, \frac{1}{3}\right] \cup \left[\frac{2}{3}, 1\right]$ 就是当区间 $[0, 1]$ 的中间三分之一（middle third）被移除后所剩下的部分。
这就是我们构造的第一阶段。
---
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> "perfect set（完全集）"的定义——非空闭集且没有孤立点——初看似乎平淡，但当你尝试构造一个既 perfect 又 nowhere dense 的集合时，任何简单尝试都会失败。有限个闭区间的并若没有孤立点则必含开区间（从而不无处稠密）。Cantor 集的构造策略是**自相似地"挖洞"**：第 $n$ 阶段从 $2^{n-1}$ 个区间中各挖掉中间三分之一的**开**区间。关键点在于挖开区间而非闭区间——保留端点确保 $K$ 非空且闭；每一阶段剩余 $2^n$ 个闭区间、每个长 $1/3^n$；取可数无穷次交集后 $K$ 没有长度正的开区间（因此无处稠密），但端点始终保留，且每个点都被其他点从两侧任意逼近（因此无孤立点）。这是一个典型的"无穷过程产生反直觉对象"的案例：有限步操作不可能同时满足 perfect 和 nowhere dense，但可数无穷步可以。

---
---

---
<!-- ===== 书页 248（PDF 页 14）===== -->
---
<span style="color:#7f8c8d">*Part006 · 书页 247 行内双语翻译*</span>

<span style="color:#2471a3;">**[figure]**</span> **Figure 6.1（图 6.1）** Cantor 三进制集构造的第三阶段。
图中自上而下绘出 $K_1$、$K_2$、$K_3$ 三层区间带，横轴刻度依次为 $0,\ \frac{1}{9},\ \frac{2}{9},\ \frac{1}{3},\ \frac{2}{3},\ \frac{7}{9},\ \frac{8}{9},\ 1$。

我们对 $K_1$ 的两个 component interval（分量区间）分别重复这一构造。
令 $G_2 = \left(\frac{1}{9}, \frac{2}{9}\right) \cup \left(\frac{7}{9}, \frac{8}{9}\right)$，并令 $K_2 = [0, 1] \setminus (G_1 \cup G_2)$。
于是

```math
K_2 = \left[0, \frac{1}{9}\right] \cup \left[\frac{2}{9}, \frac{1}{3}\right] \cup \left[\frac{2}{3}, \frac{7}{9}\right] \cup \left[\frac{8}{9}, 1\right].
```

这样便完成了第二阶段。

我们归纳地继续这一过程，得到两列集合 $\{K_n\}$ 与 $\{G_n\}$，它们具有下列性质：对每个 $n \in \mathbb{N}$，

1. $G_n$ 是 $2^{n-1}$ 个两两不交的开区间之并。
2. $K_n$ 是 $2^n$ 个两两不交的闭区间之并。
3. $K_n = [0, 1] \setminus (G_1 \cup G_2 \cup \cdots \cup G_n)$。
4. $G_{n+1}$ 的每个分量都是 $K_n$ 的某个分量的「middle third（中间三分之一）」。
5. $K_n$ 的每个分量的长度都是 $1/3^n$。

图 6.1 展示了 $K_1$、$K_2$ 与 $K_3$。

现在令

```math
G = \bigcup_{n=1}^{\infty} G_n,
```

并令

```math
K = [0, 1] \setminus G = \bigcap_{n=1}^{\infty} K_n.
```

那么 $G$ 是开集，而集合 $K$（即我们的康托集）是闭集。

为了看出 $K$ 无处稠密，由于 $K$ 是闭集，只需证明 $K$ 不包含任何开区间即可（见 <span style="color:#7f8c8d">Exercise 6.3.4</span>）。
设 $J$ 是 $[0, 1]$ 中的一个开区间，记 $\lambda$ 为其长度。
选取 $n \in \mathbb{N}$ 使 $1/3^n < \lambda$。
由性质 5，$K_n$ 的每个分量长度为 $1/3^n < \lambda$；又由性质 2，$K_n$ 的各分量两两不交。
因此 $K_n$ 不可能包含 $J$，于是 $K = \bigcap_{n=1}^{\infty} K_n$ 也不可能包含 $J$。
这样我们就证明了闭集 $K$ 不包含任何区间，因而无处稠密。

剩下还要证明 $K$ 没有孤立点。
令 $x_0 \in K$，我们证明 $x_0$ 是 $K$ 的一个 limit point（聚点）。
为此我们证明：对每个 $\varepsilon > 0$，都存在 $x_1 \in K$ 使得……
（下页续）
---

---
<!-- ===== 书页 249（PDF 页 15）===== -->
---
<span style="color:#7f8c8d">*Part006 · 书页 249 行内双语翻译*</span>

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">6.5 Cantor Sets（康托集）</span>

本页开头是上一页某个定理证明的收尾部分，其结论是 $K$ 没有 isolated point（孤立点）。

> 使得 $0 < |x_1 - x_0| < \varepsilon$。
> 选取 $n$ 使得 $1/3^n < \varepsilon$。
> 在 $K_n$ 中存在一个包含 $x_0$ 的 component（分量）$L$。
> 这个分量是一个长度为 $1/3^n < \varepsilon$ 的闭区间。
> 集合 $K_{n+1} \cap L$ 有两个分量 $L_0$ 和 $L_1$，其中每一个都含有 $K$ 的点。
> 点 $x_0$ 位于其中一个分量之中，设为 $L_0$。
> 设 $x_1$ 是 $K \cap L_1$ 中任意一点。
> 于是 $0 < |x_0 - x_1| < \varepsilon$。
> 这验证了 $x_0$ 是 $K$ 的 limit point（聚点）。
> 因此 $K$ 没有孤立点。

集合 $K$ 被称为 Cantor set（康托集）。
由于它的构造方式，它常常被称为 Cantor middle third set（康托中间三分集）。
稍后我们将给出康托集的一个纯算术描述，这个描述提示了 $K$ 的另一个常见名称——「Cantor ternary set（康托三进制集）」。
但首先，我们先提及 $K$ 及其 complement（补集）$G$ 的几个性质，它们或许有助于你直观地想象这些集合。

首先注意到 $G$ 是 $[0,1]$ 中的 dense open set（稠密开集）。
将 $G$ 写成 $G = \bigcup_{k=1}^{\infty} (a_k, b_k)$。
（$G$ 的分量区间（component interval）$(a_k, b_k)$ 可以称为 $K$ 在 $(0,1)$ 中的互补区间（intervals complementary to $K$）；其中每一个都是某个 $K_n$ 的一个分量区间的中间三分之一。）
注意到这些分量区间中任意两个都不可能有一个公共端点。
例如，若 $b_m = a_n$，那么这个点就会成为 $K$ 的一个孤立点，而 $K$ 没有孤立点。

其次观察到，对每个 $k \in \mathbb{N}$，点 $a_k$ 与 $b_k$ 都是 $K$ 的点。
但 $K$ 中还有其他的点。
事实上，我们马上就会看到 $K$ 是 uncountable（不可数的）。
这些其他的点都是互补区间端点的聚点。
端点集是 countable（可数的），但正如我们即将看到的，这个集合的 closure（闭包）却是不可数的。
因此，从 cardinality（基数）的意义上说，康托集的「大部分」点并不是 $K$ 的互补区间的端点。

集合 $G_n$ 的每个分量区间长度都是 $1/3^n$，因此这些分量区间的长度之和为

```math
\frac{2^{n-1}}{3^n} = \frac{1}{2}\left(\frac{2}{3}\right)^n .
```

由此可见，$G$ 的所有分量区间的长度构成一个 geometric series（几何级数），其和为

```math
\sum_{n=1}^{\infty} \frac{1}{2}\left(\frac{2}{3}\right)^n = 1 .
```

（这同时也给我们一个线索，说明为什么 $K$ 不可能包含区间：从单位区间中移去一族两两不相交、长度总和为 $1$ 的区间之后，在剩下的集合 $K$ 中便不再有任何区间的容身之处了。）

<!-- 习题 6.5.1–6.5.3(a)，按约定跳过 -->
---

---
<!-- ===== 书页 250（PDF 页 16）===== -->
---
<span style="color:#7f8c8d">*Part006 · 书页 249 行内双语翻译*</span>

<!-- 习题 6.5.3(b)(c)–6.5.6，按约定跳过 -->

### <span style="color:#2471a3;">**[subsection]**</span> <span style="color:#c0392b">6.5.2 An Arithmetic Construction of K（$K$ 的算术构造）</span>

> 富余内容（enrichment section），可略过。

我们现在转向康托集的一个纯算术构造。
这里你需要对 ternary（base 3）算术，即三进制算术，有一些了解。

每个 $x \in [0,1]$ 都可以用三进制表示为

```math
x = .a_1 a_2 a_3 \ldots ,
```

其中 $a_i = 0, 1$ 或 $2$，$i = 1, 2, 3, \ldots$。
某些点有两个表示，一种以一串零结尾，另一种以一串二结尾。
例如，$.1000 \cdots = .0222 \cdots$ 两者都表示同一个数 $1/3$（十进制）。
现在，若 $x \in (1/3, 2/3)$，则 $a_1 = 1$，因此每个 $x \in G_1$ 的 ternary expansion（三进制展开）的第一位必须是 '1'。
类似地，若 $x \in G_2 = (1/9, 2/9) \cup (7/9, 8/9)$，则其三进制展开的第二位必须是 1（即 $a_2 = 1$）。
一般地，$G_n$ 中的每个点都必须有 $a_n = 1$。
由此可得，$G = \bigcup_{n=1}^{\infty} G_n$ 中的每个点在其三进制展开的某处必定有一个 1。

现在，$K$ 的互补区间的端点都有两个表示，其中一个是完全不出现 1 的。
$K$ 的其余点从不落入某个集合 $K_n$ 的一个分量的中间三分之一，因此它们的三进制展开具有形式

```math
x = .a_1 a_2 \ldots , \quad a_i = 0 \ \text{或} \ 2 .
```

因此我们可以把 $K$ 算术地描述为如下集合

```math
\{ x = .a_1 a_2 a_3 \ldots \ (\text{base three}) : a_i = 0 \ \text{或} \ 2,\ \text{对每个 } i \in \mathbb{N} \} .
```

作为直接结果，我们看到 $K$ 是不可数的。
事实上，$K$ 可以与 $[0,1]$ 建立一一对应（1-1 correspondence）：对每个 $x = .a_1 a_2 a_3 \ldots$（base 3），$a_i = 0, 2$，……
---
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Cantor 集的三进制刻画——$K = \{0.a_1a_2a_3\ldots_{(3)} : a_i \in \{0, 2\}\}$——是理解其不可数性的关键。这与 $[0,1]$ 的二进制展开 $\{0.b_1b_2b_3\ldots_{(2)} : b_i \in \{0,1\}\}$ 仅差一个"除以 2"的映射 $b_i = a_i/2$。这立即给出 $K$ 与 $[0,1]$ 之间的一一对应，从而 $K$ 不可数。你已在 6.042J 中通过**对角线论证**证明了 $[0,1]$ 不可数：假设存在枚举 $x_1, x_2, \ldots$，构造 $x$ 使其第 $n$ 位与 $x_n$ 第 $n$ 位不同。这个论证完全适用于 $K$——只需限制每位取 0 或 2。事实上，Cantor 本人正是在研究三角级数的唯一性时发现了这个集合（Smith 1874 年更早发现，Cantor 1883 年提及），而对角线论证正是他后来用于证明实数不可数的方法。历史顺序是：先有 Cantor 集（一个"无处稠密却不可数"的具体反例），后有对角线论证（推广到整个 $[0,1]$ 的不可数性证明）。

---
---

---
<!-- ===== 书页 251（PDF 页 17）===== -->
---
<span style="color:#7f8c8d">*Part006 · 书页 251 行内双语翻译*</span>

<span style="color:#7f8c8d">Section 6.5 Cantor Sets（康托集）· 收尾</span>

对于集合 $K$ 中的元素，令其对应数 $y = .b_1 b_2 b_3 \ldots$（以 2 为底，base 2），其中 $b_i = a_i/2$。

这样便在 $K$（去掉互补区间的端点）与 $[0,1]$（去掉拥有两种基 2 表示形式的数的可数集，countable set）之间建立了一一对应（1-1 correspondence）。

通过让这两个可数集彼此对应，我们便得到 $K$ 与 $[0,1]$ 之间的一一对应。

**注记（Note）.** 我们在本节结尾提到，$K$ 构造方式的变化可以引出有趣的情形。

例如，稍加改变构造，我们可以移除区间，使得

```math
G_0 = \bigcup_{k=1}^{\infty} (a_{0k}, b_{0k})
```

其中

```math
\sum_{k=1}^{\infty} (b_{0k} - a_{0k}) = 1/2
```

（而不是 1），同时仍保持 $K_0 = [0,1] \setminus G_0$ 是无处稠密（nowhere dense）且完美（perfect）的。

这样得到的集合 $K_0$ 给十九世纪末那些试图发展测度（measure）理论的数学家们制造了难题。

$G_0$ 的“测度”应当是 $1/2$；$[0,1]$ 的“测度”应当是 1。

直觉要求这个无处稠密集 $K_0$ 的测度应当是 $1 - 1/2 = 1/2$。

而当 $K_0$ 如此“小”时，这怎么可能呢？

<span style="color:#7f8c8d">Exercises（习题）6.5.7–6.5.10：按约定跳过。</span>
---

---
<!-- ===== 书页 252（PDF 页 18）===== -->
---
<span style="color:#7f8c8d">*Part006 · 书页 252 行内双语翻译*</span>

### <span style="color:#2471a3;">**[subsection]**</span> <span style="color:#c0392b">6.5.3 The Cantor Function（康托函数）</span>

*高级小节（Advanced section）。可略过。*

康托集（Cantor set）使得我们可以构造一个相当奇特的函数，它在区间 $[0,1]$ 上连续且非递减（nondecreasing）。

它的性质是：在康托集的每一个互补区间上取常值，却又设法从 $f(0) = 0$ 增加到 $f(1) = 1$——它把全部的增长都放在康托集本身之上完成。

它有时被称为“魔鬼阶梯”（the devil's staircase）。

按如下方式定义函数 $f$。

在 $(1/3, 2/3)$ 上，令 $f = 1/2$；在 $(1/9, 2/9)$ 上，令 $f = 1/4$；在 $(7/9, 8/9)$ 上，令 $f = 3/4$。

如此归纳地进行下去。

在第 $n$ 阶段出现的 $2^{n-1}$ 个开区间上，定义 $f$ 使其满足下列条件：

1. $f$ 在每一个这样的区间上都取常值。

2. $f$ 在这些区间上取值 $\dfrac{1}{2^n}, \dfrac{3}{2^n}, \ldots, \dfrac{2^n - 1}{2^n}$。

3. 若 $x$ 与 $y$ 属于不同的第 $n$ 阶段区间且 $x < y$，则 $f(x) < f(y)$。

这一描述在 $G = [0,1] \setminus K$ 上定义了 $f$。

通过定义 $f(0) = 0$，并对 $0 < x \le 1$ 定义 $f(x) = \sup\{f(t) : t \in G, t < x\}$，我们把 $f$ 延拓到整个 $[0,1]$。

为了验证这定义的就是我们想要的函数，需要逐项核对下列各条：

1. $f(G)$ 在 $[0,1]$ 中稠密（dense）。

2. $f$ 在 $[0,1]$ 上非递减。

3. $f$ 在 $[0,1]$ 上连续。

4. $f(K) = [0,1]$。

这些已留作习题。

图 6.2 展示了这一构造。

函数 $f$ 被称为康托函数（Cantor function）。

注意，$f$ 的“全部上升”都发生在集合 $K$ 上。

康托函数使得许多关于函数与导数的问题都能得到否定的回答，因此它已成为一个广受欢迎的反例（counterexample）。

例如，让我们循着这样的思路推想。

若 $f$ 是 $[0,1]$ 上的连续函数，且对每个 $x \in (0,1)$ 都有 $f'(x) = 0$，则 $f$ 是常函数。

（这一点在大多数微积分课程中都用中值定理（mean value theorem）来证明。）

现在假设我们所知更少：对每个 $x \in (0,1)$，除一个我们对其一无所知的“小”集合 $E$ 之外，都有 $f'(x) = 0$。

若 $E$ 是有限的，则仍很容易证明 $f$ 必为常函数。

若 $E$ 是可数的，则仍有可能证明 $f$ 必为常函数，只是要稍微困难一些。

于是问题产生了：这里的集合 $E$ 究竟能小到什么程度；也就是说，我们到底需要知道……
---
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Cantor 函数（"魔鬼阶梯"）是对微积分直觉的一记精确打击。微积分基本定理告诉你：若 $f'(x)=0$ 对所有 $x$ 成立，则 $f$ 是常数。若 $f'(x)=0$ 除了有限个点外成立，你仍能用中值定理逐个区间推出 $f$ 常数。若例外集是可数的——这需要更细致的论证，但结论依然成立。Cantor 函数揭示的惊人事实是：例外集可以是一个**不可数的、无处稠密的**集合（Cantor 集 $K$），$f$ 在 $K$ 的每个互补区间上取常值（导数为 0），却仍能从 0 一路爬到 1。这迫使你重新思考：导数几乎处处为零的函数，其单调递增的"全部上升"可以被压缩在一个测度为零（但不可数！）的集合上。这个例子直接通向测度论的核心动机——你需要比"纲"更精细的工具来区分 Cantor 集的"大小"（测度 0）与"拓扑大小"（不可数、完全集）。

---
---

---
<!-- ===== 书页 253（PDF 页 19）===== -->
---
<span style="color:#7f8c8d">*Part006 · 书页 253 行内双语翻译*</span>

**Figure 6.2（图 6.2）**：Cantor function（康托函数）构造的第三阶段。

<span style="color:#1e8449">*译者注：*</span> 图中纵轴标注的是台阶取值（依次为 1/8、1/4、3/8、1/2、5/8、3/4、7/8 等），横轴为相应三分区间的端点（1/9、2/9、1/3、2/3、7/9、8/9）。

（第 6.5 节末尾的讨论继续）关于某个集合 $E$，能否做到：只要对每个 $x \in (0, 1) \setminus E$ 都有 $f'(x) = 0$，就能推出 $f$ 是常值？

Cantor function（康托函数）正是这样一个函数的例子：它在与 Cantor set（康托集）$K$ 互补的每一个区间上都是常值（从而在这些点处的导数为零），然而它本身却不是常值。

既然 Cantor set 是 nowhere dense（无处稠密）的，它或许会被视为极其微小；但即便如此，对于这个问题它也并非无关紧要。

<!-- 习题 6.5.11、6.5.12 属习题区，按约定跳过 -->

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">6.6 Borel Sets（Borel 集）</span>

高级内容（Advanced section），可以略过。

在我们对连续函数的研究中已经看到，open sets（开集）类与 closed sets（闭集）类起着重要作用。

然而，在分析中具有重要意义的集合类并不仅限于开集与闭集。

E. Borel（1871–1956）认识到，对于分析的许多运算，我们需要形成集合类的 countable intersections（可数交）与 countable unions（可数并）。
---
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 第 6.6 节引入 Borel 集——从开集出发，经可数次并、交、补运算生成的集合族。此处仅开篇，故本条注作为展望：Borel 集的出现动机正是前述内容的自然延伸。Cantor 集 $K$ 是可数个开集的交的补集（即 Gδ 集的补），因而是 Borel 集。第一纲集、剩余集、Gδ 集、Fσ 集——这些概念在第 6 章后半（以及后续 Lebesgue 测度章节）将交织成一张描述实数子集"正则性"的概念网络。你已掌握的 De Morgan 定律（6.042J）将是穿梭于这些集合运算之间的基本工具。
---

---
<!-- ===== 书页 254（PDF 页 20）===== -->
---
<span style="color:#7f8c8d">*Part006 · 书页 254 行内双语翻译*</span>

（承上页）……集合类的并。Borel set（Borel 集）这一集合族正是为了允许这些运算而引入的。

我们回忆：closed sets（闭集）的可数并可能不再是闭集（或开集），而 open sets（开集）的可数交同样可能不再是开集（或闭集）。

在本节中，我们引入分析中重要的另外两类集合：sets of type $G_\delta$（Gδ 型集合，即可数个开集的交集）与 sets of type $F_\sigma$（Fσ 型集合，即可数个闭集的并集）。

这两类只是庞大的 Borel 集类的开端。

我们将发现，它们恰好是解决关于实函数的一些基本问题的正确集合类。

### <span style="color:#2471a3;">**[subsection]**</span> <span style="color:#c0392b">6.6.1 Sets of Type Gδ（Gδ 型集合）</span>

高级内容（Advanced section），可以略过。

回忆：一族开集的并仍是开集（无论该族中有多少个集合），但如果一族开集含有无穷多个集合，则它们的交未必是开集。

例如，
```math
\bigcap_{n=1}^\infty \left(-\frac{1}{n}, \frac{1}{n}\right) = \{0\}.
```

类似地，若 $q_1, q_2, q_3, \ldots$ 是 $\mathbb{Q}$ 的一个 enumeration（枚举），则
```math
\bigcap_{k=1}^\infty \left(\mathbb{R} \setminus \{q_k\}\right) = \mathbb{R} \setminus \mathbb{Q},
```
即无理数集。

集合 $\{0\}$ 是闭集（不是开集），而 $\mathbb{R} \setminus \mathbb{Q}$ 既不是开集也不是闭集。

集合 $\mathbb{R} \setminus \mathbb{Q}$ 是开集的一个可数交。

这类集合足够重要，值得为它们命名。

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">Definition 6.14（定义 6.14）</span>

> <span style="color:#7f8c8d;">TBB §6.6, p.254</span>

<span style="color:#00838f">$\mathbb{R}$ 的子集 $H$ 称为 Gδ 集，如果它能表示为开集的可数交</span>，也就是说，如果存在开集 $G_1, G_2, G_3, \ldots$ 使得
```math
H = \bigcap_{k=1}^\infty G_k .
```

<span style="color:#2471a3;">**[example]**</span> **Example 6.15（例 6.15）**

> <span style="color:#7f8c8d;">TBB §6.6, p.254</span>

闭区间 $[a, b]$ 或半开区间 $(a, b]$ 都是 Gδ 型，因为
```math
[a, b] = \bigcap_{n=1}^\infty \left(a - \frac{1}{n}, b + \frac{1}{n}\right)
```
并且
```math
(a, b] = \bigcap_{n=1}^\infty \left(a, b + \frac{1}{n}\right).
```

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 6.16（定理 6.16）</span>

> <span style="color:#7f8c8d;">TBB §6.6, p.254</span>

$\mathbb{R}$ 中的每一个开集和每一个闭集都是 Gδ 型。

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 设 $G$ 是 $\mathbb{R}$ 中的一个开集。
>
> 显然 $G$ 是 Gδ 型。
>
> 我们还要证明 $G$ 可以表示为闭集的可数并。
>
> 将 $G$ 写成如下形式
> ```math
> G = \bigcup_{k=1}^\infty (a_k, b_k)
> ```

<!-- XREF: Example 6.15 → §6.6 p.254 -->
---
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> $G_\delta$ 与 $F_\sigma$ 这两个记号各自承载着德文与法文的「混血」起源。$G_\delta$ 中，$G$ 取自德文 *Gebiet*（意为「开集」/「区域」），$\delta$ 取自德文 *Durchschnitt*（意为「交」）——所以 $G_\delta$ 直译就是「开集的可数交」。对偶地，$F_\sigma$ 中，$F$ 取自法文 *fermé*（意为「闭集」），$\sigma$ 取自法文 *somme*（意为「并」）——$F_\sigma$ 直译就是「闭集的可数并」。这两个记号大约在 20 世纪初由 Hausdorff 等人在集合论拓扑学中推广定型。知道记号来源有助于记忆：$\delta$ 像「交」的楔形、$\sigma$ 像「并」的 S 形——但严格对应关系要反直觉地归到德文/法文缩写。这也解释了为什么不是英语缩写：现代分析学的「骨架」主要是在德法两国搭建的。
---
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 为什么需要引入 Borel set（Borel 集）？回忆你已知的结论：开集的可数并仍是开集，但开集的**可数交**不一定是开集；闭集的可数交仍是闭集，但闭集的**可数并**不一定是闭集。这意味着「开集」和「闭集」两个类在可数运算下并不封闭——你连续做几次可数交/并就会「溢出」到新类型的集合。Borel 集正是通过反复对开集做可数并、可数交、取补集这些运算所生成的最小集合族——在数学上这叫做包含全体开集的**最小 σ-代数**（σ-algebra）。此处 σ 的含义与 $F_\sigma$ 中的 σ 一致（可数并运算），「代数」则指该集合族对补集运算封闭。Borel 集以 Émile Borel（1898, *Leçons sur la théorie des fonctions*）命名，他最早系统研究这类集合。目前你只需知道 Gδ 和 Fσ 是 Borel 层级的最底两层（往上还有 Gδσ、Fσδ、Gδσδ……无穷层），这为后续测度论（哪些集合可测）和概率论（事件 σ-代数）提供了基础框架。Borel 集的完整理论在测度论中才会展开——这里只是「预告片」。
---

---
<!-- ===== 书页 255（PDF 页 21）===== -->
---
> Part006 · 第 6 章 · 书页 255 行内双语翻译

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">6.6 Borel Sets（Borel 集）（续）</span>

<span style="color:#1e8449;">*译者注：* 本页开头承接上一页 Theorem 6.16 的证明。</span>

其中区间 $(a_k, b_k)$ 两两不相交（pairwise disjoint）。现在，对每个 $k \in \mathbb{N}$，都存在序列 $\{c_{kj}\}$ 与 $\{d_{kj}\}$，使得序列 $\{c_{kj}\}$ 递减趋于 $a_k$，序列 $\{d_{kj}\}$ 递增趋于 $b_k$，并且对每个 $j \in \mathbb{N}$ 都有 $c_{kj} < d_{kj}$。因此

```math
(a_k, b_k) = \bigcup_{j=1}^{\infty} [c_{kj}, d_{kj}].
```

这样，我们就将 $G$ 的每个构成区间（component interval）表示成了闭集的可数并（countable union）。由此可知

```math
G = \bigcup_{k=1}^{\infty}\bigcup_{j=1}^{\infty} [c_{kj}, d_{kj}] = \bigcup_{j,k=1}^{\infty} [c_{kj}, d_{kj}]
```

也是闭集的可数并。现在取补集（complement）。利用 de Morgan 定律（De Morgan's laws），这表明 $\mathbb{R} \setminus G$ 可以表示为开集的可数交（countable intersection）。由于每个闭集 $F$ 都能写成 $F = \mathbb{R} \setminus G$（其中 $G$ 为某个开集），我们便证明了：任何闭集都是 Gδ 型（type $G_\delta$）的，即属于 Gδ set（Gδ 集，即可数个开集的交集）。$\blacksquare$

我们在第 6.4 节观察到，一个 dense set（稠密集）在范畴（category）意义下可以是很小的。例如，$\mathbb{Q}$ 是一个 first category set（第一纲集）。我们的下一个结果表明，一个 Gδ 型的稠密集在范畴意义下必定是很大的。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 6.17（定理 6.17）</span>

> <span style="color:#7f8c8d;">TBB §6.6, p.255</span>

设 $H$ 为 Gδ 型且在 $\mathbb{R}$ 中稠密，则 $H$ 是 residual set（剩余集）。

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 把 $H$ 写成 $H = \bigcap_{k=1}^{\infty} G_k$，其中每个集合 $G_k$ 都是开集。由假设 $H$ 稠密，且对每个 $k \in \mathbb{N}$ 都有 $H \subset G_k$，于是每个开集 $G_k$ 也都是稠密的。因此，对每个 $k \in \mathbb{N}$，$\mathbb{R} \setminus G_k$ 都是 nowhere dense（无处稠密）的，从而每个 $G_k$ 都是剩余集。结论现在由 Lemma 6.10（引理 6.10）得出。$\blacksquare$

---

---
<!-- ===== 书页 256（PDF 页 22）===== -->
---
> Part006 · 第 6 章 · 书页 256 行内双语翻译

### <span style="color:#2471a3;">**[subsection]**</span> <span style="color:#c0392b">6.6.2 Sets of Type Fσ（Fσ 型集合）</span>

<span style="color:#7f8c8d;">*（高级小节（advanced section），可略读。）*</span>

正如开集的可数交构成更大一类的集合——即 Gδ 集——同样，闭集的可数并也构成更大一类的集合。开集的补集是闭集。通过考察 Gδ 集的补集，我们便得到 Fσ set（Fσ 集，即可数个闭集的并集）这一对偶概念（dual notion）。

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">Definition 6.18（定义 6.18）</span>

> <span style="color:#7f8c8d;">TBB §6.6, p.256</span>

<span style="color:#00838f">若 $\mathbb{R}$ 的子集 $E$ 可以表示为闭集的可数并，即存在闭集 $F_1, F_2, F_3, \ldots$ 使得 $E = \bigcup_{k=1}^{\infty} F_k$，则称 $E$ 为 Fσ 型（type $F_\sigma$）集合</span>。

利用 de Morgan 定律，我们容易验证：Gδ 集的补集是 Fσ 集，反之亦然（见习题 6.6.4）。这与「一个集合是开集当且仅当其补集是闭集」这一事实密切相关。

<span style="color:#2471a3;">**[example]**</span> **Example 6.19（例 6.19）**

> <span style="color:#7f8c8d;">TBB §6.6, p.256</span>

有理数集 $\mathbb{Q}$ 是一个 Fσ 型集合。这一点很清楚，因为它可以表示为

```math
\mathbb{Q} = \bigcup_{n=1}^{\infty} \{r_n\}
```

其中 $\{r_n\}$ 是有理数的任意枚举（enumeration）。单点集（singleton set）$\{r_n\}$ 显然是闭集。但请注意，$\mathbb{Q}$ 也不是 Gδ 型的。由 Theorem 6.17（定理 6.17）可知，Gδ 型的稠密集必定是 uncountable（不可数）的（因为可数集是第一纲集）。特别地，$\mathbb{Q}$ 不是 Gδ 型的，因此 $\mathbb{R} \setminus \mathbb{Q}$ 也不是 Fσ 型的。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 6.20（定理 6.20）</span>

> <span style="color:#7f8c8d;">TBB §6.6, p.256</span>

一个集合是 Gδ 型的当且仅当其补集是 Fσ 型的。

<span style="color:#2471a3;">**[example]**</span> **Example 6.21（例 6.21）**

> <span style="color:#7f8c8d;">TBB §6.6, p.256</span>

半开区间（half-open interval）$(a, b]$ 既是 Gδ 型也是 Fσ 型：

```math
(a, b] = \bigcap_{n=1}^{\infty}\left(a, b + \frac{1}{n}\right) = \bigcup_{n=1}^{\infty}\left[a + \frac{b-a}{n}, b\right].
```

<span style="color:#7f8c8d;">*Note（注意）：*</span> $\mathbb{R}$ 中既开又闭的子集只有空集和 $\mathbb{R}$ 本身。然而，同时为 Gδ 型和 Fσ 型的集合却有很多，见习题 6.6.1。

我们现在可以扩展 Theorem 6.16（定理 6.16）。在那里我们证明了所有开集和所有闭集都属于 Gδ 类。我们现在证明它们也属于 Fσ 类。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 6.22（定理 6.22）</span>

> <span style="color:#7f8c8d;">TBB §6.6, p.256</span>

$\mathbb{R}$ 中每个开集和每个闭集都既是 Fσ 型也是 Gδ 型。

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 在 Theorem 6.16 的证明中，我们明确展示了如何将任何开集表示为 Fσ 型。因此，开集既是 Fσ 型也是 Gδ 型（后者是平凡的）。关于闭集的部分，现在通过考虑补集并利用 de Morgan 定律即得。闭集的补集是开集，因此 Fσ 集的补集是 Gδ 集。$\blacksquare$

<!-- XREF: Example 6.19 → §6.6 p.256 -->
<!-- XREF: Example 6.21 → §6.6 p.256 -->
---

---
<!-- ===== 书页 257（PDF 页 23）===== -->
---
<span style="color:#7f8c8d">*Part006 · 书页 257 行内双语翻译*</span>

<span style="color:#7f8c8d">本页开头为习题区（Exercise 6.6.4–6.6.7），按约定跳过。</span>

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">6.7 Oscillation and Continuity（振幅与连续性）</span>

> 高级节（Advanced section），可以略读。

在本节中，我们回到一个自第 5.9 节起就开始研究的问题，即关于函数间断点集合性质的问题。

为了讨论这个集合，我们将需要 Fσ set（Fσ 集，即可数个闭集的并集）与 Gδ set（Gδ 集，即可数个开集的交集）的概念，并且需要引入一个新的工具——函数的 oscillation（振幅）。

我们从这样一个函数 $f$ 的例子开始：它在每个有理数处都不连续，而在每个无理数处都连续。

<span style="color:#2471a3;">**[example]**</span> **Example 6.23（例 6.23）**

> <span style="color:#7f8c8d;">TBB §6.7, p.257</span>

设 $q_1, q_2, q_3, \ldots$ 是 $\mathbb{Q}$ 的一个 enumeration（枚举）。

定义函数 $f$ 如下：

```math
f(x) = \begin{cases} 1/k, & \text{if } x = q_k \\ 0, & \text{if } x \in \mathbb{R} \setminus \mathbb{Q}. \end{cases}
```

由于 $\mathbb{R} \setminus \mathbb{Q}$ 在 $\mathbb{R}$ 中 dense（稠密），$f$ 在点 $x$ 处连续仅当 $f(x) = 0$；也就是说，仅当 $x \in \mathbb{R} \setminus \mathbb{Q}$ 时才有可能。

因此 $f$ 在每个 $x \in \mathbb{Q}$ 处都不连续。

为验证 $f$ 在 $\mathbb{R} \setminus \mathbb{Q}$ 的每一点处连续，设 $x_0 \in \mathbb{R} \setminus \mathbb{Q}$，并设 $\varepsilon > 0$。

选取 $k \in \mathbb{N}$ 使得 $1/k < \varepsilon$。

由于集合 $\{q_1, q_2, \ldots, q_k\}$ 是不含 $x_0$ 的有限集，故存在 $\delta > 0$，使得对每个 $i = 1, \ldots, k$ 都有 $|q_i - x_0| \geq \delta$。

因此，若 $x \in \mathbb{R}$ 且 $|x - x_0| < \delta$，则要么 $x \in \mathbb{R} \setminus \mathbb{Q}$，要么对某个 $j > k$ 有 $x = q_j$。

无论哪种情形都有 $|f(x) - f(x_0)| \leq 1/k < \varepsilon$。

这验证了 $f$ 在 $x_0$ 处的连续性。

由于 $x_0$ 是任意选取的无理点，我们看到 $f$ 在每个无理点处都连续。$\blacksquare$

我们的例子表明，一个函数可以做到在每个无理数处连续、而在每个有理数处不连续。

相反的情形是否可能发生？

---

---
<!-- ===== 书页 258（PDF 页 24）===== -->
---
<span style="color:#7f8c8d">*Part006 · 书页 258 行内双语翻译*</span>

——也就是说，是否存在一个函数 $f$，在 $\mathbb{Q}$ 上连续而在 $\mathbb{R} \setminus \mathbb{Q}$ 上不连续？

更一般地，定义在某个区间上的函数 $f$，其连续点集（set of continuity points）可以是哪些集合？

我们将在本节回答这个问题。

主要的工具是函数在某一点的 oscillation（振幅）。

### <span style="color:#2471a3;">**[subsection]**</span> <span style="color:#c0392b">6.7.1 Oscillation of a Function（函数的振幅）</span>

> 高级节（Advanced section），可以略读。

为了描述一个间断点，我们需要一种度量该间断的方式。

对于 monotonic（单调）函数，此前是用 jump（跳跃）作为这样的度量。

对于一般的、非单调的函数，则使用另一种工具。

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">Definition 6.24（定义 6.24）</span>

> <span style="color:#7f8c8d;">TBB §6.7, p.258</span>

<span style="color:#00838f">设 $f$ 定义在非退化区间（nondegenerate interval）$I$ 上。我们定义 $f$ 在 $I$ 上的 oscillation（振幅）为如下量：</span>

```math
\omega_f(I) = \sup_{x,y \in I} |f(x) - f(y)|.
```

下面看看振幅与连续性有何关联。

设 $f$ 定义在 $x_0$ 的一个 neighborhood（邻域）内，并且 $f$ 在 $x_0$ 处连续，那么

```math
\inf_{\delta > 0} \omega_f((x_0 - \delta, x_0 + \delta)) = 0. \tag{1}
```

为看出这一点，设 $\varepsilon > 0$。

由于 $f$ 在 $x_0$ 处连续，故存在 $\delta_0 > 0$，使得当 $|x - x_0| < \delta_0$ 时有 $|f(x) - f(x_0)| < \varepsilon/2$。

若 $x_0 - \delta_0 < x_1 \leq x_2 < x_0 + \delta_0$，则

```math
|f(x_1) - f(x_2)| \leq |f(x_1) - f(x_0)| + |f(x_0) - f(x_2)| < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon. \tag{2}
```

由于 (2) 对一切 $x_1, x_2 \in (x_0 - \delta_0, x_0 + \delta_0)$ 都成立，我们得到

```math
\sup \{|f(x_1) - f(x_2)| : x_0 - \delta_0 < x_1 \leq x_2 < x_0 + \delta_0\} \leq \varepsilon. \tag{3}
```

而 (3) 蕴含：若 $0 < \delta < \delta_0$，则 $\omega_f([x_0 - \delta, x_0 + \delta]) \leq \varepsilon$。

由于 $\varepsilon$ 是任意的，结论成立。

其逆命题也成立。

设 (1) 成立，并设 $\varepsilon > 0$。

选取 $\delta > 0$ 使得 $\omega_f((x_0 - \delta, x_0 + \delta)) < \varepsilon$。

于是

```math
\sup \{|f(x) - f(x_0)| : x \in (x_0 - \delta, x_0 + \delta)\} < \varepsilon,
```

从而当 $|x - x_0| < \delta$ 时就有 $|f(x) - f(x_0)| < \varepsilon$。

这意味着 $f$ 在 $x_0$ 处连续。

我们将以上内容总结为一条定理。

---
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> oscillation（振幅）$\omega_f(I)=\sup_{x,y\in I}|f(x)-f(y)|$ 的本质是「函数在区间 $I$ 上的最大波动幅度」。把这个「区间振幅」逐层缩小到一点，就得到点态振幅 $\omega_f(x_0)=\inf_{\delta>0}\omega_f((x_0-\delta,x_0+\delta))$。Theorem 6.25 告诉我们：$f$ 在 $x_0$ 连续当且仅当 $\omega_f(x_0)=0$——这个结论可以命名为 **「振幅归零法」**。它的直观非常自然：连续性要求当 $x$ 靠近 $x_0$ 时 $f(x)$ 靠近 $f(x_0)$，等价地说，在足够小的邻域内函数的波动幅度可以任意小。振幅归零法将 $\varepsilon$-$\delta$ 定义中的「存在性和任意性嵌套」转化为一个单一的极限式 $\inf_{\delta>0}\omega_f=0$，这是一个重大的技术简化——后面分析间断点集的拓扑性质时（Theorem 6.27/6.28），正是靠这个等价刻画「撬动」了整个证明。记住这个策略：当你需要将逐点性质转化为全局拓扑性质时，振幅常常是桥梁。
---

---
<!-- ===== 书页 259（PDF 页 25）===== -->
---
<span style="color:#7f8c8d">*Part006 · 书页 259 行内双语翻译*</span>

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">6.7 Oscillation and Continuity（振幅与连续性）</span>

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 6.25（定理 6.25）</span>

> <span style="color:#7f8c8d;">TBB §6.7, p.259</span>

设 $f$ 定义在区间 $I$ 上，且 $x_0 \in I$。则 $f$ 在 $x_0$ 处连续，当且仅当

```math
\inf_{\delta>0} \omega_f((x_0 - \delta, x_0 + \delta)) = 0.
```

定理陈述中的这个量十分重要，值得为它专门命名。

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">Definition 6.26（定义 6.26）</span>

> <span style="color:#7f8c8d;">TBB §6.7, p.259</span>

设 $f$ 定义在 $x_0$ 的一个邻域（neighborhood）内。量

```math
\omega_f(x_0) = \inf_{\delta>0} \omega_f((x_0 - \delta, x_0 + \delta))
```

<span style="color:#00838f">称为 $f$ 在 $x_0$ 处的 oscillation（振幅）。</span>

因此，Theorem 6.25（定理 6.25）表明：函数 $f$ 在点 $x_0$ 处连续，当且仅当 $\omega_f(x_0) = 0$。回到本节开头引入的那个函数，我们看到

```math
\omega_f(x) =
\begin{cases}
1/k, & \text{if } x = q_k,\\
0, & \text{if } x \in \mathbb{R} \setminus \mathbb{Q}.
\end{cases}
```

现在让我们看看 oscillation（振幅）这一概念与函数的连续点集（set of continuity points）之间有何关联。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 6.27（定理 6.27）</span>

> <span style="color:#7f8c8d;">TBB §6.7, p.259</span>

设 $f$ 定义在闭区间 $I$ 上（$I$ 可以是整个 $\mathbb{R}$）。设 $\gamma > 0$。则集合

```math
\{ x : \omega_f(x) < \gamma \}
```

是开集（open set），而集合

```math
\{ x : \omega_f(x) \geq \gamma \}
```

是闭集（closed set）。

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 设 $A = \{ x : \omega_f(x) < \gamma \}$，并取 $x_0 \in A$。我们希望找到 $x_0$ 的一个邻域 $U$，使得 $U \subset A$；也就是说，使得对所有 $x \in U$ 都有 $\omega_f(x) < \gamma$。
>
> 设 $\omega_f(x_0) = \alpha < \gamma$，并取 $\beta \in (\alpha, \gamma)$。由 Definition 6.26（定义 6.26）可推知，存在某个 $\delta > 0$，使得对一切 $u, v \in (x_0 - \delta, x_0 + \delta)$ 都有 $|f(u) - f(v)| \leq \beta$。
>
> 令 $U = (x_0 - \delta, x_0 + \delta)$，并取 $x \in U$。由于 $U$ 是开集，存在某个 $\delta_1 < \delta$，使得 $(x - \delta_1, x + \delta_1) \subset U$。于是
>
> ```math
> \omega_f(x) \leq \sup \{ |f(t) - f(s)| : t, s \in (x - \delta_1, x + \delta_1) \} \leq \sup \{ |f(u) - f(v)| : u, v \in U \} \leq \beta < \gamma,
> ```

<!-- XREF: Definition 6.26 → §6.7 p.259 -->
---
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Theorem 6.27 的证明策略可以命名为 **「振幅阈值分解法」**：对每个阈值 $\gamma>0$，把定义域按振幅是否小于 $\gamma$ 拆成两个互补集合 $A=\{x:\omega_f(x)<\gamma\}$ 和 $B=\{x:\omega_f(x)\ge\gamma\}$，然后分别证明 $A$ 是开集、$B$ 是闭集。证明 $A$ 为开集的核心手法是：在 $x_0\in A$ 处，取 $\omega_f(x_0)=\alpha<\gamma$ 和一个中间值 $\beta\in(\alpha,\gamma)$，利用振幅定义找到一个 $\delta$-邻域使该邻域内所有函数值波动不超过 $\beta$；然后对该邻域内任一点 $x$，「再缩一次」找更小的邻域，利用振幅的 sup 定义传递不等式，得出 $\omega_f(x)\le\beta<\gamma$。这个过程本质上是将「振幅小」这个性质从一点**传播**到整个邻域——是一种典型的开集传播论证（openness propagation argument）。这个技术在后文中至关重要：Theorem 6.28 正是利用 $\gamma=1/k$ 的阈值分解，把连续点集 $C_f$（即 $\omega_f=0$ 的点集）写成可数个开集的交。
---

---
<!-- ===== 书页 260（PDF 页 26）===== -->
---
<span style="color:#7f8c8d">*Part006 · 书页 260 行内双语翻译*</span>

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明，续接上页）.*

> 从而 $x \in A$。这就证明了 $A$ 是开集。由此进一步推出，$A$ 在 $I$ 中的补集（complement），即集合 $\{ x : \omega_f(x) \geq \gamma \}$，必为闭集。$\blacksquare$

我们将在下一小节中使用 oscillation（振幅）来回答一个关于函数连续点集性质的问题。

<span style="color:#7f8c8d;">*（习题 6.7.1–6.7.5 为练习区，按约定跳过，不收录。）*</span>

### <span style="color:#2471a3;">**[subsection]**</span> <span style="color:#c0392b">6.7.2 The Set of Continuity Points（连续点集）</span>

本节为高级内容（Advanced section），可以省略。

给定一个任意函数，我们如何刻画 $f$ 连续的那些点所构成的集合的性质？这个集合可以是任何集合吗？给定一个集合 $E$，我们又如何知道是否存在这样一个函数：它在 $E$ 的每一点都连续，而在不属于 $E$ 的每一点都不连续？
---

---
<!-- ===== 书页 261（PDF 页 27）===== -->
---
<span style="color:#7f8c8d">*Part006 · 书页 261 行内双语翻译*</span>

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">6.7 Oscillation and Continuity（振幅与连续性）</span>

我们在 Example 6.23（例 6.23）中看到：存在一个函数，其连续点集（set of continuity points）恰为无理数集。那么，能否存在一个函数，其连续点集恰为有理数集？通过对这类点集加以特征刻画（characterization），我们就能回答这个问题，以及其他关于函数结构的问题。

现在我们证明本节的主要结果，所用工具主要是 6.7.1 小节引入的 oscillation（振幅）概念。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 6.28（定理 6.28）</span>

> <span style="color:#7f8c8d;">TBB §6.7, p.261</span>

设 $f$ 定义在闭区间 $I$ 上（$I$ 可以是整个 $\mathbb{R}$）。则 $f$ 的连续点集 $C_f$ 是 Gδ 型（type $G_\delta$，即可数个开集的交集），而 $f$ 的间断点集（set of discontinuity points）$D_f$ 是 Fσ 型（type $F_\sigma$，即可数个闭集的并集）。反之，若 $H$ 是 Gδ 型集合，则存在定义在 $\mathbb{R}$ 上的函数 $f$，使得 $C_f = H$。

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 为证明第一部分，设 $f : I \to \mathbb{R}$。我们要证明集合
>
> ```math
> C_f = \{ x : \omega_f(x) = 0 \}
> ```
>
> 是 Gδ 型。对每个 $k \in \mathbb{N}$，令
>
> ```math
> B_k = \left\{ x : \omega_f(x) \ge \frac{1}{k} \right\}
> ```
>
> 由 Theorem 6.27（定理 6.27）可知，每个集合 $B_k$ 都是闭集。于是集合
>
> ```math
> B = \bigcup_{k=1}^{\infty} B_k
> ```
>
> 是 Fσ 型。由 Theorem 6.25（定理 6.25）知 $D_f = B$。因此 $C_f = I \setminus B$。既然 Fσ 集的补集（complement）是 Gδ 集，故 $C_f$ 是 Gδ 集。
>
> 为证明逆命题，设 $H$ 是 $\mathbb{R}$ 中任意一个 Gδ 型子集。则 $H$ 可表示为如下形式
>
> ```math
> H = \bigcap_{k=1}^{\infty} G_k
> ```
>
> 其中每个集合 $G_k$ 都是开集。不失一般性（without loss of generality），我们可以假设 $G_1 = \mathbb{R}$，并且对每个 $i \in \mathbb{N}$ 都有 $G_i \supset G_{i+1}$（请读者验证这一事实）。
>
> 设 $\{\alpha_k\}$ 与 $\{\beta_k\}$ 是两个正数序列，各自都收敛到零，并且满足
>
> ```math
> \alpha_k > \beta_k > \alpha_{k+1}
> ```
>
> 对所有 $k \in \mathbb{N}$ 成立。按下式定义一个函数 $f : \mathbb{R} \to \mathbb{R}$：
>
> ```math
> f(x) =
> \begin{cases}
> 0, & x \in H \\
> \alpha_k, & x \in (G_k \setminus G_{k+1}) \cap \mathbb{Q} \\
> \beta_k, & x \in (G_k \setminus G_{k+1}) \cap (\mathbb{R} \setminus \mathbb{Q})
> \end{cases}
> ```
>
> 我们要证明 $f$ 在 $H$ 的每一点连续，而在 $\mathbb{R} \setminus H$ 的每一点间断。
>
> 设 $x_0 \in H$，并设 $\varepsilon > 0$。选取 $n$ 使得 $\alpha_n < \varepsilon$。由于
>
> ```math
> x_0 \in H = \bigcap_{k=1}^{\infty} G_k,
> ```

---
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Theorem 6.28 是本节的「皇冠定理」，它回答了一个极具**设计感**的问题：**什么样的点集能成为某函数的连续点集？** 换句话说，如果我给你一个点集 $E\subseteq\mathbb{R}$，我能否构造一个函数，让它恰好在 $E$ 上连续、在其余点上间断？正向结论告诉我们：任何函数的连续点集 $C_f$ 必定是 Gδ 型（间断点集 $D_f$ 必定是 Fσ 型）。证明路线清晰如梯子：先用 Theorem 6.27 把「振幅 $\ge 1/k$」的点集 $B_k$ 识别为闭集，则 $D_f=\bigcup_k B_k$ 是 Fσ，取补即得 $C_f$ 为 Gδ。逆命题的构造更为精彩：给定任意 Gδ 集 $H=\bigcap_k G_k$，逐层用有理/无理赋值区分隶属层级，使得 $H$ 内点振幅为零（连续）、$H$ 外点振幅跳跃（间断）。推论立刻回答了一个经典悬念：**不存在一个函数恰好在有理数集上连续**——因为 $\mathbb{Q}$ 不是 Gδ 型（它是可数稠密集，而 Gδ 稠密集必为不可数/剩余集）。Theorem 6.28 的核心思想——连续点集与 Gδ/Fσ 的拓扑对应——是实分析从「逐点分析」走向「集合论分析」的里程碑。
---

---
<!-- ===== 书页 262（PDF 页 28）===== -->
---
<span style="color:#7f8c8d">*Part006 · 书页 262 行内双语翻译*</span>

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明，续接书页 261）.*

> 由此我们看到 $x_0 \in G_n$。集合 $G_n$ 是开集，所以存在 $\delta > 0$ 使得 $(x_0 - \delta, x_0 + \delta) \subset G_n$。根据 $f$ 在 $G_n$ 上的定义可知，对所有 $x \in (x_0 - \delta, x_0 + \delta)$ 都有
>
> ```math
> 0 \le f(x) \le \alpha_n < \varepsilon
> ```
>
> 于是当 $|x - x_0| < \delta$ 时
>
> ```math
> |f(x) - f(x_0)| = |f(x) - 0| = |f(x)| < \varepsilon
> ```
>
> 所以 $f$ 在 $x_0$ 处连续。
>
> 现在设 $x_0 \in \mathbb{R} \setminus H$。则存在 $k \in \mathbb{N}$ 使得 $x_0$ 属于集合 $G_k \setminus G_{k+1}$，从而 $f(x_0) = \alpha_k$ 或 $f(x_0) = \beta_k$。我们假设 $f(x_0) = \alpha_k$。若 $x_0$ 是 $G_k \setminus G_{k+1}$ 的 interior point（内点），则 $x_0$ 是集合
>
> ```math
> \{ x : x \in (G_k \setminus G_{k+1}) \cap (\mathbb{R} \setminus \mathbb{Q}) \} = \{ x : f(x) = \beta_k \}
> ```
>
> 的 limit point（聚点），因此 $f$ 在 $x_0$ 处不连续。
>
> 若 $x_0$ 是 $G_k \setminus G_{k+1}$ 的 boundary point（边界点），论证与此类似。再次假设 $f(x_0) = \alpha_k$。在任意接近 $x_0$ 处都有集合 $\mathbb{R} \setminus (G_k \setminus G_{k+1})$ 的点。在这些点上，$f$ 取集合
>
> ```math
> S = \{0\} \cup \bigcup_{i \neq k} \alpha_i \cup \bigcup_{j \neq k} \beta_j
> ```
>
> 中的值。这个集合唯一的聚点是零，因此 $S$ 是闭集。特别地，$\alpha_k$ 不是这个集合的聚点，也不属于这个集合。令 $\varepsilon$ 为点 $\alpha_k$ 到闭集 $S$ 的距离的一半，即令
>
> ```math
> \varepsilon = \frac{1}{2}\, d(\alpha_k, S).
> ```
>
> 在任意接近 $x_0$ 处都存在满足 $f(x) \in S$ 的点 $x$。对这样的点，
>
> ```math
> |f(x) - f(x_0)| = |f(x) - \alpha_k| > \varepsilon
> ```
>
> 所以 $f$ 在 $x_0$ 处不连续。$\blacksquare$

注意，Theorem 6.28（定理 6.28）回答了我们先前提出的一个问题：是否存在函数 $f$，它在 $\mathbb{Q}$ 上连续，而在 $\mathbb{R} \setminus \mathbb{Q}$ 的每一点都间断？答案是否定的，因为 $\mathbb{Q}$ 不是 Gδ 型集合。

<!-- page_028：习题 6.7.6、6.7.7 按约定跳过 -->
---

---
<!-- ===== 书页 263（PDF 页 29）===== -->
---
### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">6.8 Sets of Measure Zero（零测集）</span>

本节为 advanced section（进阶内容），可以略过。

在分析学中，一个集合可以在多种意义下被视为「small（小）」集合。
例如，Cantor set（康托集）在计数的意义下并不小：它是 uncountable（不可数的）。
它在另一种不同的意义下是小的：它是 nowhere dense（无处稠密）的，也就是说，根本不存在任何区间使它在其中稠密。
现在我们转向康托集可以被视为小的另一种方式：它具有「长度为零」的性质。

<span style="color:#2471a3;">**[example]**</span> **Example 6.29（例 6.29）**

> <span style="color:#7f8c8d;">TBB §6.8, p.263</span>

> 假设我们希望测量康托集的「长度」。
> 由于康托集相当怪异，我们或许转而考察那些在构造中被移除的区间序列。
> 为区间赋予长度的含义并无困难：区间 $(a, b)$ 的长度是 $b - a$。
> 在康托集的构造中被移除的区间，其总长度是多少？
> 从区间 $[0, 1]$ 出发，我们先移除一个长度为 $1/3$ 的中间三分之一区间，再移除两个长度为 $1/9$ 的中间三分之一区间，依此类推，于是在第 $n$ 阶段我们移除 $2^{n-1}$ 个长度为 $3^{-n}$ 的区间。
> 所有这些被移除区间的长度之和为
>
> ```math
> 1/3 + 2(1/9) + 4(1/27) + \cdots = 1/3\left(1 + 2/3 + (2/3)^2 + (2/3)^3 + \cdots \right) = 1.
> ```
>
> 从区间 $[0, 1]$ 来看，我们似乎已经移除了全部长度。
> 所剩下的康托集必然具有长度零。

这种计算长度的方法有其优点，但它并非我们在此希望采用的方法。
另一种「测量」康托集长度的方法是考察在每个阶段所剩余的长度。
在第一阶段，康托集包含于并集 $[0, 1/3] \cup [2/3, 1]$ 之内，该并集的长度为 $2(1/3)$。
在下一阶段，它包含于四个区间的并集之内，总长度为 $4(1/9)$。
类似地，在第 $n$ 阶段，康托集包含于 $2^n$ 个区间的并集之内，每个区间的长度为 $3^{-n}$。
所有这些区间的长度之和为 $(2/3)^n$，当 $n$ 增大时它趋于零。
因此，与之前一样，我们似乎应当把长度零赋予康托集。

我们把该例题的第二种方法转化为一个定义，说明一个集合在什么意义下具有 measure zero（零测度）。
「measure（测度）」是描述那些未必是区间的集合之「长度」的技术术语。
在该例题中我们使用了闭区间，而在我们的定义中则采用开区间。
两者并无差别（见 Exercise 6.8.13）。
在该例题中我们用有限个区间的序列覆盖康托集，而在我们的定义中则采用无限序列。
对于康托集，两者没有差别；但对于其他集合（无界或非闭的集合）则有差别。

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">Definition 6.30（定义 6.30）</span>

> <span style="color:#7f8c8d;">TBB §6.8, p.263</span>

设 $E$ 是实数集。若对每个 $\varepsilon > 0$，都存在一个有限或无限序列

```math
(a_1, b_1), (a_2, b_2), (a_3, b_3), (a_4, b_4), \ldots
```

（下接书页 264）

---
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> measure zero（零测度）是分析学中度量集合「小」的第三种尺度——你已经学过前两种：计数意义上的「小」（可数 vs 不可数）和范畴意义上的「小」（first category vs second category / Baire 纲定理）。零测集的核心直觉是：集合 $E$ 可以被总长度任意小的开区间序列覆盖。换句话说，不管你要求多苛刻的误差 $\varepsilon>0$，我都能找到一列开区间，使它们的长度总和 $\le\varepsilon$，却仍然盖住 $E$。这直接打包了你已有的两个脚手架：Example 6.31 用「$\varepsilon/N$ 平均分配」证明有限集零测；Example 6.32 用「$\varepsilon/2^{i+1}$ 几何衰减」证明可数集零测——后者的技巧（给第 $i$ 个点分配 $\varepsilon/2^{i+1}$ 长度，利用 $\sum 2^{-i}=1$ 收敛）是分析学中的「万能覆盖模板」。零测集的可数并仍为零测（Theorem 6.34）进一步表明：零测集类比可数集类更大，但仍然对可数并封闭——这是测度论中 $\sigma$-代数框架的雏形。
---

---
<!-- ===== 书页 264（PDF 页 30）===== -->
---
#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">Definition 6.30（定义 6.30，续）</span>

> <span style="color:#7f8c8d;">TBB §6.8, p.263–264</span>

（承上书页 263）这些区间为开区间，它们组成一个覆盖集合 $E$ 的序列，使得

```math
\sum_{k=1}^{\infty} (b_k - a_k) \leq \varepsilon.
```

则称 $E$ 具有零测度。

<span style="color:#2471a3;">**[note]**</span> **Note（注）**
> 在零测集的定义中，如果我们坚持采用无限区间序列、不允许有限序列，定义会改变吗？
> 假设开区间序列 $(a_1, b_1), (a_2, b_2), \ldots, (a_N, b_N)$ 覆盖集合 $E$，使得

> ```math
> \sum_{k=1}^{N} (b_k - a_k) < \varepsilon/2.
> ```

> 那么为满足定义，我们可以再加入一些额外区间，这些区间的长度总计不超过 $\varepsilon/2$。
> 例如，取 $(a_{N+p}, b_{N+p}) = (0, \varepsilon/2^{p+1})$，其中 $p = 1, 2, 3, \ldots$。
> 于是

> ```math
> \sum_{k=1}^{\infty} (b_k - a_k) = \sum_{k=1}^{N} (b_k - a_k) + \sum_{p=1}^{\infty} \varepsilon/2^{p+1} < \varepsilon.
> ```

> 因此，即使我们当初就要求用无限覆盖，这个定义也不会改变。

下面是一些零测集的例子。

<span style="color:#2471a3;">**[example]**</span> **Example 6.31（例 6.31）**

> <span style="color:#7f8c8d;">TBB §6.8, p.264</span>

> 每个 finite set（有限集）都具有零测度。
> 空集很容易处理。
> 若 $E = \{x_1, x_2, \ldots, x_N\}$ 且 $\varepsilon > 0$，则区间序列

> ```math
> \left( x_i - \frac{\varepsilon}{2N}, \; x_i + \frac{\varepsilon}{2N} \right), \quad i = 1, 2, 3, \ldots, N
> ```

> 覆盖集合 $E$，且所有这些区间的长度之和为 $\varepsilon$。

<span style="color:#2471a3;">**[example]**</span> **Example 6.32（例 6.32）**

> <span style="color:#7f8c8d;">TBB §6.8, p.264</span>

> 每个无限的 countable（可数的）集合都具有零测度。
> 若 $E = \{x_1, x_2, \ldots\}$ 且 $\varepsilon > 0$，则区间序列

> ```math
> \left( x_i - \frac{\varepsilon}{2^{i+1}}, \; x_i + \frac{\varepsilon}{2^{i+1}} \right), \quad i = 1, 2, 3, \ldots
> ```

> 覆盖集合 $E$，并且由于

> ```math
> \sum_{k=1}^{\infty} 2\left(\frac{\varepsilon}{2^{k+1}}\right) = \sum_{k=1}^{\infty} \varepsilon 2^{-k} = \varepsilon,
> ```

> 所有这些区间的长度之和为 $\varepsilon$。

<!-- XREF: Example 6.31 → §6.8 p.264 -->
---

---
<!-- ===== 书页 265（PDF 页 31）===== -->
---
### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">6.8 Sets of Measure Zero（零测集）</span>

<span style="color:#2471a3;">**[example]**</span> **Example 6.33（例 6.33）** Cantor set（康托集）具有 measure zero（零测度）。

> <span style="color:#7f8c8d;">TBB §6.8, p.265</span>

设 $\varepsilon > 0$。

选取 $n$ 使得 $(2/3)^n < \varepsilon$。

那么，康托集构造中的第 $n$ 阶段区间给出 $2^n$ 个闭区间，每个的长度为 $(1/3)^n$。

这就用总长度为 $(2/3)^n$（小于 $\varepsilon$）的 $2^n$ 个闭区间覆盖了康托集。

如果闭区间令你困扰（定义要求的是开区间），可参见练习 6.8.13，或按如下方式论证。

由于 $(2/3)^n < \varepsilon$，存在正数 $\delta$ 使得

```math
(2/3)^n + \delta < \varepsilon.
```

将每个闭区间放大成略大的开区间，但每个区间长度的调整仅限于使全部 $2^n$ 个闭区间长度总和的增加不超过 $\delta$。

所得的开区间族同样覆盖康托集，且这些区间的长度之和小于 $\varepsilon$。

$\blacksquare$

零测集最根本的性质之一，在于这类集合的序列如何复合。

我们回顾：任何 countable（可数的）集合序列的并集也是可数的。

现在我们证明：任何零测集序列的并集也是零测集。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 6.34（定理 6.34）</span>

> <span style="color:#7f8c8d;">TBB §6.8, p.265</span>

设 $E_1, E_2, E_3, \ldots$ 是一列零测集。

那么，由该序列中所有集合取并集而成的集合 $E$ 也是零测度的。

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 设 $\varepsilon > 0$。
>
> 我们将构造 $E$ 的一个覆盖，它由一列总长度小于 $\varepsilon$ 的开区间组成。
>
> 由于 $E_1$ 具有零测度，存在一列开区间 $(a_{11}, b_{11}), (a_{12}, b_{12}), (a_{13}, b_{13}), (a_{14}, b_{14}), \ldots$ 覆盖集合 $E_1$，且这些区间的长度之和小于 $\varepsilon/2$。
>
> 由于 $E_2$ 具有零测度，存在一列开区间 $(a_{21}, b_{21}), (a_{22}, b_{22}), (a_{23}, b_{23}), (a_{24}, b_{24}), \ldots$ 覆盖集合 $E_2$，且这些区间的长度之和小于 $\varepsilon/4$。
>
> 一般地，对每个 $k = 1, 2, 3, \ldots$，存在一列开区间 $(a_{k1}, b_{k1}), (a_{k2}, b_{k2}), (a_{k3}, b_{k3}), (a_{k4}, b_{k4}), \ldots$ 覆盖集合 $E_k$，且这些区间的长度之和小于 $\varepsilon/2^k$。
>
> 所有这些区间的全体可排列成一个单一的开区间序列，它覆盖序列 $\{E_k\}$ 之并集中的每一点。
>
> 这个大序列中所有区间的长度之和小于 $\varepsilon/2 + \varepsilon/4 + \varepsilon/8 + \cdots = \varepsilon$。
>
> 由此得出 $E$ 具有零测度。$\blacksquare$

让我们再次回到康托集的情形。

对每个 $\varepsilon > 0$，我们都能选取总长度小于 $\varepsilon$ 的有限个开区间来覆盖它。

但并非对所有零测集都如此。

例如，实数线上全体有理数的集合是可数的，因而也是零测度的。

---
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Cantor 集是实分析中反复登场的「反例之王」：你已在 6.5 节知道它是不可数的 nowhere dense 完备集，本节又揭示它还具有 measure zero。这就制造了一个深刻的现象——**一个集合可以在计数意义上「大」（不可数），但在测度意义上「小」（零测）**。三种「小」的尺度（可数、第一纲、零测）彼此独立、互不蕴含，这是实分析最迷人的结构之一。Theorem 6.34 的证明策略可以命名为 **「ε/2^k 分层覆盖法」**：对第 $k$ 个零测集 $E_k$，分配误差预算 $\varepsilon/2^k$，找到覆盖它的开区间序列使长度总和 $\le\varepsilon/2^k$；然后对所有 $k$ 取可数并——总预算 $\sum_{k=1}^\infty \varepsilon/2^k=\varepsilon$ 正好收敛，精妙地利用了调和级数的几何衰减。这个证明模式（逐层分配预算→可数汇总→收敛级数）与 Example 6.32 中覆盖可数集的手法本质同构，是实分析中最常用的「预算分配论证」（budget allocation argument）。最后做个预告：零测集在 Lebesgue 积分理论（Lebesgue 1902, *Intégrale, longueur, aire*）中扮演核心角色——Lebesgue 积分的「几乎处处」（almost everywhere）概念正是建立在零测集上：若一个性质在除去某个零测集之外的所有点成立，就说它几乎处处成立。Riemann 积分对间断点的容忍度有限（间断点集必须是零测的——这是 Lebesgue 可积性准则），而 Lebesgue 积分将这一思想彻底系统化。
---

---
<!-- ===== 书页 266（PDF 页 32）===== -->
---
（续上页）任何有限个区间的集合都必然无法覆盖那个集合，事实上连接近覆盖全部有理数都做不到。

对什么样的集合才能选取长度很小的有限覆盖呢？

答案是：对零测度的 compact sets（紧集）可以做到。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 6.35（定理 6.35）</span>

> <span style="color:#7f8c8d;">TBB §6.8, p.266</span>

设 $E$ 是零测度的紧集。

则对每个 $\varepsilon > 0$，存在有限个开区间

```math
(a_1, b_1), (a_2, b_2), (a_3, b_3), (a_4, b_4), \ldots, (a_N, b_N)
```

覆盖集合 $E$，且

```math
\sum_{k=1}^{N} (b_k - a_k) < \varepsilon.
```

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 由于 $E$ 具有零测度，当然可以选取一列开区间 $(a_1, b_1), (a_2, b_2), (a_3, b_3), (a_4, b_4), \ldots$ 覆盖集合 $E$，且 $\sum_{k=1}^{\infty} (b_k - a_k) < \varepsilon$。
>
> 但我们怎样才能把这个集合缩减为仍然覆盖集合 $E$ 的有限集合呢？
>
> 如果你学过 Heine–Borel theorem（Heine–Borel 定理）（定理 4.33），你就知道怎么做。
>
> 这里我们将改述一个使用 Bolzano–Weierstrass theorem（Bolzano–Weierstrass 定理）的证明。
>
> 我们断言：可以找到整数 $N$，使得 $E$ 的所有点都位于区间 $(a_1, b_1), (a_2, b_2), (a_3, b_3), (a_4, b_4), \ldots, (a_N, b_N)$ 之一中。
>
> 这将证明该定理。
>
> 我们用反证法（proof by contradiction）来证明这一点。
>
> 若并非如此，则对每个整数 $k = 1, 2, 3, \ldots$，我们必能找到一点 $x_k \in E$，但 $x_k$ 不属于区间 $(a_1, b_1), (a_2, b_2), \ldots, (a_k, b_k)$ 中的任何一个。
>
> 由于 $E$ 有界，序列 $\{x_k\}$ 是有界的。
>
> 由 Bolzano–Weierstrass 定理，该序列有收敛子序列 $\{x_{n_j}\}$。
>
> 设 $z$ 是这一收敛子序列的极限。
>
> 由于 $E$ 是闭集，$z$ 属于 $E$。
>
> 原来的区间序列覆盖整个 $E$，所以必有一个区间 $(a_M, b_M)$ 包含 $z$。
>
> 对足够大的 $j$，点 $x_{n_j}$ 也属于 $(a_M, b_M)$。
>
> 但这是不可能的，因为当 $n_j \ge M$ 时 $x_{n_j}$ 不能属于区间 $(a_M, b_M)$。
>
> 既然矛盾出现，证明完成。$\blacksquare$

<!-- page_032：末尾为 Exercises 6.8.1–6.8.2 习题区，按约定跳过 -->

---
> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Theorem 6.35 揭示了紧性（compactness）与零测度的一个精妙交互：对于零测的紧集，无限覆盖可以「压缩」成有限覆盖。证明中使用 Bolzano–Weierstrass 定理的反证法值得细品：假设不存在有限子覆盖，则对每个 $k$ 可选取 $x_k\in E$ 不属于前 $k$ 个区间——由此构造有界序列→收敛子序列→极限 $z\in E$→$z$ 必属于某个 $(a_M,b_M)$→对充分大的 $n_j\ge M$，$x_{n_j}$ 也不得不落入 $(a_M,b_M)$，与构造矛盾。这个论证本质上是 Heine–Borel 定理的另一条证明路线。如果回到你的已知工具：你学过 Bolzano–Weierstrass（有界序列必有收敛子序列），而紧集的 Heine–Borel 刻画（$\mathbb{R}$ 中紧 ⇔ 有界闭）正好是 Theorem 4.33。这里的核心教训是：紧集迫使「无穷覆盖」退化为「有限覆盖」——这为后续测度论中「紧集的正则性」（regularity）概念埋下伏笔。
---

---
<!-- ===== 书页 271（PDF 页 37）===== -->
---
> Part006 · 第 7 章 · 书页 271 行内双语翻译

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Chapter 7 Differentiation（第 7 章 微分）</span>

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">7.1 Introduction（导言）</span>

微积分课程成功地传达了导数（derivative）是什么这一概念，学生们也在导数的计算及其应用中培养出许多技术性技能。

我们将重新回到导数这一主题，但目标有所不同。

现在我们希望看得更深一些，去理解该理论赖以发展的基础。

本章的大部分内容看上去是对导数主题的复习，只不过现在更注意细节，而较少关注应用。

不过，某些更高级的材料将是全新的。

我们从源头开始，即从导数理论的初步知识（rudiments）讲起。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">7.2 The Derivative（导数）</span>

设 $f$ 是定义在区间 $I$ 上的函数，并设 $x_0$ 与 $x$ 为 $I$ 中的点。

考虑由点 $x_0$ 与 $x$ 确定的差商（difference quotient）：

```math
\frac{f(x)-f(x_0)}{x-x_0}, \qquad (1)
```

它表示 $f$ 在以 $x$ 与 $x_0$ 为端点的区间上的平均变化率。

在图 7.1 中，这个差商表示由点 $(x,f(x))$ 与 $(x_0,f(x_0))$ 确定的弦（chord）——即割线（secant line）——的斜率。

同一幅图还可作物理上的解释。

若 $f(x)$ 表示一个在直线上运动的点自某固定时刻 $x_0$ 起所移动的距离，那么 $f(x)-f(x_0)$ 就表示该点移动的（净）距离。

<span style="color:#7f8c8d">*（本句跨页，其余部分续于书页 272。）*</span>

<span style="color:#7f8c8d">*Figure 7.1（图 7.1）：由 $(x,f(x))$ 与 $(x_0,f(x_0))$ 确定的弦。*</span>
---
> <span style="color:#1e8449;">**[note] Note（译者注）：差商→极限两步法——从平均速度到瞬时速度的认知跃迁**</span>

本章开头用两种语言同时引入导数：几何的「割线斜率→切线斜率」与物理的「平均速度→瞬时速度」。这不是修辞并列，而是深层的认知锚固——你在高等数学里已经用 $(f(x)-f(x_0))/(x-x_0)$ 算过无数次导数，但当时你可能只把它当作一个「操作流程」：写差商、消去、取极限。TBB 在这里做的第一件事，是把差商本身当作分析对象：它不只是计算中间步骤，而是首先回答「这个比值在说什么」——它度量的是函数在以 $x$ 与 $x_0$ 为端点的区间上的平均变化率（average rate of change）。🎥 *Colding 在视频中讲解导数定义时强调*: "This quotient here is usually called the difference quotient. And it's always, of course, when you form this difference quotient, it's always assumed, obviously, that x is not equal to x0 so that the denominator makes sense."（翻译：这个商通常被称为差商。当然，在构造这个差商时，我们总是默认 $x$ 不等于 $x_0$，这样分母才有意义。）注意「分母有意义」这句话：它提醒我们差商是一个代数对象，在 $x = x_0$ 处本身就是无定义的——导数的极限定义正是在处理这个无定义点的「逼近行为」。这一点与你学过的 MIT 6.042J 离散数学中序列极限的 $\epsilon$-$N$ 定义精神完全一致：我们不是在「代入」$x=x_0$，而是在观察 $x$ 越来越接近 $x_0$ 时差商的趋势。从高等数学的「公式操作」过渡到实分析的「极限存在性判定」，这是本章第一个真正的认知跃迁。

---
---

---
<!-- ===== 书页 272（PDF 页 38）===== -->
---
> Part006 · 第 7 章 · 书页 272 行内双语翻译

（接前页）即该点在时间区间 $[x_0,x]$ 内移动的（净）距离；而差商 (1) 就表示该时间区间内的平均速度（average velocity）。

现在假设我们固定 $x_0$，并让 $x$ 趋近于 $x_0$。

我们在初等微积分中学到：若

```math
\lim_{x\to x_0}\frac{f(x)-f(x_0)}{x-x_0}
```

存在，则该极限表示函数 $f$ 的图形在点 $(x_0,f(x_0))$ 处切线（tangent line）的斜率。

在运动的背景下，该极限表示时刻 $x_0$ 的瞬时速度。

导数起源于几何与运动物理学中的这两种解释，但如今已完全超越它们。

导数在数学与科学的几乎每一个分支中都有应用。

我们将研究导数的结构，但对计算与应用的关注将少于我们在微积分课程中所见。

现在我们希望理解这一概念本身，并弄清楚它为何具有微积分的众多计算与应用所使用的那种性质。

### <span style="color:#2471a3;">**[subsection]**</span> <span style="color:#c0392b">7.2.1 Definition of the Derivative（导数的定义）</span>

我们从一条熟悉的定义开始。

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">Definition 7.1（定义 7.1）</span>

> <span style="color:#7f8c8d;">TBB §7.2, p.272</span>

设 $f$ 定义在区间 $I$ 上，且 $x_0\in I$。

$f$ 在 $x_0$ 处的导数，记作 $f'(x_0)$，定义为

```math
f'(x_0)=\lim_{x\to x_0}\frac{f(x)-f(x_0)}{x-x_0}, \qquad (2)
```

只要该极限存在或是无穷大。

若 $f'(x_0)$ 是有限的，我们就说 $f$ 在 $x_0$ 处可微（differentiable）。

若 $f$ 在集合 $E\subset I$ 的每一点处都可微，我们就说 $f$ 在 $E$ 上可微。

当 $E$ 就是整个 $I$ 时，我们便简单地说 $f$ 是可微函数。

<span style="color:#2471a3;">**[note]**</span> **Note（注意）.** 我们允许无穷导数，它们确实在许多研究中发挥作用。

但「可微」始终指有限导数。

通常「导数存在」这一说法也意味着该导数是有限的。

<span style="color:#2471a3;">**[example]**</span> **Example 7.2（例 7.2）**

> <span style="color:#7f8c8d;">TBB §7.2, p.272</span>

设 $f(x)=x^2$ 定义在 $\mathbb{R}$ 上，并设 $x_0\in\mathbb{R}$。

若 $x\in\mathbb{R}$ 且 $x\neq x_0$，则

```math
\frac{f(x)-f(x_0)}{x-x_0}=\frac{x^2-x_0^2}{x-x_0}=\frac{(x-x_0)(x+x_0)}{(x-x_0)}.
```

由于 $x\neq x_0$，最后一个表达式等于 $x+x_0$，因此

```math
\lim_{x\to x_0}\frac{f(x)-f(x_0)}{x-x_0}=\lim_{x\to x_0}(x+x_0)=2x_0,
```

这就为函数 $f(x)=x^2$ 确立了公式 $f'(x_0)=2x_0$。　$\blacksquare$

---
> <span style="color:#1e8449;">**[note] Note（译者注）：Definition 7.1——为什么必须用极限，而不能说「瞬时变化率」**</span>

Definition 7.1 的表述看似与你在大一高数中学过的完全一样：$f'(x_0)=\lim_{x\to x_0}\frac{f(x)-f(x_0)}{x-x_0}$。但 TBB 紧接着加了一条你在大一可能从未注意过的细节：「只要该极限存在或是无穷大（infinite）」。然后立刻澄清：「若 $f'(x_0)$ 是有限的，我们就说 $f$ 在 $x_0$ 处可微（differentiable）」——这说明本书明确区分了「导数存在（含无穷）」与「可微（仅限有限）」。为什么要在定义层面做这种细分？因为「无穷导数」对应的是切线垂直于 $x$ 轴的情形（如 $f(x)=\sqrt[3]{x}$ 在 $x_0=0$ 处），它在几何上有意义，但在代数上不能参与后续的和/积/链式法则运算。🎥 *Colding 在视频中说*: "If this limit here, as x goes to x0, if this exists, then we say that the function f is differentiable at x0. And the limit is called the derivative of f at x0."（翻译：如果当 $x$ 趋于 $x_0$ 时这个极限存在，我们就说 $f$ 在 $x_0$ 处可微，这个极限就称为 $f$ 在 $x_0$ 处的导数。）注意 Colding 把「极限存在」等同于「可微」，隐去了无穷导数的情形——这正是初等微积分教学的典型简化。TBB 比视频更精细：极限允许无穷，但可微要求有限。你需要同时适应两种口径：Colding 的课堂语言（省略边界情形以聚焦核心）和 TBB 的严格文本（包含边界情形以完备化理论）。从构建主义的角度看，这个区分恰好帮你理解：为什么实分析教材要比微积分教材「啰嗦」——因为在严格理论中，「导数存在」和「可微」不是同义词。

---
---

---
<!-- ===== 书页 273（PDF 页 39）===== -->
---
### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">7.2 The Derivative（导数）</span>

我们花一点时间来澄清定义：当区间 $I$ 包含其中一个或全部两个端点时，定义应如何理解。
设 $I = [a, b]$。
对于 $x_0 = a$（或 $x_0 = b$），式 (2) 中的极限只是一个 one-sided（单侧）极限，即 unilateral（单边）极限。
函数 $f$ 只在 $[a, b]$ 上有定义，因此我们不能考虑该区间之外的点。

这又把我们引向另一点。
有可能出现这样的情况：一个在 $x_0$ 处不可微（not differentiable）的函数，却在 $x_0$ 的某一侧满足式 (2) 的要求。
这意味着当 $x$ 从那一侧趋于 $x_0$ 时，式 (2) 中的极限存在。
我们给出一个形式化定义。

#### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">Definition 7.3（定义 7.3）</span>

> <span style="color:#7f8c8d;">TBB §7.2, p.273</span>

设 $f$ 定义在区间 $I$ 上，且 $x_0 \in I$。
$f$ 在 $x_0$ 处的 right-hand derivative（右导数），记作 $f'_+(x_0)$，是如下极限：

```math
f'_+(x_0) = \lim_{x \to x_0+} \frac{f(x) - f(x_0)}{x - x_0},
```

只要该单侧极限存在或为无穷（infinite）。
类似地，$f$ 在 $x_0$ 处的 left-hand derivative（左导数）$f'_-(x_0)$ 是极限：

```math
f'_-(x_0) = \lim_{x \to x_0-} \frac{f(x) - f(x_0)}{x - x_0}.
```

注意，若 $x_0$ 是 $I$ 的 interior point（内点），则 $f'(x_0)$ 存在当且仅当 $f'_+(x_0) = f'_-(x_0)$。<span style="color:#7f8c8d">（参见 Exercise 7.2.8。）</span>

<span style="color:#2471a3;">**[example]**</span> **Example 7.4（例 7.4）**

> <span style="color:#7f8c8d;">TBB §7.2, p.273</span>

在 $\mathbb{R}$ 上取 $f(x) = |x|$。
我们考察 $f$ 在 $x_0 = 0$ 处的可微性（differentiability）。
差商 (1) 变成：

```math
\frac{f(x) - f(0)}{x - 0} = \frac{|x|}{x} = \begin{cases} 1, & \text{if } x > 0 \\ -1, & \text{if } x < 0. \end{cases}
```

因此

```math
f'_+(0) = \lim_{x \to 0+} \frac{|x|}{x} = 1
```

而

```math
f'_-(0) = \lim_{x \to 0-} \frac{|x|}{x} = -1.
```

该函数在 $x_0 = 0$ 处的右导数与左导数不同，因此在 $x_0 = 0$ 处不可微。

<span style="color:#2471a3;">**[example]**</span> **Example 7.5（例 7.5）（一个「trapping principle（夹逼原理）」）**

> <span style="color:#7f8c8d;">TBB §7.2, p.273</span>

设 $f$ 是定义在零点的一个 neighborhood（邻域）$I$ 上的任意函数。
设对所有 $x \in I$，$f$ 都满足不等式 $|f(x)| \le x^2$。
于是，$f$ 的图形被「夹在（trapped）」抛物线 $y = x^2$ 与 $y = -x^2$ 之间。
特别地，$f(0) = 0$。
对 $x_0 = 0$ 计算的差商变成：

```math
\frac{f(x) - f(0)}{x - 0} = \frac{f(x)}{x},
```

由此我们计算：

```math
\left| \frac{f(x)}{x} \right| \le \left| \frac{x^2}{x} \right| = |x|.
```

<!-- XREF: Example 7.4 → §7.2 p.273 -->
---
> <span style="color:#1e8449;">**[note] Note（译者注）：左右导数——单侧极限如何自然产生「不可微」的诊断工具**</span>

Definition 7.3 引入了右导数 $f'_+(x_0)$ 和左导数 $f'_-(x_0)$。这与第 4 章的单侧极限一脉相承：当 $x_0$ 是区间 $I$ 的内点（interior point）时，$f'(x_0)$ 存在当且仅当 $f'_+(x_0)=f'_-(x_0)$。Example 7.4（$f(x)=|x|$ 在 $x_0=0$）是大一高数中的经典反例，但 TBB 的处理方式有所不同：不是先告诉你「绝对值函数在零点不可导」，而是让你亲手算出 $f'_+(0)=1$、$f'_-(0)=-1$，然后因为两者不相等而判定不可微。这个「计算→比较→判定」的三步流程，本质上就是实分析处理可微性的标准模板：你不必直接攻击那个双侧极限，而是将问题分解为两个单侧极限分别计算。🎥 *Colding 在视频中讲解 $|x|$ 的例子时指出*: "There are both cases where it's 1 and cases where it's minus 1."（翻译：既有等于 1 的情形，也有等于 -1 的情形。）这个口语化的表达恰好对应了左右导数不相等的本质。此外请注意：当 $x_0$ 是区间端点（如 $[a,b]$ 的 $a$ 或 $b$）时，Definition 7.1 中的极限自动退化为单侧极限——这不是定义的漏洞，而是定义的自然延伸。你在学 Strang 线性代数时已经习惯了「定义在特定集合上的运算」，这里同理：导数的定义域始终受限于函数本身的定义域。

---
---

---
<!-- ===== 书页 274（PDF 页 40）===== -->
---
<span style="color:#7f8c8d">**Figure 7.2（图 7.2）**：一个被夹在 $x^2$ 与 $-x^2$ 之间的函数。</span>

因此

```math
\lim_{x \to 0} \left| \frac{f(x)}{x} \right| \le \lim_{x \to 0} |x| = 0.
```

从而

```math
\lim_{x \to 0} \frac{f(x)}{x} = 0.
```

结果是 $f'(0) = 0$。
图 7.2 展示了这一原理。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Higher-Order Derivatives（高阶导数）</span>

当一个函数 $f$ 在 $I$ 上可微时，它的导数 $f'$ 也可能可微。
若是这种情况，函数 $f'' = (f')'$ 被称为函数 $f$ 的 second derivative（二阶导数）。
归纳地，我们可以定义所有阶的导数：$f^{(n+1)} = (f^{(n)})'$（只要 $f^{(n)}$ 可微）。
当 $n$ 较小时，习惯上使用便捷记号：用 $f''$ 表示 $f^{(2)}$，用 $f'''$ 表示 $f^{(3)}$，等等。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Notation（记号）</span>

为函数 $f$ 的导数配备其他记号是有用的。
常见的记号是 $\frac{df}{dx}$ 与 $\frac{dy}{dx}$（当函数表为 $y = f(x)$ 的形式时）。
另一个有用的记号是 $Df$。
这些替代记号连同它们的细微变体对各类计算都很有用。
你无疑熟悉这类用法——使用 chain rule（链式法则）时书写

```math
\frac{dy}{dx} = \frac{dy}{du} \frac{du}{dx}
```

的便捷，或者把 $D$ 视为 operator（算子）来求解线性微分方程。
记号有时可能很重要。
试想，例如用罗马数字 (CIV)(XC) 去做像 $(104)(90)$ 这样简单的乘法运算会有多困难！

> 本页习题区（Exercise 7.2.1 及其 Note 提示）按约定跳过。
---
> <span style="color:#1e8449;">**[note] Note（译者注）：Trapping Principle——用已知函数夹逼未知函数导数的技巧**</span>

Example 7.5 展示了一个你可能不熟悉的技巧：如果对所有 $x$ 都有 $|f(x)|\le x^2$，那么 $f'(0)=0$。这个结论不需要知道 $f$ 的具体形式——仅凭不等式的夹逼就足以推出导数。证明的关键一步是 $|f(x)/x|\le |x|$，然后两边取极限由夹逼定理得到 $f(x)/x \to 0$。这个技巧与你在 CSAPP 中学到的「信息隐藏」有类似的哲学：我们不需要知道函数内部的全部细节，只要上界和下界在零点「捏合」得足够紧，导数就被唯一确定。注意这里用到了绝对值版本的夹逼：$|a_n|\le b_n$ 且 $b_n\to 0$ 则 $a_n\to 0$——这来自第 4 章的极限定理。TBB 把这个例子称为「trapping principle（夹逼原理）」，图像是函数被夹在 $y=x^2$ 与 $y=-x^2$ 之间——抛物线在原点相切，迫使 $f$ 在原点也只能有水平切线。

---
---

---
<!-- ===== 书页 276（PDF 页 42）===== -->
---
<span style="color:#7f8c8d">*Part006 · 书页 276 行内双语翻译*</span>

### <span style="color:#2471a3;">**[subsection]**</span> <span style="color:#c0392b">7.2.2 Differentiability and Continuity（可微性与连续性）</span>

一个 continuous function（连续函数）不必是 differentiable（可微）的（见 Example 7.4（例 7.4）），但反之成立。

每个 differentiable function（可微函数）都是连续的。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 7.6（定理 7.6）</span>

> <span style="color:#7f8c8d;">TBB §7.2, p.276</span>

设 $f$ 在 $x_0$ 的某个 neighborhood（邻域）$I$ 上有定义。

若 $f$ 在 $x_0$ 处可微，则 $f$ 在 $x_0$ 处连续。

> <span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*
>
> 只需证明 $\lim_{x \to x_0}(f(x) - f(x_0)) = 0$。
>
> 对于 $x \neq x_0$，有
>
> $f(x) - f(x_0) = \frac{f(x) - f(x_0)}{x - x_0}(x - x_0)$。
>
> 现在
>
> $\lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0} = f'(x_0)$，
>
> 且 $\lim_{x \to x_0}(x - x_0) = 0$。
>
> 于是我们得到
>
> $\lim_{x \to x_0}(f(x) - f(x_0)) = (f'(x_0))(0) = 0$，
>
> 这是由极限的 product rule for limits（乘积法则）得出的。$\blacksquare$

我们可以在两个方向上使用这个定理。

若我们知道某个函数在某点处有 discontinuity（不连续点），那么立刻知道它在那一点不存在 derivative（导数）。

另一方面，若我们已能通过某种方式确定某函数在某点可微，那么我们自动知道该函数在该点也必然连续。

---
> <span style="color:#1e8449;">**[note] Note（译者注）：Theorem 7.6 的证明——为什么可微蕴含连续只需要一行代数恒等式**</span>

Theorem 7.6（可微 ⇒ 连续）的证明结构极其简洁：$f(x)-f(x_0) = \frac{f(x)-f(x_0)}{x-x_0} \cdot (x-x_0)$，然后两边取极限，左边是 $f'(x_0)$，右边第二个因子是 $0$，由极限的乘积法则得到 $0$。这个证明的核心是一个代数恒等式——把「函数值的差」写成「差商 × 自变量差」——这本质上是对导数定义中差商公式的简单移项。🎥 *Colding 在视频中明确点出这个逻辑关系*: "So in other words, being differentiable is stronger than being continuous. In a minute, we will see an example of something that's continuous but not differentiable."（翻译：换句话说，可微是比连续更强的性质。稍后我们会看到一个连续但不可微的例子。）这里的「更强」是一个偏序关系：可微 ⇒ 连续，但连续 ⇏ 可微。Example 7.4（$|x|$）就是一个连续但不可微的温和例子：它在 $x=0$ 处连续（左右极限等于函数值），但左右导数不相等。然而还有更极端的：Weierstrass 在 1872 年构造了一个处处连续但处处不可微的函数——它在每一点都连续，但没有一个点存在切线。这个函数将在后续章节（或更高级的实分析课程）中登场；现在你只需要记住：连续函数类严格大于可微函数类。在你学 CLRS 算法分析时，函数的「光滑程度」会影响你能使用什么优化工具——梯度下降要求可微，而次梯度方法只需要连续（实际上是凸的）。

---
---

---
<!-- ===== 书页 277（PDF 页 43）===== -->
---
<span style="color:#7f8c8d">*Part006 · 书页 277 行内双语翻译*</span>

<!-- page_043：页首习题区 7.2.17–7.2.23 按约定跳过。 -->

### <span style="color:#2471a3;">**[subsection]**</span> <span style="color:#c0392b">7.2.3 The Derivative as a Magnification（作为放大因子的导数）</span>

提高内容（enrichment section），可以省略。

现在我们给出 derivative（导数）的又一种解释，这次是把它作为放大因子（magnification factor）。
在基础微积分中，人们常常利用函数 $f$ 图像的几何内容。
特别地，我们可以通过图像上 tangent line（切线）的 slope（斜率）来理解导数。
而 $f$ 的图像是二维空间的子集，$f$ 的值域是一维空间的子集，因而具有一些额外的几何内容。

设 $f$ 在区间 $I$ 上可微（differentiable），并令 $J$ 为 $I$ 的一个闭子区间。
函数 $f$ 在 $J$ 上的值域也将是一个闭区间，因为 $f$ 可微从而在 $J$ 上连续，而连续函数把闭区间映为闭区间（见习题 5.8.2）。
如果我们比较区间 $J$ 的长度 $|J|$ 与区间 $f(J)$ 的长度 $|f(J)|$，那么表达式

```math
\frac{|f(J)|}{|J|}
```

就表示在映射 $f$ 下区间 $J$ 被扩张（或收缩）的量。

例如，若 $f(x)=x^2$ 且 $J=[2,3]$，则

```math
\frac{|f(J)|}{|J|} = \frac{|[4,9]|}{|[2,3]|} = \frac{5}{1} = 5.
```

因此区间 $[2,3]$ 被 $f$ 扩张为原来 5 倍大小的区间。
如果我们只考虑小区间，那么导数就为放大因子的大小提供了线索。
---
> <span style="color:#1e8449;">**[note] Note（译者注）：导数即放大因子——连接一元微积分与多元 Jacobian 的认知桥梁**</span>

7.2.3 节（enrichment section）给出了导数的第三种解释：$|f'(x_0)|$ 是「包含 $x_0$ 的小区间在映射 $f$ 下的放大倍数」。这个观点对你未来的学习非常重要：当你在 CLRS 中分析数值算法的稳定性、或在 Strang 的线性代数中遇到矩阵的条件数时，本质上都是在问「输入的小扰动在输出端被放大了多少倍」。导数作为局部线性近似的斜率，恰好捕捉了一维情形下的这种放大关系：对小区间 $J$，$\frac{|f(J)|}{|J|}\approx |f'(x_0)|$。书中以 $f(x)=x^2$、$J=[2,3]$ 为例，放大因子为 $5$（区间长度从 $1$ 变为 $5$），而在 $x_0=2$ 处 $f'(2)=4$，$x_0=3$ 处 $f'(3)=6$——放大因子恰好落在两者之间。这个视角也将帮助你理解链式法则：$f$ 放大 $|f'(x_0)|$ 倍，$g$ 再放大 $|g'(f(x_0))|$ 倍，复合函数的放大因子自然就是两者的乘积 $|g'(f(x_0))f'(x_0)|$。
---

---
<!-- ===== 书页 278（PDF 页 44）===== -->
---
<span style="color:#7f8c8d">*Part006 · 书页 278 行内双语翻译*</span>

<!-- page_044：习题区 7.2.24–7.2.26 按约定跳过；本页含 7.2.3 节末段与 7.3 节开头。 -->

（接上页 7.2.3 节正文。）

若 $J$ 是以 $x_0$ 为端点的足够小的区间，则比值 $|f(J)|/|J|$ 近似等于 $|f'(x_0)|$，且该近似在极限意义下变得「精确」。
因此 $|f'(x_0)|$ 可被视为包含点 $x_0$ 的小区间的放大因子（magnification factor）。
在我们以函数 $f(x)=x^2$ 所作的图示中，$x_0=2$ 处的放大因子为 $f'(2)=4$。
关于 $x_0$ 的小区间被放大约 4 倍。
在另一个端点 $x_0=3$ 处，关于 $x_0$ 的小区间被放大约 6 倍。
在习题 7.2.26 中，我们要求你证明一个精确的表述，以涵盖上述讨论。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">7.3 Computations of Derivatives（导数的计算）</span>

例 7.2（Example 7.2）给出了函数 $f(x)=x^2$ 的导数（derivative）的计算。
该计算涉及直接求一个适当的 difference quotient（差商）的极限。
对函数 $f(x)=x^2$ 而言，这个求值直截了当。
但差商的极限可能相当复杂。
你熟悉某些法则，它们对计算由导数已知的函数「构造」出来的函数的导数很有用。

本节我们回顾一些常用于计算导数的微积分法则。
我们首先需要证明其中的代数法则：和法则（sum rule）、乘积法则（product rule）和商法则（quotient rule）。
然后我们转向链式法则（chain rule）。
最后，我们考察幂法则（power rule）。
我们这里的观点不是练习导数的计算，而是建立导数的理论，并确保看到它如何依赖于我们先前证明的关于极限的工作。

我们将在本节得到的各种法则应被视为导数计算的辅助工具。
当然，理解这些法则对各种计算是必要的。
但它们绝不能替代对导数本身的理解。
而且在计算某些导数时它们可能并无用处。
（例如，习题 7.2.3 中的函数在 $x_0=0$ 处的导数就不能用这些法则来计算。）

尽管如此，确实常常会有这样的函数：它可以通过我们本节所考察的运算用若干个函数表达出来，而这些函数的……
<span style="color:#7f8c8d">*（原文此句跨页，续于书页 279。）*</span>
---

---
<!-- ===== 书页 279（PDF 页 45）===== -->
---
> Part006 · 第 7 章 · 书页 279 行内双语翻译

<span style="color:#7f8c8d">*第 7 章 Differentiation（微分）· 7.3 节 Computations of Derivatives（导数的计算）续*</span>

（承接前页正文）……这些函数之中，有一些是我们已经知道其导数的。在这些情形下，本节的技术或许会派上用场。

### <span style="color:#2471a3;">**[subsection]**</span> <span style="color:#c0392b">7.3.1 Algebraic Rules（代数法则）</span>

函数可以通过乘以常数、加法与减法、乘法以及除法等方式进行代数组合。
对每一种组合方式，都有一条用于计算其 derivative（导数）的微积分法则与之对应。
我们记得，和的极限（差的极限、积的极限、商的极限）等于各个极限之和（差、积、商）。
或许我们会以为，同样类型的法则也应该适用于导数。
事实上，和的导数确实等于各导数的和，但乘积的导数并不等于各导数的乘积。
商的情形也不会以如此简单的方式成立。
这些法则之所以采取这种形式的原因，可以通过写出导数的定义并逐步完成计算来找到。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 7.7（定理 7.7）</span>

> <span style="color:#7f8c8d;">TBB §7.3, p.279</span>

设 $f$ 和 $g$ 定义在区间 $I$ 上，且 $x_0 \in I$。
若 $f$ 和 $g$ 在 $x_0$ 处 differentiable（可微），则 $f+g$ 与 $fg$ 也在 $x_0$ 处可微。
若 $g(x_0) \neq 0$，则 $f/g$ 也在 $x_0$ 处可微。
此外，下列公式成立：

```math
\begin{aligned}
\text{(i)}\quad &(cf)'(x_0) = c\,f'(x_0) \qquad \text{for any real number } c,\\[2pt]
\text{(ii)}\quad &(f+g)'(x_0) = f'(x_0) + g'(x_0),\\[2pt]
\text{(iii)}\quad &(fg)'(x_0) = f(x_0)\,g'(x_0) + g(x_0)\,f'(x_0),\\[2pt]
\text{(iv)}\quad &\left(\frac{f}{g}\right)'(x_0)
  = \frac{g(x_0)\,f'(x_0) - f(x_0)\,g'(x_0)}{(g(x_0))^2}
  \qquad (\text{if } g(x_0) \neq 0).
\end{aligned}
```

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 部分 (i) 与 (ii) 可以由导数的定义以及适当的极限定理直接推出。
>
> 为验证部分 (iii)，令 $h = fg$。则对每个 $x \in I$ 有
>
> ```math
> h(x) - h(x_0) = f(x)\big[g(x) - g(x_0)\big] + g(x_0)\big[f(x) - f(x_0)\big],
> ```
>
> 于是
>
> ```math
> \frac{h(x) - h(x_0)}{x - x_0}
>   = f(x)\,\frac{g(x) - g(x_0)}{x - x_0}
>   + g(x_0)\,\frac{f(x) - f(x_0)}{x - x_0}. \tag{3}
> ```
>
> 当 $x \to x_0$ 时，$f(x) \to f(x_0)$，这是因为 $f$ 可微，从而也连续。
> 由导数的定义我们还知道，当 $x \to x_0$ 时，
> $\frac{g(x) - g(x_0)}{x - x_0} \to g'(x_0)$
> 且
> $\frac{f(x) - f(x_0)}{x - x_0} \to f'(x_0)$。
> 我们现在从方程 (3) 看到
>
> ```math
> \lim_{x \to x_0} \frac{h(x) - h(x_0)}{x - x_0}
>   = f(x_0)\,g'(x_0) + g(x_0)\,f'(x_0),
> ```
>
> 从而验证了部分 (iii)。

---
> <span style="color:#1e8449;">**[note] Note（译者注）：代数法则的结构——为什么乘积法则不是「各导数的乘积」**</span>

Theorem 7.7 罗列了四条法则：(i) 常数倍 $cf$、(ii) 和 $f+g$、(iii) 积 $fg$、(iv) 商 $f/g$。你在大一高数中已经把 (iii) 背成了 $(fg)' = f'g + fg'$。但 TBB 在这里关心的不是「公式是什么」，而是「为什么公式长这样」。证明 (iii) 的关键步骤是写下恒等式 $h(x)-h(x_0)=f(x)[g(x)-g(x_0)]+g(x_0)[f(x)-f(x_0)]$（其中 $h=fg$），然后除以 $x-x_0$，取极限。这个恒等式在代数上等价于「加一项减一项」的技巧（add-and-subtract trick），即 $f(x)g(x)-f(x_0)g(x_0) = f(x)g(x)-f(x)g(x_0)+f(x)g(x_0)-f(x_0)g(x_0)$。注意在取极限时，$f(x)\to f(x_0)$ 依赖于 Theorem 7.6（可微 ⇒ 连续）——这就是为什么必须先证明 Theorem 7.6，再证明乘积法则：乘积法则的证明用到了「可微函数连续」这个事实。换句话说，这些法则之间存在严格的依赖顺序：极限定理 → 可微 ⇒ 连续 → 乘积法则 → 商法则。🎥 *Colding 称乘积法则为 Leibniz rule*: "The next is what's called Leibniz rule. So you could also call it a product rule, but it's really quite generally called the Leibniz rule."（翻译：下一条是所谓的 Leibniz 法则。你也可以称它为乘积法则，但更普遍的名称是 Leibniz 法则。）注意本节文本特意纠正了一个常见误解：学生们可能会以为乘积的导数等于导数的乘积——这是因为和的导数等于导数的和，导致了一种错误的类比推广。代数运算的结构决定了法则的形式：和只涉及线性拆分，而积涉及交叉项的相互作用。

---
---

---
<!-- ===== 书页 280（PDF 页 46）===== -->
---
> Part006 · 第 7 章 · 书页 280 行内双语翻译

<span style="color:#7f8c8d">*第 7 章 Differentiation（微分）· Theorem 7.7 证明续*</span>

最后，为确立定理的部分 (iv)，令 $h = f/g$。
直接的代数运算表明

```math
\frac{h(x) - h(x_0)}{x - x_0}
  = \frac{1}{g(x)\,g(x_0)}
    \left[
      g(x_0)\,\frac{f(x) - f(x_0)}{x - x_0}
      - f(x)\,\frac{g(x) - g(x_0)}{x - x_0}
    \right]. \tag{4}
```

现在令 $x \to x_0$。由于 $f$ 和 $g$ 在 $x_0$ 处连续，故 $f(x) \to f(x_0)$ 且 $g(x) \to g(x_0)$。
于是，定理的部分 (iv) 由方程 (4)、导数的定义以及基本的极限定理即可得出。$\blacksquare$

<span style="color:#2471a3;">**[example]**</span> **Example 7.8（例 7.8）**

> <span style="color:#7f8c8d;">TBB §7.3, p.280</span>

为计算 $h(x) = (x^3 + 1)^2$ 的导数，我们有好几条途径可以采用。

1. 直接应用导数的定义。你或许愿意写出 difference quotient（差商），然后便会发现计算它的极限是一项艰巨的任务。
2. 将 $h(x)$ 写成 $x^6 + 2x^3 + 1$，再应用公式 $\frac{d}{dx}x^n = nx^{n-1}$（见 Exercise 7.3.5，即习题 7.3.5）以及求和法则。于是我们得到

```math
h'(x) = 6x^5 + 6x^2.
```

3. 使用 product rule（乘积法则）得到

```math
h'(x) = (x^3 + 1)\,\frac{d}{dx}(x^3 + 1) + (x^3 + 1)\,\frac{d}{dx}(x^3 + 1).
```

然后再次应用公式 $\frac{d}{dx}x^n = nx^{n-1}$ 与求和法则继续计算：

```math
h'(x) = (x^3 + 1)\,3x^2 + (x^3 + 1)\,3x^2 = 6x^5 + 6x^2. \qquad \blacksquare
```

<span style="color:#7f8c8d">*本页其余部分为习题区（Exercises 7.3.1–7.3.4），按约定跳过。*</span>

---

---
<!-- ===== 书页 281（PDF 页 47）===== -->
---
<span style="color:#7f8c8d">*Part006 · 书页 281 行内双语翻译*</span>

<span style="color:#7f8c8d">**Figure 7.3（图 7.3）**：f 与 g 在若干点处的取值。</span>

| $x$ | $f(x)$ | $f'(x)$ | $g(x)$ | $g'(x)$ |
|-----|--------|---------|--------|---------|
| 1   | 3      | 3       | 2      | 2       |
| 2   | 4      | 4       | 4      | 0       |
| 3   | 6      | 1       | 1      | 0       |
| 4   | -1     | 0       | 1      | 1       |
| 5   | 2      | 5       | 3      | 3       |

> 习题 7.3.5–7.3.10 及 SEE NOTE 171、172 提示区为习题区，按约定跳过。

### <span style="color:#2471a3;">**[subsection]**</span> <span style="color:#c0392b">7.3.2 The Chain Rule（链式法则）</span>

还有一个你可能从微积分课程中记得的、关于 Example 7.8（例 7.8）的非代数（nonalgebraic）解释。

<span style="color:#2471a3;">**[example]**</span> **Example 7.9（例 7.9）**

> <span style="color:#7f8c8d;">TBB §7.3, p.281</span>

我们可以把函数 $h(x) = (x^3 + 1)^2$ 看作函数 $f(x) = x^3 + 1$ 与 $g(u) = u^2$ 的复合（composition），于是

```math
h(x) = g \circ f(x).
```

你熟悉链式法则（chain rule），它在计算复合函数（composite function）的导数时很有用。在本例中，这一计算将导出

```math
h'(x) = g'(f(x)) f'(x) = g'(x^3 + 1) \cdot 3x^2
      = 2(x^3 + 1)3x^2 = 6x^5 + 6x^2.
```

在初等微积分里，你可能更愿意通过换元来得到（换元的具体内容见下一页书页 282 开头）：

```math
\frac{dy}{dx} = \frac{dy}{du} \frac{du}{dx} = 2(x^3 + 1)(3x^2) = 6x^5 + 6x^2.
```

---
> <span style="color:#1e8449;">**[note] Note（译者注）：链式法则——$\frac{dy}{dx}=\frac{dy}{du}\frac{du}{dx}$ 的严格化比你想象的要麻烦**</span>

本节用两种方式引入链式法则：先是通过放大因子（magnification factor）的直觉——$f$ 把小区域放大 $|f'(x_0)|$ 倍，$g$ 再把结果放大 $|g'(f(x_0))|$ 倍，复合效果是两者相乘——这建立了几何直观。然后 TBB 给出严格证明，而证明的难点恰恰在于那个「直观」写法的漏洞：我们想写 $\frac{g(f(x))-g(f(x_0))}{x-x_0} = \frac{g(f(x))-g(f(x_0))}{f(x)-f(x_0)} \cdot \frac{f(x)-f(x_0)}{x-x_0}$，但第一个因子的分母 $f(x)-f(x_0)$ 可能为零——即便 $x\neq x_0$，$f$ 也可能在 $x_0$ 附近重复取值 $f(x_0)$。🎥 *Colding 在视频中对此做了简洁回顾*: "And the chain rule was that if f and g are differentiable, then the composition here is also differentiable. And the derivative of the composition is the derivative of the second function evaluated at this point here times the derivative of the first in x."（翻译：链式法则说的是，如果 $f$ 和 $g$ 都可微，那么复合函数也可微。复合函数的导数是第二个函数在 $f(x)$ 处的导数乘以第一个函数在 $x$ 处的导数。）TBB 的证明通过将序列分成两类来处理：如果几乎所有 $x_n$ 都满足 $f(x_n)\neq f(x_0)$，则直接使用乘积形式的差商；如果存在无限多项满足 $f(x_n)=f(x_0)$，则必有 $f'(x_0)=0$（见 Exercise 7.3.11），此时 $h'(x_0)=0$ 也成立。这种「分情形讨论 + 序列语言」的证明风格是实分析的标志性操作——它不依赖任何「除以无穷小」的直觉，只依赖极限的 $\epsilon$-$\delta$（或等价的序列）定义。你会在 CLRS 的分治算法分析中看到类似的结构：把输入分解为子问题，分别处理后合并——只不过这里的「子问题」是两种不同类型的序列。

---
---

---
<!-- ===== 书页 282（PDF 页 48）===== -->
---
<span style="color:#7f8c8d">*Part006 · 书页 282 行内双语翻译*</span>

（接上页）这是通过换元（substitution）$u = x^3 + 1$、$y = u^2$ 实现的。$\blacksquare$

链式法则就是那个熟悉的微积分公式

```math
\frac{d}{dx} g(f(x)) = g'(f(x)) f'(x),
```

它在适当假设（appropriate assumptions）下用于对两个函数 $g \circ f$ 的复合求导。微积分学生常常借助新变量 $y = g(u)$ 与 $u = f(x)$，把它记忆为 $\frac{dy}{dx} = \frac{dy}{du}\frac{du}{dx}$ 的形式。

我们首先试着理解为什么链式法则应当成立，然后我们将给出链式法则的精确陈述（statement）与证明（proof）。也许「看出」链式法则最容易的方式，是把导数解释为一个放大因子（magnification factor）。

设 $f$ 在 $x_0$ 的某个邻域（neighborhood）上有定义，设 $g$ 在 $f(x_0)$ 的某个邻域上有定义。若 $f$ 在 $x_0$ 处可微（differentiable），则 $f$ 把每个包含 $x_0$ 的小区间 $J$ 映成包含 $f(x_0)$ 的区间 $f(J)$，且 $|f(J)|/|J|$ 近似等于 $|f'(x_0)|$。此外，若 $g$ 在 $f(x_0)$ 处可微，则 $g$ 会把包含 $f(x_0)$ 的小区间 $f(J)$ 映成区间 $g(f(J))$，且 $|g(f(J))|/|f(J)|$ 近似等于 $|g'(f(x_0))|$。于是 $h = g \circ f$ 把 $J$ 映成区间 $h(J) = g(f(J))$，并且

```math
\frac{|h(J)|}{|J|} = \frac{|g(f(J))|}{|f(J)|} \cdot \frac{|f(J)|}{|J|},
```

而这个量近似等于 $|g'(f(x_0))|\,|f'(x_0)|$。

简言之，放大因子 $|f'(x_0)|$ 与 $|g'(f(x_0))|$ 相乘，得到放大因子 $|h'(x_0)|$。

<span style="color:#2471a3;">**[example]**</span> **Example 7.10（例 7.10）**

> <span style="color:#7f8c8d;">TBB §7.3, p.282</span>

让我们把这段讨论与前面的例子 $h(x) = (x^3 + 1)^2$ 联系起来。这里 $f(x) = x^3 + 1$，$g(x) = x^2$。在 $x_0 = 1$ 处我们得到 $f(x_0) = 2$、$f'(x_0) = 3$、$g(f(x_0)) = 4$ 以及 $g'(f(x_0)) = 4$。函数 $f$ 把 $x_0 = 1$ 附近的小区间映成长度约为其三倍的区间；反过来，函数 $g$ 又把这些区间映成长度约为其四倍的区间，于是复合函数 $h = g \circ f$ 在 $x_0 = 1$ 处的总放大因子约为 12（图 7.4）。$\blacksquare$

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 如果我们想依据前面的讨论来表述链式法则的一个证明，可以从写下
>
> ```math
> \frac{g(f(x)) - g(f(x_0))}{x - x_0}
>     = \frac{g(f(x)) - g(f(x_0))}{f(x) - f(x_0)} \cdot \frac{f(x) - f(x_0)}{x - x_0} \tag{5}
> ```
>
> 开始，这个式子与我们的公式 $|h(J)|/|J| = (|g(f(J))|/|f(J)|)(|f(J)|/|J|)$ 相对应。

---

---
<!-- ===== 书页 283（PDF 页 49）===== -->
---
> Part006 · 第 7 章 · 书页 283 行内双语翻译

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">7.3 Computations of Derivatives（导数的计算）</span>

**Figure 7.4（图 7.4）** $f$ 将 $J$ 映射到 $f(J)$，$g$ 再将后者映射到 $h(J)$。此处 $h = g \circ f$，$x_0 = 1$，且 $J = [0.9, 1.1]$。（图中 $f$ 与 $g$ 为两条带箭头的曲线，横轴刻度为 1 至 6。）

若我们在 (5) 中令 $x \to x_0$，则会预期得到所期望的结果：
```math
(g \circ f)'(x_0) = g'(f(x_0)) f'(x_0).
```
而这一论证若 $f$ 是（比如说）increasing（递增）的，便是有效的。但要使方程 (5) 成立，我们必须有 $x \neq x_0$ 且 $f(x) \neq f(x_0)$。在计算 difference quotient（差商）的极限时，我们可以假定 $x \neq x_0$，但若没有额外的假设，我们不能假定「由 $x \neq x_0$ 就推出 $f(x) \neq f(x_0)$」。然而 chain rule（链式法则）依然成立。

若我们把这两种情形分开，证明会更清晰。在较简单的情形中，函数在 $x_0$ 的某个 neighborhood（邻域）内不会重复取值 $f(x_0)$。在较困难的情形中，函数在 $x_0$ 的每一个邻域内都会重复取值 $f(x_0)$。习题 7.3.11 表明，在后一情形下我们必须有 $f'(x_0) = 0$，于是链式法则就归结为证明 composite function（复合函数）$g \circ f$ 的导数也为零。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 7.11 (Chain Rule, 链式法则)</span>

> <span style="color:#7f8c8d;">TBB §7.3, p.283</span>

设 $f$ 定义在 $x_0$ 的一个邻域 $U$ 上，设 $g$ 定义在 $f(x_0)$ 的一个邻域 $V$ 上，且满足 $f(x_0) \in f(U) \subset V$。假定 $f$ 在 $x_0$ 处可微（differentiable），$g$ 在 $f(x_0)$ 处可微。则复合函数 $h = g \circ f$ 在 $x_0$ 处可微，并且
```math
h'(x_0) = (g \circ f)'(x_0) = g'(f(x_0)) f'(x_0).
```

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.*

> 考虑任意由互异点 $x_n$ 组成的序列，其中每一点都不同于 $x_0$ 且收敛到 $x_0$。若我们能证明：对每一个这样的序列，序列
> ```math
> S_n = \frac{g(f(x_n)) - g(f(x_0))}{x_n - x_0}
> ```
> 都收敛到 $g'(f(x_0)) f'(x_0)$，那么我们便得到了所需的公式。

---

---
<!-- ===== 书页 284（PDF 页 50）===== -->
---
> Part006 · 第 7 章 · 书页 284 行内双语翻译

<span style="color:#2471a3;">**[proof]**</span> *Proof (continued)（证明续）.*

> 注意，若 $f(x_n) \neq f(x_0)$，则可记 $y_n = f(x_n)$、$y_0 = f(x_0)$，并把 $S_n$ 写成
> ```math
> S_n = \left( \frac{g(y_n) - g(y_0)}{y_n - y_0} \right) \left( \frac{f(x_n) - f(x_0)}{x_n - x_0} \right). \tag{6}
> ```
> 从这种形式可以看出，显然
> ```math
> S_n \to g'(y_0) f'(x_0) = g'(f(x_0)) f'(x_0)
> ```
> 只是除了一个问题：我们（正如在开始证明之前所指出的）不能假定在所有情形下都有 $f(x_n) \neq f(x_0)$。

> 于是我们考虑两种情形。在第一种情形中，我们假定：对任意由互异点 $x_n$ 组成且收敛到 $x_0$ 的序列，不可能有无限多项满足 $f(x_n) = f(x_0)$。在这种情况下，chain rule（链式法则）公式显然成立。

> 在第二种情形中，我们假定：确实存在由互异点 $x_n$ 组成、收敛到 $x_0$ 且其中有无限多项满足 $f(x_n) = f(x_0)$ 的序列。在这种情况下（习题 7.3.11），我们必须有 $f'(x_0) = 0$；因此，为确立链式法则，我们需要证明 $h'(x_0) = 0$。但在此情形下，对任意收敛到 $x_0$ 的序列 $x_n$，要么 $S_n = 0$［当 $f(x_n) = f(x_0)$ 时］，要么 $S_n$ 可写成方程 (6) 的形式［当 $f(x_n) \neq f(x_0)$ 时］。于是显然 $S_n \to 0$，证明至此完成。$\blacksquare$

---

本页其余部分为习题区（Exercises 7.3.11–7.3.15，含 Notes 提示区），按约定跳过。
---


---

<span style="color:#7f8c8d;">*Part006 翻译完。习题区按约定跳过（第 5 章习题提示区 p.235–238、第 6 章各节 Exercises、6.9 Challenging Problems p.268、Notes 提示区 p.269–270、第 7 章 §7.2/§7.3 习题区）。*</span>
