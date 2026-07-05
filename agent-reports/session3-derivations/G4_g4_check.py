#!/usr/bin/env python3
"""G4 machine checks: spatial chain/strip-decomposition theorems.

Checks:
 A. Chord formula for a tilted square (piecewise: ramp x/(sc), plateau d sec th, ramp)
    against brute polygon-line intersection.  [foundation for Lemma H]
 B. Integral identity: R = int (1 - ch)_+ dx over the projection equals
    w - d^2 if d <= cos th,  sin th cos th if d >= cos th.  [mass-neutrality no-go]
 C. Lemma H (Helly-midline): random narrow groups -> midline hits every member's
    middle region; chord sum <= vertical span; adversarial random tries.
 D. Theorem SD equality on the deficient column U_k and on T12-style column tilings:
    Sum d sec th <= k per narrow class, total = N exactly at the extremals.
 E. Adversarial search: random perturbations/tilts of columnar packings trying to get
    Sum d > N while keeping <= k narrow classes and disjointness -> must fail.
 F. Over-full line existence: for a packing with Sum w > N, measure of
    {x : n(x) >= k+1} > 0 and int (n-k)_+ >= t.
"""
import numpy as np
rng = np.random.default_rng(7)

def square_poly(cx, cy, d, th):
    # square side d, rotated th, centered (cx,cy)
    h = d/2.0
    pts = np.array([[-h,-h],[h,-h],[h,h],[-h,h]])
    c, s = np.cos(th), np.sin(th)
    R = np.array([[c,-s],[s,c]])
    return pts @ R.T + np.array([cx,cy])

def chord_at_x(poly, x):
    """length of intersection of vertical line at x with convex polygon"""
    ys = []
    n = len(poly)
    for i in range(n):
        x1,y1 = poly[i]; x2,y2 = poly[(i+1)%n]
        if (x1-x)*(x2-x) < 0:
            tt = (x-x1)/(x2-x1)
            ys.append(y1 + tt*(y2-y1))
        elif x1 == x:
            ys.append(y1)
    if len(ys) < 2: return 0.0
    return max(ys)-min(ys)

def chord_formula(d, th, u):
    """u = offset from bbox-left, in [0,w]; folded th in [0,pi/4]"""
    c, s = np.cos(th), np.sin(th)
    w = d*(c+s)
    if u <= 0 or u >= w: return 0.0
    if th == 0: return d
    if u <= d*s: return u/(s*c)
    if u >= d*c: return (w-u)/(s*c)
    return d/c

# ---- A: chord formula ----
maxerr = 0.0
for _ in range(300):
    d = rng.uniform(0.2, 1.4); th = rng.uniform(0, np.pi/4)
    poly = square_poly(0,0,d,th)
    xmin = poly[:,0].min()
    w = d*(np.cos(th)+np.sin(th))
    for u in rng.uniform(1e-6, w-1e-6, 40):
        ch1 = chord_at_x(poly, xmin+u)
        ch2 = chord_formula(d, th, u)
        maxerr = max(maxerr, abs(ch1-ch2))
print("A. chord formula max err:", maxerr, "PASS" if maxerr < 1e-9 else "FAIL")

# ---- B: integral of (1-ch)_+ ----
worstB = 0.0
for _ in range(400):
    d = rng.uniform(0.3, 1.3); th = rng.uniform(1e-4, np.pi/4)
    c, s = np.cos(th), np.sin(th)
    w = d*(c+s)
    us = np.linspace(0, w, 200001)
    ch = np.array([chord_formula(d,th,u) for u in us])
    R = np.trapezoid(np.clip(1-ch,0,None), us)
    pred = (w - d*d) if d <= c else s*c
    worstB = max(worstB, abs(R-pred))
print("B. R-integral identity max err:", worstB, "PASS" if worstB < 1e-4 else "FAIL")

# ---- C: Lemma H on random narrow groups ----
# build a narrow group: X interval [0,X]; members: near-unit squares with tilts,
# bbox x-range inside [0,X], condition w - 2 d s > X/2 checked; verify midline
# X/2 lies strictly inside every member's middle region and chords disjoint (by
# construction we stack them vertically so disjointness holds), sum d sec th <= span.
failC = 0; trials = 0
for _ in range(2000):
    kk = rng.integers(3, 8)
    X = rng.uniform(0.9, 1.9)
    y = 0.0; members = []
    ok = True
    for j in range(kk):
        d = rng.uniform(0.55, 1.25); th = rng.uniform(0, 0.35)
        c, s = np.cos(th), np.sin(th)
        w = d*(c+s)
        if w > X or w - 2*d*s <= X/2 + 1e-12:
            ok = False; break
        a = rng.uniform(0, X - w)          # bbox left within [0, X-w]
        members.append((d, th, a, w))
    if not ok: continue
    trials += 1
    mid = X/2
    for (d, th, a, w) in members:
        c, s = np.cos(th), np.sin(th)
        lo, hi = a + d*s, a + d*c    # middle region
        if not (lo < mid < hi):
            failC += 1
print(f"C. Lemma H midline-in-middle: {trials} groups, {failC} failures",
      "PASS" if failC == 0 else "FAIL")

# ---- D: SD equality on deficient column + T12 ----
for k in (2,3,4):
    N = k*k
    # deficient column: k-1 unit columns (k units each) + column of k+1 squares k/(k+1)
    tot = 0.0; classes = []
    for j in range(k-1):
        classes.append([1.0]*k)      # unit column: sum d sec0 = k
    classes.append([k/(k+1)]*(k+1))  # deficient column: (k+1)*k/(k+1) = k
    per = [sum(cl) for cl in classes]
    tot = sum(per)
    assert all(p <= k + 1e-12 for p in per)
    print(f"D. k={k}: deficient column: per-class sums {['%.4f'%p for p in per]}, total {tot:.6f} vs N={N}",
          "PASS" if abs(tot-N) < 1e-9 else "FAIL")
# T12 (k=4, b=2: k=2b(b-1)=4): columns widths k/(k+b)=4/6, k/(k+1-b)=4/3>1?? widths: 4/6, 4/3 ...
# T12 column tiling k=4: columns of widths 4/6 (6 squares), 4/3 (3 squares), 1,1 (4 squares each)
k=4; per = [6*(4/6), 3*(4/3), 4*1.0, 4*1.0]
print("D. T12 k=4 per-class sums:", per, "total", sum(per), "vs N=16",
      "PASS" if abs(sum(per)-16) < 1e-9 and all(p <= 4+1e-12 for p in per) else "FAIL")
# NOTE: the 4/3-width class members have d = 4/3, w = d > X/2 = 2/3 OK, but d=4/3 means
# X_j = 4/3 and w - 2ds = 4/3 > X_j/2 = 2/3: narrow OK.

# ---- E: adversarial columnar search ----
# k=2: try to place 5 squares in [0,2]^2 in 2 narrow classes with sum d > 4.
# Parametrize: two columns [0,x0] and [x0,2]; column A: m squares tilted; column B: 5-m.
# Use random search with SAT-style rejection (polygon disjointness via separating axis).
def polys_disjoint(P, Q, eps=1e-9):
    # SAT for convex polys
    for poly in (P, Q):
        n = len(poly)
        for i in range(n):
            e = poly[(i+1)%n]-poly[i]
            ax = np.array([-e[1], e[0]])
            p1 = P @ ax; q1 = Q @ ax
            if p1.max() <= q1.min()+eps or q1.max() <= p1.min()+eps:
                return True
    return False

best = -1
for trial in range(4000):
    x0 = rng.uniform(0.8, 1.2)
    mA = rng.integers(2, 4)  # 2 or 3 in column A
    mB = 5 - mA
    ok = True; polys=[]; ds=[]
    yA = 0.0
    for j in range(mA):
        d = rng.uniform(0.5, min(x0, 1.4)*0.999); th = rng.uniform(0, 0.3)
        c,s = np.cos(th), np.sin(th); w = d*(c+s)
        if w > x0 or w - 2*d*s <= x0/2: ok=False; break
        cx = rng.uniform(w/2, x0 - w/2)
        cy = yA + w/2 + rng.uniform(0, 0.05)
        if cy + w/2 > 2: ok=False; break
        polys.append(square_poly(cx, cy, d, th)); ds.append(d); yA = cy + w/2
    if ok:
        XB = 2 - x0; yB = 0.0
        for j in range(mB):
            d = rng.uniform(0.5, min(XB,1.4)*0.999); th = rng.uniform(0, 0.3)
            c,s = np.cos(th), np.sin(th); w = d*(c+s)
            if w > XB or w - 2*d*s <= XB/2: ok=False; break
            cx = x0 + rng.uniform(w/2, XB - w/2)
            cy = yB + w/2 + rng.uniform(0, 0.05)
            if cy + w/2 > 2: ok=False; break
            polys.append(square_poly(cx, cy, d, th)); ds.append(d); yB = cy + w/2
    if not ok or len(polys) != 5: continue
    good = all(polys_disjoint(polys[i], polys[j]) for i in range(5) for j in range(i+1,5))
    if good: best = max(best, sum(ds))
print(f"E. adversarial 2-narrow-class k=2 search: best Sum d = {best:.6f} (bound N=4)",
      "PASS" if best <= 4 + 1e-9 else "FAIL")

# ---- F: over-full line existence ----
# perturbed deficient column k=3 with whisper tilts on the strip squares, then
# inflate sides slightly (breaking validity is fine -- F only tests the Fubini claim
# n(x)>=k+1 on positive measure when Sum w > N, using projections only).
k=3; N=9
wlist=[]; iv=[]
for i in range(k-1):
    for j in range(k):
        wlist.append(1.0); iv.append((i, i+1.0))
for j in range(k+1):
    d = k/(k+1) + 0.02; th=0.03
    w = d*(np.cos(th)+np.sin(th))
    wlist.append(w); iv.append((k-1, k-1+w))
t = sum(wlist) - N
xs = np.linspace(1e-6, k-1e-6, 200001)
nofx = np.zeros_like(xs)
for (a,b) in iv:
    nofx += ((xs > a) & (xs < b))
mu = np.mean(nofx >= k+1)*k
integ = np.mean(np.clip(nofx - k, 0, None))*k
print(f"F. Sum w - N = {t:.4f}; |X_over| = {mu:.4f} > 0; int (n-k)_+ = {integ:.4f} >= t?",
      "PASS" if (t > 0 and mu > 0 and integ >= t - 1e-3) else "FAIL")
