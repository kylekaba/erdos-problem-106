# REPORT — The Capture Lemma: correct general form, proofs, sharpness, and the reduction that replaces it

Worklog: `.../scratchpad/p1_capture/WORKLOG.md`; code: `.../p1_capture/cap.py, cap2.py, cap3.py, cap4.py` (all paths under `/private/tmp/claude-501/-Users-kylekabasares-Desktop-erdos-106/6b0597a9-48bd-4e8c-a957-7fc4a05f26d8/`).

Notation: `T=[0,k]²`, `N=k²`, packing of `n` squares, sides `d_i`, **any** orientations, `Σ=Σd_i`, `A=Σd_i²` (area), `s=Σ(1−d_i)²` (deficit mass), `G=T∖∪S_i` (gap), `g=|G|=N−A`, `C(p)=Σ_i|S_i∩Λ_p|`, `hits(p)=#(Λ_p∩G)=N−C(p)` a.e.

## 1. Theorem A (Structure Identity; proved, elementary, size- and tilt-free)

For every packing: **`2Σ = N + n − g − s`** (per-square algebra `d² = (2d−1)+(1−d)²` summed, plus `A = N−g`). Verified numerically to 0 residual. Consequences:

**(a) NUM's conjectured lemma in the form `max_p C ≥ 2Σ − n` is TRIVIAL.** `E[C] = A = 2Σ − n + s ≥ 2Σ − n` (Fubini), for any `n`, sizes, tilts. It reproduces exactly the classical bound `ε ≤ 1/2` and nothing more. The 4-half-squares example is explained: there `2Σ − n = 0`.

**(b) The correct nontrivial form is `max_p C ≥ 2Σ − N` restricted to `n ≤ N+1`,** which by the identity is the *gain form* `max C ≥ E[C] + (1−s) − (N+1−n)`, equivalently **`min_p hits ≤ g + s − 1 + (N+1−n)`**. Since `max C ≥ ⌈E C⌉` (integer process), it is *automatically true unless `frac(A) > s + (N+1−n)`*. The whole difficulty is a **+1 gain over the ceiling of the mean** in that regime.

**(c) In the critical range it is the conjecture:** at `n = N+1`, a packing with `Σ > N` has `g + s < 1`, and the lemma demands `min hits < 0` — impossible — so the lemma (if true) kills such packings. Because the identity is size-free, this gives the **full** conjecture at `n = N+1` with *no size restriction and no subdivision* (subdivision is not needed and in fact not tolerated: see 3).

## 2. Theorem B (Axis-parallel capture lemma, sharp; proved)

For every AP packing (any `n`, **any sizes**): pointwise `c_i ≥ p_i + q_i − 1` (case check: `c=pq`; `(p−1)(q−1) ≥ 0` unless exactly one of `p,q` is 0, and `p=0 ⇒ w<1 ⇒ q ≤ 1 ⇒ c = 0 ≥ p+q−1`). Hence
**`max_p C ≥ max_x P + max_y Q − n ≥ 2⌈Σ⌉ − n`.**
With budget `C ≤ N` and integrality of `⌈Σ⌉` this yields `Σ ≤ ⌊(N+n)/2⌋ +` frac-corrections; at `n = k²+2c+1` it gives `Σ ≤ N + c`, i.e. **the sharp BKU theorem `g(k²+2c+1) = k + c/k` for all `c ≥ 0` in one line**, and full AP-Erdős for all `n ≤ N+1` without subdivision. This is BKU's argument reorganized as a capture statement — nothing new mathematically, but it fixes the AP baseline: destruction is impossible AP-side because `⌈Σ⌉` is always captured up to the `−n` term.

## 3. Theorem C (Sharpness of the form; proved + numerically verified)

**(a) `n ≤ N+1` is exactly sharp.** Explicit counterexample at `n = N+2`, any `k ≥ 2`: `N−2` unit cells + one cell tiled by four half-squares + one empty cell. Then `C ≡ N−1` (verified: constant field), `Σ = N`, but `2Σ − N = N > N−1`. The four-way split is the cheap move (`g+s` cost 1 for +3 squares) that outruns the constant beyond `N+1`.

**(b) Split-cell configs are the exact extremal case at `n = N+1`:** `N−1` units + two squares `a+b=1` in the last cell give `max C = N = 2Σ−N` exactly (slack `0.0000` at fine grid), *and* `|{C=N}| = a²+b² = s` exactly. Double tightness.

## 4. The Full-Capture Measure Bound (FCMB) — the statement that should replace the capture lemma

**FCMB (conjectured).** *For every packing of `n = N+1` squares (any sizes, any orientations) in `[0,k]²`:*

|{p : C(p) = N}| ≤ Σᵢ (1−dᵢ)².

**Theorem D (FCMB ⇒ full Erdős conjecture; proved, 3 lines, size-free).** `g = E[hits] ≥ P(hits ≥ 1) = 1 − |{C=N}| ≥ 1 − s`; the identity gives `2Σ = 2N+1−g−s ≤ 2N`, i.e. `Σ ≤ N` — which is `f(k²+1) = k`. **No `d ≤ 1` hypothesis, no subdivision, no near-criticality needed.** This is, to my knowledge within this project, the cleanest sufficient statement yet: a single measure inequality on the shift torus.

Supporting structure (proved):
- On `{C=N}`, pigeonhole gives ≥ 1 empty square (nonempty ≤ N points < n), and when all `d_i ≤ 1` the other `N` capture bijectively; AP: the line-chord argument (each row-line meets its `k` capturing squares in disjoint full-width chords) gives `Σ' ≤ N` for the capturing subfamily on any full-capture shift.
- **FCMB is proved for `k=1`** (any orientations): `|{C=1}| = |π(S₁)∪π(S₂)| ≤ a²+b² ≤ (1−a)²+(1−b)²` iff `a+b ≤ 1`, which is `f(2)=1` (Erdős). Tilting only helps: `|π(S)| <` area once `w > 1`.
- Tightness: exactly the split-cell configs (equality); all tilted perturbations strictly decrease `|Av|` (measured: 0.48 vs 0.58 bound, etc.).
- Sharpness in `n`: at `n = N+2` even the `n`-corrected version `|Av| ≤ s + (N+1−n)` fails (measured violation +0.14 at k=3, n=11).

**Two-sided split of NUM's lemma.** For *valid* packings with `g+s < 2`, the capture lemma at `n=N+1` says `min hits = 0`, i.e. `|Av| > 0` — a **lower** bound on full-capture measure; Erdős needs only the **upper** bound (FCMB). These are independent statements. The application should target FCMB alone.

## 5. Destruction ≤ payment, formalized

Define payment `Π := N − Σ`, destruction `Δ := ⌈Σ⌉ − max C`. Proved unconditionally (Theorem A(a) + integrality): **`Δ ≤ Π + (n−N) + 1`**, so `Δ ≤ Π + 2` for `n ≤ N+1`, any sizes/tilts. The capture lemma is exactly `Δ ≤ Π + (⌈Σ⌉−Σ) ≤ Π + 1`. **Ratio forms (`Δ ≤ ½Π`) have zero additive slack as `Σ → N` and are therefore equivalent to the conjecture at the boundary, not a weaker stepping stone**; the measured 0.42 ratio (NUM Claim 5) is family-specific evidence, not a target to prove separately. Recommendation: retire "destruction ≤ ½·payment" as a goal; its provable content is `Δ ≤ Π + 2` (done) and its conjectural content is FCMB.

## 6. Adversarial numerics (all code in `p1_capture/`)

Grid resolutions 90–500²; slack = `maxC − (2Σ−N)`; `fcmb_v = |Av| − (s+(N+1−n))`. Findings:
- **No violation of the `n ≤ N+1` capture lemma or FCMB was found anywhere**: AP splits (slack 0, tight), tilted pairs (+0.04..0.10), coherent 3×3 grains at t=0.05–0.2 with `n=N+1` (full capture persists, slack = `g+s−1` > 0.8), two ±0.12-grain conflict at k=6, n=37 (slack +3.64, full capture), corner+center 5-square family through the *optimal* packing d=0.7388 (slack ≥ 0.61; simulated annealing over positions/tilts/sizes could not destroy full capture), k=3 seeds (min slack 0 at split; others ≥ 0.51).
- **Phase-adversarial grain conflicts are impossible at `n = N+1`**: Claim 5's counterexample needed grain-box offsets mod ℤ², which require free space; a tight `n ≤ N+1` packing has none. This is a structural reason the two-grain enemy dies near criticality.
- **The only candidate violating family** the analysis admits: no-full-capture (gap covering the torus) with `g+s < 2`. AP exact-tiling arithmetic floors at `g+s ≥ 3` for this (every 2-split costs 1; 4-splits overshoot `n`); the remaining possibility — `N+1` near-equal squares of side `1−δ`, `δ ∈ [1/(N+1), 1.5/(N+1))`, leaving an empty cell — was probed at k=3 (10 squares of side 0.80/0.85 in the L-region, tilts allowed): **no valid packing found** (large residual penalties), and at k=2 the only such packings (5-square family) all retain full capture. Frontier unbroken but not closed by proof.

## 7. Honest status and gaps

**Proved this session:** Theorem A (identity + triviality classification + critical-range equivalence), Theorem B (sharp AP capture lemma reproducing BKU incl. `g(k²+2c+1)`), Theorem C (sharpness both in the constant and in `n`; explicit `n=N+2` counterexample), Theorem D (FCMB ⇒ full conjecture, size-free), FCMB at `k=1`, `Δ ≤ Π + (n−N) + 1`.

**Open (Gap I — the problem):** FCMB for `k ≥ 2`. Suggested attack order: (i) AP case (a new proof of BKU as a measure bound — the bijective-capture + line-chord structure gives `Σ' ≤ N` pointwise on `Av`; what's missing is converting chord slack into measure); (ii) sea + one coherent grain via the capture-set measure formula μ(t,m) (NUM Claim 4) and the per-square product structure of good shifts (`L_i=0` off bad sets of measure `2d sinθ` per axis); (iii) general tilts using `|π(S)| ≤ d² − (chord surplus)`.

**Open (Gap II — mid-range):** the lower-bound half (`|Av| > 0` when `g+s<2`, `n=N+1`) — true in all tests, needed only if one insists on the original capture-lemma phrasing; not needed for Erdős.

**Bottom line:** NUM's conjectured lemma has been given its correct general form, proved trivial below the critical constant, proved sharp at `n ≤ N+1`, refuted at `n = N+2`, verified adversarially in the dangerous mid-range, and — most importantly — **superseded by FCMB**, a one-line-consequence sufficient condition for the full conjecture whose extremal configurations are now exactly identified (split-cells) and whose `k=1` case is a theorem.
