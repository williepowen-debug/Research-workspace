"""Pull the whole FDIC BankFind financials population for the screen quarters.
Run from repo root:  python3 AGENTS/DEWEY/research/2026-11-27_second-bank-screen/pull_fdic.py <outdir>
Writes fdic-<REPDTE>.json (full rows) + fdic-<REPDTE>-meta.json (query, retrieved_utc, total, sha256).
Public endpoint api.fdic.gov, no key. Row count must equal the API's reported total or the script exits 1.
"""
import json, sys, time, hashlib, urllib.request, urllib.parse, datetime
OUT = sys.argv[1]
DATES = ['20260930','20260630','20260331','20251231','20250930']
FIELDS = ('CERT,NAME,REPDTE,STALP,CITY,BKCLASS,ASSET,LNLSGR,LNREMULT,LNRECONS,LNRENROT,LNRENROW,'
          'NAREMULT,P3REMULT,P9REMULT,NALNLS,P3ASSET,P9ASSET,LNATRES,BRO,DEP,INVSUB,INVSUORE,LNEXAMT,'
          'EQ,RBC,RBCT1,RWAJT,RBCRWAJ,RBC1RWAJ,RBC1AAJ,IDT1CER,RBCT1CER,AVASSETJ,NTREMULQ,NTLNLSQ')
for d in DATES:
    q = {'filters': f'REPDTE:{d}', 'fields': FIELDS, 'limit': '10000', 'format': 'json', 'sort_by': 'CERT', 'sort_order': 'ASC'}
    url = 'https://api.fdic.gov/banks/financials?' + urllib.parse.urlencode(q)
    for attempt in range(4):
        try:
            raw = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'research-client'}), timeout=120).read(); break
        except Exception as e:
            print('retry', d, e); time.sleep(5)
    j = json.loads(raw)
    n, tot = len(j['data']), j['meta']['total']
    open(f'{OUT}/fdic-{d}.json', 'wb').write(raw)
    meta = {'url': url, 'retrieved_utc': datetime.datetime.utcnow().isoformat() + 'Z', 'rows': n, 'total': tot,
            'sha256_payload': hashlib.sha256(raw).hexdigest()}
    json.dump(meta, open(f'{OUT}/fdic-{d}-meta.json', 'w'), indent=1)
    print(d, n, tot)
    if n != tot: sys.exit(1)
    time.sleep(1)
