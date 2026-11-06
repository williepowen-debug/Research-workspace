"""WGC Q3 GDT central-bank page, September reported statistics. Saves raw; grades nothing."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json
from curl_cffi import requests
H=Path(__file__).resolve().parent
U={'wgc_gdt_q3_central_banks.html':'https://www.gold.org/goldhub/research/gold-demand-trends/gold-demand-trends-q3-2026/central-banks','wgc_cb_stats_sep2026.html':'https://www.gold.org/goldhub/gold-focus/2026/11/central-bank-gold-statistics-september-2026'}
rows=[]
for n,u in U.items():
    r=requests.get(u,impersonate='chrome',timeout=40);(H/n).write_bytes(r.content)
    rows.append(dict(file=n,url=u,status=r.status_code,bytes=len(r.content),sha256=hashlib.sha256(r.content).hexdigest(),utc=datetime.now(timezone.utc).isoformat())); print(n,r.status_code,len(r.content))
(H/'access_wgc.json').write_text(json.dumps(rows,indent=1)+'\n')
