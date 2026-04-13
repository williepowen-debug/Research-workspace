#!/usr/bin/env python3
"""
CARL Catalyst Countdown
Reads STATUS.md danger window and TEAM.md catalyst tables, computes
trading days to each upcoming event, and prints a prioritized countdown.

No external data — purely local file parsing.

Usage:
  .venv/bin/python3 AGENTS/CARL/scripts/catalyst_countdown.py
"""

import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

CARL_DIR = Path(__file__).resolve().parent.parent
STATUS_FILE = CARL_DIR / "STATUS.md"
TEAM_FILE = CARL_DIR / "TEAM.md"
SCRATCH_FILE = CARL_DIR / "SCRATCH.md"

# US market holidays for 2026 (known dates)
US_HOLIDAYS_2026 = {
    datetime(2026, 1, 1),   # New Year's
    datetime(2026, 1, 19),  # MLK Day
    datetime(2026, 2, 16),  # Presidents' Day
    datetime(2026, 4, 3),   # Good Friday
    datetime(2026, 5, 25),  # Memorial Day
    datetime(2026, 7, 3),   # Independence Day (observed)
    datetime(2026, 9, 7),   # Labor Day
    datetime(2026, 11, 26), # Thanksgiving
    datetime(2026, 12, 25), # Christmas
}


def trading_days_between(start, end):
    """Count trading days between start (exclusive) and end (inclusive)."""
    if end <= start:
        return 0
    count = 0
    current = start + timedelta(days=1)
    while current <= end:
        if current.weekday() < 5 and current not in US_HOLIDAYS_2026:
            count += 1
        current += timedelta(days=1)
    return count


def parse_date_from_text(text):
    """Extract a date from text like 'Apr 14', 'Apr 26', 'Jul 1', 'Q2', etc."""
    today = datetime.now()
    year = today.year

    # Try explicit patterns: "Apr 14", "May 28", "Jun 1"
    m = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+(\d{1,2})', text)
    if m:
        month_str, day = m.group(1), int(m.group(2))
        months = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
                  "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
        month = months.get(month_str)
        if month:
            try:
                dt = datetime(year, month, day)
                if dt < today - timedelta(days=30):
                    dt = datetime(year + 1, month, day)
                return dt
            except ValueError:
                pass

    # Quarter patterns: "Q2 2026", "Q3"
    m = re.search(r'Q([1-4])\s*(\d{4})?', text)
    if m:
        q = int(m.group(1))
        yr = int(m.group(2)) if m.group(2) else year
        # Use mid-quarter as estimate
        month = {1: 2, 2: 5, 3: 8, 4: 11}[q]
        return datetime(yr, month, 15)

    return None


def extract_danger_window(status_path):
    """Parse DANGER WINDOW table from STATUS.md."""
    events = []
    if not status_path.exists():
        return events

    in_table = False
    with open(status_path) as f:
        for line in f:
            line = line.strip()
            if "DANGER WINDOW" in line:
                in_table = True
                continue
            if in_table and line.startswith("---") and "|" not in line:
                in_table = False
                continue
            if in_table and "|" in line and not line.startswith("|--"):
                parts = [p.strip() for p in line.split("|")]
                parts = [p for p in parts if p]  # remove empty
                if len(parts) >= 3:
                    window = parts[0].strip("*").strip()
                    trigger = parts[1].strip("*").strip()
                    status = parts[2].strip("*").strip() if len(parts) > 2 else ""

                    # Skip header row
                    if "Window" in window or "Trigger" in window:
                        continue
                    # Skip already fired
                    if "\u2705" in status or "FIRED" in status or "PASSED" in status:
                        continue

                    dt = parse_date_from_text(window)
                    if dt:
                        events.append({
                            "date": dt,
                            "label": trigger[:80],
                            "status": status,
                            "source": "STATUS.md",
                        })
    return events


def extract_team_catalysts(team_path):
    """Parse UPCOMING CATALYSTS table from TEAM.md."""
    events = []
    if not team_path.exists():
        return events

    in_table = False
    with open(team_path) as f:
        for line in f:
            line = line.strip()
            if "UPCOMING CATALYSTS" in line:
                in_table = True
                continue
            if in_table and line.startswith("---") and "|" not in line:
                in_table = False
                continue
            if in_table and "|" in line and not line.startswith("|--"):
                parts = [p.strip() for p in line.split("|")]
                parts = [p for p in parts if p]
                if len(parts) >= 3:
                    date_str = parts[0].strip()
                    catalyst = parts[1].strip()
                    agents = parts[2].strip() if len(parts) > 2 else ""

                    if "Date" in date_str or "Catalyst" in date_str:
                        continue

                    # Skip struck-through items
                    if "~~" in catalyst:
                        continue

                    dt = parse_date_from_text(date_str + " " + catalyst)
                    if dt:
                        events.append({
                            "date": dt,
                            "label": catalyst[:80],
                            "status": agents,
                            "source": "TEAM.md",
                        })
    return events


def extract_scratch_items(scratch_path):
    """Parse IMMEDIATE and UPCOMING items from SCRATCH.md."""
    events = []
    if not scratch_path.exists():
        return events

    in_section = None
    with open(scratch_path) as f:
        for line in f:
            stripped = line.strip()
            if "### IMMEDIATE" in stripped:
                in_section = "immediate"
                continue
            elif "### UPCOMING (this week)" in stripped:
                in_section = "week"
                continue
            elif "### UPCOMING (next 2 weeks)" in stripped:
                in_section = "2week"
                continue
            elif "### BACKLOG" in stripped or stripped.startswith("---"):
                in_section = None
                continue

            if in_section and stripped and stripped[0].isdigit():
                # Numbered item like "1. **JPM Q1 earnings — Apr 14 7:00 AM ET**"
                dt = parse_date_from_text(stripped)
                if dt:
                    # Clean up the label
                    label = re.sub(r'^\d+\.\s*', '', stripped)
                    label = re.sub(r'\*\*', '', label)
                    label = label[:80]
                    events.append({
                        "date": dt,
                        "label": label,
                        "status": in_section.upper(),
                        "source": "SCRATCH.md",
                    })
    return events


def priority_emoji(td):
    """Emoji based on trading days out."""
    if td <= 0:
        return "\U0001f534\U0001f534"  # overdue / today
    if td <= 1:
        return "\U0001f534"
    if td <= 3:
        return "\U0001f7e0"
    if td <= 5:
        return "\U0001f7e1"
    return "\u26aa"


def main():
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    print(f"\n{'='*72}")
    print(f"  CARL Catalyst Countdown \u2014 {now}")
    print(f"{'='*72}")

    # Collect events from all sources
    all_events = []
    all_events.extend(extract_danger_window(STATUS_FILE))
    all_events.extend(extract_team_catalysts(TEAM_FILE))
    all_events.extend(extract_scratch_items(SCRATCH_FILE))

    if not all_events:
        print("\n  No upcoming catalysts found in STATUS.md / TEAM.md / SCRATCH.md")
        return 0

    # Deduplicate: same date + similar label (first 20 chars after stripping)
    seen = set()
    unique_events = []
    for e in all_events:
        # Normalize label for dedup: strip markdown, lowercase, first 20 chars
        norm = re.sub(r'[^a-z0-9 ]', '', e["label"][:40].lower()).strip()[:20]
        key = (e["date"].strftime("%Y-%m-%d"), norm)
        if key not in seen:
            seen.add(key)
            unique_events.append(e)

    # Add trading days
    for e in unique_events:
        e["td"] = trading_days_between(today, e["date"])
        e["calendar_days"] = (e["date"] - today).days

    # Sort by date
    unique_events.sort(key=lambda x: x["date"])

    # Filter: only show future events (up to 60 calendar days out) + today/overdue
    events = [e for e in unique_events if e["calendar_days"] >= -2 and e["calendar_days"] <= 60]

    # Display
    print(f"\n  {'':3} {'TD':>3}  {'Date':<12} {'Event':<55} {'Source':<12}")
    print(f"  {'-'*90}")

    current_week = None
    for e in events:
        # Week separator
        week = e["date"].isocalendar()[1]
        if current_week is not None and week != current_week:
            print()
        current_week = week

        emoji = priority_emoji(e["td"])
        td_str = f"{e['td']}TD" if e["td"] >= 0 else "NOW"
        date_str = e["date"].strftime("%b %d %a")
        print(f"  {emoji} {td_str:>4}  {date_str:<12} {e['label']:<55} {e['source']}")

    # Summary
    urgent = [e for e in events if e["td"] <= 1]
    this_week = [e for e in events if 0 < e["td"] <= 5]

    print(f"\n  {'='*72}")
    print(f"  {len(urgent)} events TODAY/TOMORROW | {len(this_week)} this week | {len(events)} total in window")

    if urgent:
        print(f"\n  \U0001f534 URGENT:")
        for e in urgent:
            print(f"     {e['date'].strftime('%b %d')}: {e['label']}")

    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
