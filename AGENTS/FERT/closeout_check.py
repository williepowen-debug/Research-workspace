#!/usr/bin/env python3
"""
closeout_check.py — FERT closeout runner. Runs the MECHANICAL closeout steps,
reports PASS / LOOK / FAIL per step, then NAMES the judgement steps it cannot
verify.

Added 2026-10-28 (Will-approved; peer-comparison gap 4; model = HANS
scripts/closeout_check.py). Why: a checklist with an item omitted does not look
like a failure, it looks like a shorter checklist — FERT's own 10/28 closeout
recorded a skipped step by hand. DAEDALUS's named L5 condition for FERT is a
clean closeout that someone else can read.

  ⛔ THIS SCRIPT DOES NOT CERTIFY THE CLOSEOUT. It certifies that the
  mechanical steps EXECUTED and what they printed. The judgement steps are
  listed as UNVERIFIED BY DESIGN at the end.

Gate = the tool's OWN verdict marker in its output, not its exit code: a Python
traceback exits 1 like a real finding (HANS lesson 2026-09-19). A step with no
marker, or with crash text, is FAIL even on rc 0.

Run AFTER committing, BEFORE safe-push:   python3 AGENTS/FERT/closeout_check.py
Exit: 0 all PASS · 1 something to LOOK at · 2 a step FAILED (did not run / no verdict).
"""
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PY = sys.executable

CRASH = ("traceback (most recent call last)", "modulenotfounderror", "importerror",
         "can't open file", "no such file or directory", "command not found",
         "syntaxerror", "unrecognized arguments")


def run(cmd):
    try:
        p = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True, timeout=300)
        return p.returncode, (p.stdout + "\n" + p.stderr).strip()
    except Exception as e:  # noqa: BLE001 — fail loud, never silent
        return None, f"{type(e).__name__}: {e}"


def classify(rc, out, marker, passed):
    """FAIL if the tool died or never printed its verdict marker; else PASS if
    passed(out) else LOOK. `marker` is a regex the tool owes in its output."""
    low = (out or "").lower()
    if rc is None or any(m in low for m in CRASH):
        return "FAIL", "tool did not run cleanly"
    if marker and not re.search(marker, out or "", re.M):
        return "FAIL", f"verdict marker /{marker}/ absent — not observed to do its job"
    return ("PASS", "") if passed(out) else ("LOOK", "")


def tsv_targets():
    pats = ["workbook/*.tsv", "data/*.tsv", "board_log.tsv"]
    return sorted({p for pat in pats for p in HERE.glob(pat)})


def steps():
    fert = "AGENTS/FERT"
    claim_paths = ["PROME/DOCKET.tsv", "PROME/GATES.tsv", "PROME/WILL_QUEUE.md",
                   f"{fert}/STATUS.md", f"{fert}/workbook/TRIGGERS.tsv",
                   f"{fert}/workbook/GATE_GRADES.md", f"{fert}/workbook/PREDICTIONS.tsv",
                   f"{fert}/workbook/KB.tsv",
                   *sorted(str(p.relative_to(ROOT)) for p in HERE.glob("workbook/GRADING_CARD_*.md"))]
    claim_paths = [p for p in claim_paths if (ROOT / p).exists()]
    yield ("1   own tree committed", ["git", "status", "--porcelain", "--", f"{fert}/"],
           None, lambda o: o.strip() == "")
    yield ("1b  orphan check", ["bash", "scripts/orphan_check.sh", "FERT"],
           None, lambda o: "[likely YOURS]" not in o)
    yield ("1c-bis ledger nudge", [PY, "scripts/ledger_staleness.py", "--nudge", "FERT"],
           None, lambda o: "nudge:" not in o)
    yield ("1e  claim check (FERT form)", [PY, "scripts/claim_check.py", "--check", "weekday", *claim_paths],
           r"CLAIM-CHECK", lambda o: "CLAIM-CHECK ✓" in o)
    yield ("R1  corrections", [PY, "scripts/corrections_boot_check.py", "FERT"],
           r"CORRECTIONS-CHECK", lambda o: "CORRECTIONS-CHECK 0 OK" in o)
    yield ("RC  read cap", [PY, "scripts/read_cap_check.py", "--agent", "FERT"],
           r"READ-CAP-RESULT v1",
           lambda o: all(re.search(rf"\b{k}=0\b", o) for k in ("over_budget", "over_cap", "rotation_due")))
    yield ("B   boot instrument", [PY, f"{fert}/boot.py"],
           r"FERT boot:", lambda o: "all quiet" in o)
    yield ("T   boot tests", [PY, f"{fert}/test_boot.py"],
           r"^Ran \d+ test", lambda o: re.search(r"^OK", o, re.M) is not None)
    for p in tsv_targets():
        rel = str(p.relative_to(ROOT))
        yield (f"TSV {p.relative_to(HERE)}", [PY, "scripts/tsv_append.py", "--check", rel],
               r": OK \(|inconsistent|mismatch", lambda o: ": OK (" in o)


def main():
    print("=" * 72)
    print("  FERT CLOSEOUT RUNNER — mechanical steps only (does NOT certify the closeout)")
    print("=" * 72)
    tally = {"PASS": 0, "LOOK": 0, "FAIL": 0}
    for name, cmd, marker, passed in steps():
        rc, out = run(cmd)
        verdict, why = classify(rc, out, marker, passed)
        tally[verdict] += 1
        icon = {"PASS": "✅", "LOOK": "👀", "FAIL": "❌"}[verdict]
        print(f"{icon} {verdict:4} {name}  (rc={rc}){'  — ' + why if why else ''}")
        if verdict != "PASS":
            for line in (out or "").splitlines()[:6]:
                print(f"        {line[:150]}")
    rc, out = run(["git", "branch", "-r", "--contains", "HEAD"])
    pushed = rc == 0 and "origin/master" in (out or "")
    print(f"ℹ️  INFO push state: HEAD {'IS' if pushed else 'is NOT'} on origin/master (local refs; safe-push prints the fresh-fetch receipt)")
    print("\nUNVERIFIED BY DESIGN — judgement steps this runner cannot see:")
    for j in ("1c consumer check: did this session supersede a threshold, flip level, split or band? If yes, run it",
              "1d memory-index check: only if an auto-memory was written or edited",
              "STATUS BOTTOM LINE rewritten for THIS session (not just re-stamped)",
              "every trigger consumed this session re-dated or retired in TRIGGERS.tsv",
              "grading cards: only RESULT cells or dated addenda changed after a print",
              "every new price cell carries benchmark + unit + date + source"):
        print(f"   ✍️  {j}")
    print(f"\n  {tally['PASS']} PASS · {tally['LOOK']} LOOK · {tally['FAIL']} FAIL")
    return 2 if tally["FAIL"] else (1 if tally["LOOK"] else 0)


if __name__ == "__main__":
    sys.exit(main())
