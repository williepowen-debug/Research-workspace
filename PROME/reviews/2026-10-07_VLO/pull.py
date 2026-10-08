"""Bounded VLO consumer evidence capture; no gate mutations."""
import json
from pathlib import Path
from datetime import datetime, timezone
import concurrent.futures as cf
import requests
import yfinance as yf

out = Path(__file__).parent
def quote(symbol):
    t = yf.Ticker(symbol)
    info = t.info
    result = {'identity': {k: info.get(k) for k in ['symbol','shortName','expireDate','regularMarketPrice','regularMarketTime']}}
    for interval, period in [('1m','7d'),('1d','1mo')]:
        frame = t.history(period=period, interval=interval, auto_adjust=False)
        frame.to_csv(out / (symbol + '_' + interval + '.csv'))
        if interval == '1m':
            frame = frame.tz_convert('America/New_York')
            w = frame.between_time('14:28','14:30')
            result['windows'] = {}
            for date, g in w.groupby(w.index.date):
                v = g.Volume.sum()
                result['windows'][str(date)] = {'bars':g.index.strftime('%H:%M').tolist(),'volume':int(v),'typical_vwap':float((((g.High+g.Low+g.Close)/3)*g.Volume).sum()/v) if v else None,'close_vwap':float((g.Close*g.Volume).sum()/v) if v else None}
        else:
            result['daily'] = frame.tail(5).reset_index().to_dict('records')
    return symbol, result

results = {'retrieved_utc':datetime.now(timezone.utc).isoformat(), 'quotes':{}, 'federal_register':{}}
for symbol in ['HOX26.NYM','CLX26.NYM']:
    try: k,v=quote(symbol); results['quotes'][k]=v
    except Exception as e: results['quotes'][symbol]={'error':str(e)}
for term in ['diesel export','distillate export','petroleum product export','export control']:
    try:
        r=requests.get('https://www.federalregister.gov/api/v1/documents.json',params={'conditions[term]':term,'conditions[publication_date][gte]':'2026-10-02','per_page':100,'order':'newest'}, timeout=30)
        r.raise_for_status(); body=r.json()
        results['federal_register'][term]={'url':r.url,'count':body.get('count'),'results':body.get('results')}
    except Exception as e: results['federal_register'][term]={'error':str(e)}
(out/'evidence.json').write_text(json.dumps(results,indent=2,default=str))
print(json.dumps(results,indent=2,default=str))
