"""One-session public-source and settlement-window capture; no state grades."""
import concurrent.futures as cf
import json
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import yfinance as yf
from pdfminer.high_level import extract_text

out = Path(__file__).parent
results = {'retrieved_utc': datetime.now(timezone.utc).isoformat(), 'sources': {}, 'contracts': {}}
urls = {
    'oct26.pdf': 'https://www.eia.gov/outlooks/steo/archives/oct26.pdf',
    'sep26.pdf': 'https://www.eia.gov/outlooks/steo/archives/sep26.pdf',
    'weekly.html': 'https://www.eia.gov/petroleum/supply/weekly/',
    'baltic-week40.html': 'https://www.balticexchange.com/en/data-services/WeeklyRoundup/tanker/news/2026/tanker-report-week-40.html',
    'gibson-oct02.html': 'https://www.gibsons.co.uk/report/running-out-of-room/',
    'diesel-order.html': 'https://www.whitehouse.gov/presidential-actions/2026/10/emergency-tax-relief-on-diesel-fuel/',
    'uso.html': 'https://www.uscfinvestments.com/uso',
}

def fetch(item):
    name, url = item
    try:
        r = requests.get(url, timeout=35)
        r.raise_for_status()
        (out/name).write_bytes(r.content)
        if name.endswith('.pdf'):
            (out/(name+'.txt')).write_text(extract_text(out/name))
        elif name.endswith('.html'):
            (out/(name+'.txt')).write_text(BeautifulSoup(r.content, 'html.parser').get_text('\n', strip=True))
        return name, {'url': url, 'status': r.status_code, 'bytes': len(r.content)}
    except Exception as e:
        return name, {'url': url, 'error': type(e).__name__}

results['sources'].update(dict(cf.ThreadPoolExecutor(max_workers=5).map(fetch, urls.items())))
if (out/'weekly.html').exists():
    extra = {}
    soup = BeautifulSoup((out/'weekly.html').read_text(), 'html.parser')
    for a in soup.find_all('a', href=True):
        href = urljoin(urls['weekly.html'], a['href'])
        name = href.split('?')[0].rsplit('/', 1)[-1]
        if name in {'summary.txt', 'psw01.csv', 'psw04.csv', 'psw07.csv', 'psw09.csv', 'psw01.xls', 'psw09.xls', 'psw14.csv'}:
            extra[name] = href
    results['sources'].update(dict(cf.ThreadPoolExecutor(max_workers=4).map(fetch, extra.items())))

def contract(sym):
    t = yf.Ticker(sym)
    info = t.info
    answer = {'identity': {k: info.get(k) for k in ['symbol', 'shortName', 'expireDate', 'regularMarketPrice', 'regularMarketTime']}, 'windows': {}}
    for interval, period in [('1m', '7d'), ('1d', '1mo')]:
        frame = t.history(period=period, interval=interval, auto_adjust=False)
        frame.to_csv(out/(sym+'_'+interval+'.csv'))
        if frame.empty:
            answer[interval] = 'MISSING'
            continue
        if interval == '1m':
            w = frame.tz_convert('America/New_York').between_time('14:28', '14:30')
            for date, g in w.groupby(w.index.date):
                v = int(g.Volume.sum())
                answer['windows'][str(date)] = {'bars': g.index.strftime('%H:%M').tolist(), 'volume': v, 'typical_vwap': float((((g.High+g.Low+g.Close)/3)*g.Volume).sum()/v) if v else None, 'close_vwap': float((g.Close*g.Volume).sum()/v) if v else None}
        else:
            answer['daily'] = frame.tail(6).reset_index().to_dict('records')
    return sym, answer

for sym in ['HOX26.NYM', 'CLX26.NYM', 'HOZ26.NYM', 'CLZ26.NYM', 'BZZ26.NYM', 'BZG27.NYM']:
    try:
        k, v = contract(sym)
        results['contracts'][k] = v
    except Exception as e:
        results['contracts'][sym] = {'error': type(e).__name__}
(out/'sources.json').write_text(json.dumps(results, indent=2, default=str))
print(json.dumps({'sources': results['sources'], 'windows': {s: v.get('windows', {}) for s, v in results['contracts'].items()}}, indent=2))
