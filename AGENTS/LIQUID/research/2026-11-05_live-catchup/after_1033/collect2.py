"""Second capture, 2026-11-05: first-published cells after the November 4 ICE rows appeared."""
import sys,json,pathlib,datetime,urllib.request
sys.path.insert(0,'FORGE/tools/market-data')
from fetch import fred_fetch_vintage
P=pathlib.Path(__file__).parent
out={}
for s in ['BAMLH0A0HYM2','BAMLC0A0CM','BAMLC0A4CBBB','BAMLH0A1HYBB','BAMLH0A2HYB','BAMLH0A3HYC','WRESBAL','WTREGEN','DGS10','DGS30']:
    r=fred_fetch_vintage(s,limit=25,basis='first-published',observation_start='2026-10-13')
    (P/(s+'.json')).write_text(json.dumps(r,indent=2)+'\n'); out[s]=r['rows'][:6]; 
    print(s,r.get('error'),[(x['date'],x['value'],x.get('first_published')) for x in r['rows'][:5]],flush=True)
for k in ['PDPOSCSBND-G10','PDPOSCSBND-G5L10']:
    raw=urllib.request.urlopen(urllib.request.Request(f'https://markets.newyorkfed.org/api/pd/get/{k}.json',headers={'User-Agent':'Mozilla/5.0'}),timeout=45).read()
    a=[x for x in json.loads(raw)['pd']['timeseries'] if x.get('keyid')==k and x.get('value') not in ('','*',None)]; a.sort(key=lambda x:x['asofdate'])
    (P/(k+'.json')).write_bytes(raw); print(k,[(x['asofdate'],x['value']) for x in a[-2:]],flush=True)
(P/'capture_time.txt').write_text(datetime.datetime.now(datetime.timezone.utc).isoformat()+'\n')
