import numpy as np
rng = np.random.default_rng(1)

def C(b): return np.abs(np.cos(b)) + np.abs(np.sin(b))

def verts(z, s, a):
    R = np.array([[np.cos(a), -np.sin(a)],[np.sin(a), np.cos(a)]])
    base = np.array([[1,1],[-1,1],[-1,-1],[1,-1]]) * s/2
    return z + base @ R.T

def penetration(P, Q):
    # SAT overlap depth (0 if disjoint) for convex polygons
    depth = np.inf
    for poly in (P, Q):
        n = len(poly)
        for i in range(n):
            e = poly[(i+1)%n] - poly[i]
            u = np.array([-e[1], e[0]]); u /= np.linalg.norm(u)
            p1, p2 = P @ u, Q @ u
            ov = min(p1.max(), p2.max()) - max(p1.min(), p2.min())
            if ov <= 0: return 0.0
            depth = min(depth, ov)
    return depth

def outside(P):
    return np.maximum(0, -P).sum() + np.maximum(0, P - 1).sum()

def objective(params, n, lam=50.0):
    tot, pen = 0.0, 0.0
    polys = []
    for i in range(n):
        z = params[4*i:4*i+2]; a = params[4*i+2]; s = abs(params[4*i+3])
        P = verts(z, s, a); polys.append(P); tot += s
        pen += outside(P)
    for i in range(n):
        for j in range(i+1, n):
            pen += penetration(polys[i], polys[j])
    return tot - lam*pen

def anneal(n, iters=60000, restarts=8):
    best = -np.inf; bestp = None
    for r in range(restarts):
        p = rng.uniform(0.1, 0.9, 4*n); p[3::4] = rng.uniform(0.1, 0.5, n); p[2::4] = rng.uniform(0, np.pi/2, n)
        f = objective(p, n); T = 0.1
        for t in range(iters):
            T = 0.1 * (1 - t/iters) + 1e-4
            q = p.copy()
            k = rng.integers(0, 4*n)
            q[k] += rng.normal(0, 0.03 if t < iters//2 else 0.005)
            g = objective(q, n)
            if g > f or rng.uniform() < np.exp((g-f)/T):
                p, f = q, g
        # final feasibility: shrink until feasible
        val = objective(p, n, lam=1e6)
        if val > best: best, bestp = val, p
    return best, bestp

for n, target in [(2, 1.0), (5, 2.0)]:
    best, bp = anneal(n)
    sides = np.abs(bp[3::4]); tilts = (bp[2::4] % (np.pi/2))
    print(f"n={n}: best feasible-ish total={best:.4f} (target {target}), sides={np.round(sides,3)}, tilts_deg={np.round(np.degrees(tilts),1)}")
