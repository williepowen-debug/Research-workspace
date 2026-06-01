#!/usr/bin/env python3
"""VIOLET CFTC COT — VIX futures positioning from the TFF report.

Source: CFTC Traders in Financial Futures (TFF) report. VIX futures contract:
"VIX FUTURES - CBOE FUTURES EXCHANGE" (code 1170E1).

Latest weekly text:
  https://www.cftc.gov/dea/newcot/FinFutWk.txt              (no header, all contracts, current week)
Historical annual zips (with CSV header):
  https://www.cftc.gov/files/dea/history/fut_fin_txt_YYYY.zip

Output: workbook/COT_VIX.tsv — one row per Tuesday report date with
positions, NETs, 3yr rolling percentiles for the three speculator categories
(lev_money, dealer, asset_mgr), and a flag derived from lev_money_net_pct3y.

Usage:
  .venv/bin/python3 AGENTS/VIOLET/scripts/cftc_cot.py             # fetch latest, append if new
  .venv/bin/python3 AGENTS/VIOLET/scripts/cftc_cot.py --backfill  # rebuild from 2023-current annual zips
  .venv/bin/python3 AGENTS/VIOLET/scripts/cftc_cot.py --summary   # print latest reading, no fetch
  .venv/bin/python3 AGENTS/VIOLET/scripts/cftc_cot.py --boot      # freshness-gated: fetch only if local stale
"""
from __future__ import annotations

import argparse
import csv
import io
import sys
import zipfile
from datetime import date, datetime, timedelta
from pathlib import Path

import requests

SCRIPT_DIR = Path(__file__).resolve().parent
VIOLET_DIR = SCRIPT_DIR.parent
COT_TSV = VIOLET_DIR / "workbook" / "COT_VIX.tsv"

WEEKLY_URL = "https://www.cftc.gov/dea/newcot/FinFutWk.txt"
ANNUAL_URL = "https://www.cftc.gov/files/dea/history/fut_fin_txt_{year}.zip"

VIX_MARKET_NAME = "VIX FUTURES - CBOE FUTURES EXCHANGE"
VIX_CONTRACT_CODE = "1170E1"

# TFF column indices (0-based) — same field order in both weekly and annual zip
COL_MARKET_NAME = 0
COL_REPORT_DATE = 2          # "YYYY-MM-DD"
COL_CONTRACT_CODE = 3
COL_OPEN_INTEREST = 7
COL_DEALER_LONG = 8
COL_DEALER_SHORT = 9
COL_ASSET_MGR_LONG = 11
COL_ASSET_MGR_SHORT = 12
COL_LEV_MONEY_LONG = 14
COL_LEV_MONEY_SHORT = 15
COL_OTHER_LONG = 17
COL_OTHER_SHORT = 18
COL_NONREPT_LONG = 22
COL_NONREPT_SHORT = 23

OUTPUT_HEADER = [
    "report_date",
    "open_interest",
    "dealer_long", "dealer_short", "dealer_net",
    "asset_mgr_long", "asset_mgr_short", "asset_mgr_net",
    "lev_money_long", "lev_money_short", "lev_money_net",
    "other_long", "other_short", "other_net",
    "nonrept_long", "nonrept_short", "nonrept_net",
    "lev_money_net_pct3y",
    "dealer_net_pct3y",
    "asset_mgr_net_pct3y",
    "flag",
]

ROLLING_WEEKS = 156   # 3yr × 52 weeks
MIN_WEEKS_FOR_PCT = 26  # 6 months minimum before computing pct


def parse_row(fields: list[str]) -> dict | None:
    """Parse one CSV row; return dict for VIX or None."""
    if len(fields) < 25:
        return None
    # Strip quotes from market name
    name = fields[COL_MARKET_NAME].strip().strip('"')
    code = fields[COL_CONTRACT_CODE].strip()
    if name != VIX_MARKET_NAME and code != VIX_CONTRACT_CODE:
        return None
    try:
        out = {
            "report_date": fields[COL_REPORT_DATE].strip(),
            "open_interest": int(fields[COL_OPEN_INTEREST]),
            "dealer_long": int(fields[COL_DEALER_LONG]),
            "dealer_short": int(fields[COL_DEALER_SHORT]),
            "asset_mgr_long": int(fields[COL_ASSET_MGR_LONG]),
            "asset_mgr_short": int(fields[COL_ASSET_MGR_SHORT]),
            "lev_money_long": int(fields[COL_LEV_MONEY_LONG]),
            "lev_money_short": int(fields[COL_LEV_MONEY_SHORT]),
            "other_long": int(fields[COL_OTHER_LONG]),
            "other_short": int(fields[COL_OTHER_SHORT]),
            "nonrept_long": int(fields[COL_NONREPT_LONG]),
            "nonrept_short": int(fields[COL_NONREPT_SHORT]),
        }
        for cat in ("dealer", "asset_mgr", "lev_money", "other", "nonrept"):
            out[f"{cat}_net"] = out[f"{cat}_long"] - out[f"{cat}_short"]
        return out
    except (ValueError, IndexError):
        return None


def fetch_weekly() -> dict | None:
    """Latest week. Single VIX row expected."""
    r = requests.get(WEEKLY_URL, timeout=30,
                     headers={"User-Agent": "Mozilla/5.0 VIOLET/cftc_cot"})
    r.raise_for_status()
    reader = csv.reader(io.StringIO(r.text))
    for fields in reader:
        row = parse_row(fields)
        if row is not None:
            return row
    return None


def fetch_annual(year: int) -> list[dict]:
    """All VIX rows for a given year (one per Tuesday)."""
    url = ANNUAL_URL.format(year=year)
    r = requests.get(url, timeout=60,
                     headers={"User-Agent": "Mozilla/5.0 VIOLET/cftc_cot"})
    r.raise_for_status()
    with zipfile.ZipFile(io.BytesIO(r.content)) as zf:
        names = zf.namelist()
        if not names:
            return []
        with zf.open(names[0]) as f:
            text = io.TextIOWrapper(f, encoding="utf-8", errors="replace")
            reader = csv.reader(text)
            out = []
            for i, fields in enumerate(reader):
                if i == 0:
                    continue  # header
                row = parse_row(fields)
                if row is not None:
                    out.append(row)
    return out


def percentile_rank(value: float, window: list[float]) -> float | None:
    """Percentile rank of value within window (inclusive). 0-100 scale."""
    if len(window) < MIN_WEEKS_FOR_PCT:
        return None
    below = sum(1 for x in window if x < value)
    equal = sum(1 for x in window if x == value)
    return round((below + 0.5 * equal) / len(window) * 100, 1)


def flag_from_pct(pct: float | None) -> str:
    """Categorical flag based on lev_money_net_pct3y."""
    if pct is None:
        return ""
    if pct >= 90:
        return "EXTREME_LONG"
    if pct >= 75:
        return "ELEVATED_LONG"
    if pct <= 10:
        return "EXTREME_SHORT"
    if pct <= 25:
        return "ELEVATED_SHORT"
    return "NORMAL"


def compute_all_percentiles(rows: list[dict]) -> None:
    """Mutate rows in place — add pct3y columns + flag."""
    rows.sort(key=lambda r: r["report_date"])
    for i, row in enumerate(rows):
        # Trailing window: prior ROLLING_WEEKS rows (exclusive of current)
        start = max(0, i - ROLLING_WEEKS)
        for cat in ("lev_money", "dealer", "asset_mgr"):
            key = f"{cat}_net"
            window = [r[key] for r in rows[start:i]]
            row[f"{key}_pct3y"] = percentile_rank(row[key], window)
        row["flag"] = flag_from_pct(row["lev_money_net_pct3y"])


def load_existing() -> dict[str, dict]:
    """Return {report_date: row}."""
    if not COT_TSV.exists():
        return {}
    with open(COT_TSV) as f:
        reader = csv.DictReader(f, delimiter="\t")
        return {r["report_date"]: r for r in reader if r.get("report_date")}


def write_tsv(rows: list[dict]) -> None:
    rows.sort(key=lambda r: r["report_date"])
    with open(COT_TSV, "w") as f:
        f.write("\t".join(OUTPUT_HEADER) + "\n")
        for r in rows:
            f.write("\t".join(str(r.get(c, "") if r.get(c) is not None else "") for c in OUTPUT_HEADER) + "\n")


def print_summary(rows: list[dict]) -> None:
    if not rows:
        print("No data.")
        return
    last = rows[-1]
    print(f"\nLatest COT VIX positioning ({last['report_date']}):")
    print(f"  Open Interest: {last['open_interest']:,}")
    print(f"  {'Category':<14}{'Long':>10}{'Short':>10}{'Net':>10}{'pct3y':>8}")
    for cat, label in [("dealer", "Dealer"), ("asset_mgr", "Asset Mgr"), ("lev_money", "Lev Money"), ("other", "Other"), ("nonrept", "NonRept")]:
        pct = last.get(f"{cat}_net_pct3y", "")
        pct_str = f"{pct}" if pct != "" and pct is not None else ""
        print(f"  {label:<14}{last[f'{cat}_long']:>10,}{last[f'{cat}_short']:>10,}{last[f'{cat}_net']:>+10,}{pct_str:>8}")
    flag = last.get("flag", "")
    if flag and flag != "NORMAL":
        print(f"  FLAG: {flag} (lev_money pct3y={last.get('lev_money_net_pct3y')})")
    else:
        print(f"  flag: {flag or 'NORMAL'}")


def coerce_int(v):
    if v in ("", None):
        return None
    try:
        return int(v)
    except (ValueError, TypeError):
        try:
            return int(float(v))
        except (ValueError, TypeError):
            return None


def normalize_loaded(rows: dict[str, dict]) -> list[dict]:
    """Coerce TSV string values back to int for percentile math."""
    out = []
    for d, r in rows.items():
        nr = {"report_date": d}
        for col in OUTPUT_HEADER:
            if col == "report_date":
                continue
            if col == "flag":
                nr[col] = r.get(col, "")
            elif col.endswith("_pct3y"):
                try:
                    nr[col] = float(r.get(col)) if r.get(col) not in ("", None) else None
                except ValueError:
                    nr[col] = None
            else:
                nr[col] = coerce_int(r.get(col))
        out.append(nr)
    return out


def expected_latest_report_date(today: date) -> date:
    """Most recent Tuesday whose Friday-publish has passed.

    CFTC TFF releases Friday 3:30 PM ET for the prior Tuesday close.
    If today is Mon-Thu, latest available is Tuesday of LAST week.
    If today is Friday before 3:30 PM ET, also Tuesday of LAST week.
    If today is Fri after 3:30 PM ET / Sat / Sun, Tuesday of THIS week.
    We don't track hours here — treat Fri/Sat/Sun as "current week available."
    """
    # weekday(): Mon=0, Tue=1, ..., Sun=6
    wd = today.weekday()
    if wd >= 4:  # Fri/Sat/Sun
        # Most recent Tuesday is in current week
        days_since_tue = (wd - 1) % 7
        return today - timedelta(days=days_since_tue)
    # Mon-Thu: use prior week's Tuesday
    days_since_tue = (wd - 1) % 7
    last_tue = today - timedelta(days=days_since_tue)
    return last_tue - timedelta(days=7)


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--backfill", action="store_true", help="Rebuild from 2023→present annual zips")
    p.add_argument("--summary", action="store_true", help="Print latest, no fetch")
    p.add_argument("--boot", action="store_true", help="Freshness-gated: fetch only if local data is stale")
    args = p.parse_args(argv)

    if args.boot:
        existing = load_existing()
        if not existing:
            print(f"COT VIX: no local data. Run --backfill first.")
            return 1
        latest_local = max(existing.keys())
        expected = expected_latest_report_date(date.today()).isoformat()
        if latest_local >= expected:
            rows = normalize_loaded(existing)
            print_summary(rows)
            return 0
        # Stale — fall through to default fetch path
        print(f"COT VIX: local data ({latest_local}) older than expected ({expected}); fetching latest...")
        args.backfill = False
        args.summary = False
        # fall through

    if args.summary:
        existing = load_existing()
        if not existing:
            print(f"No existing data at {COT_TSV}. Run --backfill first.")
            return 1
        rows = normalize_loaded(existing)
        print_summary(rows)
        return 0

    if args.backfill:
        print(f"Backfilling CFTC TFF VIX history {2023}→{date.today().year}...")
        rows = []
        for year in range(2023, date.today().year + 1):
            print(f"  Fetching {year}...", end=" ", flush=True)
            try:
                year_rows = fetch_annual(year)
                rows.extend(year_rows)
                print(f"{len(year_rows)} weeks")
            except requests.HTTPError as e:
                print(f"FAILED ({e})")
        # Dedupe by report_date (keep latest if duplicates)
        by_date = {r["report_date"]: r for r in rows}
        rows = list(by_date.values())
        compute_all_percentiles(rows)
        write_tsv(rows)
        print(f"\n✓ wrote {len(rows)} rows to {COT_TSV}")
        print_summary(rows)
        return 0

    # Default: fetch latest week, append if new
    existing = load_existing()
    print(f"Fetching latest week from CFTC...")
    latest = fetch_weekly()
    if latest is None:
        print("  ✗ no VIX row found in weekly file")
        return 1
    print(f"  latest report_date: {latest['report_date']}")
    if latest["report_date"] in existing:
        print(f"  (already in {COT_TSV.name})")
    else:
        existing[latest["report_date"]] = {**latest, **{c: "" for c in OUTPUT_HEADER if c not in latest}}
        print(f"  + new row appended")
    rows = normalize_loaded(existing)
    # If the new row was added, latest_normalized hasn't seen it processed; rebuild
    if latest["report_date"] not in {r["report_date"] for r in rows}:
        rows.append(latest)
    compute_all_percentiles(rows)
    write_tsv(rows)
    print_summary(rows)
    return 0


if __name__ == "__main__":
    sys.exit(main())
