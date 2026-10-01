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
WATCH_B = 1.0     # PROPOSED: one European NON-turn op >= $1.0B
ALERT_B = 5.0     # PROPOSED: one European NON-turn op >= $5.0B
# Turn ops are NEVER dropped (independent read 2026-10-01 ❌#12: an unbounded exclusion hid
# ECB $17.27B and BoE $7.71B on 2020-03-25). They grade on their own higher lines, fitted
# in-sample: calm 2010-2026 turn-op max $11.91B (ECB 2017-12-20); stress 2020-03-25 $17.27B,
# 2011-12-21 $33.0B. LIQUID post-read change, NOT yet seen by HANS.
TURN_WATCH_B = 5.0
TURN_ALERT_B = 15.0
SWPT_ALERT_M = 10_000       # PROPOSED: SWPT >= $10B ($ millions) outside a turn window
SWPT_TURN_ALERT_M = 15_000  # inside a turn window (as-of QE-7..QE+14); calm max $12,067M (2018-01-03)
MAX_OP_AGE_D = 22    # newest European op older than this -> UNGRADEABLE (longest normal ECB gap = 3-week year-end op)
MAX_SWPT_AGE_D = 10  # SWPT as-of older than this -> UNGRADEABLE (weekly + a holiday-delayed H.4.1)
HEADLINE_D = 14      # the headline grade covers European ops traded in the last 14 days
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


def spans_qe(settle, maturity):
    """True if the funds are OUT over a quarter-end: settle <= QE < maturity.
    Keyed on SETTLEMENT, not trade (independent read ❌#11: trade 9/30, settle 10/1 is
    after the quarter-end and is NOT a turn op)."""
    t, m = dt.date.fromisoformat(settle), dt.date.fromisoformat(maturity)
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


TURN_MAX_DAYS = 21  # a short op whose funds are out over a quarter-end is a TURN op


def is_turn(op):
    return op["term"] <= TURN_MAX_DAYS and spans_qe(op["settle"], op["mat"])


def grade(op):
    """Non-turn ops grade on WATCH/ALERT. Turn ops grade on the higher TURN lines and are
    never dropped. A long op over a quarter-end (the 84d 2020-03-18 op) is not a turn op."""
    if op["cp"] not in EU:
        return "n/a (not European)"
    if is_turn(op):
        if op["bn"] >= TURN_ALERT_B:
            return "ALERT-PROPOSED (turn op)"
        if op["bn"] >= TURN_WATCH_B:
            return "WATCH-PROPOSED (turn op)"
        return "turn op, below turn lines"
    if op["bn"] >= ALERT_B:
        return "ALERT-PROPOSED"
    if op["bn"] >= WATCH_B:
        return "WATCH-PROPOSED"
    return "quiet"


def swpt(a, limit=20):
    """SWPT via the standing FORGE fetch.py FRED API path (KB-LIQ-139: the API is not
    CDN-cached). NOT via fredgraph.csv with urllib: on 2026-10-01 FRED tarpitted a
    request carrying this script's User-Agent (read timeout) while curl's UA returned
    in 0.4s and the NY Fed API answered in 0.1s — a reachability failure about the
    REQUEST, not the data."""
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "FORGE" / "tools" / "market-data"))
    from fetch import fred_fetch
    rows = fred_fetch("SWPT", limit=limit)
    if not rows or isinstance(rows, dict):
        raise RuntimeError(f"SWPT fetch returned no rows: {rows!r}"[:200])
    out = [(r["date"], float(r["value"])) for r in rows if r.get("value") not in (".", "", None) and r["date"] >= a]
    return sorted(out)


def baserate():
    allops = []
    for y in range(2010, dt.date.today().year + 1):
        allops += ops(f"{y}-01-01", f"{y}-12-31")
    tur = [o for o in allops if o["cp"] in EU and is_turn(o)]
    print(f"turn ops 2010-now: {len(tur)} | TURN-WATCH hits {[(o['trade'], o['cp'][:3], round(o['bn'], 2)) for o in tur if TURN_WATCH_B <= o['bn'] < TURN_ALERT_B]} | "
          f"TURN-ALERT hits {[(o['trade'], o['cp'][:3], round(o['bn'], 2)) for o in tur if o['bn'] >= TURN_ALERT_B]}")
    sw = swpt("2007-01-01", limit=2000)
    hits = [(d, v) for d, v in sw if swpt_grade(d, v).startswith("ALERT")]
    eps = [h for k, h in enumerate(hits) if k == 0 or (dt.date.fromisoformat(h[0]) - dt.date.fromisoformat(hits[k - 1][0])).days > 21]
    print(f"SWPT leg (turn-adjusted): {len(hits)} weeks ALERT since 2007; episode starts {[(d, int(v)) for d, v in eps]}")
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


def swpt_in_turn_window(asof):
    d = dt.date.fromisoformat(asof)
    for y in (d.year - 1, d.year):
        for mo, dd in ((3, 31), (6, 30), (9, 30), (12, 31)):
            if -7 <= (d - dt.date(y, mo, dd)).days <= 14:
                return True
    return False


def swpt_grade(asof, v_m):
    line = SWPT_TURN_ALERT_M if swpt_in_turn_window(asof) else SWPT_ALERT_M
    return "ALERT-PROPOSED" if v_m >= line else "below line"


def verdict(oplist, swpt_rows, today):
    """One overall line. Fails CLOSED on empty, non-European-only or stale inputs."""
    if not oplist:
        return "UNGRADEABLE: NY Fed returned 0 operations in the window (ECB normally trades weekly)"
    eu = [o for o in oplist if o["cp"] in EU]
    if not eu:
        return "UNGRADEABLE: no European operation in the window"
    newest = max(o["trade"] for o in eu)
    if (today - dt.date.fromisoformat(newest)).days > MAX_OP_AGE_D:
        return f"UNGRADEABLE: newest European op {newest} is older than {MAX_OP_AGE_D} days"
    if not swpt_rows:
        return "UNGRADEABLE: SWPT returned no rows"
    last_sw_date, last_sw = swpt_rows[-1]
    if (today - dt.date.fromisoformat(last_sw_date)).days > MAX_SWPT_AGE_D:
        return f"UNGRADEABLE: SWPT as-of {last_sw_date} is older than {MAX_SWPT_AGE_D} days"
    recent = [o for o in eu if (today - dt.date.fromisoformat(o["trade"])).days <= HEADLINE_D]
    grades = [grade(o) for o in recent]
    cad = cadence_switch([o for o in oplist if (today - dt.date.fromisoformat(o["trade"])).days <= HEADLINE_D])
    if any(g.startswith("ALERT") for g in grades) or swpt_grade(last_sw_date, last_sw).startswith("ALERT"):
        v = "ALERT-PROPOSED"
    elif cad:
        v = "ORANGE-PROPOSED (cadence switch: " + "; ".join(cad[:3]) + ")"
    elif any(g.startswith("WATCH") for g in grades):
        v = "WATCH-PROPOSED"
    else:
        v = "below backstop lines (no draw signal; NOT 'no dollar strain')"
    return f"{v} · newest European op {newest} · SWPT as-of {last_sw_date}"


def selftest():
    """Offline. One block per acceptance condition (analysis/2026-10-01_eurusd-basis-instrument.md §7)
    plus the pre-read checks. Fixtures use real figures from the NY Fed / FRED history."""
    fails = 0
    def chk(label, got, want):
        nonlocal fails
        ok = got == want
        fails += (not ok)
        print(f"{'PASS' if ok else 'FAIL'}  {label}: got {got!r} want {want!r}")
    def mk(trade, settle, mat, cp, bn, term):
        return dict(trade=trade, settle=settle, mat=mat, cp=cp, bn=bn, rate=None, term=term)
    ECB, SNB, BOE = "European Central Bank", "Swiss National Bank", "Bank of England"
    t = dt.date(2026, 10, 1)
    wk = [mk("2026-09-16", "2026-09-17", "2026-09-24", ECB, 0.072, 7), mk("2026-09-23", "2026-09-24", "2026-10-01", ECB, 0.197, 7)]
    fresh = [("2026-09-23", 72.0)]
    # pre-read controls
    chk("2020-03-18 ECB 84d $75.82B (long op over QE) -> ALERT", grade(mk("2020-03-18", "2020-03-19", "2020-06-11", ECB, 75.82, 84)), "ALERT-PROPOSED")
    chk("2022-10-19 SNB 7d $11.09B -> ALERT", grade(mk("2022-10-19", "2022-10-20", "2022-10-27", SNB, 11.09, 7)), "ALERT-PROPOSED")
    chk("mid-month ECB $1.0B tie -> WATCH", grade(mk("2026-10-14", "2026-10-15", "2026-10-22", ECB, 1.0, 7)), "WATCH-PROPOSED")
    chk("mid-month ECB $0.999B -> quiet", grade(mk("2026-10-14", "2026-10-15", "2026-10-22", ECB, 0.999, 7)), "quiet")
    chk("mid-month BoE $5.0B tie -> ALERT", grade(mk("2026-10-14", "2026-10-15", "2026-10-22", BOE, 5.0, 7)), "ALERT-PROPOSED")
    chk("BoJ $10B -> not European", grade(mk("2026-10-14", "2026-10-15", "2026-10-22", "Bank of Japan", 10.0, 7)), "n/a (not European)")
    chk("ECB 28d $2B over QE (term > 21, not turn) -> WATCH", grade(mk("2026-09-16", "2026-09-17", "2026-10-15", ECB, 2.0, 28)), "WATCH-PROPOSED")
    # AC1 FRED down
    chk("AC1 SWPT no rows -> UNGRADEABLE", verdict(wk, [], t).startswith("UNGRADEABLE"), True)
    # AC2 empty / non-European / stale op
    chk("AC2 no ops -> UNGRADEABLE", verdict([], fresh, t).startswith("UNGRADEABLE"), True)
    chk("AC2 only BoJ ops -> UNGRADEABLE", verdict([mk("2026-09-29", "2026-10-01", "2026-10-08", "Bank of Japan", 0.01, 7)], fresh, t).startswith("UNGRADEABLE"), True)
    chk("AC2 newest European op 23d old -> UNGRADEABLE", verdict([mk("2026-09-08", "2026-09-09", "2026-09-16", ECB, 0.1, 7)], fresh, t).startswith("UNGRADEABLE"), True)
    chk("AC2 newest European op 22d old -> graded", verdict([mk("2026-09-09", "2026-09-10", "2026-09-17", ECB, 0.1, 7)], fresh, t).startswith("UNGRADEABLE"), False)
    # AC3 stale SWPT
    chk("AC3 SWPT as-of 11d old -> UNGRADEABLE", verdict(wk, [("2026-09-20", 72.0)], t).startswith("UNGRADEABLE"), True)
    chk("AC3 SWPT as-of 10d old -> graded", verdict(wk, [("2026-09-21", 72.0)], t).startswith("UNGRADEABLE"), False)
    # AC4 headline sees every European op in 14d, names dates (replay shape of 2020-03-31)
    w31 = [mk("2020-03-25", "2020-03-26", "2020-06-18", ECB, 27.81, 84)] + \
          [mk("2020-03-3%d" % k, "2020-03-31", "2020-04-0%d" % (k + 6), "Bank of Japan", 1.0, 7) for k in (0, 1)] * 6
    chk("AC4 one ALERT op among 13 ops -> ALERT headline", verdict(w31, [("2020-03-25", 0.0)], dt.date(2020, 3, 31)).startswith("ALERT"), True)
    chk("AC4 headline names newest European op and SWPT as-of", ("newest European op 2026-09-23" in verdict(wk, fresh, t)) and ("SWPT as-of 2026-09-23" in verdict(wk, fresh, t)), True)
    # AC5 settlement-keyed turn test
    chk("AC5 trade 9/30 settle 10/1 -> NOT turn", is_turn(mk("2026-09-30", "2026-10-01", "2026-10-08", ECB, 8.0, 7)), False)
    chk("AC5 trade 9/29 settle 9/30 mat 10/7 -> turn", is_turn(mk("2026-09-29", "2026-09-30", "2026-10-07", ECB, 8.0, 7)), True)
    chk("AC5 maturing ON the quarter-end day -> not turn", spans_qe("2026-09-24", "2026-09-30"), False)
    # AC6 turn ops graded on their own lines, never dropped
    chk("AC6 2020-03-25 ECB 7d $17.27B turn -> ALERT (turn)", grade(mk("2020-03-25", "2020-03-26", "2020-04-02", ECB, 17.27, 7)), "ALERT-PROPOSED (turn op)")
    chk("AC6 2011-12-21 ECB 14d $33.0B turn -> ALERT (turn)", grade(mk("2011-12-21", "2011-12-22", "2012-01-05", ECB, 33.0, 14)), "ALERT-PROPOSED (turn op)")
    chk("AC6 2017-12-20 ECB 21d $11.91B calm turn -> WATCH (turn), not ALERT", grade(mk("2017-12-20", "2017-12-21", "2018-01-11", ECB, 11.907, 21)), "WATCH-PROPOSED (turn op)")
    chk("AC6 2020-03-25 BoE 7d $7.71B turn -> WATCH (turn)", grade(mk("2020-03-25", "2020-03-26", "2020-04-02", BOE, 7.71, 7)), "WATCH-PROPOSED (turn op)")
    chk("AC6 9/23 ECB $0.197B turn -> below turn lines (printed, not dropped)", grade(wk[1]), "turn op, below turn lines")
    # AC7 SWPT turn-adjusted
    chk("AC7 SWPT $12,067M as-of 2018-01-03 (turn window) -> below line", swpt_grade("2018-01-03", 12067.0), "below line")
    chk("AC7 SWPT $11,302M as-of 2022-10-26 (outside) -> ALERT", swpt_grade("2022-10-26", 11302.0), "ALERT-PROPOSED")
    chk("AC7 SWPT $10,000M tie outside turn window -> ALERT", swpt_grade("2026-11-11", 10000.0), "ALERT-PROPOSED")
    chk("AC7 SWPT $15,000M tie inside turn window -> ALERT", swpt_grade("2026-10-07", 15000.0), "ALERT-PROPOSED")
    # cadence leg
    daily = [mk(f"2023-03-{d:02d}", f"2023-03-{d+1:02d}", f"2023-03-{d+2:02d}", ECB, 0.1, 1) for d in (20, 21, 22)]
    chk("cadence: daily ECB ops -> switch", bool(cadence_switch(daily)), True)
    chk("cadence: weekly ECB ops -> none", cadence_switch(wk), [])
    chk("cadence: single isolated 1d op -> none", cadence_switch([mk("2024-05-15", "2024-05-15", "2024-05-16", BOE, 0.01, 1)]), [])
    # fetch failure -> rc 2
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
    eu = [x for x in o if x["cp"] in EU]
    print(f"NY Fed USD swap operations, last 60 days: {len(o)} ops ({len(eu)} European, all printed; "
          f"{len(o) - len(eu)} non-European not graded). Posted at settlement:")
    for x in sorted(eu, key=lambda x: x["trade"]):
        print(f"  trade {x['trade']} settle {x['settle']} {x['term']:>3}d {x['cp'][:24]:<24} ${x['bn']:.3f}B @ {x['rate']}%  -> {grade(x)}")
    if s:
        d, v = s[-1]
        lab = swpt_grade(d, v) + (" (turn window)" if swpt_in_turn_window(d) else "")
        print(f"FRED SWPT (H.4.1, Wed level, ALL counterparties — global, not European): ${v:,.0f}M as-of {d} -> {lab}; prior: " +
              ", ".join(f"{dd[5:]} {vv:,.0f}" for dd, vv in s[-5:-1]))
    v = verdict(o, s, today)
    print(f"VERDICT (PROPOSED lines): {v}")
    return 2 if v.startswith("UNGRADEABLE") else 0


if __name__ == "__main__":
    sys.exit(main() or 0)
