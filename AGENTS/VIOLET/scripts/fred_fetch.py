"""Fetch daily series from FRED (public CSV endpoint, no API key)."""
from __future__ import annotations

import io
import os
from datetime import date
from pathlib import Path

import pandas as pd
import requests

CACHE_DIR = Path(__file__).resolve().parent.parent / "workbook" / "fred_cache"

def fetch_series(
    series_id: str,
    start: str = "2024-10-01",
    end: str = "2025-04-01",
    *,
    force: bool = False,
) -> pd.DataFrame:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_file = CACHE_DIR / f"{series_id}_{start}_{end}.csv"

    if cache_file.exists() and not force:
        return pd.read_csv(cache_file, parse_dates=["DATE"], index_col="DATE")

    url = (
        f"https://fred.stlouisfed.org/graph/fredgraph.csv"
        f"?id={series_id}&cosd={start}&coed={end}"
    )
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()

    df = pd.read_csv(io.StringIO(resp.text))
    date_col = [c for c in df.columns if "date" in c.lower()][0]
    df[date_col] = pd.to_datetime(df[date_col])
    df = df.set_index(date_col)
    df.index.name = "DATE"
    df.columns = [series_id]
    df[series_id] = pd.to_numeric(df[series_id], errors="coerce")
    df.dropna(inplace=True)

    df.to_csv(cache_file)
    print(f"[FRED] {series_id}: {len(df)} rows → {cache_file.name}")
    return df


SERIES = {
    "credit": ["BAMLH0A0HYM2", "BAMLC0A0CM", "BAMLH0A3HYC"],
    "rates": ["DGS2", "DGS10", "DFII10"],
}

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--start", default="2024-10-01")
    p.add_argument("--end", default="2025-04-01")
    p.add_argument("--force", action="store_true")
    args = p.parse_args()

    for group, ids in SERIES.items():
        print(f"\n--- {group} ---")
        for sid in ids:
            try:
                fetch_series(sid, args.start, args.end, force=args.force)
            except Exception as e:
                print(f"[ERROR] {sid}: {e}")
