import numpy as np, math
rng = np.random.default_rng(42)

def verts(z, s, a):
    R = np.array([[math.cos(a), -math.sin(a)],[math.sin(a), math.cos(a)]])
    base = np.array([[1,1],[-1,1],[-1,-1],[1,-1]]) * s/2.0
    return z + base @ R.T

def chord_at(P, y):
    xs = []
    n = len(P)
    for i in range(n):
        a, b = P[i], P[(i+1)%n]
        if (a[1]-y)*(b[1]-y) <= 0 and a[1] != b[1]:
            t = (y - a[1])/(b[1]-a[1])
            xs.append(a[0] + t*(b[0]-a[0]))
    if len(xs) < 2: return 0.0
    return max(xs) - min(xs)

print("=== CHECK 1: chord(y) <= 2(y-y_v)/sin(2 tau), equality for y-y_v <= d sin tau ===")
bad = 0; eqbad = 0
for _ in range(3000):
    d = rng.uniform(0.5, 2.0); tau = rng.uniform(1e-3, math.pi/4)
    P = verts(np.array([0.0,0.0]), d, tau)
    yv = P[:,1].min()
    for y in np.linspace(yv+1e-9, P[:,1].max()-1e-9, 23):
        c = chord_at(P, y); bnd = 2*(y-yv)/math.sin(2*tau)
        if c > bnd + 1e-7: bad += 1
        if y - yv <= d*math.sin(tau) - 1e-6 and abs(c - bnd) > 1e-6: eqbad += 1
print("violations:", bad, "| equality failures in wedge range:", eqbad)

print("=== CHECK 1b: area(S cap {y<=Y}) == (Y-y_v)^2/sin(2 tau) for Y-y_v <= d sin tau ===")
worst = 0
for _ in range(300):
    d = rng.uniform(0.5, 2.0); tau = rng.uniform(0.05, math.pi/4)
    P = verts(np.array([0.0,0.0]), d, tau)
    yv = P[:,1].min()
    Y = yv + rng.uniform(0, d*math.sin(tau))
    ys = np.linspace(yv, Y, 2001)
    area = np.trapezoid([chord_at(P, y) for y in ys], ys)
    pred = (Y-yv)**2/math.sin(2*tau)
    worst = max(worst, abs(area-pred))
print("max |area - pred| =", worst)

print("=== CHECK 2: window theorem on coherent tilted grid, k=30 ===")
def tilted_grid_squares(k, t):
    R = np.array([[math.cos(t), -math.sin(t)],[math.sin(t), math.cos(t)]])
    sq = []
    M = int(2*k)
    for i in range(-M, M):
        for j in range(-M, M):
            z = R @ np.array([i+0.5, j+0.5])
            P = verts(z, 1.0, t)
            if P.min() >= 0 and P.max() <= k:
                sq.append(P)
    return sq

def point_in_poly_sq(pts, P, ang):
    # squares: rotate back, box test. P has center = mean
    c = P.mean(axis=0)
    R = np.array([[math.cos(-ang), -math.sin(-ang)],[math.sin(-ang), math.cos(-ang)]])
    loc = (pts - c) @ R.T
    # side length from vertices
    s = np.linalg.norm(P[0]-P[1])
    return (np.abs(loc[:,0]) <= s/2) & (np.abs(loc[:,1]) <= s/2)

k = 30
for t in (0.05, 0.2, math.pi/4-0.01):
    sq = tilted_grid_squares(k, t)
    tot = len(sq)
    delta = 0.9*math.sin(t)
    Npts = 400000
    pts = np.column_stack([rng.uniform(0,k,Npts), rng.uniform(0,delta,Npts)])
    cov = np.zeros(Npts, bool)
    for P in sq:
        if P[:,1].min() < delta:
            cov |= point_in_poly_sq(pts, P, t)
    gap = (1-cov.mean())*k*delta
    L = 8.0
    nw = int(k//L)
    bound = nw*delta*(L/2-1.6)
    print(f" t={t:.3f}: squares={tot}, strip gap MC={gap:.3f}, theorem bound={bound:.3f}, ok={gap>=bound}")

print("=== CHECK 3: sector lemma: area(B(x0,r)\\(S1 u S2)) >= alpha r^2, contact configs ===")
def folded(x):
    y = x % (math.pi/2)
    return min(y, math.pi/2 - y)
worst_ratio = np.inf
for trial in range(400):
    th1 = rng.uniform(0, math.pi/2); th2 = rng.uniform(0, math.pi/2)
    al = folded(th2-th1)
    if al < 0.02: continue
    d1, d2 = rng.uniform(0.9,1.1,2)
    # S1 edge through origin along direction th1, S1 below
    n1 = np.array([-math.sin(th1), math.cos(th1)])  # normal pointing up
    z1 = -n1*d1/2 + np.array([math.cos(th1), math.sin(th1)])*rng.uniform(-d1/4, d1/4)
    P1 = verts(z1, d1, th1)
    # S2: vertex at origin, opening into upper half plane: center along rotated diagonal
    diag = np.array([math.cos(th2)-math.sin(th2), math.sin(th2)+math.cos(th2)])/2*d2
    # choose the vertex-diagonal that points most upward among 4
    best = None
    for rot in range(4):
        a2 = th2 + rot*math.pi/2
        dd = np.array([math.cos(a2)-math.sin(a2), math.sin(a2)+math.cos(a2)])/2*d2
        if best is None or dd[1] > best[1]: best = dd
    z2 = best
    P2 = verts(z2, d2, th2)
    # check disjoint-ish: skip if overlap (sample)
    r = rng.uniform(0.05, 0.35)
    Npts = 60000
    ang = rng.uniform(0, 2*math.pi, Npts); rad = r*np.sqrt(rng.uniform(0,1,Npts))
    pts = np.column_stack([rad*np.cos(ang), rad*np.sin(ang)])
    in1 = point_in_poly_sq(pts, P1, th1); in2 = point_in_poly_sq(pts, P2, th2)
    if (in1 & in2).mean() > 1e-4: continue  # overlapping config, skip
    unc = (~in1 & ~in2).mean()*math.pi*r*r
    worst_ratio = min(worst_ratio, unc/(al*r*r))
print("min uncovered/(alpha r^2) over configs =", worst_ratio, "(need >= 1)")

print("=== CHECK 4: staircase interface, alpha=0.15: disjointness + gap/length ===")
al = 0.15
# stairs: axis-parallel unit squares, square j occupies [j, j+1] x [j*tan(al) - 1, j*tan(al)]
stairs = [verts(np.array([j+0.5, j*math.tan(al)-0.5]), 1.0, 0.0) for j in range(12)]
# tilted squares of side 1, tilt al, resting on the stair corners (upper-right corners (j+1, j tan al))
# lower edge of tilted square: line y = x tan(al) + c ; touching corner (j+1, j*tan al): j*tan al = (j+1) tan al + c -> c = -tan al
# place tilted squares with lower-left vertex on that line, spaced 1/cos(al)
# tilted row: bottom edges flush along the line y = x tan(al) through stair top-LEFT corners (j, j tan al)
tl = []
for m in range(10):
    x0 = 1.0 + m*math.cos(al)
    v = np.array([x0, x0*math.tan(al)])
    z = v + np.array([math.cos(al)-math.sin(al), math.sin(al)+math.cos(al)])/2
    tl.append(verts(z, 1.0, al))
def sat_disjoint(P, Q):
    for poly in (P, Q):
        n = len(poly)
        for i in range(n):
            e = poly[(i+1)%n] - poly[i]
            u = np.array([-e[1], e[0]]); u /= np.linalg.norm(u)
            p1, p2 = P @ u, Q @ u
            if p1.max() <= p2.min() + 1e-9 or p2.max() <= p1.min() + 1e-9:
                return True
    return False
ok = True
allp = stairs + tl
for i in range(len(allp)):
    for j in range(i+1, len(allp)):
        if not sat_disjoint(allp[i], allp[j]): ok = False
print("staircase+tilted row disjoint:", ok)
# measure uncovered area in band between stair tops and tilted row over x in [3,9]
Npts = 300000
xs = rng.uniform(3, 9, Npts); ys = rng.uniform(0.0, 9*math.tan(al)+1.5, Npts)
pts = np.column_stack([xs, ys])
cov = np.zeros(Npts, bool)
for P in stairs: cov |= point_in_poly_sq(pts, P, 0.0)
for P in tl: cov |= point_in_poly_sq(pts, P, al)
# restrict to points between stair top surface and tilted lower surface: y in [floor stair top, line]
line = pts[:,0]*math.tan(al)
stairtop = np.floor(pts[:,0])*math.tan(al)
sel = (pts[:,1] < line + 1e-9)
gap_area = ((~cov) & sel & (pts[:,1] > stairtop - 1.0)).mean()*(6*(9*math.tan(al)+1.5))
print(f"measured interface gap area over run 6: {gap_area:.3f}; tan(al)/2 per unit length -> {6*math.tan(al)/2:.3f}")
