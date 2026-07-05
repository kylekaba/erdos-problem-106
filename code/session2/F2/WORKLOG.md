# F2 worklog — FCMB refutation

## The refuting family (row packings R_k), fully rigorous

R_k in T=[0,k]^2, n = k^2+1 = N+1 squares:
- Bottom row: k+1 squares Q_i = [(i-1)k/(k+1), ik/(k+1)] x [0, k/(k+1)], i=1..k+1, side k/(k+1).
  Their union is EXACTLY the strip [0,k] x [0, k/(k+1)].
- Units: [a,a+1] x [b,b+1] for a=0..k-1, b=1..k-1, tiling [0,k] x [1,k] exactly.
- Gap G = [0,k] x (k/(k+1), 1), area g = k/(k+1).

Checks: n = (k+1) + k(k-1) = k^2+1. Sum d_i = k + k(k-1) = k^2 = N (EXTREMAL packing,
attains the conjectured optimum; for k=2 it is a classical f(5)=2 equality configuration).
s = (k+1) * (1/(k+1))^2 = 1/(k+1).  g + s = 1 exactly (consistent with structure identity).

|Av| computation (exact, no numerics): p=(px,py) in [0,1)^2, lattice points (px+a, py+b),
a,b in {0..k-1}. b>=1 points lie in [0,k]x[1,k] = tiled by units: always captured.
b=0 points lie at height py: if py < k/(k+1) they are in the fully-covered strip
(captured for every px); if py in (k/(k+1),1) ALL k of them are in G (hits = k).
Hence Av = {py < k/(k+1)} (mod measure zero), |Av| = k/(k+1).

FCMB demands |Av| <= s: k/(k+1) <= 1/(k+1) — FALSE for every k >= 2,
violation margin |Av| - s = (k-1)/(k+1) -> 1 as k -> infinity.

Folded form: pi(G) = [0,1) x (k/(k+1),1), |pi(G)| = 1/(k+1) < 1 - s = k/(k+1);
the strip folds with multiplicity exactly k (k cells share the same gap offsets).

hits distribution: hits in {0, k}; P(hits=k) = 1/(k+1). E[hits] = g = k/(k+1) OK
(conjecture-side inequality g >= 1-s holds WITH EQUALITY; the packing is on the critical
surface g+s=1). What FCMB threw away: E[(hits-1)^+] = (k-1)/(k+1) = exactly the violation.
Identity: g = (1-|Av|) + E[(hits-1)^+]  =>  (sum d <= N) <=> (|Av| <= s + E[(hits-1)^+]).

Second-moment (condition E): E[hits^2] = k^2/(k+1); autocorr = k(k-1)/(k+1) (x-translates
of the strip overlap fully, k-|v| cells for shift v); g^2/(1-s) = k/(k+1).
Condition E fails (k^2 > k). Paley–Zygmund is TIGHT on R_k:
P(hits>=1) = 1/(k+1) = g^2/E[hits^2] (two-point distribution).

## Why previous searches missed it
Previous session tested: split-cell (tight, F=0), column tilings (g=0, |Av|=1, s=1 EXACTLY —
verified: s = b^2/(k+b) + (b-1)^2/(k+1-b) = 1 identically when k=2b(b-1); tight, no
violation), corner+center 5-square family, coherent grains, annealing near those seeds.
The row extremal — one of the most classical equality configurations — was never evaluated
for |Av|. FCMB was calibrated at k=1, where the row IS the split cell (tight); the two
families diverge for k >= 2 because s scales as 1/(k+1) while |Av| stays ~1.

## Straddle family (continuous path from split-cell boundary into violation), k=2
delta in (0, 1/3]: squares (1-delta)^2 at [0,1-d]x[0,1-d] and [1+delta,2]x[0,1-delta],
b = 2delta at [1-delta,1+delta]x[0,2delta], 2 units on top. Sum d = N exactly for ALL delta.
Exact: |pi(G)| = 3delta - 6delta^2, 1-s = 4delta - 6delta^2, F = -delta.
Verified numerically at delta = 0.05, 0.1, 0.2, 0.3 (F = -delta to 1e-6, exact SAT-feasible).
At delta -> 0 this approaches N units + vanishing square: violations exist at every scale
of proximity to the trivial boundary. At delta = 1/3 it becomes R_2.

## Row optimality (partial argument + numerics)
Among packings whose gap lies within a single row of cells (mult <= k) and with the
conjecture (g+s>=1) granted: F = piG + s - 1 >= (1-s)/k + s - 1 = (s-1)(1-1/k) minimized
by minimizing s; deficit carriers for a one-band gap number <= k+1 (n-budget: a 1xj strip
of cells can host at most j+1 squares without exceeding n = N+1), so s >= 1/(k+1) and
F >= -(k-1)/(k+1) with equality exactly at R_k. Numerics (Nelder-Mead multistart with
exact-feasibility repair, k=2): every violating start converges to R_2; nothing below -1/3.
Unconditional lower bound (any packing, conjecture granted): mult <= N gives
F >= (s-1)(1-1/N) >= -(N-1)/(N+1); beating the row would need gap folding coherently
across >= 2 rows of cells, which needs deficit carriers in >= 2 rows — n-budget allows
only one "extra"; two coherent full rows cost +2. Not a proof for general (tilted,
multi-band) configs, but k=3 search found nothing below the row either.

## Files
- fcmb.py: rasterizer (validated: split-cell F = 0.000000 at M=1200), direct |Av|
  shift-sampler (independent check: 0.666667 = 2/3 at k=2), exact SAT feasibility.
- optimize.py, repair.py: multistart Nelder-Mead + exact repair; best_k2.json.
- triage.py: repeated-offset margins jdelta^2 (exact), tilt response, N+2-truncations.
- opt_k2.log, opt_k3.log.
