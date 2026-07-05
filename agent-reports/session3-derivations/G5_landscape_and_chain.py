"""G5 part 2:
(A) D-landscape per k: regime, bad-set measure, diamond-route bound for all-short packings.
(B) Rotated-grid pure-45 packing: verify pointwise chain sum p_i q_i <= k^2 + D(x,y),
    measure G, compare against the wall-argument prediction G >= 0.0433k - 0.17.
(C) Direct Wall-Lemma check at 45 deg in the original frame.
"""
import math, random
random.seed(45)
SQ2 = math.sqrt(2)

print("=== (A) landscape: k, gamma, regime, bad measure, all-short diamond bound on eps ===")
for k in range(2, 61):
    g = (k/SQ2) % 1.0
    K = math.floor(k/SQ2)
    # regime thresholds ignoring O(1/K) margins (flagged)
    if g < 0.25:   reg, bad, bound = 1, 4*g-4*g*g, 4*g
    elif g < 0.5:  reg, bad, bound = 2, 4*g*g, float('inf')     # intersection regime: sumset only
    elif g < 0.75: reg, bad, bound = 3, (2*g-1)*(3-2*g), 2*(2*g-1)
    else:          reg, bad, bound = 4, (2*g-1)**2, float('inf')
    margin_ok = min(abs(4*g-round(4*g)), 1) * K > 1.5   # crude O(1/K) safety flag
    tag = "" if margin_ok else "  [margin<O(1/K): reclassify]"
    if bound < 0.5:
        tag += "  <-- sub-C-S from diamond alone (all-short)"
    print(f"k={k:2d} gamma={g:.4f} regime={reg} bad|={bad:.3f} eps<= {bound if bound<9 else 9.99:.3f}{tag}")

def diamond_D(k, x, y):
    half = k/SQ2; K = math.floor(half); g = half-K
    chi = lambda z: 1 if (z % 2.0) < 2*g else 0
    s, t = x+y, x-y
    che_s, cho_s, che_t, cho_t = chi(s), chi(s-1), chi(t), chi(t-1)
    return K*(che_s+cho_s+che_t+cho_t) + che_s*che_t + cho_s*cho_t + 2*K*K - k*k

print("\n=== (B) rotated-grid pure-45 packing, chain check ===")
for k in [5, 10, 17]:
    c = k/SQ2; L = k*SQ2
    # unit cells [a+ox,a+1+ox]x[b+oy,b+1+oy] inside diamond; offset tuned
    ox, oy = 0.3, 0.2
    cells = []
    for a in range(-1, math.ceil(L)+1):
        for b in range(-math.ceil(c)-1, math.ceil(c)+1):
            u0, u1, v0, v1 = a+ox, a+1+ox, b+oy, b+1+oy
            ok = all(abs(u-c)+abs(v) <= c + 1e-12 for u in (u0,u1) for v in (v0,v1))
            if ok: cells.append((u0, v0))
    n = len(cells); Sd = n; G = k*k - n
    print(f"k={k}: squares={n}, Sum d={Sd}, eps={Sd-k*k}, G={G}  (wall pred G>={0.0433*k-0.17:.2f})")
    # pointwise chain: sum p_i q_i <= k^2 + D  at random shifts
    worst = -1e9; viol = 0
    for _ in range(3000):
        x, y = random.random(), random.random()
        tot = 0
        for (u0, v0) in cells:
            # p_i = #integers m with u0 <= m+x < u0+1  (equals 1 always for unit side, any x) -- compute generically
            p = math.floor(u0+1-x) - math.ceil(u0-x) + 1
            q = math.floor(v0+1-y) - math.ceil(v0-y) + 1
            # half-open [u0,u0+1): careful: integer count in [u0-x, u0+1-x)
            p = math.ceil(u0+1-x) - math.ceil(u0-x)
            q = math.ceil(v0+1-y) - math.ceil(v0-y)
            tot += p*q
        Dv = diamond_D(k, x, y)
        slack = (k*k + Dv) - tot
        if slack < 0: viol += 1
        worst = max(worst, -slack) if False else worst
    print(f"   chain violations: {viol}/3000")

print("\n=== (C) direct Wall-Lemma check at 45 deg, original frame ===")
# squares: centers z_j, side d=1 at 45 -> lower envelope V at lowest vertex
# use the k=5 packing mapped back: original coords (X,Y) = R_45(u,v) i.e. X=(u-v)/sq2? define R: frame->orig
# frame point (u,v) -> original (x,y) = ((u+? )) ; we rotated original by -45: (u,v)=R_-45(x,y) => (x,y)=R_45(u,v)
# R_45(u,v) = ((u - v)/SQ2, (u + v)/SQ2). Check container: frame diamond vertices (0,0)->(0,0), (L,0)->(k,k), (L/2,L/2)->(0,k): orig square [0,k]^2. ok
k = 5; c = k/SQ2; L = k*SQ2; ox, oy = 0.3, 0.2
cells = []
for a in range(-1, math.ceil(L)+1):
    for b in range(-math.ceil(c)-1, math.ceil(c)+1):
        u0,u1,v0,v1 = a+ox, a+1+ox, b+oy, b+1+oy
        if all(abs(u-c)+abs(v) <= c+1e-12 for u in (u0,u1) for v in (v0,v1)):
            cells.append((u0,v0))
# lowest vertex of cell in original frame: corners
def orig(u,v): return ((u-v)/SQ2, (u+v)/SQ2)
sq = []
for (u0,v0) in cells:
    pts = [orig(u0,v0), orig(u0+1,v0), orig(u0,v0+1), orig(u0+1,v0+1)]
    sq.append(pts)
NX = 4000; dx = k/NX; intphi = 0.0
lhs_terms = {}
served = {}
for ix in range(NX):
    x = (ix+0.5)*dx
    best = k; who = None
    for j,pts in enumerate(sq):
        xs = [p[0] for p in pts]; ys=[p[1] for p in pts]
        if min(xs) <= x <= max(xs):
            # lower envelope of 45-square: V from lowest vertex
            lv = min(pts, key=lambda p: p[1])
            f = lv[1] + abs(x - lv[0])
            # valid only within projection; clip: check f <= max over edges... for diamond it's exact
            if f < best: best, who = f, j
    intphi += best*dx
    if who is not None:
        served.setdefault(who, []).append(x)
lhs = 0.0
for j, xs in served.items():
    A = len(xs)*dx
    lv = min(sq[j], key=lambda p: p[1])
    lhs += lv[1]*A + A*A/4
Aempty = k - sum(len(v) for v in served.values())*dx
lhs += k*Aempty
G = k*k - len(cells)
print(f"k=5: int phi = {intphi:.3f}, wall-LHS = {lhs:.3f}, G = {G}   (need LHS <= int phi <= G)")
