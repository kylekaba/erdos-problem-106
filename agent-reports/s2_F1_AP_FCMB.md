All verification complete. Composing final report.

## CLAIMS

**C1. The FCMB is FALSE for every k ≥ 2 — already for axis-parallel packings.** [CONFIRMED: proof + exact computation + independent grid check]

*Counterexample (the "column packing" P_k).* In [0,k]², place k+1 squares of side d = k/(k+1) stacked in the column [0,d]×[0,k] (y-intervals [jd,(j+1)d] tile [0,k] exactly), plus k(k−1) unit squares tiling [1,k]×[0,k]. This is a valid AP packing of n = k²+1 squares (machine-checked, k=1..6) with Σdᵢ = N, g = k/(k+1), s = 1/(k+1), g+s = 1 exactly.

*Proof that |Av| = k/(k+1).* For generic x ∈ (0, k/(k+1)) all k+1 column squares meet lattice line 0; their y-intervals tile [0,k], which contains exactly k points of y+ℤ, each interior to exactly one interval for a.e. y — so exactly one column square is empty and the other k capture; the units always capture k(k−1). Hence C = k + k(k−1) = N for a.e. y, i.e. the slice is full. For x ∈ (k/(k+1), 1) every column square is empty (C = N−k). So Av = [0, k/(k+1)) × [0,1) up to null sets. ∎

FCMB demands |Av| ≤ s = 1/(k+1); actual is k/(k+1). **Violation (k−1)/(k+1) → 1 as k → ∞** while s → 0. At k=1 the construction degenerates to the split cell a=b=1/2 with equality — which is exactly why the proved k=1 case gave no warning. Section 7A of ERDOS_106_REPORT.md ("the new central conjecture", "survived adversarial search") and assignment F1's goal must be retracted/amended; the prior adversarial searches simply never tried this two-parameter-free family.

**C2. One-gadget formula unifying the tight and the violating cases.** [CONFIRMED numerically exact on 5 mixed test cases] Stack m+1 squares of sides d₁..d_{m+1} ≤ 1 (Σ = h integer ≤ k) sharing their left edge at the bottom of strip 0, k−h units above, k(k−1) units in the other strips (valid packing, n = N+1, always g+s = 1). With d₍₁₎ ≤ d₍₂₎ the two smallest sides:
|Av| = d₍₁₎ + (d₍₂₎ − d₍₁₎)(1 − d₍₁₎).
The split cell is the h=1 case: |Av| = a + (b−a)(1−a) = a²+b² = s (FCMB-tight); the equal-sides column is the maximally violating case. So the previously identified "extremal family" and the counterexample family are one family; FCMB fails on most of it.

**C3. Exact decomposition identity (AP, all dᵢ ≤ 1).** [PROVED; verified to 5.6e-17 on 200 random packings] With miss-sets M_X(x) = {i : x ∉ Xᵢ} (Xᵢ = x-projection arc, length dᵢ), α₀ = |{M_X = ∅}|, αᵢ = |{M_X = {i}}| (and β's for y):
- Av = ⊔ᵢ Avᵢ with Avᵢ = [∩_{j≠i}X_j × ∩_{j≠i}Y_j] \ [Xᵢ×Yᵢ] **exactly** (no inequality — the assignment's route-(B) sum equals |Av|, hence route (B)'s target inequality is identically FCMB and is false by C1);
- **|Av| = α₀·Σβᵢ + β₀·Σαᵢ + Σαᵢβᵢ, with α₀β₀ = 0** (budget), and termwise αᵢβᵢ ≤ (1−dᵢ)², so **Σαᵢβᵢ ≤ s always**. All FCMB failure lives in the full-hit terms α₀, β₀; α₀ > 0 forces an over-full lattice column: k+1 squares on one vertical line with total deficit Σ(1−d) ≥ 1 and x-phases aligned (stress-tested: 129/129 random instances).

**C4. THEOREM (Restricted FCMB-AP — the strongest theorem fully proved; NEW).** *Every axis-parallel packing of N+1 squares in [0,k]² with all dᵢ ≤ 1 and Σdᵢ > N satisfies |Av| ≤ s.*

*Proof.* σ := Σ(1−dᵢ) = (N+1) − Σd < 1, all terms ≥ 0. **Lemma A: {M_X = ∅} is null.** For generic x in it, every square's x-interval contains an interior point x+mᵢ, mᵢ ∈ {0..k−1}; pigeonhole gives a line with L ≥ ⌈(N+1)/k⌉ = k+1 squares; these pairwise overlap openly in x, hence have pairwise disjoint y-intervals in [0,k], so Σ_L(1−dᵢ) ≥ L−k ≥ 1 > σ ≥ Σ_L(1−dᵢ) — contradiction. Symmetrically β₀ = 0. By C3, |Av| = Σαᵢβᵢ ≤ s. ∎

**Corollary (new proof of BKU for sides ≤ 1, self-contained, ~½ page).** If Σd > N then g+s < 1 (structure identity) while g = E[hits] ≥ P(hits ≥ 1) = 1−|Av| ≥ 1−s. Contradiction; hence Σd ≤ N. This is the measure-theoretic reproof of g(k²+1) = k (side-≤1 case) the assignment targeted — but it exists **only in restricted form**; C1 shows the hypothesis Σd > N is razor-sharp (at Σd = N, α₀ jumps to k/(k+1)).

**C5. Logical status of FCMB after C1+C4.** FCMB restricted to g+s < 1 still implies the full Erdős conjecture (same 3 lines, run as a contradiction), and is implied by it vacuously — so **restricted FCMB is logically equivalent to the conjecture**, carrying no independent content as a statement. Its remaining value is the *proof template* of C4: global deficit < 1 forbids over-full lines. Theorem D stays valid as an implication; unrestricted FCMB is dead. Boundary-instability principle: |Av| − s jumps from ≤ 0 (target) to (k−1)/(k+1) ON the boundary g+s = 1, so no perturbative/continuous argument in (g,s) can prove the restricted version; integrality of the pigeonhole must carry it. Also refuted en route: any bound |Av| ≤ F(g,s) with F continuous and ≤ s on {g+s<1} (column family sits on the closure); |Av| ≤ max(g,s) (stack gadget [0.9,0.9,0.9,0.3] at k=3: |Av| = 0.72 > max = 0.52).

**C6. Corrections to session notes.** Note (E)'s "for one-cell-confined gaps (all extremals) autocorrelation = 0" is wrong as a classification: column packings are extremals with strip gaps, autocorrelation Σ_{v≠0}|G∩(G−v)| = g(k−1), and Paley–Zygmund is exactly tight on them too (hits ∈ {0,k}). Note (F)'s dislocation heuristic fails on them: zero phase drift, maximally folded gap |π(G)| = g/k. Note (B)'s displayed inequality is FCMB itself (C3) and is false.

## COUNTEREXAMPLES AND CHECKS

- Column packings k=1..6, exact breakpoint evaluation: |Av| = k/(k+1) to machine precision; independent 2001² midpoint grid agrees (k=2: 0.666667; k=3: 0.749750 ≈ 3/4 − grid line artifact). Budget maxC = N a.e.; the only C = N+1 artifacts are closed-boundary double counts of total measure ≤ 8e-16 (exact method) and the single grid line y = 0.5 (measure 0) — diagnosed explicitly.
- Split-cell k=2,3, a ∈ {0.37, 0.5, 0.8}: |Av| = s to machine precision (re-confirms prior tightness claim).
- Stack-gadget formula: exact on all tests (k=2,3,4, unequal sides, 5-square stacks).
- k=2 global search (assignment step 3): 20k random strip packings + structured seeds + 3×4000-step hill-climbs on |Av|−s. **Optimum found: +1/3 at the equal column packing** (the assignment's expectation "optimum 0 on split-cells" is wrong); max |Av| found = 2/3. Violations also occur strictly inside g+s > 1 (e.g. +0.18 at g+s = 1.16) — failure is a region, not a boundary accident.
- Identity C3 and α₀β₀ = 0: 200 random packings, max error 5.6e-17; Lemma A mechanism: 129/129.

Code and full derivations: `/private/tmp/claude-501/-Users-kylekabasares-Desktop-erdos-106/6b0597a9-48bd-4e8c-a957-7fc4a05f26d8/scratchpad/session2/F1/{fcmb_check.py, search_k2.py, NOTES.md}`.

## DEAD ENDS

- Proving unrestricted FCMB-AP (assignment routes 2–4): impossible, statement false. The hoped-for "correlation content" of simultaneous capture vanishes exactly when k+1 phase-aligned squares over-fill one column — then capture of all-but-one is automatic for *every* y.
- The abstract two-circle inequality (C3's RHS with only α₀β₀ = 0 as constraint): false (4 arcs of length 3/4, W's stacked, Z's tiling ⇒ LHS 0.75 vs s = 0.25); real packing geometry is needed, and at σ = 1 the bad configuration is packable (that discovery *is* the counterexample).
- "Chord-slack-to-measure conversion" as a general lemma: the 1-D version Σᵢ|{y : all Iⱼ (j≠i) hit, Iᵢ missed}| ≤ Σ(1−dᵢ)² is false (two ½-intervals in [0,1]: LHS 1, RHS ½); only the σ < 1 pigeonhole rescues the 2-D statement.
- Extension of C4 to dᵢ ∈ (1,2) (d ≥ 2 is trivial since then s ≥ 1): GAP. Big squares never miss and can capture 2 points per line, breaking the exactly-one-empty combinatorics; the over-full-line deficit ≥ 1 still holds but can be offset by negative deficits elsewhere. Not needed for any application (vacuous by BKU) but needed for a fully non-circular general-size reproof.

## BEST NEXT STEP

Port the C4 mechanism to the rotated problem — this is now the sharpest live route. The corrected central statement is restricted FCMB (equivalent to the conjecture): *Σdᵢ > N ⇒ |Av| ≤ s*. The AP proof needs exactly two ingredients, both with rotated analogues: (i) **termwise bound** on single-miss products — for tilted squares the miss arcs have length (1−wᵢ)₊ ≤ 1−dᵢ, so this side only *improves* under tilt; (ii) **Lemma A** (full-hit shifts are null when total deficit < 1) — the rotated obstacle is that a tilted square can cross a vertical lattice line with a tiny corner chord, so over-full lines are not immediately forbidden; but crossing-without-capturing is precisely the corner-triangle defect Lᵢ > 0, whose per-square bad-shift measure is 2d sinθ per axis (§5 product structure). Concrete next assignment: prove "rotated Lemma A" — if Σdᵢ > N then the set of x for which all N+1 squares meet vertical lattice lines *and* all can simultaneously capture has measure controlled by Σdᵢθᵢ — combining the disjoint-chord stacking (Σ chords ≤ k per line) with the Coverage Lemma. Secondarily: (a) update ERDOS_106_REPORT.md §0.6 and §7A per C1/C5 (I did not edit the shared report; amendments are itemized in NOTES.md §4); (b) close the d ∈ (1,2) gap of C4 to make the BKU reproof size-free; (c) determine the sharp AP measure bound (data suggests max_{AP} |Av| = k/(k+1) and max(|Av|−s) = (k−1)/(k+1), attained at the column packing — a clean finite conjecture worth settling at k=2 by cases).