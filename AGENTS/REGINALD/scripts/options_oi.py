#!/usr/bin/env python3
"""
REGINALD Options Open Interest Monitor
Pulls options chains via yfinance for thesis tickers.
Computes put/call ratios, top put strikes, and appends to OPTIONS_OI.tsv.

Usage:
  .venv/bin/python3 AGENTS/REGINALD/scripts/options_oi.py              # full run
  .venv/bin/python3 AGENTS/REGINALD/scripts/options_oi.py --print      # print latest from TSV
"""

import sys
from datetime import datetime, timedelta
from pathlib import Path

try:
    import yfinance as yf
except ImportError:
    print("  ERROR: yfinance not installed.")
    sys.exit(1)

TICKERS = ["KRE", "WAL", "OZK", "EGBN"]

REGINALD_DIR = Path(__file__).resolve().parent.parent
WORKBOOK = REGINALD_DIR / "workbook"
OPTIONS_TSV = WORKBOOK / "OPTIONS_OI.tsv"

# Header for the TSV
TSV_HEADER = "Date\tTicker\tExpiry\tTotal_Put_OI\tTotal_Call_OI\tPC_Ratio\tTop_Put_Strike\tTop_Put_OI\tTop5_Puts\n"


def get_options_data(ticker_str):
    """Fetch options data for a ticker. Returns list of expiry summaries."""
    try:
        t = yf.Ticker(ticker_str)
        expiries = t.options
        if not expiries:
            return []
    except Exception:
        return []

    # Focus on near-term expiries (next 90 days)
    cutoff = (datetime.now() + timedelta(days=90)).strftime("%Y-%m-%d")
    results = []

    for expiry in expiries:
        if expiry > cutoff:
            break
        try:
            chain = t.option_chain(expiry)
            puts = chain.puts
            calls = chain.calls

            total_put_oi = int(puts["openInterest"].sum()) if "openInterest" in puts.columns else 0
            total_call_oi = int(calls["openInterest"].sum()) if "openInterest" in calls.columns else 0

            pc_ratio = round(total_put_oi / total_call_oi, 2) if total_call_oi > 0 else 999.0

            # Top 5 put strikes by OI
            top_puts = []
            if "openInterest" in puts.columns and len(puts) > 0:
                sorted_puts = puts.sort_values("openInterest", ascending=False).head(5)
                for _, row in sorted_puts.iterrows():
                    oi = int(row["openInterest"]) if row["openInterest"] == row["openInterest"] else 0
                    if oi > 0:
                        top_puts.append((row["strike"], oi))

            top_strike = top_puts[0][0] if top_puts else 0
            top_oi = top_puts[0][1] if top_puts else 0
            top5_str = "; ".join(f"${s:.0f}={oi:,}" for s, oi in top_puts)

            results.append({
                "expiry": expiry,
                "total_put_oi": total_put_oi,
                "total_call_oi": total_call_oi,
                "pc_ratio": pc_ratio,
                "top_strike": top_strike,
                "top_oi": top_oi,
                "top5_str": top5_str,
            })
        except Exception:
            continue

    return results


def append_tsv(date_str, ticker, data_list):
    """Append today's options data to TSV if not already present."""
    existing = set()
    if OPTIONS_TSV.exists():
        with open(OPTIONS_TSV) as f:
            for line in f:
                parts = line.strip().split("\t")
                if len(parts) >= 3:
                    existing.add((parts[0], parts[1], parts[2]))
    else:
        with open(OPTIONS_TSV, "w") as f:
            f.write(TSV_HEADER)

    with open(OPTIONS_TSV, "a") as f:
        for d in data_list:
            key = (date_str, ticker, d["expiry"])
            if key not in existing:
                f.write(
                    f"{date_str}\t{ticker}\t{d['expiry']}\t{d['total_put_oi']}\t"
                    f"{d['total_call_oi']}\t{d['pc_ratio']}\t{d['top_strike']}\t"
                    f"{d['top_oi']}\t{d['top5_str']}\n"
                )


def main():
    if "--print" in sys.argv:
        if OPTIONS_TSV.exists():
            with open(OPTIONS_TSV) as f:
                print(f.read())
        else:
            print("  No OPTIONS_OI.tsv yet.")
        return

    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    print(f"\n{'='*70}")
    print(f"  REGINALD Options OI Monitor — {now.strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*70}")

    for ticker in TICKERS:
        print(f"\n  {ticker}")
        print(f"  {'-'*50}")

        data = get_options_data(ticker)
        if not data:
            print(f"  No options data available.")
            continue

        # Aggregate across all near-term expiries
        total_puts = sum(d["total_put_oi"] for d in data)
        total_calls = sum(d["total_call_oi"] for d in data)
        agg_pc = round(total_puts / total_calls, 2) if total_calls > 0 else 999.0

        print(f"  Expiries scanned: {len(data)} (next 90 days)")
        print(f"  Aggregate Put OI:  {total_puts:>10,}")
        print(f"  Aggregate Call OI: {total_calls:>10,}")
        print(f"  Put/Call Ratio:    {agg_pc:>10.2f}x", end="")
        if agg_pc > 3:
            print("  🔴 EXTREME bearish")
        elif agg_pc > 2:
            print("  🟠 Very bearish")
        elif agg_pc > 1.5:
            print("  🟡 Bearish")
        else:
            print("  ⚪ Normal")

        # Show top expiries by put OI
        sorted_data = sorted(data, key=lambda x: x["total_put_oi"], reverse=True)
        print(f"\n  Top expiries by put OI:")
        for d in sorted_data[:5]:
            print(f"    {d['expiry']:>12}  Puts: {d['total_put_oi']:>8,}  Calls: {d['total_call_oi']:>8,}  P/C: {d['pc_ratio']:.1f}x")
            if d["top5_str"]:
                print(f"                   Top strikes: {d['top5_str']}")

        # Append to TSV
        append_tsv(date_str, ticker, data)

    # Ensure TSV has header if new
    if OPTIONS_TSV.exists():
        print(f"\n  Updated OPTIONS_OI.tsv")

    print()


if __name__ == "__main__":
    main()
