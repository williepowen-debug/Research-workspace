#!/usr/bin/env python3
"""
BRENT Boot Sequence — Master Orchestrator

Runs all BRENT monitoring scripts in sequence and prints a consolidated boot
brief. Replaces manual web-search refresh with a single command.

Smart behavior:
  - Scripts run in order of priority (threshold breaches first)
  - Each script's exit code captured; failures reported but don't stop sequence
  - Collapsed output by default; --verbose shows full script output

Usage:
  .venv/bin/python3 AGENTS/BRENT/scripts/boot.py
  .venv/bin/python3 AGENTS/BRENT/scripts/boot.py --quick    # skip slow
  .venv/bin/python3 AGENTS/BRENT/scripts/boot.py --verbose  # full output
"""

import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
BRENT_DIR = SCRIPTS_DIR.parent
WORKSPACE = BRENT_DIR.parent.parent  # Research-workspace/
VENV_PYTHON = WORKSPACE / ".venv" / "bin" / "python3"


# Boot sequence: (label, script_name, args, slow)
BOOT_SEQUENCE = [
    ("Threshold Monitor",    "thresholds.py",         [], False),
    ("EIA Weekly Monitor",   "eia_weekly.py",         [], False),
    ("Catalyst Countdown",   "catalyst_countdown.py", [], False),
]


def run_script(script_path, args, timeout=60):
    """Run a script and capture output. Returns (success, output, elapsed_seconds)."""
    if not script_path.exists():
        return False, f"  SKIP: {script_path.name} not found", 0

    start = time.time()
    try:
        result = subprocess.run(
            [str(VENV_PYTHON), str(script_path)] + args,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=str(WORKSPACE),
        )
        elapsed = time.time() - start
        output = result.stdout
        if result.returncode != 0 and result.stderr:
            output += f"\n  STDERR: {result.stderr[:500]}"
        return result.returncode == 0, output, elapsed
    except subprocess.TimeoutExpired:
        elapsed = time.time() - start
        return False, f"  TIMEOUT after {elapsed:.0f}s", elapsed
    except Exception as e:
        elapsed = time.time() - start
        return False, f"  ERROR: {e}", elapsed


def main():
    quick = "--quick" in sys.argv
    verbose = "--verbose" in sys.argv

    start_time = time.time()
    now = datetime.now()

    print(f"\n{'#'*72}")
    print(f"#{'':^70}#")
    print(f"#{'BRENT BOOT SEQUENCE':^70}#")
    print(f"#{'':^70}#")
    print(f"#  {now.strftime('%A, %B %d, %Y  %H:%M'):^66}#")
    print(f"#{'':^70}#")
    print(f"{'#'*72}")

    results = []

    for label, script_name, args, is_slow in BOOT_SEQUENCE:
        if is_slow and quick:
            print(f"\n  ⏩ Skipping {label} (--quick)")
            results.append((label, "SKIP", 0))
            continue

        script_path = SCRIPTS_DIR / script_name

        print(f"\n  ⏳ {label}...", flush=True)
        success, output, elapsed = run_script(script_path, args)

        if verbose:
            if output.strip():
                print(output)
        else:
            # Collapsed: show only alert-worthy lines
            key_markers = (
                "🔴", "🟠", "⚠️",
                "BREACHED", "BREACH", "CRISIS", "STRESS",
                "IMMINENT", "HIGH PRIORITY",
                "FIRED", "TRIGGER",
                "Source:", "Week ending", "Released",
                "Cushing:", "Gas demand YoY", "Refinery util",
                "Commercial crude",
                "CRUDE & FUTURES", "POSITIONS", "Brent futures", "WTI futures",
                "THESIS CONFIRMING",
            )
            lines = output.splitlines()
            shown = False
            for line in lines:
                if any(marker in line for marker in key_markers):
                    print(f"    {line}")
                    shown = True
            if not shown:
                print(f"    ✓ ran cleanly, no alerts")

        status = "OK" if success else "FAIL"
        results.append((label, status, elapsed))

    # Summary
    total_time = time.time() - start_time
    print(f"\n{'='*72}")
    print(f"  BOOT SUMMARY")
    print(f"{'='*72}")
    print(f"\n  {'Script':<30} {'Status':>8} {'Time':>8}")
    print(f"  {'-'*50}")
    for label, status, elapsed in results:
        icon = "✅" if status == "OK" else "⏩" if status == "SKIP" else "❌"
        print(f"  {icon} {label:<28} {status:>6} {elapsed:>6.1f}s")

    print(f"\n  Total boot time: {total_time:.1f}s")
    print(f"  Date: {now.strftime('%Y-%m-%d')} | Day: {now.strftime('%A')}")

    failures = [r for r in results if r[1] == "FAIL"]
    if failures:
        print(f"\n  ⚠️  {len(failures)} script(s) failed — check output (try --verbose).")
        return 1
    else:
        print(f"\n  ✅ All scripts completed successfully.")
        print(f"\n  Tip: run with --verbose to see full output for each script.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
