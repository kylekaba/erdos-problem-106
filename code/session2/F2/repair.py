import numpy as np, json, glob, sys
from fcmb import analyze, feasible, sat_disjoint, corners

def repair(squares, k, tol=1e-9):
    """Greedy: keep each square, shrink it (about its center) until it fits T and
    is disjoint from all previously accepted squares. Returns exactly feasible packing."""
    acc = []
    for (cx, cy, th, d) in squares:
        # clamp center into T
        cx = min(max(cx, 0.0), k); cy = min(max(cy, 0.0), k)
        lo, hi = 0.0, d
        def ok(dd):
            sq = (cx, cy, th, dd)
            P = corners(*sq)
            if P.min() < -tol or P.max() > k + tol:
                return False
            return all(sat_disjoint(sq, o, tol=0.0) for o in acc)
        if ok(d):
            acc.append((cx, cy, th, d)); continue
        for _ in range(60):
            mid = (lo + hi) / 2
            if ok(mid): lo = mid
            else: hi = mid
        acc.append((cx, cy, th, lo * (1 - 1e-12)))
    return acc

if __name__ == '__main__':
    k = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    fn = sys.argv[2]
    sqs = json.load(open(fn))
    rep = repair([tuple(s) for s in sqs], k)
    print('feasible after repair:', feasible(rep, k, tol=1e-9))
    r = analyze(rep, k, M=1600)
    print('F:', float(r['F']), 'piG:', float(r['piG']), 's:', float(r['s']), 'sumd:', float(r['sumd']))
    print('config:', [tuple(round(float(v), 8) for v in sq) for sq in rep])
