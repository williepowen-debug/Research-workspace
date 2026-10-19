import requests,pathlib,json,concurrent.futures,datetime
P=pathlib.Path(__file__).resolve().parent
ciks={'MOS':1285785,'HII':1501585,'ADM':7084,'CPRT':900075}
def get(t):
 s,c=t;u='https://data.sec.gov/submissions/CIK'+str(c).zfill(10)+'.json';stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
 try:
  r=requests.get(u,headers={'User-Agent':'Mozilla/5.0'},timeout=18);(P/'raw'/('submissions-'+s+'.json')).write_bytes(r.content);out=dict(symbol=s,url=u,status=r.status_code,requested_at=stamp)
  if r.status_code==200:
   d=r.json()['filings']['recent'];out['filings']=[{k:d[k][i] for k in ['accessionNumber','filingDate','reportDate','acceptanceDateTime','form','primaryDocument','items'] if k in d} for i,date in enumerate(d['filingDate']) if '2026-07-24'<=date<='2026-10-19' and d['form'][i] in ['8-K','8-K/A','10-Q','10-K']]
  return out
 except Exception as e:return dict(symbol=s,url=u,error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as x:out=list(x.map(get,ciks.items()))
(P/'sec-inventory.json').write_text(json.dumps(out,indent=2)+'\n')
for row in out:
 print(row['symbol'],row.get('status'),len(row.get('filings',[])))
 for f in row.get('filings',[]):print(f['filingDate'],f['form'],f.get('reportDate'),f['primaryDocument'],f.get('items'))
