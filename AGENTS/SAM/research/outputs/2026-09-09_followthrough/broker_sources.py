"""Retrieve publisher links discovered on their current home pages; preserve source clocks."""
from pathlib import Path
from datetime import datetime,timezone
from concurrent.futures import ThreadPoolExecutor
import urllib.request,json,hashlib
P=Path(__file__).resolve().parent
URLS={'ueda-september-forecast.pdf':'https://www.uedayagi.com/wp/wp-content/uploads/2026/09/202609jukyu.pdf','cme-currency-sep8.pdf':'https://www.cmegroup.com/daily_bulletin/current/Section07_Currency_Futures.pdf','central-september-forecast.pdf':'https://www.central-tanshi.com/media/files/_u/market_schedule/fmjuqf202609.pdf','central-sep9-provisional.pdf':'https://www.central-tanshi.com/media/files/_u/short_term_market_report/centdaily20260909.pdf','ueda-september.html':'https://www.uedayagi.com/fundingforecast/2026-9/'}
def fetch(item):
 name,url=item
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=25) as r:
   data=r.read(); headers=dict(r.headers)
  (P/'raw'/name).write_bytes(data)
  return dict(file='raw/'+name,url=url,sha256=hashlib.sha256(data).hexdigest(),retrieved_at=datetime.now(timezone.utc).isoformat(),headers=headers)
 except Exception as exc:return dict(file=name,url=url,error=str(exc))
with ThreadPoolExecutor(max_workers=3) as pool:records=list(pool.map(fetch,URLS.items()))
(P/'broker-final-manifest.json').write_text(json.dumps(records,indent=2)+'\n'); print(json.dumps(records,indent=2))
