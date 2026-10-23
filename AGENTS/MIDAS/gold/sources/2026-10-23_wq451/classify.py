"""WQ-451 decomposition instrument v1 (MIDAS, frozen 2026-10-23 before any forward grade).
Residual e = GLD daily % - BETA * dDFII10 (bp). Thresholds fixed from the 120-pair window ending 2026-10-21 (excludes the 10/22 graded case).
Classes: RATE (|e| <= K*sd) | LIQUIDATION (e < -K*sd, equity stress, GLD tonnes down) | HAVEN (e > +K*sd, equity stress, dollar not falling)
 | DEDOLLAR-PROXY (e > +K*sd, no equity stress, dollar falling) | UNEXPLAINED-DOWN / UNEXPLAINED-UP otherwise.
Equity stress = SPX <= -1.0% OR dVIX >= +2.0 pts. Dollar falling = DXY <= -0.20%. Usage: python3 classify.py panel.csv"""
import sys, pandas as pd
BETA=-0.1526; K=1.0; SPX_STRESS=-1.0; VIX_STRESS=2.0; DXY_FALL=-0.20
df=pd.read_csv(sys.argv[1],index_col=0,parse_dates=True).dropna(subset=["GLD","DFII10"])
d=pd.DataFrame({"gld":df.GLD.pct_change()*100,"dr":df.DFII10.diff()*100,"dxy":df.DXY.pct_change()*100,
  "spx":df.SPX.pct_change()*100,"dvix":df.VIX.diff(),"dton":df.TONNES.diff()}).dropna()
d["e"]=d.gld-BETA*d.dr
base=d.loc[:"2026-10-21"].tail(120); SD=base.e.std()
def cls(r):
    stress=(r.spx<=SPX_STRESS) or (r.dvix>=VIX_STRESS)
    if abs(r.e)<=K*SD: return "RATE"
    if r.e<0: return "LIQUIDATION" if (stress and r.dton<0) else "UNEXPLAINED-DOWN"
    if stress and r.dxy>DXY_FALL: return "HAVEN"
    if (not stress) and r.dxy<=DXY_FALL: return "DEDOLLAR-PROXY"
    return "UNEXPLAINED-UP"
d["cls"]=d.apply(cls,axis=1)
print(f"BETA {BETA} %/bp | residual sd (120 pairs to 2026-10-21) {SD:.3f}% | threshold +/-{K*SD:.3f}%")
print("\n10/22 graded case:"); print(d.loc["2026-10-22"].to_string())
print("\nBase rates, 120-pair window to 10/21:"); print(base.assign(cls=d.cls).cls.value_counts().to_string())
print("\nBase rates, 2025-01 to 2026-10-21:"); print(d.loc[:"2026-10-21"].cls.value_counts().to_string())
w=d.loc["2026-09-04":"2026-10-15"]
print(f"\nWindow 9/3->10/15: GLD {100*(df.GLD['2026-10-15']/df.GLD['2026-09-03']-1):+.2f}%  dDFII10 {100*(df.DFII10['2026-10-15']-df.DFII10['2026-09-03']):+.0f}bp  DXY {100*(df.DXY['2026-10-15']/df.DXY['2026-09-03']-1):+.2f}%  tonnes {df.TONNES['2026-10-15']-df.TONNES['2026-09-03']:+.2f}  sum e {w.e.sum():+.2f}%")
print(w.cls.value_counts().to_string())
print("GLD max close 2026:", df.GLD.loc['2026'].idxmax().date(), round(df.GLD.loc['2026'].max(),2))
print("\nLast 8 sessions:"); print(d.tail(8)[["gld","dr","e","dxy","spx","dvix","dton","cls"]].round(2).to_string())
