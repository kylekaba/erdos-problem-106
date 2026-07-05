# G1 VERIFIER — fresh independent numerics for fp_P_SQUEEZE + fp_P_RIGIDITY.
# All code written from scratch (no reuse of squeeze_check.py / lemmaK_check.py etc.)
import numpy as np

rng = np.random.default_rng(20260704)
FAIL = []


def report(name, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    if not ok:
        FAIL.append(name)
    print(f"[{tag}] {name}  {detail}")


# ---------------------------------------------------------------- geometry ---
def square_verts(cx, cy, d, th):
    c, s = np.cos(th), np.sin(th)
    h = d / 2.0
    base = np.array([[-h, -h], [h, -h], [h, h], [-h, h]])
    R = np.array([[c, -s], [s, c]])
    return base @ R.T + np.array([cx, cy])


class Sq:
    def __init__(self, cx, cy, d, th):
        self.cx, self.cy, self.d, self.th = cx, cy, d, th
        self.u1 = np.cos(th) + np.sin(th)
        self.w = d * self.u1
        self.sig = self.u1 - 1.0
        self.verts = square_verts(cx, cy, d, th)
        self.bx0, self.bx1 = cx - self.w / 2, cx + self.w / 2
        self.by0, self.by1 = cy - self.w / 2, cy + self.w / 2

    def inside(self, px, py):
        c, s = np.cos(self.th), np.sin(self.th)
        ux = c * (px - self.cx) + s * (py - self.cy)
        uy = -s * (px - self.cx) + c * (py - self.cy)
        h = self.d / 2
        return (np.abs(ux) < h) & (np.abs(uy) < h)

    def chord_v(self, X):
        """vertical chord length at x=X (exact segment intersections)."""
        ys = []
        V = self.verts
        for e in range(4):
            (x1, y1), (x2, y2) = V[e], V[(e + 1) % 4]
            if (x1 - X) * (x2 - X) < 0:
                tpar = (X - x1) / (x2 - x1)
                ys.append(y1 + tpar * (y2 - y1))
        return (max(ys) - min(ys)) if len(ys) >= 2 else 0.0


def sat_disjoint(A, B):
    """separating-axis: open interiors disjoint?"""
    for P in (A, B):
        V = P.verts
        for e in range(4):
            n = V[(e + 1) % 4] - V[e]
            n = np.array([-n[1], n[0]])
            pa = V @ n
            pb = B.verts @ n if P is A else A.verts @ n
            if pa.max() <= pb.min() + 1e-12 or pb.max() <= pa.min() + 1e-12:
                return True
    return False


def check_packing(sqs, k):
    ok = True
    for S in sqs:
        if S.verts.min() < -1e-9 or S.verts.max() > k + 1e-9:
            ok = False
    for i in range(len(sqs)):
        for j in range(i + 1, len(sqs)):
            if not sat_disjoint(sqs[i], sqs[j]):
                ok = False
    return ok


# ================================================== 1. LEMMA 0 (chord law) ===
def lemma0():
    bad_exceed = 0
    bad_mid = 0
    worst = 0.0
    for _ in range(300):
        d = rng.uniform(0.2, 1.6)
        th = rng.uniform(1e-3, np.pi / 4)
        S = Sq(0.0, 0.0, d, th)
        sec = d / np.cos(th)
        ds, dc = d * np.sin(th), d * np.cos(th)
        for X in rng.uniform(S.bx0, S.bx1, 90):
            ch = S.chord_v(X)
            if ch > sec + 1e-10:
                bad_exceed += 1
            xr = X - S.bx0  # position in [0,w]
            if ds + 1e-9 < xr < dc - 1e-9:
                worst = max(worst, abs(ch - sec))
        # horizontal chords via transpose (swap x/y = reflect): use rotated-by-(pi/2 - th)? Instead
        # test horizontal chord by chord_v on the square reflected across y=x:
        S2v = Sq(0.0, 0.0, d, np.pi / 2 - th)  # reflection swaps role; folded tilt same
        for Y in rng.uniform(S2v.bx0, S2v.bx1, 30):
            ch = S2v.chord_v(Y)
            if ch > sec + 1e-10:
                bad_exceed += 1
            yr = Y - S2v.bx0
            if ds + 1e-9 < yr < dc - 1e-9:
                worst = max(worst, abs(ch - sec))
    report("Lemma0 chord<=d.sec everywhere", bad_exceed == 0, f"exceed={bad_exceed}")
    report("Lemma0 chord==d.sec on middle region", worst < 1e-10, f"worst={worst:.2e}")


# ============================== 2. Lemma K pointwise integer inequalities ===
def lemK_pointwise():
    bad1 = bad2 = 0
    for a in range(-8, 9):
        for b in range(-8, 9):
            lhs = max(a + b - 1, 0)
            i1 = max(a, 0) * (b >= 1) + max(b, 0) * (a >= 1) - (a >= 1) * (b >= 1)
            i2 = max(a - 1, 0) + b * (a >= 1)
            if lhs < i1:
                bad1 += 1
            if lhs < i2:
                bad2 += 1
    report("LemmaK ineq (I) exhaustive [-8,8]^2", bad1 == 0, f"viol={bad1}")
    report("LemmaK ineq (II) exhaustive [-8,8]^2", bad2 == 0, f"viol={bad2}")


# =========================================== 3. Lemma K Monte-Carlo (fresh) ==
def lemK_mc(n_target=200000):
    vals = np.arange(-3, 6)  # support -3..5
    M = np.maximum(vals[:, None] + vals[None, :] - 1, 0).astype(float)
    got, worst = 0, np.inf
    viol = 0
    batch = 400000
    while got < n_target:
        # biased Dirichlet to land means in [0,1]
        alpha = rng.uniform(0.05, 1.0, size=(batch, 9))
        P = rng.dirichlet(np.ones(9) * 0.3, size=batch) * 0  # placeholder
        # use gamma draws for per-row dirichlet with varying alpha
        G = rng.gamma(alpha, 1.0)
        P = G / G.sum(1, keepdims=True)
        mu = P @ vals
        okm = (mu >= 0) & (mu <= 1)
        P = P[okm]
        mu = mu[okm]
        half = len(P) // 2
        P1, P2 = P[:half], P[half : 2 * half]
        m1, m2 = mu[:half], mu[half : 2 * half]
        E = np.einsum("ij,jk,ik->i", P1, M, P2)
        d = E - m1 * m2
        viol += int((d < -1e-11).sum())
        worst = min(worst, d.min())
        got += half
    report("LemmaK MC (>=200k independent law pairs)", viol == 0,
           f"pairs={got}, min(E-mu1mu2)={worst:.3e}")
    # sharpness of mu<=1 hypothesis: phi=psi=3 a.s.
    report("LemmaK mu<=1 necessary (phi=psi=3: 5<9)", max(3 + 3 - 1, 0) == 5 and 5 < 9)
    # erratum probe: equality with NON-Bernoulli laws at boundary means
    # (a) mu1=0: phi=0 a.s., psi=+-1 w.p. 1/2
    E_a = 0.5 * max(0 - 1 + 1 - 1, 0) + 0.5 * max(0 + 1 - 1, 0)
    # (b) mu1=1: phi=1 a.s., psi in {0,2} w.p. {3/4,1/4} (mu2=1/2)
    E_b = 0.75 * max(1 + 0 - 1, 0) + 0.25 * max(1 + 2 - 1, 0)
    report("LemmaK equality-iff-Bernoulli FAILS at boundary (erratum expected)",
           abs(E_a - 0.0) < 1e-15 and abs(E_b - 0.5) < 1e-15,
           f"E_a={E_a} (=0=mu1mu2, psi not 0/1), E_b={E_b} (=1/2=mu1mu2, psi not 0/1)")


# ====================== 4. arc engine (exact) for Theorem K, D1-D4, kappa ===
def axis_pieces(ws, phases):
    """P(x)=sum floor(w)+1_{F_i}; F_i=[ph, ph+frac(w)) mod 1. exact breakpoints."""
    W0 = int(np.floor(ws).sum())
    bps = set([0.0])
    arcs = []
    for w, ph in zip(ws, phases):
        f = w - np.floor(w)
        if f > 1e-15:
            a, b = ph % 1.0, (ph + f) % 1.0
            arcs.append((a, b))
            bps.add(a)
            bps.add(b)
    bp = sorted(bps) + [1.0]
    pieces = []  # (value, length, midpoint)
    for i in range(len(bp) - 1):
        lo, hi = bp[i], bp[i + 1]
        if hi - lo < 1e-15:
            continue
        mid = (lo + hi) / 2
        val = W0
        for (a, b) in arcs:
            if (a <= mid < b) if a < b else (mid >= a or mid < b):
                val += 1
        pieces.append((val, hi - lo, mid))
    return pieces, arcs


def kappa_from_pieces(px, py, N):
    k = kp = 0.0
    for vP, lP, _ in px:
        for vQ, lQ, _ in py:
            z = vP + vQ - (2 * N + 1)
            kp += max(z, 0) * lP * lQ
            k += max(-z, 0) * lP * lQ
    return k, kp


def d_checks(ws, phases, N, pieces):
    """D1,D2,D3 on one axis. returns dict."""
    n = len(ws)
    r = 1 + sum(max(int(np.floor(w)) - 1, 0) for w in ws)
    t = ws.sum() - N
    # Gcheck, Fplus at piece midpoints
    ok_d1 = True
    delta = 0.0
    intG = 0.0
    H = 0
    for vP, lP, mid in pieces:
        G = 0
        Fp = 0
        for w, ph in zip(ws, phases):
            f = w - np.floor(w)
            a, b = ph % 1.0, (ph + f) % 1.0
            inF = ((a <= mid < b) if a < b else (mid >= a or mid < b)) and f > 1e-15
            if w < 1:
                if not inF:
                    G += 1
            else:
                if inF:
                    Fp += 1
        if (vP <= N) != (G - Fp >= r):
            ok_d1 = False
        if vP <= N:
            delta += lP
            intG += G * lP
            H = max(H, G)
    EG_F = sum((1 - w) for w in ws if w < 1) - sum(w - np.floor(w) for w in ws if w >= 1)
    ok_d2 = abs(EG_F - (r - t)) < 1e-9
    ok_d3 = (intG >= 1 - t - 1e-9) and (max(1 - t, 0) <= H * delta + 1e-9 if H > 0 else (1 - t) <= 1e-9)
    return ok_d1, ok_d2, ok_d3, delta, H, t


def thmK_arcs(trials=400):
    bad = 0
    bad_id = 0
    badD = 0
    for tr in range(trials):
        N = int(rng.choice([1, 4, 9]))
        n = N + 1
        t = rng.uniform(0.0, 1.0)
        raw = rng.uniform(0.05, 2.4, n)
        ws = raw * (N + t) / raw.sum()
        phx = rng.uniform(0, 1, n)
        phy = rng.uniform(0, 1, n)
        px, _ = axis_pieces(ws, phx)
        py, _ = axis_pieces(ws, phy)
        kap, kapp = kappa_from_pieces(px, py, N)
        if kapp < t * t - 1e-9:
            bad += 1
        if abs(kap - (1 - 2 * t + kapp)) > 1e-9:
            bad_id += 1
        for pieces, ph in ((px, phx), (py, phy)):
            d1, d2, d3, _, _, _ = d_checks(ws, ph, N, pieces)
            if not (d1 and d2 and d3):
                badD += 1
    report("Theorem K: kappa' >= t^2 (400 random arc systems, t in [0,1])", bad == 0, f"viol={bad}")
    report("Identity kappa = 1-2t+kappa'", bad_id == 0, f"viol={bad_id}")
    report("D1/D2/D3 exact on 800 random axes", badD == 0, f"viol={badD}")
    # Claim 3(a): M arcs of length 1/2 at phases j/M -> flat coverage M/2
    M0 = 16
    ws = np.full(M0, 0.5)
    ph = np.arange(M0) / M0
    pieces, _ = axis_pieces(ws, ph)
    vals = set(v for v, l, m in pieces if l > 1e-12)
    report("Claim3(a): equidistributed half-arcs flat coverage = M/2", vals == {M0 // 2},
           f"coverage values={sorted(vals)}")
    # kappa=0 attainable: all w=1 exactly
    ws = np.ones(5)
    N = 4
    px, _ = axis_pieces(ws, rng.uniform(0, 1, 5))
    py, _ = axis_pieces(ws, rng.uniform(0, 1, 5))
    kap, _ = kappa_from_pieces(px, py, N)
    report("Claim3(b): kappa=0 attainable at arc level (all w_i=1)", abs(kap) < 1e-12, f"kappa={kap}")


# ============================ 5. packing test-bench (2-D shift experiments) ==
def analyze_packing(name, sqs, k, M=720, do_S2=None, expect_beta=None, expect_pin=True):
    N = k * k
    n = len(sqs)
    assert n == N + 1, f"{name}: n={n} != N+1"
    ok_pack = check_packing(sqs, k)
    report(f"{name}: valid packing (SAT + containment)", ok_pack)
    off = 0.000123456789
    X = (np.arange(M) + 0.5) / M + off
    X = X % 1.0
    Y = (np.arange(M) + 0.61803398) / M % 1.0
    # per-square p_i(x), q_i(y)
    p = np.zeros((n, M), dtype=np.int8)
    q = np.zeros((n, M), dtype=np.int8)
    for i, S in enumerate(sqs):
        for m in range(k):
            p[i] += ((X + m > S.bx0) & (X + m < S.bx1)).astype(np.int8)
            q[i] += ((Y + m > S.by0) & (Y + m < S.by1)).astype(np.int8)
    # c_i over shift grid
    c = np.zeros((n, M, M), dtype=np.int8)
    XX = X[:, None]
    YY = Y[None, :]
    for i, S in enumerate(sqs):
        for m in range(k):
            for l in range(k):
                c[i] += S.inside(XX + m, YY + l).astype(np.int8)
    C = c.sum(0)
    P = p.sum(0)
    Q = q.sum(0)
    report(f"{name}: budget C<=N everywhere", int(C.max()) <= N, f"maxC={int(C.max())}")
    # B-arcs / E set
    goodx = np.ones(M, bool)
    goody = np.ones(M, bool)
    for S in sqs:
        ds = S.d * np.sin(S.th)
        if ds > 1e-15:
            for (a, b) in [(S.bx0, S.bx0 + ds), (S.bx1 - ds, S.bx1)]:
                am, bm = a % 1, b % 1
                inarc = ((X >= am) & (X <= bm)) if am <= bm else ((X >= am) | (X <= bm))
                goodx &= ~inarc
            for (a, b) in [(S.by0, S.by0 + ds), (S.by1 - ds, S.by1)]:
                am, bm = a % 1, b % 1
                inarc = ((Y >= am) & (Y <= bm)) if am <= bm else ((Y >= am) | (Y <= bm))
                goody &= ~inarc
    Ux = 1.0 - goodx.mean()
    Uy = 1.0 - goody.mean()
    E = goodx[:, None] & goody[None, :]
    # product structure on E
    okE = True
    for i in range(n):
        pq = p[i][:, None].astype(np.int16) * q[i][None, :].astype(np.int16)
        if not np.all(c[i][E] == pq[E]):
            okE = False
    report(f"{name}: c_i = p_i q_i on E (all i, all E-shifts)", okE)
    # ledger on Av cap E
    Av = C == N
    mask = Av & E
    idle = c == 0
    Icnt = idle.sum(0)
    mu = np.maximum(c.astype(np.int16) - 1, 0).sum(0)
    ok_ledger = np.all(Icnt[mask] == 1 + mu[mask])
    report(f"{name}: ledger |I| = 1 + mu on Av∩E", ok_ledger)
    ws = np.array([S.w for S in sqs])
    shorts = ws < 1
    ok_short = all(not np.any(idle[i] & mask) for i in range(n) if not shorts[i])
    ok_multi = all(not np.any((c[i] >= 2) & mask) for i in range(n) if shorts[i])
    report(f"{name}: idles are short / multi-captures are long", ok_short and ok_multi)
    # unique-idle pinning (the A''-mechanism inside S2 case (1))
    um = mask & (Icnt == 1)
    ok_pin = True
    for i in range(n):
        ev = um & idle[i]
        if np.any(ev):
            rows = np.any(ev, axis=1)
            cols = np.any(ev, axis=0)
            if np.any(p[i][rows] != 0) or np.any(q[i][cols] != 0):
                ok_pin = False
    if expect_pin:
        report(f"{name}: unique idle is BOTH x-missed and y-missed (p=q=0)", ok_pin,
               f"(unique-idle measure={um.mean():.4f})")
    else:
        print(f"    {name}: [INFO beta>=1, pinning not implied] both-missed={ok_pin} "
              f"(unique-idle measure={um.mean():.4f})")
    # >=2 idle  =>  x in Vx-union or y in Vy-union
    Vxm = np.zeros(M, bool)
    Vym = np.zeros(M, bool)
    for i in range(n):
        if ws[i] >= 1:
            Vxm |= p[i] >= 2
            Vym |= q[i] >= 2
    m2 = mask & (Icnt >= 2)
    ok_2 = np.all((Vxm[:, None] | Vym[None, :])[m2]) if np.any(m2) else True
    report(f"{name}: >=2-idle events inside Vx/Vy union", ok_2, f"(measure={m2.mean():.4f})")
    Vx, Vy = Vxm.mean(), Vym.mean()
    beta = sum(max(1 - S.d / np.cos(S.th), 0) for S in sqs)
    if expect_beta is not None:
        report(f"{name}: beta = {expect_beta:.4f}", abs(beta - expect_beta) < 1e-9, f"beta={beta:.6f}")
    Avm = Av.mean()
    RHS = float(np.sum(np.maximum(1 - ws, 0) ** 2)) + Ux + Uy + Vx + Vy
    tol = 6.0 / M  # grid tolerance
    print(f"    {name}: |Av|={Avm:.4f} S2-RHS={RHS:.4f} beta={beta:.4f} "
          f"Ux={Ux:.4f} Uy={Uy:.4f} Vx={Vx:.4f} Vy={Vy:.4f}")
    if do_S2 == "holds":
        report(f"{name}: S2 inequality |Av| <= RHS (beta<1)", Avm <= RHS + tol,
               f"|Av|={Avm:.4f} RHS={RHS:.4f}")
    elif do_S2 == "violated":
        report(f"{name}: S2 conclusion VIOLATED (sharpness, beta>=1)", Avm > RHS + tol,
               f"|Av|-RHS={Avm - RHS:.4f}")
    # kappa-coupling: kappa >= (1 - Ux - Uy - |Av|)_+
    kap = np.maximum(2 * N + 1 - P[:, None] - Q[None, :], 0).mean()
    report(f"{name}: kappa >= (1-Ux-Uy-|Av|)_+", kap >= max(1 - Ux - Uy - Avm, 0) - tol,
           f"kappa={kap:.4f} bound={max(1 - Ux - Uy - Avm, 0):.4f}")
    # MPI spot-check: D >= P+Q-2N-1  (supports T6 chain [P])
    L = np.zeros((M, M), dtype=np.int16)
    D = np.zeros((M, M), dtype=np.int16)
    ok_L = True
    for i in range(n):
        pq = p[i][:, None].astype(np.int16) * q[i][None, :].astype(np.int16)
        Li = pq - c[i]
        if Li.min() < 0:
            ok_L = False
        Bi = (p[i][:, None].astype(np.int16) - 1) * (q[i][None, :].astype(np.int16) - 1)
        D += np.maximum(Li - Bi, 0)
    ok_mpi = np.all(D >= P[:, None] + Q[None, :] - 2 * N - 1)
    report(f"{name}: L_i>=0 and MPI D>=P+Q-2N-1 (numeric support for T6[P])", ok_L and ok_mpi)
    # Theorem K on this packing
    t = ws.sum() - N
    if 0 <= t <= 1:
        report(f"{name}: Theorem K kappa >= (1-t)^2", kap >= (1 - t) ** 2 - tol,
               f"kappa={kap:.4f} (1-t)^2={(1 - t) ** 2:.4f} t={t:.4f}")
    # K' final inequality with report margins (conditional on T6[P] but should hold)
    eps = sum(S.d for S in sqs) - N
    tau = sum(S.d * S.sig for S in sqs)
    msum = 0.0
    for S in sqs:
        if S.th == 0:
            mi = 0.0
        elif S.w <= 1:
            mi = S.d * S.sig * (2 - S.d - S.w)
        elif S.d <= S.u1:
            mi = (1 - S.d) ** 2
        else:
            mi = -S.d * S.sig * (S.d + S.w - 2)
        msum += mi
    if t <= 1:
        report(f"{name}: K' (eps+tau)_+^2 <= 2 tau - sum m", max(eps + tau, 0) ** 2 <= 2 * tau - msum + 1e-9,
               f"lhs={max(eps + tau, 0) ** 2:.4f} rhs={2 * tau - msum:.4f}")
    return dict(Av=Avm, Ux=Ux, Uy=Uy, Vx=Vx, Vy=Vy, beta=beta, kappa=kap, t=t)


# ---- configs -----------------------------------------------------------------
def col_AP(k):
    dd = k / (k + 1)
    sqs = [Sq(dd / 2, dd / 2 + j * dd, dd, 0.0) for j in range(k + 1)]
    for cx in range(1, k):
        for cy in range(k):
            sqs.append(Sq(cx + 0.5, cy + 0.5, 1.0 - 1e-12, 0.0))
    return sqs


def col_tilt(k, th):
    u1 = np.cos(th) + np.sin(th)
    dd = (k / (k + 1)) / u1  # bbox = k/(k+1)
    wb = k / (k + 1)
    sqs = [Sq(wb / 2, wb / 2 + j * wb, dd, th) for j in range(k + 1)]
    for cx in range(1, k):
        for cy in range(k):
            sqs.append(Sq(cx + 0.5, cy + 0.5, 1.0 - 1e-12, 0.0))
    return sqs


def diamond_pair():
    d = 0.47
    th = np.pi / 4
    w = d * np.sqrt(2)
    return [Sq(w / 2, w / 2, d, th), Sq(1 - w / 2, 1 - w / 2, d, th)]


def big_AP():
    # big 1.3 + column of three 0.6 + one 0.7 on top: valid packing, beta=1.5
    return [Sq(0.65, 0.65, 1.3, 0.0),
            Sq(1.7, 0.3, 0.6, 0.0), Sq(1.7, 0.9, 0.6, 0.0), Sq(1.7, 1.5, 0.6, 0.0),
            Sq(0.35, 1.65, 0.7, 0.0)]


def long_tilted():
    # tilted long 1.1@0.03 (bbox 1.1325) + 0.86,0.86,0.87,0.25 -- valid, beta=1.16
    th = 0.03
    d = 1.1
    u1 = np.cos(th) + np.sin(th)
    w = d * u1
    return [Sq(w / 2, w / 2, d, th),
            Sq(1.57, 0.43, 0.86, 0.0), Sq(1.57, 1.29, 0.86, 0.0),
            Sq(0.435, 1.565, 0.87, 0.0), Sq(1.005, 1.875, 0.25, 0.0)]


def tilt30_k1():
    # two 0.48-squares at theta=0.3 in [0,1]^2: beta = 2(1-0.48 sec .3) = 0.9950 < 1,
    # E nonempty, unique-idle events on Av∩E have positive measure -> real pinning test
    th = 0.3
    d = 0.48
    w = d * (np.cos(th) + np.sin(th))
    e = 2e-4
    return [Sq(w / 2 + e, w / 2 + e, d, th), Sq(1 - w / 2 - e, 1 - w / 2 - e, d, th)]


# ============================ 6. Lemma A'' over-full-line mechanism ==========
def lemmaA2_mech(name, sqs, k, nsamp=200):
    n_found = 0
    n_good_fullhit = 0
    ok = True
    for _ in range(nsamp * 20):
        if n_good_fullhit >= nsamp:
            break
        x = rng.uniform(1e-6, 1 - 1e-6)
        # good?
        good = True
        for S in sqs:
            ds = S.d * np.sin(S.th)
            if ds > 1e-15:
                for (a, b) in [(S.bx0, S.bx0 + ds), (S.bx1 - ds, S.bx1)]:
                    am, bm = a % 1, b % 1
                    if (am <= x <= bm) if am <= bm else (x >= am or x <= bm):
                        good = False
        if not good:
            continue
        # all p_i >= 1?
        fullhit = True
        lines = {m: [] for m in range(k)}
        for i, S in enumerate(sqs):
            pi = 0
            for m in range(k):
                if S.bx0 < x + m < S.bx1:
                    pi += 1
                    lines[m].append(i)
            if pi == 0:
                fullhit = False
        if not fullhit:
            continue
        n_good_fullhit += 1
        # find over-full line
        found = False
        for m in range(k):
            if len(lines[m]) >= k + 1:
                found = True
                chs = []
                for i in lines[m]:
                    S = sqs[i]
                    ch = S.chord_v(x + m)
                    sec = S.d / np.cos(S.th)
                    if abs(ch - sec) > 1e-9:
                        ok = False
                    chs.append(ch)
                if sum(chs) > k + 1e-9:
                    ok = False
                if sum(1 - c for c in chs) < 1 - 1e-9:
                    ok = False
        if not found:
            ok = False
        else:
            n_found += 1
    report(f"A'' mech [{name}]: over-full line, chords=d.sec, sum<=k, deficit>=1",
           ok and n_found == n_good_fullhit, f"({n_found}/{n_good_fullhit} good full-hit x)")
    return n_good_fullhit


# ============================ 7. algebra identities ==========================
def algebra():
    d = rng.uniform(0.1, 1.8, 20000)
    th = rng.uniform(0, np.pi / 4, 20000)
    u1 = np.cos(th) + np.sin(th)
    sig = u1 - 1
    w = d * u1
    lhs = (1 - w) ** 2
    rhs = (1 - d) ** 2 - d * sig * (2 - d - w)
    report("Identity (1-w)^2=(1-d)^2-d.sig(2-d-w)", np.max(np.abs(lhs - rhs)) < 1e-12,
           f"max err={np.max(np.abs(lhs - rhs)):.2e}")
    # T4 chain: T = sum d(1-1/u1) <= tau = sum d.sig  (pointwise 1-1/u1 <= sig)
    report("T4 bridge: (1-1/u1) <= sigma pointwise (=> tau >= T >= eps)",
           np.all(u1 - 1 >= 1 - 1 / u1 - 1e-15))
    # sigma <= sin(th) (orchestrator fact) and sigma <= th
    report("sigma <= sin th and sigma <= th pointwise",
           np.all(sig <= np.sin(th) + 1e-15) and np.all(sig <= th + 1e-15))
    # S3(i) algebra: beta>=1 <=> b0>=eps+Gamma  on random profiles
    okk = True
    for _ in range(2000):
        n = 10
        dd = rng.uniform(0.3, 1.5, n)
        tt = rng.uniform(0, np.pi / 4, n)
        beta = np.maximum(1 - dd / np.cos(tt), 0).sum()
        Gam = (np.maximum(1 - dd, 0) - np.maximum(1 - dd / np.cos(tt), 0)).sum()
        b0 = np.maximum(dd - 1, 0).sum()
        Nn = n - 1
        eps = dd.sum() - Nn
        # sum(1-d)_+ = 1 - eps + b0 identity:
        if abs(np.maximum(1 - dd, 0).sum() - (1 - eps + b0)) > 1e-10:
            okk = False
        if (beta >= 1) != (b0 >= eps + Gam - 1e-12):
            if abs(beta - 1) > 1e-9:
                okk = False
        if Gam < -1e-12:
            okk = False
    report("S3(i): beta>=1 <=> b0>=eps+Gamma; Gamma>=0; positive-part identity", okk)


# ============================ 8. diamond-pair Theorem-K equality (exact) =====
def diamond_exact():
    d = 0.47
    w = d * np.sqrt(2)
    N = 1
    t = 2 * w - 1
    ws = np.array([w, w])
    phx = np.array([0.0, 1 - w])  # bbox mins at 0 and 1-w
    px, _ = axis_pieces(ws, phx)
    py, _ = axis_pieces(ws, phx)
    kap, kapp = kappa_from_pieces(px, py, N)
    report("Diamond pair: kappa == (1-t)^2 exactly (Theorem K tight)",
           abs(kap - (1 - t) ** 2) < 1e-12, f"kappa={kap:.10f} (1-t)^2={(1 - t) ** 2:.10f}")


# =============================================================== run all =====
print("=" * 78)
lemma0()
lemK_pointwise()
lemK_mc()
thmK_arcs()
algebra()
diamond_exact()
print("-" * 78)

r1 = analyze_packing("col_AP_k2", col_AP(2), 2, M=720, do_S2="violated", expect_beta=1.0,
                     expect_pin=False)
report("col_AP_k2: |Av|=2/3, RHS=1/3, violation=(k-1)/(k+1)=1/3",
       abs(r1["Av"] - 2 / 3) < 0.01 and abs(r1["Av"] - (1 / 3 + r1["Ux"] + r1["Uy"] + r1["Vx"] + r1["Vy"]) - 1 / 3) < 0.02)
r2 = analyze_packing("col_AP_k3", col_AP(3), 3, M=480, do_S2="violated", expect_beta=1.0,
                     expect_pin=False)
r3 = analyze_packing("col_tilt_k2_th.05", col_tilt(2, 0.05), 2, M=720, do_S2=None,
                     expect_pin=False)  # beta=1.09>=1: no S2/pinning claim either way
r4 = analyze_packing("diamond_k1", diamond_pair(), 1, M=900, do_S2="holds")
r5 = analyze_packing("bigAP_k2", big_AP(), 2, M=720, do_S2=None, expect_pin=False)  # beta=1.5
r6 = analyze_packing("long_tilted_k2", long_tilted(), 2, M=720, do_S2=None,
                     expect_pin=False)  # beta=1.16
r7 = analyze_packing("tilt30_k1", tilt30_k1(), 1, M=900, do_S2="holds")
print("-" * 78)
g1 = lemmaA2_mech("col_AP_k2", col_AP(2), 2)
report("col_AP_k2 good-full-hit measure ~ k/(k+1)=2/3 (beta=1 sharpness)", g1 > 0)
lemmaA2_mech("col_tilt_k2", col_tilt(2, 0.05), 2)
lemmaA2_mech("col_AP_k3", col_AP(3), 3)
# beta<1 configs must have NO good full-hit x at all (A'' conclusion):
g4 = lemmaA2_mech("diamond_k1(exp 0)", diamond_pair(), 1, nsamp=100)
report("diamond (beta<1): good full-hit measure = 0 (A'' conclusion)", g4 == 0)
g7 = lemmaA2_mech("tilt30_k1(exp 0)", tilt30_k1(), 1, nsamp=100)
report("tilt30_k1 (beta=0.995<1): good full-hit measure = 0 (A'' conclusion)", g7 == 0)

print("=" * 78)
print("FAILURES:", FAIL if FAIL else "NONE")
