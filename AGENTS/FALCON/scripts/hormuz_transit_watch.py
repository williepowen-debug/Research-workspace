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
BASELINE = 88                        # PortWatch pre-crisis transits/day
FRESH_LEG_BAR = 18                   # <=18/day = countable fresh leg (row 2)
STALE_DAYS = 10                      # dataset lag alarm (normal lag ~5-8d)
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

    new_rows = [r for r in rows if last_seen is None or r["date"] > last_seen]
    review = [r for r in new_rows if r["n_total"] <= FRESH_LEG_BAR]
    for r in rows[:7]:
        marker = " ⚠️ REVIEW: at/below 18/day fresh-leg bar" \
            if r in review else ""
        print(f"  {r['date']}: total {r['n_total']:>3}  tanker "
              f"{r['n_tanker']:>3}{marker}")

    if review:
        print(f"⚠️ {len(review)} new print(s) at/below the {FRESH_LEG_BAR}/day "
              f"fresh-leg bar — REVIEW against FRESH_LEG_BASELINE.md row 2; "
              f"disposition is FALCON's call, this script does not fire legs.")
    elif new_rows:
        print(f"{len(new_rows)} new print(s) since last run — none at/below "
              f"the fresh-leg bar.")
    else:
        print("No new prints since last run.")

    state = {"last_seen_date": newest["date"],
             "last_run": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    STATE_PATH.write_text(json.dumps(state, indent=1) + "\n")
    return 1 if review else 0


if __name__ == "__main__":
    sys.exit(main())
