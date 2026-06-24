#!/usr/bin/env python3
"""
csv_pnl.py — reconstruct realized P&L and behavioral cuts from a Robinhood
account-activity CSV export (the "best-acceptable" day-trading intake).

Usage:
    python3 AGENTS/TERRY/scripts/csv_pnl.py <activity.csv> [--review YYYY-MM-DD]

What it does (cash-flow / thread method):
  * Groups every fill into a position thread (one per option contract, or per
    stock symbol). Option key = TICKER + expiry + Put/Call + strike.
  * Nets cash per thread. A thread is CLOSED if it has an expiration (OEXP) row
    OR nets to zero contracts; otherwise it's OPEN at the review date.
  * Realized P&L = sum of net cash over closed threads. Expired-worthless longs
    are realized LOSSES (premium fully paid, nothing returned) and are counted.

Hard lessons baked in (Session 2, 2026-06-24):
  * The "1S"/"2S" quantity tag on OEXP rows is Robinhood notation, NOT a short
    marker. Do not infer shorts from it. A real short requires an STO code.
  * This CSV contains only SETTLED activity — it has NO canceled orders, so a
    cancel-rate / churn figure cannot be computed from it. Says UNKNOWN.

It does NOT fetch live marks; open threads are reported at cost basis for Will
to mark (or feed a positions/marks export).
"""
import csv, re, sys, argparse
from collections import defaultdict
from datetime import datetime


def money(s):
    s = s.strip()
    if not s:
        return 0.0
    neg = s.startswith("(")
    s = s.replace("(", "").replace(")", "").replace("$", "").replace(",", "")
    if s == "":
        return 0.0
    return -float(s) if neg else float(s)


OPT_RE = re.compile(r"([A-Z]+)\s+(\d+/\d+/\d{4})\s+(Put|Call)\s+\$([\d.]+)")


def load(path):
    trades, deposits, fees = [], 0.0, 0.0
    with open(path, newline="") as f:
        r = csv.reader(f)
        next(r)
        for row in r:
            if len(row) < 9 or not row[0].strip() or not row[5].strip():
                continue
            act, _, _, inst, desc, code, qty, _, amount = row[:9]
            amt = money(amount)
            if code == "ACH":
                deposits += amt
                continue
            if code in ("GOLD", "FUTSWP"):
                fees += amt
                continue
            m = re.match(r"(\d+)", qty.strip())
            trades.append(dict(
                date=datetime.strptime(act, "%m/%d/%Y"),
                inst=inst, desc=desc.replace("\n", " ").strip(),
                code=code, nq=int(m.group(1)) if m else 0, amt=amt))
    return trades, deposits, fees


def thread_key(t):
    m = OPT_RE.search(t["desc"].replace("Option Expiration for ", ""))
    if m:
        return ("OPT",) + m.groups()
    return ("STK", t["inst"])


def label(k):
    return f"{k[1]} {k[2]} {k[3]} ${k[4]}" if k[0] == "OPT" else f"{k[1]} stock"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--review", default=None, help="review date YYYY-MM-DD (default: latest fill)")
    a = ap.parse_args()

    trades, deposits, fees = load(a.csv)
    if not trades:
        print("No trades parsed.")
        return 1
    review = datetime.strptime(a.review, "%Y-%m-%d") if a.review else max(t["date"] for t in trades)

    threads = defaultdict(list)
    for t in trades:
        threads[thread_key(t)].append(t)

    realized = 0.0
    closed, openp, expired = [], [], []
    sto_count = sum(1 for t in trades if t["code"] in ("STO", "Sell To Open"))
    for k, ts in threads.items():
        net = sum(t["amt"] for t in ts)
        has_exp = any(t["code"] == "OEXP" for t in ts)
        pos = 0
        for t in ts:
            if t["code"] in ("BTO", "Buy", "BTC"):
                pos += t["nq"]
            elif t["code"] in ("STC", "Sell", "STO"):
                pos -= t["nq"]
        if has_exp:
            pos = 0
        exp_date = datetime.strptime(k[2], "%m/%d/%Y") if k[0] == "OPT" else None
        is_open = pos != 0 and (exp_date is None or exp_date > review)
        rec = dict(k=k, net=net, pos=pos, has_exp=has_exp)
        if is_open:
            openp.append(rec)
        else:
            closed.append(rec)
            realized += net
            if has_exp and net < 0:
                expired.append(rec)

    days = len({t["date"] for t in trades})
    fills = sum(1 for t in trades if t["code"] in ("BTO", "STC", "STO", "BTC", "Buy", "Sell"))
    put_pnl = sum(r["net"] for r in closed if r["k"][0] == "OPT" and r["k"][3] == "Put")
    call_pnl = sum(r["net"] for r in closed if r["k"][0] == "OPT" and r["k"][3] == "Call")

    print(f"Review date: {review:%Y-%m-%d} | {days} trading days | {fills} fills | {len(threads)} threads")
    print(f"Sell-to-open (STO) codes: {sto_count}  ->  {'SHORTS PRESENT' if sto_count else 'all long, realized is firm'}")
    print(f"\nREALIZED (closed threads): {realized:+.2f}")
    print(f"  expired-worthless drag:  {sum(r['net'] for r in expired):+.2f} over {len(expired)} threads")
    print(f"  long puts:  {put_pnl:+.2f}   long calls: {call_pnl:+.2f}")
    print(f"  deposits {deposits:+.2f}  fees {fees:+.2f}")
    print(f"  cancel-rate: UNKNOWN (settled-activity CSV has no canceled orders)")

    print("\nExpired-worthless (held to $0):")
    for r in sorted(expired, key=lambda x: x["net"]):
        print(f"  {r['net']:+9.2f}  {label(r['k'])}")

    print(f"\nOPEN at {review:%Y-%m-%d} (cost basis — needs live/Will marks):")
    for r in sorted(openp, key=lambda x: x["net"]):
        print(f"  {r['net']:+9.2f}  pos {r['pos']:+d}  {label(r['k'])}")
    print(f"  total open cost: {sum(r['net'] for r in openp):+.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
