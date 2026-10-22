#!/usr/bin/env python3
"""
Event-window stock reactions + since-date/drawdown table. Built 2026-10-22
(Will-greenlit) from REQ-008 (cyber-wave equity windows) and the bank-vendor
study (vendor drawdowns). Needs yfinance (in the venv): run with .venv/bin/python.

Usage:
  # returns around an event: base = last close BEFORE d0; d0 = first session on/after the date
  .venv/bin/python scripts/event_window.py window --date 2024-07-19 CRWD MSFT KBE
  .venv/bin/python scripts/event_window.py window --date 2020-12-14 HACK --offsets 0,5,20,60 --bench ^GSPC

  # performance since a date + YTD + distance from 2-year peak + worst days
  .venv/bin/python scripts/event_window.py since --date 2026-10-20 FISV FIS JKHY KRE

Method: adjusted closes; "vs bench" = stock return minus benchmark return over the
same offset (simple market adjustment, NOT a regression abnormal return).

CAVEATS (state them in any report that uses the output):
  - One event per row: confounded by whatever else happened (earnings, rallies).
  - A bar dated TODAY before the close is INTRADAY, not a close — label it.
  - Delisted names (e.g. SWI, FEYE) return no data: cite a dated secondary for them.
  - Tickers change (Fiserv: FI -> FISV on Nasdaq, ~11 Nov 2025): "NO DATA" may be a rename.
"""
import argparse, datetime, sys, warnings
warnings.filterwarnings("ignore")
try:
    import pandas as pd
    import yfinance as yf
except ImportError:
    sys.exit("needs yfinance + pandas: run with /home/willi/Research-workspace/.venv/bin/python")


def closes(t, start, end):
    h = yf.Ticker(t).history(start=start, end=end, auto_adjust=True)["Close"]
    if not h.empty:
        h.index = h.index.tz_localize(None).normalize()
    return h


def window(t, d0, offsets, span):
    d = pd.Timestamp(d0)
    h = closes(t, d - pd.Timedelta(days=20), d + pd.Timedelta(days=span))
    if h.empty:
        return None
    pre, post = h[h.index < d], h[h.index >= d]
    if pre.empty or post.empty:
        return None
    b = pre.iloc[-1]
    r = {"base": (pre.index[-1].date(), b), "d0": post.index[0].date(), "last": post.index[-1].date()}
    r["ret"] = {n: (post.iloc[n] / b - 1) * 100 if len(post) > n else None for n in offsets}
    r["low20"] = (post.iloc[:20].min() / b - 1) * 100
    r["high20"] = (post.iloc[:20].max() / b - 1) * 100
    return r


def fmt(x):
    return "   n/a" if x is None else f"{x:+6.1f}%"


def cmd_window(a):
    offs = [int(x) for x in a.offsets.split(",")]
    span = int(max(offs) * 1.6) + 15
    bench = window(a.bench, a.date, offs, span)
    print(f"event date {a.date} · base = last close before d0 · offsets in trading days · bench {a.bench}")
    print(f"{'ticker':10s} {'d0':10s} " + " ".join(f"{'+'+str(o):>7s}" for o in offs) + f" {'20d low':>8s} {'20d high':>8s}  vs bench at each offset (pp)")
    for t in a.tickers + [a.bench]:
        r = window(t, a.date, offs, span)
        if not r:
            print(f"{t:10s} NO DATA (delisted / renamed / no window)"); continue
        vs = ""
        if bench and t != a.bench:
            vs = " ".join("  n/a" if r["ret"][o] is None or bench["ret"][o] is None else f"{r['ret'][o]-bench['ret'][o]:+5.1f}" for o in offs)
        print(f"{t:10s} {str(r['d0']):10s} " + " ".join(fmt(r["ret"][o]) for o in offs) + f" {fmt(r['low20']):>8s} {fmt(r['high20']):>8s}  {vs}")
        if r["last"] >= datetime.date.today():
            print(f"{'':10s} ⚠ last bar {r['last']} is today — intraday if read before the close")


def cmd_since(a):
    d = pd.Timestamp(a.date)
    print(f"since {a.date} close · YTD from first 2026 session · peak = 2-year max close")
    for t in a.tickers:
        h = closes(t, pd.Timestamp.today() - pd.Timedelta(days=740), pd.Timestamp.today() + pd.Timedelta(days=1))
        if h.empty:
            print(f"{t:8s} NO DATA (delisted / renamed?)"); continue
        last = h.iloc[-1]
        base = h[h.index <= d]
        ytd = h[h.index >= pd.Timestamp(f"{pd.Timestamp.today().year}-01-01")]
        worst = h.pct_change().nsmallest(2)
        print(f"{t:8s} last {h.index[-1].date()} {last:10.2f} | since {a.date} {fmt((last/base.iloc[-1]-1)*100 if not base.empty else None)}"
              f" | YTD {fmt((last/ytd.iloc[0]-1)*100 if not ytd.empty else None)} | peak {h.idxmax().date()} {fmt((last/h.max()-1)*100)}"
              f" | worst days " + ", ".join(f"{i.date()} {v*100:+.1f}%" for i, v in worst.items()))
        if h.index[-1].date() >= datetime.date.today():
            print(f"{'':8s} ⚠ last bar is today — intraday if read before the close")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    sub = ap.add_subparsers(dest="cmd", required=True)
    w = sub.add_parser("window"); w.add_argument("--date", required=True); w.add_argument("tickers", nargs="+")
    w.add_argument("--offsets", default="0,5,20,60"); w.add_argument("--bench", default="^GSPC")
    s = sub.add_parser("since"); s.add_argument("--date", required=True); s.add_argument("tickers", nargs="+")
    a = ap.parse_args()
    cmd_window(a) if a.cmd == "window" else cmd_since(a)


if __name__ == "__main__":
    main()
