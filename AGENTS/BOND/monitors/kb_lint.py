#!/usr/bin/env python3
"""BOND — workbook conformance lint (KB.tsv / VX.tsv / FLOW.tsv / PREDICTIONS.tsv).

WHY THIS EXISTS
---------------
Boot step 7 has always said: *"Before any KB write: read workbook/SCHEMA.tsv
(validate Conf/Epistemic/Status enums) + AGENTS/VOCABULARIES.tsv (Group/Entity/
Source vocab)."*  Nothing ever ENFORCED it, and a 2026-08-21 boot-document audit
found the drift that had accumulated in the gap:

  * 14 rows with Conf outside the Admiralty enum ('high' x13, 'med-high' x1)
  * 13 rows with Epistemic outside its enum ('measured' x10, 'CONFIRMED' x3)
  * 11 rows with a Group not in NETWORK_GROUPS ('CREDIT', 'FED', 'FISCAL')

The tell that it was a MISSING GUARD and not carelessness: BOND wrote three
off-vocab rows that same morning, hours before finding the class. An instruction
a human must remember at every write is not a control; a check is.

  rc 0  clean
  rc 1  conformance finding (NOT a pass)
  rc 2  could not run (missing schema/vocab) -- also NOT a pass

    python3 monitors/kb_lint.py [--selftest]
"""
from __future__ import annotations

import csv
import datetime as dt
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
TODAY = dt.date.today()

ADMIRALTY = {a + str(n) for a in "ABCDEF" for n in range(1, 7)}


def load_vocab_groups() -> set:
    p = HERE.parent / "VOCABULARIES.tsv"
    if not p.exists():
        return set()
    sec, out = None, set()
    for l in p.read_text(encoding="utf-8").splitlines():
        if l.startswith("---"):
            sec = l.strip("-")
            continue
        if sec == "NETWORK_GROUPS" and l and not l.startswith("#"):
            out.add(l.split("\t")[0].strip())
    return out


def load_schema_enums() -> dict:
    p = HERE / "workbook" / "SCHEMA.tsv"
    if not p.exists():
        return {}
    out = {}
    for r in csv.DictReader(p.open(encoding="utf-8"), delimiter="\t"):
        av = (r.get("allowed_values") or "").strip()
        if av:
            out[r["variable_name"]] = set(av.split(";"))
    return out


def lint_kb(rows, enums, groups, report):
    n = 0
    seen = {}
    for r in rows:
        rid = r.get("ID", "?")
        if rid in seen:
            report(f"duplicate ID {rid} (also at row {seen[rid]})")
            n += 1
        seen[rid] = rid
        for col in ("Conf", "Epistemic", "Status"):
            allowed = enums.get(col)
            v = (r.get(col) or "").strip()
            if allowed and v and v not in allowed:
                report(f"{rid}: {col}='{v}' is not in SCHEMA.tsv's enum for {col}")
                n += 1
        g = (r.get("Group") or "").strip()
        if groups and g and g not in groups:
            report(f"{rid}: Group='{g}' is not in VOCABULARIES.tsv NETWORK_GROUPS")
            n += 1
        d = (r.get("Date") or "").strip()
        try:
            if dt.date.fromisoformat(d) > TODAY:
                report(f"{rid}: Date {d} is in the FUTURE")
                n += 1
        except ValueError:
            report(f"{rid}: Date '{d}' is not ISO YYYY-MM-DD")
            n += 1
    return n


def advisories(rows, report):
    """Status hygiene -- closeout step 10. ADVISORY: printed, not counted as
    a failure, because 'flip it or say why not' is a judgment the desk makes."""
    overdue, unset = [], []
    for r in rows:
        if (r.get("Status") or "").strip() != "ACTIVE":
            continue
        sb = (r.get("Stale_By") or "").strip()
        if not sb:
            unset.append(r["ID"])
            continue
        try:
            d = dt.date.fromisoformat(sb)
        except ValueError:
            continue
        if d < TODAY:
            overdue.append((r["ID"], sb, (TODAY - d).days))
    if overdue:
        report(f"ADVISORY — {len(overdue)} ACTIVE row(s) past Stale_By "
               "(closeout 10: flip to STALE/SUPERSEDED, or say why not):")
        for i, sb, age in sorted(overdue, key=lambda x: -x[2]):
            report(f"     {i}  stale_by {sb}  {age}d overdue")
    if unset:
        # NOT a defect claim. SCHEMA.tsv says Stale_By is optional -- "empty if
        # the fact is static or atemporal" -- and most of these are METHOD rows
        # (process lessons), which genuinely do not decay. The first version of
        # this advisory asserted the opposite and contradicted the schema it
        # exists to enforce; corrected 2026-08-21, same session it was written.
        report(f"FYI — {len(unset)} ACTIVE row(s) have an empty Stale_By: "
               f"{', '.join(unset)}")
        report("     SCHEMA permits this for STATIC or ATEMPORAL facts (method/process "
               "rows qualify). Listed so the choice stays deliberate, not inherited.")


def selftest() -> int:
    enums = {"Conf": ADMIRALTY, "Epistemic": {"EMPIRICAL", "ESTIMATE", "ASSUMPTION"},
             "Status": {"ACTIVE", "CONFIRMED", "STALE", "SUPERSEDED", "CORRECTED"}}
    groups = {"RATES", "CREDIT_SPREADS"}
    FIX = [
        ("REAL 8/21 defect: Conf='high' (14 rows drifted this way)",
         [{"ID": "X", "Conf": "high", "Epistemic": "EMPIRICAL", "Status": "ACTIVE",
           "Group": "RATES", "Date": "2026-08-01"}], 1),
        ("REAL 8/21 defect: Epistemic='measured' (10 rows)",
         [{"ID": "X", "Conf": "A1", "Epistemic": "measured", "Status": "ACTIVE",
           "Group": "RATES", "Date": "2026-08-01"}], 1),
        ("REAL 8/21 defect: Group='CREDIT' not in NETWORK_GROUPS",
         [{"ID": "X", "Conf": "A1", "Epistemic": "EMPIRICAL", "Status": "ACTIVE",
           "Group": "CREDIT", "Date": "2026-08-01"}], 1),
        ("a fully conformant row is clean",
         [{"ID": "X", "Conf": "A1", "Epistemic": "EMPIRICAL", "Status": "ACTIVE",
           "Group": "RATES", "Date": "2026-08-01"}], 0),
        ("future-dated row is caught",
         [{"ID": "X", "Conf": "A1", "Epistemic": "EMPIRICAL", "Status": "ACTIVE",
           "Group": "RATES", "Date": "2099-01-01"}], 1),
        ("duplicate IDs are caught",
         [{"ID": "D", "Conf": "A1", "Epistemic": "EMPIRICAL", "Status": "ACTIVE",
           "Group": "RATES", "Date": "2026-08-01"}] * 2, 1),
    ]
    fails = 0
    print("[kb_lint --selftest] fixtures are REAL drift this desk shipped\n")
    for label, rows, expected in FIX:
        got = lint_kb(rows, enums, groups, lambda m: None)
        ok = got == expected
        fails += 0 if ok else 1
        print(f"  {'PASS' if ok else 'FAIL'}  {label}")
        if not ok:
            print(f"        expected {expected}, got {got}")
    print(f"\n  {'ALL PASS' if not fails else str(fails) + ' FAILURE(S)'} — {len(FIX)} lint fixtures")
    return 1 if fails else 0


PRED_STATUS = {"OPEN", "TRUE", "FALSE", "VOID"}
# Declared here 2026-08-21 because it was declared NOWHERE. PREDICTIONS.tsv had
# been carrying BOTH "FAILED" (x4) and "FALSE" (x5) for one state, and no schema
# file covers that surface -- so nothing could ever have caught it. Two tokens
# for one state is not cosmetic: calibration is a COUNT of resolved outcomes,
# and a count keyed on either token silently drops the other group.


def lint_predictions(report) -> int:
    p = HERE / "thesis" / "PREDICTIONS.tsv"
    if not p.exists():
        return 0
    n = 0
    rows = list(csv.DictReader(p.open(encoding="utf-8"), delimiter="\t"))
    # FAIL LOUD on a wrong header rather than reporting clean. Learned the hard
    # way 2026-08-21: a "# Status ENUM ..." comment was added to the top of this
    # TSV as documentation, csv.DictReader took THAT line as the header, every
    # r.get("Status") came back empty -- and this very function reported ZERO
    # findings. A check reading the wrong referent has no error to notice.
    # (finding_instrument_reports_clean_against_the_wrong_reference)
    if not rows or "Status" not in rows[0]:
        report("PREDICTIONS.tsv: no 'Status' column — header row is wrong "
               "(a leading comment line?). NOT a pass; the enum check could not run.")
        return 1
    for r in rows:
        st = (r.get("Status") or "").strip()
        rid = r.get("ID", "?")
        if st and st not in PRED_STATUS:
            report(f"{rid}: PREDICTIONS Status='{st}' is not in {sorted(PRED_STATUS)}")
            n += 1
        resolved = st in ("TRUE", "FALSE", "VOID")
        if resolved and not (r.get("Date_Resolved") or "").strip():
            report(f"{rid}: resolved ({st}) with NO Date_Resolved")
            n += 1
        if resolved and not (r.get("Outcome") or "").strip():
            report(f"{rid}: resolved ({st}) with an EMPTY Outcome")
            n += 1
        if st == "OPEN" and (r.get("Date_Resolved") or "").strip():
            report(f"{rid}: OPEN but carries a Date_Resolved")
            n += 1
    return n


def main() -> int:
    if "--selftest" in sys.argv:
        return selftest()
    kb = HERE / "workbook" / "KB.tsv"
    enums, groups = load_schema_enums(), load_vocab_groups()
    if not enums:
        print("  ⚠️  SCHEMA.tsv unreadable — GAP, not a pass"); return 2
    if not groups:
        print("  ⚠️  VOCABULARIES.tsv NETWORK_GROUPS unreadable — GAP, not a pass"); return 2
    rows = list(csv.DictReader(kb.open(encoding="utf-8"), delimiter="\t"))

    out = []
    widths = {len(l.split("\t")) for l in kb.read_text(encoding="utf-8").splitlines() if l.strip()}
    if widths != {13}:
        out.append(f"KB.tsv field-count is not uniformly 13: saw {sorted(widths)}")

    n = len(out) + lint_kb(rows, enums, groups, out.append) + lint_predictions(out.append)
    print(f"[kb_lint] {len(rows)} KB rows · SCHEMA enums {sorted(enums)} · "
          f"{len(groups)} network groups")
    for m in out:
        print(f"   🔴 {m}")
    if not n:
        print("   ✅ conformant: enums, vocabulary, dates, IDs, field-count")
    adv = []
    advisories(rows, adv.append)
    for m in adv:
        print(f"   🟠 {m}" if not m.startswith("     ") else m)
    return 1 if n else 0


if __name__ == "__main__":
    raise SystemExit(main())
