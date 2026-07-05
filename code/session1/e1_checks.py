import numpy as np
rng = np.random.default_rng(0)

def C(b):
    return np.abs(np.cos(b)) + np.abs(np.sin(b))

# square as polygon: center z, side s, tilt a
def verts(z, s, a):
    R = np.array([[np.cos(a), -np.sin(a)],[np.sin(a), np.cos(a)]])
    base = np.array([[1,1],[-1,1],[-1,-1],[1,-1]]) * s/2
    return z + base @ R.T

def sat_disjoint(P, Q):
    # exact for convex polygons: check separating axis among edge normals; return (disjoint, axis u or None)
    best = None
    for poly in (P, Q):
        n = len(poly)
        for i in range(n):
            e = poly[(i+1)%n] - poly[i]
            u = np.array([-e[1], e[0]]); u /= np.linalg.norm(u)
            p1, p2 = P @ u, Q @ u
            if p1.max() <= p2.min() + 1e-12 or p2.max() <= p1.min() + 1e-12:
                return True, u
    return False, None

# TEST B: key inequality D(alpha) >= 2 C(theta) on a fine grid
th = np.linspace(0, np.pi/2, 2001)[None,:]
al = np.linspace(-np.pi/4, np.pi/4, 2001)[:,None]
D = C(al)*C(th) + C(th-al)
print("TEST B: min of D - 2C(theta) =", (D - 2*C(th)).min())

# TEST B2: submultiplicativity C(x)C(y) >= C(x+y) random
x = rng.uniform(-10,10,10**6); y = rng.uniform(-10,10,10**6)
print("TEST B2: min of C(x)C(y)-C(x+y) =", (C(x)*C(y)-C(x+y)).min())

# TEST A: random disjoint pairs in U: verify s1+s2<=1 and the support-inequality chain
viol_sum = 0; viol_chain = 0; tested = 0; maxsum = 0
while tested < 20000:
    s1, s2 = rng.uniform(0.05, 1, 2)
    a1, a2 = rng.uniform(0, np.pi/2, 2)
    if s1*C(a1) > 1 or s2*C(a2) > 1: continue
    z1 = rng.uniform(s1*C(a1)/2, 1 - s1*C(a1)/2, 2)
    z2 = rng.uniform(s2*C(a2)/2, 1 - s2*C(a2)/2, 2)
    P, Q = verts(z1, s1, a1), verts(z2, s2, a2)
    dis, u = sat_disjoint(P, Q)
    if not dis: continue
    tested += 1
    maxsum = max(maxsum, s1+s2)
    if s1 + s2 > 1 + 1e-9: viol_sum += 1
    # reflect config so u has nonneg entries; reflections x->1-x flip z and tilt sign
    uu = u.copy(); zz1, zz2 = z1.copy(), z2.copy(); aa1, aa2 = a1, a2
    if uu[0] < 0: uu[0] = -uu[0]; zz1[0] = 1-zz1[0]; zz2[0] = 1-zz2[0]; aa1, aa2 = -aa1, -aa2
    if uu[1] < 0: uu[1] = -uu[1]; zz1[1] = 1-zz1[1]; zz2[1] = 1-zz2[1]; aa1, aa2 = -aa1, -aa2
    th0 = np.arctan2(uu[1], uu[0])
    Pr, Qr = verts(zz1, s1, aa1), verts(zz2, s2, aa2)
    h1, l1 = (Pr@uu).max(), (Pr@uu).min()
    h2, l2 = (Qr@uu).max(), (Qr@uu).min()
    # order along u
    if h1 <= l2 + 1e-9:
        lowS, lowA, lowH = s1, aa1, h1; hiS, hiA, hiL = s2, aa2, l2
    elif h2 <= l1 + 1e-9:
        lowS, lowA, lowH = s2, aa2, h2; hiS, hiA, hiL = s1, aa1, l1
    else:
        continue
    ok1 = (lowS/2)*(C(lowA)*C(th0) + C(th0-lowA)) <= lowH + 1e-9
    ok2 = C(th0) - (hiS/2)*(C(hiA)*C(th0) + C(th0-hiA)) >= hiL - 1e-9
    if not (ok1 and ok2): viol_chain += 1
print(f"TEST A: tested={tested}, sum-violations={viol_sum}, chain-violations={viol_chain}, max(s1+s2)={maxsum:.4f}")

# TEST C: ledger identity E[p+q-1-c] = 2dC(a)-1-d^2 for tilted square, Monte Carlo
def mc_identity(d, a, M=400000):
    w = d*C(a)
    V = verts(np.array([3.5,3.5]), d, a)  # place away from origin
    xs = rng.uniform(0,1,M); ys = rng.uniform(0,1,M)
    # p: number of integers in x-projection shifted
    px0, px1 = V[:,0].min(), V[:,0].max()
    py0, py1 = V[:,1].min(), V[:,1].max()
    p = np.floor(px1 - xs) - np.ceil(px0 - xs) + 1
    q = np.floor(py1 - ys) - np.ceil(py0 - ys) + 1
    # c: lattice count inside square: count integer points (i+x, j+y) in K
    R = np.array([[np.cos(a), np.sin(a)],[-np.sin(a), np.cos(a)]])  # world->square frame
    cs = np.zeros(M)
    I = np.arange(int(np.floor(px0))-1, int(np.ceil(px1))+2)
    J = np.arange(int(np.floor(py0))-1, int(np.ceil(py1))+2)
    for i in I:
        for j in J:
            pts = np.stack([i+xs-3.5, j+ys-3.5], axis=1) @ R.T
            cs += ((np.abs(pts[:,0]) <= d/2) & (np.abs(pts[:,1]) <= d/2)).astype(float)
    lhs = (p + q - 1 - cs).mean()
    rhs = 2*d*C(np.array(a)) - 1 - d*d
    return lhs, rhs

for d, a in [(0.75, np.pi/4), (0.9, 0.3), (1.0, 0.0), (1.3, 0.2), (0.6, np.pi/8)]:
    lhs, rhs = mc_identity(d, a)
    print(f"TEST C: d={d}, a={a:.3f}: MC E[delta]={lhs:.4f}, formula={float(rhs):.4f}")

# TEST C2: explicit pointwise failure: d=0.75, 45 deg, centered at cell center
d = 0.75; a = np.pi/4
V = verts(np.array([0.5,0.5]), d, a)
R = np.array([[np.cos(a), np.sin(a)],[-np.sin(a), np.cos(a)]])
c = 0
for i in (0,1):
    for j in (0,1):
        pt = (np.array([i,j]) - 0.5) @ R.T
        if abs(pt[0]) <= d/2 and abs(pt[1]) <= d/2: c += 1
px0, px1 = V[:,0].min(), V[:,0].max(); py0, py1 = V[:,1].min(), V[:,1].max()
p = len([i for i in (0,1) if px0 <= i <= px1]); q = len([j for j in (0,1) if py0 <= j <= py1])
print(f"TEST C2: p={p}, q={q}, c={c}, defect={p+q-1-c}")

# TEST D: diamond chain: 45-deg squares along diagonal, total side -> sqrt(2)
def diamond_chain(s):
    # centers at (t,t) with <z,u> = t*sqrt2 from s to sqrt2-s spaced s
    us = np.sqrt(2)
    vals = np.arange(s, us - s + 1e-12, s)
    cs = [np.array([v/us, v/us])*1.0 for v in vals]  # t = v/sqrt2... <z,u>=t*sqrt2=v -> t=v/sqrt2
    cs = [np.array([v/np.sqrt(2), v/np.sqrt(2)]) for v in vals]
    polys = [verts(z, s, np.pi/4) for z in cs]
    # check containment in U and pairwise interior-disjoint
    ok_in = all((P.min() >= -1e-9) and (P.max() <= 1+1e-9) for P in polys)
    ok_dis = True
    for i in range(len(polys)):
        for j in range(i+1, len(polys)):
            dis, _ = sat_disjoint(polys[i], polys[j])
            if not dis: ok_dis = False
    return len(polys), len(polys)*s, ok_in, ok_dis
for s in (0.2, 0.1, 0.05):
    n, tot, oki, okd = diamond_chain(s)
    print(f"TEST D: s={s}: n={n}, total side={tot:.4f} (sqrt2-s={np.sqrt(2)-s:.4f}), inside={oki}, disjoint={okd}")
