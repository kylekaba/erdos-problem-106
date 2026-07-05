All checks pass (the deficit identity matches within MC error). I now have everything verified; writing the final report.

## CLAIMS

Throughout: scaled setting, `T = [0,k)^2` (half-open), `N = k^2`, a packing is `N+1` squares in `[0,k]^2` with pairwise disjoint interiors, sides `d_i`, excess `eps := sum d_i - N`. "Orientation" means angle mod 90°. `R_t` = rotation by `t`. For a lattice `L`, `L_p := L + p`.

---

### Claim 1 (Exact Budget Lemma — the complete rotation-friendly catalog of BKU-type budgets)

**Statement.** Let `L` be a lattice in the plane with `L ⊇ kZ^2`. Then for **every** shift `p ∈ R^2`,

```
|T ∩ (L + p)| = k^2 / covol(L)     (T = [0,k)^2 half-open).
```

In particular:

- **(a) Pythagorean unit frames.** Let `(a,b,c)` be a primitive Pythagorean triple, `cos θ = a/c`, `sin θ = b/c`. If `c | k`, then the rotated **unit-covolume** lattice `L_θ = R_θ Z^2` satisfies `|T ∩ (L_θ + p)| = N` for every shift `p`.
- **(b) Diagonal (checkerboard) lattice.** `D = Z^2 ∪ (Z^2 + (1/2,1/2)) = (1/√2)R_{45}Z^2` satisfies `|T ∩ (D+p)| = 2N` for every `k` and every `p`.
- **(c) Fine Pythagorean lattices.** `(1/c)R_θ Z^2 ⊇ Z^2 ⊇ kZ^2`, so `|T ∩ ((1/c)R_θZ^2 + p)| = c^2 N` for **every** `k` (no divisibility needed at this scale).
- **(d) Negative result for 45°.** The unit-covolume lattice `R_{45}Z^2` (the unique unit lattice under which 45°-tilted unit squares tile) is **never** container-exact, for any `k`.

**Proof.** Main statement: since `kZ^2 ⊆ L`, the lattice `L` is the disjoint union of `m = [L : kZ^2] = covol(kZ^2)/covol(L) = k^2/covol(L)` cosets `v_j + kZ^2`. The half-open square `T = [0,k)^2` is an exact fundamental domain of `kZ^2`, so each translated coset `v_j + p + kZ^2` meets `T` in exactly one point. Summing over cosets gives `m`, independent of `p`. ∎

(a): `R_θZ^2 ⊇ kZ^2` iff `kR_{-θ}e_1, kR_{-θ}e_2 ∈ Z^2` iff `c | ka` and `c | kb`; for a primitive triple `gcd(a,c) = gcd(b,c) = 1`, so this holds iff `c | k`. Covolume 1 gives budget `k^2 = N`. ∎

(b): `e_1 = (1/2)(1,1) + (1/2)(1,-1) ∈ D` and similarly `e_2`, so `D ⊇ Z^2 ⊇ kZ^2`; `covol(D) = 1/2`. ∎

(c): `e_1 = (1/c)R_θ(a,-b) ∈ (1/c)R_θZ^2`, similarly `e_2`. Covolume `1/c^2`. ∎

(d): By Poisson summation / direct Fourier, `p ↦ |T ∩ (L+p)|` is constant iff `\hat{1_T}(ξ) = 0` for all nonzero `ξ ∈ L^*`; since `\hat{1_T}` factors, this holds iff every nonzero `ξ ∈ L^*` has some coordinate in `(1/k)Z \ {0}`. For `L = R_{45}Z^2`, `L^* = R_{45}Z^2`, whose nonzero vectors have coordinates `((m-n)/√2, (m+n)/√2)`; `(m±n)/√2 ∈ (1/k)Z\{0}` is impossible (irrational), so **no** nonzero dual vector satisfies the condition; the count genuinely fluctuates. ∎

Numerically verified: (3,4,5)-lattice gives exactly 25 points for `k=5` and 100 for `k=10` over random shifts, and fluctuates `{48,49,50}` for `k=7`; `D` gives exactly `2k^2` for `k = 3,4,7`.

**Confidence: 0.98.**

---

### Claim 2 (Tilted BKU: the axis-parallel theorem extends verbatim to every Pythagorean orientation along divisibility subsequences)

**Statement.** Let `(a,b,c)` be a primitive Pythagorean triple, `θ = arctan(b/a)`, and `c | k`. Then any packing of `k^2+1` squares in `[0,k]^2`, **all** with sides parallel to the directions `θ, θ+90°` (arbitrary sizes), satisfies `sum d_i ≤ k^2`. (Unscaled: the common-orientation-θ analogue of `f(k^2+1) = k` holds, with the lower bound from the θ-rotated... the upper bound holds; `θ = 0` recovers BKU.)

**Proof.** Suppose `sum d_i > N`. Work in the θ-frame: coordinates `(x,y) = R_{-θ}(u,v)`. Each closed square becomes an axis-parallel box in these coordinates; replace it by the half-open box `[α_i, α_i+d_i) × [β_i, β_i+d_i)` (in θ-frame coordinates). Two same-frame axis boxes with disjoint interiors admit an axis separating line in that frame, and the half-open convention removes exactly the closed face on the separator, so the half-open squares are **pairwise disjoint sets**, all contained in the closed container `T̄ = [0,k]^2`.

Counting lattice: `Λ_p = R_θZ^2 + p`. For the half-open square `S_i`, in the θ-frame the lattice is `Z^2 + p'` (`p' = R_{-θ}p`) and

```
|S_i ∩ Λ_p| = p_i(x) · q_i(y),
```

where `p_i(x) = #{m ∈ Z : α_i ≤ m + x < α_i + d_i} ∈ {⌊d_i⌋, ⌈d_i⌉}`, `q_i(y)` likewise, `x, y` the θ-frame components of `p'`. Note `∫_0^1 p_i(x) dx = d_i`, and `|p_i - q_i| ≤ 1` (a square has equal sides), so `p_i q_i ≥ p_i + q_i − 1` (if `p,q ≥ 1` this is `(p−1)(q−1) ≥ 0`; if `p = 0` then `q ≤ 1` and the RHS is `≤ 0`).

Budget: by Claim 1(a), `|T ∩ Λ_p| = N` for every `p`. The closed container `T̄` may exceed this only when `Λ_p` meets `∂T̄`; the set `B` of such shifts is a countable union of translated segments, hence null.

Pigeonhole: let `A = {x : Σ_i p_i(x) ≥ N+1}`. If `λ(A) = 0` then `Σ p_i ≤ N` a.e. and `Σ d_i = ∫ Σ p_i ≤ N`, a contradiction; so `λ(A) > 0`. Similarly `λ(A') > 0` for the `q`-sums. By Fubini, for a.e. `x_0 ∈ A` the slice `B_{x_0}` is null; fix such `x_0`, then pick `y_0 ∈ A' \ B_{x_0}`. At the shift `(x_0,y_0)`:

```
N = |T̄ ∩ Λ| ≥ Σ_i p_i q_i ≥ Σ_i (p_i + q_i − 1) ≥ (N+1) + (N+1) − (N+1) = N+1,
```

a contradiction. ∎

**Remarks.** (i) Pythagorean angles are dense in `[0°, 90°]`; taking `k = K!` makes the set of exactly-covered orientations `{θ : c ≤ K}` dense as `K → ∞`. (ii) The hypothesis is sharp within this method: product structure with `|p−q| ≤ 1` forces a square lattice `R_θ((1/m)Z^2)`; containment of `kZ^2` then forces `cos θ` rational — Pythagorean angles are exactly the reachable ones (45° is unreachable at unit scale by Claim 1(d), and reachable only at scale `1/√2` where the method is void by Claim 6). (iii) This does **not** propagate through Singh's monotonicity (the substitution mixes orientations), so it is a structural restriction on counterexamples, not a bound on `f`.

**Confidence: 0.95.**

---

### Claim 3 (Every exact tiling of a rectangle by finitely many squares is axis-parallel; counterexamples need positive gaps)

**Statement.** If finitely many squares (positive sides, pairwise disjoint interiors) cover an axis-parallel rectangle `R` exactly, then every square is axis-parallel.

**Proof.** Suppose some tile is tilted. A tilted square has no horizontal side, so its minimum `y`-coordinate is attained at a unique vertex. Let `y_0` be the minimum, over all tilted tiles, of that value; let `S` be a tilted tile attaining it and `v = (x_0, y_0)` its lowest vertex. Every tilted tile lies in `{y ≥ y_0}`.

Local sector structure at `v`: only the (finitely many) tiles containing `v` meet a small disk `B(v, δ)`. If `v` were interior to another tile `T''`, then `int T''` would meet `int S` (every neighborhood of the vertex `v` contains interior points of `S`) — impossible; so `v` lies on the boundary of each tile containing it, and each such tile meets `B(v,δ)` in a closed circular **sector** of angle exactly 90° (`v` a vertex) or 180° (`v` interior to an edge), with bounding rays along that tile's edge directions. These sectors have disjoint interiors and cover `B(v,δ) ∩ R`.

Case `v ∈ int R`: the sectors partition the full circle. Their bounding rays, in cyclic order, have consecutive angular gaps in `{90°, 180°}` (each gap is one sector), hence **all ray directions are congruent mod 90°**. Now produce two incongruent rays: (1) `S` contributes rays along its edges, direction `≡ θ' (mod 90°)` with `θ' ≠ 0` (tilted). (2) Points `(x_0, y_0 − δ_n)`, `δ_n ↓ 0`, lie in tiles; by finiteness one tile `T'` contains a sequence of them, hence contains `v` and contains points with `y < y_0`. If `T'` were tilted its minimum `y` would be `< y_0`, contradicting minimality; so `T'` is axis-parallel and contributes rays `≡ 0 (mod 90°)` at `v`. Contradiction.

Case `v ∈ ∂R`: the sectors partition the angular region of `R` at `v` (180° at an edge point, 90° at a corner), whose bounding rays are axis-parallel (`∂R` is axis-parallel). Walking from one boundary ray to the other, gaps are again 90° or 180°, so all rays `≡ 0 (mod 90°)`, contradicting `S`'s tilted rays. ∎

**Corollary.** Any counterexample packing (`N+1` squares, `Σd_i > N`) (i) contains at least one tilted square (else BKU applies), hence (ii) by the theorem is **not** an exact tiling, so its gap area satisfies `G > 0`; combined with Cauchy–Schwarz, `0 < G ≤ [N(1−2ε) − ε^2]/(N+1) < 1 − 2ε`, where `ε = Σd_i − N ∈ (0, 1/2)`. (From `(N+ε)^2 ≤ (N+1)Σd_i^2 = (N+1)(N−G)`.)

**Confidence: 0.92.**

---

### Claim 4 (Exact deficit identity; the tilt mode is exactly neutral in expectation)

**Statement.** For a single square of side `d` at tilt `t ∈ [0°, 90°]`, define for shift `p` of the aligned unit lattice the *deficit* `δ(p) := p(x) + q(y) − 1 − |S ∩ (Z^2+p)|` (line counts of the two projections minus the BKU-claimed lower bound witness). Then **exactly**

```
∫_{torus} δ(p) dp = 2d(cos t + sin t) − 1 − d^2 = 2dτ(t) − (1−d)^2 ,   τ(t) := cos t + sin t − 1 ≥ 0.
```

Consequences: (i) axis-parallel squares have average **surplus** `(1−d)^2 ≥ 0`; a tilted near-unit square has average deficit `≈ 2dt > 0`. (ii) The extra pigeonhole mass a tilt makes available is `∫p − d = dτ(t)` per direction, i.e. `2 Σ d_i τ_i` in total — **identical, exactly, to the total average deficit** `Σ[2d_iτ_i − (1−d_i)^2]` up to the axis-parallel surplus term. Hence any argument that controls the tilted squares' counting deficit only through shift-averages gains exactly zero against the coherent-tilt mode: the cancellation is an identity, not an estimate. This is the sharp form of the "marginal global mode" trap.

**Proof.** `∫ p(x)dx =` projection width `= d(cos t + sin t)` (both projections of a square are equal), and `∫ |S ∩ (Z^2+p)| dp = area = d^2`. Subtract. ∎ (Monte Carlo verified at `(d,t) = (0.97, 0.2), (1, 45°), (0.9, 0.05), (1.05, 0.3)` to 3 decimals.)

**Confidence: 0.96.**

---

### Claim 5 (No-go: class-decoupled multi-frame counting can never beat Cauchy–Schwarz)

**Statement.** Partition any packing into orientation classes `C_1, …, C_J` (arbitrary angles `θ_j`, arbitrary `J`). For each `j` and every shift `p` (outside a null set) the pointwise inequality

```
F_j(p) := Σ_{i∈C_j}(p_i + q_i − 1) + Σ_{i∉C_j}|S_i ∩ (R_{θ_j}Z^2 + p)| − |T̄ ∩ (R_{θ_j}Z^2 + p)| ≤ 0
```

holds (product structure in-class, disjointness globally). Averaging each `F_j` over shifts and summing gives

```
2 Σd − (N+1) + (J−1)A ≤ JN,   A := Σ d_i^2 ,
```

and together with `(Σd)^2 ≤ (N+1)A` this yields a bound on `ε` that is `≥` the Cauchy–Schwarz bound for every `J` and every choice of angles: `J = 1` gives exactly `ε ≤ 1/2` (so **any common orientation**, including 45° and irrational ones, satisfies `Σd ≤ N + 1/2` for all `k` — but Cauchy–Schwarz already gives `ε < 1/2`), and `J → ∞` degenerates to Cauchy–Schwarz itself. The opposite endpoint — per-class pigeonhole with cross-terms dropped to 0 — is far worse (`ε ≲ (J−1)N/2`).

**Proof.** Averages: `E[p_i + q_i] = 2d_i` in-class; `E|S_i ∩ Λ_j + p| = d_i^2` off-class; `E|T̄ ∩ Λ_j+p| = area = N` for **any** unit-covolume lattice (exactness not needed after averaging). Summing over `j` with `Σ_j n_j = N+1`, `Σ_j (A − A_j) = (J−1)A` gives the display. Substituting `Σd = N + ε` and `A ≥ (N+ε)^2/(N+1)`: at `ε = 1/2` the left side already exceeds `JN` by `(J−1)/(4(N+1)) ≥ 0`, with equality analysis showing the implied bound on `ε` decreases from `1/2` (J=1) to the C–S value (`J→∞`), never below. For the dropped-cross-terms endpoint: per class `2⌈Σ_j⌉ − n_j ≤ N`; summing gives `2Σd ≤ JN + N + 1`. ∎

**Moral (the central Route-D finding):** the "+1" in BKU is a *global integrality* gain, extracted by a pigeonhole over the *whole* packing in *one* frame. Splitting into frames converts it into fractional garbage per class; averaging (which is what makes multiple frames compatible) provably reproduces the LP/Cauchy–Schwarz value. Budgets exist in every Pythagorean frame (Claim 1) but **cannot be shared**. Any Route-D success must couple classes through geometry (interfaces/gaps), not through counting alone.

**Confidence: 0.9** (rigorous for the two endpoint schemes stated; intermediate "conditioned" schemes are not formally excluded but face the measure-inflation trap).

---

### Claim 6 (No-go: fine commensurate lattices; 45° is the extremal hard angle)

**Statement.** (a) Using a single lattice of covolume `1/c^2` (`c > 1`, e.g. Claim 1(c)'s fine Pythagorean lattices, or `D` with `c = √2`) with the BKU chain gives at best `Σd ≤ N(c + 1/c)/2 + O(1)`, strictly worse than Cauchy–Schwarz for every `c > 1`; sharpened convexity inequalities `pq ≥ m(p+q) − m^2` only recover area information with integrality gain `O(1/c^2)`. (b) For a pure-45° packing counted against `D` (the only exact lattice with product structure for 45°, spacing `1/√2`, budget `2N`), the *optimal* linear inequality `pq ≥ α(p+q) − β` valid on the occurring range `p,q ∈ {1,2}` yields `Σd ≤ (3/(2√2))N + O(1) ≈ 1.0607N` — an LP-optimality computation over `(α,β)`: the per-square shortfall is exactly `(√2 d − 1)^2 ≈ 0.172` at `d = 1`.

**Proof.** (a) Budget `c^2N`; pigeonhole `Σp ≥ ⌈cΣd⌉`; chain `c^2N ≥ 2cΣd − (N+1)`. Minimum of `(c^2+1)/(2c)` is at `c=1`. For the refined inequality with `m_i = ⌊cd_i⌋`, the claimed terms telescope to `c^2`-weighted area quantities and the ceiling gain is one lattice point against a budget of size `c^2N`. (b) Feasibility constraints at `(p,q) ∈ {(1,1),(1,2),(2,2)}`: `2α−β ≤ 1`, `3α−β ≤ 2`, `4α−β ≤ 4`; minimizing `(2+β)/(2√2 α)` over the feasible region gives value `3/(2√2)` on the whole edge between `(α,β) = (1,1)` and `(2,4)`. ∎

**Corollary (important negative).** The **common-45° case is not resolved by any counting in this catalog**: `R_{45}Z^2` is never container-exact (Claim 1(d)); `D` is exact but fine (loss `0.172` per square); averaging gives only `N + 1/2` (Claim 5). Best known for pure-45° packings remains Cauchy–Schwarz. 45° is provably the orientation most distant from the Pythagorean frames at bounded height — the hardest single angle for lattice methods.

**Confidence: 0.93.**

---

### Claim 7 (Fragility ledger: one tilted square voids the BKU surplus)

**Statement.** (a) A **unit** square at 45° centered at a deep hole (`(1/2,1/2) + Z^2`) has `p = q = 2` and contains **0** lattice points: pointwise deficit `3` — a single square can overspend the "+1" three times over (verified numerically; the prompt's diamond example had deficit 2, the truth is worse). (b) If all but `M` squares are axis-parallel, the class-BKU argument gives only `ε ≤ Σ_{tilted}d_i − M/2 + 1/2`, which for `M ≥ 1` is weaker than Cauchy–Schwarz (`ε < 1/2`) whenever any tilted square has `d_i ≥ 1`: **the case `M = 1` is already open beyond C–S.** (c) (Essentially known = trap #3, stated for completeness with proof:) replacing every tilted square by its concentric inscribed axis-parallel square (side `d_i/(cos t_i + sin t_i)`, inside the old footprint, so the packing property is preserved) and applying BKU yields the rigorous constraint `ε ≤ Σ_i d_i τ(t_i)/(1+τ(t_i))`: counterexamples must carry tilt-weighted side mass `Σ d_i t_i ≳ ε`.

**Proof.** (a) Direct check: `(±1/2, ±1/2)`-neighbors have `|x−c_1|+|y−c_2| = 1 > √2/2`; projections have width `√2`, so both projections meet the lines through `0` and `1`. (b) Pigeonhole the axis class alone: `N ≥ 2⌈Σ_0⌉ − (N+1−M)` gives `Σ_0 ≤ N + (1−M)/2`; add `Σ_{tilted} d_i`. (c) As stated; the inscribed square is inside the original, so disjointness holds, and BKU applies to the all-axis result. ∎

**Confidence: 0.92.**

---

### Claim 8 (D4 majority-ownership matching: dead as formulated)

(a) A unit 45° square centered at a **cell center** owns `1 − 4(√2/2 − 1/2)^2 = 2√2 − 2 + ... = 0.8284` of that cell (> 1/2), but centered at a **lattice point** it splits into four pieces of exactly `1/4` each; an axis-parallel unit square at a lattice point does the same. So "every big square majority-owns a cell" fails at some shifts for *every* orientation — only shift-existence versions could survive, and that is BKU again. (b) Structurally, majority-ownership matching bounds the **number** of squares by the number of cells (`≤ (k+1)^2`, with `~2k` boundary slack), and is blind to the side-length objective; the side sum enters BKU through multiplicity `p·q ≥ 2`, which is precisely what ownership discards. Verdict: no theorem here without reinventing the multiplicity count. **Confidence: 0.85.**

---

## COUNTEREXAMPLES AND SANITY CHECKS

All numerical (scripts in scratchpad, seeds fixed):

1. **Claim 1(a):** `(3,4,5)` rotated unit lattice: exactly `k^2` points in `[0,k)^2` for 30 random shifts at `k = 5, 10`; fluctuates `{48,49,50}` at `k = 7` — confirms both exactness and the necessity of divisibility at unit covolume.
2. **Claim 1(b):** diagonal lattice `D`: exactly `2k^2` for `k = 3, 4, 7`, random shifts.
3. **Claim 2 mechanics:** 2000 random θ-tilted squares vs `R_θZ^2` (`θ = arctan(3/4)`): count `= p·q` with `p,q ∈ {⌊d⌋,⌈d⌉}` in every trial.
4. **Claim 4:** deficit identity vs Monte Carlo (400k shifts at the tightest case): `0.34735` vs predicted `0.34585` — within noise; three other `(d,t)` pairs match to ~3 decimals.
5. **Claim 7(a):** deep-hole diamond: count 0, `p = q = 2`, deficit 3.
6. **Claim 8:** piece areas `0.8284` and `4 × 1/4` confirmed.
7. **Cross-checks of the no-gos:** Claim 5 at `J=1` reproduces `N + 1/2 ≈` C–S ≈ LP value `k + 1/(2k+1)` (scaled `ε → 1/2`) — consistent with the known LP-gap warning, as it must be.

---

## DEAD ENDS

1. **Multi-frame budget sharing (D1's main hope).** Exact budgets exist in every Pythagorean frame with `c | k` (Claim 1), and along `k = K!` the covered orientations are dense. But a frame's budget is consumed by *all* squares while honest lower bounds exist only for its own class; keeping cross-terms as `≥ 0` loses `~A ≈ N` per extra frame, and keeping them as averages provably ties Cauchy–Schwarz (Claim 5). Two-scale schemes (coarse aligned + one adapted frame) are the `J = 2` case of Claim 5: dead.
2. **Rational approximation of arbitrary angles.** Transferring a common-θ packing to a nearby Pythagorean θ′ by a rigid global rotation costs `~k^2·|θ−θ′|` in side length, so one needs `|θ−θ′| ≲ 1/k^2`; but exactness demands hypotenuse `c | k`, hence `c ≤ k`, and rational points of height `≤ k` on the circle have typical spacing `~1/k`. Off by a factor `k` — structurally, not marginally. Fine lattices dodge the divisibility (Claim 1(c)) but are void by Claim 6(a).
3. **Signed/hybrid budgets** (e.g. `δ_{Z^2} + δ_{L_θ} − Leb`, budget `N` exact): superadditivity over disjoint squares fails on the negative part (the uncovered region's negative mass is unaccounted). Positive measures are forced; positive + rotation-invariant + shift-exact ⇒ Lebesgue ⇒ area ⇒ C–S. This is the cleanest statement of why Route D needs *orientation-adapted* (hence class-coupled) budgets.
4. **D3 (Dehn/Kenyon).** Dehn-type invariants are `Q`-linear functionals on side lengths — wildly discontinuous; a near-tiling with gap `G > 0` has continuum-free parameters that scramble any such functional. Kenyon's electrical correspondence needs the exact contact structure. Nothing survives `G > 0`; and `G = 0` is already fully handled by Claim 3 + BKU. Abandoned quickly, as instructed.
5. **Local wedge-waste around a tilted square (my own candidate lemma, killed).** I attempted: "a `t`-tilted square amid an axis-parallel near-tiling forces local gap `~d^2 t`" (which, combined with Claim 7(c), would have given `ε ≤ 1/4` for `M = 1`). False as stated: a neighbor unit square placed at a bounding-box corner covers the entire corner triangle (legs `d sin t, d cos t ≤ 1`) while touching `S` only along its edge — zero forced gap. Any interface-waste lemma must be global (grain-boundary-length–based), not per-corner.
6. **D4 matching** — see Claim 8: counts cardinality, not side length.
7. **Conditioned pigeonholes** (choose shifts in the good set of one class, control other classes' deficit there): the good set has measure as small as `~ε`, deficits inflate by `1/ε`; Claim 4 shows the first moment cancels identically, so only pointwise/joint-shift structure can work — none found with honest constants.

---

## BEST NEXT STEP

**Attack the pure-45° case: prove `Σ d_i ≤ k^2` (or anything strictly below Cauchy–Schwarz) for `k^2+1` squares all tilted at exactly 45° in `[0,k]^2`.**

Why this is the right target: it is the *minimal* configuration this entire triage leaves open — a single common orientation, full product structure available, and yet every exact-budget lattice fails (Claim 1(d), Claim 6(b)); the best known bound is still Cauchy–Schwarz. Any rotation-friendly budget that cannot crack pure-45° cannot crack the general problem; conversely a solution here would be the first counting result beyond C–S with rotation, and its mechanism (necessarily coupling the pigeonhole to container-boundary discrepancy) is exactly the missing lemma identified in the problem statement.

Concrete plan: rotate to the squares' frame. The problem becomes: axis-parallel BKU inside a **diamond container** `D_k` (45°-rotated square of side `k`). The pointwise inequality `Σ(p_i + q_i − 1) ≤ |D_k ∩ (Z^2+p)|` holds for every shift (Claim 5, `J=1`), `E_p|D_k ∩ (Z^2+p)| = k^2` exactly, and the entire difficulty is the container count's fluctuation. But this fluctuation is now *completely explicit*: the four edges have slope `±1`, so the row lengths `ℓ_j` of `D_k` differ by exactly 2 from row to row — all row-rounding phases are **perfectly correlated** and governed by just two parameters (the phases of `x+y` and `x−y`). The task reduces to: show the two pigeonhole functionals `Σp_i(x)`, `Σq_i(y)` (which depend on the packing) and the two-phase container discrepancy `|D_k ∩ Z^2_p| − k^2` (which does not) can be jointly optimized — a 2-parameter problem with an explicit, piecewise-linear, mean-zero discrepancy whose positive spikes live on measure-`O(1/k)` phase sets. Sub-goal worth proving first: for every packing there exists a shift with `Σp_i(x) + Σq_i(y) ≥ 2⌈Σd⌉` **and** container count `≤ k^2 + C` for an absolute constant `C` — even `C = o(k)` would be the first nontrivial control of trap #2, and `C < 2ε` closes the pure-45° case via the chain in Claim 2.