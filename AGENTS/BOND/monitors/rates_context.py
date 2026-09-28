#!/usr/bin/env python3
"""BOND — rates-context block for boot_recompute: market-implied Fed path,
term premium (ACM + KW), and the VX-BND-17 MBS re-arm watcher.

WHY THIS EXISTS (2026-09-28, Will: "go ahead with 1 + 2 + 3", coverage-gap
review `analysis/2026-09-28_coverage-gap-review.md`)
-----------------------------------------------------------------------------
Three load-bearing inputs were either hand-pulled or watched by nobody:

  1. MARKET-IMPLIED FED PATH. The 9/28 deep-dive (KB-BND-353) had to pull
     fed funds futures ad hoc. BOND owns curve shape and owes a 10/28 FOMC
     curve-shape row keyed on the TERMINAL, not the meeting. HENRY owns
     macro -> rate expectations; BOND CONSUMES this read and does not own it.
  2. TERM PREMIUM. ACM/KW are a Will-ruled BOND scope claim (8/10 forum,
     sovereign-credibility set), and STATUS carried them STALE from a 9/24
     hand pull through the year's biggest long-end move.
  3. VX-BND-17 RE-ARM. The MBS vector was declared DORMANT 8/18 with a named
     re-arm trigger (primary spread outside ~180-230bp) that NOTHING measured.
     An unmeasured exit cannot fire, so the dormancy was self-sealing.

SOURCES AND THEIR LIMITS (said out loud, so nobody over-reads the block)
  · Fed path = CBOT 30-day fed funds futures via yfinance (ZQ<m><yy>.CBT).
    VENDOR bars, NOT settlement prices (CME settlements returned 403 on
    2026-09-28, re-test at next build). A bar read after 14:30 ET on a weekday
    is a last trade / next-session bar, not the settle (fleet memory
    finding_a_daily_bar_read_after_the_evening_open_belongs_to_the_next_session).
    CME SOFR futures (SR3) are NOT used: yfinance returned one bar and no
    history for every contract on 2026-09-28.
  · Next-meeting date comes from BOND's OWN docket (`docket/CATALYSTS.tsv`,
    rows naming an FOMC DECISION), never a hardcoded calendar. If no future
    FOMC decision is docketed this block FLAGS it: the September FOMC once went
    missing from this docket, and a missing row is invisible to every other check.
  · Term premium: NY Fed ACM Daily sheet (ACMTP10) and FRED THREEFYTP10 (KW).
    Two MODELS; name the model in every TP claim.
  · MBS primary spread = Freddie Mac PMMS 30Y (FRED MORTGAGE30US, weekly Thu)
    minus DGS10 on the same date (or the latest prior close). This is the
    definition consistent with VX-BND-17's own 7/1 baseline (~200-205bp); the
    ~100-110bp "CC" figure there is a DIFFERENT spread. Only the spread leg of
    the re-arm trigger is machine-watched; the GSE-release and active-MBS-sales
    legs are NOT, and the block says so every run.

rc contribution to boot_recompute: each fetch failure, a stale source, a
fired re-arm band, or no future FOMC on the docket counts ONE finding. A
finding is a prompt to LOOK, never a pass.

    python3 monitors/rates_context.py            # print the block
    python3 monitors/rates_context.py --selftest # verify the pure functions
"""
from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BOND = HERE.parent
REPO = BOND.parents[1]
sys.path.insert(0, str(REPO / "FORGE" / "tools" / "market-data"))

MONTH_CODES = "FGHJKMNQUVXZ"
ACM_URL = "https://www.newyorkfed.org/medialibrary/media/research/data_indicators/ACMTermPremium.xls"
MBS_BAND = (1.80, 2.30)          # VX-BND-17 re-arm band, percentage points (workbook/VX.tsv)
STALE_DAYS = 14                  # a TP source older than this (calendar days) is a finding
STRIP_MONTHS = 20                # contracts requested; the vendor listed 17 live months on 2026-09-28


# ---------------------------------------------------------------------------
# PURE FUNCTIONS (selftested)
# ---------------------------------------------------------------------------

def zq_tickers(today: dt.date, n: int = STRIP_MONTHS) -> list:
    """[(YYYY-MM, ticker)] from the current month forward."""
    out, y, m = [], today.year, today.month
    for _ in range(n):
        out.append((f"{y}-{m:02d}", f"ZQ{MONTH_CODES[m - 1]}{y % 100:02d}.CBT"))
        m += 1
        if m > 12:
            y, m = y + 1, 1
    return out


def strip_summary(strip: list, effr: float) -> dict:
    """strip = [(month, rate, bar_date)]. Contracts whose last bar is older than
    the strip's newest bar are STALE and excluded from the terminal."""
    newest = max(b for _, _, b in strip)
    live = [(m, r) for m, r, b in strip if b == newest]
    stale = [m for m, _, b in strip if b != newest]
    peak_m, peak = max(live, key=lambda x: x[1])
    last_m, last = live[-1]
    return {"newest_bar": newest, "stale": stale, "terminal": peak, "terminal_month": peak_m,
            "cum_bp": round((peak - effr) * 100, 1), "hikes": round((peak - effr) / 0.25, 1),
            "after_peak_bp": round((last - peak) * 100, 1), "last_month": last_m}


def next_meeting_odds(rates_by_month: dict, effr: float, meeting: dt.date, fomc_dates: list):
    """25bp-hike odds at `meeting` from the fed funds strip.

    Uses the month AFTER the meeting month when fewer than 10 days of the
    meeting month remain after the decision (thin in-month signal), which
    assumes no other docketed FOMC in that following month; otherwise
    backs the post-meeting rate out of the meeting-month average (CME method).
    Returns (bp_priced, method) or (None, reason)."""
    import calendar
    ndays = calendar.monthrange(meeting.year, meeting.month)[1]
    after = ndays - meeting.day                       # days at the new rate (effective next day)
    mk = f"{meeting.year}-{meeting.month:02d}"
    if after >= 10:
        if mk not in rates_by_month:
            return None, f"no contract for {mk}"
        post = (rates_by_month[mk] * ndays - effr * (ndays - after)) / after
        return round((post - effr) * 100, 1), f"in-month ({mk}, {after} days after decision)"
    ny, nm = (meeting.year + (meeting.month == 12), meeting.month % 12 + 1)
    nk = f"{ny}-{nm:02d}"
    if any(d.year == ny and d.month == nm for d in fomc_dates):
        return None, f"assumption void: another FOMC is docketed in {nk}"
    if nk not in rates_by_month:
        return None, f"no contract for {nk}"
    return round((rates_by_month[nk] - effr) * 100, 1), f"next-month ({nk} avg; assumes no {nk} meeting)"


def docket_fomc(rows: list, today: dt.date) -> list:
    """Future FOMC DECISION dates from CATALYSTS rows [(date_str, event)]."""
    out = []
    for d, ev in rows:
        e = ev.upper()
        if "FOMC" in e and "DECISION" in e and "MINUTES" not in e:
            try:
                x = dt.date.fromisoformat(d.strip()[:10])
            except ValueError:
                continue
            if x >= today:
                out.append(x)
    return sorted(set(out))


def mbs_state(mort: float, ust10: float, band=MBS_BAND):
    s = round(mort - ust10, 4)          # float guard: 6.80 − 5.00 must be 1.80, not 1.7999…
    if s < band[0]:
        return round(s * 100), "BELOW"
    if s > band[1]:
        return round(s * 100), "ABOVE"
    return round(s * 100), "INSIDE"


def bar_timing_label(now_et: dt.datetime) -> str:
    if now_et.weekday() < 5 and (now_et.hour, now_et.minute) >= (14, 30):
        return "read after 14:30 ET on a weekday: bars are LAST TRADE / next session, NOT settlement"
    return "read outside the 14:30 ET weekday window: last bar = prior session's vendor close, NOT settlement"


# ---------------------------------------------------------------------------
# I/O
# ---------------------------------------------------------------------------

def _fred(sid, limit):
    import fetch
    raw = fetch.fred_fetch(sid, limit=limit)
    obs = []
    for o in raw:
        if "error" in o:
            raise RuntimeError(f"{sid}: {o['error']}")
        try:
            obs.append((o["date"], float(o["value"])))
        except (ValueError, KeyError):
            pass
    if not obs:
        raise RuntimeError(f"{sid} returned no observations")
    return sorted(obs)


def _now_et():
    try:
        from zoneinfo import ZoneInfo
        return dt.datetime.now(ZoneInfo("America/New_York"))
    except Exception:
        return dt.datetime.now()


def policy_path(today: dt.date) -> int:
    print("\n== FED PATH (CBOT fed funds futures · vendor bars, NOT settlement · HENRY owns the read, BOND consumes) ==")
    try:
        import logging
        import yfinance as yf
        logging.getLogger("yfinance").setLevel(logging.CRITICAL)   # unlisted far months are expected, not errors
        effr_d, effr = _fred("EFFR", 10)[-1]
        pairs = zq_tickers(today)
        df = yf.download([t for _, t in pairs], period="1mo", progress=False, auto_adjust=False)["Close"]
        strip, hist = [], {}
        for m, t in pairs:
            if t not in df.columns:
                continue
            c = df[t].dropna()
            if c.empty:
                continue
            strip.append((m, round(100 - float(c.iloc[-1]), 3), str(c.index[-1].date())))
            hist[m] = [round(100 - float(x), 3) for x in c.tolist()]
        if len(strip) < 6:
            raise RuntimeError(f"only {len(strip)} contracts returned")
    except Exception as e:
        print(f"   🔴 GAP — fed path not read ({e}). NOT a pass.")
        return 1
    print(f"   {bar_timing_label(_now_et())}")
    s = strip_summary(strip, effr)
    by_m = {m: r for m, r, b in strip if b == s["newest_bar"]}
    print(f"   anchor EFFR {effr:.2f} [{effr_d}] · newest bar {s['newest_bar']} · {len(by_m)} live contracts"
          + (f" · STALE (excluded): {', '.join(s['stale'])}" if s["stale"] else ""))
    print("   month     implied   Δ1obs   Δ5obs   vs EFFR")
    for m, r in by_m.items():
        h = hist[m]
        d1 = (h[-1] - h[-2]) * 100 if len(h) >= 2 else float("nan")
        d5 = (h[-1] - h[-6]) * 100 if len(h) >= 6 else float("nan")
        print(f"   {m}   {r:7.3f}  {d1:+6.1f}  {d5:+6.1f}  {(r - effr) * 100:+7.1f}bp")
    print(f"   TERMINAL (max implied, method: max over live contracts): {s['terminal']:.3f} in {s['terminal_month']} "
          f"= {s['cum_bp']:+.1f}bp vs EFFR ≈ {s['hikes']} × 25bp; {s['last_month']} is {s['after_peak_bp']:+.1f}bp from the peak")
    findings = 0
    rows = []
    try:
        for line in (BOND / "docket" / "CATALYSTS.tsv").read_text(encoding="utf-8").splitlines()[1:]:
            f = line.split("\t")
            if len(f) >= 2:
                rows.append((f[0], f[1]))
    except OSError as e:
        print(f"   🔴 GAP — CATALYSTS.tsv unreadable ({e})")
        return 1
    fomc = docket_fomc(rows, today)
    if not fomc:
        print("   🔴 NO FUTURE FOMC DECISION ON THE DOCKET — add the row (a missing row is invisible to every other check).")
        findings += 1
    else:
        bp, how = next_meeting_odds(by_m, effr, fomc[0], fomc)
        if bp is None:
            print(f"   ⚠️ next FOMC {fomc[0]} (docket): odds not computed — {how}")
        else:
            print(f"   next FOMC {fomc[0]} (from docket): {bp:+.1f}bp priced ≈ {bp / 25:.0%} of a 25bp move · method {how}; "
                  f"assumes EFFR holds at {effr:.2f} until then")
    return findings


def term_premium(today: dt.date) -> int:
    print("\n== TERM PREMIUM (two MODELS — name the model in every TP claim) ==")
    findings = 0
    try:
        import tempfile
        import urllib.request
        import xlrd
        req = urllib.request.Request(ACM_URL, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as r, tempfile.NamedTemporaryFile(suffix=".xls") as tmp:
            tmp.write(r.read()); tmp.flush()
            sh = xlrd.open_workbook(tmp.name).sheet_by_name("ACM Daily")
            ci = {x: i for i, x in enumerate(sh.row_values(0))}
            acm = []
            for i in range(max(1, sh.nrows - 30), sh.nrows):
                v = sh.row_values(i)
                acm.append((dt.datetime.strptime(v[0], "%d-%b-%Y").date(), float(v[ci["ACMTP10"]])))
        d, v = acm[-1]
        age = (today - d).days
        print(f"   ACM 10Y TP (NY Fed ACM Daily, ACMTP10) {v:.4f} [{d}]  Δ1obs {(v - acm[-2][1]) * 100:+.1f}bp  "
              f"Δ5obs {(v - acm[-6][1]) * 100:+.1f}bp  age {age}d")
        if age > STALE_DAYS:
            print(f"   🔴 ACM frontier is {age} days old (> {STALE_DAYS}) — source stale; LOOK before citing.")
            findings += 1
    except Exception as e:
        print(f"   🔴 GAP — ACM not read ({e}). NOT a pass.")
        findings += 1
    try:
        kw = _fred("THREEFYTP10", 30)
        d, v = kw[-1]
        age = (today - dt.date.fromisoformat(d)).days
        print(f"   KW 10Y TP (FRED THREEFYTP10)            {v:.4f} [{d}]  Δ1obs {(v - kw[-2][1]) * 100:+.1f}bp  "
              f"Δ5obs {(v - kw[-6][1]) * 100:+.1f}bp  age {age}d")
        if age > STALE_DAYS:
            print(f"   🔴 KW frontier is {age} days old (> {STALE_DAYS}) — source stale; LOOK before citing.")
            findings += 1
    except Exception as e:
        print(f"   🔴 GAP — KW not read ({e}). NOT a pass.")
        findings += 1
    return findings


def mbs_rearm(today: dt.date) -> int:
    print("\n== VX-BND-17 RE-ARM WATCHER (MBS relay DORMANT since 8/18; spread leg only) ==")
    try:
        mort = _fred("MORTGAGE30US", 12)
        ust = dict(_fred("DGS10", 60))
    except Exception as e:
        print(f"   🔴 GAP — watcher not read ({e}). NOT a pass.")
        return 1
    findings = 0
    for d, mv in mort[-3:]:
        k = max(x for x in ust if x <= d)
        bp, state = mbs_state(mv, ust[k])
        print(f"   {d}  PMMS 30Y {mv:.2f} − DGS10 {ust[k]:.2f} [{k}] = {bp}bp  → {state} "
              f"{MBS_BAND[0]*100:.0f}–{MBS_BAND[1]*100:.0f}bp")
    d, mv = mort[-1]
    k = max(x for x in ust if x <= d)
    bp, state = mbs_state(mv, ust[k])
    if state != "INSIDE":
        print(f"   🔴 RE-ARM TRIGGER (spread leg) FIRED: {bp}bp is {state} the band — VX-BND-17 re-arm review owed; "
              f"coordinate HOMER/REGINALD (per the VX row).")
        findings += 1
    else:
        print(f"   ✅ spread leg not fired ({bp - MBS_BAND[0]*100:.0f}bp above the low edge, "
              f"{MBS_BAND[1]*100 - bp:.0f}bp below the high edge).")
    print("   ⚠️ NOT watched by this tool: the GSE-release-execution and active-Fed-MBS-sales legs of the re-arm trigger.")
    return findings


def run(today: dt.date | None = None) -> int:
    today = today or dt.date.today()
    return policy_path(today) + term_premium(today) + mbs_rearm(today)


# ---------------------------------------------------------------------------
# SELFTEST
# ---------------------------------------------------------------------------

def selftest() -> int:
    fails = 0

    def check(label, ok):
        nonlocal fails
        fails += 0 if ok else 1
        print(f"  {'PASS' if ok else 'FAIL'}  {label}")

    print("[rates_context --selftest]\n")
    t = zq_tickers(dt.date(2026, 11, 3), 3)
    check("tickers roll the year: Nov-26 → X26, Z26, F27", [x[1] for x in t] == ["ZQX26.CBT", "ZQZ26.CBT", "ZQF27.CBT"])
    # the 9/28 strip, abridged (real vendor reads, KB-BND-353); a stale Feb-28 bar must not set the terminal
    strip = [("2026-10", 3.893, "2026-09-28"), ("2026-11", 4.05, "2026-09-28"), ("2027-11", 4.855, "2026-09-28"),
             ("2027-12", 4.845, "2026-09-28"), ("2028-01", 4.81, "2026-09-28"), ("2028-02", 4.99, "2026-09-25")]
    s = strip_summary(strip, 3.88)
    check("terminal = Nov-27 4.855 (+97.5bp ≈ 3.9 hikes)", (s["terminal_month"], s["terminal"], s["cum_bp"], s["hikes"]) == ("2027-11", 4.855, 97.5, 3.9))
    check("a STALE bar is excluded, never the terminal", s["stale"] == ["2028-02"])
    check("post-peak decline reported (Jan-28 −4.5bp)", s["after_peak_bp"] == -4.5)
    by = {m: r for m, r, _ in strip[:5]}
    bp, how = next_meeting_odds(by, 3.88, dt.date(2026, 10, 28), [dt.date(2026, 10, 28)])
    check("10/28 meeting → next-month (Nov) method, +17bp ≈ 68%", bp == 17.0 and how.startswith("next-month"))
    bp, how = next_meeting_odds(by, 3.88, dt.date(2026, 10, 28), [dt.date(2026, 10, 28), dt.date(2026, 11, 4)])
    check("next-month method VOIDED when another FOMC is docketed that month", bp is None and "void" in how)
    bp, _ = next_meeting_odds({"2026-12": 4.0}, 3.88, dt.date(2026, 12, 9), [dt.date(2026, 12, 9)])
    check("in-month method backs out the post-meeting rate (Dec 9: 22 days after)", bp == round(((4.0 * 31 - 3.88 * 9) / 22 - 3.88) * 100, 1))
    rows = [("2026-10-28", "🔴 **OCTOBER FOMC DECISION, 2:00 PM ET**"), ("2026-10-08", "FOMC MINUTES (decision recap)"),
            ("2026-09-16", "SEPTEMBER FOMC DECISION"), ("watch", "FOMC DECISION something")]
    check("docket parser: future DECISION rows only; minutes, past and undated rows ignored", docket_fomc(rows, dt.date(2026, 9, 28)) == [dt.date(2026, 10, 28)])
    check("docket parser: nothing future → empty (the caller FLAGS it)", docket_fomc(rows, dt.date(2026, 10, 29)) == [])
    check("MBS 9/24 real case: 7.03 − 5.18 = 185bp INSIDE", mbs_state(7.03, 5.18) == (185, "INSIDE"))
    check("MBS band edges inclusive: 180 and 230 INSIDE", mbs_state(6.80, 5.00)[1] == "INSIDE" and mbs_state(7.30, 5.00)[1] == "INSIDE")
    check("MBS 179bp BELOW, 231bp ABOVE", mbs_state(6.79, 5.00)[1] == "BELOW" and mbs_state(7.31, 5.00)[1] == "ABOVE")
    check("bar label after 14:30 ET weekday = last trade", "LAST TRADE" in bar_timing_label(dt.datetime(2026, 9, 28, 16, 30)))
    check("bar label on a Saturday = prior-session close", "prior session" in bar_timing_label(dt.datetime(2026, 9, 26, 16, 30)))
    print(f"\n  {'ALL PASS' if not fails else str(fails) + ' FAILURE(S)'} — 14 fixtures")
    return 1 if fails else 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    sys.exit(1 if run() else 0)
