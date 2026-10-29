"""WQ-545 leg 1: forward VIX/SPX/OVX after prior OVX/VIX canary fires (2026-10-29).
Fire = ovx.py rule on Cboe history: ratio >= p95 of ratio AND OVX >= p75 of OVX.
Two ladders: (A) full-sample (as the live canary computes, look-ahead) and
(B) expanding as-of-date (no future data, min 500 obs). Episodes: first fire after
>=20 sessions with no fire. Forward windows 5/10/20 sessions from the fire close.
Run from repo root: .venv/bin/python3 AGENTS/VIOLET/research/2026-10-29_WQ545/ovx_fire_study.py"""
import io, urllib.request, pandas as pd, numpy as np, yfinance as yf
def cb(sym):
    u=f"https://cdn.cboe.com/api/global/us_indices/daily_prices/{sym}_History.csv"
    r=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0 research"}),timeout=30).read().decode()
    df=pd.read_csv(io.StringIO(r)); df.columns=[c.upper() for c in df.columns]
    col='CLOSE' if 'CLOSE' in df.columns else sym.upper()
    return pd.Series(df[col].values,index=pd.to_datetime(df['DATE'])).dropna()
ovx,vix=cb('OVX'),cb('VIX')
spx=yf.Ticker('^GSPC').history(period='max',auto_adjust=False)['Close']; spx.index=spx.index.tz_localize(None).normalize()
df=pd.DataFrame({'ovx':ovx,'vix':vix,'spx':spx}).dropna(); df['ratio']=df.ovx/df.vix
df=df[df.index<='2026-10-28']
A=(df.ratio>=df.ratio.quantile(.95))&(df.ovx>=df.ovx.quantile(.75))
rq=df.ratio.expanding(500).quantile(.95); oq=df.ovx.expanding(500).quantile(.75)
B=(df.ratio>=rq)&(df.ovx>=oq)
def episodes(mask):
    idx=np.where(mask.values)[0]; ep=[]; last=-999
    for i in idx:
        if i-last>20: ep.append(i)
        last=i
    return ep
print(f"sample {df.index[0].date()}..{df.index[-1].date()} n={len(df)}; p95 ratio {df.ratio.quantile(.95):.2f}; p75 OVX {df.ovx.quantile(.75):.2f}")
for name,m in (('A full-sample',A),('B as-of-date',B)):
    ep=episodes(m); print(f"\n== {name}: fire days {int(m.sum())}, episodes {len(ep)} (last = 2026-10-28 live, excluded from forwards)")
    rows=[]
    for i in ep:
        d=df.index[i]; r={'date':d.date(),'ratio':round(df.ratio.iloc[i],2),'vix0':df.vix.iloc[i]}
        for h in (5,10,20):
            if i+h<len(df):
                r[f'vix{h}%']=round((df.vix.iloc[i+h]/df.vix.iloc[i]-1)*100,1)
                r[f'spx{h}%']=round((df.spx.iloc[i+h]/df.spx.iloc[i]-1)*100,2)
                r[f'ovx{h}%']=round((df.ovx.iloc[i+h]/df.ovx.iloc[i]-1)*100,1)
        rows.append(r)
    t=pd.DataFrame(rows); print(t.to_string(index=False))
    done=t.dropna(subset=['vix20%'])
    for h in (5,10,20):
        c=t.dropna(subset=[f'vix{h}%'])
        print(f"h={h}: n={len(c)} | VIX median {c[f'vix{h}%'].median():+.1f}% up-share {(c[f'vix{h}%']>0).mean():.0%} | SPX median {c[f'spx{h}%'].median():+.2f}% down-share {(c[f'spx{h}%']<0).mean():.0%} | OVX median {c[f'ovx{h}%'].median():+.1f}%")
# unconditional base rates for comparison
for h in (5,10,20):
    v=(df.vix.shift(-h)/df.vix-1).dropna(); s=(df.spx.shift(-h)/df.spx-1).dropna()
    print(f"UNCONDITIONAL h={h}: VIX up-share {(v>0).mean():.0%} median {v.median()*100:+.1f}% | SPX down-share {(s<0).mean():.0%} median {s.median()*100:+.2f}%")
