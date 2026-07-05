"""F3 numerical rig: k=2 (N=4, n=5) packings, AP sea + one tilted square.
Computes |Av|, s, g, comparison quantities for inscribed-AP replacement.
Grid over torus shifts p in [0,1)^2, pixel centers, M x M.
Square = (cx, cy, side, angle). Point-in test in rotated frame, strict-ish.
"""
import numpy as np

K = 2
N = K*K

def masks(squares, M=600):
    """Return per-square capture-count arrays (M,M) int8 and C."""
    idx = (np.arange(M) + 0.5) / M
    PX, PY = np.meshgrid(idx, idx, indexing='ij')
    counts = []
    for (cx, cy, d, th) in squares:
        cnt = np.zeros((M, M), dtype=np.int8)
        ct, st = np.cos(th), np.sin(th)
        for i in range(K):
            for j in range(K):
                x = PX + i - cx
                y = PY + j - cy
                u = ct*x + st*y
                v = -st*x + ct*y
                inside = (np.abs(u) <= d/2) & (np.abs(v) <= d/2)
                cnt += inside.astype(np.int8)
        counts.append(cnt)
    counts = np.array(counts)          # (n, M, M)
    C = counts.sum(axis=0)
    return counts, C

def region_hit_mask(inside_fn, M=600):
    """Mask of shifts p such that some candidate lattice point lies in region."""
    idx = (np.arange(M) + 0.5) / M
    PX, PY = np.meshgrid(idx, idx, indexing='ij')
    hit = np.zeros((M, M), dtype=bool)
    for i in range(K):
        for j in range(K):
            hit |= inside_fn(PX + i, PY + j)
    return hit

def in_tilted(cx, cy, d, th):
    ct, st = np.cos(th), np.sin(th)
    def f(X, Y):
        x, y = X - cx, Y - cy
        u = ct*x + st*y
        v = -st*x + ct*y
        return (np.abs(u) <= d/2) & (np.abs(v) <= d/2)
    return f

def stats(squares, M=600):
    counts, C = masks(squares, M)
    Av = (C == N)
    over = (C > N)
    s = sum((1-d)**2 for (_,_,d,_) in squares)
    g = N - sum(d*d for (_,_,d,_) in squares)
    return dict(Av=Av, avm=Av.mean(), s=s, g=g, over=over.mean(),
                counts=counts, C=C)

def validate(squares, tol=1e-9):
    """Crude overlap/containment check via fine sampling of each square."""
    # containment
    for (cx, cy, d, th) in squares:
        ct, st = np.cos(th), np.sin(th)
        w = d/2*(abs(ct)+abs(st))
        if cx - w < -tol or cx + w > K+tol or cy - w < -tol or cy + w > K+tol:
            return False
    # pairwise disjoint: sample points of each square, test in others
    for a in range(len(squares)):
        cx, cy, d, th = squares[a]
        ct, st = np.cos(th), np.sin(th)
        m = 60
        uu = (np.arange(m)+0.5)/m*d - d/2
        U, V = np.meshgrid(uu, uu, indexing='ij')
        X = cx + ct*U - st*V
        Y = cy + st*U + ct*V
        for b in range(len(squares)):
            if b == a: continue
            f = in_tilted(*squares[b])
            # shrink test points slightly inward already via pixel centers
            if f(X, Y).any():
                return False
    return True

def compare_inscribed(squares, tilt_index, M=600):
    """Full comparison: P vs P' (tilted square -> inscribed AP square)."""
    cx, cy, d, th = squares[tilt_index]
    c = np.cos(th) + np.sin(th)
    dp = d / c
    sq2 = list(squares)
    sq2[tilt_index] = (cx, cy, dp, 0.0)
    A = stats(squares, M)
    B = stats(sq2, M)
    # R = S_tilt \ inscribed
    f_tilt = in_tilted(cx, cy, d, th)
    f_ins  = in_tilted(cx, cy, dp, 0.0)
    hitR = region_hit_mask(lambda X, Y: f_tilt(X, Y) & ~f_ins(X, Y), M)
    piR = hitR.mean()
    diff = (A['Av'] & ~B['Av']).mean()          # |Av \ Av'|
    subset_viol = (B['Av'] & ~A['Av']).mean()   # should be 0 (Av' subset Av)
    piR_minus_piG = (hitR & A['Av']).mean()     # |pi(R) \ pi(G)| (pi(G)=~Av)
    areaR = d*d - dp*dp
    ds = (1-dp)**2 - (1-d)**2
    return dict(avm=A['avm'], s=A['s'], g=A['g'], margin=A['s']-A['avm'],
                avm2=B['avm'], s2=B['s'], g2=B['g'], margin2=B['s2'] if False else B['s']-B['avm'],
                diff=diff, piR=piR, piRnG=piR_minus_piG, areaR=areaR, ds=ds,
                subset_viol=subset_viol, over=A['over'])
