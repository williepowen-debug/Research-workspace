#!/usr/bin/env python3
"""
hormuz_transit_watch.py — Boot-time Strait of Hormuz transit-count monitor.

Pulls the IMF PortWatch Daily_Chokepoints_Data ArcGIS FeatureServer directly
(the portwatch.imf.org page itself is a JS-rendered Hub SPA and unscrapable;
the underlying FeatureServer is public — endpoint identified 2026-07-12,
FALCON round-2 probe, PROME-tasked).

Grades the fresh-leg bar from domain/FRESH_LEG_BASELINE.md row 2:
  pre-crisis baseline = 88 transits/day (PortWatch's own figure);
  a fresh officially-dated count <= ~18/day (~20% of baseline) = countable
  fresh leg toward the GATE-BRENT-SUSTAIN re-arm condition.

KNOWN LIMITATION (documented at build): the dataset publishes with a ~5-8 day
lag (on 2026-07-12 the newest row was 2026-07-05). This script therefore
cannot see TODAY's transits — it sees the freshest official print and tells
you its age. That is still strictly better than the search-snippet method:
exact per-vessel-type counts, exact vintage, no third-party mirror.

FLAG-NOT-FIRE: prints REVIEW on a bar-crossing print; disposition is FALCON's.

Exit codes (baghdad_watch.py convention):
  0 = data pulled OK, no fresh-leg bar crossing in the new prints
  1 = new print(s) at/below the 18/day bar — REVIEW: possible fresh leg
  2 = fetch/parse failure (fail LOUD; never fabricate or silently skip)

State: hormuz_transit_watch_state.json alongside this script (committed —
last-seen date travels across machines). Cwd-proof via Path(__file__).

Built by FALCON 2026-07-12 (round-2, PROME-tasked probe -> script).
"""
import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE = ("https://services9.arcgis.com/weJ1QsnbMYJlCHdG/ArcGIS/rest/services/"
        "Daily_Chokepoints_Data/FeatureServer/0/query")
CHOKEPOINT = "chokepoint6"          # Strait of Hormuz
# BASELINE provenance PINNED 2026-07-27 (closes KB-FALCON-019, resolution KB-FALCON-055).
# 88 = the TRAILING-12-MONTH PRE-WAR *MEDIAN* of this very series: window 2025-02-28..2026-02-27,
# n=365, mean 90.7 / median 88.0 total vessels/day. Computed from this same FeatureServer
# (2757 daily rows 2019-01-01..2026-07-19; NOTE the server caps at 1000 rows — paginate with
# resultOffset or you silently get 2019-2021 only). Corroborated at CRS/Britannica/Statista:
# "peacetime throughput averaged roughly 88 commercial vessels per day, per IMF PortWatch";
# "over 30,000 vessels/year" = 82/day. Annual means for context: 2019 74.3 · 2021 90.8 ·
# 2023 97.8 · 2024 96.1 · 2025 91.5 · 2026 pre-war 80.5.
# ⚠️ THE TWO RIVAL BASELINES ARE RECONCILED, NOT REJECTED:
#   97/day (Hormuz Strait Monitor) ≈ the CY2023 MEAN of THIS SAME SERIES (97.8) — a VINTAGE
#     difference, not a methodology one; traffic genuinely ran ~10% higher in 2023.
#   ~130-140/day = the UPPER END OF THE DAILY RANGE, *NOT* a mean. No annual mean in 7.5 years
#     approaches 140 (max annual mean = 97.8) though single days reach 152-157. Quoting 130-140
#     as "the baseline" is a range-max-as-average error — it is what made a 17% print look like 11%.
# DISCIPLINE (unchanged, now better founded): cite "15/88" inline, never a bare %, never blend series.
BASELINE = 88                        # TTM pre-war median, PortWatch — see provenance block above
# ============================ FIRE BAR — RE-SPECIFIED 2026-08-10 ============================
# SUPERSEDED VALUE, PRESERVED: FRESH_LEG_BAR = 18  ("<=18/day = countable fresh leg", row 2).
# WHY IT WAS RETIRED (self-audit item 4, Will-approved via PROME — a SCRIPT-LOCAL grading bar,
# NOT a registered GATES.tsv number; nothing Will-gated is touched here):
#   The bar was set when the series lived near it. The series has since moved an ORDER OF
#   MAGNITUDE: prints for 2026-07-27..08-02 ran 2-6 total/day, tankers 0-2. EVERY future print
#   is therefore at-or-below 18, so rc=1 would fire on EVERY OBSERVATION.
#   ⇒ AN ALARM THAT CANNOT FAIL TO FIRE CARRIES NO INFORMATION.
#   Worse, it was semantically INVERTED against my own frozen reading bands
#   (FRESH_LEG_BASELINE.md): "<10/day = DEEPENING · 7-14 = bypass-carries [modal] · >~18 = LEAKING".
#   18 is the boundary of the LEAKING/recovery band — so the alarm nominally marked the condition
#   I would read as IMPROVEMENT, while the deterioration band (<10) had no trigger at all.
# NEW DERIVATION: alert on a BAND TRANSITION, not a level cross. The bands are unchanged and
# remain canonical in domain/FRESH_LEG_BASELINE.md; this script now reports which band the newest
# print sits in and fires only when that band CHANGES versus the last logged print. A level bar on
# a collapsed series is a constant; a band transition is an event.
#   ⚠️ Do NOT re-introduce a bare level bar without re-deriving it against the CURRENT series.
#   This is the MIDAS 90d-vs-3wk class: the number did not drift, the WORLD moved past it.
BAND_EDGES = (10, 14, 18)            # <10 DEEPENING | 10-14 BYPASS-CARRIES | 14-18 MIXED | >18 LEAKING
BAND_NAMES = ("DEEPENING", "BYPASS-CARRIES", "MIXED", "LEAKING")
FRESH_LEG_BAR = 18                   # RETAINED for the printed reference line only — NOT a trigger
STALE_DAYS = 10                      # dataset lag alarm (normal lag ~5-8d)


def band_of(n_total):
    """Return the frozen FRESH_LEG_BASELINE.md reading band for a daily total."""
    if n_total < BAND_EDGES[0]:
        return BAND_NAMES[0]
    if n_total < BAND_EDGES[1]:
        return BAND_NAMES[1]
    if n_total <= BAND_EDGES[2]:
        return BAND_NAMES[2]
    return BAND_NAMES[3]
STATE_PATH = Path(__file__).resolve().parent / "hormuz_transit_watch_state.json"


def fetch_latest(n=14):
    params = urllib.parse.urlencode({
        "where": f"portid='{CHOKEPOINT}'",
        "outFields": "date,portname,n_total,n_tanker,n_container,n_cargo",
        "orderByFields": "date DESC",
        "resultRecordCount": str(n),
        "f": "json",
    })
    with urllib.request.urlopen(f"{BASE}?{params}", timeout=30) as resp:
        d = json.loads(resp.read())
    if "error" in d:
        raise RuntimeError(f"ArcGIS error: {d['error']}")
    rows = []
    for f in d.get("features", []):
        a = f["attributes"]
        raw = a["date"]
        # esriFieldTypeDateOnly returns 'YYYY-MM-DD' strings; classic esri
        # date fields return epoch-ms ints — handle both.
        if isinstance(raw, (int, float)):
            dt = datetime.fromtimestamp(raw / 1000, tz=timezone.utc).date()
        else:
            dt = datetime.strptime(str(raw)[:10], "%Y-%m-%d").date()
        rows.append({"date": dt.isoformat(), "n_total": a["n_total"],
                     "n_tanker": a["n_tanker"], "n_container": a["n_container"],
                     "n_cargo": a["n_cargo"]})
    return rows


def main():
    try:
        rows = fetch_latest()
    except Exception as e:
        print(f"hormuz_transit_watch: FETCH/PARSE FAILURE — {e!r}\n"
              f"Endpoint: {BASE}\nDo NOT assume unchanged; the 7/5-vintage "
              f"fallback in FRESH_LEG_BASELINE.md row 2 stays canonical until "
              f"a successful pull.", file=sys.stderr)
        return 2

    if not rows:
        print("hormuz_transit_watch: endpoint returned 0 rows — verify "
              "portid/layer schema unchanged.", file=sys.stderr)
        return 2

    state = {"last_seen_date": None}
    if STATE_PATH.exists():
        state = json.loads(STATE_PATH.read_text())
    last_seen = state.get("last_seen_date")

    newest = rows[0]
    age = (datetime.now(timezone.utc).date()
           - datetime.strptime(newest["date"], "%Y-%m-%d").date()).days
    pct = 100 * newest["n_total"] / BASELINE

    print(f"Hormuz transits (IMF PortWatch, official): newest print "
          f"{newest['date']} = {newest['n_total']}/{BASELINE} ({pct:.0f}% of "
          f"pre-crisis), tankers {newest['n_tanker']} — print is {age}d old"
          f"{' ⚠️ STALE (>' + str(STALE_DAYS) + 'd, check endpoint/lag)' if age > STALE_DAYS else ' (normal publication lag ~5-8d)'}")

    # ---- BAND-TRANSITION LOGIC (re-specified 2026-08-10; see the FIRE BAR block above) ----
    newest_band = band_of(newest["n_total"])
    prev_band = state.get("last_band")
    new_rows = [r for r in rows if last_seen is None or r["date"] > last_seen]

    print(f"  band: {newest_band}"
          f"{'' if prev_band is None else f'  (previous logged band: {prev_band})'}"
          f"   [bands: <{BAND_EDGES[0]} DEEPENING | {BAND_EDGES[0]}-{BAND_EDGES[1]} "
          f"BYPASS-CARRIES | {BAND_EDGES[1]}-{BAND_EDGES[2]} MIXED | >{BAND_EDGES[2]} LEAKING]")

    for r in rows[:7]:
        print(f"  {r['date']}: total {r['n_total']:>3}  tanker "
              f"{r['n_tanker']:>3}   [{band_of(r['n_total'])}]")

    transition = prev_band is not None and newest_band != prev_band
    if transition:
        print(f"⚠️ BAND TRANSITION: {prev_band} → {newest_band} on the {newest['date']} "
              f"print — REVIEW against domain/FRESH_LEG_BASELINE.md; disposition is "
              f"FALCON's call, this script does not fire legs.")
    elif new_rows:
        print(f"{len(new_rows)} new print(s) since last run — band unchanged "
              f"({newest_band}).")
    else:
        print(f"No new prints since last run — band {newest_band}.")

    state = {"last_seen_date": newest["date"],
             "last_band": newest_band,
             "last_run": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    STATE_PATH.write_text(json.dumps(state, indent=1) + "\n")
    return 1 if transition else 0


if __name__ == "__main__":
    sys.exit(main())
