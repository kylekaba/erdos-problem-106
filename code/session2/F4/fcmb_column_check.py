"""
F4: FCMB counterexample check — the deficient-column packing.

Packing (k >= 1), n = k^2+1 squares, ALL AXIS-PARALLEL:
  - one column: k+1 squares of side c = k/(k+1), lower-left (0, r*c), r=0..k
    (exactly tiles [0,c] x [0,k])
  - units: (k-1)*k unit squares filling [1,k] x [0,k]
  Gap G = [c,1] x [0,k], a vertical sliver of width w = 1/(k+1), area g = k/(k+1).
  s = (k+1)*(1-c)^2 = 1/(k+1).
  Claim: Av = {p : C(p)=N} = {p1 < c}, |Av| = k/(k+1) > s = 1/(k+1) for k>=2.
  => FCMB (|Av| <= s) is FALSE for every k >= 2.

Also: validation of the harness on the split-cell family (known tight),
tilted perturbation of the column (violation is robust/open),
and check of Lemma L1 (|A_v| = covered area of cell v).
"""
import numpy as np

def contains(sq, X, Y, eps=0.0):
    """sq = (x0, y0, d, theta, cx, cy). theta=0: AP with lower-left (x0,y0).
       theta!=0: square of side d centered (cx,cy) rotated by theta."""
    x0, y0, d, th, cx, cy = sq
    if th == 0.0:
        return (X >= x0 + eps) & (X <= x0 + d - eps) & (Y >= y0 + eps) & (Y <= y0 + d - eps)
    ct, st = np.cos(th), np.sin(th)
    U = ct * (X - cx) + st * (Y - cy)
    V = -st * (X - cx) + ct * (Y - cy)
    return (np.abs(U) <= d / 2 - eps) & (np.abs(V) <= d / 2 - eps)

def corners(sq):
    x0, y0, d, th, cx, cy = sq
    if th == 0.0:
        return np.array([[x0, y0], [x0 + d, y0], [x0 + d, y0 + d], [x0, y0 + d]])
    ct, st = np.cos(th), np.sin(th)
    R = np.array([[ct, -st], [st, ct]])
    base = np.array([[-d/2, -d/2], [d/2, -d/2], [d/2, d/2], [-d/2, d/2]])
    return base @ R.T + np.array([cx, cy])

def sat_disjoint(sqA, sqB, tol=1e-12):
    """Separating-axis test: True if interiors disjoint (convex polygons)."""
    CA, CB = corners(sqA), corners(sqB)
    for C1, C2 in ((CA, CB), (CB, CA)):
        for e in range(4):
            p, q = C1[e], C1[(e + 1) % 4]
            n = np.array([q[1] - p[1], p[0] - q[0]])
            if C2 @ n .T is None:
                pass
            a1, a2 = (C1 @ n).min(), (C1 @ n).max()
            b1, b2 = (C2 @ n).min(), (C2 @ n).max()
            if b1 >= a2 - tol or a1 >= b2 - tol:
                return True
    return False

def validate_packing(sqs, k, tol=1e-9):
    ok = True
    for sq in sqs:
        C = corners(sq)
        if C.min() < -tol or C.max() > k + tol:
            ok = False
    for i in range(len(sqs)):
        for j in range(i + 1, len(sqs)):
            if not sat_disjoint(sqs[i], sqs[j]):
                ok = False
    return ok

def measure_Av(sqs, k, M=800):
    """|{p in [0,1)^2 : C(p) = k^2}| on an MxM offset grid (midpoints)."""
    N = k * k
    t = (np.arange(M) + 0.5) / M
    P1, P2 = np.meshgrid(t, t, indexing="ij")
    Ccount = np.zeros((M, M), dtype=int)
    for v1 in range(k):
        for v2 in range(k):
            X, Y = P1 + v1, P2 + v2
            cov = np.zeros((M, M), dtype=bool)
            for sq in sqs:
                cov |= contains(sq, X, Y)
            Ccount += cov
    assert Ccount.max() <= N, "budget violated!"
    return (Ccount == N).mean(), Ccount

def stats(sqs, k):
    d = np.array([sq[2] for sq in sqs])
    N = k * k
    return dict(n=len(sqs), sumd=d.sum(), g=N - (d**2).sum(), s=((1 - d)**2).sum())

def AP(x0, y0, d):
    return (x0, y0, d, 0.0, x0 + d / 2, y0 + d / 2)

def column_packing(k):
    c = k / (k + 1)
    sqs = [AP(0.0, r * c, c) for r in range(k + 1)]
    for a in range(k - 1):
        for b in range(k):
            sqs.append(AP(1.0 + a, float(b), 1.0))
    return sqs

def column_packing_tilted(k, t):
    """Column squares tilted by t about their centers, shrunk to c/u1(t) so
       bounding boxes stay inside the original c x c cells (still disjoint)."""
    c = k / (k + 1)
    u1 = np.cos(t) + np.sin(t)
    d = c / u1
    sqs = []
    for r in range(k + 1):
        cx, cy = c / 2, r * c + c / 2
        sqs.append((0.0, 0.0, d, t, cx, cy))
    for a in range(k - 1):
        for b in range(k):
            sqs.append(AP(1.0 + a, float(b), 1.0))
    return sqs

def split_cell_packing(k, a):
    """Validation family: (N-1) units + {a, 1-a} split in the last cell."""
    sqs = []
    for i in range(k):
        for j in range(k):
            if (i, j) == (k - 1, k - 1):
                continue
            sqs.append(AP(float(i), float(j), 1.0))
    b = 1 - a
    sqs.append(AP(k - 1.0, k - 1.0, a))
    sqs.append(AP(k - 1.0 + a, k - 1.0 + a, b))
    return sqs

print("=" * 72)
print("HARNESS VALIDATION: split-cell family (known: |Av| = a^2+b^2 = s, tight)")
for k, a in [(2, 0.37), (3, 0.5)]:
    sqs = split_cell_packing(k, a)
    st = stats(sqs, k)
    assert validate_packing(sqs, k), "invalid packing"
    Av, _ = measure_Av(sqs, k, M=1000)
    exact = a**2 + (1 - a)**2
    print(f"k={k} a={a}: n={st['n']}  |Av|={Av:.6f}  exact a^2+b^2={exact:.6f}  "
          f"s={st['s']:.6f}  FCMB slack s-|Av| = {st['s']-Av:+.6f}")

print("=" * 72)
print("MAIN CHECK: deficient-column packing (AP)")
for k in [1, 2, 3, 4]:
    sqs = column_packing(k)
    st = stats(sqs, k)
    assert st['n'] == k * k + 1, (st, k)
    assert validate_packing(sqs, k), "invalid packing"
    M = 1200 if k <= 3 else 700
    Av, Cc = measure_Av(sqs, k, M=M)
    c = k / (k + 1)
    print(f"k={k}: n={st['n']}, sum d={st['sumd']:.6f} (N={k*k}), "
          f"g={st['g']:.6f}, s={st['s']:.6f}, g+s={st['g']+st['s']:.6f}")
    print(f"      |Av| (grid {M}^2) = {Av:.6f}   exact prediction c = {c:.6f}")
    print(f"      FCMB requires |Av| <= s = {st['s']:.6f}  ==> "
          f"{'VIOLATED by ' + format(Av - st['s'], '.6f') if Av > st['s'] + 1e-6 else 'holds/tight'}")
    # hits distribution: predicted two-point {0, k}
    hits = k * k - Cc
    vals, cnts = np.unique(hits, return_counts=True)
    print(f"      hits distribution: {dict(zip(vals.tolist(), (cnts/cnts.sum()).round(6).tolist()))}")

print("=" * 72)
print("ROBUSTNESS: tilted column (t=0.02 and t=0.05), squares shrunk to c/u1(t)")
for k in [2, 3]:
    for t in [0.02, 0.05]:
        sqs = column_packing_tilted(k, t)
        st = stats(sqs, k)
        assert validate_packing(sqs, k), "invalid packing"
        Av, _ = measure_Av(sqs, k, M=1000)
        print(f"k={k} t={t}: sum d={st['sumd']:.5f}, s={st['s']:.5f}, "
              f"|Av|={Av:.5f}  ==> {'VIOLATED by ' + format(Av-st['s'],'.5f') if Av > st['s'] else 'holds'}")

print("=" * 72)
print("LEMMA L1 CHECK (column, k=2): |A_v| = covered area of cell C_v;  Av = inter A_v")
k = 2
sqs = column_packing(k)
M = 1200
t_ = (np.arange(M) + 0.5) / M
P1, P2 = np.meshgrid(t_, t_, indexing="ij")
inter = np.ones((M, M), dtype=bool)
for v1 in range(k):
    for v2 in range(k):
        X, Y = P1 + v1, P2 + v2
        cov = np.zeros((M, M), dtype=bool)
        for sq in sqs:
            cov |= contains(sq, X, Y)
        inter &= cov
        # covered area of cell v via the same grid (shift-average = area, exact here)
        print(f"  v=({v1},{v2}): |A_v| = {cov.mean():.6f}   "
              f"(exact covered area of cell = {2/3 if v1==0 else 1.0:.6f})")
Av_direct, _ = measure_Av(sqs, k, M=M)
print(f"  |inter A_v| = {inter.mean():.6f}  vs |Av| = {Av_direct:.6f}  (must agree)")
