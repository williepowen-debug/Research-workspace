"""Fetch Feb 2018 Volmageddon M1:M2 contango analog series.

Downloads CBOE historical VX futures contracts F18 (Jan), G18 (Feb), H18 (Mar),
J18 (Apr), aligns by trade date, and computes daily M1:M2 contango for the
Jan 2 → Feb 28 2018 window.

URL pattern (discovered via web search 6/1/2026):
    https://cdn.cboe.com/resources/futures/archive/volume-and-price/CFE_{CODE}{YY}_VX.csv

Output:
    workbook/FEB2018_VOLMAGEDDON_M1M2.csv

Notes:
    Month codes: F=Jan G=Feb H=Mar J=Apr K=May M=Jun N=Jul Q=Aug U=Sep V=Oct
                 X=Nov Z=Dec.
    First CSV line is a disclaimer; real header on line 2.
    Expiration day = last row of contract; the price 0 in non-settle columns
    on settlement day is normal.
"""
from __future__ import annotations

import csv
import io
import sys
from datetime import date, datetime
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
OUT_CSV = ROOT / "workbook" / "FEB2018_VOLMAGEDDON_M1M2.csv"

CONTRACTS = [
    ("F18", date(2018, 1, 17)),   # expires Wed Jan 17 2018
    ("G18", date(2018, 2, 14)),   # expires Wed Feb 14 2018  <-- the Volmageddon M1
    ("H18", date(2018, 3, 21)),   # expires Wed Mar 21 2018
    ("J18", date(2018, 4, 18)),   # expires Wed Apr 18 2018
]


def fetch_contract(code: str) -> list[dict]:
    url = f"https://cdn.cboe.com/resources/futures/archive/volume-and-price/CFE_{code}_VX.csv"
    print(f"  fetching {code}…", end="", flush=True)
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=15)
    r.raise_for_status()
    lines = r.text.splitlines()
    # Skip disclaimer (first line), keep header + data
    csv_body = "\n".join(lines[1:])
    reader = csv.DictReader(io.StringIO(csv_body))
    rows = []
    for r_ in reader:
        try:
            td = datetime.strptime(r_["Trade Date"], "%m/%d/%Y").date()
            settle = float(r_["Settle"])
            rows.append({"date": td, "settle": settle})
        except (ValueError, KeyError):
            continue
    print(f" {len(rows)} rows")
    return rows


def main() -> None:
    contracts = {}
    print("CBOE 2018 contract fetch:")
    for code, expiry in CONTRACTS:
        rows = fetch_contract(code)
        contracts[code] = {"expiry": expiry, "data": {r["date"]: r["settle"] for r in rows}}

    # Build the unified date grid from all contracts
    all_dates = sorted(set().union(*(set(c["data"].keys()) for c in contracts.values())))
    # Filter to Jan 2 → Feb 28 2018 window
    window_start = date(2018, 1, 2)
    window_end = date(2018, 2, 28)
    dates = [d for d in all_dates if window_start <= d <= window_end]

    out_rows = []
    print(f"\nComputing M1:M2 for {len(dates)} trade dates in window:")
    for d in dates:
        # M1 = nearest non-expired contract on date d; M2 = next one
        live = [(code, c) for code, c in contracts.items() if c["expiry"] >= d and d in c["data"]]
        live.sort(key=lambda x: x[1]["expiry"])
        if len(live) < 2:
            continue
        m1_code, m1 = live[0]
        m2_code, m2 = live[1]
        m1_px = m1["data"][d]
        m2_px = m2["data"][d]
        if m1_px <= 0:
            continue
        contango_pct = (m2_px - m1_px) / m1_px * 100.0
        dte_m1 = (m1["expiry"] - d).days
        out_rows.append({
            "date": d.isoformat(),
            "m1_code": m1_code,
            "m1_settle": round(m1_px, 4),
            "m2_code": m2_code,
            "m2_settle": round(m2_px, 4),
            "m1m2_pct": round(contango_pct, 4),
            "m1_dte": dte_m1,
        })

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_CSV, "w") as f:
        w = csv.DictWriter(f, fieldnames=list(out_rows[0].keys()))
        w.writeheader()
        w.writerows(out_rows)

    print(f"\n  Written: {OUT_CSV.relative_to(ROOT.parent.parent)}")
    print(f"  Rows: {len(out_rows)}")

    # Print summary
    pcts = [r["m1m2_pct"] for r in out_rows]
    print()
    print("=" * 70)
    print(f"  Volmageddon M1:M2 contango — Jan 2 → Feb 28 2018")
    print("=" * 70)
    print(f"  Pre-spike (Jan 2 - Feb 2):")
    pre = [r for r in out_rows if r["date"] <= "2018-02-02"]
    if pre:
        ppcts = [r["m1m2_pct"] for r in pre]
        print(f"    n={len(pre)}  min={min(ppcts):+.2f}%  max={max(ppcts):+.2f}%  mean={sum(ppcts)/len(ppcts):+.2f}%")
    print(f"  Volmageddon week (Feb 5 - Feb 9):")
    vol = [r for r in out_rows if "2018-02-05" <= r["date"] <= "2018-02-09"]
    for r in vol:
        marker = " <-- VOLMAGEDDON" if r["date"] == "2018-02-05" else ""
        print(f"    {r['date']}  M1({r['m1_code']}) {r['m1_settle']:>6.2f}  M2({r['m2_code']}) {r['m2_settle']:>6.2f}  contango {r['m1m2_pct']:+7.2f}%{marker}")
    print(f"  Recovery (Feb 12 - Feb 28):")
    rec = [r for r in out_rows if r["date"] >= "2018-02-12"]
    if rec:
        rpcts = [r["m1m2_pct"] for r in rec]
        print(f"    n={len(rec)}  min={min(rpcts):+.2f}%  max={max(rpcts):+.2f}%  mean={sum(rpcts)/len(rpcts):+.2f}%")
    print()
    print("  Full daily series:")
    for r in out_rows:
        print(f"    {r['date']}  dte={r['m1_dte']:3d}  M1({r['m1_code']}) {r['m1_settle']:>6.2f}  M2({r['m2_code']}) {r['m2_settle']:>6.2f}  contango {r['m1m2_pct']:+7.2f}%")


if __name__ == "__main__":
    main()
