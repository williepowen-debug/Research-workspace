#!/usr/bin/env python3
"""partb_realized_moves.py — IV-crush diagnostic PART B (the free proxy).

Spec: IV_CRUSH_DIAGNOSTIC_PLAN.md §Part B (registered 2026-07-17, queued 2026-08-04,
run 2026-08-13 Will-directed). For each basket name: last 6-8 earnings dates,
realized 1-day (close-to-close) post-print move from free price history, compared
against (a) each other (the distribution) and (b) the strike distances the July
bank-put book actually bought (12.7-15.5% OTM). Consistently-smaller realized moves
=> structurally buying overpriced event vol / unreachable strikes => the crush+depth
diagnosis confirmed by proxy.

LIMITS (named, not hidden): proxies crush via realized-vs-needed move, not direct
IV (Part C, the direct measure, is KILLED — paid data, Will 8/4). Reaction-day
attribution uses the yfinance earnings timestamp when it carries a real clock;
otherwise the name's known convention (WAL/OZK/ZION AMC, HBAN BMO). Rows where
history is missing print as gaps — never silently dropped.

Run:  (cd "$(git rev-parse --show-toplevel)" && python3 AGENTS/TERRY/options/partb_realized_moves.py)
Self-heals under .venv like the desk's other chain tools.
"""
from __future__ import annotations

import os
import sys
from datetime import date
from pathlib import Path

N_PRINTS = 8
# Reaction-day convention fallback, used ONLY when the vendor timestamp carries no
# real clock. Adding a name here does NOT widen rule #18's measured envelope — the
# envelope is whatever THIS tool prints for that name. Rule #18's 10%-OTM line was
# measured on the regional-bank four and is name-class-specific by its own text.
CONVENTION = {"WAL": "AMC", "OZK": "AMC", "HBAN": "BMO", "ZION": "AMC",
              # cruise (added 2026-09-19, rule #18 re-measure for a new sector):
              # CCL/RCL/NCLH all release results pre-open and hold the call the
              # same morning => reaction is the SAME session.
              "CCL": "BMO", "RCL": "BMO", "NCLH": "BMO"}
DEFAULT_BASKET = ["WAL", "OZK", "HBAN", "ZION"]
# The July book's strike depth at entry (Part A, 7/17 spots): what the puts NEEDED.
BOOK_DEPTH = {"WAL": 15.5, "OZK": 13.8, "HBAN": 12.7}  # % OTM at 7/17


def _ensure_deps_or_reexec():
    try:
        import yfinance  # noqa: F401
        return
    except ModuleNotFoundError:
        pass
    if os.environ.get("_PBRM_VENV_REEXEC"):
        return
    venv_py = Path(__file__).resolve().parents[3] / ".venv" / "bin" / "python3"
    if venv_py.exists():
        os.environ["_PBRM_VENV_REEXEC"] = "1"
        os.execv(str(venv_py), [str(venv_py), *sys.argv])


def reaction_day(ts, ticker):
    """AMC print -> reaction is the NEXT session; BMO -> the SAME session.
    A timestamp with a real clock decides; a midnight-looking stamp falls back to
    the name's convention (stated in output so the fallback is auditable)."""
    if ts.hour >= 15:
        return "next", "ts"
    if 0 < ts.hour <= 9:
        return "same", "ts"
    conv = CONVENTION.get(ticker, "AMC")
    return ("next" if conv == "AMC" else "same"), f"conv:{conv}"


def run(basket=None):
    import pandas as pd
    import yfinance as yf

    basket = basket or DEFAULT_BASKET
    today = date.today()
    out_rows, summaries = [], {}
    for t in basket:
        tk = yf.Ticker(t)
        try:
            ed = tk.earnings_dates
        except Exception as e:
            print(f"{t}: earnings_dates FAILED ({e.__class__.__name__}) — name skipped, NOT faked")
            continue
        if ed is None or ed.empty:
            print(f"{t}: no earnings dates returned — name skipped, NOT faked")
            continue
        past = [ts for ts in ed.index if ts.date() < today]
        past = sorted(past, reverse=True)[:N_PRINTS]
        hist = tk.history(start="2024-01-01", auto_adjust=True)
        if hist.empty:
            print(f"{t}: no price history — name skipped")
            continue
        hist.index = [d.date() for d in hist.index]
        days = sorted(hist.index)
        moves = []
        for ts in sorted(past):
            when, how = reaction_day(ts, t)
            d = ts.date()
            after = [x for x in days if x > d]
            onafter = [x for x in days if x >= d]
            if when == "next":
                rd = after[0] if after else None
            else:
                rd = onafter[0] if onafter else None
            if rd is None:
                out_rows.append((t, d, "?", how, None, "no reaction session in history"))
                continue
            prevs = [x for x in days if x < rd]
            if not prevs:
                out_rows.append((t, d, rd, how, None, "no prior session"))
                continue
            mv = (hist.loc[rd, "Close"] / hist.loc[prevs[-1], "Close"] - 1) * 100
            moves.append(mv)
            out_rows.append((t, d, rd, how, mv, ""))
        if moves:
            absm = sorted(abs(m) for m in moves)
            summaries[t] = {
                "n": len(moves),
                "mean_abs": sum(absm) / len(absm),
                "median_abs": absm[len(absm) // 2] if len(absm) % 2 else (absm[len(absm)//2 - 1] + absm[len(absm)//2]) / 2,
                "max_abs": max(absm),
                "worst_down": min(moves),
                "n_down": sum(1 for m in moves if m < 0),
            }

    print(f"PART B — realized 1-day post-earnings moves (close-to-close), run {today.isoformat()}")
    print(f"basket: {', '.join(basket)}  (default basket = rule #18's measured regional-bank four)")
    print(f"{'name':<6}{'print':<12}{'reaction':<12}{'attrib':<10}{'move%':>8}  note")
    for t, d, rd, how, mv, note in out_rows:
        mvs = f"{mv:+.2f}" if mv is not None else "  n/a"
        print(f"{t:<6}{str(d):<12}{str(rd):<12}{how:<10}{mvs:>8}  {note}")
    print()
    print(f"{'name':<6}{'n':>3}{'mean|mv|':>10}{'med|mv|':>9}{'max|mv|':>9}{'worst dn':>10}{'#down':>7}   book needed")
    for t, s in summaries.items():
        need = BOOK_DEPTH.get(t)
        needs = f"{need:.1f}% OTM" if need else "-"
        print(f"{t:<6}{s['n']:>3}{s['mean_abs']:>9.2f}%{s['median_abs']:>8.2f}%{s['max_abs']:>8.2f}%{s['worst_down']:>9.2f}%{s['n_down']:>7}   {needs}")
    return 0


if __name__ == "__main__":
    _ensure_deps_or_reexec()
    args = [a.upper() for a in sys.argv[1:] if not a.startswith("-")]
    raise SystemExit(run(args or None))
