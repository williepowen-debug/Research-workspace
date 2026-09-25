# 2026-09-25 BOND WQ-290: WQ-157 leg-2 instrument re-run on the CORRECTED trade-date window.
# Uses monitors/fr2004_join.join() AS FIXED (PRE < auction <= POST) plus the same permutation
# setup as the 9/17 ad-hoc test: median +5-session DGS30 change, paired vs unpaired I-prime fires,
# 20,000 resamples, seed 20260917, two-sided on |median difference|. Run from AGENTS/BOND with the venv.
import sys, random, statistics as st, io, contextlib
sys.path.insert(0, "monitors"); sys.path.insert(0, "../../FORGE/tools/market-data")
import fr2004_join as J
with contextlib.redirect_stdout(io.StringIO()):
    fr, _ = J.fr2004_pooled(); aucs = J.auctions_with_iprime()
j = J.join(aucs, fr)
s = J.dgs30_series(); idx = {d: i for i, (d, _) in enumerate(s)}
def fwd(ds, k):
    i = idx.get(ds)
    return None if i is None or i + k >= len(s) else 100 * (s[i + k][1] - s[i][1])
def perm(x, y, n=20000, seed=20260917):
    rng = random.Random(seed); obs = st.median(x) - st.median(y); pool = x + y; k = len(x); c = 0
    for _ in range(n):
        rng.shuffle(pool)
        if abs(st.median(pool[:k]) - st.median(pool[k:])) >= abs(obs) - 1e-12: c += 1
    return obs, (c + 1) / (n + 1)
legs = {"long-end TOTAL > $1B": lambda a: a["d_long"] > 1.0, "long-end TOTAL > 0": lambda a: a["d_long"] > 0,
        "11-21Y > 0": lambda a: a["d_1121"] > 0, ">21Y > 0": lambda a: a["d_21"] > 0}
print(f"n joined = {len(j)}  I' fired = {sum(a['fired'] for a in j)}  frontier auction = {max(a['date'] for a in j)}")
for name, leg in legs.items():
    P = [v for v in (fwd(a["date"].isoformat(), 5) for a in j if a["fired"] and leg(a)) if v is not None]
    U = [v for v in (fwd(a["date"].isoformat(), 5) for a in j if a["fired"] and not leg(a)) if v is not None]
    N = [v for v in (fwd(a["date"].isoformat(), 5) for a in j if not a["fired"]) if v is not None]
    d1, p1 = perm(P, U); d2, p2 = perm(P, N)
    print(f"{name:22} paired n={len(P):2} med {st.median(P):+5.1f} | unpaired n={len(U):2} med {st.median(U):+5.1f} | "
          f"no-fire n={len(N)} med {st.median(N):+5.1f} | P-U {d1:+5.1f}bp p={p1:.3f} | P-nofire {d2:+5.1f}bp p={p2:.3f}")
