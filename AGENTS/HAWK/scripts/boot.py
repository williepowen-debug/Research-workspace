#!/usr/bin/env python3
"""
HAWK Boot Sequence — Master Orchestrator

One-command morning refresh for all HAWK monitoring. Runs scripts in
priority order and outputs consolidated brief with 🔴 alerts.

Usage:
  .venv/bin/python3 AGENTS/HAWK/scripts/boot.py
  .venv/bin/python3 AGENTS/HAWK/scripts/boot.py --quick    # skip slow fetches
  .venv/bin/python3 AGENTS/HAWK/scripts/boot.py --verbose  # full output
"""

import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
HAWK_DIR = SCRIPTS_DIR.parent
WORKSPACE = HAWK_DIR.parent.parent
WORKBOOK = HAWK_DIR / "workbook"
# Use system python3 if venv not available
VENV_PATH = WORKSPACE / ".venv" / "bin" / "python3"
VENV_PYTHON = VENV_PATH if VENV_PATH.exists() else Path("/usr/bin/python3")

# Boot sequence: (label, script_name, args, section_header, slow)
BOOT_SEQUENCE = [
    ("Brent Thresholds",      "thresholds.py",         [], "THRESHOLDS",    False),
    ("Catalyst Countdown",    "catalyst_countdown.py", [], "CATALYSTS",     False),
    ("War Monitor",           "war_monitor.py",        [], "WAR STATUS",    False),
    ("Oil Infrastructure",    "oil_infrastructure.py", [], "INFRASTRUCTURE", False),
    ("Sanctions Tracker",     "sanctions_tracker.py",  [], "SANCTIONS",     True),  # slower
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


def extract_alerts(output):
    """Extract alert lines from script output."""
    alerts = []
    lines = output.splitlines()
    for line in lines:
        if any(marker in line for marker in ["🔴", "🟠", "ALERT", "CRITICAL", "WARNING"]):
            alerts.append(line.strip())
    return alerts


def save_boot_log(results, alerts):
    """Save boot log to workbook/BOOT_LOG.md."""
    log_path = WORKBOOK / "BOOT_LOG.md"
    today = datetime.now().strftime("%Y-%m-%d %H:%M ET")
    
    with open(log_path, "a") as f:
        f.write(f"\n## Boot Sequence — {today}\n\n")
        f.write("**Script Results:**\n\n")
        for label, status, elapsed in results:
            icon = "✅" if status == "OK" else "⏩" if status == "SKIP" else "❌"
            f.write(f"- {icon} {label}: {status} ({elapsed:.1f}s)\n")
        
        if alerts:
            f.write("\n**Alerts:**\n")
            for alert in alerts:
                f.write(f"- {alert}\n")
        else:
            f.write("\n**Alerts:** None\n")
        
        f.write("\n---\n")


def main():
    quick = "--quick" in sys.argv
    verbose = "--verbose" in sys.argv
    
    start_time = time.time()
    now = datetime.now()
    
    print(f"\n{'#'*72}")
    print(f"#{'':^70}#")
    print(f"#{'HAWK BOOT SEQUENCE':^70}#")
    print(f"#{'':^70}#")
    print(f"#  {now.strftime('%A, %B %d, %Y  %H:%M %Z'):^66}#")
    print(f"#{'':^70}#")
    print(f"#  War Day: 51 | Ceasefire Day: 8 | Scenario: D 82% / C 12% / B 6%  #")
    print(f"#{'':^70}#")
    print(f"{'#'*72}")
    
    results = []
    all_alerts = []
    
    for label, script_name, args, section_header, is_slow in BOOT_SEQUENCE:
        # Skip slow scripts in quick mode
        if is_slow and quick:
            print(f"\n  ⏩ Skipping {label} (--quick)")
            results.append((label, "SKIP", 0))
            continue
        
        script_path = SCRIPTS_DIR / script_name
        
        print(f"\n  ⏳ {label}...", flush=True)
        success, output, elapsed = run_script(label, script_path, args)
        
        # Extract alerts
        alerts = extract_alerts(output)
        all_alerts.extend([f"[{section_header}] {a}" for a in alerts])
        
        if verbose or not output:
            if output.strip():
                print(output)
        else:
            # Collapsed mode: show section header and alerts only
            key_markers = (
                "🔴", "🟠", "🟡", "🟢", "⚠️",
                "BREACH", "CRISIS", "STRESS", "ELEVATED",
                "ALERT", "IMMINENT", "HIGH PRIORITY",
                "Brent", "SCENARIO", "DAMAGED", "SUSPENDED"
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
    print(f"  CONSOLIDATED BRIEF")
    print(f"{'='*72}")
    
    # Show all alerts
    if all_alerts:
        print(f"\n  🔴 ALERTS ({len(all_alerts)})")
        print(f"  {'-'*60}")
        for alert in all_alerts[:10]:  # Limit to first 10
            print(f"  {alert}")
        if len(all_alerts) > 10:
            print(f"  ... and {len(all_alerts) - 10} more")
    else:
        print(f"\n  ✅ No alerts")
    
    # Script summary
    print(f"\n  SCRIPT SUMMARY")
    print(f"  {'-'*60}")
    print(f"  {'Script':<25} {'Status':>8} {'Time':>8}")
    print(f"  {'-'*45}")
    for label, status, elapsed in results:
        icon = "✅" if status == "OK" else "⏩" if status == "SKIP" else "❌"
        print(f"  {icon} {label:<23} {status:>6} {elapsed:>6.1f}s")
    
    print(f"\n  Total boot time: {total_time:.1f}s")
    
    failures = [r for r in results if r[1] == "FAIL"]
    if failures:
        print(f"\n  ⚠️  {len(failures)} script(s) failed — check output above (try --verbose).")
        save_boot_log(results, all_alerts)
        return 1
    else:
        print(f"\n  ✅ All scripts completed successfully.")
        save_boot_log(results, all_alerts)
        print(f"\n  💾 Log saved to workbook/BOOT_LOG.md")
        return 0


if __name__ == "__main__":
    sys.exit(main())
