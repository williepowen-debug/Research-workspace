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
from datetime import date, datetime, timedelta
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
TERRY_DIR = SCRIPTS_DIR.parent
PAPER_BOOK = TERRY_DIR / "PAPER_BOOK.tsv"
DEFAULT_STALE_DAYS = 2  # business days


def _ensure_deps_or_reexec() -> None:
    """venv self-heal (PROME nit 'venv-for-live-marks', 2026-07-20).

    chain_fetch -> yfinance lives in the repo market-data venv, not base
    python, so a bare `python3 ... paper_book_mark.py` (e.g. boot step 5b)
    degraded every OPEN row to UNMARKED. If the deps are missing AND the repo
    venv exists, re-exec this same command under it so the mark 'just works'
    regardless of how it was invoked. If the venv is absent (or we already
    re-exec'd once), fall through untouched — the run then degrades to
    UNMARKED exactly as before, NEVER a fabricated mark. --selftest is offline
    and calls this before its own branch is reached, so it is not affected
    (it never imports chain_fetch)."""
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

# structure e.g. "TLT Sep-30 77P x45" or "TLT 2026-09-30 77P x45"
STRUCT_RE = re.compile(
    r"^\s*([A-Za-z][A-Za-z0-9.\-]*)\s+"            # 1 ticker
    r"([A-Za-z]{3}-\d{1,2}|\d{4}-\d{2}-\d{2})\s+"  # 2 expiry token
    r"(\d+(?:\.\d+)?)\s*([PCpc])\s*"               # 3 strike, 4 type
    r"x?\s*(\d+)"                                   # 5 qty
)


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

def parse_structure(struct, today=None):
    """Return (ticker, expiry_iso, strike, type_letter, qty) or None."""
    today = today or date.today()
    m = STRUCT_RE.match(struct or "")
    if not m:
        return None
    ticker, exp_tok, strike, tletter, qty = m.groups()
    exp_iso = _expiry_iso(exp_tok, today)
    if exp_iso is None:
        return None
    return ticker.upper(), exp_iso, float(strike), tletter.upper(), int(qty)


def _expiry_iso(tok, today):
    if re.match(r"\d{4}-\d{2}-\d{2}$", tok):
        return tok
    try:
        mon, day = tok.split("-")
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


def compute_mark(match, today, now_str):
    """Given a matched chain row dict, return (mark, mark_asof, note) or
    (None, None, reason). MID when NBBO live; last-trade when stale; never faked."""
    bid, ask, last = match.get("bid"), match.get("ask"), match.get("last")
    last_trade = match.get("last_trade")
    if bid is not None and ask is not None and (bid > 0 or ask > 0):
        mark = round((bid + ask) / 2, 4)
        if last_trade and last_trade[:10] == today.isoformat():
            return mark, now_str, "mid/live"
        return mark, (last_trade or now_str), "mid/stale-quote"
    if last is not None and last > 0:
        return round(last, 4), (last_trade or now_str), "last/no-nbbo"
    return None, None, "NO-QUOTE"


def mark_row(row, today, now_str, fetch=_fetch_chain):
    """Return (new_mark, new_asof, status_note). Non-fatal on any error."""
    parsed = parse_structure(row.get("structure"), today)
    if not parsed:
        return None, None, "PARSE-ERROR"
    ticker, expiry, strike, tletter, _qty = parsed
    opt_type = "put" if tletter == "P" else "call"
    try:
        rows, _meta = fetch(ticker, expiry, opt_type)
    except Exception as e:  # network/yfinance/expiry-gone — never crash the run
        return None, None, f"FETCH-ERROR:{e.__class__.__name__}"
    match = next((r for r in rows
                  if r.get("strike") is not None
                  and abs(r["strike"] - strike) < 1e-6
                  and r.get("type") == tletter), None)
    if match is None:
        return None, None, "NO-STRIKE"
    mark, asof, note = compute_mark(match, today, now_str)
    if mark is None:
        return None, None, note
    return mark, asof, note


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

    stale, marked, problems = [], 0, []
    for r in open_rows:
        new_mark, new_asof, note = mark_row(r, today, now_str)
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
    staleq = {"bid": 0.10, "ask": 0.12, "last": 0.11, "last_trade": "2026-07-17 16:00"}
    m, a, n = compute_mark(staleq, today, now)
    assert m == 0.11 and a == "2026-07-17 16:00" and n == "mid/stale-quote", (m, a, n)
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
    assert mk == 0.11 and note == "mid/stale-quote", (mk, asof, note)

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
