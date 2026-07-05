# F4 derivations — localization lemma, FCMB refutation, no-repair theorem

Notation as in ERDOS_106_REPORT.md: T=[0,k]^2, N=k^2, n=N+1 squares S_i (closed,
pairwise disjoint interiors), U = union S_i, G = [0,k)^2 \ U, g=|G|, s=sum(1-d_i)^2,
C(p) = sum_i |S_i ∩ (Z^2+p)|, Av = {p in [0,1)^2 : C(p)=N}, V = {0..k-1}^2,
C_v = v+[0,1)^2 (cell), pi = folding map R^2 -> R^2/Z^2 realized on [0,1)^2.

## 1. Lemma L1 (cell localization) — PROVED

For v in V put A_v := (U ∩ C_v) - v ⊆ [0,1)^2. Then:

(i) For a.e. p in [0,1)^2:  C(p) = #{v in V : p ∈ A_v} = sum_{v in V} 1_{A_v}(p).

(ii) Av = ∩_{v in V} A_v up to a null set.

(iii) |A_v| = |U ∩ C_v| = 1 - γ_v where γ_v := |G ∩ C_v| (cell gap).

(iv) For every B ⊆ V:  |Av| ≤ |∩_{v∈B} A_v| = 1 - |pi(G ∩ C_B)|, C_B = ∪_{v∈B} C_v;
     at B=V: |Av| = 1 - |pi(G)|. The bound is non-increasing in B.

Hygiene/proof. (a) Points of Λ_p ∩ T not of the form p+v, v∈V, have a coordinate
exactly k, i.e. p has a zero coordinate: null in p. (b) For fixed v,i the set
{p : p+v ∈ ∂S_i} = (∂S_i - v) ∩ [0,1)^2 is null (∂S_i is a null set, Lebesgue is
translation invariant); union over the finitely many (v,i): null exceptional set E.
Off E each point p+v lies in the interior of at most one square (disjoint interiors)
and not on any boundary, so sum_i |S_i ∩ Λ_p| counts exactly the covered p+v once
each: C(p) = #{v : p+v ∈ U} = #{v : p ∈ A_v}. Since #V = N, C(p)=N iff p ∈ A_v for
all v: (ii). (iii) is translation invariance. (iv): the complement of ∩_{v∈B}A_v in
[0,1)^2 is ∪_{v∈B} ((G∩C_v) - v); since {C_v} partition [0,k)^2, this union is
exactly the image of G ∩ C_B under folding (up to the null set from overlapping
translates' boundaries — as a union of measurable sets its measure is
|pi(G∩C_B)| by definition of the folded image). Monotonicity is trivial. ∎

Corollary L2 (one-cell bound). |Av| ≤ 1 - max_v γ_v. Numerically verified (column
k=2: |A_v| = 2/3, 2/3, 1, 1; ∩ = 2/3 = |Av|; script fcmb_column_check.py).

Corollary L3 (Markov lower bound — two-sided frame). For EVERY packing,
|Av| ≥ 1 - g:  hits(p) := N - C(p) = #(Λ_p ∩ G) is a nonneg integer a.e. with
E[hits] = g (Fubini), so P(hits≥1) ≤ g, |Av| = 1 - P(hits≥1) ≥ 1-g. Equality iff
hits ∈ {0,1} a.e. So FCMB (|Av| ≤ s) always contained "1-g ≤ s", i.e. the
conjecture, per packing; for a hypothetical enemy (g+s<1) FCMB fails automatically
(|Av| ≥ 1-g > s). FCMB-for-enemies IS the conjecture; the surplus content of FCMB
lives on VALID packings only — and is refuted below.

## 2. THE COUNTEREXAMPLE: FCMB is false for every k ≥ 2 — PROVED + VERIFIED

Deficient-column packing P_k (axis-parallel): c := k/(k+1).
 - k+1 squares of side c at lower-left (0, r c), r = 0..k  (exactly tile
   [0,c]×[0,k] since (k+1)c = k);
 - (k-1)k unit squares tiling [1,k]×[0,k].
n = (k+1) + k^2 - k = k^2+1 = N+1. Valid: interiors disjoint, all inside T
(machine-verified by separating-axis test). Sum d = (k+1)c + k^2-k = N (extremal).
g = N - (k+1)c^2 - (k^2-k) = k - k^2/(k+1) = k/(k+1).  s = (k+1)(1-c)^2 = 1/(k+1).
g+s = 1: consistent with the Structure Identity 2Σd = 2N+1-g-s = 2N. Gap
G = [c,1]×[0,k], one vertical sliver of width w = 1/(k+1).

Capture: for a.e. p ∈ [0,1)^2 and v with v1 ≥ 1: p+v ∈ (1,k)×(0,k) ⊆ units ⇒
covered. For v1 = 0: p+v = (p1, p2+v2); the column covers [0,c]×[0,k] entirely, so
covered iff p1 < c, uncovered (in the sliver) iff p1 > c — simultaneously for all k
values of v2. Hence
   C(p) = N  ⟺  p1 < c,   |Av| = c = k/(k+1),
   hits(p) = k·1[p1 > c]  (two-point law {0,k}),  |pi(G)| = w = g/k  (k-fold fold).
FCMB demands |Av| ≤ s = 1/(k+1): violated by (k-1)/(k+1) → 1. At k=1, P_1 is the
a=b=1/2 split cell: equality (why k=1 proof + split-cell tightness gave no warning).

Numerics (fcmb_column_check.py, budget C ≤ N asserted, grids 700²–1200²):
 k=2: |Av| = 0.666667, s = 0.333333 (violation 0.333333); hits ∈ {0,2} at {2/3,1/3}
 k=3: |Av| = 0.750000, s = 0.250000 (violation 0.500000)
 k=4: |Av| = 0.800000, s = 0.200000 (violation 0.600000)
Harness validated on split-cell k=2 (a=0.37) and k=3 (a=0.5): |Av| = a²+b² = s to
6 decimals (known tight family reproduced exactly).

Robustness (violation is open, not a degenerate boundary artifact): tilt the k+1
column squares by t about their centers, shrink side to c/u1(t) (bounding boxes stay
in the c×c cells ⇒ disjoint; SAT-verified). These are STRICTLY sub-critical valid
packings (Σd < N, g+s > 1):
 k=2, t=0.02: s=0.35972, |Av|=0.62206 (violation 0.26234)
 k=2, t=0.05: s=0.39817, |Av|=0.56227 (violation 0.16411)
 k=3, t=0.02: s=0.27997, |Av|=0.68360 (violation 0.40363)
 k=3, t=0.05: s=0.32456, |Av|=0.59568 (violation 0.27112)
As t→0, (g,s,|Av|) → (2/3, 1/3, 2/3) at k=2 from the strict interior of the valid
region.

Also refuted by the same example (all were ≥-FCMB reformulations):
 - folded-gap form |pi(G)| ≥ 1-s  (here |pi(G)| = 1/(k+1), 1-s = k/(k+1));
 - AP empty-square-decomposition target Σ_i |∩_{j≠i} pi(S_j) \ pi(S_i)| ≤ s:
   the column squares' y-phases y_r = -r/(k+1) mod 1 are equidistributed at spacing
   1/(k+1); the omitted arcs (y_r+c, y_r+1) tile the circle, so the i-th term is
   exactly c·w for each of the k+1 column squares and 0 for units; the sum is
   (k+1)·c·w = k/(k+1) = |Av| (decomposition EXACT, bound false);
 - route-(E) target g + Σ_{v≠0}|G∩(G-v)| ≤ g²/(1-s): here the autocorrelation is
   R = Σ_{j=1}^{k-1} 2w(k-j) = wk(k-1) = (k-1)g, so LHS = kg, RHS = g (since
   1-s = k/(k+1) = c and g²/(1-s) = g·(k/(k+1))/c = g). LHS/RHS = k.

## 3. Triage of route (E) and all gap-mass routes — PROVED

(a) If the route-(E) condition g + R ≤ g²/(1-s) holds (R ≥ 0), then g ≤ g²/(1-s),
i.e. g ≥ 1-s: the condition already contains the conjecture's conclusion for that
packing. It is unsatisfiable on the entire enemy region g+s<1. Route (E) can never
carry conjecture content; at best it certifies the FCMB surplus on valid packings —
and §2 shows that surplus is false. Same computation kills the Bonferroni/integer
support bound |pi(G)| ≥ g - R (needs R ≤ g+s-1 ≤ 0 on enemies).

(b) General principle. Any chain of the form |Av| ≤ 1 - h with h a lower bound for
|pi(G∩W)| for some W ⊆ T (second moment, Bonferroni, block localization,
Kneser/Macbeath-type sumset or support bounds — any "gap-mass" argument) has
h ≤ |G| = g, hence cannot prove |Av| ≤ s for an enemy (which needs h ≥ 1-s > g).
All conjecture-content must come from the capture/geometry side, never from
measure-mass accounting of the gap. (This was provable before the counterexample;
the counterexample additionally shows the target itself was false.)

(c) Fold cap. Any TRUE bound |pi(G)| ≥ h(s) valid for all packings must satisfy
h(1/(k+1)) ≤ 1/(k+1) (column), i.e. asymptotically h(s) ≤ s ~ (1-s)/k·(k+1)s...
concretely at the column points h(s) ≤ s = (1-s)/k: any s-only lower bound on the
folded gap yields at best g ≥ (1-s)/k — a factor k off the conjecture.

## 4. Exact overlap identity and the no-repair theorem

Identity (proved): with Φ(p) = hits(p) = Σ_{v∈Z²} 1_G(p+v),
   |Av| = 1 - |pi(G)| = 1 - g + E[(Φ-1)_+],
since |pi(G)| = |{Φ≥1}| and g = E[Φ] = |{Φ≥1}| + E[(Φ-1)_+]. Hence
   FCMB ⟺ E[(Φ-1)_+] ≤ g+s-1  ("folding overlap ≤ extremality slack").
Column: overlap = g - g/k = (k-1)/(k+1), slack = 0. So the overlap can exceed the
slack by an amount → 1 ON EXTREMAL packings; no correction term vanishing at
extremality can repair FCMB.

No-repair theorem (for the (g,s)-frame). There is no F : R²→R such that
 (i) |Av| ≤ F(g,s) for every valid packing (every k, n=N+1),
 (ii) F(g,s) < 1-g whenever g+s < 1 (what the Theorem-D contradiction needs), and
 (iii) F is continuous at (2/3, 1/3) (equivalently at any accumulation point
      (k/(k+1)·(1+o(1)), 1/(k+1)·(1+o(1))) of the tilted-column family).
Proof. The tilted columns P_2(t), t→0+, are valid with (g,s) → (2/3,1/3) and
|Av| → 2/3 (numerics above; |Av| ≥ 0.62 already at t=0.02). By (i) and (iii),
F(2/3,1/3) ≥ 2/3. By (ii), for enemy-side points (g,s)→(2/3,1/3) with g+s<1,
F < 1-g → 1/3. So F jumps by ≥ 1/3 across g+s=1 at (2/3,1/3); with P_k(t) the
forced jump at (k/(k+1), 1/(k+1)) is ≥ 1 - 2/(k+1) → 1. Any conjecture-closing
"measure inequality in (g,s)" must be discontinuous with jump → 1 exactly on the
extremal surface — i.e. it must already encode the conjecture. The repaired target
must use finer data than (g, s): per-direction fold multiplicities, ε explicitly,
or capture-side rigidity. ∎

## 5. Two-cell lemma / "repetition charges s" — FALSE as a local statement

For adjacent v, v' = v+u: |A_v ∩ A_{v'}| = 1 - γ_v - γ_{v'} + ov, with
ov = |G ∩ (G-u) ∩ C_v| (exact inclusion-exclusion). The hoped-for local charging
"ov ≤ h(local deficits)" fails: in the column, for vertically adjacent cells,
ov = w = 1/(k+1), while the squares meeting the two cells carry deficit
≤ 3(1-c)² = 3/(k+1)²: ratio (k+1)/3 → ∞. In-phase repetition is paid for by the
deficit of the WHOLE repeated chain, not locally — and even globally the exchange
rate is quadratic (k-fold repetition of a width-w sliver costs only (k+1)w²),
which is exactly why FCMB dies.

## 6. Dislocation heuristic — refuted as stated

P_k is a bona fide dislocation (one extra square in one column). Its phase drift is
w per cell ALONG the column (y-direction), and it resonates: (k+1) steps = full
cycle, the square-phases equidistribute (three-distance at rational rotation
1/(k+1)). But the gap sliver's folding direction is also y while its phase is
constant in x: drift spreads pi(G) only in the drift direction, and a gap sliver
PARALLEL to the drift is immune. Equidistribution of square phases here works
AGAINST capture-avoidance spread: every torus point is missed by exactly one
column square's footprint, which is what makes Av large (= c) instead of small.

## 7. What survives (capture-side residue)

 - Lemma L1/L2/L3 (this file) — unconditional bookkeeping, now the correct frame.
 - Markov lower bound |Av| ≥ 1-g: an enemy MUST have a full-capture set of measure
   > s — large, not small. The conjecture = "no packing has |Av| > s AND g < 1-s
   simultaneously with ..." — the productive contradiction is now on the capture
   side:
 - AP row-chord rigidity (from p1 report, still valid): pointwise on Av the N
   capturing squares satisfy Σ' d_i ≤ N (k disjoint full-width chords per row line),
   hence the empty square of every full-capture shift of an enemy has
   d_{i0(p)} ≥ ε := Σd - N. Two-sided squeeze target: enemy needs
   |∪_{i : d_i ≥ ε} Av_i| ≥ 1-g with Av_i ⊆ {S_i captures nothing} of measure
   1 - |pi(S_i)|, and the capturing-N structure forces near-grid rigidity. This —
   not gap-mass — is where FCMB's successor should be built.
