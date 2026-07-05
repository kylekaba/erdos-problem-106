# G3 derivations — BRIDGE (I): the incoherence charging scheme

Session 3, assignment G3. Notation as in ERDOS_106_REPORT.md. Machine checks:
`g3_checks.py` in this directory (all assertions pass; outputs quoted in §9).

Imported verified tools:
- **alpha'-edge [V, corrected]** (F5 Claim 2 + verifier sv_V3 fixes): S* with side
  d* in [1-eta, 1+eta], eta <= 1/20, folded mismatch alpha to a reference
  orientation gamma with tan alpha >= 2 tan phi0; e an edge of S*;
  R_e := {p : dist(p, e) <= h = 1/4, p on the outward side of aff(e)}; if every
  packing square other than S* whose interior meets R_e has folded tilt <= phi0
  in the gamma-frame, and R_e lies in T, then
      |R_e \ packing| >= (1/240) min(tan alpha - tan phi0, 1/3).
  (Shallow edges; for a steep edge rotate the gamma-frame by pi/2 — folded
  quantities invariant. Verified components reused below: the separating-line
  uniform below/above dichotomy, the argmin re-anchoring with two-sided growth
  >= tau_1, the bathtub bound, the corrected crest count with poke zones.)
- Lemma alpha' [V] (half-plane version, 1/60 sharpened) — not used directly, but
  its Steps 1–5 are the template.
- Wall Lemma [V], crystallization law [V] — context only.

Elementary facts used throughout (machine-checked on grids, §9):
(T1) tan(2x) >= 2 tan x on [0, pi/4);  (T2) tan a - tan b >= a - b for
0 <= b <= a <= pi/4;  (T3) 2/tau - tau >= 1 on (0, 1].

Folded circle: orientations live in Theta := R/(pi/2)Z with metric
dist_f(x, y) <= pi/4. "Folded tilt" of S = dist_f(beta_S, 0). For a finite
nonempty set B of orientations, its minimal covering arc A(B) exists and has
length < pi/2; write gamma(B) = midpoint, phi0(B) = half-length (< pi/4).

Throughout: PACKING HYPOTHESIS (H): squares S_1..S_{N+1} with pairwise disjoint
interiors in T = [0,k]^2, all sides in [1-eta, 1+eta], eta <= 1/20.
(§6 explains how the enemy profile G+V <= 2c delivers (H) minus at most one
outlier square, which is routed to an exceptional set.)

---

## 1. LEMMA E (frame-optimized strip payment, interior edges). PROVED.

**Definitions.** For an ordered edge (S, e) (S a packing square, e one of its 4
edges): R_e := {p not in S : dist(p, e) <= 1/4, p strictly on the outward side
of aff(e)} (segment distance; end caps included). Occ(e) := {W != S : int(W)
meets R_e}. If Occ(e) is nonempty: A(e) := minimal covering arc of
{beta_W : W in Occ(e)}, gamma(e) its midpoint, phi0(e) its half-length,
alpha(e) := dist_f(beta_S, gamma(e)).

**Lemma E.** Assume (H), R_e contained in T.
(a) If Occ(e) is empty: |R_e \ packing| = |R_e| >= 0.2375.
(b) If Occ(e) nonempty and tan alpha(e) >= 2 tan phi0(e):
    |R_e \ packing| >= (1/240) * min( tan alpha(e) - tan phi0(e), 1/3 ).

*Proof.* (a) Any square covering a point of R_e has interior meeting R_e (up to
null sets), so would be in Occ(e); S itself is (interior-)disjoint from R_e
since S lies on the inward closed side of aff(e). |R_e| >= |e| * h >= 0.95/4.
(b) This is exactly alpha'-edge with reference orientation gamma := gamma(e):
every W in Occ(e) has dist_f(beta_W, gamma) <= phi0(e) (definition of the
minimal arc), i.e. folded tilt <= phi0(e) in the gamma-frame; S has folded
mismatch alpha(e) to gamma; tan alpha >= 2 tan phi0 is the hypothesis; squares
not in Occ(e) never meet R_e so the "only phi0-tilted squares meet the strip"
hypothesis holds verbatim; R_e in T replaces dist(S, dT) >= h (that is the only
use of the original standoff hypothesis: uncovered strip must be genuine gap).
If e is steep in the gamma-frame, rotate by pi/2. QED

**Angle form.** If alpha >= 2 phi0 then tan alpha >= tan(2 phi0) >= 2 tan phi0
by (T1) and monotonicity (alpha <= pi/4 forces phi0 <= pi/8 < pi/4), and
tan alpha - tan phi0 >= alpha - phi0 >= alpha - 2 phi0 by (T2). Hence (b) gives
    |R_e \ packing| >= (1/240) * min( (alpha(e) - 2 phi0(e))_+ , 1/3 )
whenever alpha(e) >= 2 phi0(e).

---

## 2. LEMMA E-wall (the wall as a zero-orientation occupant). PROVED
(one bookkeeping constant re-derived; machine-optimized).

**Setting.** Same as Lemma E but R_e is NOT contained in T, and R_e \ T
touches only ONE side of dT (say the floor {y = 0}; all four walls are folded-
orientation 0). Occ(e) := {W != S : int(W) meets R_e ∩ T}.
A_w(e) := minimal covering arc of {0} ∪ {beta_W : W in Occ(e)} — the wall
enters the occupant set with orientation 0. gamma, phi0, alpha as before.

**Lemma E-wall.** Assume (H). If tan alpha(e) >= 2 tan phi0(e), then
    |(R_e ∩ T) \ packing| >= (1/252) * min( tan alpha(e) - tan phi0(e), 1/3 ).

*Proof.* Re-run the alpha'-edge proof in the gamma-frame with the floor
adjoined as one extra covering envelope.
- Step 1 (vertical accounting): the uncovered segment at abscissa x in the
  window [0, X_e] becomes {x} x ( max(F(x), T_fl(x), l(x) - h), l(x) ), where
  T_fl is the floor line in the gamma-frame. It lies in R_e ∩ T (above the
  floor; inside the strip; R_e exits only through the floor) and is uncovered.
- Step 2 for the floor: the floor is a single infinite edge of folded slope
  dist_f(0, gamma) <= phi0 in the gamma-frame (0 is in A_w). D_fl(x) :=
  l(x) - T_fl(x) has D_fl' = tau - s with |s| <= tan phi0, so D_fl' >= tau_1 :=
  tan alpha - tan phi0 > 0: monotone increasing; and D_fl >= 0 on the window
  because e lies in T (every point of e is on or above the floor and e's line
  coincides with e over its span). Anchoring at the left window end gives
  D_fl(x) >= tau_1 |x - a_fl|, the same envelope inequality as for squares.
- Step 3 (bathtub): the floor's crest interval has length <= X_e <= 1.06, and
  2h/1.06 = 0.47 >= 1/3, so tau_2 = min(tau_1, 1/3) is unchanged; square crests
  are unchanged.
- Step 4 (crest count): J <= (verifier's corrected count) + 1 for the floor:
  J <= [(X_e + 2.98) * 3.23 + 2*1.49*2.98]/0.9025 + 1 <= 23.76 at X_e = 0.63.
- Step 5 (assembly): lambda-dichotomy optimized numerically over
  X_e in [0.63, 1.06] (g3_checks.py): worst constant 1/243.8; we state 1/252.
QED

*Corner exclusion.* If R_e \ T touches two walls, (S, e) is put in the
exceptional set E_exc (§5). Count: a square within 1/4 of two walls lies with
its whole body in the quarter-disk B(corner, 1/4 + 1.49); area/0.9025 gives at
most 2 such squares per corner, at most 2 charged edges each: |E_exc| <= 16.

---

## 3. LEMMA E-narrow (mid-span localization; kills cap contamination). PROVED.

Motivation (see §7–§8): in Lemma E the occupant set of the FULL strip includes
squares near the endpoints of e (lateral and diagonal neighbors), whose
orientations are often close to beta_S; they drag gamma(e) toward beta_S and
kill the payment even at genuinely mismatched interfaces (the +-theta
checkerboard, gradient rows). Trimming the strip to the mid-span of e removes
them whenever the interface is "facing-clean".

**Definitions.** Parameters rho' := 0.22 (arclength trim), h' := 1/8.
e' := the closed sub-segment of e at arclength distance >= rho' from both
endpoints (length d* - 0.44 >= 0.51). R'_e := {p not in S : dist(p, e') <= h',
p strictly on the outward side of aff(e)}. Occ'(e), A'(e), gamma', phi0',
alpha' defined from R'_e exactly as in §1. (Frame-free definitions: no
circularity — the gamma'-frame is chosen AFTER Occ' is read off.)

**Lemma E-narrow.** Assume (H), R'_e contained in T, Occ'(e) nonempty,
tan alpha'(e) >= 2 tan phi0'(e). Then
    |R'_e \ packing| >= (1/650) * min( tan alpha'(e) - tan phi0'(e), 1/3 ),
and if moreover alpha'(e) <= 0.30,
    |R'_e \ packing| >= (1/300) * ( tan alpha'(e) - tan phi0'(e) ).
(If Occ'(e) is empty, |R'_e \ packing| = |R'_e| >= 0.51/8 = 0.06375.)

*Proof.* Re-run alpha'-edge in the gamma'-frame with strip height h' and window
W := x-extent of e' = [r_x, X_e - r_x], r_x = rho' cos alpha', X_e = d* cos
alpha'; window length X' = (d* - 0.44) cos alpha' in [0.36, 0.61]
(d* in [0.95, 1.05], alpha' <= pi/4).
- Step 1: for x in W the uncovered segment {x} x (max(F(x), l(x) - h'), l(x))
  lies within vertical distance h' of the point (x, l(x)) of e', hence in R'_e;
  any square covering one of its points has interior meeting R'_e, i.e. is in
  Occ'(e) — the tilt hypothesis is only ever used on Occ'(e). Squares spanning
  x with tops below l - h' only push the integrand to its cap h'.
- Step 2: unchanged (separating-line dichotomy holds on e's FULL span for every
  W with interior disjoint from S: below-type have T_W <= l on span(e) ∩
  span(W); above-type never cover points below l over span(e); argmin
  re-anchoring on the window with two-sided growth >= tau_1 = tan alpha' -
  tan phi0', using (T3) for the psi < 0 left branch).
- Step 3 (bathtub): crest intervals lie in W, so m_j <= X' <= 0.61 and
  2h'/X' >= 0.25/0.61 = 0.41 >= 1/3: tau_2 >= min(tau_1, 1/3) as before.
- Step 4 (crest count, the only step with new constants): a crest square W has
  a witness point in R'_e; every point of W satisfies
  x'' in [r_x - 1.49, X_e - r_x + 1.49] and y'' > l(x'') - (h' + 1.49 + 1.49 tau);
  below-type containment T_W <= l holds on e's FULL span [0, X_e], so above-l
  excursions (height <= 2.98) are confined to the two poke zones of width
  (1.49 - r_x) outside the span. Region area <=
  (X' + 2.98)(h' + 1.49 + 1.49 tau) + 2 (1.49 - r_x) * 2.98;  J <= area/0.9025.
- Step 5: lambda-dichotomy, optimized numerically over d* in [0.95, 1.05] and
  alpha' in [0, pi/4] (g3_checks.py): worst constant 1/639.8 (uniform) and
  1/287.9 (alpha' <= 0.30, where tau <= 0.31 also shrinks the crest band and
  the cap 1/3 never binds). Stated: 1/650 and 1/300. QED

**Corollary F (clean facing interfaces pay).** Assume (H). Call (S, e, W) a
*clean facing interface* if int(W) meets R'_e and no third square's interior
meets R'_e (then Occ' = {W}, phi0' = 0, alpha' = m(S, W) := dist_f(beta_S,
beta_W), and tan alpha' >= 0 = 2 tan phi0' holds automatically whenever
m(S, W) > 0). Then, if R'_e is in T:
    |R'_e \ packing| >= (1/650) min( tan m(S, W), 1/3 ),
and (1/300) tan m(S, W) >= m(S, W)/300 when m(S, W) <= 0.30.
This is the pairwise-mismatch payment that the full-strip scheme cannot see;
it charges the +-theta checkerboard (§8, machine-verified with 77x slack).

---

## 4. MULTIPLICITY LEMMA. PROVED.

**Lemma M.** Assume (H). Every point p of T lying in no square lies in R_e (a
fortiori R'_e, which is a subset of R_e) for at most 20 ordered edges (S, e).

*Proof.* p in R_e forces dist(p, S) <= dist(p, e) <= 1/4. Each such S is
contained in B(p, 1/4 + sqrt2 * 1.05) = B(p, 1.735) and the squares have
pairwise disjoint interiors of area >= 0.9025: their number m satisfies
0.9025 m <= pi * 1.735^2 = 9.457, so m <= 10. For a fixed S, the outward open
half-planes of an opposite edge pair are separated by a slab of width
d* >= 0.95 > 0, hence disjoint: p is on the outward side of at most one edge
from each pair, i.e. at most 2 edges of S. Total <= 10 * 2 = 20. QED

(Measured on the checkerboard test: max multiplicity 6 — the bound is lax but
costs only a constant.)

---

## 5. THEOREM I (the charging-scheme theorem). PROVED.

**Definitions.** Assume (H). E := all ordered edges (S, e) whose strip R_e
exits T through at most one wall; E_exc := the rest (|E_exc| <= 16, §2).
For e in E define the *incoherence credit*
    pi(e) := 1/3                                   if Occ(e) = empty (interior e);
    pi(e) := min( tan alpha(e) - tan phi0(e), 1/3 )  if tan alpha(e) >= 2 tan phi0(e);
    pi(e) := 0                                     otherwise,
where for interior edges (R_e in T) the arc A(e) is built from Occ(e), and for
single-wall edges it is A_w(e) (the wall adjoined as orientation 0, §2). The
*total (paid) incoherence* of the packing is  I := sum_{e in E} pi(e).

> **Theorem I.** Every packing satisfying (H) has
>     G >= I / 5040 .
> In the angle form, with I_ang := sum_{e in E} min( (alpha(e) - 2 phi0(e))_+, 1/3 )
> (same arcs; credit 1/3 for empty interior strips):  G >= I_ang / 5040.

*Proof.* By Lemmas E, E-wall and the empty case, each e in E pays
|R_e ∩ T \ packing| >= pi(e)/252 (240 <= 252 for interior; 0.2375 >=
(1/252)(1/3) for empty). Summing and applying Lemma M (each gap point charged
<= 20 times):
    20 G >= sum_{e in E} |R_e ∩ T \ packing| >= (1/252) I.
The angle form follows from pi(e) >= min((alpha - 2 phi0)_+, 1/3) when
alpha >= 2 phi0 (§1 angle form) and from alpha >= 2 phi0 implying the tan
condition (T1). QED

> **Theorem I-narrow.** With pi'(e) defined identically from the narrow strips
> (rho' = 0.22, h' = 1/8; interior only: R'_e in T; empty-strip credit 1/3
> backed by 0.06375 >= (1/650)(1/3)), and I' := sum pi'(e):
>     G >= I' / 13000 ,
> and restricted to edges with alpha'(e) <= 0.30 (no cap):
>     G >= (1/6000) * sum_{those e} ( tan alpha'(e) - tan phi0'(e) ).

*Proof.* Identical: per-edge >= pi'(e)/650 (resp. /300), R'_e subset of R_e so
Lemma M applies unchanged; 650 * 20 = 13000, 300 * 20 = 6000. QED

*Remark (using both).* R'_e is a subset of R_e, so the same gap can back both
credits; the safe combined statement is G >= max(I/5040, I'/13000).

---

## 6. COROLLARY H (the enemy handoff — what Bridge (I) delivers to (II)).

Enemy profile: eps > 1/2 - c, so G <= G + V <= 2c (budget identity [V]), and
sum_i (d_i - 1)^2 = V + (N+1)(dbar - 1)^2 <= 2c + 1/(N+1).

*(H)-repair.* If c <= 1/800 and k >= 21, at most ONE square ("outlier") can
have |d_i - 1| > 1/20 (since (d_i - 1)^2 <= 2c + 1/(N+1) <= 0.0025 + 0.0023
allows |d_i - 1| <= 0.0693, and two outliers would need sum (d-1)^2 >= 2 *
0.0025 > 2c + 1/(N+1) for k >= 21... at c = 1/800, k >= 30 exactly:
2*(0.05)^2 = 0.005 > 0.0025 + 1/901 = 0.00361 — one outlier only; for smaller
c none). Every side is <= 1 + 0.07 <= 1.07; the outlier W contaminates the
edges of squares within 1/4 of it: at most (4 * 1.07 * 1.735 + pi * 1.735^2)/
0.9025 <= 19 squares, <= 2 edges each, plus W's own 4: |E_O| <= 42.
All uncontaminated edges satisfy (H) with eta = 0.07 — NOTE: alpha'-edge
requires eta <= 1/20 = 0.05, so strictly the scheme needs
    c <= 1/1000 and k >= 32  ==>  all sides in [0.95, 1.05] except <= 1 outlier
(then 2c + 1/(N+1) <= 0.002 + 0.00098 < 2 * 0.0025). Under that regime:

> **Corollary H.** For any enemy packing (eps > 1/2 - c) with c <= 1/1000,
> k >= 32, and E* := E \ (E_exc ∪ E_O) (|E_exc ∪ E_O| <= 58):
> (a) I(E*) <= 5040 * 2c = 10080 c   and   I'(E*) <= 26000 c.
> (b) For every xi in (0, 1/3]:
>     #{ e in E* : alpha(e) >= 2 phi0(e) + xi } <= 10080 c / min(xi, 1/3).
> (c) For every Delta in (0, 0.30]:
>     #{ clean facing interfaces in E* with mismatch m >= Delta }
>        <= 6000 * 2c / tan Delta <= 12000 c / Delta.
> (d) Consequently the enemy is STRIP-COHERENT except on a bounded set:
>     all but <= 30240 c + 58 ordered edges have alpha(e) < 2 phi0(e) + 1/3,
>     and all but <= 12000 c/Delta + 58 clean facing pairs have mismatch < Delta.

At c = 1/1000: (b) with xi = 1/3 gives <= 31 strongly torn strips out of
~4k^2; (c) with Delta = 0.1 gives <= 120 torn clean facing interfaces out of
~2k^2 — for k >= 35 this is < 1% of interfaces. **This is the quantitative
content of "incoherence pays gap": on an enemy, orientation mismatch above
twice the local spread is confined to O(c) many edges.**

*Interface handed to G4/G2 (stated exactly):* my I controls (i) per-strip
excess alpha - 2 phi0 (arc-center mismatch above occupant spread), full-strip
and mid-strip versions; (ii) pairwise mismatch across intruder-free mid-strip
interfaces; (iii) wall edges with the wall counted as an orientation-0
occupant (so a square of tilt theta whose strip reaches a wall through
phi0-coherent company pays min(tan theta - tan phi0, 1/3)/252 — Route B's wall
anchoring in charging form). My I does NOT control: (iv) spread within strips
(phi0 itself is free); (v) mismatch at intruded/rough interfaces; (vi) any
mod-1 phase data. The (II)-side must therefore consume coherence in the form
"per-strip / per-facing-pair mismatch small off an O(c)-size exceptional set",
NOT "global orientation within a single arc" — drift over long chains remains
possible at zero I-cost (each hop coherent, total travel unbounded by I: see
Dead end 3).

---

## 7. THE SHIELDING RECURSION: what is proved, what is not.

**Lemma R (spread realization; trivial but structural).** If e in E has
alpha(e) < 2 phi0(e) (no payment) and |Occ(e)| >= 2, then two occupants
W1, W2 realize dist_f(beta_{W1}, beta_{W2}) = 2 phi0(e) > alpha(e), both
within 1/4 of S and within diam(R_e) <= |e| + 2h <= 1.55 of each other.
*Proof:* endpoints of the minimal arc are attained. QED
So an unpaid mismatch is always shielded by a LARGER mismatch between two
nearby squares — the assignment's triangle-inequality intuition, made exact.
The recursion this suggests does NOT terminate as stated: W1, W2 need not be
within 1/4 of each other (they can sit at opposite ends of the strip), so the
pair does not yield a new EDGE to recurse on. This is the precise point where
the naive shielding recursion fails.

**Lemma C (chain triangle inequality; trivial).** For any chain S_0, ..., S_r
with dist(S_{j-1}, S_j) <= 1/4 for all j:
sum_j m(S_{j-1}, S_j) >= dist_f(beta_{S_0}, beta_{S_r}); and if S_r is within
1/4 of a wall, sum_j m_j + tilt(S_r) >= tilt(S_0).
(Adjacency at range 1/4 is symmetric: dist(A, B) <= 1/4 iff B meets the
outward 1/4-collar of A, which is the union of A's four strips.)

**Proposition D (conditional descent; proved GIVEN clean chains).** Assume (H).
Suppose S_0 (folded tilt theta_0) admits a chain as in Lemma C reaching a wall
in which every link is a clean facing interface (Corollary F) with mismatch
<= 0.30, the last square's wall edge satisfies Lemma E-wall with phi0 = 0 and
its own tilt <= 0.30... (final link: tilt(S_r) paid by E-wall), and the strips
R'(link) are pairwise disjoint. Then
    G >= (1/300) * sum_j tan m_j + (1/252) tan tilt(S_r)
      >= (1/300) * theta_0 .
If the strips are not disjoint, divide by the multiplicity 20:
G >= theta_0/6000. With k disjoint such chains (one per unit column),
G >= (k/6000) * (average column max tilt) — the assignment's k-leverage.
*Proof:* Corollary F per link, Lemma E-wall at the base, Lemma C to lower-bound
the sum of mismatches by theta_0 (using tan m >= m). QED

**GAP-I (the honest open core of Bridge (I)).** Proposition D's hypothesis —
existence of clean facing chains — is NOT derived. Two failure modes:
(1) *Intruded interfaces:* a third square D meets R'_e between S and its
facing W. Then phi0' > 0 and the payment degrades by tan phi0'; if
beta_D is close to beta_S the payment dies entirely. Geometric content: D
shields S by PRESENTING S's own orientation to the sea one layer deeper —
the interface is postponed, not destroyed. Depth quantization (near-unit
squares: consecutive layers >= 0.51 apart) bounds the postponement chain by
2k hops, but "D is between S and the sea" is not a theorem: D can poke into
the strip from the side. Unproved.
(2) *Rough interfaces / spread shields:* Occ'(e) with genuinely mixed
orientations at all relevant edges (no clean sub-window). The needed statement
is a measurable "facing-function" version of E-narrow: with W(x) := the first
square hit outward from x in e', if |{x : m(S, W(x)) >= Delta}| >= L0 then the
strip pays c(Delta, L0). The obstruction is that alpha'-edge's Steps 2–3 need
one reference frame for all crests in the window; crests near beta_S break the
anchor bound precisely when they legitimately postpone (mode 1). The two
modes are the same phenomenon and both are Route B Dead End 5 (roughness
self-correction) in charging clothes. A future agent should attack the
two-scale version: split the window into maximal sub-windows by which half-arc
(within Delta/2 of beta_S, or not) the facing orientation lies in; E-narrow
pays on the mismatched sub-windows of length >= 0.36; postponed sub-windows
recurse downward with disjoint strips (depth-indexed, so no double charge);
the recursion depth is <= 2k but each level's payment is per-unit-length, so
the bill is X * min mismatch — this is exactly the gradient corollary's
accounting [V for straight rows], and ONLY the sub-window fragmentation
(losing the X' >= 0.36 window length) blocks it. Quantify the fragmentation:
sub-windows shorter than 0.36 have total length controlled by the number of
orientation sign-changes of the facing function along e', which is <= number
of distinct squares met <= 4 — so at most 4 * 0.36 = 1.44 of window length is
lost per edge... but e' has length <= 0.61: the count bound is vacuous.
Sharpen: each facing square occupies an x-interval (convexity), so the facing
function has <= 3 breakpoints on e' and >= one sub-window of length
>= X'/4 >= 0.09 survives; E-narrow with window 0.09 still pays (constant
~1/6500 by the same Step-5 arithmetic). This suggests GAP-I mode (2) is
CLOSEABLE for single-layer roughness; the genuinely open part is the
multi-layer postponement bookkeeping (mode 1). Flagged as the best next step.

**Why no unconditional descent theorem is claimed.** The +-theta checkerboard
shows pairwise mismatch alone (Sector-Lemma style) cannot be charged — §6.6 of
the report (pairwise charging impossibility). My scheme respects this: it
charges only strip-witnessed, spread-dominated mismatch. The diamond chain
(45-degree, internally coherent) has I = 0 through its interior — correct, its
cost is at the sea interface and at the walls, where E-wall charges it.

---

## 8. ADVERSARIAL TESTS (assignment: staircase, gradient, shielded grains).

1. **Axis-parallel staircase/running bond** (T12 tilings, deficient column):
   all orientations 0: every arc A(e) = {0}, alpha = 0: I = 0, Theorem I
   claims nothing. Correct behavior — these packings have G = 0 or tiny; their
   physics is phase drift, which belongs to (III)/G2, not to Bridge (I). No
   false positives (a theorem claiming G > 0 here would be FALSE — this test
   is why pi(e) must vanish at alpha = 0).
2. **Coherent grain in an axis-parallel sea** (tilt theta, boundary length B):
   boundary squares of the sea see occupant arcs {theta}-ish: alpha = theta,
   phi0 = 0: payment theta/240 per exposed edge — reproduces the alpha'-jaw,
   now without any half-plane hypothesis, per edge.
3. **Single-intermediate shield** (A at alpha, C at alpha/2, B at 0, stacked):
   interfaces A–C and C–B are clean facing with mismatch alpha/2 each:
   I' >= 2 * tan(alpha/2) - no dodge; matches the triangle-inequality
   prediction exactly.
4. **Spread shield in one strip** (occupants of A's strip at alpha/2 +- phi,
   phi > alpha/4): full-strip payment dies (alpha = alpha/2 < 2 phi0). Narrow
   strip: if one occupant faces the mid-span alone, Corollary F pays its
   pairwise mismatch; if both genuinely share the mid-span, phi0' = phi and
   payment survives iff alpha/2 >= 2 phi. The residue is GAP-I mode (2);
   single-layer version closeable (see §7).
5. **Gradient texture** (rows stepping by s_n, intra-row spread delta):
   full-strip Theorem I is BLIND (cap contamination by same-row lateral
   neighbors: A(e) stretches to beta_S, alpha ~ phi0). E-narrow pays per row
   interface when rows are height-aligned (lateral neighbors stay outside the
   mid-strip); staggered rough rows dodge E-narrow too — consistent with the
   known open residue (rough-line alpha'). Bridge (I) therefore does NOT
   supersede the gradient corollary (F5 Claim 3); they are complementary.
6. **+-theta checkerboard** (the texture that dodges full strips AND pairwise
   sector charging): machine-verified (g3_checks.py): 6x6 checkerboard,
   theta = 0.12, d = 0.898, SAT-disjoint; the mid-strip of an interior square's
   edge contains EXACTLY the facing neighbor (orientation -theta); Corollary F
   bound 0.00061 vs measured uncovered 0.047 — holds with 77x slack; strip
   multiplicity measured max 6 <= 20. On an enemy-scaled checkerboard the
   per-interface payment tan(2 theta)/300 over ~2k^2 interfaces forces
   G ~ k^2 theta >> 2c: checkerboards are DEAD as enemies for
   theta >= 450 c/k^2, i.e. down to whisper scale.
7. **k-leverage arithmetic** (assignment's self-check, re-derived): even with
   Proposition D's chains granted, k disjoint descent paths give
   G >= (k/6000) T*, so T* <= 12000 c/k; whisper tilts T* ~ 1/(2k^2) sit far
   below this: Bridge (I) can never kill the whisper enemy — its exact role is
   to force near-coherence (Corollary H) so that Bridge (II) (coherence =>
   phase clustering => Theorem W/S3) takes over. Confirmed: no contradiction,
   no overclaim.

---

## 9. MACHINE CHECK LOG (g3_checks.py, all PASS)

- tan(2x) >= 2 tan x on [0, pi/4): 200001-point grid, 0 violations.
- tan a - tan b >= a - b (0 <= b <= a <= pi/4): 5*10^5 random pairs, 0 viol.
- 2/tau - tau >= 1 on (0, 1]: grid, 0 violations.
- E-wall constant: worst over X_e in [0.63, 1.06], J+1 floor crest,
  lambda-optimized: 1/243.8 (stated 1/252).
- E-narrow constants (rho' = 0.22, h' = 1/8, d* in [0.95, 1.05]):
  uniform worst 1/639.8 (stated 1/650); alpha' <= 0.30 worst 1/287.9
  (stated 1/300). tau_2-cap side condition 2h'/X' >= 1/3 asserted throughout.
- Checkerboard: 36 squares, pairwise SAT-separating-axis disjoint; single
  facing occupant in mid-strip (orientation -0.12 exactly); uncovered area in
  R'_e = 0.0472 >= bound 0.00061 (ratio 77.2); multiplicity max 6.

Constants summary (all absolute, all explicit):
  full-strip per-edge: 1/240 interior [V-derived], 1/252 wall;
  mid-strip per-edge: 1/650 uniform, 1/300 for mismatch <= 0.30;
  multiplicity: 20;  Theorem I: 1/5040;  Theorem I-narrow: 1/13000 (1/6000
  small-mismatch);  handoff at c <= 1/1000, k >= 32: exceptional edges <= 58.
