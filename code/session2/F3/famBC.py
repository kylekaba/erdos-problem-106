"""Family B: folding-gap config (two congruent u-squares at integer offset).
Family C: randomized perturbed split-cells with one tilted square."""
import numpy as np
from rig import stats, compare_inscribed, validate

def report(tag, sq, ti, M=600):
    ok = validate(sq)
    r = compare_inscribed(sq, ti, M=M)
    piG = 1 - r['avm']
    fold = r['g'] - piG                       # folding loss of gap (>=0 iff |piG|<g)
    save = r['piR'] - r['piRnG']              # |pi(R) ∩ pi(G)| : genuine savings
    red = r['margin2'] - (r['ds'] + r['diff'])
    print(f"{tag:18s} valid={ok} |Av|={r['avm']:.5f} s={r['s']:.5f} g={r['g']:.5f} "
          f"marg={r['margin']:.5f} g+s={r['g']+r['s']:.4f} fold={fold:.5f}")
    print(f"{'':18s} diff={r['diff']:.5f} areaR={r['areaR']:.5f} piR={r['piR']:.5f} "
          f"piRnoG={r['piRnG']:.5f} save={save:.5f} ds={r['ds']:.5f} red_ok={red:.5f} "
          f"sub_v={r['subset_viol']:.5f} over={r['over']:.6f}")
    return r

print("=== FAMILY B: folding gap, near-critical bottom row ===")
for (u, v, t) in [(0.90, 0.10, 0.3), (0.90, 0.10, 0.6), (0.95, 0.05, 0.5),
                  (0.80, 0.20, 0.3), (0.80, 0.20, 0.7854), (0.98, 0.02, 0.5)]:
    c = np.cos(t) + np.sin(t)
    vt = v / c
    sq = [
        (0.5, 1.5, 1.0, 0.0),
        (1.5, 1.5, 1.0, 0.0),
        (u/2, u/2, u, 0.0),               # [0,u]^2
        (1 + u/2, u/2, u, 0.0),           # [1,1+u]x[0,u]  (offset (1,0) twin)
        (u + v/2, v/2, vt, t),            # tilted 5th in [u,u+v]x[0,v]
    ]
    report(f"B u={u} v={v} t={t}", sq, 4)

print()
print("=== FAMILY C: randomized perturbed split-cells, one tilted ===")
rng = np.random.default_rng(20260704)
worst = None
nval = 0
for trial in range(60):
    # three big squares in cells (0,1),(1,0),(1,1), random side & corner
    sq = []
    for (ox, oy) in [(0,1),(1,0),(1,1)]:
        d = rng.uniform(0.85, 1.0)
        cx = ox + (d/2 if rng.random() < .5 else 1 - d/2)
        cy = oy + (d/2 if rng.random() < .5 else 1 - d/2)
        sq.append((cx, cy, d, 0.0))
    # cell (0,0): a tilted (inscribed in [0,a]x[0,a]) + b AP at [a,a+b]x[0,b]
    a = rng.uniform(0.25, 0.7)
    b = rng.uniform(0.5*(1-a), 1-a)
    t = rng.uniform(0.05, np.pi/4)
    c = np.cos(t) + np.sin(t)
    sq.append((a/2, a/2, a/c, t))
    sq.append((a + b/2, b/2, b, 0.0))
    if not validate(sq):
        continue
    nval += 1
    r = compare_inscribed(sq, 4, M=400)
    red = r['margin2'] - (r['ds'] + r['diff'])
    m = r['margin']
    if worst is None or m < worst[0]:
        worst = (m, red, a, b, t, r['subset_viol'], r['over'], r['piR']-r['piRnG'])
    if m < 0 or red < -1e-3 or r['subset_viol'] > 1e-9:
        print("VIOLATION", trial, m, red, a, b, t)
print(f"valid samples: {nval}")
print(f"worst FCMB margin: {worst[0]:.5f} (red_ok={worst[1]:.5f}, a={worst[2]:.3f}, "
      f"b={worst[3]:.3f}, t={worst[4]:.3f}, sub_v={worst[5]:.5f}, over={worst[6]:.6f}, save={worst[7]:.5f})")
