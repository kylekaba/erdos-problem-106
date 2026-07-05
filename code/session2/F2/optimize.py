import numpy as np, json, sys
from fcmb import analyze, feasible, square_mask
from scipy.optimize import minimize

rng = np.random.default_rng(7)

def penalized_F(x, k, n, M=220):
    sq = x.reshape(n, 4)
    if np.any(sq[:, 3] < 0.02) or np.any(sq[:, 3] > k + 0.5):
        return 10.0
    xs = (np.arange(k * M) + 0.5) / M
    X, Y = np.meshgrid(xs, xs, indexing='ij')
    occ = np.zeros(X.shape, dtype=np.int16)
    inside = 0.0
    for (cx, cy, th, d) in sq:
        m = square_mask(X, Y, cx, cy, th, d)
        occ += m.astype(np.int16)
        inside += m.mean() * k * k
    overlap = ((occ > 1) * (occ - 1)).sum() / M**2
    out_of_T = sum(d * d for d in sq[:, 3]) - inside  # area sticking out (>=0 up to grid err)
    Gmask = occ == 0
    mult = Gmask.reshape(k, M, k, M).sum(axis=(0, 2))
    piG = (mult > 0).mean()
    s = float(np.sum((1 - sq[:, 3]) ** 2))
    F = piG - (1 - s)
    return F + 60.0 * overlap + 60.0 * max(out_of_T, 0.0)

def seeds_k2():
    d3 = 2 / 3
    row = [(d3/2, d3/2, 0, d3), (1.0, d3/2, 0, d3), (2 - d3/2, d3/2, 0, d3),
           (0.5, 1.5, 0, 1), (1.5, 1.5, 0, 1)]
    delta = 0.2; dd = 1 - delta; bb = 2 * delta
    strad = [(dd/2, dd/2, 0, dd), (1 + delta + dd/2, dd/2, 0, dd),
             (1.0, bb/2, 0, bb), (0.5, 1.5, 0, 1), (1.5, 1.5, 0, 1)]
    a = 0.37; b = 1 - a
    split = [(0.5, 0.5, 0, 1), (0.5, 1.5, 0, 1), (1.5, 1.5, 0, 1),
             (1 + a/2, a/2, 0, a), (1 + b/2, a + b/2, 0, b)]
    # 5 near-equal squares attempt (side ~0.8, one forced small/tilted)
    e = 0.8
    nearq = [(e/2, e/2, 0, e), (e/2 + e, e/2, 0, e), (e/2, e/2 + e, 0, e),
             (e/2 + e, e/2 + e, 0, e), (1.8, 1.8, np.pi/8, 0.35)]
    # tilted row seed
    trow = [(d3/2, d3/2, 0.15, d3*0.95), (1.0, d3/2, 0.15, d3*0.95), (2 - d3/2, d3/2, 0.15, d3*0.95),
            (0.5, 1.5, 0, 0.98), (1.5, 1.5, 0, 0.98)]
    return [row, strad, split, nearq, trow]

def run(k, n, seeds, n_random=6, noise_reps=3, maxiter=1500):
    results = []
    starts = []
    for s0 in seeds:
        starts.append(np.array(s0, float).flatten())
        for _ in range(noise_reps):
            x = np.array(s0, float).flatten()
            x += rng.normal(0, 0.03, x.size)
            starts.append(x)
    for _ in range(n_random):
        sq = np.column_stack([rng.uniform(0.2, k - 0.2, n), rng.uniform(0.2, k - 0.2, n),
                              rng.uniform(-0.3, 0.3, n), rng.uniform(0.3, 1.0, n)])
        starts.append(sq.flatten())
    best = None
    from repair import repair
    for i, x0 in enumerate(starts):
        res = minimize(penalized_F, x0, args=(k, n), method='Nelder-Mead',
                       options=dict(maxiter=maxiter, xatol=1e-5, fatol=1e-7, adaptive=True))
        sq = repair([tuple(row) for row in res.x.reshape(n, 4)], k)
        feas = feasible(sq, k, tol=1e-9)
        r = analyze(sq, k, M=800)
        results.append((res.fun, float(r['F']), feas, i))
        if feas and (best is None or r['F'] < best[0]):
            best = (float(r['F']), sq)
        print(f'start {i}: pen={res.fun:.5f} repairedF={r["F"]:.5f} feas={feas}', flush=True)
    return best, results

if __name__ == '__main__':
    k = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    n = k * k + 1
    if k == 2:
        seeds = seeds_k2()
    else:
        d4 = k / (k + 1)
        row = [((i + 0.5) * d4, d4/2, 0, d4) for i in range(k + 1)] + \
              [(0.5 + i, 0.5 + j, 0, 1) for j in range(1, k) for i in range(k)]
        seeds = [row]
    best, _ = run(k, n, seeds)
    print('BEST feasible F:', best[0] if best else None)
    if best:
        # verify at doubled resolution + exact feasibility
        r = analyze(best[1], k, M=1600)
        print('doubled-res F:', float(r['F']), 'piG:', float(r['piG']), 's:', float(r['s']),
              'sumd:', float(r['sumd']), 'feasible exact:', feasible(best[1], k, tol=1e-9))
        json.dump(best[1], open(f'best_k{k}.json', 'w'))
        print('config:', [tuple(round(float(v), 6) for v in sq) for sq in best[1]])
