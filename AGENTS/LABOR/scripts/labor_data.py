#!/usr/bin/env python3
"""
LABOR Domain Data Sweep

Pulls the LABOR-domain FRED series via the shared market-data tool
(FORGE/tools/market-data/fetch.py) and prints a dashboard with threshold
flags wired to STATUS.md KEY THRESHOLDS. Self-contained under AGENTS/LABOR/;
no shared-file edits required (fetch.py accepts arbitrary FRED series).

Usage:
  .venv/bin/python3 AGENTS/LABOR/scripts/labor_data.py
  .venv/bin/python3 AGENTS/LABOR/scripts/labor_data.py --verbose   # show history rows
  .venv/bin/python3 AGENTS/LABOR/scripts/labor_data.py --periods 6 # deeper history

Exit code: 0 normally, 2 if any 🔴 threshold flag fired (so boot.py can surface).
"""

import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
LABOR_DIR = SCRIPTS_DIR.parent
WORKSPACE = LABOR_DIR.parent.parent  # Research-workspace/
VENV_PYTHON = WORKSPACE / ".venv" / "bin" / "python3"
FETCH = WORKSPACE / "FORGE" / "tools" / "market-data" / "fetch.py"

# series_id, label, kind, source_tag
#   kind: "claims" (thousands, K)  | "rate" (%)  | "level_mom" (thousands, show MoM Δ)
LABOR_SERIES = [
    ("ICSA",      "Initial Claims (wkly)",       "claims",    "DOL"),
    ("IC4WSA",    "Initial Claims 4-wk MA",      "claims",    "DOL"),
    ("CCSA",      "Continuing Claims (1wk lag)",  "claims",    "DOL"),
    ("PAYEMS",    "NFP total (MoM Δ)",            "level_mom", "BLS"),
    ("UNRATE",    "U-3 unemployment",             "rate",      "BLS"),
    ("U6RATE",    "U-6 underemployment",          "rate",      "BLS"),
    ("CIVPART",   "Labor force participation",    "rate",      "BLS"),
    ("JTSJOL",    "JOLTS openings (MoM Δ)",       "level_mom", "BLS"),
    ("JTSHIL",    "JOLTS hires (MoM Δ)",          "level_mom", "BLS"),
    ("JTSQUL",    "JOLTS quits (MoM Δ)",          "level_mom", "BLS"),
    ("JTSLDL",    "JOLTS layoffs/disch (MoM Δ)",  "level_mom", "BLS"),
    ("TEMPHELPS", "Temp help svcs (MoM Δ)",       "level_mom", "BLS"),
]


def fetch_series(series_id, periods=4):
    """Call shared fetch.py in --json mode. Returns list of (date, float|None) newest-first."""
    try:
        result = subprocess.run(
            [str(VENV_PYTHON), str(FETCH), "fred", series_id, "--periods", str(periods), "--json"],
            capture_output=True, text=True, timeout=40, cwd=str(WORKSPACE),
        )
        if result.returncode != 0:
            return None, f"fetch.py exit {result.returncode}: {result.stderr.strip()[:120]}"
        data = json.loads(result.stdout)
        obs = data.get("observations", [])
        out = []
        for o in obs:
            try:
                out.append((o["date"], float(o["value"])))
            except (ValueError, KeyError):
                out.append((o.get("date", "?"), None))
        return out, None
    except subprocess.TimeoutExpired:
        return None, "timeout"
    except (json.JSONDecodeError, Exception) as e:  # noqa: BLE001
        return None, f"{type(e).__name__}: {e}"


def fmt_value(kind, val):
    if val is None:
        return "n/a"
    if kind == "rate":
        return f"{val:.1f}%"
    # claims + level series are in thousands in FRED
    return f"{val:,.0f}K"


def assess(series_id, kind, obs):
    """Return (display_str, flag) where flag in {'', '🟢', '🟠', '🔴', '🔴🔴'}."""
    if not obs or obs[0][1] is None:
        return "n/a", "⚠️"
    date, val = obs[0]
    prev = obs[1][1] if len(obs) > 1 and obs[1][1] is not None else None

    disp = fmt_value(kind, val)
    flag = ""

    if kind == "level_mom" and prev is not None:
        mom = val - prev
        disp = f"{val:,.0f}K  (MoM {mom:+,.0f}K)"

    # --- threshold logic wired to STATUS KEY THRESHOLDS ---
    if series_id in ("ICSA", "IC4WSA"):
        # FRED claims are in actual persons (e.g. 225000), not thousands
        if val >= 300_000:
            flag = "🔴🔴"  # all ORANGE banks escalate
        elif val >= 250_000:
            flag = "🔴"   # consumer conversion accelerates
        elif val >= 230_000:
            flag = "🟠"   # drift watch
        else:
            flag = "🟢"
        disp = f"{val/1000:,.1f}K"
        if prev is not None:
            disp += f"  (WoW {(val-prev)/1000:+,.1f}K)"
    elif series_id == "CCSA":
        disp = f"{val/1000:,.0f}K"
        flag = "🟢" if val < 1_900_000 else "🟠"
    elif series_id == "UNRATE":
        if val >= 5.0:
            flag = "🔴"   # structural bid break
        elif val >= 4.7:
            flag = "🟠"
        else:
            flag = "🟢"
    elif series_id == "PAYEMS" and prev is not None:
        mom = (val - prev)  # already in thousands
        disp = f"{mom:+,.0f}K MoM"
        if mom < 0:
            flag = "🔴"
        elif mom < 100:
            flag = "🟠"   # weak / consistent with freeze
        elif mom >= 200:
            flag = "🟠"   # Kill A watch (bull-break risk for bearish thesis)
        else:
            flag = "🟢"
    elif series_id == "TEMPHELPS" and prev is not None:
        mom = val - prev
        disp = f"{val:,.1f}K  (MoM {mom:+,.1f}K)"
        flag = "🔴" if mom < 0 else "🟢"
    return disp, flag


def main():
    verbose = "--verbose" in sys.argv
    periods = 4
    if "--periods" in sys.argv:
        i = sys.argv.index("--periods")
        if i + 1 < len(sys.argv):
            periods = int(sys.argv[i + 1])

    now = datetime.now()
    print(f"\n{'='*72}")
    print(f"  LABOR DOMAIN DATA SWEEP — {now.strftime('%A, %B %d, %Y  %H:%M')}")
    print(f"  source: FRED via FORGE/tools/market-data/fetch.py")
    print(f"{'='*72}\n")
    print(f"  {'Indicator':<30} {'Latest':>26}  {'Flag':<4} {'As of':<11} Src")
    print(f"  {'-'*78}")

    red_fired = []
    fetch_failures = 0
    for series_id, label, kind, src in LABOR_SERIES:
        obs, err = fetch_series(series_id, periods)
        if err or not obs:
            print(f"  {label:<30} {'ERROR: ' + (err or 'no data'):>26}  ⚠️")
            fetch_failures += 1
            continue
        disp, flag = assess(series_id, kind, obs)
        asof = obs[0][0]
        print(f"  {label:<30} {disp:>26}  {flag:<4} {asof:<11} [{src}]")
        if "🔴" in flag:
            red_fired.append((label, disp, asof))
        if verbose and len(obs) > 1:
            for d, v in obs[1:]:
                print(f"      {'':28} {fmt_value(kind, v):>26}  {'':4} {d}")

    # post-don't-hire composite check (JOLTS openings up while hires down)
    print(f"\n  {'-'*78}")
    print("  THRESHOLD NOTES (wired to STATUS KEY THRESHOLDS):")
    print("    • Initial claims: >300K single → FIRE 🔴 (CARL/REGINALD/HENRY; all ORANGE→RED); 251-300K single → ARM provisional (confirm 2nd consecutive >250K); 230-250K → accelerating — apply premortem for the action")
    print("    • U-3  >5.0% → HENRY structural bid break")
    print("    • NFP  ≥200K x3 consecutive → Kill A (bull falsification of bearish thesis)")
    print("    • DOGE >400K → manual (not FRED); see STATUS dashboard")

    if fetch_failures:
        print(f"\n  ⚠️  {fetch_failures}/{len(LABOR_SERIES)} series FAILED to fetch — "
              f"sweep INCOMPLETE; do NOT read as all-clear (check venv/FRED/network).")
    if red_fired:
        print(f"\n  🔴 {len(red_fired)} RED threshold flag(s) fired:")
        for label, disp, asof in red_fired:
            print(f"     • {label}: {disp} ({asof})")
    elif not fetch_failures:
        print("\n  ✅ No RED thresholds breached this sweep.")

    print(f"\n  → Report refreshed levels to Will before analysis.\n")
    return 2 if (red_fired or fetch_failures) else 0


if __name__ == "__main__":
    sys.exit(main())
