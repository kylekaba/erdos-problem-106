import numpy as np
from fcmb import analyze, feasible

def show(r):
    return {k2: (bool(v) if isinstance(v, (bool, np.bool_)) else round(float(v), 6)) for k2, v in r.items()}

# --- 1. Repeated-offset corner family, k=3: j cells with (1-delta)-squares at same corner,
#        extra square b=delta in the corner notch of one L. FCMB predicted margin j*delta^2.
k = 3
for j, delta in [(2, 0.15), (3, 0.15), (2, 0.3)]:
    dd = 1 - delta
    cells = [(0, 0), (1, 0), (2, 0)][:j]
    sqs = [(cx + dd/2, cy + dd/2, 0, dd) for (cx, cy) in cells]
    # b in the corner notch [1-delta,1]^2 of cell (0,0)
    sqs.append((1 - delta/2, 1 - delta/2, 0, delta))
    used = set(cells)
    sqs += [(ix + 0.5, iy + 0.5, 0, 1) for ix in range(k) for iy in range(k) if (ix, iy) not in used]
    r = analyze(sqs, k, M=900, second_moment=True)
    print(f'REPEATED-OFFSET j={j} delta={delta}: F={r["F"]:.6f} (pred {j*delta**2:.6f}) '
          f'condE_holds={bool(r["condE_holds"])} Eh2={r["Eh2"]:.4f} PZrhs={r["PZ_rhs"]:.4f} feas={feasible(sqs, k)}')

# --- 2. Row config with tilted bottom squares: does tilt rescue FCMB? (shrink to keep feasible)
d3 = 2/3
for t in [0.0, 0.05, 0.1, 0.2]:
    sh = 1/(np.cos(t) + np.sin(t))  # shrink so tilted square width = 2/3
    dd = d3 * sh
    row = [(d3/2, d3/2 * 1.0, t, dd), (1.0, d3/2, t, dd), (2 - d3/2, d3/2, t, dd),
           (0.5, 1.5, 0, 1), (1.5, 1.5, 0, 1)]
    ok = feasible(row, 2)
    r = analyze(row, 2, M=1200)
    print(f'TILTED ROW k=2 t={t}: F={r["F"]:.6f} feas={ok} sumd={r["sumd"]:.4f}')

# --- 3. Family 4: truncation of the n=N+2 violator (N-2 units + 3 half-squares + empty cell), k=3
k = 3
half = 0.5
sqs = [(0.25, 0.25, 0, half), (0.75, 0.25, 0, half), (0.25, 0.75, 0, half)]  # 3 halves in cell (0,0)
# empty cell (1,0); units elsewhere
sqs += [(ix + 0.5, iy + 0.5, 0, 1) for ix in range(3) for iy in range(3) if (ix, iy) not in [(0, 0), (1, 0)]]
r = analyze(sqs, k, M=900, second_moment=True)
print('TRUNCATED N+2-VIOLATOR (3 halves + empty cell) k=3:', show(r), 'feas:', feasible(sqs, k))

# --- 4. Near-truncation without empty cell: 3 halves in cell(0,0), one 1.0 unit moved to
#        straddle: push a "unit" partially into the empty cell? Instead: shrink the empty
#        cell by putting the 4th square of the split there as a full unit -> that's just N units-ish.
#        More interesting: 4-split cell + REMOVE one unit elsewhere and enlarge nothing:
#        n = N-2 + 4 = N+2 -> not allowed. Truncate by merging two halves into one? -> split cell. Skip.

# --- 5. k=2 straddle family second-moment status where FCMB holds (delta small, b in notch, no straddle)
for delta in [0.1, 0.2]:
    dd = 1 - delta
    sqs = [(dd/2, dd/2, 0, dd), (1 + dd/2, dd/2, 0, dd), (1 - delta/2, 1 - delta/2, 0, delta),
           (0.5, 1.5, 0, 1), (1.5, 1.5, 0, 1)]
    r = analyze(sqs, 2, M=1500, second_moment=True)
    print(f'TWO-CELL SAME-OFFSET (no straddle) delta={delta}: F={r["F"]:.6f} (pred {2*delta**2:.4f}) '
          f'condE_holds={bool(r["condE_holds"])} Eh2={r["Eh2"]:.4f} PZrhs={r["PZ_rhs"]:.4f}')
