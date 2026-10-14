"""Bounded source diagnostics; only owned evidence writes, no grades or credentials."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import datetime as dt
import hashlib
import json
import sys
import urllib.error
import urllib.parse
import urllib.request

HERE = Path(__file__).resolve().parent
BRENT = HERE.parents[1]
sys.path.insert(0, str(BRENT.parents[1] / 'FORGE/tools/market-data'))
import fetch as forge

KEY = forge.EIA_API_KEY
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126.0.0.0 Safari/537.36'
def eia_url(path, **extra):
    params = {'api_key': KEY, **extra}
    return 'https://api.eia.gov/v2/' + path + '?' + urllib.parse.urlencode(params)

common = {'frequency': 'weekly', 'data[0]': 'value', 'sort[0][column]': 'period', 'sort[0][direction]': 'desc', 'length': 2}
jobs = [
    ('util-current-series', eia_url('petroleum/pnp/wiup/data/', **common, **{'facets[series][]': 'WPULEUS3'})),
    ('util-route-metadata', eia_url('petroleum/pnp/wiup/')),
    ('util-facet-list', eia_url('petroleum/pnp/wiup/facet/series/', length=500)),
    ('cftc-www-raw', 'https://www.cftc.gov/dea/newcot/f_disagg.txt'),
    ('cftc-bare-raw', 'https://cftc.gov/dea/newcot/f_disagg.txt'),
]
public_jobs = [
    ('public-eia-retail', 'https://www.eia.gov/petroleum/gasdiesel/'),
    ('public-fedex-surcharge', 'https://www.fedex.com/en-us/shipping/fuel-surcharge.html'),
    ('public-adnoc-habshan', 'https://www.adnocgas.ae/en/news-and-media/press-releases/2026/q2-2026-results'),
    ('public-valero-q2', 'https://investorvalero.com/news/news-details/2026/Valero-Energy-Reports-Second-Quarter-2026-Results/default.aspx'),
    ('public-satorp-media', 'https://satorp.com/en/media/'),
    ('public-tuapse-profile', 'https://www.rosneft.com/about/Rosneft_today/Operational_structure/Refining/tuapsinskijnpz/'),
    ('public-aramco-q2', 'https://india.aramco.com/en/news-media/news/2026/aramco-announces-second-quarter-and-half-year-2026-results'),
]
def pull(job):
    name, url = job
    rec = {'name': name, 'retrieved_at_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
           'source_path_without_credentials': url.split('?')[0]}
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=35) as response:
            body = response.read()
            rec.update(http_status=response.status, bytes=len(body), sha256=hashlib.sha256(body).hexdigest())
            text = body.decode('utf-8', errors='replace')
            if KEY:
                text = text.replace(KEY, '[REDACTED]')
            suffix = '.json' if name.startswith('util-') else '.txt'
            (HERE / (name + suffix)).write_text(text)
            if name.startswith('util-'):
                data = json.loads(text).get('response', {})
                rows = data.get('data', []) if isinstance(data, dict) else []
                rec.update(total=data.get('total') if isinstance(data, dict) else None,
                           rows=rows[:2] if isinstance(rows, list) else [])
    except Exception as exc:
        rec['error_type'] = type(exc).__name__
        if getattr(exc, 'code', None) is not None:
            rec['http_status'] = exc.code
    return rec

if __name__ == '__main__':
    public_only = '--public-only' in sys.argv
    with ThreadPoolExecutor(max_workers=5) as executor:
        receipts = list(executor.map(pull, public_jobs if public_only else jobs))
    output = 'public-source-receipts.json' if public_only else 'source-receipts.json'
    (HERE / output).write_text(json.dumps(receipts, indent=2)+'\n')
    print(json.dumps(receipts, indent=2))
