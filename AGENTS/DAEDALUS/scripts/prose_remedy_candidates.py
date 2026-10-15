#!/usr/bin/env python3
"""prose_remedy_candidates.py — Prose-Remedy Census step 1 (candidate GENERATOR, never a verdict).

Playbook: AGENTS/DAEDALUS/sweeps/PROSE_REMEDY_SWEEP.md §1. Run #1 (2026-10-08) ran this step as an
inline one-off; its record (runs/2026-10-08_PROSE_REMEDY_CENSUS_01.md "Step-1 refinement for run #2")
named five fixes. This file is those fixes typed (H-4: a remedy carried as prose is the defect):
  R1 word boundaries on every token ('owed' matched 'windowed')
  R2 negated forms excluded PER OCCURRENCE ('no … owed', 'nothing owed', 'owed none')
  R3 resolved text excluded: a line LED by ✅, a token inside ~~struck~~ text, or a ✅ in the same
     clause just before the token — never a whole line for a ✅ elsewhere on it (a mixed line such as
     "④ STILL OWED … ✅ done-item" keeps its live token; found on the first real-tree run 10/14)
  R4 form-2 ID ranges excluded only when an ID word governs them ('rows ≤223', 'IDs ≥100') or the
     'HAW-18+' shape — a bare '≤280' is a THRESHOLD (SHADE's HY sustain bar), never an ID
  R5 widening: 'not patched' · 'not attempted' (missed FLG STATUS · MARCO/ORACLE MAINTENANCE)
  R6 perimeter from PROME/ROSTER.md via render_directory.parse_roster: ACTIVE + TIER-2 + SPECIAL
     (DAEDALUS, RAV); DORMANT out (SENTRY slipped in at run #1); CATO out by ruling (WQ-255).
     PROME lives at PROME/, never AGENTS/PROME/ (root CLAUDE.md) — mapped explicitly.

The playbook forbids a widening without a fleet before/after diff, so every run computes BOTH
pattern versions (v1 = run #1 as written in the playbook, v2 = this) over the same tree and prints
what each change added and removed.

Usage:  prose_remedy_candidates.py [--out PATH.tsv]   ·   prose_remedy_candidates.py --selftest
rc: 0 candidates generated (any count, including 0 for a desk) · 2 CANNOT-EVALUATE (ROSTER unparseable
or the perimeter came out empty — an empty population certifies nothing, PAT-155).
A candidate is a line to CLASSIFY (step 2), never a finding.
"""
import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))

SURFACES = ["STATUS.md", "SCRATCH.md", "CANARY_MAP.md", "MAINTENANCE.md", "LAST_COMPLETION.md", "CLAUDE.md"]
SPECIAL_IN = ["DAEDALUS", "RAV"]          # render_directory.SPECIAL keys; CATO excluded by WQ-255
SCRIPT = re.compile(r"\b[\w-]+\.py\b")

V1_TOKENS = (r"queued|owed|not yet (built|wired)|unbuilt|un-wired|BUILT-UNWIRED|fix pending|"
             r"should (be|compute|check|compare)|needs? (a|an|to)|TODO|remedy|as a sentence|as prose|"
             r"not a check|never computed|nothing (checks|computes|compares)")
V1 = re.compile(V1_TOKENS)
V2 = re.compile(r"\b(?:" + V1_TOKENS + r"|not patched|not attempted)\b")          # R1 + R5
NEG_BEFORE = re.compile(r"\b(?:no|nothing|not|none)\b[^.;|,()]{0,30}$", re.I)       # R2, window before
NEG_AFTER = re.compile(r"^\s*(?:none|nothing)\b", re.I)                               # R2, 'owed none'
LEAD_DONE = re.compile(r"^[-*|#>\s]*(?:\*\*)?✅")   # R3 line-led ✅ — ONE char class: a nested (x+\s*)* hung on "|---|---|" rows (10/14)
STRUCK = re.compile(r"~~[^~]*~~")
FORM2 = re.compile(r"≥|>=|≤|<=|must not lag|\b\d+ consecutive\b|\bunder \d[\d,]* (?:lines|bytes|B)\b")
ID_RANGE = re.compile(r"\b(?:rows?|IDs?|entries|lines? L)\s*[≤≥<>]=?\s?\d+(?![\d.,]*\s?(?:%|bp|B\b|lines|ln\b|bytes|cm|pp|d\b|days|KB|MB))|\b[A-Z]{2,6}-\d+\+")  # R4 — a unit after the number makes it a threshold (LABOR "row ≥60% confidence", 10/14)


def v2_form1(line):
    if not SCRIPT.search(line):
        return False
    if LEAD_DONE.search(line):                                         # R3
        return False
    bare = STRUCK.sub(" ", line)                                       # R3
    for x in V2.finditer(bare):
        before = bare[max(0, x.start() - 40):x.start()]
        clause = re.split(r"[.;|]", before)[-1]
        if "✅" in clause:                                             # R3, same clause
            continue
        if x.group(0) == "owed" and (NEG_BEFORE.search(before) or NEG_AFTER.search(bare[x.end():])):
            continue                                                   # R2
        return True
    return False


def v1_form1(line):
    return bool(SCRIPT.search(line) and V1.search(line))


def v2_form2(line):
    if SCRIPT.search(line) or LEAD_DONE.search(line):
        return False
    bare = ID_RANGE.sub(" ", STRUCK.sub(" ", line))                    # R3 + R4
    return bool(FORM2.search(bare))


def v1_form2(line):
    return bool(FORM2.search(line)) and not SCRIPT.search(line)


def desk_dir(a):
    return REPO / "PROME" if a == "PROME" else REPO / "AGENTS" / a


def perimeter():
    import render_directory as rd
    agents, _ = rd.parse_roster(rd.ROSTER)
    names = [a for a, (grp, _) in agents.items() if grp in ("ACTIVE", "TIER-2")] + SPECIAL_IN
    out, missing = [], []
    for a in names:
        (out if desk_dir(a).is_dir() else missing).append(a)
    return out, missing


def scan(desks):
    rows = {"v1": set(), "v2": set()}
    read_files = 0
    for desk in desks:
        for name in SURFACES:
            p = desk_dir(desk) / name
            if not p.is_file():
                continue
            read_files += 1
            for i, line in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                key = lambda form: (desk, form, name, i, line.strip()[:400])
                if v1_form1(line):
                    rows["v1"].add(key("1-script+token"))
                if v2_form1(line):
                    rows["v2"].add(key("1-script+token"))
                if name == "CLAUDE.md":
                    if v1_form2(line):
                        rows["v1"].add(key("2-charter-comparison"))
                    if v2_form2(line):
                        rows["v2"].add(key("2-charter-comparison"))
    return rows, read_files


def selftest():
    cases = [
        ("R1 'windowed' is not 'owed'", v2_form1("boot.py windowed check"), False, v1_form1("boot.py windowed check"), True),
        ("R2 negated owed", v2_form1("fetch.py — no fix owed"), False, v1_form1("fetch.py — no fix owed"), True),
        ("R2 bare owed still hits", v2_form1("fetch.py fix owed since 9/2"), True, None, None),
        ("R3 ✅-led line", v2_form1("- ✅ boot.py remedy built 9/4"), False, None, None),
        ("R3 mixed line keeps live token", v2_form1("④ STILL OWED, named as owed: x.py ✅ done item"), True, None, None),
        ("R3 ✅ in same clause", v2_form1("x.py ✅ fixed, was queued"), False, None, None),
        ("R2 owed none", v2_form1("x.py: terminal rows are owed none"), False, None, None),
        ("R2 per occurrence", v2_form1("x.py: no packet owed; review owed to RED"), True, None, None),
        ("R3 struck token", v2_form1("boot.py ~~queued~~ done"), False, None, None),
        ("R5 not patched", v2_form1("strike_feed.py not patched yet"), True, v1_form1("strike_feed.py not patched yet"), False),
        ("R5 not attempted", v2_form1("pull.py re-pull not attempted"), True, None, None),
        ("control: should compare", v2_form1("boot.py should compare X to Y"), True, v1_form1("boot.py should compare X to Y"), True),
        ("R4 ID range ≤223", v2_form2("rows ≤223 are legacy"), False, v1_form2("rows ≤223 are legacy"), True),
        ("R4 bare ≤280 is a threshold", v2_form2("a run breaks on any session ≤280."), True, None, None),
        ("R4 ≤ 153 cm is a threshold", v2_form2("daily mean ≤ 153 cm"), True, None, None),
        ("R4 row ≥60% is a threshold", v2_form2("over every OPEN row ≥60% confidence"), True, None, None),
        ("R4 ID+ range", v2_form2("HAW-18+ use the new form ≥"), True, None, None),
        ("R4 real threshold kept", v2_form2("STATUS stays ≤ 32,550 B"), True, None, None),
        ("R4 percent threshold kept", v2_form2("alert when share ≥150%"), True, None, None),
        ("form 2 never on a script line", v2_form2("check.py asserts ≥ 3"), False, None, None),
    ]
    bad = 0
    for name, got2, want2, got1, want1 in cases:
        ok = got2 == want2 and (want1 is None or got1 == want1)
        bad += not ok
        print(f"  {'✓' if ok else '✗'} {name}: v2={got2} (want {want2})" + ("" if want1 is None else f" · v1={got1} (want {want1})"))
    desks, missing = perimeter()
    pc = ("SENTRY" not in desks) and ("CATO" not in desks) and ("RAV" in desks or "RAV" in missing) and ("DAEDALUS" in desks) and ("PROME" in desks)
    bad += not pc
    print(f"  {'✓' if pc else '✗'} R6 perimeter: {len(desks)} desks, SENTRY out, CATO out, DAEDALUS+RAV+PROME in")
    print(f"PROSE-REMEDY-CANDIDATES SELFTEST {'✓' if not bad else '✗'} {len(cases) + 1 - bad}/{len(cases) + 1}")
    return 0 if not bad else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(selftest())
    try:
        desks, missing = perimeter()
    except SystemExit as e:
        print(f"PROSE-REMEDY-CANDIDATES CANNOT-EVALUATE: ROSTER parse failed ({e})")
        sys.exit(2)
    if not desks:
        print("PROSE-REMEDY-CANDIDATES CANNOT-EVALUATE: empty perimeter")
        sys.exit(2)
    rows, nfiles = scan(desks)
    added, removed = rows["v2"] - rows["v1"], rows["v1"] - rows["v2"]
    per = {}
    for r in rows["v2"]:
        per[r[0]] = per.get(r[0], 0) + 1
    print(f"PROSE-REMEDY-CANDIDATES v2: {len(rows['v2'])} candidate line(s) over {len(desks)} desks / {nfiles} files "
          f"(v1 on the same tree: {len(rows['v1'])}; v2 added {len(added)}, removed {len(removed)}). "
          f"No directory: {', '.join(missing) or 'none'}. Desks with 0 candidates: "
          f"{', '.join(sorted(set(desks) - set(per))) or 'none'}. A candidate is a line to classify, never a finding.")
    for tag, s in (("ADDED-BY-V2", added), ("REMOVED-BY-V2", removed)):
        for r in sorted(s):
            print(f"  {tag}\t{r[0]}\t{r[1]}\t{r[2]}:{r[3]}\t{r[4][:140]}")
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write("desk\tform\tfile\tline\ttext\n")
            for r in sorted(rows["v2"]):
                f.write("\t".join([r[0], r[1], r[2], str(r[3]), r[4].replace("\t", " ")]) + "\n")
        print(f"  written: {a.out}")
    sys.exit(0)


if __name__ == "__main__":
    main()
