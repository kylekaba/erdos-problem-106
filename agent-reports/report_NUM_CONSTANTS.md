All experiments complete and cross-checked. Cleaning up stray pollers is unnecessary (they exit on their own). Final report follows.

## CLAIMS

Throughout: unit lattice Λ(x₀,y₀)=Z²+(x₀,y₀); for a square S of side d tilted by θ∈(0°,45°], p = #{vertical lines x∈x₀+Z meeting S}, q = horizontal analog, c = #(Λ∩S), defect D := p+q−1−c, projection width w := d(cosθ+sinθ), surplus := 2d(cosθ+sinθ−1) = E[p]+E[q]−2d. "a.e. shift" excludes the null set where a lattice line touches ∂S tangentially or passes through a vertex. All numerics: `/private/tmp/claude-501/-Users-kylekabasares-Desktop-erdos-106/6b0597a9-48bd-4e8c-a957-7fc4a05f26d8/scratchpad/numlem/`.

**Claim 1 (Fubini identities; proved, verified).** E[c] = d² and E[p] = E[q] = w for uniform shift on [0,1)². Proof: ∫c = area(S), ∫p = length of the x-projection interval. Numerically confirmed to ≤0.2% for all 56 (d,θ) pairs (table below). Note E[c] is *tilt-invariant*: the mean lattice count sees only area. Confidence 1.0.

**Claim 2 (pointwise defect structure and exact closed form, d ≤ 1; proved).**
For d ≤ 1, θ∈(0°,45°], a.e. shift:
(a) c ≤ pq (each lattice point in S lies on one of the p columns and one of the q rows; distinct points give distinct pairs).
(b) p,q ≤ 2 (w ≤ √2 < 2), and if p=2 the two columns are consecutive (spacing 1).
(c) **D ≥ −1, and D = −1 exactly on the event {p=q=0}** (probability (1−w)₊², by independence of the x- and y-shift). Case check: (p,q)=(0,0): D=−1. (0,q≥1): c=0, D=q−1≥0. (1,1): c≤1 ⇒ D≥0. (1,2),(2,1): c≤2 ⇒ D≥0. (2,2): D<0 needs c=4, i.e. the 4 vertices of an axis-parallel **unit** square inside S (columns/rows are consecutive ⇒ spacing exactly 1; S convex ⇒ hull inside S); but the largest axis-parallel square inscribed in a θ-tilted square of side d has side d/(cosθ+sinθ) < 1 for d ≤ 1 < cosθ+sinθ. So c ≤ 3, D ≥ 0.
(d) Hence the exact formula
**E[D⁺] = 2w − 1 − d² + (1−w)₊²**, and in particular for **d = 1: D ≥ 0 pointwise and E[D⁺] = 2(cosθ+sinθ) − 2 = surplus, exactly, for every θ**.
(e) Small-θ slope: dE[D⁺]/dθ|₀₊ = 2d². 
Verification: formula matches all measured E[D⁺] for d∈{0.85,0.9,0.95,1.0} at θ∈{1,…,45°} to ≤0.7% for θ≥8° and ≤7% at 1° (residuals fully explained by 600²-grid noise: the independent check E[D⁻] = (1−w)₊² matched to 0.8%, e.g. d=0.85, θ=1°: measured 0.018450 vs (1−w)²=0.018303). Also verified P(D<0)=0 for d=1 at θ∈{0.25°,0.5°,1°,4°,15°,45°}. Confidence 0.93.

**Claim 3 (corollary: the per-square BKU inequality REVERSES under tilt, and the mean-shift argument is exactly neutral).**
For axis-parallel squares BKU rests on c ≥ p+q−1. Claim 2 shows that for a tilted unit square **c ≤ p+q−1 pointwise a.e.** (strict with probability ≈1.9θ), i.e. tilted squares are a pure liability for the pointwise counting inequality; the exact compensation is the projection surplus, and at d=1 the two cancel **exactly in expectation** (E[D⁺]=surplus). Verdicts requested:
- **(i) The single-square defect is Θ(θ), not O(θ²)**: log-log fits of E[D⁺] on θ∈{1,2,4,8°} give exponent α = 0.97–1.02 for every d (table below); slope C_def(d)=2d² (d≤1), ≈2d (d≥1).
- **(ii) The surplus (≈2dθ, also linear — cosθ+sinθ−1 ≈ θ, verified) does NOT dominate the defect near d=1**: ratio E[D⁺]/surplus → d for d ≤ 1 (=1 exactly at d=1, proved), and is 0.80–0.97 for d∈{0.85,…,1.2} at θ=1–8°. All decision power therefore lives in the choice of shift, not in shift averages. Confidence: proved for d≤1 (0.93); numeric for d>1 (0.9).

Measured exp1 table (n=600², placement-invariant to <1.5% across 3 random placements; E[c],E[p] check columns omitted — all pass):

| d | θ° | P(D>0) | E[D⁺] | maxD | surplus | ratio |
|---|----|--------|-------|------|---------|-------|
|0.85|1|0.0243|0.0243|1|0.0294|0.83|
|0.85|8|0.199|0.199|1|0.220|0.90|
|0.85|45|0.401|0.685|3|0.704|0.97|
|0.90|1|0.0303|0.0303|1|0.0311|0.97|
|0.95|4|0.103|0.124|3|0.128|0.97|
|1.00|1|0.0328|0.0333|3|0.0346|0.96|
|1.00|4|0.124|0.133|3|0.135|0.99|
|1.00|45|0.484|0.826|3|0.828|1.00|
|1.05|1|0.0352|0.0353|2|0.0363|0.97|
|1.10|4|0.137|0.138|2|0.148|0.93|
|1.20|1|0.0331|0.0334|2|0.0415|0.80|

Fitted α (θ-exponent), C over θ∈{1,2,4,8°}: d=0.85: (1.01, 1.45); 0.90: (0.97, 1.47); 0.95: (0.98, 1.67); 1.00: (0.99, 1.84); 1.05: (0.98, 1.86); 1.10: (0.98, 1.85); 1.20: (1.02, 2.06). (2d² prediction: 1.445, 1.62, 1.805, 2.0.)

**Claim 4 (coherent tilted grid: full lattice capture up to t ≈ 1/(2k); sufficiency proved, measure formula effectively exact).**
Configuration: k×k grid of squares of side d = 1/(cos t + sin t) rigidly rotated by t (bounding box = k exactly; containment asserted programmatically). Each square's axis projection has width d(cos t+sin t) = 1 exactly, so Σpᵢ = Σqᵢ = k² for a.e. shift (measured: max = min = k² at all t, all k).
(a) **Capture lemma (proved):** if sin 2t ≤ 1/(k−1), some shift gives total count Σcᵢ = k². Proof: the little half-open squares tile the big tilted half-open square of side L=kd, so Σcᵢ = #(Λ ∩ big square); an aligned k×k lattice block has convex hull a (k−1)-side axis-parallel square, which fits inside the L-square iff (k−1)(cos t+sin t) ≤ L = k/(cos t+sin t) ⟺ sin 2t ≤ 1/(k−1).
(b) **Capture-set measure (derived, verified to 3–4 significant figures at all 5 test points):** μ(t,k) = (1−(k−1)sin 2t)₊²/(1+sin 2t) (area of valid block translations in the rotated frame, mapped mod 1; GAP: injectivity of the mod-1 map not proven, but data match is exact: e.g. t=0.05,m=5: predicted 0.3280, measured 0.3281).
(c) Measured transition (300²–400² shift grids, k=5,10,20): max-shift count ≥ ⌈Σdᵢ⌉ persists to t = 1.2/(2k) and fails by 1.6/(2k):

| k | t | Σdᵢ | area | max Σcᵢ | margin vs ⌈Σd⌉ |
|---|---|-----|------|--------|--------|
|10|0.2/k²|99.80|99.60|100|0|
|10|5/k²|95.35|90.92|100|+4|
|10|0.06|94.50|89.31|96|+1|
|10|0.08|92.88|86.26|88|−5|
|20|5/k²|395.09|390.24|400|+4|
|20|0.03|388.52|377.37|390|+1|
|20|0.05|381.41|363.69|364|−18|

**Marginal-mode verdict:** in the marginal regime t ~ ε/k², the best-shift count is exactly k² with zero defect; the pessimistic estimate of Warning 4 ("coherent tilt destroys ~Nt of counting") is the **typical-shift** defect (= surplus, by Claim 2), not the best-shift defect. To make best-shift counting fail, one must tilt to t ≈ 0.6/k, paying side ≈ k²t ≈ 0.6k ≫ 1. **The sharp constant in the marginal mode is on counting's side by a factor ~k, not O(1).** Confidence: (a) 0.95; (b) 0.8; (c) 0.9 (shortfall rows are grid lower bounds on the max, but margins are large; borderline cases re-verified at higher resolution in Claim 5's setting).

**Claim 5 (the strong counting lemma is FALSE for rotated squares; explicit verified counterexample).**
There is a genuine packing of 400 squares in T=[0,20]² with Σdᵢ = 394.943 whose **best-shift total lattice count is 393 < 395 = ⌈Σdᵢ⌉**: 350 aligned half-open unit cells on integer positions (each contains exactly 1 point of Λ for *every* shift — the aligned bulk is shift-neutral), plus two 5×5 grains (squares of side d=1/(cos 0.12+sin 0.12)=0.8990) tilted +0.12 and −0.12 rad in two 5×5 boxes (grain bounding box = 5.0000 exactly), with adversarial center offsets mod Z². Each grain alone captures all 25 points at its own shifts (margin +2), but the capture sets (measure μ≈0.002 each) are disjoint: joint best = 43 < 45. Verified end-to-end on 2000² and the grain pair at 3000² shift grids. Consequently the "only missing lemma" **cannot** be strengthened to "every packing has a shift with count ≥ ⌈Σd⌉"; it must use Σd > N (near-extremality). Note the counterexample is far from near-extremal: it pays side deficit N−Σd = 5.06 to destroy 2 units of counting margin — **destruction/payment ≈ 0.4**, and in *all* two-grain trials destruction ≤ 0.42 × payment. Confidence 0.9 (finite shift grid could in principle miss a shift, but count plateaus are far larger than grid spacing; three resolutions agree).

**Claim 6 (interface gap cost is LINEAR in mismatch angle, coefficient ≈ 2 ≈ sin2θ/θ; numeric, upper bounds certified).**
Central unit square tilted θ at the origin of box [−1.5,1.5]², 8 translating axis-parallel unit squares, pairwise disjoint (residual overlap ≤ 10⁻⁵, mostly ≤10⁻⁷), squares may protrude (for θ>0 "all inside" is infeasible: total area = box area and exact rectangle tilings by squares are axis-parallel); maximize covered area in box; exact polygon-clipping objective, L-BFGS-B with penalty ramp, 40–80 multistarts, two warm-start refinement passes; every solution independently re-measured by 4×10⁶-point Monte Carlo (agreement ≤ 0.1%):

| θ | uncovered (min found) | uncovered/θ | sin 2θ |
|---|---|---|---|
|0°|0.000000|—|0|
|1°|0.036421|2.09|0.03490|
|2°|0.068114|1.95|0.06976|
|5°|0.166576|1.91|0.17365|
|10°|0.416422|2.39|0.34202|
|20°|0.567030|1.62|0.64279|
|45°|0.825847|1.05|1.00000|

Fitted exponent on θ∈{1°,2°,5°}: **α ≈ 0.94, C ≈ 1.7–2.0**; slope is flat (1.9–2.1) across 1°–5°, decisively **linear, not quadratic** (a θ² law would halve the slope from 2° to 1°). For small θ the optimum found essentially equals sin 2θ (the tilted square wastes its whole bounding-box excess; sliding neighbors into the corner notches recovers only a few %). **Verdict (iii): interface mismatch costs area ≈ 2·(angle) per unit square, linearly** — coherent tilts are *expensive* at interfaces, so Route B's structure-then-perturb rounding must treat tilt as a first-order cost, and the near-extremal budget G+V ≤ 1 caps Σ_grains (perimeter × tilt) = O(1). GAP: these are optimizer upper bounds; that no sub-linear (θ²) arrangement exists is unproved (heuristic support: any axis-parallel edge meeting a θ-sloped edge of length ℓ forces a wedge of area ~ℓ²θ/2, and only translations are available). Confidence: linear-cost-of-found-optima 0.95; linearity as a true lower bound 0.7.

**Claim 7 (synthesis — what decides the marginal mode; heuristic, honestly flagged).**
Combining: (a) mean-shift counting is exactly tilt-neutral (Claim 2), (b) best-shift counting tolerates coherent tilts up to t ≈ 1/(2m) per m-grain at zero defect (Claim 4), (c) destroying counting margin costs ≥ ~2.4× that margin in side/gap (Claims 5–6), and (d) near-extremal packings have total gap+variance budget < 1 (given context): a grain that could threaten counting needs mt ≈ 1/2 and pays interface gap ≈ 2mt ≈ 1, saturating the entire near-extremal budget, while a single grain within budget cannot break capture at all. **All measured constants favor the counting route; nothing is borderline.** GAP: this is order-of-magnitude bookkeeping over the specific families tested (coherent grains, two-grain conflicts), not a proof over all configurations. Confidence in the numerology 0.85; as evidence about all packings 0.5.

## COUNTEREXAMPLES AND SANITY CHECKS
- E[c]=d², E[p]=w verified to ≤0.2% for all 56 (d,θ) pairs; placement invariance verified with 3 random placements (differences <1.5%, pure grid noise).
- Closed form of Claim 2 tested against all d≤1 data (28 pairs); residuals consistent with grid noise; the D=−1 event probability (1−w)₊² checked independently; D≥0 at d=1 checked at 6 angles including 0.25°.
- Exp2: per-square count sum = big-square count asserted programmatically (k=5); Σpᵢ=k² at every shift confirmed; capture threshold sin2t ≤ 1/(k−1) matches transitions for k=5,10,20; μ(t,m) formula matches at 5 points to 3–4 digits.
- Two-grain conflict re-verified at 400², 1000², 3000² shift grids (margin −2 stable); full 400-square embedding re-verified at 2000².
- Exp3: every optimum independently re-measured by 4M-point MC (≤0.1% agreement); residual overlaps ≤10⁻⁵; warm-started second pass left θ=2°,5° unchanged (robust optima); θ=0 recovers exact tiling (uncovered 0.000000). A regex bug in the first version of the MC checker (it applied a 3° tilt to every saved solution) was caught via inconsistent labels and fixed before use.

## DEAD ENDS
- **"Surplus beats defect as θ→0" (hoped-for mechanism): false.** They cancel exactly in expectation at d=1 (Claim 2d) — no mean/averaged-shift argument can win; this sharpens Warning 5.
- **Strong shift-counting lemma for arbitrary Σd: false** (Claim 5). Any generalization of BKU must consume the hypothesis Σd > N, not just "some shift is good on average".
- **Exp3 as literally specified (all 9 squares inside the box, disjoint): infeasible for θ>0** (area = box area would force an exact tiling, which must be axis-parallel); replaced by the protrusion relaxation, which is the meaningful interface-cost measure.
- **Bounding-box ring construction pressed against the box boundary**: costs 6θ (perimeter loss), not 2θ; the optimizer's ~2θ shows gaps must be kept local to the interface. θ=10° resisted refinement (slope bump 2.39) — apparently a regime transition where the ring must decide which squares protrude; irrelevant to the small-θ verdicts.

## BEST NEXT STEP
The data single out one clean quantitative target that would close the whole problem: prove
**Lemma (conjectured): for every packing of squares with sides dᵢ ≤ 1 (any orientations) in T=[0,k]², max over shifts of Σᵢ|Sᵢ∩Λ| ≥ 2Σdᵢ − k².**
This is (a) tight exactly at the aligned unit tiling; (b) satisfied with slack ≥ 3 in the worst adversarial two-grain configuration found (389.9 vs 393) and with slack ~m²t for single grains; (c) equivalent to "counting destruction ≤ side payment", the inequality every experiment satisfied with a factor ≥ 2.4 to spare; and (d) **sufficient for the full conjecture**: if k²+1 squares had Σd > k² = N, the lemma gives a shift with total count ≥ 2Σd−N > N, contradicting Σᵢ|Sᵢ∩Λ| ≤ |T∩Λ| = N. Concrete plan: first verify it adversarially (optimize grain sizes/tilts/offsets and multi-grain mixtures to minimize count −(2Σd−N); the two-grain machinery in `exp2b_two_grains.py` extends directly), then attack the proof via the pointwise inequality D ≥ −1{p=q=0} of Claim 2 summed over squares, plus the observation that the loss terms are controlled by projection surpluses — Claim 2 supplies exactly the per-square identity needed to convert Σd into Σ(p+q)-type quantities with the right constant 2.

**Code and data (all paths absolute):**
- `/private/tmp/claude-501/-Users-kylekabasares-Desktop-erdos-106/6b0597a9-48bd-4e8c-a957-7fc4a05f26d8/scratchpad/numlem/exp1_single_square.py` (+ `exp1_results.json`)
- `.../numlem/exp2_coherent_grid.py`
- `.../numlem/exp2b_two_grains.py`
- `.../numlem/exp3_interface.py`, `.../numlem/exp3_refine.py`, `.../numlem/exp3_refine2.py`, `.../numlem/exp3_check.py`
- `.../numlem/exp3_sol_theta{0,2,5,10,20,45}.npy`, `.../numlem/exp3_sol_theta{1,2,5,10,20,45}_refined.npy`