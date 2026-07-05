# V5 VERIFICATION REPORT: dual f(2)=1 proofs + Route B structure suite

Verification script: `/private/tmp/claude-501/-Users-kylekabasares-Desktop-erdos-106/6b0597a9-48bd-4e8c-a957-7fc4a05f26d8/scratchpad/v5_checks.py` (all numerics below reproduced from its output).

---

## PART 1 — Route E (report_ROUTE_E_SMALL_CASES.md), Claims 1–4

### Claim 1 (submultiplicativity C(x)C(y) ≥ C(x±y)) — VERDICT: CORRECT
Expanding the product gives the four terms |cos x cos y|, |sin x sin y|, |sin x cos y|, |cos x sin y|; pairing (1st,2nd) and (3rd,4th) and applying the triangle inequality yields |cos(x+y)|+|sin(x+y)|. Airtight for all real x,y. Numerics: min of C(x)C(y)−C(x+y) over 10^6 random pairs = 9.9e−9 ≥ 0. **Sharpened form (provable):** equality holds iff x ≡ 0 or y ≡ 0 (mod π/2); this is what feeds the rigidity in Claim 4 and it is exactly right — equality in both triangle-inequality applications forces sin x sin y cos x cos y terms to have coherent signs, which happens iff one angle is a multiple of π/2.

### Claim 2 (corner-standoff lemma) — VERDICT: CORRECT
- Support function h_K(u_φ) = ⟨z,u_φ⟩ + (s/2)C(φ−α): correct (rotation shifts the argument of the axis-parallel support function (s/2)(|cos φ|+|sin φ|)).
- (i): the four half-plane constraints use C(π−α)=C(−α)=C(α) — correct (C is even and π/2-periodic). Cosmetic only: the "±z₁+(s/2)C(α) ≤ {1,0}" display is sloppy shorthand for z₁+(s/2)C(α) ≤ 1 and −z₁+(s/2)C(α) ≤ 0, but the content is right.
- (ii): **θ-convention check (assigned focus):** the step u₁+u₂ = C(θ) is valid precisely because the hypothesis cos θ, sin θ ≥ 0 is stated in the claim; on [0,π/2], C(θ) = cos θ + sin θ. No leak. The chain D(α) ≥ C(θ)(C(α)+1/C(α)) ≥ 2C(θ) via Claim 1 (x=θ−α, y=α gives C(θ−α)C(α) ≥ C(θ)) and AM–GM is correct.
- (iii): symmetric, correct.
- Numerics: min of D(α;θ)−2C(θ) on a 2001×2001 grid (θ∈[0°,90°], α∈[−45°,45°]) = 0.0 exactly, **equality attained only at α = 0** (grid equality set = {α=0}), confirming both the inequality and the equality classification used by Claim 4.

### Claim 3 (f(2)=1) — VERDICT: CORRECT
**The normalization step (assigned focus), checked in full detail.** Under the reflection R: (x,y)↦(1−x,y): if K₁ ⊆ {⟨x,u⟩ ≤ c}, then for x′=Rx, ⟨x,u⟩ = u₁ − u₁x′₁ + u₂x′₂, so R(K₁) ⊆ {⟨x′,u′⟩ ≤ c′} with u′=(−u₁,u₂), c′=c−u₁, and simultaneously R(K₂) ⊆ {⟨x′,u′⟩ ≥ c′}. So each reflection (a) flips exactly one sign of u, (b) **preserves which square is on which side** (only c changes, and c is free), (c) preserves side lengths, containment in U, and interior-disjointness, (d) preserves |u|=1. The two reflections generate all four sign patterns, so u can always be brought to the closed first quadrant with labels and inequality directions intact — no label swap is ever needed. This is the step where such proofs usually break; here it does not.

Remaining steps: separation theorem for disjoint open convex sets (valid; s_i>0 case), closure passage K = cl(int K) (valid for s>0), degenerate s_i=0 case handled separately (valid). Chain s₁C(θ) ≤ h_{K₁}(u) ≤ c ≤ min_{K₂} ≤ (1−s₂)C(θ), divide by C(θ) ≥ 1 > 0. Correct.

**Adversarial end-to-end numerics (assigned):** 20,000 random interior-disjoint pairs (SAT-verified disjointness, actual SAT separating axis, reflections implemented as literal coordinate maps on the corner sets, transformed edge angles tracked): **0 violations** of any of: separation preservation after normalization, s₁C(θ) ≤ h_{K₁}, min_{K₂} ≤ (1−s₂)C(θ), the stronger D-standoffs (s₁/2)D(α₁′) ≤ h_{K₁} and min_{K₂} ≤ C(θ)−(s₂/2)D(α₂′), and s₁+s₂ ≤ 1.

### Claim 4 (rigidity) — VERDICT: CORRECT
The sandwich C(θ) = (s₁+s₂)C(θ) ≤ (s₁/2)D(α₁)+(s₂/2)D(α₂) ≤ C(θ) is right: the middle inequality comes from h_{K₁} ≤ min_{K₂} plus 2(ii)/(iii); the left from D(αᵢ) ≥ 2C(θ). Equality with sᵢ>0 forces D(αᵢ)=2C(θ), which forces AM–GM equality C(αᵢ)=1, i.e. axis-parallel (this uses the equality classification confirmed numerically under Claim 2). The chain then collapses entirely (h₁ = c = min₂ = s₁C(θ)), pinning ⟨z₁,u⟩ = (s₁/2)C(θ); since z₁ − (s₁/2)(1,1) has nonnegative components and u ≥ 0, each strictly-positive component of u pins the corresponding coordinate. The case split (u=e₁ / u=e₂ / u₁,u₂>0) is exhaustive and each case lands in the stated strip/corner family. Correct; the diagonal-reflection remark for u=e₂ is fine (a symmetry of U).

---

## PART 2 — LIT_CLASSICAL (report_LIT_CLASSICAL.md) §3

### Lemma A (corner lemma) — VERDICT: CORRECT
- Vertex extremization: min x over S = z_x − (s/2)(|u_x|+|w_x|) with |u_x|+|w_x| = cos θ + sin θ = G for θ∈[0,π/2): correct.
- φ(u)=cos(θ−α), φ(w)=sin(α−θ), D=|cos(θ−α)|+|sin(θ−α)|: correct.
- Product identity GF = cos(θ−α)+sin(θ+α): expanded and verified.
- **Concavity computations (assigned):**
  - Case θ≥α: θ−α ∈ [0,π/2) so D = cos(θ−α)+sin(θ−α) — sign choice valid. g(θ)=cos(θ−α)+sinθcosα−cosα−sinα; endpoints g(α)=(1−cosα)(1−sinα) (identity machine-verified to 1.8e−16) ≥ 0, g(π/2)=0 ✓; g″=−cos(θ−α)−sinθcosα ≤ 0 on [α,π/2] since θ−α∈[0,π/2] and sinθ,cosα ≥ 0 ✓. Concave + nonneg endpoints ⇒ ≥ 0 ✓.
  - Case θ<α: α−θ ∈ (0,π/2] so D = cos(α−θ)+sin(α−θ) valid; h₀(0)=0, h₀(α)=(1−cosα)(1−sinα) ≥ 0, h₀″=−cos(α−θ)−sinαcosθ ≤ 0 on [0,α] ✓.
- Grid check: min of GF+D−2F over θ_sq∈[0,π/2), α_n∈[0,π/2] on 2001² grid = 0.0, never negative.
- Equality clause: one **cosmetic slip** — "forcing θ = π/2 ≡ 0" is outside the stated convention θ∈[0,π/2). Corrected statement: in case θ ≥ α, concavity puts g strictly above the chord from (α, g(α)>0) to (π/2, 0), so g > 0 on all of [α, π/2); hence **no equality occurs in this case at all** within the convention, and the only equality point is θ = 0 (from the h₀ chord argument). Conclusion unchanged: for α∈(0,π/2), equality ⇒ axis-parallel. CORRECT WITH (cosmetic) FIX.

### Step 4 (reflection ρ) — VERDICT: CORRECT
φ(ρ(x,y)) = (1−x)cosα + (1−y)sinα = h − φ(x,y): verified. ρ(S₂) ⊆ {x≥0,y≥0} uses S₂ ⊆ U ⊆ {x≤1,y≤1} ✓; φ ≥ c on S₂ gives φ ≤ h−c on ρ(S₂) ✓; ρ is a point reflection (rotation by π), so it preserves squarehood, side length, and orientation mod π/2 ✓ (the last is needed so the equality clause transfers to S₂ itself). a+b ≤ c/h + (h−c)/h = 1 ✓. The preliminary 0 < c < h argument (one sentence is truncated mid-text: "c > 0 would fail only if… precisely:", but the completed argument that follows — c=0 forces S₁ ⊆ {φ=0}, empty interior — is complete and correct). Strictly, Lemma A does not even need c>0 (a positive-side square forces c ≥ (s/2)(GF+D) > 0 automatically), so this is belt-and-braces.

### Equality/rigidity discussion — VERDICT: CORRECT
Dichotomy is exhaustive: for a given extremal pair, every valid separating (n,c) yields a tight chain (a ≤ c/h and b ≤ (h−c)/h hold for each, and a+b=1 forces both tight). If some separating direction has α∈(0,π/2), the equality clause of Lemma A (applied to S₁ and to ρ(S₂)) forces both axis-parallel. If only axis-parallel separations exist, the projection argument (x-projections of lengths aG₁, bG₂ with disjoint interiors in [0,1], a+b ≤ aG₁+bG₂ ≤ 1, equality ⇒ Gᵢ=1) is correct. Note it delivers less than Route E Claim 4 (no position pinning), but claims less.

---

## PART 3 — Cross-check of the two proofs

**Same inequality.** Notation map: (E square angle α, E normal angle θ) = (LIT θ, LIT α). E's D(α;θ) ≥ 2C(θ) reads C(a)C(t)+C(t−a) ≥ 2C(t) (a = square, t = normal); LIT's GF+D ≥ 2F reads C(θ)C(α)+C(θ−α) ≥ 2C(α) (θ = square, α = normal). Under the map and evenness of C these are **literally the same scalar inequality**, with the "2·" on the normal-angle factor in both. Machine check: max |E_form − LIT_form| over 10⁵ random angle pairs = 0.0 (exactly).

**Same chain.** With the sharpest constants c = h_{K₁}(u) and c = min_{K₂}, LIT's a·F ≤ c and b·F ≤ F−c are identical to E's s₁C(θ) ≤ h_{K₁} and min_{K₂} ≤ (1−s₂)C(θ). The two proofs share the whole skeleton (separation → reflection normalization → corner standoff → additivity along the normal) and differ **only** in the proof of the scalar inequality: E uses submultiplicativity + AM–GM (valid for all real angles, and gives the equality classification C(α)=1 for free); LIT uses a two-case concavity argument (valid on the stated ranges, gives equality via chord-strictness). Both proofs of the scalar inequality are independently correct; grid minima are 0 with identical equality sets ({square axis-parallel}). E's route is strictly more flexible (no case split, no range restriction); LIT's is self-contained trigonometry.

**Random-pairs test of the full chain:** 20,000 SAT-disjoint pairs, 0 violations of any link of either chain (Part 1, Claim 3 numerics — the D-standoff checks are exactly LIT's (s/2)(GF+D) bound).

**One real discrepancy of scope, not correctness:** E Claim 4 pins positions (strip/corner classification); LIT's equality discussion only proves axis-parallelism. They are consistent; E's is the stronger citable statement.

---

## PART 4 — Route B (report_ROUTE_B_STRUCTURE.md)

### Claim 2 (tangent cones; parallel-contact rigidity) — VERDICT: CORRECT
S ⊆ C(S,x₀) globally: a convex body lies in its tangent cone at any boundary point (intersection of supporting half-planes at incident edges). Local equality for small ρ: correct. Parallel contact: near x₀ cones = squares, so cone interiors are disjoint near x₀, and by positive homogeneity globally (y ∈ int C₁ ∩ int C₂ ⇒ x₀+t(y−x₀) in both square interiors for small t). Two half-planes through a common point with disjoint interiors must be complementary (otherwise a direction lies in both open halves), so the boundary lines coincide = both edges collinear ⇒ mismatch α=0. The phrase "whose union lies in the disk" is stray/garbled but unused — the argument stands on disjoint interiors alone. Consequence (α>0 contact involves a vertex) is the direct contrapositive. CORRECT.

### Claim 3 (Sector Lemma) — VERDICT: CORRECT
Cone-angle bookkeeping |C₁|+|C₂| ∈ {3π/2, π} (edge–edge excluded by Claim 2), complement angle ∈ {π/2, π}, at most two gap arcs each bounded by one edge-ray of each square: correct. The "neither sector empty" step is sound: an empty gap arc means the cones share a boundary ray, which is an edge direction of both squares, forcing θ₁ ≡ θ₂ mod π/2, i.e. α=0 — contradiction. Sector angles lie in {α, π/2−α, π/2+α, π−α}, all ≥ α for α ≤ π/4 ✓. The all-r validity of the area bound (γ₁+γ₂)/2·r² ≥ αr² rests exactly on the global inclusion S_j ⊆ C_j ✓. My independent MC (300 vertex–edge configurations, fresh code): min uncovered/(αr²) = 0.993 (=1 within MC noise at 20k samples), consistent. The honest caveat (third squares may fill the sectors) is correctly flagged and does not affect the claim as stated.

### Claim 4 (buried-point crystallization; wall version) — VERDICT: CORRECT
**The assigned subtle point — "positive angular gap forces uncovered points arbitrarily close":** valid, and here is the fully explicit version the report compresses. The packing is finite; let ρ₀ = min over (a) the radii below which each square containing x₀ coincides with its cone, (b) dist(x₀, S_j) over squares not containing x₀ (positive, closed sets). For 0 < t < ρ₀ and any direction v in an open angular gap between consecutive cone-sectors, x₀+tv lies in no square: not in squares ∌ x₀ (too far), not in squares ∋ x₀ (their trace in B(x₀,ρ₀) is their cone, which excludes direction v). So x₀ is not buried — contradiction. Correct.

Remaining steps: shared ray = edge direction of both neighbors (Claim 2) ⇒ θᵢ ≡ θⱼ mod π/2, chain around the circle ✓; angle multisets from parts in {π/2, π} summing to 2π are exactly {π,π}, {π,π/2,π/2}, {π/2⁴} ✓. **Wall version:** correct — insert the container's tangent cone (half-plane at a wall point, quarter-plane at a container corner, orientation 0 mod π/2 either way) as one sector; its boundary rays are axis directions, so the adjacent square inherits orientation 0 mod π/2 and the chain propagates. One unstated but automatic hygiene fact: the hypothesis "x₀ on the boundary of every square containing it" is free in a packing — x₀ ∈ ∂S ∩ int S′ would give int S ∩ int S′ ≠ ∅ (every neighborhood of a boundary point of a nondegenerate square meets its interior).

### Claim 5 (tiling rigidity, lowest-tilted-vertex induction) — VERDICT: CORRECT; and LIT §5's lex-min proof is ALSO CORRECT (independent double coverage)
Route B's proof, checked step by step: complement of the closed union is relatively open with zero area, hence empty ⇒ every point buried ✓; tilted tile ⇒ unique lowest vertex ✓; v ∈ ∂R handled by the wall version (⇒ τ*=0, contradiction) ✓; v ∈ int R: Claim 4 makes all tiles at v share orientation, all tilted by τ*>0; the tangent cone of S* at its lowest vertex spans directions [τ*, τ*+π/2] ⊂ (0,π), so the downward direction 3π/2 is outside it, and since all boundary rays at v have directions ≡ τ* mod π/2 with τ*∈(0,π/4], none is vertical — so the downward ray lies in the **open interior** of some other tile's sector; that tile is tilted and dips strictly below y*, contradicting minimality ✓ (the possible worry that the downward ray is a shared boundary ray is excluded exactly by τ*>0 — worth stating explicitly in a write-up). The "v on the boundary of every tile containing it" hypothesis of Claim 4 is automatic (see Claim 4 note).

LIT §5 (lex-min corner + rectilinear induction): verified independently in Part 2 territory — the lex-min corner is the lower-left vertex of every defining rectangle containing it; local wedge identity; the corner tile must be the axis-parallel corner square (half-disk/cone-comparison steps all valid); removal preserves rectilinearity via the refinement grid (valid because the removed tile is axis-parallel); induction closes. **Both proofs correct.** Differences: LIT's is self-contained, covers rectilinear regions and rectangle tiles, and constructively locates tiles (used in its Corollary for f(k²)=k rigidity); Route B's is shorter but inherits Claim 4, and covers only the initial rectangle (sufficient for its use). No conflict.

### Claim 7 (Window Theorem) — VERDICT: CORRECT (constants re-derived and confirmed)
Re-derivation, as assigned: non-deviant S_i meeting W has y_v ∈ [0,δ) (container floor + intersection), d_i sin τ_i ≥ 0.9 sin t = δ ≥ δ−y_v, so Claim 6(c) applies at Y=δ: area(S_i∩W) ≤ area(S_i∩{y≤δ}) = ½(δ−y_v)ch_i(δ) ≤ (δ/2)ch_i(δ) ✓. Every such square crosses height δ (vertical extent d(cos τ+sin τ) ≥ 0.9 > 0.64 ≥ δ) ✓; chords at height δ have disjoint interiors (interior-disjoint convex bodies on a line) ✓; diameter ≤ √2·1.1 = 1.5556 < 1.56, and each meets [a,a+L], so all chords ⊆ [a−1.56, a+L+1.56], Σch ≤ L+3.12 ✓; covered-by-nondeviants ≤ (δ/2)(L+3.12); deviant term area(S_i∩W) ≤ δ·(max chord) ≤ √2 δ d_i ✓; gap ≥ Lδ − (δ/2)(L+3.12) − √2δΣ_dev = δ(L/2−1.56) − √2δΣ_dev ✓ — exactly as stated. Approximate-wall degradation (h/2)(L+3.12): follows by the same substitution ✓. Independent MC re-check (fresh code, tilted unit-square grids clipped to [0,30]², window [0,8]×[0,δ]): t=0.05: gap 0.360 vs bound 0.110; t=0.2: 1.360 vs 0.436; t=0.775: 5.038 vs 1.537 — holds with factor ~3 slack, matching Route B's own CHECK 2.

### Claim 8 (no coherent tilt; final arithmetic) — VERDICT: CORRECT (constants conservative-valid; sharper constants below)
Recomputation, as assigned:
- 2√2·136 = **384.6661** (not 388; see below for why 388 still appears legitimately).
- 2.44⌊k/8⌋ ≥ 2.44(k/8 − 1) = 0.305k − 2.44.
- Exact combination: **G ≥ 0.9 sin t · (2.44⌊k/8⌋ − 384.67) ≥ 0.9 sin t · (0.305k − 387.11).** (The assignment's guess "0.305k − 384.7" holds only when 8 | k; in general the floor costs the extra 2.44, giving 387.11.)
- The report's "0.3k − 388" is a **valid weakening**: 0.305k − 387.106 ≥ 0.3k − 388 ⟺ 0.005k ≥ −0.894, true for all k. Not an error.
- Consequence: sin t < 1/(0.9·(0.3k−388)) = 1/(0.27k − 349.2); the report's 1/(0.27k − 350) is again a valid (slightly weaker) bound. "Meaningful for k ≥ 1300" ✓ (0.27·1300−350 = 1); "< 4/k for k ≥ 17500" is **exact** (1/(0.27k−350) = 4/k at k = 17500).
- Supporting steps checked: deviant diameter ≤ √2·d_i < 2√2 ≈ 2.83 < 8 ⇒ meets ≤ 2 windows ✓; window strips pairwise disjoint so gaps add into G ✓; G < 1 from Claim 1 (needs ε > 0, i.e. Σd_i > N strictly — in the hypothesis) ✓; the fed-in Claim 1(b) constant Σ_D d_i < 136 re-verified (|D| ≤ V/0.09² ≤ 123.5, Σ_D d_i ≤ 124m + √(124V) ≤ 124 + 11.14 < 136, using 1−m ≤ 1/(N+1) ≤ 0.01 for k ≥ 10) ✓.
- **Sharpened form (provable, same proof):** G ≥ 0.9 sin t·(0.305k − 387.11), hence sin t < 1/(0.2745k − 348.44), meaningful for k ≥ 1274, and < 4/k for k ≥ 14221.

---

## Summary table

| Item | Verdict |
|---|---|
| E Claim 1 (submultiplicativity) | CORRECT (+equality classification provable) |
| E Claim 2 (corner standoff) | CORRECT (cosmetic notation in (i)) |
| E Claim 3 (f(2)=1; normalization) | CORRECT — normalization step verified exactly; no label/side leak |
| E Claim 4 (rigidity) | CORRECT |
| LIT §3 Lemma A (concavity) | CORRECT WITH FIXES (cosmetic: equality clause should say "no equality in case θ≥α on [α,π/2); θ=0 in case θ<α"; one truncated sentence in Step 2) |
| LIT §3 Step 4 (reflection ρ) | CORRECT |
| LIT §3 equality/rigidity | CORRECT (weaker than E Claim 4 but claims less) |
| Cross-check | Same inequality (exact notation map, machine-identical), same chain; both scalar proofs independently valid; 20,000-pair chain test: 0 violations |
| B Claim 2 (cones/parallel contact) | CORRECT (one stray phrase, unused) |
| B Claim 3 (Sector Lemma) | CORRECT |
| B Claim 4 (crystallization + wall) | CORRECT (gap-argument sound for finite packings; boundary hypothesis automatic) |
| B Claim 5 (tiling rigidity) | CORRECT; LIT §5 lex-min proof also CORRECT — independent double coverage, no conflict |
| B Claim 7 (Window Theorem) | CORRECT — constants re-derived exactly as stated; MC re-check passes |
| B Claim 8 (min-tilt arithmetic) | CORRECT — 2√2·136 = 384.67, exact chain 0.305k − 387.11; "0.3k−388" and "1/(0.27k−350)" are valid weakenings, not errors; sharpened: sin t < 1/(0.2745k − 348.44), <4/k for k ≥ 14221 |

No claim in this assignment is FLAWED or UNSALVAGEABLE. The two f(2)=1 proofs are the same proof in two notations with two different proofs of one scalar inequality; both are publish-solid, and E's version additionally carries the position-rigidity statement.