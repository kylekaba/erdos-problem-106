import sympy as sp

d, t = sp.symbols('d t', positive=True)
c = sp.cos(t) + sp.sin(t)          # c = cos t + sin t in (1, sqrt2]
dp = d/c                            # inscribed AP square side d' = d/c

s_orig = (1-d)**2                   # deficit contribution of S_1 (tilted, side d)
s_new  = (1-dp)**2                  # deficit contribution of inscribed square
dS     = sp.simplify(s_new - s_orig)          # Delta s = s' - s
areaR  = sp.simplify(d**2 - dp**2)            # area(S_1 \ inscribed) = d^2(1-1/c^2)

# THE assignment's check:  s' + areaR <= s  ??   i.e.  dS + areaR <= 0 ??
excess = sp.simplify(dS + areaR)
print("Delta_s =", sp.factor(dS))
print("areaR   =", sp.factor(areaR))
print("excess  = Delta_s + areaR =", sp.simplify(excess))
print("claim: excess == 2*d*(1-1/c):", sp.simplify(excess - 2*d*(1-1/c)) == 0)

# structure-identity conservation check: 2(d-d') == (d^2-d'^2) + (s'-s)
print("conservation check:", sp.simplify(2*(d-dp) - (areaR + dS)) == 0)

# sign of Delta_s alone (need <= 0 even if |Av\Av'|=0):
print("Delta_s factored:", sp.factor(sp.expand(dS)))
# = d(1-1/c)(2 - d(1+1/c))  -> positive for d < 2c/(c+1); note 2c/(c+1) > 1
print("2c/(c+1) at t=pi/4:", float((2*sp.sqrt(2)/(sp.sqrt(2)+1)).evalf()))
