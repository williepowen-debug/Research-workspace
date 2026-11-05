"""Frozen one-use SEC evidence retrieval; no persistent tracking or monitor."""
from pathlib import Path
import json, urllib.request, hashlib, datetime, concurrent.futures, re
from bs4 import BeautifulSoup
HERE=Path(__file__).resolve().parent; S=HERE/'sources'
CIK={'GOOGL':1652044,'MSFT':789019,'META':1326801,'AMZN':1018724}
jobs=[]
for tick,cik in CIK.items():
 for r in json.loads((S/f'{tick}-index.json').read_text()):
  if r['filingDate']<'2026-01-01': continue
  if r['form'].startswith('424B') or r['form'] in ('10-Q','10-K','8-K'):
   accession=r['accessionNumber']; url=f'https://www.sec.gov/Archives/edgar/data/{cik}/{accession.replace("-","")}/{r["primaryDocument"]}'
   jobs.append((tick,r,url))
import pathlib, sys  # WQ-600: SEC contact lives in the gitignored local .env (scripts/sec_contact.py)
sys.path.append(str(next(p for p in pathlib.Path(__file__).resolve().parents if (p / "scripts" / "sec_contact.py").is_file()) / "scripts"))
from sec_contact import sec_ua
def run(job):
 tick,r,url=job; name=f'{tick}-{r["accessionNumber"]}'
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':sec_ua('VULCAN-research contact {}')}),timeout=35) as response: body=response.read()
  (S/(name+'.html')).write_bytes(body)
  soup=BeautifulSoup(body,'html.parser')
  for el in soup(['script','style','ix:header']): el.decompose()
  plain=soup.get_text(' ',strip=True); (S/(name+'.txt')).write_text(plain)
  summary=dict(tick=tick,**r,url=url,path='sources/'+name+'.html',sha256=hashlib.sha256(body).hexdigest(),retrieved_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
  print(tick,r['form'],r['filingDate'],len(body),plain[:180])
  return summary
 except Exception as ex:
  print('FAIL',name,str(ex)); return dict(tick=tick,**r,url=url,error=str(ex))
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool: manifest=list(pool.map(run,jobs))
(S/'DOCUMENT_MANIFEST.json').write_text(json.dumps(manifest,indent=2))
