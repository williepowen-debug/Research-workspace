#!/usr/bin/env python3
"""VIOLET Convergence Score — compute the matrix sum by script, never by hand.

Parses the CONVERGENCE MATRIX table in STATUS.md, maps each vector's emoji to
its score (⚪1 🟡2 🟠3 🔴4 🔴🔴5), prints the per-vector breakdown, and checks
the computed total against the "Convergence Score: N/D" line in the file.

Origin: CHG-RED-037a — the hand-summed score was wrong twice in 48h (6/9 and
6/10, opposite directions, both Orch-caught). The mechanical sum replaces
vigilance.

Usage:
  .venv/bin/python3 AGENTS/VIOLET/scripts/convergence_score.py
  → exit 0 if the declared score matches the computed one, exit 1 on mismatch
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

STATUS = Path(__file__).resolve().parent.parent / "STATUS.md"

# Order matters: check 🔴🔴 before 🔴
EMOJI_SCORES = [("🔴🔴", 5), ("🔴", 4), ("🟠", 3), ("🟡", 2), ("⚪", 1)]


def parse_matrix(text: str) -> tuple[list[tuple[str, str, int]], list[str]]:
    """Return ([(vector, emoji, score)], problems) from the CONVERGENCE MATRIX."""
    m = re.search(r"## CONVERGENCE MATRIX\n(.*?)(?:\n## |\Z)", text, re.S)
    if not m:
        sys.exit("ERROR: no '## CONVERGENCE MATRIX' section found in STATUS.md")
    rows: list = []
    bad: list[str] = []
    for line in m.group(1).splitlines():
        if not line.startswith("|") or set(line.replace("|", "").strip()) <= {"-", " "}:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2 or cells[0].lower() in ("vector", ""):
            continue
        vector, score_cell = cells[0], cells[1]
        for emoji, score in EMOJI_SCORES:
            if emoji in score_cell:
                # ⚠️ EMOJI vs DIGIT CROSS-CHECK, added 2026-09-04 (DAEDALUS 🔴#2).
                # The cells carry BOTH a badge and a number and they can disagree
                # silently: `🔴 **5**` scored 4 here while a human read 5, which is
                # one of the three totals that were live on STATUS at once. Neither
                # is trusted alone any more.
                m = re.search(r"\*{0,2}(\d)\*{0,2}\s*$", score_cell.strip())
                if m and int(m.group(1)) != score:
                    bad.append(f"{vector!r}: badge {emoji} = {score} but the cell "
                               f"writes {m.group(1)} ({score_cell!r})")
                rows.append((vector, emoji, score))
                break
        else:
            # FAIL CLOSED. v1 warned and DROPPED the row, which silently changed
            # both the vector count and the total — the 🟣 cheap-tail row vanished
            # from a "10 vector" report that should have been 11.
            bad.append(f"{vector!r}: no recognised badge in cell {score_cell!r} — "
                       f"row DROPPED from the sum, which changes the denominator")
    return rows, bad


def declared_score(text: str) -> tuple[int, int] | None:
    m = re.search(r"Convergence Score:\s*(\d+)\s*/\s*(\d+)", text)
    return (int(m.group(1)), int(m.group(2))) if m else None


def main() -> int:
    text = STATUS.read_text()
    rows, bad = parse_matrix(text)
    if bad:
        print("  🔴 MATRIX CELLS UNRELIABLE — refusing to certify a total:")
        for b_ in bad:
            print(f"     {b_}")
        return 1
    total = sum(s for _, _, s in rows)
    denom = 5 * len(rows)

    print(f"CONVERGENCE SCORE  ({len(rows)} vectors)")
    for vector, emoji, score in rows:
        print(f"  {score}  {emoji:2s}  {vector}")
    pct = f"{total / denom * 100:.0f}%" if denom else "n/a"
    print(f"  COMPUTED: {total}/{denom} ({pct})")

    decl = declared_score(text)
    if decl is None:
        print("  ⚠️  no 'Convergence Score: N/D' line found to verify against")
        return 1
    if decl == (total, denom):
        print(f"  ✓ declared score matches: {decl[0]}/{decl[1]}")
        return 0
    print(f"  ❌ MISMATCH — declared {decl[0]}/{decl[1]} vs computed {total}/{denom}. Fix STATUS.md.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
