import numpy as np
import itertools, math, random

# AP packing: list of (a, b, d): square [a,a+d] x [b,b+d] in [0,k]^2.

def check_packing(sq, k, tol=1e-9):
    for (a,b,d) in sq:
        assert d > 0 and a >= -tol and b >= -tol and a+d <= k+tol and b+d <= k+tol, (a,b,d)
    for i in range(len(sq)):
        for j in range(i+1, len(sq)):
            a1,b1,d1 = sq[i]; a2,b2,d2 = sq[j]
            ox = min(a1+d1, a2+d2) - max(a1, a2)
            oy = min(b1+d1, b2+d2) - max(b1, b2)
            assert not (ox > tol and oy > tol), f"overlap {i},{j}"
    return True

def p_count(a, d, x):
    # number of integers m with a <= m + x <= a + d
    return math.floor(a + d - x) - math.ceil(a - x) + 1

def exact_Av(sq, k):
    """Exact |{p in [0,1)^2 : C(p)=N}| via breakpoint partition (AP => C is
    piecewise constant on the product partition of x- and y-breakpoints)."""
    N = k*k
    def breaks(coords):
        bs = set([0.0, 1.0])
        for (c, d) in coords:
            bs.add(c % 1.0); bs.add((c + d) % 1.0)
        return sorted(bs)
    xb = breaks([(a, d) for (a,b,d) in sq])
    yb = breaks([(b, d) for (a,b,d) in sq])
    xm = [(xb[i]+xb[i+1])/2 for i in range(len(xb)-1)]
    ym = [(yb[i]+yb[i+1])/2 for i in range(len(yb)-1)]
    xl = [xb[i+1]-xb[i] for i in range(len(xb)-1)]
    yl = [yb[i+1]-yb[i] for i in range(len(yb)-1)]
    # p_i(x) matrix
    P = np.array([[max(0, p_count(a, d, x)) for x in xm] for (a,b,d) in sq])
    Q = np.array([[max(0, p_count(b, d, y)) for y in ym] for (a,b,d) in sq])
    C = P.T @ Q   # C[x_cell, y_cell] = sum_i p_i q_i
    XL = np.array(xl); YL = np.array(yl)
    area = np.outer(XL, YL)
    maxC = C.max()
    Av = area[C == N].sum()
    return Av, int(maxC)

def grid_Av(sq, k, n=1500):
    N = k*k
    xs = (np.arange(n)+0.5)/n; ys = (np.arange(n)+0.5)/n
    C = np.zeros((n,n))
    for (a,b,d) in sq:
        p = np.floor(a+d-xs) - np.ceil(a-xs) + 1
        q = np.floor(b+d-ys) - np.ceil(b-ys) + 1
        C += np.outer(np.maximum(p,0), np.maximum(q,0))
    return (C == N).mean(), C.max()

def stats(sq, k):
    N = k*k
    S = sum(d for (_,_,d) in sq)
    A = sum(d*d for (_,_,d) in sq)
    g = N - A
    s = sum((1-d)**2 for (_,_,d) in sq)
    return S, g, s

def column_packing(k):
    """k+1 squares of side k/(k+1) stacked in column [0, k/(k+1)] x [0,k],
    plus k(k-1) unit squares tiling [1,k] x [0,k]."""
    d = k/(k+1)
    sq = [(0.0, i*d, d) for i in range(k+1)]
    for cx in range(1, k):
        for cy in range(k):
            sq.append((float(cx), float(cy), 1.0))
    return sq

def split_cell(k, a):
    """N-1 units + sides {a, 1-a} stacked in cell [0,1]^2."""
    b = 1-a
    sq = [(0.0, 0.0, a), (0.0, a, b)]
    cells = [(cx,cy) for cx in range(k) for cy in range(k)][1:]
    for (cx,cy) in cells:
        sq.append((float(cx), float(cy), 1.0))
    return sq

def stack_gadget(k, sides, x0=0.0):
    """Stack of len(sides) squares (sum(sides)=h integer <= k) at bottom of
    strip 0, k-h units above, plus k(k-1) units in strips 1..k-1."""
    h = sum(sides)
    assert abs(h - round(h)) < 1e-12 and max(sides) <= 1
    h = round(h)
    sq = []
    y = 0.0
    for d in sides:
        sq.append((x0, y, d)); y += d
    for j in range(h, k):
        sq.append((x0, float(j), 1.0))
    for cx in range(1, k):
        for cy in range(k):
            sq.append((float(cx), float(cy), 1.0))
    return sq

print("=== 1. Column packing counterexamples ===")
for k in range(1, 7):
    sq = column_packing(k)
    check_packing(sq, k)
    assert len(sq) == k*k+1
    S, g, s = stats(sq, k)
    Av, maxC = exact_Av(sq, k)
    print(f"k={k}: n={len(sq)}, Sum d={S:.6f} (N={k*k}), g={g:.6f}, s={s:.6f}, "
          f"g+s={g+s:.6f}, |Av|={Av:.6f}, pred k/(k+1)={k/(k+1):.6f}, "
          f"FCMB rhs s={s:.6f}, VIOLATION={Av - s:.6f}, maxC={maxC}")

print("\n=== 2. Grid cross-check (k=2,3) ===")
for k in (2,3):
    sq = column_packing(k)
    Avg, maxC = grid_Av(sq, k, n=2001)
    print(f"k={k}: grid |Av|={Avg:.6f}, maxC={maxC}")

print("\n=== 3. Split-cell tightness check ===")
for k in (2,3):
    for a in (0.37, 0.5, 0.8):
        sq = split_cell(k, a)
        check_packing(sq, k)
        S, g, s = stats(sq, k)
        Av, maxC = exact_Av(sq, k)
        print(f"k={k} a={a}: |Av|={Av:.6f}, s={s:.6f}, diff={Av-s:+.6f}")

print("\n=== 4. Stack-gadget formula |Av| = d(1) + (d(2)-d(1))(1-d(1)) ===")
random.seed(1)
tests = [(3, [0.9,0.9,0.9,0.3]), (3, [0.8,0.7,0.6,0.9]), (4, [0.75]*4 ,),
         (4, [0.5,0.9,0.8,0.8,1.0]), (2, [0.6,0.7,0.7])]
for (k, sides) in tests:
    h = sum(sides)
    if abs(h - round(h)) > 1e-9:
        print(f"skip {sides} (h={h})"); continue
    sq = stack_gadget(k, sides)
    check_packing(sq, k)
    assert len(sq) == k*k+1, (len(sq), k)
    ds = sorted(sides)
    pred = ds[0] + (ds[1]-ds[0])*(1-ds[0])
    S, g, s = stats(sq, k)
    Av, maxC = exact_Av(sq, k)
    print(f"k={k} sides={sides}: |Av|={Av:.6f}, formula={pred:.6f}, s={s:.6f}, "
          f"g+s={g+s:.6f}, viol={Av-s:+.6f}")
