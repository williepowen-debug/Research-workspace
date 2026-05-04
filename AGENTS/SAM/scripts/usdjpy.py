#!/usr/bin/env python3
"""
SAM USDJPY History + At-a-Glance Summary

Fetches USDJPY=X daily OHLC from Yahoo Finance, maintains workbook/USDJPY.tsv
(5Y rolling), and prints a compact summary block: current level, recent
ranges (30d/90d/52wk), and days since last intraday touch of key levels.

Source: Yahoo Finance via yfinance (USDJPY=X)

Reference levels (matched to THESIS KEY THRESHOLDS):
  160  MOF intervention zone
  155  Phase 2 carry unwind onset
  150  Psychological / mid-cycle
  145  Forced unwind / unhedged positions underwater
  140  Aug 2024 post-unwind low / structural floor

"Touch" semantics: directional. For levels ABOVE current close (yen-weak side),
days since HIGH reached up to level (e.g., last time we hit intervention zone).
For levels BELOW current close (yen-strong side), days since LOW reached down
to level (e.g., last time yen was that strong). Always asks "when did we last
touch this level from the current side?"

Usage:
  .venv/bin/python3 AGENTS/SAM/scripts/usdjpy.py              # refresh + summary
  .venv/bin/python3 AGENTS/SAM/scripts/usdjpy.py --summary    # summary only
  .venv/bin/python3 AGENTS/SAM/scripts/usdjpy.py --refresh    # refresh only
"""

import sys
from datetime import date, datetime, timedelta
from pathlib import Path

SAM_DIR = Path(__file__).resolve().parent.parent
WORKBOOK = SAM_DIR / "workbook"
USDJPY_TSV = WORKBOOK / "USDJPY.tsv"

TSV_HEADER = "Date\tOpen\tHigh\tLow\tClose\n"

# Reference levels matched to THESIS KEY THRESHOLDS table
REFERENCE_LEVELS = [
    (160, "MOF intervention"),
    (155, "Phase 2 onset"),
    (150, "Psychological"),
    (145, "Forced unwind"),
    (140, "Aug 2024 low"),
]


def fetch_yfinance(period="5y"):
    """Fetch USDJPY=X OHLC from yfinance. Returns DataFrame or None."""
    try:
        import yfinance as yf
        ticker = yf.Ticker("USDJPY=X")
        df = ticker.history(period=period, interval="1d", auto_adjust=False)
        if df.empty:
            return None
        return df
    except Exception as e:
        print(f"  ERROR fetching from yfinance: {e}")
        return None


def load_tsv():
    """Load existing TSV into list of dicts ordered by date asc. [] if missing."""
    if not USDJPY_TSV.exists():
        return []
    rows = []
    with open(USDJPY_TSV) as f:
        next(f, None)  # skip header
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if len(parts) >= 5:
                try:
                    rows.append({
                        "date": parts[0],
                        "open": float(parts[1]),
                        "high": float(parts[2]),
                        "low": float(parts[3]),
                        "close": float(parts[4]),
                    })
                except ValueError:
                    pass
    rows.sort(key=lambda r: r["date"])
    return rows


def merge_and_write(df):
    """Append rows in df that aren't already in TSV. Returns count appended."""
    existing_dates = set()
    if USDJPY_TSV.exists():
        with open(USDJPY_TSV) as f:
            next(f, None)
            for line in f:
                parts = line.split("\t", 1)
                if parts:
                    existing_dates.add(parts[0])
    else:
        with open(USDJPY_TSV, "w") as f:
            f.write(TSV_HEADER)

    new_rows = []
    for ts, row in df.iterrows():
        date_str = ts.strftime("%Y-%m-%d")
        if date_str in existing_dates:
            continue
        # NaN check (yfinance can return NaN rows for non-trading days)
        vals = [row["Open"], row["High"], row["Low"], row["Close"]]
        if any(v != v for v in vals):  # NaN != NaN
            continue
        new_rows.append((date_str, vals[0], vals[1], vals[2], vals[3]))

    if new_rows:
        new_rows.sort(key=lambda r: r[0])
        with open(USDJPY_TSV, "a") as f:
            for date_str, op, hi, lo, cl in new_rows:
                f.write(f"{date_str}\t{op:.4f}\t{hi:.4f}\t{lo:.4f}\t{cl:.4f}\n")

    return len(new_rows)


def color_for_price(close):
    """Color marker reflecting yen-weakness state (FXY-long position lens)."""
    if close >= 160:
        return "🔴"  # intervention zone
    if close >= 156:
        return "🟠"  # close to intervention, fuel accumulating
    if close >= 150:
        return "🟡"  # active range
    return "🟢"      # thesis playing out


def print_summary(rows):
    """Print compact summary block (2 marker-prefixed lines for boot collapse)."""
    if not rows:
        print("  ⚠️  USDJPY.tsv is empty — run --refresh first")
        return

    latest = rows[-1]
    today = date.today()
    latest_date = date.fromisoformat(latest["date"])
    days_since_latest = (today - latest_date).days

    def date_n_days_ago(n):
        return today - timedelta(days=n)

    def range_for_window(days):
        cutoff = date_n_days_ago(days)
        windowed = [r for r in rows if date.fromisoformat(r["date"]) >= cutoff]
        if not windowed:
            return None, None
        return min(r["low"] for r in windowed), max(r["high"] for r in windowed)

    r30 = range_for_window(30)
    r90 = range_for_window(90)
    r52w = range_for_window(365)

    current = latest["close"]

    def days_since_level(level):
        """Directional touch — looks at HIGH for above-current levels,
        LOW for below-current levels. Returns None if never touched in window."""
        for r in reversed(rows):
            if level >= current:
                if r["high"] >= level:
                    return (today - date.fromisoformat(r["date"])).days
            else:
                if r["low"] <= level:
                    return (today - date.fromisoformat(r["date"])).days
        return None

    color = color_for_price(current)
    stale_tag = f" (STALE +{days_since_latest}d)" if days_since_latest > 3 else ""

    line1 = (
        f"  {color} USDJPY {current:.2f}{stale_tag} | "
        f"30d: {r30[0]:.1f}-{r30[1]:.1f} | "
        f"90d: {r90[0]:.1f}-{r90[1]:.1f} | "
        f"52wk: {r52w[0]:.1f}-{r52w[1]:.1f}"
    )
    print(line1)

    touch_parts = []
    for level, _name in REFERENCE_LEVELS:
        days = days_since_level(level)
        if days is None:
            touch_parts.append(f"{level} (n/a)")
        else:
            touch_parts.append(f"{level} ({days}d)")
    line2 = f"  {color} Days since touch: " + " | ".join(touch_parts)
    print(line2)


def main():
    summary_only = "--summary" in sys.argv
    refresh_only = "--refresh" in sys.argv

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"\n{'='*70}")
    print(f"  SAM USDJPY Monitor — {now}")
    print(f"{'='*70}\n")

    if not summary_only:
        df = fetch_yfinance(period="5y")
        if df is None:
            print("  ⚠️  yfinance fetch failed — falling back to cached TSV")
        else:
            appended = merge_and_write(df)
            if appended > 0:
                print(f"  ✓ Appended {appended} new row(s) to USDJPY.tsv")
            else:
                print(f"  ✓ TSV up to date (no new rows)")

    if not refresh_only:
        rows = load_tsv()
        if not rows:
            print("  ⚠️  USDJPY.tsv empty or missing")
            return 1
        print()
        print_summary(rows)

    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
