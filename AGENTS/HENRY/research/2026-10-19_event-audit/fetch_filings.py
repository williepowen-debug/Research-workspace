import json,pathlib,requests,concurrent.futures,datetime
from urllib.parse import urljoin
P=pathlib.Path(__file__).resolve().parent
inv=json.loads((P/'sec-inventory.json').read_text());ciks={'MOS':1285785,'HII':1501585,'ADM':7084,'CPRT':900075};jobs=[]
for row in inv:
 for f in row.get('filings',[]):
  url='https://www.sec.gov/Archives/edgar/data/'+str(ciks[row['symbol']])+'/'+f['accessionNumber'].replace('-','')+'/'+f['primaryDocument'];jobs.append((row['symbol'],f,url))
def get(t):
 s,f,u=t;stem=s+'-'+f['filingDate']+'-'+f['accessionNumber'];stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
 try:
  r=requests.get(u,headers={'User-Agent':'Mozilla/5.0'},timeout=18);(P/'raw'/(stem+'.html')).write_bytes(r.content);out=dict(symbol=s,filing=f,url=u,status=r.status_code,requested_at=stamp,file='raw/'+stem+'.html')
  return out
 except Exception as e:return dict(symbol=s,filing=f,url=u,error=str(e),requested_at=stamp)
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:r=list(ex.map(get,jobs))
(P/'filing-receipts.json').write_text(json.dumps(r,indent=2)+'\n');print('filings',len(r),'HTTP200',sum(x.get('status')==200 for x in r))
