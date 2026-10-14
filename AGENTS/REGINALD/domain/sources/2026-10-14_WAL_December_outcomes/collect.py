"""One bounded public quote/chain snapshot for Will's requested December probabilities."""
from pathlib import Path
from datetime import datetime, date
from zoneinfo import ZoneInfo
import json, math
import yfinance as yf

base=Path(__file__).resolve().parent
yf.set_tz_cache_location('/tmp/reginald-wal-december-yf')
t=yf.Ticker('WAL'); info=t.info
assert info['symbol']=='WAL' and 'Western Alliance' in info['longName']
quote={k:info.get(k) for k in ['symbol','longName','regularMarketPrice','regularMarketTime','exchangeDataDelayedBy','regularMarketPreviousClose']}
quote['trade_ET']=datetime.fromtimestamp(quote['regularMarketTime'],ZoneInfo('America/New_York')).isoformat()
assert quote['trade_ET'].startswith('2026-10-14')
chain=t.option_chain('2026-12-18')
cols=['contractSymbol','lastTradeDate','strike','lastPrice','bid','ask','volume','openInterest','impliedVolatility','inTheMoney']
def records(frame):
    frame=frame.loc[(frame.strike>=50)&(frame.strike<=100),[c for c in cols if c in frame.columns]].copy()
    frame['lastTradeDate']=frame['lastTradeDate'].astype(str)
    return json.loads(frame.to_json(orient='records'))
data={'retrieved_ET':datetime.now(ZoneInfo('America/New_York')).isoformat(),'public_vendor':'Yahoo through yfinance','quote':quote,'expiry':'2026-12-18','calls':records(chain.calls),'puts':records(chain.puts),'limits':'Last trade timestamp is not bid/ask timestamp. Vendor IV is not independently repriced; American exercise/dividends/skew unmodeled. Not a physical probability or live executable quote certificate.'}
(base/'quote-and-chain.json').write_text(json.dumps(data,indent=2)+'\n')
for k in [65,70,72.5,75]:
    row=next(r for r in data['puts'] if r['strike']==k)
    print(k,{c:row[c] for c in ['bid','ask','impliedVolatility','lastTradeDate']})
print(json.dumps({'retrieved_ET':data['retrieved_ET'],'quote':quote}))
