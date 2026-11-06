"""Base rates for MIDAS-18..22. Reads only saved files. Windows: 38 NYSE sessions 11/05->12/31; 31 LME days 11/05->12/18; COT 4 weeks 11/03? uses 5 vintages 10/27->12/01."""
from pathlib import Path
import io,json,re
from datetime import datetime
import pandas as pd, numpy as np
P=Path(__file__).resolve().parent; G=P.parent/'2026-11-06_L819_grade'
# --- GLD tonnes
iss=pd.read_excel(G/'GLD_issuer_archive.xlsx',sheet_name='US GLD Historical Archive'); iss.columns=[str(c).strip() for c in iss.columns]
iss['Date']=pd.to_datetime(iss['Date'],format='%d-%b-%Y',errors='coerce'); iss=iss.dropna(subset=['Date']).sort_values('Date').set_index('Date')
t=pd.to_numeric(iss['Tonnes of Gold'],errors='coerce').dropna()
now=t.iloc[-1]; need=1045.64/now-1
f=t.shift(-38)/t-1; past=t/t.shift(30)-1
for name,s in {'all':f,'2015+':f['2015':],'2022+':f['2022':]}.items():
    s=s.dropna(); print('GLD +38s tonnes >=',round(need*100,2),'%',name,round((s>=need).mean(),3),'n',len(s))
c=f[(past<=-0.02)&(past>=-0.06)].dropna(); print(' after prior 30s -2..-6%:',round((c>=need).mean(),3),'n',len(c),'non-overlap n',len(c.iloc[::38]),round((c.iloc[::38]>=need).mean(),3))
print(' prior30 now',round(past.iloc[-1]*100,2),'tonnes',now)
# --- SLV d200
j=json.loads((P/'SLV_max.json').read_text())['chart']['result'][0]
s=pd.Series(j['indicators']['quote'][0]['close'],index=pd.to_datetime(j['timestamp'],unit='s').normalize()).dropna()
s=s[s.index<=pd.Timestamp('2026-11-05')]
d=(s/s.rolling(200).mean()-1)*100
fut=d.shift(-38)
for lo,hi in [(-32,-22),(-30,-23)]:
    m=(d>=lo)&(d<=hi); c=fut[m].dropna(); print('SLV d200 in',lo,hi,'-> d200(+38)>-20:',round((c>-20).mean(),3),'n',len(c),'n-nonover',len(c.iloc[::38]),round((c.iloc[::38]>-20).mean(),3))
    print('   by first-day episodes:',int(((m)&(~m.shift(1,fill_value=False))).sum()))
# flat price arithmetic at 12/31
cl=s.copy(); px=46.93; path=list(cl.values[-(200-38):])+[px]*38; print('SLV flat 46.93 SMA200 at 12/31',round(np.mean(path),3),'d200',round((px/np.mean(path)-1)*100,2),'price needed for -20:',round(0.8*np.mean(path),2))
# solve close-needed with linear walk from 46.93
for tgt in [50,52,54,56]:
    p=list(cl.values[-(200-38):])+list(np.linspace(46.93,tgt,39)[1:]); print('  linear to',tgt,'d200',round((tgt/np.mean(p)-1)*100,2))
# --- LME
rows={}
for f_ in sorted(list(P.glob('westmetall_*.html'))+[G/'westmetall_2026.html']):
    tb=pd.read_html(io.StringIO(f_.read_text(errors='ignore')))[0]
    for _,r in tb.iterrows():
        try: rows[pd.Timestamp(datetime.strptime(str(r['date']).strip(),'%d. %B %Y'))]=float(r['LME Copper stock'])
        except Exception: pass
l=pd.Series(rows).sort_index(); print('LME n',len(l),l.index[0].date(),l.index[-1].date(),l.iloc[-1])
need=350000/l.iloc[-1]-1; fl=l.shift(-31)/l-1
print('LME +31d >=',round(need*100,1),'%: all',round((fl>=need).mean(),3),'n',fl.notna().sum()); p20=l/l.shift(10)-1
c=fl[p20>=0.10].dropna(); print(' after 10d rise >=10%:',round((c>=need).mean(),3),'n',len(c),'nonover',len(c.iloc[::31]),round((c.iloc[::31]>=need).mean(),3),'median',round(c.median()*100,1))
c2=fl[(p20>=0.10)&(l>=250000)].dropna(); print(' same & level>=250k:',round((c2>=need).mean(),3),'n',len(c2),'median chg',round(c2.median()*100,1))
for lvl in [300000,330000,350000]:
    print('  P(+31d >=',lvl,') after 10d rise >=10%:',round((fl[p20>=0.10].dropna()>=lvl/l.iloc[-1]-1).mean(),3))
print('10d chg now',round(p20.iloc[-1]*100,1)); print('2026 max',l['2026'].max(),l['2026'].idxmax().date()); print('2026 rows since Jan: last 12',l.tail(12).to_dict())
# --- Pd COT
h=pd.read_csv(Path('sources/cot_metals_history_2010_2026.tsv'),sep='\t',comment='#'); print(h.columns.tolist()[:12]); print(h.tail(2).to_string())
# --- tie-set realisation (SL-5) on the letters' operators and precision
print('TIES: GLD tonnes rows exactly 1045.64:',int((t.round(2)==1045.64).sum()),'of',len(t))
print('TIES: SLV d200 rounded exactly -20.00:',int((d.round(2)==-20.00).sum()),'of',int(d.notna().sum()))
print('TIES: LME exactly 350000:',int((l==350000).sum()),'of',len(l),'; LME 2026 rows >=350000:',int((l['2026']>=350000).sum()))
pp=h[h.metal=='palladium'].net_over_oi_pct; print('TIES: Pd net/OI exactly -30.0000:',int((pp.round(4)==-30.0).sum()),'of',len(pp))
