"""
RED adversarial re-analysis of VIOLET's SKEW divergence base rate.

Tier A:
  A1 — Ex-cluster base rate (drop 2024-26 episodes, recompute)
  A2 — Sustained vs intraday peak (closed >25 for >=5 consecutive days)
  A3 — 36-day window (matching May 19 from Apr 13) split by sustained-vs-intraday

Data: VIOLET's vix_historical.csv (2018-01-02 to 2026-04-10). Limited to 2018+,
so we recover episodes #3-#16 (n=14) — episodes #1 (2014-11) and #2 (2015-10)
not in this dataset. Effect: drops 2 from non-cluster cohort, makes the
2024-26 cluster effect MORE pronounced (5 of 14 episodes).
"""

import pandas as pd
import numpy as np

DATA = "/home/willi/Research-workspace/AGENTS/VIOLET/workbook/vix_historical.csv"

# Reproduce VIOLET's pattern definition exactly:
#   20-day rolling window where:
#     SKEW rose >=10 pts AND VIX fell >=5 pts AND VVIX fell >=15 pts
SKEW_THRESHOLD = 10
VIX_DROP_THRESHOLD = 5
VVIX_DROP_THRESHOLD = 15
WINDOW = 20


def load_data():
    df = pd.read_csv(DATA, parse_dates=["Date"])
    df = df.sort_values("Date").reset_index(drop=True)
    df = df.rename(columns={
        "Close ^SKEW": "SKEW",
        "Close ^VIX": "VIX",
        "Close ^VVIX": "VVIX",
        "High ^VIX": "VIX_HIGH",
    })
    return df[["Date", "SKEW", "VIX", "VVIX", "VIX_HIGH"]].dropna()


def find_fire_days(df):
    """Days where the 20d rolling change matches VIOLET's pattern."""
    skew_chg = df["SKEW"].diff(WINDOW)
    vix_chg = df["VIX"].diff(WINDOW)
    vvix_chg = df["VVIX"].diff(WINDOW)
    mask = (skew_chg >= SKEW_THRESHOLD) & (vix_chg <= -VIX_DROP_THRESHOLD) & (vvix_chg <= -VVIX_DROP_THRESHOLD)
    return df.loc[mask, "Date"].tolist()


def cluster_into_episodes(fire_dates, max_gap=20):
    """Group consecutive fire days within max_gap days into single episodes.
    Episode start = first fire date. Episode end = last fire date in cluster."""
    if not fire_dates:
        return []
    fire_dates = sorted(fire_dates)
    episodes = [[fire_dates[0], fire_dates[0]]]
    for d in fire_dates[1:]:
        if (d - episodes[-1][1]).days <= max_gap:
            episodes[-1][1] = d
        else:
            episodes.append([d, d])
    return episodes


def episode_skew_peak(df, start, end, lookback=10):
    """Peak SKEW within the episode window (and the few days surrounding)."""
    window_start = start - pd.Timedelta(days=lookback)
    window_end = end + pd.Timedelta(days=lookback)
    sub = df[(df["Date"] >= window_start) & (df["Date"] <= window_end)]
    return sub["SKEW"].max() if len(sub) else np.nan


def forward_window(df, start, days):
    """Trading-day window of length `days` starting from `start`."""
    fwd = df[df["Date"] > start].head(days)
    return fwd


def peak_intraday(fwd):
    return fwd["VIX_HIGH"].max() if len(fwd) else np.nan


def peak_close(fwd):
    return fwd["VIX"].max() if len(fwd) else np.nan


def sustained_above(fwd, level, n_consec):
    """True iff close >= level for >= n_consec consecutive trading days."""
    if len(fwd) < n_consec:
        return False
    above = (fwd["VIX"] >= level).astype(int).values
    # Find longest consecutive run
    run = 0
    best = 0
    for v in above:
        run = run + 1 if v else 0
        best = max(best, run)
    return best >= n_consec


def episode_outcomes(df, start, vix_at_start, horizon_days=60):
    """Compute per-episode forward stats."""
    fwd = forward_window(df, start, horizon_days)
    if not len(fwd):
        return None
    pk_intra = peak_intraday(fwd)
    pk_close = peak_close(fwd)
    pct_intra = (pk_intra - vix_at_start) / vix_at_start * 100
    pct_close = (pk_close - vix_at_start) / vix_at_start * 100
    return {
        "horizon_days": horizon_days,
        "peak_intraday": pk_intra,
        "peak_close": pk_close,
        "pct_intra": pct_intra,
        "pct_close": pct_close,
        "sust_25_5d": sustained_above(fwd, 25, 5),
        "sust_25_3d": sustained_above(fwd, 25, 3),
        "sust_30_3d": sustained_above(fwd, 30, 3),
        "intra_above_25": pk_intra >= 25,
        "close_above_25": pk_close >= 25,
        "intra_above_30": pk_intra >= 30,
    }


def main():
    df = load_data()
    print(f"Data range: {df['Date'].min().date()} to {df['Date'].max().date()} ({len(df)} rows)\n")

    fires = find_fire_days(df)
    print(f"Total individual fire days: {len(fires)}")

    episodes = cluster_into_episodes(fires)
    print(f"Distinct episodes after clustering: {len(episodes)}\n")

    rows = []
    for i, (start, end) in enumerate(episodes, 1):
        skew_peak = episode_skew_peak(df, start, end)
        vix_at_start = df.loc[df["Date"] == start, "VIX"].iloc[0]
        for h in [30, 36, 60]:
            o = episode_outcomes(df, start, vix_at_start, h)
            if o is None:
                continue
            rows.append({
                "ep": i,
                "start": start.date(),
                "end": end.date(),
                "n_fire_days": (df["Date"].between(start, end)).sum(),
                "skew_peak": round(skew_peak, 1),
                "vix_at_start": round(vix_at_start, 2),
                **{k: (round(v, 2) if isinstance(v, float) else v) for k, v in o.items()},
            })

    out = pd.DataFrame(rows)

    # Tag cluster
    out["in_2024_26_cluster"] = out["start"].apply(lambda d: pd.Timestamp(d) >= pd.Timestamp("2024-01-01"))

    # Print episode summary at 60d
    print("=" * 110)
    print("ALL EPISODES — 60d horizon")
    print("=" * 110)
    cols_60 = ["ep", "start", "skew_peak", "vix_at_start", "peak_close", "peak_intraday",
               "pct_close", "pct_intra", "sust_25_5d", "sust_25_3d", "intra_above_25", "in_2024_26_cluster"]
    print(out[out["horizon_days"] == 60][cols_60].to_string(index=False))

    # Tier A1: ex-cluster base rate
    print("\n" + "=" * 110)
    print("A1 — Ex-cluster base rate")
    print("=" * 110)
    for label, sub in [("ALL", out[out["horizon_days"] == 60]),
                       ("EX 2024-26 CLUSTER", out[(out["horizon_days"] == 60) & (~out["in_2024_26_cluster"])]),
                       ("ONLY 2024-26 CLUSTER", out[(out["horizon_days"] == 60) & (out["in_2024_26_cluster"])])]:
        n = len(sub)
        if n == 0:
            continue
        any_30 = (sub["pct_intra"] >= 30).sum()
        any_50 = (sub["pct_intra"] >= 50).sum()
        sust_25 = sub["sust_25_5d"].sum()
        intra_25 = sub["intra_above_25"].sum()
        intra_30 = sub["intra_above_30"].sum()
        print(f"\n  {label}: n={n}")
        print(f"    Intraday peak >+30%:        {any_30}/{n} ({any_30/n*100:.0f}%)")
        print(f"    Intraday peak >+50%:        {any_50}/{n} ({any_50/n*100:.0f}%)")
        print(f"    Intraday peak VIX >=25:     {intra_25}/{n} ({intra_25/n*100:.0f}%)")
        print(f"    Intraday peak VIX >=30:     {intra_30}/{n} ({intra_30/n*100:.0f}%)")
        print(f"    SUSTAINED close >=25 5d+:   {sust_25}/{n} ({sust_25/n*100:.0f}%)")

    # Tier A2: sustained vs intraday at 60d
    print("\n" + "=" * 110)
    print("A2 — Sustained vs intraday peak (60d)")
    print("=" * 110)
    sub = out[out["horizon_days"] == 60]
    n = len(sub)
    print(f"\n  Sample n={n}")
    print(f"    Intraday peak VIX >=25:                {(sub['intra_above_25']).sum()}/{n} ({(sub['intra_above_25']).sum()/n*100:.0f}%)")
    print(f"    Closing peak VIX >=25:                 {(sub['close_above_25']).sum()}/{n} ({(sub['close_above_25']).sum()/n*100:.0f}%)")
    print(f"    Sustained close >=25 for 3 td:         {(sub['sust_25_3d']).sum()}/{n} ({(sub['sust_25_3d']).sum()/n*100:.0f}%)")
    print(f"    Sustained close >=25 for 5 td:         {(sub['sust_25_5d']).sum()}/{n} ({(sub['sust_25_5d']).sum()/n*100:.0f}%)")
    print(f"    Sustained close >=30 for 3 td:         {(sub['sust_30_3d']).sum()}/{n} ({(sub['sust_30_3d']).sum()/n*100:.0f}%)")

    # Tier A3: 36-day option-specific horizon
    print("\n" + "=" * 110)
    print("A3 — 36-day option-specific horizon (matches May 19 from Apr 13 fire)")
    print("=" * 110)
    sub = out[out["horizon_days"] == 36]
    n = len(sub)
    print(f"\n  Sample n={n}")
    print(f"    Intraday peak VIX >=25:                {(sub['intra_above_25']).sum()}/{n} ({(sub['intra_above_25']).sum()/n*100:.0f}%)")
    print(f"    Closing peak VIX >=25:                 {(sub['close_above_25']).sum()}/{n} ({(sub['close_above_25']).sum()/n*100:.0f}%)")
    print(f"    Sustained close >=25 for 3 td:         {(sub['sust_25_3d']).sum()}/{n} ({(sub['sust_25_3d']).sum()/n*100:.0f}%)")
    print(f"    Sustained close >=25 for 5 td:         {(sub['sust_25_5d']).sum()}/{n} ({(sub['sust_25_5d']).sum()/n*100:.0f}%)")

    # Cross-tab: A3 split by cluster
    print("\n  Cross-tab — A3 (36d) split by cluster:")
    for label, ssub in [("EX 2024-26", sub[~sub["in_2024_26_cluster"]]),
                        ("ONLY 2024-26", sub[sub["in_2024_26_cluster"]])]:
        nn = len(ssub)
        if nn == 0:
            continue
        print(f"    {label:14s} n={nn} | sust25_5d {ssub['sust_25_5d'].sum()}/{nn} ({ssub['sust_25_5d'].sum()/nn*100:.0f}%) | sust25_3d {ssub['sust_25_3d'].sum()}/{nn} ({ssub['sust_25_3d'].sum()/nn*100:.0f}%) | intra25 {ssub['intra_above_25'].sum()}/{nn} ({ssub['intra_above_25'].sum()/nn*100:.0f}%)")

    # Save full output
    out.to_csv("/home/willi/Research-workspace/AGENTS/RED/research/violet_skew_recheck_results.csv", index=False)
    print("\nFull results written to research/violet_skew_recheck_results.csv")


if __name__ == "__main__":
    main()
