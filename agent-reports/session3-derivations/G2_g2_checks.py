"""G2 master-assembly machine checks.

Checks every algebraic identity and every arithmetic constant used in the
G2 conditional assembly (G2_MASTER_ASSEMBLY.md). Pure algebra / numeric scans;
packing-level numerics were already done by SQUEEZE/RIGIDITY/verifiers.
"""
import numpy as np

rng = np.random.default_rng(106)
FAIL = []

def check(name, ok, detail=""):
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name} {detail}")
    if not ok:
        FAIL.append(name)

# ---------------------------------------------------------------- 1
# Identity I1:  (1-w)^2 = (1-d)^2 - d*sigma*(2-d-w),  w = d*u1, sigma = u1-1
d = rng.uniform(0.05, 2.5, 200000)
th = rng.uniform(0, np.pi/4, 200000)
u1 = np.cos(th) + np.sin(th)
sig = u1 - 1
w = d*u1
lhs = (1-w)**2
rhs = (1-d)**2 - d*sig*(2-d-w)
check("I1 (1-w)^2 identity (all d,theta)", np.max(np.abs(lhs-rhs)) < 1e-12,
      f"max err {np.max(np.abs(lhs-rhs)):.2e}")

# ---------------------------------------------------------------- 2
# Bracket identity: s - sum_short (1-w)^2 = sum_short m + sum_long (1-d)^2
# on random populations
for trial in range(200):
    n = rng.integers(5, 60)
    dd = rng.uniform(0.5, 1.5, n)
    tt = rng.uniform(0, np.pi/4, n)
    uu = np.cos(tt)+np.sin(tt); ss = uu-1; ww = dd*uu
    short = ww < 1
    s_tot = np.sum((1-dd)**2)
    m = dd*ss*(2-dd-ww)
    lhs = s_tot - np.sum((1-ww[short])**2)
    rhs = np.sum(m[short]) + np.sum((1-dd[~short])**2)
    if abs(lhs-rhs) > 1e-10:
        check("I2 bracket identity", False, f"trial {trial} err {abs(lhs-rhs)}"); break
else:
    check("I2 bracket identity s - sum_short(1-w)^2 = sum_short m + sum_long(1-d)^2", True)

# margins nonneg for shorts: 2-d-w>0 when w<1 (since d<=w)
check("I2b short margins m_i >= 0", np.all(m[short] >= -1e-15))

# ---------------------------------------------------------------- 3
# beta = 1 - eps + b0 - Gamma  (with N+1 squares, eps = sum d - N)
for trial in range(200):
    k = rng.integers(2, 9); N = k*k; n = N+1
    dd = rng.uniform(0.6, 1.4, n)
    tt = rng.uniform(0, np.pi/4, n)
    beta = np.sum(np.clip(1-dd/np.cos(tt), 0, None))
    eps = np.sum(dd)-N
    b0 = np.sum(np.clip(dd-1, 0, None))
    Gam = np.sum(np.clip(1-dd,0,None) - np.clip(1-dd/np.cos(tt),0,None))
    if abs(beta - (1-eps+b0-Gam)) > 1e-9:
        check("I3 beta identity", False, f"err {abs(beta-(1-eps+b0-Gam))}"); break
else:
    check("I3 beta = 1 - eps + b0 - Gamma", True)
check("I3b Gamma terms >= 0 pointwise",
      bool(np.all(np.clip(1-dd,0,None) >= np.clip(1-dd/np.cos(tt),0,None) - 1e-15)))

# ---------------------------------------------------------------- 4
# Pointwise chain sigma <= sin th <= th ; th <= (pi/4)/sin(pi/4) * sin th on [0,pi/4]
th = np.linspace(0, np.pi/4, 100001)
check("I4a sigma <= sin(th)", np.all(np.cos(th)+np.sin(th)-1 <= np.sin(th)+1e-15))
check("I4b sin(th) <= th", np.all(np.sin(th) <= th+1e-15))
c_fold = (np.pi/4)/np.sin(np.pi/4)
check("I4c th <= 1.1108*sin(th) on [0,pi/4]",
      np.all(th <= c_fold*np.sin(th)+1e-12), f"const {c_fold:.6f}")
# (1 - d sec th)_+ <= (1-d)_+ pointwise
dd = rng.uniform(0.0, 2.0, 100000); tt = rng.uniform(0, np.pi/4, 100000)
check("I4d (1-d sec)_+ <= (1-d)_+", np.all(np.clip(1-dd/np.cos(tt),0,None) <= np.clip(1-dd,0,None)+1e-15))
# w - 1 <= (d-1)_+ + d*sigma
uu = np.cos(tt)+np.sin(tt)
check("I4e (w-1)_+ <= (d-1)_+ + d*sigma",
      np.all(np.clip(dd*uu-1,0,None) <= np.clip(dd-1,0,None)+dd*(uu-1)+1e-12))

# ---------------------------------------------------------------- 5
# S3(II) chain end-to-end algebra: given 1-g <= Sum_short(1-w)^2 + UV  (S2+Markov),
# structure identity 1-g = s + 2eps  =>  UV >= 2eps + sum_short m + sum_long (1-d)^2.
for trial in range(500):
    k = rng.integers(2, 7); N = k*k; n = N+1
    dd = rng.uniform(0.8, 1.2, n); tt = rng.uniform(0, 0.3, n)
    uu = np.cos(tt)+np.sin(tt); ww = dd*uu; sg = uu-1
    eps = np.sum(dd)-N; g = N - np.sum(dd**2); s = np.sum((1-dd)**2)
    # structure identity
    if abs((g+s) - (1-2*eps)) > 1e-9:
        check("I5 structure identity", False); break
    short = ww < 1
    m = dd*sg*(2-dd-ww)
    # pretend UV is exactly at the S2 bound: UV = (1-g) - sum_short (1-w)^2
    UV = (1-g) - np.sum((1-ww[short])**2)
    target = 2*eps + np.sum(m[short]) + np.sum((1-dd[~short])**2)
    if UV < target - 1e-9:
        check("I5 S3(II) rearrangement", False, f"UV {UV} < {target}"); break
else:
    check("I5 structure identity g+s=1-2eps AND S3(II) rearrangement exact", True)

# ---------------------------------------------------------------- 6
# Raw-mass fact: R := 4*sum d sin th + 2*sum(w-1)_+ >= 4*sum d*sigma >= 4*eps
# whenever T4 (eps <= sum d sigma / u1) holds. Check 4 d sin th >= 4 d sigma pointwise
check("I6 raw arc mass >= 4*tilt-sigma mass (pointwise sin>=sigma)", True)  # = I4a
# and T4 chain: sum d sigma/u1 <= sum d sigma
check("I6b d*sigma/u1 <= d*sigma", bool(np.all(dd*sg/uu <= dd*sg + 1e-15)))

# ---------------------------------------------------------------- 7
# Vernier Cauchy-Schwarz: k+1 line squares, sum_L (1-d_j) >= 1  =>  s >= 1/(k+1)
for trial in range(2000):
    k = rng.integers(2, 60)
    a = rng.uniform(-0.2, 0.6, k+1)         # deficits 1-d_j, may be negative
    tot = np.sum(a)
    if tot < 1: a = a + (1-tot)/(k+1)       # normalize to sum exactly 1
    if np.sum(a**2) < 1/(k+1) - 1e-12:
        check("I7 vernier CS", False); break
else:
    check("I7 vernier line => s >= 1/(k+1)   (Cauchy-Schwarz)", True)

# ---------------------------------------------------------------- 8
# Steep charge ratio: sup over th in [2*t0, pi/4], t0 <= th/2, of
#   ratio(th) = 4*(1+sqrt(2c))*sin(th) / ( min(tan th - tan t0, 1/3)/240 )
# with worst case tan t0 = tan(th)/2  => tan th - tan t0 >= tan(th)/2.
c = 2e-4  # generous
th = np.linspace(1e-6, np.pi/4, 400000)
num = 4*(1+np.sqrt(2*c))*np.sin(th)
den = np.minimum(np.tan(th)/2, 1.0/3.0)/240.0
ratio = num/den
check("I8 steep charge ratio sup <= 2200 (before overlap mult.)",
      np.max(ratio) <= 2200, f"sup = {np.max(ratio):.1f} at th={th[np.argmax(ratio)]:.4f}")
C_X1 = 12*np.max(ratio)   # overlap multiplicity 12
print(f"    C_X1 = 12 * sup = {C_X1:.0f}")

# ---------------------------------------------------------------- 9
# c0 arithmetic (instantiated): need  2*C_X1*c + C_X2*(sqrt(c)+1/k) < 1 - 2c
C_X2 = 30.0
def margin(c, k, C1):
    return (1 - 2*c) - (2*C1*c + C_X2*(np.sqrt(c) + 1.0/k))
C1 = 26400.0
for (c0, k0) in [(1e-5, 300), (1.4e-5, 300), (1e-5, 1000)]:
    m0 = margin(c0, k0, C1)
    print(f"    c={c0:g}, k={k0}: margin = {m0:+.4f}")
check("I9 c0 = 1e-5, K0 = 300 closes with margin >= 0.25",
      margin(1e-5, 300, C1) >= 0.25, f"margin {margin(1e-5,300,C1):.4f}")

# ---------------------------------------------------------------- 10
# Whisper budget: t0 = 1/(4k^2): whisper tilt mass <= (N+eps)*t0 ~ 1/4 < eps
for k in [20, 100, 1000]:
    N = k*k; eps = 0.4975
    wm = (N+eps)/(4*k*k)
    ok = wm < eps
    check(f"I10 whisper mass bound k={k}", ok, f"{wm:.4f} < {eps}")

# ---------------------------------------------------------------- 11
# T4 whisper kill threshold: all th <= t0, t0 < eps/(N+eps) => sum d th < eps
k = 50; N = k*k; eps = 0.4975
t0 = eps/(N+eps)*0.999
check("I11 T4 kills literal whisper t0 < eps/(N+eps)", (N+eps)*t0 < eps)

# ---------------------------------------------------------------- 12
# Theorem W phantom arithmetic recheck (c=1/400, k=20): 4*sqrt(2c)+1/k+13/400
val = 4*np.sqrt(2/400)+1/20+13/400
check("I12 W phantom-kill arithmetic", abs(val-0.36534) < 1e-4 and val < 0.4975,
      f"{val:.5f} < 0.4975")

# ---------------------------------------------------------------- 13
# 45-degree single-square attack on instantiated constants:
# gap charge >= 4 edges * (1/720)/12 = 4.63e-4 >= 2c for c <= 2.3e-4; our c0=1e-5.
charge = 4*(1/720)/12
check("I13 45-deg single-square attack absorbed", charge > 2*1e-5,
      f"charge {charge:.2e} vs 2c0 {2e-5:.1e} (x{charge/2e-5:.0f} margin)")

# ---------------------------------------------------------------- 14
# enemy side window: (1-d)^2 <= s < 2c  =>  |d-1| < sqrt(2c); w<2 check for V-arcs
c = 2.3e-4
dmax = 1+np.sqrt(2*c)
check("I14 w_max = sqrt(2)*d_max < 2 (V-arcs are arcs, not full circle)",
      np.sqrt(2)*dmax < 2, f"w_max={np.sqrt(2)*dmax:.4f}")

print()
print("ALL PASS" if not FAIL else f"FAILURES: {FAIL}")
