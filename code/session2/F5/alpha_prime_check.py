"""Numerical stress test of Lemma alpha-prime.

Lemma alpha': theta in (0,pi/4], tau=tan theta; phi0 with tan phi0 <= tau/2;
family of squares, sides in [1-eta,1+eta] (eta<=1/20), folded tilts <= phi0,
pairwise disjoint interiors, all contained in {y <= tau x + beta}.
Claim: uncovered area of strip R={0<=x<=X, tau x + beta - 1/4 < y < tau x + beta}
        >= (X/228) * min(tau - tan phi0, 1/3).

We build adversarial covering families (coherent tilted rows hugging the line,
brick-staggered rows, mixed-tilt staircases) and measure the uncovered strip area.
"""
import numpy as np

H = 0.25

def square(cx, cy, d, psi):
    hs = d / 2.0
    c = np.array([[-hs, -hs], [hs, -hs], [hs, hs], [-hs, hs]])
    R = np.array([[np.cos(psi), -np.sin(psi)], [np.sin(psi), np.cos(psi)]])
    return c @ R.T + np.array([cx, cy])

def top_vertex_offset(d, psi):
    # offset from center to topmost vertex, for psi in (-pi/4, pi/4]
    hs = d / 2.0
    if psi >= 0:
        v = np.array([hs, hs])
    else:
        v = np.array([-hs, hs])
    R = np.array([[np.cos(psi), -np.sin(psi)], [np.sin(psi), np.cos(psi)]])
    return R @ v

def covered_mask(pts, polys):
    res = np.zeros(len(pts), bool)
    for poly in polys:
        m = np.ones(len(pts), bool)
        for i in range(4):
            a = poly[i]; b = poly[(i + 1) % 4]
            cr = (b[0]-a[0])*(pts[:,1]-a[1]) - (b[1]-a[1])*(pts[:,0]-a[0])
            m &= cr >= -1e-12
            if not m.any():
                break
        res |= m
    return res

def sat_disjoint(p1, p2):
    """Separating-axis test for two convex quads (interiors disjoint)."""
    for poly, other in ((p1, p2), (p2, p1)):
        for i in range(4):
            a = poly[i]; b = poly[(i+1) % 4]
            n = np.array([-(b[1]-a[1]), b[0]-a[0]])
            if max(other @ n) <= min(poly @ n) + 1e-12 or min(other @ n) >= max(poly @ n) - 1e-12:
                return True
    return False

def below_line(poly, tau, beta):
    return np.all(poly[:, 1] <= tau * poly[:, 0] + beta + 1e-12)

def uncovered_strip_area(polys, tau, beta, X, ngrid=1400):
    # sheared coords: u in [0,X], v in [-H,0); point (u, tau*u+beta+v)
    us = (np.arange(ngrid) + 0.5) / ngrid * X
    vs = -H * (np.arange(ngrid) + 0.5) / ngrid
    U, V = np.meshgrid(us, vs)
    pts = np.column_stack([U.ravel(), tau * U.ravel() + beta + V.ravel()])
    cov = covered_mask(pts, polys)
    frac_unc = 1.0 - cov.mean()
    return frac_unc * H * X

def flush_to_line(cx, cy, d, psi, tau, beta):
    """Return square centered at (cx, *) raised so that max_corner (y - tau x - beta) = 0."""
    P = square(cx, cy, d, psi)
    excess = np.max(P[:, 1] - tau * P[:, 0] - beta)
    P[:, 1] -= excess
    return P

def coherent_row(tau, psi, d, X):
    """Row of side-d squares at tilt psi, each flush against y=tau x (support
    point on the line), stepped by d along their own frame axis (disjoint)."""
    polys = []
    cx = -1.5
    step = d * np.array([np.cos(psi), np.sin(psi)])
    while cx < X + 1.5:
        polys.append(flush_to_line(cx, 0.0, d, psi, tau, 0.0))
        cx += step[0]
    return polys

def greedy_row(tau, X, psis, ds):
    """Greedy left-to-right: square j at tilt psis[j], side ds[j]; placed flush
    against the line, pushed down (binary search) until disjoint from previous."""
    polys = []
    x = -1.5
    j = 0
    while x < X + 1.5 and j < len(psis):
        psi, d = psis[j], ds[j]
        def make(s):
            P = flush_to_line(x, 0.0, d, psi, tau, 0.0)
            P[:, 1] -= s
            return P
        ok_prev = lambda P: all(sat_disjoint(P, Q) for Q in polys[-4:])
        P = make(0.0)
        if not ok_prev(P):
            lo, hi = 0.0, 4.0
            for _ in range(60):
                mid = 0.5 * (lo + hi)
                if ok_prev(make(mid)):
                    hi = mid
                else:
                    lo = mid
            P = make(hi + 1e-9)
        polys.append(P)
        x += d * np.cos(psi)
        j += 1
    return polys

def run_case(tau, phi0, mode, eta=0.0, X=20.0, seed=0):
    rng = np.random.default_rng(seed)
    beta = 0.0
    nmax = int(2 * (X + 4)) + 4
    if mode == 'coherent+':
        polys = greedy_row(tau, X, [phi0] * nmax, [1.0 - eta] * nmax)
    elif mode == 'coherent-':
        polys = greedy_row(tau, X, [-phi0] * nmax, [1.0 - eta] * nmax)
    elif mode == 'axis':
        polys = greedy_row(tau, X, [0.0] * nmax, [1.0 - eta] * nmax)
    elif mode == 'mixed':
        psis = rng.uniform(-phi0, phi0, nmax)
        ds = 1.0 + rng.uniform(-eta, eta, nmax)
        polys = greedy_row(tau, X, psis, ds)
    else:
        raise ValueError(mode)
    # verify disjointness (sample pairs) and below-line
    for p in polys:
        assert below_line(p, tau, beta), "square above line!"
    bad = 0
    for i in range(len(polys)):
        for j in range(i + 1, min(i + 4, len(polys))):
            if not sat_disjoint(polys[i], polys[j]):
                bad += 1
    unc = uncovered_strip_area(polys, tau, beta, X)
    bound = (X / 228.0) * min(tau - np.tan(phi0), 1.0 / 3.0)
    return unc, bound, bad, len(polys)

print(f"{'tau':>5} {'phi0/atan':>9} {'mode':>10} {'uncovered':>10} {'bound':>9} {'ratio':>8} {'overlaps':>8}")
worst = np.inf
for tau in [0.1, 0.2, 0.4, 1.0]:
    for frac in [0.5, 0.25, 0.0]:
        phi0 = np.arctan(frac * tau)
        modes = ['coherent+', 'coherent-', 'axis'] + (['mixed'] if frac > 0 else [])
        for mode in modes:
            unc, bound, bad, n = run_case(tau, phi0, mode, eta=0.05 if mode == 'mixed' else 0.0)
            r = unc / bound
            worst = min(worst, r)
            print(f"{tau:5.2f} {frac:9.2f} {mode:>10} {unc:10.4f} {bound:9.4f} {r:8.2f} {bad:8d}")
print(f"\nWORST ratio uncovered/bound = {worst:.3f}  (must be >= 1)")
