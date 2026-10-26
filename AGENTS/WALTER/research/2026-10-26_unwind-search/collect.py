"""One-off Will-directed evidence pull; no recurring collector or trading rule."""
import concurrent.futures as cf
import datetime as dt
import hashlib
import json
from pathlib import Path
import requests
import yfinance as yf

OUT = Path(__file__).resolve().parent
yf.set_tz_cache_location(str(OUT / '.cache'))

def price(symbol):
    retrieved = dt.datetime.now(dt.timezone.utc).isoformat()
    try:
        t = yf.Ticker(symbol)
        daily = t.history(period='5d', interval='1d', auto_adjust=False, actions=False)
        bars = t.history(period='1d', interval='1m', auto_adjust=False, actions=False)
        prior = daily[daily.index.strftime('%Y-%m-%d') < '2026-10-26'].dropna(subset=['Close'])
        bars = bars.dropna(subset=['Close'])
        if prior.empty or bars.empty:
            return symbol, {'error': 'no prior or current bars', 'retrieved': retrieved}
        last = bars.iloc[-1]
        p = float(prior.iloc[-1]['Close'])
        return symbol, {'retrieved': retrieved, 'observed': bars.index[-1].isoformat(),
            'prior_date': prior.index[-1].strftime('%Y-%m-%d'), 'prior_raw_close': p,
            'last': float(last['Close']), 'change_pct': (float(last['Close'])/p-1)*100,
            'bars': [{'t': i.isoformat(), 'c': float(r['Close']), 'v': int(r['Volume'])}
                     for i,r in bars.iterrows()]}
    except Exception as e:
        return symbol, {'error': str(e), 'retrieved': retrieved}

def primary(item):
    name, url = item
    try:
        r = requests.get(url, timeout=25)
        record = {'url':url,'retrieved':dt.datetime.now(dt.timezone.utc).isoformat(),
                  'status':r.status_code,'sha256':hashlib.sha256(r.content).hexdigest()}
        if r.status_code == 200:
            if 'json' in r.headers.get('Content-Type',''):
                record['data'] = r.json()
            else:
                from bs4 import BeautifulSoup
                text = BeautifulSoup(r.text, 'html.parser').get_text(' ',strip=True)
                record['text'] = text[:12000]
        return name,record
    except Exception as e:
        return name,{'url':url,'error':str(e)}

if __name__ == '__main__':
    symbols=['BRL=X','JPY=X','MXN=X','ZAR=X','AUDJPY=X','EURJPY=X','EWZ',
             'EWW','EZA','EMB','HYG','LQD','BKLN','^GSPC','QQQ','KRE','^VIX','GLD','BTC-USD']
    with cf.ThreadPoolExecutor(max_workers=6) as pool:
        prices=dict(pool.map(price,symbols))
    (OUT/'prices.json').write_text(json.dumps(prices,indent=2)+'\n')
    urls={
      'repo-results':'https://markets.newyorkfed.org/api/rp/repo/all/results/latest.json',
      'repo-announcements':'https://markets.newyorkfed.org/api/rp/repo/all/announcements/latest.json',
      'sofr':'https://markets.newyorkfed.org/api/rates/secured/sofr/last/5.json',
      'b3-price-band':'https://sistemasweb.b3.com.br/PlantaoNoticias/Noticias/Detail?agencia=17&dataNoticia=2026-10-26+09%3A07%3A56&idNoticia=3527929',
      'retail-treasury':'https://www.tesourodireto.com.br/ja/w/atraso-na-abertura-do-mercado'}
    with cf.ThreadPoolExecutor(max_workers=5) as pool:
        official=dict(pool.map(primary,urls.items()))
    (OUT/'primary-retrievals.json').write_text(json.dumps(official,indent=2)+'\n')
    for s,x in prices.items():
        print(s, x.get('observed'), round(x.get('change_pct',0),3), x.get('error',''))
    for k,x in official.items():
        print(k,x.get('status'),str(x.get('data',x.get('text',x.get('error'))))[:1600])
