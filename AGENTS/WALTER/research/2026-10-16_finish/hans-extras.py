import requests,json,concurrent.futures
from pathlib import Path
from datetime import datetime,timezone
OUT=Path('/home/willi/Research-workspace/AGENTS/WALTER/research/2026-10-16_finish')
urls={'eurostat-sep-final':'https://ec.europa.eu/eurostat/web/products-euro-indicators/w/2-16102026-ap','eurostat-api':'https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/prc_hicp_manr?lang=EN&geo=EA21&coicop=CP00_X_EF_AT&sinceTimePeriod=2026-07','eurusd-chart':'https://query1.finance.yahoo.com/v8/finance/chart/EURUSD=X?interval=1d&range=1mo','ttf-chart':'https://query1.finance.yahoo.com/v8/finance/chart/TTFX26.NYM?interval=1d&range=1mo'}
def get(kv):
 k,u=kv
 try:
  r=requests.get(u,timeout=35,headers={'User-Agent':'Mozilla/5.0'});(OUT/('hans-'+k+'.txt')).write_text(r.text);return k,{'status':r.status_code,'bytes':len(r.content),'url':r.url}
 except Exception as e:return k,{'error':type(e).__name__}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as p:out=dict(p.map(get,urls.items()))
try:
 u='https://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd'
 r=requests.post(u,data={'bld':'dbms/MDC/STAT/standard/MDCSTAT02201','locale':'ko_KR','mktId':'STK','trdDd':'20261016','money':'1','csvxls_isNo':'false'},headers={'User-Agent':'Mozilla/5.0','Referer':'https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020301'},timeout=35)
 (OUT/'hans-krx-response.txt').write_text(r.text);out['krx']={'status':r.status_code,'bytes':len(r.content)}
except Exception as e:out['krx']={'error':type(e).__name__}
out['fetched_utc']=datetime.now(timezone.utc).isoformat();(OUT/'hans-extra-receipt.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
