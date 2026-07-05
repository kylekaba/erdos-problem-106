# Capture-side squeeze with tilts: complete derivations

Notation as in ERDOS_106_REPORT.md. T=[0,k]^2, N=k^2, n=N+1 squares S_i, sides d_i,
folded tilts th_i in [0,pi/4], u1 = cos+sin, sigma_i = u1(th_i)-1, w_i = d_i u1(th_i),
eps = sum d_i - N, g = N - sum d_i^2, s = sum(1-d_i)^2, b0 = sum(d_i-1)_+.
Shift torus p=(x,y); p_i(x) = # vertical lattice lines meeting S_i (= meeting its
x-projection, an interval of length w_i); q_i(y) likewise; c_i = |S_i cap Lambda_p|;
C = sum c_i <= N a.e. (budget); Av = {C = N}; hits = N - C >= 0, E[hits] = g,
so |Av| >= 1-g (Markov; No-Repair direction).
B_i^x = the two tall-corner-triangle x-phase arcs of S_i (each of length d_i sin th_i,
at the bbox x-extremes), B_i^y the wide ones; U_x = |union_i B_i^x|, U_y likewise
(exactly C''s bad sets). NEW: V_x := |union_i {x : p_i(x) >= 2}| (for w_i in [1,2) an
arc of length w_i - 1 at the bbox-min phase; for w_i >= 2 the whole circle), V_y likewise.
beta := sum_i (1 - d_i sec th_i)_+  (chord-deficit mass; NEW).

## Lemma 0 (chord constancy; exact geometry, NEW)
For a square of side d, folded tilt th in (0,pi/4], with bbox x-range normalized to
[0,w]: the vertical chord length ch(x) satisfies ch(x) <= d sec th for all x, with
ch(x) = d sec th IDENTICALLY on the middle region [d sin th, d cos th].
Proof: vertices A=(ds,0), B=(w,ds), C=(dc,w), D=(0,dc) (s=sin th, c=cos th). For
x in [ds,dc], bottom envelope = edge AB: y=(x-ds)tan th; top envelope = edge DC:
y = dc + x tan th; chord = dc + ds tan th = d(c^2+s^2)/c = d sec th. On [0,ds] and
[dc,w] the chord tapers linearly to 0. At th=0 the middle region is the whole
projection and ch = d. At th=pi/4 the middle region degenerates to a point.
By the 90-degree symmetry of the square, horizontal chords obey the same law with
the same folded th (max chord d/max(cos phi, sin phi) = d sec(folded)).
[Machine check: max |ch - d sec th| on middle region = 1.6e-15 over 300 random
(d,th), 80 x-values each; 0 exceedances of d sec th anywhere.]

Consequence: if x mod 1 is outside union_i B_i^x, then EVERY lattice line meeting
ANY square meets it in its middle region, where its chord is exactly d_i sec th_i.

## Lemma A'' (tilted over-full-line exclusion, NEW; generalizes F1's Lemma A)
Let a packing of n = N+1 squares in T have beta = sum_i (1 - d_i sec th_i)_+ < 1.
Then for a.e. x with x mod 1 not in union_i B_i^x, some square has p_i(x) = 0.
Symmetrically in y with B_i^y.

Proof. Take x generic (avoiding the finitely many phases mod 1 where some lattice
line passes through a bbox endpoint, an envelope kink, or a vertex — a null set) with
x good and all p_i(x) >= 1. Each square meets some line x+m; since its projection is
inside [0,k] and x in (0,1), m in {0,...,k-1}. That is >= N+1 incidences on k lines,
so some line l = {x+m} x R meets a set L of at least ceil((N+1)/k) = k+1 squares.
For each j in L, x good means x+m lies in the middle region of S_j's bbox (Lemma 0),
so the chord of S_j on l has length exactly d_j sec th_j, its open part lies in the
interior of S_j, and it lies in [0,k] (containment). Interiors of the squares are
pairwise disjoint, so the chords have pairwise disjoint interiors:
    sum_{j in L} d_j sec th_j <= k .
Hence sum_{j in L} (1 - d_j sec th_j) >= (k+1) - k = 1, and a fortiori
beta >= sum_{j in L} (1 - d_j sec th_j)_+ >= 1. Contradiction with beta < 1. QED

Remarks. (a) At th_i = 0 for all i this is exactly F1's Lemma A but with the
hypothesis "all d_i <= 1 and sum d_i > N" (i.e. sum(1-d_i) < 1, all terms >= 0)
replaced by the weaker positive-part hypothesis sum(1-d_i)_+ < 1: big squares are
now allowed. (b) Tilts HELP the hypothesis: (1-d sec th)_+ <= (1-d)_+, with strict
gain for tilted sub-unit squares (quadratic in th). (c) 45-degree squares contribute
0 to beta but their B-arcs cover their whole projection, so they shrink the good set
instead — the lemma stays sound, becoming vacuous only when U_x -> 1.
(d) Sharpness: the deficient column U_k has beta = (k+1)(1/(k+1)) = 1 EXACTLY and a
good full-hit x-set of measure k/(k+1) > 0; the split cell also has beta = 1 with
positive full-hit measure on one axis. So the constant 1 cannot be raised.
[Machine check: on 4 column configs (AP and tilted t=0.02,0.05), 120-150 sampled
good full-hit x each: an over-full line with k+1 squares was found at every sample,
chord sum <= k, chords = d sec th to 1e-9, line deficit sum >= 1. On all 12 test
packings: whenever the good full-hit measure was positive, beta >= 1 held; the two
beta < 1 packings (diamond family) had good full-hit measure 0.]

## Theorem S2 (tilted capture-measure bound, NEW)
Every packing of n = N+1 squares in T (any sizes, any orientations) with beta < 1
satisfies
    |Av| <= sum_i (1 - w_i)_+^2 + U_x + U_y + V_x + V_y .

Proof. Let Gx = [0,1) minus union B_i^x, Gy likewise, E = Gx x Gy; |E^c| <= U_x+U_y.
On E (generic): no lattice point lies in any corner triangle (verified product
structure: L_i >= 1 forces x-phase in B_i^x or y-phase in B_i^y), so c_i = p_i q_i
for every i.
Work on Av cap E. There C = sum p_i q_i = N. Since both projections of S_i have
width w_i: p_i = 0 forces w_i < 1 (else p_i >= floor(w_i) >= 1), and then also
q_i <= 1; p_i q_i >= 2 forces max(p_i,q_i) >= 2, hence w_i >= 1. Call i SHORT if
w_i < 1 (then on E, c_i = 1_{X_i}(x) 1_{Y_i}(y) with arcs X_i, Y_i of length w_i)
and LONG if w_i >= 1 (then c_i >= 1 on E).
Idle set I := {i : c_i = 0} = M_X cup M_Y, where M_X(x) = {i : p_i(x)=0},
M_Y(y) = {i : q_i(y)=0} (x-only and y-only events!). All idles are short. Excess
mu := sum_{i not in I} (c_i - 1) = N - (N+1-|I|) = |I| - 1.
By Lemma A'', for a.e. (x,y) in E: M_X(x) and M_Y(y) are both nonempty. Split:
 (1) |I| = 1: then M_X = M_Y = {i} for some short i. The event is contained in
     {x : p_i = 0} x {y : q_i = 0}, of measure (1-w_i)^2; the events are disjoint
     across i. Total contribution <= sum_short (1-w_i)^2 = sum_i (1-w_i)_+^2.
 (2) |I| >= 2: then mu >= 1, so some long square has p_i q_i >= 2, i.e. p_i >= 2 or
     q_i >= 2; hence x in the V_x-union or y in the V_y-union. Contribution
     <= V_x + V_y.
Adding |E^c| <= U_x + U_y gives the bound. QED

Restriction to AP (th = 0: U = 0, w = d): every AP packing of N+1 squares with
sum(1-d_i)_+ < 1 has |Av| <= sum_{d_i<1}(1-d_i)^2 + V_x + V_y — extends restricted
FCMB-AP (which required ALL d_i <= 1) to arbitrary sizes.
[Machine check: 12 packings (columns AP + tilted, split cell, 10-diamond 45-degree
family, mixed tilted, long tilted w=1.147, long AP d=1.3, random strips), grids up
to 420^2 with generic offsets: budget C <= N everywhere; on E zero violations of
c_i = p_i q_i (all i, all shifts), zero idle-longs, zero multi-capturing shorts;
S2 inequality satisfied whenever beta < 1. Sharpness: the deficient column
(beta = 1) violates the conclusion by (k-1)/(k+1): hypothesis beta < 1 is exact.]

## Corollary S3 (enemy alternative — the assembled squeeze)
Every packing of N+1 squares with eps = sum d_i - N > 0 satisfies at least one of
 (i) b0 >= eps + Gamma, where Gamma := sum_i [ (1-d_i)_+ - (1 - d_i sec th_i)_+ ] >= 0
     is the chord (sec-)gain of the tilts     [ this is exactly "beta >= 1" ];
 (ii) U_x + U_y + V_x + V_y >= 2 eps + sum_{w_i<1} m_i + sum_{w_i>=1} (1-d_i)^2 ,
     with m_i = d_i sigma_i (2 - d_i - w_i) >= 0 the exact T6 margin (short branch).

Proof of (ii) given beta < 1: Markov gives 1-g <= |Av|; Theorem S2 bounds |Av|;
the Structure Identity gives 1-g = s + 2 eps; and the EXACT identity
    (1-w)^2 = (1-d)^2 - d sigma (2-d-w)          [machine-checked to 2e-16]
gives sum_short (1-w)^2 = sum_short (1-d)^2 - sum_short m_i; finally
s - sum_short (1-d)^2 = sum_long (1-d)^2. Rearrange. For (i): beta =
sum(1-d)_+ - Gamma = (1 - eps + b0) - Gamma (Structure Identity on positive parts:
sum(1-d)_+ = (N+1) - sum d + b0 = 1 - eps + b0), so beta >= 1 iff b0 >= eps + Gamma. QED

## Corollary S1 (all-short regime, unconditional)
If all w_i < 1 and sum d_i > N, then U_x + U_y >= 2 eps + sum_i m_i.
(beta <= sum(1-d_i) = 1 - eps < 1 automatically; V = 0.)

## Corollary S4 (BKU-free AP enemy kill up to b0)
No AP packing of N+1 squares has sum d_i > N and b0 < eps.
Proof: (i) fails (Gamma = 0, b0 < eps). So (ii): U = 0, and for AP longs the V_x
arcs have length d_i - 1 (any long with d >= 2 gives b0 >= 1 > eps, impossible since
eps < 1/2), so V_x + V_y <= 2 b0 < 2 eps <= RHS. Contradiction. QED
(At b0 = 0 this is F1's restricted FCMB-AP corollary = the half-page BKU reproof;
the b0-extension is new. Entirely lattice-free of BKU.)

## The kappa-coupling (secondary; unconditional given T6 [P])
kappa := E[(2N+1-P-Q)_+]. On {sum L_i = 0} (superset of E): C = sum p_i q_i >=
P + Q - (N+1) pointwise (the (0,>=2) corner impossible by equal widths), and C <= N,
so P+Q <= 2N+1 there; on {sum L_i = 0} cap {hits >= 1}: P+Q <= 2N, integrand >= 1.
Hence   kappa >= (1 - U_x - U_y - |Av|)_+  ,
and with T6 (2 eps <= 1 - sum m_i - kappa):
    2 eps <= |Av| + U_x + U_y - sum_i m_i        (unconditional; no beta needed)
equivalently  2 eps + sum m_i + |pi(G)| <= 1 + U_x + U_y  (|Av| = 1 - |pi(G)|).
This is exactly the mechanism the assignment sketched; on its own it is weaker than
S3 wherever S2 applies (S2 route replaces |Av| <= 1 by the capture bound), but it
holds with NO hypothesis on beta and quantifies "the kappa-inequality gets teeth":
any enemy must either carry dip mass or bad-phase mass.

## Behaviour on the four test configurations
(i) AP enemy, all d <= 1: b0 = 0, Gamma = 0, (i) fails; all-short so (ii) reads
    0 >= 2 eps + sum m_i > 0: contradiction. Reproves BKU for d <= 1 — and it IS
    F1's argument (Lemma A'' restricted = Lemma A; case (1) = the C3 decomposition).
(ii) Deficient column: eps = 0 (not an enemy; theorem silent, correctly). It sits
    EXACTLY on the boundary of (i): b0 = 0 = eps + Gamma, beta = 1; and it violates
    S2's conclusion, so beta < 1 is sharp. The whole extremal manifold (split cells,
    stack gadgets, columns) satisfies beta = 1 identically.
(iii) Coherent whisper grid (all tilts <= t0, K phase clusters of total length
    lambda per axis, near-unit sides): b0 = 0 => (i) fails; U_x <= lambda + 2K dmax
    sin t0 and V_x <= lambda + K dmax sigma-arcs of the same size, so (ii) forces
    2 eps <= 2 lambda + O(K dmax t0) — Theorem W's kill with the per-square penalty
    sum(d-1)_+ replaced by the UNION V and the constant doubled. No PH hypothesis
    enters the theorem; PH-type data only enters when evaluating U,V on the model.
(iv) 45-degree configurations: beta counts (1 - d sqrt2)_+ (usually 0) but U_x =
    U_y ~ 1 (B-arcs of length d/sqrt2 per square): (ii) becomes vacuous. 45-degree
    remains the alpha'/T2 jaw's territory, as before.

## Code
squeeze_check.py in this directory. 12 SAT-validated packings; all assertions pass:
chord constancy 1.6e-15; algebra identity 2.2e-16; budget everywhere; E-structure
(c=pq / idle-short / multi-long) zero violations on ~2.1M grid shifts total;
Lemma A'' witness test 531/531 sampled good full-hit x across 4 column configs;
S2 satisfied on all beta<1 configs; beta=1 sharpness confirmed on columns k=2,3.
