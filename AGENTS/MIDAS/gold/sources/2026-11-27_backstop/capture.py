"""D:L1113 backstop capture, 2026-11-27 (PROME prome-80). Treasury real/nominal CSVs with the honest client name research-bot/1.0
(WQ-735, Will 2026-11-23); market series through the fleet tool FORGE fetch.py (yfinance; not MIDAS's to change, WQ-735 rule 3).
The SPDR archive was asked ONCE by probe.py (its own record is probe_access.json); it is not asked again here. Grades nothing."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib, json, subprocess, sys, urllib.request
HERE = Path(__file__).resolve().parent; ROOT = HERE.parents[4]
URLS = {
 'treasury_real.csv': 'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_real_yield_curve&field_tdr_date_value=2026&page&_format=csv',
 'treasury_nominal.csv': 'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv'}
rows = []
for name, url in URLS.items():
    row = {'file': name, 'url': url, 'client': 'python urllib, User-Agent research-bot/1.0', 'requested_utc': datetime.now(timezone.utc).isoformat()}
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'research-bot/1.0'}), timeout=60) as r:
            b = r.read(); row['status'] = r.status
        (HERE/name).write_bytes(b); row.update(bytes=len(b), sha256=hashlib.sha256(b).hexdigest(), received_utc=datetime.now(timezone.utc).isoformat())
    except Exception as e:
        row['error'] = repr(e)
    rows.append(row); print(name, row.get('status', row.get('error')), row.get('bytes'))
TICKERS = ['GLD','SLV','PPLT','PALL','CPER','GCZ26.CMX','GCG27.CMX','SIZ26.CMX','SIH27.CMX','PLF27.NYM','PAZ26.NYM','PAH27.NYM','HGZ26.CMX','HGH27.CMX','DX-Y.NYB','^GSPC','^VIX','^TNX','JPY=X','QQQ']
t0 = datetime.now(timezone.utc).isoformat()
p = subprocess.run([sys.executable, str(ROOT/'FORGE/tools/market-data/fetch.py'), 'price', *TICKERS, '--history', '420', '--json'], capture_output=True, text=True, cwd=ROOT)
(HERE/'fetch_history.json').write_text(p.stdout)
rows.append({'file': 'fetch_history.json', 'tool': 'FORGE fetch.py price --history 420 --json', 'rc': p.returncode, 'stderr_tail': p.stderr[-800:], 'requested_utc': t0,
             'received_utc': datetime.now(timezone.utc).isoformat(), 'sha256': hashlib.sha256(p.stdout.encode()).hexdigest()})
print('fetch.py rc', p.returncode, len(p.stdout))
(HERE/'capture_access.json').write_text(json.dumps(rows, indent=2) + '\n')
