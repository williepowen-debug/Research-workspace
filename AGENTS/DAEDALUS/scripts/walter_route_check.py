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

rc contract (CHECK_STANDARD sec9): 0 = no ROUTE-AROUND or DEAD-ROUTER rows · 1 = >=1 ROUTE-AROUND
or DEAD-ROUTER row in ANY scanned charter, a RETIRED desk's charter included · 2 = cannot certify
(control unrunnable / no files found). (Before 2026-09-24 this line named ROUTE-AROUND only, although
the code has always exited 1 on DEAD-ROUTER too. The line was corrected to match the code, and the rc
itself is unchanged.)
rc is a claim about CANON TEXT, not about OWED WORK. Every run prints an "RC BASIS" line stating how
many of the rc-driving rows sit on RETIRED desks, so rc=1 and "DESKS OWED (0)" cannot be read as one
claim. The two 2026-09-24 additions below are reporting only and never move the rc (ruling
2026-09-24, team-lead: the docstring defines rc on rows, so the rc stays and the basis line is added).

WALTER-LANE DROP COUNT (added 2026-09-24, OTTO correction a84f5a9ca): per desk, the distinct files
git ever ADDED under AGENTS/WALTER/inbox/**, in BOTH sender forms, and each form is reported:
  from-<AGENT>            e.g. 2026-08-28_from-LABOR_cc-routing-record.md   (anchored at ^ or _)
  SIG-<AGENT>-WALTER-     e.g. SIG-OTTO-WALTER-20260902-002-....md          (OTTO's lane, CLAUDE.md:185)
The agent token is case-insensitive. The 9/17 judgment counted OTTO "0 all-time" because a hand grep matched
only the from- form; git shows 17 of the SIG form. PERIMETER: git-added files only (untracked drops are
invisible). Filenames with no sender token (*_handoff.md, *_to-WALTER_*, README) are counted as
UNATTRIBUTED and printed, never assigned to a desk. `--drops [DESK ...]` prints the table alone
(rc 0 = printed · 2 = git log failed).

ROSTER SCREEN (added 2026-09-24, DAEDALUS 9/18 rider): a desk ROSTER marks RETIRED (its '## RETIRED'
section or a bold '**NAME** — RETIRED' line; parser = render_directory.retired_from_roster, reused and
not copied) is printed "RETIRED — not owed" instead of in DESKS OWED. An ask of a retired desk can never
be discharged. If ROSTER is unreadable, the OWED line says UNSCREENED.
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


DROP_FORMS = (
    ("from-<AGENT>", re.compile(r"(?:^|_)from-([A-Za-z0-9]+)", re.I)),
    ("SIG-<AGENT>-WALTER-", re.compile(r"^SIG-([A-Za-z0-9]+)-WALTER-", re.I)),
)


def walter_drops():
    """-> ({AGENT: {form: {basename: first_added_date}}}, [unattributed basenames]) or None if git fails.
    Distinct BASENAMES, so a file re-added under processed/ counts once."""
    r = subprocess.run(["git", "-C", str(ROOT), "log", "--format=@%cs", "--diff-filter=A",
                        "--name-only", "--", "AGENTS/WALTER/inbox/**"],
                       capture_output=True, text=True)
    if r.returncode != 0 or not r.stdout.strip():
        return None
    by, unattr, day = {}, set(), None
    for ln in r.stdout.splitlines():
        if ln.startswith("@"):
            day = ln[1:]
            continue
        if not ln.strip():
            continue
        b = ln.rsplit("/", 1)[-1]
        for form, rx in DROP_FORMS:
            m = rx.search(b)
            if m:
                slot = by.setdefault(m.group(1).upper(), {}).setdefault(form, {})
                slot[b] = min(day, slot.get(b, day))   # git log is newest-first; keep the earliest
                break
        else:
            unattr.add(b)
    return by, sorted(unattr)


def drop_line(agent, by):
    forms = by.get(agent.upper(), {})
    files = set().union(*forms.values()) if forms else set()
    dates = sorted(d for f in forms.values() for d in f.values())
    parts = " · ".join(f"{form}: {len(forms.get(form, {}))}" for form, _ in DROP_FORMS)
    span = f", first {dates[0]} · last {dates[-1]}" if dates else ""
    return f"{agent}: {len(files)} WALTER-lane drop(s) all-time ({parts}{span})"


def roster_retired():
    """Names ROSTER marks RETIRED, via render_directory's parser (one parser, not two). None = unreadable."""
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from render_directory import retired_from_roster
        return retired_from_roster(ROOT / "PROME" / "ROSTER.md")
    except Exception as e:                      # fail visible, never silently unscreened
        print(f"ROSTER SCREEN UNAVAILABLE: {type(e).__name__}: {e}")
        return None


RC_CLASSES = ("ROUTE-AROUND", "DEAD-ROUTER")


def census_rc(rows):
    """The rc contract, in one place: 1 iff any rc-class row exists in ANY scanned charter."""
    return 1 if any(r[2] in RC_CLASSES for r in rows) else 0


def owed_split(rows, retired):
    """-> (owed desks, retired desks, rc-class row count, of which on retired desks). retired=None: unscreened."""
    rc_rows = [r for r in rows if r[2] in RC_CLASSES]
    desks = sorted({r[0].split('/')[0] for r in rc_rows})
    if retired is None:
        return desks, [], len(rc_rows), None
    gone = [x for x in desks if x.upper() in retired]
    n_ret = sum(1 for r in rc_rows if r[0].split('/')[0].upper() in retired)
    return [x for x in desks if x.upper() not in retired], gone, len(rc_rows), n_ret


def rc_basis_line(n_rc, n_ret):
    split = ("retired split UNKNOWN — ROSTER unreadable" if n_ret is None
             else f"{n_ret} of them on RETIRED desks")
    return (f"RC BASIS: rc={1 if n_rc else 0} counts {n_rc} ROUTE-AROUND/DEAD-ROUTER row(s) in EVERY scanned "
            f"charter ({split}); DESKS OWED lists live desks only — rc=1 is a claim about canon text, "
            f"not about work owed.")


def drill_retired_only():
    """Drill (2026-09-24 ruling): a census whose ONLY rc-class row is on a retired desk must print
    OWED none + that desk as retired, and still return rc 1 with the basis line naming the split.
    Uses the same helpers main() uses. Control arm: an active desk stays OWED."""
    ok = True
    ret = {"YEYOU"}
    only = [("YEYOU/CLAUDE.md", 1, "ROUTE-AROUND", "drill", "drill")]
    owed, gone, n, nr = owed_split(only, ret)
    if (owed, gone, n, nr, census_rc(only)) == ([], ["YEYOU"], 1, 1, 1):
        print("  PASS  retired-only drill: OWED none · RETIRED YEYOU · rc=1 · basis '1 of them on RETIRED desks'")
    else:
        print(f"  FAIL  retired-only drill: got owed={owed} gone={gone} n={n} n_ret={nr} rc={census_rc(only)}")
        ok = False
    mixed = only + [("LIQUID/CLAUDE.md", 2, "ROUTE-AROUND", "drill", "drill")]
    owed, gone, n, nr = owed_split(mixed, ret)
    if (owed, gone, n, nr) == (["LIQUID"], ["YEYOU"], 2, 1):
        print("  PASS  control arm: active LIQUID stays OWED beside retired YEYOU")
    else:
        print(f"  FAIL  control arm: got owed={owed} gone={gone} n={n} n_ret={nr}")
        ok = False
    return ok


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
    ok = drill_retired_only() and ok
    return 0 if ok else 2


def main():
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    if "--drops" in sys.argv:
        d = walter_drops()
        if d is None:
            print("rc=2 CANNOT-CERTIFY: git log over AGENTS/WALTER/inbox/** failed or returned nothing")
            sys.exit(2)
        by, unattr = d
        names = [a.upper() for a in sys.argv[sys.argv.index("--drops") + 1:] if not a.startswith("-")]
        print("WALTER-LANE DROPS (git-added files under AGENTS/WALTER/inbox/**, distinct basenames; "
              "forms: " + ", ".join(f for f, _ in DROP_FORMS) + ")")
        for a in (names or sorted(by)):
            print("  " + drop_line(a, by))
        print(f"  UNATTRIBUTED (no sender token, not assigned to any desk): {len(unattr)}")
        sys.exit(0)
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
    print(f"CENSUS: {counts['ROUTE-AROUND']} ROUTE-AROUND · "
          f"{counts['DEAD-ROUTER']} DEAD-ROUTER · {counts['MIXED']} MIXED (read, not owed) · "
          f"{counts['PACKET-LANE']} PACKET-LANE · {counts['TWO-LANE']} TWO-LANE (pass) · {counts['CORRECT']} CORRECT")
    retired = roster_retired()
    desks, gone, n_rc, n_ret = owed_split(rows, retired)
    if retired is None:
        print(f"DESKS OWED A PACKET ({len(desks)}, UNSCREENED — ROSTER unreadable): {', '.join(desks) or 'none'}")
    else:
        print(f"DESKS OWED A PACKET ({len(desks)}): {', '.join(desks) or 'none'}")
        for x in gone:
            print(f"RETIRED — not owed: {x} (PROME/ROSTER.md marks it RETIRED; its canon rows still count toward rc)")
    print(rc_basis_line(n_rc, n_ret))
    d = walter_drops()
    flagged = sorted({r[0].split('/')[0] for r in rows if r[2] in ("ROUTE-AROUND", "DEAD-ROUTER")})
    if flagged:
        if d is None:
            print("WALTER-LANE DROPS: UNKNOWN (git log over AGENTS/WALTER/inbox/** failed)")
        else:
            print("WALTER-LANE DROPS for flagged desks (practice beside canon):")
            for x in flagged:
                print("    " + drop_line(x, d[0]))
    print("PERIMETER: leg A (phrase) only. Leg B (OTTO structural form: recipient-named "
          "trigger table + WALTER-less signal instruction) is NOT covered here and is "
          "agent-judged. A clean leg-A run is not a clean desk.")
    if rc_ctl == 2:
        print("rc=2 CANNOT-CERTIFY (positive control did not pass)")
        sys.exit(2)
    sys.exit(census_rc(rows))


if __name__ == "__main__":
    main()
