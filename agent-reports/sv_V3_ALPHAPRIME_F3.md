# Adversarial verification — F5 (Lemma α′, α′-edge, gradient corollary) and F3 (Claims 2, 4, 5)

All numerics re-run and extended; independent adversarial suites written at `/private/tmp/claude-501/-Users-kylekabasares-Desktop-erdos-106/6b0597a9-48bd-4e8c-a957-7fc4a05f26d8/scratchpad/verify_s2/{alpha_adv2.py,f3_adv.py}`.

## VERDICT TABLE

| Claim | Verdict | One-line |
|---|---|---|
| F5 Claim 1 (Lemma α′) | **CORRECT** | Every step checks; constants all verified; I can sharpen 228 → 60 |
| F5 Claim 2 (α′-edge) | **CORRECT WITH FIXES** | The flagged gap **closes** (expanded below), but the crest-count constant 1/520–1/585 is **wrong**: crest squares can poke above ℓ outside e's span. Corrected: 1/920 (author's assembly) or 1/240 (optimized) |
| F5 Claim 3 (gradient corollary) | **CORRECT** (as the conditional statement it claims to be) | Reflection/frame bookkeeping checks; constant inherits my α′ sharpening (456 → 120) |
| F3 Claim 2 (Comparison Identity) | **CORRECT** | (i)–(iv) all airtight; a.e. logic sound; verified on a new non-cell-confined big-square case |
| F3 Claim 4 (tilt-neutrality) | **CORRECT** | As scoped (diam < 1 / cell-confined); the "100% shrinkage artifact" reading is justified on the session-1 family |
| F3 Claim 5 (tightness-manifold FCMB) | **CORRECT** | Every step verified; depends on f(2)=1 (any orientations), which the report proves self-contained (§3, with rigidity — also needed for the equality case) |

---

## F5 Claim 1 — Lemma α′. CORRECT.

**Step 1 (vertical accounting).** Sound. F(x) := max top among spanning squares; covering requires spanning; all tops ≤ ℓ; the segment {x}×(max(F, ℓ−h), ℓ) ⊆ R is uncovered; Fubini gives ∫₀^X min(h, ℓ−F). If no square spans x, F = −∞ and the integrand is h. ✓

**Step 2 (per-square envelope, both tilt signs).** Verified in full.
- ψ ≥ 0: (ℓ−T_S)′ = τ − tanψ ≥ τ₁ on the rising branch, τ + cotψ > τ₁ on the falling branch; anchor x_L under the line gives (ℓ−T_S)(x_L) ≥ 0; integrate. ψ = 0 (flat top, slope τ ≥ τ₁) is covered. ✓
- ψ < 0: anchor at topmost vertex x_U (under the line ⇒ value ≥ 0). Right: slope τ + tan|ψ| ≥ τ ≥ τ₁. Left: going left, ℓ−T_S grows at rate cot|ψ| − τ. The requested chain holds exactly: tan φ₀ ≤ τ/2 ⇒ cot|ψ| ≥ 1/tan φ₀ ≥ 2/τ; **2/τ − τ ≥ 1 for all τ ∈ (0,1]** (decreasing in τ, value 1 at τ=1; verified numerically over a 1000-point grid); and τ₁ ≤ τ ≤ 1, so cot|ψ| − τ ≥ 1 ≥ τ₁. ✓ This is the only place tan φ₀ ≤ τ/2 is load-bearing, and the hypothesis shape is right (at φ₀ = θ a coherent row hugs at zero cost — confirmed as the numerical extremal).

**Step 3 (argmax/bathtub).** Sound. Ties broken by index keep I_j measurable; I_j ⊆ π_x(S_j) so m_j ≤ w_max; the rearrangement to the interval centered at a_j is the standard bathtub bound for a symmetric-increasing integrand (valid even when a_j ∉ I_j, which occurs after re-anchoring in the edge version); for s ≤ m_j/2 ≤ w_max/2, τ₂s ≤ min(τ₁s, h) since τ₂ ≤ τ₁ and τ₂·(w_max/2) ≤ h. Constants: w_max = 1.05·(cos+sin)(arctan ½) = **1.40872 ≤ 1.409**; 2h/w_max = **0.35493 ≥ 1/3**. ✓ (machine-checked)

**Step 4 (crest count).** Witness (x, y₀) with y₀ > ℓ(x)−h; diam = √2·1.05 = **1.48492 ≤ 1.49**; every point of a crest square satisfies ℓ(x′) ≥ y′ > ℓ(x′) − (h + 1.49 + 1.49τ) ≥ ℓ(x′) − 3.23 (τ ≤ 1). Parallelogram area = 3.23(X+2.98) (base × vertical height for a sheared parallelogram ✓). J ≤ 3.23(X+2.98)/0.95² = 3.5789X + 10.665; at X = 1 this is **14.2442 ≤ 14.25**, and ≤ 14.25X for X ≥ 1. ✓ Note: containment below ℓ is where this step **uses the half-plane hypothesis** — this is exactly what breaks in the edge version (see Claim 2).

**Step 5 (assembly).** Cauchy–Schwarz Σm_j² ≥ (X−|N₀|)²/J with Σm_j = X−|N₀| ✓; both dichotomy branches check; 4·4·14.25 = 228 ✓; the 456-form follows from τ−tanφ₀ ≥ τ/2 ✓.

**Numerics.** Re-ran `alpha_prime_check.py`: worst ratio **112.286**, 0 violations, tightest case = coherent +φ₀ hug — reproduces the report exactly. My independent suite added cheat families the author never tested: **two-layer notch-filling** (second row binary-searched *upward* into the V-notches of the hug row), sides at the extreme 1.05, mixed 0.95/1.05, exact boundary tan φ₀ = τ/2, and 12 random-brick restarts — all SAT-verified disjoint and below-line. Worst new ratio **110.29 ≥ 1**, minimum again at a coherent-hug variant. The lemma is numerically robust with two orders of slack.

**Sharpening (proved).** The |N₀| ≥ X/2 dichotomy is wasteful. Split at |N₀| = λX with λ = 1/45: branch 1 gives U ≥ hλX = X/180 = (X/60)(1/3) ≥ RHS; branch 2 gives U ≥ (τ₂/4)(44/45)²X²/(14.25X) = τ₂X/59.65 ≥ τ₂X/60. Hence
**|R \ ∪Q| ≥ (X/60)·min(τ − tan φ₀, 1/3) ≥ (X/120)·min(τ, 2/3)** — a free 3.8× improvement of both constants with no other change. (This propagates to Claim 3: 456 → 120, and partially recovers the "hoped 36".)

## F5 Claim 2 — Corollary α′-edge. CORRECT WITH FIXES.

**The flagged GAP (re-anchoring) closes; I expanded it.** Two components:

*(a) The dichotomy is uniform, not just per-abscissa (this makes the re-anchoring clean).* W and S* are convex with disjoint interiors, so a separating line L exists. On e's span, S*'s chord bottom is ℓ(x), hence L(x) ≤ ℓ(x) there. So a "below-type" W (on L's lower side) has T_W(x) ≤ L(x) ≤ ℓ(x) for **every** x in e's span ∩ span(W) — no below/above flips inside the span; above-type W's never enter F. This is stronger and simpler than the derivation's "a.e. abscissa" chord argument and eliminates the possibility of crest intervals fragmented by type-flips.

*(b) Re-anchoring.* Let D(x) := ℓ(x) − T_W(x) on span(W), with ℓ now e's line (τ = tan α ≤ 1, τ₁ = tan α − tan φ₀ ≥ tan α/2 > 0 by hypothesis). From Step 2's slope inventory: for ψ ≥ 0, D′ ∈ {τ−tanψ, τ+cotψ}, both ≥ τ₁ > 0, so D is **increasing** on the whole span; for ψ < 0, D is **V-shaped** (slopes τ−cot|ψ| ≤ −1 then τ+tan|ψ| ≥ τ), with the left branch falling at rate cot|ψ|−τ ≥ 2/τ−τ ≥ 1 ≥ τ₁ in the leftward direction. By (a), D ≥ 0 on the relevant window [0,X_e] ∩ span(W). Anchor a_W := the argmin of D restricted to that window (= x_U if interior, else the appropriate window endpoint); in every case D(a_W) ≥ 0 and both one-sided growth rates are ≥ τ₁, so D(x) ≥ τ₁|x − a_W| on the window. The bathtub step never needed a_W ∈ I_j. So Steps 2–3 survive verbatim. **The gap is real only as an exposition gap; the mathematics closes routinely, as claimed.**

**However, the constant is wrong — a genuine (fixable) error.** Location: derivations §2, the crest count "crest squares lie in a parallelogram of horizontal extent X_e+2.98, area ≤ 13.05, J ≤ 14.5". This silently reuses Step 4's containment **below ℓ**, which in the edge setting only holds over [0, X_e]: a below-type crest square W (T_W ≤ ℓ on e's span, forced by the separating line only there) may legitimately **poke above ℓ outside e's span** — e.g. a square wrapping around S*'s vertex, rising along its steep envelope edge (slope cot|ψ| ≥ 2) up to ~1 above ℓ just beyond X_e; it can still be crest inside the window. Such squares are not contained in the stated parallelogram, so J ≤ 14.5 is unjustified. Correct containment: every point of a crest square has ℓ(x′) − 3.23 < y′ ≤ ℓ(x′) + 2.98, with the above-ℓ part confined to x′ ∈ [−1.49,0) ∪ (X_e, X_e+1.49]. Region area ≤ (X_e+2.98)·3.23 + 2·1.49·2.98; worst case X_e = 0.63 gives J ≤ 22.76 and (author's |N₀| ≥ X_e/2 assembly) U ≥ τ₂·X_e²/(16J) = **τ₂/918** (machine-checked; X_e²/J is increasing in X_e, so 0.63 is the worst point; the author's own no-poke arithmetic reproduces exactly their 521/585, confirming this is the sole discrepancy).

**Corrected statement (proved, incorporating the optimized dichotomy λ = 0.00882):**
> Under the hypotheses of Claim 2, |R_e \ packing| ≥ **(1/240)**·min(tan α − tan φ₀, 1/3).

(Conservative variant keeping the author's assembly: 1/920.) Everything downstream that cites "1/520" or "1/585" (Claim 6's Jaw-1 arithmetic, §6 vertical transport "tiltmass/(260k)") should be rescaled by ≈ 240/585 — the ~1/k shape and the "Jaw 1 alone cannot beat 2c" conclusion are unaffected.

Two hygiene notes: (i) the corollary as stated applies to the two *shallow* edges (horizontal extent d·cos α); for a steep edge, rotate the γ-frame by π/2 first (folded tilts invariant) — worth a sentence; (ii) "R_e = points within distance h of e" (segment-distance, with end caps) is the right definition: it does contain the vertical strip {x ∈ span(e)} × (ℓ−h, ℓ) since the vertical drop v bounds the segment-distance; a *perpendicular rectangle* definition would not, and would cost span at the ends.

## F5 Claim 3 — gradient corollary. CORRECT (conditional, as flagged).

The reflection through ℓ_n is an isometry, so α′ applies; in the ψ_{n+1}-rotated frame the covering family (row n+1) has folded tilts ≤ δ_{n+1}/2 and the line has folded slope tan s_n; the hypothesis tan(δ_{n+1}/2) ≤ tan(s_n)/2 is verbatim α′'s. Strip disjointness (≥ 3/4 vertical separation) keeps rows n, n+2 out of the h-strip at ℓ_n, so "uncovered by row n+1" = "uncovered by the packing" under the stated row organization. The two-regime summation (all-small vs. one-large term) checks, including tan s ≥ s. The honest residue (rough interfaces; provenance of the row decomposition) is exactly as stated. With my α′ sharpening the conclusion improves for free to **G ≥ (X/120)·min(Θ, 1/3)**.

---

## F3 Claim 2 — Comparison Identity Theorem. CORRECT.

(i) *Validity + G′ = G ⊔ R.* Containment |x cos t + y sin t| ≤ (d/2c)(cos t + sin t) = d/2 (both coordinates) ✓; S′_i ⊆ S_i preserves disjointness and containment; G′ = G ⊔ R up to null sets ✓.

(ii) *Av′ = Av \ π(R) exactly, a.e. logic.* C′(p) = C(p) − #(Λ_p ∩ R) a.e. (boundaries null). Budget C ≤ N a.e. holds for **any** packing, any sizes/orientations (disjoint squares in T; a.e. shift has exactly N lattice points in T, each counted at most once — double-count shifts are null). Then C′ = N ⇔ [C = N ∧ Λ_p ∩ R = ∅], so Av′ = Av \ π(R), Av′ ⊆ Av, and with D1's Av = π(G)ᶜ: |Av| − |Av′| = |Av ∩ π(R)| = |π(R) \ π(G)|. The orchestrator's directional worry is indeed resolved by C′ ≤ C pointwise. **Exact, airtight.**

(iii) *Exchange identity.* (1−d′)² − (1−d)² + d² − d′² = 2(d−d′) — pure algebra, re-verified by sympy (`algebra_check.py`: both identities `True`) and by hand. With d′ = d/c: 2d(1−1/c). ✓

(iv) *Master equivalence.* Direct substitution of (ii)+(iii) into |Av| ≤ s; the bound RHS ≤ 2Σ(d−d′) follows from |π(R)\π(G)| ≤ |R| and (iii). ✓

*New numerics (mine).* The author's families are cell-confined. I tested a **side-1.2, diam > 1 tilted square crossing all four cells of k=2** (valid, SAT/containment-checked): subset violation 0, |Av\Av′| = |π(R)\π(G)| to grid precision, exchange identity exact to 6 decimals, over-budget measure 0. Plus the author's famA: 24 configs, `diff = piRnG` to 1e-5, `red_ok ≡ margin` throughout. The theorem's "any sizes, any orientations" scope is genuine.

Post-refutation note: since FCMB is now refuted, (iv) reads correctly as an *exact change of coordinates* (as F3's own Claim 3 concedes); its surviving value is Claim 1's impossibility result and the two-regime slack diagnosis, not a reduction route.

## F3 Claim 4 — tilt-neutrality of |Av|. CORRECT.

|π(S)| ≤ |S| with equality iff no two points of S differ by a nonzero integer vector; diam = d√2 < 1 (or S inside an open unit cell) forces this, so **|π(S)| = d², tilt-independent** — one line, correct. My direct fold-measure check (900² grid, d ∈ {0.5, 0.69}, t ∈ {0, 0.2, 0.5, π/4}): constant to ≤ 5e-4 (pixelization noise only). `tests2.py` Test 1: |Av| = 0.361110 across t ∈ {0.2, 0.4, 0.6}, pred 0.361111, with clearance and no shrinking. The claim that session-1's "tilted perturbations strictly decrease |Av|" is 100% shrinkage artifact is **justified for the family session-1 observed it on** (cell-confined split-cell, where |Av| routes through |π(S_a)|+|π(S_b)| exactly); the write-up correctly scopes the general statement to "configurations where Av decomposes through |π(S)|" and correctly flags the w > 1 folded-footprint case as GAP-2. The strategic corollary — any tilt penalty must come from packing geometry, not capture measure — stands.

## F3 Claim 5 — tightness-manifold FCMB with two tilted squares. CORRECT.

Each step verified per the assignment's checklist:
- Unit cells capture exactly 1 for a.e. p (the "every p" in D6 needs an a.e. caveat for phase-0 boundary shifts — cosmetic only). ✓
- Open cell holds exactly one lattice point a.e. ✓; S_a, S_b ⊆ closed cell capture only that point a.e. ✓
- Disjointness of the two capture events: direct (disjoint interiors ⇒ q in both only on the shared boundary, null); the budget argument (both ⇒ C = N+1 > N) is a valid alternative. ✓
- Measures: p ↦ q(p) is a piecewise-translation bijection torus → cell (measure-preserving), so |{q ∈ S_a}| = a² for **any** orientation — this doesn't even need D5's folding language. ✓
- s = (1−a)² + (1−b)², s − |Av| = 2(1−a−b) ✓ algebra.
- a + b ≤ 1 = f(2) = 1 with arbitrary orientations: an **external dependency, but a discharged one** — the report proves it self-contained with rigidity (ERDOS_106_REPORT.md §3; NOTES.md lists two independent proofs), and the rigidity version is exactly what the equality-case remark ("forces the AP split-cell family") needs. Should be cited explicitly at that point in D6.

Numerics reproduce: 0/25 mismatches (`tests2.py`), famA margin = 2a(1−1/c) to ≤ 1.5e-3 at 24 (a,t) pairs. This is a genuine unconditional theorem, and it coexists consistently with the session's FCMB refutation: the deficient-column counterexamples live off this manifold.

## FCMB refutation arithmetic (re-verified in passing, as instructed)

k+1 squares of side a = k/(k+1) stacked in one column + k(k−1) units: count k²+1 ✓; column fits (width a < 1, height (k+1)a = k) ✓; s = (k+1)/(k+1)² = 1/(k+1) ✓; |Av| = |{x-phase ∈ (0,a)}| = k/(k+1) exactly (column captures all k of its lattice points iff the x-phase lands in the column; verified by an exact brute-force grid at k=3: |Av| = 0.7500 = pred, over-budget = 0) ✓; |Av| = k/(k+1) > s for k ≥ 2, FCMB refuted; g = k/(k+1), **g + s = 1 exactly** — the conjecture holds with equality, so the refutation kills only the FCMB proof-route, not the target. Foldloss cross-check: foldloss(G) = (k−1)/(k+1) > e = 0, consistent with F3's Claim 3 equivalence.

## Summary of required corrections

1. **F5 Claim 2 / derivations §2**: replace the per-abscissa chord dichotomy with the separating-line uniform dichotomy; add the expanded re-anchoring (argmin-anchor on the window, both growth rates ≥ τ₁); **replace 1/520 and 1/585 by 1/240** (optimized) or 1/920 (conservative) — the current constants are unproved because crest squares may poke above ℓ outside e's span. Rescale Claim 6/§6 citations of 520/585 accordingly (conclusions unchanged).
2. **F5 Claim 1**: optionally adopt the free sharpening 228 → 60, 456 → 120 (dichotomy at |N₀| = X/45); Claim 3 then gives (X/120)·min(Θ, 1/3).
3. **F3 Claim 5 / D6**: cite the report's rigidity-strengthened f(2)=1 (§3) explicitly for step (4) and for the equality case; change "for every p" to "for a.e. p" in step (1).
4. F3 Claims 2 and 4: no corrections needed.