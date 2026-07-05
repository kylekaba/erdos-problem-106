"""Independent adversarial verification of F5 Claims 4 (Theorem C'') and 5 (Theorem W).
All code written from scratch (not reusing F5's helpers except conceptually).
"""
import numpy as np
from itertools import combinations

rng = np.random.default_rng(20260704)

# ---------- geometry primitives ----------
def mk_square(x0, y0, d, th):
    """square with 'lowest' vertex at (x0+d sin th, y0); bbox = [x0,x0+w]x[y0,y0+w]"""
    s, c = np.sin(th), np.cos(th)
    w = d*(c+s)
    V = np.array([[d*s, 0],[w, d*s],[d*c, w],[0, d*c]]) + np.array([x0, y0])
    return V

def mk_square_center(cx, cy, d, th):
    s, c = np.sin(th), np.cos(th)
    h = d/2
    V = np.array([[-h,-h],[h,-h],[h,h],[-h,h]])
    R = np.array([[c,-s],[s,c]])
    return V@R.T + np.array([cx,cy])

def inside(pts, V, eps=1e-11):
    m = np.ones(len(pts), bool)
    for i in range(4):
        a, b = V[i], V[(i+1)%4]
        m &= (b[0]-a[0])*(pts[:,1]-a[1]) - (b[1]-a[1])*(pts[:,0]-a[0]) > eps
    return m

def sat_disjoint(V1, V2):
    for P, O in ((V1,V2),(V2,V1)):
        for i in range(4):
            a, b = P[i], P[(i+1)%4]
            n = np.array([a[1]-b[1], b[0]-a[0]])
            if O@n.T is None: pass
            if (O@n).min() >= (P@n).max() - 1e-12 or (O@n).max() <= (P@n).min() + 1e-12:
                return True
    return False

def nlines(lo, hi, ph):
    """# of lines ph+Z meeting [lo,hi]"""
    return int(np.floor(hi-ph) - np.ceil(lo-ph) + 1)

def clat(V, x, y):
    """lattice points of (x,y)+Z^2 strictly inside polygon V"""
    xs = np.arange(np.floor(V[:,0].min())-1, np.ceil(V[:,0].max())+2)
    ys = np.arange(np.floor(V[:,1].min())-1, np.ceil(V[:,1].max())+2)
    X, Y = np.meshgrid(xs+x, ys+y)
    pts = np.column_stack([X.ravel(), Y.ravel()])
    return int(inside(pts, V).sum())

def bad_iv(V, d, th, axis):
    s = d*np.sin(th)
    if s <= 1e-15: return []
    lo, hi = V[:,axis].min(), V[:,axis].max()
    return [(lo % 1.0, s), ((hi-s) % 1.0, s)]

def umeas(ivs, grid=None):
    if not ivs: return 0.0
    segs = []
    for a,l in ivs:
        l = min(l,1.0)
        if a+l <= 1: segs.append((a,a+l))
        else: segs.append((a,1.0)); segs.append((0.0,a+l-1.0))
    segs.sort(); tot=0; ca,cb = segs[0]
    for a,b in segs[1:]:
        if a > cb: tot += cb-ca; ca,cb=a,b
        else: cb = max(cb,b)
    return min(tot + cb-ca, 1.0)

def in_ivs(v, ivs):
    return any((v-a) % 1.0 < l for a,l in ivs)

# ============================================================
# A. Fact 4.0: triangle geometry + product structure, exhaustive random
# ============================================================
print("=== A. Fact 4.0: corner-triangle geometry (independent brute force) ===")
viol_geom = 0; viol_prod = 0; tested = 0
for trial in range(400):
    d = rng.uniform(0.2, 2.8); th = rng.uniform(1e-3, np.pi/4)
    x0, y0 = rng.uniform(0, 3, 2)
    V = mk_square(x0, y0, d, th)
    s, c = d*np.sin(th), d*np.cos(th); w = s+c
    # (A1) points in bbox \ square: tall triangles have x in [x0,x0+s]u[x0+c,x0+w],
    #      wide have y in [y0,y0+s]u[y0+c,y0+w]; every such pt in one of these
    P = np.column_stack([rng.uniform(x0, x0+w, 3000), rng.uniform(y0, y0+w, 3000)])
    out = P[~inside(P, V, eps=1e-9)]
    for p in out:
        in_tallx = (p[0] <= x0+s+1e-9) or (p[0] >= x0+c-1e-9)
        in_widey = (p[1] <= y0+s+1e-9) or (p[1] >= y0+c-1e-9)
        if not (in_tallx or in_widey): viol_geom += 1
    # (A2) product structure: L>=1 => phase bad
    bx, by = bad_iv(V, d, th, 0), bad_iv(V, d, th, 1)
    for _ in range(60):
        x, y = rng.random(2)
        p = nlines(V[:,0].min(), V[:,0].max(), x)
        q = nlines(V[:,1].min(), V[:,1].max(), y)
        cc = clat(V, x, y)
        tested += 1
        if p*q - cc >= 1 and not (in_ivs(x, bx) or in_ivs(y, by)):
            viol_prod += 1
print(f"  geometry violations: {viol_geom}/1.2M pts;  product-structure violations: {viol_prod}/{tested}")

# ============================================================
# B. Theorem C'' on packings (mine, fresh)
# ============================================================
def check_packing(name, polys, dths, k, ng=2000):
    N = k*k; M = len(polys)
    assert M == N+1, f"{name}: M={M} != N+1={N+1}"
    for V in polys:
        assert V.min() > -1e-9 and V.max() < k+1e-9, f"{name}: containment FAIL"
    for i,j in combinations(range(M),2):
        assert sat_disjoint(polys[i], polys[j]), f"{name}: overlap {i},{j}"
    ws = np.array([d*(np.cos(t)+np.sin(t)) for d,t in dths])
    gam = np.maximum(0, 1-ws); sg = gam.sum()
    BX = [bad_iv(polys[i], *dths[i], 0) for i in range(M)]
    BY = [bad_iv(polys[i], *dths[i], 1) for i in range(M)]
    Ux, Uy = umeas([iv for b in BX for iv in b]), umeas([iv for b in BY for iv in b])
    # P(x), Q(y) on fine grid; A, B, and A\UBx, B\UBy
    xs = (np.arange(ng)+0.5)/ng
    xmin = np.array([V[:,0].min() for V in polys]); xmax = np.array([V[:,0].max() for V in polys])
    ymin = np.array([V[:,1].min() for V in polys]); ymax = np.array([V[:,1].max() for V in polys])
    P = np.array([sum(nlines(xmin[i], xmax[i], x) for i in range(M)) for x in xs])
    Q = np.array([sum(nlines(ymin[i], ymax[i], y) for i in range(M)) for y in xs])
    A = P >= N+1; B = Q >= N+1
    inUx = np.array([in_ivs(x, [iv for b in BX for iv in b]) for x in xs])
    inUy = np.array([in_ivs(y, [iv for b in BY for iv in b]) for y in xs])
    mA, mB = A.mean(), B.mean()
    mAfree, mBfree = (A & ~inUx).mean(), (B & ~inUy).mean()
    # budget check at random 2-D shifts + Sum c_i <= N
    worst = -1
    for _ in range(300):
        x, y = rng.random(2)
        tot = sum(clat(polys[i], x, y) for i in range(M))
        worst = max(worst, tot)
    lhs = sg + max(Ux, Uy)
    t = ws.sum() - N; eps_ = sum(d for d,_ in dths) - N
    rhs2 = t - np.maximum(0, ws-1).sum()   # should equal 1 - sg
    print(f"--- {name} (k={k}) ---")
    print(f"  sum(1-w)+ = {sg:.4f}  Ux={Ux:.4f}  Uy={Uy:.4f}  ->  C'' LHS = {lhs:.4f}  {'PASS' if lhs>=1-2e-3 else '*** FAIL ***'}")
    print(f"  |A|={mA:.4f} >= 1-sg={max(0,1-sg):.4f}: {'PASS' if mA >= (1-sg)-2e-3 else 'FAIL'};  identity t-sum(w-1)+ = {rhs2:.4f} vs 1-sg = {1-sg:.4f}")
    print(f"  chain: eps - sum(d-1)+ = {eps_ - sum(max(0,d-1) for d,_ in dths):.4f} <= {rhs2:.4f} : "
          f"{'PASS' if eps_ - sum(max(0,d-1) for d,_ in dths) <= rhs2 + 1e-9 else 'FAIL'}")
    print(f"  emptiness prediction min(|A\\UBx|,|B\\UBy|) = {min(mAfree,mBfree):.4f}  (must be 0)"
          f"  {'PASS' if min(mAfree,mBfree) < 2e-3 else '*** FAIL ***'}")
    print(f"  budget max sum c_i over 300 shifts = {worst} <= N = {N}: {'PASS' if worst <= N else 'FAIL'}")
    return dict(sg=sg, Ux=Ux, Uy=Uy)

print("\n=== B. Theorem C'' on 3 fresh packings ===")
# P1: k=2, rotated 2x2 block (side .95, tilt .05) + tiny corner square
t = 0.05
polys, dths = [], []
for dx in (-0.475, 0.475):
    for dy in (-0.475, 0.475):
        R = np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])
        cc = np.array([1,1]) + R@np.array([dx,dy])
        polys.append(mk_square_center(cc[0], cc[1], 0.95, t)); dths.append((0.95,t))
polys.append(mk_square_center(0.035,0.035,0.05,0)); dths.append((0.05,0.0))
check_packing("P1 rotated block k=2", polys, dths, 2)

# P2: k=3 deficient column (FCMB refutation family): 4 squares side 3/4 + 6 units
polys, dths = [], []
for j in range(4):
    polys.append(mk_square(0, 0.75*j, 0.75, 0)); dths.append((0.75,0.0))
for cx in (0.75, 1.75):
    for cy in (0,1,2):
        polys.append(mk_square(cx, cy, 1.0, 0)); dths.append((1.0,0.0))
r = check_packing("P2 deficient column k=3", polys, dths, 3)

# FCMB refutation arithmetic in passing: |Av| and s for P2
ng = 400
Av = 0
for xi in range(ng):
    for yi in range(ng):
        x, y = (xi+0.5)/ng, (yi+0.5)/ng
        tot = sum(clat(V, x, y) for V in polys)
        if tot == 9: Av += 1
s_stat = sum((1-d)**2 for d,_ in dths)
print(f"  [FCMB re-check] |Av| ~= {Av/ng**2:.4f} (claim k/(k+1)={3/4}),  s = {s_stat:.4f} (claim 1/(k+1)={0.25}),"
      f"  |Av|>s: {'CONFIRMED REFUTATION' if Av/ng**2 > s_stat else 'NOT confirmed'}")

# P3: k=3 mixed: big tilted 1.3 @ 0.35, five units, four small tilted 0.28 @ 0.05
polys, dths = [], []
polys.append(mk_square(0.01, 0.01, 1.3, 0.35)); dths.append((1.3,0.35))
for (x0,y0) in [(2,0),(2,1),(2,2),(1,2),(0,2)]:
    polys.append(mk_square(x0,y0,1.0,0)); dths.append((1.0,0.0))
for j in range(4):
    polys.append(mk_square(1.70, 0.02+0.31*j, 0.28, 0.05)); dths.append((0.28,0.05))
check_packing("P3 mixed k=3", polys, dths, 3)

# ============================================================
# C. Theorem W: fattening bound + kill arithmetic
# ============================================================
print("\n=== C. Theorem W ===")
# coherent whisper near-grid, k=6: 36 squares side dbar rotated by t0 as rigid block + 1 tiny
k = 6; N = k*k
t0 = 1/(2*k*k)
dbar = 0.985
polys, dths = [], []
R = np.array([[np.cos(t0),-np.sin(t0)],[np.sin(t0),np.cos(t0)]])
c0 = np.array([k/2, k/2])
for a in range(k):
    for b in range(k):
        cc = c0 + R@(np.array([a+0.5,b+0.5])*dbar*1.001 - np.array([k/2,k/2])*dbar*1.001)
        polys.append(mk_square_center(cc[0],cc[1],dbar,t0)); dths.append((dbar,t0))
polys.append(mk_square_center(k-0.03,k-0.03,0.04,0)); dths.append((0.04,0.0))
for i,j in combinations(range(len(polys)),2):
    assert sat_disjoint(polys[i],polys[j]), f"W-grid overlap {i},{j}"
assert all(V.min()>-1e-9 and V.max()<k+1e-9 for V in polys)
M = len(polys)
BX = [bad_iv(polys[i],*dths[i],0) for i in range(M)]
Ux = umeas([iv for b in BX for iv in b])
# phase cover: bbox-min and bbox-max phases per axis
ph = sorted(set([V[:,0].min()%1 for V in polys] + [V[:,0].max()%1 for V in polys]))
# greedy: cover with 2 arcs -> find 2 largest circular gaps
gaps = [( (ph[(i+1)%len(ph)]-ph[i])%1.0, i) for i in range(len(ph))]
gaps.sort(reverse=True)
lam2 = 1.0 - gaps[0][0] - gaps[1][0]   # cover by K=2 arcs, total length
smax = max(d*np.sin(t) for d,t in dths)
print(f"  coherent near-grid k=6, t0={t0:.5f}: actual U_x = {Ux:.4f}")
print(f"  PH(2,lambda): lambda = {lam2:.4f};  W bound lambda + 2K smax = {lam2 + 4*smax:.4f} >= U_x: "
      f"{'PASS' if lam2 + 4*smax >= Ux - 1e-9 else '*** FAIL ***'}")
# kill arithmetic
c = 1/400
for kk in (10, 20):
    lhs = 4*np.sqrt(2*c) + 1/kk + 13/kk**2
    print(f"  kill arithmetic c=1/400, k={kk}: LHS = {lhs:.5f}  vs 1/2-c = {0.5-c:.5f}"
          f"  -> {'DEAD (margin %.3f)' % (0.5-c-lhs) if lhs <= 0.5-c else 'not killed (marginal)'}")
# exact terms at k=20
print(f"  4*sqrt(2c) = {4*np.sqrt(2*c):.5f}; 1/20 = 0.05; 13/400 = {13/400:.5f}; total {4*np.sqrt(2*c)+0.05+13/400:.5f}")
# fattening term honesty: 2K(max d) sin t0 with K=2, max d = 1+sqrt(2c)+1/k^2, t0 <= 1/(2k^2)
for kk in (10,20):
    ft = 4*(1+np.sqrt(2*c)+1/kk**2)*np.sin(1/(2*kk**2))
    print(f"  fattening term k={kk}: 2K(maxd)sin t0 = {ft:.6f} vs budgeted 9/k^2 = {9/kk**2:.6f} : "
          f"{'covered' if ft <= 9/kk**2 else 'NOT covered'}")

# ============================================================
# D. equivalence-chain identity on random data
# ============================================================
print("\n=== D. identity/chain spot-check on random (d,theta) ===")
bad = 0
for _ in range(20000):
    m = rng.integers(2, 12)
    d = rng.uniform(0.1, 2.5, m); th = rng.uniform(0, np.pi/4, m)
    w = d*(np.cos(th)+np.sin(th)); Nn = m-1
    t = w.sum()-Nn
    lhs1 = 1 - np.maximum(0,1-w).sum(); rhs1 = t - np.maximum(0,w-1).sum()
    if abs(lhs1-rhs1) > 1e-9: bad += 1
    if (d.sum()-Nn) - np.maximum(0,d-1).sum() > rhs1 + 1e-9: bad += 1
print(f"  identity 1-sum(1-w)+ == t-sum(w-1)+ and chain >= eps-sum(d-1)+ : violations = {bad}/20000")
