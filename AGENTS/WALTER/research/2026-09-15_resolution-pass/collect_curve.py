"""Read-only missing curve legs for the FT-11 alternate path."""
from pathlib import Path
import sys,json,datetime
root=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(root/'FORGE/tools/market-data'))
from fetch import fred_fetch
out={s:fred_fetch(s,limit=12) for s in ('DGS10','DGS20','DGS30')}
out['retrieved_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
Path(__file__).with_name('curve-observations.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
print({s:v.get('error','available') for s,v in out.items() if isinstance(v,dict)})
