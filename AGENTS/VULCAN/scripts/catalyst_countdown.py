#!/usr/bin/env python3
"""
VULCAN catalyst countdown — ONE READER over VULCAN's dated-event registries, plus a
consumer-side scan of NEIGHBOURS' registries for rows that name VULCAN.

  1. docket/CATALYSTS.tsv       — VULCAN's forward calendar (source of truth)
  2. workbook/PREDICTIONS.tsv   — resolve_date column, OPEN rows only
  3. PROME/DOCKET.tsv           — rows naming VULCAN (read-only, never written)
  4. NEIGHBOURS' catalyst/calendar files — rows naming VULCAN  [see THE TRANSPORT GAP]

PORTED 2026-08-21 from AGENTS/ZHAO/scripts/catalyst_countdown.py, the reference
implementation under the DAEDALUS Q1 ruling (packet de9f1b441). Ported, NOT reinvented:
`finding_port_exposes_what_share_propagates` — reinventing HIDES defects, sharing
PROPAGATES them, porting EXPOSES them. Two exposures on this port are recorded below.

⚠️ DO NOT re-port from OTTO's fork. PROME 2026-08-21, sweep item ⑫: OTTO's look-back is
   mtime-keyed and therefore INERT on any git-synced desk
   (`finding_mtime_is_corrupted_by_git_sync`). ZHAO's basis-PRINTING form is the reference
   precisely because it says which clock it fell back to.

⚠️ THE FIRED-ROW RULE (ported from OTTO via ZHAO, PAT-116). Every past-due row surfaces
   REGARDLESS of priority. Filtering the past-due catch by priority silently re-creates
   the exact miss the countdown exists to prevent.

────────────────────────────────────────────────────────────────────────────────────────
EXPOSURE 1 — SCHEMA DIVERGENCE, deliberately NOT "fixed" by renaming my columns.
   ZHAO's PREDICTIONS.tsv is Title_Case (`Pred_ID`, `Resolve_By`, `Anchor_Type`, `Status`).
   VULCAN's is lower_snake (`id`, `resolve_date`, `anchor_type`, `status`). A verbatim
   port reads NOTHING and warns "no Resolve_By column" — it fails loud, which is correct,
   but the fix is NOT to rename my columns:
     · `resolve_date` and `Resolve_By` are the SAME concept. Adding a second column would
       be duplicate state, which is a defect, not conformance.
     · 7 of my 12 rows are GRADED, frozen calibration artifacts. Renaming columns under a
       graded ledger risks the record for cosmetics.
   So this reader is SCHEMA-TOLERANT (accepts either casing) and the divergence is FLAGGED
   TO DAEDALUS for the 2026-08-28 canonization sweep to rule on. Conform on a ruling, not
   on a guess.

EXPOSURE 2 — THE TRANSPORT GAP, and why leg 4 exists.
   VIOLET's CATALYSTS.tsv has an `agent_domain` column; LIQUID's has `who_cares`. Both
   NAME OTHER DESKS. Neither is transported anywhere. DAEDALUS 2026-08-21: they are LOCAL
   ANNOTATION — "it reads as addressed and isn't: PAT-063's exact class."
   Measured cost on this desk, the day leg 4 was written:
     · NVDA Q2 FY27 earnings 2026-08-26, PRIMARY-VERIFIED at NVIDIA IR, sitting in
       VIOLET's file tagged `VULCAN/VIOLET/HENRY` since 8/18 — while VULCAN carried
       "8/31 NVDA 10-Q" as its S1 tripwire. The capex guide lands at the CALL, 5 days
       earlier than the date this desk held.
     · MU FQ4 ~9/29 flagged by VIOLET as "ESTIMATED, NOT CONFIRMED", while THREE VULCAN
       predictions resolved against it as if settled.
   Leg 4 is the CONSUMER-SIDE fix: it needs no publisher cooperation, no new convention,
   and no fleet rollout — each desk greps its own name out of its neighbours' files.
   ⚠️ STRICTLY READ-ONLY on other agents' trees (PAT-054). This never writes outside
      AGENTS/VULCAN/. It reports; the human decides what to register.
   ⚠️ Coverage matching is BY DATE ONLY and therefore COARSE: a neighbour row on a date
      VULCAN already carries counts as covered even if it is a different event. This
      under-reports. Stated rather than silently tuned — a coarse check that says so
      beats a precise-looking one that doesn't.

Usage:
  .venv/bin/python AGENTS/VULCAN/scripts/catalyst_countdown.py [--days N] [--asof YYYY-MM-DD]
                                                               [--no-neighbours]
"""

import argparse
import csv
import re
import subprocess
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
VULCAN_DIR = SCRIPTS_DIR.parent
REPO = VULCAN_DIR.parent.parent
AGENTS = REPO / "AGENTS"
CATALYSTS_TSV = VULCAN_DIR / "docket" / "CATALYSTS.tsv"
PRED_TSV = VULCAN_DIR / "workbook" / "PREDICTIONS.tsv"
STATUS_MD = VULCAN_DIR / "STATUS.md"
DOCKET_TSV = REPO / "PROME" / "DOCKET.tsv"

DEFAULT_HORIZON = 60
PAST_RETENTION_MIN = 10
PAST_RETENTION_MAX = 120
DATE_CLASS_ENUM = {"confirmed", "external", "estimated", "modeled"}
ANCHOR_ENUM = {"calendar", "publication", "market", "mixed"}
CLOSED_STATUS = ("HIT", "MISS", "RESOLVED", "CONFIRMED", "FALSIFIED", "VOID")

# STATE_VOCABULARY Class 9 (marker-role separation), Will-ruled 2026-08-21: PRIORITY is
# carried by the P1/P2/P3 TEXT token; a coloured circle is severity and is NOT a priority
# glyph. This reader keys every verdict on RETURNED COUNTS, never on scraping glyphs.
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
    d = _git_commit_date(STATUS_MD)
    if d:
        return d, "git-commit"
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
    """(start, end, is_range). 'YYYY-MM-DD..YYYY-MM-DD' encodes month-known-day-unknown.
    Parsing only the start renders an UNANNOUNCED date as a firm deadline."""
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


def _pick(row, *names):
    """EXPOSURE 1: schema-tolerant column access across casing conventions."""
    for n in names:
        if n in row and (row[n] or "").strip():
            return row[n].strip()
    return ""


def _easter(y):
    """Anonymous Gregorian algorithm. Good Friday = Easter - 2."""
    a = y % 19
    b, c = divmod(y, 100)
    d, e = divmod(b, 4)
    g = (8 * b + 13) // 25
    h = (19 * a + b - d - g + 15) % 30
    i, k = divmod(c, 4)
    l = (2 * e + 2 * i - h - k + 32) % 7
    m = (a + 11 * h + 19 * l) // 433
    mo = (h + l - 7 * m + 90) // 25
    day = (h + l - 7 * m + 33 * mo + 19) % 32
    return date(y, mo, day)


def _nth_weekday(y, month, weekday, n):
    """n-th <weekday> of <month>; n<0 counts from the end."""
    if n > 0:
        d = date(y, month, 1)
        d += timedelta(days=(weekday - d.weekday()) % 7)
        return d + timedelta(weeks=n - 1)
    nxt = date(y + (month == 12), (month % 12) + 1, 1)
    d = nxt - timedelta(days=1)
    return d - timedelta(days=(d.weekday() - weekday) % 7)


def _observed(d):
    """NYSE shifts a fixed-date holiday off the weekend: Sat -> Fri, Sun -> Mon."""
    if d.weekday() == 5:
        return d - timedelta(days=1)
    if d.weekday() == 6:
        return d + timedelta(days=1)
    return d


def market_holidays(y):
    """NYSE full-day closures for year y, computed from the RULES, not a hardcoded list.

    ⚠️ ADDED 2026-09-06. `trading_days_between` counted weekdays only, with no holiday
    calendar at all — so on Sunday 2026-09-06 it reported 2026-09-08 as "2d trd" while
    2026-09-07 was Labor Day and the market was closed. EVERY `d trd` figure past the
    next holiday was overstated, silently and in the reassuring direction (more runway
    than exists). This desk grades dated obligations on that distance.

    Rule-based on purpose: a hardcoded year list is a dated carry item that goes stale
    without ever saying so [[finding_dated_carry_item_has_no_expiry_check]].

    ⚠️ NOT MODELLED, and stated rather than hidden: ad-hoc closures (national days of
    mourning, weather) and half-days (the 1pm closes around Thanksgiving/Christmas/July 4).
    A half-day IS a trading day, so omitting half-days is correct here; ad-hoc closures
    are genuinely unpredictable and would make this figure at most 1 day optimistic in a
    rare year. Both are bounded and named.
    """
    hs = {
        _observed(date(y, 1, 1)),               # New Year's Day
        _nth_weekday(y, 1, 0, 3),               # MLK — 3rd Monday January
        _nth_weekday(y, 2, 0, 3),               # Presidents' Day — 3rd Monday February
        _easter(y) - timedelta(days=2),         # Good Friday
        _nth_weekday(y, 5, 0, -1),              # Memorial Day — last Monday May
        _observed(date(y, 6, 19)),              # Juneteenth
        _observed(date(y, 7, 4)),               # Independence Day
        _nth_weekday(y, 9, 0, 1),               # Labor Day — 1st Monday September
        _nth_weekday(y, 11, 3, 4),              # Thanksgiving — 4th Thursday November
        _observed(date(y, 12, 25)),             # Christmas
    }
    # NYSE does NOT observe Jan 1 on the preceding Friday (Dec 31 stays a trading day).
    return {d for d in hs if not (d.month == 12 and d.day == 31)}


_HOLIDAY_CACHE = {}


def is_trading_day(d):
    if d.weekday() >= 5:
        return False
    if d.year not in _HOLIDAY_CACHE:
        _HOLIDAY_CACHE[d.year] = market_holidays(d.year)
    return d not in _HOLIDAY_CACHE[d.year]


def trading_days_between(a, b):
    n, cur = 0, a
    while cur < b:
        cur += timedelta(days=1)
        if is_trading_day(cur):
            n += 1
    return n


def collect(today, want_neighbours=True):
    """(events, warnings, neighbour_hits). event = (date, label, detail, pri, cls, src, dend)"""
    ev, warn = [], []

    # --- 1. docket/CATALYSTS.tsv --------------------------------------------------
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
                warn.append(f"🟠 date_class {cls!r} outside the declared enum {sorted(DATE_CLASS_ENUM)} — {r.get('event','')[:38]}")
            pri = (r.get("priority") or "").strip()
            if pri and not pri.startswith(PRIORITY_TOKENS):
                warn.append(f"🟠 priority {pri!r} carries no P-token (Class 9: the TEXT token carries the role) — {r.get('event','')[:38]}")
            if is_rng and cls != "modeled":
                warn.append(f"🟠 date RANGE with date_class={cls!r} — a range means the day is unknown, i.e. 'modeled': {r.get('event','')[:38]}")
            detail = " · ".join(x for x in [(r.get("what_to_check") or "").strip(),
                                            (r.get("threshold_signal") or "").strip()] if x)
            ev.append((d, r.get("event", ""), detail, pri,
                       "modeled" if is_rng else cls, "CAT", dend))

    # --- 2. PREDICTIONS.tsv (schema-tolerant, EXPOSURE 1) -------------------------
    rows = _rows(PRED_TSV)
    if rows is None:
        warn.append("🔴 PREDICTIONS.tsv NOT FOUND")
    else:
        keys = set(rows[0].keys()) if rows else set()
        if not (keys & {"resolve_date", "Resolve_By"}):
            warn.append("🔴 PREDICTIONS.tsv has NO resolve_date/Resolve_By column — prediction leg is blind")
        for r in rows:
            rb = _pick(r, "resolve_date", "Resolve_By")
            if not rb:
                continue
            d = _parse(rb)
            pid = _pick(r, "id", "Pred_ID") or "?"
            if not d:
                warn.append(f"🔴 UNPARSEABLE resolve date on {pid}: {rb!r}")
                continue
            st = _pick(r, "status", "Status")
            if st.upper().startswith(CLOSED_STATUS):
                continue
            anchor = _pick(r, "anchor_type", "Anchor_Type")
            if anchor and anchor not in ANCHOR_ENUM:
                warn.append(f"🟠 anchor_type {anchor!r} outside the declared enum {sorted(ANCHOR_ENUM)} — {pid}")
            if not anchor:
                warn.append(f"🟠 {pid} has NO anchor_type — its resolve date's slip risk is UNSTATED "
                            f"(`finding_resolver_anchored_to_expected_event_inherits_slip_risk`)")
            # anchor=publication ⇒ the resolve date can slip ⇒ render as modeled (~)
            ev.append((d, f"{pid} resolves — {_pick(r,'prediction','Prediction')[:52]}",
                       f"conf {_pick(r,'conf_tier','Confidence')} · status {st[:32]} · anchor {anchor or 'UNSET'}",
                       "P1", "modeled" if anchor == "publication" else "confirmed", "PRED", d))

    # --- 3. PROME/DOCKET.tsv rows OWNED BY VULCAN (read-only) ---------------------
    # ⚠️ PORT DEFECT FOUND AND FIXED 2026-08-21 — INHERITED, not introduced. The donor
    #    matches its own name anywhere in the row: `if "ZHAO" not in "\t".join(r)`. On
    #    PROME's DOCKET that over-matches 2x for VULCAN — 14 rows MENTION it, only 7 OWN
    #    it. The extras are downstream-route notes ("multi-route WATT/CARL/MARCO/VULCAN
    #    on material steps") on another desk's catalyst: real context, but NOT dated
    #    commitments of mine, and they arrive rendered identically to ones that are.
    #    A register that doubles itself with other desks' events is one nobody reads.
    #    Fix: OWNER FIELD (col 3) decides; mentions are counted, never silently dropped
    #    (`finding_silent_blank_evades_review`). Reported to DAEDALUS for the donor.
    try:
        if DOCKET_TSV.exists():
            mention_only = 0
            with open(DOCKET_TSV, encoding="utf-8", newline="") as f:
                for r in csv.reader(f, delimiter="\t"):
                    if not r or r[0].lstrip().startswith("#") or len(r) < 3:
                        continue
                    if "VULCAN" not in "\t".join(r):
                        continue
                    if "VULCAN" not in r[2]:          # named, but not the owner
                        mention_only += 1
                        continue
                    d, dend, is_rng = _parse_span(r[0])
                    if d:
                        ev.append((d, f"[PROME DOCKET] {r[1][:60]}", "", "P2",
                                   "modeled" if is_rng else "external", "DOCK", dend))
            if mention_only:
                warn.append(f"ℹ️  DOCKET: {mention_only} row(s) NAME VULCAN downstream but are owned "
                            f"by another desk — excluded from the countdown, not dropped silently")
        else:
            warn.append("🟠 PROME/DOCKET.tsv not found — cross-agent leg unread")
    except Exception as e:
        warn.append(f"🟠 DOCKET read failed ({type(e).__name__}) — cross-agent leg unread")

    # --- 4. NEIGHBOURS' registries naming VULCAN (EXPOSURE 2; READ-ONLY) ----------
    hits = []
    if want_neighbours:
        try:
            hits = scan_neighbours(today, ev, warn)
        except Exception as e:
            warn.append(f"🟠 neighbour scan failed ({type(e).__name__}) — transport-gap leg unread")

    return ev, warn, hits


def scan_neighbours(today, ev, warn):
    """Grep neighbours' catalyst/calendar files for rows naming VULCAN. STRICTLY READ-ONLY.

    Reports rows on dates VULCAN's own register does not carry. Coverage matching is BY
    DATE ONLY and therefore coarse (see EXPOSURE 2) — it UNDER-reports rather than
    manufacturing work."""
    mine = {e[0] for e in ev}
    hits, scanned = [], 0
    lo, hi = today - timedelta(days=14), today + timedelta(days=DEFAULT_HORIZON)

    cands = []
    for pat in ("*/workbook/CATALYSTS.tsv", "*/docket/CATALYSTS.tsv", "*/CALENDAR.md"):
        cands += sorted(AGENTS.glob(pat))
    for p in cands:
        owner = p.relative_to(AGENTS).parts[0]
        if owner == "VULCAN":
            continue
        scanned += 1
        try:
            if p.suffix == ".tsv":
                for r in (_rows(p) or []):
                    joined = "\t".join(v or "" for v in r.values())
                    if "VULCAN" not in joined:
                        continue
                    d, _, _ = _parse_span(r.get("date"))
                    if not d or not (lo <= d <= hi) or d in mine:
                        continue
                    hits.append((d, owner, p.relative_to(REPO),
                                 (r.get("event") or "")[:70],
                                 (r.get("date_class") or r.get("type") or "").strip()))
            else:
                for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
                    if "VULCAN" not in line:
                        continue
                    m = re.search(r"\b(20\d\d)-(\d\d)-(\d\d)\b", line)
                    if not m:
                        continue
                    d = _parse(m.group(0))
                    if not d or not (lo <= d <= hi) or d in mine:
                        continue
                    hits.append((d, owner, p.relative_to(REPO),
                                 re.sub(r"\s+", " ", line.strip())[:70], "md-line"))
        except Exception as e:
            warn.append(f"🟠 could not read {p.relative_to(REPO)} ({type(e).__name__})")
    return sorted(set(hits))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=DEFAULT_HORIZON)
    ap.add_argument("--asof", default=None, help="override today (test fixture)")
    ap.add_argument("--no-neighbours", action="store_true",
                    help="skip leg 4 (the read-only neighbour scan)")
    a = ap.parse_args()
    today = _parse(a.asof) or date.today()

    print("\n--- 5. catalyst countdown (CATALYSTS + PREDICTIONS + DOCKET + neighbours) ---")
    ev, warn, hits = collect(today, want_neighbours=not a.no_neighbours)

    for w in warn:
        print(f"  {w}")

    if not ev:
        print("  🔴 NO DATED EVENTS READ AT ALL — a BLIND registry, not an empty calendar.")
        return 2

    retention, basis = past_retention_days(today)
    past_cut = today - timedelta(days=retention)
    fired = sorted([e for e in ev if e[0] < today and e[0] >= past_cut])
    upcoming = sorted([e for e in ev if today <= e[0] <= today + timedelta(days=a.days)])

    # ⚠️ FIRED ROWS SURFACE REGARDLESS OF PRIORITY (PAT-116)
    if fired:
        print(f"\n  ⚠️  RECENTLY FIRED — last {retention}d (since last closeout, basis={basis}) — SWEEP NOW")
        for d, label, detail, pri, cls, src, dend in fired:
            print(f"    {(pri or '').ljust(3)} {d} ({d.strftime('%a')}) {(today-d).days:>3}d ago [{src}] {label[:58]}")
    else:
        print(f"  ✓ nothing fired unswept in the last {retention}d (basis={basis})")

    if not upcoming:
        print(f"  (no dated events within {a.days}d — a blank here is a CLAIM, verify it)")
    else:
        print(f"\n  📅 UPCOMING (≤{a.days}d)")
        for d, label, detail, pri, cls, src, dend in upcoming:
            mark = "~" if cls == "modeled" else " "
            cal, trd = (d - today).days, trading_days_between(today, d)
            span = f"..{dend}" if dend and dend != d else ""
            print(f"    {(pri or '').ljust(3)} {mark}{d}{span}  {cal:>3}d cal /{trd:>3}d trd  [{src}] {label[:56]}")
            if detail and cal <= 14:
                print(f"        ↳ {detail[:104]}")
        print("\n  ('~' = modeled/publication-anchored: the DAY IS A PLACEHOLDER or can slip — re-date when announced)")

    # leg 4 — the transport gap
    if hits:
        print(f"\n  🔔 NEIGHBOUR-TAGGED, NOT IN YOUR REGISTER — {len(hits)} row(s) naming VULCAN in other desks' files")
        print("     (they are LOCAL ANNOTATION — nothing transports them; PAT-063. Read-only scan.)")
        for d, owner, path, event, cls in hits:
            print(f"    {d} ({(d-today).days:+d}d) [{owner}] {event}")
            print(f"        ↳ {path}{('  · '+cls) if cls else ''}")
        print("     ⇒ REGISTER the real ones in docket/CATALYSTS.tsv, or they reach you only by accident.")
    elif not a.no_neighbours:
        print("\n  ✓ neighbour scan: no VULCAN-tagged dates missing from your register")

    rc = 2 if any(w.startswith("🔴") for w in warn) else (1 if (fired or hits) else 0)
    return rc


if __name__ == "__main__":
    sys.exit(main())
