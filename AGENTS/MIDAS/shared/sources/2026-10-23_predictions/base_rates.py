"""Base rates for MIDAS-13..17 (registered 2026-10-23). Yahoo MIRROR unadjusted Close; frozen COT reference for gold."""
import yfinance as yf, pandas as pd, numpy as np
def px(t,start="2008-01-01"): return yf.download(t,start=start,end="2026-10-23",auto_adjust=False,progress=False)["Close"].squeeze().dropna()
g=px("GLD")
# MIDAS-13: from a close, any close in sessions t+2..t+21 >= +2.70%
def touch(s,up,a=2,b=21):
    r=[]
    for i in range(len(s)-b):
        w=s.iloc[i+a:i+b+1]; r.append((w.max()/s.iloc[i]-1)*100>=up)
    return np.mean(r),len(r)
for lab,s in [("GLD 2008+",g),("GLD 2025+",g.loc["2025":])]:
    p,n=touch(s,2.70); print(f"M13 {lab}: P(any close t+2..t+21 >= +2.70%) {p:.2f} n{n}")
r1=g.pct_change()*100
idx=[i for i in range(len(g)-21) if r1.iloc[i]<=-2.0]
print(f"M13 after a <=-2% day (2008+): {np.mean([(g.iloc[i+2:i+22].max()/g.iloc[i]-1)*100>=2.70 for i in idx]):.2f} n{len(idx)}")
# MIDAS-14/15: d200 still beyond line 7 sessions later, conditional on starting band
for t,lo,hi,line in [("SLV",-27,-21,-20),("PALL",-30,-24,-25)]:
    s=px(t); d=(s/s.rolling(200).mean()-1)*100; d=d.dropna()
    st=[i for i in range(len(d)-7) if lo<=d.iloc[i]<=hi]
    print(f"{t}: P(d200 <= {line} after 7 sessions | start in [{lo},{hi}]) {np.mean([d.iloc[i+7]<=line for i in st]):.2f} n{len(st)} (overlapping starts)")
# MIDAS-17: 20-session cumulative residual > 0, beta -0.1526 %/bp, GLD vs DFII10
f=pd.read_csv("https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFII10&cosd=2010-01-01"); f.columns=["d","v"]; f["v"]=pd.to_numeric(f.v,errors="coerce"); f=f.dropna(); f.index=pd.to_datetime(f.d)
j=pd.DataFrame({"g":g,"r":f.v}).dropna()
e=(j.g.pct_change()*100+0.1526*j.r.diff()*100).dropna()
for lab,x in [("2010+",e),("2025+",e.loc["2025":])]:
    c=x.rolling(20).sum().dropna(); print(f"M17 {lab}: P(20-session cum residual > 0) {(c>0).mean():.2f} n{len(c)} overlapping; non-overlap {(c.iloc[::20]>0).mean():.2f} n{len(c.iloc[::20])}")
# MIDAS-16: gold COT net/OI two vintages later lower than current; and after >=4 consecutive declines
h=pd.read_csv("AGENTS/MIDAS/sources/cot_gold_history_2010_2026.tsv",sep="\t",comment="#")
v=h.net_over_oi_pct.values
print(f"M16 P(v[t+2]<v[t]) {np.mean(v[2:]<v[:-2]):.2f} n{len(v)-2}")
dec=[i for i in range(4,len(v)-2) if all(v[i-k]<v[i-k-1] for k in range(4))]
print(f"M16 after 4 straight declines: P(v[t+2]<v[t]) {np.mean([v[i+2]<v[i] for i in dec]):.2f} n{len(dec)}")
hi=[i for i in range(len(v)-2) if v[i]>=50]
print(f"M16 when v>=50: P(v[t+2]<v[t]) {np.mean([v[i+2]<v[i] for i in hi]):.2f} n{len(hi)}")
