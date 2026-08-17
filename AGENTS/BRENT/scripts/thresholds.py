#!/usr/bin/env python3
"""
BRENT Threshold Monitor
Pulls live oil/energy market prices (yfinance) and economic data (FRED) and
compares against BRENT's two-phase oil thesis thresholds.

CANONICAL MACHINE STATE = `workbook/REGISTRY.tsv` — this script READS it (see the
consolidation note ~L68) and holds NO threshold table of its own.
CANONICAL PROSE = `thesis/THESIS.md` § KEY THRESHOLDS — meaning and rationale, no live state.
They may disagree only in wording, never in a number.

⛔ THIS DOCSTRING SAID THE OPPOSITE UNTIL 2026-08-04 (session 4). It read "CANONICAL
THRESHOLD REGISTRY = thesis/THESIS.md ... THESIS WINS on any disagreement with the tables
below — they are a RESTATEMENT, and a restatement rots." Correct when written; stale the
moment the RAV pilot deleted those tables and moved the machine home here — so the file
carried TWO CONTRADICTORY OWNERSHIP DECLARATIONS, this one and the L78 note, for a day.
It also referred readers to "the tables below," which no longer exist.
(Earlier history, retained: the pre-7/28 header credited `workbook/VX.tsv`, FROZEN since
2026-06-14 — that mis-citation is how two retired v4 Brent rows survived to 7/28.)
★ THE PATTERN, THREE TIMES IN THIS ONE DOCSTRING: the ownership claim is the LAST thing
updated when ownership moves, because the refactor changes the CODE and the claim lives
in a comment nothing executes.

Color key:
  BREACHED  = threshold crossed
  WARNING   = within 5% of threshold

Classifications:
  risk    (🔴) = price moving bad for thesis (demand destruction, stop hit)
  thesis  (🟢) = price confirming thesis (squeeze intensifying)
  stress  (🟠) = structural stress level (not directional)

Usage:
  .venv/bin/python3 AGENTS/BRENT/scripts/thresholds.py
  .venv/bin/python3 AGENTS/BRENT/scripts/thresholds.py --json
"""

import json
import os
import sys
import urllib.request
import urllib.parse
from datetime import datetime

try:
    import yfinance as yf
except ImportError:
    print("  ERROR: yfinance not installed.")
    sys.exit(1)

# ---------------------------------------------------------------------------
# FRED config (same key as CARL)
# ---------------------------------------------------------------------------

def _fred_key():
    """Env first, else the gitignored FORGE market-data .env (single per-machine home).
    Hardcoded copies scrubbed 2026-07-01 (public-prep) — never hardcode this key."""
    import pathlib, sys
    k = os.environ.get("FRED_API_KEY", "")
    if k:
        return k
    p = pathlib.Path(__file__).resolve().parents[3] / "FORGE/tools/market-data/.env"
    if p.exists():
        for line in p.read_text().splitlines():
            if line.startswith("FRED_API_KEY="):
                return line.split("=", 1)[1].strip()
    # ⚠️ STDOUT, not stderr: boot.py only surfaces stderr when rc != 0, so a stderr-only
    # warning here was deleted on every clean run — the board rendered green with every
    # FRED threshold silently absent. (DAEDALUS SFG sweep 2026-08-17; verified same day.)
    # Suppressed in --json mode only, where a bare line would corrupt the payload.
    if "--json" not in sys.argv:
        print("  ⚠️  FRED_API_KEY not found (env or FORGE/tools/market-data/.env) "
              "— every FRED threshold below will be UNGRADED, not un-breached")
    return ""

FRED_API_KEY = _fred_key()
FRED_BASE = "https://api.stlouisfed.org/fred/series/observations"

# ---------------------------------------------------------------------------
# Market thresholds (yfinance)
# (ticker, direction, level, classification, label)
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# ⚑ CONSOLIDATION 2026-08-04 (Will-approved, on RAV's ruling): the hardcoded
# MARKET_THRESHOLDS / FRED_THRESHOLDS tables that used to live here are GONE.
# Both are now READ from workbook/REGISTRY.tsv, the single machine home for a
# test's level AND its instrument.
#
# This closes the standing TODO that sat at this exact spot ("scripts should
# READ that registry, not restate it — instance n=2 fleet-wide of the
# registry-restatement class"). The restatement had already rotted twice into
# alerting in the WRONG DIRECTION on retired v4 framing.
#
# THESIS.md remains canonical PROSE. REGISTRY.tsv is canonical MACHINE state.
# They may disagree only in wording, never in a number.
# ---------------------------------------------------------------------------

import csv as _csv
from pathlib import Path as _Path

_REGISTRY = _Path(__file__).resolve().parent.parent / "workbook" / "REGISTRY.tsv"


def _load_registry():
    if not _REGISTRY.exists():
        print(f"  ERROR: registry missing at {_REGISTRY} — thresholds cannot be graded", file=sys.stderr)
        sys.exit(1)
    lines = [l for l in _REGISTRY.read_text(encoding="utf-8").splitlines()
             if l.strip() and not l.startswith("#")]
    return [r for r in _csv.DictReader(lines, delimiter="\t") if r.get("test_id")]


def _levels(source):
    """Live, gradeable level rows for one source. Blank level = instrument-only row, skipped."""
    out = []
    for r in _load_registry():
        if r["status"] != "live" or r["source"] != source or not r["level"]:
            continue
        out.append(r)
    return out


# Shapes preserved EXACTLY so the rest of this script is untouched by the move.
MARKET_THRESHOLDS = [(r["symbol"], r["direction"], float(r["level"]), r["classification"], r["label"])
                     for r in _levels("yf")]
FRED_THRESHOLDS = [(r["symbol"], r["series_label"], r["direction"], float(r["level"]),
                    r["classification"], r["label"]) for r in _levels("fred")]

CONTEXT_TICKERS = ["BZ=F", "CL=F", "USO", "STNG", "LNG", "VG", "XLE", "XOP", "VLO", "MPC",
                   "NG=F", "UNG", "FRO", "EURN", "DHT", "HAL", "SLB", "CVX", "XOM", "^VIX"]

# ---------------------------------------------------------------------------
# FRED thresholds
# (series_id, label, direction, level, classification, threshold_label)
# ---------------------------------------------------------------------------

# ⛔⛔ THE HARDCODED `FRED_THRESHOLDS` LITERAL THAT STOOD HERE WAS DELETED 2026-08-17.
#
# WHY, and it is a defect this script hid from itself: this file assigned `FRED_THRESHOLDS`
# TWICE — once above (line ~127) from REGISTRY.tsv via `_levels("fred")`, and again HERE to a
# hardcoded literal. Python takes the SECOND binding, so the registry-derived list was built
# and then silently discarded, and `check_fred_thresholds` iterated the literal.
#
# THREE CONSEQUENCES (found by DAEDALUS's reader during the Will-directed structure review,
# 2026-08-17; independently verified here before deleting):
#   (1) REGISTRY.tsv was NOT the machine home for FRED rows, despite the module docstring and
#       the header comment above both asserting the hardcoded tables were gone. The RAV
#       state-replacement pilot moved MARKET rows and left this one behind.
#   (2) The 2026-08-12 audit-convention relabel (F-2: declare BASIS + UNIT in the label)
#       reached the REGISTRY and never reached the BOARD. Verified: 3 Dated Brent rows read
#       "Dated Brent >$140 — extreme (ATH $144)" on the board while the registry carried
#       "Dated Brent PHYSICAL SPOT (FRED DCOILBRENTEU) >$140 USD/bbl". Five days of a
#       ratified relabel that no reader of the board could see.
#   (3) IT PUNCHED A HOLE IN THE SAME-DAY false-green fix (97bbef457). That fix guarantees
#       every threshold in the ITERATED list is either graded or reported UNGRADED — but a
#       FRED row registered in REGISTRY.tsv tomorrow would never ENTER the iterated list, so
#       it would be absent from the board AND absent from `ungraded`. The identical
#       false-green, one layer up, inside the repair for it.
#
# SAFE TO DELETE, VERIFIED BEFORE DOING IT, NOT ASSUMED: the two lists were compared row by
# row — 10 vs 10, IDENTICAL on (symbol, direction, level), so NO level changes and nothing
# was mis-graded while the literal stood. The only differences were the 3 labels in (2),
# where the registry text is the CORRECT post-F-2 wording. Deleting therefore fixes the
# labels and changes no graded state.
#
# supersedes: the hardcoded FRED table. REGISTRY.tsv is now the machine home in FACT and not
# only in the docstring — `FRED_THRESHOLDS` is built once, at line ~127, from `_levels("fred")`.
#
# ⚠️ THE ONE PIECE OF DATED REASONING THAT LIVED IN THE DELETED LITERAL, PRESERVED VERBATIM
# BECAUSE IT IS A RULING AND NOT A COMMENT (it governs the Dated Brent >$100 row's DIRECTION,
# and the registry row carries the level but not the argument):
#
#   ⚠️ v5.1 CORRECTION (2026-07-28) — third instance of the registry-restatement class, and
#   the only one that was FIRING. This row read: below $100 = "risk" / "physical squeeze
#   resolving". Two defects:
#     (1) It infers PHYSICAL tightness from FLAT PRICE — the exact inversion of v5.1's
#         central finding. Crude fell −15.6% off the 7/23 high with ZERO barrels returned,
#         Hormuz at 8% of pre-war and war-risk at cycle highs. Flat price is NOT the clean
#         instrument for physical tightness; CRACKS/DIESEL and transits are.
#     (2) Dated Brent has been under $100 nearly always, so it fired every boot = alert
#         fatigue, no signal. Below $100 is the BASELINE, not a breach.
#   Kept as thesis-class context in the CORRECT direction only; no physical claim asserted.

# Context FRED series (display only)
CONTEXT_FRED = [
    ("DCOILBRENTEU", "Dated Brent"),
    ("DCOILWTICO",   "WTI Spot"),
    ("BAMLH0A0HYM2", "HY Total OAS (%)"),
    ("DHHNGSP",      "Henry Hub Gas"),
    ("GASREGW",      "US Retail Gas"),
]

WARN_PCT = 0.05  # 5% proximity warning

# ---------------------------------------------------------------------------
# FRED fetcher (urllib)
# ---------------------------------------------------------------------------

def fred_fetch(series_id, limit=3):
    """Fetch latest observations from FRED. Returns list of {date, value}."""
    params = {
        "series_id": series_id,
        "api_key": FRED_API_KEY,
        "file_type": "json",
        "sort_order": "desc",
        "limit": limit,
    }
    url = f"{FRED_BASE}?{urllib.parse.urlencode(params)}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "BRENT-Monitor/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
        obs = data.get("observations", [])
        return [{"date": o["date"], "value": o["value"]} for o in obs if o["value"] != "."]
    except Exception as e:
        return [{"error": str(e)}]


# ---------------------------------------------------------------------------
# Market price fetcher (yfinance)
# ---------------------------------------------------------------------------

def get_prices(symbols):
    """Fetch current prices. Returns dict symbol -> {price, prev, chg}."""
    prices = {}
    try:
        tickers = yf.Tickers(" ".join(symbols))
        for sym in symbols:
            try:
                info = tickers.tickers[sym].info
                price = info.get("regularMarketPrice") or info.get("previousClose")
                prev = info.get("previousClose") or info.get("regularMarketPreviousClose")
                if price:
                    chg = ((price - prev) / prev * 100) if prev else 0
                    prices[sym] = {"price": price, "prev": prev, "chg": chg}
            except Exception:
                pass
    except Exception as e:
        print(f"  ERROR fetching prices: {e}")
    return prices


# ---------------------------------------------------------------------------
# Threshold checking
# ---------------------------------------------------------------------------

def check_market_thresholds(prices):
    results = []
    ungraded = []
    warning_candidates = {}

    for ticker, direction, level, clas, label in MARKET_THRESHOLDS:
        p = prices.get(ticker)
        if not p:
            # ⚠️ NOT a silent skip: an un-fetched threshold is UNGRADED, never un-breached.
            ungraded.append({"ticker": ticker, "label": label, "class": clas,
                             "source": "market",
                             "reason": "no price returned (fetch failed, or symbol dead)"})
            continue
        price = p["price"]
        dist = (price - level) / level * 100

        if direction == "above":
            if price > level:
                results.append({"ticker": ticker, "level": level, "label": label,
                                "class": clas, "status": "BREACHED", "price": price,
                                "dist": dist, "direction": direction, "source": "market"})
            elif price > level * (1 - WARN_PCT):
                cand = {"ticker": ticker, "level": level, "label": label,
                        "class": clas, "status": "WARNING", "price": price,
                        "dist": dist, "direction": direction, "source": "market"}
                key = (ticker, direction)
                if key not in warning_candidates or abs(dist) < abs(warning_candidates[key]["dist"]):
                    warning_candidates[key] = cand
        else:
            if price < level:
                results.append({"ticker": ticker, "level": level, "label": label,
                                "class": clas, "status": "BREACHED", "price": price,
                                "dist": dist, "direction": direction, "source": "market"})
            elif price < level * (1 + WARN_PCT):
                cand = {"ticker": ticker, "level": level, "label": label,
                        "class": clas, "status": "WARNING", "price": price,
                        "dist": dist, "direction": direction, "source": "market"}
                key = (ticker, direction)
                if key not in warning_candidates or abs(dist) < abs(warning_candidates[key]["dist"]):
                    warning_candidates[key] = cand

    results.extend(warning_candidates.values())
    return results, ungraded


def check_fred_thresholds(fred_data):
    results = []
    ungraded = []
    warning_candidates = {}

    for series_id, label, direction, level, clas, thresh_label in FRED_THRESHOLDS:
        obs = fred_data.get(series_id, [])
        if not obs or "error" in obs[0]:
            # ⚠️ NOT a silent skip. This `continue` used to drop the row entirely, so a dead
            # FRED key or a transient SSL timeout removed the threshold from the board with
            # no signal at all. Near-miss 2026-08-17: instrument_check flagged FRED-GASREGW
            # DEAD on SSL timeout while this script graded it fine in the same boot.
            reason = (str(obs[0].get("error", "no data"))[:70] if obs else "no data returned")
            ungraded.append({"ticker": series_id, "label": thresh_label, "class": clas,
                             "source": "fred", "reason": reason})
            continue
        try:
            value = float(obs[0]["value"])
        except (ValueError, KeyError):
            ungraded.append({"ticker": series_id, "label": thresh_label, "class": clas,
                             "source": "fred",
                             "reason": f"unparseable value: {obs[0].get('value', '<missing>')!r}"})
            continue

        dist = (value - level) / level * 100

        if direction == "above":
            if value > level:
                results.append({"ticker": series_id, "level": level, "label": thresh_label,
                                "class": clas, "status": "BREACHED", "price": value,
                                "dist": dist, "direction": direction, "source": "fred",
                                "date": obs[0]["date"], "series_label": label})
            elif value > level * (1 - WARN_PCT):
                cand = {"ticker": series_id, "level": level, "label": thresh_label,
                        "class": clas, "status": "WARNING", "price": value,
                        "dist": dist, "direction": direction, "source": "fred",
                        "date": obs[0]["date"], "series_label": label}
                key = (series_id, direction, level)
                if key not in warning_candidates or abs(dist) < abs(warning_candidates[key]["dist"]):
                    warning_candidates[key] = cand
        else:
            if value < level:
                results.append({"ticker": series_id, "level": level, "label": thresh_label,
                                "class": clas, "status": "BREACHED", "price": value,
                                "dist": dist, "direction": direction, "source": "fred",
                                "date": obs[0]["date"], "series_label": label})
            elif value < level * (1 + WARN_PCT):
                cand = {"ticker": series_id, "level": level, "label": thresh_label,
                        "class": clas, "status": "WARNING", "price": value,
                        "dist": dist, "direction": direction, "source": "fred",
                        "date": obs[0]["date"], "series_label": label}
                key = (series_id, direction, level)
                if key not in warning_candidates or abs(dist) < abs(warning_candidates[key]["dist"]):
                    warning_candidates[key] = cand

    results.extend(warning_candidates.values())
    return results, ungraded


# ---------------------------------------------------------------------------
# Display
# ---------------------------------------------------------------------------

def emoji_for(clas, status):
    if status == "BREACHED":
        return {"risk": "🔴", "thesis": "🟢", "stress": "🟠"}[clas]
    else:
        return {"risk": "⚠️ ", "thesis": "🟡", "stress": "🟠"}[clas]


def fmt_value(value):
    if abs(value) > 1000:
        return f"{value:,.0f}"
    if abs(value) > 10:
        return f"{value:.2f}"
    return f"{value:.3f}"


def print_alerts(alerts, header):
    if not alerts:
        return
    print(f"\n  {header}")
    print(f"  {'-'*64}")
    for a in alerts:
        e = emoji_for(a["class"], a["status"])
        val_str = fmt_value(a["price"])
        lev_str = fmt_value(a["level"])
        src = f" ({a['date']})" if a.get("date") else ""
        print(f"  {e} {a['ticker']:<16} {val_str:>12}  (level {lev_str}, {a['dist']:+.1f}%){src}")
        print(f"              {a['label']}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    json_mode = "--json" in sys.argv
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Collect all market symbols
    threshold_syms = list(set(t[0] for t in MARKET_THRESHOLDS))
    all_syms = list(set(threshold_syms + CONTEXT_TICKERS))

    if not json_mode:
        print(f"\n{'='*72}")
        print(f"  BRENT Threshold Monitor — {now}")
        print(f"{'='*72}")

    # Market
    if not json_mode:
        print(f"\n  Fetching market data...", flush=True)
    prices = get_prices(all_syms)

    # FRED
    if not json_mode:
        print(f"  Fetching FRED data...", flush=True)
    fred_series = list(set([t[0] for t in FRED_THRESHOLDS] + [s[0] for s in CONTEXT_FRED]))
    fred_data = {}
    for sid in fred_series:
        fred_data[sid] = fred_fetch(sid, limit=3)

    # Check thresholds
    market_alerts, market_ungraded = check_market_thresholds(prices)
    fred_alerts, fred_ungraded = check_fred_thresholds(fred_data)
    all_alerts = market_alerts + fred_alerts
    ungraded = market_ungraded + fred_ungraded

    if json_mode:
        output = {
            "timestamp": now,
            "alerts": all_alerts,
            "ungraded": ungraded,
            "prices": {s: prices[s] for s in sorted(prices)},
            "fred": {s: fred_data[s] for s in sorted(fred_data)},
        }
        print(json.dumps(output, indent=2))
        return 2 if ungraded else 0

    # Display alerts
    breaches_risk = [a for a in all_alerts if a["status"] == "BREACHED" and a["class"] == "risk"]
    breaches_thesis = [a for a in all_alerts if a["status"] == "BREACHED" and a["class"] == "thesis"]
    breaches_stress = [a for a in all_alerts if a["status"] == "BREACHED" and a["class"] == "stress"]
    warnings = [a for a in all_alerts if a["status"] == "WARNING"]

    print_alerts(breaches_risk,   "🔴 RISK BREACHES (bad for thesis)")
    print_alerts(breaches_thesis, "🟢 THESIS CONFIRMING BREACHES")
    print_alerts(breaches_stress, "🟠 STRUCTURAL STRESS BREACHES")
    print_alerts(warnings,        "⚠️  NEAR THRESHOLDS (within 5%)")

    if not any([breaches_thesis, breaches_risk, breaches_stress, warnings]):
        print(f"\n  ✅ No threshold breaches or warnings.")

    # Crude / futures snapshot
    print(f"\n  CRUDE & FUTURES")
    print(f"  {'-'*64}")
    crude_display = [
        ("BZ=F", "Brent futures"),
        ("CL=F", "WTI futures"),
        ("NG=F", "Natgas futures"),
    ]
    for sym, label in crude_display:
        p = prices.get(sym)
        if p:
            arrow = "🟢" if p["chg"] >= 0 else "🔴"
            print(f"  {arrow} {label:<22} ${p['price']:>8.2f}  ({p['chg']:+.2f}%)")

    # Positions
    print(f"\n  POSITIONS")
    print(f"  {'-'*64}")
    pos_display = [
        ("USO", "USO (oil long)"),
        ("STNG", "STNG (tanker)"),
        ("LNG", "Cheniere"),
        ("VG", "Venture Global"),
    ]
    for sym, label in pos_display:
        p = prices.get(sym)
        if p:
            arrow = "🟢" if p["chg"] >= 0 else "🔴"
            print(f"  {arrow} {label:<22} ${p['price']:>8.2f}  ({p['chg']:+.2f}%)")

    # Energy sector
    print(f"\n  ENERGY SECTOR")
    print(f"  {'-'*64}")
    energy_display = [
        ("XLE", "Energy ETF"),
        ("XOP", "E&P ETF"),
        ("XOM", "Exxon"),
        ("CVX", "Chevron"),
        ("HAL", "Halliburton"),
        ("SLB", "Schlumberger"),
        ("VLO", "Valero (refiner)"),
        ("MPC", "Marathon (refiner)"),
    ]
    for sym, label in energy_display:
        p = prices.get(sym)
        if p:
            arrow = "🟢" if p["chg"] >= 0 else "🔴"
            print(f"  {arrow} {label:<22} ${p['price']:>8.2f}  ({p['chg']:+.2f}%)")

    # Tanker universe
    print(f"\n  TANKERS (proxy for VLCC/LR2/MR rates)")
    print(f"  {'-'*64}")
    tanker_display = [
        ("FRO",  "Frontline (VLCC)"),
        ("EURN", "Euronav (VLCC/Suezmax)"),
        ("DHT",  "DHT (VLCC pure)"),
        ("STNG", "Scorpio (product)"),
    ]
    for sym, label in tanker_display:
        p = prices.get(sym)
        if p:
            arrow = "🟢" if p["chg"] >= 0 else "🔴"
            print(f"  {arrow} {label:<22} ${p['price']:>8.2f}  ({p['chg']:+.2f}%)")

    # FRED snapshot
    print(f"\n  FRED LATEST VALUES")
    print(f"  {'-'*64}")
    for sid, label in CONTEXT_FRED:
        obs = fred_data.get(sid, [])
        if obs and "error" not in obs[0]:
            val = obs[0]["value"]
            date = obs[0]["date"]
            try:
                num = float(val)
                formatted = fmt_value(num)
            except ValueError:
                formatted = val
            prior_str = ""
            if len(obs) > 1:
                try:
                    prior = float(obs[1]["value"])
                    diff = num - prior
                    prior_str = f"  (prior {fmt_value(prior)}, {diff:+.2f})"
                except (ValueError, KeyError):
                    pass
            print(f"  {label:<26} {formatted:>10}  as of {date}{prior_str}")
        else:
            err = obs[0].get("error", "no data") if obs else "no data"
            print(f"  {label:<26} {'ERROR':>10}  {err[:50]}")

    # Macro context
    print(f"\n  MACRO CONTEXT")
    print(f"  {'-'*64}")
    p = prices.get("^VIX")
    if p:
        arrow = "🔴" if p["chg"] >= 0 else "🟢"  # rising VIX = risk-off
        print(f"  {arrow} {'VIX':<10} {p['price']:>10.2f}  ({p['chg']:+.2f}%)")

    # ⚠️ UNGRADED — the whole point of the 2026-08-17 fix. An un-fetched threshold used to
    # vanish from this board with no signal; absence read identically to "not breached".
    if ungraded:
        print(f"\n  ⚠️  UNGRADED — {len(ungraded)} registered threshold(s) COULD NOT BE GRADED")
        print(f"  {'-'*64}")
        for u in ungraded:
            print(f"      ⚠️  {u['ticker']:<20} [{u['source']:<6}] {str(u['label'])[:40]}")
            print(f"          reason: {u['reason']}")
        print("      ⛔ These are NOT known to be un-breached — they were never evaluated.")
        print("         A clean board above is clean ONLY over the thresholds that graded.")

    print()
    # rc=2 == FINDINGS in boot.py's tri-state (same convention as instrument_check.py):
    # the script RAN fine, but a registered test could not be evaluated. Previously this
    # was an unconditional `return 0`, so no failure inside this script could ever reach
    # boot's status line. supersedes: none (EXTENDS the existing rc contract).
    return 2 if ungraded else 0


if __name__ == "__main__":
    sys.exit(main())
