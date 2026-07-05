# G1 — Independent verification of the final-push suite (fp_P_SQUEEZE + fp_P_RIGIDITY)

Verifier: session-3 agent G1. Date 2026-07-04.
Code (all written from scratch, no reuse of the authors' scripts):
`verify_g1.py` in this directory (also copied beside this file in
agent-reports/session3-derivations/). Full run log: `run2.log`. Final result:
**0 failures over ~60 checks** (7 SAT-validated packings, 400 exact random arc
systems, 237k random integer-law pairs, exhaustive integer-inequality scans).

VERDICT SUMMARY (details and re-derivations below):

| Item | Verdict |
|---|---|
| Lemma 0 (chord constancy) | **CONFIRMED — promote to [V]** |
| Lemma A″ (tilted over-full-line exclusion, sharpness, genericity) | **CONFIRMED — promote to [V]** |
| Theorem S2 incl. the flagged idle/multiplicity ledger | **CONFIRMED — promote to [V]** (one loose phrase in the summary, math correct) |
| Corollary S3 (assembly algebra), S1 | **CONFIRMED — [V]** |
| Corollary S4 | **CONFIRMED — [V]** with one missing-citation note (ε<1/2) |
| κ-coupling (Claim 5) | **CONFIRMED as stated** — [V modulo T6, which stays [P]] |
| Lemma K (integer anti-concentration) | **CONFIRMED — promote to [V]**; equality-characterization erratum at boundary means (inequality untouched) |
| Theorem K (κ ≥ (1−t)₊², 0≤t≤1) | **CONFIRMED — promote to [V]** (unconditional) |
| Theorem K′ chain | **CONFIRMED given T6's MPI [P]** — keep conditional status |
| Claim 3 (κ-neutralization) | **CONFIRMED** incl. re-derivation of t ≥ 2ε from T4 |
| D1–D4, (★★), Corollary R, arc-count ≤ N+1, c=1/400 numbers | **CONFIRMED — [V]** |

## 1. The flagged step: Theorem S2's idle/multiplicity ledger — CONFIRMED

Setting: on Av∩E (E = good phases both axes), c_i = p_i q_i for all i and
Σ c_i = N. Idle set I = {i : p_i q_i = 0}; μ = Σ_{i∉I}(c_i − 1).

(a) Count: Σ_{i∉I} c_i = N and #{i∉I} = (N+1) − |I|, so μ = N − (N+1−|I|) =
|I| − 1, i.e. **|I| = 1 + μ**, and |I| ≥ 1 always (μ ≥ 0). ✓

(b) Idles are short, multis are long: c_i = 0 ⇒ p_i = 0 or q_i = 0 ⇒ w_i < 1
(an interval of length w ≥ 1 contains ≥ ⌊w⌋ ≥ 1 lattice lines); c_i ≥ 2 ⇒
max(p_i,q_i) ≥ 2 ⇒ w_i ≥ 1 (both bbox projections have the same width w_i). ✓

(c) The assignment's suspicion — "idle i means p_i = 0 OR q_i = 0, a union
event, not the product event {p_i=0}×{q_i=0}" — is resolved EXACTLY as the
orchestrator guessed, and the derivation file (SQUEEZE_DERIVATIONS.md, Thm S2,
split (1)) states it correctly: write M_X(x) = {i : p_i(x)=0}, M_Y(y) =
{i : q_i(y)=0}; then I = M_X ∪ M_Y. Lemma A″ (hypothesis β < 1 = S2's
hypothesis; applies for a.e. good x and a.e. good y separately, hence a.e. on
E by Fubini) gives **M_X(x) ≠ ∅ and M_Y(y) ≠ ∅**. Both are subsets of I. If
|I| = 1, say I = {i*}, then M_X = M_Y = {i*}, forcing p_{i*}(x) = 0 AND
q_{i*}(y) = 0 simultaneously. (Equivalently: if the x-missed square differed
from the y-missed one, both would be idle, contradicting |I| = 1.) So the
event {Av∩E, I = {i}} ⊆ {p_i=0}×{q_i=0}, of measure (1−w_i)_+². The EVENTS
are disjoint across i (unique idle); the PRODUCTS need not be, but the bound
Σ_i |{p_i=0}|·|{q_i=0}| = Σ(1−w_i)_+² only needs event-disjointness plus
per-event containment. Measure bookkeeping ✓: |{p_i=0}| = (1−w_i)_+ exactly.

(d) |I| ≥ 2 ⇒ μ ≥ 1 ⇒ some non-idle (hence long) i has p_i q_i ≥ 2 ⇒ p_i ≥ 2
or q_i ≥ 2 ⇒ x ∈ V_x-union or y ∈ V_y-union; contribution ≤ V_x + V_y. ✓
Adding |E^c| ≤ U_x + U_y gives S2. ✓

Numerics (mine, fresh): on all 7 valid packings, at every grid shift in Av∩E
(~10⁶ shifts total): ledger |I| = 1+μ exact, idles all short, multis all long,
c_i = p_i q_i on E — 0 violations. **Non-vacuous pinning test**: I built
`tilt30_k1` (two 0.48-side squares at θ=0.3 in [0,1]², β = 0.9951 < 1, E
nonempty, unique-idle measure 0.132): the unique idle had p = 0 AND q = 0 at
every one of the ~10⁵ unique-idle grid shifts. On β ≥ 1 configs (columns,
big-square configs) the pinning demonstrably FAILS (as it must — A″
unavailable), confirming the hypothesis is load-bearing, not decorative.
S2's inequality held on every β < 1 config; the deficient column (β = 1)
violates it by exactly (k−1)/(k+1) (measured 1/3 at k=2, 1/2 at k=3):
**β < 1 is razor-sharp, as claimed.**

One wording nit: fp_P_SQUEEZE Claim 3's phrase "contained in the disjoint
products" is loose (events disjoint, products not necessarily); the
derivation file is precise. No math error.

## 2. Lemma 0 — CONFIRMED (re-derived + fresh numerics)

Vertices A=(ds,0), B=(w,ds), C=(dc,w), D=(0,dc) verified by direct rotation.
On x ∈ [ds,dc]: bottom envelope edge AB, y=(x−ds)tanθ; top envelope edge DC,
y=dc+x·tanθ (both slopes tanθ checked: ds/dc·... = tanθ); chord = dc+ds·tanθ =
d(c²+s²)/c = d secθ, constant. Taper linear to 0 outside. Max chord = d secθ.
Horizontal chords: 90°-symmetry, same folded θ. My independent
segment-intersection code: 300 random (d,θ), 120 chords each (vertical AND
horizontal via reflection): 0 exceedances of d secθ, max middle-region error
4.4e-16. Also re-derived the B-arc/middle-region complementarity used
downstream: within the projection, complement of the two B^x arcs
([bbox_min, +d sinθ] and [bbox_max −d sinθ, bbox_max]) is exactly the middle
region — so "x good ⇒ every line meeting the projection meets the middle
region" is airtight.

## 3. Lemma A″ — CONFIRMED (proof, genericity, sharpness)

Pigeonhole re-derived: good generic x, all p_i ≥ 1 ⇒ ≥ N+1 incidences on the
k lines {x+m}, m ∈ {0..k−1} (x ∈ (0,1) generic, projections ⊆ [0,k]) ⇒ some
line meets ⌈(N+1)/k⌉ = k+1 squares; each in its middle region (x good), chord
exactly d_j secθ_j, open chords in disjoint square interiors, all inside
[0,k] ⇒ Σ_L d_j secθ_j ≤ k ⇒ Σ_L (1−d_j secθ_j) ≥ 1 ⇒ β ≥ Σ_L(1−·)_+ ≥
Σ_L(1−·) ≥ 1 (over-unit chords only strengthen: positive parts dominate raw
terms). Contradiction with β < 1. Genericity: exceptional phases (lines
through vertices/bbox endpoints/kinks) are finite per square per m — null. ✓
Sharpness: deficient column has β = 1 exactly and good full-hit measure
k/(k+1) > 0 — reproduced numerically (my sampler: 200/200 good full-hit x at
k=2,3 and tilted k=2 each produced an over-full line with k+1 squares, every
chord = d secθ to <1e-9, chord sum ≤ k, line deficit ≥ 1). Both my β < 1
configs had good full-hit measure 0, as the lemma demands. **Constant 1 is
exact; promote to [V].**

## 4. S3 / S1 / S4 — CONFIRMED

S3(ii) chain re-derived: 1−g ≤ |Av| (Markov, E[hits]=g) ≤ S2 bound;
1−g = 2ε+s (from 2Σd = 2N+1−g−s); (1−w)² = (1−d)² − dσ(2−d−w) is an exact
polynomial identity ((d−w)(2−d−w) = −dσ(2−d−w)); s splits short/long;
rearrangement gives (ii) verbatim, margins m_i ≥ 0 on the short branch
(d ≤ w < 1 ⇒ 2−d−w > 0). S3(i): Σ(1−d)_+ = 1−ε+b0 (positive-part identity,
machine-checked on 2000 random profiles) and β = Σ(1−d)_+ − Γ give
β ≥ 1 ⟺ b0 ≥ ε+Γ, Γ ≥ 0 since sec ≥ 1. ✓ S1: all-short ⇒ β ≤ 1−ε < 1,
V = 0 automatic. ✓ S4: correct, with one gap-note: the step "some d ≥ 2 gives
b0 ≥ 1 > ε" silently uses ε < 1/2; this follows unconditionally from area +
Cauchy–Schwarz (Σd ≤ √(N(N+1)) < N + 1/2), so no BKU/T2 dependence enters —
worth one line in the writeup, not an error. For d ∈ [1,2) longs, V_x ≤
Σ(d−1) = b0 per axis ✓, contradiction with (ii) ✓.

## 5. κ-coupling (Claim 5) — CONFIRMED as stated

pq ≥ p+q−1 for nonneg integers unless (0,≥2); that corner is impossible by
equal projection widths ✓. So on {ΣL=0}: N ≥ C = Σp_iq_i ≥ P+Q−(N+1) ⇒
P+Q ≤ 2N+1; on {ΣL=0}∩{hits≥1}: C ≤ N−1 ⇒ P+Q ≤ 2N ⇒ integrand ≥ 1; measure
≥ 1−|Av|−U_x−U_y. Hence κ ≥ (1−U_x−U_y−|Av|)_+ — verified numerically on all
7 packings. The T6 combination 2ε ≤ |Av|+U_x+U_y−Σm_i is a two-line
consequence and also correct in the degenerate branch (if 1−U−|Av| ≤ 0 the
claim follows from T6 alone). Status stays [V modulo T6 [P]] exactly as the
authors flagged.

## 6. Lemma K — CONFIRMED (with one equality-characterization erratum)

Pointwise inequalities re-proved case-by-case AND verified exhaustively on
[−8,8]²: (I) (a+b−1)_+ ≥ a_+1{b≥1}+b_+1{a≥1}−1{a≥1}1{b≥1} (equality when both
≥1; RHS = 0 otherwise); (II) (a+b−1)_+ ≥ (a−1)_+ + b·1{a≥1} for ALL integer b
(sign of b immaterial: a ≥ 1 gives x ≤ x_+; a ≤ 0 gives RHS = 0). Expectation
versions use independence only. Three-case analysis re-derived: Case 1
(p ≤ μ1): E ≥ A−(1−μ2)p ≥ μ1−(1−μ2)μ1 = μ1μ2 using μ2 ≤ 1 (monotone in p) and
A ≥ μ1; Case 2 symmetric; Case 3 (p > μ1, q > μ2): E ≥ Aq+Bp−pq ≥ pq > μ1μ2
using A ≥ p, B ≥ q. Fresh MC: **237,139 random independent law pairs**
(support −3..5, biased Dirichlet, means in [0,1], exact expectations): 0
violations. μ ≤ 1 necessity confirmed (φ=ψ≡3: 5 < 9).

**ERRATUM (minor, does not affect any downstream use):** "equality iff both
{0,1}-Bernoulli" fails at boundary means. Counterexamples (machine-checked):
(i) μ1 = 0: φ ≡ 0, ψ = ±1 w.p. 1/2 — equality (0 = 0), ψ not {0,1}-valued;
(ii) μ1 = 1: φ ≡ 1, ψ ∈ {0,2} w.p. {3/4,1/4} — E = 1/2 = μ1μ2, ψ not
Bernoulli. The characterization is correct for μ1, μ2 ∈ (0,1) (my
re-derivation: Case-1 equality forces φ ≥ 0, p = μ1 ⇒ φ ∈ {0,1}; then p < 1
forces ψ ≤ 1 and ψ ≥ 0 ⇒ ψ ∈ {0,1}). Suggested fix: add "for μ1,μ2 ∈ (0,1)"
to the equality clause. The inequality, and every tightness instance cited
(extremal manifold, diamond pair), are unaffected.

## 7. Theorem K — CONFIRMED, unconditional; promote to [V]

φ = P−N, ψ = Q−N independent (product shift measure), integer, means t
(E[p_i] = w_i re-derived from the arc structure). Lemma K ⇒ κ′ ≥ t² for
t ∈ [0,1]; κ = κ′ + 1 − 2t (identity E[(−Z)_+] = E[Z_+] − E[Z]) ⇒ κ ≥ (1−t)².
Fresh exact arc engine (my own breakpoint arithmetic): 400 random arc systems
(N ∈ {1,4,9}, w ∈ (0.05,2.4) rescaled, random phases): κ′ ≥ t² and the
κ-identity, 0 violations. Diamond pair (d=0.47, 45°, k=1): my exact
computation gives κ = 0.4497570055 = (1−t)² to 10 digits — **equality
confirmed**. Flat-coverage counterexample to naive circle-LO confirmed (16
half-arcs at phases j/16: coverage ≡ 8). κ = 0 attainability confirmed (all
w_i = 1: κ computed exactly 0). t < 0 caveat is correctly scoped ((1−t)² >
1−2t makes the floor claim genuinely need t ≥ 0).

## 8. Theorem K′ chain — CONFIRMED conditional on T6's MPI (stays [P])

Chain re-derived: MPI ⇒ E[D] ≥ κ′ (D ≥ 0 and D ≥ P+Q−2N−1 ⇒ D ≥ (·)_+);
margin bound Σ E[(L_i−B_i)_+] ≤ 2τ − Σm_i (T6's verified branch identities);
Lemma K ⇒ κ′ ≥ t₊² for t ≤ 1; t = ε+τ. For t < 0 the statement degrades
gracefully to 0 ≤ 2τ−Σm (E[D] ≥ 0). t ≥ 1 branch is plain T6 with κ ≥ 0. ✓
Note: the quadratic-window corollary (b) additionally needs Σm_i ≥ 0 — the
derivation file states this hypothesis, the fp summary headline omits it
(margins are negative on the d > u1 branch); one-word fix. My numerics: MPI
plus L_i ≥ 0 checked pointwise on ~3.6M shifts across all 7 packings — 0
violations (further numeric support for T6 [P], which remains the only
unproved link). K′ final inequality held on all 7 packings.

## 9. Claim 3 (κ-neutralization) — CONFIRMED, including the t ≥ 2ε bridge

The load-bearing bridge re-derived from the report's T4 [V] as the assignment
demanded: T4 states ε ≤ T = Σ d_i(1 − 1/u_1(θ_i)). Pointwise
1 − 1/u1 ≤ u1 − 1 = σ (since u1 ≥ 1), machine-checked; hence
**ε ≤ T ≤ τ = Σd_iσ_i**, so t = ε + τ ≥ 2ε. (Note: the naive route via the
report's weaker display "ε ≤ Σd_iθ_i" would NOT give τ ≥ ε, since σ ≤ θ;
the inscribed-square form T is the one that works. The orchestrator's brief
and fp_P_RIGIDITY both use the correct form.) Then enemy ⇒ t ≥ 2ε > 1−2c ⇒
(1−t)₊² < 4c² ≪ 2c, and κ = 0 arc systems exist (all w ≥ 1): no κ lower
bound from arc/phase data alone reaches 2c. Directionality confirmed: in my
arc experiments clustering raises κ; the floor (1−t)² is attained by
equidistributed phases. The meta-conclusion — the second jaw must be
geometric, not measure-theoretic — is sound as scoped (statements provable
from arc structure alone).

## 10. D1–D4, (★★), Corollary R — CONFIRMED

D1 (P ≤ N ⟺ Ǧ−F₊ ≥ r, with W0+n₋ = N+r), D2 (E[Ǧ−F₊] = r−t), D3
(∫_{E_x}Ǧ ≥ (r−t)−(r−1)(1−δ) ≥ 1−t; (1−t)_+ ≤ Hδ) re-derived line-by-line and
verified exactly on 800 random axes (0 failures, my own piecewise engine).
D4(a),(b),(c) and (★★) algebra re-derived (all two-line consequences). 
Corollary R: δ ≤ κ/(1−t) < 2c/(1−t); component count of {P ≤ N} ≤ N+1
(≤ one falling edge per square per period — re-derived); H ≥ (1−t)²/(2c);
c = 1/400, τ ≤ 1/4 arithmetic re-checked (1−t ≥ 1/4 > 1/5 via ε ≤ 1/2 by
area; δ < 0.025; H ≥ 8). The honest-limitation caveat (vacuous for the true
enemy at t ≥ 2ε) is correct and important. Lemma S's AP argument is fine;
its tilted version is flagged GAP by the authors — agreed, unresolved.

## 11. Adversarial attacks attempted (all defeated)

(a) Tried to break the ledger with an all-idle or zero-idle configuration:
impossible on Av∩E (μ ≥ 0 forces |I| ≥ 1; C = N ≥ 1 forces a non-idle when
|I| = n). (b) Tried to realize a real β < 1 packing with positive unique-idle
measure and pinning failure: at β = 0.995 (θ = 0.3, k = 1) pinning held on
every shift; β < 1 with whisper tilts is impossible for real packings
(β = 1−ε+b0−Γ ≥ 1 needs Γ+ε > b0; Γ is quadratic in θ), so the hypothesis
does exactly the work claimed and no counterexample family exists to probe —
consistent with the authors' self-attack (e). (c) Long squares with
d secθ > 1 on the over-full line: strengthen A″ (positive-part step). (d)
θ = π/4 degeneracy: middle region a point, B-arcs swallow the projection,
lemma vacuous not false (diamond config: good set empty, confirmed). (e)
Negative-margin branch (d > u1) feeding S3/K′: S3 only uses short-branch
margins (m ≥ 0 there); K′ keeps Σm signed; only the window corollary needs
the sign hypothesis, which the derivation file has. (f) My own two initially
"failing" packings turned out to be overlapping (my construction error,
caught by my SAT check + budget C > N); after fixing, everything passed —
incidentally re-confirming that budget violations reliably detect overlap.

## 12. Corrections list (all minor, none fatal)

1. Lemma K equality clause: restrict to μ1, μ2 ∈ (0,1) (boundary
   counterexamples above). [RIGIDITY_derivations.md §1; fp_P_RIGIDITY Claim 1]
2. fp_P_RIGIDITY Claim 5 headline: add "Σm_i ≥ 0" to the quadratic-window
   sentence (derivation file already has it).
3. fp_P_SQUEEZE Claim 3: rephrase "contained in the disjoint products" →
   "the (disjoint) exactly-one-idle events are each contained in the product
   {p_i=0}×{q_i=0}".
4. SQUEEZE_DERIVATIONS.md Corollary S4: add the one-line justification
   ε < 1/2 (area + Cauchy–Schwarz: Σd ≤ √(N(N+1))), keeping S4 fully
   BKU/T2-free.
5. Report should record that Theorem K's t < 0 failure mode and K′'s
   t ≥ 1 branch are correctly scoped (no action, just confirmed).
