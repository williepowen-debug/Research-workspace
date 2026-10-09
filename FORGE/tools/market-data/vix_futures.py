"""VIX futures M1/M2 contango steepness fetcher.

Pulls daily settlement from CBOE's public CSV endpoint, filters to standard monthly
contracts (ignores weeklies), and computes M1:M2 contango steepness:

    steepness_pct = (M2 - M1) / M1 * 100

Classification bands (per VIOLET KB-VIO-025, source: research article Apr 15):
    < 5.6%         — below historical average
    5.6% - 8.99%   — normal-to-elevated
    > 8.99%        — top 30th percentile complacency (reversal-vulnerable)

Roll handling: when M1 has <5 calendar days to expiration, it has converged to spot
and understates M1/M2 dispersion. The tool reports both:
    - Strict (M1, M2)          — nearest two standard monthlies
    - Roll-adjusted (M_eff, next) — skip M1 if <5 days to expiry

CLI:
    python3 vix_futures.py [--date YYYY-MM-DD]

With no --date, resolves to the most recent session that actually HAS settlements
(probes backwards up to MAX_SETTLEMENT_LOOKBACK_DAYS), so Mondays and post-holiday
sessions work. An explicit --date is honoured exactly and fails loudly. Either way
the returned `as_of` is the settlement's OWN date — always read it rather than
assuming today or T-1.
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import sys
from datetime import date, datetime, timedelta

import requests

CBOE_SETTLEMENT_URL = "https://www.cboe.com/us/futures/market_statistics/settlement/csv/"
AVG_STEEPNESS = 5.6
# Basis + vintage (DOCKET L441, VIOLET KB-VIO-310): re-measured 2026-09-24 on VIOLET
# workbook/VX_TERM_HISTORY.tsv — CBOE settles, standard monthlies, roll-adjusted (front skipped at
# <=5d to expiry), n=3,324 sessions 2013-05-20 -> 2026-08-03: mean 5.41 / median 5.84 (p70 8.22,
# p90 12.0). 5.6 sits between mean and median; kept. VIOLET owns the recompute rule (each quarterly
# VIX expiry; replace with the median rounded to 0.1 if |delta| > 0.5pp) and re-stamps the vintage.
# Past AVG_STEEPNESS_RECHECK_BY with no re-stamp the classification prints UNVERIFIED (fail-closed).
AVG_STEEPNESS_VINTAGE = "2026-09-24"
AVG_STEEPNESS_RECHECK_BY = "2026-12-16"


def avg_steepness_status(today: "date | None" = None) -> str:
    """OK while the vintage is inside its re-check window; UNVERIFIED once past it (L441 class)."""
    today = today or date.today()
    return "OK" if today.isoformat() <= AVG_STEEPNESS_RECHECK_BY else "UNVERIFIED"


def _label(cls: str) -> str:
    return cls if avg_steepness_status() == "OK" else f"{cls} UNVERIFIED"
COMPLACENCY_THRESHOLD = 8.99
ROLL_WINDOW_DAYS = 5

# How far back the no-`--date` default will probe for a real settlement.
# 7 covers a three-day weekend plus an adjacent holiday.
MAX_SETTLEMENT_LOOKBACK_DAYS = 7


def _is_standard_monthly(symbol: str) -> bool:
    """CBOE VX symbols: VX/J6 (standard monthly) vs VX16/J6, VX17/J6 (weeklies).
    Standard = no digits between 'VX' and '/'."""
    if not symbol.startswith("VX/"):
        return False
    prefix = symbol.split("/")[0]
    return prefix == "VX"


def fetch_settlement(query_date: date) -> list[dict]:
    """Return list of {symbol, expiration, price} dicts for VX standard monthlies."""
    resp = requests.get(
        CBOE_SETTLEMENT_URL,
        params={"dt": query_date.isoformat()},
        headers={"User-Agent": "Mozilla/5.0", "Referer": "https://www.cboe.com/"},
        timeout=15,
    )
    resp.raise_for_status()
    reader = csv.DictReader(io.StringIO(resp.text))
    rows = []
    for row in reader:
        if row["Product"] != "VX":
            continue
        if not _is_standard_monthly(row["Symbol"]):
            continue
        rows.append(
            {
                "symbol": row["Symbol"],
                "expiration": datetime.strptime(row["Expiration Date"], "%Y-%m-%d").date(),
                "price": float(row["Price"]),
            }
        )
    rows.sort(key=lambda r: r["expiration"])
    return rows


def resolve_latest_settlement(
    start: date, max_lookback: int = MAX_SETTLEMENT_LOOKBACK_DAYS
) -> tuple[date | None, list[dict]]:
    """Walk back from `start` to the most recent date that actually HAS settlements.

    Replaces a fixed `date.today() - timedelta(days=1)` default — one CALENDAR day —
    which landed on SUNDAY every Monday and on a holiday after every long weekend,
    making the tool exit 1 with "No VX standard monthly settlements". That is how
    VIOLET's M1:M2 front-curve column went blank on 8 of the last 12 Mondays
    (KB-VIO-130): the caller saw the failure and wrote an empty cell, silently, for
    two months. A calendar-day offset cannot express "the last trading session".

    Probing is the honest form of the question. It handles weekends AND market
    holidays without needing a holiday calendar, because **the presence of data is
    the test** — no calendar can be wrong about a settlement that exists. It also
    means a post-settle run resolves SAME-DAY instead of always being T-1.

    Returns (settlement_date, contracts), or (None, []) if nothing in the window.
    """
    for back in range(max_lookback + 1):
        d = start - timedelta(days=back)
        try:
            contracts = fetch_settlement(d)
        except requests.RequestException:
            continue  # transient/404 for that day — keep walking, don't abort
        if contracts:
            return d, contracts
    return None, []


def compute_steepness(contracts: list[dict], as_of: date) -> dict:
    """Compute M1/M2 contango metrics from a sorted list of standard monthly contracts.

    as_of: the date we're evaluating from (typically settlement_date). Contracts with
    expiration <= as_of are treated as expired and dropped.
    """
    live = [c for c in contracts if c["expiration"] > as_of]
    if len(live) < 2:
        raise ValueError(f"Need >=2 live contracts, got {len(live)}")

    m1, m2 = live[0], live[1]
    m1_dte = (m1["expiration"] - as_of).days
    strict = (m2["price"] - m1["price"]) / m1["price"] * 100

    # Roll-adjusted: if M1 within roll window, shift to (M2, M3)
    if m1_dte < ROLL_WINDOW_DAYS and len(live) >= 3:
        m3 = live[2]
        adjusted_front, adjusted_back = m2, m3
        adjusted = (m3["price"] - m2["price"]) / m2["price"] * 100
        adjusted_reason = f"M1 has {m1_dte}d to expiry (<{ROLL_WINDOW_DAYS}d), using M2/M3"
    else:
        adjusted_front, adjusted_back = m1, m2
        adjusted = strict
        adjusted_reason = "no roll adjustment needed"

    def classify(pct: float) -> str:
        # Callers pass the SAME 3-dp value the JSON publishes (L546, 2026-10-08): the unrounded
        # ratio×100 mis-landed 8 of 8 reachable exact-5.6% pairs ((13.20-12.50)/12.50*100 =
        # 5.599999999999994 → BELOW_AVG at exactly average), so label and number disagreed.
        if pct < 0:
            return "BACKWARDATION"
        if pct < AVG_STEEPNESS:
            return _label("BELOW_AVG")
        if pct < COMPLACENCY_THRESHOLD:
            return _label("NORMAL_TO_ELEVATED")
        return _label("COMPLACENCY_TOP_30PCT")

    return {
        "as_of": as_of.isoformat(),
        "strict": {
            "front": m1,
            "back": m2,
            "steepness_pct": round(strict, 3),
            "m1_days_to_expiry": m1_dte,
            "classification": classify(round(strict, 3)),  # L546: label the 3-dp value published above
        },
        "adjusted": {
            "front": adjusted_front,
            "back": adjusted_back,
            "steepness_pct": round(adjusted, 3),
            "classification": classify(round(adjusted, 3)),  # L546: same rounded value as steepness_pct
            "reason": adjusted_reason,
        },
        "thresholds": {
            "historical_avg": AVG_STEEPNESS,
            "historical_avg_vintage": AVG_STEEPNESS_VINTAGE,
            "historical_avg_recheck_by": AVG_STEEPNESS_RECHECK_BY,
            "historical_avg_status": avg_steepness_status(),
            "complacency_top30": COMPLACENCY_THRESHOLD,
        },
    }


def _serialize(result: dict) -> dict:
    """Convert date/contract objects to JSON-safe primitives."""
    def fix_contract(c):
        return {"symbol": c["symbol"], "expiration": c["expiration"].isoformat(), "price": c["price"]}

    out = dict(result)
    for band in ("strict", "adjusted"):
        b = dict(out[band])
        b["front"] = fix_contract(b["front"])
        b["back"] = fix_contract(b["back"])
        out[band] = b
    return out


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--date",
        help="Settlement date YYYY-MM-DD (default: most recent session that has settlements)",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of human summary")
    args = parser.parse_args(argv)

    if args.date:
        # An explicit date is a PRECISE request — honour it exactly and fail loudly
        # if that session has no settlements. Never silently substitute a
        # neighbouring day: a caller naming a date is usually reconciling a record
        # against it, and a quietly-shifted as_of is the bug class this tool already
        # caused once (KB-VIO-092, the T-1-stamped-as-same-day misread).
        query_date = datetime.strptime(args.date, "%Y-%m-%d").date()
        contracts = fetch_settlement(query_date)
    else:
        query_date, contracts = resolve_latest_settlement(date.today())

    if not contracts:
        target = (
            args.date
            if args.date
            else f"any of the {MAX_SETTLEMENT_LOOKBACK_DAYS} days to {date.today()}"
        )
        print(f"No VX standard monthly settlements for {target}", file=sys.stderr)
        return 1

    result = compute_steepness(contracts, as_of=query_date)

    if args.json:
        print(json.dumps(_serialize(result), indent=2))
        return 0

    s = result["strict"]
    a = result["adjusted"]
    print(f"VIX M1:M2 Contango Steepness — settlement {result['as_of']}")
    print(f"  Historical avg: {AVG_STEEPNESS}% (vintage {AVG_STEEPNESS_VINTAGE}, re-check {AVG_STEEPNESS_RECHECK_BY}, {avg_steepness_status()})  |  Complacency threshold: >{COMPLACENCY_THRESHOLD}%")
    print()
    print(f"  Strict (nearest 2 monthlies):")
    print(f"    M1 {s['front']['symbol']} exp {s['front']['expiration']} = {s['front']['price']:.4f}  ({s['m1_days_to_expiry']}d to expiry)")
    print(f"    M2 {s['back']['symbol']} exp {s['back']['expiration']} = {s['back']['price']:.4f}")
    print(f"    Steepness: {s['steepness_pct']:+.2f}%  [{s['classification']}]")
    print()
    print(f"  Roll-adjusted:")
    print(f"    {a['reason']}")
    print(f"    Front {a['front']['symbol']} = {a['front']['price']:.4f}  |  Back {a['back']['symbol']} = {a['back']['price']:.4f}")
    print(f"    Steepness: {a['steepness_pct']:+.2f}%  [{a['classification']}]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
