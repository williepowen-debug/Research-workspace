#!/usr/bin/env python3
"""
LIQUID HY OAS watcher — unattended credit-trigger guard (P1b, 2026-06-26).

Pulls HY OAS live from FRED and classifies it against the SHARED config.py bands
(SENTRY-retuned 2026-06-26: green <265 / yellow 265-280 / red >280; kill_below 260).
Fires a LOCAL file alert on a zone ESCALATION (severity increase into 🟡/🔴) and on
the two-way bear-axis KILL (<260 on two consecutive closes). File-only surface — no
Telegram, no network push. Source of truth = config.py (imported, not copied), so a
future SENTRY retune flows through automatically.

Run by systemd --user timer `liquid-hy-watch.timer` (Mon–Fri 13:00 ET). Manual:
    .venv/bin/python3 AGENTS/LIQUID/scripts/hy_oas_watch.py

Surfaces (AGENTS/LIQUID/alerts/):
  HY_OAS_ALERTS.log  append-only — only transitions/kills (the thing a human reads)
  HY_OAS_STATE       json — last zone/bps/sev/sub260 streak + obs date (transition memory; boot.py reads it)
  watch.log          append-only — one line every run (liveness / silent-failure proof)

Escalation uses NO hysteresis on the way UP (earliest catch is the point); transition
memory in HY_OAS_STATE prevents re-firing the same zone, so daily oscillation ≠ spam.
Exit: 0 normal · 3 fetch/parse failure (timer logs it; check watch.log).
"""

import json
import sys
from datetime import datetime
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
LIQUID_DIR = SCRIPTS_DIR.parent
WORKSPACE = SCRIPTS_DIR.parents[2]
FETCH_DIR = WORKSPACE / "FORGE" / "tools" / "market-data"
sys.path.insert(0, str(FETCH_DIR))

ALERTDIR = LIQUID_DIR / "alerts"
STATE = ALERTDIR / "HY_OAS_STATE"
ALOG = ALERTDIR / "HY_OAS_ALERTS.log"
RLOG = ALERTDIR / "watch.log"

SEV = {"green": 0, "yellow": 1, "red": 2, "unknown": -1}
EMOJI = {"green": "🟢", "yellow": "🟡", "red": "🔴", "unknown": "⚪"}
HY_ID = "BAMLH0A0HYM2"


def _ts():
    return datetime.now().strftime("%Y-%m-%d %H:%M %Z")


def _log(path, line):
    ALERTDIR.mkdir(parents=True, exist_ok=True)
    with path.open("a") as f:
        f.write(line + "\n")


def _read_state():
    try:
        return json.loads(STATE.read_text())
    except Exception:
        return {}


def main():
    try:
        from fetch import fred_fetch
        from config import classify, get_agent
    except Exception as e:
        _log(RLOG, f"{_ts()}  IMPORT-FAIL — {e}")
        return 3

    # HY OAS series def straight from shared config (inherits SENTRY bands + multiply + kill_below)
    hy = next((s for s in get_agent("LIQUID") if s["name"] == "HY OAS"), None)
    if hy is None:
        _log(RLOG, f"{_ts()}  CONFIG-FAIL — HY OAS series not found in config.py")
        return 3

    obs = fred_fetch(HY_ID, limit=2)
    if not obs or (isinstance(obs[0], dict) and "error" in obs[0]):
        err = obs[0]["error"] if obs else "no data"
        _log(RLOG, f"{_ts()}  FETCH-FAIL — {err}")
        return 3

    try:
        raw = float(obs[0]["value"])
        obs_date = obs[0]["date"]
    except (ValueError, KeyError, TypeError) as e:
        _log(RLOG, f"{_ts()}  PARSE-FAIL — {e}")
        return 3

    bps = raw * hy.get("multiply", 1)
    zone = classify(bps, hy)
    sev = SEV.get(zone, -1)
    mk = EMOJI.get(zone, "⚪")
    kill_below = hy.get("kill_below", 260)

    prev = _read_state()
    prev_sev = prev.get("sev", 0)
    prev_zone = prev.get("zone", "green")
    prev_date = prev.get("obs_date")
    sub260 = prev.get("sub260", 0)
    new_obs = obs_date != prev_date  # only advance the kill streak on a genuinely new daily close

    fired = []

    # 1) Zone escalation into 🟡/🔴 (severity up vs last recorded zone). No hysteresis on the way up.
    if sev >= 1 and sev > prev_sev:
        fired.append(f"🚨 ESCALATION {EMOJI[prev_zone]}{prev_zone}→{mk}{zone}  HY OAS {bps:.0f}bps "
                     f"(as-of {obs_date}) — {hy.get('notes','')}")

    # 2) Bear-axis KILL: <260 on two consecutive CLOSES (two-way secondary classify() can't encode)
    if bps < kill_below:
        if new_obs:
            sub260 += 1
        if sub260 >= 2:
            fired.append(f"🚨 BEAR-AXIS KILL — HY OAS {bps:.0f}bps < {kill_below} on {sub260} consecutive "
                         f"closes (as-of {obs_date}) — credit-thesis INVALIDATION (not a stress event); escalate")
    else:
        sub260 = 0

    for line in fired:
        _log(ALOG, f"{_ts()}  {line}")

    _log(RLOG, f"{_ts()}  HY OAS {bps:.0f}bps {mk}{zone} (sev {sev}, prev {prev_sev}{prev_zone}, "
               f"sub260 {sub260}, obs {obs_date}{' NEW' if new_obs else ''}) "
               f"{'FIRED ' + str(len(fired)) if fired else 'ok'}")

    STATE.write_text(json.dumps({
        "zone": zone, "bps": round(bps), "sev": sev, "marker": mk,
        "sub260": sub260, "obs_date": obs_date, "checked": _ts(),
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
