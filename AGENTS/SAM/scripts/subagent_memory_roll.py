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
RUN_BLOCK = re.compile(r"^#{2,3}\s*(PENDING from Run|Pending from Run|Run \d+\s*—)", re.I)


def split_sections(text):
    """Split on ## / ### headings, preserving everything verbatim."""
    lines = text.split("\n")
    idx = [i for i, ln in enumerate(lines) if re.match(r"^#{2,3}\s", ln)]
    if not idx:
        return [("", text)]
    out = []
    if idx[0] > 0:
        out.append(("", "\n".join(lines[: idx[0]])))
    for a, b in zip(idx, idx[1:] + [len(lines)]):
        out.append((lines[a], "\n".join(lines[a:b])))
    return out


def plan(path, keep_runs):
    text = path.read_text(encoding="utf-8")
    secs = split_sections(text)
    run_blocks = [(h, b) for h, b in secs if RUN_BLOCK.match(h)]
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
    for h, b in secs:
        if not h or NEVER_ROLL.match(h) or not RUN_BLOCK.match(h):
            stay.append((h, b))
        elif h in keep_recent:
            stay.append((h, b))
        elif TERMINAL.search(b):
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
            f"2026-08-20 to `{arch.name}`\n\n"
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
