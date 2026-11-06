"""Base-rate inputs for MIDAS-18..22, 2026-11-06, before registration. Saves raw public responses."""
from pathlib import Path
from urllib.parse import quote
import hashlib,json,time
from datetime import datetime,timezone
from curl_cffi import requests
H=Path(__file__).resolve().parent
U={}
for t in ['SLV']:
    U[f'{t}_max.json']=f'https://query1.finance.yahoo.com/v8/finance/chart/{t}?period1=1136073600&period2={int(time.time())}&interval=1d&events=div%2Csplits'
for y in range(2015,2026):
    U[f'westmetall_{y}.html']=f'https://www.westmetall.com/en/markdaten.php?action=table&field=LME_Cu_stock&year={y}'
U['wpic_quarterly_page.html']='https://platinuminvestment.com/supply-and-demand/platinum-quarterly'
rows=[]
for n,u in U.items():
    try:
        r=requests.get(u,impersonate='chrome',timeout=40);(H/n).write_bytes(r.content)
        rows.append(dict(file=n,url=u,status=r.status_code,bytes=len(r.content),sha256=hashlib.sha256(r.content).hexdigest(),utc=datetime.now(timezone.utc).isoformat()))
        print(n,r.status_code,len(r.content))
    except Exception as e: print(n,'ERR',e); rows.append(dict(file=n,url=u,error=str(e)))
(H/'access.json').write_text(json.dumps(rows,indent=1)+'\n')
