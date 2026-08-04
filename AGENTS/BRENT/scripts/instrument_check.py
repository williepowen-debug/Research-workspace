#!/usr/bin/env python3
"""
BRENT Instrument Check — does every registered test have a WORKING instrument?

Registry: workbook/REGISTRY.tsv  (consolidated 2026-08-04; absorbed the former INSTRUMENTS.tsv
          AND thresholds.py's hardcoded level tables -- one machine home for level + instrument)

WHY THIS EXISTS (built 2026-08-04, after DEPLOY GATE v2 turned out to be unfillable):
LESSONS #21 says a threshold fails on its SPEC before it fails on the world.
LESSONS #22 says a test must name an instrument that actually TRADES in the window
it will be graded in. This script is #22 pointed at GATES rather than pre-registrations.

It answers four questions a spec review CANNOT answer by reading:
  1. EXISTS       — is an instrument even declared? ("none" is a real, common answer)
  2. REACHABLE    — does a probe return data right now?
  3. FRESH        — is the newest datapoint inside the test's own staleness budget?
  4. FEASIBLE     — for a test that must be graded AND acted on in one session,
                    does the instrument still print while the ACTION market is open?

(4) is the one that is invisible to every other check in the kit, and it is the one
that cost a ratified gate: ^OVX's last bar is 16:00 and USO options close 16:00, so
DEPLOY GATE v2's leg (a) became knowable at exactly the moment leg (b) became
ungradeable. Zero-minute execution window, ratified, and undetected for five days.

⚠️  DELIBERATELY NOISY ABOUT ITS OWN BLIND SPOTS. A silent pass here would be worse
    than no check (`finding_verification_zero_is_ambiguous`), so the summary always
    states how many rows were actually PROBED vs merely asserted.

Exit codes:
  0 = ran clean, nothing blocking
  2 = RAN CORRECTLY and FOUND blocking 🔴 findings (DEAD / NO_INSTRUMENT / WINDOW_INFEASIBLE)
  1 = the SCRIPT ITSELF failed (bad registry, unreadable file)

⚠️  2-not-1 is deliberate. Collapsing "found problems" into the same code as "crashed"
    is how a broken tool hides: this morning `eia_weekly.py` showed FAIL in the boot
    summary purely because of a wrapper timeout, and a real data outage would have looked
    identical. A check whose findings are indistinguishable from its own failure is a
    check you stop reading.

Usage:
  .venv/bin/python3 AGENTS/BRENT/scripts/instrument_check.py
  .venv/bin/python3 AGENTS/BRENT/scripts/instrument_check.py --quick   # skip network probes
  .venv/bin/python3 AGENTS/BRENT/scripts/instrument_check.py --json
"""

import argparse
import csv
import json
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

BRENT_DIR = Path(__file__).resolve().parent.parent
REGISTRY = BRENT_DIR / "workbook" / "REGISTRY.tsv"   # consolidated 2026-08-04; was INSTRUMENTS.tsv

# When the ACTION market closes, ET. Used only for window_req=same_session_action.
# US equity/ETF options close 16:00 ET; the broad-based ETFs (SPY/QQQ/IWM/DIA) run to 16:15.
ACTION_CLOSE_ET = {"_default": "16:00", "SPY": "16:15", "QQQ": "16:15", "IWM": "16:15", "DIA": "16:15"}

RED, AMBER, GREEN = "🔴", "🟠", "✅"


def load_registry():
    rows = []
    with open(REGISTRY, newline="", encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            rows.append(line.rstrip("\n"))
    rdr = csv.DictReader(rows, delimiter="\t")
    # RETIRED rows stay in the registry as the do-not-resurrect list, but are not probed.
    return [r for r in rdr if r.get("test_id") and r.get("status", "live") != "retired"]


# ---------------------------------------------------------------------------
# Probes. Each returns (ok, last_dt_or_None, detail)
# ---------------------------------------------------------------------------

def probe_yf(ticker, want_intraday=False):
    try:
        import yfinance as yf
    except ImportError:
        return None, None, "yfinance not installed"
    try:
        t = yf.Ticker(ticker)
        d = t.history(period="10d")
        if d.empty:
            return False, None, "no daily bars returned"
        last = d.index[-1].to_pydatetime()
        detail = f"last daily bar {last.date()}, close {float(d['Close'].iloc[-1]):.2f}"
        if want_intraday:
            i = t.history(period="5d", interval="5m")
            if not i.empty:
                i.index = i.index.tz_convert("America/New_York")
                # last COMPLETE session in the series, so an in-progress day can't
                # masquerade as an early close (the 13:40 bar on a live afternoon).
                days = sorted({x.date() for x in i.index})
                ref = days[-2] if len(days) > 1 else days[-1]
                sub = i[[x.date() == ref for x in i.index]]
                detail += f" | last intraday print {sub.index[-1].strftime('%H:%M')} ET (on {ref})"
                return True, last, detail
            detail += " | NO intraday bars"
        return True, last, detail
    except Exception as e:
        return False, None, f"probe error: {type(e).__name__}: {e}"


def last_intraday_time_et(ticker):
    """LATEST clock time this ticker prints, taken as the MAX across recent complete
    sessions — never a single session's final bar.

    ⚠️  This is deliberately the CONSERVATIVE (defect-revealing) choice and v1 of this
    function got it wrong. Sampling only the most recent complete session read ^OVX as
    stopping at 15:55 (8/3 had a thin final bar), which reported the DEPLOY GATE v2
    defect as WINDOW_TIGHT/5min instead of WINDOW_INFEASIBLE/0min. 7/31 shows the true
    16:00. An instrument that prints to 16:00 on ANY session prints to 16:00.
    Understating an instrument's reach understates the window defect — i.e. v1 failed
    in the COMFORTING direction, which is the failure mode this whole script exists for.
    """
    try:
        import yfinance as yf
        # prepost=False: the REGULAR session is the basis for "when can I still act".
        i = yf.Ticker(ticker).history(period="10d", interval="5m", prepost=False)
        if i.empty:
            return None
        i.index = i.index.tz_convert("America/New_York")
        days = sorted({x.date() for x in i.index})
        complete = days[:-1] if len(days) > 1 else days   # drop an in-progress today
        if not complete:
            return None
        # ⚠️ 5m bars are LABELLED BY THEIR START. The 15:55 bar covers 15:55–16:00, so the
        # instrument prints until 16:00, not 15:55. v1 compared the LABEL against the action
        # close and therefore reported a phantom 5-minute window on a gate whose real window
        # is ZERO — understating the exact defect this script was built to catch.
        latest = max(max(x for x in i.index if x.date() == d) for d in complete)
        return (latest + timedelta(minutes=5)).strftime("%H:%M")
    except Exception:
        return None


def _fred_key():
    """Same resolution order as thresholds.py: env, then the gitignored FORGE .env."""
    import os
    k = os.environ.get("FRED_API_KEY", "")
    if k:
        return k
    f = BRENT_DIR.parent.parent / "FORGE/tools/market-data/.env"
    if f.exists():
        for line in f.read_text().splitlines():
            if line.startswith("FRED_API_KEY="):
                return line.split("=", 1)[1].strip()
    return ""


def probe_fred(series):
    """FRED observations — returns the newest observation DATE, which is the whole point:
    a FRED series can answer 200 and still be months behind (GASREGW is weekly, BAMLH0A0HYM2
    lags a day). Reachability alone would be a false green.

    ⚠️ ADDED DURING THE 2026-08-04 CONSOLIDATION, and it was NOT cosmetic: folding the FRED
    threshold rows into the shared registry put 10 rows in front of a checker that had no
    fred: prober, so they all reported 🔴 DEAD on a source that works perfectly. Ten false
    positives would have been worse than no check — it is exactly the "a structural edit can
    silently change operational meaning" failure RAV flagged when approving this work.
    """
    key = _fred_key()
    if not key:
        return None, None, "FRED_API_KEY not found (env or FORGE/tools/market-data/.env)"
    url = ("https://api.stlouisfed.org/fred/series/observations"
           f"?series_id={series}&api_key={key}&file_type=json&sort_order=desc&limit=1")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "BRENT-instrument-check/1.0"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            obs = json.loads(resp.read()).get("observations", [])
        if not obs:
            return False, None, "no observations returned"
        d = obs[0].get("date")
        val = obs[0].get("value")
        last = datetime.fromisoformat(d)
        return True, last, f"last observation {d} = {val}"
    except Exception as e:
        return False, None, f"unreachable: {type(e).__name__}: {e}"


def probe_http(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "BRENT-instrument-check/1.0"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            if resp.status != 200:
                return False, None, f"HTTP {resp.status}"
            body = resp.read(4096)
            if len(body) < 64:
                return False, None, f"HTTP 200 but body only {len(body)}B — treat as empty"
            # ⚠️ A 200 proves the HOST answered, NOT that the DATA PARTITION is publishing.
            # This is `finding_partitioned_source_returns_stale_window_at_200` — the exact
            # shape of the PortWatch failure: chokepoint6 serves clean 200s while having
            # published nothing since 7/23, so it reads as "the data ends here" rather
            # than as a fault. Reachability is NEVER evidence of freshness here; the
            # staleness verdict must come from last_verified, and it is not optional.
            return True, None, (f"HTTP 200, {len(body)}B sampled — ⚠️ reachability only; "
                                f"a 200 does NOT prove the data partition is current")
    except Exception as e:
        return False, None, f"unreachable: {type(e).__name__}: {e}"


def probe_chain(spec):
    try:
        import yfinance as yf
        tick, expiry = spec.split("@")
        t = yf.Ticker(tick)
        if expiry not in (t.options or ()):
            return False, None, f"expiry {expiry} not listed"
        ch = t.option_chain(expiry).calls
        if ch.empty:
            return False, None, "chain empty"
        two_sided = int(((ch["bid"] > 0) & (ch["ask"] > 0)).sum())
        return True, None, f"{len(ch)} calls, {two_sided} two-sided"
    except Exception as e:
        return False, None, f"probe error: {type(e).__name__}: {e}"


# ---------------------------------------------------------------------------

_PROBE_CACHE = {}


def _cached(key, fn):
    if key not in _PROBE_CACHE:
        _PROBE_CACHE[key] = fn()
    return _PROBE_CACHE[key]


def evaluate(row, quick=False):
    probe = (row.get("probe") or "").strip()
    findings = []
    probed = False

    def add(level, code, msg):
        findings.append({"level": level, "code": code, "msg": msg})

    # 1. EXISTS
    if probe == "none" or not probe:
        add(RED, "NO_INSTRUMENT", "no instrument declared — this test CANNOT be evaluated, ever")
        return findings, probed, ""

    detail = ""
    last_dt = None

    # 2. REACHABLE
    if probe.startswith("manual:"):
        add(GREEN, "MANUAL", f"human-graded ({probe.split(':',1)[1]}) — not probed")
    elif quick:
        add(AMBER, "SKIPPED", "network probe skipped (--quick)")
    else:
        if probe.startswith("yf:"):
            need_intra = row.get("window_req") == "same_session_action"
            ok, last_dt, detail = _cached((probe, need_intra), lambda: probe_yf(probe[3:], want_intraday=need_intra))
        elif probe.startswith("fred:"):
            ok, last_dt, detail = _cached(probe, lambda: probe_fred(probe[5:]))
        elif probe.startswith("http:"):
            ok, last_dt, detail = _cached(probe, lambda: probe_http(probe[5:]))
        elif probe.startswith("chain:"):
            ok, last_dt, detail = _cached(probe, lambda: probe_chain(probe[6:]))
        else:
            ok, detail = False, f"unknown probe grammar: {probe!r}"
        probed = True
        if ok is None:
            add(AMBER, "NO_PROBER", detail)
        elif not ok:
            add(RED, "DEAD", f"instrument did not return usable data — {detail}")
        else:
            add(GREEN, "REACHABLE", detail)

    # 3. FRESH — content vintage, never mtime (git sync restamps mtime)
    try:
        budget = int(row.get("max_stale_days") or -1)
    except ValueError:
        budget = -1
    if budget >= 0:
        newest = None
        if last_dt is not None:
            newest = last_dt.date()
        else:
            lv = (row.get("last_verified") or "").strip()
            if lv and lv != "NEVER":
                try:
                    newest = datetime.fromisoformat(lv).date()
                except ValueError:
                    newest = None
        if newest is None:
            add(RED, "NO_VINTAGE", "no datapoint date and no usable last_verified — freshness UNKNOWN, not OK")
        else:
            age = (datetime.now().date() - newest).days
            if age > budget:
                # Escalation is KIND-AWARE, not a blanket 2x multiplier. A gate or a
                # falsifier that is out of budget is BLOCKING by definition — it is the
                # thing standing between a thesis and capital, so "a bit stale" is not a
                # warning-level state. v1 used a flat 2x and reported the DEAD PortWatch
                # falsifier — the one currently blocking my thesis — as merely 🟠.
                hard = row.get("kind") in ("gate", "falsifier")
                add(RED if (hard or age > budget * 2) else AMBER, "STALE",
                    f"newest datapoint {newest} is {age}d old vs a {budget}d budget"
                    + ("  [gate/falsifier ⇒ blocking, not advisory]" if hard else ""))

    # 4. FEASIBLE — the window check
    if row.get("window_req") == "same_session_action" and not quick and probe.startswith("yf:"):
        co = (row.get("co_instrument") or "").strip()
        if co:
            inst_t = last_intraday_time_et(probe[3:])
            act_t = ACTION_CLOSE_ET.get(co, ACTION_CLOSE_ET["_default"])
            if inst_t:
                mins = (int(act_t[:2]) * 60 + int(act_t[3:])) - (int(inst_t[:2]) * 60 + int(inst_t[3:]))
                if mins <= 0:
                    add(RED, "WINDOW_INFEASIBLE",
                        f"instrument's last print {inst_t} ET is at/after the {co} action close {act_t} ET "
                        f"⇒ {mins}min window: the test becomes knowable only once it can no longer be acted on")
                elif mins < 30:
                    add(AMBER, "WINDOW_TIGHT",
                        f"only {mins}min between the last {probe[3:]} print ({inst_t}) and the {co} close ({act_t})")
                else:
                    add(GREEN, "WINDOW_OK", f"{mins}min of actionable window after the last print ({inst_t} ET)")

    return findings, probed, detail


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true", help="skip network probes")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--id", help="check a single test_id")
    args = ap.parse_args()

    if not REGISTRY.exists():
        print(f"  ERROR: registry not found at {REGISTRY}")
        return 1

    rows = load_registry()
    if args.id:
        rows = [r for r in rows if r["test_id"] == args.id]
        if not rows:
            print(f"  ERROR: no such test_id {args.id!r}")
            return 1

    results, n_probed = [], 0
    for r in rows:
        f, probed, _ = evaluate(r, quick=args.quick)
        n_probed += 1 if probed else 0
        results.append({"test_id": r["test_id"], "kind": r.get("kind", ""),
                        "spec_home": r.get("spec_home", ""), "findings": f})

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        blocking = [x for x in results if any(g["level"] == RED for g in x["findings"])]
        warn = [x for x in results if x not in blocking and any(g["level"] == AMBER for g in x["findings"])]

        print(f"\n  INSTRUMENT CHECK — {len(results)} registered tests"
              f"{' (--quick: probes skipped)' if args.quick else ''}")
        print(f"  {'-'*74}")

        if blocking:
            print(f"\n  {RED} BLOCKING — these tests cannot be graded as written ({len(blocking)}):")
            for x in blocking:
                for g in x["findings"]:
                    if g["level"] == RED:
                        # test_id goes on the SAME line as the finding: boot.py's output filter
                        # keeps marker lines and drops the header line above them, so a
                        # separate title line yields "7 problems" with no way to tell WHICH.
                        print(f"     {RED} {x['test_id']} [{x['kind']}] {g['code']}: {g['msg']}")
                        print(f"         → spec: {x['spec_home']}")
        if warn:
            print(f"\n  {AMBER} WARNINGS ({len(warn)}):")
            for x in warn:
                for g in x["findings"]:
                    if g["level"] == AMBER:
                        print(f"     {AMBER} {x['test_id']}: {g['code']} — {g['msg']}")
        if not blocking and not warn:
            print(f"\n  {GREEN} all registered tests have a reachable, fresh, feasible instrument.")

        # Anti-false-clean disclosure. A pass means nothing without this.
        print(f"\n  {'-'*74}")
        print(f"  Probed {n_probed} of {len(results)} rows over the network"
              f"{' (0 — --quick)' if args.quick else ''}; the rest are manual/none/unprobeable.")
        print(f"  ⚠️  This checks the INSTRUMENT, never whether the THRESHOLD LEVEL is still meaningful.")
        print(f"      A permanently-breached line (gasoline crack >$30) probes perfectly GREEN.")

    return 2 if any(g["level"] == RED for x in results for g in x["findings"]) else 0


if __name__ == "__main__":
    sys.exit(main())
