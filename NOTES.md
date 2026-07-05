# Erdős Problem #106 — working notes (main analysis)

**Problem.** $f(n)$ = max total side length of $n$ squares with pairwise disjoint interiors
inside the unit square $U=[0,1]^2$, **arbitrary rotations allowed**. Conjecture (Erdős ~1932):
$f(k^2+1)=k$. Open. Axis-parallel variant $g$ solved: Baek–Koizumi–Ueoro, arXiv:2411.07274
($g(k^2+2c+1)=k+c/k$). Known rotated results: $f(2)=1$ (Erdős), $f(5)=2$ (Newman, unpublished),
$f(k^2)=k$ (Cauchy–Schwarz). Singh (arXiv:2506.23284, 2601.22163): $k\,\varepsilon(k)$ is
non-decreasing where $\varepsilon(k)=f(k^2+1)-k$; hence conjecture ⟺ $f(k^2+1)\le k+o(1/k)$
along any subsequence ⟺ true for infinitely many $k$.

## 1. Scaled reformulation and the single missing lemma

Scale by $k$: arena $T=[0,k]^2$, $N=k^2$, squares $S_1,\dots,S_{N+1}$, sides $d_i$, suppose
$\sum d_i > N$. For any shifted aligned unit lattice $\Lambda_p=\mathbb{Z}^2+p$ (half-open
conventions), disjointness+containment give $\sum_i |S_i\cap\Lambda_p| \le |T\cap\Lambda_p| = N$
for every $p$. So the **only missing lemma** is:

> **(ML)** A packing of $N+1$ squares (any orientations) in $T$ with $\sum d_i>N$ admits a shift
> $p$ with total lattice count $\ge N+1$.

BKU prove (ML) for axis-parallel squares: $p_i,q_i$ = numbers of vertical/horizontal grid lines
meeting $S_i$; $\int p_i\,dx_0=d_i$; pigeonhole gives $x_0,y_0$ with $\sum p_i,\sum q_i\ge N+1$;
axis-parallelism gives the *product structure* $c_i=|S_i\cap\Lambda_p|=p_iq_i$ and
$p_i,q_i\in\{\lfloor d_i\rfloor,\lceil d_i\rceil\}$ ⟹ $|p_i-q_i|\le1$ ⟹ $p_iq_i\ge p_i+q_i-1$;
sum: $N \ge \sum c_i \ge \sum p_i+\sum q_i-(N+1)\ge N+1$, contradiction.

## 2. Corner-triangle decomposition for a tilted square

Square $S$, side $d$, tilt $\theta\in(0,\pi/4]$. Its bounding box is a $w\times w$ square,
$w=d(\cos\theta+\sin\theta)$, and $\mathrm{bbox}(S)\setminus S$ = 4 right triangles with legs
$d\cos\theta\times d\sin\theta$ (total area $w^2-d^2=d^2\sin2\theta$). Both projections of $S$
have the same width $w$, so $|p-q|\le1$ still holds for every shift and any tilt. The crossing
of a vertical and a horizontal line meeting $S$ lies in $\mathrm{bbox}(S)$; hence
$$c = pq - e,\qquad e := \#\{\text{lattice points in the 4 corner triangles}\}.$$
The per-square BKU inequality $c\ge p+q-1$ becomes exactly
$$e \le (p-1)(q-1).$$
This **fails pointwise for every $\theta>0$** (e.g. $p=q=1$ with the unique crossing in a thin
corner triangle), so no verbatim pointwise extension exists; failures have shift-measure
$O(d^2\theta)$ per square.

## 3. Exact criticality identity (new, verified numerically)

For $1\le w\le 2$, over the uniform shift torus ($p,q$ independent, $p-1\sim$ Bernoulli$(w-1)$):
$$\underbrace{\big(\mathbb{E}[p]-d\big)+\big(\mathbb{E}[q]-d\big)}_{\text{projection surplus}=2(w-d)}
-\underbrace{\Big(\mathbb{E}[e]-\mathbb{E}[(p-1)(q-1)]\Big)}_{\text{net counting defect}=(w^2-d^2)-(w-1)^2}
= (1-d)^2 .$$
*Proof:* algebraic: $2(w-d)-(w^2-d^2)+(w-1)^2=d^2-2d+1$. (Monte Carlo verified,
`scratchpad` script, all $(d,\theta)$ tested.)

**Interpretation.** In expectation over shifts, the extra projection mass a tilted square gains
*exactly* pays for its expected counting defect, with safety margin $(1-d)^2$ — which vanishes
precisely at the critical side $d=1$ (scaled; i.e. side $1/k$ unscaled), the side length forced
in near-extremal configurations. So the tilted problem is **exactly critical in expectation at
every tilt angle**, not just as $\theta\to0$; first-moment arguments cannot decide it (this
subsumes the LP-duality obstruction). Any successful counting proof must extract
max-over-shifts gains beyond the mean (equidistribution / second-moment leverage) or inject
geometric structure (gap forcing).

## 4. Near-extremal structure

If $\sum d_i = N+\varepsilon$ ($\varepsilon>0$), Cauchy–Schwarz gives, with
$G:=N-\sum d_i^2$ (total gap area) and $V:=\sum_i(d_i-\bar d)^2$:
$$G+V \le 1-2\varepsilon+O(\varepsilon^2/N).$$
Total gap + total squared side-deviation less than **one unit cell** over the whole $k\times k$
arena. Consequences: near-tiling by near-unit squares; exact tilings are automatically
axis-parallel (folklore) and hence obey BKU; genuine counterexamples need gaps but less than
one cell's worth. Note the identity in §3: the total expected counting safety margin is exactly
$\sum_i(1-d_i)^2 \approx V$ — the same quantity the Cauchy–Schwarz budget caps. Criticality
everywhere.

## 5. Obstructions catalogued

1. **LP gap:** fractional packings with multiplicity $N+1$ achieve $\ge k+\tfrac{1}{2k+1}$
   (mix $k$-grid and $(k{+}1)$-grid tilings, weights $\tfrac{2k}{2k+1},\tfrac{1}{2k+1}$) —
   matches Cauchy–Schwarz; no pure convex-duality proof can give $k$.
2. **Rotated counting lattices** blow an $O(k)$ boundary budget — fatal when fighting for +1.
3. **Per-square untilting** (rotate about center, shrink by $1/(\cos\theta+\sin\theta)$) costs
   $\sum d_i\theta_i$; a coherent tilted $m\times m$ grain only shows gap $\sim m\theta$ at its
   boundary ⟹ rounding must treat grains rigidly.
4. **Marginal global mode:** coherent tilt $t$ of the whole configuration costs $\sim Nt$
   side-length (fitting) and its counting defect is also $\sim Nt$; with $t\sim\varepsilon/N$
   both are $\sim\varepsilon$ — decided by constants, and §3 says the first-order constants tie.
5. **Pigeonhole conditioning:** good shift sets can have measure $\sim\varepsilon$; conditional
   defect expectations inflate by $1/\varepsilon$.

## 6. Attack routes (delegated to parallel agents, workflow `wf_5f6ab1ff-90f`)

## 5.5 Break-even principle for rotated counting frames (new)

The diagonal lattice $\Lambda_\diamond$ generated by $(\tfrac12,\tfrac12),(\tfrac12,-\tfrac12)$
contains $\mathbb{Z}^2$, so $|[0,k)^2\cap(\Lambda_\diamond+p)|=2k^2$ **exactly for every
shift** (it is a union of two shifted copies of $\mathbb{Z}^2$). In its own 45° frame it is
$(1/\sqrt2)\mathbb{Z}^2$. A 45°-tilted square of side $d$ is axis-parallel in that frame, so
BKU counting applies — but with line spacing $1/\sqrt2$ and budget $2N$: the contradiction
threshold becomes $\sqrt2\sum d_i > 2N$, i.e. $\sum d_i > \sqrt2\,N$. Break-even with
Cauchy–Schwarz, no gain. This is general: for any commensurate frame,
(budget)·(spacing)$^2$ = area$(T)$ is invariant and per-axis capture scales like $d/$spacing,
so **any single-lattice counting scheme sits exactly at the Cauchy–Schwarz break-even for
squares misaligned with the container**. BKU's leverage exists only because the squares share
the container's frame at spacing 1. Hence all genuine leverage against rotated squares must
come from cross-orientation interaction (forced gaps) or from shift-optimization strictly
beyond the mean — consistent with §3.

## 6. Attack routes (delegated to parallel agents, workflow `wf_5f6ab1ff-90f`)

A. Robust BKU under small tilts (per-square $e\le(p-1)(q-1)$ failure analysis).
B. Structure/crystallization: gaps force orientation alignment (discrete Gauss–Bonnet idea);
   coherent tilt forces fitting loss.
C. Unconditional constant improvement: $f(k^2+1)\le k+(1/2-c)/k$ via
   "$G+V\ge\delta_0$ for $k^2+1$ squares" (no near-perfect near-equal near-tiling with a
   non-square count).
D. Wildcard budgets: two-frame/diagonal lattices ($|T\cap\Lambda|$ exact), Pythagorean-angle
   commensurate lattices along subsequences of $k$ (allowed by Singh!), square↔cell matching.
E. Small cases: full proof of $f(2)=1$; independent proof of Newman's $f(5)=2$; the equivalent
   gap-witness form: $f$-conjecture ⟺ uncovered area $\ge 2\sum_{i<j}s_is_j-(k^2-1)$.
Numerics: counterexample stress-test ($n=2,5,10,17$) + tilt-penalty curve + defect/surplus and
interface gap-cost constants.

## 7. Phase-1 results digest (reports in scratchpad `tasks/report_*.md`)

**New theorems claimed (pending Phase-2 adversarial verification, workflow `wf_1f763b9b-e70`):**
- **T1 (Route C Claim 5).** Every tilted square contains its concentric axis-parallel square of
  side $d/(\cos\theta+\sin\theta)$; applying BKU to the inscribed family:
  $\varepsilon \le T:=\sum d_i(1-\tfrac{1}{\cos\theta_i+\sin\theta_i}) \le \sum d_i\theta_i$.
  First unconditional structural bound on rotated counterexamples ("rotation pays linearly").
- **Theorem C (Route A Claim 10).** If $\Delta:=\sum d_i^2\sin2\theta_i\le 1/4$ then
  $\sum d_i\le k^2+2(k^2+2)\sqrt\Delta$ — BKU recovered at $\Delta=0$; first
  rotation-tolerant exact-constant counting theorem.
- **Tilt-robust ledger (Route A Claims 1–9).** $c=pq-L$ (corner-triangle decomposition);
  $|p-q|\le1$ for every tilt; per-square margin $= (1-d)^2$ (ties at $d=1$, all $\theta$);
  Main Theorem $\sum d_i \le (k^2+M)/2 - \frac12\sum m_i$ under mild size conditions.
- **Pointwise reversal (NUM Claim 2, proved).** For $d\le1$, tilted: $c\le p+q-1$ pointwise
  a.e.; $D\ge0$ at $d=1$; $E[D^+]=2w-1-d^2+(1-w)_+^2$ = surplus exactly at $d=1$.
- **Pythagorean-frame BKU (Route D Claim 2).** All squares at a common Pythagorean angle,
  $c\,|\,k$: $\sum d_i\le k^2$ exactly. Common-orientation averaged bound (any angle):
  $\sum d_i\le N+1/2$ (Route D Claim 5, $J=1$).
- **$f(2)=1$, two complete independent proofs** (Route E corner-standoff; LIT §3 Lemma A =
  analytic Beck–Bleicher), with rigidity: equality forces axis-parallel strips.
- **Structure suite (Route B).** Buried-contact crystallization law; tiling rigidity (full
  proof); Sector Lemma; Window Theorem at walls; min-tilt exclusion
  ($\min$ folded tilt $\ge \arcsin\frac{1}{0.27k-350}$ impossible when $\sum d_i>k^2$).
- **Column tilings (Route C Claim 7).** Exact tilings of $[0,k]^2$ by $k^2+1$ axis-parallel
  squares with all sides $1\pm\Theta(k^{-1/2})$ exist for $k=2b(b-1)$ — kills $L^\infty$
  near-tiling rigidity; only $L^2$ (variance) rigidity can be true.

**Key negative results:** pointwise BKU fails for every $\theta>0$ ($\eta_0=0$); multi-frame
counting provably ties Cauchy–Schwarz; strengthened lemma "max count $\ge\lceil\sum d\rceil$"
FALSE (two-grain counterexample, capture sets disjoint); local per-corner gap-forcing false
(one corner triangle is coverable for free); Dehn/Kenyon dead for near-tilings; square-lattice
packing not uniformly stable.

**Literature verdicts (LIT reports):** no upper bound beyond Cauchy–Schwarz ever published for
rotated case (even $f(3)=3/2$ open); Newman's $f(5)=2$ proof definitively lost ("personal
communication", Erdős–Graham 1975 ref [2]); classical $f(2)=1$ published proof =
Beck–Bleicher, Acta Math. Hungar. 22 (1971/72) 283–303 (regular polygons are tight);
Roth–Vaughan 1978 = the only quantitative tilted-square upper-bound technology in print.

**Numerics:** conjecture survives stress tests at $n=2,5,10,17$ (certified sums $<k$; optimal
tilts $\to0$); coherent tilt penalty $\approx0.43\,kt$ (linear, boundary-only); interface
mismatch cost linear $\approx\sin2\theta$ per unit length; capture lemma: $m\times m$ grain
at tilt $t$ captures fully iff $\sin2t\le\frac{1}{m-1}$; counting destruction $\le0.42\times$
side payment in all adversarial trials.

## 8. Session-2 inline derivations (FCMB structure)

- **Folded-gap form:** $|Av| = 1-|\pi(G)|$; FCMB ⟺ $|\pi(G)|\ge 1-s$. Since $|\pi(G)|\le g$,
  FCMB ⟹ $g+s\ge1$ (= conjecture) *and* demands near-injective folding at criticality —
  FCMB ⟺ conjecture + boundary injectivity. Could be false with conjecture true.
- **Empty-square decomposition:** on $Av$ at least one square is lattice-empty; for AP,
  $d\le1$: exactly one empty, $Av_i \subseteq \bigcap_{j\ne i}\pi(S_j)\setminus\pi(S_i)$;
  verified exact on split-cell ($|Av| = a^2+b^2 = s$, parts $b^2, a^2$).
- **Union bound fails:** $|\{S_i\text{ empty}\}| = 1-d_i^2 \ne (1-d_i)^2$; all content is in
  the "others capture simultaneously" correlation.
- **Mod-1 pigeonhole:** at most $N$ disjoint squares share one position mod $\mathbb{Z}^2$.
- **Second-moment route:** FCMB ⟸ $g+\sum_{v\ne0}|G\cap(G-v)| \le g^2/(1-s)$; tight for
  one-cell gaps (hits Bernoulli).
- **Inscribed-replacement reduction FAILS by the marginal quantity:** replacing tilted $S_1$
  by its concentric inscribed AP square and applying AP-FCMB overshoots by exactly
  $2d(1-1/u)$, $u=\cos t+\sin t$ (computed inline): $(1-d/u)^2-(1-d)^2+d^2(1-1/u^2)
  = 2d(1-1/u) > 0$. One-tilt FCMB must use the tilted square's own capture deficiency
  (folding overlap when $w>1$; corner-triangle structure), not generic monotonicity.
- Session-2 workflow `wf_25ed6619-4c3`: F1 AP-FCMB proof, F2 falsification, F3 one-tilt,
  F4 localization/second-moment, F5 Gap A correlated defects, F6 wildcard transfers.

## 9. Session-2 outcomes (verification wave `wf_1b024c01-ecd` pending)

**FCMB REFUTED** (4 independent constructions): deficient-column family $U_k$: $k+1$
squares of side $k/(k+1)$ stacked in one $1\times k$ strip + $k(k-1)$ units. Valid AP
extremal packing ($\Sigma d = N$, $g+s=1$), $|Av| = k/(k+1) \gg s = 1/(k+1)$. Gap folds
$k$-to-1. At $k=1$ degenerates to split cell (tight) — why $k=1$ proof gave no warning.
Violation is an open condition (tilted/perturbed neighbors still violate). Straddle family
interpolates continuously ($F = -\delta$).

**Salvage / new theorems (pending verification):**
- Restricted FCMB-AP (F1 C4): AP, all $d\le1$, $\Sigma d > N$ ⟹ $|Av| \le s$, via over-full
  column pigeonhole (Lemma A: full-hit set null since $k{+}1$ squares on one line force
  deficit $\ge 1 > \sigma$). Corollary: new ½-page measure proof of BKU (sides ≤ 1).
- Exact decomposition (F1 C3): $|Av| = \alpha_0\Sigma\beta_i + \beta_0\Sigma\alpha_i +
  \Sigma\alpha_i\beta_i$, $\alpha_0\beta_0 = 0$.
- OC-FCMB (F2 C4/F6 C4, trivial algebra, checked): conjecture ⟺
  $|Av| \le s + \sum_{m\ge2}|\{hits \ge m\}|$; equality on the whole deficient-column
  manifold. FCMB dropped the multiplicity credit.
- New extremal manifold (F6 C2): $U_k(a_1..a_{k+1})$, $\Sigma a_j = k$: $g+s=1$ exactly —
  $k$-dimensional equality family with gap up to $k/(k+1)$.
- No-Repair theorem (F4 C4): no $F(g,s)$ measure bound can close the conjecture; ALL
  gap-mass routes structurally dead (enemy has $|Av| \ge 1-g > s$ automatically).
- Comparison Identity (F3 C2): inscribed-replacement is an exact change of coordinates;
  FCMB ⟺ foldloss$(G) \le g+s-1$. Tilt-neutrality (F3 C4): $|\pi(S)| = d^2$ regardless of
  tilt (diam < 1); session-1 "tilt decreases $|Av|$" was 100% shrinkage artifact.
- Tightness-manifold FCMB with tilts (F3 C5): $N-1$ units + 2 arbitrary-orientation squares
  in one cell: $|Av| = a^2+b^2$, margin $2(1-a-b) \ge 0$, via $f(2)=1$ in-cell.
- **Theorem C″ (F5 C4, main new unconditional theorem):** every packing of $N+1$ squares
  (any sizes/orientations): $\sum_i(1-w_i)_+ + \max(U_x,U_y) \ge 1$, where $U_x, U_y$ are
  UNION measures of per-square tall/wide corner-triangle phase sets — coherent families pay
  per distinct phase, not per square. Tight on split-cells.
- Lemma α′ (F5 C1): interface bound generalized to tilted seas ($\tan\varphi_0\le\tau/2$):
  cost $(X/228)\min(\tau-\tan\varphi_0, 1/3)$; gradient smoothing pays $m$-independently
  (F5 C3). α′-edge (C2): localized version, one GAP flagged.
- Theorem W (F5 C5): phase-clustering hypothesis PH(K,λ) ⟹ $\varepsilon \le
  \Sigma(d-1)_+ + \lambda + 2K d_{max}\sin t_0$; kills the coherent whisper phantom for
  $c_0 = 1/400$, $k \ge 20$.
- **Consolidation (F5 C6): Gaps A and B share ONE core — the mod-1 rigidity lemma** (phase
  drift charged to local gap, not variance). That single lemma + W + α′-edge ⟹ first
  unconditional $\varepsilon \le 1/2 - c_0$ in coherent+whisper regimes.
- Winding salvage (F6 C5): total phase drift along a deficient column = 1 exactly (Burgers
  vector); $\cap_j \pi(S_j') = \emptyset$; topology forces an annulus, not area.
- New enemy degree of freedom identified (F5 dead-end 4): one-sided $\ell^1$ deviation
  $\Sigma(d-1)_+$ up to $\sim k\sqrt c$ is permitted by all current bounds.

**The identified remaining enemy:** the *giant gentle grain* ($M\sim T/\theta$ near-unit
squares at coherent tilt $\theta\to0$ carrying tilt mass $T\sim1/2$, boundary gap
$\sim\sqrt{T\theta}\to0$) escapes both T1+gap-charging and $\Delta$-small counting. It IS
covered by the capture lemma (for $\theta\lesssim1/k$), so the pincer plausibly closes —
Phase-2 pushers P1 (quadratic-cost two-orientation theorem) and P2 (level-selection
pigeonhole + staircase interface lemma → first sub-Cauchy–Schwarz bound) are attacking the
two formalizations.
