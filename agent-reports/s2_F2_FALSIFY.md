k=3 search also converges to the row configuration R_3 (F → −1/2). All results are in. Final report:

## CLAIMS

**C1. FCMB is FALSE for every k ≥ 2 — refuted by an explicit, classical, axis-parallel EXTREMAL packing (proof by hand, no numerics needed). Confidence: certain.**
The *row packing* R_k in T=[0,k]²: bottom row of k+1 squares of side k/(k+1), Q_i = [(i−1)k/(k+1), ik/(k+1)] × [0, k/(k+1)]; the region [0,k]×[1,k] tiled by k(k−1) unit squares. Then n = (k+1)+k(k−1) = k²+1 = N+1, Σd_i = k + k(k−1) = N (extremal — for k=2 it is a classical f(5)=2 equality configuration), G = [0,k]×(k/(k+1),1).
*Proof of violation.* s = (k+1)·(1/(k+1))² = 1/(k+1). For p=(px,py): lattice points with b ≥ 1 lie in the unit-tiled block (always captured); points at height py are in the fully covered strip iff py < k/(k+1) (captured for every px), and ALL k of them are in G iff py ∈ (k/(k+1),1). Hence Av = {py < k/(k+1)}, |Av| = k/(k+1). FCMB demands k/(k+1) ≤ 1/(k+1): false for k ≥ 2, **violation margin (k−1)/(k+1) → 1**. At k=2: |Av| = 2/3 vs s = 1/3, F := |π(G)|−(1−s) = −1/3.
Numerically confirmed three independent ways (rasterized folding at M=1200/1600; direct shift-sampling of C(p) = |Av| = 0.666667/0.750000; exact SAT feasibility). The AP-FCMB (recommended attack step (i), "measure reproof of BKU") is therefore also false.

**C2. Straddle family: violations form a continuous path from the trivial boundary into R_2 (exact closed form; verified to 1e−6 at δ = 0.05, 0.1, 0.2, 0.3). Confidence: certain.**
k=2, δ∈(0,1/3]: sides (1−δ) at [0,1−δ]² and [1+δ,2]×[0,1−δ], side 2δ at [1−δ,1+δ]×[0,2δ], two units on top. Σd = N exactly for all δ; |π(G)| = 3δ−6δ², 1−s = 4δ−6δ², **F = −δ exactly**. This is precisely the configuration the orchestrator flagged as unexplored (the b-square straddling two cells lets b = 2δ > δ, doubling the deficit budget); at δ=1/3 it becomes R_2. Without the straddle (b = δ in the corner notch) FCMB holds with margin exactly jδ² (verified) — the straddle is the load-bearing move.

**C3. Second-moment route (E) is dead. Confidence: certain.**
On R_k: hits ∈ {0,k}, E[hits²] = k²/(k+1), autocorrelation Σ_{v≠0}|G∩(G−v)| = k(k−1)/(k+1), while g²/(1−s) = k/(k+1). Condition (E) fails by factor k (it implies FCMB, so it had to). Notably Paley–Zygmund is *tight* on R_k: P(hits≥1) = 1/(k+1) = g²/E[hits²]. On every family where FCMB holds that I tested (repeated-offset j-cells, no-straddle two-cell, N+2-truncations), condition (E) also holds — (E) and FCMB were never separated; they die together on the row/straddle families.

**C4. Exact diagnosis of what FCMB dropped, and the corrected identity. Confidence: certain (2-line algebra).**
g = E[hits] = (1−|Av|) + E[(hits−1)⁺], hence **Σd ≤ N ⟺ |Av| ≤ s + E[(hits−1)⁺]** per packing. FCMB deleted the multiplicity term E[(hits−1)⁺]; on R_k it equals (k−1)/(k+1) — *exactly* the violation margin (equality because R_k sits on the critical surface g+s=1). Any repaired sufficient condition must credit hit multiplicity; no bound of the form |Av| ≤ (function of s alone) can hold, since |Av| → 1 while s → 0 along rows as k → ∞.

**C5. Column tilings satisfy s = 1 identically (why they didn't refute FCMB). Confidence: certain.**
For T12 tilings (k = 2b(b−1)): s = b²/(k+b) + (b−1)²/(k+1−b) = b/(2b−1) + (b−1)/(2b−1) = 1 exactly, and |Av| = 1 (g=0). FCMB is tight there, tight on split-cells, proved at k=1 — all its calibration points sat on the tight set, while the row family (whose k=1 member IS the split cell) diverges from it for k ≥ 2. s scales as 1/(k+1) on rows but |Av| stays ≈ 1.

**C6. Row is optimal among single-band configurations; global searches find nothing worse. Confidence: high (partial proof + numerics).**
Granting g+s ≥ 1: if the gap lies in one row of cells, folding multiplicity ≤ k gives |π(G)| ≥ (1−s)/k, and the n-budget caps one-band deficit carriers at k+1 squares so s ≥ 1/(k+1); hence F ≥ −(k−1)/(k+1) with equality exactly at R_k. GAP: no proof for multi-band/tilted configs (unconditional floor is only F ≥ −(N−1)/(N+1)); but multistart Nelder-Mead with exact-feasibility repair (k=2: 26 starts incl. row/straddle/split/near-equal/tilted/random; k=3: 10 starts) converged to R_k from every violating basin and never went below −(k−1)/(k+1). Beating the row needs coherent gap in ≥2 cell-rows, i.e. ≥2 "extras" — the n-budget has only one.

**C7. Boundary probes (family 4): any packing containing a fully empty unit cell has |π(G)| = 1, so FCMB holds trivially (F = s > 0); the N+2-violator truncations are harmless. Violations require gap short in one coordinate everywhere. Confidence: certain (proof + numeric check, F = +0.75 at k=3).**

**C8. Tilt strictly repairs FCMB (family 2 dead for the adversary). Confidence: high (numeric).**
Row with bottom squares tilted by t (width-preserving shrink): F(t) = −1/3 + ≈3.4t (F = −0.164 at t=0.05, −0.020 at t=0.10, +0.208 at t=0.20). All optimizer runs drive tilts to 0 (|θ| < 1e−4 at optima). Tilted concentrators cannot compete: tilting bleeds Σd at rate Θ(kt) while saving at most O(t) of folded measure.

## COUNTEREXAMPLES AND CHECKS
- Rasterizer validated on split-cell a=0.37 at M=1200: F = 0.000000 exactly; overlap detector 0; exact SAT feasibility for all reported configs (tol 1e−9).
- R_2: g = 0.666667, |π(G)| = 0.333333, s = 0.333333, F = −0.333333; **independent direct shift-sampling |Av| = 0.666667** (bypasses the folding identity entirely). R_3: F = −0.500000, |Av| = 0.750000. Doubled-resolution recomputation confirms (M=1600).
- Straddle δ-family: F = −δ at four values of δ, feasible, Σd = N exactly.
- Repeated-offset (no straddle): F = jδ² to 6 decimals at (j,δ) = (2,0.15), (3,0.15), (2,0.3) — the FCMB-holding side of the orchestrator's family 1, margins exactly as hand-computed.
- Nothing violates the *conjecture* anywhere: every violating packing has Σd = N exactly and g+s = 1 exactly (structure identity holds to 0 residual throughout).

## DEAD ENDS
- **FCMB itself** — and with it the recommended attack ladder (i) AP-FCMB, (ii) sea+grain FCMB, (iii) general tilts: (i) is false, so (ii),(iii) are moot.
- **Second-moment/autocorrelation route (E)** — fails on the refuting family by factor k; PZ is tight there, so no moment-method sharpening of P(hits≥1) can recover it.
- **Folded-gap/dislocation heuristic (F)** — the row fault is a lattice-parallel dislocation with zero phase drift: gaps fold with multiplicity k. Near-critical gaps need NOT spread mod Z². Equidistribution-based formalizations should be shelved.
- Tilted concentrators and N+2-truncations as violation sources (C7, C8).

## BEST NEXT STEP
Retire FCMB and redirect: the correct per-packing target is the conjecture-equivalent **g ≥ 1 − s** itself (E[hits] ≥ 1−s; folding/measure-of-support was a false strengthening). The surviving structural fact from this refutation: on all known critical-surface packings (g+s=1: rows, straddles, split-cells, tilings), hits is supported on {0, m} with m = folding multiplicity, and PZ is tight — suggesting the right intermediate object is the *multiplicity function* mult(ω) on the torus, with target ∫mult = g ≥ 1−s and the extremals characterized by mult ∈ {0,m} bands. Recommend the proof agents pivot to the κ-route (T6 anti-concentration), which is untouched by this refutation, and that the orchestrator record R_k in the report as the canonical FCMB counterexample. Note the k=2 minimizer of F appears to be exactly R_2 (worth a short proof attempt of C6's multi-band gap, which would fully characterize how badly folding fails).

Files (all under `/private/tmp/claude-501/-Users-kylekabasares-Desktop-erdos-106/6b0597a9-48bd-4e8c-a957-7fc4a05f26d8/scratchpad/session2/F2/`): `WORKLOG.md` (full derivations incl. exact |Av| proof, straddle closed form, column-tiling s=1 identity, row-optimality argument), `fcmb.py` (validated rasterizer + direct |Av| sampler + exact SAT), `optimize.py`, `repair.py`, `triage.py`, logs `opt_k2.log`, `opt_k3.log`, best configs `best_k2.json`, `best_k3.json`.