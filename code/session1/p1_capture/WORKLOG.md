# P1 Capture Lemma — WORKLOG

## Step 0: read context (done)
Read report_NUM_CONSTANTS.md, p2_P2_SUB_CS.md, p2_V3_COUNTING_CORE.md.

## Step 1: STRUCTURAL DISCOVERY (pen and paper, to be verified numerically)

Notation: N = k^2, T=[0,k]^2, n squares, sides d_i, ANY tilt, disjoint interiors.
Sigma = sum d_i;  A = sum d_i^2 (area);  s = sum (1-d_i)^2 (size-deficit mass);
g = |G| = N - A (gap area);  C(p) = sum_i #(S_i ∩ Λ_p) (count process);
hits(p) = #(Λ_p ∩ G) = N - C(p) a.e. (budget identity).

**Identity I (per-square algebra, exact, any orientation, any d):**
   d^2 = (2d - 1) + (1-d)^2  ⇒  A = 2Sigma - n + s  ⇒  2Sigma = N + n - g - s.

Consequences:
1. **NUM's conjectured lemma in the form max_p C ≥ 2Sigma - n is TRIVIAL:**
   E[C] = A = 2Sigma - n + s ≥ 2Sigma - n. Fubini. Any n, any d, any tilts.
   This explains the 4-half-squares example exactly (2Sigma - n = 0 there).
   It reproduces exactly the classical trivial bound eps ≤ 1/2 and NOTHING more.
2. **The correct target form is max_p C ≥ 2Sigma - N restricted to n ≤ N+1**, and via
   Identity I it equals: max C ≥ A + (1 - s) + (n - N - 1), i.e.
   **GAIN FORM: max_p C ≥ E[C] + (1 - s) - (N + 1 - n).**
   The entire content = gaining (1 - s) over the MEAN of the integer process C.
   Trivial by integrality (max ≥ ceil(E C)) unless frac(A) > s + (N+1-n).
3. **Equivalent min-hits form:** min_p hits ≤ g + s - 1 + (N+1-n).
4. For n = N+1: if the packing has Sigma > N (i.e. g + s < 1), the claim forces
   min hits < 0, impossible ⇒ no such packing ⇒ **capture lemma at n=N+1 in the
   critical range IS the d≤1-restricted Erdős conjecture** (g + s ≥ 1).
5. **FCMB (full-capture measure bound), a clean sufficient statement:**
   |{p : C(p) = N}| ≤ s   for n = N+1 packings with d_i ≤ 1.
   Proof that FCMB ⇒ conjecture: g = E[hits] ≥ P(hit≥1) = 1 - |{C=N}| ≥ 1 - s.
   FCMB is tight on split-cell configs (N-1 units + sides a+b=1: |Av| = a²+b², s = b²+a²).
   FCMB is STRICTLY stronger than the conjecture (adds torus-injectivity of gap).
6. On {C=N} with n=N+1: pigeonhole ⇒ ≥1 empty square; the other N squares
   capture bijectively (each exactly 1 lattice point). AP: line-chord argument ⇒
   capturing subfamily has Sigma' ≤ N (each row-line meets its k squares with
   full-width chords, disjoint ⇒ sum ≤ k). Tilted: chords can be short — the
   known enemy, quantified by avg chord = d/(cosθ+sinθ).

## Step 2 plan
- AP sharp lemma: max C ≥ max_x P + max_y Q - n ≥ 2⌈Sigma⌉ - n (BKU); tightness.
- Numerics N1-N4: identity check; adversarial mid-range hunt for violations of
  min-hits ≤ g+s-1+(N+1-n) on EXISTING packings incl. tilted grains; FCMB tests;
  destruction-vs-payment recast: destruction ≤ payment + 1 - {Sigma} is the lemma.

## Step 2 results (cap.py, run 1)
- Identity verified (resid 0).
- AP split-cell (n=N+1): slack=0 EXACTLY, |Av|=s EXACTLY (both tight, all a).
- Tilted pair in cell: slack>0, |Av| < s strictly (tilt wastes pi-measure -> helps FCMB).
- Grain m=3, t in {.05,.12,.2}, k=5, n=26=N+1: full capture at best shift (minhits=0),
  slack = g+s-1 > 0. Capture regime sin2t <= 1/2 as per Claim 4.
- Note slack == rhs - minhits is an identity (checked): slack >= 0 iff minhits <= g+s-1+(N+1-n).
- 2-grain configs invalid: BUG d=1/(cos t + sin t) with t<0 gives d>1. Fix: use |t|.

## Step 3: SHARPNESS + theoretical developments (pen&paper, to verify)
(a) **n=N+2 COUNTEREXAMPLE to the raw form maxC >= 2Sig-N:** k=2: units at cells
(0,0),(1,0); cell (0,1) tiled by FOUR 1/2-squares; cell (1,1) EMPTY. n=6=N+2,
Sig=4, C === 3 constant (empty cell's point never captured), 2Sig-N = 4 > 3.
So the restriction n <= N+1 is SHARP. (verify numerically)
(b) **Mid-range risk at n=N+1:** violation iff exists packing with NO full-capture
shift (maxC <= N-1) and g+s < 2 (i.e. Sig > (N+n-2)/2 = N - 1/2). k=2: five squares
with Sig > 3.5 and empty full-capture set. The optimal 5-square packing
(4 corners + 45deg center, d = 2/(2+1/sqrt2) = 0.73879, Sig = 3.694) has
full capture (corner arcs overlap: x,y in (1-d,d) captures all 4 corners) -> slack
+0.6 predicted. Adversarial search over repositionings needed.
(c) Polyomino-BKU: BKU's AP argument works verbatim in any lattice polyomino
(budget = area, pigeonhole unchanged). Useful for empty-cell analyses.
(d) Destruction<=payment: capture lemma at n<=N+1 iff destruction := ceil(Sig)-maxC
<= payment + (1-frac(Sig)), payment := N-Sig. Ratio-1/2 form has no additive slack
=> equivalent to conjecture at the boundary; only measured 0.42 on two-grain family.

## Step 4 results (cap2.py, cap3.py, cap4.py)
- S1 CONFIRMED: n=N+2 counterexample (2 units + 4 halves tiling a cell + empty cell,
  k=2): C === 3 constant < 4 = 2Sig-N. n<=N+1 restriction SHARP.
- S2: two-grain conflict CANNOT be phase-adversarial at n=N+1 (no room to offset
  grain boxes in a tight packing): minhits=0, slack +3.6.
- S3/A1: corner-center 5-square family (incl. optimal d=0.7388): annealing cannot
  destroy full capture; slack floor ~0.61 = g+s-1.
- A1/A2: k=2 all seeds: min slack = 0.0000 attained EXACTLY at 3units+split(1/2,1/2);
  FCMB max violation = 0.0000 at same config (double tightness of split-cell).
- A3/B1: k=3 n=10: min slack 0.0000 (8u+split), others >= 0.51. n=11=N+2 seed shows
  fcmb_v=+0.14: generalized-n FCMB also fails past N+1.
- B2: feasibility probe: 10 squares side 0.80/0.85 in L-region (k=3, empty cell):
  NO valid packing found (residual penalty 2.2/4.1) -> near-unit empty-cell violation
  family looks geometrically infeasible.
- B3 sampler produced no valid random configs (rejection too weak) - inconclusive,
  but seeded annealing covers the space better anyway.

## Step 5: KEY REDUCTION (proved, size-free!)
FCMB => FULL Erdos conjecture WITHOUT any d<=1 restriction and WITHOUT subdivision:
For n = N+1 squares ANY sizes/orientations: if |Av| <= s then
g = E[hits] >= P(hit) = 1 - |Av| >= 1 - s, and identity 2Sig = 2N+1-g-s <= 2N.
(Identity and Fubini are size-free; pigeonhole "some square empty on Av" also
size-free: #nonempty <= #points = N < n.)
FCMB(k=1) is proved: |pi(S1) u pi(S2)| <= a^2+b^2 <= (1-a)^2+(1-b)^2 iff a+b<=1 = f(2)=1 (Erdos).
Two-sided structure: Erdos needs only the UPPER bound |Av| <= s;
the mid-range capture lemma (valid packings, g+s<2) needs the LOWER bound |Av| > 0.
Destruction<=payment: D_c := ceil(Sig)-maxC <= Pi + (n-N) + 1 proved (Pi = N-Sig);
capture lemma = "D_c <= Pi + 1 - frac(-Sig)..."; ratio-1/2 forms have zero slack at
Sig->N: equivalent to conjecture, not a weaker stepping stone.
