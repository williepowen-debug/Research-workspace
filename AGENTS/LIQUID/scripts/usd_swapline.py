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

EXIT CODES (L568 pass 2026-10-08): 0 both legs healthy and graded · 1 --selftest failure ·
2 UNGRADEABLE · 3 PARTIAL (one leg not healthy, and a leg with data reads WATCH or above) ·
4 WITHHELD (default run refused; --baserate / --force-withheld-test computed while WITHHELD).
"""
import json, sys, urllib.request, datetime as dt, time, csv, io, contextlib

# ⛔ CATO D2 / AC-D2 (analysis 2026-10-01 §7b): ONE switch. While True, a default run prints the
# refusal below and NO reading, before any network call. Clearing it is the release step after
# PROME's LAST independent read (DOCKET L568) — never a side effect of a fix.
WITHHELD = True
WITHHELD_WHY = ("WITHHELD — not for operational use; disposition: PROME DOCKET L568 / "
                "AGENTS/LIQUID/analysis/2026-10-01_eurusd-basis-instrument.md §WITHHELD "
                "(PROME read 2: AGENTS/LIQUID/inbox/processed/2026-10-01_from-PROME_usd-swapline-result-read-2-WITHHELD.md)")
RC_OK, RC_SELFTEST_FAIL, RC_UNGRADEABLE, RC_PARTIAL, RC_WITHHELD = 0, 1, 2, 3, 4

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
SWPT_TURN_ALERT_M = 15_000  # inside a turn window (as-of QE-7..QE+14). Max in-window reading in CALM years
# only: $12,067M (2018-01-03). ⚠️ X3 (read 2): in-window STRESS weeks also sit under this line and are
# suppressed — 2007-12-26 $14,000M (the first GFC draw week; onset reads 2008-01-02, one week late) and
# 2012-09-26..10-10 $12.5-14.7B (splits 2011-12; the '2012-10-17' episode start is an artifact). The
# window holds ~1 week in 4. --baserate prints the share and every suppressed week. Line = Will's word.
MAX_OP_AGE_D = 22    # newest European op older than this -> UNGRADEABLE (longest normal ECB gap = 3-week year-end op)
MAX_SWPT_AGE_D = 10  # SWPT as-of older than this -> UNGRADEABLE (weekly + a holiday-delayed H.4.1)
HEADLINE_D = 14      # the headline grade covers European ops traded in the last 14 days
# WQ-398 (a) AC-X2b (2026-10-09, UNREVIEWED until Will's named read): --baserate history floors, measured
# 10/9 on real data — European trade dates have no gap > 21d since 2015-06-10 (before it, use was dormant
# for months at a time); SWPT is weekly from 2007-01-03 with every gap exactly 7 days.
CONTINUOUS_FROM = "2015-06-10"
SWPT_FIRST_MAX = "2007-01-10"
API ="https://markets.newyorkfed.org/api/fxs/usdollar/search.json?startDate={a}&endDate={b}"


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


def _isodate(v, what):
    if not isinstance(v, str):
        raise ValueError(f"malformed field {what}={v!r}")
    try:
        return dt.date.fromisoformat(v)
    except ValueError:
        raise ValueError(f"malformed field {what}={v!r}") from None


def _num(v, what):
    if isinstance(v, bool) or not isinstance(v, (int, float)) or v != v or v in (float("inf"), float("-inf")) or v < 0:
        raise ValueError(f"malformed field {what}={v!r}")


def check_ops(oplist):
    """AC-X1p (WQ-398 a): every field the OPS leg reads must parse, or the WHOLE leg is DOWN.
    A malformed op is never dropped-and-the-rest-graded: it could be the ALERT op."""
    for x in oplist:
        try:
            who = f" (op traded {x.get('trade')!r}, {str(x.get('cp'))[:24]!r})"
            if not isinstance(x.get("cp"), str) or not x["cp"]:
                raise ValueError(f"malformed field cp={x.get('cp')!r}")
            for k in ("trade", "settle", "mat"):
                _isodate(x.get(k), k)
            _num(x.get("bn"), "bn")
            if isinstance(x.get("term"), bool) or not isinstance(x.get("term"), int) or x["term"] < 0:
                raise ValueError(f"malformed field term={x.get('term')!r}")
        except ValueError as e:
            raise ValueError(f"{e}{who}") from None
        except Exception as e:   # not a dict, etc.
            raise ValueError(f"malformed op row {x!r}"[:200]) from None


def check_swpt(rows):
    """AC-X1p: every SWPT row must be (ISO as-of, finite non-negative number), or the leg is DOWN."""
    for r in rows:
        try:
            d, v = r
        except Exception:
            raise ValueError(f"malformed SWPT row {r!r}"[:200]) from None
        _isodate(d, "SWPT as-of")
        _num(v, f"SWPT value (as-of {d!r})")


def check_ops_history(by_year, today):
    """AC-X2b (1)-(5): the NY Fed history is complete enough to count on, or raise naming the gap."""
    for y, ol in by_year.items():
        check_ops(ol)
        out = [o["trade"] for o in ol if not (f"{y}-01-01" <= o["trade"] <= f"{y}-12-31")]
        if out:
            raise RuntimeError(f"the {y} request returned {len(out)} ops traded outside {y} (e.g. {out[0]}) — not {y}'s history")
        if y < today.year and not any(o["cp"] in EU for o in ol):
            raise RuntimeError(f"NY Fed returned no European op for {y} (every year 2010-2025 had >= 16 on 2026-10-09)")
    seen = set()
    for ol in by_year.values():
        for o in ol:
            k = (o["trade"], o["settle"], o["mat"], o["cp"], o["bn"], o["term"])
            if k in seen:
                raise RuntimeError(f"duplicate op across year fetches: {k}")
            seen.add(k)
    ds = sorted({dt.date.fromisoformat(o["trade"]) for ol in by_year.values() for o in ol
                 if o["cp"] in EU and o["trade"] >= CONTINUOUS_FROM})
    if not ds:
        raise RuntimeError(f"no European op since {CONTINUOUS_FROM}")
    for a, b in zip(ds, ds[1:]):
        if (b - a).days > MAX_OP_AGE_D:
            raise RuntimeError(f"European ops missing between {a} and {b} ({(b - a).days} days > {MAX_OP_AGE_D}; "
                               f"continuous since {CONTINUOUS_FROM}) — partial history")
    if (today - ds[-1]).days > MAX_OP_AGE_D:
        raise RuntimeError(f"newest European op {ds[-1]} is older than {MAX_OP_AGE_D} days — truncated or stale history")


def check_swpt_history(sw, today):
    """AC-X2b (6)-(9): SWPT weekly history from the start of 2007, no missing week, current."""
    check_swpt(sw)
    if not sw:
        raise RuntimeError("SWPT returned no usable rows")
    if sw[0][0] > SWPT_FIRST_MAX:
        raise RuntimeError(f"SWPT history starts {sw[0][0]}, after {SWPT_FIRST_MAX} — the GFC onset would be missing")
    for (a, _), (b, _) in zip(sw, sw[1:]):
        gap = (dt.date.fromisoformat(b) - dt.date.fromisoformat(a)).days
        if gap != 7:
            raise RuntimeError(f"SWPT weeks missing or misaligned between {a} and {b} ({gap} days, weekly series)")
    if (today - dt.date.fromisoformat(sw[-1][0])).days > MAX_SWPT_AGE_D:
        raise RuntimeError(f"SWPT newest as-of {sw[-1][0]} is older than {MAX_SWPT_AGE_D} days — truncated or stale history")


def baserate(today=None):
    """Replays the lines over history. Fails CLOSED (X2, read 2 2026-10-01; X2-residual, read 3
    2026-10-08): with either source down OR PARTIAL (an empty year, a gap, a late start, a stale
    tail, a malformed field) it prints UNGRADEABLE and returns 2 — never a count off part of a leg."""
    today = today or dt.date.today()
    try:
        by_year = {y: ops(f"{y}-01-01", f"{y}-12-31") for y in range(2010, today.year + 1)}
        check_ops_history(by_year, today)
        allops = [o for ol in by_year.values() for o in ol]
        if len(allops) < 1000:
            raise RuntimeError(f"NY Fed history returned {len(allops)} ops since 2010 (expected > 1,000)")
    except Exception as e:
        print(f"UNGRADEABLE: --baserate NY Fed leg failed ({e.__class__.__name__}: {e}) — no counts printed")
        return RC_UNGRADEABLE
    try:
        sw = swpt("2007-01-01", limit=2000)
        check_swpt_history(sw, today)
        if len(sw) < 900:
            raise RuntimeError(f"SWPT returned {len(sw)} usable weekly rows since 2007 (expected > 900)")
    except Exception as e:
        print(f"UNGRADEABLE: --baserate SWPT leg failed ({e.__class__.__name__}: {e}) — no counts printed")
        return RC_UNGRADEABLE
    print(f"history coverage (AC-X2b floor): European ops per year {[(y, sum(o['cp'] in EU for o in ol)) for y, ol in by_year.items()]}; "
          f"none missing > {MAX_OP_AGE_D}d since {CONTINUOUS_FROM} · SWPT {sw[0][0]} -> {sw[-1][0]}, {len(sw)} weeks, no missing week")
    tur = [o for o in allops if o["cp"] in EU and is_turn(o)]
    print(f"turn ops 2010-now: {len(tur)} | TURN-WATCH hits {[(o['trade'], o['cp'][:3], round(o['bn'], 2)) for o in tur if TURN_WATCH_B <= o['bn'] < TURN_ALERT_B]} | "
          f"TURN-ALERT hits {[(o['trade'], o['cp'][:3], round(o['bn'], 2)) for o in tur if o['bn'] >= TURN_ALERT_B]}")

    def episodes(hits):
        return [h for k, h in enumerate(hits) if k == 0 or (dt.date.fromisoformat(h[0]) - dt.date.fromisoformat(hits[k - 1][0])).days > 21]
    hits = [(d, v) for d, v in sw if swpt_grade(d, v).startswith("ALERT")]
    print(f"SWPT leg (turn-adjusted): {len(hits)} weeks ALERT since 2007; episode starts {[(d, int(v)) for d, v in episodes(hits)]}")
    # X3: the turn window's cost, computed rather than asserted
    inw = [(d, v) for d, v in sw if swpt_in_turn_window(d)]
    supp = [(d, int(v)) for d, v in inw if SWPT_ALERT_M <= v < SWPT_TURN_ALERT_M]
    flat = [(d, v) for d, v in sw if v >= SWPT_ALERT_M]
    print(f"SWPT turn-window cost (X3): {len(inw)} of {len(sw)} weeks ({100 * len(inw) / len(sw):.1f}%) sit inside the window; "
          f"weeks >= ${SWPT_ALERT_M:,}M it suppresses (read 'below line'): {supp}")
    print(f"SWPT for comparison, UN-adjusted (${SWPT_ALERT_M:,}M everywhere): {len(flat)} weeks; episode starts {[(d, int(v)) for d, v in episodes(flat)]}")
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
    return RC_OK


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


_RANK = {"ALERT": 3, "ORANGE": 2, "WATCH": 1, "below": 0}


def ops_leg(oplist, today, err=None):
    """OPS leg on its own (X1). state OK / STALE / DOWN; grade ALERT / ORANGE / WATCH / below."""
    leg = dict(name="OPS", state="DOWN", reason="", grade=None, cad=[], newest=None)
    if err is not None:
        leg["reason"] = f"NY Fed fetch or field check failed ({err})"
        return leg
    if not oplist:
        leg["reason"] = "NY Fed returned 0 operations in the window (ECB normally trades weekly)"
        return leg
    try:
        check_ops(oplist)   # AC-X1p: a malformed row marks THIS leg DOWN, never raises
    except ValueError as e:
        leg["reason"] = f"NY Fed {e}"
        return leg
    eu = [o for o in oplist if o["cp"] in EU]
    if not eu:
        leg["reason"] = "no European operation in the window"
        return leg
    newest = max(o["trade"] for o in eu)
    leg["newest"] = newest
    recent = [o for o in eu if (today - dt.date.fromisoformat(o["trade"])).days <= HEADLINE_D]
    grades = [grade(o) for o in recent]
    cad = cadence_switch([o for o in oplist if (today - dt.date.fromisoformat(o["trade"])).days <= HEADLINE_D])
    leg["cad"] = cad
    leg["grade"] = ("ALERT" if any(g.startswith("ALERT") for g in grades) else "ORANGE" if cad
                    else "WATCH" if any(g.startswith("WATCH") for g in grades) else "below")
    if (today - dt.date.fromisoformat(newest)).days > MAX_OP_AGE_D:
        leg["state"], leg["reason"] = "STALE", f"newest European op {newest} is older than {MAX_OP_AGE_D} days"
    else:
        leg["state"] = "OK"
    return leg


def swpt_leg(swpt_rows, today, err=None):
    """SWPT leg on its own (X1). state OK / STALE / DOWN; grade ALERT / below."""
    leg = dict(name="SWPT", state="DOWN", reason="", grade=None, asof=None, value=None)
    if err is not None:
        leg["reason"] = f"FRED SWPT fetch or field check failed ({err})"
        return leg
    if not swpt_rows:
        leg["reason"] = "SWPT returned no usable rows"
        return leg
    try:
        check_swpt(swpt_rows)   # AC-X1p
    except ValueError as e:
        leg["reason"] = f"FRED {e}"
        return leg
    d, v = swpt_rows[-1]
    leg["asof"], leg["value"] = d, v
    leg["grade"] = "ALERT" if swpt_grade(d, v).startswith("ALERT") else "below"
    if (today - dt.date.fromisoformat(d)).days > MAX_SWPT_AGE_D:
        leg["state"], leg["reason"] = "STALE", f"SWPT as-of {d} is older than {MAX_SWPT_AGE_D} days"
    else:
        leg["state"] = "OK"
    return leg


def assess(oplist, swpt_rows, today, ops_err=None, swpt_err=None):
    """(verdict text, rc, legs). X1 (read 2): each leg graded on its own. A known ALERT is never
    printed as UNGRADEABLE (a STALE leg's ALERT is named STALE with its as-of); "below backstop
    lines" is never printed off a partial; PARTIAL carries rc 3, UNGRADEABLE rc 2."""
    legs = [ops_leg(oplist, today, ops_err), swpt_leg(swpt_rows, today, swpt_err)]
    opl, swl = legs
    with_data = [l for l in legs if l["state"] in ("OK", "STALE")]
    not_ok = [l for l in legs if l["state"] != "OK"]
    top = max((_RANK[l["grade"]] for l in with_data), default=-1)

    def label(g):
        src = [l for l in with_data if l["grade"] == g]
        stale = [l for l in src if l["state"] == "STALE"]
        if g == "ALERT":
            t = "ALERT-PROPOSED"
            if src and len(stale) == len(src):   # ALERT known only from a STALE leg
                t += " (" + "; ".join(f"{l['name']} STALE, last reading as-of {l.get('asof') or l.get('newest')}" for l in stale) + ")"
            return t
        if g == "ORANGE":
            return "ORANGE-PROPOSED (cadence switch: " + "; ".join(opl["cad"][:3]) + ")"
        if g == "WATCH":
            return "WATCH-PROPOSED"
        return "below backstop lines (no draw signal; NOT 'no dollar strain')"

    tail = f"newest European op {opl['newest'] or 'n/a'} · SWPT as-of {swl['asof'] or 'n/a'}"
    grade_name = {v: k for k, v in _RANK.items()}.get(top)
    if not not_ok:
        return f"{label(grade_name)} · {tail}", RC_OK, legs
    partial = "PARTIAL: " + "; ".join(f"{l['name']} {l['state']} ({l['reason']})" for l in not_ok)
    if top >= _RANK["WATCH"]:
        return f"{label(grade_name)} · {partial} · {tail}", RC_PARTIAL, legs
    seen = "; ".join(f"{l['name']} {l['state']} reads below its line" for l in with_data) or "no leg has data"
    return f"UNGRADEABLE: {partial} · {seen} — no overall reading · {tail}", RC_UNGRADEABLE, legs


def verdict(oplist, swpt_rows, today, ops_err=None, swpt_err=None):
    """One overall line (text only; rc via assess)."""
    return assess(oplist, swpt_rows, today, ops_err, swpt_err)[0]


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
    # ---- L568 pass (2026-10-08): AC-X1 · AC-X2 · AC-D2 (change note analysis/2026-10-08_usd-swapline-L568-change-note.md §A)
    t2 = dt.date(2026, 10, 16)
    big = [mk("2026-10-14", "2026-10-15", "2026-10-22", ECB, 20.0, 7), mk("2026-10-07", "2026-10-08", "2026-10-15", ECB, 0.1, 7)]
    quiet = [mk("2026-10-14", "2026-10-15", "2026-10-22", ECB, 0.1, 7), mk("2026-10-07", "2026-10-08", "2026-10-15", ECB, 0.1, 7)]
    sw_ok = [("2026-10-14", 72.0)]
    def A(*a, **k):
        v, rc, _ = assess(*a, **k)
        return (v.split(" · ")[0].split(" (")[0], "PARTIAL" in v, rc)
    chk("X1 $20B ECB op + FRED down -> ALERT, PARTIAL, rc 3", A(big, [], t2, swpt_err="TimeoutError"), ("ALERT-PROPOSED", True, 3))
    chk("X1 $20B ECB op + SWPT 12d old -> ALERT, PARTIAL, rc 3", A(big, [("2026-10-04", 72.0)], t2), ("ALERT-PROPOSED", True, 3))
    chk("X1 SWPT $50,000M fresh + NY Fed down -> ALERT, PARTIAL, rc 3", A([], [("2026-10-14", 50000.0)], t2, ops_err="TimeoutError"), ("ALERT-PROPOSED", True, 3))
    r327 = [mk("2020-03-18", "2020-03-19", "2020-06-11", ECB, 75.82, 84), mk("2020-03-25", "2020-03-26", "2020-06-18", ECB, 27.81, 84)]
    chk("X1 real-shape 2020-03-27 ops + SWPT as-of 2020-03-11 (stale) -> ALERT, PARTIAL, rc 3",
        A(r327, [("2020-03-11", 45.0)], dt.date(2020, 3, 27)), ("ALERT-PROPOSED", True, 3))
    chk("X1 quiet ops + FRED down -> UNGRADEABLE rc 2 (never 'below' off a partial)", A(quiet, [], t2, swpt_err="x")[0::2], ("UNGRADEABLE: PARTIAL: SWPT DOWN", 2))
    chk("X1 quiet SWPT + NY Fed down -> UNGRADEABLE rc 2", A([], sw_ok, t2, ops_err="x")[0::2], ("UNGRADEABLE: PARTIAL: OPS DOWN", 2))
    chk("X1 both down -> UNGRADEABLE rc 2", assess([], [], t2, ops_err="x", swpt_err="y")[1], 2)
    v_st = verdict(quiet, [("2026-10-04", 50000.0)], t2)
    chk("X1 STALE SWPT $50,000M + quiet fresh ops -> ALERT named STALE, PARTIAL, rc 3",
        (v_st.startswith("ALERT-PROPOSED (SWPT STALE, last reading as-of 2026-10-04)"), "PARTIAL" in v_st, assess(quiet, [("2026-10-04", 50000.0)], t2)[1]), (True, True, 3))
    chk("X1 both OK and quiet -> below backstop lines, rc 0", A(quiet, sw_ok, t2), ("below backstop lines", False, 0))
    chk("X1 both OK, $20B op -> ALERT, no PARTIAL, rc 0", A(big, sw_ok, t2), ("ALERT-PROPOSED", False, 0))
    # separate try blocks through run_live: NY Fed raising must not hide a $50B SWPT line
    g = globals()
    real_ops, real_swpt, real_get = g["ops"], g["swpt"], g["_get"]
    calls = []
    def ops_boom(*a, **k):
        calls.append("ops"); raise TimeoutError("synthetic")
    def swpt_boom(*a, **k):
        calls.append("swpt"); raise TimeoutError("synthetic")
    def get_boom(*a, **k):
        calls.append("_get"); raise TimeoutError("synthetic")
    def run(fn, *a):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = fn(*a)
        return buf.getvalue(), rc
    try:
        g["ops"], g["swpt"] = ops_boom, (lambda *a, **k: [("2026-10-14", 50000.0)])
        out, rc = run(run_live, t2)
        chk("X1 run_live: NY Fed down, SWPT $50,000M -> SWPT line printed + ALERT verdict, rc 3",
            ("$50,000M as-of 2026-10-14" in out, "VERDICT (PROPOSED lines): ALERT-PROPOSED" in out, rc), (True, True, 3))
        g["ops"], g["swpt"] = (lambda *a, **k: big), swpt_boom
        out, rc = run(run_live, t2)
        chk("X1 run_live: FRED down, $20B op -> op row + SWPT DOWN line + ALERT verdict, rc 3",
            ("$20.000B" in out, "SWPT leg DOWN" in out, "VERDICT (PROPOSED lines): ALERT-PROPOSED" in out, rc), (True, True, True, 3))
        # AC-X2: --baserate fails closed on either source
        g["ops"], g["swpt"] = (lambda *a, **k: [mk("2014-01-08", "2014-01-09", "2014-01-16", ECB, 0.1, 7)] * 100), (lambda *a, **k: [])
        out, rc = run(baserate)
        chk("X2 --baserate, FRED down -> UNGRADEABLE rc 2, no SWPT count line", (rc, "UNGRADEABLE" in out, "weeks ALERT since" in out), (2, True, False))
        g["ops"] = ops_boom
        out, rc = run(baserate)
        chk("X2 --baserate, NY Fed down -> UNGRADEABLE rc 2, no counts", (rc, out.startswith("UNGRADEABLE"), "turn ops" in out), (2, True, False))
        # ---- WQ-398 (a) pass (2026-10-09, UNREVIEWED): AC-X2b · AC-X1p (analysis/2026-10-09_usd-swapline-WQ398-fix.md §A)
        T = dt.date(2026, 10, 9)
        def wednesdays(a, b):
            d = a
            while d <= b:
                yield d
                d += dt.timedelta(7)
        def hist_ops(end, drop=lambda d: False):
            out = []
            for d in wednesdays(dt.date(2010, 1, 6), end):
                if drop(d):
                    continue
                s, m = d + dt.timedelta(1), d + dt.timedelta(8)
                out += [mk(str(d), str(s), str(m), ECB, 0.1, 7), mk(str(d), str(s), str(m), SNB, 0.05, 7)]
            return out
        def ops_from(hist, override=None):
            def f(a, b):
                if override and a[:4] in override:
                    return override[a[:4]]
                return [o for o in hist if a <= o["trade"] <= b]
            return f
        def hist_sw(a, b, drop=lambda d: False):
            return [(str(d), 0.0) for d in wednesdays(a, b) if not drop(d)]
        H, SWH = hist_ops(dt.date(2026, 10, 7)), hist_sw(dt.date(2007, 1, 3), dt.date(2026, 10, 7))
        def BR(o, s, today=T):
            g["ops"], g["swpt"] = o, (lambda *a, **k: s)
            return run(baserate, today)
        out, rc = BR(ops_from(H), SWH)
        chk("X2b healthy synthetic history -> rc 0, coverage line + counts", (rc, "history coverage" in out, "turn ops" in out, "weeks ALERT since" in out), (0, True, True, True))
        out, rc = BR(ops_from(H, {"2020": []}), SWH)
        chk("X2b CE2a NY Fed empty for 2020 only -> rc 2 naming 2020, no counts", (rc, "for 2020" in out, "turn ops" in out), (2, True, False))
        out, rc = BR(ops_from(H), hist_sw(dt.date(2008, 10, 1), dt.date(2026, 10, 7)))
        chk("X2b CE2b SWPT starts 2008-10 -> rc 2, no SWPT count line", (rc, "starts 2008-10-01" in out, "weeks ALERT since" in out), (2, True, False))
        out, rc = BR(ops_from(H), hist_sw(dt.date(2007, 1, 3), dt.date(2026, 10, 7), drop=lambda d: d == dt.date(2008, 10, 1)))
        chk("X2b SWPT one week missing (2008-10-01) -> rc 2 naming the gap", (rc, "between 2008-09-24 and 2008-10-08" in out, "weeks ALERT since" in out), (2, True, False))
        out, rc = BR(ops_from(H), hist_sw(dt.date(2007, 1, 3), dt.date(2026, 9, 9)))
        chk("X2b SWPT newest as-of 30 days old -> rc 2", (rc, "newest as-of 2026-09-09" in out, "weeks ALERT since" in out), (2, True, False))
        out, rc = BR(ops_from(hist_ops(dt.date(2026, 10, 7), drop=lambda d: dt.date(2016, 7, 1) <= d <= dt.date(2016, 12, 31))), SWH)
        chk("X2b 2016 truncated after June -> rc 2 naming the gap", (rc, "missing between 2016-06-29 and 2017-01-04" in out, "turn ops" in out), (2, True, False))
        out, rc = BR(ops_from(H, {"2020": [o for o in H if o["trade"][:4] == "2019"]}), SWH)
        chk("X2b the 2020 request answered with 2019's ops -> rc 2", (rc, "traded outside 2020" in out, "turn ops" in out), (2, True, False))
        y19 = [o for o in H if o["trade"][:4] == "2019"]
        out, rc = BR(ops_from(H, {"2019": y19 + y19[:1]}), SWH)
        chk("X2b one op returned twice -> rc 2 duplicate", (rc, "duplicate op" in out, "turn ops" in out), (2, True, False))
        out, rc = BR(ops_from(hist_ops(dt.date(2026, 12, 16))), hist_sw(dt.date(2007, 1, 3), dt.date(2026, 12, 30)), dt.date(2027, 1, 5))
        chk("X2b run 2027-01-05, 2027 empty, newest op 2026-12-16 -> NOT failed for the current year", (rc, "turn ops" in out), (0, True))
        bad_h = [dict(o, mat="") if o["trade"] == "2018-05-02" and o["cp"] == ECB else o for o in H]
        out, rc = BR(ops_from(bad_h), SWH)
        chk("X2b malformed op in history -> rc 2, field named", (rc, "malformed field mat=''" in out, "turn ops" in out), (2, True, False))
        out, rc = BR(ops_from(H), [])
        chk("X2b healthy NY Fed + FRED empty -> rc 2 on the SWPT leg", (rc, "SWPT leg failed" in out, "weeks ALERT since" in out), (2, True, False))
        # AC-X1p: a malformed field marks only its own leg DOWN (CE1e / CE1f, read 3)
        ce1e = [dict(big[0], mat="")] + quiet
        g["ops"], g["swpt"] = (lambda *a, **k: ce1e), (lambda *a, **k: [("2026-10-14", 50000.0)])
        out, rc = run(run_live, t2)
        chk("X1p CE1e European op mat='' + SWPT $50,000M -> SWPT line + ALERT · PARTIAL OPS DOWN, rc 3",
            ("$50,000M as-of 2026-10-14" in out, "VERDICT (PROPOSED lines): ALERT-PROPOSED" in out, "PARTIAL: OPS DOWN" in out, "malformed field mat=''" in out, rc), (True, True, True, True, 3))
        g["ops"], g["swpt"] = (lambda *a, **k: big), (lambda *a, **k: [("2026-13-01", 72.0)])
        out, rc = run(run_live, t2)
        chk("X1p CE1f SWPT as-of '2026-13-01' + $20B op -> op row + SWPT DOWN + ALERT, rc 3",
            ("$20.000B" in out, "SWPT leg DOWN" in out, "VERDICT (PROPOSED lines): ALERT-PROPOSED" in out, rc), (True, True, True, 3))
        raw = json.dumps({"fxSwaps": {"operations": [dict(tradeDate="2026-10-14", settlementDate="2026-10-15", maturityDate="2026-10-22",
                          counterparty=ECB, amount=None, interestRate=4.15, termInDays=7)]}})
        g["ops"], g["_get"], g["swpt"] = real_ops, (lambda *a, **k: raw), (lambda *a, **k: sw_ok)
        out, rc = run(run_live, t2)
        chk("X1p raw NY Fed amount=null through real ops() -> OPS DOWN, SWPT printed, rc 2",
            ("OPS leg DOWN" in out, "$72M as-of 2026-10-14" in out, "VERDICT (PROPOSED lines): UNGRADEABLE" in out, rc), (True, True, True, 2))
        g["_get"] = real_get
        g["ops"], g["swpt"] = (lambda *a, **k: quiet + [mk("2026-10-13", "2026-10-14", "", "Bank of Japan", 0.1, 7)]), (lambda *a, **k: sw_ok)
        out, rc = run(run_live, t2)
        chk("X1p non-European op mat='' + quiet legs -> OPS DOWN, UNGRADEABLE rc 2 (fail closed)",
            ("OPS leg DOWN" in out, "VERDICT (PROPOSED lines): UNGRADEABLE" in out, rc), (True, True, 2))
        chk("X1p SWPT value NaN + $20B op (assess) -> ALERT, PARTIAL SWPT DOWN, rc 3",
            A(big, [("2026-10-14", float("nan"))], t2), ("ALERT-PROPOSED", True, 3))
        g["ops"], g["swpt"] = (lambda *a, **k: ce1e), (lambda *a, **k: [("", 50000.0)])
        out, rc = run(run_live, t2)
        chk("X1p both legs malformed -> verdict printed, UNGRADEABLE rc 2, no traceback",
            ("VERDICT (PROPOSED lines): UNGRADEABLE" in out, rc), (True, 2))
        v_m, rc_m, legs_m = assess(ce1e, sw_ok, t2)
        chk("X1p assess() direct with a malformed op -> returns, OPS DOWN, rc 2", (legs_m[0]["state"], "malformed field mat" in v_m, rc_m), ("DOWN", True, 2))
        # AC-D2: WITHHELD refuses before any network call, leaks no grade, exit 4
        if WITHHELD:
            del calls[:]
            g["ops"], g["swpt"], g["_get"] = ops_boom, swpt_boom, get_boom
            out, rc = run(main, [])
            chk("D2 default run while WITHHELD, network failing -> refusal, rc 4, no network call",
                ("WITHHELD" in out, "VERDICT" in out, rc, calls), (True, False, 4, []))
            g["ops"], g["swpt"] = (lambda *a, **k: big), (lambda *a, **k: [("2026-10-14", 50000.0)])
            out, rc = run(main, [])
            chk("D2 default run while WITHHELD on REAL-ALERT feeds -> refusal only, no ALERT text, rc 4",
                ("WITHHELD" in out, "ALERT" in out, rc), (True, False, 4))
            g["ops"], g["swpt"] = (lambda *a, **k: quiet), (lambda *a, **k: sw_ok)
            out, rc = run(main, ["--force-withheld-test"])
            lines = [l for l in out.splitlines() if l.strip()]
            chk("D2 --force-withheld-test -> computes, EVERY line prefixed WITHHELD-TEST:, rc 4",
                (all(l.startswith("WITHHELD-TEST: ") for l in lines), any("VERDICT" in l for l in lines), rc), (True, True, 4))
    finally:
        g["ops"], g["swpt"], g["_get"] = real_ops, real_swpt, real_get
    print(f"selftest: {'OK' if not fails else str(fails) + ' FAIL'}")
    return RC_SELFTEST_FAIL if fails else RC_OK


def run_live(today):
    """One live reading. X1: the two legs are fetched in SEPARATE try blocks, so one source
    failing never hides the other leg's line or grade."""
    o = s = None
    oerr = serr = None
    # AC-X1p (WQ-398 a): each leg's FIELD CHECK sits inside that leg's own try, so a malformed
    # field marks only that leg DOWN (CE1e/CE1f, read 3: it used to crash after the try blocks).
    try:
        o = ops(str(today - dt.timedelta(days=60)), str(today))
        check_ops(o)
    except Exception as e:
        o, oerr = None, f"{e.__class__.__name__}: {e}"[:200]
    try:
        s = swpt(str(today - dt.timedelta(days=120)))
        check_swpt(s)
    except Exception as e:
        s, serr = None, f"{e.__class__.__name__}: {e}"[:200]
    print("⛔ Lines are PROPOSED, NOT REGISTERED (Will's word). Usage = ceiling-binding, not a basis level.")
    if oerr:
        print(f"NY Fed USD swap operations: FETCH OR FIELD CHECK FAILED ({oerr}) — OPS leg DOWN")
    else:
        try:
            eu = [x for x in o if x["cp"] in EU]
            print(f"NY Fed USD swap operations, last 60 days: {len(o)} ops ({len(eu)} European, all printed; "
                  f"{len(o) - len(eu)} non-European not graded). Posted at settlement:")
            for x in sorted(eu, key=lambda x: x["trade"]):
                print(f"  trade {x['trade']} settle {x['settle']} {x['term']:>3}d {x['cp'][:24]:<24} ${x['bn']:.3f}B @ {x['rate']}%  -> {grade(x)}")
        except Exception as e:
            o, oerr = None, f"{e.__class__.__name__}: {e}"[:200]
            print(f"NY Fed USD swap operations: GRADING FAILED ({oerr}) — OPS leg DOWN")
    if serr:
        print(f"FRED SWPT: FETCH OR FIELD CHECK FAILED ({serr}) — SWPT leg DOWN")
    elif s:
        try:
            d, v = s[-1]
            lab = swpt_grade(d, v) + (" (turn window)" if swpt_in_turn_window(d) else "")
            if (today - dt.date.fromisoformat(d)).days > MAX_SWPT_AGE_D:
                lab += f" — STALE (> {MAX_SWPT_AGE_D} days)"
            print(f"FRED SWPT (H.4.1, Wed level, ALL counterparties — global, not European): ${v:,.0f}M as-of {d} -> {lab}; prior: " +
                  ", ".join(f"{dd[5:]} {vv:,.0f}" for dd, vv in s[-5:-1]))
        except Exception as e:
            s, serr = None, f"{e.__class__.__name__}: {e}"[:200]
            print(f"FRED SWPT: GRADING FAILED ({serr}) — SWPT leg DOWN")
    else:
        print("FRED SWPT: no usable rows — SWPT leg DOWN")
    v, rc, _ = assess(o or [], s or [], today, oerr, serr)
    print(f"VERDICT (PROPOSED lines): {v}")
    return rc


def _prefixed(fn, *a):
    """Run fn with stdout captured; re-emit every line prefixed WITHHELD-TEST: (AC-D2 #3).
    Output is flushed even if fn raises."""
    buf = io.StringIO()
    rc = None
    try:
        with contextlib.redirect_stdout(buf):
            rc = fn(*a)
    finally:
        for line in buf.getvalue().splitlines():
            print(f"WITHHELD-TEST: {line}")
    return rc


def main(_argv=None):
    argv = sys.argv[1:] if _argv is None else _argv
    if "--selftest" in argv:
        return selftest()
    research = "--baserate" in argv or "--force-withheld-test" in argv
    if WITHHELD and not research:
        # refusal FIRST: no network call, no grade, no verdict line (CATO D2)
        print(f"⛔ {WITHHELD_WHY}")
        print("No reading is printed while WITHHELD. Isolated testing only: --selftest · --baserate · "
              f"--force-withheld-test (every line prefixed WITHHELD-TEST:, exit {RC_WITHHELD}).")
        return RC_WITHHELD
    fn, args = (baserate, ()) if "--baserate" in argv else (run_live, (dt.date.today(),))
    if not WITHHELD:
        return fn(*args)
    rc = _prefixed(fn, *args)
    print(f"WITHHELD-TEST: underlying rc {rc}; exit {RC_WITHHELD} because the instrument is {WITHHELD_WHY}")
    return RC_WITHHELD


if __name__ == "__main__":
    sys.exit(main())
