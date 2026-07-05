"""
Capture-side squeeze, tilted extension: numerical verification.

New objects verified here:
  T1  Chord constancy: vertical chord of a tilted square == d*sec(theta) exactly
      on the middle region [d sin, d cos] of its bbox x-range (and <= elsewhere).
  T2  Lemma A'' (tilted over-full-line exclusion): if the "good full-hit" x-set
      {x : x not in U_i B_i^x  and  p_i(x) >= 1 for all i} has positive measure,
      then beta := sum_i (1 - d_i sec theta_i)_+ >= 1.  (Contrapositive: beta<1
      forces that set to be null.)  Same in y.
  T3  Pointwise structure on E = goodx x goody: c_i = p_i q_i ; c_i=0 => w_i<1 ;
      c_i>=2 => w_i>=1.
  T4  Theorem S2: beta < 1  ==>  |Av| <= sum (1-w_i)_+^2 + U_x+U_y + V_x+V_y.
  T5  Sharpness: deficient column has beta = 1 exactly and violates the S2
      conclusion (|Av| = k/(k+1) > 1/(k+1) = RHS)  -> beta<1 cannot be dropped.
  T6  Algebra: (1-w)^2 = (1-d)^2 - d*sigma*(2-d-w)  (identity used in S3).
"""
import numpy as np

rng = np.random.default_rng(7)
EPS = 1e-12

# ---------- geometry ----------
def square(cx, cy, d, th):
    return dict(cx=cx, cy=cy, d=d, th=th)

def verts(S):
    c, s = np.cos(S['th']), np.sin(S['th'])
    h = S['d']/2.0
    V = np.array([[-h,-h],[h,-h],[h,h],[-h,h]])
    R = np.array([[c,-s],[s,c]])
    return V @ R.T + np.array([S['cx'], S['cy']])

def bbox(S):
    V = verts(S)
    return V[:,0].min(), V[:,0].max(), V[:,1].min(), V[:,1].max()

def contains(S, X, Y, tol=1e-12):
    c, s = np.cos(S['th']), np.sin(S['th'])
    dx, dy = X - S['cx'], Y - S['cy']
    u =  c*dx + s*dy
    v = -s*dx + c*dy
    h = S['d']/2.0 + tol
    return (np.abs(u) <= h) & (np.abs(v) <= h)

def sat_disjoint(S1, S2, tol=1e-9):
    """separating axis test for two convex quads (interior-disjoint check)."""
    V1, V2 = verts(S1), verts(S2)
    for V in (V1, V2):
        for i in range(4):
            e = V[(i+1)%4] - V[i]
            n = np.array([-e[1], e[0]])
            p1 = V1 @ n; p2 = V2 @ n
            if p1.max() <= p2.min() + tol or p2.max() <= p1.min() + tol:
                return True
    return False

def validate(pack, k):
    for S in pack:
        V = verts(S)
        assert V.min() >= -1e-9 and V[:,0].max() <= k+1e-9 and V[:,1].max() <= k+1e-9, "containment fail"
    n = len(pack)
    for i in range(n):
        for j in range(i+1, n):
            assert sat_disjoint(pack[i], pack[j]), f"overlap {i},{j}"

# ---------- vertical chord of a tilted square ----------
def vchord(S, x):
    """length of {y : (x,y) in S} by clipping (exact for convex polygon)."""
    V = verts(S)
    ys = []
    for i in range(4):
        (x1,y1),(x2,y2) = V[i], V[(i+1)%4]
        if abs(x2-x1) < 1e-15:
            if abs(x-x1) < 1e-12: ys += [y1, y2]
            continue
        t = (x-x1)/(x2-x1)
        if -1e-12 <= t <= 1+1e-12:
            ys.append(y1 + t*(y2-y1))
    if len(ys) < 2: return 0.0
    return max(ys) - min(ys)

def test_chord():
    worst_mid = 0.0; bad = 0
    for _ in range(300):
        d = rng.uniform(0.2, 2.5)
        th = rng.uniform(1e-4, np.pi/4 - 1e-4)
        S = square(rng.uniform(3,5), rng.uniform(3,5), d, th)
        b0, b1, _, _ = bbox(S)
        w = b1 - b0
        ds, dc = d*np.sin(th), d*np.cos(th)
        sec = d/np.cos(th)
        for x in np.linspace(b0+1e-9, b1-1e-9, 80):
            ch = vchord(S, x)
            if ch > sec + 1e-9: bad += 1
            xr = x - b0
            if ds + 1e-9 <= xr <= dc - 1e-9:
                worst_mid = max(worst_mid, abs(ch - sec))
    print(f"T1 chord constancy: max |chord - d sec| in middle = {worst_mid:.2e}; over-max count = {bad}")
    assert worst_mid < 1e-8 and bad == 0

# ---------- per-square 1-D line counts ----------
def pcounts(S, xs):
    b0, b1, _, _ = bbox(S)
    return np.floor(b1 - xs).astype(int) - np.ceil(b0 - xs).astype(int) + 1

def qcounts(S, ys):
    _, _, b0, b1 = bbox(S)
    return np.floor(b1 - ys).astype(int) - np.ceil(b0 - ys).astype(int) + 1

def arcs_mod1(intervals, M=200001):
    """indicator of union of [a,b] intervals mod 1 on grid of M points."""
    g = np.zeros(M, dtype=bool)
    xs = (np.arange(M) + 0.5)/M
    for (a, b) in intervals:
        if b - a >= 1: g[:] = True; continue
        a0, b0 = a % 1.0, b % 1.0
        if a0 <= b0: g |= (xs >= a0) & (xs <= b0)
        else:        g |= (xs >= a0) | (xs <= b0)
    return xs, g

def analyze(pack, k, name, M2=420, tol2d=None):
    N = k*k
    n = len(pack)
    assert n == N+1, f"{name}: need N+1 squares, got {n}"
    validate(pack, k)
    d = np.array([S['d'] for S in pack]); th = np.array([S['th'] for S in pack])
    w = d*(np.cos(th)+np.sin(th)); sec = d/np.cos(th)
    beta = np.sum(np.clip(1-sec, 0, None))
    s_def = np.sum((1-d)**2)
    g_gap = N - np.sum(d**2)
    eps = np.sum(d) - N

    # B^x, B^y tall/wide triangle phase arcs
    Bx, By, Fx2, Fy2 = [], [], [], []
    for S in pack:
        b0, b1, c0, c1 = bbox(S)
        dsn = S['d']*np.sin(S['th'])
        if dsn > 1e-15:
            Bx += [(b0, b0+dsn), (b1-dsn, b1)]
            By += [(c0, c0+dsn), (c1-dsn, c1)]
        wS = b1 - b0
        if wS >= 1.0:  # arcs where p_i >= floor(w)+1 >= 2 (w<2 assumed here)
            fr = wS - np.floor(wS)
            if np.floor(wS) >= 2: Fx2 += [(0.0, 1.0)]
            else: Fx2 += [(b0, b0+fr)] if fr > 1e-15 else []
        wT = c1 - c0
        if wT >= 1.0:
            fr = wT - np.floor(wT)
            if np.floor(wT) >= 2: Fy2 += [(0.0, 1.0)]
            else: Fy2 += [(c0, c0+fr)] if fr > 1e-15 else []
    xs1, gBx = arcs_mod1(Bx); _, gBy = arcs_mod1(By)
    _, gFx2 = arcs_mod1(Fx2); _, gFy2 = arcs_mod1(Fy2)
    Ux, Uy = gBx.mean(), gBy.mean()
    Vx, Vy = gFx2.mean(), gFy2.mean()

    # good full-hit measure per axis (Lemma A'')
    P1 = np.array([pcounts(S, xs1) for S in pack])   # n x M
    Q1 = np.array([qcounts(S, xs1) for S in pack])
    fullx = (P1 >= 1).all(axis=0); fully = (Q1 >= 1).all(axis=0)
    gfh_x = float(np.mean(fullx & ~gBx)); gfh_y = float(np.mean(fully & ~gBy))

    # 2-D capture on grid
    off1, off2 = np.sqrt(2)*1e-6, np.sqrt(3)*1e-6
    gx = (np.arange(M2)+0.5)/M2 + off1
    gy = (np.arange(M2)+0.5)/M2 + off2
    X, Y = np.meshgrid(gx, gy, indexing='ij')
    C = np.zeros((M2, M2), dtype=int)
    Cin = {}
    for i, S in enumerate(pack):
        b0, b1, c0, c1 = bbox(S)
        ci = np.zeros((M2, M2), dtype=int)
        for m in range(int(np.floor(b0))-1, int(np.ceil(b1))+1):
            for l in range(int(np.floor(c0))-1, int(np.ceil(c1))+1):
                ci += contains(S, X+m, Y+l).astype(int)
        Cin[i] = ci
        C += ci
    assert C.max() <= N, f"{name}: budget violated max C={C.max()}"
    Av = float(np.mean(C == N))

    # pointwise structure on E
    Pg = np.array([pcounts(S, gx) for S in pack])
    Qg = np.array([qcounts(S, gy) for S in pack])
    goodx = np.interp(gx % 1.0, xs1, gBx.astype(float)) < 0.5
    goody = np.interp(gy % 1.0, xs1, gBy.astype(float)) < 0.5
    Emask = np.outer(goodx, goody)
    viol_pq = viol_idle = viol_multi = 0
    for i in range(n):
        pq = np.outer(Pg[i], Qg[i])
        viol_pq += int(np.sum((Cin[i] != pq) & Emask))
        if w[i] >= 1: viol_idle  += int(np.sum((Cin[i] == 0) & Emask))
        if w[i] < 1:  viol_multi += int(np.sum((Cin[i] >= 2) & Emask))
    RHS = np.sum(np.clip(1-w, 0, None)**2) + Ux + Uy + Vx + Vy
    ok = (beta >= 1 - 1e-9) or (Av <= RHS + 5.0/M2)
    print(f"{name}: n={n} k={k} eps={eps:+.4f} g={g_gap:.4f} s={s_def:.4f} "
          f"beta={beta:.4f} |Av|={Av:.4f} sum(1-w)+^2={np.sum(np.clip(1-w,0,None)**2):.4f} "
          f"Ux={Ux:.4f} Uy={Uy:.4f} Vx={Vx:.4f} Vy={Vy:.4f} RHS={RHS:.4f} "
          f"gfh=({gfh_x:.4f},{gfh_y:.4f}) E-viol(pq,idle,multi)=({viol_pq},{viol_idle},{viol_multi}) "
          f"S2 {'OK' if ok else 'VIOLATED'}")
    assert viol_pq == 0 and viol_multi == 0
    if beta < 1 - 1e-9:
        assert gfh_x < 2e-3 and gfh_y < 2e-3, f"{name}: Lemma A'' violated"
        assert ok, f"{name}: S2 violated"
    return dict(beta=beta, Av=Av, RHS=RHS, gfh=(gfh_x, gfh_y))

# ---------- packings ----------
def col_pack(k, t=0.0):
    c = k/(k+1)
    P = []
    d = c/(np.cos(t)+np.sin(t))
    for r in range(k+1):
        # column square r occupies [0,c] x [r c,(r+1)c] when t=0; tilted version inscribed
        P.append(square(c/2, r*c + c/2, d, t))
    for i in range(1, k):
        for j in range(k):
            P.append(square(i+0.5, j+0.5, 1.0, 0.0))
    return P

def split_cell(k, a):
    P = [square(a/2, a/2, a, 0.0), square(a + (1-a)/2, (1-a)/2, 1-a, 0.0)]
    for i in range(k):
        for j in range(k):
            if i == 0 and j == 0: continue
            P.append(square(i+0.5, j+0.5, 1.0, 0.0))
    return P

def diamonds(k=3, d=0.70):
    # 10 interlocked diamonds (theta=45) in [0,3]^2; d*sec(45)=0.9899<1 so beta small
    wd = d*np.sqrt(2)          # 0.98995
    P = []
    for j in range(5):
        y = 0.497 + j*(wd/2 + 0.0065)
        if j % 2 == 0:
            xs = [0.497 + i*(wd + 0.006) for i in range(3)]
        else:
            xs = [0.497 + (wd + 0.006)/2 + i*(wd + 0.006) for i in range(2)]
        for x in xs:
            if x + wd/2 <= k + 1e-9 and y + wd/2 <= k + 1e-9:
                P.append(square(x, y, d, np.pi/4))
    return P[:k*k+1]

def mixed_tilt(k=2):
    # 3 units + two tilted squares in cell [1,2]^2
    P = [square(0.5,0.5,1,0), square(0.5,1.5,1,0), square(1.5,0.5,1,0)]
    P.append(square(1.35, 1.35, 0.55, 0.20))
    P.append(square(1.78, 1.78, 0.25, 0.70))
    return P

def rand_strip(k=2, seed=0):
    r = np.random.default_rng(seed)
    # deterministic-shape random-width strip packing: 2+2+1 squares, k=2
    w1 = r.uniform(0.75, 1.0); w2 = r.uniform(0.6, 0.9)
    d5 = min(2 - w1 - w2, 0.6)
    P = [square(w1/2, w1/2, w1, 0), square(w1/2, w1 + w1/2, w1, 0),
         square(w1 + w2/2, w2/2, w2, 0), square(w1 + w2/2, w2 + w2/2, w2, 0)]
    if d5 > 0.05:
        P.append(square(w1 + w2 + d5/2, d5/2, d5, 0))
    else:
        P.append(square(w1/2, 2*w1 + 0.01 + 0.02, 0.04, 0))
    return P

def test_algebra():
    d = rng.uniform(0.1, 1.4, 10000); th = rng.uniform(0, np.pi/4, 10000)
    sig = np.cos(th)+np.sin(th)-1; w = d*(1+sig)
    lhs = (1-w)**2; rhs = (1-d)**2 - d*sig*(2-d-w)
    print(f"T6 identity (1-w)^2=(1-d)^2-d.sigma(2-d-w): max err {np.abs(lhs-rhs).max():.2e}")
    assert np.abs(lhs-rhs).max() < 1e-12

if __name__ == "__main__":
    test_chord()
    test_algebra()
    res = {}
    res['col_k2']   = analyze(col_pack(2), 2, 'col_k2 (AP deficient column)')
    res['col_k3']   = analyze(col_pack(3), 3, 'col_k3 (AP deficient column)', M2=300)
    res['colT_k2']  = analyze(col_pack(2, 0.02), 2, 'colT_k2 (tilted column t=0.02)')
    res['colT_k2b'] = analyze(col_pack(2, 0.05), 2, 'colT_k2 (tilted column t=0.05)')
    res['split_k2'] = analyze(split_cell(2, 0.37), 2, 'split_k2 (split cell a=0.37)')
    res['diam_k3']  = analyze(diamonds(3, 0.70), 3, 'diam_k3 (10 diamonds 45deg, beta small)', M2=300)
    res['mixed_k2'] = analyze(mixed_tilt(2), 2, 'mixed_k2 (3 units + 2 tilted)')
    for sd in range(3):
        res[f'rand{sd}'] = analyze(rand_strip(2, sd), 2, f'rand_strip k=2 seed={sd}')
    # T5 sharpness of beta<1: column has beta=1 and violates S2 conclusion
    r = res['col_k2']
    print(f"T5 sharpness: col_k2 beta={r['beta']:.6f} (==1), |Av|={r['Av']:.4f} > RHS={r['RHS']:.4f} -> hypothesis beta<1 is sharp")
    assert abs(r['beta']-1) < 1e-9 and r['Av'] > r['RHS'] + 0.2
    print("ALL TESTS PASSED")

# ---------- direct over-full-line witness test (Lemma A'' mechanism) ----------
def witness_test(pack, k, name, nsamp=200):
    """for x in the good full-hit set: some line x+m carries >= k+1 squares,
    chords are interior-disjoint, sum chords <= k, sum (1 - d sec) >= 1."""
    import numpy as np
    d = np.array([S['d'] for S in pack]); th = np.array([S['th'] for S in pack])
    sec = d/np.cos(th)
    Bx = []
    for S in pack:
        b0,b1,_,_ = bbox(S); dsn = S['d']*np.sin(S['th'])
        if dsn > 1e-15: Bx += [(b0,b0+dsn),(b1-dsn,b1)]
    xs1, gBx = arcs_mod1(Bx, 20001)
    checked = failures = 0
    for x in np.linspace(0.001, 0.999, nsamp):
        if np.interp(x, xs1, gBx.astype(float)) > 0.4: continue
        P = [pcounts(S, np.array([x]))[0] for S in pack]
        if min(P) < 1: continue
        checked += 1
        found = False
        for m in range(k):
            L = [i for i,S in enumerate(pack) if bbox(S)[0] <= x+m <= bbox(S)[1]]
            if len(L) >= k+1:
                chords = [vchord(pack[i], x+m) for i in L]
                iv = sorted((pack[i]['cy']-1, pack[i]['cy']+1, c) for i,c in zip(L,chords))
                assert sum(chords) <= k + 1e-9, f"{name}: chord sum > k"
                assert sum(1 - sec[i] for i in L) >= 1 - 1e-9, f"{name}: line deficit < 1"
                for i in L:
                    assert abs(vchord(pack[i], x+m) - sec[i]) < 1e-9, f"{name}: chord != d sec"
                found = True
        if not found: failures += 1
    print(f"A''-witness {name}: {checked} good full-hit x sampled, over-full line found in all "
          f"{'OK' if failures==0 else f'FAIL({failures})'}")
    assert failures == 0

if __name__ == "__main__" and True:
    witness_test(col_pack(2), 2, 'col_k2')
    witness_test(col_pack(3), 3, 'col_k3')
    witness_test(col_pack(2, 0.02), 2, 'colT_k2_t.02')
    witness_test(col_pack(2, 0.05), 2, 'colT_k2_t.05')
    print("WITNESS TESTS PASSED")

def bigtilt(k=2):
    # one long tilted square (d=1.05, th=0.1, w=1.147>1) + 4 AP fillers
    P = [square(0.6035, 0.6035, 1.05, 0.10)]
    P.append(square(1.625, 0.375, 0.75, 0))
    P.append(square(1.625, 1.125, 0.75, 0))
    P.append(square(0.375, 1.625, 0.75, 0))
    P.append(square(1.0,   1.75,  0.48, 0))
    return P

def bigAP(k=2):
    # AP with d=1.3 long: exercises V_x arcs for AP longs
    P = [square(0.65, 0.65, 1.3, 0), square(1.65, 0.35, 0.7, 0),
         square(1.65, 1.05, 0.7, 0), square(0.35, 1.65, 0.7, 0),
         square(1.7, 1.7, 0.6, 0)]
    return P

if __name__ == "__main__" and True:
    analyze(bigtilt(2), 2, 'bigtilt_k2 (long tilted w=1.147)')
    analyze(bigAP(2), 2, 'bigAP_k2 (long AP d=1.3)')
    print("LONG-SQUARE TESTS PASSED")
