<span style="color:#7f8c8d">书页 335 · §8.2 Cauchy 第一方法（定理 8.1 证明收尾 · 推论 8.3 · §8.2.1）</span>

与此同时还有 $m(\pi_n) \le m(\pi_{n+1})$。（这些细节只须一些不等式运算，留作习题 8.2.17。）

若在此过程中的某一步已有 $m(\pi_n)=M(\pi_n)$，则我们已完成并可选取这个数作为 $I$。否则，诸区间 $[m(\pi_n), M(\pi_n)]$ 构成一个长度收缩到零的嵌套下降序列（descending sequence）区间。由 Cantor 交叠性质（Cantor's intersection property，见第 4.5.2 节），存在数 $I$，使得当 $n\to\infty$ 时 $m(\pi_n)\to I$ 且 $M(\pi_n)\to I$。我们将证明 $I$ 具有定理所要求的性质。

现在设 $\varepsilon>0$，并任取一个满足"每个子区间（subinterval）长度均小于 $\delta(\varepsilon/2)$"性质的分划（partition）$\pi$。由前述结果，区间 $[m(\pi), M(\pi)]$ 的长度小于 $\varepsilon/2$。

任何关于该分划 $\pi$ 的 Riemann 和（Riemann sum）显然必属于区间 $[m(\pi), M(\pi)]$。

取 $N>2/\varepsilon$。暂时假设区间 $[m(\pi), M(\pi)]$ 与 $[m(\pi_N), M(\pi_N)]$ 在某点相交。在此情形下，关于分划 $\pi$ 的 Riemann 和与 $I$（后者位于区间 $[m(\pi_N), M(\pi_N)]$ 之内）彼此之间的距离必小于 $\varepsilon/2+1/N$，而这一数值小于 $\varepsilon$。由于这正是我们所要证明的结论，故证明完毕。

剩下来要检查这两个区间 $[m(\pi), M(\pi)]$ 与 $[m(\pi_N), M(\pi_N)]$ 确实相交于某点。为求得这两个区间的某一公共点，把分划 $\pi$ 与 $\pi_N$ 合并，构成一个包含二者中所有点的分划。关于这样一个分划的 Riemann 和既属于区间 $[m(\pi), M(\pi)]$，也属于区间 $[m(\pi_N), M(\pi_N)]$。这便完成了证明。（$I$ 的唯一性留作习题 8.2.2。）

$\blacksquare$

这一定义与定理的一个特殊情形，使我们能把一个积分作为某一序列的极限来计算。在实践中这很少是计算积分的最佳途径，但它在理论的某些部分既有趣又有用。

#### <span style="color:#2471a3">**[corollary]**</span> <span style="color:#c0392b">推论 8.3（Corollary 8.3）</span>
> <span style="color:#7f8c8d;">TBB §8.2, p.335</span>

设 $f$ 是区间 $[a,b]$ 上的连续函数（continuous function）。则
```math
\int_a^b f(x)\,dx=\lim_{n\to\infty}\frac{b-a}{n}\sum_{k=0}^{n-1}
f\!\left(a+\frac{k}{n}(b-a)\right).
```

#### 8.2.1 Cauchy 第一方法的论域（Scope）

（提高性小节，可略去。）

人们很自然会问，Cauchy 描述连续函数积分的这种方法，是否适用于更大的一类函数。但 Cauchy 并没有提出这个问题。他的目标是要为连续函数这一类对大多数应用已足够大的函数赋予意义。他可能看到的唯一局限，是此方法会对带有无穷奇点（infinite singularities，即函数无界的不连续点）的函数失效。于是他被迫走向我们将在第 8.4 节作为 Cauchy 第二方法（Cauchy's second method）来讨论的方法。

<span style="color:#7f8c8d">书页 336 · 第 8 章 积分（§8.2.1 论域讨论 · 习题）</span>

Cauchy 与他同时代的许多数学家，对"函数（function）"一词的含义相当困惑，以至于他们也许根本就不会提出这样的问题。

但我们能够提出这样的问题。许多年后 Riemann 也提出了，正如我们在第 8.6 节将要看到的。

习题中要求你证明以下两条结论：

- 第一方法若应用于区间 $[a,b]$ 上的无界（unbounded）函数 $f$，将会失效。
- 第一方法若应用于任何在区间 $[a,b]$ 上有界（bounded）、且在该区间上仅含有限多个不连续点（discontinuity）的函数 $f$，则会成功。

第一条结论表明，此处用来定义积分的方法受到严重限制。它永远不能用于无界函数。由于我们这里已把讨论限定在连续函数上，这不成问题；任何在区间 $[a,b]$ 上连续的函数都在该区间上有界。

第二条结论则表明，尽管 Cauchy 的初衷如此，此方法却并不只局限于连续函数。稍后我们将用此方法定义 Riemann 积分（Riemann's integral），它适用于一大类（有界）函数，这类函数被允许有大量、甚至无限多个不连续点。

#### 习题（Exercises）

**8.2.2** 英文原题：Show that the number $I$ in the statement of Theorem 8.1 is unique; that is, that there cannot be two numbers that would be assigned to the symbol $\int_a^b f(x)\,dx$.

最小翻译：证明定理 8.1 中的数 $I$ 是唯一的；即不存在两个数能被赋予符号 $\int_a^b f(x)\,dx$。（该习题在定理 8.1 的证明中被引用。）<span style="color:#7f8c8d">书页 337 · §8.2 Cauchy’s First Method</span>

<span style="color:#7f8c8d">本页为 §8.2 的习题 8.2.7–8.2.16，均属非必要习题，按翻译规则跳过，不翻译、不收录。</span>

---

<span style="color:#7f8c8d">书页 338 · §8.3 Properties of the Integral 开头</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）：**</span> 这里引入的"上合 M(f,π)"与"下合 m(f,π)"，本质是把"曲线下的面积"用矩形从上下两侧逼近、从而"夹逼"出来。第一性原理：面积无法被"看见"，只能被"逼近"；最诚实的做法是同时从上方（每段取 sup 的最高矩形）和下方（每段取 inf 的最低矩形）逼向它，若上下两个逼近最终落到同一个数，就把它定义为积分——这就是夹逼（sandwiching）的证明策略。这与你在 CLRS 学的分治 divide and conquer 完全同构：把区间切分成小段、每段单独用矩形近似、再求和合并，把连续问题离散化。历史注：矩形逼近求面积的"穷竭法"可上溯到公元前阿基米德求抛物线弓形面积，但把它严格化为"对任意有界函数都能定义上/下和、再比较上下极限"的现代形式，要等到 1854 年 Riemann 的教授资格论文；1875 年 Darboux 才正式把上和/下和（"Darboux 和"）整理为判断可积性的标准工具，这正是本节为何先讲上合/下合的原因。

---


<span style="color:#00838f">**定义 [definition]**（习题 8.2.17）上合与下合 upper and lower sums</span>

> <span style="color:#7f8c8d;">TBB §8.2.17，p.338</span>

对任何有界函数 bounded function $f$ 与区间 $[a,b]$ 的任一分划 partition $\pi$：

> 该分划将区间记为子区间 $[x_0,x_1], [x_1,x_2], \dots, [x_{n-1},x_n]$。

定义
```math
M(f,\pi)=\sum_{k=1}^{n} \sup\{f(x): x\in[x_{k-1},x_k]\}(x_k-x_{k-1})
```
以及
```math
m(f,\pi)=\sum_{k=1}^{n} \inf\{f(x): x\in[x_{k-1},x_k]\}(x_k-x_{k-1})
```

这两个量分别称为函数 $f$ 关于该分划的上合 upper sum 与下合 lower sum。

其中 $M(f,\pi)$ 是上合、$m(f,\pi)$ 是下合。

它们曾用于定理 8.1 的证明之中。

---

# §8.3 Properties of the Integral（积分的基本性质）

至此，积分 integral 仅仅为连续函数 continuous functions 所定义。

我们要询问它必须具备哪些性质 properties。

稍后我们将不得不把积分的适用范围 extension 扩展到远比此广阔得多的函数类 classes of functions。

那时对我们重要的是：此处汇集起来的基本性质 collection 依然成立。

这些性质展示了积分的结构 structure。

它们是处理积分——无论理论问题还是实际问题——时最根本的、应反复使用的工具 tools。

由于本节局限于连续函数，证明都很简单。

当我们扩大积分的适用范围时，证明可能会变得更加困难，而且断言中也可能出现细微的差异 subtle differences。

注 Note. 各条断言中出现的一切函数 $f$ 与 $g$ 均被假定在断言中所涉及的区间 $[a,b]$、$[b,c]$、$[a,c]$ 上连续。

因此各个积分都有意义。

这意味我们无需证明这些积分中任何一个的存在性：它们确实存在。

每一种情形需要证明的正是所陈述的恒等式 identity 本身。

为证明该恒等式，我们考虑一列分划 $\pi_n$，并将其分点选择得彼此更加靠近……<span style="color:#7f8c8d">书页 339 · §8.3 Properties of the Integral（积分性质）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）：**</span> 注意性质 8.4、8.5 的证明结构惊人地一致：先在各自的分划 π′n 与 π″n 上写出 Riemann 和，利用有限和的代数恒等式（S(π,f)=S(π′,f)+S(π″,f) 等）成立的"显然事实"，再取极限把恒等式传递到积分。关键中间件是分划的 refinement（加细）：把两个分划的分点取并集，就得到同时加细二者的"共同分划"——这正是和你在 CLRS 中学过的归并（merge）把两列有序元素合成一列同构的操作，也像二分搜索逐步缩小区间。第一性原理：加细 = 提高采样分辨率，网格越细，上下和之间的缝隙只会收窄而不会张大。Colding 在课堂上把这个性质当作核心引理强调：

🎥 *Colding 教授*："And so this is like a key fact. It's an obvious fact, but it's a key fact."（翻译：而且这是一个关键事实。它是个显然的事实，但却是个关键的事实。）

> 它保证：若 P1 是 P 的加细，则 m 单调不减、M 单调不增——正因为"上和不增、下和不减"，才可能用两列单调有界序列的夹逼去逼近同一个积分值。这条"上合下合靠加细互相收拢"的引理，在后面定理 8.15/8.16/8.17 里会被一遍遍复用。

---

---

> <span style="color:#1e8449;">**[note] Note（译者注）：**</span> 性质 8.4（可加）与 8.5（线性）合起来说明：积分是一个把"函数"映射到"实数"的映射，且这个映射保持加法和数乘。这正是你在 Strang 线性代数和 18.065 里反复遇到的同构对象——线性算子 T 满足 T(αu+βv)=αTu+βTv；这里把 u,v 换成 f,g、把 T 换成 ∫ab，形状一模一样。第一性原理（为什么必须这样定义）：只要"积分 = 有限 Riemann 和的极限"，那么任何对有限求和成立的线性/可加恒等式，都会在取极限后原样保留——因为极限运算不破坏有限和既有的代数结构，只把它"无穷化"。这也是为什么先对连续函数证明、再推广到更大函数类时，这些性质"依然成立"如此重要：它们是积分理论打的桩，丢了它们理论就塌了。这里的证明策略可命名为"先有限和、后取极限（finite-sum then pass to limit）"，是一种用代数恒等式 + 连续性作桥的套路。

---


> 引接上页 §8.3 引言（该性子章继续）：我们考虑一列分划（partition）$\pi_n$，使分划中的点彼此间距小于 $1/n$（closer together than $1/n$）。我们用记号 $S(\pi_n, f)$ 表示对于函数 $f$ 在该分划上、关联点（associated points）选取在（比如说）相应各小区间左端点处所得的 Riemann 和（Riemann sum）。于是
```math
\lim_{n\to\infty} S(\pi_n, f) = \int_a^b f(x)\,dx.
```
我们将运用这一想法于下面的证明中。

**8.4 可加性（Additive Property）**　<span style="color:#2471a3">[property]</span>

> <span style="color:#7f8c8d;">TBB §8.3, p.339</span>

设 $f$ 在 $[a,c]$ 上连续，并设 $a<b<c$。则
```math
\int_a^b f(x)\,dx + \int_b^c f(x)\,dx = \int_a^c f(x)\,dx.
```

<span style="color:#2471a3">**证明。**</span> 对我们的分划序列，我们选取 $\pi_n$ 为 $[a,c]$ 的一个分划，使分划中的点彼此间距小于 $1/n$，并且使点 $b$ 成为其中的一个分点。每个分划 $\pi_n$ 被拆成两部分 $\pi'_n$ 与 $\pi''_n$，其中前者是 $[a,b]$ 的一个分划，后者是 $[b,c]$ 的一个分划。注意，由初等算术（elementary arithmetic）可知
```math
S(\pi_n, f) = S(\pi'_n, f) + S(\pi''_n, f).
```
若在该恒等式（identity）中令 $n\to\infty$，我们便立即得到所要证明的结论中的恒等式。$\blacksquare$

**8.5 线性性（Linear Property）**　<span style="color:#2471a3">[property]</span>

> <span style="color:#7f8c8d;">TBB §8.3, p.339</span>

设 $f$ 与 $g$ 在 $[a,b]$ 上连续。则对所有 $\alpha, \beta \in \mathbb{R}$，
```math
\int_a^b [\alpha f(x) + \beta g(x)]\,dx = \alpha\int_a^b f(x)\,dx + \beta\int_a^b g(x)\,dx.
```

<span style="color:#2471a3">**证明。**</span> 再次考虑 $[a,b]$ 的一列分划 $\pi_n$，使其满足分划中的点彼此间距小于 $1/n$。若 $S(\pi_n, f)$ 表示在函数 $f$ 的这一分划上所取的 Riemann 和，则
```math
\lim_{n\to\infty} S(\pi_n, f) = \int_a^b f(x)\,dx.
```
以同样方式，对 $g$ 我们也有
```math
\lim_{n\to\infty} S(\pi_n, g) = \int_a^b g(x)\,dx.
```
但容易验证
```math
S(\pi_n, \alpha f + \beta g) = \alpha S(\pi_n, f) + \beta S(\pi_n, g)，
```
在这一恒等式中令 $n\to\infty$ 便恰好得到该性质中的结论。注意我们并不需要去证明
```math
S(\pi_n, \alpha f + \beta g) \to \int_a^b [\alpha f(x) + \beta g(x)]\,dx。
```
这可由定理 8.1（Theorem 8.1）推出，因为被积函数（integrand）是连续的。$\blacksquare$

<span style="color:#7f8c8d">书页 340 · §8.3 Properties of the Integral（积分性质）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）：**</span> 这条定理（以及下一页的性质 8.9）合起来正是"微积分基本定理"：F(x)=∫ax f(t)dt 的导数是 f，而 ∫ F′ 又回到 F 的端点差——求积与求导互为逆运算，就像 CSAPP 里"编码/解码"互为逆操作。第一性原理：微积分之所以"基本"，是因为它为无穷多分点求和（积分）找到了一个"查表捷径"——只要找到反导数 F，就把算极限化成了两次求值 F(b)−F(a)，复杂度从 O(分点数) 降到 O(1)，这和你学过的"预计算/缓存"降低复杂度的直觉一致。证明的核心是"夹逼"（squeezing）：把差商 (F(x+h)−F(x))/h 夹在区间 [x,x+h] 上 f 的 inf 与 sup 之间，利用 f 的连续性让两侧都逼向 f(x)。而性质 8.9 的证明借用了你在基础实分析就熟的中值定理（MVT）在每个小区间 [x_{k−1},x_k] 内挑点 ξk，使得 F(xk)−F(x_{k−1})=F′(ξk)Δx——这一"调差挑点"手法（telescoping + MVT）是把离散和精确接回连续导数的高招。

---


**8.6 单调性（Monotone Property）**　<span style="color:#2471a3">[property]</span>

> <span style="color:#7f8c8d;">TBB §8.3, p.340</span>

设 $f$ 与 $g$ 在 $[a,b]$ 上连续。则若对所有 $a\le x\le b$ 有 $f(x)\le g(x)$，
```math
\int_a^b f(x)\,dx \le \int_a^b g(x)\,dx.
```

<span style="color:#2471a3">**证明。**</span> 考虑一列分划 $\pi_n$，使其满足分划中的点彼此间距小于 $1/n$。若 $S(\pi_n, f)$ 表示在函数 $f$ 的这一分划上所取的 Riemann 和，则
```math
\lim_{n\to\infty} S(\pi_n, f) = \int_a^b f(x)\,dx.
```
以同样方式，对 $g$ 我们有
```math
\lim_{n\to\infty} S(\pi_n, g) = \int_a^b g(x)\,dx.
```
但由于对所有 $x$ 有 $f(x)\le g(x)$，我们必定有 $S(\pi_n, f)\le S(\pi_n, g)$。在该不等式中令 $n\to\infty$ 取极限便得到该性质。$\blacksquare$

**8.7 绝对值性质（Absolute Property）**　<span style="color:#2471a3">[property]</span>

> <span style="color:#7f8c8d;">TBB §8.3, p.340</span>

设 $f$ 在 $[a,b]$ 上连续。则
```math
-\int_a^b |f(x)|\,dx \le \int_a^b f(x)\,dx \le \int_a^b |f(x)|\,dx，
```
或等价地，
```math
\left|\int_a^b f(x)\,dx\right| \le \int_a^b |f(x)|\,dx.
```

<span style="color:#2471a3">**证明。**</span> 这由单调性（monotone property）立即推出，因为 $-|f(x)|\le f(x)\le |f(x)|$。$\blacksquare$

下面两条性质合在一起被称为微积分基本定理（the fundamental theorem of calculus）。它们建立起微分与积分之间的密切联系，并且为微积分学习者提供了一种计算积分的有用方法。该方法把积分这一计算问题（即计算 Riemann 和的极限）化归为求一个反导数（antiderivative）的问题。

**8.8 不定积分的微分（Differentiation of the Indefinite Integral）**　<span style="color:#2471a3">[theorem]</span>

> <span style="color:#7f8c8d;">TBB §8.3, p.340</span>

设 $f$ 在 $[a,b]$ 上连续。则函数
```math
F(x) = \int_a^x f(t)\,dt
```
在 $[a,b]$ 上有导数，并且在每一点处有 $F'(x)=f(x)$。

<span style="color:#2471a3">**证明。**</span> 设 $h>0$ 且 $x\in[a,b)$。我们计算
```math
F(x+h) - F(x) - h f(x) = \int_x^{x+h} (f(t) - f(x))\,dt
```
（证明于下一页继续）<span style="color:#7f8c8d">书页 341 · §8.3 Properties of the Integral（积分性质）</span>

（接上页——位于 §8.3 之前的性质 8.8 之证明末段；书中省略了该性质重述。）此处只需保证 $x+h \le b$ 即可。于是，利用习题 8.3.1，我们得到
```math
|F(x+h)-F(x)-hf(x)| \le h\max\bigl\{|f(t)-f(x)|:\ t\in[x,x+h]\bigr\},
```
并由此得到
```math
\left|\frac{F(x+h)-F(x)}{h}-f(x)\right| \;\!\le\;\! \max\bigl\{|f(t)-f(x)|:\ t\in[x,x+h]\bigr\}.
```
由于 $f$ 在 $x$ 处连续，当 $h\to 0^+$ 时
```math
\max\bigl\{|f(t)-f(x)|:\ t\in[x,x+h]\bigr\}\to 0,
```
且上述不等式表明 $F$ 在 $x\in[a,b)$ 处的右导数（right-hand derivative）恰等于 $f(x)$。

相似的论证可表明 $F$ 在 $x\in(a,b]$ 处的左导数（left-hand derivative）也恰等于 $f(x)$。这就证明了该性质。$\blacksquare$

**性质 8.9 · [property] 导数的积分，微积分基本定理第二条（Integral of a Derivative）**

> <span style="color:#7f8c8d;">TBB §8.3, p.341</span>

> <span style="color:#7f8c8d;">若函数 $F$ 在 $[a,b]$ 上具有连续导数（continuous derivative），则</span>

```math
\int_a^b F'(x)\,dx = F(b)-F(a).
```

**证明 [proof]：** 任给 $\varepsilon>0$，存在 $\delta>0$，使得对连续函数 $F'$ 而言，关于 $[a,b]$ 的、将各区间的长度取为小于 $\delta$ 的任意一个分划，其对应的任一 Riemann 和（Riemann sum）与 $\int_a^b F'(x)\,dx$ 的偏差都在 $\varepsilon$ 以内。若
```math
[x_0,x_1],\;[x_1,x_2],\;\ldots,\;[x_{n-1},x_n]
```
是这样一个分划，则注意到：如果我们借助中值定理（mean value theorem）选取相应的点 $\xi_k\in[x_{k-1},x_k]$，使得
```math
F(x_k)-F(x_{k-1})=F'(\xi_k)(x_k-x_{k-1}),
```
那么我们就有
```math
F(b)-F(a)=\sum_{k=1}^n\bigl[F(x_k)-F(x_{k-1})\bigr]=\sum_{k=1}^n F'(\xi_k)(x_k-x_{k-1}).
```
由于该恒等式的右端与 $\int_a^b F'(x)\,dx$ 的偏差在 $\varepsilon$ 以内，故值 $F(b)-F(a)$ 也必然如此。但这对任意 $\varepsilon>0$ 都成立，因此可知二者必须相等；也就是说，
```math
\int_a^b F'(x)\,dx=F(b)-F(a).
```
$\blacksquare$

<span style="color:#7f8c8d">习题</span>

8.3.1 若 $f$ 在区间 $[a,b]$ 上连续，且 $M=\max\{|f(x)|:\ x\in[a,b]\}$，证明
```math
\left|\int_a^b f(x)\,dx\right| \le M(b-a).
```
（根据任务规则，习题非必要可跳过，此处仅为完整性列出。）

<span style="color:#7f8c8d">书页 342 · §8.3 Properties of the Integral（积分性质）</span>

> <span style="color:#7f8c8d;">本页主体为 §8.3 的习题区（8.3.2–8.3.10），非必要条件，予以跳过，不逐条翻译。</span>

<span style="color:#7f8c8d">本页习题概览（依规则跳过，仅供索引）：</span>

- 8.3.2 积分的均值定理（Mean Value Theorem for Integrals）：若 $f$ 连续，则存在点 $\xi\in(a,b)$ 使得 $\int_a^b f(x)\,dx=f(\xi)(b-a)$。
- 8.3.3 若 $f$ 连续且对所有 $x\in[a,b]$ 有 $m\le f(x)\le M$，且 $g$ 为连续非负函数，证明 $m\int_a^b g(x)\,dx\le\int_a^b f(x)g(x)\,dx\le M\int_a^b g(x)\,dx$。
- 8.3.4 若 $f$ 在 $[a,b]$ 上连续且非负，且 $\int_a^b f(x)\,dx=0$，证明 $f$ 在该区间上恒为零。
- 8.3.5 积分的第二均值定理（Second Mean Value Theorem for Integrals）。
- 8.3.6 若 $f$ 连续且对 $[a,b]$ 上每个连续函数 $g$ 都有 $\int_a^b f(x)g(x)\,dx=0$，证明 $f$ 在该区间上恒为零。
- 8.3.7 分部积分（Integration by parts）。
- 8.3.8 换元积分（Integration by substitution）。
- 8.3.9 复合换元积分的条件。
- 8.3.10（Schwarz 不等式）若 $f,g$ 均连续，证明 $\left(\int_a^b f(x)g(x)\,dx\right)^2\le\left(\int_a^b [f(x)]^2\,dx\right)\left(\int_a^b [g(x)]^2\,dx\right)$。<span style="color:#7f8c8d">书页 343 · §8.4 Cauchy's Second Method（Cauchy 第二方法）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）：**</span> 面对无界函数（在 0 处趋于无穷大的 1/√x），前面对连续函数甚至"有限个不连续点"的积分方法都失效了。Cauchy 第二方法的第一性原理极其朴素：绕开坏点——先在坏点右侧一个正 δ 处正常积分，再把截断点 δ 推向 0 取极限，于是"广义积分"被定义为截断积分的极限。这与你处理有符号整型溢出时"放大尺度再取极限"、以及级数用部分和极限定义总和，是同一套"用一个可计算对象的极限来定义原对象"的思想。注意书中的几何直觉：$\int_0^1 x^{-1/2}\,dx$ 竟等于 $1+\tfrac12+\tfrac14+\cdots$，被求和出一个几何级数 $2$——这直接连接 6.042J 的无穷求和与 CLRS 的分治求和。历史注：Cauchy 1823 年在《无穷小计算教程》（Résumé des leçons……sur le calcul infinitésimal）为连续函数定义了第一个严格的积分（通常即"Cauchy 第一方法"），并意识到这方法对有无穷奇点的函数会失效，于是被迫走向这里概述的"第二方法"——广义（反常）积分。这一创举也让他被后世视为严格积分理论的奠基人，而"为什么必须区分可积与不可积、收敛与发散"正是从他这里第一次被认真追问。

---


正如我们在上一节中所做的那样，只为 continuous functions（连续函数）定义 integral（积分），实在太过局限（too limiting）。

即便在十九世纪早期，需要处理更一般函数的必要性也已十分明显。

对 Cauchy 而言，这意味着处理具有 discontinuity（不连续性）的函数。

但 Cauchy 不会感到任何处理严重不连续函数的必要，事实上他甚至可能根本不把这样的对象视为函数。

用我们的术语来说，Cauchy 所关心的是把他的积分从连续函数推广到具有 isolated discontinuities（孤立不连续点）的函数（即：不连续点集合只包含孤立点）。

我们在 8.2.1 节已经指出，具有有限多个不连续点的有界函数并不构成任何困难。

Cauchy 第一方法（Cauchy's first method）可以应用于它们。

真正带来抵抗的，是无界（unbounded）函数的情形。

我们应该怎样理解积分 $\int_0^1 \dfrac{dx}{\sqrt{x}}$ 呢？

虽然被积函数只有一个不连续点（在 $x=0$ 处），但该函数是无界的，因此 Cauchy 第一方法无法应用。

如果该积分确实有意义，那么我们会预期函数 $F(\delta) = \int_\delta^1 \dfrac{dx}{\sqrt{x}}$ 在整个区间 $[0,1]$ 上都有定义且连续，并且值 $F(0)$ 将等于我们的积分。

但这里 $F(x)$ 在 $x=0$ 处没有定义，尽管它对所有 $x\in(0,1]$ 都有定义，因为对 $x>0$，被积函数在任意区间 $[x,1]$ 上连续。

若计算之，我们看到 $F(\delta) = \int_\delta^1 \dfrac{dx}{\sqrt{x}} = 2 - 2\sqrt{\delta}$。

虽然我们不能取 $F(0)$ 本身（它没有定义），但我们确实可以取极限，即

```math
\lim_{\delta\to 0^+} F(\delta) = \lim_{\delta\to 0^+} \int_\delta^1 \frac{dx}{\sqrt{x}} = 2,
```

作为该积分一个完全合理的值。

事实上，如果我们把它看作一个求图 8.3 中无界区域面积的问题，我们就能从图形上理解为何答案应为 2。

注意到图中 $0<a<b<c<1$，且这些数取值为 $a=1/64$，$b=1/16$，$c=1/4$。

这些积分的值分别为 $\int_a^b x^{-1/2}\,dx = 1/4$、$\int_b^c x^{-1/2}\,dx = 1/2$，以及 $\lim F(\delta) = \int_c^1 x^{-1/2}\,dx = 1$，

因此我们预期 $\int_0^1 x^{-1/2}\,dx = 1 + 1/2 + 1/4 + \cdots = 2$，正如这一方法确实给出的那样。

这正是 Cauchy 第二方法（Cauchy's second method）。

如果你理解了这个例子，你就理解了这个方法。

任何对这一方法的一般性叙述，都可能遮蔽这个简单思想。

<span style="color:#7f8c8d">书页 344 · §8.4 Cauchy's Second Method（Cauchy 第二方法）</span>

然而，我们确实需要一些语言（language）。

通过取极限来获得积分的最终值的这一过程，可能起作用也可能不起作用。

如果极限存在，我们就说该积分收敛（converges），或是一个收敛积分（convergent integral），并说函数 $f$ 依 Cauchy 第二方法是可积的（integrable），若上下文清楚则简称为可积。

否则，该积分称为发散的（divergent）。

图 8.3. 计算 $\int_0^1 x^{-1/2}\,dx = 2$。

我们给出一个 formal definition（正式定义），它仅适用于函数只有一个无界点、且该点落在区间左端点这一情形。

对于多于一个点，或对于不在端点处的点，最好通过把积分拆分成若干单独的积分来推广这一定义，其中每个积分都能一次一个地这样处理。

（参见 Exercise 8.4.3（练习 8.4.3）。）

**[definition] 定义 8.10**

> <span style="color:#7f8c8d">TBB §8.4, p.344</span>

设 $f$ 是区间 $(a,b]$ 上的连续函数，且 $f$ 在每个区间 $(a, a+\delta)$ 上无界。

则我们定义

```math
\int_a^b f(x)\,dx
```

为

```math
\lim_{\delta\to 0^+} \int_{a+\delta}^b f(x)\,dx
```

只要该极限存在，在此情形下该积分称为收敛的。

若两个积分 $\int_a^b f(x)\,dx$ 与 $\int_a^b |f(x)|\,dx$ 都收敛，则该积分称为绝对收敛的（absolutely convergent）。

**[note] 注**

> <span style="color:#7f8c8d">TBB §8.4, p.344</span>

关于 absolute convergence（绝对收敛）这一额外条件的作用，与它在无穷级数研究中的作用十分相似。

你会记得，绝对收敛级数（absolutely convergent series）更为"稳健"（robust），意思是它们可以被相当自由地操作，而不绝对收敛的级数则相当"脆弱"（fragile）。

对于绝对收敛积分，情形同样如此。

注意到积分 $\int_0^1 x^{-1/2}\,dx$ 既是收敛的也是绝对收敛的，仅仅因为被积函数是非负的（nonnegative）。<span style="color:#7f8c8d">书页 345 · §8.4 反常积分 / §8.5</span>

**§8.4 习题（部分保留）· 柯西第二方法（续）**

> <span style="color:#7f8c8d;">习题 8.4.1 与 8.4.2 给出了两种重要的反常积分定义，正文中会引述，故在此完整保留英文原题并附最小翻译。</span>

<span style="color:#7f8c8d">习题</span>

**8.4.1** 对在 $[a,b)$ 上连续、且在右端点无界（unbounded at the right-hand endpoint）的函数 $f$，为其积分 $\displaystyle\int_a^b f(x)\,dx$ 给出一个定义，并给出一个例子。

- 英文原题：*Formulate a definition of the integral $\int_a^b f(x)\,dx$ for a function continuous on $[a,b)$ and unbounded at the right-hand endpoint. Supply an example.*

**8.4.2** 对在 $[a,c)$ 与 $(c,b]$ 上连续、且在每个含 $c$ 的区间内均无界的函数 $f$，为其积分 $\displaystyle\int_a^b f(x)\,dx$ 给出一个定义，并给出一个例子。

- 英文原题：*Formulate a definition of the integral $\int_a^b f(x)\,dx$ for a function continuous on $[a,c)$ and on $(c,b]$ and unbounded in every interval containing $c$. Supply an example.*

> <span style="color:#7f8c8d;">习题 8.4.3–8.4.8（$f$ 连续时形如 $\int_0^3 \frac{f(x)}{\sqrt{|x(x-1)(x-2)(x-3)|}}\,dx$ 的反常积分应如何解释，以及柯西第二方法的相关性质推广）均非必要，依规则跳过，不逐条翻译。</span>

**§8.5 柯西第二方法（续）· 无穷区间上的反常积分**

处理无界函数积分的那一思想，柯西也用来处理定义在无界区间（unbounded intervals）上的函数。我们应当如何理解积分
```math
\int_1^\infty \frac{dx}{x^2}\ ?
```
我们或许可以先尝试对无界区间 $[1,\infty)$ 作一个分划，并寻求某类 Riemann 和（Riemann sums）的极限。但一个简单得多的想法是：照显而易见的方式把柯西第二方法（Cauchy's second method）推广到这里。
```math
\int_1^\infty \frac{dx}{x^2}
=\lim_{X\to\infty}\int_1^X \frac{dx}{x^2}
=\lim_{X\to\infty}\left(1-\frac{1}{X}\right)=1.
```

<span style="color:#7f8c8d">书页 346 · §8.5 柯西第二方法（续）</span>

**图 8.4 · [example] 计算 $\int_1^\infty x^{-2}\,dx=1$**

在图 8.4 中，我们以图形方式展示了如何计算由 $\int_1^\infty x^{-2}\,dx$ 所表示的面积（area）。注意到
```math
\int_1^2 x^{-2}\,dx=1/2,\qquad \int_2^4 x^{-2}\,dx=1/4,\qquad \int_4^8 x^{-2}\,dx=1/8,
```
因此我们理应预期
```math
\int_1^\infty x^{-2}\,dx=1/2+1/4+1/8+\cdots=1,
```
而这一方法给出的结果正是如此（见图 8.4）。

这正是把柯西第二方法应用于无界区间的情形。同样地，如果你理解了这个例子，你就理解了这种方法。

我们对仅形如 $[a,\infty)$ 的无穷区间给出一个正式定义。情形 $(-\infty,b]$ 是类似的；情形 $(-\infty,+\infty)$ 最好拆成两个积分之和，即 $(-\infty,a]$ 与 $[a,\infty)$ 上的两个积分，这两个积分都可用此方式处理。（见习题 8.5.2。）

---
**定义 8.11 · [definition] 无穷区间 $[a,\infty)$ 上的反常积分（The Integral on an Infinite Interval）**

> <span style="color:#7f8c8d;">TBB §8.5, p.346</span>

> <span style="color:#7f8c8d;">设 $f$ 是区间 $[a,\infty)$ 上的连续函数。于是我们定义 $\int_a^\infty f(x)\,dx$ 为 $\lim\limits_{X\to\infty}\int_a^X f(x)\,dx$，若该极限存在；此时称该积分收敛（convergent）。若两个积分 $\int_a^\infty f(x)\,dx$ 与 $\int_a^\infty |f(x)|\,dx$ 都收敛，则称该积分为绝对收敛（absolutely convergent）。</span>

再一次地，绝对收敛这一附加条件所起的作用，与它在无穷级数（infinite series）研究中所起的作用非常相似。注意积分 $\int_1^\infty x^{-2}\,dx$ 是收敛的，并且仅仅因为被积函数非负，它也是绝对收敛的。$\blacksquare$

<span style="color:#7f8c8d">习题</span>

> <span style="color:#7f8c8d;">习题 8.5.1–8.5.2：为连续于 $(-\infty,b]$ 的函数给出 $\int_{-\infty}^b f(x)\,dx$ 的定义（含收敛与发散之例子），并讨论 $(-\infty,+\infty)$ 情形。依规则跳过，不逐条翻译。</span><span style="color:#7f8c8d">书页 347 · §8.6 The Riemann Integral（Riemann 积分）</span>

**§8.6 The Riemann Integral（Riemann 积分）**

> <span style="color:#7f8c8d;">页首为 §8.5 的习题区（8.5.2–8.5.13，涉及无穷区间上的反常积分（improper integral）），依规则非必要习题予以跳过，仅保留概览。</span>

<span style="color:#7f8c8d">本页习题概览（依规则跳过，仅供索引）：</span>

- 8.5.2 为在 $(-\infty,\infty)$ 上连续的函数表述积分 $\int_{-\infty}^{\infty}f(x)\,dx$ 的定义，并给出该类型收敛与发散积分的例子。
- 8.5.3 确定使积分 $\int_1^{\infty}x^{-p}dx$ 收敛的 $p$ 的取值范围。
- 8.5.4 证明 $\int_0^{\infty}x^n e^{-x}dx=n!$。
- 8.5.5 若 $f$ 在 $[1,\infty)$ 上连续且满足 $\lim_{x\to\infty}f(x)=\alpha$，证明：若 $\int_1^{\infty}f(x)\,dx$ 收敛，则必有 $\alpha=0$。
- 8.5.6 若 $f$ 在 $[1,\infty)$ 上连续且 $\int_1^{\infty}f(x)\,dx$ 收敛，能否得出 $\lim_{x\to\infty}f(x)=0$？
- 8.5.7 若 $f$ 在 $[1,\infty)$ 上连续且单调递减（decreasing），证明 $\int_1^{\infty}f(x)\,dx$ 收敛当且仅当级数 $\sum_{n=1}^{\infty}f(n)$ 收敛（积分检验的雏形，与后文 8.7 呼应）。
- 8.5.8 给出连续函数 $f$ 使积分收敛但级数 $\sum_{n=1}^{\infty}f(n)$ 发散的例子。
- 8.5.9 给出连续函数 $f$ 使积分发散但级数 $\sum_{n=1}^{\infty}f(n)$ 收敛的例子。
- 8.5.10 证明 $\int_0^{\infty}\frac{\sin x}{x}dx$ 收敛但不绝对收敛（absolutely convergent）。
- 8.5.11（Cauchy 收敛准则）若 $f:[a,\infty)\to\mathbb{R}$ 连续，证明 $\int_a^{\infty}f(x)\,dx$ 收敛当且仅当：对每个 $\varepsilon>0$ 存在 $M$，使得对所有 $M<c<d$，均有 $\left|\int_c^d f(x)\,dx\right|<\varepsilon$。
- 8.5.12（绝对收敛的 Cauchy 判据）若 $f:[a,\infty)\to\mathbb{R}$ 连续，证明 $\int_a^{\infty}f(x)\,dx$ 绝对收敛当且仅当：对每个 $\varepsilon>0$ 存在 $M$，使得对所有 $M<c<d$，均有 $\int_c^d |f(x)|\,dx<\varepsilon$。
- 8.5.13（项目题）确定 §8.3 中对有限区间上连续函数成立的积分性质，哪些可以推广到无穷区间 $[a,\infty]$，并给出证明。

正式正文自本节引言开始：到目前为止，在我们对积分的讨论中，我们已定义符号 $\int_a^b f(x)\,dx$ 的含义，首先对所有连续函数借助 Cauchy 第一方法（Cauchy's first method），然后对在有限个不连续点处无界的函数借助 Cauchy 第二方法（Cauchy's second method）。$\blacksquare$

<span style="color:#7f8c8d">书页 348 · §8.6 The Riemann Integral（Riemann 积分）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）：**</span> 这里发生了全书一次重要的视角翻转：Cauchy 的做法是"列一个函数类（连续函数），再定义积分"； Riemann 的做法则是"直接定义一种可积性性质，再去刻画满足它的函数类"。第一性原理：与其逐个函数问"这个能不能积"，不如把"能积"本身定义成一个标准——于是"哪些函数可积"变成一个待研究的刻画问题，这正是现代数学"先用定义卡出一个类、再刻画这个类"的典型模板，和你用 6.042J 里"先定义关系、再刻画其性质的集合"异曲同工。Colding 在课堂上给这个定义很高的评价：

🎥 *Colding 教授*："I think this was the first way where you have a definition that really made sense."（翻译：我认为这是第一次出现了真正讲得通的积分定义。）

> 定义 8.12 的核心是"对每个 ε 存在 δ，使所有小区间长度小于 δ 的分划的所有 Riemann 和都落在 I 的 ε 邻域内"——注意关联点 ξk 可以任意选取，这正是后面定理 8.15 要用力去对付的地方。

---


让我们回到 Cauchy 第一方法。我们要问的是，这个方法究竟能被应用到多远。它可以应用到所有连续函数；这正是定理 8.1（Theorem 8.1）的内容。它可以应用到所有只有有限多个不连续点的有界函数（习题 8.2.15）。它也可以应用到某些具有无限多个不连续点的有界函数之中（习题 8.2.16）。

我们不再去搜索适用这一方法的更泛函数类，转而采纳 Riemann 所采取的视角。我们径直定义"能应用 Cauchy 第一方法的所有函数"这一函数类，然后尝试刻画这一函数类。这代表了比 Cauchy 会采取的视角远为现代的观点，因为 Cauchy 对"什么是函数"持有更局限的看法。注意我们只需把定理 8.1 转变成为一条定义。

**定义 8.12 · [definition] Riemann 可积（Riemann Integrable）**

> <span style="color:#7f8c8d;">TBB §8.6, p.348</span>

设 $f$ 为区间 $[a,b]$ 上的一个函数。假设存在一个数 $I$，使得对每个 $\varepsilon>0$ 都能找到 $\delta>0$，从而当下式成立时满足条件——

```math
\left|\sum_{k=1}^{n}f(\xi_k)(x_k-x_{k-1})-I\right|<\varepsilon
```

——其中 $[x_0,x_1],[x_1,x_2],\ldots,[x_{n-1},x_n]$ 是区间 $[a,b]$ 的一个分划，且各子区间长度均小于 $\delta$，每个 $\xi_k$ 是区间 $[x_{k-1},x_k]$ 中的一点。那么 $f$ 称为在 $[a,b]$ 上 Riemann 可积（Riemann integrable），并且我们记

```math
\int_a^b f(x)\,dx
```

为该数 $I$。

我们可以把点集

```math
\pi=\{x_0,x_1,x_2,\ldots,x_{n-1},x_n\}
```

称为区间 $[a,b]$ 的分划（partition）；或者，如果更方便，也可以等价地把区间族

```math
[x_0,x_1],[x_1,x_2],\ldots,[x_{n-1},x_n]
```

称为分划。从每个区间 $[x_{k-1},x_k]$ 中选出的点 $\xi_k$ 被称为该分划的关联点（associated points）。请注意，在定义中，关联点可以在分划的各区间之内自由选取。

粗略地说，函数 $f$ 是 Riemann 可积的，如果 $f$ 的 Riemann 和（Riemann sums）在该区间上的极限存在。目前的计划是：确定哪些函数类是 Riemann 可积的，并得到 Riemann 可积性的各种刻画。我们将在本节余下的部分研究这个问题。

我们还需要查明：对连续函数成立的积分性质，现在是否对所有 Riemann 可积函数继续成立。我们将在下一节考虑这一点。

从先前的工作出发，我们立刻可以得到两点观察：<span style="color:#7f8c8d">书页 349 · §8.6 Riemann 积分</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）：**</span> 例 8.13 给出"处处不连续"的 Dirichlet 函数（有理数取 1、无理数取 0）：它在任意小区间上的上确界恒为 1、下确界恒为 0，所以上合恒为区间长、下合恒为 0，二者永不相等——不唯一地把"可积"的标准卡死。Colding 用一句非常直觉的话概括了病因：

🎥 *Colding 教授*："if it's not just a point but it's a proper interval, then there's always points that are rational and always points that are not rational... the sup here would have to be 1, but the inf here would be 0."（翻译：只要不是单个点而是真正的小区间，就总既有有理点也有无理点……于是上确界必为 1，下确界必为 0。）

> 需要辨析一处术语：TBB 把例 8.14 中 f(p/q)=1/q 的那个函数也叫"Dirichlet 函数"，但更准确的称呼是 Thomae 函数（1875 年，Thomae 提出），它只在每个有理点有"微量"跳跃、而在每个无理点连续，因此虽在不连续点稠密却仍可积、且积分为 0。相比之下，真正的 Dirichlet 函数（处处不连续）是 Riemann 不可积的。历史上 Dirichlet 约在 1829/1837 年（研究 Fourier 级数收敛时）给出他那个处处不连续的例子，而"递增分母的 1/q"这一可积变体到 1875 年才由 Thomae 整理。分辨这一对"表亲"对把握"不连续点的'多少'×'大小'共同决定可积性"至关重要。

---


所有连续函数都是 Riemann 可积的（Riemann integrable）。所有 Riemann 可积的函数都是有界的（bounded）。鉴于最后这条陈述，我们看到Riemann积分在某种程度上是有限的，因为它在处理无界函数时将无能为力。为此我们仍需回到柯西的第二方法（Cauchy's second method）。不过，正如我们将看到的，Riemann积分能够处理许多"坏地不连续"（但并非太坏）的有界函数。随着十九世纪研究的推进，Riemann积分成为讨论有界函数积分的标准工具。对于无界函数，柯西的第二方法仍被继续采用，尽管这时也出现了其他方法。到二十世纪初，Riemann积分已为所有严肃的分析学家所摒弃，转而采用Lebesgue积分（Lebesgue's integral）。Riemann积分之所以能存活于诸如此类的教科书中，主要在于Lebesgue那种更优却更困难的方法在技术上烦琐。

**§8.6.1 若干例子（Some Examples）**

所有 Riemann 可积的函数都是有界的。所有连续函数都是 Riemann 可积的。为了对"什么样的函数是可积的"这一问题获得一些洞见，我们给出若干例子：首先是一个有界却不可积的函数，然后是一个"坏地不连续"但可积的函数。

**例 8.13 · [example] 有界但"太不连续"而不可积的函数**

> <span style="color:#7f8c8d;">TBB §8.6, p.349</span>

这里给出一个函数，它有界但"太不连续"（too discontinuous）以致不可Riemann积分。在区间 $[0,1]$ 上，令 $f$ 对有理数 $x$ 等于 $1$、对无理数 $x$ 等于 $0$。设
```math
[x_0,x_1],\;[x_1,x_2],\;\ldots,\;[x_{n-1},x_n]
```
为任意分划。若我们选取相应点（associated points）$\xi_k\in[x_{k-1},x_k]$ 使 $\xi_k$ 为有理数，则 Riemann 和（Riemann sum）满足
```math
\sum_{k=1}^n f(\xi_k)(x_k-x_{k-1})=\sum_{k=1}^n (x_k-x_{k-1})=1\tag{2}
```
而若我们选取相应点 $\eta_k\in[x_{k-1},x_k]$ 使 $\eta_k$ 为无理数，则
```math
\sum_{k=1}^n f(\eta_k)(x_k-x_{k-1})=0.\tag{3}
```
由于 (2) 与 (3)，积分 $\int_0^1 f(x)\,dx$ 不可能存在。$\blacksquare$

**例 8.14 · [example] Dirichlet 函数的可积性**

> <span style="color:#7f8c8d;">TBB §8.6, p.349</span>

回忆狄利克雷函数（Dirichlet function，见 §5.2.6），它给出一个在每个有理数处不连续、在每个无理数处连续的函数之例。我们证明该函数是 Riemann 可积的。在区间 $[0,1]$ 上令 $f(0)=0$，在有理数处对 $0<p/q\le1$ 令 $f(p/q)=1/q$（假定 $p/q$ 已表示为最简形式），而对无理数 $x$ 令 $f(x)=0$。

任给 $\varepsilon>0$。令 $q_0$ 为任何大于 $2/\varepsilon$ 的正整数。我们来数一数 $[0,1]$ 中满足 $f(x)>1/q_0$ 的点 $x$ 的个数。这样的点只有有限多个，设其为 $M$ 个。

<span style="color:#7f8c8d">书页 350 · §8.6 Riemann 积分</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）：**</span> 振幅 ωf([c,d])=sup f − inf f 度量的是"函数在一个小区间内波动的总幅度"。第一性原理： Riemann 和能收敛的唯一理由是"当区间切得足够细时，函数在每段上的波动可以被压到任意小"；如果一个小区间里函数从 0 跳到 1（如 Dirichlet 函数），那无论切多细都是灾难。于是"可积"就可以被等价地翻译成"（以长度加权后）总振幅可以被压到 ε 以内"——这为后面定理 8.15/8.16/8.17 提供了统一的"显微镜"。对连续函数，振幅正是"最大值减最小值"，且只要区间够小振幅就够小（这是连续函数可积的几何原因）；而对不连续点，振幅就等于该点"跳跃的高度"。这一步其实建立了"不连续点的大小画像"：每个点 x 有一个振幅 ωf(x)，它非零 ⟺ f 在 x 处不连续（证明 8.17 会用到）。这在概念上就像你用 CSS 的网格/分块（grid/partition）把波动大小分层度量。历史注：正是 Riemann 在 1854 年首创用振幅分析可积性，把"跳跃多高、分布在多小的集合上"这一思路明确下来。

---


选取 $\delta_1$ 足够小，使得这些点中的任意两点相隔都大于 $2\delta_1$。再选取 $\delta<\delta_1$，使得（其理由要到我们做完所有计算之后才明晰）$M\delta<\varepsilon/2$。这将使我们能够运用不等式
```math
M\delta + 1/q_0 < \varepsilon.\tag{4}
```
设
```math
[x_0,x_1],\;[x_1,x_2],\;\ldots,\;[x_{n-1},x_n]
```
为任意一个分划，使得其中每个小区间都短于 $\delta$。对于任意选取的相应点 $\xi_k\in[x_{k-1},x_k]$，我们注意到以下三种情形之一成立：

- (i) 若 $\xi_k=0$ 或 $\xi_k$ 是无理数，则 $f(\xi_k)=0$；
- (ii) 若 $\xi_k$ 是先前数出的 $M$ 个点之一，则 $f(\xi_k)>1/q_0$；
- (iii) 若 $\xi_k$ 是任何其他有理点，则 $0<f(\xi_k)\le1/q_0$。

我们可以通过分别考虑这三种情形来估计 Riemann 和
```math
\sum_{k=1}^n f(\xi_k)(x_k-x_{k-1}).
```
情形 (i) 显然对该和没有贡献。情形 (ii) 至多对该和贡献 $M\delta$，因为分划中每个区间至多包含一个类型 (ii) 的点，且这样的点总共只有 $M$ 个。最后，情形 (iii) 总共至多贡献 $1/q_0$。于是，利用不等式 (4)，我们得到
```math
0 \le \sum_{k=1}^n f(\xi_k)(x_k-x_{k-1}) \le M\delta + 1/q_0 < \varepsilon.
```
这证明了积分 $\int_0^1 f(x)\,dx=0$。考虑到这个函数究竟有多不连续（它具有一个稠密的不连续点集），它竟然仍可积，这令人震惊。$\blacksquare$

**§8.6.2 Riemann 的判据（Riemann's Criteria）**

> <span style="color:#7f8c8d;">进阶章节，可略读（Advanced section. May be omitted）。</span>

那么，什么样的有界函数才是 Riemann 可积的？答案是：这样的函数必须"大部分"是连续的。例 8.13 中那个极不连续的函数之例已暗示了这一点。另一方面，例 8.14 表明一个 Riemann 可积函数的全部不连续点甚至可能是稠密的。Riemann首先通过函数 $f$ 在一个区间上的振幅（oscillation）来分析这一点。我们回忆（定义 6.24）它定义为
```math
\omega_f([c,d])=\sup_{x\in[c,d]} f(x)-\inf_{x\in[c,d]} f(x).
```
这度量的是函数 $f$ 在区间 $[c,d]$ 内变化的幅度。对于连续函数而言，这正是 $f$ 在 $[c,d]$ 上最大值与最小值之差，并且只要区间 $[c,d]$ 足够小，它就将会很小。<span style="color:#7f8c8d">书页 351 · §8.6 Riemann 的判据（Riemann's Criteria）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）：**</span> 定理 8.15、8.16 把"可积"化约为一个纯量化的加权和条件：∑ωf([x_{k−1},x_k])Δxk<ε。这里咬合两个证明策略：一是 ε/2 技巧（split-the-epsilon）——定理 8.15 的证明先把"两个 Riemann 和都离积分 I 在 ε/4 内"这条可积性事实搬出来，再用三角不等式把差压到 ε；二是"集合二分"（classify-then-bound），定理 8.16 把加细后的小区间分成两类——完全落在旧小区间内的（好区间，用旧分划的 ω 定界）与横跨旧分点的（坏区间，至多 n−1 个，用粗略的 2M 定界）——然后分别控制，这正是分治里"把坏分子单独隔离处理"的经典套路。Colding 给出了这个判据的口语版，方便你记住它的一处必要条件（尽管 TBB 的定理以积分本身表述）：

🎥 *Colding 教授*："if we want to check that a function is Riemann integrable, then we just need to check that for all epsilon, we can find a partition with this property."（翻译：若我们要检验一个函数是否Riemann可积，只需检验：对一切 ε，都能找到一个具备该性质的分划。）

> 注意定理 8.16 比 8.15 更省力：只需"存在一个好分划"，而不必检查"所有细分划"。这让你想起在 6.042J 里"存在性证明只需构造一个例子"的作风。

---


**定理 8.15 · [theorem] Riemann（Riemann）判据**

> <span style="color:#7f8c8d;">TBB §8.6, p.351</span>

定义在区间 $[a,b]$ 上的函数 $f$ Riemann 可积（Riemann integrable），当且仅当对每个 $\varepsilon>0$ 都存在一个 $\delta>0$，使得无论 $[x_0,x_1],[x_1,x_2],\ldots,[x_{n-1},x_n]$ 何时为区间 $[a,b]$ 的、把区间剖分成每个小区间长度小于 $\delta$ 的分划（partition），都有
```math
\sum_{k=1}^n \omega_f([x_{k-1},x_k])(x_k-x_{k-1})<\varepsilon.
```

**证明。**

若 $f$ 在 $[a,b]$ 上以积分 $I$ Riemann 可积，则对任意 $\varepsilon>0$，必定存在一个 $\delta>0$，使得取一个所有小区间都小于 $\delta$ 的分划时，任意两个 Riemann 和（Riemann sum）都与 $I$ 相距不超过 $\varepsilon/4$。特别的，我们有
```math
\left|\sum_{k=1}^n f(\xi_k)(x_k-x_{k-1})-\sum_{k=1}^n f(\eta_k)(x_k-x_{k-1})\right|<\varepsilon/2
```
无论 $[x_0,x_1],[x_1,x_2],\ldots,[x_{n-1},x_n]$ 何时为区间 $[a,b]$ 的、长度小于 $\delta$ 的分划。这里 $\xi_k$ 和 $\eta_k$ 是从 $[x_{k-1},x_k]$ 中任意选取的。我们把它改写为
```math
\left|\sum_{k=1}^n [f(\xi_k)-f(\eta_k)](x_k-x_{k-1})\right|\le\varepsilon/2<\varepsilon.\tag{5}
```
现在注意到
```math
\sup_{\eta,\xi\in[x_{k-1},x_k]}(f(\xi)-f(\eta))=\omega_f([x_{k-1},x_k]).
```
于是我们看到，在不等式 (5) 中对 $\xi_k$ 与 $\eta_k$ 的这些选取取上确界（supremum），判据便立即得出。定理的另一个方向可以解释为一个"柯西判据"（Cauchy criterion），其证明方式与书中此前所有柯西判据的证明相类似（实际上与定理 8.1 的证明相类似）。我们略去这些细节。$\blacksquare$

定理 8.15 提供了可积性的一个有趣充要条件。这里的充分性判据使用起来很笨拙，因为它要求我们检查所有的小分划都具有某一性质。下面这个变体用起来稍容易一些，因为对每个正的 $\varepsilon$，我们只需找到一个分划。

**定理 8.16 · [theorem] 可积性的振幅和判据**

> <span style="color:#7f8c8d;">TBB §8.6, p.351/352</span>

区间 $[a,b]$ 上的函数 $f$ Riemann 可积，当且仅当对每个 $\varepsilon>0$，区间 $[a,b]$ 至少存在一个分划 $[x_0,x_1],[x_1,x_2],\ldots,[x_{n-1},x_n]$，使得
```math
\sum_{k=1}^n \omega_f([x_{k-1},x_k])(x_k-x_{k-1})<\varepsilon.
```

**证明。**

由定理 8.15，若 $f$ Riemann 可积，则必定存在这样的一个分划。

在反方向上，我们必须证明这里的条件蕴含着可积性。当然，这个条件蕴含着 $f$ 有界（bounded，否则这个和将为无穷），因而我们可以假设对所有 $x$ 都有 $|f(x)|\le M$。这给了我们对任意区间 $[c,d]$ 上的振幅（oscillation）大小的一个有用而粗略的估计：
```math
\omega_f([c,d])\le 2M.
```

<span style="color:#7f8c8d">书页 352 · §8.6 Riemann 的判据（Riemann's Criteria）</span>

设 $\varepsilon>0$。我们将找到一个数 $\delta$，使得定理 8.15 的判据被满足。设 $[x_0,x_1],[x_1,x_2],\ldots,[x_{n-1},x_n]$ 为题目所给的那个存在的分划。我们利用它来找出 $\delta$。选取 $\delta$ 足够小，使得
```math
2Mn\delta<\varepsilon.
```
现在设
```math
[y_0,y_1],[y_1,y_2],\ldots,[y_{m-1},y_m]
```
为区间 $[a,b]$ 的任一分划，把区间剖分成每个小区间长度小于 $\delta$。这些小区间分为两类：第 (i) 类是完全包含在原始分划的某个小区间之内的那些；第 (ii) 类是把某个点 $x_k$（$k=1,2,\ldots,n-1$）作为内点包含在内的那些。无论如何，后一类至多只有 $n-1$ 个，且每个长度小于 $\delta$。于是，仅对其中每一项用粗略的估计，第 (ii) 类区间对和
```math
\sum_{k=1}^m \omega_f([y_{k-1},y_k])(y_k-y_{k-1})
```
的贡献不超过 $(2M)n\delta$。所有第 (i) 类区间上的和必须小于
```math
\sum_{k=1}^n \omega_f([x_{k-1},x_k])(x_k-x_{k-1})<\varepsilon.
```
于是总和
```math
\sum_{k=1}^m \omega_f([y_{k-1},y_k])(y_k-y_{k-1})<2Mn\delta+\varepsilon<2\varepsilon.
```
由定理 8.15 中的判据即知，$f$ Riemann 可积，此即所证。$\blacksquare$

**§8.6.3 Lebesgue 的判据（Lebesgue's Criterion）**

> <span style="color:#7f8c8d;">进阶章节，可略读（Advanced section. May be omitted）。</span>

定理 8.16 很漂亮，看似以一种有意义的方式刻画了 Riemann 可积函数这一类别。但在 Riemann 那个时代，人们对实数集仅有一种不完善的理解，因此 Riemann 并未想到：一个有界函数 $f$ 的 Riemann 可积性，仅仅取决于 $f$ 的不连续点（point of discontinuity）之集的性质。的确，作用于函数振幅上的那个条件
```math
\sum_{k=1}^n \omega_f([x_{k-1},x_k])(x_k-x_{k-1})<\varepsilon
```
暗示着其中发生的情形比这还要微妙。在 1901 年，亨利·Lebesgue（Henri Lebesgue）借助零测度（measure zero）集的概念补全了这个定理。回忆（见 §6.8）实数的一个集合 $E$ 是零测度的，若对每个 $\varepsilon>0$ 都存在一列区间（interval）$\{(c_i,d_i)\}$ 覆盖 $E$ 的所有点，且其总长度 $\sum_{i=1}^\infty (d_i-c_i)<\varepsilon$。 Riemann 可积函数的准确刻画正是如此：它们是有界的（如我们所熟知），而且它们的不连续点集为零测集——这正是下面定理 8.17 的内容。<span style="color:#7f8c8d">书页 353 · §8.6 Theorem 8.17（Riemann-Lebesgue）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）：**</span> 定理 8.17 是这一节的巅峰：有界函数 Riemann 可积 ⟺ 其不连续点集是零测集（几乎处处连续，a.e.）。第一性原理：这是把前面所有直觉压缩成一句话——"能积"= "坏点（不连续点）既没'多少'（测度零）也没'太大'（有界）"。零测集是个极聪明的否定式定义：一个集合可以稠密（如全体有理数）却仍"总长"任意小，于是"测度为 0"管住的是集合的"长度总量"而非"疏密程度"。这要连接你在 6.042J 学的可数性：可数集必为零测集，而零测集未必可数。定理证明的正反向分别用了上一组判据（8.15/8.16）并配以"把大振幅点揪出来用短区间盖住"的覆盖策略（covering-a-small-set），其中坏点集合 N(ε)（振幅>ε 的点）被一列总长 <ε 的开区间盖住——这叫"用区间把坏区域包起来，越包越细"。历史注： Riemann 1854 年已得到振幅判据，但受制于当时对实数集理解不完善，没意识到可积性只取决于不连续点的集合性质；1901 年 Lebesgue（他在 1902 年博士论文《积分、长度与面积》中系统发展 Lebesgue 测度与积分）补上了"零测集"这个关键概念，才把定理推进为今天的充要刻画——故文献中也常把它称作"Lebesgue 可积性判据"。这正是" Riemann–Lebesgue"这一双名字的由来：判据条件出自 Riemann，而零测集的现代语言出自 Lebesgue。

---


上面那段话的意思是：函数在除某个零测集（set of measure zero，其定义见 §6.8）之外的一切点上都是连续的。（用现代说法，它们被称为"几乎处处连续"（continuous almost everywhere），记作"几乎处处（a.e.）连续"。）

**定理 8.17（Riemann-Lebesgue）** 一个在区间 $[a,b]$ 上的函数 $f$ 是 Riemann 可积的（Riemann integrable），当且仅当 $f$ 有界（bounded），且 $[a,b]$ 中 $f$ 不连续的那些点所构成的集合是一个零测集。

> <span style="color:#7f8c8d;">TBB §8.6, p.353</span>

**证明。** 必要性（necessity）并不难证，但对我们而言是最不重要的一部分。充分性（sufficiency）更为重要，也更难证明。在整个证明中，我们需要熟悉第 6.7 节所讨论的函数 $f$ 在点 $x$ 处的振幅（oscillation）$\omega_f(x)$ 这一概念。回忆：这个值非零当且仅当 $f$ 在 $x$ 处不连续。

让我们先假设 $f$ 是 Riemann 可积的。显然 $f$ 是有界的。固定 $\varepsilon>0$，并考虑集合 $N(\varepsilon)$，它包含所有使 $f$ 在 $x$ 处的振幅大于 $\varepsilon$ 的点 $x$；也就是说，
```math
\omega_f(x)>\varepsilon.
```
任何一个含有点 $x\in N(\varepsilon)$ 的区间 $(c,d)$ 必满足
```math
\omega_f([c,d])\ge\varepsilon.
```
取 $\varepsilon>0$，运用定理 8.15 找出构成 $[a,b]$ 的一个分划（partition）的诸区间
```math
[x_0,x_1],\;[x_1,x_2],\;\ldots,\;[x_{n-1},x_n],
```
使得
```math
\sum_{k=1}^n \omega_f([x_{k-1},x_k])(x_k-x_{k-1})<\varepsilon/2 .
```
从这些区间里，只挑选那些内部（interior）含有 $N(\varepsilon)$ 中某点的区间。这些区间的总长度不能超过 $\varepsilon/2$，因为对这样的每个区间 $[x_{k-1},x_k]$ 必有 $\omega_f([x_{k-1},x_k])\ge \varepsilon$。

于是，我们成功地把集合 $N(\varepsilon)$ 用一列总长度小于 $\varepsilon/2$ 的开区间 $(x_{k-1},x_k)$ 覆盖住了，只是出了一点纰漏。某个（或某些）分点 $\{x_i\}$ 可能落在 $N(\varepsilon)$ 中，而我们忽略了覆盖它。由于这样的点只有有限多个，我们只需在集合中加入少数几个足够短的区间即可。

这样我们就证明了：对任何 $\varepsilon>0$，集合 $N(\varepsilon)$ 总可以被一列总长度小于 $\varepsilon$ 的开区间所覆盖。由此推出 $N(\varepsilon)$ 是零测集。而 $f$ 的不连续点集合正是这些集合 $N(1),N(1/2),N(1/4),N(1/8),\ldots$ 的并集。既然其中每一个都是零测集，由定理 6.34 可知 $f$ 的不连续点集合也是零测集，如所求。

这就证明了定理的一个方向。反方向，假设 $f$ 是有界的，比方说对所有 $x$ 有 $|f(x)|\le M$，并且集合 $E$（即 $[a,b]$ 中 $f$ 不连续的点的集合）是一个零测集。取 $\varepsilon>0$。由定理 8.16，我们需要找出至少一个分划
```math
[x_0,x_1],\;[x_1,x_2],\;\ldots,\;[x_{n-1},x_n]
```
使得所求和小于 $\varepsilon$。

<span style="color:#7f8c8d">书页 354 · §8.6 Theorem 8.17（Riemann-Lebesgue）</span>

区间 $[a,b]$ 的分划要满足
```math
\sum_{k=1}^n \omega_f([x_{k-1},x_k])(x_k-x_{k-1})<\varepsilon.
```
令 $E_1$ 表示 $[a,b]$ 中振幅大于或等于 $\varepsilon/(2(b-a))$ 的点 $x$ 之集合；也就是说，满足
```math
\omega_f(x)\ge\varepsilon/(2(b-a)).
```
这个集合是闭的（closed，见定理 6.27），并且作为 $E$ 的子集，它必为零测集。而零测闭集总可以被有限多个总长度小于
```math
\varepsilon/(4M+1)
```
的小开区间所覆盖。（见定理 6.35。）我们可以假设这些开区间的端点互不相同。注意，在剩余的那些区间中的点上，$f$ 的振幅都小于 $\varepsilon/(2(b-a))$。因此，这些区间可以被细分（subdivided）成更小的区间，使其上振荡至多仍不小于此前假定的值（习题 8.6.6）。

于是我们可以作出区间 $[a,b]$ 的一个分划
```math
[x_0,x_1],\;[x_1,x_2],\;\ldots,\;[x_{n-1},x_n],
```
它由两类闭区间组成：(i) 第一类覆盖了 $E_1$ 的全部点，总长度小于 $\varepsilon/(4M+1)$；(ii) 其余一类不含有 $E_1$ 的任何点，且 $f$ 在其中每个区间上的振幅都小于 $\varepsilon/(2(b-a))$；也就是说，
```math
\omega_f([x_{k-1},x_k])<\varepsilon/(2(b-a)).
```
和式
```math
\sum_{k=1}^n \omega_f([x_{k-1},x_k])(x_k-x_{k-1})
```
按区间属于类型 (i) 还是类型 (ii) 分为两个和。前者至多贡献
```math
(2M)\times\varepsilon/(4M+1)<\varepsilon/2,
```
而后者至多贡献
```math
\varepsilon/(2(b-a))\times(b-a)=\varepsilon/2 .
```
于是总而言之，
```math
\sum_{k=1}^n \omega_f([x_{k-1},x_k])(x_k-x_{k-1})<\varepsilon,
```
证明完毕。$\blacksquare$

**§8.6.4 哪些函数是 Riemann 可积的？（What Functions Are Riemann Integrable？）**

> <span style="color:#7f8c8d;">进阶章节，可略读（Advanced section. May be omitted）。</span>

定理 8.17 精确刻画了 Riemann 可积的到底是哪些函数：它们正是那些"没有太多不连续点"的有界函数这一类别。我们<span style="color:#7f8c8d">书页 355 · §8.6 Corollaries（推论）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）：**</span> 推论 8.18 与 8.19 是定理 8.17 的现成果子：阶梯函数（§5.2.6 提到）只有有限多个不连续点，所以当然可积（8.18）；而任何"不连续点集合至多可数"的有界函数也都可积（8.19）。连接点：可数集 = 能被 1,2,3,… 编号的集合（6.042J 的 countability），而任何可数集都是零测集——想象把它一个点一个点地放进总长任意小的开区间并里，就能理解"可数 ⟹ 测度零"。第一性原理：这解释了为什么"阶跃/采样/量化"这类在数字系统（CSAPP 的 ADC、采样、查找表）里无处不在的硬跳变函数，仍然"面积良好"——关键在不连续点的"量"（至多可数）而非它们的"疏密布局"。推论 8.19 的证明几乎为零行：可数 ⟹ 零测 ⟹ 由 8.17 可积。它立刻让你看到 Dirichlet 函数（不连续点即全体实数，不可数、测度非零）与 Thomae 函数（不连续点即全体有理数，可数个、零测度）在天平两端的本质差别。

---

---

> <span style="color:#1e8449;">**[note] Note（译者注）：**</span> 推论 8.20 说：任一单调函数都 Riemann 可积。它的洞察藏在"单调函数只有至多可数多个不连续点"这个事实里：给每次跳跃的高度设一个下界（比如 δ=1/k），则高度超过 δ 的跳跃点只能有有限个（否则单调有限区间内总跳跃量会无穷大），再让 δ=1,1/2,1/3,… 一层层剥下去并取并，便知全部不连续点至多可数；一旦套用推论 8.19 立得可积。这是理论中"单调性强制整洁"的又一例子，和你用单调栈/单调队列优化算法（算法课常见思想）时"单调性能推出强结构"的直觉完全一致。推论 8.21 则说：若 f 可积则 |f| 也可积——因为 |f| 的不连续点全部来自 f 的不连续点，不可能"制造"新的坏点。这里有个必须警惕的"方向"：|f| 可积推不出 f 可积（习题 8.6.7 与 8.6.11 正是为点出这一点而设），这再次提醒你：可积保的是"点集层面的小"，而更细微的正负号/阶梯差异并不参与判断。合起来看，四个推论（8.18–8.21）展示了同一条定理 8.17 能如何毯式地覆盖"阶跃的""可数个断点的""单调的"以及"取绝对值的"一大族实用函数，这正是"一个深刻刻画 + 现成推论"的方法论样板。历史注：Lebesgue 早在 1901 年关于 Riemann 可积性的刻画中就暗含这些推论，而"单调函数不连续点至多可数"这一结论本身也常归功于他在测度论框架下的整理。

---


应当立即辨认出，一些我们惯常使用的函数类型（types of functions）也是可积的。我们将这些结论表述为上述定理的推论。（回忆阶梯函数（step function）已在 §5.2.6 中定义。）

**推论 8.18 · <span style="color:#2471a3">[corollary]</span> 区间上的每个阶梯函数都是 Riemann 可积的**

> <span style="color:#7f8c8d;">TBB §8.6, p.355</span>

<span style="color:#2471a3">**证明**</span>：一个阶梯函数有界（bounded）且只有有限多个不连续点。因此它的不连续点集具有零测集（measure zero）。由此，该推论由定理 8.17（Theorem 8.17）直接得出。$\blacksquare$

**推论 8.19 · <span style="color:#2471a3">[corollary]</span> 在区间 $[a,b]$ 上仅有至多可数个不连续点的每个有界函数都是 Riemann 可积的**

> <span style="color:#7f8c8d;">TBB §8.6, p.355</span>

<span style="color:#2471a3">**证明**</span>：由于可数集（countable set）具有零测集，该推论由定理 8.17 直接推出。$\blacksquare$

**推论 8.20 · <span style="color:#2471a3">[corollary]</span> 在区间 $[a,b]$ 上单调的每个函数都是 Riemann 可积的**

> <span style="color:#7f8c8d;">TBB §8.6, p.355</span>

<span style="color:#2471a3">**证明**</span>：一个单调函数（monotonic function）有界且只有至多可数个不连续点。因此，该推论由前述推论得出。$\blacksquare$

**推论 8.21 · <span style="color:#2471a3">[corollary]</span> 若函数 $f$ 在区间 $[a,b]$ 上 Riemann 可积，则函数 $|f|$ 在该区间上也是 Riemann 可积的**

> <span style="color:#7f8c8d;">TBB §8.6, p.355</span>

<span style="color:#2471a3">**证明**</span>：该推论由定理 8.17 直接得出，因为若 $f$ 在 $[a,b]$ 上 Riemann 可积，则 $f$ 必有界，并且除一个零测集的集合外在每一点处连续。习题 8.6.7 表明 $|f|$ 具有完全相同的性质。$\blacksquare$

<span style="color:#7f8c8d">书页 356 · §8.6 习题（Exercises，按规范跳过）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）：**</span> §8.7 开头抛出一个极富方法论味道的问题：我们已把积分从连续函数推广到更大的有界函数类，那么第 8.3 节那些基本性质（可加、线性、单调、绝对值）还保得住吗？注意这里回答的方式是"先证新类可积，再沿用旧证明"——几乎所有性质 8.22–8.25 的证明都退化为"用定理 8.17 验证 αf+βg、|f| 可在真类上可积，然后说恒等式证明与连续情形无异"。第一性原理：**推广的对象是"能对哪些函数求积分"，而不可以动摇"积分应有的行为"**。若为求更多函数而把性质弄丢，则理论得不偿失。这种"扩大定义域但保持代数规律（等价于一个同态必须保住运算）"的设计原则，既是你在 Strang 18.065 里看到算子理论的精神，也是后续泛函/测度论里"扩展定理（extension theorem）+ 唯一性"反复出现的架构：先在小函数类（连续）上定规矩，再证明它们能在更大类上稳定地延伸。换言之，好的推广不是"破规则"，而是"找更多的合格对象"。

---

> 历史注释汇总（均已核对）：Cauchy 连续函数积分——1823（*Résumé……calcul infinitésimal*）； Riemann 积分与振幅判据——1854 教授资格论文（《论函数可按三角级数表示》），1868 年刊出， Riemann 卒于 1866；Darboux 上和/下和整理——1875；Thomae 函数（f(p/q)=1/q）——1875；Lebesgue 零测集刻画 Riemann 可积（定理 8.17 之充分性）——1901，系统化于其 1902 博士论文《积分、长度与面积》。


习题区包含 8.6.1–8.6.11，均为围绕上述推论及定理 8.15–8.17 的证明练习，按翻译规范跳过。（其中 8.6.4、8.6.5 以阶梯函数刻画 Riemann 可积，8.6.7 用于推出推论 8.21 的另一证明，8.6.11 断言推论 8.21 的逆命题不成立。）

#### <span style="color:#2471a3">**[section]**</span> <span style="color:#c0392b">8.7 Properties of the Riemann Integral（Riemann 积分的性质）</span>

> <span style="color:#7f8c8d;">*（本节承前页转换而来；本节证明将用到可积性的 Lebesgue 判据。你可跳过证明，只需留意这些性质实质上与第 8.3 节针对 Cauchy 原始积分的情形并无二致。）*</span>

 Riemann 积分是 Cauchy 第一积分的扩展，它把积分的适用范围从连续函数扩大到一个更大的有界函数类——那些有界且除一个小集合（一个零测集）内的点外处处连续的函数。我们已经扩大了"可对其求积分"的函数类。那么，第 8.3 节的关键性质我们是否有所丢失？

这些性质表达的是我们对积分行为的期待；丢失其中任何一条都会令人沮丧。在某些情形它们原封不动地保持成立，在另一些情形则需稍加修改。但我们的目标从来不只是对尽可能多的函数求积分；而是要保存积分的理论，并把这一理论足够广泛地应用于所有必要的场合。若我们丢失了基本性质，那我们就损失太大了。幸运的是， Riemann 积分保留了连续函数积分的一切基本性质。少数几处差异应当仔细留意，尤其要注意其中一些性质不得不重新表述。

#### <span style="color:#2471a3">**[property]**</span> <span style="color:#c0392b">性质 8.22 可加性（Additive Property）</span>

> <span style="color:#7f8c8d;">TBB §8.7, p.356</span>

若 $f$ 在区间 $[a,b]$ 与 $[b,c]$ 上都 Riemann 可积，则 $f$ 在 $[a,c]$ 上 Riemann 可积，且

```math
\int_a^b f(x)\,dx + \int_b^c f(x)\,dx = \int_a^c f(x)\,dx .
```<span style="color:#7f8c8d">书页 357 · §8.7 Riemann 积分性质</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 性质 8.22–8.25 讲的不只是四条孤立的公式——把它们摆在一起，你会发现积分 $I: f\mapsto \int_a^b f$ 是在"函数组成的向量空间"上定义的一个**线性泛函**：它把（可积的）函数当作"无穷维向量"，把积分值当作"标量"，并且对这个映射保持着加法与数乘。这正是你在 Strang《线性代数》里反复见到的那条规则——"线性变换 $L$ 满足 $L(u+v)=Lu+Lv$ 与 $L(cu)=cLu$"。唯一的变化是：输入从有限维向量换成了函数，输出从向量换成了实数。第一性原理是：这些性质不是积分"顺便"有的，而是积分作为一个"面积/累积"工具**应当遵守的行为契约**——TBB 原话是目标在于"保存积分的理论"，而不只是对更多函数求积分。注意 8.24 单调性不是线性性质，它的作用是做**夹逼法**：用较大函数与较小函数的积分把目标夹住。Colding 教授在这里提醒你一个极易踩的坑：$f$ 与 $g$ 的"和的上确界"并不等于"上确界的和"（反例在符号相反时就会出现），要靠不等式而非等式来夹。他接着给出的"$\left|\int f\right|\le\int|f|$ 是极其简单却极其有用的不等式"——这句值得你抄下来，它正是后文反常积分收敛性讨论中无处不在的刃。

---


证明。恒等式（可加性中那条等式的）证明与当初处理连续函数（continuous functions）时并无不同（请核实）。必须验证的是陈述中的第一条断言：我们证明 $f$ 在 $[a,c]$ 上 Riemann 可积（Riemann integrable）。

由定理 8.17（Theorem 8.17）知，若 $f$ 在这两个区间上都 Riemann 可积，则它在二者上都有界（bounded），且每个区间内的不连续点集（set of points of discontinuity）都是零测集（measure zero）。由此推出 $f$ 在 $[a,c]$ 上有界。同时，$f$ 在 $[a,c]$ 中的不连续点集等于 $f$ 在 $[a,b]$ 与 $[b,c]$ 中不连续点集的并集，再加上（可能）点 $b$ 本身。因此 $f$ 在 $[a,c]$ 中的不连续点集同样是零测集。从而由定理 8.17，$f$ Riemann 可积。$\blacksquare$

<span style="color:#2471a3">**[property] 性质 8.23 线性性（Linear Property）**</span>

> <span style="color:#7f8c8d;">TBB §8.7, p.357</span>

若 $f$ 与 $g$ 都在 $[a,b]$ 上 Riemann 可积，则任一线性组合（linear combination）$\alpha f+\beta g$ 亦然，且

```math
\int_a^b [\alpha f(x)+\beta g(x)]\,dx = \alpha\int_a^b f(x)\,dx + \beta\int_a^b g(x)\,dx .
```

<span style="color:#2471a3">**[proof] 证明**</span>

恒等式的证明与当初处理连续函数时并无不同（请核实）。需要验证的是陈述中的第一条断言：我们必须证明 $\alpha f+\beta g$ 在 $[a,b]$ 上 Riemann 可积。

函数 $\alpha f+\beta g$ 的不连续点或是 $f$ 的不连续点，或是 $g$ 的不连续点。若 $f$ 与 $g$ 都 Riemann 可积，则二者都有界，且除一个零测集上的点之外处处连续（continuous）。由此推出 $\alpha f+\beta g$ 有界，且除一个零测集上的点之外处处连续。从而由定理 8.17，$\alpha f+\beta g$ 在 $[a,b]$ 上 Riemann 可积。$\blacksquare$

<span style="color:#2471a3">**[property] 性质 8.24 单调性（Monotone Property）**</span>

> <span style="color:#7f8c8d;">TBB §8.7, p.357</span>

若 $f$ 与 $g$ 都在 $[a,b]$ 上 Riemann 可积，且对所有 $a\le x\le b$ 都有 $f(x)\le g(x)$，则

```math
\int_a^b f(x)\,dx \le \int_a^b g(x)\,dx .
```

<span style="color:#2471a3">**[proof] 证明**</span>

为连续函数所作的那套证明在这里同样适用。$\blacksquare$

<span style="color:#2471a3">**[property] 性质 8.25 绝对值性质（Absolute Property）**</span>

> <span style="color:#7f8c8d;">TBB §8.7, p.357</span>

若 $f$ 在 $[a,b]$ 上 Riemann 可积，则 $|f|$ 亦然，并且

```math
-\int_a^b |f(x)|\,dx \le \int_a^b f(x)\,dx \le \int_a^b |f(x)|\,dx ,
```

或等价地，

```math
\left|\int_a^b f(x)\,dx\right| \le \int_a^b |f(x)|\,dx .
```

<span style="color:#2471a3">**[proof] 证明**</span>

为连续函数所作的那套证明在这里同样适用，因为我们已经在推论 8.21（Corollary 8.21）中证明：若 $f$ 在 $[a,b]$ 上 Riemann 可积，则 $|f|$ 亦然。$\blacksquare$

<span style="color:#7f8c8d">书页 358 · §8.7 Riemann 积分性质</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 两条 FTC 各占一个方向：8.26 说"先积分再求导"回到原函数（$\tfrac{d}{dx}\int_a^x f=f$），8.27 说"先求导再积分"得到端点的净变化（$\int_a^b F'=F(b)-F(a)$）。合起来看，求导算子 $D$ 与积分算子 $\int$ 互为**部分逆**。这与你学过的两组东西严格类比：① 矩阵与其逆，$AA^{-1}=I$ 与 $A^{-1}A=I$；② 函数与其反函数，$f^{-1}\circ f=\mathrm{id}$。但这里藏着第一个不对称：$D\circ\int=\mathrm{id}$ 是完全还原，而 $\int\circ D$ 要**扣掉"积分常数"这个核**才成立——因为 $\int_a^b F'$ 把 $F$ 内部的平移常数消掉了。Colding 教授对此有一句很直觉的话，他说这两条其实不该当成两条各自独立的定理，而是"关于同一个东西的两件事（two things about the same stuff）"——正如 $A$ 可逆与 $A^{-1}$ 存在本就是同一件事。第一性原理的洞察：$\int_a^b F'$ 不是在"相加所有瞬时值"，而是在"累积所有瞬时变化率"，所以总增量恰等于末态减初态——好比一笔流水账，每一刻的微小变动加起来恰好等于期末减去期初。把"常数核"记牢，后面你遇到"不定积分都不唯一、差一个常数"时就不会懵。

---

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 注意 8.26 被悄悄改弱了：只有 $f$ **连续**的点处才保证 $F'(x)=f(x)$；8.27 则硬性前提是"$F'$ 的确 Riemann 可积"。为什么这两个条件如此碍眼？因为"能找一个 $f$ 使 $\int$ 存在"和"能找一个 $F$ 使 $F'=f$"是两个不同的问题——就像离散数学里"给一个度序列、能否唯一重建一个图"并不总是可行；这里"给一个导数、能否唯一还原原函数"也不总成立。第一性原理的张力在于：求导把一个函数的全部几何信息"摊平、打散"成很多个局部斜率，而 Riemann 积分这套"把定义域切成均匀小块求和"的工具，重建能力有限，塞不下所有导数。§9.7 承诺构造一个"处处可微、导数有界，却在任一子区间上都不是 Riemann 可积"的函数——这正是墙角所在：$F'$ 存在且正常，$\int F'$ 却无意义。TBB 提到，正是" Riemann 积分无法积分所有导数"这个失败，被Lebesgue（Lebesgue，1902 年提出新积分）当作他寻找更一般积分理论的动机之一。你在线性代数里的体验完全对应：某算子不满秩时，它的伪逆存在但"不是真逆"—— Riemann 积分之于导数，就像那个不够格的真逆。这条注也为你稍后读 §8.9 的广义 Riemann 积分埋下引线。

---


接下来两个性质 8.26 与 8.27 十分重要。它们展示了求积与求导（differentiation）这两个过程如何互为逆运算。二者合称为 Riemann 积分的微积分基本定理（fundamental theorem of calculus）。不过，你应当注意到这一理论中存在一个弱点。若我们计算 $\int F'$，则不能立即从 8.27 推出

```math
\int_a^b F'(x)\,dx = F(b)-F(a) .
```

我们首先需要检验 $F'$ 是 Riemann 可积的。这未必总是容易。更糟的是，它甚至可能是假的，即使对导数有界（bounded）的情形亦然（见 §9.7 的讨论）。正是 Riemann 积分无法积分所有导数这一失败，被Lebesgue（Lebesgue）宣称是他寻找一种更一般积分理论的动机。

<span style="color:#2471a3">**[property] 性质 8.26 不定积分的微分（Differentiation of the Indefinite Integral）**</span>

> <span style="color:#7f8c8d;">TBB §8.7, p.358</span>

若 $f$ 在 $[a,b]$ 上 Riemann 可积，则函数

```math
F(x) = \int_a^x f(t)\,dt
```

在 $[a,b]$ 上连续，并且在函数 $f$ 连续的每一个点 $x$ 处都有 $F'(x)=f(x)$。

<span style="color:#2471a3">**[proof] 证明**</span>

再说一次，为连续函数所作的那套证明在这里同样适用。但请注意，我们不再试图在每一点 $x$ 处证明 $F'(x)=f(x)$，而只在 $f$ 连续的这些点 $x$ 处证明它。

这个证明留给你去检查，并要求你核实它在这里原样适用。$\blacksquare$

<span style="color:#2471a3">**[property] 性质 8.27 导数的积分（Integral of a Derivative）**</span>

> <span style="color:#7f8c8d;">TBB §8.7, p.358</span>

设函数 $F$ 在 $[a,b]$ 上可微。若同时也确有 $F'$ 在 $[a,b]$ 上 Riemann 可积，则

```math
\int_a^b F'(x)\,dx = F(b)-F(a) .
```

<span style="color:#2471a3">**[proof] 证明**</span>

对连续函数所作的那套证明在这里同样适用。$\blacksquare$


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> $1/\sqrt{x}$ 在 $x\to 0^+$ 时趋于 $+\infty$，所以在 $[0,1]$ 上**无界**，作为普通 Riemann 积分它不存在——即便它除 $0$ 外处处连续。可是"函数无界"并不等于"面积无穷大"。怎样救它？关键的一步是把有问题的那个端点"截掉"再取极限（正则化–极限化，regularization–limit）：先对任意 $\delta>0$ 计算正常积分 $F(\delta)=\int_\delta^1 \tfrac{dx}{\sqrt{x}}=2-2\sqrt{\delta}$，再令 $\delta\to 0^+$，得 $F(\delta)\to 2$，于是把 $\int_0^1\tfrac{dx}{\sqrt{x}}$ 定义为 $2$。第一性原理是："奇异点附近那一小段的累积贡献"要用一列**排除它的有限积分**来逼近，正如无穷级数用部分和的极限来定义。这与你熟悉的二分搜索同构：我们不断把"奇异端点 $0$"附近的带子 $\delta$ 推向 $0$，看总面积是否趋于一个稳定的数。要是换成 $1/x$ 就不同了——$\int_\delta^1 dx/x=-\ln\delta\to+\infty$ 发散。把两者对看，你会得到后面 §8.8 习题里反复出现的 **$p$-测试雏形**：$\int_0^1 dx/x^p$ 在 $p<1$ 收敛、$p\ge1$ 发散（记住 $1/\sqrt{x}$ 即 $x^{-1/2}$，这里 $p=1/2<1$，所以它能救）。这个"端点临界指数"与调和级数在第 3 章给你的体会是镜像关系，值得并排默写。

---

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 反常积分有两类：区间无界（$\int_1^\infty dx/x^2$）与函数无界（上面的 $\int_0^1 dx/\sqrt{x}$）。两者都被同一种手法驯服——**极限化**：前者写作 $\lim_{X\to\infty}\int_1^X$，后者写作 $\lim_{\delta\to0^+}\int_\delta^1$。Colding 教授一语道破它与级数的亲戚关系：他举例时说"这有点像我们处理级数时所做的那样——对无穷多个数求和"，反常积分与之同理，只是把"无穷多个数"换成"无穷区域的面积"。最关键的对照是 $1/x^2$ 与 $1/x$：随着 $X\to\infty$，$\int_1^X dx/x^2=1-1/X\to1$（收敛），而 $\int_1^X dx/x=\ln X\to+\infty$（发散）。两条被积函数在无穷远处都趋于 $0$，可收敛与否天差地别，原因只剩一个——**衰减速度快不快**。Colding 的原话是"$1/x^2$ 相当快速地趋于 $0$（goes really quite fast to 0）"。这正是你第 3 章学级数时"通项趋于 $0$ 只是收敛的必要条件、而非充分条件"的积分版：函数要趋于 $0$ 才有一点希望，但还必须"够快地"趋于 $0$。于是积分的 $p$-测试（$\int_1^\infty dx/x^p$，$p>1$ 收敛）与级数的 $p$-测试（$\sum 1/n^p$，$p>1$ 收敛）永远配对出现，它们是同一个"衰减率决定收敛"哲学的两种方言。

---


本页余下的 §8.7 习题 8.7.7（柯西-施瓦茨不等式（Cauchy-Schwarz inequality）在 Riemann 积分上的推广）、8.7.8（分部积分（integration by parts）的推广）与 8.7.9（微积分基本定理的进一步探讨）均属巩固性练习，正文不复引用，故此处从略。§8.7 至此收束，以下转入 §8.8。

<span style="color:#7f8c8d">书页 359 · §8.8 反常 Riemann 积分（The Improper Riemann Integral）</span>

> <span style="color:#7f8c8d">提高（Enrichment）小节，可略过。</span>

 Riemann 积分（Riemann integral）只适用于有界函数（bounded functions）。那么积分

```math
\int_0^1 \frac{dx}{\sqrt{x}}
```

应当作何理解呢？由于被积函数（integrand）在 $[0,1]$ 上无界，这个积分作为 Riemann 积分并不存在，即便被积函数除一点之外处处连续（continuous）也是如此。

<span style="color:#7f8c8d">书页 360 · §8.8 反常 Riemann 积分</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定义里那句"$\int f$ 与 $\int |f|$ 都收敛才叫绝对收敛"并非新造，而是第 3 章级数绝对/条件收敛概念的精确搬运。直觉是这样区分两者：**绝对收敛** = "符号乱打乱也稳稳收敛"，因为把被积函数拆成正部 $f^+$ 与负部 $f^-$（$f=f^+-f^-$），每一块带绝对值的积分都是有限的，总和与取和的次序无关；**条件收敛**（非绝对收敛）= "剥掉绝对值才勉强收敛"，它靠正负无限地互相抵消撑住，一旦允许重排就可能改变结果。你在级数里已经见识过这一点的凌厉形态——条件收敛级数经恰当重排能得到任意想要的和（Riemann 重排定理， Riemann series theorem），这是绝对收敛级数绝不会有的病态。历史注：对定积分与反常积分的严格极限定义，是由 Cauchy 在 1823 年系统给出的（他之前，积分常被直接理解为"微分求逆的过程"，对 $e^{-1/x^2}$ 这样没有初等反导数的函数就会失效）；"绝对收敛 / 条件收敛"的区分也基本定型于 Cauchy 一派的严格化过程中。这一区别在你和数值计算打交道时无比实在：CSAPP / 18.065 里强调"先加小项、再加大项"以减少浮点舍入误差，本质就是在回避条件收敛的次序敏感——把大数先算，小数那部分会"被淹没"。把"绝对收敛是次序无关的健壮性质、条件收敛是精细的次序依赖"这条，当作你判断一切级数与积分收敛性质的第一反应。

---

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 文本先借"Cauchy 第二方法"把刚才的正则化步骤（$\lim_{\delta\to0^+}\int_\delta^1\tfrac{dx}{\sqrt{x}}=2$）与 Riemann 积分焊接成一个混合积分——这是反常积分（improper integral）的由来：数学史上，正是 Cauchy 在 1823 年把"正常"的定积分通过取极限推广到无界区域与无界函数，反常积分由此诞生。而 §8.9 的广义 Riemann 积分（Henstock–Kurzweil 积分，又称 gauge integral）走得更远：普通 Riemann 分划全局用一个最大步长（一个固定的 $x_i-x_{i-1}<\delta$），广义定义改为给**每一点 $x$ 自己配一个控制函数（gauge）$\delta(x)>0$**，只要求每个小区间 $[x_{i-1},x_i]$ 的候选点 $\xi_i$ 满足 $x_i-x_{i-1}<\delta(\xi_i)$。第一性原理：这是把"均匀网格"换成"**自适应步长**"——哪里函数变化剧烈，那里的 $\delta$ 就取得小；哪里平稳，$\delta$ 就大。它就像 CLRS 里的分治/二分：不在整个区间用一刀切的分辨率，而是按局部特征细化。Cousin 定理（TBB 的引理 4.26）保证"无论给什么样的 $\delta$，δ-fine 分划总存在"，这是这套积分能立住的支点（它在现代表述中等价于 Bolzano–Weierstrass 定理）。历史注：这种能把所有导数都积起来的积分，思想发端于 Denjoy（1912）与 Perron（1914）的复杂构造；1957 年捷克数学家 Jaroslav Kurzweil 给出这个"优雅地贴近 Riemann 原味"的 gauge 定义，英国数学家 Ralph Henstock 在大致同时期（1955–1961 年间）独立发展，故合称 Henstock–Kurzweil 积分，又名广义 Riemann 积分。它就恰好补上了前面的墙角——能积所有导数，连曾经"不可积"的那个有界反例也被收编。你若在数值分析里见过"自适应求积（adaptive quadrature）"，会认出这正是 gauge 思想的工程化身。


对我们而言，几乎别无他法，只能回溯数十年，回到 Cauchy 第二方法（Cauchy's second method）；也就是说，我们计算

```math
\lim_{\delta\to 0^+}F(\delta)=\lim_{\delta\to 0^+}\int_{\delta}^{1}\frac{dx}{\sqrt{x}}=2 .
```

我们现在应当做的，是把 Riemann 积分与 Cauchy 第二方法结合起来，构造一种新的混合积分（hybrid integral）。这通常被称为反常（广义） Riemann 积分（improper Riemann integral）。与先前一样，我们先给出一个只考虑单个无界点（位于区间左端点（left endpoint）处）的定义，并理解这一思想可以推广到任意有限多个这样的点。

<span style="color:#2471a3">**[definition] Definition 8.28**</span>

> <span style="color:#7f8c8d;">TBB §8.8, p.360</span>

设 $f$ 为区间 $(a,b]$ 上的函数，它对每个 $0<\delta<b-a$ 都在 $[a+\delta,b]$ 上 Riemann 可积，并在区间 $(a,a+\delta)$ 内无界。则若下列极限存在，我们定义

```math
\int_a^b f(x)\,dx = \lim_{\delta\to 0^+}\int_{a+\delta}^b f(x)\,dx ,
```

此时称该积分为收敛的（convergent）。若 $\int_a^b f(x)\,dx$ 与 $\int_a^b |f(x)|\,dx$ 这两个积分都收敛，则称该积分绝对收敛（absolutely convergent）。

依同样的方式，我们还可以把 Riemann 积分从有界区间推广到无界区间（unbounded intervals）。积分

```math
\int_1^{\infty}\frac{dx}{x^2}
```

又应如何解释呢？它不能作为 Riemann 积分而存在，因为定义显然被限制在有限区间（finite intervals）上，无法为无穷区间给出便捷的解释。与前述同理，我们利用 Cauchy 第二方法得到

```math
\int_1^{\infty}\frac{dx}{x^2}=\lim_{X\to\infty}\int_1^{X}\frac{dx}{x^2}=\lim_{X\to\infty}\left(1-\frac{1}{X}\right)=1 .
```

下面给出一个只针对形如 $[a,\infty)$ 的无穷区间的正式定义（此定义完整陈述续于书页 361）。情形 $(-\infty,b]$ 与此类似。情形 $(-\infty,+\infty)$ 最好拆成 $(-\infty,a]$ 与 $[a,\infty)$ 两个积分之和，其中每一个都可用这种方式处理。

> <span style="color:#7f8c8d;">*（定义 8.29 的完整陈述与收敛/发散/绝对收敛讨论，见书页 361–362 的 W14 翻译。）*</span><span style="color:#7f8c8d">书页 361 · §8.8/§8.9 反常积分</span>

## §8.8 反常 Riemann 积分（续）

若极限存在，我们便定义 $\int_a^\infty f(x)\,dx$ 为 $\lim_{X\to\infty}\int_a^X f(x)\,dx$；在此情形下称该积分**收敛（convergent）**。

<span style="color:#00838f">**定义 8.29（$[a,\infty)$ 上的 Riemann 反常积分）**</span>

> <span style="color:#7f8c8d;">TBB §8.9, p.362</span>

若极限 $\lim_{X\to\infty}\int_a^X f(x)\,dx$ 存在，则定义 $[a,\infty)$ 上的反常积分并称之收敛；否则称其为发散（divergent）。

若 $\int_a^\infty f(x)\,dx$ 与 $\int_a^\infty |f(x)|\,dx$ 两者均收敛，则称该积分**绝对收敛（absolutely convergent）**。

上述两种定义都把 Riemann 积分推广为更一般的概念。

注意：在任一涉及反常 Riemann 积分的应用中，我们都有义务声明该积分是收敛还是发散，并且常常还需进一步声明它是绝对收敛还是非绝对收敛（nonabsolutely convergent）。

人们或许以为这套理论值得认真掌握，并代表了积分学议题的最终结论。

但到十九世纪末已日益清楚：这套 Riemann 积分理论本身在处理许多应用中出现的**有界函数（bounded functions）**时，是全然不足的。

这里借助 Cauchy 的第二种方法所增加的步骤，本意是处理无界函数，结果也被证明过于严苛。

现代化的积分理论是在二十世纪最初几十年间发展起来的，其方法截然不同，甚至连语言都需要许多改变。

因此，这最后几节的素材在很大程度上只有历史意义：一些数学家声称其仅有历史价值，另一些人则认为学习这些素材是学习更高等内容的良好准备。

## 习题 8.8.1

**例题（习题 8.8.1）**：对怎样的 $p,q$ 取值，下列积分

```math
\int_0^1 \frac{\sin x}{x^p}\,dx \quad\text{与}\quad \int_0^1 \frac{(\sin x)^q}{x^p}\,dx
```

分别是普通 Riemann 积分、收敛的反常 Riemann 积分，抑或发散的反常 Riemann 积分？

## §8.9 微积分基本定理续论

*拓展章节，可略读。*

 Riemann 积分并不能积分所有有界导数，因此该积分下的微积分基本定理呈现出别扭的形式：

```math
\int_a^b F'(x)\,dx = F(b) - F(a)
```

其前提条件是 $F$ 在 $[a,b]$ 上可微，且导数 $F'$ 在该区间上 Riemann 可积。

这段被强调的话颇为遗憾：它意味着我们拥有的理论十分有限，也意味着在实践中，我们在积分一个导数之前，总必须先核实该导数确实可积。

在 §9.7 中我们将展示如何构造一个函数 $F$，它在某区间上处处可微，其导数 $F'$ 有界，却在任一子区间上都不是 Riemann 可积的。

<span style="color:#7f8c8d">书页 362 · §8.9 微积分基本定理续论</span>

让我们换一个角度来审视导数的可积性，看看能否发现究竟哪里出了问题。

我们采取一种完全天真的思路，从导数的定义本身出发。

若 $F'=f$ 处处成立，则在每一点 $\xi$ 处，对每个 $\varepsilon>0$，都存在 $\delta>0$，使得当 $x'\le\xi\le x''$ 且 $0<x''-x'<\delta$ 时，有

```math
|F(x'')-F(x')-f(\xi)(x''-x')| < \varepsilon(x''-x')
```

一个粗心的学生可能会这样论证：可以按下法把 $F(b)-F(a)$ 恢复为 $f$ 的 Riemann 和之极限。

设 $a=x_0<x_1<x_2<\cdots<x_n=b$ 是 $[a,b]$ 的一个分划（partition），并令 $\xi_i\in[x_{i-1},x_i]$。

于是

```math
F(b)-F(a) = \sum_{i=1}^{n}\bigl(F(x_{i-1})-F(x_i)\bigr) = \sum_{i=1}^{n} f(\xi_i)(x_i-x_{i-1}) + R
```

其中

```math
R = \sum_{i=1}^{n}\Bigl(F(x_i)-F(x_{i-1})-f(\xi_i)(x_i-x_{i-1})\Bigr)
```

这样，$F(b)-F(a)$ 就被表示为 $f$ 的一个 Riemann 和再加上某个误差项 $R$。

现在似乎可以这样：只要分划比使得 (6) 可用的 $\delta$ 更细，就有

```math
|R| \le \sum_{i=1}^{n}\Bigl|F(x_i)-F(x_{i-1})-f(\xi_i)(x_i-x_{i-1})\Bigr| < \sum_{i=1}^{n}\varepsilon(x_i-x_{i-1}) = \varepsilon(b-a)
```

这样一来，如果这套推理没有差错，即可推得 $f$ 是 Riemann 可积的，且 $\int_a^b f(t)\,dt=F(b)-F(a)$。

正如我们提到过的，这个结论是错误的，我们把它留作习题 8.9.1，请读者找出其中的谬误。

但我们并非要放弃这段论证，而是可以修改 Riemann 积分的定义，使这套推理成立。

修改后的定义如下。

<span style="color:#00838f">**定义 8.30（广义 Riemann 可积，generalized Riemann integrable）**</span>

> <span style="color:#7f8c8d;">TBB §8.9, p.362</span>

一个函数 $f$ 在 $[a,b]$ 上**广义 Riemann 可积**且取值为 $I$，若对每个 $\varepsilon$，都存在 $[a,b]$ 上的正函数 $\delta$，使得只要 $a=x_0<x_1<x_2<\cdots<x_n=b$ 是 $[a,b]$ 的分划，且 $\xi_i\in[x_{i-1},x_i]$、$0<x_i-x_{i-1}<\delta(\xi_i)$，便成立

```math
\left|\sum_{i=1}^{n} f(\xi_i)(x_i-x_{i-1}) - I\right| < \varepsilon
```

积分 $\int_a^b f(x)\,dx$ 即取作这个存在的数 $I$。

容易检验：若 $f$ 是 Riemann 可积的，则它也是广义 Riemann 可积的，且两个积分值相同。

因此这个新积分是旧积分的推广。<span style="color:#7f8c8d">书页 363 · §8.9/§8.10 挑战题</span>

<span style="color:#7f8c8d">注：定义 8.30（广义 Riemann 积分）已在书页 362 译出，此处不再重复。</span>

（§8.9 收尾，续接定义 8.30）该定义要求知道：对任意这样的正函数 $\delta$，这样的分划确实存在；这一事实由 Cousin 定理（Cousin theorem）（引理 4.26）来保证。

由此定义出的积分是一种 Riemann 型积分（Riemann-type integral），它包含通常的 Riemann 积分，并且能够积分所有的导数。

广义 Riemann 积分在 1950 年代由 R. Henstock 与 J. Kurzweil 彼此独立地发现，这些思想又引出了许多其他的积分理论，它们都以这种积分利用实数轴上的导数几何结构的方式，去利用底空间（underlying space）的几何结构。

我们不再把这些思想进一步展开，而是请你参阅 Pfeffer 或 Gordon 的专著。

**习题 8.9.1** 指出正文中那个粗心学生论证里所犯的错误。

<span style="color:#7f8c8d">本章其余 §8.9 习题（8.9.2–8.9.4）按既定格式规则省略。</span>

**§8.10 第八章挑战题（Challenging Problems for Chapter 8）**

<span style="color:#7f8c8d">挑战题 8.10.1 与 8.10.2 按既定格式规则省略不译。</span>

> <span style="color:#7f8c8d;">[1] W. F. Pfeffer, *The Riemann Approach to Integration: Local Geometric Theory*. Cambridge University Press (1993).</span>

> <span style="color:#7f8c8d;">[2] R. A. Gordon, *The Integrals of Lebesgue, Denjoy, Perron and Henstock*. Graduate Studies in Mathematics, 4, American Mathematical Society (1994).</span>

<span style="color:#7f8c8d">书页 364 · 第八章挑战题与注记</span>

挑战题 8.10.2 按既定格式规则省略不译。

**注记（Notes）**

**226（习题 8.2.1）** 你需要求出 $\displaystyle\sum_{k=1}^{n} k^3$ 的公式。

**227（习题 8.2.9）** 首先务必核实这些选点（associated points）是否合法。再证明这些和中的每一个都取相同的值（想想 telescoping sums，即累次相消之和！）。那么，这些 Riemann 和的极限应该是什么呢？

**228（习题 8.3.10）** 这就是所谓的 Cauchy–Schwarz 不等式（Cauchy-Schwarz inequality），它是习题 3.5.13 中那个不等式对积分的对应形式，可用同样的方式证明，且不涉及积分的任何深刻性质（deep properties of integrals）。

**229（习题 8.4.5）** 它会对所有连续函数收敛。

**230（习题 8.5.2）** 将 $\int_{-\infty}^{\infty} f(x)\,dx$ 定义为 $\int_{-\infty}^{a} f(x)\,dx$ 与 $\int_{a}^{\infty} f(x)\,dx$ 之和，并务必证明这个定义不依赖于 $a$ 的选取。

**231（习题 8.5.10）** 请与习题 3.4.26 比较。同时要注意：它看似需要在左端点处做特殊处理，实则不然。

**232（习题 8.6.1）** 注意这个函数处处不连续，且对每个区间 $[c,d]$ 都有 $\omega_f([c,d])=1$。

**233（习题 8.6.3）** 答案是否定的。若处处有 $|f|>c>0$，则为真；等价地，当 $1/f$ 有界时亦为真。<span style="color:#7f8c8d">书页 365 · 第 8 章 NOTES（习题提示，跳过）</span>

<span style="color:#7f8c8d">书页 366 · 第 9 章 Sequences and Series of Functions（函数序列与级数）</span>

## 第 9 章 函数序列与级数（Sequences and Series of Functions）

[note]<span style="color:#1e8449">注：</span>如果初读时略去了第 3 章关于 series（级数）的内容，那么在尝试本章之前，应当先学习 3.4、3.5 节以及 3.6 节的部分内容。

### 9.1 引言（Introduction）

我们已经看到，作为两个或多个函数之和的函数 $f$ 会与那些函数共同享有某些令人满意的性质。例如，我们对 continuity（连续性）、differentiation（可微性）以及 integration（积分）的研究使我们能够陈述：如果在区间 $I=[a,b]$ 上有 $f=f_1+f_2+\cdots+f_n$，那么

- (1) 若 $f_1,f_2,\ldots,f_n$ 在 $I$ 上连续，则 $f$ 也在 $I$ 上连续。
- (2) 若 $f_1,f_2,\ldots,f_n$ 在 $I$ 上可微，则 $f$ 也在 $I$ 上可微，并且 $f'=f_1'+f_2'+\cdots+f_n'$。
- (3) 若 $f_1,f_2,\ldots,f_n$ 在 $I$ 上可积，则 $f$ 也在 $I$ 上可积，并且

```math
\int_a^b f(x)\,dx=\int_a^b f_1(x)\,dx+\int_a^b f_2(x)\,dx+\cdots+\int_a^b f_n(x)\,dx
```

自然要问：当 $f$ 是一个函数无穷 series（级数）之和时，相应的结论是否依然成立？

```math
f=\sum_{k=0}^\infty f_k
```

如果级数的每一项都是连续的，那么和函数是否也连续？导数能否通过对各项求导后逐项求和得到？积分能否通过对各项积分后逐项求和得到？我们在本章中研究这类问题。

这些问题具有相当大的实际重要性。例如，如果我们被允许自由地取极限、积分和微分，那么下面例子中的所有计算都将成立。<span style="color:#7f8c8d">书页 367 · §9.2 Pointwise Limits（逐点极限）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定义 9.2 的关键不在"收敛"二字，而在"逐点"二字。逐点收敛说的是：你先把 $x$ 锁死（fix $x$），再看数列 $\{f_n(x)\}$ 是否趋近 $f(x)$。Colding 教授在课堂上一上来就把这句话讲透了——"once x is fixed, then this sequence fn of x converges to this"，即"一旦 $x$ 固定，数列 $f_n(x)$ 就收敛到 $f(x)$"。注意这里的 $N$ 是允许**依赖 $x$** 的：对不同的 $x_0$、$x_1$，可能要用不同的 $N$ 才能进入误差带。这跟你以前见过的分治算法里的复杂度分析是同一件事：逐点收敛等于"对每个点单独配一个解"，而我们在 $O(n\log n)$ 之类的记号里说的最坏情况，本质上也要求一个 **不依赖具体输入** 的统一上界——这正是下面一致收敛要做的事。先记住一个量化词结构：逐点是"$\forall x\ \exists N$"，一致是"$\exists N\ \forall x$"，顺序调换，结论天壤之别。这是分析学里最值钱的一个句式差异，值得像背单词一样背下来。

---


### 9.2 逐点极限（Pointwise Limits）

[example]<span style="color:#c0392b">例 9.1：</span>由 geometric series（几何级数）的求和公式，我们知道在区间 $(−1,1)$ 上有

```math
\frac{1}{1+x}=1-x+x^2-x^3+x^4-x^5+\cdots \tag{1}
```

对 (1) 式两端求导，立即得到

```math
\frac{-1}{(1+x)^2}=-1+2x-3x^2+4x^3-5x^4+\cdots
```

反复求导可以得到对所有正整数 $n$ 成立的 $(1+x)^{−n}$ 的公式。另一方面，对 (1) 式两端从 $0$ 到 $t$ 积分又立即得到

```math
\ln(1+t)=t-\frac{1}{2}t^2+\frac{1}{3}t^3-\frac{1}{4}t^4+\frac{1}{5}t^5-\cdots
```

对后者取 $t\to 1$ 时的 limit（极限），便得到交替调和级数（alternating harmonic series）求和的那个引人入胜的公式：

```math
\ln 2=1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\frac{1}{5}-\cdots \blacksquare
```

该例中的结论都是真实且有用的。但是，我们求取这些结论所使用的手段是否合法？如果我们随意使用这类方法，是否会碰到结论错误的场合？

我们先把这些问题用函数序列（sequence of functions）的语言（而非级数的语言）加以表述。这是我们在第 9.2 节中要做的，在那里我们将看到，对我们问题的回答是"未必（not necessarily）"。然后在第 9.3–9.6 节中我们将看到，如果对收敛性要求更多一些，那么对每一个问题，回答都将变成"是（yes）"。

假设 $f_1,f_2,f_3,\ldots$ 是一个函数序列，其中的每个函数都定义在一个公共的定义域 $D$（common domain）上。那么和

```math
f=\sum_{k=0}^\infty f_k
```

或者极限

```math
f=\lim_{n\to\infty} f_n
```

究竟应当是什么意思？

对于序列极限，自然的要求看来是：函数值 $f_n(x)$ 应收敛到函数值 $f(x)$。

[definition]<span style="color:#00838f">定义 9.2：</span>设 $\{f_n\}$ 是一个定义在公共定义域 $D$ 上的函数序列。如果对所有 $x\in D$，$\lim_{n\to\infty} f_n(x)$ 都存在（作为实数），我们就说该序列 $\{f_n\}$ 在 $D$ 上 pointwise（逐点）收敛。该极限通过如下等式在 $D$ 上定义一个函数 $f$：

```math
f(x)=\lim_{n\to\infty} f_n(x)
```

我们记 $\lim_n f_n=f$ 或者 $f_n\to f$。对于无穷和，最简单的想法是用我们对一个数项无穷级数收敛的常见解释，即把有限和的定义推广为部分和序列的极限。

<span style="color:#7f8c8d">书页 368 · §9.1 Pointwise Convergence（逐点收敛）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 例 9.4（$f_n(x)=x^n$）是整个第 9 章的第一个"翻车现场"，务必把它钉进脑子里。每一个 $f_n$ 都在 $[0,1]$ 上连续，但逐点极限 $f$ 在 $x=1$ 处突然跳到 $1$，于是不连续。第一性原理地问：**连续性管的是"一片"点的性质，而逐点收敛只独立地管"一串孤立的点"，中间缺一个把"点连成片"的约束。** 用几何说：逐点收敛保证的是"对每个固定的 $x$，$(x,f_n(x))$ 这串点各自点到地收进 $f(x)$ 的 ε-带"，但它不保证这些点*同时*、*用同一批 $n$* 收进去。当 $x$ 越靠近 $1$，$x^n\to0$ 的速度就越慢（$N$ 随 $x$ 爆涨，书中算出的 $N\ge \ln\varepsilon/\ln x$ 就是证据）。Colding 用中值定理给出了一个更漂亮的判别法：因为每个 $f_n$ 都连续、图像从 $0$ 爬到 $1$，所以每个 $f_n$ 都必经中点 $1/2$——于是存在一个"逃逸点" $x_n$（还随 $n$ 移动）使 $f_n(x_n)=1/2$，而这里是 $f(x_n)=0$，差值恒为 $1/2$，永远压不进 $\varepsilon=1/2$ 的误差带。这个"找逃逸点"的动作，就是接下来判断"不是一致收敛"的万能钥匙。

---


[definition]<span style="color:#00838f">定义 9.3：</span>对 $D$ 中的每个 $x$ 以及每个 $n\in\mathbb{N}$，令

```math
S_n(x)=f_1(x)+\cdots+f_n(x)
```

如果 $\lim_{n\to\infty} S_n(x)$ 存在（作为实数），我们就说级数 $\sum_{k=1}^\infty f_k$ 在 $x$ 处收敛，并把 $\lim_{n\to\infty} S_n(x)$ 记为

```math
\sum_{k=1}^\infty f_k(x)
```

如果该级数对所有 $x\in D$ 都收敛，我们就说该级数在 $D$ 上逐点收敛到由下式定义的函数 $f$：

```math
f(x)=\sum_{k=1}^\infty f_k(x)\;\left(=\lim_{n\to\infty}\sum_{k=1}^n f_k(x)\right)
```

我们希望这类函数无穷和能够表现得像函数的有限和一样（正如我们在第 9.1 节中的三个问题所暗示的）：如果在一个区间 $I=[a,b]$ 上有 $f=\sum_{k=1}^\infty f_k$，那么下面这些是否都成立？

- (1) 若所有 $k\in\mathbb{N}$ 的 $f_k$ 都在 $I$ 上连续，那么 $f$ 是否也在 $I$ 上连续？
- (2) 若所有 $k\in\mathbb{N}$ 的 $f_k$ 都在 $I$ 上可微，那么 $f$ 是否也在 $I$ 上可微，并且

```math
f'(x)=\sum_{k=1}^\infty f'_k(x)?
```

- (3) 若所有 $k\in\mathbb{N}$ 的 $f_k$ 都在 $I$ 上可积，那么 $f$ 是否也在 $I$ 上可积，并且

```math
\int_a^b f(x)\,dx=\sum_{k=1}^\infty \int_a^b f_k(x)\,dx?
```

在 $D$ 是区间 $I=[a,b]$ 的特殊情形下，我们的问题于是变成下面的形式：下列结论是否都成立？

1. 若对所有 $n$，$f_n$ 都在 $I$ 上连续，那么 $f$ 是否在 $I$ 上连续？
2. 若对所有 $n$，$f_n$ 都在 $I$ 上可微，那么 $f$ 是否在 $I$ 上可微；若可微，是否又有 $f'=\lim_n f'_n$？
3. 若对所有 $n$，$f_n$ 都在 $I$ 上可积，那么 $f$ 是否在 $I$ 上可积；若可积，是否又有 $\int_a^b f(x)\,dx=\lim_n \int_a^b f_n(x)\,dx$？

一般说来，这些问题都有否定的回答，下面的三个例子将表明这一点。

[example]<span style="color:#c0392b">例 9.4：（连续函数的极限函数可以不连续）</span>对每个 $n\in\mathbb{N}$ 以及 $x\in[0,1]$，令 $f_n(x)=x^n$。这些函数中的每一个都在 $[0,1]$ 上连续。然而请注意，对每个 $x\in(0,1)$，$\lim_n f_n(x)=0$，但 $\lim_n f_n(1)=1$。这很容易看出来，不过核查一下细节是有教益的，因为稍后我们可以借助这些细节弄清本例中到底出了什么问题。在右端点 $x=1$ 处显然有 $\lim_n f_n(x)=1$。对 $0<x_0<1$ 和 $\varepsilon>0$，取 $N\geq\ln\varepsilon/\ln x_0$。于是有 $(x_0)^N\leq\varepsilon$，从而当 $n\geq N$ 时

```math
|f_n(x_0)-0|=(x_0)^n<(x_0)^N\leq\varepsilon \blacksquare
```<span style="color:#7f8c8d">书页 369 · §9.1 Pointwise Convergence（逐点收敛）</span>

于是逐点极限 $f$ 为 $f(x)=\lim_n f_n(x)$，其中

```math
f(x)=\begin{cases}0 & 0\le x<1\\ 1 & x=1\end{cases}
```

于是连续函数序列 $\{f_n\}$ 的 pointwise limit（逐点极限）$f$ 在 $x=1$ 处是不连续的（discontinuous）。（图 9.1 展示了该序列中若干函数的图像。）

[example]<span style="color:#c0392b">例 9.5</span>（极限的导数不一定等于导数的极限；The derivative of the limit is not the limit of the derivative）
> <span style="color:#7f8c8d;">TBB §9.1, p.369</span>

设 $f_n(x)=x^n/n$。那么 $f_n\to 0$ 于 $[0,1]$ 上。现在 $f_n'(x)=x^{n-1}$，于是根据上一个例子即例 9.4，

```math
\lim_n f_n'(x)=\lim_n x^{n-1}=\begin{cases}0 & 0\le x<1\\ 1 & x=1\end{cases}
```

而极限函数 $f\equiv 0$ 的导数在 $[0,1]$ 上恒等于零。因此在 $x=1$ 处有

```math
\frac{d}{dx}\Bigl(\lim_{n\to\infty} f_n(x)\Bigr)\ \neq\ \lim_{n\to\infty}\Bigl(\frac{d}{dx}f_n(x)\Bigr)
```

[example]<span style="color:#c0392b">例 9.6</span>（极限的积分不一定等于积分的极限；The integral of the limit is not the limit of the integrals）
> <span style="color:#7f8c8d;">TBB §9.1, p.369</span>

在这个例子中，我们考虑一个连续函数序列，其中每个函数在定义域上的积分都相同。对于每个 $n\in\mathbb{N}$，在 $[0,1]$ 上如下定义 $f_n$：$f_n(0)=0$，$f_n(1/(2n))=2n$，$f_n(1/n)=0$，$f_n$ 在 $[0,1/(2n)]$ 上及在 $[1/(2n),1/n]$ 上是线性的，且 $f_n$ 在 $[1/n,1]$ 上为零。（见图 9.2。）

容易验证 $f_n\to 0$ 于 $[0,1]$ 上。现在，对于每个 $n\in\mathbb{N}$，

```math
\int_0^1 f_n(x)\,dx = 1
```

但是

```math
\int_0^1 \Bigl(\lim_n f_n(x)\Bigr)\,dx=\int_0^1 0\,dx=0
```

于是

```math
\lim_n \int_0^1 f_n(x)\,dx\ \neq\ \int_0^1 \Bigl(\lim_n f_n(x)\Bigr)\,dx
```

所以积分的极限不等于极限的积分。

<span style="color:#7f8c8d">书页 370 · §9.1 Pointwise Convergence（逐点收敛）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 例 9.7 用一张 $0/1$ 矩阵干净地展示了"交换极限顺序"会翻车：先对行取极限再对列取极限得 $0$，反过来却得 $1$。这跟你熟悉的**矩阵**有直接联系——把 $\{S_{mn}\}$ 看成一张无穷大的下三角矩阵，行极限和列极限顺序不同，结果就不同。它说明了一个根本事实：**两个可交换的算子凑到一起未必可交换**；"取极限"这个运算是单薄的，不能随随便便挪到积分号、求和号、微分号里外。想想 Strang 那门课里强调的"变换的可交换性"——两个可交换的运算顺序无关，问题的背景常常决定它们能不能换。第 9 章后续的核心工作，全部是在追问同一个问题：**在什么加强的收敛（一致收敛）下，$d/dx$、$\int$、$\sum$ 三个 operator 与 $\lim_{n\to\infty}$ 可以安全地交换位置。** 抓住这条主线，9.1–9.6 的很多定理就都只是这一问的不同答案。

---


图 9.2 展示了例 9.6 中的 $f_n$ 在 $[0,1]$ 上的图像：它在 $[0,1/n]$ 上形成一座高度为 $2n$ 的尖峰（在 $x=1/(2n)$ 处取最大值），并在 $[1/n,1]$ 上取零值。

这些例子表明，就一般情形而言，我们先前三个问题的答案都是否定的。我们将在习题中给出更多说明类似现象的补充例子。

在接下来的几节中，我们将会看到：通过在适当的位置把 pointwise convergence（逐点收敛）替换为一种更强的收敛形式，我们这些问题的答案就会变成肯定的。这一所要讨论的收敛形式被称为 uniform convergence（一致收敛）。

在转而讨论一致收敛之前，若我们希望对问题取得肯定的答案，先来理解我们必须克服的一个困难。设 $\{f_n\}$ 是一个收敛到函数 $f$ 的连续函数序列，那么 $f$ 是否一定连续？$f$ 在点 $x_0$ 处的连续性将意味着

```math
\lim_{x\to x_0}f(x)=f(x_0)
```

而这将要求（下面关于极限运算的交换）

```math
\lim_{x\to x_0}\Bigl(\lim_{n\to\infty} f_n(x)\Bigr)=\lim_{n\to\infty} f_n(x_0)=\lim_{n\to\infty}\Bigl(\lim_{x\to x_0} f_n(x)\Bigr)
```

显然，要验证 $f$ 在 $x_0$ 处的连续性，我们需要用到两种极限运算，并且要确信取极限的顺序是无关紧要的（order of passing to the limits is immaterial）。

你也许还能回忆起这样一些情形：其中涉及两种极限运算，而取极限的顺序并不影响结果。例如，在初等微积分中，人们会找到一些条件，在这些条件下，一个 double integral（二重积分）的值可以通过按任意顺序迭代"单积分"来求得。与之形成对照，我们给出一个 double sequence（二重序列）的例子，在其中取极限的顺序是很重要的。

[example]<span style="color:#c0392b">例 9.7</span>（极限运算交换的失效：二重序列）
> <span style="color:#7f8c8d;">TBB §9.1, p.370</span>

在这个例子中，我们说明交换极限运算（an interchange of limit operations）可能不会给出正确的结果。设

```math
S_{mn}=\begin{cases}0 & m\le n\\ 1 & m>n\end{cases}
```

将 $\{S_{mn}\}$ 视作一个矩阵（matrix），

```math
[S_{mn}]=
\begin{pmatrix}
0 & 0 & 0 & \cdots\\
1 & 0 & 0 & \cdots\\
1 & 1 & 0 & \cdots\\
\vdots & \vdots & \vdots & \ddots
\end{pmatrix}
```

其中我们将元素 $S_{mn}$ 置于第 $m$ 行第 $n$ 列处。对每一行 $m$，有 $\lim_{n\to\infty} S_{mn}=0$，故

```math
\lim_{m\to\infty}\Bigl(\lim_{n\to\infty} S_{mn}\Bigr)=0 .
```

另一方面，对每一列 $n$，有 $\lim_{m\to\infty} S_{mn}=1$，故

```math
\lim_{n\to\infty}\Bigl(\lim_{m\to\infty} S_{mn}\Bigr)=1 .
```
■

### 习题（Exercises）

#### 习题 9.2.1
考察下列函数序列（sequence of functions）
```math
f_n(x)=\frac{x^n}{1+x^n}
```
的逐点极限（pointwise limit）行为。

#### 习题 9.2.2
证明对数函数（logarithm function）可以表示为某个"较简单"函数序列的逐点极限，
```math
\ln x=\lim_{n\to\infty} n\Bigl(\sqrt[n]{x}-1\Bigr)
```
对其定义域内的每一点都成立。若对这一特定的极限，我们那三个问题的答案均是肯定的，那么关于对数函数的连续性（continuity）你能得出什么结论？它的导数（derivative）会是什么？$\int_1^2 \ln x\,dx$ 又会等于多少？

#### 习题 9.2.3
设 $x_1,x_2,\ldots$ 是有理数集 $\mathbb{Q}$ 的一个枚举（enumeration），令
```math
f_n(x)=\begin{cases} 1, & \text{若 } x\in\{x_1,\ldots,x_n\}\\ 0, & \text{否则} \end{cases}
```
并令
```math
f(x)=\begin{cases} 1, & \text{若 } x\in\mathbb{Q}\\ 0, & \text{否则} \end{cases}
```

#### 习题 9.2.4
证明 $f_n\to f$ 在 $[0,1]$ 上逐点收敛，但对一切 $n\in\mathbb{N}$ 有 $\int_0^1 f_n(x)\,dx=0$，而 $f$ 在 $[0,1]$ 上并不可积（integrable）。

#### 习题 9.2.5
设 $f_n(x)=\dfrac{\sin nx}{\sqrt{n}}$。证明 $\lim_n f_n=0$，但 $\lim_n f_n'(0)=\infty$。

#### 习题 9.2.6
例 9.4、例 9.5 与例 9.6 均可被解释为：取极限运算（limit operation）的顺序确实重要。验证这一点。

#### 习题 9.2.7
设 $f_n\to f$ 在区间 $[a,b]$ 上每一点处逐点收敛。我们已经看到，即使每个 $f_n$ 都连续，也推不出 $f$ 连续。下列诸命题中哪些为真？

<span style="color:#7f8c8d">书页 372 · §9.2 习题（续）</span>

##### 9.2.7（a）——（h）
- （a）若每个 $f_n$ 在 $[a,b]$ 上递增（increasing），则 $f$ 也递增。
- （b）若每个 $f_n$ 在 $[a,b]$ 上非递减（nondecreasing），则 $f$ 也非递减。
- （c）若每个 $f_n$ 在 $[a,b]$ 上有界（bounded），则 $f$ 也有界。
- （d）若每个 $f_n$ 在 $[a,b]$ 上处处不连续（everywhere discontinuous），则 $f$ 也处处不连续。
- （e）若每个 $f_n$ 在 $[a,b]$ 上为常值（constant），则 $f$ 也为常值。
- （f）若每个 $f_n$ 在 $[a,b]$ 上为正（positive），则 $f$ 也为正。
- （g）若每个 $f_n$ 在 $[a,b]$ 上为线性（linear），则 $f$ 也为线性。
- （h）若每个 $f_n$ 在 $[a,b]$ 上为凸（convex），则 $f$ 也为凸。

（参看注 242）

图 9.3. 习题 9.2.8 中的构造。

#### 习题 9.2.8
一位粗心的学生[1]曾这样论证道："在我看来，人们能够用一种非常初等的方式构造一条没有切线的曲线。我们把一个正方形（square）的对角线分成 $n$ 等份，并在每一小段上以该小段为底边构造一个等腰直角三角形（right isosceles triangle）。这样我们得到一种精致的小锯齿。现在令 $n=\infty$。这个锯齿变成一条连续曲线，它与对角线相差无穷小量（zero）。但显而易见，它的切线一会儿平行于 $x$ 轴，一会儿平行于 $y$ 轴。"这里的错误是什么？（图 9.3 说明了这一构造。）

（参看注 243）[1]此处这位"粗心的学生"正是伟大的俄罗斯分析学家卢津（N. N. Luzin，1883–1950）。他在一封书信中（该书信重印于《Amer. Math. Monthly》107（2000 年）第 64–82 页）讲述了：在一次关于魏尔斯特拉斯（Weierstrass）连续但处处不可微函数的讲座之后，他如何将这个论证呈给他的教授。

#### 习题 9.2.9
作为"有些性质在取极限时不成立"的又一说明，计算习题 9.2.8（图 9.3）中诸曲线的长度，并与极限曲线（limiting curve）的长度作比较。

#### 习题 9.2.10
若 $f_n\to f$ 在每一个实数处逐点收敛，则证明
```math
\{x : f(x)>\alpha\} = \bigcup_{m=1}^{\infty}\bigcap_{r=1}^{\infty}\bigcup_{n=r}^{\infty}\{x : f_n(x)\ge \alpha + 1/m\}.
```

#### 习题 9.2.11
设 $\{f_n\}$ 是一列实值函数。证明序列的收敛点集 $E$ 可以写成下列形式
```math
E=\bigcap_{k=1}^{\infty}\bigcup_{N=1}^{\infty}\bigcap_{n=N}^{\infty}\bigcap_{m=N}^{\infty}
\Bigl\{x : |f_n(x)-f_m(x)|\le \tfrac1k\Bigr\}.
```<span style="color:#7f8c8d">书页 373 · §9.3 Uniform Convergence（一致收敛）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 一致收敛的定义把逐点收敛里"$N$ 允许依赖 $x$"这个漏洞堵死了：现在要求**同一个 $N$ 对一切 $x\in D$ 都有效**。Colding 的原话是——"And again, the uniformness, it holds for all x. You can use the same capital N for all x."（翻译：再一次强调，一致性是针对所有 $x$ 都成立的；你可以对所有的 $x$ 用同一个大 N。）几何上这就是书里图 9.6 的 **ε-band 带**：以 $f$ 的图像为中线，上下各画宽 $\varepsilon$ 的管道带，一致收敛就是说从某一项 $n\ge N$ 起，**整条曲线 $y=f_n(x)$ 都整段落在管道里**、没有一根刺冒出来。这跟算法里的"最坏情况上界"是同一个直觉：CLRS 第 3 章里你学过的数列收敛，很多是"逐点"（针对单个项），而在这里你要的是"整段一起贴紧"。CSAPP 里估上界时"对整个输入区间找一个统一的界"，本质也是这种"不依赖具体实例"的约束。要判断一致收敛，无需多言，只需问一句：**能不能找到一个不依赖 $x$ 的 $N$？** 答案是否定，就找逃逸点。

---

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这一小段历史被很多读者跳过，但它恰恰是最佳的第一性原理教材。1821 年 Cauchy 在《Cours d'analyse》里断言"连续函数的收敛级数，其和函数仍连续"，并在 1823 年的《Résumé des leçons》里把积分一路逐项搬进级数——因为这些"看起来"都对，他也确实把大量铁一般的事实逼对了。但 Abel 在 1826 年研究二项式级数时（据称在其著名论文的脚注中）发现了反例，直接戳穿了"收敛级数保持连续性"这句过于宽泛的断言。这件事的教训（可与 CSAPP 里"先靠直觉、再被 corner case 打脸"的调试循环类比）：**结论不能宽于它能成立的假设；当反例出现，正确的回应不是放弃结论，而是把前提收紧以求再造一个新概念。** 正是 Weierstrass 从 1841 年起在柏林讲座中系统引入并严格化了"一致收敛"（德文 gleichmäßige Konvergenz，即"处处齐步"的收敛），M-判别法等工具也是由他在讲座体系中给出的，才算给这条断裂处补上了合法的桥。数学史提醒我们：逐点收敛不是"错误的"概念，它只是"不够强"的概念。

---


§9.3 本节继续讨论一致极限（Uniform Limits）。

逐点极限（pointwise limits）不允许我们交换极限运算的顺序。而在许多情形下，一致极限（uniform limits）是允许这样交换的。为了弄清一致极限的定义应当如何表述，让我们回到 Example 9.4 中的序列。那个序列说明了：连续函数（continuous functions）的逐点极限未必是连续的。那里的困难在于

```math
\lim_{x\to 1^-}\lim_{n\to\infty}f_n(x)\neq\lim_{n\to\infty}\lim_{x\to 1^-}f_n(x) .
```

更仔细地考察这里所涉及的极限，就能看出问题出在哪里，并提示我们需要寻找什么条件，才能允许交换极限的顺序。

<span style="color:#c0392b">**[example] Example 9.8**</span>

> <span style="color:#7f8c8d;">TBB §9.3, p.373</span>

再考虑由函数 $f_n(x)=x^n$ 组成的序列 $\{f_n\}$。我们已经看到，$f_n\to 0$ 在 $[0,1)$ 上逐点成立，并且对每个固定的 $x_0\in(0,1)$ 与 $\varepsilon>0$，都有

```math
|x_0|^n<\varepsilon\iff n>\ln\varepsilon/\ln x_0 .
```

现在固定 $\varepsilon$，但让点 $x_0$ 变化。可以看到，当 $x_0$ 相对于 $\varepsilon$ 较小时，$\ln x_0$ 的绝对值比 $\ln\varepsilon$ 大，因此相对较小的 $n$ 就足以满足不等式 $|x_0|^n<\varepsilon$；另一方面，当 $x_0$ 靠近 $1$ 时，$\ln x_0$ 的绝对值很小，于是 $\ln\varepsilon/\ln x_0$ 将很大。事实上，

```math
\lim_{x_0\to 1^-}\frac{\ln\varepsilon}{\ln x_0}=\infty .
```

下面的表格展示了在 $\varepsilon=.1$ 时，$n$ 需要多大才能使 $|x_0^n|<\varepsilon$：当 $x_0$ 取 $.1,.5,.9,.99,.999,.9999$ 时，相应的 $n$ 为 $2,4,22,230,\;2302,\;23025$。

注意，对于 $\varepsilon=.1$，不存在单个 $N$ 使得对 $x_0\in(0,1)$ 的每一个取值以及一切 $n>N$ 都有 $|x_0|^n<\varepsilon$。（图 9.4 说明了这一点。）

$\blacksquare$

一些十九世纪的数学家会这样描述这个例子中收敛速率的变化，说"序列 $\{x^n\}$ 在 $(0,1)$ 上无限缓慢地收敛"。今天我们则会说，这个确实逐点收敛的序列，并不一致收敛（converge uniformly）。我们的定义正是被这样精心表述，以排除无限缓慢收敛这种可能性的出现。

<span style="color:#00838f">**[definition] Definition 9.9**</span>

> <span style="color:#7f8c8d;">TBB §9.3, p.373</span>

设 $\{f_n\}$ 为定义在公共定义域（common domain）$D$ 上的函数序列。若对每个 $\varepsilon>0$，都存在 $N\in\mathbb{N}$，使得对一切 $n\geq N$ 与 $x\in D$，都有

```math
|f_n(x)-f(x)|<\varepsilon ,
```

则称 $\{f_n\}$ 在 $D$ 上收敛一致（converges uniformly to）到函数 $f$。我们写

```math
f_n\to f\ [\text{unif}]\ \text{on }D\quad\text{或}\quad\lim_n f_n=f\ [\text{unif}]\ \text{on }D ,
```

来表示序列 $\{f_n\}$ 在 $D$ 上一致收敛于 $f$。如果定义域 $D$ 由上下文自然明了，我们也可以删去对 $D$ 的显式提及，直接写

```math
f_n\to f\ [\text{unif}]\quad\text{或}\quad\lim_n f_n=f\ [\text{unif}] .
```

<span style="color:#7f8c8d">书页 374 · §9.3 Uniform Convergence（一致收敛）</span>

图 9.4（Figure 9.4）。序列 $\{x^n\}$ 在 $[0,1]$ 上无限缓慢地收敛。图中分别画出了 $n=2,4,22,100$ 的函数 $y=x^n$，并取 $x_0=.1,.5,.9,.99$，$\varepsilon=.1$。

<span style="color:#c0392b">**[example] Example 9.10**</span>

> <span style="color:#7f8c8d;">TBB §9.3, p.374</span>

设 $f_n(x)=x^n$，$D=[0,\eta]$，$0<\eta<1$。我们已经看到，序列 $\{f_n\}$ 在 $(0,1)$（或在 $[0,1]$）上逐点收敛，但不一致收敛。我们也已意识到，困难源于在靠近 $1$ 处收敛非常"缓慢"。但只需 $0<\eta<1$ 为任意固定值，收敛在 $[0,\eta]$ 上就是一致的。

为看清这一点，注意对 $0\leq x_0<\eta$，有 $0\leq (x_0)^n<\eta^n$。设 $\varepsilon>0$。由于 $\lim_n\eta^n=0$，存在 $N$ 使得只要 $n\geq N$，就有 $0<\eta^n<\varepsilon$。于是若 $n\geq N$，我们得到

```math
0\leq x_0^n<\eta^n<\varepsilon ,
```

因此对 $x=\eta$ 有效的同一个 $N$，对一切 $x\in[0,\eta)$ 也都有效。

$\blacksquare$

一致收敛在分析的许多部分都扮演重要角色；尤其，它出现在涉及交换极限运算顺序的这类问题之中，正如我们在 §9.2 中所讨论的那些。这一点在十九世纪早期的数学家中并不显而易见。直到 1823 年，Cauchy 仍相信一个连续函数的收敛级数（convergent series）可以逐项积分（integrate term by term）；同理，Cauchy 还相信连续函数的收敛级数具有连续的和函数（continuous sum）。Abel 在 1826 年给出了一个反例（counterexample）。或许正是 Weierstrass 在十九世纪中叶第一个认识到了一致收敛的重要性。[2]

若 $f_n\to f$ 在 $[0,1]$ 上成立，则由定义容易推出：收敛在 $[0,1]$ 的任意有限子集 $D$ 上都是一致的（习题 9.3.3）。于是，给定任意 $\varepsilon>0$ 与 $[0,1]$ 中任意有限个点 $x_1,x_2,\ldots,x_m$，我们都能找到 $N\in\mathbb{N}$，使得对一切 $n\geq N$ 与一切 $i=1,2,\ldots,m$，都有

```math
|f_n(x_i)-f(x_i)|<\varepsilon .
```

（图 9.5 说明了这一点。）

> <span style="color:#7f8c8d;">[2] 有关一致收敛历史的更多内容，可参见 Thomas Hawkins 那本有趣的历史专著 *Lebesgue's Theory of Integration: Its Origins and Development*, Univ. of Wisconsin Press (Madison, 1970)。</span>

<span style="color:#7f8c8d">书页 375 · §9.3 Uniform Limits（一致极限）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定理 9.12 就是你第 3 章学过的**数列的 Cauchy 判据**在函数上的"身位升级版"：数列 $\{a_n\}$ 收敛当且仅当它把尾巴互相咬紧（$|a_m-a_n|\to0$ 不管 $m,n$ 取多大），不依赖你先知道极限值 $L$。这里一模一样，只是把"咬紧"从单个点推广到**整个定义域上一致地咬紧**——对足够大的 $n,m$，$|f_m(x)-f_n(x)|<\varepsilon$ 对一切 $x$ 同时成立（一致 Cauchy）。它的价值是决定性的：第一章定理 9.22 之前的很多证明，我们**根本不知道极限函数 $f$ 长什么样**，这时无法直接用定义（定义要先写 $|f_n(x)-f(x)|$），只能用 Cauchy 判据这条"不需要目标值"的通道。Colding 讲 M-判别法时把这套两步走演示得很清楚："先证明对每个固定的 x，$S_n(x)$ 是个 Cauchy 数列，于是存在函数 S；再把这个逐点收敛‘升级’成一致收敛"——注意**"先用 Cauchy 制造极限对象、再升级收敛强弱"**是分析中极其标准的套路，往后还会反复出现。这条中转通道比结论本身更值得记。

---


图 9.5（Figure 9.5）：有限集 $\{x_1,x_2,x_3\}$ 上的一致收敛。

图 9.6（Figure 9.6）：整个区间上的一致收敛。

落在点 $x_1,\ldots,x_m$ 上方的这些垂直线段（vertical line segments）都以函数 $f$ 的图像为中心，长度均为 $2\varepsilon$。用简单的几何语言来说，我们可以沿着序列走得足够远，以保证所有函数 $f_n$ 的图像都与这有限多条垂直线段相交。

与此相对，在 $[0,1]$ 上的一致收敛（uniform convergence）则要求：我们能沿序列走得足够远，以保证这些函数的图像在 $[0,1]$ 的每一个点上都穿过这样的垂直线段；也就是说，对足够大的 $n$，$f_n$ 的图像落在以 $f$ 的图像为中心的"$\varepsilon$-带（$\varepsilon$-band）"之内。（见图 9.6。）

§9.3.1 Cauchy 判据（The Cauchy Criterion）

现在假设给定一个定义在区间 $I$ 上的函数序列 $\{f_n\}$，并且我们希望知道它是否在 $I$ 上一致收敛到某个函数。我们并不知道那个极限函数可能是什么。这个问题与我们在研究序列时面对过的数列（sequence of numbers）$\{a_n\}$ 的问题类似。在那里我们看到，$\{a_n\}$ 收敛当且仅当它是一个 Cauchy 序列（Cauchy sequence）。我们可以为函数序列的一致收敛制定一个类似的判据。

<span style="color:#00838f">**[definition] Definition 9.11**</span>

> <span style="color:#7f8c8d;">TBB §9.3, p.375</span>

设 $\{f_n\}$ 是定义在集合 $D$ 上的函数序列。若对每个 $\varepsilon>0$，都存在 $N\in\mathbb{N}$，使得只要 $n\geq N$ 且 $m\geq N$，就有一切 $x\in D$ 满足 $|f_m(x)-f_n(x)|<\varepsilon$，则称该序列在 $D$ 上一致 Cauchy（uniformly Cauchy）。

<span style="color:#2471a3">**[theorem] Theorem 9.12（Cauchy 判据）**</span>

> <span style="color:#7f8c8d;">TBB §9.3, p.375</span>

设 $\{f_n\}$ 是定义在集合 $D$ 上的函数序列。那么存在一个定义在 $D$ 上的函数 $f$，使得 $f_n\to f$ 在 $D$ 上一致收敛，当且仅当 $\{f_n\}$ 是一致 Cauchy 的。

$\blacksquare$

<span style="color:#7f8c8d">书页 376 · §9.3 Uniform Limits（一致极限）</span>

<span style="color:#2471a3">**[proof] 证明**</span>

我们把 Theorem 9.12 的证明留作习题 9.3.15。

$\blacksquare$

<span style="color:#c0392b">**[example] Example 9.13**</span>

> <span style="color:#7f8c8d;">TBB §9.3, p.376</span>

在 Example 9.10 中，我们已经证明序列 $f_n(x)=x^n$ 在任意区间 $[0,\eta]$（$0<\eta<1$）上一致收敛。现在让我们用 Cauchy 判据再把它证明一次。

固定 $n\geq m$ 并计算

```math
\sup_{x\in[0,\eta]}|x^n-x^m|\leq\eta^m .
\tag{3}
```

设 $\varepsilon>0$，并取整数 $N$ 使 $\eta^N<\varepsilon$。等价地，我们要求 $N>\ln\varepsilon/\ln\eta$。于是由 (3) 推出：对一切 $n\geq m\geq N$ 及一切 $x\in[0,\eta]$，都有 $|x^n-x^m|\leq\eta^m<\varepsilon$。

由 Cauchy 判据可得，序列 $f_n(x)=x^n$ 在任意区间 $[0,\eta]$（$0<\eta<1$）上一致收敛。这里相对 Example 9.10 的论证，在计算上并无优势。不过，我们常常并不知道极限函数，因而必须使用 Cauchy 判据而不是定义。

$\blacksquare$

Cauchy 判据也同样可以针对一致收敛级数（uniformly convergent series）来表述。若部分和序列 $\{S_n\}=\{\sum_{k=1}^{n}f_k\}$ 在 $D$ 上一致收敛到函数 $f$，我们就称级数 $\sum_{k=1}^{\infty}f_k$ 在 $D$ 上一致收敛到 $f$。

级数的 Cauchy 判据

<span style="color:#2471a3">**[theorem] Theorem 9.14（Cauchy 判据）**</span>

> <span style="color:#7f8c8d;">TBB §9.3, p.376</span>

设 $\{f_k\}$ 是定义在集合 $D$ 上的函数序列。那么级数 $\sum_{k=1}^{\infty}f_k$ 在 $D$ 上一致收敛到某个函数 $f$，当且仅当对每个 $\varepsilon>0$，都存在整数 $N$，使得对一切 $n\geq m\geq N$ 及一切 $x\in D$，都有

```math
\left|\sum_{j=m}^{n}f_j(x)\right|<\varepsilon .
```

<span style="color:#2471a3">**[proof] 证明**</span>

这直接由 Theorem 9.12 推出。

$\blacksquare$

<span style="color:#c0392b">**[example] Example 9.15**</span>

> <span style="color:#7f8c8d;">TBB §9.3, p.376</span>

让我们证明级数

```math
1+x+x^2+x^3+x^4+\cdots
```

在任意区间 $[0,\eta]$（$0<\eta<1$）上一致收敛。我们的计算可以基于这样一个已知事实：这个级数的和是 $(1-x)^{-1}$。我们本可以从定义直接证明一致收敛。不过，让我们改用 Cauchy 判据。

固定 $n\geq m$ 并计算

```math
\sup_{x\in[0,\eta]}\left|\sum_{j=m}^{n}x^j\right|
\leq\sup_{x\in[0,\eta]}\left|\frac{x^m}{1-x}\right|
\leq\frac{\eta^m}{1-\eta} .
\tag{4}
```

设 $\varepsilon>0$。由于 $\eta^m(1-\eta)^{-1}\to 0$，取 $N$ 使当 $m\geq N$ 时成立 $0<\eta^m(1-\eta)^{-1}<\varepsilon$。于是由 (4)，对一切 $n\geq m\geq N$ 及一切 $x\in[0,\eta]$，都有

```math
\left|\sum_{j=m}^{n}x^j\right|<\varepsilon .
```

由 Cauchy 判据可得，级数 $1+x+x^2+x^3+x^4+\cdots$ 在任意区间 $[0,\eta]$（$0<\eta<1$）上一致收敛。

$\blacksquare$<span style="color:#7f8c8d">书页 377 · §9.3 The Weierstrass M-Test / Abel Theorem</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Weierstrass M-判别法是这一节最常用的"一键工具"，而你其实**早就会它的思想了**。第 3 章你学过比较判别法（dominance）：正项级数 $\sum b_k$ 收敛、且 $|a_k|\le b_k$，则 $\sum a_k$ 收敛。M-判别法就是把这个"被更强对象罩住"的思维整套搬到**函数项级数**上：给每个 $f_k$ 找一个**与 $x$ 无关**的上界常数 $M_k$（$|f_k(x)|\le M_k$），再要求数项级数 $\sum M_k$ 收敛——"把函数的无穷和压到正数级数的收不收敛"上，一票决胜负。这里的关键一步，是你合通了的：$|S_n(x)-S_m(x)|\le M_{m+1}+\cdots+M_n$，右端完全**不含 $x$**，所以只要控制尾部就能一致控制整根曲线（这就是"一致"二字兑现的地方）。这个"用简单可判定的对象去支配复杂对象"的套路，和 Strang 矩阵分解里"把难矩阵分解成好矩阵的乘积"、CSAPP 里"用上界分配保证最坏情况"是同构的。M-判别法是充分非必要——例 9.18 就是提醒：它只会对**绝对且一致**收敛的级数出手，碰到非绝对收敛的（$0<p\le1$ 的 $\sum\sin k\theta/k^p$）它就闭麦了，得换下一节的 Abel 判别法。

---


承接上一页的讨论，当 $m\to\infty$ 时，我们可以选取一个整数 $N$，使得

```math
\eta^{N}(1-\eta)^{-1}<\varepsilon .
```

于是由 (4) 可知，对一切 $n\geq m\geq N$ 与一切 $x\in[0,\eta]$，都有

```math
\|x^m+x^{m+1}+\cdots+x^{n}\|\leq\frac{\eta^{m+1}}{1-\eta}<\eta^{N}(1-\eta)^{-1}<\varepsilon .
```

由此，根据 Cauchy 判据（Cauchy criterion）可知，级数在任意区间 $[0,\eta]$（其中 $0<\eta<1$）上一致收敛（converges uniformly）。注意，尽管该级数在 $(-1,1)$ 上逐点收敛（converges pointwise），它却并不在 $(-1,1)$ 上一致收敛。（见习题 9.3.16。）

$\blacksquare$

**§9.3.2 Weierstrass M-判别法（M-Test）**

要判定一个函数序列是否一致收敛，并不总是容易的。在函数项级数（series of functions）的情形下，有一个简单判别法往往很有用。它无疑将成为你在研究一致收敛时最常用的工具之一。

<span style="color:#2471a3">**[theorem] Theorem 9.16（M-Test）**</span>

> <span style="color:#7f8c8d;">TBB §9.3, p.377</span>

设 $\{f_k\}$ 为定义在集合 $D$ 上的函数序列，设 $\{M_k\}$ 为正常数（positive constants）序列。若

```math
\sum_{k=0}^{\infty}M_k<\infty
```

并且对每个 $x\in D$ 及 $k=0,1,2,\ldots$，都有

```math
|f_k(x)|\leq M_k ,
```

则级数 $\sum_{k=0}^{\infty}f_k$ 在 $D$ 上一致收敛。

<span style="color:#2471a3">**[proof] 证明**</span>

设 $S_n(x)=\sum_{k=0}^{n}f_k(x)$。我们证明 $\{S_n\}$ 在 $D$ 上一致 Cauchy（uniformly Cauchy）。设 $\varepsilon>0$。对 $m<n$，我们有

```math
S_n(x)-S_m(x)=f_{m+1}(x)+\cdots+f_n(x) ,
```

于是

```math
|S_n(x)-S_m(x)|\leq M_{m+1}+\cdots+M_n .
```

由于常数项级数 $\sum_{k=0}^{\infty}M_k$ 依假设收敛，故存在整数 $N$，使得只要 $n>m\geq N$，就有

```math
M_{m+1}+\cdots+M_n<\varepsilon .
```

这意味着对 $n>m\geq N$，对一切 $x\in D$ 都有

```math
|S_n(x)-S_m(x)|<\varepsilon .
```

因此序列 $\{S_n\}$ 在 $D$ 上一致收敛；也就是说，级数 $\sum_{k=0}^{\infty}f_k$ 在 $D$ 上一致收敛。

$\blacksquare$

<span style="color:#c0392b">**[example] Example 9.17**</span>

> <span style="color:#7f8c8d;">TBB §9.3, p.377</span>

再次考虑区间 $[-a,a]$ 上的几何级数（geometric series）$1+x+x^2+\cdots$，其中 $0<a<1$（正如我们在 Example 9.15 中所做的那样）。则对每个 $k=0,1,2,\ldots$ 及 $x\in[-a,a]$，都有 $|x^k|\leq a^k$。由于级数 $\sum_{k=0}^{\infty}a^k$ 收敛，根据 M-判别法，级数 $\sum_{k=0}^{\infty}x^k$ 在 $[-a,a]$ 上一致收敛。

$\blacksquare$

<span style="color:#7f8c8d">书页 378 · §9.3 The Weierstrass M-Test / Abel Theorem</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> M-判别法只啃得动"绝对收敛"的硬骨头，而 Abel 判别法是给"条件（非绝对）收敛且一致"开的另一扇门。它的引擎是一个你其实见过的工具——**分部求和（summation by parts，也叫 Abel 变换）**，本质就是离散的分部积分：$\sum_{k=m}^{n}a_kb_k$ 里，把"振荡项 $a_k$ 的部分和 $\{s_k\}$ 有界"和"单调项 $b_k\to0$"两个信息组合起来，交换求和顺序后整个和式坍缩成头尾几项。这正是 CLRS 第 3 章里处理和式时那套"换求和指标 / 用部分和"的手法。证明的三条腿：① $\{s_N\}$ 对一切 $x$ 有界（$|s_N|\le M$）——对应"振荡受控"；② $b_k$ 一致单调趋于 $0$；③ 由此把误差压到 $\sup_{x}|b_m(x)|$，再次不含 $n$，所以一致成立。注意这里有个容易混的坑：教科书里有两个"Abel"——一个是**本节这个 Abel 判别法**（收敛性测试），另一个是 §9.6 的 **Abel 定理**（幂级数在收敛圆边界上的连续性），都出自 Niels Henrik Abel (1826)，但用途不同，别放到一块。例 9.21 里 $\sum\sin k\theta/k$ 正是 Abel 判别法的标准应用，后面傅里叶分析还会完整回归它。

---


<span style="color:#c0392b">**[example] Example 9.18**</span>

> <span style="color:#7f8c8d;">TBB §9.3, p.378</span>

让我们研究级数

```math
\sum_{k=1}^{\infty}\frac{\sin k\theta}{k^{p}}
```

在 $p>0$ 各取值下的一致收敛性。对该级数各项大小最粗略的估计，只需利用正弦函数（sine）的绝对值永不大于 $1$ 这一事实即可得到。于是对一切 $\theta\in\mathbb{R}$，

```math
\left|\frac{\sin k\theta}{k^{p}}\right|\leq\frac{1}{k^{p}} .
```

由于级数 $\sum_{k=1}^{\infty}1/k^p$ 在 $p>1$ 时收敛，由 M-判别法我们立即得到：只要 $p>1$，我们的级数就对一切实数 $\theta$ 一致（且绝对）收敛。特别地，正如我们将在后续章节看到的，这个级数表示一个连续函数（continuous function），并且可以在任意有界区间上逐项积分（integrate term by term）。

我们在这里似乎特别成功，但更仔细的考察也揭示了这种方法的一个局限。对 $0<p\leq1$，该级数对一切 $\theta$ 取值也是逐点收敛的（可用 Dirichlet 判别法），但它并非绝对收敛（converges nonabsolutely）。M-判别法在这种情形下毫无帮助，因为它只能处理绝对收敛的级数。

$\blacksquare$

鉴于这个例子结尾处的评论，在使用 M-判别法时，最好在结论中指出所考察的级数"在所给集合上绝对且一致收敛"。这也提醒我们：对非绝对收敛级数的一致收敛性，需要采用不同的方法去检验（见下一节）。

**§9.3.3 Abel 判别法（Abel's Test）用于一致收敛**

> <span style="color:#7f8c8d;">" 高级章节，可略过。</span>

M-判别法是检验级数一致收敛性的一种极有用的工具。然而就其本质而言，它显然只适用于绝对收敛的级数。为了寻找一个能适用于某些非绝对收敛级数的更精细的判别法，我们应该回到第 3 章的方法中，去检索那些处理非绝对收敛的判别法。其中有两个——Dirichlet 判别法与 Abel 判别法——可以加以改造，从而给出一致收敛性。十九世纪的一批作者（包括 Abel、Dirichlet、Dedekind 以及 du Bois-Reymond）曾得到若干类似的一致收敛判别法。我们回顾一下：级数 $\sum_{k=1}^{\infty}a_kb_k$ 的 Abel 判别法要求序列 $\{b_k\}$ 收敛且单调，并要求级数 $\sum_{k=1}^{\infty}a_k$ 收敛。Dirichlet 的变形放宽了后一要求，使得 $\sum_{k=1}^{\infty}a_k$ 只需有有界的部分和（bounded partial sums），但对序列 $\{b_k\}$ 要求其单调收敛到零。这里我们在函数项级数

```math
\sum_{k=1}^{\infty}a_k(x)b_k(x)
```

上寻求类似的条件，以得到一致收敛性。下面的定理是其中一种变形；其他的可参见习题。

<span style="color:#2471a3">**[theorem] Theorem 9.19（Abel）**</span>

> <span style="color:#7f8c8d;">TBB §9.3, p.378</span>

设 $\{a_k\}$ 与 $\{b_k\}$ 为定义在集合 $E\subset\mathbb{R}$ 上的函数序列。<span style="color:#7f8c8d">书页 379 · §9.3 Abel 定理 / M-判别法应用</span>

**[theorem] 定理 9.19（续）**
> <span style="color:#7f8c8d;">TBB §9.3, p.379</span>

假设存在一个数 M，使得对一切 $x\in E$ 与一切 $N\in\mathbb{N}$ 都有
```math
-M \le s_N(x) = \sum_{k=1}^{N}a_k(x) \le M
```
再假设函数序列 $\{b_k\}$ 在每个点都单调收敛到零，且这个收敛在 $E$ 上是一致的。则级数
```math
\sum_{k=1}^{\infty}a_k b_k
```
在 $E$ 上一致收敛。

**[proof] 证明**：我们使用应用于此级数的 Cauchy 判别法（Cauchy criterion）来得到一致收敛。我们可以假设 $b_k(x)$ 非负且递减到零。取 $\varepsilon>0$。对足够大的 $n$ 与 $m$ 以及一切 $x\in E$，我们需要估计和式
```math
\left|\sum_{k=m}^{n}a_k(x)b_k(x)\right|
```
由于函数序列 $\{b_k\}$ 在 $E$ 上一致收敛到零，故可找到一个整数 $N$，使得对所有 $k\ge N$ 与所有 $x\in E$ 都有
```math
0 \le b_k(x) \le \frac{\varepsilon}{2M}.
```
估计和式 (5) 的关键，现在是我们早先使用过（见第 3.2 节）的分部求和公式（summation by parts formula）。这不过是初等恒等式
```math
\sum_{k=m}^{n}a_k b_k = \sum_{k=m}^{n}(s_k-s_{k-1})b_k = s_m(b_m-b_{m+1}) + s_{m+1}(b_{m+1}-b_{m+2}) + \cdots + s_{n-1}(b_{n-1}-b_n) + s_n b_n .
```
这为我们提供了
```math
\left|\sum_{k=m}^{n}a_k(x)b_k(x)\right| \le 2M\sup_{x\in E}|b_m(x)| < \varepsilon
```
对所有 $n\ge m\ge N$ 与一切 $x\in E$ 成立，而这正是该级数的 Cauchy 判别法条件，因而证明了本定理。$\blacksquare$

值得指出，在定理的许多应用中，序列 $\{b_k\}$ 可以取为一列常数，此时所要验证的陈述与条件都要简单得多。

**[corollary] 推论 9.20**：设 $\{a_k\}$ 是定义在集合 $E\subset\mathbb{R}$ 上的函数序列。假设存在一个数 $M$，使得对一切 $x\in E$ 与一切整数 $N$ 都有
```math
\left|\sum_{k=1}^{N}a_k(x)\right| \le M
```
再假设实数序列 $\{b_k\}$ 单调收敛到零。则级数
```math
\sum_{k=1}^{\infty}b_k a_k
```
在 $E$ 上一致收敛。

> <span style="color:#7f8c8d;">TBB §9.3, p.379</span>

<span style="color:#7f8c8d">书页 380 · §9.3 Abel 判别法应用（续）</span>

**[proof] 证明**：我们把 $\{b_k\}$ 视作定义在 $E$ 上的常数函数序列，然后应用上面的定理即可。$\blacksquare$

在习题中还有若干定理 9.19 的其他变体，它们的证明类似，应用也类似。

图 9.7 给出的是级数 $\sum_{k=1}^{n}(\sin k\theta)/k$ 在 $[0,2\pi]$ 上的图像，自左上起顺时针依次对应于 $n=1,4,7,10$。

**[example] 例 9.21**：作为定理 9.19 的一个有趣应用，考虑一个源自傅里叶分析（Fourier analysis）的级数：
```math
\sum_{k=1}^{\infty}\frac{\sin k\theta}{k}.
```
借助狄利克雷判别法（Dirichlet's test，见 3.6.13 节）可以证明，该级数对一切 $\theta$ 都收敛。这个级数的一致收敛性问题相当引人入胜。图 9.7 给出了该级数若干部分和的图像。

在 $\theta=0$ 附近的行为最为奇特。显然，倘若我们能避开这个点（更准确地说，若能保持在离这个点一个小距离之外），我们就应当能够得到一致收敛。定理 9.19 将提供证明。我们取 $b_k(\theta)=1/k$ 与 $a_k(\theta)=\sin k\theta$ 来应用该定理。全部所需只是对一切 $n$ 与合适集合中的一切 $\theta$ 得到和式 $\sum_{k=1}^{n}\sin k\theta$ 的估计。设 $0<\eta<\pi/2$，考虑在区间 $[\eta, 2\pi-\eta]$ 上作这一估计。由习题 3.2.11 得到公式
```math
\sin\theta + \sin 2\theta + \sin 3\theta + \sin 4\theta + \cdots + \sin n\theta = \frac{\cos(\theta/2) - \cos\!\big((2n+1)\theta/2\big)}{2\sin(\theta/2)}
```
利用这个公式，我们可以看出
```math
\left|\sum_{k=1}^{n}\sin k\theta\right| \le \frac{1}{\sin(\eta/2)}.
```

> <span style="color:#7f8c8d;">TBB §9.3, p.380</span>

<span style="color:#7f8c8d">书页 381 · §9.3 Uniform Limits（一致极限）收尾 · 习题 9.3.1–9.3.23</span>

§9.3 一致极限（Uniform Limits）本节这一段收尾论证，说明了如何用 Cauchy 判据（Cauchy criterion）证明一个级数在特定集合上不一致收敛。

此刻定理 9.19（Theorem 9.19）立刻表明，级数

```math
\sum_{k=1}^{\infty}\frac{\sin k\theta}{k}
```

在 $[\eta, 2\pi-\eta]$ 上一致收敛（converge uniformly）。

图 9.7（Figure 9.7）以图像方式解释了为何不能指望收敛在 $0$ 的邻近是一致的。这里的一番计算很有启发意义。

为了在 $[0,\pi]$ 上检验 Cauchy 判据，我们需要证明：当 $m,n$ 很大时，和式

```math
\sup_{\theta\in[0,\pi]}\left|\sum_{k=m}^{n}\frac{\sin k\theta}{k}\right|
```

都很小。但事实上，选取指标 $2m$，并考察 $n=2m$ 处的和，可得

```math
\sup_{\theta\in[0,\pi]}\left|\sum_{k=m}^{2m}\frac{\sin k\theta}{k}\right|
\;\ge\;
\sum_{k=m}^{2m}\frac{\sin(k/2m)}{k}
\;\ge\;
\sum_{k=m}^{2m}\frac{\sin(1/2)}{2m}
\;\approx\;
\frac{\sin(1/2)}{2} .
```

（这里的中间不等式派生于：当 $k\geq m$ 时 $k/2m\geq 1/2$，从而 $\sin(k/2m)\geq\sin(1/2)$；又因 $k\leq 2m$，故 $1/k\geq 1/2m$。）这一下界是通过在诸点 $\theta=1/2m$ 处取值而得到的。由于它不会被任意地变小，说明该级数不能在 $[0,\pi]$ 上一致收敛。

$\blacksquare$

<span style="color:#7f8c8d">书页 381–382 · §9.3 习题 9.3.1–9.3.23（本节为纯习题区，现按要求跳过，仅作说明）</span>

以下 §9.3 习题区包含习题 9.3.1–9.3.23，内容如下，均按任务规则直接跳过（习题除非被正文核心论证引用，否则不翻译）：

- **9.3.1–9.3.2**：考察函数列 $f_n(x)=x^n/(1+x^n)$ 与 $f_n(x)=x^2e^{-nx}$（及 $n^2f_n$）的一致极限行为，判断其一致收敛所在的集合。
- **9.3.3**：若 $f_n\to f$ 在有限集 $D$ 上逐点收敛，则收敛是一致的。
- **9.3.4–9.3.6**：分别证/证否——一致收敛在 $E_1$ 与 $E_2$ 上则在并集 $E_1\cup E_2$ 上成立；在每一 $E_k$ 上成立则在并集 $\bigcup_{k=1}^{\infty}E_k$ 上成立；在 $E$ 上成立则在 $E$ 的每一子集上成立。
- **9.3.7–9.3.8**：证/证否——对每个区间 $[a,b]$ 在 $E\cap[a,b]$ 上一致收敛，则在整个 $E$ 上一致收敛；对每个含于 $(c,d)$ 的闭区间 $[a,b]$ 一致收敛，则在 $(c,d)$ 上一致收敛。
- **9.3.9–9.3.10**：若 $\{f_n\}$ 与 $\{g_n\}$ 都在 $D$ 上一致收敛，则 $\{f_n+g_n\}$（及 $\{f_n g_n\}$）亦一致收敛（后者证否）。
- **9.3.11**：证/证否 $f(x+1/n)\to f(x)$ 在 $(-\infty,\infty)$ 上一致（需何强于连续性的条件）。
- **9.3.12–9.3.13**：一致收敛当且仅当 $\lim_{n\to\infty}\sup_{x\in D}|f_n(x)-f(x)|=0$；给出非一致收敛的 $\varepsilon_0$-判别刻画。
- **9.3.14–9.3.15**：用前一判别证明 $f_n(x)=x^n$ 在 $(0,1)$ 上不一致收敛于零；证明定理 9.12。
- **9.3.16–9.3.17**：验证几何级数 $\sum_{k=0}^{\infty}x^k$ 在 $(-1,1)$ 上逐点收敛但非一致收敛；对其逐项求导得到的级数 $\sum_{k=1}^{\infty}kx^{k-1}$ 同理，但它在 $(-1,1)$ 的每个闭区间 $[a,b]$ 上一致收敛。
- **9.3.18**：验证级数 $\sum_{k=1}^{\infty}\frac{\cos kx}{k^2}$ 在 $\mathbb{R}$ 上一致收敛。
- **9.3.19**：研究使 $g\circ f_n$ 在 $E$ 上一致收敛于 $g\circ f$ 时函数 $g$ 所需的条件。
- **9.3.20**：证明级数 $\sum_{k=0}^{\infty}\frac{x^k}{k!}$ 对每个 $b\in[0,1)$ 在 $[0,b]$ 上一致收敛，但在 $[0,1)$ 上不如此。
- **9.3.21**：若 $\sum f_k$ 在 $D$ 上一致收敛，则其项序列 $\{f_k\}$ 在 $D$ 上一致收敛于零。
- **9.3.22**：定义一致有界（uniformly bounded），证明 $[a,b]$ 上一致收敛的连续函数列必一致有界，而逐点收敛则未必如此。
- **9.3.23**：研究使 $\lim_{n\to\infty}f_n(x+1/n)=f(x)$ 可成立所需的条件。

（本页在 §9.3 正文收尾处附带给出了关于 $\sum\sin k\theta/k$ 逐点收敛但不一致收敛的重要论证，已在上方完整翻译；其余全部为上述习题列表，均按规则跳过。）

<span style="color:#7f8c8d">书页 382 · §9.3 习题 9.3.11–9.3.23（全页为习题区，已在上方合并说明，本页无需要翻译的正文）</span><span style="color:#7f8c8d">书页 383 · §9.4 Uniform Convergence and Continuity（一致收敛与连续性）</span>

> 本页前半部分的习题 9.3.24–9.3.31 为 §9.3 一节后续的变式习题（Weierstrass M-test、Theorem 9.19 的不同变形、连续函数序列的一致收敛与序列极限交换等），非本章核心内容，此处省略。正文直接进入 §9.4 的开头。

## 9.4 一致收敛与连续性 Uniform Convergence and Continuity

我们现在可以来回答本章开头提出的那些问题。我们首先从连续性（continuity）入手。我们知道，一列连续函数（continuous functions）的逐点极限（pointwise limit）未必是连续的。我们现在要证明：一列连续函数的一致极限（uniform limit）必定是连续的。

这一看似简单的断言，正是本章乃至整个函数序列理论中最重要的桥梁之一。逐点收敛（pointwise convergence）太弱，它无法把"每个函数的连续性"这一性质传递给极限函数 $f$；而一致收敛（uniform convergence）恰好为本次传递提供了足够的控制。直观上看，一致收敛意味着当 $n$ 足够大时，图像 $y=f_n(x)$ 在实轴上与图像 $y=f(x)$ 的竖向偏离处处都小于 $\varepsilon/3$，因此极限函数 $f$ 的震荡不会超过各个 $f_n$ 的震荡太多。下一页的定理 9.22（Theorem 9.22）将用严格的 $\varepsilon/3$ 论证（argument）把这一直观变成证明。

---

<span style="color:#7f8c8d">书页 384 · §9.4 Continuity and Uniform Convergence（连续性与一致收敛）</span>

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定理 9.22 是整个 §9.4 的"定海神针"，而它的证明只有一招，就是 **$\varepsilon/3$ 三步走**（教科书自己称作 stepping stone，垫脚石）。要证 $f$ 在 $x_0$ 连续，把目标差 $|f(x)-f(x_0)|$ 用三角不等式拆成三段，各自独立清零：① $|f(x)-f_N(x)|$（整个 $I$ 上小——这是**一致**收敛的功劳，正是逐点收敛做不到的那段）；② $|f_N(x)-f_N(x_0)|$（$x$ 靠近 $x_0$ 时小——这是 $f_N$ **连续**的本职）；③ $|f_N(x_0)-f(x_0)|$（单点收敛）。注意一个精妙的次序：**先统一把 $N$ 取死**，让被当作"垫脚石"的那个 $f_N$ 定下来，再用它的连续性去控"局部"。这跟分治算法里"先选一个 pivot、其余全部对齐它"是同一个动作：你把一个无穷麻烦的 $\lim_{n\to\infty}$ 折叠进一个事先挑好的、可控的中间站 $f_N$，剩下就只剩连杆。$\varepsilon/3$ 与自然出现的三角不等式在这里就是依次分给三段，不给证明多添一个字节。定理 9.22 的级数版本同样成立（每项连续、部分和一致收敛 $\Rightarrow$ 和函数连续），这正是 §9.3 里**逐项连续性可交换**的合法保证——它把本章开头例 9.4 那个"翻车"完整地救回来了。

#### <span style="color:#2471a3">**[theorem]**</span> <span style="color:#c0392b">定理 9.22（Theorem 9.22）</span>

> <span style="color:#7f8c8d;">TBB §9.4, p.384</span>

设 $\{f_n\}$ 是定义在区间 $I$ 上的函数序列（sequence of functions），且设 $x_0 \in I$。若序列 $\{f_n\}$ 在 $I$ 上一致收敛于某个函数 $f$，并且每个 $f_n$ 都在 $x_0$ 处连续，那么函数 $f$ 也在 $x_0$ 处连续。特别地，若每个 $f_n$ 都在 $I$ 上连续，那么 $f$ 亦然。

## 证明 <span style="color:#2471a3">［proof 证明］</span>

设 $\varepsilon > 0$。我们必须证明存在 $\delta > 0$，使得当 $x \in I$ 且 $|x - x_0| < \delta$ 时有
$|f(x) - f(x_0)| < \varepsilon$。对每个 $x \in I$，我们都有

```math
f(x) - f(x_0) = (f(x) - f_n(x)) + (f_n(x) - f_n(x_0)) + (f_n(x_0) - f(x_0)),
```

于是，利用三角不等式（triangle inequality），

```math
|f(x) - f(x_0)| \le |f(x) - f_n(x)| + |f_n(x) - f_n(x_0)| + |f_n(x_0) - f(x_0)|. \tag{6}
```

由于 $f_n \to f$ 一致收敛，存在 $N \in \mathbb{N}$，使得对所有的 $x \in I$ 与所有 $n \ge N$，均有

```math
|f_n(x) - f(x)| < \frac{\varepsilon}{3}. \tag{7}
```

我们从不等式 (6) 与 (7) 推得

```math
|f(x) - f(x_0)| < |f_N(x) - f_N(x_0)| + \frac{2}{3}\,\varepsilon. \tag{8}
```

现在我们利用固定下来的函数 $f_N$ 的连续性。我们选取 $\delta > 0$，使得若 $x \in I$ 且 $|x - x_0| < \delta$，则

```math
|f_N(x) - f_N(x_0)| < \frac{\varepsilon}{3}. \tag{9}
```

综合 (8) 与 (9)，对每个满足 $|x - x_0| < \delta$ 的 $x \in I$，我们得到

```math
|f(x) - f(x_0)| < \frac{\varepsilon}{3} + \frac{2}{3}\,\varepsilon = \varepsilon,
```

这正是所要证明的。

$\blacksquare$

**Note（注）** <span style="color:#1e8449">［note 注］</span> 让我们更仔细地审视定理 9.22 的证明。我们首先得到 $N \in \mathbb{N}$，使得函数 $f_N$ 在整个 $I$ 上与 $f$ 充分贴近（偏差在 $\varepsilon/3$ 之内）。这个函数 $f_N$ 充当了验证 $f$ 在 $x_0$ 处连续性的"垫脚石（stepping stone）"。这里一共包含三个小小的"步骤（steps）"：

1. $|f_N(x) - f(x)|$ 很小（对所有 $x \in I$），这归因于一致收敛性。
2. $|f_N(x) - f_N(x_0)|$ 很小（对所有靠近 $x_0$ 的 $x$），这归因于 $f_N$ 的连续性。
3. $|f_N(x_0) - f(x_0)|$ 很小，这是因为 $\{f_n(x_0)\} \to f(x_0)$。

如果我们试图在逐点收敛（pointwise convergence）的假设下模仿这一证明，那么其中第一步就会失效。你或许希望动手完成习题 (Exercise) 9.4.2，来观察这种失效具体发生在何处。

定理 9.22 也可以用级数（series）的语言来表述。回顾一下：若部分和序列（sequence of partial sums）

```math
\{S_n\} = \left\{ \sum_{k=1}^{n} f_k \right\}
```

在集合 $D$ 上一致收敛于 $f$，则称级数 $\sum_{k=1}^{\infty} f_k$ 在 $D$ 上一致收敛于函数 $f$。据此，定理 9.22 告诉我们：若每个通项 $f_k$ 都连续且相应的部分和序列一致收敛，那么极限函数 $f$ 也连续——这正是 §9.3 中逐函数（term-by-term）连续性与极限可交换性的级数版本基础。