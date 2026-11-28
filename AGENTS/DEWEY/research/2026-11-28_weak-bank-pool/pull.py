"""Leg C pull: whole FDIC BankFind financials population, 3/31/2019 to 9/30/2026 (31 quarters), plus the FDIC failed-bank CSV.
Run from repo root: python3 AGENTS/DEWEY/research/2026-11-28_weak-bank-pool/pull.py <outdir>
Writes fdic-<REPDTE>.json.gz + meta (row count must equal API total, else exit 1) and failed-banks.csv.
"""
import json, sys, time, gzip, hashlib, urllib.request, urllib.parse, datetime, os
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
F = 'CERT,NAME,REPDTE,STALP,BKCLASS,ASSET,EQ,INTAN,LNATRES,NCLNLS,ORE,NETINCQ,BRO,DEP,RBC,RBCRWAJ,RBC1RWAJ,IDT1CER,RBC1AAJ,LNLSGR'
F2 = 'CERT,REPDTE,RBCT1'   # supplementary pull (fdic-t1-<REPDTE>.json.gz): tier 1 capital, so set 2 and 1d avoid GAAP AOCI
D = [f'{y}{md}' for y in range(2019, 2027) for md in ('0331', '0630', '0930', '1231')]
D = [d for d in D if d <= '20260930']
def get(url):
    for a in range(4):
        try: return urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'research-client'}), timeout=180).read()
        except Exception as e: print('retry', e); time.sleep(5)
    sys.exit(1)
for d in D:
    p = f'{OUT}/fdic-{d}.json.gz'
    if os.path.exists(p): continue
    url = 'https://api.fdic.gov/banks/financials?' + urllib.parse.urlencode({'filters': f'REPDTE:{d}', 'fields': F, 'limit': '10000', 'format': 'json', 'sort_by': 'CERT', 'sort_order': 'ASC'})
    raw = get(url); j = json.loads(raw); n, t = len(j['data']), j['meta']['total']
    open(p, 'wb').write(gzip.compress(raw))
    json.dump({'url': url, 'retrieved_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'rows': n, 'total': t, 'sha256_payload': hashlib.sha256(raw).hexdigest()}, open(f'{OUT}/fdic-{d}-meta.json', 'w'), indent=1)
    print(d, n, t, flush=True)
    if n != t: sys.exit(1)
    time.sleep(1)
for d in D:
    p = f'{OUT}/fdic-t1-{d}.json.gz'
    if os.path.exists(p): continue
    url = 'https://api.fdic.gov/banks/financials?' + urllib.parse.urlencode({'filters': f'REPDTE:{d}', 'fields': F2, 'limit': '10000', 'format': 'json', 'sort_by': 'CERT', 'sort_order': 'ASC'})
    raw = get(url); j = json.loads(raw); n, t = len(j['data']), j['meta']['total']
    open(p, 'wb').write(gzip.compress(raw)); print('t1', d, n, t, flush=True)
    if n != t: sys.exit(1)
    time.sleep(0.5)
raw = get('https://www.fdic.gov/bank-failures/download-data.csv'); open(f'{OUT}/failed-banks.csv', 'wb').write(raw)
print('failed-banks.csv', len(raw), hashlib.sha256(raw).hexdigest())
