#!/usr/bin/env python3
"""Refine exp3: add theta=1 deg, re-run theta=10 deg with more starts and
warm starts from the (good) theta=5 solution."""
import numpy as np
import importlib.util
spec = importlib.util.spec_from_file_location("e3", "exp3_interface.py")
e3 = importlib.util.module_from_spec(spec); spec.loader.exec_module(e3)
from scipy.optimize import minimize

def solve_with_warm(theta, warm_list, nstarts=80, seed=99):
    Cpoly = e3.tilted_square(theta)
    rng = np.random.default_rng(seed)
    base = np.array([[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]],
                    dtype=float)
    w = np.cos(theta) + np.sin(theta)
    starts = [base.ravel().copy(), (base * (0.5 + w / 2)).ravel()] + list(warm_list)
    while len(starts) < nstarts:
        starts.append((base * rng.uniform(0.9, 1.3)).ravel() + rng.normal(0, 0.15, 16))
    best = None
    for x0 in starts:
        x = np.array(x0, dtype=float)
        for lam in [30.0, 300.0, 3000.0, 30000.0]:
            res = minimize(e3.objective, x, args=(Cpoly, lam), method='L-BFGS-B',
                           options=dict(maxiter=500, ftol=1e-12, gtol=1e-10))
            x = res.x
        ov = e3.total_overlap(x, Cpoly)
        cov = e3.covered_exact(x, Cpoly)
        unc = 9.0 - cov
        if ov < 1e-5 and (best is None or unc < best[0]):
            best = (unc, ov, x.copy())
    return best

import glob
warm = []
for f in glob.glob("exp3_sol_theta*.npy"):
    warm.append(np.load(f))

for th_deg in [1, 10]:
    th = np.radians(th_deg)
    best = solve_with_warm(th, warm, nstarts=80, seed=th_deg + 100)
    unc, ov, x = best
    print(f"theta={th_deg}: uncovered={unc:.6f} residual_ov={ov:.2e} "
          f"slope(unc/theta)={unc/th:.4f} sin2t={np.sin(2*th):.6f}", flush=True)
    np.save(f"exp3_sol_theta{th_deg}_refined.npy", x)
