<span style="color:#7f8c8d">书页 485 · §12.4 Differentiable Functions（可微函数）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 在第 7 章（part007）你把单变量导数理解成切线斜率：$f'(x_0)$ 让你在 $x_0$ 近旁用直线 $f(x_0)+f'(x_0)h$ 去近似 $f$。现在定义 12.16 是这个直觉唯一正确的推广，但关键差异在于——"导数"不再是一个数，而是一个 **线性函数** $T$：$f(\mathbf{x})-f(\mathbf{x}_0)=T(\mathbf{x}-\mathbf{x}_0)+o(\|\mathbf{x}-\mathbf{x}_0\|)$。凑巧的是，一维恰好是它的退化情形，此时 $T(h)=f'(x_0)\,h$ 仅仅是"乘以一个常数"。这就是本节的**第一性原理**：**可微性 = 局部用线性函数（矩阵）逼近，而余项是比距离更快趋零的高阶小量**。把它接到你的既有根基（Strang《线性代数》/18.065）：线性函数的信息浓缩在一个矩阵——雅可比矩阵里，这里的 $T$ 正是它的预演（§12.8 正式登场）。历史上这是 **Fréchet** 的现代观点（20 世纪初）：微分是赋范空间之间的**有界线性算子**；其"只看一个方向"的弱兄弟 Gâteaux 微分只能给出方向导数，正是反例（例 12.20）暴露出的漏洞。全章证明反复使用同一种策略，建议命名「**线性化逼近法**」：先写出 $\Delta f=$线性主部$+$高阶余项，再驱动余项归零——连续性、方向导数、链式法则全部出自这一招。

---


# §12.4 可微函数（Differentiable Functions）

习题（Exercises）

**习题 12.4.1**　验证函数 $f(x,y)=\sqrt{|xy|}$ 在点 $(0,0)$ 处连续（continuous）。

**习题 12.4.2**　对实数 $h_1,\ldots,h_n$，验证下列不等式成立：
```math
\sqrt{h_1^2+\cdots+h_n^2}\le|h_1|+\cdots+|h_n|\le\sqrt{n}\sqrt{h_1^2+\cdots+h_n^2}.
```
利用这些不等式给出 n 元函数在点 $\mathbf{x}_0$ 处可微的另一个（等价）定义，该定义表明：$f(\mathbf{x})-f(\mathbf{x}_0)$ 在 $\mathbf{x}_0$ 附近可被一线性函数 $T$ 逼近，使得当 $\|\mathbf{x}-\mathbf{x}_0\|_1\to 0$ 时 $|f(\mathbf{x})-T(\mathbf{x})|\to 0$。

**习题 12.4.3**　对 $\mathbf{h}=(h_1,\ldots,h_n)\in\mathbb{R}^n$，记
```math
\|\mathbf{h}\|_1=|h_1|+\cdots+|h_n|,\qquad
\|\mathbf{h}\|_2=\|\mathbf{h}\|=\sqrt{h_1^2+\cdots+h_n^2},\qquad
\|\mathbf{h}\|_\infty=\max(|h_1|,\ldots,|h_n|).
```
证明下列四个条件彼此等价（equivalent）：对一切 $i=1,\ldots,n$ 有 $h_i\to 0$；$\|\mathbf{h}\|_1\to 0$；$\|\mathbf{h}\|_2\to 0$；$\|\mathbf{h}\|_\infty\to 0$。再以 $\|\mathbf{h}\|_\infty$ 取代 $\|\mathbf{h}\|_1$ 或 $\|\mathbf{h}\|_2$，给出可微性的又一定义。（见注释 277）

**习题 12.4.4**　证明函数
```math
f(x,y)=\begin{cases}\dfrac{x^3-xy^2}{x^2+y^2},&\text{若 }(x,y)\neq(0,0),\\[2pt]0,&\text{若 }(x,y)=(0,0),\end{cases}
```
在 $\mathbb{R}^2$ 上连续且具有一阶偏导数（partial derivative），但在 $(0,0)$ 处不可微。

**习题 12.4.5**　有些作者在定义可微性（differentiability）时避免使用偏导数，此时定义 12.16（Definition 12.16）便采取如下形式。

<span style="color:#00838f">**定义（Definition）**</span>

设 $f$ 定义于开集（open set）$D\subset\mathbb{R}^n$ 上，且 $\mathbf{x}=(x_1,\ldots,x_n)\in D$。则称 $f$ 在点 $\mathbf{x}$ 处可微，若存在一线性函数 $L:\mathbb{R}^n\to\mathbb{R}$，使下面的余项 $\varepsilon$ 满足：当如下差值写成
```math
f(x_1+h_1,\ldots,x_n+h_n)-f(x_1,\ldots,x_n)=L(h_1,\ldots,h_n)+\varepsilon\sqrt{h_1^2+\cdots+h_n^2},
```
并约定 $\varepsilon(0)=0$ 时，随着 $\sqrt{h_1^2+\cdots+h_n^2}\to 0$，有 $\varepsilon\to 0$。试证明此定义与定义 12.16 等价。

# 12.4.3 可微性与连续性（Differentiability and Continuity）

现在我们来证明可微函数必是连续的。我们首先考虑 $n=2$ 的情形，这样做是因为证明的要点已经包含在 $n=2$ 这一特殊情形之中，而在 $\mathbb{R}^2$ 中记号更简洁，且与证明相配套的图像更容易直观地把握。

---

<span style="color:#7f8c8d">书页 486 · §12.4 Differentiable Functions（可微函数）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这条"可微则连续"在单变量时你已经背过（可导必连续），现在只是把它重写成多变量版本并给出证明。它的证明几乎不用新思想：可微性给出的余项 $\varepsilon(|h|+|k|)\to 0$ 本身就足以把 $\Delta f$ 压到零，而 $\varepsilon\to 0$ 甚至比连续性所需更强。**第一性原理**：连续性要求"函数值趋近"，可微性要求"函数值减去线性主部后还能被高阶余项控制"——后者是更强的纪律。难点其实在于**反向**：函数可以在某点连续却不连续可导（一维 $|x|$）；而在多维还会更糟（见 p.488 反例），偏导数全存在都未必可微。这就是为什么实分析要用"找反例"来标注概念的边界。策略可命名为「**余项归零法**」：把 $\Delta f$ 拆成"有限量 $\times$ 小量"之积，逐一驱动小量归零（$|f_1||h|+|f_2||k|+|\varepsilon|(|h|+|k|)\to0$）。这和你处理极限的常规套路（夹逼/分解）一脉相承，属一维结论的"套路平移"，不必畏惧。

---


<span style="color:#2471a3">**定理 12.17（Theorem 12.17）**</span>　若 $f$ 在 $(x_0,y_0)$ 处可微，则 $f$ 在 $(x_0,y_0)$ 处连续。

> <span style="color:#7f8c8d;">TBB §12.4, p.486</span>

<span style="color:#2471a3">**证明（Proof）**</span>

需要证明 $\lim_{(h,k)\to(0,0)}f(x_0+h,y_0+k)=f(x_0,y_0)$。

由于 $f$ 在 $(x_0,y_0)$ 处可微，可以写成
```math
f(x_0+h,y_0+k)-f(x_0,y_0)=f_1(x_0,y_0)h+f_2(x_0,y_0)k+\varepsilon(|h|+|k|),
```
其中当 $(h,k)\to(0,0)$ 时 $\varepsilon\to 0$。由三角不等式（triangle inequality）可得
```math
|f(x_0+h,y_0+k)-f(x_0,y_0)|
\le|f_1(x_0,y_0)||h|+|f_2(x_0,y_0)||k|+|\varepsilon|(|h|+|k|).\tag{28}
```
现在 $f_1(x_0,y_0)$ 与 $f_2(x_0,y_0)$ 都是固定常数，因此不等式 (28) 的右端在 $(h,k)\to(0,0)$ 时趋近于 0，于是左端也随之趋近于 0。而这正是 $\lim_{(h,k)\to(0,0)}f(x_0+h,y_0+k)=f(x_0,y_0)$ 这一要求的等价表述。$\blacksquare$

注记（Note）：观察可知，要推出不等式 (28) 的右端在 $(h,k)\to(0,0)$ 时趋近于 0，我们其实只需 $f_1$ 与 $f_2$ 在 $(x_0,y_0)$ 处有限，以及随 $(h,k)\to(0,0)$ 有 $\varepsilon(h,k)(|h|+|k|)\to 0$ 即可。可微性为我们提供的比所需更多，即随 $(h,k)\to(0,0)$ 有 $\varepsilon(h,k)\to 0$。（参见习题 12.4.7。）

到 $\mathbb{R}^n$ 的推广证明本质上完全相同，我们将其留作习题 12.4.6。

习题（Exercises）

**习题 12.4.6**　证明：若 $f$ 在点 $\mathbf{x}\in\mathbb{R}^n$ 的某个邻域（neighborhood）内有定义且在点 $\mathbf{x}$ 处可微，则 $f$ 在点 $\mathbf{x}$ 处连续。

**习题 12.4.7**　给出一个函数 $f:\mathbb{R}^2\to\mathbb{R}$ 的例子，使得
```math
|f(h,k)-f(0,0)|=f_1(0,0)h+f_2(0,0)k+\varepsilon(|h|+|k|),
```
其中随 $(h,k)\to(0,0)$ 有 $\varepsilon(|h|+|k|)\to 0$，但随 $(h,k)\to(0,0)$ 时有 $\varepsilon\not\to 0$。

# 12.4.4 方向导数（Directional Derivatives）

在例 12.15（Example 12.15）中我们看到，函数 $f(x,y)=\sqrt{|xy|}$ 在 $(0,0)$ 处的偏导数均为 0，却并不可微。我们在某一方向上找出了问题所在：该函数在这个方向上没有方向导数（directional derivative）（习题 12.4.11）。接下来我们将看到：可微函数在一切方向上都有方向导数，而且，更进一步地，所有的方向导数都可借助一个简单的公式由偏导数计算出来。<span style="color:#7f8c8d">书页 487 · §12.4 Differentiable Functions（可微函数）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 方向导数回答"沿方向 $\mathbf{u}$ 上升多快"，可微时它退化为一个内积：$D_{\mathbf{u}}f=\nabla f\cdot\mathbf{u}=\|\nabla f\|\cos\theta$。于是整套几何由这个内积给出：梯度 $\nabla f$ 指向**上升最快的方向**，其模长就是最大爬升速率；与等高线（水平集）正交——因为在等高线上 $D_{\mathbf{u}}f=0$ 意味着 $\cos\theta=0$。这正是 Strang 梯度下降（你 18.065 里的最优化方法）的全部依据：**负梯度是局部最速下降方向**，机器学习的每一轮更新都是"往 $- \nabla f$ 挪一小步"。注意这与一维的差异：一维只有一个方向（$\pm1$），梯度只是带符号的斜率；多维才有"选择方向"的自由度，所以方向导数这个概念在一维几乎隐形。记号上，$\nabla$ 是**哈密顿**在四元数体系中引入的向量微分算符原型（后由泰特旋转定型、麦克斯韦推广为"哈密顿算符"），"nabla"这个命名借用古希腊竖琴的形状（1870 年由 W. R. Smith 提议）；同一家谱里 Laplacian $\nabla^2$ 源自 **Laplace** 的引力势理论（1799）。读到此地你不妨脑补一张"等高线 + 最陡爬坡箭头"的图，梯度下降的直觉会立刻和定理 12.19 重合。

---


## 定理 12.18 <span style="color:#2471a3">[theorem]</span>
> <span style="color:#7f8c8d;">TBB §12.4, p.487</span>

设 $f$ 在点 $(x_0,y_0)\in\mathbb{R}^2$ 处可微，并设 $\mathbf{u}=(u_1,u_2)$ 为任意单位向量（unit vector）。则方向导数（directional derivative）$D_{\mathbf{u}}f(x_0,y_0)$ 存在，且

```math
D_{\mathbf{u}}f(x_0,y_0)=f_1(x_0,y_0)u_1+f_2(x_0,y_0)u_2. \tag{29}
```

<span style="color:#2471a3">**证明**</span>。因为 $f$ 在 $(x_0,y_0)$ 处可微，我们可以写出

```math
f(x_0+h,y_0+k)-f(x_0,y_0)=f_1(x_0,y_0)h+f_2(x_0,y_0)k+\varepsilon(|h|+|k|),
```

其中当 $(h,k)\to(0,0)$ 时 $\varepsilon\to0$。于是

```math
f(x_0+tu_1,y_0+tu_2)-f(x_0,y_0)=f_1(x_0,y_0)tu_1+f_2(x_0,y_0)tu_2+\varepsilon(|tu_1|+|tu_2|) \tag{30}
```

且当 $t\to0$ 时 $\varepsilon\to0$。将（30）式两边同时除以 $t$ 并令 $t\to0$，我们得到

```math
\lim_{t\to0}\frac{f(x_0+tu_1,y_0+tu_2)-f(x_0,y_0)}{t}=\lim_{t\to0}\Big(f_1(x_0,y_0)u_1+f_2(x_0,y_0)u_2+\varepsilon(|u_1|+|u_2|)\frac{|t|}{t}\Big).
```

现在 $|u_1|+|u_2|$ 是一个常数，$\frac{|t|}{t}=1$，且当 $t\to0$ 时 $\varepsilon\to0$，因此该极限等于 $f_1(x_0,y_0)u_1+f_2(x_0,y_0)u_2$，如所断言。$\blacksquare$

定理 12.18 对每个正整数 $n$ 的 $\mathbb{R}^n$ 上的函数均成立，其证明类似。我们将这一证明留作习题 12.4.12。

## 梯度 Gradient <span style="color:#00838f">[definition]</span>
> <span style="color:#7f8c8d;">TBB §12.4, p.487</span>

注意，对于可微函数 $f$，恒等式

```math
D_{\mathbf{u}}f(x_0,y_0)=f_1(x_0,y_0)u_1+f_2(x_0,y_0)u_2
```

可以写作

```math
D_{\mathbf{u}}f(x_0,y_0)=(f_1(x_0,y_0),\,f_2(x_0,y_0))\cdot(u_1,u_2).
```

向量 $(f_1,f_2)$ 或 $\big(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y}\big)$（其中偏导数在 $(x_0,y_0)$ 处取值）十分重要，值得给它一个名称。它被称为 $f$ 在 $(x_0,y_0)$ 处的梯度（gradient），记作

```math
\operatorname{grad} f(x_0,y_0)\quad\text{或}\quad \nabla f(x_0,y_0).
```

由余弦定理（law of cosines，或习题 11.2.4）我们可以写出

```math
D_{\mathbf{u}}f(x_0,y_0)=(\nabla f(x_0,y_0))\cdot\mathbf{u}=\|\nabla f(x_0,y_0)\|\,\|\mathbf{u}\|\cos\theta=\|\nabla f(x_0,y_0)\|\cos\theta
```

其中 $\theta$ 是向量 $\nabla f(x_0,y_0)$ 与 $\mathbf{u}$ 之间的夹角。[这里必须有 $\nabla f(x_0,y_0)\neq0$，否则 $\theta$ 未定义。] 于是 $f$ 的最大变化率（maximum rate of change）出现在 $\theta=0$ 对应的方向上（此时 $\cos\theta$ 达到其最大值）。这发生在 $\mathbf{u}$ 与 $\nabla f(x_0,y_0)$ 方向相同之时。$f$ 在该方向上增加的速率大小为 $\|\nabla f(x_0,y_0)\|$。

<span style="color:#7f8c8d">书页 488 · §12.4 Differentiable Functions（可微函数）</span>

参考起见，我们将此陈述为一个定理，针对多变量函数来表达。

## 定理 12.19 <span style="color:#2471a3">[theorem]</span>
> <span style="color:#7f8c8d;">TBB §12.4, p.488</span>

如果 $f:\mathbb{R}^n\to\mathbb{R}$ 是开集（open set）$D$ 上的可微函数，那么在 $D$ 中梯度不为零的每一点 $\mathbf{x}$ 处，$f$ 的最大变化率出现在方向 $\nabla f(\mathbf{x})$ 上，且 $f$ 在该方向上增加的速率大小为 $\|\nabla f(\mathbf{x})\|$。

习题 12.4.17 和 12.4.18 表明，若我们把可微性（differentiability）的假设弱化为仅仅要求偏导数在 $(x_0,y_0)$ 处存在，则前面的讨论就可能失效。

**习题（非必要，略）**。习题 12.4.9–12.4.13 多为常规检验题，按排版约定跳过。此处仅保留被正文引用、且其证明构成定理 12.18 关键延伸的习题：

> **习题 12.4.12**（State and prove the extension of Theorem 12.18 to functions of $n$ variables。）叙述并证明定理 12.18 对 $n$ 变量函数的推广。

## 12.4.5 一个例子 An Example <span style="color:#c0392b">[example]</span>

## 例 12.20 <span style="color:#c0392b">[example]</span>
> <span style="color:#7f8c8d;">TBB §12.4, p.488</span>

我们之前已经看到，一个连续函数可以在某点处具有偏导数（partial derivative）却在该点不可微。更令人瞩目的是，一个连续函数可以在每个方向上都具有方向导数，却仍然不可微。习题 12.4.13 已经展示了一个具有所有方向导数的不连续函数；由于它不连续，因此不可能可微。在本节中，我们将在几何上描述一个具有这些性质的连续函数。我们将要描述的图形应当是有启发性的，而计算分析则会略显繁琐。（见习题 12.4.14。）

我们分阶段构造函数 $f$。首先令 $f(x,0)=x$ 对所有 $x\in\mathbb{R}$ 成立。这将保证 $f_1(0,0)=1$。接着，对 $|y|\ge x^2$，我们定义 $f(x,y)=0$。这将保证在 $(0,0)$ 处所有其他方向导数均为 $0$。

要看清这一点，我们只需注意到，任何过 $(0,0)$ 而不同于 $x$ 轴的直线，都与集合

```math
\{(x,y):|y|\ge x^2\}
```

在一个包含 $(0,0)$ 的线段上相交。# 第 12 章 R^n 上的微分（Differentiation on R^n）· 书页 489-490

<span style="color:#7f8c8d">书页 489 · §12.4 Differentiable Functions（可微函数）</span>

最后，在集合 $\{(x,y):|y|\lt x^{2}\}$ 上，我们以任意能使 $f$ 在 $\mathbb{R}^{2}$ 上连续（continuous）的方式定义 $f$。例如，$f$ 可以在每一条竖直片段上取线性函数（linear），该片段的两个端点分别取自抛物线 $y=x^{2}$ 或 $y=-x^{2}$ 上的点与 $x$ 轴上的点，且在抛物线上取值为 0、在 $x$ 轴上取值为 $x$。图 12.5 对此作了说明。

> <span style="color:#7f8c8d;">TBB §12.4, p.489</span>

例：[example] 于是，$f$ 在所有方向上的方向导数（directional derivative）都为 0，唯独方向
```math
(u_1,u_2)=(1,0)\quad\text{或}\quad (u_1,u_2)=(-1,0)
```
除外。若 $f$ 在 $(0,0)$ 处可微（differentiable），则由定理 12.18，对任意单位向量 $\mathbf{u}=(u_1,u_2)$，应有
```math
D_{\mathbf{u}} f(0,0)=f_1(0,0)u_1+f_2(0,0)u_2=1\cdot u_1+0\cdot u_2=u_1 .
```
但我们已经看到，除非 $u_2=0$，否则 $D_{\mathbf{u}} f(0,0)=0$，因此等式 $D_{\mathbf{u}} f(0,0)=u_1$ 仅当 $u_1=0$ 或 $u_2=0$ 时成立。由于定理 12.18 给出的方向导数并不正确，故 $f$ 在 $(0,0)$ 处不可微。$\blacksquare$

注意：对我们所述的这一函数，除指向 $x$ 轴正方向或负方向的方向（direction）以外，所有方向导数都要求切平面（tangent plane）就是平面 $z=0$。然而位于平面 $y=0$ 内的那条切线（tangent line）并不在这个平面内。总而言之（In short），不存在切平面。另参见习题 12.4.15。

例 12.20 同时也表明：若我们去掉 $f$ 可微这一要求，定理 12.18 便不再成立。在去掉该假设之后，方向导数未必总能由公式 (29) 计算得出。（但参见习题 12.4.15。）

<span style="color:#7f8c8d">书页 490 · §12.4.6 Sufficient Conditions for Differentiability</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 例 12.20 是全章最值得细品的反例：函数沿每个方向看都"淡出"（方向导数几乎全为 0），却仍不可微，因为不存在一张切平面把各方向的斜率"缝"到一起。**第一性原理**：偏导数只测量"沿坐标轴直线的斜率"，是可微性的**必要而非充分**窥探；可微性则要求"从所有方向、沿任意路径逼近时，线性接近都一致有效"。所以"每个偏导都存在"远弱于"一个线性函数能整体逼近"。这与你学的 CSAPP 形成呼应：可微性类似"全局一致的模块契约"，而偏导管无论你怎么逐坐标检验，都可能漏掉坐标轴之外的问题路径。对智能科学而言这条反例很重要——如果你仅凭梯度（各方向导数的封装）判断"局部像个平面"，遇到这种"山谷谷底塌陷"的表面就会误判。**策略名**：「**逐坐标失效，需整体线性**」；判断可微常用配套定理 12.21（有偏导连续即充分），它用中值定理把"局部线性"从阴阳两方向补平——这正是"充分条件"与"必要条件"分工的范例，也预告了后面 §12.6 隐函数定理同样要靠会用的充分条件而非光看偏导。

---


【习题区】习题 12.4.14（例 12.20 的解析表示）未被正文引用，按规则跳过其完整翻译：其构造了一个按 $\{(x,y):|y|\geq x^{2}\}\cup\{y=0\}$ 及两抛物线间区域分段定义的函数，验证其连续且除 $(1,0),(-1,0)$ 外所有方向导数均为 $0$，并说明其偏导数 $f_1,f_2$ 在 $(0,0)$ 处不连续。习题 12.4.15 被正文引用（"see Exercise 12.4.15"），保留英文原题并作最小翻译：

**12.4.15** A careless student states, "The functions in Example 12.20 and Ex. 12.4.14 fail to be differentiable at (0,0) even though all derivatives exist at (0,0) because the tangent lines at (0,0) don't all lie in the same plane, so there is no tangent plane. If all tangent lines at a point exist and do lie in the same plane, then that plane must be the tangent plane." Is the second statement correct? That is, if $f:\mathbb{R}^{2}\to\mathbb{R}$ is continuous on $\mathbb{R}^{2}$ with $f(0,0)=0$ and every directional derivative at $f(0,0)$ is zero, is $f$ differentiable at $(0,0)$ and is the $xy$-plane the tangent plane at $(0,0,0)$? （大意：一位粗心的学生断言，"例 12.20 与例 12.4.14 中的函数即使 $(0,0)$ 处所有导数都存在仍不可微，是因为 $(0,0)$ 处的诸切线并非同处一平面，因而没有切平面。若一点处的所有切线都存在并确实落在同一平面内，则该平面必为切平面。"第二句是否正确？即，若 $f$ 在 $\mathbb{R}^{2}$ 上连续、$f(0,0)=0$ 且 $(0,0)$ 处每个方向导数都为 0，$f$ 是否在 $(0,0)$ 处可微、$xy$-平面是否为 $(0,0,0)$ 处的切平面？可参见注记 280。）

**Sufficient Conditions for Differentiability（可微的充分条件）** 要直接从定义 12.16 证明一个函数可微，并不总是容易的。处理单变量函数时情况也是如此；在那种情形下我们得到了常能简化任务的通用定理。下面我们给出一个定理，它常可用来证明多变量函数的可微性。

定理：[theorem] **定理 12.21**：设 $f$ 在 $(x_0,y_0)$ 的一个邻域 $D$ 内有定义。假设两个偏导数（partial derivative）之一在 $D$ 上有定义且在 $(x_0,y_0)$ 处连续（continuous），另一个偏导至少在 $(x_0,y_0)$ 处有定义（且在该处有限）。则 $f$ 在 $(x_0,y_0)$ 处可微。

> <span style="color:#7f8c8d;">TBB §12.4.6, p.490</span>

证明 [proof]。设有 $f_1$ 在 $(x_0,y_0)$ 处连续（若连续的是 $f_2$，证明类似）。我们希望证明可以写出
```math
f(x_0+h,\,y_0+k)-f(x_0,y_0)=f_1(x_0,y_0)h+f_2(x_0,y_0)k+\varepsilon\,(|h|+|k|),\tag{31}
```
其中当 $(h,k)\to(0,0)$ 时 $\varepsilon\to0$。

我们将把 (31) 式的左边表示成两项之和（sum of two terms）：对其中一项应用中值定理（mean value theorem），并利用 $f_1$ 在 $(x_0,y_0)$ 处的连续性来获得 (31) 式右边第一项的估计；然后仅利用 $f_2$ 在 $(x_0,y_0)$ 处的存在性（existence）来估计第二项。对这些估计加以整理即可得到所希望的结果。

首先，写出
```math
\begin{aligned}
f(x_0+h,\,y_0+k)-f(x_0,y_0)={}&\big[f(x_0+h,\,y_0+k)-f(x_0,y_0+k)\big]\\
&+\big[f(x_0,y_0+k)-f(x_0,y_0)\big].\tag{32}
\end{aligned}
```<span style="color:#7f8c8d">书页 491 · §12.4 Differentiable Functions（可微函数）</span>

> <span style="color:#7f8c8d;">TBB §12.4, p.491 —— 定理 12.21 证明收尾（中值定理法）</span>

**[theorem]** 定理 12.21（续）证明：
> <span style="color:#7f8c8d;">TBB §12.4, p.491</span>

将中值定理（Mean Value Theorem，定理 7.20）应用于第一个括号项，得到位于 $x_0$ 与 $x_0+h$ 之间的一个数 $\bar{x}_0$（MVT 挑出的点），使得
```math
f(x_0+h,y_0+k)-f(x_0,y_0+k)=f_1(\bar{x}_0,y_0+k)\,h . \tag{33}
```
由于 $f_1$ 在 $(x_0,y_0)$ 处连续（continuous），故有
```math
\lim_{\bar{x}_0\to x_0,\;k\to 0} f_1(\bar{x}_0,y_0+k)=f_1(x_0,y_0).
```
于是我们可以写作
```math
f_1(\bar{x}_0,y_0+k)=f_1(x_0,y_0)+\varepsilon_1 , \tag{34}
```
其中当 $\bar{x}_0\to x_0$ 且 $k\to 0$ 时 $\varepsilon_1\to 0$。注意：由于 $\bar{x}_0$ 位于 $x_0$ 与 $x_0+h$ 之间，故当 $h\to 0$ 时确有 $\bar{x}_0\to x_0$。

现在考察第二个括号项。由于 $f_2$ 在 $(x_0,y_0)$ 处有限，当 $k\neq 0$ 时可写
```math
\frac{f(x_0,y_0+k)-f(x_0,y_0)}{k}=f_2(x_0,y_0)+\varepsilon_2 ,
```
其中当 $k\to 0$ 时 $\varepsilon_2\to 0$。这又可写成
```math
f(x_0,y_0+k)-f(x_0,y_0)=f_2(x_0,y_0)\,k+\varepsilon_2 k . \tag{35}
```
将 $(33)$ 与 $(35)$ 代入 $(32)$，再应用 $(34)$，便得到等式
```math
f(x_0+h,y_0+k)-f(x_0,y_0)=f_1(x_0,y_0)\,h+f_2(x_0,y_0)\,k+(\varepsilon_1 h+\varepsilon_2 k), \tag{36}
```
其中当 $(h,k)\to(0,0)$ 时 $\varepsilon_1$ 与 $\varepsilon_2$ 均趋于 $0$。

将 $(36)$ 与所求形式 $(31)$ 比较，可见我们需要把量 $(\varepsilon_1 h+\varepsilon_2 k)$ 替换成 $\varepsilon(|h|+|k|)$ 这种形式。令
```math
\varepsilon=\frac{\varepsilon_1 h+\varepsilon_2 k}{|h|+|k|}
```
即可胜任。事实上，取此 $\varepsilon$ 值时成立 $\varepsilon_1 h+\varepsilon_2 k=\varepsilon(|h|+|k|)$，故 $(36)$ 化简为 $(31)$。此外，当 $(h,k)\to(0,0)$ 时 $\varepsilon\to 0$。为看出这一点，注意
```math
|\varepsilon|=\left|\frac{\varepsilon_1 h}{|h|+|k|}+\frac{\varepsilon_2 k}{|h|+|k|}\right|
\le \left|\frac{\varepsilon_1 h}{|h|+|k|}\right|+\left|\frac{\varepsilon_2 k}{|h|+|k|}\right|
\le |\varepsilon_1|+|\varepsilon_2| .
```
因为当 $(h,k)\to(0,0)$ 时 $\varepsilon_1\to 0$ 且 $\varepsilon_2\to 0$，所以 $\varepsilon\to 0$。 $\blacksquare$

定理 12.21 的条件通常容易满足，并且往往比直接从定义出发验证可微性（differentiability）更为简便。与前述情况相同，$n$ 元函数的一般情形成立，可通过类似的证明得到（习题 12.4.16）。

（本页下方为习题区，按规范跳过 12.4.16/12.4.17/12.4.18。）

<span style="color:#7f8c8d">书页 492 · §12.4.7 The Differential（全微分）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 从高中起你就习惯写 $df = f'\,dx$，但可别把 $dx,dy$ 当成"无穷小"。本文正式把它们看作 **四个独立变量**：$df=df(x,y,dx,dy)$——即 df 是一个"输入扰动 $(dx,dy)$、输出线性主部"的机器，这正是把可微性定义里的线性函数 $T$ 命名成独立的数学对象。**第一性原理**：微分不是"增量本身"，而是"对增量响应的最佳线性规则"；$df$ 这个记号的价值在于它能提示公式（如 $d(uv)=u\,dv+v\,du$），也提醒你一阶近似的误差级别。例 12.23 是很好的数值检验：$df=0.33$ 以 $0.0046$ 的误差逼近 $\Delta f=0.3346$，误差量级与 $|dx|+|dy|=0.02$ 同阶——这正是"余项是二阶小量"的翻译。把这条和 §1 一维泰勒/数值微分衔接：任何近似估计（比如 CSAPP 里浮点误差分析）都可以看作"保留一阶主部、丢弃高阶余项"。历史上 $dx$ 记号出自 **莱布尼茨**（1675 年手稿），他当时确实把它当无穷小；偏微分符号 $\partial$ 由 Legendre（1786）确立。现代把 $df$ 重铸为"导数处的线性映射"的正是 Fréchet 观点，这里第一次让你看到它的坐标长相。

---


> <span style="color:#7f8c8d;">TBB §12.4, p.492 —— 全微分 $df$ 的引入</span>

设函数 $f$ 在点 $(x_0,y_0)\in\mathbb{R}^2$ 处可微。则可写
```math
f(x_0+h,y_0+k)-f(x_0,y_0)=f_1(x_0,y_0)\,h+f_2(x_0,y_0)\,k+\varepsilon(|h|+|k|) , \tag{37}
```
其中当 $(h,k)\to(0,0)$ 时 $\varepsilon\to 0$。

让我们把上式改写成初等微积分中可能更为熟悉的形式。设 $z=f(x,y)$，记 $\Delta x=h$、$\Delta y=k$，令 $\Delta f=\Delta z$。于是 $\Delta f=\Delta z=f(x_0+\Delta x,\ y_0+\Delta y)-f(x_0,y_0)$
表示的正是与 $x$、$y$ 分别改变 $\Delta x$、$\Delta y$ 相对应的 $f$（即 $z$）的增量（increment），即 $f$（亦即 $z$）的变化量。采用这一记号后，$(37)$ 变为
```math
\Delta f=f_1(x_0,y_0)\,\Delta x+f_2(x_0,y_0)\,\Delta y+\varepsilon(|\Delta x|+|\Delta y|) . \tag{38}
```
项 $\varepsilon(|\Delta x|+|\Delta y|)$ 表示用 $(x_0,y_0)$ 处切平面（tangent plane）分别对应于 $\Delta x$、$\Delta y$ 的变化量去估计 $z$ 的变化量 $\Delta z$ 时所产生的误差。历史上，当明显地涉及极限时，惯常会使用如下一类记号：
```math
df=f_1\,dx+f_2\,dy \quad\text{或}\quad dz=\frac{\partial z}{\partial x}\,dx+\frac{\partial z}{\partial y}\,dy .
```
我们该如何理解这类记号？精确地说，$df$ 是依赖 $x,y,dx,dy$ 的函数：$df=df(x,y,dx,dy)$。
（于是 $x,y,dx,dy$ 是独立变量，而 $df$ 是这四个变量的函数。）这个函数 $df$ 足够重要，理应获得一个专门名称。

**[definition]** 定义 12.22：设 $f$ 在点 $(x,y)$ 处可微。由下式 $df(x,y,dx,dy)=f_1(x,y)\,dx+f_2(x,y)\,dy$
所定义的函数 $df$ 称为 $f$ 在 $(x,y)$ 处的全微分（total differential / differential）。
> <span style="color:#7f8c8d;">TBB §12.4, p.492</span><span style="color:#7f8c8d">书页 493 · §12.4 Differentiable Functions（可微函数）</span>

我们来看一个简单例子以说明上述概念。

**例 12.23** [example]:
> <span style="color:#7f8c8d;">TBB §12.4, p.493</span>

设 $f(x,y)=x^2 y^3$，$x=3$，$y=1$，$\Delta x=\Delta y=0.01$。我们将计算 $\Delta f$ 以及 $\Delta f$ 的近似值 $df$。这里 $x+\Delta x=3.01$，$y+\Delta y=1.01$，故

```math
\Delta f = f(3.01,1.01)-f(3,1)=9.3346-9=0.3346
```

（保留四位小数）。我们的近似值 $df(3,1,0.01,0.01)$ 为

```math
df = f_1(3,1)\,dx + f_2(3,1)\,dy = (6\times 0.01)+(27\times 0.01)=0.33 .
```

于是用微分 $df$ 来估计真实变化量 $\Delta f$ 时，误差仅为约 $0.0046$。注意，此误差与 $|\Delta x|+|\Delta y|=0.02$ 相比是小的。 $\blacksquare$

多变量函数：当涉及两个以上变量时，情形是类似的。

**定义 12.24** [definition]:
> <span style="color:#7f8c8d;">TBB §12.4, p.493</span>

设 $f$ 在 $\mathbf{x}=(x_1,\ldots,x_n)\in\mathbb{R}^n$ 处可微。$f$ 在 $\mathbf{x}$ 处的微分是如下关于 $2n$ 个变量的函数：

```math
df(x_1,\ldots,x_n,h_1,\ldots,h_n) = f_1 h_1 + \cdots + f_n h_n .  \tag{39}
```

与前面一样，有时把 (39) 写成如下形式更为方便：

```math
df = \frac{\partial f}{\partial x_1}\,dx_1 + \cdots + \frac{\partial f}{\partial x_n}\,dx_n .  \tag{40}
```

正如处理导数时多种替换记号常见的现象，记号 (40) 能提示出各种公式。例如，若 $u$ 与 $v$ 均在 $\mathbb{R}^n$ 中的某点 $\mathbf{x}$ 处可微，则

```math
d(u+v)=du+dv,\qquad d(uv)=u\,dv + v\,du ,  \tag{41}
```
```math
d\left(\frac{u}{v}\right) = \frac{v\,du - u\,dv}{v^2}\qquad (v \neq 0).
```

例如，为检验乘积公式，注意根据定义，每个微分都可以写成

```math
du=\frac{\partial u}{\partial x_1}\,dx_1 + \cdots + \frac{\partial u}{\partial x_n}\,dx_n,
```
```math
dv=\frac{\partial v}{\partial x_1}\,dx_1 + \cdots + \frac{\partial v}{\partial x_n}\,dx_n,
```
```math
d(uv)=\frac{\partial(uv)}{\partial x_1}\,dx_1 + \cdots + \frac{\partial(uv)}{\partial x_n}\,dx_n .  \tag{42}
```

但乘积法则对偏导数显然是成立的。因此 (42) 变为

```math
d(uv)=\left(u\frac{\partial v}{\partial x_1}+v\frac{\partial u}{\partial x_1}\right)dx_1+\cdots+\left(u\frac{\partial v}{\partial x_n}+v\frac{\partial u}{\partial x_n}\right)dx_n
```
```math
= u\left(\frac{\partial v}{\partial x_1}\,dx_1+\cdots+\frac{\partial v}{\partial x_n}\,dx_n\right)+v\left(\frac{\partial u}{\partial x_1}\,dx_1+\cdots+\frac{\partial u}{\partial x_n}\,dx_n\right)
```
```math
= u\,dv + v\,du .
```

类似地，基本初等函数的微分正如我们所预期的那样，下面的例子便说明了这一点。

<span style="color:#7f8c8d">书页 494 · §12.4 Differentiable Functions（可微函数）</span>

**例 12.25** [example]:
> <span style="color:#7f8c8d;">TBB §12.4, p.494</span>

若 $u:\mathbb{R}^n\to\mathbb{R}$ 可微，并且我们暂且允许假定 $e^u$ 也可微，则

```math
d(e^u)=\frac{\partial e^u}{\partial x_1}\,dx_1 + \cdots + \frac{\partial e^u}{\partial x_n}\,dx_n
```
```math
= e^u\frac{\partial u}{\partial x_1}\,dx_1 + \cdots + e^u\frac{\partial u}{\partial x_n}\,dx_n
```
```math
= e^u\left(\frac{\partial u}{\partial x_1}\,dx_1 + \cdots + \frac{\partial u}{\partial x_n}\,dx_n\right)
```
```math
= e^u\,du
```

从而得到一个熟悉的形式。（关于 $e^u$ 是否可微的讨论，参见习题 12.8.7。） $\blacksquare$

本页随后列出习题（Exercises）12.4.19、12.4.20、12.4.21：分别是在例 12.23 中当 $\Delta x=0.001$、$\Delta y=0.002$ 时计算 $\Delta f$ 与 $df$ 并比较其误差；验证 (41) 中关于 $d(u+v)$ 与 $d(u/v)$ 的公式；以及证明当 $u,v$ 在 $(x_0,y_0)\in\mathbb{R}^2$ 处可微时，它们的和、积与商（商还需 $v(x_0,y_0)\neq 0$）也可微。因未被正文直接引用，按约定此处略去详细翻译。

书页 494 末尾进入了下一节 12.5 链式法则（Chain Rules）的引言部分，属于后续翻译内容，此处不再展开。<span style="color:#7f8c8d">书页 495 · §12.5 Chain Rules（链式法则）</span>

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> §12.5 的一切从一个依赖图开始：（见下方正文）……

变量之间的依赖关系可以描述为“z 依赖 u，而 u 依赖 x 与 y”，并用示意图表示为：

#### <span style="color:#2471a3">**[example]**</span> <span style="color:#c0392b">例 12.26（Example 12.26）</span>

> <span style="color:#7f8c8d;">TBB §12.5, p.494</span>

（承接书页 494 末尾的 §12.5 引言与例 12.26：）设 $u=u(x,y)$，并设 $z=F(u)$。我们可以经由中间变量 $u$，把 $z$ 看作 $x,y$ 的函数 $G$。于是
```math
z=F(u)=F(u(x,y))=G(x,y).
```
这正是链式法则的"单中间变量"框架例子，其依赖图为
```math
\begin{array}{c}
x \\
\searrow \\
u \longrightarrow z \\
\nearrow \\
y
\end{array}
\tag{43}
```

与之关联的是两条 chain rules（链式法则）：

```math
\frac{\partial z}{\partial x} = \frac{\partial z}{\partial u}\frac{\partial u}{\partial x}, \qquad
\frac{\partial z}{\partial y} = \frac{\partial z}{\partial u}\frac{\partial u}{\partial y}
\tag{44}
```

这正是你在微积分中记住的公式。归根结底，z 通过单个变量 u 依赖两个变量 x 与 y。于是要计算两个偏导数（partial derivatives），$\frac{\partial z}{\partial x}$ 与 $\frac{\partial z}{\partial y}$，每个都像 (44) 那样涉及一项单项的链条化简。

> <span style="color:#7f8c8d;">TBB §12.5, p.495</span>（译者注：此为示例标记，实际对应例 12.27）

**例 12.27（例）** [example]：作为具体例子，令 $z = \sin(x^2 + y^3) = G(x,y)$，并记 $u(x,y) = x^2 + y^3$，$F(u) = \sin u$。这正对应于(43)中的框架。于是利用链式法则(44)可以得出：

```math
\frac{\partial z}{\partial x} = 2x\cos(x^2+y^3), \qquad
\frac{\partial z}{\partial y} = 3y^2\cos(x^2+y^3).
```

$\blacksquare$

下面我们把情况稍微复杂化一些。

> <span style="color:#7f8c8d;">TBB §12.5, p.495</span>（译者注：此为示例标记，实际对应例 12.28）

**例 12.28（例）** [example]：设 $x = f(t)$、$y = g(t)$、$z = F(x,y)$。这里我们可以把 z 看作 t 的函数：

```math
z = F(x,y) = F(f(t), g(t)) = G(t).
```

变量之间的依赖关系可以描述为“z 依赖 x 与 y，而两者又各自依赖 t”，并用示意图表示为：

```math
\begin{array}{c}
t \longrightarrow x \longrightarrow z \\
t \longrightarrow y \longrightarrow z
\end{array}
```

与之关联的链式法则为：

```math
G'(t) = \frac{dz}{dt} = \frac{\partial z}{\partial x}\frac{dx}{dt} + \frac{\partial z}{\partial y}\frac{dy}{dt}.
\tag{45}
```

注意，x 与 y 都只是 t 的函数，G 亦然，所以这里涉及的是 ordinary derivatives（常导数）。另一方面，$F(x,y)$ 是两个变量的函数，因此 $\frac{\partial z}{\partial x} = F_1$ 与 $\frac{\partial z}{\partial y} = F_2$ 才是偏导数。与例 12.26 相比，现在我们只需计算一个导数 $G'(t) = \frac{dz}{dt}$，但这一链式法则却包含两项求和，其中一项来自“从 t 到 z 的每一条路径”。$\blacksquare$

<span style="color:#7f8c8d">书页 496 · §12.5 Chain Rules（链式法则）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 例 12.30 把复杂度推上台阶：$z=F(x,y)$，而 $x=f(s,t),y=g(s,t)$。现在 $\partial z/\partial s$ 要沿"从 $s$ 到 $z$ 的每一条路径"走并求和：$s\!\to\!x\!\to\!z$ 与 $s\!\to\!y\!\to\!z$，于是 $\frac{\partial z}{\partial s}=\frac{\partial z}{\partial x}\frac{\partial x}{\partial s}+\frac{\partial z}{\partial y}\frac{\partial y}{\partial s}$。请把这个式子中的两项分别与依赖图的两条边一一对应——这就是**路径求和直觉**的完整形态，也是你之后在 §12.8 看到"雅可比矩阵相乘 $(k,i)$ 元素 = 对中间索引 $j$ 求和"时的直观底座。**第一性原理**：不论链条多长、分叉多少，规则始终是"线性逼近——复合——再展成和"，矩阵乘法把你的图压缩成一行点积。对比一维：一维只有一条链，所以链式法则就是"一个乘积"；多维分叉后变成"多个乘积的和"，这是"一个数→一个矩阵"跃迁的另一面。策略命名为「**逐路径求积再求和**」：画依赖图 → 数从目标到源的所有路径 → 每条路径写分量之乘积 → 相加。用它做例 12.31 的 $2st^2+3t e^{3st}$ 时，你会亲身体会到图比公式更可靠。

---


> <span style="color:#7f8c8d;">TBB §12.5, p.496</span>（译者注：此为示例标记，实际对应例 12.29）

**例 12.29（例）** [example]：再次给出一个具体例子，令 $x = t^2$、$y = t^3$，且 $z = xy$。于是由(45)得：

```math
\frac{dz}{dt} = y\cdot 2t + x\cdot 3t^2 = 2t^4 + 3t^4 = 5t^4,
```

当我们观察到 $G(t) = t^5$ 时，结果正如预期。$\blacksquare$

下面我们再让情形复杂一点。

> <span style="color:#7f8c8d;">TBB §12.5, p.496</span>（译者注：此为示例标记，实际对应例 12.30）

**例 12.30（例）** [example]：设 $z = F(x,y)$、$x = f(s,t)$、$y = g(s,t)$。我们可以经由 x 与 y 把 z 看作 s 与 t 的函数：

```math
z = F(x(s,t), y(s,t)) = G(s,t).
```

变量之间的依赖关系可以描述为“z 同时依赖 x 与 y，而两者又各自依赖 s 与 t”，并用示意图表示为：

```math
\begin{array}{c}
s \longrightarrow x \longrightarrow z \\
s \longrightarrow y \longrightarrow z \\
t \longrightarrow x \longrightarrow z \\
t \longrightarrow y \longrightarrow z
\end{array}
```

要计算 $\frac{\partial z}{\partial s}$，我们沿从 s 到 z 的每一条路径走，于是

```math
\frac{\partial z}{\partial s} = \frac{\partial z}{\partial x}\frac{\partial x}{\partial s} + \frac{\partial z}{\partial y}\frac{\partial y}{\partial s}
\tag{46}
```

类似地，沿从 t 到 z 的每一条路径走，有

```math
\frac{\partial z}{\partial t} = \frac{\partial z}{\partial x}\frac{\partial x}{\partial t} + \frac{\partial z}{\partial y}\frac{\partial y}{\partial t}.
```

$\blacksquare$

> <span style="color:#7f8c8d;">TBB §12.5, p.496</span>（译者注：此为示例标记，实际对应例 12.31）

**例 12.31（例）** [example]：设 $z = F(x,y) = x^2 + y^3$，$x = f(s,t) = st$，$y = g(s,t) = e^{st}$。那么(46)中的链式法则给出：

```math
\frac{\partial z}{\partial s} = 2x\cdot t + 3y^2\cdot t\,e^{st}
= 2(st)t + 3e^{2st}\cdot t\,e^{st}
= 2st^2 + 3t\,e^{3st}.
```

我们仍可通过观察到 $G(s,t) = (st)^2 + e^{3st}$ 并直接计算来验证这一结果。$\blacksquare$

当然，还有大量其他链条（chains）是可能的。<span style="color:#7f8c8d">书页 497 · §12.5 Chain Rules（链式法则）</span>

> <span style="color:#7f8c8d;">TBB §12.5, p.497 —— 例 12.32 的链式法则 schema 与 12.5.2 非形式证明之引入</span>

**[example]** 例 12.32：考虑一个由若干变量构成的依赖图（dependency schema / path schema）：四个源变量 $r,\,s,\,t,\,u$ 经由中间变量 $x,\,y$ 汇集到终极变量 $z$。具体而言，各条“路径”为 $r\to x\to z$、$s\to x\to z$ 与 $s\to y\to z$，以及 $u\to t\to y\to z$。也就是说：$r$ 只通向 $x$；$s$ 同时分叉通向 $x$ 与 $y$；而 $u$ 先通向 $t$，再由 $t$ 通向 $y$；最终 $x$ 与 $y$ 二者都通向 $z$。
> <span style="color:#7f8c8d;">TBB §12.5, p.497</span>

这一 schema 将导出下述三条链式法则（chain rule）：
```math
\frac{\partial z}{\partial r}=\frac{\partial z}{\partial x}\frac{\partial x}{\partial r}, \qquad
\frac{\partial z}{\partial s}=\frac{\partial z}{\partial x}\frac{\partial x}{\partial s}
+\frac{\partial z}{\partial y}\frac{\partial y}{\partial s}, \qquad
\frac{\partial z}{\partial u}=\frac{\partial z}{\partial y}\frac{\partial y}{\partial t}\frac{\partial t}{\partial u}.
```
我们应当就这一 schema 自行编出一个具体例子，并实际验证相应的链式法则成立。（这正是习题 12.5.1 的要求。）

（习题区按规范跳过：12.5.1、12.5.2、12.5.3、12.5.4。其中 12.5.4 给出 $z=F(x,y)$、$x=g(u,v,w)$、$y=h(u,v)$，要求画出依赖 schema 并写出 $\frac{\partial z}{\partial u},\frac{\partial z}{\partial v},\frac{\partial z}{\partial w}$ 的链式法则，思路与本例相同。）

**[subsection]** 12.5.2 链式法则的非形式证明（Informal Proof of a Chain Rule）

让我们以一种非形式的方式，来看看为什么链式法则会成立。例如，考察如下 schema：变量 $t$ 同时通向 $x$ 与 $y$，而 $x$ 与 $y$ 又都通向 $z$，即
```math
t\;\longrightarrow\; x\;\longrightarrow\; z , \qquad
t\;\longrightarrow\; y\;\longrightarrow\; z .
```

<span style="color:#7f8c8d">书页 498 · §12.5.2 链式法则的非形式证明（续）</span>

> <span style="color:#7f8c8d;">TBB §12.5, p.498 —— 例 12.30 的链式法则（非形式证明）</span>

与此 schema 相应的链式法则为
```math
\frac{dz}{dt}=\frac{\partial z}{\partial x}\frac{dx}{dt}+\frac{\partial z}{\partial y}\frac{dy}{dt}.
```
假设所需的可微性条件（differentiability requirements）均已满足，并采用显然的记号，则可以写
```math
\Delta z=f_1\,\Delta x+f_2\,\Delta y+\varepsilon\bigl(|\Delta x|+|\Delta y|\bigr), \tag{47}
```
其中当 $(\Delta x,\Delta y)\to(0,0)$ 时 $\varepsilon\to 0$。两边同时除以 $\Delta t$，得
```math
\frac{\Delta z}{\Delta t}=f_1\frac{\Delta x}{\Delta t}+f_2\frac{\Delta y}{\Delta t}
+\varepsilon\left(\frac{|\Delta x|}{\Delta t}+\frac{|\Delta y|}{\Delta t}\right). \tag{48}
```
在 $(48)$ 中令 $\Delta t\to 0$。我们注意到：由于当 $\Delta t\to 0$ 时确有 $\Delta x\to 0$ 且 $\Delta y\to 0$，故当 $\Delta t\to 0$ 时同样有 $\varepsilon\to 0$。

现在考察乘积项 $\varepsilon\bigl(\frac{|\Delta x|}{\Delta t}+\frac{|\Delta y|}{\Delta t}\bigr)$ 当 $\Delta t\to 0$ 时的行为。括号内的量分别趋于
```math
\varepsilon\!\left(\Bigl|\frac{dx}{dt}\Bigr|+\Bigl|\frac{dy}{dt}\Bigr|\right) \quad \text{当 } \Delta t\to 0^{+}\ \text{时}, \qquad
-\varepsilon\!\left(\Bigl|\frac{dx}{dt}\Bigr|+\Bigl|\frac{dy}{dt}\Bigr|\right) \quad \text{当 } \Delta t\to 0^{-}\ \text{时}.
```
因为 $\varepsilon\to 0$，当 $\Delta t$ 从任一侧趋于 $0$ 时，上述乘积都趋于 $0$。于是
```math
\frac{dz}{dt}=\lim_{\Delta t\to 0}\frac{\Delta z}{\Delta t}
=f_1\frac{dx}{dt}+f_2\frac{dy}{dt}+0
=\frac{\partial z}{\partial x}\frac{dx}{dt}+\frac{\partial z}{\partial y}\frac{dy}{dt}.
```
你会注意到，这段推导仅仅呈现了证明的“思路”（idea of a proof）；我们还尚未把各种假设（hypotheses）明确地表述出来。例如，$(47)$ 要求 $z$（作为 $x,y$ 的函数）可微。在目前这一阶段，我们只是想先把框架准备妥当，以便在下一小节中能对若干链式法则给出严格的证明（rigorous proof）。在那里，我们将证明一个覆盖例 12.30 的链式法则；其他链式法则的证明则会遵循类似的模式。

（习题 12.5.5 按规范跳过：要求就另一条链式法则写出非形式证明，方法与此相同。）

**[subsection]** 12.5.3 链式法则的记号（Notation of Chain Rules）

关于记号有必要先提一句告诫（word of caution）。像
```math
\frac{\partial z}{\partial s}=\frac{\partial z}{\partial x}\frac{\partial x}{\partial s}+\frac{\partial z}{\partial y}\frac{\partial y}{\partial s}
```
这样的链式，用 $\frac{\partial z}{\partial x}$、$\frac{\partial z}{\partial y}$ 这类符号来书写十分方便，因为这一记号大家都很熟悉，而且还暗示着各种“约分”（cancelation）：于是我们便很想说
```math
\frac{\partial z}{\partial x}\frac{\partial x}{\partial s}\quad\text{“看起来像”}\quad\frac{\partial z}{\partial s}.
```<span style="color:#7f8c8d">书页 499 · §12.5 Chain Rules（链式法则）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 例 12.33 想敲打的是记号真正的陷阱：式(49)两侧的 $\frac{\partial z}{\partial t}$ 是**两种不同的函数**——左侧把 $z$ 看作物 $s,t$ 的函数，右侧把 $z$ 看作物 $x,t$ 的函数。这在单变量里几乎不会出现，因为一维导数只有一种含义（自变量就一个）；多维引入"选择哪一组独立变量"后，同一个 $\frac{\partial z}{\partial t}$ 就因"函数身份"不同而不同。**第一性原理**：偏导数的完整身份 =（哪个函数 × 对它而言哪些是自变量）；记号砍掉了后半截信息，才造成"约分"幻觉。习题 12.5.6 那位想当然的学生正是在这里翻车：左右"约掉 $\partial z/\partial x$"得到 $e^x\,\partial z/\partial y=0$ 是彻头彻尾的错，因为等式两边 $\partial z/\partial x$ 指的不是同一个对象。规避之道在 p.500 末尾已有：引入辅助变量 $y=t$ 或写无歧义形式 $z=F(f(s,t),t)$ 并标注求值点。这与你学 6.042J 的"作用域/改名"思维同构——先厘清"每个名字绑定到哪个角色"再求导。我给这条**策略名**：「**定身份，再求导**」：写下每个偏导的完整自变量清单，再去套链式法则。

---


> <span style="color:#7f8c8d;">TBB §12.5, p.499 —— 例 12.33 与变量出现在不同层次时的细致辨析</span>

但当变量出现在不同层次（different levels）时须格外小心。考虑如下示意图
```math
\begin{array}{c}
t,\ s \rightarrow x \rightarrow z \\
t \rightarrow z
\end{array}
```
以及与之对应的链式法则
```math
\frac{\partial z}{\partial t}=\frac{\partial z}{\partial t}+\frac{\partial z}{\partial x}\frac{\partial x}{\partial t} . \tag{49}
```
记号 $\frac{\partial z}{\partial t}$ 在此有两种不同含义，一种在 $(49)$ 的左侧，另一种在右侧。让我们用一个具体例子来澄清这一点。

**[example]** 例 12.33：设 $z=te^{st}$。若直接计算 $\frac{\partial z}{\partial t}$，由乘积法则（product rule）得 $\frac{\partial z}{\partial t}=e^{st}+ste^{st}$。现在把 $z$ 视为复合函数（composite function）：令 $x=e^{st}$，于是 $z=tx$。由链式法则 $(49)$ 计算得
```math
\frac{\partial z}{\partial t}=\frac{\partial z}{\partial t}+\frac{\partial z}{\partial x}\frac{\partial x}{\partial t}
=x+t\,\frac{\partial x}{\partial t}=e^{st}+tse^{st}
```
与前面结果一致。这里 $\frac{\partial z}{\partial t}$ 的第一次出现才是我们所要求的：它表示当把 $z$ 视为 $s$ 与 $t$ 的函数时 $z$ 关于 $t$ 的偏导数（partial derivative）。第二次出现则表示当把 $z$ 视为 $x$ 与 $t$ 的函数时 $z$ 关于 $t$ 的偏导数。 $\blacksquare$
> <span style="color:#7f8c8d;">TBB §12.5, p.499</span>

若某示意图过于复杂而引起混淆，最好改用其他避免歧义的记号。我们可以通过引入一个额外变量 $y=t$ 来避开 $(49)$ 中的歧义记号。于是示意图变为
```math
\begin{array}{c}
s \rightarrow x \rightarrow z \\
t \rightarrow y \rightarrow z
\end{array}
```
而链式法则相应变为
```math
\frac{\partial z}{\partial t}=\frac{\partial z}{\partial x}\frac{\partial x}{\partial t}+\frac{\partial z}{\partial y}\frac{\partial y}{\partial t}
```
其中
```math
\frac{\partial y}{\partial t}=\frac{dy}{dt}=1
```
这是因为 $y=t$。在这一表达式中，$\frac{\partial z}{\partial y}$ 消除了 $\frac{\partial z}{\partial t}$ 的歧义使用。或者，我们还可以写出无歧义记号：令 $z=F(x,t)$、$x=f(s,t)$，于是 $z=F(f(s,t),t)$；那么
```math
\frac{\partial z}{\partial t}=F_1(f(s,t),t)\,f_2(s,t)+F_2(f(s,t),t) .
```

<span style="color:#7f8c8d">书页 500 · §12.5 Exercises（习题）</span>

> <span style="color:#7f8c8d;">TBB §12.5, p.500 —— 习题区 12.5.6–12.5.8 与 §12.5.4 链式法则的严格证明引言</span>

**[example]** 习题 12.5.6：设 $z=f(x,y)$ 且 $y=e^x$。由链式法则
```math
\frac{\partial z}{\partial x}=\frac{\partial z}{\partial x}\frac{\partial x}{\partial x}+\frac{\partial z}{\partial y}\frac{\partial y}{\partial x}=\frac{\partial z}{\partial x}+e^x\frac{\partial z}{\partial y} .
```
一位粗心的学生建议：两边同时约去 $\frac{\partial z}{\partial x}$，得到 $e^x\frac{\partial z}{\partial y}=0$，从而 $\frac{\partial z}{\partial y}=0$。你同意这种说法吗？若不同意，$\frac{\partial z}{\partial y}$ 的正确计算是什么？你需要哪些恰当的前提假设（hypotheses）？
> <span style="color:#7f8c8d;">TBB §12.5, p.500</span>

**[example]** 习题 12.5.7：设 $F$ 在 $\mathbb{R}^2$ 上可微。令 $x=r\cos\theta$、$y=r\sin\theta$，并设 $G(r,\theta)=F(x,y)=F(r\cos\theta,r\sin\theta)$。这样，当我们把直角坐标（rectangular coordinates）变换为极坐标（polar coordinates）时，$F$ 就变换成了 $G$。求证
```math
\frac{\partial G}{\partial r}=\frac{\partial F}{\partial x}\cos\theta+\frac{\partial F}{\partial y}\sin\theta
```
以及
```math
\frac{\partial G}{\partial \theta}=-\frac{\partial F}{\partial x}\,r\sin\theta+\frac{\partial F}{\partial y}\,r\cos\theta .
```
> <span style="color:#7f8c8d;">TBB §12.5, p.500</span>

**[example]** 习题 12.5.8：考虑一个水平边为 $x$、竖直边为 $y$ 的矩形。它的面积由公式 $A(x,y)=xy$ 给出，周长为 $P(x,y)=2x+2y$。我们立刻算出
```math
\frac{\partial A}{\partial x}=y . \tag{50}
```
现在把 $A$ 视为 $x$ 与 $P$ 的函数：
```math
A(x,P)=x\left(\frac{P}{2}-x\right)=\frac{Px}{2}-x^2 .
```
这里 $\frac{\partial A}{\partial x}=\frac{P}{2}-2x$，换算成 $x$、$y$ 后得到
```math
\frac{\partial A}{\partial x}=y-x . \tag{51}
```
我们看到 $(50)$ 与 $(51)$ 并不一致。（a）解释这个明显的矛盾（apparent discrepancy）。（b）把 $A$ 视为以 $P$ 为中间变量的 $x$、$y$ 的函数，从而推导出 $(50)$。参见注释 282。
> <span style="color:#7f8c8d;">TBB §12.5, p.500</span>

<span style="color:#7f8c8d">书页 500 · §12.5.4 Proofs of Chain Rules (I)（链式法则的证明（一））</span>

在 §12.5.2 中，我们给出了一条非严格的指示性说明，解释链式法则为何成立。在例 12.28 中，我们考察了与如下链式示意图相对应的情形
```math
\begin{array}{c}
t \rightarrow x \rightarrow z \\
t \rightarrow y \rightarrow z
\end{array}
```
现在我们给出这条链式法则的严格（precise）陈述与证明，它可作为如何推广到一般情形的范本。<span style="color:#7f8c8d">书页 501 · §12.5 Chain Rules（链式法则）</span>

**[theorem]** 定理 12.34：设 $f$ 与 $g$ 是定义在 $t_0 \in \mathbb{R}$ 的一个邻域（neighborhood）上的实值函数（real-valued functions）。假定 $f$ 与 $g$ 都在 $t_0$ 处可微（differentiable）。设 $F$ 是定义在 $(x_0,y_0)\in\mathbb{R}^2$ 的一个邻域上的实值函数，其中 $x_0=f(t_0)$ 且 $y_0=g(t_0)$。假定 $F$ 在 $(x_0,y_0)$ 处可微。令 $G(t)=F(f(t),\,g(t))$。则 $G$ 在 $t_0$ 处可微，且
```math
G'(t_0)=F_1(x_0,y_0)\,f'(t_0)+F_2(x_0,y_0)\,g'(t_0) .
```
> <span style="color:#7f8c8d;">TBB §12.5, p.501</span>

**[proof]** 证明：记 $x=f(t)$、$y=g(t)$。于是
```math
G(t)-G(t_0)=F(f(t),\,g(t))-F(f(t_0),\,g(t_0))=F(x,y)-F(x_0,y_0) .
```
由于 $F$ 在 $(x_0,y_0)$ 处可微，我们可以写出
```math
\frac{G(t)-G(t_0)}{t-t_0}=\frac{F(x,y)-F(x_0,y_0)}{t-t_0}
=F_1(x_0,y_0)\,\frac{x-x_0}{t-t_0}+F_2(x_0,y_0)\,\frac{y-y_0}{t-t_0}+\varepsilon(x,y)\left(\frac{|x-x_0|}{t-t_0}+\frac{|y-y_0|}{t-t_0}\right) \tag{52}
```
其中
```math
\varepsilon(x,y)\to 0\ \ \text{当 }\ |x-x_0|\to 0\ \text{且 }\ |y-y_0|\to 0 . \tag{53}
```
现在我们令 $t\to t_0$，并考察 $(52)$ 中第二、第三行的三项。由于 $f$ 与 $g$ 在 $t_0$ 处可微，它们在 $t_0$ 处连续（continuous），所以当 $t\to t_0$ 时
```math
f(t)\to f(t_0)\ \ \text{且 }\ g(t)\to g(t_0) .
```
从而当 $t\to t_0$ 时
```math
x\to x_0\ \ \text{且 }\ y\to y_0 . \tag{54}
```
我们还得到当 $t\to t_0$ 时
```math
\frac{x-x_0}{t-t_0}=\frac{f(t)-f(t_0)}{t-t_0}\to f'(t_0) , \tag{55}
```
当 $t\to t_0$ 时
```math
\frac{y-y_0}{t-t_0}=\frac{g(t)-g(t_0)}{t-t_0}\to g'(t_0) . \tag{56}
```
$(52)$ 中最后一项是两个量的乘积。第一个量是 $\varepsilon(x,y)$，当 $t\to t_0$ 时它趋于零（依据 $(53)$ 与 $(54)$）。第二个量是
```math
\frac{|x-x_0|}{t-t_0}+\frac{|y-y_0|}{t-t_0} ,
```
它的绝对值不超过
```math
\left|\frac{x-x_0}{t-t_0}\right|+\left|\frac{y-y_0}{t-t_0}\right| .
```
最后一个表达式趋于 $|f'(t_0)|+|g'(t_0)|$，因此当 $t\to t_0$ 时
```math
\varepsilon(x,y)\left(\frac{|x-x_0|}{t-t_0}+\frac{|y-y_0|}{t-t_0}\right)\to 0 . \tag{57}
```

<span style="color:#7f8c8d">书页 502 · §12.5 Chain Rules（链式法则）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定理 12.35 是一维中值定理 $f(x_0+h)-f(x_0)=f'(\xi_0)h$ 的忠实移植：$F(x_0+h,y_0+k)-F(x_0,y_0)=F_1(\xi_0,\eta_0)\,h+F_2(\xi_0,\eta_0)\,k$，等价地写作 $F(P_2)-F(P_1)=\nabla F(P_0)\cdot(P_2-P_1)$。**第一性原理**：多起来的那几个维度，用一条"参数化线段" $G(t)=F(x_0+th,y_0+tk)$ 就整整齐齐压回单变量，再调用一维 MVT（定理 7.20）+ 链式法则（定理 12.34）即得——这是「**降维转单**」的教科书级示范：不发明新算法，把新问题化为旧定理的调用链。几何上它说：线段两端点函数值之差，等于**线段内某点的梯度**在位移方向上的投影（乘以线段长），把"斜率"推广成"梯度轮廓"。对比一维：一维的点 $\xi_0$ 换成二维的 $(\xi_0,\eta_0)$ 时，课本选在两个坐标轴上各自取点——这是为了维持证明的简洁，也提示二维 MVT 的中间点不必唯一、不必居中。该定理是后面 §12.6 隐函数/反函数定理的核心工具（章末你会反复回来用它），值得在笔记里单独给它贴上"降维转单"的标签。

---


于是，综合 $(52)$、$(55)$、$(56)$ 与 $(57)$，我们看到
```math
\lim_{t\to t_0}\frac{G(t)-G(t_0)}{t-t_0}=F_1(x_0,y_0)\,f'(t_0)+F_2(x_0,y_0)\,g'(t_0)
```
这正是所要证明的。 $\blacksquare$
> <span style="color:#7f8c8d;">TBB §12.5, p.502</span>

**[definition]** §12.5.5 Mean Value Theorem（中值定理）：定理 12.34 使我们得以获得经典中值定理（mean value theorem）的二维类比。回忆经典中值定理断言：在函数 $f$ 的适当可微性假设下，
```math
f(x_0+h)-f(x_0)=f'(\xi_0)\,h
```
对某个介于 $x_0+h$ 与 $x_0$ 之间的 $\xi_0$ 成立。

**[theorem]** 定理 12.35：设 $F$ 定义在开集（open set）$D\subset\mathbb{R}^2$ 上。设 $(x_0,y_0)$ 与 $(x_0+h,\,y_0+k)$ 是 $D$ 中的点，并假定由这两点所确定的线段（line segment）$L$ 位于 $D$ 中。假定 $F$ 在 $L$ 上可微。则存在介于 $x_0$ 与 $x_0+h$ 之间的 $\xi_0$，以及介于 $y_0$ 与 $y_0+k$ 之间的 $\eta_0$，使得
```math
F(x_0+h,\,y_0+k)-F(x_0,y_0)=F_1(\xi_0,\eta_0)\,h+F_2(\xi_0,\eta_0)\,k . \tag{58}
```
> <span style="color:#7f8c8d;">TBB §12.5, p.502</span>

**[proof]** 证明：首先将线段 $L$ 参数化表示：
```math
x=x_0+th ,\qquad y=y_0+tk \qquad (0\le t\le 1) .
```
于是我们可以把 $F$ 在 $L$ 上的函数视为 $[0,1]$ 上关于 $t$ 的函数。令
```math
G(t)=F(x_0+th,\,y_0+tk) ,\qquad (0\le t\le 1) . \tag{59}
```
由定理 12.34，
```math
G'(t)=h\,F_1(x_0+th,\,y_0+tk)+k\,F_2(x_0+th,\,y_0+tk) . \tag{60}
```
由一元函数的中值定理（定理 7.20），我们得到对某个 $t_0\in(0,1)$ 有
```math
G(1)-G(0)=G'(t_0) .
```
现在，由 $(59)$ 我们看到 $G(0)=F(x_0,y_0)$、$G(1)=F(x_0+h,\,y_0+k)$，故
```math
G'(t_0)=F(x_0+h,\,y_0+k)-F(x_0,y_0) . \tag{61}
```
但由 $(60)$ 有
```math
G'(t_0)=h\,F_1(x_0+t_0h,\,y_0+t_0k)+k\,F_2(x_0+t_0h,\,y_0+t_0k) . \tag{62}
```<span style="color:#7f8c8d">书页 503 · §12.5 Chain Rules（链式法则）</span>

> <span style="color:#7f8c8d;">TBB §12.5, p.503 —— 定理 12.35 证明的收尾，与例 12.30 的链式示意图</span>

将 (61) 与 (62) 结合，我们得到
```math
F(x_0+h,\,y_0+k)-F(x_0,\,y_0)=hF_1(x_0+t_0h,\,y_0+t_0k)+kF_2(x_0+t_0h,\,y_0+t_0k).
```
为了得到 (58)，我们只需令 $\xi_0=x_0+t_0h$ 且 $\eta_0=y_0+t_0k$。 $\blacksquare$
> <span style="color:#7f8c8d;">至此完成了定理 12.35（中值定理的二维形式，即 $F(P_2)-F(P_1)=\nabla F(P_0)\cdot(P_2-P_1)$）的证明。</span>

> 习题 12.5.10 要求以给出结论 $F(P_2)-F(P_1)=\nabla F(P_0)\cdot(P_2-P_1)$ 的形式来陈述刚才的中值定理（其中 $P_1,P_2,P_0$ 为 $\mathbb{R}^2$ 中的点，$\nabla$ 表示 gradient（梯度））。该题属于非必需的练习，此处跳过。

**[theorem]** 定理 12.36（链式法则的证明（二），12.5.6）：现在我们转向一条与例 12.30 中示意图相对应的链式法则的陈述与证明。
> <span style="color:#7f8c8d;">此处对应的链式结构可示意为 $s\to x$、$t\to y$，两者共同汇入 $z=F(x,y)$，即 $G(s,t)=F(f(s,t),\,g(s,t))$。</span>

令 $F$ 定义于某个 open set（开集）$D\subset\mathbb{R}^2$ 上，并令 $(x_0,y_0)$ 为 $D$ 中的一点。设 $F$ 在 $(x_0,y_0)$ 处可微（differentiable）。令 $f$ 与 $g$ 定义于点 $(s_0,t_0)\in\mathbb{R}^2$ 的一个邻域内。设 $f$ 与 $g$ 在 $(s_0,t_0)$ 处具有一阶偏导数（first partial derivative），且 $x_0=f(s_0,t_0)$、$y_0=g(s_0,t_0)$。定义 $G(s,t)=F(f(s,t),\,g(s,t))$。那么 $G$ 在 $(s_0,t_0)$ 处具有一阶偏导数，并且
```math
G_1(s_0,t_0)=F_1(x_0,y_0)\,f_1(s_0,t_0)+F_2(x_0,y_0)\,g_1(s_0,t_0). \tag{63}
```
```math
G_2(s_0,t_0)=F_1(x_0,y_0)\,f_2(s_0,t_0)+F_2(x_0,y_0)\,g_2(s_0,t_0).
```
> <span style="color:#7f8c8d;">TBB §12.5, p.503</span>

在证明定理 12.36 之前，我们作若干观察。

1. 读者应当检查：公式 (63) 不过是例 12.30 中示意图的精确版本。特别是，公式 (63) 使各偏导数的求值位置一目了然。

2. 在定理 12.34 中我们得出了函数 $G$ 的可微性。此处我们并不得出这一结论。我们也不在这里假设 $f$ 与 $g$ 可微。定理 12.36 只是一个关于 $G$ 的一阶偏导数的定理，涉及它们的存在性以及求取它们的公式。[诚然，若我们假设 $f$ 与 $g$ 在 $(s_0,t_0)$ 处可微，那么本可以得出 $G$ 可微，但这一点我们要到 §12.8 才会证明。]

3. 注意定理 12.34 与定理 12.36 两段证明在思路上彼此相似。

<span style="color:#7f8c8d">书页 504 · §12.5.6 Proofs of Chain Rules (II)（链式法则的证明（二））</span>

> <span style="color:#7f8c8d;">TBB §12.5, p.504 —— 定理 12.36 的证明与讨论</span>

**[proof]** 证明：我们将建立第一条链式法则 (63)，第二条的证明与之类似（习题 12.5.11）。

为了计算 $G_1(s_0,t_0)$，记 $x=f(s,t_0)$、$y=g(s,t_0)$。于是由 $G$ 的定义，
```math
G(s,t_0)-G(s_0,t_0)=F(x,y)-F(x_0,y_0). \tag{64}
```
由于假设 $F$ 在 $(x_0,y_0)$ 处可微，我们可以写出
```math
F(x,y)-F(x_0,y_0)=F_1(x_0,y_0)(x-x_0)+F_2(x_0,y_0)(y-y_0)+\varepsilon(x,y)\left(|x-x_0|+|y-y_0|\right), \tag{65}
```
其中当 $(x,y)\to(x_0,y_0)$ 时 $\varepsilon(x,y)\to 0$。

由 (64) 与 (65) 可见，对 $s\neq s_0$，
```math
\frac{G(s,t_0)-G(s_0,t_0)}{s-s_0}
=\frac{F(x,y)-F(x_0,y_0)}{s-s_0}
```
```math
=F_1(x_0,y_0)\frac{x-x_0}{s-s_0}+F_2(x_0,y_0)\frac{y-y_0}{s-s_0}+\varepsilon(x,y)\left(\frac{|x-x_0|}{s-s_0}+\frac{|y-y_0|}{s-s_0}\right). \tag{66}
```
现在我们就可以如定理 12.34 的证明那样完成本证明：令 $s\to s_0$。(66) 的右端趋于
```math
F_1(x_0,y_0)\,f_1(s_0,t_0)+F_2(x_0,y_0)\,g_1(s_0,t_0), \tag{67}
```
而余项（residual term）
```math
\varepsilon(x,y)\left(\frac{|x-x_0|}{s-s_0}+\frac{|y-y_0|}{s-s_0}\right)
```
趋于零，这一事实与定理 12.34 证明中的相应部分相似。于是，(66) 的左端在 $s\to s_0$ 时趋于一个极限。该极限当然就是 $G_1(s_0,t_0)$。因此
```math
G_1=F_1(x_0,y_0)\,f_1(s_0,t_0)+F_2(x_0,y_0)\,g_1(s_0,t_0).
```
$\blacksquare$

> 习题 12.5.11 要求证明链式法则 (63) 中的第二条；习题 12.5.12 要求补充 (66) 中 $\varepsilon(x,y)(\frac{|x-x_0|}{s-s_0}+\frac{|y-y_0|}{s-s_0})$ 这一项在 $s\to s_0$ 时趋于零的论证细节；习题 12.5.13 则要求对另一链式示意图陈述并证明相应的链式法则。这三题均为非必需的练习，此处跳过。<span style="color:#7f8c8d">书页 505 · §12.5 Chain Rules（链式法则）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> Laplacian $\nabla^2 z=\frac{\partial^2 z}{\partial x^2}+\frac{\partial^2 z}{\partial y^2}$ 是一个**二阶线性微分算子**（$\nabla\cdot\nabla$），满足它的 $z$ 叫调和函数。把它和你已学的物理对接：**拉普拉斯方程**源自 Laplace 的引力势理论（1799）；**热传导方程** $\kappa\nabla^2 T=\partial T/\partial t$ 由 Fourier（1822）给出，Hamilton（1847）最早用算符形式 $\bigl(\triangleleft^2-\frac{a\,d}{dt}\bigr)v=0$ 重写；**波动方程** $c^2 f_{xx}=f_{tt}$ 是本章例 12.38。**第一性原理**：$\nabla^2 f$ 测量"$f$ 在一点相对其邻域平均的偏离"——第二差分的无穷小极限，它无关整体平移、只对局曲率敏感，所以是扩散/波的"加速项"。这同时也解释了计算机视觉里为什么 Image/Sobel 类"拉普拉斯模板"能抓边缘：灰度变化剧烈处二阶差最大。组合微分的计算（例 12.37 求 $d^2z/dt^2$）是链式法则第二次上阵的实战：关键是把 $F_1,F_2$ 再当作 $t$ 的复合函数重套一次链式法则，并借用混合偏导相等（定理 12.5）把两个交叉项合并——这是「**复合的分层再套链**」的收敛版，也是你衔接 §12.8 里"二次逼近 / 牛顿迭代"的伏笔（18.065 的 Newton 法同样基于 Taylor 展开）。

---

> 以上共 10 条译者注，覆盖书页 485–506（§12.4 + §12.5）。每条注前均已注明拟插入的书页与上下文关键词。


> <span style="color:#7f8c8d;">TBB §12.5, p.505 —— 承接定理 12.36 的讨论，引入 §12.5.7 高阶导数与 Laplacian</span>

要理解这张示意图，可以循两种途径进行：其一，模仿定理 12.34 与 12.36 的证明思路；其二，把它看作支配定理 12.36 的那张 $schema$（示意图）的一个特例。

**12.5.7 Higher Derivatives（高阶导数）**

有时需要用链式法则来计算高阶偏导数（higher partial derivatives）。例如考虑 Laplace 方程（Laplace's equation）
```math
\frac{\partial^2 z}{\partial x^2}+\frac{\partial^2 z}{\partial y^2}=0 . \tag{68}
```
一个满足此方程的二次可微（twice differentiable）函数 $z$ 称为调和函数（harmonic）。这类函数在数学（如复分析、应用数学）和物理学的许多领域中都很重要。表达式
```math
\frac{\partial^2 z}{\partial x^2}+\frac{\partial^2 z}{\partial y^2}
```
被称为函数 $z$ 的 Laplacian（Laplace 算子（Laplacian））。

假设我们希望把这个方程用极坐标（polar coordinates）表示。我们令 $x=r\cos\theta$、$y=r\sin\theta$，并考虑如下的示意图
```math
\begin{array}{c}
x \rightarrow r \rightarrow z \\
x \rightarrow \theta \rightarrow z \\
y \rightarrow r \rightarrow z \\
y \rightarrow \theta \rightarrow z
\end{array}
```
我们想把 $(68)$ 用 $r$ 与 $\theta$ 来表示，为此需把 $\frac{\partial^2 z}{\partial x^2}$ 与 $\frac{\partial^2 z}{\partial y^2}$ 化为以 $r$、$\theta$ 为变量的函数。这些计算显得繁琐，已留作习题 12.5.14。而我们转而在例 12.28 中首先考察一个不那么繁琐的示意图
```math
\begin{array}{c}
t \rightarrow x \rightarrow z \\
t \rightarrow y \rightarrow z
\end{array}
 \tag{69}
```
这里 $z=F(x,y)$，而 $x$、$y$ 都是 $t$ 的函数。与之相应的链式法则为
```math
\frac{\partial z}{\partial t}
=\frac{\partial z}{\partial x}\frac{dx}{dt}
+\frac{\partial z}{\partial y}\frac{dy}{dt} . \tag{70}
```
我们希望计算 $\frac{d^2z}{dt^2}=\frac{d}{dt}\!\left(\frac{dz}{dt}\right)$。由 $(70)$ 可见
```math
\frac{\partial^2 z}{\partial t^2}
=\frac{d}{dt}\!\left(\frac{\partial z}{\partial x}\frac{dx}{dt}\right)
+\frac{d}{dt}\!\left(\frac{\partial z}{\partial y}\frac{dy}{dt}\right)
=\frac{d}{dt}\!\left(\frac{\partial z}{\partial x}\right)\frac{dx}{dt}
+\frac{\partial z}{\partial x}\frac{d^2 x}{dt^2}
+\frac{d}{dt}\!\left(\frac{\partial z}{\partial y}\right)\frac{dy}{dt}
+\frac{\partial z}{\partial y}\frac{d^2 y}{dt^2} . \tag{71}
```

<span style="color:#7f8c8d">书页 506 · §12.5 Chain Rules（链式法则）</span>

> <span style="color:#7f8c8d;">TBB §12.5, p.506 —— 混合偏导的代入重排得到公式 (74)，例 12.37、12.38（波动方程）</span>

这最后一项表达式中含有两项尚需进一步展开，即 $\frac{d}{dt}\!\left(\frac{\partial z}{\partial x}\right)$ 与 $\frac{d}{dt}\!\left(\frac{\partial z}{\partial y}\right)$。现在 $\frac{\partial z}{\partial x}=F_1$、$\frac{\partial z}{\partial y}=F_2$，二者都是 $x$、$y$ 的函数。为求它们对 $t$ 的导数，我们注意到示意图 $(69)$ 再次适用，于是得到
```math
\frac{d}{dt}\!\left(\frac{\partial z}{\partial x}\right)
=\frac{\partial}{\partial x}\!\left(\frac{\partial z}{\partial x}\right)\frac{dx}{dt}
+\frac{\partial}{\partial y}\!\left(\frac{\partial z}{\partial x}\right)\frac{dy}{dt}
=\frac{\partial^2 z}{\partial x^2}\frac{dx}{dt}
+\frac{\partial^2 z}{\partial y\,\partial x}\frac{dy}{dt} . \tag{72}
```
类似地
```math
\frac{d}{dt}\!\left(\frac{\partial z}{\partial y}\right)
=\frac{\partial^2 z}{\partial y^2}\frac{dy}{dt}
+\frac{\partial^2 z}{\partial x\,\partial y}\frac{dx}{dt} . \tag{73}
```
若假设所涉及的所有偏导数均连续，那么 $(72)$、$(73)$ 中出现的混合偏导数（mixed partials）相等（定理 12.5）。把 $(72)$、$(73)$ 代入 $(71)$ 并重新整理各项，就得到公式
```math
\frac{\partial^2 z}{\partial t^2}
=\frac{\partial^2 z}{\partial x^2}\left(\frac{dx}{dt}\right)^{\!2}
+2\frac{\partial^2 z}{\partial x\,\partial y}\frac{dx}{dt}\frac{dy}{dt}
+\frac{\partial^2 z}{\partial y^2}\left(\frac{dy}{dt}\right)^{\!2}
+\frac{\partial z}{\partial x}\frac{d^2 x}{dt^2}
+\frac{\partial z}{\partial y}\frac{d^2 y}{dt^2} . \tag{74}
```
若我们不作充分的正则性（regularity）假设以保证混合偏导数相等，那么 $(74)$ 的第二个项就必须写成和的形式
```math
\left(\frac{\partial^2 z}{\partial x\,\partial y}
+\frac{\partial^2 z}{\partial y\,\partial x}\right)
\frac{dx}{dt}\frac{dy}{dt} .
```

**[example]** 例 12.37：公式 $(74)$ 可以用下面这个简单的例子来说明：$z=x^2y^3$，$x=t^4$，$y=t^5$。于是直接可得 $z=t^{23}$，所以 $\frac{d^2z}{dt^2}=506\,t^{21}$。应用公式 $(74)$ 能得到同样的结果。 $\blacksquare$
> <span style="color:#7f8c8d;">TBB §12.5, p.506</span>

**[example]** 例 12.38：考虑波动方程（wave equation）
```math
c^2\frac{\partial^2 f}{\partial x^2}=\frac{\partial^2 f}{\partial t^2} ,
```
其中 $c$ 是一个常数。这里 $f(x,t)$ 描述波中位于水平坐标 $x$ 处的质点在时刻 $t$ 的竖直位移（vertical displacement）。我们来证明：任何形如
```math
f(x,t)=g(x+ct)
```
的函数（其中 $g$ 二次可微）都满足此方程。通过作代换 $u=x+ct$、$z=g(u)$，我们得到如下示意图，它与例 12.26 的示意图 $(43)$ 等价。
```math
\begin{array}{c}
x \rightarrow u \rightarrow z \\
t \rightarrow u \rightarrow z
\end{array}
```
> <span style="color:#7f8c8d;">TBB §12.5, p.506</span><span style="color:#7f8c8d">书页 507 · §12.6 Implicit Function Theorems（隐函数定理）</span>

于是合适的 chain rule（链式法则）变为 $f_1(x,t)=g_0(u)\frac{\partial u}{\partial x}=g_0(x+ct)$ 与 $f_2(x,t)=g_0(u)\frac{\partial u}{\partial t}=cg_0(x+ct)$。

再次应用链式法则，我们得到 $f_{11}(x,t)=\frac{\partial}{\partial x}\left(g_0(x+ct)\right)=g_{00}(x+ct)$，以及 $f_{22}(x,t)=\frac{\partial}{\partial t}\left(cg_0(x+ct)\right)=c^2 g_{00}(x+ct)$。

因此 $c^2 f_{11}(x,t)=f_{22}(x,t)$，亦即 $c^2\frac{\partial^2 f}{\partial x^2}=\frac{\partial^2 f}{\partial t^2}$，确证函数 $f$ 确实满足 wave equation（波动方程）。$\blacksquare$

> 习题 12.5.14、12.5.15 讨论 Laplacian（Laplace 算子（Laplacian））在极坐标与柱坐标下的变换形式，属于非必需习题，此处跳过。

> 习题 12.5.16 要求利用习题 12.5.15 的结果推导球坐标下的Laplace 算子（Laplacian），同样为非必需习题，此处跳过。

假设我们被要求解一个形如 $F(x, y) = 0$ 的方程（记为 (75)），把 $y$ 表示为 $x$ 的函数。

要说明某个函数 $y=\varphi(x)$ 在点 $x_0$ 的一个 neighborhood（邻域）$I$ 内"解出"以 $x$ 表示的 $y$，我们真正的意思是：$\varphi: I \to \mathbb{R}$，且对所有 $x\in I$ 成立 $F(x,\varphi(x))=0$。

由于要显式地解出这种方程（亦即求出 $\varphi(x)$ 的一个公式）往往并不可能，我们需要了解解存在的条件、解唯一的条件，还需要了解求取解的导数 $y'=\varphi'(x)$ 的方法。

这应该是一个熟悉的问题。

它在大多数微积分课程中被作为 implicit differentiation（隐微分）讲授，在那里我们获得求导的种种技巧。

不过在通常的讲授中，人们对 existence（存在性）与 uniqueness（唯一性）问题很少关注。

一个例子就足以唤起这些想法。

<span style="color:#7f8c8d">书页 508 · §12.6 Implicit Function Theorems（隐函数定理）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 为什么必须 $F_2(x_0,y_0)\neq 0$ 才能把 $y$ 解出来？先回到你熟悉的代数。把 $F$ 看成 $x$-$y$ 平面上方的一张曲面，$F_2$ 就是 $y$ 方向的变化率——沿 $y$ 挪动时 $F$ 升落得快不快。若在某点 $F_2=0$，说明曲面在该点沿 $y$ 方向"拉平了"（这样的点我们称为驻点/奇点）；此时方程 $F=0$ 的零点在 $y$ 方向可能分叉成多枝、甚至整段塌陷，你没法凭局部信息锁定唯一一个 $y$。正如 $Ax^2+Bx+C=0$，判别式为 0 时两解"粘合"、退化成无法稳定追踪的一个根。换句话说，$F_2\neq 0$ 保证曲面在该处沿 $y$ 是"竖着穿过"而非"水平擦抹"，于是切平面与水平切片横截相交、交点唯一——这就是"正则条件"的第一性原理直观。后文正是靠 $F_2>0$ 推出 $F(x_0,\cdot)$ 严格单调，再借介值性质锁定那个唯一解。它也是你在第 11 章已熟悉的"压缩/非退化给出局部良构"这一思想的又一化身。

---


> <span style="color:#7f8c8d;">图 12.6 展示了 $F(x,y)=y^2-x=0$ 在 $x_0$ 的一个邻域 $I$ 中的一条解曲线，其中 $x_0 > 0$。</span>

> <span style="color:#7f8c8d;">TBB §12.6, p.508</span>

> [example]<span style="color:#c0392b">例 12.39</span>

考虑简单的方程 $F(x,y)=y^2-x=0$（记为 (76)）。

如果我们把此方程显式地就 $x$ 用 $y$ 来表达而解出，得到 $x=y^2$（记为 (77)）。

在初等微积分中，人们说方程 (76) 隐式地把 $x$ 表示为 $y$ 的函数，而 (77) 给出了 $x$ 作为 $y$ 的函数的显式表示。

若反过来，我们尝试就 $y$ 用 $x$ 来表达而解出 (76)，则得到 $y=\pm\sqrt{x}$（记为 (78)）。

这并不能把 $y$ 表示为 $x$ 的函数，因为对每一个 $x>0$ 都存在两个可能的 $y$ 值。

然而，若 $x_0>0$ 且 $y_0$ 是使 (76) 得到满足的取值之一，那么在 $\mathbb{R}$ 中存在 $x_0$ 的一个邻域 $I$，使得式 (78) 中的两种选择之一在该邻域内把 $y$ 表示为 $x$ 的连续函数（图 12.6）。

注意我们不能对 $x_0=0$ 作出同样的断言。

还应注意，在点 $(0,0)$ 处存在一条 vertical tangent（铅直切线），并且对 $F(x,y)=y^2-x$ 有 $F_2(0,0)=0$。$\blacksquare$

> [theorem]<span style="color:#2471a3">定理 12.40（引言）

我们现在即将陈述并证明的 implicit function theorem（隐函数定理），恰好刻画了这种情形，并给出解确实存在的条件。

这一判断同样为隐微分这一微积分技巧提供了理论基础，该技巧正是用来求取隐式定义函数的导数的。

> <span style="color:#7f8c8d;">TBB §12.6, p.508</span>

> [definition]<span style="color:#00838f">12.6.1 单变量情形（One-Variable Case）

定理 12.40 给出了形如 $F(x,y)=0$ 的方程能够在局部唯一解出的条件。

此外，它表明我们对 $F$ 所强加的 regularity（正则）条件保证了解函数也具有良态的性质。

我们把这个定理看成通向我们在接下来两个小节中所得到的、更一般的隐函数定理的一块"热身"。

> <span style="color:#7f8c8d;">TBB §12.6, p.508</span>

注意该结论的 local（局部）性质：我们并不宣称存在全局解。<span style="color:#7f8c8d">书页 509 · §12.6 Implicit Function Theorems（隐函数定理）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 隐函数定理的故事横贯三个世纪。Joseph-Louis Lagrange（1736–1813）在 18 世纪为求约束极值发明了"拉格朗日乘子"：在 $F(x,y)=0$ 这条约束曲线下找 $\nabla g$ 与 $\nabla F$ 平行的点——他事实上默认了约束曲线是"良构"的，而这恰是今天这条定理要保底的事。Augustin-Louis Cauchy（1789–1857）在《无穷小分析讲义》(1823) 里处理了 $F(x,y)=0$ 的隐式求导，为初等"隐微分"的合法性作了早期辩护，但还没升级成今日这种精确表述。Ulisse Dini（1845–1918）在 1877 年给出隐函数定理的现代严格证明，故它时称"Dini 定理"；反函数定理的严格现代版本同样归功于他。Carl Jacobi（1804–1851）贡献的雅可比行列式为"线性化是否可逆"的检验提供了工具，而 Camille Jordan（1838–1922）在分析教程中对这类局部结构又作了系统整理。今天的形式，是把这些散落多个世纪的零散结论"收拢"成的一条定理。

---

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定理 12.40 的证明是两条老思路的接力赛。第一阶段可命名为「夹逼–介值法」：先用连续性把 $(x_0,y_0)$ 收进一个 $F_2>0$ 的开矩形 $N$，沿 $y$ 剖一刀得 $F(x_0,c)<0\lt F(x_0,d)$；再把这条"界"（bound）铺满整个 $I_0$，最后用介值性质加单调性同时拿到"存在"与"唯一"。这正是从单变量推广到多元时不变的那根骨架。第二阶段可叫「切线逼近法」：在竖直线段上应用二维中值定理（定理 12.35）把 $F$ 线性化，颠出差商 $\varphi'=-F_1/F_2$。请注意你的脚手架——单变量隐微分公式 $\frac{dy}{dx}=-\frac{F_1}{F_2}$ 在初等微积分你早熟记过，这里的新突破不是新公式，而是把"若解存在则导数长这样"升级为"解确实存在、唯一、且光滑"。每一步都在复用你已装好的工具：开集、邻域、中值、单调、连续性。

---


> [theorem]<span style="color:#2471a3">定理 12.40（隐函数定理）</span>

> <span style="color:#7f8c8d;">TBB §12.6, p.509</span>

设 $D$ 是 $\mathbb{R}^2$ 中的一个开集，且 $F:D\to\mathbb{R}$。

假设 $F$ 在 $D$ 上具有连续的 partial derivatives（偏导数）$F_1$ 与 $F_2$，并设 $(x_0,y_0)\in D$ 满足
```math
F(x_0,y_0)=0 \quad\text{且}\quad F_2(x_0,y_0)\neq 0.
```

于是存在开区间 $I_0\subset\mathbb{R}$ 与一个 continuously differentiable（连续可微）函数 $\varphi:I_0\to\mathbb{R}$，使得 $x_0\in I_0$，对所有 $x\in I_0$ 有 $(x,\varphi(x))\in D$，$\varphi(x_0)=y_0$，且对所有 $x\in I_0$ 成立 $F(x,\varphi(x))=0$。

此外，公式
```math
\varphi'(x)=-\frac{F_1(x,\varphi(x))}{F_2(x,\varphi(x))}
```
对所有 $x\in I_0$ 均成立。

> [proof]<span style="color:#2471a3">证明</span>

假设 $F_2(x_0,y_0)>0$。（若 $F_2(x_0,y_0)<0$，证明类似。）

由于由假设 $F_2$ 连续，故存在 $(x_0,y_0)$ 在 $D$ 中的一个 neighborhood（邻域）$N$，使得在 $N$ 上 $F_2>0$。

我们可以取 $N$ 为矩形形式 $N=I\times J$，以 $(x_0,y_0)$ 为矩形中心；设 $J=[c,d]$。

由于在 $N$ 上 $F_2>0$，函数 $F(x_0,\cdot)$ 在 $J$ 上递增；而 $F(x_0,y_0)=0$，故得知 $F(x_0,c)<0\lt F(x_0,d)$。

函数 $F$ 连续，所以存在开区间 $I_0\subset I$，以 $x_0$ 为中心，且对每个 $x\in I_0$ 成立
```math
F(x,c)<0<F(x,d)\qquad(79)
```

$F$（作为二变量函数）的连续性蕴含：对每个 $x\in I_0$，函数 $F(x,\cdot)$ 在第二个变量上是连续的。

由 (79) 以及连续函数的 intermediate value property（介值性质）（我们在 §5.8 中已讨论）可知：对每个 $x\in I_0$，至少存在一个值 $y\in(c,d)$ 使 $F(x,y)=0$。

此外，由于 $F(x,\cdot)$ 也递增，此 $y$ 值唯一。

我们把 $y$ 对 $x$ 的这种依赖关系写作 $y=\varphi(x)$，从而找到了一个函数 $\varphi$，使对每个 $x\in I_0$ 成立
```math
F(x,\varphi(x))=0\qquad(80)
```
且
```math
c<\varphi(x)<d.\qquad(81)
```

我们现在证明 $\varphi$ 具有定理结论中宣称的所有其余性质。

显然 $\varphi(x_0)=y_0$，且对每个 $x\in I_0$ 有 $(x,\varphi(x))\in D$。

接下来检验 $\varphi$ 在 $I_0$ 上连续。

首先由 (81) 观察知：若 $x_1,x_2\in I_0$，则 $|\varphi(x_1)-\varphi(x_2)|\lt d-c$。

矩形 $N$ 本来可以取到任意小——更小的矩形可能导出更短的区间 $I_0$。

因此，若 $x_1$ 是 $I_0$ 中任意一点而 $\varepsilon>0$，我们可以把先前在 $x_1$ 的一个邻域 $I_1\subset I_0$ 上所用的同一论证应用于 $d_1-c_1<\varepsilon$。

在图 12.7 中，我们把以 $(x_0,y_0)$ 为中心的矩形 $I_0\times J$ 叠加到了图 12.6 之上。

结果是：在 $I_1$ 上 $|\varphi(x)-\varphi(x_1)|<\varepsilon$。

但这蕴含 $\varphi$ 在 $x_1$ 处连续；又因 $x_1$ 是 $I_1\subset I_0$ 中任意一点，$\varphi$ 在 $I_0$ 上连续。

剩下来需证明 $\varphi$ 在 $I_0$ 上连续可微，且所给的 $\varphi'$ 公式成立。

设 $x,x+h\in I_0$；由于 $\varphi$ 的图包含于矩形 $N$ 中，以 $(x,\varphi(x))$ 与 $(x+h,\varphi(x+h))$ 为端点的线段 $L$ 位于 $N$ 之内。

<span style="color:#7f8c8d">书页 510 · §12.6 Implicit Function Theorems（隐函数定理）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 例 12.41、12.42 在敲黑板：隐函数定理只保证"局部"解，绝不含"全局"。$F=x^2-y^4$ 在原点 $F_2=0$——正是正则条件失灵之点，原点附近反而解不出，而离原点稍远一切正常。这教你两点：其一，正则条件是"点态"的，不同点各有自己的邻域、彼此独立；其二，"能不能解"与"解长什么样"是两码事。折射到例 12.39 的 $y^2=x$：在 $(0,0)$ 处 $F_2=0$ 且曲线带尖，$y$ 在此分叉成 $\pm\sqrt{x}$ 两枝，故原点处不能作为光滑函数解出。再看球面 $x^2+y^2+z^2=9$：南北两极恰是 $F_3=0$ 的水平切点，所以极点邻域内 $z$ 无法被光滑表示为 $x,y$ 的函数。这构成一种「分叉/裁剪」直觉——解是局部的枝叶而非全局的树干，正则条件就是判断某根枝条是否"结实"的探针。

---


> <span style="color:#7f8c8d;">图 12.7 展示的是证明中矩形 $I_0\times J$ 的构造。</span>

由 mean value theorem（中值定理）（定理 12.35）知，存在 $(\xi,\eta)\in L$ 使得
```math
F(x+h,\varphi(x+h))-F(x,\varphi(x))=F_1(\xi,\eta)h+F_2(\xi,\eta)\big[\varphi(x+h)-\varphi(x)\big].
```

但 $F(x+h,\varphi(x+h))=F(x,\varphi(x))=0$，故
```math
F_1(\xi,\eta)h+F_2(\xi,\eta)\big[\varphi(x+h)-\varphi(x)\big]=0.
```

于是，若 $F_2(\xi,\eta)\neq 0$，我们可写出
```math
\frac{\varphi(x+h)-\varphi(x)}{h}=-\frac{F_1(\xi,\eta)}{F_2(\xi,\eta)}.\qquad(82)
```

由于 $F_2$ 在 $(x,\varphi(x))$ 的某个邻域内永不取零，故 (82) 在该邻域内成立。

当 $h\to 0$ 时，(82) 左端趋于 $\varphi'(x)$，$(\xi,\eta)$ 趋于 $(x,\varphi(x))$，而凭借 $F_1$ 与 $F_2$ 的连续性，(82) 右端趋于
```math
-\frac{F_1(x,\varphi(x))}{F_2(x,\varphi(x))},
```
正如所要证明的。$\blacksquare$

> [example]<span style="color:#c0392b">例 12.41</span>

> <span style="color:#7f8c8d;">TBB §12.6, p.510</span>

例 $F(x,y)=x^2-y^4$ 与 $(x_0,y_0)=(1,1)$ 说明了如下事实：尽管存在一个在 $x_0=1$ 的邻域内成立的解，却在过大的区间上不可能存在解。

事实上，在任何一个包含 $x=0$ 的区间 $I_0$ 上，解均不存在。$\blacksquare$

> [example]<span style="color:#c0392b">例 12.42</span>

我们回到例 12.39：$F(x,y)=y^2-x=0$。

此处 $F_1(x,y)=-1$，$F_2(x,y)=2y$。

只要 $y\neq 0$，定理 12.40 的假设便得到满足。

若 $(x_0,y_0)=(4,2)$，则所得函数为 $\varphi(x)=\sqrt{x}$，且 $\varphi'(x)=1/(2y)$。

在此情形，区间 $I_0$ 可取为任意包含 $x_0=4$ 但不包含 $0$ 的区间。$\blacksquare$<span style="color:#7f8c8d">书页 511 · §12.6 Implicit Function Theorems（隐函数定理）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定理 12.44 是定理 12.40 的 $n$ 维翻版：把 $F(x,y)=0$ 换成 $F(x_1,\dots,x_n,z)=0$，把孤立点 $x_0$ 换成向量 $\mathbf{x}_0$。关键改动只有一个——正则条件从 $F_2\neq 0$ 变成 $F_{n+1}\neq 0$，即"沿要解出的那个变量的方向"必须非退化。这不难理解：现在要解的"主角"是 $z$，自然看的变化率是 $\partial F/\partial z$。证明几乎原封不动：先在 $z$ 方向用介值+单调夹出唯一的 $z=\varphi(x_1,\dots,x_n)$，再用中值定理线性化。这里想你留意"脚手架"：你在离散数学里早已熟悉"把单个对象升级为多元"的模式（向量不过是点的推广），多元偏导公式 $\varphi_i=-F_i/F_z$ 形如单变量的 $-\frac{F_1}{F_2}$，只是下标"蜕化"而已。$n=2$ 的证明就是"两页纸复读机"，一般 $n$ 没有新想法——这正是分析学里"记号麻烦、思想朴素"的典型。

---


**习题**

> <span style="color:#7f8c8d;">TBB §12.6, p.511</span>

12.6.1 证明方程 $x^2y^2 + 2e^{xy} - 4 - 2e^2 = 0$ 可以在点 $x=1$（此时 $y(1)=2$）的邻域内将 $y$ 表示为 $x$ 的函数。并计算当 $x=1$ 时的 $\dfrac{dy}{dx}$。

12.6.2 用初等微积分中惯用的隐微分（implicit differentiation）方法完成习题 12.6.1。（在那里人们通常直接假设解的存在性。）

<span style="color:#7f8c8d">书页 511 · §12.6 Implicit Function Theorems（隐函数定理）</span>

**12.6.2 多变量情形（Several-Variable Case）**：定理 12.40 可以推广到涉及更多变量的情形。考虑三个变量的一个方程。我们希望在点 $(x_0, y_0)$ 的某个邻域内，将方程
```math
F(x, y, z) = 0
```
对于 $z$ 求解为 $x$ 与 $y$ 的函数。与前面一样，解应当是一个函数 $z = \varphi(x, y)$，使得对那个邻域中的所有 $(x, y)$ 都有
```math
F(x, y, \varphi(x, y)) = 0.
```

[example] **例 12.43**：考虑方程
```math
x^2 + y^2 + z^2 - 9 = 0. \tag{83}
```

> <span style="color:#7f8c8d;">TBB §12.6, p.511</span>

方程 (83) 可以轻松解开，把其中某一变量用其余变量来表示。于是
```math
z = \pm\sqrt{9 - x^2 - y^2} \tag{84}
```
就在 $x^2 + y^2 \le 3$ 时将 $z$ 表示为 $x$ 与 $y$ 的函数。正如我们在一元情形所看到的那样，在圆盘 $x^2 + y^2 \le 9$ 上 $z$ 并不是 $x$ 与 $y$ 的函数，因为 $z$ 的值并不能由方程 (84) 唯一确定。尽管如此，若 $(x_0, y_0)$ 是该圆盘内部的点，而 $z_0$ 是使得 (83) 成立的那些值之一，那么在 $\mathbb{R}^2$ 中 $(x_0, y_0)$ 存在一个邻域 $I$，使得方程 (84) 中的某个选择在该邻域内把 $z$ 表示为关于 $(x, y)$ 的连续函数。$\blacksquare$

下面的定理 12.44 是在处理多于两个变量的一个方程时与定理 12.40 相应的版本。我们把定理陈述成针对 $n+1$ 个变量的情形。

### 定理 12.44

> <span style="color:#7f8c8d;">TBB §12.6, p.511</span>

设 $F$ 在开集 $D \subset \mathbb{R}^{n+1}$ 上具有连续一阶偏导数。设 $\mathbf{x}_0 = (x_{10}, x_{20}, \ldots, x_{n0}, z_0) \in D$。假设
```math
F(x_{10}, x_{20}, \ldots, x_{n0}, z_0) = 0
```
且
```math
F_{n+1}(x_{10}, x_{20}, \ldots, x_{n0}, z_0) \ne 0.
```
那么存在 $z_0$ 的一个邻域 $J_0 \subset \mathbb{R}$，以及 $(x_{10}, x_{20}, \ldots, x_{n0})$ 的一个邻域 $I_0 \subset \mathbb{R}^n$，并且存在定义在 $I_0$ 上的唯一函数 $\varphi$，使得
```math
z_0 = \varphi(x_{10}, x_{20}, \ldots, x_{n0})
```
且
```math
F(x_1, \ldots, x_n, \varphi(x_1, \ldots, x_n)) = 0
```

<span style="color:#7f8c8d">书页 512 · §12.6 Implicit Function Theorems（隐函数定理）</span>

对所有 $(x_1, \ldots, x_n) \in I_0$ 成立。此外，函数 $\varphi$ 关于每个变量 $(x_1, \ldots, x_n)$ 都具有连续偏导数，并且对每个 $i = 1, \ldots, n$ 以及对所有 $(x_1, \ldots, x_n) \subset I_0$，有
```math
\varphi_i(x_1, \ldots, x_n) = -\frac{F_i(x_1, \ldots, x_n, z)}{F_{n+1}(x_1, \ldots, x_n, z)}. \tag{85}
```

[proof] **证明**：注意到通过令 $z = \varphi(x_1, \ldots, x_n)$，一旦我们指定了 $z_0$ 的值，就已在 $(x_{10}, \ldots, x_{n0})$ 的一个邻域上，把变量 $z$ 显式地表示成 $x_1, \ldots, x_n$ 的连续可微函数。

> <span style="color:#7f8c8d;">TBB §12.6, p.512</span>

我们对 $n=2$ 的情形来证明定理 12.44。一般情形的证明并不需要新的想法，只是记号较为繁琐，图形也不那么容易想象。请注意我们证明背后的想法与定理 12.40 的证明之间的相似性。为简化记号，我们把讨论中的那个点记为 $(x_0, y_0, z_0)$。我们首先获得定理中提到的邻域 $J_0$ 与 $I_0$。

假设 $F_3(x_0, y_0, z_0) > 0$。[情形 $F_3(x_0, y_0, z_0) < 0$ 是类似的。]由于 $F_3$ 在 $D$ 上连续，存在一个中心为 $(x_0, y_0, z_0)$、棱边平行于坐标轴的开长方体盒子 $A$，使得 $F_3$ 在 $A$ 上取正值。设 $2c$ 为该盒子的高。于是 $F(x_0, y_0, \cdot)$ 是区间 $[z_0 - c, z_0 + c]$ 上 $z$ 的一个增函数。由于由假设有 $F(x_0, y_0, z_0) = 0$，我们有
```math
F(x_0, y_0, z_0 - c) < 0 < F(x_0, y_0, z_0 + c).
```

因为由假设 $F$ 在 $D$ 上具有连续的一阶偏导数，所以 $F$ 在 $D$ 上连续。因此我们可以得到正数 $a$ 和 $b$，使得当 $|x - x_0| < a$ 且 $|y - y_0| < b$ 时，有
```math
F(x, y, z_0 - c) < 0 \ \text{与} \ F(x, y, z_0 + c) > 0.
```
我们总可以选取 $a$ 与 $b$ 足够小，使得盒子
```math
\mathbf{B} = \{(x, y, z) : |x - x_0| < a,\ |y - y_0| < b,\ |z - z_0| < c\}
```
被包含在 $A$ 中。因此所需的邻域为
```math
\mathbf{I}_0 = \{(x, y) : |x - x_0| < a,\ |y - y_0| < b\}
```
与
```math
J_0 = \{z : |z - z_0| < c\}.
```

接下来我们构造函数 $\varphi$。设 $(x, y) \in \mathbf{I}_0$。由于 $F_3 > 0$ 在集合 $B = \mathbf{I}_0 \times J_0$ 上成立，故 $F(x, y, z)$ 是区间 $[z_0 - c, z_0 + c]$ 上 $z$ 的一个连续增函数。它在 $(x, y, z_0 + c)$ 处取正值，在 $(x, y, z_0 - c)$ 处取负值，因此在 $[z_0 - c, z_0 + c]$ 中存在唯一的 $z$ 值使得 $F(x, y, z) = 0$。我们把该 $z$ 值记为 $\varphi(x, y)$。于是我们就在 $\mathbf{I}_0$ 上确定了函数 $\varphi$。

现在我们证明 $\varphi$ 具有所期望的性质。如同我们在定理 12.40 中所做的那样来证明连续性。设 $(x_1, y_1) \in \mathbf{I}_0$，并设 $\varepsilon > 0$。我们可以假设 $\varepsilon \le c$。设 $z_1 = \varphi(x_1, y_1)$。则 $F(x_1, y_1, z_1) = 0$。把先前构造盒子 $B$ 时所用的论证再应用一次，我们得到（可能更小的）一个以 $(x_1, y_1, z_1)$ 为中心的盒子 $\mathbf{B}_1$，其高度 $2c_1$ 可以任意小。取 $2c_1 < \varepsilon$，并令 $B_1 = \mathbf{I}_1 \times J_1$，其中
```math
J_1 = [z_1 - c_1, z_1 + c_1]
```

<span style="color:#7f8c8d">书页 513 · §12.6 Implicit Function Theorems（隐函数定理）</span>

> <span style="color:#7f8c8d;">TBB §12.6, p.513</span>

我们设
```math
I_1 = \{(x,y) : |x-x_1| < a_1,\ |y-y_1| < b_1\}.
```

先前针对 $B_1$ 的论证给出一个定义在 $I_1$ 上的函数 $g$，使得 $F(x,y,g(x,y))=0$ 在 $I_1$ 上成立，并且 $z_1-c_1 < g(x,y) < z_1+c_1$ 在 $I_1$ 上也成立。

于是，若 $(\xi,\eta)\in I_1$，则
```math
|g(\xi,\eta)-g(x_1,y_1)| < 2c_1 < \varepsilon.
```

由此得出 $g$ 在 $(x_1,y_1)$ 处是连续的。

由于 $g$ 是从 $F$ 里以与 $\varphi$ 完全相同的方式获得的，且满足条件的值唯一，所以 $g=\varphi$ 在 $I_1$ 上成立。

因此 $\varphi$ 在 $(x_1,y_1)$ 处连续。

既然 $(x_1,y_1)$ 是 $I_0$ 中的任意一点，故 $\varphi$ 在 $I_0$ 上是连续的。

最后，我们验证偏导数公式 (85) 成立。

我们仅为 $\varphi_1$ 给出证明；$\varphi_2$ 的证明完全相同。

把函数 $F(\cdot\,,\,y,\,\cdot)$ 视为以 $y$ 固定、关于 $x$ 与 $z$ 的函数。

记 $z+k = \varphi(x+h,y)$。

（这里我们当然假定 $(x,y)\in I_0$ 且 $(x+h,y)\in I_0$。）

由于 $\varphi$ 在 $I_0$ 上连续，我们还可以假定 $z+k \in J_0$。

此时
```math
F(x,y,z) = 0 = F(x+h,y,z+k).
```

根据 mean value theorem（中值定理）（定理 12.35）
```math
0 = F(x+h,y,z+k) - F(x,y,z) = F_1(\xi,y,\zeta)\,h + F_3(\xi,y,\zeta)\,k, \tag{86}
```
其中 $\xi$ 介于 $x$ 与 $x+h$ 之间，$\zeta$ 介于 $z$ 与 $z+k$ 之间。

于是
```math
\varphi_1(x,y) = \lim_{h\to 0}\frac{\varphi(x+h,y)-\varphi(x,y)}{h} = \lim_{h\to 0}\frac{(z+k)-z}{h} = \lim_{h\to 0}\frac{k}{h}.
```

由 (86)，最后的这个极限就是
```math
\lim_{h\to 0}\left(-\frac{F_1(\xi,y,\zeta)}{F_3(\xi,y,\zeta)}\right) = -\frac{F_1(x,y,z)}{F_3(x,y,z)}
```
这是因为当 $h\to 0$ 时 $(\xi,\zeta)\to (x,z)$，而由假设函数 $F_1$ 与 $F_3$ 是连续的。$\blacksquare$

> [example]<span style="color:#c0392b">例 12.45</span>

> <span style="color:#7f8c8d;">TBB §12.6, p.513</span>

回到例 12.43，那里有
```math
x^2+y^2+z^2-9 = 0,
```
我们求出
```math
F_1(x,y,z)=2x,\qquad F_2(x,y,z)=2y,\qquad F_3(x,y,z)=2z.
```

当 $z\neq 0$ 且 $x^2+y^2+z^2\leq 9$ 时，有 $F_3(x,y,z)\neq 0$，于是定理 12.44 的假设得到满足。

给定 $(x_0,y_0,z_0)$ 使得 $x_0^2+y_0^2+z_0^2\leq 9$ 且 $z_0\neq 0$，则存在 $(x_0,y_0)$ 的一个 neighborhood（邻域）$N$ 以及定义在该邻域上的一个函数 $\varphi$，使得
```math
F(x,y,\varphi(x,y))=0.
```

<span style="color:#7f8c8d">书页 514 · §12.6 Implicit Function Theorems（隐函数定理）</span>

> <span style="color:#7f8c8d;">TBB §12.6, p.514</span>

或等价地，
```math
x^2+y^2+[\varphi(x,y)]^2-9 = 0.
```

函数 $\varphi$ 的偏导数对所有 $(x,y)\in N$ 由
```math
\varphi_1(x,y)=-\frac{x}{z}\qquad\text{及}\qquad \varphi_2(x,y)=-\frac{y}{z}
```
给出。

事实上，我们知道
```math
\varphi(x,y)=\sqrt{9-x^2-y^2}\quad\text{或}\quad \varphi(x,y)=-\sqrt{9-x^2-y^2}
```
具体取哪一个，取决于 $z_0>0$ 还是 $z_0<0$。$\blacksquare$

> 习题 12.6.3–12.6.6 属于非必需习题，此处跳过：12.6.3 要求比较本节定理 12.44 与上一节定理 12.40 的证明；12.6.4 要求证明对一般 $n\geq 2$ 的定理 12.44；12.6.5 涉及链式法则在求积恒等式上的应用；12.6.6 预告了用度量空间方法证明隐函数定理的习题 13.11.3。

> [definition]<span style="color:#00838f">12.6.3 联立方程组（Simultaneous Equations）

> <span style="color:#7f8c8d;">TBB §12.6, p.514</span>

在上一小节中，我们处理的是含多个变量的单个方程，例如 $F(x,y,z)=0$。

我们找到了在点 $(x_0,y_0)$ 的一个邻域中能够就 $y$ 和 $x$ 解出 $z$ 的条件，从而得到在该邻域上连续可微的函数 $z=\varphi(x,y)$。

现在我们转向一种经常出现的情形，其中涉及若干个 simultaneous equations（联立方程），例如在 $m+n$ 个变量中有 $m$ 个方程。

> [example]<span style="color:#c0392b">例 12.46</span>

> <span style="color:#7f8c8d;">TBB §12.6, p.514</span>

这里有两个方程
```math
x = r\cos\theta,\qquad y = r\sin\theta
```
涉及四个变量 $x,y,r,\theta$。

这些方程可以被看成给出从极坐标到直角坐标的坐标系的变换。

另外，我们也可以把它们看成显式地以 $r$ 和 $\theta$ 表示 $x$ 和 $y$，或者隐式地以 $x$ 和 $y$ 表示 $r$ 和 $\theta$。

第三种视角是把它们看成定义一个从 $\mathbb{R}^2$ 到 $\mathbb{R}^2$ 的映射：$F(r,\theta)=(r\cos\theta,\ r\sin\theta)$。

在以上每种视角中，都有理由希望把 $r$ 和 $\theta$ 表示为 $x$ 和 $y$ 的函数。

第一种诠释将供我们从直角坐标变换到极坐标时所用的方程。

第二种诠释只是给出 $r$、$\theta$ 关于 $x$、$y$ 的一个显式表示。

第三种诠释则给出 $F$ 的一个 inverse function（反函数）：一个使得 $G(x,y)=(r,\theta)$ 的函数 $G$。<span style="color:#7f8c8d">书页 515 · §12.6 Implicit Function Theorems（隐函数定理）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 一旦进入联立方程组，正则条件的化身就变成"雅可比行列式非零"。例 12.47 解两个线性方程，靠的是系数行列式 $A_1B_2-A_2B_1\neq 0$；写成 $F,G$ 后，正是 $\frac{\partial(F,G)}{\partial(u,v)}$——雅可比行列式。从 Strang 的线性代数看，这是在说：在参考点处，$F,G$ 对 $(u,v)$ 的线性化是一个可逆矩阵。可逆矩阵 $\iff$ 方程组 $Ju=T$ 有唯一解，而这里的非线性方程组"遗传"了这条局部结论：可逆的线性化 = 局部可解。这正是第一性原理：微分把非线性映射局部"读成"线性映射，于是线性代数里"可逆"的整套理论（秩、行列式、逆矩阵）顺理成章地翻译成微分几何里的局部可逆性。定理 12.48 那串复杂的 $\varphi_1=-\frac{1}{|J|}\frac{\partial(F,G)}{\partial(x,v)}$，本质就是克莱姆（Cramer）法则的微分翻版。

---


你可能记得，当 x 与 y 不同时为零时，下列方程即可完成这一目标：

```math
r = \sqrt{x^2 + y^2},\qquad \theta = \arctan\frac{y}{x}.
```
$\blacksquare$

[example] 例 12.47
> <span style="color:#7f8c8d;">TBB §12.6, p.515</span>
考虑方程组（system）

```math
\begin{cases}
A_1 u + B_1 v + C_1 = 0,\\
A_2 u + B_2 v + C_2 = 0,
\end{cases} \tag{87}
```

其中各 A、B、C 均为 x 与 y 的函数。这里我们有四个变量 x、y、u、v 上的两个方程。

用初等代数（elementary algebra）的想法，只要行列式

```math
|J| = \begin{vmatrix} A_1 & B_1 \\ A_2 & B_2 \end{vmatrix} = A_1 B_2 - A_2 B_1 \neq 0, \tag{88}
```

我们就可以把这些方程“解出” u 与 v，以 x 与 y 表示之。方程 (87) 具有如下形式

```math
F(x, y, u, v) = 0,\qquad G(x, y, u, v) = 0. \tag{89}
```

注意

```math
\frac{\partial F}{\partial u} = A_1,\quad \frac{\partial F}{\partial v} = B_1,\quad \frac{\partial G}{\partial u} = A_2,\quad \frac{\partial G}{\partial v} = B_2.
```

条件 (88) 遂化为

```math
|J| = \begin{vmatrix} \dfrac{\partial F}{\partial u} & \dfrac{\partial F}{\partial v} \\[4pt] \dfrac{\partial G}{\partial u} & \dfrac{\partial G}{\partial v} \end{vmatrix} \neq 0. \tag{90}
```
$\blacksquare$

(90) 中的行列式称为雅可比行列式（Jacobian determinant），即雅可比矩阵

```math
J =
\begin{pmatrix}
\dfrac{\partial F}{\partial u} & \dfrac{\partial F}{\partial v} \\[4pt]
\dfrac{\partial G}{\partial u} & \dfrac{\partial G}{\partial v}
\end{pmatrix}
```

的行列式。它只是本节及数学其他领域中出现的众多雅可比行列式之一。我们常把雅可比行列式写成

```math
\frac{\partial(F, G)}{\partial(u, v)}.
```

我们关心的是：何时能够找到例 12.46 和例 12.47 所启示的那类解，以及如何求出所得函数的偏导数（例如例 12.47 中的 $\partial u/\partial x$、$\partial u/\partial y$、$\partial v/\partial x$、$\partial v/\partial y$）。

我们处理四个变量上一对方程（a pair of simultaneous equations）的情形，因为它能代表一般情况。

<span style="color:#7f8c8d">书页 516 · §12.6 Implicit Function Theorems（隐函数定理）</span>

[theorem] 定理 12.48
> <span style="color:#7f8c8d;">TBB §12.6, p.516</span>
设 F 与 G 在开集 $D \subset \mathbb{R}^4$ 上具有连续的一阶偏导数，又设 $p_0 = (x_0, y_0, u_0, v_0) \in D$，且

```math
F(x_0, y_0, u_0, v_0) = 0,\qquad G(x_0, y_0, u_0, v_0) = 0. \tag{91}
```

设

```math
|J| =
\frac{\partial(F, G)}{\partial(u, v)} =
\begin{vmatrix}
\dfrac{\partial F}{\partial u} & \dfrac{\partial F}{\partial v} \\[4pt]
\dfrac{\partial G}{\partial u} & \dfrac{\partial G}{\partial v}
\end{vmatrix}.
```

假设 $|J|$ 在 $p_0$ 处不为零。则存在 $(x_0, y_0)$ 的邻域 $I_0$ 以及 $(u_0, v_0)$ 的邻域 $J_0$，使得

(i) 对每个 $(x, y) \in I_0$，存在唯一的 $(u, v) \in J_0$，使方程 (91) 在 $(x, y, u, v)$ 处成立。这一对应关系通过在 $I_0$ 上定义 u 与 v 为函数

```math
u = \varphi(x, y), \qquad v = \psi(x, y).
```

(ii) 函数 $\varphi$ 与 $\psi$ 在 $I_0$ 上有连续的偏导数，由下列公式给出：

```math
\frac{\partial \varphi}{\partial x} = -\frac{1}{|J|}\frac{\partial(F, G)}{\partial(x, v)},\qquad
\frac{\partial \psi}{\partial x} = -\frac{1}{|J|}\frac{\partial(F, G)}{\partial(u, x)},
```

```math
\frac{\partial \varphi}{\partial y} = -\frac{1}{|J|}\frac{\partial(F, G)}{\partial(y, v)},\qquad
\frac{\partial \psi}{\partial y} = -\frac{1}{|J|}\frac{\partial(F, G)}{\partial(u, y)}.
```

[proof] 证明
> <span style="color:#7f8c8d;">TBB §12.6, p.516</span>
我们将定理 12.44 应用两次，第一次把 v 作为 x、y、u 的函数求出，然后又把 u 作为 x 与 y 的函数求出。由于 $|J| \neq 0$ 在 $p_0$ 处成立，故 $\partial F/\partial v$ 与 $\partial G/\partial v$ 中至少有一个在 $p_0$ 处异于零。我们可以假设 $F_4 = \partial F/\partial v \neq 0$ 在 $p_0$ 处成立；若 $\partial G/\partial v \neq 0$ 在 $p_0$ 处成立，论证是类似的。

现在对方程 $F(x, y, u, v) = 0$ 应用定理 12.44。可得一个函数 $v = g(x, y, u)$，它在 $(x_0, y_0, u_0)$ 的一个邻域内有定义，使得在该邻域上 $F(x, y, u, g(x, y, u)) = 0$。

接下来我们考察函数 G。设

```math
H(x, y, u) = G(x, y, u, g(x, y, u)).
```

于是我们已把四变量函数 G 替换成三变量函数 H。我们的任务是把这一方程解出 u，以 x 与 y 表示。

为此，我们再一次使用定理 12.44。为了检验定理 12.44 适用，必须证明 $H_3$ 在 $(x_0, y_0, u_0)$ 处不为零。应用链式法则（chain rule），可得

```math
H_3 = G_3 + G_4\, g_3 = G_3 - G_4 \frac{F_3}{F_4}
    = \frac{G_3 F_4 - G_4 F_3}{F_4}
    = -\frac{|J|}{F_4}. \tag{92}
```

现在 $|J|$ 与 $F_4$ 在 $p_0$ 的某个邻域内异于零。因此 $H_3$ 在该邻域内是有限的且非零。对方程 $H(x, y, u) = 0$ 应用定理 12.44，可得一个解

```math
u = \varphi(x, y) = g(x, y, \psi(x, y)).
```<span style="color:#7f8c8d">书页 517 · §12.6 Implicit Function Theorems（隐函数定理）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 反函数定理是隐函数定理的"免费午餐"——定理 12.50 的证明一句话就交代：令 $F=f(u,v)-x$、$G=g(u,v)-y$，再把定理 12.48 整套搬过来即可。哲学上一针见血：所谓"给定目标 $(x,y)$ 反解 $(u,v)$"，无非是"同时满足两个方程"的特例。这与你在逻辑/离散数学里熟悉的化归（reduction）同源——新问题是老问题的实例。历史核对：隐函数与反函数定理的现代严格形式都由 Ulisse Dini（1845–1918）于 1877 年系统证明，故常冠以"Dini 定理"；Cauchy 更早处理过隐式求导但不如其严格。读懂这个"化归视角"很划算：已证好的定理 12.48 一复用，就白得整套反函数理论，无需重新发明。此处正则条件自动变成"雅可比行列式 $\det J\neq 0$"，与隐的情形丝丝入扣。

---


在 $(x_0, y_0)$ 的某个邻域（neighborhood）内，函数 $u = \varphi(x, y)$ 与 $v = \psi(x, y)$ 是方程组
```math
F(x, y, u, v) = 0,\qquad G(x, y, u, v) = 0
```
的解，其中 $(x, y)$ 取自 $(x_0, y_0)$ 的某个邻域 $I_0$，而 $(u, v)$ 取自 $(u_0, v_0)$ 的某个邻域 $J_0$。由定理 12.44 我们确知 $\varphi$ 与 $\psi$ 具有连续的一阶偏导数（continuous first partials）。余下的工作是验证为这些偏导数推出的公式。

为检验 $\varphi_1$ 的公式，回顾 $u = \varphi(x, y)$ 是方程 $H(x, y, u) = 0$ 的解。利用 (92)，我们得到
```math
\varphi_1 = -\frac{H_1}{H_3}
          = -\frac{G_1 + G_4\, g_1}{-\dfrac{|J|}{F_4}}
          = -\,\frac{G_1 - G_4\left(-\dfrac{F_1}{F_4}\right)}{-\dfrac{|J|}{F_4}}
          = -\frac{F_4 G_1 - G_4 F_1}{|J|}
          = -\frac{1}{|J|}\frac{\partial(F, G)}{\partial(x, v)}.
```
其余偏导数的公式可类似地得到。$\blacksquare$

[note] 注
> <span style="color:#7f8c8d;">TBB §12.6, p.517</span>
我们仅就四个变量上的两个方程陈述了定理 12.48。上一节的定理 12.44 处理的则是若干变量上的单个方程。涉及 $n + m$ 个变量上 $m$ 个方程的一般性定理，其思路与此类似。这些 $m$ 个方程中典型的一个具有如下的形式
```math
F^i(x_1, \ldots, x_n, u_1, \ldots, u_m) = 0.
```
（这里用上标（superscript）来标示函数，以免把方程的编号与偏导数相混淆——若用下标就可能产生这种歧义。）我们假设 $F^i$ 在 $\mathbb{R}^{m+n}$ 中的某个区域内具有连续的偏导数，并且相应的雅可比行列式
```math
\frac{\partial(F^1, \ldots, F^m)}{\partial(u_1, \ldots, u_m)}
```
不为零。那么所得的结论正是定理 12.48 结论的显然类比。

[exercise] 习题
> <span style="color:#7f8c8d;">TBB §12.6, p.517</span>
12.6.7 验证定理 12.48 中那些在正文里未予验证的偏导数公式。

12.6.4 反函数定理（Inverse Function Theorem）

现在我们应用定理 12.48 来获得一个关于映射（mapping）的反函数的定理。设有如下形式的方程
```math
x = f(u, v),\qquad y = g(u, v),
```

<span style="color:#7f8c8d">书页 518 · §12.6 Implicit Function Theorems（隐函数定理）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 例 12.49 用 $f(x)=x^2$ 点破"局部逆 vs 全局逆"：$g(u)=\sqrt{u}$ 满足 $f\circ g=\mathrm{id}$（在 $u\ge 0$）却只是单侧逆，而 $g\circ f=\sqrt{x^2}=|x|$ 在整个 $\mathbb R$ 上并非恒等。根源是 $f$ 在 $\mathbb R$ 上非单射。这是你把离散数学 6.042J 的集合论迁移进分析：函数有逆 $\iff$ 它是双射 $\iff$ 既是单射又是满射；若 $f(I)=J$ 且 $f$ 在 $I$ 上单射，则 $f$ 限制在 $I$ 上有反函数。TBB 定理 12.50 恰只保证"某个邻域上的单射性"——雅可比行列式非零在局部逼出可逆线性化、因而是双射，从而局部单射成立。这与全局形成对照：例 12.51 的极坐标变换在 $r\neq 0$ 时处处雅可比行列式非零，却在整个平面、甚至同时含 $(4,0)$ 与 $(4,2\pi)$ 的集合 $D$ 上失败——因为 $r,\theta$ 并非全局单射。结论"局部很强、全局很脆"，正是反函数定理的宿命。

---


其中 $f$ 与 $g$ 定义在开集 $D \subset \mathbb{R}^2$ 上。这些方程确定了一个函数 $T : D \to \mathbb{R}^2$，$T(u, v) = (x, y)$。我们常把这样的函数称为 mapping 或 transformation（变换）。若我们能针对属于某个集合 $D_0 \subset \mathbb{R}^2$ 的 $(x, y)$ 之值把这些方程解出 $u$ 与 $v$，
```math
u = \varphi(x, y), \qquad v = \psi(x, y), \tag{93}
```
则这就确定了映射 $S : D_0 \to \mathbb{R}^2$，使得 $T \circ S$ 在 $D_0$ 上是恒等映射（identity）。因此 $S$ 与 $T$ 在某种意义上互为反函数。在把 $S$ 与 $T$ 之间的这种互逆关系表述精确时，必须格外小心。问题出在 $S$ 与 $T$ 的定义域上——即 $S \circ T$ 与 $T \circ S$ 分别成为恒等映射的集合。

[example] 例 12.49
> <span style="color:#7f8c8d;">TBB §12.6, p.518</span>
考虑定义在 $\mathbb{R}$ 上的单变量函数 $u = f(x) = x^2$。若令 $g(u) = \sqrt{u}\ (u \geq 0)$，则
```math
(f \circ g)(u) = (\sqrt{u})^2 = u,
```
故 $f \circ g$ 在集合 $\{u : u \geq 0\}$ 上是恒等映射。但
```math
(g \circ f)(x) = \sqrt{x^2} = |x|,
```
故 $g \circ f$ 在集合 $\{x : x \geq 0\}$ 上是恒等映射，但在整个 $\mathbb{R}$ 上并不是。由于 $f$ 在 $\mathbb{R}$ 上不是单射（one-to-one），必须把它的定义域缩减成某个在其上 $f$ 为单射的更小的集合。若这一缩减操作得当，$f$ 确实就有反函数。假如我们事先指定某个 $x_0 \neq 0$，那么我们就能找到一个 $x_0$ 的邻域 $I$ 以及 $u_0 = f(x_0)$ 的邻域 $J$，使得 $f(I) = J$，并且 $f$ 在 $I$ 上是单射。$\blacksquare$

定理 12.50 给出一组条件，在此条件下，对从 $\mathbb{R}^2$ 到 $\mathbb{R}^2$ 的映射存在这样的局部逆（local inverse）。

[theorem] 定理 12.50（反函数定理）
> <span style="color:#7f8c8d;">TBB §12.6, p.518</span>
设 $f$ 与 $g$ 在开集 $D \subset \mathbb{R}^2$ 上具有连续的一阶偏导数。设 $(u_0, v_0) \in D$，且设
```math
x_0 = f(u_0, v_0),\qquad y_0 = g(u_0, v_0).
```
再假设
```math
|J| = \frac{\partial(f, g)}{\partial(u, v)} \neq 0 \quad \text{在} (u_0, v_0) \text{处}.
```
则存在 $(x_0, y_0)$ 的邻域 $I_0$ 与 $(u_0, v_0)$ 的邻域 $J_0$，使得对每个 $(x, y) \in I_0$，对应地存在唯一的 $(u, v) \in J_0$，满足
```math
x = f(u, v),\qquad y = g(u, v).
```
这一对应关系确定了从 $I_0$ 到 $J_0$ 的函数
```math
u = \varphi(x, y),\qquad v = \psi(x, y).
```<span style="color:#7f8c8d">书页 519 · §12.6 Implicit Function Theorems（隐函数定理）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 往深处看，反函数/隐函数定理与牛顿法共享同一根数学神经。牛顿法求 $F(x)=0$ 的根，迭代 $x_{k+1}=x_k-\frac{F(x_k)}{F'(x_k)}$；要在解附近收敛，前提是分母 $F'(x)\neq 0$——这恰好就是"正则条件"的重演。在数值分析与控制理论里，你"在线性化处解开一个非线性方程"的能力，正是局部可逆性的另一面：每步把曲线当直线（沿切线逼近），恰因雅可比/导数可逆。反观定理 12.50，我们也是"把映射局部当作可逆线性映射"才敢反解。直觉内核同一：非线性对象在一点被可逆线性化后，局部行为便忠实于这条切线。牛顿法的思想可上溯至 Isaac Newton 与 Joseph Raphson，而这一"在切点线性化求根/求逆"的策略贯穿你 CLRS 与 18.065 中的许多算法——从优化到根求解，正则性/可逆性与你今后会碰到的各种 Jacobian 类算法密不可分。


函数 $\varphi$ 与 $\psi$ 具有如下的连续偏导数（continuous partial derivatives）：

```math
\frac{\partial \varphi}{\partial x} = -\frac{1}{|J|}\frac{\partial g}{\partial v},\qquad
\frac{\partial \varphi}{\partial y} = -\frac{1}{|J|}\frac{\partial f}{\partial v},
```

```math
\frac{\partial \psi}{\partial x} = -\frac{1}{|J|}\frac{\partial g}{\partial u},\qquad
\frac{\partial \psi}{\partial y} = -\frac{1}{|J|}\frac{\partial f}{\partial u}.
```

[proof] 证明
> <span style="color:#7f8c8d;">TBB §12.6, p.519</span>
定理 12.50 只是定理 12.48 的一个特例（special case）。令

```math
F(x, y, u, v) = f(u, v) - x,\qquad G(x, y, u, v) = g(u, v) - y.
```

对定理 12.48 应用之后，我们便得到函数 $\varphi$ 与 $\psi$，以及这些偏导数的公式。例如，为求 $\partial \psi/\partial y$，我们只需利用定理 12.48 计算：

```math
\frac{\partial \psi}{\partial y}
= -\frac{1}{|J|}\frac{\partial(F, G)}{\partial(y, u)}
= -\frac{1}{|J|}
\begin{vmatrix}
\dfrac{\partial F}{\partial y} & \dfrac{\partial G}{\partial y} \\[4pt]
\dfrac{\partial F}{\partial u} & \dfrac{\partial G}{\partial u}
\end{vmatrix}
= -\frac{1}{|J|}
\begin{vmatrix}
0 & -1 \\[4pt]
\dfrac{\partial f}{\partial u} & \dfrac{\partial g}{\partial u}
\end{vmatrix}
= -\frac{1}{|J|}\frac{\partial f}{\partial u}.
```

其余的计算是类似的。$\blacksquare$

[example] 例 12.51
> <span style="color:#7f8c8d;">TBB §12.6, p.519</span>
考虑例 12.46 中的方程组：

```math
x = r\cos\theta,\qquad y = r\sin\theta.
```

这里的雅可比行列式是

```math
\begin{vmatrix}
\cos\theta & -r\sin\theta \\[4pt]
\sin\theta & r\cos\theta
\end{vmatrix}
= r(\cos^2\theta + \sin^2\theta) = r.
```

对于 $(r_0, \theta_0) \in \mathbb{R}^2$（其中 $r_0 \neq 0$），存在 $(r_0, \theta_0) \in \mathbb{R}^2$ 的一个邻域，在该邻域上此变换的逆（inverse）存在。在整个 $\mathbb{R}^2$ 上，甚至在任何一个同时包含点 $(4, 0)$ 与点 $(4, 2\pi)$ 的集合 $D$ 上，都没有逆，因为

```math
(4\cos 0, 4\sin 0) = (4\cos 2\pi, 4\sin 2\pi) = (4, 0).
```

在这些点上雅可比行列式并不等于零，但变换在 $D$ 上不是一对一（one-to-one）的。$\blacksquare$

<span style="color:#7f8c8d">书页 520 · §12.7 Functions From R → R^{m}（从 R 到 R^{m} 的函数）</span>

这里我们关心的是定义在 $\mathbb{R}$ 的某个子集上、取值于 $\mathbb{R}^m$（$m > 1$）的函数 $f$ 的可微性（differentiability）。设给定两个方程

```math
x = x(t),\qquad y = y(t) \qquad (a \le t \le b). \tag{94}
```

这些方程确定一个函数 $f : [a, b] \to \mathbb{R}^2$，其定义为

```math
f(t) = (x(t), y(t)).
```

在初等微积分（elementary calculus）中，我们常把方程组 (94) 视为一条曲线的参数表示（parametric representation）。当 $t$ 从 $a$ 移动到 $b$ 时，$f(t)$ 描出一条曲线。学生学到，在适当的假设下，我们可以通过计算

```math
\frac{dy}{dx} = \frac{y'(t)}{x'(t)}
```

来确定在点 $(x(t), y(t))$ 处切线的斜率（slope of the tangent line）。

在本节中，我们把函数 $f$ 仅仅看作一个从 $[a, b]$ 到 $\mathbb{R}^2$ 的函数。我们将用一个线性函数（linear function）来逼近 $f$ 的方式定义 $f$ 的可微性。我们在 $t$ 处对可微性的要求，与由 (94) 参数化地给出的曲线在 $(x(t), y(t))$ 处具有切线这一要求并不相同。（事实上，例 12.52 将表明：即使 $f$ 在 $t$ 处可微，曲线也未必有这样的切线。）

那么我们该如何定义 $f$ 的可微性呢？我们从前几节的内容中获取启示。我们希望在点 $t$ 的附近用一个线性函数 $T$ 去逼近 $f$。这种逼近应当足够好，其含义是：当 $t$ 接近 $t_0$ 时，$\|f(t) - T(t)\|$ 与 $t$ 和 $t_0$ 之间的距离相比是很小的。由于

```math
T(t_0 + h) - T(t_0) = T(h)
```<span style="color:#7f8c8d">书页 521 · §12.7 Functions From R→R^m（从 R 到 R^m 的函数）</span>

#### <span style="color:#2471a3">**[section]**</span> <span style="color:#c0392b">12.7 从 R 到 R^m 的函数（Functions From R→R^m）</span>



---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 全书进入向量值函数的第一道坎，是把一元可微定义里的绝对值换成了范数，形式上几乎一字不改。第一性原理在这里：可微性的本质不是"极限算得出来"，而是"函数被自己的最佳线性逼近以可忽略的误差夹住"——`|f(t+h)-f(t)-f'(t)h|/|h|→0` 里分子丈量"误差大小"、分母丈量"自变量走了多远"。当 f:ℝ→ℝ^m，分子 `f(t+h)-f(t)-T(h)` 从数变成向量，(95) 写不下去的唯一障碍就是"向量没有长度可谈"；你只需给向量配备范数这个"长度"，整条式子的骨架就原封不动立住了。这正是范数的第一性意义：它是朝圣高等数学的通用"尺子"，把"数的大小"升级为"向量/矩阵的大小"，从而让极限、连续、可微这些概念在任意维空间自动复活。它也是你在 §11.6 见过的等价范数的一次实战：在有限维 ℝ^m 上选哪种范数都不影响收敛（习题 12.8.1）。对智能学科，这像 CSAPP 里"对象的大小由你声明的类型决定"——范数就是你为误差指定的测量字长，换单位不换结论。

---


对于 linear functions（线性函数），我们可以把式 (94) 改写为如下形式
```math
\lim_{h\to 0}\frac{\|\mathbf{f}(t_0+h)-\mathbf{f}(t_0)-\mathbf{T}(h)\|}{|h|}=0.\qquad(95)
```

让我们回到本节开篇用过的熟悉情形 $m=2$：
```math
x=x(t),\qquad y=y(t)\qquad(a\le t\le b),
```
其中 $x$ 与 $y$ 都是 $[a,b]$ 上的 continuous functions（连续函数）。

正如我们已经提及的，这些方程通过
```math
\mathbf{f}(t)=(x(t),y(t))
```
定义了一个函数 $\mathbf{f}:[a,b]\to\mathbb{R}^2$。

我们希望按照一个与 (95) 类似的 criterion（准则）来定义 $\mathbf{f}$ 在一点 $t\in[a,b]$ 处的 differentiability（可微性）。

现在暂时假设 $x$ 与 $y$ 在 $t$ 处可微，令
```math
\mathbf{T}(h)=\big(x'(t),\,y'(t)\big)h.
```

于是 $\mathbf{f}(t+h)-\mathbf{f}(t)-\mathbf{T}(h)$ 变为
```math
\big(x(t+h)-x(t),\,y(t+h)-y(t)\big)-\big(x'(t)h,\,y'(t)h\big)=\big(x(t+h)-x(t)-x'(t)h,\,y(t+h)-y(t)-y'(t)h\big).
```

在考察这些表达式时，有几点立刻显现出来：

1. $\mathbf{f}(t+h)-\mathbf{f}(t)-\mathbf{T}(h)$ 是 $\mathbb{R}^2$ 中的一个 vector（向量）而并非实数，因此在 (95) 的分子中需要用 norm（范数）取代绝对值。

2. 如所要求的那样，$\mathbf{T}(h)=\big(x'(t),\,y'(t)\big)h$ 关于 $h$ 是线性的。这意味着对所有的 $\alpha,h_1,h_2\in\mathbb{R}$，成立
```math
\mathbf{T}(\alpha h)=\alpha\mathbf{T}(h)
```
以及
```math
\mathbf{T}(h_1+h_2)=\mathbf{T}(h_1)+\mathbf{T}(h_2).
```
（在本次讨论中，点 $t$ 是固定的。）

3. 由于 $x$ 与 $y$ 都可微（由假设），故当 $h\to 0$ 时，
```math
\frac{x(t+h)-x(t)-x'(t)h}{h}\to 0,\qquad \frac{y(t+h)-y(t)-y'(t)h}{h}\to 0,
```
从而
```math
\frac{\|\mathbf{f}(t+h)-\mathbf{f}(t)-\mathbf{T}(h)\|}{|h|}\to 0.
```

更一般地，我们得到如下结论。设 $\mathbf{f}$ 定义在 $t\in\mathbb{R}$ 的某个 neighborhood（邻域）上，且其取值范围在 $\mathbb{R}^m$ 中。我们可以写成
```math
\mathbf{f}(t)=\big(x_1(t),\dots,x_m(t)\big),
```
其中 $x_1,\dots,x_m$ 全都定义在 $t$ 的某个邻域上（续下页）。

<span style="color:#7f8c8d">书页 522 · §12.7 Functions From R→R^m（从 R 到 R^m 的函数）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 正文把"f 在 t 可微"和"每个坐标函数 x_i 在 t 可微"划了等号。为什么敢这么划？因为范数的"分量夹逼"性质——对向量 v=(v_1,…,v_m)，总有 `max_i|v_i| ≤ ||v||_1 ≤ m·max_i|v_i|`，分子的每个分量被整体范数上下夹住（这就是记法策略模板**"分量归结法"**：把高维问题压回一维来证明，再用一维结果推回高维）。书中正是这样做的：若 f 可微，则第 i 个误差分量 `(x_i(t+h)-x_i(t)-a_i·h)/h` 的绝对值 ≤ 整体商，故每个差商必收敛，a_i 因此被迫等于 x_i'(t)；反过来各分量可微，则整体商是有限个趋于零的量之和，自然趋于零。对智能学子，这其实是 CSAPP 数据并行的数学版：m 个坐标并行地各自"跑微分"，能共享同一个收敛结论，就在于"整体误差不超过各自误差之和"这条三角形不等式。它同时解释了为何坐标函数可微 **不意谓** 整体可微，而偏导数存在却不够——差别你看后面的注 12.8 会看清，正是"逐方向"和"逐分量"的差异。

---


> <span style="color:#7f8c8d;">第 12 章　$\mathbb{R}^n$ 上的微分</span>

若函数 $x_1,\dots,x_m$ 中的每一个都在 $t$ 处可微，则
```math
\lim_{h\to 0}\frac{\|\mathbf{f}(t+h)-\mathbf{f}(t)-\mathbf{T}(h)\|}{|h|}=0,\qquad(96)
```
其中
```math
\mathbf{T}(h)=\big(x_1'(t),\dots,x_m'(t)\big)h.\qquad(97)
```

函数 $\mathbf{T}$ 关于 $h$ 是线性的（见习题 12.7.1）。

我们说 $\mathbf{f}$ 在 $t$ 处可微，并且把 $\mathbf{f}$ 在 $t$ 处的 differential（微分）称为函数 $\mathbf{T}$，它以 $\mathbf{T}(h)$ 为其在 $h$ 处的取值。

注意，$\mathbf{T}$ 依赖于点 $t$。

> [remark]<span style="color:#00838f">注记</span>

我们对在 $t$ 处可微性的定义，假定了函数 $x_1,\dots,x_m$ 中的每一个都在 $t$ 处可微。

这一假设与我们对 real-valued functions of several variables（实值多元函数）所作的定义类似，在那里我们假定了相应 partial derivatives（偏导数）的存在。

这一假设看起来也许很自然，但从技术上说，我们是在寻找任意一个满足 (96) 的 linear function（线性函数）$\mathbf{T}$。

先验地看，$\mathbf{T}$ 并未必要满足 (97)。

> [remark]<span style="color:#00838f">注记</span>

然而，以下是不争的事实：若 $\mathbf{f}$ 在 $t$ 处可微，则函数 $x_1,\dots,x_m$ 都在 $t$ 处可微。

不仅如此，若某个线性函数 $\mathbf{T}$ 满足 (96)，它必须由 (97) 给出。

为证此，假设 $\mathbf{f}:\mathbb{R}\to\mathbb{R}^m$ 在 $t$ 处可微，且 $\mathbf{T}=\mathbf{T}_t$ 是关于 $h$ 的一个线性函数。

于是存在 $(a_1,\dots,a_m)\in\mathbb{R}^m$，使得对所有 $h\in\mathbb{R}$ 成立 $\mathbf{T}(h)=(a_1,\dots,a_m)h$。

向量
```math
\frac{\mathbf{f}(t+h)-\mathbf{f}(t)-\mathbf{T}(h)}{h}
```
的第 $i$ 个分量是
```math
\frac{x_i(t+h)-x_i(t)}{h}-a_i.
```

为使 (96) 成立，必要且充分的条件是对 $i=1,\dots,m$ 都有
```math
\lim_{h\to 0}\frac{x_i(t+h)-x_i(t)}{h}=a_i,
```
即 $a_i=x_i'(t)$，这正是所要证明的。

> [remark]<span style="color:#00838f">注记</span>

此时我们应当对照两个有时会被学生混淆的陈述。

两个陈述都是真的。

- 函数 $\mathbf{f}:\mathbb{R}\to\mathbb{R}^m$ 在 $t$ 处可微，当且仅当所有 coordinate functions（坐标函数）$x_1,\dots,x_m$ 都在 $t$ 处可微。

- 若 $\mathbf{f}:\mathbb{R}^n\to\mathbb{R}$ 在 $x\in\mathbb{R}^n$ 处可微，则所有偏导数 $\partial f/\partial x_1,\dots,\partial f/\partial x_n$ 在 $x$ 处都存在。其逆命题为假：所有偏导数都可能存在，而 $f$ 却并不可微。

这一情形与连续性方面的对应情形相似。$\mathbf{f}:\mathbb{R}\to\mathbb{R}^m$ 在一点 $t$ 处连续，当且仅当所有坐标函数都在该点连续。

但一个函数 $f:\mathbb{R}^n\to\mathbb{R}$ 有可能在一点处关于每个变量分别连续，却在该点并不连续。$\blacksquare$<span style="color:#7f8c8d">书页 523 · §12.8 Functions From R^n 到 R^m（从 R^n 到 R^m 的函数）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 例 12.52 是一个极好的"反直觉清醒剂"：f(t)=(x(t),y(t)) 在 t=0 处可微，曲线却是 y=|x|——在 (0,0) 是尖点，没切线。第一性原理的教训：向量值函数 f 的导数 T 是"速度向量"（位移方向的线性化），它只告诉你"映射这一步往哪个方向走"，并不保证"走过的轨迹弯不弯"。尖点两条支线在原点各有一条半切线，方向不一致，但 t=0 处速度向量 (x'(0),y'(0))=(0,0) 只是"瞬时停住"，二者并不矛盾。这正像 CSAPP 里的局部性思维：导数只捕捉映射在一点处一阶的、无穷小的行为，轨迹的全局几何（是否平滑、有无转角）是更高阶的信息。它也在提醒你：把"可微"翻译成"曲线光滑有切线"在空间曲线情形会翻车，必须直接回到线性逼近的定义本身去判断——这是本节的纪律。

---


我们以一段说明结束上一节：之所以采用那样的可微性（differentiability）定义，正是为了获得我们想要的 $f$ 的那种线性逼近——一种与前文各节精神相符的逼近。这并不蕴含由参数式给出的曲线
```math
x_1=x_1(t),\quad x_2=x_2(t),\quad \ldots,\quad x_m=x_m(t),\qquad a\le t\le b
```
在点 $(x_1(t),\ldots,x_m(t))$ 处必有切线（tangent line），仅仅因为所有 $x_1,\dots,x_m$ 在 $t$ 处可微是不够的。

[example] **例 12.52**
> <span style="color:#7f8c8d;">TBB §12.8, p.523</span>

定义曲线
```math
x(t)=
\begin{cases}
t^2, & \text{若 }0\le t\le 1,\\[4pt]
-t^2, & \text{若 }-1\le t<0,
\end{cases}
\qquad
y(t)=t^2,\ \text{若 }-1\le t\le 1.
```
于是 $x'(0)=y'(0)=0$，所以函数 $f(t)=(x(t),y(t))$ 在 $t=0$ 处可微。但 (98) 给出的曲线正是 $y=|x|$，它并不在 $(0,0)=f(0)$ 处存在切线。$\blacksquare$

（习题 12.7.1 与 12.7.2 从略。）


**12.8 Functions From R^n 到 R^m（从 R^n 到 R^m 的函数）**

本小节为进阶节，可略读。本小节需要一些线性代数的知识，如必要时可以省略。

我们迄今讨论的可微函数是 $\mathbb{R}^n\to\mathbb{R}$ 与 $\mathbb{R}\to\mathbb{R}^m$ 的情形。这些当然只是更一般设定——从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的函数——的特例。我们现在转向这一更一般的设定。事实上，此前的大量内容都在试图以温和的方式将我们引导到这个抽象层次。我们首先回顾，在 §12.4 与 §12.7 中我们的目标是以某种意义用线性函数（linear function）逼近一个函数。这里我们怀有类似的目标。对这一内容的自然阐述需要线性代数的视角。

<span style="color:#7f8c8d">书页 524 · §12.8 Functions From R^n 到 R^m（从 R^n 到 R^m 的函数）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这是本书给你的一次观点跃迁，也是 Strang《线性代数》最该在此刻被唤醒的地方。Strang 的开篇立场是"线性变换才是主角，矩阵只是它的演员表"：fix 一个线性变换直接从 ℝ^n 打到 ℝ^m，再选定标准基，就能用唯一一个 m×n 矩阵去"演"它。现在对照表 12.8.1：一元时 f'(x) 是数（1×1 矩阵），ℝ^n→ℝ 时是行向量（梯度），ℝ→ℝ^m 时是列向量，而 ℝ^n→ℝ^m 则统一成 m×n 矩阵——它们不是四种不同东西，而是同一个对象 `A_x`（某个线性变换）在不同(定义域,值域)维下的"演出服"。于是微分 df(x,h)=A_x(h) 读法就变成:"增量 h 被线性变换 A_x 作用"。对智能学科这是 18.065 的伏笔：神经网络的每一层就是矩阵，前向传播=f 的复合，反向传播就是链式法则（下一整页）算出来的复合导数——你现在学的一节，正是深度学习的求导引擎的文字剧本。

---


**12.8.1 Review of Differentials and Derivatives（微分与导数的回顾）**

本小节为增补节，可以省略。

让我们回顾此前诸设定中的微分（differential）概念，不过现在借用一些线性代数的语言。对可微函数 $f:\mathbb{R}^n\to\mathbb{R}$，其在某点 $x=(x_1,\ldots,x_n)$ 处的微分具有形式
```math
df(x,h)=\frac{\partial f}{\partial x_1}h_1+\cdots+\frac{\partial f}{\partial x_n}h_n,
```
其中 $h=(h_1,\ldots,h_n)$，各偏导数在 $x$ 处取值。我们可以把它看成 $1\times n$ 矩阵
```math
\left(\frac{\partial f}{\partial x_1},\ldots,\frac{\partial f}{\partial x_n}\right)
```
与 $n\times 1$ 矩阵
```math
\begin{pmatrix}h_1\\ \vdots\\ h_n\end{pmatrix}
```
的乘积，于是微分就是一个行向量与一个列向量的乘积。若在记法中用 $dx_i$ 替换 $h_i$（$i=1,\ldots,n$），并定义 $f'$ 为
```math
f'(x)=\left(\frac{\partial f}{\partial x_1},\ldots,\frac{\partial f}{\partial x_n}\right),
```
那么可以写成
```math
d(f,dx)=f'(x)\,dx,
```
其中
```math
dx=(dx_1,\ldots,dx_n).
```
（这一记法令人联想起初等微积分中一元函数微分的记法。）

现在我们来看 §12.7 中讨论的情形，那里处理的是函数 $f:\mathbb{R}\to\mathbb{R}^m$，用通常的记法写成
```math
f=(f_1,f_2,f_3,\ldots,f_m).
```
这些 $f_k$ 称为 $f$ 的分量函数（component function）。在那里微分呈现形式
```math
df(x,h)=\left(\frac{df_1}{dx},\frac{df_2}{dx},\ldots,\frac{df_m}{dx}\right)h,
```
其中各导数在 $x$ 处取值。用矩阵记法可将其写成
```math
df(x,h)=\begin{pmatrix}\dfrac{df_1}{dx}\\[4pt]\dfrac{df_2}{dx}\\ \vdots\\ \dfrac{df_m}{dx}\end{pmatrix}(h).
```<span style="color:#7f8c8d">书页 525 · §12.8 Functions From R^n 到 R^m（从 R^n 到 R^m 的函数）</span>

下表概括了各情形中 $f'(x)$ 与 $df(x,h)=f'(x)h$ 这两种对象的具体形式：

| 定义域 | 值域 | 导数 $A=f'(x)=$ | 微分 $df(x,h)=f'(x)h$ |
|---|---|---|---|
| $\mathbb{R}$ | $\mathbb{R}$ | $f'(x)$ | $f'(x)h$ |
| $\mathbb{R}^n$ | $\mathbb{R}$ | $\left(\dfrac{\partial f}{\partial x_1},\ldots,\dfrac{\partial f}{\partial x_n}\right)$ | $\left(\dfrac{\partial f}{\partial x_1},\ldots,\dfrac{\partial f}{\partial x_n}\right)\begin{pmatrix}h_1\\ \vdots\\ h_n\end{pmatrix}$ |
| $\mathbb{R}$ | $\mathbb{R}^m$ | $\begin{pmatrix}\dfrac{df_1}{dx}\\ \vdots\\ \dfrac{df_m}{dx}\end{pmatrix}$ | $\begin{pmatrix}\dfrac{df_1}{dx}\\ \vdots\\ \dfrac{df_m}{dx}\end{pmatrix}(h)$ |

这些表目概括了导数与微分的形式。

若我们把 $f'(x)$ 写成以下矩阵
```math
f'(x)=\begin{pmatrix}\dfrac{df_1}{dx}\\[2pt] \dfrac{df_2}{dx}\\ \vdots\\ \dfrac{df_m}{dx}\end{pmatrix},
```
那么微分就取形式
```math
df(x,h)=f'(x)h \quad \text{或} \quad df(x,dx)=f'(x)\,dx.
```

在这两种情形中，我们都有导数 $f'(x)$ 的概念，以及微分
```math
df(x,h)=f'(x)h
```
或
```math
df(x,dx)=f'(x)\,dx.
```
在每一种情形中，我们都可以把导数 $f'(x)$ 看成某个线性变换（linear transformation）$A_x$ 的矩阵表示，而把微分看成该变换作用于向量 $h$ 的结果：
```math
df(x,h)=A_x(h).
```

**小结（Summary）**：让我们用一张表来总结上述内容。我们有一个定义在 $\mathbb{R}$ 或 $\mathbb{R}^n$ 中的开集 $D$ 上的函数，其值域落在 $\mathbb{R}$ 或 $\mathbb{R}^m$ 中。图 12.8.1 中的表格指明了在点 $x$ 处导数与微分的形式。

**注意（Note）**：我们把 $f'(x)$ 和 $h$ 都看成表示线性变换的矩阵，而把 $df(x,h)$ 看成这些矩阵的乘积。（当处理定义在 $\mathbb{R}$ 上的实值函数时，两个数的乘积可以看成一元 $1\times 1$ 矩阵的乘积。）

<span style="color:#7f8c8d">书页 526 · §12.8 Functions From R^n 到 R^m（从 R^n 到 R^m 的函数）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定义 12.53 把可微写成"存在线性变换 $T_x$ 使得商 $\|f(x+h)-f(x)-T_x(h)\|/\|h\|\to0$"，其第一性本质是一条加法分解——稍后正文干脆写成交待误差的式 (107)：$f(x+h)-f(x)=f'(x)h+E(h)\|h\|$，其中 $E\to0$。这是一种可复用的万能策略模板，叫**"线性主部 + 误差余项"**：把一个非线性增量拆成"线性部分 + 比 $\|h\|$ 更快缩到 0 的余项"。你这个观念的 Strang 用法：$T_x$ 唯一地由"在基上作用 $h$ 时误差消失"锁定。为什么非有 $T_x$ 不可？因为"线性逼近打哪儿出发都由 $h$ 的进入方向和步长决定"，$T_x(h)$ 关于 $h$ 线性（$T(\alpha h)=\alpha T(h)$、$T(h_1+h_2)=T(h_1)+T(h_2)$，书页 521 早就验证），所以逼近才不会弯。这条定义同时是 §12.4 你的老熟识定义 12.16 的"复合级升级"：$n=1$ 时只是把绝对值的事打包。对智能学子，这类似自动化差分：可微就是"一阶泰勒误差可控"，是梯度下降合法的前提。

---


**12.8.2 导数的定义（Definition of the Derivative）**

进阶节，可以省略。

现在让我们转向一般情形。假定有 $m$ 个含 $n$ 个变量的线性方程
```math
\begin{aligned}
y_1&=a_{11}x_1+a_{12}x_2+\cdots+a_{1n}x_n\\
y_2&=a_{21}x_1+a_{22}x_2+\cdots+a_{2n}x_n\\
&\;\;\vdots\\
y_m&=a_{m1}x_1+a_{m2}x_2+\cdots+a_{mn}x_n
\end{aligned} \tag{99}
```
这些方程定义了从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的一个线性变换。我们可以把这组方程写成矩阵方程
```math
y=Ax,
```
其中 $x=(x_1,\ldots,x_n)$、$y=(y_1,\ldots,y_m)$，而 $A=(a_{ij})$ 是 $m\times n$ 的系数矩阵。

从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的一般函数可以写成与 (99) 类似的形式。对 $f=(f^1,\ldots,f^m)$ 写出
```math
\begin{aligned}
y_1&=f^1(x_1,\ldots,x_n)\\
y_2&=f^2(x_1,\ldots,x_n)\\
&\;\;\vdots\\
y_m&=f^m(x_1,\ldots,x_n)
\end{aligned} \tag{100}
```
（这里和前面一样，采用上标来标识各个函数，以免与偏导数混淆。）

我们的任务是用一个由 (99) 给出的线性变换去逼近一个由 (100) 给出的函数。具体地说，我们要寻找一个从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的线性变换 $T$，其中 $T=T_x$ 依赖于 $x$，使得
```math
\lim_{\|\mathbf{h}\|\to 0}\frac{\|f(x+h)-f(x)-T_x(h)\|}{\|h\|}=0.
```
其中所涉及的范数（norm）可以任取：分子取 $\mathbb{R}^m$ 上任意一种范数，分母 $\|h\|$ 取 $\mathbb{R}^n$ 上任意一种范数。之所以如此，是因为如我们在 §11.6 所见，相对于一种范数的收敛等价于相对于另一种范数的收敛，即这些范数彼此等价（equivalent norms，等价范数）。不过为明确起见，我们约定采用 $\|t\|=\|t\|_1$，即 $t$ 各分量绝对值之和。

[definition] **定义 12.53**
> <span style="color:#7f8c8d;">TBB §12.8, p.526</span>

设 $D$ 为 $\mathbb{R}^n$ 中的开集，$x$ 为 $D$ 中一点，并设 $f:D\to\mathbb{R}^m$。若存在一个从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的线性变换 $T_x$，使得
```math
\lim_{\|\mathbf{h}\|\to 0}\frac{\|f(x+h)-f(x)-T_x(h)\|}{\|h\|}=0, \tag{101}
```
则称 $f$ 在 $x$ 处可微（differentiable）。

[definition] **定义 12.54**
> <span style="color:#7f8c8d;">TBB §12.8, p.526</span>

$f$ 的微分（differential），记作 $df$，在 $x$ 处定义为
```math
df(x,h)=T_x(h)
```
对所有 $h\in\mathbb{R}^n$ 成立。<span style="color:#7f8c8d">书页 527 · §12.8 Functions From R^n 到 R^m（从 R^n 到 R^m 的函数）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定义 12.55 是全书的一个高光时刻：它宣布"f'(x) 是函数，是那个线性变换 T_x 本身"，而不是某个数、某个向量。这句话有多重爆炸性。其一，对象型升级：过去 f'(x) 总问"等于多少"（一个数值），现在它问"是什么映射"；Strang 会说这正该如此——算子位于矩阵所有可能形态的最上位。其二，忠实性：f'(x) 完全记住 f 在 x 处一阶的全部信息，超过它就丢了，少于它就不够，这正是"导数作为最佳线性逼近"的唯一性。其三，范畴性：任何在 x 可微的 f，其行为在"一阶镜下"就是 T_x；而所有"可微点集合 + 它们的 T_x"一起，定义了一个把点送到线性变换的函数 x↦T_x——于是"导数"本身成了一个从空间到算子空间的映射，为后面反函数定理(12.50)的"导数非退化⇒局部可逆"埋下总纲。对智能学科，你会在 18.065 里看到同一对象升格再升格：当 f 是神经网络、x 是参数向量时，f'(x) 就是"把损失函数局部线性化"的梯度/雅可比，这一定义正是所有优化算法的合法性巴别塔底座。

---

---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定理 12.56 回答"线性变换 T_x 的矩阵到底长什么样"：答案就是第 i 行第 j 列取 ∂f_i/∂x_j 的 m×n 矩阵。理解它的最佳路径是回归 Strang 的**列思想**（column picture）：线性变换的矩阵表示中，第 j 列 = 单位方向 e_j 被 T_x 作用后的像。把 e_j 当作增量 h，则 (T_x)(e_j) 的 i 分量恰是全微分里 ∂f_i/∂x_j·1 那一项，于是 a_{ij} 被强制等于 ∂f_i/∂x_j。这正是正文 a_{ij}=∂f_i/∂x_j (105) 的由来，也是作业 12.8.5 让你亲手验的式子。一行一读更直观：第 i 行是第 i 个分量函数 f_i 的梯度（这是你在 §12.4 已认识的梯度拼成的). 雅可比矩阵因此是"m 行梯度、n 列对 n 个输入方向的敏感性"的双重透视。它告诉你，多输出神经网络/多输出机器人的"导数"天然是矩阵而非向量——这也是你后面做多任务学习、机械臂运动学时雅可比一抓一个准的原因。

---


[definition] **定义 12.55 (The derivative of f at x)**
> <span style="color:#7f8c8d;">TBB §12.8, p.527</span>

$f$ 在 $x$ 处的导数（derivative）是函数
```math
f'(x)=T_x,
```
它定义在 $f$ 的可微点集（set of points of differentiability of $f$）上。

我们注意到 $f'(x)$ 正是线性变换（linear transformation）$T_x$。它的定义域（domain）是 $\mathbb{R}^n$，值域（range）是 $\mathbb{R}^m$。当 $f$ 在 $x$ 处可微时，我们可以把 (101) 写成
```math
\lim_{\|\mathbf{h}\|\to 0}\frac{\|f(x+\mathbf{h})-f(x)-f'(x)\mathbf{h}\|}{\|\mathbf{h}\|}=0.
\qquad(102)
```
这一形式与从 $\mathbb{R}$ 到 $\mathbb{R}$ 的函数那种熟知的可微性形式相仿，只是其中的绝对值（absolute value）被范数（norm）所取代。

**习题 (Exercises)**

**12.8.1** 验证 (101) 的有效性不依赖于 $\mathbb{R}^n$ 与 $\mathbb{R}^m$ 上所采用的范数。

**12.8.2** 设 $A$ 是从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的一个线性变换。证明：对每个 $x\in\mathbb{R}^n$，都有 $A'(x)=A$。（提示参见附注 285。）

**12.8.3** 设 $f,g:\mathbb{R}^n\to\mathbb{R}^m$ 且 $\alpha\in\mathbb{R}$。证明：若 $f$ 与 $g$ 在 $x$ 处可微，则 $f+g$ 与 $\alpha f$ 也在 $x$ 处可微。此外，
```math
(f+g)'(x)=f'(x)+g'(x),
```
以及
```math
(\alpha f)'(x)=\alpha\,f'(x).
```

**12.8.4** 设 $f:\mathbb{R}^n\to\mathbb{R}$ 且 $g:\mathbb{R}^n\to\mathbb{R}^m$。证明：若 $f$ 与 $g$ 在 $x$ 处可微，则乘积函数 $fg$ 也在 $x$ 处可微，且
```math
(fg)'(x)=f'(x)g(x)+f(x)g'(x).
```

**12.8.3 Jacobians（雅可比矩阵）**

（*增补节，可以省略。*）

在完成这些准备工作之后，我们提出第一个问题：若 $f$ 在 $x$ 处可微，我们能否用涉及偏导数的矩阵来表示线性变换 $f'(x)$？对于从 $\mathbb{R}^n$ 到 $\mathbb{R}$ 或从 $\mathbb{R}$ 到 $\mathbb{R}^m$ 的映射这两种情形，我们已经看到了如何做到这一点（图 12.8.1）。这些结果提示，$f'(x)$ 的矩阵表示应当是一个 $m\times n$ 阶的雅可比矩阵（Jacobian matrix）。事实确实如此。

[theorem] **定理 12.56**
> <span style="color:#7f8c8d;">TBB §12.8, p.527</span>

设 $D$ 是 $\mathbb{R}^n$ 的一个开子集，设 $f:D\to\mathbb{R}^m$。设 $(f_1,\ldots,f_m)$ 是 $f$ 的分量函数（component function），如同 (100) 那样。于是
```math
f=(f_1,\ldots,f_m)，
```
其中对每个 $i=1,\ldots,m$ 都有 $f_i:D\to\mathbb{R}$。那么 $f$ 在 $x\in D$ 处可微当且仅当（if and only if）每个函数 $f_i$ 都在 $x$ 处可微。当 $f$ 在 $x$ 处可微时，其导数 $f'(x)$ 可由

<span style="color:#7f8c8d">书页 528 · §12.8 Functions From R^n 到 R^m（从 R^n 到 R^m 的函数）</span>

雅可比矩阵表示如下：
```math
T_x=f'(x)=
\begin{pmatrix}
\dfrac{\partial f_1}{\partial x_1} & \dfrac{\partial f_1}{\partial x_2} & \cdots & \dfrac{\partial f_1}{\partial x_n}\\[6pt]
\dfrac{\partial f_2}{\partial x_1} & \dfrac{\partial f_2}{\partial x_2} & \cdots & \dfrac{\partial f_2}{\partial x_n}\\[6pt]
\vdots & \vdots & \ddots & \vdots\\[6pt]
\dfrac{\partial f_m}{\partial x_1} & \dfrac{\partial f_m}{\partial x_2} & \cdots & \dfrac{\partial f_m}{\partial x_n}
\end{pmatrix},
\qquad(103)
```
其中各偏导数均在 $x$ 处取值。

[proof] **证明 (Proof)**
> <span style="color:#7f8c8d;">TBB §12.8, p.528</span>

本定理的证明只不过是对分量函数 $f_i$ 进行考察。首先假定 $f$ 在 $x$ 处可微。这意味着
```math
\lim_{\|\mathbf{h}\|\to 0}\frac{\|f(x+\mathbf{h})-f(x)-f'(x)\mathbf{h}\|}{\|\mathbf{h}\|}=0.
\qquad(104)
```
现在，$f'(x)$ 作为从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的线性变换，有一个矩阵表示 $A=(a_{ij})$。于是若 $\mathbf{h}=(h_1,\ldots,h_n)$，则 $f'(x)\mathbf{h}$ 的第 $i$ 个分量是 $\sum_{j=1}^n a_{ij}h_j$，而
```math
f(x+\mathbf{h})-f(x)
```
的第 $i$ 个分量是 $f_i(x+\mathbf{h})-f_i(x)$。因此，
```math
f(x+\mathbf{h})-f(x)-f'(x)\mathbf{h}
```
的第 $i$ 个分量是
```math
f_i(x+\mathbf{h})-f_i(x)-\sum_{j=1}^n a_{ij}h_j.
```
现在有
```math
\left|\,f_i(x+\mathbf{h})-f_i(x)-\sum_{j=1}^n a_{ij}h_j\,\right|\le \|f(x+\mathbf{h})-f(x)-f'(x)\mathbf{h}\|,
```
所以由 (104) 可得
```math
\lim_{\|\mathbf{h}\|\to 0}\frac{\left|\,f_i(x+\mathbf{h})-f_i(x)-\sum_{j=1}^n a_{ij}h_j\,\right|}{\|\mathbf{h}\|}=0.
```
因此 $f_i$ 在 $x$ 处可微。此外，
```math
a_{ij}=\frac{\partial f_i}{\partial x_j}.
\qquad(105)
```
(105) 的验证与上一节相应事实的证明类似（我们把它留作习题 12.8.5）。

为证明逆命题（converse），假定每个 $f_i$ 都在 $x$ 处可微。这意味着
```math
\lim_{\|\mathbf{h}\|\to 0}\frac{\left|\,f_i(x+\mathbf{h})-f_i(x)-\sum_{j=1}^n \dfrac{\partial f_i}{\partial x_j}h_j\,\right|}{\|\mathbf{h}\|}=0.
\qquad(106)
```

<span style="color:#7f8c8d">书页 529 · §12.8 Functions From R^n 到 R^m（从 R^n 到 R^m 的函数）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 例 12.57 看似只是算题，实则示范了一套可复用的证明策略**"范数夹逼"**（norm squeeze）：把一个看似"管不住"的误差算式，分解成受我们能掌控的上界夹住的项，再证明上界趋于零。对 $f(x,y)=(xy,x+y)$，雅可比是 $\begin{pmatrix}y&x\\1&1\end{pmatrix}$，(107) 式把增量 $\Delta f=(xy+hy+hk+xk-xk,\ldots)$ 拆成线性主部 $(yh+xk,\,h+k)$ 与余项 $(hk,0)$；剩下的误差 $E(h,k)=(hk/(|h|+|k|),\,0)$ 不是直线趋于零，而是被 $\|E(h,k)\|=|hk|/(|h|+|k|)$ 这同一个量控制。关键一夹：因为 $\dfrac{|h|}{|h|+|k|}\le 1$、$\dfrac{|k|}{|h|+|k|}\le 1$，故 $|hk|/(|h|+|k|)\le\min(|h|,|k|)\to0$，于是余项被夹到 $0$。这正是"误差余项比 $h$ 本身消失得还快"的工厂流水线。对智能学子，这套"把高阶项扔进余项、证明余项被夹死"的手法，你在后面的牛顿法、泰勒展开、数值稳定性分析里会反复撞见，值得今天就在这张小例子上练熟。

---


如今 (106) 式对每个 $i=1,\ldots,m$ 均成立。但 (104) 式分子中的范数正是一个求和式
```math
\sum_{i=1}^{m}\left|f^i(x+h)-f^i(x)-\sum_{j=1}^{n}\frac{\partial f^i}{\partial x_j}h_j\right|,
```
其中每一项在除以 $\|\mathbf{h}\|$ 后都趋于零。因此该和也趋于零，从而 (104) 式得以满足。故 $f$ 在 $x$ 处可微。$\blacksquare$

我们注意到，$f$ 在 $x$ 处可微的要求可以写成下述形式
```math
f(x+h)-f(x)=f'(x)h+E(h)\|\mathbf{h}\|, \tag{107}
```
其中误差项（error term）$E$ 满足
```math
\lim_{\|\mathbf{h}\|\to 0}\|E(h)\|=0 \quad \text{且} \quad E(0)=0.
```

这一观察表明，当 $f$ 在 $x$ 处可微时，$f$ 也在 $x$ 处连续。它还凸显出线性变换（linear transformation）$f'(x)$ 在何种意义下逼近 $x$ 附近的 $f$。我们看到，当我们处理从 $\mathbb{R}^n$ 到 $\mathbb{R}$ 的函数时，(107) 只是定义 12.16 中条件 2 的一种紧凑表达方式。

[example] **例 12.57**
> <span style="color:#7f8c8d;">TBB §12.8, p.529</span>

一个例子可以阐明 (107) 式。设
```math
u=xy,\qquad v=x+y,\qquad f(x,y)=(u,v).
```
由 (103) 式得
```math
f'(x)=
\begin{pmatrix}
\dfrac{\partial u}{\partial x} & \dfrac{\partial u}{\partial y}\\[6pt]
\dfrac{\partial v}{\partial x} & \dfrac{\partial v}{\partial y}
\end{pmatrix}
=
\begin{pmatrix} y & x\\ 1 & 1 \end{pmatrix}.
```
于是 (107) 式成为
```math
\bigl((x+h)(y+k)-xy,\;(x+h)+(y+k)-(x+y)\bigr)
=
\begin{pmatrix} y & x\\ 1 & 1 \end{pmatrix}\begin{pmatrix} h\\ k \end{pmatrix}
+E(h,k)\bigl(|h|+|k|\bigr).
```
化简并对 $E(h,k)$ 求解，得
```math
E(h,k)=\frac{(hk,0)}{|h|+|k|}.
```
从而
```math
\|E(h,k)\|=\frac{|hk|}{|h|+|k|}.
```
若 $h=0$ 或 $k=0$，则 $\|E(h,k)\|=0$。否则
```math
\|E(h,k)\|=\frac{1}{|1/k|+|1/h|}.
```
因此 $\displaystyle\lim_{(h,k)\to(0,0)}\|E(h,k)\|=0$。$\blacksquare$

<span style="color:#7f8c8d">书页 530 · §12.8.4 Chain Rules（链式法则）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这一页是 Strang《线性代数》最有价值的一句"广告语"被数学接管的时刻：**矩阵乘法就是复合的坐标账本**。Strang 说，把线性变换 A、B 复合，若 A 用矩阵 M_A、B 用矩阵 M_B 表示，则复合 B∘A 的矩阵就是 M_B·M_A。现在把"导数"也看成线性变换（上一注），复合函数的导数就该是矩阵乘积：(g∘f)'(x)=g'(f(x))·f'(x)。本节正是用这个框架统一了你在 §12.5 学的那一屋子链式法则（schema）与一维的定理 7.11——它们全是一条通式的特例。对智能学科，这是 18.065 的引擎：深度网络 L = L_n∘…∘L_1，其关于参数的导数照抄这条公式就是**反向传播**，(g∘f)' 的每一对相乘对应一层，矩阵乘的顺序从左往右恰是从输出层往输入层回传梯度。因此"链式法则=矩阵乘法"不是比喻，而是身份同一。这也解释了为何书页 530 把 B·A 直接演出来就能读出复合导数，因为"复合线性变换的矩阵按定义就是乘积"。

---


**习题**

12.8.5 在定理 12.56 的证明中验证 (105) 式。
（此习题为对正文的验证性补充，此处从略。）

**12.8.4 链式法则（Chain Rules）**

* 增补节。可以省略。

在 §12.5 中我们讨论了链式法则（chain rule），并指出运用“schema（链式图）”可能会便于写出相关的复合链。所有这些链式法则，连同熟悉的涉及从 $\mathbb{R}$ 到 $\mathbb{R}$ 的函数的微积分链式法则（定理 7.11），都是某一条一般链式法则的特殊情形。接下来我们就来考虑这条链式法则。我们的线性代数框架，连同本节所采用的便捷记法，使这条链式法则易于证明、易于记忆。

在陈述并证明这条链式法则之前，让我们回顾 §12.5.6 中那条链式法则之一（定理 12.36）。这就是与我们在例 12.30 中已见过的 schema 相关联的法则
```math
\begin{array}{c}
s \\[2pt]
\searrow\\[2pt]
t
\end{array}
\quad s,t\longrightarrow \begin{array}{c}x\\ y\end{array}
\longrightarrow z
```
（此处以 (108) 的方式示意 $s,t$ 经 $x,y$ 复合到 $z=g(x,y)$。）

在本节的术语中，这里有两个函数：$f:\mathbb{R}^2\to\mathbb{R}^2$，其坐标函数为 $x$ 与 $y$；以及 $g:\mathbb{R}^2\to\mathbb{R}$，在 (108) 中表示为 $z$，即 $z=g(x,y)$。假设按需可微，暂时忽略偏导数被取值的点，并采用 (108) 提示的记号，我们发现 $g$ 由矩阵 $B=\left(\frac{\partial z}{\partial x},\frac{\partial z}{\partial y}\right)$ 表示，而 $f'$ 由矩阵
```math
A=
\begin{pmatrix}
\dfrac{\partial x}{\partial s} & \dfrac{\partial x}{\partial t}\\[6pt]
\dfrac{\partial y}{\partial s} & \dfrac{\partial y}{\partial t}
\end{pmatrix}
```
表示。于是
```math
BA=
\left(\frac{\partial z}{\partial x},\frac{\partial z}{\partial y}\right)
\begin{pmatrix}
\dfrac{\partial x}{\partial s} & \dfrac{\partial x}{\partial t}\\[6pt]
\dfrac{\partial y}{\partial s} & \dfrac{\partial y}{\partial t}
\end{pmatrix}
=
\left(
\frac{\partial z}{\partial x}\frac{\partial x}{\partial s}+\frac{\partial z}{\partial y}\frac{\partial y}{\partial s},\;
\frac{\partial z}{\partial x}\frac{\partial x}{\partial t}+\frac{\partial z}{\partial y}\frac{\partial y}{\partial t}
\right).
```
最后这个表达式正是复合函数（composite function）$F=g\circ f$ 的导数，因为 $F'=\left(\frac{\partial z}{\partial s},\frac{\partial z}{\partial t}\right)$，而由例 12.30（或定理 12.36），$F'$ 的分量正是向量 $BA$ 的分量。

上述讨论并不精确，但它确实提示了一条以如下优美公式作结的链式法则
```math
(g\circ f)'(x)=g'\bigl(f(x)\bigr)\,f'(x).
```
在尝试证明这条链式法则公式（我们将在定理 12.58 中完成证明）之前，让我们先试着理解它为何成立。在 §7.3.2 中，我们通过考察某点处导数的绝对值来为从 $\mathbb{R}$ 到 $\mathbb{R}$ 的函数的链式法则提供动机<span style="color:#7f8c8d">书页 531 · §12.8 Functions From R^n→R^m（从 R^n 到 R^m 的函数）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 当值域与定义域维数相等（m=n），雅可比矩阵是方阵，其行列式 |J| 成为本书"导数是局部放大器"的完整化身：一元时放大的量是曲线弧长（比值 f'(x)），这里放大的量是面积/体积，比值正是 |det(f'(x))|（书页 531 的 ab 例子：对角形 [[a,0],[0,b]] 把单位正方形放成 a×b 矩形）。与此同步，有一个漂亮的代数事实：det(B·A)=det(B)·det(A)——这正是雅可比在 1841 年的《论函数行列式的形成与性质》(De determinantibus functionalibus) 里证明的**雅可比乘积定理**。把它和链式法则 (g∘f)'=g'(f(x))f'(x) 一拼，就立刻推出 det(F')=det(g')·det(f')，即**复合映射的放大因子等于各级放大因子之积**：先放大 det(f') 再放大 det(g')，总放大是乘积。这在书页 531 被几何化地推演了一次（线性情形），正是重积分换元法 ∫∬ f |J| du dv 的理论依据。对智能学科，det J=0 就是"局部坍缩/奇异"，代表不可逆、能控性丧失——机械臂越奇异的构型越危险，正是这里的主语。

---


作为局部的放大因子（magnification factor）。当处理 $f:\mathbb{R}^n\to\mathbb{R}^n$ 时，可以照搬类比，只需把 $f'$ 的绝对值换成雅可比矩阵的行列式（determinant of the Jacobian）。

先设 $A$ 是 $\mathbb{R}^2\to\mathbb{R}^2$ 的线性变换，例如 $A(u,v)=(x,y)$，其中 $x=au$，$y=bv$。则

```math
A'(u,v)=\begin{pmatrix}\frac{\partial x}{\partial u} & \frac{\partial x}{\partial v}\\[2pt] \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v}\end{pmatrix}=\begin{pmatrix}a&0\\[2pt]0&b\end{pmatrix}.
```

把 $A$ 视为 $\mathbb{R}^2\to\mathbb{R}^2$ 的映射，可以看到它把集合 $E$ 沿水平方向拉伸 $a$ 倍、沿垂直方向拉伸 $b$ 倍。（例如当 $a=2$、$b=3$ 时，$A$ 把单位正方形 $[0,1]\times[0,1]$ 映到矩形 $[0,2]\times[0,3]$。）于是若 $E$ 与 $A(E)$ 都有面积，则

```math
\frac{\operatorname{Area} A(E)}{\operatorname{Area} E}=ab.
```

映射 $A$ 把集合的面积放大了 $ab$ 倍。这一点可通过计算 $A'$ 的行列式来反映：

```math
\begin{vmatrix}a&0\\0&b\end{vmatrix}=ab.
```

现在取任何在点 $(u,v)\in\mathbb{R}^2$ 可微的 $f:\mathbb{R}^2\to\mathbb{R}^2$。若

```math
f'(u,v)=\begin{pmatrix}a&0\\0&b\end{pmatrix},
```

则由 $f$ 定义的映射在 $(u,v)$ 附近在极限意义下具有放大因子 $ab$。用与 §7.3.2 相近的记号，可以写作

```math
\lim_{J\to(u,v)}\frac{\operatorname{Area}f(J)}{\operatorname{Area}J}=ab.
```

之所以如此，是因为线性变换在 $f$ 的可微点附近以该意义逼近 $f$。

再考虑另一映射 $g:\mathbb{R}^2\to\mathbb{R}^2$，其导数 $g'$ 在 $f(x)$ 处取值。它在 $f(x)$ 处的导数是线性变换 $B=g'(f(x))$。$g$ 在 $f(x)$ 的放大因子与 $B$ 的放大因子相同，即 $B$ 的行列式。

于是，若 $\alpha$ 是 $A$（从而也是 $f$ 在 $x$）的放大因子，$\beta$ 是 $B$（从而也是 $g$ 在 $f(x)$）的放大因子，则 $\beta\alpha$ 就是 $BA$（从而也是 $g\circ f$ 在 $x$）的放大因子。这提示我们线性变换 $BA$ 正是 $g\circ f$ 在 $x$ 处的导数，至少对 $n=m=p$ 的情形如此。定理 12.58 将说明对所有 $m,n,p$ 这一结论都成立。

我们需要回忆一点会出现在定理 12.58 证明中的线性代数。设 $A$ 是从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的线性变换。由于 $A$ 与范数都是连续的（见习题 11.7.10），$\|\mathbf{A}\mathbf{x}\|$ 在紧集（compact set）$\{\mathbf{x}:\|\mathbf{x}\|=1\}$ 上取得最大值。我们把这一最大值记为 $\|\mathbf{A}\|$。即

```math
\|\mathbf{A}\|=\max_{\|\mathbf{x}\|=1}\|\mathbf{A}\mathbf{x}\|.
```

我们使用这个"范数"记号，是因为 $\|\cdot\|$ 事实上是从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的线性变换集合上的一个范数，不过我们并不需要这一事实。注意对所有 $\mathbf{x}\in\mathbb{R}^n$：

<span style="color:#7f8c8d">书页 532 · §12.8 Functions From R^n→R^m（从 R^n 到 R^m 的函数）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 定理 12.58 的证明用了一条贯穿全篇的策略**"三角形不等式控制"**（triangle-inequality domination）：要证 \|F-F_0-BAh\|/\|h\|→0，先把分子拆成若干可分工的项，每一项用三角形不等式交给一个"自己能控到零"的上界，最后收网。三件装备你也应记牢：(i) **算子范数** \|A\|=max_{\|x\|=1}\|Ax\|，保证对任意 h 有 \|Ah\|≤\|A\|\|h\|（紧网格上的最大值存在性依赖 \|·\| 连续，习题 11.7.10——这是你前面学的连续性派上用场的地方）；(ii) 误差余项 E_1、E_2 各自 →0（来自 f、g 的可微性）；(iii) 由 f 连续，当 h→0 时增量 k=f(x_0+h)-f(x_0)→0，从而 E_2(k)→0。于是 (116) 的每一项（\|B\|E_1、(\|A\|+E_1)E_2）都趋于零，整体被夹死。这套"两个可微性的余项配对、再用一个缓冲的 \|k\| 换 \|h\|"的骨架，你会在整个多元分析反复见到。历史在此必须补一笔（虽然本书未点名）：把导数定义成"Banach 空间之间的有界线性算子 A 使商趋零"的形式，正是 **Fréchet 导数**，得名于法国数学家 Maurice Fréchet（1878—1973）；而 Peano（1858—1932）早在其 1884—1887 的著作里已具备近乎现代的可微性与线性主部——史学家据此认为现代微分定义的雏形可上溯到 Peano，Fréchet 是在泛函分析的抽象框架里把它立成惯例。当 V=ℝ^n、W=ℝ^m（有限维）时，Fréchet 导数正是定义 12.53–12.55，其矩阵就是雅可比矩阵——所以你在写"向量函数的导数矩阵"时，其实是在写 Fréchet 导数的坐标表。

---


（$\mathbf{x}\neq 0$），

```math
\|\mathbf{A}\mathbf{x}\|=\left\|\mathbf{A}\frac{\mathbf{x}}{\|\mathbf{x}\|}\right\|\,\|\mathbf{x}\|\le\|\mathbf{A}\|\,\|\mathbf{x}\|.
```

在下面的证明中会出现若干不同的范数，它们都记作 $\|\cdot\|$。空间 $\mathbb{R}^n$、$\mathbb{R}^m$、$\mathbb{R}^p$ 各有范数，从一个空间到另一个空间的线性变换集合也是如此。本可以为不同的范数使用不同的记号，但那样可能令人眼花缭乱。反之，我们遵循通行的做法，只用单一符号表示所有范数，相信上下文会表明所指的究竟是哪个范数。

**习题 12.8.6**（跳过）：证明从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的所有线性变换集合是一个向量空间（在适当的和与标量积解释下），并证明 $ \|\mathbf{A}\|=\max_{\|\mathbf{x}\|=1}\|\mathbf{A}\mathbf{x}\|$ 为该空间元素定义了一个范数。

**12.8.5 链式法则的证明**

*进阶章节（Enrichment section），可省略。*

现在我们有条件给出一般链式法则公式的正式陈述与证明。

**定理 12.58** [theorem]
> <span style="color:#7f8c8d;">TBB §12.8, p.532</span>

设 $D$ 是 $\mathbb{R}^n$ 中的开集。设 $f:D\to\mathbb{R}^m$ 在 $\mathbf{x}_0\in D$ 可微。设 $H$ 是包含 $f(D)$ 的开集，且 $g:H\to\mathbb{R}^p$ 在 $f(\mathbf{x}_0)$ 可微。则由

```math
F(\mathbf{x})=g(f(\mathbf{x}))
```

定义的函数 $F:D\to\mathbb{R}^p$ 在 $\mathbf{x}_0$ 可微，且

```math
F'(\mathbf{x}_0)=g'(f(\mathbf{x}_0))\,f'(\mathbf{x}_0). \tag{109}
```

(109) 中的乘积是两个线性变换的乘积（matrix product）。

**证明** [proof]. 设

```math
\mathbf{y}_0=f(\mathbf{x}_0),\qquad A=f'(\mathbf{x}_0),\qquad B=g'(\mathbf{y}_0).
```

我们希望证明

```math
\frac{\|F(\mathbf{x}_0+\mathbf{h})-F(\mathbf{x}_0)-BA\,\mathbf{h}\|}{\|\mathbf{h}\|}\to0\qquad(\mathbf{h}\to0). \tag{110}
```

由于 $f$ 在 $\mathbf{x}_0$ 可微、$g$ 在 $\mathbf{y}_0$ 可微，利用 (107)，可对满足 $\mathbf{x}_0+\mathbf{h}\in D$、$\mathbf{y}_0+\mathbf{k}\in H$ 的向量写出

```math
f(\mathbf{x}_0+\mathbf{h})-f(\mathbf{x}_0)-A\mathbf{h}=E_1(\mathbf{h})\|\mathbf{h}\|,\tag{111}
```

```math
g(\mathbf{y}_0+\mathbf{k})-g(\mathbf{y}_0)-B\mathbf{k}=E_2(\mathbf{k})\|\mathbf{k}\|,
```

其中

```math
\|E_1(\mathbf{h})\|\to0\quad(\mathbf{h}\to0),\qquad \|E_2(\mathbf{k})\|\to0\quad(\mathbf{k}\to0).\tag{112}
```<span style="color:#7f8c8d">书页 533 · §12.8 Functions From R^n→R^m（从 R^n 到 R^m 的函数）</span>

下面我们估计 (110) 中的分子。对给定的 $\mathbf{h}$，设

```math
\mathbf{k}=f(\mathbf{x}_0+\mathbf{h})-f(\mathbf{x}_0). \tag{113}
```

由 (111) 可得

```math
\|\mathbf{k}\|=\|\mathbf{A}\mathbf{h}+E_1(\mathbf{h})\|\mathbf{h}\|\|
\le \|\mathbf{A}\|\|\mathbf{h}\|+\|E_1(\mathbf{h})\|\,\|\mathbf{h}\|
=(\|\mathbf{A}\|+\|E_1(\mathbf{h})\|)\|\mathbf{h}\|. \tag{114}
```

由 (113) 我们看到

```math
f(\mathbf{x}_0+\mathbf{h})=f(\mathbf{x}_0)+\mathbf{k}=\mathbf{y}_0+\mathbf{k},
```

所以

```math
F(\mathbf{x}_0+\mathbf{h})-F(\mathbf{x}_0)=g(f(\mathbf{x}_0+\mathbf{h}))-g(\mathbf{y}_0)=g(\mathbf{y}_0+\mathbf{k})-g(\mathbf{y}_0).
```

于是

```math
F(\mathbf{x}_0+\mathbf{h})-F(\mathbf{x}_0)-BA\,\mathbf{h}=g(\mathbf{y}_0+\mathbf{k})-g(\mathbf{y}_0)-BA\,\mathbf{h}. \tag{115}
```

利用 (111)，我们把 (115) 的右端写成

```math
B\mathbf{k}+E_2(\mathbf{k})\|\mathbf{k}\|-BA\mathbf{h}
=B(\mathbf{k}-A\mathbf{h})+E_2(\mathbf{k})\|\mathbf{k}\|
=BE_1(\mathbf{h})\|\mathbf{h}\|+E_2(\mathbf{k})\|\mathbf{k}\|.
```

对量

```math
F(\mathbf{x}_0+\mathbf{h})-F(\mathbf{x}_0)-BA\,\mathbf{h}
```

的这一估计，连同 (112) 与 (114)，意味着当 $\mathbf{h}\neq 0$ 时，

```math
\frac{\|F(\mathbf{x}_0+\mathbf{h})-F(\mathbf{x}_0)-BA\,\mathbf{h}\|}{\|\mathbf{h}\|}
\le \frac{\|BE_1(\mathbf{h})\|\mathbf{h}\|\|+\|E_2(\mathbf{k})\|\mathbf{k}\|\|}{\|\mathbf{h}\|}
\le \|B\|\,E_1(\mathbf{h})+\|E_2(\mathbf{k})\|(\|A\|+\|E_1(\mathbf{h})\|). \tag{116}
```

现在 $\|B\|$ 与 $\|A\|$ 都是固定的数，且

```math
E_1(\mathbf{h})\to0\quad(\mathbf{h}\to0).
```

此外，由 (113) 及 $f$ 在 $\mathbf{x}_0$ 处的连续性，当 $\mathbf{h}\to0$ 时 $\mathbf{k}\to0$，所以

```math
E_2(\mathbf{k})\to0\quad(\mathbf{h}\to0).
```

于是 (116) 中的表达式当 $\mathbf{h}\to0$ 时趋于零。但我们已经看到，这一表达式支配着 (110) 中的商式，因而 (110) 成立，故 $F$ 在 $\mathbf{x}_0$ 可微且导数为 $BA$。由于

```math
BA=g'(f(\mathbf{x}_0))\,f'(\mathbf{x}_0),
```

我们的证明至此完成。 $\blacksquare$

<span style="color:#7f8c8d">书页 534 · §12.8 Functions From R^n→R^m（从 R^n 到 R^m 的函数）</span>


---

> <span style="color:#1e8449;">**[note] Note（译者注）:**</span> 这道题是链式法则矩阵版的一次验收：你说 e^u（u:ℝ^n→ℝ）可微？定理 12.58 替你买单——把 e^u 写成复合 exp∘u，exp:ℝ→ℝ 处处可微且 (exp)'=exp，u 在点可微，则复合必可微，导数等于 (exp)'(u)·u' = e^u·u'。这里 exp' 是 1×1 矩阵（就是数 e^u），u' 是行向量（梯度），1×1 矩阵乘行向量还是行向量，于是 d(e^u)=e^u·du 顺理成章。它示范了矩阵版的**幂勒法/链式法则**日常工作流——把"看起来不能直接微分"的对象，拆成"已知可微的简单函数"的复合，再用 (g∘f)'=g'(f(x))·f'(x) 一次成型，维数由乘积自动校准。对 §12.5 那个小心翼翼回避"e^u 是否可微"的一维推导，这页给了它一个干净而彻底的合法性修复：可微性不是假定出来的，是链式法则证出来的。你现在可以用同一套路去判定任意"外函数简单、内函数复杂"的复合的可微性，这就是智能学科里梯度代码里每一行可微性检查背后的那条定理。


**习题（Exercises）**

**习题 12.8.7** [example]

> <span style="color:#7f8c8d;">TBB §12.8, p.534</span>

若 $u:\mathbb{R}^n\to\mathbb{R}$ 可微，则我们此前（例 12.25）曾得出公式 $d(e^u)=e^udu$，但当时不得不假定 $e^u$ 也是可微的。请用定理 12.58 来论证这一假定，并检验该公式。

*英文原题：* If $u:\mathbb{R}^n\to\mathbb{R}$ is differentiable, then we obtained earlier (Example 12.25) the formula $d(e^u)=e^udu$ but we were required to assume that $e^u$ is also differentiable. Use Theorem 12.58 to justify that assumption and to check the formula.

> **解答思路（提纲）：** 把 $e^u$ 视为复合映射 $e^u=\exp\circ u$，其中 $\exp:\mathbb{R}\to\mathbb{R}$ 处处可微且 $(\exp)'=\exp$。由定理 12.58，$g'\circ f'$ 存在，故复合映射 $e^u$ 必可微，从而该假定得到印证；再由链式法则，$(e^u)'=e^u\,u'$，即 $d(e^u)=e^udu$，公式得到检验。

*注：* 习题 12.8.8 至 12.8.13 涉及复合微分的图式（schema）推理、$F=h\circ g\circ f$ 的三重复合定理陈述、含极坐标与指数型的映射微分计算以及反函数定理的链式法则证明，均属本章练习内容，此处按任务要求跳过。