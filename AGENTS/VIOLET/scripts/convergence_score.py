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


def parse_matrix(text: str) -> list[tuple[str, str, int]]:
    """Return [(vector, emoji, score)] from the CONVERGENCE MATRIX table."""
    m = re.search(r"## CONVERGENCE MATRIX\n(.*?)(?:\n## |\Z)", text, re.S)
    if not m:
        sys.exit("ERROR: no '## CONVERGENCE MATRIX' section found in STATUS.md")
    rows = []
    for line in m.group(1).splitlines():
        if not line.startswith("|") or set(line.replace("|", "").strip()) <= {"-", " "}:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2 or cells[0].lower() in ("vector", ""):
            continue
        vector, score_cell = cells[0], cells[1]
        for emoji, score in EMOJI_SCORES:
            if emoji in score_cell:
                rows.append((vector, emoji, score))
                break
        else:
            print(f"  ⚠️  no emoji parsed in row: {vector!r} (cell: {score_cell!r})")
    return rows


def declared_score(text: str) -> tuple[int, int] | None:
    m = re.search(r"Convergence Score:\s*(\d+)\s*/\s*(\d+)", text)
    return (int(m.group(1)), int(m.group(2))) if m else None


def main() -> int:
    text = STATUS.read_text()
    rows = parse_matrix(text)
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
