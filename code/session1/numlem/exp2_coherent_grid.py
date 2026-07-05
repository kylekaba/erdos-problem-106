#!/usr/bin/env python3
"""Experiment 2: coherent tilted k x k grid in arena [0,k]^2.

Configuration: k x k grid of squares of side d = 1/(cos t + sin t), the whole
block (side k*d) rigidly rotated by t about the arena center (k/2,k/2).
Bounding box of the block = k*d*(cos t + sin t) = k, so it fits exactly.
The little squares exactly tile the big tilted square of side k*d, so
sum_i c_i(shift) = #(Z^2 + shift) inside the big tilted square (verified
directly for k=5).
Each little square's axis projection has width d*(cos t+sin t) = 1 exactly,
so sum_i p_i = k^2 for a.e. shift (verified).

Half-open convention in the block frame: u,v in [-L/2, L/2), L = k*d.

Report: max over shift grid of sum c_i; max_x sum p_i; max_y sum q_i;
compare with N = k^2, sum d_i = k^2 * d, ceil(sum d_i).
"""
import numpy as np

def run(k, t, n2=300, n1=4000, verify_per_square=False):
    ct, st = np.cos(t), np.sin(t)
    d = 1.0 / (ct + st)
    L = k * d
    cx = cy = k / 2.0
    # containment check: corners of big tilted square
    corners = np.array([[u, v] for u in (-L/2, L/2) for v in (-L/2, L/2)])
    R = np.array([[ct, -st], [st, ct]])
    pts = corners @ R.T + np.array([cx, cy])
    assert pts.min() >= -1e-9 and pts.max() <= k + 1e-9, (pts.min(), pts.max())

    # 2-D shift grid (jittered), count lattice points in big tilted square
    xs = (np.arange(n2) + 0.5) / n2 + np.sqrt(2) * 1e-5
    ys = (np.arange(n2) + 0.5) / n2 + np.sqrt(3) * 1e-5
    X0, Y0 = np.meshgrid(xs, ys, indexing='ij')
    cnt = np.zeros_like(X0)
    for i in range(-1, k + 2):
        for j in range(-1, k + 2):
            px = X0 + i - cx
            py = Y0 + j - cy
            u = ct * px + st * py
            v = -st * px + ct * py
            cnt += ((u >= -L/2) & (u < L/2) & (v >= -L/2) & (v < L/2))
    maxc = int(cnt.max()); meanc = float(cnt.mean())

    if verify_per_square:
        # direct per-square sum at 5 random shifts
        rng = np.random.default_rng(0)
        for _ in range(5):
            x0, y0 = rng.uniform(0, 1, 2)
            tot_direct = 0
            for a in range(k):
                for b in range(k):
                    # square (a,b): in block frame [a*d - L/2, (a+1)*d - L/2) etc.
                    for i in range(-1, k + 2):
                        for j in range(-1, k + 2):
                            px, py = x0 + i - cx, y0 + j - cy
                            u = ct * px + st * py
                            v = -st * px + ct * py
                            if (a*d - L/2 <= u < (a+1)*d - L/2) and (b*d - L/2 <= v < (b+1)*d - L/2):
                                tot_direct += 1
            tot_big = 0
            for i in range(-1, k + 2):
                for j in range(-1, k + 2):
                    px, py = x0 + i - cx, y0 + j - cy
                    u = ct * px + st * py
                    v = -st * px + ct * py
                    if (-L/2 <= u < L/2) and (-L/2 <= v < L/2):
                        tot_big += 1
            assert tot_direct == tot_big, (tot_direct, tot_big)

    # 1-D: sum_i p_i over x-shift grid. Square (a,b) center in block frame:
    # ((a+0.5)d - L/2, (b+0.5)d - L/2); rotated + translated center x-coord:
    aa, bb = np.meshgrid(np.arange(k), np.arange(k), indexing='ij')
    ub = (aa + 0.5) * d - L/2
    vb = (bb + 0.5) * d - L/2
    cxs = (ct * ub - st * vb + cx).ravel()   # projection centers, width w=1
    x0s = (np.arange(n1) + 0.5) / n1 + np.sqrt(5) * 1e-6
    # p_i(x0) = ceil(cx_i + 0.5 - x0) - ceil(cx_i - 0.5 - x0)
    A = cxs[None, :] - x0s[:, None]
    P = (np.ceil(A + 0.5) - np.ceil(A - 0.5)).sum(axis=1)
    maxP = int(P.max()); minP = int(P.min())

    sumd = k * k * d
    return dict(k=k, t=t, d=d, sumd=sumd, ceil_sumd=int(np.ceil(sumd - 1e-12)),
                N=k*k, maxc=maxc, meanc=meanc, area=L*L, maxP=maxP, minP=minP)

def main():
    for k in [5, 10, 20]:
        print(f"\n=== k = {k}  (N = {k*k}) ===")
        ts = [0.0, 0.2/k**2, 1.0/k**2, 5.0/k**2, 1.0/k, 5.0/k]
        for t in ts:
            r = run(k, t, n2=300, n1=4000, verify_per_square=(k == 5 and t == ts[2]))
            verdict = "count >= ceil(sum d)" if r['maxc'] >= r['ceil_sumd'] else "COUNT FALLS SHORT"
            print(f"t={t:.6f} (k^2 t={t*k*k:.2f})  d={r['d']:.6f}  sum d_i={r['sumd']:.4f} "
                  f"ceil={r['ceil_sumd']}  area={r['area']:.4f}  max_shift sum c={r['maxc']} "
                  f"mean={r['meanc']:.3f}  max_x sum p={r['maxP']} (min {r['minP']})  -> {verdict}",
                  flush=True)

if __name__ == '__main__':
    main()
