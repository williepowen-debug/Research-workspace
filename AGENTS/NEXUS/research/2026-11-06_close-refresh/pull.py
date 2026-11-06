"""First-published FRED pull for the 11/6 close refresh. Writes fp_<id>.json here; no owner writes."""
import sys, json, datetime
from pathlib import Path
sys.path.insert(0, '/home/willi/Research-workspace/FORGE/tools/market-data')
import fetch
out = Path(__file__).resolve().parent/'fred'
for s in ['VIXCLS','DFII10','DGS10','DGS2','BAMLH0A0HYM2','BAMLC0A0CM','BAMLH0A1HYBB','BAMLH0A2HYB','BAMLH0A3HYC','ICSA']:
    r = fetch.fred_fetch_vintage(s, limit=8, basis='first-published', observation_start='2026-10-20')
    (out/f'fp_{s}.json').write_text(json.dumps(r, indent=0, default=str))
    rows = r.get('rows') or r.get('observations') or []
    print(s, [(x.get('date'), x.get('value')) for x in rows][-4:], 'short=', r.get('short'), 'missing=', r.get('missing'))
print(datetime.datetime.now().astimezone().isoformat(timespec='seconds'))
