All verification work is complete. Final report follows.

---

# ASSIGNMENT VA — Adversarial verification of G6's Marginal Displacement Theorem suite

**Independent code**: `/private/tmp/claude-501/-Users-kylekabasares-Desktop-erdos-106/6b0597a9-48bd-4e8c-a957-7fc4a05f26d8/scratchpad/va_mdt_verify.py` (written from scratch: own tilted-square geometry via vertex/edge chord intersection, own packings, 4001 generic phases per packing; did not reuse g6_check.py). All checks pass; details per claim.

## CLAIM 1 (Theorem G6-1, MDT) — VERDICT: CORRECT

Every step re-derived independently:

1. **Line inventory**: for generic x ∈ (0,1), the lines meeting (0,k) are exactly l_m = x+m, m = 0..k−1; every square's interior lies in (0,k)², so all incidences are on these k lines and every chord ⊆ [0,k]. Sound.
2. **Per-line capacity (G6-A)**: chords have pairwise-disjoint interiors (square interiors disjoint) inside a length-k segment ⟹ Σ_{i∈L_m} ch_i ≤ k. Sound. My numerics: 0 violations over ~48,000 line evaluations across 12 packings.
3. **Ledger**: P − N = Σ_m(|L_m| − k) ≤ Σ_m Σ_{i∈L_m}(1 − ch_i) is pure algebra from capacity (|L_m| − Σch ≤ |L_m| − k reversed correctly). Holds at *every* generic x, not just good x — 0 violations everywhere.
4. **Chord pinning at good x**: goodness (no line in any end region, i.e. x mod 1 ∉ ∪B_i^x) + Lemma 0 gives ch_i(x+m) = d_i secθ_i for every incidence, so the double sum equals Σ_i p_i(1 − d_i secθ_i). Confirmed to 1e-9 at all good phases. (Lemma 0 itself re-verified implicitly: my chord routine is independent geometry and always matched d secθ on middle regions.)
5. **Fact 1**: d secθ < 1 ⟹ d < cosθ ⟹ middle length d(cosθ−sinθ) < cosθ(cosθ−sinθ) = cos²θ − sinθcosθ ≤ 1, strictly (< is preserved: either cosθ > sinθ giving strict first step, or θ = π/4 giving middle length 0). At good x all incident lines lie in this one closed interval of length < 1; unit-spaced lines ⟹ p_i ≤ 1. Sound. I confirmed max_{[0,π/4]} cosθ(cosθ−sinθ) = 1 (attained only at θ=0, where d < 1 strictly anyway).
6. **Fact 2**: d secθ ≥ 1 ⟹ d ≥ cosθ ⟹ w ≥ cosθ(cosθ+sinθ) = (1+cos2θ+sin2θ)/2 ≥ 1 on [0,π/4] (√2·sin(2θ+π/4) ≥ 1 there; equality at endpoints — confirmed numerically, min = 1.000000000000). Open projection interval of length ≥ 1 contains a point of x+ℤ except on a null set (w = 1 with x ≡ endpoint); interior-meeting follows from convexity (chord > 0 on the open projection). Sound.
7. **Sign split**: the step I probed hardest. For a *surplus* square, p_i = 0 would violate the per-term bound (0 > 1−d secθ) — Fact 2 is exactly what excludes this, a.e. This is genuinely load-bearing and correctly supplied. Deficit squares with p_i = 0 contribute 0 ≤ (1−dsecθ)_+, fine. Surplus squares with p_i ≥ 2 make the term more negative — safe. Total ≤ n − Σd_i secθ_i. Sound.
8. **Hygiene**: the excluded set is (finite per square: 4 vertices + 2 bbox endpoints, k lines each) ∪ (w_i = 1 endpoint alignments) — null. All statements survive as "every generic good x". Symmetry in y via Lemma 0's 90° symmetry (same folded θ, same secθ, hence same ρ on both axes — needed later by S2′, and it holds).

**Numerics** (my own): 12 packings (U_2, U_3, T12 k=4, split cell a=0.37, tilted columns θ=0.02/0.05, adversarial fat tapered square, near-45°, oversize tilted d=1.5, random tilted k=3/4, deficient row), 4001 generic phases each: 0 violations of capacity, ledger, chord law, Fact 1, Fact 2, or MDT on good sets; E[P] = Σw_i to grid tolerance (≤3e-4). **Adversarial fat square** (d=0.89, θ=0.4: d secθ = 0.9663 < 1, w = 1.1663 > 1): p = 2 occurred on 666/4001 = 16.6% of phases (= w−1, as theory predicts), every one inside the square's own B-arcs; zero good-set Fact-1 violations. Reproduces and independently extends G6's 15.35% finding. Near-45° config: good set empty, MDT vacuous-not-wrong, as claimed.

**Tightness**: bound = +1.000 and max(P−N) = 1 attained on measure 0.6666 (U_2; k/(k+1)=2/3), 0.7501 (U_3; 3/4), 0.6666 (T12 k=4; 2/3), 0.3699 (split; a=0.37) — all as claimed. Deficient row: x-axis max(P−N) = 0, tight on y-axis only — confirms "≥1 axis". (Caveat: sharpness measure a for the split cell requires the standard stacked-column placement of the two split squares; diagonal placement gives measure 0. Not an error, just placement-dependent.)

## CLAIM 2 (Corollary G6-2, BKU) — VERDICT: CORRECT WITH FIXES

The proof is valid and non-circular: MDT (which for AP needs only capacity + p ≤ 1 for d < 1 + p ≥ 1 for d ≥ 1) + integrality + E[P] = Σd. Free sharpening: the argument works verbatim for all integer c > −k, not just c ≥ 0 (P ≤ N+c a.e. vs E[P] = N+c+ε), so it recovers BKU's *entire* Theorem 1.1 range without Praton's equivalence.

**Fix 1 (statement error)**: "g(k²+2c+1) = k + c/k, c ≥ 0 arbitrary" is FALSE as an equality for c ≥ k. Counterexample: k=2, c=3 gives n=11 and k+c/k = 3.5, but g(11) = 4 − 3/4 = 3.25 (via k′=4, c′=−3, inside BKU's range). Only the upper bound Σd ≤ N+c is proved for all c; equality requires −k < c < k (where the Erdős–Soifer/Campbell–Staton constructions exist). This propagates to the ENDGAME Claim 2 wording and should be corrected before entering §7C.

**Fix 2 (novelty overstated)**: I read `bku24.pdf` (Baek–Koizumi–Ueoro, arXiv:2411.07274). The paper contains **two** proofs. The report's description ("c = pq + two 1-D pigeonholes + lattice counting") matches only **Baek's** proof. The **Koizumi–Ueoro** proof is *already* single-axis, lattice-free chord counting: k vertical lines, one pigeonhole to an over-full shift (Σm_i ≥ k²+1), then per-square inequalities d_i ≤ 1/k for missed squares (= Fact-2 contrapositive) and d_i ≥ (m_i−1)/k for multi-hit squares (= Fact-1 species), closed by total-chord capacity ≤ k. That is the same signed ledger as MDT-AP, run in the opposite direction (max ≥ mean at one shift, instead of a.e. pointwise cap + integrality + mean). What is genuinely new in G6-2: (a) the a.e.-pointwise form P ≤ N+c (KU only get one bad shift); (b) all c in one stroke, no Praton reduction (BKU handle c ≠ 0 only by citing Praton [Pra08]); (c) the tilted extension (MDT proper) — BKU is AP-only and their d_i ≥ (m_i−1)/k step has no tilted analogue without Lemma 0. So: not "absent from BKU's paper" — its AP skeleton is half-present there; the honest claim is "a mirror-image reweighting of Koizumi–Ueoro that survives tilting and yields the pointwise/a.e. form."

## CLAIM 3 (G6-3 + S2′ + S3′) — VERDICT: CORRECT (S2′ conditional, as flagged)

- **G6-3**: ε+ρ > 0 ⟹ n − Σd secθ = 1−ε−ρ < 1 ⟹ P ≤ N a.e. good (integrality); some p_i = 0 since all p_i ≥ 1 would give P ≥ n = N+1. Sound (uses n = N+1, correctly stated). Boundary check ε = ρ = 0 → bound N+1, U_k full-hit measure k/(k+1): confirmed numerically.
- **S2′ substitution completeness**: I re-read `SQUEEZE_DERIVATIONS.md`. The *only* β<1 use in Theorem S2's proof is line 84: "By Lemma A″, for a.e. (x,y) in E: M_X(x) and M_Y(y) are both nonempty." G6-3 supplies exactly this from ε > 0, on both axes (y-axis MDT legitimate: Lemma 0's 90° symmetry gives the same folded θ, same secθ, same ρ). Every other step (E-structure c=pq, idle ledger |I| = 1+μ, disjoint products, V-arcs) is untouched by the substitution. Substitution COMPLETE. Inherited caveat correctly flagged: S2's idle-ledger assembly step remains unverified by an independent pass, so S2′/S3′ confidence is capped by that.
- **S3′ algebra**: re-derived symbolically: |Av| ≥ 1−g (Markov, hits integer ≥ 0, E[hits]=g); 1−g = s+2ε (uses n=N+1: 1−g = 1−N+Σd² = s+2ε ✓); (1−w)² = (1−d)² − dσ(2−d−w) is an exact identity ((1−d)²−(1−w)² = (w−d)(2−d−w) = dσ(2−d−w)); m_i ≥ 0 for shorts ✓; rearrangement gives U_x+U_y+V_x+V_y ≥ 2ε + Σ_{w<1}m_i + Σ_{w≥1}(1−d)² exactly as stated. Branch (i) of S3 (b₀ ≥ ε+Γ ⟺ β ≥ 1, via β = 1−ε+b₀−Γ, re-checked) is indeed deleted for every enemy. Correct.

## CLAIM 4 (β-frontier, T12) — VERDICT: CORRECT

Independent exact-fraction recomputation, b = 2..6 (one more than G6): widths k/(k+b) + k/(k+1−b) + (k−2) = k reduces to (2b−2)/(2b−1) + 2b/(2b−1) = 2 ✓ exactly at k = 2b(b−1); count = k²+1 ✓; Σd = k², ε = 0 ✓; **β = b(2b−1)·1/(2b−1) = b; b₀ = b0sec = (2b−1)(b−1)·1/(2b−1) = b−1** ✓. So β is unbounded on the catalogue and "extremals at β = 1" is false, while β − b0sec = 1 on every catalogued extremal (U_k: 1−0; split: (1−a)+a − 0 = 1; T12: b−(b−1); deficient row: 1−0) ✓. MDT tightness (max P−N = 1, positive measure, values matching exactly) confirmed above; deficient row saturates on one axis only, as claimed. The equality profile (all lines chord-tiled, deficit squares all incident, surplus squares single-incident) reads off the proof correctly — each inequality in the chain must be tight, and on U_k/T12 at full-hit phases the chords do tile each line by the exact width arithmetic. (Untested minor datum: "uneven U_3 = 0.50" — measure equals the intersection of the deficit-square hit intervals, side-set dependent; mechanism sound, exact value not reproduced.)

## CLAIM 5 (OC-FCMB multiplicity) — VERDICT: CORRECT

Layer-cake identity re-derived: E[hits] = Σ_{m≥1}|{hits≥m}| ⟹ Σ_{m≥2}|{hits≥m}| = g − |π(G)|; hits ∈ {0,1} a.e. ⟺ |π(G)| = g ⟺ fold a.e. injective on the gap. Trivially sound. U_k analytically: hits = k·1{x mod 1 ∈ gap-strip}, so E = k/(k+1) = g, |π(G)| = 1/(k+1) = g/k, multiplicity mass (k−1)/(k+1); my 2D-grid check reproduces all three for k=2,3 (0.3333/0.4994 vs exact 1/3, 1/2). The reverse-OC-FCMB counterexample arithmetic (mass → 1 while (b₀−ε)_+ = 0 on U_k) is confirmed; caveat: I could not inspect the original conjecture's residual "…" terms, but they are described as oversize/tilt-type and U_k has b₀ = ε = τ = 0, so the kill stands as stated.

## Brief note on Claim 6 (G6-5, not core-assigned)

Spot-checked: (a) follows from G6-3 + E[P]−N = t (Σw = N+ε+τ ✓); (b)'s key sub-step "deficit-chord squares have ≤ 1 middle-region line at ANY x" is right — the middle region has length < 1 regardless of goodness; my everywhere-ledger check (C2, 0 violations at all phases including bad ones) covers the skeleton. No error found.

## Summary of required edits before propagation to §7C

1. G6-2/ENDGAME Claim 2: replace "c ≥ 0" equality claim with: upper bound Σd ≤ N+c for all integer c > −k; **equality g = k+c/k only for −k < c < k** (counterexample at k=2, c=3).
2. Soften the novelty claim: the AP core is a mirror-image of BKU's Koizumi–Ueoro single-axis proof (which is *not* the lattice-counting proof the report describes); the new content is the a.e.-pointwise form, direct all-c coverage without Praton, and the tilted MDT itself. The report's §-description of BKU should be corrected to acknowledge both proofs in that paper.
3. S2′/S3′ remain conditional on S2's one unverified idle-ledger step (already flagged by G6; still open).

**Overall: MDT (Claim 1) survives adversarial verification intact and is safe to build on. Claims 3, 4, 5 CORRECT; Claim 2 CORRECT WITH FIXES (equality range + novelty framing).**