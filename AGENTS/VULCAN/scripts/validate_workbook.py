#!/usr/bin/env python3
"""
VULCAN workbook validator — enforces workbook/SCHEMA.tsv against EVERY ledger it declares.

WHY THIS EXISTS (2026-08-21). `SCHEMA.tsv` described **KB.tsv only** for its entire life —
9 rows for one of eight ledgers — while `CLAUDE.md` said "read before writing" and nothing
ever checked anything. That is a ritual with no mechanism behind it. Ported from VIOLET's
`validate_workbook.py` (KB-VIO-165, 2026-07-30), whose first run found 11 enum violations,
one unchallenged for 109 days.

⚠️ GENERALISED ON THE PORT, and the generalisation is the point: VIOLET's schema has no
   `ledger` column, so its validator can only ever check ONE table. That is the same
   single-ledger limitation VULCAN had, sitting in the donor. This version adds `ledger`
   and validates N tables from one declaration — offered back to the donor.

⚠️ ONE FIELD, ONE TOKEN is the rule this enforces hardest (ZHAO's, learned the hard way).
   An enum cell carrying prose — `EMPIRICAL on the cadence; MODERATE as a forward prior` —
   is not a smaller problem than a wrong value. It matches NO filter, so the row becomes
   invisible to every scan that keys on that column while looking perfectly fine to a human
   reader. Both of the violations this validator found on its first run are that shape.

CHECKS
  · header drift        — declared columns vs the ledger's actual header (both directions)
  · ragged rows         — field count != header count
  · required-field population
  · enum membership     — against SCHEMA `allowed_values`
  · type shape          — Date/Timestamp/Integer/Float
  · id format + uniqueness where an id pattern is declared
  · CROSS-FILE score reconcile — VX.tsv vs STATUS matrix vs STATUS composite arithmetic
  · ERR: sentinels in series ledgers — REPORTED AS A COUNT (they are honest failures,
    not schema violations; a partial run is a FAILED run [L-16/L-20], so they surface)

Exit 2 on ERROR, 1 on WARN only, 0 clean — safe to wire into boot.

Usage:
  .venv/bin/python AGENTS/VULCAN/scripts/validate_workbook.py [--boot] [--ledger NAME]
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

WB = Path(__file__).resolve().parents[1] / "workbook"
SCHEMA = WB / "SCHEMA.tsv"

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
TS_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
DMY_RE = re.compile(r"^\d{2}-[A-Za-z]{3}-\d{4}$")
ID_PAT = re.compile(r"^([A-Z]+(?:-[A-Z]+)*)-N+$")   # e.g. KB-VULCAN-NNN, FL-VULCAN-NN


def rows(p):
    with open(p, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def raw_widths(p):
    with open(p, encoding="utf-8", newline="") as f:
        return [len(r) for r in csv.reader(f, delimiter="\t")]


def check_enum(val, allowed):
    return val in {a.strip() for a in allowed.split("|") if a.strip()}


def type_ok(val, t, allowed):
    if t == "Date":
        return bool(DATE_RE.match(val)) or bool(DMY_RE.match(val))
    if t == "Timestamp":
        return bool(TS_RE.match(val))
    if t == "Integer":
        return val.lstrip("-").isdigit()
    if t == "Float":
        try:
            float(val)
            return True
        except ValueError:
            return False
    return True


def validate(only=None):
    errs, warns, notes = [], [], []
    spec = rows(SCHEMA)
    by_ledger = {}
    for r in spec:
        by_ledger.setdefault(r["ledger"], []).append(r)

    for ledger, fields in by_ledger.items():
        if only and ledger != only:
            continue
        p = WB / ledger
        if not p.exists():
            errs.append(f"{ledger}: DECLARED IN SCHEMA BUT MISSING ON DISK")
            continue
        data = rows(p)
        declared = [f["variable_name"] for f in fields]
        actual = list(data[0].keys()) if data else []

        # header drift, BOTH directions
        missing = [c for c in declared if c not in actual]
        undocumented = [c for c in actual if c not in declared]
        if missing:
            errs.append(f"{ledger}: SCHEMA declares column(s) the file does not have: {missing}")
        if undocumented:
            warns.append(f"{ledger}: {len(undocumented)} column(s) present but UNDOCUMENTED: {undocumented}")

        # ragged rows
        w = Counter(raw_widths(p))
        if len(w) > 1:
            errs.append(f"{ledger}: RAGGED — field counts {dict(w)}")

        err_sentinels = 0
        for i, row in enumerate(data, start=2):
            for f in fields:
                col = f["variable_name"]
                if col not in row:
                    continue
                val = (row[col] or "").strip()
                if val.startswith("ERR:"):
                    err_sentinels += 1
                    continue
                if not val:
                    if f["required"] == "Yes":
                        errs.append(f"{ledger}:{i} required field `{col}` is EMPTY")
                    continue
                if f["data_type"] == "Enum" and f["allowed_values"]:
                    if not check_enum(val, f["allowed_values"]):
                        errs.append(f"{ledger}:{i} `{col}` = {val[:58]!r} not in enum "
                                    f"[{f['allowed_values']}]"
                                    + ("  <- ONE FIELD, ONE TOKEN: prose in a machine-read cell"
                                       if len(val) > 24 else ""))
                elif not type_ok(val, f["data_type"], f["allowed_values"]):
                    errs.append(f"{ledger}:{i} `{col}` = {val[:40]!r} is not a valid "
                                f"{f['data_type']}")
        if err_sentinels:
            notes.append(f"{ledger}: {err_sentinels} ERR: sentinel(s) — honest failures, "
                         f"NOT schema violations, but a partial run is a FAILED run [L-16/L-20]")

        # id uniqueness/format where declared
        idf = next((f for f in fields if f["variable_name"] in ("id",)), None)
        if idf and data and "id" in data[0]:
            ids = [(r.get("id") or "").strip() for r in data]
            dupes = [k for k, v in Counter(ids).items() if v > 1 and k]
            if dupes:
                errs.append(f"{ledger}: DUPLICATE id(s) {dupes[:5]}")
            m = ID_PAT.match(idf["allowed_values"].split()[0]) if idf["allowed_values"] else None
            if m:
                pre = m.group(1)
                bad = [x for x in ids if x and not x.startswith(pre)]
                if bad:
                    warns.append(f"{ledger}: {len(bad)} id(s) not matching prefix {pre}-: {bad[:3]}")

    return errs, warns, notes


def score_reconcile():
    """CROSS-FILE: VX.tsv scores vs STATUS.md's matrix vs STATUS's composite arithmetic.

    ⚠️ WHY THIS EXISTS, and the provenance is embarrassing enough to be worth stating: on
       2026-08-21 this desk wrote `MUST equal STATUS's matrix — STATUS is canonical` into
       SCHEMA.tsv as the description of `VX.score`, and NOTHING CHECKED IT. That is a rule
       with no mechanism — the exact class the validator around it was built that same
       afternoon to kill, committed hours later by the same session. Wired while all three
       surfaces AGREE, which is the only time you can trust a check you just wrote.

    THREE surfaces, not two, because they fail in different ways:
      · VX.tsv `score`          — the ledger
      · STATUS matrix rows      — the narrative table a reader actually meets
      · STATUS composite line   — `S1 3 · S2 3 · …`, the arithmetic
    The matrix-vs-composite leg is not hypothetical: STATUS's composite footer read
    "HELD 8/13" while its header said 8/21, and that sat there until a files audit found
    it by eye. A footer that restates a total is a SECOND copy of the state.

    STATUS is canonical. A mismatch never says which side is wrong on its own
    (`finding_reconcile_mismatch_does_not_say_which_side_is_wrong`) — but VX is the
    derived surface, so VX is where you look first.
    """
    import re
    status = WB.parent / "STATUS.md"
    out = []
    if not status.exists():
        return ["STATUS.md NOT FOUND — score reconcile is blind"], []
    txt = status.read_text(encoding="utf-8")

    vx = {}
    for r in rows(WB / "VX.tsv"):
        ch, sc = (r.get("channel") or "").strip(), (r.get("score") or "").strip()
        if ch:
            vx[ch] = sc

    # matrix rows: | **S1** | <name> | **3 ...
    matrix = {m.group(1): m.group(2) for m in
              re.finditer(r"\|\s*\*\*(S[1-5])\*\*\s*\|[^|]*\|\s*\*\*([1-5])", txt)}
    # composite arithmetic: S1 3 · S2 3 · ...
    comp = {}
    cm = re.search(r"(S1\s+[1-5](?:\s*·\s*S[2-5]\s+[1-5]){4})", txt)
    if cm:
        comp = dict(re.findall(r"(S[1-5])\s+([1-5])", cm.group(1)))

    errs, warns = [], []
    if not matrix:
        warns.append("STATUS.md: could not parse the convergence matrix — reconcile UNGRADEABLE, "
                     "not clean (a parse miss must never render as agreement)")
        return errs, warns
    if not comp:
        warns.append("STATUS.md: could not parse the composite arithmetic line — that leg is UNGRADEABLE")

    for ch in sorted(set(vx) | set(matrix) | set(comp)):
        v, m, c = vx.get(ch), matrix.get(ch), comp.get(ch)
        seen = {k: x for k, x in (("VX", v), ("matrix", m), ("composite", c)) if x is not None}
        if len(set(seen.values())) > 1:
            errs.append(f"{ch}: SCORE DISAGREEMENT " +
                        " vs ".join(f"{k}={x}" for k, x in seen.items()) +
                        "  <- STATUS is canonical; VX is derived, look there first")
        elif v is None and (m or c):
            warns.append(f"{ch}: in STATUS but has NO VX.tsv row")
    return errs, warns


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--boot", action="store_true", help="terse one-line verdict")
    ap.add_argument("--ledger", default=None)
    a = ap.parse_args()

    if not SCHEMA.exists():
        print("🔴 SCHEMA.tsv MISSING — nothing to validate against")
        return 2
    errs, warns, notes = validate(a.ledger)
    if not a.ledger:
        se, sw = score_reconcile()
        errs += se
        warns += sw
    n_led = len({r["ledger"] for r in rows(SCHEMA)})

    if a.boot:
        if errs:
            print(f"  🔴 workbook: {len(errs)} schema ERROR(s) across {n_led} ledgers — "
                  f"run scripts/validate_workbook.py")
        elif warns:
            print(f"  ⚠️ workbook: {len(warns)} warning(s), {n_led} ledgers validated")
        else:
            print(f"  ✓ workbook: {n_led} ledgers clean; VX/STATUS/composite scores reconcile")
        for n in notes:
            print(f"    ℹ️  {n}")
        return 2 if errs else (1 if warns else 0)

    print(f"VULCAN workbook validation — {n_led} ledger(s) declared in SCHEMA.tsv\n")
    for label, items, mark in (("ERROR", errs, "🔴"), ("WARN", warns, "🟠"), ("NOTE", notes, "ℹ️ ")):
        if items:
            print(f"{mark} {label} ({len(items)})")
            for x in items:
                print(f"    {x}")
            print()
    if not (errs or warns):
        print("✓ all declared ledgers conform.")
    return 2 if errs else (1 if warns else 0)


if __name__ == "__main__":
    sys.exit(main())
