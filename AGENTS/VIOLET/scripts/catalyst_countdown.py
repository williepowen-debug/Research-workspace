#!/usr/bin/env python3
"""VIOLET Catalyst Countdown.

Reads AGENTS/VIOLET/workbook/CATALYSTS.tsv and prints a countdown table.
Flags events within 5 trading days and internal VIOLET checkpoints.

Usage:
  .venv/bin/python3 AGENTS/VIOLET/scripts/catalyst_countdown.py
  .venv/bin/python3 AGENTS/VIOLET/scripts/catalyst_countdown.py --json
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import date, datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
CATALYSTS = SCRIPT_DIR.parent / "workbook" / "CATALYSTS.tsv"


# NYSE full-day closures. Added 2026-09-04 (KB-VIO-240): this counter was
# weekend-only and printed Labor Day (Mon 2026-09-07) as "1 trading day" out from
# Fri 9/4 — a day that does not exist. Found by adding the Labor Day row, not by
# the tool. A holiday-blind trading-day count is off by one IN THE DIRECTION OF
# CALLING AN EVENT EARLY, which is the dangerous direction for a sustain counter
# or a +N-session grade window (RED-FT-10's chain and every VIO-FOMC-0916 leg
# cross a holiday this month).
#
# ⚠️ HALF-DAYS ARE DELIBERATELY NOT LISTED. A 13:00 early close is a full trading
# day for a session count; it matters for a SETTLE, and that is a different
# question this tool does not answer. Listing them here would silently drop real
# sessions — the same off-by-one in the same dangerous direction.
NYSE_HOLIDAYS = {
    # 2026
    "2026-01-01",  # New Year's Day (Thu)
    "2026-01-19",  # MLK Jr. Day (3rd Mon)
    "2026-02-16",  # Washington's Birthday (3rd Mon)
    "2026-04-03",  # Good Friday
    "2026-05-25",  # Memorial Day (last Mon)
    "2026-06-19",  # Juneteenth (Fri)
    "2026-07-03",  # Independence Day OBSERVED (Jul 4 is a Saturday)
    "2026-09-07",  # Labor Day (1st Mon)
    "2026-11-26",  # Thanksgiving (4th Thu)
    "2026-12-25",  # Christmas (Fri)
    # 2027
    "2027-01-01", "2027-01-18", "2027-02-15", "2027-03-26", "2027-05-31",
    "2027-06-18",  # Juneteenth OBSERVED (Jun 19 is a Saturday)
    "2027-07-05",  # Independence Day OBSERVED (Jul 4 is a Sunday)
    "2027-09-06", "2027-11-25",
    "2027-12-24",  # Christmas OBSERVED (Dec 25 is a Saturday)
}
# The table is finite, so say where it ends rather than degrading silently to a
# weekend-only count — an unmaintained holiday table that keeps answering is the
# same failure it was built to fix, one year later.
HOLIDAY_COVERAGE = (date(2026, 1, 1), date(2027, 12, 31))


def is_trading_day(d: date) -> bool:
    return d.weekday() < 5 and d.isoformat() not in NYSE_HOLIDAYS


def coverage_warning(target: date, today: date) -> str | None:
    """Non-empty when a span reaches outside the holiday table's known window."""
    lo, hi = HOLIDAY_COVERAGE
    a, b = min(today, target), max(today, target)
    if a < lo or b > hi:
        return (f"⚠️  HOLIDAY TABLE COVERS {lo}..{hi} — the span {a}..{b} reaches "
                f"outside it, so this count is WEEKEND-ONLY there and may run long. "
                f"Extend NYSE_HOLIDAYS in catalyst_countdown.py.")
    return None


def trading_days_until(target: date, today: date) -> int:
    """Trading-day count excluding weekends AND NYSE full-day closures."""
    if target < today:
        return -1 * trading_days_until(today, target)
    days = 0
    d = today
    while d < target:
        d = d.fromordinal(d.toordinal() + 1)
        if is_trading_day(d):
            days += 1
    return days


def load_catalysts() -> list[dict]:
    with open(CATALYSTS) as f:
        return list(csv.DictReader(f, delimiter="\t"))


def classify(td: int, impact: str, is_internal: bool) -> str:
    if td < 0:
        return "PAST"
    if is_internal:
        if td <= 5: return "🟣 CHECKPOINT"
        return "  checkpoint"
    if td <= 5:
        if impact == "HIGH": return "🔴 IMMINENT HIGH"
        if impact == "MEDIUM": return "🟠 IMMINENT"
        return "🟡 imminent"
    if td <= 14:
        if impact == "HIGH": return "🟠 NEAR HIGH"
        return "🟡 near"
    return "⚪ scheduled"


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--json", action="store_true")
    p.add_argument("--all", action="store_true", help="Include past events")
    args = p.parse_args(argv)

    rows = load_catalysts()
    today = date.today()

    enriched = []
    warns: list[str] = []
    for r in rows:
        try:
            ev_date = datetime.strptime(r["date"], "%Y-%m-%d").date()
        except ValueError:
            continue
        w = coverage_warning(ev_date, today)
        if w and w not in warns:
            warns.append(w)
        td = trading_days_until(ev_date, today)
        if td < 0 and not args.all:
            continue
        is_internal = r.get("type") == "INTERNAL" or "checkpoint" in r.get("event", "").lower()
        enriched.append({
            "date": r["date"],
            "td": td,
            "event": r["event"],
            "type": r.get("type", ""),
            "domain": r.get("agent_domain", ""),
            "impact": r.get("expected_vol_impact", "") or "—",
            "notes": r.get("notes", ""),
            "status": classify(td, r.get("expected_vol_impact", ""), is_internal),
        })
    enriched.sort(key=lambda x: (x["td"], x["event"]))

    if args.json:
        print(json.dumps({"today": today.isoformat(), "catalysts": enriched}, indent=2))
        return 0

    print(f"VIOLET CATALYST COUNTDOWN  •  {today.isoformat()} ({today.strftime('%A')})")
    for w in warns:
        print(f"  {w}")
    print("─" * 100)
    print(f"{'Date':<12} {'TD':>4}  {'Status':<18} {'Impact':<7} {'Domain':<18} {'Event'}")
    print("─" * 100)
    for e in enriched:
        td_str = f"{e['td']:>3}d" if e["td"] >= 0 else "past"
        print(f"{e['date']:<12} {td_str:>4}  {e['status']:<18} {e['impact']:<7} {e['domain']:<18} {e['event']}")

    # Highlight section
    imminent = [e for e in enriched if 0 <= e["td"] <= 5]
    if imminent:
        print("\n⚠️  IMMINENT (≤5 trading days):")
        for e in imminent:
            print(f"  • {e['date']} ({e['td']}d) — {e['event']}")
            if e["notes"]:
                print(f"    Note: {e['notes']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
