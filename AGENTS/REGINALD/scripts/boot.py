#!/usr/bin/env python3
"""
REGINALD Boot Sequence
Master orchestrator — runs all monitoring scripts in sequence.
Single command replaces the multi-step manual boot.

Usage:
  .venv/bin/python3 AGENTS/REGINALD/scripts/boot.py
  .venv/bin/python3 AGENTS/REGINALD/scripts/boot.py --skip-slow   # skip EDGAR queries (insider, 8k)
"""

import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
WORKSPACE = SCRIPTS_DIR.parent.parent.parent  # Research-workspace/
VENV_PYTHON = WORKSPACE / ".venv" / "bin" / "python3"

# Market.py lives at workspace root
MARKET_PY = WORKSPACE / "scripts" / "market.py"

# Scripts on the shared verdict contract (repair 2026-10-09): rc 0 = read, nothing to review ·
# rc 1 = ALERT, read the output · rc 2 = INCOMPLETE, some name or input has NO VERDICT.
# Every other script: rc != 0 = FAIL. Only an all-OK run prints the all-clear line.
TRI_STATE = {"Insider Activity", "8-K Monitor", "Earnings Countdown"}

# Boot sequence: (name, script_path, category, slow)
BOOT_SEQUENCE = [
    ("Market Prices",      MARKET_PY,                          "PRICES",    False),
    ("Dark Pool + Short Vol", SCRIPTS_DIR / "darkpool.py",     "MICRO",     False),
    ("Thresholds",         SCRIPTS_DIR / "thresholds.py",      "ALERTS",    False),
    ("KRE Float",          SCRIPTS_DIR / "kre_float.py",       "STRUCTURE", False),
    ("Earnings Countdown", SCRIPTS_DIR / "earnings_countdown.py", "CALENDAR", False),
    ("Short Interest",     SCRIPTS_DIR / "si_refresh.py",      "SI",        False),
    ("Insider Activity",   SCRIPTS_DIR / "insider.py",         "EDGAR",     True),
    ("8-K Monitor",        SCRIPTS_DIR / "8k_monitor.py",      "EDGAR",     True),
]


def run_script(name, script_path, timeout=120):
    """Run a script and capture output. Returns (success, output, elapsed)."""
    if not script_path.exists():
        return None, f"  MISSING: {script_path.name} not found", 0

    start = time.time()
    try:
        result = subprocess.run(
            [str(VENV_PYTHON), str(script_path)],
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=str(WORKSPACE),
        )
        elapsed = time.time() - start
        output = result.stdout
        if result.returncode != 0:
            output += f"\n  STDERR: {result.stderr[:500]}" if result.stderr else ""
        return result.returncode, output, elapsed
    except subprocess.TimeoutExpired:
        elapsed = time.time() - start
        return None, f"  TIMEOUT after {elapsed:.0f}s", elapsed
    except Exception as e:
        elapsed = time.time() - start
        return None, f"  ERROR: {e}", elapsed


def main():
    skip_slow = "--skip-slow" in sys.argv
    start_time = time.time()
    now = datetime.now()

    print(f"\n{'#'*70}")
    print(f"#{'':^68}#")
    print(f"#{'REGINALD BOOT SEQUENCE':^68}#")
    print(f"#{'':^68}#")
    print(f"#  {now.strftime('%A, %B %d, %Y  %H:%M'):^66}#")
    print(f"#{'':^68}#")
    print(f"{'#'*70}")

    results = []

    for name, script_path, category, is_slow in BOOT_SEQUENCE:
        if is_slow and skip_slow:
            print(f"\n  ⏩ Skipping {name} (--skip-slow)")
            results.append((name, "SKIP", 0))
            continue

        print(f"\n  ⏳ Running {name}...", flush=True)
        rc, output, elapsed = run_script(name, script_path)

        if output.strip():
            print(output)

        if rc == 0:
            status = "OK"
        elif name in TRI_STATE and rc == 1:
            status = "ALERT"
        elif name in TRI_STATE and rc == 2:
            status = "INCOMPLETE"
        else:
            status = "FAIL"
        results.append((name, status, elapsed))

    # Summary
    total_time = time.time() - start_time
    print(f"\n{'='*70}")
    print(f"  BOOT SUMMARY")
    print(f"{'='*70}")
    print(f"\n  {'Script':<25} {'Status':>8} {'Time':>8}")
    print(f"  {'-'*45}")
    for name, status, elapsed in results:
        icon = {"OK": "✅", "SKIP": "⏩", "ALERT": "🔔", "INCOMPLETE": "⚠️ "}.get(status, "❌")
        print(f"  {icon} {name:<23} {status:>10} {elapsed:>6.1f}s")

    print(f"\n  Total boot time: {total_time:.1f}s")
    print(f"  Date: {now.strftime('%Y-%m-%d')} | Day: {now.strftime('%A')}")

    # Count non-OK outcomes — an ALERT, INCOMPLETE or FAIL is never folded into an all-clear
    by = {k: [r[0] for r in results if r[1] == k] for k in ("FAIL", "INCOMPLETE", "ALERT", "SKIP")}
    for k, label in (("FAIL", "❌ FAILED"), ("INCOMPLETE", "⚠️  INCOMPLETE (no verdict for some names)"),
                     ("ALERT", "🔔 ALERT (read the output)"), ("SKIP", "⏩ SKIPPED")):
        if by[k]:
            print(f"\n  {label}: {', '.join(by[k])}")
    if not any(by[k] for k in ("FAIL", "INCOMPLETE", "ALERT", "SKIP")):
        print(f"\n  ✅ All scripts completed and every check read cleanly.")

    print()


if __name__ == "__main__":
    main()
