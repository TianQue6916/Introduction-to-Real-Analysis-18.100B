<span style="color:#7f8c8d">书页 297 · §7.6 Mean Value Theorem（中值定理）</span>

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