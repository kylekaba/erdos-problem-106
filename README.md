# Erdős Problem #106 — An AI-Assisted Attack on the Rotated Square-Packing Conjecture

> **Update (Session 3, July 2026):** a third session ("the final assault") added, all
> adversarially verified: the **Marginal Displacement Theorem** (a signed chord ledger
> giving the complete axis-parallel theorem in five lines at arbitrary sizes, and deleting
> the "top-heavy" escape route for counterexamples), the **Columnar Kill** (the conjecture
> holds for every columnar packing, tilts strictly penalized), **the fall of the 45°
> fortress** (pure-45° packings satisfy $\sum d \le N$ for all $k \ge 10$; every common
> orientation — including irrational angles — is closed for $k \ge 10/\sin 2\theta$), an
> incoherence-charging theorem, a 14-constraint unconditional structure theorem for
> counterexamples, and the reduction of the sub-Cauchy–Schwarz program to **one remaining
> lemma**. See `ERDOS_106_REPORT.md` §7D and section 3½ below.

**Problem** ([erdosproblems.com/106](https://www.erdosproblems.com/106)). Let $f(n)$ be the
maximum of $\sum_i s_i$ over packings of $n$ squares (side lengths $s_i$, **arbitrary
orientations**, pairwise disjoint interiors) inside the unit square. Erdős conjectured
(~1932):

$$f(k^2+1) = k \quad \text{for all } k \ge 1.$$

The conjecture is **open**, and remains open after this project. The axis-parallel variant
$g(n)$ was completely solved by Baek–Koizumi–Ueoro
([arXiv:2411.07274](https://arxiv.org/abs/2411.07274)); before this project **no upper
bound beyond Cauchy–Schwarz ($f(k^2+1) \le \sqrt{k^2+1}$) had ever been published for the
rotated problem** — even $f(3) = 3/2$ is open. The only known rotated exact values are
$f(2)=1$ (Erdős / Beck–Bleicher), $f(5)=2$ (D. J. Newman — proof lost), and $f(k^2)=k$.

## Provenance and epistemic status — read this first

This repository is the output of two working sessions of a **multi-agent AI system**
(Claude, Anthropic) directed at this problem: roughly 40 specialised agent runs
(literature recovery, independent proof attacks along separate routes, numerical
experiments, and dedicated adversarial verification passes), orchestrated across two
sessions in July 2026.

- Results marked **[V]** were proved by one agent and then independently re-derived,
  adversarially attacked, and numerically stress-tested by separate verifier agents.
- Results marked **[P]** have complete proofs and machine checks but no independent
  verification pass yet.
- Results marked **[N]** are numerical evidence only.
- **Nothing here has been peer-reviewed by human mathematicians.** The repository owner
  is verifying the material; until then, treat every claim as a carefully-argued
  candidate theorem, not established mathematics. Complete proofs, constants, and
  falsification tests are included precisely so that humans can check them.

## What was accomplished

### 1. First upper-bound theorems beyond Cauchy–Schwarz for the rotated problem

Scaled setting throughout: $T=[0,k]^2$, $N=k^2$, $n=N+1$ squares, sides $d_i$, folded
tilts $\theta_i$, widths $w_i = d_i(\cos\theta_i+\sin\theta_i)$; excess
$\varepsilon = \sum d_i - N$; gap $g = N - \sum d_i^2$; deficit mass $s = \sum(1-d_i)^2$.

- **T4, rotation pays linearly [V]:** $\varepsilon \le \sum_i d_i\theta_i$ — every tilted
  square contains its concentric axis-parallel square of side $d/(\cos\theta+\sin\theta)$;
  apply the BKU theorem to the inscribed family. Any counterexample to Erdős must carry
  total tilt mass at least its excess.
- **T2, common orientation [V]:** any packing of $k^2+1$ squares sharing one arbitrary
  orientation has $\sum d_i \le N + \tfrac12$.
- **T3, Pythagorean frames [V]:** at a common Pythagorean angle ($\cos\theta = a/c$,
  $c \mid k$) the exact bound $\sum d_i \le N$ holds (BKU transfers verbatim through a
  rotated exact-budget lattice).
- **T5, small aggregate tilt [V]:** if $\Delta = \sum d_i^2\sin 2\theta_i < 1$ then
  $\sum w_i \le N + \sqrt\Delta\,(N+1)/(1-\sqrt\Delta)$ — the exact constant $k$ survives
  small total tilt.
- **T6, the master $\kappa$-inequality [P]:** $2\varepsilon \le 1 - \sum_i m_i - \kappa$
  with explicit per-square margins $m_i$ and dip mass
  $\kappa = \mathbb E[(2N+1-P-Q)_+]$; exactly tight on all known extremal families.
- **Theorem K [P, final push]:** the exact anti-concentration law
  $\kappa \ge (1-t)_+^2$, $t = \sum w_i - N$, from a new elementary lemma
  ($\mathbb E[(\varphi+\psi-1)_+] \ge \mu_1\mu_2$ for independent integer variables with
  means in $[0,1]$) — tight on every known extremal configuration.
- **Theorem C″, correlated defects [V]:** every packing satisfies
  $\sum_i(1-w_i)_+ + \max(U_x,U_y) \ge 1$, where $U_x, U_y$ are measures of **unions**
  of per-square bad-phase arcs — coherent families pay per distinct phase, not per
  square. **Theorem W [V]** builds on it to kill the coherent "whisper-tilt" enemy under
  phase clustering.
- **Lemma α′ / α′-edge [V]:** interface cost lemmas — near-unit squares of tilt spread
  $\varphi_0$ below a slope-$\tau$ line leave uncovered area
  $\ge \tfrac{X}{60}\min(\tau-\tan\varphi_0, \tfrac13)$ per length $X$; gradient
  smoothing of an orientation interface cannot reduce the total bill.
- **Lemma A″ / Theorem S2 / dichotomy S3 [P, final push]:** a tilted square's vertical
  chord equals $d\sec\theta$ *identically* on the middle of its bounding-box range; this
  revives over-full-line pigeonholes for tilted packings under the chord-deficit
  hypothesis $\beta = \sum(1-d_i\sec\theta_i)_+ < 1$, giving a tilted capture-measure
  bound and an enemy dichotomy (top-heavy sides or scattered phases).

### 2. The complete $f(2)=1$, recovered classics, and structure theory

- A complete, self-contained proof of $f(2)=1$ with a new rigidity statement (equality
  forces axis-parallel strip configurations) **[V]** — plus recovery of the classical
  published proof (Beck–Bleicher, *Acta Math. Acad. Sci. Hungar.* 22 (1971/72) 283–303).
- Documentation that **Newman's proof of $f(5)=2$ is definitively lost** (its only trace
  is "personal communication" in Erdős–Graham 1975).
- Structure theory of near-extremal packings **[V]**: buried-contact crystallization law,
  sector lemma, tiling rigidity (every square tiling of a rectangle is axis-parallel,
  two independent full proofs), wall anchoring, exclusion of coherently tilted packings.
- Exact single-square counting laws **[V]** explaining *why* the problem is hard: the
  tilted counting problem is **exactly critical in expectation at every tilt angle** —
  per-square projection surplus minus expected counting defect equals $(1-d)^2$,
  vanishing precisely at the extremal size.

### 3. A conjecture proposed, then refuted — and what the refutation taught

Session 1 proposed the **FCMB** (Full-Capture Measure Bound): $|Av| \le s$, where
$Av$ is the set of lattice shifts capturing the full budget $N$. It implies the Erdős
conjecture in three lines, was proved at $k=1$, and survived that session's adversarial
search. **Session 2 refuted it** (four independent constructions): the *deficient
column* — $k+1$ squares of side $\tfrac{k}{k+1}$ stacked in one strip plus $k(k-1)$ unit
squares — is a valid **extremal** packing with $|Av| = \tfrac{k}{k+1} \gg s =
\tfrac{1}{k+1}$. The wreckage yielded:

- a previously uncatalogued **$k$-dimensional manifold of extremal packings** with
  $g+s=1$ identically;
- the exact identity FCMB truncated: the conjecture is *equivalent* to
  $|Av| \le s + \sum_{m\ge2}|\{C \le N-m\}|$ (the hit-multiplicity credit);
- **restricted FCMB-AP [V]**: for axis-parallel packings with $d_i \le 1$ and
  $\sum d_i > N$, $|Av| \le s$ — whose corollary is a **new, self-contained, half-page
  measure-theoretic proof of the BKU theorem** (sides $\le 1$);
- a **No-Repair theorem [V]**: every "gap-mass" measure route (second moments,
  autocorrelation, sumset/support bounds, any bound $|Av| \le F(g,s)$) is structurally
  incapable of closing the conjecture.

### 3½. Session 3: the final assault (all verified by fresh adversarial passes)

- **Theorem MDT (Marginal Displacement).** For a.e. "good" phase,
  $P(x)-N \le n-\sum_i d_i\sec\theta_i$ — a signed per-line chord ledger built on the new
  exact fact that a tilted square's vertical chord equals $d\sec\theta$ *identically* on
  the middle of its bounding-box range. Consequences: the complete axis-parallel theorem
  ($\sum d_i \le N+c$, arbitrary sizes, all integer $c>-k$, no Praton reduction) in five
  lines; **S3′** — every counterexample *unconditionally* owes the union requirement
  $U_x+U_y+V_x+V_y \ge 2\varepsilon+\text{margins}$ (the top-heavy branch is deleted).
- **Theorem SD (Columnar Kill).** Any packing that splits into $\le k$ narrow vertical
  classes satisfies $\sum d_i \le \sum d_i\sec\theta_i \le N$: the conjecture for all
  columnar packings, exactly tight on the entire known extremal catalogue.
- **The 45° regime closed at large $k$.** Theorem 45-A: $\varepsilon \le \tfrac14 +
  \tfrac1{4(N+1)}$ at 45°, all $k$. Theorem 45-B: pure-45° packings satisfy
  $\sum d_i \le N$ for all $k\ge10$ (open residue $k\in[2,9]$). Theorem CO: every common
  orientation is closed for $k \ge 10/\sin2\theta$. Plus an exact diamond-container
  discrepancy formula (verified on 56,000/56,000 shifts) with a Raikov-sumset regime
  analysis.
- **Theorem I:** total orientation incoherence is charged to gap area with explicit
  absolute constants ($G \ge I/5040$; sharper mid-strip forms).
- **Theorem U:** fourteen simultaneous verified constraints every near-counterexample
  must satisfy.
- **The one-lemma reduction.** The Conditional Master Theorem: modulo a single stated
  lemma (L2: a union-measure phase bound for gap-starved packings),
  $f(k^2+1) \le k+(1/2-c_0)/k$ for **every** $k$. L2's proof program is scaffolded with
  one case fully proved and two finite bridges (X1 exposure bookkeeping, X2 dislocation
  cost) remaining.

### 4. Impossibility principles (what a correct proof cannot look like)

Proved obstructions: LP/duality gap (fractional packings reach the Cauchy–Schwarz value);
single-lattice and multi-frame counting are exactly at break-even for misaligned squares;
pointwise-robust BKU fails for every positive tilt; pairwise/local charging schemes are
impossible ($45°$ diamond chains have zero mutual standoff); $L^\infty$ near-tiling
rigidity is false (explicit column tilings); gap-mass measure routes (No-Repair);
$\kappa$-from-phase-spread (equidistributed phases *minimize* the dip mass; the naive
"circle Littlewood–Offord" is false).

### 5. Numerical evidence [N]

Certified global optimization at $n = 2, 5, 10, 17$: no rotated configuration ever beat
$k$; optima always collapse to axis-parallel; measured tilt penalty is linear; the
counting/capture machinery was stress-tested on every adversarial family found.

## Repository map

| Path | Contents |
|---|---|
| `ERDOS_106_REPORT.md` | **The consolidated report** — all definitions, theorems, proofs or proof-locations, verification status tags, impossibility principles, and the architecture for a future proof (§7, §7A–§7C). Start here. |
| `NOTES.md` | The orchestrator's running mathematical notes across both sessions. |
| `agent-reports/` | Full per-agent research reports: session-1 attacks (`report_*.md`), session-1 verification (`p2_*.md`), FCMB genesis (`p1_capture_FCMB.md`), session-2 attacks (`s2_F*.md`), session-2 verification (`sv_V*.md`), final push (`fp_P_*.md`). |
| `agent-reports/session2-derivations/` | Complete long-form derivations behind the session-2 and final-push theorems. |
| `code/session1/` | Numerics: counterexample search (`numce/`), marginal-constant measurements (`numlem/`), verification scripts. |
| `code/session2/` | FCMB falsification and refutation certificates (`F2/`, `F4/`, `F6/`), restricted-FCMB machinery (`F1/`), interface/counting lemma checks (`F5/`), anti-concentration and squeeze checks (`RIGIDITY/`, `capture_squeeze/`), independent verifier scripts (`verify_s2/`). |

## Future directions

Listed in order of leverage; see `ERDOS_106_REPORT.md` §7–§7D for full context. (Items
resolved during session 3: the S2 ledger is now verified; the top-heavy/capture-squeeze
branch is closed by MDT; the 45° regime is closed for $k\ge10$.)

1. **Lemma L2 — the last gate.** Prove: every packing with $\varepsilon > 1/2 - c_2$ has
   $U_x+U_y+V_x+V_y < 1-2c_2$ (a pure union-measure statement about defect-phase arcs).
   By the verified Conditional Master Theorem this alone yields the **first unconditional
   bound $f(k^2+1) \le k+(1/2-c_0)/k$ below Cauchy–Schwarz**. The scaffolded program:
   Case II (clustered whisper) is proved; bridge X1 (steep-exposure bookkeeping via
   α′-edge, Theorem I, and the Wall lemmas) is finite geometry; bridge X2 (whisper
   dislocation cost — the accumulation obstruction) is the one deep gap. MDT's
   localization ($t \le \int_{\cup B^x}(P-N)_+$: the entire width surplus lives on the
   bad arcs) pins where the proof must work.
2. **Close $k \in [2,9]$ at 45°** (a second-level refinement of Theorem 45-B's
   window/δ scheme; $k=9$ peaks at $0.90$ of the needed gap) and port Theorem CO into
   the trichotomy as the quantitative (I)→gap bridge at walls.
3. **The wedge displacement lemma** (G4's proposal): convert the $\Omega(k)$ forced
   wedges of any non-columnar enemy into a positional phase-scatter lower bound — the
   spatial replacement for mod-1 rigidity, feeding L2.
4. **By Singh's reduction** ([arXiv:2601.22163](https://arxiv.org/abs/2601.22163)),
   $k\,(f(k^2+1)-k)$ is non-decreasing, so the full conjecture is equivalent to
   $f(k^2+1) \le k + o(1/k)$ along any subsequence — the asymptotic version of item 1's
   program ($c_0 \to 1/2$) is the road to the complete conjecture; the honest caveat is
   that the current architecture's constants cap $c_0$ at $\sim 2\cdot10^{-4}$, so the
   full conjecture likely needs a qualitatively sharper interface tax.
5. **Independent human verification of everything in this repository** — especially the
   [V]-tagged theorems, which are candidates for standalone publication if they hold:
   MDT and its five-line axis-parallel theorem, the Columnar Kill, Theorems 45-A/45-B/CO,
   T2–T5, Theorem C″, Lemma α′, Theorem I, Theorem U, the restricted-FCMB proof of BKU,
   and the $f(2)=1$ rigidity proof.

## Key references

- P. Erdős, R. L. Graham, *On packing squares with equal squares*, JCTA A **19** (1975) 119–123.
- A. Beck, M. N. Bleicher, *Packing convex sets into a similar set*, Acta Math. Acad. Sci. Hungar. **22** (1971/72) 283–303.
- J. Baek, J. Koizumi, T. Ueoro, *A note on the Erdős conjecture about square packing*, [arXiv:2411.07274](https://arxiv.org/abs/2411.07274).
- A. Raj Singh, *On a square packing conjecture of Erdős*, [arXiv:2601.22163](https://arxiv.org/abs/2601.22163).
- I. Praton, *Packing squares in a square*, Math. Mag. **81** (2008) 358–361.
- K. F. Roth, R. C. Vaughan, *Inefficiency in packing squares with unit squares*, JCTA A **24** (1978) 170–186.
- T. F. Bloom, *Erdős Problem #106*, [erdosproblems.com/106](https://www.erdosproblems.com/106).

---

*Generated with [Claude Code](https://claude.com/claude-code) (Claude Fable 5, Anthropic), July 2026, directed by Kyle Kabasares. All mathematical content pending human verification.*
