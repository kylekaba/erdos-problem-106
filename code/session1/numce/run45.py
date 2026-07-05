import numpy as np, json
import pack

n, k = 10, 3
rng = np.random.default_rng(999)
starts = pack.make_starts(n, k, 120, rng)
fix = np.zeros(n, bool); fix[0] = True
best = None
for st in starts:
    st = dict(st)
    th = st['th'].copy(); th[0] = np.pi / 4; st['th'] = th
    s2 = st['s'].copy(); s2[0] *= 0.6; st['s'] = s2
    try:
        r = pack.solve(n, st, theta_fix=fix, ftol=1e-10, maxiter=600)
    except Exception:
        continue
    if r['viol'] > -1e-6 and (best is None or r['sum'] > best['sum']):
        best = r
csum, shrink = pack.certify(best)
out = {'tag': 'one_square_45deg', 'n': n,
       'best_raw_sum': best['sum'], 'best_certified_sum': csum,
       'ld_margin': pack.feas_margin_ld(best),
       's_of_45deg_square': float(best['s'][0]),
       'best_cfg': {kk: best[kk].tolist() for kk in ('cx', 'cy', 'th', 's')}}
print(json.dumps({kk: vv for kk, vv in out.items() if kk != 'best_cfg'}))
with open('tilt45_results.json', 'w') as fh:
    json.dump(out, fh, indent=1)
