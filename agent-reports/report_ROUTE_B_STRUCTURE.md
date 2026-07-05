All numerical checks pass. Writing the final report now.

## CLAIMS

Throughout: arena $T=[0,k]^2$, $N=k^2$, squares $S_1,\dots,S_{N+1}$ (closed, pairwise disjoint interiors), sides $d_i$, orientations $\theta_i$, **folded tilt** $\tau_i:=\mathrm{dist}(\theta_i,\tfrac{\pi}{2}\mathbb Z)\in[0,\pi/4]$. Gap $\Omega=T\setminus\bigcup S_i$, $G:=\mathrm{area}(\Omega)=N-\sum d_i^2$. "Near-extremal" means $\sum d_i=N+\varepsilon$, $\varepsilon>0$. Verification scripts: `/private/tmp/claude-501/-Users-kylekabasares-Desktop-erdos-106/6b0597a9-48bd-4e8c-a957-7fc4a05f26d8/scratchpad/routeB_checks.py` (all checks referenced below are in its output).

---

### Claim 1 (Exact budget identity; $\varepsilon<1/2$ automatic; deviant counts). Confidence 1.0.

Let $m=\frac{N+\varepsilon}{N+1}$, $V:=\sum_i (d_i-m)^2$. Then for any packing with $\sum d_i=N+\varepsilon$:

$$G+V \;=\; N-\frac{(N+\varepsilon)^2}{N+1}\;=\;\frac{N-2N\varepsilon-\varepsilon^2}{N+1}\;\le\;1-2\varepsilon .$$

Moreover $\varepsilon<1/2$ holds automatically for every packing, and if $\varepsilon>0$:
(a) every $d_i< m+\sqrt V<2$;
(b) the set $\mathcal D$ of **deviants** ($d_i\notin[0.9,1.1]$) has $|\mathcal D|\le V/0.09^2\le 124$ and $\sum_{i\in\mathcal D} d_i\le 124\,m+\sqrt{124\,V}<136$ (for $k\ge 10$).

**Proof.** $V=\sum d_i^2-(N+1)m^2=\sum d_i^2-\frac{(N+\varepsilon)^2}{N+1}$, so $G+V=N-\frac{(N+\varepsilon)^2}{N+1}$, and $(N+1)(1-2\varepsilon)-(N-2N\varepsilon-\varepsilon^2)=(1-\varepsilon)^2\ge0$ gives the bound. $\varepsilon<1/2$: since $\sum d_i^2\le \mathrm{area}(T)=N$, Cauchy–Schwarz gives $\sum d_i\le\sqrt{(N+1)N}<N+\tfrac12$. (a): $(d_i-m)^2\le V\le 1$, $m<1$. (b): $|d_i-1|\ge 0.1$ and $1-m=\frac{1-\varepsilon}{N+1}\le\frac1{N+1}\le 0.01$ give $|d_i-m|\ge 0.09$; count by Chebyshev; the sum by Cauchy–Schwarz on $\sum_{\mathcal D}|d_i-m|$. $\blacksquare$

*Interpretation: total gap + total side-variance in a hypothetical counterexample is below one unit cell; all structure results below only get to spend this budget.*

---

### Claim 2 (Tangent-cone facts; parallel-contact rigidity). Confidence 1.0.

Let $S$ be a square and $x_0\in\partial S$. The tangent cone $C(S,x_0)$ is a right-angle wedge (if $x_0$ is a vertex) or a half-plane (if $x_0$ is edge-interior), its boundary rays lie along edge directions of $S$, and $S\subseteq C(S,x_0)$ **globally**, with $S\cap B(x_0,\rho)=C(S,x_0)\cap B(x_0,\rho)$ for $\rho$ less than the distance from $x_0$ to the non-incident vertices/edges.

**(Parallel contact.)** If squares $S_1,S_2$ have disjoint interiors and touch at a point interior to an edge of *both*, then those edges are collinear-parallel, so the folded mismatch $\alpha:=\mathrm{dist}(\theta_1-\theta_2,\tfrac\pi2\mathbb Z)=0$.

**Proof.** Cone facts: a square is the intersection of the half-planes of its edge lines; near $x_0$ only incident edges matter. Parallel contact: both cones are half-planes with disjoint interiors whose union lies in the disk; two half-planes through one point with disjoint interiors are complementary, hence have the same boundary line; boundary rays are edge directions. $\blacksquare$

**Consequence: any contact between squares with mismatch $\alpha>0$ involves a vertex of at least one square.**

---

### Claim 3 (Sector Lemma = B1, exact form). Confidence 1.0. (Numerically verified: CHECK 3, min ratio $1.0009\ge 1$ over 400 random contact configurations.)

Let $S_1,S_2$ have disjoint interiors, touch at $x_0$, with folded mismatch $\alpha>0$. Then within $B(x_0,r)$ the complement of the two tangent cones consists of **exactly two open sectors with apex $x_0$, of angles $\gamma_1,\gamma_2$ with $\gamma_1+\gamma_2\in\{\pi/2,\pi\}$ (vertex–edge / vertex–vertex) and $\gamma_1,\gamma_2\ge\alpha$**, each sector flush against an edge-ray of one of the squares. Consequently, **for every $r>0$**

$$\mathrm{area}\big(B(x_0,r)\setminus(S_1\cup S_2)\big)\;\ge\;\tfrac{\gamma_1+\gamma_2}{2}\,r^2\;\ge\;\alpha\,r^2 ,$$

and the flush sector adjacent to a given edge has area **exactly** $\tfrac{\gamma}{2}r^2$ (no $O(\alpha^2r^2)$ correction) as long as it is measured against the cones. This is the cleanest true form of the assignment's "$\alpha r^2/2+O(\alpha^2r^2)$" question: the correction terms appear only when $r$ exceeds the distance from $x_0$ to an edge endpoint, not from the angle.

**Proof.** By Claim 2 the case edge–edge is excluded, so $|C_1|+|C_2|\in\{\pi/2+\pi,\ \pi/2+\pi/2\}$; cones have disjoint interiors (they agree with the disjoint squares near $x_0$), so the complement in the circle of directions has total angle $2\pi-|C_1|-|C_2|\in\{\pi/2,\pi\}$, split into at most two sectors, each bounded by one edge-ray of $S_1$ and one of $S_2$. A sector angle $\gamma$ is therefore congruent to $\pm(\theta_1-\theta_2)\bmod \tfrac\pi2$; $\gamma=0$ would force $\alpha=0$; hence $\gamma\in\{\alpha,\tfrac\pi2-\alpha,\tfrac\pi2+\alpha,\pi-\alpha\}$, all $\ge\alpha$ ($\alpha\le\pi/4$), and neither sector can be empty. The area bound holds for all $r$ because $S_j\subseteq C_j$ globally. $\blacksquare$

*Caveat (honest): the lemma bounds area uncovered by the pair; third squares may fill the sectors. Claims 5–7 are the tools that survive this.*

---

### Claim 4 (Surrounded-point alignment — the local crystallization law; wall version). Confidence 0.97.

Call $x_0$ **buried** if a neighborhood of $x_0$ is covered by $\bigcup_i S_i$. If $x_0$ is buried and lies on the boundary of every square containing it, then **all squares containing $x_0$ have the same orientation mod $\pi/2$**, and the corner multiset at $x_0$ is one of $\{\pi,\pi\}$, $\{\pi,\frac\pi2,\frac\pi2\}$, $\{\frac\pi2,\frac\pi2,\frac\pi2,\frac\pi2\}$. If $x_0\in\partial T$ is covered relative to $T$ (or, more generally, one of the bodies at $x_0$ is a half-plane wall), all squares at $x_0$ are additionally **axis-parallel** ($\tau=0$).

**Proof.** Near $x_0$ each square equals its tangent cone (Claim 2). The cones have pairwise disjoint interiors and cover a disk, so their angular sectors partition the circle; consecutive sectors share boundary rays (a positive angular gap between consecutive sectors would be uncovered arbitrarily close to $x_0$). A shared ray is an edge direction of both neighbors, hence consecutive squares agree mod $\pi/2$; chain around the circle. Angle bookkeeping: parts from $\{\pi/2,\pi\}$ summing to $2\pi$ give exactly the three listed multisets. Wall version: include the tangent cone of $T$ (half-plane or quarter-plane of orientation $0$) as one sector and run the same chain. $\blacksquare$

**Corollary (grains).** Define $S_i\approx S_j$ if they share a buried contact point; connected components of $\approx$ ("grains") are orientation-coherent mod $\pi/2$. Every contact point between distinct grains, and every contact with mismatch $\alpha>0$, is non-buried, i.e. lies in $\overline{\Omega}$: **the gap wets all misaligned interfaces** (topological statement; quantitative version is the open part, see Claim 10).

---

### Claim 5 (Tiling rigidity: every tiling of a rectangle by finitely many squares is axis-parallel). Confidence 0.9.

**Proof.** A finite union of closed squares of total area equal to the rectangle $R$, with disjoint interiors, covers $R$ (the complement is open with zero area, hence empty), so *every* point is buried (relative to $R$). Suppose some tile is tilted; among tilted tiles pick $S^*$ minimizing the height $y^*$ of its lowest vertex $v$ (unique since $\tau^*>0$). If $v\in\partial R$: Claim 4 (wall version) forces $\tau^*=0$, contradiction. If $v\in\mathrm{int}\,R$: Claim 4 makes all squares at $v$ share $S^*$'s orientation mod $\pi/2$, i.e. all are tilted with the same folded tilt $\tau^*>0$. The cone of $S^*$ at its lowest vertex opens strictly upward (edge directions at angles $\tau^*,\tau^*+\frac\pi2\in(0,\pi)$), so the downward ray at $v$ lies in the cone of some other tile $S'$ at $v$; then $S'$ contains points strictly below $y^*$, so its lowest vertex is $<y^*$, and $S'$ is tilted — contradicting minimality. $\blacksquare$

*(Consequence for the program: exact tilings obey BKU; a counterexample to $f(k^2+1)=k$ needs $G>0$, and by Claim 1 it must spend $G<1-2\varepsilon$.)*

---

### Claim 6 (Chord/Wedge Lemma for a tilted square over a floor). Confidence 1.0. (CHECK 1/1b: 0 violations over 3000 random squares; exact area formula to $2\cdot10^{-16}$.)

Let $S$ be a square, side $d$, folded tilt $\tau\in(0,\pi/4]$, lowest point at height $y_v$. Let $\mathrm{ch}(y)$ be the length of the horizontal chord of $S$ at height $y$. Then:

(a) $\mathrm{ch}(y)\le \dfrac{2\,(y-y_v)^+}{\sin 2\tau}$ for **all** $y$, with equality iff $0\le y-y_v\le d\sin\tau$;
(b) $\mathrm{area}\big(S\cap\{y\le Y\}\big)\le \dfrac{((Y-y_v)^+)^2}{\sin 2\tau}$, with equality iff $Y-y_v\le d\sin\tau$;
(c) (used in Claim 7) if $Y-y_v\le d\sin\tau$ then $\mathrm{area}(S\cap\{y\le Y\})=\tfrac12 (Y-y_v)\,\mathrm{ch}(Y)$.

**Proof.** At the lowest vertex the two edges rise at angles $\tau$ and $\tau+\frac\pi2$; at height $s=y-y_v\le d\sin\tau$ (the height of the lower adjacent vertex; $\sin\tau\le\cos\tau$) the cross-section is the interval between these edges, of width $s(\cot\tau+\tan\tau)=2s/\sin2\tau$. For $s>d\sin\tau$: chords of a convex body along parallel lines are a concave function of the height (1-D Brunn–Minkowski / trapezoid rule for polygons); concave with value $0$ at $s=0$ implies $\mathrm{ch}(s)/s$ is non-increasing, so $\mathrm{ch}(s)\le s\cdot\frac{\mathrm{ch}(d\sin\tau)}{d\sin\tau}=\frac{2s}{\sin2\tau}$. (b),(c) integrate (a). $\blacksquare$

---

### Claim 7 (Window Theorem = B2, explicit constants). Confidence 0.9. (CHECK 2: holds with factor 3–4 slack on coherent tilted grids, $k=30$, $t\in\{0.05,0.2,0.775\}$.)

Fix $t\in(0,\pi/4]$ and set $\delta:=0.9\sin t\ (\le 0.64)$. Let $W=[a,a+L]\times[0,\delta]\subseteq T$ be a **wall window strip** ($L\ge 1$). Suppose every non-deviant square ($d_i\in[0.9,1.1]$) meeting $W$ has folded tilt $\tau_i\ge t$. Then

$$\mathrm{area}(W\setminus\textstyle\bigcup_i S_i)\;\ge\;\delta\Big(\tfrac{L}{2}-1.56\Big)\;-\;\sqrt2\,\delta \sum_{i\in\mathcal D,\ S_i\cap W\neq\emptyset} d_i .$$

**Proof.** Any square meeting $W$ has $y_{v,i}<\delta$ and $y_{v,i}\ge0$ (container). Non-deviant meeting $W$: $\tau_i\ge t>0$ and $d_i\sin\tau_i\ge 0.9\sin t=\delta\ge\delta-y_{v,i}$, so Claim 6(c) applies at $Y=\delta$:
$\mathrm{area}(S_i\cap W)\le \mathrm{area}(S_i\cap\{y\le\delta\})=\tfrac12(\delta-y_{v,i})\,\mathrm{ch}_i(\delta)\le\tfrac{\delta}{2}\,\mathrm{ch}_i(\delta)$.
The chords at height $\delta$ are disjoint intervals; every such square crosses height $\delta$ (vertical extent $d_i(\cos\tau_i+\sin\tau_i)\ge0.9>\delta$) and has diameter $\le\sqrt2\cdot 1.1<1.56$, so all these chords lie in $[a-1.56,\,a+L+1.56]$, whence $\sum_i \mathrm{ch}_i(\delta)\le L+3.12$. Deviants: $\mathrm{area}(S_i\cap W)\le\delta\cdot(\text{max horizontal chord})\le\sqrt2\,\delta d_i$. Subtract from $\mathrm{area}(W)=L\delta$. $\blacksquare$

The same holds at all four walls (rotate). **Approximate-wall version (proved the same way):** if the "floor" is only known to satisfy $y_{v,i}\ge -h$ (squares may start up to $h$ below the reference line, e.g. the top envelope of a lower row with height roughness $h$), the bound degrades exactly by $\tfrac{h}{2}(L+3.12)$: replace $\delta-y_{v,i}\le\delta$ by $\le\delta+h$.

---

### Claim 8 (No coherently tilted near-extremal packing; quantitative min-tilt). Confidence 0.9.

Let $k\ge10$ and let the packing satisfy $\sum d_i>N$ (so Claim 1 applies). Partition the bottom wall into $\lfloor k/8\rfloor$ windows of length $L=8$. If **every** square has folded tilt $\ge t$, then every window satisfies Claim 7's hypothesis, each deviant meets $\le2$ windows (diameter $<3<8$), and summing over disjoint window strips:

$$1>G\;\ge\;\delta\big(2.44\lfloor k/8\rfloor-2\sqrt2\cdot136\big)\;\ge\;0.9\sin t\,(0.3k-388).$$

Hence: **in any packing of $k^2+1$ squares in $[0,k]^2$ with $\sum d_i>k^2$, some square has folded tilt $<\arcsin\frac{1}{0.27k-350}$** (meaningful for $k\ge1300$; $<4/k$ for $k\ge17500$). Equivalently (fitting loss, coherent branch of B4): a packing whose every square is tilted at least $t$, with $\sin t\ge\frac{1}{0.27k-350}$, has $\sum d_i\le k^2$. This confirms, with explicit constants, that a **global rigid rotation by $t\gtrsim 1/k$ is dead** — the loss is linear in $k\sin t$, exactly the predicted order of the fitting obstruction. Confidence 0.9 (the constants were re-derived twice and stress-tested numerically; the logic is elementary).

---

### Claim 9 (Boundary anchoring: $\Omega(k)$ aligned wall squares, and a summed-tilt bound). Confidence 0.85.

Assume $\sum d_i>N$, $k\ge10$. For window $j$ let $t_j:=\min\{\tau_i:\ S_i \text{ non-deviant},\ S_i\cap([8(j-1),8j]\times[0,0.64])\neq\emptyset\}$ (set $t_j=\pi/4$ if none). Then:

(a) **Summed-tilt bound (B2 target form).** Excluding the $\le 248$ windows met by deviants,
$$\sum_{j\ \mathrm{dev\text{-}free}}\sin t_j\;<\;\frac{G}{2.19}\;\le\;0.46 .$$
*Proof:* apply Claim 7 to window $j$ with $t=t_j$, $\delta_j=0.9\sin t_j$ (squares meeting the shorter strip $[0,\delta_j]$ are among those meeting the tall strip, hence have $\tau\ge t_j$); window strips are disjoint in $x$, so the gap contributions add. $\blacksquare$

(b) **Existence of many aligned wall squares.** Taking $\sin t=5/k$: the number of "bad" windows is $\le \frac{1}{2.44\,\delta}+158\le 0.092k+158$, so at least $0.033k-160$ windows each contain a non-deviant square with folded tilt $<\arcsin(5/k)\le 5.1/k$ and lowest point within $4.5/k$ of the wall; since a square meets $\le2$ windows, this yields $\ge k/120$ **distinct** such squares for $k\ge2\cdot10^4$ — per wall. **Near-extremal packings are pinned to orientation $0$ at $\Omega(k)$ spots on each wall.**

---

### Claim 10 (What closes and what does not: the B4 dichotomy, honestly). Confidence 1.0 in the meta-statements.

Proved above: (i) exact local crystallization law (Claim 4) — misalignment cannot be buried; (ii) tilings rigid (Claim 5); (iii) wall anchoring with linear-in-$k$ leverage (Claims 7–9); (iv) coherent global tilt $t\gtrsim1/k$ impossible (Claim 8); (v) pairwise mismatch cost is exactly sectorial, $\ge\alpha r^2$ against the pair (Claim 3), and the staircase construction (CHECK 4: disjointness verified, measured cost $0.456$ vs $\tan\alpha/2\cdot 6=0.453$) shows the **true optimal interface cost between a $0$-grain and an $\alpha$-grain is $\Theta(\alpha)$ per unit length** as an upper bound.

**GAP 1 (interior interface lower bound).** No proof that an interior misaligned interface of length $\ell$ costs $\ge c\,\alpha\,\ell$ gap area. Obstruction: the sector at each mismatched contact has unquantified persistence radius — a third square can truncate it at radius $\rho\ll1$; the mismatch then propagates to a new contact (folded mismatch is a metric, so one of the new contacts inherits $\ge\alpha/2$), but I could not close the induction: the propagation chain's total charge is not yet controlled (near-contacts at clearance $h$ weaken the sector bound to $\alpha r^2-O(hr)$, and clearances are unconstrained).

**GAP 2 (the $\varepsilon/k^2\ll t\ll 1/k$ hole).** Route A (robust BKU) plausibly needs total tilt mass $\sum_i d_i\tau_i\lesssim\varepsilon$, i.e. typical $\tau\lesssim\varepsilon/k^2$. Route B kills coherent tilts only down to $\tau\sim1/k$ (Claim 8; wall leverage is $\sim k\sin t$ against budget $1$, and this order is *correct* — the tilted-grid construction wastes only $\Theta(k\sin t)$). Between these, a coherent grain tilted by $t\in(\varepsilon/k^2,\,C/k)$ costs $O(kt)\le O(1)$ gap — affordable within the Claim 1 budget — and defeats both routes as currently formulated. **Closing either GAP 1 (to localize grains) or improving Route A's tolerance to coherent small tilts (second-moment/shift-optimized counting) is necessary; Route B alone cannot finish.**

**Remark (discrete Gauss–Bonnet).** Around any simply connected gap component with $m$ boundary corners, interior angles sum to $(m-2)\pi$; each corner angle is a multiple of $\pi/2$ plus a signed orientation difference of the two incident squares, giving the cocycle relation $\sum_{\text{cycle}} \pm(\theta_i-\theta_j)\equiv 0 \pmod{\pi/2}$ around every gap component. This constrains frustrated textures but carries no area lower bound by itself (angles close up for free in "gradient" textures); I therefore demoted it from theorem-target to bookkeeping tool.

## COUNTEREXAMPLES AND SANITY CHECKS

- **CHECK 1/1b** (3000 random squares): chord bound and exact wedge-area formula of Claim 6 — 0 violations, equality confirmed on the wedge range.
- **CHECK 2**: Window Theorem tested against coherently tilted grids clipped to $[0,30]^2$ at $t=0.05,\,0.2,\,0.775$: measured strip gaps $1.33,\ 5.11,\ 18.6$ vs theorem bounds $0.32,\ 1.29,\ 4.54$. Holds with factor $3$–$4$ slack — constants are not tight but not vacuous.
- **CHECK 3**: Sector Lemma on 400 random vertex–edge contact configurations: $\min \mathrm{area}/(\alpha r^2)=1.0009\ge1$.
- **CHECK 4**: staircase interface (axis-parallel stair row + flush $\alpha$-tilted row on the line through stair corners, $\alpha=0.15$): SAT-verified disjoint; measured gap per unit length $=0.0760$ vs $\tan\alpha/2=0.0755$. Confirms (as an upper bound) that interface cost is linear in $\alpha$, hence any B3 lower bound must also be linear — quadratic-in-$\alpha$ conjectures are false, and "gradient" textures (orientation drifting by $\alpha$ over $m$ rows) genuinely spread the cost.
- Consistency with known obstructions: the Window Theorem's leverage vanishes exactly on axis-parallel packings ($t\to0$), so it cannot contradict the LP-duality barrier; it uses integrality-free geometry and therefore *cannot alone* prove the conjecture — it only supplies structure to feed a counting argument.
- Claim 8's linear loss $\Theta(k\sin t)$ matches the tilted-grid construction's actual waste (upper bound), so the coherent branch is closed at the right order, not by a lucky weak bound.

## DEAD ENDS

1. **Interior 1-D slicing.** On any interior line, a tilted square's chord is *longer* ($\le d/\cos\tau$, $\ge$ average $d/(\cos\tau+\sin\tau)$); per-line accounting sees no tilt penalty in the interior. All slice-based waste is a boundary effect. Interior crystallization cannot come from slices; it must be a two-orientation interaction (pairwise geometry) or counting.
2. **Naive sector charging (B3).** Sector persistence radius is not lower-boundable: truncating squares can enter at any depth; propagation chains resist a clean monovariant. (Recorded as GAP 1 with the exact failure mode.)
3. **Isoperimetric charging of gap components.** Thin slivers have huge perimeter and tiny area; "perimeter $\ge c\sqrt{\text{area}}$" charges the wrong way. Angular (Gauss–Bonnet) accounting closes exactly (cocycle relation) and yields no area.
4. **Rotated-frame BKU for coherent tilt.** In the squares' frame the container is tilted; the lattice budget acquires an $O(k)$ shift-dependent boundary excess, and mean-value pigeonholing then gives only $\sum d_i\lesssim k^2+O(k)$ — strictly weaker than Cauchy–Schwarz. Consistent with the break-even principle in the parent notes.
5. **Row-by-row bootstrap of the Window Theorem.** The approximate-wall version (end of Claim 7) costs an extra $Lh/2$ per window for floor roughness $h$; propagating from the anchored wall row upward, roughness accumulates like per-row side deviations, and $\sum_{\text{rows}} h_j$ is only bounded by $\sim\sqrt{kV}$, giving total charge $\sim k\sqrt{kV}\gg1$. Naive iteration fails; a self-correction (negative feedback of gaps on heights) would be needed.

## BEST NEXT STEP

Prove the **interface lemma** that upgrades Claim 7 from the container wall to internal reference lines, in the following concrete form: *if a segment $\ell$ of length $L$ admits a "rough floor" — a set of squares covering all of $\{$dist $\le h$ below $\ell\}$ except area $g_0$ — then the strip above $\ell$ obeys the Window bound degraded by $L h/2+g_0$.* The proof of Claim 7 already gives the $Lh/2$ term; what is missing is a mechanism that bounds the accumulated roughness $h_j$ of successive rows by *locally available gap* rather than by side-variance (the failure in Dead End 5). The most promising mechanism: use Claim 9's $\Omega(k)$ wall anchors as boundary conditions and prove a *height self-correction* inequality — a row whose top envelope is rough by $h$ over a window either pays gap $\ge c\,h$ inside that window (not just above it) or contains a deviant — turning roughness itself into a charged quantity. If that closes, induction gives alignment and near-grid position control through $\Theta(1)$ rows of depth per unit of gap budget, which is exactly the structure a shift-optimized robust-BKU (Route A) needs at the boundary rows where its pigeonhole failures concentrate; jointly this would attack the remaining $t\in(\varepsilon/k^2,1/k)$ hole at its only load-bearing location, the container boundary.