#!/usr/bin/env python3
"""
PROME Market Stress Dashboard — Layer 3
Pulls live data, classifies against thresholds, outputs color-coded stress view.

Usage:
  python3 dashboard.py                # Full dashboard
  python3 dashboard.py --tier 1       # Decision drivers only
  python3 dashboard.py --agent LABOR  # Single agent view
  python3 dashboard.py --quiet        # Breaches only (red items)
  python3 dashboard.py --json         # JSON output
  python3 dashboard.py --compact      # One-line format (good for Telegram)

Exit codes:
  Normal/compact/json successful output returns 0, even when red zones exist.
  --cron/--notify preserve alert semantics: 2 = new red, 1 = existing red, 0 = no red.
"""

# Venv self-heal (2026-07-30, TERRY flag): root CLAUDE.md documents bare
# `python3` invocation, but yfinance lives in .venv — and fetch.py imports it
# LAZILY inside price_fetch/price_history, so caller-side import guards never
# fire. Re-exec under the venv interpreter when available; exit 2 with the fix
# printed when it is not. Never a raw traceback a caller could mistake for data.
import os as _os, sys as _sys, pathlib as _pl
_VENV_PY = _pl.Path(__file__).resolve().parents[3] / ".venv" / "bin" / "python3"
if _os.environ.get("MKTDATA_REEXEC") != "1" and _VENV_PY.exists() \
        and _pl.Path(_sys.prefix).resolve() != _VENV_PY.parents[1].resolve():
    # NB: compare sys.prefix to the venv ROOT — .venv/bin/python3 is a SYMLINK
    # to the base interpreter, so resolved-executable comparison always matches
    # and silently skips the re-exec (caught live on first test, 2026-07-30).
    _os.environ["MKTDATA_REEXEC"] = "1"
    _os.execv(str(_VENV_PY), [str(_VENV_PY)] + _sys.argv)
elif not _VENV_PY.exists():
    try:
        import yfinance  # noqa: F401 — probe only
    except ImportError:
        _sys.stderr.write(
            "FATAL: yfinance unavailable and no venv found at %s\n"
            "Fix: python3 -m venv .venv && .venv/bin/pip install yfinance pandas\n" % _VENV_PY)
        _sys.exit(2)

import argparse
import datetime
import json
import os
import sys
import time
import urllib.request
from pathlib import Path

from config import SERIES, classify, get_emoji, get_tier, get_agent, format_value
from fetch import fred_fetch, price_fetch, eia_fetch

# ---------------------------------------------------------------------------
# State tracking (Segment 3)
# ---------------------------------------------------------------------------

STATE_FILE = Path(__file__).parent / ".cache" / "last_run.json"
LOG_FILE = Path(__file__).parent / ".cache" / "dashboard_log.jsonl"

# De-hardcoded 2026-06-27 (token was exposed in git history → rotate via BotFather).
# send_telegram() is DISABLED in main(); if re-enabling, put the rotated token in a
# gitignored .env and export it. Read from env so the literal never re-enters this tracked file.
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "8463631023")


def load_last_state():
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except Exception as e:
            # A corrupt state file made --cron print nothing — byte-identical to
            # a quiet run (SFG sweep 8/17). Still fail-safe to {} (transitions
            # re-baseline), but say so on stderr per CHECK_STANDARD §8 rule ⑤.
            print(f"⚠️ dashboard: last_run.json unreadable ({e}) — transition "
                  f"baseline RESET; this run's zones are all 'new'", file=sys.stderr)
    return {}


def save_state(state):
    STATE_FILE.parent.mkdir(exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2))


# ---------------------------------------------------------------------------
# Data fetching
# ---------------------------------------------------------------------------

def fetch_all(series_list):
    """Fetch current values for all series. Returns list of result dicts."""
    results = []

    # Batch price tickers
    price_tickers = [s["id"] for s in series_list if s["source"] == "price"]
    price_data = {}
    if price_tickers:
        price_data = price_fetch(price_tickers)

    for s in series_list:
        entry = {
            "name": s["name"],
            "agent": s["agent"],
            "tier": s["tier"],
            "direction": s["direction"],
            "notes": s.get("notes", ""),
            "value": None,
            "zone": "unknown",
            "emoji": "⚪",
            "date": None,
            "prev": None,
            "change": None,
            "shadow": None,
        }

        if s["source"] == "price":
            pd = price_data.get(s["id"], {})
            if "error" not in pd:
                entry["value"] = pd.get("price")
                entry["prev"] = pd.get("prev")
                # fetch.py returns change_pct (a percent) + asof, never "change" —
                # reading pd.get("change") left the Δ column silently None on every
                # run (SFG sweep 8/17). Compute the absolute delta to match the
                # FRED/EIA branches' semantics; asof stamps the As-of column.
                entry["date"] = pd.get("asof")
                if entry["value"] is not None and entry["prev"] is not None:
                    entry["change"] = round(entry["value"] - entry["prev"], 4)
            else:
                entry["error"] = pd.get("error", "fetch failed")

        elif s["source"] == "fred":
            obs = fred_fetch(s["id"], limit=2)
            mult = s.get("multiply", 1)
            if obs and "error" not in obs[0]:
                entry["value"] = float(obs[0]["value"]) * mult
                entry["date"] = obs[0]["date"]
                if len(obs) > 1 and "error" not in obs[1]:
                    entry["prev"] = float(obs[1]["value"]) * mult
                    entry["change"] = entry["value"] - entry["prev"]

        elif s["source"] == "fred_spread":
            # Spread = series[0] - series[1]
            id_a, id_b = s["id"][0], s["id"][1]
            obs_a = fred_fetch(id_a, limit=2)
            obs_b = fred_fetch(id_b, limit=2)
            if obs_a and obs_b and "error" not in obs_a[0] and "error" not in obs_b[0]:
                val_a = float(obs_a[0]["value"])
                val_b = float(obs_b[0]["value"])
                entry["value"] = round(val_a - val_b, 4)
                entry["date"] = obs_a[0]["date"]
                if len(obs_a) > 1 and len(obs_b) > 1 and "error" not in obs_a[1] and "error" not in obs_b[1]:
                    prev_a = float(obs_a[1]["value"])
                    prev_b = float(obs_b[1]["value"])
                    entry["prev"] = round(prev_a - prev_b, 4)
                    entry["change"] = round(entry["value"] - entry["prev"], 4)

        elif s["source"] == "eia":
            obs = eia_fetch(s["id"], route=s.get("eia_route", "petroleum/stoc/wstk"), limit=2)
            mult = s.get("multiply", 1)
            if obs and "error" not in obs[0]:
                entry["value"] = float(obs[0]["value"]) * mult
                entry["date"] = obs[0]["date"]
                if len(obs) > 1 and "error" not in obs[1]:
                    entry["prev"] = float(obs[1]["value"]) * mult
                    entry["change"] = entry["value"] - entry["prev"]
            elif obs:
                entry["error"] = obs[0].get("error", "fetch failed")

        # Classify
        if entry["value"] is not None:
            entry["zone"] = classify(entry["value"], s)
            entry["emoji"] = get_emoji(entry["zone"])
            entry["formatted"] = format_value(entry["value"], s)
        else:
            entry["formatted"] = "N/A"

        # Shadow adjustment (claims)
        shadow = s.get("shadow_adj")
        if shadow and entry["value"] is not None:
            entry["shadow"] = {
                "label": shadow["label"],
                "value": entry["value"] + shadow["add"],
                "formatted": f"{entry['value'] + shadow['add']:,.0f}",
            }

        results.append(entry)

    return results


# ---------------------------------------------------------------------------
# Display
# ---------------------------------------------------------------------------

BOX_H = "─"
BOX_V = "│"
BOX_TL = "┌"
BOX_TR = "┐"
BOX_BL = "└"
BOX_BR = "┘"
BOX_ML = "├"
BOX_MR = "┤"
BOX_MC = "┼"
BOX_TM = "┬"
BOX_BM = "┴"


def hr(widths, left, mid, right, fill=BOX_H):
    parts = [fill * w for w in widths]
    return left + mid.join(parts) + right


def row(cells, widths):
    parts = []
    for c, w in zip(cells, widths):
        parts.append(f" {c:<{w-2}} ")
    return BOX_V + BOX_V.join(parts) + BOX_V


def _date_stamp(entry):
    """Format an as-of date stamp for FRED-sourced entries.

    Returns short MM/DD label if entry has a date (FRED observation date);
    empty string for yfinance-sourced entries (which are intraday-live).

    Surfaces FRED's T+1 publication lag in user-facing output so agents
    don't propagate stale-data-as-live. Per citation convention in
    FORGE/tools/market-data/README.md § Citation Convention.
    """
    if not entry.get("date"):
        return ""
    try:
        obs = datetime.date.fromisoformat(entry["date"])
        return f"[{obs.month}/{obs.day}]"
    except (ValueError, TypeError):
        return f"[{entry['date']}]"


def stress_score(results):
    """Weighted stress: Tier 1 reds = 2pts, Tier 2 reds = 1pt."""
    score = 0
    for r in results:
        if r["zone"] == "red":
            score += 2 if r["tier"] == 1 else 1
    return score


def stress_label(results):
    score = stress_score(results)
    if score >= 6:
        return f"🔴 CRITICAL (score {score})"
    elif score >= 4:
        return f"🟠 ELEVATED (score {score})"
    elif score >= 2:
        return f"🟡 WATCH (score {score})"
    return f"🟢 CALM (score {score})"


def print_table(results, title, transitions=None):
    """Print a formatted table for a set of results."""
    if not results:
        return

    print(f"\n  {title}")

    widths = [18, 20, 8, 12, 10]
    print(f"  {hr(widths, BOX_TL, BOX_TM, BOX_TR)}")
    print(f"  {row(['Series', 'Value', 'As-of', 'Zone', 'Agent'], widths)}")
    print(f"  {hr(widths, BOX_ML, BOX_MC, BOX_MR)}")

    for r in results:
        zone_str = f"{r['emoji']} {r['zone']}"

        # Add transition marker
        trans = ""
        if transitions and r["name"] in transitions:
            old, new = transitions[r["name"]]
            trans = f" ({get_emoji(old)}→{get_emoji(new)})"

        change_str = ""
        if r.get("change") is not None:
            sign = "+" if r["change"] >= 0 else ""
            if abs(r["change"]) > 100:
                change_str = f" ({sign}{r['change']:,.0f})"
            else:
                change_str = f" ({sign}{r['change']:.2f})"

        val_str = f"{r['formatted']}{change_str}"
        date_str = _date_stamp(r)

        print(f"  {row([r['name'], val_str, date_str, zone_str + trans, r['agent']], widths)}")

        # Shadow adjustment line
        if r.get("shadow"):
            sh = r["shadow"]
            print(f"  {row([f'  ({sh['label']})', sh['formatted'], '', ''], widths)}")

    print(f"  {hr(widths, BOX_BL, BOX_BM, BOX_BR)}")


def print_compact(results, transitions=None):
    """One-line-per-series format for Telegram."""
    for r in results:
        trans = ""
        if transitions and r["name"] in transitions:
            old, new = transitions[r["name"]]
            trans = f" ← was {get_emoji(old)}"
        date_str = _date_stamp(r)
        date_part = f" {date_str}" if date_str else ""
        print(f"{r['emoji']} {r['name']}: {r['formatted']}{date_part}{trans}  [{r['agent']}]")
        if r.get("shadow"):
            print(f"   ({r['shadow']['label']}: {r['shadow']['formatted']})")


def print_dashboard(results, transitions=None):
    """Full dashboard display."""
    ts = time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())

    print()
    print("  ══════════════════════════════════════════════════════════")
    print("   PROME Market Stress Dashboard")
    print(f"   {ts}")
    print("  ══════════════════════════════════════════════════════════")

    t1 = [r for r in results if r["tier"] == 1]
    t2 = [r for r in results if r["tier"] == 2]

    if t1:
        print_table(t1, "TIER 1 — DECISION DRIVERS", transitions)
    if t2:
        print_table(t2, "TIER 2 — POSITION MONITORING", transitions)

    # Summary
    reds = sum(1 for r in results if r["zone"] == "red")
    yellows = sum(1 for r in results if r["zone"] == "yellow")
    greens = sum(1 for r in results if r["zone"] == "green")

    print(f"\n  SUMMARY: {reds}🔴  {yellows}🟡  {greens}🟢  │  {stress_label(results)}")

    # Transitions
    if transitions:
        print(f"\n  ZONE CHANGES:")
        for name, (old, new) in transitions.items():
            print(f"    {get_emoji(old)}→{get_emoji(new)}  {name}")

    print()


# ---------------------------------------------------------------------------
# Transition detection
# ---------------------------------------------------------------------------

def detect_transitions(results, last_state):
    """Compare current zones to last run. Returns dict of {name: (old_zone, new_zone)}.
    
    Supports hysteresis: indicators with a 'hysteresis' config in SERIES require
    the value to cross a buffer beyond the threshold before triggering a zone change.
    This prevents alert spam when values oscillate near boundaries.
    """
    transitions = {}
    for r in results:
        name = r["name"]
        old_zone = last_state.get(name, {}).get("zone")
        if old_zone and old_zone != r["zone"]:
            # Check if this series has hysteresis configured
            series_def = next((s for s in SERIES if s["name"] == name), None)
            if series_def and "hysteresis" in series_def and r["value"] is not None:
                buf = series_def["hysteresis"]
                old_value = last_state.get(name, {}).get("value")
                if old_value is not None:
                    diff = abs(r["value"] - old_value)
                    if diff < buf:
                        # Value hasn't moved enough past boundary — suppress transition
                        # Keep the OLD zone in state to prevent drift
                        r["zone"] = old_zone
                        r["emoji"] = get_emoji(old_zone)
                        continue
            transitions[name] = (old_zone, r["zone"])
    return transitions


def build_state(results):
    """Build state dict from results for persistence."""
    return {
        r["name"]: {
            "zone": r["zone"],
            "value": r["value"],
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }
        for r in results
    }


# ---------------------------------------------------------------------------
# Quiet window
# ---------------------------------------------------------------------------

def in_quiet_window():
    """Returns True if current time is 11 PM – 8 AM ET (Will's skip window)."""
    import zoneinfo
    et = datetime.datetime.now(zoneinfo.ZoneInfo("America/New_York"))
    return et.hour >= 23 or et.hour < 8


def is_market_hours():
    """Returns True during US market hours (9:30 AM – 4 PM ET, Mon-Fri)."""
    import zoneinfo
    et = datetime.datetime.now(zoneinfo.ZoneInfo("America/New_York"))
    if et.weekday() >= 5:  # Sat/Sun
        return False
    t = et.hour * 60 + et.minute
    return 570 <= t <= 960  # 9:30=570, 16:00=960


# ---------------------------------------------------------------------------
# Telegram notification
# ---------------------------------------------------------------------------

def send_telegram(message):
    """Send a message to Will via Telegram."""
    try:
        payload = json.dumps({
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message,
            "parse_mode": "Markdown",
        }).encode()
        req = urllib.request.Request(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        urllib.request.urlopen(req, timeout=10)
        return True
    except Exception as e:
        print(f"[Telegram] Failed: {e}", file=sys.stderr)
        return False


def notify_transitions(results, transitions):
    """Build and send a Telegram alert for zone transitions.
    
    DISABLED: Telegram notifications turned off to reduce API costs.
    Re-enable by uncommenting the send_telegram() call below.
    """
    return  # Notifications disabled — 2026-04-15
    
    if not transitions:
        return

    lines = ["🚨 *PROME Zone Change*\n"]
    for name, (old, new) in transitions.items():
        r = next((x for x in results if x["name"] == name), None)
        val = r["formatted"] if r else "?"
        lines.append(f"{get_emoji(old)}→{get_emoji(new)}  *{name}*: {val}")

    reds = sum(1 for r in results if r["zone"] == "red")
    yellows = sum(1 for r in results if r["zone"] == "yellow")
    greens = sum(1 for r in results if r["zone"] == "green")
    lines.append(f"\n_{reds}🔴 {yellows}🟡 {greens}🟢_")

    # send_telegram("\n".join(lines))  # DISABLED


# ---------------------------------------------------------------------------
# Run log
# ---------------------------------------------------------------------------

def append_log(results, transitions):
    """Append a summary line to the JSONL log."""
    LOG_FILE.parent.mkdir(exist_ok=True)
    entry = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "values": {r["name"]: r["value"] for r in results},
        "zones": {r["name"]: r["zone"] for r in results},
        "transitions": {k: list(v) for k, v in transitions.items()} if transitions else {},
        "summary": {
            "red": sum(1 for r in results if r["zone"] == "red"),
            "yellow": sum(1 for r in results if r["zone"] == "yellow"),
            "green": sum(1 for r in results if r["zone"] == "green"),
        },
    }
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry, default=str) + "\n")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="PROME Market Stress Dashboard")
    parser.add_argument("--tier", type=int, choices=[1, 2], help="Show only this tier")
    parser.add_argument("--agent", type=str, help="Show only this agent's series")
    parser.add_argument("--quiet", action="store_true", help="Show red items only")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    parser.add_argument("--compact", action="store_true", help="One-line format (Telegram)")
    parser.add_argument("--no-save", action="store_true", help="Don't save state (dry run)")
    parser.add_argument("--notify", action="store_true", help="Send Telegram alert on zone transitions")
    parser.add_argument("--cron", action="store_true", help="Cron mode: log + notify on transitions, no stdout unless changes")

    args = parser.parse_args()

    # Select series
    if args.agent:
        series = get_agent(args.agent)
        if not series:
            print(f"No series found for agent '{args.agent}'")
            sys.exit(1)
    elif args.tier:
        series = get_tier(args.tier)
    else:
        series = SERIES

    # Fetch
    results = fetch_all(series)

    # Filter quiet mode
    if args.quiet:
        results = [r for r in results if r["zone"] == "red"]

    # Transitions
    last_state = load_last_state()
    transitions = detect_transitions(results, last_state)

    # Save state
    if not args.no_save:
        full_results = fetch_all(SERIES) if (args.tier or args.agent) else results
        save_state(build_state(full_results))

    # Always log (unless dry run)
    if not args.no_save:
        append_log(results, transitions)

    # Notifications
    if args.notify or args.cron:
        if transitions and not in_quiet_window():
            notify_transitions(results, transitions)
        elif transitions and in_quiet_window():
            print("[quiet window] Suppressed notification", file=sys.stderr)

    # Output
    if args.cron:
        # Cron mode: silent unless transitions
        if transitions:
            print_compact(results, transitions)
    elif args.json:
        output = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "results": results,
            "transitions": transitions,
            "summary": {
                "red": sum(1 for r in results if r["zone"] == "red"),
                "yellow": sum(1 for r in results if r["zone"] == "yellow"),
                "green": sum(1 for r in results if r["zone"] == "green"),
            },
        }
        print(json.dumps(output, indent=2, default=str))
    elif args.compact:
        print_compact(results, transitions)
    else:
        print_dashboard(results, transitions)

    # Exit codes:
    # - Human/data modes should return 0 after successful output; red zones are data, not command failure.
    # - Cron/notify modes keep alert semantics for automation: 2 = new reds, 1 = existing reds, 0 = no reds.
    if args.cron or args.notify:
        new_reds = any(new == "red" for _, new in transitions.values())
        any_reds = any(r["zone"] == "red" for r in results)
        if new_reds:
            sys.exit(2)
        elif any_reds:
            sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
