#!/usr/bin/env python3
"""regen_patterns_hot.py — regenerate PATTERNS_HOT.md from PATTERNS.tsv.

The hot index is the BOOT-READ half of the 2026-08-17 hot/cold split (self-audit
F37/B0: the boot spine exceeded the single-Read cap, so SPAWN step 3 now reads
the ~21KB index, and full rows are pulled from PATTERNS.tsv by ID on demand).
Run after ANY PATTERNS.tsv change. Conservation-checked: hot line count must
equal cold row count or this dies loud (rc=2, CHECK_STANDARD §9).

Usage: python3 "$(git rev-parse --show-toplevel)/AGENTS/DAEDALUS/scripts/regen_patterns_hot.py"
"""
import os
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
COLD = os.path.normpath(os.path.join(HERE, "..", "PATTERNS.tsv"))
HOT = os.path.normpath(os.path.join(HERE, "..", "PATTERNS_HOT.md"))


def main():
    try:
        lines = open(COLD, encoding="utf-8").read().splitlines()
    except OSError as e:
        print(f"🔴 regen_patterns_hot CANNOT-CERTIFY: {e}")
        return 2
    rows = [l for l in lines[1:] if l.strip() and not l.startswith("#")]
    hot = []
    for l in rows:
        f = l.split("\t")
        if len(f) != 7:
            print(f"🔴 regen_patterns_hot CANNOT-CERTIFY: ragged row {f[0]!r} ({len(f)} fields) — fix PATTERNS.tsv first")
            return 2
        head = " ".join(f[2].split())
        hot.append(f"- **{f[0]}** ({f[1]}, {f[3]}/{f[5]}) — {head[:150]}{'…' if len(head) > 150 else ''}")
    if len(hot) != len(rows):
        print(f"🔴 regen_patterns_hot CANNOT-CERTIFY: conservation FAIL hot={len(hot)} cold={len(rows)}")
        return 2
    doc = ["# PATTERNS — HOT INDEX (GENERATED — do not hand-edit; regenerate via scripts/regen_patterns_hot.py)",
           f"> One line per pattern; full sourced rows in `PATTERNS.tsv` (cold). Boot reads THIS file "
           f"(425KB-spine fix, self-audit F37/B0). Generated {date.today().isoformat()} · {len(hot)} rows · "
           f"conservation: hot count MUST equal cold row count.",
           ""] + hot
    open(HOT, "w", encoding="utf-8").write("\n".join(doc) + "\n")
    print(f"✅ wrote PATTERNS_HOT.md — {len(hot)} rows (== {len(rows)} cold rows, conservation OK)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
