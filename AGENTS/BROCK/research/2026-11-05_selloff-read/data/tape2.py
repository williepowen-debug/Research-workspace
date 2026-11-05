import yfinance as yf, pandas as pd, numpy as np, warnings
warnings.filterwarnings('ignore')
W=['ARCC','FSK','OBDC','BIZD']; M=['APO','ARES']; X=['HYG','SPY']
ext=['OWL','BX','KKR','CG','BXSL','GBDC','MAIN','HTGC','GS','MS','KRE','CRWV']
adj=yf.download(W+M+X+ext,period='420d',interval='1d',auto_adjust=True,progress=False)['Close']
ret=adj.pct_change()
print('now',pd.Timestamp.now(tz='America/New_York'),'last',adj.index[-1].date())
idx=adj.index
def fit(names,s):
    f=ret.iloc[s-5-249:s-5+1]
    y=f[names].mean(axis=1)
    A=np.c_[np.ones(len(f)),f['HYG'],f['SPY']]
    b,*_=np.linalg.lstsq(A,y.values,rcond=None)
    r=y.values-A@b
    return b,r.std(ddof=3)
def win(names,s,e):
    b,sd=fit(names,s)
    w=ret.iloc[s+1:e+1]
    act=(1+w[names].mean(axis=1)).prod()-1
    pred=(1+(b[1]*w['HYG']+b[2]*w['SPY'])).prod()-1
    n=len(w); r=act-pred
    return act*100,pred*100,r*100,r/(sd*np.sqrt(n)),b[1],b[2],n
def P(lbl,st,en=None):
    s=idx.searchsorted(pd.Timestamp(st)); e=len(idx)-1 if en is None else idx.searchsorted(pd.Timestamp(en))
    a=win(W,s,e);ax=win(['ARCC','OBDC','BIZD'],s,e);m=win(M,s,e)
    print(f"{lbl} {idx[s].date()}->{idx[e].date()} n={a[6]} HYG {(adj['HYG'].iloc[e]/adj['HYG'].iloc[s]-1)*100:+.2f} SPY {(adj['SPY'].iloc[e]/adj['SPY'].iloc[s]-1)*100:+.2f}")
    print(f"   wrappers act {a[0]:+.2f} pred {a[1]:+.2f} resid {a[2]:+.2f} ({a[3]:+.1f}s)  bH {a[4]:.2f} bS {a[5]:.2f}| exFSK act {ax[0]:+.2f} resid {ax[2]:+.2f} ({ax[3]:+.1f}s)")
    print(f"   managers act {m[0]:+.2f} pred {m[1]:+.2f} resid {m[2]:+.2f} ({m[3]:+.1f}s)  bH {m[4]:.2f} bS {m[5]:.2f}")
    print(f"   W minus M raw {a[0]-m[0]:+.2f}pp  resid spread {a[2]-m[2]:+.2f}pp")
P('TODAY',idx[-2])
P('since 11/3 close','2026-11-03')
P('10/27->10/30 HY 318->344','2026-10-27','2026-10-30')
P('10/27->11/3','2026-10-27','2026-11-03')
P('10/27->today','2026-10-27')
s=len(idx)-2
print('\nname-level today: actual, predicted (250d betas HYG+SPY), resid, z')
for t in W+M+ext:
    a=win([t],s,s+1); print(f"{t:5s} {a[0]:+6.2f} {a[1]:+6.2f} {a[2]:+6.2f} {a[3]:+5.1f}s bH {a[4]:+.2f} bS {a[5]:+.2f}")
# how many sessions in the last 250 had SPY <= -3%
sp=ret['SPY'].iloc[-251:-1]
big=sp[sp<=-0.025]
print('\nprior SPY <=-2.5% days in 250:',[(d.date().isoformat(),round(v*100,2)) for d,v in big.items()])
for d in big.index:
    print(d.date(),'W',round(ret.loc[d,W].mean()*100,2),'M',round(ret.loc[d,M].mean()*100,2))
print('today W',round(ret[W].iloc[-1].mean()*100,2),'M',round(ret[M].iloc[-1].mean()*100,2),'SPY',round(ret['SPY'].iloc[-1]*100,2))
print(adj[['ARCC','FSK','OBDC','BIZD','APO','ARES','SPY']].iloc[-1]/adj[['ARCC','FSK','OBDC','BIZD','APO','ARES','SPY']].loc['2026-11-03']-1)
