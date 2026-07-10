#!/usr/bin/env python3
"""
job_postings_tracker — Indeed Hiring Lab Job Postings Index puller (LABOR feasibility-probe build,
2026-07-09; see AGENTS/LABOR/OPEN_THREADS_2026-07-09.md GAPS #5).

FEASIBILITY VERDICT: a free, no-auth, weekly-refreshed job-postings data source EXISTS and is
live — Indeed Hiring Lab's public GitHub data repo (github.com/hiring-lab/job_postings_tracker),
plain CSV, no API key, no scraping/ToS issue (it's a published open-data repo, not a scrape).
National + sector + state + metro granularity. Verified live 2026-07-09: national aggregate CSV
runs through 2026-06-26 (~13 days lag from today, consistent with weekly refresh + reporting lag
per the repo README). This is a genuine, repeatable, cheap-to-pull source — the paid alternatives
(LinkUp, Revelio Labs, Lightcast/Burning Glass) were NOT probed further once this free source
confirmed live; if Indeed's free feed is ever pulled, those are the paid fallbacks, not evaluated
here.

WHAT THIS TRACKS (and what it is honestly NOT):
  - This is a POSTINGS-VOLUME index (% chg vs a Feb-1-2020 baseline = 100), not a literal
    per-listing "this posting was withdrawn" event feed — no free source does per-listing
    withdrawal detection. But a falling "total postings" (stock) index IS the aggregate
    signature of net withdrawal exceeding net new posting — the same leading-indicator
    function LABOR's framework wants (4-12wk lead ahead of WARN/claims per the framework
    table in CLAUDE.md). Treat this as the closest free proxy, not a literal withdrawal
    counter. National-level splits "new postings" (flow, <=7 days on Indeed) from "total
    postings" (stock, all active) — flow decelerating first, then stock declining, is the
    sequence to watch. State-level has ONE blended index only (Indeed does not publish the
    new/total split below national).

NOT BUILT tonight (documented, not fabricated): metro-level file (60MB — needs a local cache
  layer to stay cheap on repeat runs, deferred) and sector-level ranking (10MB file, same
  reasoning). State-level (50 states + DC + PR) IS built below — partially closes LABOR's
  OPEN_THREADS gap #2 ("no state/MSA-level JOLTS"); state, not MSA.

Usage:
  python3 job_postings_tracker.py national
  python3 job_postings_tracker.py state FL
  python3 job_postings_tracker.py rank --n 10          # worst 4-week decliners, all states+DC+PR
  python3 job_postings_tracker.py rank --states FL,TX,WA,CA,NY   # rank a specific watchlist

Run with the repo-root venv:
  /home/willi/Research-workspace/.venv/bin/python3 AGENTS/LABOR/tools/job_postings_tracker.py national
"""

import argparse, csv, io, sys, time, urllib.request, urllib.error
from datetime import datetime, timedelta

UA = "LABOR-research williepowen@gmail.com"
REPO_RAW = "https://raw.githubusercontent.com/hiring-lab/job_postings_tracker/master"
NATIONAL_URL = f"{REPO_RAW}/US/aggregate_job_postings_US.csv"
STATE_URL = f"{REPO_RAW}/US/state_job_postings_us.csv"

DECEL_FLAG_PT = -1.0  # 4-week point drop that trips a [DECELERATING] flag (index-point terms)


def _get(url, retries=3, backoff=1.5, timeout=30):
    headers = {"User-Agent": UA}
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read().decode()
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
            last = e
            if attempt < retries - 1:
                time.sleep(backoff * (attempt + 1))
    raise last


def _parse_csv(text):
    return list(csv.DictReader(io.StringIO(text)))


def _trend(series_sorted, value_key, weeks_back=4):
    """series_sorted: date-ascending list of dict rows. Latest value + delta vs nearest
    date <= (latest_date - weeks_back weeks). Returns None if series is empty."""
    if not series_sorted:
        return None
    latest = series_sorted[-1]
    latest_val = float(latest[value_key])
    latest_date = latest["date"]
    target = (datetime.strptime(latest_date, "%Y-%m-%d") - timedelta(weeks=weeks_back)).strftime("%Y-%m-%d")
    prior = None
    for r in series_sorted:
        if r["date"] <= target:
            prior = r
        else:
            break
    prior_val = float(prior[value_key]) if prior else None
    delta = (latest_val - prior_val) if prior_val is not None else None
    return {
        "latest_date": latest_date, "latest_value": latest_val,
        "prior_date": prior["date"] if prior else None, "prior_value": prior_val,
        "delta": delta, "weeks_back": weeks_back,
    }


def _fmt_trend(label, t):
    if t is None:
        return f"  {label}: no data"
    d = t["delta"]
    if d is None:
        return f"  {label}: {t['latest_value']:.2f} ({t['latest_date']}) | no {t['weeks_back']}wk-prior row found"
    flag = " [DECELERATING]" if d < DECEL_FLAG_PT else (" [ACCELERATING]" if d > -DECEL_FLAG_PT else "")
    return (f"  {label}: {t['latest_value']:.2f} ({t['latest_date']}) | "
            f"{t['weeks_back']}wk ago: {t['prior_value']:.2f} ({t['prior_date']}) | "
            f"Δ{t['weeks_back']}wk: {d:+.2f}pt{flag}")


def national():
    rows = _parse_csv(_get(NATIONAL_URL))
    by_variable = {}
    for r in rows:
        by_variable.setdefault(r["variable"], []).append(r)
    for rs in by_variable.values():
        rs.sort(key=lambda r: r["date"])
    return by_variable


def state_series(abbr):
    abbr = abbr.lower()
    rows = _parse_csv(_get(STATE_URL))
    rs = [r for r in rows if r["state"] == abbr]
    rs.sort(key=lambda r: r["date"])
    return rs


def all_states():
    rows = _parse_csv(_get(STATE_URL))
    by_state = {}
    for r in rows:
        by_state.setdefault(r["state"], []).append(r)
    for rs in by_state.values():
        rs.sort(key=lambda r: r["date"])
    return by_state


def cmd_national():
    by_var = national()
    print("=== US National — Indeed Hiring Lab Job Postings Index (SA, %chg vs Feb-1-2020=100) ===")
    for var in ("new postings", "total postings"):
        rs = by_var.get(var, [])
        t = _trend(rs, "indeed_job_postings_index_SA", weeks_back=4)
        print(_fmt_trend(var, t))
        t1 = _trend(rs, "indeed_job_postings_index_SA", weeks_back=1)
        print(_fmt_trend(f"  {var} (1wk)", t1))


def cmd_state(abbr):
    rs = state_series(abbr)
    if not rs:
        print(f"ERROR: no rows found for state code '{abbr}' (use 2-letter lowercase/uppercase, e.g. FL)", file=sys.stderr)
        sys.exit(1)
    t4 = _trend(rs, "indeed_job_postings_index", weeks_back=4)
    t1 = _trend(rs, "indeed_job_postings_index", weeks_back=1)
    print(f"=== {abbr.upper()} — Indeed Hiring Lab state postings index (SA, blended, %chg vs Feb-1-2020=100) ===")
    print(_fmt_trend("index", t4))
    print(_fmt_trend("index (1wk)", t1))


def cmd_rank(n, states_filter):
    by_state = all_states()
    keys = [s.lower() for s in states_filter] if states_filter else list(by_state.keys())
    rows = []
    for st in keys:
        rs = by_state.get(st)
        if not rs:
            continue
        t = _trend(rs, "indeed_job_postings_index", weeks_back=4)
        if t and t["delta"] is not None:
            rows.append((st.upper(), t))
    rows.sort(key=lambda x: x[1]["delta"])  # worst decliner first
    print(f"=== State ranking — worst 4-week Δ first (n={len(rows)} states pulled) ===")
    for st, t in rows[:n]:
        print(_fmt_trend(st, t))


def main():
    ap = argparse.ArgumentParser(description="Indeed Hiring Lab job-postings index puller (LABOR)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("national", help="US national new/total postings index + trend")

    s = sub.add_parser("state", help="single state postings index + trend")
    s.add_argument("abbr", help="2-letter state code, e.g. FL")

    r = sub.add_parser("rank", help="rank states by 4-week Δ (worst decliners first)")
    r.add_argument("--n", type=int, default=10)
    r.add_argument("--states", default=None, help="comma-separated watchlist, e.g. FL,TX,WA,CA,NY (default: all)")

    a = ap.parse_args()
    try:
        if a.cmd == "national":
            cmd_national()
        elif a.cmd == "state":
            cmd_state(a.abbr)
        elif a.cmd == "rank":
            states_filter = a.states.split(",") if a.states else None
            cmd_rank(a.n, states_filter)
    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
