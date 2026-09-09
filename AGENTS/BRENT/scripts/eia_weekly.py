#!/usr/bin/env python3
"""
BRENT EIA Weekly Petroleum Status Monitor

Two modes (auto-selects LIVE when the EIA key is available, else LOCAL):
  1. LIVE — pulls the EIA v2 API directly for the headline WPSR series, reusing
     FORGE/tools/market-data/fetch.py:eia_fetch() (key from the gitignored FORGE
     .env / EIA_API_KEY). Series IDs validated against known wk-6/12 prints on
     2026-06-22: commercial crude, SPR, Cushing, gasoline, distillate, util, and
     gasoline 4-wk YoY demand (−1.08% vs the published −1.1%). Default on WPSR days.
  2. LOCAL — parses the latest AGENTS/BRENT/demand_destruction/data/eia_YYYY-MM-DD.md
     (fallback when the key/FORGE module is unavailable, or forced with --local).

Key metrics tracked:
  - Commercial crude stocks (WoW change)
  - Cushing stocks (<20M = operational minimum / WTI dislocation = ROUTING Boundary #3)
  - SPR level
  - Gasoline stocks + 4-wk YoY product-supplied proxy (record only)
  - Distillate stocks
  - Refinery utilization (>95% = crack squeeze territory)

Usage:
  .venv/bin/python3 AGENTS/BRENT/scripts/eia_weekly.py           # auto (LIVE if key set)
  .venv/bin/python3 AGENTS/BRENT/scripts/eia_weekly.py --local   # force local-file parse
  .venv/bin/python3 AGENTS/BRENT/scripts/eia_weekly.py --live    # force live pull
"""

import os
import math
import csv
import re
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

BRENT_DIR = Path(__file__).resolve().parent.parent
EIA_DATA_DIR = BRENT_DIR / "demand_destruction" / "data"

# ---- LIVE EIA v2 access: reuse FORGE's tested eia_fetch (key from gitignored .env) ----
FORGE_MD = BRENT_DIR.parent.parent / "FORGE" / "tools" / "market-data"
try:
    sys.path.insert(0, str(FORGE_MD))
    import fetch as _forge  # eia_fetch() + EIA_API_KEY + .env loader
    HAVE_FORGE = True
except Exception:
    _forge = None
    HAVE_FORGE = False

# canonical metric -> (EIA v2 series_id, route, multiply-to-display-unit, compute_wow)
# All series IDs validated against known wk-6/12 prints on 2026-06-22.
EIA_SERIES = {
    "commercial_crude": ("WCESTUS1",              "petroleum/stoc/wstk", 0.001, True),   # k bbl -> M
    "spr":              ("WCSSTUS1",              "petroleum/stoc/wstk", 0.001, True),
    "cushing":          ("W_EPC0_SAX_YCUOK_MBBL", "petroleum/stoc/wstk", 0.001, True),
    "gasoline":         ("WGTSTUS1",              "petroleum/stoc/wstk", 0.001, True),
    "distillate":       ("WDISTUS1",              "petroleum/stoc/wstk", 0.001, True),
    "util":             ("WPULEUS3",              "petroleum/pnp/wiup",  1.0,   False),  # already %
}
# Finished motor gasoline product supplied (kbpd) — for the 4-wk YoY demand proxy (record only).
GAS_SUPPLIED_SERIES = ("WGFUPUS2", "petroleum/cons/wpsup")

# Thresholds
CUSHING_MIN = 20.0          # M bbl — operational minimum / WTI dislocation
CUSHING_WATCH = 25.0        # M bbl — approaching minimum
UTIL_SQUEEZE = 95.0         # % — crack squeeze territory
# The old SPR operational ladder and gasoline Phase-2 trigger are retired.
# Existing monitoring readers below retain observations, never revive those rules.


def parse_date(value):
    if not value:
        return None
    for fmt in ("%Y-%m-%d", "%B %d, %Y", "%b %d, %Y", "%A, %B %d, %Y"):
        try:
            return datetime.strptime(value.strip(), fmt).date()
        except (ValueError, AttributeError):
            pass
    return None


def find_latest_eia_file():
    """Latest dated numerical report; publication notices are not observations."""
    candidates = []
    for path in EIA_DATA_DIR.glob("eia_*.md"):
        metrics = extract_metrics(path.read_text())
        observed = parse_date(metrics.get("week_ending"))
        if observed and any(key in metrics for key in EIA_SERIES):
            candidates.append((observed, path.name, path))
    return max(candidates)[2] if candidates else None


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

    # September consolidated report: current/prior/WoW columns, never prose
    # mentions of older values. Modern report header is ISO-dated.
    modern = re.search(r"(?im)^# .*Week Ending (\d{4}-\d{2}-\d{2})\s*$", text)
    if modern:
        metrics = {"week_ending": modern.group(1)}
        released = re.search(r"\*\*Released:\*\*\s*(\d{4}-\d{2}-\d{2})", text)
        if released:
            metrics["report_date"] = released.group(1)
        labels = {"commercial crude (excl spr)": "commercial_crude", "cushing, ok": "cushing",
                  "spr": "spr", "total motor gasoline": "gasoline",
                  "distillate fuel oil": "distillate", "refinery utilization": "util"}
        for line in text.splitlines():
            if not line.startswith("|"):
                continue
            cells = [cell.replace("**", "").strip() for cell in line.strip("|").split("|")]
            if len(cells) < 4:
                continue
            key = labels.get(cells[0].lower())
            if key:
                unit = "%" if key == "util" else "M"
                current = re.match(r"([+−-]?[\d,.]+)" + unit, cells[1])
                if current:
                    metrics[key] = float(current.group(1).replace(",", "").replace("−", "-"))
                if key != "util":
                    wow = re.match(r"([+−-]?[\d,.]+)M", cells[3])
                    if wow:
                        metrics[key + "_wow"] = float(wow.group(1).replace(",", "").replace("−", "-"))
            if cells[0].lower() == "motor gasoline product supplied (4-wk avg)" and len(cells) >= 6:
                yoy = re.match(r"([+−-]?[\d.]+)%", cells[5])
                if yoy:
                    metrics["gas_yoy_latest"] = float(yoy.group(1).replace("−", "-"))
    observed = parse_date(metrics.get("week_ending"))
    if observed:
        metrics["week_ending"] = observed.isoformat()
        metrics["dates"] = {k: observed.isoformat() for k in metrics if isinstance(metrics[k], (int, float))}
    released = parse_date(metrics.get("report_date"))
    if released:
        metrics["report_date"] = released.isoformat()
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
    return "⚪", "UNKNOWN — no complete comparison" if val is None else "record only; retired BRT-08 trigger is not evaluated"


def status_for_spr(val):
    return "⚪", "UNKNOWN" if val is None else "level only; exact current contract/authority unresolved; no universal statutory floor inferred"


REQUIRED = tuple(EIA_SERIES) + tuple(k + "_wow" for k, v in EIA_SERIES.items() if v[3]) + ("gas_yoy_latest",)


def dated_values(rows):
    """Keep invalid/missing observations as holes; reject conflicting duplicates."""
    values = {}
    conflicts = set()
    for row in rows or []:
        when = parse_date(row.get("date"))
        if when is None:
            continue
        try:
            val = float(row["value"])
            if not math.isfinite(val):
                val = None
        except (ValueError, TypeError, KeyError):
            val = None
        if when in conflicts or (when in values and values[when] != val):
            conflicts.add(when)
            values[when] = None
        else:
            values[when] = val
    return values


def gas_comparison(values, when):
    current = [when - timedelta(weeks=i) for i in range(4)]
    prior = [d - timedelta(weeks=52) for d in current]
    if any(values.get(d) is None for d in current + prior):
        return None
    base = sum(values[d] for d in prior)
    return (sum(values[d] for d in current) / base - 1) * 100 if base > 0 else None


def fetch_live_metrics():
    """Retrieve per-metric dates and required comparisons; never fill holes."""
    if not HAVE_FORGE or not getattr(_forge, "EIA_API_KEY", ""):
        return None
    metrics = {"dates": {}, "errors": []}
    for key, (sid, route, mult, want_wow) in EIA_SERIES.items():
        try:
            values = dated_values(_forge.eia_fetch(sid, route=route, limit=2))
        except Exception as exc:
            metrics["errors"].append(f"{key}: {type(exc).__name__}")
            continue
        if not values:
            continue
        when = max(values)
        val = values[when]
        if val is None:
            continue
        metrics[key] = val * mult
        metrics["dates"][key] = when.isoformat()
        previous = values.get(when - timedelta(weeks=1))
        if want_wow and previous is not None:
            metrics[key + "_wow"] = (val - previous) * mult
            metrics["dates"][key + "_wow"] = when.isoformat()
    try:
        values = dated_values(_forge.eia_fetch(GAS_SUPPLIED_SERIES[0], route=GAS_SUPPLIED_SERIES[1], limit=60))
        if values:
            when = max(values)
            result = gas_comparison(values, when)
            if result is not None:
                metrics["gas_yoy_latest"] = result
                metrics["dates"]["gas_yoy_latest"] = when.isoformat()
    except Exception as exc:
        metrics["errors"].append(f"gas_yoy_latest: {type(exc).__name__}")
    dates = set(metrics["dates"].values())
    if not dates:
        return None
    if len(dates) == 1:
        metrics["week_ending"] = next(iter(dates))
    return metrics


def observation_budget():
    """Use the existing weekly EIA observation budget; do not change its level."""
    path = BRENT_DIR / "workbook/REGISTRY.tsv"
    rows = csv.DictReader([l for l in path.read_text().splitlines() if l and not l.startswith("#")], delimiter="\t")
    return int(next(r for r in rows if r["test_id"] == "CUSHING-20M")["max_stale_days"])


def coverage(metrics, today=None):
    today = today or date.today()
    issues = ["missing " + k for k in REQUIRED if metrics.get(k) is None]
    dates = metrics.get("dates", {})
    seen = set()
    for key in REQUIRED:
        if metrics.get(key) is None:
            continue
        when = parse_date(dates.get(key))
        if when is None:
            issues.append(key + ": observation date UNKNOWN")
        else:
            seen.add(when)
            if when > today:
                issues.append(key + ": future observation")
            elif (today - when).days > observation_budget():
                issues.append(key + ": STALE observation " + when.isoformat())
    if len(seen) > 1:
        issues.append("mixed observation weeks; no synchronized report")
    return issues


def main():
    now = datetime.now(timezone.utc)
    print(f"BRENT EIA Weekly Monitor — retrieved {now.isoformat()}")
    force_local, force_live = "--local" in sys.argv, "--live" in sys.argv
    if force_local and force_live:
        print("Choose --local or --live, not both")
        return 1
    metrics = None if force_local else fetch_live_metrics()
    kind = "API"
    source = "EIA v2 API; retrieval time is not release time"
    if metrics is None:
        if force_live:
            print("FINDINGS: --live unavailable or no valid dated observations; no local substitution")
            return 2
        latest = find_latest_eia_file()
        if latest is None:
            print("FINDINGS: no dated numerical local report available")
            return 2
        kind, source = "LOCAL", latest.name
        metrics = extract_metrics(latest.read_text())
    issues = coverage(metrics, today=now.date())
    print(f"Source: {kind} ({source})")
    print(f"Week ending: {metrics.get('week_ending', 'MIXED / UNKNOWN — see each metric')}")
    print(f"Released: {metrics.get('report_date', 'UNKNOWN — API observation dates below')}")
    print(f"Coverage: {'FINDINGS' if issues else 'COMPLETE dated observations'}")
    for key in REQUIRED:
        value = metrics.get(key)
        unit = '%' if key in ('util', 'gas_yoy_latest') else 'M bbl'
        shown = 'UNKNOWN' if value is None else f'{value:+.3f} {unit}'
        print(f"  {key}: {shown}; observed {metrics.get('dates', {}).get(key, 'UNKNOWN')}")
    print("Gasoline YoY: record only; retired BRT-08 trigger not evaluated; BRT-29 requires owner review.")
    print("SPR: level only; exact current contract/authority unresolved; no universal floor inferred.")
    cushing = metrics.get('cushing')
    when = parse_date(metrics.get('dates', {}).get('cushing'))
    eligible = when is not None and 0 <= (now.date() - when).days <= observation_budget()
    if cushing is None or not eligible:
        print("Cushing <20M: UNGRADED — absent or stale dated observation")
    else:
        print(f"Cushing <20M: {'BREACHED' if cushing < CUSHING_MIN else 'not breached'} on {when}; observation check only")
    util = metrics.get('util')
    util_date = parse_date(metrics.get('dates', {}).get('util'))
    if util is not None and util_date and 0 <= (now.date() - util_date).days <= observation_budget():
        print(f"Refinery utilization: {status_for_util(util)[1]} on {util_date}; observation check only")
    else:
        print("Refinery utilization: UNGRADED — absent or stale dated observation")
    for issue in issues + metrics.get('errors', []):
        print('  FINDINGS: ' + issue)
    return 2 if issues or metrics.get('errors') else 0


if __name__ == "__main__":
    sys.exit(main())
