#!/usr/bin/env python3
"""Fetch NCLH quarterly earnings exhibits and 10-Q/10-K documents, 2022-11 to 2026-10, into raw/."""
import sys, json, pathlib, urllib.request, time, re
ROOT=pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'scripts'))
from sec_contact import sec_ua
RAW=pathlib.Path(sys.argv[1])  # scratch directory; filings are not committed
def get(url):
    r=urllib.request.Request(url,headers={'User-Agent':sec_ua(),'Accept-Encoding':'identity'})
    return urllib.request.urlopen(r,timeout=60).read()
s=json.load(open(RAW/'submissions.json'))['filings']['recent']
for f,d,a,i,p in zip(s['form'],s['filingDate'],s['accessionNumber'],s['items'],s['primaryDocument']):
    if d<'2022-11-01': continue
    base=f"https://www.sec.gov/Archives/edgar/data/1513761/{a.replace('-','')}/"
    if f in('10-Q','10-K'):
        out=RAW/f"{d}_{f}.htm"
        if not out.exists():
            out.write_bytes(get(base+p)); time.sleep(.15)
    elif f=='8-K' and '2.02' in i and d>='2022-11-08':
        idx=json.loads(get(base+'index.json')); time.sleep(.15)
        names=[x['name'] for x in idx['directory']['item']]
        ex=[n for n in names if re.search(r'ex.?99|exh?_?99',n,re.I) and n.endswith('.htm')]
        print(d,a,ex[:3])
        for n in ex[:1]:
            out=RAW/f"{d}_8K_{n}"
            if not out.exists():
                out.write_bytes(get(base+n)); time.sleep(.15)
