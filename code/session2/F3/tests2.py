"""Test 1: tilt-neutrality — tilting WITHOUT shrinking (room available) leaves |Av| unchanged.
Test 2: Theorem F3-C family — 3 units + two squares (one tilted) at random spots in cell (0,0);
        check |Av| = a^2 + b^2 exactly and FCMB margin = 2(1-a-b) >= 0."""
import numpy as np
from rig import stats, validate

print("=== Test 1: pure tilt with clearance (a0 fixed, no shrink) ===")
a, b = 0.5, 0.5
a0 = a / 1.5                      # side fixed; bounding box a0*c <= a for all t<=pi/4? c<=1.415 -> a0*c=0.472<a ok
for t in [0.0, 0.2, 0.4, 0.6, np.pi/4]:
    sq = [(0.5,1.5,1,0.0),(1.5,0.5,1,0.0),(1.5,1.5,1,0.0),
          (a/2, a/2, a0, t), (a + b/2, b/2, b, 0.0)]
    assert validate(sq)
    r = stats(sq, M=700)
    pred = a0*a0 + b*b
    print(f" t={t:.3f}  |Av|={r['avm']:.6f}  pred={pred:.6f}  s={r['s']:.5f}  marg={r['s']-r['avm']:.5f}")

print()
print("=== Test 2: F3-C family, random placements in cell ===")
rng = np.random.default_rng(7)
bad = 0
for trial in range(25):
    aa = rng.uniform(0.2, 0.55)
    t = rng.uniform(0.0, np.pi/4)
    c = np.cos(t) + np.sin(t)
    # tilted square side aa, bounding box w=aa*c; place box uniformly in cell
    w = aa*c
    x0 = rng.uniform(0, 1-w); y0 = rng.uniform(0, 1-w)
    tilt_sq = (x0+w/2, y0+w/2, aa, t)
    # AP square side bb placed in cell, rejection-sample for disjointness
    for _ in range(200):
        bb = rng.uniform(0.15, min(0.9, 1-aa))
        bx = rng.uniform(0, 1-bb); by = rng.uniform(0, 1-bb)
        sq = [(0.5,1.5,1,0.0),(1.5,0.5,1,0.0),(1.5,1.5,1,0.0),
              tilt_sq, (bx+bb/2, by+bb/2, bb, 0.0)]
        if validate(sq):
            break
    else:
        continue
    r = stats(sq, M=500)
    pred = aa*aa + bb*bb
    marg = r['s'] - r['avm']
    predmarg = 2*(1-aa-bb)
    ok = abs(r['avm']-pred) < 3e-3 and abs(marg-predmarg) < 6e-3 and marg > -1e-9
    if not ok:
        bad += 1
        print(f" MISMATCH a={aa:.3f} b={bb:.3f} t={t:.3f} |Av|={r['avm']:.5f} pred={pred:.5f} marg={marg:.5f} predmarg={predmarg:.5f}")
print(f"done, mismatches: {bad} / 25 (mismatch=deviation from |Av|=a^2+b^2 or margin=2(1-a-b))")
