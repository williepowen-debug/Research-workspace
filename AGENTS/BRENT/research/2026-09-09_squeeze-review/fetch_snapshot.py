import json, urllib.request, subprocess, hashlib
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor
root=Path('/home/willi/Research-workspace'); out=root/'AGENTS/BRENT/research/2026-09-09_squeeze-review';out.mkdir(exist_ok=True)
urls={
'retail.html':'https://www.eia.gov/petroleum/gasdiesel/',
'retail-gas.xls':'https://www.eia.gov/petroleum/gasdiesel/xls/pswrgvwall.xls',
'retail-diesel.xls':'https://www.eia.gov/petroleum/gasdiesel/xls/psw18vwall.xls',
'aug26_base.xlsx':'https://www.eia.gov/outlooks/steo/archives/aug26_base.xlsx',
'steo-current.html':'https://www.eia.gov/outlooks/steo/',
'wpsr-current.html':'https://www.eia.gov/petroleum/supply/weekly/',
'wpsr-table1.xls':'https://www.eia.gov/petroleum/supply/weekly/xls/wpsrsummary.xls',
'wpsr-table2.xls':'https://www.eia.gov/petroleum/supply/weekly/xls/wpsr2.xls',
'cboe-USO.json':'https://cdn.cboe.com/api/global/delayed_quotes/options/USO.json',
'cboe-XLE.json':'https://cdn.cboe.com/api/global/delayed_quotes/options/XLE.json',
}
def get(item):
 name,url=item;r={'file':name,'url':url,'retrieved_at':datetime.now(timezone.utc).isoformat()}
 try:
  resp=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=35);raw=resp.read();(out/name).write_bytes(raw);r.update(status=resp.status,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),content_type=resp.headers.get('Content-Type'))
 except Exception as e:r['error']=str(e)
 return r
def chain(task):
 ticker,expiry,legs=task;name=ticker+'-'+expiry+'-chain.json';args=[str(root/'.venv/bin/python3'),'AGENTS/TERRY/scripts/chain_fetch.py',ticker,expiry,'--type','call','--legs',legs,'--json','--no-cache'];r={'file':name,'args':args,'retrieved_at':datetime.now(timezone.utc).isoformat()}
 try:
  p=subprocess.run(args,cwd=root,capture_output=True,text=True,timeout=80);(out/name).write_text(p.stdout);(out/(name+'.stderr')).write_text(p.stderr);r.update(rc=p.returncode,stdout_bytes=len(p.stdout),stderr_bytes=len(p.stderr))
 except Exception as e:r['error']=str(e)
 return r
with ThreadPoolExecutor(max_workers=5) as pool:
 futures=[pool.submit(get,item) for item in urls.items()]+[pool.submit(chain,t) for t in [('USO','2026-10-16','135'),('USO','2026-09-18','150,165'),('XLE','2026-09-30','65')]]
 rows=[f.result() for f in futures]
(out/'fetch-manifest.json').write_text(json.dumps(rows,indent=2))
for r in rows: print(json.dumps(r))
