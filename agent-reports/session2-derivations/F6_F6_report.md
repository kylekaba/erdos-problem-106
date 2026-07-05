# F6 (wildcard transfer) — FULL REPORT: FCMB IS FALSE for every k ≥ 2

Code: `refute_fcmb.py` (this directory). Grid 1200², controls tight to 1e-4.

## The counterexample (deficient-column family)

U_k(a_1..a_{k+1}), a_j ∈ (0,1], Σa_j = k:
- (k−1)k unit squares [i,i+1]×[j,j+1], 0 ≤ i ≤ k−2, 0 ≤ j ≤ k−1;
- k+1 squares S'_j = [k−1, k−1+a_j] × [h_{j−1}, h_j], h_j = a_1+…+a_j, in the last column strip.

n = k(k−1)+(k+1) = k²+1 = N+1. Σd = k(k−1)+k = N exactly. Valid packing (disjoint, inside [0,k]²).

**Lemma F6.1 (extremal manifold).** g+s = 1 for EVERY member:
g = k² − k(k−1) − Σa_j² = k − Σa_j²; s = Σ(1−a_j)² = (k+1) − 2k + Σa_j² = 1 − k + Σa_j²; sum = 1. ∎
A k-dimensional manifold of equality cases of the conjecture (g+s ≥ 1), containing the split-cell
family (a = (1,…,1,a,b)) as a face and reaching gap area g up to k/(k+1). NEW: extremal packings
with large positive gap (previous catalogue: tilings g=0, and split-cells g=2ab ≤ 1/2).

**Lemma F6.2 (exact FCMB defect = folding overlap).** Gap pieces P_j = [k−1+a_j, k]×[h_{j−1},h_j]
(width δ_j = 1−a_j ≤ 1, height a_j ≤ 1 ⇒ π injective on each piece). Σ|P_j| = Σδ_j(1−δ_j)
= Σδ_j − Σδ_j² = 1 − s (since Σδ_j = 1). Hence
   |Av| − s = (1 − |π(G)|) − s = Σ_j |π(P_j)| − |∪_j π(P_j)| ≥ 0,
with equality iff the folded pieces are a.e. disjoint mod Z². So on the whole family REVERSE FCMB
holds, FCMB holds only on the overlap-free stratum (e.g. split-cells), and any folding overlap is
a strict FCMB violation. Overlap is generic. ∎

**Theorem F6.3 (FCMB refuted).** Equal split a_j = k/(k+1): the k+1 gap pieces stack into the
single strip [k−1+d, k]×[0,k], d = k/(k+1); π(G) = [d,1)×S¹, |π(G)| = 1/(k+1);
   |Av| = k/(k+1),  s = 1/(k+1),  |Av| − s = (k−1)/(k+1) → 1,  |Av|/s = k → ∞.
FCMB (ERDOS_106_REPORT.md §7A central conjecture) is false for every k ≥ 2, by an axis-parallel,
fully explicit, 5-square (k=2) example: 2 units + three 2/3-squares stacked in [1,5/3]×[0,2];
|Av| = 2/3 > 1/3 = s. Verified numerically (1200² grid, exact match; split-cell control exactly
tight; violation robust: units shrunk to 0.98 → 0.6533 > 0.3341; middle square replaced by a
0.6-square tilted 0.1 rad → 0.5822 > 0.3822; staggered strip squares → 0.4444 > 0.3333). ∎

Consistency: at k=1 the family degenerates to the split cell (FCMB tight — matches "proved at
k=1"). No [V]/[P] theorem of the report is touched: budget C ≤ N holds (max C = N measured),
structure identity holds, conjecture holds with equality (Σd = N). The prior adversarial search
simply never tried a deficient column (it searched tilted grains, split-cell anneals, and
no-full-capture probes).

## Why every "measure shortcut" dies (the honest rewrite)

E[hits] = g and hits = Σ_{m≥1} 1{hits ≥ m} give the identity
   g = (1 − |Av|) + Σ_{m≥2} |{hits ≥ m}|.
So at n = N+1 the conjecture (g+s ≥ 1) is EXACTLY equivalent to
   **OC-FCMB:  |Av| ≤ s + Σ_{m≥2} |{p : C(p) ≤ N−m}|**,
and the deficient-column family attains equality in OC-FCMB throughout (verified numerically:
defect 0.00000 on equal/uneven/split/staggered members, k=2,3). FCMB was the m≥2-truncated
version; the counterexample hides exactly (k−1)/(k+1) of the needed mass in multiplicity m ≥ 2
(a tall thin gap strip meets k lattice points at once). Any correct measure statement must count
multiplicity — and then it is Fubini, i.e. the conjecture itself. There is no strictly-weaker
true interpolant of this type: replacing s by s' needs s' ≥ s + overlap-loss, which by F6.2 is
exactly the quantity one cannot bound without proving the conjecture.

## Triage verdicts (assignment menu)

1. **Kneser/measurable sumsets: DEAD.** The hoped-for lower bound |π(G)| ≥ 1−s is false
   (|π(G)| = (1−s)/k on U_k, maximally sub-additive folding at exact criticality). π(G) is a
   union of translates with no forced sumset/periodicity structure; Kneser-type lower bounds
   need hypotheses validity does not supply. Ruzsa covering gives nothing beyond the trivial
   |π(G)| ≤ g. The Av-stability idea degenerates: Av = arc × S¹ here, boundary structure trivial.
2. **Ergodic/fault-drift: mechanism TRUE, conclusion FALSE.** The deficient column IS the fault;
   its y-phases drift by exactly the local deficits and sweep the full circle (winding 1). This
   spreads the SQUARES' folded positions (∩_j Y_j = ∅: no shift captures all k+1 column squares
   — a true and possibly reusable fact), but not the GAP: the gap stays locked at one x-arc.
   Drift spreads π(G) in the drift direction only; the transverse coordinate can be constant.
   |π(G)| = width × 1, not ≥ 1−s.
3. **Discrepancy/near-injectivity: REFUTED — the headline.** Near-injectivity of folding at
   criticality is false: U_k folds its gap k-to-1 at g+s = 1 exactly. This kills FCMB
   unconditionally (independent of the conjecture's truth).
4. **Dislocation/winding: correct topology, insufficient strength.** "Total phase travel = 1
   around the extra square" is provable on a deficient column (trivially: k+1 heights summing to
   k ⇒ Σδ_j = 1 = Burgers vector), and the empty-square index on Av rotates through the column
   as p_y winds — an interval-exchange/three-distance pattern. But winding is 1-D; it forces the
   swept ANNULUS, not area. Winding-1 with zero transverse variation has |π(G)| = max-width. To
   force area one would need transverse spreading, which validity does not force (that is
   precisely the counterexample).

## Collateral refutations (coordination)

- F4's AP reduction target Σ_i |∩_{j≠i} π(S_j) \ π(S_i)| ≤ Σ(1−d_i)² is FALSE: at U_2 the three
  column terms are each (2/3)·(1/3) = 2/9 (unit squares have π = full torus; the two other
  y-arcs' complements tile), total 2/3 > 1/3. The briefing's split-cell verification was of the
  nongeneric overlap-free stratum.
- The "repetition charges s" candidate lemma (F4.1) is FALSE: U_k has k-fold in-phase repetition
  of the gap strip charged only s = 1/(k+1).
- The second-moment sufficient condition (E) [g + Σ_{v≠0}|G∩(G−v)| ≤ g²/(1−s)] fails on U_k as
  it must (LHS = 4/3, RHS = 2/3 at k=2); note Paley–Zygmund is TIGHT here (hits = k·Bernoulli(1/(k+1)))
  — the failure is FCMB's, not P–Z slack.
- UNTOUCHED and still valid: Structure Identity, Theorem B (sharp AP capture/BKU), Theorem D as
  an implication (hypothesis now known false), κ-bound T6, all §1–6 theorems, and the lower-bound
  direction |Av| ≥ 1−g > 0 for any hypothetical counterexample.

## Surviving route sketched (for the orchestrator)

For a hypothetical counterexample (Σd = N+ε, g+s < 1): |Av| ≥ 1−g > s ≥ 0. On Av (AP, d_i ≤ 1)
exactly one square is empty and the rest capture bijectively; per-row disjoint chords give
Σ_capturing d ≤ N pointwise, so Σd ≤ N + d_{empty(p)} for EVERY p ∈ Av, i.e. every ever-empty
square has d_i > ε... and side < 1. On U_k the ever-empty set is exactly the deficient column and
the empty index is an interval-exchange orbit of winding 1. Candidate true lemma space: control
WHICH squares can be empty on Av and force one of them small (or force multiplicity mass
Σ_{m≥2}|{hits≥m}| ≥ |Av| − s directly = OC-FCMB). The enemy shape is now explicit.

## Erratum needed in ERDOS_106_REPORT.md §7A

Demote FCMB from "new central conjecture" to REFUTED (this file + refute_fcmb.py = certificate);
add the deficient-column family to the extremal catalogue (§6.7 nonuniqueness: extremals with
g > 0 exist, a k-parameter manifold); replace the recommended attack order (i)–(iii) (all target
a false statement); state OC-FCMB as the exact (conjecture-equivalent) corrected form.
