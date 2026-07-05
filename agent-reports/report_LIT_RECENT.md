# Literature Reconnaissance: Erdős Problem #106 (f(k²+1) = k, tilted square packing)
*Recon date: 4 July 2026*

---

## 1. The anchor paper

**[BKU24] J. Baek, J. Koizumi, T. Ueoro, "A note on the Erdős conjecture about square packing," arXiv:2411.07274 (Nov 11, 2024; v2 Nov 18, 2024), 5pp, math.CO/math.MG.**

- **Main theorems (verbatim):**
  - Theorem 1.1: "For any integers k, c with −k < c < k, we have g(k²+2c+1) = k + (c/k)."
  - Theorem 2.1: "For any positive integer k, we have g(k²+1) = k."
  Here g(n) is f(n) restricted to squares with **sides parallel to the unit square** (the Staton–Tyler variant). Theorem 1.1 determines *all* values of g.
- **Method:** Two independent proofs of the upper bound g(k²+1) ≤ k. The main one is a probabilistic/averaging argument: choose a random family of k equally spaced vertical lines (spacing 1/k), count intersections m_i of each packed square with the line family; an expectation argument produces a shifted family with Σm_i ≥ k²+1; a case partition of the squares (sets A, B, C by intersection count) then forces Σd_i ≤ k, contradiction. Axis-parallelism is used essentially — the intersection count of a square of side d with the line grid is controlled by ⌊kd⌋/⌈kd⌉ only when its sides are axis-aligned; a tilted square meets vertical lines over a horizontal extent up to √2·d, which breaks the counting.
- **On the tilted case:** The paper contains **no discussion of the rotated case** — no remark, no partial bound, no proposed approach. The general conjecture is stated as "unsolved to this day."
- **Semantic Scholar shows citationCount = 0** (paper b63aa26e…); the real follow-ups below were found by direct search.

## 2. Papers citing / following up BKU (2024–2026)

Exhaustive search (Semantic Scholar API, ADS, arXiv API, web) found **only one genuine mathematical follow-up line**, by Anshul Raj Singh, plus one formalization effort:

**[Si26 / Ra26] A. Raj Singh, "On a square packing conjecture of Erdős," arXiv:2601.22163 (submitted Jan 10, 2026).**
This supersedes his withdrawn preprint *"An Equivalence Between Erdős's Square Packing Conjecture and the Convergence of an Infinite Series,"* arXiv:2506.23284 (Jun 29, 2025; **withdrawn Dec 20, 2025** — the author's withdrawal notice says the proof of the second theorem "relies on an inequality due to Halász, which is valid only for small values of c," a restriction the proof ignored).
- **Abstract (2601.22163, verbatim):** "Let f(n) be the maximum sum of the sides of non-overlapping squares (or equilateral triangles) packed inside a unit square or (unit equilateral triangle). In this paper, we explore some properties of f and examine how the square and triangle cases are similar. We prove that a conjecture of Erdős, which says that f(k²+1) = k for all k, is equivalent to the convergence of the series Σ_{k≥1}(f(k²+1)−k). We also explore the case of parallelograms and discuss how that is similar to the case of unit square and triangle."
- **Main theorems (verbatim from the paper):**
  - Theorem 1: "Let f: ℕ→ℝ such that for all a ≤ b, we have a·f(m) ≤ a²−b²+b·f(b²−a²+m) and f(m²+1) ≥ m for any positive integer m. Let ε(k) := f(k²+1)−k, then (1) If ε(n)=0 for some n, then ε(k)=0 for all k ≤ n. (2) If ε(n)>0 for some n, then ε(k) = Ω(1/k)."
  - Theorem 2: "f(k²+1)=k for all k if and only if Σ_{k≥1} ε(k) converges."
- **Method:** Establishes a recursive superadditivity-type inequality (subdivide the unit square into a b×b grid, keep a corner a×a block scaled from an m-square packing, fill the rest with grid squares); this yields that **k·(f(k²+1)−k) is non-decreasing in k**. Both equivalences (all-k ⟺ infinitely-many-k ⟺ series convergence) follow.
- **Bears on the TILTED case: YES.** The recursive inequality does not need axis-parallelism (a scaled copy of an arbitrary packing fits in a subsquare), and erdosproblems.com has incorporated it for the general f: *"Raj Singh [Ra26] has noted that f(k²+1)=k being true for all k is equivalent to it being true for infinitely many k, which in turn is equivalent to the convergence of Σ_{k≥1}(f(k²+1)−k)."* Strategic consequence: it suffices to prove f(k²+1)=k for **infinitely many k**, and conversely, any single failure ε(n)>0 propagates to ε(k) ≥ n·ε(n)/k for all k ≥ n. It contains no new upper bound.

**Lean formalization (AI-assisted, not a new result):** erdosproblems.com forum comment on #106 by user *llllvvuu*, 10 Dec 2025: "I've used Aristotle to generate a Lean formalization of Baek-Koizumi-Ueoro (2024)'s proof that g(k²+2c+1)=k+c/k for any −k<c<k, with a remark from Terence Tao that the proof works without the arguments of Praton." This is the sole #106 entry in the GitHub wiki `teorth/erdosproblems` (AI-contributions table): `| [[106]] | 🟡 Baek, Koizumi, and Ueoro (2024) | Aristotle | 10 Dec, 2025` — 🟡 = partial (axis-parallel only). No AI contribution touches the tilted case. The AlphaEvolve paper (Georgiev–Gómez-Serrano–Tao–Wagner, arXiv:2511.02864) does **not** include problem 106.

**Adjacent but different problems (do not bear on #106):** R. McClenagan, "Optimally Packing a Large Square by Unit Squares," arXiv:2602.01484 (Feb 2026) — wasted-space W(x)=O(x^{3/5}), Erdős–Graham problem (#103), not total-side-length; "Covering a square by congruent squares," arXiv:2601.16535 — covering, not packing.

## 3. Vugar Guliyev, Baek, Koizumi (2025–2026 preprints)

- **Vugar Guliyev** (erdosproblems user Vugar_Guliyev; listed as "currently working" and "interested in collaborating" on #106, alongside **JineonBaek**): arXiv full-record search returns exactly **one** paper — Aliev, **Vugar A. Guliyev**, Jabiyev, "Best approximation of a three-variable function by sum of one-variable coordinate functions," arXiv:2507.04747 (Jul 2025, math.FA). **Nothing on square packing.** No other preprint found under this name.
- **Jineon Baek** (arXiv author feed through mid-2026): nothing further on square packing (latest: Lean-GAP dataset, May 2026; Optimality of Gerver's Sofa, 2024). Baek marked #106 "looks difficult" on erdosproblems.com.
- **Junnosuke Koizumi** (through mid-2026): nothing further on square packing (mutually touching cylinders 2025, magnitude homology 2026, etc.). His research page recounts the BKU genesis (Ueoro's 5-square proof, generalized by Koizumi, independent proof by Baek) but announces no sequel.

## 4. The classical tilted-case record (Campbell–Staton, Staton–Tyler, Praton, Halász)

- **Erdős–Graham, "On packing squares with equal squares" (1975)** — origin context; Erdős proved f(2)=1 (rotations allowed) in an early Hungarian high-school journal paper; **Newman** proved **f(5)=2** (personal communication to Erdős, rotations allowed). These remain the *only* nontrivial exact values of f at k²+1 known for the tilted problem (k=1, 2).
- **Erdős–Soifer [ErSo95] "Squares in a square" and Campbell–Staton [CaSt05] "A square packing problem of Erdős" (Geombinatorics)**: independently the lower bound f(k²+2c+1) ≥ k + c/k (−k < c < k) and the conjecture that it is sharp. **Lower bounds only; no tilted upper bound.**
- **Halász [Ha84]**: constructions f(k²+2) ≥ k + 1/(k+1), f(k²+2c) ≥ k + c/(k+1); parallelogram/triangle variants. Lower bounds only.
- **I. Praton, "The Erdős and Campbell-Staton conjectures about square packing," arXiv:math/0504341 (2005), Amer. Math. Monthly**: the Campbell–Staton conjecture for a single c is equivalent to f(k²+1)=k (all c ⟺ c=0). Reduction only; and per Tao's Dec 2025 remark, BKU's proof of the full g-conjecture doesn't even need Praton. Applies to general f, so it **does bear on the tilted case** as a reduction.
- **Staton–Tyler, "On the Erdős square-packing conjecture," Geombinatorics 17 (2007)**: introduced the axis-parallel variant g(n) (the one BKU solved) and showed g(n) is attained by tilings. Axis-parallel only.

## 5. Has any upper bound f(k²+1) ≤ k + (1/2−c)/k beyond Cauchy–Schwarz ever been published for the rotated case?

**No.** After targeted searching (arXiv full-text, Semantic Scholar, ADS, Google-indexed literature, erdosproblems.com remarks/history/forum, the Geombinatorics-adjacent literature, Friedman's packing survey), I found **no published upper bound on f(k²+1) for freely rotated squares better than the Cauchy–Schwarz bound** f(n) ≤ √n, i.e. f(k²+1) ≤ √(k²+1) < k + 1/(2k). No bound of the form k + (1/2−c)/k with c > 0 exists in the literature for any k ≥ 3. The only exact tilted values at n=k²+1 are f(2)=1 (Erdős, k=1) and f(5)=2 (Newman, unpublished personal communication, k=2). Erdősproblems.com (page last edited 6 Mar 2026, checked today) explicitly lists **no partial or complete solutions claimed** and marks the problem **OPEN / FALSIFIABLE**.

## 6. State of the art on the tilted problem (as of July 2026)

1. **The tilted conjecture f(k²+1)=k is open for every k ≥ 3.** Known exactly: f(k²)=k (Cauchy–Schwarz), f(2)=1 (Erdős), f(5)=2 (Newman).
2. **Best known bounds for k ≥ 3:** k ≤ f(k²+1) ≤ √(k²+1) < k + 1/(2k). The upper bound is bare Cauchy–Schwarz; no improvement — not even k + (1/2−ε)/k for a fixed ε — has ever been published for the rotated case.
3. **Axis-parallel case fully solved** by Baek–Koizumi–Ueoro (2024): g(k²+2c+1)=k+c/k for all −k<c<k; formalized in Lean via Aristotle (Dec 2025). Their line-counting argument breaks for tilted squares and they offer no route around it.
4. **Structural reductions available for an attack:** (a) Praton: it suffices to handle a single c; (b) Raj Singh (arXiv:2601.22163, Jan 2026): k·(f(k²+1)−k) is non-decreasing, so the conjecture for infinitely many k implies it for all k, is equivalent to convergence of Σ(f(k²+1)−k), and any counterexample at n forces error ≥ n·ε(n)/k at all k ≥ n. Consequently, **any upper bound f(k²+1) ≤ k + o(1/k) along any subsequence of k proves the full conjecture** — this is exactly why beating Cauchy–Schwarz's +1/(2k) slack in the rotated setting is the whole game.
5. **Nobody has posted a tilted-case attack.** Active claimants on erdosproblems.com are Jineon Baek and Vugar Guliyev (both "currently working"); neither has any square-packing preprint in 2025–2026 (Guliyev's only arXiv paper is in approximation theory, arXiv:2507.04747). Semantic Scholar records zero citations to BKU; the only real follow-up is Raj Singh's equivalence paper.

Sources: [arXiv:2411.07274](https://arxiv.org/abs/2411.07274) · [arXiv:2601.22163](https://arxiv.org/abs/2601.22163) · [arXiv:2506.23284 (withdrawn)](https://arxiv.org/abs/2506.23284) · [arXiv:math/0504341](https://arxiv.org/abs/math/0504341) · [erdosproblems.com/106](https://www.erdosproblems.com/106) (+ /history/106, /forum/thread/106) · [teorth/erdosproblems wiki, AI-contributions](https://github.com/teorth/erdosproblems/wiki) · [Koizumi research page](https://jkoizumi144.com/research.html) · [arXiv:2511.02864](https://arxiv.org/abs/2511.02864) · [arXiv:2602.01484](https://arxiv.org/abs/2602.01484) · [arXiv:2507.04747](https://arxiv.org/abs/2507.04747) · [Erdős–Graham 1975](https://www.math.ucsd.edu/~fan/ron/papers/75_06_squares.pdf)