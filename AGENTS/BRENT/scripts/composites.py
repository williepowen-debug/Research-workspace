#!/usr/bin/env python3
"""Complete vendor-quote diagnostics; never persist a gate or prediction grade.

Extends existing instrument_check; supersedes its STNG-only tanker probe.
Matched futures mode extends the one-off research retrieval, with explicit
contract identity. It does not replace the original missing DIESEL-CRACK/BRT-12
construction. Same maturity and USD/bbl conversion are mandatory.
"""
import argparse
import json
import re
import sys
from datetime import datetime, time, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parent))
from thresholds import get_prices, finite_number

TANKERS = ('STNG', 'FRO', 'DHT')
MAX_LEG_SKEW_SECONDS = 300  # quote synchronization tolerance, not a trading level
ET = ZoneInfo('America/New_York')


def checked_legs(prices, symbols):
    problems, stamps = [], []
    for symbol in symbols:
        q = prices.get(symbol, {})
        if q.get('state') != 'RECENT_QUOTE':
            problems.append(f"{symbol}: {q.get('reason') or 'quote absent/unverified'}")
            continue
        if q.get('symbol') != symbol or q.get('currency') != 'USD':
            problems.append(f'{symbol}: returned symbol/currency not verified as requested USD instrument')
        if finite_number(q.get('price')) is None:
            problems.append(f'{symbol}: price is not finite')
        try:
            stamp = datetime.fromisoformat(q['date'])
            if stamp.tzinfo is None:
                raise ValueError('naive quote timestamp')
            stamps.append(stamp)
        except (KeyError, TypeError, ValueError):
            problems.append(f'{symbol}: invalid timestamp')
    if len(stamps) == len(symbols):
        if (max(stamps) - min(stamps)).total_seconds() > MAX_LEG_SKEW_SECONDS:
            problems.append('quote legs differ by more than five minutes')
        if len({stamp.astimezone(ET).date() for stamp in stamps}) != 1:
            problems.append('quote legs have different ET observation dates')
    return problems, stamps


def tanker_snapshot(prices, now=None):
    now = now or datetime.now(timezone.utc)
    problems, stamps = checked_legs(prices, TANKERS)
    moves = {}
    for symbol in TANKERS:
        q = prices.get(symbol, {})
        if q.get('chg') is None or not q.get('prev'):
            problems.append(f'{symbol}: vendor previous regular close missing')
        else:
            moves[symbol] = q['chg']
    window = (not problems and now.astimezone(ET).weekday() < 5 and
              time(14) <= now.astimezone(ET).time() < time(16) and
              len(stamps) == len(TANKERS) and
              all(stamp.astimezone(ET).date() == now.astimezone(ET).date() and
                  time(14) <= stamp.astimezone(ET).time() < time(16) for stamp in stamps))
    return dict(state='UNGRADED' if problems else 'DIAGNOSTIC', problems=problems,
                window_open=window, quotes={s: prices.get(s) for s in TANKERS},
                max_absolute_percent=max(map(abs, moves.values())) if not problems else None,
                reading='vendor previous regular close to timestamped quote; sign discarded',
                limit='No gate grade, day-0 inference or repeat-grade authorization. Owner reads complete BE-04 through BE-12, including C and close veto; grade once at/after 14:00 ET.')


def futures_snapshot(prices, wti, brent, product):
    symbols = (wti, brent, product)
    parsed = [re.fullmatch(r'(CL|BZ|HO)([FGHJKMNQUVXZ])(\d{2})\.NYM', symbol) for symbol in symbols]
    problems = []
    if (not all(parsed) or [m.group(1) for m in parsed if m] != ['CL', 'BZ', 'HO'] or
            len({m.group(2, 3) for m in parsed if m}) != 1):
        problems.append('require explicit CL/BZ/HO contracts with identical delivery month/year; continuous tickers rejected')
    quality, stamps = checked_legs(prices, symbols)
    problems.extend(quality)
    values = None
    if not problems:
        cl, bz, ho = [prices[s]['price'] for s in symbols]
        values = {'WTI_minus_Brent': cl - bz, 'ULSD_minus_Brent': ho * 42 - bz,
                  'ULSD_minus_WTI': ho * 42 - cl}
    return dict(state='UNGRADED' if problems else 'DIAGNOSTIC', problems=problems,
                quotes={s: prices.get(s) for s in symbols}, spreads_usd_per_bbl=values,
                basis='Explicit matched delivery month; ULSD USD/gallon ×42; timestamped vendor quotes, not settlements.',
                limit='No automatic roll, t-4 comparison, historical BRT-12 reconstruction or original DIESEL-CRACK grade.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tanker', action='store_true')
    parser.add_argument('--wti')
    parser.add_argument('--brent')
    parser.add_argument('--product')
    args = parser.parse_args()
    if args.tanker:
        if args.wti or args.brent or args.product:
            parser.error('choose tanker or named-contract futures mode')
        result = tanker_snapshot(get_prices(TANKERS))
    elif all((args.wti, args.brent, args.product)):
        result = futures_snapshot(get_prices([args.wti, args.brent, args.product]),
                                  args.wti, args.brent, args.product)
    else:
        parser.error('provide --tanker or all of --wti --brent --product')
    print(json.dumps(result, indent=2))
    return 2 if result['problems'] else 0


if __name__ == '__main__':
    sys.exit(main())
