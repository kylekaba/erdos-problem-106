#!/usr/bin/env python3
"""Experiment 1: single-square lattice-count defect vs projection surplus.

Square S of side d, tilted by theta, fixed placement (center).
For shift (x0,y0) in [0,1)^2:
  p = #{j in Z : vertical line x = x0+j meets S}   (projection interval count)
  q = analog horizontal
  c = #{points of Z^2 + (x0,y0) in S}
Half-open convention in the square's own frame: u,v in [-d/2, d/2).
Shift grid is jittered by irrational offsets so boundary ties never occur
(closed vs half-open then irrelevant).
Checks: E[c]=d^2, E[p]=E[q]=d(cos t + sin t).
Defect statistics of D = p+q-1-c: P(D>0), E[D^+], max D.
Projection surplus: E[p]+E[q]-2d = 2d(cos t + sin t - 1) ~ 2d*t.
"""
import numpy as np
import json, sys

def stats_single(d, theta_deg, n=600, center=(0.37, 0.61)):
    t = np.radians(theta_deg)
    ct, st = np.cos(t), np.sin(t)
    cx, cy = center
    w = d * (abs(ct) + abs(st))          # projection width (both axes, it's a square)
    xs = (np.arange(n) + 0.5) / n + np.sqrt(2) * 1e-4
    ys = (np.arange(n) + 0.5) / n + np.sqrt(3) * 1e-4
    X0, Y0 = np.meshgrid(xs, ys, indexing='ij')
    # p(x0) = #{j : x0 + j in [cx - w/2, cx + w/2)}
    a, b = cx - w / 2.0, cx + w / 2.0
    p = np.ceil(b - X0) - np.ceil(a - X0)
    ay, by = cy - w / 2.0, cy + w / 2.0
    q = np.ceil(by - Y0) - np.ceil(ay - Y0)
    # c(x0,y0): lattice points in S
    c_cnt = np.zeros_like(X0)
    imin, imax = int(np.floor(a)) - 1, int(np.ceil(b)) + 1
    jmin, jmax = int(np.floor(ay)) - 1, int(np.ceil(by)) + 1
    for i in range(imin, imax + 1):
        for j in range(jmin, jmax + 1):
            px = X0 + i - cx
            py = Y0 + j - cy
            u = ct * px + st * py
            v = -st * px + ct * py
            c_cnt += ((u >= -d/2) & (u < d/2) & (v >= -d/2) & (v < d/2))
    D = p + q - 1 - c_cnt
    Dp = np.maximum(D, 0.0)
    return dict(d=d, theta_deg=theta_deg,
                Ec=float(c_cnt.mean()), Ep=float(p.mean()), Eq=float(q.mean()),
                Pdef=float((D > 0).mean()),
                EDplus=float(Dp.mean()),
                maxD=int(D.max()),
                surplus=float(2*d*(ct+st-1)))

def main():
    ds = [0.85, 0.9, 0.95, 1.0, 1.05, 1.1, 1.2]
    thetas = [0, 1, 2, 4, 8, 15, 30, 45]
    out = []
    for d in ds:
        for th in thetas:
            r = stats_single(d, th, n=600)
            r['Ec_expected'] = d*d
            r['Ep_expected'] = d*(np.cos(np.radians(th))+np.sin(np.radians(th)))
            out.append(r)
            print(f"d={d:5.2f} th={th:5.1f}  Ec={r['Ec']:.5f}(exp {r['Ec_expected']:.5f})"
                  f" Ep={r['Ep']:.5f}(exp {r['Ep_expected']:.5f})"
                  f" P(D>0)={r['Pdef']:.5f} E[D+]={r['EDplus']:.6f} maxD={r['maxD']}"
                  f" surplus={r['surplus']:.6f}"
                  f" ratio={r['EDplus']/r['surplus'] if r['surplus']>0 else float('nan'):.4f}",
                  flush=True)
    # placement invariance check
    print("\n--- placement invariance (3 random placements) ---", flush=True)
    rng = np.random.default_rng(7)
    for d in [0.95, 1.0, 1.1]:
        for th in [4, 30]:
            vals = []
            for _ in range(3):
                ctr = tuple(rng.uniform(0, 1, 2))
                r = stats_single(d, th, n=600, center=ctr)
                vals.append(r['EDplus'])
            print(f"d={d} th={th}: E[D+] over 3 placements = {[f'{v:.6f}' for v in vals]}", flush=True)
    # small-theta scaling fit on theta in {1,2,4,8} deg
    print("\n--- small-theta scaling fits: E[D+] ~ C * theta^alpha (theta in radians) ---", flush=True)
    fit_th = [1, 2, 4, 8]
    for d in ds:
        ys = []
        for th in fit_th:
            r = next(o for o in out if o['d'] == d and o['theta_deg'] == th)
            ys.append(r['EDplus'])
        ys = np.array(ys)
        if np.all(ys > 0):
            xs = np.log(np.radians(fit_th))
            A = np.vstack([xs, np.ones_like(xs)]).T
            sol, *_ = np.linalg.lstsq(A, np.log(ys), rcond=None)
            alpha, logC = sol
            print(f"d={d:5.2f}: alpha={alpha:.3f}, C={np.exp(logC):.4f}   "
                  f"(E[D+] at 1,2,4,8 deg: {ys})", flush=True)
        else:
            print(f"d={d:5.2f}: E[D+] contains zeros at small theta: {ys}", flush=True)
    with open('exp1_results.json', 'w') as f:
        json.dump(out, f, indent=1)

if __name__ == '__main__':
    main()
