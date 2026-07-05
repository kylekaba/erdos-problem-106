# V4 VERIFICATION REPORT — Route D Claims 1, 2, 5; Route E Claim 6

Numerical checks: `/private/tmp/claude-501/-Users-kylekabasares-Desktop-erdos-106/6b0597a9-48bd-4e8c-a957-7fc4a05f26d8/scratchpad/v4_checks.py` (all pass; details inline).

---

## Route D, Claim 1 (Exact Budget Lemma)

**VERDICT: CORRECT** (one cosmetic caveat in (d), non-load-bearing).

**Coset argument (main statement).** Verified line by line. `kZ² ⊆ L` with both full-rank ⇒ index `m = [L : kZ²]` is finite and equals `covol(kZ²)/covol(L) = k²/covol(L)` (standard). `T = [0,k)²` is an exact fundamental domain of `kZ²` (tiles the plane, one representative per coset). Hence each of the `m` translated cosets `v_j + p + kZ²` meets `T` in exactly one point, for *every* `p`, giving `|T ∩ (L+p)| = m`. Airtight; no genericity needed. Adversarial attempt: the only way to break this is a lattice not containing `kZ²` (e.g. `R_45Z²`) — which is exactly part (d).

**(a)** `R_θZ² ⊇ kZ²` ⟺ `kR_{-θ}e_1, kR_{-θ}e_2 ∈ Z²` ⟺ `c | ka` and `c | kb`. For a primitive triple, `gcd(a,c) = gcd(b,c) = 1` (a common prime `p | a, c` would divide `b² = c² − a²`, hence `b`, contradicting `gcd(a,b)=1`), so the condition is `c | k`. Covolume 1 ⇒ budget `N`. Correct. **Numerics:** (3,4,5) lattice, 200 random shifts: exactly 25 for `k=5`, exactly 100 for `k=10`; fluctuates `{48,49,50}` for `k=7`. Matches.

**(b)** `D = {(x,y) : 2x,2y ∈ Z, x+y ∈ Z} = (1/√2)R_45Z²` verified; `D ⊇ Z² ⊇ kZ²`, covol `1/2`, budget `2N`. **Numerics:** exactly `2k²` at `k = 3, 4, 7`, 200 random shifts each. Correct.

**(c)** `c·R_{-θ}e_1 = (a,-b) ∈ Z²`, `c·R_{-θ}e_2 = (b,a) ∈ Z²`, so `(1/c)R_θZ² ⊇ Z² ⊇ kZ²`; covol `1/c²`, budget `c²N`, no divisibility. Correct.

**(d)** The assigned question: is the criterion "count constant iff `hat(1_T)` vanishes on `L*\{0}`" correctly applied?

- The factorization is right: `hat(1_T)(ξ) = ∏_{j=1,2} ∫_0^k e^{-2πiξ_j t}dt`, and the 1-D factor vanishes iff `kξ_j ∈ Z\{0}`, i.e. iff `ξ_j ∈ (1/k)Z\{0}`. So `hat(1_T)(ξ) = 0` iff **some** coordinate of `ξ` lies in `(1/k)Z\{0}`. The report's criterion is stated correctly.
- Direction actually used: **only** "count constant ⇒ all nonzero dual coefficients vanish." This is sound: `φ(p) = Σ_{λ∈L}1_T(λ+p)` is a bounded measurable function on `R²/L` whose Fourier coefficients are `(1/covol L)·conj(hat(1_T)(ξ))`, `ξ ∈ L*`; if `φ` is constant everywhere it is constant a.e., so all nonzero-frequency coefficients vanish. To conclude non-constancy for `R_45Z²` one needs **one** nonzero `ξ ∈ L* = R_45Z²` with nonvanishing hat. The report proves the stronger fact that *every* nonzero dual vector has nonvanishing hat (coordinates `(m∓n)/√2` are irrational or zero, never in `(1/k)Z\{0}`) — more than needed, but valid. E.g. `ξ = R_45(1,1) = (0,√2)`: factor at coordinate `0` is `k ≠ 0`, factor at `√2` is nonzero since `√2k ∉ Z` (numerically `|factor| = 0.155, 0.050, 0.097` at `k = 3,5,10`).
- Cosmetic caveat: the converse direction ("vanishing on all of `L*\{0}` ⇒ constant for EVERY `p`") only yields a.e.-constancy for a general `L` via Fourier; everywhere-constancy in the positive parts (a)–(c) is instead supplied by the coset argument, which is what the report uses. So the "iff" as literally written should be read "constant a.e."; nothing in the report depends on the unused half. **Numerics:** `R_45Z²` counts in `[0,k)²` fluctuate, e.g. `{24,25,28,32}` at `k=5`, `{98,…,113}` at `k=10`. Confirmed.

---

## Route D, Claim 2 (Pythagorean-frame BKU)

**VERDICT: CORRECT.** Every step of the chain survives adversarial scrutiny.

1. **Half-open disjointification in the rotated frame.** Two axis-parallel (in the θ-frame) closed boxes with disjoint interiors: if both coordinate projections overlapped in intervals of positive length, the interiors (products of open intervals) would intersect. So some coordinate projection overlaps in at most a point, giving a frame-axis separating value `s` with box 1 in `{u < s}` after half-opening and box 2 in `{u ≥ s}`. Hence the half-open boxes `[α_i, α_i+d_i) × [β_i, β_i+d_i)` are pairwise disjoint **sets**, contained in `T̄ = [0,k]²`. Sound. (This is exactly where a mixed-orientation packing would break — separating axis need not be a frame axis — so the common-orientation hypothesis is genuinely load-bearing.)
2. **Product structure.** In frame coordinates the lattice `R_θZ² + p` becomes `Z² + p'`, `p' = R_{-θ}p`, and the count over a half-open frame-aligned box factorizes as `p_i(x)·q_i(y)` with `p_i, q_i ∈ {⌊d_i⌋, ⌈d_i⌉}` and `∫_0^1 p_i(x)dx = d_i`. **Numerics:** 3000 random (side, position, shift) trials: count `= p·q` and both in `{⌊d⌋,⌈d⌉}` in all 3000.
3. **`pq ≥ p+q−1`.** If `p,q ≥ 1`: `(p−1)(q−1) ≥ 0`. If `p = 0`: `d_i < 1`, so `q ∈ {0,1}` and RHS `≤ 0`. The `|p−q| ≤ 1` structure (both in a two-element set) is what excludes `(0, ≥2)`. Correct.
4. **Budget with closed-container caveat.** `|T ∩ Λ_p| = N` for every `p` by Claim 1(a) (`c | k`, covol 1). `T̄ \ T` is two boundary segments; `B := {p : Λ_p ∩ (T̄\T) ≠ ∅}` is a countable union of translated segments in the shift torus, hence null. Correct. **Numerics:** at `k=5`, `θ = arctan(3/4)`: half-open budget was exactly 25 in all 500 random shifts.
5. **Pigeonhole + Fubini.** `∫_0^1 Σp_i(x)dx = Σd_i > N` and `Σp_i` integer-valued ⇒ `λ(A) > 0` where `A = {Σp_i ≥ N+1}`; likewise `λ(A') > 0`. Fubini: a.e. `x_0` has null slice `B_{x_0}`; the positive-measure set `A` therefore contains such an `x_0`; then `A' \ B_{x_0} ≠ ∅` gives `y_0`. Note `(x,y) = R_{-θ}p` is a measure-preserving reparametrization of the shift torus, and `Σp_i` depends only on `x`, `Σq_i` only on `y` — the product-measurability needed for Fubini is genuine. Sound.
6. **Final chain.** At `(x_0,y_0)`: `N = |T̄ ∩ Λ| ≥ Σ p_iq_i ≥ Σ(p_i+q_i−1) = Σp_i + Σq_i − (N+1) ≥ N+1`. Contradiction. Correct — note the count of squares `N+1` enters exactly once, in the `−1` sum; the statement needs all `k²+1` squares, as written.

**End-to-end numerics** (`k=5`, `θ = arctan(3/4)`, a legitimate 21-square tilted packing, 500 random shifts): `Σp_iq_i ≤ |T̄ ∩ Λ_p|` never violated; half-open budget constant at 25. (A 26-square counterexample packing cannot be built to test the contradiction — that is the theorem itself; all constituent inequalities check out.)

**Sharpened form (provable, same proof):** the hypothesis "`k²+1` squares" can be replaced by "`n` squares with `Σd_i > N` and `n ≤ ?`" — precisely, the proof gives: any common-θ packing of `n` squares in `[0,k]²` (θ Pythagorean, `c|k`) has `Σd_i ≤ max(N, (N + n − 1)/2)`... in the useful regime: if `n ≤ N+1` then `Σd_i ≤ N` whenever `2⌈Σd⌉ − n ≥ N+1` fails to be blocked — cleanest version: `2⌈Σd_i⌉ − n ≤ N`, i.e. `Σd_i ≤ (N+n)/2` for every `n`, with the integrality kick giving `Σd_i ≤ N` exactly at `n = N+1`. The report's statement is the sharp instance.

---

## Route D, Claim 5 (multi-frame no-go; J=1 common-orientation theorem)

**VERDICT: CORRECT** (assigned parts: the averaged inequality, its derivation, and the J=1 conclusion; the report's own honesty caveat — that J=1 is weaker than Cauchy–Schwarz — is accurate and should be kept).

**Pointwise step.** For each class `j`, against `Λ_j + p = R_{θ_j}Z² + p`: in-class squares are frame-aligned, so half-open product structure gives `c_i = p_iq_i ≥ p_i + q_i − 1` with `p_i,q_i ∈ {⌊d_i⌋,⌈d_i⌉}` (valid — the product structure is with respect to `Λ_j`, the lattice rotated to the class's own angle, which is exactly what `F_j` uses). Off-class squares contribute their raw counts. Global disjointness of counted sets needs no lattice point on any square boundary or on `∂T̄` — a null set of shifts. So `F_j(p) ≤ 0` off a null set. Sound.

**Averaging.** `E[p_i] = E[q_i] = d_i` for in-class squares — correct, and this is the crux the assignment flagged: in the tilted frame the frame-aligned square's projections onto the frame axes have width exactly `d_i` (not `d_i(cosθ+sinθ)`; that inflation only occurs for off-frame squares). Verified numerically: MC over 2·10⁵ shifts, `d = 1.3` gives `E[p] = 1.2990`. `E|S_i ∩ Λ_j+p| = d_i²` and `E|T̄ ∩ Λ_j+p| = area = N` hold for **any** unit-covolume lattice at any angle (no exactness needed after averaging) — verified: `θ = 1.0 rad`, `k = 4`: MC mean `16.021` vs `16`. Summing `E[F_j] ≤ 0` over `j` with `Σ_j n_j = N+1` and `Σ_j Σ_{i∉C_j} d_i² = (J−1)A`:

```
2 Σd − (N+1) + (J−1)A ≤ JN.    ✓ (algebra re-derived and confirmed)
```

**J = 1 conclusion.** `2Σd − (N+1) ≤ N` ⇒ `Σd ≤ N + 1/2`, for ANY common angle including 45° and irrationals. Pointwise-then-average is sound here; in fact for `J = 1` the pointwise inequality `Σ(p_i+q_i−1) ≤ Σp_iq_i ≤ |T̄ ∩ Λ_p|` holds for **every** shift (half-open boxes are deterministically disjoint; the closed container only over-counts), so no null-set bookkeeping is even needed before taking expectations. Numerically confirmed: 45°-packing in `[0,4]²`, 2000 shifts, `max[Σ(p+q−1) − |T̄∩Λ_p|] = −2 ≤ 0`.

**Standalone theorem (clean statement, verified proof):**

> **Theorem (common-orientation counting bound).** Let `θ` be arbitrary, `k ≥ 1`, and let `S_1,…,S_n ⊂ [0,k]²` be squares with pairwise disjoint interiors, all with edge angle `θ`, sides `d_i`. Then `2Σd_i − n ≤ k²`. In particular `n = k²+1` gives `Σd_i ≤ k² + 1/2`; unscaled, any `k²+1` squares of a single common orientation in the unit square have total side `≤ k + 1/(2k)`.
>
> *Proof.* Work in the θ-frame; half-open the squares (pairwise disjoint sets in `T̄` as in Claim 2 step 1). For the shifted lattice `Λ_p = R_θZ² + p` and every `p`: `Σ_i(p_i+q_i−1) ≤ Σ_i p_iq_i = Σ_i|S_i ∩ Λ_p| ≤ |T̄ ∩ Λ_p|`. Take expectation over `p` uniform on the torus: `E[p_i] = E[q_i] = d_i` (frame projections have width `d_i`), `E|T̄ ∩ Λ_p| = area(T̄) = k²`. Hence `2Σd_i − n ≤ k²`. ∎

**Mandatory honesty note (the report already contains it, correctly):** this is numerically *weaker* than Cauchy–Schwarz, which gives `Σd_i ≤ √(N(N+1)) = N + 1/2 − 1/(8N) + O(N⁻²)` with no orientation hypothesis. Its value is purely methodological (first counting-type bound valid at all orientations). **Sharpening I can prove:** equality `Σd = N + 1/2` is impossible — it would force `Σp_iq_i = |T̄∩Λ_p|` a.e., hence every lattice point covered a.e. shift, hence `Σd_i² = N` (full area), and then C–S gives `(N+1/2)² ≤ N(N+1)`, false. So strict: `Σd < N + 1/2` — still dominated by C–S.

**Auxiliary claims checked.** The parenthetical "at `ε = 1/2` the LHS exceeds `JN` by `(J−1)/(4(N+1))`" is exact (re-derived: excess `= (J−1)[(N+1/2)²/(N+1) − N] = (J−1)/(4(N+1))`). The implied ε-bound solves `2ε − 1 = (J−1)(N(1−2ε)−ε²)/(N+1)`; it is `1/2` at `J=1`, decreasing in `J`, with limit the C–S root of `N(1−2ε) = ε²` — always `≥` the C–S value since at `ε = ε_CS` the constraint reads `2ε_CS − 1 ≤ 0`, true. So "never beats C–S" is confirmed.

---

## Route E, Claim 6 (diamond chain; chain supremum = √2)

**VERDICT: CORRECT.**

**Upper bound.** A `u`-chain's members are separated in order by parallel lines with normal `u`, so their `u`-projections have pairwise disjoint interiors inside the `u`-projection of `U`, an interval of length `C(θ) ≤ √2`. Each square's `u`-projection has length `s_iC(θ−α_i) ≥ s_i` (`C ≥ 1` everywhere). Hence `Σs_i ≤ Σs_iC(θ−α_i) ≤ C(θ) ≤ √2`. Sound. (The sup is not attained: containment forces each 45°-square's projection to stand off `s/2` from the interval ends, so equality would need `s → 0`. "Equals √2" as a supremum is the right statement.)

**Construction.** `u = (1,1)/√2`, side `s`, angle 45°, centers `z_j = (v_j/√2)(1,1)`, `v_j = js`, `j = 1,…,m`, `m = ⌊√2/s⌋ − 1`.

- *Containment:* the 45°-square's vertices are `z ± (s/√2)e_1, z ± (s/√2)e_2`; containment in `U` ⟺ both center coordinates in `[s/√2, 1 − s/√2]` ⟺ `v_j ∈ [s, √2 − s]`. `j = 1`: `v_1 = s` ✓ (boundary contact allowed, square still in `U`). `j = m`: `v_m = ms ≤ (√2/s − 1)s = √2 − s` ✓. Verified.
- *Disjointness/chain:* `⟨z_j, u⟩ = v_j` and the half-width along `u` is `(s/2)C(45°−45°) = s/2` (u along the diagonal of each square), so projections `[v_j − s/2, v_j + s/2]` abut; the lines `⟨x,u⟩ = v_j + s/2` support square `j` at its single extreme vertex and square `j+1` at its single opposite vertex, placing all interiors strictly between consecutive lines — interiors pairwise disjoint and the family is a genuine `u`-chain.
- *Total:* `ms = (⌊√2/s⌋ − 1)s → √2`. **Numerics (exact SAT disjointness + vertex containment):** `s = 0.2`: 6 squares, total 1.200; `s = 0.1`: 13, total 1.300; `s = 0.05`: 27, total 1.350 — all contained, all pairwise disjoint. Matches the report's figures exactly.

Adversarial notes: no non-consecutive collision is possible (projections disjoint up to endpoints); the touching at single vertices is interior-disjoint, which is the packing condition in force. The "moral" drawn (zero standoff between consecutive tilted squares; only the container's corners charge tilt) is a fair reading of the construction and correctly identifies why bound-1 "linear" generalizations of `f(2)=1` are impossible.

---

## Summary

| Claim | Verdict | Notes |
|---|---|---|
| D-1 (exact budgets) | CORRECT | Coset argument airtight; (d) uses only the sound direction of the Fourier criterion; write "constant a.e." in the unused converse |
| D-2 (Pythagorean BKU) | CORRECT | All six steps verified; product structure, budget, Fubini handling all sound; numerics pass at `k=5, θ=arctan(3/4)` |
| D-5 (multi-frame no-go, J=1 theorem) | CORRECT | Averaged inequality exact; standalone common-orientation theorem stated + proved above; strict `< N+1/2` provable; dominated by C–S (report says so, honestly) |
| E-6 (diamond chain, sup = √2) | CORRECT | Containment window `v_j ∈ [s, √2−s]` checks at both ends; SAT-verified disjointness; upper bound √2 sound; sup not attained |

No errors requiring fixes were found in the four assigned claims. The one wording repair: in D-1(d), the biconditional should read "the count is constant **a.e.** iff `hat(1_T)` vanishes on `L*\{0}`"; the everywhere-version used in parts (a)–(c) comes from the coset argument, and part (d) only uses the (valid) forward direction.