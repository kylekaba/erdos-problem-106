"""Numerical stress-test of Erdos square-packing conjecture f(k^2+1)=k.

Maximize sum of sides of n squares (cx,cy,theta,s each) packed with
pairwise-disjoint interiors in [0,1]^2. Disjointness via separating-axis
theorem (4 candidate axes per pair: the 2 edge-normal directions of each
square). Containment: all 4 corners in [0,1]^2.
"""
import numpy as np
import json, sys, time
from scipy.optimize import minimize

rng_global = np.random.default_rng(12345)

# ---------------- geometry ----------------

def corners(cx, cy, th, s):
    """(n,4,2) corner array."""
    n = len(cx)
    hs = s / 2.0
    ct, st = np.cos(th), np.sin(th)
    # local corners (+-1,+-1)*hs
    lx = np.array([1, 1, -1, -1])
    ly = np.array([1, -1, -1, 1])
    X = cx[:, None] + hs[:, None] * (ct[:, None] * lx[None, :] - st[:, None] * ly[None, :])
    Y = cy[:, None] + hs[:, None] * (st[:, None] * lx[None, :] + ct[:, None] * ly[None, :])
    return np.stack([X, Y], axis=-1)


def pair_seps(cx, cy, th, s, I, J):
    """SAT separation for each pair (I[p],J[p]).
    sep >= 0  <=>  interiors disjoint (for squares: max over the 4 edge-normal
    axes of the projected interval gap).  Returns (P,) array."""
    dx = cx[J] - cx[I]
    dy = cy[J] - cy[I]
    # axes: th_i, th_i+pi/2, th_j, th_j+pi/2   -> (P,4)
    A = np.stack([th[I], th[I] + np.pi / 2, th[J], th[J] + np.pi / 2], axis=1)
    ux, uy = np.cos(A), np.sin(A)
    dist = np.abs(dx[:, None] * ux + dy[:, None] * uy)          # (P,4)
    # half-width of square (side s, angle t) projected on axis angle a:
    # (s/2)(|cos(t-a)|+|sin(t-a)|)
    ri = 0.5 * s[I][:, None] * (np.abs(np.cos(th[I][:, None] - A)) + np.abs(np.sin(th[I][:, None] - A)))
    rj = 0.5 * s[J][:, None] * (np.abs(np.cos(th[J][:, None] - A)) + np.abs(np.sin(th[J][:, None] - A)))
    gaps = dist - ri - rj
    return gaps.max(axis=1)


def all_constraints(cx, cy, th, s, I, J):
    """Vector of quantities required >= 0."""
    C = corners(cx, cy, th, s)          # (n,4,2)
    cont = np.concatenate([C.ravel(), (1.0 - C).ravel()])
    seps = pair_seps(cx, cy, th, s, I, J)
    return np.concatenate([seps, cont])


# ---------------- optimizer wrapper ----------------

def solve(n, start, free_theta=True, theta_fix=None, ftol=1e-9, maxiter=400):
    """start: dict with cx,cy,th,s arrays.  theta_fix: array of bool (fixed) +
    values taken from start.th for fixed entries.  Returns result dict."""
    I, J = np.triu_indices(n, 1)
    th0 = np.asarray(start['th'], float).copy()
    if theta_fix is None:
        theta_fix = np.zeros(n, bool) if free_theta else np.ones(n, bool)
    free_idx = np.where(~theta_fix)[0]
    nf = len(free_idx)

    def unpack(z):
        cx = z[0:n]; cy = z[n:2 * n]; s = z[2 * n:3 * n]
        th = th0.copy()
        if nf: th[free_idx] = z[3 * n:3 * n + nf]
        return cx, cy, th, s

    z0 = np.concatenate([start['cx'], start['cy'], start['s'],
                         th0[free_idx] if nf else []])

    def obj(z):
        return -np.sum(z[2 * n:3 * n])

    def obj_grad(z):
        g = np.zeros_like(z)
        g[2 * n:3 * n] = -1.0
        return g

    def cons(z):
        return all_constraints(*unpack(z), I, J)

    bounds = ([(0.0, 1.0)] * n + [(0.0, 1.0)] * n + [(0.0, 1.0)] * n
              + [(-np.pi, np.pi)] * nf)
    res = minimize(obj, z0, jac=obj_grad, bounds=bounds,
                   constraints=[{'type': 'ineq', 'fun': cons}],
                   method='SLSQP', options={'maxiter': maxiter, 'ftol': ftol})
    cx, cy, th, s = unpack(res.x)
    return {'cx': cx, 'cy': cy, 'th': th, 's': s, 'sum': float(np.sum(s)),
            'status': int(res.status), 'viol': float(min(0.0, cons(res.x).min()))}


# ---------------- certification (float128 + shrink repair) ----------------

def feas_margin_ld(cfg):
    """Min of all constraint values in long double."""
    L = np.longdouble
    cx = cfg['cx'].astype(L); cy = cfg['cy'].astype(L)
    th = cfg['th'].astype(L); s = cfg['s'].astype(L)
    n = len(cx); I, J = np.triu_indices(n, 1)
    hs = s / 2
    ct, st = np.cos(th), np.sin(th)
    lx = np.array([1, 1, -1, -1], dtype=L); ly = np.array([1, -1, -1, 1], dtype=L)
    X = cx[:, None] + hs[:, None] * (ct[:, None] * lx - st[:, None] * ly)
    Y = cy[:, None] + hs[:, None] * (st[:, None] * lx + ct[:, None] * ly)
    m = min(X.min(), Y.min(), (1 - X).max() * 0 + (1 - X.max()), (1 - Y.max()))
    dx = cx[J] - cx[I]; dy = cy[J] - cy[I]
    A = np.stack([th[I], th[I] + L(np.pi) / 2, th[J], th[J] + L(np.pi) / 2], axis=1)
    ux, uy = np.cos(A), np.sin(A)
    dist = np.abs(dx[:, None] * ux + dy[:, None] * uy)
    ri = L(0.5) * s[I][:, None] * (np.abs(np.cos(th[I][:, None] - A)) + np.abs(np.sin(th[I][:, None] - A)))
    rj = L(0.5) * s[J][:, None] * (np.abs(np.cos(th[J][:, None] - A)) + np.abs(np.sin(th[J][:, None] - A)))
    seps = (dist - ri - rj).max(axis=1)
    if len(seps): m = min(m, seps.min())
    return float(m)


def certify(cfg):
    """Shrink all sides about centers until exactly feasible (long double).
    Returns certified sum."""
    if feas_margin_ld(cfg) >= 0:
        return float(np.sum(cfg['s'])), 1.0
    lo, hi = 0.0, 1.0   # shrink factor t applied to sides; t=0 surely feasible (if centers in U)
    for _ in range(80):
        mid = (lo + hi) / 2
        c2 = dict(cfg); c2 = {k: (v.copy() if isinstance(v, np.ndarray) else v) for k, v in cfg.items()}
        c2['s'] = cfg['s'] * mid
        c2['cx'] = np.clip(cfg['cx'], 0, 1); c2['cy'] = np.clip(cfg['cy'], 0, 1)
        if feas_margin_ld(c2) >= 0:
            lo = mid
        else:
            hi = mid
    return float(np.sum(cfg['s']) * lo), lo


# ---------------- structured starts ----------------

def grid_split_start(k, jitter=0.0, tilt=0.0, rng=None, shrink=1.0,
                     row_tilt=None, all_tilt=None, diamonds=0):
    """k x k grid with one cell replaced by two half-size squares -> k^2+1
    squares, sum = k exactly (before shrink)."""
    rng = rng or rng_global
    h = 1.0 / k
    cx, cy, th, s = [], [], [], []
    for i in range(k):
        for j in range(k):
            if i == 0 and j == 0:
                continue
            cx.append((i + 0.5) * h); cy.append((j + 0.5) * h)
            th.append(0.0); s.append(h)
    # split cell (0,0) into two h/2 squares
    for t in range(2):
        cx.append(0.25 * h + 0.5 * h * t); cy.append(0.25 * h)
        th.append(0.0); s.append(0.5 * h)
    cx = np.array(cx); cy = np.array(cy); th = np.array(th); s = np.array(s) * shrink
    n = len(cx)
    if jitter:
        cx = cx + rng.normal(0, jitter, n); cy = cy + rng.normal(0, jitter, n)
    if tilt:
        th = th + rng.normal(0, tilt, n)
    if row_tilt is not None:
        # tilt squares in the top row coherently
        mask = cy > 1 - 1.5 * h
        th[mask] = row_tilt
        s[mask] *= 0.9
    if all_tilt is not None:
        th[:] = all_tilt
        s *= 0.9
    if diamonds:
        idx = rng.choice(n, size=min(diamonds, n), replace=False)
        th[idx] = np.pi / 4
        s[idx] *= 0.7
    cx = np.clip(cx, 0.02, 0.98); cy = np.clip(cy, 0.02, 0.98)
    return {'cx': cx, 'cy': cy, 'th': th, 's': s}


def subgrid_start(n, k):
    """First n cells of the (k+1)x(k+1) grid."""
    g = k + 1
    h = 1.0 / g
    cells = [(i, j) for i in range(g) for j in range(g)][:n]
    cx = np.array([(i + 0.5) * h for i, j in cells])
    cy = np.array([(j + 0.5) * h for i, j in cells])
    return {'cx': cx, 'cy': cy, 'th': np.zeros(n), 's': np.full(n, h * 0.98)}


def random_start(n, k, rng):
    return {'cx': rng.uniform(0.05, 0.95, n), 'cy': rng.uniform(0.05, 0.95, n),
            'th': rng.uniform(-np.pi / 4, np.pi / 4, n),
            's': rng.uniform(0.2, 0.75, n) / k}


def pinwheel_start(n, k, rng):
    st = grid_split_start(k, jitter=0.005, rng=rng, shrink=0.92)
    # rotate a central block of 4-5 squares by a common random angle
    a = rng.uniform(0.1, 0.6)
    d = np.hypot(st['cx'] - 0.5, st['cy'] - 0.5)
    idx = np.argsort(d)[:5]
    st['th'][idx] = a
    st['s'][idx] *= 0.8
    return st


def make_starts(n, k, count, rng):
    starts = []
    starts.append(grid_split_start(k, shrink=0.985))         # near conjectured optimum
    starts.append(grid_split_start(k, shrink=0.96))
    starts.append(grid_split_start(k, shrink=0.9))
    starts.append(subgrid_start(n, k))
    starts.append(grid_split_start(k, row_tilt=np.deg2rad(5)))
    starts.append(grid_split_start(k, row_tilt=np.deg2rad(15)))
    starts.append(grid_split_start(k, all_tilt=np.deg2rad(3)))
    starts.append(grid_split_start(k, all_tilt=np.deg2rad(10)))
    starts.append(grid_split_start(k, diamonds=2, rng=rng))
    starts.append(grid_split_start(k, diamonds=n // 2, rng=rng))
    while len(starts) < count:
        r = rng.random()
        if r < 0.35:
            starts.append(grid_split_start(k, jitter=rng.uniform(0.002, 0.02),
                                           tilt=rng.uniform(0.01, 0.3), rng=rng,
                                           shrink=rng.uniform(0.9, 1.0)))
        elif r < 0.5:
            starts.append(pinwheel_start(n, k, rng))
        elif r < 0.6:
            starts.append(grid_split_start(k, diamonds=rng.integers(1, n), rng=rng,
                                           jitter=0.01, tilt=0.05))
        else:
            starts.append(random_start(n, k, rng))
    return starts


# ---------------- experiment driver ----------------

def run_case(n, k, nstarts, free_theta=True, tag=""):
    rng = np.random.default_rng(1000 + n + (0 if free_theta else 7))
    starts = make_starts(n, k, nstarts, rng)
    results = []
    t0 = time.time()
    for idx, st in enumerate(starts):
        try:
            r = solve(n, st, free_theta=free_theta, ftol=1e-9, maxiter=350)
            results.append(r)
        except Exception as e:
            print(f"  start {idx} failed: {e}", flush=True)
    # discard grossly infeasible SLSQP failures before ranking
    results = [r for r in results if r['viol'] > -1e-6]
    results.sort(key=lambda r: -r['sum'])
    # polish top 10
    polished = []
    for r in results[:10]:
        # tiny shrink to step off the degenerate active boundary before polish
        st = {kk: r[kk].copy() for kk in ('cx', 'cy', 'th', 's')}
        st['s'] = st['s'] * 0.9995
        try:
            p = solve(n, st, free_theta=free_theta, ftol=1e-12, maxiter=1500)
            polished.append(p if p['sum'] >= r['sum'] else r)
        except Exception:
            polished.append(r)
    polished = [r for r in polished if r['viol'] > -1e-6] or results[:3]
    polished.sort(key=lambda r: -r['sum'])
    # certify top 3, keep the best certified sum
    best, csum, shrink = None, -1.0, 0.0
    for cand in polished[:3]:
        cs, sh = certify(cand)
        if cs > csum:
            best, csum, shrink = cand, cs, sh
    out = {
        'n': n, 'k': k, 'free_theta': free_theta, 'tag': tag,
        'nstarts': len(results), 'time_s': round(time.time() - t0, 1),
        'best_raw_sum': best['sum'], 'best_certified_sum': csum,
        'shrink_factor': shrink, 'raw_viol': best['viol'],
        'ld_margin': feas_margin_ld(best),
        'max_abs_theta_mod90': float(np.max(np.abs(
            (best['th'] + np.pi / 4) % (np.pi / 2) - np.pi / 4))),
        'top5_sums': [r['sum'] for r in polished[:5]],
        'best_cfg': {kk: best[kk].tolist() for kk in ('cx', 'cy', 'th', 's')},
    }
    return out


if __name__ == '__main__':
    which = sys.argv[1]
    outfile = sys.argv[2]
    all_out = []
    if which == 'main':
        for n, k, ns in [(2, 1, 100), (5, 2, 150), (10, 3, 220), (17, 4, 120)]:
            print(f"=== n={n} rotated ===", flush=True)
            all_out.append(run_case(n, k, ns, free_theta=True, tag='rotated'))
            print(json.dumps({kk: vv for kk, vv in all_out[-1].items() if kk != 'best_cfg'}), flush=True)
    elif which == 'control':
        for n, k, ns in [(2, 1, 60), (5, 2, 80), (10, 3, 120), (17, 4, 80)]:
            print(f"=== n={n} axis-parallel control ===", flush=True)
            all_out.append(run_case(n, k, ns, free_theta=False, tag='axis'))
            print(json.dumps({kk: vv for kk, vv in all_out[-1].items() if kk != 'best_cfg'}), flush=True)
    elif which == 'tilt':
        # tilt penalty curve for n=10: all thetas frozen at t0
        n, k = 10, 3
        for deg in [2, 5, 10]:
            t0 = np.deg2rad(deg)
            rng = np.random.default_rng(500 + deg)
            starts = make_starts(n, k, 80, rng)
            best = None
            for st in starts:
                st = dict(st); st['th'] = np.full(n, t0)
                st['s'] = st['s'] / (np.cos(t0) + np.sin(t0))  # keep start feasible-ish
                try:
                    r = solve(n, st, theta_fix=np.ones(n, bool), ftol=1e-10, maxiter=600)
                except Exception:
                    continue
                if r['viol'] > -1e-6 and (best is None or r['sum'] > best['sum']):
                    best = r
            csum, shrink = certify(best)
            all_out.append({'tag': f'all_tilt_{deg}deg', 'n': n,
                            'best_raw_sum': best['sum'], 'best_certified_sum': csum,
                            'ld_margin': feas_margin_ld(best),
                            'best_cfg': {kk: best[kk].tolist() for kk in ('cx', 'cy', 'th', 's')}})
            print(json.dumps({kk: vv for kk, vv in all_out[-1].items() if kk != 'best_cfg'}), flush=True)
        # one square frozen at 45 deg, others free
        rng = np.random.default_rng(999)
        starts = make_starts(n, k, 80, rng)
        best = None
        fix = np.zeros(n, bool); fix[0] = True
        for st in starts:
            st = dict(st); th = st['th'].copy(); th[0] = np.pi / 4; st['th'] = th
            s2 = st['s'].copy(); s2[0] *= 0.7; st['s'] = s2
            try:
                r = solve(n, st, theta_fix=fix, ftol=1e-10, maxiter=600)
            except Exception:
                continue
            if best is None or r['sum'] > best['sum']:
                best = r
        csum, shrink = certify(best)
        all_out.append({'tag': 'one_square_45deg', 'n': n,
                        'best_raw_sum': best['sum'], 'best_certified_sum': csum,
                        'ld_margin': feas_margin_ld(best),
                        'best_cfg': {kk: best[kk].tolist() for kk in ('cx', 'cy', 'th', 's')}})
        print(json.dumps({kk: vv for kk, vv in all_out[-1].items() if kk != 'best_cfg'}), flush=True)
    with open(outfile, 'w') as fh:
        json.dump(all_out, fh, indent=1)
    print("WROTE", outfile, flush=True)
