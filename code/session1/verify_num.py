import numpy as np

def setup(d, th):
    c, s = np.cos(th), np.sin(th)
    u1 = c + s
    w = d*u1
    return c, s, u1, w

def in_S(P, d, th):
    # S = rotate [0,d]^2 by th, translate by (d sin th, 0). Inverse map.
    c, s = np.cos(th), np.sin(th)
    x = P[...,0] - d*s
    y = P[...,1]
    qx =  c*x + s*y
    qy = -s*x + c*y
    return (qx > 0) & (qx < d) & (qy > 0) & (qy < d)

def counts(d, th, x, y):
    """Exact p,q,c,L for lattice Z^2+(x,y) in box frame [0,w]^2."""
    c_, s_, u1, w = setup(d, th)
    ms = np.arange(-2, int(w)+3)
    xs = ms + x; ys = ms + y
    vx = xs[(xs > 0) & (xs < w)]
    vy = ys[(ys > 0) & (ys < w)]
    p, q = len(vx), len(vy)
    if p == 0 or q == 0:
        return p, q, 0, 0
    X, Y = np.meshgrid(vx, vy, indexing='ij')
    pts = np.stack([X.ravel(), Y.ravel()], axis=-1)
    cnt = int(in_S(pts, d, th).sum())
    L = p*q - cnt
    return p, q, cnt, L

rng = np.random.default_rng(7)

print("=== Claims 1,2 pointwise: c=pq-L, |p-q|<=1, p,q in {fl(w),fl(w)+1}, B>=0 ===")
for (d, th) in [(0.7,0.3),(0.9,0.2),(1.0,0.05),(1.1,0.2),(1.15,0.3),(1.15,0.2),
                (np.sqrt(2)-1e-3, np.pi/4),(0.4,0.1),(2.7,0.6),(5.3,0.33),(1.4,0.02)]:
    c_,s_,u1,w = setup(d,th)
    bad = 0
    for _ in range(20000):
        x, y = rng.random(), rng.random()
        p,q,cnt,L = counts(d,th,x,y)
        if abs(p-q) > 1: bad += 1
        if p not in (int(w), int(w)+1) or q not in (int(w), int(w)+1): bad += 1
        if (p-1)*(q-1) < 0: bad += 1
        # c = pq - L is enforced by construction; independently check c <= pq and L>=0
        if cnt > p*q or L < 0: bad += 1
    print(f"  d={d:.4f} th={th:.3f} w={w:.4f}: violations={bad}")

print("\n=== Claim 5/7/8: E[L]=d^2 sin2th, E[min(L,B)]=W^2, margin closed forms ===")
cases = [(0.7,0.3),(0.9,0.2),(1.0,0.05),(1.0,0.3),(1.1,0.2),(1.15,0.3),(1.15,0.2),(np.sqrt(2)-1e-3,np.pi/4)]
n = 1200  # midpoint grid n x n
g = (np.arange(n)+0.5)/n
for (d, th) in cases:
    c_,s_,u1,w = setup(d,th)
    W = max(w-1.0, 0.0)
    EL = 0.0; Emin = 0.0; Edef = 0.0
    for x in g:
        for y in g:
            p,q,cnt,L = counts(d,th,x,y)
            B = (p-1)*(q-1)
            EL += L; Emin += min(L,B); Edef += max(L-B,0)
    EL/=n*n; Emin/=n*n; Edef/=n*n
    m_meas = 2*w - EL + Emin - 2*d
    sig = u1-1
    m_pred = d*sig*(2-d-w) if w <= 1 else (1-d)**2
    print(f"  d={d:.4f} th={th:.3f} w={w:.4f} d<=u1={d<=u1+1e-12} dcos={d*c_:.3f}:"
          f" EL={EL:.5f} vs {d*d*np.sin(2*th):.5f} | Emin={Emin:.5f} vs W^2={W*W:.5f}"
          f" | m={m_meas:.5f} vs pred {m_pred:.5f}")
