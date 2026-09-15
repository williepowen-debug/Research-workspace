"""Public-source retrieval only. Input URL manifest; raw bytes and dated receipts."""
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor
import json
import hashlib
import urllib.request
import sys
from bs4 import BeautifulSoup

out = Path(__file__).resolve().parent
manifest = Path(sys.argv[1]) if len(sys.argv) > 1 else out / 'urls.json'

def fetch(item):
    name, url = item
    row = dict(name=name, url=url, retrieved=datetime.now(timezone.utc).isoformat())
    try:
        request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Accept': '*/*'})
        with urllib.request.urlopen(request, timeout=25) as response:
            blob = response.read()
            row.update(status=response.status, final_url=response.url)
        suffix = '.pdf' if blob.startswith(b'%PDF') else '.html'
        (out / (name + suffix)).write_bytes(blob)
        row.update(bytes=len(blob), sha256=hashlib.sha256(blob).hexdigest())
        if suffix == '.html':
            soup = BeautifulSoup(blob, 'html.parser')
            for tag in soup(['script', 'style']):
                tag.decompose()
            (out / (name + '.txt')).write_text(soup.get_text('\n', strip=True))
            row['links'] = [{'text': a.get_text(' ', strip=True), 'href': a['href']} for a in soup.select('a[href]') if '.pdf' in a['href'].lower()]
    except Exception as exc:
        row['error'] = f'{type(exc).__name__}: {exc}'
    print(name, row.get('status', row.get('error')), row.get('bytes', ''), flush=True)
    return row

with ThreadPoolExecutor(max_workers=4) as pool:
    rows = list(pool.map(fetch, json.loads(manifest.read_text()).items()))
(out / (manifest.stem + '-receipts.json')).write_text(json.dumps(rows, indent=2) + '\n')
