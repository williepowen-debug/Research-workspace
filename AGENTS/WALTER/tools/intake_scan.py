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
from intake_cadence import missed_weekday_runs

HERE = Path(__file__).resolve().parent
WALTER = HERE.parent
LANE = Path("/home/willi/Research-Intake")
LIVENESS = LANE / "liveness.json"
SEEN = WALTER / "registry" / "intake_seen.json"

STALE_RUNS = 2  # Weekday daily; holidays still count, consistently with doctor.

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
    "edgar_8k": (["REGINALD"], []),       # LEGACY (Phase B 2026-08-02): routing now reads
                                          # per-filing route_to via _edgar_route(); this row
                                          # kept only as documentation of the old default
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


def _edgar_route(cid):
    """Phase B: resolve (owners, entity_class-label) for an edgar critical[] string
    ("TICKER YYYY-MM-DD [...]") via the lane's per-filing route_to/entity_class fields
    (Phase A, PROME `3b07f9d`). Fail-LOUD: an unparseable string or a row the join
    cannot find surfaces as UNTAGGED in the label — the legacy REGINALD(+OZK) chain is
    the fallback so nothing is silently dropped, but the consumer SEES the join failed.
    entity_class=other legitimately routes to [] (consumer judgment, per the ruling)."""
    legacy = ["REGINALD"] + (["OZK"] if "OZK" in cid.upper() else [])
    m = re.match(r"([A-Z][A-Z0-9.\-]{0,9})\s+(\d{4}-\d{2}-\d{2})", cid)
    if not m:
        return legacy, "UNTAGGED: unparseable critical[] string — check lane"
    ticker, fdate = m.group(1), m.group(2)
    try:
        run_dirs = sorted((LANE / "data").iterdir(), reverse=True)[:5]
    except OSError:
        return legacy, "UNTAGGED: lane data/ unreadable — check lane"
    for d in run_dirs:
        p = d / "edgar_8k.json"
        if not p.exists():
            continue
        try:
            filings = json.loads(p.read_text()).get("filings", [])
        except (OSError, ValueError):
            continue
        for f in filings:
            if f.get("ticker") == ticker and f.get("date") == fdate:
                ec = f.get("entity_class")
                rt = f.get("route_to")
                if ec is None or rt is None:
                    return legacy, "UNTAGGED: row found but Phase-A fields missing — check lane"
                return (rt if rt else []), (ec if rt else f"{ec} — no route_to: consumer judgment")
    return legacy, "UNTAGGED: no lane row joined (ticker+date) — check lane"


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

    # edgar_8k: critical[] — event-like, each item its own onset key.
    # Phase B (2026-08-02, PROME Phase-A contract `3b07f9d`): routing reads the lane's
    # per-filing entity_class/route_to (joined on ticker+date into data/*/edgar_8k.json).
    # The critical[] string stays the onset key — byte-stable, seen-keys never churn.
    # Missing/unjoinable tag = fail-LOUD in the label (per the 7/28 ruling), never a
    # silent default; legacy REGINALD(+OZK) routing kept as the visible fallback.
    for c in jobs.get("edgar_8k", {}).get("critical", []):
        cid = c if isinstance(c, str) else json.dumps(c, sort_keys=True)
        own, ec_label = _edgar_route(cid)
        recs.append(dict(feed="edgar_8k", key=f"edgar:{re.sub(r'[^A-Za-z0-9]+','_',cid)[:60]}",
                         band="red", gate="ACTION", owners=own, info_cc=[],
                         precedence="PRIORITY", raw=cid, label=f"critical 8-K [{ec_label}]"))

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

    # NEW_WATCH_HIT + DEVELOPMENT — PER ITEM, owned by the desk that registered the term.
    # Added 2026-09-25 (walter-9c): until today this function read only the NEW_ALERT/NEW_WATCH
    # COUNTS, so every WATCH_FOR hit (the owner-registered wake terms: FLG rent freeze, HENRY,
    # BROCK, SAM, and the WQ-295 R3 lists) was classified by the lane and NEVER reached WALTER's
    # worklist. The lane's own alert list (fetch_newsweep.py) already treats these two classes as
    # alerts; this aligns the consumer with it. Per-item keys, so a dark owner's hit can carry the
    # rule-6b doorbell recommendation. Onset keys are the title hash (the news feed is deduped
    # lane-side, so an item is one onset).
    saved = nw.get("saved")
    if saved and (byc.get("NEW_WATCH_HIT") or byc.get("DEVELOPMENT")):
        try:
            items = json.loads((LANE / saved).read_text(encoding="utf-8")).get("items", [])
        except Exception as e:
            items = []
            recs.append(dict(feed="newsweep", key=f"news:UNREADABLE:{saved}", band=None, gate="INFO",
                             owners=["WALTER"], info_cc=[], precedence="ROUTINE",
                             raw=f"{saved} unreadable ({type(e).__name__}); watch hits UNKNOWN",
                             label="news.json unreadable — watch hits UNKNOWN"))
        import hashlib
        for it in items:
            cls = it.get("classification")
            if cls not in ("NEW_WATCH_HIT", "DEVELOPMENT"):
                continue
            title = it.get("title", "")
            h = hashlib.sha1(title.encode("utf-8")).hexdigest()[:12]
            if cls == "NEW_WATCH_HIT":
                hits = it.get("watch_hits") or []
                owners = sorted({hw[0] for hw in hits if isinstance(hw, (list, tuple)) and hw}) or ["(unknown)"]
                phrases = "; ".join(f"{hw[0]}:'{hw[1]}'" for hw in hits if isinstance(hw, (list, tuple)) and len(hw) > 1)
                recs.append(dict(feed="newsweep", key=f"news:WATCH_HIT:{h}", band=None, gate="ACTION",
                                 owners=owners, info_cc=[], precedence="PRIORITY", raw=title[:160],
                                 label=f"WATCH_HIT [{phrases}]"))
            else:
                ents = it.get("entity") or "?"
                recs.append(dict(feed="newsweep", key=f"news:DEVELOPMENT:{h}", band=None, gate="INFO",
                                 owners=list(it.get("agents") or []) or ["(per-item agents field)"],
                                 info_cc=[], precedence="ROUTINE", raw=title[:160],
                                 label=f"DEVELOPMENT [known entity {ents} + escalation qualifier]"))
    return recs


def health(live):
    out = []
    lr = _parse_iso_z(live.get("last_run_utc", ""))
    if lr is None or lr.tzinfo is None:
        out.append(("MED", "last_run_utc missing/unparseable"))
    else:
        now = _now_utc()
        age = (now - lr).days
        missed = missed_weekday_runs(lr.astimezone(dt.timezone.utc).date(), now.date())
        if lr > now:
            out.append(("MED", "last_run_utc is in the future — freshness UNVERIFIED"))
        elif missed > STALE_RUNS:
            out.append(("MED", f"lane STALE: {missed} missed weekday runs, {age} calendar days — collector likely down; flag PROME"))
        else:
            out.append(("OK", f"last_run {live.get('last_run_utc')} ({missed} missed weekday runs, {age} calendar days)"))
    if live.get("status") != "ok":
        out.append(("MED", f"lane status={live.get('status')}"))
    for feed, j in live.get("jobs", {}).items():
        st = j.get("status")
        if st not in ("ok", None):
            out.append(("MED", f"feed {feed} status={st}"))
    out.extend(news_search_coverage(live))
    return out


def _search_labels():
    """Labels of the lane's Google News queries, read from the lane's own config."""
    try:
        sys.path.insert(0, str(LANE / "scripts"))
        import newsweep_config as cfg
        return {q.get("label", "") for q in cfg.GOOGLE_NEWS_QUERIES} - {""}
    except Exception:
        return None
    finally:
        sys.path.pop(0)


def news_search_coverage(live):
    """Coverage anomaly: the newsweep job can report status=ok while its Google News
    leg saved NOTHING (2026-09-17 and 2026-09-30: 0 search items vs 88-221 typical;
    the collector swallows per-query errors). A low SAVED count does not prove the
    searches failed (dedup and the noise filter also drop items), so this reports an
    ANOMALY WITH CAUSE UNKNOWN, never an outage. research/2026-10-01_intake-bounded-comparison.md"""
    job = live.get("jobs", {}).get("newsweep") or {}
    saved = job.get("saved")
    # Report the job's own status, never assume it: since RESEARCH-INTAKE 429f948 (L569) the job can
    # read `degraded` with `degraded_reasons`, and a hard-coded "reported ok" would then be untrue.
    status = job.get("status", "UNKNOWN")
    reasons = job.get("degraded_reasons")
    if isinstance(reasons, dict):   # shape not stated in the L569 packet; keep the values either way
        reasons = [f"{k}: {v}" for k, v in reasons.items()]
    elif reasons is not None and not isinstance(reasons, (list, tuple)):
        reasons = [reasons]
    job_state = f"newsweep reported {status}" + (f" ({'; '.join(map(str, reasons))})" if reasons else "")
    labels = _search_labels()
    if not saved:
        return []
    if labels is None:
        return [("MED", "news search coverage UNCHECKED — lane newsweep_config not importable")]

    def count(path):
        try:
            items = json.loads((LANE / path).read_text(encoding="utf-8")).get("items", [])
        except (OSError, json.JSONDecodeError, AttributeError):
            return None
        return sum(1 for i in items if i.get("label") in labels)

    n = count(saved)
    if n is None:
        return [("MED", f"news search coverage UNCHECKED — {saved} unreadable")]
    earlier = [p.relative_to(LANE) for p in sorted(LANE.glob("data/*/news.json"))
               if str(p.relative_to(LANE)) < saved][-10:]   # the 10 batches BEFORE this one
    prior = [c for c in map(count, earlier) if c is not None]
    med = sorted(prior)[len(prior) // 2] if prior else None
    basis = f"trailing median {med} over {len(prior)} batches" if med is not None else "no trailing batches"
    if n == 0 or (med and n < med * 0.25):
        return [("MED", f"news search COVERAGE ANOMALY: {saved} saved {n} Google News items ({basis}) "
                        f"while {job_state} — cause UNKNOWN (failed requests, malformed feeds, "
                        "or dedup/filtering); treat the batch as degraded and do not read its silence as quiet")]
    return [("OK", f"news search items saved: {n} ({basis})")]


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
