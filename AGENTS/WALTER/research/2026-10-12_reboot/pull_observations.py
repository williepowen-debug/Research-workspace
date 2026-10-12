"""Session evidence collector; writes only WALTER-owned evidence and cache."""
import concurrent.futures
import csv
import importlib.util
import io
import json
import os
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
os.environ['FORGE_CACHE_DIR'] = str(HERE / '.cache')
sys.path.insert(0, str(ROOT / 'FORGE/tools/market-data'))
import fetch
fetch.AUDIT_LOG = HERE / 'market-audit.log'

def module(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj

def skew():
    url = 'https://cdn.cboe.com/api/global/us_indices/daily_prices/SKEW_History.csv'
    data = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=30).read().decode('utf-8-sig')
    (HERE / 'SKEW_History.csv').write_text(data)
    return list(csv.DictReader(io.StringIO(data)))[-12:]

def storage():
    eu = module('walter_eu', 'AGENTS/HANS/scripts/fetch_eu.py')
    row, err = eu.agsi_eu()
    return {'row': row, 'error': err, 'norm': eu.agsi_norm(row[0]) if row else None}

series = ['BAMLH0A0HYM2','BAMLH0A3HYC','VIXCLS','ICSA','T5YIFR','SOFR','IORB','DGS2','DGS5','DGS10','DGS20','DGS30','T10YIE','DFII10']
jobs = {s: lambda s=s: fetch.fred_fetch(s, 12) for s in series}
jobs.update({'prices': lambda: fetch.price_fetch(['KRE','WAL','OZK','^VIX','QQQ','USO','CLX26.NYM','CLZ26.NYM','BZZ26.NYM','RBX26.NYM','RBZ26.NYM','HOX26.NYM','HOZ26.NYM','TTFX26.NYM','EURUSD=X']), 'Cushing': lambda: fetch.eia_fetch('W_EPC0_SAX_YCUOK_MBBL',limit=2), 'SKEW': skew, 'AGSI': storage})
result = {'as_of': datetime.now(timezone.utc).isoformat(), 'basis': 'Fetched evidence; intraday/vendor bars do not complete settlement or daily-close grades.'}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    pending = {pool.submit(fn): key for key, fn in jobs.items()}
    for future in concurrent.futures.as_completed(pending):
        key = pending[future]
        try:
            result[key] = future.result()
        except Exception as exc:
            result[key] = {'error': type(exc).__name__}
(HERE / 'observations.json').write_text(json.dumps(result, indent=2, default=str)+'\n')
print('Saved observations.json; source keys:', ', '.join(result))
