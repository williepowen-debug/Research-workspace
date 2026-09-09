#!/usr/bin/env python3
"""Fetch dated FX/oil observations and compare structural watch levels.

Crossings are observations, not mechanism grades or position instructions.
Previous-close fallbacks are historical and never evaluated as current quotes.
"""
import csv
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

# Current structural references: THESIS.md KEY THRESHOLDS. Strict comparators
# and descriptive 5% proximity window retained; no trading/causal inference.
THRESHOLDS = [
    ('USDJPY=X', 'above', 160.0, 'watch', 'Intervention-risk watch; check speed and official evidence.'),
    ('USDJPY=X', 'below', 155.0, 'watch', 'Yen-strength watch; mechanism unconfirmed.'),
    ('USDJPY=X', 'below', 147.0, 'watch', 'Forced-unwind investigation level; check funding, positioning and transmission.'),
    ('USDJPY=X', 'below', 145.0, 'watch', 'Historical insurer-exposure watch zone; named exposures and sales require evidence.'),
    ('USDJPY=X', 'below', 135.0, 'watch', 'Historical deeper insurer-exposure watch zone; named exposures and sales require evidence.'),
]
CONTEXT_TICKERS = ['FXY', 'EURJPY=X', 'GBPJPY=X', 'AUDJPY=X', 'BZ=F']
JGB_DELEGATED = [
    ('JGB 10Y', '10Y', 2.40, 'Stress crossover'),
    ('JGB 30Y', '30Y', 4.00, 'Conditional demand-floor test; auction and institution evidence required'),
    ('JGB 40Y', '40Y', 4.00, 'Long-end context; no mechanism grade from level alone'),
]
JGB_TSV = Path(__file__).resolve().parents[1]/'workbook/JGB_YIELDS.tsv'
WARN_PCT = 0.05


def _last_jgb_row():
    try:
        with JGB_TSV.open(encoding='utf-8') as fh:
            return list(csv.DictReader(fh, delimiter='\t'))[-1]
    except (OSError, IndexError, csv.Error):
        return None


def positive(value):
    return isinstance(value, (float, int)) and not isinstance(value, bool) and math.isfinite(value) and value > 0


def quote_from_info(info, retrieved_at):
    field = 'regularMarketPrice' if positive(info.get('regularMarketPrice')) else 'previousClose'
    price = info.get(field)
    if not positive(price):
        return {'price': None, 'error': 'No valid regularMarketPrice or previousClose', 'retrieved_at': retrieved_at.isoformat()}
    # regularMarketTime does NOT date previousClose. No fabricated fallback date.
    asof = None
    if field == 'regularMarketPrice' and positive(info.get('regularMarketTime')):
        try:
            asof = datetime.fromtimestamp(info['regularMarketTime'], timezone.utc)
        except (ValueError, OverflowError, OSError):
            pass
    if asof and asof > retrieved_at:
        return {'price': None, 'error': 'Provider quote timestamp is in the future', 'retrieved_at': retrieved_at.isoformat()}
    prev = info.get('previousClose') or info.get('regularMarketPreviousClose')
    return {'price': price, 'field': field, 'as_of': asof.isoformat() if asof else None,
            'retrieved_at': retrieved_at.isoformat(),
            'eligible': field == 'regularMarketPrice' and asof is not None,
            'chg': (price/prev-1)*100 if field == 'regularMarketPrice' and positive(prev) else None}


def get_prices(symbols):
    import yfinance as yf
    tickers = yf.Tickers(' '.join(symbols))
    prices = {}
    for sym in symbols:
        try:
            info = tickers.tickers[sym].info
            prices[sym] = quote_from_info(info, datetime.now(timezone.utc))
        except Exception as exc:
            prices[sym] = {'price': None, 'error': str(exc), 'retrieved_at': datetime.now(timezone.utc).isoformat()}
    return prices


def check_thresholds(prices):
    results, warnings = [], {}
    for ticker, direction, level, classification, label in THRESHOLDS:
        quote = prices.get(ticker, {})
        if not quote.get('eligible') or not positive(quote.get('price')):
            continue
        price = quote['price']
        distance = (price-level)/level*100
        crossed = price > level if direction == 'above' else price < level
        near = price > level*(1-WARN_PCT) if direction == 'above' else price < level*(1+WARN_PCT)
        row = dict(ticker=ticker, level=level, label=label, **{'class': classification},
                   status='BREACHED' if crossed else 'WARNING', price=price, dist=distance, direction=direction)
        if crossed:
            results.append(row)
        elif near:
            key = ticker, direction
            if key not in warnings or abs(distance) < abs(warnings[key]['dist']):
                warnings[key] = row
    return results + list(warnings.values())


def main():
    print('SAM watch-level observations — run started '+datetime.now(timezone.utc).isoformat())
    symbols = sorted({t[0] for t in THRESHOLDS} | set(CONTEXT_TICKERS))
    try:
        prices = get_prices(symbols)
    except Exception as exc:
        print(f'ERROR: price fetch failed for {", ".join(symbols)}: {exc}')
        return 1
    incomplete = []
    print('\nQUOTES: vendor field and observation clock; session freshness not certified')
    for sym in symbols:
        quote = prices.get(sym, {})
        if not positive(quote.get('price')):
            incomplete.append(sym)
            print(f'UNAVAILABLE {sym}: {quote.get("error", "No result returned")}')
            continue
        kind = 'HISTORICAL previous close' if quote['field'] == 'previousClose' else 'vendor regular-market observation'
        print(f'{sym}: {quote["price"]:.2f} | {kind} | field={quote["field"]} | as_of={quote["as_of"] or "UNKNOWN"} | retrieved_at={quote["retrieved_at"]}')
        if not quote['eligible']:
            incomplete.append(sym)
            print(f'  NOT EVALUATED {sym}: historical fallback or unknown quote age')
    print('BZ=F is a continuous context quote; automated oil thresholds suspended pending a contract/roll specification.')
    print('\nWatch levels crossed / near (5% descriptive proximity):')
    alerts = check_thresholds(prices)
    for alert in alerts:
        print(f'{alert["status"]}: {alert["ticker"]} {alert["price"]:.2f} vs {alert["direction"]} {alert["level"]:.2f}: {alert["label"]}')
    eligible = sorted({t[0] for t in THRESHOLDS if prices.get(t[0], {}).get('eligible')})
    if not alerts:
        print('No crossed/near levels among evaluated symbols: '+(', '.join(eligible) or 'NONE'))
    print('Crossings refer to the displayed vendor observation clocks; no mechanism or trade grade.')
    row = _last_jgb_row()
    print('\nJGBs NOT EVALUATED HERE: jgb_yields.py owns the comparison.')
    print('Stored echo as_of='+ (row.get('Date', 'UNKNOWN') if row else 'UNKNOWN'))
    for name, column, level, note in JGB_DELEGATED:
        print(f'  {name}: {row.get(column, "UNKNOWN") if row else "UNKNOWN"} vs {level:.2f}% — {note}')
    if incomplete:
        print('ERROR: incomplete quote coverage: '+', '.join(incomplete))
    return int(bool(incomplete))


if __name__ == '__main__':
    sys.exit(main())
