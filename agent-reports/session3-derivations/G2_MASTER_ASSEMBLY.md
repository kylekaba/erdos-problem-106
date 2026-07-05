# G2 — THE CONDITIONAL MASTER ASSEMBLY

Session 3, agent G2. Complete conditional proof skeleton of
`f(k^2+1) <= k + (1/2 - c0)/k`, modulo a minimal explicitly-stated set of unproved
lemmas; plus the strongest fully-unconditional Structure-of-Counterexamples theorem.

Notation as in ERDOS_106_REPORT.md throughout: T = [0,k]^2, N = k^2, n = N+1 squares
S_1..S_{N+1}, sides d_i, folded tilts th_i in [0,pi/4], u1(th) = cos th + sin th,
sigma_i = u1(th_i) - 1, w_i = d_i u1(th_i) (common width of both axis projections),
eps = Sum d_i - N, t = Sum w_i - N, tau = Sum d_i sigma_i = t - eps,
g = N - Sum d_i^2 (gap area), s = Sum (1-d_i)^2, b0 = Sum (d_i-1)_+,
beta = Sum (1 - d_i sec th_i)_+, Gamma = Sum [(1-d_i)_+ - (1-d_i sec th_i)_+] >= 0.
Shift torus p = (x,y) in [0,1)^2; p_i(x), q_i(y) = lattice-line counts; c_i = captures;
C = Sum c_i <= N a.e. (budget [V]); Av = {C = N}; hits = N - C.
B_i^x, B_i^y = the corner-triangle phase arcs (each of length d_i sin th_i, at the bbox
extremes); U_x = |Union_i B_i^x|, U_y likewise; V_x = |Union_i {x : p_i(x) >= 2}|
(for w_i in [1,2) an arc of length w_i - 1 at the bbox-min phase), V_y likewise.
"Enemy(c)": a packing of N+1 squares in T with eps > 1/2 - c.

Machine checks: `g2_checks.py` in this directory — 14 check groups, ALL PASS
(identities to 1.8e-15; constants scanned; c0 arithmetic margins printed).

**Status upgrade (same session):** the sibling verifier G1 (G1_VERIFICATION.md, this
directory) has independently CONFIRMED and promoted to [V]: Lemma 0, Lemma A'',
Theorem S2 (including the idle/multiplicity ledger), Corollaries S1/S3/S4, Lemma K,
and Theorem K (unconditional). My Part-I re-derivations of Lemma 0 / A'' / the S2
ledger are therefore a THIRD independent pass; everything below marked
"[P; re-derived here]" should be read as **[V]** as of this session. Consequently
Theorem S3+ and Theorem U item 16 rest on [V] pieces only; the only remaining [P]
dependencies anywhere in this file are T6's MPI chain (used solely in Theorem U
items 13/15, never in the Conditional Master Theorem).

---

## PART I. THE PROVED BACKBONE (with full proofs or [V]/[P] citations)

### Prop 1.1 (Structure identity and the enemy profile). [V]
For any packing of N+1 squares (any sizes/orientations):
`g + s = 1 - 2 eps` exactly. Hence Enemy(c) satisfies:
g < 2c, s < 2c, every d_i in (1 - sqrt(2c), 1 + sqrt(2c)), Sum d_i^2 > N - 2c,
and total uncovered area G = g < 2c.
*Proof.* g + s = N - Sum d^2 + (N+1) - 2 Sum d + Sum d^2 = 2N + 1 - 2 Sum d = 1 - 2 eps.
Each consequence is immediate ((1-d_i)^2 <= s). [Machine: I5.] QED

### Prop 1.2 (Mandatory tilt mass; the T4 chain). [V]
Any packing with eps > 0 has
`eps <= Sum d_i sigma_i / u1(th_i) <= tau = Sum d_i sigma_i <= Sum d_i sin th_i <= Sum d_i th_i`,
and consequently `t = eps + tau >= 2 eps`.
*Proof.* First inequality is T4 [V] (inscribed-square + BKU g-theorem). The chain uses
u1 >= 1, sigma <= sin (equivalent to cos <= 1), sin <= id. [Machine: I4a/b, I6b.] QED
*Enemy(c) reading:* tilt mass in every metric >= 1/2 - c; the packing fakes a full unit
of aggregate projection width by tilt (t > 1 - 2c).

### Prop 1.3 (No-Repair / Markov floor). [V]
|Av| >= 1 - g. *Proof.* hits = N - C is a nonneg integer a.e. (budget), E[hits] =
N - Sum E[c_i] = N - Sum d_i^2 = g (E[c_i] = area, any orientation), so
Pr[hits >= 1] <= g. QED
*Enemy(c) reading:* full-capture shifts occupy measure > 1 - 2c: near-certainty.

### Prop 1.4 (Lemma 0 — chord constancy). [P: proof elementary, machine 1.6e-15; re-derived here]
A square of side d, folded tilt th in (0, pi/4], bbox x-range [0,w]: its vertical chord
is <= d sec th everywhere and equals d sec th identically on the middle region
[d sin th, d cos th]. Horizontal chords likewise (90-degree symmetry). Hence if
x mod 1 is outside Union_i B_i^x, every lattice line meets every square it touches in
that square's middle region, with chord exactly d_i sec th_i.
*Independent re-derivation (this session):* vertices A=(d sin,0), B=(w, d sin),
C=(d cos, w), D=(0, d cos); on [d sin, d cos] bottom envelope = AB (slope tan th), top
envelope = DC (same slope); vertical difference = d cos + d sin tan th = d sec th. QED

### Prop 1.5 (Lemma A''-mechanism — over-full lines; saturation form). [P; re-derived here]
Call an x-phase *saturating* if x mod 1 is outside Union_i B_i^x (good) and p_i(x) >= 1
for all i. For a.e. saturating x there is a lattice line x + m carrying a set L of at
least k+1 squares whose chords on that line are pairwise interior-disjoint segments of
[0,k] of length exactly d_j sec th_j; consequently
`Sum_{j in L} d_j sec th_j <= k` and `Sum_{j in L} (1 - d_j sec th_j) >= 1`, hence
`beta >= 1`.
*Independent re-derivation (this session):* generic x in (0,1): every line meeting a
square has index m in {0..k-1} (containment); N+1 squares each meeting >= 1 line gives
>= k^2+1 incidences on k lines; pigeonhole: some line meets ceil((N+1)/k) = k+1 squares.
Goodness of x pins each meeting to the middle region (Prop 1.4), chord = d_j sec th_j,
open chord inside the square's interior; packing disjointness makes the chords
interior-disjoint inside [0,k]; sum <= k. The deficit sum over k+1 terms is
>= (k+1) - k = 1; positive parts dominate: beta >= 1. QED
*(Lemma A'' as stated by SQUEEZE is the contrapositive: beta < 1 => no saturating
phases on either axis. At th = 0 it is F1's Lemma A [V] with the weaker positive-part
hypothesis.)*

### Prop 1.6 (Theorem S2 — capture-measure bound; saturation-free form). [P; assembly independently re-derived here — this is the previously-unverified ledger step]
If neither axis has a positive-measure set of saturating phases, then
`|Av| <= Sum_i (1 - w_i)_+^2 + U_x + U_y + V_x + V_y`.
In particular this holds whenever beta < 1 (Prop 1.5).
*Re-derivation of the ledger (the step flagged as awaiting verification):*
Let E = (good x) x (good y); |E^c| <= U_x + U_y. On E, a.e.: no lattice point lies in
any corner triangle (Fact 4.0, verified [V] in sv_V2 for d up to 2.8), so
c_i = p_i q_i for all i (bbox capture = p_i q_i for the axis-aligned w x w bbox; c =
bbox capture minus triangle points). On Av cap E: Sum p_i q_i = N over N+1 squares.
Idle set I = {i : c_i = 0}; every idle has p_i = 0 or q_i = 0; p_i = 0 forces
floor(w_i) = 0 i.e. w_i < 1, and then q_i <= 1 (equal projection widths). Ledger:
Sum_{i not in I} (c_i - 1) = N - (N+1-|I|) = |I| - 1 =: mu >= 0.
By non-saturation, a.e. (x,y) in E has M_X(x) = {i : p_i(x) = 0} nonempty and
M_Y(y) nonempty; I = M_X cup M_Y (on Av cap E: c_i=0 iff p_i q_i = 0).
- Case |I| = 1: I = {i} = M_X = M_Y, so p_i = 0 AND q_i = 0: the event is contained in
  {p_i = 0} x {q_i = 0}, measure (1-w_i)_+^2; events disjoint across i (distinct unique
  idle) so their total measure <= Sum_i (1-w_i)_+^2.
- Case |I| >= 2: mu >= 1: some square has p_i q_i >= 2, hence p_i >= 2 or q_i >= 2:
  (x,y) in the V_x-union x [0,1) or [0,1) x V_y-union; measure <= V_x + V_y.
Total: |Av| <= |E^c| + Sum (1-w)_+^2 + V_x + V_y. QED
*(Verdict on the flagged step: CORRECT. The only inputs are Fact 4.0 [V], equal
projection widths [V], the budget [V], and Prop 1.5.)*

### Prop 1.7 (THE LOAD-BEARING COMPUTATION — exact requirement for a non-saturating enemy).
This is the exact grind the assignment demanded. Let a packing have eps > 0 and no
saturating axis (e.g. b0 < eps, see Prop 1.8). Then
`U_x + U_y + V_x + V_y >= 2 eps + Sum_{w_i<1} m_i + Sum_{w_i>=1} (1-d_i)^2`,
with m_i = d_i sigma_i (2 - d_i - w_i) >= 0 (the exact T6 margins, but NO T6 input —
pure algebra here).
*Proof (every step exact).* Chain:
(1) 1 - g <= |Av|                        [Prop 1.3]
(2) |Av| <= Sum_short (1-w_i)^2 + U_x+U_y+V_x+V_y      [Prop 1.6]
(3) 1 - g = s + 2 eps                    [Prop 1.1 rearranged]
(4) The bracket [s - Sum_short (1-w)^2]: by the exact identity
    `(1-w)^2 = (1-d)^2 - d sigma (2-d-w)` (valid for ALL d, th; machine I1) summed over
    shorts, and s = Sum_short (1-d)^2 + Sum_long (1-d)^2:
    `s - Sum_short (1-w)^2 = Sum_short m_i + Sum_long (1-d_i)^2 >= 0`. [machine I2]
Assemble: s + 2 eps <= Sum_short(1-d)^2 - Sum_short m_i + U+V, i.e.
U+V >= 2 eps + Sum_short m_i + Sum_long (1-d_i)^2. QED
*Answer to the assignment's bracket question:* s - Sum(1-w)_+^2 is EXACTLY
Sum_short m_i + Sum_long (1-d_i)^2 — nonnegative, with the long squares contributing
their full squared deviation and the shorts their T6 margin. Nothing is lost: the
b0-light enemy must beat 2 eps PLUS these margins with union mass alone.

### Prop 1.8 (b0-light => non-saturating). Pure algebra.
`beta = 1 - eps + b0 - Gamma` (machine I3; from Sum(1-d)_+ = (N+1) - Sum d + b0 =
1 - eps + b0 and beta = Sum(1-d)_+ - Gamma). Since Gamma >= 0 (sec th >= 1, positive
part monotone; machine I3b/I4d): `b0 < eps  =>  beta < 1  =>  no saturating axis`
(Prop 1.5). The assignment's hoped chain "b0 < eps => beta < 1" is CONFIRMED exactly,
including the correction term: beta < 1 iff b0 < eps + Gamma.

### THEOREM S3+ (the vernier dichotomy — new assembly, this session).
**Every packing of N+1 squares in [0,k]^2 with eps > 0 satisfies at least one of:**
**(I) [vernier structure] some axis has a positive-measure set of saturating phases;
for a.e. such phase there is an over-full lattice line: k+1 squares with pairwise
interior-disjoint chords, each exactly d_j sec th_j, total <= k, line chord-deficit
Sum_L (1 - d_j sec th_j) >= 1. In particular beta >= 1 and b0 >= eps + Gamma.**
**(II) [union requirement] U_x + U_y + V_x + V_y >= 2 eps + Sum_{w<1} m_i +
Sum_{w>=1} (1-d_i)^2.**
*Proof.* If some axis saturates on positive measure: Prop 1.5 gives (I) (and
beta >= 1 gives b0 - eps - Gamma = beta - 1 >= 0 via Prop 1.8's identity). Else
Prop 1.6 applies and Prop 1.7 gives (II). QED
*Status: assembled entirely from Prop 1.1/1.3 [V], Fact 4.0 [V], and Prop 1.4/1.5/1.6
— now [V] via G1's promotion plus the third-pass re-derivations above. S3+ is
therefore a fully [V]-based theorem. It strictly upgrades SQUEEZE's S3: branch (i) is
promoted from the arithmetic condition b0 >= eps + Gamma to the geometric vernier
structure (which implies it).*

### Cor 1.9 (small-k saturation kill — new, unconditional).
An Enemy(c) in branch (I) has `s >= 1/(k+1)`; hence **every Enemy(c) with
k <= 1/(2c) - 1 is in branch (II)**.
*Proof.* The vernier line's k+1 squares satisfy Sum_L (1-d_j) >= Sum_L (1-d_j sec th_j)
>= 1 (pointwise 1-d >= 1-d sec th). Cauchy-Schwarz: 1 <= (Sum_L (1-d_j))^2 <=
(k+1) Sum_L (1-d_j)^2 <= (k+1) s. [machine I7] Enemy: s < 2c. QED
*(At c = 1e-5 this covers every k <= 49,999.)*

### Prop 1.10 (mass never obstructs — the orchestrator's strategic fact, formalized).
The raw (pre-union) arc mass feeding (II) is
R := 2 Sum 2 d_i sin th_i + 2 Sum (w_i - 1)_+ >= 4 Sum d_i sigma_i >= 4 eps
for any packing with eps > 0 (sin th >= sigma pointwise, machine I4a; T4 chain 1.2).
Since the requirement in (II) is 2 eps + margins (margins <= Sum_short 2 d sigma + s
<= 2 tau + s < R/2 + s), **branch (II) can never fail for lack of mass — only the
collapse of unions (phase clustering / arc overlap) can violate it.** Every kill of
branch (II) must therefore be a kill of phase scattering, i.e. a rigidity statement.

### Inventory of the remaining verified weapons and their binding conditions.
| Weapon | Status | Binds when | Gives |
|---|---|---|---|
| C'' | [V] | always | Sum(1-w)_+ + max(U_x,U_y) >= 1; hence max(U_x,U_y) >= eps - b0 |
| Theorem W | [V] | all th_i <= t0, phases PH(K,lambda) | eps <= b0 + lambda + 2K d_max sin t0 |
| alpha'-edge | [V, 1/240] | exposed edge, env. tilts <= phi0 <= (tan alpha)/2 | local gap >= (1/240) min(tan alpha - tan phi0, 1/3) |
| alpha' / gradient | [V, 1/60 and 1/120] | tilted line over near-unit sea / texture | gap >= (X/60) min(tau - tan phi0, 1/3); (X/120) min(Theta,1/3) |
| Wall lemma | [V] | squares serving a wall | Sum(y_i|A_i| + sin2th/2 |A_i|^2) + k|A_0| <= g |
| Window / min-tilt | [V] | all tilts >= t, k >= 1274 | G >= 0.9 sin t (0.305k - 387.2) |
| T2 / T3 | [V] | common orientation / Pythagorean+c|k | eps <= 1/2 / eps <= 0 |
| T5 | [V] | Delta = Sum d^2 sin 2th < 1 | eps <= 2(N+1) sqrt(Delta) |
| Crystallization/Sector | [V] | buried contacts | mismatch cannot be buried |
| Theorem K | [P] | t <= 1 | kappa >= (1-t)^2 (vacuous on enemies: t >= 2eps) |
| T6 | [P] | always | 2 eps <= 1 - Sum m_i - kappa |
| kappa-coupling | [P] | always | 2 eps <= |Av| + U_x + U_y - Sum m_i |
| restricted FCMB-AP | [V] | AP, d<=1, Sum d > N | |Av| <= s (BKU reproof) |
| S4 | [P] | AP, b0 < eps | no AP enemy at all (BKU-free) |
| BKU | published | AP | eps <= 0 |
| Singh | published | — | k*eps(k) non-decreasing in k |

---

## PART II. THE COHERENCE TRICHOTOMY — FORMAL DEFINITIONS

Fix the whisper threshold `t0 := 1/(4k^2)` and the steep threshold `2*t0`.

**D1 (classes).** WHISPER squares: th_i <= 2 t0. STEEP squares: th_i > 2 t0.
T4 needs Sum d th >= eps > 1/2 - c; whisper squares alone can supply at most
(N+eps) * 2 t0 = 1/2 + O(1/k^2), i.e. they can just barely carry T4 at this
normalization. With the sharper split t0 = 1/(8 k^2), whisper mass <= 1/4 < eps and
steep squares become mandatory, carrying >= eps - 1/4 of the tilt mass (machine I10).
Either normalization works below; what the trichotomy actually splits on is which
class carries the UNION mass of S3+(II), not which carries the T4 mass.

**D2 (interfaces and the mismatch functional).** For squares i != j let the
eta-interface (eta := 1/4, alpha'-edge's strip height) be
L_ij := length of {p in bd(S_i) : dist(p, S_j) <= eta}, and the folded mismatch
alpha_ij := folded angle difference of th_i, th_j (in [0, pi/4]). The container walls
participate as four fictitious squares of tilt 0. The **mismatch functional** is
`I := Sum_{pairs, incl. walls} L_ij * min(tan alpha_ij, 1/3)`.

**D3 (phase scatter).** Per axis, the arc system A_x := {B_i^x arcs} cup {V-arcs of
long squares}: 2(N+1) + #longs arcs, anchored at bbox-extreme phases, lengths
d_i sin th_i resp. (w_i - 1). The scatter of the enemy is the union measure
U_x + V_x (and per D1, splits into whisper-anchored and steep-anchored parts).

**D4 (grains).** A grain is a connected component of the graph on squares with edges
{L_ij > 0 and alpha_ij <= 2 t0}: maximal eta-connected orientation-coherent clusters.
Grain boundary = pairs (i,j) in different grains with L_ij > 0, plus wall interfaces.

**The trichotomy (formal).** Every Enemy(c) satisfying S3+(II) obtains its union mass
2 eps > 1 - 2c from the arc system; decompose U+V = M_steep + M_whisper (mass of the
union restricted to arcs of steep resp. whisper squares; subadditive). Then at least
one of:
- **Case I (steep-carried scatter):** M_steep >= (1 - 2c)/2. The steep arcs are long
  (length ~ d sin th each); their carriers sit at pairwise-distinct phases (else no
  union gain).
- **Case II/III (whisper-carried scatter):** M_whisper >= (1 - 2c)/2, from >= about
  (1-2c) / (2 * 2 d_max sin(2 t0)) ~ k^2/2 essentially-distinct whisper phases.
  Sub-split: II = the phases admit a coarse cluster structure (K arcs, K small);
  III = genuinely scattered (no o(k^2)-arc cover of length < (1-2c)/2).
And branch S3+(I) is the fourth case (vernier), outside the trichotomy.

---

## PART III. KILL CHAINS AND THE UNPROVED BRIDGES

### Case I kill chain (steep carriers). Constants explicit.
Chain: distinct-phase steep squares cannot bury their orientation mismatch:
(a) [Crystallization, V] a mismatched contact cannot be buried — gaps wet every
misoriented interface;
(b) [alpha'-edge, V, corrected constant 1/240] an exposed edge of a steep square
(slope tan th_i) over an environment of tilts <= t0 <= th_i/2 pays local gap
>= (1/240) min(tan th_i - tan t0, 1/3) >= (1/240) min(tan th_i / 2, 1/3);
(c) charge ratio: the square's total possible union contribution is <= 4 d_i sin th_i
<= 4 (1+sqrt(2c)) sin th_i; the ratio (union contribution)/(alpha'-edge charge) is
<= sup_th 4(1+sqrt(2c)) sin th * 240 / min(tan th / 2, 1/3) = **2078** (machine I8;
sup at th = pi/4).
(d) overlap of charge regions: distinct squares' alpha'-edge regions (within eta=1/4
of the edge) can overlap; near-unit sides bound the multiplicity of squares whose
1/4-neighborhoods share a point by a constant; we budget C_ov = 12.

> **LEMMA X1 (exposure bookkeeping = Gap A, quantified; UNPROVED).**
> There is an absolute C_ov (conjectured <= 12) such that for every packing with all
> sides in [3/4, 5/4]: `M_steep <= 2078 * C_ov * G + [wall-anchored steep grains'
> contribution, absorbed into the same bound via the Wall lemma]`.
> Weakest sufficient form: M_steep <= C_X1 * G + (1-2c)/4 for some absolute C_X1.
> *Why it should be true:* a steep square contributing NEW union mass sits at a phase
> distinct from its steep neighbors, hence (by D4) either it has an exposed interface
> against whisper environment (alpha'-edge pays), or it is interior to a coherent
> steep grain — but grain-interior squares of a rigid grain REPEAT phases mod 1 up to
> the grain's drift, so new union mass from a grain is generated only along its
> boundary layer of thickness ~1/(sin th-bar) columns, whose exposed boundary pays;
> the gradient corollary [V] (X/120 * min(Theta,1/3), row-count-free) closes the
> "smoothed texture" escape; the Wall lemma anchors grains that reach walls.
> *Its enemy:* a moderate-size 45-degree grain (phases scatter internally at rate
> 0.414/step while all interfaces are grain-internal). The grain's own boundary is
> the only payer: boundary ~ 4 sqrt(m) edges for m squares vs internal phase mass
> min(1, m * 1.4) — the constants above survive this attack with a 23x margin at
> c = 1e-5 (machine I13), but the bookkeeping (that boundary/gradient/wall charges
> cannot ALL be dodged simultaneously) is the unproved content. This is exactly
> session-1's Gap A in its final quantitative form.

### Case II kill chain (whisper, clustered). Fully proved given the cluster data.
If the whisper arcs admit a K-arc cover of total length lambda (per axis), their
union contribution is M_whisper <= 2 lambda + 2 K * 2 d_max sin(2 t0)
<= 2 lambda + 4 K (1+sqrt(2c)) * 2 t0. With t0 = 1/(4k^2): fattening term
<= 2.2 K / k^2. [This is Theorem W's fattening step, verified [V], applied per class.]
So Case II self-destructs: clustering DESTROYS the union mass that S3+(II) demands.
Quantitatively: if K <= K-bar and lambda <= A sqrt(2c) + D/k then
M_whisper <= 2 A sqrt(2c) + 2D/k + 2.2 K-bar / k^2 — for the enemy this must still
reach (1-2c)/2, which fails for c, 1/k small: **Case II is dead the moment the
cluster structure exists.** No new lemma needed HERE; the lemma is that II-or-III is
really II (next).

### Case III kill chain (whisper, scattered) — the hard core.
The enemy needs ~k^2/2 essentially-distinct whisper phases mod 1 in a packing with
G + V-variance < 2c... wait: G < 2c and s < 2c (Prop 1.1). Phase freedom comes from
side deviations (accumulating ell^1 along rows ~ sqrt(2ck) >> 1 for k > 1/(2c):
variance does NOT forbid scattering — Route B Dead End 5, unrepaired) and from tilt
drift. The payment must be GEOMETRIC (local gap at phase dislocations), not
variance-accounting:

> **LEMMA X2 (dislocation cost / drift-to-local-gap; UNPROVED — the mod-1 Rigidity
> Lemma in its final, weakest, union form).**
> There are absolute C_X2, K2 such that every packing with all sides in
> [1 - sqrt(2c), 1 + sqrt(2c)], gap G <= 2c, k >= K2 has whisper-arc union
> `M_whisper <= C_X2 (sqrt(c) + 1/k)`.
> Equivalently (contrapositive): a near-tiling whose whisper bbox-extreme phases are
> spread over measure >> sqrt(c) pays gap > 2c.
> *Why it should be true:* the deficient column realizes winding 1 (a single unit of
> phase drift within one column) at gap cost k/(k+1) ~ 1: the only known mechanism
> for large phase drift charges ~1 unit of gap per unit of winding. Scattering
> measure ~1/2 of phases needs total pairwise drift >= ~1/2 unit; at the deficient-
> column exchange rate that is gap ~ 1/2 >> 2c. The unproved content is that the
> deficient-column rate is (up to a constant) the CHEAPEST: that no vernier-free
> arrangement of near-unit squares buys phase spread at o(1) gap per unit spread.
> *Its enemy:* the "gentle-giant multigrain" — many whisper grains, each internally
> rigid, with grain-to-grain phase offsets absorbed by O(sqrt(2c))-side adjustments
> along grain boundaries (the ell^1/ell^2 accumulation loss). Killing it needs the
> boundary-localized charge: each offset boundary either creates a sliver (gap ~
> offset x length) or a side mismatch propagating to a wall (Wall lemma pays).
> This is the single deepest open point of the whole program; No-Repair and Claim 3
> of RIGIDITY prove no measure-theoretic route (variance, dip mass, phases-only)
> can substitute for it.

### Case S3+(I) kill chain (vernier).
> **LEMMA X3 (vernier kill; UNPROVED — replaces and weakens "top-heavy kill").**
> There are absolute c3, K3 such that no packing with eps > 1/2 - c3, k >= K3 has a
> positive-measure set of saturating phases on either axis.
> *Why it should be true:* a saturating enemy contains over-full lines: k+1 squares
> whose chords tile [0,k] with slack <= k - Sum_L d sec th < ... and per-square
> deficits averaging 1/(k+1) — a vernier column. In every known realization
> (deficient column and its perturbations) the vernier's width-slack forces a gap
> sliver of area ~ k * (1 - column width) ~ 1 unless neighbors encroach into the
> column strip, which near-unit AP neighbors cannot and whisper-tilted neighbors can
> only by O(t0): expected true cost ~ 1 >> 2c. Also unconditional already: branch (I)
> forces s >= 1/(k+1) (Cor 1.9), b0 >= eps + Gamma ~ 1/2 (so ~ (1/2)/sqrt(2c)
> oversize squares ELSEWHERE), and k > 1/(2c) - 1. The unproved content is the
> quantitative "vernier column costs Omega(1) gap even inside an arbitrary tilted
> environment".
> *Its enemy:* a deficient-column-like stack whose flanks are hugged by whisper-tilted
> slightly-oversize squares that eat the sliver — exactly the b0 >= eps + Gamma
> arithmetic says the packing must ALSO be top-heavy: the two requirements (hug the
> vernier, keep s < 2c) fight; no explicit near-realization is known.

---

## PART IV. THE MINIMAL LEMMA SET AND THE CONDITIONAL THEOREM

The three bridges consolidate into TWO lemmas (X1 + X2 merge into the union bound):

> **LEMMA L1 (= X3, vernier kill).** There exist absolute c1 > 0, K1 such that no
> packing of N+1 squares in [0,k]^2 with k >= K1 and eps > 1/2 - c1 has a positive-
> measure set of saturating phases on either axis.
> *(Weakest known sufficient form; implied by — and strictly weaker than — the
> "top-heavy kill: no enemy has b0 >= eps", since saturation => b0 >= eps + Gamma.
> Note L1 is NOT needed at all for k <= 1/(2 c0) - 1 by Cor 1.9.)*

> **LEMMA L2 (union bound = the weakened mod-1 Rigidity Lemma; contains X1 + X2).**
> There exist absolute c2 > 0, K2 such that every packing of N+1 squares in [0,k]^2
> with k >= K2 and eps > 1/2 - c2 satisfies
> `U_x + U_y + V_x + V_y < 1 - 2 c2`.
> *(Pure union-measure statement: no arc counts, no cover structure, no top-heaviness
> hypothesis. Its proof program is the trichotomy: X1 bounds the steep contribution
> by 2078 * C_ov * G < 2078 * 12 * 2c; X2 bounds the whisper contribution by
> C_X2 (sqrt c + 1/k); their sum stays below 1 - 2c for c <= 1e-5, k >= 300 with
> margin 0.28 — machine I8/I9.)*

### THEOREM (Conditional Master Theorem).
**Assume Lemmas L1(c1, K1) and L2(c2, K2). Let c0 := min(c1, c2) and
K0 := max(K1, K2). Then for EVERY k >= 1:**
`f(k^2 + 1) <= k + (1/2 - c0)/k .`
*Proof.* Fix k >= K0 and suppose a packing has eps > 1/2 - c0. By S3+ it satisfies
(I) or (II). Branch (I) contradicts L1 (eps > 1/2 - c1). Branch (II) demands
U_x+U_y+V_x+V_y >= 2 eps + nonneg margins > 1 - 2 c0 >= 1 - 2 c2, contradicting L2.
So eps <= 1/2 - c0 for all k >= K0; unscaled, f(k^2+1) <= (N + 1/2 - c0)/k =
k + (1/2 - c0)/k. For k < K0: Singh's monotonicity [published] — k(f(k^2+1) - k) =
eps(k) is non-decreasing in k — gives eps(k) <= eps(K0) <= 1/2 - c0. QED

Dependencies of the proof besides L1, L2: Props 1.1-1.8 / S3+ (backbone: [V] pieces
plus the twice-derived, machine-verified [P] pieces Lemma 0, A''-mechanism, S2 ledger,
Fact 4.0 [V]) and Singh's published monotonicity. NOTHING else.

### Minimality discussion.
- L1 cannot be dropped: the deficient column sits exactly on the saturation boundary
  (beta = 1, saturating measure k/(k+1)) at eps = 0; nothing in the verified arsenal
  moves against a hypothetical eps ~ 1/2 vernier except the unquantified gap
  intuition. It CAN be weakened to k > 1/(2c0) - 1 only (Cor 1.9).
- L2 cannot be dropped: Prop 1.10 shows raw mass always suffices for (II); some
  rigidity statement converting low gap into union collapse is logically necessary.
  No-Repair [V] and RIGIDITY Claim 3 [P] prove that no measure-theoretic weakening
  (gap-mass inequalities, dip-mass/kappa bounds, variance) can replace it.
- Merging L1 into L2 fails: branch (I) enemies have no union obligation at all.
- Weakening L2 to "PH(K, lambda) holds" (Theorem W's hypothesis) is a STRONGER
  assumption (needs cover structure); the union form is the weakest input S3+ accepts.

### The instantiated constant.
Assuming the granular bridges with their computed constants (X1 with C_ov = 12:
C_X1 = 24,930; X2 with C_X2 = 30), the closing arithmetic
`2 * 26400 * c + 30 (sqrt c + 1/k) < 1 - 2c`
holds at **c0 = 1e-5, K0 = 300, margin +0.277** (machine I9; still +0.05 at
c = 1.4e-5). Hence the headline conditional result:
**Modulo X1 (constant 12), X2 (constant 30), and L1: f(k^2+1) <= k + (1/2 - 1e-5)/k
for all k.** The bottleneck constant is alpha'-edge's 1/240 times the overlap
multiplicity: improving 1/240 toward alpha's 1/60 and proving C_ov <= 4 would push
c0 toward 1e-4; the Theorem-W-style modeled arithmetic (K=2 clusters) reaches 1/400
but only for the exactly-rigid phantom class.

---

## PART V. THE UNCONDITIONAL STRUCTURE-OF-COUNTEREXAMPLES THEOREM

### THEOREM U (fully proved; Tier 1 uses [V]-and-published pieces only).
Let c in (0, 1/12], k >= 1, and let P be any packing of k^2+1 squares in [0,k]^2 with
eps > 1/2 - c. Then ALL of the following hold.
1. **(profile)** g + s = 1 - 2 eps < 2c; gap area < 2c; every side in
   (1 - sqrt(2c), 1 + sqrt(2c)); Sum d_i^2 > N - 2c. [Prop 1.1]
2. **(mandatory tilt)** Sum d_i th_i >= Sum d_i sin th_i >= tau >= eps > 1/2 - c and
   t >= 2 eps > 1 - 2c: a full faked unit of projection width. [Prop 1.2]
3. **(not axis-parallel)** P has a tilted square [BKU, published]; moreover k >= 2
   [T1: f(2) = 1, V].
4. **(no common frame)** the squares do not all share one orientation th with
   tan th = b/a Pythagorean and c | k [T3]; if they share ANY single orientation then
   eps < 1/2 strictly [T2] and Delta = Sum d_i^2 sin 2 th_i satisfies the T5 bound.
5. **(T5 floor)** Delta > ((1 - 2c)/(4(N+1)))^2: aggregate corner-triangle area is
   bounded below (weak but nonzero). [T5 contrapositive]
6. **(C'' scatter-or-oversize)** Sum (1 - w_i)_+ + max(U_x, U_y) >= 1, and hence
   `max(U_x, U_y) >= eps - b0 > 1/2 - c - b0`: either oversize mass b0 >= 1/4, or one
   axis's corner-triangle phase union exceeds 1/4 - c. [C'', V]
7. **(whisper => scattered-or-heavy; Theorem W)** for every t0, K, lambda: if all
   th_i <= t0 and the bbox-extreme phases of one axis are covered by K arcs of total
   length lambda, then 1/2 - c < eps <= b0 + lambda + 2 K (1 + sqrt(2c)) sin t0. In
   particular a whisper counterexample with b0 <= 1/4 admits NO phase cover with
   lambda + 2K(1+sqrt 2c) sin t0 <= 1/4 - c. [W, V]
8. **(no cheap exposed mismatch)** for every square edge e satisfying alpha'-edge's
   hypotheses over environment tilts <= phi0 <= (tan alpha)/2:
   (1/240) min(tan alpha - tan phi0, 1/3) <= G < 2c; so every eligible exposed
   interface has min(tan alpha - tan phi0, 1/3) < 480 c. [alpha'-edge, V-corrected]
9. **(buried coherence)** every buried contact point is orientation-matched
   (crystallization law); every mismatch angle alpha at a contact carries uncovered
   sectors of angle >= 2 alpha wetted by the < 2c gap budget. [V]
10. **(wall discipline)** Sum_floor (y_i |A_i| + (sin 2 th_i)/2 * |A_i|^2 /... ) +
    k |A_empty| <= g < 2c: the boundary layer is quantitatively axis-aligned and
    phase-locked on all four walls. [Wall lemma, V]
11. **(min-tilt)** if k >= 1274, some square has th_i < 1/(0.2745 k - 348). [V]
12. **(propagation)** counterexamples propagate upward: eps(k') >= eps(k) > 1/2 - c
    for every k' >= k [Singh, published] — so if ANY counterexample-at-level-c exists,
    one exists for all larger k, and all constraints above hold along the entire tail.

### Tier 1 additions promoted this session (G1's [V]-promotions + this file).
13. **(the S3+ dichotomy)** vernier structure (with s >= 1/(k+1), b0 >= eps + Gamma
    > 1/2 - c, k > 1/(2c) - 1, and >= (1/2 - c)/sqrt(2c) oversize squares) — or —
    U_x + U_y + V_x + V_y >= 2 eps + Sum_short m_i + Sum_long (1-d_i)^2 > 1 - 2c,
    despite item 7's clustering prohibition and item 8's interface tax. [S3+, this
    file; components [V] via G1]
14. **(kappa floors vacuous — by design)** t >= 2 eps > 1 - 2c puts the enemy exactly
    where Theorem K's floor (1-t)_+^2 < 4c^2 is negligible: no anti-concentration
    route remains [Theorem K now [V]; RIGIDITY Claim 3].

### Tier 2 additions (the remaining [P] pieces: T6's MPI chain).
15. **(dip and margin caps)** kappa + Sum m_i <= 2c: dip mass below 2c AND the total
    per-square counting margins below 2c. [T6]
16. **(kappa-coupling)** 2 eps <= |Av| + U_x + U_y - Sum m_i, i.e.
    U_x + U_y >= 2 eps - 1 + |pi(G)| + Sum m_i. [P via T6]
17. **(covering law)** on at least one axis, outside dip sets with delta_x delta_y
    < 2c: undersize-miss counts are pointwise dominated by oversize frac-hits plus
    r - 1 [RIGIDITY D1/D4, [V] via G1].

*Every Tier-1 item (1-14) is proved by [V]-verified or published results; Tier-2
(15-17) additionally uses T6 [P]. No unproved lemma enters Theorem U.*

---

## PART VI. ANSWERS TO THE ASSIGNMENT'S DIRECT QUESTIONS

1. *"Does case (III) near-zero-tilt + b0 < eps close NOW?"* — The chain b0 < eps
   => beta < 1 => S2/S3(II) is CONFIRMED exact (Props 1.7/1.8, machine I3/I5). But it
   closes into a REQUIREMENT (U+V >= 2 eps + margins), not a contradiction: by Prop
   1.10 the raw mass is always available, so nothing dies unconditionally. What DOES
   close unconditionally: literal whisper (all th <= t0 < eps/(N+eps)) dies by T4
   alone (machine I11); AP with b0 < eps dies (S4); AP entirely dies (BKU); and
   saturating enemies with k <= 1/(2c) - 1 die (Cor 1.9, new). The near-AP case's
   residue is exactly L2 — as the preamble's strategic fact predicted, the kill must
   target clustering, not mass.
2. *"Grind the exact chain: what EXACTLY must U+V exceed for a b0-light enemy?"* —
   `U_x+U_y+V_x+V_y >= 2 eps + Sum_{w<1} d sigma (2-d-w) + Sum_{w>=1} (1-d)^2`,
   exactly; the bracket s - Sum(1-w)_+^2 equals the two margin sums (Prop 1.7).
3. *"Can bridges be merged?"* — X1 + X2 merge into L2 (union form); X3 = L1 stays
   separate (branch (I) has no union obligation). Two lemmas is minimal (Part IV).
4. *"Compute c0."* — min(c1, c2) in the minimal form; 1e-5 (K0 = 300, margin 0.28)
   in the instantiated form; bottleneck = alpha'-edge 1/240 x overlap multiplicity.

## PART VII. ADVERSARIAL SELF-ATTACK (what I tried to break)

- S2 ledger for big squares: c_i = p_i q_i - L_i needs Fact 4.0 for w up to
  sqrt2(1+sqrt 2c) < 2 — verified range d <= 2.8 covers it; V-arcs stay arcs
  (machine I14). Idle => w < 1 uses equal projection widths [V]. OK.
- S3+ branch split: is "saturating" the right disjunction? S2's proof needs
  M_X, M_Y nonempty a.e. ON E; nonsaturation gives exactly that; saturation on a null
  set is harmless (a.e. arguments). OK.
- Vernier CS (Cor 1.9): deficits 1 - d_j may be negative for oversize line members —
  Cauchy-Schwarz over signed reals still valid (machine I7 includes negatives). OK.
- The 45-degree single square: makes U_x = U_y ~ 1 all by itself with only ~ 5e-4
  exposed-interface charge — kills any hope of c0 > ~2e-4 via this route, absorbed at
  c0 = 1e-5 with 23x margin (machine I13). This is why c0 is small: alpha'-edge's
  1/240 must tax a 0.7-length arc.
- Whisper-mass double counting: t0 = 1/(4k^2) makes whisper tilt mass ~ 1/4 which is
  NOT below eps - so steep squares are not mandatory; the trichotomy correctly splits
  on which class CARRIES THE UNION (D1 note), not on T4 mass. Fixed in D1.
- Theorem W cannot be cited for a mixed packing (it needs ALL tilts <= t0): Case II
  uses only W's fattening STEP (verified separately) on the whisper subfamily. OK.
- Sign of the S3(II) margins: 2 - d - w > 0 for shorts because d <= w < 1. OK.
- L1 vs L2 gap at b0 in [eps, eps + Gamma): beta can still be < 1 there
  (b0 < eps + Gamma), so S3+(II) still fires; the split is exhaustive: saturation
  handled by L1 regardless of b0. OK — no crack between the lemmas.

## FILES
- This file + `g2_checks.py` (ALL PASS) in scratchpad/session3/G2/ and copied to
  /Users/kylekabasares/Desktop/erdos-106/agent-reports/session3-derivations/.
