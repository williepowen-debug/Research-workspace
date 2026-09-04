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
COLD_INDEX = os.path.normpath(os.path.join(HERE, "..", "PATTERNS_COLD_INDEX.md"))
# ROLLING WINDOW (2026-09-03, EVOLUTION (l)): the hot index reached 84% of the 32,550 B budget at
# 143 rows and, being generated, could not be rotated — the row SET had to split. Hot = rows dated
# within HOT_DAYS or carrying "[HOT]" in Notes (a held-hot tag for unpredictable-trigger lessons);
# everything older → PATTERNS_COLD_INDEX.md, one short line each, grep on demand. Measured 2026-09-03: the whole
# register was 68 days old (oldest row 6/27), so 75d would have split NOTHING — 45d cuts to ~95 rows
# ≈ 52% at the observed 2.1 mints/day. Conservation: hot + cold == rows, or rc 2.
HOT_DAYS = 45
HOT_HOOK, COLD_HOOK = 130, 100
BUDGET = 32550


def main():
    try:
        lines = open(COLD, encoding="utf-8").read().splitlines()
    except OSError as e:
        print(f"🔴 regen_patterns_hot CANNOT-CERTIFY: {e}")
        return 2
    rows = [l for l in lines[1:] if l.strip() and not l.startswith("#")]
    today = date.today()
    hot, cold = [], []
    for l in rows:
        f = l.split("\t")
        if len(f) != 7:
            print(f"🔴 regen_patterns_hot CANNOT-CERTIFY: ragged row {f[0]!r} ({len(f)} fields) — fix PATTERNS.tsv first")
            return 2
        head = " ".join(f[2].split())
        try:
            age = (today - date.fromisoformat(f[1].strip())).days
        except ValueError:
            print(f"🔴 regen_patterns_hot CANNOT-CERTIFY: un-parseable date {f[1]!r} on {f[0]} — a row with no date cannot be tiered")
            return 2
        held = "[HOT]" in f[6]
        if age <= HOT_DAYS or held:
            hot.append(f"- **{f[0]}** ({f[1]}, {f[3]}/{f[5]}{', HELD-HOT' if held and age > HOT_DAYS else ''}) — {head[:HOT_HOOK]}{'…' if len(head) > HOT_HOOK else ''}")
        else:
            cold.append(f"- **{f[0]}** ({f[1]}, {f[3]}/{f[5]}) — {head[:COLD_HOOK]}{'…' if len(head) > COLD_HOOK else ''}")
    if len(hot) + len(cold) != len(rows):
        print(f"🔴 regen_patterns_hot CANNOT-CERTIFY: conservation FAIL hot={len(hot)} + cold={len(cold)} != rows={len(rows)}")
        return 2
    doc = ["# PATTERNS — HOT INDEX (GENERATED — do not hand-edit; regenerate via scripts/regen_patterns_hot.py)",
           f"> One line per pattern dated within the last {HOT_DAYS} days or tagged `[HOT]` in Notes; older rows → "
           f"`PATTERNS_COLD_INDEX.md` (grep on demand); full sourced rows in `PATTERNS.tsv`. Boot reads THIS file. "
           f"Generated {today.isoformat()} · {len(hot)} hot + {len(cold)} cold = {len(rows)} rows · conservation-checked.",
           ""] + hot
    cdoc = ["# PATTERNS — COLD INDEX (GENERATED — do not hand-edit; regenerate via scripts/regen_patterns_hot.py)",
            f"> Rows older than {HOT_DAYS} days and not `[HOT]`-tagged. NOT a boot read — grep by ID or keyword, then pull the "
            f"full row from `PATTERNS.tsv`. Generated {today.isoformat()} · {len(cold)} rows.", ""] + cold
    open(HOT, "w", encoding="utf-8").write("\n".join(doc) + "\n")
    open(COLD_INDEX, "w", encoding="utf-8").write("\n".join(cdoc) + "\n")
    hb = os.path.getsize(HOT)
    print(f"✅ wrote PATTERNS_HOT.md — {len(hot)} hot rows ({hb:,} B = {hb/BUDGET:.0%} of budget) + PATTERNS_COLD_INDEX.md — "
          f"{len(cold)} cold rows; {len(hot)}+{len(cold)} == {len(rows)} conservation OK")
    if hb > BUDGET * 0.75:
        print(f"⚠️  hot index at {hb/BUDGET:.0%} ≥ 75% — shorten HOT_DAYS or HOT_HOOK; never raise the budget")
    return 0


if __name__ == "__main__":
    sys.exit(main())
