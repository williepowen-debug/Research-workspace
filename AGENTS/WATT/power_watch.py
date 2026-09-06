#!/usr/bin/env python3
"""
power_watch.py — boot-time power/grid-stress instrument (PJM leg).

Built by DAEDALUS 2026-07-10 (Will-approved Step-1 instrument layer — power-agent
staged path; see AGENTS/DAEDALUS/outbox/
2026-07-10_to-PROME_tier3-gaps-and-power-agent-memo.md §5).
Moved into AGENTS/WATT/ 2026-07-10 on the WATT spinout (Step-2, Will-approved):
WATT owns the power/grid thesis + this instrument. HENRY consumes WATT's OUTPUT
(STATUS + NEXUS_BRIEF), no longer runs the instrument itself.
Owner/consumer: WATT (channel P1 stress→price). Imports the shared FORGE EIA
client (fetch.py) by absolute self-location — the client stays in FORGE.

Five reads, one verdict line, each fail-LOUD (stderr + rc=2, never fabricated):
  1. PJM emergency-procedures postings — https://emergencyprocedures.pjm.com/
     (public, no key; JSF app but postings are SERVER-RENDERED in the initial
     HTML, so a plain GET with a browser User-Agent works — verified 2026-07-10).
     FLAG-NOT-FIRE: an emergency-class posting prints "REVIEW", this script
     never auto-declares a C3/grid-stress event — that call is AEOLUS/HENRY
     judgment. Routine localized transmission warnings (e.g. Post Contingency
     Local Load Relief) are counted but do NOT trip REVIEW/rc=1 — only
     emergency-class types (EEA / Capacity Emergency / Load Shed / etc.) do.
  2. PJM hourly demand via EIA-930 (fetch.eia_pjm_demand): latest hour vs
     prior-24h peak. Stamps are UTC hours; EIA-930 publication lags real time
     ~2-6h — the "latest" hour is the latest PUBLISHED, not the current hour.
  3. Retail price backdrop via EIA retail-sales (fetch.eia_retail_power_price):
     latest monthly US industrial + residential prints. ~2-MONTH LAG — always
     cited with their month labels.
  4. LMP-PROXY + SPARK SPREAD (added 2026-07-12, WATT session 2): EIA's free
     ICE-sourced wholesale price file (eia.gov/electricity/wholesale,
     ice_electric-YYYY.xlsx, no key), hub "PJM WH Real Time Peak" — real OTC
     trade wtd-avg $/MWh by delivery day. BIWEEKLY publication + daily-hub
     aggregation: this is a lagged proxy, NOT real-time LMP — every print is
     stamped with its delivery date, never "now". Spark spread computed inline
     vs Henry Hub (yfinance NG=F latest daily close, own date stamp) using a
     7.0 MMBtu/MWh heat rate = EIA's published spark-spread benchmark (7,000
     Btu/kWh, efficient-CCGT proxy — NOT a live marginal-unit HR; full EIA-923
     PJM-fleet derivation spec'd next session). REVIEW (rc=1) trips on:
     latest proxy print >= $500/MWh (Orange band) OR spark spread negative.

  5. OFFICIAL LMP (added 2026-07-16, PROME-wired Will-directed after the
     PJM_API_KEY landed — see MACHINE_LOCAL.md PJM row): PJM Data Miner 2
     `rt_unverified_fivemin_lmps`, PJM-RTO aggregate (pnode_id=1), all 5-min
     prints for the current EPT day. Latest print + today's max, each with its
     EPT stamp. This closes the leg-4 blind spot (the 7/12 intraday spike class:
     e.g. 7/16 printed $410.55 @11:30 EPT while the proxy's newest row was days
     old). UNVERIFIED feed = operational read, NOT settlement data — PJM's
     verified hourly feed (rt_hrl_lmps) lags ~4 DAYS, NOT one business day
     (MEASURED 2026-08-17 09:20 EPT: frontier 8/13 while 8/14, 8/15 and 8/16
     all returned 0 rows, against a control pull of 7/23-8/2 that returned its
     full 264 rows. The earlier "next business day ~11 AM-12 PM" written here
     was assumed, never probed — see KB-WATT-081 / L-33. Re-measure with a
     known-good-period control + a frontier walk before trusting any figure
     here again);
     cite prints as "unverified 5-min". Key from FORGE .env (PJM_API_KEY,
     loaded by the fetch.py import); key ABSENT = leg prints a SKIP note, not
     a failure (laptop until the key is copied — env_doctor flags it at boot).
     REVIEW (rc=1) trips when latest OR today-max >= $500 (Orange band).

Exit codes: 0 = ok/quiet · 1 = emergency-class posting(s) OR Orange-band
LMP print (official latest/today-max, or proxy latest) OR negative spark
spread — review · 2 = fetch/parse failure.

HONEST WALLS (what this script does NOT cover, and why):
  - Settlement-grade LMPs: leg 5 reads the UNVERIFIED 5-min feed (fresh but
    subject to PJM verification); the verified hourly feed lags a business
    day. Anything settlement-critical re-reads rt_hrl_lmps after posting.
  - Non-member key = 6 calls/min: leg 5 spends 1 call/run. Do not loop it.
  - Structural capacity cost: 2026/27 BRA cleared at the $329.17/MW-day cap,
    2027/28 at the $333.44 cap (uncapped sim ~$530; 6,623 MW short of the
    reliability requirement). Annual cadence, tracked via BRA PDFs — not here.

Usage (self-locating, works from any cwd — venv python REQUIRED: leg 4 needs
openpyxl, which lives in the repo venv, not system python):
  /home/willi/Research-workspace/.venv/bin/python3 /home/willi/Research-workspace/AGENTS/WATT/power_watch.py
"""

import json
import os
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

# Self-locate the shared FORGE EIA client (fetch.py) regardless of cwd.
# This file lives at AGENTS/WATT/power_watch.py -> parents[2] == repo root.
# fetch.py stays in FORGE/tools/market-data/ (shared client, not moved).
_FORGE_MD = Path(__file__).resolve().parents[2] / "FORGE" / "tools" / "market-data"
sys.path.insert(0, str(_FORGE_MD))
import fetch  # noqa: E402  (eia_pjm_demand, eia_retail_power_price, .env loader)

PJM_EP_URL = "https://emergencyprocedures.pjm.com/"
BROWSER_UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

# Emergency-class message types (trip REVIEW / rc=1). Everything else on the
# postings board is surfaced in the count but treated as routine/local.
HIGH_SEV_PAT = re.compile(
    r"EEA|Capacity Emergency|Load Shed|Load Dump|Voltage Reduction"
    r"|Emergency Load Mgmt|Pre-Emergency Load Mgmt|Conservative Operations"
    r"|Deploy All Resources|Maximum Generation Emergency|Load Management Alert",
    re.IGNORECASE)

NEAR_PEAK_PCT = 95.0  # latest hour within 5% of 24h peak = stress hint

# --- Leg 4: LMP-proxy + spark spread (EIA ICE wholesale file) ---------------
EIA_WHOLESALE_URL = "https://www.eia.gov/electricity/wholesale/xls/ice_electric-{year}.xlsx"
PJM_HUB = "PJM WH Real Time Peak"  # the PJM Western Hub row in the EIA file
# Heat rate for the spark spread (MMBtu/MWh). CALIBRATED 2026-07-12 (rd-3) from
# a NAMED PUBLISHED proxy, no longer a bare guess: 7.0 MMBtu/MWh = EIA's own
# standard spark-spread benchmark of 7,000 Btu/kWh ("a fairly new and efficient
# natural gas combined-cycle generator" — eia.gov/todayinenergy/includes/
# sparkspread_explain.php). PJM-specific vintage range [EIA id=47556, 2020 data]:
# 1990s CCGT >8,000, 2000s 7,300, 2010s 6,700-7,000 Btu/kWh. So 7.0 is the
# efficient-CCGT end; the marginal price-setting unit during scarcity is often
# OLDER/less-efficient (higher HR), which would NARROW the computed spread.
# CAVEAT still stands: fleet-BENCHMARK, not a live marginal-unit heat rate.
# Full EIA-923 PJM-gas-fleet-average derivation spec'd next session (KB-WATT-025).
# Low sensitivity while gas is cheap: at HH ~$3 a 7.0->8.0 swing moves the
# spread only ~$3/MWh. HEAT_RATE_LABEL prints with every spread.
HEAT_RATE_MMBTU_PER_MWH = 7.0
HEAT_RATE_LABEL = "EIA benchmark 7,000 Btu/kWh (efficient-CCGT proxy, not live marginal HR)"
LMP_ORANGE = 500.0   # $/MWh — WATT THRESHOLDS Orange band
LMP_RED = 1000.0     # $/MWh — WATT THRESHOLDS Red band / scarcity cap zone

# Max allowed vintage gap (days) between the spark's power leg and its gas leg.
# Beyond this the proxy-basis spread is REFUSED, not caveated (L-17 fix 2026-08-17;
# N5 v1.1 capture-time clause). 3 days tolerates a weekend; the ICE file's real
# lag is ~12 days, so in practice the proxy spark is refused and the same-vintage
# DM2 figure carries. Chosen from the CADENCE of the gas leg (daily), not inherited.
SPARK_MAX_VINTAGE_GAP_DAYS = 3


def fetch_pjm_postings():
    """Scrape the PJM emergency-procedures postings dashboard.
    Returns (postings, high_sev) — lists of dicts — or raises on fetch/parse
    failure (never fabricates). postings rows: msg_id, priority, type, when
    (EPT, as posted), region."""
    req = urllib.request.Request(
        PJM_EP_URL, headers={"User-Agent": BROWSER_UA, "Accept": "text/html"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        html = resp.read().decode("utf-8", "replace")

    if "Emergency Procedures" not in html:
        raise ValueError("PJM EP page fetched but title marker missing — layout change?")

    postings = []
    for row in re.findall(r"<tr[^>]*data-ri[^>]*>(.*?)</tr>", html, flags=re.S):
        cells = [re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", c)).strip()
                 for c in re.findall(r"<td[^>]*>(.*?)</td>", row, flags=re.S)]
        if len(cells) >= 6 and cells[1].isdigit():
            postings.append({"msg_id": cells[1], "priority": cells[2],
                             "type": cells[3], "when": cells[4], "region": cells[5]})

    if not postings and "No records found" not in html and 'class="posting"' not in html:
        # Zero rows AND no empty-table marker AND no posting blocks = parse break, not a quiet board.
        raise ValueError("PJM EP page parsed to 0 postings with no empty-marker — layout change?")

    high_sev = [p for p in postings if HIGH_SEV_PAT.search(p["type"])]
    return postings, high_sev


def read_pjm_demand():
    """EIA-930 PJM demand: (latest_mw, latest_stamp_utc, peak24_mw, peak_stamp, pct_of_peak)."""
    rows = fetch.eia_pjm_demand(hours=26)
    if not rows or "error" in rows[0]:
        raise ValueError(f"EIA-930 PJM demand fetch failed: {rows[0].get('error') if rows else 'no rows'}")
    latest = rows[0]
    window = rows[1:25]  # the 24 hours preceding the latest print
    if len(window) < 20:
        raise ValueError(f"EIA-930 returned only {len(rows)} hourly rows — cannot form a 24h peak window")
    latest_mw = float(latest["value"])
    peak_row = max(window, key=lambda r: float(r["value"]))
    peak_mw = float(peak_row["value"])
    pct = latest_mw / peak_mw * 100.0 if peak_mw else 0.0
    return latest_mw, latest["date"], peak_mw, peak_row["date"], pct


def read_retail_prices():
    """Latest monthly US retail power prices: {"IND": (c/kWh, "YYYY-MM"), "RES": ...}."""
    rows = fetch.eia_retail_power_price(sectors=("IND", "RES"), state="US", months=3)
    if not rows or "error" in rows[0]:
        raise ValueError(f"EIA retail-sales fetch failed: {rows[0].get('error') if rows else 'no rows'}")
    out = {}
    for r in rows:  # newest-first; keep first (latest) print per sector
        sec = r.get("sectorid")
        if sec in ("IND", "RES") and sec not in out:
            out[sec] = (float(r["value"]), r["date"])
    if "IND" not in out or "RES" not in out:
        raise ValueError(f"EIA retail-sales missing a sector (got {sorted(out)})")
    return out


def read_wholesale_pjm(rows_back=10):
    """LMP-proxy: EIA's free ICE-sourced wholesale price file, PJM Western Hub
    RT Peak rows. Returns the last `rows_back` rows sorted by trade date, each
    {trade, deliv, wtd, high, low} with datetime.date stamps. BIWEEKLY
    publication — the newest row can lag real time by up to ~2 weeks; callers
    must cite the delivery date, never 'now'. Fail-loud: raises on fetch/parse
    failure or zero hub rows (hub rename / layout change), never fabricates."""
    import io
    from openpyxl import load_workbook

    year = datetime.now(timezone.utc).year
    url = EIA_WHOLESALE_URL.format(year=year)
    req = urllib.request.Request(url, headers={"User-Agent": BROWSER_UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = resp.read()

    wb = load_workbook(io.BytesIO(data), data_only=True, read_only=True)
    ws = wb[wb.sheetnames[0]]
    rows = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        # cols: hub(0) trade_date(1) deliv_start(2) deliv_end(3) high(4) low(5) wtd_avg(6)
        if row and row[0] == PJM_HUB and row[1] is not None and row[6] is not None:
            rows.append({"trade": row[1].date(), "deliv": row[2].date() if row[2] else None,
                         "wtd": float(row[6]), "high": float(row[4]), "low": float(row[5])})
    wb.close()
    if not rows:
        raise ValueError(f"EIA wholesale file parsed but 0 '{PJM_HUB}' rows — "
                         f"hub renamed or layout change? ({url})")
    rows.sort(key=lambda r: r["trade"])
    return rows[-rows_back:]


def read_henry_hub():
    """Henry Hub front-month (NG=F) latest daily close + ITS OWN date stamp
    (yfinance). The stamp can differ from the LMP-proxy's delivery date —
    callers print both, never blend the vintages."""
    import yfinance as yf
    h = yf.Ticker("NG=F").history(period="10d")
    if h is None or h.empty:
        raise ValueError("yfinance NG=F returned no rows")
    return float(h["Close"].iloc[-1]), h.index[-1].date().isoformat()


# --- Leg 5: official LMP (PJM Data Miner 2) ---------------------------------
PJM_DM2_BASE = "https://api.pjm.com/api/v1"
PJM_RTO_PNODE_ID = 1  # PJM-RTO aggregate node


def read_pjm_lmp_official(api_key):
    """Official PJM-RTO real-time LMP via Data Miner 2 `rt_unverified_fivemin_lmps`
    (posts every 5 min, ~5-10 min behind real time; UNVERIFIED — operational read,
    not settlement). Pulls every 5-min print for the current EPT day and returns
    ((latest_lmp, latest_stamp_ept), (max_lmp, max_stamp_ept), n_prints).
    Date format has NO leading zeros (m/d/yyyy) — the API's accepted form,
    live-verified 2026-07-16. Fail-loud: raises on HTTP error, 0 rows, or a
    schema change (missing fields); never fabricates."""
    now_ept = datetime.now(ZoneInfo("America/New_York"))
    day = f"{now_ept.month}/{now_ept.day}/{now_ept.year}"
    qs = urllib.parse.urlencode({
        "rowCount": 500, "startRow": 1,
        "datetime_beginning_ept": f"{day} 00:00to{day} 23:59",
        "pnode_id": PJM_RTO_PNODE_ID,
        "fields": "datetime_beginning_ept,total_lmp_rt",
    })
    req = urllib.request.Request(
        f"{PJM_DM2_BASE}/rt_unverified_fivemin_lmps?{qs}",
        headers={"Ocp-Apim-Subscription-Key": api_key})
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    items = payload.get("items") or []
    if not items:
        raise ValueError(f"Data Miner 2 returned 0 five-min rows for pnode "
                         f"{PJM_RTO_PNODE_ID} on {day} EPT — feed gap or query break "
                         f"(errors: {payload.get('errors')})")
    items.sort(key=lambda r: r["datetime_beginning_ept"])
    latest = items[-1]
    peak = max(items, key=lambda r: float(r["total_lmp_rt"]))
    stamp = lambda r: r["datetime_beginning_ept"][11:16] + " EPT"  # noqa: E731
    return ((float(latest["total_lmp_rt"]), stamp(latest)),
            (float(peak["total_lmp_rt"]), stamp(peak)), len(items))


def read_pjm_onpeak_mean(api_key, days=6, end=None):
    """SAME-VINTAGE power leg for the spark spread: mean PJM-RTO on-peak RT LMP
    (HE08-23 EPT) over the `days` calendar days ENDING at `end` (default: the
    most recent complete EPT day). Returns (mean_lmp, first_day, last_day, n).

    WHY THIS EXISTS (L-17, 2026-08-04; reinforced by N5 v1.1's capture-time
    clause 2026-08-13): leg-4's spark paired a ~12-day-stale ICE power print with
    a SAME-DAY gas quote. On 2026-08-17 that printed +$59.37/MWh against a
    same-vintage +$48.31 — an $11.06 overstatement, and the error GROWS the more
    the market trends, because the stale leg is drawn from a different regime.
    A derived metric across mismatched vintages is biased toward the regime its
    stale leg came from; it is not a measurement.

    BASIS NOTE, and it matters: this is RT on-peak LMP, NOT the ICE peak-period
    OTC print. Different products. This series and the leg-4 proxy series are NOT
    interchangeable, and a level change BETWEEN them is a basis change, not a
    market move — never score that delta against P4's 'compresses 50%' trigger.
    Uses the UNVERIFIED 5-min feed (the verified hourly lags ~4 days, measured
    2026-08-17, KB-WATT-081), so it is an operational read, not settlement.
    """
    now_ept = datetime.now(ZoneInfo("America/New_York"))
    last = end or (now_ept.date() - timedelta(days=1))
    first = last - timedelta(days=days - 1)
    fmt = lambda d: f"{d.month}/{d.day}/{d.year}"  # noqa: E731 — API wants no leading zeros
    qs = urllib.parse.urlencode({
        "rowCount": 6000, "startRow": 1,
        "datetime_beginning_ept": f"{fmt(first)} 00:00to{fmt(last)} 23:59",
        "pnode_id": PJM_RTO_PNODE_ID,
        "fields": "datetime_beginning_ept,total_lmp_rt",
    })
    req = urllib.request.Request(
        f"{PJM_DM2_BASE}/rt_unverified_fivemin_lmps?{qs}",
        headers={"Ocp-Apim-Subscription-Key": api_key})
    with urllib.request.urlopen(req, timeout=45) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    items = payload.get("items") or []
    onpeak = [r for r in items if 8 <= int(r["datetime_beginning_ept"][11:13]) <= 23]
    vals = [float(r["total_lmp_rt"]) for r in onpeak]
    if len(vals) < 100:  # ~12 prints/hr x 16 on-peak hrs x 6d ~= 1150; fail loud
        raise ValueError(
            f"DM2 on-peak window {first}..{last} returned only {len(vals)} on-peak "
            f"prints ({len(items)} rows total) — feed gap or query break, refusing "
            f"to compute a spark from a thin window")

    # COVERAGE assert (added 2026-09-06, L-44). A COUNT check cannot see a window
    # SHORTER than the one it labels. The unverified 5-min feed retains only ~15
    # days and returns the surviving slice with NO error: a 8/10-8/23 request on
    # 9/6 returned 336 rows covering 8/22-8/23 only. That is >100 prints, so the
    # count guard passes and the caller gets a 2-day mean LABELLED as 14-day.
    # Same defect class as the unfiltered-pnode truncation: a short read is not
    # an error here, so the guard has to be about COVERAGE, not volume.
    got_days = {r["datetime_beginning_ept"][:10] for r in onpeak}
    want_days = {(first + timedelta(days=i)).isoformat() for i in range(days)}
    missing = want_days - got_days
    if missing:
        raise ValueError(
            f"DM2 on-peak window {first}..{last} is SHORT: {len(got_days)}/{days} "
            f"days present, missing {sorted(missing)} — the 5-min feed's ~15-day "
            f"retention boundary (or a feed gap) fell inside the window. Refusing "
            f"to label a {len(got_days)}-day mean as a {days}-day one.")
    thin = sorted(d for d in got_days if sum(
        1 for r in onpeak if r["datetime_beginning_ept"][:10] == d) < 150)  # 192 = full day
    if thin:
        raise ValueError(
            f"DM2 on-peak window {first}..{last}: day(s) {thin} carry <150 of 192 "
            f"on-peak prints — partial day at a retention/feed boundary, refusing.")

    # DISPERSION flag (added 2026-09-06, L-44 forward rule). A trailing window
    # that swallows a scarcity episode manufactures a trend: the 8/4->9/6 spark
    # series read +$29.84 -> +$48.12 -> +$53.65 -> +$77.02 and then +$28.98 once
    # measured on a CLEAN window — each level tracked its emergency-day count
    # (0 -> ? -> 1 -> 3 -> 0), not the spread. The mean alone cannot show that.
    #
    # SCOPE, STATED NARROWLY (tightened 2026-09-06 after an external review built
    # the counter-example): this is a SINGLE-DAY OUTLIER DETECTOR against the
    # window median. It is NOT an emergency-window classifier and it FAILS BY
    # CONSTRUCTION when the contaminated days are the MAJORITY — a 6-day window
    # with 4 high days lifts the median itself and nothing fires. It caught the
    # 8/31-9/5 window only because 9/1 alone was extreme (3.1x a $68.36 median).
    # A SILENT FLAG MEANS "no single day dominates", NEVER "this window is clean."
    # Deliberately not replaced with a cleverer detector: the honest scope note is
    # the fix, and a detector trusted past its scope is worse than none.
    by_day = {}
    for r in onpeak:
        by_day.setdefault(r["datetime_beginning_ept"][:10], []).append(
            float(r["total_lmp_rt"]))
    dm = sorted((sum(v) / len(v), d) for d, v in by_day.items())
    med = dm[len(dm) // 2][0]
    note = None
    if med > 0:
        flagged = [(m, d) for m, d in dm if m > 2.0 * med]
        if flagged:
            days = " · ".join(f"{d} ${m:,.2f} ({m / med:.1f}x)" for m, d in flagged)
            note = (f"⚠️ SINGLE-DAY OUTLIER(S) vs the window median ${med:,.2f}: {days}. "
                    f"This mean is a STRESS read, not a baseline — cite the window "
                    f"composition beside it and re-measure on a clean window before any "
                    f"DIRECTION claim. NOTE: median-based, so it CANNOT see contamination "
                    f"that is the majority of the window; silence != clean.")
    return sum(vals) / len(vals), first, last, len(vals), note


def lmp_band(wtd):
    """WATT THRESHOLDS band label for a $/MWh print."""
    if wtd >= LMP_RED:
        return "RED (>=$1,000)"
    if wtd >= LMP_ORANGE:
        return "ORANGE (>=$500)"
    if wtd >= 150.0:
        return "YELLOW (>=$150)"
    return "normal"


def main():
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print(f"{'=' * 72}\n  POWER WATCH (PJM leg) — fetched {now_utc}\n{'=' * 72}")

    failures = []

    # --- 1. PJM emergency postings ---
    postings = high_sev = None
    try:
        postings, high_sev = fetch_pjm_postings()
        if postings:
            print(f"\n  PJM EMERGENCY POSTINGS ({len(postings)} on board, times EPT):")
            for p in postings[:8]:
                sev = "  << EMERGENCY-CLASS — REVIEW" if HIGH_SEV_PAT.search(p["type"]) else ""
                print(f"    [{p['when']}] {p['priority']}: {p['type']} ({p['region']}, #{p['msg_id']}){sev}")
            if len(postings) > 8:
                print(f"    ... +{len(postings) - 8} more — review {PJM_EP_URL}")
        else:
            print("\n  PJM EMERGENCY POSTINGS: none on board")
    except Exception as e:
        failures.append(f"PJM-EP: {e}")
        print(f"\n  ERROR PJM emergency postings fetch/parse FAILED: {e}\n"
              f"  Manual check: {PJM_EP_URL}", file=sys.stderr)

    # --- 2. PJM demand (EIA-930) ---
    demand = None
    try:
        demand = read_pjm_demand()
        latest_mw, latest_ts, peak_mw, peak_ts, pct = demand
        hint = "  << NEAR 24h PEAK" if pct >= NEAR_PEAK_PCT else ""
        print(f"\n  PJM DEMAND (EIA-930, UTC hour stamps; publishes ~2-6h behind real time):")
        print(f"    Latest:   {latest_mw:>9,.0f} MW  @{latest_ts}Z{hint}")
        print(f"    24h peak: {peak_mw:>9,.0f} MW  @{peak_ts}Z  (latest = {pct:.1f}% of peak)")
    except Exception as e:
        failures.append(f"EIA-930: {e}")
        print(f"\n  ERROR PJM demand (EIA-930) FAILED: {e}", file=sys.stderr)

    # --- 3. Retail price backdrop ---
    retail = None
    try:
        retail = read_retail_prices()
        print(f"\n  RETAIL PRICE BACKDROP (US avg, EIA monthly, ~2mo lag):")
        # (source-mode note printed once, after both EIA legs — see below)
        print(f"    Industrial:  {retail['IND'][0]:.2f} c/kWh ({retail['IND'][1]})")
        print(f"    Residential: {retail['RES'][0]:.2f} c/kWh ({retail['RES'][1]})")
    except Exception as e:
        failures.append(f"retail: {e}")
        print(f"\n  ERROR retail price backdrop FAILED: {e}", file=sys.stderr)

    # --- EIA source-mode provenance (DAEDALUS SFG sweep §8 rule 1, 2026-08-17) ---
    # Legs 2 and 3 call the shared FORGE fetch.py, which has a cache layer whose
    # HITS CARRY NO MARKER in the returned payload (logged only to
    # logs/market_data.log). So a cache-served value renders here exactly like a
    # live pull. The TTL bounds the damage (<=1hr) and both legs already stamp the
    # DATA vintage — which is the figure that matters for a claim — but the
    # SOURCE-MODE is genuinely not distinguishable from this side.
    # Stating the limit is the honest fix; asserting "live" would be the PAT-107
    # error (my own: I published an instrument clock I had assumed, not probed).
    # A real fix belongs in fetch.py = FORGE = shared: flagged to PROME, not
    # edited here (root CLAUDE.md — do not commit outside your own dir).
    print("\n  NOTE: EIA LEG PROVENANCE — date stamps above are DATA vintage (authoritative). "
          "SOURCE-MODE (live pull vs <=1hr FORGE cache hit) is NOT distinguishable "
          "from this side — fetch.py cache hits carry no payload marker. "
          "Not an alert; a stated wall.")

    # --- 4. LMP-proxy + spark spread (EIA ICE wholesale, biweekly lag) ---
    lmp = None          # latest proxy row
    spread = None       # $/MWh, vs assumed heat rate
    hh = None           # (close, date)
    lmp_review = False
    try:
        px = read_wholesale_pjm()
        lmp = px[-1]
        wmax = max(px, key=lambda r: r["wtd"])
        print(f"\n  LMP-PROXY (EIA ICE wholesale, {PJM_HUB}; BIWEEKLY file — "
              f"latest row can lag ~2wk, cite delivery dates):")
        for r in px[-5:]:
            flag = f"  << {lmp_band(r['wtd'])}" if r["wtd"] >= 150.0 else ""
            print(f"    deliv {r['deliv']} (traded {r['trade']}): "
                  f"wtd ${r['wtd']:,.2f}/MWh (hi {r['high']:,.2f} / lo {r['low']:,.2f}){flag}")
        if wmax is not lmp and wmax["wtd"] >= 150.0:
            print(f"    window max: ${wmax['wtd']:,.2f}/MWh deliv {wmax['deliv']} "
                  f"[{lmp_band(wmax['wtd'])}] — {len(px)}-row window")
        if lmp["wtd"] >= LMP_ORANGE:
            lmp_review = True
            print(f"    LATEST PRINT {lmp_band(lmp['wtd'])} — REVIEW")

        try:
            hh = read_henry_hub()
            print(f"\n  SPARK SPREAD (P4; heat rate {HEAT_RATE_MMBTU_PER_MWH} MMBtu/MWh "
                  f"= {HEAT_RATE_LABEL}):")

            # --- PRIMARY: same-vintage spark off DM2 on-peak (L-17 fix, 8/17) ---
            api_key = os.environ.get("PJM_API_KEY")
            if api_key:
                try:
                    opk, d0, d1, n, wnote = read_pjm_onpeak_mean(api_key, days=6)
                    spread = opk - HEAT_RATE_MMBTU_PER_MWH * hh[0]
                    spread_hi = opk - 8.0 * hh[0]
                    print(f"    SAME-VINTAGE (primary): PJM-RTO on-peak mean "
                          f"${opk:,.2f}/MWh (HE08-23 EPT, {d0}..{d1}, n={n:,}) - "
                          f"{HEAT_RATE_MMBTU_PER_MWH} x HH ${hh[0]:.3f} ({hh[1]}) "
                          f"= {'+' if spread >= 0 else ''}${spread:,.2f}/MWh")
                    if wnote:
                        print(f"      {wnote}")
                    print(f"      sensitivity @ HR 8.0 (older marginal unit): "
                          f"{'+' if spread_hi >= 0 else ''}${spread_hi:,.2f}/MWh "
                          f"(delta ${spread - spread_hi:,.2f} — low while gas is cheap)")
                except Exception as e:  # noqa: BLE001
                    failures.append(f"DM2 on-peak: {e}")
                    print(f"    ⚠️ SAME-VINTAGE spark NOT COMPUTED (DM2 on-peak leg "
                          f"failed: {e})", file=sys.stderr)
            else:
                print("    ⚠️ SAME-VINTAGE spark SKIPPED — no PJM_API_KEY "
                      "(proxy-basis figure below is vintage-mismatched; see refusal rule)")

            # --- SECONDARY: ICE-proxy spark, REFUSED on a stale power leg -------
            # L-17 / N5 v1.1 capture-time clause: do NOT print a spread whose two
            # legs are days apart. It is not conservative to print it with a
            # caveat — the number gets quoted and the caveat does not travel.
            gap = None
            if lmp["deliv"] is not None:
                try:
                    gap = (datetime.strptime(hh[1], "%Y-%m-%d").date() - lmp["deliv"]).days
                except Exception:  # noqa: BLE001
                    gap = None
            proxy_spread = lmp["wtd"] - HEAT_RATE_MMBTU_PER_MWH * hh[0]
            if gap is not None and gap > SPARK_MAX_VINTAGE_GAP_DAYS:
                print(f"    NOTE: PROXY-BASIS spark REFUSED (by design) — power leg deliv {lmp['deliv']} "
                      f"vs gas leg {hh[1]} = {gap}-day vintage gap "
                      f"(> {SPARK_MAX_VINTAGE_GAP_DAYS}d limit). Would have printed "
                      f"{'+' if proxy_spread >= 0 else ''}${proxy_spread:,.2f}/MWh — "
                      f"a stale-regime power leg against today's gas. Use the "
                      f"same-vintage figure above.")
            else:
                print(f"    proxy basis: power ${lmp['wtd']:,.2f} (deliv {lmp['deliv']}) - "
                      f"{HEAT_RATE_MMBTU_PER_MWH} x HH ${hh[0]:.3f} ({hh[1]}) "
                      f"= {'+' if proxy_spread >= 0 else ''}${proxy_spread:,.2f}/MWh "
                      f"(gap {gap}d)")
                if spread is None:
                    spread = proxy_spread
            print("      NOTE: BASIS — RT on-peak LMP != ICE peak-period OTC — different "
                  "products. Never treat the two as one compression time-series.")

            if spread is not None and spread < 0:
                lmp_review = True
                print(f"    SPREAD NEGATIVE — gas-fired uneconomic — REVIEW")
        except Exception as e:
            failures.append(f"HenryHub: {e}")
            print(f"\n  ERROR Henry Hub (NG=F) FAILED: {e} — spark spread not computed",
                  file=sys.stderr)
    except Exception as e:
        failures.append(f"EIA-wholesale: {e}")
        print(f"\n  ERROR LMP-proxy (EIA wholesale) FAILED: {e}\n"
              f"  Manual check: https://www.eia.gov/electricity/wholesale/", file=sys.stderr)

    # --- 5. Official LMP (PJM Data Miner 2, 5-min unverified) ---
    lmp_off = None      # ((latest, stamp), (max, stamp), n_prints)
    pjm_key = os.environ.get("PJM_API_KEY", "")
    if not pjm_key:
        print(f"\n  OFFICIAL LMP: SKIPPED — PJM_API_KEY absent from the FORGE .env on this "
              f"box (machine-local; copy it per PROME/MACHINE_LOCAL.md PJM row — env_doctor "
              f"flags this at boot). Leg-4 proxy above is the only price read: it can MISS "
              f"intra-day spikes.")
    else:
        try:
            lmp_off = read_pjm_lmp_official(pjm_key)
            (cur, cur_ts), (pk, pk_ts), n = lmp_off
            cur_flag = f"  << {lmp_band(cur)}" if cur >= 150.0 else ""
            pk_flag = f"  << {lmp_band(pk)}" if pk >= 150.0 else ""
            print(f"\n  OFFICIAL LMP (Data Miner 2, PJM-RTO 5-min UNVERIFIED — operational "
                  f"read, not settlement; verified hourly lags ~4 days [measured 8/17]):")
            print(f"    latest:    ${cur:>9,.2f}/MWh  @{cur_ts}{cur_flag}")
            print(f"    today max: ${pk:>9,.2f}/MWh  @{pk_ts}  ({n} prints since 00:00 EPT){pk_flag}")
            if cur >= LMP_ORANGE or pk >= LMP_ORANGE:
                lmp_review = True
                print(f"    OFFICIAL PRINT {lmp_band(max(cur, pk))} — REVIEW")
        except Exception as e:
            failures.append(f"DM2-LMP: {e}")
            print(f"\n  ERROR official LMP (Data Miner 2) FAILED: {e}\n"
                  f"  Manual check: https://dataminer2.pjm.com/feed/rt_unverified_fivemin_lmps",
                  file=sys.stderr)

    # --- Verdict (always printed; failed legs say so, never fabricated) ---
    if demand:
        d = f"PJM demand {demand[0]:,.0f} MW @{demand[1]}Z ({demand[4]:.1f}% of 24h peak)"
    else:
        d = "PJM demand FETCH-FAIL"
    if postings is None:
        e = "emergencies: FETCH-FAIL — check " + PJM_EP_URL
    elif high_sev:
        e = f"emergencies: {len(postings)} postings, {len(high_sev)} emergency-class — REVIEW"
    elif postings:
        e = f"emergencies: {len(postings)} postings (routine/local, 0 emergency-class)"
    else:
        e = "emergencies: none posted"
    r = (f"retail ind {retail['IND'][0]:.2f} c/kWh ({retail['IND'][1]}), "
         f"res {retail['RES'][0]:.2f} ({retail['RES'][1]})") if retail else "retail FETCH-FAIL"
    if lmp_off:
        (ocur, ocur_ts), (opk, opk_ts), _n = lmp_off
        o = (f"LMP {ocur:,.2f} @{ocur_ts} / max {opk:,.2f} @{opk_ts} "
             f"[{lmp_band(max(ocur, opk))}] (DM2 5-min unverified)")
    elif pjm_key:
        o = "LMP official FETCH-FAIL"
    else:
        o = "LMP official SKIP (no key this box)"
    if lmp:
        p = f"LMP-proxy ${lmp['wtd']:,.2f}/MWh deliv {lmp['deliv']} [{lmp_band(lmp['wtd'])}]"
        if spread is not None:
            p += (f" · spark {'+' if spread >= 0 else ''}${spread:,.2f}/MWh "
                  f"(HR {HEAT_RATE_MMBTU_PER_MWH} = EIA benchmark; gas {hh[1]})")
        else:
            p += " · spark NOT COMPUTED (gas leg fail)"
    else:
        p = "LMP-proxy FETCH-FAIL"
    print(f"\n  Power leg: {d} · {e} · {o} · {p} · {r}\n")

    if failures:
        print(f"power_watch: {len(failures)} leg(s) FAILED — {'; '.join(failures)}", file=sys.stderr)
        return 2
    return 1 if (high_sev or lmp_review) else 0


if __name__ == "__main__":
    sys.exit(main())
