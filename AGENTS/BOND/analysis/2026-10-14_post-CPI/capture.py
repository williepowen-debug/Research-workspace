from pathlib import Path
import concurrent.futures as cf,urllib.request,csv,io,json,datetime as dt,sys
from zoneinfo import ZoneInfo
B=Path(__file__).resolve().parents[2]; R=B.parents[1]; O=Path(__file__).parent/'raw'; O.mkdir(exist_ok=True)
sys.path[:0]=[str(B/'monitors'),str(R/'FORGE/tools/market-data')]
import fetch,fr2004_fetch as pd
sources={
 'nominal.csv':'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&_format=csv',
 'real.csv':'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_real_yield_curve&_format=csv',
 'ACM.xls':'https://www.newyorkfed.org/medialibrary/media/research/data_indicators/ACMTermPremium.xls',
 'bund10.csv':'https://api.statistiken.bundesbank.de/rest/download/BBSIS/D.I.ZST.ZI.EUR.S1311.B.A604.R10XX.R.A.A._Z._Z.A?format=csv&lang=en',
 'cpi.html':'https://www.bls.gov/news.release/archives/cpi_10142026.htm',
 'beige.html':'https://www.federalreserve.gov/monetarypolicy/beigebook202610.htm',
 'auction_schedule.pdf':'https://home.treasury.gov/system/files/221/Tentative-Auction-Schedule.pdf',
 'nbim.html':'https://www.nbim.no/en/news-and-insights/submissions-to-ministry/2026/the-government-pension-fund-global--analyses-and-assessments-of-the-investment-strategy-for-bonds/',
 'ministry.html':'https://www.regjeringen.no/en/topics/the-economy/the-government-pension-fund/eksterne-rapporter-og-brev/id2358366/',
 'norway-budget.html':'https://www.regjeringen.no/no/dokumenter/meld.-st.-1-20262027/id3175768/?ch=4',
 'nyfed_rates.json':'https://markets.newyorkfed.org/api/rates/all/latest.json',
}
def get(k,u):
 t=dt.datetime.now(ZoneInfo('America/New_York')).isoformat()
 try:
  with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 BOND research'}),timeout=35) as r: b=r.read();status=r.status
  (O/k).write_bytes(b);return k,{'url':u,'captured_et':t,'status':status,'bytes':len(b)}
 except Exception as e:return k,{'url':u,'captured_et':t,'error':str(e)}
man=dict(cf.ThreadPoolExecutor(8).map(lambda z:get(*z),sources.items()))
for sid in ['BAMLH0A0HYM2','BAMLH0A3HYC','BAMLC0A0CM','BAMLC0A4CBBB','BAMLH0A1HYBB','BAMLH0A2HYB','EFFR','SOFR','IORB','T5YIFR','T10YIE','THREEFYTP10','THREEFY10']:
 try:(O/(sid+'.json')).write_text(json.dumps(fetch.fred_fetch(sid,limit=30),indent=2)+'\n')
 except Exception as e:man[sid]={'error':str(e)}
try:
 sb=pd.current_seriesbreak(dt.date.today());out={k:pd.fetch(k,sb) for k in ['PDPOSGSC-G3L6','PDPOSGSC-G7L11','PDPOSGSC-G11L21','PDPOSGSC-G21']};(O/'dealer.json').write_text(json.dumps({'seriesbreak':sb,'data':out},indent=2))
except Exception as e:man['dealer']={'error':str(e)}
try:
 import yfinance as yf
 symbols=['ZQV26.CBT','ZQX26.CBT','ZQZ26.CBT','ZQF27.CBT','^FVX','^TNX','^TYX','TLT','TBT'];out={}
 for s in symbols:
  h=yf.Ticker(s).history(period='5d',interval='1d',auto_adjust=False)
  out[s]=[{'date':str(i),'close':float(v.Close)} for i,v in h.iterrows()]
 (O/'vendor_daily.json').write_text(json.dumps({'captured_et':dt.datetime.now(ZoneInfo('America/New_York')).isoformat(),'basis':'Yahoo evolving daily bars; not settlement or event-window quote','data':out},indent=2))
except Exception as e:man['vendor']={'error':str(e)}
(O/'manifest.json').write_text(json.dumps(man,indent=2)+'\n');print(json.dumps(man,indent=2))
