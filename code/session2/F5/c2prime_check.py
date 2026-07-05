"""Verify Theorem C'' (union-bad-set counting bound) and its ingredients.

Theorem C'': for every packing of N+1 squares in [0,k]^2,
    sum_i (1 - w_i)_+  +  max(U_x, U_y)  >=  1,
where w_i = d_i(cos t_i + sin t_i) (folded tilt t_i), U_x = |union_i B_i^x|,
B_i^x = the two tall-corner-triangle x-phase intervals of square i (each of
length d_i sin t_i, at the bbox-left and bbox-right ends), U_y likewise.

Ingredients checked numerically on a genuine mixed packing:
 (I1) {L_i >= 1} subset (B_i^x x T) u (T x B_i^y)   [per-square product structure]
 (I2) |A| >= 1 - sum gamma_i  where A = {P >= N+1}, gamma_i = (1-w_i)_+
 (I3) the disjunction: |A| <= U_x or |B| <= U_y  (else contradiction)
 (I4) the inequality of C'' itself.
Also checked on the split-cell extremal (tightness) and a coherent-grain packing.
"""
import numpy as np
from itertools import combinations

def square(cx, cy, d, th):
    hs = d / 2
    c = np.array([[-hs, -hs], [hs, -hs], [hs, hs], [-hs, hs]])
    R = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
    return c @ R.T + np.array([cx, cy])

def sat_disjoint(p1, p2):
    for poly, other in ((p1, p2), (p2, p1)):
        for i in range(4):
            a = poly[i]; b = poly[(i+1) % 4]
            n = np.array([-(b[1]-a[1]), b[0]-a[0]])
            if max(other @ n) <= min(poly @ n) + 1e-12 or min(other @ n) >= max(poly @ n) - 1e-12:
                return True
    return False

def in_poly(pts, poly):
    m = np.ones(len(pts), bool)
    for i in range(4):
        a = poly[i]; b = poly[(i+1) % 4]
        cr = (b[0]-a[0])*(pts[:,1]-a[1]) - (b[1]-a[1])*(pts[:,0]-a[0])
        m &= cr > 1e-12   # strict interior
    return m

def count_lattice_in_poly(poly, x, y, k):
    xs = np.arange(np.floor(poly[:,0].min()) - 1, np.ceil(poly[:,0].max()) + 2)
    ys = np.arange(np.floor(poly[:,1].min()) - 1, np.ceil(poly[:,1].max()) + 2)
    XX, YY = np.meshgrid(xs + x, ys + y)
    pts = np.column_stack([XX.ravel(), YY.ravel()])
    return int(in_poly(pts, poly).sum())

def bad_intervals_axis(poly, d, th, axis):
    """x-phase intervals (mod 1) of the two tall triangles (axis=0) or
    y-phase intervals of the two wide triangles (axis=1); th = folded tilt."""
    s = d * np.sin(th)
    if s <= 0:
        return []
    lo = poly[:, axis].min(); hi = poly[:, axis].max()
    return [(lo % 1.0, s), ((hi - s) % 1.0, s)]   # (start mod 1, length)

def union_measure(ivs):
    if not ivs:
        return 0.0
    segs = []
    for (a, l) in ivs:
        l = min(l, 1.0)
        if a + l <= 1:
            segs.append((a, a + l))
        else:
            segs.append((a, 1.0)); segs.append((0.0, a + l - 1.0))
    segs.sort()
    tot, cur_a, cur_b = 0.0, segs[0][0], segs[0][1]
    for a, b in segs[1:]:
        if a > cur_b:
            tot += cur_b - cur_a; cur_a, cur_b = a, b
        else:
            cur_b = max(cur_b, b)
    tot += cur_b - cur_a
    return min(tot, 1.0)

def in_intervals(v, ivs):
    for (a, l) in ivs:
        if (v - a) % 1.0 < l:
            return True
    return False

def analyze(name, polys, dths, k, ngrid=600):
    N = k * k
    M = len(polys)
    assert M == N + 1
    # containment & disjointness
    for p in polys:
        assert p.min() >= -1e-9 and p.max() <= k + 1e-9, f"{name}: outside container"
    for i, j in combinations(range(M), 2):
        assert sat_disjoint(polys[i], polys[j]), f"{name}: overlap {i},{j}"
    ws = np.array([d * (np.cos(t) + np.sin(t)) for d, t in dths])
    gammas = np.maximum(0.0, 1.0 - ws)
    badx = [bad_intervals_axis(polys[i], *dths[i], 0) for i in range(M)]
    bady = [bad_intervals_axis(polys[i], *dths[i], 1) for i in range(M)]
    Ux = union_measure([iv for b in badx for iv in b])
    Uy = union_measure([iv for b in bady for iv in b])
    # shift grid: P, Q, and I1 check
    shifts = (np.arange(ngrid) + 0.383) / ngrid
    xmins = np.array([p[:,0].min() for p in polys]); xmaxs = np.array([p[:,0].max() for p in polys])
    ymins = np.array([p[:,1].min() for p in polys]); ymaxs = np.array([p[:,1].max() for p in polys])
    P = np.zeros(ngrid, int); Q = np.zeros(ngrid, int)
    for ii, x in enumerate(shifts):
        P[ii] = int(sum(np.floor(xmaxs - x) - np.ceil(xmins - x) + 1))
        Q[ii] = int(sum(np.floor(ymaxs - x) - np.ceil(ymins - x) + 1))
    A = P >= N + 1; B = Q >= N + 1
    mA, mB = A.mean(), B.mean()
    # I1: sample 2-D shifts, check L_i>=1 => bad
    rng = np.random.default_rng(1)
    viol_I1 = 0
    for _ in range(4000):
        x, y = rng.random(2)
        for i in range(M):
            d, t = dths[i]
            if t == 0:
                continue
            p_i = int(np.floor(xmaxs[i]-x) - np.ceil(xmins[i]-x) + 1)
            q_i = int(np.floor(ymaxs[i]-y) - np.ceil(ymins[i]-y) + 1)
            c_i = count_lattice_in_poly(polys[i], x, y, k)
            L_i = p_i * q_i - c_i
            if L_i >= 1 and not (in_intervals(x, badx[i]) or in_intervals(y, bady[i])):
                viol_I1 += 1
    sg = gammas.sum()
    lhs = sg + max(Ux, Uy)
    print(f"--- {name} (k={k}, M={M}) ---")
    print(f"  sum gamma = {sg:.4f}   Ux = {Ux:.4f}   Uy = {Uy:.4f}")
    print(f"  C'' LHS = sum gamma + max(U) = {lhs:.4f}  >= 1 ?  {'PASS' if lhs >= 1 - 5e-3 else 'FAIL'}")
    print(f"  |A| = {mA:.4f} (>= 1 - sum gamma = {max(0,1-sg):.4f} ? "
          f"{'PASS' if mA >= (1-sg) - 5e-3 else 'FAIL'})   |B| = {mB:.4f}")
    print(f"  disjunction (|A|<=Ux or |B|<=Uy): "
          f"{'HOLDS' if (mA <= Ux + 5e-3 or mB <= Uy + 5e-3) else 'VIOLATED (theorem falsified!)'}")
    print(f"  I1 (L>=1 => bad shift) violations: {viol_I1}")

# Packing 1: split-cell extremal, k=2 (tightness: sum gamma = 1, U = 0)
a = 0.37
polys1, dths1 = [], []
for (cx, cy, d, t) in [(0.5,0.5,1,0),(1.5,0.5,1,0),(0.5,1.5,1,0),
                        (1+a/2, 1+a/2, a, 0), (1+(1+a)/2 if False else 1+a+(1-a)/2, 1+(1-a)/2, 1-a, 0)]:
    polys1.append(square(cx, cy, d, t)); dths1.append((d, t))
analyze("split-cell (a=0.37)", polys1, dths1, 2)

# Packing 2: mixed 5-square packing in [0,2]^2: 3 units + 0.75@0.3rad + small
polys2, dths2 = [], []
for (cx, cy, d, t) in [(0.5,0.5,1,0),(1.5,0.5,1,0),(0.5,1.5,1,0),
                        (1.5,1.5,0.75,0.3)]:
    polys2.append(square(cx, cy, d, t)); dths2.append((d, t))
# small square tucked in the lower-left corner triangle region of the tilted bbox
small = square(1.075, 1.075, 0.09, 0.0)
polys2.append(small); dths2.append((0.09, 0.0))
analyze("mixed 5-square", polys2, dths2, 2)

# Packing 3: coherent tilted 2x2 grain (t=0.12) + axis-parallel filler, k=3, 10 squares
t = 0.12
polys3, dths3 = [], []
# grain: 2x2 block of unit squares tilted by t, occupying rotated 2x2 square anchored at corner
c0 = np.array([1.13, 1.13])   # center of the 2x2 rotated block
R = np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
for dx in (-0.5, 0.5):
    for dy in (-0.5, 0.5):
        cc = c0 + R @ np.array([dx, dy])
        polys3.append(square(cc[0], cc[1], 0.999, t)); dths3.append((0.999, t))
# filler: 6 axis-parallel squares in the remaining L-shape of [0,3]^2
for (cx, cy, d) in [(2.63,0.36,0.7),(2.63,1.08,0.7),(2.63,1.80,0.7),
                     (2.63,2.52,0.7),(0.36,2.63,0.7),(1.08,2.63,0.7)]:
    polys3.append(square(cx, cy, d, 0.0)); dths3.append((d, 0.0))
analyze("2x2 grain t=0.12 + filler", polys3, dths3, 3)
