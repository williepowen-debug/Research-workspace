"""10/10 BRENT: Friday 10/9 diesel tape on its basis. Single vendor (yfinance). Not settles."""
import json, os
from datetime import datetime, timezone, date
import yfinance as yf
os.chdir(os.path.dirname(os.path.abspath(__file__)) or ".")
D = date(2026, 10, 9)
res = {'retrieved_utc': datetime.now(timezone.utc).isoformat(), 'vendor': 'yfinance', 'note': 'single vendor; 1m bars; not CME/ICE settlements'}
for sym in ['HOX26.NYM', 'CLX26.NYM', 'HOZ26.NYM', 'CLZ26.NYM', 'BZZ26.NYM']:
    try:
        t = yf.Ticker(sym)
        fr = t.history(period='5d', interval='1m', auto_adjust=False).tz_convert('America/New_York')
        d = fr[fr.index.date == D]
        def win(a, b):
            w = d.between_time(a, b); v = w.Volume.sum()
            return {'n': len(w), 'vol': int(v),
                    'typ_vwap': float((((w.High + w.Low + w.Close) / 3) * w.Volume).sum() / v) if v else None,
                    'first': str(w.index[0]) if len(w) else None, 'last': str(w.index[-1]) if len(w) else None}
        r = {'n_day_bars': len(d), 'first_bar': str(d.index[0]) if len(d) else None, 'last_bar': str(d.index[-1]) if len(d) else None,
             'last_close': float(d.Close.iloc[-1]) if len(d) else None,
             'win_1428_1430': win('14:28', '14:30'),
             'win_1430_1500': win('14:31', '15:00'),
             'win_1500_1700': win('15:00', '17:00')}
        # minute path 14:00-17:00 at 5-minute sampling (close)
        p = d.between_time('14:00', '17:00')
        r['path_5m'] = [(i.strftime('%H:%M'), round(float(x.Close), 5), int(x.Volume)) for i, x in p.iterrows() if i.minute % 5 == 0]
        dd = t.history(period='10d', interval='1d', auto_adjust=False)
        r['daily_tail'] = [(str(i.date()), float(x.Open), float(x.High), float(x.Low), float(x.Close), int(x.Volume)) for i, x in dd.tail(4).iterrows()]
        try:
            fi = t.fast_info; r['fast_info_prev_close'] = float(fi['previousClose']); r['fast_info_last'] = float(fi['lastPrice'])
        except Exception as e:
            r['fast_info_err'] = repr(e)
        try:
            inf = t.info
            r['info'] = {k: inf.get(k) for k in ('regularMarketPreviousClose', 'regularMarketPrice', 'regularMarketChangePercent', 'previousClose', 'regularMarketTime', 'shortName', 'expireDate')}
        except Exception as e:
            r['info_err'] = repr(e)
        fr.to_csv(f'{sym}_1m.csv')
        res[sym] = r
    except Exception as e:
        res[sym] = {'error': repr(e)}
json.dump(res, open('tape_evidence.json', 'w'), indent=1, default=str)
for m in ('X26', 'Z26'):
    h, c = res.get(f'HO{m}.NYM', {}), res.get(f'CL{m}.NYM', {})
    for k in ('win_1428_1430', 'win_1430_1500', 'win_1500_1700'):
        if h.get(k, {}).get('typ_vwap') and c.get(k, {}).get('typ_vwap'):
            print(m, k, 'crack typ_vwap', round(h[k]['typ_vwap'] * 42 - c[k]['typ_vwap'], 5), 'bars HO/CL', h[k]['n'], c[k]['n'])
        else:
            print(m, k, 'NOT MEASURABLE')
    if h.get('last_close') and c.get('last_close'):
        print(m, 'last-trade crack', round(h['last_close'] * 42 - c['last_close'], 5), h['last_bar'], c['last_bar'])
