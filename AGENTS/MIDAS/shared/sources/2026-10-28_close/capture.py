"""One requested close snapshot; saves raw public responses, never grades forecasts."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote
import hashlib,json
from curl_cffi import requests
HERE=Path(__file__).resolve().parent
START=1735689600  # 2025-01-01 00:00 UTC
END=1793246400    # 2026-10-29 04:00 UTC (2026-10-29 00:00 EDT)
TICKERS=['GLD','SLV','PPLT','PALL','CPER','GCZ26.CMX','SIZ26.CMX','PLF27.NYM','PAZ26.NYM','HGZ26.CMX','DX-Y.NYB','^GSPC']
urls={t.replace('^','')+'.json':f'https://query1.finance.yahoo.com/v8/finance/chart/{quote(t,safe="")}?period1={START}&period2={END}&interval=1d&events=div%2Csplits&includeAdjustedClose=true' for t in TICKERS}
urls.update({'GLD_issuer_archive.xlsx':'https://api.spdrgoldshares.com/api/v1/historical-archive?exchange=NYSE&lang=en&product=gld','treasury_real.csv':'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_real_yield_curve&field_tdr_date_value=2026&page&_format=csv','westmetall_2026.html':'https://www.westmetall.com/en/markdaten.php?action=table&field=LME_Cu_stock','westmetall_2025.html':'https://www.westmetall.com/en/markdaten.php?action=table&field=LME_Cu_stock&year=2025','westmetall_2024.html':'https://www.westmetall.com/en/markdaten.php?action=table&field=LME_Cu_stock&year=2024'})
def get(item):
 name,url=item;row={'file':name,'url':url,'requested_utc':datetime.now(timezone.utc).isoformat()}
 try:
  r=requests.get(url,impersonate='chrome',timeout=40);(HERE/name).write_bytes(r.content)
  row.update(status=r.status_code,bytes=len(r.content),sha256=hashlib.sha256(r.content).hexdigest(),received_utc=datetime.now(timezone.utc).isoformat())
 except Exception as e:row['error']=str(e)
 return row
rows=list(ThreadPoolExecutor(max_workers=4).map(get,urls.items()))
(HERE/'access.json').write_text(json.dumps(rows,indent=2)+'\n')
for r in rows:print(r['file'],r.get('status',r.get('error')),r.get('bytes'))
