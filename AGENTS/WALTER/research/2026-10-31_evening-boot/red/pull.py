import os,sys,json,csv,io,urllib.request,concurrent.futures
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path('/home/willi/Research-workspace')
HERE=Path(__file__).resolve().parent
os.environ['FORGE_CACHE_DIR']=str(HERE/'.cache')
sys.path.insert(0,str(ROOT/'FORGE/tools/market-data'))
import fetch
fetch.AUDIT_LOG=HERE/'audit.txt'
def skew():
 u='https://cdn.cboe.com/api/global/us_indices/daily_prices/SKEW_History.csv'
 t=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=30).read().decode('utf-8-sig'); (HERE/'SKEW_History.csv').write_text(t)
 return list(csv.DictReader(io.StringIO(t)))[-20:]
series=['BAMLH0A0HYM2','BAMLH0A3HYC','VIXCLS','ICSA','T5YIFR','DGS2','DGS5','DGS10','DGS20','DGS30','T10YIE','BAMLH0A0E2Y']
jobs={s:lambda s=s:fetch.fred_fetch(s,16) for s in series}
jobs.update({'HY_first_published':lambda:fetch.fred_fetch_vintage('BAMLH0A0HYM2',limit=16),'Cushing':lambda:fetch.eia_fetch('W_EPC0_SAX_YCUOK_MBBL',limit=4),'SKEW':skew,'prices':lambda:fetch.price_fetch(['CLZ26.NYM','BZZ26.NYM','RBZ26.NYM','HOZ26.NYM','BZF27.NYM','RBF27.NYM','HOF27.NYM'])})
for root in ['BZ','CL','HO','RB']:jobs['probe_'+root]=lambda root=root:fetch.contract_probe(root)
result={'as_of':datetime.now(timezone.utc).isoformat()}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
 fut={pool.submit(fn):k for k,fn in jobs.items()}
 for f in concurrent.futures.as_completed(fut):
  k=fut[f]
  try:result[k]=f.result()
  except Exception as e:result[k]={'error':type(e).__name__}
(HERE/'observations.json').write_text(json.dumps(result,indent=2,default=str)+'\n')
print('Saved',str(HERE/'observations.json'))
for k,v in result.items():
 if isinstance(v,list): print(k, v[:2] if k!='SKEW' else v[-6:])
 elif k.startswith('probe'):print(k,v.get('verdict'))
 elif k=='HY_first_published': print(k,v.get('rows',[])[:5], 'short',v.get('short'),'error',v.get('error'))
