"""Family A: tilted split-cell. 3 units + b AP + a-square tilted (shrunk a/c)."""
import numpy as np
from rig import stats, compare_inscribed, validate

def famA(a, t):
    b = 1 - a
    c = np.cos(t) + np.sin(t)
    at = a / c
    sq = [
        (0.5, 1.5, 1.0, 0.0),
        (1.5, 0.5, 1.0, 0.0),
        (1.5, 1.5, 1.0, 0.0),
        (a/2, a/2, at, t),            # tilted, inscribed in [0,a]^2
        ((a+1)/2 if False else a + b/2, b/2, b, 0.0),  # [a,1]x[0,b]
    ]
    return sq, 3

hdr = ("{:>5} {:>6} | {:>8} {:>8} {:>8} {:>9} | {:>9} {:>8} {:>8} | {:>8} {:>7} {:>6}"
       .format('a','t','|Av|','s','marg','2a(1-1/c)','AvminusA','areaR','piRnoG','ds','red_ok','sub_v'))
print(hdr)
for a in [0.30, 0.37, 0.50, 0.62]:
    for t in [0.0, 0.15, 0.30, 0.45, 0.60, np.pi/4]:
        sq, ti = famA(a, t)
        assert validate(sq), (a, t)
        r = compare_inscribed(sq, ti, M=600)
        c = np.cos(t) + np.sin(t)
        pred = 2*a*(1 - 1/c)
        # reduction requirement: margin' >= ds + |Av\Av'| ?
        red_ok = r['margin2'] - (r['ds'] + r['diff'])
        print(f"{a:5.2f} {t:6.3f} | {r['avm']:8.5f} {r['s']:8.5f} {r['margin']:8.5f} {pred:9.5f} | "
              f"{r['diff']:9.5f} {r['areaR']:8.5f} {r['piRnG']:8.5f} | {r['ds']:8.5f} {red_ok:7.4f} {r['subset_viol']:6.4f}")
