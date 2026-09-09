#!/usr/bin/env python3
"""
bypass_watch.py — Hormuz-bypass (STS/shuttle) integrity gauge.

Pulls IMF PortWatch Daily_Ports_Data (ArcGIS FeatureServer) export_tanker for
the East-coast Gulf-of-Oman STS/transshipment hub cluster — the ports that sit
OUTSIDE Hormuz and receive the shuttle/STS trade that makes the Hormuz closure
non-hermetic. This is the first quantitative gauge of the single most important
FALCON transmission tell:

  "If the shuttle trade breaks, THAT is how risk-premium becomes supply-loss"
  (STATUS / NEXUS_BRIEF). A holding bypass => premium-only read (the MARK lives in STATUS.md, not in this script). A COLLAPSING
  bypass while Hormuz transits stay collapsed => barrels genuinely not moving
  => premium becoming supply-loss => D toward 75.

PRIMARY cluster (robust, oil-tanker-export populated — positive-control PASSED,
18-26 nonzero days/mo unlike dark-fleet Kharg's 4/30):
  Fujairah  port362 (ARE) — world's largest bunkering/storage hub; early-Jul
            throughput at a Mar-Jul HIGH (~45.5k t/d) = bypass absorbing
  Sohar     port988 (OMN) — steady ~25-29k t/d, well-captured
SECONDARY (noisier, minor): Sharjah port72 (ARE)
DROPPED: Khor Fakkan port561 — a CONTAINER port, ~0 oil-tanker export (no signal)

⚠️ HONEST LIMITS — this is a PROXY, not an STS meter (see
domain/BYPASS_INTEGRITY_BASELINE.md for the full characterization):
  1. STS-AT-ANCHORAGE: pure ship-to-ship in Fujairah OPL / mid-Gulf anchorage
     zones may fall outside the port polygon and NOT register. The gauge sees
     tankers loading from/departing the hub, which co-moves with bypass
     activity but is not a direct STS count.
  2. ATTRIBUTION: Fujairah/Sohar export_tanker is GLOBAL hub traffic, not
     Iran-bypass-only. A rise can be non-Iran flows. Use DIRECTIONALLY: the
     informative alarm is a sustained COLLAPSE (barrels stop moving through the
     bypass) while Hormuz stays closed, NOT the absolute level.
  3. LAG: ~5-8d PortWatch publication lag; a fast break is invisible for ~a week.
  Because these are NON-sanctioned downstream legs (crude re-flagged at STS),
  AIS coverage here is GOOD — which is exactly why the hubs are populated while
  Kharg is dark. The gauge works precisely because it sits downstream of the
  dark leg.

ALARM DIRECTION IS INVERTED vs a normal watcher — here the alarm is a COLLAPSE:
  rc 0 = bypass HOLDING/absorbing (trailing throughput at/above the floor) —
         premium-only read intact. NOT an alarm. (No scenario mark is printed here — marks live in STATUS.md.)
  rc 1 = bypass THROUGHPUT COLLAPSED below the floor — REVIEW: possible
         premium->supply-loss transmission; disposition is FALCON's call.
  rc 2 = fetch/parse failure (fail LOUD; never fabricate).

State: bypass_watch_state.json alongside (committed, cross-machine).
Built by FALCON 2026-07-18. Same ArcGIS infra as hormuz_transit_watch.py /
kharg_loadings_watch.py.
"""
import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE = ("https://services9.arcgis.com/weJ1QsnbMYJlCHdG/ArcGIS/rest/services/"
        "Daily_Ports_Data/FeatureServer/0/query")
# primary cluster (label -> portid); secondary flagged separately
PRIMARY = {"Fujairah": "port362", "Sohar": "port988"}
SECONDARY = {"Sharjah": "port72"}
TRAIL_DAYS = 14                     # trailing-window sum (daily is too lumpy)
BASE_DAYS = 60                      # baseline daily-mean window
FLOOR_FRAC = 0.30                   # collapse floor = 30% of baseline daily mean
STALE_DAYS = 12                     # publication-lag alarm (normal ~5-8d)
STATE_PATH = Path(__file__).resolve().parent / "bypass_watch_state.json"


def fetch_port(pid, n=90):
    params = urllib.parse.urlencode({
        "where": f"portid='{pid}'",
        "outFields": "date,portcalls_tanker,export_tanker",
        "orderByFields": "date DESC",
        "resultRecordCount": str(n),
        "returnGeometry": "false",
        "f": "json",
    })
    req = urllib.request.Request(
        f"{BASE}?{params}",
        headers={"User-Agent": "Mozilla/5.0 (research; FALCON agent)"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        d = json.loads(resp.read())
    if "error" in d:
        raise RuntimeError(f"ArcGIS error ({pid}): {d['error']}")
    rows = []
    for f in d.get("features", []):
        a = f["attributes"]
        raw = a["date"]
        if isinstance(raw, (int, float)):
            dt = datetime.fromtimestamp(raw / 1000, tz=timezone.utc).date()
        else:
            dt = datetime.strptime(str(raw)[:10], "%Y-%m-%d").date()
        rows.append((dt, a.get("portcalls_tanker") or 0,
                     a.get("export_tanker") or 0))
    rows.sort()
    return rows


def summarize(rows):
    trail = rows[-TRAIL_DAYS:]
    base = rows[-BASE_DAYS:]
    trail_sum = sum(r[2] for r in trail)
    trail_calls = sum(r[1] for r in trail)
    base_daily_mean = (sum(r[2] for r in base) / len(base)) if base else 0
    trail_daily_mean = trail_sum / len(trail) if trail else 0
    return trail_sum, trail_calls, trail_daily_mean, base_daily_mean


def main():
    try:
        data = {lbl: fetch_port(pid) for lbl, pid in
                {**PRIMARY, **SECONDARY}.items()}
    except Exception as e:
        print(f"bypass_watch: FETCH/PARSE FAILURE — {e!r}\n"
              f"Endpoint: {BASE}\nDo NOT assume unchanged; consult "
              f"domain/BYPASS_INTEGRITY_BASELINE.md.", file=sys.stderr)
        return 2

    newest = max(rows[-1][0] for rows in data.values())
    age = (datetime.now(timezone.utc).date() - newest).days
    print(f"Hormuz-bypass gauge (IMF PortWatch, Gulf-of-Oman STS hubs): "
          f"newest print {newest} — {age}d old"
          f"{' ⚠️ STALE (>' + str(STALE_DAYS) + 'd)' if age > STALE_DAYS else ' (normal lag ~5-8d)'}")

    prim_trail = 0.0
    prim_floor = 0.0
    for lbl in PRIMARY:
        ts, tc, tdm, bdm = summarize(data[lbl])
        floor = bdm * FLOOR_FRAC
        prim_trail += tdm
        prim_floor += floor
        state = "HOLDING" if tdm >= floor else "⚠️ BELOW FLOOR"
        print(f"  [PRIMARY] {lbl:9} trail-{TRAIL_DAYS}d {tdm:8.0f} t/d  "
              f"vs {BASE_DAYS}d-base {bdm:8.0f}  floor({int(FLOOR_FRAC*100)}%) "
              f"{floor:8.0f}  {state}  (calls {tc})")
    for lbl in SECONDARY:
        ts, tc, tdm, bdm = summarize(data[lbl])
        print(f"  [second.] {lbl:9} trail-{TRAIL_DAYS}d {tdm:8.0f} t/d  "
              f"vs {BASE_DAYS}d-base {bdm:8.0f}  (calls {tc}) — context only")

    collapsed = prim_trail < prim_floor
    print(f"  PRIMARY combined: trail {prim_trail:.0f} t/d vs floor "
          f"{prim_floor:.0f} t/d — {'⚠️ COLLAPSED' if collapsed else 'HOLDING'}")

    state = {"last_seen_date": newest.isoformat(),
             "last_run": datetime.now(timezone.utc).isoformat(timespec="seconds"),
             "primary_trail_daily": round(prim_trail),
             "primary_floor_daily": round(prim_floor),
             "collapsed": collapsed}
    STATE_PATH.write_text(json.dumps(state, indent=1) + "\n")

    if collapsed:
        print("→ ⚠️ REVIEW: primary bypass-hub throughput COLLAPSED below floor. "
              "IF Hormuz transits remain collapsed, this is the premium->supply-"
              "loss transmission (D toward 75). Cross-check attribution (global "
              "hub traffic vs Iran-bypass) before firing; disposition is FALCON's.")
        return 1
    print("→ Bypass HOLDING/absorbing (throughput at/above floor) — premium-only "
          "read intact. Not an alarm. Mark lives in STATUS.md, not here.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
