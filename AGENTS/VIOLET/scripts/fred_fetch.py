"""Fetch daily series from FRED (public CSV endpoint, no API key).

Cache model (rewritten 2026-06-23, KB-VIO-103): ONE canonical file per
(series, start) — `{series_id}_{start}.csv` — that grows in place via
merge-on-write. The old `{series_id}_{start}_{end}.csv` convention minted a
new file every calendar day (8+ per code), so any ad-hoc "read the latest"
glob could non-deterministically pick a STALE older-dated file. That mis-read
(NOT a fetch failure) is what produced the false "fred_fetch broken" call at
the 6/23 boot — the fetch was fine; the reader picked the wrong file.

Use `latest_value()` / `--summary` to read the gate; never glob the cache.
"""
from __future__ import annotations

import io
import os
from datetime import date
from pathlib import Path

import pandas as pd
import requests

CACHE_DIR = Path(__file__).resolve().parent.parent / "workbook" / "fred_cache"

# Freshness tolerance: cache is "fresh enough" if its last row is within this
# many calendar days of the requested end (covers weekends + FRED's T+1 lag).
FRESH_TOLERANCE_DAYS = 4


def _cache_path(series_id: str, start: str) -> Path:
    # NOTE: end deliberately NOT in the filename — one canonical file per
    # (series, start), grown via merge-on-write. See module docstring.
    return CACHE_DIR / f"{series_id}_{start}.csv"


def fetch_series(
    series_id: str,
    start: str = "2024-10-01",
    end: str | None = None,
    *,
    force: bool = False,
) -> pd.DataFrame:
    if end is None:
        end = date.today().isoformat()
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_file = _cache_path(series_id, start)

    if cache_file.exists() and not force:
        cached = pd.read_csv(cache_file, parse_dates=["DATE"], index_col="DATE")
        if not cached.empty:
            fresh_through = pd.Timestamp(end) - pd.Timedelta(days=FRESH_TOLERANCE_DAYS)
            if cached.index.max() >= fresh_through:
                print(f"[FRED] {series_id}: {len(cached)} rows (cached, "
                      f"latest {cached.index.max().date()})")
                return cached
            # stale → fall through and re-fetch, then merge
            print(f"[FRED] {series_id}: cache stale "
                  f"(latest {cached.index.max().date()} < {fresh_through.date()}), refetching")

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

    # merge-on-write: never let a partial/past-window fetch SHRINK the
    # canonical file. Union by date; freshly-fetched values win on overlap.
    if cache_file.exists():
        old = pd.read_csv(cache_file, parse_dates=["DATE"], index_col="DATE")
        df = df.combine_first(old).sort_index()
        df = df[~df.index.duplicated(keep="first")]

    df.to_csv(cache_file)
    print(f"[FRED] {series_id}: {len(df)} rows → {cache_file.name} "
          f"(latest {df.index.max().date()})")
    return df


def latest_value(
    series_id: str,
    start: str = "2024-10-01",
    end: str | None = None,
    *,
    force: bool = False,
) -> tuple[pd.Timestamp, float]:
    """Canonical 'read the latest value' — freshness-aware, no globbing.

    Returns (date, value) of the most recent row. This is the ONLY supported
    way to read a current value; do not glob the cache dir by hand.
    """
    df = fetch_series(series_id, start, end, force=force)
    last = df.dropna().iloc[-1]
    return df.dropna().index.max(), float(last.iloc[0])


# Friendly names + the credit series of interest for --summary.
NAMES = {
    "BAMLH0A0HYM2": "HY", "BAMLC0A0CM": "IG", "BAMLH0A3HYC": "CCC",
    "BAMLH0A1HYBB": "BB", "BAMLH0A2HYB": "B", "BAMLC0A4CBBB": "BBB",
    "BAMLHE00EHYIOAS": "EuroHY", "BAMLEMHBHYCRPIOAS": "EM_HY",
    "DGS2": "2Y", "DGS10": "10Y", "DFII10": "TIPS10",
}

# Credit-gate lines (KB-VIO-090 tree / KB-VIO-096 block).
BINB_BLOCK_LINE = 9.55          # CCC >= this => Bin-B block ACTIVE; < this => block LIFTS
BINA_LINES = {                  # any one tripped => Bin-A escalation
    "CCC >= 9.65": ("CCC", 9.65),
    "BB >= 1.73": ("BB", 1.73),
    "HY >= 2.85": ("HY", 2.85),
    "CCC-BB disp >= 8.00": ("DISP", 8.00),
}


def credit_summary(*, force: bool = False) -> dict:
    """Print + return the credit-gate dashboard with KB-VIO-090/096 verdict."""
    codes = ["BAMLH0A0HYM2", "BAMLH0A3HYC", "BAMLH0A1HYBB", "BAMLH0A2HYB",
             "BAMLC0A4CBBB", "BAMLC0A0CM", "BAMLHE00EHYIOAS", "BAMLEMHBHYCRPIOAS"]
    vals, dates = {}, {}
    for c in codes:
        try:
            d, v = latest_value(c, force=force)
            vals[NAMES[c]] = v
            dates[NAMES[c]] = d.date().isoformat()
        except Exception as e:
            print(f"[ERROR] {NAMES.get(c, c)}: {e}")
    disp = round(vals["CCC"] - vals["BB"], 2) if {"CCC", "BB"} <= vals.keys() else None
    if disp is not None:
        vals["DISP"] = disp

    print("\n" + "=" * 60)
    print("  CREDIT GATE SUMMARY (KB-VIO-090 tree / KB-VIO-096 block)")
    print("=" * 60)
    asof = dates.get("CCC", "?")
    for name in ["HY", "CCC", "BB", "B", "BBB", "IG", "EuroHY", "EM_HY"]:
        if name in vals:
            print(f"  {name:7s} {vals[name]:>6.2f}   [{dates.get(name, '?')}]")
    if disp is not None:
        print(f"  {'CCC-BB':7s} {disp:>6.2f}   (Bin-A line 8.00)")

    # Verdict
    tripped = [label for label, (k, lvl) in BINA_LINES.items()
               if k in vals and vals[k] >= lvl]
    print("-" * 60)
    if tripped:
        verdict = "🔴 BIN-A ESCALATION — " + "; ".join(tripped)
    elif vals.get("CCC", 0) >= BINB_BLOCK_LINE:
        verdict = f"🟠 BIN-B BLOCK ACTIVE (CCC {vals['CCC']:.2f} ≥ {BINB_BLOCK_LINE})"
    else:
        margin = BINB_BLOCK_LINE - vals.get("CCC", BINB_BLOCK_LINE)
        verdict = (f"🟢 BLOCK LIFTED (CCC {vals.get('CCC'):.2f} < {BINB_BLOCK_LINE}, "
                   f"{margin:.2f} below the line); no Bin-A")
    print(f"  VERDICT [{asof}]: {verdict}")
    print("=" * 60)
    return {"asof": asof, "values": vals, "dates": dates,
            "dispersion": disp, "bin_a_tripped": tripped, "verdict": verdict}


SERIES = {
    # HY composite, IG composite, CCC
    "credit": ["BAMLH0A0HYM2", "BAMLC0A0CM", "BAMLH0A3HYC"],
    # KB-VIO-090 tree conversion lines: BB (A2 1.73), single-B (watch-only), CCC-BB dispersion needs BB
    "credit_ladder": ["BAMLH0A1HYBB", "BAMLH0A2HYB", "BAMLC0A4CBBB"],
    # KB-VIO-097 US-local-vs-global control: Euro HY + EM HY corp
    "credit_global": ["BAMLHE00EHYIOAS", "BAMLEMHBHYCRPIOAS"],
    "rates": ["DGS2", "DGS10", "DFII10"],
}

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--start", default="2024-10-01")
    p.add_argument("--end", default=date.today().isoformat())
    p.add_argument("--force", action="store_true")
    p.add_argument("--summary", action="store_true",
                   help="Print the credit-gate dashboard (KB-VIO-090/096 verdict)")
    args = p.parse_args()

    for group, ids in SERIES.items():
        print(f"\n--- {group} ---")
        for sid in ids:
            try:
                fetch_series(sid, args.start, args.end, force=args.force)
            except Exception as e:
                print(f"[ERROR] {sid}: {e}")

    if args.summary:
        credit_summary(force=False)  # already fetched above; read canonical
