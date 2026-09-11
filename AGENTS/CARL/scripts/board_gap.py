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
freshness/throttle mechanism on mtime"). A checkout can refresh mtime when it
rewrites a file, but does not rewrite every unchanged file. The historical gate
decisions were not recorded: neither "always RUN" nor "the silencer" is proven.
Sparse receipt dates establish a gap in recorded processing. This unconditional
check removes the dependency on remembering the manual comparison.

EXIT CODES:  0 = no unrecorded action:[CARL] ids · 1 = at least one (BLOCKING)
             2 = input missing, malformed, or INDEX differs from BOARD records
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
INDEX = ROOT / "BOARD" / "INDEX.md"
LEDGER = ROOT / "AGENTS" / "CARL" / "board" / "BOARD_LOG.tsv"
SIG_RE = re.compile(r"SIG-W-\d{8}-\d{3}")


def logged_ids():
    if not LEDGER.exists():
        raise ValueError(f"missing receipt ledger: {LEDGER}")
    lines = LEDGER.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].split("\t")[0].strip().lower() != "signal_id":
        raise ValueError(f"invalid receipt ledger header: {LEDGER}")
    out = set()
    for line in lines[1:]:
        cell = line.split("\t")[0].strip()
        if SIG_RE.fullmatch(cell):
            out.add(cell)
    return out


def action_names(action):
    """Legacy routes annotate desk names in parentheses; annotations are not desks."""
    action = re.sub(r"\([^)]*\)", "", action)
    return {name for n in re.split(r"[,/]", action)
            if (name := n.strip().upper().strip("*_`[]"))}


def index_rows():
    """Yield (sig_id, action_recipients, precedence, summary) per INDEX table row."""
    if not INDEX.exists():
        raise ValueError(f"missing BOARD index: {INDEX}")
    for line in INDEX.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells or not SIG_RE.fullmatch(cells[0]):
            continue
        if len(cells) < 6:
            raise ValueError(f"truncated BOARD index row: {cells[0]}")
        # "Action → Info" cell, e.g. "WALTER → CARL · info: HENRY, LIQUID"
        routing = cells[4]
        action = routing.split("·")[0]
        action = action.split("→", 1)[1] if "→" in action else action
        # ACTION recipients only — everything after "info:" is explicitly NOT action
        names = action_names(action)
        yield cells[0], names, cells[3], cells[5][:90]


def load_board_signals():
    # Use the publisher's parser, including its legacy frontmatter support.
    sys.path.insert(0, str(ROOT / "AGENTS/WALTER/tools"))
    from gen_board_index import load_signals
    signals, errors = load_signals()
    if errors or not signals:
        raise ValueError("BOARD source unavailable or malformed: " + "; ".join(errors[:3]))
    return signals


def main():
    try:
        have = logged_ids()
        rows = list(index_rows())
        if not rows:
            raise ValueError("empty or unparseable BOARD index")
        indexed = {sid: (action, prec) for sid, action, prec, _ in rows}
        if len(indexed) != len(rows):
            raise ValueError("duplicate BOARD index signal IDs")
        signals = load_board_signals()
        expected = {sid: (action_names(", ".join(row["action"])), row["precedence"])
                    for sid, row in signals.items()}
        if indexed != expected:
            raise ValueError("INDEX is stale or differs from BOARD signal IDs/routing/precedence; publisher regeneration needed")
    except (OSError, ValueError, ImportError) as exc:
        print(f"  🔴 BOARD GAP UNKNOWN: {exc} — cannot certify consumption")
        return 2
    unrecorded, action_gap = [], []
    total = 0
    for sig, action, prec, summary in rows:
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
        print(f"  🟠 {len(unrecorded)} unrecorded, NONE with action:[CARL] — no explicit CARL routing gap; relevance/disposition review remains separate.")
        print(f"      oldest: {min(unrecorded)}   newest: {max(unrecorded)}")
    else:
        print("  ✅ no unrecorded ids.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
