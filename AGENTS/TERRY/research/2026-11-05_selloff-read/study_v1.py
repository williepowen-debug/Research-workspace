import yfinance as yf, pandas as pd, numpy as np
d=yf.download(['SPY','QQQ','RSP','HYG','^VIX','^VIX3M'],start='2003-01-01',auto_adjust=False,progress=False)['Close']
print('bars',d.count().to_dict(), d.index[0].date(), d.index[-1].date())
d=d[d.index<'2026-11-05']
r=d.pct_change()
tr=yf.download(['SPY','QQQ','RSP'],start='2003-01-01',auto_adjust=True,progress=False)['Close']
tr=tr[tr.index<'2026-11-05']
def fwd(s,n): return s.shift(-n)/s-1
out={}
def rep(name,mask,sym='SPY'):
    idx=d.index[mask.fillna(False)]
    # cluster: first event in a 10-session gap
    pos=[d.index.get_loc(i) for i in idx]; keep=[]
    for p in pos:
        if not keep or p-keep[-1]>10: keep.append(p)
    ci=d.index[keep]
    print(f"\n{name}: all days {len(idx)}, clusters(10-session gap) {len(ci)}")
    for lab,ii in (('all',idx),('clusters',ci)):
        for n in (1,5,10,20,30):
            f=fwd(tr[sym],n).reindex(ii).dropna()
            if len(f)==0: continue
            print(f"  {lab:8s} +{n:2d}d {sym}: n={len(f)} med {f.median()*100:+.2f}% mean {f.mean()*100:+.2f}% win {(f>0).mean()*100:.0f}% p10 {f.quantile(.1)*100:+.2f}% worst {f.min()*100:+.2f}%")
    return ci
m1=(r['SPY']<=-0.03)
ci=rep('SPY day <= -3%',m1)
m2=(r['SPY']<=-0.03)&(r['HYG']>-0.01)
ci2=rep('SPY <= -3% AND HYG > -1%',m2)
print(list(ci2.date))
ratio=d['^VIX3M']/d['^VIX']
m3=(r['SPY']<=-0.03)&(r['HYG']>-0.01)&(ratio<1)
ci3=rep('... AND VIX3M/VIX close <1',m3)
print(list(ci3.date))
m4=(r['SPY']<=-0.03)&(r['HYG']<=-0.01)
ci4=rep('SPY <= -3% AND HYG <= -1% (credit followed)',m4)
print(list(ci4.date))
m5=(r['QQQ']<=-0.05)
ci5=rep('QQQ <= -5%',m5,'QQQ'); print(list(ci5.date))
m6=(r['RSP']<=-0.025)&(r['SPY']<=-0.03)&(r['HYG']>-0.01)
rep('RSP measure on same',m2,'RSP')
# HYG drawdown after: did credit follow in next 10d?
idx=d.index[m2.fillna(False)]
pos=[d.index.get_loc(i) for i in idx]; keep=[]
for p in pos:
    if not keep or p-keep[-1]>10: keep.append(p)
hy=[]
for p in keep:
    w=d['HYG'].iloc[p:p+21]
    hy.append((d.index[p].date(), round(r['HYG'].iloc[p]*100,2), round((w.min()/w.iloc[0]-1)*100,2)))
print('HYG next-20d worst from event close'); print(hy)
print('median',np.median([h[2] for h in hy]),'share worse than -3%',np.mean([h[2]<=-3 for h in hy]),len(hy))
