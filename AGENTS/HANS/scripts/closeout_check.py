#!/usr/bin/env python3
"""
HANS closeout runner — executes the MECHANICAL closeout steps and reports
RAN / FAILED per step, then NAMES the judgement steps it cannot verify.

WHY THIS EXISTS
---------------
On 2026-09-18 this desk reported a closeout complete with root step 1c's
`--self` form never executed.  Six other checks were green.  No individual
check could see it, because each check reports ITS OWN result and none
reports WHICH STEPS RAN.  A checklist with an item omitted does not look
like a failure; it looks like a shorter checklist.  -> ML-HANS-456

  ⛔ THIS SCRIPT DOES NOT CERTIFY THE CLOSEOUT.
  It certifies that the mechanical steps EXECUTED and what they returned.
  The judgement steps (did the registry actually get the right value? did
  LAST_COMPLETION say something true?) are listed as UNVERIFIED BY DESIGN.
  A runner that claimed to certify those would be the same defect one
  level up: a green light standing in for work nobody did.

Exit: 0 all mechanical steps ran and passed · 1 a step FAILED or errored.
      A non-zero exit never means "closeout invalid" — it means LOOK.
"""
import re, subprocess
import sys
from pathlib import Path

HANS = Path(__file__).resolve().parent.parent
ROOT = HANS.parent.parent


def run(cmd, cwd):
    try:
        p = subprocess.run(cmd, cwd=str(cwd), capture_output=True,
                           text=True, timeout=300)
        return p.returncode, (p.stdout + p.stderr).strip()
    except FileNotFoundError as e:
        return None, f"tool not found: {e}"
    except subprocess.TimeoutExpired:
        return None, "TIMEOUT"
    except Exception as e:                      # fail loud, never silent
        return None, f"{type(e).__name__}: {e}"


# 🔴 `lambda rc: rc is not None` WAS A HOLE THAT ACCEPTED A CRASH. Steps 9a/9b/10 legitimately
# exit NON-ZERO to mean "I found something" (consumer_check flags, ledger_staleness nudges),
# so the predicate was written to accept any rc — and therefore accepted rc=3 from a
# traceback too. Verified 2026-09-19 by injecting a stub that printed "BOOM" and exited 3:
# the runner printed "✅ RAN ... rc=3" for BOTH consumer steps. It only exited 1 because an
# unrelated test failed; crash something no test covers and it certifies 8/8, 0 failed.
# ⛔ THAT IS THIS RUNNER'S OWN FAILURE MODE REPRODUCED — it exists because ML-HANS-456 was
# "six checks green around the one that never ran".
# The fix distinguishes a SIGNALLING exit from a BROKEN one by its documented range: these
# tools signal with 1 (and consumer_check with 2 for a certified-stale finding). Anything
# else, including any rc>=3, is a crash [[finding_lenient_parser_reports_unparseable_as_a_behavior]].
def _crashed(out):
    """Did the tool DIE rather than report? Exit codes cannot answer this.

    🔴 SECOND CORRECTION, 2026-09-19. My first fix accepted rc in (0,1,2) because these
    tools signal with non-zero. CATO then showed a PYTHON TRACEBACK EXITS 1 and a missing
    script exits 2 — both still printed "✅ RAN ... 8/8 executed, 0 failed". I had fixed
    the payload I happened to test (rc=3), not the property.
    THE PROPERTY: a tool that actually ran prints its own verdict; a tool that died prints
    a traceback. So the gate is the OUTPUT, and the exit code is only corroboration.
    """
    low = (out or "").lower()
    return any(m in low for m in (
        "traceback (most recent call last)", "modulenotfounderror", "importerror",
        "no such file or directory", "can't open file", "command not found",
        "syntaxerror", "indentationerror", "unrecognized arguments", "usage:"))


def _ok(rc, out, expect):
    """A step passes only if it did NOT crash AND printed the verdict marker it owes.

    ⛔ AN ABSENT MARKER IS A FAILURE EVEN ON rc=0 — a tool that exits clean while printing
    nothing it promised has not been observed to do its job, and this runner exists
    because ML-HANS-456 was "six checks green around the one that never ran".
    """
    if rc is None or _crashed(out):
        return False
    # 🔴 A MARKER IS NOT A CONTRACT. Substring-presence passed a REAL ERROR whose text
    # happened to contain the marker: `SELF mode: ERROR - nothing scanned` + exit 1 was
    # reported "✅ RAN" (CATO, 2026-09-19). The step must match its own COMPLETION
    # signature — the shape the tool only produces when it ran to the end.
    # re.M as well as re.S: the contracts anchor on a tool's TERMINAL LINE, and without
    # MULTILINE the ^/$ anchors only ever match the whole output. Caught immediately —
    # the tests step failed in the runner while passing standalone.
    if expect and not re.search(expect, out or "", re.S | re.M | re.I):
        return False
    return True


# (step label, argv, cwd, "ok" predicate on rc)
STEPS = [
    ("1  doc_audit (RULE #1b)",
     [sys.executable, "scripts/doc_audit.py"], HANS, (0,), r"HANS DOC AUDIT — \d+ finding"),
    ("8  root 1b · orphan",
     ["bash", "scripts/orphan_check.sh", "HANS"], ROOT, (0,), None),
    ("9a root 1c · consumer CROSS-AGENT",
     [sys.executable, "scripts/consumer_check.py", "--agent", "HANS",
      "--from-ledger"], ROOT, (0, 1, 2), r"CONSUMER CHECK[\s\S]*\n=[=]{9,}\s*$"),
    ("9b root 1c · consumer --SELF  <- the one that went missing",
     [sys.executable, "scripts/consumer_check.py", "--agent", "HANS",
      "--self", "--from-ledger"], ROOT, (0, 1, 2), r"SELF mode[\s\S]*\n=[=]{9,}\s*$"),
    ("10 root 1c-bis · ledger nudge",
     [sys.executable, "scripts/ledger_staleness.py", "--nudge", "HANS"],
     ROOT, (0, 1), r"(nudge:\s*\[HANS\]|\[HANS\][^\n]*ledger)"),
    ("11 root 1e · claim check",
     [sys.executable, "scripts/claim_check.py", "--check", "weekday",
      "AGENTS/HANS/STATUS.md", "AGENTS/HANS/workbook/KB.tsv",
      "AGENTS/HANS/registry/THRESHOLDS.tsv"], ROOT, (0,), r"CLAIM-CHECK"),
    ("12 tests",
     [sys.executable, "scripts/test_hans.py"], HANS, (0,), r"^Ran \d+ tests[\s\S]*^OK\s*$"),
    ("12 read-cap",
     [sys.executable, "scripts/read_cap_check.py", "--agent", "HANS"],
     ROOT, (0,), r"READ-CAP-RESULT v1[^\n]*rc=\d"),
]

# Steps whose CONTENT no script can judge.  Named so they are visible as
# obligations rather than absent as omissions.
JUDGEMENT = [
    ("2  registry + fired log",
     "did every threshold you touched get current_value/as_of/state, or a "
     "stated no-op?  did a count mirror change?"),
    ("3  VX metric surfaces", "does every moved threshold's VX row agree?"),
    ("4  KB.tsv",
     "new facts added; superseded not overwritten; status tokens from "
     "STATE_VOCABULARY.md (RULE #1c)"),
    ("5  PREDICTIONS + FLOW",
     "a due/drifting prediction tracked; a chain whose trigger leg moved "
     "updated; ledger nudge ANSWERED not dismissed"),
    ("6  PUBLISHED.tsv",
     "every figure published to a desk or to Will, INCLUDING ONE YOU "
     "WITHDREW -- and CONTINUING the established metric name (ML-HANS-455)"),
    ("7  LAST_COMPLETION.md",
     "overwritten this session?  it sat 2 months stale asserting "
     "'WILL_NEEDS: None'"),
    ("9c consumer-check dispositions",
     "cross-agent RED -> packet the owner, never edit their files.  self "
     "RED on a graded table / dated log / archive / PUBLISHED.tsv -> DO NOT "
     "CLEAR; that is resolving a flag backwards"),
    ("11 root 1d · memory-index", "ONLY if an auto-memory was written"),
]


def main():
    print("=" * 74)
    print("  HANS CLOSEOUT RUNNER — did the mechanical steps EXECUTE?")
    print("=" * 74)
    failed, ran = [], 0
    for label, cmd, cwd, codes, expect in STEPS:
        rc, out = run(cmd, cwd)
        if rc is None:
            print(f"  ⛔ ERROR   {label}\n              {out.splitlines()[0][:90]}")
            failed.append(label)
            continue
        ran += 1
        if _ok(rc, out, expect) and rc in codes:
            tail = out.strip().splitlines()
            note = tail[-1][:78] if tail else ""
            print(f"  ✅ RAN     {label}   rc={rc}")
            if note:
                print(f"              {note}")
        else:
            print(f"  🔴 FAILED  {label}   rc={rc}")
            for ln in out.strip().splitlines()[-3:]:
                print(f"              {ln[:88]}")
            failed.append(label)

    print("\n" + "-" * 74)
    print(f"  MECHANICAL: {ran}/{len(STEPS)} executed · {len(failed)} failed")
    print("-" * 74)
    print("  ⛔ NOT VERIFIED BY THIS SCRIPT — judgement steps, listed so they")
    print("     are visible as obligations rather than absent as omissions:")
    for label, ask in JUDGEMENT:
        print(f"     ·  {label:34s} {ask[:70]}")
        if len(ask) > 70:
            print(f"        {'':34s} {ask[70:150]}")

    print("\n  ⚠️  A clean run means THE STEPS EXECUTED, never that the closeout")
    print("      is correct.  This script cannot read what you wrote.")
    if failed:
        print(f"\n  EXIT 1 — {len(failed)} step(s) need a look: {', '.join(f.split()[0] for f in failed)}")
        return 1
    print("\n  EXIT 0 — every mechanical step executed and passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
