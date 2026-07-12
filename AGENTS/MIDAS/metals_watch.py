#!/usr/bin/env python3
"""
metals_watch.py — MIDAS boot-time instrument: real yield + metals spot + GSR
+ M1 divergence flag.

Built 2026-07-12 (first real session, Will-directed priority build). Thin
wrapper over the shared FORGE market-data client (FORGE/tools/market-data/
fetch.py) — imported by absolute self-location, per WATT/power_watch.py's
precedent (see that file's header + FORGE README "shared client" note). If
fetch.py itself needs extending, that is a FORGE edit — flag to PROME, don't
fork it here.

SCOPE (per SCRATCH.md 2026-07-11 pickup, PAT-041 — wire the cadence durably
at build time): real yield (FRED DFII10) + gold/silver/copper/platinum/
palladium spot (COMEX futures primary: GC=F/SI=F/HG=F/PL=F/PA=F; ETF proxies
GLD/SLV/CPER/PPLT/PALL as a secondary cross-check row) + gold/silver ratio
(GSR, computed off futures) + an M1 divergence classifier (gold trend vs
real-yield trend over a trailing ~90-day window — CONVERGE = real-rate-
consistent / debasement premium NOT confirmed this window; DIVERGE = gold
holding/rising through rising real yields / premium confirmed this window).

LME COPPER INVENTORY LEG (added round-2 same day, 2026-07-12): westmetall.com
publishes the LME copper stock series (daily, business days) in a plain
server-rendered HTML table — scraped with a browser UA, fail-loud. This
closes the "no free LME source" wall hit earlier the same session (CME
warehouseStockAPI 403'd; LME.com vendor-gated). Sanity cross-check 7/12:
westmetall LME cash $13,408.50/t [7/10] vs COMEX HG=F $6.28/lb = $13,845/t
(~3% COMEX premium — consistent, two independent venues).

OUT OF SCOPE (documented gaps, not silently dropped):
  - CFTC COT (gold/silver/copper net positioning) — weekly cadence (Fri
    release, Tue data), not a daily-pull fit for this script. Pulled manually
    this session via the CFTC Socrata API (see STATUS.md baseline + KB rows);
    a future increment could wire a weekly-cadence COT leg here.
  - Copper vs 200dma (I1 threshold table) — needs a 200-trading-day history
    pull; scoped OUT of this first increment (kept to the SCRATCH-specified
    spot+yield+GSR legs). Computed manually this session (see STATUS.md);
    candidate next increment.

Exit codes: 0 = quiet · 1 = REVIEW (GSR band crossed, or M1 divergence state
flips vs STATUS.md's last-recorded state) · 2 = a leg failed (fail-LOUD,
never fabricated — a missing leg prints ERROR and is excluded from the
verdict, it is never silently treated as zero/neutral).

Usage (self-locating, works from any cwd):
  python3 /home/willi/Research-workspace/AGENTS/MIDAS/metals_watch.py
"""

import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

# Self-locate the shared FORGE client regardless of cwd.
# This file lives at AGENTS/MIDAS/metals_watch.py -> parents[2] == repo root.
_FORGE_MD = Path(__file__).resolve().parents[2] / "FORGE" / "tools" / "market-data"
sys.path.insert(0, str(_FORGE_MD))
import fetch  # noqa: E402

FUTURES = {"GC=F": "Gold fut", "SI=F": "Silver fut", "HG=F": "Copper fut",
           "PL=F": "Platinum fut", "PA=F": "Palladium fut"}
ETF_PROXIES = {"GLD": "Gold ETF", "SLV": "Silver ETF", "CPER": "Copper ETF",
               "PPLT": "Platinum ETF", "PALL": "Palladium ETF"}

# GSR bands (MIDAS CLAUDE.md THRESHOLDS table)
GSR_YELLOW, GSR_ORANGE, GSR_RED = 85, 90, 95

WESTMETALL_CU_URL = ("https://www.westmetall.com/en/markdaten.php"
                     "?action=table&field=LME_Cu_cash")
BROWSER_UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")


def read_lme_copper_stocks():
    """LME copper warehouse stocks (tonnes) scraped from westmetall.com's
    public daily table (columns: date | cash | 3-month | stock). Returns
    (rows_newest_first, latest, oldest) where each row = (date_str, tonnes).
    Fail-loud: raises on HTTP failure or if the table shape isn't recognized
    (never fabricates a value)."""
    req = urllib.request.Request(WESTMETALL_CU_URL, headers={"User-Agent": BROWSER_UA})
    with urllib.request.urlopen(req, timeout=25) as r:
        html = r.read().decode("utf-8", errors="replace")
    trs = re.findall(r"<tr[^>]*>(.*?)</tr>", html, re.S)
    data = []
    for tr in trs:
        cells = [re.sub(r"<[^>]+>", "", c).strip()
                 for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", tr, re.S)]
        if len(cells) == 4 and re.match(r"\d{2}\.\s", cells[0]):
            try:
                data.append((cells[0], int(cells[3].replace(",", ""))))
            except ValueError:
                continue  # non-numeric stock cell (header/blank) — skip, don't guess
    if len(data) < 5:
        raise ValueError(f"westmetall LME table parse got only {len(data)} rows — "
                         f"layout may have changed, check {WESTMETALL_CU_URL}")
    return data, data[0], data[-1]


def read_real_yield():
    """Latest DFII10 + a ~90-calendar-day-prior print for the divergence calc.
    Fail-loud: raises if fetch.py returns an error row or too few observations."""
    obs = fetch.fred_fetch("DFII10", limit=100)
    if obs and "error" in obs[0]:
        raise ValueError(f"FRED DFII10 fetch failed: {obs[0]['error']}")
    if len(obs) < 2:
        raise ValueError(f"FRED DFII10: too few observations ({len(obs)})")
    latest = obs[0]  # newest-first
    target = None
    # obs is newest->oldest; find first obs whose date is <= 90 days before latest
    from datetime import date as _date
    latest_d = _date.fromisoformat(latest["date"])
    for o in obs:
        d = _date.fromisoformat(o["date"])
        if (latest_d - d).days >= 88:
            target = o
            break
    if target is None:
        target = obs[-1]  # fall back to oldest available
    return latest, target


def read_spot(tickers_map):
    """price_fetch wrapper — raises if EVERY ticker errored (total fetch failure);
    partial failures are reported per-ticker (fail-loud, not silently dropped)."""
    results = fetch.price_fetch(list(tickers_map.keys()))
    if all("error" in d for d in results.values()):
        raise ValueError(f"ALL spot tickers failed: {results}")
    return results


def main():
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print(f"{'=' * 72}\n  METALS WATCH — fetched {now_utc}\n{'=' * 72}")

    failures = []

    # --- 1. Real yield (FRED DFII10) ---
    latest_y = target_y = None
    try:
        latest_y, target_y = read_real_yield()
        print(f"\n  REAL YIELD (FRED DFII10, T+1 publication lag):")
        print(f"    Latest: {latest_y['value']} [{latest_y['date']}]")
        print(f"    ~90d prior: {target_y['value']} [{target_y['date']}]")
    except Exception as e:
        failures.append(f"DFII10: {e}")
        print(f"\n  ERROR real-yield fetch FAILED: {e}", file=sys.stderr)

    # --- 2. Futures spot (primary) ---
    fut = None
    try:
        fut = read_spot(FUTURES)
        print(f"\n  METALS SPOT — COMEX futures (yfinance, weekend/holiday = last close):")
        for t, label in FUTURES.items():
            d = fut.get(t, {})
            if "error" in d:
                print(f"    {t:<8} {label:<14} ERROR: {d['error']}")
            else:
                print(f"    {t:<8} {label:<14} ${d['price']:>10,.2f}  chg {d['change_pct']:+.2f}%  (prev ${d['prev']:,.2f})")
    except Exception as e:
        failures.append(f"futures: {e}")
        print(f"\n  ERROR futures spot fetch FAILED: {e}", file=sys.stderr)

    # --- 3. ETF proxy spot (secondary cross-check) ---
    etf = None
    try:
        etf = read_spot(ETF_PROXIES)
        print(f"\n  METALS SPOT — ETF proxies (secondary cross-check, NOT 1:1 unit-matched to futures):")
        for t, label in ETF_PROXIES.items():
            d = etf.get(t, {})
            if "error" in d:
                print(f"    {t:<8} {label:<14} ERROR: {d['error']}")
            else:
                print(f"    {t:<8} {label:<14} ${d['price']:>10,.2f}  chg {d['change_pct']:+.2f}%  (prev ${d['prev']:,.2f})")
    except Exception as e:
        failures.append(f"etf: {e}")
        print(f"\n  ERROR ETF proxy spot fetch FAILED: {e}", file=sys.stderr)

    # --- 4. Gold/silver ratio (off futures) ---
    gsr = None
    gsr_band = None
    if fut and "error" not in fut.get("GC=F", {"error": 1}) and "error" not in fut.get("SI=F", {"error": 1}):
        gsr = fut["GC=F"]["price"] / fut["SI=F"]["price"]
        gsr_band = ("RED" if gsr >= GSR_RED else
                    "ORANGE" if gsr >= GSR_ORANGE else
                    "YELLOW" if gsr >= GSR_YELLOW else "benign")
        print(f"\n  GOLD/SILVER RATIO: {gsr:.2f}  (bands: Y{GSR_YELLOW}/O{GSR_ORANGE}/R{GSR_RED} — currently {gsr_band})")
    else:
        failures.append("GSR: could not compute (gold or silver futures leg failed)")
        print(f"\n  ERROR GSR not computed — gold/silver futures leg failed", file=sys.stderr)

    # --- 5. M1 divergence classifier ---
    divergence_state = None
    if latest_y and target_y and fut and "error" not in fut.get("GC=F", {"error": 1}):
        try:
            y_chg_bp = (float(latest_y["value"]) - float(target_y["value"])) * 100
            gold_now = fut["GC=F"]["price"]
            # need gold price ~90d ago too — pull short history for GC=F
            hist = fetch.price_history(["GC=F"], days=100)["GC=F"]
            if "error" in hist:
                raise ValueError(hist["error"])
            gold_then = hist["history"][0]["close"]  # oldest in window
            gold_then_date = hist["history"][0]["date"]
            gold_chg_pct = (gold_now - gold_then) / gold_then * 100
            if y_chg_bp > 0 and gold_chg_pct < 0:
                divergence_state = "CONVERGE (real-rate-consistent — yields up, gold down; debasement premium NOT confirmed this window)"
            elif y_chg_bp > 0 and gold_chg_pct >= 0:
                divergence_state = "DIVERGE (debasement premium LIVE — yields up, gold holding/up)"
            elif y_chg_bp <= 0 and gold_chg_pct > 0:
                divergence_state = "CLASSIC (yields down, gold up — expected inverse relationship)"
            else:
                divergence_state = "BOTH-DOWN (unusual — yields down AND gold down; check liquidity/USD confound)"
            print(f"\n  M1 DIVERGENCE CHECK (trailing ~90d, {gold_then_date} -> {latest_y['date']}):")
            print(f"    DFII10: {target_y['value']} -> {latest_y['value']}  ({y_chg_bp:+.0f}bp)")
            print(f"    Gold (GC=F): ${gold_then:,.2f} -> ${gold_now:,.2f}  ({gold_chg_pct:+.1f}%)")
            print(f"    State: {divergence_state}")
        except Exception as e:
            failures.append(f"divergence-calc: {e}")
            print(f"\n  ERROR divergence classifier FAILED: {e}", file=sys.stderr)
    else:
        failures.append("divergence-calc: missing real-yield or gold leg")

    # --- 6. LME copper stocks (I1 inventory leg — westmetall scrape) ---
    lme_latest = None
    lme_drawdown_pct = None
    try:
        rows, lme_latest, lme_oldest = read_lme_copper_stocks()
        peak = max(rows, key=lambda t: t[1])
        lme_drawdown_pct = (lme_latest[1] - peak[1]) / peak[1] * 100
        ytd_pct = (lme_latest[1] - lme_oldest[1]) / lme_oldest[1] * 100
        print(f"\n  LME COPPER STOCKS (westmetall.com scrape, LME data, business-daily):")
        print(f"    Latest: {lme_latest[1]:,} t  [{lme_latest[0]}]")
        print(f"    Table span: {lme_oldest[0]} ({lme_oldest[1]:,} t) -> latest  ({ytd_pct:+.1f}% over span)")
        print(f"    Span peak: {peak[1]:,} t [{peak[0]}]  (latest = {lme_drawdown_pct:+.1f}% vs peak)")
    except Exception as e:
        failures.append(f"LME-stocks: {e}")
        print(f"\n  ERROR LME copper stocks scrape FAILED: {e}", file=sys.stderr)

    print(f"\n  NOTE: CFTC COT (weekly cadence) and copper-vs-200dma (I1) are NOT wired "
          f"into this script — documented gaps, see file header + STATUS.md.")

    # --- Verdict (always printed; failed legs say so, never fabricated) ---
    y_s = f"DFII10 {latest_y['value']} [{latest_y['date']}]" if latest_y else "real-yield FETCH-FAIL"
    g_s = (f"gold ${fut['GC=F']['price']:,.2f}" if fut and "error" not in fut.get("GC=F", {"error": 1}) else "gold FETCH-FAIL")
    gsr_s = f"GSR {gsr:.2f} ({gsr_band})" if gsr else "GSR FETCH-FAIL"
    div_s = divergence_state or "divergence FETCH-FAIL"
    lme_s = (f"LME Cu {lme_latest[1]:,}t [{lme_latest[0]}]" if lme_latest else "LME Cu FETCH-FAIL")
    print(f"\n  Metals leg: {y_s} · {g_s} · {gsr_s} · {lme_s} · M1: {div_s}\n")

    rc = 0
    if failures:
        print(f"  metals_watch.py: {len(failures)} leg(s) FAILED: {'; '.join(failures)}", file=sys.stderr)
        rc = 2
    elif gsr_band in ("YELLOW", "ORANGE", "RED") or (divergence_state and divergence_state.startswith("CONVERGE")):
        # CONVERGE flags REVIEW as the falsification direction of M1 v1's premium
        # claim. Under M1 v2 (2026-07-12 re-derivation, THESIS.md) CONVERGE is the
        # EXPECTED state (cyclical layer re-coupled to real rates) — the flag stays
        # deliberately: it keeps the operator eyeballing the divergence state each
        # boot until v2 survives its first catalyst tests (MIDAS-03/04). Revisit
        # after those resolve: if v2 holds, CONVERGE should become the quiet state
        # and DIVERGE (premium reassertion) should become the REVIEW trigger.
        rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main())
