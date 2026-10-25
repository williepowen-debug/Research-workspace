"""Dated public-source capture; only writes this source directory."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,urllib.request
import yfinance as yf

HERE=Path(__file__).resolve().parent
meta={'captured_at':datetime.now(timezone.utc).isoformat(),'sources':{}}
for ticker in ['SPY','IEF','TLT']:
 try:
  d=yf.Ticker(ticker).history(start='2004-11-18',end='2026-10-24',auto_adjust=False,actions=True)
  assert not d.empty and 'Adj Close' in d and 'Dividends' in d,ticker
  d.index=d.index.tz_localize(None).normalize()
  assert str(d.index[-1].date())=='2026-10-23',(ticker,d.index[-1])
  p=HERE/(ticker+'.csv');d.to_csv(p)
  meta['sources'][ticker]={'source':'Yahoo MIRROR via yfinance; explicit auto_adjust=False; Adj Close is dividend-adjusted market-return proxy',
     'rows':len(d),'start':str(d.index[0].date()),'end':str(d.index[-1].date()),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
     'nonzero_dividend_rows':int((d.Dividends!=0).sum()),'nonzero_split_rows':int((d['Stock Splits']!=0).sum())}
 except Exception as e:meta['sources'][ticker]={'error':str(e)}
urls={
 'EIA_WTI_daily.xls':'https://www.eia.gov/dnav/pet/hist_xls/RWTCd.xls',
 'EIA_WTI_daily.html':'https://www.eia.gov/dnav/pet/hist/RWTCD.htm',
 'IEF_issuer.html':'https://www.ishares.com/us/products/239456/ishares-710-year-treasury-bond-etf',
 'TLT_issuer.html':'https://www.ishares.com/us/products/239454/ishares-20-year-treasury-bond-etf',
 'SPY_issuer.html':'https://www.ssga.com/us/en/individual/etfs/state-street-spdr-sp-500-etf-trust-spy',
}
for fn,url in urls.items():
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
  with urllib.request.urlopen(req,timeout=40) as r:body=r.read()
  (HERE/fn).write_bytes(body)
  meta['sources'][fn]={'url':url,'bytes':len(body),'sha256':hashlib.sha256(body).hexdigest()}
 except Exception as e:meta['sources'][fn]={'url':url,'error':str(e)}
(HERE/'access.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta,indent=2))
