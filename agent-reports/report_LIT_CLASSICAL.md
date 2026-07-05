# Deep dig: Erdős #106 upper-bound technology for TILTED squares — findings, recovered proofs, and full reconstructions

---

## 0. Executive summary

- **f(2) = 1 (rotations allowed): RECOVERED.** The original Erdős article (a 1930s Hungarian high-school journal item) remains unlocated and uncited even by Erdős himself, but a **complete published proof allowing rotations exists in the classical literature**: A. Beck and M. N. Bleicher, *Packing convex sets into a similar set*, Acta Math. Acad. Sci. Hungar. **22** (1971/72), 283–303 — free scan recovered (see §2.3). Their method (separating line → renormalize each square to a "corner position" → compare diameters along the diagonal) is exactly the "corner regions" technique. I give a fully self-contained, rigorous modern proof below (§3), whose key lemma is a clean analytic version of Beck–Bleicher's Lemma 14.
- **f(5) = 2 (Newman): DEFINITIVELY LOST.** Erdős–Graham 1975 (full text recovered, §4) cites it as "[2] D. J. Newman, *personal communication*." No written account survives anywhere I could find. Amusingly, Beck–Bleicher's footnote says they *learned the two-squares problem itself from D. J. Newman and Morris Newman* — Newman was demonstrably engaged with this problem circle, but his k=2 proof was never written down. §4.3 gives a reconstruction analysis of what his proof had to overcome.
- **Folklore lemma (tilings of a rectangle by squares are axis-parallel): PROVED IN FULL** (§5), by a lexicographic-corner induction over rectilinear regions; plus the corollary that the equality case of f(k²)=k is exactly the k×k grid — a genuine (if soft) "stability anchor" that is rotation-proof.
- **Stability literature (§6):** the only quantitative tilted-square upper-bound technology in print is Roth–Vaughan 1978 (waste ≥ 10⁻¹⁰⁰·√(s‖s‖) for packing unit squares in an s×s square; "good squares" = inclination ≤ 10⁻¹⁰, tilt-penalty accounting). Also: Beck–Bleicher's "tight figure" characterization; a warning that the square lattice packing is **not uniformly stable**, so soft stability cannot be expected; Montgomery's improvement of the Erdős–Graham construction; the 2025 arXiv refinement ("only needs good squares").
- **Current state of #106** (from erdosproblems.com #106 and arXiv): Baek–Koizumi–Ueoro (arXiv:2411.07274) settled the **axis-parallel** case completely: g(k²+2c+1)=k+c/k. Praton (2005, 2008) reduced the general conjecture to f(k²+1)=k; Raj Singh (arXiv:2601.22163) reduced "all k" to "infinitely many k". **With rotations, the known values are exactly f(1)=1, f(2)=1, f(k²)=k, f(5)=2 — even f(3)=3/2 is open.**

---

## 1. The problem and what is known (verified statements)

Let f(n) be the maximum of Σᵢ aᵢ over collections of n squares with side lengths aᵢ, arbitrary orientation, contained in the closed unit square U with pairwise disjoint interiors.

- **Trivial with rotations:** f(k²) = k. Lower bound: the grid. Upper bound: Cauchy–Schwarz, Σaᵢ ≤ √(k²·Σaᵢ²) ≤ k, since Σaᵢ² = Σ area ≤ area(U) = 1. *(Note: this is rotation-proof — one of the very few tools that is.)* Hence also f(n) ≤ √n for all n.
- **Erdős (~1932):** f(2) = 1. "As far as we know, this was first published by P. Erdős and appeared as a problem in a mathematical paper for high school students in Hungary" (Erdős–Graham 1975, p. 119, verbatim). No bibliographic citation is given anywhere — not by Erdős–Graham 1975, not by Erdős's 1994 problem paper (full text checked), not by erdosproblems.com. The original is genuinely unlocated; it is not in the Rényi digital archive of Erdős's papers (which begins with his 1929 KöMaL-adjacent article).
- **Newman:** f(5) = 2. Erdős–Graham 1975, p. 120: "D. J. Newman [2] proved the conjecture for k = 2 but the general case is still unsettled." Reference [2] reads, in full: "D. J. NEWMAN, personal communication."
- **Conjecture (Erdős, >60 years before 1994):** f(k²+1) = k. Lower bound easy (split one grid cell into two half-size squares). Halász (JCTA A 36? — cited as *Packing a convex domain with similar convex domains*, JCTA A (1984) 85–90): f(k²+2c+1) ≥ k + c/k and f(k²+2c) ≥ k + c/(k+1). Erdős–Soifer (Geombinatorics 4(4) (1995) 110–114) and Campbell–Staton (Amer. Math. Monthly 112 (2005) 165–167) conjecture f(k²+2c+1) = k + c/k for −k<c<k.
- **Praton** (Math. Mag. 81 (2008) 358–361; also arXiv:math/0504341): the Erdős–Soifer/Campbell–Staton conjecture is equivalent to f(k²+1)=k for all k.
- **Baek–Koizumi–Ueoro** (arXiv:2411.07274): the axis-parallel variant g satisfies g(k²+2c+1) = k+c/k for all −k<c<k (two proofs: a randomized sweep by k equally spaced parallel lines, and a lattice-point counting argument after scaling by k). **Neither proof survives rotations**: both rely on a line/lattice-line meeting an axis-parallel square of side a in a trace of length exactly a and on integrality of crossing counts; a tilted square's chord can be as long as a√2.
- **Raj Singh** (arXiv:2601.22163; see also arXiv:2506.23284): k(f(k²+1)−k) is non-decreasing in k; hence f(k²+1)=k for all k ⟺ for infinitely many k ⟺ Σₖ (f(k²+1)−k) < ∞. (Construction-based; valid for the rotational f.)

**With rotations the complete list of known exact values is: f(1)=f(2)=1, f(4)=2 (=f(2²)), f(5)=2, f(k²)=k. f(3) (conjecturally 3/2) is open.** The only upper-bound technology ever to handle tilted squares in this problem is the f(2) technique below and the Cauchy–Schwarz area bound.

---

## 2. The hunt: what was found where

### 2.1 erdosproblems.com #106 (T. F. Bloom) — full page text recovered
Confirms the history exactly as above; cites [ErGr75b], [Er94b], [Er95], [Ha84], [ErSo95], [CaSt05], [Pr08], [BKU24], [Ra26]. States "Erdős proved that f(2)=1 in an early mathematical paper for high school students in Hungary. Newman proved (in personal communication to Erdős) that f(5)=2." No proof sketch of either. Forum has nothing further (checked).

### 2.2 Erdős, *Some problems in number theory, combinatorics and combinatorial geometry*, Math. Pannonica 5/2 (1994) 261–269 — **full scanned PDF recovered and read** (`https://mathematica-pannonica.ttk.pte.hu/articles/mp05-2/mp05-2-261-269.pdf`), §3.3:
> "Inscribe n non-overlapping squares into a unit square. Denote by a₁,…,aₙ the sides of these squares. Let f(n) = max Σ aᵢ. It is easy to see that f(k²)=k and I conjectured that f(k²+1)=k. I conjectured (1) more than 60 years ago. Perhaps the proof (or disproof) of (1) will not be difficult."

No mention of Newman or of the f(2) proof there.

### 2.3 Erdős–Graham, *On packing squares with equal squares*, JCTA A 19 (1975) 119–123 — **full text recovered** (Ron Graham's publication archive, `https://mathweb.ucsd.edu/~ronspubs/75_06_squares.pdf`). Key verbatim passage (p. 119–120):

> "If two nonoverlapping squares are inscribed in a unit square, then the sum of their circumferences is at most 4, the circumference of the unit square. As far as we know, this was first published by P. Erdős and appeared as a problem in a mathematical paper for high school students in Hungary. Beck and Bleicher [1] proved that if a closed convex curve 𝒞 has the property that for every two inscribed nonoverlapping similar curves 𝒞₁ and 𝒞₂, the sum of the circumferences of 𝒞₁ and 𝒞₂ is not greater than the circumference of 𝒞, then 𝒞 is either a regular polygon or a curve of constant width. … Erdős conjectured 40 years ago that if we inscribe k²+1 squares into a unit square, the total circumference remains at most 4k. For k=1, this is true as we have just stated. D. J. Newman [2] proved the conjecture for k=2 but the general case is still unsettled."

### 2.4 Beck–Bleicher, *Packing convex sets into a similar set*, Acta Math. Acad. Sci. Hungar. 22 (1971/72) 283–303 — **full scanned text recovered** (REAL-J repository of the Hungarian Academy: item `https://real-j.mtak.hu/7419/1/MTA_ActaMathHung_22.pdf`, printed pp. 283–303). This is **the published classical proof of f(2)=1 with rotations** (the square is a regular polygon, and their similarity classes include rotations and reflections). Verbatim from the introduction:

> "This paper deals with a subject which arises out of a famous problem.¹ The problem, which is an old chestnut and makes the rounds every so often, goes as follows: Let squares of perimeter a and b be enclosed in a square of perimeter c so that their interiors do not overlap. Then one must show that a+b ≤ c. … We shall prove, inter alia, that a figure is tight exactly if it is either a regular polygon or a curve of constant width."
>
> Footnote 1: "The authors first heard of this problem from Newman. The first author from **D. J. Newman** and the second from **Morris Newman** when he sent this problem in to the Mathematical Talent Search at the University of Wisconsin."

Their definitions: K̄ = sup π(K₁)+π(K₂) over packings of two similar copies into K₀ ∼ K, normalized π(K₀)=1; K is *tight* if K̄ = 1. Their Theorem 18: **every regular polygon is tight** (this specializes to f(2)=1 for the square). Their Theorem 12 (via Barbier): any two constant-width curves packed in a constant-width curve satisfy π(K₁)+π(K₂) ≤ π(K₀). Lemma 1: 1 ≤ K̄ ≤ √2 for every convex K (upper bound by the area/Cauchy–Schwarz argument!), with K̄=√2 iff K is an isosceles right triangle or a parallelogram with side ratio √2.

**Their proof skeleton for the square (Theorem 18 + Lemmas 14, 17):** given K₁, K₂ packed in K₀, take a line ℓ separating K₁ from K₂; take the two support lines ℓ₁ ∥ ℓ ∥ ℓ₂ of K₀ touching it at vertices P₁, P₂ (for a square, P₁P₂ is a diagonal when ℓ is not parallel to a side). Replace K₁ by an equal-size regular n-gon K′ in "standard position" with a vertex at P₁ (for the square: the axis-parallel corner square). **Lemma 14** (their key lemma): if the triangle formed by the two sides of K₀ at P₁ (extended) and the line ℓ contains *some* regular n-gon of side a, then the standard-position n-gon of side a at P₁ also fits, still on P₁'s side of ℓ. Then K′ and K″ occupy disjoint parts of the diagonal P₁P₂, whence d(K′)+d(K″) ≤ d(K₀), i.e. (for squares) √2·a + √2·b ≤ √2, i.e. **a + b ≤ 1**. Their proof of Lemma 14 for even n (Lemma 17) is synthetic (rotate the standard n-gon about its center, track the displacement vector needed to re-inscribe it in the corner angle, and show the far vertex moves inward). Section §3 below replaces this synthetic step with a short, fully rigorous computation.

### 2.5 Sources checked for a surviving account of Newman's f(5)=2: **all negative**
- Erdős–Graham 1975: "personal communication", zero detail (§2.3).
- Erdős, Math. Pannonica 1994: conjecture only.
- Erdős's other problem collections (e.g. *Combinatorial problems in geometry*, Math. Chronicle 12 (1983), full text checked): the squares problem does not appear with detail.
- erdosproblems.com #106 + forum: "personal communication to Erdős", nothing more.
- Campbell–Staton (Monthly 2005), Praton (2005, 2008), BKU24, Raj Singh 2026, and the 2025–26 arXiv wave: none reproduce or even sketch it; BKU24 explicitly does not discuss the rotated case.
- Erdős–Soifer, Geombinatorics 4(4) 1995: full text inaccessible (journal archive is Cloudflare-gated; no free copy located); however every secondary source describing this paper (Soifer's later chapter "Classic Conjectures Allow Young Mathematicians to Commence Research", the Monthly and Math. Mag. papers, and Bloom's site, and Soifer's books' publicity text) describes only the problem statement, the prize, and the **lower-bound constructions** — never a proof of f(5)=2.
- Bollobás, *The Art of Mathematics: Coffee Time in Memphis*, C.U.P. 2006, **Problem 32**: "Place two squares (with disjoint interiors) into a unit square. Show that the sum of the side-lengths is at most 1." — a modern published home for the f(2) result (solution text not recoverable online; the archive.org scan is disabled). Nothing on f(5).

Conclusion: **Newman's proof of f(5)=2 survives only as an attribution.** Any modern attack must reconstruct it from scratch (see §4.3).

---

## 3. Complete proof that f(2) = 1, rotations allowed

Everything below is self-contained and fully rigorous. It is a modern rendering of the classical technique (separating line + corner renormalization = "corner regions").

**Setup.** U = [0,1]². S₁, S₂ ⊆ U are closed squares with side lengths a, b ≥ 0 and disjoint interiors. Squares may be arbitrarily rotated. Goal: a + b ≤ 1.

If a = 0 or b = 0 the claim is trivial (a square inside U has side ≤ 1). So assume a, b > 0.

**Step 1 (separating line).** int S₁ and int S₂ are disjoint nonempty open convex sets, so by the separation theorem there exist a unit vector n and c ∈ ℝ with ⟨x, n⟩ ≤ c on int S₁ and ⟨x, n⟩ ≥ c on int S₂; by continuity the same holds on S₁ = cl(int S₁) and S₂. 

**Step 2 (normalization).** The maps (x,y) ↦ (1−x, y), (x,y) ↦ (x, 1−y), (x,y) ↦ (1−x, 1−y) are symmetries of U carrying squares to squares; they flip the signs of the coordinates of n. Applying one of them (and, if needed, replacing (n, c) by (−n, −c) and swapping the labels of S₁, S₂), we may assume

  n = (cos α, sin α) with α ∈ [0, π/2],  S₁ ⊆ {φ ≤ c},  S₂ ⊆ {φ ≥ c},  where φ(x,y) := x cos α + y sin α.

Since S₁ ⊆ U lies in the first quadrant, where φ ≥ 0, and S₁ has interior points, c > 0 would fail only if… precisely: sup_{S₁} φ ≤ c and φ ≥ 0 on S₁ force c ≥ 0; if c = 0 then S₁ ⊆ {φ = 0} has empty interior — contradiction. So c > 0. Symmetrically, writing h := cos α + sin α (note h = max_U φ, attained at (1,1)), we get c < h. So 0 < c < h.

**Step 3 (Key Lemma / "corner lemma").**

> **Lemma A.** Let α ∈ [0, π/2], h = cos α + sin α, and c > 0. If a square S of side s lies in the region T = {(x,y) : x ≥ 0, y ≥ 0, x cos α + y sin α ≤ c}, then
>   **s·(cos α + sin α) ≤ c**, i.e. s ≤ c/h.
> Equivalently: if any square of side s fits in the corner region T, then the axis-parallel corner square [0,s]² fits in T. For α ∈ (0, π/2), equality forces S to be axis-parallel.

*Proof.* Let S have center z = (z_x, z_y) and edge directions u = (cos θ, sin θ), w = (−sin θ, cos θ), with θ ∈ [0, π/2) (the orientation angle is well-defined mod π/2). The four vertices are z ± (s/2)u ± (s/2)w with independent signs. Since a linear functional on a square is extremized at vertices:

- min over S of the x-coordinate is z_x − (s/2)(|u_x| + |w_x|) = z_x − (s/2)(cos θ + sin θ). Since S ⊆ {x ≥ 0}: **z_x ≥ (s/2)G**, where G := cos θ + sin θ ∈ [1, √2].
- Likewise z_y ≥ (s/2)G.
- max over S of φ equals φ(z) + (s/2)(|φ(u)| + |φ(w)|) = φ(z) + (s/2)·D, where φ(u) = cos(θ−α), φ(w) = sin(α−θ), so D := |cos(θ−α)| + |sin(θ−α)| ∈ [1, √2].

Since cos α, sin α ≥ 0, the first two bullets give φ(z) ≥ (s/2)G(cos α + sin α) = (s/2)GF with F := h = cos α + sin α. Therefore

  c ≥ max_S φ ≥ (s/2)(GF + D).

So it suffices to prove **GF + D ≥ 2F** for all θ ∈ [0, π/2), α ∈ [0, π/2]. Note θ − α ∈ (−π/2, π/2), so cos(θ−α) ≥ 0 and

  GF = (cos θ + sin θ)(cos α + sin α) = cos(θ−α) + sin(θ+α).

*Case θ ≥ α.* Then D = cos(θ−α) + sin(θ−α), and sin(θ+α) + sin(θ−α) = 2 sin θ cos α, so
  GF + D − 2F = 2·g(θ), g(θ) := cos(θ−α) + sin θ cos α − cos α − sin α.
Compute: g(α) = 1 + sin α cos α − cos α − sin α = (1 − cos α)(1 − sin α) ≥ 0; g(π/2) = sin α + cos α − cos α − sin α = 0; and g″(θ) = −cos(θ−α) − sin θ cos α ≤ 0 on [α, π/2]. A concave function that is ≥ 0 at both endpoints of an interval is ≥ 0 on the whole interval. Hence g ≥ 0 on [α, π/2]. ✔

*Case θ < α.* Then D = cos(α−θ) + sin(α−θ), and sin(θ+α) + sin(α−θ) = 2 sin α cos θ, so
  GF + D − 2F = 2·h₀(θ), h₀(θ) := cos(α−θ) + sin α cos θ − cos α − sin α.
Compute: h₀(0) = 0; h₀(α) = (1 − cos α)(1 − sin α) ≥ 0; h₀″(θ) = −cos(α−θ) − sin α cos θ ≤ 0 on [0, α]. Concavity again gives h₀ ≥ 0 on [0, α]. ✔

Thus c ≥ (s/2)(GF + D) ≥ sF = s(cos α + sin α), proving the inequality. For the equality statement with α ∈ (0, π/2): then (1−cos α)(1−sin α) > 0, so in the first case g > 0 on [α, π/2) (concavity: g lies above the chord joining (α, g(α)>0) and (π/2, 0)), forcing θ = π/2 ≡ 0 (axis-parallel); in the second case h₀ lies above the chord joining (0,0) and (α, h₀(α)>0), so h₀ > 0 for θ ∈ (0, α], forcing θ = 0. ∎

*Remark.* Lemma A is exactly Beck–Bleicher's Lemma 14 specialized to n = 4 (their Lemma 17), in analytic form: "if the corner triangle accommodates any square of side s, it accommodates the corner-aligned one."

**Step 4 (conclusion).** Apply Lemma A to S₁ ⊆ U ∩ {φ ≤ c} ⊆ {x ≥ 0, y ≥ 0, φ ≤ c}:

  a ≤ c / h.

For S₂, apply the point reflection ρ(x,y) = (1−x, 1−y), a symmetry of the plane carrying squares to squares. Since φ(ρ(x,y)) = h − φ(x,y), the image ρ(S₂) is a square of side b contained in {x ≥ 0, y ≥ 0, φ ≤ h − c} (using S₂ ⊆ U ⊆ {x ≤ 1, y ≤ 1} and φ ≥ c on S₂). Lemma A gives

  b ≤ (h − c)/h.

Adding: **a + b ≤ c/h + (h−c)/h = 1.** ∎

**Equality.** If a + b = 1, both applications of Lemma A are tight. If moreover the separating direction can only be chosen with α ∈ (0, π/2) strictly, the equality clause forces both squares to be axis-parallel; if an axis-parallel separating line exists (say vertical), then the x-projections of S₁, S₂ (of lengths aG₁, bG₂ ≥ a, b) have disjoint interiors inside [0,1], so a + b ≤ aG₁ + bG₂ ≤ 1 with equality again forcing G₁ = G₂ = 1, i.e. axis-parallel. **So every extremal pair is axis-parallel** — consistent with the general conjecture's extremal pictures. Equality is attained, e.g. by [0,t]² and [t,1]² for any t ∈ [0,1]; hence f(2) = 1 exactly.

**Beck–Bleicher's original finish (equivalent):** with ℓ not parallel to a side, the support lines of U parallel to ℓ touch U at opposite corners P₁, P₂; replacing S₁, S₂ by the corner-aligned squares of the same sides at P₁, P₂ (Lemma A), their diagonals are disjoint segments of the main diagonal P₁P₂, so √2·a + √2·b ≤ √2.

**Why this is "the" technology for the tilted case.** The two rotation-proof mechanisms in this proof are:
1. **Corner renormalization** (Lemma A): the corner of the container beats rotation — among all placements of a square of side s in a corner region cut off by a line, the axis-aligned corner placement minimizes the "support width" toward the cut. This converts a tilted square into an axis-parallel one *at no cost in the relevant functional*.
2. **One-dimensionalization along the separating normal**: after renormalization, the constraint becomes additive along a single segment (the diagonal / the φ-range [0,h]).

Any attack on f(k²+1) with rotations must generalize (1) to interior squares (which see no corner) — this is precisely what breaks for n ≥ 3 squares, and what Newman must have overcome for n = 5.

---

## 4. Newman's f(5) = 2

### 4.1 Status of the source
Definitive: the only trace in print is Erdős–Graham 1975, reference "[2] D. J. NEWMAN, personal communication." Every later mention (Erdős 1994; Erdős–Soifer 1995 as described by all secondary sources; erdosproblems.com) traces back to this attribution. D. J. Newman died in 2007; no problem-collection of his (e.g. *A Problem Seminar*, Springer 1982) contains it — the technique is lost.

### 4.2 What f(5)=2 says and rotation-proof partial bounds
Five squares in U with disjoint interiors: Σaᵢ ≤ 2, tight (four 1/2-squares + one degenerate, or the split-cell configuration: side lengths 1/2,1/2,1/2,1/4,1/4… — the standard extremal families all satisfy Σ = 2).

Rotation-proof bounds available today:
- Cauchy–Schwarz: f(5) ≤ √5 ≈ 2.2360.
- Monotonicity: f(5) ≥ f(4) = 2.
- Any improvement of the constant √5 toward 2 with rotations allowed would already be new.

### 4.3 Reconstruction analysis (what a Newman-style proof must do)
Labeled speculation, but constrained by the tools available in 1975:

1. **The largest-square dichotomy.** Let a₁ ≥ … ≥ a₅. Since Σaᵢ² ≤ 1, if a₁ ≤ 1/2 then Σaᵢ ≤ √(5·¼)·… (C–S gives Σ ≤ √5/2·? — precisely Σaᵢ ≤ √(5 Σaᵢ²) doesn't improve; but Σaᵢ ≤ a₁ + √(4(1−a₁²)) = a₁ + 2√(1−a₁²), maximized at a₁ = 1/√5 giving √5). To reach 2 one needs geometric, not just area, information. The natural split: (i) a₁ large (≥ 1/2): then S₁ "blocks" U — every axis-parallel or tilted big square of side ≥ 1/2 in U contains the center of U (elementary check via the bounding-box constraint), so the other four squares are distributed among the four center-missing corner regions; a Lemma-A-type corner bound per region then bounds each of them. (ii) all aᵢ < 1/2: here the area bound alone gives Σ ≤ √5 and something extra is needed — this is the genuinely hard regime, and precisely the regime the axis-parallel proofs (BKU24) handle by line-sweeps that fail for tilted squares.
2. **Separating structure.** For each pair (i,j) a separating line exists; for 5 convex bodies in a square the "separation pattern" can be encoded by a planar structure (a pseudoline arrangement / a partition of U into 5 convex cells, one per square, by the "power-diagram"-like refinement of separating lines). A Newman-style elegant proof plausibly used: partition U into 5 convex polygons P₁,…,P₅ with Sᵢ ⊆ Pᵢ (this always exists for pairwise interior-disjoint convex bodies — iteratively cut along separating lines), then a **per-cell isoperimetric-type inequality**: for a convex polygon P ⊆ U, the largest square in P has side ≤ β(P) for a functional β that is superadditive-compatible with Σβ(Pᵢ) ≤ 2 over 5-cell convex partitions of U. Lemma A is exactly the required inequality when P is a corner cell cut by one line. The missing ingredient is the analogous sharp bound for cells cut by 2+ lines (interior cells). **Recovering/creating this "multi-cut Lemma A" is, in my assessment, the most promising concrete step toward reproducing Newman's result** — for n=5 the combinatorics of 5-cell convex partitions of a square is small enough to case-check (at most one bounded "interior" cell, or configurations of 4+1 / 3+2 boundary cells).
3. **Sanity constraint on any reconstruction:** the proof must be sharp simultaneously for the two distinct near-extremal families (2×2 grid with one cell split into two 1/4-squares; and 2×2 grid with one degenerate square anywhere), and must *not* prove f(6) ≤ 2 + something false (f(6) ≥ 2 + 1/3 by Halász).

---

## 5. Folklore theorem: every tiling of a rectangle by squares is axis-parallel — complete proof

This is stated as "easy to prove" folklore in the literature (e.g. in arXiv:1406.0823 for rectangle tiles); here is a full rigorous proof. It is needed as a rigidity lemma (e.g. §5.1) and is the natural "0-th stability theorem" for the tilted problem.

**Definitions.** A *tiling* of a compact region R by squares Q₁,…,Q_N means: each Qᵢ is a (closed, possibly tilted) square, ∪ᵢQᵢ = R, and int Qᵢ ∩ int Qⱼ = ∅ for i ≠ j. Fix coordinates so the rectangle R is axis-parallel. Call a compact set *rectilinear* if it is a finite union of axis-parallel closed rectangles (possibly empty).

> **Theorem.** If a rectilinear region P is tiled by squares Q₁,…,Q_N, then every Qᵢ is axis-parallel. In particular this holds for a rectangle P. (The same proof works verbatim when the tiles are rectangles.)

*Proof.* Induction on N. For N = 0, vacuous. Let N ≥ 1 and let P = ∪ᵢQᵢ ≠ ∅ be rectilinear, P = R₁ ∪ … ∪ R_m with Rⱼ axis-parallel rectangles (each with nonempty interior WLOG — degenerate ones can be dropped since P = cl(int P), as P is a finite union of squares with interior).

**(1) The lex-min corner.** Let y₀ = min{y : (x,y) ∈ P} and x₀ = min{x : (x, y₀) ∈ P}; set c = (x₀, y₀). Every defining rectangle Rⱼ containing c satisfies Rⱼ ⊆ {y ≥ y₀} (else P would contain points below y₀), and its bottom edge is at height y₀; moreover Rⱼ cannot contain a point (x, y₀) with x < x₀. Hence c is the lower-left vertex of each such Rⱼ, i.e. Rⱼ ⊆ W := {x ≥ x₀, y ≥ y₀}, and Rⱼ ⊇ [x₀, x₀+δⱼ] × [y₀, y₀+δⱼ] for some δⱼ > 0. Since the Rⱼ are closed and finitely many, there is δ > 0 with B(c, δ) ∩ Rⱼ = ∅ for every Rⱼ ∌ c. Therefore, near c,
  P ∩ B(c, δ) = W ∩ B(c, δ)  (for δ small enough): "P is locally a 90° wedge with axis-parallel edges at c."

**(2) The tile at c is axis-parallel.** Let Q = Qᵢ ∋ c. Since Q ⊆ P, near c we have Q ⊆ W.
- c ∉ int Q: else Q ⊇ B(c, ε) ⊄ W.
- c is not in the relative interior of an edge of Q: else Q contains a half-disk centered at c, whose directions span an angle π > π/2, contradicting Q ⊆ W locally (W spans exactly π/2).
- Hence c is a vertex of Q. The two edges of Q at c span a closed 90° cone C_Q ∋ directions of Q near c, and C_Q ⊆ C_W = [0°, 90°] (the wedge cone). Two closed 90° arcs with C_Q ⊆ C_W must coincide. So the edges of Q at c point in directions +x and +y: **Q = [x₀, x₀+s] × [y₀, y₀+s] is axis-parallel.**

**(3) Removing Q preserves the setting.** Let P′ = ∪_{j≠i} Qⱼ. Claim: P′ = cl(P ∖ Q) and P′ is rectilinear, tiled by the remaining N−1 squares.
- Tiling of P′ is by definition (interiors pairwise disjoint, union P′).
- P′ = cl(P∖Q): (⊇) P∖Q ⊆ P′ since a point of P outside Q lies in some tile ≠ Q; P′ closed. (⊆) For j ≠ i: int Qⱼ ∩ Q = ∅ — indeed int Qⱼ ∩ int Q = ∅, and if y ∈ int Qⱼ ∩ ∂Q then every neighborhood of y meets int Q (Q is a solid square), so int Qⱼ ∩ int Q ≠ ∅, contradiction. Hence int Qⱼ ⊆ P ∖ Q and Qⱼ = cl(int Qⱼ) ⊆ cl(P∖Q).
- Rectilinearity: take the finite grid generated by all x- and y-coordinates of the corners of R₁,…,R_m and of Q. Then P and Q are unions of closed grid cells. For a closed cell C ⊆ P: if C ⊆ Q it contributes nothing to cl(P∖Q); otherwise C ∩ Q ⊆ ∂C (as Q is a union of cells), so C ∖ Q ⊇ int C is dense in C and C ⊆ cl(P∖Q). Hence cl(P∖Q) = ∪{cells C : C ⊆ P, C ⊄ Q}, a finite union of axis-parallel rectangles. ✔

By induction all remaining tiles are axis-parallel. ∎

**Corollary (rigidity of the equality case of f(k²) = k — rotation-proof).** If k² squares in U with disjoint interiors have Σaᵢ = k, then they are exactly the axis-parallel k×k grid of (1/k)-squares. 
*Proof.* Equality in Σaᵢ ≤ √(k² Σaᵢ²) forces a₁ = … = a_{k²} =: a, and then k²a = k gives a = 1/k, so Σaᵢ² = 1 = area(U): the squares tile U (their union is a closed subset of U of full measure, and it is closed with U∖∪ open of measure 0, hence empty). By the Theorem all tiles are axis-parallel, and a tiling of U by k² axis-parallel (1/k)-squares is the grid (each square on the bottom edge must sit on the floor; induct along rows, or: the lex-min induction above successively locates each tile at the current lex-min corner, whose position is forced). ∎

This corollary is the honest "stability anchor": **any proof of f(k²+1) = k must in particular rule out tilted near-tilings, and the folklore theorem is the qualitative statement that exact tilings cannot tilt.** A quantitative version ("a packing of k² squares with Σaᵢ ≥ k − ε is ε′-close to the grid") is not in the literature (see §6) and would be a publishable step.

---

## 6. Stability-type theorems for square packings (Fejes Tóth school and successors)

What actually exists, with precise statements:

1. **Roth–Vaughan 1978** (*Inefficiency in packing squares with unit squares*, JCTA A 24, 170–186). Let W(s) = s² − (max number of unit squares, arbitrary rotation, packable in an s×s square). Then (verbatim from Friedman's survey, confirmed): **if s(s−⌊s⌋) > 1/6, then W(s) ≥ 10⁻¹⁰⁰ √(s·‖s‖)**, where ‖s‖ is the distance from s to the nearest integer. Consequently W(s) ≠ O(s^α) for α < 1/2. *Technique (the one genuinely tilted-square-capable quantitative argument in print):* classify each unit square as **good** (inclination ≤ 10⁻¹⁰ to the container's sides) or bad; bad squares are charged an area waste proportional to (tilt angle)² in thin horizontal strips (a tilted unit square crossing a strip of height τ covers at most τ·(1 + O(φ²))⁻¹… i.e., wastes ~ φ²τ per unit length); good squares are then treated by a 1-dimensional discrepancy/parity argument across ~√s strips, where the non-integrality ‖s‖ forces per-strip waste. This "tilt-penalty + near-aligned discrepancy" scheme is the closest thing to a stability theorem for square packings and is directly relevant technology for bounding Σaᵢ in #106-type problems.
2. **Erdős–Graham 1975:** W(s) = O(s^{7/11}) (tilted "herringbone" boundary packings — the reason rotations must be taken seriously). **Montgomery** improved to O(s^{(3−√3)/2+ε}) (exponent ≈ 0.634; reported in Roth–Vaughan). Recent: **arXiv:2504.09489** (*Square packing with asymptotically smallest waste only needs good squares*, 2025) shows near-optimal waste is achievable using only almost-aligned squares — a structural "you may as well be nearly axis-parallel" result, i.e., a stability statement in the constructive direction. Survey: Erich Friedman, *Packing Unit Squares in Squares*, Electron. J. Combin. Dynamic Survey #7.
3. **Beck–Bleicher 1971/72** (§2.4): the exact characterization of "tight" figures (two similar copies can't beat the perimeter) as regular polygons and constant-width curves — with the perimeter-supremum bounded by √2 for every convex figure (their Lemma 1, by the area argument), and the extremal figures for √2 identified (isosceles right triangle; parallelogram with side ratio √2). Their §§VI–IX develop necessary conditions ("minimum width condition", "non-rotation condition") — infinitesimal-rigidity-style arguments about rotating one packed copy out of contact, which is precisely a stability analysis of two-body packings and may generalize.
4. **Negative result to be aware of:** the **square lattice packing of congruent squares is NOT uniformly stable** (in the sense of Bárány–Dolbilin / Connelly's packing-stability theory — see Connelly, *Packings of circles and spheres*, and the Fejes Tóth-school surveys; the triangular circle packing IS uniformly stable). Also, perfect *non-grid* square tilings of a square exist with unequal squares (squared squares), so "density ≈ 1 ⇒ grid-like" is simply false without the equal-sides/equal-sum functional. Any stability approach to #106 must therefore hinge on the specific functional Σaᵢ (as in the Corollary of §5), not on density alone.
5. **L. Fejes Tóth's classical stability program** (Lagerungen; G. Fejes Tóth's survey chapter *Packing and Covering*, Handbook of Discrete and Computational Geometry, ch. 2) contains stability versions for circle packings (hexagonal), but **no quantitative stability theorem for congruent/near-equal square packings is on record** — a genuine gap; the Roth–Vaughan machinery is the substitute.

---

## 7. Assessment: the recovered "tilted technology", condensed

1. **Corner renormalization (Lemma A / Beck–Bleicher Lemma 14).** *In a corner region cut by a line, the axis-aligned corner square is optimal.* Rigorous, sharp, rotation-proof; equality forces axis-parallel. This is the entire content of the f(2)=1 proof and the only sharp per-region bound known for tilted squares. **Generalization target:** the analogous sharp statement for a convex cell of U cut by two or more lines ("multi-cut corner lemma") would likely reprove f(5)=2 and is the concrete next step.
2. **Support/width one-dimensionalization** along a separating normal (plus Barbier's theorem in the constant-width analogue, Beck–Bleicher Thm. 12) — turn 2-D disjointness into additivity over a segment.
3. **Cauchy–Schwarz/area** — rotation-proof but off by the factor √(1 + 1/k²) at n = k²+1.
4. **Roth–Vaughan tilt-penalty accounting** — quantitative: a square tilted by φ inside near-rectangular structures wastes area ≳ φ²·(scale). Combine with §5's rigidity to hope for: "Σaᵢ ≥ k − ε with n = k²+1 squares ⇒ all tilts O(√ε) ⇒ reduce to the solved axis-parallel case (BKU24) with controlled error." This "reduce-to-BKU-by-stability" pipeline is, on the evidence collected here, the most promising known-technology route to f(k²+1) = k with rotations.

---

## Sources

- [Erdős Problem #106 (T. F. Bloom, erdosproblems.com)](https://www.erdosproblems.com/106) and [reference list](https://www.erdosproblems.com/latex/106)
- [P. Erdős, *Some problems in number theory, combinatorics and combinatorial geometry*, Math. Pannonica 5/2 (1994) 261–269 — full PDF](https://mathematica-pannonica.ttk.pte.hu/articles/mp05-2/mp05-2-261-269.pdf)
- [P. Erdős, R. L. Graham, *On packing squares with equal squares*, JCTA A 19 (1975) 119–123 — full PDF](https://mathweb.ucsd.edu/~ronspubs/75_06_squares.pdf)
- [A. Beck, M. N. Bleicher, *Packing convex sets into a similar set*, Acta Math. Acad. Sci. Hungar. 22 (1971/72) 283–303 — full volume scan, REAL-J](https://real-j.mtak.hu/7419/1/MTA_ActaMathHung_22.pdf)
- [Baek–Koizumi–Ueoro, *A note on the Erdős conjecture about square packing*, arXiv:2411.07274](https://arxiv.org/abs/2411.07274)
- [I. Praton, *The Erdős and Campbell-Staton conjectures about square packing*, arXiv:math/0504341](https://arxiv.org/abs/math/0504341); Praton, *Packing squares in a square*, Math. Mag. 81 (2008) 358–361
- [Campbell–Staton, *A Square-Packing Problem of Erdős*, Amer. Math. Monthly 112 (2005) 165–167](https://www.tandfonline.com/doi/abs/10.1080/00029890.2005.11920180)
- [A. Raj Singh, *On a square packing conjecture of Erdős*, arXiv:2601.22163](https://arxiv.org/abs/2601.22163); [arXiv:2506.23284](https://arxiv.org/abs/2506.23284)
- [E. Friedman, *Packing Unit Squares in Squares: A Survey*, Electron. J. Combin. DS#7](https://erich-friedman.github.io/papers/squares.pdf) (source of the verified Roth–Vaughan and Montgomery statements)
- [Roth–Vaughan, *Inefficiency in packing squares with unit squares*, JCTA A 24 (1978) 170–186](https://www.sciencedirect.com/science/article/pii/0097316578900055)
- [*Square packing with asymptotically smallest waste only needs good squares*, arXiv:2504.09489](https://arxiv.org/abs/2504.09489)
- [G. Fejes Tóth, *Packing and Covering*, Handbook of Discrete and Computational Geometry, ch. 2](http://www.csun.edu/~ctoth/Handbook/chap2.pdf); [R. Connelly, *Packings of circles and spheres* (uniform stability; square lattice not uniformly stable)](https://pi.math.cornell.edu/~connelly/PackingsIII.IV.pdf)
- B. Bollobás, *The Art of Mathematics: Coffee Time in Memphis*, CUP 2006, Problem 32 (modern home of the f(2) problem); [Geombinatorics author index (Erdős–Soifer 1995 bibliographic data)](https://geombina.uccs.edu/author-index/paul-erdos)
- Axis-parallel tiling folklore cited in [arXiv:1406.0823](https://arxiv.org/abs/1406.0823) (proof reconstructed in full above)