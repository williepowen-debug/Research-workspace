"""Capture primary baseline files; separate from the 10:26 option snapshot."""
import hashlib
import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parent
URLS = {
    'wpsr-table1.csv': 'https://ir.eia.gov/wpsr/table1.csv',
    'wpsr-table2.csv': 'https://ir.eia.gov/wpsr/table2.csv',
    'wpsr-table9.csv': 'https://ir.eia.gov/wpsr/table9.csv',
    'steo-publication-check.html': 'https://www.eia.gov/outlooks/steo/',
    'wpsr-schedule.html': 'https://www.eia.gov/petroleum/supply/weekly/schedule.php',
    'moran-sep2.html': 'https://www.moranshipping.com/news/bulletins/port-update-port-arthur-tx-slash-sabine-slash-neches-2026-09-02',
}

def fetch(item):
    name, url = item
    result = dict(file=name, url=url, retrieved_at=datetime.now(timezone.utc).isoformat())
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=40) as response:
            raw = response.read()
            (OUT/name).write_bytes(raw)
            result.update(status=response.status, bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
    except Exception as exc:
        result['error'] = str(exc)
    return result

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(fetch, URLS.items()))
    (OUT/'baseline-fetch-manifest.json').write_text(json.dumps(results, indent=2)+'\n')
    for result in results:
        print(json.dumps(result))
