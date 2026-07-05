import numpy as np
from cap import valid_packing, count_field, units_grid, split_cell

rng = np.random.default_rng(23)

def metrics(k, sqs, M=110):
    N = k*k; n = len(sqs)
    d = np.array([q[2] for q in sqs])
    Sig = d.sum(); s = ((1-d)**2).sum()
    C = count_field(k, sqs, M)
    maxC = int(C.max())
    slack = maxC - (2*Sig - N)
    Av = float((C == N).mean())
    fv = Av - (s + (N+1-n))
    return slack, fv, maxC, Sig

def anneal(k, seed_sqs, iters=4000, M=100, obj='slack', T0=0.08):
    N = k*k
    cur = [list(q) for q in seed_sqs]
    def score(sq):
        sl, fv, mC, Sig = metrics(k, [tuple(q) for q in sq], M)
        return sl if obj=='slack' else -fv
    cs = score(cur); best = [list(q) for q in cur]; bs = cs
    for it in range(iters):
        T = T0*(1 - it/iters)
        prop = [list(q) for q in cur]
        r = rng.random()
        i = rng.integers(0, len(prop))
        if r < 0.45:   # jiggle
            prop[i][0] += rng.normal(0, 0.05); prop[i][1] += rng.normal(0, 0.05)
            prop[i][3] += rng.normal(0, 0.08)
        elif r < 0.80: # grow (adversary wants big Sigma)
            prop[i][2] = min(1.0, prop[i][2] + abs(rng.normal(0, 0.03)))
        elif r < 0.90: # shrink a bit
            prop[i][2] = max(0.05, prop[i][2] - abs(rng.normal(0, 0.02)))
        else:          # teleport
            w = prop[i][2]
            prop[i][0] = rng.uniform(w/2, k-w/2); prop[i][1] = rng.uniform(w/2, k-w/2)
            prop[i][3] = rng.uniform(0, np.pi/2)
        cand = [tuple(q) for q in prop]
        if not valid_packing(k, cand): continue
        s2 = score(prop)
        if s2 <= cs or rng.random() < np.exp(-(s2-cs)/max(T,1e-4)):
            cur, cs = prop, s2
            if s2 < bs: best, bs = [list(q) for q in prop], s2
    return [tuple(q) for q in best], bs

def seeds_k2():
    d0 = 0.70
    S = {}
    S['corner-center'] = [(d0/2,d0/2,d0,0.),(2-d0/2,d0/2,d0,0.),(d0/2,2-d0/2,d0,0.),
                          (2-d0/2,2-d0/2,d0,0.),(1.,1.,d0,np.pi/4)]
    S['3u+split'] = units_grid(2, skip=((1,1),)) + split_cell(1,1,0.5)
    S['2u+3L'] = [(0.5,0.5,1.,0.),(1.5,0.5,1.,0.)] + \
                 [(0.5,1.5,1.,0.),(1.25,1.25,0.5,0.),(1.75,1.25,0.25,0.)]
    S['pinwheel'] = [(0.4,0.4,0.78,0.),(1.6,0.35,0.68,0.),(0.35,1.6,0.68,0.),
                     (1.6,1.6,0.78,0.),(1.0,1.0,0.55,np.pi/4)]
    return S

def seeds_k3():
    S = {}
    # 5 units + corner-center block in [0,2]^2 region + split cell
    d0=0.70
    cc = [(d0/2,d0/2,d0,0.),(2-d0/2,d0/2,d0,0.),(d0/2,2-d0/2,d0,0.),
          (2-d0/2,2-d0/2,d0,0.),(1.,1.,d0,np.pi/4)]
    un = units_grid(3, skip=((0,0),(1,0),(0,1),(1,1),(2,2)))
    S['cc+units+split'] = cc + un + split_cell(2,2,0.5)
    # 8 units + split + one more split  -> n=10? 7 units + 2 splits = 11 too many; use 8u+split=10
    S['8u+split'] = units_grid(3, skip=((2,2),)) + split_cell(2,2,0.5)
    return S

print("== A1: adversarial slack minimization, k=2, n=5 ==")
for name, sd in seeds_k2().items():
    ok = valid_packing(2, sd)
    if not ok: print(f"  seed {name}: INVALID"); continue
    best, bs = anneal(2, sd, iters=3500, M=100, obj='slack')
    slf, fvf, mC, Sig = metrics(2, best, M=500)
    print(f"  {name}: coarse slack={bs:.4f} | fine slack={slf:.4f} maxC={mC} Sig={Sig:.4f} fcmb_v={fvf:.4f}")
    if slf < 0.02:
        print("    cfg:", [tuple(round(v,4) for v in q) for q in best])

print("== A2: adversarial FCMB (maximize |Av| - s), k=2, n=5 ==")
for name, sd in seeds_k2().items():
    if not valid_packing(2, sd): continue
    best, bs = anneal(2, sd, iters=3500, M=100, obj='fcmb')
    slf, fvf, mC, Sig = metrics(2, best, M=500)
    print(f"  {name}: fine fcmb_viol={fvf:.4f} (viol if >0) slack={slf:.4f} Sig={Sig:.4f}")
    if fvf > -0.005:
        print("    cfg:", [tuple(round(v,4) for v in q) for q in best])

print("== A3: adversarial slack minimization, k=3, n=10 ==")
for name, sd in seeds_k3().items():
    ok = valid_packing(3, sd)
    if not ok: print(f"  seed {name}: INVALID n={len(sd)}"); continue
    best, bs = anneal(3, sd, iters=2500, M=90, obj='slack')
    slf, fvf, mC, Sig = metrics(3, best, M=400)
    print(f"  {name}: n={len(sd)} coarse slack={bs:.4f} | fine slack={slf:.4f} maxC={mC} Sig={Sig:.4f} fcmb_v={fvf:.4f}")
