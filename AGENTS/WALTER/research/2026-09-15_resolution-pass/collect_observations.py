"""Dated read-only provider pull; never changes a fire ledger or dashboard cache."""
import concurrent.futures
import datetime
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / 'FORGE/tools/market-data'))
from fetch import fred_fetch, price_history

IDS = ['BAMLH0A0HYM2', 'BAMLH0A3HYC', 'VIXCLS', 'T5YIFR', 'DGS30',
       'ICSA', 'SOFR', 'IORB', 'CPILFESL', 'BAMLH0A0HYEY']

def collect(series):
    return series, fred_fetch(series, limit=12)

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        data = dict(pool.map(collect, IDS))
    data['prices'] = price_history(['WAL', 'KRE', 'BZX26.NYM'], days=16)
    data['retrieved_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    Path(__file__).with_name('observations.json').write_text(json.dumps(data, indent=2, allow_nan=False, default=str)+'\n')
    print('Saved dated observations; inspect completeness and source calendars before grading.')
