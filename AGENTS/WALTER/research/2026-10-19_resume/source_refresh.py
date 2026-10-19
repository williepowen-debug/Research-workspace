"""Bounded, read-only refresh for the resumed morning commission. No credentials logged."""
import concurrent.futures as cf
import csv
import datetime as dt
import importlib.util
import io
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('walter_forge', ROOT/'FORGE/tools/market-data/fetch.py')
f = importlib.util.module_from_spec(spec)
spec.loader.exec_module(f)
f.CACHE_DIR = OUT/'.cache'
f.AUDIT_LOG = OUT/'fetch-audit.log'

def history(symbol):
    return f.fred_fetch(symbol, limit=12)

def cboe(symbol):
    url = f'https://cdn.cboe.com/api/global/us_indices/daily_prices/{symbol}_History.csv'
    with urllib.request.urlopen(url, timeout=20) as r:
        raw = r.read()
    (OUT/f'{symbol}_History.csv').write_bytes(raw)
    return {'url':url, 'rows':list(csv.DictReader(io.StringIO(raw.decode('utf-8-sig'))))[-8:]}

jobs = {sid:(lambda s=sid:history(s)) for sid in ['VIXCLS','BAMLH0A3HYC','BAMLC0A0CM','ICSA','SOFR','IORB','T5YIFR','DGS30','DGS20','DGS10','DGS5','DGS2','T10YIE']}
jobs['HY_FIRST_PUBLISHED'] = lambda:f.fred_fetch_vintage('BAMLH0A0HYM2',limit=12,observation_start='2026-10-01')
jobs['CUSHING'] = lambda:f.eia_fetch('W_EPC0_SAX_YCUOK_MBBL',limit=3)
for symbol in ['VIX','VVIX','SKEW']:
    jobs['CBOE_'+symbol] = lambda s=symbol:cboe(s)
result = {'started':dt.datetime.now(dt.timezone.utc).isoformat(),'results':{}}
with cf.ThreadPoolExecutor(max_workers=8) as pool:
    futures={pool.submit(fn):key for key,fn in jobs.items()}
    for future in cf.as_completed(futures):
        key=futures[future]
        try:
            value=future.result()
        except Exception as exc:
            value={'error':type(exc).__name__+': '+str(exc).split('?')[0]}
        result['results'][key]={'retrieved':dt.datetime.now(dt.timezone.utc).isoformat(),'data':value}
result['finished']=dt.datetime.now(dt.timezone.utc).isoformat()
(OUT/'source-refresh.json').write_text(json.dumps(result,indent=2)+'\n')
for key,value in result['results'].items():
    data=value['data']
    print(key,json.dumps(data if isinstance(data,dict) and 'rows' not in data else (data.get('rows',[])[:3] if isinstance(data,dict) else data[:3])))
