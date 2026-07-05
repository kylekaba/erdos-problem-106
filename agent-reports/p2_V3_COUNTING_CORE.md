# VERIFICATION REPORT — V3: counting core (Route A Claim 10, NUM_CONSTANTS Claim 2, NOTES §3 identity)

Numerics: `/private/tmp/claude-501/-Users-kylekabasares-Desktop-erdos-106/6b0597a9-48bd-4e8c-a957-7fc4a05f26d8/scratchpad/verify_v3/{single_square.py, misc_checks.py, packing_mechanism.py}`. All runs reproduced below where load-bearing.

---

## 1. Route A Claim 10 (Theorem C)

**VERDICT: CORRECT** (proof sound step by step; constant sharpenable from 2(k²+2) to 2(k²+1); one false parenthetical side-remark at k=1; one WLOG phrasing to fix).

### Step-by-step audit

**(i) Measure bound |A| ≥ t/(t+M).** Exact rederivation: S(x) := Σpᵢ(x) is integer-valued for *every* x (each pᵢ is a count), so on A^c := {S ≤ k²+1}^c we have S ≤ k² (integer < k²+1). Pointwise sup: an interval of length w (closed) contains at most ⌊w⌋+1 points of Z+x in all cases, including w ∈ Z (then ⌊w⌋+1 = w+1, attained only non-generically); so S ≤ Σ(⌊wᵢ⌋+1) ≤ W_tot + M everywhere. Then
W_tot = E[S] ≤ (1−|A|)k² + |A|(W_tot+M) ⇒ t ≤ |A|(t+M) ⇒ **|A| ≥ t/(t+M)**, valid for every t > 0 — no case split needed between t < 1 and t ≥ 1; large t only pushes the bound toward 1, harmlessly. The identical bound for B uses E[Σqᵢ] = W_tot, which holds because **both** projections of a square have the same width wᵢ = dᵢ(cosθᵢ+sinθᵢ) — correct for any tilt. Also note the proof bounds t = W_tot − k² and then uses ε ≤ t (since wᵢ ≥ dᵢ); this direction is fine. Empirical adversarial test: 2000 random synthetic instances of Σpᵢ, **0 violations** of |A| ≥ t/(t+M) (misc_checks.py §3).

**(ii) E[ΣLᵢ] = Δ.** For any measurable region R, E_{(x,y)}[#(Λ∩R)] = area(R) (Fubini). The four corner triangles of bbox(Sᵢ) have total area wᵢ² − dᵢ² = dᵢ²((cos+sin)²−1) = dᵢ² sin2θᵢ. ✓. Grid-verified at 15 (d,θ) pairs to grid precision ~5·10⁻⁴ (single_square.py, col E[L]).

**(iii) Markov.** ΣLᵢ is a nonnegative integer at generic shifts, so |{ΣL ≥ 1}| ≤ E[ΣL] = Δ. ✓.

**(iv) The counting chain.** At a generic shift (no lattice point on any ∂Sᵢ, ∂bbox(Sᵢ), or ∂T — still a null-set exclusion since these are finitely many segments), the identity cᵢ = pᵢqᵢ − Lᵢ holds: vertical line meets bbox ⟺ meets S (full extent by convexity), so lattice points in bbox = pq exactly, split into int S (= c) and open triangles (= L). Verified with **0 violations** on 2.25M-shift grids at 15 (d,θ) pairs. With Lᵢ = 0: cᵢ = pᵢqᵢ ≥ pᵢ+qᵢ−1 ⟺ Bᵢ = (pᵢ−1)(qᵢ−1) ≥ 0, which needs only "not (p=0, q≥2)": p = 0 forces w < 1 (generically), and then q ≤ 1 since q ∈ {⌊w⌋,⌊w⌋+1} = {0,1}. The p=q=0 case gives c = 0 ≥ −1 and enters the sum bookkeeping Σcᵢ ≥ Σpᵢ + Σqᵢ − M harmlessly. |p−q| ≤ 1 in full strength is **not needed** — only the excluded corner (0,≥2), which the equal-width mechanism kills.
**Budget:** at any shift with x,y ∉ Z, Λ∩[0,k]² = Λ∩(0,k)² has exactly k² points. At a generic shift every counted lattice point is interior to its square; disjoint interiors ⇒ points counted by different squares are distinct (a shared boundary lattice point is excluded by genericity, and the chosen point is generic since A×B minus the bad set minus the null set has measure ≥ |A||B| − Δ > 0). So Σcᵢ ≤ k² < k²+1 ≤ Σcᵢ, contradiction. ✓. End-to-end mechanism test on an actual 4-square mixed (axis-parallel + two-tilt) packing in [0,2]²: 160,000 shifts, **0 budget violations, 0 chain violations** on the 116,080 shifts with all Lᵢ=0 (packing_mechanism.py).

**(v) Final algebra.** (t/(t+M))² ≤ |A||B| ≤ Δ ⇒ t ≤ √Δ·M/(1−√Δ); √Δ ≤ 1/2 ⇒ multiplier ≤ 2√Δ, with equality exactly at Δ = 1/4 (numerically confirmed). ε ≤ t finishes. ✓. Note ε ≤ 0 makes the conclusion trivial, and Δ = 0 needs only |A||B| > 0, so BKU is genuinely recovered.

### Errors found (all minor, none fatal)

1. **Constant:** M = k²+1, so the proof yields Σdᵢ ≤ k² + 2(k²+1)√Δ; the stated 2(k²+2) is a needless weakening. (Suspect a typo/safety pad.)
2. **False side-remark at k=1:** "θᵢ ≤ 2⁻⁷k⁻⁶ suffices to beat Cauchy–Schwarz". Beating CS needs √Δ < (k√(k²+1)−k²)/(2(k²+2)); the recipe gives √Δ ≤ 1/(8k²). Numerically: k=1 threshold 0.0690 < 0.125 — **fails**; k ≥ 2 passes (0.0313 < 0.0393 at k=2, margins grow). Fix: restrict to k ≥ 2 (or use 2⁻⁹k⁻⁶). Irrelevant for k=1 anyway (f(2)=1 known).
3. **WLOG phrasing:** "axis swap for θ ∈ (π/4,π/2)" is not a legal global operation per square. Unneeded: the identity c = pq − L, the equal-width fact, and triangle area d²|sin2θ| all hold verbatim for any tilt with θ read mod π/2; define Δ := Σdᵢ² sin(2θ̃ᵢ), θ̃ᵢ ∈ [0,π/2) the mod-π/2 representative (sin2θ̃ ≥ 0 automatically). No configuration is ever transformed.

### Strongest correct version (proved by the audited argument)

> **Theorem C′.** Let M = k²+1 squares with pairwise disjoint interiors lie in [0,k]², sides dᵢ, tilts θᵢ (mod π/2), Δ := Σᵢ dᵢ² sin(2θ̃ᵢ). If Δ < 1 then
> **Σᵢ wᵢ ≤ k² + √Δ·(k²+1)/(1−√Δ)**, where wᵢ = dᵢ(cosθ̃ᵢ+sinθ̃ᵢ) ≥ dᵢ; in particular Σdᵢ ≤ k² + √Δ(k²+1)/(1−√Δ), and for Δ ≤ 1/4, Σdᵢ ≤ k² + 2(k²+1)√Δ.

Note it bounds the *larger* quantity Σwᵢ, and holds for all Δ < 1, not just ≤ 1/4. Unscaled: Σsᵢ ≤ k + √Δ(k²+1)/(k(1−√Δ)).

---

## 2. NUM_CONSTANTS Claim 2

**VERDICT: CORRECT** (all of (a)–(e); the inscribed-square sub-claim is true and admits a fully rigorous one-line proof; the d=1 edge case is handled by the sharp — not just area — bound).

**(a) c ≤ pq.** Each lattice point of S lies on one of the p columns and one of the q rows; the map point ↦ (column,row) is injective. ✓ (subsumed by the exact c = pq − L, verified 0 violations on 2.25M shifts × 15 pairs).

**(b) p,q ≤ 2, consecutive columns when p=2.** w ≤ √2 < 2 ⇒ p ≤ ⌊w⌋+1 ≤ 2; two points of Z+x at spacing ≥ 2 need interval length ≥ 2. ✓. Verified: p,q ∈ {⌊w⌋,⌊w⌋+1} with 0 violations.

**(c) D ≥ −1, equality iff p=q=0.** Case check verified exhaustively on grids (columns `D=-1V`, `minD`: minD = −1 exactly when w < 1, minD = 0 when w ≥ 1; the event D=−1 coincided with {p=q=0} at every one of ~34M tested shifts).

**The (2,2) sub-case — the sharp inscribed-square claim.** c = 4 would put four lattice points at spacing exactly 1×1 (consecutive columns and rows) inside S; convexity puts their hull, a closed axis-parallel **unit** square Q, inside S. Rigorous kill, valid **including d = 1 exactly** (where the area argument fails):

> *Lemma.* If an axis-parallel square of side s is contained in a square S of side d tilted by θ ∈ (0,π/4], then s(cosθ+sinθ) ≤ d; hence the largest such inscribed square has side exactly d/(cosθ+sinθ), attained by the concentric axis-parallel square.
> *Proof.* Project onto the direction of an edge of **S** (not onto the lattice axes — projecting onto the lattice axes gives only 1 ≤ w, no contradiction; this is the one place a careless proof goes wrong). proj(S) has length d; proj(Q) has length s(cosθ+sinθ) since Q's edges make angle θ with the projection direction. Containment ⇒ s(cosθ+sinθ) ≤ d. Attainment: the concentric axis-parallel square of side s* = d/(cosθ+sinθ) has corners mapping (in S's frame, center at origin) to (±d/2, ±s*(cosθ−sinθ)/2) and (±s*(sinθ−cosθ)/2, ±d/2), all in [−d/2,d/2]². ∎

So Q ⊆ S forces cosθ+sinθ ≤ d ≤ 1, false for θ ∈ (0,π/4] where cosθ+sinθ > 1 strictly. Hence c ≤ 3 and D ≥ 0 on (2,2). The "is the concentric one really maximal" worry is resolved affirmatively — the projection bound is placement-free, so maximality of the concentric square is a corollary, not an assumption. **LP verification** (16 linear constraints, maximize s over placements): LP optimum = d/(cosθ+sinθ) to machine precision (diff ≤ 2·10⁻¹⁶) at all 15 tested (d,θ). Empirically max c on the (2,2) event was **1** in all runs — comfortably below the proved bound 3.

**(d) E[D⁺] = 2w − 1 − d² + (1−w)₊², and D ≥ 0 pointwise at d=1.** Since D ≥ −1 with D = −1 exactly on {p=q=0}, D⁻ = 1_{p=q=0}, so E[D⁺] = E[D] + P(p=0)P(q=0) = (2w−1−d²) + (1−w)₊² (x,y independent; P(p=0) = (1−w)₊). At d=1: w > 1 ⇒ p,q ≥ 1 generically ⇒ D ≥ 0 pointwise by (c), and E[D⁺] = 2w−2 = surplus, exactly. Grid-verified to ≤ 7·10⁻⁴ at 15 pairs including (1, 0.25°), (1, 45°); minD = 0 at d=1 for all tested angles. ✓.

**(e) Small-θ slope 2d².** For d < 1 and small θ (w < 1): E[D⁺] = w²−d² = d²sin2θ (a pleasant simplification the report doesn't state), slope 2d²cos2θ → 2d². For d = 1: E[D⁺] = 2(cosθ+sinθ−1), slope → 2 = 2d². Numerically E[D⁺]/θ = 2d² to 4 decimals at θ = 0.05° for d ∈ {0.6, 0.85, 1.0}. ✓.

**Sharpened form:** for w ≤ 1 the closed form collapses to **E[D⁺] = d² sin2θ = E[L]** exactly (all defect mass, no budget offset); for w ≥ 1, E[D⁺] = 2w−1−d² and D ≥ 0 pointwise (d ≤ 1). This joins seamlessly to Route A Claim 8's two branches.

---

## 3. NOTES.md §3 exact criticality identity

**VERDICT: CORRECT — and it extends beyond the stated range 1 ≤ w ≤ 2 to all 0 ≤ w ≤ 2.**

Ingredients, each verified: E[p] = E[q] = w; E[e] = w² − d² (e ≡ L); E[(p−1)(q−1)] = E[p−1]·E[q−1] by x/y independence. For 1 ≤ w ≤ 2, p−1 ~ Bernoulli(w−1) (interval of length w ∈ [1,2) contains 2 points with probability w−1) ⇒ E[B] = (w−1)². Algebra: 2(w−d) − (w²−d²) + (w−1)² = d² − 2d + 1 = **(1−d)²**, an identity in (d,w) — machine-precision residual ≤ 7·10⁻¹⁶ over 10⁵ random (d,θ), and measured (grid) LHS matched (1−d)² at every tested pair (e.g. d=0.9,θ=20°: 0.01042 vs 0.01; d=1: |LHS| ≤ 6·10⁻⁴ ≈ grid noise).

**Sharpening (new):** for w < 1, (p−1)(q−1) = 1_{p=0}1_{q=0}, so E[B] = (1−w)² = (w−1)² — the *same formula*. Hence the identity
$$2(w-d)\;-\;\big(\mathbb E[e]-\mathbb E[(p-1)(q-1)]\big)\;=\;(1-d)^2$$
holds for **all** 0 ≤ w ≤ 2 (i.e. all d ≤ 2/(cosθ+sinθ)), not only 1 ≤ w ≤ 2. Only the Bernoulli *justification* changes across w = 1; the value doesn't.

**Interpretation audit.** Since c = pq − e and pq = p+q−1+B pointwise, D = e − B pointwise, so "net counting defect" = E[D] — a *signed* mean. The identity is thus: surplus − E[D] = (1−d)², an exact first-moment statement. Two caveats confirmed as consistent rather than contradictory:
- For d ≤ 1 and w ≥ 1, D ≥ 0 pointwise (Claim 2(c)), so E[D] = E[D⁺] and the identity is exactly Claim 2(d) rearranged: the "in expectation, margin (1−d)², vanishing iff d=1" reading is fully rigorous there.
- For w < 1, the operationally relevant quantity is E[D⁺] = E[D] + (1−w)², and surplus − E[D⁺] = (1−d)² − (1−w)² = (w−d)(2−d−w) = dσ(θ)(2−d−w) — precisely Route A Claim 8's w ≤ 1 branch. So the three documents (NOTES §3, NUM Claim 2, Route A Claims 6/8) are mutually consistent to identity level; cross-check (w−1)² − dσ(d+w−2) = (1−d)² residual ≤ 7·10⁻¹⁶.

The strategic conclusion drawn in NOTES §3 ("exactly critical in expectation at every tilt; first-moment arguments cannot decide it; must use max-over-shift or geometric structure") is a correct reading of a correct identity, with the one caution that at d > 1 the identity still holds but D ≥ 0 is no longer pointwise-guaranteed, so "margin (1−d)² > 0 for d > 1" is a statement about the signed mean only.

---

## Summary table

| Claim | Verdict | Notes |
|---|---|---|
| Route A Claim 10 (Theorem C) | **CORRECT** | Sharpen: Σwᵢ ≤ k² + √Δ(k²+1)/(1−√Δ) for all Δ < 1; constant 2(k²+1) not 2(k²+2); k=1 "beats CS" side-remark false; replace axis-swap WLOG by per-square mod-π/2 reading |
| NUM_CONSTANTS Claim 2 (a)–(e) | **CORRECT** | Inscribed-square sub-claim proved sharply (project in S's own frame; LP confirms d/(cos+sin) to 1e-16); covers d=1 exactly; bonus: E[D⁺] = d²sin2θ for w ≤ 1 |
| NOTES §3 identity | **CORRECT** | Extends to all 0 ≤ w ≤ 2 (E[B] = (w−1)² on both sides of w=1); "net defect" is signed E[D]; equals E[D⁺] iff d ≤ 1, w ≥ 1 |

No counterexamples found despite adversarial search: 0 violations of c = pq−L, p,q ∈ {⌊w⌋,⌊w⌋+1}, D ≥ −1 iff-condition, c ≤ 3 on (2,2) (~34M shifts, 15 (d,θ) pairs); 0 violations of |A| ≥ t/(t+M) (2000 random instances); 0 budget/chain violations in the end-to-end packing test (160k shifts).

Scripts: `/private/tmp/claude-501/-Users-kylekabasares-Desktop-erdos-106/6b0597a9-48bd-4e8c-a957-7fc4a05f26d8/scratchpad/verify_v3/single_square.py`, `.../verify_v3/misc_checks.py`, `.../verify_v3/packing_mechanism.py`