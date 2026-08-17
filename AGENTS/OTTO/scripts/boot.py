#!/usr/bin/env python3
"""
OTTO Boot Sequence — Master Orchestrator

Runs OTTO's automatable boot steps in one command and prints a consolidated brief.
Replaces the manual price/predictions/calendar sweep that gets skipped under time
pressure (which is how OTTO's dashboard goes stale).

What it runs:
  1. Price snapshot — OTTO's tradeable watchlist (CVNA, ALLY) via FORGE fetch.py
  2. Predictions-due scan — thesis/PREDICTIONS.tsv (boot step 4)
  3. Catalyst countdown — docket/CATALYSTS.tsv (boot step 5)

What it does NOT do: OTTO's domain data (fraud filings, ABS surveillance, bank
8-Ks) has no clean automated feed — those are news/EDGAR/PACER lookups done
in-session. abs_issuance_tracker.py / extension_proxy.py are manual-check stubs,
not wired here. This kit automates the calendar/ledger/price hygiene only.

Usage:
  .venv/bin/python3 AGENTS/OTTO/scripts/boot.py
  .venv/bin/python3 AGENTS/OTTO/scripts/boot.py --verbose
  .venv/bin/python3 AGENTS/OTTO/scripts/boot.py --no-price   # skip network price call
"""

import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

DATE_ROW = re.compile(r"\d{4}-\d{2}-\d{2}")  # identifies catalyst data rows in sub-script output

SCRIPTS_DIR = Path(__file__).resolve().parent
OTTO_DIR = SCRIPTS_DIR.parent
WORKSPACE = OTTO_DIR.parent.parent  # Research-workspace/
VENV_PYTHON = WORKSPACE / ".venv" / "bin" / "python3"
FETCH = WORKSPACE / "FORGE" / "tools" / "market-data" / "fetch.py"
STALENESS = WORKSPACE / "scripts" / "ledger_staleness.py"  # fleet enforcer (PROME PAT-035)

WATCHLIST = ["CVNA", "ALLY"]  # OTTO's tradeable names (TRADE.md)

# (label, script_name, args)
BOOT_SEQUENCE = [
    ("Predictions Due",    "predictions_due.py",    []),
    ("Catalyst Countdown", "catalyst_countdown.py", []),
]


def run(cmd, timeout=60):
    start = time.time()
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout, cwd=str(WORKSPACE)
        )
        elapsed = time.time() - start
        output = result.stdout
        if result.returncode != 0 and result.stderr:
            output += f"\n  STDERR: {result.stderr[:400]}"
        return result.returncode, output, elapsed
    except subprocess.TimeoutExpired:
        return 124, f"  TIMEOUT after {time.time()-start:.0f}s", time.time() - start
    except Exception as e:
        return 1, f"  ERROR: {e}", time.time() - start


def main():
    verbose = "--verbose" in sys.argv
    no_price = "--no-price" in sys.argv

    start_time = time.time()
    now = datetime.now()

    print(f"\n{'#'*72}")
    print(f"#{'OTTO BOOT SEQUENCE':^70}#")
    print(f"#  {now.strftime('%A, %B %d, %Y  %H:%M'):^66}#")
    print(f"{'#'*72}")

    results = []

    # 1. Price snapshot (network)
    if not no_price and FETCH.exists():
        print(f"\n  ⏳ Price snapshot ({', '.join(WATCHLIST)})...", flush=True)
        rc, out, elapsed = run([str(VENV_PYTHON), str(FETCH), "price"] + WATCHLIST, timeout=40)
        if out.strip():
            for ln in out.splitlines():
                if ln.strip():
                    print(f"    {ln}")
        results.append(("Price Snapshot", "OK" if rc == 0 else "FAIL", elapsed))
    elif no_price:
        print(f"\n  ⏩ Skipping price snapshot (--no-price)")
        results.append(("Price Snapshot", "SKIP", 0))

    # 2..N scripts
    for label, script_name, args in BOOT_SEQUENCE:
        script_path = SCRIPTS_DIR / script_name
        print(f"\n  ⏳ {label}...", flush=True)
        if not script_path.exists():
            print(f"    SKIP: {script_name} not found")
            results.append((label, "FAIL", 0))
            continue
        rc, out, elapsed = run([str(VENV_PYTHON), str(script_path)] + args)
        if verbose:
            if out.strip():
                print(out)
        else:
            key = ("🔴", "🟠", "⚠️", "OVERDUE", "IMMINENT", "HIGH PRIORITY",
                   "RECENTLY FIRED", "due soon", "overdue", "OPEN |")
            # Section-sticky pass for RECENTLY FIRED: every fired row must surface
            # regardless of its priority glyph. A 🟡 fired catalyst is still an UNSWEPT
            # catalyst, and filtering the past-due-catch by priority silently re-creates
            # the exact miss the countdown exists to prevent. (2026-07-25: 3 of 4 fired
            # rows were hidden at boot — incl. the First Brands creditor-vote deadline,
            # a direct dependency of the OTTO-32 resolver.)
            section_end = ("IMMINENT", "UPCOMING", "HIGH PRIORITY in horizon")
            in_fired = False
            shown = False
            for ln in out.splitlines():
                if "RECENTLY FIRED" in ln:
                    in_fired = True
                elif in_fired and any(k in ln for k in section_end):
                    in_fired = False
                if in_fired and DATE_ROW.search(ln):
                    print(f"    {ln}")
                    shown = True
                    continue
                if any(k in ln for k in key):
                    print(f"    {ln}")
                    shown = True
            if not shown:
                print(f"    ✓ ran cleanly, no alerts")
        # predictions_due returns 1 when overdue exist — that's a flag, not a failure
        status = "OK" if rc in (0, 1) else "FAIL"
        results.append((label, status, elapsed))

    # N. Ledger staleness — workbook TSVs + trade surface (fleet enforcer, read-only alert; PROME PAT-035)
    if STALENESS.exists():
        for slabel, sargs in [("Workbook", []), ("Trade", ["--trade"])]:
            print(f"\n  ⏳ {slabel} Staleness...", flush=True)
            rc, out, elapsed = run([str(VENV_PYTHON), str(STALENESS), "OTTO", "--quiet"] + sargs)
            line = out.strip() or f"✓ {slabel.lower()} surface current or FROZEN"
            print(f"    {line}")
            # rc contract REVISED 2026-08-17 (DAEDALUS shared-script fix, CHECK_STANDARD
            # §8 rule 3): 0 clean · 1 stale FINDINGS · 2 cannot-certify. FINDINGS = the
            # check ran correctly and reported rot — never render it as script failure.
            status = "OK" if rc == 0 else ("FINDINGS" if rc == 1 else "FAIL")
            results.append((f"{slabel} Staleness", status, elapsed))

    # Summary
    total = time.time() - start_time
    print(f"\n{'='*72}")
    print(f"  BOOT SUMMARY")
    print(f"{'='*72}")
    print(f"\n  {'Step':<22} {'Status':>8} {'Time':>8}")
    print(f"  {'-'*42}")
    for label, status, elapsed in results:
        icon = "✅" if status == "OK" else "⏩" if status == "SKIP" else "⚠️" if status == "FINDINGS" else "❌"
        print(f"  {icon} {label:<20} {status:>6} {elapsed:>6.1f}s")
    print(f"\n  Total boot time: {total:.1f}s")
    print(f"  Date: {now.strftime('%Y-%m-%d')} ({now.strftime('%A')})")
    print(f"\n  Next: read STATUS.md → LAST_COMPLETION.md → MEMORY.md, then report.")
    print(f"  (Domain intel — fraud filings, ABS surveillance, bank 8-Ks — is in-session web/EDGAR work.)\n")

    return 0 if all(r[1] != "FAIL" for r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
