"""Focused n=17 rotated attack: two-stage (axis-solve then release thetas),
plus extra rotated multistarts with larger iteration budget."""
import numpy as np, json
import pack

n, k = 17, 4
rng = np.random.default_rng(2026)
best = None

def consider(r):
    global best
    if r['viol'] > -1e-6 and (best is None or r['sum'] > best['sum']):
        best = r

# Stage A: axis-parallel solves from structured starts, then release thetas
axis_starts = [pack.grid_split_start(k, shrink=sh) for sh in (0.985, 0.96, 0.9)]
axis_starts += [pack.grid_split_start(k, jitter=rng.uniform(0.002, 0.01), rng=rng,
                                      shrink=rng.uniform(0.92, 0.99)) for _ in range(12)]
for st in axis_starts:
    st = dict(st); st['th'] = np.zeros(n)
    try:
        ra = pack.solve(n, st, free_theta=False, ftol=1e-10, maxiter=800)
    except Exception:
        continue
    if ra['viol'] < -1e-6:
        continue
    # release thetas from the axis solution (slightly shrunk), jitter thetas a bit
    for tj in (0.0, 0.02, 0.1):
        st2 = {kk: ra[kk].copy() for kk in ('cx', 'cy', 'th', 's')}
        st2['s'] = st2['s'] * 0.999
        st2['th'] = st2['th'] + (rng.normal(0, tj, n) if tj else 0.0)
        try:
            rb = pack.solve(n, st2, free_theta=True, ftol=1e-12, maxiter=1500)
        except Exception:
            continue
        consider(rb)
        consider(ra)

# Stage B: extra rotated multistarts, big budget
starts = pack.make_starts(n, k, 100, rng)
for st in starts:
    try:
        r = pack.solve(n, st, free_theta=True, ftol=1e-10, maxiter=800)
    except Exception:
        continue
    consider(r)

csum, shrink = pack.certify(best)
out = {'tag': 'n17_rotated_twostage', 'n': n,
       'best_raw_sum': best['sum'], 'best_certified_sum': csum,
       'ld_margin': pack.feas_margin_ld(best),
       'max_abs_theta_mod90': float(np.max(np.abs(
           (best['th'] + np.pi / 4) % (np.pi / 2) - np.pi / 4))),
       'best_cfg': {kk: best[kk].tolist() for kk in ('cx', 'cy', 'th', 's')}}
print(json.dumps({kk: vv for kk, vv in out.items() if kk != 'best_cfg'}))
with open('n17_results.json', 'w') as fh:
    json.dump(out, fh, indent=1)
