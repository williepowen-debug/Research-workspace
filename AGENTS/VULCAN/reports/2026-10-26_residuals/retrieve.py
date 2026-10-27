"""One-use source capture for the two October 26 residual studies; no scheduled collector."""
from pathlib import Path
import urllib.request, json, hashlib, datetime, concurrent.futures
HERE=Path(__file__).resolve().parent
UA='VULCAN-research contact williepowen@gmail.com'
ISSUERS={'GOOGL':1652044,'MSFT':789019,'META':1326801,'AMZN':1018724}
def get(url,name):
 req=urllib.request.Request(url,headers={'User-Agent':UA})
 with urllib.request.urlopen(req,timeout=40) as r: data=r.read()
 path=HERE/'sources'/name; path.write_bytes(data)
 return data,{'url':url,'path':str(path.relative_to(HERE)),'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}
def capture(pair):
 tick,cik=pair; raw,meta=get(f'https://data.sec.gov/submissions/CIK{cik:010d}.json',f'{tick}-submissions.json')
 j=json.loads(raw); records=[meta]
 recent=j['filings']['recent']; allarrays=[recent]
 # Full primary index history gives chronological rather than selected-quarter method evidence.
 for page in j['filings'].get('files',[]):
  if tick=='GOOGL' or page.get('filingTo','')>='2026-01-01':
   body,m=get('https://data.sec.gov/submissions/'+page['name'],tick+'-'+page['name']); records.append(m); allarrays.append(json.loads(body))
 rows=[]
 for a in allarrays:
  for i,f in enumerate(a['form']):
   rows.append({k:a.get(k,['']*len(a['form']))[i] for k in ['form','filingDate','reportDate','accessionNumber','primaryDocument','items']})
 rows=sorted({r['accessionNumber']:r for r in rows}.values(),key=lambda r:(r['filingDate'],r['accessionNumber']))
 (HERE/'sources'/f'{tick}-index.json').write_text(json.dumps(rows,indent=2))
 print(tick,'rows',len(rows),'first',rows[0]['filingDate'],'2026 material',[(r['filingDate'],r['form'],r['accessionNumber'],r['primaryDocument']) for r in rows if r['filingDate']>='2026-01-01' and (r['form'] in ('10-K','10-Q','424B2','424B5') or r['form']=='8-K' and any(x in r['items'] for x in ['1.01','2.03']))])
 return records
manifest=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
 for rows in ex.map(capture,ISSUERS.items()): manifest.extend(rows)
(HERE/'sources/INDEX_MANIFEST.json').write_text(json.dumps(manifest,indent=2))
