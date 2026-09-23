# 2025 Spring · 18.100B/18.1002 · Real Analysis

<span style="color:#7f8c8d">*Tobias Holck Colding*</span>

---

## <span style="color:#c0392b">Lecture 2（第2讲）</span>

### Introduction to Real Numbers (cont.)（实数的引入 · 续）

---

<span style="color:#2471a3;">**[question]**</span> **Question（问题）：** What distinguishes $\mathbb{R}$ from $\mathbb{Q}$?  
One answer: $\sqrt{2}\in\mathbb{R}$ but $\sqrt{2}\notin\mathbb{Q}$.

The real numbers（实数）$\mathbb{R}$ form a **complete ordered field**（完备有序域）containing $\mathbb{Q}$. $\sqrt{2}$ is the unique $x>0$ satisfying $x^{2}=2$.

---

<span style="color:#2471a3;">**[theorem]**</span> ### <span style="color:#c0392b">Theorem（定理）</span>

**Irrationality of $\sqrt{2}$（$\sqrt{2}$ 的无理性）.** 不存在 rational number（有理数）$x$ 使得 $x^{2}=2$.

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.* 使用反证法（proof by contradiction）。假设 $x=\dfrac{m}{n}\in\mathbb{Q}$，其中 $m\in\mathbb{Z}$, $n\in\mathbb{N}$，且 $\gcd(m,n)=1$（即 $m,n$ 互质）。由 $x^{2}=m^{2}/n^{2}=2$ 得 $m^{2}=2n^{2}$，故 $2\mid m^{2}$，从而 $2\mid m$。令 $m=2m_{1}$，代入得 $4m_{1}^{2}=2n^{2}$，即 $2m_{1}^{2}=n^{2}$，故 $2\mid n$ 亦成立。于是 $m$ 和 $n$ 均为偶数，与 $\gcd(m,n)=1$ 矛盾。∎

---

### 如何将 $\sqrt{2}$ 添加到 number system（数系）？

$$
\sqrt{2}=1.41421356\ldots
$$

数列（sequence）$1,\;1.4,\;1.41,\;1.414,\;1.4142,\;1.41421,\;\dots$ 收敛到（converges to）$\sqrt{2}$。

$\sqrt{2}$ 是该数列的 **limit（极限）**。

---

## <span style="color:#c0392b">Completeness of $\mathbb{R}$（$\mathbb{R}$ 的完备性）</span>

### Least Upper Bound Property（最小上界性质）

<span style="color:#2471a3;">**[definition]**</span> <span style="color:#00838f">**Completeness（完备性）：**</span> 任意有 **upper bound（上界）** 的非空子集 $A\subseteq\mathbb{R}$ 都有 **least upper bound（最小上界）**。

设 $S$ 是一个 **ordered set（有序集）**，$A\subseteq S$。若对所有 $a\in A$ 均有 $a\le M$，则称 $M$ 是 $A$ 的一个 **upper bound（上界）**。

<span style="color:#2471a3;">**[example]**</span> **Example（例）.**
:   $A=\{1,2,3\}\subset\mathbb{Z}$：$4$ 是一个上界，$2$ 不是。

<span style="color:#2471a3;">**[example]**</span> **Example（例）.**
:   $S=\mathbb{Q}$：$\mathbb{N}\subset\mathbb{Q}$ 没有上界 <span style="color:#1e8449">（we will return to this shortly）.</span>

---

<span style="color:#2471a3;">**[definition]**</span> #### <span style="color:#2471a3">Least Upper Bound（最小上界）</span>

设 $S$ 是一个有序集，$A\subseteq S$ 有上界。$M\in S$ 是 $A$ 的 **least upper bound（最小上界）**（或称 **supremum（上确界）**），如果  
(i) $M$ 是 $A$ 的一个上界；  
(ii) 对 $A$ 的任意上界 $M_{1}$，均有 $M\le M_{1}$。

---

<span style="color:#2471a3;">**[definition]**</span> #### <span style="color:#c0392b">Complete Ordered Set（完备有序集）</span>

若有序集 $S$ 中任意有上界的非空子集都有最小上界，则称 $S$ 是 **complete（完备的）**。

---

<span style="color:#2471a3;">**[theorem]**</span> ### <span style="color:#c0392b">Theorem（定理）</span>

**Existence of $\mathbb{R}$（$\mathbb{R}$ 的存在性）.**
存在一个包含 $\mathbb{Q}$ 的 complete ordered field（完备有序域），记作 $\mathbb{R}$。（我们将其视为公理，其构造证明超出本课程范围。）

---

<span style="color:#2471a3;">**[theorem]**</span> ### <span style="color:#c0392b">Theorem（定理）</span>

$\sqrt{2}\in\mathbb{R}$.

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.* 构造集合  

$$
A \;=\; (0,\sqrt{2})\cap\mathbb{Q} \;=\; \{\,a\in\mathbb{Q}_{>0}\mid a^{2}<2\,\}.
$$

$A$ 非空（$1\in A$）且有上界（例如 $2$）。设 $x=\sup A$（最小上界），显然 $x\ge1>0$。需证 $x^{2}=2$。

**(i) $x^{2}\le2$.** 若 $x^{2}>2$，选取 $h>0$ 使  

$$
2hx < x^{2}-2 \quad\Longleftrightarrow\quad h<\frac{x^{2}-2}{2x}.
$$

则  

$$
(x-h)^{2}=x^{2}-2xh+h^{2}>x^{2}-2xh>2,
$$

故 $x-h$ 也是 $A$ 的上界，与 $x$ 是*最小*上界矛盾。因此 $x^{2}\le2$。

**(ii) $x^{2}\ge2$.** 若 $x^{2}<2$，选取 $h>0$（且 $h<1$）使  

$$
h<\frac{2-x^{2}}{2x+1}.
$$

则  

$$
(x+h)^{2}=x^{2}+2xh+h^{2}<x^{2}+2xh+h=x^{2}+h(2x+1)<2,
$$

故 $x+h\in A$，与 $x$ 是上界矛盾。因此 $x^{2}\ge2$。

由 (i)(ii) 得 $x^{2}=2$，即 $x=\sqrt{2}\in\mathbb{R}$。∎

---

<span style="color:#2471a3;">**[corollary]**</span> ### <span style="color:#c0392b">Corollary（推论）</span>

$\mathbb{Q}$ **不是**完备的（not complete）。

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.* 若 $\mathbb{Q}$ 完备，则 $\sqrt{2}\in\mathbb{Q}$，与 √2 无理性定理矛盾。∎

---

## <span style="color:#c0392b">Archimedean Property（阿基米德性质）</span>

<span style="color:#2471a3;">**[property]**</span> <span style="color:#c0392b">**Archimedean Property（阿基米德性质）.**
</span> 对所有 $x\in\mathbb{R}$，存在 $n\in\mathbb{N}$ 使得 $n>x$。

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.* 若 $\mathbb{N}$ 有上界，设 $\alpha=\sup\mathbb{N}$。则 $\forall n\in\mathbb{N}$ 有 $n\le\alpha$。但 $n+1\in\mathbb{N}$，故 $n+1\le\alpha$，即 $n\le\alpha-1$。于是 $\alpha-1$ 是比 $\alpha$ 更小的上界，与 $\alpha$ 的定义矛盾。∎

---

<span style="color:#2471a3;">**[corollary]**</span> ### <span style="color:#c0392b">Corollary（推论）</span>

**Density of $\mathbb{Q}$（有理l数的稠密性）.**
若 $x<y$，则存在 $r\in\mathbb{Q}$ 使得 $x<r<y$。

<span style="color:#2471a3;">**[proof]**</span> *Proof（证明）.* 令 $\beta=\dfrac{1}{\,y-x\,}>0$。由阿基米德性质，取 $n\in\mathbb{N}$ 使 $n>\beta$，则 $0<\dfrac{1}{n}<\dfrac{1}{\beta}=y-x$。选 $m\in\mathbb{Z}$ 为满足 $m>xn$ 的最小整数，则 $m-1\le xn<m$，故  

$$
x<\frac{m}{n}<x+\frac{1}{n}<y.
$$

因此 $r=m/n$ 即为所求。∎

---

## References（参考文献）

<span style="color:#2471a3;">**[reference]**</span> **[TBB]** B.S. Thomson, J.B. Bruckner, and A.M. Bruckner, *Elementary Real Analysis*, 2nd ed.  
<span style="color:#2471a3;">https://classicalrealanalysis.info/com/documents/TBB-AllChapters-Landscape.pdf</span>

---

<span style="color:#7f8c8d">*MIT, Dept. of Math., Cambridge, MA 02139*</span>

---

<span style="color:#2471a3;">**[source]**</span> **Source（来源）：** MIT OpenCourseWare — 18.100B Real Analysis, Spring 2025 · <span style="color:#2471a3;">https://ocw.mit.edu</span>
