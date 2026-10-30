"""Liquidation-vs-repricing arithmetic, 2026-10-30. Reads only saved raw files in this directory."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import json,math
import pandas as pd, numpy as np
P=Path(__file__).resolve().parent
T='2026-10-30'; out={'target':T}
S={}
for f in sorted(P.glob('*.json')):
    if f.name.startswith(('access','summary','intraday')): continue
    r=json.loads(f.read_text())['chart']['result'][0]; tz=ZoneInfo(r['meta']['exchangeTimezoneName'])
    q=r['indicators']['quote'][0]
    rows={}
    for i,t in enumerate(r['timestamp']):
        d=datetime.fromtimestamp(t,tz)
        c=q['close'][i]
        if c is None: continue
        rows.setdefault(d.strftime('%Y-%m-%d'),[]).append((d.strftime('%H:%M:%S'),c,q['low'][i],q['high'][i]))
    ser={}
    for d,v in rows.items():
        daily=[x for x in v if x[0]=='00:00:00'] or v
        ser[d]=daily[0]
    s=pd.Series({pd.Timestamp(k):v[1] for k,v in ser.items()}).sort_index()
    S[r['meta']['symbol']]=s
    out.setdefault('lows',{})[r['meta']['symbol']]={k:v[2] for k,v in ser.items() if k==T}
px=pd.DataFrame(S)
px.to_csv(P/'closes.csv')
last=px.loc[:T].iloc[-6:]
out['last6_closes']={c:{str(k.date()):(None if pd.isna(v) else round(float(v),4)) for k,v in last[c].items()} for c in px.columns}
def pct(c,a,b):
    s=px[c].dropna(); return float(100*(s.loc[:b].iloc[-1]/s.loc[:a].iloc[-1]-1))
day={}
for c in px.columns:
    s=px[c].dropna().loc[:T]
    if len(s)<10: day[c]={'note':'series too short, excluded','n':int(len(s))}; continue
    if s.index[-1]!=pd.Timestamp(T): day[c]={'note':'no row for target','last':str(s.index[-1].date())}; continue
    day[c]=dict(close=float(s.iloc[-1]),prev_date=str(s.index[-2].date()),prev=float(s.iloc[-2]),pct=float(100*(s.iloc[-1]/s.iloc[-2]-1)))
out['day']=day
# GLD history vs July low
g=px['GLD'].dropna().loc[:T]
out['gld_july16']=float(g.loc['2026-07-16'])
below=g[g<g.iloc[-1]]
out['gld_last_close_below_today']=str(below.index[-1].date()) if len(below) else None
out['gld_peak']=dict(date=str(g.idxmax().date()),close=float(g.max()),dd_pct=float(100*(g.iloc[-1]/g.max()-1)))
out['gld_5d_pct']=float(100*(g.iloc[-1]/g.iloc[-6]-1))
# 5-session return percentile vs pre-2026? use available (2025+) only
# daily returns & beta to SPY, rolling
r=px[['GLD','SPY','QQQ','GDX','SLV','TLT','DX-Y.NYB','^VIX','BTC-USD','HYG']].pct_change(fill_method=None).loc[:T]
rr=r.dropna(subset=['GLD','SPY'])
for n in (20,60,120):
    w=rr.iloc[-n:]
    out.setdefault('corr',{})[f'GLD_SPY_{n}']=float(w['GLD'].corr(w['SPY']))
    out['corr'][f'GLD_QQQ_{n}']=float(w['GLD'].corr(w['QQQ']))
    out['corr'][f'GLD_DXY_{n}']=float(w['GLD'].corr(w['DX-Y.NYB']))
    b=np.polyfit(w['SPY'],w['GLD'],1)[0]; out.setdefault('beta',{})[f'GLD_on_SPY_{n}']=float(b)
    out['beta'][f'GDX_on_GLD_{n}']=float(np.polyfit(w['GLD'],w['GDX'],1)[0])
    out['beta'][f'SLV_on_GLD_{n}']=float(np.polyfit(w['GLD'],w['SLV'],1)[0])
# today's z-scores against trailing 120 (excluding today)
h=rr.iloc[-121:-1]; t=rr.iloc[-1]
out['z_today_vs_120']={c:float((t[c]-h[c].mean())/h[c].std()) for c in rr.columns if not pd.isna(t[c])}
# GLD residual vs SPY model
b=np.polyfit(h['SPY'],h['GLD'],1); out['gld_spy_model_today']=dict(beta=float(b[0]),alpha=float(b[1]),predicted_pct=float(100*(b[0]*t['SPY']+b[1])),actual_pct=float(100*t['GLD']),residual_pct=float(100*(t['GLD']-(b[0]*t['SPY']+b[1]))))
# rank of today's GLD return in 2025+ sample
gr=r['GLD'].dropna()
out['gld_today_rank']=dict(n=int(len(gr)),worse_or_equal=int((gr<=gr.iloc[-1]).sum()))
# days in sample where GLD<-2.5% : what did SPY/real yields do
big=gr[gr<-0.025]
out['gld_big_down_days']={str(k.date()):dict(gld=float(100*v),spy=float(100*r['SPY'].get(k,np.nan)),gdx=float(100*r['GDX'].get(k,np.nan)),slv=float(100*r['SLV'].get(k,np.nan)),vix=float(100*r['^VIX'].get(k,np.nan)),dxy=float(100*r['DX-Y.NYB'].get(k,np.nan)) if not pd.isna(r['DX-Y.NYB'].get(k,np.nan)) else None) for k,v in big.items()}
# rates (PRIMARY Treasury)
re_=pd.read_csv(P/'treasury_real.csv',parse_dates=['Date']).set_index('Date').sort_index()['10 YR']
no=pd.read_csv(P/'treasury_nominal.csv',parse_dates=['Date']).set_index('Date').sort_index()
out['real10']={str(k.date()):float(v) for k,v in re_.loc['2026-10-08':].items()}
out['nom10']={str(k.date()):float(v) for k,v in no['10 Yr'].loc['2026-10-08':].items()}
out['nom2']={str(k.date()):float(v) for k,v in no['2 Yr'].loc['2026-10-08':].items()}
# windows
W=[('2026-07-16',T),('2026-10-09',T),('2026-10-22',T),('2026-10-29',T),('2026-10-23',T)]
out['windows']={}
for a,b_ in W:
    out['windows'][f'{a}->{b_}']=dict(real10_bp=float(100*(re_.loc[:b_].iloc[-1]-re_.loc[:a].iloc[-1])),nom10_bp=float(100*(no['10 Yr'].loc[:b_].iloc[-1]-no['10 Yr'].loc[:a].iloc[-1])),**{f'{c}_pct':pct(c,a,b_) for c in ['GLD','SPY','QQQ','GDX','SLV','TLT','DX-Y.NYB','BTC-USD','HYG']})
# issuer tonnes
iss=pd.read_excel(P/'GLD_issuer_archive.xlsx',sheet_name='US GLD Historical Archive')
iss['Date']=pd.to_datetime(iss['Date'],format='%d-%b-%Y'); iss=iss.sort_values('Date').set_index('Date')
for c in ['Closing Price','Tonnes of Gold']: iss[c]=pd.to_numeric(iss[c],errors='coerce')
i=iss.dropna(subset=['Tonnes of Gold'])
tail=i.loc['2026-10-01':]
out['issuer']={str(k.date()):dict(close=None if pd.isna(v['Closing Price']) else float(v['Closing Price']),tonnes=float(v['Tonnes of Gold'])) for k,v in tail.iterrows()}
tt=i['Tonnes of Gold']
out['issuer_latest']=dict(date=str(tt.index[-1].date()),tonnes=float(tt.iloc[-1]),d1=float(tt.iloc[-1]-tt.iloc[-2]),since_0930=float(tt.iloc[-1]-tt.loc[:'2026-09-30'].iloc[-1]),since_0716=float(tt.iloc[-1]-tt.loc[:'2026-07-16'].iloc[-1]),since_1021=float(tt.iloc[-1]-tt.loc[:'2026-10-21'].iloc[-1]),max_date=str(tt.loc['2026-01-01':].idxmax().date()),max=float(tt.loc['2026-01-01':].max()))
(P/'summary.json').write_text(json.dumps(out,indent=1,default=str)+'\n')
print(json.dumps(out,indent=1,default=str))
