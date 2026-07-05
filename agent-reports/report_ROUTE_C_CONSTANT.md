## CLAIMS

Throughout: $n=k^2+1$ squares $S_1,\dots,S_n$ with pairwise disjoint interiors in $T=[0,k]^2$ (scaled setting), sides $d_i>0$, tilts $\theta_i$ (angle of a side to the $x$-axis, taken in $[0,\pi/4]$ by the square's symmetry; write $c_i=\cos\theta_i$, $s_i=\sin\theta_i$). $\sum d_i = k^2+\varepsilon$; $f(k^2+1)=k+\varepsilon^*/k$ where $\varepsilon^*$ is the max excess. $G:=k^2-\sum d_i^2\ge 0$ (uncovered area), $m:=(k^2+\varepsilon)/(k^2+1)$ (mean side), $V:=\sum_i (d_i-m)^2$.

### Claim 1 (Exact identity and exact reformulation of the target). Confidence: 1.

**Statement.** For every packing as above,
$$G+V \;=\; k^2-\frac{(k^2+\varepsilon)^2}{k^2+1}\;=\;\frac{k^2(1-2\varepsilon)-\varepsilon^2}{k^2+1}. \qquad (\ast)$$
Consequently: (i) $G+V\ge 0$ re-derives Cauchy–Schwarz $f(k^2+1)\le\sqrt{k^2+1}$; (ii) for any $\delta_0\in(0,1)$, the statement "every packing of $k^2+1$ squares in $[0,k]^2$ has $G+V\ge\delta_0$" is **equivalent** to $\varepsilon^*\le(1-\delta_0)/2$, i.e. to $f(k^2+1)\le k+\frac{1/2-\delta_0/2}{k}$ — the C2 target with $c=\delta_0/2$.

**Proof.** $V=\sum d_i^2 - n m^2$ (definition of variance about the mean), $G=k^2-\sum d_i^2$ (disjointness), so $G+V=k^2-nm^2=k^2-(k^2+\varepsilon)^2/(k^2+1)$; expand the numerator over $k^2+1$: $k^2(k^2+1)-(k^2+\varepsilon)^2=k^2(1-2\varepsilon)-\varepsilon^2$. For (ii): $G+V\ge\delta_0$ iff $k^2(1-2\varepsilon)-\varepsilon^2\ge\delta_0(k^2+1)$, which (since $\varepsilon^2\ge0$, $\delta_0(k^2+1)/k^2\ge\delta_0$) forces $1-2\varepsilon\ge\delta_0$, i.e. $\varepsilon\le(1-\delta_0)/2$; conversely $\varepsilon\le(1-\delta_0)/2$ gives $k^2(1-2\varepsilon)-\varepsilon^2\ge \delta_0 k^2-\tfrac14 \ge \delta_0(k^2+1)$ for $k^2\ge (1/4+\delta_0)/(1-\delta_0)\cdot$—up to the harmless $O(1/k^2)$ adjustment of $\delta_0$; both directions exact up to $O(1/k^2)$ in the constant. $\square$

**Remark.** $(\ast)$ is an *identity*: $G+V$ is a function of $\varepsilon$ alone. So "gap + variance bounded below" is not extra information to be combined with Cauchy–Schwarz — it *is* the theorem, in geometric coordinates. Every attack below is an attack on: *no packing has $G+V<\delta_0$*.

### Claim 2 (Side uniformity in the critical regime). Confidence: 1.

**Statement.** If $G+V<\delta_0\le 1/5$ and $\varepsilon\ge0$, then **every** side satisfies $|d_i-m|<\sqrt{\delta_0}$, with $m\in[1-\tfrac{1}{k^2+1},\,1]$ (using $\varepsilon\le 1/2$ from Claim 1(i)). In particular all $d_i\in(1-\sqrt{\delta_0}-\tfrac1{k^2},\,1+\sqrt{\delta_0})$: there are **no small squares at all** in a near-critical packing.

**Proof.** $(d_i-m)^2\le V< \delta_0$ per square. $m=(k^2+\varepsilon)/(k^2+1)$ with $0\le\varepsilon\le1/2$. $\square$

### Claim 3 (C1: corrected slice/chord calculus for tilted squares). Confidence: 1.

Let $S$ have side $d$, tilt $\theta\in[0,\pi/4]$, and let $\ell$ be a vertical line.

**(a) Chords exceed the side.** The chord length profile $x\mapsto \mu(S\cap\ell_x)$ is trapezoidal: it rises linearly with slope $\tan\theta+\cot\theta=1/(s c)$ over the first $d\,s$ of the projection, plateaus at the value $d\sec\theta$ over an interval of length $d(c-s)$, and descends symmetrically. Max chord $=d\sec\theta\in[d,\,d\sqrt2]$ (**not** $\le d$; the assignment's suspicion is confirmed). $\int \mu\, dx = d^2$. Projection width $w=d(c+s)$; the number of lines of the shifted unit grid meeting $S$ is $p(x_0)\in\{\lfloor w\rfloor,\lceil w\rceil\}$ with $\int_0^1 p\,dx_0=w$. (Verified symbolically and numerically; see sanity checks.)

**(b) Per-line and per-family inequalities.** For each vertical line $L_j=\{x=x_0+j\}$, disjointness gives $\sum_i \mu(S_i\cap L_j)\le k$; summing over the $k$ lines: $\sum_i M_i(x_0)\le k^2$ **for every shift** $x_0$, where $M_i$ is the total chord mass of $S_i$ on the family. Since $\int_0^1 M_i = d_i^2$, the *average* of this inequality is exactly the area bound $\sum d_i^2\le k^2$: chord slicing alone can never see the "+1"; the integrality of counts must enter (as in BKU).

**(c) Weighted corollary at the BKU shift (axis-parallel).** For axis-parallel packings, $M_i=p_i d_i$, so at any $x_0$ with $\sum p_i\ge k^2+1$ (which exists by pigeonhole when $\varepsilon>0$): $\sum_i p_i d_i\le k^2$ and $\sum p_i\ge k^2+1$ give
$$\sum_i p_i(1-d_i)\;\ge\;1 .$$
At a good shift, the deficiency $1-d_i$ of the lines' host squares must total at least one full unit. (Complete proof: subtract.)

### Claim 4 (First-moment no-go theorem; exact neutrality of rotation). Confidence: 1.

**Statement.** Let $\Lambda_u=\mathbb Z^2+u$. (i) For every packing and every $u$, $\Phi(u):=\sum_i|S_i\cap\Lambda_u| = k^2-\gamma(u)$, where $\gamma(u)=|\Omega\cap\Lambda_u|$ counts lattice points in the gap set $\Omega=T\setminus\bigcup S_i$; so the counting inequality $\Phi\le k^2$ is an identity in disguise and all information sits in *where the gap points are*. (ii) For a single square of side $d$, tilt $\theta$:
$$\mathbb E_u\big[p+q-|S\cap\Lambda_u|\big] \;=\; 2d(\cos\theta+\sin\theta)-d^2 .$$
Hence the shift-averaged "BKU defect" $\mathbb E[p+q-1-|S\cap\Lambda_u|]-\big(2(w-1)\big) = -(1-d)^2\le 0$ **with equality at $d=1$ for every tilt**: on average, the extra projection mass $2(w-d)$ a tilt donates to the pigeonhole is *exactly* cancelled by the extra lattice-count defect it creates. (iii) Consequently any argument using only per-square shift-averaged quantities (first moments of counts, chords, projections) reduces to the area bound $\sum d_i^2\le k^2$ and cannot improve on Cauchy–Schwarz. The "+1" in BKU comes solely from integer concentration of $p,q$ at a *chosen* shift.

**Proof.** (i) $\bigcup S_i\subseteq T$, interiors disjoint, boundaries null for a.e. $u$; $|T\cap\Lambda_u|=k^2$ a.e. (ii) $\mathbb E|S\cap\Lambda_u|=\operatorname{area}=d^2$ (Fubini), $\mathbb E p=\mathbb E q=w=d(c+s)$. (iii) Per-square averaged quantities are determined by $(d_i,\theta_i)$ through area and width alone, and the assembled inequalities close only through $\sum d_i^2\le k^2$; the neutrality (ii) shows tilt terms cancel identically. Monte Carlo confirmation of (ii) to 3 digits at $(d,\theta)=(1,0.3),(0.95,0.7),(1,\pi/4)$. $\square$

### Claim 5 (Theorem T1: unconditional excess-vs-tilt inequality via BKU black box). Confidence: 0.97 (modulo BKU's theorem, used as stated).

**Statement.** For every packing of $n$ squares in $[0,k]^2$ (any orientations),
$$\sum_i \frac{d_i}{\cos\theta_i+\sin\theta_i}\;\le\; k\cdot g\!\left(\tfrac{n}{\,}\right)\Big|_{\text{scaled}},\qquad\text{in particular for } n=k^2+1:\quad \sum_i \frac{d_i}{c_i+s_i}\;\le\;k^2 .$$
Hence, with the **total tilt cost** $T:=\sum_i d_i\Big(1-\frac{1}{c_i+s_i}\Big)$:
$$\varepsilon \;\le\; T \;\le\; \sum_i d_i(c_i+s_i-1)\;\le\;\sum_i d_i\,\theta_i .$$
Corollaries. (i) $0\le f(n)-g(n)\le T(\text{any optimal packing})$ for all $n$; a counterexample packing to Erdős's conjecture must carry total tilt $\sum d_i\theta_i\ge\varepsilon$. (ii) **Conditional constant improvement:** if a packing has $T\le 1/2-c$, then $\varepsilon\le 1/2-c$. So the only obstruction to C2 is the *tilt-heavy* regime $T>1/2-c$.

**Proof.** Every square of side $d$, tilt $\theta$, contains the concentric *axis-parallel* square of side $a=d/(c+s)$: in the square's own frame the corner $(\pm a/2,\pm a/2)$ has rotated coordinates of absolute value $\tfrac a2|\cos\theta\pm\sin\theta|\le \tfrac a2(c+s)=d/2$; convexity finishes. (Numerically verified on 2000 random $(d,\theta)$.) The inscribed squares are axis-parallel, have pairwise disjoint interiors, and lie in $[0,k]^2$; BKU (scaled: any $k^2+1$ axis-parallel squares in $[0,k]^2$ have total side $\le k\,g(k^2+1)=k^2$) gives $\sum d_i/(c_i+s_i)\le k^2$. Then $k^2+\varepsilon=\sum d_i = \sum \frac{d_i}{c_i+s_i} + T \le k^2+T$. Finally $1-\frac1{c+s}=\frac{c+s-1}{c+s}\le c+s-1\le\theta$ (the last since $h(\theta)=\theta-(c+s-1)$ has $h(0)=0$, $h'=1-c+s\ge0$). $\square$

To my knowledge this is the first unconditional inequality for the rotated problem that is not pure convexity; it says **rotation must pay for itself linearly**, and reduces C2 exactly to excluding $\{T\ge 1/2-c\}\cap\{G+V<\delta_0\}$.

### Claim 6 (Theorem T2: Wall Lemma — tilt and lift-off of wall-servicing squares are gap-controlled). Confidence: 0.95.

**Statement.** For any packing (any $n$, any sides/orientations) in $[0,k]^2$ with gap area $G$: for $x\in[0,k]$ let $\varphi(x)=\inf\{y:(x,y)\in\bigcup_i S_i\}$ ($=k$ if the vertical line misses all squares); let $A_i\subseteq[0,k]$ be the (measurable, tie-broken) set where the infimum is attained by $S_i$, $A_\emptyset$ the missed set; let $y_i\ge0$ be the height of the lowest point of $S_i$ and $v_i$ the abscissa of its lowest vertex (any point of the bottom edge if $\theta_i=0$). Then
$$\sum_i \Big( y_i\,|A_i| \;+\; \tfrac{\tan\theta_i}{4}\,|A_i|^2 \Big)\;+\;k\,|A_\emptyset| \;\;\le\;\; G,$$
and the same for the other three walls.

**Proof.** The region $R=\{(x,y):0\le y<\varphi(x)\}$ meets no square (by definition of $\varphi$) and lies in $T$, so $\int_0^k\varphi \le G$. On $A_i$, $\varphi=f_i$, the lower envelope of $S_i$, which for $\theta_i\in(0,\pi/4]$ consists of two segments of slopes $-\cot\theta_i$ and $+\tan\theta_i$ meeting at $(v_i,y_i)$; since $\cot\theta_i\ge\tan\theta_i$ on $(0,\pi/4]$, $f_i(x)\ge y_i+\tan\theta_i\,|x-v_i|$ (trivially true for $\theta_i=0$). By the bathtub principle, $\int_{A}|x-v|\,dx\ge |A|^2/4$ for any measurable $A\subseteq\mathbb R$ (worst case: interval centered at $v$). Sum over the partition $\{A_i\}\cup\{A_\emptyset\}$ of $[0,k]$. $\square$

**Sanity check** (coherent $\theta$-tilted grid resting on the wall): true wall waste per unit length $\approx\sin\theta\cos\theta$; T2 gives $\ge \tfrac14\tan\theta\cdot(c+s)$ per unit length — consistent, correct order, valid inequality. **Consequence:** in the critical regime $G<\delta_0$, wall-servicing squares satisfy $\sum\tan\theta_i|A_i|^2<4\delta_0$ and $\sum y_i|A_i|<\delta_0$ with $\sum|A_i|=k$: the boundary layer is quantitatively phase-locked and nearly axis-parallel. This is the rigorous base case of any inward-propagation scheme.

### Claim 7 (Column-tiling family: the assignment's route (a) is FALSE as stated). Confidence: 1.

**Statement.** For every integer $b\ge2$, let $k=2b(b-1)$. Then $[0,k]^2$ admits an **exact tiling by exactly $k^2+1$ axis-parallel squares** with all sides in $\big[1-\sqrt{2/k}\,(1+o(1)),\;1+\sqrt{1/(2k)}\,(1+o(1))\big]$: take $k$ vertical columns, of widths $\tfrac{k}{k+b}$, $\tfrac{k}{k+1-b}$, and $1$ ($k-2$ of them), each column of width $k/n_j$ stacked with $n_j$ squares of side $k/n_j$.

**Proof.** Widths sum: $\frac{k}{k+b}+\frac{k}{k+1-b}=2\iff k(2k+1)=2(k+b)(k+1-b)\iff k=2b^2-2b$ ✓. Piece count: $(k+b)+(k+1-b)+(k-2)k=k^2+1$ ✓. Column heights $n_j\cdot(k/n_j)=k$ ✓. Sides $k/(k+b)=1-\Theta(k^{-1/2})$, $k/(k+1-b)=1+\Theta(k^{-1/2})$. (Verified exactly by machine for $b=2,3,5,8$, i.e. $k=4,12,40,112$.) $\square$

**Consequences.** (i) The qualitative core proposed in the attack plan — "*no exact tiling of $[0,k]^2$ by $k^2+1$ squares with all sides in $[1-a,1+a]$ exists, for a suitable absolute $a$*" — is **false**: for every fixed $a>0$ it fails for all $k\ge C/a^2$ of the above form. $L^\infty$-closeness of sides to 1 has *no* rigidity content; only the $L^2$ smallness of $V$ does. (ii) These tilings have $\varepsilon=0$, $G=0$, and by the identity $(\ast)$, $V=k^2/(k^2+1)$ exactly (machine-verified: $V=0.9411\ldots=16/17$ at $k=4$, $144/145$ at $k=12$, etc.): they saturate the critical identity with the variance budget spread over $\Theta(k^{3/2})$ squares in deviations $\Theta(k^{-1/2})$, unlike the "grid + split cell" configuration (also verified: $G=1/2$, $V=(k^2-1)/(2(k^2+1))$, $G+V=k^2/(k^2+1)$ exactly), which concentrates it in $O(1)$ squares. Any proof of $G+V\ge\delta_0$ must handle *both* concentration patterns; equivalently, any near-counterexample perturbs configurations of both types. (iii) These are new(?) explicit extremal configurations for BKU's $g(k^2+1)=k$ far from the grid.

## COUNTEREXAMPLES AND SANITY CHECKS

- **Machine checks (all passed):** column-tiling family for $b=2,3,5,8$ (widths sum, piece count $=k^2+1$, $\varepsilon=0$, $G=0$, $G+V$ matches identity $(\ast)$ to $10^{-10}$); inscribed axis-parallel square $d/(c+s)$ inside every tilted square (2000 random trials); neutrality identity $\mathbb E[p+q-|S\cap\Lambda|]=2d(c+s)-d^2$ (Monte Carlo, 3 parameter pairs, error $<0.01$); chord profile: max chord $=d\sec\theta$ and $\int\mu=d^2$ (numeric integration at $\theta=0.2,0.5,\pi/4$).
- **Grid + split cell** ($k^2-1$ unit squares + two $\tfrac12$-squares): $\varepsilon=0$, $G=\tfrac12$, $V=\tfrac{k^2-1}{2(k^2+1)}$, $G+V=\tfrac{k^2}{k^2+1}$ — identity confirmed exactly by hand.
- **Coherent $\theta$-tilted grid**: T1 predicts $\varepsilon\le T\approx k^2\theta$ (vacuous, correct sign: such grids actually have $\varepsilon\approx-ck\theta<0$); Wall Lemma T2 constant checked against its true wall waste ($\tfrac14\tan\theta$ vs true $sc$ per unit length — valid).
- **Erdős–Graham cross-check**: packing $(1-a)$-side squares for $a\ge C/k$ *can* exceed $k^2$ pieces in $[0,k]^2$ (tilted-lattice packings waste only $O(k^{7/11})$), so the naive lemma "$\le k^2$ near-unit squares fit" is false without the gap constraint — consistent with Claims 2 and 7 requiring $G$ *and* $V$ small simultaneously.

## DEAD ENDS

1. **A fake averaging re-proof of BKU.** Chain: $\Phi\le k^2$ a.s., $\mathbb E\Phi=k^2-G$, Markov $\Rightarrow\Phi=k^2$ w.p. $\ge1-G$; on that event $\ge1$ square is lattice-empty; so $\sum_i U_i\ge1-G$ where $U_i$ = torus measure uncovered by $S_i\bmod\mathbb Z^2$. Looked like it gave $\varepsilon\le0$ for axis-parallel via "$U_i=(1-d_i)^2$" — but that value is wrong ($U_i=1-d_i^2$ for $d_i\le1$: a $d<1$ square mod 1 covers only its own area). With the correct $U_i$ the chain is strictly weaker than the trivial pointwise bound $Z\ge n-\Phi$, whose expectation is the *identity* $\sum U_i = 1+G+\sum(\text{self-overlap}_i)$. Zero content. Generalized post-mortem = Claim 4(iii): all per-square first moments are identities.
2. **Chord slicing for the "+1"**: pointwise family inequality $\sum M_i(x_0)\le k^2$ averages exactly to the area bound (Claim 3(b)); no route to the extra unit without count integrality.
3. **Grain-boundary energy budget for the tilt-heavy case.** Attempted: $T\ge1/2-c$ and $G<\delta_0$ impossible via "misoriented grain of $M$ squares, tilt $\theta$, wastes $\gtrsim\sqrt M\,\theta$ at its boundary". Even granting this unproved waste law, the **giant gentle grain** ($\theta\sim\delta_0^4$, $M\sim T/\theta$, diameter $\ll k$) achieves $T\ge1/2$ with boundary waste $\sim\sqrt{T\theta}\sim\delta_0^2<\delta_0$: *not excluded*. Gap accounting alone cannot kill the tilt-heavy regime; exactly the marginality of Warning 4, now localized to a specific enemy.
4. **Rigid grain untilting.** Rotating a diameter-$L$ grain back by $\theta$ displaces boundary points by $L\theta$, so the conflicted layer has $\sim\sqrt M\cdot L\theta = M\theta$ squares-worth of repair — total repair cost $\sim T$, the same as per-square shrinking (T1). Rigid rotation does **not** beat the inscribed-square bound for round grains; T1's linear loss is intrinsic to all shrink/rotate repair schemes.
5. **Quantitative near-tiling rigidity from $L^\infty$ side control** (assignment route (a) as written): refuted outright by Claim 7.
6. **Second moment of $\Phi$**: $\operatorname{Var}(\Phi)=\operatorname{Var}(\gamma)\le k^2G$ with $\gamma\ge0$, $\mathbb E\gamma=G$ — no lower-bound mechanism on $\operatorname{Var}$ without structural input; abandoned.

## BEST NEXT STEP

By T1 the entire remaining content of C2 is the **tilt-heavy exclusion**: *no packing of $k^2+1$ squares in $[0,k]^2$ has simultaneously $T\ge\tfrac12-c$ and $G+V<\delta_0$.* The extremal enemy is now explicit (Dead End 3): a single huge coherent grain of $M\sim\theta^{-2}$ near-unit squares at gentle tilt $\theta\to0$, floating in an axis-parallel sea, carrying $T\sim M\theta$ with only $O(\sqrt M\theta)$ boundary gap. The decisive lemma to attempt — and it is counting-shaped, not gap-shaped, so it should be coordinated with Route A:

> **Quadratic-cost BKU.** There is an absolute $C$ such that every packing (any orientations) of $k^2+1$ squares in $[0,k]^2$ satisfies $\sum_i d_i\le k^2 + C\sum_i d_i\,\theta_i^2 + CG$.

This is consistent with the neutrality identity (Claim 4(ii): first-order tilt terms cancel exactly, so the true cost should be second order), it is *not* contradicted by tilted grids ($\varepsilon<0$ there), and it kills the giant gentle grain: $\varepsilon\le CT\theta+C\delta_0\ll1/2$. Combined with T1, one then splits per square: tilts $\le\theta^*$ handled by quadratic-cost BKU, tilts $>\theta^*$ contribute $T$-mass at unit rate and should be chargeable to $G$ locally via wedge arguments seeded by the Wall Lemma T2 (whose per-layer propagation, with total gap budget $\delta_0$ shared additively across layers, is the natural proof scaffold for the large-tilt case). Concretely: prove quadratic-cost BKU first for a *single coherent tilted grain in an axis-parallel remainder* by running BKU's count with the container-aligned lattice and showing the grain's counting defect at the pigeonholed shift is $\le M\theta^2\cdot C$ plus boundary terms — the one-grain case is finite-dimensional in the right way and would already exclude the extremal enemy.