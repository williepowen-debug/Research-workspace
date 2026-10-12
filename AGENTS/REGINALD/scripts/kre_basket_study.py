#!/usr/bin/env python3
"""One dated KRE basket study. No orders, intraday quotes or scheduled monitor."""
import argparse
import csv
import datetime as dt
import hashlib
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd
import yfinance as yf

yf.config.debug.hide_exceptions = False

ET = ZoneInfo('America/New_York')
BENCHMARKS = ['KRE', 'KBE', 'SPY', 'IWM', 'XLF', 'QQQ', 'TLT', '^TNX']


def now():
    return dt.datetime.now(ET).isoformat()


def fetch(symbol, start, end):
    requested = now()
    last_error = None
    for attempt in range(2):
        try:
            ticker = yf.Ticker(symbol)
            frame = ticker.history(start=start, end=end, auto_adjust=False,
                                   actions=True, timeout=20)
            if frame.empty:
                raise ValueError('Empty price history')
            metadata = ticker.history_metadata
            if metadata.get('currency') != 'USD':
                raise ValueError(f"Unexpected currency {metadata.get('currency')}")
            expected = 'INDEX' if symbol == '^TNX' else 'ETF' if symbol in BENCHMARKS else 'EQUITY'
            if metadata.get('instrumentType') != expected:
                raise ValueError(f"Unexpected instrument type {metadata.get('instrumentType')}")
            frame = frame.reset_index()
            frame['date'] = frame['Date'].dt.strftime('%Y-%m-%d')
            frame['symbol'] = symbol
            cols = ['symbol', 'date', 'Open', 'High', 'Low', 'Close', 'Adj Close',
                    'Volume', 'Dividends', 'Stock Splits']
            for column in cols:
                if column not in frame:
                    frame[column] = 0 if column in ['Dividends', 'Stock Splits'] else None
            frame = frame[cols]
            receipt = {'symbol': symbol, 'requested_at_et': requested,
                       'completed_at_et': now(), 'attempt': attempt + 1,
                       'rows': len(frame), 'first_date': frame['date'].iloc[0],
                       'last_date': frame['date'].iloc[-1],
                       'source': f'https://finance.yahoo.com/quote/{symbol}/history/',
                       'identity': {k: metadata.get(k) for k in
                                    ['symbol', 'longName', 'shortName', 'currency',
                                     'instrumentType', 'exchangeName', 'exchangeTimezoneName']}}
            return frame, receipt
        except Exception as exc:
            last_error = str(exc)
    return None, {'symbol': symbol, 'requested_at_et': requested,
                  'completed_at_et': now(), 'error': last_error, 'rows': 0}


def pct(first, last):
    return 100 * (last / first - 1)


def metrics(frame, symbol, weight, name, dates):
    frame = frame.sort_values('date').set_index('date')
    row = {'symbol': symbol, 'name': name, 'oct9_weight_pct': weight,
           'last_available_date': frame.index[-1], 'daily_bars': len(frame)}
    for label, (first, last) in dates.items():
        valid = first in frame.index and last in frame.index
        row[f'{label}_covered'] = valid
        if valid:
            row[f'{label}_price_pct'] = pct(frame.loc[first, 'Close'], frame.loc[last, 'Close'])
            row[f'{label}_adjusted_return_pct'] = pct(frame.loc[first, 'Adj Close'], frame.loc[last, 'Adj Close'])
            row[f'{label}_current_weight_scenario_pp'] = weight * row[f'{label}_adjusted_return_pct'] / 100 if weight is not None else None
        else:
            for suffix in ['price_pct', 'adjusted_return_pct', 'current_weight_scenario_pp']:
                row[f'{label}_{suffix}'] = None
    last = dates['three_month'][1]
    settled = frame.loc[frame.index <= last].copy()
    row['settled_close'] = float(settled['Close'].iloc[-1])
    for n in [20, 50]:
        value = float(settled['Close'].tail(n).mean()) if len(settled) >= n else None
        row[f'sma{n}_close'] = value
        row[f'below_sma{n}'] = row['settled_close'] < value if value is not None else None
    row['latest_volume'] = float(settled['Volume'].iloc[-1])
    prior20 = settled['Volume'].iloc[-21:-1]
    row['latest_volume_vs_prior20'] = row['latest_volume'] / float(prior20.mean()) if len(prior20) == 20 and prior20.mean() > 0 else None
    returns = settled['Adj Close'].pct_change()
    last20 = settled.tail(20)
    up = last20.loc[returns.reindex(last20.index) > 0, 'Volume']
    down = last20.loc[returns.reindex(last20.index) < 0, 'Volume']
    row['last20_up_sessions'] = len(up)
    row['last20_down_sessions'] = len(down)
    row['last20_mean_down_vs_up_volume'] = float(down.mean() / up.mean()) if len(up) and len(down) and up.mean() > 0 else None
    row['last20_total_down_vs_up_volume'] = float(down.sum() / up.sum()) if len(up) and up.sum() > 0 else None
    row['reported_split_events'] = int((settled['Stock Splits'] != 0).sum())
    row['zero_volume_sessions_last20'] = int((last20['Volume'] == 0).sum())
    return row


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--holdings', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise SystemExit('Output already exists; use a new dated run to preserve evidence.')
    args.output.mkdir(parents=True)
    holdings = list(csv.DictReader(args.holdings.open()))
    banks = [r for r in holdings if r['ticker'] != '-']
    assert len(banks) == len({r['ticker'] for r in banks}) == 167
    symbols = [r['ticker'] for r in banks] + BENCHMARKS
    frames, receipts = {}, []
    began = now()
    with ThreadPoolExecutor(max_workers=6) as pool:
        futures = {pool.submit(fetch, s, '2025-10-01', '2026-10-10'): s for s in symbols}
        for count, future in enumerate(as_completed(futures), 1):
            frame, receipt = future.result()
            receipts.append(receipt)
            if frame is not None:
                frames[receipt['symbol']] = frame
            if count % 25 == 0 or count == len(symbols):
                print(f'Fetched {count}/{len(symbols)} histories; failures {count-len(frames)}', flush=True)
    if 'KRE' not in frames:
        (args.output / 'fetch-receipt.json').write_text(json.dumps(receipts, indent=2) + '\n')
        raise SystemExit('KRE benchmark unavailable; sources saved, analysis withheld.')
    all_bars = pd.concat(frames.values(), ignore_index=True).sort_values(['symbol', 'date'])
    assert not all_bars.duplicated(['symbol', 'date']).any()
    assert all(all_bars['date'] <= '2026-10-09')
    all_bars.to_csv(args.output / 'daily-history.csv.gz', index=False,
                    compression={'method': 'gzip', 'mtime': 0})
    dates = {'three_month': ('2026-07-10', '2026-10-09'),
             'four_week': ('2026-09-11', '2026-10-09')}
    rows = []
    for r in banks:
        if r['ticker'] in frames:
            rows.append(metrics(frames[r['ticker']], r['ticker'], float(r['weight_pct']), r['name'], dates))
        else:
            rows.append({'symbol': r['ticker'], 'name': r['name'],
                         'oct9_weight_pct': float(r['weight_pct']), 'three_month_covered': False,
                         'four_week_covered': False, 'fetch_failed': True})
    table = pd.DataFrame(rows)
    table.to_csv(args.output / 'basket-metrics.csv', index=False)
    bench = pd.DataFrame([metrics(frames[s], s, None, s, dates) for s in BENCHMARKS if s in frames])
    bench.to_csv(args.output / 'benchmark-metrics.csv', index=False)
    summaries = {}
    for label in dates:
        covered = table[table[f'{label}_covered'] == True]
        negative = covered[covered[f'{label}_price_pct'] < 0]
        weight = float(covered['oct9_weight_pct'].sum())
        summaries[label] = {'covered_banks': len(covered), 'covered_oct9_weight_pct': weight,
                            'declining_banks': len(negative), 'declining_oct9_weight_pct': float(negative['oct9_weight_pct'].sum()),
                            'declining_count_share_pct': 100 * len(negative) / len(covered),
                            'median_price_pct': float(covered[f'{label}_price_pct'].median()),
                            'median_adjusted_return_pct': float(covered[f'{label}_adjusted_return_pct'].median()),
                            'price_p10_pct': float(covered[f'{label}_price_pct'].quantile(.1)),
                            'price_p90_pct': float(covered[f'{label}_price_pct'].quantile(.9)),
                            'oct9_weight_adjusted_scenario_pp': float(covered[f'{label}_current_weight_scenario_pp'].sum()),
                            'scenario_label': 'October9 end-weight fixed-basket diagnostic; NOT actual historical fund contributions'}
    for n in [20, 50]:
        valid = table[table[f'below_sma{n}'].notna()]
        below = valid[valid[f'below_sma{n}'] == True]
        summaries[f'sma{n}'] = {'covered_banks': len(valid), 'below_banks': len(below),
                                 'below_oct9_weight_pct': float(below['oct9_weight_pct'].sum())}
    receipt = {'started_at_et': began, 'finished_at_et': now(), 'yfinance_version': yf.__version__,
               'authority': 'Will direct: Okay approved. Go ahead. Approved next-research proposal 6c917f2a8.',
               'holdings_source': str(args.holdings), 'holdings_as_of': '2026-10-09',
               'holdings_sha256': hashlib.sha256(args.holdings.read_bytes()).hexdigest(),
               'requested_symbols': len(symbols), 'returned_symbols': len(frames),
               'history_start': '2025-10-01', 'history_end_exclusive': '2026-10-10',
               'quote_refresh': False, 'source': 'Yahoo chart history via yfinance; no independent-vendor verification',
               'price_basis': 'Vendor closing prices, historical split handling; cash dividends excluded',
               'adjusted_basis': 'Vendor adjusted close ratios, dividend-adjusted total-return proxy',
               'moving_average_basis': '20/50 settled daily Close bars through October9',
               'volume_basis': 'Complete daily sessions; latest volume divided by prior20 session mean; up/down classified by adjusted close return',
               'historical_membership_warning': 'October9 basket selected at window end; membership and rebalance changes not reconstructed',
               'daily_history_sha256': hashlib.sha256((args.output / 'daily-history.csv.gz').read_bytes()).hexdigest(),
               'requests': sorted(receipts, key=lambda r: r['symbol'])}
    (args.output / 'fetch-receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    (args.output / 'breadth-summary.json').write_text(json.dumps(summaries, indent=2) + '\n')
    print(json.dumps(summaries, indent=2), flush=True)
    print('Worst three-month price returns:', table.nsmallest(12, 'three_month_price_pct')[['symbol', 'oct9_weight_pct', 'three_month_price_pct', 'four_week_price_pct']].to_string(index=False), flush=True)
    print('Worst current-weight scenario drag:', table.nsmallest(12, 'three_month_current_weight_scenario_pp')[['symbol', 'oct9_weight_pct', 'three_month_price_pct', 'three_month_current_weight_scenario_pp']].to_string(index=False), flush=True)


if __name__ == '__main__':
    main()
