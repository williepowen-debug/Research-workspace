import sys,json,time,urllib.request
sys.path.insert(0,'scripts')
from sec_contact import sec_ua
ua=sec_ua()
for t,c in {'FSK':1422183,'BXSL':1736035,'GSBD':1572694,'OBDC':1655888,'MAIN':1396440}.items():
    r=json.loads(urllib.request.urlopen(urllib.request.Request(f'https://data.sec.gov/submissions/CIK{c:010d}.json',headers={'User-Agent':ua}),timeout=40).read()); time.sleep(.2)
    f=r['filings']['recent']
    print(t,c,*[ (f['accessionNumber'][i],f['primaryDocument'][i]) for i in range(len(f['form'])) if f['form'][i]=='10-Q' and f['reportDate'][i]=='2026-03-31'][0])
