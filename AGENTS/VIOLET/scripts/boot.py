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
    ("Credit gate (FRED · KB-VIO-096 block; BIN-A STUCK)", "fred_fetch.py", ["--summary"], True),
    ("VIX options positioning",     "vix_options.py", [], False),
    ("CFTC COT VIX positioning",    "cftc_cot.py", ["--boot"], False),
    # MOVE has an OWNER now. `CANARY_MAP.md` has carried "investing.com primary;
    # yf ^MOVE unreliable as sole source" as PROSE since 7/30 with no script
    # implementing it — so every read went through the source the map already
    # called unreliable, and I carried "confirm-3 BROKEN" for five sessions while
    # MOVE was above its line every one of them (KB-VIO-177). Built 8/4.
    # --strict added 2026-09-04 (DAEDALUS 🔴#5c): without it move.py returns 0
    # even when the investing.com PRIMARY fails and it falls back to the labelled
    # cross-check, so a primary outage read as a clean stage on the boot path.
    ("MOVE rates-vol (investing.com PRIMARY; built 8/4)", "move.py", ["--boot", "--strict"], True),
    ("JPY carry-vol canary (scope 7/11; built 7/16)", "jpy_vol.py", ["--boot"], True),
    ("OVX oil-vol→equity-vol transmission canary (built 7/17)", "ovx.py", ["--boot"], True),
    ("Cheap-tail window alert (operator decision surface; built 7/23)", "cheap_tail.py", ["--boot"], True),
    ("Implied correlation (KB-VIO-126 mechanism; built 7/30)", "implied_corr.py", ["--boot"], False),
    ("Catalyst countdown",          "catalyst_countdown.py", [], False),
    # Runs LAST, after every canary has written its row this session — so it audits
    # the state boot just produced, not the state it inherited. Enforces the
    # CANARY_MAP staleness contract that went unenforced from v1.0 to 2026-07-28
    # and was breaching on five rows when finally audited by hand (built 7/30).
    ("CANARY_MAP staleness contract (built 7/30)", "canary_staleness.py", ["--quiet"], False),
    # VX_DAILY session completeness (built 9/6). `ledger_staleness.py` measures
    # VINTAGE, NOT GAPS — a ledger whose newest row is today passes it with any
    # number of holes behind that row. On 2026-09-06 four sessions were missing
    # (8/28 · 8/31 · 9/1 · 9/3), inside the live RED-FT-10 window, past every
    # green boot check. FT-10 counts CONSECUTIVE bars, so a hole in this ledger
    # is indistinguishable from a bar that reset the chain.
    ("VX_DAILY session completeness (built 9/6)", "vx_daily_gapcheck.py", ["--quiet"], False),
    # KB schema conformance. SCHEMA.tsv declared the KB's enums on 2026-04-12 and
    # nothing ever checked them — write-back step 8 said "validate enums against
    # SCHEMA.tsv", a ritual with no mechanism (KB-VIO-165). First run found 11
    # violating rows, one unchallenged for 109 days.
    ("KB schema conformance (built 7/30 PM)", "validate_workbook.py", ["--boot"], False),
    # Catalyst notes are what boot PRINTS at the moment a prediction resolves, and
    # nothing ever checked them — 4 instances by 8/4, one of which cited a
    # RETRACTED forward beta on the next prediction due (KB-VIO-169). Built 8/4.
    ("Grading-note citations (built 8/4)", "grading_note_check.py", ["--boot"], False),
    # ADVISORY. v3.8 asserted "the family closes at five fields" while my own
    # STATUS asserted a sixth, same day — and no check in this agent could see it,
    # because a missed thesis bump ages nothing and reddens nothing. Built 8/4.
    ("Thesis currency (advisory; built 8/4)", "thesis_bump_check.py", ["--boot"], False),
    # F-B is a falsifier this desk registered against its OWN cheap-vol verdict,
    # pre-CPI, with nothing riding on it. A registered prediction whose resolver
    # nobody runs is graded by whoever remembers it, which is how the 8/5 SOQ
    # grade went 13 days late (KB-VIO-196). Wired at boot so the 9/16 grade is
    # mechanical. Prints progress before the window closes; harmless after.
    ("F-B falsifier (SPX realized vs 17.84% implied; built 9/11)", "fb_grade.py", [], False),
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
    "MOVE [", "PRIMARY investing.com", "CROSS-CHECK", "UNCORROBORATED", "F1 (KB-VIO-116)", "confirm-3",  # move.py
    "GRADING-NOTE", "thesis 3", "retraction",  # grading-note + thesis-currency checks
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
            elif not ok:
                # Silent AND failed: the quietest possible failure. Say so.
                print(f"    ⚠️  STAGE FAILED (non-zero exit) and produced NO OUTPUT")
        else:
            shown = collapse(out)
            if shown:
                for line in shown:
                    print(f"    {line}")
            elif ok:
                print(f"    ✓ ran cleanly, no alerts")
            else:
                # ⚠️ WAS an unconditional clean line (DAEDALUS 🔴#5b): a stage that
                # exited non-zero but printed nothing this collapser recognised was
                # reported as "ran cleanly". A crash with no known marker is the
                # case most in need of a loud line, and it got the quietest one.
                print(f"    ⚠️  STAGE FAILED (non-zero exit), no recognised markers "
                      f"— output not understood by the collapser; re-run this "
                      f"stage directly before trusting anything downstream of it")
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
