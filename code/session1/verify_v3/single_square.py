import numpy as np

def stats(d, theta, n=1500, seed=0):
    """Deterministic midpoint grid over shift torus [0,1)^2.
    Square S = rotate([0,d]^2, theta) + (d sin th, 0); bbox = [0,w]^2.
    Lattice = Z^2 + (x,y). p = # vertical lines x+Z meeting bbox x-extent [0,w] (== meeting S).
    c = # lattice points strictly inside S (generic shifts; midpoint grid avoids boundaries a.s.)."""
    ct, st = np.cos(theta), np.sin(theta)
    w = d*(ct+st)
    xs = (np.arange(n)+0.5)/n
    X, Y = np.meshgrid(xs, xs, indexing='ij')
    X = X.ravel(); Y = Y.ravel()
    # integers a with x+a in [0,w]  <=> a in [-x, w-x]
    lo = np.ceil(-X); hi = np.floor(w - X)
    p = (hi - lo + 1).astype(int)
    lo2 = np.ceil(-Y); hi2 = np.floor(w - Y)
    q = (hi2 - lo2 + 1).astype(int)
    # count lattice points in S and in bbox: enumerate a in {lo..lo+2}, b likewise (w<2 => <=2 cols, use 3 safe)
    c = np.zeros_like(p); box = np.zeros_like(p)
    for da in range(3):
        a = lo + da
        oka = a <= hi
        Px = X + a
        for db in range(3):
            b = lo2 + db
            okb = b <= hi2
            Py = Y + b
            inbox = oka & okb
            # membership in S: u = R_{-th}(P - (d st, 0)) in [0,d]^2
            ux = ct*(Px - d*st) + st*Py
            uy = -st*(Px - d*st) + ct*Py
            inS = inbox & (ux > 0) & (ux < d) & (uy > 0) & (uy < d)
            c += inS.astype(int)
            box += inbox.astype(int)
    L = box - c           # points in the 4 corner triangles
    B = (p-1)*(q-1)
    D = p + q - 1 - c
    res = {}
    res['w'] = w
    res['identity_c_eq_pq_minus_L_viol'] = int(np.sum(c != p*q - L))
    res['pq_in_floor_set_viol'] = int(np.sum(~np.isin(p,[int(np.floor(w)), int(np.floor(w))+1])) + np.sum(~np.isin(q,[int(np.floor(w)), int(np.floor(w))+1])))
    res['minD'] = int(D.min())
    res['D_eq_m1_iff_pq00_viol'] = int(np.sum((D==-1) != ((p==0)&(q==0))))
    m22 = (p==2)&(q==2)
    res['max_c_on_22'] = int(c[m22].max()) if m22.any() else None
    res['E_c'] = c.mean(); res['E_p'] = p.mean(); res['E_L'] = L.mean(); res['E_B'] = B.mean()
    Dp = np.maximum(D,0)
    res['E_Dp'] = Dp.mean()
    res['E_Dp_formula'] = 2*w - 1 - d**2 + max(0.0,1-w)**2
    res['E_L_formula'] = d*d*np.sin(2*theta)
    res['E_B_formula'] = (w-1)**2
    # NOTES sec.3 identity: surplus - (E[L]-E[B]) =? (1-d)^2  (measured LHS)
    res['identity_LHS_measured'] = 2*(w-d) - (L.mean() - B.mean())
    res['identity_RHS'] = (1-d)**2
    return res

pairs = [(0.85,np.deg2rad(1)),(0.85,np.deg2rad(8)),(0.85,np.deg2rad(45)),
         (0.9,np.deg2rad(20)),(0.95,np.deg2rad(4)),(0.99,np.deg2rad(30)),
         (1.0,np.deg2rad(0.25)),(1.0,np.deg2rad(1)),(1.0,np.deg2rad(4)),(1.0,np.deg2rad(15)),(1.0,np.deg2rad(45)),
         (0.6,np.deg2rad(10)),(0.7,np.deg2rad(30)),(0.5,np.deg2rad(45)),(0.75,np.deg2rad(2))]
print(f"{'d':>5} {'th_deg':>6} {'w':>6} | idV pqV D=-1V minD c22max | E[L]meas/form  E[B]meas/form  E[D+]meas/form | id_LHS/(1-d)^2")
for d,th in pairs:
    r = stats(d,th)
    print(f"{d:5.2f} {np.rad2deg(th):6.2f} {r['w']:6.4f} | {r['identity_c_eq_pq_minus_L_viol']:3d} {r['pq_in_floor_set_viol']:3d} {r['D_eq_m1_iff_pq00_viol']:5d} {r['minD']:4d} {str(r['max_c_on_22']):>6} | {r['E_L']:.5f}/{r['E_L_formula']:.5f}  {r['E_B']:.5f}/{r['E_B_formula']:.5f}  {r['E_Dp']:.5f}/{r['E_Dp_formula']:.5f} | {r['identity_LHS_measured']:.5f}/{r['identity_RHS']:.5f}")
