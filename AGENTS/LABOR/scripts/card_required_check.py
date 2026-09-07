#!/usr/bin/env python3
"""card_required_check.py — DOES A CARD THAT SHOULD EXIST, EXIST?

THE GAP THIS CLOSES (declared 2026-09-07, Will):
  B5b enumerates the cards in `docket/` and asks whether each has been GRADED.
  It is an inventory check over EXISTING artifacts, so **an empty docket is
  indistinguishable from a docket with nothing owed** — a required card that was
  never created produces a clean boot while preparation is late. That is exactly
  what happened to the 2026-09-10 claims card: B5b returned zero live cards, the
  boot read clean, and the card was 3 days from its print with no file.

  This check runs the other direction: it derives the cards that SHOULD exist from
  `docket/CATALYSTS.tsv` and reports the ones that do not. B5b answers "is this card
  graded?"; this answers "is this card WRITTEN?". Neither can substitute for the other.
  (`[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]` — a scan over the
  artifacts you have cannot report the artifact you never made.)

CLASSIFICATION IS EXPLICIT AND FAILS LOUD.
  A row is card-owing if its notes carry an explicit `CARD:<stem>` token, else if its
  event text matches one of the declared patterns below. A row that matches NOTHING is
  reported as UNCLASSIFIED — never silently treated as "no card owed", because that
  default is what makes an absence invisible in the first place.

EXIT CODES (repo convention): 0 = nothing owed and missing · 1 = a required card is
MISSING inside its freeze window · 2 = CANNOT-VERIFY (parse/IO failure). A parse
failure is never a PASS.
"""

import csv
import datetime as dt
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LABOR = os.path.dirname(HERE)
CATALYSTS = os.path.join(LABOR, "docket", "CATALYSTS.tsv")
DOCKET = os.path.join(LABOR, "docket")
GRADED = os.path.join(DOCKET, "graded")

# C2a: write the card "~1 week out, not on print morning."
FREEZE_LEAD_DAYS = 7
# How far ahead to look. Beyond this a missing card is not yet owed.
HORIZON_DAYS = 21

# Declared card-owing patterns. event-regex -> (card stem suffix, why it is multi-loaded).
# Adding a row here is the ONLY way a new event class starts being required.
PATTERNS = [
    (r"\binitial claims\b", "claims",
     "T-01/T-02 + vector 13 + Kill B + LAB-03 + CARL kill-rule leg 1 — permanently multi-loaded"),
    (r"\bNFP\b|\bnonfarm payroll", "NFP",
     "Kill A + T-06 + freeze-thaw LEG A + vector 8 + U-3/LFPR joint grade"),
    (r"\bECI\b", "ECI",
     "quarterly composition gauge (C2a names ECI explicitly)"),
    (r"\bQCEW\b", "QCEW",
     "quarterly benchmark gauge (C2a names QCEW explicitly)"),
    (r"\bJOLTS\b", "JOLTS",
     "quarterly-class gauge; v4 NET bands pre-registered"),
    (r"\bISM\b", "ISM",
     "vector 3 survey layer, pre-registered drop-to-1 condition"),
    (r"\bFOMC\b", "FOMC",
     "labor-language card (separate baseline per instrument type, L-09)"),
]

# Rows that are explicitly NOT card-owing: builds, admin re-triggers, watch-only items.
# Matching here suppresses the UNCLASSIFIED report; it does not require a card.
NO_CARD = [
    (r"READ_CAP", "admin re-trigger, no print to grade"),
    (r"VINTAGE TABLE due|MEASUREMENT build", "build deliverable, not a graded print"),
    (r"grading card FREEZE", "this row IS the freeze reminder for another row's card"),
    (r"counter-tariffs", "WATCH only — no LABOR threshold armed (docketed as such)"),
]


def classify(event, notes):
    """-> (kind, stem, why). kind in REQUIRED | NO-CARD | UNCLASSIFIED."""
    m = re.search(r"CARD:([A-Za-z0-9_.-]+)", notes or "")
    if m:
        return "REQUIRED", m.group(1), "explicit CARD: token in notes"
    hay = f"{event} {notes}"
    for rx, why in NO_CARD:
        if re.search(rx, hay, re.I):
            return "NO-CARD", None, why
    for rx, stem, why in PATTERNS:
        if re.search(rx, event or "", re.I):
            return "REQUIRED", stem, why
    return "UNCLASSIFIED", None, "matched no declared pattern"


def card_names(date, stem):
    """Accepted filenames for a card. FOMC uses its own prefix (see FILES table)."""
    d = date.strftime("%Y%m%d")
    if stem == "FOMC":
        return [f"FOMC_LABOR_LANGUAGE_{d}.md"]
    return [f"GRADING_CARD_{d}_{stem}.md", f"GRADING_CARD_{d}.md"]


def exists(names):
    for n in names:
        for base in (DOCKET, GRADED):
            p = os.path.join(base, n)
            if os.path.isfile(p):
                return os.path.relpath(p, LABOR)
    return None


def main(argv):
    if "--self-test" in argv:
        return self_test()
    today = dt.date.today()
    for a in argv:
        if a.startswith("--today="):
            today = dt.date.fromisoformat(a.split("=", 1)[1])

    print("=" * 72)
    print(f"  LABOR Required-Card Check — {today}  (horizon {HORIZON_DAYS}d · freeze lead {FREEZE_LEAD_DAYS}d)")
    print("  derives cards that SHOULD exist from CATALYSTS.tsv — the inverse of B5b")
    print("=" * 72)

    try:
        with open(CATALYSTS, newline="", encoding="utf-8") as fh:
            rdr = csv.DictReader(fh, delimiter="\t")
            fields = rdr.fieldnames or []
            rows = list(rdr)
    except OSError as e:
        print(f"  ⛔ CANNOT-VERIFY: {e}")
        return 2
    # A header with zero rows is a VALID empty calendar, not a parse failure. Only a
    # missing 'date' column is unreadable. (Conflating the two made the guard's own
    # first run report CANNOT-VERIFY on an empty calendar — caught by --self-test.)
    if "date" not in fields:
        print("  ⛔ CANNOT-VERIFY: CATALYSTS.tsv missing a 'date' column")
        return 2

    late, upcoming, unclassified, ok = [], [], [], []
    for r in rows:
        raw = (r.get("date") or "").strip().lstrip("~")
        try:
            d = dt.date.fromisoformat(raw)
        except ValueError:
            unclassified.append((raw, (r.get("event") or "")[:60], "unparseable date"))
            continue
        days = (d - today).days
        if days < 0 or days > HORIZON_DAYS:
            continue
        kind, stem, why = classify(r.get("event", ""), r.get("notes", "") + " " + r.get("what_to_check", ""))
        if kind == "NO-CARD":
            continue
        if kind == "UNCLASSIFIED":
            unclassified.append((raw, (r.get("event") or "")[:60], why))
            continue
        names = card_names(d, stem)
        found = exists(names)
        rec = (d, days, stem, names[0], found, why, (r.get("event") or "")[:70])
        if found:
            ok.append(rec)
        elif days <= FREEZE_LEAD_DAYS:
            late.append(rec)
        else:
            upcoming.append(rec)

    rc = 0
    if late:
        rc = 1
        print("\n  🔴 MISSING AND OWED NOW — inside the C2a freeze window")
        print("  " + "-" * 68)
        for d, days, stem, name, _f, why, ev in sorted(late):
            print(f"  {d} ({days}d)  MISSING  docket/{name}")
            print(f"       event: {ev}")
            print(f"       owed because: {why}")
    if upcoming:
        print("\n  📅 NOT YET OWED — beyond the freeze lead, listed so it is not a surprise")
        for d, days, stem, name, _f, _why, _ev in sorted(upcoming):
            print(f"  {d} ({days}d)  freeze by {d - dt.timedelta(days=FREEZE_LEAD_DAYS)}  docket/{name}")
    if ok:
        print("\n  ✅ PRESENT")
        for d, days, stem, name, found, _why, _ev in sorted(ok):
            print(f"  {d} ({days}d)  {found}")
    if unclassified:
        rc = max(rc, 1)
        print("\n  ⚠️  UNCLASSIFIED — matched no declared pattern. NOT the same as 'no card owed'.")
        print("      Decide, then add it to PATTERNS or NO_CARD so the answer is durable.")
        for raw, ev, why in unclassified:
            print(f"  {raw}  {ev}  [{why}]")

    if rc == 0 and not upcoming:
        print("\n  ✅ Nothing owed and missing inside the horizon.")
    print("\n  SCOPE: reports only on rows in CATALYSTS.tsv. An event that was never")
    print("  docketed is invisible here too — that is BD-23, and this check does not close it.")
    return rc


def self_test():
    """Falsify the check before trusting it: it must FIND a missing card, not just pass."""
    global CATALYSTS, DOCKET, GRADED
    import tempfile
    cases, fails = [], 0
    hdr = "date\tevent\twhat_to_check\tthreshold_signal\tpriority\twho_cares\tnotes\tdate_class\n"
    today = dt.date(2026, 9, 7)

    def run(rows, files, want, label):
        nonlocal fails
        global CATALYSTS, DOCKET, GRADED
        with tempfile.TemporaryDirectory() as td:
            DOCKET = os.path.join(td, "docket"); GRADED = os.path.join(DOCKET, "graded")
            os.makedirs(GRADED)
            CATALYSTS = os.path.join(DOCKET, "CATALYSTS.tsv")
            with open(CATALYSTS, "w", encoding="utf-8") as fh:
                fh.write(hdr + "".join(rows))
            for f in files:
                open(os.path.join(DOCKET, f), "w").close()
            import io, contextlib
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                rc = main([f"--today={today}"])
            ok = rc == want
            if not ok:
                fails += 1
            print(f"  {'PASS' if ok else 'FAIL'}  {label:<58} rc={rc} (want {want})")

    claims = "2026-09-10\tInitial claims w/e Sep 5\tlevel\tbands\tHIGH\tLABOR\tnotes\tconfirmed\n"
    far = "2026-09-25\tNFP September\tx\ty\tHIGH\tLABOR\tn\tconfirmed\n"
    admin = "2026-09-09\tREAD_CAP dated re-trigger\tx\ty\tHIGH\tLABOR\tn\tconfirmed\n"
    weird = "2026-09-09\tSomething nobody classified\tx\ty\tHIGH\tLABOR\tn\tconfirmed\n"

    print("  REQUIRED-CARD CHECK — SELF-TEST")
    print("  " + "-" * 68)
    run([claims], [], 1, "missing card inside freeze window must FAIL")
    run([claims], ["GRADING_CARD_20260910_claims.md"], 0, "present card must PASS")
    run([far], [], 0, "beyond freeze lead must NOT be reported late")
    run([admin], [], 0, "admin re-trigger must not demand a card")
    run([weird], [], 1, "unclassifiable row must FAIL, never default to 'no card'")
    run([], [], 0, "empty calendar must PASS")
    print("  " + "-" * 68)
    print("  ✅ SELF-TEST PASSES" if not fails else f"  ❌ {fails} SELF-TEST FAILURE(S)")
    return 0 if not fails else 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
