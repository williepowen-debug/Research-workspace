"""Verify captured sources and derive the bounded scan and timing evidence."""
import csv
from datetime import date
import gzip
import hashlib
import json
from pathlib import Path
import re
import tarfile
from bs4 import BeautifulSoup

B = Path(__file__).resolve().parent
manifest = json.loads((B / 'sources.json').read_text())
def raw(key):
    r = manifest[key]
    if (B/'sources.tar.gz').exists():
        with tarfile.open(B/'sources.tar.gz','r:gz') as archive:
            data=archive.extractfile(r['path']).read()
    else:
        data = (B / r['path']).read_bytes()
    return gzip.decompress(data) if r.get('storage_encoding') == 'gzip' else data

checked = 0
for key, r in manifest.items():
    if 'error' in r:
        continue
    assert hashlib.sha256(raw(key)).hexdigest() == r['sha256'], key
    checked += 1

# Include all 8-K item classes. The original VRM short roll was Item 8.01.
rows = []
for name in ('vrm', 'cacc', 'cps', 'crmt'):
    j = json.loads(raw(name + '_submissions'))['filings']['recent']
    for i, form in enumerate(j['form']):
        d = j['filingDate'][i]
        if form == '8-K' and '2026-09-24' <= d <= '2026-10-19':
            acc = j['accessionNumber'][i]
            cik = {'vrm':1580864,'cacc':885550,'cps':889609,'crmt':799850}[name]
            url = f'https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace("-", "")}/{j["primaryDocument"][i]}'
            captures = [key for key,r in manifest.items() if r['url'] == url and 'error' not in r]
            assert captures, (name, acc, 'uncaptured document')
            rows.append({'borrower':name.upper(),'filing_date':d,'accepted_raw_submissions':j['acceptanceDateTime'][i],
                         'accession':acc,'items':j['items'][i],'url':url,'source_key':captures[-1]})
with (B/'filing_scan.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)

def published(key):
    t = raw(key).decode()
    if key == 'hindenburg_jan02':
        s = BeautifulSoup(t,'html.parser')
        return s.select_one('time.entry-date.published')['datetime']
    match = re.search(r'"datePublished"\s*:\s*"([^"]+)"', t)
    if match:return match.group(1)
    s = BeautifulSoup(t,'html.parser')
    return s.find('meta',attrs={'itemprop':'datePublished'})['content']

timing=[]
for ticker,key,earn,kind in [
    ('CVNA','hindenburg_jan02','2025-02-19','initial'),
    ('CVNA','gotham_jan28','2026-02-18','initial'),
    ('CVNA','gotham_feb18','2026-02-18','follow-up, same Gotham campaign'),
    ('CACC','cacc_bleecker','2023-01-31','initial, older comparison')]:
    stamp=published(key); pub=stamp[:10]
    timing.append({'ticker':ticker,'source_key':key,'publisher_timestamp':stamp,'report_date':pub,
                   'next_actual_earnings':earn,'calendar_days_before':(date.fromisoformat(earn)-date.fromisoformat(pub)).days,
                   'type':kind})
assert [r['calendar_days_before'] for r in timing] == [48,21,0,18]
with (B/'timing.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=list(timing[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(timing)
print(json.dumps({'source_hashes_verified':checked,'failed_capture_attempts':sum('error' in r for r in manifest.values()),
                  '8K_inventory':len(rows),'8K_by_borrower':{n:sum(r['borrower']==n for r in rows) for n in ('VRM','CACC','CPS','CRMT')},
                  'timing_days':[r['calendar_days_before'] for r in timing]},indent=2))
