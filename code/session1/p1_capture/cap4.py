import numpy as np
from cap import valid_packing, count_field, units_grid, split_cell, square_corners
from cap3 import metrics, anneal

rng = np.random.default_rng(5)

print("== B1: fixed k=3 seeds, n=10=N+1 ==")
d0=0.70
cc = [(d0/2,d0/2,d0,0.),(2-d0/2,d0/2,d0,0.),(d0/2,2-d0/2,d0,0.),
      (2-d0/2,2-d0/2,d0,0.),(1.,1.,d0,np.pi/4)]
un5 = units_grid(3, skip=((0,0),(1,0),(0,1),(1,1)))
seed1 = cc + un5   # n=10
def grain(i0,j0,m,t):
    ta=abs(t); d=1/(np.cos(ta)+np.sin(ta)); out=[]
    c0=np.array([i0+m/2, j0+m/2]); R=np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])
    for a in range(m):
        for b in range(m):
            rel=(np.array([a+0.5,b+0.5])-m/2)*d
            cc2=c0+R@rel; out.append((cc2[0],cc2[1],d,t))
    return out
seed2 = grain(0,0,2,0.25) + units_grid(3, skip=((0,0),(1,0),(0,1),(1,1),(2,2))) + split_cell(2,2,0.5)
for name, sd in (('cc+5units',seed1), ('grain2+units+split',seed2)):
    if not valid_packing(3, sd): print(f"  {name}: INVALID n={len(sd)}"); continue
    best, bs = anneal(3, sd, iters=2500, M=90, obj='slack')
    slf, fvf, mC, Sig = metrics(3, best, M=400)
    print(f"  {name}: n={len(sd)} fine slack={slf:.4f} maxC={mC} Sig={Sig:.4f} fcmb_v={fvf:.4f}")

print("== B2: feasibility probe: 10 squares side ~0.85 in k=3 L-region (empty cell (2,2)) ==")
# squares must avoid cell [2,3]x[2,3] entirely; allow tilts; penalty annealing
def penalty(sqs):
    pen = 0.0
    for sq in sqs:
        P = square_corners(*sq)
        pen += max(0, -P.min())*10
        pen += max(0, P[:,0].max()-3)*10 + max(0, P[:,1].max()-3)*10
        # empty-cell intrusion: overlap of bbox with [2,3]^2 (approx by corner test + center grid)
        cx, cy, d, th = sq
        gx = np.linspace(-d/2*0.98, d/2*0.98, 6)
        Xg, Yg = np.meshgrid(gx, gx)
        c,s = np.cos(th), np.sin(th)
        px = cx + c*Xg - s*Yg; py = cy + s*Xg + c*Yg
        inbad = ((px>2)&(px<3)&(py>2)&(py<3)).mean()
        pen += inbad*d*d*10
    # pairwise overlap penalty via SAT depth (approx: penetration along best axis)
    nn = len(sqs)
    for i in range(nn):
        Pi = square_corners(*sqs[i])
        for j in range(i+1,nn):
            Pj = square_corners(*sqs[j])
            # min over axes of overlap depth; if separated on any axis -> 0
            depth = np.inf
            for P,Q in ((Pi,Pj),(Pj,Pi)):
                for e0 in range(4):
                    e = P[(e0+1)%4]-P[e0]; ax = np.array([-e[1],e[0]]); ax/=np.linalg.norm(ax)
                    a1,a2 = P@ax, Q@ax
                    ov = min(a1.max(),a2.max()) - max(a1.min(),a2.min())
                    depth = min(depth, ov)
            if depth > 0: pen += depth*5
    return pen

def feas_search(dside, trials=6, iters=6000):
    bestpen = np.inf
    for tr in range(trials):
        # random init in L region
        sqs = []
        for _ in range(10):
            while True:
                cx, cy = rng.uniform(0.45,2.55), rng.uniform(0.45,2.55)
                if not (cx>1.9 and cy>1.9): break
            sqs.append([cx, cy, dside, rng.uniform(0,np.pi/2)])
        cp = penalty([tuple(q) for q in sqs])
        for it in range(iters):
            T = 0.05*(1-it/iters)
            prop = [list(q) for q in sqs]
            i = rng.integers(0,10)
            prop[i][0]+=rng.normal(0,0.06); prop[i][1]+=rng.normal(0,0.06); prop[i][3]+=rng.normal(0,0.1)
            pp = penalty([tuple(q) for q in prop])
            if pp <= cp or rng.random() < np.exp(-(pp-cp)/max(T,1e-4)):
                sqs, cp = prop, pp
        bestpen = min(bestpen, cp)
    return bestpen

for dside in (0.80, 0.85):
    bp = feas_search(dside)
    print(f"  d={dside}: best residual penalty = {bp:.5f} (0 => feasible packing found)")

print("== B3: long-shot k=2: heavy restarts, tilt-rich, slack objective ==")
bestall = 99
for r in range(8):
    sd = []
    # random construction: 2 big + 3 medium with random tilts, greedy legalize by shrinking
    for _ in range(5):
        sd.append([rng.uniform(0.4,1.6), rng.uniform(0.4,1.6), rng.uniform(0.65,0.95), rng.uniform(0,np.pi/2)])
    # shrink until valid
    for _ in range(200):
        if valid_packing(2, [tuple(q) for q in sd]): break
        i = rng.integers(0,5); sd[i][2] *= 0.97
        sd[i][0] = min(max(sd[i][0], sd[i][2]), 2-sd[i][2]); sd[i][1] = min(max(sd[i][1], sd[i][2]), 2-sd[i][2])
    cfg = [tuple(q) for q in sd]
    if not valid_packing(2, cfg): continue
    best, bs = anneal(2, cfg, iters=3000, M=100, obj='slack')
    slf, fvf, mC, Sig = metrics(2, best, M=400)
    bestall = min(bestall, slf)
    print(f"  restart {r}: slack={slf:.4f} Sig={Sig:.4f} maxC={mC} fcmb_v={fvf:.4f}")
print(f"  min slack over restarts: {bestall:.4f}")
