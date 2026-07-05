# P2 REPORT — anti-concentration / variance route: what is now proved, and where the ½ actually lives

Setting (fixed throughout): $T=[0,k]^2$, $N=k^2$, $M=N+1$ squares $S_i$, sides $d_i$, tilts $\theta_i\in[0,\pi/4]$, $\sigma_i:=\cos\theta_i+\sin\theta_i-1$, $w_i:=d_i(1+\sigma_i)$, $u_1(\theta):=1+\sigma$, $\sum d_i=N+\varepsilon$. For a shift $(x,y)\in[0,1)^2$: $p_i(x),q_i(y)$ line counts, $c_i$ lattice count, $L_i:=p_iq_i-c_i\ge0$ (corner-triangle points), $B_i:=(p_i-1)(q_i-1)\ge0$, $D:=\sum_i(L_i-B_i)_+$, $P:=\sum p_i$, $Q:=\sum q_i$, $S:=\varepsilon+\sum d_i\sigma_i$ (so $\mathbb E P=\mathbb E Q=N+S$). All statements at generic shifts (a.e.). Numerics: `/private/tmp/claude-501/-Users-kylekabasares-Desktop-erdos-106/6b0597a9-48bd-4e8c-a957-7fc4a05f26d8/scratchpad/p2/check.py` (all checks pass; cited below as [num]).

---

## 1. Verdicts on the assignment's embedded claims

| Claim (from the P2 strategy text) | Verdict |
|---|---|
| "$G+V\le 2c$ when $\varepsilon>1/2-c$; all sides within $\sqrt{2c}$ of the mean $\approx1$" | **CORRECT** (Route C Claims 1–2, re-verified; $\sum(d_i-1)^2\le 2V+2/k^2+O(1/k^2)\le 4c+O(1/k^2)$). |
| "$T\ge\varepsilon$" and hence tilt-heavy: $\sum d_i\sigma_i\ge T\ge 1/2-c$ | **CORRECT** (Route C Claim 5 chain re-checked; note $T=\sum d_i\sigma_i/(1+\sigma_i)\le\sum d_i\sigma_i$). |
| "$W-N=\varepsilon+\Theta(T)$, i.e. $\ge 1-2c$ in the enemy regime" | **CORRECT**: $W_{tot}-N=S=\varepsilon+\sum d_i\sigma_i\ge 2\varepsilon-c'\,$-ish $\ge 1-3c$. |
| "if $\max P=N{+}1$ then $\lvert A\rvert=\lvert\{P\ge N{+}1\}\rvert\ge 1/2$" | **CORRECT** (conditional): $P\le N{+}1$ and $\mathbb E P=N+S$ give $\lvert A\rvert\ge S\ge 1-3c$ — even stronger than claimed. |
| "level-selection: choose $j^*$ maximizing $j\lvert\{P\ge N{+}j\}\rvert$" | **CORRECT WITH FIXES**: done optimally it is *exactly* a first-moment identity (Lemma β below); by itself it reproduces the ½, it cannot beat it. The gain is the leftover term $\kappa$ (Theorem 1), which is genuinely new. |
| "two axis-parallel unit squares are disjoint only if $dx\ge1$ or $dy\ge1$; slope-$\tan\theta$ staircase wedge cost $\ge c\min(\theta,1)$ per unit length" | **CORRECT** — and now **proved** (Lemma α below), with explicit constant $\min(\tan\theta,1/5)/36$ per unit length. |
| "no near-unit axis-parallel square fits inside the $45°$ corner triangle" | **CORRECT**: largest axis-parallel square in the right-isosceles corner triangle with legs $d/\sqrt2\approx0.707$ has side $\approx0.354<1-\sqrt{2c}$. |
| "gentle giant grain has $\theta\gtrsim T/(2k^2)$, interface cost $\gtrsim\sqrt{\theta}$, hence $G\gtrsim1/k$; and it sits deep inside the capture regime $\sin2\theta\le1/(m-1)$" | **CORRECT** (arithmetic re-checked: mass $m^2\theta\ge1/2$, $m\le k$ ⇒ $\theta\ge1/(2k^2)$; capture margin factor $\sim m$). |
| "THE PINCER MAY CLOSE" (unconditional $c>0$) | **FLAWED as an argument / NOT YET CLOSED**: two genuine gaps remain (§6). All components that could be made rigorous are proved below; the missing pieces are precisely identified. |

---

## 2. Master Pointwise Inequality (MPI) — the correct primitive

**MPI.** *For every packing of $M=N+1$ squares in $T$ and a.e. shift $(x,y)$:*
$$D(x,y)\;\ge\;P(x)+Q(y)-2N-1 .$$

*Proof.* Per square, $c=pq-L=p+q-1+B-L\ge p+q-1-(L-B)_+$ (both cases $L\le B$, $L>B$; $B\ge0$ by $|p-q|\le1$). Sum over $i$ and use $\sum c_i\le|T\cap\Lambda|=N$: $N\ge P+Q-M-D$. $\square$

MPI **contains BKU**: axis-parallel ⇒ $D\equiv0$ ⇒ $\max P+\max Q\le 2N+1$; but integrality gives $\max P\ge\lceil N+\varepsilon\rceil\ge N+1$ and likewise $Q$ whenever $\varepsilon>0$ — contradiction, so $\varepsilon\le0$. So nothing is lost at the pointwise level; every loss in the literature chain comes from how MPI is averaged. Verified pointwise with zero violations on a genuine mixed 5-square packing in $[0,2]^2$ (500² shifts) [num §3].

---

## 3. THEOREM 1 (κ-sharpened robust BKU) — the strongest fully proved statement

Define per square the **margin**
$$m_i:=\begin{cases}0 & \theta_i=0\\ d_i\sigma_i(2-d_i-w_i)\ \ (\ge0) & w_i\le1\\ (1-d_i)^2\ \ (\ge0) & w_i>1,\ d_i\le u_1(\theta_i)\\ -\,d_i\sigma_i(d_i+w_i-2)\ \ (<0,\ |m_i|\le 4d_i(d_i-1)^2) & w_i>1,\ d_i>u_1(\theta_i)\end{cases}$$
and the **dip mass**
$$\kappa\;:=\;\int_0^1\!\!\int_0^1\big(2N+1-P(x)-Q(y)\big)_+\,dx\,dy\;\ge\;0 .$$

> **Theorem 1.** *Every packing of $N+1$ squares in $[0,k]^2$, arbitrary sizes and orientations, satisfies*
> $$\boxed{\;2\varepsilon\;\le\;1-\sum_i m_i-\kappa\;}$$

*Proof.* (i) $(X)_+=X+(-X)_+$ with $X=P+Q-2N-1$ gives, by MPI,
$\mathbb E[D]\ \ge\ \mathbb E[(P+Q-2N-1)_+]\ =\ (2S-1)+\kappa$.
(ii) Per-square upper bound $\mathbb E[(L_i-B_i)_+]\le 2d_i\sigma_i-m_i$: exact identities $d^2\sin2\theta=d\sigma(d+w)$ and $(w-1)^2-d\sigma(d+w-2)=(1-d)^2$ [num §0, $10^{-16}$]; for $w\le1$ use $\mathbb E[(L-B)_+]\le\mathbb E L=d^2\sin2\theta=2d\sigma-d\sigma(2-d-w)$; for $w>1$, $d\le u_1$ use the Coverage Lemma (Route A Claim 7, re-verified [num §1]) $\mathbb E[(L-B)_+]\le d^2\sin2\theta-(w-1)^2=2d\sigma-(1-d)^2$; for $d>u_1$ use $\mathbb E L$ again with $d+w-2=2\delta+\sigma(1+\delta)\le\delta(3+\delta)$, $\sigma<\delta:=d-1$, giving the debit branch. All four branches verified on a 700² shift grid at 8 $(d,\theta)$ pairs including three debit cases; residual violations $\le5\times10^{-4}$ = grid noise, pointwise $c\ge p+q-1-(L-B)_+$ violated nowhere [num §1].
(iii) Chain: $2(\varepsilon+\sum d_i\sigma_i)-1+\kappa\le\mathbb E D\le 2\sum d_i\sigma_i-\sum m_i$; the tilt mass **cancels identically**, leaving the box. $\square$

**Remarks.**
- Dropping $\kappa$ and the debit branch recovers Route A Claim 9 exactly; so Theorem 1 is a strict sharpening, now **unconditional in size** (no $d\le u_1$ or $d\ge3/2$ hypothesis; the debit branch costs only $4\sum d_i\delta_i^2=O(V)=O(c)$ in the near-critical regime).
- **Tightness.** On the BKU-extremal column tilings (Route C Claim 7): $\theta_i=0$, $\varepsilon=0$, $\sum m_i=0$, and $P+Q\le 2N+1$ pointwise with $\kappa=1$ **exactly** — verified at $k=4$: $\max P+\max Q=33=2N+1$, $\kappa=1.00025$ (grid) [num §2]. Theorem 1 is an equality there. It is the exact envelope of first-moment information.
- End-to-end check on a genuine mixed packing (3 unit squares + one $0.75$-square at $0.3$ rad + one $0.1$-square in $[0,2]^2$; disjointness and containment machine-verified): $\mathbb E D=0.321\ge 2S-1+\kappa=0.002$; $2\varepsilon=-0.30\le 1-\sum m-\kappa=0.016$ [num §3].

**Corollary 1 (new equivalent target).** $f(k^2+1)\le k+(1/2-c)/k$ for all packings **iff** every packing with $\varepsilon>1/2-c$ has
$$\kappa+\sum_i m_i\;\ge\;2c .$$
Since near-critically $\sum m_i=O(c)$ in absolute value, the whole problem is now the single anti-concentration statement: **the integer process $P(x)+Q(y)$, of mean $2N+2S\ge 2N+1-6c$, must dip to $\le 2N$ on shift-measure $\ge 2c$.** This is the precise, provable-looking form of the "variance route": no variance lower bound is needed, only *dip* mass.

**Corollary 2 (structure of the enemy).** If $\varepsilon>1/2-c$ (and $k^2\ge 10$, $c\le1/40$ say) then:
1. $G+V\le 2c$; all $d_i\in(1-\sqrt{2c}-k^{-2},\,1+\sqrt{2c})$;
2. $\sum d_i\sigma_i\ge T\ge\varepsilon>1/2-c$ (tilt-heavy), so $S\ge 1-2c$;
3. $\kappa<2c-\sum m_i\le 2c+O(c)$; hence for **every** integer $a$: $\;|\{P\le a\}|\cdot|\{Q\le 2N-a\}|\le\kappa<3c$;
4. (defect saturation) $\sum_i\big[(2d_i\sigma_i-m_i)-\mathbb E(L_i-B_i)_+\big]\le 1-2\varepsilon-\sum m_i-\kappa< 3c$: every tilted square must realize its corner-defect budget to within a total $O(c)$;
5. (arc rigidity) writing $p_i(x)=\lfloor w_i\rfloor+\mathbf 1_{F_i}(x)$ with $F_i$ an arc of length $\mathrm{frac}(w_i)$, statement 3 says the arc system $\{F_i\}$ covers the circle with essentially no multiplicity dips below level $N+1-\sum\lfloor w_i\rfloor$ except on measure $O(\sqrt c)$ — an efficient integer covering with overlap excess $S-1$. Any future rigidity/Fourier argument should attack exactly this object.

Proofs: 1–2 as in the verdict table; 3 from Theorem 1 plus $\{P\le a\}\times\{Q\le 2N-a\}\subseteq\{P+Q\le 2N\}$ and $(2N+1-P-Q)_+\ge1$ there; 4 by re-running the Theorem 1 chain keeping the slack; 5 immediate.

---

## 4. Lemma β (level-selection pigeonhole): resolved — it is the κ-envelope

**Lemma β (optimal level selection).** For $j,j'\ge1$ let $A_j=\{P\ge N+j\}$, $B_{j'}=\{Q\ge N+j'\}$. For every packing,
$$\int_{A_j\times B_{j'}} D \;\ge\;(j+j'-1)\,|A_j||B_{j'}|\qquad\text{for all } j,j'\ge1,$$
and the envelope of all level choices is exactly $\mathbb E[D]\ge\mathbb E[(P+Q-2N-1)_+]=2S-1+\kappa$, i.e. **Theorem 1**. In particular no selection rule $j^*=\arg\max j|A_j|$ can extract more than the mean-plus-κ; the strategy's hoped-for "$\varepsilon^2\le\Delta$ improvement" is unavailable from levels alone. *Proof:* MPI restricted to $A_j\times B_{j'}$; the envelope is the pointwise supremum of the affine minorants of $(\cdot)_+$. $\square$

**Absorption corollary (the usable form).** A packing is **impossible** if for some $j,j'\ge1$ the set
$$\{(x,y): D(x,y)\le j+j'-2\}\ \cap\ (A_j\times B_{j'})$$
has positive measure. Grain capture sets are exactly sets where the grain's $D$-contribution vanishes (NUM Claim 4); an axis-parallel sea contributes $D\equiv0$ pointwise. Hence:

**Proposition (single gentle grain + axis-parallel sea; conditional).** Suppose the packing is a rigid $m\times m$ grain at tilt $t$ with $\sin 2t\le 1/(m-1)$ plus axis-parallel squares, $\varepsilon>1/2-c$, and suppose $\operatorname{ess\,sup}P=N+1=\operatorname{ess\,sup}Q$. Then $|A_1|\ge S\ge1-2c$ and $|B_1|\ge1-2c$, so $|A_1\times B_1|\ge1-4c$; the grain's 2-D capture set $\mathcal C$ (where $D\equiv0$) satisfies $|\mathcal C|=\mu(t,m)>4c$ for $c<\mu/4$, hence $\mathcal C\cap(A_1\times B_1)\neq\emptyset$ — **contradiction**; no such packing exists. *Gap:* the hypothesis $\max P=N+1$ (equivalently: control of $j_{\max}:=\max P-N$; without it $|A_1|\ge S/j_{\max}$ only), and the restriction to one grain (the NUM Claim 5 two-grain counterexample shows disjoint capture sets are possible, though at side-deficit cost $\ge2.4\times$ the destroyed margin — far outside the near-critical budget, but this trade-off is only measured, not proved).

---

## 5. Lemma α (staircase interface lower bound): PROVED

> **Lemma α.** Let $\theta\in(0,\pi/4]$, $\tau=\tan\theta$, $\eta\le1/20$, $h=1/4$. Let $\mathcal Q$ be a finite family of axis-parallel squares with sides in $[1-\eta,1+\eta]$ and pairwise disjoint interiors, each contained in the half-plane $\{y\le \tau x+\beta\}$. Then for every $X\ge1$, the uncovered area of the strip $R=\{0\le x\le X,\ \tau x+\beta-h<y<\tau x+\beta\}$ satisfies
> $$\big|R\setminus\textstyle\bigcup\mathcal Q\big|\;\ge\;\frac{X}{36}\,\min\!\big(\tan\theta,\ \tfrac15\big).$$

*Proof.* (1) *Vertical gap function.* For $x\in[0,X]$ let $F(x)=\max\{t_S:\ S\in\mathcal Q$ spans $x\}$ ($-\infty$ if none), $t_S$ = top-edge height, $a_S$ = left edge. Any square containing a point of abscissa $x$ spans $x$, so the segment $\{x\}\times(F(x),\ell(x))$ is uncovered, where $\ell(x)=\tau x+\beta$; note $t_S\le\ell(a_S)\le\ell(x)$ for every spanning square (top-left corner must be under the line, $\ell$ increasing), so $F(x)\le\ell(x)$. Thus uncovered area $\ge\int_0^X\min(h,\,\ell(x)-F(x))\,dx$ (Fubini over disjoint vertical segments).

(2) *Crest uniqueness (disjointness quantization).* Two spanning squares at the same $x$ have vertically disjoint intervals of heights $\ge1-\eta$, so their top edges differ by $\ge1-\eta>h$. Hence at most **one** spanning square at $x$ has $t_S\in(\ell(x)-h,\ \ell(x)]$ — the *crest* square. If none: $\ell(x)-F(x)\ge h$. If crest $S_j$: $\ell(x)-F(x)=\ell(x)-t_j\ge\ell(x)-\ell(a_j)=\tau(x-a_j)$.

(3) *Per-crest cost.* Let $I_j=\{x: S_j$ is the crest$\}\subseteq[a_j,a_j+d_j]$. Since the integrand $\min(h,\tau(x-a_j))$ is nondecreasing, the bathtub bound gives $\int_{I_j}\min(h,\tau(x-a_j))\,dx\ge\int_0^{|I_j|}\min(h,\tau s)\,ds\ge \tfrac{\tau'}{2}|I_j|^2$ with $\tau':=\min(\tau,\ h/(1+\eta))\ge\min(\tau,1)/5$, using $|I_j|\le1+\eta$.

(4) *Crest count.* Every crest square lies in the parallelogram $\{-(1+\eta)\le x\le X+(1+\eta),\ \ell(x)-h-(1+\eta)\le y\le\ell(x)\}$ (checked corner by corner using $t_j\le\ell(a_j)$ and $t_j>\ell(x)-h$ for a crest abscissa), of area $(X+2(1+\eta))(h+1+\eta)$. Disjointness: $J\le (X+2.1)\cdot1.3/(1-\eta)^2\le1.44X+3.03$.

(5) *Assemble.* With $N_0$ = no-crest set: uncovered $\ge \frac{\tau'}{2}\sum_j|I_j|^2+h|N_0|\ge\frac{\tau'(X-|N_0|)^2}{2J}+h|N_0|$ (Cauchy–Schwarz). If $|N_0|\ge X/2$: $\ge hX/2=X/8\ge$ RHS. Else $\ge\frac{\tau'X^2/4}{2(1.44X+3.03)}\ge\frac{\tau'X}{36}$ for $X\ge1$. $\square$

Sharpness/sanity: the optimal unit staircase (step exactly 1, forced by disjointness since a step $(\delta,\tau\delta)$, $\delta<1$, $\tau<1$ overlaps) achieves uncovered per unit length $\min(\tau/2,\,h-h^2/2\tau)$: measured $0.050,\ 0.146,\ 0.219$ at $\tau=0.1,0.3,1.0$ vs proven bound $0.0028,\ 0.0056,\ 0.0056$ [num §4]. The proven constant is ~20× off optimal but **absolute and unconditional**, which is what the pincer needs. This settles Route B's GAP 1 **in the pure-interface (half-plane, axis-parallel-sea) case** — the first rigorous "interface cost $\ge c\min(\theta,1)$ per unit length" statement in the session.

A localized single-edge version also goes through with the same mechanism (any square covering just above a tilted edge's middle half must have its horizontal bottom edge above the edge-line at every abscissa it serves, forcing gap $\tau\cdot(\text{distance to its exit abscissa})$; crest count $\le3$ by horizontal disjointness of squares with bottoms within $h$), yielding uncovered $\ge c_2\min(\theta,1)$ per lone tilted square, **provided all covering neighbors are axis-parallel**. With mixed-orientation neighbors it fails as stated (a co-tilted neighbor hugs the edge at zero cost) — that is the grain phenomenon, and it is the honest boundary of what Lemma α proves.

---

## 6. Pincer status: what is proved, what is missing, and why no unconditional $c>0$ yet

**Proved pieces of the pincer** (all new or newly rigorous):
- (P1) Theorem 1 + Corollary 1: the target is exactly "dip mass $\kappa\ge 2c$" for tilt-heavy, gap-starved, side-uniform enemies (Corollary 2's profile).
- (P2) Lemma α: steep or moderate-tilt orientation interfaces against an axis-parallel environment cost gap linearly in $\theta$ per unit length, absolute constants — so any grain of tilt $\theta$ and boundary length $\Lambda$ facing axis-parallel squares pays $G\ge\Lambda\min(\theta,1/5)/36$, and with $G\le 2c$ a mass-$1/2$ carrier at tilt $\theta$ needs boundary $\lesssim c/\theta$ while its mass forces area $\gtrsim1/(2\theta)$, i.e. boundary $\gtrsim\sqrt{2/\theta}$: contradiction unless $\theta\lesssim c^2$ — steep grains are dead, **modulo (Gap A)**.
- (P3) The surviving gentle carriers ($\theta\lesssim c^2$, hence $m\gtrsim1/c$, diameter forcing $\theta\ge1/(2k^2)$) lie strictly inside the capture regime $\sin2\theta\le1/(m-1)$, and the absorption corollary + Proposition kill the single-grain case under the stated hypotheses.

**Gap A (mixed-orientation interface / grain decomposition).** Lemma α requires the covering family at the interface to be axis-parallel. To charge a general packing one must decompose the tilted squares into "grains" (contact/proximity components of nearly-equal orientation) and show every grain's outer boundary faces either the axis-parallel sea (Lemma α applies, possibly after rotating coordinates to the grain's frame — Lemma α is frame-symmetric, so a $\theta$-grain against a $\theta'$-sea pays in the mismatch $|\theta-\theta'|$) or another grain with different orientation (pay in that mismatch). The missing piece is a rigorous decomposition lemma with a triangle-inequality bookkeeping of mismatch angles along a path from any tilt-carrying square to the container walls (whose frame is $0$, and which dominate: $T\ge1/2-c$ of tilt mass cannot all hide, since total orientation must return to $0$ at all four walls — Route B's Wall Lemma T2 is the proved base case). This is a genuinely finite, combinatorial-geometric task, but it is not done.

**Gap B (multi-grain capture positioning / $j_{\max}$ anti-concentration).** The absorption route needs $(A_j\times B_{j'})\cap\{D\le j+j'-2\}\neq\emptyset$. Proved when $\max P=N+1$ (then $|A_1|\ge1-2c$). Unproved when $P$ overshoots ($j_{\max}\ge2$), where $|A_1|\ge S/j_{\max}$ only, and when several gentle grains have disjoint capture sets. Evidence (not proof) that near-criticality forbids the escape: in NUM Claim 5, destroying one unit of counting margin cost side-deficit $\ge2.4$ — two conflicting grains cost $\gg 2c$; a proved "destruction $\le0.5\times$ payment ⇒ contradiction" inequality (NUM's conjectured lemma $\max_\Lambda\sum c_i\ge2\sum d_i-N$) would close Gap B entirely and, per NUM's report, the full conjecture.

**Honest bottom line.** The unconditional bound $f(k^2+1)\le k+(1/2-c)/k$ is **not proved**. The session's net gain from P2:
1. **Theorem 1** ($2\varepsilon\le1-\sum m_i-\kappa$): unconditional, size- and tilt-free, exactly tight on all known BKU-extremal tilings, strictly sharper than Route A Claim 9, and it converts the ½-problem into the single clean statement $\kappa+\sum m_i\ge2c$ (Corollary 1) with the enemy's structure pinned down (Corollary 2, arc rigidity).
2. **Lemma α proved** with explicit absolute constants — Route B's GAP 1 closed in the pure-interface case; steep-grain carriers excluded modulo the decomposition bookkeeping (Gap A).
3. **Lemma β resolved**: level selection is exactly the $\kappa$-envelope (no hidden $\varepsilon^2\le\Delta$ gain exists in levels alone); its usable residue is the absorption corollary and the conditional single-grain Proposition.
4. Recommended order of attack for the next phase: (i) Gap B via the "destruction ≤ payment" counting lemma restricted to near-critical packings (use Corollary 2.4's defect saturation as the new hypothesis the two-grain counterexample violates); (ii) Gap A via a grain-decomposition + mismatch-triangle-inequality lemma seeded by Wall Lemma T2 and Lemma α.

Files: verification script and outputs at `/private/tmp/claude-501/-Users-kylekabasares-Desktop-erdos-106/6b0597a9-48bd-4e8c-a957-7fc4a05f26d8/scratchpad/p2/check.py`.