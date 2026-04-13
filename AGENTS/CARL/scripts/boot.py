#!/usr/bin/env python3
"""
CARL Boot Sequence — Master Orchestrator

Runs all CARL monitoring scripts in sequence and prints a consolidated boot
brief. Replaces multi-step manual data pulls with a single command.

Smart behavior:
  - Scripts run in priority order (threshold breaches first).
  - Each script's exit code is captured; failures don't stop the sequence.
  - Collapsed output: only show alert lines unless --verbose.
  - --quick skips slow scripts (EDGAR ABS monitor, housing web scrape).
  - --skip-abs skips just ABS monitor.

Usage:
  .venv/bin/python3 AGENTS/CARL/scripts/boot.py
  .venv/bin/python3 AGENTS/CARL/scripts/boot.py --quick
  .venv/bin/python3 AGENTS/CARL/scripts/boot.py --verbose
"""

import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
CARL_DIR = SCRIPTS_DIR.parent
WORKSPACE = CARL_DIR.parent.parent  # Research-workspace/
VENV_PYTHON = WORKSPACE / ".venv" / "bin" / "python3"

# Boot sequence: (label, script_name, args, section_header, slow)
BOOT_SEQUENCE = [
    ("Market + FRED Thresholds",  "thresholds.py",       [], "THRESHOLDS",      False),
    ("Gas Price Tracker",         "gas_tracker.py",       [], "GAS PRICES",      False),
    ("Consumer Pulse (FRED)",     "consumer_pulse.py",    [], "CONSUMER PULSE",  False),
    ("Housing Pulse (FRED)",      "housing_pulse.py",     [], "HOUSING PULSE",   False),
    ("Catalyst Countdown",        "catalyst_countdown.py", [], "CATALYSTS",       False),
    ("ABS Trust Monitor (EDGAR)", "abs_monitor.py",       [], "ABS FILINGS",     True),
]

# Key markers to show in collapsed mode
KEY_MARKERS = (
    "\U0001f534", "\U0001f7e0", "\U0001f7e1", "\U0001f7e2", "\u26a0\ufe0f",
    "BREACH", "CRISIS", "STRESS", "ELEVATED", "FIRED",
    "ALERT", "WARNING", "RED", "URGENT",
    "ABOVE $4", "behavioral breakpoint",
    "\U0001f195",  # NEW filing emoji
    "NEW FILINGS",
    "SUMMARY:", "THRESHOLD STATUS",
    "1TD", "2TD", "3TD",
)


def run_script(label, script_path, args, timeout=90):
    """Run a script and capture output. Returns (success, output, elapsed)."""
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


def collapse_output(output):
    """Show only lines containing key alert markers."""
    lines = output.splitlines()
    shown = []
    for line in lines:
        if any(marker in line for marker in KEY_MARKERS):
            shown.append(f"    {line}")
    return shown


def main():
    quick = "--quick" in sys.argv
    verbose = "--verbose" in sys.argv
    skip_abs = "--skip-abs" in sys.argv

    start_time = time.time()
    now = datetime.now()

    print(f"\n{'#'*72}")
    print(f"#{'':^70}#")
    print(f"#{'CARL BOOT SEQUENCE':^70}#")
    print(f"#{'Consumer Stress Monitoring Suite':^70}#")
    print(f"#{'':^70}#")
    print(f"#  {now.strftime('%A, %B %d, %Y  %H:%M'):^66}  #")
    print(f"#{'':^70}#")
    print(f"{'#'*72}")

    if quick:
        print(f"\n  [--quick mode: skipping slow scripts]")
    if skip_abs:
        print(f"\n  [--skip-abs: skipping ABS EDGAR monitor]")

    results = []

    for label, script_name, args, section_header, is_slow in BOOT_SEQUENCE:
        # Skip logic
        if is_slow and quick:
            print(f"\n  \u23e9 Skipping {label} (--quick)")
            results.append((label, "SKIP", 0))
            continue
        if script_name == "abs_monitor.py" and skip_abs:
            print(f"\n  \u23e9 Skipping {label} (--skip-abs)")
            results.append((label, "SKIP", 0))
            continue

        script_path = SCRIPTS_DIR / script_name

        print(f"\n  \u23f3 {label}...", flush=True)
        timeout = 120 if is_slow else 90
        success, output, elapsed = run_script(label, script_path, args, timeout=timeout)

        if verbose or not output.strip():
            if output.strip():
                print(output)
        else:
            # Collapsed: show only alert lines
            shown_lines = collapse_output(output)
            if shown_lines:
                for line in shown_lines:
                    print(line)
            else:
                print(f"    \u2713 ran cleanly, no alerts")

        status = "OK" if success else "FAIL"
        results.append((label, status, elapsed))

    # Summary
    total_time = time.time() - start_time
    print(f"\n{'='*72}")
    print(f"  BOOT SUMMARY")
    print(f"{'='*72}")
    print(f"\n  {'Script':<35} {'Status':>8} {'Time':>8}")
    print(f"  {'-'*55}")
    for label, status, elapsed in results:
        icon = "\u2705" if status == "OK" else "\u23e9" if status == "SKIP" else "\u274c"
        print(f"  {icon} {label:<33} {status:>6} {elapsed:>6.1f}s")

    print(f"\n  Total boot time: {total_time:.1f}s")
    print(f"  Date: {now.strftime('%Y-%m-%d')} | Day: {now.strftime('%A')}")
    print(f"  Data dir: AGENTS/CARL/scripts/data/")

    failures = [r for r in results if r[1] == "FAIL"]
    if failures:
        print(f"\n  \u26a0\ufe0f  {len(failures)} script(s) failed \u2014 run with --verbose for details.")
        return 1
    else:
        print(f"\n  \u2705 All scripts completed successfully.")
        print(f"\n  Tip: --verbose for full output, --quick to skip EDGAR, --skip-abs to skip ABS only")
        return 0


if __name__ == "__main__":
    sys.exit(main())
