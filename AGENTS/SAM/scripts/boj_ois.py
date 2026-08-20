#!/usr/bin/env python3
"""
SAM BOJ OIS Monitor — market-implied hike probability per MPM.

WHY THIS EXISTS (2026-08-04). SAM sourced this number by ad-hoc web search. On 8/4 that
failed twice in one session: (a) two of three searches returned 2025-VINTAGE BOJ content
reading as current — including a "42% October" that conflicted with SAM's own verified
~64%; (b) after failing to source it, SAM asserted a DIRECTION anyway ("BOJ-hawkish route
= up-risk") and had the sign backwards. Route 1 is BOJ hawkish-OF-PRICED: it pays on
SURPRISE, so a RISE in priced probability SHRINKS the edge. Sourcing the number turns
that from an assertion into arithmetic.

SOURCE
  https://centralbank.watch/bank-of-japan/  — server-rendered HTML, no JS, no JSON API.
  Underlying instrument: 3-month TONA (Tokyo Overnight Average Rate) futures.
  Page layout parsed:  <meeting date> | Cut <x>% | Hold <y>% | Hike <z>%

⚠️ BASIS — THE THING THAT BIT SAM ON 8/4, so the script ASSERTS it rather than assuming.
  The page states its probabilities are CUMULATIVE relative to today:
    "a given meeting's hike probability is the chance the rate is higher than today's
     level by that meeting date, and it already includes any move priced in for
     earlier ones."
  If that statement disappears or changes, the basis may have changed silently and every
  delta computed against stored history becomes meaningless. The script therefore
  VERIFIES the basis sentence on every run and refuses to write rows if it cannot.
  (Class: a number without its basis is not a number. See also KB-183 / the FXY RR proxy,
  where "computable" was wrongly treated as "trustworthy".)

WHAT IT DERIVES (the cumulative figure alone is not what the thesis needs)
  marginal(k)   = cum(k) - cum(k-1)        per-meeting hike probability
  unpriced(k)   = 100 - cum(k)             SURPRISE ROOM at meeting k
  The convexity route's edge lives in unpriced(), not in cum(). THESIS/STATUS/STRATEGY/
  TRADE all cite "Sep 17-18 ~60% unpriced" — this script is what keeps that honest.

TWO-CLOCK DISCIPLINE (PAT-044)
  The source's own "Data as of" date is stored SEPARATELY from the pull timestamp, and
  staleness is derived from CONTENT VINTAGE, never mtime (git sync restamps mtime, so an
  mtime-keyed freshness check fails FALSE-NEGATIVE — finding_mtime_is_corrupted_by_git_sync).
  If the source's as-of date has NOT advanced, the script reports "no new data" and writes
  NOTHING. A stale source must never manufacture a fresh-looking row
  (finding_partitioned_source_returns_stale_window_at_200).

ALERTS ARE NOT INVENTED HERE
  Per SAM CLAUDE.md: script thresholds MUST match THESIS definitions. The delta bar below
  is the SAME >5pp "named driver" bar the carry-bucket method already uses. This script
  does not define new policy — it reports and points at the owner doc.

Appends to workbook/BOJ_OIS.tsv, idempotent by (as_of_date, meeting_date).

Usage:
  .venv/bin/python3 AGENTS/SAM/scripts/boj_ois.py
  .venv/bin/python3 AGENTS/SAM/scripts/boj_ois.py --history      # stored curve history
  .venv/bin/python3 AGENTS/SAM/scripts/boj_ois.py --no-write     # recon only
"""

import html
import re
import sys
import urllib.request
from datetime import datetime, date
from pathlib import Path

SAM_DIR = Path(__file__).resolve().parent.parent
WORKBOOK = SAM_DIR / "workbook"
OIS_TSV = WORKBOOK / "BOJ_OIS.tsv"

SOURCE_URL = "https://centralbank.watch/bank-of-japan/"
SOURCE_NAME = "centralbank.watch"
INSTRUMENT = "3m-TONA-futures"
HEADERS = {"User-Agent": "Mozilla/5.0 (SAM-Research; williepowen@gmail.com)"}

COLUMNS = [
    "as_of_date", "meeting_date", "cum_hike_pct", "hold_pct", "cut_pct",
    "marginal_hike_pct", "unpriced_pct", "basis", "instrument",
    "source", "policy_rate_pct", "quality", "pulled_at",
]

# --- basis assertion -------------------------------------------------------
# Fragments that must ALL be present for the cumulative basis to be considered verified.
# Deliberately short + lowercased so ordinary copy edits don't false-trip, while an actual
# basis CHANGE (to per-meeting/independent odds) removes them.
BASIS_MARKERS = ("cumulative", "already includes any move priced in for")
BASIS_LABEL = "cumulative-from-today"

# --- THESIS-anchored reference (NOT invented here) -------------------------
# The in-window meeting for the locked Sep-18 convexity window. THESIS § THE
# CARRY-CONVEXITY TAIL; the decision day lands ON the inclusive Sep-18 boundary.
IN_WINDOW_MEETING_MONTH = (2026, 9)
# Same >5pp bar the carry-bucket method uses for a "named driver" re-mark
# (THESIS § CARRY-UNWIND PROBABILITY METHOD). Not a new policy.
MATERIAL_DELTA_PP = 5.0

# --- sanity gates (learning from the FXY RR defect: computable != trustworthy) ---
PROB_SUM_TOL_PP = 2.0      # cut+hold+hike must land within this of 100
MAX_MEETINGS = 12          # more than this = parse ran away


def fetch(url=SOURCE_URL):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as r:
        raw = r.read()
    return raw.decode("utf-8", errors="replace")


def to_text(page):
    """Strip scripts/styles/tags to a newline-separated token stream."""
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", page, flags=re.S | re.I)
    t = html.unescape(re.sub(r"<[^>]+>", "\n", t))
    return [ln.strip() for ln in t.split("\n") if ln.strip()]


def verify_basis(lines):
    """Return (ok, evidence). The basis must be ASSERTED, never assumed — this is the
    exact failure the script exists to prevent."""
    blob = " ".join(lines).lower()
    missing = [m for m in BASIS_MARKERS if m not in blob]
    if missing:
        return False, f"missing basis marker(s): {missing}"
    for ln in lines:
        if "cumulative" in ln.lower() and "priced in for" in ln.lower():
            return True, ln[:200]
    return True, "cumulative-basis markers present"


def parse_as_of(lines):
    """Source's OWN data vintage. Never substitute the pull date — that is the whole
    point of the two-clock rule."""
    for i, ln in enumerate(lines):
        if re.fullmatch(r"data as of", ln.strip(), re.I) or re.match(r"data as of\b", ln, re.I):
            chunk = " ".join(lines[i:i + 3])
            m = re.search(r"([A-Z][a-z]+ \d{1,2},? \d{4})", chunk)
            if m:
                for fmt in ("%B %d, %Y", "%B %d %Y"):
                    try:
                        return datetime.strptime(m.group(1).replace(",", " ").replace("  ", " "),
                                                 fmt.replace(",", "")).date()
                    except ValueError:
                        continue
    return None


def parse_policy_rate(lines):
    for i, ln in enumerate(lines):
        if re.search(r"current bo?j policy rate", ln, re.I):
            for nxt in lines[i + 1:i + 4]:
                m = re.search(r"(-?\d+\.\d+)\s*%", nxt)
                if m:
                    return float(m.group(1))
    return None


def parse_meetings(lines):
    """Extract [(meeting_date, cut, hold, hike)] from the repeating
    <date> | Cut | x% | Hold | y% | Hike | z% block."""
    out = []
    for i, ln in enumerate(lines):
        m = re.fullmatch(r"([A-Z][a-z]+ \d{1,2}, \d{4})", ln.strip())
        if not m:
            continue
        try:
            mtg = datetime.strptime(m.group(1), "%B %d, %Y").date()
        except ValueError:
            continue
        window = lines[i + 1:i + 9]
        vals = {}
        for j, w in enumerate(window):
            key = w.strip().lower()
            if key in ("cut", "hold", "hike") and j + 1 < len(window):
                pm = re.match(r"(-?\d+(?:\.\d+)?)\s*%", window[j + 1].strip())
                if pm:
                    vals[key] = float(pm.group(1))
        if {"cut", "hold", "hike"} <= set(vals):
            out.append((mtg, vals["cut"], vals["hold"], vals["hike"]))
    # dedupe by meeting date, keep first, chronological
    seen, uniq = set(), []
    for row in sorted(out, key=lambda r: r[0]):
        if row[0] not in seen:
            seen.add(row[0])
            uniq.append(row)
    return uniq


# 🔴 SOURCE IMPEACHMENT (SAM 2026-08-20, on ORACLE's adversarial verdict + WALTER SIG-W-20260820-001).
# centralbank.watch's SEPTEMBER-2026 leg is refuted MODEL-FREE: under "at most one 25bp hike in
# the 26.09 reference quarter" the observed TFX spread forces P(Sep) >= 81.3%, and its 51-52%
# print would require pricing 126.9% of a hike. The defect is in MEETING ATTRIBUTION, so sibling
# legs are not cleared by agreeing -- an agreement can be cancelling errors
# ([[finding_agreement_at_one_date_can_be_cancelling_errors]]).
#
# WHY THIS LIVES IN THE WRITER AND NOT IN A DOC: on 2026-08-20 WALTER found this TSV publishing
# 52.20 for Sep, quality-flagged "ok", pull-stamped ~30 min BEFORE the packet retiring it. The
# do-not-cite existed only in packet PROSE, so the dead figure was the freshest-stamped,
# cleanest-flagged, only MACHINE-READABLE number SAM published. Readers filter quality == "ok"
# (see latest_rows), so stamping here is what actually stops a downstream cite.
IMPEACHED_SOURCES = {"centralbank.watch"}
IMPEACHED_MEETING_PREFIX = "2026-09"   # the specific refuted leg


def impeach(meeting_iso, quality):
    """Downgrade the quality cell for an impeached source. Canonical tokens per
    AGENTS/DAEDALUS/BLUEPRINTS/STATE_VOCABULARY.md; free prose after the token is allowed."""
    if SOURCE_NAME not in IMPEACHED_SOURCES:
        return quality
    if meeting_iso.startswith(IMPEACHED_MEETING_PREFIX):
        return "SUPERSEDED refuted model-free; cite the converged multi-source row"
    return "UNKNOWN impeached source; this leg not independently corroborated"


def grade(rows, as_of):
    """Per-curve quality. Fail LOUDLY rather than write plausible garbage."""
    problems = []
    if not rows:
        return "none", ["no meetings parsed"]
    if len(rows) > MAX_MEETINGS:
        problems.append(f"{len(rows)} meetings parsed (>{MAX_MEETINGS}) — parse ran away")
    for mtg, cut, hold, hike in rows:
        for nm, v in (("cut", cut), ("hold", hold), ("hike", hike)):
            if not (0.0 <= v <= 100.0):
                problems.append(f"{mtg} {nm}={v} out of [0,100]")
        if abs((cut + hold + hike) - 100.0) > PROB_SUM_TOL_PP:
            problems.append(f"{mtg} cut+hold+hike={cut + hold + hike:.1f} != ~100")
    # cumulative series must be non-decreasing BY CONSTRUCTION
    for a, b in zip(rows, rows[1:]):
        if b[3] < a[3] - 0.05:
            problems.append(f"cumulative hike DECREASES {a[0]}({a[3]}) -> {b[0]}({b[3]}) "
                            f"— impossible on a cumulative basis; parse or basis error")
    if as_of and rows and rows[0][0] < as_of:
        problems.append(f"first meeting {rows[0][0]} predates as-of {as_of}")
    return ("ok" if not problems else "suspect"), problems


def derive(rows):
    """cumulative -> per-meeting marginal + unpriced surprise room."""
    out, prev = [], 0.0
    for mtg, cut, hold, hike in rows:
        out.append({
            "meeting": mtg, "cut": cut, "hold": hold, "cum": hike,
            "marginal": round(hike - prev, 2), "unpriced": round(100.0 - hike, 2),
        })
        prev = hike
    return out


def read_tsv():
    if not OIS_TSV.exists():
        return []
    lines = OIS_TSV.read_text(encoding="utf-8").rstrip("\n").split("\n")
    if len(lines) < 2:
        return []
    hdr = lines[0].split("\t")
    return [dict(zip(hdr, ln.split("\t"))) for ln in lines[1:] if ln.strip()]


def write_rows(as_of, derived, policy_rate, quality):
    """Idempotent by (as_of_date, meeting_date) — NOT by pull date, so re-running the
    same day cannot duplicate and a stale source cannot fabricate new rows."""
    existing = read_tsv()
    have = {(r.get("as_of_date"), r.get("meeting_date")) for r in existing}
    pulled = datetime.now().strftime("%Y-%m-%dT%H:%M")
    new = []
    for d in derived:
        key = (as_of.isoformat(), d["meeting"].isoformat())
        if key in have:
            continue
        new.append("\t".join([
            as_of.isoformat(), d["meeting"].isoformat(),
            f"{d['cum']:.2f}", f"{d['hold']:.2f}", f"{d['cut']:.2f}",
            f"{d['marginal']:.2f}", f"{d['unpriced']:.2f}",
            BASIS_LABEL, INSTRUMENT, SOURCE_NAME,
            "" if policy_rate is None else f"{policy_rate:.2f}",
            impeach(d["meeting"].isoformat(), quality), pulled,
        ]))
    if not OIS_TSV.exists():
        OIS_TSV.write_text("\t".join(COLUMNS) + "\n", encoding="utf-8")
    if new:
        with OIS_TSV.open("a", encoding="utf-8") as fh:
            fh.write("\n".join(new) + "\n")
    return len(new)


def prior_curve(as_of):
    """Most recent stored curve from a STRICTLY EARLIER as-of date (the comparison
    baseline for deltas)."""
    rows = [r for r in read_tsv() if r.get("as_of_date", "") < as_of.isoformat()
            and r.get("quality") == "ok"]
    if not rows:
        return None, {}
    prev_as_of = max(r["as_of_date"] for r in rows)
    return prev_as_of, {r["meeting_date"]: float(r["cum_hike_pct"])
                       for r in rows if r["as_of_date"] == prev_as_of}


def main():
    args = sys.argv[1:]
    no_write = "--no-write" in args

    print(f"\n{'=' * 70}\n  SAM BOJ OIS Monitor — {datetime.now():%Y-%m-%d %H:%M}\n{'=' * 70}\n")

    if "--history" in args:
        rows = read_tsv()
        if not rows:
            print("  no stored history yet")
            return 0
        for a in sorted({r["as_of_date"] for r in rows}):
            cur = [r for r in rows if r["as_of_date"] == a]
            bits = " · ".join(f"{r['meeting_date'][5:]} {float(r['cum_hike_pct']):.1f}%"
                              for r in sorted(cur, key=lambda r: r["meeting_date"]))
            print(f"  as-of {a}  [{cur[0]['quality']}]  {bits}")
        return 0

    try:
        lines = to_text(fetch())
    except Exception as exc:                                   # noqa: BLE001
        print(f"  ⚠️  fetch failed: {exc}\n")
        return 1

    ok_basis, evidence = verify_basis(lines)
    if not ok_basis:
        # HARD STOP. Deltas against stored history are meaningless if the basis moved.
        print("  🔴 BASIS ASSERTION FAILED — refusing to write.")
        print(f"      {evidence}")
        print("      The page no longer states the cumulative basis. Re-read the source")
        print("      before trusting ANY stored delta; the whole series assumes it.\n")
        return 2

    as_of = parse_as_of(lines)
    rows = parse_meetings(lines)
    policy_rate = parse_policy_rate(lines)
    quality, problems = grade(rows, as_of)

    if as_of is None:
        print("  🔴 could not parse the source's 'Data as of' date — refusing to write.")
        print("      Substituting today's date would break the two-clock rule and let a")
        print("      stale page look fresh forever.\n")
        return 2

    derived = derive(rows)
    age = (date.today() - as_of).days

    print(f"  Source:     {SOURCE_NAME} ({INSTRUMENT})")
    print(f"  Basis:      {BASIS_LABEL}  ✓ asserted on page")
    print(f"  Data as of: {as_of}  ({age}d old)" + ("  ⚠️ STALE" if age > 4 else ""))
    if policy_rate is not None:
        print(f"  Policy rate: {policy_rate:.2f}%")
    print(f"  Quality:    {quality}")
    for p in problems:
        print(f"      ⚠️  {p}")
    print()

    prev_as_of, prev = prior_curve(as_of)
    print(f"  {'Meeting':<13}{'cum hike':>10}{'marginal':>10}{'UNPRICED':>10}   vs prior")
    print(f"  {'-' * 60}")
    alerts = []
    for d in derived:
        mk = d["meeting"].isoformat()
        delta = ""
        if mk in prev:
            dv = d["cum"] - prev[mk]
            delta = f"{dv:+.1f}pp"
            if abs(dv) >= MATERIAL_DELTA_PP:
                delta += " 🔴"
                alerts.append((d, dv))
        star = " ◀ IN-WINDOW" if (d["meeting"].year, d["meeting"].month) == IN_WINDOW_MEETING_MONTH else ""
        print(f"  {mk:<13}{d['cum']:>9.1f}%{d['marginal']:>9.1f}%{d['unpriced']:>9.1f}%   {delta:<12}{star}")
    if prev_as_of:
        print(f"\n  (deltas vs stored as-of {prev_as_of})")

    inw = [d for d in derived
           if (d["meeting"].year, d["meeting"].month) == IN_WINDOW_MEETING_MONTH]
    if inw:
        d = inw[0]
        print(f"\n  🎯 IN-WINDOW MEETING {d['meeting']} — surprise room {d['unpriced']:.1f}% unpriced")
        print( "      Route 1 is BOJ hawkish-OF-PRICED: it pays on SURPRISE, so a RISE in")
        print( "      cum hike SHRINKS this edge. Do not read 'more priced' as bullish —")
        print( "      CH-004 is confirmed (a fully-priced hike did NOT unwind carry, Jun-16).")

    if alerts:
        print(f"\n  🔴 MATERIAL MOVE (≥{MATERIAL_DELTA_PP:.0f}pp — the THESIS named-driver bar):")
        for d, dv in alerts:
            print(f"      {d['meeting']}  cum hike {dv:+.1f}pp → unpriced now {d['unpriced']:.1f}%")
        print( "      → a named anchor moved. Re-pencil per THESIS § CARRY-UNWIND")
        print( "        PROBABILITY METHOD (touch ALL changed anchors, not just this one).")

    if quality != "ok":
        print("\n  ⚠️  quality != ok — rows stored but flagged; do NOT cite without a look.")
    if no_write:
        print("\n  --no-write: nothing stored.\n")
        return 0

    added = write_rows(as_of, derived, policy_rate, quality)
    if added:
        print(f"\n  ✓ BOJ_OIS.tsv — appended {added} row(s) for as-of {as_of}")
    else:
        print(f"\n  ✓ BOJ_OIS.tsv — already current for as-of {as_of} (no new data)")
    if SOURCE_NAME in IMPEACHED_SOURCES:
        print("\n" + "=" * 72)
        print("  ⛔ DO NOT CITE THE SEPTEMBER FIGURE ABOVE. THE SOURCE IS IMPEACHED.")
        print("=" * 72)
        print("  centralbank.watch's Sep-2026 leg is refuted MODEL-FREE: the observed TFX")
        print("  spread forces P(Sep) >= 81.3% under at-most-one-hike, and a ~51-52% print")
        print("  would require pricing 126.9% of a hike (ORACLE verdict 2026-08-17).")
        print("  ✅ CITE ~73%, CONVERGED AND FALLING — Kalshi 74.5 / Polymarket 73.5 /")
        print("     TFX 72.2, within 2.3pp in one 7-min window. It is a stored row in")
        print("     BOJ_OIS.tsv under source 'multi-source-converged'.")
        print("  ⚠️  SAM's OWN ~72-77% TFX band is ALSO superseded — it bracketed the truth")
        print("     only because three derivation errors cancelled (+6.0 settlement-column")
        print("     offset, +8.0 day-count f_Sep=0.9121, -19.0 two-meeting reference quarter).")
        print("  ⚠️  Sibling legs (Oct/Dec) are NOT cleared by agreeing — the defect is in")
        print("     MEETING ATTRIBUTION, and an agreement can be cancelling errors.")
        print("  ⚠️  Any TFX cite needs a last-TRADED date: the 8/17 print was a ZERO-VOLUME")
        print("     theoretical mark (all 20 strip contracts 0 lots) — worth 12.2pp.")
    print("\n  ⚠️  SINGLE SOURCE. Corroborate a material move on a wire before re-marking.")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
