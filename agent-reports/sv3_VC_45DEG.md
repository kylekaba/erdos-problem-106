All verification complete. Final report follows.

---

# ADVERSARIAL VERIFICATION — ASSIGNMENT VC (G5 45° closure suite + G3 Theorem I constants)

Independent code: `/private/tmp/claude-501/-Users-kylekabasares-Desktop-erdos-106/6b0597a9-48bd-4e8c-a957-7fc4a05f26d8/scratchpad/vc_check.py` (all my own implementations; brute-force lattice counts, independent packing generator, independent constant optimizations). Sources verified: `/Users/kylekabasares/Desktop/erdos-106/agent-reports/session3-derivations/G5_45FORTRESS_derivations.md`, `.../G3_BRIDGE_I_derivations.md`, `s3_G5_DIAMOND.md`, `s3_G3_INCOHERENCE.md`, cross-checked against `p2_V1_T1_TILINGS.md` (Claim 6 sharpened Wall Lemma) and `sv_V3_ALPHAPRIME_F3.md` (corrected α′-edge, 1/240).

## G5 VERDICTS

**Master identity 2ε+G+s = 1 (n = N+1): CORRECT.** G+s = N−Σd² + (N+1) −2Σd + Σd² = 2N+1−2Σd = 1−2ε. Machine-confirmed to 1e−12 on random d-vectors. Requires exactly n = N+1; tilt-independent.

**Theorem 45-A: CORRECT.** Every link re-derived:
- Sharpened Wall Lemma: coefficient sinθcosθ/2 comes from the two-slope wedge (tanθ, cotθ): sublevel set of level c has length c(tanθ+cotθ)⁻¹·… giving min ∫ = (sc/2)L²; at 45° both slopes are 1, coefficient 1/4, tight (matches p2_V1's proof, which I checked line-by-line). My independent numeric test on three random 45° packings I generated myself (k = 5, 6, 8; SAT-disjoint in the rotated frame; 40001-point quadrature): LHS ≤ ∫φ ≤ G, PASS all three (e.g. k=6: 5.006 ≤ 5.231 ≤ 23.042).
- **Disjointness: yes, automatic.** For any column x meeting a square, φ_floor(x) ≤ (bottom of that square's chord) ≤ (top) ≤ k−ψ_ceil(x), so the gap segments [0,φ) and (k−ψ, k] are disjoint pointwise; both uncovered; empty columns contribute k exactly once via k|A_∅| (no double count — checked the bookkeeping in (*)).
- Constant chain: G ≥ (1/4)(k−a)²(1/m₁+1/m₂) + ka with m₁,m₂ ≤ N+1 gives G ≥ (k−a)²/(2(N+1)) + ka; derivative in a is k − (k−a)/(N+1) > 0 ✓, so G ≥ k²/(2(N+1)) = N/(2(N+1)); identity gives ε ≤ 1/2 − N/(4(N+1)) = **1/4 + 1/(4(N+1))** exactly. k=1: 3/8; k=2: 0.30; limit 1/4. All confirmed.

**Theorem 45-B: CORRECT; threshold 28 confirmed, does not shift.**
- s < 1 structure: d_i < 2 ✓; #{d ≤ 1/2} ≤ 3 (each pays (1−d)² ≥ 1/4 to s < 1) ✓; G < 1 ✓ (all from 2ε+G+s=1 with ε>0).
- Strip count: 45° square with d < 2 has vertical extent √2d < 2√2; y_i ≤ h puts it in the strip of area k(h+2√2); area > 1/4 each ⟹ **M < 4k(h+2√2)** ✓ (strict).
- Ledger: interior minimum S₁* = 2Mh gives hk − Mh² − hσ₃, boundary branch k²/(4M) − hσ₃; my exact recomputation: interior coefficient h − 4h²(h+2√2) = **0.0216421** (they state 0.0216415/0.021642 — conservative, fine), boundary 1/(16(h+2√2)) = 0.0217889, σ₃ = 3√2/2 = 2.12132, hσ₃ = 0.084853. Doubling via the disjoint ceiling region (empty-column term absorbs correctly: G ≥ 2(hk−Mh²−hσ₃) + a(k−2h)): **G > 0.0432841k − 0.16971; threshold k > 27.0239 → k ≥ 28** exactly as claimed; at k=28, G > 1.0423 > 1 = contradiction with G < 1. ✓
- **Free sharpening (verified rigorously in code): the threshold drops to k ≥ 10.** Two waste-free improvements: (i) fold the ≤3 tiny servers into the Cauchy–Schwarz denominator instead of subtracting their served length (σ₃ term vanishes; −hσ₃ → −3h²; alone this gives k ≥ 24); (ii) δ-window: #{|d−1| ≥ δ} ≤ s/δ² < 1/δ², so with δ = 0.28 at most 12 servers are exceptional and the remaining low servers have d ∈ (0.72, 1.28): strip height h+1.28√2, area > 0.5184, giving M̄ ≤ k(h+1.81019)/0.5184 + 12. With h = 0.10: G > 2·min(hk − M̄h², k²/(4M̄)) = 1.0230 at k=10, and > 1 for all k ≥ 10 (checked k = 10…199; k = 9 peaks at 0.9025 over the full (δ,h) grid, so 9 needs a second idea). **Open window shrinks from k ∈ [2,27] to k ∈ [2,9].**

**Theorem CO: CORRECT.** Scaling verified: extent d(cosθ+sinθ) < 2√2 (d<2, cos+sin ≤ √2); coefficient sin2θ/4; with h = 0.04sin2θ, I verified min over sin2θ ∈ (0,1] of [h − (4/sin2θ)h²(h+2√2)]/sin2θ = 0.0216421 on a 1000-point grid; G > 0.0432841·k·sin2θ − 0.1697, so **k ≥ 28/sin2θ suffices** ✓ (G > 1.0423). Same sharpening applies verbatim (h = 0.10sin2θ, δ = 0.28): interior value = sin2θ(0.063152k − 0.12), boundary = sin2θ·k/19.539; both branches exceed 1/2 at k·sin2θ ≥ 10, so **CO holds for k ≥ 10/sin2θ**.

**Theorem D45 + landscape: CORRECT.** 
- **D-formula: EXACT match on my fully independent implementation — 56,000/56,000 shifts** (12,000 each for k = 3, 5, 8, 12; 4,000 each for k = 29, 41; brute-force count of Z²+(x,y) in the diamond vs. the closed form; integer-exact via −4Kγ−2γ² = 2K²−k²). The derivation (a=m+n, b=m−n parity factorization; A_e = K+χ(s); σ 1-periodic with the stated two shapes for γ<1/2 and γ>1/2) is algebraically sound — I re-derived each step.
- **Four regimes: 0 violations in 56,000 shifts using the brute-force D** (not the formula), and re-derived symbolically: (0,1/4]: cell (0,0) has D = −4Kγ−2γ² < 0 with X forced 0 (X ≠ 0 requires both σ = 1) → union; (1/4,1/2): cells (1,0)/(0,1) have X = 0, D = K(1−4γ)−2γ² < 0 → intersection; (1/2,3/4]: at σ+σ = 2 exactly one χ is on per phase so X ≤ 1 and D ≤ (2−4γ)K+1−2γ² < 1 for K ≥ 1 → union; (3/4,1): at σ+σ = 3, X = 1 exactly and D ≤ 4−4γ−2γ² < 0 → intersection. All unconditional in K ≥ 1 as claimed (K ≥ 1 needs k ≥ 2; k=1 is T1's — worth one sentence in the writeup).
- Chain: Σp_iq_i ≤ k²+D is sound (all squares axis-parallel in one frame — this is exactly why the route is pure-45-only), P+Q+R+W = 2N+1+D and |A|,|B| ≥ ε (all-short) re-derived; A×B ⊆ {D≥1} ✓.
- **Raikov step: rigorous, and genuinely needed.** The upgrade A → W = {x: μ(B∖(U−x)) = 0} (level set of the continuous g(x) = μ(B∩(U−x)), hence closed, ⊇ A a.e. by Fubini) and B → B* (closed support, full measure, W+B* ⊆ closure(U)) is the standard essential-sumset reduction, correctly executed; W+B* is compact hence measurable. Interval arithmetic (lifting to ℝ and using supA+supB−infA−infB ≤ |J|) suffices only when 2|U| ≤ 1; in the intersection regimes |U| = 2γ ∈ (1/2,1) (resp. 2γ−1 up to 1) can exceed 1/2, where wraparound kills the elementary argument — so the Raikov/Macbeath citation is load-bearing and correct (circle-group Cauchy–Davenport, Raikov 1939 measurable / Macbeath 1953 compact torus).
- b(γ) table and examples confirmed (k=17: 0.0833; k=29: γ = 0.5061, b = 0.0244; k=58: 0.0488; k=10: 0.2843). **"Sub-C-S for 3/4 density of k": CORRECT as the conditional (all-short) statement it explicitly is**: b < 1/2 exactly off [1/8,1/4]∪[5/8,3/4] (measure 1/4; equidistribution of frac(k/√2) since √2/2 irrational). The obstruction list (big squares break |A| ≥ ε; fat-arc γ vacuous; tightness of b for the counting information) is honest and matches my analysis.

## G3 VERDICTS

**Lemma E-wall, constant 1/252 (the flagged un-cross-checked constant): CORRECT — independently re-derived.** The floor-as-occupant step is sound: with 0 ∈ A_w, the floor line has in-frame folded slope ≤ tanφ₀, so D_fl′ = τ−s ≥ τ₁; D_fl ≥ 0 on the window because e ⊆ T (e coincides with its line over the span); left-endpoint anchoring gives the same envelope D_fl ≥ τ₁|x−a_fl| — legitimately one extra crest, J+1. Floor-crest cap: 2h/1.06 = 0.4717 ≥ 1/3 so τ₂ unchanged ✓. My independent reconstruction of the λ-dichotomy assembly (branch 1: c ≤ 3hλX; branch 2: c ≤ (1−λ)²X²/(4(J(X)+1)) with the sv_V3-corrected poke-zone crest count J(X) = [(X+2.98)·3.23 + 2·1.49·2.98]/0.9025; J(0.63)+1 = 23.760 ✓): optimizing over λ and minimizing over X ∈ [0.63,1.06] gives **c* = 1/243.7 (they: 1/243.8) — stated 1/252 is valid with margin**. (My same machinery reproduces the interior case at 1/234–1/240, consistent with sv_V3's 1/240.) Corner exclusion |E_exc| ≤ 16 checks: quarter-disk area π(1.74)²/4 = 2.378, /0.9025 = 2.64 → ≤2 squares per corner; ≤2 both-wall edges per square (only the two edges adjacent to the corner-nearest vertex can have points within 1/4 of both walls — verified for both axis-parallel and 45° extremes).

**Theorem I disjointification (multiplicity 20): CORRECT.** Exact statement: dist(p,S) ≤ dist(p,e) ≤ 1/4, so S ⊆ B(p, 1/4 + √2·1.05) = B(p, 1.73492) (equivalently: center within 1/4 + diam/2 = 0.99246, then square ⊆ B(p, 0.99246+0.74246) — same radius). π(1.735)²/0.9025 = 10.478 → **≤ 10 squares**. Opposite outward open half-planes are separated by the square's slab of width ≥ 0.95 > 0, so ≤ 1 edge per opposite pair, **≤ 2 edges per square → 20**. In the Corollary-H application the outlier square (possibly area < 0.9025) does not break this: its edges are excluded from E*, and for the restricted sum only the ≤ 10 (H)-compliant squares near p are counted.

**5040/13000/6000 assemblies: CORRECT.** 252·20 = 5040, 650·20 = 13000, 300·20 = 6000; interior 1/240 ≥ 1/252 uniformization ✓; empty-strip backings 0.2375 ≥ (1/3)/252 and 0.06375 ≥ (1/3)/650 ✓; angle form via tan2x ≥ 2tanx and tan a − tan b ≥ a−b (both re-verified) ✓. I also sanity-reproduced the E-narrow Step-5 arithmetic at corner parameter values (my quick versions give 1/634 uniform, 1/282 small-mismatch vs. their scanned 1/639.8, 1/287.9 — consistent; stated 1/650, 1/300 safe).

**One flaw found (outside the three assigned items but in the same file) — Corollary H(c): CORRECT WITH FIXES.** The bound #{clean facing interfaces with m ≥ Δ} ≤ 12000c/Δ silently assumes all such interfaces have m ≤ 0.30 — interfaces with m > 0.30 are excluded from the /6000 sum that backs it. **Fix:** use the uniform I-narrow form: each clean facing interface with m ≥ Δ ≤ 0.3 pays ≥ min(tanΔ,1/3)/650 = tanΔ/650, giving **≤ 26000c/tanΔ ≤ 26000c/Δ** (or keep 12000c/Δ restricted to m ∈ [Δ, 0.30] and add ≤ 26000c/tan(0.30) ≈ 84,100c for m > 0.30). Also the commentary "≤120 out of ~2k², <1% for k ≥ 35" is arithmetically off even before the fix (120/2450 = 4.9%); with the fix, <1% needs k ≳ 114 at Δ = 0.1. Theorems I/I-narrow and H(a),(b),(d) are unaffected; H(b)'s "≤31" is a safe rounding of 30.24.

## SUMMARY TABLE

| Claim | Verdict |
|---|---|
| G5 master identity | CORRECT |
| G5 Theorem 45-A (ε ≤ 1/4 + 1/(4(N+1))), disjointness automatic | CORRECT |
| G5 Theorem 45-B, threshold k ≥ 28 | CORRECT (threshold confirmed exactly: 27.024→28) |
| G5 Theorem CO (k ≥ 28/sin2θ) | CORRECT |
| G5 D45 formula + 4 regimes + Raikov + 3/4-density | CORRECT (formula exact 56,000/56,000 independent; Raikov needed and rigorous; density claim conditional on all-short as stated) |
| G3 Lemma E-wall 1/252 | CORRECT (independently re-derived: 1/243.7) |
| G3 multiplicity 20 | CORRECT |
| G3 assemblies 5040/13000/6000 | CORRECT |
| G3 Corollary H(c) constant | CORRECT WITH FIXES (12000c/Δ → 26000c/tanΔ; "<1%@k≥35" commentary wrong) |

**Sharpenings delivered (all machine-verified):** 45-B threshold **28 → 10** (δ-window δ = 0.28, h = 0.10, fold tiny servers into Cauchy–Schwarz; single fixed parameter pair closes all k ≥ 10; k = 9 unreachable by this single-level scheme, max 0.9025); correspondingly **CO: k ≥ 10/sin2θ**. Pure-45 open window is now k ∈ [2,9].