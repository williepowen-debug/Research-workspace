#!/usr/bin/env python3
"""
ZHAO catalyst countdown — ONE READER over ZHAO's THREE dated-event registries.

  1. docket/CATALYSTS.tsv          — ZHAO's forward calendar (source of truth)
  2. workbook/PREDICTIONS.tsv      — Resolve_By column (added 2026-08-21)
  3. PROME/DOCKET.tsv              — rows naming ZHAO (read-only, never written)

Per DAEDALUS ruling 2026-08-21 (Q1): ONE READER over the existing three, never a
fourth registry. The three have different owners and lifecycles — PREDICTIONS rows
are letter-frozen graded artifacts, DOCKET is PROME's cross-agent surface, CATALYSTS
is ZHAO's forward calendar. Merging them would be an interface break for every
consumer AND you would still need the reader. ZHAO's measured defect was never
surface-count: it was INVOCATION.

⚠️ THE FIRED-ROW RULE (ported from OTTO, PAT-116). Every past-due row surfaces
   REGARDLESS of priority. Filtering the past-due catch by priority silently
   re-creates the exact miss the countdown exists to prevent. OTTO 2026-07-25:
   3 of 4 fired rows hidden at boot, one a live resolver dependency.
   ZHAO 2026-08-21: ZHA-15's grade and the Korea tripwire both came due with
   nothing sweeping them. Same class.

⚠️ LOOK-BACK IS ADAPTIVE, AND NOT KEYED ON MTIME. OTTO's version sizes the
   past-window off STATUS.md's st_mtime. ZHAO does NOT copy that: root Data-Hygiene
   canon forbids keying a NEW freshness mechanism on mtime — git sync restamps it and
   it fails FALSE-NEGATIVE (finding_mtime_is_corrupted_by_git_sync, VIOLET 7/27).
   A restamped mtime would read dark_days≈0, collapse the window to the floor, and
   age out exactly the fired rows OTTO's fix exists to catch. We use git commit time
   (the canon-preferred fallback), then content vintage, then mtime last-resort.

Usage:
  .venv/bin/python AGENTS/ZHAO/scripts/catalyst_countdown.py [--days N] [--asof YYYY-MM-DD]
"""

import argparse
import csv
import subprocess
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
ZHAO_DIR = SCRIPTS_DIR.parent
REPO = ZHAO_DIR.parent.parent
CATALYSTS_TSV = ZHAO_DIR / "docket" / "CATALYSTS.tsv"
PRED_TSV = ZHAO_DIR / "workbook" / "PREDICTIONS.tsv"
STATUS_MD = ZHAO_DIR / "STATUS.md"
DOCKET_TSV = REPO / "PROME" / "DOCKET.tsv"

DEFAULT_HORIZON = 60
PAST_RETENTION_MIN = 10
PAST_RETENTION_MAX = 120
DATE_CLASS_ENUM = {"confirmed", "external", "estimated", "modeled"}

# STATE_VOCABULARY Class 9 (marker-role separation) — Will-ruled 2026-08-21, provenance
# this desk's own glyph-collision find. PRIORITY is carried by a P1/P2/P3 TEXT token;
# the coloured circle beside it is DECORATION ONLY. Rationale: a coloured circle that
# means "priority" in one column and "severity" everywhere else makes any marker-scrape
# read a healthy high-priority row as an alert — which is exactly why this file's reader
# keys the boot verdict on RETURNED COUNTS, never on scraping glyphs out of stdout.
PRIORITY_TOKENS = ("P1", "P2", "P3")


def _git_commit_date(path):
    """Canon-preferred vintage: git commit time, NOT mtime (git sync restamps mtime)."""
    try:
        out = subprocess.run(
            ["git", "-C", str(REPO), "log", "-1", "--format=%cI", "--", str(path)],
            capture_output=True, text=True, timeout=10)
        s = out.stdout.strip()[:10]
        return datetime.strptime(s, "%Y-%m-%d").date() if s else None
    except Exception:
        return None


def last_closeout(today):
    """When did ZHAO last write back? git commit time → content vintage → mtime."""
    d = _git_commit_date(STATUS_MD)
    if d:
        return d, "git-commit"
    try:  # content vintage: newest Resolve_By/date we can see
        d = max(_parse(r.get("date", "")) or date.min
                for r in _rows(CATALYSTS_TSV))
        if d != date.min:
            return d, "content"
    except Exception:
        pass
    try:
        return datetime.fromtimestamp(STATUS_MD.stat().st_mtime).date(), "mtime⚠️"
    except OSError:
        return today - timedelta(days=PAST_RETENTION_MIN), "floor"


def past_retention_days(today):
    lc, basis = last_closeout(today)
    dark = (today - lc).days + 3          # +3 grace
    return max(PAST_RETENTION_MIN, min(dark, PAST_RETENTION_MAX)), basis


def _parse(s):
    try:
        return datetime.strptime((s or "").strip(), "%Y-%m-%d").date()
    except Exception:
        return None


def _parse_span(s):
    """Return (start, end, is_range). PROME's DOCKET encodes month-known-day-unknown
    as 'YYYY-MM-DD..YYYY-MM-DD'. Parsing only the start and dropping the range renders
    an UNANNOUNCED date as a firm deadline — the same make-an-unknown-look-certain
    class this desk spent 2026-08-21 chasing. Ranges are carried, not truncated."""
    s = (s or "").strip()
    if ".." in s:
        a, _, b = s.partition("..")
        da, db = _parse(a[:10]), _parse(b[:10])
        if da:
            return da, (db or da), True
    d = _parse(s[:10])
    return (d, d, False) if d else (None, None, False)


def _rows(path):
    if not path.exists():
        return None
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def trading_days_between(a, b):
    n, cur = 0, a
    while cur < b:
        cur += timedelta(days=1)
        if cur.weekday() < 5:
            n += 1
    return n


def collect(today):
    """Return (events, warnings). Each event: (date, label, detail, priority, cls, src)."""
    ev, warn = [], []

    # --- 1. CATALYSTS.tsv
    rows = _rows(CATALYSTS_TSV)
    if rows is None:
        warn.append(f"🔴 {CATALYSTS_TSV.relative_to(REPO)} NOT FOUND — catalyst leg is blind")
    else:
        for r in rows:
            d, dend, is_rng = _parse_span(r.get("date"))
            if not d:
                warn.append(f"🔴 UNPARSEABLE date in CATALYSTS.tsv: {r.get('date')!r} — {r.get('event','')[:44]}")
                continue
            cls = (r.get("date_class") or "").strip()
            if cls and cls not in DATE_CLASS_ENUM:
                warn.append(f"🟠 date_class {cls!r} not in the declared enum {sorted(DATE_CLASS_ENUM)} — {r.get('event','')[:38]}")
            detail = " · ".join(x for x in [
                (r.get("what_to_check") or "").strip(),
                (r.get("threshold_signal") or "").strip()] if x)
            if is_rng and cls != "modeled":
                warn.append(f"🟠 date RANGE with date_class={cls!r} — a range means the day is unknown, so it is 'modeled': {r.get('event','')[:38]}")
            ev.append((d, r.get("event", ""), detail, (r.get("priority") or "").strip(),
                       "modeled" if is_rng else cls, "CAT", dend))

    # --- 2. PREDICTIONS.tsv Resolve_By
    rows = _rows(PRED_TSV)
    if rows is None:
        warn.append("🔴 PREDICTIONS.tsv NOT FOUND")
    elif "Resolve_By" not in (rows[0].keys() if rows else {}):
        warn.append("🔴 PREDICTIONS.tsv has NO Resolve_By column — prediction leg is blind (the WAL ungradeable-book defect)")
    else:
        for r in rows:
            rb = (r.get("Resolve_By") or "").strip()
            if not rb:
                continue
            d = _parse(rb)
            if not d:
                warn.append(f"🔴 UNPARSEABLE Resolve_By on {r.get('Pred_ID')}: {rb!r}")
                continue
            st = (r.get("Status") or "").strip()
            if st.upper().startswith(("RESOLVED", "CONFIRMED", "FALSIFIED")):
                continue
            anchor = (r.get("Anchor_Type") or "").strip()
            ev.append((d, f"{r.get('Pred_ID')} resolves — {(r.get('Prediction') or '')[:52]}",
                       f"conf {r.get('Confidence','')} · status {st[:40]}",
                       "P1 🔴", "modeled" if anchor == "publication" else "confirmed", "PRED", d))

    # --- 3. PROME/DOCKET.tsv rows naming ZHAO (read-only)
    try:
        if DOCKET_TSV.exists():
            with open(DOCKET_TSV, encoding="utf-8", newline="") as f:
                for r in csv.reader(f, delimiter="\t"):
                    if len(r) < 3 or "ZHAO" not in "\t".join(r):
                        continue
                    d, dend, is_rng = _parse_span(r[0])
                    if d:
                        ev.append((d, f"[PROME DOCKET] {r[1][:60] if len(r) > 1 else ''}",
                                   "", "P2 🟠", "modeled" if is_rng else "external", "DOCK", dend))
    except Exception as e:
        warn.append(f"🟠 DOCKET read failed ({type(e).__name__}) — cross-agent leg unread")

    return ev, warn


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=DEFAULT_HORIZON)
    ap.add_argument("--asof", default=None, help="override today (test fixture)")
    a = ap.parse_args()
    today = _parse(a.asof) or date.today()

    print("\n[4] CATALYST COUNTDOWN  — one reader over CATALYSTS + PREDICTIONS.Resolve_By + DOCKET(ZHAO)")
    ev, warn = collect(today)

    for w in warn:
        print(f"    {w}")

    if not ev:
        print("    🔴 NO DATED EVENTS READ AT ALL — this is a BLIND registry, not an empty calendar.")
        return 1

    retention, basis = past_retention_days(today)
    past_cut = today - timedelta(days=retention)
    fired = sorted([e for e in ev if e[0] < today and e[0] >= past_cut])
    upcoming = sorted([e for e in ev if e[0] >= today and e[0] <= today + timedelta(days=a.days)])

    # ⚠️ FIRED ROWS SURFACE REGARDLESS OF PRIORITY (OTTO / PAT-116)
    if fired:
        print(f"\n    ⚠️  RECENTLY FIRED — last {retention}d (since last closeout, basis={basis}) — SWEEP NOW")
        print(f"    {'-'*72}")
        for d, label, detail, pri, cls, src, dend in fired:
            print(f"    {(pri or '').ljust(5)} {d} ({d.strftime('%a')})  {(today-d).days:>3}d ago  [{src}] {label}")
            if detail:
                print(f"         ↳ {detail[:110]}")
    else:
        print(f"\n    ✓ nothing fired unswept in the last {retention}d (basis={basis})")

    if not upcoming:
        print(f"\n    (no dated events within {a.days}d — verify against STATUS CALENDAR; a blank here is a CLAIM)")
    else:
        print(f"\n    📅 UPCOMING (≤{a.days}d)")
        print(f"    {'-'*72}")
        for d, label, detail, pri, cls, src, dend in upcoming:
            mark = "~" if cls == "modeled" else " "
            cal = (d - today).days
            trd = trading_days_between(today, d)
            span = f"..{dend}" if dend and dend != d else ""
            when = f"{mark}{d}{span}"
            print(f"    {(pri or '').ljust(5)} {when:<24s} {cal:>3}d cal /{trd:>3}d trd  [{src}] {label[:52]}")
            if detail and cal <= 14:
                print(f"         ↳ {detail[:110]}")
        print(f"\n    ('~' = modeled date: month known, DAY IS A PLACEHOLDER — re-date when announced)")

    return 1 if any(w.startswith("🔴") for w in warn) else 0


if __name__ == "__main__":
    sys.exit(main())
