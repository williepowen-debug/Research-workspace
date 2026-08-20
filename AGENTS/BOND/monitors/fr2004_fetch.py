#!/usr/bin/env python3
"""
FR2004 primary-dealer position fetcher (NY Fed markets API).

WHY THIS EXISTS
---------------
BOND carried "FR2004 is env-blocked, the NY Fed API caps pre-2026" as an owed data
gap for ~6 weeks (5 prints owed; retried 2026-07-06, 07-23, 07-28). It was never an
access problem.

ROOT CAUSE: the primary-dealer API is partitioned into SERIES BREAKS. Querying a
stale break returns only that break's window and then simply stops:

    SBN2015   2015-01-01 -> 2022-01-04
    SBN2022   2022-01-05 -> 2024-07-02     <-- querying this returns data ending 2024-07-02
    SBN2024   2024-07-03 -> 9999-12-31     <-- the live one

An ad-hoc query against SBN2022 returns a valid 200 with real data that stops in
mid-2024, which reads exactly like "the API caps pre-2026." Nothing errors. This is
the stale-executable failure mode: it exits clean and returns the wrong window.

THE FIX: never hardcode a series break. Resolve the CURRENT break at runtime by
asking the API which one covers today, and fail loudly if the data returned does not
reach the expected recency.

Usage:
    python3 monitors/fr2004_fetch.py            # long-end buckets, last 12 prints
    python3 monitors/fr2004_fetch.py --weeks 26
"""
import argparse
import datetime as _dt
import json
import sys
import urllib.request

API = "https://markets.newyorkfed.org/api/pd"
UA = "BOND-research (Research-workspace agent; contact via repo owner)"

# Long-end nominal coupon position buckets. Codes verified against
# /pd/list/timeseries.json on 2026-07-28 -- note it is G7L11 (not G07L11);
# the zero-padded guess returns an EMPTY timeseries with a 200, silently.
BUCKETS = [
    ("PDPOSGSC-G7L11", "7-11Y"),
    ("PDPOSGSC-G11L21", "11-21Y"),
    ("PDPOSGSC-G21", ">21Y"),
]
# Staleness guard: FR2004 is weekly (Wed as-of, ~2wk publication lag).
MAX_EXPECTED_LAG_DAYS = 28


def _get(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def current_seriesbreak(today: _dt.date) -> str:
    """Resolve the live series break at runtime. NEVER hardcode this."""
    breaks = _get(f"{API}/list/seriesbreaks.json")["pd"]["seriesbreaks"]
    for b in breaks:
        start = _dt.date.fromisoformat(b["startdate"])
        end = _dt.date.fromisoformat(b["enddate"])
        if start <= today <= end:
            return b["seriesbreak"]
    raise SystemExit(
        "FAIL: no series break covers today. The API's partitioning changed -- "
        "re-read /pd/list/seriesbreaks.json before trusting any number.\n"
        f"  breaks seen: {[b['seriesbreak'] for b in breaks]}"
    )


def fetch(keyid: str, sb: str) -> dict:
    d = _get(f"{API}/get/{sb}/timeseries/{keyid}.json")
    ts = d.get("pd", {}).get("timeseries", [])
    if not ts:
        raise SystemExit(
            f"FAIL: {keyid} returned an EMPTY series on break {sb}. A 200 with no rows "
            "usually means a wrong keyid (e.g. G07L11 vs G7L11) -- it does NOT mean the "
            "data is missing. Check /pd/list/timeseries.json."
        )
    return {
        t["asofdate"]: float(t["value"]) / 1000.0
        for t in ts
        if t.get("value") not in (None, "", "*")
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--weeks", type=int, default=12)
    args = ap.parse_args()

    today = _dt.date.today()
    sb = current_seriesbreak(today)
    print(f"# FR2004 long-end dealer positions ($B) | series break {sb} (resolved at runtime)")

    series = {label: fetch(k, sb) for k, label in BUCKETS}
    dates = sorted(set.intersection(*(set(v) for v in series.values())))
    if not dates:
        raise SystemExit("FAIL: buckets share no common as-of dates.")

    # Fail LOUD on staleness rather than silently printing an old window.
    # 2026-08-19 (DAEDALUS SFG sweep 8/17): banner moved stderr -> STDOUT so any
    # stdout-capture path (the common way this table reaches a memo) carries the
    # warning WITH the table instead of losing it.
    lag = (today - _dt.date.fromisoformat(dates[-1])).days
    if lag > MAX_EXPECTED_LAG_DAYS:
        print(
            f"\n!! STALE: latest as-of {dates[-1]} is {lag}d old (>{MAX_EXPECTED_LAG_DAYS}d).\n"
            "!! Either publication paused or the break rolled over. Do NOT cite these "
            "as current until resolved."
        )

    shown = dates[-args.weeks:]
    labels = [l for _, l in BUCKETS]
    print(f"{'as-of':<12}" + "".join(f"{l:>10}" for l in labels) + f"{'LONG-END':>12}{'w/w':>9}")
    prev = None
    for d in shown:
        tot = sum(series[l][d] for l in labels)
        chg = f"{tot - prev:+.1f}" if prev is not None else "--"
        print(f"{d:<12}" + "".join(f"{series[l][d]:>9.1f}B" for l in labels) + f"{tot:>11.1f}B{chg:>9}")
        prev = tot

    peak = max(shown, key=lambda d: sum(series[l][d] for l in labels))
    tp = sum(series[l][peak] for l in labels)
    tl = sum(series[l][shown[-1]] for l in labels)
    key = series["11-21Y"]
    kpk = max(shown, key=lambda d: key[d])
    print(
        f"\n# 11-21Y : peak {key[kpk]:.1f}B ({kpk}) -> {key[shown[-1]]:.1f}B ({shown[-1]}) "
        f"= {key[shown[-1]] - key[kpk]:+.1f}B ({100 * (key[shown[-1]] / key[kpk] - 1):+.1f}%)"
    )
    print(
        f"# LONG-END: peak {tp:.1f}B ({peak}) -> {tl:.1f}B ({shown[-1]}) "
        f"= {tl - tp:+.1f}B ({100 * (tl / tp - 1):+.1f}%)"
    )
    print(
        "\n# READ: dealer absorption is a STOCK vector -- benign auction takedowns do NOT\n"
        "# refresh it, only this series does. A drawdown is ambiguous on its own:\n"
        "#   BENIGN distribution  -> falling inventory WITH firm indirect demand at auction\n"
        "#   FORCED de-risking    -> falling inventory WITH weak auctions and/or SOFR-IORB positive\n"
        "# Check those two before scoring the vector in either direction."
    )


if __name__ == "__main__":
    main()
