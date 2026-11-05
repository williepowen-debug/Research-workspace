#!/usr/bin/env python3
"""Card SIG-W-20261104-055: reconcile the attributed '60% of S&P 500 constituents in bear-market territory'.
Reuses the L616 member list (SSGA holdings as of 10/29). Bars: yfinance, auto_adjust=False (Close = split-adjusted).
Bear-market territory = close at least 20% below the member's highest close (and, separately, highest intraday high)
in the trailing 252 sessions. Survivorship: today's members. Not a monitor, threshold or prediction."""
import csv, pandas as pd, yfinance as yf, json
u=[r for r in csv.DictReader(open('research/2026-10-31_L616_breadth/universe.csv')) if r['index']=='SP500']
t=[r['yf_ticker'] for r in u]
fr=[]
for i in range(0,len(t),150):
    fr.append(yf.download(t[i:i+150],start='2025-08-01',end='2026-11-05',auto_adjust=False,progress=False,threads=True,group_by='column'))
df=pd.concat(fr,axis=1); c=df['Close'].dropna(how='all'); h=df['High'].reindex(c.index)
# remove columns duplicated across chunks if any
c=c.loc[:,~c.columns.duplicated()]; h=h.loc[:,~h.columns.duplicated()]
out={}
hc=c.rolling(252,min_periods=200).max(); hh=h.rolling(252,min_periods=200).max()
dd_c=c/hc-1; dd_h=c/hh-1
for d in ['2026-10-30','2026-11-02','2026-11-03','2026-11-04']:
    v=c.loc[d].notna(); n=int(v.sum())
    a50=(c>c.rolling(50).mean()).loc[d][v].mean()*100; a200=(c>c.rolling(200).mean()).loc[d][v].mean()*100
    out[d]=dict(n=n,bear_close_pct=round(float((dd_c.loc[d][v]<=-0.20).mean()*100),1),bear_highbasis_pct=round(float((dd_h.loc[d][v]<=-0.20).mean()*100),1),
      bear10_close_pct=round(float((dd_c.loc[d][v]<=-0.10).mean()*100),1),above50=round(float(a50),1),above200=round(float(a200),1),
      median_dd_close=round(float(dd_c.loc[d][v].median()*100),1))
print(json.dumps(out,indent=1)); print('failed/missing',len(t)-c.iloc[-1].notna().sum(), list(c.columns[c.iloc[-1].isna()])[:10], 'last bar', c.index[-1])
