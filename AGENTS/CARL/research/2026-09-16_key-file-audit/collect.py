"""Read-only source retrieval; canonical updates are separate from collection."""
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor
import importlib.util
import json
import sys
import urllib.request

HERE = Path(__file__).resolve().parent
CARL = HERE.parents[1]
spec = importlib.util.spec_from_file_location('thresholds', CARL/'scripts/thresholds.py')
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
URLS = {
    'nfib_august.pdf': 'https://www.nfib.com/wp-content/uploads/2026/09/NFIB-SBET-Report-August-2026.pdf',
    'crop0926.txt': 'https://esmis.nal.usda.gov/sites/default/release-files/796056/crop0926.txt',
    'mba_q2.html': 'https://www.mba.org/news-and-research/newsroom/news/2026/08/13/mortgage-delinquencies-decrease-slightly-in-the-second-quarter-of-2026',
    'attom_july.html': 'https://www.attomdata.com/news/market-trends/foreclosures/july-2026-foreclosure-market-report/',
    'fair.html': 'https://www.cfpnet.com/key-statistics-data/',
    'fomc_statement.html': 'https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm',
    'fomc_sep.pdf': 'https://www.federalreserve.gov/monetarypolicy/files/fomcprojtabl20260916.pdf',
    'fsa_head': 'https://studentaid.gov/sites/default/files/fsawg/datacenter/library/PortfoliobyLoanStatus.xls',
}

def fetch(item):
    name, url = item
    result = {'url': url, 'checked_utc': datetime.now(timezone.utc).isoformat()}
    try:
        req = urllib.request.Request(url, method='HEAD' if name == 'fsa_head' else 'GET',
                                     headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=35) as r:
            result['status'] = r.status
            result['headers'] = {k: v for k, v in r.headers.items()
                                  if k.lower() in ['content-type', 'content-length', 'last-modified', 'etag']}
            if name != 'fsa_head':
                body = r.read()
                (HERE/name).write_bytes(body)
                result['bytes'] = len(body)
    except Exception as e:
        result['error_type'] = type(e).__name__
        result['status'] = getattr(e, 'code', None)
    return name, result

def series(sid):
    return sid, {'url': 'https://fred.stlouisfed.org/series/'+sid,
                 'observations': helper.fred_fetch(sid, limit=15)}

selected = set(sys.argv[1:])
with ThreadPoolExecutor(max_workers=6) as pool:
    sources = dict(pool.map(fetch, [(k, v) for k, v in URLS.items() if not selected or k in selected]))
    data = {} if selected else dict(pool.map(series, ['PSAVERT', 'PCEC96', 'DSPIC96', 'DCOILBRENTEU']))
receipt = {'retrieved_utc': datetime.now(timezone.utc).isoformat(), 'sources': sources, 'series': data}
(HERE/('followup_sources.json' if selected else 'sources.json')).write_text(json.dumps(receipt, indent=2)+'\n')
print(json.dumps(sources, indent=2))
for sid, value in data.items():
    print(sid, value['observations'][:3])
