#!/usr/bin/env python3
"""VIOLET grading-note check — do CATALYSTS notes cite KB rows that have since been retracted?

WHY THIS EXISTS (KB-VIO-169, n=4 by 2026-08-04)
-----------------------------------------------
`workbook/CATALYSTS.tsv` notes are what `boot.py` prints **at the exact moment a
prediction resolves** — pre-formatted, authoritative-looking, and read once, under
time pressure, when their content is load-bearing. **Nothing ever checked them.**

Four instances:
  · 7/31 — the note said *"no >20 settle has occurred at any point in the episode."*
    True when written, FALSE from 7/29. Grading off it yields the right verdict
    with the wrong content.
  · 7/31 — the **8/5 SOQ** row, the *next* prediction due, still cited TERRY's
    **retracted 0.28** forward beta, a figure I had myself re-derived to 0.591.
  · 8/4 AM — the NFP row asserted *"no confirmed July CPI date exists anywhere in
    the fleet."* `PROME/DOCKET.tsv` had it DATE VERIFIED the whole time.
  · 8/4 PM — caught in the same session that wrote it.

🔑 **A grading aid decays faster than the thing it grades**, and my twin check
(`CALENDAR.md` vs `CATALYSTS.tsv`) compares which ROWS EXIST, never what the notes
SAY — the two files were row-for-row consistent all week and semantically
contradictory.

WHAT THIS CHECKS, and why this rule and not figure-matching
-----------------------------------------------------------
For every catalyst row, every `KB-VIO-nnn` cited in its note is resolved against
`KB.tsv` and flagged if it is **SUPERSEDED / CORRECTED / STALE**, or missing.

⚠️ **I deliberately did NOT build figure-matching.** `consumer_check.py` matches
bare strings with no unit or series context and returned **9-of-9 false positives**
on a live scan; a check that cries wolf on every 2-significant-figure number gets
ignored, which is worse than no check. **Citation status is exact, has no unit
ambiguity, and catches the actual failure** — the 0.28 beta was retracted, and a
retraction is a status change on a row.

⚠️ **SCOPE — what this CANNOT catch.** A note asserting a stale FACT that cites no
KB row (instances 1 and 3 above) is invisible here. **This closes the citation half
of the class, not the prose half.** The prose half needs an external completeness
check and is NOT solved. Stated so nobody reads a green run as "notes verified."

Exit codes: 0 = no cited row is retracted; 1 = at least one is (with --strict).
"""
from __future__ import annotations
import argparse, csv, re, sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAT = ROOT / "workbook" / "CATALYSTS.tsv"
KB = ROOT / "workbook" / "KB.tsv"
RETRACTED = {"SUPERSEDED", "CORRECTED", "STALE"}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--boot", action="store_true")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--within", type=int, default=0,
                    help="only rows dated within N days (0 = all forward rows)")
    a = ap.parse_args()

    if not CAT.exists() or not KB.exists():
        print("  ⚠️  CATALYSTS.tsv or KB.tsv missing — cannot check"); return 0

    kb = {r["ID"]: r for r in csv.DictReader(KB.open(), delimiter="\t")}
    today = date.today()
    findings, scanned, cites = [], 0, 0

    for row in csv.DictReader(CAT.open(), delimiter="\t"):
        try:
            d = date.fromisoformat(row["date"])
        except (ValueError, KeyError):
            continue
        if a.within and (d - today).days > a.within:
            continue
        note = row.get("notes", "") or ""
        scanned += 1
        for cid in sorted(set(re.findall(r"KB-VIO-\d+", note))):
            cites += 1
            r = kb.get(cid)
            if r is None:
                findings.append((row["date"], row["event"], cid, "NOT IN KB.tsv"))
            elif r["Status"].strip().upper() in RETRACTED:
                findings.append((row["date"], row["event"], cid, r["Status"].strip()))

    if not findings:
        if not a.boot:
            print(f"  ✓ grading notes clean — {cites} KB citation(s) across {scanned} catalyst row(s), none retracted")
        return 0

    print(f"  🔴 GRADING-NOTE CHECK — {len(findings)} catalyst note(s) cite a RETRACTED KB row:")
    for d, ev, cid, st in findings:
        print(f"     {d}  {ev[:46]:46s}  cites {cid} [{st}]")
    print("     ⚠️  This note prints AT THE MOMENT the prediction resolves. Fix the note, not the KB row.")
    print("     ⚠️  Scope: catches retracted CITATIONS only — a stale bare assertion with no KB cite is invisible here.")
    return 1 if a.strict else 0


if __name__ == "__main__":
    sys.exit(main())
