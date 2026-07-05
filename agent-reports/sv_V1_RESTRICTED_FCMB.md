# Verification report: F1 claims C3, C4 (and C2 formula, C1 arithmetic)

## VERDICTS

| Claim | Verdict |
|---|---|
| C3 (exact decomposition identity + α₀β₀ = 0) | **CORRECT** |
| C4 (Restricted FCMB-AP via Lemma A) + Corollary (BKU reproof, d ≤ 1) | **CORRECT** |
| C2 (stack-gadget formula) | **CORRECT** (one implicit hypothesis should be stated: the stack has exactly h+1 squares, h ≥ 1 — forced by n = N+1) |
| C1 arithmetic (re-checked in passing) | **CORRECT** |

No errors found. Complete independent re-derivations below; all numerics reproduced and extended. Verification code: `/private/tmp/claude-501/-Users-kylekabasares-Desktop-erdos-106/6b0597a9-48bd-4e8c-a957-7fc4a05f26d8/scratchpad/session2/F1/verify_f1_c3c4.py` (written from scratch, independent of F1's `fcmb_check.py`/`search_k2.py`, which I also reran and reproduced exactly).

---

## C3 — exact decomposition identity: CORRECT (full re-derivation)

**Setup.** All dᵢ ≤ 1. For a.e. shift p = (x,y) ∈ [0,1)², square i captures cᵢ = pᵢ(x)qᵢ(y) ∈ {0,1} lattice points, where pᵢ = 1_{Xᵢ}, Xᵢ = x-projection [aᵢ, aᵢ+dᵢ] mod 1 (arc of length dᵢ), likewise Yᵢ. (Factorization needs dᵢ ≤ 1: the interval [aᵢ−x, aᵢ+dᵢ−x] contains an integer iff x mod 1 ∈ Xᵢ, and contains two integers only on a null set of x when dᵢ = 1.)

**Step 1: Av = ⊔ᵢ Avᵢ with Avᵢ = [∩_{j≠i}Xⱼ × ∩_{j≠i}Yⱼ] \ [Xᵢ×Yᵢ], exactly (a.e.).** Since each cᵢ ∈ {0,1} a.e. and there are N+1 squares, C = Σcᵢ = N iff exactly one cᵢ = 0. (This step does *not* need the budget C ≤ N.) "cⱼ = 1 for all j ≠ i" ⟺ (x,y) ∈ (∩_{j≠i}Xⱼ) × (∩_{j≠i}Yⱼ); "cᵢ = 0" ⟺ (x,y) ∉ Xᵢ×Yᵢ. Both directions immediate; the sets Avᵢ are pairwise disjoint (different unique empty square). Confirmed: the displayed set identity is exact, not an inequality.

**Step 2: the measure formula.** With A = {M_X = ∅}, Aᵢ = {M_X = {i}} (so α₀ = |A|, αᵢ = |Aᵢ|), note ∩_{j≠i}Xⱼ = {M_X ⊆ {i}} = A ⊔ Aᵢ, and crucially **A ⊆ Xᵢ** while **Aᵢ ∩ Xᵢ = ∅**. Expanding the product (A⊔Aᵢ)×(B⊔Bᵢ) into four rectangles and removing Xᵢ×Yᵢ:
- A×B ⊆ Xᵢ×Yᵢ — removed entirely;
- A×Bᵢ, Aᵢ×B, Aᵢ×Bᵢ each miss Xᵢ×Yᵢ entirely (one factor is disjoint from the corresponding side) — kept entirely.

So |Avᵢ| = α₀βᵢ + αᵢβ₀ + αᵢβᵢ, and summing:
**|Av| = α₀·Σβᵢ + β₀·Σαᵢ + Σαᵢβᵢ.** ∎ Exactly as displayed in F1.

**Step 3: α₀β₀ = 0.** For generic (x,y), [0,k]² contains exactly N = k² points of (x,y)+ℤ² (the points x+m, y+l with m,l ∈ {0,…,k−1}; boundary coincidences x+m = k etc. are null), and a captured point lies in the *interior* of its square for a.e. shift (finitely many boundary-alignment conditions, each null). Interiors are pairwise disjoint, so each of the N points is captured by at most one square: **C ≤ N a.e.** If α₀ > 0 and β₀ > 0, then A×B has positive measure and on it every cᵢ = 1, giving C = N+1 — contradiction. ∎ (F1's "over budget" argument, correct.)

**Step 4: termwise bound.** Aᵢ ⊆ Xᵢᶜ so αᵢ ≤ 1−dᵢ, likewise βᵢ, hence Σαᵢβᵢ ≤ Σ(1−dᵢ)² = s always. Correct.

**Numerics.** My independent implementation (breakpoint product partition + separate 1-D α/β sweep): identity holds to **max error 1.1e-16 on 25 packings** (20 random strip packings at k=2,3 + column k=2,3 + split-cell k=2 a=0.37, k=3 a=0.5 + the gadget [0.9,0.9,0.9,0.3]); α₀β₀ = 0 in every case (max product 0.0); termwise αᵢ ≤ 1−dᵢ held in all cases. Monte Carlo (4×10⁵ samples) cross-checks exact |Av| to ~5e-4 on 3 packings. F1's own 200-packing run reproduced verbatim (max err 5.55e-17).

---

## C4 — Restricted FCMB-AP and Lemma A: CORRECT (complete re-derivation)

**Theorem.** AP packing of N+1 squares in [0,k]², all dᵢ ≤ 1, Σdᵢ > N ⇒ |Av| ≤ s.

Let σ = Σ(1−dᵢ) = (N+1) − Σdᵢ < 1; every term ≥ 0 (needs **all** dᵢ ≤ 1 — this hypothesis is used twice: here and in the cᵢ ∈ {0,1} factorization).

**Lemma A: {M_X = ∅} is null.** Take x in this set avoiding the null set where some x+m equals some aᵢ or aᵢ+dᵢ (finitely many conditions mod 1).

*(i) Pigeonhole — verified.* x ∈ Xᵢ means ∃mᵢ ∈ ℤ with aᵢ ≤ x+mᵢ ≤ aᵢ+dᵢ; since 0 ≤ aᵢ and aᵢ+dᵢ ≤ k and x ∈ (0,1), necessarily mᵢ ∈ {0,…,k−1} (mᵢ > −1 from x+mᵢ ≥ 0, x < 1; mᵢ < k from x+mᵢ ≤ k, x > 0). Each of the N+1 squares contributes ≥ 1 incidence with the k lines {x+m}×ℝ; a square is counted at most once per line, so some line carries **L ≥ ⌈(N+1)/k⌉ distinct squares**. Ceil check: (k²+1)/k = k + 1/k, so ⌈(N+1)/k⌉ = k+1 for every k ≥ 1 — machine-verified k = 1..8. The assignment's worry is resolved: incidences ≥ N+1 is right (each square meets *at least* one line; extra incidences only help).

*(ii) Disjoint y-intervals — verified, including degenerate cases.* By genericity of x, the common point x+m is *interior* to each of the L x-intervals (endpoint touching excluded on a null set of x — this is exactly where "generic" is needed). Hence the L open x-intervals pairwise intersect (they share the interior point x+m). If two of these squares also had intersecting *open* y-intervals, their open rectangles (interiors) would intersect, contradicting packing. So the L closed y-intervals have pairwise disjoint interiors; endpoint touching between them is allowed and harmless. They sit in [0,k], so Σ_L dᵢ ≤ k.

*(iii) Deficit arithmetic — verified.* Σ_{i∈L}(1−dᵢ) = L − Σ_L dᵢ ≥ L − k ≥ (k+1) − k = 1. But nonnegativity of all deficits gives Σ_L(1−dᵢ) ≤ σ < 1. Contradiction. Since the contradiction holds for a.e. x in {M_X = ∅}, that set is null: **α₀ = 0**; symmetrically β₀ = 0. By C3, |Av| = Σαᵢβᵢ ≤ s. ∎

**Corollary (BKU reproof, d ≤ 1) — verified.** Structure identity: g + s = (N − Σd²) + Σ(1−dᵢ)² over N+1 squares = 2N+1 − 2Σd (algebra checked; matches the session identity 2Σd = 2N+1−g−s). If Σd > N then g+s < 1. But hits := N − C ≥ 0 a.e. (budget, Step 3 above), E[hits] = N − Σdᵢ² = g (since E[cᵢ] = dᵢ²), and hits ≥ 1_{hits≥1} gives g ≥ P(hits ≥ 1) = 1 − |Av| ≥ 1 − s, i.e. g+s ≥ 1. Contradiction; hence Σd ≤ N. ∎ Self-contained and correct. F1's sharpness remark is right: at Σd = N the column packing has α₀ = k/(k+1) > 0, so the hypothesis is exactly sharp.

**Mechanism stress test (extended).** F1 claimed "129/129 random instances" for the Lemma-A mechanism but that test is *not in the committed scripts* (only the α₀β₀ = 0 assertion is) — a reproducibility gap, not an error. I reran independently: over 400 random strip packings (k = 2,3), **109/109 instances with α₀ > 0 or β₀ > 0 exhibited the witness**: a lattice line carrying L ≥ k+1 squares with pairwise interior-disjoint y-intervals and deficit sum ≥ 1, and σ ≥ 1 in every such case.

---

## C2 — gadget formula |Av| = d₍₁₎ + (d₍₂₎−d₍₁₎)(1−d₍₁₎): CORRECT

**Derivation (F1 gave only numerics; here is a proof).** Stack of h+1 squares, sides d₁..d_{h+1} ≤ 1 summing to integer h ∈ {1,…,k}, sharing a left edge at x₀, y-intervals tiling [0,h]; N−h unit squares fill the rest (units capture 1 always). For a.e. y, the h points of y+ℤ in [0,h] each lie interior to exactly one stack y-interval (each interval holds ≤ 1 point since dᵢ ≤ 1), so **exactly one stack square misses in y** — call it J(y); |{J = i}| = 1−dᵢ, and Σ(1−dᵢ) = (h+1)−h = 1, a partition of [0,1). In x (translating so x₀ = 0): square i hits iff x < dᵢ. Empty squares = {i : dᵢ ≤ x} ∪ {J(y)}; Av ⟺ that set is a singleton:
- x < d₍₁₎: only J empty — always Av. Contribution d₍₁₎.
- d₍₁₎ ≤ x < d₍₂₎: need J = argmin — contribution (d₍₂₎−d₍₁₎)(1−d₍₁₎).
- x ≥ d₍₂₎: ≥ 2 empty — never Av. ∎

Checks: h = 1 gives a + (b−a)(1−a) = b(1−a) + a² = b² + a² = s (split cell, tight — algebra verified); equal sides give |Av| = d = k/(k+1) (column). Also Σd = h + (N−h) = N always, so g+s = 1 on the whole family — confirms C2's claim and that the tight family and the refuting family are one family.

**Numerics.** F1's 5 cases reproduced exactly. My extension: **12 randomized gadgets** (k ∈ {2,3,4}, h ∈ {1,…,k}, random sides summing to h, *shuffled order*, *random x₀* — configurations F1 never tested): formula exact in **12/12** (error < 1e-9), g+s = 1 in all.

## C1 arithmetic (re-verified in passing)

Column packing Pₖ, k = 1..6: valid packing, n = N+1, Σd − N = 0 exactly, g − k/(k+1) and s − 1/(k+1) at ~1e-15, |Av| − k/(k+1) at ~1e-16, and the derivation (y-intervals tile [0,k], exactly one column square empty for a.e. y when x ∈ (0, k/(k+1))) is sound. The maxC = 41 > N+1 at k = 6 in F1's output is a floating-point sliver of measure ≤ 8e-16 (closed-boundary double counting at coincident breakpoints jd); my independent implementation reproduces the identical artifact (|{C>N}| = 7.6e-16), confirming F1's diagnosis. k = 1 degenerates to the split cell with equality, as claimed.

---

## Sharpenings (new, proved here)

**S1 (unconditional Lemma A′).** *For any AP packing of N+1 squares with all dᵢ ≤ 1: if α₀ > 0 then (a) Σdᵢ ≤ N (i.e. σ ≥ 1), and (b) α₀ ≤ min_i dᵢ ≤ k/(k+1).* Proof: (a) is Lemma A's contrapositive. (b): A = ∩ᵢXᵢ ⊆ Xᵢ gives α₀ ≤ min dᵢ; the over-full line's L ≥ k+1 squares satisfy Σ_L d ≤ k, so min_L d ≤ k/(k+1) ≥ min_all d. Hence **max(α₀, β₀) ≤ k/(k+1) always, with equality at the column packing** — the full-hit terms in C3 are themselves capped, sharply. (Verified: 109/109 instances, plus columns k=2..5 attain equality.) Cheap corollary via C3, Σβᵢ ≤ min(1, σ): |Av| ≤ s + k/(k+1) unconditionally — weak, but the first unconditional AP bound of this shape.

**S2 (rigidity at the extremal budget Σd = N).** *If Σd = N (σ = 1), dᵢ ≤ 1, and α₀ > 0, then for a.e. full-hit x: the over-full line carries exactly k+1 squares, L = k+1; their y-intervals tile [0,k] up to null sets (Σ_L d = k exactly); every square off that line is a unit square; and the over-full line is unique for that x.* Proof: the Lemma A chain 1 = σ ≥ Σ_L(1−d) ≥ L−k ≥ 1 forces equality everywhere: L = k+1 (L ≥ k+2 would give deficit ≥ 2), Σ_L d = k (so the k+1 disjoint y-intervals of total length k tile [0,k]), and zero deficit off the line (all other squares are units). Uniqueness: a square on two lines x+m, x+m′ needs width ≥ 1, i.e. is a unit (deficit 0); a second over-full line would need deficit ≥ 1 from squares that are all units — impossible. ∎ (Verified numerically, k = 2..5.) This pins every α₀-positive BKU-extremal AP packing to exactly the stack-gadget structure, strongly supporting F1's "best next step (c)" conjecture max_AP |Av| = k/(k+1): combined with C2, any candidate maximizer with α₀ > 0 is a stack family member, where the max of d₍₁₎ + (d₍₂₎−d₍₁₎)(1−d₍₁₎) subject to k+1 sides ≤ 1 summing to k is d₍₁₎ = … = d₍₂₎ = k/(k+1) (the column). What remains open for that conjecture is only the case α₀ = β₀ = 0 (where |Av| ≤ s ≤ … needs a separate cap) and non-tiling stack variants.

## Minor presentational fixes recommended (no math changes)

1. C2 should state explicitly that the stack has exactly h+1 squares (m = h is forced by n = N+1); "d₍₂₎" is the second-smallest *with multiplicity* (ties give |Av| = d₍₁₎).
2. C3/C4 statements hold up to null sets ("a.e."); NOTES.md says "generic shifts" — carry that qualifier into the report statement.
3. The "129/129" Lemma-A stress test should be committed to code (currently unreproducible from the scripts; independently reconfirmed here as 109/109 on a fresh sample).
4. In Lemma A, "unique, interior point x+mᵢ" — uniqueness is generic (fails only on the null set x ≡ aᵢ mod 1 when dᵢ = 1) and is not needed; "at least one, interior" suffices.

**Bottom line:** C3 and C4 are correct as stated; C4 (with its Corollary) is a genuine, fully rigorous new theorem, and its hypothesis is exactly sharp per C1. C2's formula is correct and now has a proof, not just numerics. Sharpenings S1 (max(α₀,β₀) ≤ k/(k+1), sharp) and S2 (rigidity: α₀ > 0 at Σd = N forces the stack structure) are proved above and reduce the conjecture max_AP |Av| = k/(k+1) to the α₀ = β₀ = 0 case.