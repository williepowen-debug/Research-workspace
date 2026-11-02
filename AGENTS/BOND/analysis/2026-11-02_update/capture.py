"""BOND 2026-11-02 Will-directed file update capture (copied from 2026-10-29_catchup/capture.py; PDFs/calendars/vendor bars dropped); issuer, mirror and vendor clocks kept separate.
Raw bytes land in raw/ with a manifest; nothing here grades a gate."""
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
 'refunding.html':'https://home.treasury.gov/policy-issues/financing-the-government/quarterly-refunding/most-recent-quarterly-refunding-documents/',
 'nyfed_rates.json':'https://markets.newyorkfed.org/api/rates/all/latest.json',
 'pmms.csv':'https://www.freddiemac.com/pmms/docs/PMMS_history.csv',
}
def get(k,u):
 t=dt.datetime.now(ET).isoformat()
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 BOND research'}),timeout=35) as r: b=r.read();status=r.status
  (O/k).write_bytes(b);return k,{'url':u,'captured_et':t,'status':status,'bytes':len(b)}
 except Exception as e:return k,{'url':u,'captured_et':t,'error':str(e)}
man=dict(cf.ThreadPoolExecutor(8).map(lambda z:get(*z),sources.items()))
for sid in ['BAMLH0A0HYM2','BAMLH0A3HYC','BAMLC0A0CM','BAMLC0A4CBBB','BAMLH0A1HYBB','BAMLH0A2HYB','EFFR','SOFR','IORB','T5YIFR','T10YIE','THREEFYTP10','DFII5','DFII10','DFII30','DGS2','DGS5','DGS10','DGS20','DGS30']:
 try:(O/(sid+'.json')).write_text(json.dumps(fetch.fred_fetch(sid,limit=400),indent=2)+'\n')
 except Exception as e:man[sid]={'error':str(e)}
(O/'manifest.json').write_text(json.dumps(man,indent=2)+'\n');print(json.dumps(man,indent=2))

import fr2004_fetch as fr
sb=fr.current_seriesbreak(dt.date.today())
keys=fr.BUCKETS+[('PDPOSGSC-G3L6','3-6Y'),('PDPOSGSC-G2L3','2-3Y'),('PDPOSGSC-G6L7','6-7Y')]
pd={label:fr.fetch(k,sb) for k,label in keys}
(O/'fr2004.json').write_text(json.dumps({'seriesbreak':sb,'captured_et':dt.datetime.now(ET).isoformat(),'units':'USD billion net stock','series':pd},indent=2)+'\n')
print('FR2004 saved:',{k:max(v) for k,v in pd.items()})
