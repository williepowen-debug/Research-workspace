"""Weekly contract-map review, 2026-11-06: mapped month vs next listed active month, volume and open-interest-free read."""
from pathlib import Path
from urllib.parse import quote
import json
from curl_cffi import requests
H=Path(__file__).resolve().parent
PAIRS=[('GCZ26.CMX','GCG27.CMX'),('SIZ26.CMX','SIH27.CMX'),('HGZ26.CMX','HGH27.CMX'),('PLF27.NYM','PLJ27.NYM'),('PAZ26.NYM','PAH27.NYM')]
out={}
for a,b in PAIRS:
    row={}
    for t in (a,b):
        r=requests.get(f'https://query1.finance.yahoo.com/v8/finance/chart/{quote(t)}?range=15d&interval=1d',impersonate='chrome',timeout=30)
        (H/f'{t}.json').write_bytes(r.content); j=r.json()['chart']['result'][0]; q=j['indicators']['quote'][0]
        from datetime import datetime,timezone
        row[t]=[(datetime.fromtimestamp(x,timezone.utc).strftime('%m-%d'),v,c) for x,v,c in zip(j['timestamp'],q['volume'],q['close'])][-5:-1]
    out[a]=row; print(a,row[a]); print(b,row[b])
(H/'review_output.json').write_text(json.dumps(out,indent=1)+'\n')
