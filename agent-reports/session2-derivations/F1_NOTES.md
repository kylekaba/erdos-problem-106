# F1 worklog — FCMB-AP: refutation of the unrestricted statement + proof of the restricted statement

Code: `fcmb_check.py` (counterexample verification, exact breakpoint |Av| + grid cross-check),
`search_k2.py` (identity verification, k=2 global search). All runs reproduced below claims.

## 1. THE COLUMN PACKING (counterexample to FCMB as stated, every k >= 2)

P_k: in [0,k]^2 place k+1 squares of side d = k/(k+1) stacked in the column
[0,d] x [0,k] (y-intervals [jd,(j+1)d], j=0..k, tiling [0,k] exactly), plus
k(k-1) unit squares tiling [1,k] x [0,k]. n = (k+1) + k(k-1) = k^2+1 = N+1. Valid AP packing
(machine-checked k=1..6). Invariants: Sum d = k + (k^2-k) = N (BKU-extremal);
g = k/(k+1); s = (k+1)/(k+1)^2 = 1/(k+1); g+s = 1.

|Av| = k/(k+1): for x in [0, k/(k+1)) all k+1 column squares meet lattice line 0; their
y-intervals tile [0,k], which contains exactly k points of y+Z, each interior to exactly one
interval for a.e. y => exactly one column square empty, other k capture; units always capture
k(k-1); C = k + k(k-1) = N for a.e. y. For x in (k/(k+1), 1) all column squares are empty:
C = N - k. So Av = [0,k/(k+1)) x [0,1), |Av| = k/(k+1) (exact; machine-verified).

FCMB demands |Av| <= s = 1/(k+1). Violation = (k-1)/(k+1) -> 1. k=1 gives equality (split
cell a=b=1/2), which is why the k=1 proof could not see this.

Generalization (stack gadget, verified): stack m+1 squares of sides d_1..d_{m+1} <= 1,
Sum = h integer <= k, at the bottom of strip 0 sharing left edge; k-h units above; k(k-1)
units in the other strips. Then (d_(1) <= d_(2) smallest two sides)
   |Av| = d_(1) + (d_(2) - d_(1)) (1 - d_(1)),   and always g + s = 1.
Split-cell = h=1 case: |Av| = a + (b-a)(1-a) = a^2+b^2 = s (tight case of FCMB);
column = equal-sides case: |Av| = d = k/(k+1) (max violation). One formula covers both.

## 2. EXACT DECOMPOSITION IDENTITY (AP, all d_i <= 1)

Generic shifts: c_i = p_i q_i, p_i = 1_{X_i}(x), q_i = 1_{Y_i}(y); X_i, Y_i arcs of length
d_i (projections mod 1). Miss sets M_X(x) = {i : x not in X_i}, M_Y likewise.
alpha_0 = |{M_X empty}|, alpha_i = |{M_X = {i}}|; beta likewise.

Av = {C = N} = {exactly one c_i = 0} = disjoint union of
Av_i = [cap_{j!=i} X_j x cap_{j!=i} Y_j] \ [X_i x Y_i]  (exact, no inequality), giving

   |Av| = alpha_0 Sum_i beta_i + beta_0 Sum_i alpha_i + Sum_i alpha_i beta_i,
   with alpha_0 beta_0 = 0 (budget: else C = N+1 on a positive-measure set).

Termwise alpha_i <= 1 - d_i, beta_i <= 1 - d_i, so Sum alpha_i beta_i <= s ALWAYS.
All FCMB violation lives in the alpha_0/beta_0 terms. [Verified numerically to 5.6e-17
on 200 random valid strip packings at k=2.]

## 3. THEOREM (restricted FCMB-AP, sides <= 1) — fully proved

THEOREM 1. Let S_1..S_{N+1} be an axis-parallel packing of [0,k]^2 with all d_i <= 1 and
Sum d_i > N. Then |Av| <= s. (Hence, by the 3-line chain, no such packing exists:
a new, self-contained, measure-theoretic proof of f_AP(k^2+1) = k for side-<=1 packings.)

Proof. sigma := Sum (1 - d_i) = (N+1) - Sum d_i < 1, all terms >= 0.
LEMMA A: alpha_0 = 0 (indeed {M_X = empty} is null). Suppose x generic with M_X(x) empty:
every square's x-interval contains a (unique, interior) point x + m_i, m_i in {0..k-1}.
Pigeonhole: some m has L >= ceil((N+1)/k) = k+1 squares. These L squares pairwise overlap
openly in x, hence have pairwise disjoint y-intervals in [0,k]: Sum_L d_i <= k, so
Sum_L (1 - d_i) >= L - k >= 1 > sigma >= Sum_L (1 - d_i)  (nonneg terms). Contradiction.
Symmetrically beta_0 = 0. By the identity, |Av| = Sum alpha_i beta_i <= Sum (1-d_i)^2 = s. QED

COROLLARY (new proof of BKU, d <= 1). If Sum d_i > N then g + s < 1 (structure identity)
while g = E[hits] >= P(hits >= 1) = 1 - |Av| >= 1 - s. Contradiction. So Sum d_i <= N. QED

Sharpness: at Sum d = N (sigma = 1) the column packing realizes alpha_0 = k/(k+1) > 0 and
|Av| = g >> s: Lemma A's hypothesis Sum d > N is exactly sharp; the theorem sits one
epsilon from a cliff where |Av| jumps by (k-1)/(k+1).

GAP (general sizes): extension to d_i in (1,2) (d >= 2 is trivial: s >= 1). Big squares
never miss (p_i >= 1) and can capture 2 points on a line, breaking the exactly-one-empty
combinatorics; the over-full-line deficit Sum_L(1-d) >= 1 still holds but can be paid by
negative deficits (d>1) off the line. Not done. (For AP the statement is vacuously true by
BKU; a non-circular proof is what is missing.)

## 4. Logical status of FCMB after this

- Unrestricted FCMB (report section 7A "central conjecture"): FALSE for every k >= 2,
  already axis-parallel, violation -> 1.
- FCMB restricted to g+s < 1: implies the full Erdos conjecture (same 3 lines,
  by contradiction), and is implied by it vacuously. So restricted FCMB is EQUIVALENT
  to the conjecture — no independent content as a statement; its value is the proof
  template (Theorem 1's mechanism: global deficit < 1 forbids over-full lines).
- Theorem D (FCMB => conjecture) remains a valid implication; its hypothesis is false.
- Note (A) folded-gap form: column packing has |pi(G)| = g/k (maximal folding: gap strip
  repeats with period 1 in y). The dislocation heuristic (F) fails on it: zero phase drift.
- Note (E): P(hits>=1) >= g^2/E[hits^2] is tight on BOTH extremal families
  (split: hits Bernoulli(g); column: hits in {0,k}, E[hits^2] = kg). The proposed
  sufficient autocorrelation bound fails at g+s = 1 (must, since FCMB fails there).

## 5. Numerics summary (all in fcmb_check.py / search_k2.py output)

- Column packings k=1..6: exact |Av| = k/(k+1), s = 1/(k+1), maxC = N a.e. (only fp-sliver
  cells of measure <= 8e-16 from closed-boundary double counting show C = N+1 artifacts;
  grid k=3 artifact confined to the single line y = 0.5, fraction 3.7e-4 of grid points, 
  measure 0).
- Split-cell k=2,3, a in {0.37, 0.5, 0.8}: |Av| = s exactly (tight, as previously known).
- Stack-gadget formula: exact match on 5 test cases (k=2,3,4, mixed sides).
- k=2 global search (20k random strip packings + 3 structured seeds + hill-climbing 3 x 4000
  steps on |Av| - s): maximum violation found = +1/3 at the equal column packing; maximum
  |Av| found = 2/3 (same packing). Violations also occur strictly inside g+s > 1
  (e.g. viol +0.18 at g+s = 1.16), so failure is not confined to the boundary.
- Identity |Av| = a0*Sum(bi) + b0*Sum(ai) + Sum(ai*bi): max error 5.6e-17 over 200 random
  packings; a0*b0 = 0 in all cases.
