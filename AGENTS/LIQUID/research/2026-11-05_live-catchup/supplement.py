"""Dealer positions and DTCC capture for the 2026-11-05 catch-up, not a monitor."""
import sys,json,pathlib,urllib.request
sys.path.insert(0,'AGENTS/LIQUID/scripts')
import dtcc_cds_probe as dt
p=pathlib.Path(__file__).parent
def pd(k):
 u=f'https://markets.newyorkfed.org/api/pd/get/{k}.json'
 with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=45) as r: raw=r.read()
 (p/(k+'.json')).write_bytes(raw)
 a=[x for x in json.loads(raw)['pd']['timeseries'] if x.get('keyid')==k and x.get('value') not in ('','*',None)]
 a.sort(key=lambda x:x['asofdate']); print(k,[(x['asofdate'],x['value']) for x in a[-4:]],flush=True)
for k in ['PDPOSCSBND-G10','PDPOSCSBND-G5L10']:
 try: pd(k)
 except Exception as e: print(k,'FAIL',repr(e),flush=True)
for day in ['2026-11-04']:
 try:
  rs=dt.rows(day); batch=dt.batch_keys(rs)
  hits=[r for r in rs if any(n in (r['Underlying Asset Name'] or '').upper() for n in ['COREWEAVE','ORACLE','META PLATFORMS'])]
  out={'file_date':day,'source':dt.URL.format(r='sec',R='SEC',d=day.replace('-','_')),'rows_total':len(rs),'rows':[{**r,'_batch':dt.batch_key(r) in batch} for r in hits]}
  (p/('dtcc_'+day+'.json')).write_text(json.dumps(out,indent=2)+'\n'); print(day,'rows',len(rs),'hits',len(hits),flush=True)
 except Exception as e: print(day,'FAIL',repr(e),flush=True)
