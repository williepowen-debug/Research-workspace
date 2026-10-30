"""C9 commission 2026-10-30: GLD close below July low — liquidation test. Saves raw public responses + hashes; no grading."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote
import hashlib,json
from curl_cffi import requests
HERE=Path(__file__).resolve().parent
START=1735689600  # 2025-01-01 UTC
END=1793419200    # 2026-10-31 04:00 UTC
D=['GLD','IAU','SLV','GDX','GDXJ','PPLT','PALL','CPER','SPY','QQQ','IWM','TLT','IEF','HYG','^VIX','DX-Y.NYB','^TNX','BTC-USD','GCZ26.CMX','SIZ26.CMX','HGZ26.CMX','CL=F','USDJPY=X','CNH=X']
I=['GLD','SPY','QQQ','GDX','SLV','DX-Y.NYB','^TNX','^VIX','GCZ26.CMX','TLT']
urls={}
for t in D: urls[t.replace('^','').replace('=','_')+'.json']=f'https://query1.finance.yahoo.com/v8/finance/chart/{quote(t,safe="")}?period1={START}&period2={END}&interval=1d&events=div%2Csplits&includeAdjustedClose=true'
for t in I: urls['intraday_'+t.replace('^','').replace('=','_')+'.json']=f'https://query1.finance.yahoo.com/v8/finance/chart/{quote(t,safe="")}?range=5d&interval=5m&includePrePost=false'
urls.update({
 'GLD_issuer_archive.xlsx':'https://api.spdrgoldshares.com/api/v1/historical-archive?exchange=NYSE&lang=en&product=gld',
 'treasury_real.csv':'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_real_yield_curve&field_tdr_date_value=2026&page&_format=csv',
 'treasury_nominal.csv':'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv',
 'fred_DFII10.csv':'https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFII10',
 'fred_DTWEXBGS.csv':'https://fred.stlouisfed.org/graph/fredgraph.csv?id=DTWEXBGS',
 'fred_BAMLH0A0HYM2.csv':'https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2',
 'cftc_disagg_other_lf.htm':'https://www.cftc.gov/dea/futures/other_lf.htm',
 'cftc_legacy_deafut.txt':'https://www.cftc.gov/dea/newcot/deafut.txt',
 'cftc_disagg_f_disagg.txt':'https://www.cftc.gov/dea/newcot/f_disagg.txt',
 'wgc_etf_page.html':'https://www.gold.org/goldhub/data/gold-etfs-holdings-and-flows',
 'cme_margins_probe_SKIPPED.txt':None,
})
urls={k:v for k,v in urls.items() if v}
def get(item):
 name,url=item;row={'file':name,'url':url,'requested_utc':datetime.now(timezone.utc).isoformat()}
 try:
  r=requests.get(url,impersonate='chrome',timeout=45);(HERE/name).write_bytes(r.content)
  row.update(status=r.status_code,bytes=len(r.content),sha256=hashlib.sha256(r.content).hexdigest(),received_utc=datetime.now(timezone.utc).isoformat())
 except Exception as e:row['error']=str(e)
 return row
rows=list(ThreadPoolExecutor(max_workers=6).map(get,urls.items()))
(HERE/'access.json').write_text(json.dumps(rows,indent=2)+'\n')
for r in rows:print(r['file'],r.get('status',r.get('error')),r.get('bytes'))
