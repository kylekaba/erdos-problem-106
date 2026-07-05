#!/usr/bin/env python3
"""Experiment 3: gap-forcing at a tilt interface.

Box B = [-1.5,1.5]^2 (area 9). Central unit square C tilted by theta, center
fixed at origin. 8 axis-parallel unit squares, translation only (16 vars).
All 9 squares pairwise DISJOINT (interiors); the 8 AP squares MAY protrude
outside B (for theta>0, "all inside B" is infeasible: total area = box area
and exact tilings of a rectangle by squares are axis-parallel).
Maximize covered area inside B; report uncovered(theta) = 9 - covered.

covered = area(C) [C always inside B: circumradius sqrt(2)/2 < 1.5]
        + sum_m area(A_m cap B)  -  (pairwise overlaps, driven to ~0 by penalty)
Exact geometry: rectangle-rectangle overlaps in closed form; C-vs-rectangle
and triple corrections via Sutherland-Hodgman convex clipping + shoelace.
Optimizer: scipy L-BFGS-B, numeric gradient, penalty ramp, multistart.
Optimizer values are UPPER bounds on the true minimal uncovered area.
"""
import numpy as np
from scipy.optimize import minimize

BOX = 1.5

def clip_poly(poly, a, b, c):
    """Clip polygon (list of 2-vectors) by half-plane a*x+b*y<=c."""
    out = []
    n = len(poly)
    for i in range(n):
        P, Q = poly[i], poly[(i + 1) % n]
        fp = a * P[0] + b * P[1] - c
        fq = a * Q[0] + b * Q[1] - c
        if fp <= 0:
            out.append(P)
            if fq > 0:
                s = fp / (fp - fq)
                out.append(P + s * (Q - P))
        elif fq <= 0:
            s = fp / (fp - fq)
            out.append(P + s * (Q - P))
    return out

def poly_area(poly):
    if len(poly) < 3:
        return 0.0
    x = np.array([p[0] for p in poly]); y = np.array([p[1] for p in poly])
    return 0.5 * abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1)))

def clip_rect(poly, xlo, xhi, ylo, yhi):
    for (a, b, c) in [(-1, 0, -xlo), (1, 0, xhi), (0, -1, -ylo), (0, 1, yhi)]:
        poly = clip_poly(poly, a, b, c)
        if not poly:
            return []
    return poly

def tilted_square(theta):
    t = theta
    R = np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
    base = np.array([[-0.5, -0.5], [0.5, -0.5], [0.5, 0.5], [-0.5, 0.5]])
    return [R @ p for p in base]

def rect_overlap(z1, z2):
    dx = abs(z1[0] - z2[0]); dy = abs(z1[1] - z2[1])
    return max(0.0, 1.0 - dx) * max(0.0, 1.0 - dy)

def area_in_box(z):
    xlo, xhi = max(z[0] - 0.5, -BOX), min(z[0] + 0.5, BOX)
    ylo, yhi = max(z[1] - 0.5, -BOX), min(z[1] + 0.5, BOX)
    return max(0.0, xhi - xlo) * max(0.0, yhi - ylo)

def overlap_C_rect(Cpoly, z):
    return poly_area(clip_rect(Cpoly, z[0] - 0.5, z[0] + 0.5, z[1] - 0.5, z[1] + 0.5))

def objective(x, Cpoly, lam):
    zs = x.reshape(8, 2)
    covered = 1.0  # central square, always inside box
    ov = 0.0
    for m in range(8):
        covered += area_in_box(zs[m])
        ov += overlap_C_rect(Cpoly, zs[m])
        for m2 in range(m + 1, 8):
            ov += rect_overlap(zs[m], zs[m2])
    return -(covered - ov) + lam * ov

def total_overlap(x, Cpoly):
    zs = x.reshape(8, 2)
    ov = 0.0
    for m in range(8):
        ov += overlap_C_rect(Cpoly, zs[m])
        for m2 in range(m + 1, 8):
            ov += rect_overlap(zs[m], zs[m2])
    return ov

def covered_exact(x, Cpoly):
    """Union area inside box via inclusion-exclusion truncated at pairs
    (exact when residual overlaps ~ 0; error bounded by triple overlaps)."""
    zs = x.reshape(8, 2)
    cov = 1.0
    ov = 0.0
    for m in range(8):
        cov += area_in_box(zs[m])
        # overlap with C, clipped to box (C inside box so same)
        ov += overlap_C_rect(Cpoly, zs[m])
        for m2 in range(m + 1, 8):
            # rectangle overlap clipped to box
            xlo = max(zs[m][0], zs[m2][0]) - 0.5; xhi = min(zs[m][0], zs[m2][0]) + 0.5
            ylo = max(zs[m][1], zs[m2][1]) - 0.5; yhi = min(zs[m][1], zs[m2][1]) + 0.5
            xlo, xhi = max(xlo, -BOX), min(xhi, BOX)
            ylo, yhi = max(ylo, -BOX), min(yhi, BOX)
            ov += max(0.0, xhi - xlo) * max(0.0, yhi - ylo)
    return cov - ov

def solve(theta, nstarts=40, seed=1):
    Cpoly = tilted_square(theta)
    rng = np.random.default_rng(seed)
    base = np.array([[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]],
                    dtype=float)
    best = None
    w = np.cos(theta) + np.sin(theta)
    for s in range(nstarts):
        if s == 0:
            x0 = base.ravel().copy()
        elif s == 1:
            x0 = (base * (0.5 + w / 2)).ravel()  # hug the bounding box of C
        else:
            x0 = (base * rng.uniform(0.9, 1.3)).ravel() + rng.normal(0, 0.15, 16)
        x = x0
        for lam in [30.0, 300.0, 3000.0, 30000.0]:
            res = minimize(objective, x, args=(Cpoly, lam), method='L-BFGS-B',
                           options=dict(maxiter=500, ftol=1e-12, gtol=1e-10))
            x = res.x
        ov = total_overlap(x, Cpoly)
        cov = covered_exact(x, Cpoly)
        unc = 9.0 - cov
        if ov < 1e-5 and (best is None or unc < best[0]):
            best = (unc, ov, x.copy())
    return best

def main():
    print("theta_deg  uncovered(optimized)  residual_overlap   sin(2*theta) [bbox construction]")
    results = {}
    for th_deg in [0, 2, 5, 10, 20, 45]:
        th = np.radians(th_deg)
        best = solve(th, nstarts=40, seed=th_deg + 1)
        if best is None:
            print(f"{th_deg:8.1f}  NO FEASIBLE LOCAL OPT FOUND")
            continue
        unc, ov, x = best
        results[th_deg] = unc
        print(f"{th_deg:8.1f}  {unc:0.6f}            {ov:.2e}        {np.sin(2*th):0.6f}", flush=True)
        np.save(f"exp3_sol_theta{th_deg}.npy", x)
    # small-theta exponent fit on {2,5,10} deg
    fit = [(np.radians(t), results[t]) for t in [2, 5, 10] if t in results and results[t] > 0]
    if len(fit) >= 2:
        xs = np.log([f[0] for f in fit]); ys = np.log([f[1] for f in fit])
        A = np.vstack([xs, np.ones_like(xs)]).T
        (alpha, logC), *_ = np.linalg.lstsq(A, ys, rcond=None)
        print(f"\nfit uncovered ~ C*theta^alpha on theta in {{2,5,10}} deg: "
              f"alpha={alpha:.3f}, C={np.exp(logC):.4f}")

if __name__ == '__main__':
    main()
