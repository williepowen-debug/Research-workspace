import sys,json,pathlib,concurrent.futures,urllib.request,hashlib
sys.path.insert(0,'FORGE/tools/market-data');sys.path.insert(0,'AGENTS/LIQUID/scripts')
from fetch import fred_fetch_vintage
import dtcc_cds_probe as dt
p=pathlib.Path(__file__).parent

def fp(s):
 r=fred_fetch_vintage(s,limit=60,basis='first-published',observation_start='2026-09-01'); (p/(s+'.json')).write_text(json.dumps(r,indent=2)+'\n'); print(s,len(r['rows']),r.get('error'),flush=True)
def pd(k):
 u=f'https://markets.newyorkfed.org/api/pd/get/{k}.json'
 with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=45) as r: raw=r.read(); heads=dict(r.headers)
 (p/(k+'.json')).write_bytes(raw)
 data=json.loads(raw)['pd']['timeseries']; a=[x for x in data if x.get('keyid')==k and x.get('value') not in ('','*',None)]; a.sort(key=lambda x:x['asofdate'])
 print(k,a[-4:],flush=True)
def cds(day):
 try:
  rs=dt.rows(day); batch=dt.batch_keys(rs)
  hits=[r for r in rs if any(n in (r['Underlying Asset Name'] or '').upper() for n in ['COREWEAVE','ORACLE','META PLATFORMS'])]
  out={'file_date':day,'source':dt.URL.format(r='sec',R='SEC',d=day.replace('-','_')),'rows_total':len(rs),'rows':[{**r,'_batch':dt.batch_key(r) in batch} for r in hits]}
  (p/('dtcc_'+day+'.json')).write_text(json.dumps(out,indent=2)+'\n')
  print('DTCC',day,len(rs),len(hits),flush=True)
 except Exception as e: print('DTCC',day,type(e).__name__,str(e)[:130],flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as e:
 futures=[e.submit(fp,s) for s in ['BAMLH0A0HYM2','BAMLC0A0CM','BAMLH0A1HYBB','BAMLH0A2HYB','BAMLH0A3HYC']]
 futures += [e.submit(pd,s) for s in ['PDPOSCSBND-G10','PDPOSCSBND-G5L10']]
 futures += [e.submit(cds,d) for d in ['2026-11-02','2026-11-03']]
 for f in futures:
  try: f.result()
  except Exception as ex: print(type(ex).__name__,str(ex)[:160],flush=True)
