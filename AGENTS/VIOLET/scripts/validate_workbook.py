#!/usr/bin/env python3
"""VIOLET workbook validator — enforces workbook/SCHEMA.tsv against workbook/KB.tsv.

WHY THIS EXISTS (KB-VIO-165, 2026-07-30). `SCHEMA.tsv` has declared the KB's
column types and enums since 2026-04-12 and **nothing ever checked them.**
VIOLET's own CLAUDE.md write-back step 8 says "validate enums against
workbook/SCHEMA.tsv" — a ritual with no mechanism behind it, which is the same
class as the MAINTENANCE cap banner (`finding_mechanize_the_cap_not_the_ritual`).
The first run found 11 rows violating the enums, one of them dating to the
founding batch and unchallenged for 109 days.

CHECKS
  · ID uniqueness, format (KB-VIO-NNN), and numbering gaps
  · Conf / Epistemic / Status against SCHEMA `allowed_values`
  · Date / Stale_By ISO-8601 shape
  · Required-field population
  · DerivedFrom referential integrity (every parent ID must exist)
  · Ragged rows (column count != header)
  · Stale_By past-due on ACTIVE rows — REPORTED AS A COUNT, not a wall of IDs

⚠️ ON Stale_By, AND WHY THIS IS A WARNING AND NOT AN ERROR. 73 of 164 ACTIVE
rows were past their review date on first run, some since April. That is not 73
neglected reviews — it is a **field applied to the wrong population.** A KB row
recording a dated observation ("on 6/10 CPI printed X") is a historical record
and cannot go stale; only a row carrying a *live forward claim* can. `Stale_By`
was set indiscriminately at logging time, so the past-due count measures how
many dated facts have aged, not how much review is owed. Fixing that means
deciding per row whether it carries a live claim, which is a judgement pass and
not this script's job. It is surfaced so the number stays visible instead of
quietly growing.

Exit 1 on any ERROR, 0 on warnings only — safe to wire into boot.

Usage:
  .venv/bin/python3 AGENTS/VIOLET/scripts/validate_workbook.py
  .venv/bin/python3 AGENTS/VIOLET/scripts/validate_workbook.py --boot   # terse
"""
from __future__ import annotations

import argparse
import collections
import csv
import re
import sys
from datetime import date
from pathlib import Path

WB = Path(__file__).resolve().parents[1] / "workbook"
SCHEMA, KB = WB / "SCHEMA.tsv", WB / "KB.tsv"
ID_RE = re.compile(r"KB-VIO-\d{3}")
ISO_RE = re.compile(r"\d{4}-\d{2}-\d{2}")


def load_schema() -> dict:
    return {r["variable_name"]: r for r in csv.DictReader(SCHEMA.open(), delimiter="\t")}


def validate() -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []
    schema = load_schema()

    header = KB.open().readline().rstrip("\n").split("\t")
    raw = KB.read_text(encoding="utf-8").splitlines()[1:]
    for n, line in enumerate(raw, start=2):
        got = len(line.split("\t"))
        if got != len(header):
            errors.append(f"line {n}: ragged row — {got} fields, header has {len(header)}")

    rows = list(csv.DictReader(KB.open(), delimiter="\t"))
    ids = [r["ID"] for r in rows]

    for i, c in collections.Counter(ids).items():
        if c > 1:
            errors.append(f"duplicate ID {i} ({c}×)")
    bad_fmt = [i for i in ids if not ID_RE.fullmatch(i)]
    if bad_fmt:
        errors.append(f"malformed IDs: {bad_fmt[:5]}")

    nums = sorted(int(i.split("-")[-1]) for i in ids if ID_RE.fullmatch(i))
    if nums:
        gaps = [n for n in range(nums[0], nums[-1] + 1) if n not in nums]
        if gaps:
            warnings.append(f"ID numbering gaps: {gaps}")

    for col in ("Conf", "Epistemic", "Status"):
        allowed = {v.strip() for v in schema[col]["allowed_values"].split(";") if v.strip()}
        offenders = collections.defaultdict(list)
        for r in rows:
            if r[col] not in allowed:
                offenders[r[col]].append(r["ID"])
        for val, who in sorted(offenders.items()):
            errors.append(f"{col}='{val}' not in SCHEMA allowed_values — {len(who)} row(s): "
                          f"{', '.join(who[:6])}{' …' if len(who) > 6 else ''}")

    for col in ("Date", "Stale_By"):
        bad = [r["ID"] for r in rows if r[col] and not ISO_RE.fullmatch(r[col])]
        if bad:
            errors.append(f"{col} not ISO-8601 — {bad[:5]}")

    required = [c for c, s in schema.items() if s["required"] == "Yes"]
    missing = [(r["ID"], c) for r in rows for c in required if not r.get(c)]
    if missing:
        errors.append(f"required field empty — {missing[:5]}")

    idset = set(ids)
    dangling = []
    for r in rows:
        for ref in (r.get("DerivedFrom") or "").split(","):
            ref = ref.strip()
            if ref and ref not in idset:
                dangling.append((r["ID"], ref[:48]))
    if dangling:
        errors.append(f"DerivedFrom references a non-existent KB ID — {len(dangling)} case(s): "
                      f"{dangling[:3]}")

    today = date.today().isoformat()
    overdue = [r["ID"] for r in rows
               if r["Stale_By"] and r["Stale_By"] < today and r["Status"] == "ACTIVE"]
    if overdue:
        warnings.append(
            f"{len(overdue)} ACTIVE row(s) past Stale_By (oldest {min(r['Stale_By'] for r in rows if r['ID'] in overdue)}) "
            f"— see the module docstring: this measures dated facts aging, not reviews owed")

    stats = {"rows": len(rows), "errors": len(errors), "warnings": len(warnings),
             "overdue": len(overdue)}
    return errors, warnings, stats


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Validate KB.tsv against SCHEMA.tsv")
    ap.add_argument("--boot", action="store_true", help="terse one-line output")
    args = ap.parse_args(argv)

    errors, warnings, stats = validate()

    if args.boot:
        if errors:
            print(f"    🔴 KB.tsv SCHEMA VIOLATIONS ({len(errors)}) — {errors[0]}")
            for e in errors[1:]:
                print(f"       · {e}")
        else:
            print(f"    ✓ KB.tsv {stats['rows']} rows — schema clean"
                  + (f" ({stats['overdue']} past Stale_By, informational)" if stats["overdue"] else ""))
        return 1 if errors else 0

    print(f"KB.tsv — {stats['rows']} rows validated against SCHEMA.tsv")
    for e in errors:
        print(f"  🔴 ERROR   {e}")
    for w in warnings:
        print(f"  ⚠️  WARN    {w}")
    if not errors and not warnings:
        print("  ✓ clean")
    elif not errors:
        print("  ✓ no errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
