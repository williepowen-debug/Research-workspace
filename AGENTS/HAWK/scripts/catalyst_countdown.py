#!/usr/bin/env python3
"""
HAWK Catalyst Countdown — Days to Key Dates

Reads CALENDAR.md and calculates days until each event. Outputs countdown
table with 🔴 alerts for items within 7 days.

Usage:
  .venv/bin/python3 AGENTS/HAWK/scripts/catalyst_countdown.py
  .venv/bin/python3 AGENTS/HAWK/scripts/catalyst_countdown.py --days 30    # horizon override
"""

import sys
import re
import argparse
from datetime import datetime, timedelta
from pathlib import Path

HAWK_DIR = Path(__file__).resolve().parent.parent
CALENDAR_MD = HAWK_DIR / "CALENDAR.md"

DEFAULT_HORIZON = 60  # days to look ahead


def parse_calendar():
    """Parse CALENDAR.md for events with dates."""
    if not CALENDAR_MD.exists():
        return []
    
    events = []
    with open(CALENDAR_MD) as f:
        content = f.read()
    
    # Look for table rows with dates
    # Pattern: | Date | Event | ... | Status |
    lines = content.split("\n")
    for line in lines:
        if line.startswith("|") and "---" not in line:
            parts = [p.strip() for p in line.split("|")]
            parts = [p for p in parts if p]  # Remove empty
            
            if len(parts) >= 4:
                date_str = parts[0]
                event = parts[1]
                
                # Skip header rows
                if date_str.lower() in ["date", "priority"]:
                    continue
                
                # Extract priority from event or look for 🔴🟡⚪
                priority = ""
                if "🔴🔴" in line or "🔴" in date_str:
                    priority = "🔴🔴"
                elif "🔴" in line:
                    priority = "🔴"
                elif "🟡" in line:
                    priority = "🟡"
                
                # Try to parse date
                parsed_date = None
                
                # Patterns: "Apr 12-13", "May 12-13", "TBD", "Ongoing"
                date_patterns = [
                    r"([A-Za-z]{3})\s+(\d{1,2})-\d{1,2}",  # Apr 12-13
                    r"([A-Za-z]{3})\s+(\d{1,2})",          # May 12
                    r"([A-Za-z]{3,})\s+(\d{4})",          # May 2026
                ]
                
                year = 2026  # Default year
                
                for pattern in date_patterns:
                    match = re.search(pattern, date_str)
                    if match:
                        try:
                            month_str = match.group(1)
                            day_str = match.group(2)
                            
                            # Handle year in third pattern
                            if len(match.groups()) >= 2 and len(day_str) == 4:
                                year = int(day_str)
                                day_str = "1"  # Default to 1st of month
                            
                            # Try parsing
                            date_fmt = f"{month_str} {day_str} {year}"
                            parsed_date = datetime.strptime(date_fmt, "%b %d %Y").date()
                            break
                        except ValueError:
                            try:
                                parsed_date = datetime.strptime(date_fmt, "%B %d %Y").date()
                                break
                            except ValueError:
                                continue
                
                # Check for TBD/Ongoing
                is_tbd = "TBD" in date_str or "Ongoing" in date_str
                
                events.append({
                    "date_str": date_str,
                    "date": parsed_date,
                    "event": event,
                    "priority": priority,
                    "is_tbd": is_tbd,
                    "raw_line": line
                })
    
    return events


def trading_days_between(start_date, end_date):
    """Count weekdays between two dates."""
    if end_date <= start_date:
        return 0
    days = 0
    current = start_date + timedelta(days=1)
    while current <= end_date:
        if current.weekday() < 5:
            days += 1
        current += timedelta(days=1)
    return days


def main():
    parser = argparse.ArgumentParser(description="HAWK catalyst countdown")
    parser.add_argument("--days", type=int, default=DEFAULT_HORIZON, help="Days horizon")
    args = parser.parse_args()
    
    horizon = args.days
    today = datetime.now().date()
    now = datetime.now().strftime("%Y-%m-%d %H:%M ET")
    
    print(f"\n{'='*70}")
    print(f"  HAWK Catalyst Countdown — {now}")
    print(f"  War Day: 51 | Scenario: D 82% / C 12% / B 6%")
    print(f"{'='*70}")
    
    events = parse_calendar()
    if not events:
        print(f"\n  ERROR: Could not parse {CALENDAR_MD}")
        return 1
    
    # Categorize events
    upcoming = []
    past = []
    tbd = []
    horizon_cutoff = today + timedelta(days=horizon)
    
    for e in events:
        if e["is_tbd"]:
            tbd.append(e)
        elif e["date"]:
            if e["date"] < today:
                past.append(e)
            elif e["date"] <= horizon_cutoff:
                upcoming.append(e)
    
    # Sort by date
    upcoming.sort(key=lambda x: x["date"] if x["date"] else today + timedelta(days=999))
    
    # 🔴 IMMINENT (≤7 calendar days or ≤5 trading days)
    imminent = []
    this_month = []
    
    for e in upcoming:
        edate = e["date"]
        cal_days = (edate - today).days
        trd_days = trading_days_between(today, edate)
        
        if cal_days <= 7 or trd_days <= 5:
            imminent.append((e, cal_days, trd_days))
        else:
            this_month.append((e, cal_days, trd_days))
    
    # Output IMMINENT
    if imminent:
        print(f"\n  🔴 IMMINENT (≤7 days)")
        print(f"  {'-'*66}")
        for e, cal_days, trd_days in imminent:
            pri = e["priority"] or "  "
            day_of_week = e["date"].strftime("%a")
            print(f"  {pri} {e['date'].strftime('%Y-%m-%d')} ({day_of_week})  {cal_days:>2}d cal / {trd_days:>2}d trd  {e['event']}")
    
    # Output UPCOMING
    if this_month:
        print(f"\n  📅 UPCOMING (within {horizon} days)")
        print(f"  {'-'*66}")
        for e, cal_days, trd_days in this_month:
            pri = e["priority"] or "  "
            day_of_week = e["date"].strftime("%a")
            event_str = e["event"][:45] + "..." if len(e["event"]) > 45 else e["event"]
            print(f"  {pri} {e['date'].strftime('%Y-%m-%d')} ({day_of_week})  {cal_days:>3}d cal / {trd_days:>3}d trd  {event_str}")
    
    # Output TBD
    if tbd:
        print(f"\n  ⏳ TBD / ONGOING")
        print(f"  {'-'*66}")
        for e in tbd:
            pri = e["priority"] or "  "
            if "🔴" in e["priority"]:
                print(f"  {pri} {e['date_str']:<15} {e['event']}")
    
    # Summary
    high_pri = [x for x in upcoming if "🔴" in x.get("priority", "")]
    if high_pri:
        print(f"\n  🔴 HIGH PRIORITY in horizon: {len(high_pri)}")
        for e in high_pri:
            cal_days = (e["date"] - today).days
            print(f"     • {e['date'].strftime('%a %b %d')} ({cal_days}d) — {e['event']}")
    
    # Key checkpoint
    checkpoint_date = datetime(2026, 5, 12).date()
    if today <= checkpoint_date:
        days_to_checkpoint = (checkpoint_date - today).days
        trd_to_checkpoint = trading_days_between(today, checkpoint_date)
        print(f"\n  ⏰ KEY CHECKPOINT: May 12 Ceasefire Checkpoint")
        print(f"     {days_to_checkpoint} calendar days / {trd_to_checkpoint} trading days remaining")
    
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
