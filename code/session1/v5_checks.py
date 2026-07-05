import numpy as np

def C(x): return np.abs(np.cos(x)) + np.abs(np.sin(x))

print("=== 1. Grid checks of the two key inequalities ===")
# E's inequality: D(alpha;theta) = C(alpha)C(theta) + C(theta-alpha) >= 2 C(theta)
# theta = separating-normal angle in [0,pi/2]; alpha = square edge angle in [-pi/4,pi/4]
th = np.linspace(0, np.pi/2, 2001)
al = np.linspace(-np.pi/4, np.pi/4, 2001)
TH, AL = np.meshgrid(th, al, indexing='ij')
E_diff = C(AL)*C(TH) + C(TH-AL) - 2*C(TH)
print("E: min D - 2C(theta) =", E_diff.min())
i,j = np.unravel_index(E_diff.argmin(), E_diff.shape)
print("   at theta=%.4f deg alpha=%.4f deg" % (np.degrees(th[i]), np.degrees(al[j])))
# equality set: should be alpha == 0 mod pi/2 only
mask = E_diff < 1e-9
alphas_at_eq = np.unique(np.round(np.degrees(AL[mask]), 6))
print("   alpha values where equality (deg):", alphas_at_eq[:10], "... count", len(alphas_at_eq))

# LIT inequality: G*F + D >= 2F,  G=C(theta_sq), F=C(alpha_n), D=C(theta_sq - alpha_n)
# theta_sq in [0, pi/2), alpha_n in [0, pi/2]
ths = np.linspace(0, np.pi/2-1e-12, 2001)
aln = np.linspace(0, np.pi/2, 2001)
TS, AN = np.meshgrid(ths, aln, indexing='ij')
L_diff = C(TS)*C(AN) + C(TS-AN) - 2*C(AN)
print("LIT: min GF + D - 2F =", L_diff.min())
# identity check under the notation swap (E square angle <-> LIT theta_sq; E normal <-> LIT alpha_n)
a = np.random.default_rng(0).uniform(-np.pi, np.pi, 100000)
t = np.random.default_rng(1).uniform(-np.pi, np.pi, 100000)
lhsE = C(a)*C(t) + C(t-a) - 2*C(t)          # E with square angle a, normal t
lhsL = C(a)*C(t) + C(a-t) - 2*C(t)          # LIT with theta_sq=a, alpha_n=t
print("max |E_form - LIT_form| over random angles:", np.max(np.abs(lhsE-lhsL)))

# E's intermediate: submultiplicativity C(x)C(y) >= C(x+y)
x = np.random.default_rng(2).uniform(-10,10,10**6); y = np.random.default_rng(3).uniform(-10,10,10**6)
print("submult min C(x)C(y)-C(x+y):", np.min(C(x)*C(y)-C(x+y)))

# LIT concavity endpoints: g(alpha)=(1-cos a)(1-sin a) identity
aa = np.linspace(0,np.pi/2,1001)
g_alpha = 1+np.sin(aa)*np.cos(aa)-np.cos(aa)-np.sin(aa)
print("max |g(alpha)-(1-cos)(1-sin)|:", np.max(np.abs(g_alpha-(1-np.cos(aa))*(1-np.sin(aa)))))

print()
print("=== 2. Random-pairs full-chain test (both proofs' chains) ===")
rng = np.random.default_rng(42)
def mk_corners(z, s, a):
    Ra = np.array([[np.cos(a), -np.sin(a)],[np.sin(a), np.cos(a)]])
    base = np.array([[1,1],[1,-1],[-1,-1],[-1,1]], float)*(s/2)
    return z + base @ Ra.T

def sat_sep_axes(c1, c2, a1, a2):
    """Return list of (u, side) with u unit sep axis s.t. max proj c1 <= min proj c2 after orienting."""
    out = []
    for phi in [a1, a1+np.pi/2, a2, a2+np.pi/2]:
        u = np.array([np.cos(phi), np.sin(phi)])
        p1, p2 = c1@u, c2@u
        if p1.max() <= p2.min() + 1e-12: out.append(u.copy())
        if p2.max() <= p1.min() + 1e-12: out.append(-u.copy())
    return out

n_ok = 0; viol = {k:0 for k in ['sum','chain1','chain2','sep','D1','D2']}
trials = 0
while n_ok < 20000 and trials < 10**7:
    trials += 1
    s1, s2 = rng.uniform(0.05, 0.65, 2)
    a1, a2 = rng.uniform(0, np.pi/2, 2)
    w1, w2 = 0.5*s1*C(a1), 0.5*s2*C(a2)
    if 1-2*w1 <= 0 or 1-2*w2 <= 0: continue
    z1 = rng.uniform(w1, 1-w1, 2); z2 = rng.uniform(w2, 1-w2, 2)
    c1, c2 = mk_corners(z1,s1,a1), mk_corners(z2,s2,a2)
    axes = sat_sep_axes(c1,c2,a1,a2)
    if not axes: continue   # overlapping
    n_ok += 1
    u = axes[0]
    A1, A2 = a1, a2
    C1, C2 = c1.copy(), c2.copy()
    # reflections to first quadrant
    if u[0] < 0:
        C1[:,0] = 1-C1[:,0]; C2[:,0] = 1-C2[:,0]; u = np.array([-u[0], u[1]])
        A1, A2 = np.pi-A1, np.pi-A2
    if u[1] < 0:
        C1[:,1] = 1-C1[:,1]; C2[:,1] = 1-C2[:,1]; u = np.array([u[0], -u[1]])
        A1, A2 = -A1, -A2
    Cth = u[0]+u[1]
    h1 = (C1@u).max(); m2 = (C2@u).min()
    th = np.arctan2(u[1], u[0])
    if h1 > m2 + 1e-9: viol['sep'] += 1
    if s1*Cth > h1 + 1e-9: viol['chain1'] += 1
    if m2 > (1-s2)*Cth + 1e-9: viol['chain2'] += 1
    if s1+s2 > 1 + 1e-9: viol['sum'] += 1
    D1 = C(A1)*Cth + C(th-A1); D2 = C(A2)*Cth + C(th-A2)
    if 0.5*s1*D1 > h1 + 1e-9: viol['D1'] += 1
    if m2 > Cth - 0.5*s2*D2 + 1e-9: viol['D2'] += 1
print("pairs tested:", n_ok, " violations:", viol)

print()
print("=== 3. Route B Claim 8 arithmetic ===")
import math
print("2*sqrt(2)*136 =", 2*math.sqrt(2)*136)
print("2.44*floor(k/8) >= 2.44*(k/8 - 1) = 0.305k - 2.44")
print("=> G >= delta*(0.305k - %.4f)" % (2.44 + 2*math.sqrt(2)*136))
print("report's weakening 0.3k-388 valid iff 0.305k-387.106 >= 0.3k-388 iff 0.005k >= -0.894: always true")
print("0.9*388 =", 0.9*388, " => sin t < 1/(0.27k - 349.2); report used 1/(0.27k-350) (weaker, valid)")
print("sharpened: sin t < 1/(0.2745k - %.2f)" % (0.9*(2.44+2*math.sqrt(2)*136)))
for k in [1273, 1300, 17500]:
    print("  k=%d: 0.27k-350=%.2f, 0.2745k-348.44=%.2f, 4/k vs bound: %.6g vs %.6g"
          % (k, 0.27*k-350, 0.2745*k-348.44, 4/k, 1/(0.27*k-350) if 0.27*k-350>0 else float('inf')))
# check k>=17500 gives 1/(0.27k-350) <= 4/k exactly
k=17500; print("  equality check k=17500:", 1/(0.27*k-350), 4/k)

print()
print("=== 4. Independent MC re-check of Window Theorem (Claim 7) on tilted grid ===")
def window_check(k, t, L=8, npts=400000, seed=7):
    d = 1.0
    delta = 0.9*np.sin(t)
    Rt = np.array([[np.cos(t), -np.sin(t)],[np.sin(t), np.cos(t)]])
    # tilted grid of unit squares: centers at Rt @ (i+0.5, j+0.5), keep those fully in [0,k]^2
    idx = np.arange(-k-2, 2*k+2)
    I, J = np.meshgrid(idx, idx, indexing='ij')
    cen = np.stack([I+0.5, J+0.5], -1).reshape(-1,2) @ Rt.T
    # containment: bounding half-width = 0.5*C(t)
    w = 0.5*C(t)
    keep = (cen[:,0]>=w)&(cen[:,0]<=k-w)&(cen[:,1]>=w)&(cen[:,1]<=k-w)
    cen = cen[keep]
    rng = np.random.default_rng(seed)
    pts = np.column_stack([rng.uniform(0,L,npts), rng.uniform(0,delta,npts)])
    # near-window squares only
    near = cen[(cen[:,0]>-2)&(cen[:,0]<L+2)&(cen[:,1]<2)]
    Rinv = Rt.T
    cov = np.zeros(npts, bool)
    for z in near:
        q = (pts - z) @ Rinv.T
        cov |= (np.abs(q[:,0])<=0.5)&(np.abs(q[:,1])<=0.5)
    gap = (1-cov.mean())*L*delta
    bound = delta*(L/2 - 1.56)
    return gap, bound
for t in [0.05, 0.2, 0.775]:
    g,b = window_check(30, t)
    print("  t=%.3f: MC gap in window = %.4f, theorem bound = %.4f, holds: %s" % (t,g,b,g>=b))

print()
print("=== 5. Sector Lemma (Claim 3) MC spot check ===")
# S1 vertex at origin, tilted alpha; S2 edge through origin (edge-interior contact), axis-parallel below
rng = np.random.default_rng(11)
worst = np.inf
for trial in range(300):
    alpha = rng.uniform(0.02, np.pi/4)
    d1, d2 = rng.uniform(0.5, 1.5, 2)
    # S2: axis-parallel square below y=0 with top edge on y=0, origin interior to top edge
    off = rng.uniform(0.2*d2, 0.8*d2)
    z2 = np.array([off - d2/2, -d2/2])
    # S1: vertex at origin, edges at angles alpha and alpha+pi/2 (opens upward-ish), center along bisector
    bis = alpha + np.pi/4
    z1 = (d1/np.sqrt(2))*np.array([np.cos(bis), np.sin(bis)])
    r = rng.uniform(0.05, 0.3)
    pts = rng.uniform(-r, r, (20000,2)); pts = pts[np.linalg.norm(pts,axis=1)<=r]
    def insq(p, z, a, d):
        Ra = np.array([[np.cos(a), np.sin(a)],[-np.sin(a), np.cos(a)]])
        q = (p-z)@Ra.T
        return (np.abs(q[:,0])<=d/2)&(np.abs(q[:,1])<=d/2)
    cov = insq(pts, z1, alpha, d1) | insq(pts, z2, 0, d2)
    area_unc = (1-cov.mean())*np.pi*r*r
    ratio = area_unc/(alpha*r*r)
    worst = min(worst, ratio)
print("  min uncovered/(alpha r^2) over 300 configs:", worst, "(should be >= ~1)")
