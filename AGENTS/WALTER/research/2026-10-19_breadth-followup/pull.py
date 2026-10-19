"""Public-source bounded pull. No credentials or changes outside this study."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib, json, subprocess, urllib.parse

D = Path(__file__).resolve().parent
(D / 'raw').mkdir(exist_ok=True)
symbols = ['SPY', 'RSP', 'QQQ', 'QQEW', 'IWM', 'QUAL', 'SPHQ', 'SPHB',
           'XLK', 'XLC', 'XLY', 'XLF', 'XLV', 'XLI', 'XLP', 'XLE', 'XLU', 'XLRE', 'XLB']

def get(item):
    name, url = item
    start = datetime.now(timezone.utc).isoformat()
    p = subprocess.run(['curl', '-sS', '-L', '--max-time', '18', '-A', 'Mozilla/5.0', url], capture_output=True)
    raw = p.stdout
    path = D / 'raw' / name
    path.write_bytes(raw)
    result = {'name': name, 'url': url, 'start': start, 'end': datetime.now(timezone.utc).isoformat(),
              'curl_rc': p.returncode, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}
    if name.endswith('.json'):
        try:
            z = json.loads(raw)['chart']['result'][0]
            result.update(bars=len(z.get('timestamp', [])), granularity=z['meta'].get('dataGranularity'))
        except Exception as e:
            result['parse_error'] = type(e).__name__
    return result

items = [(f'chart-{s}.json', 'https://query1.finance.yahoo.com/v8/finance/chart/' + s + '?' + urllib.parse.urlencode({
    'period1': '1041379200', 'period2': '1792368000', 'interval': '1d',
    'events': 'div,splits', 'includeAdjustedClose': 'true'})) for s in symbols]
items += [(f'{s}.csv', 'https://fred.stlouisfed.org/graph/fredgraph.csv?id=' + s)
          for s in ['BAMLH0A0HYM2', 'BAMLH0A3HYC', 'BAMLC0A0CM']]
with ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(get, items))
(D / 'source-receipt.json').write_text(json.dumps(results, indent=2) + '\n')
for r in results:
    print(r['name'], r['bytes'], r.get('bars'), r.get('granularity'), r.get('parse_error'), flush=True)
