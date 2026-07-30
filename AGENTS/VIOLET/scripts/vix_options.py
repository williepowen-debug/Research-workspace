#!/usr/bin/env python3
"""VIOLET VIX Options Positioning — daily snapshot + log.

Fetches VIX option chain via yfinance for all expirations within next 60 days.
For each expiry computes:
  - Call OI, Call Volume
  - Put OI, Put Volume
  - Call/Put OI ratio, Call/Put Volume ratio
  - Top 5 call strikes by OI (with daily volume)

Appends one row per (date, expiry) to workbook/VIX_OPTIONS.tsv.
Prints a summary suitable for boot.py collapse-mode.

Usage:
  .venv/bin/python3 AGENTS/VIOLET/scripts/vix_options.py
  .venv/bin/python3 AGENTS/VIOLET/scripts/vix_options.py --json
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import date, datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
VIOLET_DIR = SCRIPT_DIR.parent
DAILY_LOG = VIOLET_DIR / "workbook" / "VIX_OPTIONS.tsv"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _daily_log import upsert_row  # noqa: E402

LOOKAHEAD_DAYS = 60
TOP_N_STRIKES = 5
NOTABLE_OI = 100_000  # flag individual strikes holding >= 100K contracts


def fetch_snapshot() -> dict:
    import yfinance as yf
    import pandas as pd

    tk = yf.Ticker("^VIX")
    spot = round(float(tk.fast_info["lastPrice"]), 2)
    today = date.today()
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")

    results = []
    for exp_s in tk.options or []:
        try:
            exp = pd.to_datetime(exp_s).date()
        except Exception:
            continue
        dte = (exp - today).days
        if dte < 0 or dte > LOOKAHEAD_DAYS:
            continue
        try:
            chain = tk.option_chain(exp_s)
        except Exception as e:
            results.append({"expiry": exp_s, "dte": dte, "_error": str(e)[:100]})
            continue
        calls = chain.calls
        puts = chain.puts
        call_oi = int(calls.openInterest.fillna(0).sum())
        call_vol = int(calls.volume.fillna(0).sum())
        put_oi = int(puts.openInterest.fillna(0).sum())
        put_vol = int(puts.volume.fillna(0).sum())

        # Top-N call strikes by OI
        top = calls[calls.openInterest.fillna(0) > 0].nlargest(TOP_N_STRIKES, "openInterest")
        top_rows = []
        for _, r in top.iterrows():
            top_rows.append({
                "strike": float(r.strike),
                "oi": int(r.openInterest) if r.openInterest else 0,
                "vol": int(r.volume) if not (r.volume != r.volume) else 0,
                "iv": round(float(r.impliedVolatility), 3) if r.impliedVolatility and r.impliedVolatility == r.impliedVolatility else None,
                "pct_vs_spot": round((float(r.strike) / spot - 1) * 100, 1),
            })

        results.append({
            "expiry": exp_s,
            "dte": dte,
            "call_oi": call_oi,
            "call_vol": call_vol,
            "put_oi": put_oi,
            "put_vol": put_vol,
            "cp_oi_ratio": round(call_oi / max(put_oi, 1), 3),
            "cp_vol_ratio": round(call_vol / max(put_vol, 1), 3),
            "top_call_strikes": top_rows,
        })

    return {
        "as_of": today.isoformat(),
        "source_ts": ts,
        "vix_spot": spot,
        "expiries": results,
        "totals": _summarize_totals(results),
    }


def _summarize_totals(expiries: list[dict]) -> dict:
    # Exclude same-day expiries (they're about to settle, OI is stale pre-expiry)
    fwd = [e for e in expiries if e.get("dte", 0) > 0 and "_error" not in e]
    if not fwd:
        return {}
    call_oi = sum(e["call_oi"] for e in fwd)
    call_vol = sum(e["call_vol"] for e in fwd)
    put_oi = sum(e["put_oi"] for e in fwd)
    put_vol = sum(e["put_vol"] for e in fwd)
    return {
        "forward_expiries": len(fwd),
        "call_oi": call_oi,
        "call_vol": call_vol,
        "put_oi": put_oi,
        "put_vol": put_vol,
        "cp_oi_ratio": round(call_oi / max(put_oi, 1), 3),
        "cp_vol_ratio": round(call_vol / max(put_vol, 1), 3),
    }


def append_to_log(snapshot: dict) -> tuple[int, int]:
    """UPSERT rows keyed on (date, expiry) — KB-VIO-163, see scripts/_daily_log.py.

    Was first-write-wins on that composite key, so whichever run happened first
    each day froze the whole day's snapshot. **Volume accumulates through the
    session**, so a morning boot pinned `call_vol`/`put_vol` at their partial
    early-session values and no later run could correct them — the ledger read
    as an end-of-day snapshot while carrying a 09:00 one. (OI is the milder
    leg: it updates once daily, and after-hours runs print OI=0, a documented
    artifact — the NULL-preserving merge keeps a good stored OI rather than
    letting a 0 overwrite it.)

    Returns (appended, updated).
    """
    if not DAILY_LOG.exists():
        return 0, 0
    with open(DAILY_LOG) as f:
        header = csv.DictReader(f, delimiter="\t").fieldnames or []
    if not header:
        return 0, 0

    appended = updated = 0
    for e in snapshot["expiries"]:
        if "_error" in e:
            continue
        top = e["top_call_strikes"]
        row = {
            "date": snapshot["as_of"],
            "expiry": e["expiry"],
            "dte": e["dte"],
            "call_oi": e["call_oi"],
            "call_vol": e["call_vol"],
            "put_oi": e["put_oi"],
            "put_vol": e["put_vol"],
            "cp_oi_ratio": e["cp_oi_ratio"],
            "cp_vol_ratio": e["cp_vol_ratio"],
            "top_call_strikes": ",".join(str(int(r["strike"])) for r in top),
            "top_call_oi": ",".join(str(r["oi"]) for r in top),
            "top_call_vol": ",".join(str(r["vol"]) for r in top),
            "vix_spot": snapshot["vix_spot"],
            "source_ts": snapshot["source_ts"],
        }
        status, _changes = upsert_row(
            DAILY_LOG, header, [row.get(c, "") for c in header],
            key_cols=["date", "expiry"], state_col=None,
        )
        if status == "appended":
            appended += 1
        elif status == "superseded":
            updated += 1
    return appended, updated


def is_oi_artifact(call_oi, call_vol) -> bool:
    """True if a row's open-interest leg is the documented after-hours artifact.

    yfinance serves OI=0 (or a token value) outside RTH while still returning a
    real volume figure. **Open interest below a single day's volume for an entire
    expiry is structurally impossible** — OI is a cumulative outstanding balance,
    volume is one session's trades — so `call_oi < call_vol` is a principled
    discriminator rather than a tuned threshold.

    Base-rated over the full ledger before adoption (2026-07-30, n=132):
      · flags **34 rows (25.8%)**, vs 28 for a bare `call_oi == 0` test — so it
        catches **6 non-zero artifacts** the obvious test misses (OI 6 / 47 / 47 /
        484 / 1,146 / 1,146 against volumes of 58k–181k);
      · **zero** rows with OI > 50k are flagged (no false positives);
      · negative control: the 98 clean rows have a median OI/volume of **7.9×**.
    The two populations are separated by orders of magnitude, not by a hair.
    """
    try:
        oi, vol = int(float(call_oi)), int(float(call_vol))
    except (TypeError, ValueError):
        return True
    return oi < vol


def detect_dod_changes() -> tuple[list[dict], list[str]]:
    """Compare today's OI to the prior date's, per expiry. Flag >20% moves.

    ⚠️ **Artifact-guarded since 2026-07-30 (KB-VIO-164).** This compared raw OI
    across dates with no idea that ~1 in 4 stored rows carries the after-hours
    OI artifact, so it emitted nonsense: on 7/30 it reported
    `2026-08-19 call_oi: 1,146 → 3,785,644 (+330,235%)` — a pure artifact-to-real
    transition, not a positioning move. **The silent direction is worse than that
    loud one:** when TODAY is the artifact row, a real OI build reads as a
    collapse to zero and the >20% test fires on garbage or, once dismissed as
    "the usual after-hours thing," gets ignored entirely.

    Skipped comparisons are RETURNED and printed, never silently dropped — a
    detector that quietly compares nothing looks identical to one that found
    nothing (`finding_silent_blank_evades_review`).

    Returns (alerts, skip_notes).
    """
    if not DAILY_LOG.exists():
        return [], []
    import pandas as pd
    try:
        df = pd.read_csv(DAILY_LOG, sep="\t", parse_dates=["date"])
    except Exception:
        return [], []
    if df.empty or df.date.nunique() < 2:
        return [], []
    alerts, skipped = [], []
    latest = df.date.max()
    prior_dates = sorted(df.date.unique())
    if len(prior_dates) < 2:
        return [], []
    prior = prior_dates[-2]
    for exp, group in df.groupby("expiry"):
        if latest not in group.date.values or prior not in group.date.values:
            continue
        t = group[group.date == latest].iloc[0]
        p = group[group.date == prior].iloc[0]
        t_art = is_oi_artifact(t.call_oi, t.call_vol)
        p_art = is_oi_artifact(p.call_oi, p.call_vol)
        if t_art or p_art:
            which = "today" if t_art and not p_art else ("prior" if p_art and not t_art else "both")
            skipped.append(
                f"{exp}: OI comparison SKIPPED — {which} row carries the after-hours "
                f"OI artifact (prior oi={int(p.call_oi):,}/vol={int(p.call_vol):,}, "
                f"today oi={int(t.call_oi):,}/vol={int(t.call_vol):,})"
            )
            continue
        if p.call_oi and abs(t.call_oi - p.call_oi) / p.call_oi > 0.20 and t.call_oi > NOTABLE_OI:
            alerts.append({
                "expiry": exp, "metric": "call_oi",
                "prior": int(p.call_oi), "current": int(t.call_oi),
                "pct_change": round((t.call_oi - p.call_oi) / p.call_oi * 100, 1),
            })
    return alerts, skipped


def print_report(snapshot: dict):
    print(f"VIX OPTIONS POSITIONING  {snapshot['as_of']}  spot={snapshot['vix_spot']}")
    totals = snapshot.get("totals", {})
    if totals:
        print(f"  Forward ({totals['forward_expiries']} expiries, 0 < DTE ≤ {LOOKAHEAD_DAYS}): "
              f"Call OI={totals['call_oi']:,}  Put OI={totals['put_oi']:,}  "
              f"C/P OI={totals['cp_oi_ratio']:.2f}  C/P Vol={totals['cp_vol_ratio']:.2f}")

    for e in snapshot["expiries"]:
        if "_error" in e:
            print(f"  {e['expiry']} ({e['dte']}d) ERROR: {e['_error']}")
            continue
        marker = "⚠️ " if e["dte"] == 0 else "  "
        print(f"{marker}{e['expiry']} ({e['dte']:>2}d) Call OI {e['call_oi']:>9,} Vol {e['call_vol']:>6,} | Put OI {e['put_oi']:>9,} Vol {e['put_vol']:>6,} | C/P OI {e['cp_oi_ratio']:.2f}")
        # Show top strikes only for forward expiries with meaningful OI
        if e["dte"] > 0 and e["call_oi"] > NOTABLE_OI / 10:
            top = e["top_call_strikes"][:3]
            if top:
                line = "    top-3 call strikes: " + " · ".join(
                    f"{int(r['strike'])}C OI {r['oi']:,} ({r['pct_vs_spot']:+.0f}%)"
                    for r in top
                )
                print(line)

    # DoD alerts
    alerts, skipped = detect_dod_changes()
    if alerts:
        print("\n  📊 DAY-OVER-DAY OI MOVES (>20% at notable strikes):")
        for a in alerts:
            print(f"    {a['expiry']}  {a['metric']}: {a['prior']:,} → {a['current']:,} ({a['pct_change']:+.1f}%)")
    if skipped:
        # Loud on purpose: a detector that quietly compared nothing is
        # indistinguishable from one that found nothing.
        print(f"\n  ⚠️  {len(skipped)} OI comparison(s) SKIPPED (after-hours OI artifact):")
        for note in skipped:
            print(f"    · {note}")


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--json", action="store_true")
    p.add_argument("--no-append", action="store_true", help="Skip writing to daily log")
    args = p.parse_args(argv)

    snapshot = fetch_snapshot()
    appended, updated = (0, 0) if args.no_append else append_to_log(snapshot)

    if args.json:
        out = dict(snapshot)
        out["rows_appended"] = appended
        out["rows_updated"] = updated
        _alerts, _skipped = detect_dod_changes()
        out["dod_alerts"] = _alerts
        out["dod_skipped"] = _skipped
        print(json.dumps(out, indent=2, default=str))
        return 0

    print_report(snapshot)
    parts = []
    if appended:
        parts.append(f"appended {appended} row(s)")
    if updated:
        parts.append(f"↻ UPDATED {updated} existing row(s) — intraday values moved")
    print(f"\n  {'✓ ' + ' · '.join(parts) if parts else '· no change'} in VIX_OPTIONS.tsv")
    return 0


if __name__ == "__main__":
    sys.exit(main())
