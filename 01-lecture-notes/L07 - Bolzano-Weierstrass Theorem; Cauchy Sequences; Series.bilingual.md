# 18.100B / 18.1002 Real Analysis（实分析）

## <span style="color:#c0392b">Lecture 7 — Bolzano-Weierstrass Theorem; Cauchy Sequences; Series（Bolzano-Weierstrass 定理；柯西序列；级数）</span>

<span style="color:#7f8c8d;">Instructor: Tobias Holck Colding · Spring 2025 · MIT</span>

---

### <span style="color:#2471a3;">**[lecture]**</span> <span style="color:#c0392b">Last Time（上节回顾）</span>

上节课我们讨论了两件事：首先是 **Cauchy convergence theorem（柯西收敛定理）**——任何 Cauchy sequence（柯西序列）都是 convergent（收敛）的；其次是 **Bolzano-Weierstrass theorem（Bolzano-Weierstrass 定理）**。

上节课我们证明了 Cauchy convergence theorem，但证明中**假设**了 Bolzano-Weierstrass 定理成立——我们当时说：Cauchy 序列有界，由 Bolzano-Weierstrass 定理存在收敛子列，再证明该子列的极限就是整个序列的极限。今天要做的就是**补上 Bolzano-Weierstrass 定理本身的证明**。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Colding 在视频开头明确交代了两条定理的逻辑关系，但如果你把 L05–L07 串起来看，会发现一条**三环证明链**：**单调收敛定理（MCT）→ Bolzano-Weierstrass → Cauchy 收敛定理**。这个顺序不能颠倒——每一环恰好为下一环提供它缺少的那块拼图。具体来说：MCT（L05）告诉你「单调 + 有界 ⟹ 收敛」，但它只对单调序列管用，遇到震荡序列就废了；B-W 定理（本讲）把 MCT 作为子程序，用二分法从任意有界序列中「抽出」一个收敛子列——它把 MCT 的适用范围从「必须单调」扩展到了「只要有界」；Cauchy 收敛定理（L06）再用 B-W 作为子程序，把「收敛」这个需要事先知道极限的概念，替换成「序列内部的项越来越靠近」这个自检条件——它把收敛判定从「需要猜极限」变成了「只需检查序列自身」。三层下来，你从最原始的「单调有界」一路走到了「自检收敛」，等于用三个定理给 ℝ 的完备性搭出了三套等价表述。这正是实分析大厦的第一块承重墙：后面级数收敛的每一个判别法，归根到底都是 Cauchy 准则的特例或变形。🎥 *Colding 在视频中说:* "we didn't prove the Bolzano-Weierstrass Theorem. So let's try to prove it now."（翻译：我们当时没有证明 Bolzano-Weierstrass 定理，所以现在来证明它。）

---

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">Bolzano-Weierstrass Theorem（Bolzano-Weierstrass 定理）</span>

任何 bounded sequence（有界序列）$a_n$ 都有一个 convergent subsequence（收敛子列）$a_{n_k}$。

> <span style="color:#7f8c8d;">TBB §2.11, p.56</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这个定理回答了一个设计问题：**只知道序列有界（每一项都在一个有限范围内），能得到什么？** 答案出人意料——虽然序列本身可以不收敛（比如来回震荡），但一定能从中抽出一个收敛的子列。直观上，有界意味着序列的「信息」被压缩在有限区间里；无穷多个点挤在有限区间里，必然在某处「聚集」——这个聚集点就是子列的极限。
>
> 这里的证明策略可以命名为**「二分夹逼法」**：① 把区间对半分割，利用「无穷多个点必有一半含无穷多个」（无限鸽笼原理，见下文注）定位一个越来越窄的区间套；② 从每个区间里各取一个点构成子列；③ 用区间长度 $\to 0$ 夹出收敛性。这套「二分 + 夹逼」的骨架在后面还会反复出现——比如 L14 在 metric space（度量空间）里证明 sequential compactness（序列紧致性）时，本质还是它。

---

### <span style="color:#2471a3;">**[proof]**</span> <span style="color:#c0392b;">Proof（证明）</span>

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

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 回顾整个 B-W 定理的证明，你会发现一个比定理本身更深刻的模式：**在 ℝ 中，「有界」和「存在收敛子列」在闭区间上是等价的。** 换句话说，B-W 定理实际上刻画了闭有界区间 $[a,b]$ 的一个深层性质——任何无穷点集在它里面都「无处可逃」，必然在某处堆积。这个性质在更高级的框架里叫 **sequential compactness（序列紧致性）**：一个集合是序列紧致的，当且仅当其中每个序列都有收敛到该集合内某点的子列。B-W 定理说「ℝ 中的闭有界区间是序列紧致的」——这是 ℝ 区别于 ℚ（有理数集）的关键特征之一：你可以构造一个有理数序列（比如十进制逼近 $\sqrt{2}$ 的序列 $1, 1.4, 1.41, 1.414, \ldots$），它在 ℝ 中收敛到无理数 $\sqrt{2}$，因此在 ℚ 内**没有任何**收敛子列。L14 会把这个概念推广到一般的 metric space（度量空间），届时「闭 + 有界」不再自动蕴含紧致性——你会在那里看到，恰好是 ℝ 的完备性（Cauchy 序列必收敛）让 B-W 定理成立。现在你不需要知道度量空间是什么，只需要记住一个心态模型：**B-W 定理 = ℝ 中「有限空间装不下无穷多个彼此远离的点」的形式化**——这个直觉在后面讨论连续函数在闭区间上的性质（最大值定理、一致连续性）时会反复兑现，那些证明几乎全是以 B-W 定理为发动机的。

---

### <span style="color:#2471a3;">**[note]**</span> <span style="color:#c0392b">From Wikipedia: Karl Weierstrass（维基百科：卡尔·魏尔斯特拉斯）</span>

Karl Theodor Wilhelm Weierstrass（1815 – 1897）是德国数学家，常被称为 **"father of modern analysis"（现代分析之父）**。尽管他未获学位便离开了大学，他仍自学数学并接受教师培训，最终教授数学、物理、植物学与体操。在他的众多贡献中，Weierstrass 将函数的连续性定义与复分析严格形式化，证明了 intermediate value theorem（介值定理）与 Bolzano–Weierstrass 定理，并用后者研究了 closed bounded intervals（闭有界区间）上连续函数的性质。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 为什么这个定理叫「Bolzano–Weierstrass」而不是只叫「Weierstrass」？因为 Bernard Bolzano（伯纳德·波尔查诺，1781–1848）在 **1817 年**就已经证明并使用了这个结果——他当时的目标是证明介值定理（这需要「有界序列有收敛子列」这个事实），他的论文比 Weierstrass 早了半个世纪。但 Bolzano 的工作长期被忽视，Weierstrass 在 **1860 年代**柏林大学的讲义中独立地重新证明了它，并以此为基础建立了整个「用 $\epsilon$-$\delta$ 语言严格化分析学」的纲领。数学史上这种「一个人先发现、被遗忘、另一个人重新发现并推广」的故事反复发生，定理命名通常纪念的是让结果广为人知的那位。
>
> 这条生平还揭示了一个有趣的事实：Weierstrass 是**中学教师出身**，教过植物学和体操——19 世纪的分析学奠基人之一并非科班教授。这对你理解「数学家的直觉来自哪里」有启发：Weierstrass 的严格化动力恰恰来自教学——他需要把分析学讲得让师范生能听懂，这逼出了 $\epsilon$-$\delta$ 语言。你在 L04 学到的 sequence convergence 的 $\epsilon$-$N$ 定义，就是这场「教学驱动的严格化运动」的产物。

---

### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f;">**Series（级数）**</span>

设 $a_n$ 是一个序列。我们可以用它构造一个新的序列 $s_n$：令

```math
s_1 = a_1, \qquad s_2 = a_1 + a_2, \qquad s_3 = a_1 + a_2 + a_3,
```

一般地，

```math
s_n = a_1 + \cdots + a_n = \sum_{i=1}^{n} a_i.
```

这个由部分和构成的序列 $s_n$ 称为 **series（级数）**（$s_n$ 本身仍是一个普通序列，只是它的每一项是前 $n$ 个 $a_i$ 的和）。级数 $\sum_{i=1}^{\infty} a_i$ **converges（收敛）** 当且仅当序列 $s_n$ 收敛；若收敛，我们也用同一个符号 $\sum_{i=1}^{\infty} a_i$ 表示它的极限（即无穷和）。

> <span style="color:#7f8c8d;">TBB §3.4, p.84</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这里有一个贯穿整个级数理论的 **notation abuse（记号滥用）**：符号 $\sum_{i=1}^{\infty} a_i$ 被用来表示两个不同的东西——级数本身（即部分和序列），以及（若收敛时）它的极限。Colding 在课上专门停下来强调这一点。🎥 *Colding 在视频中说:* "this symbol here is used for two different things. It's used for the series. And if the series is convergent, it's also used for the limit."（翻译：这个符号在这里被用于两件不同的事：它表示级数本身；而当级数收敛时，它也表示极限。）
>
> 这个「双重身份」你在编程里其实很熟悉：这就像 C 语言里的函数重载或 Python 里同一个名字在不同上下文中绑定到不同对象——数学家知道上下文，所以不觉得混乱，但初学时容易把「级数的值」和「级数」混为一谈。**关键的第一性原理认知：级数不是一个「和」，而是一个序列（部分和序列）**；「级数收敛」四个字说的完全是「部分和序列 $s_n$ 收敛」这件事。这样一来，你已经在 L04–L06 学到的关于序列的一切（极限、Cauchy、单调收敛）都自动适用于级数——级数理论并不需要新的收敛概念，只需要把序列的语言翻译过来。这正是 TBB 把级数放在第 3 章、紧接序列之后的原因。
>
> 🎥 *Colding 还用一个经典例子引入级数：芝诺悖论——阿喀琉斯追乌龟。* "the paradox is that because the turtle have a head start, then Achilles can never catch up with the turtle... in order to catch up with the turtle, then Achilles first have to go half of the distance... And so this goes on infinitely long, and therefore, he can never catch up with the turtle."（翻译：悖论说因为乌龟有先发优势，阿喀琉斯永远追不上乌龟——为了追上乌龟，他必须先跑完乌龟已跑距离的一半，然后再跑一半，如此无限进行下去，所以他永远追不上。）**这个悖论在讲义里没有，是 Colding 课上口头讲的。** 它的数学破解正是级数：阿喀琉斯跑的总距离是 $1 + \frac{1}{2} + \frac{1}{4} + \cdots$，这是一个**有限值**（$2$，见下文的几何级数），所以无限多个「步骤」加起来可以是有限的——芝诺的谬误在于以为「无限步」必然需要「无限时间」。

---

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">Geometric Series（几何级数）</span>

设 $a_n = c^n$，则级数 $s_n = \sum_{i=0}^{n} c^i$ 称为 **geometric series（几何级数）**。它收敛当且仅当 $|c| < 1$。并且当 $|c| < 1$ 时，它的极限（无穷和）为

```math
\sum_{i=0}^{\infty} c^i = \frac{1}{1 - c}.
```

**证明的准备工作（telescoping，相消）。** 观察到

```math
(1 - c)\sum_{i=0}^{n} c^i = 1 - c^{n+1}.
```

（展开即得：$1 + c + c^2 + \cdots + c^n$ 减去 $c + c^2 + \cdots + c^n + c^{n+1}$，中间项全部抵消，只剩 $1 - c^{n+1}$。）由此，若 $c \ne 1$，则

```math
s_n = \sum_{i=0}^{n} c^i = \frac{1 - c^{n+1}}{1 - c}.
```

**收敛性。** 当 $|c| < 1$ 时，$c^{n+1} \to 0$，故 $s_n$ 收敛，极限为 $\frac{1}{1-c}$。当 $|c| > 1$ 或 $c = -1$ 时发散；$c = 1$ 的情形单独检查也发散（此时 $s_n = n + 1 \to \infty$）。$\square$

> <span style="color:#7f8c8d;">TBB §3.4, p.87（作为与调和级数对比的基准级数）</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Colding 称几何级数是**最重要的级数**，理由很实用：它是少数几个「能算出精确极限」的非平凡级数，因此可以作为**基准**——其他级数通过与它比较来判断敛散（这正是本讲后面的 comparison test 和 ratio test 的底层逻辑，下一讲 L08 的 root test 也是）。🎥 *Colding 在视频中说:* "it's kind of a non-trivial series that can be used to determine whether other series... converge or not. And the geometric series is easier to determine whether it is convergent or not."（翻译：它是一个非平凡的级数，可以用来判断其他级数是否收敛；而几何级数本身的敛散性很容易判断。）
>
> 证明中的 telescoping 技巧值得单独命名：**「错位相消法」**——把和式乘上一个因子（这里是 $1-c$），让展开后的项两两抵消，只剩首尾两项。这个技巧你在高中数列求和时就见过（等比数列求和公式就是这么来的），在 CLRS 第 3 章分析分治算法复杂度时也会反复用到：$\sum_{i=0}^{n} r^i \le \frac{1}{1-r}$（当 $0 < r < 1$）是算法分析中最常用的上界工具之一——比如递归树展开 $T(n) = 2T(n/2) + n$ 时，各层工作量构成几何级数。你在 6.006 里见过的「几何级数有界」这个结论，源头就是今天这个定理。
>
> 发散方向的证明用的是另一个通用模板：**「连续项差不趋于零」检测**。$s_{n+1} - s_n = c^{n+1}$，当 $|c| \ge 1$ 时它恒 $\ge 1$——连相邻两项都不靠近，序列必然不是 Cauchy 序列，从而发散。这里用到的结论「收敛序列必是 Cauchy 序列」正是 L06 的内容，说明今天的内容在系统性地复用前几讲的工具。

---

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">Harmonic Series（调和级数）</span>

**Harmonic series（调和级数）**：$a_n = \frac{1}{n}$，即级数 $\sum_{i=1}^{\infty} \frac{1}{i}$。这个级数是 **divergent（发散）** 的。

**证明。** 我们将证明

```math
s_{2^n - 1} \ge \frac{n}{2}.
```

（如果原级数收敛，它的任何子列也收敛；一旦证明子列 $s_{2^n - 1}$ 无界，原级数必发散。）

**归纳奠基（$n = 1$）：** $s_1 = 1 \ge \frac{1}{2}$，成立。

**归纳步（$n \Rightarrow n + 1$）：** 假设 $s_{2^n - 1} \ge \frac{n}{2}$，则

```math
s_{2^{n+1} - 1} \ge s_{2^n - 1} + \sum_{i=2^n}^{2^{n+1}-1} \frac{1}{i} \ge \frac{n}{2} + 2^n \cdot \frac{1}{2^{n+1}} \ge \frac{n}{2} + \frac{1}{2} = \frac{n+1}{2}.
```

（中间那段和共有 $2^n$ 项，每一项都 $\ge \frac{1}{2^{n+1}}$（因为 $i \le 2^{n+1}-1 < 2^{n+1}$），所以整段和 $\ge 2^n \cdot \frac{1}{2^{n+1}} = \frac{1}{2}$。）归纳完成，故对所有 $n$ 成立。

由于 $\frac{n}{2} \to \infty$，子列 $s_{2^n - 1}$ 发散，因此原级数发散。$\square$

> <span style="color:#7f8c8d;">TBB §3.4, p.86</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 调和级数发散是分析学中最反直觉的事实之一：**它的项 $a_n = \frac{1}{n}$ 趋于零，但级数仍然发散**。这是初学者最常见的卡点——「各项趋于零」只是收敛的**必要条件**，远非充分条件。Colding 在课上给了一个实用的 side remark（旁注）：拿到一个级数，第一件事永远是检查 $a_n$ 是否趋于 $0$——如果 $a_n \not\to 0$，级数必发散，直接结束，不用浪费精力在任何判别法上。🎥 *Colding 在视频中说:* "if you give me a series, the first thing I always check is that... does an go to 0 or not... if an does not go to 0, you're already done. There's no reason to continue."（翻译：如果你给我一个级数，我第一件事总是检查 $a_n$ 是否趋于 $0$……如果 $a_n$ 不趋于 $0$，你就已经结束了，没有理由继续。）
>
> 但注意：这个检查是**单向**的——调和级数告诉我们 $a_n \to 0$ 时级数照样可以发散。直觉上，$\frac{1}{n}$ 趋向 $0$ 的速度「太慢了」：把 $2^n$ 项 $\frac{1}{2^{n+1}}$ 这样的小项凑在一起，每组还能凑出 $\frac{1}{2}$ 的量级，无限多组凑出无限大。用算法复杂度的话说：$\sum \frac{1}{n}$ 的发散速度是 $\Theta(\log n)$——指数个子列项只贡献线性增长。**「趋于 0 的速度」是级数理论真正关心的量**，这个视角在后面会反复出现（比如 p-series $\sum \frac{1}{n^p}$ 以 $p = 1$ 为收敛分界线，TBB §3.4, p.87）。
>
> Colding 还预告了一个更好的工具：**integral test（积分判别法）**——把级数看成矩形面积之和，与曲线 $\int \frac{1}{x} dx = \ln x$ 的面积比较，立刻得到同样的结论且能给出发散速度。他说今天这个证明是 "very simple-minded"（非常朴素的），只是为了在还没有积分工具时先立住结论。🎥 *Colding 的预告:* "once we learn about the integral test and so on, there are other way better ways of doing it."（翻译：等我们学了积分判别法之后，会有好得多的做法。）

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 如果你把调和级数的发散证明和稍后 $\sum 1/i^2$ 的收敛证明对比着看，会发现它们用了**同一套技术骨架**：（1）不直接分析 $s_n$，而是分析按 $2$ 的幂次抽样的子列 $s_{2^n-1}$；（2）把 $2^n$ 到 $2^{n+1}-1$ 之间的所有项捆成一组；（3）用「组内项数 × 组内最值（最大项或最小项）」给每组贡献一个 bound；（4）把 bound 加总，得到一个几何级数或等差数列，从而判断敛散。这套「按指数间隔抽样、分组放缩」的技术，在数学里有个正式名称叫 **Cauchy condensation test（柯西凝聚判别法）**：对于非负递减序列 $a_n$，$\sum a_n$ 与 $\sum 2^n a_{2^n}$ 同敛散。本讲两个证明正是这个判别法的特例——调和级数对应 $a_n = 1/n$，凝聚后 $\sum 2^n \cdot (1/2^n) = \sum 1$ 发散；$\sum 1/n^2$ 对应 $a_n = 1/n^2$，凝聚后 $\sum 2^n \cdot (1/4^n) = \sum (1/2)^n$ 收敛。一旦你认出这个模式，p-series 的临界点 $p=1$ 就一目了然：凝聚后变成 $\sum 2^n \cdot (1/2^{pn}) = \sum (2^{1-p})^n$，这恰好是一个公比为 $2^{1-p}$ 的几何级数——$p>1$ 时公比 $<1$ 收敛，$p\le 1$ 时公比 $\ge 1$ 发散。**这个模式的价值不在于「记住公式」，而在于它揭示了分析学中一个深层技巧：用指数间隔采样把「多项式衰减」转化成「指数衰减」来比较**——而指数衰减正是几何级数最擅长处理的。TBB §3.6, p.103–104 正是用凝聚法作为推论（corollary）证明了 p-harmonic series 的完整收敛行为；你现在就可以把它当成一个心态模型来用。

---

### <span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f;">**Absolutely Convergent（绝对收敛）**</span>

我们称级数 $\sum_{n=0}^{\infty} a_n$ 是 **absolutely convergent（绝对收敛）** 的，如果级数

```math
\sum_{n=0}^{\infty} |a_n|
```

收敛。**绝对收敛蕴含收敛，但反过来不成立。**

**Example（例）：** 我们将在后面的讲次中证明，级数

```math
\sum_{n=1}^{\infty} \frac{(-1)^n}{n}
```

是收敛的；但若对各项取绝对值，得到的正是调和级数 $\sum \frac{1}{n}$，而它发散。所以这个级数收敛但不绝对收敛——它是著名的 **alternating harmonic series（交错调和级数）**。

> <span style="color:#7f8c8d;">TBB §3.5, p.92–93</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 为什么需要「绝对收敛」这个更强的概念？因为**收敛**本身是个「弱」性质：它只告诉你部分和有极限，但对「正负号互相抵消」极度敏感——交错调和级数就是靠 $(-1)^n$ 的符号交替勉强收敛的，稍微扰动（比如只取绝对值）就发散。而**绝对收敛**说「连绝对值加起来都收敛」，这意味着级数的收敛不依赖符号的运气，纯粹由各项的大小决定。在后面（L08 及以后）你会看到：绝对收敛的级数可以放心地重排项、换序求和、逐项积分——这些操作对条件收敛的级数全是禁区。
>
> **证明策略命名：「绝对值支配法」。** 证明「绝对收敛 ⟹ 收敛」只需一个不等式（见下文 proof）：原级数的部分和之差 $|s_n - s_m|$ 被绝对值级数的部分和之差 $|\bar{s}_n - \bar{s}_m|$ 支配（dominate）。于是绝对值级数收敛（= Cauchy）自动把原级数「拉」成 Cauchy 序列，再由 Cauchy convergence theorem 收工。这个「**找一个更大的、已知收敛的东西来控制目标**」的思路是分析学的主旋律之一——比较判别法、支配收敛定理（dominated convergence）都是它的变体。你在 6.042J 里也见过它的离散版本：证明某个量趋于 0 时，先找绝对值更大的量证明它趋于 0。

---

### <span style="color:#2471a3;">**[proof]**</span> <span style="color:#c0392b;">Proof: 绝对收敛蕴含收敛</span>

由 Cauchy convergence theorem，我们只需证明：若 $\sum_{n=0}^{\infty} |a_n|$ 收敛，则部分和序列

```math
s_n = \sum_{i=0}^{n} a_i
```

是 Cauchy 序列。设 $\bar{s}_n = \sum_{i=0}^{n} |a_i|$。对 $m < n$，由三角不等式，

```math
|s_n - s_m| = |a_{m+1} + \cdots + a_n| \le |a_{m+1}| + \cdots + |a_n| = |\bar{s}_n - \bar{s}_m|.
```

由于 $\bar{s}_n$ 收敛，它是 Cauchy 序列；上式表明 $s_n$ 也被「夹」成 Cauchy 序列，故 $s_n$ 收敛。$\square$

> <span style="color:#7f8c8d;">TBB §3.5, p.93</span>

---

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">Non-negative Terms ⟺ Bounded Partial Sums（非负项级数：收敛 ⟺ 部分和有界）</span>

设 $\sum_{i=0}^{\infty} a_i$ 是 **non-negative（非负）** 项级数（即 $a_n \ge 0$ 对所有 $n$）。则它收敛当且仅当部分和序列 $s_n$ **bounded from above（上有界）**。

**Proof（证明）。** 由于 $s_{n+1} = s_n + a_n \ge s_n$，部分和序列 $s_n$ 是 monotone nondecreasing（单调不减）的。由 monotone convergence theorem（单调收敛定理，L05），单调序列收敛当且仅当有界，命题得证。$\square$

> <span style="color:#7f8c8d;">TBB §3.5, p.91（Boundedness Criterion）</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这个定理把「级数收敛」这个看起来全新的问题，**归约**成了 L05 已经解决的「单调有界序列」问题——这是整个级数理论中最省力的一个定理：**只要各项非负，判断收敛就只需要找一个上界，连极限都不用算**。Colding 在视频里专门强调了这条思维路径：非负项 ⟹ 部分和单调 ⟹ 收敛 ⟺ 有界。🎥 *Colding 在视频中说:* "if all of the elements, an, is non-negative, then this sequence, sn, is monotone increasing. And so... to determine whether this series here is convergent or not, it's just a matter of proving... whether this sequence is bounded or not."（翻译：如果所有项 $a_n$ 非负，那么 $s_n$ 单调递增，于是判断级数是否收敛就归结为证明这个序列是否有界。）
>
> 这个「归约」模式你在算法课见过无数次：把新问题归约到已知问题（reduction），是理论计算机科学的看家本领——CSAPP/6.006 里把归并排序的复杂度归约到递归树、把 NP 问题归约到 3-SAT，都是同一个思维动作。**数学证明和算法设计共享同一套「把陌生问题翻译成熟知问题」的心智模型。** 下一节 $\sum \frac{1}{i^2}$ 的例子就是这条定理的实战：只需证明部分和有界，甚至不需要知道和是多少。

---

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example: $\sum_{i=1}^{\infty} \frac{1}{i^2}$ 收敛</span>

级数

```math
\sum_{i=1}^{\infty} \frac{1}{i^2}
```

收敛。这是非负项级数，所以只需证明存在 $M$ 使得对所有 $n$，

```math
s_n = \sum_{i=1}^{n} \frac{1}{i^2} \le M.
```

**Claim（断言）：**

```math
s_{2^n - 1} \le \sum_{i=0}^{n-1} \left( \frac{1}{2} \right)^{i}.
```

这足够了，因为右边是收敛的几何级数（$c = \frac{1}{2}$），特别是它有界。

**用归纳证明 Claim。** **奠基（$n = 1$）：** $s_1 = 1 = \left( \frac{1}{2} \right)^0$，成立。**归纳步（$n \Rightarrow n+1$）：** 假设它对 $n$ 成立，则

```math
s_{2^{n+1} - 1} = s_{2^n - 1} + \sum_{i=2^n}^{2^{n+1}-1} \frac{1}{i^2} \le \sum_{i=0}^{n-1} \left( \frac{1}{2} \right)^{i} + 2^n \cdot \frac{1}{(2^n)^2} \le \sum_{i=0}^{n-1} \left( \frac{1}{2} \right)^{i} + \frac{1}{2^n} = \sum_{i=0}^{n} \left( \frac{1}{2} \right)^{i}.
```

（中间那段和共 $2^n$ 项，每一项都 $\le$ 第一项 $\frac{1}{(2^n)^2}$，故整段和 $\le 2^n \cdot \frac{1}{2^{2n}} = \frac{1}{2^n}$。）归纳步完成，Claim 得证。$\square$

> <span style="color:#7f8c8d;">TBB §3.4, p.87（p-series $\sum 1/n^p$ 特例）</span>

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这个证明是「几何级数当基准」的第一次实战：用 $\sum (1/2)^i$ 这个**已知收敛**的级数给 $\sum 1/i^2$ 的部分和「封顶」。注意证明只证明了**收敛性**，没有给出极限——事实上 $\sum_{i=1}^{\infty} \frac{1}{i^2} = \frac{\pi^2}{6}$，这是 **Euler 在 1735 年**解决的著名 Basel problem（巴塞尔问题）。Euler 的证明用到了正弦函数的无穷乘积展开，远远超出本讲工具的范围；Colding 在这里刻意选择了朴素的归纳法，就是为了不依赖任何「高级工具」。🎥 *Colding 在视频中解释了这个教学选择:* "this is not necessarily how I would do it... the advantage with this here is that it doesn't use anything fancy."（翻译：这未必是我通常会用的方法……这个方法的优点是不用任何花哨的工具。）
>
> **「存在性证明 vs 精确值」的区分**值得记住：本讲证明的是「$\sum 1/i^2$ 收敛」（存在极限），Basel 问题是「极限恰好是 $\frac{\pi^2}{6}$」（算出精确值）。两者难度天差地别——前者只需一个上界，后者需要天才的一击。这个区分贯穿整个分析学：很多问题我们先证明「存在」，再（或许永远无法）求「是多少」。你在 6.006 里也见过类似现象：证明「存在最优解」容易，求出具体最优解难。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 把本讲两个「亲手证明」的级数放在一起，你会看到一个更一般的规律正在浮现：$\sum \frac{1}{n}$（$p=1$）发散，$\sum \frac{1}{n^2}$（$p=2$）收敛。这暗示存在一个**临界指数**：对于形如 $\sum_{n=1}^{\infty} \frac{1}{n^p}$ 的级数（称为 **p-series**），当 $p > 1$ 时收敛，当 $p \le 1$ 时发散——也就是说，$p=1$ 正是收敛与发散的分水岭。直觉上，$p$ 控制的是通项 $\frac{1}{n^p}$ 趋于零的「速度」：$p$ 越大，尾巴越薄，无穷求和越容易收敛。$p=1$ 恰好是「不够快」的边界——调和级数的项 $\frac{1}{n}$ 衰减得太慢，无限多组 $2^n$ 项还能每组凑出 $\frac{1}{2}$ 的量级；而 $p=2$ 时衰减快了一档，相同分组方式下每组贡献呈几何衰减。这个直觉的严格证明需要积分判别法（integral test），它把 $\sum \frac{1}{n^p}$ 的敛散性归约到 $\int_1^{\infty} \frac{1}{x^p} dx$ 的敛散性——而反常积分 $\int_1^{\infty} x^{-p} dx$ 恰好在 $p > 1$ 时收敛，与 p-series 的分界线完全吻合。Colding 选择不讲积分判别法（留到后续讲次），但你现在已经可以在脑子里画出这张图：$p$ 轴上，$p=1$ 左边（包括 $p=1$）全是「发散区」，右边全是「收敛区」。这条分界线后面会反复出现：L08 的积分判别法将给出完整证明（TBB §3.6, p.104 用凝聚法已给出 p-harmonic 的完整收敛行为）；你大二上要学的概率论（6.431, Bertsekas）中，随机变量期望 $E[X] = \sum x \cdot P(X=x)$ 是否存在也依赖同样的尾巴比较——若 $P(X=n)$ 衰减得像 $\frac{1}{n^p}$，则 $p > 2$ 时期望才有限。参考：TBB §3.4, p.87（p-series）。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">Convergence Tests（收敛判别法总览）</span>

为了判断一个级数是否收敛，有一系列 **tests（判别法）**：

- **Comparison test（比较判别法）**——本讲介绍两种版本。
- **Ratio test（比值判别法）**——本讲介绍。
- **Root test（根值判别法）**——下一讲 L08 介绍。

（Colding 在课上还提到了 integral test（积分判别法）与 alternating series test（交错级数判别法），但均留待后续讲次。🎥 *Colding 在课上强调选择判别法的关键是:* "the key point is to use the right test."（翻译：关键点是使用正确的判别法。））

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 判别法不是一个「按顺序挨个试」的机械清单，而是一个**工具箱**——关键在于「先看问题形状，再选工具」。大致的形状识别指南：（1）**含阶乘或指数项**（如 $n!$、$2^n$、$n^n$）→ 比值判别法或根值判别法，因为相邻项比值容易化简，指数在比值中会消掉；（2）**含 $n$ 次幂**（如 $n^{-p}$、含 $\sqrt[n]{\ }$ 的项）→ 根值判别法，因为 $n$ 次根号恰好消掉指数；（3）**看起来像某个已知级数加低阶扰动**（如 $\frac{1}{n^2-1}$、$\frac{2^{-n}}{n}$）→ 比较判别法，把低阶项扔掉或放大后和基准级数比。Colding 强调「用对工具」而不是「试遍所有工具」——这和算法设计中选择数据结构的心智完全一致：你不会对排序问题挨个试堆、哈希表、平衡树，而是先看操作模式（频繁插入？随机访问？）再选。这里一样：**拿到级数先花 10 秒扫描 $a_n$ 的形状，而不是立刻开始算极限。** 另外，$a_n \not\to 0$ 永远是第一道关口——如果通项都不趋于零，连工具箱都不用打开，直接判发散。下一讲 L08 会补齐根值判别法，并引入积分判别法和交错级数判别法，届时工具箱才算完整。

---

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">Comparison Test, Version 1（比较判别法，第一版）</span>

设 $a_n$ 与 $b_n$ 是两个序列，满足

```math
0 \le a_n \le b_n.
```

若 $\sum_{n=1}^{\infty} b_n$ 收敛，则 $\sum_{n=1}^{\infty} a_n$ 也收敛。

> <span style="color:#7f8c8d;">TBB §3.6, p.101（Direct Comparison Test I, Theorem 3.19）</span>

**Example（例）：** 级数

```math
\sum_{n=1}^{\infty} \frac{2^{-n}}{n}
```

收敛。事实上，令 $a_n = \frac{2^{-n}}{n}$，$b_n = 2^{-n}$，则 $0 \le a_n \le b_n$；而 $\sum b_n$ 是几何级数（$c = \frac{1}{2}$），收敛。由比较判别法，$\sum a_n$ 收敛。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这个例子的直觉是「**缩小分母让项变大，仍然收敛，所以原级数更收敛**」：$\frac{2^{-n}}{n} \le 2^{-n}$，而 $\sum 2^{-n}$ 是指数衰减的几何级数。注意比较的方向：我们要证明**收敛**，所以必须用一个**更大的、已知收敛**的级数压住它。如果你搞反方向——比如想证 $\sum \frac{1}{n}$ 收敛，说「$\frac{1}{n} \le 1$ 而 $\sum 1$ 发散，所以……」——这什么都推不出来。**用一个更大的发散级数做上界，不能推出原级数发散；同理，用一个更小的收敛级数做下界，不能推出原级数收敛。** 核心记忆口诀：**「大收敛 ⟹ 小收敛，小发散 ⟹ 大发散」**——想象一个「收敛上界」像天花板压住下面的一切，「发散下界」像地板撑开上面的一切。这两个方向是不对称的：小收敛推不出任何东西，大发散也推不出任何东西。这个不等式的方向敏感性，你在 L05 的夹逼定理（squeeze theorem）里已经见过完全相同的逻辑——夹逼需要两侧趋于同一个极限，光有一侧不够。发散方向的应用本讲没展开，但 L08 会用调和级数 $\sum 1/n$ 作为「发散下界」来证明别的级数发散，届时你会看到这个「地板效应」的实战。

---

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">Comparison Test, Version 2（比较判别法，第二版）</span>

设 $a_n$ 与 $b_n$ 是两个序列，$b_n \ne 0$，且

```math
\lim_{n \to \infty} \frac{a_n}{b_n} = L \ne 0.
```

则 $\sum_{n=1}^{\infty} a_n$ 收敛当且仅当 $\sum_{n=1}^{\infty} b_n$ 收敛。

> <span style="color:#7f8c8d;">TBB §3.6, p.104（Limit Comparison Test, Theorem 3.23）</span>

**Example（例）：** 级数

```math
\sum_{n=2}^{\infty} \frac{1}{n^2 - 1}
```

收敛。因为

```math
\frac{n^2}{n^2 - 1} \to 1 \quad (n \to \infty),
```

而 $\sum_{n=2}^{\infty} \frac{1}{n^2}$ 收敛（上一节已证），由第二版比较判别法，原级数收敛。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 第二版的本质是 **「渐近同阶」**：$\frac{a_n}{b_n} \to L \ne 0$ 意味着 $a_n$ 与 $b_n$ 在 $n$ 很大时**成正比**（$a_n \approx L b_n$），所以两者敛散性一致。这正是你在 CLRS 第 3 章学过的 **$\Theta$ notation（渐近紧确界）**：$a_n = \Theta(b_n)$ 当且仅当 $\lim \frac{a_n}{b_n}$ 存在且非零（在 $b_n > 0$ 时）。**算法分析里的「同阶复杂度」，在级数理论里就是「同敛散」**——同一个数学事实，两个学科各用各的语言。🎥 *Colding 在视频中总结了两个版本的用法:* "it's used in both ways. It's used to both determine that a series is convergent. And it's also used to determine that the series is divergent."（翻译：它有两种用法——既用来判定级数收敛，也用来判定级数发散。）
>
> 例子里 $\frac{1}{n^2 - 1}$ 的处理是个好模板：分母里的「$-1$」是低阶项，**不影响** $n \to \infty$ 时的主导行为（$\frac{1}{n^2 - 1} \sim \frac{1}{n^2}$），于是直接和 $\sum \frac{1}{n^2}$ 比。这就是「抓主导项」的思想——你在 CSAPP 性能分析（哪项主导循环开销）和 6.006 复杂度分析（只看最高次项）里每天都在用。

---

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b;">Ratio Test（比值判别法）</span>

设 $a_n \ge 0$，且

```math
\frac{a_{n+1}}{a_n} \to a.
```

则：

- 若 $a < 1$，级数 $\sum a_n$ **收敛**；
- 若 $a > 1$，级数 $\sum a_n$ **发散**；
- 若 $a = 1$，判别法**失效**（inconclusive，无法判定）。

> <span style="color:#7f8c8d;">TBB §3.6, p.107（d'Alembert's Ratio Test, Theorem 3.28）</span>

**Example 1（例 1）：** 取 $a_n = \frac{1}{n}$。此时 $\frac{a_{n+1}}{a_n} \to 1$，判别法失效——但该级数（调和级数）发散。

**Example 2（例 2）：** 取 $a_n = \frac{1}{n^2}$。此时 $\frac{a_{n+1}}{a_n} \to 1$，判别法同样失效——但该级数收敛。

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 比值判别法的直觉是**把级数与几何级数暗中比较**：$\frac{a_{n+1}}{a_n} \to a$ 意味着 $a_n$ 大致以公比 $a$ 等比衰减（$a_n \approx \text{const} \cdot a^n$）。$a < 1$ 时它衰减得像收敛的几何级数（$\sum a^n$ 收敛），$a > 1$ 时增长得像发散的几何级数。所以比值判别法本质上就是「**和几何级数比增长率**」——再次印证了几何级数的基准地位。
>
> 两个例子的对比是**故意设计的教学陷阱**：$a_n = \frac{1}{n}$ 和 $a_n = \frac{1}{n^2}$ 的比值极限都是 $1$，但一个发散一个收敛。这说明 $a = 1$ 是「临界点」——比值恰好为 $1$ 意味着衰减速度是「多项式级」的，而几何级数只刻画「指数级」的衰减，两者在临界点处需要更精细的工具（积分判别法）才能区分。用复杂度语言说：比值判别法只能区分**指数级**快慢，多项式级差异（$\frac{1}{n}$ vs $\frac{1}{n^2}$）它看不见。🎥 *Colding 在结尾预告了积分判别法的直觉:* "the integral test is that you're looking at a series... you can think about that the series is like the area below... the sum as the sum of the areas."（翻译：积分判别法是把级数看成曲线下方的面积——级数求和就是小矩形面积之和，与曲线下的面积比较。）这个「级数 = 面积」的视角在 L17 引入 Riemann integral 后会彻底兑现。

---

### <span style="color:#2471a3;">**[note]**</span> <span style="color:#c0392b">References（参考文献）</span>

- **[TBB]** B.S. Thomson, J.B. Bruckner, and A.M. Bruckner, *Elementary Real Analysis*, 2nd edition
  - TBB 可下载于（screen-optimized，屏幕优化版）：https://classicalrealanalysis.info/com/documents/TBB-AllChapters-Landscape.pdf
  - （print-optimized，打印优化版）：https://classicalrealanalysis.info/com/documents/TBB-AllChapters-Portrait.pdf

<span style="color:#7f8c8d;">MIT, Dept. of Math., 77 Massachusetts Avenue, Cambridge, MA 02139-4307. · MIT OpenCourseWare https://ocw.mit.edu · 18.100B Real Analysis, Spring 2025</span>
