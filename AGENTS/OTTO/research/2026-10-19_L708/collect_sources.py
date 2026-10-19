"""Bounded L708 primary-source inventory. Writes only this owned result directory."""
import concurrent.futures,datetime,gzip,hashlib,json,pathlib,urllib.request
BASE=pathlib.Path(__file__).resolve().parent
UA={'User-Agent':'OTTO Research willi.research@gmail.com'}
ISSUERS={'ENVA':1529864,'CVNA':1690820,'CRMT':799850,'WRLD':108385,'OPRT':1538716,'CACC':885550,'OMF':1584207,'CPSS':889609}
def get(t,cik):
 u=f'https://data.sec.gov/submissions/CIK{cik:010d}.json'
 try:
  data=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=25).read()
  (BASE/'sources'/f'{t}-submissions.json').write_bytes(data)
  j=json.loads(data)['filings']['recent']; out=[]
  for i,d in enumerate(j['filingDate']):
   if '2026-09-15'<=d<='2026-10-19':
    acc=j['accessionNumber'][i]; doc=j['primaryDocument'][i]
    out.append({'ticker':t,'date':d,'form':j['form'][i],'accession':acc,'items':j['items'][i],'url':f'https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace("-","")}/{doc}'})
  return t,out
 except Exception as e:return t,{'error':str(e),'url':u}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:rows=dict(ex.map(lambda x:get(*x),ISSUERS.items()))
(BASE/'filing_inventory.json').write_text(json.dumps(rows,indent=2))
for t,rs in rows.items():
 print(t,rs if isinstance(rs,dict) else [(x['date'],x['form'],x['accession'],x['items']) for x in rs if x['form'] in ['8-K','10-Q','10-K']])
