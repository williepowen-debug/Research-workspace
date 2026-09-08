#!/usr/bin/env python3
"""
BRENT Instrument Check — does every registered test have a WORKING instrument?

Registry: workbook/REGISTRY.tsv  (consolidated 2026-08-04; absorbed the former INSTRUMENTS.tsv
          AND thresholds.py's hardcoded level tables -- one machine home for level + instrument)

WHY THIS EXISTS (built 2026-08-04, after DEPLOY GATE v2 turned out to be unfillable):
LESSONS #21 says a threshold fails on its SPEC before it fails on the world.
LESSONS #22 says a test must name an instrument that actually TRADES in the window
it will be graded in. This script is #22 pointed at GATES rather than pre-registrations.

It answers four questions a spec review CANNOT answer by reading:
  1. EXISTS       — is an instrument even declared? ("none" is a real, common answer)
  2. REACHABLE    — does a probe return data right now?
  3. FRESH        — is the newest datapoint inside the test's own staleness budget?
  4. FEASIBLE     — for a test that must be graded AND acted on in one session,
                    does the instrument still print while the ACTION market is open?

(4) is the one that is invisible to every other check in the kit, and it is the one
that cost a ratified gate: ^OVX's last bar is 16:00 and USO options close 16:00, so
DEPLOY GATE v2's leg (a) became knowable at exactly the moment leg (b) became
ungradeable. Zero-minute execution window, ratified, and undetected for five days.

⚠️  DELIBERATELY NOISY ABOUT ITS OWN BLIND SPOTS. A silent pass here would be worse
    than no check (`finding_verification_zero_is_ambiguous`), so the summary always
    states how many rows were actually PROBED vs merely asserted.

Exit codes:
  0 = ran clean, nothing blocking
  2 = RAN CORRECTLY and FOUND blocking 🔴 findings (DEAD / NO_INSTRUMENT / WINDOW_INFEASIBLE)
  1 = the SCRIPT ITSELF failed (bad registry, unreadable file)

⚠️  2-not-1 is deliberate. Collapsing "found problems" into the same code as "crashed"
    is how a broken tool hides: this morning `eia_weekly.py` showed FAIL in the boot
    summary purely because of a wrapper timeout, and a real data outage would have looked
    identical. A check whose findings are indistinguishable from its own failure is a
    check you stop reading.

Usage:
  .venv/bin/python3 AGENTS/BRENT/scripts/instrument_check.py
  .venv/bin/python3 AGENTS/BRENT/scripts/instrument_check.py --quick   # skip network probes
  .venv/bin/python3 AGENTS/BRENT/scripts/instrument_check.py --json
"""

import argparse
import csv
import json
import io
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

BRENT_DIR = Path(__file__).resolve().parent.parent
REGISTRY = BRENT_DIR / "workbook" / "REGISTRY.tsv"   # consolidated 2026-08-04; was INSTRUMENTS.tsv

# When the ACTION market closes, ET. Used only for window_req=same_session_action.
# US equity/ETF options close 16:00 ET; the broad-based ETFs (SPY/QQQ/IWM/DIA) run to 16:15.
ACTION_CLOSE_ET = {"_default": "16:00", "SPY": "16:15", "QQQ": "16:15", "IWM": "16:15", "DIA": "16:15"}

# ⚠️ LOAD-BEARING, NOT COSMETIC — 2026-08-21.
# Some publishers' WAFs TARPIT a self-identifying User-Agent: they do not 403, they simply
# never respond, so the caller reads TimeoutError and concludes THE HOST IS DOWN.
# MEASURED at rigcount.bakerhughes.com, same URL, back to back:
#     UA "BRENT-instrument-check/1.0" -> TimeoutError at BOTH 20s and 45s (so not a timeout-tuning issue)
#     UA <this browser string>        -> HTTP 200, 4096B, in 0.1-0.4s
# COST OF NOT KNOWING THIS: every BRT-26 rig grade from 7/31 to 8/14 was taken off AGGREGATORS and
# recorded with the standing caveat "the Baker Hughes PRIMARY TIMED OUT AGAIN (http=000) — I have
# still never reached the true primary." The primary was never down. It was declining to talk to me.
# ⛔ A HANG AND AN OUTAGE ARE INDISTINGUISHABLE AT THE CALLER, AND ONLY ONE OF THEM IS THE HOST'S FAULT.
# ⚠️ THIS FILE ALREADY KNEW: probe_gie() has carried this exact fix + a "check the User-Agent FIRST"
# comment since the EU-STORAGE work. The lesson was learned in one function and never carried to the
# one next to it. [[finding_record_of_an_action_is_not_the_action]] — across FUNCTIONS in ONE FILE.
# ⚠️ CAVEAT: keyless-via-browser-UA is undocumented publisher behavior and can tighten without notice.
BROWSER_UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

# ⚑ ADDED 2026-09-07. supersedes: none — EXTENDS BROWSER_UA, does not replace it.
#
# ⛔ THE FINDING THAT FORCED THIS, AND IT CORRECTS A RECORDED ONE: the 2026-09-06 SCRATCH
# diagnosed the Baker Hughes 403 as "usage-triggered WAF, NOT a header defect." That is WRONG,
# and it was wrong in the direction that costs a grade. Falsified 2026-09-07 on rigcount
# .bakerhughes.com, back to back, same box, same minute:
#     BROWSER_UA alone ................. HTTP 403 Forbidden
#     BROWSER_UA + the headers below ... HTTP 200, 27,016 B
# The gate is the HEADER SHAPE — a real browser sends Sec-Fetch-*/Accept-Language/Accept, and
# the WAF checks for them. A UA is necessary and NOT sufficient. The 9/6 note reached "not a
# header defect" because it only ever varied the UA, so the one axis that mattered was held
# fixed across every trial. [[finding_crosscheck_with_free_parameter_validates_nothing]]
#
# ⚠️ SCOPED DELIBERATELY: used by probe_bhrigs ONLY. The other probes keep bare BROWSER_UA
# because they are GREEN on it today, and widening a working probe's request shape to match a
# broken one's is an untested change to a passing check. If another probe starts 403ing, this
# is the first thing to try — that is why it is module-level and not local.
BROWSER_HEADERS = {
    "User-Agent": BROWSER_UA,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "identity",          # identity: we parse bytes, never a gzip stream
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Connection": "keep-alive",
}

RED, AMBER, GREEN = "🔴", "🟠", "✅"


def load_registry():
    rows = []
    with open(REGISTRY, newline="", encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            rows.append(line.rstrip("\n"))
    rdr = csv.DictReader(rows, delimiter="\t")
    # RETIRED rows stay in the registry as the do-not-resurrect list, but are not probed.
    return [r for r in rdr if r.get("test_id") and r.get("status", "live") != "retired"]


# ---------------------------------------------------------------------------
# Probes. Each returns (ok, last_dt_or_None, detail)
# ---------------------------------------------------------------------------

# ---- LIVE EIA v2 access for probe_eia(): reuse FORGE's tested eia_fetch (key from gitignored .env) ----
# Same import pattern eia_weekly.py already uses, so there is ONE EIA read-path on this desk, not two.
try:
    _FORGE_MD = str(Path(__file__).resolve().parents[3] / "FORGE" / "tools" / "market-data")
    if _FORGE_MD not in sys.path:
        sys.path.insert(0, _FORGE_MD)
    import fetch as _forge_eia
    HAVE_FORGE_EIA = True
except Exception:
    _forge_eia = None
    HAVE_FORGE_EIA = False


def probe_yf(ticker, want_intraday=False):
    try:
        import yfinance as yf
    except ImportError:
        return None, None, "yfinance not installed"
    try:
        t = yf.Ticker(ticker)
        d = t.history(period="10d")
        if d.empty:
            return False, None, "no daily bars returned"
        last = d.index[-1].to_pydatetime()
        detail = f"last daily bar {last.date()}, close {float(d['Close'].iloc[-1]):.2f}"
        if want_intraday:
            i = t.history(period="5d", interval="5m")
            if not i.empty:
                i.index = i.index.tz_convert("America/New_York")
                # last COMPLETE session in the series, so an in-progress day can't
                # masquerade as an early close (the 13:40 bar on a live afternoon).
                days = sorted({x.date() for x in i.index})
                ref = days[-2] if len(days) > 1 else days[-1]
                sub = i[[x.date() == ref for x in i.index]]
                detail += f" | last intraday print {sub.index[-1].strftime('%H:%M')} ET (on {ref})"
                return True, last, detail
            detail += " | NO intraday bars"
        return True, last, detail
    except Exception as e:
        return False, None, f"probe error: {type(e).__name__}: {e}"


def last_intraday_time_et(ticker):
    """LATEST clock time this ticker prints, taken as the MAX across recent complete
    sessions — never a single session's final bar.

    ⚠️  This is deliberately the CONSERVATIVE (defect-revealing) choice and v1 of this
    function got it wrong. Sampling only the most recent complete session read ^OVX as
    stopping at 15:55 (8/3 had a thin final bar), which reported the DEPLOY GATE v2
    defect as WINDOW_TIGHT/5min instead of WINDOW_INFEASIBLE/0min. 7/31 shows the true
    16:00. An instrument that prints to 16:00 on ANY session prints to 16:00.
    Understating an instrument's reach understates the window defect — i.e. v1 failed
    in the COMFORTING direction, which is the failure mode this whole script exists for.
    """
    try:
        import yfinance as yf
        # prepost=False: the REGULAR session is the basis for "when can I still act".
        i = yf.Ticker(ticker).history(period="10d", interval="5m", prepost=False)
        if i.empty:
            return None
        i.index = i.index.tz_convert("America/New_York")
        days = sorted({x.date() for x in i.index})
        complete = days[:-1] if len(days) > 1 else days   # drop an in-progress today
        if not complete:
            return None
        # ⚠️ 5m bars are LABELLED BY THEIR START. The 15:55 bar covers 15:55–16:00, so the
        # instrument prints until 16:00, not 15:55. v1 compared the LABEL against the action
        # close and therefore reported a phantom 5-minute window on a gate whose real window
        # is ZERO — understating the exact defect this script was built to catch.
        latest = max(max(x for x in i.index if x.date() == d) for d in complete)
        return (latest + timedelta(minutes=5)).strftime("%H:%M")
    except Exception:
        return None


def first_intraday_time_et(ticker):
    """EARLIEST clock time this ticker prints — the moment an EXISTENCE-form test first
    becomes evaluable. Taken as the MAX across recent complete sessions of each session's
    FIRST bar, i.e. the LATEST that trading has actually opened.

    ⚠️  Deliberately the CONSERVATIVE choice in the same direction as its `last_` twin:
    a LATER assumed open means a SMALLER computed window, so an error here understates
    the window and over-reports the defect. Both helpers must fail toward ALARMING, never
    toward COMFORTING — that asymmetry is the whole point of this script
    (`[[finding_test_the_guard_not_just_the_guarded]]`).
    Bars are labelled by their START, so the first bar's label IS the first print time —
    no +5min adjustment here, unlike `last_intraday_time_et`.
    """
    try:
        import yfinance as yf
        i = yf.Ticker(ticker).history(period="10d", interval="5m", prepost=False)
        if i.empty:
            return None
        i.index = i.index.tz_convert("America/New_York")
        days = sorted({x.date() for x in i.index})
        complete = days[:-1] if len(days) > 1 else days
        if not complete:
            return None
        return max(min(x for x in i.index if x.date() == d) for d in complete).strftime("%H:%M")
    except Exception:
        return None


# ---------------------------------------------------------------------------
# ⚑ READING BASIS (added 2026-08-05) — `window_req` = "same_session_action[:BASIS]".
#
# WHY: v1 computed EVERY same-session window as `action_close − LAST print`. That is the
# right test only for a reading that needs the instrument's FINAL value. It produced a
# FALSE 🔴 on DEPLOY GATE v3 leg (a2) — an EXISTENCE-form test ("OVX must PRINT ≤ the line
# at the ticket"), which is evaluable and actionable from the opening bell. v1 reported a
# 0-minute window on a leg whose real window is ~6.5 HOURS, on the gate ratified the day
# before. A false red on a live gate is corrosive twice over: it makes the flagship class
# noisy, and a permanently-red row decays into decoration — the exact disease that retired
# the `crack >$30` line on 7/31.
#
#   :final  the test needs the instrument's FINAL/closing value, or a session aggregate
#           not known until the close (e.g. a close-to-close % move).
#           window = action_close − LAST print.
#   :any    EXISTENCE form — satisfied by ANY qualifying print during the session, so it is
#           evaluable from the open.  window = action_close − FIRST print.
#
# ⛔ A BARE `same_session_action` (no suffix) IS TREATED AS `:final`. That is deliberate and
# fail-safe: an undeclared row keeps firing the conservative red rather than silently
# passing. The LOOSENING must be declared PER ROW, never inferred — otherwise this fix
# would quietly weaken the check on every row that predates it, which is precisely the
# "did a red disappear because the scanner got weaker?" failure RAV's WP7 asks about.
# ---------------------------------------------------------------------------

def needs_same_session(row):
    return (row.get("window_req") or "").split(":", 1)[0].strip() == "same_session_action"


def window_basis(row):
    parts = (row.get("window_req") or "").split(":", 1)
    return parts[1].strip().lower() if len(parts) == 2 and parts[1].strip() else "final"


def _fred_key():
    """Same resolution order as thresholds.py: env, then the gitignored FORGE .env."""
    import os
    k = os.environ.get("FRED_API_KEY", "")
    if k:
        return k
    f = BRENT_DIR.parent.parent / "FORGE/tools/market-data/.env"
    if f.exists():
        for line in f.read_text().splitlines():
            if line.startswith("FRED_API_KEY="):
                return line.split("=", 1)[1].strip()
    return ""


def probe_fred(series):
    """FRED observations — returns the newest observation DATE, which is the whole point:
    a FRED series can answer 200 and still be months behind (GASREGW is weekly, BAMLH0A0HYM2
    lags a day). Reachability alone would be a false green.

    ⚠️ ADDED DURING THE 2026-08-04 CONSOLIDATION, and it was NOT cosmetic: folding the FRED
    threshold rows into the shared registry put 10 rows in front of a checker that had no
    fred: prober, so they all reported 🔴 DEAD on a source that works perfectly. Ten false
    positives would have been worse than no check — it is exactly the "a structural edit can
    silently change operational meaning" failure RAV flagged when approving this work.
    """
    key = _fred_key()
    if not key:
        return None, None, "FRED_API_KEY not found (env or FORGE/tools/market-data/.env)"
    url = ("https://api.stlouisfed.org/fred/series/observations"
           f"?series_id={series}&api_key={key}&file_type=json&sort_order=desc&limit=1")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "BRENT-instrument-check/1.0"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            obs = json.loads(resp.read()).get("observations", [])
        if not obs:
            return False, None, "no observations returned"
        d = obs[0].get("date")
        val = obs[0].get("value")
        last = datetime.fromisoformat(d)
        return True, last, f"last observation {d} = {val}"
    except Exception as e:
        return False, None, f"unreachable: {type(e).__name__}: {e}"


def probe_http(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": BROWSER_UA})
        with urllib.request.urlopen(req, timeout=20) as resp:
            if resp.status != 200:
                return False, None, f"HTTP {resp.status}"
            body = resp.read(4096)
            if len(body) < 64:
                return False, None, f"HTTP 200 but body only {len(body)}B — treat as empty"
            # ⚠️ A 200 proves the HOST answered, NOT that the DATA PARTITION is publishing.
            # This is `finding_partitioned_source_returns_stale_window_at_200` — the exact
            # shape of the PortWatch failure: chokepoint6 serves clean 200s while having
            # published nothing since 7/23, so it reads as "the data ends here" rather
            # than as a fault. Reachability is NEVER evidence of freshness here; the
            # staleness verdict must come from last_verified, and it is not optional.
            return True, None, (f"HTTP 200, {len(body)}B sampled — ⚠️ reachability only; "
                                f"a 200 does NOT prove the data partition is current")
    except Exception as e:
        return False, None, f"unreachable: {type(e).__name__}: {e}"


def probe_arcgis(spec):
    """ArcGIS FeatureServer probe — returns the REAL newest datapoint date.

    Grammar: arcgis:<query-endpoint-url>|<where-clause>|<date-field>

    ⚑ WHY THIS EXISTS (2026-08-07, BRENT). `probe_http` deliberately derives freshness
    from `last_verified` because PortWatch serves clean 200s on a stale partition
    (`finding_partitioned_source_returns_stale_window_at_200`). That is correct and stays.
    But it has a FALSE-RED twin nobody had named: a source that HEALS stays red until a
    HUMAN re-stamps `last_verified`. chokepoint6 recovered ~2026-08-03 and boot was still
    reporting "15d stale" on 08-07 — five days of a red on a healthy series, which is the
    same disease as a green on a dead one: a confident answer over an inadequate scope.

    The fix is not to trust the 200 — it is to STOP PROBING THE LANDING PAGE AND QUERY THE
    DATA. This asks the FeatureServer for the max date in the partition and reports it, so
    freshness comes from the SERIES, never from a human stamp and never from reachability.

    supersedes: none — EXTENDS the probe grammar (retirement ratchet). `http:` rows are
    untouched and keep their fail-safe last_verified semantics.
    """
    try:
        parts = spec.split("|")
        if len(parts) != 3:
            return None, None, f"bad arcgis grammar (want url|where|datefield): {spec!r}"
        url, where, datefield = (x.strip() for x in parts)
        q = {"where": where, "outFields": datefield,
             "orderByFields": f"{datefield} DESC", "resultRecordCount": "1", "f": "json"}
        req = urllib.request.Request(url + "?" + urllib.parse.urlencode(q),
                                     headers={"User-Agent": "BRENT-instrument-check/1.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = json.loads(resp.read())
        if body.get("error"):
            return False, None, f"service error: {body['error'].get('message', '?')}"
        feats = body.get("features") or []
        if not feats:
            # A 200 with zero rows is the partition-stale shape — FAIL LOUD, never "fresh".
            return False, None, "HTTP 200 but the partition returned ZERO rows for this where-clause"
        raw = feats[0]["attributes"].get(datefield)
        if raw is None:
            return False, None, f"newest row has no {datefield}"
        # ArcGIS date fields are epoch-millis
        last = (datetime.utcfromtimestamp(raw / 1000) if isinstance(raw, (int, float))
                else datetime.fromisoformat(str(raw)[:10]))
        return True, last, f"newest datapoint {last.date()} (queried live, not last_verified)"
    except Exception as e:
        return False, None, f"unreachable: {type(e).__name__}: {e}"


def probe_eia(spec):
    """EIA v2 weekly-series probe — returns the REAL newest period, not a reachability 200.

    Grammar: eia:<route>|<series_id>   e.g. eia:petroleum/stoc/wstk|W_EPC0_SAX_YCUOK_MBBL

    ⚑ WHY THIS EXISTS (2026-08-28, BRENT). `CUSHING-20M` carried the probe
    `manual:EIA v2 API via eia_weekly.py`. A `manual:` probe is NEVER network-checked, so
    this checker fell back to `last_verified` — a HUMAN STAMP — and reported the row
    STALE at 15d against a 10d budget. ⛔ THE SERIES WAS NEVER STALE: `eia_weekly.py`
    pulls it LIVE at every boot and printed Cushing 22.43M for wk-2026-08-21 in the very
    same boot that rendered the row amber. The row went red because nobody re-stamped it,
    not because any datum aged.

    ★ THIS IS THE FALSE-RED TWIN ALREADY FIXED ONCE ON THIS REGISTRY. On 2026-08-07 the
    `KILL-LEG2-TRANSIT` probe was repointed from a landing page (`http:`) to the
    FeatureServer QUERY path (`arcgis:`) precisely so "freshness is now read from the
    SERIES itself, live, never from last_verified and never from reachability" — and that
    row's own note names the failure mode: "a source that HEALS stayed red until a human
    re-stamped it." Same disease, different row, three weeks later. The lesson had been
    written down and the sweep for OTHER instances of it never happened
    `[[finding_a_ruling_governs_the_next_write_not_the_existing_state]]`.

    ⚠️ A manual: probe is not wrong in itself — it is right for a genuinely human-graded
    test. It is wrong HERE because a machine-readable series exists and is already being
    pulled every boot. Do not convert manual: rows wholesale; convert the ones with a live
    read-path, and leave the rest honestly manual.

    ⛔ NO LEVEL MOVED BY ADDING THIS: 20.0M is untouched, direction untouched, budget
    untouched. Instrument repair only — the same scope as the 8/21 BRT-26-RIGS probe fix.
    """
    if "|" not in spec:
        return False, None, f"bad eia: grammar {spec!r} — want eia:<route>|<series_id>"
    route, series_id = spec.split("|", 1)
    if not HAVE_FORGE_EIA:
        return None, None, "FORGE fetch.eia_fetch unavailable (path or import failed)"
    if not getattr(_forge_eia, "EIA_API_KEY", ""):
        return None, None, "EIA_API_KEY not set (FORGE/tools/market-data/.env)"
    try:
        rows = _forge_eia.eia_fetch(series_id, route=route, limit=2)
    except Exception as e:
        return False, None, f"unreachable: {type(e).__name__}: {e}"
    if not rows:
        return False, None, "empty response — treat as FAILURE, never as 'no data exists'"
    if isinstance(rows[0], dict) and rows[0].get("error"):
        return False, None, f"API error: {rows[0]['error']}"
    d = rows[0].get("date")
    v = rows[0].get("value")
    if not d:
        return False, None, f"no period in newest row: {rows[0]!r}"
    try:
        last = datetime.fromisoformat(str(d)[:10])
    except Exception:
        return False, None, f"unparseable period {d!r}"
    return True, last, f"newest period {d} = {v}"


def probe_gie(spec):
    """GIE AGSI+ / ALSI+ probe — returns the REAL newest gas-day, not a reachability 200.

    Grammar: gie:<api-url>          e.g. gie:https://agsi.gie.eu/api/data/eu

    ⚑ WHY THIS EXISTS (2026-08-13, BRENT). The `EU-STORAGE` row sat 🔴 NO_INSTRUMENT from
    2026-08-02, blocked on a GIE API key that was never the gate. GIE denies by USER-AGENT
    and its denial text MISNAMES ITS OWN DISCRIMINATOR: a short/plain UA gets
    `{"error":"access denied","message":"Invalid or missing API key"}` — so an 11-day
    blocker was created by a server error string, not by a missing credential. An identical
    URL with a full browser UA returns the full dataset, keyless. Reproduced by PROME
    2026-08-12 and again by BRENT 2026-08-13 (bare UA -> the key error; browser UA -> data).
    `[[finding_audit_resolution_path_before_reattempt]]` — blocked by the PATH, not the data.

    TWO FAIL-LOUD GUARDS, both from measured failure shapes:
      1. `total == 0` — AGSI/ALSI answer HTTP 200 with an EMPTY payload on a malformed
         query AND on a UA denial. A 200 is therefore NEVER evidence here; `total` is.
      2. Freshness comes from the newest `gasDayStart` IN THE PAYLOAD, never from
         `last_verified` and never from the 200 — the `probe_arcgis` lesson applied to a
         second source.

    ⚠️ CAVEAT THAT TRAVELS WITH EVERY USE: keyless-via-browser-UA is UNDOCUMENTED behavior
    and can tighten without notice. The official free GIE key remains the robust path
    (Will queue row 37 — HARDENING ONLY, no longer blocking). If this probe starts
    returning the key error again, that is the tightening, not a regression to diagnose.

    supersedes: none — EXTENDS the probe grammar (retirement ratchet), like `arcgis:`.
    """
    # Full browser UA is LOAD-BEARING, not cosmetic — see docstring and the module-level
    # BROWSER_UA note. The local shadow was REMOVED 2026-08-21 when probe_http was found to
    # need the identical fix: one definition, so the next probe that needs it inherits it.
    try:
        req = urllib.request.Request(spec.strip(), headers={"User-Agent": BROWSER_UA})
        with urllib.request.urlopen(req, timeout=30) as resp:
            if resp.status != 200:
                return False, None, f"HTTP {resp.status}"
            body = json.loads(resp.read())
        if body.get("error"):
            return False, None, (f"GIE error: {body.get('message', '?')} "
                                 f"(⚠️ if this says 'API key', check the User-Agent FIRST — "
                                 f"GIE's error text misnames its own gate)")
        # Guard 1: HTTP 200 with total:0 is the malformed-query / denial shape. Fail loud.
        if int(body.get("total") or 0) == 0:
            return False, None, "HTTP 200 but total=0 — empty payload, treat as a FAILURE not as data"
        rows = body.get("data") or []
        if not rows:
            return False, None, "HTTP 200, total>0, but data[] is empty"
        # Guard 2: freshness from the payload's own newest gas day.
        last = datetime.fromisoformat(str(rows[0].get("gasDayStart"))[:10])
        full = rows[0].get("full")
        return True, last, (f"newest gas day {last.date()}, full={full}% "
                            f"(queried live, total={body.get('total')}; keyless via browser UA)")
    except Exception as e:
        return False, None, f"unreachable: {type(e).__name__}: {e}"


def probe_bhrigs(spec):
    """Baker Hughes North America rig count — grammar: `bhrigs:<listing-url>|<link-text>`.

    Grades BRT-26 (US OIL rig count vs the frozen 457 line). supersedes: the `http:` probe on
    the BRT-26-RIGS registry row, which is RETIRED by this — it pinned a /static-files/<uuid>
    that no longer exists on the page (verified 2026-09-07: the registered uuid
    3acfe9c4-cdbf-4e4d-b8b2-71535396f8b1 is absent from all 10 uuids the listing now serves).

    ⛔ THREE DEFECTS THIS REPLACES, each measured 2026-09-07 rather than reasoned about:

    1. HEADER SHAPE. Bare BROWSER_UA gets 403; BROWSER_HEADERS gets 200. See that constant.

    2. A PINNED UUID IS A DEAD INSTRUMENT ON A TIMER. Baker Hughes re-issues the weekly file
       under a NEW uuid, so any registry row naming one grades fine until the week it silently
       cannot. We resolve the uuid AT RUN TIME from the listing page's own anchor text. The
       registry therefore stores a QUESTION ("the link called 'New Report'"), never an ANSWER.
       [[finding_dated_carry_item_has_no_expiry_check]]

    3. THE DECOY. The listing carries year-stale archives alongside the live weekly. Picking by
       link text alone would have grabbed one silently, so the print date parsed out of
       Content-Disposition is asserted FRESH below — a wrong file fails LOUD, never quietly.

    ⚠️ ONE DOWNLOAD PER RUN, BY CONSTRUCTION. The file is ~7 MB. Selection happens on the free
    HTML; exactly one static-file GET follows. Do not "check them all" — ~10 rapid downloads is
    what trips this WAF, which is the grain of truth in the 9/6 note.

    ⚠️ GET, NEVER HEAD. HEAD is 403 on this host under every header shape tried.

    ⚖️ L25 GOVERNS AND IS HONOURED ("a source that HANGS is not a source that is DOWN — a WAF
    tarpitting your User-Agent"). This host shows BOTH signatures and they mean different things,
    which is why the error strings below distinguish them:
        bare BROWSER_UA .................. HTTP 403, immediate  -> WRONG HEADER SHAPE
        "BRENT-instrument-check/1.0" ..... TimeoutError, hangs  -> TARPIT (the L25 case)
    A self-identifying UA does not get refused here, it gets STRUNG ALONG — so a naive read of the
    timeout as "Baker Hughes is down" is the exact L25 error, and it is available to make on this
    host today. Both signatures observed 2026-09-07. (L25 was already cited elsewhere in this
    FILE, by probe_jwc — which is why the file-level --spec sweep reported it satisfied while THIS
    function was silent on it. Cited here, where it actually governs.)
    [[finding_instrument_reports_clean_against_the_wrong_reference]]

    ⚑ RECONCILED WITH A STANDING INSTRUCTION THAT THIS APPEARS TO CONTRADICT, so nobody has to
    guess whether it was overlooked. The 2026-09-06 grade note (CATALYSTS.tsv 9/4 row, and the
    BRT-26 row in PREDICTIONS.tsv) says: "pick by the DATE in content-disposition, NEVER by link
    text (the index also lists a YEAR-STALE archive whose link ALSO says 'New Report')." That
    warning is CORRECT and it is HONOURED here, because the two jobs are split:
        SELECTION  is by link text — it is the only signal available for FREE, off HTML we
                   already hold. Picking by date would mean downloading every candidate to read
                   its header, which is the ~10-download pattern that trips the WAF.
        VALIDATION is by the Content-Disposition date, which is AUTHORITATIVE and always runs.
    So link text never DECIDES anything on its own: a mislabelled or relabelled link fails the
    freshness assert. Both halves are exercised, not assumed —
        T2 wrong label      -> "matched 0 anchors, need exactly 1" (fails loud)
        T5 the real decoy   -> "newest file is 2025-08-29 (374d old) ... Do NOT grade off this"
    The decoy the note warns about is literally the file T5 catches. Falsified 2026-09-07.
    [[finding_test_the_guard_not_just_the_guarded]]
    """
    parts = spec.split("|")
    if len(parts) != 2:
        return False, None, f"bad bhrigs grammar (want listing-url|link-text): {spec!r}"
    listing, want = parts[0].strip(), parts[1].strip()

    def _get(url, extra=None, timeout=60):
        h = dict(BROWSER_HEADERS)
        h.update(extra or {})
        return urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=timeout)

    try:
        with _get(listing, timeout=40) as resp:
            if resp.status != 200:
                return False, None, f"listing HTTP {resp.status}"
            html = resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        return False, None, (f"listing unreachable: {type(e).__name__}: {e} — ⚠️ a 403 here is "
                             f"the HEADER SHAPE, not a usage ban: check BROWSER_HEADERS first, "
                             f"a bare User-Agent 403s on this host by design")

    links = {}
    for m in re.finditer(r'<a[^>]*href="([^"]*static-files/([0-9a-f-]{36})[^"]*)"[^>]*>(.*?)</a>',
                         html, re.S | re.I):
        txt = " ".join(re.sub(r"<[^>]+>", "", m.group(3)).split())
        links[txt] = m.group(2)
    if not links:
        return False, None, ("listing HTTP 200 but NO /static-files/ anchors — reachable-but-"
                             "not-readable (navigation shell). Treat as FAILURE, not 'no change'.")
    hit = [(t, u) for t, u in links.items() if want.lower() in t.lower()]
    if len(hit) != 1:
        return False, None, (f"link text {want!r} matched {len(hit)} anchors, need exactly 1 — "
                             f"the page relabelled its links. Available: {sorted(links)}")
    label, uuid = hit[0]

    try:
        with _get(f"https://rigcount.bakerhughes.com/static-files/{uuid}",
                  extra={"Accept": "*/*", "Referer": listing, "Sec-Fetch-Dest": "empty",
                         "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin"}) as resp:
            if resp.status != 200:
                return False, None, f"static-file HTTP {resp.status}"
            disp = resp.headers.get("Content-Disposition") or ""
            blob = resp.read()
    except Exception as e:
        return False, None, f"static-file unreachable: {type(e).__name__}: {e}"

    dm = re.search(r"(\d{2})-(\d{2})-(\d{4})", disp)
    if not dm:
        return False, None, (f"no print date in Content-Disposition ({disp!r}) — the freshness "
                             f"assertion is the decoy guard; without it this probe is blind")
    mm, dd, yy = dm.groups()
    print_dt = datetime(int(yy), int(mm), int(dd))
    age = (datetime.now() - print_dt).days
    if age > 14:
        return False, None, (f"🔴 newest file is {print_dt.date()} ({age}d old) — Baker Hughes "
                             f"prints WEEKLY, so >14d means we grabbed an ARCHIVE (the decoy) or "
                             f"publication stopped. Do NOT grade off this file.")

    try:
        import openpyxl
        wb = openpyxl.load_workbook(io.BytesIO(blob), read_only=True, data_only=True)
        if "NAM Summary" not in wb.sheetnames:
            return False, None, (f"no 'NAM Summary' sheet (have: {wb.sheetnames}) — the grade "
                                 f"locator in REGISTRY.tsv names that sheet; workbook reshaped")
        ws = wb["NAM Summary"]
        oil = None
        for row in ws.iter_rows(min_row=1, max_row=60, values_only=True):
            cells = [c for c in row if c is not None]
            if len(cells) >= 2 and str(cells[0]).strip().lower() == "oil":
                oil = int(cells[1])
                break            # FIRST 'Oil' row is the U.S. Breakout; Canada's is below it
    except Exception as e:
        return False, None, f"workbook unreadable: {type(e).__name__}: {e}"

    if oil is None:
        return False, None, ("'NAM Summary' has no 'Oil' row in its first 60 — the U.S. Breakout "
                             "block moved. Fail loud: a missing row must never read as 0.")
    return True, print_dt, (f"US OIL rig count {oil} (print {print_dt.date()}, {label!r}, "
                            f"uuid {uuid[:8]}…) — BRT-26 line is 457, "
                            f"{'BELOW ✅ claim holds' if oil < 457 else '🔴 AT/ABOVE THE LINE'}, "
                            f"headroom {457 - oil}")


def probe_jwc(spec):
    """JWC Listed-Areas CHANGE DETECTOR — the circular NUMBER, not the page's reachability.

    Grammar: jwc:<index-url>|<baseline-circular>       e.g. jwc:https://...|JWLA-034

    ⚑ ADDED 2026-08-21. supersedes: none — EXTENDS the probe grammar (retirement ratchet),
    exactly as `arcgis:` and `gie:` did before it.

    ⛔⛔ WHY A PLAIN `http:` PROBE IS NOT ENOUGH, WHICH IS THE WHOLE REASON THIS EXISTS:
    `probe_http` answers "did the host reply?". The IUA page will answer 200 FOREVER while
    the circular number moves underneath it. REACHABILITY IS NOT CHANGE-DETECTION, and
    `KILL-LEG2-JWC-LISTING` is an ASYMMETRIC STANDING NEGATIVE — a row whose failure mode is
    precisely that NOTHING MAKES ANYONE RE-READ IT. A green reachability probe on a standing
    negative actively misleads: it looks like a watched instrument and is not one.

    ⚑ THE COST OF NOT HAVING THIS, MEASURED ON THIS DESK 2026-08-21: `JWLA-033` was superseded
    on 2026-07-29 by `JWLA-034` — which amended SAUDI ARABIA into the Listed Areas — and
    THESIS's Path-A criterion went on citing `JWLA-033` for three weeks. Nothing was broken,
    nothing 404'd, so nothing re-asked. Found only by chasing anchors before a file cut.

    ⚑ PRIOR-ART LINE (CHECK_STANDARD §13, RULED Will 2026-08-21). SYMPTOM SEARCHED: "a carried
    baseline that nothing re-evaluates, behind a source that keeps answering 200 while its
    CONTENT moves underneath it." Searched MEMORY.md, memory/auto/ BODIES and PATTERNS_HOT.md.
    ⇒ NOT NOVEL, and the prior art SHARPENS the design rather than duplicating it:
      * [[finding_dated_carry_item_has_no_expiry_check]] — PRIMARY. "A carried ASSERTION never
        self-reports as wrong — it is a string, and reading it does not evaluate it. State gets
        re-derived because CHECKING IS USING; carried claims do not." The JWLA-034 baseline is
        exactly such a carried claim, and a standing negative is the purest case: nothing USES
        it, so nothing re-derives it. That is the argument for this probe, already written down.
      * [[finding_partitioned_source_returns_stale_window_at_200]] — ADJACENT, and the mirror
        image: there the SOURCE is stale behind a 200; here the source MOVES while my BASELINE
        stands still. Same 200, opposite direction.
      * [[finding_retired_threshold_has_no_publisher]] — ADJACENT: tooling instruments REVISED
        values and is structurally blind to WITHDRAWN ones. A JWC DELISTING is a withdrawal.

    ⛔ THIS IS A PROMPT, NEVER A FIRE. Will ruled 2026-08-21 that a delisting is PROMPT-ONLY
    (a removal can be LOBBIED rather than earned — Pakistan was an explicit state campaign
    taking ~4.5 months). So a new circular means GO READ IT. It does NOT grade the falsifier,
    does not kill the thesis leg, and authorises nothing.
    """
    parts = spec.split("|")
    if len(parts) != 2:
        return False, None, f"bad jwc grammar (want url|baseline-circular): {spec!r}"
    url, baseline = parts[0].strip(), parts[1].strip().upper()
    m0 = re.match(r"JWLA-(\d+)", baseline)
    if not m0:
        return False, None, f"bad baseline circular {baseline!r} (want JWLA-NNN)"
    base_n = int(m0.group(1))
    try:
        req = urllib.request.Request(url, headers={"User-Agent": BROWSER_UA})
        with urllib.request.urlopen(req, timeout=30) as resp:
            if resp.status != 200:
                return False, None, f"HTTP {resp.status}"
            body = resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        return False, None, (f"unreachable: {type(e).__name__}: {e} — ⚠️ if this is a HANG "
                             f"rather than an HTTP error, check the User-Agent first (L25)")
    found = {}
    for mm in re.finditer(r"JWLA-(\d+)([^<]{0,120})", body):
        n = int(mm.group(1))
        dm = re.search(r"(\d{1,2}/\d{1,2}/\d{4})", mm.group(2))
        found[n] = found.get(n) or (dm.group(1) if dm else None)
    if not found:
        # a 200 with no circular numbers in it is the LMA navigation-shell shape: fail loud.
        return False, None, ("HTTP 200 but NO JWLA circular number in the page — this is the "
                             "reachable-but-not-readable shape (the LMA committee page does "
                             "exactly this). Treat as a FAILURE, not as 'no change'.")
    newest = max(found)
    if newest > base_n:
        newer = sorted(k for k in found if k > base_n)
        lst = ", ".join(f"JWLA-{k:03d}{' (' + found[k] + ')' if found[k] else ''}" for k in newer)
        return False, None, (f"🔴 NEW JWC CIRCULAR SINCE THE FROZEN BASELINE {baseline}: {lst}. "
                             f"⇒ PROMPT TO INVESTIGATE — read the circular and check whether the "
                             f"Persian/Arabian Gulf + Gulf of Oman are still LISTED. "
                             f"⛔ THIS IS NOT A FIRE: a delisting is PROMPT-ONLY (Will, 2026-08-21) "
                             f"and a removal can be lobbied rather than earned.")
    if newest < base_n:
        return False, None, (f"baseline {baseline} is NEWER than anything on the index "
                             f"(newest JWLA-{newest:03d}) — baseline or index is wrong, do not ignore")
    return True, None, (f"baseline {baseline} is still the newest circular on the IUA index "
                        f"({len(found)} circulars listed) — Listed Areas UNCHANGED since it")


def probe_chain(spec):
    try:
        import yfinance as yf
        tick, expiry = spec.split("@")
        t = yf.Ticker(tick)
        if expiry not in (t.options or ()):
            return False, None, f"expiry {expiry} not listed"
        ch = t.option_chain(expiry).calls
        if ch.empty:
            return False, None, "chain empty"
        two_sided = int(((ch["bid"] > 0) & (ch["ask"] > 0)).sum())
        return True, None, f"{len(ch)} calls, {two_sided} two-sided"
    except Exception as e:
        return False, None, f"probe error: {type(e).__name__}: {e}"


# ---------------------------------------------------------------------------

_PROBE_CACHE = {}


def _cached(key, fn):
    if key not in _PROBE_CACHE:
        _PROBE_CACHE[key] = fn()
    return _PROBE_CACHE[key]


def evaluate(row, quick=False):
    probe = (row.get("probe") or "").strip()
    findings = []
    probed = False

    def add(level, code, msg):
        findings.append({"level": level, "code": code, "msg": msg})

    # 1. EXISTS
    if probe == "none" or not probe:
        add(RED, "NO_INSTRUMENT", "no instrument declared — this test CANNOT be evaluated, ever")
        return findings, probed, ""

    detail = ""
    last_dt = None

    # 2. REACHABLE
    if probe.startswith("manual:"):
        add(GREEN, "MANUAL", f"human-graded ({probe.split(':',1)[1]}) — not probed")
    elif quick:
        add(AMBER, "SKIPPED", "network probe skipped (--quick)")
    else:
        if probe.startswith("yf:"):
            need_intra = needs_same_session(row)
            ok, last_dt, detail = _cached((probe, need_intra), lambda: probe_yf(probe[3:], want_intraday=need_intra))
        elif probe.startswith("fred:"):
            ok, last_dt, detail = _cached(probe, lambda: probe_fred(probe[5:]))
        elif probe.startswith("http:"):
            ok, last_dt, detail = _cached(probe, lambda: probe_http(probe[5:]))
        elif probe.startswith("arcgis:"):
            ok, last_dt, detail = _cached(probe, lambda: probe_arcgis(probe[7:]))
        elif probe.startswith("eia:"):
            ok, last_dt, detail = _cached(probe, lambda: probe_eia(probe[4:]))
        elif probe.startswith("gie:"):
            ok, last_dt, detail = _cached(probe, lambda: probe_gie(probe[4:]))
        elif probe.startswith("bhrigs:"):
            ok, last_dt, detail = _cached(probe, lambda: probe_bhrigs(probe[7:]))
        elif probe.startswith("jwc:"):
            ok, last_dt, detail = _cached(probe, lambda: probe_jwc(probe[4:]))
        elif probe.startswith("chain:"):
            ok, last_dt, detail = _cached(probe, lambda: probe_chain(probe[6:]))
        else:
            ok, detail = False, f"unknown probe grammar: {probe!r}"
        probed = True
        if ok is None:
            add(AMBER, "NO_PROBER", detail)
        elif not ok:
            # ⚑ 2026-08-21: a CHANGE-DETECTOR failing is NOT a dead instrument — the source
            # answered perfectly and the BASELINE moved. Labelling that "DEAD: instrument did
            # not return usable data" is factually wrong and is the same mislabel class this
            # desk spent the day correcting: the wrapper contradicting its own payload.
            # Detected off the probe's own PROMPT sentinel so every other probe is untouched.
            if "PROMPT TO INVESTIGATE" in (detail or ""):
                add(RED, "BASELINE-MOVED",
                    f"the instrument answered FINE — the FROZEN BASELINE is stale. {detail}")
            else:
                add(RED, "DEAD", f"instrument did not return usable data — {detail}")
        else:
            add(GREEN, "REACHABLE", detail)

    # 3. FRESH — content vintage, never mtime (git sync restamps mtime)
    try:
        budget = int(row.get("max_stale_days") or -1)
    except ValueError:
        budget = -1
    if budget >= 0:
        newest = None
        if last_dt is not None:
            newest = last_dt.date()
        else:
            lv = (row.get("last_verified") or "").strip()
            if lv and lv != "NEVER":
                try:
                    newest = datetime.fromisoformat(lv).date()
                except ValueError:
                    newest = None
        if newest is None:
            add(RED, "NO_VINTAGE", "no datapoint date and no usable last_verified — freshness UNKNOWN, not OK")
        else:
            age = (datetime.now().date() - newest).days
            if age > budget:
                # Escalation is KIND-AWARE, not a blanket 2x multiplier. A gate or a
                # falsifier that is out of budget is BLOCKING by definition — it is the
                # thing standing between a thesis and capital, so "a bit stale" is not a
                # warning-level state. v1 used a flat 2x and reported the DEAD PortWatch
                # falsifier — the one currently blocking my thesis — as merely 🟠.
                hard = row.get("kind") in ("gate", "falsifier")
                add(RED if (hard or age > budget * 2) else AMBER, "STALE",
                    f"newest datapoint {newest} is {age}d old vs a {budget}d budget"
                    + ("  [gate/falsifier ⇒ blocking, not advisory]" if hard else ""))

    # 4. FEASIBLE — the window check
    if needs_same_session(row) and not quick and probe.startswith("yf:"):
        co = (row.get("co_instrument") or "").strip()
        if co:
            basis = window_basis(row)
            act_t = ACTION_CLOSE_ET.get(co, ACTION_CLOSE_ET["_default"])
            if basis == "any":
                # EXISTENCE form: evaluable from the first print, so the window opens there.
                inst_t = first_intraday_time_et(probe[3:])
                anchor = f"first {probe[3:]} print {inst_t} ET"
            elif basis == "final":
                inst_t = last_intraday_time_et(probe[3:])
                anchor = f"last {probe[3:]} print {inst_t} ET"
            elif re.fullmatch(r"at\d{4}", basis):
                # FIXED-TIME grade: the spec names a clock time to grade at, ONCE.
                # (Stage-A Leg T v6, Will-ruled 2026-08-05.) The window opens at that
                # time — but never EARLIER than the instrument's first print, because a
                # grade time before the open is not gradeable at all.
                g = f"{basis[2:4]}:{basis[4:6]}"
                fp = first_intraday_time_et(probe[3:])
                if fp and (int(fp[:2]) * 60 + int(fp[3:])) > (int(g[:2]) * 60 + int(g[3:])):
                    add(RED, "WINDOW_GRADE_BEFORE_OPEN",
                        f"[basis={basis}] spec grades at {g} ET but {probe[3:]}'s first print is {fp} ET "
                        f"— the instrument does not exist yet at the graded moment")
                    inst_t = None
                    anchor = ""
                else:
                    inst_t = g
                    anchor = f"specified grade time {g} ET ({probe[3:]} open {fp} ET)"
            else:
                add(RED, "WINDOW_BASIS_UNKNOWN",
                    f"window_req declares basis '{basis}', which this script does not implement "
                    f"— expected ':final', ':any' or ':atHHMM'. NOT graded rather than graded on a guess")
                inst_t = None
                anchor = ""
            if inst_t:
                mins = (int(act_t[:2]) * 60 + int(act_t[3:])) - (int(inst_t[:2]) * 60 + int(inst_t[3:]))
                tag = f"[basis={basis}]"
                if mins <= 0:
                    add(RED, "WINDOW_INFEASIBLE",
                        f"{tag} instrument's {anchor} is at/after the {co} action close {act_t} ET "
                        f"⇒ {mins}min window: the test becomes knowable only once it can no longer be acted on")
                elif mins < 30:
                    add(AMBER, "WINDOW_TIGHT",
                        f"{tag} only {mins}min between the {anchor} and the {co} close ({act_t})")
                else:
                    add(GREEN, "WINDOW_OK",
                        f"{tag} {mins}min of actionable window from the {anchor} to the {co} close ({act_t})")

    return findings, probed, detail


INCIDENTS = BRENT_DIR / "refinery_damage" / "INCIDENTS.tsv"
INCIDENT_ACTIVE_BUDGET_D = 60   # ACTIVE >=60d unverified => re-verify-or-downgrade


PRESENT_TENSE_UNBUDGETED = ("PARTIAL_RESTART", "MONITORING", "DISPUTED")


def check_incident_unbudgeted(today=None):
    """I-9 — stale rows in PRESENT-TENSE statuses that the 60-day budget does NOT cover.

    Adopted 2026-08-21 (BRENT). supersedes: none. ⛔ DELIBERATELY NOT AN EXPANSION OF THE
    I-2 BUDGET: that scope ('status == ACTIVE', 60 days) was ruled by Will on 2026-08-12 as
    spec'd, and widening a ruled alert unasked would change its meaning and its volume.
    This is a DISCLOSURE line, not a budget — it changes no threshold and gates nothing.

    ⚑ WHY, and it was found the hard way, by me, in the same session: correcting RF-005
    Bazan from ACTIVE to PARTIAL_RESTART — a genuine accuracy improvement — SILENTLY REMOVED
    a five-month-stale row from the staleness check, because the check filters on ACTIVE.
    ⇒ MAKING A ROW MORE ACCURATE MADE IT LESS SUPERVISED. Without this line, the cleanest way
    to clear the re-verify queue would be to re-classify rows out of it.
    `[[finding_registered_gate_captures_attention]]`

    PARTIAL_RESTART / MONITORING / DISPUTED are all PRESENT-TENSE claims about the world and
    age exactly like ACTIVE does. RESOLVED, ATTACKED_INFRA_INTACT and PERMANENT_CLOSURE are
    terminal and are correctly excluded.
    """
    if not INCIDENTS.exists():
        return []
    if today is None:
        today = datetime.now(timezone.utc).replace(tzinfo=None)
    out = []
    with open(INCIDENTS, newline="", encoding="utf-8") as fh:
        hdr = None
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            f = line.rstrip("\n").split("\t")
            if hdr is None:
                hdr = f
                continue
            r = dict(zip(hdr, f))
            if (r.get("status") or "").strip() not in PRESENT_TENSE_UNBUDGETED:
                continue
            lv = (r.get("last_verified") or "").strip()
            try:
                age = (today - datetime.fromisoformat(lv[:10])).days
            except Exception:
                continue
            if age >= INCIDENT_ACTIVE_BUDGET_D:
                out.append((r.get("id", "?"), r.get("facility", "?"), age,
                            lv, (r.get("status") or "?").strip()))
    out.sort(key=lambda x: -x[2])
    return out


def check_incident_impossible(today=None):
    """I-8 — INTERNAL-CONSISTENCY invariant: bpd_offline_est must not exceed capacity_bpd.

    Adopted 2026-08-21 (BRENT). supersedes: none — EXTENDS this script's INCIDENTS coverage
    with a check that needs NO network, NO source, and NO judgement.

    ⚑ WHY IT EXISTS. Found by accident: RF-008 Port Arthur asserted 415,000 bpd offline
    against its OWN capacity_bpd of 380,000 — more offline than the facility has — carried
    as offline_state=MEASURED, while the row's own note said 47,000. It had sat that way
    since 2026-04-16.

    ⛔ AND THE REASON NOTHING CAUGHT IT IS THE POINT: RF-008's status is PARTIAL_RESTART,
    and the 60-day re-verify budget filters on status == 'ACTIVE'. 25 of the ledger's 53
    rows sit in statuses NO check reads (MONITORING 15, RESOLVED 12, ATTACKED_INFRA_INTACT 3,
    PARTIAL_RESTART 1, DISPUTED 1). The staleness check answers 'has anyone looked lately?'
    for one status; this answers 'is the row even self-consistent?' for ALL of them.
    `[[finding_registered_gate_captures_attention]]` — the gated instrument gets the
    attention and the un-gated ones are swept by nothing.

    ⚠️ SCOPED DELIBERATELY NARROW: only rows where BOTH units are BPD are compared, so the
    BCFD / MTPA / MW rows (offline_state=NA-WRONG-UNIT) are skipped rather than mis-flagged.
    This checks ARITHMETIC POSSIBILITY, never whether either figure is TRUE.
    """
    if not INCIDENTS.exists():
        return []
    bad = []
    with open(INCIDENTS, newline="", encoding="utf-8") as fh:
        hdr = None
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            f = line.rstrip("\n").split("\t")
            if hdr is None:
                hdr = f
                continue
            r = dict(zip(hdr, f))
            if (r.get("capacity_unit") or "").strip() != "BPD":
                continue
            if (r.get("offline_unit") or "").strip() != "BPD":
                continue
            cap = (r.get("capacity_bpd") or "").strip()
            off = (r.get("bpd_offline_est") or "").strip()
            if cap.isdigit() and off.isdigit() and int(off) > int(cap):
                bad.append((r.get("id", "?"), r.get("facility", "?"),
                            int(cap), int(off), (r.get("status") or "?").strip()))
    return bad


def check_incident_staleness(today=None):
    """I-2 — ACTIVE incident rows are a PRESENT-TENSE CAPACITY CLAIM with no expiry check.

    Adopted 2026-08-13, Will-ruled 2026-08-12 as BRENT spec'd it: `status=ACTIVE` and
    `last_verified` older than 60 days => RE-VERIFY-OR-DOWNGRADE, surfaced at boot.

    ⚑ WHY THIS LIVES HERE AND IS NOT A TENTH SCRIPT (retirement ratchet — the rider Will
    honored): `instrument_check.py` already answers exactly this question for registry
    rows — "is the thing this file asserts still fresh enough to assert?" An incident row
    saying ACTIVE is the same claim shape as a threshold row saying live. supersedes: none
    — EXTENDS this script to a second ledger.

    THE MEASUREMENT THAT FORCED IT (audit 2026-08-12b, I-2): 23 ACTIVE rows, MEDIAN
    last_verified age 124 days, max 146; 18 unverified >=90d, and those 18 carry
    4,774,000 of 6,474,000 bpd = 74% of the asserted ACTIVE total. The highest-confidence
    rows (source_tier A-1) were the stalest. If any of those facilities restarted, the file
    says offline and NOTHING would flag it. `[[finding_dated_carry_item_has_no_expiry_check]]`
    — a carried assertion is a string; reading it never grades it.

    ⛔ THIS FLAGS, IT NEVER EDITS. Re-verification is research, not a mechanical fix, and
    downgrading a row on a timer would fabricate a restart nobody observed.
    ⚠️ AND IT IS NOT A CAPACITY MEASURE: the bpd totals printed here are the LEDGER'S OWN
    asserted numbers, reported to rank the re-verify queue. Per the standing verdict
    (Will-ruled fleet-wide 2026-08-12) NO AGGREGATE OVER INCIDENTS.tsv IS QUOTABLE — it is
    an EVENT RECORD, not a capacity measure. Do not lift these figures onto any surface.
    """
    if not INCIDENTS.exists():
        return []
    today = today or datetime.today()
    stale = []
    permanent = []
    with open(INCIDENTS, newline="", encoding="utf-8") as fh:
        hdr = None
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            f = line.rstrip("\n").split("\t")
            if hdr is None:
                hdr = f
                continue
            r = dict(zip(hdr, f))
            st = (r.get("status") or "").strip()
            if st == "PERMANENT_CLOSURE":
                # ⚑ ADDED 2026-08-21. TERMINAL STATE — deliberately OUT of the re-verify budget,
                # and counted separately below so it can never vanish silently.
                # WHY: a permanently shut refinery fits NEITHER existing status. ACTIVE means
                # "still offline, re-verify me", which is trivially true forever and puts the row
                # on an endless treadmill; RESOLVED means "restored", which is false. Left as
                # ACTIVE, RF-028/RF-029 tripped the 60-day flag EVERY boot with no reachable
                # end state — diluting a queue whose whole purpose is to show real work owed.
                # ⛔ THIS IS NOT DOWNGRADING ON A TIMER (which the ledger header forbids and
                # which would fabricate a restart): it is a re-classification made on a
                # RE-VERIFIED primary, and each such row carries a NAMED RE-ENTRY CONDITION
                # in its notes instead of a clock. `[[finding_guard_correctness_and_wiring_are_independent]]`
                # — the status was added and this filter updated IN THE SAME EDIT, because a new
                # status with an unchanged reader drops the rows out of every check silently.
                permanent.append((r.get("id", "?"), r.get("facility", "?"),
                                  (r.get("last_verified") or "").strip()))
                continue
            if st != "ACTIVE":
                continue
            lv = (r.get("last_verified") or "").strip()
            try:
                age = (today - datetime.fromisoformat(lv[:10])).days
            except Exception:
                stale.append((r.get("id", "?"), r.get("facility", "?"), None, lv or "(blank)"))
                continue
            if age >= INCIDENT_ACTIVE_BUDGET_D:
                stale.append((r.get("id", "?"), r.get("facility", "?"), age, lv))
    stale.sort(key=lambda x: (x[2] is not None, -(x[2] or 0)))
    check_incident_staleness.permanent = permanent   # side-channel for the caller's summary line
    return stale


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true", help="skip network probes")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--id", help="check a single test_id")
    args = ap.parse_args()

    if not REGISTRY.exists():
        print(f"  ERROR: registry not found at {REGISTRY}")
        return 1

    rows = load_registry()
    if args.id:
        rows = [r for r in rows if r["test_id"] == args.id]
        if not rows:
            print(f"  ERROR: no such test_id {args.id!r}")
            return 1

    results, n_probed = [], 0
    for r in rows:
        f, probed, _ = evaluate(r, quick=args.quick)
        n_probed += 1 if probed else 0
        results.append({"test_id": r["test_id"], "kind": r.get("kind", ""),
                        "spec_home": r.get("spec_home", ""), "findings": f})

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        blocking = [x for x in results if any(g["level"] == RED for g in x["findings"])]
        warn = [x for x in results if x not in blocking and any(g["level"] == AMBER for g in x["findings"])]

        print(f"\n  INSTRUMENT CHECK — {len(results)} registered tests"
              f"{' (--quick: probes skipped)' if args.quick else ''}")
        print(f"  {'-'*74}")

        if blocking:
            print(f"\n  {RED} BLOCKING — these tests cannot be graded as written ({len(blocking)}):")
            for x in blocking:
                for g in x["findings"]:
                    if g["level"] == RED:
                        # test_id goes on the SAME line as the finding: boot.py's output filter
                        # keeps marker lines and drops the header line above them, so a
                        # separate title line yields "7 problems" with no way to tell WHICH.
                        print(f"     {RED} {x['test_id']} [{x['kind']}] {g['code']}: {g['msg']}")
                        print(f"         → spec: {x['spec_home']}")
        if warn:
            print(f"\n  {AMBER} WARNINGS ({len(warn)}):")
            for x in warn:
                for g in x["findings"]:
                    if g["level"] == AMBER:
                        print(f"     {AMBER} {x['test_id']}: {g['code']} — {g['msg']}")
        if not blocking and not warn:
            print(f"\n  {GREEN} all registered tests have a reachable, fresh, feasible instrument.")

        # I-2 — INCIDENTS.tsv ACTIVE staleness budget (adopted 2026-08-13, Will-ruled 8/12).
        inc = check_incident_staleness()
        if inc:
            print(f"\n  {AMBER} INCIDENTS.tsv — {len(inc)} ACTIVE rows past the "
                  f"{INCIDENT_ACTIVE_BUDGET_D}d re-verify budget "
                  f"(ACTIVE is a PRESENT-TENSE claim; re-verify or downgrade):")
            for rid, fac, age, lv in inc[:8]:
                aged = f"{age}d" if age is not None else f"unparseable last_verified {lv!r}"
                print(f"     {AMBER} {rid} {fac[:38]:38s} last verified {lv} ({aged})")
            if len(inc) > 8:
                print(f"     … and {len(inc)-8} more (run with --json or read the ledger)")
            print(f"     ⚠️  Flags only — never auto-edits. Downgrading on a timer would "
                  f"fabricate a restart nobody observed.")
            print(f"     ⛔ NO AGGREGATE OVER INCIDENTS.tsv IS QUOTABLE — event record, "
                  f"not a capacity measure (Will-ruled fleet-wide 2026-08-12).")

        # ⚑ ADDED 2026-08-21 alongside the PERMANENT_CLOSURE terminal state. This line is the
        # WHOLE REASON the new status is safe: the filter above skips these rows, so WITHOUT
        # this print they would leave the re-verify queue AND every other surface at once —
        # a silent coverage hole wearing the appearance of a cleaner board.
        # ⚠️ Prints UNCONDITIONALLY when any such row exists, including when `inc` is empty,
        # so an otherwise-clean run still discloses what has been moved out of scope.
        # I-9 — stale PRESENT-TENSE rows OUTSIDE the ruled ACTIVE budget. Disclosure only.
        unb = check_incident_unbudgeted()
        if unb:
            print(f"\n  {AMBER} INCIDENTS.tsv — {len(unb)} row(s) in PRESENT-TENSE statuses the "
                  f"{INCIDENT_ACTIVE_BUDGET_D}d budget does NOT cover, also stale "
                  f"(DISCLOSURE, not a budget — no threshold, gates nothing):")
            for rid, fac, age, lv, st in unb[:6]:
                print(f"     {AMBER} {rid} {fac[:32]:32s} {st:15s} last verified {lv} ({age}d)")
            if len(unb) > 6:
                print(f"     … and {len(unb)-6} more")
            print(f"     ⚠️  Here because re-classifying a row OUT of ACTIVE silently removes it "
                  f"from the re-verify queue — accuracy must not buy invisibility.")

        # I-8 — arithmetic-possibility invariant, ALL statuses (see check_incident_impossible).
        imp = check_incident_impossible()
        if imp:
            print(f"\n  {RED} INCIDENTS.tsv — {len(imp)} row(s) assert MORE OFFLINE THAN THE FACILITY HAS "
                  f"(bpd_offline_est > capacity_bpd — arithmetically impossible, fix the row):")
            for rid, fac, cap, off, st in imp:
                print(f"     {RED} {rid} {fac[:34]:34s} capacity {cap:>9,} < offline {off:>9,} "
                      f"({off-cap:+,}) status={st}")
            print(f"     ⚠️  Checks POSSIBILITY, never truth — and it reads EVERY status, not just ACTIVE.")

        perm = getattr(check_incident_staleness, "permanent", [])
        if perm:
            print(f"\n  {GREEN} INCIDENTS.tsv — {len(perm)} row(s) in PERMANENT_CLOSURE "
                  f"(TERMINAL: deliberately OUTSIDE the {INCIDENT_ACTIVE_BUDGET_D}d re-verify budget, "
                  f"listed so the exclusion is never silent):")
            for rid, fac, lv in perm:
                print(f"     {GREEN} {rid} {fac[:38]:38s} re-verified {lv}")
            print(f"     ⚠️  These are NOT restarts and NOT resolutions — the capacity is gone, "
                  f"permanently. They re-enter ACTIVE only on a REPORTED restart or sale-and-restart, "
                  f"never on a clock. Each row names that condition in its notes.")

        # Anti-false-clean disclosure. A pass means nothing without this.
        print(f"\n  {'-'*74}")
        print(f"  Probed {n_probed} of {len(results)} rows over the network"
              f"{' (0 — --quick)' if args.quick else ''}; the rest are manual/none/unprobeable.")
        print(f"  ⚠️  This checks the INSTRUMENT, never whether the THRESHOLD LEVEL is still meaningful.")
        print(f"      A permanently-breached line (gasoline crack >$30) probes perfectly GREEN.")

    # ⛔ I-8 MUST REACH THE EXIT CODE, NOT JUST THE SCREEN (added 2026-08-21, same edit as I-8).
    # boot.py renders this script's SUMMARY line from its rc, and prints the body separately.
    # Without this clause an arithmetically-impossible row printed a RED line in the body while
    # the boot summary said "✅ Instrument Check OK" — a reader scanning the summary saw a clean
    # board. That is the identical silent-fallback-green shape killed in thresholds.py on
    # 2026-08-17, reproduced by me in a NEW check on the same desk four days later.
    # [[finding_guard_correctness_and_wiring_are_independent]] — writing the check and making it
    # REACH anyone are two changes, and only the first is interesting to write.
    # ⚠️ NOTE the incident STALENESS block deliberately does NOT set rc (it is amber/advisory by
    # its 2026-08-13 spec). I-8 does, because an impossible value is a DEFECT, not a backlog item.
    if check_incident_impossible():
        return 2
    return 2 if any(g["level"] == RED for x in results for g in x["findings"]) else 0


if __name__ == "__main__":
    sys.exit(main())
