#!/usr/bin/env python3
"""RESEARCH-INTAKE lane consumer — detection + onset-dedup for WALTER boot step 7e.

Wires the RESEARCH-INTAKE collection lane (separate repo, clone at
/home/willi/Research-Intake, GitHub Action writes it weekday-daily) to WALTER as
its consumer, per PROME packet 2026-06-29 (Will-decided option A: push lane-flagged
breaches through WALTER's existing delivery lane, gated to significance — NOT a new
passive dashboard, which is the COP/BOARD-v0.1 read-side rot failure mode).

READ-ONLY DETECTION. This script does NOT route and does NOT git-pull. The WALTER
boot step pulls the lane (`git -C /home/willi/Research-Intake pull --ff-only`),
runs this to get the worklist, then ROUTES the NEW breaches through the normal
dispatch flow (BOARD + inbox/WALTER handoff + delivery_log, tagged
`source: RESEARCH-INTAKE`), then runs `--mark` to record them as seen.

Onset/change dedup is the anti-spam core: the structured feeds (fred/eia/cftc)
overwrite daily, so a STILL-TRUE condition reappears every run. We push once on
ONSET, not every day it stays true. State: AGENTS/WALTER/registry/intake_seen.json.
Event feeds (edgar critical[], treasury weak[], newsweep) are naturally onset —
each carries an item id, and news is already deduped lane-side (news_seen.json).

  $ python3 tools/intake_scan.py            # report: health + NEW breaches + suppressed
  $ python3 tools/intake_scan.py --mark     # record all currently-true gated keys as seen
                                            #   (seed once at wiring; re-run after routing)
  $ python3 tools/intake_scan.py --json     # machine-readable worklist

Stdlib only. Exit 0 always (informational). Lane read-only; never writes the lane.
"""
import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WALTER = HERE.parent
LANE = Path("/home/willi/Research-Intake")
LIVENESS = LANE / "liveness.json"
SEEN = WALTER / "registry" / "intake_seen.json"

STALE_DAYS = 2  # weekday-daily; >2 calendar days (spans a weekend) => collector likely down

# ── §3 significance gate: feed → owner map (defaults from PROME packet + ROUTING_TABLE) ──
# fred is per-series; the rest are per-feed. Owners are the ACTION target; info-cc in INFO_CC.
FRED_OWNER = {
    "BAMLH0A0HYM2": ["LIQUID", "PROME"],  # HY OAS — the X1 credit-bear arm (highest priority)
    "UMCSENT": ["HENRY"],                 # UMich sentiment
    "PSAVERT": ["CARL"],                  # personal savings rate (consumer)
    "ICSA": ["LABOR"], "CCSA": ["LABOR"], "IC4WSA": ["LABOR"],  # jobless claims
    "CPIAUCSL": ["CARL"], "PCEPILFE": ["CARL"], "T5YIE": ["CARL"], "T10YIE": ["CARL"],  # inflation
    "DGS10": ["HENRY"], "T10Y2Y": ["HENRY"], "DFF": ["HENRY"], "VIXCLS": ["VIOLET"],
}
FRED_INFO = {"BAMLH0A0HYM2": ["HENRY"]}   # HY OAS info-cc beyond the owners
FEED_OWNER = {                            # per-feed ACTION owner / INFO-cc
    "eia_petroleum": (["BRENT"], ["HAWK"]),
    "cftc_cot": (["VIOLET"], ["SAM"]),
    "edgar_8k": (["REGINALD"], []),       # +OZK appended if an OZK ticker appears
    "treasury_auctions": (["BOND"], ["LIQUID"]),
}


def _now_utc():
    return dt.datetime.now(dt.timezone.utc)


def _parse_iso_z(s):
    try:
        return dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
    except (ValueError, AttributeError):
        return None


def load_liveness():
    if not LIVENESS.exists():
        return None, f"lane not found at {LANE} (liveness.json missing) — is RESEARCH-INTAKE cloned?"
    try:
        return json.loads(LIVENESS.read_text(encoding="utf-8")), None
    except (OSError, json.JSONDecodeError) as e:
        return None, f"liveness.json unreadable: {type(e).__name__}: {e}"


def load_seen():
    if not SEEN.exists():
        return {"seen": {}, "updated": None}
    try:
        d = json.loads(SEEN.read_text(encoding="utf-8"))
        d.setdefault("seen", {})
        return d
    except (OSError, json.JSONDecodeError):
        return {"seen": {}, "updated": None}


def _band(s):
    m = re.search(r"\[(red|orange|yellow)\]", s)
    return m.group(1) if m else None


def _gate_for_band(band):
    return {"red": "ACTION", "orange": "INFO", "yellow": "INFO"}.get(band, "INFO")


def collect_alerts(live):
    """Normalize every feed's alert-bearing field into gate records.
    record = dict(feed, key, band, gate, owners, info_cc, precedence, raw)."""
    recs = []
    jobs = live.get("jobs", {})

    def fred_owner(series, band):
        owners = FRED_OWNER.get(series, ["PROME"])  # unknown series -> PROME to triage
        info = FRED_INFO.get(series, [])
        # HY OAS named thresholds (7/1 addendum): >=280 X1-breach / re-kill = IMMEDIATE
        prec = "PRIORITY" if band == "red" else "ROUTINE"
        label = ""
        if series == "BAMLH0A0HYM2":
            info = ["HENRY"]
            if band == "red":
                prec, label = "IMMEDIATE", "X1-trigger breach (credit-bear arm)"
        return owners, info, prec, label

    # fred: alerts[] of "SERIES desc=val [band]"
    for a in jobs.get("fred", {}).get("alerts", []):
        series = a.split(" ", 1)[0]
        band = _band(a) or "orange"
        owners, info, prec, label = fred_owner(series, band)
        recs.append(dict(feed="fred", key=f"fred:{series}:{band}", band=band,
                         gate=_gate_for_band(band), owners=owners, info_cc=info,
                         precedence=prec, raw=a, label=label))

    # eia_petroleum: alerts[] of "metric ... [band] (threshold)"
    for a in jobs.get("eia_petroleum", {}).get("alerts", []):
        band = _band(a) or "red"
        metric = a.split(" ", 1)[0]
        own, info = FEED_OWNER["eia_petroleum"]
        recs.append(dict(feed="eia_petroleum", key=f"eia:{metric}:{band}", band=band,
                         gate=_gate_for_band(band), owners=own, info_cc=info,
                         precedence="PRIORITY" if band == "red" else "ROUTINE",
                         raw=a, label="energy/storage threshold"))

    # cftc_cot: alerts[] (VIX positioning band breaches)
    for a in jobs.get("cftc_cot", {}).get("alerts", []):
        band = _band(a) or "orange"
        own, info = FEED_OWNER["cftc_cot"]
        recs.append(dict(feed="cftc_cot", key=f"cftc:{re.sub(r'[^A-Za-z0-9]+','_',a)[:40]}:{band}",
                         band=band, gate=_gate_for_band(band), owners=own, info_cc=info,
                         precedence="PRIORITY" if band == "red" else "ROUTINE",
                         raw=a, label="VIX positioning"))

    # edgar_8k: critical[] — event-like, each item its own onset key
    for c in jobs.get("edgar_8k", {}).get("critical", []):
        cid = c if isinstance(c, str) else json.dumps(c, sort_keys=True)
        own = ["REGINALD"] + (["OZK"] if "OZK" in cid.upper() else [])
        recs.append(dict(feed="edgar_8k", key=f"edgar:{re.sub(r'[^A-Za-z0-9]+','_',cid)[:60]}",
                         band="red", gate="ACTION", owners=own, info_cc=[],
                         precedence="PRIORITY", raw=cid, label="critical 8-K"))

    # treasury_auctions: weak[] — event-like
    for w in jobs.get("treasury_auctions", {}).get("weak", []):
        wid = w if isinstance(w, str) else json.dumps(w, sort_keys=True)
        recs.append(dict(feed="treasury_auctions", key=f"treasury:{re.sub(r'[^A-Za-z0-9]+','_',wid)[:60]}",
                         band="red", gate="ACTION", owners=["BOND"], info_cc=["LIQUID"],
                         precedence="PRIORITY", raw=wid, label="weak auction"))

    # newsweep: by_class NEW_ALERT->ACTION / NEW_WATCH->INFO; per-item routing reads data/<date>/news.json
    nw = jobs.get("newsweep", {})
    byc = nw.get("by_class", {})
    for cls, gate, prec in (("NEW_ALERT", "ACTION", "PRIORITY"), ("NEW_WATCH", "INFO", "ROUTINE")):
        n = byc.get(cls, 0)
        if n:
            recs.append(dict(feed="newsweep", key=f"news:{cls}:{nw.get('saved','')}", band=None,
                             gate=gate, owners=["(per-item agents field)"], info_cc=[],
                             precedence=prec, raw=f"{n} {cls} item(s) — read {nw.get('saved','data/<date>/news.json')}",
                             label=f"{n} {cls}"))
    return recs


def health(live):
    out = []
    lr = _parse_iso_z(live.get("last_run_utc", ""))
    if lr is None:
        out.append(("MED", "last_run_utc missing/unparseable"))
    else:
        age = (_now_utc() - lr).days
        if age > STALE_DAYS:
            out.append(("MED", f"lane STALE {age}d (last_run {live.get('last_run_utc')}; >{STALE_DAYS}d) — collector likely down; flag PROME"))
        else:
            out.append(("OK", f"last_run {live.get('last_run_utc')} ({age}d)"))
    if live.get("status") != "ok":
        out.append(("MED", f"lane status={live.get('status')}"))
    for feed, j in live.get("jobs", {}).items():
        st = j.get("status")
        if st not in ("ok", None):
            out.append(("MED", f"feed {feed} status={st}"))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mark", action="store_true", help="record all current gated keys as seen")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    live, err = load_liveness()
    if err:
        if args.json:
            print(json.dumps({"error": err}))
        else:
            print(f"RESEARCH-INTAKE scan — ERROR: {err}")
        return 0

    seen = load_seen()
    recs = collect_alerts(live)
    for r in recs:
        r["onset"] = r["key"] not in seen["seen"]
    new = [r for r in recs if r["onset"]]
    suppressed = [r for r in recs if not r["onset"]]
    hz = health(live)

    if args.mark:
        # RECONCILE, don't just add: seen := exactly the currently-true gated keys
        # (preserve first_seen for still-present keys; DROP keys whose alert cleared).
        # This gives correct onset/change semantics — a condition that clears and later
        # re-appears is a fresh onset again, not permanently suppressed.
        stamp = _now_utc().strftime("%Y-%m-%dT%H:%M:%SZ")
        prev = seen.get("seen", {})
        new_seen = {r["key"]: prev.get(r["key"], stamp) for r in recs}
        dropped = [k for k in prev if k not in new_seen]
        seen = {"seen": new_seen, "updated": stamp}
        SEEN.write_text(json.dumps(seen, indent=2) + "\n", encoding="utf-8")
        print(f"reconciled intake_seen.json -> {len(new_seen)} currently-true gated key(s) "
              f"(+{len([r for r in recs if r['key'] not in prev])} new, -{len(dropped)} cleared)")
        return 0

    if args.json:
        print(json.dumps({"health": hz, "new": new, "suppressed": suppressed}, indent=2))
        return 0

    print(f"RESEARCH-INTAKE scan — {_now_utc().strftime('%Y-%m-%d %H:%M')}Z")
    print("=" * 64)
    print("\n[health]")
    for sev, msg in hz:
        print(f"  {sev:<4} {msg}")
    print(f"\n[NEW breaches to ROUTE — {len(new)}]  (onset; push per §3, tag source: RESEARCH-INTAKE)")
    if not new:
        print("  (none — gate quiet)")
    for r in new:
        cc = f" cc {','.join(r['info_cc'])}" if r["info_cc"] else ""
        lbl = f"  [{r['label']}]" if r["label"] else ""
        print(f"  {r['precedence']:<9} {r['gate']:<6} -> {','.join(r['owners'])}{cc}{lbl}\n      {r['raw']}")
    print(f"\n[suppressed — still-true, already seen — {len(suppressed)}]  (do NOT re-push)")
    for r in suppressed:
        print(f"  {r['key']}  ({r['raw'][:70]})")
    print("\nAfter routing the NEW breaches, run:  python3 tools/intake_scan.py --mark")
    return 0


if __name__ == "__main__":
    sys.exit(main())
