#!/usr/bin/env python3
"""
REGINALD Dark Pool Monitor
Pulls off-exchange % (chartexchange) and short volume (FINRA RegSHO) for thesis tickers.
Appends to workbook TSVs and prints a summary table.

Usage:
  .venv/bin/python3 AGENTS/REGINALD/scripts/darkpool.py          # full run (fetch + append + print)
  .venv/bin/python3 AGENTS/REGINALD/scripts/darkpool.py --print   # print latest from TSVs only
"""

import urllib.request
import json
import re
import sys
import os
from datetime import datetime, timedelta
from pathlib import Path

TICKERS = ['WAL', 'OZK', 'KRE', 'EGBN', 'ZION', 'CFG']

# Chartexchange exchange codes
CE_EXCHANGES = {
    'WAL': 'nyse', 'OZK': 'nasdaq', 'KRE': 'nyse',
    'EGBN': 'nasdaq', 'ZION': 'nasdaq', 'CFG': 'nyse',
}

REGINALD_DIR = Path(__file__).resolve().parent.parent
WORKBOOK = REGINALD_DIR / 'workbook'
DARKPOOL_TSV = WORKBOOK / 'DARKPOOL.tsv'
SHORT_VOL_TSV = WORKBOOK / 'SHORT_VOL.tsv'


def fetch_url(url, timeout=15):
    """Fetch URL with user-agent, return text or None."""
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req, timeout=timeout)
        return resp.read().decode('utf-8')
    except Exception:
        return None


def fetch_darkpool(ticker):
    """Scrape chartexchange for off-exchange stats. Returns dict or None."""
    exchange = CE_EXCHANGES.get(ticker, 'nyse')
    url = f'https://chartexchange.com/symbol/{exchange}-{ticker.lower()}/stats/'
    html = fetch_url(url)
    if not html:
        return None

    result = {}
    # Extract off-exchange % and 30d avg from page text
    m = re.search(r'is\s+([\d,]+),?\s+which\s+is\s+([\d.]+)%\s+of\s+today', html)
    if m:
        result['off_ex_vol'] = int(m.group(1).replace(',', ''))
        result['off_ex_pct'] = float(m.group(2))

    # Look for 30-day average — chartexchange format:
    # "Over the past 30 days, the average Off Exchange & Dark Pool volume has been XX.XX%"
    m2 = re.search(r'past\s+30\s+days.*?average\s+Off\s+Exchange.*?been\s+([\d.]+)%', html, re.IGNORECASE | re.DOTALL)
    if m2:
        result['avg_30d'] = float(m2.group(1))
    else:
        result['avg_30d'] = None

    # Extract total volume
    m3 = re.search(r'Total\s+Daily\s+Volume[:\s]+([\d,]+)', html, re.IGNORECASE)
    if m3:
        result['total_vol'] = int(m3.group(1).replace(',', ''))
    elif 'off_ex_vol' in result and 'off_ex_pct' in result and result['off_ex_pct'] > 0:
        result['total_vol'] = int(result['off_ex_vol'] / (result['off_ex_pct'] / 100))
    else:
        result['total_vol'] = 0

    return result if 'off_ex_pct' in result else None


def fetch_short_volume(date_str=None):
    """Fetch FINRA RegSHO CNMS file for a date. Returns dict of ticker -> {short, total, pct}."""
    if date_str is None:
        # Try today, then yesterday, then day before
        for offset in range(0, 4):
            d = datetime.now() - timedelta(days=offset)
            if d.weekday() >= 5:
                continue
            ds = d.strftime('%Y%m%d')
            data = fetch_url(f'https://cdn.finra.org/equity/regsho/daily/CNMSshvol{ds}.txt')
            if data and len(data) > 100:
                date_str = d.strftime('%Y-%m-%d')
                break
        else:
            return None, None
    else:
        ds = date_str.replace('-', '')
        data = fetch_url(f'https://cdn.finra.org/equity/regsho/daily/CNMSshvol{ds}.txt')

    if not data:
        return None, date_str

    results = {}
    for line in data.strip().split('\n'):
        parts = line.strip().split('|')
        if len(parts) >= 5 and parts[1] in TICKERS:
            ticker = parts[1]
            short_v = int(float(parts[2]))
            total_v = int(float(parts[4]))
            pct = (short_v / total_v * 100) if total_v > 0 else 0
            results[ticker] = {'short': short_v, 'total': total_v, 'pct': round(pct, 1)}

    return results, date_str


def append_darkpool_tsv(date_str, data):
    """Append today's darkpool readings to DARKPOOL.tsv if not already present."""
    existing = set()
    if DARKPOOL_TSV.exists():
        with open(DARKPOOL_TSV) as f:
            for line in f:
                parts = line.strip().split('\t')
                if len(parts) >= 2:
                    existing.add((parts[0], parts[1]))

    with open(DARKPOOL_TSV, 'a') as f:
        for ticker, d in data.items():
            if (date_str, ticker) not in existing:
                delta = round(d['off_ex_pct'] - d['avg_30d'], 1) if d['avg_30d'] else ''
                f.write(f"{date_str}\t{ticker}\t{d['off_ex_vol']}\t{d['total_vol']}\t{d['off_ex_pct']}\t{d.get('avg_30d', '')}\t{delta}\n")


def append_short_vol_tsv(date_str, data):
    """Append today's short volume to SHORT_VOL.tsv if not already present."""
    existing = set()
    if SHORT_VOL_TSV.exists():
        with open(SHORT_VOL_TSV) as f:
            for line in f:
                parts = line.strip().split('\t')
                if len(parts) >= 2:
                    existing.add((parts[0], parts[1]))

    with open(SHORT_VOL_TSV, 'a') as f:
        for ticker, d in data.items():
            if (date_str, ticker) not in existing:
                f.write(f"{date_str}\t{ticker}\t{d['short']}\t{d['total']}\t{d['pct']}\n")


def print_summary(dp_data, sv_data, sv_date):
    """Print formatted summary table."""
    today = datetime.now().strftime('%Y-%m-%d')
    print(f"\n{'='*70}")
    print(f"  REGINALD Dark Pool Monitor — {today}")
    print(f"{'='*70}")

    print(f"\n  {'Ticker':<8} {'Off-Ex%':>8} {'30d Avg':>8} {'Delta':>8} {'Signal':<16} {'Short%':>8}")
    print(f"  {'-'*60}")

    for ticker in TICKERS:
        # Dark pool data
        dp = dp_data.get(ticker, {})
        off_ex = f"{dp.get('off_ex_pct', 0):.1f}%" if dp else '—'
        avg = f"{dp.get('avg_30d', 0):.1f}%" if dp and dp.get('avg_30d') else '—'
        delta = dp.get('off_ex_pct', 0) - dp.get('avg_30d', 0) if dp and dp.get('avg_30d') else 0

        if delta > 10:
            signal = 'VERY ELEVATED'
            flag = ' ***'
        elif delta > 5:
            signal = 'ELEVATED'
            flag = ' **'
        elif delta > 2:
            signal = 'Above avg'
            flag = ' *'
        else:
            signal = 'Normal'
            flag = ''

        delta_str = f"{delta:+.1f}pp" if dp and dp.get('avg_30d') else '—'

        # Short volume
        sv = sv_data.get(ticker, {}) if sv_data else {}
        short_pct = f"{sv.get('pct', 0):.1f}%" if sv else '—'

        print(f"  {ticker:<8} {off_ex:>8} {avg:>8} {delta_str:>8} {signal:<16} {short_pct:>8}{flag}")

    if sv_date:
        print(f"\n  Short volume date: {sv_date}")
    print()


def main():
    print_only = '--print' in sys.argv

    if print_only:
        # Just read latest from TSVs and display
        print("  [print-only mode — reading from TSVs]")
        # TODO: implement TSV reading
        return

    # Fetch dark pool data from chartexchange
    print("  Fetching dark pool data from chartexchange...", flush=True)
    dp_data = {}
    for ticker in TICKERS:
        result = fetch_darkpool(ticker)
        if result:
            dp_data[ticker] = result
        import time
        time.sleep(1.5)  # rate limit

    # Fetch short volume from FINRA
    print("  Fetching short volume from FINRA...", flush=True)
    sv_data, sv_date = fetch_short_volume()

    # Print summary
    print_summary(dp_data, sv_data, sv_date)

    # Append to TSVs
    today = datetime.now().strftime('%Y-%m-%d')
    if dp_data:
        append_darkpool_tsv(today, dp_data)
        print(f"  Updated DARKPOOL.tsv ({len(dp_data)} tickers)")

    if sv_data and sv_date:
        append_short_vol_tsv(sv_date, sv_data)
        print(f"  Updated SHORT_VOL.tsv ({len(sv_data)} tickers, date: {sv_date})")

    print()


if __name__ == '__main__':
    main()
