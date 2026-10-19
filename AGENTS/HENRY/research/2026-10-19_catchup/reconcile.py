"""Reproduce frozen cohort, matching, F1 estimates and dated rates from retained inputs."""
import json,csv,math,pathlib,datetime,hashlib
from zoneinfo import ZoneInfo
from decimal import Decimal as D
P=pathlib.Path(__file__).resolve().parent
R=P/'raw';NY=ZoneInfo('America/New_York')
def dump(name,data): (P/name).write_text(json.dumps(data,indent=2)+'\n')
def chart(name):return json.loads((R/name).read_text())['chart']['result'][0]
def prices(s):
 d=chart('chart-'+s+'.json');q=d['indicators']['quote'][0];a=d['indicators']['adjclose'][0]['adjclose']
 return {datetime.datetime.fromtimestamp(t,NY).date().isoformat():{'raw':c,'adj':ac} for t,c,ac in zip(d['timestamp'],q['close'],a) if c is not None and ac is not None}
shares=json.loads((P/'shares.json').read_text());pr={s:prices(s) for s in shares}
end='2026-10-16';calendar=sorted(d for d in pr['MU'] if d<=end);dates={n:calendar[-1-n] for n in [5,20,60]};assert dates[20]=='2026-09-18'
out={}
for s in shares:
 x=pr[s];assert all(d in x for d in calendar[-61:])
 assert shares[s]['period_end']<=shares[s]['available_by']<dates[20]
 out[s]={'shares':shares[s]['shares'],'formation_cap_bn':x[dates[20]]['raw']*shares[s]['shares']/1e9,'formation_raw_close':x[dates[20]]['raw'],'end_raw_close':x[end]['raw'],'returns':{str(n):{'start':d,'raw_pct':100*(x[end]['raw']/x[d]['raw']-1),'adjusted_pct':100*(x[end]['adj']/x[d]['adj']-1)} for n,d in dates.items()}}
# Snapshot and sector map are retained copies; no financing values enter selection.
snap=json.loads((P/'constituent-snapshot.json').read_text());sectors={r['symbol']:r['sector'] for r in csv.DictReader((P/'quality-screen-stocks.csv').open()) if r['sessions']=='20'}
screen=[]
for s,d in snap.items():
 b=d['bars'];reason=''
 if sectors.get(s) in ['XLF','XLRE']:reason='financial_or_REIT_sector'
 elif s=='SKYD':reason='corporate_action_identity_not_reconciled'
 elif s not in sectors:reason='sector_UNKNOWN'
 elif dates[20] not in b or end not in b:reason='missing_exact_endpoint'
 ret=100*(b[end]/b[dates[20]]-1) if end in b and dates[20] in b else None
 screen.append(dict(symbol=s,sector=sectors.get(s),raw20_pct=ret,exclusion=reason))
screen.sort(key=lambda r:(r['raw20_pct'] if r['raw20_pct'] is not None else math.inf,r['symbol']))
assert len(screen)==503
selected=[r['symbol'] for r in screen if not r['exclusion']][:8]
assert selected==['SNDK','COHR','STX','WDC','MGM','MOS','DELL','SMCI'],selected
candidates={'SNDK':['MU'],'COHR':['LITE'],'STX':['WDC'],'WDC':['STX'],'MGM':['WYNN','LVS'],'MOS':['CF'],'DELL':['SMCI','HPE','HPQ'],'SMCI':['DELL','HPE','HPQ']}
audit=[];matches={}
for s,cs in candidates.items():
 valid=[]
 for c in cs:
  a,b=out[s]['formation_cap_bn'],out[c]['formation_cap_bn'];ratio=max(a,b)/min(a,b)
  row=dict(weak=s,candidate=c,weak_cap_bn=a,candidate_cap_bn=b,size_ratio=ratio,eligible=ratio<=2,log_distance=abs(math.log(a/b)));audit.append(row)
  if row['eligible']:valid.append(row)
 best=min(valid,key=lambda r:(r['log_distance'],r['candidate']))['candidate'] if valid else None
 matches[s]=dict(control=best,reason='nearest_size_within_2x' if best else 'no_candidate_within_2x',adjusted20_difference_pp=(out[s]['returns']['20']['adjusted_pct']-out[best]['returns']['20']['adjusted_pct']) if best else None)
dump('screen.json',screen);dump('returns-size.json',out);dump('candidate-audit.json',audit);dump('matches.json',matches)
for name in selected:
 assert abs(out[name]['formation_raw_close']-snap[name]['bars'][dates[20]])<.011
 assert abs(out[name]['end_raw_close']-snap[name]['bars'][end])<.011
# Exactly the two start-labelled bars in approved tier-3 proxy; no 14:30 bar.
f1=[]
for day in ['2026-10-15','2026-10-16','2026-10-19']:
 legs={}
 for s in ['HOZ26.NYM','CLZ26.NYM']:
  d=chart(s+'-1m.json');assert d['meta']['symbol']==s and d['meta']['instrumentType']=='FUTURE' and d['meta']['exchangeName']=='NYM' and 'Dec 26' in d['meta']['shortName']
  q=d['indicators']['quote'][0];rows=[]
  for i,t in enumerate(d['timestamp']):
   dt=datetime.datetime.fromtimestamp(t,NY)
   if dt.date().isoformat()==day and dt.strftime('%H:%M') in ['14:28','14:29']:
    c=q['close'][i];v=q['volume'][i];assert c and v and v>0
    rows.append(dict(label=dt.isoformat(),close=str(c),volume=v))
  assert len(rows)==2
  vw=sum(D(r['close'])*r['volume'] for r in rows)/sum(r['volume'] for r in rows)
  legs[s]=dict(rows=rows,close_volume_vwap=str(vw))
 crack=D(legs['HOZ26.NYM']['close_volume_vwap'])*42-D(legs['CLZ26.NYM']['close_volume_vwap'])
 f1.append(dict(date=day,legs=legs,crack=str(crack),below95=crack<D(95),below9016=crack<D('90.16')))
spy=chart('SPY-1m.json');conv={}
for day in ['2026-10-15','2026-10-16','2026-10-19']:
 stamps=[datetime.datetime.fromtimestamp(t,NY) for t in spy['timestamp']];ss=[t for t in stamps if t.date().isoformat()==day and '09:30'<=t.strftime('%H:%M')<'16:00']
 conv[day]=dict(count=len(ss),first=ss[0].isoformat(),last=ss[-1].isoformat());assert len(ss)==390 and ss[0].strftime('%H:%M')=='09:30' and ss[-1].strftime('%H:%M')=='15:59'
dump('f1-calculations.json',dict(observations=f1,bar_convention_control=conv,float32_price_error_bound_usd_per_bbl=.0001))
rates={}
for s in ['DGS2','DGS10','DGS30','DFII10','DFII30','T10YIE']:
 rates[s]={r['observation_date']:float(r[s]) for r in csv.DictReader((R/('rates-'+s+'.csv')).open()) if r[s] not in ['', '.']}
import xlrd
wb=xlrd.open_workbook(str(R/'acm.xlsx'));ws=wb.sheet_by_name('ACM Daily');header=ws.row_values(0);a=[]
for i in range(1,ws.nrows):
 row=ws.row_values(i)
 if not row[0]:continue
 if isinstance(row[0],(float,int)): day=xlrd.xldate_as_datetime(row[0],wb.datemode).strftime('%d-%b-%Y')
 else: day=str(row[0])
 try:dt=datetime.datetime.strptime(day,'%d-%b-%Y')
 except ValueError:continue
 if dt.date()>=datetime.date(2026,9,30):a.append(dict(zip(header,[day]+row[1:])))
assert a and a[-1]['DATE']=='16-Oct-2026'
for row in a:assert abs(row['ACMY10']-row['ACMRNY10']-row['ACMTP10'])<1e-9
dump('acm-recent.json',a)
dump('rates-calculations.json',dict(rates=rates,acm=a))
print('Selection:',selected);print('Windows:',dates)
for s,m in matches.items():print(s,round(out[s]['formation_cap_bn'],3),round(out[s]['returns']['20']['adjusted_pct'],4),m)
print('Fuel:',[(r['date'],r['crack']) for r in f1]);print('Rates:',{s:list(v.items())[-1] for s,v in rates.items()})
print('PASS: eight fixed weak names; all exact windows; full candidate audit; F1 two bars/leg and SPY390 control')

identities={}
for symbol in ['HOZ26.NYM','CLZ26.NYM']:
 info=json.loads((R/('info-'+symbol+'.json')).read_text());expiry=datetime.datetime.fromtimestamp(info['expireDate'],datetime.timezone.utc).date().isoformat()
 assert info['symbol']==symbol and info['exchange']=='NYM' and info['quoteType']=='FUTURE' and info['currency']=='USD'
 assert expiry==('2026-11-30' if symbol.startswith('HO') else '2026-11-20')
 identities[symbol]=dict(expiry_utc=expiry,name=info['shortName'],underlying=info['underlyingSymbol'])
aal=chart('supplement-AAL.json');q=aal['indicators']['quote'][0];path=[]
for i,t in enumerate(aal['timestamp']):
 day=datetime.datetime.fromtimestamp(t,NY).date().isoformat()
 if '2026-09-11'<=day<='2026-10-19':
  assert q['low'][i] is not None and q['close'][i] is not None
  path.append(dict(date=day,close=q['close'][i],low=q['low'][i]))
f5=dict(start='2026-09-11',end='2026-10-19',threshold=12.85*.88,bars=len(path),minimum_close=min(path,key=lambda r:r['close']),minimum_low=min(path,key=lambda r:r['low']))
f5['fired']=f5['minimum_low']['low']<f5['threshold'];assert not f5['fired']
dump('f1-identity-f5.json',dict(contracts=identities,f5=f5))
print('PASS: source-before-formation, full return windows, original-selection prices, December expiry identity and AAL full low/close path')
