#!/usr/bin/env python3
"""
kharg_loadings_watch.py — Kharg Island crude export-loadings cross-check.

Pulls IMF PortWatch Daily_Ports_Data (ArcGIS FeatureServer) for Kharg Island
(portid='port2164'), the terminal that handles ~90-96% of Iran's crude
exports (~1.577 Mbpd, Kpler). Reports export_tanker (est. tonnes/day),
portcalls_tanker, and trailing-window sums. Endpoint identified 2026-07-18
(FALCON, PROME-tasked Kharg-source freeze).

⚠️ CRITICAL — READ BEFORE TRUSTING A "QUIET" RESULT (see domain/KHARG_LOADINGS_SOURCE.md):
This series is AIS-based and Iran's crude leaves Kharg on a dark/AIS-off
shadow fleet. PortWatch is ~90%+ BLIND to Kharg's true throughput and reads
literal ZERO for entire NORMAL export months (Jan/May/Jul-2026 all showed 0).
Therefore a zero/low print is the UNINFORMATIVE normal state and MUST NOT be
read as a strand. This script is a CROSS-CHECK / REFUTATION tool, NOT a
fire signal for GATE-TERRY-006:
  - A NONZERO print (detected loading) is INFORMATIVE: it proves flow is
    CONTINUING and REFUTES a Kharg strand -> the gate must NOT fire. rc 1.
  - A zero/quiet window is NOT proof of a strand (dark fleet invisible). rc 0.
The gate FIRES on the corroborator menu (official declaration / Kpler-Vortexa-
TankerTrackers dark-fleet read / Kharg-specific war-risk notice), NOT on this
script. This script's job is the veto: "is flow still visibly happening?"

Exit codes (inverted vs a normal watcher, on purpose):
  0 = data pulled OK, trailing window is quiet/zero (UNINFORMATIVE - normal
      dark-fleet baseline; NOT a strand confirmation)
  1 = a NONZERO export/call print in the trailing window - REFUTES a strand
      (flow continuing); informative do-not-fire signal
  2 = fetch/parse failure (fail LOUD; never fabricate)

State: kharg_loadings_watch_state.json alongside this script (committed).
Built by FALCON 2026-07-18. Clone of hormuz_transit_watch.py infra.
"""
import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE = ("https://services9.arcgis.com/weJ1QsnbMYJlCHdG/ArcGIS/rest/services/"
        "Daily_Ports_Data/FeatureServer/0/query")
PORTID = "port2164"                  # Kharg Island
TRAIL_DAYS = 14                      # trailing-window sum (daily-zero is useless)
STALE_DAYS = 12                      # publication-lag alarm (normal lag ~5-8d)
STATE_PATH = Path(__file__).resolve().parent / "kharg_loadings_watch_state.json"


def fetch_latest(n=45):
    params = urllib.parse.urlencode({
        "where": f"portid='{PORTID}'",
        "outFields": "date,portname,portcalls_tanker,export_tanker,export",
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
        raise RuntimeError(f"ArcGIS error: {d['error']}")
    rows = []
    for f in d.get("features", []):
        a = f["attributes"]
        raw = a["date"]
        if isinstance(raw, (int, float)):
            dt = datetime.fromtimestamp(raw / 1000, tz=timezone.utc).date()
        else:
            dt = datetime.strptime(str(raw)[:10], "%Y-%m-%d").date()
        rows.append({"date": dt.isoformat(),
                     "pc_tanker": a.get("portcalls_tanker") or 0,
                     "export_tanker": a.get("export_tanker") or 0,
                     "export": a.get("export") or 0})
    rows.sort(key=lambda r: r["date"])
    return rows


def main():
    try:
        rows = fetch_latest()
    except Exception as e:
        print(f"kharg_loadings_watch: FETCH/PARSE FAILURE — {e!r}\n"
              f"Endpoint: {BASE}\nDo NOT assume unchanged; consult "
              f"domain/KHARG_LOADINGS_SOURCE.md and corroborators manually.",
              file=sys.stderr)
        return 2
    if not rows:
        print("kharg_loadings_watch: endpoint returned 0 rows — verify "
              "portid='port2164'/schema unchanged.", file=sys.stderr)
        return 2

    newest = rows[-1]
    age = (datetime.now(timezone.utc).date()
           - datetime.strptime(newest["date"], "%Y-%m-%d").date()).days
    trail = rows[-TRAIL_DAYS:]
    sum_exp = sum(r["export_tanker"] for r in trail)
    sum_call = sum(r["pc_tanker"] for r in trail)

    print(f"Kharg loadings (IMF PortWatch port2164, AIS-est): newest print "
          f"{newest['date']} — {age}d old"
          f"{' ⚠️ STALE (>' + str(STALE_DAYS) + 'd)' if age > STALE_DAYS else ' (normal lag ~5-8d)'}")
    print(f"  trailing-{TRAIL_DAYS}d: export_tanker sum={sum_exp} t, "
          f"tanker_calls sum={sum_call}")
    for r in rows[-7:]:
        print(f"  {r['date']}: export_tanker {r['export_tanker']:>8} t  "
              f"calls {r['pc_tanker']}")

    # informative direction = NONZERO (flow continuing, refutes strand)
    flow_visible = sum_exp > 0 or sum_call > 0
    state = {"last_seen_date": None}
    if STATE_PATH.exists():
        state = json.loads(STATE_PATH.read_text())
    state = {"last_seen_date": newest["date"],
             "last_run": datetime.now(timezone.utc).isoformat(timespec="seconds"),
             "trail14_export_tanker": sum_exp, "trail14_calls": sum_call}
    STATE_PATH.write_text(json.dumps(state, indent=1) + "\n")

    if flow_visible:
        print(f"→ NONZERO loadings visible in trailing window — flow CONTINUING, "
              f"REFUTES a Kharg strand. Gate must NOT fire on strand grounds.")
        return 1
    print("→ Quiet/zero trailing window. ⚠️ UNINFORMATIVE — this is the normal "
          "dark-fleet baseline (whole normal months read 0), NOT a strand "
          "confirmation. Gate fires on the corroborator menu, never on this zero.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
