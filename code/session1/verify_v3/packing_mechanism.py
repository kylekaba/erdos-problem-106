import numpy as np

# k=2, T=[0,2]^2. Packing: 3 axis-parallel unit squares at (0,0),(1,0),(0,1),
# plus a tilted square side 0.9, theta=0.2 inside cell [1,2]x[1,2],
# plus a small tilted square side 0.35, theta=0.6 in the remaining corner area of that cell?
# (Just need pairwise-disjoint, inside T.)
# Square spec: (cx, cy, d, th) center-based.
sq = [
    (0.5,0.5,1.0,0.0),
    (1.5,0.5,1.0,0.0),
    (0.5,1.5,1.0,0.0),
    (1.5,1.5,0.9,0.2),   # bbox width 0.9*(cos.2+sin.2)=1.061 <=1? 1.061>1 -> shrink
]
# fix: tilted square must fit in [1,2]^2: need d*(cos+sin) <= 1 -> d <= 0.842 for th=0.2
sq[3] = (1.5,1.5,0.84,0.2)
k = 2

def inside_T(cx,cy,d,th):
    c,s = np.cos(th), np.sin(th)
    w = d*(abs(c)+abs(s))
    return cx-w/2 >= -1e-12 and cx+w/2 <= k+1e-12 and cy-w/2>=-1e-12 and cy+w/2<=k+1e-12

def corners(cx,cy,d,th):
    c,s = np.cos(th), np.sin(th)
    h = d/2
    pts = []
    for ex,ey in [(-h,-h),(h,-h),(h,h),(-h,h)]:
        pts.append((cx + c*ex - s*ey, cy + s*ex + c*ey))
    return np.array(pts)

# disjointness check via SAT for convex polygons
def sat_disjoint(P,Q):
    def axes(R):
        A=[]
        for i in range(4):
            e = R[(i+1)%4]-R[i]
            A.append(np.array([-e[1],e[0]]))
        return A
    for ax in axes(P)+axes(Q):
        p0,p1 = (P@ax).min(),(P@ax).max()
        q0,q1 = (Q@ax).min(),(Q@ax).max()
        if p1 <= q0 + 1e-12 or q1 <= p0 + 1e-12:
            return True
    return False

polys = [corners(*s) for s in sq]
ok = all(inside_T(*s) for s in sq) and all(sat_disjoint(polys[i],polys[j]) for i in range(4) for j in range(i+1,4))
print("packing valid (inside T, pairwise disjoint):", ok)

def in_sq(P, s):
    cx,cy,d,th = s
    c,sn = np.cos(th), np.sin(th)
    ux =  c*(P[...,0]-cx) + sn*(P[...,1]-cy)
    uy = -sn*(P[...,0]-cx) + c*(P[...,1]-cy)
    return (np.abs(ux) < d/2) & (np.abs(uy) < d/2)

rng = np.random.default_rng(3)
n = 400
xs = (np.arange(n)+0.5)/n
viol_budget = 0; viol_chain = 0; checked_chain = 0
for x in xs:
    for y in xs:
        # lattice points in [0,k]^2: (x+a, y+b), a,b in {0,..,k-1} (x,y in (0,1))
        pts = np.array([[x+a, y+b] for a in range(k) for b in range(k)])
        total_c = 0; sum_pq = 0; allL0 = True
        for s in sq:
            cx,cy,d,th = s
            c_,sn = np.cos(th), np.sin(th)
            w = d*(abs(c_)+abs(sn))
            x0,x1 = cx-w/2, cx+w/2
            y0,y1 = cy-w/2, cy+w/2
            p = int(np.floor(x1-x)-np.ceil(x0-x)+1)
            q = int(np.floor(y1-y)-np.ceil(y0-y)+1)
            inb = (pts[:,0]>x0)&(pts[:,0]<x1)&(pts[:,1]>y0)&(pts[:,1]<y1)
            cc = int(np.sum(in_sq(pts, s)))
            L = int(np.sum(inb)) - cc
            total_c += cc; sum_pq += p+q
            if L != 0: allL0 = False
        if total_c > k*k: viol_budget += 1
        if allL0:
            checked_chain += 1
            if total_c < sum_pq - len(sq): viol_chain += 1
print(f"shifts tested: {n*n}; budget violations (sum c > k^2): {viol_budget}")
print(f"shifts with all L_i=0: {checked_chain}; chain violations (sum c < sum(p+q)-M): {viol_chain}")
