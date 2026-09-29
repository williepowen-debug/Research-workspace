#!/usr/bin/env python3
"""
LABOR spine-gate regression tests — spine_check.py parse_spine() / verdict().

Run:  .venv/bin/python3 AGENTS/LABOR/scripts/tests/test_spine_check.py
Exit: 0 all pass, 1 any fail.  (Run directly, not via pytest — see CLAUDE.md FILES.)

WHY THIS FILE EXISTS
--------------------
2026-09-29: the gate was extended to JOLTS + FL UR and negative-tested on ONE case
(live row set back to July -> STALE). A reviewer then found two FALSE PASSES the
self-test could not see, reproduced here before the fix:
  (1) live JOLTS row left at July + an unrelated August-dated note elsewhere -> FRESH
  (2) FL UR row dated AHEAD of FRED (unreleased month) -> FRESH
Both came from the reducer taking max() over any keyword line. The fix reads only
the series' live KEY THRESHOLDS row. Cases (1) and (2) are the reviewer's; the rest
are the edges of the new parser. This suite is still self-authored (L-30): it covers
the cases listed below and nothing else.
"""
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from spine_check import parse_spine, verdict, STATUS  # noqa: E402

ROW_IC = "| Initial claims (MA basis) | **197K** [w/e Sep 19 · obs 2026-09-19 · DOL] | b | s |"
ROW_CC = "| Continuing claims | **1,719K** [w/e Sep 12 · obs 2026-09-12] | b | s |"
ROW_JO = "| JOLTS hires (gross) | **5,192K** [Aug P · obs {d} · BLS] | b | s |"
ROW_FL = "| FL UR | **4.5%** [Aug P · obs {d}] | b | s |"


def doc(jolts="2026-08-01", fl="2026-08-01", extra=()):
    return "\n".join([ROW_IC, ROW_CC, ROW_JO.format(d=jolts), ROW_FL.format(d=fl), *extra])


FRED = {"ICSA": "2026-09-19", "CCSA": "2026-09-12", "JTSHIL": "2026-08-01", "FLUR": "2026-08-01"}
fails = []


def check(name, got, want):
    ok = got == want
    print(f"{'PASS' if ok else 'FAIL'}  {name}: got {got!r}, want {want!r}")
    if not ok:
        fails.append(name)


def v(text, sid):
    d, _why = parse_spine(text)[sid]
    return "CANNOT-VERIFY" if d is None else verdict(d, FRED[sid])


# Baseline
check("all fresh", [v(doc(), s) for s in FRED], ["FRESH"] * 4)
# Reviewer case 1: stale live row + later-dated note elsewhere must NOT certify
check("R1 JOLTS July row + Aug note elsewhere",
      v(doc(jolts="2026-07-01", extra=["note: JOLTS hires source checked (obs 2026-08-01)"]), "JTSHIL"),
      "STALE")
check("R1 FL same shape",
      v(doc(fl="2026-07-01", extra=["- FL UR prose line (obs 2026-08-01)"]), "FLUR"), "STALE")
# Reviewer case 2: a date AHEAD of FRED is unverified, never fresh
check("R2 FL ahead of FRED", v(doc(fl="2026-12-01"), "FLUR"), "AHEAD")
check("R2 JOLTS ahead of FRED", v(doc(jolts="2026-09-01"), "JTSHIL"), "AHEAD")
# Ordinary stale
check("plain stale JOLTS", v(doc(jolts="2026-07-01"), "JTSHIL"), "STALE")
# Parser edges — every one must be CANNOT-VERIFY
check("live row missing", v("\n".join([ROW_IC, ROW_CC, ROW_FL.format(d="2026-08-01")]), "JTSHIL"),
      "CANNOT-VERIFY")
check("duplicate live row", v(doc(extra=[ROW_JO.format(d="2026-08-01")]), "JTSHIL"), "CANNOT-VERIFY")
check("live row without obs token",
      v(doc().replace("[Aug P · obs 2026-08-01 · BLS]", "[Aug P · BLS]"), "JTSHIL"), "CANNOT-VERIFY")
check("live row with two different obs dates",
      v(doc().replace("[Aug P · obs 2026-08-01 · BLS]", "[obs 2026-08-01 · obs 2026-07-01]"), "JTSHIL"),
      "CANNOT-VERIFY")
# A graded/historical row that merely MENTIONS the series is never read
check("calendar row mentioning JOLTS hires is inert",
      v(doc(jolts="2026-07-01", extra=["| ✅ Tue 9/29 | JOLTS hires Aug (obs 2026-08-01) graded | x |"]), "JTSHIL"),
      "STALE")
# The live STATUS.md parses to exactly one date per series (no ambiguity today)
live = parse_spine(STATUS.read_text(encoding="utf-8"))
check("live STATUS.md: every series resolves to one live-row date",
      all(d is not None for d, _ in live.values()), True)

print(f"\n{len(fails)} failure(s)")
sys.exit(1 if fails else 0)
