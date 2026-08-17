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
# Credential homes, searched in order.
# ⚠️ The fleet's SINGLE HOME for API keys is FORGE/tools/market-data/.env (PROME
# MACHINE_LOCAL.md: FRED, PJM, EIA all live there; "two homes = rotation drift").
# This script originally read ONLY the repo-root .env, which is why ESTAT_APPID was
# left behind when the 2026-07-01..04 credential cleanup re-homed the other three keys
# — CPI's last successful pull was 6/29, immediately before that window, and the gap
# went unnoticed for ~5 weeks. Read BOTH, fleet home first, so the key can live in one
# place with everything else. (Class: [[finding_unversioned_local_secret_fails_silently]])
ENV_FILES = [
    WORKSPACE / "FORGE" / "tools" / "market-data" / ".env",   # fleet single home
    WORKSPACE / ".env",                                        # legacy/local fallback
]
ENV_FILE = ENV_FILES[0]   # kept for message text; see load_env() for the real search

API_URL = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

# ---------------------------------------------------------------------------
# BASE REGISTRY — 2025-base rebasing, live-verified against the API 2026-08-17.
#
# Japan's CPI was rebased 2020 → 2025 (the 17th revision). Statistics Bureau, own
# primary (stat.go.jp/english/data/cpi/2025plan.html): "We will begin to release the
# 2025-base CPI in August 2026" and — the part that matters operationally —
# "The 2020-base CPI will also be calculated and released until December 2026."
# ⇒ BOTH bases are live until Dec-2026. Nothing breaks on 8/21; what changes is
# WHICH BASIS a number is on, and the two do NOT agree.
#
# ⚠️ TWO parameters move between bases, not one. The second is the dangerous one:
#   statsDataId  0003427113 → 0004052037
#   cdArea Tokyo 13A01      → 13100        ← silently returns "no data" if not changed
# cdArea national (00000), cdTab (3 = 前年同月比) and all three cdCat01 codes
# (0001 総合 / 0161 生鮮食品を除く総合 / 0178 生鮮食品及びエネルギーを除く総合) are UNCHANGED —
# each binding read off both tables' own metadata, then confirmed live.
#
# Live probe 2026-08-17 (the verification, not an inference):
#   2020-base: 00000 OK · 13A01 OK · 13100 → "no data"
#   2025-base: 00000 OK · 13A01 → "no data" · 13100 OK
#   National 2026-06 headline: 1.7 on 2020-base vs 1.6 on 2025-base
# ⚠️ THAT 0.1pp IS THE DISCONTINUITY, MEASURED. Never difference across bases.
#
# ⚠️ e-Stat returns STATUS=1 "successfully completed, but there was no data" for a
# stale area code — a SUCCESS-shaped response carrying nothing. That is why the
# area code is registry-driven here and why fetch_series refuses to write on an
# empty result rather than degrading quietly.
# ---------------------------------------------------------------------------
BASES = {
    "2025": {
        "stats_data_id": "0004052037",   # 2025年基準消費者物価指数1 消費者物価指数（2025年基準）
        "area_national": "00000",
        "area_tokyo": "13100",
        "label": "2025-base",
        # Retroactive coverage starts Jan-2025 (e-Stat loaded it 2026-08-07);
        # the first NEW monthly print on this base is National July, due 2026-08-21.
        "starts": "2025-01",
    },
    "2020": {
        "stats_data_id": "0003427113",   # 2020年基準消費者物価指数1 消費者物価指数（2020年基準）
        "area_national": "00000",
        "area_tokyo": "13A01",
        "label": "2020-base",
        "starts": "2020-01",
        # Published in parallel until Dec-2026, then retired.
        "retires": "2026-12",
    },
}
DEFAULT_BASE = "2025"

# Mutated by main() per --base; defaults to the live base.
BASE_KEY = DEFAULT_BASE
STATS_DATA_ID = BASES[DEFAULT_BASE]["stats_data_id"]
AREA_NATIONAL = BASES[DEFAULT_BASE]["area_national"]
AREA_TOKYO = BASES[DEFAULT_BASE]["area_tokyo"]

CAT_HEADLINE = "0001"      # 総合                       — unchanged across bases
CAT_CORE = "0161"          # 生鮮食品を除く総合            — unchanged across bases
CAT_CORECORE = "0178"      # 生鮮食品及びエネルギーを除く総合 — unchanged across bases
TAB_YOY = "3"  # Change over the year (前年同月比) — unchanged across bases

# `Base` column added 2026-08-17. Without it the 2020-base rows already on disk and
# the incoming 2025-base rows are indistinguishable, and a 0.1pp basis shift reads as
# a data move. Legacy rows (6 columns, no Base) are stamped 2020-base on read.
TSV_HEADER = "Pulled_Date\tSeries\tReference_Month\tHeadline\tCore\tCoreCore\tBase\n"


def load_env():
    """Load ESTAT_APPID from the first .env that defines it (fleet home first)."""
    if os.environ.get("ESTAT_APPID"):
        return
    for env_path in ENV_FILES:
        if not env_path.exists():
            continue
        try:
            with open(env_path) as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    if "=" in line:
                        k, v = line.split("=", 1)
                        os.environ.setdefault(k.strip(), v.strip())
        except OSError:
            continue
        if os.environ.get("ESTAT_APPID"):
            return


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
        "statsDataId": BASES[BASE_KEY]["stats_data_id"],
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
        # ⚠️ STATUS=1 "successfully completed, but there was no data" is what a STALE
        # AREA CODE returns — a success-shaped answer carrying nothing. It is the exact
        # signature of the 13A01→13100 rebasing change, so name that hypothesis here
        # rather than leaving a future reader to rediscover it.
        if "no data" in str(err).lower():
            print(f"      ↳ 🔴 EMPTY RESULT for cdArea={area_code} on "
                  f"{BASES[BASE_KEY]['label']} (statsDataId "
                  f"{BASES[BASE_KEY]['stats_data_id']}).")
            print(f"      ↳ This is the signature of a code that does not exist in THIS "
                  f"base — check the base registry before assuming the data is absent. "
                  f"(Tokyo is 13A01 on 2020-base and 13100 on 2025-base.)")
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


def load_tsv(base=None):
    """Rows from CPI.tsv, filtered to ONE base.

    ⚠️ Defaults to the active base rather than returning everything. The two bases
    disagree on the same month (National 2026-06: 1.7 on 2020-base, 1.6 on 2025-base),
    so an unfiltered read would let the display difference across a basis change and
    report it as a data move. Pass base="all" only for a deliberate cross-base view.
    """
    if not CPI_TSV.exists():
        return []
    if base is None:
        base = BASE_KEY
    rows = []
    with open(CPI_TSV) as f:
        next(f, None)
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if len(parts) >= 6:
                row_base = parts[6] if len(parts) >= 7 else "2020"
                if base != "all" and row_base != base:
                    continue
                rows.append({
                    "pulled": parts[0],
                    "series": parts[1],
                    "ref_month": parts[2],
                    "headline": float(parts[3]) if parts[3] else None,
                    "core": float(parts[4]) if parts[4] else None,
                    "core_core": float(parts[5]) if parts[5] else None,
                    "base": row_base,
                })
    return rows


def _migrate_tsv_base_column():
    """Add the `Base` column if the file predates it, stamping legacy rows 2020-base.

    Every row written before 2026-08-17 came from statsDataId 0003427113, so the
    backfill is a fact, not a guess. Done as .tmp + os.replace with a whole-file
    field-count so a partial write cannot leave a ragged ledger
    ([[finding_ragged_row_tolerance_hides_schema_change]])."""
    if not CPI_TSV.exists():
        return
    lines = CPI_TSV.read_text(encoding="utf-8").splitlines()
    if not lines:
        return
    if lines[0].split("\t")[-1] == "Base":
        return
    out = [TSV_HEADER.rstrip("\n")]
    for ln in lines[1:]:
        if not ln.strip():
            continue
        out.append(ln + "\t2020")
    want = len(TSV_HEADER.rstrip("\n").split("\t"))
    bad = [(i, len(r.split("\t"))) for i, r in enumerate(out) if len(r.split("\t")) != want]
    if bad:
        raise SystemExit(f"  🔴 CPI.tsv migration aborted — ragged rows {bad[:5]}")
    tmp = CPI_TSV.with_suffix(".tsv.tmp")
    tmp.write_text("\n".join(out) + "\n", encoding="utf-8")
    os.replace(tmp, CPI_TSV)
    print(f"  🔧 CPI.tsv migrated: added `Base` column, stamped {len(out)-1} legacy row(s) 2020-base")


def append_tsv(series_name, by_month):
    """Append new (series, ref_month) rows. Idempotent.

    ⚠️ Keyed on (series, ref_month, BASE). The same month legitimately appears once
    per base with DIFFERENT values (National 2026-06 = 1.7 on 2020-base, 1.6 on
    2025-base), so base must be part of the identity or one silently shadows the other.
    """
    _migrate_tsv_base_column()
    existing = set()
    if CPI_TSV.exists():
        with open(CPI_TSV) as f:
            next(f, None)
            for line in f:
                parts = line.strip().split("\t")
                if len(parts) >= 3:
                    base = parts[6] if len(parts) >= 7 else "2020"
                    existing.add((parts[1], parts[2], base))
    else:
        with open(CPI_TSV, "w") as f:
            f.write(TSV_HEADER)

    today_str = date.today().isoformat()
    appended = 0
    with open(CPI_TSV, "a") as f:
        for ref_month in sorted(by_month.keys()):
            if (series_name, ref_month, BASE_KEY) in existing:
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
                f"{cc if cc is not None else ''}\t"
                f"{BASE_KEY}\n"
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


def print_comparison_note(nat_by_month, tok_by_month):
    """Tokyo-vs-National core-core. Two DIFFERENT figures share that name —
    print both, each labelled with its own basis, so neither can be restated
    as the other:

      PAIRED — same reference month in BOTH series. This is the canonical
               "Tokyo vs National gap" (KB-169). Only this one is a gap.
      LEAD   — Tokyo's newest month, which National has not published yet.
               Tokyo leads National by ~1 month BY CONSTRUCTION, so this is a
               leading read. Differencing it against an older National month
               manufactures a number that collides with PAIRED.

    Fixed 2026-08-04. Before: this took the two *latest* value-dicts — the
    reference month was discarded by print_summary_for, so the same-month
    check the old docstring promised was structurally impossible — differenced
    them whatever months they were, and labelled the result a gap. On
    2026-08-04 that printed +0.3pp (Tokyo Jul 2.0 vs National Jun 1.7) while
    the canonical paired figure was +0.2pp (Tokyo Jun 1.9 vs National Jun 1.7).
    """
    if not nat_by_month or not tok_by_month:
        return

    def cc(by_month, month):
        return (by_month.get(month) or {}).get("core_core")

    def months_with_cc(by_month):
        return [m for m in by_month if cc(by_month, m) is not None]

    # --- PAIRED: latest month carrying core-core in BOTH series (ISO YYYY-MM sorts)
    common = sorted(set(months_with_cc(nat_by_month)) & set(months_with_cc(tok_by_month)))
    if common:
        m = common[-1]
        n_cc, t_cc = cc(nat_by_month, m), cc(tok_by_month, m)
        diff = t_cc - n_cc
        # Tokyo runs ~30-40bp BELOW National historically; flag an inversion.
        if diff < -0.2:
            note = f"Tokyo {diff:+.1f}pp BELOW National — expected pattern (~30-40bp)"
        elif diff > 0.1:
            note = f"⚠️ Tokyo {diff:+.1f}pp ABOVE National — pattern INVERTED, leading-indicator hawkish"
        else:
            note = f"Tokyo {diff:+.1f}pp vs National — narrower than the typical 30-40bp; Tokyo softness closing"
        print(f"  ℹ️  PAIRED {m} core-core (Tokyo {t_cc:.1f} / National {n_cc:.1f}): {note}")
    else:
        print("  ℹ️  PAIRED core-core: no reference month published in both series — no gap figure this run.")

    # --- LEAD: Tokyo ahead of National. Explicitly NOT a gap.
    nat_months, tok_months = months_with_cc(nat_by_month), months_with_cc(tok_by_month)
    if nat_months and tok_months:
        nat_max, tok_max = max(nat_months), max(tok_months)
        if tok_max > nat_max:
            print(f"  ℹ️  LEAD {tok_max} Tokyo core-core {cc(tok_by_month, tok_max):.1f} "
                  f"— National {tok_max} unpublished (latest {nat_max}). "
                  f"Leading read, NOT a gap: do not difference across months.")
    print("      (CALENDAR <1.9% trigger applies as <1.95% for Tokyo.)")



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
        print("       → fix: set ESTAT_APPID in the fleet .env named above.")
    except Exception as exc:                                       # noqa: BLE001
        print(f"  (staleness check unavailable: {exc})")


def _warn_if_active_base_lags():
    """Say so, loudly, when another base in the ledger has a MORE RECENT month.

    Real as of 2026-08-17 and the reason this guard exists: the 2025-base was loaded
    retroactively only through 2026-06, while the 2020-base already carries Tokyo
    2026-07. Switching the default to 2025-base therefore makes the newest Tokyo
    reading vanish from the display until the 2026-08-21 print lands. A datum that
    disappears because of a BASIS SWITCH looks exactly like a datum that was never
    published — so the difference has to be stated, not inferred.
    """
    try:
        rows = load_tsv(base="all")
    except Exception:
        return
    if not rows:
        return
    latest = {}
    for r in rows:
        k = (r["base"], r["series"])
        if r["ref_month"] > latest.get(k, ""):
            latest[k] = r["ref_month"]
    msgs = []
    for (base, series), month in sorted(latest.items()):
        if base == BASE_KEY:
            continue
        mine = latest.get((BASE_KEY, series), "")
        if month > mine:
            msgs.append(f"{series}: {BASES[base]['label']} has {month}, "
                        f"{BASES[BASE_KEY]['label']} only {mine or 'none'}")
    if msgs:
        print(f"  ⚠️  ACTIVE BASE LAGS ANOTHER BASE IN THE LEDGER:")
        for msg in msgs:
            print(f"        {msg}")
        print(f"      ↳ The newer figure EXISTS and is on the other basis. Read it with "
              f"`--base 2020`; do NOT difference the two.")


def main():
    global BASE_KEY, STATS_DATA_ID, AREA_NATIONAL, AREA_TOKYO
    load_env()
    refresh_only = "--refresh" in sys.argv
    summary_only = "--summary" in sys.argv

    # --base 2020|2025 — the 2020-base stays published until Dec-2026, so reading it
    # is a legitimate operation (that is how you measure the rebasing wedge), but it
    # must be an EXPLICIT choice that gets stamped into the ledger, never a default drift.
    if "--base" in sys.argv:
        i = sys.argv.index("--base")
        if i + 1 < len(sys.argv) and sys.argv[i + 1] in BASES:
            BASE_KEY = sys.argv[i + 1]
        else:
            print(f"  🔴 --base needs one of: {', '.join(BASES)}")
            return 1
    STATS_DATA_ID = BASES[BASE_KEY]["stats_data_id"]
    AREA_NATIONAL = BASES[BASE_KEY]["area_national"]
    AREA_TOKYO = BASES[BASE_KEY]["area_tokyo"]
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
    b = BASES[BASE_KEY]
    print(f"  BASIS: {b['label']}  (statsDataId {b['stats_data_id']}, "
          f"Tokyo cdArea {b['area_tokyo']})")
    if BASE_KEY != DEFAULT_BASE:
        print(f"  ⚠️  NOT the default basis — figures below are {b['label']} and must "
              f"NOT be differenced against {BASES[DEFAULT_BASE]['label']} readings.")
    _warn_if_active_base_lags()
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
            searched = " , ".join(
                f"{p}{'' if p.exists() else ' [absent]'}" for p in ENV_FILES)
            print("  ⚠️  ESTAT_APPID not set. Searched: os.environ , " + searched)
            print(f"  →  Put it in the FLEET SINGLE HOME alongside FRED/PJM/EIA:")
            print(f"         {ENV_FILES[0]}")
            print( "         ESTAT_APPID=<id from e-Stat My Page -> API -> Issue Application ID>")
            print( "     ℹ️  If you registered before, the ID is probably ALREADY ISSUED —")
            print( "         My Page lists existing Application IDs; no need to make a new one.")
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
    print_summary_for("National", nat_data)
    print_summary_for("Tokyo   ", tok_data)
    # Pass the full by-month maps, not the latest value-dicts: the comparison
    # needs reference months to tell a PAIRED gap from a LEAD read.
    print_comparison_note(nat_data, tok_data)

    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
