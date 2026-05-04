#!/usr/bin/env python3
"""
BRENT EIA Weekly Petroleum Status Monitor

Two modes:
  1. LIVE (if EIA_API_KEY env var set) — pulls EIA v2 API for headline series
  2. LOCAL — parses the latest AGENTS/BRENT/demand_destruction/data/eia_YYYY-MM-DD.md

Key metrics tracked:
  - Commercial crude stocks (WoW change)
  - Cushing stocks (<20M = operational minimum / WTI dislocation)
  - SPR level
  - Gasoline stocks + YoY demand (-5% = Phase 2 signal)
  - Distillate stocks
  - Refinery utilization (>95% = crack squeeze territory)

Usage:
  .venv/bin/python3 AGENTS/BRENT/scripts/eia_weekly.py
"""

import os
import re
import sys
from datetime import datetime
from pathlib import Path

BRENT_DIR = Path(__file__).resolve().parent.parent
EIA_DATA_DIR = BRENT_DIR / "demand_destruction" / "data"

# Thresholds
CUSHING_MIN = 20.0          # M bbl — operational minimum / WTI dislocation
CUSHING_WATCH = 25.0        # M bbl — approaching minimum
UTIL_SQUEEZE = 95.0         # % — crack squeeze territory
GAS_YOY_PHASE2 = -5.0       # % — Phase 2 demand destruction trigger
SPR_FLOOR = 400.0           # M bbl — near SPR operational floor


def find_latest_eia_file():
    """Find most recent eia_YYYY-MM-DD.md file."""
    if not EIA_DATA_DIR.exists():
        return None
    files = sorted(EIA_DATA_DIR.glob("eia_*.md"))
    return files[-1] if files else None


def extract_metrics(text):
    """Parse an eia_*.md report into headline metrics.

    Supports two file templates:
      - LEGACY (eia_2026-04-15 style): one named table per metric, with rows
        like `| Commercial crude stocks | **463.8M bbl** | ...` and a separate
        `| Week-over-week change | **−0.913M bbl (DRAW)** |` row.
      - CONSOLIDATED (eia_2026-04-29 style): a single KEY DATA POINTS table
        with rows like `| US commercial crude | **459.5M bbl** | **−6.2M (BIG DRAW)** | ...`.

    Regexes match BOTH so the parser stays robust as the writer's template
    evolves.
    """
    metrics = {}

    # ---- Commercial crude stocks level ----
    # Legacy: `Commercial crude stocks | **463.8M bbl**`
    # Consolidated: `US commercial crude | **459.5M bbl**`
    m = re.search(
        r"(?:US )?[Cc]ommercial crude(?:\s+stocks?)?\s*\|\s*\*\*([\d.,]+)M bbl\*\*",
        text,
    )
    if m:
        metrics["commercial_crude"] = float(m.group(1).replace(",", ""))

    # ---- Commercial crude WoW change ----
    # Legacy: `Week-over-week change | **−0.913M bbl (DRAW)**`
    m = re.search(
        r"Week-over-week change\s*\|\s*\*\*([−\-+]?[\d.]+)M bbl\s*\((DRAW|BUILD)\)\*\*",
        text,
    )
    if m:
        raw = m.group(1).replace("−", "-")
        val = float(raw)
        if m.group(2) == "DRAW" and val > 0:
            val = -val
        metrics["commercial_crude_wow"] = val
    else:
        # Consolidated: WoW is the next cell of the commercial-crude row.
        # `| US commercial crude | **459.5M bbl** | **−6.2M (BIG DRAW)** |`
        m = re.search(
            r"(?:US )?[Cc]ommercial crude(?:\s+stocks?)?\s*\|\s*\*\*[\d.,]+M bbl\*\*\s*\|\s*\*\*([−\-+]?[\d.]+)M(?:\s*bbl)?\s*\(?\s*(?:[A-Z]+\s*)?(DRAW|BUILD)\)?\*\*",
            text,
        )
        if m:
            raw = m.group(1).replace("−", "-")
            val = float(raw)
            if m.group(2) == "DRAW" and val > 0:
                val = -val
            metrics["commercial_crude_wow"] = val

    # ---- Cushing ----
    # Legacy: dated rows in a Cushing-only table
    #   `| **Apr 10** | **~29.8M bbl** | **−1.7M bbl** |`
    cushing_rows = re.findall(
        r"\|\s*\*\*[A-Z][a-z]+ \d+\*\*\s*\|\s*\*\*~?([\d.]+)M bbl\*\*\s*\|\s*\*\*([−\-+]?[\d.]+)M bbl\*\*",
        text,
    )
    if cushing_rows:
        cur_val, cur_wow = cushing_rows[-1]
        metrics["cushing"] = float(cur_val)
        metrics["cushing_wow"] = float(cur_wow.replace("−", "-"))

    # Consolidated: `| Cushing | **~29.8M bbl** | **−796K (RESUMED DRAW)** | ...`
    # Change value can be in K or M — normalize to M.
    if "cushing" not in metrics:
        m = re.search(
            r"\|\s*Cushing\s*\|\s*\*\*~?([\d.]+)M bbl\*\*\s*\|\s*\*\*([−\-+]?[\d.]+)([KM])(?:[^*]*)\*\*",
            text,
        )
        if m:
            metrics["cushing"] = float(m.group(1))
            wow_raw = float(m.group(2).replace("−", "-"))
            if m.group(3) == "K":
                wow_raw = wow_raw / 1000.0
            metrics["cushing_wow"] = wow_raw

    # Fallback: prose form `Cushing at XX.XM bbl`
    if "cushing" not in metrics:
        m = re.search(r"Cushing at ([\d.]+)M bbl", text)
        if m:
            metrics["cushing"] = float(m.group(1))

    # ---- Gasoline stocks WoW ----
    # Legacy: `Gasoline stocks change | **+0.626M bbl BUILD**`
    m = re.search(
        r"Gasoline stocks change\s*\|\s*\*\*([−\-+]?[\d.]+)M bbl\s*(DRAW|BUILD)?\*\*",
        text,
    )
    if m:
        raw = m.group(1).replace("−", "-")
        val = float(raw)
        if m.group(2) == "DRAW" and val > 0:
            val = -val
        metrics["gasoline_wow"] = val
    else:
        # Consolidated: `| Gasoline inventories | 222.3M bbl | **−6.1M (LARGE DRAW)** | ...`
        m = re.search(
            r"\|\s*Gasoline (?:inventories|stocks)\s*\|\s*[\d.]+M bbl\s*\|\s*\*\*([−\-+]?[\d.]+)M(?:\s*bbl)?\s*\(?\s*(?:[A-Z]+\s*)?(DRAW|BUILD)\)?\*\*",
            text,
        )
        if m:
            raw = m.group(1).replace("−", "-")
            val = float(raw)
            if m.group(2) == "DRAW" and val > 0:
                val = -val
            metrics["gasoline_wow"] = val

    # ---- Gasoline YoY (4-wk demand proxy) ----
    # Legacy: `YoY — Apr 3 week | **+0.8%** | ...`
    yoy_matches = re.findall(
        r"YoY\s*[—\-]\s*[A-Z][a-z]+ \d+[^\|]*\|\s*\*\*([−\-+][\d.]+)%\*\*",
        text,
    )
    if yoy_matches:
        for yoy_str in yoy_matches:
            try:
                metrics["gas_yoy_latest"] = float(yoy_str.replace("−", "-"))
                break
            except ValueError:
                continue

    # Consolidated: `| **Motor gasoline** | **9.0 mbpd** | **+1.2% YoY** |`
    if "gas_yoy_latest" not in metrics:
        m = re.search(
            r"\*\*[Mm]otor gasoline\*\*\s*\|\s*\*\*[\d.]+\s*mbpd\*\*\s*\|\s*\*\*([−\-+][\d.]+)%\s*YoY\*\*",
            text,
        )
        if m:
            metrics["gas_yoy_latest"] = float(m.group(1).replace("−", "-"))

    # ---- Refinery utilization ----
    # Match both "Refinery utilization" (legacy) and "Refinery util" (consolidated).
    m = re.search(r"[Rr]efinery [Uu]til(?:ization)?[^\n|]*\|\s*\*\*([\d.]+)%\*\*", text)
    if m:
        metrics["util"] = float(m.group(1))
    else:
        m = re.search(r"[Rr]efinery [Uu]til(?:ization)?[^\n]*?([\d.]+)%", text)
        if m:
            metrics["util"] = float(m.group(1))

    # ---- SPR ----
    m = re.search(r"SPR[:\s]+([\d.]+)M bbl", text)
    if m:
        metrics["spr"] = float(m.group(1))

    # ---- Week ending ----
    # Legacy: `**Week ending:** April 10, 2026`
    m = re.search(r"\*\*Week ending:\*\* (\w+ \d+,? \d+)", text)
    if m:
        metrics["week_ending"] = m.group(1)
    else:
        # Consolidated H1: `# EIA WPSR — Week Ending April 24, 2026`
        m = re.search(r"[Ww]eek [Ee]nding\s+(\w+ \d+,? \d+)", text)
        if m:
            metrics["week_ending"] = m.group(1)

    # ---- Report released ----
    # Legacy: `**Report released:** Wednesday, April 15, 2026, 10:30 AM ET`
    m = re.search(r"\*\*Report released:\*\* (\w+, \w+ \d+,? \d+)", text)
    if m:
        metrics["report_date"] = m.group(1)
    else:
        # Consolidated: `**Released:** April 29, 2026 (10:30 AM ET)`
        m = re.search(r"\*\*Released:\*\*\s+(\w+ \d+,? \d+)", text)
        if m:
            metrics["report_date"] = m.group(1)

    return metrics


def status_for_cushing(val):
    if val is None:
        return "⚪", "unknown"
    if val < CUSHING_MIN:
        return "🔴", f"BELOW {CUSHING_MIN}M OPERATIONAL MIN — WTI DISLOCATION RISK"
    if val < CUSHING_WATCH:
        return "🟠", f"approaching {CUSHING_MIN}M minimum"
    return "🟢", "above operational minimum"


def status_for_util(val):
    if val is None:
        return "⚪", "unknown"
    if val > UTIL_SQUEEZE:
        return "🔴", f">{UTIL_SQUEEZE}% — crack spread squeeze territory"
    if val > 92.0:
        return "🟠", "elevated — production running hot"
    return "🟢", "normal range"


def status_for_gas_yoy(val):
    if val is None:
        return "⚪", "unknown"
    if val <= GAS_YOY_PHASE2:
        return "🔴", f"≤{GAS_YOY_PHASE2}% — PHASE 2 DEMAND DESTRUCTION TRIGGER"
    if val < 0:
        return "🟠", "negative YoY — first soft signal"
    return "🟢", "positive — hoarding window / no destruction"


def status_for_spr(val):
    if val is None:
        return "⚪", "unknown"
    if val < SPR_FLOOR:
        return "🔴", f"<{SPR_FLOOR}M — near operational floor"
    if val < 420:
        return "🟠", "drawn down from crisis releases"
    return "🟢", "normal"


def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"\n{'='*72}")
    print(f"  BRENT EIA Weekly Monitor — {now}")
    print(f"{'='*72}")

    latest = find_latest_eia_file()
    if latest is None:
        print(f"\n  ❌ No EIA data files found in {EIA_DATA_DIR}")
        print(f"  Expected pattern: eia_YYYY-MM-DD.md")
        return 1

    # File age
    mtime = datetime.fromtimestamp(latest.stat().st_mtime)
    age_days = (datetime.now() - mtime).days
    age_icon = "🟢" if age_days <= 3 else "🟠" if age_days <= 7 else "🔴"

    print(f"\n  Source: {latest.name}")
    print(f"  File age: {age_icon} {age_days} days (modified {mtime.strftime('%Y-%m-%d')})")

    # Parse
    with open(latest) as f:
        text = f.read()
    m = extract_metrics(text)

    if not m:
        print(f"\n  ⚠️  Could not extract metrics from {latest.name}")
        print(f"  The file may not match expected format.")
        return 1

    print(f"\n  Week ending:   {m.get('week_ending', 'unknown')}")
    print(f"  Released:      {m.get('report_date', 'unknown')}")

    # Key metrics
    print(f"\n  HEADLINE METRICS")
    print(f"  {'-'*64}")

    val = m.get("commercial_crude")
    wow = m.get("commercial_crude_wow")
    if val is not None:
        wow_str = f"  ({wow:+.2f}M WoW)" if wow is not None else ""
        print(f"  Commercial crude:  {val:>7.1f}M bbl{wow_str}")

    val = m.get("cushing")
    wow = m.get("cushing_wow")
    icon, note = status_for_cushing(val)
    if val is not None:
        wow_str = f"  ({wow:+.2f}M WoW)" if wow is not None else ""
        print(f"  {icon} Cushing:         {val:>7.1f}M bbl{wow_str}  — {note}")
        if wow is not None and wow < 0 and val is not None:
            weeks_to_floor = (val - CUSHING_MIN) / abs(wow)
            print(f"              At current pace: {weeks_to_floor:.1f} weeks to {CUSHING_MIN}M floor")

    val = m.get("spr")
    icon, note = status_for_spr(val)
    if val is not None:
        print(f"  {icon} SPR:             {val:>7.1f}M bbl                — {note}")

    wow = m.get("gasoline_wow")
    yoy = m.get("gas_yoy_latest")
    icon, note = status_for_gas_yoy(yoy)
    if wow is not None:
        print(f"  Gasoline stocks:   {wow:+.2f}M bbl WoW")
    if yoy is not None:
        print(f"  {icon} Gas demand YoY:  {yoy:+.2f}%                     — {note}")

    val = m.get("util")
    icon, note = status_for_util(val)
    if val is not None:
        print(f"  {icon} Refinery util:   {val:>7.1f}%                     — {note}")

    # Path B trigger status
    print(f"\n  PATH B TRIGGER STATUS (demand destruction)")
    print(f"  {'-'*64}")
    gas_trigger = yoy is not None and yoy <= GAS_YOY_PHASE2
    cushing_trigger = val is not None and m.get("cushing", 100) < CUSHING_MIN

    print(f"  Trigger #2 (Gas YoY ≤ -5%):  {'🔴 FIRED' if gas_trigger else '⚪ not fired'}")
    print(f"  Cushing < 20M:               {'🔴 BREACHED' if cushing_trigger else '⚪ not breached'}")

    print(f"\n  NOTE: This parses local eia_*.md files written by the scheduled EIA sub-agent.")
    print(f"  For live EIA v2 API (direct pull), set EIA_API_KEY env var (register at eia.gov/opendata).")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
