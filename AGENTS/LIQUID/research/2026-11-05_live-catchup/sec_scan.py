"""Latest 10-Q/8-K per card name, and Q2/Q3 XBRL NAV and FV/Cost. Read-only."""
import sys,json,os,time,urllib.request
UA=os.environ.get('SEC_CONTACT') or ''
print('SEC_CONTACT set:',bool(UA))
CIK={'FSK':1422183,'BXSL':1736035,'GSBD':1572694,'OBDC':1655888,'ARCC':1287750,'MAIN':1396440}
def get(u):
    r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA or 'research'}),timeout=40); time.sleep(0.2); return json.loads(r.read())
for t,c in CIK.items():
    try:
        s=get(f'https://data.sec.gov/submissions/CIK{c:010d}.json')
        f=s['filings']['recent']
        rows=[(f['form'][i],f['filingDate'][i],f['reportDate'][i],f['accessionNumber'][i],f['primaryDocument'][i]) for i in range(len(f['form'])) if f['form'][i] in('10-Q','10-K','8-K') and f['filingDate'][i]>='2026-07-15']
        print(t,s['name'],[r for r in rows if r[0]!='8-K'][:3],'8K',[r[1] for r in rows if r[0]=='8-K'][:4])
    except Exception as e: print(t,'FAIL',repr(e))
