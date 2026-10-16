"""Read-only $0 collection/matcher sizing; no lane writes or deployment."""
import concurrent.futures, hashlib, html, json, sys, urllib.parse, urllib.request, xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime, timezone
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parents[1]/'tools'))
import watch_for_harness as h
C=h.load_matcher()
queries={
 'ai-financing':'(Volta OR CoreWeave OR Lambda OR Crusoe OR Nebius OR IREN OR "Applied Digital" OR AirTrunk OR Firmus OR "SB Energy") ("price talk" OR loan OR pricing OR flexed OR pulled OR postponed) when:7d',
 'korean-memory':'(삼성전자 OR SK하이닉스) (HBM OR DRAM OR 부품 OR 감산 OR 주문) when:7d',
 'gpu-collateral':'("GPU collateral" OR "GPU-backed" OR "GPU useful life" OR "GPU depreciation" OR "GPU residual value" OR "chip lease") when:7d'}
def pull(item):
 key,q=item
 locale={'hl':'ko','gl':'KR','ceid':'KR:ko'} if key=='korean-memory' else {'hl':'en-US','gl':'US','ceid':'US:en'}
 url='https://news.google.com/rss/search?'+urllib.parse.urlencode(dict(q=q,**locale))
 try:
  raw=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=30).read()
  (HERE/f'intake-{key}.xml').write_bytes(raw)
  items=[{k:el.findtext(k) for k in ['title','pubDate','link','source']} for el in ET.fromstring(raw).findall('./channel/item')]
  return key,dict(query=q,locale=locale,url=url,items=items,sha256=hashlib.sha256(raw).hexdigest())
 except Exception as e:return key,dict(query=q,error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as p: results=dict(p.map(pull,queries.items()))
files,history=h.headlines('2026-09-16')
phrases=['Volta price talk','Volta loan pricing','CoreWeave loan pricing','GPU useful life','GPU collateral','GPU depreciation','HBM order cut','DRAM component shipments']
C.WATCH_FOR={'VULCAN':phrases}
live=[('LIVE-'+key,row['title']) for key,v in results.items() for row in v.get('items',[])]
synthetic=[('CONTROL','Volta price talk raised on loan'),('CONTROL','Volta loan pricing delayed'),('CONTROL','CoreWeave loan pricing revised'),('CONTROL','GPU useful life assumptions changed'),('CONTROL','GPU collateral liquidated'),('CONTROL','GPU depreciation schedules extended'),('CONTROL','HBM order cut denied; shipments increase'),('CONTROL','DRAM component shipments rise')]
hits={phrase:[{'date':d,'title':t} for d,t in history+live+synthetic if ('VULCAN',phrase) in C.match_watch_for(t)] for phrase in phrases}
out={'as_of':datetime.now(timezone.utc).isoformat(),'query_results':results,'history_unique':len(history),'history_files':len(files),'phrase_hits':hits,'lane_config_sha256':hashlib.sha256(Path(C.__file__).read_bytes()).hexdigest()}
(HERE/'intake-design-results.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'counts':{k:len(v.get('items',[])) for k,v in results.items()},'errors':{k:v.get('error') for k,v in results.items() if 'error'in v},'history':len(history),'hits':{k:len(v) for k,v in hits.items()}},ensure_ascii=False))
