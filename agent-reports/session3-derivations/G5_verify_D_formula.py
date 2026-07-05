"""G5: verify the exact two-phase formula for the diamond-container discrepancy.

Squares' frame: container = diamond D_k = {(u,v): |u - k/sqrt2| + |v| <= k/sqrt2},
vertices (0,0),(L,0),(L/2,+-L/2), L=k*sqrt2.  Lattice Z^2+(x,y).
Claim:  |D_k cap (Z^2+p)| = 2K^2 + K(sig(s)+sig(t)) + X(s,t)
with L/2 = k/sqrt2 = K+gamma (K=floor, gamma=frac), s=x+y, t=x-y,
chi_e(s) = 1 if s mod 2 in [0,2gamma) else 0,   chi_o(s)=chi_e(s-1),
sig(s) = chi_e(s)+chi_o(s)   (1-periodic),
X = chi_e(s)chi_e(t) + chi_o(s)chi_o(t).
Hence D := count - k^2 = K(sig(s)+sig(t)-4gamma) + X - 2gamma^2.
"""
import math, random
random.seed(106)

def brute_count(k, x, y):
    L = k*math.sqrt(2); c = L/2
    cnt = 0
    # u = m+x in [0,L], v = n+y in [-L/2, L/2]
    for m in range(math.floor(-x)-1, math.ceil(L-x)+2):
        u = m+x
        h = c - abs(u-c)          # allowed |v| <= h
        if h < 0: continue
        n_lo = math.ceil(-h - y); n_hi = math.floor(h - y)
        if n_hi >= n_lo: cnt += n_hi - n_lo + 1
    return cnt

def formula_count(k, x, y):
    half = k/math.sqrt(2); K = math.floor(half); g = half - K
    s = (x+y) % 2.0; t = (x-y) % 2.0
    chi = lambda z: 1 if (z % 2.0) < 2*g else 0
    che_s, cho_s = chi(s), chi(s-1)
    che_t, cho_t = chi(t), chi(t-1)
    sig_s, sig_t = che_s+cho_s, che_t+cho_t
    X = che_s*che_t + cho_s*cho_t
    return 2*K*K + K*(sig_s+sig_t) + X, (sig_s, sig_t, X, K, g)

bad = 0; trials = 0
for k in [2,3,4,5,7,10,12,17,29,41]:
    meanD = 0.0; M = 4000
    for _ in range(M):
        x, y = random.random(), random.random()
        b = brute_count(k,x,y); f,_ = formula_count(k,x,y)
        trials += 1
        if b != f:
            bad += 1
            if bad < 8: print("MISMATCH", k, x, y, b, f)
        meanD += b - k*k
    print(f"k={k:3d} gamma={ (k/math.sqrt(2))%1 :.4f}  meanD={meanD/M:+.4f}  (formula matches so far: {trials-bad}/{trials})")
print("TOTAL mismatches:", bad, "of", trials)
