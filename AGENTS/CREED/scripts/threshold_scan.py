#!/usr/bin/env python3
"""
CREED BOOT-TIME THRESHOLD SCAN
==============================
Reads every CREED-T row in registry/THRESHOLDS.tsv, resolves its source_of_truth
vectors in workbook/VX.tsv, and compares the CURRENT VALUE against the FROZEN BAND
-- at boot, before the session does any work.

WHY THIS EXISTS
---------------
This is CREED-T-02's root cause. On 2026-08-13, mid-cycle, CREED wrote "66% of $6.0B"
into its own workbook -- the T-02 metric, against a frozen band of 50 -- and did not
grade it. The trigger had been fireable since the June print and was not noticed for
~6 weeks. No boot step read the registry, so nothing compared a value to its band
until a human happened to look.

The FORUM-5 K5 test falsified the obvious hypothesis: dark-cadence was NOT the defect.
CREED was awake, holding the number, with the band written down. Nothing connected them.

WHAT IT REFUSES TO DO
---------------------
*** IT NEVER PRINTS "ALL CLEAR". ***
Most registry rows do NOT carry both a numeric band and a metric vector, so a numeric
pass covers a minority of the registry and says NOTHING about the rest. The summary is
built so that a clean numeric pass cannot be misread as a clean registry. Every
unscannable row is ENUMERATED BY NAME and BY REASON on every run -- silence about them
is the failure mode, not brevity.
(No count is written in this docstring ON PURPOSE. The counts move whenever a vector or
a trigger is added, and a hardcoded one rots into a false claim -- the defect class this
desk keeps finding in others, and found in its own README on 2026-08-27, where a stale
"14 comment lines" sat inside the warning against hardcoding. The scan COMPUTES its
counts and prints them; derive them from a run, never quote them from here.)

*** IT NEVER SUPPRESSES A COMPARISON. ***
Rows whose comparison is not currently VALID (basis defect, undeclared basis) are
labelled BLOCKED -- but their raw arithmetic is still printed. A block downgrades a
verdict; it never hides a number. A hardcoded block that silently swallowed a real
crossing would reproduce the exact class this script exists to catch.

*** IT IS NOT AN ADJUDICATOR. ***
A TRIPPED line is an instruction to GO GRADE THE TRIGGER at primary, not a fire.
Adjudication is a CREED act performed against primary sources and recorded in
registry/CREED_T_FIRED_LOG.tsv. This script reads state; it never writes any.

Exit: 0 = nothing needs attention · 1 = something does (TRIPPED / NEAR / broken pointer).
Both exits still print the full unscannable register.
"""

import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
THRESHOLDS = os.path.join(REPO, "AGENTS/CREED/registry/THRESHOLDS.tsv")
VX = os.path.join(REPO, "AGENTS/CREED/workbook/VX.tsv")
FIRED = os.path.join(REPO, "AGENTS/CREED/registry/CREED_T_FIRED_LOG.tsv")

# Distance from band, as a fraction of |band|, at which a row is called NEAR.
NEAR_FRAC = 0.05

# ---------------------------------------------------------------------------
# BASIS BLOCKS -- rows whose numeric comparison is NOT currently a valid verdict.
#
# ⚠️ EVERY ENTRY HERE IS A LIVE DEFECT WITH AN OPEN RULING, NOT A PERMANENT EXEMPTION.
#    Each MUST be deleted the moment Will rules the underlying item -- a stale entry
#    silently downgrades a real crossing, which is this script's own worst failure mode.
#    That is why each carries the obligation that clears it: grep the reason, not the id.
#
#    Blocked rows STILL PRINT their arithmetic. BLOCKED means "this comparison is not a
#    verdict", never "do not look".
# ---------------------------------------------------------------------------
BASIS_BLOCKS = {
    "CREED-T-03": (
        "BAND AND VALUE ARE ON DIFFERENT BASES -- the comparison is arithmetic, not a verdict. "
        "The >3.40 band cannot be reproduced from the FDIC Q1 2026 QBP it cites (that cell reads "
        "2.73%); the value now carried is the QBP COMBINED cell. Comparing them measures a "
        "PERIMETER GAP, not stress. KB-CREED-024, AWAITING WILL. "
        "CLEARS WHEN: Will re-points the source or re-bases the band (never band-to-fit-value)."
    ),
    "CREED-T-08a": (
        "BASIS UNDECLARED IN THE BAND -- '< -10' does not say total-return or price-only, and "
        "VX-7.01 currently carries BOTH (+0.07pp TR / -0.58pp price-only, 0.65pp apart = ~6.5% "
        "of the 10pp band). An undeclared basis POSITIONS the trigger, so no single number can "
        "grade it. PROPOSED, AWAITING WILL. "
        "CLEARS WHEN: Will declares which basis is canonical."
    ),
}


def rows(path, prefix):
    """Rows matching a prefix. Never tail -n +2: the comment block above the header
    grows whenever an obligation is logged, so any hardcoded offset is a future defect."""
    out = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith(prefix):
                out.append(line.rstrip("\n").split("\t"))
    return out


def first_number(text):
    """First signed decimal in a prose cell. Returns None when there is nothing to parse."""
    m = re.search(r"[-+]?\d+(?:\.\d+)?", text.replace(",", ""))
    return float(m.group()) if m else None


def parse_context(text, width=34):
    """The parsed number shown in its surrounding text, so a reader can eyeball whether
    first_number() grabbed the RIGHT number. These cells are prose: re-wording one can
    silently change what gets parsed, and a wrong-but-plausible parse is exactly the
    'real number carrying the wrong basis' failure this desk calls its dominant one.
    Print the provenance; never ask anyone to trust the extraction."""
    m = re.search(r"[-+]?\d+(?:\.\d+)?", text.replace(",", ""))
    if not m:
        return ""
    s = text.replace(",", "")
    lo, hi = max(0, m.start() - 4), min(len(s), m.end() + width)
    return ("…" if lo else "") + s[lo:hi].replace("\t", " ") + ("…" if hi < len(s) else "")


def all_numbers(text):
    return [float(x) for x in re.findall(r"[-+]?\d+(?:\.\d+)?", text.replace(",", ""))]


# Strict: exactly one dot, digits both sides. A looser [\d.]+ swallows the range
# shorthand "VX-CREED-10.01..10.05" whole and invents a vector that cannot exist —
# which this script's OWN FIRST RUN did, reporting a phantom pointer defect against
# CREED-T-08b whose five vectors are all present and fine.
# [[finding_test_the_guard_not_just_the_guarded]] — a guard's v1 fails on first RUN,
# and it failed here in the guard's single most load-bearing direction: FABRICATING a
# defect in the very check built to find real ones. Caught before commit by running it.
VEC_RE = re.compile(r"VX-CREED-\d+\.\d+")
RANGE_RE = re.compile(r"VX-CREED-(\d+)\.(\d+)\s*\.\.\s*(?:VX-CREED-)?(\d+)\.(\d+)")


def vectors_named(src):
    """Every vector a source_of_truth cell names, expanding '10.01..10.05' range shorthand.
    Returns (ids, note) — note is non-empty when shorthand was expanded, because a reader
    should see that the scan interpreted the cell rather than read it literally."""
    ids, note = [], ""
    for maj1, min1, maj2, min2 in RANGE_RE.findall(src):
        if maj1 == maj2 and int(min1) <= int(min2):
            span = [f"VX-CREED-{maj1}.{str(i).zfill(len(min1))}"
                    for i in range(int(min1), int(min2) + 1)]
            ids.extend(span)
            note = f"expanded range shorthand → {len(span)} vectors"
    src_wo_ranges = RANGE_RE.sub(" ", src)
    ids.extend(VEC_RE.findall(src_wo_ranges))
    seen, out = set(), []
    for v in ids:
        if v not in seen:
            seen.add(v)
            out.append(v)
    return out, note


def load_vectors():
    out = {}
    for r in rows(VX, "VX-CREED-"):
        if len(r) >= 10:
            out[r[0]] = {"value": r[3], "state": r[7], "updated": r[9]}
    return out


def load_fired():
    return {r[0]: r[1] for r in rows(FIRED, "CREED-T") if len(r) >= 2}


def trips(op, value, band):
    if op == ">":
        return value > band
    if op == ">=":
        return value >= band
    if op == "<":
        return value < band
    if op == "<=":
        return value <= band
    return None


def main():
    for p in (THRESHOLDS, VX, FIRED):
        if not os.path.exists(p):
            print(f"THRESHOLD SCAN: FAIL-LOUD — missing {p}", file=sys.stderr)
            return 2

    registry = rows(THRESHOLDS, "CREED-T")
    vectors = load_vectors()
    fired = load_fired()

    scannable, blocked, unscannable, pointer_defects, expansions = [], [], [], [], []

    for r in registry:
        tid, op, raw_band, src = r[0], r[3], r[4], (r[8] if len(r) > 8 else "")
        band = first_number(raw_band) if op in (">", ">=", "<", "<=") else None
        vecs, range_note = vectors_named(src)
        if range_note:
            expansions.append((tid, range_note))

        # Follow the pointer and read what is at the other end. n=3 registry-pointer
        # defects in 8 days (T-08a wrong vector, T-01b DQ-on-an-SS-bar, T-03 baseline
        # not in its cited source) -- all three had rows that EXISTED and READ FINE.
        for v in vecs:
            if v not in vectors:
                pointer_defects.append((tid, v, "named vector does NOT exist in VX.tsv"))

        if band is None:
            unscannable.append((tid, f"no numeric band (op={op!r}, band={raw_band[:60]!r})"))
            continue
        if not vecs:
            # A numeric band with no metric vector is UNTRIPPABLE BY CONSTRUCTION.
            # This is the exact shape of K5: T-02 was the only banded trigger with no
            # vector, and it went ungraded for 6 weeks. Reported as a DEFECT, not a skip.
            unscannable.append((tid, f"⚠️ NUMERIC BAND ({op} {band}) BUT NO METRIC VECTOR — "
                                     "UNTRIPPABLE BY CONSTRUCTION (the K5 shape)"))
            continue

        live = [v for v in vecs if v in vectors]
        if not live:
            unscannable.append((tid, "every named vector is unresolvable — see pointer defects"))
            continue

        vid = live[0]
        cur = first_number(vectors[vid]["value"])
        if cur is None:
            unscannable.append((tid, f"{vid} carries no parseable number"))
            continue

        rec = {"tid": tid, "op": op, "band": band, "vid": vid, "cur": cur,
               "updated": vectors[vid]["updated"],
               "ctx": parse_context(vectors[vid]["value"]),
               "nvals": len(all_numbers(vectors[vid]["value"])),
               "trip": trips(op, cur, band),
               "dist": abs(cur - band),
               "frac": abs(cur - band) / abs(band) if band else None}
        (blocked if tid in BASIS_BLOCKS else scannable).append(rec)

    # ---------------- output ----------------
    print("CREED BOOT THRESHOLD SCAN — current values vs FROZEN bands")
    print(f"  registry: {len(registry)} CREED-T rows · "
          f"{len(scannable)} comparable · {len(blocked)} basis-BLOCKED · "
          f"{len(unscannable)} not scannable")
    print()

    attention = False

    print("  ── COMPARABLE ──")
    for rec in sorted(scannable, key=lambda x: (x["frac"] is None, x["frac"])):
        tid, arrow = rec["tid"], f"{rec['cur']} {rec['op']} {rec['band']}"
        if rec["trip"] and tid in fired:
            print(f"  🔴 FIRED    {tid:12} {arrow}  — exceeds, and FIRED {fired[tid]}. "
                  f"State confirmed, not a new alarm. [{rec['vid']}, {rec['updated']}]")
        elif rec["trip"]:
            attention = True
            print(f"  🔴🔴 TRIPPED {tid:12} {arrow}  — EXCEEDS ITS BAND AND IS NOT IN THE FIRE "
                  f"LEDGER. [{rec['vid']}, {rec['updated']}]")
            print(f"       ⇒ GO GRADE IT AT PRIMARY NOW. This is the K5 state: the number and "
                  f"the band are both on file and nothing has connected them.")
        elif tid in fired:
            attention = True
            print(f"  ⚠️  WAS-FIRED {tid:12} {arrow}  — logged FIRED {fired[tid]} but the current "
                  f"value NO LONGER exceeds. [{rec['vid']}, {rec['updated']}]")
            print(f"       ⇒ A fire is not un-fired by a later print. Reconcile deliberately; "
                  f"never silently clear the ledger.")
        elif rec["frac"] is not None and rec["frac"] <= NEAR_FRAC:
            attention = True
            print(f"  🟠 NEAR     {tid:12} {arrow}  — {rec['dist']:.4g} away "
                  f"({rec['frac']*100:.2f}% of band). [{rec['vid']}, {rec['updated']}]")
        else:
            print(f"  ✅ CLEAR    {tid:12} {arrow}  — {rec['dist']:.4g} away "
                  f"({rec['frac']*100:.1f}% of band). [{rec['vid']}, {rec['updated']}]")
    print("     parsed-from (eyeball these — the cells are prose, not fields):")
    for rec in sorted(scannable, key=lambda x: x["tid"]):
        print(f"       {rec['tid']:12} {rec['cur']:>8}  ←  {rec['ctx']}")

    if blocked:
        print()
        print("  ── BASIS-BLOCKED — arithmetic shown, VERDICT WITHHELD ──")
        for rec in blocked:
            verdict = "would exceed" if rec["trip"] else "would not exceed"
            print(f"  ⛔ BLOCKED  {rec['tid']:12} {rec['cur']} {rec['op']} {rec['band']} "
                  f"({verdict}) [{rec['vid']}, {rec['updated']}]")
            print(f"       parsed-from: {rec['ctx']}"
                  f"   ⚠️ cell holds {rec['nvals']} numbers — extraction is fragile")
            print(f"       {BASIS_BLOCKS[rec['tid']]}")
        print("  ⚠️  A BLOCKED row is NOT a clear row. It cannot be graded on the registered")
        print("      basis at all — which is a worse state than being close to its band.")

    print()
    print("  ── NOT SCANNABLE — enumerated every run, by name and reason ──")
    for tid, why in unscannable:
        print(f"  ·  {tid:12} {why}")
        if "UNTRIPPABLE" in why:
            attention = True

    if expansions:
        print()
        print("  ── shorthand the scan INTERPRETED (not read literally) ──")
        for tid, note in expansions:
            print(f"  ·  {tid:12} {note}")

    if pointer_defects:
        attention = True
        print()
        print("  ── 🔴 REGISTRY POINTER DEFECTS ──")
        for tid, v, why in pointer_defects:
            print(f"  🔴 {tid:12} → {v}: {why}")

    print()
    print("  " + "=" * 74)
    n_ok = len(scannable)
    print(f"  A numeric pass covers {n_ok} of {len(registry)} rows. IT SAYS NOTHING ABOUT THE "
          f"OTHER {len(registry) - n_ok}.")
    print("  This scan CANNOT tell you: whether a band is still the right band; whether a")
    print("  vector's value is fresh or true; whether a qualitative trigger has fired. Those")
    print("  need a session to look. A green here certifies arithmetic on resolvable rows only.")
    print("  " + "=" * 74)

    return 1 if attention else 0


if __name__ == "__main__":
    sys.exit(main())
