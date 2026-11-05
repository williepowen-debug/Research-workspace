import yfinance as yf, pandas as pd, numpy as np
c=yf.download(['SPY','QQQ','RSP','HYG','^VIX','^VIX3M'],start='2003-01-01',auto_adjust=False,progress=False)['Close']
a=yf.download(['SPY','QQQ','RSP'],start='2003-01-01',auto_adjust=True,progress=False)['Close']
c=c[c.index<'2026-11-05']; a=a[a.index<'2026-11-05']
r=c.pct_change(); ratio=c['^VIX3M']/c['^VIX']
def clus(mask,gap=10):
    pos=np.flatnonzero(mask.fillna(False).values); k=[]
    for p in pos:
        if not k or p-k[-1]>gap: k.append(p)
    return k
def show(name,k,s='SPY',ns=(5,10,20,29)):
    line=f"{name:52s} n={len(k):2d}"
    for n in ns:
        f=[a[s].iloc[p+n]/a[s].iloc[p]-1 for p in k if p+n<len(a)]
        if f: line+=f" | +{n}d med {np.median(f)*100:+.1f}% win {np.mean(np.array(f)>0)*100:.0f}%"
    print(line)
for spx,hy in ((-.03,-.01),(-.025,-.01),(-.035,-.01),(-.03,-.0075),(-.03,-.005)):
    m=(r['SPY']<=spx)&(r['HYG']>hy); k=clus(m); show(f"SPY<={spx:.3f} HYG>{hy:.4f} all",k)
    k2=[p for p in k if not (c.index[p].year in (2008,2009))]; show(f"   ex-2008/09",k2)
    m=(r['SPY']<=spx)&(r['HYG']<=hy); k=clus(m); show(f"SPY<={spx:.3f} HYG<={hy:.4f} (credit with it)",k)
    k2=[p for p in k if not (c.index[p].year in (2008,2009))]; show(f"   ex-2008/09",k2)
base=(r['SPY']<=-.03)&(r['HYG']>-.01); k=clus(base)
print('\nevents:',[str(c.index[p].date()) for p in k])
print('per-event SPY +20d TR / HYG min 29d / HYG end29 / HYG end48')
for p in k:
    f=a['SPY'].iloc[p+20]/a['SPY'].iloc[p]-1
    w=c['HYG'].iloc[p:p+49]
    print(c.index[p].date(), f"{f*100:+.1f}%", f"HYGday {r['HYG'].iloc[p]*100:+.2f}", f"min29 {(c['HYG'].iloc[p:p+30].min()/c['HYG'].iloc[p]-1)*100:+.1f}", f"end29 {(c['HYG'].iloc[p+29]/c['HYG'].iloc[p]-1)*100:+.1f}", f"end48 {(c['HYG'].iloc[p+48]/c['HYG'].iloc[p]-1)*100:+.1f}")
e=[(c['HYG'].iloc[p+48]/c['HYG'].iloc[p]-1)*100 for p in k]; print('HYG end48 med',np.median(e),'share<=-1.4',np.mean(np.array(e)<=-1.4),'share<=-4.1',np.mean(np.array(e)<=-4.1))
mn=[(c['HYG'].iloc[p:p+49].min()/c['HYG'].iloc[p]-1)*100 for p in k]; print('HYG min48 med',np.median(mn),'share<=-1.4',np.mean(np.array(mn)<=-1.4),'share<=-3',np.mean(np.array(mn)<=-3))
k2=[p for p in k if c.index[p].year not in (2008,2009)]
e=[(c['HYG'].iloc[p+48]/c['HYG'].iloc[p]-1)*100 for p in k2]; mn=[(c['HYG'].iloc[p:p+49].min()/c['HYG'].iloc[p]-1)*100 for p in k2]
print('ex0809 n',len(k2),'end48 med',round(np.median(e),2),'share<=-1.4',np.mean(np.array(e)<=-1.4),'min48 med',round(np.median(mn),2),'share min<=-3',np.mean(np.array(mn)<=-3))
# patient entry: first red SPY day at or after event+1 with VIX3M/VIX>=1, within 20 sessions
print('\npatient entry after each event (first red day with VIX3M/VIX>=1.00, 20-session limit)')
def patient(k,req_ratio=True):
    res=[]
    for p in k:
        for q in range(p+1,min(p+21,len(c)-30)):
            if r['SPY'].iloc[q]<0 and (ratio.iloc[q]>=1.0 if req_ratio else True):
                res.append(q);break
    return res
for nm,kk in (('all calm-credit',k),('ex-08/09',k2),('all SPY<=-3% clusters',clus(r['SPY']<=-.03))):
    q=patient(kk); show(nm+' patient',q)
    print('   filled',len(q),'of',len(kk),[str(c.index[x].date()) for x in q][:14])
print('\nbaseline any day SPY +20d/+29d med/win:')
for n in (20,29):
    f=(a['SPY'].shift(-n)/a['SPY']-1).dropna(); print(n,round(f.median()*100,2),round((f>0).mean()*100,1),len(f))
