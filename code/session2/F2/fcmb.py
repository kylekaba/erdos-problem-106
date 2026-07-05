import numpy as np

def square_mask(X, Y, cx, cy, th, d):
    c, s = np.cos(th), np.sin(th)
    u = (X - cx) * c + (Y - cy) * s
    v = -(X - cx) * s + (Y - cy) * c
    return (np.abs(u) <= d / 2) & (np.abs(v) <= d / 2)

def analyze(squares, k, M=1200, second_moment=False):
    """squares: list of (cx,cy,theta,d). Returns dict with g, piG, s, F, and optionally 2nd moment."""
    xs = (np.arange(k * M) + 0.5) / M
    X, Y = np.meshgrid(xs, xs, indexing='ij')
    occ = np.zeros(X.shape, dtype=np.int16)
    for (cx, cy, th, d) in squares:
        occ += square_mask(X, Y, cx, cy, th, d).astype(np.int16)
    overlap_area = ((occ > 1) * (occ - 1)).sum() / M**2  # double-counted area
    Gmask = occ == 0
    g = Gmask.mean() * k * k
    mult = Gmask.reshape(k, M, k, M).sum(axis=(0, 2))  # multiplicity of gap at each torus offset
    piG = (mult > 0).mean()
    s = sum((1 - d) ** 2 for (_, _, _, d) in squares)
    out = dict(g=g, piG=piG, s=s, F=piG - (1 - s), overlap=overlap_area,
               sumd=sum(d for *_, d in squares), Av=1 - piG)
    if second_moment:
        Eh2 = (mult.astype(float) ** 2).mean()
        autocorr = Eh2 - g
        out.update(Eh2=Eh2, autocorr=autocorr, PZ_rhs=g * g / max(1 - s, 1e-12),
                   condE_holds=(Eh2 <= g * g / max(1 - s, 1e-12)))
    return out

def av_direct(squares, k, Mp=800):
    """Direct |Av| by shift sampling: count shifts p in [0,1)^2 with all N lattice points captured."""
    ps = (np.arange(Mp) + 0.5) / Mp
    PX, PY = np.meshgrid(ps, ps, indexing='ij')
    N = k * k
    captured = np.zeros(PX.shape, dtype=np.int16)
    for ix in range(k):
        for iy in range(k):
            lx, ly = PX + ix, PY + iy
            inc = np.zeros(PX.shape, dtype=bool)
            for (cx, cy, th, d) in squares:
                c, s = np.cos(th), np.sin(th)
                u = (lx - cx) * c + (ly - cy) * s
                v = -(lx - cx) * s + (ly - cy) * c
                inc |= (np.abs(u) <= d / 2) & (np.abs(v) <= d / 2)
            captured += inc.astype(np.int16)
    return (captured == N).mean()

# exact feasibility: SAT for tilted squares + containment
def corners(cx, cy, th, d):
    c, s = np.cos(th), np.sin(th)
    h = d / 2
    pts = []
    for su in (-1, 1):
        for sv in (-1, 1):
            pts.append((cx + su * h * c - sv * h * s, cy + su * h * s + sv * h * c))
    return np.array(pts)

def sat_disjoint(sq1, sq2, tol=1e-9):
    P1, P2 = corners(*sq1), corners(*sq2)
    for (th,) in [(sq1[2],), (sq2[2],)]:
        for ang in (th, th + np.pi / 2):
            ax = np.array([np.cos(ang), np.sin(ang)])
            a1, a2 = P1 @ ax, P2 @ ax
            if a1.max() <= a2.min() + tol or a2.max() <= a1.min() + tol:
                return True
    return False

def feasible(squares, k, tol=1e-9):
    n = len(squares)
    for sq in squares:
        P = corners(*sq)
        if P.min() < -tol or P.max() > k + tol:
            return False
    for i in range(n):
        for j in range(i + 1, n):
            if not sat_disjoint(squares[i], squares[j], tol):
                return False
    return True

if __name__ == '__main__':
    np.set_printoptions(precision=6)
    # 1. VALIDATION: split-cell config at k=2, a=0.37  (expect F = 0 exactly)
    a = 0.37; b = 1 - a
    split = [(0.5, 0.5, 0, 1), (0.5, 1.5, 0, 1), (1.5, 1.5, 0, 1),
             (1 + a/2, a/2, 0, a), (1 + b/2, a + b/2, 0, b)]
    r = analyze(split, 2, M=1200)
    print('SPLIT-CELL a=0.37 (expect F=0):', {k2: round(v, 6) for k2, v in r.items()})
    print('  feasible:', feasible(split, 2))

    # 2. ROW CONFIG k=2: three 2/3-squares bottom row + two units (classical extremal, sum d = 4)
    d3 = 2/3
    row2 = [(d3/2, d3/2, 0, d3), (1.0, d3/2, 0, d3), (2 - d3/2, d3/2, 0, d3),
            (0.5, 1.5, 0, 1), (1.5, 1.5, 0, 1)]
    def show(r):
        return {k2: (bool(v) if isinstance(v, (bool, np.bool_)) else round(float(v), 6)) for k2, v in r.items()}
    r = analyze(row2, 2, M=1200, second_moment=True)
    print('ROW k=2 (expect piG=1/3, s=1/3, F=-1/3):', show(r))
    print('  feasible:', feasible(row2, 2))
    print('  |Av| direct shift-sampling (expect 2/3):', round(av_direct(row2, 2, 900), 6))

    # 3. ROW CONFIG k=3: four 3/4-squares bottom row + six units
    d4 = 3/4
    row3 = ([(d4/2 + i*d4, d4/2, 0, d4) for i in range(4)] +
            [(0.5 + i, 1.5, 0, 1) for i in range(3)] +
            [(0.5 + i, 2.5, 0, 1) for i in range(3)])
    r = analyze(row3, 3, M=900, second_moment=True)
    print('ROW k=3 (expect piG=1/4, s=1/4, F=-1/2):', show(r))
    print('  feasible:', feasible(row3, 3))
    print('  |Av| direct (expect 3/4):', round(av_direct(row3, 3, 600), 6))

    # 4. STRADDLE FAMILY k=2, delta in (0,1/3): expect F = -delta
    for delta in (0.05, 0.1, 0.2, 0.3):
        dd = 1 - delta; bb = 2 * delta
        strad = [(dd/2, dd/2, 0, dd), (1 + delta + dd/2, dd/2, 0, dd),
                 (1.0, bb/2, 0, bb), (0.5, 1.5, 0, 1), (1.5, 1.5, 0, 1)]
        r = analyze(strad, 2, M=1500)
        print(f'STRADDLE delta={delta} (expect F={-delta}):',
              'F=', round(r['F'], 6), 'piG=', round(r['piG'], 6), 's=', round(r['s'], 6),
              'sumd=', round(r['sumd'], 6), 'feasible:', feasible(strad, 2))
