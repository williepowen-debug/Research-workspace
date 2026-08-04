#!/usr/bin/env python3
"""
SAM Japan CPI Monitor
Fetches Japan CPI (National + Tokyo Ku-area) via the e-Stat API and emits
a two-table threshold read against the BOJ rate-pricing thesis.

Source: e-Stat API v3 (api.e-stat.go.jp/rest/3.0/app/json/getStatsData)
        Statistics Bureau of Japan; 2020-base CPI; statsDataId 0003427113
        Requires ESTAT_APPID (free registration; loaded from repo-root .env).

Series tracked (cat01 codes):
  0001  Headline (All items) YoY %
  0161  Core (All items, less fresh food) YoY %   ← BOJ policy target
  0178  Core-core (less fresh food and energy) YoY %  ← Trend gauge

Areas: 00000 = All Japan, 13A01 = Ku-area of Tokyo

Thresholds (per Will spec 2026-05-26):

  Core (BOJ target series):
    <1.2%      🔴 Deep miss; June pricing collapses (<30%)
    1.2-1.5%   🟠 Soft band; pricing biased lower
    1.5-1.8%   🟡 In-line; pricing stable
    ≥1.8%      🟢 Toward consensus; pricing firms toward 70%+

  Core-core (trend gauge):
    <1.5%      🔴 Dovish trajectory broken; June pricing collapses
    1.5-1.8%   🟠 CALENDAR <1.9% threshold tripped
    1.8-2.1%   🟡 Sticky; no new signal
    ≥2.2%      🟢 Hawkish anchor / re-accelerating

Cross-series divergence:
  core_core − core ≥ 0.5pp  → energy/subsidy-driven softness; BOJ can look through
  core_core − core ≤ 0.2pp  → broad-based softening; less BOJ cover to hike

Tokyo runs ~30-40bp below National across the board; bands above are calibrated
to National. For Tokyo prints the script applies the same buckets and adds a
comparison-to-National footer so it doesn't false-positive a Tokyo soft print
as hawkish in absolute terms.

Usage:
  .venv/bin/python3 AGENTS/SAM/scripts/cpi_japan.py
  .venv/bin/python3 AGENTS/SAM/scripts/cpi_japan.py --refresh  # API pull only
  .venv/bin/python3 AGENTS/SAM/scripts/cpi_japan.py --summary  # cached read only
  .venv/bin/python3 AGENTS/SAM/scripts/cpi_japan.py --months 6 # show last N
"""

import os
import sys
import json
import urllib.request
import urllib.error
from datetime import date, datetime
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
SAM_DIR = SCRIPTS_DIR.parent
WORKSPACE = SAM_DIR.parent.parent
WORKBOOK = SAM_DIR / "workbook"
CPI_TSV = WORKBOOK / "CPI.tsv"
ENV_FILE = WORKSPACE / ".env"

API_URL = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"
STATS_DATA_ID = "0003427113"  # 2020-base CPI database

AREA_NATIONAL = "00000"
AREA_TOKYO = "13A01"
CAT_HEADLINE = "0001"
CAT_CORE = "0161"
CAT_CORECORE = "0178"
TAB_YOY = "3"  # Change over the year

TSV_HEADER = "Pulled_Date\tSeries\tReference_Month\tHeadline\tCore\tCoreCore\n"


def load_env():
    """Read .env at repo root if ESTAT_APPID not already in os.environ."""
    if os.environ.get("ESTAT_APPID"):
        return
    if not ENV_FILE.exists():
        return
    with open(ENV_FILE) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())


def time_code(ref_month: date) -> str:
    """e-Stat time code: YYYYMMmm format encoded as 10 chars.
    e.g., Apr 2026 → 2026000404."""
    return f"{ref_month.year}{ref_month.month:04d}{ref_month.month:02d}"


def fetch_series(area_code, from_month, to_month):
    """Fetch headline + core + core-core YoY for an area over a month range.
    Returns dict {ref_month_str: {headline, core, core_core}} or {} on failure."""
    appid = os.environ.get("ESTAT_APPID")
    if not appid:
        print("  ⚠️  ESTAT_APPID not set (check repo-root .env)")
        return {}

    params = {
        "appId": appid,
        "statsDataId": STATS_DATA_ID,
        "cdTab": TAB_YOY,
        "cdArea": area_code,
        "cdCat01": f"{CAT_HEADLINE},{CAT_CORE},{CAT_CORECORE}",
        "cdTimeFrom": time_code(from_month),
        "cdTimeTo": time_code(to_month),
        "lang": "E",
        "metaGetFlg": "N",
    }
    query = "&".join(f"{k}={v}" for k, v in params.items())
    url = f"{API_URL}?{query}"

    try:
        req = urllib.request.Request(url)
        # 8s (not 30s): e-Stat normally answers in ~1-2s. Two calls (National +
        # Tokyo) must finish well under boot.py's 60s per-script ceiling so the
        # graceful cached-TSV fallback can run when the API is transiently slow.
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read())
    except urllib.error.URLError as e:
        print(f"  ⚠️  e-Stat fetch failed: {e}")
        return {}
    except Exception as e:
        print(f"  ⚠️  e-Stat parse failed: {e}")
        return {}

    result = data.get("GET_STATS_DATA", {})
    if result.get("RESULT", {}).get("STATUS") != 0:
        err = result.get("RESULT", {}).get("ERROR_MSG", "unknown")
        print(f"  ⚠️  e-Stat API error: {err}")
        return {}

    values = result.get("STATISTICAL_DATA", {}).get("DATA_INF", {}).get("VALUE", [])
    if not isinstance(values, list):
        values = [values]

    # time format 2026000404 → YYYYMM string '2026-04'
    cat_to_field = {CAT_HEADLINE: "headline", CAT_CORE: "core", CAT_CORECORE: "core_core"}
    out = {}
    for v in values:
        tcode = v.get("@time", "")
        if len(tcode) != 10:
            continue
        year = tcode[:4]
        month = tcode[6:8]
        ref = f"{year}-{month}"
        field = cat_to_field.get(v.get("@cat01"))
        if not field:
            continue
        try:
            val = float(v.get("$"))
        except (ValueError, TypeError):
            val = None
        out.setdefault(ref, {})[field] = val
    return out


def load_tsv():
    if not CPI_TSV.exists():
        return []
    rows = []
    with open(CPI_TSV) as f:
        next(f, None)
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if len(parts) >= 6:
                rows.append({
                    "pulled": parts[0],
                    "series": parts[1],
                    "ref_month": parts[2],
                    "headline": float(parts[3]) if parts[3] else None,
                    "core": float(parts[4]) if parts[4] else None,
                    "core_core": float(parts[5]) if parts[5] else None,
                })
    return rows


def append_tsv(series_name, by_month):
    """Append new (series, ref_month) rows. Idempotent."""
    existing = set()
    if CPI_TSV.exists():
        with open(CPI_TSV) as f:
            next(f, None)
            for line in f:
                parts = line.strip().split("\t")
                if len(parts) >= 3:
                    existing.add((parts[1], parts[2]))
    else:
        with open(CPI_TSV, "w") as f:
            f.write(TSV_HEADER)

    today_str = date.today().isoformat()
    appended = 0
    with open(CPI_TSV, "a") as f:
        for ref_month in sorted(by_month.keys()):
            if (series_name, ref_month) in existing:
                continue
            vals = by_month[ref_month]
            h = vals.get("headline")
            c = vals.get("core")
            cc = vals.get("core_core")
            if h is None and c is None and cc is None:
                continue
            f.write(
                f"{today_str}\t{series_name}\t{ref_month}\t"
                f"{h if h is not None else ''}\t"
                f"{c if c is not None else ''}\t"
                f"{cc if cc is not None else ''}\n"
            )
            appended += 1
    return appended


def classify_core(v):
    if v is None:
        return "  ", "n/a"
    if v < 1.2:
        return "🔴", "Deep miss"
    if v < 1.5:
        return "🟠", "Soft band"
    if v < 1.8:
        return "🟡", "In-line"
    return "🟢", "Toward consensus"


def classify_core_core(v):
    if v is None:
        return "  ", "n/a"
    if v < 1.5:
        return "🔴", "Dovish broken"
    if v < 1.8:
        return "🟠", "CALENDAR trigger"
    if v < 2.2:
        return "🟡", "Sticky"
    return "🟢", "Hawkish anchor"


def divergence_note(core, core_core):
    if core is None or core_core is None:
        return ""
    gap = core_core - core
    if gap >= 0.5:
        return f"gap +{gap:.1f}pp → energy/subsidy-driven (BOJ can look through)"
    if gap <= 0.2:
        return f"gap +{gap:.1f}pp → broad-based softening (less BOJ cover)"
    return f"gap +{gap:.1f}pp"


def print_summary_for(series_name, by_month):
    """Print latest print for a series + divergence + bucket markers."""
    if not by_month:
        print(f"  ⚪ {series_name}: no data returned (current month likely not published yet)")
        return None
    latest_ref = max(by_month.keys())
    vals = by_month[latest_ref]
    h = vals.get("headline")
    c = vals.get("core")
    cc = vals.get("core_core")
    core_m, core_label = classify_core(c)
    cc_m, cc_label = classify_core_core(cc)
    dnote = divergence_note(c, cc)
    h_str = f"{h:.1f}" if h is not None else "n/a"
    c_str = f"{c:.1f}" if c is not None else "n/a"
    cc_str = f"{cc:.1f}" if cc is not None else "n/a"
    print(f"  {core_m} {series_name} {latest_ref}: headline {h_str} | core {c_str} ({core_label}) | core-core {cc_str} ({cc_label}) | {dnote}")
    return vals


def print_comparison_note(nat_latest, tok_latest):
    """If both series available for same month or adjacent months,
    print the National-vs-Tokyo comparison line."""
    if not nat_latest or not tok_latest:
        return
    n_cc = nat_latest.get("core_core")
    t_cc = tok_latest.get("core_core")
    if n_cc is None or t_cc is None:
        return
    diff = t_cc - n_cc
    # Tokyo running below National by ~30-40bp historically; flag if it inverts
    if diff < -0.2:
        note = f"Tokyo {diff:+.1f}pp below National core-core — expected pattern (~30-40bp gap)"
    elif diff > 0.1:
        note = f"⚠️ Tokyo {diff:+.1f}pp ABOVE National core-core — pattern inverted, leading-indicator hawkish"
    else:
        note = f"Tokyo gap {diff:+.1f}pp — narrower than typical 30-40bp; Tokyo softness may be closing"
    print(f"  ℹ️  {note}. (CALENDAR <1.9% trigger applies as <1.95% for Tokyo.)")



def _report_staleness():
    """Say how stale CPI.tsv is when we cannot refresh it.

    A broken fetcher that only reports "credential missing" understates the damage —
    the durable harm is the workbook drifting behind published releases while every
    other surface looks current. Best-effort and never raises: this runs on a path
    that is already failing.
    """
    try:
        from datetime import date
        rows = [l.split("\t") for l in
                CPI_TSV.read_text(encoding="utf-8").rstrip("\n").split("\n")[1:] if l.strip()]
        if not rows:
            print("  🔴 CPI.tsv is EMPTY — no CPI history at all.")
            return
        latest = {}
        for r in rows:
            if len(r) >= 3:
                latest[r[1]] = max(latest.get(r[1], ""), r[2])   # series -> max ref month
        print("  🔴 CPI.tsv CANNOT REFRESH — and it is drifting behind published releases:")
        for series, ref in sorted(latest.items()):
            try:
                y, m = (int(x) for x in ref.split("-")[:2])
                months = (date.today().year - y) * 12 + (date.today().month - m)
            except ValueError:
                months = "?"
            print(f"       {series:<9} latest reference month {ref}  (~{months} months behind today)")
        print("       ⚠️  STATUS may carry newer figures by hand — that is the trap: the")
        print("           workbook looks maintained because another surface is current.")
        print("       → set ESTAT_APPID (free e-Stat registration) in the repo-root .env")
    except Exception as exc:                                       # noqa: BLE001
        print(f"  (staleness check unavailable: {exc})")


def main():
    load_env()
    refresh_only = "--refresh" in sys.argv
    summary_only = "--summary" in sys.argv
    months_back = 6
    if "--months" in sys.argv:
        i = sys.argv.index("--months")
        if i + 1 < len(sys.argv):
            try:
                months_back = max(1, int(sys.argv[i + 1]))
            except ValueError:
                pass

    now = datetime.now()
    print(f"\n{'='*70}")
    print(f"  SAM Japan CPI Monitor — {now.strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*70}\n")

    # Fetch window: last `months_back` months back from current month
    today = now.date()
    # Walk back to first of month, then back N more months
    first_of_current = today.replace(day=1)
    from_year = first_of_current.year
    from_month = first_of_current.month - months_back
    while from_month < 1:
        from_month += 12
        from_year -= 1
    from_d = date(from_year, from_month, 1)
    to_d = first_of_current

    nat_data = {}
    tok_data = {}

    if not summary_only:
        if not os.environ.get("ESTAT_APPID"):
            print(f"  ⚠️  ESTAT_APPID not set (looked in env + {ENV_FILE})")
            # A credential failure used to end here — which made the REAL cost invisible:
            # the fetch stops, but CPI.tsv silently ROTS while STATUS keeps carrying the
            # figures by hand, so the workbook looks maintained and is not. Found 2026-08-04
            # via KB-169 (tsv was ~6 weeks stale, missing 2 published releases, unnoticed).
            # Report the staleness the credential is causing, not just the credential.
            _report_staleness()
            return 1
        nat_data = fetch_series(AREA_NATIONAL, from_d, to_d)
        tok_data = fetch_series(AREA_TOKYO, from_d, to_d)
        n_app = append_tsv("National", nat_data)
        t_app = append_tsv("Tokyo", tok_data)
        total = n_app + t_app
        if total > 0:
            print(f"  ✓ Appended {total} new row(s) to CPI.tsv ({n_app} National, {t_app} Tokyo)")
        else:
            print(f"  ✓ CPI.tsv up to date (no new prints)")

    if refresh_only:
        print()
        return 0

    # If we fetched, we have nat_data/tok_data in memory. Otherwise reload from TSV.
    if not nat_data and not tok_data:
        all_rows = load_tsv()
        if not all_rows:
            print(f"  ⚠️  CPI.tsv empty — run without --summary first")
            return 1
        # Re-bucket for display
        for r in all_rows:
            target = nat_data if r["series"] == "National" else tok_data
            target[r["ref_month"]] = {
                "headline": r["headline"], "core": r["core"], "core_core": r["core_core"]
            }

    print()
    nat_latest = print_summary_for("National", nat_data)
    tok_latest = print_summary_for("Tokyo   ", tok_data)
    print_comparison_note(nat_latest, tok_latest)

    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
