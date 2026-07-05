# F3 full derivations (one tilted square / grain vs AP sea)

Notation: T=[0,k]^2, N=k^2, n=N+1 squares S_i, sides d_i, tilt angles t_i (folded to [0,pi/4]),
c_i = cos t_i + sin t_i in [1, sqrt2]. G = T \ U S_i (gap), g = |G| = N - sum d_i^2,
s = sum (1-d_i)^2, e = g+s-1 (excess). Lambda_p = Z^2 + p, C(p) = sum_i #(S_i ∩ Lambda_p),
Av = {p in torus: C(p) = N}. Budget: C(p) <= N a.e. [verified, report §]. pi = projection
R^2 -> R^2/Z^2; for a set X ⊆ T, pi(X) = {p : Lambda_p ∩ X ≠ ∅}, |pi(X)| <= |X|,
with equality iff no two points of X differ by a nonzero integer vector ("X folds injectively").

## D1. Exact Av identity
For a.e. p: C(p) = #(Lambda_p ∩ T) - #(Lambda_p ∩ G) = N - hits(p). Hence
  Av = {hits = 0} = torus \ pi(G),   |Av| = 1 - |pi(G)|   (exact, any orientations).
Define foldloss(G) := g - |pi(G)| >= 0. Then
  s - |Av| = s - 1 + |pi(G)| = (g+s-1) - foldloss(G) = e - foldloss(G).
**FCMB(P) <=> foldloss(G) <= e.**  In particular FCMB => e >= 0 (the conjecture), and the
whole content of FCMB beyond the conjecture is an upper bound on gap self-overlap mod Z^2.

## D2. Inscribed-AP replacement (any number of tilted squares)
For a tilted square S (side d, tilt t, c = cos t + sin t), the concentric AP square S' of
side d' = d/c is contained in S: if |x|,|y| <= d/(2c) (center coords), then
|x cos t + y sin t| <= (d/2c)(cos t + sin t) = d/2, same for the other coordinate. (This is
the largest inscribed AP square; maximality is not needed below.)
P' := packing with every tilted square replaced by its inscribed AP square. P' is valid
(each S_i' ⊆ S_i). R := U_i (S_i \ S_i') (empty for AP squares). Then G' = G ⊔ R (disjoint),
|R| = sum_i d_i^2 (1 - 1/c_i^2).

## D3. Comparison identities (THEOREM, proved)
(i) C'(p) = C(p) - #(Lambda_p ∩ R) for a.e. p (the sets S_i', R, G partition T up to null sets).
(ii) Since C <= N a.e.: C'(p) = N  <=>  [C(p) = N and Lambda_p ∩ R = ∅]. Hence
     Av' = Av \ pi(R),   Av' ⊆ Av,   |Av| - |Av'| = |pi(R) ∩ Av| = |pi(R) \ pi(G)|.
(iii) Exchange identity (per replaced square, side d -> d' = d/c):
     (s' - s) + area(S\S') = [(1-d')^2 - (1-d)^2] + (d^2 - d'^2) = 2(d - d').
     [sympy-verified; also = the Structure Identity applied to both packings.]
(iv) Master equivalence:
     FCMB(P)  <=>  |Av'| <= s - |pi(R)\pi(G)|  <=>  slack_AP(P') >= (s'-s) + |pi(R)\pi(G)|,
     where slack_AP(Q) := s(Q) - |Av(Q)|. Always (s'-s) + |pi(R)\pi(G)| <= 2 sum_i (d_i - d_i').

## D4. Failure of the naive reduction (THEOREM, proved; assignment's check #1)
Plain AP-FCMB says only slack_AP(P') >= 0, so via D3 it yields
  |Av(P)| <= s(P) + 2 sum_i (d_i - d_i') = s + 2 sum_i d_i (1 - 1/c_i),
short of FCMB by exactly the perimeter defect 2 sum (d_i - d_i') > 0 for any true tilt.
Worse: for one square, Delta_s = s'-s = d(1-1/c)(2 - d(1+1/c)) > 0 whenever
d < 2c/(c+1) (and 2c/(c+1) > 1 for t>0, so all d <= 1 qualify). Since the route needs
slack_AP(P') >= Delta_s + |pi(R)\pi(G)| and plain AP-FCMB provides slack 0, the route fails
EVEN IF |pi(R)\pi(G)| = 0. No refinement of the corner-region bound can rescue it; a
slack-carrying AP statement is necessary. [sympy: excess = Delta_s + areaR = 2d(1-1/c), exact.]

## D5. Tilt-neutrality of capture measure (THEOREM, proved)
If S is a tilted square with no two points differing by a nonzero integer vector (e.g.
diam = d sqrt2 < 1, or S contained in an open unit cell), then |pi(S)| = d^2, independent
of t. Consequently, in any configuration where a square can be tilted about its center
without violating the packing (clearance) and where the Av-measure decomposes through
|pi(S)| alone (e.g. the cell-confined family of D6), |Av| is EXACTLY independent of t.
Numerics (700^2 grid): |Av| constant to 6e-4 across t in [0, pi/4].
COROLLARY. FCMB's tilt penalty is entirely a PACKING effect (tilted squares force side
shrinkage, raising s), never a capture-measure effect. Session-1's "tilting strictly
decreases |Av|" is an artifact of the forced shrinkage, not of the tilt.

## D6. Unconditional one-/two-tilt FCMB on the tightness manifold (THEOREM, proved)
Let P consist of N-1 axis-parallel UNIT squares occupying N-1 lattice cells of T, plus two
squares S_a, S_b (sides a, b, ARBITRARY orientations) with disjoint interiors contained in
the closed remaining cell Q (interiors in the open cell). Then
  |Av| = a^2 + b^2  and  s - |Av| = 2(1 - a - b) >= 0,
i.e. FCMB holds, with equality iff a + b = 1 (which forces the AP split-cell family).
Proof. (1) Each unit cell square contains exactly one point of Lambda_p for every p, so the
N-1 units contribute N-1 to C(p) for all p. (2) The open cell Q° contains exactly one point
q(p) of Lambda_p for a.e. p; S_a, S_b ⊆ Q, so S_a (resp. S_b) captures iff q(p) ∈ S_a
(resp. S_b), and since S_a, S_b are disjoint these events are disjoint. Hence
C = N-1 + 1_{q∈S_a} + 1_{q∈S_b} and Av = {q ∈ S_a} ⊔ {q ∈ S_b}, of measure a^2 + b^2
(cell-confined sets fold injectively: D5). (3) s = (N-1)*0 + (1-a)^2 + (1-b)^2, so
s - |Av| = 2 - 2a - 2b = 2(1-a-b). (4) a + b <= 1 is exactly the theorem f(2) = 1 (two
squares with disjoint interiors, any orientations, packed in a unit square have side-sum
<= 1) applied inside Q. QED
Remarks. (a) Covers the ENTIRE known tightness family of FCMB (split-cell) and all its
tilted deformations, with both small squares allowed to tilt. (b) Unconditional — does not
assume AP-FCMB. (c) Margin formula for the shrink-to-fit family (tilted square inscribed
in [0,a]^2 at angle t): sides (a/c, 1-a), margin 2a(1-1/c) — matches the 600^2-grid scan
to <=1.5e-3 at 24 (a,t) pairs.

## D7. Two-regime behavior of the corner term |pi(R)\pi(G)| (numerics)
Family A (tilted split-cell; gap confined to one cell): pi(R) ∩ pi(G) = ∅ exactly (R and G
are disjoint subsets of one cell; cell-confined folding is injective), so the corner term
is maximal, = |R|; the requirement in D3(iv) is met because P' inherits side-sum deficit:
here the shrink is a/c -> a/c^2, so (s'-s)+|R| = 2(a/c - a/c^2) while slack_AP(P') =
2(1 - a/c^2 - b) = 2(a - a/c^2); the requirement reads a >= a/c, strict for t>0.
Family B (two congruent near-unit squares at integer offset (1,0); folding gap): measured
pi(R) ⊆ pi(G) (corner term = 0, savings = |pi(R)| entire): the folded gap absorbs the
corner regions completely; the requirement reduces to slack_AP(P') >= Delta_s, supplied by
the foldloss slack e - foldloss > Delta_s.
Interpretation: the two loss sources of the reduction (corner term; Delta_s) are covered by
the two slack sources of AP packings (side-sum deficit; gap folding absorption), and in the
tested families each is separately sufficient. No configuration was found where both slacks
vanish while a true tilt is present — consistent with (but not proving) one-tilt FCMB.

## D8. Grain corollary
D2-D4 never use the number of tilted squares nor one-point capture (they hold for any d_i,
any m-point captures, via the budget C <= N only). For a coherent m x m grain at tilt t:
P' inscribes all m^2 squares, total perimeter defect 2(1-1/c) * sum_grain d_i, and D3(iv)
is verbatim the reduction target. The capture-measure formula mu(t,m) =
(1-(m-1) sin 2t)_+^2/(1+sin 2t) is NOT needed for the reduction; it quantifies the joint
capture event only if one attacks Av through capture events rather than through pi(G).

## D9. What is NOT delivered (GAPS)
GAP-1: One-tilt FCMB for a general (soft, non-unit) AP sea. Needs a slack-carrying AP-FCMB:
  slack_AP(Q) >= (s'-s) + |pi(R)\pi(G)| for shrunk packings Q = P'. By D1 this equals
  foldloss(G_P) <= e(P) — i.e. it is FCMB(P) itself rewritten; the reduction is an exact
  change of coordinates, not a strict decrease of difficulty. Its value: it isolates WHERE
  slack must come from (D7) and shows plain AP-FCMB is provably insufficient (D4).
GAP-2: folded footprint |pi(S)| of a tilted square with bounding width w = dc > 1 (integer
  self-overlap of one tilted square): not derived; not needed for D1-D8 (all delivered
  statements confine tilted squares to diam < 1 or use pi(G) only).
GAP-3: no unconditional theorem when the sea squares are non-unit (sides in (1-eps,1)):
  the D6 argument breaks because sea squares no longer capture with probability 1.
  Expected route: F1's AP machinery + D3 corner accounting.

## Code
algebra_check.py (sympy, D4), rig.py (600^2-800^2 torus grid engine), famA.py, famBC.py,
tests2.py — all in this directory; all runs green as reported.
