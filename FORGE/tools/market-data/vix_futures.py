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
COMPLACENCY_THRESHOLD = 8.99
ROLL_WINDOW_DAYS = 5


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
        if pct < 0:
            return "BACKWARDATION"
        if pct < AVG_STEEPNESS:
            return "BELOW_AVG"
        if pct < COMPLACENCY_THRESHOLD:
            return "NORMAL_TO_ELEVATED"
        return "COMPLACENCY_TOP_30PCT"

    return {
        "as_of": as_of.isoformat(),
        "strict": {
            "front": m1,
            "back": m2,
            "steepness_pct": round(strict, 3),
            "m1_days_to_expiry": m1_dte,
            "classification": classify(strict),
        },
        "adjusted": {
            "front": adjusted_front,
            "back": adjusted_back,
            "steepness_pct": round(adjusted, 3),
            "classification": classify(adjusted),
            "reason": adjusted_reason,
        },
        "thresholds": {
            "historical_avg": AVG_STEEPNESS,
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
    parser.add_argument("--date", help="Settlement date YYYY-MM-DD (default: yesterday)")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of human summary")
    args = parser.parse_args(argv)

    query_date = (
        datetime.strptime(args.date, "%Y-%m-%d").date() if args.date else date.today() - timedelta(days=1)
    )

    contracts = fetch_settlement(query_date)
    if not contracts:
        print(f"No VX standard monthly settlements for {query_date}", file=sys.stderr)
        return 1

    result = compute_steepness(contracts, as_of=query_date)

    if args.json:
        print(json.dumps(_serialize(result), indent=2))
        return 0

    s = result["strict"]
    a = result["adjusted"]
    print(f"VIX M1:M2 Contango Steepness — settlement {result['as_of']}")
    print(f"  Historical avg: {AVG_STEEPNESS}%  |  Complacency threshold: >{COMPLACENCY_THRESHOLD}%")
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
