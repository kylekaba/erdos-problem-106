"""F6: numerical verification that FCMB is FALSE.

FCMB (report section 7A): for every packing of n=k^2+1 squares in [0,k]^2,
  |Av| := |{p in [0,1)^2 : C(p) = N}| <= s := sum_i (1-d_i)^2,  N=k^2.

Counterexample family ("deficient column", axis-parallel):
  (k-1) columns of k unit squares + one 1 x k strip holding (k+1) squares of
  side k/(k+1), flush left; empty strip of width 1/(k+1), height k remains.
Analytic prediction: |Av| = k/(k+1), s = 1/(k+1) -> violation for k>=2.
"""
import numpy as np

def count_AP(x, y, d, PX, PY):
    # number of lattice points of Z^2+p in [x,x+d]x[y,y+d]
    nx = np.floor(x + d - PX) - np.ceil(x - PX) + 1
    ny = np.floor(y + d - PY) - np.ceil(y - PY) + 1
    return np.maximum(nx, 0) * np.maximum(ny, 0)

def count_tilted(cx, cy, half, th, PX, PY, k):
    # lattice points of Z^2+p inside square center (cx,cy), half-side, angle th
    tot = np.zeros_like(PX)
    c, s = np.cos(th), np.sin(th)
    for a in range(0, k + 1):
        for b in range(0, k + 1):
            qx = PX + a - cx
            qy = PY + b - cy
            u = c * qx + s * qy
            v = -s * qx + c * qy
            tot += ((np.abs(u) <= half) & (np.abs(v) <= half)).astype(float)
    return tot

def measure_Av(squares, tilted, k, M=1200):
    N = k * k
    off = (np.sqrt(5) - 2)  # irrational-ish offset to dodge boundaries
    px = (np.arange(M) + 0.5 + off * 0.1) / M
    py = (np.arange(M) + 0.5 + off * 0.05) / M
    PX, PY = np.meshgrid(px, py, indexing="ij")
    C = np.zeros_like(PX)
    for (x, y, d) in squares:
        C += count_AP(x, y, d, PX, PY)
    for (cx, cy, half, th) in tilted:
        C += count_tilted(cx, cy, half, th, PX, PY, k)
    assert C.max() <= N + 1e-9, f"budget violated: max C = {C.max()}"
    Av = float(np.mean(C >= N - 1e-9))
    s = sum((1 - d) ** 2 for (_, _, d) in squares) + sum(
        (1 - 2 * h) ** 2 for (_, _, h, _) in tilted)
    Sig = sum(d for (_, _, d) in squares) + sum(2 * h for (_, _, h, _) in tilted)
    return Av, s, Sig, float(C.max()), float(C.mean())

def deficient_column(k, shrink_units=0.0):
    du = 1.0 - shrink_units
    sq = []
    for i in range(k - 1):
        for j in range(k):
            sq.append((i, j, du))
    d = k / (k + 1)
    for j in range(k + 1):
        sq.append((k - 1, j * d, d))
    return sq

for k in (2, 3):
    sq = deficient_column(k)
    Av, s, Sig, Cmax, Cmean = measure_Av(sq, [], k)
    print(f"k={k} deficient column: n={len(sq)}  Sigma={Sig:.6f}  N={k*k}  "
          f"|Av|={Av:.4f}  s={s:.4f}  pred |Av|={k/(k+1):.4f} pred s={1/(k+1):.4f}  "
          f"VIOLATION={Av > s}  maxC={Cmax}  E[C]={Cmean:.4f}")

# control: split-cell config at a=0.37 must be TIGHT (|Av| = s)
k = 2
a, b = 0.37, 0.63
sq = [(0, 0, 1), (0, 1, 1), (1, 0, 1), (1, 1, a), (1 + 0, 1 + a, b)]
# fix: place a,b stacked in cell [1,2]x[1,2]: a at (1,1), b at (1,1+a)
Av, s, Sig, Cmax, Cmean = measure_Av(sq, [], k)
print(f"k=2 split-cell a=0.37: |Av|={Av:.4f}  s={s:.4f}  (should be equal, "
      f"a^2+b^2={a*a+b*b:.4f})")

# robustness 1: shrink the unit squares by 0.02 (g+s = 1 + delta, delta>0)
sq = deficient_column(2, shrink_units=0.02)
Av, s, Sig, Cmax, Cmean = measure_Av(sq, [], 2)
print(f"k=2 shrunk units (0.98): Sigma={Sig:.4f}  |Av|={Av:.4f}  s={s:.4f}  "
      f"VIOLATION={Av > s}")

# robustness 2: tilted variant - replace middle 2/3-square by side-0.6 square
# tilted 0.1 rad about the cell center (4/3, 1); stays inside [1,5/3]x[2/3,4/3]
k = 2
d = 2 / 3
sq = [(0, 0, 1), (0, 1, 1), (1, 0, d), (1, 2 * d, d)]
tl = [(1 + d / 2, 1.0, 0.3, 0.1)]
Av, s, Sig, Cmax, Cmean = measure_Av(sq, tl, k, M=900)
print(f"k=2 tilted variant: n={len(sq)+len(tl)}  |Av|={Av:.4f}  s={s:.4f}  "
      f"VIOLATION={Av > s}")

# general column family: interpolate split-cell -> equal column at k=2
print("\nk=2 one-deficient-column family (a1,a2,a3), sum=2, |Av| vs s:")
for a1 in (1.0, 0.9, 0.8, 2/3):
    rem = 2 - a1
    for a2 in (min(1.0, rem - 1e-9), rem / 2 + 0.1, rem / 2):
        a3 = rem - a2
        if not (0 < a3 <= 1 and 0 < a2 <= 1):
            continue
        sq = [(0, 0, 1), (0, 1, 1),
              (1, 0, a1), (1, a1, a2), (1, a1 + a2, a3)]
        Av, s, Sig, _, _ = measure_Av(sq, [], 2, M=900)
        print(f"  a=({a1:.3f},{a2:.3f},{a3:.3f})  |Av|={Av:.4f}  s={s:.4f}  "
          f"viol={Av - s:+.4f}")
