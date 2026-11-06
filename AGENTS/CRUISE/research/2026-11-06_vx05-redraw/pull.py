#!/usr/bin/env python3
"""Pull NCLH filing list and XBRL facts for the VX-CRU-05 redraw. SEC contact comes from scripts/sec_contact.py."""
import sys, json, pathlib, urllib.request, time
ROOT=pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'scripts'))
from sec_contact import sec_ua
RAW=pathlib.Path(sys.argv[1])  # scratch directory; filings are not committed
def get(url):
    r=urllib.request.Request(url,headers={'User-Agent':sec_ua(),'Accept-Encoding':'identity'})
    return urllib.request.urlopen(r,timeout=60).read()
CIK='0001513761'
(RAW/'submissions.json').write_bytes(get(f'https://data.sec.gov/submissions/CIK{CIK}.json'))
time.sleep(.2)
(RAW/'companyfacts.json').write_bytes(get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{CIK}.json'))
print('ok')
