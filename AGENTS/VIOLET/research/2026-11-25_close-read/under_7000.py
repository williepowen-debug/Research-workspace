# What VIOLET's instruments show around S&P 7,000 on 11/25 (vendor 1-min bars; not dealer-hedging data)
import yfinance as yf, pandas as pd, numpy as np
D={}
for s in ["^GSPC","^VIX","^VIX9D","^VIX3M","^VIX6M","^VVIX"]:
    h=yf.Ticker(s).history(period="2d",interval="1m"); h.index=h.index.tz_convert("America/New_York")
    h=h[h.index.date==pd.Timestamp("2026-11-25").date()]; D[s]=h["Close"]
df=pd.DataFrame(D).between_time("09:31","16:00").dropna()
print("bars",len(df), df.index[0].strftime("%H:%M"), df.index[-1].strftime("%H:%M"))
df["under"]=df["^GSPC"]<7000
df["r"]=np.log(df["^GSPC"]).diff()
u=df[df.under]
print("minutes closing under 7,000:",len(u), "first",u.index[0].strftime("%H:%M") if len(u) else None,"last",u.index[-1].strftime("%H:%M") if len(u) else None)
df["dV"]=df["^VIX"].diff(); df["dV6"]=df["^VIX6M"].diff()
for n,g in (("under 7,000",df[df.under]),("7,000 to 7,050",df[(df["^GSPC"]>=7000)&(df["^GSPC"]<7050)]),("7,050 and over",df[df["^GSPC"]>=7050])):
    g=g.dropna()
    if len(g)<5: print(n,"n",len(g)); continue
    b=np.polyfit(g.r*100,g.dV,1)[0]
    print(f"{n}: n={len(g)} min-return sd {g.r.std()*1e4:.1f}bp  VIX pts per 1% S&P {b:.2f}  mean VIX {g['^VIX'].mean():.2f} 3M/VIX {(g['^VIX3M']/g['^VIX']).mean():.4f}")
for m in ["09:45","10:00","10:30","11:00","11:20","11:39","12:00","12:30","13:00","14:00","15:00","16:00"]:
    r=df[df.index.strftime("%H:%M")<=m].iloc[-1]; print(m,*(round(r[c],2) for c in D))
# same S&P level, morning vs later
x=df[(df["^GSPC"]>=7005)&(df["^GSPC"]<=7045)]
print("S&P 7,005-7,045: bars",len(x),"VIX median before 10:15",x[x.index.strftime('%H:%M')<'10:15']['^VIX'].median(),"after 10:15",x[x.index.strftime('%H:%M')>='10:15']['^VIX'].median(), "VIX6M",x[x.index.strftime('%H:%M')<'10:15']['^VIX6M'].median(),x[x.index.strftime('%H:%M')>='10:15']['^VIX6M'].median())
