#!/usr/bin/env python3
"""
LIQUID Boot — live 3-dashboard sweep (Credit / Domestic / Foreign) in one command.

Pulls every load-bearing LIQUID figure from primary sources (FRED + yfinance via
FORGE/tools/market-data/fetch.py), classifies each against LIQUID thresholds, and
prints an alert-collapsed boot brief. Replaces ~13 manual `fetch.py` calls.

Alert labels are tied to LIQUID's actual thesis triggers (KILL / CONFIRM /
PRE-TRIGGER / TRIGGER-A / UNWIND / co-trigger), not invented independently.

⚠️  Run with the venv (yfinance lives there):
      .venv/bin/python3 AGENTS/LIQUID/scripts/boot.py
      .venv/bin/python3 AGENTS/LIQUID/scripts/boot.py --verbose   # every value + 6-print trend
      .venv/bin/python3 AGENTS/LIQUID/scripts/boot.py --quick     # FRED only (skip slow yfinance)
      .venv/bin/python3 AGENTS/LIQUID/scripts/boot.py --selftest  # validate CATALYSTS/PREDICTIONS/KB + fetch import

Basis canon (declare when citing a number downstream): FRED OAS / H.15 are end-of-day
computed and publish T+1 — the latest print may be 1-2 sessions back, more over a
weekend. yfinance = last close (raw). Brent BZ=F front-month is NOT the ICE settle;
USD/JPY JPY=X is NOT the 5pm-ET NY close. H.4.1 series (WRESBAL) are dated by their
as-of Wednesday. Verify load-bearing triggers against the canonical basis before acting.

Exit code = FETCH health only (non-zero if any series failed to pull) — NOT alert state:
a red thesis trigger (HY <260, USD/JPY >160, SRF >50) still exits 0. Parse stdout for alerts.
"""

import calendar
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
LIQUID_DIR = SCRIPTS_DIR.parent                    # AGENTS/LIQUID
WORKSPACE = SCRIPTS_DIR.parents[2]                 # AGENTS/LIQUID/scripts -> Research-workspace
FETCH_DIR = WORKSPACE / "FORGE" / "tools" / "market-data"
sys.path.insert(0, str(FETCH_DIR))

try:
    from fetch import fred_fetch, price_fetch
except Exception as e:                              # pragma: no cover
    print(f"FATAL: cannot import FORGE fetch.py from {FETCH_DIR}: {e}")
    sys.exit(2)

RESULTS = []   # list of row dicts: dashboard,label,display,marker,note,asof,trend,headline
ERRORS = 0


def add(dashboard, label, display, marker, note, asof="", trend="", headline=False):
    RESULTS.append(dict(dashboard=dashboard, label=label, display=display, marker=marker,
                        note=note, asof=asof, trend=trend, headline=headline))


def fred_series(sid, n=6):
    """Return (latest_float, asof_date, [recent floats newest-first], error_or_None)."""
    global ERRORS
    obs = fred_fetch(sid, limit=n)
    if not obs or (isinstance(obs[0], dict) and "error" in obs[0]):
        ERRORS += 1
        return None, None, [], (obs[0]["error"] if obs else "no data")
    vals = []
    for o in obs:
        try:
            vals.append(float(o["value"]))
        except (ValueError, KeyError, TypeError):
            pass
    if not vals:
        ERRORS += 1
        return None, None, [], "no numeric values"
    return vals[0], obs[0]["date"], vals, None


def trend_str(vals, mult=1.0, dp=0):
    return " → ".join(f"{v * mult:.{dp}f}" for v in reversed(vals[:6]))


# ---------------------------------------------------------------------------
# Dashboard 1 — CREDIT SPREADS
# ---------------------------------------------------------------------------

def build_credit():
    ccc = bb = None  # for the CCC-BB tail-gap composite

    # HY OAS (macro) — kill <260 / confirm >320  [headline]
    v, d, tr, err = fred_series("BAMLH0A0HYM2")
    if err:
        add("CREDIT", "HY OAS", "ERR", "🔴", f"fetch error: {err}", headline=True)
    else:
        bps = v * 100
        if bps < 260:   m, n = "🔴", "KILL (<260) — credit-channel thesis kill; escalate ALL"
        elif bps < 265: m, n = "🟠", "TRIGGER-A zone (<265 ×2 sessions = cut credit-thesis to half)"
        elif bps < 270: m, n = "🟡", "PRE-TRIGGER (<270): re-read positions, check duration channel"
        elif bps > 320: m, n = "🔴", "CONFIRMATION (>320) — credit transmission; escalate ALL"
        elif bps > 300: m, n = "🟠", "approaching 320 confirmation"
        else:           m, n = "🟢", f"cushion {bps - 260:.0f}bps to 260 kill / {320 - bps:.0f}bps to 320 confirm"
        add("CREDIT", "HY OAS", f"{bps:.0f}bps", m, n, d, trend_str(tr, 100, 0), headline=True)

    # CCC OAS — >1000 trip
    v, d, tr, err = fred_series("BAMLH0A3HYC")
    if not err:
        ccc = v * 100
        if ccc > 1000:  m, n = "🔴", "CCC tail >1000 trip"
        elif ccc > 960: m, n = "🟡", f"{1000 - ccc:.0f}bps below 1000 trip"
        else:           m, n = "🟢", ""
        add("CREDIT", "CCC OAS", f"{ccc:.0f}bps", m, n, d, trend_str(tr, 100, 0))
    else:
        add("CREDIT", "CCC OAS", "ERR", "🟠", f"fetch error: {err}")

    # BB OAS — feeds the CCC-BB tail-gap (NEXUS R3 pin)
    v, d, tr, err = fred_series("BAMLH0A1HYBB")
    if not err:
        bb = v * 100
        add("CREDIT", "BB OAS", f"{bb:.0f}bps", "🟢", "(feeds CCC-BB gap)", d, trend_str(tr, 100, 0))
    else:
        add("CREDIT", "BB OAS", "ERR", "🟠", f"fetch error: {err}")

    # CCC-BB tail-gap — NEXUS R3 / KB-LIQ-058 pin; falsifier <~400  [headline]
    if ccc is not None and bb is not None:
        gap = ccc - bb
        if gap < 400:   m, n = "🔴", "PIN BROKEN (<400) — bifurcation falsified (NEXUS R3 falsifier)"
        elif gap < 500: m, n = "🟠", "tail-gap compressing toward the <400 falsifier"
        else:           m, n = "🟢", "pin INTACT — quality bifurcation wide (KB-LIQ-058)"
        add("CREDIT", "CCC-BB gap", f"{gap:.0f}bps", m, n, "", "", headline=True)
    else:
        # never let the headline pin silently vanish on a CCC/BB fetch failure
        add("CREDIT", "CCC-BB gap", "N/A", "🟠",
            "gap UNAVAILABLE — CCC or BB fetch failed (headline pin missing this boot)", headline=True)

    # IG OAS — reference, no LIQUID trigger
    v, d, tr, err = fred_series("BAMLC0A0CM")
    if not err:
        add("CREDIT", "IG OAS", f"{v * 100:.0f}bps", "🟢", "(reference — benign)", d, trend_str(tr, 100, 0))


# ---------------------------------------------------------------------------
# Dashboard 2 — DOMESTIC PLUMBING
# ---------------------------------------------------------------------------

def build_domestic():
    sofr = iorb = None

    v, d, tr, err = fred_series("SOFR")
    if not err:
        sofr = v
        m, n = ("🟠", "above 3.70") if v > 3.70 else ("🟢", "")
        add("DOMESTIC", "SOFR", f"{v:.2f}%", m, n, d, trend_str(tr, 1, 2))

    v, d, tr, err = fred_series("IORB")
    if not err:
        iorb = v
        add("DOMESTIC", "IORB", f"{v:.2f}%", "🟢", "(ceiling ref)", d)

    # SOFR-IORB spread — sustained >0 = funding stress
    if sofr is not None and iorb is not None:
        spr = (sofr - iorb) * 100
        if spr > 0:  m, n = "🟠", "ABOVE ceiling (>0) — re-open KB-LIQ-051 (verify non-mechanical, 3+ sessions)"
        else:        m, n = "🟢", "negative/clean — no funding stress"
        add("DOMESTIC", "SOFR-IORB", f"{spr:+.0f}bps", m, n)

    # 2Y — front-end reference (FOMC-day hawkish reprice tell)
    v, d, tr, err = fred_series("DGS2")
    if not err:
        add("DOMESTIC", "2Y (DGS2)", f"{v:.2f}%", "🟢", "(front-end ref / bear-flattener tell)", d, trend_str(tr, 1, 2))

    # 10Y — >4.50 sustained
    v, d, tr, err = fred_series("DGS10")
    if not err:
        m, n = ("🟠", "ABOVE 4.50 pivot") if v > 4.50 else ("🟢", "below 4.50 pivot")
        add("DOMESTIC", "10Y (DGS10)", f"{v:.2f}%", m, n, d, trend_str(tr, 1, 2))

    # 30Y — >5.00 re-establish / <4.90 unwind  [headline]
    v, d, tr, err = fred_series("DGS30")
    if not err:
        if v > 5.00:    m, n = "🟠", "ABOVE 5.00 — duration regime re-establishing (need ≥5 closes)"
        elif v < 4.90:  m, n = "🟠", "BELOW 4.90 — duration UNWIND test firing"
        else:           m, n = "🟢", f"5.00-pivot oscillation ({v - 4.90:.2f} above the 4.90 unwind)"
        add("DOMESTIC", "30Y (DGS30)", f"{v:.2f}%", m, n, d, trend_str(tr, 1, 2), headline=True)

    # Reserves WRESBAL ($ millions on FRED) — <2.8T floor. Canonical WRESBAL only —
    # NOT the FFIEC bank-reported reserves figure (different measure; see STATUS 6/20).
    v, d, tr, err = fred_series("WRESBAL")
    if not err:
        t = v / 1e6  # $millions -> $T
        m, n = ("🟠", "BELOW $2.8T floor — escalate PROME") if t < 2.8 else ("🟢", f"cushion ${(t - 2.8) * 1000:.0f}B above floor")
        add("DOMESTIC", "Reserves", f"${t:.3f}T", m, n, d + " (as-of Wed)")

    # RRP (billions) — >5 signal; structural zero now
    v, d, tr, err = fred_series("RRPONTSYD")
    if not err:
        m, n = ("🟡", "ABOVE $5B — buffer re-activating? (check sustained vs month-end noise)") if v > 5 else ("🟢", "structural zero")
        add("DOMESTIC", "RRP", f"${v:.2f}B", m, n, d)

    # SRF = Treasury leg + MBS leg (billions) — >50 stress
    t_v, t_d, _, t_err = fred_series("RPONTSYD")
    m_v, m_d, _, m_err = fred_series("RPONMBSD")
    if not t_err and not m_err:
        srf = t_v + m_v
        note = "no funding stress (both legs)" if srf <= 50 else "ABOVE $50B — escalate REGINALD/HENRY/PROME"
        if t_d != m_d:
            note += f" [legs differ: T {t_d} / MBS {m_d}]"
        add("DOMESTIC", "SRF usage", f"${srf:.2f}B", "🔴" if srf > 50 else "🟢", note, max(t_d, m_d))
    else:
        leg = f"T ${t_v:.2f}B" if not t_err else f"MBS ${m_v:.2f}B" if not m_err else "neither leg"
        add("DOMESTIC", "SRF usage", "PARTIAL", "🟠", f"leg fetch failed — only {leg} available")


# ---------------------------------------------------------------------------
# Dashboard 3 — FOREIGN OFFICIAL + position/vol prices (yfinance)
# ---------------------------------------------------------------------------

PRICE_SPECS = [
    # ticker, dashboard, label, check(price) -> (marker, note)
    ("APO",  "CREDIT",  "APO",     lambda p: ("🟡", "co-trigger satisfied (>$130) — NOT Trigger C absent HY compression") if p > 130 else ("🟢", "below $130 co-trigger")),
    ("BIZD", "CREDIT",  "BIZD",    lambda p: ("🟡", "above $12.50 mark-stress line") if p > 12.50 else ("🟢", "below $12.50")),
    ("^VIX", "CREDIT",  "VIX",     lambda p: ("🟠", ">25") if p > 25 else (("🟡", "elevated >20") if p > 20 else ("🟢", "calm"))),
    ("HYG",  "CREDIT",  "HYG",     lambda p: ("🟢", "(price ref — HY ETF)")),
    ("TLT",  "DOMESTIC", "TLT",    lambda p: ("🟢", "(price ref — 20Y+ UST)")),
    ("JPY=X", "FOREIGN", "USD/JPY", lambda p: ("🔴", "TRIGGERED (>160) — awaiting flow confirm (SAM owns)") if p > 160 else ("🟢", "below 160")),
    ("BZ=F", "FOREIGN", "Brent",    lambda p: ("🟢", "(price ref — BZ=F ≠ ICE settle)")),
]


def build_prices():
    global ERRORS
    tickers = [s[0] for s in PRICE_SPECS]
    try:
        res = price_fetch(tickers)
    except ModuleNotFoundError as e:
        print(f"  ⚠️  yfinance unavailable ({e}) — re-run with .venv/bin/python3 for prices (FRED dashboards still render below).")
        return
    except Exception as e:
        print(f"  ⚠️  price fetch failed: {e} (FRED dashboards still render below).")
        return
    for ticker, dash, label, check in PRICE_SPECS:
        d = res.get(ticker, {})
        if "error" in d:
            ERRORS += 1
            add(dash, label, "ERR", "🟠", f"fetch error: {str(d['error'])[:40]}")
            continue
        p = d["price"]
        chg = d.get("change_pct")
        m, n = check(p)
        disp = f"{p:,.2f}" if (label in ("USD/JPY",) or p >= 1000) else f"${p:,.2f}"
        if chg is not None:
            disp += f" ({chg:+.2f}%)"
        head = label in ("USD/JPY",)
        add(dash, label, disp, m, n, "last close", headline=head)


# ---------------------------------------------------------------------------
# Forward state — catalyst countdown + predictions due-scan
# ---------------------------------------------------------------------------

def _trading_days(start, end):
    """Weekdays strictly after `start` through `end` inclusive (US holidays ignored)."""
    if end <= start:
        return 0
    n, cur = 0, start + timedelta(days=1)
    while cur <= end:
        if cur.weekday() < 5:
            n += 1
        cur += timedelta(days=1)
    return n


def catalyst_countdown(horizon=60):
    """Print dated catalysts within `horizon` days. Returns count flagged imminent (<=5 trd)."""
    path = LIQUID_DIR / "workbook" / "CATALYSTS.tsv"
    if not path.exists():
        print("    (no workbook/CATALYSTS.tsv)")
        return 0
    rows = path.read_text().splitlines()
    if len(rows) < 2:
        print("    (CATALYSTS.tsv empty)")
        return 0
    hdr = rows[0].split("\t")
    today = datetime.now().date()
    cutoff = today + timedelta(days=horizon)
    upcoming, unparsed = [], 0
    for ln in rows[1:]:
        parts = ln.split("\t")
        if len(parts) != len(hdr):
            unparsed += 1   # wrong field count -> would render misaligned; flag, don't skip silently
            continue
        c = dict(zip(hdr, parts))
        try:
            ed = datetime.strptime(c.get("date", ""), "%Y-%m-%d").date()
        except ValueError:
            unparsed += 1   # fail loud — a malformed date silently drops from the countdown
            continue
        if today <= ed <= cutoff:
            upcoming.append((ed, c))
    if unparsed:
        print(f"    ⚠️  {unparsed} malformed row(s) (bad date or field count) — fix CATALYSTS.tsv (silently skipped otherwise)")
    if not upcoming:
        print(f"    no dated catalysts within {horizon}d")
        return 0
    upcoming.sort(key=lambda x: x[0])
    imminent = 0
    for ed, c in upcoming:
        trd = _trading_days(today, ed)
        cal = (ed - today).days
        mk = "~" if c.get("date_class", "").strip() == "modeled" else " "
        pri = c.get("priority", "").strip() or "  "
        flag = "  ⏰ IMMINENT" if trd <= 5 else ""
        if trd <= 5:
            imminent += 1
        print(f"    {pri} {mk}{c['date']} {ed.strftime('%a')}  {cal:>3}d cal /{trd:>3}d trd  {c.get('event', '')[:50]}{flag}")
    return imminent


_MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
# full month names also accepted; the parser requires the WHOLE word be a month, so 'Junk' != 'Jun'
_MONTH_WORDS = dict(_MONTHS)
_MONTH_WORDS.update({m: i for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june", "july", "august",
     "september", "october", "november", "december"], 1)})


def _parse_timeframe(tf):
    """Best-effort resolve-date from a free-text Timeframe. Returns (date|None, parsed_bool)."""
    tf = (tf or "").strip()
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", tf)             # explicit ISO
    if m:
        try:
            return date(*map(int, m.groups())), True
        except ValueError:
            pass
    m = re.search(r"H([12])\s*(\d{4})", tf)                   # H1/H2 YYYY
    if m:
        y = int(m.group(2))
        return (date(y, 6, 30) if m.group(1) == "1" else date(y, 12, 31)), True
    m = re.search(r"Q([1-4])\s*(\d{4})", tf)                  # Q1-Q4 YYYY
    if m:
        y = int(m.group(2))
        return date(y, *{1: (3, 31), 2: (6, 30), 3: (9, 30), 4: (12, 31)}[int(m.group(1))]), True
    m = re.search(r"\b([A-Za-z]{3,9})\b\.?\s*(?:(\d{1,2})\s*-\s*(\d{1,2}))?\s*,?\s*(\d{4})", tf)  # Month [DD-DD] YYYY
    if m and m.group(1).lower() in _MONTH_WORDS:   # whole word must BE a month ('Junk' rejected)
        mo, y = _MONTH_WORDS[m.group(1).lower()], int(m.group(4))
        last = calendar.monthrange(y, mo)[1]
        day = min(int(m.group(3)), last) if m.group(3) else last
        return date(y, mo, day), True
    return None, False


def predictions_scan():
    """Flag OPEN predictions whose timeframe is due/overdue. Returns overdue count."""
    path = LIQUID_DIR / "workbook" / "PREDICTIONS.tsv"
    if not path.exists():
        print("    (no workbook/PREDICTIONS.tsv)")
        return 0
    rows = path.read_text().splitlines()
    if len(rows) < 2:
        print("    (PREDICTIONS.tsv empty)")
        return 0
    hdr = rows[0].split("\t")
    today = datetime.now().date()
    open_rows = [d for d in (dict(zip(hdr, ln.split("\t"))) for ln in rows[1:])
                 if d.get("Status", "").strip().upper() == "OPEN"]
    if not open_rows:
        print("    ✓ no OPEN predictions")
        return 0
    overdue = 0
    for p in open_rows:
        pid, tf, pred = p.get("Pred_ID", "?"), p.get("Timeframe", ""), p.get("Prediction", "")[:52]
        due, parsed = _parse_timeframe(tf)
        if not parsed:
            print(f"    ⚠️  {pid}: OPEN — timeframe '{tf}' unparsed; check manually — {pred}")
            continue
        d = (due - today).days
        if d < 0:
            overdue += 1
            print(f"    🔴 {pid}: OVERDUE {-d}d (resolve now — don't let it rot like LIQ-02) — {pred}")
        elif d <= 7:
            print(f"    🟠 {pid}: DUE in {d}d ({due}) — {pred}")
        else:
            print(f"    🟡 {pid}: due {due} ({d}d) — {pred}")
    return overdue


def selftest():
    """Validate the data files + fetch import (fail-loud parser test). Returns 0 pass / 1 fail."""
    ok = True
    print("  ✓ FORGE fetch.py import OK")   # module-load would have exited 2 otherwise

    cat = LIQUID_DIR / "workbook" / "CATALYSTS.tsv"
    if not cat.exists():
        print("  ⚠️  CATALYSTS.tsv not found")
    else:
        rows = cat.read_text().splitlines()
        exp = ["date", "event", "what_to_check", "threshold_signal",
               "priority", "who_cares", "notes", "date_class"]
        if rows[0].split("\t") != exp:
            print(f"  ✗ CATALYSTS.tsv header mismatch: {rows[0].split(chr(9))}")
            ok = False
        bad = 0
        for i, ln in enumerate(rows[1:], 2):
            p = ln.split("\t")
            if len(p) != 8:
                print(f"  ✗ CATALYSTS.tsv line {i}: {len(p)} fields (expect 8)")
                ok = False; bad += 1; continue
            try:
                datetime.strptime(p[0], "%Y-%m-%d")
            except ValueError:
                print(f"  ✗ CATALYSTS.tsv line {i}: bad date {p[0]!r}")
                ok = False; bad += 1
        if not bad and ok:
            print(f"  ✓ CATALYSTS.tsv OK ({len(rows) - 1} rows, 8 cols, dates parse)")

    pred = LIQUID_DIR / "workbook" / "PREDICTIONS.tsv"
    if not pred.exists():
        print("  ⚠️  PREDICTIONS.tsv not found")
    else:
        rows = pred.read_text().splitlines()
        hdr = rows[0].split("\t")
        unparsed = [d.get("Pred_ID", "?") for d in (dict(zip(hdr, ln.split("\t"))) for ln in rows[1:])
                    if d.get("Status", "").strip().upper() == "OPEN" and not _parse_timeframe(d.get("Timeframe", ""))[1]]
        if unparsed:
            print(f"  ⚠️  PREDICTIONS.tsv OPEN rows with unparseable Timeframe: {unparsed} (scan flags manual-check)")
        else:
            print("  ✓ PREDICTIONS.tsv OK (all OPEN timeframes parse)")

    kb = LIQUID_DIR / "workbook" / "KB.tsv"
    if not kb.exists():
        print("  ⚠️  KB.tsv not found")
    else:
        rows = [ln for ln in kb.read_text().split("\n") if ln != ""]
        exp = ["ID", "Date", "Group", "Entity", "Fact", "Source", "Conf",
               "Epistemic", "Status", "Stale_By", "DerivedFrom", "Vectors", "Notes"]
        if rows[0].split("\t") != exp:
            print(f"  ✗ KB.tsv header mismatch ({len(rows[0].split(chr(9)))} cols, expect 13): {rows[0].split(chr(9))}")
            ok = False
        bad = 0
        for i, ln in enumerate(rows[1:], 2):
            p = ln.split("\t")
            if len(p) != 13:
                print(f"  ✗ KB.tsv line {i} ({p[0] if p else '?'}): {len(p)} fields (expect 13 — column drift)")
                ok = False; bad += 1; continue
            sid = p[0]
            if not (sid.startswith("KB-LIQ-") and len(sid) == 10 and sid[7:].isdigit()):
                print(f"  ✗ KB.tsv line {i}: malformed ID {sid!r}")
                ok = False; bad += 1
        if not bad and ok:
            print(f"  ✓ KB.tsv OK ({len(rows) - 1} rows, 13 cols, IDs well-formed)")

    print(f"\n  SELFTEST: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

SEV = {"🔴": 3, "🟠": 2, "🟡": 1, "🟢": 0}
DASH_ORDER = ["CREDIT", "DOMESTIC", "FOREIGN"]
DASH_TITLE = {"CREDIT": "Dashboard 1 — Credit Spreads",
              "DOMESTIC": "Dashboard 2 — Domestic Plumbing",
              "FOREIGN": "Dashboard 3 — Foreign Official"}


def render(verbose):
    for dash in DASH_ORDER:
        rows = [r for r in RESULTS if r["dashboard"] == dash]
        if not rows:
            continue
        # collapsed: show alerts (non-🟢) + headline rows; verbose: show all
        shown = [r for r in rows if (verbose or r["marker"] != "🟢" or r["headline"])]
        print(f"\n  {DASH_TITLE[dash]}")
        if not shown:
            print("    🟢 all clear")
            continue
        for r in shown:
            line = f"    {r['marker']} {r['label']:<12} {r['display']:<20}"
            if r["note"]:
                line += f" {r['note']}"
            print(line)
            if verbose and r["trend"]:
                print(f"       trend: {r['trend']}   [{r['asof']}]")


def summary(elapsed, imminent=0, overdue=0):
    reds = [r for r in RESULTS if r["marker"] == "🔴"]
    oranges = [r for r in RESULTS if r["marker"] == "🟠"]
    yellows = [r for r in RESULTS if r["marker"] == "🟡"]
    hy = next((r for r in RESULTS if r["label"] == "HY OAS"), None)

    print(f"\n  {'=' * 66}")
    print(f"  BOOT SUMMARY   🔴 {len(reds)}   🟠 {len(oranges)}   🟡 {len(yellows)}   "
          f"⏰ {imminent} imminent   📋 {overdue} overdue-pred   "
          f"({len(RESULTS)} series, {ERRORS} fetch errors, {elapsed:.1f}s)")
    if hy and hy["display"] != "ERR":
        print(f"  Headline: HY OAS {hy['display']} — {hy['note']}")
    for r in reds:
        print(f"    🔴 {r['label']}: {r['note']}")
    print(f"\n  ⚠️  Basis: FRED prints lag T+1 (latest may be 1-2 sessions back, more on a weekend);")
    print(f"      yfinance = last close; Brent BZ=F ≠ ICE settle; USD/JPY ≠ 5pm-ET NY close.")
    print(f"      Declare the basis when citing any figure downstream.")


def main():
    if "--selftest" in sys.argv:
        print("\n  LIQUID boot.py --selftest")
        return selftest()
    quick = "--quick" in sys.argv
    verbose = "--verbose" in sys.argv
    t0 = datetime.now()

    print(f"\n{'#' * 68}")
    print(f"#{'LIQUID BOOT — 3-dashboard live sweep':^66}#")
    print(f"#{t0.strftime('%A, %B %d, %Y  %H:%M'):^66}#")
    print(f"{'#' * 68}")

    build_credit()
    build_domestic()
    if quick:
        print("\n  ⏩ --quick: skipping yfinance prices (APO/BIZD/VIX/HYG/TLT/USDJPY/Brent)")
    else:
        build_prices()

    render(verbose)

    print("\n  Catalyst Countdown (workbook/CATALYSTS.tsv, 60d horizon)")
    imminent = catalyst_countdown()
    print("\n  Predictions Due-Scan (workbook/PREDICTIONS.tsv)")
    overdue = predictions_scan()

    elapsed = (datetime.now() - t0).total_seconds()
    summary(elapsed, imminent, overdue)
    print()
    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main())
