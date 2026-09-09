"""Read-only public data capture for the XLE decision; writes only beside this file.

Run with repo .venv/bin/python3. No broker access or orders. Yahoo option bid/ask
timestamps are unavailable: capture time and last trade time are different fields.
Daily history ends before Sep 9, excluding today's incomplete equity session.
"""
import io
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import yfinance as yf
from curl_cffi import requests

ROOT = Path(__file__).resolve().parent
yf.set_tz_cache_location('/tmp/prome-xle-yfinance-cache')


def stamp():
    return datetime.now(timezone.utc).isoformat()


def main():
    if '--fred-only' in sys.argv:
        receipt = json.loads((ROOT / 'capture.json').read_text())
        secret = os.environ.get('FRED_API_KEY')
        if not secret:
            for line in (ROOT.parents[2] / 'FORGE/tools/market-data/.env').read_text().splitlines():
                if line.startswith('FRED_API_KEY='):
                    secret = line.split('=', 1)[1].strip().strip('\"\'')
        if not secret:
            raise SystemExit('FRED credential unavailable')
        for series in ['DCOILBRENTEU', 'DCOILWTICO', 'DGS1MO']:
            response = requests.get('https://api.stlouisfed.org/fred/series/observations',
                params={'series_id': series, 'api_key': secret, 'file_type': 'json',
                        'observation_start': '2023-01-01', 'observation_end': '2026-09-08'},
                impersonate='chrome', timeout=30)
            # Do not emit request URLs; they contain credentials.
            if response.status_code != 200:
                raise SystemExit(f'FRED {series} status {response.status_code}')
            data = response.json()
            rows = [{'date': r['date'], series: r['value']} for r in data['observations']]
            pd.DataFrame(rows).to_csv(ROOT / (series + '.csv'), index=False)
            receipt['sources'][series] = {'url': 'https://fred.stlouisfed.org/series/' + series,
                'retrieved_utc': stamp(), 'file': series + '.csv',
                'transport': 'official FRED observations API; prior CSV endpoint 404'}
            receipt['errors'].pop(series, None)
            print(series, 'OK', flush=True)
        receipt['fred_retry_finished_utc'] = stamp()
        (ROOT / 'capture.json').write_text(json.dumps(receipt, indent=2) + '\n')
        return
    receipt = {'started_utc': stamp(), 'sources': {}, 'errors': {}}
    session = requests.Session(impersonate='chrome')
    for symbol in ['XLE', 'XOM', 'CVX', 'SPY', 'USO', 'BZX26.NYM', 'BZF27.NYM']:
        try:
            ticker = yf.Ticker(symbol, session=session)
            history = ticker.history(start='2023-01-01', end='2026-09-09',
                                     auto_adjust=False, actions=True, raise_errors=True)
            if history.empty:
                raise ValueError('empty daily history')
            history.index = history.index.strftime('%Y-%m-%d')
            name = symbol.replace('.', '-') + '.csv'
            history.to_csv(ROOT / name, index_label='date')
            receipt['sources'][symbol] = {'retrieved_utc': stamp(), 'file': name,
                'first': history.index[0], 'last': history.index[-1],
                'basis': 'Yahoo Close and Adj Close retained; auto_adjust=False; actions=True'}
        except Exception as exc:
            receipt['errors'][symbol] = str(exc)
        print(symbol, 'OK' if symbol in receipt['sources'] else receipt['errors'][symbol], flush=True)
    for series in ['DCOILBRENTEU', 'DCOILWTICO', 'DGS1MO']:
        try:
            url = 'https://fred.stlouisfed.org/graph/graph.csv?id=' + series + '&cosd=2023-01-01&coed=2026-09-08'
            response = session.get(url, timeout=30)
            response.raise_for_status()
            frame = pd.read_csv(io.StringIO(response.text))
            if series not in frame:
                raise ValueError('missing requested FRED column')
            (ROOT / (series + '.csv')).write_text(response.text)
            receipt['sources'][series] = {'url': url, 'retrieved_utc': stamp(), 'file': series + '.csv'}
        except Exception as exc:
            receipt['errors'][series] = str(exc)
        print(series, 'OK' if series in receipt['sources'] else receipt['errors'][series], flush=True)
    capture = {'started_utc': stamp(), 'chains': {}, 'errors': {},
               'warning': 'Bid/ask quote timestamps unavailable. lastTradeDate is not quote time.'}
    ticker = yf.Ticker('XLE', session=session)
    try:
        capture['expiries'] = list(ticker.options)
        for expiry in ['2026-09-18', '2026-09-25', '2026-09-30', '2026-10-16']:
            if expiry not in capture['expiries']:
                capture['errors'][expiry] = 'Expiry absent from vendor list'
                continue
            chain = ticker.option_chain(expiry)
            capture['chains'][expiry] = {
                'retrieved_utc': stamp(), 'underlying': chain.underlying,
                'calls': json.loads(chain.calls.to_json(orient='records', date_format='iso')),
                'puts': json.loads(chain.puts.to_json(orient='records', date_format='iso'))}
        capture['info'] = {k: ticker.info.get(k) for k in [
            'symbol', 'regularMarketPrice', 'regularMarketTime', 'regularMarketPreviousClose',
            'bid', 'ask', 'bidSize', 'askSize', 'marketState', 'exchangeDataDelayedBy',
            'dividendRate', 'exDividendDate', 'trailingAnnualDividendRate']}
    except Exception as exc:
        capture['errors']['chain'] = str(exc)
    capture['finished_utc'] = stamp()
    (ROOT / 'options.json').write_text(json.dumps(capture, indent=2, default=str) + '\n')
    receipt['finished_utc'] = stamp()
    (ROOT / 'capture.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps({'data_errors': receipt['errors'], 'option_errors': capture['errors']}), flush=True)
    if receipt['errors'] or not capture['chains']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
