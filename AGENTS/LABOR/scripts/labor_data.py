#!/usr/bin/env python3
"""
LABOR Domain Data Sweep

Pulls the LABOR-domain FRED series via the shared market-data tool
(FORGE/tools/market-data/fetch.py) and prints a dashboard with threshold
flags wired to STATUS.md KEY THRESHOLDS. Self-contained under AGENTS/LABOR/;
no shared-file edits required (fetch.py accepts arbitrary FRED series).

WIRING BASIS: STATUS.md § KEY THRESHOLDS as of 2026-09-07.
⚠️ This claim rots silently. Between 2026-08-07 (BD-15 demoted U-3 to a reported
gauge and moved T-03/T-04 to EPOP) and 2026-09-07, this file kept firing the
RETIRED U-3 level bars and did not fetch EMRATIO at all — so for 31 days the boot
could raise a 🔴 on a trigger that no longer existed while the live gauge was
invisible, and the docstring above asserted it was wired the whole time.
A guard being CORRECT and a guard being WIRED TO THE DECLARED REFERENCE are
independent properties (finding_guard_correctness_and_wiring_are_independent).
⇒ When a KEY THRESHOLDS row changes, re-date this line and diff the branches below.

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
PYTHON = str(VENV_PYTHON) if VENV_PYTHON.exists() else sys.executable  # fall back to system python in no-.venv envs
FETCH = WORKSPACE / "FORGE" / "tools" / "market-data" / "fetch.py"

# series_id, label, kind, source_tag
#   kind: "claims" (thousands, K)  | "rate" (%)  | "level_mom" (thousands, show MoM Δ)
LABOR_SERIES = [
    ("ICSA",      "Initial Claims (wkly)",       "claims",    "DOL"),
    ("IC4WSA",    "Initial Claims 4-wk MA",      "claims",    "DOL"),
    ("CCSA",      "Continuing Claims (1wk lag)",  "claims",    "DOL"),
    ("PAYEMS",    "NFP total (MoM Δ)",            "level_mom", "BLS"),
    ("EMRATIO",   "EPOP ratio (T-03/T-04)",       "epop",      "BLS"),
    ("UNRATE",    "U-3 (reported gauge only)",     "rate",      "BLS"),
    ("U6RATE",    "U-6 underemployment",          "rate",      "BLS"),
    ("CIVPART",   "Labor force participation",    "rate",      "BLS"),
    ("JTSJOL",    "JOLTS openings (MoM Δ)",       "level_mom", "BLS"),
    ("JTSHIL",    "JOLTS hires (MoM Δ)",          "level_mom", "BLS"),
    ("JTSQUL",    "JOLTS quits (MoM Δ)",          "level_mom", "BLS"),
    ("JTSLDL",    "JOLTS layoffs/disch (MoM Δ)",  "level_mom", "BLS"),
    ("TEMPHELPS", "Temp help svcs (MoM Δ)",       "level_mom", "BLS"),
]

# Series needing deeper history than the default fetch window.
# EMRATIO carries T-03 (3-month Δ) and T-04 (6-month Δ), so it needs the current
# observation plus 6 prior months = 7. A short fetch cannot be allowed to look
# like "no decline" — assess() reports CANNOT-VERIFY rather than a 🟢 if it is short.
MIN_PERIODS = {"EMRATIO": 7}


def fetch_series(series_id, periods=4):
    """Call shared fetch.py in --json mode. Returns list of (date, float|None) newest-first."""
    try:
        result = subprocess.run(
            [PYTHON, str(FETCH), "fred", series_id, "--periods", str(periods), "--json"],
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
    if kind in ("rate", "epop"):   # 'epop' added 2026-09-07 — without it the verbose
        return f"{val:.1f}%"       # history block printed EPOP 59.4 as "59K" (CODEX #4)
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
        # ⛔ NO FLAG BY DESIGN. U-3 was DEMOTED TO A REPORTED GAUGE on 2026-08-07
        # (BD-15); STATUS § KEY THRESHOLDS: "It no longer carries a trigger."
        # The retired bars were `>=4.7 -> T-03` and `>=5.0 -> T-04`; measured
        # 1990-2026, a 4.7% LEVEL bar fired in 65.4% of ALL months and separated
        # recession from non-recession by only +12.9pp. Both moved to EPOP below.
        # This branch printed 🔴/🟠 off those retired bars until 2026-09-07 and fed
        # the rc=2 path, i.e. the boot could raise a RED on a trigger that no longer
        # exists while the live gauge was not fetched at all.
        # ⚠️ Do NOT restore a flag here without a STATUS KEY THRESHOLDS row to wire it to.
        flag = ""
        disp = f"{val:.1f}%  (no trigger)"
    elif series_id == "EMRATIO":
        # LIVE trigger gauge since 2026-08-07 (BD-15), replacing the retired U-3 bars.
        # STATUS § KEY THRESHOLDS:
        #   T-03 🟠 = EPOP fell >=0.3pp over 3 months          -> CARL + HENRY
        #   T-04 🔴 = EPOP fell >=0.5pp over 6 months AND >=0.3pp over 3 months
        #                                                      -> HENRY + REGINALD
        # Both are Δ-over-a-WINDOW, not level bars: the far end of the window rolls,
        # so a FLAT print can fire one. Referents are obs[3] (3-mo) and obs[6] (6-mo);
        # verified 2026-09-07 against STATUS: 59.1 - 59.2 = -0.1pp (3m, May referent)
        # and 59.1 - 59.3 = -0.2pp (6m, Feb referent), reproducing both published values.
        # ⚠️ EXACT ARITHMETIC IN INTEGER TENTHS — NOT float subtraction.
        # EPOP is published to ONE decimal, and these triggers compare to exact
        # boundaries (-0.3, -0.5). Binary float makes that comparison VALUE-DEPENDENT:
        #     59.1 - 59.4 = -0.29999999999999716  -> <= -0.3 is FALSE  (T-03 missed)
        #     58.9 - 59.2 = -0.30000000000000426  -> <= -0.3 is TRUE   (T-03 fires)
        # Same -0.3pp move, opposite verdicts, and BOTH display as "-0.3" — so the
        # printed evidence contradicted the verdict on exactly half the boundary.
        # This shipped on 2026-09-07 and my own 8 guard tests PASSED, because the
        # fixture I chose (58.9/59.2) happened to land on the lucky side.
        # ⇒ finding_float_precision_empties_the_tie_set_and_voids_the_operator.
        # A single boundary fixture is a SAMPLE, not a proof, when the operator is
        # float. Integer tenths removes the class rather than sampling it.
        # Found by CODEX review; regression fixtures in tests/test_epop_thresholds.py
        # sweep the WHOLE boundary class, not one pair.
        def tenths(x):
            return int(round(x * 10))
        t_now = tenths(val)
        t3 = tenths(obs[3][1]) if len(obs) > 3 and obs[3][1] is not None else None
        t6 = tenths(obs[6][1]) if len(obs) > 6 and obs[6][1] is not None else None
        if t3 is None or t6 is None:
            # A short/gappy history cannot demonstrate the ABSENCE of a decline.
            # Fail loud: never let insufficient data print as 🟢.
            disp = f"{val:.1f}%  (Δ unavailable — history short)"
            return disp, "⚠️"
        d3, d6 = t_now - t3, t_now - t6          # integer tenths of a pp
        disp = f"{val:.1f}%  (3m {d3/10:+.1f} · 6m {d6/10:+.1f})"
        if d6 <= -5 and d3 <= -3:
            flag = "🔴"   # T-04: >=0.5pp over 6m AND >=0.3pp over 3m
        elif d3 <= -3:
            flag = "🟠"   # T-03: >=0.3pp over 3m
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
    cannot_verify = []
    fetch_failures = 0
    for series_id, label, kind, src in LABOR_SERIES:
        obs, err = fetch_series(series_id, max(periods, MIN_PERIODS.get(series_id, 0)))
        if err or not obs:
            print(f"  {label:<30} {'ERROR: ' + (err or 'no data'):>26}  ⚠️")
            fetch_failures += 1
            continue
        disp, flag = assess(series_id, kind, obs)
        asof = obs[0][0]
        print(f"  {label:<30} {disp:>26}  {flag:<4} {asof:<11} [{src}]")
        if "🔴" in flag:
            red_fired.append((label, disp, asof))
        elif "⚠️" in flag:
            # The fetch SUCCEEDED but the series cannot be assessed (newest value
            # null, or history too short for a windowed trigger). Root canon and
            # spine_check.py both hold that a failure to verify is CANNOT-VERIFY,
            # never a pass — so this must suppress the all-clear exactly as a
            # network failure does. Before 2026-09-07 it did not: `fetch_failures`
            # only counted `err`, so a null latest value printed ⚠️ on its own row
            # and "✅ No RED thresholds breached this sweep" underneath it.
            cannot_verify.append((label, asof))
        if verbose and len(obs) > 1:
            for d, v in obs[1:]:
                print(f"      {'':28} {fmt_value(kind, v):>26}  {'':4} {d}")

    # post-don't-hire composite check (JOLTS openings up while hires down)
    print(f"\n  {'-'*78}")
    print("  THRESHOLD NOTES (wired to STATUS KEY THRESHOLDS):")
    print("    • Initial claims: >300K single → FIRE 🔴 (CARL/REGINALD/HENRY; all ORANGE→RED); 251-300K single → ARM provisional (confirm 2nd consecutive >250K); 230-250K → accelerating — apply premortem for the action")
    print("    • EPOP T-03 🟠 = fell ≥0.3pp over 3mo → CARL+HENRY · T-04 🔴 = fell ≥0.5pp over 6mo AND ≥0.3pp over 3mo → HENRY+REGINALD")
    print("    • U-3  NO TRIGGER — demoted to a reported gauge 2026-08-07 (BD-15); triggers live on EPOP above")
    print("    • NFP  ≥200K x3 consecutive → Kill A (bull falsification of bearish thesis)")
    print("    • DOGE >400K → manual (not FRED); see STATUS dashboard")

    if fetch_failures:
        print(f"\n  ⚠️  {fetch_failures}/{len(LABOR_SERIES)} series FAILED to fetch — "
              f"sweep INCOMPLETE; do NOT read as all-clear (check venv/FRED/network).")
    if cannot_verify:
        print(f"\n  ⚠️  {len(cannot_verify)} series CANNOT-VERIFY (fetched, not assessable) — "
              f"sweep INCOMPLETE; do NOT read as all-clear:")
        for label, asof in cannot_verify:
            print(f"     • {label} (latest obs {asof})")
    if red_fired:
        print(f"\n  🔴 {len(red_fired)} RED threshold flag(s) fired:")
        for label, disp, asof in red_fired:
            print(f"     • {label}: {disp} ({asof})")
    elif not fetch_failures and not cannot_verify:
        print("\n  ✅ No RED thresholds breached this sweep.")

    print(f"\n  → Report refreshed levels to Will before analysis.\n")
    return 2 if (red_fired or fetch_failures or cannot_verify) else 0


if __name__ == "__main__":
    sys.exit(main())
