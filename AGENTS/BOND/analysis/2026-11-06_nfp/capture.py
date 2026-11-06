"""BOND 2026-11-06 October-payrolls rates read. Issuer files and vendor bars land in raw/ with a manifest.
Nothing here grades a gate. Copied from 2026-11-05_catchup/capture.py; intraday leg added."""
from pathlib import Path
import concurrent.futures as cf,urllib.request,json,datetime as dt,sys
from zoneinfo import ZoneInfo
B=Path(__file__).resolve().parents[2]; R=B.parents[1]; O=Path(__file__).parent/'raw'; O.mkdir(exist_ok=True)
sys.path[:0]=[str(B/'monitors'),str(R/'FORGE/tools/market-data')]
import fetch
ET=ZoneInfo('America/New_York')
sources={
 'nominal.csv':'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&_format=csv',
 'real.csv':'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_real_yield_curve&_format=csv',
 'nyfed_rates.json':'https://markets.newyorkfed.org/api/rates/all/latest.json',
}
def get(k,u):
 t=dt.datetime.now(ET).isoformat()
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 BOND research'}),timeout=35) as r: b=r.read();status=r.status
  (O/k).write_bytes(b);return k,{'url':u,'captured_et':t,'status':status,'bytes':len(b)}
 except Exception as e:return k,{'url':u,'captured_et':t,'error':str(e)}
man=dict(cf.ThreadPoolExecutor(8).map(lambda z:get(*z),sources.items()))
for sid in ['BAMLH0A0HYM2','BAMLH0A3HYC','BAMLC0A0CM','BAMLC0A4CBBB','BAMLH0A1HYBB','BAMLH0A2HYB','EFFR','SOFR','IORB','T5YIFR','T10YIE','VIXCLS']:
 try:(O/(sid+'.json')).write_text(json.dumps(fetch.fred_fetch(sid,limit=400),indent=2)+'\n')
 except Exception as e:man[sid]={'error':str(e)}
(O/'manifest.json').write_text(json.dumps(man,indent=2)+'\n')
import yfinance as yf
T=['^FVX','^TNX','^TYX','ZT=F','ZF=F','ZN=F','ZB=F','ZQZ26.CBT','ZQF27.CBT','ZQH27.CBT','ZQV27.CBT','TLT','TIP','HYG','LQD','KRE','SPY','DX-Y.NYB','BZF27.NYM','GC=F']
d=yf.download(T,period='5d',interval='5m',progress=False,auto_adjust=False,prepost=True)['Close']
d.to_csv(O/'intraday_5m.csv')
e=yf.download(T,period='1mo',interval='1d',progress=False,auto_adjust=False)['Close']
e.to_csv(O/'daily.csv')
print('captured',dt.datetime.now(ET).isoformat(),d.shape,e.shape)
print(json.dumps(man,indent=1))
