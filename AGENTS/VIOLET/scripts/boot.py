#!/usr/bin/env python3
"""VIOLET Boot Sequence — master orchestrator.

Runs VIOLET monitoring scripts in sequence and prints a consolidated brief.
Collapsed output by default — only alert lines unless --verbose.

Flags:
  --quick     : skip non-essential checks (currently: no-op, placeholder)
  --verbose   : print full output from each subscript
  --json      : machine-readable combined result

Usage:
  .venv/bin/python3 AGENTS/VIOLET/scripts/boot.py
  .venv/bin/python3 AGENTS/VIOLET/scripts/boot.py --verbose
  .venv/bin/python3 AGENTS/VIOLET/scripts/boot.py --json
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
VIOLET_DIR = SCRIPTS_DIR.parent
WORKSPACE = VIOLET_DIR.parent.parent
VENV_PY = WORKSPACE / ".venv" / "bin" / "python3"

BOOT_SEQUENCE = [
    # (label, script, args, slow)
    ("Live thresholds + daily log", "thresholds.py", [], False),
    ("Credit gate (FRED · KB-VIO-090/096)", "fred_fetch.py", ["--summary"], True),
    ("VIX options positioning",     "vix_options.py", [], False),
    ("CFTC COT VIX positioning",    "cftc_cot.py", ["--boot"], False),
    ("JPY carry-vol canary (scope 7/11; built 7/16)", "jpy_vol.py", ["--boot"], True),
    ("OVX oil-vol→equity-vol transmission canary (built 7/17)", "ovx.py", ["--boot"], True),
    ("Cheap-tail window alert (operator decision surface; built 7/23)", "cheap_tail.py", ["--boot"], True),
    ("Catalyst countdown",          "catalyst_countdown.py", [], False),
    # Runs LAST, after every canary has written its row this session — so it audits
    # the state boot just produced, not the state it inherited. Enforces the
    # CANARY_MAP staleness contract that went unenforced from v1.0 to 2026-07-28
    # and was breaching on five rows when finally audited by hand (built 7/30).
    ("CANARY_MAP staleness contract (built 7/30)", "canary_staleness.py", ["--quiet"], False),
]

KEY_MARKERS = (
    "🔴", "🟠", "🟡", "🟣",
    "ALERT", "BREACH", "INVERSION", "COMPLACENCY",
    "REGIME SHIFT", "CRASH", "BACKWARDATION",
    "COMPLACENCY_TOP_30PCT",
    "Regime:", "M1:M2", "VVIX", "SKEW", "VIX",  # always show the core numbers
    "IMMINENT", "CHECKPOINT", "checkpoint",  # catalyst countdown markers
    "C/P OI", "top-3 call",  # VIX options markers
    "Lev Money", "lev_money", "pct3y", "FLAG:", "Open Interest", "Dealer", "Asset Mgr",  # COT markers
    "EXTREME_", "ELEVATED_",  # COT flag triggers
    "📊",  # DoD OI alert
    "CREDIT GATE", "VERDICT", "CCC", "Bin-A", "🟢",  # fred credit-gate summary (🟢 = block-lifted verdict)
    "JPY VOL", "FXY confirm",  # jpy_vol carry canary (RV spine + IV leg)
    "OVX", "oil-vol", "transmission channel", "CO-MOVE",  # ovx oil-vol→equity-vol canary
    "CHEAP-TAIL", "🟣", "ARMING", "VVIX cheap", "VIX complacency", "SKEW divergence",  # cheap-tail window alert
    "event-boxed", "OPERATOR DECISION", "Vehicle discipline", "SPREADS", "Rates-vol", "EVENT-BOXED", "Route: PROME",
    "⚠️",
    "✓ appended", "already has a row",
)


def run_script(script_path: Path, args: list[str], timeout: int = 60) -> tuple[bool, str, float]:
    if not script_path.exists():
        return False, f"SKIP: {script_path.name} not found", 0.0
    start = time.time()
    try:
        r = subprocess.run(
            [str(VENV_PY), str(script_path)] + args,
            capture_output=True, text=True, timeout=timeout, cwd=str(WORKSPACE),
        )
        elapsed = time.time() - start
        out = r.stdout
        if r.returncode != 0 and r.stderr:
            out += f"\nSTDERR: {r.stderr[:500]}"
        return r.returncode == 0, out, elapsed
    except subprocess.TimeoutExpired:
        return False, f"TIMEOUT after {time.time() - start:.0f}s", time.time() - start
    except Exception as e:
        return False, f"ERROR: {e}", time.time() - start


def collapse(output: str) -> list[str]:
    return [line for line in output.splitlines() if any(m in line for m in KEY_MARKERS)]


def main():
    verbose = "--verbose" in sys.argv
    as_json = "--json" in sys.argv
    # quick = "--quick" in sys.argv  # reserved for future

    start = time.time()
    now = datetime.now()

    if not as_json:
        bar = "═" * 70
        print(f"\n{bar}")
        print(f"  VIOLET BOOT  •  {now.strftime('%A %Y-%m-%d %H:%M')}")
        print(f"  Volatility / Term Structure Monitoring")
        print(f"{bar}")

    results = []
    combined_json = {"boot_ts": now.isoformat(timespec="seconds"), "scripts": {}}

    for label, script_name, args, _slow in BOOT_SEQUENCE:
        script_path = SCRIPTS_DIR / script_name
        if as_json:
            args_eff = args + (["--json"] if script_name == "thresholds.py" else [])
            ok, out, elapsed = run_script(script_path, args_eff)
            try:
                combined_json["scripts"][script_name] = json.loads(out) if ok else {"_error": out[:400]}
            except json.JSONDecodeError:
                combined_json["scripts"][script_name] = {"_raw": out[:400]}
            results.append((label, "OK" if ok else "FAIL", elapsed))
            continue

        print(f"\n  ⏳ {label}...", flush=True)
        ok, out, elapsed = run_script(script_path, args)
        if verbose or not out.strip():
            if out.strip():
                print(out)
        else:
            shown = collapse(out)
            if shown:
                for line in shown:
                    print(f"    {line}")
            else:
                print(f"    ✓ ran cleanly, no alerts")
        results.append((label, "OK" if ok else "FAIL", elapsed))

    total = time.time() - start

    if as_json:
        combined_json["elapsed_s"] = round(total, 2)
        combined_json["results"] = [{"label": r[0], "status": r[1], "elapsed_s": round(r[2], 2)} for r in results]
        print(json.dumps(combined_json, indent=2, default=str))
        return 0 if all(r[1] == "OK" for r in results) else 1

    print(f"\n{'─' * 70}")
    print(f"  SUMMARY")
    print(f"{'─' * 70}")
    for label, status, elapsed in results:
        icon = "✅" if status == "OK" else "❌"
        print(f"  {icon} {label:<40} {status:>5} {elapsed:>5.1f}s")
    print(f"\n  Total: {total:.1f}s  •  Daily log: AGENTS/VIOLET/workbook/VX_DAILY.tsv")
    print(f"  Tips:  --verbose for full output  •  --json for machine format\n")
    return 0 if all(r[1] == "OK" for r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
