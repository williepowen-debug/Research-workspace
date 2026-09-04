#!/usr/bin/env python3
"""walter_route_check.py — census of ROUTE-AROUND-WALTER instructions in desk canon.

Commissioned: PROME packet 2026-09-02 (item 2), off OTTO 16d78369b / LIQUID ff478f328.
Owner: DAEDALUS.

STANDARD GRADED AGAINST (verified at the artifact, not asserted):
  - MESSAGING/CROSS_SESSION_MESSAGING.md sec2 rule 4: "WALTER's mandate is not bypassed.
    Market signals/news/intelligence route through WALTER's lanes (dedupe, archive,
    routing judgment). ... WALTER owns the semantics of what counts as a signal."
  - root CLAUDE.md: "never route signals around WALTER"
  - root CLAUDE.md carve-out (1): a PACKET you authored into another agent's inbox is
    legitimate and must be self-committed. So direct PACKETS are fine; direct SIGNALS
    are not. That distinction is the whole classifier.
  - LIQUID's own corrected rule states it best (AGENTS/LIQUID/CLAUDE.md, 2026-09-03):
    "SIGNALS go to WALTER for routing. ANALYSIS goes direct."

*** DECLARED PERIMETER — this checker is BLIND to one of the two known defect forms. ***
Leg A (implemented here) is a PHRASE detector: it finds an instruction that says, in
words, "deliver the signal directly to the target's inbox". That is the LIQUID form.
Leg B is the OTTO form and is NOT phrase-detectable: OTTO's route-around was EMERGENT
from juxtaposition -- a trigger table whose rows name recipient desks (CARL, REGINALD,
PROME) sitting above a "How to Signal" section that never mentions WALTER. No single
line is wrong; the pair is. Leg B stays agent-judged. Every verdict this tool prints
carries that perimeter, per READ_CAP.md enforcement convention
(finding_instrument_reports_clean_against_the_wrong_reference).

POSITIVE CONTROL (CHECK_STANDARD sec3 / WQ-117 B): --selftest replays the two known
pre-fix files out of git and asserts the expected split -- LIQUID pre-fix MUST hit,
OTTO pre-fix MUST NOT (that miss is the declared blind spot, so a hit there would mean
the classifier had drifted). rc=2 CANNOT-CERTIFY if the control cannot be run at all.

rc contract (CHECK_STANDARD sec9): 0 = no ROUTE-AROUND rows · 1 = >=1 ROUTE-AROUND row
· 2 = cannot certify (control unrunnable / no files found).
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                           capture_output=True, text=True, check=True).stdout.strip())

# --- the phrase set, derived FROM the known positives, not invented ---
DIRECT = re.compile(
    r"(directly|direct)\s+(to|into)\s+(the\s+)?(target|recipient)?[^.\n]{0,40}?inbox"
    r"|inbox[^.\n]{0,25}?\bdirectly\b"
    r"|go\s+direct(ly)?\s+to[^.\n]{0,40}?inbox"
    r"|drop\s+the\s+packet\s+in\s+the\s+target[^.\n]{0,30}?inbox",
    re.I)
SIGNALWORD = re.compile(r"\bsignals?\b", re.I)
WALTERWORD = re.compile(r"\bWALTER\b")
# HERMES retired 2026-06-30. Present-tense delivery claims are a DEAD-ROUTER defect:
# a signal written per that instruction reaches nobody at all.
HERMES_LIVE = re.compile(
    r"HERMES\s+(will\s+deliver|sweeps|delivers|picks\s+up)"
    r"|delivered\s+by\s+HERMES"
    r"|moved\s+here\s+by\s+HERMES",
    re.I)
# explicit prohibitions and already-corrected lines are the counter-examples
NEGATED = re.compile(
    r"do\s+not\s+write\s+directly|not\s+write\s+directly|never\s+write\s+directly"
    r"|outbox,\s*not\s+other\s+agents|CORRECTED\s+20|pointed\s+AROUND\s+WALTER"
    r"|as\s+it\s+should\s+have\s+read|\bFROZEN\b|Deprecated|deprecated\s+—\s+legacy",
    re.I)

# TWO-LANE (2026-09-03, CRUISE instrument feedback): the CORRECT rule necessarily names BOTH lanes
# in one sentence — "a SIGNAL goes to WALTER … an ANALYSIS or PACKET goes direct" — so the phrase
# matcher scored every desk that did exactly what the census asked as MIXED, and a MIXED bucket
# read as owed work would re-flag compliant desks (BRENT/CARL/CORAL/HANS/HENRY/REGINALD/SAM sat
# there). A line that routes SIGNALS to WALTER and PACKETS/ANALYSIS direct is the two-lane rule,
# not a mixture: PASS-class, never owed.
TWO_LANE = re.compile(
    r"signals?\b[^.;\n]{0,80}\bWALTER\b[^.;\n]{0,160}\b(analys[ei]s|packets?|memo)\b[^.;\n]{0,80}\bdirect"
    r"|\b(analys[ei]s|packets?|memo)\b[^.;\n]{0,80}\bdirect[^.;\n]{0,160}signals?\b[^.;\n]{0,80}\bWALTER\b"
    r"|signals?\b[^.;\n]{0,40}(?:→|->|to|via|through)\s*WALTER\b",
    re.I)

CANON_NAMES = ("CLAUDE.md", "PROTOCOL.md", "CLOSEOUT.md", "BOOT.md")


def classify(line):
    """Return (verdict, why) or None if the line is not about direct delivery."""
    if NEGATED.search(line):
        return ("CORRECT", "explicit prohibition / already-corrected line")
    if HERMES_LIVE.search(line):
        return ("DEAD-ROUTER", "instructs delivery via HERMES, retired 2026-06-30")
    if not DIRECT.search(line):
        return None
    if SIGNALWORD.search(line):
        if WALTERWORD.search(line):
            if TWO_LANE.search(line):
                return ("TWO-LANE", "signals → WALTER and packets/analysis → direct, both lanes on one line (the prescribed form)")
            return ("MIXED", "signal + direct-to-inbox, but WALTER named on the line — read it: under-specified, or a two-lane rule the matcher missed")
        return ("ROUTE-AROUND", "SIGNAL delivered direct to inbox, WALTER not named")
    if WALTERWORD.search(line):
        return ("MIXED", "direct-to-inbox with WALTER named")
    return ("PACKET-LANE", "direct-to-inbox, not scoped to 'signal' (carve-out 1 lane)")


def scan_text(text, label):
    out = []
    for n, line in enumerate(text.split("\n"), 1):
        v = classify(line)
        if v:
            out.append((label, n, v[0], v[1], line.strip()))
    return out


def scan_tree():
    rows = []
    for d in sorted((ROOT / "AGENTS").iterdir()):
        if not d.is_dir() or d.name.startswith("_"):
            continue
        for name in CANON_NAMES:
            f = d / name
            if f.exists():
                rows += scan_text(f.read_text(encoding="utf-8", errors="replace"),
                                  f"{d.name}/{name}")
    return rows


def git_show(ref):
    r = subprocess.run(["git", "-C", str(ROOT), "show", ref],
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def selftest():
    """Positive control with a DECLARED expected split."""
    print("POSITIVE CONTROL (replays the two known pre-fix files out of git)")
    liq = git_show("ff478f328^:AGENTS/LIQUID/CLAUDE.md")
    otto = git_show("16d78369b^:AGENTS/OTTO/CLAUDE.md")
    if liq is None or otto is None:
        print("  rc=2 CANNOT-CERTIFY: control blobs unreachable "
              "(shallow clone or rewritten history)")
        return 2
    lh = [r for r in scan_text(liq, "LIQUID@pre-fix") if r[2] == "ROUTE-AROUND"]
    oh = [r for r in scan_text(otto, "OTTO@pre-fix") if r[2] == "ROUTE-AROUND"]
    ok = True
    if lh:
        print(f"  PASS  LIQUID pre-fix: {len(lh)} ROUTE-AROUND row(s) found (expected >=1)")
        for r in lh:
            print(f"          L{r[1]}: {r[4][:120]}")
    else:
        print("  FAIL  LIQUID pre-fix: 0 hits -- the phrase set has DRIFTED "
              "(the fleet is not clean; the pattern set is wrong)")
        ok = False
    if oh:
        print(f"  FAIL  OTTO pre-fix: {len(oh)} hit(s) -- classifier drifted; the OTTO "
              "defect is structural, not phrasal, and must NOT match by phrase")
        ok = False
    else:
        print("  PASS  OTTO pre-fix: 0 hits, AS EXPECTED -- confirms the declared blind "
              "spot. OTTO's route-around was a trigger table naming recipient desks above "
              "a 'How to Signal' section omitting WALTER. Leg B stays agent-judged.")
    print("  => the phrase detector covers the LIQUID class only. "
          "Any 'fleet clean' claim from this tool is a claim about leg A alone.")
    return 0 if ok else 2


def main():
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    rc_ctl = selftest()
    print()
    rows = scan_tree()
    if not rows:
        print("rc=2 CANNOT-CERTIFY: no desk canon files scanned")
        sys.exit(2)
    order = ["ROUTE-AROUND", "DEAD-ROUTER", "MIXED", "PACKET-LANE", "TWO-LANE", "CORRECT"]
    counts = {k: 0 for k in order}
    for k in order:
        hits = [r for r in rows if r[2] == k]
        counts[k] = len(hits)
        if not hits or k in ("CORRECT", "TWO-LANE"):
            continue
        mark = {"ROUTE-AROUND": "[X]", "DEAD-ROUTER": "[X]",
                "MIXED": "[!]", "PACKET-LANE": "[i]"}[k]
        print(f"{mark} {k} — {len(hits)} row(s)")
        for lbl, n, _, why, line in hits:
            print(f"    {lbl}:{n}  {line[:150]}")
        print()
    desks = sorted({r[0].split('/')[0] for r in rows
                    if r[2] in ("ROUTE-AROUND", "DEAD-ROUTER")})
    print(f"CENSUS: {counts['ROUTE-AROUND']} ROUTE-AROUND · "
          f"{counts['DEAD-ROUTER']} DEAD-ROUTER · {counts['MIXED']} MIXED (read, not owed) · "
          f"{counts['PACKET-LANE']} PACKET-LANE · {counts['TWO-LANE']} TWO-LANE (pass) · {counts['CORRECT']} CORRECT")
    print(f"DESKS OWED A PACKET ({len(desks)}): {', '.join(desks)}")
    print("PERIMETER: leg A (phrase) only. Leg B (OTTO structural form: recipient-named "
          "trigger table + WALTER-less signal instruction) is NOT covered here and is "
          "agent-judged. A clean leg-A run is not a clean desk.")
    if rc_ctl == 2:
        print("rc=2 CANNOT-CERTIFY (positive control did not pass)")
        sys.exit(2)
    sys.exit(1 if (counts["ROUTE-AROUND"] or counts["DEAD-ROUTER"]) else 0)


if __name__ == "__main__":
    main()
