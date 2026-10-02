#!/usr/bin/env python3
"""
BROCK self-check: three NARROW closeout checks. BROCK-scoped; reads nothing outside AGENTS/BROCK/.

Adopted 2026-10-02 from CREED's scripts/creed_selfcheck.py (Will: "adopt as much as you think is
valuable"). WHY: on 2026-10-02 VX-BRK-004 still read "three vehicles at 2 [9/3]" after GATE-BRK-R2
(a) had FIRED twice (North Haven 9/25, OCIC 10/2), and the STATUS matrix row said "0 fired" two
lines after recording both fires. consumer_check scans superseded VALUES; this is a superseded
STATE, a different object, so a clean consumer_check meant nothing. CREED's name for it: a grade is
not a propagation.

DELIBERATELY NOT A GENERAL CLAIM DETECTOR. Each check is file-level and enumerable, so a flag is
actionable. Every surface it reads is BROCK-owned, so it can never block on another desk's work.

  python3 AGENTS/BROCK/scripts/brock_selfcheck.py [--root DIR]

exit 0 = clean, exit 1 = findings, exit 2 = cannot run (a required surface is missing).

CHECK 1  fire / resolution propagation
  1a  Gates with a FIRE RECORD line in workbook/PC_REDEMPTION_REGISTER.tsv: every LIVE line on
      STATUS.md, workbook/VX.tsv and docket/CATALYSTS.tsv (future-dated rows only) that names the
      gate must carry FIRED, and none may assert "0 fired".
  1b  Predictions whose PREDICTIONS.tsv Status is RESOLVED-*: no LIVE line on STATUS.md that names
      the ID may say it is open / not graded / stays open.
  HISTORY SEGMENTS are stripped before the test, never whole lines: text from a marker
  (PRIOR CELL, PRIOR NOTE, Original row, Pre-grade record, Superseded text, earlier stamp) to the
  end of that cell. v1 exempted any LINE with a marker and so MISSED VX-BRK-004 itself (its
  Current_Value carried "PRIOR CELL:"); falsified on the pre-fix files 2026-10-02 and replaced.
  Scope limit, stated: only these phrasings. Add one in the same edit that introduces it.
CHECK 2  asserted counts on STATUS.md
  matrix scores sum == "Convergence: X/Y" X; Y == 5 x vector rows; "(N vectors)" == rows.
CHECK 3  field counts: every data row of workbook/KB.tsv and workbook/VX.tsv has 13 fields
  (LESSONS #14).
"""
import argparse, datetime, os, re, sys

ap = argparse.ArgumentParser()
ap.add_argument("--root", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
ap.add_argument("--today", default=datetime.date.today().isoformat())
a = ap.parse_args()
ROOT = a.root

def R(p):
    fp = os.path.join(ROOT, p)
    return open(fp, encoding="utf-8").read() if os.path.exists(fp) else None

REQ = ["STATUS.md", "workbook/PC_REDEMPTION_REGISTER.tsv", "workbook/PREDICTIONS.tsv",
       "workbook/VX.tsv", "workbook/KB.tsv", "docket/CATALYSTS.tsv"]
missing = [p for p in REQ if R(p) is None]
if missing:
    print(f"⛔ CANNOT RUN — missing: {', '.join(missing)} (root {ROOT})"); sys.exit(2)

findings = []
flag = lambda chk, msg: findings.append((chk, msg))
SEG = re.compile(r"(PRIOR CELL|PRIOR NOTE|Original row|Pre-grade record|Superseded text|Earlier stamp)[^\t|]*", re.I)
live_of = lambda line: SEG.sub("", line)

# ── CHECK 1a ── fired gates
reg = R("workbook/PC_REDEMPTION_REGISTER.tsv")
fired = sorted(set(re.findall(r"FIRE RECORD[^=]*=+\s*(GATE-[A-Z0-9-]+)", reg)) |
               set(re.findall(r"FIRE RECORD.{0,200}?(GATE-[A-Z0-9-]+)[^\n]{0,40}FIRED", reg)))
def surfaces():
    for ln, line in enumerate(R("STATUS.md").split("\n"), 1):
        yield "STATUS.md", ln, line
    for ln, line in enumerate(R("workbook/VX.tsv").split("\n"), 1):
        if line.startswith("VX-"): yield "workbook/VX.tsv", ln, line
    for ln, line in enumerate(R("docket/CATALYSTS.tsv").split("\n"), 1):
        d = line.split("\t")[0]
        if re.match(r"\d{4}-\d{2}-\d{2}$", d) and d >= a.today: yield "docket/CATALYSTS.tsv", ln, line
for gate in fired:
    short = gate.replace("GATE-", "")
    for f, ln, line in surfaces():
        live = live_of(line)
        if gate not in live and short not in live and not re.search(r"\bR2 \((a|b)\)", live): continue
        if re.search(r"\b0 (fired|FIRED)\b", live):
            flag("1a", f"{f}:{ln} names {gate} and asserts '0 fired' — the gate has a FIRE RECORD")
        elif "FIRED" not in live.upper():
            flag("1a", f"{f}:{ln} names {gate} with no FIRED marker — the gate has a FIRE RECORD")
if not fired:
    flag("1a", "no FIRE RECORD parsed from the register — if a gate has fired, the parser is stale (fail loud)") if "FIRE RECORD" in reg else None

# ── CHECK 1b ── resolved predictions shown as open
resolved = {}
for line in R("workbook/PREDICTIONS.tsv").split("\n")[1:]:
    c = line.split("\t")
    if len(c) > 5 and c[5].startswith("RESOLVED"): resolved[c[0]] = c[5]
OPEN_WORDS = re.compile(r"STAYS OPEN|NOT GRADED|\bis DUE\b|still OPEN|ungraded", re.I)
for ln, line in enumerate(R("STATUS.md").split("\n"), 1):
    for pid, st in resolved.items():
        live = live_of(line)
        if re.search(rf"\b{re.escape(pid)}\b", live) and OPEN_WORDS.search(live):
            flag("1b", f"STATUS.md:{ln} calls {pid} open/ungraded but PREDICTIONS.tsv says {st}")

# ── CHECK 2 ── asserted counts
st = R("STATUS.md")
rows = [l for l in st.split("\n") if l.startswith("| ") and re.search(r"\|\s*\**\s*(🔴🔴|🔴|🟠|🟡|⚪)\((\d)\)", l)]
scores = [int(re.search(r"\((\d)\)", l.split("|")[2]).group(1)) for l in rows if re.search(r"\((\d)\)", l.split("|")[2])]
m = re.search(r"Convergence:\s*\**(\d+)/(\d+)", st)
if not rows:
    flag("2", "convergence matrix not parsed (0 scored rows) — fail loud")
elif m:
    x, y = int(m.group(1)), int(m.group(2))
    if sum(scores) != x: flag("2", f"matrix scores sum {sum(scores)} ≠ asserted 'Convergence: {x}/{y}'")
    if 5 * len(rows) != y: flag("2", f"{len(rows)} vector rows ⇒ max {5*len(rows)} ≠ asserted denominator {y}")
else:
    flag("2", "no 'Convergence: X/Y' line found on STATUS.md")
nv = re.search(r"CONVERGENCE MATRIX \((\d+) vectors\)", st)
if nv and int(nv.group(1)) != len(rows):
    flag("2", f"header says {nv.group(1)} vectors, matrix has {len(rows)} rows")

# ── CHECK 3 ── field counts
for p in ("workbook/KB.tsv", "workbook/VX.tsv"):
    for ln, line in enumerate(R(p).split("\n"), 1):
        if not line or line.startswith("#") or line.startswith("ID\t"): continue
        n = line.count("\t") + 1
        if n != 13: flag("3", f"{p}:{ln} has {n} fields, schema is 13 ({line.split(chr(9))[0][:20]})")

print(f"BROCK selfcheck — gates with FIRE RECORD: {', '.join(fired) or 'none'} · resolved predictions: {len(resolved)} · matrix rows: {len(rows)}")
if findings:
    for chk, msg in findings: print(f"  ❌ [{chk}] {msg}")
    print(f"FINDINGS: {len(findings)}"); sys.exit(1)
print("CLEAN — covers only checks 1a/1b/2/3 as documented in this file's header; it is not a general staleness audit.")
sys.exit(0)
