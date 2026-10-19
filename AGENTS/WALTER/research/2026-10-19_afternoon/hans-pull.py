import sys,os,json,importlib.util,concurrent.futures
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path('/home/willi/Research-workspace'); OUT=ROOT/'AGENTS/WALTER/research/2026-10-19_afternoon'
os.environ['FORGE_CACHE_DIR']=str(OUT/'hans-cache')
sys.path.insert(0,str(ROOT/'FORGE/tools/market-data')); import fetch
fetch.AUDIT_LOG=OUT/'hans-market-audit.log'
spec=importlib.util.spec_from_file_location('eu',ROOT/'AGENTS/HANS/scripts/fetch_eu.py'); eu=importlib.util.module_from_spec(spec);spec.loader.exec_module(eu)
def storage():
 r,e=eu.agsi_eu(); return {'row':r,'error':e,'norm':eu.agsi_norm(r[0]) if r else None}
jobs={'AGSI':storage,'ECB_AAA10Y':lambda:eu.ecb(eu.AAA10Y,6),'BOE_10Y_PAR':lambda:eu.boe('IUDMNPY'),'prices':lambda:fetch.price_fetch(['TTFX26.NYM','EURUSD=X'])}
out={'fetched_utc':datetime.now(timezone.utc).isoformat()}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as p:
 for k,v in zip(jobs,p.map(lambda f:f(),jobs.values())):out[k]=v
(OUT/'hans-observations.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
