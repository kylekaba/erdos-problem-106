import numpy as np
rng = np.random.default_rng(12345)

def lattice_points_in_box(B, p, k):
    """count points of B@Z^2 + p in [0,k)^2. B columns = basis."""
    # enumerate integer range generously
    Binv = np.linalg.inv(B)
    # corners of [0,k)^2 shifted
    corners = np.array([[0,0],[k,0],[0,k],[k,k]]) - p
    ij = corners @ Binv.T
    i0, i1 = int(np.floor(ij[:,0].min()))-2, int(np.ceil(ij[:,0].max()))+2
    j0, j1 = int(np.floor(ij[:,1].min()))-2, int(np.ceil(ij[:,1].max()))+2
    I, J = np.meshgrid(np.arange(i0,i1+1), np.arange(j0,j1+1), indexing='ij')
    pts = np.stack([I.ravel(), J.ravel()],1) @ B.T + p
    inside = (pts[:,0]>=0)&(pts[:,0]<k)&(pts[:,1]>=0)&(pts[:,1]<k)
    return int(inside.sum())

def R(t):
    return np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])

# ---- Claim 1(a): (3,4,5) rotated unit lattice
th = np.arctan2(4,3)
B = R(th)  # columns R e1, R e2
for k in [5,10,7]:
    counts = set()
    for _ in range(200):
        p = rng.uniform(-3,3,2)
        counts.add(lattice_points_in_box(B,p,k))
    print(f"Claim1a (3,4,5) k={k}: counts={sorted(counts)} (expect {{{k*k}}} iff 5|k)")

# ---- Claim 1(b): D lattice covol 1/2
BD = np.array([[0.5,0.5],[0.5,-0.5]]).T
for k in [3,4,7]:
    counts = set()
    for _ in range(200):
        p = rng.uniform(-3,3,2)
        counts.add(lattice_points_in_box(BD,p,k))
    print(f"Claim1b D k={k}: counts={sorted(counts)} (expect {{{2*k*k}}})")

# ---- Claim 1(d): R_45 Z^2 fluctuates
B45 = R(np.pi/4)
for k in [3,5,10]:
    counts = set()
    for _ in range(400):
        p = rng.uniform(-3,3,2)
        counts.add(lattice_points_in_box(B45,p,k))
    print(f"Claim1d R45 k={k}: counts={sorted(counts)} (expect fluctuation around {k*k})")

# ---- Claim 2 product structure: theta-frame squares vs R_theta Z^2 + p
th = np.arctan2(4,3)  # arctan(4/3); also test arctan(3/4)
def check_product(th, ntrials=3000):
    bad = 0
    for _ in range(ntrials):
        d = rng.uniform(0.1, 3.5)
        alpha, beta = rng.uniform(-5,5,2)
        x, y = rng.uniform(0,1,2)   # frame shift
        # square in frame coords: [alpha,alpha+d) x [beta,beta+d); lattice Z^2+(x,y) in frame
        def cnt1(a, w, s):
            lo = np.ceil(a - s); hi = np.floor(a + w - s)
            # m with a <= m+s < a+w  => m in [a-s, a+w-s)
            m0 = int(np.ceil(a - s)); m1 = int(np.ceil(a + w - s)) - 1
            return max(0, m1 - m0 + 1)
        p_ = cnt1(alpha, d, x); q_ = cnt1(beta, d, y)
        # direct count
        M = np.arange(int(np.floor(alpha-2)), int(np.ceil(alpha+d+2)))
        Nn = np.arange(int(np.floor(beta-2)), int(np.ceil(beta+d+2)))
        c = 0
        for m in M:
            if alpha <= m + x < alpha + d:
                for n in Nn:
                    if beta <= n + y < beta + d:
                        c += 1
        ok = (c == p_ * q_) and p_ in (int(np.floor(d)), int(np.ceil(d))) and q_ in (int(np.floor(d)), int(np.ceil(d)))
        if not ok: bad += 1
    print(f"Claim2 product structure: {ntrials-bad}/{ntrials} ok")
check_product(th)

# ---- Claim 2 end-to-end sanity: packing of theta-tilted squares in [0,5]^2, chain inequality
k = 5; N = 25
th = np.arctan2(3,4)  # arctan(3/4), c=5 | k=5
Rt = R(th); Rmt = R(-th)
# build tilted squares: grid in the tilted frame, keep those inside [0,k]^2
side = 0.8
squares = []  # (alpha,beta,d) frame coords of lower-left, half-open
for i in range(-10, 20):
    for j in range(-10, 20):
        a, b = i*side*1.05, j*side*1.05
        # corners in original coords
        cs = np.array([[a,b],[a+side,b],[a,b+side],[a+side,b+side]]) @ Rt.T
        if (cs>=0).all() and (cs<=k).all():
            squares.append((a,b,side))
print(f"Claim2 sanity packing: {len(squares)} tilted squares, sum d = {len(squares)*side:.2f}")
viol = 0
for _ in range(500):
    p = rng.uniform(-2,2,2)
    x, y = Rmt @ p  # frame shift components
    xf, yf = x % 1.0, y % 1.0
    tot_pq = 0
    for (a,b,d) in squares:
        m0 = int(np.ceil(a - xf)); m1 = int(np.ceil(a + d - xf)) - 1
        p_ = max(0, m1-m0+1)
        n0 = int(np.ceil(b - yf)); n1 = int(np.ceil(b + d - yf)) - 1
        q_ = max(0, n1-n0+1)
        tot_pq += p_*q_
    # container count, closed [0,k]^2
    Binv = np.linalg.inv(Rt)
    corners = np.array([[0,0],[k,0],[0,k],[k,k]]) - p
    ij = corners @ Binv.T
    i0,i1 = int(np.floor(ij[:,0].min()))-2, int(np.ceil(ij[:,0].max()))+2
    j0,j1 = int(np.floor(ij[:,1].min()))-2, int(np.ceil(ij[:,1].max()))+2
    I,J = np.meshgrid(np.arange(i0,i1+1), np.arange(j0,j1+1), indexing='ij')
    pts = np.stack([I.ravel(),J.ravel()],1) @ Rt.T + p
    closed = int(((pts[:,0]>=-1e-12)&(pts[:,0]<=k+1e-12)&(pts[:,1]>=-1e-12)&(pts[:,1]<=k+1e-12)).sum())
    halfopen = int(((pts[:,0]>=0)&(pts[:,0]<k)&(pts[:,1]>=0)&(pts[:,1]<k)).sum())
    if tot_pq > closed: viol += 1
    assert halfopen == N, halfopen
print(f"Claim2 sanity: sum p*q <= |closed T cap Lambda| violated in {viol}/500 shifts; half-open budget always {N}")

# ---- Claim 5: E[p]=d for frame-aligned square; E|T cap Lambda| = N for irrational angle
th2 = 1.0  # irrational-ish angle, common orientation
d = 1.3; a, b = 0.37, -0.81
M = 200000
xs = rng.uniform(0,1,M)
pvals = np.ceil(a + d - xs) - np.ceil(a - xs)
print(f"Claim5 E[p] = {pvals.mean():.4f} vs d = {d}")
k = 4; N = 16
tot = 0; trials = 4000
B2 = R(th2)
for _ in range(trials):
    p = rng.uniform(-2,2,2)
    tot += lattice_points_in_box(B2,p,k)
print(f"Claim5 E|T cap R_1.0 Z^2 + p| = {tot/trials:.3f} vs N = {N}")

# pointwise F_1 <= 0 check for a common-orientation (45 deg) packing in [0,4]^2
k = 4; N = 16
th3 = np.pi/4
Rt = R(th3); Rmt = R(-th3)
side = 0.9
squares = []
for i in range(-10,20):
    for j in range(-10,20):
        a,b = i*side*1.02, j*side*1.02
        cs = np.array([[a,b],[a+side,b],[a,b+side],[a+side,b+side]]) @ Rt.T
        if (cs>=0).all() and (cs<=k).all():
            squares.append((a,b,side))
worst = -99
for _ in range(2000):
    p = rng.uniform(-2,2,2)
    x,y = Rmt @ p; xf,yf = x%1, y%1
    tot_lhs = 0
    for (a,b,d) in squares:
        p_ = int(np.ceil(a+d-xf) - np.ceil(a-xf)); q_ = int(np.ceil(b+d-yf) - np.ceil(b-yf))
        tot_lhs += p_ + q_ - 1
    Binv = np.linalg.inv(Rt)
    corners = np.array([[0,0],[k,0],[0,k],[k,k]]) - p
    ij = corners @ Binv.T
    i0,i1 = int(np.floor(ij[:,0].min()))-2, int(np.ceil(ij[:,0].max()))+2
    j0,j1 = int(np.floor(ij[:,1].min()))-2, int(np.ceil(ij[:,1].max()))+2
    I,J = np.meshgrid(np.arange(i0,i1+1), np.arange(j0,j1+1), indexing='ij')
    pts = np.stack([I.ravel(),J.ravel()],1) @ Rt.T + p
    closed = int(((pts[:,0]>=-1e-12)&(pts[:,0]<=k+1e-12)&(pts[:,1]>=-1e-12)&(pts[:,1]<=k+1e-12)).sum())
    worst = max(worst, tot_lhs - closed)
print(f"Claim5 J=1 pointwise: max over shifts of [sum(p+q-1) - |T closed cap Lambda|] = {worst} ({len(squares)} squares at 45deg, sum d={len(squares)*side:.2f}) — expect <= 0")

# ---- Route E Claim 6: diamond chain
def sat_disjoint(c1,s1,a1,c2,s2,a2):
    """separating axis test for two squares (centers, sides, angles): True if interiors disjoint"""
    def verts(c,s,a):
        h = s/2
        loc = np.array([[h,h],[-h,h],[-h,-h],[h,-h]])
        return loc @ R(a).T + c
    V1, V2 = verts(c1,s1,a1), verts(c2,s2,a2)
    for ang in [a1, a1+np.pi/2, a2, a2+np.pi/2]:
        u = np.array([np.cos(ang), np.sin(ang)])
        p1, p2 = V1@u, V2@u
        if p1.max() <= p2.min() + 1e-12 or p2.max() <= p1.min() + 1e-12:
            return True
    return False

for s in [0.2, 0.1, 0.05]:
    m = int(np.floor(np.sqrt(2)/s)) - 1
    centers = [np.array([j*s/np.sqrt(2)]*2) for j in range(1,m+1)]
    ang = np.pi/4
    ok_contain = True
    for c in centers:
        h = s/np.sqrt(2)
        vs = np.array([[h,0],[-h,0],[0,h],[0,-h]]) + c
        if not ((vs>=-1e-12).all() and (vs<=1+1e-12).all()): ok_contain = False
    ok_disj = all(sat_disjoint(centers[i],s,ang,centers[j],s,ang) for i in range(m) for j in range(i+1,m))
    print(f"Claim6E s={s}: m={m}, total={m*s:.3f}, contained={ok_contain}, pairwise disjoint={ok_disj}")

# check hat(1_T) nonzero at xi = R45(1,1) = (0, sqrt2): 1-D factor for coordinate 0 is k (nonzero), for sqrt2: |int_0^k e^{-2pi i sqrt2 t} dt|
for k in [3,5,10]:
    import cmath
    val = (cmath.exp(-2j*np.pi*np.sqrt(2)*k)-1)/(-2j*np.pi*np.sqrt(2))
    print(f"Claim1d Fourier: |hat factor| at xi2=sqrt2, k={k}: {abs(val):.4f} (nonzero)")
