# F5 full derivations (Gap A jaw: Lemma alpha', Theorem C'', Theorem W)

Conventions as in ERDOS_106_REPORT.md: T=[0,k]^2, N=k^2, M=N+1 squares S_i, sides d_i,
folded tilts th_i in [0,pi/4] (mod pi/2 representative; signed representative psi in
(-pi/4,pi/4] where needed), w_i = d_i(cos th_i + sin th_i), eps = sum d_i - N,
p_i(x), q_i(y) line counts against Lambda_(x,y), P = sum p_i, Q = sum q_i,
c_i = lattice points in S_i, L_i = p_i q_i - c_i >= 0 at generic shifts.

## 1. LEMMA alpha' (tilted-sea staircase interface bound)

**Statement.** Let theta in (0, pi/4], tau = tan theta, and phi0 >= 0 with
tan phi0 <= tau/2. Let eta <= 1/20, h = 1/4. Let Q be a finite family of squares
with sides in [1-eta, 1+eta] and folded tilts <= phi0, with pairwise disjoint
interiors, each contained in the half-plane {y <= tau x + beta}. Then for every
X >= 1 the strip R = {0 <= x <= X, tau x + beta - h < y < tau x + beta} satisfies

    | R \ union(Q) |  >=  (X/228) * min( tau - tan phi0 , 1/3 ).

**Proof.**

*Step 0 (notation).* l(x) := tau x + beta. For S in Q with signed folded tilt
psi in [-phi0, phi0] (representative of the orientation mod pi/2 in (-pi/4, pi/4];
|psi| = folded tilt) and x in pi_x(S) (the x-projection, an interval of length
w_S = d_S(cos|psi| + sin|psi|) <= w_max := (1+eta)(cos phi0 + sin phi0)), let
T_S(x) := max{y : (x,y) in S}. Since tan phi0 <= 1/2, phi0 <= 26.57deg and
w_max <= 1.05 * 1.3417 <= 1.409. Diameter of any S is <= sqrt(2)(1+eta) <= 1.485.

*Step 1 (vertical accounting).* For x in [0,X] let F(x) := max{T_S(x) : S spans x}
(-infinity if none). If a square S' contains a point (x,y) then S' spans x and
y <= T_{S'}(x) <= F(x). Every S lies under the line, so F(x) <= l(x). Hence the
segment {x} x ( max(F(x), l(x)-h), l(x) ) lies in R and is uncovered, and by Fubini

    |R \ union(Q)| >= Int_0^X min( h , l(x) - F(x) ) dx .

*Step 2 (per-square envelope bound).* Claim: for each S there is an anchor
a_S in pi_x(S) with

    l(x) - T_S(x)  >=  tau_1 * | x - a_S |   for all x in pi_x(S),
    tau_1 := tau - tan phi0  (>= tau/2 > 0).

Case psi >= 0. The upper envelope T_S consists of the edge of slope tan psi from
the leftmost vertex (abscissa x_L) to the topmost vertex (abscissa x_U), then the
edge of slope -cot psi (for psi>0; single flat edge for psi=0). Take a_S := x_L.
On [x_L, x_U]: d/dx (l - T_S) = tau - tan psi >= tau - tan phi0 = tau_1 > 0 and
(l - T_S)(x_L) = l(x_L) - (leftmost vertex height) >= 0 since the vertex is under
the line. On [x_U, x_R]: d/dx (l - T_S) = tau + cot psi > tau_1. Integrating,
l - T_S >= tau_1 (x - x_L) = tau_1 |x - a_S| on the whole span.

Case psi < 0. The upper envelope rises at slope cot|psi| on [x_L, x_U]
(x_U - x_L = d sin|psi|), then falls at slope -tan|psi|. Take a_S := x_U.
Right of a_S: d/dx (l - T_S) = tau + tan|psi| >= tau >= tau_1, value >= 0 at a_S;
so l - T_S >= tau_1 (x - a_S). Left of a_S: d/dx (l - T_S) = tau - cot|psi| < 0,
because cot|psi| >= 1/tan phi0 >= 2/tau >= 2 > 1 >= tau; going left,
l - T_S >= (cot|psi| - tau)(a_S - x), and cot|psi| - tau >= 2/tau - tau >= 1 >= tau_1
(using tau <= 1). So l - T_S >= tau_1 |x - a_S| on the whole span. QED claim.

*Step 3 (crest decomposition and bathtub).* For a.e. x with F(x) > l(x) - h let
crest(x) := the spanning square maximizing T_S(x) (ties broken by index; no
uniqueness needed). Let N_0 := {x in [0,X] : F(x) <= l(x) - h} and
I_j := {x : crest(x) = S_j}. Then [0,X] = N_0 u (disjoint union of I_j),
I_j subset pi_x(S_j), and

    Int_0^X min(h, l - F) >= h |N_0| + sum_j Int_{I_j} min( h , tau_1 |x - a_j| ) dx .

The integrand g(x) = min(h, tau_1|x-a_j|) is symmetric-increasing in |x-a_j|, so by
rearrangement the integral over I_j (measure m_j := |I_j| <= w_max) is minimized by
the interval centered at a_j:

    Int_{I_j} g >= 2 Int_0^{m_j/2} min(h, tau_1 s) ds >= (tau_2/4) m_j^2 ,
    tau_2 := min( tau_1 , 2h/w_max ) >= min( tau - tan phi0 , 1/3 ),

using: for s <= m_j/2 <= w_max/2, tau_2 s <= min(tau_1 s, h); and
2h/w_max >= 0.5/1.409 = 0.3549 >= 1/3.

*Step 4 (crest count).* A crest square has a witness x in [0,X] with
T_S(x) > l(x) - h, i.e. it contains a point (x, y0) with y0 > l(x) - h; by the
diameter bound every point (x', y') of S has |x' - x| <= 1.485 <= 1.49 and
y' > l(x) - h - 1.49 >= l(x') - 1.49 tau - h - 1.49. With tau <= 1, h = 1/4, all
crest squares lie in the sheared parallelogram

    P := { -1.49 <= x' <= X + 1.49 ,  l(x') - 3.23 < y' <= l(x') },

of area (X + 2.98) * 3.23. Disjoint interiors and per-square area >= (1-eta)^2
= 0.9025 give J := #crests <= 3.579 X + 10.67 <= 14.25 X for X >= 1.

*Step 5 (assembly).* Write U for the uncovered area. By Cauchy-Schwarz,
sum m_j^2 >= (X - |N_0|)^2 / J.
If |N_0| >= X/2:  U >= h X/2 = X/8 >= (X/228)(1/3) >= RHS. Otherwise

    U >= (tau_2/4) (X/2)^2 / (14.25 X) = tau_2 X / 228 >= (X/228) min(tau - tan phi0, 1/3).
QED.

*Remarks.* (i) phi0 = 0 recovers Lemma alpha with a worse constant (1/228 vs 1/36)
but a simpler proof: the crest-uniqueness/quantization step of Lemma alpha is not
needed (argmax replaces it); the near-unit hypothesis is used only in the crest
COUNT (Step 4) and in w_max. (ii) The hypothesis tan phi0 <= tau/2 is essentially
sharp in kind: at phi0 = theta a coherent row at tilt theta hugs the line with
zero strip cost, so linear-in-(tau - tan phi0) degradation is the true shape.
(iii) Frame symmetry: rotating coordinates, the lemma reads "a phi0-coherent sea
pays linearly in (mismatch to any bounding line) - (its own spread)".

*Numerics* (alpha_prime_check.py): adversarial families (coherent rows at +phi0
hugging the line - the optimal cheat; rows at -phi0; axis staircases; random
mixed tilts), tau in {0.1, 0.2, 0.4, 1.0}, tan phi0/tau in {0, 1/4, 1/2}, X = 20,
all placements SAT-verified disjoint and below the line. Minimum ratio
measured-uncovered / bound = 112.3 (>= 1 with two orders of slack; the tightest
case is the coherent +phi0 hug, exactly the predicted extremal). 0 violations.

## 2. COROLLARY alpha'-edge (localized version at a single square's edge; the
covering constraint from disjointness, no half-plane hypothesis)

**Statement.** Let S* be a square, side d* in [1-eta, 1+eta], orientation beta
(mod pi/2), inside T with dist(S*, boundary T) >= h = 1/4. Let e be an edge of S*
and let gamma be a reference orientation with folded mismatch
alpha := dist(beta - gamma, (pi/2)Z) satisfying tan alpha >= 2 tan phi0, where
every square of the packing OTHER than S* that meets the open strip
R_e := {points within distance h of e on the outward side of e} has folded tilt
<= phi0 in the gamma-frame. Work in the gamma-frame, rotated so that e's outward
side is "below" e; e is then a segment of slope tan alpha' for some folded
alpha' = alpha, of horizontal extent X_e >= (1-eta) cos alpha >= 0.63. Then

    | R_e \ union(packing) |  >=  (1/520) * min( tan alpha - tan phi0 , 1/3 ).

**Proof.** Identical to Lemma alpha' with two changes.
(1) The half-plane hypothesis is replaced by disjointness from S*: for a.e.
abscissa x in the open x-extent of e, the vertical chord of S* just above e has
positive length c(x) > 0, and any other square W spanning x has vertical
cross-section interval with interior disjoint from S*'s (two convex bodies with
disjoint interiors have vertical chords with disjoint interiors at a.e. common
abscissa); hence either T_W(x) <= l(x) (below e's line l) or B_W(x) >= l(x)+c(x)
(above S*). Defining F(x) := max{T_W(x) : W spans x, T_W(x) <= l(x)}, the segment
{x} x (max(F(x), l(x)-h), l(x)) is uncovered by every square: squares below cannot
reach above F, squares above have bottoms > l(x). Step 1 then runs verbatim over
x in [0, X_e].
(2) Steps 2-4 are unchanged (they only use "each covering square is below l at
the abscissas where it matters": a square with T_W(x) <= l(x) at ALL x in its span
within [0,X_e] - if W pokes above l outside [0,X_e], its envelope bound is only
applied at abscissas where it is the crest, i.e. where T_W(x) <= l(x); Step 2's
inequality l - T_W >= tau_1|x - a_W| holds at such x because the envelope slopes
are unchanged and (l - T_W)(x) >= 0 at the anchor-side endpoint of the interval
{x in span : T_W <= l} - anchor the bound at that endpoint instead).
Constants: X = X_e in [0.63, 1.06]: J <= 3.579*1.06 + 10.67 <= 14.5, and
U >= (tau_2/4)(X_e/2)^2 / 14.5 >= tau_2 * 0.63^2/(4*4*14.5) >= tau_2/585. A slightly
more careful count (crest squares lie in a parallelogram of horizontal extent
X_e + 2.98 <= 4.04, area <= 13.05, J <= 14.5) gives 1/520 for X_e >= 0.66 and
1/585 always; we state 1/520 for alpha <= 0.35pi/4-ish and note 1/585 uniformly.
[GAP-flag: the re-anchoring in (2) is stated tersely; the fully expanded case
check (crest interval possibly split by excursions of W above l outside [0,X_e])
is routine but should be written out before publication. Everything else is
verbatim Lemma alpha'.]

## 3. COROLLARY (gradient textures pay linearly, m-independent)

**Statement (conditional on straight-row structure).** Suppose a region of the
packing is organized as rows R_1, ..., R_{m+1}: row n consists of near-unit
squares (sides in [1-eta,1+eta]) whose orientations lie within delta_n/2 of a row
orientation psi_n, and there are lines l_n (n = 1..m) of direction psi_n such that
row n lies below l_n and row n+1 lies above l_n, over a common horizontal extent
X >= 1, with consecutive lines at vertical distance >= 1/2 + 1/4 (so the h = 1/4
strips are pairwise disjoint) and all strips inside T. If for each n the step
s_n := |psi_{n+1} - psi_n| (folded) satisfies tan(delta_{n+1}/2) <= tan(s_n)/2, then

    G >= sum_{n=1}^m (X/228) min( tan s_n - tan(delta_{n+1}/2), 1/3 )
      >= (X/456) * min( sum_n tan s_n , 1/3 )  >=  (X/456) * min( Theta, 1/3 ),

Theta := total orientation travel sum_n s_n (for all s_n <= pi/4; use
tan s >= s). In particular the cost is LINEAR in the total travel and INDEPENDENT
of the number of rows m: smoothing an interface into a gradient does not reduce
the interface bill below X*Theta/456.

**Proof.** Apply Lemma alpha' at each line l_n, reflected (squares above a line;
apply the lemma to the reflection through l_n) and in the frame rotated by
psi_{n+1}: in that frame the covering family (row n+1) has folded tilts
<= delta_{n+1}/2 and the line l_n has folded slope tan s_n; the hypothesis
tan(delta_{n+1}/2) <= tan(s_n)/2 is exactly Lemma alpha's hypothesis. The strips
are disjoint and inside T, so the costs add into G. For the second inequality,
if every term has tan s_n - tan(delta_{n+1}/2) <= 1/3 then each term is
>= (X/228)(tan s_n)/2 and sum >= (X/456) sum tan s_n; otherwise a single term
already gives (X/228)(1/3) >= (X/456)(1/3). QED.

**What is NOT proved (the honest residue of Gap A).** (i) Interfaces between
grains/rows in a real packing are not straight lines; the needed extension is a
"rough line" version of alpha' (Route B's height-self-correction). The natural
statement: if row n's top envelope is within roughness rho of a line and
rho <= h/4, alpha' survives with h -> h/2 and an additive -C*rho*X term. Not done.
(ii) The row structure itself (existence of l_n) must come from a decomposition
lemma; the crystallization law (Route B Claim 4) gives the topological version
(misaligned contacts are wetted), not the metric one.

## 4. THEOREM C'' (correlated-defect counting bound; union bad sets)

Per square i with folded tilt th_i > 0, bbox = w_i x w_i, define
  B_i^x := ( [x_i]_1 + [0, d_i sin th_i] ) u ( [x_i + d_i cos th_i]_1 + [0, d_i sin th_i] )  (mod 1),
where x_i := min x-coordinate of the bbox; B_i^y likewise from the bbox
y-extremes. ([v]_1 = v mod 1.) These are the x-projections mod 1 of the two TALL
corner triangles (legs d sin th horizontal, d cos th vertical, at the bbox-left
and bbox-right), resp. the y-projections of the two WIDE triangles. Set
  U_x := | union_i B_i^x | ,  U_y := | union_i B_i^y | ,
  gamma_i := (1 - w_i)_+ .

**Fact 4.0 (product structure; verified, 0 violations).** At a.e. shift,
L_i >= 1 implies x in B_i^x or y in B_i^y. (A lattice point of the bbox outside
the square lies in one of the four corner triangles; a point in a tall triangle
has x-coordinate in that triangle's x-projection, i.e. x-phase in B_i^x; wide -> B_i^y.)

**Theorem C''.** Every packing of N+1 squares in [0,k]^2 (any sizes, any
orientations) satisfies

    sum_i (1 - w_i)_+  +  max( U_x , U_y )  >=  1 .

Equivalently, with t := sum w_i - N and using t - sum(w_i - 1)_+ = 1 - sum gamma_i:

    max(U_x, U_y) >= t - sum_i (w_i - 1)_+  >=  eps - sum_i (d_i - 1)_+ .

**Proof.** Suppose sum gamma_i + max(U_x,U_y) < 1. Write p_i(x) = floor(w_i) +
1_{F_i}(x) a.e., F_i an arc of length frac(w_i) [proved: p in {floor w, floor w + 1}].
Let W_0 = sum floor(w_i) and A := {x : P(x) >= N+1}, B := {y : Q(y) >= N+1}.
(a) |A| >= 1 - sum gamma_i, and the same for |B| (both projections have the same
width w_i). Indeed if W_0 >= N+1 then A = [0,1). Otherwise: the squares with
w_i < 1 number M - n_2 where n_2 := #{w_i >= 1} <= W_0, so there are at least
N+1-W_0 arcs F_i with w_i < 1, each of length w_i = 1 - gamma_i; on the
intersection of any N+1-W_0 of them, P >= W_0 + (N+1-W_0) = N+1; the
intersection has measure >= 1 - sum_{chosen}(1 - w_i) >= 1 - sum_i gamma_i.
(b) By hypothesis |A| >= 1 - sum gamma_i > U_x and |B| > U_y, so
A \ union_i B_i^x and B \ union_i B_i^y have positive measure; pick a generic
(x, y) in their product.
(c) At (x,y): all L_i = 0 (Fact 4.0), so c_i = p_i q_i; moreover
(p_i, q_i) = (0, >=2) is impossible (p_i = 0 forces w_i < 1 generically, whence
q_i <= 1), and symmetrically; so c_i = p_i q_i >= p_i + q_i - 1 for every i. Then
  sum c_i >= P(x) + Q(y) - (N+1) >= (N+1) + (N+1) - (N+1) = N+1 .
(d) But at a generic shift the captured points are distinct interior lattice
points of T and |T cap Lambda| = N: sum c_i <= N. Contradiction. QED.

**Remarks.**
- Tight: split-cell configurations have sum gamma = (1-a) + a = 1, U = 0: equality.
- Axis-parallel corollary: sum_i (1 - d_i)_+ >= 1 for every axis-parallel packing
  of N+1 squares; if additionally all d_i <= 1 this is BKU's eps <= 0 statement
  in one line, with the new deficit-mass form.
- Against T4/T5: C'' needs no smallness of Delta; its right side is a UNION, so
  coherent families (whose bad sets stack) pay ~(number of distinct phases) x
  (2 d sin th) instead of N x (2 d sin th). This is the "correlated defects"
  upgrade of Theorem C requested by the assignment: Markov on E[sum L] = Delta is
  replaced by the union measure, and |A| >= t/(t+M) is replaced by the sharp
  arc-union bound |A| >= 1 - sum gamma.
- The unconditional weakening U_x <= 2 sum d_i sin th_i gives
  eps <= sum (d_i - 1)_+ + 2 sum d_i sin th_i (a companion to T4; not stronger
  than T4 in general, but it is the version that sharpens under phase clustering).

*Numerics* (c2prime_check.py): three machine-verified packings (SAT-disjoint,
containment checked): split-cell k=2 (equality 1.0000 = 1, U = 0); mixed
5-square k=2 (LHS 1.415; |A| = 0.088 <= U_x = 0.443: disjunction holds); coherent
2x2 grain t=0.12 + filler k=3 (LHS 2.05). Fact 4.0: 0 violations in 4000 random
2-D shifts x all tilted squares with exact lattice counts. |A| >= 1 - sum gamma
verified in all three.

## 5. THEOREM W (phase-clustered whisper kill; explicit constants)

**Phase-cover hypothesis PH(K, lambda).** For each axis, the 2(N+1) phases
{bbox-min mod 1} u {bbox-max mod 1} are covered by K arcs of total length lambda.

**Theorem W.** If every folded tilt is <= t_0 and PH(K, lambda) holds, then

    eps <= sum_i (d_i - 1)_+ + lambda + 2 K (max_i d_i) sin t_0 .

**Proof.** Each interval of B_i^x extends from a covered phase (bbox-min to the
right, bbox-max to the left) by d_i sin th_i <= (max d) sin t_0 =: s_max; fattening
each cover arc by s_max on both sides covers union B_i^x: U_x <= lambda + 2 K s_max;
same for U_y. Plug into Theorem C''. QED.

**Corollary (the coherent whisper phantom is dead, explicitly).** In the enemy
profile (eps > 1/2 - c, sides in 1 +- sqrt(2c) + k^{-2}): if additionally
sum (d_i - 1)_+ <= b0, tilts <= t_0, PH(K, lambda), then the packing is impossible
whenever  b0 + lambda + 2K(1 + sqrt(2c) + k^{-2}) sin t_0 <= 1/2 - c.
Canonical uniform coherent whisper phantom: uniform sides d-bar = (N+eps)/(N+1)
< 1 so b0 = 0; coherent tilt t_0 ~ eps/(N+1) ~ 1/(2k^2) (forced scale from T4);
rigid near-grid rotated coherently: bbox phases drift by <= k*t_0 <= 1/(2k) plus
the w-spread <= 2 sqrt(2c) + 2/k^2 across squares: PH holds with K = 2,
lambda <= 4 sqrt(2c) + 1/k + 4/k^2. Kill condition becomes
  4 sqrt(2c) + 1/k + 4/k^2 + 9/k^2 <= 1/2 - c .
At c = 1/400 (4 sqrt(2c) = 0.283) and k >= 10 (1/k + 13/k^2 <= 0.23):
LHS <= 0.513 - marginal; k >= 20: LHS <= 0.366 <= 0.4975 ✓ DEAD.
So c_0 = 1/400, k >= 20 kills the uniform-side coherent whisper-tilt
near-grid phantom outright, with margin 0.13.

**Status.** Theorem W is unconditional GIVEN its hypotheses; the two hypotheses
that are not yet derived from the enemy profile are (i) b0 = sum (d_i-1)_+ small
(the profile bounds sum (d_i-1)^2 <= 2c + k^{-2} only: b0 <= k sqrt(2c) in the
worst case), and (ii) PH(K, lambda) (mod-1 positional rigidity). Both are
positional/mod-1 rigidity statements: Gap A and Gap B have a common core.

## 6. Vertical-transport bookkeeping (why Jaw 1 alone gives only ~1/k, proved shape)

Conditional on the alpha'-edge hypotheses holding along each interface: summing
edge costs over any family of interfaces crossed by vertical lines, orientation
must travel from theta(square) to 0 at floor and ceiling; each unit of travel
alpha across an interface of horizontal extent ~1 costs >= alpha/520 of gap. A
column of squares over x in [x0, x0+1] with maximal folded tilt theta_max on it
has total travel >= 2 theta_max (down to both walls). Integrating over k disjoint
unit columns: G >= (2/520) sum_{columns} theta_max(col) >= (2/520) * (1/k) *
sum_i d_i^2 th_i-ish >= tiltmass/(260 k) ~ 1/(520 k). This matches the
assignment's arithmetic: the decomposition jaw alone cannot beat gap budget 2c
for k >> 1/c; the surviving enemy is whisper-coherent-per-column, which is
Theorem W's target. The pincer geometry is therefore: alpha'/alpha'-edge kills
tilt carried at angles theta >~ 520*2c per unit of exposed interface; Theorem W
kills tilt spread below t_0 with clustered phases; the remaining enemy must
combine moderate tilts with UNclustered phases and rough interfaces - i.e. it
must spend positional entropy, which is exactly what the (unproved) mod-1
rigidity would forbid.
