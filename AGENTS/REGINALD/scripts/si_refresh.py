#!/usr/bin/env python3
"""
REGINALD Short Interest Monitor
Pulls short interest data via yfinance for thesis tickers.
Appends to SHORT_INTEREST.tsv when newer data is available.

Usage:
  .venv/bin/python3 AGENTS/REGINALD/scripts/si_refresh.py
"""

import sys
from datetime import datetime
from pathlib import Path

try:
    import yfinance as yf
except ImportError:
    print("  ERROR: yfinance not installed.")
    sys.exit(1)

TICKERS = ["OZK", "WAL", "EGBN", "ZION", "CFG"]

REGINALD_DIR = Path(__file__).resolve().parent.parent
WORKBOOK = REGINALD_DIR / "workbook"
SI_TSV = WORKBOOK / "SHORT_INTEREST.tsv"


def get_short_interest():
    """Fetch short interest data for all tickers."""
    results = {}
    for ticker in TICKERS:
        try:
            t = yf.Ticker(ticker)
            info = t.info
            si = info.get("sharesShort")
            si_pct = info.get("shortPercentOfFloat")
            si_ratio = info.get("shortRatio")
            si_date = info.get("dateShortInterest")
            shares_float = info.get("floatShares")

            if si is not None and si_date is not None:
                dt = datetime.fromtimestamp(si_date)
                results[ticker] = {
                    "shares_short": si,
                    "pct_float": si_pct * 100 if si_pct else 0,
                    "short_ratio": si_ratio or 0,
                    "date": dt.strftime("%Y-%m-%d"),
                    "float_shares": shares_float or 0,
                }
        except Exception:
            pass
    return results


def get_last_tsv_entry(ticker):
    """Get the most recent TSV entry for a ticker."""
    if not SI_TSV.exists():
        return None

    last = None
    with open(SI_TSV) as f:
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) >= 3 and parts[1] == ticker:
                try:
                    pct = float(parts[4]) if len(parts) > 4 and parts[4] else 0
                except (ValueError, IndexError):
                    pct = 0
                try:
                    si = int(parts[2]) if parts[2].isdigit() else 0
                except (ValueError, IndexError):
                    si = 0
                last = {
                    "date": parts[0],
                    "shares_short": si,
                    "pct_float": pct,
                }
    return last


def append_tsv(data):
    """Append new entries to SHORT_INTEREST.tsv."""
    existing = set()
    if SI_TSV.exists():
        with open(SI_TSV) as f:
            for line in f:
                parts = line.strip().split("\t")
                if len(parts) >= 2:
                    existing.add((parts[0], parts[1]))

    appended = 0
    with open(SI_TSV, "a") as f:
        for ticker, d in data.items():
            key = (d["date"], ticker)
            if key not in existing:
                f.write(
                    f"{d['date']}\t{ticker}\t{d['shares_short']}\t"
                    f"{d['pct_float']:.2f}\t{d['short_ratio']:.2f}\t"
                    f"{d['float_shares']}\n"
                )
                appended += 1
    return appended


def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"\n{'='*70}")
    print(f"  REGINALD Short Interest Monitor — {now}")
    print(f"{'='*70}")

    data = get_short_interest()
    if not data:
        print("\n  ERROR: Could not fetch short interest data.")
        return

    print(f"\n  {'Ticker':<6} {'Shares Short':>14} {'% Float':>8} {'Days-to-Cover':>14} {'SI Date':>12} {'vs. Prior':>12}")
    print(f"  {'-'*70}")

    for ticker in TICKERS:
        d = data.get(ticker)
        if not d:
            print(f"  {ticker:<6} {'—':>14} {'—':>8} {'—':>14} {'—':>12} {'—':>12}")
            continue

        # Compare against last TSV entry
        last = get_last_tsv_entry(ticker)
        if last and last["date"] != d["date"]:
            prev_pct = last["pct_float"]
            delta = d["pct_float"] - prev_pct
            vs_prior = f"{delta:+.2f}pp"
        elif last and last["date"] == d["date"]:
            vs_prior = "unchanged"
        else:
            vs_prior = "NEW"

        si_str = f"{d['shares_short']:>14,}"
        pct_str = f"{d['pct_float']:>7.2f}%"
        ratio_str = f"{d['short_ratio']:>13.1f}d"

        # Flag significance
        flag = ""
        if d["pct_float"] > 10:
            flag = " 🔴 HIGH"
        elif d["pct_float"] > 5:
            flag = " 🟠"

        print(f"  {ticker:<6} {si_str} {pct_str} {ratio_str} {d['date']:>12} {vs_prior:>12}{flag}")

    # Append to TSV
    appended = append_tsv(data)
    if appended > 0:
        print(f"\n  Appended {appended} new entries to SHORT_INTEREST.tsv")
    else:
        print(f"\n  No new data to append (same reporting date)")

    # Data quality warnings
    print(f"\n  ⚠️  Note: yfinance SI data may lag 2-4 weeks. Cross-check against Fintel for latest bi-monthly report.")
    print(f"  ⚠️  KRE (ETF) excluded — yfinance does not provide SI for ETFs. Track via KRE short volume in darkpool.py.")

    print()


if __name__ == "__main__":
    main()
