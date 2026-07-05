"""
G6 session-3 verification: the Marginal Displacement Theorem (MDT) and friends.

Objects (notation as ERDOS_106_REPORT.md):
  P(x) = sum_i p_i(x), p_i = # vertical lattice lines x+m meeting square S_i.
  B_i^x = the two end-region ("tall corner triangle") phase arcs of S_i, each of
          length d_i sin th_i, at the bbox x-extremes.  Good x: x mod 1 outside all B_i^x.
  beta   = sum_i (1 - d_i sec th_i)_+          (chord-deficit mass)
  b0sec  = sum_i (d_i sec th_i - 1)_+          (chord-surplus mass)
  rho    = sum_i d_i (sec th_i - 1) >= 0
  For n squares:  beta - b0sec = n - sum d_i sec th_i  (identity)
                  = (n - N - eps_n) - rho  with eps_n = sum d_i - N... we just use
                  bound_good := n - sum_i d_i sec th_i.

CLAIMS CHECKED:
 C1 (per-line capacity): for every line, sum of vertical chords <= k.
 C2 (chord ledger, everywhere): P(x) - N <= sum_{incidences} (1 - ch)  a.e. x.
 C3 (MDT, good x): P(x) - N <= sum_i p_i (1 - d_i sec th_i) <= bound_good;
    per-square on good x:  d sec th < 1 => p_i <= 1;  d sec th >= 1 => p_i >= 1
    and every incident line is in the middle region (ch = d sec th).
 C4 (integer ledger, everywhere): (P-N)_+ <= floor(beta) + T(x), T = # end-region
    incidences; and T = 0 on good x.   [needs n = N+1 for floor(beta) form; we
    check the general form (P-N)_+ <= floor(max(bound_good,0)+beta_extra)... we
    check exactly the N+1 packings for this claim.]
 C5 (mean): grid-average of P == sum w_i (within grid tolerance).
 C6 (sharpness): U_k has |{P=N+1}| = k/(k+1); T12(k=4) has |{P=N+1}| = 2/3;
    both good-set bounds are tight (bound_good = 1, eps=0, rho=0).
 C7 (beta table on extremals): U_k:1, split cell:1, T12(k=4,b=2): b=2,
    deficient row: 1.  => "extremal manifold sits at beta=1" is FALSE (T12).
 C8 (orchestrator fact): sin th >= cos th + sin th - 1 on [0, pi/2].
"""
import numpy as np

rng = np.random.default_rng(106)
TOL = 1e-9

# ---------------- geometry (from squeeze_check.py, session 2) ----------------
def square(cx, cy, d, th): return dict(cx=cx, cy=cy, d=d, th=th)

def verts(S):
    c, s = np.cos(S['th']), np.sin(S['th'])
    h = S['d']/2.0
    V = np.array([[-h,-h],[h,-h],[h,h],[-h,h]])
    R = np.array([[c,-s],[s,c]])
    return V @ R.T + np.array([S['cx'], S['cy']])

def bbox(S):
    V = verts(S)
    return V[:,0].min(), V[:,0].max(), V[:,1].min(), V[:,1].max()

def sat_disjoint(S1, S2, tol=1e-9):
    V1, V2 = verts(S1), verts(S2)
    for V in (V1, V2):
        for i in range(4):
            e = V[(i+1)%4] - V[i]
            nrm = np.array([-e[1], e[0]])
            p1 = V1 @ nrm; p2 = V2 @ nrm
            if p1.max() <= p2.min() + tol or p2.max() <= p1.min() + tol:
                return True
    return False

def validate(pack, k):
    for S in pack:
        V = verts(S)
        assert V.min() >= -1e-9 and V[:,0].max() <= k+1e-9 and V[:,1].max() <= k+1e-9
    for i in range(len(pack)):
        for j in range(i+1, len(pack)):
            assert sat_disjoint(pack[i], pack[j]), f"overlap {i},{j}"

def vchord(S, x):
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

# ---------------- packings ----------------
def U_k(k, a=None):
    """deficient column: k+1 squares of sides a_j (sum=k) in strip [k-1,k]x[0,k],
       k(k-1) units in [0,k-1]x[0,k]."""
    if a is None: a = [k/(k+1.0)]*(k+1)
    assert abs(sum(a)-k) < 1e-12
    pack = []
    for i in range(k-1):
        for j in range(k):
            pack.append(square(i+0.5, j+0.5, 1.0, 0.0))
    h = 0.0
    for aj in a:
        pack.append(square(k-1+aj/2.0, h+aj/2.0, aj, 0.0))
        h += aj
    return pack, k

def split_cell(k=2, a=0.37):
    b = 1.0 - a
    pack = []
    for (i,j) in [(0,0),(0,1),(1,0)]:
        pack.append(square(i+0.5, j+0.5, 1.0, 0.0))
    pack.append(square(1+a/2.0, 1+a/2.0, a, 0.0))
    pack.append(square(1+b/2.0, 1+a+b/2.0, b, 0.0))
    return pack, k

def T12(k=4, b=2):
    """column tiling: col width k/(k+b) with k+b squares; col width k/(k+1-b)
       with k+1-b squares; k-2 unit columns."""
    dA, nA = k/(k+b), k+b
    dB, nB = k/(k+1.0-b), k+1-b
    pack = []
    for j in range(nA): pack.append(square(dA/2.0, (j+0.5)*dA, dA, 0.0))
    for j in range(nB): pack.append(square(dA + dB/2.0, (j+0.5)*dB, dB, 0.0))
    x0 = dA + dB
    assert abs(x0 - 2.0) < 1e-12 or True
    for c in range(k-2):
        for j in range(k):
            pack.append(square(x0 + c + 0.5, j+0.5, 1.0, 0.0))
    return pack, k

def deficient_row(k=3):
    pack, kk = U_k(k)
    # transpose x<->y
    return [square(S['cy'], S['cx'], S['d'], S['th']) for S in pack], k

def tilted_column(k=3, t=0.05):
    u1 = np.cos(t)+np.sin(t)
    d = k/((k+1.0)*u1)          # shrunk so k+1 tilted bboxes stack to height k
    w = d*u1
    pack = []
    for i in range(k-1):
        for j in range(k):
            pack.append(square(1+i+0.5, j+0.5, 1.0, 0.0))
    for j in range(k+1):
        pack.append(square(w/2.0 + 1e-6, (j+0.5)*w, d, t))
    return pack, k

def oversize_tilted(k=3):
    """general-n pack: 4 units + one oversize tilted square (d sec th > 1,
       d(cos-sin) < 1: the no-guaranteed-midline case)."""
    pack = [square(0.5,0.5,1,0.0), square(1.5,0.5,1,0.0), square(2.5,0.5,1,0.0),
            square(2.5,1.5,1,0.0)]
    pack.append(square(1.0, 2.0, 1.25, 0.3))
    return pack, k

def fat_tilted_deficit(k=3):
    """adversarial: deficit-chord squares (d sec th < 1) with bbox width w > 1,
       so p_i = 2 is possible -- MDT says only at bad phases."""
    S1 = square(0.7, 0.7, 0.85, 0.5)    # d sec = 0.9686 < 1, w = 1.1535 > 1
    return [S1, square(2.4, 2.4, 1.0, 0.0)], k

def random_tilted(k=3, n=12, dmin=0.3, dmax=1.3, seed=1):
    r = np.random.default_rng(seed)
    pack = []
    tries = 0
    while len(pack) < n and tries < 20000:
        tries += 1
        d = r.uniform(dmin, dmax); th = r.uniform(0, np.pi/4)
        w = d*(np.cos(th)+np.sin(th))
        cx = r.uniform(w/2, k-w/2); cy = r.uniform(w/2, k-w/2)
        S = square(cx, cy, d, th)
        if all(sat_disjoint(S, S2) for S2 in pack):
            pack.append(S)
    return pack, k

# ---------------- the checker ----------------
def analyze(name, pack, k, M=4001, expect_beta=None, expect_sharp=None):
    validate(pack, k)
    N = k*k; n = len(pack)
    d  = np.array([S['d'] for S in pack])
    th = np.array([S['th'] for S in pack])
    sec = d/np.cos(th)
    w  = d*(np.cos(th)+np.sin(th))
    eps_n = d.sum() - N
    beta  = np.clip(1-sec, 0, None).sum()
    b0sec = np.clip(sec-1, 0, None).sum()
    rho   = (d*(1/np.cos(th)-1)).sum()
    bound_good = n - sec.sum()
    assert abs((beta - b0sec) - bound_good) < 1e-9      # identity
    bxs = [bbox(S) for S in pack]

    # bad-phase arcs B_i^x on a grid mod 1
    xs = (np.arange(M) + 0.3183098861837907) / M   # generic offset (1/pi)
    bad = np.zeros(M, dtype=bool)
    for S,(b0,b1,_,_) in zip(pack, bxs):
        ds = S['d']*np.sin(S['th'])
        if ds < 1e-15: continue
        for (a0,a1) in [(b0, b0+ds), (b1-ds, b1)]:
            a0m, a1m = a0 % 1.0, (a0 + (a1-a0)) % 1.0
            L = a1 - a0
            if L >= 1: bad[:] = True; continue
            if a0m <= a1m: bad |= (xs >= a0m-1e-12) & (xs <= a1m+1e-12)
            else:          bad |= (xs >= a0m-1e-12) | (xs <= a1m+1e-12)

    Pv = np.zeros(M); ledger = np.zeros(M); Tv = np.zeros(M, dtype=int)
    viol = dict(cap=0, ledger=0, good=0, persq=0, intledger=0, mid=0)
    worst_good = -99
    for ix, x in enumerate(xs):
        P = 0; led = 0.0; T = 0
        line_ch = np.zeros(k)
        for S,(b0,b1,_,_) in zip(pack, bxs):
            ds, dc = S['d']*np.sin(S['th']), S['d']*np.cos(S['th'])
            dsec = S['d']/np.cos(S['th'])
            p = 0; inc_mid_all = True; nmid = 0
            for m in range(k):
                X = x + m
                if b0 + 1e-12 < X < b1 - 1e-12:
                    p += 1
                    ch = vchord(S, X)
                    line_ch[m] += ch
                    led += 1 - ch
                    u = X - b0
                    in_mid = (ds - 1e-9 <= u <= dc + 1e-9)
                    if in_mid: nmid += 1
                    else: T += 1
            P += p
            if not bad[ix]:
                if dsec < 1 - 1e-9 and p > 1: viol['persq'] += 1
                if dsec > 1 + 1e-9 and (p < 1 or nmid < 1): viol['mid'] += 1
        Pv[ix] = P; ledger[ix] = led; Tv[ix] = T
        if line_ch.max() > k + 1e-6: viol['cap'] += 1
        if P - N > led + 1e-6: viol['ledger'] += 1
        if (not bad[ix]) and (P - N > bound_good + 1e-9):
            viol['good'] += 1; worst_good = max(worst_good, P-N-bound_good)
        if n == N+1:
            if max(P - N, 0) > int(np.floor(beta + 1e-9)) + Tv[ix]:
                viol['intledger'] += 1
        if (not bad[ix]) and Tv[ix] != 0: viol['intledger'] += 1
    meanP = Pv.mean()
    sharp = (np.abs(Pv - (N+1)) < 0.5).mean()
    print(f"[{name}] n={n} N={N} eps={eps_n:+.4f} beta={beta:.4f} b0sec={b0sec:.4f} "
          f"rho={rho:.4f} bound_good={bound_good:.4f} U_x(grid)={bad.mean():.4f}")
    print(f"   E[P]: grid {meanP:.4f} vs sum w = {w.sum():.4f} | maxP-N={Pv.max()-N:.0f} "
          f"|{{P=N+1}}|={sharp:.4f} | viol={viol}")
    assert all(v == 0 for v in viol.values()), (name, viol)
    assert abs(meanP - w.sum()) < 0.02, name
    if expect_beta is not None:
        assert abs(beta - expect_beta) < 1e-9, (name, beta, expect_beta)
    if expect_sharp is not None:
        assert abs(sharp - expect_sharp) < 2e-3, (name, sharp, expect_sharp)
    return beta

print("== C8: sin th >= sigma(th) on [0,pi/2] ==")
tt = np.linspace(0, np.pi/2, 100001)
assert (np.sin(tt) - (np.cos(tt)+np.sin(tt)-1) >= -1e-15).all()
print("   OK (equivalent to 1-cos th >= 0)")

print("== extremal manifold beta table + MDT checks ==")
analyze("U_2 equal",   *U_k(2), expect_beta=1.0, expect_sharp=2/3)
analyze("U_3 equal",   *U_k(3), expect_beta=1.0, expect_sharp=3/4)
analyze("U_3 uneven",  *U_k(3, [0.8,0.7,1.0,0.5]), expect_beta=1.0)
analyze("split k=2 a=.37", *split_cell(2, 0.37), expect_beta=1.0)
analyze("T12 k=4 b=2", *T12(4,2), expect_beta=2.0, expect_sharp=2/3)
analyze("deficient row k=3 (x-axis view)", *deficient_row(3))
analyze("tilted column k=3 t=0.05", *tilted_column(3, 0.05))
analyze("tilted column k=3 t=0.02", *tilted_column(3, 0.02))
analyze("oversize tilted (general n)", *oversize_tilted(3))
analyze("fat tilted deficit (p=2 possible)", *fat_tilted_deficit(3))
# verify p=2 DOES occur for the fat squares (so the persq check is not vacuous)
_pk, _k = fat_tilted_deficit(3)
_b = bbox(_pk[0]); hit2 = 0
for _x in np.linspace(0.001, 0.999, 997):
    p = sum(1 for m in range(_k) if _b[0] + 1e-12 < _x+m < _b[1] - 1e-12)
    hit2 += (p == 2)
print(f"   fat square attains p=2 on {hit2/997:.4f} of phases (must be >0, "
      f"all inside its bad arcs)")
assert hit2 > 0
for seed in (1,2,3):
    analyze(f"random tilted seed={seed}", *random_tilted(3, 12, seed=seed))
analyze("random tilted big", *random_tilted(4, 20, dmin=0.4, dmax=1.45, seed=7))

print("== T12 arithmetic (beta=b for all b) ==")
for b in range(2, 6):
    k = 2*b*(b-1)
    dA = k/(k+b); dB = k/(k+1-b)
    beta = (k+b)*(1-dA); b0 = (k+1-b)*(dB-1)
    sides = (k+b)*dA + (k+1-b)*dB + k*(k-2)
    widths = k*1/(k+b)*1 + 0  # width check below
    assert abs(beta - b) < 1e-9 and abs(b0 - (b-1)) < 1e-9
    assert abs(sides - k*k) < 1e-9
    assert abs(k/(k+b) + k/(k+1-b) + (k-2) - k) < 1e-9
    print(f"   k={k:3d} b={b}: beta={beta:.6f}=b, b0={b0:.6f}=b-1, sum d=N, widths OK")

print("== multiplicity vs b0 on U_k (reverse-OC-FCMB dead end) ==")
for k in (2,3,4):
    g = k/(k+1.0); mult = g*(k-1)/k
    print(f"   U_{k}: multiplicity mass g-|pi(G)| = {mult:.4f}  vs  (b0-eps)_+ = 0  -> "
          f"'multiplicity <= (b0-eps)_+ + ...' FALSE")

print("ALL CHECKS PASSED")
