# RIGIDITY agent — complete derivations (session 2, final push)

Assignment: mod-1 Rigidity Lemma / dichotomy (W or circle-Littlewood-Offord kappa).
Notation as in ERDOS_106_REPORT.md: T=[0,k]^2, N=k^2, M=N+1 squares, sides d_i, folded
tilts th_i in [0,pi/4], u1 = cos+sin, sigma_i = u1(th_i)-1, w_i = d_i u1(th_i),
eps = sum d_i - N, t = sum w_i - N, tau = sum d_i sigma_i = t - eps (>=0),
P(x) = sum p_i(x), Q(y) = sum q_i(y) vs the shifted lattice, kappa = E[(2N+1-P-Q)_+],
kappa' = E[(P+Q-2N-1)_+]. (x,y) uniform on the shift torus; P and Q are INDEPENDENT
as random variables (P depends only on x, Q only on y). Both projections of a square's
bbox have length w_i, so E[P] = E[Q] = N + t, and kappa = (1-2t) + kappa'.

Everything below is elementary given: (A) the 1-D arc structure
p_i(x) = floor(w_i) + 1_{F_i}(x) a.e., |F_i| = frac(w_i) [V, report §1/§5];
(B) for Theorem K' only: the MPI chain of T6 [P].

---------------------------------------------------------------------------
## 1. Lemma K (two-variable integer anti-concentration). NEW. Self-contained.

**Lemma K.** Let phi, psi be independent integer-valued random variables with
mu1 = E[phi], mu2 = E[psi], 0 <= mu1, mu2 <= 1. Then

    E[(phi + psi - 1)_+]  >=  mu1 * mu2 ,

with equality iff phi, psi are Bernoulli(mu1), Bernoulli(mu2) supported on {0,1}
(equality analysis below). The hypothesis mu <= 1 is necessary (phi=psi=3 a.s. gives
5 < 9).

*Proof.* Two pointwise inequalities for integers a, b:

  (I)   (a+b-1)_+ >= a_+ 1{b>=1} + b_+ 1{a>=1} - 1{a>=1} 1{b>=1}.
        [a,b>=1: both sides equal a+b-1 (>=1>0). If exactly one of a,b >= 1, RHS = 0
         (the positive part of the non-positive one vanishes and its indicator kills
         the other's term)... explicitly a>=1, b<=0: RHS = a_+*0 + 0*1 - 0 = 0 <= LHS.
         Both <=0: RHS = 0.]

  (II)  (a+b-1)_+ >= (a-1)_+ + b * 1{a>=1}   for ALL integers b (any sign).
        [a>=1: RHS = a-1+b <= (a+b-1)_+ since x <= x_+. a<=0: RHS = 0 <= LHS.]

Write p = P(phi>=1), q = P(psi>=1), A = E[phi_+], B = E[psi_+]. Basic facts:
A >= mu1 (phi_+ >= phi), A >= p (phi_+ >= 1{phi>=1}); same for B, q.
E[(phi-1)_+] = E[(phi-1) 1{phi>=1}] = A - p. By independence, expectations of (I), (II):

  (I')   E[(phi+psi-1)_+] >= A q + B p - p q .
  (II')  E[(phi+psi-1)_+] >= (A - p) + mu2 p  =  A - (1 - mu2) p .
  (II'') symmetrically       >= B - (1 - mu1) q .

Case 1: p <= mu1. Since mu2 <= 1, (II') is non-increasing in p, so
E >= A - (1-mu2) mu1 >= mu1 - (1-mu2) mu1 = mu1 mu2.
Case 2: q <= mu2. Symmetric via (II'').
Case 3: p > mu1 and q > mu2. By (I') with A >= p, B >= q:
E >= p q + q p - p q = p q > mu1 mu2.                                        QED

*Equality.* Case 3 is strict. In Case 1 equality needs A = mu1 (no negative part,
phi >= 0 a.s.) and p = mu1 (so E[(phi-1)_+] = A - p = 0, i.e. phi in {0,1});
then for the applied combination one checks psi in {0,1} likewise. Bernoulli pairs
attain: E[(B1+B2-1)_+] = P(B1=B2=1) = mu1 mu2.

Verified: 200,000 random discrete-law pairs on support {-3..5} with means in [0,1]:
0 violations (lemmaK_check.py).

---------------------------------------------------------------------------
## 2. Theorem K (dip-mass anti-concentration; the exact "circle Littlewood-Offord").

**Theorem K.** For every family of N+1 squares in [0,k]^2 (any sizes, any
orientations, packing NOT required — only the projection/arc structure is used):
if 0 <= t <= 1 then
        kappa' >= t^2      and equivalently      kappa >= (1 - t)^2 .
(For t < 0: kappa >= 1-2t > 1 trivially but (1-t)^2 can fail — jittered split grid:
kappa = 1.3200 < 1.3456; for t > 1: sharp floor is kappa' >= 2t-1, i.e. kappa >= 0.)

*Proof.* phi = P - N and psi = Q - N are independent integer-valued with means t.
kappa' = E[(phi + psi - 1)_+] >= t^2 by Lemma K (0 <= t <= 1).
kappa = 1 - 2t + kappa' >= 1 - 2t + t^2 = (1-t)^2.                             QED

**Tightness — exact equality on every known extremal configuration.** Machine-exact:
split cell (all a), deficient column U_k (k=3,4), T12 column tiling (k=4),
deficient-row packing, all have t=0 and kappa = 1 = (1-t)^2 EXACTLY; the diamond
pair (k=1, two 45-degree squares side 0.47) has t = 0.3294 and
kappa = 0.449817... = (1-t)^2 to machine precision. So K is the exact envelope:
the answer to F4's "pin the true shape of the dip-mass anti-concentration statement".

**What K settles about the assigned dichotomy.** The assignment's route (b) asked:
"phases spread => dip mass >= f(K,lambda) => kappa >= 2c". Two-sided resolution:
(i) POSITIVE: the dip mass has the unconditional floor (1-t)^2 — no phase hypothesis
    at all; the conjectured "Gaussian-small but positive" lower bound is in fact
    polynomial and exact, and clustering *raises* kappa (measured: column-phase arc
    systems at t=1/2 have kappa ~ 0.9 vs the floor 0.25; equidistributed phases
    exactly attain 0.25).
(ii) NEGATIVE: the floor is (1-t)^2, NOT a function of phase spread — and T4 forces
    every enemy (eps > 1/2 - c) to have tau >= eps, hence t = eps + tau >= 2 eps
    > 1 - 2c, hence (1-t)^2 < 4c^2 << 2c. Also kappa = 0 is genuinely attainable at
    the arc level (all w_i >= 1 gives P, Q >= N+1 everywhere). **So no lower bound on
    kappa in terms of phase data alone can reach 2c for the enemy: the phase-spread
    degree of freedom is FREE at pigeonhole depth 1.** The "either W or
    Littlewood-Offord" dichotomy cannot close the conjecture; the second jaw must be
    geometric (C''-union / interface gap), not measure-theoretic. This is the
    kappa-side sharpening of F4's No-Repair theorem.

**Naive circle-LO is false (for the record).** M arcs of length 1/2 with phases
j/M: coverage is identically M/2 (+-1); the lower level set at depth >= 2 below the
mean is EMPTY although the endpoint phases are maximally spread (2M equidistributed
points need K arcs of total length lambda >= ... any cover with lambda < 1 has
K ~ M). So "spread endpoints => positive dip measure at fixed depth" is false;
integrality of the mean is the only true source of forcing (Section 4).

---------------------------------------------------------------------------
## 3. Theorem K' (tilt-mass window). Status: [chain of T6, i.e. P] + Lemma K.

MPI (report T6 [P]): D(x,y) := sum_i (L_i - B_i)_+ >= P(x) + Q(y) - 2N - 1 a.e.;
D >= 0, hence D >= (P+Q-2N-1)_+ pointwise, hence E[D] >= kappa'.
Per-square first-moment bound (T6's verified branch identities, §5 of the report):
E[(L_i - B_i)_+] <= 2 d_i sigma_i - m_i with the exact margins m_i >= 0.
Combining with Theorem K:

**Theorem K'.** For every packing of N+1 squares in [0,k]^2:
  if t <= 1:   ( eps + tau )_+^2  <=  2 tau - sum_i m_i ,
  if t >= 1:   2 eps <= 1 - sum_i m_i   (T6 with kappa >= 0).

Consequences.
(a) tau = 0 (axis-parallel) forces eps <= 0: K' *contains* BKU's g(k^2+1) = k
    endpoint (the chain at tau=0 reads: c=pq >= p+q-1 with the (0,>=2) corner
    excluded, budget, and Lemma K replacing the two max-pigeonholes by a mean
    statement with quadratic gain — a third proof shape for BKU's endpoint, after
    BKU's own and the restricted-FCMB measure proof).
(b) Quadratic window: for t <= 1 and sum m_i >= 0,
    tau in [ (1-eps) - sqrt(1-2eps), (1-eps) + sqrt(1-2eps) ].
    The LOWER root ~ eps^2/2 + ... is weaker than T4's tau >= eps for eps near 1/2
    (honest: K' adds no enemy constraint beyond T4/T6 at eps -> 1/2); the window's
    value is that it is a single smooth inequality exactly tight on the extremal
    manifold (all t=0 extremals: 0 <= 0). (Feasible diamond pair: lhs 0.1085 vs
    rhs 0.4418 — not tight; the arc-level equality of Theorem K on the diamond
    pair is the sharp statement, K' loses through the margin bound.)
(c) Enemy width pinch (with T4): every enemy has t >= 2 eps > 1 - 2c; and if
    t <= 1, K' pins tau <= 1 - eps. So the enemy's width surplus satisfies
    t in (1-2c, infinity) with the sub-case t <= 1 squeezed into (1-2c, 1]:
    the enemy must fake essentially exactly one extra unit of total width via tilt.

---------------------------------------------------------------------------
## 4. The dip structure theory (D1-D4) and the proved clustering forcing.

Fix one axis. Split the squares: U = {i : w_i < 1}, O = {i : w_i >= 1}; n- = |U|.
For i in U let J_i = complement of the hit arc, |J_i| = gamma_i = 1 - w_i
("deficit arc": phases at which the lattice MISSES square i; its endpoints are the
two bbox-extreme phases of square i). Gcheck(x) = sum_U 1_{J_i}(x) = number of
simultaneously missed undersize squares. Fplus(x) = sum_O 1_{F_i}(x) = number of
oversize frac-hits (arcs beta_i = frac(w_i)). Set

    r = 1 + sum_i (floor(w_i) - 1)_+   (>= 1;  r = 1 whenever all w_i < 2).

**D1 (dip identity, exact, a.e.).**   { P <= N }  =  { Gcheck - Fplus >= r }.
*Proof.* P = W0 + sum 1_{F_i}, W0 = sum floor(w_i). For i in U, 1_{F_i} = 1 - 1_{J_i}.
So P = W0 + n- - Gcheck + Fplus, and P <= N iff Gcheck - Fplus >= W0 + n- - N.
W0 + n- = sum_i max(floor(w_i),1) = (N+1) + sum_i (floor(w_i)-1)_+ = N + r.  QED

**D2 (mean identity).**  E[Gcheck - Fplus] = r - t.
*Proof.* E = sum_U (1-w_i) - sum_O (w_i - floor w_i)
= sum_i (1 - w_i) + sum_O (floor(w_i) - 1) = (N+1 - sum w) + (r-1) = r - t.  QED

**D3 (stack forcing).** Let E_x = {P <= N}, delta_x = |E_x|, and
H_x = ess sup_{E_x} Gcheck (max number of simultaneously missed undersize squares
over the dip set). Then

    integral_{E_x} Gcheck  >=  1 - t        and        (1-t)_+ <= H_x delta_x .

*Proof.* On the complement of E_x, Gcheck - Fplus <= r - 1 (integer, < r), so
int_{E_x}(Gcheck - Fplus) >= (r-t) - (r-1)(1-delta_x) >= 1 - t. Drop Fplus >= 0.
Then 1-t <= int_{E_x} Gcheck <= H_x delta_x.                                  QED

**D4 (kappa lower bounds).**
  (a) kappa >= delta_x delta_y            [P<=N and Q<=N give P+Q <= 2N];
  (b) kappa >= (1-t)_+ max(delta_x, delta_y)
      [for x in E_x: (2N+1-P-Q)_+ >= (N+1-Q)_+ pointwise in y, and
       E_y[(N+1-Q)_+] >= E_y[N+1-Q] = 1-t; integrate over E_x];
  (c) hence with D3:  kappa >= (1-t)_+^2 / min(H_x, H_y)   —
      and Theorem K strengthens this to kappa >= (1-t)^2 outright (H >= 1 on a
      nonempty dip set; D1-D4 remain of value because they localize WHERE the dip
      lives and WHAT pays when it is small).

**(★★) combined form** (unconditional, t <= 1):
      1 - eps  <=  tau  +  sqrt( kappa * min(H_x, H_y) ) .
Verified exactly on 7 packings; EQUALITY on deficient column (min H = 1 via the
winding axis!), split cell, T12, deficient row.

**Corollary R (forced deficit-phase clustering — the proved variant of the mod-1
Rigidity Lemma, valid in the regime t < 1).** If eps > 1/2 - c, t < 1 and the
packing survives T6 (kappa + sum m_i < 2c), then D4(b) gives on EACH axis
    delta <= kappa / (1-t) < 2c / (1-t),
while D3 says deficit-arc mass >= 1-t lies inside E (measure delta): on both axes,
at least (1-t) of the deficit-arc mass mod 1 is crammed into <= N+1 arcs of total
length < 2c/(1-t), and >= (1-t)^2/(2c) undersize squares are simultaneously trapped
strictly inside the open unit strips of a single common lattice (interpretation of
H via D1: a missed square's bbox projection lies strictly between consecutive
lattice lines). Numbers at c = 1/400 if additionally tau <= 1/4 (so 1-t > 1/5):
both axes have >= 1/5 of deficit mass in measure < 2c/(1-t) = 0.025 and stacking
H >= (1-t)^2/(2c) = 8 —
deficient-column-like dislocations on both axes simultaneously.
HONEST LIMITATION: T4 forces the true enemy into t >= 2 eps > 1 - 2c, where this
corollary is vacuous ((1-t) < 2c). It has content exactly in the moderate-tilt
window tau < 1 - eps - (payment), which T4 says is empty for eps > 1/2 - c. So the
clustering forcing is real mathematics but the enemy walks around it by paying
width surplus — the same neutralization as (ii) of §2. The surviving pressure point
is NOT the phases; it is the pointwise covering demand of §5.

**Lemma S (stack geometry, AP case).** If Gcheck_x(x*) >= H at a generic phase x*,
the H missed squares lie strictly inside the open vertical strips of x* + Z. Two
axis-parallel squares in the same open unit strip with w_1 + w_2 > 1 have disjoint
y-projections; hence if all missed squares have w > 1/2, the squares in one strip
stack vertically and any strip containing k+1 of them carries deficit
sum (1 - d_i) >= 1 (their heights sum <= k) — the deficient column is the unique
minimal saturator. (Tilted version needs the chord bookkeeping — GAP, low value
given the neutralization above.)

---------------------------------------------------------------------------
## 5. The enemy covering law (what replaces the rigidity lemma as the open core).

Combining T4 (t >= 2eps), T6 (kappa + sum m < 2c), D1, D4(a):
every enemy satisfies, with r as above, ON BOTH AXES up to product measure 2c:

    Gcheck(x) - Fplus(x) <= r - 1   outside a dip set, delta_x delta_y < 2c,

i.e. THE UNDERSIZE MISSES MUST BE POINTWISE DOMINATED (up to r-1) BY OVERSIZE
FRAC-HITS at almost every phase on at least one axis — an exact integer covering
system in which every unit of domination is paid by width surplus w_i - 1 <= 
d_i sigma_i + (d_i - 1)_+ u1, i.e. by tilt or by oversize sides. At the same time
C'' demands sum (1-w)_+ + max(U_x, U_y) >= 1. These two, plus alpha'-edge for the
gap side, are the full surviving system. The pointwise covering demand is the
correct successor target: it is capture-side (F4's residue), quantitative, and the
deficient column shows its extremal mechanism (resonant winding) — but at eps > 0
the winding budget breaks (F4 Claim 5b), which is where the contradiction should
be extracted.

---------------------------------------------------------------------------
## 6. Numerics index (all code in this directory).

dipstack_check.py : exact piecewise-constant arc engine; SAT disjointness; D1-D4,
  (★★) on 7 packings + 4000-trial arc MC (0 failures; worst H delta/(1-t) = 1.0000,
  equality realized). enemy_arcs.py : enemy-shaped arc systems (t = 1/2, M = 17),
  5 phase strategies x 3 spreads x 60 trials: kappa min 0.25 = (1-t)^2 attained by
  equidistributed phases; clustered/column phases give kappa 0.79-0.99; worst
  kappa*minH/(1-t)^2 = 1.0000 (claim >= 1, tight). lemmaK_check.py : Lemma K MC
  (200k law pairs, 0 failures), Theorem K + K' + T6 on 10 packings incl. tilted
  deficient columns and diamond pair (kappa = (1-t)^2 equality to machine precision).
