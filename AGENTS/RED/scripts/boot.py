#!/usr/bin/env python3
"""RED boot kit — live tape + trigger check + catalyst countdown + DUE-scan in one pass.

Usage:  .venv/bin/python3 AGENTS/RED/scripts/boot.py [--verbose]
        (bare python3 also works — self re-execs under the repo venv)

READ-ONLY by design: prints, never writes state. Data sources:
  prices/FRED  -> FORGE/tools/market-data/fetch.py (imported as a library)
  hard triggers-> AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv (WALTER auto-fire surface)
  watch lines  -> AGENTS/RED/docket/WATCHLINES.tsv (soft, display-only)
  catalysts    -> AGENTS/RED/docket/CATALYSTS.tsv
  DUE-scan     -> AGENTS/RED/workbook/PREDICTIONS.tsv + CHALLENGES.tsv

Mirrors SPAWN PROTOCOL boot steps 3 (DUE-scan, catalysts) + 9 (live anchors).
"""
import csv
import io
import os
import re
import sys
from datetime import date, datetime, timedelta
from decimal import Decimal, InvalidOperation
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]


def _ensure_venv():
    """Re-exec under the repo venv if yfinance is missing (PEP-668 system python)."""
    try:
        import yfinance  # noqa: F401
        return
    except ImportError:
        pass
    venv_py = REPO / ".venv" / "bin" / "python3"
    if venv_py.exists() and os.environ.get("RED_BOOT_REEXEC") != "1":
        os.environ["RED_BOOT_REEXEC"] = "1"
        os.execv(str(venv_py), [str(venv_py), __file__] + sys.argv[1:])
    sys.exit("yfinance unavailable and no repo venv found at .venv/ — cannot continue")


_ensure_venv()
sys.path.insert(0, str(REPO / "FORGE" / "tools" / "market-data"))
import fetch  # noqa: E402

RED = REPO / "AGENTS" / "RED"
TODAY = date.today()

# ⚠️ ^SKEW REMOVED from the yfinance tape 2026-09-06 (S41), on VIOLET's caveat via PROME.
# The GRADE path was re-pointed to CBOE earlier the same session, but the TAPE still printed a
# mirror-derived ^SKEW, unlabelled, directly above a trigger section grading off the publisher —
# so a reader could take the tape number as the graded one. Today they agree, which is exactly
# the condition under which the discrepancy is invisible. The tape now prints the CBOE bar with
# its own date (see section_tape), so tape and grade agree BY CONSTRUCTION rather than by luck.
# Census behind this: the mirror is defective on 4.31% of 9,221 sessions across three modes, and
# the dominant silent mode is FORWARD-FILL — it repeats its own prior value while CBOE moves,
# which on a sustain counter holds a broken run alive or kills a live one with no visible tell.
TICKERS = ["^VIX", "SPY", "KRE", "WAL", "OZK", "IWM", "TLT", "HYG", "BZ=F", "JPY=X", "^TNX"]
FRED_SERIES = [
    # VIXCLS added to the tape 2026-09-06: the canonical VIX close beside the live ^VIX quote, each
    # with its own source and date, so the graded value cannot be confused with the indicative one.
    ("VIXCLS", "VIX close (CBOE/FRED)", 1, ""),
    ("BAMLH0A0HYM2", "HY OAS", 100, "bps"),
    ("BAMLH0A3HYC", "CCC OAS", 100, "bps"),
    ("ICSA", "Initial Claims", 0.001, "K"),
    ("T5YIFR", "5y5y Breakeven", 1, "%"),
]
# registry metric vocabulary -> live-value resolution (units match registry: bps / K / level)
METRIC_MAP = {
    # ⚠️ RE-POINTED 2026-09-06 (S41) from ("yf","^VIX") to the DECLARED basis. FT-06's card has
    # said "FRED VIXCLS … only a published VIXCLS observation may COMPLETE a sustain count" since
    # 8/12, and the mismatch was DISCLOSED on the row that same day and then left unfixed for 25
    # days — a disclosed defect is not a fixed one. Triggered by WALTER SIG-W-20260906-003, which
    # found FT-06's fire record claimed TWO instruments where both legs were yfinance. FRED also
    # gives eval_line a real trail, so the sustain count is COMPUTED instead of "needs judgment".
    "VIX": ("fred", "VIXCLS", "value", 1),
    "HY-OAS": ("fred", "BAMLH0A0HYM2", "value", 100),
    "CCC-OAS": ("fred", "BAMLH0A3HYC", "value", 100),
    "BRENT-PAPER": ("yf", "BZ=F", "price", 1),
    "INITIAL-CLAIMS": ("fred", "ICSA", "value", 0.001),
    # FT-09 expectations-unanchor line (added 2026-08-12, audit R17 / PROME amendment 2 —
    # it sat 24bps from firing while rendering "unmapped metric, manual check" on WALTER's
    # auto-fire path. CORE-CPI-3MO-ANN (FT-08) stays unmapped by design: a release-derived
    # 3-month compound has no FRED series, and failing loud is correct for it.
    "BREAKEVEN-5Y5Y": ("fred", "T5YIFR", "value", 1),
    # FT-10 tail-bid-reload line. ⚠️ RE-POINTED 2026-09-06 (S41) FROM yfinance ^SKEW TO THE
    # CBOE CSV. FT-10's own instrument_basis_operative (declared under WQ-162 on 9/2)
    # DISQUALIFIES the yfinance mirror: it is "a PROVISIONAL SAME-DAY MIRROR ONLY ... cannot
    # complete a grade" (measured defect rate CORRECTED 2026-09-10 per COR-20260908-03 -- the published
    # 0.79%/session is WITHDRAWN: RED's 253-session window reproduces 0.40%/session, and the
    # full 9,221-session census gives 397 unique defective sessions = 4.31%. Two DISTINCT
    # perimeters -- never merge them, and the three defect categories OVERLAP. The 8/28 bar
    # omitted AND a 2025-12-24 value disagreement). For four days this tool graded a
    # registered trigger off the source its own registry forbids, and was correct only
    # because the two series happened to agree — guard correctness and guard WIRING are
    # independent properties. Bonus: the CSV is a real trail, so the sustain count is now
    # COMPUTED rather than deferred to "needs trail/judgment".
    "SKEW-CBOE": ("cboe", "SKEW", "close", 1),
}
NEAR_PCT = 0.03  # within 3% of threshold = NEAR

CBOE_SKEW_URL = "https://cdn.cboe.com/api/global/us_indices/daily_prices/SKEW_History.csv"
_CBOE_CACHE = {}


def cboe_skew():
    """(date_str, value) list, oldest-first, from the PUBLISHER OF RECORD.

    Fails LOUD and returns [] rather than falling back to the yfinance mirror: under
    FT-10's declared basis a provisional mirror CANNOT complete a grade, so a silent
    substitution would manufacture a gradeable-looking answer out of a disqualified
    source. An empty return renders "n/a / no data", which is the correct output.
    """
    if "rows" in _CBOE_CACHE:
        return _CBOE_CACHE["rows"]
    rows = []
    try:
        import urllib.request
        req = urllib.request.Request(CBOE_SKEW_URL, headers={"User-Agent": "Mozilla/5.0"})
        txt = urllib.request.urlopen(req, timeout=30).read().decode("utf-8-sig")
        for r in csv.reader(io.StringIO(txt)):
            if r and r[0][:1].isdigit():
                try:
                    rows.append((r[0], float(r[1])))
                except (ValueError, IndexError):
                    pass
    except Exception as e:                                    # noqa: BLE001
        print(f"   \u26a0\ufe0f  CBOE SKEW_History.csv UNREACHABLE ({type(e).__name__}) \u2014 FT-10 renders n/a. "
              f"The yfinance mirror is NOT substituted: it cannot complete a grade.")
    _CBOE_CACHE["rows"] = rows
    return rows


def _us_market_holidays(y):
    """Standard US equity-market holidays for year y (observed rule for fixed dates)."""
    def nth(m, wd, k):
        d = date(y, m, 1); d += timedelta(days=(wd - d.weekday()) % 7)
        return d + timedelta(weeks=k - 1)
    def last(m, wd):
        d = date(y, m, 31) if m != 5 else date(y, 5, 31)
        while d.weekday() != wd:
            d -= timedelta(days=1)
        return d
    def obs(d):
        return d - timedelta(days=1) if d.weekday() == 5 else (d + timedelta(days=1) if d.weekday() == 6 else d)
    a = y % 19; b_ = y // 100; c = y % 100; d_ = b_ // 4; e = b_ % 4
    f = (b_ + 8) // 25; g = (b_ - f + 1) // 3
    h = (19 * a + b_ - d_ - g + 15) % 30; i_ = c // 4; k_ = c % 4
    l = (32 + 2 * e + 2 * i_ - h - k_) % 7; mm = (a + 11 * h + 22 * l) // 451
    easter = date(y, (h + l - 7 * mm + 114) // 31, ((h + l - 7 * mm + 114) % 31) + 1)
    out = {obs(date(y, 1, 1)), obs(date(y, 7, 4)), obs(date(y, 12, 25)),
           nth(1, 0, 3), nth(2, 0, 3), last(5, 0), nth(9, 0, 1), nth(11, 3, 4),
           easter - timedelta(days=2)}
    if y >= 2021:
        out.add(obs(date(y, 6, 19)))
    return out


def _gap_reconciled(d1, d2):
    """True iff every weekday strictly between two CBOE bars is a market holiday.

    This is FT-10's declared clause made executable: a NON-SESSION (exchange closed)
    bridges the run; an UNRECONCILED MISSING SESSION breaks it. Weekends and holidays
    produce no bar and are expected; an unexplained weekday gap means the publisher had
    a session we cannot see, and the run may not be counted across it.
    """
    d = d1 + timedelta(days=1)
    while d < d2:
        if d.weekday() < 5 and d not in _us_market_holidays(d.year):
            return False, d
        d += timedelta(days=1)
    return True, None


def cboe_run_length(op, thr):
    """Consecutive most-recent CBOE bars satisfying op/thr, per FT-10's reset rule.

    ⚠️ REBUILT 2026-09-06 (S41) after CODEX found the v1 walked consecutive ROWS with no
    date logic at all — so a run of 9/3, 9/4, 9/9, 9/10 with the 9/8 session MISSING
    counted 4-of-4 and FIRED. That directly violates the clause RED had RULED the same
    morning ("an unreconciled missing session BREAKS the run, never bridges it"). I ruled
    the clause, wrote its test onto the card, and then shipped a counter that could not
    enforce the half I ruled on. Returns (run, rows, break_reason).
    """
    rows = cboe_skew()
    n = 0
    reason = None
    prev_date = None
    for ds, v in reversed(rows):
        try:
            cur = datetime.strptime(ds, "%m/%d/%Y").date()
        except ValueError:
            break
        if prev_date is not None:
            ok, missing = _gap_reconciled(cur, prev_date)
            if not ok:
                reason = f"UNRECONCILED MISSING SESSION {missing.isoformat()} — run may not be counted across it"
                break
        if not cmp_op(v, op, thr):
            break
        n += 1
        prev_date = cur
    return n, rows, reason


def tsv(path):
    with open(path, newline="") as f:
        rows = list(csv.reader(f, delimiter="\t"))
    head = rows[0]
    return [dict(zip(head, r)) for r in rows[1:] if r and len(r) >= len(head) - 2]


def pull_tape():
    prices = fetch.price_fetch(TICKERS)
    fred = {sid: fetch.fred_fetch(sid, limit=6) for sid, _, _, _ in FRED_SERIES}
    return prices, fred


def scaled(published, scale):
    """Scale a PUBLISHED value exactly, in decimal, never in binary float.

    WHY (DOCKET L258, DAEDALUS 2026-09-12; fixed S44 same day): every credit line is
    registered in bps but PUBLISHED by FRED in percent at 2dp, so the tool multiplies by
    100. In binary float `float("9.30") * 100 == 930.0000000000001`, which is `> 930`.
    RED-FT-07's letter is `CCC-OAS > 930` STRICT with sustain 1 — so a published 9.30
    print FIRED a band the letter says must not fire, on the first observation, with no
    sustain window to absorb it.

    NOT HYPOTHETICAL: `9.30` has printed 5 times in BAMLH0A3HYC's 787-observation history
    (2024-02-14, 2024-07-16, 2024-07-18, 2025-06-04, 2025-06-10) and all 787 observations
    publish at exactly 2dp, so the tie value sits squarely on the publication grid.

    Decimal multiplication on the published STRING is exact: Decimal("9.30") * 100 = 930.00.
    The float conversion afterwards is safe because the product is now an exact decimal that
    is representable. This is a CONFORMANCE repair, not a threshold change - it makes the
    instrument agree with the letter it was always supposed to implement.
    
    ⛔ NO FALLBACK BRANCH. A try/except here that returns `float(published) * float(scale)`
    RESTORES THE EXACT L258 DEFECT THIS FUNCTION EXISTS TO REMOVE: forced, it returns
    930.0000000000001, which fires RED-FT-07's `> 930` STRICT band that the letter says
    must not fire. And it buys nothing - it re-raises on the very inputs it was written
    for (None -> TypeError, "" -> ValueError), so behaviour on bad input is IDENTICAL
    with or without it. All it can ever do is convert a loud failure into a silent wrong
    number. Removed 2026-09-14 (S45) after DAEDALUS forced the branch and demonstrated the
    restoration; the twin fallback in ft11_delta5() was removed the same session for the
    same reason, caught there by this repair's own acceptance test rather than by review.
    ⚠️ An error handler whose fallback is the PRE-REPAIR behaviour is invisible in review
    BECAUSE A try/except READS AS CAUTION (DAEDALUS PAT-171). Bad input must raise here.
    """
    return float(Decimal(str(published)) * Decimal(str(scale)))


def live_value(src_type, key, field, scale, prices, fred):
    if src_type == "cboe":
        rows = cboe_skew()
        return scaled(rows[-1][1], scale) if rows else None
    if src_type == "yf":
        d = prices.get(key, {})
        v = d.get(field if field else "price")
        return scaled(v, scale) if v is not None else None
    obs = fred.get(key) or []
    if obs and "value" in obs[0]:
        return scaled(obs[0]["value"], scale)
    return None


def fred_trail(key, scale, fred, n):
    obs = fred.get(key) or []
    return [scaled(o["value"], scale) for o in obs[:n] if "value" in o]


def cmp_op(v, op, thr):
    # 2026-08-20 (S32): was `v > thr if op == ">" else v < thr` — every op that is not ">"
    # fell into "<", so FT-08/FT-10's ">=" would have evaluated SIGN-INVERTED (>=150 read
    # as <150 = false FIRING at 142.93). Caught at FT-10 registration, before data arrived.
    # Unknown op now fails loud rather than silently picking a branch. ML-RED-178.
    if op == ">":
        return v > thr
    if op == "<":
        return v < thr
    if op == ">=":
        return v >= thr
    if op == "<=":
        return v <= thr
    raise ValueError(f"unknown threshold_op {op!r}")


def eval_line(value, op, thr, sustain, src_type, key, scale, fred):
    """Return (status, detail). status in FIRING / NEAR / clear / n/a."""
    if value is None:
        return "n/a", "no data"
    thr = float(thr)
    hit = cmp_op(value, op, thr)
    dist = value - thr
    near = abs(dist) <= abs(thr) * NEAR_PCT
    sustain_n = int(sustain) if str(sustain).isdigit() else 1
    # thresholds are printed at the precision they were REGISTERED at: a .0f here rendered
    # FT-09's 2.55 as ">3" (2026-08-12) — a 24bp-away line reading as 69bp-away. Sub-unit
    # thresholds keep 2dp; bps/K thresholds stay integer so the credit lines read unchanged.
    thr_s = f"{thr:,.2f}" if abs(thr) < 100 and thr != int(thr) else f"{thr:,.0f}"
    # trail values print at the THRESHOLD's own precision. A '%.0f' here rendered VIXCLS 16.34 as
    # '16' beside a '<16' line — a value that BREAKS the run displayed as one that sits exactly ON
    # it. Same class as the S29e formatter defect already noted above: data right, representation
    # wrong, and the representation is what a consumer acts on. (S41 2026-09-06.)
    tf = (lambda x: f"{x:,.2f}") if abs(thr) < 100 else (lambda x: f"{x:,.0f}")
    detail = f"live {value:,.2f} vs {op}{thr_s} (dist {dist:+,.2f})"
    if src_type == "cboe":
        # The publisher of record IS the trail, so the sustain count is COMPUTED, never
        # deferred. Bar date is printed because this series publishes LAGGED — a value
        # without its bar date is the exact ambiguity that put "SKEW crossed 150" on the
        # tape two days before the publisher had spoken (SIG-W-20260903-001).
        run, rows, break_reason = cboe_run_length(op, thr)
        bar = rows[-1][0] if rows else "?"
        detail = f"live {value:,.2f} [CBOE bar {bar}] vs {op}{thr_s} (dist {dist:+,.2f})"
        if not hit:
            return ("NEAR" if near else "clear"), detail + f" — run 0-of-{sustain_n}"
        if run >= sustain_n:
            return "FIRING", detail + f" — SUSTAINED {run}-of-{sustain_n}" + (f" ⚠️ {break_reason}" if break_reason else "")
        start = rows[-run][0] if run else "?"
        gap = f" ⚠️ {break_reason}" if break_reason else ""
        return "FIRING*", detail + (f" — SATISFIED but COUNTING {run}-of-{sustain_n} "
                                    f"(run start {start}); NOT FIRED") + gap
    if hit and sustain_n > 1 and src_type == "fred":
        trail = fred_trail(key, scale, fred, sustain_n)
        if len(trail) >= sustain_n and all(cmp_op(t, op, thr) for t in trail):
            return "FIRING", detail + f" — sustained {sustain_n} obs {[tf(t) for t in trail]}"
        return "FIRING*", detail + f" — condition true, sustain {sustain_n} NOT yet met (trail {[tf(t) for t in trail]})"
    if hit:
        tag = "" if sustain_n == 1 and str(sustain).isdigit() else f" — sustain '{sustain}' needs trail/judgment"
        return "FIRING", detail + tag
    if near:
        return "NEAR", detail
    return "clear", detail


ICON = {"FIRING": "🔴", "FIRING*": "🟠", "NEAR": "🟡", "clear": "🟢", "n/a": "⚪"}


def section_tape(prices, fred):
    print("\n① TAPE — live anchors", TODAY.isoformat())
    for t in TICKERS:
        d = prices.get(t, {})
        if "error" in d:
            print(f"   ⚪ {t:<7} ERROR {d['error'][:50]}")
            continue
        chg = d.get("change_pct")
        print(f"   {d.get('name', t):<22} {d.get('price', '?'):>10,.2f}  {('%+.2f%%' % chg) if chg is not None else '':>8}")
    rows = cboe_skew()
    if rows:
        bar, v = rows[-1]
        prev = rows[-2][1] if len(rows) > 1 else None
        chg = f" ({v - prev:+.2f})" if prev is not None else ""
        print(f"   {'^SKEW (CBOE, publisher)':<22} {v:>10,.2f}{chg}  [CBOE bar {bar}]")
    else:
        print(f"   {'^SKEW (CBOE, publisher)':<22} {'n/a':>10}  — publisher unreachable; mirror NOT substituted")
    for sid, label, scale, unit in FRED_SERIES:
        obs = fred.get(sid) or []
        if obs and "value" in obs[0]:
            v = float(obs[0]["value"]) * scale
            prev = float(obs[1]["value"]) * scale if len(obs) > 1 else None
            dp = 2 if abs(v) < 100 else 0   # sub-100 series (breakevens, yields) need decimals; bps/K do not
            delta = f" ({v - prev:+,.{dp}f})" if prev is not None else ""
            print(f"   {label:<22} {v:>10,.{dp}f}{unit}{delta}  [FRED {obs[0]['date']}]")


def section_triggers(prices, fred, verbose):
    print("\n② TRIGGER CHECK")
    print("   — registry (hard, WALTER auto-fire) —")
    for r in tsv(RED / "registry" / "FALSIFICATION_TRIGGERS.tsv"):
        m = METRIC_MAP.get(r["metric"])
        if not m:
            print(f"   ⚪ {r['trigger_id']:<10} {r['metric']} — unmapped metric, manual check")
            continue
        v = live_value(*m, prices, fred)
        status, detail = eval_line(v, r["threshold_op"], r["threshold_value"], r["sustain_window"], m[0], m[1], m[3], fred)
        print(f"   {ICON[status]} {r['trigger_id']:<10} {r['metric']} {r['threshold_op']}{r['threshold_value']} s={r['sustain_window']:<2} {status:<8} {detail}")
    print("   — watch lines (soft, docket/WATCHLINES.tsv) —")
    for r in tsv(RED / "docket" / "WATCHLINES.tsv"):
        v = live_value(r["Source_Type"], r["Source_Key"], r["Field"], r["Scale"], prices, fred)
        status, detail = eval_line(v, r["Op"], r["Threshold"], r["Sustain"], r["Source_Type"], r["Source_Key"], r["Scale"], fred)
        line = f"   {ICON[status]} {r['WL_ID']:<10} {r['Metric']} {r['Op']}{r['Threshold']:<7} {status:<8} {detail} — {r['Label']}"
        print(line if not verbose else line + f"  [{r['Notes']}]")


def parse_fuzzy_date(s):
    """Return (date, exact) or (None, None) if unparseable."""
    s = s.strip()
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", s)
    if m:
        return date(*map(int, m.groups())), True
    m = re.match(r"^(\d{4})-(\d{2})-(early|mid|late|XX)$", s, re.I)
    if m:
        day = {"early": 5, "mid": 15, "late": 25, "xx": 15}[m.group(3).lower()]
        return date(int(m.group(1)), int(m.group(2)), day), False
    m = re.match(r"^([A-Za-z]{3,9})\s+(\d{4})$", s)  # "Jun 2026"
    if m:
        try:
            mo = datetime.strptime(m.group(1)[:3], "%b").month
            nxt = date(int(m.group(2)) + (mo == 12), (mo % 12) + 1, 1)
            return date.fromordinal(nxt.toordinal() - 1), False  # end of month
        except ValueError:
            return None, None
    m = re.search(r"Q([1-4])(?:-Q([1-4]))?\s+(\d{4})", s)  # "Q2 2026" / "Q2-Q3 2026"
    if m:
        q = int(m.group(2) or m.group(1))
        return date(int(m.group(3)), q * 3, [31, 30, 30, 31][q - 1]), False
    return None, None


def section_catalysts(verbose):
    print("\n③ CATALYST COUNTDOWN (pending, ≤14d" + (" — verbose: all" if verbose else "") + ")")
    for r in tsv(RED / "docket" / "CATALYSTS.tsv"):
        if not r.get("status", "").startswith("pending"):
            continue
        d, exact = parse_fuzzy_date(r["date"])
        if d is None:
            print(f"   ⚪ {r['date']:<12} {r['event'][:60]} — unparseable date, manual check")
            continue
        days = (d - TODAY).days
        if days > 14 and not verbose:
            continue
        approx = "" if exact else "~"
        if days < 0:  # S50: was printed as "⏰ T--13", easy to read past; a pending row with a past date is owed an outcome
            print(f"   🔴 OVERDUE {-days}d {r['date']:<12} {r.get('priority', '')} {r['event'][:66]} — resolve with outcome")
            continue
        flag = "⏰" if days <= 2 else "  "
        print(f"   {flag} T-{approx}{days:<3} {r['date']:<12} {r.get('priority', '')} {r['event'][:70]}")


def section_due_scan():
    print("\n④ DUE-SCAN (boot step 3 / resolve at W2)")
    due = manual = 0
    for r in tsv(RED / "workbook" / "PREDICTIONS.tsv"):
        if r.get("Status") != "ACTIVE":
            continue
        d, _ = parse_fuzzy_date(r.get("Timeframe", ""))
        if d is None:
            manual += 1
            print(f"   ⚠️  {r['Pred_ID']} timeframe '{r['Timeframe']}' unparseable — MANUAL CHECK")
        elif d < TODAY:
            due += 1
            print(f"   🔴 {r['Pred_ID']} DUE since {d} ({(TODAY - d).days}d): {r['Prediction'][:60]}")
    if due == 0 and manual == 0:
        print("   🟢 predictions: no ACTIVE row past its timeframe")
    # S50 2026-10-01: every NON-RESOLVED row, not just tokens containing "ACTIVE" — five rows
    # (RE-TARGETED / WEAKENED / STRENGTHENED-IN-FLIGHT) sat invisible 101-122d under the old filter.
    # Resolved_Date's leading YYYY-MM-DD is read as the re-review date; past ⇒ 🔴, absent ⇒ 🔴 (ML-125).
    print("   — open challenges (every non-RESOLVED status; leading Resolved_Date = re-review) —")
    for r in tsv(RED / "workbook" / "CHALLENGES.tsv"):
        if r.get("Status", "").startswith("RESOLVED"):
            continue
        try:
            age = (TODAY - datetime.strptime(r["Date"], "%Y-%m-%d").date()).days
        except ValueError:
            age = "?"
        m = re.match(r"\s*(\d{4}-\d{2}-\d{2})", r.get("Resolved_Date", ""))
        if not m:
            mark, when = "🔴", "NO re-review date"
        else:
            rd = date.fromisoformat(m.group(1))
            mark, when = ("🔴", f"re-review PASSED {rd} ({(TODAY - rd).days}d)") if rd < TODAY else ("•", f"re-review {rd}")
        print(f"   {mark} {r['CHG_ID']} [{r['Status']}] ({age}d, {when}, {r['Target'][:40]}): {r['Key_Finding'][:60]}")
    # S50: TRIGGER_OUTCOMES rows past resolve_after and still UNRESOLVED (FT-06 sat 22d ungraded).
    for r in tsv(RED / "registry" / "TRIGGER_OUTCOMES.tsv"):
        if not r.get("outcome", "").startswith("UNRESOLVED"):
            continue
        m = re.search(r"(\d{4}-\d{2}-\d{2})", r.get("resolve_after", ""))
        if m and date.fromisoformat(m.group(1)) < TODAY:
            rd = date.fromisoformat(m.group(1))
            print(f"   🔴 OUTCOME {r['trigger_id']} fire {r['fire_date']} — resolve_after {rd} PASSED ({(TODAY - rd).days}d), still {r['outcome']}")


def _red_addressed(head):
    """True if a BOARD signal's frontmatter routes an ACTION to RED.

    Reads BOTH routing keys: v0.12+ `action:` and the legacy `to:` used by
    585 April-July files. Three value forms occur in the corpus and all three
    are handled: bracketed list (quoted or bare), bare scalar, and
    `NAME (annotation...)`. Matching is WHOLE-TOKEN, so RED never matches
    inside REDACTED or any longer word.
    """
    for line in head.splitlines():
        key, sep, val = line.partition(":")
        if not sep or key.strip().lower() not in ("action", "to"):
            continue
        val = val.strip().strip("[]")
        for piece in val.split(","):
            tok = piece.strip().strip('"\'').split("(")[0].strip()
            if tok.upper() == "RED":
                return True
    return False


def _logged_ids():
    """Every SIG-W id appearing in ANY RED BOARD ledger — live plus archives.

    Reads the live board_log.tsv AND archive/board_log*.tsv, because the
    2026-09-10 rotation moved 36 dispositions out of the live file and a
    live-file-only reader re-reports every one of them as unlogged.
    Comment lines and the header row are skipped; ids are matched anywhere
    in the row, so an `id + slug` cell counts as a disposition.
    """
    ids, files = set(), []
    for p in [RED / "board_log.tsv", *sorted((RED / "archive").glob("board_log*.tsv"))]:
        if not p.is_file():
            continue
        files.append(p)
        for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
            if line.startswith("#") or line.startswith("timestamp_read"):
                continue
            ids.update(re.findall(r"SIG-W-\d{8}-\d{3}", line))
    return ids, files


def section_board_gap(verbose):
    """(5) BOARD-vs-board_log gap — the boot-1.5 disposition obligation, made checkable.

    WHY THIS AND NOT A STALENESS ALERT (audit R6, S30 2026-08-12): board_log.tsv is
    EXCLUDED fleet-wide from ledger_staleness's outside-glob warning by design, and
    staleness is the wrong signal anyway - it cannot tell "no signals arrived" from
    "signals arrived and went unlogged", and would false-fire in any quiet week.

    *** REBUILT AS AN ID-DIFF, S44 2026-09-12. The previous implementation reported
    GREEN while 27 action-addressed signals sat unlogged, the oldest 154 days. Three
    independent defects, each sufficient on its own:

      (1) HEADER READ AS DATA. It sliced `[1:]` to drop ONE leading line, but after the
          2026-09-10 rotation line 0 is a `#` comment and line 1 is the HEADER. So
          `max(timestamp_read)` compared the literal string "timestamp_read", which
          sorts ABOVE every "2026-.." date. Every signal then satisfied `d <= last`
          and the gate was HARD-WIRED GREEN - not merely lossy, unconditionally blind.
      (2) DATE FLOOR. Even with a correct `last`, it only examined files dated AFTER
          the newest disposition, so logging ANY recent signal hid every older
          unlogged one. Newest-vs-newest cannot answer a set question.
      (3) LIVE LEDGER ONLY. It never read archive/board_log*.tsv, so the rotation
          would have re-flagged 36 already-dispositioned signals.

    The replacement is a SET DIFFERENCE with NO DATE FLOOR: {BOARD ids routing an
    action to RED} minus {ids in every RED ledger}. It also reads the legacy `to:`
    routing key, absent from the old matcher entirely.

    Cross-checked against PROME/tools/exempt_gap.py --desks RED, an INDEPENDENT
    implementation over the same corpus - a different perimeter agreeing on the
    same count, not a matching absolute (finding_crosscheck_with_free_parameter).
    """
    print("\n(5) BOARD DISPOSITION GAP (boot 1.5 obligation - log what you consume)")
    # S50: size of the live ledger, every boot (three breaches S44-S46 by sessions that had read the warning).
    # Append ONLY via scripts/board_log_append.py, which REFUSES at >=75%; this line shows the state.
    _bl = (RED / "board_log.tsv").stat().st_size if (RED / "board_log.tsv").is_file() else 0
    _pct = _bl / 32550
    _mk = "🔴 OVER rotation line - run board_log_append.py --rotate" if _pct >= 0.75 else ("⚠️  rotate at closeout (--rotate)" if _pct >= 0.60 else "OK")
    print(f"   board_log.tsv size: {_bl:,} B = {_pct:.1%} of 32,550  {_mk}  [append via scripts/board_log_append.py]")
    try:
        logged, ledgers = _logged_ids()
    except OSError:
        print("   WARN board_log unreadable - cannot grade the disposition obligation")
        return
    if not ledgers:
        print("   WARN no RED BOARD ledger found - a desk with no ledger owes one")
        return
    board = REPO / "BOARD"
    sigs = sorted(board.glob("SIG-W-*.md")) if board.is_dir() else []
    if not sigs:
        print("   WARN BOARD/ not found or empty - cannot grade")
        return
    today, addressed, unrouted = date.today(), [], 0
    for p in sigs:
        m = re.match(r"(SIG-W-(\d{4})(\d{2})(\d{2})-\d{3})", p.name)
        if not m:
            continue
        try:
            head = p.read_text(encoding="utf-8", errors="replace")[:2000]
        except OSError:
            continue
        if not re.search(r"^\s*(action|to)\s*:", head, re.M):
            unrouted += 1
            continue
        if not _red_addressed(head):
            continue
        sid = m.group(1)
        age = (today - date(int(m.group(2)), int(m.group(3)), int(m.group(4)))).days
        if sid not in logged:
            addressed.append((age, sid, p.name))
    addressed.sort(key=lambda r: -r[0])
    print(f"   ledgers read      : {len(ledgers)} ({sum(1 for f in ledgers if 'archive' in str(f))} archived)"
          f" - {len(logged)} ids logged")
    print(f"   BOARD signals     : {len(sigs)} scanned, {unrouted} carry no routing key")
    if not addressed:
        print("   OK  every action-addressed BOARD signal has a disposition row")
        return
    aged = [a for a in addressed if a[0] >= 2]
    print(f"   ALERT {len(addressed)} action-addressed signal(s) UNLOGGED"
          f" - {len(aged)} aged >=2d, oldest {addressed[0][0]}d")
    for age, sid, name in (addressed if verbose else addressed[:8]):
        print(f"      {sid}  {age:>4}d  {name[:64]}")
    if not verbose and len(addressed) > 8:
        print(f"      ... +{len(addressed) - 8} more (--verbose)")
    print("   -> append a row per id to board_log.tsv"
          " (timestamp/signal_id/disposition/source/notes); one word is a legitimate row")


def main():
    verbose = "--verbose" in sys.argv
    print("=" * 72)
    print(" RED BOOT KIT — " + datetime.now().strftime("%Y-%m-%d %H:%M ET-local"))
    print("=" * 72)
    prices, fred = pull_tape()
    section_tape(prices, fred)
    section_triggers(prices, fred, verbose)
    section_catalysts(verbose)
    section_due_scan()
    section_board_gap(verbose)
    print("\nDone. (read-only — no state written; resolve DUE rows at W2)")


if __name__ == "__main__":
    main()
