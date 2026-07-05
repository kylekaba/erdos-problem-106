"""Independent checks:
(A) F3 Claim 2 comparison identity on a BIG tilted square (side 1.2 > 1, diam > 1,
    crossing cell boundaries) -- outside the families the author tested.
(B) F3 Claim 4 tilt-neutrality |pi(S)| = d^2 for diam < 1 via direct fold measure.
(C) FCMB refutation arithmetic (deficient column family), exact combinatorial check k=3,4.
"""
import sys, numpy as np
sys.path.insert(0, "/private/tmp/claude-501/-Users-kylekabasares-Desktop-erdos-106/6b0597a9-48bd-4e8c-a957-7fc4a05f26d8/scratchpad/session2/F3")
from rig import stats, compare_inscribed, validate

print("=== (A) Claim 2 on big tilted square, k=2 ===")
t = 0.25
sq = [
    (1.0, 1.0, 1.2, t),          # big tilted, crosses all four cells
    (0.22, 0.22, 0.40, 0.0),
    (1.78, 0.22, 0.40, 0.0),
    (0.22, 1.78, 0.40, 0.0),
    (1.78, 1.78, 0.40, 0.0),
]
assert validate(sq), "invalid packing"
r = compare_inscribed(sq, 0, M=700)
print(f" subset_viol(|Av'\\Av|) = {r['subset_viol']:.6f}  (must be 0)")
print(f" |Av\\Av'| = {r['diff']:.5f}  vs |pi(R)\\pi(G)| = {r['piRnG']:.5f}  (must match)")
c = np.cos(t)+np.sin(t); d = 1.2
print(f" exchange identity: ds+areaR = {r['ds']+r['areaR']:.6f}  vs 2d(1-1/c) = {2*d*(1-1/c):.6f}")
print(f" over-budget measure (C>N): {r['over'].mean():.6f} (must be 0)")

print("\n=== (B) Claim 4: |pi(S)|=d^2 tilt-invariance, direct fold measure ===")
M = 900
idx = (np.arange(M)+0.5)/M
PX, PY = np.meshgrid(idx, idx, indexing='ij')
for d in [0.5, 0.69]:
    vals = []
    for t in [0.0, 0.2, 0.5, np.pi/4]:
        ct, st = np.cos(t), np.sin(t)
        hit = np.zeros((M, M), bool)
        for i in range(-1, 2):
            for j in range(-1, 2):
                x = PX+i-0.5; y = PY+j-0.5   # square centered (.5,.5)
                u, v = ct*x+st*y, -st*x+ct*y
                hit |= (np.abs(u) <= d/2) & (np.abs(v) <= d/2)
        vals.append(hit.mean())
    print(f" d={d}: |pi(S)| over tilts = {['%.5f'%v for v in vals]}  d^2={d*d:.5f}")

print("\n=== (C) deficient-column family, exact, k=3,4 ===")
for k in [3, 4]:
    N = k*k
    a = k/(k+1)
    s = (k+1)*(1-a)**2
    g = N - (k*(k-1)*1 + (k+1)*a*a)
    # |Av| exact: units always capture k(k-1); column [0,a]x[0,k] tiled by k+1 squares
    # captures all k lattice pts of column iff x-phase in (0,a): measure a
    Av = a
    print(f" k={k}: |Av|={Av:.4f}  s={s:.4f}  FCMB |Av|<=s: {Av<=s}   g+s={g+s:.6f} (conjecture needs >=1)")
    # numeric verification of |Av| for k=3 via brute shift grid
    if k == 3:
        M2 = 400
        idx2 = (np.arange(M2)+0.5)/M2
        PXs, PYs = np.meshgrid(idx2, idx2, indexing='ij')
        C = np.full((M2, M2), k*(k-1), dtype=int)
        # column squares: [0,a] x [m*a,(m+1)*a], m=0..k
        for m in range(k+1):
            for i in range(k):
                for j in range(k):
                    px = PXs + i; py = PYs + j
                    inside = (px > 0) & (px < a) & (py > m*a) & (py < (m+1)*a) & (px < k) & (py < k)
                    C += inside.astype(int)
        av = (C == N).mean(); over = (C > N).mean()
        print(f"   numeric k=3: |Av|={av:.4f} (pred {a:.4f}), over-budget={over:.4f}")
