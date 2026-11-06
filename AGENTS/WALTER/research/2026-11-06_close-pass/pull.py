import os,sys,json,csv,io,urllib.request,concurrent.futures
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path('/home/willi/Research-workspace')
HERE=Path(__file__).resolve().parent
os.environ['FORGE_CACHE_DIR']=str(HERE/'.cache')
sys.path.insert(0,str(ROOT/'FORGE/tools/market-data'))
import fetch
fetch.AUDIT_LOG=HERE/'audit.txt'
def cboe(n):
 u=f'https://cdn.cboe.com/api/global/us_indices/daily_prices/{n}_History.csv'
 t=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=30).read().decode('utf-8-sig'); (HERE/f'{n}_History.csv').write_text(t)
 return list(csv.DictReader(io.StringIO(t)))[-3:]
def nasdaq(sym,cls):
 r=urllib.request.urlopen(urllib.request.Request(f'https://api.nasdaq.com/api/quote/{sym}/historical?assetclass={cls}&fromdate=2026-11-02&limit=5&todate=2026-11-06',headers={'User-Agent':'Mozilla/5.0','Accept':'application/json'}),timeout=25).read()
 return json.loads(r)['data']['tradesTable']['rows'][:4]
series=['BAMLH0A0HYM2','BAMLH0A3HYC','VIXCLS','ICSA','T5YIFR','SOFR','IORB','DGS10','DGS2','DGS30']
jobs={s:lambda s=s:fetch.fred_fetch(s,6) for s in series}
jobs.update({'HY_first_published':lambda:fetch.fred_fetch_vintage('BAMLH0A0HYM2',limit=6),'Cushing':lambda:fetch.eia_fetch('W_EPC0_SAX_YCUOK_MBBL',limit=3),'SKEWh':lambda:cboe('SKEW'),'VIXh':lambda:cboe('VIX'),'VIX9Dh':lambda:cboe('VIX9D'),'VIX3Mh':lambda:cboe('VIX3M'),'VVIXh':lambda:cboe('VVIX'),
 'WALn':lambda:nasdaq('WAL','stocks'),'KREn':lambda:nasdaq('KRE','etf'),'ZIONn':lambda:nasdaq('ZION','stocks'),'HYGn':lambda:nasdaq('HYG','etf'),'SPYn':lambda:nasdaq('SPY','etf'),
 'prices':lambda:fetch.price_fetch(['CLF27.NYM','BZF27.NYM','RBF27.NYM','HOF27.NYM','CLZ26.NYM','HOZ26.NYM','RBZ26.NYM','KRE','WAL','ZION','OZK','VLY','FLG','^VIX','^VIX9D','^VIX3M','^VVIX','^SKEW','VLO','USO','GLD','APO','SPY','^GSPC','QQQ','SMH','NVDA','HYG','LQD','IWM','TLT','RSP','UNG','ORCL','AAPL'])})
for root in ['BZ','CL','HO','RB']:jobs['probe_'+root]=lambda root=root:fetch.contract_probe(root)
result={'as_of':datetime.now(timezone.utc).isoformat()}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 fut={pool.submit(fn):k for k,fn in jobs.items()}
 for f in concurrent.futures.as_completed(fut):
  k=fut[f]
  try:result[k]=f.result()
  except Exception as e:result[k]={'error':type(e).__name__+': '+str(e)[:120]}
(HERE/'observations.json').write_text(json.dumps(result,indent=2,default=str)+'\n')
print('as_of',result['as_of'])
for k,v in result.items():
 if isinstance(v,list): print(k, json.dumps(v[:3],default=str)[:400])
 elif k.startswith('probe'):print(k,v.get('verdict'),v.get('resolved_symbol'))
 elif k=='HY_first_published': print(k,str(v.get('rows',[])[:4])[:300], 'short',v.get('short'),'error',v.get('error'))
 elif k=='prices': print('prices',json.dumps({s:{a:b for a,b in q.items() if a in('price','change_pct','prev_close','previous_close','market_time','timestamp','asof','as_of','refusal','verdict')} if isinstance(q,dict) else q for s,q in v.items()},default=str)[:4500])
 elif k!='as_of':print(k,str(v)[:300])
