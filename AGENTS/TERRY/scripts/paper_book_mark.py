#!/usr/bin/env python3
"""
paper_book_mark.py — mark OPEN rows in TERRY's PAPER_BOOK.tsv to market.

Phase-1 shadow-book helper (see PAPER_BOOK_DESIGN.md, "★ PHASE-1 SHADOW BOOK").
For every OPEN paper row it pulls a live option chain (via chain_fetch.py),
updates `mark` + `mark_asof`, and flags any row whose mark_asof is older than N
business days as STALE. It does NOT score, does NOT compute open-row P&L, and
does NOT execute — scoring is gated on N>=10 CLOSED rows per lane
(PAPER_BOOK_DESIGN.md §Scoring gate). This tool only logs+marks.

Marking convention: long options are marked at the chain MID = (bid+ask)/2.
When the NBBO is unavailable (closed market / weekend -> bid/ask 0 or absent),
the row is marked at the last trade price and mark_asof is stamped to that
last-trade timestamp — NEVER a fabricated live mark. Stale marks are surfaced,
not hidden (same discipline as the ledger-staleness boot alert).

Fill rule (ENTRY/CLOSE, not marking) lives in PAPER_BOOK_DESIGN.md §Fill rules:
ask-for-buys / bid-for-sells at the trigger timestamp, wide-spread penalty,
auditable entry_basis, never mid. This helper only MARKS an OPEN row; it never
sets an entry or close fill.

Usage:
  python3 AGENTS/TERRY/scripts/paper_book_mark.py            # mark OPEN rows + write back
  python3 AGENTS/TERRY/scripts/paper_book_mark.py --dry-run  # print only, no write
  python3 AGENTS/TERRY/scripts/paper_book_mark.py --stale-days 3
  python3 AGENTS/TERRY/scripts/paper_book_mark.py --selftest # offline, no network

cwd note (PAT-031): run from the repo root, e.g.
  (cd "$(git rev-parse --show-toplevel)" && python3 AGENTS/TERRY/scripts/paper_book_mark.py)
"""
from __future__ import annotations

import argparse
import os
import re
import sys
import time
from datetime import date, datetime, timedelta
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
TERRY_DIR = SCRIPTS_DIR.parent
PAPER_BOOK = TERRY_DIR / "PAPER_BOOK.tsv"
DEFAULT_STALE_DAYS = 2   # business days
PHASE2_GATE_COUNT = 6    # trailing-90d would-fire count that opens Phase 2 (PAPER_BOOK_DESIGN.md §Phase 2, pinned 2026-07-24)
SCORING_MIN_CLOSED = 10  # PAPER_BOOK_DESIGN.md 5b — N>=10 CLOSED per lane ...
SCORING_MIN_ANTECEDENTS = 5  # ... AND >=5 DISTINCT antecedents per lane (conjunctive)


def print_scoring_gate(rows) -> None:
    """Make the CONJUNCTIVE scoring gate machine-visible, per lane.

    ⚠️ ADDED 2026-07-30 (RAV + DAEDALUS, converging independently). `PAPER_BOOK_DESIGN.md`
    5b has required BOTH conditions since 7/26 — `N>=10 closed per lane AND >=5 distinct
    antecedents per lane` — but this tool only ever printed the Phase-2 VOLUME gate, and
    the `antecedent` field 5b mandates did not exist as a column at all (it was buried in
    freeform notes, uncountable). So the independence half of the gate was unenforced AND
    unmeasurable: the design said scoring was protected and nothing computed the protection.

    Why the second condition exists (5b's own words): ten rows sharing one antecedent are
    not ten independent trials, they are roughly ONE trial logged ten times — and scoring
    them as ten manufactures false confidence at exactly the moment the gate says it is
    safe to start trusting the record. PB-0001/PB-0002 are the live worked example: same
    card, same underlying, same antecedent, two rows.
    """
    lanes: dict[str, list] = {}
    for r in rows:
        lanes.setdefault((r.get("lane") or "unset").strip(), []).append(r)
    print("\nScoring gate (PAPER_BOOK_DESIGN.md 5b — CONJUNCTIVE, both must hold):")
    for lane in sorted(lanes):
        lr = lanes[lane]
        closed = [r for r in lr if (r.get("status") or "").strip().upper() == "CLOSED"]
        antes = {(r.get("antecedent") or "").strip().lower()
                 for r in closed if (r.get("antecedent") or "").strip()}
        unset = sum(1 for r in lr if not (r.get("antecedent") or "").strip())
        n_ok = len(closed) >= SCORING_MIN_CLOSED
        a_ok = len(antes) >= SCORING_MIN_ANTECEDENTS
        state = "★ OPEN" if (n_ok and a_ok) else "CLOSED"
        # Which condition binds matters: 'N-too-small' wants MORE cards,
        # 'N-not-independent' wants VARIED ones. Different fix, so name it.
        if not n_ok and not a_ok:
            why = "N-too-small (and independence unmet)"
        elif not n_ok:
            why = "N-too-small — need more CLOSED rows"
        elif not a_ok:
            why = "N-not-independent — need VARIED antecedents, not more cards"
        else:
            why = "both conditions met"
        print(f"  lane={lane:6s} closed {len(closed)}/{SCORING_MIN_CLOSED} · "
              f"distinct antecedents {len(antes)}/{SCORING_MIN_ANTECEDENTS} → {state} ({why})")
        if antes:
            print(f"           antecedents: {', '.join(sorted(antes))}")
        if unset:
            print(f"           ⚠️ {unset} row(s) with NO antecedent — uncountable toward independence")
    print("  → no Brier/calibration scoring and no decision acts on this record until a lane shows ★ OPEN.")


def _ensure_deps_or_reexec() -> None:
    """venv self-heal (PROME nit 'venv-for-live-marks', 2026-07-20).

    chain_fetch -> yfinance lives in the repo market-data venv, not base
    python, so a bare `python3 ... paper_book_mark.py` (e.g. boot step 5b)
    degraded every OPEN row to UNMARKED. If the deps are missing AND the repo
    venv exists, re-exec this same command under it so the mark 'just works'
    regardless of how it was invoked. If the venv is absent (or we already
    re-exec'd once), fall through untouched — the run then degrades to
    UNMARKED exactly as before, NEVER a fabricated mark. --selftest is offline
    and is handled in main() BEFORE this function is reached, so it never runs
    the heal at all. *(Corrected 2026-07-30, RAV review: this said selftest
    "calls this before its own branch is reached" — describing the opposite of
    the code. Harmless in effect, but a docstring that misdescribes control
    flow is how the next reader builds on a wrong mental model.)*"""
    try:
        import yfinance  # noqa: F401  # deps present -> nothing to do
        return
    except ModuleNotFoundError:
        pass
    if os.environ.get("_PBM_VENV_REEXEC"):
        return  # already re-exec'd once (venv python also lacks deps) -> degrade
    # NB: do NOT gate on sys.executable != venv_py — the venv's python3 is a
    # symlink to the system python, so .resolve() collapses them and the guard
    # would falsely block re-exec. The env flag above is the loop-breaker.
    venv_py = SCRIPTS_DIR.parents[2] / ".venv" / "bin" / "python3"
    if venv_py.exists():
        os.environ["_PBM_VENV_REEXEC"] = "1"
        os.execv(str(venv_py), [str(venv_py), *sys.argv])

MONTHS = {m: i for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}

# Structures this book actually writes:
#   "TLT Sep-30 77P x45"                              single leg
#   "WAL 2026-09-18 67.5P x1"                         ISO expiry
#   "KRE Dec-18 68P x2 (~8-12% OTM per card ZONE-1)"  trailing prose (ignored)
#   "VIX (VIXW) Aug-05 20C/25C call debit spread x4"  option ROOT + TWO LEGS
#   "VLO Jan-15-2027 360C/380C call debit spread x1"  4-digit-year expiry + two legs
#
# The two-leg and (ROOT) forms were unparseable until 2026-07-30 — PB-0003 marked
# UNMARKED/PARSE-ERROR on the one day it mattered. It failed SAFE (kept the prior mark,
# fabricated nothing), but every live card candidate is a SPREAD (diesel VLO 360C/380C,
# Kharg USO call spread), so the next paper row would have hit it too.
STRUCT_RE = re.compile(
    r"^\s*([A-Za-z][A-Za-z0-9.\-]*)"                    # 1 ticker
    r"(?:\s*\(([A-Za-z][A-Za-z0-9.\-]*)\))?\s+"        # 2 optional option ROOT, e.g. (VIXW)
    r"([A-Za-z]{3}-\d{1,2}(?:-\d{4})?|\d{4}-\d{2}-\d{2})\s+"  # 3 expiry token
    r"(\d+(?:\.\d+)?)\s*([PCpc])"                      # 4 strike1, 5 type1
    r"(?:\s*/\s*(\d+(?:\.\d+)?)\s*([PCpc])?)?"        # 6 strike2, 7 optional type2
    r"[^x]*?x\s*(\d+)"                                 # 8 qty
)


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

def parse_structure(struct, today=None):
    """
    Single-leg contract, unchanged: (ticker, expiry_iso, strike, type_letter, qty) or None.

    Returns None for spreads so no caller can silently mark one leg of a two-leg structure
    as though it were the whole position. Spreads go through parse_legs().
    """
    parsed = parse_legs(struct, today)
    if not parsed or len(parsed["legs"]) != 1:
        return None
    (strike, tletter), = parsed["legs"]
    return parsed["ticker"], parsed["expiry"], strike, tletter, parsed["qty"]


def parse_legs(struct, today=None):
    """
    Full parse, single- or multi-leg.

    Returns {ticker, root, expiry, legs: [(strike, type), ...], qty} or None.
    `root` is the option root when it differs from the underlying ticker (VIX -> VIXW);
    fetches must use the ROOT or they pull the wrong chain entirely.
    Leg order is as written: FIRST leg is the LONG leg, second the SHORT — the convention
    every row in this book already uses ("20C/25C call debit spread" = long 20, short 25).
    """
    today = today or date.today()
    m = STRUCT_RE.match(struct or "")
    if not m:
        return None
    ticker, root, exp_tok, k1, t1, k2, t2, qty = m.groups()
    exp_iso = _expiry_iso(exp_tok, today)
    if exp_iso is None:
        return None
    legs = [(float(k1), t1.upper())]
    if k2 is not None:
        # "20C/25C" -> the second leg inherits the first leg's type when unwritten
        legs.append((float(k2), (t2 or t1).upper()))
    return {
        "ticker": ticker.upper(),
        "root": (root or ticker).upper(),
        "expiry": exp_iso,
        "legs": legs,
        "qty": int(qty),
    }


def _expiry_iso(tok, today):
    if re.match(r"\d{4}-\d{2}-\d{2}$", tok):
        return tok
    try:
        parts = tok.split("-")
        if len(parts) == 3:                   # "Jan-15-2027" — year stated, do not infer
            mon, day, yr = parts
            return date(int(yr), MONTHS[mon.capitalize()], int(day)).isoformat()
        mon, day = parts
        mnum = MONTHS[mon.capitalize()]
        cand = date(today.year, mnum, int(day))
        if cand < today:                      # already passed -> next year
            cand = date(today.year + 1, mnum, int(day))
        return cand.isoformat()
    except (KeyError, ValueError):
        return None


def _asof_date(asof):
    """Extract a date from a mark_asof cell like '2026-07-17 16:00 ET'."""
    if not asof:
        return None
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", asof.strip())
    if not m:
        return None
    return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))


def business_days_between(d1, d2):
    """Count weekdays in the half-open interval (d1, d2]. 0 if d2<=d1 or d1 None."""
    if d1 is None or d2 is None or d2 <= d1:
        return 0
    days, cur = 0, d1
    while cur < d2:
        cur += timedelta(days=1)
        if cur.weekday() < 5:
            days += 1
    return days


# ---------------------------------------------------------------------------
# TSV load / save (preserves '#' banner + header)
# ---------------------------------------------------------------------------

def load_tsv(path):
    lines = path.read_text().splitlines()
    banner, header, data = [], None, []
    for ln in lines:
        if header is None:
            if ln.split("\t")[0] == "paper_id":
                header = ln.split("\t")
            else:
                banner.append(ln)
        else:
            if ln.strip() == "":
                continue
            data.append(ln.split("\t"))
    if header is None:
        raise ValueError("PAPER_BOOK.tsv: no header row starting with 'paper_id'")
    rows = []
    for cells in data:
        cells = (cells + [""] * len(header))[: len(header)]
        rows.append(dict(zip(header, cells)))
    return banner, header, rows


def save_tsv(path, banner, header, rows):
    out = list(banner)
    out.append("\t".join(header))
    for r in rows:
        out.append("\t".join((r.get(c, "") or "") for c in header))
    path.write_text("\n".join(out) + "\n")


# ---------------------------------------------------------------------------
# Marking
# ---------------------------------------------------------------------------

def _fetch_chain(ticker, expiry, opt_type):
    """Import chain_fetch lazily so --selftest stays network-free."""
    sys.path.insert(0, str(SCRIPTS_DIR))
    import chain_fetch
    return chain_fetch.fetch_chain(ticker, expiry, opt_type)


def _make_run_fetch(base_fetch=_fetch_chain, retries=1, sleep_s=0.5):
    """Per-run chain fetch: dedupe identical (ticker,expiry,type) pulls within one
    run (twin rows on the same series pull ONCE and mark identically) and retry
    once on a transient fetch error (yfinance JSONDecodeError / rate-limit flake)
    so a random hiccup does not leave one row UNMARKED while its twin marks fine
    (the 2026-07-24 PB-0001 case). Only SUCCESSFUL pulls are cached; a hard
    failure after all retries propagates so mark_row degrades to UNMARKED — never
    a fabricated mark."""
    cache = {}

    def fetch(ticker, expiry, opt_type):
        key = (ticker, expiry, opt_type)
        if key in cache:
            return cache[key]
        last_exc = None
        for attempt in range(retries + 1):
            try:
                result = base_fetch(ticker, expiry, opt_type)
                cache[key] = result
                return result
            except Exception as e:  # transient — retry, then propagate
                last_exc = e
                if attempt < retries and sleep_s:
                    time.sleep(sleep_s)
        raise last_exc

    return fetch


def _wf_event_key(row):
    """Dedup key for would-fire counting: the INSTRUMENT the event fired into.

    A would-fire EVENT is a card reaching would-fire state — not a ledger row.
    Rows multiply per event by construction (the documented PB-0001/PB-0002 pair =
    two rows, ONE observation of TRY-FIRE-004; the RULING-D split PB-0002a/PB-0002b
    = one fill, two rows), so counting rows inflated the Phase-2 counter to 5/6 on
    2026-08-07 when the distinct-event count was 3 (flagged in the ledger's own
    banner that day; fix authorized by Will 2026-08-13).

    Key = parsed (root, expiry, legs) — qty EXCLUDED (x45/x25/x5 are tranches of
    one event, never three events). Expiry is resolved against the row's OPENED
    date, not today: "Sep-30" written in July must key to 2026-09-30 forever, even
    when this runs after that date has passed — otherwise a Jan-inferred year flip
    splits a key mid-window. Fallbacks when the structure is unparseable: card_id,
    then paper_id with any split-letter suffix stripped (PB-0002a -> PB-0002).

    ⚠️ Known tie-break, DOWNWARD by design: two genuinely different cards firing
    into the identical instrument inside one 90d window would collapse to one
    event. Under-counting cannot false-trip the Will-pinned gate; a late trip
    costs attention timing, a false trip spends a $1,500/mo conversation on
    arithmetic. The conservative direction is the safe one for this gate."""
    opened = _asof_date(row.get("opened"))
    parsed = parse_legs(row.get("structure"), opened)
    if parsed:
        return ("instr", parsed["root"], parsed["expiry"], tuple(parsed["legs"]))
    cid = (row.get("card_id") or "").strip()
    if cid:
        return ("card", cid)
    pid = (row.get("paper_id") or "").strip()
    return ("pid", re.sub(r"^([A-Za-z]+-\d+)[a-z]$", r"\1", pid))


def would_fire_90d(rows, today):
    """Trailing-90-day DISTINCT would-fire events = the Phase-2 volume-gate metric
    (PAPER_BOOK_DESIGN.md §Phase 2; gate opens at PHASE2_GATE_COUNT). An event is
    counted once regardless of how many rows record it (see _wf_event_key); a card
    that fired and closed still fired. Returns (distinct_events, raw_rows) so the
    display can show both — the raw count stays visible precisely because it is
    the number that was wrong."""
    events, raw = set(), 0
    for r in rows:
        # RULING E (Will-ruled 2026-08-19, queue row 63, Option 3): approval-pending
        # rows are LOGGED but EXCLUDED from this Will-pinned gate until Will flips
        # inclusion — preserves the 8/13 fix's bias (an under-count cannot false-trip).
        if "approval-pending" in (r.get("notes") or "").lower():
            continue
        d = _asof_date(r.get("opened"))
        if d is not None and 0 <= (today - d).days <= 90:
            raw += 1
            events.add(_wf_event_key(r))
    return len(events), raw


def compute_mark(match, today, now_str):
    """Given a matched chain row dict, return (mark, mark_asof, note) or
    (None, None, reason). MID when NBBO live; last-trade when stale; never faked."""
    bid, ask, last = match.get("bid"), match.get("ask"), match.get("last")
    last_trade = match.get("last_trade")
    if bid is not None and ask is not None and (bid > 0 or ask > 0):
        mark = round((bid + ask) / 2, 4)
        # mark_asof describes WHEN THE MARK WAS TAKEN — always now, because the mid comes
        # from the CURRENT two-sided quote. Stamping it with last_trade (the pre-2026-07-30
        # behaviour) made a live mid look 10 business days old on any illiquid strike and
        # tripped a STALE alarm on it. This book is deep-OTM options; "quoted but not traded
        # today" is its NORMAL state, not a defect, and conflating the two cries wolf exactly
        # where the alarm needs to be trusted. Illiquidity is still reported — in the NOTE,
        # which is where it belongs — rather than by falsifying the timestamp.
        if last_trade and last_trade[:10] == today.isoformat():
            return mark, now_str, "mid/live"
        return mark, now_str, f"mid/live-quote (no trade since {last_trade or 'unknown'})"
    if last is not None and last > 0:
        # No two-sided market: the mark really IS as old as the last print. Timestamp it so.
        return round(last, 4), (last_trade or now_str), "last/no-nbbo"
    return None, None, "NO-QUOTE"


def mark_row(row, today, now_str, fetch=_fetch_chain):
    """Return (new_mark, new_asof, status_note). Non-fatal on any error."""
    parsed = parse_legs(row.get("structure"), today)
    if not parsed:
        return None, None, "PARSE-ERROR"
    root, expiry, legs = parsed["root"], parsed["expiry"], parsed["legs"]

    leg_marks, notes = [], []
    for strike, tletter in legs:
        opt_type = "put" if tletter == "P" else "call"
        try:
            rows, _meta = fetch(root, expiry, opt_type)
        except Exception as e:  # network/yfinance/expiry-gone — never crash the run
            return None, None, f"FETCH-ERROR:{e.__class__.__name__}"
        match = next((r for r in rows
                      if r.get("strike") is not None
                      and abs(r["strike"] - strike) < 1e-6
                      and r.get("type") == tletter), None)
        if match is None:
            return None, None, f"NO-STRIKE:{strike:g}{tletter}"
        mk, _asof, note = compute_mark(match, today, now_str)
        if mk is None:
            # One dead leg means NO net mark. Never mark a spread off its live leg alone —
            # that would report a two-leg position at a one-leg value, which is worse than
            # reporting nothing (`finding_fail_loud_on_incomplete_data`).
            return None, None, f"{note}:{strike:g}{tletter}"
        leg_marks.append(mk)
        notes.append(note)

    if len(leg_marks) == 1:
        return leg_marks[0], now_str, notes[0]

    # Spread: net = LONG (first leg, as written) minus SHORT (second). Positive = debit.
    net = round(leg_marks[0] - leg_marks[1], 4)
    detail = "+".join(f"{k:g}{t}@{m:g}" for (k, t), m in zip(legs, leg_marks))
    worst = "live" if all(n == "mid/live" for n in notes) else "live-quote"
    return net, now_str, f"net-mid/{worst} [{detail}]"


def run(args):
    if not PAPER_BOOK.exists():
        print(f"FATAL: {PAPER_BOOK} not found.")
        return 2
    banner, header, rows = load_tsv(PAPER_BOOK)
    today = date.today()
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M") + " local"

    open_rows = [r for r in rows if (r.get("status") or "").upper().startswith("OPEN")]
    print("TERRY paper-book mark")
    print("=====================")
    print(f"PAPER — card-quality shadow book, NOT an endorsed P&L. {PAPER_BOOK.name}")
    print(f"OPEN rows: {len(open_rows)} of {len(rows)} | stale-bar: {args.stale_days} business days\n")

    run_fetch = _make_run_fetch()  # dedupe identical series + retry-once on transient flake
    stale, marked, problems = [], 0, []
    for r in open_rows:
        new_mark, new_asof, note = mark_row(r, today, now_str, fetch=run_fetch)
        pid = r.get("paper_id", "?")
        struct = r.get("structure", "?")
        if new_mark is None:
            problems.append((pid, struct, note))
            # keep the prior mark; still evaluate its staleness below
        else:
            r["mark"], r["mark_asof"] = f"{new_mark:g}", new_asof
            marked += 1
        asof_d = _asof_date(r.get("mark_asof"))
        age = business_days_between(asof_d, today)
        is_stale = age > args.stale_days
        flag = f"  ⚠ STALE {age}bd" if is_stale else ""
        if is_stale:
            stale.append((pid, struct, r.get("mark_asof"), age))
        src = note if new_mark is not None else f"UNMARKED ({note})"
        print(f"  {pid:<8} {struct:<22} mark={r.get('mark','?'):>7} "
              f"asof={r.get('mark_asof','?'):<22} [{src}]{flag}")

    print(f"\nMarked: {marked} | Stale (>{args.stale_days}bd): {len(stale)} | "
          f"Unmarked: {len(problems)}")
    for pid, struct, asof, age in stale:
        print(f"  ⚠ STALE  {pid} {struct} — mark_asof {asof} ({age} business days)")
    for pid, struct, note in problems:
        print(f"  ⚠ UNMARKED {pid} {struct} — {note} (prior mark kept, not fabricated)")

    gate, raw_rows = would_fire_90d(rows, today)
    if gate >= PHASE2_GATE_COUNT:
        gate_msg = "— ★ GATE TRIPPED: Phase-2 salaried-desk trigger met (PAPER_BOOK_DESIGN.md §Phase 2 — confirm salary tranche w/ Will)"
    else:
        gate_msg = "(un-tripped; Phase 1 shadow-only)"
    dup_note = f" [{raw_rows} rows; splits/twins dedup to events]" if raw_rows != gate else ""
    print(f"\nPhase-2 volume gate: would-fire (90d) {gate}/{PHASE2_GATE_COUNT} distinct events{dup_note} {gate_msg}")
    print_scoring_gate(rows)

    if args.dry_run:
        print("\n--dry-run: no write.")
    else:
        save_tsv(PAPER_BOOK, banner, header, rows)
        print(f"\nWrote {PAPER_BOOK}")
    print("\nScoring is gated on N>=10 CLOSED rows per lane — this tool only logs+marks.")
    return 0


# ---------------------------------------------------------------------------
# Self-test (offline — no network)
# ---------------------------------------------------------------------------

def selftest():
    today = date(2026, 7, 19)  # a Sunday

    # parse_structure
    p = parse_structure("TLT Sep-30 77P x45", today)
    assert p == ("TLT", "2026-09-30", 77.0, "P", 45), p
    p2 = parse_structure("WAL 2026-09-18 67.5P x1", today)
    assert p2 == ("WAL", "2026-09-18", 67.5, "P", 1), p2
    assert parse_structure("garbage", today) is None
    # calls + already-passed month rolls to next year
    pc = parse_structure("SPY Jan-16 500C x2", today)
    assert pc == ("SPY", "2027-01-16", 500.0, "C", 2), pc
    # trailing prose must not defeat the parse (PB-0004 carries a ZONE-1 note)
    assert parse_structure("KRE Dec-18 68P x2 (~8-12% OTM per card ZONE-1)", today) \
        == ("KRE", "2026-12-18", 68.0, "P", 2)

    # --- multi-leg / option-root parsing (the PB-0003 PARSE-ERROR class, fixed 2026-07-30)
    sp = parse_legs("VIX (VIXW) Aug-05 20C/25C call debit spread x4", today)
    assert sp == {"ticker": "VIX", "root": "VIXW", "expiry": "2026-08-05",
                  "legs": [(20.0, "C"), (25.0, "C")], "qty": 4}, sp
    # 4-digit-year expiry must be taken literally, never year-inferred
    vlo = parse_legs("VLO Jan-15-2027 360C/380C call debit spread x1", today)
    assert vlo["expiry"] == "2027-01-15" and len(vlo["legs"]) == 2, vlo
    # a spread must NOT come back from the single-leg API — no caller may mark one leg
    # of a two-leg position as though it were the whole thing
    assert parse_structure("VIX (VIXW) Aug-05 20C/25C call debit spread x4", today) is None

    # business_days_between: Fri 7/17 -> Sun 7/19 = 0 (weekend only); -> Tue 7/21 = 2
    assert business_days_between(date(2026, 7, 17), date(2026, 7, 19)) == 0
    assert business_days_between(date(2026, 7, 17), date(2026, 7, 21)) == 2
    assert business_days_between(date(2026, 7, 17), date(2026, 7, 17)) == 0

    # _asof_date
    assert _asof_date("2026-07-17 16:00 ET") == date(2026, 7, 17)
    assert _asof_date("") is None

    # compute_mark: live NBBO -> mid @ now; stale quote -> mid @ last_trade; no nbbo -> last
    now = "2026-07-19 12:00 local"
    live = {"bid": 0.10, "ask": 0.12, "last": 0.11, "last_trade": "2026-07-19 15:30"}
    m, a, n = compute_mark(live, today, now)
    assert m == 0.11 and a == now and n == "mid/live", (m, a, n)
    # A live two-sided quote on an option that has not TRADED today is the normal state of
    # this book (deep-OTM). The mark is as-of NOW because that is when the quote was pulled;
    # the illiquidity goes in the note. Pre-2026-07-30 this stamped last_trade and then
    # tripped its own STALE alarm on a perfectly live mid (PB-0004, "STALE 10bd").
    quoted = {"bid": 0.10, "ask": 0.12, "last": 0.11, "last_trade": "2026-07-17 16:00"}
    m, a, n = compute_mark(quoted, today, now)
    assert m == 0.11 and a == now and n.startswith("mid/live-quote"), (m, a, n)
    assert "2026-07-17 16:00" in n, "illiquidity must stay visible in the note"

    # No two-sided market -> the mark really IS as old as the last print, so timestamp it so.
    nonbbo = {"bid": None, "ask": None, "last": 0.11, "last_trade": "2026-07-17 16:00"}
    m, a, n = compute_mark(nonbbo, today, now)
    assert m == 0.11 and a == "2026-07-17 16:00" and n == "last/no-nbbo", (m, a, n)
    nonbbo = {"bid": 0.0, "ask": 0.0, "last": 0.09, "last_trade": "2026-07-17 16:00"}
    m, a, n = compute_mark(nonbbo, today, now)
    assert m == 0.09 and n == "last/no-nbbo", (m, a, n)
    dead = {"bid": 0.0, "ask": 0.0, "last": 0.0, "last_trade": None}
    m, a, n = compute_mark(dead, today, now)
    assert m is None and n == "NO-QUOTE", (m, a, n)

    # mark_row with a stubbed fetch (no network)
    def stub_fetch(ticker, expiry, opt_type):
        assert (ticker, expiry, opt_type) == ("TLT", "2026-09-30", "put")
        return ([{"strike": 77.0, "type": "P", "bid": 0.10, "ask": 0.12,
                  "last": 0.11, "last_trade": "2026-07-17 16:00"}], {})
    mk, asof, note = mark_row({"structure": "TLT Sep-30 77P x45"}, today, now, fetch=stub_fetch)
    assert mk == 0.11 and asof == now and note.startswith("mid/live-quote"), (mk, asof, note)

    # load/save round-trip preserves banner + header
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        tp = Path(td) / "pb.tsv"
        tp.write_text(
            "# banner line\n"
            "paper_id\tstructure\tmark\tmark_asof\tstatus\n"
            "PB-0001\tTLT Sep-30 77P x45\t0.11\t2026-07-17 16:00 ET\tOPEN\n"
        )
        b, h, rws = load_tsv(tp)
        assert b == ["# banner line"], b
        assert h[0] == "paper_id" and rws[0]["status"] == "OPEN"
        rws[0]["mark"] = "0.10"
        save_tsv(tp, b, h, rws)
        b2, h2, rws2 = load_tsv(tp)
        assert b2 == b and rws2[0]["mark"] == "0.10"

    # _make_run_fetch: dedupe (base called once for same key) + retry-once
    calls = {"n": 0}

    def flaky_once(ticker, expiry, opt_type):
        calls["n"] += 1
        if calls["n"] == 1:
            raise ValueError("simulated JSONDecodeError")  # first attempt flakes
        return ([{"strike": 77.0, "type": "P"}], {})
    rf = _make_run_fetch(base_fetch=flaky_once, retries=1, sleep_s=0)
    r1 = rf("TLT", "2026-09-30", "put")            # attempt1 fails -> retry succeeds
    assert r1[0][0]["strike"] == 77.0 and calls["n"] == 2, calls
    r2 = rf("TLT", "2026-09-30", "put")            # cache hit -> base NOT called again
    assert r2 is r1 and calls["n"] == 2, calls
    # distinct key -> fresh pull
    rf("WAL", "2026-09-18", "put")
    assert calls["n"] == 3, calls

    # hard failure after retries -> propagates (row degrades to UNMARKED, never faked)
    # --- spread marking: net = long leg minus short leg, both legs required
    def two_leg_fetch(ticker, expiry, opt_type):
        assert ticker == "VIXW", f"must fetch the option ROOT, not the underlying: {ticker}"
        return ([{"strike": 20.0, "type": "C", "bid": 1.20, "ask": 1.26,
                  "last": 1.23, "last_trade": f"{today.isoformat()} 15:30"},
                 {"strike": 25.0, "type": "C", "bid": 0.50, "ask": 0.56,
                  "last": 0.53, "last_trade": f"{today.isoformat()} 15:30"}], {})
    mk, asof, note = mark_row(
        {"structure": "VIX (VIXW) Aug-05 20C/25C call debit spread x4"},
        today, now, fetch=two_leg_fetch)
    assert mk == 0.7 and note.startswith("net-mid/live"), (mk, note)  # 1.23 - 0.53

    # one dead leg => NO net mark. Marking a spread off its live leg alone would report a
    # two-leg position at a one-leg value — worse than reporting nothing.
    def one_dead_leg(ticker, expiry, opt_type):
        return ([{"strike": 20.0, "type": "C", "bid": 1.20, "ask": 1.26,
                  "last": 1.23, "last_trade": f"{today.isoformat()} 15:30"},
                 {"strike": 25.0, "type": "C", "bid": None, "ask": None,
                  "last": None, "last_trade": None}], {})
    mk2, _a2, note2 = mark_row(
        {"structure": "VIX (VIXW) Aug-05 20C/25C call debit spread x4"},
        today, now, fetch=one_dead_leg)
    assert mk2 is None and "NO-QUOTE" in note2, (mk2, note2)

    def always_fails(ticker, expiry, opt_type):
        raise RuntimeError("dead feed")
    rf2 = _make_run_fetch(base_fetch=always_fails, retries=1, sleep_s=0)
    try:
        rf2("TLT", "2026-09-30", "put")
        assert False, "expected propagation"
    except RuntimeError:
        pass

    # would_fire_90d: DISTINCT events, not rows (fix authorized 2026-08-13; the 8/7
    # live ledger printed 5/6 on a distinct-event count of 3 — that exact shape is
    # the regression case below). Window/blank handling unchanged.
    tref = date(2026, 7, 24)
    wf_rows = [
        {"paper_id": "PB-1", "structure": "TLT Sep-30 77P x45",
         "opened": "2026-07-17 16:00 ET", "status": "OPEN"},    # 7d ago -> in
        {"paper_id": "PB-2", "structure": "KRE Dec-18 68P x2",
         "opened": "2026-07-20 09:50 ET", "status": "CLOSED"},  # 4d ago, closed -> in
        {"paper_id": "PB-3", "structure": "SPY Jan-16 500C x2",
         "opened": "2026-04-01 10:00 ET", "status": "CLOSED"},  # 114d ago -> out
        {"paper_id": "PB-4", "structure": "WAL 2026-09-18 67.5P x1",
         "opened": "", "status": "OPEN"},                        # blank -> out
    ]
    assert would_fire_90d(wf_rows, tref) == (2, 2), would_fire_90d(wf_rows, tref)

    # ★ REGRESSION — the live 2026-08-07 ledger shape: 5 rows in window, 3 events.
    # PB-0001 + PB-0002a + PB-0002b are three rows of ONE observation (same TLT
    # Sep-30 77P; the documented pair + the RULING-D split); qty differs and must
    # not split the key.
    live_shape = [
        {"paper_id": "PB-0001", "card_id": "TRY-FIRE-004-ZONE2/3",
         "structure": "TLT Sep-30 77P x45", "opened": "2026-07-17 16:00 ET"},
        {"paper_id": "PB-0002a", "card_id": "TRY-FIRE-004-ZONE3-FILL",
         "structure": "TLT Sep-30 77P x5 (HARVEST TRANCHE)", "opened": "2026-07-20 09:50 ET"},
        {"paper_id": "PB-0002b", "card_id": "TRY-FIRE-004-ZONE3-FILL",
         "structure": "TLT Sep-30 77P x25 (REMAINING TRANCHE)", "opened": "2026-07-20 09:50 ET"},
        {"paper_id": "PB-0003", "card_id": "TRY-VIOLET-VIXCS-ZONE2-FILL",
         "structure": "VIX (VIXW) Aug-05 20C/25C call debit spread x4", "opened": "2026-07-27 11:38 ET"},
        {"paper_id": "PB-0004", "card_id": "TRY-FIRE-001-HY280",
         "structure": "KRE Dec-18 68P x2 (~8-12% OTM per card ZONE-1)", "opened": "2026-07-30 13:02 ET"},
    ]
    got = would_fire_90d(live_shape, date(2026, 8, 13))
    assert got == (3, 5), got

    # Key stability across an expiry passing: "Sep-30" opened in July and its ISO
    # twin "2026-09-30" must collapse to ONE event even when counted AFTER Sep-30
    # (expiry resolves against the row's OPENED date, never today).
    post_expiry = [
        {"paper_id": "PB-A", "structure": "TLT Sep-30 77P x45", "opened": "2026-07-17 16:00 ET"},
        {"paper_id": "PB-B", "structure": "TLT 2026-09-30 77P x25", "opened": "2026-07-20 09:50 ET"},
    ]
    got2 = would_fire_90d(post_expiry, date(2026, 10, 5))
    assert got2 == (1, 2), got2

    # Fallbacks: unparseable structure -> card_id; no card_id -> paper_id with the
    # split-letter suffix stripped (PB-0009a/PB-0009b -> one event).
    fb = [
        {"paper_id": "PB-0009a", "card_id": "", "structure": "not parseable",
         "opened": "2026-07-20 09:00 ET"},
        {"paper_id": "PB-0009b", "card_id": "", "structure": "also not parseable",
         "opened": "2026-07-20 09:00 ET"},
        {"paper_id": "PB-0010", "card_id": "TRY-X-CARD", "structure": "garbage",
         "opened": "2026-07-21 09:00 ET"},
    ]
    got3 = would_fire_90d(fb, tref)
    assert got3 == (2, 3), got3

    print("paper_book_mark.py SELFTEST: PASS")
    return 0


def main():
    ap = argparse.ArgumentParser(description="TERRY paper-book mark-to-market helper")
    ap.add_argument("--dry-run", action="store_true", help="print marks, do not write back")
    ap.add_argument("--stale-days", type=int, default=DEFAULT_STALE_DAYS,
                    help=f"business-day staleness bar (default {DEFAULT_STALE_DAYS})")
    ap.add_argument("--selftest", action="store_true", help="offline self-test (no network)")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    _ensure_deps_or_reexec()  # venv self-heal before any live chain fetch
    return run(args)


if __name__ == "__main__":
    raise SystemExit(main())
