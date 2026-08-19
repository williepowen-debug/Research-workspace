"""
refresh_auction_history_prome-spawned.py
=========================================

Refreshes AGENTS/BOND/data/auction_history_prome-spawned.csv (v1) AND
AGENTS/BOND/data/auction_history_v2_prome-spawned.csv (v2 = v1 + tail
+ indirect_pct_of_competitive columns) from the US Treasury FiscalData
auctions_query endpoint plus FRED constant-maturity yields.

Source (auctions):
    https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/od/auctions_query

Source (CMT closes, for tail proxy):
    https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS{2,3,5,7,10,20,30}

Scope:
    - Coupon-bearing Treasuries only: Notes + Bonds (Bills excluded).
    - Tenors: 2Y, 3Y, 5Y, 7Y, 10Y, 20Y, 30Y (includes reopenings).
    - TIPS are included and flagged via the `inflation_index_security` column.
    - Date range: 2023-01-01 through today (configurable below).

How to run (from repo root, with .venv active):
    source .venv/bin/activate && python3 AGENTS/BOND/data/refresh_auction_history_prome-spawned.py

Dependencies: pandas, requests (already in .venv).

GOTCHAS (BOND 2026-06-05):
  1. FiscalData `auctions_query` returns HTTP 200 with ZERO rows — no error — if
     ANY name in the `fields=` projection is invalid. A hand-rolled query that
     asks for e.g. `competitive_accepted` or `high_investment_rate` (neither
     exists) silently yields []. Always validate field names against this
     script's API_FIELDS, or omit `fields` and filter in pandas. Don't trust an
     empty result as "no auctions happened."
  2. Use api.stlouisfed.org (keyed JSON), NOT fred.stlouisfed.org/graph (keyless
     CSV) — the graph host hangs in this sandbox. See fetch_fred().
  3. TIPS discriminator: use the `is_tips` column (from `inflation_index_security`),
     NOT the term label. A "10-Year" / "9Y8M" can be a TIPS reopening with a real
     high_yield (~2%) that looks nothing like the nominal (~4.5%).

Versions:
    v1 (2026-05-20 AM): auctions + allocation pcts (of offering_amt).
    v2 (2026-05-20 PM): + cmt_close_prior_day, tail_vs_cmt_bps,
        total_competitive_accepted, indirect_pct_of_competitive.

Author: Prome-spawned sub-agent.
BOND integrates / commits on next boot.
"""

from __future__ import annotations

import datetime as dt
import io
import os
import sys
import time
from pathlib import Path

import pandas as pd
import requests

API_URL = (
    "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/"
    "v1/accounting/od/auctions_query"
)

# Tenors of interest. Match against `original_security_term` from the API.
TARGET_TENORS = {
    "2-Year": "2Y",
    "3-Year": "3Y",
    "5-Year": "5Y",
    "7-Year": "7Y",
    "10-Year": "10Y",
    "20-Year": "20Y",
    "30-Year": "30Y",
}

# Coupon-bearing security types only (Bills excluded).
TARGET_SEC_TYPES = {"Note", "Bond"}

START_DATE = "2023-01-01"
END_DATE = dt.date.today().isoformat()  # inclusive

OUTPUT_CSV = Path(__file__).parent / "auction_history_prome-spawned.csv"
OUTPUT_CSV_V2 = Path(__file__).parent / "auction_history_v2_prome-spawned.csv"

# FRED CMT series for tail approximation.
TENOR_TO_FRED = {
    "2Y": "DGS2",
    "3Y": "DGS3",
    "5Y": "DGS5",
    "7Y": "DGS7",
    "10Y": "DGS10",
    "20Y": "DGS20",
    "30Y": "DGS30",
}

# Fields we ask the API for. Keeping the projection narrow speeds the response.
API_FIELDS = ",".join(
    [
        "auction_date",
        "issue_date",
        "maturity_date",
        "cusip",
        "security_type",
        "security_term",
        "original_security_term",
        "reopening",
        "inflation_index_security",
        "offering_amt",
        "total_accepted",
        "high_yield",
        "bid_to_cover_ratio",
        "primary_dealer_accepted",
        "direct_bidder_accepted",
        "indirect_bidder_accepted",
        "soma_accepted",
    ]
)


def fetch_all() -> pd.DataFrame:
    """Pull the full date range. The endpoint allows page[size]=10000; we still
    page defensively in case the row count grows past that."""
    rows: list[dict] = []
    page = 1
    while True:
        params = {
            "filter": f"auction_date:gte:{START_DATE},auction_date:lte:{END_DATE}",
            "fields": API_FIELDS,
            "page[size]": "10000",
            "page[number]": str(page),
            "sort": "auction_date",
        }
        r = requests.get(API_URL, params=params, timeout=120)
        r.raise_for_status()
        payload = r.json()
        chunk = payload.get("data", [])
        rows.extend(chunk)
        meta = payload.get("meta", {})
        total_pages = meta.get("total-pages", 1)
        if page >= total_pages or not chunk:
            break
        page += 1
    return pd.DataFrame(rows)


def transform(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df

    # Filter to coupon-bearing notes + bonds in the target tenors.
    df = df[df["security_type"].isin(TARGET_SEC_TYPES)].copy()
    df = df[df["original_security_term"].isin(TARGET_TENORS.keys())].copy()

    # Drop rows without auction results (announcements, future auctions).
    # We treat absence of high_yield AND bid_to_cover_ratio as "no result yet".
    df = df.replace({"null": None, "": None})
    df = df[
        df["high_yield"].notna() | df["bid_to_cover_ratio"].notna()
    ].copy()

    # Coerce numerics.
    num_cols = [
        "offering_amt",
        "total_accepted",
        "high_yield",
        "bid_to_cover_ratio",
        "primary_dealer_accepted",
        "direct_bidder_accepted",
        "indirect_bidder_accepted",
        "soma_accepted",
    ]
    for col in num_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Booleans.
    df["is_reopening"] = df["reopening"].map(
        lambda v: True if str(v).lower() == "yes" else False
    )
    df["is_tips"] = df["inflation_index_security"].map(
        lambda v: True if str(v).lower() == "yes" else False
    )

    # Tenor label.
    df["tenor"] = df["original_security_term"].map(TARGET_TENORS)

    # Derived allocation percentages.
    # Denominator: total_accepted when present (true allocation base),
    # else offering_amt as a fallback.
    denom = df["total_accepted"].where(df["total_accepted"].gt(0), df["offering_amt"])
    df["dealer_pct"] = df["primary_dealer_accepted"] / denom
    df["direct_pct"] = df["direct_bidder_accepted"] / denom
    df["indirect_pct"] = df["indirect_bidder_accepted"] / denom

    # Final column order.
    out_cols = [
        "auction_date",
        "tenor",
        "security_type",
        "is_reopening",
        "is_tips",
        "issue_date",
        "maturity_date",
        "cusip",
        "offering_amt",
        "total_accepted",
        "high_yield",
        "bid_to_cover_ratio",
        "primary_dealer_accepted",
        "direct_bidder_accepted",
        "indirect_bidder_accepted",
        "soma_accepted",
        "dealer_pct",
        "direct_pct",
        "indirect_pct",
    ]
    df = df[out_cols].sort_values(["auction_date", "tenor"]).reset_index(drop=True)
    return df


def fetch_fred(series_id: str) -> pd.Series:
    """Download a FRED daily series via the FRED API (api.stlouisfed.org).

    NOTE (BOND 2026-06-05): switched from the keyless graph CSV endpoint
    (fred.stlouisfed.org/graph/fredgraph.csv) to the keyed JSON API because the
    graph-CSV host hangs/blocks in this sandbox — it stalled the whole v2
    enrichment. Key mirrors FORGE/tools/market-data/fetch.py. Retries on 429."""
    key = os.environ.get("FRED_API_KEY", "")
    if not key:
        # gitignored FORGE market-data .env = single per-machine key home
        # (hardcoded copies scrubbed 2026-07-01, public-prep)
        import pathlib
        _p = pathlib.Path(__file__).resolve().parents[3] / "FORGE/tools/market-data/.env"
        if _p.exists():
            key = next((l.split("=", 1)[1].strip() for l in _p.read_text().splitlines()
                        if l.startswith("FRED_API_KEY=")), "")
        if not key:
            import sys
            print("WARN: FRED_API_KEY not found (env or FORGE/tools/market-data/.env) — FRED pull will fail",
                  file=sys.stderr)
    url = "https://api.stlouisfed.org/fred/series/observations"
    params = {
        "series_id": series_id,
        "api_key": key,
        "file_type": "json",
        "observation_start": "2022-06-01",
    }
    ok = False
    for attempt in range(4):
        try:
            r = requests.get(url, params=params, timeout=60)
            if r.status_code == 429:
                wait = 2 ** attempt
                print(f"[fred] 429 on {series_id}, backoff {wait}s", file=sys.stderr)
                time.sleep(wait)
                continue
            r.raise_for_status()
            ok = True
            break
        except requests.RequestException as e:
            if attempt == 3:
                raise
            print(f"[fred] retry {series_id}: {e}", file=sys.stderr)
            time.sleep(2 ** attempt)
    # FIX 2026-08-18 (DAEDALUS defect 3): the loop previously exited on a
    # 4x-429 exhaustion WITHOUT break and WITHOUT raising, so r.json() ran on
    # the 429 body -> obs=[] -> an all-null tail column written at rc=0.
    # A rate-limit exhaustion is a FAILURE and must be loud.
    if not ok:
        raise RuntimeError(
            f"FRED rate-limited {series_id}: 4 consecutive 429s. "
            "Refusing to continue -- silently returning an empty series here "
            "writes an all-null enrichment column at exit code 0."
        )
    obs = r.json().get("observations", [])
    df = pd.DataFrame([(o["date"], o["value"]) for o in obs], columns=["date", "yld"])
    df["date"] = pd.to_datetime(df["date"]).dt.date
    df["yld"] = pd.to_numeric(df["yld"], errors="coerce")
    df = df.dropna(subset=["yld"]).sort_values("date")
    return df.set_index("date")["yld"]


def build_cmt_lookup() -> dict[str, pd.Series]:
    out: dict[str, pd.Series] = {}
    for tenor, fid in TENOR_TO_FRED.items():
        print(f"[fred] fetching {fid} for {tenor}...")
        out[tenor] = fetch_fred(fid)
        time.sleep(0.3)
    return out


# FIX 2026-08-18 (DAEDALUS defect 1): the fallback was UNBOUNDED and recorded
# NO DATE, so a same-day close and a 90-day-old close wrote byte-identical
# cmt_close_prior_day / tail_vs_cmt_bps cells. That column is an auction-tail
# instrument, and BOND RETIRED the tail metric on 2026-07-28 as unscoreable
# from primaries. It is now bounded, stamped, and explicitly non-gating.
MAX_CMT_LOOKBACK_DAYS = 7


def _cmt_for(series: pd.Series, auction_date):
    """Return (yield, asof_date, lag_days) for auction_date.

    Falls back to the most recent business day strictly prior, but ONLY within
    MAX_CMT_LOOKBACK_DAYS. Past that bound it REFUSES (returns None) rather than
    silently serving a stale close as if it were the auction-day close.
    """
    if auction_date in series.index:
        return float(series.loc[auction_date]), auction_date, 0
    prior = series.index[series.index < auction_date]
    if len(prior) == 0:
        return None, None, None
    asof = prior.max()
    lag = (auction_date - asof).days
    if lag > MAX_CMT_LOOKBACK_DAYS:
        print(f"[cmt] REFUSED: nearest prior close for {auction_date} is {asof} "
              f"({lag}d > {MAX_CMT_LOOKBACK_DAYS}d bound) -- writing null, not a stale value",
              file=sys.stderr)
        return None, None, None
    return float(series.loc[asof]), asof, lag


def enrich_v2(df: pd.DataFrame, cmt: dict[str, pd.Series]) -> pd.DataFrame:
    """Add v2 columns: cmt_close_prior_day, tail_vs_cmt_bps,
    total_competitive_accepted, indirect_pct_of_competitive."""
    df = df.copy()
    dates = pd.to_datetime(df["auction_date"]).dt.date.tolist()
    tenors = df["tenor"].tolist()
    highs = df["high_yield"].tolist()

    cmt_close, tail_bps, cmt_asof, cmt_lag = [], [], [], []
    for ad, t, hy in zip(dates, tenors, highs):
        c, asof, lag = _cmt_for(cmt[t], ad) if t in cmt else (None, None, None)
        cmt_close.append(c)
        cmt_asof.append(asof)
        cmt_lag.append(lag)
        if c is None or pd.isna(hy):
            tail_bps.append(None)
        else:
            tail_bps.append(round((float(hy) - c) * 100, 1))
    df["cmt_close_prior_day"] = cmt_close
    # FIX 2026-08-18: cmt_asof / cmt_lag_days make the fallback VISIBLE. Without
    # them a same-day close and a stale one are indistinguishable in the file.
    df["cmt_asof"] = cmt_asof
    df["cmt_lag_days"] = cmt_lag
    df["tail_vs_cmt_bps"] = tail_bps

    pda = pd.to_numeric(df["primary_dealer_accepted"], errors="coerce").fillna(0)
    dba = pd.to_numeric(df["direct_bidder_accepted"], errors="coerce").fillna(0)
    iba = pd.to_numeric(df["indirect_bidder_accepted"], errors="coerce")
    comp = pda + dba + iba.fillna(0)
    df["total_competitive_accepted"] = comp
    df["indirect_pct_of_competitive"] = ((iba / comp.where(comp > 0)) * 100).round(1)
    return df


# --- write-safety helpers (added 2026-08-18 after DAEDALUS SFG sweep) --------

REQUIRED_V1 = [
    "auction_date", "tenor", "security_type", "cusip", "offering_amt",
    "total_accepted", "high_yield", "bid_to_cover_ratio",
    "primary_dealer_accepted", "direct_bidder_accepted",
    "indirect_bidder_accepted",
]
REQUIRED_V2_EXTRA = [
    "cmt_close_prior_day", "cmt_asof", "cmt_lag_days", "tail_vs_cmt_bps",
    "total_competitive_accepted", "indirect_pct_of_competitive",
]
# A refresh may legitimately ADD rows; it may never lose more than a hair.
MIN_ROW_RATIO = 0.95


def _validate_or_die(df: pd.DataFrame, target: Path, label: str, required: list[str]) -> None:
    """Refuse to write if the frame is empty, missing columns, or has shrunk.

    This is the guard whose absence made a documented empty-200 response
    DESTRUCTIVE rather than merely annoying.
    """
    if df is None or df.empty:
        raise SystemExit(
            f"[refresh] ABORT: {label} frame is EMPTY. Refusing to overwrite {target}. "
            "This is the documented empty-200 path (a bad `fields=` projection returns "
            "HTTP 200 with zero rows) -- the existing file is INTACT."
        )
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise SystemExit(
            f"[refresh] ABORT: {label} frame missing required columns {missing}. "
            f"Refusing to overwrite {target}; existing file is INTACT."
        )
    if target.exists():
        try:
            prior = sum(1 for _ in open(target, encoding="utf-8")) - 1
        except OSError:
            prior = 0
        if prior > 0 and len(df) < prior * MIN_ROW_RATIO:
            raise SystemExit(
                f"[refresh] ABORT: {label} would SHRINK {target} from {prior} to {len(df)} rows "
                f"(< {MIN_ROW_RATIO:.0%}). Refusing. If this shrink is intended, delete the file "
                "deliberately and re-run -- do not weaken this guard."
            )
    print(f"[refresh] {label} validated: {len(df)} rows, {len(df.columns)} cols")


def _atomic_write(df: pd.DataFrame, target: Path, label: str) -> None:
    """Write via .tmp + os.replace so a crash mid-write cannot truncate the file."""
    tmp = target.with_suffix(target.suffix + ".tmp")
    df.to_csv(tmp, index=False)
    os.replace(tmp, target)
    print(f"[refresh] wrote {label} -> {target} ({len(df)} rows)")


def main() -> int:
    print(f"[refresh] pulling {START_DATE} -> {END_DATE} from FiscalData...")
    raw = fetch_all()
    print(f"[refresh] raw rows: {len(raw)}")
    out = transform(raw)
    print(f"[refresh] filtered rows (coupon notes/bonds, target tenors, with results): {len(out)}")
    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)

    # v2: enrich FIRST, so a failure in enrichment cannot leave a half-written pair.
    print("[refresh] fetching FRED CMT series for v2 enrichment...")
    cmt = build_cmt_lookup()
    out_v2 = enrich_v2(out, cmt)

    # FIX 2026-08-18 (DAEDALUS defect 2 -- the destructive one): this function
    # previously called out.to_csv(OUTPUT_CSV) BEFORE any validation. The file's
    # own docstring warns that a bad `fields=` projection returns HTTP 200 with
    # ZERO rows; that path overwrote a good 370-row corpus with a header-only
    # file and THEN raised a confusing KeyError in enrich_v2. Data destroyed
    # first, error reported second. Now: validate -> .tmp -> os.replace.
    _validate_or_die(out, OUTPUT_CSV, "v1", REQUIRED_V1)
    _validate_or_die(out_v2, OUTPUT_CSV_V2, "v2", REQUIRED_V1 + REQUIRED_V2_EXTRA)
    _atomic_write(out, OUTPUT_CSV, "v1")
    _atomic_write(out_v2, OUTPUT_CSV_V2, "v2")

    # Quick sanity print.
    if not out.empty:
        by_tenor = out.groupby("tenor").size().to_dict()
        print(f"[refresh] rows per tenor: {by_tenor}")
        print(f"[refresh] latest auction in file: {out['auction_date'].max()}")
        tail_n = out_v2["tail_vs_cmt_bps"].notna().sum()
        ipc_n = out_v2["indirect_pct_of_competitive"].notna().sum()
        print(f"[refresh] v2 tail_vs_cmt_bps non-null: {tail_n}/{len(out_v2)}")
        print(f"[refresh] v2 indirect_pct_of_competitive non-null: {ipc_n}/{len(out_v2)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
