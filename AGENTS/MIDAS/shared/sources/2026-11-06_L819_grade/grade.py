"""WQ-451 L1 (DOCKET L819), MIDAS-14/15, 10/30 class, L2 count, band state. Reads only saved raw files here.
Frozen parameters copied, not re-fit: beta -0.1526 %/bp, sd 1.402, stress = S&P <= -1.0% OR VIX >= +2.0 pts, DXY -0.20%."""
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
spx,vix,dxy=ser('GSPC'),ser('VIX'),ser('DX-Y.NYB')
print('=== L1 (letter section 4)')
win=spx['2026-10-22':'2026-11-05']; print('S&P 10/21',round(spx['2026-10-21'],2),'max close 10/22..11/05',round(win.max(),2),win.idxmax().date(),'sessions',len(win))
t=iss['Tonnes of Gold']; print('tonnes 10/22',t['2026-10-22'],'11/05',t['2026-11-05'],'vs 10/22',round(t['2026-11-05']-t['2026-10-22'],2),'falsify <=1035.64, support >=1045.64')
stress_cleared=bool((win>=7757.17).any()); tn=t['2026-11-05']
v='FALSIFIED' if stress_cleared and tn<=1035.64 else 'SUPPORTED' if stress_cleared and tn>=1045.64 else 'NOT TESTED'
print('stress cleared',stress_cleared,'outflows continued',bool(tn<=1035.64),'->',v)
print('=== daily classes (frozen classifier)')
days=[d for d in iss.index if pd.Timestamp('2026-10-22')<=d<=pd.Timestamp('2026-11-05')]
rows=[]
for a,b in zip(days[:-1],days[1:]):
    gl=100*(iss['Closing Price'][b]/iss['Closing Price'][a]-1); dr=100*(real[b]-real[a]); e=gl-B*dr
    sp=100*(spx[b]/spx[a]-1); dv=vix[b]-vix[a]; dx=100*(dxy[b]/dxy[a]-1); st=bool(sp<=-1.0 or dv>=2.0); dt=round(float(t[b]-t[a]),2)
    if abs(e)<=SD: c='RATE'
    elif e<-SD and st and dt<0: c='LIQUIDATION'
    elif e>SD and st and dx>-0.20: c='HAVEN' if dt>0 else 'UNEXPLAINED-UP (haven leg, tonnes not up)'
    elif e>SD and not st and dx<=-0.20: c='DE-DOLLAR proxy'
    else: c='UNEXPLAINED-'+('DOWN' if e<0 else 'UP')
    rows.append(dict(date=str(b.date()),gld=round(iss['Closing Price'][b],2),gld_pct=round(gl,2),d_real_bp=round(dr),e=round(e,2),e_sd=round(e/SD,2),spx_pct=round(sp,2),dvix=round(dv,2),dxy_pct=round(dx,2),stress=st,d_t=dt,t=t[b],cls=c))
df=pd.DataFrame(rows); df.to_csv(P/'wq451_applied.csv',index=False); print(df.to_string(index=False))
s=df[df.stress]; print('L2 stress days after 10/22:',len(s),'GLD up on',int((s.gld_pct>0).sum()),'dates',list(s.date))
print('DE-DOLLAR proxy days:',list(df[df.cls=='DE-DOLLAR proxy'].date),'tonnes 10/22->11/05',round(t['2026-11-05']-t['2026-10-22'],2))
print('min tonnes since 10/22',t['2026-10-22':].min(),t['2026-10-22':].idxmin().date(),'9/30',t.get(pd.Timestamp('2026-09-30')),'3m line 1035.70')
print('GLD min issuer close',iss['Closing Price']['2026-10-22':].min(),'closes < 360.71:',[str(d.date()) for d,v in iss['Closing Price']['2026-10-22':].items() if v<360.71],'max since 10/26',iss['Closing Price']['2026-10-26':].max(),'target 378.95')
print('=== d200 / dd252 (close / mean last 200 incl day - 1; drawdown from 252-session max close)')
for name in ['SLV','PPLT','PALL']:
    c=ser(name); c=c[c.index<=pd.Timestamp('2026-11-05')]
    d=(c/c.rolling(200).mean()-1)*100; dd=(c/c.rolling(252,min_periods=200).max()-1)*100
    print(name,{k:round(float(d[k]),2) for k in ['2026-10-30','2026-11-02','2026-11-03','2026-11-04','2026-11-05']},'dd252 11/05',round(float(dd['2026-11-05']),2),'bars',len(c),'SMA200 11/05',round(float(c.rolling(200).mean().iloc[-1]),3))
