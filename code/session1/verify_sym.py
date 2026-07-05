import sympy as sp

d, u1, th = sp.symbols('d u1 theta', positive=True)
c, s = sp.cos(th), sp.sin(th)
U = c + s
sig = U - 1
w = d*U
sin2 = sp.sin(2*th)

# Claim 6(i): 2 d sigma - d^2 sin2th == d sigma (2 - d - w)
lhs = 2*d*sig - d**2*sin2
rhs = d*sig*(2 - d - w)
print("6(i):", sp.simplify(sp.expand_trig(lhs - rhs)))

# equivalence: surplus>=defect iff d+w<=2  (difference factors as d*sigma*(2-d-w))
print("6(i) factor:", sp.factor(sp.simplify(sp.expand_trig(lhs))))

# Claim 6(ii)
print("6(ii)a:", sp.simplify(sig**2 - 2*(1-c)*(1-s)))
print("6(ii)b:", sp.simplify(sp.expand_trig(sig**2 - (sin2 - 2*sig))))

# Claim 6(iii): (w-1)^2 - d sigma (d + w - 2) == (1-d)^2
print("6(iii):", sp.simplify(sp.expand_trig((w-1)**2 - d*sig*(d + w - 2) - (1-d)**2)))

# Claim 7 algebra: with W = d*u1 - 1, s*c = (u1^2-1)/2:
# ell1+ell2 = W*u1/(d*s*c) = 2*u1*(d*u1-1)/(d*(u1^2-1)) ; is  <2  <=>  d<u1 ?
W = d*u1 - 1
sumell = W*u1 / (d*(u1**2-1)/2)
print("7 sum simplified:", sp.simplify(sumell))
# sumell - 2:
diff = sp.simplify(sp.together(sumell - 2))
print("7 (ell1+ell2) - 2 =", sp.factor(diff))
