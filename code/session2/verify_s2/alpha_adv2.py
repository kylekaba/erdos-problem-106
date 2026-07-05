"""Independent adversarial re-check of Lemma alpha' with NEW cheat families:
(1) two-layer notch filling: second row pushed UP into the V-notches of the hug row;
(2) sides 1.05 (max allowed), exact boundary tan phi0 = tau/2;
(3) alternating-tilt brick rows;
(4) random restarts with many seeds.
Also arithmetic audit of the constants in Steps 3-5 and of the edge corollary.
"""
import sys, numpy as np
sys.path.insert(0, "/private/tmp/claude-501/-Users-kylekabasares-Desktop-erdos-106/6b0597a9-48bd-4e8c-a957-7fc4a05f26d8/scratchpad/session2/F5")
from alpha_prime_check import square, sat_disjoint, below_line, uncovered_strip_area, flush_to_line, greedy_row

H = 0.25

def push_up(P0, polys, tau, beta):
    """Raise square from far below until it (a) stays disjoint from polys, (b) below line."""
    def ok(dy):
        P = P0.copy(); P[:, 1] += dy
        if not below_line(P, tau, beta): return False
        return all(sat_disjoint(P, Q) for Q in polys)
    lo, hi = 0.0, 6.0   # dy raise from start
    if not ok(0.0): return None
    # find max raise
    for _ in range(60):
        mid = 0.5*(lo+hi)
        if ok(mid): lo = mid
        else: hi = mid
    P = P0.copy(); P[:, 1] += lo
    return P

def two_layer(tau, phi0, d1, d2, psi2, X, stagger=0.5):
    """Layer 1: greedy coherent hug at +phi0, sides d1.
       Layer 2: squares at tilt psi2 pushed up into the notches, staggered."""
    nmax = int(2*(X+4))+4
    polys = greedy_row(tau, X, [phi0]*nmax, [d1]*nmax)
    layer2 = []
    x = -1.5 + stagger*d2
    while x < X + 1.5:
        P0 = square(x, -8.0, d2, psi2)
        P = push_up(P0, polys + layer2, tau, 0.0)
        if P is not None:
            layer2.append(P)
        x += d2*np.cos(psi2)
    allp = polys + layer2
    # verify
    for p in allp:
        assert below_line(p, tau, 0.0)
    bad = 0
    for i in range(len(allp)):
        for j in range(i+1, len(allp)):
            if not sat_disjoint(allp[i], allp[j]): bad += 1
    return allp, bad

worst = np.inf
print(f"{'tau':>5} {'case':>28} {'unc':>8} {'bound':>8} {'ratio':>8} {'ovl':>4}")
X = 20.0
for tau in [0.1, 0.2, 0.4, 1.0]:
    phi0 = np.arctan(tau/2.0)   # EXACT boundary
    cases = [
        ('2layer d=1.05 psi2=+phi0', 1.05, 1.05, phi0),
        ('2layer d=1.05 psi2=-phi0', 1.05, 1.05, -phi0),
        ('2layer d1=0.95 d2=1.05 +', 0.95, 1.05, phi0),
        ('2layer d1=1.05 d2=0.95 0', 1.05, 0.95, 0.0),
    ]
    for name, d1, d2, psi2 in cases:
        allp, bad = two_layer(tau, phi0, d1, d2, psi2, X)
        unc = uncovered_strip_area(allp, tau, 0.0, X, ngrid=1200)
        bound = (X/228.0)*min(tau - np.tan(phi0), 1/3)
        r = unc/bound
        worst = min(worst, r)
        print(f"{tau:5.2f} {name:>28} {unc:8.4f} {bound:8.4f} {r:8.2f} {bad:4d}")
# random restarts, exact boundary, sides mixed in [0.95,1.05]
rng = np.random.default_rng(1)
for tau in [0.2, 1.0]:
    phi0 = np.arctan(tau/2.0)
    for seed in range(6):
        rng = np.random.default_rng(seed)
        nmax = int(2*(X+4))+4
        psis = rng.choice([-phi0, phi0, 0.0], nmax)
        ds = rng.uniform(0.95, 1.05, nmax)
        polys = greedy_row(tau, X, psis, ds)
        for p in polys: assert below_line(p, tau, 0.0)
        unc = uncovered_strip_area(polys, tau, 0.0, X, ngrid=1000)
        bound = (X/228.0)*min(tau - np.tan(phi0), 1/3)
        r = unc/bound
        worst = min(worst, r)
        print(f"{tau:5.2f} {'rand-brick seed '+str(seed):>28} {unc:8.4f} {bound:8.4f} {r:8.2f}    0")
print(f"\nWORST ratio (new adversaries) = {worst:.3f}  (must be >= 1)")

# ---- arithmetic audit of constants ----
print("\n--- constants audit ---")
eta = 1/20
phi0max = np.arctan(0.5)
wmax = (1+eta)*(np.cos(phi0max)+np.sin(phi0max))
print("w_max =", wmax, "<= 1.409:", wmax <= 1.409)
print("2h/w_max =", 0.5/wmax, ">= 1/3:", 0.5/wmax >= 1/3)
diam = np.sqrt(2)*(1+eta)
print("diam =", diam, "<= 1.49:", diam <= 1.49)
print("height 3.23 = h+1.49+1.49*tau(<=1):", 0.25+1.49+1.49)
print("J coef: 3.23/0.9025 =", 3.23/0.9025, " (claimed 3.579)")
print("J at X=1:", 3.23*(1+2.98)/0.9025, "<= 14.25:", 3.23*3.98/0.9025 <= 14.25)
print("assembly: 4*4*14.25 =", 4*4*14.25)
print("min tau-branch: 2/tau - tau >= 1 for tau<=1:", min(2/t - t for t in np.linspace(0.01,1,1000)) >= 1)
# edge corollary corrected constant
print("\n--- alpha'-edge corrected count (poke-above allowed) ---")
for Xe in [0.63, 0.8, 1.06]:
    area_below = (Xe+2.98)*3.23
    area_above = 2*1.49*2.98     # x' in [-1.49,0]u[Xe,Xe+1.49], 0 < y-l <= 2.98
    J = (area_below+area_above)/0.9025
    const = (Xe/2)**2/ ( J )/4   # U >= tau2 * const
    print(f" Xe={Xe:5.2f}  J<={J:6.2f}  U >= tau2/{4*J/(Xe/2)**2:7.1f}")
# author's claimed 585 audit (ignoring poke-above):
for Xe in [0.63, 1.06]:
    J = (Xe+2.98)*3.23/0.9025
    print(f" author-style Xe={Xe}: J<={J:.2f}, 1/const={4*J/(Xe/2)**2:.0f}")
