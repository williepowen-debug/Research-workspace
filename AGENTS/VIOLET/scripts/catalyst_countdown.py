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


def trading_days_until(target: date, today: date) -> int:
    """Rough trading-day count excluding weekends. Ignores US holidays."""
    if target < today:
        return -1 * trading_days_until(today, target)
    days = 0
    d = today
    while d < target:
        d = d.fromordinal(d.toordinal() + 1)
        if d.weekday() < 5:
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
    for r in rows:
        try:
            ev_date = datetime.strptime(r["date"], "%Y-%m-%d").date()
        except ValueError:
            continue
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
