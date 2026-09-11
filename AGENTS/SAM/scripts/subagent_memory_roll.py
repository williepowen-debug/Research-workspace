#!/usr/bin/env python3
"""Roll TERMINAL run-history out of a sub-agent state file into its archive.

WHY THIS EXISTS (2026-08-20, Will-directed)
-------------------------------------------
SAM's own surfaces are capped -- STATUS.md 250 lines, MEMORY.md 100 -- because
unbounded accumulation drowns signal. SAM's SUB-AGENTS had no equivalent rule,
and nobody noticed until the cost was measured:

    METSUKE  spec  20K + memory 370K = ~100K TOKENS read before any work
    KURA     spec 158K + memory 176K =  ~85K TOKENS
    KOYOMI   spec  17K + memory 119K =  ~35K TOKENS

A METSUKE spawn was spending roughly a third of a context window reading its own
history before it looked at a single artifact.

The failure was not the WRITE step -- that always worked. It was that the
closeout had a WRITE step and no PRUNE step, so `PENDING from Run N` blocks and
per-run LAST RUN entries accumulated forever. The bill came due on 2026-08-20
when METSUKE's PENDING was found holding 97 open items, most of them made moot
by a ruling issued 13 days earlier, surviving 14 runs because nothing in the
closeout ever asked "what does this ruling close?"

DESIGN RULES (deliberate, do not relax)
---------------------------------------
1. MOVE, NEVER DELETE. Every rolled block is appended verbatim to the archive.
   The script verifies byte conservation and refuses to write if content is lost.
2. TERMINAL ONLY. A block rolls only if it is explicitly marked closed/cleared/
   resolved. An unmarked block is treated as LIVE and stays -- silence is never
   read as closure.
3. ARCHIVES ARE NOT BOOT-READ. The working file keeps a pointer; the archive is
   reference-only, the same split SAM already uses for PREDICTIONS_ARCHIVE.md,
   timeline/ARCHIVE.md and KB_ARCHIVE.tsv.
4. REPORT-ONLY BY DEFAULT. --apply is required to write. The sub-agent PROPOSES
   the roll; SAM rules -- the propose-only pattern used everywhere else here.

Usage:
    subagent_memory_roll.py <state-file> [--apply] [--keep-runs N]
    subagent_memory_roll.py --all            # report on all three
"""
import argparse
import datetime as _dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SAM = ROOT / "AGENTS" / "SAM"

TARGETS = [
    SAM / "docket" / "KOYOMI_MEMORY.md",
    SAM / "METSUKE_MEMORY.md",
    SAM / "workbook" / "KURA_MEMORY.md",
]

def _today():
    """The roll date, READ FROM THE CLOCK.

    🔴 This was the literal string "2026-08-20" until 2026-09-11 — the date this tool
    was BUILT — so every pointer stub it ever wrote claimed the file was rolled on the
    build date. 8 of 9 stubs fleet-wide were wrong; the one correct stamp was hand-written.
    A stamp that cannot be right except on one day is worse than no stamp, because it
    looks like provenance. Found by KURA's self-audit 2026-09-11.
    """
    return _dt.date.today().isoformat()


# A block is TERMINAL only on an explicit closure marker. Silence != closed.
TERMINAL = re.compile(
    r"CLOSED|CLEARED|RESOLVED-BY-RULING|ALL\s+(NINE|\d+)\s+ITEMS|MOOT-BY-BANNER"
    r"|ALREADY-APPLIED|✅\s*\*\*(ALL|CLOSED|CLEARED)|⚰️\s*CLOSED",
    re.I,
)
# Sections that are the LIVE working set and never roll, whatever they contain.
NEVER_ROLL = re.compile(
    r"^#{2,3}\s*(CHANGES SINCE|STANDING MONITORS|CALIBRATION|NEXT RUN HINTS"
    r"|PENDING \(escalations)",
    re.I,
)
# Per-run history blocks that are candidates to roll.
RUN_BLOCK = re.compile(
    r"^#{2,3}\s*(?:[^\w\s#]\uFE0F?\s*)*(PENDING from Run|Pending from Run|Run \d+\s*—)", re.I
)  # leading-emoji tolerant: "### 🆕 Run 21 …" was previously unreachable entirely

# A PENDING block specifically must DECLARE its closure IN ITS HEADING.
#
# 🔴 WHY THIS IS NARROWER THAN TERMINAL (2026-09-11, found via METSUKE Run 20 E2):
# TERMINAL is searched over a block's whole body, and a PENDING block's body is exactly
# where someone writes ABOUT a missing marker. `## PENDING from Run 18` contained only
# sentences like "Run-19 E1 asked for the CLOSED marker; it has not been written" and
# "Mark that section CLOSED after recording these artifact references" — i.e. the block
# said IT IS NOT CLOSED, and the scanner read it as closed because the word appeared.
# METSUKE had flagged it unmarked for three consecutive runs while this tool scored it
# terminal; it was spared only by --keep-runs. Class:
# [[finding_marker_word_in_prose_disables_the_scanner_that_reads_for_it]].
#
# ⛔ AND WHY IT IS *ONLY* PENDING BLOCKS. Applying heading-anchoring to run-history
# blocks too was tried first and reclassified 16 blocks across all three files: a run
# narrative legitimately discusses closures, and run blocks roll on RECENCY, not on a
# marker. That version failed in the useless direction — nothing would ever roll. The
# defect is specific to the one block type whose subject matter is its own closure.
PENDING_BLOCK = re.compile(r"^#{2,3}\s*(PENDING from Run|Pending from Run)", re.I)


def is_terminal(heading, body):
    """PENDING blocks: closure must be declared in the HEADING. Others: body-wide."""
    if PENDING_BLOCK.match(heading):
        return bool(TERMINAL.search(heading))
    return bool(TERMINAL.search(body))


def split_sections(text):
    """Split on ## / ### headings, preserving everything verbatim.

    Returns (heading, body, parent_h2) — the PARENT matters, see classify().
    """
    lines = text.split("\n")
    idx = [i for i, ln in enumerate(lines) if re.match(r"^#{2,3}\s", ln)]
    if not idx:
        return [("", text, "")]
    out = []
    if idx[0] > 0:
        out.append(("", "\n".join(lines[: idx[0]]), ""))
    parent = ""
    for a, b in zip(idx, idx[1:] + [len(lines)]):
        h = lines[a]
        if re.match(r"^##\s", h):
            parent = h
        out.append((h, "\n".join(lines[a:b]), parent))
    return out


def classify(heading, body, parent):
    """Return ('roll'|'stay', why).

    🔴 CONTAINMENT BEATS SPELLING (2026-09-11, KOYOMI self-audit, predicted then verified).
    A '###' block inside a NEVER_ROLL parent is a PENDING sub-block whatever it is CALLED.
    '### Run 20 — current dispositions' is a LIVE pending block merely NAMED like run
    history: RUN_BLOCK matched it, the PENDING_BLOCK spelling rule did not, so closure was
    judged body-wide and its body contains the word "CLOSED". It was one --keep-runs slot
    from being archived while live. KOYOMI predicted this as a dated, falsifiable claim and
    a direct test of the code confirmed it.
    The same rule recovers the opposite failure: '### ✅ CLOSED by KOYOMI itself this run'
    blocks under the PENDING parent were unreachable because RUN_BLOCK cannot skip a leading
    emoji, leaving tens of KB of explicitly-closed material permanently unrollable while the
    dry run reported "nothing terminal to roll".
    """
    if not heading:
        return "stay", "preamble"
    in_never_roll_parent = bool(NEVER_ROLL.match(parent)) if parent else False
    if re.match(r"^###\s", heading) and in_never_roll_parent:
        # Pending sub-block: rolls ONLY if its OWN HEADING declares closure.
        if TERMINAL.search(heading):
            return "roll", f"closed in heading, under {parent[:38]}"
        return "stay", "pending sub-block (no closure in heading)"
    if NEVER_ROLL.match(heading) or not RUN_BLOCK.match(heading):
        return "stay", "never-roll or not a run block"
    return None, None  # caller applies the existing run-block logic


def plan(path, keep_runs):
    text = path.read_text(encoding="utf-8")
    secs = split_sections(text)
    # Only TOP-LEVEL run blocks compete for the --keep-runs window. A '###' block inside a
    # NEVER_ROLL parent is a pending sub-block and is judged by classify(), not by recency.
    run_blocks = [(h, b) for h, b, par in secs
                  if RUN_BLOCK.match(h) and not (re.match(r"^###\s", h) and par and NEVER_ROLL.match(par))]
    # ⚠️ DO NOT keep "the last N in FILE ORDER". Sub-agents differ: METSUKE writes
    # its run history oldest-first, KURA newest-first. On 2026-08-20 the file-order
    # version proposed archiving KURA's Run 12 -- THAT DAY'S RUN -- because it sat
    # at the top. Caught only because this tool is report-only by default.
    # Keep the highest RUN NUMBERS, parsed from the heading, order-independent.
    def run_no(h):
        m = re.search(r"Run\s+(\d+)", h, re.I)
        return int(m.group(1)) if m else -1
    newest = sorted({run_no(h) for h, _ in run_blocks if run_no(h) >= 0}, reverse=True)[:keep_runs]
    keep_recent = {h for h, _ in run_blocks if run_no(h) in newest} if keep_runs else set()

    roll, stay = [], []
    for h, b, par in secs:
        verdict, _why = classify(h, b, par)
        if verdict == "roll":
            roll.append((h, b)); continue
        if verdict == "stay":
            stay.append((h, b)); continue
        # top-level run block: existing recency + closure-marker logic
        if h in keep_recent:
            stay.append((h, b))
        elif is_terminal(h, b):
            roll.append((h, b))
        else:
            stay.append((h, b))  # unmarked => LIVE, by rule 2
    return text, stay, roll


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("state_file", nargs="?")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--keep-runs", type=int, default=3,
                    help="always keep the N most recent run blocks in the live file")
    a = ap.parse_args()

    files = TARGETS if a.all or not a.state_file else [Path(a.state_file).resolve()]
    total_saved = 0

    for path in files:
        if not path.exists():
            print(f"  🔴 missing: {path}")
            continue
        text, stay, roll = plan(path, a.keep_runs)
        rolled_bytes = sum(len(b) for _, b in roll)
        print(f"\n── {path.relative_to(SAM)}")
        print(f"   now: {len(text.splitlines()):>5} lines  {len(text)/1024:>6.0f}K")
        if not roll:
            print("   ✅ nothing terminal to roll")
            continue
        for h, b in roll:
            print(f"      roll → {h[:64]:<64} {len(b.splitlines()):>4} lines")
        new_live = "\n".join(b for _, b in stay)
        print(f"   after: {len(new_live.splitlines()):>4} lines  {len(new_live)/1024:>6.0f}K"
              f"   (−{rolled_bytes/1024:.0f}K, −{100*rolled_bytes/len(text):.0f}%)")
        total_saved += rolled_bytes

        if not a.apply:
            continue

        arch = path.with_name(path.stem + "_ARCHIVE.md")
        header = (
            f"# {path.stem} — ARCHIVE\n\n"
            "> **Reference only. NOT read at boot.** Terminal run-history rolled out of "
            f"`{path.name}` so the live file stays a working set rather than a ledger.\n"
            "> **Nothing here was deleted — every block is verbatim.** A block reaches this "
            "file only when it carries an explicit closure marker; unmarked blocks stay live "
            "by rule, because silence is never read as closure.\n"
            "> Rolled by `scripts/subagent_memory_roll.py`.\n\n---\n"
        )
        prev = arch.read_text(encoding="utf-8") if arch.exists() else header
        arch.write_text(prev + "\n" + "\n".join(b for _, b in roll) + "\n", encoding="utf-8")

        pointer = (
            f"\n## ↪️ ARCHIVED RUN HISTORY — {len(roll)} terminal block(s) rolled "
            f"{_today()} to `{arch.name}`\n\n"
            "**Moved, not deleted; verbatim; reference-only and NOT boot-read.** Every block "
            "carried an explicit closure marker at the time of the roll. **If you need a "
            "historical disposition, read the archive — do not re-open it here.**\n"
        )
        path.write_text(new_live.rstrip("\n") + "\n" + pointer, encoding="utf-8")

        # rule 1: byte conservation
        after = len(path.read_text(encoding="utf-8")) + len(arch.read_text(encoding="utf-8"))
        before = len(text) + len(prev)
        if after < before - len(pointer) - len(header):
            print("   🔴 BYTE CONSERVATION FAILED — investigate before trusting this run")
            sys.exit(1)
        print(f"   ✅ applied · archive {arch.name} · byte-conservation OK")

    if not a.apply and total_saved:
        print(f"\n  report-only. --apply to write. would free ~{total_saved/1024:.0f}K "
              f"(~{total_saved/4/1000:.0f}K tokens per spawn)")


if __name__ == "__main__":
    main()
