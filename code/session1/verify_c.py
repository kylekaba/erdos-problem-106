import numpy as np, math
from fractions import Fraction as F

rng = np.random.default_rng(7)

print("=== Claim 1: identity G+V = k^2 - (k^2+eps)^2/(k^2+1) ===")
for k in [3,7]:
    n = k*k+1
    d = rng.uniform(0.3,1.3,size=n)
    S = d.sum(); eps = S - k*k
    G = k*k - (d**2).sum()
    m = S/n
    V = ((d-m)**2).sum()
    lhs = G+V
    rhs = k*k - S**2/n
    rhs2 = (k*k*(1-2*eps)-eps**2)/n
    print(k, lhs-rhs, lhs-rhs2)

print("\n=== Claim 5: inscribed axis-parallel square d/(c+s), theta unfolded in [0,pi) ===")
worst = 0.0
for _ in range(20000):
    d = rng.uniform(0.05, 3.0)
    th_raw = rng.uniform(0, math.pi)          # arbitrary orientation
    th = th_raw % (math.pi/2)
    thf = min(th, math.pi/2 - th)             # folded to [0,pi/4]
    c, s = math.cos(thf), math.sin(thf)
    a = d/(c+s)
    # world-frame corners of axis-parallel square side a, center origin
    for sx in (-1,1):
        for sy in (-1,1):
            x, y = sx*a/2, sy*a/2
            # rotate world point into S's frame by -th_raw; S = [-d/2,d/2]^2 in its frame
            cr, sr = math.cos(th_raw), math.sin(th_raw)
            u =  cr*x + sr*y
            v = -sr*x + cr*y
            worst = max(worst, abs(u)-d/2, abs(v)-d/2)
print("max corner excess over d/2 (should be <=0 up to fp):", worst)

# chain 1-1/(c+s) <= c+s-1 <= theta_folded on a grid
ths = np.linspace(0, math.pi/4, 100001)
c, s = np.cos(ths), np.sin(ths)
chain1 = ((1-1/(c+s)) - (c+s-1)).max()
chain2 = ((c+s-1) - ths).max()
# concavity chord lower bound c+s-1 >= (4(sqrt2-1)/pi) theta
chord = ((4*(math.sqrt(2)-1)/math.pi)*ths - (c+s-1)).max()
print("max[(1-1/(c+s))-(c+s-1)] =", chain1, "  max[(c+s-1)-theta] =", chain2, "  chord-bound violation:", chord)

print("\n=== Claim 6: wall lemma numeric adversarial test ===")
def square(cx, cy, d, th):
    # corners
    cr, sr = math.cos(th), math.sin(th)
    pts = []
    for sx,sy in [(-1,-1),(1,-1),(1,1),(-1,1)]:
        x = cx + (sx*d/2)*cr - (sy*d/2)*sr
        y = cy + (sx*d/2)*sr + (sy*d/2)*cr
        pts.append((x,y))
    return pts

def lower_env(pts, x):
    # min y over square at abscissa x, or None
    best = None
    n = len(pts)
    for i in range(n):
        (x1,y1),(x2,y2) = pts[i], pts[(i+1)%n]
        if x1 == x2:
            if x == x1:
                yv = min(y1,y2)
                best = yv if best is None else min(best,yv)
            continue
        if min(x1,x2) <= x <= max(x1,x2):
            t = (x-x1)/(x2-x1)
            yv = y1 + t*(y2-y1)
            best = yv if best is None else min(best,yv)
    return best

def inside(pts, x, y):
    n=len(pts); sgn=None
    for i in range(n):
        (x1,y1),(x2,y2)=pts[i],pts[(i+1)%n]
        cr=(x2-x1)*(y-y1)-(y2-y1)*(x-x1)
        if cr==0: continue
        if sgn is None: sgn = cr>0
        elif (cr>0)!=sgn: return False
    return True

k = 3.0
cfgs = [
    # (cx,cy,d,theta_folded)  -- includes theta=0 full-bottom-edge and theta=pi/4
    (0.85, 0.85, 1.0, 0.3),
    (2.35, 0.75, 0.8, math.pi/4),
    (1.6, 2.2, 0.9, 0.0),
    (2.6, 2.4, 0.7, 0.15),
]
sqs = [square(*c) for c in cfgs]
# disjointness check by sampling
M = 400
xs = np.linspace(0.001, k-0.001, M)
ys = np.linspace(0.001, k-0.001, M)
bad = 0; outside=0
for p in sqs:
    for (x,y) in p:
        if not (0<=x<=k and 0<=y<=k): outside+=1
for xi in xs[::4]:
    for yi in ys[::4]:
        cnt = sum(inside(p, xi, yi) for p in sqs)
        if cnt > 1: bad += 1
print("corners outside T:", outside, " overlap samples:", bad)

# phi and A_i
dx = k/len(xs)
int_phi = 0.0; Alen = [0.0]*len(sqs); Aempty = 0.0
# per-square (y_i, v_i)
yv = []
for p in sqs:
    ymin = min(pt[1] for pt in p)
    vxs = [pt[0] for pt in p if abs(pt[1]-ymin) < 1e-12]
    yv.append((ymin, sum(vxs)/len(vxs)))
LHS_A = [0.0]*len(sqs)   # accumulate integral of y_i + tan|x-v| over A_i for cross-check
for x in xs:
    vals = [lower_env(p, x) for p in sqs]
    cand = [(v,i) for i,v in enumerate(vals) if v is not None]
    if not cand:
        phi = k; Aempty += dx
    else:
        phi, i0 = min(cand)
        Alen[i0] += dx
        LHS_A[i0] += dx*(yv[i0][0] + math.tan(cfgs[i0][3])*abs(x - yv[i0][1]))
    int_phi += phi*dx

LHS = sum(yv[i][0]*Alen[i] + math.tan(cfgs[i][3])/4*Alen[i]**2 for i in range(len(sqs))) + k*Aempty
LHS_sharp = sum(yv[i][0]*Alen[i] + math.sin(cfgs[i][3])*math.cos(cfgs[i][3])/2*Alen[i]**2 for i in range(len(sqs))) + k*Aempty
G = k*k - sum(c[2]**2 for c in cfgs)
print(f"LHS(T2)={LHS:.4f}  LHS(sharp sc/2)={LHS_sharp:.4f}  pointwise-envelope integral={sum(LHS_A)+k*Aempty:.4f}  int_phi={int_phi:.4f}  G={G:.4f}")
print("T2 holds:", LHS <= int_phi + 1e-6 <= G + 1e-6, " sharp holds:", LHS_sharp <= int_phi + 1e-6)

# wall-row constant check: row of unit squares tilted theta resting on wall
for th in [0.05, 0.2, math.pi/4]:
    c_,s_ = math.cos(th), math.sin(th)
    w = c_+s_
    per_len_true = s_*c_/w          # true area under envelope per unit wall length
    per_len_T2   = math.tan(th)/4*w # T2 bound per unit length (|A_i|=w)
    per_len_shp  = s_*c_/2*w
    print(f"theta={th:.3f}: true={per_len_true:.5f}  T2={per_len_T2:.5f}  sharp={per_len_shp:.5f}  T2<=true:{per_len_T2<=per_len_true+1e-12}  sharp<=true:{per_len_shp<=per_len_true+1e-12}")

# bathtub with two slopes: verify min over interval position of int envelope = (sc/2) L^2
for th in [0.1, 0.4, math.pi/4]:
    a_, b_ = math.tan(th), 1/math.tan(th)
    L = 1.7
    ts = np.linspace(0, L, 20001)
    vals = 0.5*(b_*ts**2 + a_*(L-ts)**2)
    print(f"theta={th:.3f}: min two-slope integral={vals.min():.6f}  (sc/2)L^2={math.sin(th)*math.cos(th)/2*L*L:.6f}  tan/4 L^2={a_/4*L*L:.6f}")

print("\n=== Claim 7: column tiling, exact rational arithmetic ===")
for b in [2,3,5,8]:
    k = 2*b*(b-1)
    n_cols = [k+b, k+1-b] + [k]*(k-2)
    widths = [F(k,nj) for nj in n_cols]
    assert sum(widths) == k, (b, sum(widths))
    pieces = sum(n_cols)
    total_side = sum(nj*F(k,nj) for nj in n_cols)
    sumsq = sum(nj*F(k,nj)**2 for nj in n_cols)
    G = k*k - sumsq
    n = k*k+1
    m = F(int(total_side), n)
    V = sumsq - n*m*m
    ident = F(k*k*(1-0)-0, n)  # eps=0
    dev_lo = 1 - F(k, k+b); dev_hi = F(k, k+1-b) - 1
    print(f"b={b} k={k}: pieces={pieces} (k^2+1={k*k+1})  total_side={total_side} (=k^2? {total_side==k*k})  G={G}  V={V}  G+V={G+V}  identity={ident}  match={G+V==ident}")
    print(f"   sides: {float(F(k,k+b)):.6f}, {float(F(k,k+1-b)):.6f}, 1 ; dev_lo={float(dev_lo):.5f} dev_hi={float(dev_hi):.5f}  sqrt(1/(2k))={math.sqrt(1/(2*k)):.5f}  sqrt(2/k)={math.sqrt(2/k):.5f}  n_nonunit={2*k+1}")

print("\n=== Claim 7 extension: |P|=3 perturbed columns -> other admissible k ===")
found = set()
for m1 in range(-25,26):
    for m2 in range(m1,26):
        m3 = 1-m1-m2
        if m3 < m2: continue
        e2 = m1*m2+m1*m3+m2*m3; e3 = m1*m2*m3
        disc = e2*e2 - 3*e3
        if disc < 0: continue
        r = math.isqrt(disc)
        if r*r != disc: continue
        kk = -e2 + r
        if kk >= 3 and all(kk+m >= 1 for m in (m1,m2,m3)) and (m1,m2,m3)!=(0,0,1):
            # verify exactly
            if sum(F(1,kk+m) for m in (m1,m2,m3)) == F(3,kk) and kk-3 >= 0:
                found.add((kk,(m1,m2,m3)))
two_col_ks = {2*b*(b-1) for b in range(2,40)}
new_ks = sorted({kk for kk,_ in found} - two_col_ks)
print("additional exact-tiling k values from 3 perturbed columns (not of form 2b(b-1)):", new_ks[:15])
for kk,ms in sorted(found):
    if kk in new_ks[:5]:
        n_cols = [kk+m for m in ms] + [kk]*(kk-3)
        assert sum(F(kk,nj) for nj in n_cols) == kk and sum(n_cols) == kk*kk+1
        print(f"  k={kk}: m={ms} verified exact tiling with k^2+1={kk*kk+1} pieces, total side k^2")
