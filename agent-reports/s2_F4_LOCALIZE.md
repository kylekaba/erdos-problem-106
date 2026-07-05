All verifications complete. Final report follows.

## CLAIMS

**CLAIM 1 (REFUTATION — headline result). FCMB is FALSE for every k ≥ 2.** Confidence: certain (analytic proof + machine verification).

*The deficient-column packing* P_k (axis-parallel, n = k²+1): with c = k/(k+1), take k+1 squares of side c stacked at (0, rc), r = 0..k (they exactly tile [0,c]×[0,k] since (k+1)c = k), plus (k−1)k unit squares tiling [1,k]×[0,k]. Validity machine-verified (SAT disjointness + containment). Then: Σd = N exactly (extremal), g = k/(k+1), s = 1/(k+1), g+s = 1 (Structure Identity checks). The gap is a single vertical sliver G = [c,1]×[0,k] of width w = 1/(k+1).

*Capture computation (3 lines, exact):* for a.e. p, every lattice point p+v with v₁ ≥ 1 lies in [1,k)×[0,k) and is always covered by the units; the k points with v₁ = 0 are all covered iff p₁ < c (the column covers [0,c]×[0,k] entirely), else all k are in the sliver. So C(p) = N ⟺ p₁ < c:

**|Av| = k/(k+1)  vs  s = 1/(k+1): FCMB violated by (k−1)/(k+1) → 1.**

hits(p) = k·1[p₁ > c] (two-point law {0,k}); |π(G)| = g/k (the k per-cell sliver pieces are perfectly in phase — k-fold folding). At k = 1, P₁ *is* the a=b=½ split cell (equality) — which is exactly why the k=1 proof and split-cell tightness gave no warning: P_k is the height-k extension of the split cell, and folding kills the bound.

*Robustness:* the violation is an open condition. Tilting the column squares by t (side shrunk to c/u₁(t); SAT-verified valid, strictly sub-critical, g+s > 1): k=2, t=0.02: |Av| = 0.622 vs s = 0.360; t=0.05: 0.562 vs 0.398; k=3, t=0.02: 0.684 vs 0.280. Harness validated first on the known-tight split-cell family (|Av| = a²+b² = s reproduced to 6 decimals at k=2,3).

*Also refuted by the same example:* the folded-gap form |π(G)| ≥ 1−s (here g/k vs k/(k+1)); FCMB-AP; the empty-square-decomposition target Σᵢ|∩_{j≠i}π(S_j) \ π(S_i)| ≤ s — on P_k that sum is exactly (k+1)·c·w = k/(k+1) = |Av| (the column squares' y-phases −r/(k+1) equidistribute; the omitted arcs tile the circle; decomposition is EXACT, bound false); and route (E)'s target (Claim 3). Theorem D (FCMB ⇒ conjecture) stands as an implication with false hypothesis. **The conjecture itself is untouched** — P_k is extremal, not an enemy.

**CLAIM 2 (Localization Lemma L1 — proved, survives, correct frame).** For v ∈ V = {0..k−1}², A_v := (U∩C_v) − v with C_v = v+[0,1)², U = ∪S_i. Then a.e.: C(p) = Σ_v 1_{A_v}(p); Av = ∩_{v∈V} A_v; |A_v| = 1 − γ_v (γ_v = cell-v gap); and for every block B ⊆ V: |Av| ≤ |∩_{v∈B}A_v| = 1 − |π(G∩C_B)|, with equality |Av| = 1 − |π(G)| at B = V. Full measure hygiene (boundary/null-set bookkeeping) in DERIVATIONS.md §1. One-cell corollary |Av| ≤ 1 − max_v γ_v is tight on BOTH the split-cell and column families. Confidence: proved, numerically verified (cell-by-cell at k=2).

**CLAIM 3 (Route-(E) triage — decisive structural negative; proved).**
(a) The sufficient condition g + R ≤ g²/(1−s) (R = Σ_{v≠0}|G∩(G−v)|) *implies* g ≥ 1−s, since R ≥ 0. It is unsatisfiable on the entire enemy region g+s < 1 and thus can never carry conjecture content; on P_k it fails by exactly the factor k (R = (k−1)g, LHS/RHS = k, verified k=2..5). Same for the Bonferroni/integer-support bound |π(G)| ≥ g − R (needs R ≤ g+s−1 ≤ 0).
(b) *General principle:* |Av| ≥ 1 − g for EVERY packing (Markov on the integer variable hits). Hence any enemy automatically violates |Av| ≤ s; and any proof chain of the form |Av| ≤ 1 − (lower bound on |π(G∩W)|) is capped by |G| = g < 1−s on enemies. **All gap-mass routes — second moment, Bonferroni, block localization, Kneser/Macbeath sumset/support bounds — are structurally incapable of conjecture content.** The assigned localization program ("find one block B with |∩_B A_v| ≤ s") is included: ∩_B A_v ⊇ Av ≥ 1−g > s on enemies.
(c) Fold cap: any TRUE s-only lower bound on |π(G)| is ≤ (1−s)/k at the column points, so gap-mass yields at best g ≥ (1−s)/k — a factor k off.

**CLAIM 4 (Exact overlap identity + no-repair theorem; proved).** With Φ = hits: |Av| = 1 − g + E[(Φ−1)₊], so FCMB ⟺ "folding overlap ≤ extremality slack g+s−1". On P_k: overlap = (k−1)/(k+1), slack = 0 — the overlap exceeds the slack by an amount → 1 *on extremal packings*, so no correction vanishing at extremality repairs FCMB. **No-repair theorem:** no F(g,s) can satisfy (i) |Av| ≤ F(g,s) on all valid packings, (ii) F < 1−g on {g+s<1} (what the Theorem-D contradiction needs), (iii) continuity at the tilted-column accumulation points: the family P_k(t), t→0⁺ forces a jump ≥ 1 − 2/(k+1) → 1 across the extremal surface g+s = 1 at (k/(k+1), 1/(k+1)). Any conjecture-closing measure inequality in (g,s) must already encode the conjecture. The successor target must use finer data (per-direction fold multiplicities, ε explicitly, or capture-side rigidity).

**CLAIM 5 (What survives; proof-side residue).** (a) Enemy-FCMB (|Av| ≤ s restricted to Σd > N) is *equivalent* to the conjecture — correct proof shape, zero independent content. (b) The productive two-sided squeeze, new leverage exposed by L3: an enemy must have a **large** full-capture set, |Av| ≥ 1−g > s, and the AP row-chord rigidity (p1 report, still valid) forces pointwise on Av: the N capturing squares satisfy Σ′d ≤ N, hence *every* full-capture shift's empty square has d_{i₀(p)} ≥ ε = Σd − N. Enemy ⇒ measure ≥ 1−g of shifts, each exhibiting a bijective near-grid capture by N squares plus one ε-large idle square. The contradiction should be extracted from this rigidity (capture side), not from gap mass.

## COUNTEREXAMPLES AND CHECKS

- **P_k kills FCMB**: k=2: |Av| = 0.666667 vs s = 0.333333; k=3: 0.750000 vs 0.250000; k=4: 0.800000 vs 0.200000 (grids 700²–1200², budget C ≤ N asserted everywhere, exact analytic agreement). Harness pre-validated on split-cell (slack +0.000000, tight, as known).
- Tilted P_k(t): violations 0.164–0.404 at t ∈ {0.02, 0.05}, k ∈ {2,3} — open set, strictly sub-critical.
- Route-(E) constants on P_k: R = (k−1)g exactly; E[hits²] = kg; Cauchy–Schwarz is *tight* (hits is {0,k}-valued) and gives only P(hits≥1) ≥ g/k. P_k is the R-maximizer archetype at fixed (g,s) the assignment asked me to construct — it maximizes so hard it falsifies the target.
- "Repetition charges s" local lemma (mechanism (i)): FALSE. Adjacent-cell overlap ov = w = 1/(k+1) vs local deficit ≤ 3/(k+1)²: ratio (k+1)/3 → ∞. Even globally the exchange rate is quadratic: k-fold repetition of a width-w sliver costs only (k+1)w² of deficit.
- Consistency: capture lemma max C ≥ 2Σd−N is tight on P_k (max C = N), κ-bound and Structure Identity check; mod-1 pigeonhole not violated (units share one phase: k²−k ≤ N).

Code/derivations: `/private/tmp/claude-501/-Users-kylekabasares-Desktop-erdos-106/6b0597a9-48bd-4e8c-a957-7fc4a05f26d8/scratchpad/session2/F4/fcmb_column_check.py` (all output reproduced above) and `.../session2/F4/DERIVATIONS.md` (full proofs of L1, overlap identity, no-repair theorem, triage).

## DEAD ENDS

1. **FCMB itself** — false for all k ≥ 2; retire as central conjecture; §7A of ERDOS_106_REPORT.md needs a refutation addendum.
2. **Route (E) second-moment/autocorrelation** — doubly dead: unsatisfiable in the enemy regime (needs R < 0) and its safe-regime target (FCMB surplus) is false.
3. **Block localization to |∩_B A_v| ≤ s** — impossible for enemies (Claim 3b); the localization *identity* survives as bookkeeping only.
4. **Kneser/Macbeath sumset angle** (assignment part 2) — capped by the fold cap (Claim 3c); no support/sumset lower bound can beat |π(G)| = g/k realized by P_k.
5. **Dislocation heuristic (F)** — refuted as stated: P_k is a genuine dislocation whose phase drift is parallel to the gap sliver and resonant ((k+1) steps = full cycle, three-distance at rotation 1/(k+1)); drift spreads π(G) only transversally to the gap's thin direction, and equidistribution of *square* phases here makes Av large, not small.
6. **Two-cell/local charging lemmas** — false locally, quadratic (not linear) exchange rate globally.

## BEST NEXT STEP

1. **Immediately propagate the refutation**: update ERDOS_106_REPORT.md §7A (FCMB → REFUTED, deficient-column family, tight at k=1 only) and inform F2 (falsification agent) that the search is settled — the counterexample is P_k, closed-form, k ≥ 2. The attack-order recommendation (i)–(iii) of §7A is obsolete.
2. **New central target (capture-side squeeze), concrete first milestone**: for AP packings with all d_i ≤ 1 and Σd = N+ε, ε > 0, combine (a) |Av| ≥ 1−g (L3), (b) row-chord rigidity ⇒ empty square d_{i₀} ≥ ε pointwise on Av, (c) Av_i ⊆ {S_i captures nothing}, |{S_i empty}| = 1−d_i², and the exact Av_i-decomposition (verified exact on both P_k and split-cell) to derive a contradiction. The enemy must sustain a measure-(1−g) set of bijective near-grid captures while hiding an ε-large idle square everywhere — quantify the rigidity of the capturing N-family across a positive-measure shift set (its phase structure is an exact integer covering system; P_k shows the extremal mechanism is a resonant column, which at ε > 0 breaks). This inherits everything true from the FCMB program while dodging all four impossibility results above.
3. Secondary: recompute what P_k does to the κ-bound arc-rigidity picture (P2 report §Corollary 2.5) — the column is the natural extremal arc system; it may pin the true shape of the "dip mass ≥ 2c" anti-concentration statement, which Claims 3–4 leave as the only measure-type route not factoring through gap mass.