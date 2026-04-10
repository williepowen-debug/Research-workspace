#!/usr/bin/env python3
"""
REGINALD Earnings Countdown
Counts trading days until thesis-name earnings dates.
Flags anything within 5 trading days.

Usage:
  .venv/bin/python3 AGENTS/REGINALD/scripts/earnings_countdown.py
"""

from datetime import datetime, timedelta

# Hardcoded earnings dates (update as confirmed)
# Format: (ticker, date_str, time, confirmed)
EARNINGS = [
    ("MTB",  "2026-04-15", "pre-market", True),
    ("KEY",  "2026-04-16", "pre-market", True),
    ("CFG",  "2026-04-16", "morning",    True),
    ("RF",   "2026-04-17", "pre-market", True),
    ("ZION", "2026-04-20", "after-close", False),
    ("WAL",  "2026-04-21", "morning",    False),
    ("OZK",  "2026-04-21", "after-close", True),
    ("WTFC", "2026-04-20", "after-close", False),
    ("PB",   "2026-04-22", "morning",    False),
    ("VLY",  "2026-04-23", "after-close", False),
    ("SSB",  "2026-04-23", "after-close", False),
    ("EGBN", "2026-04-23", "morning",    False),
    ("ASB",  "2026-04-23", "after-close", False),
]

# Our position names (highlight these)
POSITION_TICKERS = {"WAL", "OZK", "EGBN", "KRE", "ZION", "SSB"}


def trading_days_between(start_date, end_date):
    """Count trading days (weekdays) between two dates, exclusive of start."""
    if end_date <= start_date:
        return 0
    days = 0
    current = start_date + timedelta(days=1)
    while current <= end_date:
        if current.weekday() < 5:  # Monday=0, Friday=4
            days += 1
        current += timedelta(days=1)
    return days


def calendar_days_between(start_date, end_date):
    """Calendar days between two dates."""
    return (end_date - start_date).days


def main():
    today = datetime.now().date()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    print(f"\n{'='*70}")
    print(f"  REGINALD Earnings Countdown — {now}")
    print(f"{'='*70}")

    # Sort by date
    sorted_earnings = sorted(EARNINGS, key=lambda x: x[1])

    # Split into upcoming and past
    upcoming = []
    past = []
    for ticker, date_str, time_of_day, confirmed in sorted_earnings:
        edate = datetime.strptime(date_str, "%Y-%m-%d").date()
        if edate >= today:
            upcoming.append((ticker, edate, time_of_day, confirmed))
        else:
            past.append((ticker, edate, time_of_day, confirmed))

    if not upcoming:
        print("\n  No upcoming earnings dates. Update the script with new dates.")
        return

    print(f"\n  {'Ticker':<6} {'Date':>12} {'Time':<12} {'Cal Days':>9} {'Trd Days':>9} {'Status':<20}")
    print(f"  {'-'*70}")

    for ticker, edate, time_of_day, confirmed in upcoming:
        cal_days = calendar_days_between(today, edate)
        trd_days = trading_days_between(today, edate)
        conf_str = "✓" if confirmed else "~est"

        # Flag proximity
        if trd_days <= 0:
            flag = "🔴 TODAY"
        elif trd_days <= 2:
            flag = "🔴 IMMINENT"
        elif trd_days <= 5:
            flag = "⚠️  THIS WEEK"
        elif trd_days <= 10:
            flag = "🟡 Next week"
        else:
            flag = ""

        # Highlight position names
        marker = " ⭐" if ticker in POSITION_TICKERS else ""

        print(f"  {ticker:<6} {edate.strftime('%a %b %d'):>12} {time_of_day:<12} {cal_days:>8}d {trd_days:>8}d {flag:<20} {conf_str}{marker}")

    # Summary
    next_report = upcoming[0]
    print(f"\n  Next up: {next_report[0]} on {next_report[1].strftime('%a %b %d')}")

    # Position-name countdown
    position_upcoming = [e for e in upcoming if e[0] in POSITION_TICKERS]
    if position_upcoming:
        print(f"\n  Position names countdown:")
        for ticker, edate, _, _ in position_upcoming:
            trd_days = trading_days_between(today, edate)
            print(f"    {ticker}: {trd_days} trading days")

    if past:
        print(f"\n  Past (reported): {', '.join(t[0] for t in past)}")

    print()


if __name__ == "__main__":
    main()
