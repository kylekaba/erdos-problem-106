import numpy as np

def setup(d, th):
    c, s = np.cos(th), np.sin(th)
    return c, s, c+s, d*(c+s)

print("=== Claim 7 coverage: on (u,v) in [0,W)^2, (u,v) in T_BL or (u+1,v+1) in T_TR ===")
def cover_check(d, th, n=2000):
    c,s,u1,w = setup(d,th)
    W = w-1
    if W <= 0: return 0.0, W
    g = (np.arange(n)+0.5)/n * W
    U,V = np.meshgrid(g,g,indexing='ij')
    l1 = U/(d*s) + V/(d*c)
    l2 = (W-U)/(d*s) + (W-V)/(d*c)
    # direct triangle membership (T_BL legs: x<d s, y<d c; T_TR = central image)
    inBL = (l1 < 1)
    inTR = (l2 < 1)
    unc = np.mean(~(inBL|inTR))
    # also verify max of min(l1,l2)
    return unc, np.max(np.minimum(l1,l2))

for (d,th) in [(1.0,0.05),(1.0,0.3),(1.1,0.2),(1.15,0.3),(1.15,0.2),(np.sqrt(2)-1e-3,np.pi/4),(1.05,0.1)]:
    c,s,u1,w = setup(d,th)
    unc, mx = cover_check(d,th)
    print(f"  d={d:.4f} th={th:.3f} (d<=u1: {d<=u1}): uncovered frac={unc:.6f}, max min(l1,l2)={mx:.5f}")

print("  -- sharpness: d slightly > u1 should leave uncovered shifts --")
for (dd,th) in [(0.06,0.2),(0.12,0.3),(0.02,0.1)]:
    c = np.cos(th); s=np.sin(th); u1=c+s; d = u1+dd
    unc, mx = cover_check(d,th)
    print(f"  d=u1+{dd}={d:.4f} th={th}: uncovered frac={unc:.6f}, max min={mx:.5f}")

print("\n=== Claim 9(a) subdivision bookkeeping: (m^2-1)/2 - (m-1)d <= 0, m=ceil(d), d>=3/2 ===")
import math
for d in [1.5, 1.500001, 1.9999, 2.0, 2.0001, 2.5, 2.9999, 3.0, 3.0001, 7.0, 7.0001, 1.499]:
    m = math.ceil(d)
    val = (m*m-1)/2 - (m-1)*d
    flag = "OK" if val <= 1e-12 else "VIOLATION"
    print(f"  d={d}: m={m}, (m^2-1)/2-(m-1)d = {val:+.6f}  {flag}")
# scan
ds = np.linspace(1.5, 50, 2000000)
ms = np.ceil(ds)
vals = (ms*ms-1)/2 - (ms-1)*ds
print(f"  scan d in [1.5,50]: max value = {vals.max():.3e} (should be <= 0; =0 only at d=1.5)")
print(f"  argmax d = {ds[np.argmax(vals)]:.6f}")
# also check piece side d/m <= 1
print(f"  max piece side d/ceil(d) on scan: {np.max(ds/ms):.6f} (<=1?)")

print("\n=== Claim 11 calibration: (k^2+M)/2 with M=k^2+1 vs k*sqrt(k^2+1); unscaled ===")
for k in [1,2,3,5,10,100]:
    scaled_9 = k*k + 0.5
    scaled_cs = k*np.sqrt(k*k+1)
    unscaled_9 = k + 1/(2*k)
    unscaled_cs = np.sqrt(k*k+1)
    thr = 2*k*k+1-2*k*np.sqrt(k*k+1)   # Sum m needed to beat CS (scaled)
    print(f"  k={k}: scaled {scaled_9:.6f} vs CS {scaled_cs:.6f} (9 weaker by {scaled_9-scaled_cs:.2e} ~ 1/(8k^2)={1/(8*k*k):.2e});"
          f" unscaled {unscaled_9:.6f} vs {unscaled_cs:.6f} (diff {unscaled_9-unscaled_cs:.2e} ~ 1/(8k^3)={1/(8*k**3):.2e}); need Sum m > {thr:.3e} ~ 1/(4k^2)={1/(4*k*k):.3e}")
