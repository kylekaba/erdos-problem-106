#!/usr/bin/env python3
"""Independent rasterization check of exp3 solutions: sample-based union area."""
import numpy as np
import importlib.util, glob, re
spec = importlib.util.spec_from_file_location("e3", "exp3_interface.py")
e3 = importlib.util.module_from_spec(spec); spec.loader.exec_module(e3)

rng = np.random.default_rng(42)
NS = 4_000_000
pts = rng.uniform(-1.5, 1.5, (NS, 2))

for f in sorted(glob.glob("exp3_sol_theta*.npy"),
                key=lambda s: int(re.search(r'theta(\d+)', s).group(1))):
    th_deg = int(re.search(r'theta(\d+)', f).group(1))
    th = np.radians(th_deg)
    x = np.load(f)
    zs = x.reshape(8, 2)
    ct, st = np.cos(th), np.sin(th)
    u = ct * pts[:, 0] + st * pts[:, 1]
    v = -st * pts[:, 0] + ct * pts[:, 1]
    inside = (np.abs(u) <= 0.5) & (np.abs(v) <= 0.5)
    for z in zs:
        inside |= (np.abs(pts[:, 0] - z[0]) <= 0.5) & (np.abs(pts[:, 1] - z[1]) <= 0.5)
    cov_mc = inside.mean() * 9.0
    unc_mc = 9.0 - cov_mc
    se = 9.0 * np.sqrt(inside.mean() * (1 - inside.mean()) / NS)
    unc_exact = 9.0 - e3.covered_exact(x, e3.tilted_square(th))
    print(f"theta={th_deg:3d}: uncovered MC={unc_mc:.5f} (+-{se:.5f})  exact-formula={unc_exact:.5f}")
