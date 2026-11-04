from pathlib import Path
import sys,json,datetime,concurrent.futures,importlib.util,email.utils
BASE=Path('/home/willi/Research-workspace/AGENTS/WALTER')
sys.path.insert(0,'/home/willi/Research-Intake/scripts')
import newsweep_config as c
import fetch_newsweep as fetch
spec=importlib.util.spec_from_file_location('harness',BASE/'tools/watch_for_harness.py');h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
queries=next(v for v in vars(c).values() if isinstance(v,list) and any(isinstance(x,dict) and x.get('label')=='bank-vendor-incidents-core' for x in v))
rows=[x for x in queries if x.get('label','').startswith('bank-vendor-incidents-')]
now=datetime.datetime.now(datetime.timezone.utc)
def pull(row,variant):
 q=row['query'] if variant=='current' else 'when:7d '+row['query']
 out={'label':row['label'],'variant':variant,'query':q,'url':c.google_news_rss_url(q),'captured_at':now.isoformat()}
 try:
  raw=fetch._get(out['url'],timeout=30);items,error=fetch._parse_feed(raw);out['parse_error']=error
  (BASE/'research/2026-11-04_maintenance'/f"supplier-{row['label']}-{variant}.xml").write_bytes(raw)
  for n,x in enumerate(items):
   x['rank']=n+1
   try:x['age_days']=(now-email.utils.parsedate_to_datetime(x['date'])).total_seconds()/86400
   except:x['age_days']=None
   x['cypher_matches']=[p for d,p in c.match_watch_for(x['title']) if d=='CYPHER']
  out['items']=items;out['total']=len(items);out['cap']=c.MAX_ARTICLES_PER_SOURCE
 except Exception as e:out['error']=repr(e)
 return out
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(lambda args:pull(*args),[(r,v) for r in rows for v in ['current','leading7d']]))
(BASE/'research/2026-11-04_maintenance/supplier-results.json').write_text(json.dumps(results,indent=2)+'\n')
for r in results:
 print(r['label'],r['variant'],r.get('total'),r.get('error'))
 for x in r.get('items',[])[:c.MAX_ARTICLES_PER_SOURCE]: print(x['rank'],round(x['age_days'],1) if x['age_days'] is not None else None,x['title'],x['cypher_matches'])
