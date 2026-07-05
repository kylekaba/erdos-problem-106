import numpy as np
from cap import square_corners, valid_packing, count_field, report, units_grid, split_cell

rng = np.random.default_rng(11)

print("== S1: n=N+2 counterexample check ==")
k=2
sqs = [(0.5,0.5,1.0,0.0),(1.5,0.5,1.0,0.0)]
# cell (0,1) tiled by four half-squares
for dx in (0.25,0.75):
    for dy in (0.25,0.75):
        sqs.append((0+dx, 1+dy, 0.5, 0.0))
print("  valid:", valid_packing(2,sqs), "n:", len(sqs))
report("n=N+2 emptycell", 2, sqs, M=200)

print("== S2: two-grain conflict, n=N+1, k=6 (fixed) ==")
def grain(i0, j0, m, t, phase=(0.0,0.0)):
    ta = abs(t)
    d = 1/(np.cos(ta)+np.sin(ta)); sqs=[]
    c0 = np.array([i0 + m/2 + phase[0], j0 + m/2 + phase[1]])
    R = np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])
    for a in range(m):
        for b in range(m):
            rel = (np.array([a+0.5, b+0.5]) - m/2)*d
            cc = c0 + R @ rel
            sqs.append((cc[0], cc[1], d, t))
    return sqs

for (t, ph) in [(0.12,(0.0,0.0)), (0.12,(0.0,0.0)), (0.2,(0.0,0.0))]:
    k=6; m=3
    skip = tuple((i,j) for i in range(m) for j in range(m)) \
         + tuple((i+3,j+3) for i in range(m) for j in range(m)) + ((5,0),)
    sqs = grain(0,0,m,t) + grain(3,3,m,-t,ph) + units_grid(k, skip=skip) + split_cell(5,0,0.5)
    ok = valid_packing(k, sqs)
    print(f"  2grain t=+-{t} ph={ph} valid={ok} n={len(sqs)}")
    if ok: report(f"2grain m=3 t=+-{t}", k, sqs, M=150)

print("== S3: adversarial search, k=2, n=5 (minimize slack) ==")
N=4
def slack_of(sqs, M=110):
    d = np.array([q[2] for q in sqs]); Sig = d.sum()
    C = count_field(2, sqs, M)
    return int(C.max()) - (2*Sig - N), int(C.max())

def try_family_corner_center(d, trials=250, iters=250):
    """4 corner squares + 1 tilted center, side d each; adversarially perturb."""
    base = [(d/2, d/2, d, 0.0), (2-d/2, d/2, d, 0.0),
            (d/2, 2-d/2, d, 0.0), (2-d/2, 2-d/2, d, 0.0),
            (1.0, 1.0, d, np.pi/4)]
    if not valid_packing(2, base): return None, None
    best = base; bs, _ = slack_of(base)
    cur = [list(q) for q in base]; cs = bs
    for it in range(iters):
        i = rng.integers(0,5)
        prop = [list(q) for q in cur]
        prop[i][0] += rng.normal(0,0.04); prop[i][1] += rng.normal(0,0.04)
        prop[i][3] += rng.normal(0,0.06)
        cand = [tuple(q) for q in prop]
        if not valid_packing(2, cand): continue
        s2, _ = slack_of(cand)
        if s2 <= cs + (0.02 if it < iters//2 else 0.0):
            cur, cs = prop, s2
            if s2 < bs: best, bs = cand, s2
    return best, bs

for d in (0.70, 0.72, 0.7387):
    best, bs = try_family_corner_center(d)
    if best is None: print(f"  d={d}: base invalid"); continue
    s_fine, mC = slack_of(best, M=400)
    dd = np.array([q[2] for q in best])
    print(f"  corner-center d={d}: best slack={s_fine:.4f} maxC={mC} Sig={dd.sum():.4f}")

print("== S4: random valid configs k=2 n=5 (mixture sizes/tilts), min slack ==")
best_slack = 99; best_cfg = None
tested = 0
for trial in range(4000):
    nun = rng.integers(0,3)  # 0-2 units at cells
    cells = [(0,0),(1,0),(0,1),(1,1)]
    sqs = [(i+0.5,j+0.5,1.0,0.0) for (i,j) in cells[:nun]]
    for _ in range(5-nun):
        dd = rng.uniform(0.45, 0.98)
        th = rng.choice([0.0, 0.0, np.pi/4, rng.uniform(0,np.pi/4)])
        w = dd*(abs(np.cos(th))+abs(np.sin(th)))/2
        cx = rng.uniform(w, 2-w); cy = rng.uniform(w, 2-w)
        sqs.append((cx,cy,dd,th))
    if not valid_packing(2, sqs): continue
    tested += 1
    sl, mC = slack_of(sqs, M=90)
    if sl < best_slack:
        best_slack, best_cfg = sl, sqs
print(f"  valid configs tested: {tested}; min slack (coarse) = {best_slack:.4f}")
if best_cfg is not None:
    sf, mC = slack_of(best_cfg, M=400)
    dd = np.array([q[2] for q in best_cfg])
    print(f"  refined: slack={sf:.4f} maxC={mC} Sig={dd.sum():.4f}")
    print("  cfg:", [tuple(round(v,3) for v in q) for q in best_cfg])
