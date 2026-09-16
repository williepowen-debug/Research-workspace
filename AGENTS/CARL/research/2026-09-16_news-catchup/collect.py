"""Capture source vintages for CARL's September 16 catch-up; no canonical writes."""
import concurrent.futures
import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path
import urllib.request

HERE = Path(__file__).resolve().parent
CARL = HERE.parents[1]
spec = importlib.util.spec_from_file_location('carl_thresholds', CARL / 'scripts/thresholds.py')
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
SERIES = ['RSAFS','RSXFS','RSDBS','RSFSDP','RSGMS','RSCCAS',
          'CUSR0000SAF11','CUSR0000SEFV','CPIAPPSL','CPIAUCSL',
          'BAMLH0A0HYM2','BAMLH0A3HYC','BAMLH0A1HYBB','REVOLNS']

def fetch_series(sid):
    rows = helper.fred_fetch(sid, limit=60)
    return sid, {'url': 'https://fred.stlouisfed.org/series/' + sid, 'observations': rows}

def fetch_url(item):
    name, url = item
    try:
        req = urllib.request.Request(url, headers={'User-Agent':'CARL research research@example.com'})
        with urllib.request.urlopen(req, timeout=30) as r:
            content = r.read()
        (HERE / name).write_bytes(content)
        return name, {'url':url,'bytes':len(content)}
    except Exception as e:
        return name, {'url':url,'error_type':type(e).__name__}

urls = {
 'retail_august.pdf':'https://www.census.gov/retail/marts/www/marts_current.pdf',
 'bread_august.pdf':'https://investor.breadfinancial.com/node/30721/pdf',
 'capitalone_august.pdf':'https://investor.capitalone.com/static-files/0191ea61-5769-40a9-b1fe-300682ded325',
 'wallethub.html':'https://wallethub.com/edu/credit-card-debt-report/127704',
 'wallethub_nominal.html':'https://cdn.wallethub.com/wallethub/embed/127704/linechart-average-debt-not-adjusted-for-inflation.html',
 'wallethub_real.html':'https://cdn.wallethub.com/wallethub/embed/127704/linechart-average-debt-adjusted-for-inflation.html',
 'syf_submissions.json':'https://data.sec.gov/submissions/CIK0001601712.json',
 'cof_submissions.json':'https://data.sec.gov/submissions/CIK0000927628.json',
}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    series = dict(pool.map(fetch_series, SERIES))
    sources = dict(pool.map(fetch_url, urls.items()))
data = {'retrieved_utc':datetime.now(timezone.utc).isoformat(),'series':series,'sources':sources}
(HERE / 'sources.json').write_text(json.dumps(data, indent=2)+'\n')
for sid, payload in series.items():
    print(sid, payload['observations'][:2])
print(json.dumps(sources, indent=2))
