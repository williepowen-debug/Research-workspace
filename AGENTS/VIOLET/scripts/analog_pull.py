"""Pull all Phase 2 analog data into a single aligned daily DataFrame.

Covers 2024-10-01 → 2025-04-01 (2 months before first SKEW divergence fire,
2 months after VIX-52 peak).

Outputs: research/analog_2024_cluster/daily.csv
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import yfinance as yf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fred_fetch import fetch_series

START = "2024-10-01"
END = "2025-04-01"
OUT_DIR = Path(__file__).resolve().parent.parent / "research" / "analog_2024_cluster"


def pull_yfinance(tickers: dict[str, str]) -> pd.DataFrame:
    frames = []
    for ticker, col_name in tickers.items():
        print(f"[yfinance] {ticker} → {col_name}")
        try:
            df = yf.download(ticker, start=START, end=END, progress=False, auto_adjust=True)
            if df.empty:
                print(f"  WARNING: no data for {ticker}")
                continue
            s = df["Close"].squeeze()
            s.name = col_name
            s.index = s.index.tz_localize(None)
            frames.append(s)
        except Exception as e:
            print(f"  ERROR: {ticker}: {e}")
    return pd.concat(frames, axis=1) if frames else pd.DataFrame()


def pull_fred() -> pd.DataFrame:
    fred_ids = [
        "BAMLH0A0HYM2", "BAMLC0A0CM", "BAMLH0A3HYC",
        "DGS2", "DGS10", "DFII10",
    ]
    frames = []
    for sid in fred_ids:
        try:
            df = fetch_series(sid, START, END)
            frames.append(df)
        except Exception as e:
            print(f"[FRED ERROR] {sid}: {e}")
    return pd.concat(frames, axis=1) if frames else pd.DataFrame()


def compute_derived(df: pd.DataFrame) -> pd.DataFrame:
    if "DGS10" in df.columns and "DGS2" in df.columns:
        df["YC_10Y2Y"] = df["DGS10"] - df["DGS2"]

    if "VIX3M" in df.columns and "VIX" in df.columns:
        df["VIX3M_VIX_RATIO"] = df["VIX3M"] / df["VIX"]

    if "SPX" in df.columns:
        df["SPX_RV20"] = df["SPX"].pct_change().rolling(20).std() * (252 ** 0.5) * 100

    if "VIX" in df.columns and "SPX_RV20" in df.columns:
        df["VOL_RISK_PREMIUM"] = df["VIX"] - df["SPX_RV20"]

    return df


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    yf_tickers = {
        "^VIX": "VIX",
        "^VIX3M": "VIX3M",
        "^VIX9D": "VIX9D",
        "^VVIX": "VVIX",
        "^SKEW": "SKEW",
        "^GSPC": "SPX",
        "^NDX": "NDX",
        "^TNX": "TNX_10Y",
        "DX-Y.NYB": "DXY",
        "JPY=X": "USDJPY",
        "GC=F": "GOLD",
    }

    print("=== Phase 2: Analog Data Pull ===\n")
    print("--- yfinance ---")
    yf_df = pull_yfinance(yf_tickers)
    print(f"\nyfinance: {len(yf_df)} rows, {len(yf_df.columns)} cols")

    print("\n--- FRED ---")
    fred_df = pull_fred()
    print(f"FRED: {len(fred_df)} rows, {len(fred_df.columns)} cols")

    print("\n--- Merging ---")
    combined = yf_df.join(fred_df, how="outer")
    combined = compute_derived(combined)
    combined.sort_index(inplace=True)

    out_path = OUT_DIR / "daily.csv"
    combined.to_csv(out_path)
    print(f"\nWrote {len(combined)} rows × {len(combined.columns)} cols → {out_path}")
    print(f"Columns: {list(combined.columns)}")
    print(f"Date range: {combined.index.min()} → {combined.index.max()}")

    nulls = combined.isnull().sum()
    if nulls.any():
        print(f"\nNull counts:\n{nulls[nulls > 0]}")

    return combined


if __name__ == "__main__":
    main()
