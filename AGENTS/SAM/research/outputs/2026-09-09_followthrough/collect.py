"""Fetch the bounded September follow-through evidence; no workbook writes."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone,timedelta
from pathlib import Path
import hashlib,json,urllib.request,urllib.error
import yfinance as yf

OUT=Path(__file__).resolve().parent;RAW=OUT/'raw';RAW.mkdir(exist_ok=True)
URLS={
 'nyfed-sofr.json':'https://markets.newyorkfed.org/api/rates/secured/sofr/last/10.json',
 'nyfed-effr.json':'https://markets.newyorkfed.org/api/rates/unsecured/effr/last/10.json',
 'iorb.csv':'https://fred.stlouisfed.org/graph/?g=1&id=IORB&cosd=2026-08-20&coed=2026-09-09&fq=Daily&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&line_id=IORB&cosd=2026-08-20&coed=2026-09-09&format=csv',
 'vix.csv':'https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv',
 'cftc-legacy.txt':'https://www.cftc.gov/dea/newcot/deafut.txt',
 'cftc-tff.txt':'https://www.cftc.gov/dea/newcot/FinFutWk.txt',
 'boj-jd20260909.xlsx':'https://www.boj.or.jp/en/statistics/boj/fm/juq/d_release/jd/2026/jd20260909.xlsx',
 'boj-jp20260910.xlsx':'https://www.boj.or.jp/en/statistics/boj/fm/juq/d_release/jp/2026/jp20260910.xlsx',
 'boj-current-account.html':'https://www.boj.or.jp/en/statistics/boj/fm/juq/index.htm',
 'totan-forecast.html':'https://www.totan.com/market_report/daily_b.html',
 'totan-actual.html':'https://www.totan.com/market_report/daily_a.html',
 'central-tanshi.html':'https://www.central-tanshi.com/market/market_info.html',
 'u-s-treasury.csv':'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv',
 'eia-steo.pdf':'https://www.eia.gov/outlooks/steo/pdf/steo_full.pdf',
 'eia-security.html':'https://www.eia.gov/outlooks/steo/report/energysecurity/article.php',
 'cme-delivery.html':'https://www.cmegroup.com/markets/fx/fx-delivery.html',
 'cme-2026-holidays.html':'https://www.cmegroup.com/trading-hours.html',
 'boj-policy-calendar.html':'https://www.boj.or.jp/en/mopo/mpmsche_minu/index.htm',
 'fed-calendar.html':'https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm',
 'cpi-calendar.html':'https://www.stat.go.jp/english/data/cpi/158c.html',
}
def fetch(item):
 name,url=item;retrieved=datetime.now(timezone.utc).isoformat()
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 SAM research'})
  with urllib.request.urlopen(req,timeout=35) as response:
   data=response.read();ctype=response.headers.get('Content-Type');final=response.url
  (RAW/name).write_bytes(data)
  return dict(file='raw/'+name,url=url,final_url=final,retrieved_at=retrieved,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),content_type=ctype,status='FETCHED; inspect content and source vintage')
 except Exception as exc:
  return dict(file='raw/'+name,url=url,retrieved_at=retrieved,status='FAILED',error=str(exc))
with ThreadPoolExecutor(max_workers=6) as pool:records=list(pool.map(fetch,URLS.items()))
for record in records:print(record['file'],record['status'],record.get('error',''),flush=True)
(OUT/'source-manifest.json').write_text(json.dumps(records,indent=2)+'\n')
symbols={'6ju26':'6JU26.CME','6jz26':'6JZ26.CME','6jh27':'6JH27.CME','usdjpy':'USDJPY=X','eurjpy':'EURJPY=X','audjpy':'AUDJPY=X','fxy':'FXY','sp500':'^GSPC','move':'^MOVE'}
market=[]
for name,symbol in symbols.items():
 try:
  ticker=yf.Ticker(symbol);end=(datetime.now(timezone.utc).date()+timedelta(days=1)).isoformat()
  history=ticker.history(start='2026-06-22',end=end,auto_adjust=False)
  if history.empty:raise ValueError('Empty history')
  history.to_csv(RAW/(name+'-daily.csv'))
  meta=ticker.history_metadata
  safe={k:meta.get(k) for k in ['symbol','currency','exchangeName','instrumentType','exchangeTimezoneName','regularMarketTime','expireDate','firstTradeDate']}
  market.append(dict(symbol=symbol,file='raw/'+name+'-daily.csv',retrieved_at=datetime.now(timezone.utc).isoformat(),rows=len(history),last=str(history.index[-1]),metadata=safe))
  print(symbol,len(history),str(history.index[-1]),flush=True)
 except Exception as exc:market.append(dict(symbol=symbol,error=str(exc)))
(OUT/'market-manifest.json').write_text(json.dumps(market,indent=2,default=str)+'\n')
