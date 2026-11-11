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
  $ python3 tools/intake_scan.py --cruise-disposition KEY DISPOSITION REF
                                            # close ONE CRUISE_CAPITAL_REVIEW candidate after review
  $ python3 tools/intake_scan.py --gpu-disposition KEY DISPOSITION REF
                                            # close ONE GPU_FINANCE_REVIEW candidate after review

CRUISE_CAPITAL_REVIEW (WQ-598 A, Will 2026-11-04): a human-review queue of KNOWN cruise-issuer
capital headlines, not an alert and not an automatic dispatch. It lives in its own namespace and
state file, so --mark can neither consume nor reset it. Design and acceptance cases:
research/2026-11-04_maintenance/CRUISE-COVERAGE.md.

Stdlib only. Exit 0 except a refused --cruise-disposition. Lane read-only; never writes the lane.
"""
import argparse
import datetime as dt
import hashlib
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

CRUISE_STATE = WALTER / "registry" / "cruise_capital_review.json"
# First day read. Fixed at install so the archive is never replayed; November 3 keeps the one
# open candidate the design named (the Sandals joint-venture relay) in view.
CRUISE_BASELINE_DAY = "2026-11-03"
CRUISE_TICKERS = {"Carnival Corp": ["CCL"], "Royal Caribbean": ["RCL"], "Norwegian Cruise": ["NCLH", "NCLC"]}
CRUISE_CAPITAL_RE = re.compile(
    r"\b(?:notes? offering|bond offering|commercial paper|credit facilit(?:y|ies)|revolver|refinanc\w*"
    r"|debt financ\w*|loan|stake|joint venture|acquisition|tender offer|debt exchange)\b", re.I)
# Same tokens as tools/batch_manifest.py, so a queue close reads like any other disposition.
CRUISE_DISPOSITIONS = ("DISPATCH", "KILL", "NOTE", "FOLD", "DUP", "NO-ACTION")

# GPU_FINANCE_REVIEW (Will 2026-11-11 12:36 ET, "can we fix it now"): the lane's gpu-obsolescence-1..4
# rows (Research-Intake 5a3b083, VULCAN/BROCK) were collected but never surfaced, because this scan
# showed alert items only (~115 unique titles 10/10 -> 11/10 sat unread; the Ares CEO remark reached
# the BOARD 13 days late as SIG-W-20261111-020). Same design as CRUISE_CAPITAL_REVIEW: a ROUTINE
# human-review list in its own namespace and state file, never an alert, never closed by --mark.
# Baseline 2026-11-11: the backlog before it was triaged by hand (research/2026-11-11_aicapex-review/).
GPU_STATE = WALTER / "registry" / "gpu_finance_review.json"
GPU_BASELINE_DAY = "2026-11-11"
GPU_LABEL_PREFIX = "gpu-obsolescence"


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

    def fred_owner(series, band, raw=""):
        owners = FRED_OWNER.get(series, ["PROME"])  # unknown series -> PROME to triage
        info = FRED_INFO.get(series, [])
        # HY OAS X1 operator (WQ-363; LIQUID KILL_MEMO_HY_OAS_260 line 62): STRICTLY above 280.0 bp,
        # three consecutive; a reading at or below 280.0 resets. One reading above 280 is an
        # IMMEDIATE observation, not the fire (charter 7e(d)); exactly 280 is PRIORITY at-line.
        prec = "PRIORITY" if band == "red" else "ROUTINE"
        label = ""
        if series == "BAMLH0A0HYM2":
            info = ["HENRY"]
            if band == "red":
                m = re.search(r"=\s*([0-9]+(?:\.[0-9]+)?)", raw)
                val = float(m.group(1)) if m else None
                if val is not None and val < 50:  # lane printed percent (e.g. 3.34) -> bp
                    val *= 100
                if val is not None and round(val, 6) > 280.0:
                    prec, label = "IMMEDIATE", "X1 reading strictly above 280 (credit-bear arm; one reading, the trigger needs three consecutive)"
                elif val is not None and round(val, 6) == 280.0:
                    label = "AT the X1 line (280.0), NOT a qualifying reading"
                else:
                    label = "HY red band, value not parsed or at/below 280: read the raw line"
        return owners, info, prec, label

    # fred: alerts[] of "SERIES desc=val [band]"
    for a in jobs.get("fred", {}).get("alerts", []):
        series = a.split(" ", 1)[0]
        band = _band(a) or "orange"
        owners, info, prec, label = fred_owner(series, band, a)
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


def is_cruise_capital_candidate(item):
    """All three legs of the design's rule. entity must be the lane's normalized issuer, so a
    bare CCL text match (CCL Industries) can never bind."""
    return (item.get("classification") == "KNOWN"
            and item.get("entity") in CRUISE_TICKERS
            and "CRUISE" in (item.get("agents") or [])
            and bool(CRUISE_CAPITAL_RE.search(item.get("title") or "")))


def _cruise_key(title):
    norm = re.sub(r"\s+", " ", title).strip().casefold()
    return "cruise:" + hashlib.sha1(norm.encode("utf-8")).hexdigest()[:12]


def _load_cruise_state():
    """(state, error). A missing file is the empty install state; an unreadable one is an error,
    never read as empty, or every closed item would come back and a write could destroy the record."""
    if not CRUISE_STATE.exists():
        return {"baseline_day": CRUISE_BASELINE_DAY, "consumed": {}}, None
    try:
        state = json.loads(CRUISE_STATE.read_text(encoding="utf-8"))
        if not isinstance(state.get("consumed"), dict):
            raise ValueError("consumed is not a mapping")
        return state, None
    except (OSError, ValueError) as e:
        return None, f"{CRUISE_STATE.name} unreadable ({type(e).__name__}); queue UNKNOWN, nothing consumed"


def _edgar_overlap(day_dir, tickers):
    p = day_dir / "edgar_8k.json"
    if not p.exists():
        return []
    try:
        filings = json.loads(p.read_text(encoding="utf-8")).get("filings", [])
    except (OSError, ValueError):
        return [f"{p.parent.name}/edgar_8k.json unreadable; overlap UNKNOWN"]
    return [f"{f.get('ticker')} {f.get('date')} {f.get('items')}" for f in filings if f.get("ticker") in tickers]


def cruise_capital_queue():
    """(open candidates, errors) over every saved day from the baseline, so a missed session loses
    nothing. Identical titles fold into one candidate with all their rows; a changed title is a new
    candidate. Read-only."""
    state, err = _load_cruise_state()
    if err:
        return [], [err]
    errors, by_key = [], {}
    try:
        days = sorted(p for p in (LANE / "data").iterdir() if p.is_dir())
    except OSError as e:
        return [], [f"lane data/ unreadable ({type(e).__name__}); queue UNKNOWN"]
    for d in days:
        if d.name < state.get("baseline_day", CRUISE_BASELINE_DAY):
            continue
        p = d / "news.json"
        try:
            items = json.loads(p.read_text(encoding="utf-8")).get("items", [])
        except (OSError, ValueError, AttributeError) as e:
            errors.append(f"{d.name}/news.json unavailable ({type(e).__name__}); that day UNKNOWN, nothing consumed")
            continue
        for i, it in enumerate(items):
            if not is_cruise_capital_candidate(it):
                continue
            key = _cruise_key(it["title"])
            if key in state["consumed"]:
                continue
            c = by_key.setdefault(key, dict(
                key=key, namespace="CRUISE_CAPITAL_REVIEW", precedence="ROUTINE", title=it["title"],
                entity=it["entity"], owner="CRUISE", rows=[], edgar_overlap=[]))
            c["rows"].append(dict(day=d.name, index=i, date=it.get("date"), link=it.get("link"), source=it.get("source")))
            for f in _edgar_overlap(d, CRUISE_TICKERS[it["entity"]]):
                if f not in c["edgar_overlap"]:
                    c["edgar_overlap"].append(f)
    return sorted(by_key.values(), key=lambda c: (c["rows"][0]["day"], c["rows"][0]["index"])), errors


def cruise_disposition(key, disposition, ref):
    """Close one candidate. Refuses a key not currently open, so an unseen item cannot be consumed."""
    if disposition not in CRUISE_DISPOSITIONS:
        print(f"REFUSED: disposition must be one of {', '.join(CRUISE_DISPOSITIONS)}")
        return 2
    if not ref.strip():
        print("REFUSED: REF must name the card, kill row or reason")
        return 2
    state, err = _load_cruise_state()
    if err:
        print(f"REFUSED: {err}")
        return 2
    queue, _ = cruise_capital_queue()
    match = [c for c in queue if c["key"] == key]
    if not match:
        print(f"REFUSED: {key} is not an open candidate")
        return 2
    c = match[0]
    state.setdefault("baseline_day", CRUISE_BASELINE_DAY)
    state["consumed"][key] = dict(title=c["title"], disposition=disposition, ref=ref.strip(),
                                  days=sorted({r["day"] for r in c["rows"]}),
                                  closed=_now_utc().strftime("%Y-%m-%dT%H:%M:%SZ"))
    CRUISE_STATE.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"closed {key} {disposition} -> {ref.strip()}")
    return 0


def _gpu_key(title):
    norm = re.sub(r"\s+", " ", title).strip().casefold()
    return "gpu:" + hashlib.sha1(norm.encode("utf-8")).hexdigest()[:12]


def _load_gpu_state():
    """(state, error). Missing = empty install state; unreadable = error, never read as empty."""
    if not GPU_STATE.exists():
        return {"baseline_day": GPU_BASELINE_DAY, "consumed": {}}, None
    try:
        state = json.loads(GPU_STATE.read_text(encoding="utf-8"))
        if not isinstance(state.get("consumed"), dict):
            raise ValueError("consumed is not a mapping")
        return state, None
    except (OSError, ValueError) as e:
        return None, f"{GPU_STATE.name} unreadable ({type(e).__name__}); queue UNKNOWN, nothing consumed"


def gpu_finance_queue():
    """(open candidates, errors): every lane news row whose label starts gpu-obsolescence, from the
    baseline day, not yet dispositioned. Identical titles fold into one candidate. Read-only."""
    state, err = _load_gpu_state()
    if err:
        return [], [err]
    errors, by_key = [], {}
    try:
        days = sorted(p for p in (LANE / "data").iterdir() if p.is_dir())
    except OSError as e:
        return [], [f"lane data/ unreadable ({type(e).__name__}); queue UNKNOWN"]
    for d in days:
        if d.name < state.get("baseline_day", GPU_BASELINE_DAY):
            continue
        p = d / "news.json"
        if not p.exists():
            continue
        try:
            items = json.loads(p.read_text(encoding="utf-8")).get("items", [])
        except (OSError, ValueError, AttributeError) as e:
            errors.append(f"{d.name}/news.json unavailable ({type(e).__name__}); that day UNKNOWN, nothing consumed")
            continue
        for i, it in enumerate(items):
            if not str(it.get("label", "")).startswith(GPU_LABEL_PREFIX) or not it.get("title"):
                continue
            key = _gpu_key(it["title"])
            if key in state["consumed"]:
                continue
            c = by_key.setdefault(key, dict(key=key, namespace="GPU_FINANCE_REVIEW", precedence="ROUTINE",
                                            title=it["title"], owner="VULCAN,BROCK", rows=[]))
            c["rows"].append(dict(day=d.name, index=i, date=it.get("date"), link=it.get("link"),
                                  source=it.get("source"), label=it.get("label")))
    return sorted(by_key.values(), key=lambda c: (c["rows"][0]["day"], c["rows"][0]["index"])), errors


def gpu_disposition(key, disposition, ref):
    """Close one GPU_FINANCE_REVIEW candidate. Refuses a key not currently open."""
    if disposition not in CRUISE_DISPOSITIONS:
        print(f"REFUSED: disposition must be one of {', '.join(CRUISE_DISPOSITIONS)}")
        return 2
    if not ref.strip():
        print("REFUSED: REF must name the card, kill row or reason")
        return 2
    state, err = _load_gpu_state()
    if err:
        print(f"REFUSED: {err}")
        return 2
    queue, _ = gpu_finance_queue()
    match = [c for c in queue if c["key"] == key]
    if not match:
        print(f"REFUSED: {key} is not an open candidate")
        return 2
    c = match[0]
    state.setdefault("baseline_day", GPU_BASELINE_DAY)
    state["consumed"][key] = dict(title=c["title"], disposition=disposition, ref=ref.strip(),
                                  days=sorted({r["day"] for r in c["rows"]}),
                                  closed=_now_utc().strftime("%Y-%m-%dT%H:%M:%SZ"))
    GPU_STATE.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"closed {key} {disposition} -> {ref.strip()}")
    return 0


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
    ap.add_argument("--cruise-disposition", nargs=3, metavar=("KEY", "DISPOSITION", "REF"),
                    help="close one CRUISE_CAPITAL_REVIEW candidate after review")
    ap.add_argument("--gpu-disposition", nargs=3, metavar=("KEY", "DISPOSITION", "REF"),
                    help="close one GPU_FINANCE_REVIEW candidate after review")
    args = ap.parse_args()

    if args.cruise_disposition:
        return cruise_disposition(*args.cruise_disposition)
    if args.gpu_disposition:
        return gpu_disposition(*args.gpu_disposition)

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

    cruise, cruise_errors = cruise_capital_queue()
    gpu, gpu_errors = gpu_finance_queue()
    if args.json:
        print(json.dumps({"health": hz, "new": new, "suppressed": suppressed,
                          "cruise_capital_review": cruise, "cruise_capital_errors": cruise_errors,
                          "gpu_finance_review": gpu, "gpu_finance_errors": gpu_errors}, indent=2))
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
    print(f"\n[CRUISE_CAPITAL_REVIEW — {len(cruise)} open]  (ROUTINE human review, never auto-dispatch; "
          "read the source, date the event, check BOARD/EDGAR/CRUISE overlap)")
    for e in cruise_errors:
        print(f"  ERROR {e}")
    if not cruise and not cruise_errors:
        print("  (none open)")
    for c in cruise:
        days = sorted({r["day"] for r in c["rows"]})
        print(f"  {c['key']}  {c['entity']}  {len(c['rows'])} row(s), {days[0]}..{days[-1]}\n      {c['title'][:150]}"
              f"\n      {c['rows'][0]['link']}")
        if c["edgar_overlap"]:
            print(f"      EDGAR same issuer in batch window: {'; '.join(c['edgar_overlap'])} "
                  "(if this is the same event, the existing route stands: no second dispatch)")
    print(f"\n[GPU_FINANCE_REVIEW — {len(gpu)} open]  (ROUTINE human review of GPU depreciation / collateral / "
          "GPU-backed loan / residual-value headlines, owners VULCAN and BROCK; never auto-dispatch; read the source, "
          "date the event (reposts carry fresh dates), check BOARD and owner KB, then --gpu-disposition)")
    for e in gpu_errors:
        print(f"  ERROR {e}")
    if not gpu and not gpu_errors:
        print("  (none open)")
    for c in gpu:
        days = sorted({r["day"] for r in c["rows"]})
        print(f"  {c['key']}  {len(c['rows'])} row(s), {days[0]}..{days[-1]}\n      {c['title'][:150]}"
              f"\n      {c['rows'][0]['link']}")
    print(f"\n[suppressed — still-true, already seen — {len(suppressed)}]  (do NOT re-push)")
    for r in suppressed:
        print(f"  {r['key']}  ({r['raw'][:70]})")
    print("\nAfter routing the NEW breaches, run:  python3 tools/intake_scan.py --mark")
    return 0


if __name__ == "__main__":
    sys.exit(main())
