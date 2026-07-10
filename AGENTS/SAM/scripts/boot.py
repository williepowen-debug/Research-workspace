#!/usr/bin/env python3
"""
SAM Boot Sequence — Master Orchestrator

Runs all SAM monitoring scripts in sequence and prints a consolidated boot
brief. Replaces the multi-step manual refresh in CLAUDE.md boot step 7 with
a single command.

Smart behavior:
  - Scripts are run in order of priority (threshold breaches first).
  - Each script's exit code is captured; failures are reported in the summary
    but do not stop the boot sequence.
  - FXY options runs weekly (skipped if FXY_OPTIONS.tsv already has today's date).
  - JGB auctions auto-probe the last few business days for recent results.

Usage:
  .venv/bin/python3 AGENTS/SAM/scripts/boot.py
  .venv/bin/python3 AGENTS/SAM/scripts/boot.py --quick    # skip options + auction lookback
  .venv/bin/python3 AGENTS/SAM/scripts/boot.py --verbose  # don't collapse script output
"""

import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
SAM_DIR = SCRIPTS_DIR.parent
WORKSPACE = SAM_DIR.parent.parent  # Research-workspace/
WORKBOOK = SAM_DIR / "workbook"
VENV_PYTHON = WORKSPACE / ".venv" / "bin" / "python3"

FXY_OPTIONS_TSV = WORKBOOK / "FXY_OPTIONS.tsv"


def _has_today_row(tsv_path):
    """Check if a TSV has a row for today's date in the first column."""
    if not tsv_path.exists():
        return False
    today = datetime.now().strftime("%Y-%m-%d")
    with open(tsv_path) as f:
        next(f, None)
        for line in f:
            parts = line.strip().split("\t")
            if parts and parts[0] == today:
                return True
    return False


# Boot sequence: (label, script_name, args, section_header, slow)
BOOT_SEQUENCE = [
    ("Market / Threshold Monitor", "thresholds.py",        [], "THRESHOLDS",   False),
    ("USDJPY History",             "usdjpy.py",            [], "USDJPY",       False),
    ("JGB Yields",                 "jgb_yields.py",        [], "JGB YIELDS",   False),
    ("JGB Auctions",               "jgb_auctions.py",      [], "JGB AUCTIONS", False),
    ("CFTC JPY Positioning",       "cftc_jpy.py",          [], "CFTC",         False),
    ("MOF Weekly Flows",           "mof_flows.py",         [], "MOF FLOWS",    False),
    ("GPIF Portfolio / Flows",     "gpif_flows.py",        [], "GPIF",         False),
    ("Japan Trade Balance",        "trade_balance_japan.py", ["--boot"], "TRADE BALANCE", False),
    ("Japan CPI",                  "cpi_japan.py",         [], "CPI",          False),
    ("Catalyst Countdown",         "catalyst_countdown.py", [], "CATALYSTS",    False),
    ("FXY Options OI",             "fxy_options.py",       [], "FXY OPTIONS",  True),  # weekly
]


def run_script(name, script_path, args, timeout=60):
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
    print(f"#{'SAM BOOT SEQUENCE':^70}#")
    print(f"#{'':^70}#")
    print(f"#  {now.strftime('%A, %B %d, %Y  %H:%M %Z'):^66}#")
    print(f"#{'':^70}#")
    print(f"{'#'*72}")

    results = []

    for label, script_name, args, section_header, is_slow in BOOT_SEQUENCE:
        # Smart skip: FXY options only if TSV doesn't already have today's data
        if script_name == "fxy_options.py":
            if _has_today_row(FXY_OPTIONS_TSV):
                print(f"\n  ⏩ Skipping {label} — TSV already has today's snapshot")
                results.append((label, "SKIP", 0))
                continue
            if quick:
                print(f"\n  ⏩ Skipping {label} (--quick)")
                results.append((label, "SKIP", 0))
                continue

        script_path = SCRIPTS_DIR / script_name

        print(f"\n  ⏳ {label}...", flush=True)
        success, output, elapsed = run_script(label, script_path, args)

        if verbose or not output:
            if output.strip():
                print(output)
        else:
            # Collapse: show only lines that contain key markers
            key_markers = (
                "🔴", "🟠", "🟡", "🟢", "⚠️",
                "BREACH", "CRISIS", "STRESS", "ELEVATED",
                "ALERT", "SHORT BUILD", "SHORT COVER",
                "BUYER STRIKE", "Quality problem",
                "IMMINENT", "HIGH PRIORITY",
                "Latest", "LATEST", "NEW:",
                "VOL PROXY", "ATM IV", "25d RR",  # surface the FXY vol read
            )
            lines = output.splitlines()
            shown = False
            # Always show the script's own section header line for context
            for line in lines:
                if any(marker in line for marker in key_markers):
                    print(f"    {line}")
                    shown = True
            if not shown:
                # Show a 1-line "ok" result
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
        print(f"\n  ⚠️  {len(failures)} script(s) failed — check output above (try --verbose).")
        return 1
    else:
        print(f"\n  ✅ All scripts completed successfully.")
        print(f"\n  Tip: run with --verbose to see full output for each script.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
