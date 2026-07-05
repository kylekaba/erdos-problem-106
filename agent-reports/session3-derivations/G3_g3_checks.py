"""G3 BRIDGE (I) machine checks.
A. elementary tan inequalities used by Lemma E / E-narrow / E-wall
B. constant assembly (J counts, lambda dichotomy) for E-wall and E-narrow
C. +-theta checkerboard: E-narrow hypotheses + payment bound holds numerically
D. strip multiplicity <= 20 sanity
"""
import numpy as np

rng = np.random.default_rng(0)
OK = True
def chk(name, cond, extra=""):
    global OK
    s = "PASS" if cond else "FAIL"
    if not cond: OK = False
    print(f"[{s}] {name} {extra}")

# ---------- A. elementary inequalities ----------
x = np.linspace(0, np.pi/4 - 1e-9, 200001)
chk("tan(2x) >= 2 tan x on [0,pi/4)",
    np.all(np.tan(np.minimum(2*x, np.pi/2 - 1e-9)) + 1e-15 >= 2*np.tan(x)))
a = rng.uniform(0, np.pi/4, 500000); b = rng.uniform(0, np.pi/4, 500000)
a, b = np.maximum(a, b), np.minimum(a, b)
chk("tan a - tan b >= a - b (0<=b<=a<=pi/4)", np.all(np.tan(a)-np.tan(b) >= (a-b)-1e-12))
t = np.linspace(1e-6, 1.0, 100001)
chk("2/tau - tau >= 1 on (0,1]", np.all(2/t - t >= 1 - 1e-12))

# ---------- B. constant assembly ----------
eta = 1/20.0; area_min = (1-eta)**2         # 0.9025
diam = np.sqrt(2)*(1+eta)                    # <=1.485 ; use 1.49
D = 1.49

def const_wall():
    # E-wall: full window [0,Xe], h=1/4, J from verifier's corrected count +1 (floor crest)
    h = 0.25
    worst = 0.0
    for Xe in np.linspace(0.63, 1.06, 44):
        # verifier region: (Xe+2.98)*3.23 + 2*1.49*2.98 ; +1 crest for the floor
        J = ((Xe + 2*D)*(h + D + D*1.0) + 2*D*2*D)/area_min + 1.0
        best = 0.0
        for lam in np.linspace(0.001, 0.2, 400):
            b2 = ((1-lam)*Xe)**2/(4*J)          # coefficient of min(tau1, 1/3)
            b1 = h*lam*Xe                        # absolute area
            c = min(b2, b1/(1/3.0))              # need b1 >= coef*(1/3)
            best = max(best, c)
        worst = max(worst, 1/best) if worst else 1/best
        # track max over Xe of 1/best
    return worst

def const_narrow(rho_arc=0.22, hp=0.125, alpha_max=np.pi/4):
    # arclength trim rho_arc from each end of e; d* in [0.95,1.05]; mismatch alpha
    worst = 0.0
    for al in np.linspace(0.0, alpha_max, 60):
        for ds in np.linspace(0.95, 1.05, 11):
            Xp = (ds - 2*rho_arc)*np.cos(al)      # window length (x-extent of e')
            rx = rho_arc*np.cos(al)               # x-trim (poke zones width D-rx)
            tmax = min(np.tan(alpha_max), 1.0)
            band = (Xp + 2*D)*(hp + D + D*tmax)
            poke = 2*max(D - rx, 0)*2*D
            J = (band + poke)/area_min
            assert 2*hp/Xp >= 1/3 - 1e-12, (al, ds, Xp)   # tau2 >= min(tau1,1/3)
            best = 0.0
            for lam in np.linspace(0.001, 0.3, 600):
                b2 = ((1-lam)*Xp)**2/(4*J)
                b1 = hp*lam*Xp
                c = min(b2, b1/(1/3.0))
                best = max(best, c)
            worst = max(worst, 1/best)
    return worst

Cw = const_wall()
Cn_all = const_narrow()
Cn_small = const_narrow(alpha_max=0.30)
print(f"  E-wall uniform constant: 1/{Cw:.1f}  (claim 1/252)")
print(f"  E-narrow uniform constant (rho'=0.22,h'=1/8): 1/{Cn_all:.1f} (claim 1/700)")
print(f"  E-narrow small-mismatch (alpha<=0.30): 1/{Cn_small:.1f} (claim 1/400)")
chk("E-wall const <= 252", Cw <= 252)
chk("E-narrow uniform const <= 700", Cn_all <= 700)
chk("E-narrow small-mismatch const <= 400", Cn_small <= 400)

# ---------- C. checkerboard test ----------
def square(cx, cy, d, th):
    c, s = np.cos(th), np.sin(th)
    R = np.array([[c, -s], [s, c]])
    P = np.array([[-d/2, -d/2], [d/2, -d/2], [d/2, d/2], [-d/2, d/2]])
    return P @ R.T + np.array([cx, cy])

def sat_disjoint(A, B):
    # separating axis for convex polygons; True if interiors disjoint
    for poly, other in ((A, B), (B, A)):
        for i in range(4):
            edge = poly[(i+1) % 4] - poly[i]
            n = np.array([-edge[1], edge[0]])
            pa = poly @ n; pb = other @ n
            if pa.max() <= pb.min() + 1e-12 or pb.max() <= pa.min() + 1e-12:
                return True
    return False

def inside_any(pts, polys):
    res = np.zeros(len(pts), dtype=bool)
    for P in polys:
        m = np.ones(len(pts), dtype=bool)
        for i in range(4):
            e = P[(i+1) % 4] - P[i]
            n = np.array([-e[1], e[0]])   # inward for CCW
            m &= ((pts - P[i]) @ n) >= -1e-12
        res |= m
    return res

th = 0.12
u1 = np.cos(th) + np.sin(th)
d = 1.0/u1 * 0.999          # rotated square fits unit cell with hair clearance
polys, oris = [], []
n = 6
for i in range(n):
    for j in range(n):
        sgn = 1 if (i+j) % 2 == 0 else -1
        polys.append(square(i+0.5, j+0.5, d, sgn*th)); oris.append(sgn*th)
bad = 0
for i in range(len(polys)):
    for j in range(i+1, len(polys)):
        if not sat_disjoint(polys[i], polys[j]): bad += 1
chk("checkerboard SAT-disjoint", bad == 0, f"(d={d:.4f}, {n}x{n})")

# pick interior square S at (2.5,2.5) with +th; right edge e; gamma-frame = frame of
# facing occupant W (-th). Work directly: strip R'_e = pts within h'=1/8 of middle
# sub-segment of e (trim rho=0.2), outward (right) side.
idxS = None
for m_, (i, j) in enumerate([(i, j) for i in range(n) for j in range(n)]):
    if (i, j) == (2, 2): idxS = m_
S = polys[idxS]; bS = oris[idxS]
# right edge of S: two vertices with largest x
order = np.argsort(S[:, 0]); e_v = S[order[2:]]  # two rightmost vertices
e0, e1 = e_v[np.argsort(e_v[:, 1])]              # bottom, top of right edge
edir = (e1 - e0)/np.linalg.norm(e1 - e0)
L = np.linalg.norm(e1 - e0)
rho, hp = 0.22, 0.125
a0 = e0 + rho*edir; a1 = e1 - rho*edir           # arclength trim
nrm = np.array([edir[1], -edir[0]])              # outward (right) normal: check sign
if nrm[0] < 0: nrm = -nrm
# occupants of R'_e: squares (other than S) with a vertex-or-edge point within hp of segment a0a1 on outward side
def seg_dist(pts, p, q):
    v = q - p; vv = v @ v
    tt = np.clip(((pts - p) @ v)/vv, 0, 1)
    proj = p + tt[:, None]*v
    return np.linalg.norm(pts - proj, axis=1)

occ = []
grid_t = np.linspace(0, 1, 60)
for m_ in range(len(polys)):
    if m_ == idxS: continue
    P = polys[m_]
    # sample boundary densely
    bpts = np.vstack([P[i][None]*(1-grid_t)[:, None] + P[(i+1) % 4][None]*grid_t[:, None] for i in range(4)])
    dists = seg_dist(bpts, a0, a1)
    outward = ((bpts - a0) @ nrm) > 0
    if np.any((dists <= hp) & outward):
        occ.append(m_)
print(f"  occupants of narrow strip: {[(m_, round(oris[m_],3)) for m_ in occ]}")
chk("checkerboard: single facing occupant, orientation -th",
    len(occ) == 1 and abs(oris[occ[0]] + th) < 1e-9)

# uncovered area in R'_e vs bound (1/360)*min(tan(2 th), 1/3)  [alpha=2th<=0.3 regime]
M = 400000
u = rng.uniform(0, 1, M); v = rng.uniform(0, hp, M)
pts = a0[None] + u[:, None]*(a1 - a0)[None] + v[:, None]*nrm[None]
area_strip = np.linalg.norm(a1 - a0)*hp
cov = inside_any(pts, [polys[m_] for m_ in occ] + [S])
unc = area_strip*np.mean(~cov)
bound = (1/400.0)*min(np.tan(2*th), 1/3.0)   # alpha = 2*0.12 = 0.24 <= 0.30 regime
print(f"  uncovered in R'_e = {unc:.5f}, bound = {bound:.5f}, ratio = {unc/bound:.1f}")
chk("checkerboard: E-narrow payment bound holds", unc >= bound)

# ---------- D. multiplicity ----------
h = 0.25
pts = rng.uniform(0.5, n - 0.5, size=(20000, 2))
gap = ~inside_any(pts, polys)
gp = pts[gap]
counts = np.zeros(len(gp))
for m_, P in enumerate(polys):
    for i in range(4):
        p, q = P[i], P[(i+1) % 4]
        e = q - p; nn = np.array([e[1], -e[0]]); nn = nn/np.linalg.norm(nn)
        ctr = P.mean(axis=0)
        if (ctr - p) @ nn > 0: nn = -nn      # outward
        dd = seg_dist(gp, p, q)
        out = ((gp - p) @ nn) > 0
        counts += ((dd <= h) & out).astype(float)
print(f"  gap samples: {len(gp)}, max strip multiplicity = {counts.max():.0f}")
chk("multiplicity <= 20", counts.max() <= 20)

print("\nALL PASS" if OK else "\nSOME CHECKS FAILED")
