import numpy as np, math, random
import fcmb_check as F

# ---------- arc-decomposition identity check (AP, all d<=1... units allowed d=1) ----------
def arc_quantities(coords_1d, eps=1e-12):
    """coords_1d: list of (start, d). Miss-arc W_i = [start+d, start+1] mod 1, length 1-d.
    Returns alpha_0 = |{x: miss none}|, alpha_i = |{x: miss exactly i}| via breakpoints."""
    n = len(coords_1d)
    bs = set([0.0, 1.0])
    for (c, d) in coords_1d:
        bs.add(c % 1.0); bs.add((c + d) % 1.0)
    bs = sorted(bs)
    a0 = 0.0; ai = [0.0]*n
    for t in range(len(bs)-1):
        x = (bs[t]+bs[t+1])/2; L = bs[t+1]-bs[t]
        missed = [i for i,(c,d) in enumerate(coords_1d) if F.p_count(c,d,x) <= 0]
        if len(missed) == 0: a0 += L
        elif len(missed) == 1: ai[missed[0]] += L
    return a0, ai

def decomposition_Av(sq, k):
    a0, ai = arc_quantities([(a,d) for (a,b,d) in sq])
    b0, bi = arc_quantities([(b,d) for (a,b,d) in sq])
    val = a0*sum(bi) + b0*sum(ai) + sum(x*y for x,y in zip(ai,bi))
    return val, a0, b0, ai, bi

# ---------- random strip packings at k=2, n=5 ----------
def random_strip_packing(rng):
    k = 2
    c1 = rng.randint(1, 4); c2 = 5 - c1
    if c2 < 1 or c2 > 4: return None
    sq = []
    for (strip, cnt) in ((0, c1), (1, c2)):
        # sides
        ds = [rng.uniform(0.15, 1.0) for _ in range(cnt)]
        if sum(ds) > 2:
            sc = (2 - 1e-9) / sum(ds) * rng.uniform(0.85, 1.0)
            ds = [d*sc for d in ds]
        slack = 2 - sum(ds)
        # random gaps
        cuts = sorted(rng.uniform(0, slack) for _ in range(cnt))
        gaps = [cuts[0]] + [cuts[i]-cuts[i-1] for i in range(1, cnt)]
        y = 0.0
        for d, gp in zip(ds, gaps):
            y += gp
            x0 = strip + rng.uniform(0, 1 - d) if rng.random() < 0.7 else float(strip)
            sq.append((x0, y, d)); y += d
    try:
        F.check_packing(sq, 2)
    except AssertionError:
        return None
    return sq

def perturb(sq, rng, scale):
    k = 2
    out = []
    for (a,b,d) in sq:
        if rng.random() < 0.6:
            d2 = min(1.0, max(0.05, d + rng.gauss(0, scale)))
        else: d2 = d
        a2 = min(k-d2, max(0.0, a + rng.gauss(0, scale)))
        b2 = min(k-d2, max(0.0, b + rng.gauss(0, scale)))
        out.append((a2,b2,d2))
    try:
        F.check_packing(out, k)
    except AssertionError:
        return None
    return out

rng = random.Random(7)
print("=== identity check on random valid strip packings (k=2) ===")
checked = 0; maxerr = 0.0
while checked < 200:
    sq = random_strip_packing(rng)
    if sq is None: continue
    if max(d for _,_,d in sq) > 1: continue
    Av, mc = F.exact_Av(sq, 2)
    dec, a0, b0, ai, bi = decomposition_Av(sq, 2)
    err = abs(Av - dec)
    maxerr = max(maxerr, err)
    assert a0*b0 < 1e-12, (a0, b0)   # budget: alpha0*beta0 = 0
    checked += 1
print(f"200 packings: max |Av - decomposition| = {maxerr:.2e}; alpha0*beta0=0 held always")

print("\n=== k=2 search: maximize |Av| - s and |Av| ===")
best = []   # (viol, Av, s, sq)
bestAv = (0, None)
seeds = []
# structured seeds
seeds.append(F.column_packing(2))
seeds.append(F.split_cell(2, 0.5))
seeds.append(F.stack_gadget(2, [0.6,0.7,0.7]))
for _ in range(20000):
    sq = random_strip_packing(rng)
    if sq: seeds.append(sq)
results = []
for sq in seeds:
    Av, mc = F.exact_Av(sq, 2)
    S, g, s = F.stats(sq, 2)
    results.append((Av - s, Av, s, g, sq))
results.sort(key=lambda r: -r[0])
print("top violations |Av|-s from seed pool:")
for r in results[:5]:
    print(f"  viol={r[0]:+.4f} |Av|={r[1]:.4f} s={r[2]:.4f} g={r[3]:.4f} g+s={r[2]+r[3]:.4f}")
results.sort(key=lambda r: -r[1])
print("top |Av|:")
for r in results[:5]:
    print(f"  |Av|={r[1]:.4f} s={r[2]:.4f} viol={r[0]:+.4f} g+s={r[2]+r[3]:.4f}")

# hill-climb from top violation seeds
print("\nhill-climbing |Av| - s:")
results.sort(key=lambda r: -r[0])
for ridx in range(3):
    cur = results[ridx][4]; curv = results[ridx][0]
    for it in range(4000):
        sc = 0.08 * (0.998 ** it)
        cand = perturb(cur, rng, sc)
        if cand is None: continue
        Av, mc = F.exact_Av(cand, 2)
        S, g, s = F.stats(cand, 2)
        if Av - s > curv:
            curv = Av - s; cur = cand
    Av, mc = F.exact_Av(cur, 2)
    S, g, s = F.stats(cur, 2)
    print(f"  seed{ridx}: viol={curv:+.5f} |Av|={Av:.5f} s={s:.5f} g={g:.5f} g+s={g+s:.5f}")
    print(f"    squares: {[(round(a,4),round(b,4),round(d,4)) for a,b,d in cur]}")
