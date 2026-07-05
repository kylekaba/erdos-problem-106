"""Independent adversarial verification of F1's C3 (decomposition identity) and
C4 (restricted FCMB-AP / Lemma A), plus C2 gadget formula and C1 arithmetic.

Written from scratch. Methods:
  - exact |Av| via breakpoint product partition (own implementation)
  - Monte Carlo cross-check of |Av| on a few packings
  - alpha/beta quantities via 1-D breakpoint sweep (own implementation)
  - Lemma A mechanism: whenever alpha0>0, exhibit the over-full line with
    disjoint y-intervals and deficit sum >= 1 (=> sigma >= 1 forced)
"""
import math, random
import numpy as np

# square = (a, b, d): [a,a+d] x [b,b+d] in [0,k]^2

def valid(sq, k, tol=1e-9):
    for (a,b,d) in sq:
        if not (d > 0 and a >= -tol and b >= -tol and a+d <= k+tol and b+d <= k+tol):
            return False
    for i in range(len(sq)):
        for j in range(i+1, len(sq)):
            a1,b1,d1 = sq[i]; a2,b2,d2 = sq[j]
            if min(a1+d1,a2+d2)-max(a1,a2) > tol and min(b1+d1,b2+d2)-max(b1,b2) > tol:
                return False
    return True

def ncap_1d(c, d, t):
    """# integers m with c <= t+m <= c+d  (captures on axis)."""
    return math.floor(c + d - t) - math.ceil(c - t) + 1

def exact_Av_and_maxC(sq, k):
    N = k*k
    def brk(cs):
        s = {0.0, 1.0}
        for (c,d) in cs:
            s.add(c % 1.0); s.add((c+d) % 1.0)
        return sorted(s)
    xb = brk([(a,d) for a,_,d in sq]); yb = brk([(b,d) for _,b,d in sq])
    xm = [(xb[i]+xb[i+1])/2 for i in range(len(xb)-1)]
    ym = [(yb[i]+yb[i+1])/2 for i in range(len(yb)-1)]
    xl = np.diff(xb); yl = np.diff(yb)
    P = np.array([[max(0, ncap_1d(a,d,x)) for x in xm] for a,_,d in sq])
    Q = np.array([[max(0, ncap_1d(b,d,y)) for y in ym] for _,b,d in sq])
    C = P.T @ Q
    area = np.outer(xl, yl)
    return float(area[C == N].sum()), int(C.max()), float(area[C > N].sum())

def mc_Av(sq, k, M=400_000, seed=0):
    rng = np.random.default_rng(seed)
    N = k*k
    xs = rng.random(M); ys = rng.random(M)
    C = np.zeros(M)
    for (a,b,d) in sq:
        p = np.floor(a+d-xs) - np.ceil(a-xs) + 1
        q = np.floor(b+d-ys) - np.ceil(b-ys) + 1
        C += np.maximum(p,0)*np.maximum(q,0)
    return float((C == N).mean())

def alphas(cs, n):
    """cs = [(start,d)] 1-D data. Returns a0, [a_i], and full-hit cells."""
    s = {0.0, 1.0}
    for (c,d) in cs:
        s.add(c % 1.0); s.add((c+d) % 1.0)
    bs = sorted(s)
    a0 = 0.0; ai = [0.0]*n; fullhit_cells = []
    for t in range(len(bs)-1):
        x = (bs[t]+bs[t+1])/2; L = bs[t+1]-bs[t]
        miss = [i for i,(c,d) in enumerate(cs) if ncap_1d(c,d,x) <= 0]
        if not miss:
            a0 += L; fullhit_cells.append(x)
        elif len(miss) == 1:
            ai[miss[0]] += L
    return a0, ai, fullhit_cells

def lemmaA_witness(sq, k, x):
    """At full-hit x: find line m in 0..k-1 carrying >= k+1 squares; check their
    y-intervals pairwise interior-disjoint; return (L, sum_deficit)."""
    lines = {m: [] for m in range(k)}
    for i,(a,b,d) in enumerate(sq):
        for m in range(k):
            if a <= x+m <= a+d:
                lines[m].append(i)
    best = max(lines, key=lambda m: len(lines[m]))
    idx = lines[best]
    ivs = sorted((sq[i][1], sq[i][1]+sq[i][2]) for i in idx)
    disj = all(ivs[t+1][0] >= ivs[t][1] - 1e-9 for t in range(len(ivs)-1))
    sumd = sum(sq[i][2] for i in idx)
    defsum = len(idx) - sumd
    return len(idx), disj, defsum

# ---------- constructions ----------
def column_packing(k):
    d = k/(k+1)
    sq = [(0.0, j*d, d) for j in range(k+1)]
    sq += [(float(cx), float(cy), 1.0) for cx in range(1,k) for cy in range(k)]
    return sq

def split_cell(k, a):
    sq = [(0.0,0.0,a),(0.0,a,1-a)]
    sq += [(float(cx),float(cy),1.0) for cx in range(k) for cy in range(k)][2:] if False else \
          [(0.0,0.0,a),(0.0,a,1-a)] + [(float(cx),float(cy),1.0)
             for cx in range(k) for cy in range(k) if (cx,cy)!=(0,0)]
    return sq[2:] if False else [(0.0,0.0,a),(0.0,a,1-a)] + \
        [(float(cx),float(cy),1.0) for cx in range(k) for cy in range(k) if (cx,cy)!=(0,0)]

def stack_gadget(k, sides, x0=0.0):
    h = round(sum(sides)); assert abs(sum(sides)-h) < 1e-9
    sq = []; y = 0.0
    for d in sides: sq.append((x0,y,d)); y += d
    sq += [(0.0, float(j), 1.0) for j in range(h,k)]  # fillers at x=0 (side-1: capture always)
    sq += [(float(cx),float(cy),1.0) for cx in range(1,k) for cy in range(k)]
    return sq

def random_packing(k, rng):
    """strip packing: k strips, distribute N+1 squares, random sides+gaps."""
    n = k*k+1
    while True:
        counts = [1]*k
        for _ in range(n-k): counts[rng.randrange(k)] += 1
        if max(counts) <= 3*k: break
    sq = []
    for strip, cnt in enumerate(counts):
        ds = [rng.uniform(0.1,1.0) for _ in range(cnt)]
        if sum(ds) > k:
            sc = (k-1e-9)/sum(ds)*rng.uniform(0.8,1.0)
            ds = [d*sc for d in ds]
        slack = k - sum(ds)
        cuts = sorted(rng.uniform(0,slack) for _ in range(cnt))
        gaps = [cuts[0]] + [cuts[i]-cuts[i-1] for i in range(1,cnt)]
        y = 0.0
        for d,gp in zip(ds,gaps):
            y += gp
            x0 = strip + (rng.uniform(0,1-d) if rng.random()<0.6 else 0.0)
            sq.append((x0,y,d)); y += d
    return sq if valid(sq,k) else None

def stats(sq,k):
    N=k*k; S=sum(d for *_,d in sq); g=N-sum(d*d for *_,d in sq)
    s=sum((1-d)**2 for *_,d in sq); return S,g,s

print("=== A. Column packing arithmetic + |Av| (k=1..6) ===")
for k in range(1,7):
    sq = column_packing(k); N=k*k
    assert valid(sq,k) and len(sq)==N+1
    S,g,s = stats(sq,k)
    Av,maxC,overN = exact_Av_and_maxC(sq,k)
    print(f"k={k}: Sumd-N={S-N:+.2e} g-k/(k+1)={g-k/(k+1):+.2e} "
          f"s-1/(k+1)={s-1/(k+1):+.2e} |Av|-k/(k+1)={Av-k/(k+1):+.2e} "
          f"maxC={maxC} |C>N|={overN:.1e}")

print("\n=== B. C3 identity + alpha0*beta0=0 on 25 packings (incl column, split) ===")
rng = random.Random(2026)
pool = [("column k=2", column_packing(2), 2), ("column k=3", column_packing(3), 3),
        ("split k=2 a=.37", split_cell(2,0.37), 2), ("split k=3 a=.5", split_cell(3,0.5), 3),
        ("gadget k=3 [.9,.9,.9,.3]", stack_gadget(3,[0.9,0.9,0.9,0.3]), 3)]
got = 0
while got < 20:
    k = rng.choice([2,3])
    sq = random_packing(k, rng)
    if sq: pool.append((f"rand k={k} #{got}", sq, k)); got += 1
maxerr = 0.0; a0b0max = 0.0; nviol_c4hyp = 0
for name, sq, k in pool:
    if max(d for *_,d in sq) > 1+1e-12: continue
    Av,maxC,overN = exact_Av_and_maxC(sq,k)
    a0, ai, fx = alphas([(a,d) for a,_,d in sq], len(sq))
    b0, bi, fy = alphas([(b,d) for _,b,d in sq], len(sq))
    ident = a0*sum(bi) + b0*sum(ai) + sum(x*y for x,y in zip(ai,bi))
    err = abs(Av - ident); maxerr = max(maxerr, err)
    a0b0max = max(a0b0max, a0*b0)
    S,g,s = stats(sq,k)
    sab = sum(x*y for x,y in zip(ai,bi))
    ok_term = sab <= s + 1e-12
    tw = all(ai[i] <= 1-sq[i][2]+1e-9 and bi[i] <= 1-sq[i][2]+1e-9 for i in range(len(sq)))
    flag = "" if err < 1e-10 else "  <-- IDENTITY FAIL"
    print(f"{name:26s} |Av|={Av:.6f} ident_err={err:.1e} a0={a0:.4f} b0={b0:.4f} "
          f"a0b0={a0*b0:.1e} Σaibi={sab:.4f} s={s:.4f} termwise_ok={tw}{flag}")
    # Lemma A mechanism: if a0>0 exhibit over-full line
    if a0 > 1e-9:
        L, disj, defsum = lemmaA_witness(sq, k, fx[0])
        print(f"   alpha0>0: line carries L={L} (need>={k+1}), y-disjoint={disj}, "
              f"deficit_sum={defsum:.4f} (need>=1), sigma={len(sq)-S:.4f}")
        assert L >= k+1 and disj and defsum >= 1-1e-9 and len(sq)-S >= 1-1e-9
print(f"\nmax identity error = {maxerr:.2e}; max a0*b0 = {a0b0max:.2e}")

print("\n=== C. Monte Carlo cross-check of exact_Av (3 packings) ===")
for name, sq, k in pool[:3]:
    Av,_,_ = exact_Av_and_maxC(sq,k)
    mc = mc_Av(sq,k)
    print(f"{name}: exact={Av:.5f} MC={mc:.5f} diff={abs(Av-mc):.5f}")

print("\n=== D. C2 gadget formula, 12 randomized stacks (random x0, shuffled) ===")
rng2 = random.Random(99)
fails = 0
for trial in range(12):
    k = rng2.choice([2,3,4])
    h = rng2.randrange(1, k+1)          # stack sum h, h+1 squares
    # random sides in (0,1] summing to h, h+1 of them
    while True:
        cuts = sorted(rng2.uniform(0,h) for _ in range(h))
        ds = [cuts[0]] + [cuts[i]-cuts[i-1] for i in range(1,h)] + [h-cuts[-1]]
        if 0.02 < min(ds) and max(ds) <= 1.0: break
    rng2.shuffle(ds)
    x0 = rng2.uniform(0, 1-max(ds)) if rng2.random()<0.5 else 0.0
    sq = stack_gadget(k, ds, x0=x0)
    assert valid(sq,k) and len(sq)==k*k+1
    Av,_,_ = exact_Av_and_maxC(sq,k)
    d1,d2 = sorted(ds)[:2]
    pred = d1 + (d2-d1)*(1-d1)
    S,g,s = stats(sq,k)
    ok = abs(Av-pred) < 1e-9
    fails += (not ok)
    print(f"k={k} h={h} x0={x0:.2f} sides={[round(d,3) for d in ds]}: "
          f"|Av|={Av:.6f} pred={pred:.6f} {'OK' if ok else 'MISMATCH'} (g+s={g+s:.4f})")
print(f"gadget formula failures: {fails}/12")

print("\n=== E. pigeonhole ceil check ===")
for k in range(1,9):
    print(f"k={k}: ceil((k^2+1)/k)={math.ceil((k*k+1)/k)} vs k+1={k+1}")
