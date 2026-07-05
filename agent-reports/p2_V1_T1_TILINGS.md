# Verification report — Route C (report_ROUTE_C_CONSTANT.md), Claims 1, 5, 6, 7

Numerics: `/private/tmp/claude-501/-Users-kylekabasares-Desktop-erdos-106/6b0597a9-48bd-4e8c-a957-7fc4a05f26d8/scratchpad/verify_c.py` (all checks quoted below reproduce from it).

---

## Claim 5 (Theorem T1) — PRIORITY

**VERDICT: CORRECT** (one garbled display; substance fully verified).

Step-by-step audit:

1. **Inscribed square.** The concentric axis-parallel square of side `a = d/(c+s)` lies in the tilted square: a world corner `(±a/2, ±a/2)` rotated into the square's frame has coordinates `(±(a/2)(c+s), ±(a/2)(c−s))` (up to sign pattern), both `≤ (a/2)(c+s) = d/2` in absolute value; convexity finishes. Proof correct. Adversarial machine check: 20,000 random `(d, θ_raw)` with **unfolded** `θ_raw ∈ [0, π)`, folding applied afterwards — max corner excess `4.4e−16`. Note `a` is also the *maximal* concentric axis-parallel inscribed square (the corner constraint is tight), so this step cannot be improved.
2. **Orientation convention.** Sound. `cosθ + sinθ` is invariant under `θ ↦ θ + π/2` and `θ ↦ π/2 − θ`, so `d/(c+s)` is well-defined on the folded angle `θ ∈ [0, π/4]` regardless of which side's direction is measured. The chain's last link `c+s−1 ≤ θ` needs the folded representative and holds there (`h(θ)=θ−(c+s−1)`, `h(0)=0`, `h'=1−c+s ≥ 0`; numerically `max[(c+s−1)−θ] = 0.0` on `[0,π/4]`). (It in fact also holds for unfolded `θ ∈ [0,π/2]` since `h' = 1−c+s ≥ 0` there too, but folded is the sharper and intended form.) T1 as stated is convention-correct.
3. **Inscribed family is a legal BKU input.** Each inscribed square sits inside its host, hence inside `[0,k]²`, interiors disjoint. ✓
4. **BKU generality and scaling.** The arXiv:2411.07274 theorem is about `g(n)` for arbitrary packings of axis-parallel squares — **no side-length restriction** (confirmed against the abstract; `g` is defined over all packings). Independently, the counting proof itself works verbatim for arbitrary `d_i`: `∫₀¹ p_i dx₀ = d_i` for any size; `p_i, q_i ∈ {⌊d_i⌋, ⌈d_i⌉}` (at integer `d_i`, `∈ {d_i, d_i+1}`), so `|p_i−q_i| ≤ 1` always; `c_i = p_i q_i` needs only axis-parallelism; `p_i q_i ≥ p_i+q_i−1` holds including the `p_i = 0` case (then `q_i ≤ 1` by `|p−q|≤1`, so `q_i − 1 ≤ 0`); the pigeonholed shift sets `{Σp_i ≥ N+1}`, `{Σq_i ≥ N+1}` have positive 1-D measure, so a generic product pair avoids the measure-zero shifts where a lattice point sits on a shared boundary (no double counting). **Scaled form is right:** `g(k²+1) = k` in `[0,1]²` scales linearly to "total side ≤ k² for k²+1 axis-parallel squares in `[0,k]²`".
5. **Chain.** `k²+ε = Σd_i = Σd_i/(c_i+s_i) + T ≤ k² + T`; `1 − 1/(c+s) = (c+s−1)/(c+s) ≤ c+s−1 ≤ θ` (both inequalities machine-checked to 0 violation). ✓ Corollary (i) (`f(n) ≤ g(n) + T_opt`, so a conjecture-counterexample needs `Σd_iθ_i ≥ ε`) and (ii) are immediate. ✓

**Fix needed (cosmetic):** the first display `Σ d_i/(c_i+s_i) ≤ k·g(n/ )|_scaled` is garbled. Corrected general statement: *for any packing of `n` squares (any orientations) in `[0,k]²`, `Σᵢ d_i/(c_i+s_i) ≤ k·g(n)`* (unscale the inscribed family by `1/k` and apply the definition of `g`). The `n = k²+1` case as printed is correct.

**Sharpened forms (proved):**
- **Two-sided tilt-cost comparability.** `c+s` is concave on `[0,π/4]` (second derivative `−(c+s) < 0`), so it lies above its chord: `c+s−1 ≥ (4(√2−1)/π)·θ ≈ 0.5274·θ` (machine-checked, violation ≤ 2.2e−16). With `c+s ≤ √2`:
  `(4(√2−1)/(π√2))·Σd_iθ_i ≤ T ≤ Σd_iθ_i`, constant `≈ 0.3729`. So `T ≍ Σd_iθ_i` within factor `2.69`; the "tilt-heavy regime" `T > 1/2 − c` can equivalently be phrased as `Σd_iθ_i > 1.34(1/2−c)` etc.
- **Excess-`c` version.** Since BKU give `g(k²+2c+1) = k + c/k`, the same one-line argument yields: any `k²+2c+1` squares (any orientations) in `[0,k]²` satisfy `Σd_i ≤ k² + c + T`.

---

## Claim 6 (Theorem T2, Wall Lemma)

**VERDICT: CORRECT** (one imprecision in the "Consequence" sentence).

Audit:
- `R = {(x,y): 0 ≤ y < φ(x)}` meets no square (any point of the closed union on line `x` has `y ≥ φ(x)`), `R ⊆ T` (convention `φ = k` off all projections, `φ ≤ k` on them), so `∫₀ᵏ φ ≤ G`. ✓
- **Lower-envelope geometry.** For folded `θ ∈ (0,π/4]` the boundary of a square visible from below over its full projection is exactly the two edges adjacent to the lowest vertex, with absolute slopes `tanθ` and `cotθ` (which side is which depends on orientation — the statement's `|x−v_i|` covers both). `cotθ ≥ tanθ` on `(0,π/4]` gives `f_i(x) ≥ y_i + tanθ|x−v_i|` on the whole projection, and `A_i ⊆ proj(S_i)`. ✓
- **Attack at θ = 0** (lowest point a full edge): `tan 0 = 0`, bound degenerates to `y_i|A_i|`, `f_i = y_i` on the projection — holds, `v_i`-ambiguity harmless. **Attack at θ = π/4:** slopes are both 1, `f_i = y_i + |x−v_i|` exactly, and if `A_i` is an interval centered at `v_i` the bathtub bound is an equality — **T2 is tight at θ = π/4**; no counterexample possible from this direction.
- **Bathtub step.** `∫_A |x−v| dx ≥ |A|²/4` for any measurable `A`: sublevel sets of `|x−v|` are intervals centered at `v`; standard rearrangement. ✓ Constants check: worst case interval gives exactly `L²/4`.
- Summation over the measurable partition `{A_i} ∪ {A_∅}` of `[0,k]`: ✓ (tie-breaking to lowest index keeps measurability).
- **Numeric adversarial test** (4 tilted squares, `θ ∈ {0, 0.15, 0.3, π/4}`, in `[0,3]²`, disjointness verified by sampling): LHS `2.327 ≤ ∫φ 2.499 ≤ G 6.06`. ✓
- **Wall-row sanity check reproduced:** per unit wall length, T2 gives `(tanθ/4)(c+s)`, true waste is `sc/(c+s)`; `(tanθ/4)(c+s) ≤ sc/(c+s) ⟺ (c+s)² ≤ 4c² ⟺ s ≤ c` ✓ on `[0,π/4]` (numeric: 0.0131 ≤ 0.0476 at θ=0.05; equality 0.3536 = 0.3536 at π/4). Report's consistency claim confirmed.

**Fix (imprecision):** in the Consequence, "`Σ|A_i| = k`" should read `Σ|A_i| = k − |A_∅|` with `|A_∅| ≤ G/k`; in the critical regime `G < δ₀` this is `Σ|A_i| ≥ k − δ₀/k`. Conclusions unchanged.

**Sharpened form (proved, factor up to 2 in exactly the dangerous small-θ regime):** replace `tanθ_i/4` by `s_i c_i/2`:
`Σᵢ ( y_i|A_i| + (s_i c_i/2)|A_i|² ) + k|A_∅| ≤ G.`
*Proof:* use the true two-slope wedge `g(x) = y_i + tanθ_i(x−v_i)_+ + cotθ_i(v_i−x)_+` (or mirrored), which equals `f_i` on the projection; `g` is unimodal, so the bathtub minimizer over `|A| = L` is a sublevel interval, and minimizing `(cotθ·t² + tanθ·(L−t)²)/2` over the split `t` gives `t* = L·tan/(tan+cot)` and value `L²/(2(tanθ+cotθ)) = (s c/2)L²`. Machine-checked: min over `t` matches `(sc/2)L²` to 6 digits at `θ = 0.1, 0.4, π/4`; and `sc/2 ≥ tanθ/4 ⟺ c² ≥ 1/2` ✓ on `[0,π/4]`, equality only at `π/4`. The sharpened inequality also passed the 4-square numeric test (`2.428 ≤ 2.499`) and the wall-row check (`(sc/2)(c+s) ≤ sc/(c+s) ⟺ (c+s)² ≤ 2` ✓, tight at π/4).

---

## Claim 7 (column-tiling family)

**VERDICT: CORRECT WITH FIXES** (theorem and refutation stand; two errors in constants/commentary).

**Arithmetic for b = 2 (k = 4), exact rationals:** widths `4/6 = 2/3`, `4/3`, plus `k−2 = 2` columns of width 1; widths sum `2/3 + 4/3 + 1 + 1 = 4 = k` ✓. Piece count `6 + 3 + 2·4 = 17 = k²+1` ✓. Column heights: `6·(2/3) = 4`, `3·(4/3) = 4`, `4·1 = 4` ✓ — genuine exact tiling. **Total side sum (computed): `6·(2/3) + 3·(4/3) + 8·1 = 4 + 4 + 8 = 16 = k²` scaled, i.e. exactly `k = 4` unscaled** ✓, so `ε = 0`, `G = 0`. `Σd_i² = 8/3 + 16/3 + 8 = 16` ✓, `V = 16 − 17·(16/17)² = 16/17` ✓ matches identity (∗). Exact-fraction verification also passed for `b = 3, 5, 8` (`k = 12, 40, 112`): pieces `= k²+1`, total side `= k²`, `G = 0`, `G+V = k²/(k²+1)` exactly. General identities `k/(k+b) + k/(k+1−b) = 2 ⟺ k = 2b²−2b` and `(k+b)+(k+1−b)+(k−2)k = k²+1` check algebraically.

**Refutation of "no exact tiling by k²+1 near-unit squares" (L∞): CONFIRMED.** Sharper than stated, in fact: the two non-unit sides are exactly `1 ∓ 1/(2b−1)` and `(2b−1)² = 2k+1`, so **all sides lie in `[1 − (2k+1)^{−1/2}, 1 + (2k+1)^{−1/2}]` exactly** (`k=4`: `1±1/3`; `k=12`: `1±1/5`; `k=40`: `1±1/9`; `k=112`: `1±1/15` — all machine-confirmed). Hence for every `a > 0`, every `k = 2b(b−1)` with `2k+1 > a^{−2}` admits an exact tiling of `[0,k]²` by `k²+1` axis-parallel squares with all sides in `(1−a, 1+a)`: route (a) is dead as an absolute-`a` statement. Moreover the special form of `k` is no escape hatch: allowing **three** perturbed columns (counts `k+m₁, k+m₂, k+m₃`, `Σm_j = 1`, `Σ1/(k+m_j) = 3/k ⟺ k² + 2e₂k + 3e₃ = 0`) yields exact `(k²+1)`-tilings for many more `k` — machine-verified examples: `k = 3, 9, 18, 30, 45, 63, 108, …` (e.g. `k=18`, `m = (−3,2,2)`: columns of counts 15, 20, 20 plus 15 unit columns; 325 = 18²+1 pieces, total side 324). The admissible `k`-set is dense enough that only the `L²` quantity `V` carries rigidity content, exactly as the report concludes.

**Errors to fix:**
1. **Side-range constants (Statement).** The claimed window `[1 − √(2/k)(1+o(1)), 1 + √(1/(2k))(1+o(1))]` is asymmetric, but the true deviations are symmetric and both equal `1/√(2k+1) = √(1/(2k))(1+o(1))`. The statement is true only as a (loose) containment; the lower constant `√(2/k)` overstates the deviation by a factor 2. Corrected statement: *all sides in `{1 − (2k+1)^{−1/2}, 1, 1 + (2k+1)^{−1/2}}`*.
2. **Consequence (ii): "variance budget spread over Θ(k^{3/2}) squares" is wrong.** The non-unit squares number `(k+b) + (k+1−b) = 2k+1 = Θ(k)` (9 at `k=4`, 25 at `k=12`, 81 at `k=40` — verified), each with deviation `1/√(2k+1)`, contributing `(2k+1)·(2k+1)^{−1} = 1 ≈ V` ✓. `Θ(k^{3/2})` squares at deviation `Θ(k^{−1/2})` would give `V ≈ √k`, contradicting the verified `V = k²/(k²+1) < 1`. Fix: `Θ(k)` squares. The structural moral (spread vs. concentrated variance; both patterns must be handled) survives unchanged.

Consequence (iii) ("new extremal configurations for BKU"): the configurations are verified equality cases of `g(k²+1) = k` far from the grid; novelty not verifiable from here, but the mathematical content is correct.

---

## Claim 1 (exact identity and reformulation)

**VERDICT: CORRECT WITH FIXES** (identity exact; the stated "equivalence" in (ii) holds only up to `O(1/k²)` in `δ₀`, which the proof half-acknowledges in a garbled sentence).

- **Identity (∗):** `G + V = k² − Σd_i² + Σd_i² − nm² = k² − (k²+ε)²/(k²+1)`, numerator `k²(1−2ε) − ε²`. Algebra correct; machine-checked to `1e−15` on random packless data (the identity needs no geometry beyond `G`'s definition). The Remark (G+V is a function of ε alone; monotone decreasing in ε) is correct and important.
- **(i):** `G+V ≥ 0 ⟺ k²+ε ≤ √(k²(k²+1)) ⟺ f(k²+1) ≤ √(k²+1)` — exactly Cauchy–Schwarz. ✓
- **(ii):** Forward direction is exact and is the direction C2 needs: `G+V ≥ δ₀` for all packings `⟹ k²(1−2ε)−ε² ≥ δ₀(k²+1) ≥ δ₀k² ⟹ ε ≤ (1−δ₀)/2`. ✓ **The converse as literally written is false:** from `ε ≤ (1−δ₀)/2` one gets `k²(1−2ε) − ε² ≥ δ₀k² − 1/4`, and `δ₀k² − 1/4 ≥ δ₀(k²+1)` never holds; the proof's line "`≥ δ₀k² − 1/4 ≥ δ₀(k²+1)` for `k² ≥ (1/4+δ₀)/(1−δ₀)·`—" is garbled and not repairable as an exact equivalence at fixed `δ₀`.
- **Corrected exact statement:** since `G+V` is strictly decreasing in `ε`, "every packing has `G+V ≥ δ₀`" is *exactly* equivalent to `ε* ≤ ε(δ₀) := √(k⁴ + (1−δ₀)k² − δ₀) − k²`, and `(1−δ₀)/2 − (1−δ₀)²/(8k²) ≤ ε(δ₀) < (1−δ₀)/2`. So: `G+V ≥ δ₀` everywhere `⟹ ε* < (1−δ₀)/2` (clean); conversely `ε* ≤ (1−δ₀)/2 ⟹ G+V ≥ δ₀ − (δ₀ + 1/4)/(k²+1)` everywhere. The equivalence "with `c = δ₀/2`" is correct after replacing `δ₀` by `δ₀ ± O(1/k²)`, harmless for the C2 target at large `k` (or by absorbing into `c`). This is a fix of the proof text, not of the claim's use downstream — every later use is of the exact forward direction.

---

## Summary

| Claim | Verdict | Action |
|---|---|---|
| 1 | CORRECT WITH FIXES | (ii)-converse needs `δ₀ ± O(1/k²)`; use exact monotone form `ε(δ₀) = √(k⁴+(1−δ₀)k²−δ₀) − k²`. Forward direction (the one C2 uses) exact. |
| 5 (T1) | CORRECT | Fix garbled general-`n` display to `Σd_i/(c_i+s_i) ≤ k·g(n)`. BKU generality (arbitrary sides) and scaling confirmed; convention confirmed. Sharpened: `0.3729·Σd_iθ_i ≤ T ≤ Σd_iθ_i`; excess-`c` version `Σd_i ≤ k² + c + T` for `k²+2c+1` squares. |
| 6 (T2) | CORRECT | Tight at θ=π/4; θ=0 attack fails. Fix `Σ|A_i| = k` → `≥ k − G/k`. Sharpened constant proved: `tanθ_i/4 → s_ic_i/2` (up to ×2 better at small tilt, the gentle-grain regime). |
| 7 | CORRECT WITH FIXES | All arithmetic exact-verified (b=2: 17 pieces, total 16 = k² scaled = k unscaled, G=0, V=16/17). Refutation of L∞ route (a) CONFIRMED and sharpened: sides exactly `1 ± (2k+1)^{−1/2}`; extra admissible `k` (3, 9, 18, 30, 45, …) via 3-column variants. Errors: lower side-constant `√(2/k)` loose by ×2; "Θ(k^{3/2}) squares" wrong → `2k+1 = Θ(k)`. |

No claim among the four is FLAWED in substance; T1's reduction (excess ≤ tilt cost, so only the tilt-heavy regime `T > 1/2−c` remains for C2) is sound and can be relied on by other routes, with the two-sided bound `T ≍ Σd_iθ_i` (factor 2.69) available if they prefer the `Σd_iθ_i` normalization.