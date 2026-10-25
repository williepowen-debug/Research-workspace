"""Bounded public-source capture for Will's current bottom-evidence check."""
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor
import hashlib, json, urllib.request

P = Path(__file__).resolve().parent
urls = {
    'GLD_issuer_archive.xlsx': 'https://api.spdrgoldshares.com/api/v1/historical-archive?exchange=NYSE&lang=en&product=gld',
    'treasury_real.html': 'https://home.treasury.gov/resource-center-data-chart-center/interest-rates/TextView?type=daily_treasury_real_yield_curve&field_tdr_date_value=2026',
    'cftc_legacy.txt': 'https://www.cftc.gov/dea/newcot/deafut.txt',
    'cftc_gold.html': 'https://www.cftc.gov/dea/futures/deacmxsf.htm',
    'wgc_etf.html': 'https://www.gold.org/goldhub/data/gold-etfs-holdings-and-flows',
    'fed_h15.html': 'https://www.federalreserve.gov/releases/h15/',
}
for ticker in ['GLD', 'SPY', 'DX-Y.NYB']:
    urls[ticker+'.json'] = f'https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?range=2y&interval=1d&events=div%2Csplits'

def get(item):
    name, url = item
    row = {'file':name, 'url':url, 'requested_utc':datetime.now(timezone.utc).isoformat()}
    try:
        req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
        with urllib.request.urlopen(req,timeout=35) as r:
            body=r.read(); row.update(status=r.status, final_url=r.url)
        (P/name).write_bytes(body)
        row.update(bytes=len(body),sha256=hashlib.sha256(body).hexdigest())
    except Exception as e:
        row['error']=str(e)
    return row

with ThreadPoolExecutor(max_workers=5) as pool:
    rows = list(pool.map(get,urls.items()))
(P/'access.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps(rows,indent=2))
