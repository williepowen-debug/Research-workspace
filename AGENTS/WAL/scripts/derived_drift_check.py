#!/usr/bin/env python3
"""WAL derived-surface drift check — finds the surfaces by SCANNING, never by a list.

Born 2026-08-20 (WAL session #3), replacing an enumerated "fold list" that was
itself the defect: an enumeration is a hidden claim that the list is COMPLETE, so
it covers today's derived surfaces and misses the next one anyone creates
(`finding_enumerated_mechanism_test_hides_a_completeness_claim`). This walks the
tree instead, so a NEW derived surface is covered the day it is written.

The class it catches: THESIS.md OWNS the thesis version / EV / PT and the live
state of each vector. Other surfaces RESTATE them. A thesis bump touches the
owner and nothing else, so the derived layer keeps asserting the pre-bump world.
Measured at birth: the MI3 falsifier was described as "never-run" on THREE
derived surfaces 13 days after it ran and disconfirmed.

  CHECK 1  value drift  — every version/EV/PT token on any surface must be the
                          canonical one from THESIS.md's own header, or sit next
                          to a historical marker.
  CHECK 2  retired claims — every pattern in workbook/RETIRED_CLAIMS.tsv must be
                          absent from live surfaces, or marked historical.

PROXIMITY, NOT PRESENCE. A marker only excuses a hit within MARKER_WINDOW chars
of it. This is deliberate: the fleet's consumer_check.py was found the same day
to suppress on marker PRESENCE anywhere on the line, which silently dropped live
values sitting beside historical ones
(`finding_supersession_marker_suppresses_the_live_value_beside_it`).

MEASURED PRECISION, stated so nobody reads a nonzero count as failure. On the
swept tree of 2026-08-23 this settles at a BASELINE of 11 check-1 and 35
check-2 hits (CHECK 3 clean after the closeout sync), and nearly all of them are correct history whose marker sits
outside the proximity window (dated KB rows, superseded THESIS/SCENARIOS
sections). Unscoped it returned 54/32 — that is alert fatigue, and a check
nobody reads is worse than no check.

  ⇒ THE SIGNAL IS THE DELTA, NOT THE LEVEL. A jump above the baseline means
    something NEW rotted. Re-baseline in this docstring whenever you do a sweep.

Advisory. Read-only. Exit 0 always.
Usage:  python3 scripts/derived_drift_check.py [--quiet] [--root DIR]
"""
import re, os, csv, argparse, sys

MARKERS = ("superseded", "supersedes", "prior", "was ", "historical", "retired",
           "frozen", "stale", "do not cite", "audit trail", "preserved",
           "corrected", "struck", "closed", "fired", "resolved", "died", "ran")
MARKER_WINDOW = 220          # chars either side of the hit a marker may excuse from
SKIP_DIRS = {"inbox", "outbox", "_archive", "archive", "sources", ".git"}
# Version-pinned history and frozen calibration records are SUPPOSED to carry old values.
# Scanning them produces guaranteed false positives and trains the reader to ignore the check.
SKIP_FILES = {"CHANGELOG.md", "RETIRED_CLAIMS.tsv",
              "Q2_GRADING_FRAME_2026-07-21.md", "PREPRINT_RECON_2026-07-17.md", "EARNINGS_PREP.md"}
# MEMORY.md's job is to DESCRIBE dead claims, so every retired pattern matches it by design.
SKIP_FOR_RETIRED = {"MEMORY.md"}


def canonical(root):
    """The owner's own header is the single source. Fail LOUD if it moves."""
    p = os.path.join(root, "THESIS.md")
    head = open(p, encoding="utf-8").read(1200)
    ver = re.search(r"\*\*Version:\*\*\s*\*\*(v[\d.]+)\*\*", head)
    ev = re.search(r"EV \$([\d,.]+)", head)
    pt = re.search(r"PT \$([\d]+-[\d]+)", head)
    if not (ver and ev and pt):
        print("  ✗ derived_drift_check: THESIS.md header did not yield version/EV/PT.\n"
              "    The owner's header format changed — FIX ME rather than trusting a clean run.")
        return None
    return {"version": ver.group(1), "ev": ev.group(1), "pt": pt.group(1)}


def surfaces(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".")]
        for fn in filenames:
            if fn in SKIP_FILES or not fn.endswith((".md", ".tsv")):
                continue
            yield os.path.relpath(os.path.join(dirpath, fn), root)


def excused(text, start, end):
    """Is a historical marker close enough to govern THIS hit? Proximity, not presence."""
    lo = max(0, start - MARKER_WINDOW)
    return any(m in text[lo:end + MARKER_WINDOW].lower() for m in MARKERS)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.path.join(os.path.dirname(__file__), ".."))
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()
    root = os.path.abspath(a.root)

    canon = canonical(root)
    if canon is None:
        return 0

    drift, revived = [], []

    # ---- CHECK 1: version / EV / PT tokens inside a PRESENT-TENSE claim about canon.
    # Scoped deliberately. An unscoped sweep returned 54 hits on this tree, nearly all
    # legitimate history (superseded sections, version lineage prose, forward names like
    # v2.5) — that ships alert fatigue and the check gets ignored. So a token only counts
    # when the line ALSO asserts it is the current/canonical value.
    # (`finding_base_rate_the_threshold_before_building_it` — measured before shipping.)
    ASSERTS = re.compile(
        r"core thesis:|thesis:|thesis v2|routes to|canonical|current(?:ly)? |live canon|"
        r"\bnow\b|per `?THESIS", re.I)
    pats = {
        "version": re.compile(r"\bv2\.\d(?:\.\d)?\b"),
        "EV":      re.compile(r"EV \$?([\d]+\.[\d]{2})"),
        "PT":      re.compile(r"PT \$?([\d]{2}-[\d]{2})\b"),
    }
    for rel in surfaces(root):
        try:
            text = open(os.path.join(root, rel), encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        for kind, rx in pats.items():
            for m in rx.finditer(text):
                tok = m.group(1) if m.groups() else m.group(0)
                if tok.lstrip("$") == canon[kind.lower() if kind != "version" else "version"].lstrip("v$") \
                   or tok == canon.get(kind.lower(), None) or tok == canon["version"]:
                    continue
                if excused(text, m.start(), m.end()):
                    continue
                ls = text.rfind("\n", 0, m.start()) + 1
                le = text.find("\n", m.end())
                whole = text[ls:le if le != -1 else len(text)]
                if not ASSERTS.search(whole):
                    continue                      # historical prose, not a present-tense claim
                line = text[:m.start()].count("\n") + 1
                drift.append((rel, line, kind, tok, whole[:150]))

    # ---- CHECK 3: KB row count. Added 2026-08-20, HOURS after this script shipped, because
    # the closeout found INDEX/CLAUDE/KB_INDEX all carrying "177 rows" against an actual 180
    # and CHECK 1 could not see it — it only knew version/EV/PT. A drift check is only as wide
    # as its list of canonical values, which is the same completeness trap the fold-list had.
    kb = os.path.join(root, "workbook", "KB.tsv")
    if os.path.exists(kb):
        actual = sum(1 for l in open(kb, encoding="utf-8") if l.startswith("KB-WAL-"))
        rx_rows = re.compile(r"\*{0,2}(\d{2,4})[- ]row s?\b|\*{0,2}(\d{2,4}) rows\b", re.I)
        for rel in surfaces(root):
            if os.path.basename(rel) in SKIP_FOR_RETIRED:
                continue
            try:
                text = open(os.path.join(root, rel), encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            for m in rx_rows.finditer(text):
                n = m.group(1) or m.group(2)
                if int(n) == actual or int(n) < 50:      # <50 = group subtotals, not the KB total
                    continue
                if excused(text, m.start(), m.end()):
                    continue
                ls = text.rfind("\n", 0, m.start()) + 1
                le = text.find("\n", m.end())
                whole = text[ls:le if le != -1 else len(text)]
                if not re.search(r"kb|evidence|workbook", whole, re.I):
                    continue                              # some other N-row table
                line = text[:m.start()].count("\n") + 1
                drift.append((rel, line, "KBrows", n + f" (actual {actual})", whole[:150]))

    # ---- CHECK 2: claims this desk has already killed
    rc = os.path.join(root, "workbook", "RETIRED_CLAIMS.tsv")
    rows = []
    if os.path.exists(rc):
        raw = [l for l in open(rc, encoding="utf-8").read().split("\n") if l and not l.startswith("#")]
        rows = list(csv.DictReader(raw, delimiter="\t"))
    for rel in surfaces(root):
        if os.path.basename(rel) in SKIP_FOR_RETIRED:
            continue
        try:
            text = open(os.path.join(root, rel), encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        low = text.lower()
        for row in rows:
            pat = (row.get("pattern") or "").strip()
            if not pat:
                continue
            try:
                rx = re.compile(pat[1:-1], re.I) if pat.startswith("/") and pat.endswith("/") \
                     else re.compile(re.escape(pat), re.I)
            except re.error:
                continue
            for m in rx.finditer(low):
                if excused(text, m.start(), m.end()):
                    continue
                line = text[:m.start()].count("\n") + 1
                revived.append((rel, line, row.get("died_on", "?"), text[m.start():m.end()][:70],
                                (row.get("replacement") or "")[:80]))

    if a.quiet:
        BASE_DRIFT, BASE_REVIVED = 12, 54      # RE-BASELINED 2026-08-28 (session #5 sweep). Was 11,35 (8/23); 11,23 (8/20).
                                               # 8/28 deltas, each verified hit-by-hit BEFORE re-baselining:
                                               #   check-1 +1  = STATUS.md KB-count token, synced 180->183 this session; the residual
                                               #                 12 are historical version cites inside dated records (correct as history).
                                               #   check-2 +19 = the 3 NEW retired-claim patterns filed today (the 8/21 tape figures, the
                                               #                 overvaluation series, and the 'not the cohort' verdict). Each matches its OWN
                                               #                 death record and the audit-trail lines that preserve the superseded figure --
                                               #                 e.g. POSITIONS.md:28 and NEXUS_BRIEF.md:9 deliberately ENUMERATE the dead
                                               #                 tokens so nobody re-derives them. Those hits are the discipline working.
                                               # check-2 moved 23 -> 35 for TWO known reasons, neither of them new rot:
                                               #   +1  the 8/20 NEXUS_BRIEF re-pin landed AFTER the 8/20 baseline was written,
                                               #       so the tree the number described was already one edit old. (Read 24/23 for
                                               #       three days: a check permanently 1 above baseline trains its reader to ignore it.)
                                               #   +11 SEVEN new RETIRED_CLAIMS patterns added 8/23 (the 77.5P 'lapsed' grade,
                                               #       '3 legs', 'six consecutive down', the July '$83.11/+$5.11' buffer, 'PT $52-74',
                                               #       'v2.3 is CURRENT', and the three dead threshold distances). Each new pattern
                                               #       also matches the audit-trail lines that RECORD the death, whose marker sits
                                               #       outside MARKER_WINDOW. Verified hit-by-hit 8/23: every 8/23-dated hit is a
                                               #       line SAYING the claim is dead, not a surface still asserting it.
                                               # ⚠️ KILLING A CLAIM RAISES THIS BASELINE. That is the tool's own cost of the discipline
                                               #    it enforces, and it is why the docstring says re-baseline ON EACH SWEEP -- an
                                               #    un-re-baselined check reads RED forever and stops being read.
        if len(drift) > BASE_DRIFT or len(revived) > BASE_REVIVED:
            print(f"🔴 derived drift ABOVE BASELINE: {len(drift)}/{BASE_DRIFT} stale value token(s), "
                  f"{len(revived)}/{BASE_REVIVED} retired claim(s) — something NEW rotted; run without --quiet")
        else:
            print(f"✓ derived drift at/below baseline ({len(drift)}/{BASE_DRIFT} · {len(revived)}/{BASE_REVIVED}) "
                  f"— residual is known history; the SIGNAL IS THE DELTA")
        return 0

    print(f"DERIVED-SURFACE DRIFT CHECK — canonical: {canon['version']} · EV ${canon['ev']} · PT ${canon['pt']}")
    print(f"(surfaces discovered by scanning, not enumerated — {sum(1 for _ in surfaces(root))} files)")
    print("=" * 72)
    print(f"\nCHECK 1 — stale version/EV/PT tokens: {len(drift)}")
    for rel, ln, kind, tok, ctx in drift[:20]:
        print(f"  {rel}:{ln}  [{kind} {tok}]\n     …{ctx.strip()}…")
    if len(drift) > 20:
        print(f"  … +{len(drift)-20} more")
    print(f"\nCHECK 2 — retired claims found alive: {len(revived)}")
    for rel, ln, died, hit, repl in revived[:20]:
        print(f"  {rel}:{ln}  (died {died})  “{hit.strip()}”\n     → {repl}")
    if len(revived) > 20:
        print(f"  … +{len(revived)-20} more")
    if not drift and not revived:
        print("\n  ✓ clean — but note this certifies the SCAN, not the thesis.")
    else:
        print("\n  ⚠️  A hit is a prompt to LOOK. Some will be correct history whose marker")
        print("      sits outside the proximity window — widen the marker, do not delete the fact.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
