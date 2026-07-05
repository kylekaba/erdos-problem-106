#!/usr/bin/env python3
"""
Verification harness for the Dip-Stack theorems (session-2 RIGIDITY agent).

Objects per axis: a family of M = N+1 squares, each contributing an interval
[a_i, b_i] (bbox projection, length w_i) on the line. Lattice-line count at
phase x*:  p_i(x*) = #{ j in Z : x*+j in [a_i, b_i] } = floor(b_i-x*) - ceil(a_i-x*) + 1.
P(x*) = sum p_i(x*), piecewise constant with breakpoints at a_i, b_i mod 1.

Claims tested exactly (piecewise-constant arithmetic, no sampling error):
  D1 (dip identity)     : {P <= N} = {Gcheck - Fplus >= r},  r = 1 + sum(floor(w)-1)_+
  D2 (mean identity)    : E[Gcheck - Fplus] = r - t,  t = sum w - N
  D3 (stack forcing)    : int_E Gcheck >= 1 - t  and  (1-t)_+ <= Hx * delta_x
  D4 (kappa bounds)     : kappa >= delta_x*delta_y, kappa >= (1-t)_+ * max(delta_x, delta_y)
  STAR (**)             : 1 - eps <= tau_m + sqrt( kappa * min(HxE, HyE) )   [tilt-aware]
  STARweak              : 1 - eps <= tau_m + sqrt( kappa * HxE * HyE )
where Gcheck = miss-count of the w<1 squares, Fplus = frac-hit count of w>=1 squares,
E = dip set {P<=N}, HxE = max of Gcheck over E, kappa = E[(2N+1-P-Q)_+] (exact double sum).
"""
import numpy as np
from math import floor, ceil, sin, cos, sqrt

EPS = 1e-12

# ---------- exact piecewise machinery on the circle [0,1) ----------

def piecewise_P(intervals):
    """intervals: list of (a,b). Return (breaks, values) where values[j] = P on
    (breaks[j], breaks[j+1]) (breaks sorted, wrap: last piece = (breaks[-1], breaks[0]+1))."""
    brk = set()
    for a, b in intervals:
        brk.add(a % 1.0); brk.add(b % 1.0)
    brk = sorted(brk)
    if not brk:
        brk = [0.0]
    vals = []
    for j in range(len(brk)):
        lo = brk[j]
        hi = brk[j + 1] if j + 1 < len(brk) else brk[0] + 1.0
        x = (lo + hi) / 2.0 % 1.0
        P = 0
        for a, b in intervals:
            P += floor(b - x) - ceil(a - x) + 1
        vals.append(P)
    lens = []
    for j in range(len(brk)):
        hi = brk[j + 1] if j + 1 < len(brk) else brk[0] + 1.0
        lens.append(hi - brk[j])
    return brk, np.array(vals), np.array(lens)

def counts_on_pieces(intervals, brk):
    """per-piece counts of Gcheck (misses of w<1 squares) and Fplus (frac hits of w>=1)."""
    G, F = [], []
    for j in range(len(brk)):
        lo = brk[j]
        hi = brk[j + 1] if j + 1 < len(brk) else brk[0] + 1.0
        x = (lo + hi) / 2.0 % 1.0
        g = f = 0
        for a, b in intervals:
            w = b - a
            p = floor(b - x) - ceil(a - x) + 1
            if w < 1.0:
                if p == 0:
                    g += 1
            else:
                if p == floor(w) + 1:
                    f += 1
        G.append(g); F.append(f)
    return np.array(G), np.array(F)

def axis_report(intervals, N):
    brk, P, lens = piecewise_P(intervals)
    G, F = counts_on_pieces(intervals, brk)
    w = np.array([b - a for a, b in intervals])
    t = w.sum() - N
    r = 1 + sum(max(floor(x) - 1, 0) for x in w)
    dip = P <= N
    dip2 = (G - F) >= r
    ident_ok = np.all(dip == dip2)
    mean_GF = float(((G - F) * lens).sum())
    mean_ok = abs(mean_GF - (r - t)) < 1e-9
    delta = float(lens[dip].sum())
    intE_G = float((G[dip] * lens[dip]).sum())
    HE = int(G[dip].max()) if dip.any() else 0
    stack_ok = intE_G >= (1 - t) - 1e-9
    forcing_ok = (max(1 - t, 0.0) <= HE * delta + 1e-9)
    return dict(brk=brk, P=P, lens=lens, G=G, F=F, t=t, r=r, delta=delta,
                HE=HE, intE_G=intE_G, ident_ok=ident_ok, mean_ok=mean_ok,
                stack_ok=stack_ok, forcing_ok=forcing_ok, mean_GF=mean_GF)

def kappa_exact(ax, ay, N):
    Px, lx = ax['P'], ax['lens']
    Qy, ly = ay['P'], ay['lens']
    K = 0.0
    for u, du in zip(Px, lx):
        z = 2 * N + 1 - u - Qy
        pos = z > 0
        K += du * float((z[pos] * ly[pos]).sum())
    return K

# ---------- geometry: squares -> axis intervals, disjointness ----------

def square_corners(cx, cy, d, th):
    h = d / 2.0
    c, s = cos(th), sin(th)
    pts = []
    for sx, sy in [(-1, -1), (1, -1), (1, 1), (-1, 1)]:
        pts.append((cx + (sx * h) * c - (sy * h) * s, cy + (sx * h) * s + (sy * h) * c))
    return pts

def bbox(sq):
    pts = square_corners(*sq)
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    return (min(xs), max(xs)), (min(ys), max(ys))

def sat_disjoint(s1, s2):
    P1 = square_corners(*s1); P2 = square_corners(*s2)
    for pts in (P1, P2):
        for i in range(4):
            x1, y1 = pts[i]; x2, y2 = pts[(i + 1) % 4]
            nx, ny = y2 - y1, x1 - x2
            pr1 = [nx * x + ny * y for x, y in P1]
            pr2 = [nx * x + ny * y for x, y in P2]
            if max(pr1) <= min(pr2) + 1e-9 or max(pr2) <= min(pr1) + 1e-9:
                return True
    return False

def check_packing(squares, k):
    n = len(squares)
    for i in range(n):
        (x0, x1), (y0, y1) = bbox(squares[i])
        assert x0 >= -1e-9 and x1 <= k + 1e-9 and y0 >= -1e-9 and y1 <= k + 1e-9, \
            f"square {i} out of container: {bbox(squares[i])}"
    bad = 0
    for i in range(n):
        for j in range(i + 1, n):
            if not sat_disjoint(squares[i], squares[j]):
                bad += 1
                print(f"  OVERLAP squares {i},{j}")
    assert bad == 0, f"{bad} overlaps"

def test_packing(name, squares, k):
    N = k * k
    assert len(squares) == N + 1, (len(squares), N + 1)
    check_packing(squares, k)
    xin, yin = [], []
    ds, ths = [], []
    for sq in squares:
        (x0, x1), (y0, y1) = bbox(sq)
        xin.append((x0, x1)); yin.append((y0, y1))
        ds.append(sq[2]); ths.append(sq[3])
    ax = axis_report(xin, N); ay = axis_report(yin, N)
    kap = kappa_exact(ax, ay, N)
    eps = sum(ds) - N
    t = ax['t']
    assert abs(ay['t'] - t) < 1e-9, "t must be equal on both axes"
    tau = t - eps  # = sum d_i sigma_i
    lhs = 1 - eps
    rhs_star = tau + sqrt(max(kap, 0) * min(ax['HE'], ay['HE'])) if min(ax['HE'], ay['HE']) > 0 or (1-t) <= 0 else tau
    rhs_weak = tau + sqrt(max(kap, 0) * ax['HE'] * ay['HE'])
    ok_prod = kap >= ax['delta'] * ay['delta'] - 1e-9
    ok_lin = kap >= max(1 - t, 0) * max(ax['delta'], ay['delta']) - 1e-9
    ok_star = lhs <= rhs_star + 1e-9
    ok_weak = lhs <= rhs_weak + 1e-9
    print(f"\n=== {name} (k={k}, n={N+1}) ===")
    print(f" eps={eps:+.6f}  t={t:+.6f}  tau_m={tau:.6f}  kappa={kap:.6f}")
    print(f" x-axis: delta={ax['delta']:.6f} H_E={ax['HE']} intE_G={ax['intE_G']:.6f} "
          f"ident={ax['ident_ok']} mean={ax['mean_ok']} stack={ax['stack_ok']} forcing={ax['forcing_ok']}")
    print(f" y-axis: delta={ay['delta']:.6f} H_E={ay['HE']} intE_G={ay['intE_G']:.6f} "
          f"ident={ay['ident_ok']} mean={ay['mean_ok']} stack={ay['stack_ok']} forcing={ay['forcing_ok']}")
    print(f" D4 kappa>=dx*dy: {ok_prod} ({kap:.6f} >= {ax['delta']*ay['delta']:.6f})")
    print(f" D4 kappa>=(1-t)max(d): {ok_lin} ({kap:.6f} >= {max(1-t,0)*max(ax['delta'],ay['delta']):.6f})")
    print(f" STAR  1-eps <= tau+sqrt(kappa*minH): {ok_star}  ({lhs:.6f} <= {rhs_star:.6f})")
    print(f" STARw 1-eps <= tau+sqrt(kappa*HxHy): {ok_weak}  ({lhs:.6f} <= {rhs_weak:.6f})")
    allok = all([ax[f] for f in ('ident_ok', 'mean_ok', 'stack_ok', 'forcing_ok')] +
                [ay[f] for f in ('ident_ok', 'mean_ok', 'stack_ok', 'forcing_ok')] +
                [ok_prod, ok_lin, ok_star, ok_weak])
    print(f" ALL CHECKS: {'PASS' if allok else '*** FAIL ***'}")
    return allok

# ---------- packings ----------

def deficient_column(k):
    c = k / (k + 1)
    sq = [(c / 2, r * c + c / 2, c, 0.0) for r in range(k + 1)]
    for i in range(1, k):
        for j in range(k):
            sq.append((i + 0.5, j + 0.5, 1.0, 0.0))
    return sq

def split_cell(k, a=0.3):
    b = 1 - a
    sq = [(a / 2, a / 2, a, 0.0), (a + b / 2, a + b / 2, b, 0.0)]
    for i in range(k):
        for j in range(k):
            if (i, j) != (0, 0):
                sq.append((i + 0.5, j + 0.5, 1.0, 0.0))
    return sq

def t12_column_tiling():
    # k=4, b=2: widths 2/3 (6 squares), 4/3 (3 squares), two unit columns (4 each)
    k = 4
    sq = []
    w1 = 2.0 / 3.0
    for r in range(6):
        sq.append((w1 / 2, r * w1 + w1 / 2, w1, 0.0))
    w2 = 4.0 / 3.0
    for r in range(3):
        sq.append((w1 + w2 / 2, r * w2 + w2 / 2, w2, 0.0))
    for cidx in range(2):
        x0 = w1 + w2 + cidx
        for r in range(4):
            sq.append((x0 + 0.5, r + 0.5, 1.0, 0.0))
    return sq, k

def running_bond_deficient_row(k=3, seed=1):
    rng = np.random.default_rng(seed)
    c = k / (k + 1)
    sq = []
    # deficient row at bottom: k+1 squares side c tiling [0,k] x [0,c]
    for r in range(k + 1):
        sq.append((r * c + c / 2, c / 2, c, 0.0))
    # k-1 unit rows above, each with random x-offset (running bond), cyclic wrap
    for row in range(k - 1):
        y = c + row + 0.5
        off = rng.uniform(0, 1)
        # k unit squares: cyclic offset means one straddles: instead use offset in [0,0] wrap-free:
        # place k unit squares at x = ((off + i) mod k) would straddle; use non-wrapping shifts:
        # squares at [off, off+1], ..., but last wraps -> split not allowed. Use offset only for phases:
        # shift row by off, but last square shrunk to fit: sides must stay 1 => instead
        # jitter: k unit squares flush from x=0 (no room for offset at side 1). Use side 1-1e-9?
        # Simplest valid running bond: rows of k unit squares flush (offset 0) BUT the
        # deficient row already spreads x-phases. Alternative: offset rows with k squares of
        # side (k-2*off_pad)/k? keep sides = 1, offset 0. We keep flush rows here.
        for i in range(k):
            sq.append((i + 0.5, y, 1.0, 0.0))
    return sq

def tilted_grain_k2():
    # k=2: 2x2 coherent grain of side 0.85 tilted 0.06 + tiny corner square
    k = 2
    d, th = 0.85, 0.06
    c, s = cos(th), sin(th)
    # grain: squares centered on a rotated grid, spacing d, grain center placed to fit
    w_block = 2 * d * (c + s)  # bbox of the 2x2 block ~ 1.7*1.058=1.799
    x0 = w_block / 2 + 0.001
    cent = (x0, x0)
    sqs = []
    for ix in (-0.5, 0.5):
        for iy in (-0.5, 0.5):
            dx = ix * d * c - iy * d * s
            dy = ix * d * s + iy * d * c
            sqs.append((cent[0] + dx, cent[1] + dy, d, th))
    sqs.append((2 - 0.1, 2 - 0.1, 0.19, 0.0))
    return sqs, k

def jittered_split_grid(k=3, seed=7):
    rng = np.random.default_rng(seed)
    sq = []
    a, b = 0.4, 0.6
    sq.append((0.5 + (0.5 - a / 2) * 0, a / 2, a, 0.0))  # placed below
    # cell (0,0): split into a (bottom-left) and b (top-right)
    sq[0] = (a / 2, a / 2, a, 0.0)
    sq.append((a + b / 2 - 1e-12, a + b / 2 - 1e-12, b, 0.0))
    for i in range(k):
        for j in range(k):
            if (i, j) == (0, 0):
                continue
            d = 0.98
            jx = rng.uniform(0, 1 - d); jy = rng.uniform(0, 1 - d)
            sq.append((i + jx + d / 2, j + jy + d / 2, d, 0.0))
    return sq

# ---------- random arc-system Monte Carlo (pure 1-D lemmas) ----------

def arc_mc(trials=4000, seed=0):
    rng = np.random.default_rng(seed)
    worst = np.inf
    fails = 0
    for tr in range(trials):
        M = rng.integers(3, 30)
        N = M - 1
        kind = tr % 4
        if kind == 0:
            w = rng.uniform(0.05, 2.4, M)
        elif kind == 1:
            w = rng.uniform(0.85, 1.15, M)          # near-critical
        elif kind == 2:
            w = np.clip(rng.normal(1.0, 0.05, M), 0.05, 2.4)  # whisper
        else:
            w = rng.uniform(0.6, 1.0, M)            # all undersize
        a = rng.uniform(0, 10, M)
        ints = [(a[i], a[i] + w[i]) for i in range(M)]
        ax = axis_report(ints, N)
        if not (ax['ident_ok'] and ax['mean_ok'] and ax['stack_ok'] and ax['forcing_ok']):
            fails += 1
            if fails < 5:
                print("FAIL arcs:", list(zip(a, w)))
        t = ax['t']
        if 1 - t > 1e-6 and ax['HE'] > 0:
            ratio = ax['HE'] * ax['delta'] / (1 - t)
            worst = min(worst, ratio)
    print(f"\narc MC: {trials} trials, failures={fails}, worst H*delta/(1-t) = {worst:.4f} (>=1 required)")
    return fails == 0 and worst >= 1 - 1e-9

if __name__ == '__main__':
    ok = True
    ok &= arc_mc()
    ok &= test_packing("deficient column k=3", deficient_column(3), 3)
    ok &= test_packing("deficient column k=4", deficient_column(4), 4)
    ok &= test_packing("split cell k=2 (a=0.3)", split_cell(2, 0.3), 2)
    sq, k = t12_column_tiling(); ok &= test_packing("T12 column tiling k=4", sq, k)
    ok &= test_packing("deficient row + rows k=3", running_bond_deficient_row(3), 3)
    sq, k = tilted_grain_k2(); ok &= test_packing("tilted 2x2 grain + filler k=2", sq, k)
    ok &= test_packing("jittered split grid k=3", jittered_split_grid(3), 3)
    print("\n" + ("ALL PASS" if ok else "*** SOME FAILURES ***"))
