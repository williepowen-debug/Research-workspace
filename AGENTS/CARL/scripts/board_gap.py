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

⛔ NOTE ON THE PRIOR GATE — AND A RETRACTION, because I got the mechanism wrong
and said so in a commit message and to two other desks:

The card's step-5 gate was "skip when INDEX hasn't moved", keyed on INDEX.md
MTIME. That IS a forbidden class under root Data Hygiene ("never key a NEW
freshness/throttle mechanism on mtime") — that part stands.

⛔ I ALSO CLAIMED it "always said RUN" and "failed OPEN", reasoning that git
restamps mtime to NOW. THAT CLAIM IS RETRACTED AND WAS NOT MINE TO MAKE.
Git only writes files whose content it needs to change, so an unchanged
INDEX.md keeps its old mtime; and sparse Date_Logged receipts (7/31, 8/10,
8/12, 8/15, 9/1, 9/11) cannot distinguish "the gate skipped" from "the step was
never run". THE GATE'S ACTUAL BEHAVIOUR IS UNDETERMINED BY THE EVIDENCE I HAD.
I corrected PROME's diagnosis using this, which means I propagated an
overstated claim while correcting someone else's — caught by external review.

WHAT SURVIVES, and it is all the remedy needs: the step is an every-boot
obligation whose receipts show six passes in six weeks, nothing MECHANICAL ran
it, and nothing FAILED when it didn't. That is sufficient to justify replacing
it with an unconditional, fail-closed check regardless of what the gate did.
[[finding_mechanize_the_cap_not_the_ritual]]

EXIT CODES:  0 = clean · 1 = unrecorded action:[CARL] id(s) · 2 = CANNOT READ INPUT\n             (2 fails CLOSED: a guard that cannot see its input must not report clean)
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


def action_names(routing):
    """ACTION recipients from the 'Action → Info' cell.

    ⛔ Everything after 'info:' is explicitly NOT an action recipient.
    ⛔ Parentheticals MUST be stripped: 'CARL (ACTION)' occurs 26x in the live
    INDEX and the first version of this parser matched none of them, because it
    only stripped markup characters. The bug cost no live signal (all 26 were
    already logged) but the check was reporting a coverage it did not have.
    Found by an external review, not by my own two negative tests — those
    exercised a missing LEDGER ROW and never a malformed INPUT.
    """
    action = routing.split("·")[0]
    action = action.split("info:")[0]
    action = action.split("→", 1)[1] if "→" in action else action
    action = re.sub(r"\([^)]*\)", " ", action)          # drop "(ACTION)", "(lead)", …
    action = re.sub(r"[*_`\[\]]", " ", action)           # drop markdown emphasis
    return {n.strip().upper() for n in re.split(r"[,/;]|\band\b", action) if n.strip()}

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
        yield cells[0], action_names(cells[4]), cells[3], cells[5][:90]


def closeout_line():
    """Emit the §3.5.6 option (b) closeout self-assertion, verbatim TERRY wording.

    The unconditional scan is the PULL; this line is its ARTIFACT. It exists
    because for a §3.5-exempt desk a skipped scan and a clean scan are otherwise
    indistinguishable on every surface either side keeps — so "no complaint" is
    not evidence. PROME's exempt_gap.py remains the CONTROL; this is a rider.

    ⛔ This line asserts the scan RAN and what it SAW. It does NOT assert the
    signals were substantively reviewed — a logged id is a receipt, not a read.
    """
    have = logged_ids()
    ids = [sig for sig, _, _, _ in index_rows()]
    last = max(have) if have else "(none)"
    new_since = [i for i in ids if i > last]
    print(f"BOARD scan run, {len(new_since)} new since {last}, {len(have)} logged")
    return 0


def main():
    # ⛔ FAIL CLOSED. The first version returned 0 ("✅ no unrecorded ids") when
    # BOARD/INDEX.md was missing OR empty — a guard reporting CLEAN when it cannot
    # see its own input, which is strictly worse than no guard because it stops
    # anyone looking. [[finding_instrument_reports_clean_against_the_wrong_reference]]
    if not INDEX.exists():
        print(f"  🔴 BOARD GAP CHECK CANNOT RUN — {INDEX} does not exist.")
        print("  ⛔ This is NOT 'no gap'. Failing closed.")
        return 2
    if not INDEX.read_text(encoding="utf-8", errors="replace").strip():
        print(f"  🔴 BOARD GAP CHECK CANNOT RUN — {INDEX} is empty.")
        print("  ⛔ This is NOT 'no gap'. Failing closed.")
        return 2
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

    if total == 0:
        print("  🔴 INDEX parsed to ZERO signal rows — the format changed or the file is")
        print("     truncated. ⛔ This is NOT 'no gap'. Failing closed.")
        return 2

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
    if "--closeout" in sys.argv:
        sys.exit(closeout_line())
    sys.exit(main())
