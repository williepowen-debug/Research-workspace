"""Intraday 5-minute path, 2026-10-30 regular session (MIRROR Yahoo). Descriptive only."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import json, pandas as pd, numpy as np
P=Path(__file__).resolve().parent; ET=ZoneInfo('America/New_York')
S={};V={}
for f in sorted(P.glob('intraday_*.json')):
    r=json.loads(f.read_text())['chart']['result'][0]
    q=r['indicators']['quote'][0]
    idx=[datetime.fromtimestamp(t,ET) for t in r['timestamp']]
    s=pd.Series(q['close'],index=idx,dtype=float); v=pd.Series(q['volume'],index=idx,dtype=float)
    S[r['meta']['symbol']]=s; V[r['meta']['symbol']]=v
df=pd.DataFrame(S); vol=pd.DataFrame(V)
day=df[(df.index.strftime('%Y-%m-%d')=='2026-10-30')&(df.index.strftime('%H:%M')>='09:30')&(df.index.strftime('%H:%M')<'16:00')]
out={}
prev={}
for c in df.columns:
    s=df[c].dropna(); p=s[s.index.strftime('%Y-%m-%d')<'2026-10-30']
    prev[c]=float(p.iloc[-1]) if len(p) else None
path=day.ffill()
for c in path.columns:
    s=path[c].dropna()
    if not len(s) or prev[c] is None: continue
    chk={}
    for hm in ['09:30','10:00','10:30','11:00','12:00','13:00','13:30','14:00','15:00','15:55']:
        x=s[s.index.strftime('%H:%M')<=hm]
        if len(x): chk[hm]=round(100*(x.iloc[-1]/prev[c]-1),2)
    out[c]=dict(prev_last_bar=prev[c],cum_pct_by_time=chk,low_time=s.idxmin().strftime('%H:%M'))
r=path.pct_change().iloc[1:]
cor={}
for a in ['SPY','QQQ','DX-Y.NYB','^TNX','^VIX','TLT']:
    if a in r and 'GLD' in r: cor[f'GLD_{a}']=float(r['GLD'].corr(r[a]))
cor['GCZ26_SPY']=float(r['GCZ26.CMX'].corr(r['SPY'])) if 'GCZ26.CMX' in r else None
out['corr_5m_regular_session']=cor; out['n_5m_bars']=int(len(r))
# same for prior four sessions
prior={}
for d in sorted(set(df.index.strftime('%Y-%m-%d')))[:-1]:
    x=df[(df.index.strftime('%Y-%m-%d')==d)&(df.index.strftime('%H:%M')>='09:30')&(df.index.strftime('%H:%M')<'16:00')].ffill().pct_change().iloc[1:]
    if len(x)>20: prior[d]=dict(GLD_SPY=float(x['GLD'].corr(x['SPY'])),GLD_QQQ=float(x['GLD'].corr(x['QQQ'])),n=int(len(x)))
out['prior_sessions_5m_corr']=prior
gv=vol['GLD'].groupby(vol.index.strftime('%Y-%m-%d')).sum()
out['GLD_regular_volume_by_day_5m_sum']={k:float(v) for k,v in gv.items()}
(P/'intraday_summary.json').write_text(json.dumps(out,indent=1)+'\n'); print(json.dumps(out,indent=1))
