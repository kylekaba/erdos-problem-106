# G6 (session 3): the Marginal Displacement Theorem, the death of the top-heavy
# branch, and the corrected beta-frontier of the extremal manifold

Author: agent G6, session-3 final assault. Code: `g6_check.py` (this directory;
durable copy `code/session3/g6_check.py`). All notation as in ERDOS_106_REPORT.md:
T = [0,k]^2, N = k^2, n squares S_i with sides d_i and folded tilts th_i in [0,pi/4],
w_i = d_i(cos th_i + sin th_i), eps = Sum d_i - N, g = N - Sum d_i^2, s = Sum(1-d_i)^2,
b0 = Sum(d_i-1)_+, t = Sum w_i - N, tau = Sum d_i sigma_i (sigma = cos+sin-1),
beta = Sum(1 - d_i sec th_i)_+, Gamma = Sum[(1-d_i)_+ - (1-d_i sec th_i)_+] >= 0,
P(x) = Sum_i p_i(x) with p_i = # vertical lattice lines x+m meeting int S_i,
B_i^x = the two end-region phase arcs of S_i (each of length d_i sin th_i, at the
bbox x-extremes; C''s tall-triangle bad set), U_x = |Union_i B_i^x|,
V_x = |Union_i {x : p_i >= 2}|, Av = {C = N}. New: b0sec := Sum(d_i sec th_i - 1)_+,
rho := Sum d_i(sec th_i - 1) >= 0. Identity: beta - b0sec = n - Sum d_i sec th_i;
for n = N+1: beta - b0sec = 1 - eps - rho.

Everything below is self-contained modulo two imported components, both from the
verified session-2 arsenal: Lemma 0 (chord constancy) [P, machine-checked to 1.6e-15]
and, for Theorem S2' only, the S2 assembly ledger [P, one step still awaiting
independent verification — inherited and flagged].

---------------------------------------------------------------------------
## 1. THEOREM G6-1 (Marginal Displacement Theorem, MDT)

**Theorem.** Let S_1..S_n be any packing of T = [0,k]^2 (any sizes, any
orientations). Then for a.e. x with x mod 1 not in Union_i B_i^x ("good x"):

   P(x) - N  <=  Sum_i p_i(x) (1 - d_i sec th_i)  <=  n - Sum_i d_i sec th_i .

For n = N+1: P(x) <= N + 1 - eps - rho on the good set; since P is an integer,
**eps + rho > 0 implies P(x) <= N for a.e. good x**. Symmetrically in y.

### Proof.

Fix x in (0,1) generic: exclude the null set of x for which some lattice line
x+m (m in Z) passes through a vertex of some square or an endpoint of some bbox
x-range. The vertical lattice lines meeting (0,k) are l_m = {x+m} x R, m = 0..k-1
(exactly k lines; every square's projection lies in [0,k]).

**Lemma G6-A (per-line capacity).** For each m, with L_m = {i : l_m meets int S_i}
and ch_i(X) = |{y : (X,y) in S_i}| the vertical chord:
   Sum_{i in L_m} ch_i(x+m) <= k .
*Proof.* The chords are intervals with pairwise disjoint interiors (the squares
have disjoint interiors) contained in [0,k] (containment in T). QED

**Lemma G6-B (chord law; = session-2 Lemma 0).** Normalize S_i's bbox x-range to
[0, w_i] and write u = X - x_i^min. Then ch_i <= d_i sec th_i everywhere, with
equality identically on the middle region u in [d_i sin th_i, d_i cos th_i];
the complement of the middle region consists of two end regions of length
d_i sin th_i each. Hence for good x every line meeting any square meets it in
its middle region, with chord exactly d_i sec th_i. (For AP squares B_i^x is
empty and every x is good; ch = d_i everywhere on the projection.) QED (session 2)

**Fact 1 (deficit-chord squares cannot double-hit at good x).** If
d_i sec th_i < 1 then p_i(x) <= 1 at every good x.
*Proof.* d_i < cos th_i, so the middle region has length
d_i(cos th_i - sin th_i) < cos th_i (cos th_i - sin th_i) <= cos^2 th_i <= 1.
At good x all incident lines lie in this interval; consecutive lattice lines are
distance 1 apart, so at most one fits. QED

**Fact 2 (surplus-chord squares always hit at good x).** If d_i sec th_i >= 1
then p_i(x) >= 1 for a.e. x (good or not), and at good x all its incident lines
are middle-region lines.
*Proof.* w_i = d_i(cos th_i + sin th_i) = (d_i sec th_i) * cos th_i (cos th_i + sin th_i)
and cos th (cos th + sin th) = (1 + cos 2th + sin 2th)/2 >= 1 for th in [0, pi/4]
(cos 2th + sin 2th = sqrt2 sin(2th + pi/4) >= 1 there, equality at the endpoints).
So w_i >= 1 and the open bbox range, an interval of length >= 1, contains at
least one point of x + Z for a.e. x. At good x no incident line is in an end
region, so all are in the middle. QED

**Assembly.** At good x:
   P(x) - N = Sum_m (|L_m| - k)
            <= Sum_m Sum_{i in L_m} (1 - ch_i(x+m))        [Lemma G6-A]
            =  Sum_i p_i(x) (1 - d_i sec th_i)             [Lemma G6-B, good x].
Split by sign of (1 - d_i sec th_i). Deficit-chord squares: coefficient > 0 and
p_i <= 1 (Fact 1): term <= (1 - d_i sec th_i)_+. Surplus-chord squares:
coefficient <= 0 and p_i >= 1 (Fact 2): term <= -(d_i sec th_i - 1)_+. Hence
   P(x) - N <= beta - b0sec = n - Sum_i d_i sec th_i .                     QED

**Remarks.**
(a) The whole point is the SIGNED ledger. Session-2 Lemma A'' pigeonholed one
over-full line and then dropped the negative (oversize) terms, which is what
created the hypothesis beta < 1 and the top-heavy escape branch b0 >= eps + Gamma.
Keeping the signs and summing over all k lines, the oversize credit -b0sec
returns, and beta - b0sec <= 1 - eps automatically for n = N+1: **no hypothesis
survives.** Facts 1 and 2 are exactly what makes the signed sum legal.
(b) Sharpness: bound = 1 with P = N+1 attained on positive measure across the
entire known extremal catalogue (Section 4).
(c) At th = pi/4 the middle region degenerates and B-arcs swallow the whole
projection: the good set is empty and MDT is vacuous (not wrong); 45-degree
stays with the alpha'/T2 jaw, as with every counting statement of this family.

---------------------------------------------------------------------------
## 2. COROLLARY G6-2: the full BKU theorem, one axis, five lines, all sizes

**Theorem.** Every axis-parallel packing of n = k^2 + 2c + 1 squares in [0,k]^2
(c >= 0 integer, ARBITRARY sizes) has Sum d_i <= k^2 + c. Unscaled:
g(k^2+2c+1) = k + c/k.

*Proof.* AP: all B_i^x are empty, every x is good, rho = 0, sec = 1. Suppose
Sum d_i = N + c + eps with eps > 0. MDT: P(x) <= N + (n - Sum d_i) =
N + c + 1 - eps for a.e. x; P integer: P(x) <= N + c a.e. But
E[P] = Sum_i E[p_i] = Sum_i d_i = N + c + eps > N + c. Contradiction. QED

Notes. (i) This closes F1's flagged gap "extension of C4 to d in (1,2)" in the
strongest possible way: the size-free BKU reproof exists, is one-axis (no q, no
capture counts, no product structure c = pq, no second pigeonhole), and is
shorter than every previous proof in this project (F1's half-page proof needed
all d <= 1; S4 needed b0 < eps; both hypotheses are now gone). (ii) It does NOT
contradict first-moment neutrality [V]: that principle concerns capture counts
c_i (E[c] = d^2, exactly critical); MDT trades in incidence counts p_i
(E[p] = w) plus pointwise chord capacity, and the strict gain is the integer
rounding of P — max-vs-mean, exactly where the report says the problem lives.
(iii) It does not contradict the LP gap: integrality of P is not LP-representable.
(iv) VERIFIER TODO: read BKU (code/session2/bku24.pdf) and confirm this argument
is not buried in their paper; from the report's [V] description (c = pq + two
1-D pigeonholes) it is not.

---------------------------------------------------------------------------
## 3. COROLLARY G6-3, THEOREM S2', COROLLARY S3': the top-heavy branch is dead

**Corollary G6-3 (unconditional over-full-line exclusion on enemies).** Any
packing of N+1 squares with eps > 0 (or eps = 0 and rho > 0, i.e. any tilt
present at criticality): for a.e. good x, P(x) <= N; in particular some
p_i(x) = 0 (all p_i >= 1 would force P >= N+1). Same in y. This is session-2
Lemma A'' with the hypothesis beta < 1 DELETED (on the enemy side, where it is
needed; for eps < 0 packings A''-type conclusions genuinely fail and beta < 1
is still the right hypothesis there — the deficient column shows the constant
is sharp at the eps = 0, rho = 0 boundary, where full-hit measure k/(k+1)
appears; MDT reproduces this boundary exactly: bound = N + 1 - 0 - 0).

**Theorem S2' (unconditional tilted capture-measure bound).** Every packing of
n = N+1 squares with eps > 0 satisfies
   |Av| <= Sum_i (1 - w_i)_+^2 + U_x + U_y + V_x + V_y .
*Proof.* Verbatim the session-2 proof of Theorem S2 (SQUEEZE_DERIVATIONS.md),
whose ONLY use of beta < 1 was invoking Lemma A'' to get both miss-sets
M_X(x), M_Y(y) nonempty a.e. on E = (good x) x (good y); G6-3 supplies this
from eps > 0 alone. All other steps (E-structure c_i = p_i q_i off the U-arcs
[V]; idle/multiplicity ledger |I| = 1 + mu; exactly-one-idle events inside
disjoint products of total measure Sum(1-w)_+^2; mu >= 1 events inside the
V-arc unions) are untouched. QED
*Status caveat:* inherits S2's one unverified assembly step (the idle ledger);
everything else in the chain is [V] or proved above.

**Corollary S3' (the enemy squeeze, now branch-free).** Every packing of N+1
squares with eps > 0 satisfies
   U_x + U_y + V_x + V_y >= 2 eps + Sum_{w_i<1} m_i + Sum_{w_i>=1} (1-d_i)^2 ,
with m_i = d_i sigma_i (2 - d_i - w_i) >= 0 the exact T6 margins.
*Proof.* Markov/No-Repair: |Av| >= 1 - g; structure identity: 1 - g = s + 2 eps;
S2' bounds |Av|; the exact identity (1-w)^2 = (1-d)^2 - d sigma (2-d-w) converts
Sum_short (1-w)^2 = Sum_short (1-d)^2 - Sum_short m_i and
s - Sum_short (1-d)^2 = Sum_long (1-d)^2. Rearrange. QED

**Consequence for the campaign.** Session-2's dichotomy S3 read "(i) top-heavy
b0 >= eps + Gamma, OR (ii) the union bound". Branch (i) — the assignment's
TOP-HEAVY-AND-DEFICIT-RICH enemy, the only dodge of the capture-side squeeze —
is now DELETED: every enemy satisfies (ii). The coherence trichotomy's case
(III) (near-AP) no longer has the b0 escape at any tilt; at exactly AP it is
dead outright (G6-2). The single remaining target of Section 7C
("|Union of bbox-extreme-phase arcs| < 2 eps under G+V <= 2c") is unchanged in
form but is now THE ONLY gate: no arc-count, no cover structure, no b0
side-condition, and it must be defeated on both U- and V-arcs simultaneously.

---------------------------------------------------------------------------
## 4. The corrected beta-frontier of the extremal manifold

The assignment asked: verify "all extremals sit at beta = 1 exactly" — suspicion:
false for T12. CONFIRMED FALSE, and the correct invariant identified.

T12 arithmetic (k = 2b(b-1), b >= 2; machine-checked b = 2..5): columns of
widths k/(k+b) (k+b squares), k/(k+1-b) (k+1-b squares), and k-2 unit columns:
  widths: k/(k+b) + k/(k+1-b) + (k-2) = k   [uses exactly k = 2b(b-1)];
  count: (k+b) + (k+1-b) + k(k-2) = k^2 + 1;  sides: Sum d = k^2, eps = 0;
  **beta = (k+b) * b/(k+b) = b;   b0 = b0sec = (k+1-b)(k/(k+1-b) - 1) = b - 1.**
So beta = b -> infinity along the family: the "beta = 1 manifold" picture is
WRONG. The correct equality coordinate is the MDT bound:
   n - Sum d_i sec th_i = beta - b0sec = 1 - eps - rho ,
which equals **1 on every known extremal** (all are AP with Sum d = N: eps = 0,
rho = 0): U_k(a) (beta = 1, b0sec = 0), split cells (1, 0), k-grid+split (1, 0),
T12 (b, b-1), deficient row (1, 0). MDT is exactly tight on all of them: the
measured full-incidence sets {P = N+1} have measure k/(k+1) (U_k), 2/3 (T12
k=4), a-dependent (split cells), 0.50 (uneven U_3) — positive throughout, and
P - N never exceeds 1 anywhere (checked on 4001-point generic phase grids).
The deficient ROW attains tightness on its y-axis (x-axis max P - N = 0), i.e.
each extremal saturates MDT on at least one axis — the winding axis of F6.

Equality profile of MDT (read off the proof): P = N+1 at good x forces
(1) every one of the k lines exactly full (chords tile every line: Lemma G6-A
equality), (2) every deficit-chord square incident (p_i = 1), (3) every
surplus-chord square exactly single-incident, and (4) total signed deficit
exactly 1 on the incident multiset. On U_k this is the over-full column with
its k in-phase gap pieces; on T12 it is the b-over-full column paid by the
(b-1)-under-full column. This is the precise "capture-side rigidity near the
extremal manifold" shape that the No-Repair theorem demanded: a bijective
near-grid capture with one idle square, now derived rather than conjectured.

---------------------------------------------------------------------------
## 5. OC-FCMB equality classification (assignment task 1, first half)

hits(p) = N - C(p) = #(Lambda_p ∩ G) a.e. (G = the gap region; the N points of
Lambda_p in T split between squares and gap). Hence
   Sum_{m>=2} |{hits >= m}| = E[hits] - P(hits >= 1) = g - |pi(G)| ,
the FOLDING OVERLAP LOSS of the gap. Classification (exact, trivial once said):

   **hits in {0,1} a.e.  <=>  the fold pi restricted to G is a.e. injective
   <=> |pi(G)| = g.**

Among known extremals: tilings (g = 0: T12, grids) and split cells (gap confined
to one cell with piece dimensions <= 1: injective) are multiplicity-free and lie
in restricted-FCMB territory (|Av| <= s, attained with equality); the deficient
columns U_k fold k-to-1 (|pi(G)| = g/k) and carry multiplicity mass
g(k-1)/k = (k-1)/(k+1). OC-FCMB holds with equality on ALL of them (it is
equivalent to g + s >= 1, with equality iff extremal).

**The assignment's conjectured reverse OC-FCMB is FALSE.** "Each unit of
multiplicity mass requires one unit of one-sided deficit beyond the first,
hence multiplicity <= (b0 - eps)_+ + ..." dies on U_k itself: multiplicity
= (k-1)/(k+1) -> 1 while b0 = 0, eps = 0. Multiplicity is a DEFICIT-CHAIN
phenomenon (k in-phase deficit pieces stacked by the winding), not an oversize
phenomenon; no bound of the proposed shape can hold. The intended chain
"eps > 0 and b0 < eps => multiplicity = 0 => hits in {0,1} => g >= 1 - |Av|
>= 1 - s" is SUPERSEDED, not repaired: S2' shows that for eps > 0 no
multiplicity accounting and no b0 hypothesis are needed at all — the capture
side closes through the union bound instead of through |Av| <= s. The
displacement/chain-counting argument the assignment asked me to grind
("#chains >= c5 b0, budget 1 + b0 - eps, c5 > 1 caps b0") is subsumed by MDT
with the optimal constants: in the MDT ledger each unit of b0sec is charged
EXACTLY once (Fact 2), each unit of deficit credited AT MOST once (Fact 1),
and the ledger closes at 1 - eps - rho with no chain combinatorics; the
would-be "c5" is exactly 1 + 1/b0 on T12, confirming that no constant c5 > 1
exists and that the correct statement was always the signed global ledger.

---------------------------------------------------------------------------
## 6. Width-surplus localization and the taper ledger (the new leverage for
## bridges (I)/(II))

**Corollary G6-5.** Any packing of N+1 squares with eps > 0, a.e. x:
(a) [localization, unconditional] t = eps + tau = E[P] - N <= ∫_{Union B_i^x}
    (P - N)_+ dx : the ENTIRE width surplus is carried on the bad arcs (P <= N
    off them, by G6-3). Same in y. On an enemy t >= 2 eps (T4).
(b) [everywhere taper ledger] P(x) - N <= beta + T(x), where T(x) = # incidences
    in end regions (T = 0 at good x). Proof: split the chord ledger into middle
    and end incidences; end terms 1 - ch <= 1 each; middle terms: deficit-chord
    squares have <= 1 middle line at ANY x (the Fact-1 interval argument needs
    no goodness for middle lines), surplus-chord middle terms are <= 0, drop.
(c) [integer form] (P - N)_+ <= floor(beta) + T(x) pointwise. If beta < 1:
    (P-N)_+ <= T(x), hence
       eps + tau <= E[T ; P >= N+1] <= E[T] <= 2 Sum_i d_i sin th_i .
    In general: eps + tau <= floor(beta) U_x + 2 Sum d_i sin th_i.
(d) Reading: (i) a new single-axis linear tilt cap: any packing with beta < 2
    (e.g. b0 < 1 + eps + Gamma) has eps <= U_x + 2 Sum d sin th
    <= 4 Sum_i d_i sin th_i — same order as T4, completely different mechanism
    (chords, not inscribed squares), and robust to oversize sides; (ii) the
    clustering currency: on coherent whisper grids the T-incidences stack on
    K arcs, so (c) is a Theorem-W-type kill with the phase hypothesis moved
    into E[T ; P >= N+1]; (iii) consistency with the orchestrator's strategic
    fact sin th >= sigma(th) [checked]: the raw bound 2 Sum d sin th >= 2 tau
    >= 2 eps is never violated by mass alone — as predicted, only phase
    clustering can be attacked, and (a) now pins WHERE: the surplus lives on
    the B-arcs, so any anti-clustering statement need only be proved on
    Union B_i^x, not on the whole circle.

---------------------------------------------------------------------------
## 7. Task 2 (local rigidity at the manifold): status

Within AP, MDT gives far more than local rigidity: Sum d <= N globally, so the
extremal manifold is the set of GLOBAL maximizers; nothing local remains to
prove in the AP directions. In the tilt-normal directions the sharpest proved
statements are the linear caps: eps <= Sum d_i th_i (T4 [V]) and the new
single-axis eps <= floor(beta) U_x + 2 Sum d_i sin th_i (G6-5c); both are
first-order in tilt and match the numerically observed linear tilt penalty.
GAP (flagged): a true second-order statement (the numerics' 0.427t coefficient
at n = 10 is interface-driven, order k*t scaled, while G6-5 gives order N*t —
a factor k loose; closing it is exactly bridge (II)'s business, not a separate
manifold question).

---------------------------------------------------------------------------
## 8. Adversarial self-attack (what I tried to break)

1. Genericity: only countably many x mod 1 put a lattice line on a vertex or
   bbox endpoint — null. All statements a.e.
2. Fact 1 needs the incident lines to be in ONE interval of length < 1: at good
   x they are all in the middle region — checked adversarially with "fat"
   deficit-chord squares (d sec th = 0.9686, w = 1.1535 > 1, so p = 2 occurs on
   15.35% of phases): all p = 2 phases landed inside the square's own B-arcs;
   zero violations on the good set (grid 4001).
3. Fact 2 at the boundary: w = 1 exactly (th in {0, pi/4}, d sec th = 1): the
   coefficient vanishes; no constraint needed. d sec th = 1: term 0 either way.
4. AP oversize d >= 2: p_i >= 2, coefficient negative, we only used p_i >= 1 —
   safe (slack, not error).
5. 45 degrees: vacuous (good set empty), not wrong; matches every prior no-go.
6. Does the AP corollary secretly assume n = N+1? No — checked for general n
   (BKU c >= 0) and machine-checked ledger inequalities on packings with
   n != N+1 (5-square and 2-square configs in k = 3).
7. Tested for contradiction against [V] impossibility principles: first-moment
   neutrality (uses c_i, not p_i — no conflict), LP gap (P-integrality is not
   LP), multi-frame no-go (single frame used), pointwise-robust BKU eta_0 = 0
   (MDT makes no pointwise capture claim). No conflicts.
8. Tightness audit: every known extremal saturates MDT (Section 4) — a bound
   tight on the full extremal catalogue cannot be "too strong by accident".
9. Honest limitation: MDT's conclusion at eps > 0 is untestable on real packings
   (none exist if the conjecture is true); what is machine-checked is every
   LINK: capacity, chord law, Facts 1-2, the assembled inequality at all
   phases on 15 packings (AP, tilted, oversize, random-tilted; ~60k more grid
   shift evaluations), the mean E[P] = Sum w_i, and sharpness values.

## 9. Machine checks (g6_check.py, all assertions pass)

- C1 per-line capacity: 0 violations, all packings, 4001 generic phases each.
- C2 chord ledger P - N <= Sum(1 - ch) everywhere: 0 violations.
- C3 MDT on good sets (incl. per-square Facts 1-2, middle-region membership
  for surplus squares): 0 violations. Fat-square adversarial config: p = 2
  occurs (0.1535 of phases) but never at good x.
- C4 integer taper ledger (P-N)_+ <= floor(beta) + T, and T = 0 on good x:
  0 violations on all N+1 packings.
- C5 E[P] = Sum w_i to grid tolerance (max dev 5e-4).
- C6 sharpness: |{P = N+1}| = 0.6668 (U_2; exact 2/3), 0.7501 (U_3; 3/4),
  0.5001 (uneven U_3), 0.3702 (split a = 0.37; = a), 0.6668 (T12 k=4; 2/3).
- C7 beta table: U_k = 1, split = 1, T12(4,2) = 2 (and = b for b = 2..5 by
  exact arithmetic), deficient row = 1; beta - b0sec = 1 on all extremals.
- C8 sin th >= sigma(th) on [0, pi/2]: verified (trivially equiv. 1 - cos th >= 0).
- Reverse-OC-FCMB dead end: multiplicity mass (k-1)/(k+1) vs (b0 - eps)_+ = 0
  on U_k, k = 2,3,4.
