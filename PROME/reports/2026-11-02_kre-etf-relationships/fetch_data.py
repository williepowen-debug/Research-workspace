"""One-off, read-only public data collection; preserves individual vendor responses."""
from pathlib import Path
from datetime import datetime
import json
import yfinance as yf
import pandas as pd

OUT = Path(__file__).resolve().parent
TICKERS = ['KRE','KBWB','XLF','IWM','SPY','RSP','QQQ','HYG','LQD','IEF','TLT','VNQ','SHY']
meta = {'started_at': datetime.now().astimezone().isoformat(),
        'source': 'Yahoo Finance via yfinance', 'version': yf.__version__,
        'request': {'start': '2012-01-01', 'end_exclusive': '2026-11-03',
                    'interval': '1d', 'auto_adjust': False, 'actions': True},
        'completed_cutoff': '2026-10-30', 'tickers': {}}
for symbol in TICKERS:
    try:
        h = yf.Ticker(symbol).history(start='2012-01-01', end='2026-11-03',
                                      interval='1d', auto_adjust=False, actions=True)
        if h.empty or 'Adj Close' not in h:
            raise ValueError('Empty response or missing adjusted close')
        h.to_csv(OUT / f'{symbol}_daily.csv', index_label='Date')
        meta['tickers'][symbol] = {'rows': len(h), 'first': str(h.index[0]),
                                  'last': str(h.index[-1]),
                                  'retrieved_at': datetime.now().astimezone().isoformat()}
        print(symbol, meta['tickers'][symbol], flush=True)
    except Exception as exc:
        meta['tickers'][symbol] = {'error': repr(exc)}
        print(symbol, 'ERROR', repr(exc), flush=True)
meta['finished_at'] = datetime.now().astimezone().isoformat()
(OUT / 'source_manifest.json').write_text(json.dumps(meta, indent=2) + '\n')
