"""Apply the FROZEN WQ-451 daily classifier (gold/research/2026-10-23_WQ451-decomposition-letter.md §2,
code frozen at a35faa6f8) to sessions 2026-10-23..10-30. Parameters copied, not re-fit:
beta -0.1526 %/bp, sd 1.402%, stress = S&P <= -1.0% OR VIX >= +2.0 pts, DXY threshold -0.20%.
Rate leg: PRIMARY Treasury real 10Y (the letter used FRED DFII10 with PRIMARY Treasury where FRED lagged).
GLD: issuer close where printed, MIRROR Yahoo close for 10/30 (issuer row not yet published); tonnes PRIMARY issuer."""
from pathlib import Path
import json, pandas as pd
P=Path(__file__).resolve().parent
B,SD=-0.1526,1.402
px=pd.read_csv(P/'closes.csv',index_col=0,parse_dates=True)
g=json.loads((P/'GSPC.json').read_text())['chart']['result'][0]
from datetime import datetime; from zoneinfo import ZoneInfo
spx=pd.Series({pd.Timestamp(datetime.fromtimestamp(t,ZoneInfo('America/New_York')).strftime('%Y-%m-%d')):c for t,c in zip(g['timestamp'],g['indicators']['quote'][0]['close']) if c})
re_=pd.read_csv(P/'treasury_real.csv',parse_dates=['Date']).set_index('Date').sort_index()['10 YR']
iss=pd.read_excel(P/'GLD_issuer_archive.xlsx',sheet_name='US GLD Historical Archive')
iss['Date']=pd.to_datetime(iss['Date'],format='%d-%b-%Y'); iss=iss.sort_values('Date').set_index('Date')
for c in ['Closing Price','Tonnes of Gold']: iss[c]=pd.to_numeric(iss[c],errors='coerce')
days=pd.bdate_range('2026-10-22','2026-10-30')
rows=[]
for a,b in zip(days[:-1],days[1:]):
    ga=iss['Closing Price'].get(a); gb=iss['Closing Price'].get(b); src='issuer'
    if pd.isna(gb) if gb is not None else True: gb=px['GLD'].get(b); src='MIRROR Yahoo (issuer row unpublished)'
    gl=100*(gb/ga-1); dr=100*(re_[b]-re_[a]); e=gl-B*dr
    sp=100*(spx[b]/spx[a]-1); dv=px['^VIX'][b]-px['^VIX'][a]; dx=100*(px['DX-Y.NYB'][b]/px['DX-Y.NYB'][a]-1)
    stress=sp<=-1.0 or dv>=2.0
    ta=iss['Tonnes of Gold'].get(a); tb=iss['Tonnes of Gold'].get(b)
    dt=None if (tb is None or pd.isna(tb)) else round(float(tb-ta),2)
    if abs(e)<=SD: cls='RATE'
    elif e<-SD and stress: cls='LIQUIDATION' if (dt is not None and dt<0) else ('LIQUIDATION-candidate: tonnes leg PENDING (issuer 10/30 unpublished)' if dt is None else 'UNEXPLAINED-DOWN (tonnes not down)')
    elif e>SD and stress and dx>-0.20: cls='HAVEN' if (dt is not None and dt>0) else 'HAVEN-candidate/UNEXPLAINED-UP'
    elif e>SD and not stress and dx<=-0.20: cls='DE-DOLLAR proxy'
    else: cls='UNEXPLAINED-'+('DOWN' if e<0 else 'UP')
    rows.append(dict(date=str(b.date()),gld_pct=round(gl,3),gld_source=src,d_real_bp=round(dr,1),implied_pct=round(B*dr,3),e_pct=round(e,3),e_sd=round(e/SD,2),spx_pct=round(sp,3),dvix_pts=round(dv,2),dxy_pct=round(dx,3),stress=stress,tonnes_d=dt,cls=cls))
df=pd.DataFrame(rows); df.to_csv(P/'wq451_applied.csv',index=False); print(df.to_string(index=False))
print('SPX max close 10/22..10/30:',round(spx['2026-10-22':'2026-10-30'].max(),2),'vs L1 line 7757.17')
