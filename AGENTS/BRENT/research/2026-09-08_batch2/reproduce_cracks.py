"""Reproduce a fixed-November-2026 vendor-bar diagnostic; not a prediction grader.

Run locally without network. No roll, filling, settlement certification or alert rule.
"""
import csv
import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent
CUTOFF = "2026-09-04"  # Last complete common historical session at capture.
legs = {}
excluded = []
for symbol in ("BZX26", "RBX26", "HOX26"):
    result = json.loads((ROOT / f"{symbol}.json").read_text())["chart"]["result"][0]
    assert result["meta"]["symbol"] == f"{symbol}.NYM"
    quotes = result["indicators"]["quote"][0]
    rows = {}
    for index, timestamp in enumerate(result["timestamp"]):
        date = datetime.fromtimestamp(timestamp, ZoneInfo("America/New_York")).date().isoformat()
        close, volume = quotes["close"][index], quotes["volume"][index]
        if date > CUTOFF or close is None or volume is None or volume <= 0:
            excluded.append({"symbol": symbol, "date": date, "close": close, "volume": volume,
                             "reason": "after cutoff / missing value / nonpositive volume"})
            continue
        assert date not in rows, (symbol, date)
        rows[date] = (close, volume)
    legs[symbol] = rows

common = sorted(set.intersection(*(set(rows) for rows in legs.values())))
rows = []
for date in common:
    brent, rb, ho = (legs[symbol][date][0] for symbol in legs)
    rows.append({"date": date, "contract_month": "2026-11", "brent_usd_bbl": brent,
                 "rb_usd_gal": rb, "ho_usd_gal": ho,
                 "brent_volume": legs["BZX26"][date][1], "rb_volume": legs["RBX26"][date][1],
                 "ho_volume": legs["HOX26"][date][1],
                 "gasoline_crack_usd_bbl": 42 * rb - brent,
                 "distillate_crack_usd_bbl": 42 * ho - brent,
                 "321_crack_usd_bbl": (2 * 42 * rb + 42 * ho) / 3 - brent,
                 "basis": "Yahoo daily close field; fixed November; NOT authenticated settlement"})
assert rows
with (ROOT / "fixed-november-cracks.csv").open("w", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)
summary = {"cutoff": CUTOFF, "matched_rows": len(rows), "first_date": common[0],
           "last_date": common[-1], "excluded": excluded,
           "unmatched_dates": sorted(set.union(*(set(r) for r in legs.values())) - set(common)),
           "minimum_321": min(rows, key=lambda row: row["321_crack_usd_bbl"]),
           "maximum_321": max(rows, key=lambda row: row["321_crack_usd_bbl"]),
           "selected_rows": [r for r in rows if r["date"] in
                             ("2026-03-27", "2026-04-30", "2026-05-29", "2026-06-11",
                              "2026-06-30", "2026-07-31", "2026-08-31", CUTOFF)]}
(ROOT / "crack-validation.json").write_text(json.dumps(summary, indent=2) + "\n")
print(json.dumps({k: summary[k] for k in ("matched_rows", "first_date", "last_date", "unmatched_dates")}))
for row in summary["selected_rows"]:
    print(row["date"], round(row["321_crack_usd_bbl"], 4), round(row["distillate_crack_usd_bbl"], 4))
