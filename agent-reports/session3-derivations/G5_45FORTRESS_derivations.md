# G5 — The 45° fortress: FALLEN. Full derivations.

Agent: G5 (session 3). Scripts: `verify_D_formula.py`, `landscape_and_chain.py` (this directory).
Setting: `T=[0,k]^2`, `N=k^2`, `n=N+1` squares, pairwise disjoint interiors, ALL at folded tilt
exactly `45°`, sides `d_i`, `eps = Sum d_i - N`, gap `G = N - Sum d_i^2`, `s = Sum(1-d_i)^2`.
Master identity (algebraic, n=N+1): **2 eps + G + s = 1**. (Check: G+s = N - Sd^2 + (N+1) - 2Sd + Sd^2
= 2N+1-2Sd = 1-2eps.)

Headline results:

- **Theorem 45-A** (all k, unconditional): `Sum d_i <= N + 1/4 + 1/(4(N+1))`.
  First-ever sub-Cauchy–Schwarz bound at 45°, uniform in k (c45 >= 1/4 - 1/(4(N+1)) - ... i.e.
  eps <= 0.375 at k=1, <= 0.30 at k=2, -> 1/4).
- **Theorem 45-B** (k >= 28): `Sum d_i <= N` — the pure-45 case CLOSED to the conjectured value
  for all k >= 28 (and k=1 via T1). Open residue: exact closure for k in [2,27], where 45-A gives
  eps <= 1/4 + 1/(4(k^2+1)).
- **Theorem CO** (common orientation, any angle): all n = N+1 squares at common folded tilt
  theta in (0, pi/4], k >= 28/sin(2 theta)  ==>  `Sum d_i <= N`. Extends T3 (Pythagorean-only,
  c|k) to every angle at large k.
- **Theorem D45** (diamond-container discrepancy; the assigned route): exact two-phase formula
  for D(p), full landscape, and for all-short pure-45 packings (all d_i <= 1) the bound
  eps <= b(gamma), gamma = frac(k/sqrt2), b as in §D below; sub-C-S for gamma outside
  [1/8,1/4] u [5/8,3/4] (density 3/4 of k).

Only 45-A/45-B/CO are needed for the headline; D45 is independent and is the assignment's
deliverable (a)+(b) for the counting route.

---

## Part I. The wall route (Theorems 45-A, 45-B, CO)

Ingredient: **Wall Lemma, sharpened form [V]** (report §4.4; proof report_ROUTE_C_CONSTANT.md
Claim 6; verified + sharpened in p2_V1_T1_TILINGS.md Claim 6 audit):
for any packing in `[0,k]^2`, with `phi(x) = inf{y : (x,y) in Union S_i}` (= k if column empty),
`A_i` = the set where the inf is attained by `S_i` (tie-broken), `A_0` the empty-column set,
`y_i` = height of lowest point of S_i:

    Sum_i ( y_i |A_i| + (sin th_i cos th_i / 2) |A_i|^2 ) + k |A_0|  <=  Int_0^k phi  <=  G.

At theta = 45°: coefficient = 1/4, and the lemma is TIGHT (lower envelope is exactly the V
`f_i(x) = y_i + |x - v_i|`; bathtub `Int_A |x-v| >= |A|^2/4`).

**Floor/ceiling disjointness.** Define `psi(x)` symmetrically from the ceiling. For a column x
that meets at least one square, the lower gap segment `[0, phi(x))` and upper gap segment
`(k - psi(x), k]` are disjoint (phi(x) <= bottom of some square <= its top <= k - psi(x)) and both
uncovered. Empty columns contribute k once. Hence

    G >= [floor sum] + [ceiling sum] + k|A_0|,       (*)

with each bracket of the Wall-Lemma form (same A_0 for both).

### Theorem 45-A (unconditional, every k)

Drop `y_i|A_i| >= 0` in (*). Let a = |A_0|, m1, m2 = number of floor-/ceiling-serving squares
(each <= n = N+1). Cauchy–Schwarz: `Sum_f |A_i|^2 >= (k-a)^2/m1`, same for ceiling. So

    G >= (1/4) (k-a)^2 (1/m1 + 1/m2) + k a >= (k-a)^2 / (2(N+1)) + k a.

The RHS is increasing in a on [0,k] (derivative k - (k-a)/(N+1) > 0), so `G >= k^2/(2(N+1))`.
By the master identity, `2 eps = 1 - G - s <= 1 - N/(2(N+1))`, i.e.

    eps <= 1/4 + 1/(4(N+1)).       QED 45-A

(k=1: eps <= 3/8, but T1 gives eps <= 0 there anyway. k=2: eps <= 0.30. k -> inf: 1/4.)

### Theorem 45-B (Sum d <= N for k >= 28)

Assume eps > 0; derive a contradiction for k >= 28. From the identity, `G + s = 1 - 2 eps < 1`.

Structure from `s < 1`:
 (S1) every d_i < 2 ((1-d_i)^2 <= s < 1);
 (S2) at most 3 squares have d_i <= 1/2 (each contributes >= 1/4 to s);
 (S3) G < 1.

Fix h = 0.04. Let M = #{i : d_i > 1/2, y_i <= h}. Every such square lies in the strip
`[0,k] x [0, h + 2 sqrt2]` (vertical extent of a 45° square = sqrt2 d_i < 2 sqrt2) and has area
> 1/4; the strip has area k(h + 2 sqrt2). Disjointness gives

    M < 4k (h + 2 sqrt2) = 4k * 2.868427...

Floor bound (Wall Lemma at 45°, splitting the serving squares):
- servers with y_i > h pay `y_i|A_i| >= h |A_i|`; total `>= h S2`;
- servers with y_i <= h, d_i > 1/2 pay `Sum |A_i|^2/4 >= S1^2/(4M)` (Cauchy–Schwarz over <= M squares);
- servers with y_i <= h, d_i <= 1/2: at most 3, total served `sigma3 <= 3 * sqrt2/2 = 2.1214`
  (served set ⊆ projection, width sqrt2 d_i <= sqrt2/2), pay >= 0;
- empty columns pay `k a >= h a`.
With `S1 + S2 + (small-server length) + a = k`:

    G_floor >= S1^2/(4M) + h (k - S1 - sigma3).

Minimizing over S1 in [0,k]: interior minimum (S1* = 2Mh) gives `hk - M h^2 - h sigma3`; boundary
S1 = k gives `k^2/(4M) - h sigma3`. Using M < 4k(h+2sqrt2):

    hk - M h^2 > k [ h - 4 h^2 (h + 2 sqrt2) ] = k * 0.0216415...   (h = 0.04)
    k^2/(4M)   > k / (16 (h + 2 sqrt2))       = k * 0.0217895...

So `G_floor > 0.0216 k - h sigma3 = 0.0216 k - 0.0849`. The ceiling gives the same bound on its
(disjoint) region. By (*):

    G > 0.043283 k - 0.1697.

For k >= 28 this exceeds 1.04 > 1, contradicting (S3). Hence eps <= 0.  QED 45-B

Remarks. (i) The count bound M ~ 11.5k is achievable only by side-1/2 squares packed solid, which
would force s ~ 2.9k >> 1; with s < 1 one gets the much stronger `G >~ 0.11 k` asymptotically
(delta-window refinement: #{d_i outside (1-δ,1+δ)} <= s/δ^2), so the true forced waste of any
eps>0-candidate is ~ k/9; the crude constants above suffice for k >= 28 and keep the proof short.
(ii) Numerical anchor: best rotated-grid pure-45 packings measured at G ≈ 2.2–2.8 k
(landscape_and_chain.py: k=5,10,17 give G = 13, 22, 47), an order of magnitude above the bound —
consistent, and showing real pure-45 packings sit at `Sum d ≈ N - Θ(k)`.
(iii) Comparison: the Window Theorem (§4.5) route also closes pure-45 via the identity — G >=
0.9 sin t (0.305k - 387.2) at t = pi/4 gives G > 1 for k >= 1275 — apparently unnoticed until now;
45-B improves the threshold 45x by using the exact 45° wall geometry instead of window generics.

### Theorem CO (all common orientations, large k)

Same proof verbatim with folded tilt theta in (0, pi/4] common to all squares: vertical extent
d(cos th + sin th) < 2 sqrt2 (same strip count M < 4k(h+2sqrt2)); Wall coefficient sc/2 =
sin(2 theta)/4; take h = 0.04 sin(2 theta):

    h - (4/sin 2th) h^2 (h + 2 sqrt2) >= sin(2th) [0.04 - 0.0064 * 2.8685] = 0.021642 sin(2 theta),

so `G > 0.043283 k sin(2 theta) - 0.17`, and `Sum d <= N` whenever `k >= 28 / sin(2 theta)`.
This is the first exact-constant theorem at arbitrary (incl. irrational) common orientations
(T3 needed Pythagorean theta with c | k; T2 gave only N + 1/2). Residual open window per theta:
k < 28/sin 2theta (there T2/T5 still apply).

Adversarial self-attack (all routes tried against 45-B):
- tiny-square wall carpets (diamond chains along the floor, waste -> 0 per length): blocked by s
  (each tiny square costs ~1 in s; only 3 allowed sub-1/2 squares when eps > 0);
- many low big squares to dilute Cauchy–Schwarz: blocked by the strip area count M;
- serving from high up: pays y_i |A_i| >= h |A_i|;
- hiding the floor behind empty columns: pays k|A_0|;
- boundary-vs-interior minimum of the quadratic: both branches computed, min taken;
- the Wall Lemma itself is TIGHT at 45°, so no constant here is fake.

---

## Part II. The diamond-container discrepancy (assigned route) — Theorem D45

### The exact two-phase formula

Rotate to the squares' frame: squares become axis-parallel; T becomes the diamond
`D_k = {(u,v): |u - k/sqrt2| + |v| <= k/sqrt2}` (vertices (0,0),(L,0),(L/2,±L/2), L = k sqrt2).
Lattice `Z^2 + (x,y)`. A lattice point (m+x, n+y) lies in D_k iff, with a = m+n, b = m-n
(parity-linked: a ≡ b mod 2), s = x+y, t = x-y:

    a in [-s, L-s],   b in [-t, L-t].

So the count factorizes over parity classes: `|D_k ∩ (Z^2+p)| = A_e(s)B_e(t) + A_o(s)B_o(t)`,
A_e/A_o = # even/odd integers in [-s, L-s], B likewise in t. Write `k/sqrt2 = K + gamma`
(K integer, gamma in (0,1) irrational). Direct floor computation gives, with
`chi(z) := 1 if z mod 2 in [0, 2 gamma) else 0`:

    A_e(s) = K + chi(s),  A_o(s) = K + chi(s-1),  same in t.

Hence with `sig(s) := chi(s) + chi(s-1)` (**1-periodic**, values {0,1} if gamma<1/2 —
`sig(s) = 1_{s mod 1 in [0,2gamma)}` — and {1,2} if gamma>1/2 — `sig = 1 + 1_{s mod 1 in [0,2gamma-1)}`),
and `X := chi(s)chi(t) + chi(s-1)chi(t-1) in {0,1,2}`:

    **D(x,y) = |D_k ∩ (Z^2+p)| - k^2 = K( sig(x+y) + sig(x-y) - 4 gamma ) + X - 2 gamma^2.**

Machine-verified EXACTLY: 40,000/40,000 random shifts across k = 2,3,4,5,7,10,12,17,29,41
(verify_D_formula.py); empirical mean of D ≈ 0 as required.

Structure: the Θ(K) term depends only on the two diagonal phases u = (x+y) mod 1,
v = (x-y) mod 1; the O(1) cross term X is the only genuinely mod-2 object. The container
discrepancy at 45° is a **two-arc, two-level staircase**: per diagonal phase, one arc
`[0, 2gamma)` (resp. `[0, 2gamma-1)`) of "high" rows.

### The BKU chain in the diamond frame

Half-open squares in the frame: `count_i = p_i q_i`, `p_i,q_i in {floor d_i, ceil d_i}`,
`E p_i = d_i`. Packing: `Sum p_i q_i <= k^2 + D(x,y)` a.e. (0 violations in 9,000 random-shift
trials over 3 packings). With `P = Sum p_i`, `Q = Sum q_i`, `W = Sum (p_i-1)(q_i-1) >= 0`
(|p_i - q_i| <= 1 rules out (0,>=2)), and R = uncovered-count >= 0:

    P(x) + Q(y) + R + W = 2N + 1 + D(x,y)  pointwise;  E P = E Q = N + eps.

Pigeonhole sets `A = {P >= N+1}`, `B = {Q >= N+1}`: if eps > 0 both have positive measure, and

    **A x B ⊆ {D >= 1}   (a.e.).**       (#)

If all d_i <= 1 (all-short): p_i in {0,1}, P = (N+1) - #missed arcs, so
`|A| >= 1 - Sum(1-d_i) = eps`, likewise `|B| >= eps`.

### The landscape of {D >= 1} — four regimes, NO O(1/K) margins needed

Write U = [0, 2gamma) (gamma < 1/2) or U' = [0, 2gamma - 1) (gamma > 1/2) in each diagonal phase.
Evaluating D on each level of (sig(u), sig(v)) — the cross term X vanishes or is dominated
exactly where needed (all four checks below are unconditional in K >= 1):

- gamma in (0, 1/4]: at sig+sig = 0: D = -4K gamma - 2 gamma^2 < 0. So
  `{D>=1} ⊆ {u in U} ∪ {v in U}`  (union regime; |U| = 2 gamma).
- gamma in (1/4, 1/2): additionally at sig+sig = 1: X = 0 and D = K(1-4gamma) - 2gamma^2 < 0. So
  `{D>=1} ⊆ {u in U} ∩ {v in U}`  (intersection regime).
- gamma in (1/2, 3/4]: sig in {1,2}; at sig+sig = 2: X <= 1 and D <= (2-4gamma)K + 1 - 2gamma^2 < 1. So
  `{D>=1} ⊆ {u in U'} ∪ {v in U'}` (union; |U'| = 2gamma - 1).
- gamma in (3/4, 1): at sig+sig = 3: X = 1 and D = K(3-4gamma) + 1 - 2gamma^2 < 0 (2gamma^2 > 9/8). So
  `{D>=1} ⊆ {u in U'} ∩ {v in U'}` (intersection).

### Theorem D45 (all-short pure-45)

Let gamma = frac(k/sqrt2), all d_i <= 1, eps > 0. Then, from (#):

- **Union regimes.** For a.e. x in A: `B ⊆ ((U - x) ∪ (x - U)) mod 1`, so
  `eps <= |B| <= 2|U|`:  `eps <= 4 gamma` (gamma <= 1/4);  `eps <= 4 gamma - 2` (1/2 < gamma <= 3/4).
- **Intersection regimes.** A+B ⊆ U and A-B ⊆ U essentially (mod 1). Upgrade to genuine sumsets:
  replace A by the closed set W = {x : mu(B \ (U-x)) = 0} ⊇_e A (W is a level set of the
  continuous function x -> mu(B ∩ (U-x)), hence closed) and B by its measure-support B*
  (closed, mu B* >= mu B, and x + B* ⊆ closure(U) for x in W). Raikov's sumset theorem on the
  circle [Raikov 1939; Macbeath 1953]: mu(W + B*) >= min(1, mu W + mu B*). Since
  W + B* ⊆ closure(U), |U| < 1:  `|A| + |B| <= |U|`, so
  `eps <= gamma` (1/4 < gamma < 1/2);  `eps <= gamma - 1/2` (3/4 < gamma < 1).

Summary bound `eps <= b(gamma)`, b = 4g / g / 4g-2 / g-1/2 on the four intervals: sub-C-S
(b < 1/2) for every k with gamma outside [1/8, 1/4] ∪ [5/8, 3/4] — asymptotic density 3/4 by
equidistribution of frac(k/sqrt2). Examples (landscape_and_chain.py table): k=17: eps <= 0.083;
k=29: eps <= 0.024 (gamma = 0.5061); k=58: eps <= 0.049; k=10: eps <= 0.284.

### The precise obstruction (deliverable (b))

1. **Phase mismatch is real but not fatal**: D lives in the diagonal phases (x±y), the
   pigeonholes in the axis phases (x, y) — but sig is 1-PERIODIC (the two parity classes are
   offset copies), so for every fixed x the bad set in y still has measure exactly 2|U| (union)
   — the mismatch costs a factor 2, not a collapse.
2. **The genuine obstruction is |A|, |B| vs |U|**: in intersection regimes the enemy survives iff
   it can confine BOTH pigeonhole sets to measure summing to |U|, with A+B and A-B inside single
   arcs. Arc-position freedom is 2 parameters vs the packing's many; the constraint is only on
   measures + sumsets. The wall geometry (Part I), not counting, is what actually kills these.
3. **Big squares (d_i > 1) break |A| >= eps**: p_i in {1,2}; A can shrink to measure ~eps/#big.
   D45 is honestly conditional on all-short. (The S3 dichotomy's b0-route would be the repair.)
4. **gamma in [1/8,1/4] ∪ [5/8,3/4]** (union regime with fat arcs): bound b(gamma) >= 1/2, vacuous.
   For these k the diamond route alone proves nothing beyond T2 — matches Claim 1(d)/Claim 6
   no-gos: at 45° no exact budget exists and the fluctuation is Θ(k), only its two-phase
   STRUCTURE (not its size) is exploitable.

## CHECKS (machine)

1. D-formula: exact match 40,000/40,000 (10 values of k, random shifts); mean-zero confirmed.
2. Chain `Sum p_i q_i <= k^2 + D`: 0 violations / 9,000 shifts on rotated-grid pure-45 packings
   (k = 5, 10, 17; 12/78/242 squares).
3. Wall Lemma at 45°, original frame, direct quadrature: LHS 7.537 <= Int phi 7.787 <= G 13 (k=5).
4. Identity 2eps + G + s = 1: algebraic; also numerically on test packings.
5. All landscape thresholds re-derived symbolically AND spot-checked numerically (levels of D on
   each (sig,sig,X) cell match the formula's predicted values and measures).
6. 45-B constants: h = 0.04: g = 0.0216415, g2 = 0.0217895, threshold k >= 27.02 -> 28. Verified
   by direct evaluation.

## DEAD ENDS (this assignment)

- Adding left+right walls to 45-A for a factor 4: the horizontal serving regions can overlap the
  vertical ones (corner gaps double-counted); only floor+ceiling (and separately left+right) are
  provably disjoint. Factor 2 is the honest maximum, giving 1/4 (not 1/8) in 45-A.
- Making D45 unconditional via P_max control: sup P - N is O(#big), and no bound on #big better
  than s-counting exists; the b0 >= eps enemy survives counting (as S3 predicted).
- Using D's O(1) cross term X for an extra kill: it shifts thresholds by O(1/K) only and its sign
  is enemy-favorable exactly on the boundary cells; all regime inclusions were instead arranged
  to hold unconditionally, so X carries no further information at this order.
- FKG/rearrangement on {D<=0} ∩ (A x B): unnecessary once sig was seen to be 1-periodic — the
  problem reduces to 1-D arc avoidance + sumsets; nothing stronger is available (the enemy CAN
  realize interval A, B with a legal miss-arc arrangement, so the measure bounds b(gamma) are
  tight for the counting information used).

## BEST NEXT STEP

Close k in [2, 27] for pure-45 (only remaining window): per-k optimization of the 45-B constants
(the delta-window refinement `#{d outside (1±delta)} <= s/delta^2` with two or three delta-levels
should push the threshold to k ~ 12–15), plus D45 bounds where gamma is favorable (k = 3,5,10,15,17,
22 all have b(gamma) < 1/2, and eps <= 4gamma is already < the 45-A bound at k = 17), plus exact
small-k SAT/SLSQP certification below N + 1/4 (numerics already certify < N for k <= 4). More
strategically: port the CO mechanism into the trichotomy — regime (I) incoherent-tilt interfaces
now have a proved 45°-anchor (the wall pays sin(2θ)/4 per unit squared served length against ANY
common-θ grain touching a wall), which is exactly the quantitative bridge (I)->(gap) the
orchestrator flagged as order-marginal.
