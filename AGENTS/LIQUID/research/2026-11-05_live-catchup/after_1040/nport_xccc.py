"""Latest public N-PORT holdings for XCCC (series S000075710), BondBloxx ETF Trust. Read-only."""
import sys,json,time,re,urllib.request,xml.etree.ElementTree as ET,pathlib
sys.path.insert(0,'scripts')
from sec_contact import sec_ua
ua=sec_ua(); P=pathlib.Path(__file__).parent; CIK=1879238; SER='S000075710'
def raw(u):
    b=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':ua}),timeout=60).read(); time.sleep(.15); return b
s=json.loads(raw(f'https://data.sec.gov/submissions/CIK{CIK:010d}.json'))
f=s['filings']['recent']
hits=[(f['filingDate'][i],f['reportDate'][i],f['accessionNumber'][i],f['primaryDocument'][i]) for i in range(len(f['form'])) if f['form'][i]=='NPORT-P']
print('NPORT-P filings',len(hits),'latest dates',sorted({h[1] for h in hits})[-3:], 'filed',sorted({h[0] for h in hits})[-3:])
found=[]
for fd,rd,acc,doc in sorted(hits,reverse=True)[:60]:
    u=f"https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace('-','')}/primary_doc.xml"
    try: x=raw(u)
    except Exception as e: print('skip',acc,repr(e)); continue
    if SER.encode() in x[:6000]:
        (P/f'nport_{acc}.xml').write_bytes(x); found.append((fd,rd,acc)); print('MATCH',fd,rd,acc,len(x)); break
print('found',found)
