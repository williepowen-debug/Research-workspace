"""Bounded Will-authorized breadth snapshot. Public sources; no owner ledger writes."""
from pathlib import Path
import csv,json,urllib.request,urllib.parse,concurrent.futures,datetime as dt,re,hashlib,time
from zoneinfo import ZoneInfo
import openpyxl
D=Path(__file__).resolve().parent;NY=ZoneInfo('America/New_York')
def now():return dt.datetime.now(dt.timezone.utc).isoformat()
rows=list(openpyxl.load_workbook(D/'holdings-daily-us-en-spy.xlsx',read_only=True,data_only=True).active.values)
h=[{'name':r[0],'ticker':r[1].replace('.','-'),'ssga_ticker':r[1],'weight_pct':r[4],'id':r[2]} for r in rows[5:] if isinstance(r[4],(float,int)) and isinstance(r[1],str) and re.fullmatch('[A-Z]{1,5}(?:[.][A-Z])?',r[1])]
assert len(h)==503 and len(set(x['ticker'] for x in h))==503
(D/'universe.json').write_text(json.dumps({'source':'https://www.ssga.com/library-content/products/fund-data/etfs/us/holdings-daily-us-en-spy.xlsx','content_asof':rows[2][1],'retrieved':now(),'holdings_sha256':hashlib.sha256((D/'holdings-daily-us-en-spy.xlsx').read_bytes()).hexdigest(),'scope':'503tradableequitysecuritylines,not500issuers;cashandnontradableCVRexcluded;currentholdingsproxy,notpointintimeindexmembership','excluded':['USDcash','2602335D CVR'],'equity_weight_sum_pct':sum(x['weight_pct'] for x in h),'rows':h},indent=2)+'\n')
def get(url):
 req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
 with urllib.request.urlopen(req,timeout=25) as r:return r.read()
def batch(pair):
 i,tickers=pair;start=now();url='https://query1.finance.yahoo.com/v7/finance/spark?'+urllib.parse.urlencode({'symbols':','.join(tickers),'range':'1y','interval':'1d','includePrePost':'false'})
 try:
  raw=get(url);j=json.loads(raw);(D/f'spark-{i:02d}.json').write_bytes(raw);return {'batch':i,'start':start,'end':now(),'url':url,'sha256':hashlib.sha256(raw).hexdigest(),'results':j.get('spark',{}).get('result',[]),'error':j.get('spark',{}).get('error')}
 except Exception as e:return {'batch':i,'start':start,'end':now(),'error':type(e).__name__+': '+str(e).split('?')[0]}
syms=[x['ticker'] for x in h];batches=[(i,syms[j:j+20]) for i,j in enumerate(range(0,len(syms),20))];start=now()
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as p:res=list(p.map(batch,batches))
receipt={'started':start,'finished':now(),'batches':[{k:v for k,v in x.items() if k!='results'} for x in res]};(D/'source-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
snap={};errors=[]
for b in res:
 for x in b.get('results',[]):
  try:
   z=x['response'][0];m=z['meta'];cl=z['indicators']['quote'][0]['close'];t=z['timestamp'];bars={dt.datetime.fromtimestamp(ts,NY).date().isoformat():v for ts,v in zip(t,cl) if v is not None};qt=dt.datetime.fromtimestamp(m['regularMarketTime'],NY);lastday=qt.date().isoformat();price=m.get('regularMarketPrice');prev=bars.get('2026-10-16');today=bars.get('2026-10-19');snap[x['symbol']]={'symbol':x['symbol'],'quote_time':qt.isoformat(),'quote_date':lastday,'price':price,'prior_close':prev,'today_bar':today,'quote_ret_pct':100*(price/prev-1) if price is not None and prev else None,'bar_ret_pct':100*(today/prev-1) if today is not None and prev else None,'bars':bars,'null_bars':sum(v is None for v in cl)}
  except Exception as e:errors.append({'symbol':x.get('symbol'),'error':str(e)})
missing=sorted(set(syms)-set(snap));usable=[x for x in snap.values() if x['quote_date']=='2026-10-19' and x['quote_ret_pct'] is not None]
quote_times=sorted(x['quote_time'] for x in usable);r=[x['quote_ret_pct'] for x in usable]
summary={'started':start,'finished':now(),'expected_securities':503,'returned':len(snap),'usable_current_session':len(usable),'missing':missing,'errors':errors,'up':sum(v>0 for v in r),'down':sum(v<0 for v in r),'unchanged':sum(v==0 for v in r),'first_quote':quote_times[0] if quote_times else None,'last_quote':quote_times[-1] if quote_times else None,'mean_ret_pct':sum(r)/len(r) if r else None,'median_ret_pct':__import__('statistics').median(r) if r else None,'limits':['currentSPYholdingsproxy,notofficialindexbreadth','securitylinesincludeAlphabettwoclassesetc','asynchronousvendorquotes;fulltimestampperline','noassumeddataforfailed/stalesymbols','historicalcurrentbasketcountsnotpointintimeindexbreadth']}
# Matched historical current-basket A/D and MA breadth are explicitly survivorship-biased proxies.
dates=sorted(set.intersection(*(set(x['bars']) for x in snap.values()))) if snap else []
hist=[]
for day in [d for d in dates if d<='2026-10-16'][-21:]:
 vals=[]
 for x in snap.values():
  ds=sorted(d for d in x['bars'] if d<=day)
  if len(ds)>=2:vals.append(x['bars'][ds[-1]]/x['bars'][ds[-2]]-1)
 hist.append({'date':day,'coverage':len(vals),'up':sum(v>0 for v in vals),'down':sum(v<0 for v in vals),'flat':sum(v==0 for v in vals)})
ma={}
for n in [20,50,200]:
 good=[]
 for x in usable:
  ds=sorted(d for d in x['bars'] if d<='2026-10-16')
  # today'spartiallastprice plus n-1completedrawpricebars; splits not independentlychecked.
  if len(ds)>=n-1:
   avg=(sum(x['bars'][d] for d in ds[-(n-1):])+x['price'])/n;good.append(x['price']>avg)
 ma[str(n)]={'covered':len(good),'above':sum(good),'pct_above':100*sum(good)/len(good) if good else None}
summary['raw_price_moving_averages']=ma;summary['historical_current_basket_ad']=hist
(D/'constituent-snapshot.json').write_text(json.dumps(snap,indent=2)+'\n');(D/'breadth-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k not in ['historical_current_basket_ad']},indent=2))
# ETF/index charts explicitly include adjusted closes for total-return proxies.
proxies=['SPY','RSP','QQQ','QQEW','IWM','DIA','MGK','VTV','VUG','XLK','XLC','XLY','XLF','XLV','XLI','XLP','XLE','XLU','XLRE','XLB','SMH','KRE','^GSPC','^IXIC']
def chart(sym):
 url='https://query1.finance.yahoo.com/v8/finance/chart/'+urllib.parse.quote(sym,safe='')+'?range=1y&interval=1d&events=div%2Csplits&includeAdjustedClose=true'
 try:
  raw=get(url);(D/('chart-'+sym.replace('^','index-')+'.json')).write_bytes(raw);return sym,{'retrieved':now(),'url':url,'data':json.loads(raw)}
 except Exception as e:return sym,{'retrieved':now(),'error':type(e).__name__+': '+str(e).split('?')[0]}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as p:out=dict(p.map(chart,proxies))
(D/'proxy-source-receipt.json').write_text(json.dumps({s:{k:v for k,v in x.items() if k!='data'} for s,x in out.items()},indent=2)+'\n')
print('ETFchartresponses',len(out),'errors',[s for s,x in out.items() if 'error' in x])
