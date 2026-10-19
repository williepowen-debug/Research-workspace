"""Save this approved Wilmington-specific primary read under OTTO only."""
import concurrent.futures,gzip,hashlib,json,pathlib,re,urllib.request
from bs4 import BeautifulSoup
B=pathlib.Path(__file__).resolve().parent
jobs=[
('mtb-release','https://www.sec.gov/Archives/edgar/data/36270/000003627026000057/ex991release3q26.htm'),
('mtb-8k','https://www.sec.gov/Archives/edgar/data/36270/000003627026000057/mbt-20261016.htm'),
('mtb-deck','https://ir.mtb.com/static-files/5e370b06-317f-4dd2-a3e9-9bccff37b8bb'),
('mtb-quarterly','https://ir.mtb.com/financial-information/quarterly-results'),
('wt-abs-services','https://www.wilmingtontrust.com/institutional-client-services/corporate-trust/structured-finance/asset-mortgage-backed-securities'),
('wt-custody-services','https://www.wilmingtontrust.com/institutional-client-services/custody-and-collateral-services'),
('mtb-submissions','https://data.sec.gov/submissions/CIK0000036270.json')]
def get(job):
 n,u=job
 try:
  raw=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'OTTO Research willi.research@gmail.com'}),timeout=25).read()
  pdf=raw.startswith(b'%PDF');js=n.endswith('submissions');ext='.pdf' if pdf else '.json' if js else '.html.gz';p=B/'sources'/(n+ext);p.write_bytes(gzip.compress(raw,mtime=0) if ext=='.html.gz' else raw)
  if pdf:
   from pdfminer.high_level import extract_text
   s=extract_text(str(p))
  elif js:s=raw.decode()
  else:s=' '.join(BeautifulSoup(raw,'html.parser').stripped_strings)
  (B/'sources'/(n+'.txt')).write_text(s)
  out={'name':n,'url':u,'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'file':p.name}
  if n=='mtb-quarterly':out['webcast_links']=[a.get('href') for a in BeautifulSoup(raw,'html.parser').find_all('a') if 'webcast' in a.get_text().lower()][:3]
  if js:
   j=json.loads(raw)['filings']['recent'];out['recent_10q']=[(j['filingDate'][i],j['accessionNumber'][i]) for i,f in enumerate(j['form']) if f=='10-Q'][:2]
  else:
   out['term_hits']={k:len(list(re.finditer(k,s,re.I))) for k in ['corporate trust','Wilmington','custod','Tricolor','wind.down','exit']}
   out['contexts']=[s[max(0,m.start()-130):m.end()+270] for m in list(re.finditer('corporate trust|non-mortgage|Tricolor|custod',s,re.I))[:15]]
  return out
 except Exception as e:return {'name':n,'url':u,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:out=list(ex.map(get,jobs))
(B/'mtb_manifest.json').write_text(json.dumps(out,indent=2))
for x in out:print(x)
