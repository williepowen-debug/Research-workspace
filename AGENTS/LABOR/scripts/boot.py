#!/usr/bin/env python3
"""
LABOR Boot Sequence — Master Orchestrator

Runs LABOR's boot scripts in sequence and prints a consolidated brief, so a
fresh spawn refreshes domain data BEFORE analysis (parity with SAM/BRENT
boot.py). Replaces manual data-refresh + calendar-walk with one command.

Sequence:
  1. labor_data.py        — live FRED sweep (claims, NFP, U-3/6, JOLTS, temp) + threshold flags
  2. catalyst_countdown.py — docket/CATALYSTS.tsv countdown (imminent ≤5 trd)
  3. predictions_due.py   — flag OPEN predictions past/near due-by

Smart behavior:
  - Each script's exit code captured; failures reported but don't stop the run
  - Collapsed output by default (alert-worthy lines only); --verbose shows full output
  - Aggregate exit: 2 if any sub-script signalled a RED/overdue condition

Usage:
  .venv/bin/python3 AGENTS/LABOR/scripts/boot.py
  .venv/bin/python3 AGENTS/LABOR/scripts/boot.py --verbose
"""

import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
LABOR_DIR = SCRIPTS_DIR.parent
WORKSPACE = LABOR_DIR.parent.parent  # Research-workspace/
VENV_PYTHON = WORKSPACE / ".venv" / "bin" / "python3"
PYTHON = str(VENV_PYTHON) if VENV_PYTHON.exists() else sys.executable  # fall back to system python in no-.venv envs

# label, script, args
BOOT_SEQUENCE = [
    ("Domain Data Sweep",  "labor_data.py",         []),
    ("Catalyst Countdown", "catalyst_countdown.py", []),
    ("Predictions Due",    "predictions_due.py",    []),
]

# lines worth surfacing in collapsed mode
KEY_MARKERS = (
    "🔴", "🟠", "⚠️", "RED", "OVERDUE", "DUE SOON",
    "IMMINENT", "HIGH PRIORITY", "threshold flag",
    "No RED", "No OPEN", "Report refreshed",
)


def run_script(script_path, args, timeout=90):
    if not script_path.exists():
        return None, f"  SKIP: {script_path.name} not found", 0
    start = time.time()
    try:
        result = subprocess.run(
            [PYTHON, str(script_path)] + args,
            capture_output=True, text=True, timeout=timeout, cwd=str(WORKSPACE),
        )
        out = result.stdout
        if result.returncode not in (0, 2) and result.stderr:
            out += f"\n  STDERR: {result.stderr[:500]}"
        return result.returncode, out, time.time() - start
    except subprocess.TimeoutExpired:
        return None, f"  TIMEOUT after {time.time()-start:.0f}s", time.time() - start
    except Exception as e:  # noqa: BLE001
        return None, f"  ERROR: {e}", time.time() - start


def main():
    verbose = "--verbose" in sys.argv
    start_time = time.time()
    now = datetime.now()

    print(f"\n{'#'*72}")
    print(f"#{'':^70}#")
    print(f"#{'LABOR BOOT SEQUENCE':^70}#")
    print(f"#{now.strftime('%A, %B %d, %Y  %H:%M'):^70}#")
    print(f"#{'':^70}#")
    print(f"{'#'*72}")

    results = []
    alert = False

    for label, script_name, args in BOOT_SEQUENCE:
        script_path = SCRIPTS_DIR / script_name
        print(f"\n  ⏳ {label}...", flush=True)
        rc, output, elapsed = run_script(script_path, args)

        if verbose:
            if output.strip():
                print(output)
        else:
            shown = False
            for line in output.splitlines():
                if any(m in line for m in KEY_MARKERS):
                    print(f"    {line.strip()}")
                    shown = True
            if not shown:
                print(f"    ✓ ran cleanly")

        if rc == 2:
            alert = True
        status = "OK" if rc in (0, 2) else "FAIL"
        results.append((label, status, elapsed))

    print(f"\n{'='*72}")
    print(f"  BOOT SUMMARY")
    print(f"{'='*72}")
    print(f"\n  {'Script':<24} {'Status':>8} {'Time':>8}")
    print(f"  {'-'*42}")
    for label, status, elapsed in results:
        icon = "✅" if status == "OK" else "❌"
        print(f"  {icon} {label:<22} {status:>6} {elapsed:>6.1f}s")

    print(f"\n  Total boot time: {time.time()-start_time:.1f}s | {now.strftime('%Y-%m-%d %A')}")
    if alert:
        print(f"\n  🔴 Alert condition(s) flagged above — review before analysis.")
    print(f"\n  Tip: --verbose for full per-script output.\n")

    failures = [r for r in results if r[1] == "FAIL"]
    if failures:
        print(f"  ⚠️  {len(failures)} script(s) failed.\n")
        return 1
    return 2 if alert else 0


if __name__ == "__main__":
    sys.exit(main())
