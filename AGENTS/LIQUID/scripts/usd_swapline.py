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
    fires, d = [], dt.date(2014, 1, 6)
    while d <= dt.date.today():
        w = [o for o in allops if d <= dt.date.fromisoformat(o["trade"]) < d + dt.timedelta(7)]
        if cadence_switch(w):
            fires.append(d)
        d += dt.timedelta(7)
    eps = [f for k, f in enumerate(fires) if k == 0 or (f - fires[k - 1]).days > 21]
    print(f"cadence leg (ORANGE-PROPOSED, HANS's): {len(fires)} weeks, episode starts {[str(e) for e in eps]}")
    for a, b, lab in (("2020-03-01", "2020-04-30", "control 2020-03"), ("2022-09-15", "2022-11-15", "control 2022-09/10"),
                      ("2023-03-08", "2023-04-30", "control 2023-03")):
        w = [o for o in allops if o["cp"] in EU and a <= o["trade"] <= b]
        m = max(w, key=lambda o: o["bn"]) if w else None
        print(f"{lab}: max EU op " + (f"${m['bn']:.2f}B {m['cp']} {m['trade']} -> {grade(m)}" if m else "none"))


def cadence_switch(oplist):
    """HANS's leg (2023-03 tell): a European CB moving to DAILY or very short USD ops.
    True if one European counterparty trades on >= 3 distinct dates inside any
    7-calendar-day span. A single short op does NOT count: replay 2014-2026 showed
    isolated 1-day ops (mostly BoE, ~annual, small test operations) firing in 11 calm
    episodes. With the date-count rule alone the replay fires on exactly 2020-03-23 and
    2023-03-20 (see --baserate). Returns the evidence list."""
    ev = []
    for cp in EU:
        ds = sorted({dt.date.fromisoformat(o["trade"]) for o in oplist if o["cp"] == cp})
        for k in range(len(ds) - 2):
            if (ds[k + 2] - ds[k]).days <= 6:
                ev.append(f"{cp[:3]} traded {ds[k]}, {ds[k + 1]}, {ds[k + 2]} (>=3 dates in 7d)")
                break
    return ev


def verdict(oplist, swpt_rows, today):
    """One overall line. Fails closed on missing/stale inputs."""
    if not oplist:
        return "UNGRADEABLE: NY Fed returned 0 operations in the window (ECB normally trades weekly)"
    if not swpt_rows:
        return "UNGRADEABLE: SWPT returned no rows"
    last_sw_date, last_sw = swpt_rows[-1]
    stale = (today - dt.date.fromisoformat(last_sw_date)).days > 13
    recent = [o for o in oplist if o["cp"] in EU and (today - dt.date.fromisoformat(o["trade"])).days <= 14]
    grades = [grade(o) for o in recent]
    cad = cadence_switch([o for o in oplist if (today - dt.date.fromisoformat(o["trade"])).days <= 14])
    if "ALERT-PROPOSED" in grades or last_sw >= SWPT_ALERT_M:
        v = "ALERT-PROPOSED"
    elif cad:
        v = "ORANGE-PROPOSED (cadence switch: " + "; ".join(cad[:3]) + ")"
    elif "WATCH-PROPOSED" in grades:
        v = "WATCH-PROPOSED"
    else:
        v = "quiet (ceiling not binding; NOT 'no dollar strain')"
    if stale:
        v += f" ⚠️ SWPT STALE (as-of {last_sw_date})"
    return v


def selftest():
    fails = 0
    def chk(label, got, want):
        nonlocal fails
        ok = got == want
        fails += (not ok)
        print(f"{'PASS' if ok else 'FAIL'}  {label}: got {got!r} want {want!r}")
    mk = lambda trade, mat, cp, bn, term: dict(trade=trade, settle=trade, mat=mat, cp=cp, bn=bn, rate=None, term=term)
    # grade(): controls and boundaries
    chk("2020-03-18 ECB 84d $75.8B spans QE but long -> ALERT", grade(mk("2020-03-18", "2020-06-11", "European Central Bank", 75.82, 84)), "ALERT-PROPOSED")
    chk("2022-10-19 SNB 7d $11.09B -> ALERT", grade(mk("2022-10-19", "2022-10-27", "Swiss National Bank", 11.09, 7)), "ALERT-PROPOSED")
    chk("2026-09-23 ECB 7d $0.197B matures 10/1 -> turn", grade(mk("2026-09-23", "2026-10-01", "European Central Bank", 0.197, 7)).startswith("turn op"), True)
    chk("2017-12-20 ECB 21d $11.9B year-end -> turn, NOT alert", grade(mk("2017-12-20", "2018-01-10", "European Central Bank", 11.907, 21)).startswith("turn op"), True)
    chk("mid-month ECB 7d $1.0B (tie) -> WATCH", grade(mk("2026-10-14", "2026-10-21", "European Central Bank", 1.0, 7)), "WATCH-PROPOSED")
    chk("mid-month ECB 7d $0.999B -> quiet", grade(mk("2026-10-14", "2026-10-21", "European Central Bank", 0.999, 7)), "quiet")
    chk("mid-month BoE 7d $5.0B (tie) -> ALERT", grade(mk("2026-10-14", "2026-10-21", "Bank of England", 5.0, 7)), "ALERT-PROPOSED")
    chk("BoJ $10B -> not European", grade(mk("2026-10-14", "2026-10-21", "Bank of Japan", 10.0, 7)), "n/a (not European)")
    chk("ECB 28d $2B spanning QE (term > 21) -> WATCH", grade(mk("2026-09-16", "2026-10-14", "European Central Bank", 2.0, 28)), "WATCH-PROPOSED")
    chk("op maturing ON quarter-end day does not span it", spans_qe("2026-09-23", "2026-09-30"), False)
    chk("op settling over quarter-end spans it", spans_qe("2026-09-30", "2026-10-07"), True)
    # cadence leg
    daily = [mk(f"2023-03-{d:02d}", f"2023-03-{d+1:02d}", "European Central Bank", 0.1, 1) for d in (20, 21, 22)]
    chk("daily 1d ECB ops -> cadence switch", bool(cadence_switch(daily)), True)
    chk("single isolated 1d BoE op -> no cadence switch", cadence_switch([mk("2024-05-15", "2024-05-16", "Bank of England", 0.01, 1)]), [])
    weekly = [mk(d, d, "European Central Bank", 0.1, 7) for d in ("2026-09-02", "2026-09-09", "2026-09-16")]
    chk("weekly 7d ECB ops -> no cadence switch", cadence_switch(weekly), [])
    # verdict fails closed
    t = dt.date(2026, 10, 1)
    chk("no ops -> UNGRADEABLE", verdict([], [("2026-09-23", 72.0)], t).startswith("UNGRADEABLE"), True)
    chk("no SWPT -> UNGRADEABLE", verdict(weekly, [], t).startswith("UNGRADEABLE"), True)
    chk("stale SWPT flagged", "STALE" in verdict(weekly, [("2026-09-02", 72.0)], t), True)
    chk("SWPT $10,000M (tie) -> ALERT", verdict(weekly, [("2026-09-23", 10000.0)], t).startswith("ALERT"), True)
    # fetch failure -> main returns 2, never 'quiet'
    global _get
    real = _get
    def boom(*a, **k):
        raise TimeoutError("synthetic")
    _get = boom
    try:
        rc = main(_argv=[])
    finally:
        _get = real
    chk("fetch failure -> main rc 2", rc, 2)
    print(f"selftest: {'OK' if not fails else str(fails) + ' FAIL'}")
    return 1 if fails else 0


def main(_argv=None):
    argv = sys.argv[1:] if _argv is None else _argv
    if "--selftest" in argv:
        return selftest()
    if "--baserate" in argv:
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
    v = verdict(o, s, today)
    print(f"VERDICT (PROPOSED lines): {v}")
    return 2 if v.startswith("UNGRADEABLE") else 0


if __name__ == "__main__":
    sys.exit(main() or 0)
