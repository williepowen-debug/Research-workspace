#!/usr/bin/env python3
"""BOND — rates-context block for boot_recompute: market-implied Fed path,
term premium (ACM + KW), and the VX-BND-17 MBS re-arm watcher.

WHY THIS EXISTS (2026-09-28, Will: "go ahead with 1 + 2 + 3", WQ-327,
coverage-gap review `analysis/2026-09-28_coverage-gap-review.md`)
-----------------------------------------------------------------------------
Three load-bearing inputs were either hand-pulled or watched by nobody:

  1. MARKET-IMPLIED FED PATH. BOND owns curve shape and owes a 10/28 FOMC
     curve-shape row keyed on the path, not the meeting. HENRY OWNS the
     fed-funds/SOFR series (WQ-327); BOND CONSUMES this read.
  2. TERM PREMIUM. ACM/KW are a Will-ruled BOND scope claim (8/10 forum,
     sovereign-credibility set), and STATUS carried them STALE from a 9/24
     hand pull through the year's biggest long-end move.
  3. VX-BND-17 RE-ARM. The MBS vector was declared DORMANT 8/18 with a named
     re-arm trigger (primary spread outside ~180-230bp) that NOTHING measured.

v2 (same evening) — CATO review `AGENTS/CATO/runs/2026-09-28_1744_bond-rates-
context-review.md` (BR1-BR4) + PROME (#5). v1 could CLEAR on bad evidence:
  BR1 stale inputs (a strip dated 8/10, an EFFR from 8/7, a PMMS or a DGS10
      from 8/13) printed a clean verdict — v1 checked freshness only for TP.
  BR2 coverage was validated BEFORE stale contracts were dropped, so a
      one-live-contract strip printed a "TERMINAL", and a missing meeting
      contract printed ⚠️ with no finding.
  BR3 the calendar guard caught an EMPTY docket, not a MISSING NEXT meeting:
      with Oct deleted and Dec kept, v1 called Dec "next" and printed
      "124% of a 25bp move".
  BR4 the bar label inferred provenance from the wall clock alone.
  #5  a PMMS date earlier than every DGS10 raised ValueError (crash-shaped).
The fix is freshness + coverage + calendar checks that turn each of those
into a GAP plus a finding. A finding is a prompt to LOOK, never a pass.
CATO's regression suite (`AGENTS/CATO/runs/2026-09-28_1744_bond-rates-context-
fixtures.py`) is the acceptance test, alongside this module's --selftest.

SOURCES, TOLERANCES AND THEIR BASIS (owner-chosen, documented here)
  · Fed path = CBOT 30-day fed funds futures via yfinance (ZQ<m><yy>.CBT).
    VENDOR bars, NOT settlement (CME settlements HTTP 403 on 2026-09-28; re-test: at the swap-spread
    build and every quarterly calendar re-record).
    Bar label comes from the returned BAR DATE, never the clock alone.
    Newest bar must be ≤ FUT_MAX_BD business days old (they trade every
    business day; +1 for a holiday). ≥ MIN_LIVE live contracts after the
    stale-contract filter. The output is the PEAK OF THE AVAILABLE STRIP with
    its horizon; if the strip is still rising at its last contract, the
    terminal is NOT established. SOFR futures (SR3) unused: 1 bar, no history.
  · EFFR anchor ≤ EFFR_MAX_BD business days old (NY Fed publishes day D on
    D+1; +2 for holidays/weekend lag).
  · Next meeting: BOND's docket checked against a RECORDED issuer calendar,
    `monitors/FOMC_CALENDAR.tsv` — the Federal Reserve's own list, written by
    `rates_context.py --record-calendar` (a deliberate human step; boot never
    fetches the page: PROME's WQ-327 letter bars new sources in the boot pull).
    The record names its page and check date. Every recorded meeting within
    CAL_WINDOW days must be docketed (missing = finding); a record older than
    CAL_RECHECK_DAYS, or ending inside the window, is a finding. If the record
    is unreadable the claim is labelled "next DOCKETED meeting — calendar
    completeness UNVERIFIED" WITH a finding, plus a structural guard: a next
    docketed meeting more than MAX_GAP_DAYS away (scheduled gaps ≤ ~8 weeks).
    A percentage is printed ONLY for a single hold/±25bp step (0 ≤ |bp| ≤ 25);
    otherwise raw bp, explicitly "not a probability".
  · Term premium: NY Fed ACM Daily (ACMTP10) + FRED THREEFYTP10 (KW); two
    MODELS, name the model; stale > STALE_DAYS calendar days = finding.
  · MBS primary spread = Freddie Mac PMMS 30Y (weekly survey, Thu-Wed
    applications, published Thursday) − DGS10 on the PMMS date or up to
    JOIN_MAX_BD business days before it. PMMS older than PMMS_MAX_DAYS = GAP.
    Only the spread leg of the re-arm is watched; the GSE-release and
    active-MBS-sales legs are NOT, and the block says so every run.

INTERPRETATION LIMIT (CATO): the FF-strip change and the ACM change are
different windows and horizons — consistent with both channels, NOT a causal
decomposition of the sell-off.

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
FOMC_URL = "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"   # --record-calendar only, never at boot
CAL_RECORD = HERE / "FOMC_CALENDAR.tsv"
MBS_BAND = (1.80, 2.30)          # VX-BND-17 re-arm band, percentage points (workbook/VX.tsv)
STALE_DAYS = 14                  # TP source older than this (calendar days) = finding
STRIP_MONTHS = 20                # contracts requested; the vendor listed 17 live months on 2026-09-28
FUT_MAX_BD = 2                   # newest futures bar, business days old
EFFR_MAX_BD = 3                  # EFFR anchor, business days old
PMMS_MAX_DAYS = 10               # weekly survey: 7 days + holiday shift + margin
JOIN_MAX_BD = 2                  # DGS10 may precede the PMMS date by at most this
MIN_LIVE = 6                     # live contracts required after the stale filter
MAX_GAP_DAYS = 63                # fallback guard: next docketed FOMC farther than this = incomplete docket
CAL_WINDOW = 120                 # recorded meetings within this many days must be docketed
CAL_RECHECK_DAYS = 90            # re-record the issuer calendar at least this often (unscheduled changes are rare, not impossible)


# ---------------------------------------------------------------------------
# PURE FUNCTIONS (selftested)
# ---------------------------------------------------------------------------

def bd_age(d_from: dt.date, d_to: dt.date) -> int:
    """Business days in [d_from, d_to) (Mon-Fri; holidays not modelled — tolerances carry margin).
    STDLIB on purpose (2026-09-28, PROME): numpy.busday_count made the standalone --selftest crash under
    the system python3, which has no numpy. Verified equal to np.busday_count on 40,000 date pairs."""
    if d_to < d_from:
        return -bd_age(d_to, d_from)
    full, rem = divmod((d_to - d_from).days, 7)
    return full * 5 + sum(1 for i in range(rem) if (d_from.weekday() + i) % 7 < 5)


def _d(x) -> dt.date:
    return x if isinstance(x, dt.date) else dt.date.fromisoformat(str(x)[:10])


def stale_reasons(today: dt.date, effr_date=None, bar_date=None, pmms_date=None) -> list:
    """Source-specific age checks (BR1). Empty list = fresh enough to be a CURRENT read."""
    out = []
    if effr_date is not None and bd_age(_d(effr_date), today) > EFFR_MAX_BD:
        out.append(f"EFFR anchor {effr_date} is {bd_age(_d(effr_date), today)} business days old (> {EFFR_MAX_BD})")
    if bar_date is not None and bd_age(_d(bar_date), today) > FUT_MAX_BD:
        out.append(f"newest futures bar {bar_date} is {bd_age(_d(bar_date), today)} business days old (> {FUT_MAX_BD})")
    if pmms_date is not None and (today - _d(pmms_date)).days > PMMS_MAX_DAYS:
        out.append(f"latest PMMS {pmms_date} is {(today - _d(pmms_date)).days} days old (> {PMMS_MAX_DAYS})")
    return out


def peak_line(s: dict) -> str:
    """BR2: never 'terminal' without its horizon."""
    tail = ("STILL RISING at the horizon end — the terminal is NOT established by this strip"
            if s["rising_at_end"] else f"{s['last_month']} is {s['after_peak_bp']:+.1f}bp from the peak")
    return (f"PEAK OF AVAILABLE STRIP ({s['first_month']}→{s['last_month']}, max over live contracts): "
            f"{s['terminal']:.3f} in {s['terminal_month']} = {s['cum_bp']:+.1f}bp vs EFFR ≈ {s['hikes']} × 25bp; {tail}")


def parse_calendar_record(text: str):
    """-> (checked_date, [decision dates]) from FOMC_CALENDAR.tsv; raises on a malformed record."""
    checked, dates = None, []
    for line in text.splitlines():
        if line.startswith("# checked:"):
            checked = dt.date.fromisoformat(line.split(":", 1)[1].strip()[:10])
        elif line and not line.startswith("#") and not line.startswith("decision_date"):
            dates.append(dt.date.fromisoformat(line.split("\t")[0].strip()))
    if checked is None or not dates:
        raise ValueError("record has no '# checked:' line or no meetings")
    return checked, sorted(dates)


def record_issues(checked: dt.date, dates: list, today: dt.date) -> list:
    out = []
    if (today - checked).days > CAL_RECHECK_DAYS:
        out.append(f"issuer calendar record checked {checked} is {(today - checked).days}d old (> {CAL_RECHECK_DAYS}d) — re-run --record-calendar")
    if dates[-1] < today + dt.timedelta(days=CAL_WINDOW):
        out.append(f"issuer calendar record ends {dates[-1]}, inside the {CAL_WINDOW}d window — re-run --record-calendar")
    return out


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
    the strip's newest bar are STALE and excluded. Reports the PEAK OF THE
    AVAILABLE STRIP and whether the strip is still rising at its horizon end."""
    newest = max(b for _, _, b in strip)
    live = [(m, r) for m, r, b in strip if b == newest]
    stale = [m for m, _, b in strip if b != newest]
    peak_m, peak = max(live, key=lambda x: x[1])
    last_m, last = live[-1]
    return {"newest_bar": newest, "stale": stale, "n_live": len(live), "first_month": live[0][0],
            "terminal": peak, "terminal_month": peak_m,
            "cum_bp": round((peak - effr) * 100, 1), "hikes": round((peak - effr) / 0.25, 1),
            "after_peak_bp": round((last - peak) * 100, 1), "last_month": last_m,
            "rising_at_end": peak_m == last_m}


def next_meeting_odds(rates_by_month: dict, effr: float, meeting: dt.date, fomc_dates: list):
    """bp priced at `meeting` from the fed funds strip.

    Uses the month AFTER the meeting month when fewer than 10 days of the
    meeting month remain after the decision (thin in-month signal), which
    requires that no FOMC falls in that following month (checked against
    `fomc_dates` — the issuer calendar when available); otherwise backs the
    post-meeting rate out of the meeting-month average (CME method).
    Returns (bp_priced, method) or (None, reason)."""
    import calendar
    ndays = calendar.monthrange(meeting.year, meeting.month)[1]
    after = ndays - meeting.day                       # days at the new rate (effective next day)
    mk = f"{meeting.year}-{meeting.month:02d}"
    if after >= 10:
        if mk not in rates_by_month:
            return None, f"no live contract for {mk}"
        post = (rates_by_month[mk] * ndays - effr * (ndays - after)) / after
        return round((post - effr) * 100, 1), f"in-month ({mk}, {after} days after decision)"
    ny, nm = (meeting.year + (meeting.month == 12), meeting.month % 12 + 1)
    nk = f"{ny}-{nm:02d}"
    if any(d.year == ny and d.month == nm for d in fomc_dates):
        return None, f"assumption void: another FOMC falls in {nk}"
    if nk not in rates_by_month:
        return None, f"no live contract for {nk}"
    return round((rates_by_month[nk] - effr) * 100, 1), f"next-month ({nk} avg; no {nk} meeting)"


def describe_pricing(bp: float) -> str:
    """A percentage only for a single hold/±25bp step; raw bp otherwise."""
    if 0 <= bp <= 25:
        return f"{bp:+.1f}bp priced ≈ {bp / 25:.0%} of a 25bp HIKE (hold-or-+25 reading)"
    if -25 <= bp < 0:
        return f"{bp:+.1f}bp priced ≈ {-bp / 25:.0%} of a 25bp CUT (hold-or-−25 reading)"
    return f"{bp:+.1f}bp priced — outside a single hold/±25bp step; NOT a probability"


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


def parse_fomc_calendar(html_text: str) -> list:
    """Decision dates (the LAST day of each meeting) from the Fed's calendar page."""
    import html as h
    import re
    months = {m: i for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul",
                                          "aug", "sep", "oct", "nov", "dec"], 1)}
    # keyed on the first 3 letters: the page writes "April/May" in some years and "Jan/Feb", "Oct/Nov" in
    # others — a full-name key silently dropped both 2023 cross-month meetings (caught 2026-09-28 on first record)
    out = []
    for y in re.findall(r"(\d{4}) FOMC Meetings", html_text):
        i = html_text.find(f"{y} FOMC Meetings")
        j = html_text.find("FOMC Meetings", i + 20)
        seg = html_text[i:j if j > 0 else len(html_text)]
        ms = re.findall(r"fomc-meeting__month[^>]*>\s*<strong>([^<]+)</strong>", seg)
        ds = re.findall(r"fomc-meeting__date[^>]*>([^<]+)<", seg)
        for m, d in zip(ms, ds):
            m, d = h.unescape(m).strip(), h.unescape(d).strip()
            mon = m.split("/")[-1].strip()[:3].lower()        # "April/May", "Oct/Nov" -> the later month
            nums = re.findall(r"\d+", d)
            if mon in months and nums and "notation" not in d.lower() and "unscheduled" not in d.lower():
                try:
                    out.append(dt.date(int(y), months[mon], int(nums[-1])))
                except ValueError:
                    pass
    return sorted(set(out))


def year_count_issues(dates: list) -> list:
    """Every recorded year must hold exactly 8 scheduled meetings (the FOMC's fixed schedule) —
    a parser that drops a row fails HERE, loudly, instead of in the docket check, silently."""
    from collections import Counter
    return [f"{y}: {n} meetings (expected 8)" for y, n in sorted(Counter(d.year for d in dates).items()) if n != 8]


def calendar_check(docket: list, issuer: list | None, today: dt.date):
    """-> (next_meeting, missing_from_docket, note). `issuer` None = issuer unreadable (fallback)."""
    if issuer:
        fut = [d for d in issuer if d >= today]
        if not fut:
            return None, [], "issuer calendar has no future meeting (page stale or reformatted)"
        missing = [d for d in fut if (d - today).days <= CAL_WINDOW and d not in docket]
        return fut[0], missing, "docket checked against the RECORDED issuer calendar"
    if not docket:
        return None, [], "no future FOMC on the docket and no issuer calendar record"
    nxt = docket[0]
    if (nxt - today).days > MAX_GAP_DAYS:
        return None, [], (f"next DOCKETED meeting {nxt} is {(nxt - today).days}d away (> {MAX_GAP_DAYS}d, longer than "
                          f"any scheduled FOMC gap) — docket likely INCOMPLETE; no issuer calendar record")
    return nxt, [], "next DOCKETED meeting — calendar completeness UNVERIFIED"


def join_prior(ust_dates: list, d: str, max_bd: int = JOIN_MAX_BD):
    """Latest DGS10 date ≤ d within max_bd business days, else None (never raises)."""
    prior = [x for x in ust_dates if x <= d]
    if not prior:
        return None
    k = max(prior)
    return k if bd_age(_d(k), _d(d)) <= max_bd else None


def mbs_state(mort: float, ust10: float, band=MBS_BAND):
    s = round(mort - ust10, 4)          # float guard: 6.80 − 5.00 must be 1.80, not 1.7999…
    if s < band[0]:
        return round(s * 100), "BELOW"
    if s > band[1]:
        return round(s * 100), "ABOVE"
    return round(s * 100), "INSIDE"


def bar_timing_label(now_et: dt.datetime, bar_date: str | None = None) -> str:
    """BR4: label from the RETURNED BAR DATE vs capture time, never the clock alone.
    Globex ZQ session = 18:00 ET (prior day) → 17:00 ET; settlement is NOT a vendor bar.
    Branches (PROME WQ-327 spec): today's bar in session = EVOLVING · today's bar after the
    17:00 halt = session's last vendor print · today's bar after the 18:00 reopen = may carry
    next-session trades (L462) · prior business day's bar = prior session's vendor close ·
    a bar dated after capture = next-session bar · anything else = UNKNOWN."""
    cap = f"captured {now_et:%Y-%m-%d %H:%M} ET"
    tail = "vendor bar, NOT settlement"
    if bar_date is None:
        return f"bar session/intraday status UNKNOWN (no bar date; {cap}); {tail}"
    b, today = _d(bar_date), now_et.date()
    hm = (now_et.hour, now_et.minute)
    if b > today:
        return f"bar dated {b}, after the capture date ({cap}) — a NEXT-SESSION bar; {tail}"
    if b == today and today.weekday() < 5:
        if hm < (17, 0):
            return f"today's EVOLVING bar {b} (session open; {cap}) — not a close; {tail}"
        if hm < (18, 0):
            return f"today's bar {b} after the 17:00 ET halt ({cap}) — the session's last vendor print; {tail}"
        return f"bar dated today {b} read after the 18:00 ET reopen ({cap}) — may carry NEXT-SESSION trades (L462); {tail}"
    if b < today and bd_age(b, today) == 1 and (today.weekday() >= 5 or hm < (18, 0)):
        return f"prior session's vendor close {b} ({cap}); {tail}"
    return f"bar {b} vs {cap}: session status UNKNOWN; {tail}"


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


def record_calendar() -> int:
    """HUMAN STEP: fetch the Fed's calendar page once and RECORD it (never called at boot)."""
    import urllib.request
    req = urllib.request.Request(FOMC_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        dates = parse_fomc_calendar(r.read().decode("utf-8", "replace"))
    bad = year_count_issues(dates)
    if len(dates) < 8 or bad:
        print(f"refused: {len(dates)} meetings parsed; {'; '.join(bad) or 'too few'} — page reformatted? record NOT written")
        return 2
    now = _now_et()
    lines = ["# FOMC scheduled-meeting calendar — RECORDED issuer list (decision day = last day of each meeting)",
             f"# source: {FOMC_URL}",
             f"# checked: {now:%Y-%m-%d %H:%M} ET by BOND via `rates_context.py --record-calendar`",
             f"# lists {len(dates)} meetings {dates[0]} → {dates[-1]}; re-record every <= {CAL_RECHECK_DAYS}d or on any unscheduled-meeting news",
             "decision_date"] + [str(d) for d in dates]
    CAL_RECORD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"recorded {len(dates)} meetings {dates[0]} → {dates[-1]} to {CAL_RECORD}")
    return 0


def _load_record():
    return parse_calendar_record(CAL_RECORD.read_text(encoding="utf-8"))


def policy_path(today: dt.date) -> int:
    print("\n== FED PATH (CBOT fed funds futures · vendor bars, NOT settlement · HENRY owns the series, BOND consumes) ==")
    findings = 0
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
        if not strip:
            raise RuntimeError("no contracts returned")
    except Exception as e:
        print(f"   🔴 GAP — fed path not read ({e}). NOT a pass.")
        return 1
    s = strip_summary(strip, effr)
    by_m = {m: r for m, r, b in strip if b == s["newest_bar"]}
    print(f"   {bar_timing_label(_now_et(), s['newest_bar'])}")
    print(f"   anchor EFFR {effr:.2f} [{effr_d}] · newest bar {s['newest_bar']} · {s['n_live']} live contracts"
          + (f" · STALE (excluded): {', '.join(s['stale'])}" if s["stale"] else ""))
    # BR1 — freshness of the anchor and of the strip itself
    usable = True
    for why in stale_reasons(today, effr_date=effr_d, bar_date=s["newest_bar"]):
        print(f"   🔴 GAP — {why}; NOT a current read.")
        findings += 1; usable = False
    # BR2 — coverage AFTER the stale filter
    if s["n_live"] < MIN_LIVE:
        print(f"   🔴 GAP — only {s['n_live']} live contract(s) after the stale filter (< {MIN_LIVE}); no path read.")
        findings += 1; usable = False
    print("   month     implied   Δ1obs   Δ5obs   vs EFFR")
    for m, r in by_m.items():
        h = hist[m]
        d1 = (h[-1] - h[-2]) * 100 if len(h) >= 2 else float("nan")
        d5 = (h[-1] - h[-6]) * 100 if len(h) >= 6 else float("nan")
        print(f"   {m}   {r:7.3f}  {d1:+6.1f}  {d5:+6.1f}  {(r - effr) * 100:+7.1f}bp")
    if usable:
        print(f"   {peak_line(s)}")
    else:
        print("   ⛔ no peak/terminal reported — inputs failed the checks above (values shown with their dates only).")
    # BR3 — the next meeting, issuer-checked when possible
    rows = []
    try:
        for line in (BOND / "docket" / "CATALYSTS.tsv").read_text(encoding="utf-8").splitlines()[1:]:
            f = line.split("\t")
            if len(f) >= 2:
                rows.append((f[0], f[1]))
    except OSError as e:
        print(f"   🔴 GAP — CATALYSTS.tsv unreadable ({e})")
        return findings + 1
    docket = docket_fomc(rows, today)
    try:
        checked, issuer = _load_record()
        for why in record_issues(checked, issuer, today):
            print(f"   🔴 {why}")
            findings += 1
    except Exception as e:
        print(f"   🔴 issuer calendar record unreadable ({e}) — next-meeting claim is UNVERIFIED.")
        findings += 1
        issuer = None
    nxt, missing, note = calendar_check(docket, issuer, today)
    if issuer is None and nxt is not None:
        findings += 1                                    # PROME #3: UNVERIFIED carries a finding
    for m in missing:
        print(f"   🔴 FOMC {m} is on the recorded Fed calendar but NOT on BOND's docket — add the row "
              f"(a missing row is invisible to every other check).")
        findings += 1
    if nxt is None:
        print(f"   🔴 NEXT MEETING UNRESOLVED — {note}.")
        return findings + 1
    if not usable:
        print(f"   next FOMC {nxt} ({note}): pricing NOT computed — inputs failed the checks above.")
        return findings
    bp, how = next_meeting_odds(by_m, effr, nxt, issuer or docket)
    if bp is None:
        print(f"   🔴 next FOMC {nxt} ({note}): pricing NOT computed — {how}.")
        return findings + 1
    print(f"   next FOMC {nxt} ({note}): {describe_pricing(bp)} · method {how}; assumes EFFR holds at {effr:.2f} until then")
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
    print("   ℹ️ ACM, KW and the FF strip cover DIFFERENT windows and horizons: co-movement is consistent with both "
          "channels, NOT a causal decomposition (CATO 9/28).")
    return findings


def mbs_rearm(today: dt.date) -> int:
    print("\n== VX-BND-17 RE-ARM WATCHER (MBS relay DORMANT since 8/18; spread leg only; weekly survey − daily Treasury) ==")
    try:
        mort = _fred("MORTGAGE30US", 12)
        ust = dict(_fred("DGS10", 60))
    except Exception as e:
        print(f"   🔴 GAP — watcher not read ({e}). NOT a pass.")
        return 1
    band = f"{MBS_BAND[0]*100:.0f}–{MBS_BAND[1]*100:.0f}bp"
    for d, mv in mort[-3:]:
        k = join_prior(list(ust), d)
        if k is None:
            print(f"   {d}  PMMS 30Y {mv:.2f} − (no DGS10 within {JOIN_MAX_BD} business days before) → not computable")
            continue
        bp, state = mbs_state(mv, ust[k])
        print(f"   {d}  PMMS 30Y {mv:.2f} − DGS10 {ust[k]:.2f} [{k}] = {bp}bp  → {state} {band}")
    d, mv = mort[-1]
    for why in stale_reasons(today, pmms_date=d):
        print(f"   🔴 GAP — {why}; NO current verdict on the re-arm leg.")
        return 1
    k = join_prior(list(ust), d)
    if k is None:
        print(f"   🔴 GAP — no DGS10 close within {JOIN_MAX_BD} business days before the {d} PMMS; NO current verdict.")
        return 1
    bp, state = mbs_state(mv, ust[k])
    findings = 0
    if state != "INSIDE":
        print(f"   🔴 RE-ARM TRIGGER (spread leg) FIRED: {bp}bp is {state} the band — VX-BND-17 re-arm REVIEW owed "
              f"(not a reactivation, not a trade); coordinate HOMER/REGINALD (per the VX row).")
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
    fails = count = 0

    def check(label, ok):
        nonlocal fails, count
        count += 1
        fails += 0 if ok else 1
        print(f"  {'PASS' if ok else 'FAIL'}  {label}")

    print("[rates_context --selftest]\n")
    t = zq_tickers(dt.date(2026, 11, 3), 3)
    check("tickers roll the year: Nov-26 → X26, Z26, F27", [x[1] for x in t] == ["ZQX26.CBT", "ZQZ26.CBT", "ZQF27.CBT"])
    strip = [("2026-10", 3.893, "2026-09-28"), ("2026-11", 4.05, "2026-09-28"), ("2027-11", 4.855, "2026-09-28"),
             ("2027-12", 4.845, "2026-09-28"), ("2028-01", 4.81, "2026-09-28"), ("2028-02", 4.99, "2026-09-25")]
    s = strip_summary(strip, 3.88)
    check("peak = Nov-27 4.855 (+97.5bp ≈ 3.9 hikes)", (s["terminal_month"], s["terminal"], s["cum_bp"], s["hikes"]) == ("2027-11", 4.855, 97.5, 3.9))
    check("a STALE bar is excluded, never the peak", s["stale"] == ["2028-02"] and s["n_live"] == 5)
    check("post-peak decline reported; not 'rising at end'", s["after_peak_bp"] == -4.5 and not s["rising_at_end"])
    check("a strip still rising at its last contract is flagged (terminal NOT established)",
          strip_summary([("2026-10", 3.9, "d"), ("2026-11", 4.0, "d")], 3.88)["rising_at_end"])
    by = {m: r for m, r, _ in strip[:5]}
    bp, how = next_meeting_odds(by, 3.88, dt.date(2026, 10, 28), [dt.date(2026, 10, 28), dt.date(2026, 12, 9)])
    check("10/28 → next-month (Nov) method, +17bp", bp == 17.0 and how.startswith("next-month"))
    bp, how = next_meeting_odds(by, 3.88, dt.date(2026, 10, 28), [dt.date(2026, 10, 28), dt.date(2026, 11, 4)])
    check("next-month method VOIDED when an FOMC falls in that month", bp is None and "void" in how)
    bp, _ = next_meeting_odds({"2026-12": 4.0}, 3.88, dt.date(2026, 12, 9), [dt.date(2026, 12, 9)])
    check("in-month method backs out the post-meeting rate (Dec 9: 22 days after)", bp == round(((4.0 * 31 - 3.88 * 9) / 22 - 3.88) * 100, 1))
    check("pricing: 17bp → '68%' of a HIKE", "68% of a 25bp HIKE" in describe_pricing(17.0))
    check("pricing: 31bp → raw bp, 'NOT a probability', no % (BR3's '124%' case)", "NOT a probability" in describe_pricing(31.0) and "%" not in describe_pricing(31.0))
    check("pricing: −10bp → CUT reading", "CUT" in describe_pricing(-10.0))
    rows = [("2026-10-28", "🔴 **OCTOBER FOMC DECISION, 2:00 PM ET**"), ("2026-10-08", "FOMC MINUTES (decision recap)"),
            ("2026-09-16", "SEPTEMBER FOMC DECISION"), ("watch", "FOMC DECISION something")]
    check("docket parser: future DECISION rows only", docket_fomc(rows, dt.date(2026, 9, 28)) == [dt.date(2026, 10, 28)])
    check("docket parser: nothing future → empty (the caller FLAGS it)", docket_fomc(rows, dt.date(2026, 10, 29)) == [])
    T = dt.date(2026, 9, 28)
    iss = [dt.date(2026, 9, 16), dt.date(2026, 10, 28), dt.date(2026, 12, 9), dt.date(2027, 1, 27)]
    n, miss, _ = calendar_check([dt.date(2026, 12, 9)], iss, T)
    check("BR3 issuer: Oct deleted from docket → next = Oct 28 (issuer) AND Oct flagged missing", n == dt.date(2026, 10, 28) and dt.date(2026, 10, 28) in miss)
    n, miss, _ = calendar_check([dt.date(2026, 10, 28), dt.date(2026, 12, 9)], iss, T)
    check("issuer: complete docket → no missing rows (Jan-27 is outside the window)", n == dt.date(2026, 10, 28) and miss == [])
    n, _, note = calendar_check([dt.date(2026, 12, 9)], None, T)
    check("BR3 fallback: Dec-only docket, issuer unavailable → UNRESOLVED (72d > 63d)", n is None and "INCOMPLETE" in note)
    n, _, note = calendar_check([dt.date(2026, 10, 28)], None, T)
    check("fallback: Oct 28 docketed, no record → 'next DOCKETED meeting — calendar completeness UNVERIFIED'", n == dt.date(2026, 10, 28) and "UNVERIFIED" in note)
    page = ('<h4>2026 FOMC Meetings</h4><div class="fomc-meeting__month"><strong>April/May</strong></div>'
            '<div class="fomc-meeting__date">30-1</div><div class="fomc-meeting__month"><strong>October</strong></div>'
            '<div class="fomc-meeting__date">27-28</div><h4>2027 FOMC Meetings</h4>'
            '<div class="fomc-meeting__month"><strong>January</strong></div><div class="fomc-meeting__date">26-27*</div>')
    check("issuer parser: decision day, cross-month range, starred SEP meetings",
          parse_fomc_calendar(page) == [dt.date(2026, 5, 1), dt.date(2026, 10, 28), dt.date(2027, 1, 27)])
    check("bd_age: Fri → Mon = 1 business day", bd_age(dt.date(2026, 9, 25), dt.date(2026, 9, 28)) == 1)
    check("BR1: an 8/10 bar on 9/28 exceeds the futures tolerance", bd_age(dt.date(2026, 8, 10), T) > FUT_MAX_BD)
    check("#5 join: PMMS earlier than every DGS10 → None, never raises", join_prior(["2026-09-24"], "2026-09-10") is None)
    check("BR1 join: current PMMS vs a six-week-old DGS10 → None", join_prior(["2026-08-13"], "2026-09-24") is None)
    check("join: same-day DGS10 accepted", join_prior(["2026-09-23", "2026-09-24"], "2026-09-24") == "2026-09-24")
    check("MBS 9/24 real case: 7.03 − 5.18 = 185bp INSIDE", mbs_state(7.03, 5.18) == (185, "INSIDE"))
    check("MBS band edges inclusive: 180 and 230 INSIDE", mbs_state(6.80, 5.00)[1] == "INSIDE" and mbs_state(7.30, 5.00)[1] == "INSIDE")
    check("MBS 179bp BELOW, 231bp ABOVE", mbs_state(6.79, 5.00)[1] == "BELOW" and mbs_state(7.31, 5.00)[1] == "ABOVE")
    # BR4 — PROME's branch spec (bar date vs capture time; UNKNOWN when it cannot be established)
    L = bar_timing_label
    check("BR4: 11:00 ET, no bar date → UNKNOWN, never 'prior session'",
          "UNKNOWN" in L(dt.datetime(2026, 9, 28, 11, 0)) and "prior session" not in L(dt.datetime(2026, 9, 28, 11, 0)))
    check("BR4: 11:00 weekday with TODAY's bar → EVOLVING, not a close", "EVOLVING" in L(dt.datetime(2026, 9, 28, 11, 0), "2026-09-28"))
    check("BR4: 16:30 weekday with today's bar → still EVOLVING (session open to 17:00)", "EVOLVING" in L(dt.datetime(2026, 9, 28, 16, 30), "2026-09-28"))
    check("BR4: 17:30 weekday with today's bar → last vendor print after the halt", "last vendor print" in L(dt.datetime(2026, 9, 28, 17, 30), "2026-09-28"))
    check("BR4: 19:00 weekday with today's bar → may carry NEXT-SESSION trades (L462)", "NEXT-SESSION" in L(dt.datetime(2026, 9, 28, 19, 0), "2026-09-28"))
    check("BR4: Saturday with Friday's bar → prior session's vendor close", "prior session" in L(dt.datetime(2026, 9, 26, 16, 30), "2026-09-25"))
    check("BR4: Monday 11:00 with Friday's bar → prior session's vendor close", "prior session" in L(dt.datetime(2026, 9, 28, 11, 0), "2026-09-25"))
    check("BR4: a bar two sessions old → UNKNOWN", "UNKNOWN" in L(dt.datetime(2026, 9, 28, 11, 0), "2026-09-24"))
    check("BR4: bar dated after capture → NEXT-SESSION bar", "NEXT-SESSION bar" in L(dt.datetime(2026, 9, 28, 19, 0), "2026-09-29"))
    check("BR4: every branch keeps 'NOT settlement'", all("NOT settlement" in L(dt.datetime(2026, 9, 28, h, 0), b)
          for h, b in [(11, None), (11, "2026-09-28"), (19, "2026-09-28"), (11, "2026-09-25"), (11, "2026-09-24")]))
    # BR1 — PROME's neighbour cases
    check("BR1 ordinary: 9/28 strip + 9/25 EFFR on 9/28 → fresh", stale_reasons(T, effr_date="2026-09-25", bar_date="2026-09-28") == [])
    check("BR1 weekend: Saturday 9/26 read, Friday bars, Thursday EFFR → fresh",
          stale_reasons(dt.date(2026, 9, 26), effr_date="2026-09-24", bar_date="2026-09-25") == [])
    check("BR1 weekly: Thursday PMMS read the following Monday → fresh", stale_reasons(T, pmms_date="2026-09-24") == [])
    check("BR1 overlap: fresh strip + 8/7 EFFR → stale", len(stale_reasons(T, effr_date="2026-08-07", bar_date="2026-09-28")) == 1)
    check("BR1: 8/10 strip → stale", len(stale_reasons(T, bar_date="2026-08-10")) == 1)
    check("BR1: 8/13 PMMS → stale", len(stale_reasons(T, pmms_date="2026-08-13")) == 1)
    check("#5 missing: empty DGS10 window → None, never raises", join_prior([], "2026-09-24") is None)
    # BR2 — label and coverage
    s17 = strip_summary([(f"m{i:02d}", 4.0 + i / 100, "2026-09-28") for i in range(17)] + [("m17", 4.9, "2026-09-25")], 3.88)
    check("BR2 ordinary: 17 live contracts ≥ MIN_LIVE", s17["n_live"] == 17 and s17["n_live"] >= MIN_LIVE)
    thin = strip_summary([("m0", 3.9, "2026-09-28")] + [(f"m{i}", 4.0, "2026-09-25") for i in range(1, 6)], 3.88)
    check("BR2 overlap: 6 raw / 1 live → below MIN_LIVE", thin["n_live"] == 1 < MIN_LIVE)
    check("BR2: printed line says 'PEAK OF AVAILABLE STRIP' with its horizon, never bare 'TERMINAL'",
          peak_line(s).startswith("PEAK OF AVAILABLE STRIP (2026-10→2028-01") and "TERMINAL" not in peak_line(s))
    # BR3 — recorded issuer calendar
    rec = "# source: x\n# checked: 2026-09-28 18:20 ET by BOND\ndecision_date\n2026-10-28\n2026-12-09\n2027-12-08\n"
    ck, ds = parse_calendar_record(rec)
    check("parser: abbreviated cross-month 'Jan/Feb 31-1' → Feb 1 (the 2023 silent drop)",
          parse_fomc_calendar('<h4>2023 FOMC Meetings</h4><div class="fomc-meeting__month"><strong>Jan/Feb</strong></div>'
                              '<div class="fomc-meeting__date">31-1</div>') == [dt.date(2023, 2, 1)])
    check("record guard: a year with 6 meetings is REFUSED", year_count_issues([dt.date(2023, m, 1) for m in range(1, 7)]) == ["2023: 6 meetings (expected 8)"])
    check("BR3 record parses: check date + meetings", ck == dt.date(2026, 9, 28) and ds[0] == dt.date(2026, 10, 28))
    check("BR3 record fresh and long enough → no issue", record_issues(ck, ds, T) == [])
    check("BR3 record > 90d old → issue", len(record_issues(dt.date(2026, 6, 1), ds, T)) == 1)
    check("BR3 record ending inside the window → issue", len(record_issues(ck, [dt.date(2026, 10, 28)], T)) == 1)
    try:
        parse_calendar_record("decision_date\n2026-10-28\n"); bad = False
    except ValueError:
        bad = True
    check("BR3 record without a '# checked:' line is REFUSED", bad)
    print(f"\n  {'ALL PASS' if not fails else str(fails) + ' FAILURE(S)'} — {count} fixtures")
    return 1 if fails else 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    if "--record-calendar" in sys.argv:
        sys.exit(record_calendar())
    sys.exit(1 if run() else 0)
