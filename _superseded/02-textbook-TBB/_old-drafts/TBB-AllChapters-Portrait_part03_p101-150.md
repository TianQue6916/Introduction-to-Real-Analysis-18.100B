# <span style="color:#c0392b">TBB《Elementary Real Analysis》· Chapter 3: Infinite Sums（第 3 章：无穷和）§3.6–§3.7 双语精译</span>****

> <span style="color:#7f8c8d;">源文件：TBB-AllChapters-Portrait_part003_p101-150.pdf（书页 101–150）| 本文件覆盖 §3.6（Tests for Convergence，收敛判别法）正文与 §3.7（Rearrangements，重排）正文 | 习题区保持英文原文，未收录</span>

---

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">3.6 Tests for Convergence（收敛判别法）</span>

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">3.6.1 Infinite Sums（无穷和）</span>

第一个判别法不过是我们关于 series（级数）早已做过的一个观察：如果级数 $\sum_{k=1}^{\infty} a_k$ 收敛，那么 $a_k \to 0$。我们把这个观察反过来使用，就得到 divergence test（发散判别法）。

例如，有些初学者会对着级数 $\sum_{k=1}^{\infty} \frac{1}{\sqrt[k]{k}}$ 发愁很久，给它套用一整套判别法来判定敛散性。而判断这个级数发散的最简单方法，是注意到它的通项当 $k \to \infty$ 时趋于 $1$（因为 $\sqrt[k]{k} \to 1$）。也许这才是面对任何级数时首先应该考虑的事：如果通项不变小，就没有必要纠结级数是否收敛——它不收敛。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 3.18 (Trivial Test, 平凡判别法)</span>

> <span style="color:#7f8c8d;">TBB §3.6.1, p.112</span>

若级数 $\sum_{k=1}^{\infty} a_k$ 的通项不收敛于 $0$，则该级数发散。

[proof] **Proof（证明）**（虚化显示）:

> 我们早已证明过这一结论，但这里把它作为 Cauchy criterion（柯西准则）的特例再证一次：对任意 $\varepsilon > 0$，存在 $N$，使得对所有 $n \ge N$ 都有
> 
> ```math
> |a_n| = \left|\sum_{k=n}^{n} a_k\right| < \varepsilon ,
> ```
> 
> 于是按定义 $a_k \to 0$。$\square$

> <span style="color:#1e8449;">**[note] Note（译者注）——"必要条件"型判别法的第一性原理：**</span>
> 这个判别法看似平凡，但它揭示了 series（级数）与 sequence（数列）之间最本质的差距：**数列收敛要求整体趋近一个极限，而级数收敛要求"尾巴"不断收缩**。$a_k \to 0$ 只是级数收敛的 necessary condition（必要条件）——它排除了"通项停在某个非零水平"的级数，却无法排除通项缩小得不够快的情形（harmonic series（调和级数）$\sum 1/k$ 就是最好的反例：$1/k \to 0$ 但级数发散）。你在 6.042J（MIT 离散数学课）学过的逻辑框架在这里直接复用：$P \Rightarrow Q$ 的逆否命题 $¬Q \Rightarrow ¬P$ 是有效的推理方向，而 $Q \Rightarrow P$ 则不一定成立——Trivial Test 正是用逆否命题把"收敛 ⟹ 通项趋于零"翻转成"通项不趋于零 ⟹ 发散"。那个例子 $\sum 1/\sqrt[k]{k}$ 之所以"坑"初学者，是因为 $\sqrt[k]{k} = k^{1/k} = e^{(\ln k)/k} \to e^0 = 1$ 用到了指数与对数的极限事实（这在前一章已经建立），表面看似"分子分母都在变大"，实际通项根本不离开发散区。**使用时机模板**：拿到任何级数的第一步永远是检查 $a_k \to 0$——这是零成本的第一道过滤，只有通过它才值得继续投入更精细的判别法。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">3.6.2 Direct Comparison Tests（直接比较判别法）</span>

所有项都非负的级数 $\sum_{k=1}^{\infty} a_k$，可以通过估计其 partial sums（部分和）的大小来处理。与其直接做估计，有时更容易的做法是**找一个收敛的、更大的级数**：这个更大的级数自动为我们的级数提供一个 upper bound（上界），省去我们自己动手计算的麻烦。

[note] **原文注意（Note）**：务必只把这些判别法用于非负项级数——对于 arbitrary series（任意项级数），这类信息毫无用处。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 3.19 (Direct Comparison Test I, 直接比较判别法 I)</span>

> <span style="color:#7f8c8d;">TBB §3.6.2, p.112</span>

设级数 $\sum_{k=1}^{\infty} a_k$ 的每一项都小于级数 $\sum_{k=1}^{\infty} b_k$ 的对应项，即对所有 $k$ 都有

```math
0 \le a_k \le b_k .
```

若较大的级数收敛，则较小的级数也收敛。

[proof] **Proof（证明）**（虚化显示）:

> 若对所有 $k$ 有 $0 \le a_k \le b_k$，则
> 
> ```math
> \sum_{k=1}^{n} a_k \;\le\; \sum_{k=1}^{n} b_k \;\le\; \sum_{k=1}^{\infty} b_k .
> ```
> 
> 于是数 $B = \sum_{k=1}^{\infty} b_k$ 是级数 $\sum_{k=1}^{\infty} a_k$ 的部分和序列的一个上界。由于 $a_k \ge 0$，部分和单调递增，故由 monotone convergence theorem（单调收敛定理，见 §2.9）可知 $\sum_{k=1}^{\infty} a_k$ 必收敛。$\square$

[note] **原文注意（Note）**：在应用这个判别法以及后续所有要求级数各项满足某种条件的判别法时，应记住：级数 $\sum a_k$ 的收敛或发散只取决于 $a_k$ 在 $k$ 很大时的行为。因此这个判别法（以及许多其他判别法）都可以改写成"只对大于某个整数 $N$ 的 $k$ 成立"的形式——这就是 finite initial segment（有限前段）不影响敛散性的体现。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 3.20 (Direct Comparison Test II, 直接比较判别法 II)</span>

> <span style="color:#7f8c8d;">TBB §3.6.2, p.113</span>

设级数 $\sum_{k=1}^{\infty} a_k$ 的每一项都大于级数 $\sum_{k=1}^{\infty} c_k$ 的对应项，即对所有 $k$ 都有

```math
0 \le c_k \le a_k .
```

若较小的级数发散，则较大的级数也发散。

[proof] **Proof（证明）**（虚化显示）:

> 这由 Test 3.19 直接推出：若较大的级数不发散，则它必收敛（非负项级数只有收敛与发散两种结局），于是由 Test 3.19 较小的级数也收敛，与假设矛盾。$\square$

> <span style="color:#1e8449;">**[note] Note（译者注）——比较判别法在"敲定"什么：**</span>
> 直接比较判别法的本质，是把**未知级数的敛散性归约为已知级数的敛散性**，代价是两条：第一，你必须"发明"一个可比较的已知级数（教材原文用 invent 这个词，这正是方法的核心难度）；第二，你要做一段 inequality work（不等式功夫）来证明逐项比较成立。两个版本（I 型找收敛的上界、II 型找发散的下界）合在一起，正好对应收敛性判定的完整逻辑：**证明收敛只需一个收敛的上界，证明发散只需一个发散的下界**——中间的项怎么折腾都不重要。这与你在 CLRS 中见过的 divide and conquer（分治）复杂度分析是同一个思想骨架：证明 $T(n) = O(n \log n)$ 时，你只需要找一个更大的已知上界把 $T(n)$ 夹住，不需要精确计算每一项。值得注意的是，"只改有限前段不影响敛散性"这一条（正文的原文 Note）是后续所有判别法的通用前提：Ratio Test、Integral Test 等全部只关心 $k \to \infty$ 的行为，因为它背后的原理正是比较判别法。

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 3.21（例 3.21）</span>

> <span style="color:#7f8c8d;">TBB §3.6.2, p.113</span>

考虑级数

```math
\sum_{k=1}^{\infty} \frac{k+5}{k^3 + k^2 + k + 1} .
```

虽然部分和乍看难以估计，但快速一瞥就提示：其通项在 $k$ 很大时（粗略地）类似于 $1/k^2$，而我们已知 $\sum_{k=1}^{\infty} 1/k^2$ 收敛。注意到

```math
\frac{k+5}{k^3+k^2+k+1}
= \frac{1+5/k}{k^2(1+1/k+1/k^2+1/k^3)}
\le \frac{C}{k^2}
```

对某个常数 $C$ 成立（例如取 $C = 6$ 即可）。于是断言：给定级数通过与收敛级数 $\sum_{k=1}^{\infty} C/k^2$ 直接比较而收敛。（这是一个 p-harmonic series（p 级数），$p = 2$。）$\blacksquare$

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 3.22（例 3.22）</span>

> <span style="color:#7f8c8d;">TBB §3.6.2, p.114</span>

考虑级数

```math
\sum_{k=1}^{\infty} \sqrt{\frac{k+5}{k^2 + k + 1}} .
```

同样，快速一瞥提示：其通项在 $k$ 很大时（粗略地）类似于 $1/\sqrt{k}$，而我们已知 $\sum_{k=1}^{\infty} 1/\sqrt{k}$ 发散。注意到

```math
\frac{k+5}{k^2+k+1}
= \frac{1+5/k}{k(1+1/k+1/k^2)}
\ge \frac{C}{k}
```

对某个常数 $C$ 成立（例如取 $C = 1/4$ 即可）。于是断言：给定级数通过与发散级数 $\sum_{k=1}^{\infty} C/\sqrt{k}$ 直接比较而发散。（这是一个 p-harmonic series，$p = 1/2$。）$\blacksquare$

这两个例子同时展示了该方法的优势与劣势：我们必须**发明**被比较的级数，还必须做一定量的不等式工作来证明比较成立。接下来的判别法用极限运算取代不等式工作，而极限运算偶尔会更容易执行。

> <span style="color:#1e8449;">**[note] Note（译者注）——p-harmonic series 是级数世界的"脚手架"：**</span>
> Example 3.21/3.22 反复用到的 p-harmonic series（p 级数）$\sum 1/k^p$ 在级数理论中扮演的角色，就像 $n^k$ 与 $e^n$ 在算法复杂度分析中的角色——它们是**基准刻度**：$p \le 1$ 发散、$p > 1$ 收敛，全部由 §3.5 的 integral test（积分判别法）或几何级数比较建立。记忆锚点：$p = 1$ 是分界线，harmonic series 本身站在发散的边缘；$p = 2$ 收敛（Basel 问题，Euler 1735 算出 $\sum 1/k^2 = \pi^2/6$），$p = 1/2$ 发散。实际解题时，任何"分子分母都是多项式"的有理型通项，第一反应就是看最高次幂决定它与哪个 $1/k^p$ 同阶——这就是这两个例子演示的 fast glance（快速一瞥）技能，它把不等式功夫压缩成了一次"次数匹配"。这个直觉在算法分析里完全平行：比较两个函数增长阶时你只关心 leading term（首项），常数因子与低阶项一律忽略。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">3.6.3 Limit Comparison Tests（极限比较判别法）</span>

我们已经看到，所有项非负的级数 $\sum_{k=1}^{\infty} a_k$ 可以通过与一个更大的收敛级数、或一个更小的发散级数比较来处理。与其逐一检查两个被比较级数的每一项，更方便的做法是让一次 limit（极限）计算自动完成这种检查。在本节中，由于判别法涉及分式，我们不仅必须确保所有项非负，还必须确保没有除以零。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 3.23 (Limit Comparison Test I, 极限比较判别法 I)</span>

> <span style="color:#7f8c8d;">TBB §3.6.3, p.114</span>

设每个 $a_k \ge 0$ 且 $b_k > 0$。若级数 $\sum_{k=1}^{\infty} a_k$ 与级数 $\sum_{k=1}^{\infty} b_k$ 可以通过计算

```math
\lim_{k \to \infty} \frac{a_k}{b_k} \;<\; \infty
```

来比较，且后者收敛，则前者也收敛。

[proof] **Proof（证明）**（虚化显示）:

> 证明很容易。若所说的极限存在且有限，则存在数 $M$ 和 $N$，使得对所有 $k \ge N$ 有
> 
> ```math
> \frac{a_k}{b_k} < M .
> ```
> 
> 这说明对所有 $k \ge N$ 有 $a_k \le M b_k$。于是应用直接比较判别法，级数 $\sum_{k=N}^{\infty} a_k$ 通过与收敛级数 $\sum_{k=N}^{\infty} M b_k$ 比较而收敛。$\square$

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 3.24 (Limit Comparison Test II, 极限比较判别法 II)</span>

> <span style="color:#7f8c8d;">TBB §3.6.3, p.114–115</span>

设每个 $a_k > 0$ 且 $c_k > 0$。若级数 $\sum_{k=1}^{\infty} a_k$ 与级数 $\sum_{k=1}^{\infty} c_k$ 可以通过计算

```math
\lim_{k \to \infty} \frac{a_k}{c_k} \;>\; 0
```

来比较，且后者发散，则原级数也发散。

[proof] **Proof（证明）**（虚化显示）:

> 由于极限存在且不为零，存在数 $\varepsilon > 0$ 和 $N$，使得对所有 $k \ge N$ 有
> 
> ```math
> \frac{a_k}{c_k} > \varepsilon ,
> ```
> 
> 即对所有 $k \ge N$ 有 $a_k \ge \varepsilon c_k$。于是由直接比较判别法，级数 $\sum_{k=N}^{\infty} a_k$ 通过与发散级数 $\sum_{k=N}^{\infty} \varepsilon c_k$ 比较而发散。$\square$

> <span style="color:#1e8449;">**[note] Note（译者注）——"商极限"如何把不等式工作外包给极限：**</span>
> 比较判别法要求逐项不等式 $a_k \le b_k$，而极限比较只要求商 $\lim a_k/b_k$ 存在且有限（I 型）或为正（II 型）。两者的关系是：**极限存在且有限 $\Rightarrow$ 比值最终有界**——这正是证明里 $M$ 与 $N$ 的来源。可以把这理解为"用极限运算自动完成不等式功夫"：你不再需要手工验证每一项，只需要算一个极限。两个方向的对称性值得记住：I 型用"比值有限"配合"上界收敛"，II 型用"比值为正"配合"下界发散"——前者排除比值爆炸（$\infty$），后者排除比值塌缩（$0$）。这与 Example 3.25/3.26 中"两次快速一瞥 + 一次极限"的工作流完全对应：先凭直觉猜一个同阶的基准级数，再算商极限验证。注意两种判别法有个不对称的细节：I 型允许 $a_k \ge 0$，II 型要求 $a_k > 0$——因为 II 型需要保证"每一项都真大于下界"时才敢用发散方向，若某项为零则 $a_k \ge \varepsilon c_k$ 仍成立，但若所有 $a_k$ 中混入负号，直接比较的推理就断裂了。

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 3.25（例 3.25）</span>

> <span style="color:#7f8c8d;">TBB §3.6.3, p.115</span>

我们把例 3.21 与 3.22 重做一遍——之前用的是直接比较判别法，这次改用极限比较判别法。先再看级数

```math
\sum_{k=1}^{\infty} \frac{k+5}{k^3 + k^2 + k + 1} ,
```

如之前一样，把它与收敛级数 $\sum_{k=1}^{\infty} 1/k^2$ 比较。这现在需要计算极限

```math
\lim_{k \to \infty} \frac{k^2 (k+5)}{k^3 + k^2 + k + 1} ,
```

初等微积分论证表明它等于 $1$。由于它不是无穷大，原级数现在可以断言：由极限比较判别法收敛。$\blacksquare$

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 3.26（例 3.26）</span>

> <span style="color:#7f8c8d;">TBB §3.6.3, p.115</span>

再考虑级数

```math
\sum_{k=1}^{\infty} \sqrt{\frac{k+5}{k^2 + k + 1}} ,
```

与发散级数 $\sum_{k=1}^{\infty} 1/\sqrt{k}$ 比较。我们需要计算极限

```math
\lim_{k \to \infty} \sqrt{k} \cdot \sqrt{\frac{k+5}{k^2 + k + 1}} ,
```

初等微积分论证表明它等于 $1$。由于它不是零，原级数现在可以断言：由极限比较判别法发散。$\blacksquare$

> <span style="color:#1e8449;">**[note] Note（译者注）——极限比较 vs 直接比较的"复杂度"视角：**</span>
> 例 3.25/3.26 与例 3.21/3.22 处理的是同一对级数，但工作量明显不同：直接比较需要手工构造常数 $C$ 并验证不等式（$C = 6$、$C = 1/4$ 都是人为挑选的），极限比较只需要算两个初等极限，且结果都是干净的 $1$。这正是教材说的"极限运算取代不等式工作"。用你熟悉的算法语言说：直接比较相当于手工做 worst-case analysis（最坏情况分析）——必须显式给出常数；极限比较相当于 asymptotic analysis（渐近分析）——只关心增长阶是否相同。极限等于 $1$ 不是巧合：两个通项本来就和基准 $1/k^2$、$1/\sqrt{k}$ 同阶，商极限自然收敛到主导项之比。**实用模板**：先对通项做"次数匹配"（分子分母最高次幂之比）猜出基准级数，再算商极限——若得非零有限常数，则两者同敛散；若得 $0$ 或 $\infty$，说明猜的基准阶太高或太低，换一个基准重试。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">3.6.4 Ratio Comparison Test（比值比较判别法）</span>

我们再次希望比较两个由正项组成的级数 $\sum_{k=1}^{\infty} a_k$ 与 $\sum_{k=1}^{\infty} b_k$。与直接比较各项大小不同，这次我们比较各项的 ratio（比值）。这个判别法的灵感来自试图把一个级数与收敛的 geometric series（几何级数）直接比较：若 $\sum b_k$ 是公比为 $r$ 的几何级数，则显然有 $b_{k+1}/b_k = r$。这提示我们：比较相邻两项的比值，或许能指示一个级数以多快的速度收敛。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 3.27 (Ratio Comparison Test, 比值比较判别法)</span>

> <span style="color:#7f8c8d;">TBB §3.6.4, p.115–116</span>

若比值满足

```math
\frac{a_{k+1}}{a_k} \le \frac{b_{k+1}}{b_k}
```

对所有 $k$ 成立（或仅对充分大的 $k$ 成立），且具有较大比值的级数 $\sum_{k=1}^{\infty} b_k$ 收敛，则级数 $\sum_{k=1}^{\infty} a_k$ 也收敛。

[proof] **Proof（证明）**（虚化显示）:

> 照例，我们假设两个级数所有项均为正。若比值对 $k > N$ 满足 $a_{k+1}/a_k \le b_{k+1}/b_k$，则它们也满足
> 
> ```math
> \frac{a_{k+1}}{b_{k+1}} \le \frac{a_k}{b_k} ,
> ```
> 
> 这意味着序列 $\{a_k/b_k\}$ 对 $k > N$ 是递减的。特别地，该序列有上界，设为 $C$，于是 $a_k \le C b_k$。从而应用直接比较判别法可知级数 $\sum_{k=1}^{\infty} a_k$ 收敛。$\square$

> <span style="color:#1e8449;">**[note] Note（译者注）——比值比较在做什么"工程"：**</span>
> 注意证明中的关键代数操作：把"两个比值逐项比较"改写成"**比值序列 $\{a_k/b_k\}$ 单调递减**"。这是把不等式条件翻译成序列性质，然后借助"递减 ⟹ 有上界"这一廉价事实拿到 $a_k \le Cb_k$，最后落回直接比较判别法。整条推理链只有四步，每一环都是已学过的工具：比值交叉相乘（初等代数）→ 单调序列有界（§2 序列理论）→ 直接比较（§3.6.2）。它体现了一个可复用的证明策略，不妨命名为**"比值转序列法"**：凡遇到"逐项之比满足某不等式"的条件，先问"这个不等式能不能改写成某个序列的单调性？"——单调性一旦到手，有界性、收敛性随之而来。这与你在 CSAPP（Computer Systems: A Programmer's Perspective，深入理解计算机系统）里调试程序时的思路同构：把难验证的全局性质（每个比值都比对方小）转化为容易验证的局部性质（商序列单调），再让单调性这种"强结构"替你完成剩下的事。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">3.6.5 d'Alembert's Ratio Test（达朗贝尔比值判别法）</span>

比值比较判别法要求挑选一个用于比较的级数。通常可以选用某个 $0 < r < 1$ 的几何级数 $\sum_{k=1}^{\infty} r^k$。我们如何计算一个能用的 $r$ 呢？我们希望取 $b_k = r^k$，并选择 $r$ 使得

```math
\frac{a_{k+1}}{a_k} \le \frac{b_{k+1}}{b_k} = \frac{r^{k+1}}{r^k} = r .
```

一个寻找这样的 $r$ 是否存在且简单易行的办法，是计算比值 $a_{k+1}/a_k$ 的极限。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 3.28 (Ratio Test, 比值判别法)</span>

> <span style="color:#7f8c8d;">TBB §3.6.5, p.116</span>

若级数 $\sum_{k=1}^{\infty} a_k$ 的各项均为正，且比值满足

```math
\lim_{k \to \infty} \frac{a_{k+1}}{a_k} < 1 ,
```

则级数 $\sum_{k=1}^{\infty} a_k$ 收敛。

[proof] **Proof（证明）**（虚化显示）:

> 证明很容易。若 $\lim_{k \to \infty} a_{k+1}/a_k < 1$，则存在数 $\beta < 1$，使得对所有充分大的 $k$ 有 $a_{k+1}/a_k < \beta$。于是由比值比较判别法（作用于收敛的几何级数 $\sum_{k=1}^{\infty} \beta^k$）可知级数 $\sum_{k=1}^{\infty} a_k$ 收敛。$\square$

[note] **原文注意（Note）**：比值判别法也可以推出发散结论：若

```math
\lim_{k \to \infty} \frac{a_{k+1}}{a_k} > 1
\tag{4}
```

则级数 $\sum_{k=1}^{\infty} a_k$ 发散。但最好淡化这一方向，否则你可能以为它给出的结论与收敛方向的结论一样有用。由 (4) 可知必存在 $N$ 与 $\beta$，使得对所有 $k \ge N$ 有

```math
\frac{a_{k+1}}{a_k} > \beta > 1 .
```

于是 $a_{N+1} > \beta a_N$，$a_{N+2} > \beta a_{N+1} > \beta^2 a_N$，$a_{N+3} > \beta a_{N+2} > \beta^3 a_N$。我们看到级数的通项 $a_k$ 以几何速率迅速增长——不仅级数发散，而且是以戏剧性的方式发散。

**如何最好地应用该判别法（原文总结）：** 若级数 $\sum a_k$ 各项均为正，计算

```math
\lim_{k \to \infty} \frac{a_{k+1}}{a_k} = L .
```

1. 若 $L < 1$，则级数 $\sum a_k$ 收敛。
2. 若 $L > 1$，则级数 $\sum a_k$ 发散；不仅如此，通项 $a_k \to \infty$。
3. 若 $L = 1$，则级数可能发散也可能收敛，判别法失效（inconclusive）。

> <span style="color:#1e8449;">**[note] Note（译者注）——比值判别法的"边界"为什么在 $L = 1$：**</span>
> 比值判别法本质上问的是"这个级数比不比某个几何级数收敛得快"，因为几何级数 $\sum r^k$ 的相邻项比值恒等于 $r$，而判别法只是让"比值序列的极限"替你选出一个有效的 $r$。$L = 1$ 之所以失效，是因为此时通项既可能像 $1/k^2$（收敛）也可能像 $1/k$（发散）——两者比值都趋于 $1$，但敛散性截然相反。换句话说，**比值趋于 1 意味着通项衰退慢于任何几何级数**，而几何级数是比值判别法唯一能"看见"的基准。这就是为什么 $L=1$ 时需要更精细的工具（下一节的 Kummer / Raabe / Gauss 判别法正是为此设计）。发散方向的推理值得注意：$a_{N+3} > \beta^3 a_N$ 表明通项被一个大于 1 的几何因子逐项放大，所以不只是发散，而是 exponential blow-up（指数爆炸）——教材用 "diverging in a dramatic way" 形容的正是这一点，它也解释了为什么发散方向的结论"太强"而需要淡化：你损失了关于发散速度的信息。这与算法复杂度中"指数级 vs 多项式级"的区分是同一直觉。

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 3.29（例 3.29）</span>

> <span style="color:#7f8c8d;">TBB §3.6.5, p.117</span>

级数

```math
\sum_{k=0}^{\infty} \frac{(k!)^2}{(2k)!}
```

特别适合用比值判别法，因为比值容易计算、极限容易求出：设 $a_k = (k!)^2/(2k)!$，则

```math
\frac{a_{k+1}}{a_k}
= \frac{((k+1)!)^2}{(2k+2)!} \cdot \frac{(2k)!}{(k!)^2}
= \frac{(k+1)^2}{(2k+2)(2k+1)}
\to \frac{1}{4} .
```

因此这是一个收敛级数。不仅如此，它比任何几何级数 $\sum_{k=0}^{\infty} (1/4 + \varepsilon)^k$（对任意 $\varepsilon > 0$）收敛得都快。（要把"收敛得更快"这个说法精确化，见 Exercise 3.12.5。）$\blacksquare$

> <span style="color:#1e8449;">**[note] Note（译者注）——"收敛得比任何几何级数都快"是什么意思：**</span>
> 比值极限 $1/4$ 意味着：对任意 $\varepsilon > 0$，最终都有 $a_{k+1}/a_k < 1/4 + \varepsilon$，于是从某个 $N$ 起 $a_k$ 被几何级数 $(1/4+\varepsilon)^k$ 控制。由于 $\varepsilon$ 可以任意小，这个级数的"有效公比"逼近 $1/4$——它收敛的速度由 $(1/4)^k$ 主导，比公比 $1/4+\varepsilon$ 的任何几何级数都快。这里的洞见是：**比值判别法给出的不只是"收敛/发散"的判断，还有一个关于收敛速度的定量信息（比值极限本身）**。阶乘与二项式系数型通项（如 $k!$、$(2k)!$）几乎总是比值判别法的主场，因为 $((k+1)!)/(k!) = k+1$ 这类比值能约分得干干净净——这正是教材说它 "particularly suited"（特别适合）的原因。用算法语言打比方：对阶乘型通项用 Root Test 等于用 $O$ 记号去分析递归树（可行但繁琐），而 Ratio Test 相当于直接对递推式做 telescoping（相消），天然便宜。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">3.6.6 Cauchy's Root Test（柯西根值判别法）</span>

还有另一种达成"与收敛几何级数比较"的方式。我们猜想级数 $\sum a_k$ 可以与某个几何级数 $\sum r^k$ 比较，但不知道哪个 $r$ 值能用。比值 $a_{k+1}/a_k$ 的极限提供了一种确定可用 $r$ 的方法，但通常难以计算。相反，我们注意到：形如 $a_k \le C r^k$ 的比较等价于

```math
\sqrt[k]{a_k} \le \sqrt[k]{C} \, r .
```

对大的 $k$，因子 $\sqrt[k]{C}$ 接近 $1$，这启发了我们的下一个判别法——通常归功于 Cauchy（柯西）。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 3.30 (Root Test, 根值判别法)</span>

> <span style="color:#7f8c8d;">TBB §3.6.6, p.118</span>

若级数 $\sum_{k=1}^{\infty} a_k$ 的各项均为非负，且根值满足

```math
\lim_{k \to \infty} \sqrt[k]{a_k} < 1 ,
```

则该级数收敛。

[proof] **Proof（证明）**（虚化显示）:

> 这几乎是平凡的。若对所有 $k \ge N$ 有 $(a_k)^{1/k} < \beta < 1$，则 $a_k < \beta^k$，于是 $\sum_{k=1}^{\infty} a_k$ 通过与收敛的几何级数 $\sum_{k=1}^{\infty} \beta^k$ 直接比较而收敛。$\square$

**如何最好地应用该判别法（原文总结）：** 结论与比值判别法几乎相同。计算

```math
\lim_{k \to \infty} (a_k)^{1/k} = L .
```

1. 若 $L < 1$，则级数 $\sum a_k$ 收敛。
2. 若 $L > 1$，则级数 $\sum a_k$ 发散；不仅如此，通项 $a_k \to \infty$。
3. 若 $L = 1$，则级数可能发散也可能收敛，判别法失效。

> <span style="color:#1e8449;">**[note] Note（译者注）——Ratio vs Root：同一枚硬币的两面：**</span>
> 根值判别法想解决的还是同一个问题：**选一个能用的几何公比 $r$**。直接比较 $a_k \le C r^k$ 两边开 $k$ 次方，$C$ 的干扰因子 $\sqrt[k]{C} \to 1$ 自动消失，于是 $\lim \sqrt[k]{a_k}$ 直接给出"有效公比"。它与比值判别法的关系可以这样看：$\lim a_{k+1}/a_k = L$ 蕴含 $\lim \sqrt[k]{a_k} = L$（Cauchy 的一个经典引理：若相邻项比值收敛到 $L$，则几何平均也收敛到 $L$），所以**比值判别法能判定的情形根值判别法也能判定，且结论相同**——反过来不成立：根值判别法的适用范围更广。教材安排 Example 3.29 与 3.31 成对出现，正是在演示"工具选择"：阶乘型通项用 Ratio Test 轻松（比值约分干净），幂型通项 $\sum k x^k$ 用 Root Test 轻松（$(kx^k)^{1/k} = x \cdot k^{1/k} \to x$）。判别法没有绝对优劣，只有"这个通项的形状更适合哪种运算"——这是实分析里少有的、与工程选型同构的品味问题。

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 3.31（例 3.31）</span>

> <span style="color:#7f8c8d;">TBB §3.6.6, p.118–119</span>

在例 3.29 中我们看到级数 $\sum_{k=0}^{\infty} (k!)^2/(2k)!$ 用比值判别法处理起来很容易；若尝试用根值判别法直接计算，则会极其不愉快。另一方面，级数

```math
\sum_{k=0}^{\infty} k x^k = x + 2x^2 + 3x^3 + 4x^4 + \cdots
```

对 $x > 0$ 可以用这两种判别法中的任何一种处理。你可以试试比值判别法，而我们用根值判别法：

```math
\lim_{k \to \infty} \sqrt[k]{k x^k} = \lim_{k \to \infty} k^{1/k} x = x
```

于是可以断言：对一切 $0 < x < 1$ 收敛，对一切 $x > 1$ 发散。$x = 1$ 的情形对根值判别法是失效的，但 trivial test（平凡判别法）瞬间表明级数在 $x = 1$ 时发散。$\blacksquare$

> <span style="color:#1e8449;">**[note] Note（译者注）——"换工具"的示范课：**</span>
> Example 3.31 的教学意图是展示**工具与通项形状的匹配**：对 $\sum k x^k$，比值判别法需要算 $(k+1)x^{k+1}/(kx^k) = x(1+1/k) \to x$，其实也不难；但根值判别法把 $(kx^k)^{1/k} = x \cdot k^{1/k}$ 一步算完，更干净。真正精彩的是收尾处：$x = 1$ 时根值失效，教材立刻调回最廉价的工具——trivial test，看到通项 $k \cdot 1^k = k \not\to 0$ 即发散。这是一条完整的决策链：**先廉价工具（trivial test）→ 再形状匹配的精细工具（ratio/root）→ 失效时退回更基础的观察**，而不是一路堆砌判别法。这个级数 $\sum k x^k$ 本身值得记住：它是 geometric series（几何级数）$\sum x^k$ 的"导数变形"，两者都在 $|x| < 1$ 收敛——你会在后续章节（幂级数、Taylor series（泰勒级数））反复遇到它。用算法直觉说：$\sum k x^k$ 收敛半径与 $\sum x^k$ 相同，因为多项式因子 $k$ 对指数衰减 $x^k$ 只造成多项式级扰动——这正是"多项式 × 指数仍是指数主导"的增长阶判断。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">3.6.7 Cauchy's Condensation Test（柯西凝聚判别法）</span>

> <span style="color:#7f8c8d;">Enrichment section（提高部分）。可以略读。</span>

偶尔，一种用于研究某个特定级数的方法可以被推广成一个有用的判别法。回忆一下：在研究 harmonic series（调和级数）的部分和序列时，我们只观察 $1, 2, 4, 8, \ldots$ 这些步点，并据此做一个粗略的下界估计。这个方法之所以奏效，仅仅是因为调和级数的通项是递减的，于是利用这一事实，对 $s_1, s_2, s_4, s_8, \ldots$ 的估计很容易得到。这个想法很快变成了一个一般性的判别法。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 3.32 (Cauchy's Condensation Test, 柯西凝聚判别法)</span>

> <span style="color:#7f8c8d;">TBB §3.6.7, p.119</span>

若级数 $\sum_{k=1}^{\infty} a_k$ 的各项非负且单调递减到零，则该级数收敛当且仅当相关的级数

```math
\sum_{j=1}^{\infty} 2^{j} a_{2^{j}}
```

收敛。

[proof] **Proof（证明）**（虚化显示）:

> 由于所有项非负，我们只需比较两个级数部分和的大小。先计算原级数前 $2^{p+1} - 1$ 项的和，有
> 
> ```math
> a_1 + (a_2 + a_3) + \cdots + (a_{2^{p}} + a_{2^{p}+1} + \cdots + a_{2^{p+1}-1})
\le a_1 + 2a_2 + \cdots + 2^{p} a_{2^{p}} .
> ```
> 
> 再把不等式符号反过来，计算原级数前 $2^{p}$ 项的和，得到
> 
> ```math
> a_1 + a_2 + (a_3 + a_4) + \cdots + (a_{2^{p-1}+1} + a_{2^{p-1}+2} + \cdots + a_{2^{p}})
\ge \frac{1}{2} \left( a_1 + 2a_2 + \cdots + 2^{p} a_{2^{p}} \right) .
> ```
> 
> 若两个级数中任一个的部分和序列有界，则另一个也有界。因此两者同时收敛或同时发散。$\square$

> <span style="color:#1e8449;">**[note] Note（译者注）——"凝聚"到底凝聚了什么：**</span>
> 凝聚判别法把原级数 $\sum a_k$ 换成一个"采样更稀疏、但每一项乘以采样间隔"的级数 $\sum 2^j a_{2^j}$。其背后的第一性原理是：**对单调递减的正项序列，整段 $[2^j, 2^{j+1})$ 上的项之和可以被 $2^j a_{2^j}$ 从上下两个方向夹住**（区间内每项都 $\le$ 左端点值、都 $\ge$ 右端点值），于是两个级数的部分和互相有界、同敛散。这其实就是积分判别法的一个离散化雏形——把"按函数积分"换成"按指数间距采样求和"。为什么采样间距取 $2^j$ 而不是均匀间距？因为要对付的是 $a_k$ 按多项式/对数衰退的情形：均匀采样会漏掉尾部的大部分信息，而指数采样在每个数量级都恰好抓一个代表点，使凝聚级数 $\sum 2^j a_{2^j}$ 仍然是一个"好算"的级数。最经典的战果立刻兑现：p-harmonic series（p 级数）$\sum 1/k^p$ 凝聚后变成几何级数 $\sum (2^{1-p})^j$，敛散性一眼看穿——$p > 1$ 收敛、$p \le 1$ 发散，$p$ 从任意实数（含无理数）全面覆盖。这与你熟悉的二分查找（binary search）思路同源：在对数尺度上采样，用 $O(\log n)$ 个点代替 $n$ 个点来提取整体信息。

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 3.33（例 3.33）</span>

> <span style="color:#7f8c8d;">TBB §3.6.7, p.119–120</span>

让我们用这个判别法研究 p-harmonic series：

```math
\sum_{k=1}^{\infty} \frac{1}{k^p} \qquad (p > 0) .
```

其通项递减到零，所以该级数的收敛性与级数

```math
\sum_{j=1}^{\infty} 2^{j} \left( \frac{1}{2^{j}} \right)^{p}
```

的收敛性等价，而后者是几何级数

```math
\sum_{j=1}^{\infty} \left( 2^{1-p} \right)^{j} .
```

它恰好当 $2^{1-p} < 1$（即 $p > 1$）时收敛，当 $2^{1-p} \ge 1$（即 $p \le 1$）时发散。于是我们确切知道了 p-harmonic series 对所有 $p$ 值的收敛行为。（对 $p \le 0$，仅由 trivial test（平凡判别法）即可得出发散。）$\blacksquare$

值得从柯西凝聚判别法推导出一个简单判别法作为 corollary（推论）。这是对 trivial test 的一个改进：trivial test 要求收敛级数 $\sum a_k$ 满足 $\lim_{k\to\infty} a_k = 0$，而这个归功于 Abel（阿贝尔）的下一个推论表明：若通项构成单调序列，还能多说一点——序列 $\{a_k\}$ 必须比 $\{1/k\}$ 更快地趋于零。

### <span style="color:#2471a3;">**[corollary]**</span> <span style="color:#c0392b">Corollary 3.34（推论 3.34）</span>

> <span style="color:#7f8c8d;">TBB §3.6.7, p.120</span>

若收敛级数 $\sum_{k=1}^{\infty} a_k$ 的通项单调递减，则

```math
\lim_{k \to \infty} k a_k = 0 .
```

[proof] **Proof（证明）**（虚化显示）:

> 由柯西凝聚判别法可知 $\lim_{j\to\infty} 2^{j} a_{2^{j}} = 0$。若 $2^{j} \le k \le 2^{j+1}$，则 $a_k \le a_{2^{j}}$，于是
> 
> ```math
> k a_k \le 2 \left( 2^{j} a_{2^{j}} \right) ,
> ```
> 
> 对大的 $j$ 它很小。因此 $k a_k \to 0$，证毕。$\square$

> <span style="color:#1e8449;">**[note] Note（译者注）——$k a_k \to 0$ 比 $a_k \to 0$ 强在哪里：**</span>
> Corollary 3.34 是"单调收敛级数的通项不能只趋于零，还要比 $1/k$ 趋于零更快"的精确表述。它的证明是"传递性"的典范：已知 $2^j a_{2^j} \to 0$（这是凝聚级数收敛的直接推论），而任意 $k$ 都落在某个区间 $[2^j, 2^{j+1}]$ 内，单调性给出 $a_k \le a_{2^j}$，于是 $k a_k \le 2 \cdot 2^j a_{2^j} \to 0$。**命名模板"采样点外推法"**：先在被采样的特殊点（$k = 2^j$）上建立极限，再借助单调性把结论外推到所有中间点。注意调和级数正好卡在边界上：$a_k = 1/k$ 时 $k a_k = 1 \not\to 0$，所以它发散；而 $\sum 1/k^p$（$p>1$）满足 $k \cdot k^{-p} = k^{1-p} \to 0$，故收敛——Corollary 与 Condensation Test 给出的判定完全一致。这条推论后面还会以更一般的形式出现（Dirichlet test（狄利克雷判别法）里的 $b_n \searrow 0$ 条件正是这种"比 $1/k$ 快"精神的弱化版）。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">3.6.8 Integral Test（积分判别法）</span>

> <span style="color:#7f8c8d;">Enrichment section（提高部分）。可以略读。</span>

要判定非负项级数 $\sum_{k=1}^{\infty} a_k$ 的收敛性，常常需要对部分和序列的大小做某种估计。我们的大部分判别法都自动完成了这件事，省去了计算这类估计的辛劳。有时这些估计可以用微积分方法获得。Integral test（积分判别法）让我们在某些情形下通过计算 $\int_1^{n} f(x)\,dx$ 来代替估计部分和 $\sum_{k=1}^{n} f(k)$。这不仅仅是一种便利；它还揭示了级数与无穷积分之间的密切关系——这一关系在分析学中非常重要。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 3.35 (Integral Test, 积分判别法)</span>

> <span style="color:#7f8c8d;">TBB §3.6.8, p.120–121</span>

设 $f$ 是 $[1, \infty)$ 上的非负递减函数，且积分 $\int_1^{X} f(x)\,dx$ 对所有 $X > 1$ 都可计算。若

```math
\lim_{X \to \infty} \int_1^{X} f(x)\,dx < \infty
```

存在，则级数 $\sum_{k=1}^{\infty} f(k)$ 收敛。若

```math
\lim_{X \to \infty} \int_1^{X} f(x)\,dx = \infty ,
```

则级数 $\sum_{k=1}^{\infty} f(k)$ 发散。

[proof] **Proof（证明）**（虚化显示）:

> 由于 $f$ 递减，必有
> 
> ```math
> \int_{k}^{k+1} f(x)\,dx \;\le\; f(k) \;\le\; \int_{k-1}^{k} f(x)\,dx .
> ```
> 
> 对 $k = 2, 3, 4, \ldots, n$ 应用这些不等式，得到
> 
> ```math
> \int_1^{n+1} f(x)\,dx \;\le\; \sum_{k=1}^{n} f(k) \;\le\; f(1) + \int_1^{n} f(x)\,dx .
\tag{5}
> ```
> 
> 级数收敛当且仅当部分和有界。而从不等式 (5) 我们看到：若积分的极限有限，则这些部分和有界；若积分的极限为无穷，则这些部分和无界。$\square$

[note] **原文注意（Note）**：积分的收敛性给出级数的收敛性，但**并不声称**级数 $\sum f(k)$ 的和与无穷积分 $\int_1^{\infty} f(x)\,dx$ 的值相同。不过关于这一点，参见 Exercise 3.6.21。

> <span style="color:#1e8449;">**[note] Note（译者注）——积分判别法为什么"免费"：**</span>
> 积分判别法的证明核心是不等式 (5)：由于 $f$ 递减，函数值 $f(k)$ 恰好被左右两个相邻区间上的积分夹住——$f(k)$ 是区间 $[k, k+1]$ 上的最大值、$[k-1, k]$ 上的最小值。对 $k$ 求和后，级数的部分和 $\sum_{k=1}^n f(k)$ 被两个"相邻错位"的积分夹在中间，而错位只差一个 $f(1)$ 的常数项。于是"部分和有界"（级数收敛的判据）与"积分有界"（反常积分收敛的判据）互相蕴含。**命名模板"错位夹逼法"**：把一个离散和夹在两个相邻的连续积分之间，让离散与连续问题同生共死。教材的原文 Note 特别提醒：积分判别法只回答"是否收敛"，**不回答"和是多少"**——$\sum 1/k^2 = \pi^2/6$ 这类精确求值完全超出了它的能力，那是 Euler 用傅里叶分析等更深的工具才做到的。不过 Exercise 3.6.21 会展示如何从积分判别法的构造中挤出更多信息（收敛速度的界），这与你做算法复杂度分析时"用积分逼近求和"（$\sum_{k=1}^n k \approx \int x\,dx$）是完全相同的技术，只是方向反过来用。

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 3.36（例 3.36）</span>

> <span style="color:#7f8c8d;">TBB §3.6.8, p.121</span>

根据这个判别法，harmonic series $\sum_{k=1}^{\infty} 1/k$ 可以通过计算

```math
\lim_{X \to \infty} \int_1^{X} \frac{dx}{x} = \lim_{X \to \infty} \log X = \infty
```

来研究。出于同样的原因，对 $p > 1$ 的 p-harmonic series $\sum_{k=1}^{\infty} 1/k^p$ 可以通过计算

```math
\lim_{X \to \infty} \int_1^{X} \frac{dx}{x^p}
= \lim_{X \to \infty} \frac{1}{p-1} \left( 1 - \frac{1}{X^{p-1}} \right)
= \frac{1}{p-1}
```

来研究。两种情况都得到与之前相同的结论：harmonic series 发散，而对 $p > 1$，p-harmonic series 收敛。$\blacksquare$

> <span style="color:#1e8449;">**[note] Note（译者注）——三套工具，同一结论：**</span>
> 到这里，p-harmonic series 的敛散性已经被三种独立的方法各证明了一遍：直接比较/几何级数比较（§3.5）、Cauchy condensation test（例 3.33）、integral test（例 3.36）。这绝非浪费——每套工具给出一条独立的证据链，交叉验证了结论的可靠性，同时演示了"同一定理、不同武器"的解题风格。积分判别法这一路的特别之处在于：$\int_1^X x^{-p}\,dx$ 的有限性一目了然（$X^{1-p} \to 0$ 当且仅当 $p > 1$），整个判定退化为一次初等微积分计算。历史上，integral test 是 Maclaurin 与 Cauchy 在 19 世纪初（约 1742 年 Maclaurin 已隐含使用）发展起来的，它第一次把"级数求和"与"曲线下面积"这两个看似无关的问题统一起来——而你现在在第 3 章看到的这种统一，正是分析学后来走向"测度与积分"宏大理论的起点。若你想在 6.006（MIT 算法导论）的视角下理解它：积分判别法相当于用定积分的"连续复杂性"去估计离散求和的"离散复杂性"，误差只来自端点的 $f(1)$ 项——与用 $\int_{1}^{n} x \log x\,dx$ 近似 $\sum k \log k$ 的做法异曲同工。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">3.6.9 Kummer's Tests（库默尔判别法）</span>

> <span style="color:#7f8c8d;">Advanced section（进阶部分）。可以略读。</span>

比值判别法只需要对比值 $a_{k+1}/a_k$ 取极限，但它经常失效。我们知道：若这个比值趋于 $1$，比值判别法对级数 $\sum a_k$ 的敛散性就什么也说不出来。

Kummer 的判别法提供了一族比值型判别法，可以通过选取不同的序列 $\{D_k\}$ 来定制。下面的判别法中分别使用了 $D_k = 1$、$D_k = k$ 与 $D_k = k \ln k$ 这些选择。Ernst Eduard Kummer（库默尔，1810–1893）最为人熟知的是他对 Fermat's last theorem（费马大定理）研究的贡献；他的这些判别法产生于他对 hypergeometric series（超几何级数）的研究。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 3.37 (Kummer's Tests, 库默尔判别法)</span>

> <span style="color:#7f8c8d;">TBB §3.6.9, p.122</span>

级数 $\sum_{k=1}^{\infty} a_k$ 可以用以下判据来检验。设 $\{D_k\}$ 是任意正数序列，计算

```math
L = \liminf_{k \to \infty} \left[ D_k \frac{a_k}{a_{k+1}} - D_{k+1} \right] .
```

若 $L > 0$，则级数 $\sum a_k$ 收敛。另一方面，若

```math
D_k \frac{a_k}{a_{k+1}} - D_{k+1} \le 0
```

对所有充分大的 $k$ 成立，且级数 $\sum_{k=1}^{\infty} 1/D_k$ 发散，则级数 $\sum a_k$ 发散。

[proof] **Proof（证明）**（虚化显示）:

> 若 $L > 0$，则可以选取一个正数 $\alpha < L$。由 liminf（下极限）的定义，这意味着存在整数 $N$，使得对所有 $k \ge N$ 有
> 
> ```math
> \alpha < D_k \frac{a_k}{a_{k+1}} - D_{k+1} .
> ```
> 
> 改写后得到 $\alpha a_{k+1} < D_k a_k - D_{k+1} a_{k+1}$。对 $k = N, N+1, N+2, \ldots, N+p$ 写出这个不等式：
> 
> ```math
> \alpha a_{N+1} < D_N a_N - D_{N+1} a_{N+1}
> ```
> 
> ```math
> \alpha a_{N+2} < D_{N+1} a_{N+1} - D_{N+2} a_{N+2}
> ```
> 
> 依此类推。把这些不等式相加（注意这里的 telescoping sums（望远镜和，逐项相消）），得到
> 
> ```math
> \alpha (a_{N+1} + a_{N+2} + \cdots + a_{N+p+1})
< D_{N+1} a_{N+1} - D_{N+p+1} a_{N+p+1} < D_{N+1} a_{N+1} .
> ```
> 
> （最后一个不等式只用到这里所有项均为正这一事实。）
> 
> 由这个不等式我们可以断定级数 $\sum a_k$ 的部分和有界。由我们惯常的判据，这证明级数收敛。
> 
> 定理的第二部分要求建立发散性。假设对所有 $k \ge N$ 有 $D_k a_k/a_{k+1} - D_{k+1} \le 0$。则 $D_k a_k \le D_{k+1} a_{k+1}$。于是序列 $\{D_k a_k\}$ 在 $k = N$ 之后递增。特别地，对某个 $C$ 与所有 $k \ge N$ 有 $D_k a_k \ge C$，从而
> 
> ```math
> a_k \ge \frac{C}{D_k} .
> ```
> 
> 通过与发散级数 $\sum C/D_k$ 直接比较，可知我们的级数也发散。$\square$

[note] **原文注意（Note）**：在实践中，对判别法的发散部分，计算

```math
L = \limsup_{k \to \infty} \left[ D_k \frac{a_k}{a_{k+1}} - D_{k+1} \right]
```

可能更容易。若 $L < 0$，则我们知道 $D_k a_k/a_{k+1} - D_{k+1} \le 0$ 对所有充分大的 $k$ 成立，于是只要级数 $\sum 1/D_k$ 发散，级数 $\sum a_k$ 就发散。

> <span style="color:#1e8449;">**[note] Note（译者注）——Kummer 判别法为什么"包罗万象"：**</span>
> Kummer 判别法的洞察是：**比值判别法的全部信息都藏在量 $D_k a_k/a_{k+1} - D_{k+1}$ 里，而 $D_k$ 的选择是一把可调的旋钮**。取 $D_k = 1$ 得到 ratio test，取 $D_k = k$ 得到 Raabe 判别法（下一节），取 $D_k = k \ln k$ 则能处理 Raabe 失效的情形（§3.6.11 的 Gauss 判别法正是这样做的）。收敛方向的证明里最漂亮的一步是 telescoping（相消）：把逐项不等式 $\alpha a_{k+1} < D_k a_k - D_{k+1} a_{k+1}$ 从 $N$ 加到 $N+p$，中间所有 $D_{k+1}a_{k+1}$ 项首尾相消，只剩下首项 $D_{N+1}a_{N+1}$ 与尾项 $D_{N+p+1}a_{N+p+1}$——部分和 $\sum \alpha a_k$ 因此被一个固定常数夹住。这正是你在 CLRS 中反复遇到的"telescoping series"（如 $\sum (1/k - 1/(k+1))$）在证明层面的重现。发散方向则更直接：$D_k a_k \le D_{k+1} a_{k+1}$ 说明 $\{D_k a_k\}$ 单调递增，于是 $a_k \ge C/D_k$，落回直接比较。**记忆锚点**：Kummer = "带权比值"判别法，$D_k$ 是权重序列，$\liminf > 0$ 收敛、$\limsup < 0$（且 $\sum 1/D_k$ 发散）发散。

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 3.38（例 3.38）</span>

> <span style="color:#7f8c8d;">TBB §3.6.9, p.123</span>

如果选用的序列是最简单的 $D_k = 1$（对所有 $k$），Kummer 判别法会变成什么？此时它就是比值判别法。例如，设 $\lim_{k\to\infty} a_{k+1}/a_k = r$。那么把 $D_k = 1$ 代入，有

```math
\lim_{k \to \infty} \left[ D_k \frac{a_k}{a_{k+1}} - D_{k+1} \right]
= \lim_{k \to \infty} \left[ \frac{a_k}{a_{k+1}} - 1 \right]
= \frac{1}{r} - 1 .
```

于是由 Kummer 判别法：若 $1/r - 1 < 0$ 则发散，若 $1/r - 1 > 0$ 则收敛。这正是比值判别法中 $r > 1$ 与 $r < 1$ 两种情形。$\blacksquare$

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">3.6.10 Raabe's Ratio Test（拉贝比值判别法）</span>

> <span style="color:#7f8c8d;">Advanced section（进阶部分）。可以略读。</span>

比值判别法的一个简单变体称为 Raabe's test（拉贝判别法）。设

```math
\lim_{k \to \infty} \frac{a_k}{a_{k+1}} = 1
```

使得比值判别法失效。此时改算

```math
\lim_{k \to \infty} k \left( \frac{a_k}{a_{k+1}} - 1 \right) .
```

级数 $\sum a_k$ 收敛还是发散，取决于这个极限大于还是小于 $1$。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 3.39 (Raabe's Test, 拉贝判别法)</span>

> <span style="color:#7f8c8d;">TBB §3.6.10, p.123–124</span>

级数 $\sum_{k=1}^{\infty} a_k$ 可以用以下判据来检验。计算

```math
L = \lim_{k \to \infty} k \left( \frac{a_k}{a_{k+1}} - 1 \right) .
```

则：

1. 若 $L > 1$，级数 $\sum a_k$ 收敛。
2. 若 $L < 1$，级数 $\sum a_k$ 发散。
3. 若 $L = 1$，判别法失效。

[proof] **Proof（证明）**（虚化显示）:

> 这就是 Kummer 判别法取序列 $D_k = k$ 的情形。$\square$

> <span style="color:#1e8449;">**[note] Note（译者注）——Raabe 在"放大"什么：**</span>
> 当比值判别法失效（$a_k/a_{k+1} \to 1$）时，Raabe 判别法做的是**高阶探测**：比值与 $1$ 的偏差 $a_k/a_{k+1} - 1$ 本身太小，看不出东西，于是乘上 $k$ 把它放大到可观测的尺度——这就像在显微镜下把一级近似看不出的差异放到二级近似来看。为什么乘 $k$ 而不是别的？因为 p 级数给出了天然刻度：对 $a_k = 1/k^p$，$a_k/a_{k+1} = ((k+1)/k)^p = 1 + p/k + O(1/k^2)$，于是 $k(a_k/a_{k+1}-1) \to p$——**Raabe 极限 $L$ 直接读出"等效幂次 $p$"**：$L > 1$ 对应 $p > 1$（收敛），$L < 1$ 对应 $p < 1$（发散），$L = 1$ 恰好是调和级数的临界情形。这解释了为什么证明一行就完事（它是 Kummer 的 $D_k = k$ 特例），也解释了为什么 Example 3.40 里 $\sum k^k/(e^k k!)$ 的 Raabe 极限是 $1/2$（发散）——Stirling 公式（斯特林公式）$k! \sim \sqrt{2\pi k}\,(k/e)^k$ 会告诉你这个级数本质上像 $\sum 1/k^{1/2}$。用你熟悉的语言：Raabe 判别法是对敛散性做"更精细的渐近分类"，把 ratio test 的"收敛/发散/边界"三态细化为"按等效幂次 $p$ 排序"的连续谱。

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 3.40（例 3.40）</span>

> <span style="color:#7f8c8d;">TBB §3.6.10, p.124</span>

考虑级数

```math
\sum_{k=0}^{\infty} \frac{k^k}{e^k k!} .
```

试图对它应用比值判别法会失败，因为比值趋于 $1$——失效情形。但若我们改而计算 Raabe 判别法要求的极限

```math
\lim_{k \to \infty} k \left( \frac{k^k}{e^k k!} \cdot \frac{e^{k+1} (k+1)!}{(k+1)^{k+1}} - 1 \right) ,
```

可以用微积分方法（L'Hôpital's rule（洛必达法则））得到极限 $1/2$。因此这个级数发散。$\blacksquare$

> <span style="color:#1e8449;">**[note] Note（译者注）——Example 3.40 的"为什么是 $1/2$"：**</span>
> 教材在这里只丢下一句"用微积分方法（洛必达法则）得到极限 $1/2$"，但第一性原理的追问会让我们想看穿这个 $1/2$ 从哪来。级数的通项 $a_k = k^k/(e^k k!)$，把 Stirling 公式（斯特林公式）$k! \approx \sqrt{2\pi k}\,(k/e)^k$ 代进去：$a_k \approx k^k / (e^k \cdot \sqrt{2\pi k}\,(k/e)^k) = 1/(\sqrt{2\pi}\,\sqrt{k})$——通项像 $1/\sqrt{k}$ 一样衰退！所以这不是巧合，而是**这个级数本质上就是一个 p 级数（$p = 1/2$），必然发散**。Stirling 公式是处理阶乘型通项的万能钥匙：凡是通项含 $k!$ 的级数，先用 $k! \sim \sqrt{2\pi k}(k/e)^k$ 换成指数-多项式混合形式，敛散性立即现形。这也是为什么阶乘型级数"适合"比值/拉贝判别法——它们的比值天然是多项式比，能干净地算极限。你在学算法分析时（如推导排序/选择复杂度的上下界）也会反复用到 Stirling 公式，它是"阶乘 ↔ 指数"之间的桥梁。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">3.6.11 Gauss's Ratio Test（高斯比值判别法）</span>

> <span style="color:#7f8c8d;">Advanced section（进阶部分）。可以略读。</span>

Raabe 判别法可以用一个与它紧密相关的、归功于 Gauss（高斯）的判别法来替换。我们在使用 Raabe 判别法时可能已经发现

```math
\lim_{k \to \infty} k \left( \frac{a_k}{a_{k+1}} - 1 \right) = L .
```

这提示我们：在任何实际计算中，也许通过除法运算，我们会发现

```math
\frac{a_k}{a_{k+1}} = 1 + \frac{L}{k} + \text{涉及 } \frac{1}{k^2} \text{ 等的项} .
```

$L > 1$ 的情形对应收敛、$L < 1$ 对应发散（都由 Raabe 判别法给出）。如果 $L = 1$——在 Raabe 判别法中被视为失效的情形——怎么办？

Gauss 判别法提供了看待 Raabe 判别法的另一种方式，并且还有一个额外优势：它能处理 Raabe 判别法中遗留的失效情形。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 3.41 (Gauss's Test, 高斯判别法)</span>

> <span style="color:#7f8c8d;">TBB §3.6.11, p.124</span>

级数 $\sum_{k=1}^{\infty} a_k$ 可以用以下判据来检验。设

```math
\frac{a_k}{a_{k+1}} = 1 + \frac{L}{k} + \frac{\varphi(k)}{k^2}
```

其中 $\varphi(k)$（$k = 1, 2, 3, \ldots$）构成一个有界序列。则：

1. 若 $L > 1$，级数 $\sum a_k$ 收敛。
2. 若 $L \le 1$，级数 $\sum a_k$ 发散。

[proof] **Proof（证明）**（虚化显示）:

> 如前所述，对 $L > 1$ 与 $L < 1$，这正是 Raabe 判别法。只有 $L = 1$ 的情形是新的！设
> 
> ```math
> \frac{a_k}{a_{k+1}} = 1 + \frac{1}{k} + \frac{x_k}{k^2}
> ```
> 
> 其中 $\{x_k\}$ 是有界序列。
> 
> 为证明这一情形（级数发散），我们用 Kummer 判别法，取序列 $D_k = k \log k$。考虑表达式
> 
> ```math
> D_k \frac{a_k}{a_{k+1}} - D_{k+1} ,
> ```
> 
> 它现在具有形式
> 
> ```math
> k \log k \left( 1 + \frac{1}{k} + \frac{x_k}{k^2} \right) - (k+1) \log(k+1) .
> ```
> 
> 我们需要计算这个表达式当 $k \to \infty$ 时的极限。只需几步操作（你应该自己试一下）就能看出极限是 $-1$。这里要用到的事实是：当 $k \to \infty$ 时 $(\log k)/k \to 0$，且 $(k+1)\log(1 + 1/k) \to 1$。
> 
> 现在我们处于可以由 Kummer 判别法断言级数 $\sum a_k$ 发散的位置。应用这一部分判别法需要核实级数
> 
> ```math
> \sum_{k=2}^{\infty} \frac{1}{k \log k}
> ```
> 
> 发散。有好几个判别法都能完成这件事。也许 Cauchy condensation test（柯西凝聚判别法）是最容易应用的，虽然 integral test（积分判别法）也可以使用（见 Exercise 3.6.2(c)）。$\square$

[note] **原文注意（Note）**：在 Gauss 判别法中，你可能会困惑如何得到表达式 $a_k/a_{k+1} = 1 + L/k + \varphi(k)/k^2$。在实践中，$a_k/a_{k+1}$ 往往是多项式之比，所以通常的代数运算就能提供它。但在理论上这毫无问题：对任何 $L$，我们都可以直接写

```math
\varphi(k) = k^2 \left( \frac{a_k}{a_{k+1}} - 1 + \frac{L}{k} \right) .
```

因此真正的技巧在于：能否以某种方式做到，使得 $\varphi(k)$ 不至于增长得太大。

> <span style="color:#1e8449;">**[note] Note（译者注）——Gauss 判别法：对 $L = 1$ 的"最后一问"：**</span>
> Raabe 判别法把 p 级数 $\sum 1/k^p$ 的判据精确化到"$L$ 与 $1$ 比大小"，但 $L = 1$ 时仍然悬而未决——此时通项与调和级数同阶，收敛与否取决于**比 $1/k$ 更细的修正项**。Gauss 判别法把这层修正显式化：$a_k/a_{k+1} = 1 + 1/k + x_k/k^2$，其中 $x_k$ 的有界性告诉你 $1/k^2$ 阶的扰动不会改变结局——答案一律发散。证明的发动机是 Kummer 判别法配 $D_k = k \log k$：核心计算是验证 $k\log k \cdot a_k/a_{k+1} - (k+1)\log(k+1) \to -1$，两个微积分事实 $(\log k)/k \to 0$ 与 $(k+1)\log(1+1/k) \to 1$ 恰好把 $\log$ 项消成常数。注意发散方向需要 $\sum 1/(k \log k)$ 发散——这是凝聚判别法的又一次胜利（凝聚后变成 $\sum 1/(j \ln 2)$，显然发散），也预告了"比 $1/k$ 稍慢的发散级数"一族：$\sum 1/(k(\log k)^p)$ 在 $p \le 1$ 时发散、$p > 1$ 时收敛，与 p 级数的分界完全平行，只是把"刻度"从 $k$ 换成 $k \log k$——这正是你在对数复杂度分析里见过的"$\log$ 因子不改变幂次敛散性"直觉的精确版。

此外，在某些计算中，你可能更愿意像比值判别法那样把比值保持为 $a_{k+1}/a_k$ 的形式。此时 Gauss 判别法具有形式

```math
\frac{a_{k+1}}{a_k} = 1 - \frac{L}{k} + \frac{\varphi(k)}{k^2} .
```

（注意减号。）结论完全相同。

> <span style="color:#7f8c8d;">译者提示：此处的 $\varphi(k)$ 与上一种写法中的 $\varphi(k)$ 是**不同的**有界序列——把 $a_k/a_{k+1}$ 的展开取倒数后，$\varphi$ 项会吸收 $L^2$ 等 $1/k^2$ 阶修正。教材沿用同一符号 $\varphi$，仅表示"某个有界序列"，不必视为同一个函数。</span>

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 3.42（例 3.42）</span>

> <span style="color:#7f8c8d;">TBB §3.6.11, p.126</span>

级数

```math
1 + mx + \frac{m(m-1)}{2!} x^2 + \frac{m(m-1)(m-2)}{3!} x^3 + \cdots + \frac{m(m-1)\cdots(m-k+1)}{k!} x^k + \cdots
```

称为 binomial series（二项式级数）。当 $m$ 是正整数时，所有 $k > m$ 的项都为零，级数退化为 $(1+x)^m$ 的二项式公式。现在 $m$ 是任意实数，我们希望公式仍然成立，只是用级数代替有限和。这个级数在许多应用中扮演重要角色。我们来检验它在 $x = 1$ 处的 absolute convergence（绝对收敛）。可以假设 $m \ne 0$，因为 $m = 0$ 的情形是平凡的。

若把第 $k+1$ 项的绝对值记为 $a_k$，即

```math
a_{k+1} = \left| \frac{m(m-1)\cdots(m-k+1)}{k!} \right| ,
```

则一个简单计算表明，对大的 $k$ 有

```math
\frac{a_{k+1}}{a_k} = 1 - \frac{m+1}{k} .
```

这里我们用的是 $a_{k+1}/a_k$ 版本而不是其倒数；参见前面的注意。在 Gauss 判别法中这里没有需要担心的更高阶项，于是级数 $\sum a_k$ 在 $m+1 > 1$ 时收敛、在 $m+1 < 1$ 时发散。因此二项式级数在 $m > 0$ 时于 $x = 1$ 处绝对收敛。对 $m = 0$，级数当然收敛，因为除第一项外所有项都恒为零。对 $m < 0$，我们目前只知道它不绝对收敛。更细致的分析（有兴趣者可以一试）将表明：对 $-1 < m < 0$ 级数非绝对收敛，对 $m \le -1$ 发散。$\blacksquare$

> <span style="color:#1e8449;">**[note] Note（译者注）——binomial series：把二项式定理推广到实数指数：**</span>
> Example 3.42 是 Gauss 判别法的招牌应用，也是教材少有的"实战案例"。核心计算只有一步：相邻项绝对值之比 $a_{k+1}/a_k = 1 - (m+1)/k$——这是 $k$ 的精确等式，没有更高阶修正项，所以 Gauss 判别法一锤定音：$L = m+1$ 与 $1$ 比大小，即 $m > 0$ 绝对收敛、$m < 0$ 不绝对收敛。这个级数把 Newton 的二项式定理（$m$ 为正整数）推广到任意实数指数 $m$，它是 Taylor series（泰勒级数）的第一个重量级例子，也是后续幂级数理论的先行者。$m < 0$ 时 $-1 < m < 0$ 非绝对收敛（条件收敛）与 $m \le -1$ 发散的结论，需要 alternating series test（交错级数判别法）与更精细的估计才能得出——教材把它留给"有兴趣者"，正说明判别法各有分工：绝对收敛问题（正项级数）用 Gauss，条件收敛问题（变号级数）要换下一节的武器。$m = -1$ 时级数就是 $1/(1+x)$ 的展开 $1 - x + x^2 - x^3 + \cdots$，在 $x = 1$ 处发散——这也解释了为什么幂级数的 convergence radius（收敛半径）常常"正好断在边界上"。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">3.6.12 Alternating Series Test（交错级数判别法）</span>

现在我们转向一批研究"各项可能变号"的级数所需的判别法。研究各项有正有负的级数 $\sum_{i=1}^{\infty} a_i$，最简单的第一步是把我们那套判别法应用到级数 $\sum_{i=1}^{\infty} |a_i|$ 上：若有任何判别法表明它收敛，我们就知道原级数 absolutely convergent（绝对收敛）——这比仅仅知道它收敛更好。

但如果级数不绝对收敛、或这类尝试失败，该怎么办？有一种方法适用于特殊的正负项交错级数。回忆一下我们是如何处理级数

```math
\sum_{k=1}^{\infty} (-1)^{k-1} \frac{1}{k} = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \cdots
```

（称为 alternating harmonic series（交错调和级数））的：我们分别考察部分和 $s_2, s_4, s_6, \ldots$ 与 $s_1, s_3, s_5, \ldots$。$+$、$-$ 符号一个接一个交替出现的特殊模式，使我们能看到两个子序列 $\{s_{2n}\}$ 与 $\{s_{2n-1}\}$ 各自单调。这一论证的所有特征可以提炼成一个适用于一大类级数（与交错调和级数相似）的判别法。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 3.43 (Alternating Series Test, 交错级数判别法)</span>

> <span style="color:#7f8c8d;">TBB §3.6.12, p.127</span>

各项符号交替的级数

```math
\sum_{k=1}^{\infty} (-1)^{k-1} a_k
```

若序列 $\{a_k\}$ 单调递减到零，则收敛。此外，这种级数的和的值介于任意两个相继阶段的部分和的值之间。

[proof] **Proof（证明）**（虚化显示）:

> 证明与交错调和级数的证明完全相同。由于 $a_k$ 非负且递减，我们计算得
> 
> ```math
> a_1 - a_2 = s_2 \le s_4 \le s_6 \le \cdots \le s_5 \le s_3 \le s_1 = a_1 .
> ```
> 
> 这两个子序列于是构成有界单调序列，故 $\lim_{n\to\infty} s_{2n}$ 与 $\lim_{n\to\infty} s_{2n-1}$ 都存在。最后，由于 $s_{2n} - s_{2n-1} = -a_{2n} \to 0$，可以断定 $\lim_{n\to\infty} s_n = L$ 存在。由证明过程清楚可见，值 $L$ 落在每一个区间 $[s_2, s_1], [s_2, s_3], [s_4, s_3], [s_4, s_5], \ldots$ 中，因此如所述，级数的和介于任意两个相继阶段的部分和的值之间。$\square$

> <span style="color:#1e8449;">**[note] Note（译者注）——交错级数判别法的"证据结构"：**</span>
> 这个判别法的证明是"分拆子序列 + 单调有界定理"的经典示范：把部分和序列 $\{s_n\}$ 按奇偶拆成两支，交替符号保证偶数项部分和 $s_{2n}$ 单调递增（每次加一个正区间 $a_{2n+1}-a_{2n+2} \ge 0$），奇数项部分和 $s_{2n-1}$ 单调递减；两支各自有界（被首项 $a_1$ 夹住），于是各自收敛；最后两支的间距 $s_{2n-1} - s_{2n} = a_{2n} \to 0$ 把两支的极限挤到同一个值 $L$。**命名模板"奇偶分拆法"**：当序列本身难以直接处理时，按某种规则（奇偶、分组）拆成两个更好处理的子序列，分别证明收敛，再让"间距趋于零"完成汇合。判别法还免费赠送一个副产品：和 $L$ 夹在任意两个相邻部分和之间——这正是 alternating series 数值计算（如 $\pi/4 = 1 - 1/3 + 1/5 - \cdots$）里"截断误差不超过下一项绝对值"的证明来源，也是你之后做数值逼近时误差估计的第一原理。注意条件"$\{a_k\}$ 单调递减"不可省：$a_k = 1/k$ 换成不单调的序列，交错级数可能发散。

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">3.6.13 Dirichlet's Test（狄利克雷判别法）</span>

> <span style="color:#7f8c8d;">Advanced section（进阶部分）。可以略读。</span>

我们的下一个判别法源自 summation by parts（分部求和）公式

```math
\sum_{k=1}^{n} a_k b_k = s_1 (b_1 - b_2) + s_2 (b_2 - b_3) + \cdots + s_{n-1} (b_{n-1} - b_n) + s_n b_n
```

（我们在 §3.2 讨论过）。可以看到：若关于这里的序列 $\{s_n\}$ 与 $\{b_n\}$ 有某些特殊信息可用，就能证明级数 $\sum_{k=1}^{n} a_k b_k$ 收敛。下面的判别法给出了这种可能性之一，下一节给出一个不同的变体。

该判别法以 Lejeune Dirichlet（狄利克雷，1805–1859）命名，他最著名的工作是 Fourier series（傅里叶级数），而这个判别法在其中扮演重要角色。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 3.44 (Dirichlet Test, 狄利克雷判别法)</span>

> <span style="color:#7f8c8d;">TBB §3.6.13, p.128</span>

若 $\{b_n\}$ 是递减到零的序列，且级数 $\sum_{k=1}^{\infty} a_k$ 的部分和有界，则级数 $\sum_{k=1}^{\infty} a_k b_k$ 收敛。

[proof] **Proof（证明）**（虚化显示）:

> 记 $s_n = \sum_{k=1}^{n} a_k$。由关于级数 $\sum a_k$ 的假设，存在正数 $M$ 使得对所有 $n$ 有 $|s_n| \le M$。设 $\varepsilon > 0$，并选取足够大的 $N$ 使 $n \ge N$ 时 $b_n < \varepsilon/(2M)$。
> 
> 分部求和公式表明，对 $m > n \ge N$ 有
> 
> ```math
> \left| \sum_{k=n}^{m} a_k b_k \right| = |a_n b_n + a_{n+1} b_{n+1} + \cdots + a_m b_m|
> ```
> 
> ```math
> = |{-s_{n-1}} b_n + s_n (b_n - b_{n+1}) + \cdots + s_{m-1} (b_{m-1} - b_m) + s_m b_m|
> ```
> 
> ```math
> \le |{-s_{n-1}} b_n| + |s_n (b_n - b_{n+1})| + \cdots + |s_{m-1} (b_{m-1} - b_m)| + |s_m b_m|
> ```
> 
> ```math
> \le M (b_n + [b_n - b_m] + b_m) \le 2M b_n < \varepsilon .
> ```
> 
> 注意我们这里用到了 $b_{k-1} - b_k \ge 0$（对每个 $k$）。这正是级数 $\sum a_k b_k$ 的 Cauchy criterion（柯西准则），于是收敛性得证。$\square$

> <span style="color:#1e8449;">**[note] Note（译者注）——分部求和：把"振动"与"衰减"分开结算：**</span>
> Dirichlet 判别法的证明是 summation by parts（分部求和，离散版的 integration by parts（分部积分））的首次大型实战。直觉是这样的：$a_k$ 是"振动源"（部分和有界，好比频率有界的振荡），$b_k$ 是"衰减因子"（单调趋于零）。分部求和把乘积级数 $\sum a_k b_k$ 重新写成 $\sum s_k (b_k - b_{k+1})$ 的形式——**振动信息全部搬进有界的 $s_k$，衰减信息全部留在相邻差 $b_k - b_{k+1}$**——于是每一项的绝对值 $\le M(b_k - b_{k+1})$，对 $k$ 求和后 telescoping 相消成 $M b_n$，配合 $b_n \to 0$ 就得到柯西准则。这正是 alternating series test 的推广：取 $a_k = (-1)^{k-1}$（部分和只有 $0$ 和 $1$，有界）时，Dirichlet 判别法直接退回交错级数判别法。Example 3.45 展示了它的威力：$\sum a_k/k$ 对任何"有界部分和"的 $\pm 1$ 符号模式都收敛——振动有界 + 衰减 $1/k$，就足以收敛，根本不需要符号严格交替。这与你后续学 Fourier series（傅里叶级数）时的收敛性证明同源，也是 Abel summation（阿贝尔求和）技巧的雏形。

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 3.45（例 3.45）</span>

> <span style="color:#7f8c8d;">TBB §3.6.13, p.128</span>

级数

```math
1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5} - \frac{1}{6} + \cdots
```

由交错级数判别法收敛。我们还能插入什么样的 $+$、$-$ 符号模式而仍然收敛？设 $a_k = \pm 1$。若部分和 $\sum_{k=1}^{n} a_k$ 保持有界，则由 Dirichlet 判别法，级数 $\sum_{k=1}^{\infty} a_k/k$ 必收敛。于是，例如模式

```math
+ - + + - - + - + + - - + - + + - - \cdots
```

会产生一个收敛级数（虽然不是交错的）。$\blacksquare$

> <span style="color:#7f8c8d;">脚注 1：</span>Dirichlet 的一位同时代人这样描述他："他是一个相当高、瘦削的人，胡须开始变灰，嗓音有些沙哑，耳朵有些背。他不修边幅，端着咖啡杯、叼着雪茄。他的缺点之一是忘记时间——他掏出怀表，发现已过三点，话没说完就跑了出去。"（引自 http://www.history.mcs.st-and.ac.uk/history）

---

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">3.6.14 Abel's Test（阿贝尔判别法）</span>

> <span style="color:#7f8c8d;">Advanced section（进阶部分）。可以略读。</span>

下一个判别法是 Dirichlet 判别法同一主题的另一个变体。在 Dirichlet 判别法中，级数 $\sum a_k b_k$ 的收敛性是通过对 $\sum a_k$ 假设一个相当弱的事实（部分和有界）、对 $\{b_k\}$ 假设一个强事实（单调收敛到零）来证明的。这里我们加强前者、削弱后者。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 3.46 (Abel Test, 阿贝尔判别法)</span>

> <span style="color:#7f8c8d;">TBB §3.6.14, p.129</span>

若 $\{b_n\}$ 是收敛的单调序列，且级数 $\sum_{k=1}^{\infty} a_k$ 收敛，则级数 $\sum_{k=1}^{\infty} a_k b_k$ 收敛。

[proof] **Proof（证明）**（虚化显示）:

> 先设 $b_k$ 递减收敛到极限 $B$。则 $b_k - B$ 递减到零。对级数 $\sum_{k=1}^{\infty} a_k (b_k - B)$ 应用 Dirichlet 判别法即可得收敛性，因为 $\sum a_k$ 收敛则其部分和序列有界。
> 
> 但这让我们把原级数写成两个收敛级数之和：
> 
> ```math
> \sum_{k=1}^{\infty} a_k b_k = \sum_{k=1}^{\infty} a_k (b_k - B) + B \sum_{k=1}^{\infty} a_k .
> ```
> 
> 若 $b_k$ 改为递增收敛到某个极限，则把已证明的第一种情形应用于级数 $-\sum_{k=1}^{\infty} a_k (-b_k)$ 即可。$\square$

> <span style="color:#1e8449;">**[note] Note（译者注）——Abel vs Dirichlet：条件的天平：**</span>
> Abel 判别法与 Dirichlet 判别法构成一对互补的判别法，区别在于把筹码放在哪一边：
> 
> |                 | $\sum a_k$ 的条件 | $\{b_k\}$ 的条件 |
> | --------------- | -------------- | ------------- |
> | Dirichlet（3.44） | 部分和有界（弱）       | 单调递减到 0（强）    |
> | Abel（3.46）      | 收敛（强）          | 收敛且单调（弱）      |
> 
> Abel 判别法的证明是"减掉极限"的技巧：$b_k$ 收敛到 $B$ 不趋于零，无法直接套 Dirichlet；但 $b_k - B \to 0$ 且单调，于是 $\sum a_k (b_k - B)$ 可以用 Dirichlet，剩下的 $B \sum a_k$ 是收敛级数的常数倍——**把一个"麻烦的极限值"拆出来单独结算**。这个"提取极限项"的手法值得命名记忆（**"去心减极限法"**）：当单调因子收敛到非零极限时，减去极限再做判别，最后把极限项加回来。Abel 判别法的应用场景同样遍布 Fourier analysis（傅里叶分析）与概率论：例如概率论中证明期望存在性时常见的"$b_n \uparrow B$ 且有界"配对。它也是 Abel summation 技巧（给发散级数加衰减因子 $r^n$ 再取 $r \to 1^-$）的收敛性基础。

**习题区（Exercises 3.6.1–3.6.23 等，p129–133）：** 按约定保留英文原文，本翻译文件不收录。

---

## <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">3.7 Rearrangements（重排）</span>

> <span style="color:#7f8c8d;">Enrichment section（提高部分）。可以略读。TBB §3.7, p.133–134</span>

任何有限和都可以重排，并可以按任何顺序求和——这是因为加法是交换的（commutative）。我们或许期望级数也有同样的情况。我们求级数 $\sum_{k=1}^{\infty} a_k$ 的和，是从第一项开始、按呈现给我们的顺序逐项相加。如果把这些项重排成不同的顺序，我们还会得到相同的结果吗？

### <span style="color:#2471a3;">**[example]**</span> <span style="color:#c0392b">Example 3.47（例 3.47）</span>

> <span style="color:#7f8c8d;">TBB §3.7, p.134</span>

关于"不能随意重排而不改变和"的级数，最著名的例子是 alternating harmonic series（交错调和级数）。我们知道级数

```math
1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \cdots
```

收敛（实际上是非绝对收敛），和介于 $1/2$ 与 $1$ 之间。如果我们把它重排成"每个正项后面跟两个负项"的形式，即

```math
1 - \frac{1}{2} - \frac{1}{4} + \frac{1}{3} - \frac{1}{6} - \frac{1}{8} + \frac{1}{5} - \frac{1}{10} - \frac{1}{12} + \cdots
```

我们将得到不同的和。分组并相加，得到

```math
\left( 1 - \frac{1}{2} \right) - \frac{1}{4} + \left( \frac{1}{3} - \frac{1}{6} \right) - \frac{1}{8} + \left( \frac{1}{5} - \frac{1}{10} \right) - \frac{1}{12} + \cdots
```

```math
= \frac{1}{2} \left( 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \cdots \right)
```

其和是原级数和的一半。重排改变了级数的和！$\blacksquare$

> <span style="color:#1e8449;">**[note] Note（译者注）——为什么"重排"会改变和：**</span>
> Example 3.47 是分析学史上最著名的"反直觉"现象之一：有限项求和无论怎么调换顺序结果都相同，无限级数却会因重排而改变和。直觉的根源在于**有限和只依赖"有哪些项"，而级数和还依赖"项以什么速度被累加"**。交错调和级数正项之和与负项之和各自发散（都是调和型），原级数收敛靠的是正负项"交替抵消"的精确节奏；重排打乱了抵消节奏，等于把发散的正项块和负项块重新配比，于是和值改变。计算细节值得看懂：分组 $\left(1 - \frac{1}{2}\right) - \frac{1}{4}$ 这一步，是把两个负项与一个正项配对，每组恰好产生原级数对应项的 $\frac{1}{2}$——所以整个重排级数是原级数的 $\frac{1}{2}$ 倍。这个"凑出倍数"的手法（缩放配对）是重排技巧的入门示范。**这与你熟悉的计算机科学概念直接对应**：浮点加法顺序影响舍入结果、分布式求和顺序影响最终精度——"求和的顺序不可交换"不是数学特有的病态，而是"无穷/极端精度"下的普遍现象。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">正文衔接：从有限和到级数的重排问题</span>

> <span style="color:#7f8c8d;">TBB §3.7, p.134（教材原文）</span>

对 unordered sum（无序和）$\sum_{j\in J} a_j$ 的理论来说，不存在这样的问题：若无序和 $\sum_{j\in J} a_j$ 收敛到数 $c$，则它的任何重排也收敛到 $c$（Exercise 3.3.8 表明：若 $\sigma: I \to I$ 是一一对应（one-to-one and onto，双射），则 $\sum_{i\in I} a_j = \sum_{i\in I} a_{\sigma(i)}$）。我们曾希望级数也有同样的情形：若 $\sigma: \mathbb{N} \to \mathbb{N}$ 是一一对应，则 $\sum_{k=1}^{\infty} a_k = \sum_{k=1}^{\infty} a_{\sigma(k)}$ 成立与否都不一定。我们把 $\sum_{k=1}^{\infty} a_{\sigma(k)}$ 称为级数 $\sum_{k=1}^{\infty} a_k$ 的一个 rearrangement（重排）。

我们现在要刻画那些允许任意重排的级数，以及那些更"脆弱"（如交错调和级数那样）不能允许重排的级数。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">3.7.1 Unconditional Convergence（无条件收敛）</span>

一个级数称为 unconditionally convergent（无条件收敛），如果该级数的所有重排都收敛且具有相同的和。不允许这样但收敛的级数称为 conditionally convergent（条件收敛）。这里的"条件"意思是：级数在给定的排列下收敛，但在另一种排列下可能发散，或收敛到不同的和。我们将看到条件收敛级数极其脆弱：存在表现出任何所期望行为的重排——有发散的重排，也有收敛到任何给定数的重排。

我们的第一个定理断言：任何绝对收敛级数都可以自由重排。所有 absolutely convergent（绝对收敛）级数都是无条件收敛的。事实上，这两个概念等价：

```math
\text{unconditionally convergent（无条件收敛）} \iff \text{absolutely convergent（绝对收敛）}
```

虽然我们必须等到下一节才能证明这一点。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 3.48 (Dirichlet, 狄利克雷)</span>

> <span style="color:#7f8c8d;">TBB §3.7.1, p.135</span>

每个绝对收敛级数都是无条件收敛的。

[proof] **Proof（证明）**（虚化显示）:

> 先对各项全为非负的级数 $\sum_{k=1}^{\infty} a_k$ 证明。对这种级数，收敛与绝对收敛是一回事。
> 
> 设 $\sum_{k=1}^{\infty} a_{\sigma(k)}$ 是任意重排。则对任何 $M$，
> 
> ```math
> \sum_{k=1}^{M} a_{\sigma(k)} \le \sum_{k=1}^{N} a_k \le \sum_{k=1}^{\infty} a_k
> ```
> 
> 只需选取足够大的 $N$，使 $\{1, 2, 3, \ldots, N\}$ 包含所有整数 $\{\sigma(1), \sigma(2), \sigma(3), \ldots, \sigma(M)\}$。
> 
> 由部分和有界判据，这表明 $\sum a_{\sigma(k)}$ 收敛且和小于 $\sum a_k$。但同样的论证也会表明 $\sum a_k$ 收敛且和小于 $\sum a_{\sigma(k)}$，因此所有重排收敛到同一个和。
> 
> 现在允许级数 $\sum a_k$ 有正有负。写出
> 
> ```math
> \sum_{k=1}^{\infty} a_k = \sum_{k=1}^{\infty} [a_k]^{+} - \sum_{k=1}^{\infty} [a_k]^{-}
> ```
> 
> （参见 Exercise 3.5.8），其中使用记号 $[X]^{+} = \max\{X, 0\}$ 与 $[X]^{-} = \max\{-X, 0\}$，并记住 $X = [X]^{+} - [X]^{-}$ 且 $|X| = [X]^{+} + [X]^{-}$。
> 
> 等式左边级数的任何重排，只不过导致右边两个非负项级数的重排。我们刚刚看到，这不会改变收敛性或和。因此，我们级数的任何重排都有相同的和——这正是定理要证明的断言。$\square$

> <span style="color:#1e8449;">**[note] Note（译者注）——定理 3.48 证明的"两步走"结构：**</span>
> 定理 3.48 的证明是两个阶段的典范：**先证非负项（正项级数）情形，再通过正部/负部分解把一般情形化归到它**。第一阶段的关键操作是"前缀包含"：对重排级数的任何有限前缀 $\{\sigma(1), \ldots, \sigma(M)\}$，总能找到原级数足够长的前缀把它整个覆盖——于是重排级数的部分和被原级数的总和 $\sum a_k$（有限数）夹住，部分和有界即收敛。第二阶段把 $a_k$ 拆成 positive part（正部）$[a_k]^+$ 与 negative part（负部）$[a_k]^-$，并利用绝对收敛保证 $\sum [a_k]^+$ 与 $\sum [a_k]^-$ 都收敛（因为 $[a_k]^+ \le |a_k|$）；重排只分别重排这两个非负级数，而第一阶段已证明非负级数重排不改变和。**命名模板"正负部化归法"**：把任意符号的级数问题拆成正部与负部两个非负问题分别处理，最后用 $X = [X]^+ - [X]^-$ 拼回——这个技巧在本节还会反复出现（定理 3.49、3.50），它也是后面 Lebesgue 积分理论里 $f = f^+ - f^-$ 分解的原型。注意第二阶段的关键前提是 $\sum |a_k| < \infty$（即绝对收敛），否则两个非负级数都发散，减法毫无意义。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">3.7.2 Conditional Convergence（条件收敛）</span>

收敛但非无条件收敛的级数称为 conditionally convergent（条件收敛）。这样的级数在给定排列下收敛，但要么存在某个发散的重排，要么存在某个具有不同和的重排。事实上，两种情形总是同时出现。

我们已经看到（Example 3.47）交错调和级数如何被重排成不同的和。下面要证明：任何非绝对收敛级数都有这个性质。之前我们的重排利用了级数的特殊结构；这里的证明必须完全一般化，所以方法不同。

下面的定理补全定理 3.48，并提供联系：

```math
\text{conditionally convergent（条件收敛）} \iff \text{nonabsolutely convergent（非绝对收敛）}
```

```math
\text{unconditionally convergent（无条件收敛）} \iff \text{absolutely convergent（绝对收敛）}
```

[note] **原文注意（Note）**：你可能会问：既然这些概念相同，为什么我们还需要这套额外术语？原因之一是强调这是理论的一部分——条件收敛与非绝对收敛也许等价，但它们有不同层面的含义。此外，这套术语也用于实数以外的其他对象的级数，而对这种更一般的级数，这些概念并不等价。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 3.49 (Riemann, 黎曼)</span>

> <span style="color:#7f8c8d;">TBB §3.7.2, p.136</span>

每个非绝对收敛级数都是条件收敛的。事实上，每个非绝对收敛级数都有一个发散的重排，也可以重排成收敛到任何预先给定的值。

[proof] **Proof（证明）**（虚化显示）:

> 设 $\sum_{k=1}^{\infty} a_k$ 是任意非绝对收敛级数。为证明第一个断言，只需观察到：为了让 $\sum a_k$ 非绝对收敛，级数 $\sum_{k=1}^{\infty} [a_k]^{+}$ 与 $\sum_{k=1}^{\infty} [a_k]^{-}$ 都必须发散。我们还需要观察到 $a_k \to 0$，因为级数被假定为收敛的。
> 
> 把序列 $\{a_k\}$ 中的正数（跳过任何零或负数）记为 $p_1, p_2, p_3, \ldots$，把跳过的项记为 $q_1, q_2, q_3, \ldots$。我们构造一个新级数
> 
> ```math
> p_1 + p_2 + \cdots + p_{n_1} + q_1 + p_{n_1+1} + p_{n_1+2} + \cdots + p_{n_2} + q_2 + p_{n_2+1} + \cdots
> ```
> 
> 其中选取 $0 = n_0 < n_1 < n_2 < n_3 < \ldots$ 使得对每个 $k = 0, 1, 2, \ldots$ 有
> 
> ```math
> p_{n_k+1} + p_{n_k+2} + \cdots + p_{n_{k+1}} > 2^k .
> ```
> 
> 由于 $\sum p_k$ 发散，这是可行的。这样构造的新级数包含原级数的所有项，因而是重排。由于 $q_k \to 0$，它们不会干扰新级数产生越来越大部分和的进程，于是显然新级数发散到 $\infty$。
> 
> 定理的第二部分要求构造一个收敛的重排，收敛到给定数 $\alpha$。我们用大致相同但更加谨慎的方式处理。这部分留给习题。$\square$

> <span style="color:#1e8449;">**[note] Note（译者注）——Riemann 重排定理的"构造哲学"：**</span>
> 定理 3.49 被称为 Riemann rearrangement theorem（黎曼重排定理），其结论远比"存在重排改变和"更极端：**非绝对收敛级数可以被重排成发散，或被重排成收敛到任何你想要的值**。证明的第一阶段（发散重排）展示了核心机制：正部级数 $\sum p_k$ 发散，所以可以切成长度递增的块，每块正项之和 $> 2^k$——即使每块后面塞进一个负项 $q_k$（它趋于零），总和的增长仍是爆炸性的。这里有两个要素缺一不可：**正部之和发散**（提供燃料）与 **$a_k \to 0$**（保证负项是"小插曲"）。第二阶段（收敛到任意 $\alpha$）的构造逻辑其实你已经能猜到：贪心地交替加正项直到超过 $\alpha$，再交替加负项直到低于 $\alpha$，如此往复——因为正部与负部都发散，每次"纠偏"都有足够的弹药，而 $a_k \to 0$ 保证振荡幅度不断收窄，最终锁定在 $\alpha$。这与你做"二分法逼近目标值"的算法思维完全同构：**有无限供应的大步长 + 步长不断缩小 = 可逼近任意目标**。这个定理也解释了上一节 Note 里"为什么需要额外术语"——conditionally convergent 强调"在给定排列下收敛"这一语义，而不只是"非绝对"这个量化事实。

### <span style="color:#2471a3;">**[section]**</span> <span style="color:#c0392b">3.7.3 Comparison of $\sum_{i=1}^{\infty} a_i$ and $\sum_{i\in\mathbb{N}} a_i$（有序和与无序和的比较）</span>

> <span style="color:#7f8c8d;">Advanced section（进阶部分）。可以略读。</span>

一个实数序列的 unordered sum（无序和），写作 $\sum_{i\in\mathbb{N}} a_i$，与有序和 $\sum_{i=1}^{\infty} a_i$ 有明显的联系。当两者都收敛时我们理应期望它们相等，但有没有可能一个收敛而另一个不收敛呢？

答案是：$\sum_{i\in\mathbb{N}} a_i$ 的收敛与 $\sum_{i=1}^{\infty} a_i$ 的绝对收敛等价。

### <span style="color:#2471a3;">**[theorem]**</span> <span style="color:#c0392b">Theorem 3.50（定理 3.50）</span>

> <span style="color:#7f8c8d;">TBB §3.7.3, p.137</span>

$\sum_{i\in\mathbb{N}} a_i$ 收敛的充要条件是级数 $\sum_{i=1}^{\infty} a_i$ 绝对收敛，且此时

```math
\sum_{i\in\mathbb{N}} a_i = \sum_{i=1}^{\infty} a_i .
```

[proof] **Proof（证明）**（虚化显示）:

> 我们将使用一个此前见过几次的技巧：对任何实数 $X$，写 $[X]^{+} = \max\{X, 0\}$ 与 $[X]^{-} = \max\{-X, 0\}$，并注意 $X = [X]^{+} - [X]^{-}$ 且 $|X| = [X]^{+} + [X]^{-}$。
> 
> 级数的绝对收敛与定理陈述中求和的收敛性，现在归结为比较下列等式两边的右端：
> 
> ```math
> \sum_{i\in\mathbb{N}} a_i = \sum_{i\in\mathbb{N}} [a_i]^{+} - \sum_{i\in\mathbb{N}} [a_i]^{-}
> ```
> 
> 与
> 
> ```math
> \sum_{i=1}^{\infty} a_i = \sum_{i=1}^{\infty} [a_i]^{+} - \sum_{i=1}^{\infty} [a_i]^{-} .
> ```
> 
> 这把我们的问题化归为只考虑非负级数（和）。
> 
> 于是可以假设每个 $a_i \ge 0$。对任何有限集 $I \subset \mathbb{N}$，显然有 $\sum_{i\in I} a_i \le \sum_{i=1}^{\infty} a_i$。由此可知：若 $\sum_{i=1}^{\infty} a_i$ 收敛，则（由 Exercise 3.3.3）$\sum_{i\in\mathbb{N}} a_i$ 也收敛，且
> 
> ```math
> \sum_{i\in\mathbb{N}} a_i \le \sum_{i=1}^{\infty} a_i .
\tag{6}
> ```
> 
> 类似地，若 $N$ 有限，则
> 
> ```math
> \sum_{i=1}^{N} a_i \le \sum_{i\in\mathbb{N}} a_i .
\tag{7}
> ```
> 
> 由此可知：若 $\sum_{i\in\mathbb{N}} a_i$ 收敛，则由有界性判据 $\sum_{i=1}^{\infty} a_i$ 也收敛，且 $\sum_{i=1}^{\infty} a_i \le \sum_{i\in\mathbb{N}} a_i$。
> 
> 这两个断言连同不等式 (6) 与 (7)，对非负级数（和）的情形证明了定理。$\square$

> <span style="color:#1e8449;">**[note] Note（译者注）——有序 vs 无序：同一个和的两种"访问协议"：**</span>
> 定理 3.50 把"无序和"与"绝对收敛"钉死在一起：无序和 $\sum_{i\in\mathbb{N}} a_i$（对所有有限子集上的和取上确界）收敛，当且仅当有序级数绝对收敛。用计算机科学的语言说，这两者是**同一个"可数和"的两种访问协议**：无序和把"求和"定义为"所有有限块之和的上确界"（不依赖顺序），有序和按 $1, 2, 3, \ldots$ 的顺序逐项累加；只有当累加的顺序不造成影响（即绝对收敛）时，两种协议才给出同一个值。证明再次使用正负部化归：先只看非负项，那么"每个有限子集和都被总和夹住"给出 (6)，"每个前缀都是有限子集"给出 (7)，双向夹逼后相等。注意 (7) 的方向：$\sum_{i\in\mathbb{N}} a_i$ 是**所有**有限子集和的上确界，而前缀只是其中特殊的有限子集，所以前缀和 $\le$ 无序和。这一点在下一节（§3.8 Cauchy product 与二重级数）会升级成更复杂的形式——两个级数相乘时"如何求和"的问题正是无序和理论的用武之地。此刻值得记住的结论链：**可重排不改变和 ⟺ 绝对收敛 ⟺ 无序和收敛 ⟺ 正负部各自收敛**——四个视角，同一个对象。

**习题区（Exercises 3.7.1–3.7.11 等，p138–140）：** 按约定保留英文原文，本翻译文件不收录。

---
