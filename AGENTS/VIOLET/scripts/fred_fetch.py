"""Fetch daily series from FRED (public CSV endpoint, no API key).

Cache model (rewritten 2026-06-23, KB-VIO-103): ONE canonical file per
(series, start) — `{series_id}_{start}.csv` — that grows in place via
merge-on-write. The old `{series_id}_{start}_{end}.csv` convention minted a
new file every calendar day (8+ per code), so any ad-hoc "read the latest"
glob could non-deterministically pick a STALE older-dated file. That mis-read
(NOT a fetch failure) is what produced the false "fred_fetch broken" call at
the 6/23 boot — the fetch was fine; the reader picked the wrong file.

Use `latest_value()` / `--summary` to read the gate; never glob the cache.
"""
from __future__ import annotations

import io
import os
from datetime import date
from pathlib import Path

import pandas as pd
import requests
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay

CACHE_DIR = Path(__file__).resolve().parent.parent / "workbook" / "fred_cache"

# Freshness is a BUSINESS-DAY question, not a calendar-day one (KB-VIO-133).
#
# The old rule was a flat `FRESH_TOLERANCE_DAYS = 4` calendar-day window, which
# failed in exactly the case that matters most: on Monday 2026-07-27 it computed
# fresh_through = 07-23, and the cache's newest row was *exactly* 07-23 — so it
# passed the test and served stale data while Friday 07-24 sat unfetched at FRED
# for all 11 series. boot.py then printed a Bin-A credit verdict stamped [07-23]
# and the whole session's top carry-forward ("re-pull the credit gate live")
# would have been discharged against a value one full session out of date.
#
# The correct question is: what is the newest observation that COULD exist right
# now? ICE BofA OAS series publish at T+1, so it is the previous US business day.
# Deriving that from a business-day calendar handles weekends and holidays by
# construction instead of approximating them with a fudge constant.
_US_BDAY = CustomBusinessDay(calendar=USFederalHolidayCalendar())

# Deliberately NO refetch throttle. The obvious guard — "skip if the cache file
# was written < N minutes ago" — trusts FILE MTIME as a proxy for "we already
# tried", and in this repo that proxy lies: fred_cache/*.csv are committed and
# git-synced across two machines, so a `git pull` stamps a STALE file with a
# CURRENT mtime. On a desktop→laptop switch the throttle would then suppress the
# refetch of genuinely out-of-date data — reintroducing KB-VIO-133 by a new
# route. It is the same disease as the original bug: trusting a proxy instead of
# the quantity you actually care about.
# The throttle also guarded a problem that does not exist here: boot.py invokes
# this once per session (11 series, ~0.4s), not on a timer, so there is no loop
# to amplify. Correctness beats a saved HTTP call.


def _expected_latest_obs(end: str | date) -> pd.Timestamp:
    """Newest observation FRED could hold as of `end`, given the T+1 lag."""
    return (pd.Timestamp(end) - _US_BDAY).normalize()


def _cache_path(series_id: str, start: str) -> Path:
    # NOTE: end deliberately NOT in the filename — one canonical file per
    # (series, start), grown via merge-on-write. See module docstring.
    return CACHE_DIR / f"{series_id}_{start}.csv"


def fetch_series(
    series_id: str,
    start: str = "2024-10-01",
    end: str | None = None,
    *,
    force: bool = False,
) -> pd.DataFrame:
    if end is None:
        end = date.today().isoformat()
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_file = _cache_path(series_id, start)

    if cache_file.exists() and not force:
        cached = pd.read_csv(cache_file, parse_dates=["DATE"], index_col="DATE")
        if not cached.empty:
            expected = _expected_latest_obs(end)
            if cached.index.max() >= expected:
                print(f"[FRED] {series_id}: {len(cached)} rows (cached, "
                      f"latest {cached.index.max().date()})")
                return cached

            # stale → fall through and re-fetch, then merge
            print(f"[FRED] {series_id}: cache stale "
                  f"(latest {cached.index.max().date()} < expected {expected.date()}), refetching")

    url = (
        f"https://fred.stlouisfed.org/graph/fredgraph.csv"
        f"?id={series_id}&cosd={start}&coed={end}"
    )
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()

    df = pd.read_csv(io.StringIO(resp.text))
    date_col = [c for c in df.columns if "date" in c.lower()][0]
    df[date_col] = pd.to_datetime(df[date_col])
    df = df.set_index(date_col)
    df.index.name = "DATE"
    df.columns = [series_id]
    df[series_id] = pd.to_numeric(df[series_id], errors="coerce")
    df.dropna(inplace=True)

    # merge-on-write: never let a partial/past-window fetch SHRINK the
    # canonical file. Union by date; freshly-fetched values win on overlap.
    if cache_file.exists():
        old = pd.read_csv(cache_file, parse_dates=["DATE"], index_col="DATE")
        df = df.combine_first(old).sort_index()
        df = df[~df.index.duplicated(keep="first")]

    df.to_csv(cache_file)
    print(f"[FRED] {series_id}: {len(df)} rows → {cache_file.name} "
          f"(latest {df.index.max().date()})")
    return df


def latest_value(
    series_id: str,
    start: str = "2024-10-01",
    end: str | None = None,
    *,
    force: bool = False,
) -> tuple[pd.Timestamp, float]:
    """Canonical 'read the latest value' — freshness-aware, no globbing.

    Returns (date, value) of the most recent row. This is the ONLY supported
    way to read a current value; do not glob the cache dir by hand.
    """
    df = fetch_series(series_id, start, end, force=force)
    last = df.dropna().iloc[-1]
    return df.dropna().index.max(), float(last.iloc[0])


# Friendly names + the credit series of interest for --summary.
NAMES = {
    "BAMLH0A0HYM2": "HY", "BAMLC0A0CM": "IG", "BAMLH0A3HYC": "CCC",
    "BAMLH0A1HYBB": "BB", "BAMLH0A2HYB": "B", "BAMLC0A4CBBB": "BBB",
    "BAMLHE00EHYIOAS": "EuroHY", "BAMLEMHBHYCRPIOAS": "EM_HY",
    "DGS2": "2Y", "DGS10": "10Y", "DFII10": "TIPS10",
}

# Credit-gate lines (KB-VIO-096 block).
BINB_BLOCK_LINE = 9.55          # CCC >= this => Bin-B block ACTIVE; < this => block LIFTS

# ⛔ BIN-A IS **STUCK** — the four level lines were RETIRED 2026-08-04 (Will-ratified,
#    relayed via PROME). They are NOT commented-out-pending-return; they are dead.
#
#    WHY (KB-VIO-184, n=784 obs / ~630 firing days — this rests on DAYS, not on the thin
#    episode count): any-1-of-4 fired on **80.7% of all days** and scored **0.78x** the
#    baseline on P(VIX +50% within 21d) — 12.2% vs 15.7% unconditional. It was not merely
#    saturated, it was an ANTI-SIGNAL. Its output was its two loosest legs (BB >= 1.73 fired
#    75.4% of days, HY >= 2.85 72.7%), while the two selective legs (CCC, dispersion) each
#    added +0.1pp of marginal coverage. Confirmed live on 2026-08-03: BB and HY both un-fired
#    on a 6-7bp tightening because their lines had been set at the then-current June-2026
#    value (KB-VIO-183).
#
#    STATE = **STUCK**, not RETIRED and not REPLACED (STATE_VOCABULARY). The old tree is
#    broken AND the replacement is not validated, so BIN-A currently answers NOTHING.
#    Emitting a fresh number here would swap one confident answer for another thinly-derived
#    one. A reader who sees STUCK goes looking; a reader who sees a number cites it.
#
#    THE CANDIDATE REPLACEMENT IS **NOT REGISTERED** and must not be coded here until Will
#    ratifies the numbers: dCCC(5 sessions) >= 48bp (p95, month-end-excluded) AND
#    [dBB(5) >= 14bp OR dB(5) >= 18bp], dwell 21 sessions, no level gate. Held pending
#    re-derivation on pre-2023 history (Wayback recovery path, PROME 2026-08-04).
#
#    ⚠️ PERMANENT SCOPE LABEL, ratified independently of the numbers and travelling with
#    BIN-A wherever it goes: **tail/convexity detector, NOT a direction forecast. No
#    demonstrated edge below VIX 20.** It fires at mean VIX 23.66 vs 17.30 unconditional
#    (COINCIDENT, not leading) and mean forward-21d return is -3.77% — P(+50%) doubles while
#    the MEAN is negative. Never sell it as "vol is going up."
BINA_LINES = {}                 # ⛔ STUCK — intentionally empty; see the block above.
BINA_STUCK_NOTE = (
    "BIN-A **STUCK** since 2026-08-04 — the four level lines were retired as an anti-signal "
    "(fired 80.7% of days, 0.78x baseline; KB-VIO-184). Replacement derived but NOT ratified "
    "(thin: ~7 episodes, no credit crisis in the 3y window). BIN-A answers nothing right now. "
    "Scope when it returns: tail/convexity detector, no demonstrated edge below VIX 20."
)


def credit_summary(*, force: bool = False) -> dict:
    """Print + return the credit-gate dashboard with KB-VIO-090/096 verdict."""
    codes = ["BAMLH0A0HYM2", "BAMLH0A3HYC", "BAMLH0A1HYBB", "BAMLH0A2HYB",
             "BAMLC0A4CBBB", "BAMLC0A0CM", "BAMLHE00EHYIOAS", "BAMLEMHBHYCRPIOAS"]
    vals, dates = {}, {}
    for c in codes:
        try:
            d, v = latest_value(c, force=force)
            vals[NAMES[c]] = v
            dates[NAMES[c]] = d.date().isoformat()
        except Exception as e:
            print(f"[ERROR] {NAMES.get(c, c)}: {e}")
    disp = round(vals["CCC"] - vals["BB"], 2) if {"CCC", "BB"} <= vals.keys() else None
    if disp is not None:
        vals["DISP"] = disp

    print("\n" + "=" * 60)
    print("  CREDIT GATE SUMMARY (KB-VIO-096 block · BIN-A = STUCK)")
    print("=" * 60)
    asof = dates.get("CCC", "?")
    for name in ["HY", "CCC", "BB", "B", "BBB", "IG", "EuroHY", "EM_HY"]:
        if name in vals:
            print(f"  {name:7s} {vals[name]:>6.2f}   [{dates.get(name, '?')}]")
    if disp is not None:
        print(f"  {'CCC-BB':7s} {disp:>6.2f}")

    # Verdict. BIN-A is STUCK — it emits no escalation verdict at all (BINA_LINES is empty
    # by ratified decision, not by accident). The KB-VIO-096 block is a SEPARATE mechanism
    # and survives the retirement, so it still evaluates below.
    tripped = [label for label, (k, lvl) in BINA_LINES.items()
               if k in vals and vals[k] >= lvl]
    print("-" * 60)
    print(f"  ⛔ BIN-A: STUCK [since 2026-08-04] — no escalation verdict is emitted.")
    print(f"     {BINA_STUCK_NOTE}")
    print("-" * 60)
    if tripped:
        verdict = "🔴 BIN-A ESCALATION — " + "; ".join(tripped)
    elif vals.get("CCC", 0) >= BINB_BLOCK_LINE:
        verdict = f"🟠 BIN-B BLOCK ACTIVE (CCC {vals['CCC']:.2f} ≥ {BINB_BLOCK_LINE})"
    else:
        margin = BINB_BLOCK_LINE - vals.get("CCC", BINB_BLOCK_LINE)
        verdict = (f"🟢 BLOCK LIFTED (CCC {vals.get('CCC'):.2f} < {BINB_BLOCK_LINE}, "
                   f"{margin:.2f} below the line); no Bin-A")
    print(f"  VERDICT [{asof}]: {verdict}")
    print("=" * 60)
    return {"asof": asof, "values": vals, "dates": dates,
            "dispersion": disp, "bin_a_tripped": tripped, "verdict": verdict}


SERIES = {
    # HY composite, IG composite, CCC
    "credit": ["BAMLH0A0HYM2", "BAMLC0A0CM", "BAMLH0A3HYC"],
    # KB-VIO-090 tree conversion lines: BB (A2 1.73), single-B (watch-only), CCC-BB dispersion needs BB
    "credit_ladder": ["BAMLH0A1HYBB", "BAMLH0A2HYB", "BAMLC0A4CBBB"],
    # KB-VIO-097 US-local-vs-global control: Euro HY + EM HY corp
    "credit_global": ["BAMLHE00EHYIOAS", "BAMLEMHBHYCRPIOAS"],
    "rates": ["DGS2", "DGS10", "DFII10"],
}

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--start", default="2024-10-01")
    p.add_argument("--end", default=date.today().isoformat())
    p.add_argument("--force", action="store_true")
    p.add_argument("--summary", action="store_true",
                   help="Print the credit-gate dashboard (KB-VIO-090/096 verdict)")
    args = p.parse_args()

    for group, ids in SERIES.items():
        print(f"\n--- {group} ---")
        for sid in ids:
            try:
                fetch_series(sid, args.start, args.end, force=args.force)
            except Exception as e:
                print(f"[ERROR] {sid}: {e}")

    if args.summary:
        credit_summary(force=False)  # already fetched above; read canonical
