import numpy as np
from scipy.optimize import linprog

print("=== 1) Largest axis-parallel square inscribed in a theta-tilted square of side d (LP) ===")
# S = rotate([0,d]^2, th) + (d sin th, 0). Axis-parallel square corners (a,b),(a+s,b),(a,b+s),(a+s,b+s).
# In S-frame: u = R_{-th}(P - (d st,0)) must be in [0,d]^2 -> 4 linear ineqs per corner.
# maximize s.
for d in (1.0, 0.9, 0.7):
    for thd in (1, 5, 15, 30, 45):
        th = np.deg2rad(thd); ct, st = np.cos(th), np.sin(th)
        # variables (a,b,s)
        A_ub, b_ub = [], []
        for (ea, eb) in [(0,0),(1,0),(0,1),(1,1)]:
            # corner P = (a+ea*s, b+eb*s); ux = ct*(Px - d st) + st*Py ; uy = -st*(Px - d st) + ct*Py
            # ux >= 0:  -ct*a - st*b - (ct*ea+st*eb)*s <= -ct*d*st
            A_ub.append([-ct, -st, -(ct*ea+st*eb)]); b_ub.append(-ct*d*st)
            # ux <= d:   ct*a + st*b + (ct*ea+st*eb)*s <= d + ct*d*st
            A_ub.append([ct, st, (ct*ea+st*eb)]); b_ub.append(d + ct*d*st)
            # uy >= 0:  st*a - ct*b + (st*ea-ct*eb)*s <= -st*d*st  ... uy = -st*Px + ct*Py + st*d*st
            A_ub.append([st, -ct, (st*ea-ct*eb)]); b_ub.append(st*d*st)
            # uy <= d:  -st*a + ct*b + (-st*ea+ct*eb)*s <= d - st*d*st
            A_ub.append([-st, ct, (-st*ea+ct*eb)]); b_ub.append(d - st*d*st)
        r = linprog(c=[0,0,-1], A_ub=A_ub, b_ub=b_ub, bounds=[(None,None),(None,None),(0,None)])
        smax = -r.fun
        pred = d/(ct+st)
        print(f"  d={d} th={thd:2d}deg: LP max s = {smax:.6f}   d/(cos+sin) = {pred:.6f}   diff={smax-pred:+.2e}")

print()
print("=== 2) small-theta slope of E[D+]: formula/theta -> 2d^2 ===")
for d in (0.6, 0.85, 1.0):
    for thd in (0.05, 0.2, 1.0):
        th = np.deg2rad(thd); w = d*(np.cos(th)+np.sin(th))
        f = 2*w - 1 - d*d + max(0.0,1-w)**2
        print(f"  d={d} th={thd}deg: E[D+]/theta = {f/th:.5f}  (2d^2 = {2*d*d})")

print()
print("=== 3) Markov/pigeonhole bound |A| >= t/(t+M): random synthetic instances ===")
rng = np.random.default_rng(1)
bad = 0
for trial in range(2000):
    M = rng.integers(2, 12)
    N = rng.integers(1, 30)   # plays role of k^2
    # random widths w_i >= 0 with sum > N
    w = rng.uniform(0, 3, size=M); w *= (N + rng.uniform(0.01, 2)) / w.sum()
    t = w.sum() - N
    if t <= 0: continue
    off = rng.uniform(0, 1, size=M)
    xs = (np.arange(200000)+0.5)/200000
    S = np.zeros_like(xs)
    for i in range(M):
        # p_i(x) = # integers in [off_i - x, off_i + w_i - x]
        S += np.floor(off[i] + w[i] - xs) - np.ceil(off[i] - xs) + 1
    measA = np.mean(S >= N+1)
    if measA < t/(t+M) - 1e-4:
        bad += 1
        print(f"  VIOLATION trial {trial}: |A|={measA:.5f} < t/(t+M)={t/(t+M):.5f} (t={t:.3f}, M={M})")
print(f"  trials done; violations: {bad}")

print()
print("=== 4) Claim 10 final algebra: t<= sqrt(D)*M/(1-sqrt(D)) <= 2M sqrt(D) for D<=1/4 ===")
for Dl in (1e-6, 0.01, 0.1, 0.25):
    print(f"  Delta={Dl}: M-multiplier sqrt(D)/(1-sqrt(D)) = {np.sqrt(Dl)/(1-np.sqrt(Dl)):.6f}  vs 2sqrt(D) = {2*np.sqrt(Dl):.6f}")

print()
print("=== 5) 'beats Cauchy-Schwarz' side-claim: need 2(k^2+2)sqrt(D) < k*sqrt(k^2+1)-k^2 ===")
for k in (1,2,3,5,10):
    R = (k*np.sqrt(k*k+1)-k*k)/(2*(k*k+2))   # threshold on sqrt(Delta)
    # theta <= 2^-7 k^-6 gives sqrt(Delta) <= sqrt(2k^2 * 2^-7 k^-6) = 2^-3 k^-2
    claimed = 2**-3 * k**-2
    print(f"  k={k}: sqrt(D) threshold={R:.6f}; claimed-sufficient 1/(8k^2)={claimed:.6f}; OK={claimed < R}")

print()
print("=== 6) Claim 6(iii)/NOTES identities symbolically-numerically ===")
rng = np.random.default_rng(2)
m = 0.0
for _ in range(100000):
    d = rng.uniform(0.05, 1.6); th = rng.uniform(1e-4, np.pi/4)
    u1 = np.cos(th)+np.sin(th); w = d*u1; sg = u1-1
    m = max(m, abs((w-1)**2 - d*sg*(d+w-2) - (1-d)**2))
    m = max(m, abs(2*(w-d) - ((w*w-d*d) - (w-1)**2) - (1-d)**2))
print(f"  max abs residual over 1e5 random (d,theta): {m:.2e}")
