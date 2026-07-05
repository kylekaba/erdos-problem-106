#!/usr/bin/env python3
"""
Lemma K (integer anti-concentration):
  phi, psi independent integer-valued, E[phi]=mu1>=0, E[psi]=mu2>=0
  =>  E[(phi+psi-1)_+] >= mu1*mu2.
MC over random discrete laws; also packing-level checks:
  K :  t>=0  =>  kappa >= (1-t)^2   (kappa = E[(2N+1-P-Q)_+])
  K':  (eps+tau)^2 <= 2*tau - sum(m_i)   [uses T6 margins; MPI chain]
"""
import numpy as np
from math import cos, sin, sqrt
from dipstack_check import (axis_report, kappa_exact, bbox, test_packing,
                            deficient_column, split_cell, t12_column_tiling,
                            running_bond_deficient_row, tilted_grain_k2,
                            jittered_split_grid, check_packing)

def lemma_mc(trials=200000, seed=3):
    rng = np.random.default_rng(seed)
    vals = np.arange(-3, 6)  # supports {-3..5}
    worst = np.inf; fails = 0
    for _ in range(trials):
        def law():
            p = rng.dirichlet(np.ones(len(vals)) * rng.uniform(0.2, 2.0))
            return p
        for _try in range(200):
            p1, p2 = law(), law()
            mu1 = float(vals @ p1); mu2 = float(vals @ p2)
            if 0 <= mu1 <= 1 and 0 <= mu2 <= 1:
                break
        else:
            continue
        s = vals[:, None] + vals[None, :] - 1
        E = float((np.maximum(s, 0) * np.outer(p1, p2)).sum())
        slack = E - mu1 * mu2
        worst = min(worst, slack)
        if slack < -1e-12:
            fails += 1
    print(f"Lemma K MC: {trials} trials, failures={fails}, worst slack={worst:.3e}")
    return fails == 0

def margins(d, th):
    if th == 0:
        return 0.0
    u1 = cos(th) + sin(th); sg = u1 - 1.0; w = d * u1
    if w <= 1:
        return d * sg * (2 - d - w)
    if d <= u1:
        return (1 - d) ** 2
    return -d * sg * (d + w - 2)

def packing_KKp(name, squares, k):
    N = k * k
    check_packing(squares, k)
    xin = []; yin = []
    for sq in squares:
        (x0, x1), (y0, y1) = bbox(sq)
        xin.append((x0, x1)); yin.append((y0, y1))
    ax = axis_report(xin, N); ay = axis_report(yin, N)
    kap = kappa_exact(ax, ay, N)
    ds = [sq[2] for sq in squares]; ths = [sq[3] for sq in squares]
    eps = sum(ds) - N
    t = ax['t']; tau = t - eps
    Sm = sum(margins(d, th) for d, th in zip(ds, ths))
    okK = True
    if t >= 0:
        okK = kap >= (1 - t) ** 2 - 1e-9
    okKp = max(eps + tau, 0.0) ** 2 <= 2 * tau - Sm + 1e-9
    okT6 = 2 * eps <= 1 - Sm - kap + 1e-9
    print(f"{name:36s} t={t:+.4f} kappa={kap:.4f} (1-t)^2={(max(1-t,0))**2:.4f} "
          f"K:{okK}  K'(lhs={max(eps+tau,0.0)**2:.4f} rhs={2*tau-Sm:.4f}):{okKp}  T6:{okT6}")
    return okK and okKp and okT6

def diamond_pair():
    # k=1: two 45-degree squares of side 0.47 on the diagonal of [0,1]^2
    s = 0.47
    a = s / sqrt(2) + 1e-6
    return [(a, a, s, np.pi / 4), (1 - a, 1 - a, s, np.pi / 4)], 1

def tilted_column(k=2, t=0.03):
    # F4's tilted deficient column P_k(t): column squares side c/u1(t), tilt t
    from math import cos as C, sin as S
    u1 = C(t) + S(t)
    c = k / (k + 1); d = c / u1
    sq = []
    for r in range(k + 1):
        sq.append((c / 2, r * c + c / 2, d, t))
    for i in range(1, k):
        for j in range(k):
            sq.append((i + 0.5, j + 0.5, 1.0, 0.0))
    return sq, k

if __name__ == '__main__':
    ok = lemma_mc()
    ok &= packing_KKp("deficient column k=3", deficient_column(3), 3)
    ok &= packing_KKp("deficient column k=4", deficient_column(4), 4)
    ok &= packing_KKp("split cell k=2", split_cell(2, 0.3), 2)
    sq, k = t12_column_tiling(); ok &= packing_KKp("T12 column tiling k=4", sq, k)
    ok &= packing_KKp("deficient row k=3", running_bond_deficient_row(3), 3)
    sq, k = tilted_grain_k2(); ok &= packing_KKp("tilted 2x2 grain k=2", sq, k)
    ok &= packing_KKp("jittered split grid k=3", jittered_split_grid(3), 3)
    sq, k = diamond_pair(); ok &= packing_KKp("diamond pair k=1", sq, k)
    sq, k = tilted_column(2, 0.03); ok &= packing_KKp("tilted deficient column k=2", sq, k)
    sq, k = tilted_column(3, 0.02); ok &= packing_KKp("tilted deficient column k=3", sq, k)
    print("ALL PASS" if ok else "*** FAIL ***")
