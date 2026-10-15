import yfinance as yf, warnings, numpy as np, pandas as pd; warnings.filterwarnings('ignore')
T=['GETY','OPTU','RXT','IHRT','SPY']
d=yf.download(T,start='2026-02-25',end='2026-10-15',auto_adjust=True,progress=False)['Close']
print('last rows:'); print(d.tail(3).round(3).to_string())
r=d.pct_change()
fit=r.loc['2026-03-02':'2026-09-23']
sess=['2026-10-02','2026-10-05','2026-10-06','2026-10-07','2026-10-08','2026-10-09','2026-10-13']
sec=['2026-09-25','2026-09-28','2026-09-29','2026-09-30','2026-10-01']
for t in ['GETY','OPTU','ATUS','RXT','IHRT']:
    if t not in r or r[t].dropna().empty: print(t,'NO DATA'); continue
    f=fit[[t,'SPY']].dropna()
    if len(f)<50: print(t,'short fit',len(f)); continue
    b=np.cov(f[t],f['SPY'])[0,1]/np.var(f['SPY'],ddof=1); s=(f[t]-b*f['SPY']).std(ddof=1)
    z=[(r.loc[x,t]-b*r.loc[x,'SPY'])/s if x in r.index else np.nan for x in sess]
    zs=[(r.loc[x,t]-b*r.loc[x,'SPY'])/s if x in r.index else np.nan for x in sec]
    print(f"{t}: n_fit={len(f)} beta={b:.2f} sigma={100*s:.2f}%  primary z: "+' '.join(f'{v:+.2f}' for v in z)+f"  | <=-1.0: {sum(v<=-1.0 for v in z)}/7  |z|<=0.3: {sum(abs(v)<=0.3 for v in z)}/7 | secondary z: "+' '.join(f'{v:+.2f}' for v in zs))
