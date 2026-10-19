"""Save bounded primary-source excerpts and hashes under OTTO only."""
import csv,concurrent.futures,gzip,hashlib,html,json,pathlib,re,urllib.request
from bs4 import BeautifulSoup
B=pathlib.Path(__file__).resolve().parent
jobs=[]
for t,cik in [('ENVA',1529864),('WRLD',108385),('CACC',885550),('OMF',1584207)]:
 j=json.loads((B/'sources'/f'{t}-submissions.json').read_text())['filings']['recent']
 i=next(i for i,x in enumerate(j['form']) if x=='10-Q' and j['filingDate'][i]<='2026-10-13')
 jobs.append((t+'-latest-10Q',f'https://www.sec.gov/Archives/edgar/data/{cik}/{j["accessionNumber"][i].replace("-","")}/{j["primaryDocument"][i]}'))
for n,u in [('ENVA-SP-20240729','https://www.spglobal.com/ratings/en/regulatory/article/-/view/type/HTML/id/3221986'),('CVNA-SP-20250313','https://www.spglobal.com/ratings/en/regulatory/article/-/view/sourceId/101616201'),('Exeter-SP-20260317','https://www.spglobal.com/ratings/en/regulatory/article/-/view/sourceId/101675261'),('DriveTime-SP-20160510','https://www.spglobal.com/ratings/en/regulatory/article/-/view/sourceId/9635349'),('ICE-FRED-CCC','https://fred.stlouisfed.org/series/BAMLH0A3HYC'),('FINRA-bond-lookup','https://www.finra.org/finra-data/fixed-income/bond')]:jobs.append((n,u))
rows=list(csv.DictReader((B.parents[1]/'workbook/PANEL_10D.tsv').open(),delimiter='\t'))
for r in rows:
 if '2026-09-24'<=r['filing_date']<='2026-10-13':jobs.append((r['deal'].replace(' ','_')+'-20260929',r['source_url']))
def get(job):
 n,u=job
 try:
  d=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'OTTO Research willi.research@gmail.com'}),timeout=25).read();s=' '.join(BeautifulSoup(d,'html.parser').stripped_strings)
  (B/'sources'/f'{n}.html.gz').write_bytes(gzip.compress(d,mtime=0));(B/'sources'/f'{n}.txt').write_text(s)
  return {'name':n,'url':u,'bytes':len(d),'sha256':hashlib.sha256(d).hexdigest(),'text_chars':len(s),'rating_context':[s[max(0,m.start()-110):m.end()+220] for m in list(re.finditer(r'credit rating|ratings|Ratings|Delinquency Trigger|Extension Limit',s))[:8]]}
 except Exception as e:return {'name':n,'url':u,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:out=list(ex.map(get,jobs))
(B/'primary_manifest.json').write_text(json.dumps(out,indent=2))
for x in out:print(x['name'],x.get('bytes',x.get('error')),x.get('rating_context',[])[:3])
# Read another desk's saved publisher snapshot without modifying it; save only relevant rows in OTTO.
p=B.parents[2]/'LIQUID/research/2026-10-15_L708-ccc-gap/hyg-download-2026-10-14-holdings.xls.gz'
s=gzip.open(p,'rt').read();rs=[]
for r in re.findall(r'<ss:Row[^>]*>(.*?)</ss:Row>',s,re.S):rs.append([html.unescape(x) for x in re.findall(r'<ss:Data[^>]*>([^<]*)</ss:Data>',r)])
hi=next(i for i,r in enumerate(rs) if r and r[0]=='Name');hdr=rs[hi]
match=[dict(zip(hdr,r)) for r in rs[hi+1:] if len(r)==len(hdr) and any(x in r[0] for x in ['CARVANA','CREDIT ACCEPTANCE','ONEMAIN'])]
(B/'hyg_candidate_rows.json').write_text(json.dumps({'source':str(p),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'asof':'2026-10-14','candidate_rows':match},indent=2))
