import numpy as np, itertools, sys

rng = np.random.default_rng(7)

def square_corners(cx, cy, d, th):
    c, s = np.cos(th), np.sin(th)
    h = d/2.0
    pts = np.array([[-h,-h],[h,-h],[h,h],[-h,h]])
    R = np.array([[c,-s],[s,c]])
    return pts @ R.T + np.array([cx,cy])

def inside(k, sq):
    P = square_corners(*sq)
    return P.min() >= -1e-12 and P[:,0].max() <= k+1e-12 and P[:,1].max() <= k+1e-12

def disjoint(sq1, sq2):
    # separating axis theorem for two squares (convex)
    P1, P2 = square_corners(*sq1), square_corners(*sq2)
    for P, Q in ((P1,P2),(P2,P1)):
        for i in range(4):
            e = P[(i+1)%4] - P[i]
            ax = np.array([-e[1], e[0]])
            a1, a2 = P @ ax, Q @ ax
            if a1.max() <= a2.min() + 1e-12 or a2.max() <= a1.min() + 1e-12:
                return True
    return False

def valid_packing(k, sqs):
    for sq in sqs:
        if not inside(k, sq): return False
    for i in range(len(sqs)):
        for j in range(i+1, len(sqs)):
            if not disjoint(sqs[i], sqs[j]): return False
    return True

def count_field(k, sqs, M):
    """C(x,y) on MxM shift grid, shifts at ((i+.5)/M,(j+.5)/M) to stay generic."""
    xs = (np.arange(M)+0.5)/M
    X, Y = np.meshgrid(xs, xs, indexing='ij')
    C = np.zeros((M,M), dtype=np.int32)
    for (cx, cy, d, th) in sqs:
        c, s = np.cos(th), np.sin(th)
        r = abs(c)*d/2 + abs(s)*d/2  # half-extent of bbox
        for u in range(int(np.floor(cx-r)), int(np.ceil(cx+r))+1):
            for v in range(int(np.floor(cy-r)), int(np.ceil(cy+r))+1):
                # lattice point (u+x, v+y) in square? rotate into frame
                dx, dy = u + X - cx, v + Y - cy
                a =  c*dx + s*dy
                b = -s*dx + c*dy
                C += ((np.abs(a) < d/2) & (np.abs(b) < d/2))
    return C

def report(name, k, sqs, M=240, fcmb=True):
    N = k*k; n = len(sqs)
    d = np.array([q[2] for q in sqs]); th = [q[3] for q in sqs]
    Sig = d.sum(); A = (d**2).sum(); s = ((1-d)**2).sum(); g = N - A
    C = count_field(k, sqs, M)
    maxC, minC = int(C.max()), int(C.min())
    minhits = N - maxC
    target = 2*Sig - N
    slack = maxC - target
    rhs_minhits = g + s - 1 + (N+1-n)
    Av = float((C == N).mean())
    line = (f"{name}: k={k} n={n} N={N} Sig={Sig:.4f} A={A:.4f} g={g:.4f} s={s:.4f} "
            f"g+s={g+s:.4f} maxC={maxC} minC={minC} 2Sig-N={target:.3f} slack={slack:.3f} "
            f"minhits={minhits} rhs={rhs_minhits:.3f} viol={minhits > rhs_minhits + 1e-9}")
    if fcmb:
        line += f" |Av|={Av:.4f} s+(N+1-n)={s + (N+1-n):.4f} FCMBviol={Av > s + (N+1-n) + 0.01}"
    print(line)
    return slack, minhits - rhs_minhits, Av - (s + (N+1-n))

# ---------- config builders ----------
def units_grid(k, skip=()):
    sqs = []
    for i in range(k):
        for j in range(k):
            if (i,j) in skip: continue
            sqs.append((i+0.5, j+0.5, 1.0, 0.0))
    return sqs

def split_cell(i, j, a, horiz=True):
    b = 1 - a
    if horiz:  # two squares side a and b stacked? place side-by-side corners
        return [(i+a/2, j+a/2, a, 0.0), (i+a+b/2, j+b/2, b, 0.0)]
    return [(i+a/2, j+a/2, a, 0.0), (i+b/2, j+a+b/2, b, 0.0)]

if __name__ == '__main__':
    print("== N1: identity check (2Sig = N+n-g-s) on 3 random configs ==")
    for t in range(3):
        k=2; sqs = units_grid(k, skip=((1,1),)) + split_cell(1,1, 0.3+0.4*rng.random())
        d = np.array([q[2] for q in sqs]); Sig=d.sum(); A=(d**2).sum(); s=((1-d)**2).sum()
        n=len(sqs); N=k*k; g=N-A
        print(f"  resid={2*Sig - (N + n - g - s):.2e}")
    
    print("== N2a: AP tight configs (n=N+1) ==")
    report("split .5/.5", 2, units_grid(2, skip=((1,1),)) + split_cell(1,1,0.5))
    report("split .7/.3", 2, units_grid(2, skip=((1,1),)) + split_cell(1,1,0.7))
    report("split .9/.1", 2, units_grid(2, skip=((1,1),)) + split_cell(1,1,0.9))
    
    print("== N2b: tilted pair in cell (n=N+1, k=2) ==")
    # 3 units + tilted a + AP b in cell (1,1)
    for (a, tha, b) in [(0.55, 0.3, 0.40), (0.6, 0.785, 0.35), (0.5, 0.15, 0.48)]:
        # place tilted square in lower-left of cell, AP in upper-right corner
        wa = a*(np.cos(tha)+np.sin(tha))/2
        sqs = units_grid(2, skip=((1,1),)) + [(1+wa+0.001, 1+wa+0.001, a, tha),
                                              (2-b/2, 2-b/2, b, 0.0)]
        if not valid_packing(2, sqs): print(f"  invalid ({a},{tha},{b})"); continue
        report(f"tiltpair a={a},th={tha},b={b}", 2, sqs)
    
    print("== N2c: missing cell family (n<N+1) ==")
    report("miss1 n=N-1", 2, units_grid(2, skip=((1,1),)), fcmb=True)
    sqs = units_grid(3, skip=((2,2),))
    report("miss1 k=3 n=N-1", 3, sqs)
    
    print("== N2d: coherent grain k=5 (n=N+1) ==")
    def grain(i0, j0, m, t):
        d = 1/(np.cos(t)+np.sin(t)); sqs=[]
        # rigid rotation of m x m grid of squares about grain-box center
        c0 = np.array([i0 + m/2, j0 + m/2])
        R = np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])
        for a in range(m):
            for b in range(m):
                rel = (np.array([a+0.5, b+0.5]) - m/2)*d
                cc = c0 + R @ rel
                sqs.append((cc[0], cc[1], d, t))
        return sqs
    
    for t in (0.05, 0.12, 0.2):
        k=5; m=3
        sqs = grain(0,0,m,t) + units_grid(k, skip=tuple((i,j) for i in range(m) for j in range(m)) + ((4,4),)) + split_cell(4,4,0.5)
        ok = valid_packing(k, sqs)
        print(f"  grain t={t} valid={ok} n={len(sqs)}")
        if ok: report(f"grain m=3 t={t}", k, sqs, M=200)
    
    print("== N2e: two conflicting grains k=6 (n=N+1) ==")
    for t in (0.12, 0.2):
        k=6; m=3
        skip = tuple((i,j) for i in range(m) for j in range(m)) + tuple((i+3,j+3) for i in range(m) for j in range(m)) + ((5,0),)
        sqs = grain(0,0,m,t) + grain(3,3,m,-t) + units_grid(k, skip=skip) + split_cell(5,0,0.5)
        ok = valid_packing(k, sqs)
        print(f"  2grain t={t} valid={ok} n={len(sqs)}")
        if ok: report(f"2grain m=3 t=+-{t}", k, sqs, M=200)
