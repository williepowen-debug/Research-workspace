import sys,json,time,urllib.request
sys.path.insert(0,'scripts')
from sec_contact import sec_ua
ua=sec_ua()
def get(u):
    r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':ua}),timeout=40); time.sleep(.2); return json.loads(r.read())
for t,c in {'GSBD':1572694,'MAIN':1396440}.items():
    f=get(f'https://data.sec.gov/submissions/CIK{c:010d}.json')['filings']['recent']
    print(t,[(f['form'][i],f['filingDate'][i],f['reportDate'][i],f['accessionNumber'][i],f['primaryDocument'][i]) for i in range(len(f['form'])) if f['filingDate'][i]>='2026-09-25' and f['form'][i] in('10-Q','8-K')])
s=get('https://www.sec.gov/files/company_tickers_mf.json')
idx=s['fields']; rows=[dict(zip(idx,r)) for r in s['data'] if r[idx.index('symbol')]=='XCCC']
print('XCCC',rows)
