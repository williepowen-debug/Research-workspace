#!/usr/bin/env python3
"""Settled daily closes only — the one filter every REGINALD settled-close grade goes through.

A yfinance daily bar for TODAY (US/Eastern) is never a settled close: during the session it
carries the in-progress last trade (10/9 10:26 ET: FLG 'close' $11.25, counted below RED), and
hours after the bell it can still read Close=NaN with partial volume (10/9 20:3x ET). Both
are excluded here, as is any NaN bar on an earlier date. Excluded bars are returned so the
caller prints them as NOT GRADED instead of dropping them silently.

Usage (repo root):
  .venv/bin/python3 AGENTS/REGINALD/scripts/settled_bars.py WAL [--days 10]   # + Nasdaq cross-check
  .venv/bin/python3 AGENTS/REGINALD/scripts/settled_bars.py --selftest
Exit (CLI): 0 = closes printed and both routes agree on every shared date ·
            2 = a route failed or the routes disagree — grade nothing from this run.
"""
import json
import math
import sys
import urllib.request
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")


def settled_closes(closes, now=None):
    """closes: pandas Series (DatetimeIndex) of daily Close -> (settled Series, [(date, reason)])."""
    today = (now or datetime.now(ET)).date()
    excluded, keep = [], []
    for ts, v in closes.items():
        d = ts.date()
        if d >= today:
            excluded.append((d, f"today's bar ({'NaN' if v != v else f'{float(v):.2f}'}) — not settled"))
            keep.append(False)
        elif v is None or (isinstance(v, float) and math.isnan(v)) or v != v:
            excluded.append((d, "Close is NaN — incomplete bar"))
            keep.append(False)
        else:
            keep.append(True)
    return closes[keep], excluded


def yf_closes(ticker, start):
    import yfinance as yf
    return yf.Ticker(ticker).history(start=start, auto_adjust=False)["Close"]


def nasdaq_closes(ticker, start, end):
    """Second, independent route -> {date: close}. Raises on failure."""
    out = {}
    for cls in ("stocks", "etf"):
        url = (f"https://api.nasdaq.com/api/quote/{ticker}/historical?assetclass={cls}"
               f"&fromdate={start}&todate={end}&limit=60")
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"})
        d = json.load(urllib.request.urlopen(req, timeout=25))
        rows = ((d.get("data") or {}).get("tradesTable") or {}).get("rows") or []
        for r in rows:
            out[datetime.strptime(r["date"], "%m/%d/%Y").date()] = float(r["close"].replace("$", "").replace(",", ""))
        if out:
            return out
    return out


def selftest():
    import pandas as pd
    now = datetime(2026, 10, 9, 20, 30, tzinfo=ET)
    idx = pd.to_datetime(["2026-10-07", "2026-10-08", "2026-10-09"])
    cases = [
        ("evening: today's bar NaN -> excluded", pd.Series([11.30, 11.35, float("nan")], index=idx), [11.30, 11.35], 1),
        ("intraday: today's bar has a value -> still excluded", pd.Series([11.30, 11.35, 11.25], index=idx), [11.30, 11.35], 1),
        ("earlier NaN bar -> excluded", pd.Series([11.30, float("nan"), 11.25], index=idx), [11.30], 2),
        ("all settled -> nothing excluded", pd.Series([11.30, 11.35], index=idx[:2]), [11.30, 11.35], 0),
    ]
    fails = 0
    for name, s, want_vals, want_excl in cases:
        got, excl = settled_closes(s, now)
        ok = [round(float(v), 2) for v in got] == want_vals and len(excl) == want_excl
        fails += not ok
        print(f"  {'PASS' if ok else 'FAIL'}  kept {len(got)} excluded {len(excl)}  {name}")
    print(f"SETTLED-BARS SELFTEST {'PASS' if not fails else 'FAIL'}: {len(cases) - fails}/{len(cases)}")
    return 1 if fails else 0


def main():
    if "--selftest" in sys.argv:
        return selftest()
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        return 2
    ticker = args[0].upper()
    days = int(sys.argv[sys.argv.index("--days") + 1]) if "--days" in sys.argv else 10
    start = (datetime.now(ET).date() - timedelta(days=days + 7)).isoformat()
    try:
        s, excl = settled_closes(yf_closes(ticker, start))
    except Exception as e:  # noqa: BLE001
        print(f"SETTLED 2 {ticker}: yfinance route failed ({type(e).__name__}: {e}) — grade nothing")
        return 2
    try:
        nq = nasdaq_closes(ticker, start, datetime.now(ET).date().isoformat())
    except Exception as e:  # noqa: BLE001
        nq, nq_err = {}, f"{type(e).__name__}: {e}"
    else:
        nq_err = None if nq else "no rows returned"
    rc = 0
    print(f"{ticker} settled closes (yfinance daily bars, NaN + today's bar excluded) vs Nasdaq historical:")
    for ts, v in s.tail(days).items():
        d = ts.date()
        other = nq.get(d)
        agree = "—" if other is None else ("agree" if abs(other - float(v)) < 0.005 else f"DISAGREE ({other:.2f})")
        if other is not None and agree != "agree":
            rc = 2
        print(f"  {d}  {float(v):.2f}   nasdaq {other if other is not None else 'n/a':>8}   {agree}")
    for d, why in excl:
        print(f"  {d}  NOT GRADED — {why}")
    if nq_err:
        print(f"  ⚠️  second route unavailable ({nq_err}) — single-route closes; label them so in any grade")
        rc = 2
    return rc


if __name__ == "__main__":
    sys.exit(main())
