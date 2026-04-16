"""Landmark + tell analysis for the 2024-11 → 2025-01 → 2025-04 cluster analog.

Marks T0, T1, T+peak, identifies Class 1-4 tells.
Outputs: research/analog_2024_cluster/tells_table.md
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "research" / "analog_2024_cluster" / "daily.csv"
OUT_DIR = DATA.parent

LANDMARKS = {
    "T_pre":  pd.Timestamp("2024-10-01"),   # 2 months before first fire
    "T0":     pd.Timestamp("2024-11-22"),   # first SKEW divergence fire
    "T1":     pd.Timestamp("2025-01-22"),   # second fire
    "T_60d":  pd.Timestamp("2025-03-23"),   # 60d from T1
    "T_peak": pd.Timestamp("2025-03-10"),   # VIX peak within 60d window (27.86)
}

INDICATORS = [
    ("VIX",           "VIX spot"),
    ("VIX3M",         "VIX 3M"),
    ("VIX9D",         "VIX 9D"),
    ("VVIX",          "Vol-of-vol"),
    ("SKEW",          "SKEW index"),
    ("VIX3M_VIX_RATIO", "Term structure ratio"),
    ("SPX",           "S&P 500"),
    ("NDX",           "Nasdaq-100"),
    ("BAMLH0A0HYM2",  "HY OAS"),
    ("BAMLC0A0CM",    "IG OAS"),
    ("BAMLH0A3HYC",   "CCC OAS"),
    ("DGS10",         "10Y Treasury"),
    ("DGS2",          "2Y Treasury"),
    ("YC_10Y2Y",      "Yield curve 10-2"),
    ("DFII10",        "10Y TIPS real"),
    ("DXY",           "Dollar index"),
    ("USDJPY",        "USD/JPY"),
    ("GOLD",          "Gold"),
    ("TNX_10Y",       "10Y yield (mkt)"),
]


def nearest(df: pd.DataFrame, col: str, dt: pd.Timestamp) -> float | None:
    s = df[col].dropna()
    if s.empty:
        return None
    idx = s.index.get_indexer([dt], method="nearest")[0]
    return float(s.iloc[idx])


def pct_change(a: float | None, b: float | None) -> str:
    if a is None or b is None or a == 0:
        return "N/A"
    return f"{((b - a) / abs(a)) * 100:+.1f}%"


def classify(t_pre, t0, t1, t_peak) -> str:
    """Classify indicator movement into tell classes."""
    if t_pre is None or t0 is None or t1 is None or t_peak is None:
        return "?"

    move_pre_t0 = abs((t0 - t_pre) / abs(t_pre)) * 100 if t_pre != 0 else 0
    move_t0_t1 = abs((t1 - t0) / abs(t0)) * 100 if t0 != 0 else 0
    move_t1_peak = abs((t_peak - t1) / abs(t1)) * 100 if t1 != 0 else 0

    if move_pre_t0 > 10 or move_t0_t1 > 10:
        return "1-LEADING"
    elif move_t1_peak > 10:
        return "2-COINCIDENT"
    elif move_pre_t0 < 5 and move_t0_t1 < 5 and move_t1_peak < 5:
        return "4-SILENT"
    else:
        return "3-MODERATE"


def main():
    df = pd.read_csv(DATA, parse_dates=["Date"], index_col="Date")

    lines = [
        "# Analog Tell Classification — 2024-11 / 2025-01 Cluster\n",
        "## Landmarks\n",
    ]
    for name, dt in LANDMARKS.items():
        lines.append(f"- **{name}:** {dt.date()}")
    lines.append("")

    header = "| Indicator | T_pre (Oct 1) | T0 (Nov 22) | T1 (Jan 22) | T_peak (Mar 10) | Δ pre→T0 | Δ T0→T1 | Δ T1→peak | Class |"
    sep    = "|-----------|--------------|-------------|-------------|-----------------|----------|---------|-----------|-------|"
    lines.extend(["## Tell Classification\n", header, sep])

    for col, label in INDICATORS:
        if col not in df.columns:
            continue
        vals = {}
        for name, dt in LANDMARKS.items():
            if name in ("T_60d",):
                continue
            vals[name] = nearest(df, col, dt)

        cls = classify(vals.get("T_pre"), vals.get("T0"), vals.get("T1"), vals.get("T_peak"))

        def fmt(v):
            if v is None:
                return "—"
            if abs(v) >= 100:
                return f"{v:,.1f}"
            return f"{v:.2f}"

        row = (
            f"| {label} "
            f"| {fmt(vals.get('T_pre'))} "
            f"| {fmt(vals.get('T0'))} "
            f"| {fmt(vals.get('T1'))} "
            f"| {fmt(vals.get('T_peak'))} "
            f"| {pct_change(vals.get('T_pre'), vals.get('T0'))} "
            f"| {pct_change(vals.get('T0'), vals.get('T1'))} "
            f"| {pct_change(vals.get('T1'), vals.get('T_peak'))} "
            f"| **{cls}** |"
        )
        lines.append(row)

    lines.append("")
    lines.append("## Class Definitions\n")
    lines.append("- **1-LEADING:** >10% absolute move before T1 (pre→T0 or T0→T1)")
    lines.append("- **2-COINCIDENT:** >10% move T1→T_peak only")
    lines.append("- **3-MODERATE:** Moderate movement (<10%) across phases")
    lines.append("- **4-SILENT:** <5% move in all phases")
    lines.append("")

    out_path = OUT_DIR / "tells_table.md"
    out_path.write_text("\n".join(lines))
    print(f"Wrote tells table → {out_path}")
    print(f"{len(INDICATORS)} indicators classified")


if __name__ == "__main__":
    main()
