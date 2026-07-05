#!/usr/bin/env python3
"""Adversarial stress test of (**): simulate ENEMY-shaped arc systems
(N+1 arcs, sum w = N + t with t ~ 1/2, widths near 1) with various phase
strategies, and measure the ratio  kappa * min(HxE,HyE) / (1-t)^2  (>= 1 claimed)
and kappa itself (enemy needs kappa < 2c = 1/200).
Since no real enemy packing exists, this bounds what the ARC data alone permits:
it shows which phase strategies minimize kappa and what stacking they are forced into.
"""
import numpy as np
from dipstack_check import axis_report, kappa_exact

def make_ws(rng, M, N, t, spread):
    # widths near 1 with one-sided spread; renormalize to sum = N + t, keep in (0,2)
    w = 1.0 + rng.uniform(-spread, spread, M)
    w = w - (w.sum() - (N + t)) / M
    return np.clip(w, 0.05, 1.95)

def system(rng, M, w, mode):
    if mode == 'random':
        a = rng.uniform(0, 1, M)
    elif mode == 'equid':
        a = (np.arange(M) / M + rng.uniform(0, 1)) % 1.0
    elif mode == 'clustered':
        a = rng.normal(0.0, 0.01, M) % 1.0
    elif mode == 'column':   # deficient-column style: undersize arcs share phase,
        a = np.zeros(M)      # i.e. all left endpoints aligned
    elif mode == 'winding':  # phases wind once around the circle scaled by deficit
        a = np.cumsum(w) % 1.0
    return [(a[i], a[i] + w[i]) for i in range(M)]

def run():
    rng = np.random.default_rng(42)
    k, N = 4, 16
    M = N + 1
    print(f"{'mode':>10} {'spread':>7} {'t':>6} | {'kappa':>8} {'dx':>7} {'dy':>7} "
          f"{'Hx':>3} {'Hy':>3} | {'ratio**':>8} {'ratio_w':>8}")
    worst = np.inf
    for mode in ['random', 'equid', 'clustered', 'column', 'winding']:
        for spread in [0.02, 0.07, 0.15]:
            best_kappa, rec = np.inf, None
            for trial in range(60):
                t = 0.5
                w = make_ws(rng, M, N, t, spread)
                ix = system(rng, M, w, mode)
                iy = system(rng, M, w, mode)   # independent draws per axis
                ax = axis_report(ix, N); ay = axis_report(iy, N)
                kap = kappa_exact(ax, ay, N)
                mh = min(ax['HE'], ay['HE'])
                ratio = kap * mh / (1 - t) ** 2 if mh > 0 else np.inf
                ratio_w = kap * ax['HE'] * ay['HE'] / (1 - t) ** 2 if mh > 0 else np.inf
                worst = min(worst, ratio)
                if kap < best_kappa:
                    best_kappa, rec = kap, (ax, ay, kap, ratio, ratio_w)
            ax, ay, kap, ratio, ratio_w = rec
            print(f"{mode:>10} {spread:7.2f} {0.5:6.2f} | {kap:8.4f} {ax['delta']:7.4f} "
                  f"{ay['delta']:7.4f} {ax['HE']:3d} {ay['HE']:3d} | {ratio:8.3f} {ratio_w:8.3f}")
    print(f"\nworst kappa*minH/(1-t)^2 over all trials: {worst:.4f}  (claim: >= 1)")

if __name__ == '__main__':
    run()
