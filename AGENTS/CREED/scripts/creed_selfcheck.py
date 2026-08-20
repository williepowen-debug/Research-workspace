#!/usr/bin/env python3
"""
CREED self-check — three NARROW closeout checks. CREED-scoped only; reads nothing outside AGENTS/CREED/.

WHY THIS EXISTS (2026-08-20). A Will-directed staleness sweep found 14 defects that no existing
tool could see. `consumer_check.py` scans superseded VALUES; the two worst findings were a superseded
STATE (a fired trigger invisible on the registry that declares it) and superseded COUNTS. Those are
different objects, so a clean consumer_check meant nothing.

DELIBERATELY NOT A GENERAL "CLAIM DETECTOR." claim_check.py's own scoping lesson: 13 decision files
-> 1 flag; the whole tree -> 131 flags of alert fatigue. Both checks below are file-level and
enumerable, so a flag is always actionable and the false-positive rate is ~0 by construction.

RUN AT CLOSEOUT, NOT BOOT. CREED is Tier-2 spawn-on-need and process weight is precisely what makes
a spawn-on-need agent expensive to wake. Target runtime: well under a second.

  python3 AGENTS/CREED/scripts/creed_selfcheck.py

exit 0 = clean · exit 1 = findings. Safe to gate a closeout on: every surface it reads is CREED-owned,
so it can never block on another agent's work (the bare-`--strict` trap from root CLAUDE.md carve-out 3).
"""
import os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
R = lambda p: open(os.path.join(ROOT, p), encoding="utf-8").read() if os.path.exists(os.path.join(ROOT, p)) else None

FIRE_MARK = re.compile(r"\bFIRED\b")
findings = []
def flag(sev, check, msg):
    findings.append((sev, check, msg))

# ══════════════ CHECK 1 — fired-trigger cross-surface consistency ══════════════
# A trigger's fire state lives on several surfaces at once. On 2026-08-20 CREED-T-02 fired and
# THRESHOLDS.tsv -- the registry that DECLARES the trigger -- said nothing. Same one-condition-many-
# surfaces defect as the K5 finding, in the file that produced K5.
CORE    = ["registry/THRESHOLDS.tsv", "STATUS.md", "thesis/THESIS.md"]   # must show the fire, always
CONTEXT = ["workbook/VX.tsv", "workbook/FLOW.tsv", "COVERAGE.md"]        # must show it IF they name the trigger

log = R("registry/CREED_T_FIRED_LOG.tsv")
if log is None:
    flag("INFO", "fired-consistency", "no registry/CREED_T_FIRED_LOG.tsv — no fires to reconcile")
else:
    fired = []
    for line in log.splitlines():
        if line.startswith("#") or line.startswith("trigger_id") or not line.strip():
            continue
        f = line.split("\t")
        if len(f) > 7 and FIRE_MARK.search(f[7]):
            fired.append((f[0], f[1], f[2]))
    if not fired:
        print("  check 1: fire ledger present, no FIRED rows — nothing to reconcile")
    for tid, fired_date, eff in fired:
        for surf in CORE + CONTEXT:
            body = R(surf)
            if body is None:
                flag("RED", "fired-consistency", f"{tid}: surface MISSING — {surf}")
                continue
            names = tid in body
            if surf in CONTEXT and not names:
                continue                      # context surface may legitimately not discuss it
            if not names:
                flag("RED", "fired-consistency",
                     f"{tid} FIRED {fired_date} but {surf} never names it (CORE surface)")
            elif not FIRE_MARK.search(body):
                flag("RED", "fired-consistency",
                     f"{tid} FIRED {fired_date} (effective {eff}) but {surf} names the trigger "
                     f"with NO fire marker — a reader of that file alone cannot tell it fired")

# ══════════════ CHECK 2 — asserted counts vs actual ══════════════
# README.md and CLAUDE.md assert counts in prose. They drifted to VX 31->32, KB 17->19,
# PRED "10 open"->9, workbook "Six files"->8, and README and CLAUDE.md disagreed with EACH OTHER.
def count_rows(path, prefix):
    b = R(path)
    return None if b is None else sum(1 for l in b.splitlines() if l.startswith(prefix))

actual = {
    "vx":       count_rows("workbook/VX.tsv", "VX-CREED-"),
    "kb":       count_rows("workbook/KB.tsv", "KB-CREED-"),
    "pred":     count_rows("workbook/PREDICTIONS.tsv", "PRED-CREED-"),
    "wbfiles":  len(os.listdir(os.path.join(ROOT, "workbook"))) if os.path.isdir(os.path.join(ROOT, "workbook")) else None,
}
WORDNUM = {"six":6,"seven":7,"eight":8,"nine":9,"ten":10,"eleven":11,"twelve":12}

# (surface, regex, key, human label). Regexes target the KNOWN phrasings only -- a NEW phrasing is
# not caught, and that scope limit is stated rather than implied.
ASSERTIONS = [
    ("README.md",  r"\*\*(\d+)-vector dashboard\*\*",              "vx",      "VX vector count"),
    ("README.md",  r"\*\*(\d+)\*\* Admiralty-scored",              "kb",      "KB row count"),
    ("COVERAGE.md",r"the (\d+)-vector workbook",                   "vx",      "VX vector count"),
    ("CLAUDE.md",  r"the live metric layer\W+(\d+) vectors",       "vx",      "VX vector count"),
    ("CLAUDE.md",  r"\b([Ss]ix|[Ss]even|[Ee]ight|[Nn]ine)\s+files:", "wbfiles","workbook file count"),
]
for surf, pat, key, label in ASSERTIONS:
    body = R(surf)
    if body is None or actual.get(key) is None:
        continue
    for m in re.finditer(pat, body):
        raw = m.group(1)
        claimed = WORDNUM.get(raw.lower(), None)
        if claimed is None:
            try: claimed = int(raw)
            except ValueError: continue
        if claimed != actual[key]:
            flag("RED", "asserted-count",
                 f"{surf}: claims {label} = {raw!r}, actual = {actual[key]}")

# PREDICTIONS is special: prose says "N open", and OPEN != total rows.
predb = R("workbook/PREDICTIONS.tsv")
if predb:
    open_n = sum(1 for l in predb.splitlines()
                 if l.startswith("PRED-CREED-") and re.search(r"\tOPEN\t", l))
    for surf in ("README.md",):
        body = R(surf)
        if not body: continue
        for m in re.finditer(r"\*\*(\d+)\*\* open forecasts", body):
            if int(m.group(1)) != open_n:
                flag("RED", "asserted-count",
                     f"{surf}: claims {m.group(1)} open predictions, actual OPEN = {open_n}")
    sb = R("workbook/PREDICTIONS_SCOREBOARD.md")
    if sb:
        resolved = sum(1 for l in predb.splitlines()
                       if l.startswith("PRED-CREED-") and re.search(r"\tRESOLVED", l))
        if resolved > 0 and re.search(r"\*\*n\s*=\s*0\*\*", sb):
            flag("RED", "asserted-count",
                 f"PREDICTIONS_SCOREBOARD.md still asserts n=0 while {resolved} prediction(s) are RESOLVED")

# ══════════════ CHECK 3 — outstanding known-stale banners ══════════════
# Added minutes after check 1 shipped, on a live observation: a "KNOWN-STALE, rebuild pending" banner
# added to COVERAGE.md contained the word FIRED, which made check 1 go GREEN on a file whose 12 lanes
# were still pre-fire. The check behaved exactly per its documented file-level scope -- and that is the
# problem: a BANNER SHOULD NOT BE ABLE TO SILENCE THE GUARD.
# This turns each banner into tracked debt. `finding_banner_is_a_warning_not_a_fix` says pair every
# banner with a dated rewrite trigger; this IS that pairing, mechanised. It clears when the banner goes.
BANNER = re.compile(r"KNOWN-STALE|rebuild pending|do NOT cite as current|DO NOT CITE AS CURRENT")
BANNER_SCAN = ["COVERAGE.md", "README.md", "STATUS.md", "thesis/THESIS.md",
               "registry/THRESHOLDS.tsv", "workbook/VX.tsv", "workbook/FLOW.tsv"]
for surf in BANNER_SCAN:
    body = R(surf)
    if body is None:
        continue
    seen_lines = {}                       # dedupe: one banner LINE = one finding, not one per pattern
    for m in BANNER.finditer(body):
        line = body[:m.start()].count("\n") + 1
        seen_lines.setdefault(line, set()).add(m.group(0))
    for line in sorted(seen_lines):
        marks = ", ".join(sorted(seen_lines[line]))
        flag("AMBER", "open-staleness-banner",
             f"{surf}:{line} carries a known-stale banner ({marks}) — outstanding debt, "
             f"not a fix. Clears when the banner is REMOVED, not when it is written.")

# ══════════════ report ══════════════
print("CREED SELF-CHECK — fired-trigger consistency + asserted counts")
print(f"  actual: VX={actual['vx']} · KB={actual['kb']} · PRED={actual['pred']} "
      f"(open={open_n if predb else '?'}) · workbook files={actual['wbfiles']}")
if not findings:
    print("\n  ✓ CLEAN — no fire-state or count inconsistencies.")
    print("  Scope: file-level fire markers on 6 surfaces + known count phrasings + open staleness")
    print("  phrasing for a count is NOT covered; add it to ASSERTIONS when you introduce one.")
    sys.exit(0)
for sev, check, msg in findings:
    icon = "\U0001f534" if sev == "RED" else ("\U0001f7e0" if sev == "AMBER" else "\u2139\ufe0f")
    print(f"\n  {icon} [{check}] {msg}")
print(f"\n  {len(findings)} finding(s). Fix by PATTERN, not by this list.")
sys.exit(1)
