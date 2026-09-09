"""Fetch links discovered on the BOJ index and the existing authenticated FRED client."""
from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,subprocess,urllib.request
P=Path(__file__).resolve().parent;ROOT=P.parents[4]
URLS={
 'boj-jx20260909.xlsx':'https://www.boj.or.jp/en/statistics/boj/fm/juq/d_release/jx/jx20260909.xlsx',
 'boj-jp20260910-current.xlsx':'https://www.boj.or.jp/en/statistics/boj/fm/juq/d_release/jp/jp20260910.xlsx',
 'central-home.html':'https://www.central-tanshi.com/',
 'ueda-tanshi.html':'https://www.ueda-net.co.jp/market/forecast.html',
 'cme-yen-rulebook.pdf':'https://www.cmegroup.com/rulebook/CME/II/250/253.pdf',
}
def fetch(item):
 name,url=item
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 SAM research'}),timeout=25) as r:data=r.read()
  (P/'raw'/name).write_bytes(data)
  return dict(file='raw/'+name,url=url,sha256=hashlib.sha256(data).hexdigest(),retrieved_at=datetime.now(timezone.utc).isoformat())
 except Exception as exc:return dict(file=name,url=url,error=str(exc))
with ThreadPoolExecutor(max_workers=5) as pool:records=list(pool.map(fetch,URLS.items()))
for series in ['IORB','BAMLH0A0HYM2','BAMLC0A0CM']:
 r=subprocess.run([str(ROOT/'.venv/bin/python3'),str(ROOT/'FORGE/tools/market-data/fetch.py'),'fred',series,'--periods','8','--json'],cwd=ROOT,capture_output=True,text=True)
 (P/'raw'/('fred-'+series+'.json')).write_text(r.stdout)
 (P/'raw'/('fred-'+series+'.stderr.txt')).write_text(r.stderr)
 records.append(dict(series=series,source='existing FORGE FRED client',exit_code=r.returncode,retrieved_at=datetime.now(timezone.utc).isoformat()))
(P/'followup-manifest.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(records,indent=2))
