import numpy as np
rng = np.random.default_rng(7)

def square(cx,cy,d,th):
    c,s = np.cos(th), np.sin(th)
    R = np.array([[c,-s],[s,c]])
    pts = np.array([[dx*d/2,dy*d/2] for dx in(-1,1) for dy in(-1,1)])
    P = pts@R.T + [cx,cy]
    return dict(cx=cx,cy=cy,d=d,th=th,
                xmin=P[:,0].min(), xmax=P[:,0].max(),
                ymin=P[:,1].min(), ymax=P[:,1].max())

def pcount(sq,X0): return np.floor(sq['xmax']-X0)-np.ceil(sq['xmin']-X0)+1
def qcount(sq,Y0): return np.floor(sq['ymax']-Y0)-np.ceil(sq['ymin']-Y0)+1

def ccount(sq,X0,Y0):
    c,s = np.cos(sq['th']), np.sin(sq['th'])
    tot = np.zeros((len(X0),len(Y0)))
    for j in range(int(np.floor(sq['xmin']))-1,int(np.ceil(sq['xmax']))+2):
        for l in range(int(np.floor(sq['ymin']))-1,int(np.ceil(sq['ymax']))+2):
            u = (j+X0[:,None]-sq['cx'])*c + (l+Y0[None,:]-sq['cy'])*s
            v = -(j+X0[:,None]-sq['cx'])*s + (l+Y0[None,:]-sq['cy'])*c
            tot += ((np.abs(u)<sq['d']/2)&(np.abs(v)<sq['d']/2))
    return tot

# ---- 0. algebraic identities, random check ----
print("== identities ==")
for _ in range(4):
    d = rng.uniform(0.5,1.5); th = rng.uniform(0.01,np.pi/4)
    sg = np.cos(th)+np.sin(th)-1; w = d*(1+sg)
    i1 = abs(np.sin(2*th) - (2*sg+sg**2))
    i2 = abs(d*d*np.sin(2*th) - d*sg*(d+w))
    i3 = abs((w-1)**2 - d*sg*(d+w-2) - (1-d)**2)
    print(f" d={d:.3f} th={th:.3f}: sin2t-id {i1:.2e}, Dl=ds(d+w) {i2:.2e}, 6(iii) {i3:.2e}")

# ---- 1. per-square bounds R=E[(L-B)+] <= 2 d sigma - m ----
print("== per-square R <= 2 d sigma - m  (grid 700^2) ==")
n=700
X0 = (np.arange(n)+0.5)/n + 0.123456789e-3
Y0 = (np.arange(n)+0.5)/n + 0.987654321e-4
cases = [(1.0,0.1),(0.95,0.3),(1.05,0.05),(1.10,0.02),(0.8,0.6),(1.3,0.4),(1.0,0.01),(1.2,0.05)]
for d,th in cases:
    sq = square(0.37,0.61,d,th)
    p = pcount(sq,X0); q = qcount(sq,Y0); c = ccount(sq,X0,Y0)
    L = p[:,None]*q[None,:] - c
    assert L.min() >= -1e-9, L.min()
    B = (p[:,None]-1)*(q[None,:]-1)
    assert B.min() >= -1e-9
    D = np.maximum(L-B,0.0)
    # pointwise c >= p+q-1-(L-B)+
    viol = (c - (p[:,None]+q[None,:]-1-D)).min()
    sg = np.cos(th)+np.sin(th)-1; w=d*(1+sg); u1=1+sg; delta=d-1
    if th==0: m=0.0
    elif w<=1: m = d*sg*(2-d-w)
    elif d<=u1: m = (1-d)**2
    else: m = -d*sg*(d+w-2)
    R = D.mean()
    print(f" d={d:.2f} th={th:.2f}: w={w:.3f} branch={'w<=1' if w<=1 else ('d<=u1' if d<=u1 else 'debit')} "
          f"R={R:.5f} bound={2*d*sg-m:.5f} slack={2*d*sg-m-R:+.5f} ptwise_min={viol:+.2e} "
          f"|m|<=4d.delta^2? {abs(m)<=4*d*delta**2+1e-12 if (w>1 and d>u1) else '-'}")

# ---- 2. column tiling k=4 (b=2): kappa should be exactly 1, P+Q<=2N+1 ----
print("== column tiling k=4 ==")
k=4; N=k*k
cols = [(0.0,2/3,6),(2/3,4/3,3),(2.0,1.0,4),(3.0,1.0,4)]
sqs=[]
for a,s,cnt in cols:
    for j in range(cnt):
        sqs.append(dict(xmin=a,xmax=a+s,ymin=j*s,ymax=(j+1)*s))
print(" pieces:",len(sqs)," sum sides:",sum(s['xmax']-s['xmin'] for s in sqs))
m1=4001
X1=(np.arange(m1)+0.5)/m1 + 1.2345e-5
P = sum(np.floor(s['xmax']-X1)-np.ceil(s['xmin']-X1)+1 for s in sqs)
Q = sum(np.floor(s['ymax']-X1)-np.ceil(s['ymin']-X1)+1 for s in sqs)
print(" P range",P.min(),P.max()," Q range",Q.min(),Q.max()," maxP+maxQ",P.max()+Q.max(),"vs 2N+1 =",2*N+1)
vals,cnts = np.unique(P,return_counts=True); pw = cnts/m1
vals2,cnts2 = np.unique(Q,return_counts=True); qw = cnts2/m1
kap = sum(pw[i]*qw[j]*max(2*N+1-vals[i]-vals2[j],0) for i in range(len(vals)) for j in range(len(vals2)))
print(f" kappa = {kap:.6f} (predict 1.0);  E[P]={P.mean():.6f} (predict {N})")

# ---- 3. genuine mixed packing k=2, MPI + Theorem 1 end to end ----
print("== mixed packing k=2, N=4, M=5 ==")
k=2;N=4
packing = [square(0.5,0.5,1.0,0.0), square(1.5,0.5,1.0,0.0), square(0.5,1.5,1.0,0.0),
           square(1.5,1.5,0.75,0.3), square(1.055,1.055,0.1,0.0)]
# verify pairwise disjoint + inside via MC
pts = rng.uniform(0,2,(400000,2))
def inside(sq,pt):
    c,s=np.cos(sq['th']),np.sin(sq['th'])
    u=(pt[:,0]-sq['cx'])*c+(pt[:,1]-sq['cy'])*s
    v=-(pt[:,0]-sq['cx'])*s+(pt[:,1]-sq['cy'])*c
    return (np.abs(u)<sq['d']/2-1e-12)&(np.abs(v)<sq['d']/2-1e-12)
mult = sum(inside(sq,pts).astype(int) for sq in packing)
print(" max multiplicity (should be 1):",mult.max()," inside box:",all(sq['xmin']>-1e-9 and sq['xmax']<2+1e-9 and sq['ymin']>-1e-9 and sq['ymax']<2+1e-9 for sq in packing))
n=500
X0=(np.arange(n)+0.5)/n+1.7e-5; Y0=(np.arange(n)+0.5)/n+2.3e-5
Ptot=np.zeros(n);Qtot=np.zeros(n);Dtot=np.zeros((n,n));Ctot=np.zeros((n,n))
Ssum=0;msum=0
for sq in packing:
    p=pcount(sq,X0);q=qcount(sq,Y0);c=ccount(sq,X0,Y0)
    L=p[:,None]*q[None,:]-c; B=(p[:,None]-1)*(q[None,:]-1)
    Dtot+=np.maximum(L-B,0); Ptot+=p; Qtot+=q; Ctot+=c
    d,th=sq['d'],sq['th']; sg=np.cos(th)+np.sin(th)-1; w=d*(1+sg)
    Ssum+=d*sg
    if th==0: m=0
    elif w<=1: m=d*sg*(2-d-w)
    elif d<=1+sg: m=(1-d)**2
    else: m=-d*sg*(d+w-2)
    msum+=m
eps = sum(sq['d'] for sq in packing)-N
print(" sum c <= N?", Ctot.max()<=N+1e-9, " (max sum c =",Ctot.max(),")")
mpi = (Dtot - (Ptot[:,None]+Qtot[None,:]-2*N-1)).min()
kap = np.maximum(2*N+1-Ptot[:,None]-Qtot[None,:],0).mean()
print(f" MPI min slack (>=0): {mpi:+.3f};  eps={eps:.3f}, S={eps+Ssum:.4f}")
print(f" E[D]={Dtot.mean():.4f} >= 2S-1+kappa = {2*(eps+Ssum)-1+kap:.4f} ?")
print(f" Thm1: 2eps={2*eps:.3f} <= 1 - sum m - kappa = {1-msum-kap:.4f}  (kappa={kap:.4f}, sum m={msum:.4f})")

# ---- 4. Lemma alpha staircase: uncovered in strip vs bound ----
print("== Lemma alpha staircase, unit squares under y=tau x, h=1/4 ==")
h=0.25; X=20.0
for tau in (0.1,0.3,1.0):
    # squares j: span [j,j+1], top = tau*j (top-left corner on the line)
    nx=20000
    xs=(np.arange(nx)+0.5)*X/nx
    F = tau*np.floor(xs)          # top of the unique spanning square
    g = np.minimum(h, tau*xs - F)
    unc = g.mean()*X
    bound = X*min(tau,0.2)/36
    print(f" tau={tau}: uncovered(strip)={unc:.4f}  proven lower bound={bound:.4f}  true/unit={unc/X:.4f} ~ tau/2 pred {min(tau/2, h-h*h/(2*tau)):.4f}")
