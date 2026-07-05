# G4 (session 3): the Columnar Kill (Theorem SD), the spatial over-full-chain
# theory, and the one-axis audit

Agent G4, session-3 final assault. Code: `g4_check.py` (this directory; durable copy
`code/session3/g4_check.py` and beside this file). Notation as in ERDOS_106_REPORT.md:
T = [0,k]^2, N = k^2, n = N+1 squares S_i, sides d_i, folded tilts th_i in [0,pi/4],
u1 = cos+sin, sigma_i = u1(th_i)-1, w_i = d_i u1(th_i) (both bbox projections have
length w_i), eps = Sum d_i - N, t = Sum w_i - N, tau = t - eps = Sum d_i sigma_i,
g = N - Sum d_i^2, s = Sum(1-d_i)^2, b0 = Sum(d_i-1)_+, D1 := Sum(1-d_i)_+,
beta = Sum(1 - d_i sec th_i)_+, Gamma = Sum[(1-d_i)_+ - (1-d_i sec th_i)_+] >= 0.
Positive-part identity (Structure Identity on positive parts, [V]):
D1 = 1 - eps + b0 and beta = 1 - eps + b0 - Gamma - (oversize-sec corrections);
precisely beta >= 1  <=>  b0 >= eps + Gamma (fp_P_SQUEEZE S3(i), re-derived below).

Everything below is SPATIAL: no lattice, no shift torus, no phases. The only
imported verified facts: Lemma 0 (chord constancy, [V] as of G1's session-3
verification) and elementary interval combinatorics.

---------------------------------------------------------------------------
## 0. Definitions (new)

For a square S of side d, folded tilt th, bbox x-range [a, a+w] (w = d u1(th)):

- **chord function** ch(u) at offset u in [0,w]: length of the vertical chord.
  Exact ([V], Lemma 0 + machine check A, err 1.4e-14):
  ch(u) = u/(sin th cos th) on [0, d sin th]; ch(u) = d sec th on the **middle
  region** MID(S) := [a + d sin th, a + d cos th]; symmetric down-ramp on the
  right. At th = 0: MID(S) = the whole projection, ch = d. |MID(S)| = w - 2 d sin th
  = d(cos th - sin th).
- **taper zones** TAP(S): the two x-intervals [a, a + d sin th] and
  [a + d cos th, a + w], total length 2 d sin th. (Spatial intervals in [0,k],
  NOT phase arcs mod 1. Their mod-1 projections are exactly C''s bad arcs B^x.)
- **narrow class**: a set Q of squares whose x-projections all lie in one interval
  I_Q of some length X, such that EVERY member satisfies
      w_i - 2 d_i sin th_i > X/2            (equivalently d_i(cos th_i - sin th_i) > X/2).
  (Note: 45-degree squares can never belong to a narrow class — the condition reads
  0 > X/2. This is forced: the diamond chain must be excluded.)
- **columnar packing**: one admitting a partition of all its squares into at most
  k narrow classes (the class intervals may overlap arbitrarily; only membership
  is a partition).
- n(x) := #{i : x in interior of pi_x(S_i)}; **over-full set**
  X_over := {x in (0,k) : n(x) >= k+1}.

---------------------------------------------------------------------------
## 1. LEMMA H (Helly-midline chord lemma). NEW. Fully rigorous, no genericity.

**Lemma H.** Let Q be a narrow class with interval I_Q = [A, A+X]. Then the
vertical line x* = A + X/2 passes through the INTERIOR of MID(S) for every S in Q,
and consequently
    Sum_{i in Q} d_i sec th_i  <=  k .

*Proof.* (i) MID(S_i) is a subinterval of [A, A+X] of length d_i(cos-sin) > X/2.
An interval [u, u+L] inside [A, A+X] with L > X/2 has u <= A+X-L < A+X/2 and
u+L >= A+L > A+X/2: the midpoint is in its open interior. (ii) x* is then in the
interior of pi_x(S_i), so the OPEN chord {x*} x (bot_i(x*), top_i(x*)) lies in the
interior of S_i (convexity), and its length is exactly d_i sec th_i (Lemma 0; at
th=0 the midpoint is interior to MID = the full projection, chord = d). (iii) The
open chords are pairwise disjoint (subsets of pairwise disjoint interiors) open
subintervals of {x*} x (0,k) (containment in T), so their lengths sum to <= k. QED

No perturbation or a.e. argument is needed anywhere: interiors do all the work.
[Machine check C: 363 random narrow groups (tilts up to 0.6, sides 0.45–1.3),
midline in every member's open middle region, 0 failures.]

---------------------------------------------------------------------------
## 2. THEOREM SD (the Columnar Kill). NEW — main deliverable.

**Theorem SD.** Every columnar packing of n squares in [0,k]^2 (ANY n, any sizes,
any orientations; at most k narrow classes on the x-axis) satisfies
    Sum_i d_i  <=  Sum_i d_i sec th_i  <=  k * (#classes)  <=  N .
In particular, for n = N+1: eps <= - Sum_i d_i (sec th_i - 1) <= 0, i.e.
**the Erdős conjecture holds for all columnar packings, with tilts strictly
penalized** (each tilted square costs an extra d(sec th - 1) ~ d th^2/2 of side
budget). By x/y symmetry the same holds with <= k narrow HORIZONTAL classes.

*Proof.* Lemma H per class; sum over <= k classes; d <= d sec th. QED

**Tightness [machine check D].** Exact equality Sum d = N with k classes on:
- the deficient column U_k (k-1 unit columns + one column of k+1 squares of side
  k/(k+1); class sums all exactly k), every k >= 2;
- the whole extremal manifold U_k(a_1..a_{k+1}) (same classes);
- the T12 column tilings (k=4: widths 4/6, 4/3, 1, 1; class sums all 4);
- the k x k grid and split-cell families (trivially).
So SD is exactly tight on EVERY known extremal configuration, and the narrowness
constant X/2 cannot be relaxed to X/2 - delta uniformly: two unit squares side by
side (X = 2, w = 1 = X/2) already defeat the midline (the line can pass between
them), which is why the strict inequality is required.

**Corollary SD-RB (the running bond is dead, top-heavy included).** The
running-bond enemy of assignment G4 — straight x-walls at k+1 clustered values
(k columns of width ~1), rows sliding freely in y, whisper tilts, ANY side profile
including b0 >= eps — is a columnar packing whenever each column width X_j
satisfies X_j < 2 min_{i in col j} d_i(cos th_i - sin th_i) (near-unit whisper:
X_j < 2 - 2 sqrt(2c) - O(t_0), amply true for width-~1 columns). Hence Sum d <= N:
**it cannot be an enemy at all.** No phase analysis, no beta-dichotomy, no
top-heavy escape: the b0-dodge does not exist for columnar packings. This closes
the columnar branch of bridge (III) and the entire audited one-axis loophole
(Section 5) in the columnar case.

**Corollary SD-45.** Any packing in which every square has folded tilt < pi/4 and
which splits into <= k classes of width X_j < 2 min_j d(cos-sin): Sum d <= N.
Diamond-chain-type configurations are automatically outside the hypothesis
(cos-sin = 0 at 45 degrees) — consistent with T2's k^2 + 1/2 barrier at 45
degrees; SD does not contradict it.

**Weak (pigeonhole) form, for use when only ONE narrow class is known.**
**Lemma H+.** If a single narrow class contains >= k+1 squares, then
Sum_{class}(1 - d_i sec th_i) >= (k+1) - k = 1, hence beta >= 1, hence
b0 >= eps + Gamma. (Proof: Lemma H + count.) — This is the SPATIAL, phase-free
version of Lemma A''s over-full line: the hypothesis "full-hit shift + good
phases" is replaced by "k+1 members of one narrow class", and the conclusion
strengthens F1's Lemma A to arbitrary sizes and tilts positionally.

---------------------------------------------------------------------------
## 3. The spatial over-full-chain theory (what non-columnar enemies must contain).

**Theorem OF (over-full lines exist; the spatial pigeonhole).** For any packing
with t = Sum w_i - N > 0 (every enemy: t >= 2 eps by T4-chain):
  (a) Int_{X_over} (n(x) - k) dx >= t   [Fubini: Int_0^k n = Sum w_i = N + t and
      n <= k off X_over];
  (b) |X_over| >= t / (n_max - k), where n_max := ess sup n(x) satisfies, for
      packings with all sides >= 1 - delta (enemy profile delta = sqrt(2c)),
      n_max <= 2k(1+delta)u1_max/(1-delta)^2 <= 2.2 k + O(delta k)
      [all squares meeting a line lie in a strip of width 2 w_max and height k;
      disjoint areas >= (1-delta)^2]. So |X_over| >= t/(1.2k) >= eps/(1.2k)-ish.
  (c) At every x in X_over avoiding the finitely many bbox endpoints: the clique
      L(x) = {i : x in int pi_x(S_i)} has >= k+1 members with pairwise disjoint
      open vertical chords: Sum_{L(x)} ch_i(x) <= k, hence
          Sum_{i in L(x)} (1 - ch_i(x))  >=  n(x) - k  >=  1 .
      **This is the assignment's conjectured theorem** ("every packing with
      eps > 0 contains k+1 pairwise-x-overlapping squares") — proved, in the
      stronger common-point (Helly) form, for any sizes/orientations, with the
      chord-deficit ledger attached. [Machine check F: perturbed deficient column
      with Sum w - N = 0.171: |X_over| = 0.79, Int(n-k)_+ = 0.79 >= t. PASS]

**Theorem CD (chain-deficit dichotomy).** At such an x, split L(x) into
middle-crossers (x in MID) and taper-crossers T(x) (x in TAP). Middle-crossers
have ch = d sec th; taper-crossers give (1 - ch)_+ <= 1. Hence
    beta  >=  Sum_{L(x) \ T(x)} (1 - d_i sec th_i)  >=  n(x) - k - |T(x)| ,
so:  **if beta < 1 then EVERY over-full line is taper-crossed** (|T(x)| >= 1),
i.e. X_over is covered by the spatial taper zones of the squares in its own
cliques; and pointwise |T(x)| >= n(x) - k - beta.

**Theorem CH (few chains / disjoint cliques are expensive).**
Let x_1 < ... < x_m in X_over with cliques L(x_a) pairwise disjoint as square
sets (guaranteed if consecutive gaps exceed w_max), and suppose every clique is
crossed middles-only (T(x_a) = 0, e.g. the AP case where TAP is empty). Then
    beta >= m ,   equivalently   b0 >= eps + Gamma + (m - 1) .
*Proof.* Sum over a of Sum_{L(x_a)}(1 - d sec th) >= m; disjointness lets each
square pay once; (1 - d sec th) <= (1 - d sec th)_+. The b0 form: by the
positive-part Structure Identity, beta = Sum(1-d_i)_+ - Gamma = 1 - eps + b0 - Gamma. QED
Consequences:
  - **AP unconditional:** any AP packing of N+1 squares with eps > 0 has
    D1 >= 1, i.e. b0 >= eps (m = 1 suffices; TAP empty). A one-paragraph spatial
    proof of "AP enemies are top-heavy", independent of BKU and of all lattice
    machinery. (BKU of course kills AP outright; the value is that THIS mechanism
    survives tilts as Theorem CD and needs no shift selection.)
  - **AP localization:** if b0 < 1 + eps then m <= 1: no two over-full abscissas
    at distance > max d_i, so diam(X_over) <= max d_i — the over-full structure of
    a near-AP low-b0 packing is confined to ONE column of width <= ~1, the
    positional deficient column. (The deficient column itself: X_over = the strip
    column at t=0 boundary... at U_k, t = 0 and X_over is empty EXCEPT that
    n = k+1 exactly on the strip x-interval when counting closed projections;
    U_k sits exactly on the boundary of OF, as it does on every other boundary.)

---------------------------------------------------------------------------
## 4. Mass neutrality (why the chain theory cannot kill by measure alone). PROVED.

**Fact R (exact chord-deficit mass).** R_i := Int_{pi_x(S_i)} (1 - ch_i)_+ dx =
    w_i - d_i^2                    if d_i <= cos th_i ,
    sin th_i cos th_i              if d_i >= cos th_i .
[Elementary integration of the ramp; machine check B, err 6e-10.] Since
R_i >= w_i - d_i^2 always, integrating Theorem OF(c) gives
Sum w - N <= Sum R_i, which is IMPLIED BY the area bound Sum d^2 <= N: vacuous.
And the taper mass Sum |TAP| = 2 Sum d_i sin th_i >= 2 Sum d_i sigma_i = 2 tau
>= t + eps > t (orchestrator's inequality sin th >= sigma, plus T4): the enemy
ALWAYS has enough raw taper mass to cover X_over as demanded by Theorem CD.
**Conclusion (the honest no-go):** the spatial chain route, in any purely
mass-integrated form, is exactly first-moment-neutral, in perfect agreement with
the report's criticality identity and with the orchestrator's strategic fact.
All content of Sections 2–3 is therefore in the COMBINATORIAL statements
(cardinality of classes, disjointness of cliques, location of tapers), never in
integrated measure. Any future strengthening must couple the taper LOCATIONS
(bbox corners physically sitting on over-full stacks) to gap or phase costs.

Quantitative residue (for the record): if X_over is confined to one column
(few-chains case), only squares within w_max of it can service the coverage, at
most ~3.3k of them, so beta < 1 forces sin t_0 >= eps/(9 k^2)-order — the same
order as T4's whisper floor, no better. The chain route REPRODUCES the T4 scale
from pure position; it does not beat it. (GAP: beating it needs the wedge–gap
coupling, Section 6.)

---------------------------------------------------------------------------
## 5. The one-axis sufficiency audit (assignment part 1). CONFIRMED, with table.

Requirement imposed on the packing by each verified/[P] tool, and whether ONE
scattered axis satisfies it (enemy: x-phases clustered in k+1 values, y-phases
scattered, whisper tilts, U_y ~ min(1, 2 Sum d sin th) ~ 1, U_x ~ lambda small):

| Tool | Requirement on enemy | one big axis enough? |
|---|---|---|
| C'' | Sum(1-w)_+ + max(U_x,U_y) >= 1 | YES: U_y alone |
| S2 | Av-bound RHS contains U_x + U_y + V_x + V_y | YES: RHS >= U_y ~ 1, vacuous |
| S3(ii) | U_x+U_y+V_x+V_y >= 2 eps + margins | YES: U_y ~ 1 >= 2 eps |
| Thm W | PH(K,lambda) on BOTH axes needed to bound both U's | inapplicable (y scattered) — and C'' only needs max |
| kappa-coupling | 2 eps <= |Av| + U_x + U_y - Sum m | YES: satisfied via U_y |
| alpha'-edge | orientation mismatch at interfaces | whisper tilts: cost O(k t_0/520): within budget |
| Lemma A''/S2 route | beta < 1 allows full hits only at bad phases | x-axis clustered: consistent |

So the audit stands exactly as the assignment predicted: **before this session,
an x-clustered / y-scattered running bond complied with every requirement in the
arsenal.** Theorem SD now adds the requirement "not columnar on EITHER axis"
(Sum d <= N otherwise), which the running bond violates structurally, phases
never entering. The surviving enemy must be non-columnar on both axes
simultaneously (x-version and y-version of SD).

---------------------------------------------------------------------------
## 6. What non-columnarity forces (the enemy's new profile) + component dichotomy.

Let r = number of connected components of Union_i pi_x(S_i) (disjoint intervals,
spans X_m, Sum X_m <= k; every component nonempty so X_m >= max member w >= w_min).
Every component of span < 2 min_{members} d(cos-sin) is automatically ONE narrow
class (two intervals of length > X/2 inside a length-X interval intersect; in fact
the narrowness condition directly). Hence for a non-columnar packing, either

  **(a) r >= k+1**, i.e. at least k+1 disjoint occupied columns. Then every
  member of component m has d_i <= w_i <= X_m, so picking one member per
  component: Sum_m (1 - X_m)_+ >= Sum_m (1 - X_m) >= r - k >= 1, and
      s >= Sum_m (1 - X_m)_+^2 >= (r-k)^2 / r >= 1/r >= w_min / k .
  For the sub-Cauchy–Schwarz enemy (s <= 2c + O(1/k^2)): **dead whenever
  k < w_min/(2c) ~ (1 - sqrt(2c))/(2c)** (c = 1/400: all k <= 185). A sharper
  count (squeezed components waste width, singleton-squeezing capped by the
  member budget) pushes this to k = O((2c)^{-3/2}) ~ 2800, not written out
  rigorously here (GAP-flag: the s >= 1/r line is fully proved; the (2c)^{-3/2}
  refinement is sketched only). For the FULL conjecture (budget s < 1 - 2 eps)
  case (a) is NOT dead: it is the transposed deficient-manifold shape
  (k+1 squeezed columns, s ~ 1/(k+1)) — the honest boundary.  OR

  **(b) some x-component is WIDE**: span >= 2 W_0, W_0 := min member d(cos-sin)
  (~ 1 - sqrt(2c) - t_0 for the enemy) — genuine horizontal interlocking: a
  connected chain of x-overlapping squares spanning >= ~2, containing two squares
  side-by-side; and the same dichotomy on the y-axis. Together with Theorem CD:
  inside the wide component, the over-full lines (Theorem OF: they carry
  Int(n-k) >= t_m over components with surplus, Sum_m surplus >= t) are each
  taper-crossed if beta < 1: **at every over-full abscissa some square's extreme
  bbox corner lies within d sin th of the line — a "wedge" square whose corner is
  physically inserted into a (k+1)-deep vertical stack.** The non-columnar,
  beta < 1 enemy is therefore a wedged running bond: coherent-ish stacks + corner
  wedges at every over-full abscissa on both axes.

**Why the crude covering pigeonhole cannot finish (recorded dead end):** greedy
partition of components into windows of stride 2W_0 - w_max gives
chi_narrow <= r + k/(2W_0 - w_max) ~ r + k(1 + 3 sqrt(2c)); the excess over k is
O(sqrt(c) k), which dwarfs the +1 integrality gain for k >> 1/sqrt(c). The +1
must be caught by measure (Theorem OF) or by exact counting (Lemma H), never by
coverings with per-window loss.

---------------------------------------------------------------------------
## 7. Winding note (assignment part 2, secondary). 

Along one over-full chain (k+1 stacked squares, heights summing <= k), the total
y-drift equals the chain deficit >= 1: the k+1 bbox y-phases sweep >= 1 full unit,
so they equidistribute-ish across the circle. But the chain contributes only its
own 2(k+1) arcs of length d sin th each to U_y: mass ~ 2(k+1) t_0 ~ 2t_0 k — for
whisper t_0 ~ 1/k^2 this is O(1/k): the chain ALONE cannot certify C''
compliance; scattered mass must come from the bulk. Confirms F6-C5's assessment;
nothing further extracted. (Consistent with the one-axis audit: the winding
spreads the chain's OWN phases, not the gap, and not the bulk's.)

---------------------------------------------------------------------------
## 8. Honest interface to the coherence trichotomy (orchestrator's (I)/(II)/(III)).

- (III) near-AP: CLOSED in the columnar case by SD (no b0 dodge). Non-columnar
  near-AP: Theorem CH forces b0 >= eps + (m-1) per extra disjoint over-full
  column and confines X_over to one column when b0 < 1 + eps. Residue: the
  single-wedged-column near-AP enemy.
- (II) coherent: coherent rigid near-grids ARE columnar (walls straight up to
  drift k t_0 + roughness; columnar as long as total wall wander < 2W_0 - 1 ~
  1 - O(sqrt c)): SD kills them OUTRIGHT (stronger than Theorem W: no phase-cover
  hypothesis, no b0 hypothesis, no k >= 20, conclusion eps <= 0 not eps <= budget).
  The (II)->(cluster) bridge is thus REPLACED by the cheaper "(II) -> columnar"
  bridge: coherence needs only to imply that each square stays within a fixed
  width-(<2W_0) vertical class — wall wander < 1 - O(sqrt c), an O(1) demand
  instead of a mod-1 clustering demand. GAP (quantified): derive wander < 1-O(sqrt c)
  from coherence + G+V <= 2c. This is strictly weaker than the old mod-1
  Rigidity Lemma (which needed clustering to lambda = O(sqrt c + k t_0)).
- (I) incoherent: the wedge structure (Section 6) is the new purchase: every
  over-full abscissa hosts a corner wedged into a stack; a wedge whose
  orientation mismatches its stack by alpha pays ~ min(tan alpha, 1/3)/520 of
  gap at its exposed edges (alpha'-edge, hypotheses to be verified per wedge);
  budget 2c kills wedges with alpha >~ 1000 c. Residue: whisper wedges — which
  carry taper width d sin th ~ t_0 each, so covering |X_over| >= eps/(1.2k)
  needs >= eps/(1.2 k t_0) wedges; with t_0 ~ eps/k^2-scale (T4 floor) that is
  >= k/1.2 wedges: **a non-columnar whisper enemy needs Omega(k) distinct wedge
  corners embedded in over-full stacks.** Each wedge is a local running-bond
  fault; whether each forces Omega(1/k)-gap or Omega(1/k)-phase-scatter on the
  x-axis (which Theorem W-side tools could then eat) is the sharpest new
  question: **the Wedge Ledger** (see BEST NEXT STEP).

---------------------------------------------------------------------------
## 9. Adversarial self-attack (what I tried to break).

- Lemma H with X/2 replaced by X/2 - delta: FALSE (two abreast). Strictness
  needed and present.
- SD with classes replaced by "components": components can number k+1 (case (a)):
  SD correctly does NOT apply; the s >= (r-k)^2/r bound covers it. No leak found.
- SD at 45 degrees: hypothesis unsatisfiable (cos-sin = 0): correctly silent;
  T2's +1/2 slack at 45 degrees is NOT contradicted.
- Oversize squares (d > 1, d sec th > 1): Lemma H handles them (chord d sec th
  counts on the LHS of Sum <= k); SD's conclusion only strengthens. Checked.
- Squares of wildly different sizes in one class: narrowness demands
  d_i(cos-sin) > X/2 for ALL members, so a tiny square voids its class — correct
  (a tiny square between two stacks defeats the midline unless it still spans
  the midline region; the condition enforces exactly that).
- Machine search (check E): 4000 random 2-narrow-class 5-square configs in
  [0,2]^2, SAT-verified disjoint: best Sum d = 3.333 <= 4. No violation.
- Theorem CH disjointness hypothesis: cliques at |x - x'| <= w_max can share
  squares; the m-count only uses pairwise-disjoint witnesses. Stated so.
- Fubini step of OF(a): n(x) is measurable (finite union of intervals), Int n =
  Sum w exact. No genericity issue: X_over defined via open projections;
  endpoints are a null set.

---------------------------------------------------------------------------
## CLAIMS (status summary)

1. Lemma H [PROVED, machine-checked; no genericity caveats].
2. Theorem SD, Corollaries SD-RB, SD-45, Lemma H+ [PROVED; tight on the entire
   extremal catalogue; kills the running bond outright including top-heavy].
3. Theorem OF (spatial over-full lines) [PROVED; the assignment's conjectured
   chain theorem, in Helly form].
4. Theorem CD (taper dichotomy: beta < 1 => every over-full line is wedged)
   [PROVED].
5. Theorem CH (m disjoint middle-crossed cliques => b0 >= eps + Gamma + m - 1;
   AP: b0 >= eps unconditionally; X_over localization) [PROVED].
6. Fact R + mass-neutrality no-go [PROVED].
7. Component dichotomy: non-columnar => (r >= k+1 => s >= (r-k)^2/r >= w_min/k,
   killing sub-CS enemies for k <~ 1/(2c)) OR (wide interlocked component on
   both axes + wedge structure) [PROVED except the (2c)^{-3/2} refinement,
   GAP-flagged].
8. One-axis audit [CONFIRMED, table in §5].

## CHECKS
g4_check.py: A chord formula (300 squares x 40 abscissas, err 1.4e-14); B Fact R
integrals (400 squares, err 6e-10); C Lemma H midline (363 random narrow groups,
0 fail); D SD equality on U_k (k=2,3,4) and T12 (k=4), exact; E adversarial
columnar search k=2 (4000 trials, SAT-disjoint, max Sum d 3.333 < 4); F over-full
existence on perturbed column (|X_over| = 0.79 > 0, Int(n-k)_+ >= t). All PASS.

## DEAD ENDS (this assignment)
- Any integrated/measure form of the chain argument (Fact R: exactly neutral).
- Crude window-covering pigeonhole for chi_narrow (loses O(sqrt(c) k) >> 1).
- Taper-mass covering exclusion (2 Sum d sin th >= t always: mass never obstructs;
  only wedge LOCATIONS can).
- Extracting more than the swept-annulus from chain winding (§7; confirms F6).
- Per-component conjecture "Sum_comp d <= k X_m" as a lemma: is the full
  conjecture in disguise for X_m = k; no independent handle found.

## BEST NEXT STEP (the Wedge Ledger)
Non-columnar beta < 1 enemies need Omega(k) wedge corners embedded in over-full
stacks (§8(I)). Prove: each wedge (corner of S* inserted between two stack
members at mismatch alpha) EITHER pays gap >= min(tan alpha,1/3)/520 locally
(alpha'-edge, hypotheses now local and checkable) OR (alpha < whisper) displaces
the stack's x-phases by >= d sin th at that abscissa — i.e. wedges at whisper
mismatch force the x-phases of the two abutting stack members apart by the taper
width. Summing over the Omega(k) wedges: either gap > 2c (dead) or the x-axis
phase spread U_x >= Omega(k t_0) ~ Omega(eps/k)... then feed U_x into the
kappa-coupling 2 eps <= |Av| + U_x + U_y - Sum m_i TOGETHER with S2's capture
bound on the y-axis. The missing quantitative piece is a single local lemma
("wedge displacement lemma"): two near-unit stack members separated by a wedged
corner of taper width delta have their MID intervals' midpoints separated by
>= delta - O(gap_local). That lemma is finite, checkable, and would convert the
Omega(k) wedge count into the first phase-scatter lower bound derived from
POSITION, closing the loop that the mod-1 Rigidity Lemma left open.
