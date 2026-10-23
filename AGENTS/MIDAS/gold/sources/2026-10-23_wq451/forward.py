"""Forward-residual base rates after each class (MIDAS WQ-451, 2026-10-23). Reuses classify.py definitions.
Cumulative residual over next H sessions after a classified day, history 2025-01 -> 2026-10-21."""
import sys, runpy, io, contextlib
with contextlib.redirect_stdout(io.StringIO()): g=runpy.run_path(sys.argv[0].replace("forward.py","classify.py"))
d=g["d"]; h=d.loc[:"2026-10-21"].copy()
for H in (5,10):
    h[f"fwd{H}"]=h.e[::-1].rolling(H).sum()[::-1].shift(-1)
    h[f"tfwd{H}"]=h.dton[::-1].rolling(H).sum()[::-1].shift(-1)
print(h.groupby("cls")[["fwd5","fwd10","tfwd10"]].agg(["mean","count"]).round(2).to_string())
L=h[h.cls=="LIQUIDATION"][["gld","dr","e","spx","dton","fwd5","fwd10","tfwd10"]].round(2)
print("\nLIQUIDATION days:"); print(L.to_string())
print("\nshare fwd10>0 after LIQUIDATION:", round((L.fwd10.dropna()>0).mean(),2), "n", L.fwd10.notna().sum())
print("unconditional share fwd10>0:", round((h.fwd10.dropna()>0).mean(),2), "n", h.fwd10.notna().sum())
