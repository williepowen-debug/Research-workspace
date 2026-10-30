#!/usr/bin/env python3
"""
REGINALD Boot Sequence
Master orchestrator — runs all monitoring scripts in sequence.
Single command replaces the multi-step manual boot.

Usage:
  .venv/bin/python3 AGENTS/REGINALD/scripts/boot.py
  .venv/bin/python3 AGENTS/REGINALD/scripts/boot.py --skip-slow   # skip EDGAR queries (insider, 8k)
  .venv/bin/python3 AGENTS/REGINALD/scripts/boot.py --check-only  # verification run: no script writes any tracked file
                                                                  # (only kre_float.py writes state; it gets --no-state)

Exit code (2026-10-22, D:L793): 0 = every leg read cleanly · 1 = at least one ALERT · 2 = any FAIL or INCOMPLETE.
Built-in legs (no subprocess) added 2026-10-22: inbox lanes (general + WALTER, BOARD_LOG-aware) ·
peer pair channels (WAL, OZK: entries newer than REGINALD's latest ACK; WQ-484) · prediction resolve-by
(registry/PREDICTION_RESOLVE_BY.tsv vs OPEN rows in workbook/PREDICTIONS.tsv).
"""
import csv
import re
from datetime import date

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
TRI_STATE = {"Thresholds", "Insider Activity", "8-K Monitor", "Earnings Countdown", "Corrections Check", "FLG Ladder",
             "Ledger Staleness", "Trade-Surface Staleness"}
DESK = SCRIPTS_DIR.parent  # AGENTS/REGINALD

# Boot sequence: (name, script_path, category, slow)
BOOT_SEQUENCE = [
    ("Market Prices",      MARKET_PY,                          "PRICES",    False),
    # Dark Pool + Short Vol and Short Interest removed 2026-10-22: their ledgers are FROZEN (2026-06-27, 0 consumers)
    # and PROME marked the READS rows RETIRED-2026-10-22 (ed5e51ea6). Scripts kept in place, not deleted.
    ("Thresholds",         SCRIPTS_DIR / "thresholds.py",      "ALERTS",    False),
    ("KRE Float",          SCRIPTS_DIR / "kre_float.py",       "STRUCTURE", False),
    ("Earnings Countdown", SCRIPTS_DIR / "earnings_countdown.py", "CALENDAR", False),
    ("Insider Activity",   SCRIPTS_DIR / "insider.py",         "EDGAR",     True),
    ("8-K Monitor",        SCRIPTS_DIR / "8k_monitor.py",      "EDGAR",     True),
    # 2026-10-22: charter checks that were manual-only. (name, path, category, slow, args)
    ("FLG Ladder",         SCRIPTS_DIR / "vx_ladder_check.py", "ALERTS",    False, []),
    ("Corrections Check",  WORKSPACE / "scripts" / "corrections_boot_check.py", "R1", False, ["REGINALD"]),
    ("Ledger Staleness",   WORKSPACE / "scripts" / "ledger_staleness.py", "HYGIENE", False, ["REGINALD", "--quiet"]),
    ("Trade-Surface Staleness", WORKSPACE / "scripts" / "ledger_staleness.py", "HYGIENE", False, ["REGINALD", "--trade", "--quiet"]),
]


def run_script(name, script_path, timeout=120, args=()):
    """Run a script and capture output. Returns (returncode, output, elapsed)."""
    if not script_path.exists():
        return None, f"  MISSING: {script_path.name} not found", 0

    start = time.time()
    try:
        result = subprocess.run(
            [str(VENV_PYTHON), str(script_path), *args],
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


def check_inbox():
    """List open packets in inbox/ and inbox/WALTER/ (processed/ excluded); WALTER items marked NEW unless logged."""
    logged = set()
    log = DESK / "board" / "BOARD_LOG.tsv"
    if log.exists():
        logged = {l.split("\t", 1)[0] for l in log.read_text().splitlines()}
    lines, new = [], 0
    for f in sorted((DESK / "inbox").glob("*.md")):
        lines.append(f"  📥 general  {f.name}")
        new += 1
    for f in sorted((DESK / "inbox" / "WALTER").glob("*.md")):
        m = re.search(r"SIG-W-\d{8}-\d{3}", f.read_text(errors="replace"))
        sig = m.group(0) if m else "?"
        tag = "logged-not-filed" if sig in logged else "NEW"
        new += tag == "NEW"
        lines.append(f"  📥 WALTER   {sig} {tag}  {f.name}")
    out = "\n".join(lines) if lines else "  inbox lanes empty (general + WALTER)"
    return (1 if new else 0), out


def check_channels():
    """WQ-484: OZK -> REGINALD and WAL -> REGINALD are directed edges. Report peer entries above REGINALD's latest ACK."""
    out, unacked = [], 0
    for peer in ("WAL", "OZK"):
        f = DESK.parent / peer / "REGINALD_CHANNEL.md"
        if not f.exists():
            out.append(f"  ❓ {peer} channel missing: {f}")
            unacked += 1
            continue
        text = f.read_text(errors="replace")
        entries = re.split(r"\n(?=## \d{4}-\d{2}-\d{2})", text)[1:]
        pending = []
        for e in entries:  # newest first by channel convention
            if "ACK — REGINALD" in e:
                break
            head = e.splitlines()[0]
            if "FROM: REGINALD" not in head and "REGINALD →" not in head:
                pending.append(head[3:80])
        unacked += len(pending)
        out.append(f"  {'🔔' if pending else '✅'} {peer}: {len(pending)} entr{'y' if len(pending) == 1 else 'ies'} above REGINALD's latest ACK")
        out += [f"       - {h}" for h in pending]
    return (1 if unacked else 0), "\n".join(out)


def check_predictions():
    """OPEN rows in PREDICTIONS.tsv vs registry/PREDICTION_RESOLVE_BY.tsv: past date -> ALERT; missing -> INCOMPLETE."""
    preds = DESK / "workbook" / "PREDICTIONS.tsv"
    side = DESK / "registry" / "PREDICTION_RESOLVE_BY.tsv"
    if not preds.exists() or not side.exists():
        return 2, "  MISSING predictions ledger or resolve-by sidecar"
    rows = [r for r in csv.reader(preds.open(), delimiter="\t") if r and not r[0].startswith("#")]
    hdr = rows[0]
    open_ids = [r[0] for r in rows[1:] if len(r) == len(hdr) and "OPEN" in r[hdr.index("Status")]]
    srows = [r for r in csv.reader(side.open(), delimiter="\t") if r and not r[0].startswith("#")]
    due = {r[0]: r[1] for r in srows[1:]}
    today = date.today().isoformat()
    out, worst = [], 0
    for pid in open_ids:
        if pid not in due:
            out.append(f"  ⚠️  {pid} OPEN with no Resolve_By row (INCOMPLETE)")
            worst = 2
        elif due[pid] < today:
            out.append(f"  🔔 {pid} OPEN past Resolve_By {due[pid]}: grade it (ALERT)")
            worst = max(worst, 1)
        else:
            out.append(f"  ✅ {pid} OPEN, resolve by {due[pid]}")
    return worst, "\n".join(out) or "  no OPEN predictions"


BUILTINS = [("Inbox Lanes", check_inbox), ("Peer Channels (WQ-484)", check_channels),
            ("Prediction Resolve-By", check_predictions)]


def main():
    skip_slow = "--skip-slow" in sys.argv
    check_only = "--check-only" in sys.argv
    if check_only:
        print("  CHECK-ONLY run: kre_float.py gets --no-state; no tracked file is written by this boot.")
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

    for item in BOOT_SEQUENCE:
        name, script_path, category, is_slow = item[:4]
        args = list(item[4]) if len(item) > 4 else []
        if check_only and script_path.name == "kre_float.py":
            args.append("--no-state")
        if is_slow and skip_slow:
            print(f"\n  ⏩ Skipping {name} (--skip-slow)")
            results.append((name, "SKIP", 0))
            continue

        print(f"\n  ⏳ Running {name}...", flush=True)
        rc, output, elapsed = run_script(name, script_path, args=args)

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

    for name, fn in BUILTINS:
        print(f"\n  ⏳ Checking {name}...", flush=True)
        t0 = time.time()
        try:
            rc, output = fn()
        except Exception as e:  # a broken check is a FAIL, never a silent pass
            rc, output = 3, f"  ERROR: {e}"
        print(output)
        results.append((name, {0: "OK", 1: "ALERT", 2: "INCOMPLETE"}.get(rc, "FAIL"), time.time() - t0))

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
    if by["FAIL"] or by["INCOMPLETE"]:
        return 2
    return 1 if by["ALERT"] else 0


if __name__ == "__main__":
    sys.exit(main())
