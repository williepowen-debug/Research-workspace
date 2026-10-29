import json, pandas as pd, numpy as np, datetime, yfinance as yf
df=pd.read_pickle('df.pkl')
k=json.load(open('kre.json')); kre=pd.Series([v for _,v in k['rows']],index=pd.to_datetime([a for a,_ in k['rows']]))
sp=yf.download('SPY',start='2006-06-01',progress=False,auto_adjust=True)['Close']; sp=sp.iloc[:,0] if hasattr(sp,'columns') else sp
sp=sp[sp.index<pd.Timestamp('2026-10-28')]
ch6=df.b.pct_change(6)*100; cur=ch6.iloc[-1]
def fwd(series,t,n):
    i=series.index.searchsorted(t)
    if i+n>=len(series): return np.nan
    return (series.iloc[i+n]/series.iloc[i]-1)*100
def episodes(th):
    hits=ch6.loc['2006-06-22':][ch6.loc['2006-06-22':]>=th]
    eps=[];last=None
    for t in hits.index:
        if last is None or (t-last).days>182: eps.append(t)
        last=t
    return eps
for th in [cur, 8.0]:
    eps=episodes(th); print(f"\n== Episodes: 6w small-bank borrowing rise >= {th:.1f}% (first week of each; >26w apart), since mid-2006: n={len(eps)}")
    rows=[]
    for t in eps:
        rel=t+pd.Timedelta(days=9)
        r={'week':t.date(),'6w%':round(ch6[t],1),'ratio%':round(df.b[t]/df.ta[t]*100,2)}
        for n,lab in [(21,'1m'),(63,'3m'),(126,'6m')]:
            a=fwd(kre,rel,n); b=fwd(sp,rel,n); r['KRE'+lab]=round(a,1); r['xs'+lab]=round(a-b,1) if a==a and b==b else np.nan
        j=df.index.searchsorted(t); 
        r['bor+13w%']=round((df.b.iloc[j+13]/df.b.iloc[j]-1)*100,1) if j+13<len(df) else np.nan
        r['dep+13w%']=round((df.dep.iloc[j+13]/df.dep.iloc[j]-1)*100,1) if j+13<len(df) else np.nan
        rows.append(r)
    t=pd.DataFrame(rows); print(t.to_string(index=False))
    ok=t.dropna(subset=['xs3m'])
    print(f"  median excess vs SPY: 1m {ok.xs1m.median():+.1f}  3m {ok.xs3m.median():+.1f}  6m {t.xs6m.dropna().median():+.1f}; share KRE lagged SPY at 3m: {(ok.xs3m<0).mean()*100:.0f}% (n={len(ok)})")
# unconditional
idx=kre.index[(kre.index>='2006-07-01')&(kre.index<'2026-04-01')]
xs=[]
for t in idx[::5]:
    a=fwd(kre,t,63); b=fwd(sp,t,63)
    if a==a and b==b: xs.append(a-b)
xs=np.array(xs); print(f"\n== Unconditional KRE-SPY 3m excess (weekly samples 2006-2026): median {np.median(xs):+.1f}, share negative {(xs<0).mean()*100:.0f}%, n={len(xs)}")
