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

Three reads, one verdict line, each fail-LOUD (stderr + rc=2, never fabricated):
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

Exit codes: 0 = ok/quiet · 1 = emergency-class posting(s) — review · 2 = fetch/parse failure.

HONEST WALLS (what this script does NOT cover, and why):
  - LMPs (the actual price leg): PJM Data Miner 2 needs a free pjm.com account
    + subscription key — one-time HUMAN registration (6 calls/min non-member).
    LMP wiring is the named next increment once a key lands in
    FORGE/tools/market-data/.env as PJM_API_KEY. Alternative: gridstatus.io
    free tier — also signup-gated.
  - Structural capacity cost: 2026/27 BRA cleared at the $329.17/MW-day cap,
    2027/28 at the $333.44 cap (uncapped sim ~$530; 6,623 MW short of the
    reliability requirement). Annual cadence, tracked via BRA PDFs — not here.

Usage (self-locating, works from any cwd):
  python3 /home/willi/Research-workspace/AGENTS/WATT/power_watch.py
"""

import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

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
        print(f"    Industrial:  {retail['IND'][0]:.2f} c/kWh ({retail['IND'][1]})")
        print(f"    Residential: {retail['RES'][0]:.2f} c/kWh ({retail['RES'][1]})")
    except Exception as e:
        failures.append(f"retail: {e}")
        print(f"\n  ERROR retail price backdrop FAILED: {e}", file=sys.stderr)

    print(f"\n  NOTE: LMP price leg NOT wired — needs PJM_API_KEY in .env "
          f"(free pjm.com registration, human one-time). See header.")

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
    print(f"\n  Power leg: {d} · {e} · {r}\n")

    if failures:
        print(f"power_watch: {len(failures)} leg(s) FAILED — {'; '.join(failures)}", file=sys.stderr)
        return 2
    return 1 if high_sev else 0


if __name__ == "__main__":
    sys.exit(main())
