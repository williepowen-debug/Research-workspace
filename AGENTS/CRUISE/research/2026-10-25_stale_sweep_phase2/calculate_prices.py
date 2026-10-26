"""Reproduce this bounded refresh from saved CSVs; no fetch or forecast grading."""
import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
results = {}
for ticker in ("CCL", "RCL", "NCLH"):
    rows = list(csv.DictReader((HERE / "sources" / f"{ticker}-yfinance.csv").open()))
    last, previous = rows[-1], rows[-2]
    close = float(last["Close"])
    results[ticker] = {
        "date": last["Date"][:10], "raw_close": close,
        "adjusted_close": float(last["Adj Close"]),
        "daily_raw_change_pct": 100 * (close / float(previous["Close"]) - 1),
    }
    if ticker == "CCL":
        results[ticker].update(
            fixed_raw_reference=33.99, reference_date="2026-02-06",
            raw_change_from_reference_pct=100 * (close / 33.99 - 1),
            distance_above_red_dollars=close-22.0935,
            decline_to_red_pct=100 * (1-22.0935/close),
            rise_to_yellow_pct=100 * (27.192/close-1),
        )
    if ticker == "NCLH":
        results[ticker]["raw_change_from_held_25_02_peak_pct"] = 100 * (close/25.02-1)
output = {
    "vendor": "Yahoo Finance via pinned repository yfinance; raw CSVs saved",
    "scope": "Three existing price series only; no CRU-11 resolver or interim update",
    "prices": results,
}
(HERE / "calculations.json").write_text(json.dumps(output, indent=2)+"\n")
print(json.dumps(output, indent=2))
