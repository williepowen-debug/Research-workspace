#!/usr/bin/env python3
"""BOARD whole-INDEX gap check — CARL's SOLE WALTER CHANNEL.

⛔ WHY THIS IS A SCRIPT AND NOT A BOOT-CARD SENTENCE
CARL is on BOARD_CONSUMPTION_SPEC §3.5 "pull-complete recipient exemption", so
WALTER does NOT deliver to AGENTS/CARL/inbox/WALTER/. That lane is empty BY
CONSTRUCTION. §3.5.6 states the consequence verbatim:

    "delivered_but_unconsumed reading zero for CARL/RED/PROME is not evidence of
     consumption; it is a definitional consequence of the exemption."

So the whole-INDEX diff is the only channel, and — the spec's words again —
skipping it is "silent by construction": for an exempt recipient a skipped scan
and a clean scan are indistinguishable on every surface either side keeps.
RED lost two action signals to exactly this on 2026-08-12; CARL lost two on
2026-09-10/09-01 and found out only because PROME read CARL's ledgers from the
outside. A remembered ritual does not survive that. [[finding_mechanize_the_cap_not_the_ritual]]

⛔ NOTE ON THE PRIOR GATE, BECAUSE THE DIAGNOSIS MATTERED:
the card's step-5 gate was "skip when INDEX hasn't moved", keyed on INDEX.md
MTIME. That is a forbidden class under root Data Hygiene ("never key a NEW
freshness/throttle mechanism on mtime"), but it is NOT what silenced the scan:
git checkout restamps mtime to NOW, so the comparison always reads "newer" and
the gate always said RUN. It failed OPEN. The scan lapsed because nothing
MECHANICAL ran it and nothing failed when it didn't — which is why the fix is
this file (unconditional, exits nonzero) rather than a better gate.

EXIT CODES:  0 = no unrecorded action:[CARL] ids · 1 = at least one (BLOCKING)
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                           capture_output=True, text=True).stdout.strip())
INDEX = ROOT / "BOARD" / "INDEX.md"
LEDGER = ROOT / "AGENTS" / "CARL" / "board" / "BOARD_LOG.tsv"
SIG_RE = re.compile(r"SIG-W-\d{8}-\d{3}")


def logged_ids():
    if not LEDGER.exists():
        return set()
    out = set()
    for line in LEDGER.read_text(encoding="utf-8", errors="replace").splitlines()[1:]:
        cell = line.split("\t")[0].strip()
        if SIG_RE.fullmatch(cell):
            out.add(cell)
    return out


def index_rows():
    """Yield (sig_id, action_recipients, precedence, summary) per INDEX table row."""
    if not INDEX.exists():
        return
    for line in INDEX.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 6 or not SIG_RE.fullmatch(cells[0]):
            continue
        # "Action → Info" cell, e.g. "WALTER → CARL · info: HENRY, LIQUID"
        routing = cells[4]
        action = routing.split("·")[0]
        action = action.split("→", 1)[1] if "→" in action else action
        # ACTION recipients only — everything after "info:" is explicitly NOT action
        names = {n.strip().upper().strip("*_`[]") for n in re.split(r"[,/]", action)}
        yield cells[0], names, cells[3], cells[5][:90]


def main():
    have = logged_ids()
    unrecorded, action_gap = [], []
    total = 0
    for sig, action, prec, summary in index_rows():
        total += 1
        if sig in have:
            continue
        unrecorded.append(sig)
        if "CARL" in action:
            action_gap.append((sig, prec, summary))

    print("  BOARD whole-INDEX gap — CARL's SOLE WALTER channel (§3.5 exempt: lane is unfed)")
    print("  " + "-" * 68)
    print(f"  INDEX rows: {total}   ledger: {len(have)}   unrecorded: {len(unrecorded)}")

    if action_gap:
        print(f"  🔴 {len(action_gap)} UNRECORDED signal(s) carry action:[CARL] — these are OWED:")
        for sig, prec, summary in action_gap:
            print(f"      {sig}  [{prec}]  {summary}")
        print("  ⛔ Disposition each in AGENTS/CARL/board/BOARD_LOG.tsv before closeout.")
        return 1

    if unrecorded:
        print(f"  🟠 {len(unrecorded)} unrecorded, NONE with action:[CARL] — backlog, not an owed action.")
        print(f"      oldest: {unrecorded[0]}   newest: {unrecorded[-1]}")
    else:
        print("  ✅ no unrecorded ids.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
