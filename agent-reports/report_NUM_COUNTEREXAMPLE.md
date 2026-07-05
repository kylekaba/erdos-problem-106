## CLAIMS

All claims below are **numerical findings**, not theorems. Method: maximize Σsᵢ over per-square variables (cx, cy, θ, s), pairwise-disjoint interiors enforced by the separating-axis theorem (SAT: max over the 4 edge-normal axes of the projected-interval gap ≥ 0), containment by all 4 corners ∈ [0,1]², solved with scipy SLSQP (analytic objective gradient, finite-difference constraint Jacobian) from many structured + random multistarts. Every reported "certified" sum was re-verified in `np.longdouble` (float80 on this machine) and, when the raw solution had a negative feasibility margin, repaired by binary-searching a global side-shrink factor until the long-double SAT + containment margin is ≥ 0 exactly (shrinking sides about fixed centers monotonically increases every SAT gap and decreases every containment violation, so the binary search is sound).

**Claim 1 (pipeline validity — axis-parallel control reaches k).** With θ frozen at 0, the optimizer attains g(k²+1)=k to ≤ 3e-9 for all four cases: n=2 → 1.0000000000, n=5 → 2.0000000000, n=10 → 3.0000000001 (certified 2.999999997), n=17 → 4.0000000000. This validates objective, constraints, and multistart coverage. Confidence 0.98.

**Claim 2 (no rotated configuration beats k; conjecture survives the stress test).** Best certified sums with free rotations:

| n | k | rotated best raw | rotated best **certified** | axis control | exceeded k+1e-7? |
|---|---|---|---|---|---|
| 2 | 1 | 1.0000000009 (viol −8.6e-10) | 0.9999999991 | 1.0000000000 | **NO** |
| 5 | 2 | 2.0000000079 (viol −4.0e-09) | 1.9999999759 | 2.0000000000 | **NO** |
| 10 | 3 | 3.0000000247 (viol −1.6e-08) | 2.9999998536 | 3.0000000001 | **NO** |
| 17 | 4 | 4.0000000000233 (viol −2.3e-11) | 3.9999999996 | 4.0000000000 | **NO** |

(n=2: 100 starts; n=5: 150; n=10: 220; n=17: 120 single-stage + a focused two-stage run, see Dead Ends.) Several raw sums exceed k by up to 4e-7, but **every** such excess is accompanied by a negative SAT margin of the same order; after exact-feasibility repair all certified sums fall (barely) below k. No apparent violation survived exact rechecking — consistent with k being the true optimum with a locally quadratic/degenerate ridge, not with any counterexample. Confidence that no counterexample exists *at these n within reach of this method*: 0.9. (This is evidence, not proof; SLSQP is a local method and an exotic deep basin could be missed — though the structured starts deliberately seeded diamonds, pinwheels, coherent row tilts, and global tilts.)

**Claim 3 (optimal rotations collapse to axis-parallel).** In every best configuration for every n, all θᵢ converged to 0 mod π/2 to within 5e-10 (n=17 two-stage: 4.4e-15), even when the optimizer was started from tilted rows, global 3°/10° tilts, diamond seeds, or pinwheels. Rotation is never retained at or near the optimum. Confidence 0.95.

**Claim 4 (the optimum at sum = k is massively non-unique).** The optimizer repeatedly hit Σs = k exactly on *irregular* axis-parallel packings: n=5 with sides {1/2, 1/2, 1/2, 0.2944, 0.2056} (any {a, 1/2−a} split works), n=10 with sides ranging 0.2407–0.4252 summing to exactly 3, n=17 similarly (sides 0.179–0.374, sum 4.0000000000). The maximizer set contains positive-dimensional families (squared-rectangle-style partitions). Relevant to theory: variational arguments at "the" optimum cannot assume isolation or a grid structure. Confidence 0.9 (the exact-sum-k membership of these irregular configs verified to 1e-10; that they are genuinely optimal follows from g(k²+1)=k).

**Claim 5 (tilt-penalty curve: coherent tilt costs Θ(k·t) scaled, not Θ(N·t)).** For n=10 with ALL thetas frozen at t₀ (positions/sides optimized, 80 starts each), best certified sums:

| t₀ | best sum | defect 3−Σs | defect/t |
|---|---|---|---|
| 2° | 2.9851626884 | 0.014837 | 0.425 |
| 5° | 2.9573408287 | 0.042659 | 0.489 |
| 10° | 2.9061232191 | 0.093877 | 0.538 |

Fit: defect ≈ 0.427·t + 0.64·t² (t in radians). Two consequences: (a) the penalty is strictly positive and linear in t — coherent tilting never helps; (b) the naive global-shrink prediction 3(1 − 1/(cos t + sin t)) ≈ 3t is beaten by a factor ≈ 7: the optimizer rearranges rows (staircase offsets) so only the boundary pays. In scaled units the defect is ≈ 0.43·k·t, i.e. **Θ(k·t), not the Θ(k²·t) feared in trap-warning #4**. GAP: these are best-found values, hence *upper bounds on the defect* (lower bounds on the constrained max); the true defect could be smaller still, and this is one k (k=3) and three t values. Confidence in the qualitative Θ(k·t) scaling: 0.7; in the table values as lower bounds on constrained maxima: 0.95.

**Claim 6 (one square frozen at 45°).** Best found 2.9809363 with the 45° square shrunk by the optimizer to s = 0.0803. The supremum of this constrained problem is exactly 3 (send the diamond's side to 0, allowed by the s ≥ 0 bound), so 2.9809 is a local optimum; the meaningful observation is that the optimizer *always shrinks the tilted square toward extinction* rather than accommodating it at unit scale. Confidence 0.9.

## COUNTEREXAMPLES AND SANITY CHECKS
- SAT unit tests: two side-1/2 squares touching → sep = 0 exactly; overlapping by 0.3 → sep = −0.3; 45°-vs-axis pair → correct positive gap.
- Axis-parallel control (Claim 1) reproduces the proven values g(k²+1)=k at all four n — validates the whole pipeline end-to-end.
- Every raw sum > k was re-verified in long double; all had genuine (if tiny) infeasibilities and certified below k. Treated per instructions with extreme suspicion; none survived.
- Garbage detection: SLSQP failure modes produce coincident squares (raw "sum 4.0" at n=5 with penetration depth 1.0). The feasibility filter (viol > −1e-6 before ranking) plus the certify step catches these; the certify shrink-repair correctly returns 0 for coincident-center configurations.
- Certify monotonicity argument (shrink about centers increases all SAT gaps, reduces containment violations) checked analytically: gap = dist − rᵢ − rⱼ with rᵢ linear in sᵢ, dist fixed; corners move affinely toward the (clipped) center.

## DEAD ENDS
1. **Starting SLSQP exactly at the tight optimum** (exact k-grid-with-split-cell, all constraints active, sum = k): the nonsmooth SAT max + fully degenerate active set makes SLSQP *descend* to 2.692 from a sum-3 start at n=10. Fix: shrink starts by 0.5–4% off the boundary; then it climbs back to 3.0000000. Also polish steps use a 0.05% pre-shrink and never accept a worse result.
2. **Ranking by raw sum without a feasibility filter**: catastrophic — deeply infeasible SLSQP failures (overlap depth ~1) dominate the ranking (fake sums 4.0 at n=5, 8.0 at n=10). All headline numbers in this report postdate the fix.
3. **Single-stage rotated SLSQP at n=17** (68 variables, 136 SAT constraints): stalls at 3.9262 across 120 starts while the axis control reaches 4.0 — pure optimizer failure, initially looking like "rotation costs 0.074". The two-stage protocol (solve axis-parallel to 4.0, release thetas with tiny shrink + θ-jitter, re-solve) recovers 4.0000000000 with θ returning to axis-parallel to 4e-15. Lesson: apparent rotated-vs-axis gaps at larger n are artifacts unless the rotated run is seeded from the axis optimum.
4. **Smoothed SAT (log-sum-exp)**: rejected before running — the conservative direction (LSE − ln4/β ≥ 0) forces artificial gaps ~ln3/β between *touching* squares, which is exactly the regime that matters; the permissive direction allows overlap. Hard max + finite differences worked once starts were kept off the degenerate boundary.

## BEST NEXT STEP
Measure the tilt-penalty curve as a function of k, not just t: repeat the all-θ-frozen-at-t experiment for k = 4, 5, 6 (n = k²+1) at t ∈ {1°, 2°, 5°} with the two-stage seeding protocol, and fit defect(k, t) = c·k·t + O(t²). If the Θ(k·t) scaling of Claim 5 holds with a stable constant c ≈ 0.4, this pins the exact exchange rate between coherent-grain tilt and side-length loss — precisely the sharp constant that trap-warning #4 says an untilting/structure proof must have, and it tells the theory side that rigid-rotation repair of a tilted grain of size m costs only Θ(m·t) (matching the boundary gap evidence), making a structure-then-untilt proof quantitatively viable rather than order-of-magnitude-blocked.

**Files:** code `/private/tmp/claude-501/-Users-kylekabasares-Desktop-erdos-106/6b0597a9-48bd-4e8c-a957-7fc4a05f26d8/scratchpad/numce/pack.py` (library + main/control/tilt drivers), `run17.py` (two-stage n=17), `run45.py` (45° square); results (full best-configuration parameters cx/cy/θ/s in each): `main_results.json` (rotated n=2,5,10,17), `control_results.json` (axis-parallel), `tilt_results.json` (coherent-tilt curve), `tilt45_results.json` (one square at 45°), `n17_results.json` (two-stage n=17); logs `main.log`, `control.log`, `tilt.log`, `n17.log` — all in the same directory.