#!/usr/bin/env python3
"""
version_drift_check.py — MARCO boot guard for the "fix cleared the region, not the file"
defect class.

WHY THIS EXISTS (all four instances are from session 21, 2026-08-11/12, all MARCO's own):
  1. NEXUS_BRIEF's NEXT DECISION POINT described a test as forthcoming for 11 days after it
     ran and resolved NULL — the SAME defect had been corrected in the brief's VIEW section
     on 7/31. A section-scoped fix did not clear the file.
  2. An inbox `git mv` was committed by path-scoping the DESTINATION directory, which takes
     the ADD half of a rename and leaves the DELETE half staged. 8 packets briefly existed in
     BOTH inbox/ and inbox/processed/ on origin.
  3. NEXUS_BRIEF's As-of line carried duplicated session-20 residue THROUGH that same
     session's rewrite of that very line.
  4. (Not checkable — analytical.) The Channel-4 read shipped before asking whether sales-tax
     receipts test municipal credit. No script detects that; it is in MEMORY.md instead.

WHAT THIS CHECKS — three mechanical classes, each base-rate-measured before shipping
(2026-08-12 measurements in the header of each class below):

  V  canonical-version drift  — a line CLAIMING to state the canonical thesis version while
                                disagreeing with thesis/THESIS.md
  C  duplicated field-label   — the same **Label:** twice in one line = stamp residue
  B  incomplete rename        — staged deletions under AGENTS/MARCO/ with no matching add

WHAT THIS DELIBERATELY DOES *NOT* CHECK, and why (measured, not assumed — 2026-08-12):
  A  "forward-looking language + a date that has passed": 21 hits across 8 MARCO surfaces,
     and on inspection **21 of 21 were false positives** — historical narrative ("Ended Apr
     30", "SIGNED INTO LAW Jun 10") and correctly-dated records of past checks. Shipping it
     would be pure alert fatigue. NOT BUILT. "Don't build it" is a real answer.
  R  "an ID resolved in its canonical ledger but written as pending in prose": 2 hits, both
     false positives (an incidental mention, and the ledger's own row matching itself).
     No signal above noise at MARCO's current surface count. NOT BUILT.
  Re-measure both before anyone revives them; the measurement harness is this file's history.

FAILURE DIRECTION (CHECK_STANDARD §6): biased toward FLAGGING for class V (a missed
canonical-version drift is boot-read by every future session and silently misroutes them; a
false flag costs one glance). Biased toward SILENCE for classes C and B, which are near-zero
false-positive by construction and should stay that way.

KNOWN-FP REGISTER (CHECK_STANDARD §1): AGENTS/MARCO/scripts/version_drift_allowlist.tsv —
per-instance, dated, EXPIRING. No pattern suppression: expired rows re-flag themselves, so a
quiet run means genuinely quiet. A malformed register suppresses NOTHING and says so.

Usage:
  python3 AGENTS/MARCO/scripts/version_drift_check.py            # all classes (boot step)
  python3 AGENTS/MARCO/scripts/version_drift_check.py --quiet    # print only on flags
  python3 AGENTS/MARCO/scripts/version_drift_check.py --strict   # exit 1 on flags (gates/CI)
Exit: 0 = ran (advisory default, flags or not) · 1 = flags AND --strict · 2 = could not run.
ADVISORY BY DEFAULT — a flag is a prompt to LOOK, never a find-replace. Class V especially:
a correctly-dated history line ("thesis v2.7 retired the thermometer") is RIGHT and must not
be rewritten to silence the check.
"""
import argparse
import collections
import datetime
import pathlib
import re
import subprocess
import sys

MARCO = pathlib.Path(__file__).resolve().parents[1]
ROOT = MARCO.parents[1]
ALLOWLIST = MARCO / "scripts" / "version_drift_allowlist.tsv"

# Surfaces scanned for text classes. Named explicitly so the perimeter is legible and so
# adding a surface is a deliberate act (CHECK_STANDARD §2).
SURFACES = [
    "STATUS.md", "NEXUS_BRIEF.md", "SCRATCH.md", "MEMORY.md", "CLAUDE.md",
    "EXPECTED_SIGNALS.md", "MAINTENANCE.md", "FIGURES.md", "FINDINGS.md",
    "TRADE.md", "RESEARCH_STATUS.md", "docket/CALENDAR.md",
    "thesis/TIMELINE.md", "thesis/CHANGELOG.md",
]
NOT_CHECKED = ("thesis/THESIS.md (it is the source of truth) · workbook/*.tsv · "
               "inbox/ · outbox/ · domain/sources/ · research/ · baselines/ · sub_agents/")

# Class V: only a token that CLAIMS to describe the CANONICAL/current thesis. A bare
# historical reference ("thesis v2.7 retired the thermometer", "v2.4→v2.5") is legitimate
# and must NOT flag — that distinction is the whole check.
CANON_CLAIM = re.compile(
    r"(?:canonical[^.\n]{0,60}?\bv(\d+\.\d+)"
    r"|\bv(\d+\.\d+)[^.\n]{0,30}?\bcanonical"
    r"|THESIS\.md`?\s*[\(\|]?\s*\**v(\d+\.\d+)"
    r"|current thesis[^.\n]{0,30}?\bv(\d+\.\d+))", re.I)

# NB the `**Label: value**` form is deliberate and was NOT in v1 of this check. v1 required
# `**Label:**` (bold closing immediately after the colon) and therefore MISSED its own
# founding instance — the brief's duplicated `**Inbox: 0**` / `**Inbox: 0 — DRAINED 27→0**`
# residue. Caught 2026-08-12 by running the capable-case test CHECK_STANDARD §3 requires,
# before shipping. Match the label + colon; do not require the bold to close.
FIELD_LABEL = re.compile(r"\*\*\s*(As of|Status|Inbox|STATUS commit|Thesis version|"
                         r"Last Updated|Priority|Domain|Position)\s*:")


def canonical_version():
    """Read the canonical thesis version. Fail LOUD if it cannot be determined."""
    th = MARCO / "thesis" / "THESIS.md"
    if not th.exists():
        return None, "thesis/THESIS.md not found"
    head = th.read_text(errors="replace")[:4000]
    for pat in (r"\*\*Version:\*\*\s*v?(\d+\.\d+)",
                r"^\s*#.*?\bv(\d+\.\d+)",
                r"\bVersion:?\s*v(\d+\.\d+)"):
        m = re.search(pat, head, re.M | re.I)
        if m:
            return m.group(1), None
    return None, "no version token found in the first 4000 chars of thesis/THESIS.md"


def load_allowlist():
    """Per-instance, dated, expiring. A malformed register suppresses NOTHING (§1).

    Registered rows are keyed on (file, token, ANCHOR-substring) — NOT on a line number.
    v1 keyed on `path:line` and broke the same day it shipped: editing MEMORY.md shifted its
    lines, every registered row stopped matching, and correctly-registered historical
    references re-flagged as if new. A line number is not an identity. The anchor is a
    distinctive substring of the line, so a row survives edits ELSEWHERE in the file but
    stops matching if the flagged sentence itself is rewritten — which is the behaviour we
    want, since a rewritten sentence deserves a fresh look. Expiry still forces
    re-verification, so this is per-instance registration, not pattern suppression.
    """
    rows, problems = [], []
    if not ALLOWLIST.exists():
        return rows, problems
    today = datetime.date.today()
    for n, raw in enumerate(ALLOWLIST.read_text().splitlines(), 1):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        parts = [p.strip() for p in raw.split("\t")]
        if len(parts) < 6:
            problems.append(f"L{n}: needs 6 tab-separated fields "
                            f"(file, token, anchor, expiry, date_added, reason), "
                            f"got {len(parts)} — SUPPRESSES NOTHING")
            continue
        fil, token, anchor, expiry, added, reason = parts[:6]
        if fil.lower() == "file":
            continue
        if not anchor:
            problems.append(f"L{n}: empty anchor ({fil} · {token}) — SUPPRESSES NOTHING "
                            f"(an anchorless row would suppress a whole file+token class)")
            continue
        try:
            exp = datetime.date.fromisoformat(expiry)
        except ValueError:
            problems.append(f"L{n}: bad expiry {expiry!r} — SUPPRESSES NOTHING")
            continue
        if exp < today:
            problems.append(f"L{n}: EXPIRED {expiry} ({fil} · {token}) "
                            f"— re-flagging by design; re-verify or re-date")
            continue
        rows.append((fil, token, anchor, reason))
    return rows, problems


def registered(allow, rel, token, line):
    """True if this exact instance is registered and unexpired."""
    return any(f == rel and t == token and a in line for f, t, a, _ in allow)


def scan_text(canon, allow):
    v_hits, c_hits = [], []
    for rel in SURFACES:
        p = MARCO / rel
        if not p.exists():
            continue
        for n, line in enumerate(p.read_text(errors="replace").split("\n"), 1):
            for m in CANON_CLAIM.finditer(line):
                got = next((g for g in m.groups() if g), None)
                if got and got != canon and not registered(allow, rel, f"v{got}", line):
                    v_hits.append((rel, n, got, line.strip()))
            labels = [m.group(1) for m in FIELD_LABEL.finditer(line)]
            dup = [k for k, v in collections.Counter(labels).items() if v > 1]
            if dup:
                token = "dup:" + ",".join(sorted(dup))
                if not registered(allow, rel, token, line):
                    c_hits.append((rel, n, dup, line.strip()))
    return v_hits, c_hits


def scan_index():
    """Class B: staged deletions under AGENTS/MARCO/ with no matching staged add.

    Catches the `git mv`-then-path-scope-the-destination defect, which half-publishes a
    rename. Near-zero false positive: a deliberate deletion is normally committed with its
    own message, and this is advisory.
    """
    try:
        out = subprocess.run(["git", "status", "--porcelain", "--", "AGENTS/MARCO/"],
                             cwd=str(ROOT), capture_output=True, text=True, timeout=30)
    except Exception as e:
        return [], f"git unavailable: {e}"
    if out.returncode != 0:
        return [], f"git status rc={out.returncode}"
    staged_del, staged_add = [], set()
    for line in out.stdout.splitlines():
        if len(line) < 4:
            continue
        x, path = line[0], line[3:].strip()
        if x == "D":
            staged_del.append(path)
        elif x in "AM":
            staged_add.add(pathlib.Path(path).name)
    orphan = [d for d in staged_del if pathlib.Path(d).name not in staged_add]
    return orphan, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quiet", action="store_true", help="print only when something flags")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 when flags are found (for gates/CI). Default is ADVISORY: "
                         "exit 0 whenever the check RAN, so a boot flag reads as a finding "
                         "to look at, not as a broken step. Boot prints the full output "
                         "either way — the signal is the text, not the status colour. "
                         "(Fleet convention: orphan_check/claim_check are advisory too. "
                         "The inverse error — a step showing ❌ FAIL for an advisory flag — "
                         "trains readers to ignore FAIL, which is how boot.py came to print "
                         "'✓ ran cleanly' beside a real failure for 101 days.)")
    args = ap.parse_args()

    canon, err = canonical_version()
    allow, allow_problems = load_allowlist()

    if err:
        print(f"🔴 version_drift_check CANNOT RUN class V: {err}")
        print("   Owner: MARCO. Next move: restore a `**Version:** vX.Y` line at the top of "
              "thesis/THESIS.md, then re-run. Classes C and B still ran below.")
        canon = None

    v_hits, c_hits = ([], []) if canon is None else scan_text(canon, allow)
    orphan_del, git_err = scan_index()

    flagged = bool(v_hits or c_hits or orphan_del or allow_problems)
    if args.quiet and not flagged and not err:
        return 0

    print("=" * 72)
    print(f"  MARCO Version / Residue Drift Check — {datetime.date.today()}")
    print("=" * 72)
    print(f"  canonical thesis version: v{canon}" if canon else "  canonical version: UNKNOWN")
    print(f"  CHECKED: {len(SURFACES)} surfaces (class V, C) + the git index (class B)")
    print(f"  NOT checked: {NOT_CHECKED}")
    print(f"  NOT built (measured 8/12, no signal): forward-language-vs-passed-date "
          f"(21/21 false positives) · resolved-ID-written-as-pending (2/2 false positives)")
    if git_err:
        print(f"  ⚠️ class B degraded: {git_err}")

    if allow_problems:
        print(f"\n  ⚠️ ALLOWLIST ({ALLOWLIST.name}) — {len(allow_problems)} issue(s):")
        for p in allow_problems:
            print(f"      {p}")

    if v_hits:
        print(f"\n  🔴 CLASS V — canonical thesis version asserted WRONG ({len(v_hits)}):")
        for rel, n, got, line in v_hits:
            print(f"      {rel}:{n}  says v{got}, canonical is v{canon}")
            print(f"         {line[:100]}")
        print("      Owner: MARCO. Next move: correct the line, or register it in "
              f"{ALLOWLIST.name} with an expiry if it is a legitimate HISTORICAL reference.")
        print("      ⚠️ A flag is a prompt to LOOK. Never find-replace a version token — a "
              "correctly-dated history line ('v2.7 retired the thermometer') is RIGHT.")

    if c_hits:
        print(f"\n  🟠 CLASS C — duplicated field-label in one line (stamp residue) ({len(c_hits)}):")
        for rel, n, dup, line in c_hits:
            print(f"      {rel}:{n}  '{', '.join(dup)}' appears twice")
            print(f"         {line[:100]}")
        print("      Owner: MARCO. Next move: the SECOND occurrence is usually the stale one "
              "— read both before deleting either.")

    if orphan_del:
        print(f"\n  🔴 CLASS B — staged deletion with no matching add ({len(orphan_del)}):")
        for d in orphan_del[:10]:
            print(f"      {d}")
        if len(orphan_del) > 10:
            print(f"      (+{len(orphan_del) - 10} more)")
        print("      Owner: MARCO. Next move: if this came from `git mv`, you path-scoped the "
              "DESTINATION. Commit the PARENT of both halves "
              "(e.g. `git commit AGENTS/MARCO/inbox/`), not `inbox/processed/`.")

    if not flagged:
        print("\n  ✓ clean — no canonical-version drift, no duplicated stamps, "
              "no half-staged renames.")
    print()
    if err:                       # could not run a class at all — a genuine failure
        return 2
    return 1 if (flagged and args.strict) else 0


if __name__ == "__main__":
    sys.exit(main())
