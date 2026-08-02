#!/usr/bin/env python3
"""
SAM USDJPY History + At-a-Glance Summary

Fetches USDJPY=X daily OHLC from Yahoo Finance, maintains workbook/USDJPY.tsv
(5Y rolling), and prints a compact summary block: current level, recent
ranges (30d/90d/52wk), and days since last intraday touch of key levels.

Source: Yahoo Finance via yfinance (USDJPY=X)

Reference levels (matched to THESIS KEY THRESHOLDS):
  160  Historic MOF strike zone (Apr30/May6 2026); live playbook zone 162-163, disorder-not-level (CH-011)
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
    (160, "MOF historic-strike zone"),
    (155, "Phase 2 onset"),
    (150, "Psychological"),
    (145, "Forced unwind"),
    (140, "Aug 2024 low"),
]

# Touch tolerance — within this many yen counts as a touch of the level.
# Reason: strict ≥/≤ comparison failed May 6 (low 155.05 missed 155 as a Phase 2 touch).
# 0.10y captures near-touches without losing precision on the 5y-range thresholds.
TOUCH_TOLERANCE = 0.10

# Intraday-range alert thresholds (high - low for a single trading day).
# Calibrated against MOF intervention events:
#   Apr 30 2026: 5.15y range (¥5.48T intervention)
#   May 6 2026:  2.84y range (¥4.3T intervention)
# Normal USDJPY daily range is 0.5-1.5y. >2.5y is a stress event.
INTRADAY_RANGE_WARN = 2.5      # 🟠 stress event — investigate
INTRADAY_RANGE_CRIT = 4.0      # 🔴 intervention-grade move

# Confirmed MOF intervention episodes (public record). Touches near these
# dates get a MOF marker; touches NOT near these dates = "no MOF" (level was
# hit naturally without policy response).
# Format: (date, label_compact, size_trillion_yen)
# Labels use MonYYYY (e.g. "May2026") — never "May26", which mis-reads as a
# day-of-month ("May 26"); that exact mis-parse propagated on 2026-06-09.
MOF_INTERVENTIONS = [
    ("2022-09-22", "Sep2022", 2.84),  # first since 1998; USDJPY 145 → 140
    ("2022-10-21", "Oct2022", 6.35),  # stealth Oct 21-24; combined Q4 2022 ¥9.2T
    ("2024-04-29", "Apr2024", 5.5),   # first 2024 act; USDJPY 160.17 peak
    ("2024-05-01", "May2024", 4.3),   # second 2024 act; combined Apr/May ¥9.8T
    ("2024-07-11", "Jul2024", 5.5),   # pre-Aug 2024 unwind
    ("2026-04-30", "Apr2026", 5.48),  # post Apr 28 BOJ hawkish hold; USDJPY 160.70 peak → 155.55 intraday low (5.15y range); first since Jul 2024
    ("2026-05-06", "May2026", 4.3),   # Golden Week round; intraday low 155.05 (2.84y range); combined Apr/May ~¥10T (~$63.5B) — largest since 2022 per BofA
]
INTERVENTION_WINDOW_DAYS = 3  # touch date within ±N days of intervention = match


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
    """Append fully-closed daily rows to TSV. Skips today (intraday partial).
    Returns count appended."""
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

    # Derive "today" in the INDEX's own timezone, not local time. yfinance labels
    # USDJPY=X bars in Europe/London; comparing them against a local (Eastern) date
    # meant any boot run after ~19:00 ET saw the next London-day's few-hours-old
    # partial bar as "not today" and appended it as final. Idempotent-by-date then
    # made it permanent. That wrote truncated bars for 10 of the last 60 sessions —
    # every one under-stating the range — including 2026-07-30, recorded as a 0.33y
    # day when the true range was 5.74y (largest yen move since Dec-2023, suspected
    # MOF op). The intraday-range alert below is the disorder detector gating the MOF
    # strike-watch, so the failure was silent and FALSE-NEGATIVE.
    idx_tz = getattr(df.index, "tz", None)
    today_str = datetime.now(idx_tz).strftime("%Y-%m-%d")
    new_rows = []
    for ts, row in df.iterrows():
        date_str = ts.strftime("%Y-%m-%d")
        if date_str in existing_dates:
            continue
        # Skip today AND anything later — USDJPY=X trades 24/5, so the current bar is
        # an intraday partial. Let it land in TSV tomorrow when the day is fully closed.
        if date_str >= today_str:
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

    rows = sorted(rows, key=lambda r: r["date"])  # defensive: key on max-date, not file last-row (fixes Jun-16 out-of-order-append mis-report)
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

    # 5-trading-day delta (one trading week) — direction/velocity context
    if len(rows) >= 6:
        delta_5d = current - rows[-6]["close"]
    else:
        delta_5d = None

    def days_since_level(level):
        """Directional touch — looks at HIGH for above-current levels,
        LOW for below-current levels. Uses TOUCH_TOLERANCE band so near-touches
        register (e.g., May 6 low 155.05 counts as a touch of 155).
        Returns (days, touch_date_str) or (None, None) if never touched in window."""
        for r in reversed(rows):
            if level >= current:
                if r["high"] >= level - TOUCH_TOLERANCE:
                    td = date.fromisoformat(r["date"])
                    return (today - td).days, r["date"]
            else:
                if r["low"] <= level + TOUCH_TOLERANCE:
                    td = date.fromisoformat(r["date"])
                    return (today - td).days, r["date"]
        return None, None

    def mof_marker(touch_date_str):
        """Returns 'MOF <label>' if touch is within window of an intervention,
        else 'no MOF'. Returns '' if touch_date_str is None."""
        if not touch_date_str:
            return ""
        td = date.fromisoformat(touch_date_str)
        for iv_date_str, label, _size in MOF_INTERVENTIONS:
            iv_d = date.fromisoformat(iv_date_str)
            if abs((td - iv_d).days) <= INTERVENTION_WINDOW_DAYS:
                return f"MOF {label}"
        return "no MOF"

    color = color_for_price(current)
    stale_tag = f" (STALE +{days_since_latest}d)" if days_since_latest > 3 else ""
    trend_tag = f" (5d: {delta_5d:+.1f})" if delta_5d is not None else ""

    line1 = (
        f"  {color} USDJPY {current:.2f}{trend_tag}{stale_tag} | "
        f"30d: {r30[0]:.1f}-{r30[1]:.1f} | "
        f"90d: {r90[0]:.1f}-{r90[1]:.1f} | "
        f"52wk: {r52w[0]:.1f}-{r52w[1]:.1f}"
    )
    print(line1)

    # Format: "level → Nd, MOF state" — arrow disambiguates level from days count
    touch_parts = []
    for level, _name in REFERENCE_LEVELS:
        days, touch_date_str = days_since_level(level)
        if days is None:
            touch_parts.append(f"{level} → n/a")
        else:
            marker = mof_marker(touch_date_str)
            touch_parts.append(f"{level} → {days}d, {marker}")
    line2 = f"  {color} Days since touch: " + " | ".join(touch_parts)
    print(line2)

    # Intraday-range alert — flag single-day high-low moves that suggest
    # intervention or capitulation. Apr 30 2026 misread as "Tokyo session reprice"
    # because close-to-close looked tame (intraday range was 5.15y = MOF intervention).
    recent = rows[-5:] if len(rows) >= 5 else rows
    ranges = [(r["date"], r["high"] - r["low"]) for r in recent]
    max_date, max_range = max(ranges, key=lambda x: x[1])
    latest_range = rows[-1]["high"] - rows[-1]["low"]

    range_marker = "🟢"
    range_note = "normal daily range"
    if max_range >= INTRADAY_RANGE_CRIT:
        range_marker = "🔴"
        range_note = f"INTERVENTION-GRADE move {max_date} ({max_range:.2f}y intraday range)"
    elif max_range >= INTRADAY_RANGE_WARN:
        range_marker = "🟠"
        range_note = f"stress-event move {max_date} ({max_range:.2f}y intraday range — investigate)"

    print(f"  {range_marker} Intraday range (5d max): {max_range:.2f}y on {max_date} | latest: {latest_range:.2f}y | {range_note}")


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
