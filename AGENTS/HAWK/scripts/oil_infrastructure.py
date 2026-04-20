#!/usr/bin/env python3
"""
HAWK Oil Infrastructure Monitor — Facility Status Tracker

Tracks status of key Gulf energy infrastructure (Fujairah, Ras Laffan,
ADCOP, Yanbu, etc.) and outputs operational status with repair timelines.

Usage:
  .venv/bin/python3 AGENTS/HAWK/scripts/oil_infrastructure.py
  .venv/bin/python3 AGENTS/HAWK/scripts/oil_infrastructure.py --save    # write to workbook
"""

import sys
import argparse
from datetime import datetime
from pathlib import Path

HAWK_DIR = Path(__file__).resolve().parent.parent
WORKBOOK = HAWK_DIR / "workbook"
WORKBOOK.mkdir(exist_ok=True)

# Facility registry
FACILITIES = [
    {
        "name": "Fujairah Terminal",
        "location": "UAE",
        "status": "DAMAGED",
        "capacity": "1.4M bpd export",
        "repair_timeline": "No timeline announced",
        "last_update": "2026-04-13",
        "priority": "🔴"
    },
    {
        "name": "Ras Laffan",
        "location": "Qatar",
        "status": "DAMAGED",
        "capacity": "LNG export hub",
        "repair_timeline": "3-5 year baseline",
        "last_update": "2026-04-13",
        "priority": "🔴"
    },
    {
        "name": "ADCOP Pipeline",
        "location": "UAE-Oman",
        "status": "DAMAGED",
        "capacity": "1.5M bpd Hormuz bypass",
        "repair_timeline": "No timeline announced",
        "last_update": "2026-04-13",
        "priority": "🔴"
    },
    {
        "name": "Yanbu",
        "location": "Saudi Arabia",
        "status": "OPERATIONAL",
        "capacity": "Red Sea export terminal",
        "repair_timeline": "N/A",
        "last_update": "2026-04-13",
        "priority": "🟢"
    },
    {
        "name": "Al Taweelah / EGA",
        "location": "UAE",
        "status": "DAMAGED",
        "capacity": "4% global aluminium",
        "repair_timeline": "No timeline announced",
        "last_update": "2026-04-13",
        "priority": "🔴"
    },
    {
        "name": "Kharg Island",
        "location": "Iran",
        "status": "OPERATIONAL",
        "capacity": "Primary Iran export terminal",
        "repair_timeline": "N/A",
        "last_update": "2026-04-13",
        "priority": "🟢"
    },
]

# Key signals to monitor
KEY_SIGNALS = [
    {"signal": "Mine clearance operations (Hormuz)", "status": "⏳ Not visible", "priority": "🔴"},
    {"signal": "Insurance reinstatement (Lloyd's/P&I)", "status": "⏳ No change", "priority": "🔴"},
    {"signal": "QatarEnergy restart timeline", "status": "⏳ No announcement", "priority": "🔴"},
    {"signal": "Fujairah structural assessment", "status": "⏳ Pending", "priority": "🔴"},
    {"signal": "ADCOP repair commencement", "status": "⏳ No timeline", "priority": "🟡"},
]


def get_status_emoji(status):
    """Return emoji for status."""
    return "🔴" if status == "DAMAGED" else "🟢" if status == "OPERATIONAL" else "🟡"


def save_facility_status():
    """Save facility status to FACILITY_STATUS.tsv."""
    tsv_path = WORKBOOK / "FACILITY_STATUS.tsv"
    today = datetime.now().strftime("%Y-%m-%d")
    
    if not tsv_path.exists():
        with open(tsv_path, "w") as f:
            f.write("date\tfacility\tlocation\tstatus\tcapacity\trepair_timeline\tlast_update\n")
    
    with open(tsv_path, "a") as f:
        for fac in FACILITIES:
            f.write(f"{today}\t{fac['name']}\t{fac['location']}\t{fac['status']}\t"
                   f"{fac['capacity']}\t{fac['repair_timeline']}\t{fac['last_update']}\n")


def save_infrastructure_log():
    """Append to INFRASTRUCTURE_LOG.md."""
    log_path = WORKBOOK / "INFRASTRUCTURE_LOG.md"
    today = datetime.now().strftime("%Y-%m-%d")
    
    with open(log_path, "a") as f:
        f.write(f"\n## {today}\n\n")
        f.write("**Facility Status:**\n\n")
        for fac in FACILITIES:
            emoji = get_status_emoji(fac['status'])
            f.write(f"- {emoji} **{fac['name']}** ({fac['location']}): {fac['status']}\n")
            f.write(f"  - Capacity: {fac['capacity']}\n")
            f.write(f"  - Repair: {fac['repair_timeline']}\n\n")


def main():
    parser = argparse.ArgumentParser(description="HAWK oil infrastructure monitor")
    parser.add_argument("--save", action="store_true", help="Save to workbook")
    args = parser.parse_args()
    
    now = datetime.now().strftime("%Y-%m-%d %H:%M ET")
    
    print(f"\n{'='*70}")
    print(f"  HAWK Infrastructure Monitor — {now}")
    print(f"{'='*70}")
    
    # Facility status table
    print(f"\n  FACILITY STATUS")
    print(f"  {'-'*66}")
    print(f"  {'Facility':<20} {'Location':<10} {'Status':<12} {'Capacity':<25}")
    print(f"  {'-'*66}")
    
    for fac in FACILITIES:
        emoji = get_status_emoji(fac['status'])
        name = fac['name'][:18] + ".." if len(fac['name']) > 20 else fac['name']
        cap = fac['capacity'][:23] + ".." if len(fac['capacity']) > 25 else fac['capacity']
        print(f"  {emoji} {name:<18} {fac['location']:<10} {fac['status']:<12} {cap}")
    
    # Repair timeline details
    print(f"\n  REPAIR TIMELINES")
    print(f"  {'-'*66}")
    
    damaged = [f for f in FACILITIES if f['status'] == 'DAMAGED']
    if damaged:
        for fac in damaged:
            print(f"  🔴 {fac['name']}")
            print(f"     Status: {fac['status']} | Last update: {fac['last_update']}")
            print(f"     Timeline: {fac['repair_timeline']}")
    else:
        print("  🟢 All facilities operational")
    
    # Key signals
    print(f"\n  KEY SIGNALS")
    print(f"  {'-'*66}")
    
    for sig in KEY_SIGNALS:
        print(f"  {sig['priority']} {sig['signal']:<40} {sig['status']}")
    
    # Summary stats
    total = len(FACILITIES)
    damaged_count = len([f for f in FACILITIES if f['status'] == 'DAMAGED'])
    operational_count = len([f for f in FACILITIES if f['status'] == 'OPERATIONAL'])
    
    print(f"\n  SUMMARY")
    print(f"  {'-'*66}")
    print(f"  Total facilities: {total}")
    print(f"  🔴 Damaged: {damaged_count} ({damaged_count/total*100:.0f}%)")
    print(f"  🟢 Operational: {operational_count} ({operational_count/total*100:.0f}%)")
    
    # Alerts
    print(f"\n  ALERTS")
    print(f"  {'-'*66}")
    
    alerts = []
    if damaged_count >= 3:
        alerts.append("🔴 Multiple facilities damaged — supply chain constrained")
    if any("Not visible" in s['status'] or "No change" in s['status'] for s in KEY_SIGNALS):
        alerts.append("🔴 No repair timeline updates — physical restart uncertain")
    
    if alerts:
        for alert in alerts:
            print(f"  {alert}")
    else:
        print("  ✅ No active alerts")
    
    # Save if requested
    if args.save:
        save_facility_status()
        save_infrastructure_log()
        print(f"\n  💾 Logged to workbook/FACILITY_STATUS.tsv and INFRASTRUCTURE_LOG.md")
    
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
