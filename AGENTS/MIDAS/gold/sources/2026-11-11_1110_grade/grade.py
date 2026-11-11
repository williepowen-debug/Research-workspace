"""11/10 gold move on the frozen WQ-451 classifier (letter gold/research/2026-10-23_WQ451-decomposition-letter.md, a35faa6f8),
plus L2 stress count, L3 daily proxy, WQ-451 section-5 lines, SLV/PPLT/PALL band legs, MIDAS-11/13/17 progress (not graded).
Reads only saved raw files here. Frozen parameters copied, not re-fit: beta -0.1526 %/bp, sd 1.402,
stress = S&P <= -1.0% OR VIX >= +2.0 pts, DXY -0.20%. Same code shape as shared/sources/2026-11-06_L819_grade/grade.py."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import json, pandas as pd
P=Path(__file__).resolve().parent
B,SD=-0.1526,1.402
def ser(name):
    j=json.loads((P/f'{name}.json').read_text())['chart']['result'][0]; tz=ZoneInfo(j['meta']['exchangeTimezoneName'])
    d={}
    for t,c in zip(j['timestamp'],j['indicators']['quote'][0]['close']):
        if c is not None: d[pd.Timestamp(datetime.fromtimestamp(t,tz).strftime('%Y-%m-%d'))]=c
    return pd.Series(d).sort_index()
iss=pd.read_excel(P/'GLD_issuer_archive.xlsx',sheet_name='US GLD Historical Archive')
iss.columns=[str(c).strip() for c in iss.columns]
iss['Date']=pd.to_datetime(iss['Date'],format='%d-%b-%Y',errors='coerce'); iss=iss.dropna(subset=['Date']).sort_values('Date').set_index('Date')
for c in ['Closing Price','Tonnes of Gold']: iss[c]=pd.to_numeric(iss[c],errors='coerce')
real=pd.read_csv(P/'treasury_real.csv',parse_dates=['Date']).set_index('Date').sort_index()['10 YR']
nom=pd.read_csv(P/'treasury_nominal.csv',parse_dates=['Date']).set_index('Date').sort_index()
spx,vix,dxy,gcz=ser('GSPC'),ser('VIX'),ser('DX-Y.NYB'),ser('GCZ26.CMX')
t=iss['Tonnes of Gold']; px=iss['Closing Price']
print('issuer last row',px.index[-1].date(),'real last',real.index[-1].date(),'nominal last',nom.index[-1].date(),'spx last',spx.index[-1].date(),'dxy last',dxy.index[-1].date())
print('=== daily classes 11/05 -> last issuer date (frozen classifier)')
days=[d for d in iss.index if pd.Timestamp('2026-11-05')<=d]
rows=[]
for a,b in zip(days[:-1],days[1:]):
    gl=100*(px[b]/px[a]-1); dr=100*(real[b]-real[a]); imp=B*dr; e=gl-imp
    sp=100*(spx[b]/spx[a]-1); dv=vix[b]-vix[a]; dx=100*(dxy[b]/dxy[a]-1); st=bool(sp<=-1.0 or dv>=2.0); dt=round(float(t[b]-t[a]),2)
    if abs(e)<=SD: c='RATE'
    elif e<-SD and st and dt<0: c='LIQUIDATION'
    elif e>SD and st and dx>-0.20: c='HAVEN' if dt>0 else 'UNEXPLAINED-UP (haven leg, tonnes not up)'
    elif e>SD and not st and dx<=-0.20: c='DE-DOLLAR proxy'
    else: c='UNEXPLAINED-'+('DOWN' if e<0 else 'UP')
    rows.append(dict(date=str(b.date()),gld=round(px[b],2),gld_pct=round(gl,2),real10=real[b],d_real_bp=round(dr),implied=round(imp,2),e=round(e,2),e_sd=round(e/SD,2),
      d_nom2y_bp=round(100*(nom['2 Yr'][b]-nom['2 Yr'][a])),d_nom10y_bp=round(100*(nom['10 Yr'][b]-nom['10 Yr'][a])),nom2y=nom['2 Yr'][b],nom10y=nom['10 Yr'][b],
      spx_pct=round(sp,2),dvix=round(dv,2),dxy=round(dxy[b],3),dxy_pct=round(dx,2),stress=st,d_t=dt,t=t[b],gcz=round(gcz.get(b,float('nan')),1),cls=c))
df=pd.DataFrame(rows); df.to_csv(P/'wq451_applied.csv',index=False); print(df.to_string(index=False))
r=df.iloc[-1]; print(f"11/10 share of GLD move explained by real-rate beta: {r.implied}/{r.gld_pct} = {100*r.implied/r.gld_pct:.0f}%  (residual {r.e}, {r.e_sd} sd; RATE band +/-{SD})")
prior=pd.read_csv(P.parent.parent.parent/'shared/sources/2026-11-06_L819_grade/wq451_applied.csv')
allc=pd.concat([prior,df[['date','stress','gld_pct','cls']]],ignore_index=True)
s=allc[allc.stress==True]; print('L2 stress days after 10/22 (incl 11/06-file rows):',len(s),'GLD up on',int((s.gld_pct>0).sum()),'dates',list(s.date))
print('DE-DOLLAR proxy days since 10/22:',list(allc[allc.cls=='DE-DOLLAR proxy'].date),'tonnes 10/22->last',round(t.iloc[-1]-t['2026-10-22'],2))
print('=== WQ-451 section 5 lines')
print('GLD last',px.iloc[-1],'1m down line 360.71 crossed now?',px.iloc[-1]<360.71,'1m up line 391.08 crossed since 10/23?',bool((px['2026-10-23':]>391.08).any()))
print('tonnes last',t.iloc[-1],'vs 3m line 1035.70; min since 10/22',t['2026-10-22':].min())
rr=real['2026-10-22':]; print('real 10Y >=3.00 count since 10/22',int((rr>=3.00).sum()),'max',rr.max(),rr.idxmax().date())
dd=dxy['2026-10-22':]; print('DXY >=105 closes since 10/22',int((dd>=105).sum()),'max',round(dd.max(),3))
print('=== MIDAS-11/13/17 progress (NOT graded; resolve 11/20)')
print('MIDAS-11 baseline 379.69; GLD now',px.iloc[-1],'side', 'NONPOSITIVE' if px.iloc[-1]<=379.69 else 'UP')
print('MIDAS-13 target 378.95; max issuer close 10/26..',px['2026-10-26':].max(),px['2026-10-26':].idxmax().date(),'HIT condition met already?',bool((px['2026-10-26':'2026-11-20']>=378.95).any()))
res=100*(px.iloc[-1]/369.00-1)-(B*100*(real.iloc[-1]-2.64)); print('MIDAS-17 running residual at',px.index[-1].date(),round(res,2),'(GLD',round(100*(px.iloc[-1]/369.00-1),2),'%, real',real.iloc[-1],')')
print('=== bands d200 / dd252 (MIRROR closes)')
for name in ['SLV','PPLT','PALL']:
    c=ser(name); c=c[c.index<=px.index[-1]]
    d=(c/c.rolling(200).mean()-1)*100; dd2=(c/c.rolling(252,min_periods=200).max()-1)*100
    print(name,'last',c.index[-1].date(),round(c.iloc[-1],2),{str(k.date()):round(float(v),2) for k,v in d.iloc[-4:].items()},'dd252',round(float(dd2.iloc[-1]),2))
print('=== named futures (MIRROR vendor Close, uncertified)')
for n in ['GCZ26.CMX','SIZ26.CMX','PLF27.NYM','PAZ26.NYM','HGZ26.CMX','GC=F']:
    c=ser(n); print(n,{str(k.date()):round(v,3) for k,v in c.iloc[-4:].items()})
