"""Refinements for MIDAS-14/15/17 base rates (2026-10-23)."""
import yfinance as yf, pandas as pd, numpy as np
def px(t): return yf.download(t,start="2008-01-01",end="2026-10-23",auto_adjust=False,progress=False)["Close"].squeeze().dropna()
for t,lo,hi,line in [("SLV",-26,-22.5,-20),("PALL",-28.5,-25.5,-25)]:
    s=px(t); d=((s/s.rolling(200).mean()-1)*100).dropna()
    st=[i for i in range(len(d)-7) if lo<=d.iloc[i]<=hi]
    ep=[i for k,i in enumerate(st) if k==0 or i-st[k-1]>7]
    print(f"{t}: P(d200<={line} after 7 | start [{lo},{hi}]) {np.mean([d.iloc[i+7]<=line for i in st]):.2f} n{len(st)}; first-day-per-episode {np.mean([d.iloc[i+7]<=line for i in ep]):.2f} n{len(ep)}")
g=px("GLD")
f=pd.read_csv("https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFII10&cosd=2025-06-01"); f.columns=["d","v"]; f["v"]=pd.to_numeric(f.v,errors="coerce"); f=f.dropna(); f.index=pd.to_datetime(f.d)
j=pd.DataFrame({"g":g,"r":f.v}).dropna(); e=(j.g.pct_change()*100+0.1526*j.r.diff()*100).dropna().loc["2026"]
c=e.rolling(20).sum().dropna(); print(f"M17 2026 only: P(20-session cum residual>0) {(c>0).mean():.2f} n{len(c)}; non-overlap {(c.iloc[::20]>0).mean():.2f} n{len(c.iloc[::20])}")
