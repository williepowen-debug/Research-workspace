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
    .venv/bin/python3 AGENTS/LIQUID/scripts/hy_oas_watch.py --selftest   # offline logic test

Surfaces (AGENTS/LIQUID/alerts/):
  HY_OAS_ALERTS.log  append-only — only transitions/kills (the thing a human reads)
  HY_OAS_STATE       json — last zone/bps/sev/sub260 streak + obs date (transition memory; boot.py reads it)
  watch.log          append-only — one line every run (liveness / silent-failure proof)

Escalation uses NO hysteresis on the way UP (earliest catch is the point); transition
memory in HY_OAS_STATE prevents re-firing the same zone, so daily oscillation ≠ spam.
Exit: 0 normal · 1 selftest fail · 3 fetch/parse failure (timer logs it; check watch.log).
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


def decide(bps, obs_date, prev, hy_def, classify):
    """PURE transition logic (no IO) — shared by the live run and --selftest.
    Returns dict: zone, sev, marker, fired (list of alert strings), state (next HY_OAS_STATE)."""
    zone = classify(bps, hy_def)
    sev = SEV.get(zone, -1)
    mk = EMOJI.get(zone, "⚪")
    kill_below = hy_def.get("kill_below", 260)

    prev_sev = prev.get("sev", 0)
    prev_zone = prev.get("zone", "green")
    prev_date = prev.get("obs_date")
    sub260 = prev.get("sub260", 0)
    new_obs = obs_date != prev_date  # advance the kill streak only on a genuinely new daily close

    fired = []
    # 1) Zone escalation into 🟡/🔴 (severity up vs last recorded zone). No hysteresis on the way up.
    if sev >= 1 and sev > prev_sev:
        fired.append(f"🚨 ESCALATION {EMOJI[prev_zone]}{prev_zone}→{mk}{zone}  HY OAS {bps:.0f}bps "
                     f"(as-of {obs_date}) — {hy_def.get('notes','')}")
    # 2) Bear-axis KILL: <260 on two consecutive CLOSES (two-way secondary classify() can't encode)
    if bps < kill_below:
        if new_obs:
            sub260 += 1
        if sub260 >= 2:
            # ⚠️ The LEVEL is met — that is NOT the same as the thesis being killed.
            # KILL_MEMO's tape-vs-substance guard blocks an auto-kill on a tape-only
            # compression, and as of 2026-08-23 its arbiter (BROCK's wrapper-leads half)
            # is CONTESTED => GUARD-HELD-PENDING-ARBITER. An unattended alert that says
            # "INVALIDATION" would contradict the guarded ladder it is watching, so it
            # reports the LEVEL and names the guard instead of pre-empting it.
            fired.append(f"🚨 KILL-LEVEL MET (NOT a kill) — HY OAS {bps:.0f}bps < {kill_below} on {sub260} "
                         f"consecutive closes (as-of {obs_date}). This is the LEVEL condition only. "
                         f"KILL_MEMO tape-vs-substance guard APPLIES: a tape-only compression while private-credit "
                         f"substance worsens is NOT an invalidation. Arbiter contested as of 2026-08-23 "
                         f"=> record GUARD-HELD-PENDING-ARBITER, escalate to BROCK/PROME, and do NOT retire the thesis.")
    else:
        sub260 = 0

    state = {"zone": zone, "bps": round(bps), "sev": sev, "marker": mk,
             "sub260": sub260, "obs_date": obs_date, "checked": _ts()}
    return {"zone": zone, "sev": sev, "marker": mk, "fired": fired, "new_obs": new_obs, "state": state}


def _load_config():
    from config import classify, get_agent
    hy = next((s for s in get_agent("LIQUID") if s["name"] == "HY OAS"), None)
    return classify, hy


def selftest():
    """Offline test of decide() against the REAL config.py bands. Returns 0 pass / 1 fail."""
    print("\n  hy_oas_watch.py --selftest")
    try:
        classify, hy = _load_config()
    except Exception as e:
        print(f"  ✗ cannot import config.py: {e}")
        return 1
    if hy is None:
        print("  ✗ HY OAS series not found in config.py")
        return 1
    print(f"  ✓ config bands: green<{hy['yellow'][0]} / yellow {hy['yellow'][0]}-{hy['red'][0]} / "
          f"red>{hy['red'][0]} · kill_below {hy.get('kill_below', 260)}")

    ok = True

    def check(label, got, want):
        nonlocal ok
        flag = "✓" if got == want else "✗"
        if got != want:
            ok = False
        print(f"  {flag} {label}: got {got!r}, want {want!r}")

    G = {"zone": "green", "sev": 0, "obs_date": "2026-01-01", "sub260": 0}

    # zone classification + escalation firing
    r = decide(264, "2026-01-02", G, hy, classify)
    check("264 → green, no fire", (r["zone"], len(r["fired"])), ("green", 0))
    r = decide(276, "2026-01-02", G, hy, classify)
    check("276 → yellow, escalation fires", (r["zone"], len(r["fired"])), ("yellow", 1))
    r = decide(281, "2026-01-02", {"zone": "yellow", "sev": 1, "obs_date": "2026-01-01"}, hy, classify)
    check("281 (from yellow) → red, escalation fires", (r["zone"], len(r["fired"])), ("red", 1))
    # idempotency: same zone, no re-fire
    r = decide(281, "2026-01-02", {"zone": "red", "sev": 2, "obs_date": "2026-01-01"}, hy, classify)
    check("281 (from red) → no re-fire", len(r["fired"]), 0)

    # bear-axis kill: needs TWO consecutive new closes
    r1 = decide(258, "2026-02-02", {"zone": "green", "sev": 0, "obs_date": "2026-02-01", "sub260": 0}, hy, classify)
    check("258 1st close → sub260=1, no kill yet", (r1["state"]["sub260"], any("KILL" in f for f in r1["fired"])), (1, False))
    r2 = decide(258, "2026-02-03", r1["state"], hy, classify)
    check("258 2nd consecutive close → sub260=2, KILL fires", (r2["state"]["sub260"], any("KILL" in f for f in r2["fired"])), (2, True))
    # same obs_date repeated must NOT advance the kill streak (weekend double-run); r1 recorded 2026-02-02
    r3 = decide(258, "2026-02-02", r1["state"], hy, classify)
    check("258 same obs_date → streak does NOT advance", r3["state"]["sub260"], 1)
    # recovery resets the streak
    r4 = decide(270, "2026-02-04", r2["state"], hy, classify)
    check("270 recovery → sub260 resets to 0", r4["state"]["sub260"], 0)

    print(f"\n  SELFTEST: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


# --------------------------------------------------------------------------- delivery
# A fire used to reach an append-only local log and NOBODY else: the alert text said
# "escalate" and nothing performed the escalation. Between sessions that meant a
# thesis-level event could sit unread for days (the desk was dark 8/24-8/27).
#
# ⛔ WHAT THIS DELIBERATELY DOES NOT DO: git add / commit / push. This runs from a
# systemd timer with no human present, while other agent sessions may hold the shared
# .git/index. An unattended committer racing live sessions is a worse failure than a
# late alert. Delivery is to DISK; the next session commits it.
#
# ⚠️ HONEST CEILING, stated so nobody mistakes this for paging: an unattended script on a
# box with no session running cannot reach a human. This converts "nobody until LIQUID
# boots" into "nobody until ANY agent boots" — a real improvement, not an alert. True
# out-of-session notification needs PROME's Will-facing lane and is PROME's to own.
PROME_INBOX = WORKSPACE / "PROME" / "inbox"      # repo ROOT, not AGENTS/PROME/
SIGNALS = WORKSPACE / "AGENTS" / "SIGNALS.md"


def _deliver(fired, bps, obs_date, state, prev):
    """Route a fire off this box's local log. Idempotent per (kind, obs_date) so a
    persisting condition does not re-file a packet every single day. Never raises:
    a delivery failure must not cost us the detection."""
    delivered = set(prev.get("delivered", []))
    fresh = [l for l in fired if f"{l[:24]}|{obs_date}" not in delivered]
    if not fresh:
        state["delivered"] = sorted(delivered)
        return
    is_kill = any("KILL-LEVEL" in l for l in fresh)
    pri = "🔴" if is_kill else "🟠"
    kind = "kill-level-met" if is_kill else "zone-escalation"
    try:
        PROME_INBOX.mkdir(parents=True, exist_ok=True)
        pkt = PROME_INBOX / f"{obs_date}_from-LIQUID_UNATTENDED-hy-oas-{kind}-{bps:.0f}bps.md"
        body = [f"## {obs_date} — To: PROME (unattended watcher, no human in the loop)",
                f"**Signal:** HY OAS {bps:.0f}bps — {kind.replace('-', ' ')}",
                f"**Priority:** {pri}", "",
                "**Generated by `AGENTS/LIQUID/scripts/hy_oas_watch.py` on a systemd timer — "
                "LIQUID was NOT in session when this fired.** Nobody has judged it.", ""]
        body += [f"- {l}" for l in fresh]
        body += ["", "**What PROME should do:** surface it. Do NOT trade or retire a thesis off this — "
                 "it is a mechanical level read with no analyst attached.",
                 "", "⚠️ **On a kill-level fire specifically: the LEVEL is not the kill.** KILL_MEMO's "
                 "tape-vs-substance guard applies and its arbiter was CONTESTED as of 2026-08-23, so the "
                 "correct state is `GUARD-HELD-PENDING-ARBITER`, not an invalidated thesis.",
                 "", f"**Basis:** FRED `{HY_ID}`, end-of-day, T+1 — `{obs_date}` is the OBSERVATION date, "
                 f"not the wall-clock date this fired.", "",
                 "*This packet is written to disk by an unattended process and is NOT committed by it. "
                 "If you are reading it, it survived to a session — commit it.*"]
        pkt.write_text("\n".join(body) + "\n", encoding="utf-8")
        _log(RLOG, f"{_ts()}  DELIVERED packet -> {pkt.relative_to(WORKSPACE)}")
    except Exception as e:
        _log(RLOG, f"{_ts()}  DELIVER-FAIL packet — {type(e).__name__}: {e}")
    try:
        if SIGNALS.exists():
            desc = fresh[0].replace("|", "/")[:240]
            with SIGNALS.open("a", encoding="utf-8") as f:      # append = least racy
                f.write(f"| {obs_date} | LIQUID | {'ALL' if is_kill else 'PROME'} | {pri} | "
                        f"{desc} | unattended watcher, no analyst attached |\n")
            _log(RLOG, f"{_ts()}  DELIVERED SIGNALS.md row")
    except Exception as e:
        _log(RLOG, f"{_ts()}  DELIVER-FAIL SIGNALS — {type(e).__name__}: {e}")
    delivered |= {f"{l[:24]}|{obs_date}" for l in fresh}
    state["delivered"] = sorted(delivered)[-40:]


def main():
    if "--selftest" in sys.argv:
        return selftest()

    try:
        from fetch import fred_fetch
        classify, hy = _load_config()
    except Exception as e:
        _log(RLOG, f"{_ts()}  IMPORT-FAIL — {e}")
        return 3
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
    prev = _read_state()
    r = decide(bps, obs_date, prev, hy, classify)

    for line in r["fired"]:
        _log(ALOG, f"{_ts()}  {line}")

    if r["fired"]:
        _deliver(r["fired"], bps, obs_date, r["state"], prev)

    _log(RLOG, f"{_ts()}  HY OAS {bps:.0f}bps {r['marker']}{r['zone']} (sev {r['sev']}, "
               f"prev {prev.get('sev', 0)}{prev.get('zone', 'green')}, sub260 {r['state']['sub260']}, "
               f"obs {obs_date}{' NEW' if r['new_obs'] else ''}) "
               f"{'FIRED ' + str(len(r['fired'])) if r['fired'] else 'ok'}")

    STATE.write_text(json.dumps(r["state"], indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
