#!/usr/bin/env python3
"""Experiment 2b: shift-conflict between two coherently tilted grains.

Facts this probes:
(a) An aligned half-open unit cell with integer corner contains exactly 1
    point of Z^2+shift for EVERY shift -> the aligned bulk of a packing is
    shift-neutral; only tilted grains care about the shift.
(b) exp2: a single m x m grain tilted by t (squares side d=1/(cos t+sin t))
    admits shifts capturing all m^2 lattice points iff roughly
    sin 2t <= 1/(m-1); measure mu(t,m) of the capture set of shifts.
(c) TWO grains with tilts t1, t2 and independent offsets must share ONE
    shift. Measure max_shift [c_A + c_B] vs m^2 + m^2 and vs
    ceil(sum d) = ceil(2 m^2 d).

Grain model: big tilted square of side m*d, d = 1/(cos t + sin t),
random center offset; count = lattice points inside (half-open in own frame).
"""
import numpy as np

def grain_counts(m, t, center, n2=400):
    ct, st = np.cos(t), np.sin(t)
    d = 1.0 / (ct + st)
    L = m * d
    cx, cy = center
    xs = (np.arange(n2) + 0.5) / n2 + np.sqrt(2) * 1e-5
    ys = (np.arange(n2) + 0.5) / n2 + np.sqrt(3) * 1e-5
    X0, Y0 = np.meshgrid(xs, ys, indexing='ij')
    cnt = np.zeros_like(X0)
    for i in range(int(np.floor(cx - L)), int(np.ceil(cx + L)) + 1):
        for j in range(int(np.floor(cy - L)), int(np.ceil(cy + L)) + 1):
            px = X0 + i - cx
            py = Y0 + j - cy
            u = ct * px + st * py
            v = -st * px + ct * py
            cnt += ((u >= -L/2) & (u < L/2) & (v >= -L/2) & (v < L/2))
    return cnt, d

def main():
    rng = np.random.default_rng(3)
    m = 5
    print(f"m={m}; capture threshold sin(2t)<=1/(m-1) -> t* = {0.5*np.arcsin(1/(m-1)):.4f}")
    print("single-grain capture-set measure mu(t):")
    for t in [0.02, 0.05, 0.08, 0.10, 0.12, 0.126]:
        cnt, d = grain_counts(m, t, (7.3, 4.1))
        mu = float((cnt >= m*m).mean())
        print(f"  t={t:.3f}: max c={int(cnt.max())}, mu(capture)={mu:.4f}, "
              f"sum d={m*m*d:.3f}, ceil={int(np.ceil(m*m*d - 1e-12))}", flush=True)
    print("\ntwo grains, one shared shift (5 random relative offsets each):")
    for (t1, t2) in [(0.08, -0.08), (0.08, 0.0), (0.10, -0.10), (0.10, 0.05),
                     (0.12, -0.12), (0.05, -0.05)]:
        worst = None
        for trial in range(5):
            c1_center = tuple(rng.uniform(0, 20, 2))
            c2_center = tuple(rng.uniform(0, 20, 2))
            cnt1, d1 = grain_counts(m, t1, c1_center)
            cnt2, d2 = grain_counts(m, abs(t2), c2_center) if t2 >= 0 else grain_counts_neg(m, t2, c2_center)
            tot = cnt1 + cnt2
            best = int(tot.max())
            sumd = m*m*(d1 + d2)
            margin = best - int(np.ceil(sumd - 1e-12))
            if worst is None or margin < worst[0]:
                worst = (margin, best, sumd)
        print(f"  t1={t1:+.2f} t2={t2:+.2f}: worst over offsets: "
              f"max_shift(cA+cB)={worst[1]}, sum d={worst[2]:.3f}, "
              f"ceil={int(np.ceil(worst[2]-1e-12))}, margin={worst[0]}", flush=True)

def grain_counts_neg(m, t, center):
    # tilt -|t|: reflect across the diagonal. cnt_{-t,(cx,cy)}(x0,y0) =
    # cnt_{+t,(cy,cx)}(y0,x0)  (the shift grids for x and y differ only by a
    # tiny jitter, negligible). d is the same for +-t.
    cnt, d = grain_counts(m, abs(t), (center[1], center[0]))
    return cnt.T, d

if __name__ == '__main__':
    main()
