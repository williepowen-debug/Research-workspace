"""Dated close arithmetic using saved responses and unchanged band methods."""
from pathlib import Path
from datetime import datetime,date,timedelta
from zoneinfo import ZoneInfo
import json,math,csv,sys,statistics
import pandas as pd
from bs4 import BeautifulSoup
P=Path(__file__).resolve().parent; ROOT=P.parents[4]
sys.path.insert(0,str(ROOT/'AGENTS/MIDAS'))
import metals_watch as mw
TARGET='2026-10-26'
series={}; history={}; output={'as_of_requested':TARGET,'prices':{},'bands':{}}
for f in P.glob('*.json'):
 if f.name in ['access.json','summary.json','validation.json']:continue
 raw=json.loads(f.read_text())
 if 'chart' not in raw:continue
 r=raw['chart']['result'][0];meta=r['meta'];tz=ZoneInfo(meta['exchangeTimezoneName'])
 idx=[datetime.fromtimestamp(t,tz).strftime('%Y-%m-%d') for t in r['timestamp']]
 q=r['indicators']['quote'][0]
 rows=[dict(date=d,close=q['close'][i],volume=q['volume'][i],timestamp=datetime.fromtimestamp(r['timestamp'][i],tz).isoformat()) for i,d in enumerate(idx) if d<=TARGET]
 live_appended=[]
 for d in sorted(set(x['date'] for x in rows)):
  same=[x for x in rows if x['date']==d]
  if len(same)>1:
   daily=[x for x in same if x['timestamp'][11:19]=='00:00:00']
   assert len(daily)==1 and len(same)==2,(f.name,same)
   live_appended += [x for x in same if x is not daily[0]]
   rows=[x for x in rows if x['date']!=d or x is daily[0]]
 missing=[x['date'] for x in rows if x['close'] is None]
 assert TARGET not in missing and '2026-10-23' not in missing,(f.name,missing)
 rows=[x for x in rows if x['close'] is not None]
 bad=[x['date'] for x in rows if not math.isfinite(x['close']) or x['close']<=0]
 assert not bad,(f.name,bad)
 assert len({x['date'] for x in rows})==len(rows)
 ticker=meta['symbol']; history[ticker]={'history':rows}
 s=pd.Series([x['close'] for x in rows],index=pd.to_datetime([x['date'] for x in rows]));series[ticker]=s
 pd.DataFrame(rows).to_csv(P/(f.stem+'.csv'),index=False)
 latest=rows[-1];prev=rows[-2]
 output['prices'][ticker]=dict(date=latest['date'],close=latest['close'],previous_date=prev['date'],previous_close=prev['close'],day_pct=100*(latest['close']/prev['close']-1),basis='MIRROR Yahoo raw daily unadjusted Close; newest futures row diagnostic only' if ticker in mw.FRONT_MONTHS.values() else 'MIRROR Yahoo raw completed unadjusted daily Close',timezone=meta['exchangeTimezoneName'],currency=meta.get('currency'),n=len(rows),excluded_null_close_dates=missing,last_volume=latest['volume'],previous_volume=prev['volume'])
 output['prices'][ticker]['excluded_live_appended_rows']=live_appended
 if ticker in ['SLV','PPLT','PALL']:
  d=100*(s/s.rolling(200).mean()-1);dd=100*(s/s.rolling(252).max()-1)
  T={'SLV':[-5,-12,-20],'PPLT':[-10,-15,-20],'PALL':[-12,-20,-25]}[ticker]
  C=[-20,-30] if ticker=='PPLT' else [-20,-30,-40]
  t=max([1]+[j for j,x in enumerate(T,2) if d.iloc[-1]<=x]);sp=3 if d.iloc[-1]>=40 else 2 if d.iloc[-1]>=30 else 1
  crossed_t=[x for x in T if d.iloc[-2]>x>=d.iloc[-1]]
  crossed_c=[x for x in C if dd.iloc[-2]>x>=dd.iloc[-1]]
  assert not crossed_c,('Fresh crash crossing needs its registered event-decay read',ticker,crossed_c)
  output['bands'][ticker]=dict(date=latest['date'],sma200=float(s.iloc[-200:].mean()),d200=float(d.iloc[-1]),previous_d200=float(d.iloc[-2]),T_level=t,dd252=float(dd.iloc[-1]),C_level=1,C_basis='Previously decayed, carried after checking no new deeper crossing since prior close',S_level=sp,T_crossings=crossed_t,C_crossings=crossed_c,would_be_max=max(t,sp,1))
front={k:v for k,v in mw.FRONT_MONTHS.items()}
primary,_,_=mw.read_contract_snapshot(front_months=front,history=history,today=date.fromisoformat(TARGET))
output['guard_qualified_futures']=primary
output['guard_qualified_gsr']=mw.primary_gsr(primary)
gold=output['prices']['GCZ26.CMX'];silver=output['prices']['SIZ26.CMX']
assert gold['date']==silver['date']==TARGET
output['diagnostic_gsr']=gold['close']/silver['close']
issuer=pd.read_excel(P/'GLD_issuer_archive.xlsx',sheet_name='US GLD Historical Archive')
issuer['Date']=pd.to_datetime(issuer['Date'],format='%d-%b-%Y');issuer=issuer.sort_values('Date').set_index('Date')
for col in ['Closing Price','Tonnes of Gold']:issuer[col]=pd.to_numeric(issuer[col],errors='coerce')
i=issuer.dropna(subset=['Closing Price','Tonnes of Gold']);i=i.loc[:TARGET]
i.tail(8).to_csv(P/'GLD_latest_issuer.csv')
output['issuer_GLD']=dict(date=str(i.index[-1].date()),close=float(i['Closing Price'].iloc[-1]),tonnes=float(i['Tonnes of Gold'].iloc[-1]),prior_date=str(i.index[-2].date()),prior_tonnes=float(i['Tonnes of Gold'].iloc[-2]),change_tonnes=float(i['Tonnes of Gold'].iloc[-1]-i['Tonnes of Gold'].iloc[-2]))
matched=series['GLD'].reindex(i.index).dropna();diff=(matched-i.loc[matched.index,'Closing Price']).abs();assert diff.max()<0.0001,float(diff.max())
output['issuer_GLD']['matched_vendor_max_abs_price_difference']=float(diff.max())
with (P/'treasury_real.csv').open() as f:rates={datetime.strptime(r['Date'],'%m/%d/%Y').strftime('%Y-%m-%d'):float(r['10 YR']) for r in csv.DictReader(f) if r['10 YR']}
keys=sorted(k for k in rates if k<=TARGET)
output['primary_real_yield']=dict(date=keys[-1],percent=rates[keys[-1]],prior_date=keys[-2],prior_percent=rates[keys[-2]],change_bp=100*(rates[keys[-1]]-rates[keys[-2]]))
combined={}
for f in P.glob('westmetall_*.html'):
 soup=BeautifulSoup(f.read_text(),'html.parser')
 table=next(t for t in soup.find_all('table') if 'LME Copper stock' in t.get_text())
 trs=table.find_all('tr');header=[c.get_text(' ',strip=True) for c in trs[0].find_all(['td','th'])]
 stock_col=header.index('LME Copper stock');date_col=header.index('date')
 for tr in trs[1:]:
  cells=[c.get_text(' ',strip=True) for c in tr.find_all(['td','th'])]
  if len(cells)!=len(header):continue
  if cells[date_col]=='date':continue
  dt=datetime.strptime(cells[date_col],'%d. %B %Y');n=int(cells[stock_col].replace(',',''))
  assert n>0
  if dt in combined:assert combined[dt]==n
  combined[dt]=n
last=max(combined);cut=last-timedelta(days=730);window=[n for d,n in combined.items() if d>=cut];median=statistics.median(window)
output['lme_copper']=dict(date=last.strftime('%Y-%m-%d'),tonnes=combined[last],median_2yr_tonnes=median,n=len(window),versus_median_pct=100*(combined[last]/median-1))
output['actual_scores']={'M1':4,'M2':1,'I1':1,'I2':2};output['actual_composite']=8
output['counterfactual']={'M1':4,'M2':output['bands']['SLV']['would_be_max'],'I1':1,'I2':max(output['bands'][t]['would_be_max'] for t in ['PPLT','PALL'])}
output['counterfactual_total']=sum(output['counterfactual'].values())
output['gold_certified_settlement_grade']='UNRESOLVED; no certified source, newest row excluded from scoring'
output['shared_root']='Retained: SLV October14 and PALL October22 within15sessions; not independent'
(P/'summary.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
