#!/usr/bin/env python3
"""ORACLE — T6 pin ledger for Kalshi KXFED-26SEP-T3.75.

WHY THIS EXISTS
  T6 (co-owned LIQUID/BOND, Will-ruled Option C) grades on the NAMED PLATFORM's
  value, and LIQUID's adopted qualifier reads: "the named platform prints below
  its value 5 trading sessions prior."  That makes a per-session pin ledger
  load-bearing, and it makes a SILENTLY-MISSING day worse than no pin at all
  (BOND 2026-08-21: "a daily pin without gap-marking is WORSE than no pin").

  So this tool never leaves a prior value standing.  Every calendar day in the
  window gets a row; a day with no exchange data gets an explicit NO-PULL row.

SOURCE OF TRUTH
  Kalshi candlesticks: /series/KXFED/markets/KXFED-26SEP-T3.75/candlesticks
  (period_interval=1440).  This is the exchange's own daily record, so a day
  ORACLE was dark is still recoverable AS REAL DATA rather than as a gap.

  ⚠️ DAY ALIGNMENT — the one thing that will bite you.  `end_period_ts` is the
  END of the candle's period, i.e. local midnight AFTER the session it covers.
  The candle stamped 2026-08-28T00:00 is the 2026-08-27 session.  Therefore
  trading_day = date(end_period_ts) - 1 day.  Verified against two independent
  anchors before this file was written:
    - session 8/18 close 0.30  ==  ORACLE's own 8/18 live pin of 30.0% (SCRATCH)
    - session 8/27 close 0.32  ==  today's live `kalshi.py pull` of 32.0%,
      and the candle's OI 230,891 matches the live pull's OI exactly.
  If you ever re-point this at another market, RE-VERIFY the shift; do not
  assume it.

"TRADING SESSIONS"
  Kalshi trades weekends, but BOND's ruled 5-session count for T6 is weekdays
  (8/28 -> 8/27 . 8/26 . 8/25 . 8/24 . 8/21).  Weekend rows are therefore
  emitted as DATA but flagged is_session=N so they never enter the count.
  Labor Day 9/7 is outside this window; no market holiday falls inside it.

Usage:  python3 tools/t6_pin.py [--write]
"""
import os, sys, argparse, datetime, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ORACLE_DIR = os.path.dirname(HERE)
LEDGER = os.path.join(ORACLE_DIR, "workbook", "T6_PIN.tsv")

TICKER = "KXFED-26SEP-T3.75"
SERIES = "KXFED"
WIN_START = datetime.date(2026, 8, 21)   # T6 pin window day 1 (BOND: 5-sessions-prior ref for the 8/28 fire path)
WIN_END   = datetime.date(2026, 8, 28)   # Will Option C: last gradeable data
TRIGGER   = 0.25                          # T6 fires below this

_spec = importlib.util.spec_from_file_location("k", os.path.join(ORACLE_DIR, "scripts", "kalshi.py"))
k = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(k)

COLS = ["trading_day", "dow", "is_session", "yes_close", "yes_bid_close", "yes_ask_close",
        "volume", "open_interest", "source", "capture_ts", "note"]


def f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def fetch():
    """trading_day -> candle dict. Pads the window so the 5-session lookback resolves."""
    start = int(datetime.datetime.combine(WIN_START - datetime.timedelta(days=12), datetime.time()).timestamp())
    end   = int(datetime.datetime.combine(WIN_END + datetime.timedelta(days=1), datetime.time()).timestamp())
    r = k._get(f"/series/{SERIES}/markets/{TICKER}/candlesticks",
               params={"start_ts": start, "end_ts": end, "period_interval": 1440})
    out = {}
    for c in r.get("candlesticks", []):
        # see DAY ALIGNMENT above: end_period_ts is midnight AFTER the session
        day = datetime.datetime.fromtimestamp(c["end_period_ts"]).date() - datetime.timedelta(days=1)
        p = c.get("price") or {}
        if f(p.get("close_dollars")) is None:
            continue
        out[day] = c
    return out


def rows(candles, today):
    yb_of = lambda c, key: f((c.get(key) or {}).get("close_dollars"))
    stamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    out = []
    d = WIN_START
    while d <= WIN_END:
        is_sess = "Y" if d.weekday() < 5 else "N"
        c = candles.get(d)
        if c is None:
            # NEVER let the prior value stand -- BOND/LIQUID mandatory gap-marking
            note = "NO EXCHANGE DATA for this session" if d <= today else "future session, not yet reachable"
            src = "NO-PULL" if d <= today else "PENDING"
            out.append([d.isoformat(), d.strftime("%a"), is_sess, "NA", "NA", "NA", "NA", "NA",
                        src, stamp, note])
        else:
            p = c["price"]
            partial = (d == today)
            out.append([
                d.isoformat(), d.strftime("%a"), is_sess,
                f"{f(p['close_dollars']):.2f}",
                f"{yb_of(c,'yes_bid'):.2f}" if yb_of(c,'yes_bid') is not None else "NA",
                f"{yb_of(c,'yes_ask'):.2f}" if yb_of(c,'yes_ask') is not None else "NA",
                f"{f(c.get('volume_fp')):.0f}" if f(c.get('volume_fp')) is not None else "NA",
                f"{f(c.get('open_interest_fp')):.0f}" if f(c.get('open_interest_fp')) is not None else "NA",
                "LIVE-INTRADAY" if partial else "CANDLE-CLOSE",
                stamp,
                "session in progress at capture; not a settled close" if partial
                else "exchange daily close, backfilled" ,
            ])
        d += datetime.timedelta(days=1)
    return out


def lookback_ref(candles, day, n=5):
    """Value n trading sessions (weekdays) prior to `day`, per BOND's ruled count."""
    seen, d = [], day - datetime.timedelta(days=1)
    while len(seen) < n and d > WIN_START - datetime.timedelta(days=30):
        if d.weekday() < 5:
            seen.append(d)
        d -= datetime.timedelta(days=1)
    if len(seen) < n:
        return None, None
    ref = seen[-1]
    c = candles.get(ref)
    return ref, (f(c["price"]["close_dollars"]) if c else None)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true", help="rewrite workbook/T6_PIN.tsv")
    a = ap.parse_args()

    today = datetime.date.today()
    candles = fetch()
    rs = rows(candles, today)

    print(f"T6 PIN LEDGER — Kalshi {TICKER}  (trigger: fires BELOW {TRIGGER:.0%})")
    print(f"window {WIN_START} .. {WIN_END}   generated {datetime.datetime.now():%Y-%m-%d %H:%M:%S %Z}")
    print("-" * 104)
    print(f"{'day':<12}{'dow':<5}{'sess':<6}{'close':>7}{'bid':>6}{'ask':>6}{'volume':>10}{'OI':>10}  {'source':<15}note")
    for r in rs:
        print(f"{r[0]:<12}{r[1]:<5}{r[2]:<6}{r[3]:>7}{r[4]:>6}{r[5]:>6}{r[6]:>10}{r[7]:>10}  {r[8]:<15}{r[10]}")

    gaps = [r for r in rs if r[8] == "NO-PULL"]
    print("-" * 104)
    print(f"MARKED GAPS: {len(gaps)}" + ("" if not gaps else "  -> " + ", ".join(g[0] for g in gaps)))

    # current state vs T6's two legs
    cur = candles.get(today)
    if cur:
        val = f(cur["price"]["close_dollars"])
        ref_day, ref_val = lookback_ref(candles, today)
        print(f"\nLEG 1 (level):    {val:.0%} vs trigger <{TRIGGER:.0%}  ->  "
              f"{'FIRED' if val < TRIGGER else 'NOT FIRED'} ({(val-TRIGGER)*100:+.1f}pp from line)")
        if ref_val is not None:
            print(f"LEG 2 (5-session): {val:.0%} vs {ref_val:.0%} [{ref_day} = 5 sessions prior]  ->  "
                  f"{'BELOW' if val < ref_val else 'NOT BELOW'} ({(val-ref_val)*100:+.1f}pp)")
        # the reference the 8/28 fire path will read
        r28, v28 = lookback_ref(candles, WIN_END)
        if v28 is not None:
            print(f"\n8/28 fire path will read 5-sessions-prior = {r28} close {v28:.0%} "
                  f"(NOT the 0.35 intraday high captured 8/21 11:14 EDT)")

    if a.write:
        with open(LEDGER, "w") as fh:
            fh.write("\t".join(COLS) + "\n")
            for r in rs:
                fh.write("\t".join(r) + "\n")
        print(f"\nwrote {len(rs)} rows -> {LEDGER}")


if __name__ == "__main__":
    main()
