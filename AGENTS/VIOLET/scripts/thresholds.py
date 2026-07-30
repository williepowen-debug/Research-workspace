#!/usr/bin/env python3
"""VIOLET Thresholds — live vol dashboard + daily log append.

Fetches spot VIX / VIX3M / VIX6M / VVIX / SKEW via yfinance, pulls M1/M2 futures
steepness from the shared vix_futures CLI, classifies against VIOLET thresholds,
and appends one row to AGENTS/VIOLET/workbook/VX_DAILY.tsv.

Classifications come from VIOLET/STATUS.md Signal Dashboard and KB-VIO-025
(M1:M2 contango bands).

Usage:
  .venv/bin/python3 AGENTS/VIOLET/scripts/thresholds.py
  .venv/bin/python3 AGENTS/VIOLET/scripts/thresholds.py --json
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")

SCRIPT_DIR = Path(__file__).resolve().parent
VIOLET_DIR = SCRIPT_DIR.parent
WORKSPACE = VIOLET_DIR.parent.parent
DAILY_LOG = VIOLET_DIR / "workbook" / "VX_DAILY.tsv"
VIX_FUTURES_CLI = WORKSPACE / "FORGE" / "tools" / "market-data" / "vix_futures.py"
VENV_PY = WORKSPACE / ".venv" / "bin" / "python3"

TICKERS = {
    "vix": "^VIX",
    "vix3m": "^VIX3M",
    "vix6m": "^VIX6M",
    "vvix": "^VVIX",
    "skew": "^SKEW",
}

# (label, getter, bands) — bands are (green_upper, yellow_upper, orange_upper); >orange = red
# Direction: higher = worse for most vol metrics, except VIX3M/VIX (lower = worse).
BANDS = {
    "vix":            {"green": 15,  "yellow": 20,  "orange": 30,  "red_above": True,  "fmt": "{:.2f}"},
    "vvix":           {"green": 80,  "yellow": 120, "orange": 150, "red_above": True,  "fmt": "{:.2f}"},
    "skew":           {"green": 120, "yellow": 140, "orange": 150, "red_above": True,  "fmt": "{:.2f}"},
    "vix3m_vix_ratio": {"green": 1.15, "yellow": 1.0, "orange": 0.9, "red_above": False, "fmt": "{:.3f}"},
    "m1m2_adj_pct":   {"green": 5.6, "yellow": 8.99, "orange": 12.0, "red_above": True,  "fmt": "{:+.2f}%"},
}


def classify(key: str, value: float) -> str:
    if value is None:
        return "⚪"
    b = BANDS.get(key)
    if not b:
        return "⚪"
    if b["red_above"]:
        if value < b["green"]: return "🟢"
        if value < b["yellow"]: return "🟡"
        if value < b["orange"]: return "🟠"
        return "🔴"
    else:
        if value > b["green"]: return "🟢"
        if value > b["yellow"]: return "🟡"
        if value > b["orange"]: return "🟠"
        return "🔴"


def last_bar_et_date(sym: str) -> date | None:
    """ET calendar date of the most recent intraday bar for `sym`, or None if it
    cannot be established. Used to answer "does this quote belong to TODAY?" —
    `fast_info['lastPrice']` cannot, because it returns the last price that
    EXISTS with no indication of when it was struck.

    None means UNVERIFIABLE, never "stale" — the caller must not delete data on
    a None (auto-memory finding_single_witness_guard_deletes_real_data).
    """
    import yfinance as yf
    try:
        h = yf.Ticker(sym).history(period="5d", interval="5m", prepost=True)
        if h is None or len(h) == 0:
            return None
        ts = h.index[-1]
        try:
            ts = ts.tz_convert(ET)
        except (TypeError, AttributeError):
            pass
        return ts.date()
    except Exception:
        return None


def fetch_spot(verify_dates: bool = True) -> dict:
    """Fetch spot levels for the vol complex.

    ⚠️ THE DEFECT THIS GUARDS (KB-VIO-139/145, built 2026-07-30 after it fired
    three consecutive sessions and nearly false-tripped a live exit guard):
    ^VIX quotes during CBOE global trading hours, but ^VIX3M / ^VIX6M / ^VVIX /
    ^SKEW DO NOT publish pre-open. `fast_info['lastPrice']` serves each one's
    PRIOR SESSION close with no staleness signal, so a pre-open TICK row silently
    fill-forwards four columns from yesterday and the derived VIX3M/VIX ratio
    becomes a CROSS-DATE artifact (a 7/29 numerator over a 7/30 denominator).

    The direction is the dangerous one: a fill-forward prior makes any 1-day
    change computed against it OVERSTATED, so the defect MANUFACTURES
    peak-markers on exactly the guards whose job is timing an exit. Graded off
    the contaminated 7/28 row, stand-down (iv) would have read −7.05pt =
    TRIPPED against a >5pt line; the true reading was −3.43pt = not tripped.

    Per KB-VIO-139's own spec: a TICK row writes NULL for a column it cannot
    source — it never carries the prior day's. Returns values with
    `<key>_stale = True` marked and the value set to None for confirmed-stale
    columns; `<key>_unverified = True` KEEPS the value (fail-safe: a network
    hiccup must not erase a real print).
    """
    import yfinance as yf
    out = {}
    today_et = datetime.now(timezone.utc).astimezone(ET).date()
    for key, sym in TICKERS.items():
        try:
            tk = yf.Ticker(sym)
            val = round(float(tk.fast_info["lastPrice"]), 4)
        except Exception as e:
            out[key] = None
            out[f"{key}_error"] = str(e)
            continue
        if not verify_dates:
            out[key] = val
            continue
        bar_date = last_bar_et_date(sym)
        if bar_date is None:
            # Could not establish a data-date. KEEP the value, flag it.
            out[key] = val
            out[f"{key}_unverified"] = True
        elif bar_date < today_et:
            # Confirmed stale: this quote belongs to a PRIOR session.
            out[key] = None
            out[f"{key}_stale"] = True
            out[f"{key}_stale_date"] = bar_date.isoformat()
            out[f"{key}_suppressed_value"] = val
        else:
            out[key] = val
            out[f"{key}_bar_date"] = bar_date.isoformat()
    return out


def fetch_m1m2(start: date | None = None, max_lookback: int = 5) -> dict:
    """Invoke vix_futures.py --json, return its dict (or {"_error": ...}).

    The CLI defaults to today-minus-one-CALENDAR-day, which lands on a day with
    no VX settlements every Monday (Sunday) and after every holiday. That
    silently blanked the m1m2 columns on 8 of 12 Mondays since 2026-05-01 (vs
    2 of 11 Fridays) — the last 8 consecutive Mondays were empty, so the
    front-curve vector went dark on exactly the session that digests the
    weekend's news flow (KB-VIO-130, found 7/27).

    Fix: walk backwards from `start` (ET today) to the most recent date that
    actually HAS settlements. An intraday run before the ~16:15 ET settle post
    simply fails on today and falls through to the prior business day, which is
    the correct answer for a TICK-basis row. The settlement's own date still
    rides out via `as_of`, so the row stays honestly stamped (KB-VIO-092).
    """
    if start is None:
        start = datetime.now(ET).date()
    last_err = "no settlement found in lookback window"
    for back in range(max_lookback + 1):
        query = start - timedelta(days=back)
        try:
            result = subprocess.run(
                [str(VENV_PY), str(VIX_FUTURES_CLI), "--json", "--date", query.isoformat()],
                capture_output=True, text=True, timeout=30, cwd=str(WORKSPACE),
            )
            if result.returncode != 0:
                last_err = result.stderr[:200]
                continue
            payload = json.loads(result.stdout)
            if payload and "_error" not in payload:
                return payload
            last_err = str(payload.get("_error", last_err))[:200]
        except Exception as e:
            last_err = str(e)
    return {"_error": last_err}


def determine_regime(vix: float | None) -> str:
    if vix is None: return "UNKNOWN"
    if vix < 15: return "COMPLACENCY"
    if vix < 20: return "LOW_VOL"
    if vix < 30: return "RISING_VOL"
    if vix < 40: return "HIGH_VOL"
    return "CRASH"


def append_daily_log(row: dict, supersede: bool = False) -> str:
    """Append one row keyed by date. Returns a STATUS CODE (not a bare bool) so
    callers can state the real reason a write was skipped — the old bool made
    every skip print the same misleading "already has a row" line (VIOLET 6/13).

    Status codes:
      'appended'             new row written
      'updated'              existing row superseded (EOD SETTLE replacing a TICK)
      'skip-no-file'         VX_DAILY.tsv missing
      'skip-weekend'         Sat/Sun — markets closed, would just dup Friday (6/6 phantom)
      'skip-exists'          row present, --supersede not set
      'skip-tick-vs-settle'  existing row is SETTLE, incoming is TICK — never downgrade

    NOTE: this only ever targets the row whose date == row['date'] (always
    "today" from build_report). It CANNOT repair a stale PRIOR-date row — use
    backfill.py (dated-row repair) for that (VIOLET 6/13, Orc).
    """
    if not DAILY_LOG.exists():
        return "skip-no-file"
    try:
        d = datetime.fromisoformat(row["date"]).date()
        if d.weekday() >= 5:  # Sat=5, Sun=6
            return "skip-weekend"
    except (KeyError, ValueError):
        pass
    with open(DAILY_LOG) as f:
        header = f.readline().strip().split("\t")
        lines = f.readlines()
    existing_idx = None
    for i, line in enumerate(lines):
        parts = line.strip().split("\t")
        if parts and parts[0] == row["date"]:
            existing_idx = i
            break
    new_line = "\t".join(str(row.get(col, "")) for col in header) + "\n"
    if existing_idx is not None:
        old_basis = lines[existing_idx].strip().split("\t")
        old_basis = old_basis[header.index("basis")] if "basis" in header and len(old_basis) > header.index("basis") else ""
        if not supersede:
            return "skip-exists"
        if old_basis == "SETTLE" and row.get("basis") != "SETTLE":
            return "skip-tick-vs-settle"  # a TICK never overwrites a SETTLE
        lines[existing_idx] = new_line
        with open(DAILY_LOG, "w") as f:
            f.write("\t".join(header) + "\n")
            f.writelines(lines)
        return "updated"
    with open(DAILY_LOG, "a") as f:
        f.write(new_line)
    return "appended"


def check_stale_tick() -> str | None:
    """Boot-time guard: if the LATEST VX_DAILY row is a TICK dated BEFORE today,
    the EOD settle run was missed and the row is stale. This is the Friday-6/13
    failure mode — no session was alive at 16:15 ET to run --supersede, so the
    row stayed a morning TICK. A closeout checklist can't catch that (nothing
    running at close); the next BOOT can. Returns a warning string or None.
    Repair with backfill.py --spot-only — --supersede only ever targets today.
    """
    if not DAILY_LOG.exists():
        return None
    try:
        with open(DAILY_LOG) as f:
            header = f.readline().rstrip("\n").split("\t")
            last = None
            for line in f:
                if line.strip():
                    last = line.rstrip("\n").split("\t")
        if not last:
            return None
        idx = {c: i for i, c in enumerate(header)}
        if "date" not in idx or "basis" not in idx:
            return None
        d_str = last[idx["date"]]
        basis = last[idx["basis"]] if len(last) > idx["basis"] else ""
        row_date = datetime.fromisoformat(d_str).date()
        today = datetime.now(timezone.utc).astimezone(ET).date()
        if basis == "TICK" and row_date < today:
            return (f"STALE TICK: latest VX_DAILY row {d_str} is TICK basis "
                    f"(EOD settle never logged) — repair: backfill.py --spot-only")
    except (ValueError, KeyError, IndexError):
        return None
    return None


FFWD_COLS = ("vix3m", "vix6m", "vvix", "skew")


def check_fillforward_contamination(scan_rows: int = 30) -> list[str]:
    """DETECTIVE half of the KB-VIO-139 guard (the preventive half lives in
    fetch_spot). Flags rows ALREADY in VX_DAILY.tsv whose companion columns are
    byte-identical to the preceding row's while basis=TICK — the fill-forward
    signature.

    Why a positive check and not a staleness check: the contaminated rows are
    FRESH (written the morning of their own date) and internally plausible, so
    every age-based guard passes them. Only comparison against a source of truth
    — here, the neighbouring row — can see it
    (auto-memory finding_freshness_check_cannot_catch_a_fresh_lie).

    Returns a list of human-readable warnings (empty = clean).
    """
    if not DAILY_LOG.exists():
        return []
    try:
        with open(DAILY_LOG) as f:
            header = f.readline().rstrip("\n").split("\t")
            rows = [ln.rstrip("\n").split("\t") for ln in f if ln.strip()]
    except OSError:
        return []
    idx = {c: i for i, c in enumerate(header)}
    if "basis" not in idx or "date" not in idx:
        return []

    def get(r, col):
        i = idx.get(col)
        return r[i] if i is not None and len(r) > i else ""

    warnings = []
    for r_i in range(max(1, len(rows) - scan_rows), len(rows)):
        cur, prev = rows[r_i], rows[r_i - 1]
        if get(cur, "basis") != "TICK":
            continue
        dup = [c for c in FFWD_COLS
               if get(cur, c) != "" and get(cur, c) == get(prev, c)]
        if len(dup) >= 2:  # 2+ identical companions is the signature, not coincidence
            warnings.append(
                f"FILL-FORWARD CONTAMINATION: {get(cur,'date')} (TICK) carries "
                f"{len(dup)}/{len(FFWD_COLS)} companion columns byte-identical to "
                f"{get(prev,'date')} — {', '.join(dup)}. These indices do not publish "
                f"pre-open; the values are NOT that date's. Any 1-day change computed "
                f"against this row is OVERSTATED. Repair: backfill.py"
            )
    return warnings


def build_report(supersede: bool = False) -> dict:
    now = datetime.now(timezone.utc)
    spot = fetch_spot()
    m1m2 = fetch_m1m2()

    # The ratio is only meaningful if BOTH legs are same-session. When ^VIX3M is
    # suppressed as stale (pre-open), this correctly yields None rather than a
    # cross-date artifact — the 7/30 TICK row printed 1.1268 from a 7/29 VIX3M
    # over a 7/30 VIX, and stand-down (ii) reads off this column (KB-VIO-139).
    ratio = None
    if spot.get("vix") and spot.get("vix3m"):
        ratio = round(spot["vix3m"] / spot["vix"], 4)

    stale = {k: spot[f"{k}_suppressed_value"] for k in TICKERS if spot.get(f"{k}_stale")}
    unverified = [k for k in TICKERS if spot.get(f"{k}_unverified")]

    m1m2_strict = None
    m1m2_adj = None
    m1_sym = ""
    m2_sym = ""
    m1m2_settle_date = ""
    if "_error" not in m1m2 and m1m2:
        m1m2_strict = m1m2["strict"]["steepness_pct"]
        m1m2_adj = m1m2["adjusted"]["steepness_pct"]
        m1_sym = m1m2["adjusted"]["front"]["symbol"]
        m2_sym = m1m2["adjusted"]["back"]["symbol"]
        # The m1m2 columns may be T-1 (or older, after a weekend/holiday) vs
        # the row date — fetch_m1m2 walks back to the most recent settlement.
        # Carry the settlement's own date so no reader mistakes it for a
        # same-day value (CHG-RED-037b; the 6/10 "+7.98% re-armed" misread was
        # this class). Post-16:15 ET this now resolves to the SAME day.
        m1m2_settle_date = m1m2.get("as_of", "")

    et_now = now.astimezone(ET)
    # Spot quotes before the 16:15 ET official settle are intraday ticks,
    # not the daily record — label the row so adjudications can't quote a
    # tick as a settle (futures-settle rule, auto-memory 337f0cfc).
    basis = "SETTLE" if (et_now.hour, et_now.minute) >= (16, 15) else "TICK"

    row = {
        # ET date, not UTC — an evening run after 8pm ET would otherwise
        # stamp tomorrow's date (caught 2026-06-09 20:29 ET → "2026-06-10" row)
        "date": et_now.strftime("%Y-%m-%d"),
        "vix": spot.get("vix") or "",
        "vix3m": spot.get("vix3m") or "",
        "vix6m": spot.get("vix6m") or "",
        "vvix": spot.get("vvix") or "",
        "skew": spot.get("skew") or "",
        "vix3m_vix_ratio": ratio if ratio is not None else "",
        "m1m2_strict_pct": m1m2_strict if m1m2_strict is not None else "",
        "m1m2_adj_pct": m1m2_adj if m1m2_adj is not None else "",
        "m1_symbol": m1_sym,
        "m2_symbol": m2_sym,
        "regime": determine_regime(spot.get("vix")),
        "source_ts": now.isoformat(timespec="seconds"),
        "basis": basis,
        "m1m2_settle_date": m1m2_settle_date,
    }

    classifications = {
        "vix": classify("vix", spot.get("vix")),
        "vvix": classify("vvix", spot.get("vvix")),
        "skew": classify("skew", spot.get("skew")),
        "vix3m_vix_ratio": classify("vix3m_vix_ratio", ratio),
        "m1m2_adj": classify("m1m2_adj_pct", m1m2_adj),
    }

    log_status = append_daily_log(row, supersede=supersede)

    return {
        "row": row,
        "classifications": classifications,
        "appended_to_daily_log": log_status in ("appended", "updated"),  # bool back-compat
        "daily_log_status": log_status,
        "m1m2_raw": m1m2,
        "stale_suppressed": stale,
        "unverified": unverified,
        "ratio_suppressed": bool(stale.get("vix3m") or stale.get("vix")),
    }


def print_report(rep: dict):
    row = rep["row"]
    cls = rep["classifications"]
    print(f"VIOLET THRESHOLDS  {row['date']}  UTC {row['source_ts'][-8:]}")
    print(f"  Regime: {row['regime']}")
    if row.get("basis") == "TICK":
        print(f"  ⚠️  BASIS: TICK (pre-16:15 ET) — spot values are intraday, NOT the daily settle")
    # Fail LOUD, not silent-blank: a nulled column must announce itself, or the
    # guard just trades a wrong value for an unreviewed hole
    # (auto-memory finding_silent_blank_evades_review).
    stale = rep.get("stale_suppressed") or {}
    if stale:
        cols = ", ".join(f"{k}(would have written {v})" for k, v in sorted(stale.items()))
        print(f"  🛡️  STALE-COLUMN GUARD FIRED — wrote NULL for: {cols}")
        print(f"      These indices do not publish pre-open; the quote belonged to a PRIOR session.")
        if rep.get("ratio_suppressed"):
            print(f"      ↳ vix3m_vix_ratio SUPPRESSED too (a cross-date ratio is not a ratio) — "
                  f"stand-down (ii) is UNGRADEABLE off this row, by design.")
    if rep.get("unverified"):
        print(f"  ⚠️  UNVERIFIED data-date (value KEPT, not nulled): {', '.join(rep['unverified'])}")
    print(f"")
    print(f"  {cls['vix']} VIX        {row['vix']:>7}")
    print(f"     VIX3M      {row['vix3m']:>7}")
    print(f"     VIX6M      {row['vix6m']:>7}")
    print(f"  {cls['vvix']} VVIX       {row['vvix']:>7}")
    print(f"  {cls['skew']} SKEW       {row['skew']:>7}")
    print(f"  {cls['vix3m_vix_ratio']} VIX3M/VIX  {row['vix3m_vix_ratio']:>7}")
    if row['m1m2_adj_pct'] != "":
        adj = rep['m1m2_raw']['adjusted']
        strict = rep['m1m2_raw']['strict']
        # State the ACTUAL lag, don't assert a fixed "T-1" — post-settle runs
        # now resolve same-day, and a hardcoded staleness label is exactly the
        # kind of false provenance the settle_date column exists to prevent.
        sd = row.get('m1m2_settle_date') or ""
        if sd:
            lag = (date.fromisoformat(row['date']) - date.fromisoformat(sd)).days
            settle_note = f"settle {sd} — " + (
                "SAME DAY as row" if lag == 0 else f"T-{lag} vs row date"
            )
        else:
            settle_note = "settle date unknown"
        print(f"  {cls['m1m2_adj']} M1:M2 adj  {row['m1m2_adj_pct']:>+7.2f}%  ({row['m1_symbol']}/{row['m2_symbol']})  [{adj['classification']}]  [{settle_note}]")
        if strict['steepness_pct'] != adj['steepness_pct']:
            print(f"     M1:M2 strict {strict['steepness_pct']:+.2f}%  ({strict['m1_days_to_expiry']}d to M1 expiry, roll-contaminated)")
    else:
        err = rep['m1m2_raw'].get('_error', 'unknown')
        print(f"  ⚪ M1:M2 adj  UNAVAILABLE  ({err[:60]})")
    print()
    status = rep.get("daily_log_status", "")
    if status == "appended":
        print(f"  ✓ appended new row to VX_DAILY.tsv")
    elif status == "updated":
        print(f"  ✓ superseded existing {row['date']} row in VX_DAILY.tsv")
    else:
        reason = {
            "skip-weekend": "weekend — markets closed, no settle to log",
            "skip-exists": f"row for {row['date']} already present — pass --supersede to replace a TICK with the SETTLE",
            "skip-tick-vs-settle": f"row for {row['date']} is already SETTLE — a TICK never overwrites it",
            "skip-no-file": "VX_DAILY.tsv not found",
        }.get(status, f"not written ({status})")
        print(f"  · skip ({status}): {reason}")
        if status in ("skip-weekend", "skip-exists", "skip-tick-vs-settle"):
            print(f"     ↳ to repair a stale PRIOR-date row, use backfill.py (--supersede only ever targets today)")

    # Boot-time staleness guard (surfaced via boot.py ⚠️ collapse)
    stale = check_stale_tick()
    if stale:
        print(f"  ⚠️  {stale}")

    # Boot-time fill-forward guard — the DETECTIVE half of KB-VIO-139. Wired
    # here, next to check_stale_tick, because detection was never the gap:
    # this defect was FILED 7/28 and recurred 7/29 and 7/30 unfixed. An
    # un-invoked check is not a mechanism.
    for w in check_fillforward_contamination():
        print(f"  ⚠️  {w}")

    # Emit KEY_MARKERS lines for boot.py collapse mode
    hottest = [f"{k}={cls[k]}" for k in cls if cls[k] in ("🟠", "🔴")]
    if hottest:
        print(f"  ⚠️  ALERT  {' '.join(hottest)}")
    else:
        print(f"  ✓ no threshold breaches")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text")
    parser.add_argument("--supersede", action="store_true",
                        help="Replace today's existing row (EOD SETTLE run replacing an intraday TICK row; TICK never overwrites SETTLE)")
    args = parser.parse_args(argv)

    rep = build_report(supersede=args.supersede)

    if args.json:
        print(json.dumps(rep, indent=2, default=str))
    else:
        print_report(rep)
    return 0


if __name__ == "__main__":
    sys.exit(main())
