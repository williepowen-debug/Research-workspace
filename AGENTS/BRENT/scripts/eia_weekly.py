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
  - Gasoline stocks + 4-wk YoY demand (-5% = Phase 2 Trigger #2)
  - Distillate stocks
  - Refinery utilization (>95% = crack squeeze territory)

Usage:
  .venv/bin/python3 AGENTS/BRENT/scripts/eia_weekly.py           # auto (LIVE if key set)
  .venv/bin/python3 AGENTS/BRENT/scripts/eia_weekly.py --local   # force local-file parse
  .venv/bin/python3 AGENTS/BRENT/scripts/eia_weekly.py --live    # force live pull
"""

import os
import re
import sys
from datetime import datetime
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
# Finished motor gasoline product supplied (kbpd) — for the 4-wk YoY demand proxy (Trigger #2).
GAS_SUPPLIED_SERIES = ("WGFUPUS2", "petroleum/cons/wpsup")

# Thresholds
CUSHING_MIN = 20.0          # M bbl — operational minimum / WTI dislocation
CUSHING_WATCH = 25.0        # M bbl — approaching minimum
UTIL_SQUEEZE = 95.0         # % — crack squeeze territory
GAS_YOY_PHASE2 = -5.0       # % — Phase 2 demand destruction trigger
SPR_FLOOR = None            # ⛔ RETIRED 2026-08-07 BY WILL RULING — F4 permanently-breached class.
#   ⚑ LABELLED 2026-08-07 (BRENT) — this and THESIS's 252.4M are TWO DIFFERENT OBJECTS, not a
#   conflict: 252.4M is the §6241 STATUTORY minimum; 400.0 is an operational watch line. The
#   147.6M gap was two questions wearing one word. Both are correct; both are now labelled.
#   ⚠️ AND THIS LINE IS CURRENTLY DECORATION: SPR is 304.8M, so 400.0 is PERMANENTLY BREACHED
#   and fires red at every boot — the same F4 disease Will retired `crack >$30` for on 7/31.
#   NOT retired unilaterally: this file's hardcoded levels are the WP3 registry-consumer
#   residual and that is Will's call. Flagged in THESIS §KEY THRESHOLDS. supersedes: none.


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
    """SPR readout — DESCRIPTIVE ONLY. No alert level. (Will ruling 2026-08-07.)

    ⛔ THE WHOLE OPERATIONAL ALERT LADDER IS RETIRED, NOT JUST THE 400.0 RED.
    Will ruled the 400.0M watch line out as F4 (permanently breached => alerts on nothing
    in either direction), same class as `crack >$30` and `VLCC >WS200`. Implementing that
    ruling exposed a SECOND hardcoded level one line below it — `val < 420` -> amber —
    which is the SAME OBJECT at a different number and is ALSO permanently breached
    (SPR 304.8M). Retiring only the red would have DEMOTED a permanent alert to a permanent
    amber and let me record the ruling as executed while the decoration survived.
    `[[finding_record_of_an_action_is_not_the_action]]`

    ⚑ I EXTENDED THE RULING BY ONE LEVEL AND FLAGGED IT rather than doing it silently:
    Will ruled on "the 400.0M row"; I am also retiring the 420 amber because it is the same
    permanently-breached watch under a different constant. Reversible in one line if Will
    disagrees — the levels are recorded in the retired registry row SPR-OPERATIONAL-400.

    WHAT SURVIVES: the LEVEL and the WoW change are still printed every boot. Retiring an
    alert is not retiring the observation. A real SPR tripwire = a NEW REGISTRATION with a
    level base-rated against the current regime. The §6241 STATUTORY floor (252.4M) is a
    DIFFERENT OBJECT and stays live in THESIS §KEY THRESHOLDS.
    """
    if val is None:
        return "⚪", "unknown"
    return "⚪", "level only — operational alert ladder RETIRED 2026-08-07 (F4); statutory floor 252.4M is separate and live"


def fetch_live_metrics():
    """Pull the headline WPSR series live from the EIA v2 API via FORGE's eia_fetch.

    Returns a metrics dict in the SAME shape as extract_metrics() (so main()'s
    print/status logic is identical), or None if live access is unavailable.
    The 'gasoline' series WoW maps to the printer's 'gasoline_wow'; the gasoline
    4-wk YoY DEMAND proxy ('gas_yoy_latest') is computed from product supplied.
    """
    if not HAVE_FORGE or not getattr(_forge, "EIA_API_KEY", ""):
        return None
    m = {}
    for key, (sid, route, mult, want_wow) in EIA_SERIES.items():
        rows = _forge.eia_fetch(sid, route=route, limit=2)
        if not rows or (isinstance(rows[0], dict) and "error" in rows[0]):
            continue
        vals = [float(r["value"]) for r in rows if r.get("value") is not None]
        if not vals:
            continue
        m[key] = vals[0] * mult
        if want_wow and len(vals) >= 2:
            m[f"{key}_wow"] = (vals[0] - vals[1]) * mult
        if key == "cushing":
            m["week_ending"] = rows[0]["date"]

    # gasoline 4-wk YoY demand (Trigger #2) from product-supplied, newest-first
    rows = _forge.eia_fetch(*GAS_SUPPLIED_SERIES, limit=60)
    gv = [float(r["value"]) for r in rows if r.get("value") is not None]
    if len(gv) >= 56:
        cur4, yago4 = sum(gv[0:4]) / 4, sum(gv[52:56]) / 4
        if yago4:
            m["gas_yoy_latest"] = (cur4 / yago4 - 1) * 100.0

    if not m:
        return None
    m["report_date"] = "LIVE pull (EIA v2 API)"
    return m


def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"\n{'='*72}")
    print(f"  BRENT EIA Weekly Monitor — {now}")
    print(f"{'='*72}")

    force_local = "--local" in sys.argv
    force_live = "--live" in sys.argv

    m = None
    source = ""
    if force_live or not force_local:
        m = fetch_live_metrics()
        if m:
            source = "🟢 LIVE (EIA v2 API)"
        elif force_live:
            print(f"\n  ❌ --live requested but EIA key / FORGE module unavailable.")
            return 1

    if not m:
        latest = find_latest_eia_file()
        if latest is None:
            print(f"\n  ❌ No live EIA access and no data files in {EIA_DATA_DIR}")
            print(f"  Set EIA_API_KEY in FORGE/.env for live, or add an eia_YYYY-MM-DD.md.")
            return 1
        mtime = datetime.fromtimestamp(latest.stat().st_mtime)
        age_days = (datetime.now() - mtime).days
        age_icon = "🟢" if age_days <= 3 else "🟠" if age_days <= 7 else "🔴"
        source = f"{age_icon} LOCAL ({latest.name}, {age_days}d old)"
        with open(latest) as f:
            m = extract_metrics(f.read())
        if not m:
            print(f"\n  ⚠️  Could not extract metrics from {latest.name} (format mismatch).")
            return 1

    print(f"\n  Source: {source}")
    print(f"  Week ending:   {m.get('week_ending', 'unknown')}")
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
        print(f"  {icon} Cushing:         {val:>7.2f}M bbl{wow_str}  — {note}")
        if wow is not None and wow < 0 and val is not None:
            weeks_to_floor = (val - CUSHING_MIN) / abs(wow)
            print(f"              At current pace: {weeks_to_floor:.1f} weeks to {CUSHING_MIN}M floor")

    val = m.get("spr")
    wow = m.get("spr_wow")
    icon, note = status_for_spr(val)
    if val is not None:
        wow_str = f"  ({wow:+.2f}M WoW)" if wow is not None else ""
        print(f"  {icon} SPR:             {val:>7.1f}M bbl{wow_str}  — {note}")

    val = m.get("distillate")
    wow = m.get("distillate_wow")
    if val is not None:
        wow_str = f"  ({wow:+.2f}M WoW)" if wow is not None else ""
        print(f"  Distillate:        {val:>7.1f}M bbl{wow_str}")

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

    # ⛔⛔ FIXED 2026-09-07 (CODEX review, Will-approved). THIS LINE READ:
    #     cushing_trigger = val is not None and m.get("cushing", 100) < CUSHING_MIN
    # `val` is REASSIGNED down this whole print block and holds m.get("util") by the time it
    # reaches here (line ~429). So the Cushing trigger was gated on REFINERY UTILIZATION: if
    # util was missing, cushing_trigger went False NO MATTER WHAT CUSHING DID, and the board
    # printed "⚪ not breached" over a real breach.
    # ⚠️ SEVERITY: Cushing <20M is not decorative — it is the registered CUSHING-20M threshold
    # that RE-ACTIVATES Routing Boundary #3 (WALTER IMMEDIATE -> LIQUID/HENRY/RED). A live
    # routing trigger was suppressible by an unrelated absent field.
    # ★ WHY IT SURVIVED: `val is not None` LOOKS like the right guard and reads as deliberate
    # care. Nothing about the line is syntactically odd; only the BINDING is wrong, and a
    # reused loop-style variable makes the wrong binding invisible at the point of use.
    # [[finding_guard_pointed_at_another_desks_surface_inherits_its_workflow]] (same class:
    # a guard that names the wrong referent), [[finding_silent_blank_evades_review]].
    cushing_val = m.get("cushing")
    cushing_trigger = cushing_val is not None and cushing_val < CUSHING_MIN

    print(f"  Trigger #2 (Gas YoY ≤ -5%):  {'🔴 FIRED' if gas_trigger else '⚪ not fired'}")
    if cushing_val is None:
        # Fail LOUD. The old default of 100 made a MISSING reading indistinguishable from a
        # comfortable one — "not breached" is a claim, and we cannot make it without the datum.
        print(f"  Cushing < 20M:               ⚪ UNGRADED — no Cushing reading in this pull. "
              f"NOT a 'not breached': the datum is absent, so no verdict exists.")
    else:
        print(f"  Cushing < 20M:               {'🔴 BREACHED' if cushing_trigger else '⚪ not breached'}")

    if source.startswith("🟢"):
        print(f"\n  NOTE: LIVE pull via EIA v2 API (FORGE eia_fetch). Cross-check Cushing vs the FORGE dashboard.")
    else:
        print(f"  NOTE: LOCAL parse. Live needs EIA_API_KEY in FORGE/.env (then drop --local).")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
