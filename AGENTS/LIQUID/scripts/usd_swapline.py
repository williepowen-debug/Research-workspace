#!/usr/bin/env python3
"""USD swap-line usage — the reachable read on European stress reaching US dollar funding.

WHY (2026-10-01, PROME touch 4, Will "go for the six"): the EUR/USD cross-currency
basis is UNMEASURED on both LIQUID and HANS (HANS-T-12 has no feed). A quoted basis
LEVEL is not reachable free (see analysis/2026-10-01_eurusd-basis-instrument.md for
the negatives). What IS reachable is USAGE of the Fed's central-bank liquidity swap
lines, which central banks on-lend to their banks at a fixed spread over OIS
(currently 25bp). A bank uses the facility only when funding dollars in the market
(FX swaps, including the basis) costs more than the facility. So usage is a
CEILING-BINDING indicator: it says the basis has reached the backstop for some
borrower. It is not a basis level, and it is silent below the ceiling.

SOURCES (both free, both pulled here; fail closed on any fetch error)
  1. NY Fed Markets API, per operation, by counterparty:
     https://markets.newyorkfed.org/api/fxs/usdollar/search.json?startDate=&endDate=
     Posted at settlement (trade T, settle T+1, ~16:00 ET). The ECB's weekly USD
     operation allotment is the same transaction from the other side.
  2. FRED SWPT (H.4.1 central bank liquidity swaps, $ millions, Wednesday level,
     published Thursday ~16:30 ET).

THRESHOLDS: ⛔ PROPOSED, NOT REGISTERED. Setting a threshold is Will's word. The lines
below are printed as context and labelled PROPOSED on every line. Base rates are in
the analysis file and reproduce with --baserate.
"""
import json, sys, urllib.request, datetime as dt, time, csv, io

EU = ("European Central Bank", "Swiss National Bank", "Bank of England")
WATCH_B = 1.0     # PROPOSED: one European op >= $1.0B, short turn ops excluded
ALERT_B = 5.0     # PROPOSED: one European op >= $5.0B, short turn ops excluded
SWPT_ALERT_M = 10_000  # PROPOSED: SWPT >= $10B ($ millions)
API = "https://markets.newyorkfed.org/api/fxs/usdollar/search.json?startDate={a}&endDate={b}"


def _get(url, timeout=90, tries=3):
    req = urllib.request.Request(url, headers={"User-Agent": "LIQUID usd_swapline.py"})
    for i in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read().decode("utf-8")
        except Exception:
            if i == tries - 1:
                raise
            time.sleep(5)


def spans_qe(trade, maturity):
    """True if the op's term crosses a quarter-end (a turn op, mechanically larger)."""
    t, m = dt.date.fromisoformat(trade), dt.date.fromisoformat(maturity)
    for y in (t.year, t.year + 1):
        for mo, d in ((3, 31), (6, 30), (9, 30), (12, 31)):
            q = dt.date(y, mo, d)
            if t <= q < m:
                return True
    return False


def ops(a, b):
    o = json.loads(_get(API.format(a=a, b=b)))["fxSwaps"]["operations"]
    return [dict(trade=x["tradeDate"], settle=x["settlementDate"], mat=x["maturityDate"],
                 cp=x["counterparty"], bn=x["amount"] / 1e9, rate=x.get("interestRate"),
                 term=x["termInDays"]) for x in o]


TURN_MAX_DAYS = 21  # a short op that spans a quarter-end is a TURN op (mechanical; excluded)


def is_turn(op):
    return op["term"] <= TURN_MAX_DAYS and spans_qe(op["trade"], op["mat"])


def grade(op):
    """Both PROPOSED lines exclude short turn ops (2014-19: all three >=$5B hits were
    turn ops). A long op that spans a quarter-end (e.g. the 84d 2020-03-18 op) still counts."""
    if op["cp"] not in EU:
        return "n/a (not European)"
    if is_turn(op):
        return "turn op (short, spans QE) — excluded"
    if op["bn"] >= ALERT_B:
        return "ALERT-PROPOSED"
    if op["bn"] >= WATCH_B:
        return "WATCH-PROPOSED"
    return "quiet"


def swpt(a):
    """SWPT via the standing FORGE fetch.py FRED API path (KB-LIQ-139: the API is not
    CDN-cached). NOT via fredgraph.csv with urllib: on 2026-10-01 FRED tarpitted a
    request carrying this script's User-Agent (read timeout) while curl's UA returned
    in 0.4s and the NY Fed API answered in 0.1s — a reachability failure about the
    REQUEST, not the data."""
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "FORGE" / "tools" / "market-data"))
    from fetch import fred_fetch
    rows = fred_fetch("SWPT", limit=20)
    if not rows or isinstance(rows, dict):
        raise RuntimeError(f"SWPT fetch returned no rows: {rows!r}"[:200])
    out = [(r["date"], float(r["value"])) for r in rows if r.get("value") not in (".", "", None) and r["date"] >= a]
    return sorted(out)


def baserate():
    allops = []
    for y in range(2014, dt.date.today().year + 1):
        allops += ops(f"{y}-01-01", f"{y}-12-31")
    for a, b, lab in (("2014-01-01", "2019-12-31", "2014-19"), ("2021-07-01", "2099-12-31", "2021H2-now")):
        w = [o for o in allops if o["cp"] in EU and a <= o["trade"] <= b]
        nonqe = [o for o in w if not is_turn(o)]
        wt = [o for o in nonqe if WATCH_B <= o["bn"] < ALERT_B]
        al = [o for o in nonqe if o["bn"] >= ALERT_B]
        print(f"{lab}: EU ops {len(w)} (non-turn {len(nonqe)}) | WATCH-PROPOSED hits {len(wt)}: {[(o['trade'], o['cp'][:3], round(o['bn'], 2)) for o in wt][:8]} | "
              f"ALERT-PROPOSED hits {len(al)}: {[(o['trade'], o['cp'][:3], round(o['bn'], 2)) for o in al][:6]}")
    for a, b, lab in (("2020-03-01", "2020-04-30", "control 2020-03"), ("2022-09-15", "2022-11-15", "control 2022-09/10"),
                      ("2023-03-08", "2023-04-30", "control 2023-03")):
        w = [o for o in allops if o["cp"] in EU and a <= o["trade"] <= b]
        m = max(w, key=lambda o: o["bn"]) if w else None
        print(f"{lab}: max EU op " + (f"${m['bn']:.2f}B {m['cp']} {m['trade']} -> {grade(m)}" if m else "none"))


def main():
    if "--baserate" in sys.argv:
        return baserate()
    today = dt.date.today()
    try:
        o = ops(str(today - dt.timedelta(days=60)), str(today))
        s = swpt(str(today - dt.timedelta(days=120)))
    except Exception as e:  # fail closed: never print a quiet reading off a failed pull
        print(f"UNGRADEABLE: fetch failed ({e.__class__.__name__}: {e}) — no reading")
        return 2
    print("⛔ Lines are PROPOSED, NOT REGISTERED (Will's word). Usage = ceiling-binding, not a basis level.")
    print(f"NY Fed USD swap operations, last 60 days ({len(o)} ops; posted at settlement):")
    for x in sorted(o, key=lambda x: x["trade"])[-12:]:
        print(f"  trade {x['trade']} settle {x['settle']} {x['term']:>3}d {x['cp'][:24]:<24} ${x['bn']:.3f}B @ {x['rate']}%  -> {grade(x)}")
    if s:
        d, v = s[-1]
        lab = "ALERT-PROPOSED" if v >= SWPT_ALERT_M else "quiet"
        print(f"FRED SWPT (H.4.1, Wed level): ${v:,.0f}M as-of {d} -> {lab}; prior: " +
              ", ".join(f"{dd[5:]} {vv:,.0f}" for dd, vv in s[-5:-1]))
    return 0


if __name__ == "__main__":
    sys.exit(main() or 0)
