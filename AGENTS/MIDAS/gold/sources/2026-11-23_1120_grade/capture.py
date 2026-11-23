"""11/20 close capture for MIDAS-11/13/17, DOCKET L819 L1/L2 and the 11/19-11/20 class grade (2026-11-23, PROME prome-77, D:L1113 + D:L819).
Changed from ../2026-11-18_close_grade/capture.py: NO browser-impersonating client (root CLAUDE.md Data Hygiene as PROME restated it 11/23).
Issuer, Treasury: Python's stdlib urllib with its default client string; a refusal is recorded and not retried another way.
Market series: the fleet tool FORGE/tools/market-data/fetch.py (price_history, yfinance), saved as returned. Grades nothing."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib, json, subprocess, sys, urllib.request
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]  # fixed 11/23 after first run resolved AGENTS/ (fetch.py not found)
URLS = {
 'GLD_issuer_archive.xlsx': 'https://api.spdrgoldshares.com/api/v1/historical-archive?exchange=NYSE&lang=en&product=gld',
 'treasury_real.csv': 'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_real_yield_curve&field_tdr_date_value=2026&page&_format=csv',
 'treasury_nominal.csv': 'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv',
}
prior = json.loads((HERE / 'access.json').read_text()) if (HERE / 'access.json').exists() else []
rows = [r for r in prior if r['file'] in URLS]  # a site already asked once this session is never asked again (a refusal is a stop)
done = {r['file'] for r in rows}
for name, url in URLS.items():
    if name in done: continue
    row = {'file': name, 'url': url, 'client': 'python urllib default', 'requested_utc': datetime.now(timezone.utc).isoformat()}
    try:
        with urllib.request.urlopen(urllib.request.Request(url), timeout=60) as r:
            b = r.read(); row['status'] = r.status
        (HERE / name).write_bytes(b)
        row.update(bytes=len(b), sha256=hashlib.sha256(b).hexdigest(), received_utc=datetime.now(timezone.utc).isoformat())
    except Exception as e:
        row['error'] = repr(e)
    rows.append(row); print(name, row.get('status', row.get('error')), row.get('bytes'))
TICKERS = ['GLD','SLV','PPLT','PALL','CPER','GCZ26.CMX','SIZ26.CMX','PLF27.NYM','PAZ26.NYM','HGZ26.CMX','DX-Y.NYB','^GSPC','^VIX','^TNX','SPY','QQQ']
t0 = datetime.now(timezone.utc).isoformat()
p = subprocess.run([sys.executable, str(ROOT / 'FORGE/tools/market-data/fetch.py'), 'price', *TICKERS, '--history', '420', '--json'], capture_output=True, text=True, cwd=ROOT)
(HERE / 'fetch_history.json').write_text(p.stdout)
rows.append({'file': 'fetch_history.json', 'tool': 'FORGE fetch.py price --history 420 --json', 'rc': p.returncode, 'stderr_tail': p.stderr[-800:], 'requested_utc': t0,
             'received_utc': datetime.now(timezone.utc).isoformat(), 'sha256': hashlib.sha256(p.stdout.encode()).hexdigest()})
print('fetch.py rc', p.returncode, len(p.stdout))
(HERE / 'access.json').write_text(json.dumps(rows, indent=2) + '\n')
