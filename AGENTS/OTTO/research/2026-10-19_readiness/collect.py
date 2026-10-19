"""Bounded s032 source capture. Run from any cwd with repository .venv Python.

Sources are explicitly supplied; this does not grade forecasts or mutate ledgers.
"""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
import subprocess
import urllib.request
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent
UA = {'User-Agent': 'OTTO Research willi.research@gmail.com'}

def collect(name, url):
    manifest_path = ROOT / 'sources.json'
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    entry = {'url': url, 'accessed_utc': datetime.now(timezone.utc).isoformat()}
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
            data = r.read()
            entry.update(status=r.status, final_url=r.url, content_type=r.headers.get('Content-Type'))
        ext = '.pdf' if data.startswith(b'%PDF') else '.json' if url.endswith('.json') else '.html'
        path = ROOT / 'sources' / (name + ext)
        path.parent.mkdir(exist_ok=True)
        path.write_bytes(data)
        entry.update(path=str(path.relative_to(ROOT)), sha256=hashlib.sha256(data).hexdigest(), bytes=len(data))
        if ext == '.pdf':
            subprocess.run(['pdftotext', '-layout', str(path), str(path.with_suffix('.txt'))], check=True)
        elif ext == '.html':
            soup = BeautifulSoup(data, 'html.parser')
            for x in soup(['script', 'style']): x.decompose()
            path.with_suffix('.txt').write_text(soup.get_text('\n', strip=True))
    except Exception as e:
        entry['error'] = str(e)
    manifest[name] = entry
    manifest_path.write_text(json.dumps(manifest, indent=2) + '\n')
    print(name, entry.get('status', entry.get('error')), entry.get('bytes', ''))

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('name')
    p.add_argument('url')
    args = p.parse_args()
    collect(args.name, args.url)
