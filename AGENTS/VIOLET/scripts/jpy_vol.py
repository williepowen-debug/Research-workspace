#!/usr/bin/env python3
"""VIOLET JPY carry-vol canary — two-legged proxy (realized spine + FXY IV confirm).

Built 2026-07-16 (PROME, Will-authorized cross-agent build; VIOLET ratifies)
per the frozen scope: research/2026-07-11_jpy-vol-instrument-scope.md.
The CBOE FX-vol index family (^JYVIX/^EVZ) is dead — this replaces it.

Leg 1 (spine, always available): USDJPY realized vol from JPY=X daily closes —
rolling 10d/20d annualized RV, percentile-calibrated over a 3y window.
THRESHOLDS ARE RE-DERIVED AT EVERY RUN (percentile-anchored, never hardcoded):
  p90 = WATCH (carry stress building)  → note in NEXUS_BRIEF cross-domain
  p95 = FIRE  (carry-unwind canary)    → outbox to SAM + PROME same session
        (KB-VIO-102 / Aug-2024 replay class; VIOLET owns the vol-transmission
        read, SAM owns the substance)

Leg 2 (confirm, chain-quality-sensitive): FXY near-ATM call IV, OI-filtered
(>=100), most-liquid monthly 25-65 DTE. IV/RV ratio = the event-premium gauge:
  >2x        = event priced
  ->1x calm  = risk passed (post-event, no RV spike)
  RV > IV    = unwind underway (the Aug-2024 signature)
FXY is yen-UP exposure — ATM IV is direction-agnostic; skew excluded (v1 scope).

Data-minute discipline (KB-VIO-100/101 class): FX trades ~24h; the RV leg uses
Yahoo's daily JPY=X bar as-is and stamps its date — with ONE guard: Yahoo rolls
the FX day at ~5 PM ET, so an evening run sees a just-opened FUTURE-dated bar;
any bar dated after "today in ET" is dropped as partial. A bar dated today is
kept (intraday-so-far, like every live level pull). Chain quotes are only
trustworthy intraday — off-RTH runs stamp a STALE caveat on the IV leg.

Appends one row per date to workbook/JPY_VOL.tsv (idempotent per day).

Usage:
  .venv/bin/python3 AGENTS/VIOLET/scripts/jpy_vol.py           # full report
  .venv/bin/python3 AGENTS/VIOLET/scripts/jpy_vol.py --boot    # collapsed
  .venv/bin/python3 AGENTS/VIOLET/scripts/jpy_vol.py --json
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")

SCRIPT_DIR = Path(__file__).resolve().parent
VIOLET_DIR = SCRIPT_DIR.parent
DAILY_LOG = VIOLET_DIR / "workbook" / "JPY_VOL.tsv"

HISTORY = "3y"          # percentile window (self-updating; re-derive, don't pin)
RV_WINDOWS = (10, 20)   # rolling realized-vol windows (trading days)
ANNUALIZE = 252
OI_FLOOR = 100          # confirm-leg strike liquidity floor (scope §4)
ATM_BAND = 0.05         # strikes within +/-5% of spot count as near-ATM
DTE_RANGE = (25, 65)    # candidate confirm-leg expiries
IV_EVENT_PRICED = 2.0   # IV/RV above this = event premium priced

TSV_COLS = ["date", "jpy_close", "rv10", "rv20", "rv10_pctile", "p90_watch",
            "p95_fire", "fxy_spot", "fxy_expiry", "atm_call_iv", "iv_rv10",
            "state", "iv_leg_note", "stamp_utc"]


def pull_realized() -> dict:
    """Leg 1: JPY=X 3y daily -> rolling RV + percentile ladder (re-derived)."""
    import yfinance as yf

    hist = yf.Ticker("JPY=X").history(period=HISTORY, auto_adjust=False)
    if hist is None or len(hist) < 300:
        raise RuntimeError(f"JPY=X history too short ({0 if hist is None else len(hist)} rows)")
    close = hist["Close"].dropna()
    # Future-stamped bar guard: Yahoo rolls the FX day ~5 PM ET — an evening run
    # sees a just-opened bar dated tomorrow. Drop bars dated past ET-today.
    et_today = datetime.now(ET).date()
    close = close[[d.date() <= et_today for d in close.index]]
    logret = (close / close.shift(1)).apply(math.log).dropna()

    rv = {}
    for w in RV_WINDOWS:
        rv[w] = logret.rolling(w).std() * math.sqrt(ANNUALIZE) * 100.0
    rv10 = rv[10].dropna()

    ladder = {p: float(rv10.quantile(p / 100.0)) for p in (50, 75, 90, 95, 99)}
    peak_idx = rv10.idxmax()
    aug24 = rv10[(rv10.index >= "2024-07-15") & (rv10.index <= "2024-09-15")]

    return {
        "asof": str(close.index[-1].date()),
        "jpy_close": round(float(close.iloc[-1]), 2),
        "rv10": round(float(rv[10].iloc[-1]), 2),
        "rv20": round(float(rv[20].iloc[-1]), 2),
        "rv10_pctile": round(float((rv10 <= rv[10].iloc[-1]).mean() * 100.0), 1),
        "ladder": {f"p{p}": round(v, 2) for p, v in ladder.items()},
        "n_obs": int(len(rv10)),
        "window_start": str(rv10.index[0].date()),
        "max": {"value": round(float(rv10.max()), 2), "date": str(peak_idx.date())},
        # Aug-2024 carry-unwind anchor — reported only while the rolling window
        # still covers it (it ages out mid-2027); absence is not an error.
        "aug2024_peak": (
            {"value": round(float(aug24.max()), 2), "date": str(aug24.idxmax().date())}
            if len(aug24) else None),
    }


def pull_fxy_iv(rv10: float) -> dict:
    """Leg 2: FXY OI-filtered near-ATM call IV on the most-liquid 25-65 DTE expiry."""
    import yfinance as yf

    out = {"fxy_spot": None, "expiry": None, "dte": None, "atm_call_iv": None,
           "iv_rv10": None, "n_strikes": 0, "note": ""}
    try:
        tk = yf.Ticker("FXY")
        spot = float(tk.fast_info["lastPrice"])
        out["fxy_spot"] = round(spot, 2)
        today = date.today()
        candidates = []
        for exp_s in tk.options or []:
            try:
                dte = (datetime.strptime(exp_s, "%Y-%m-%d").date() - today).days
            except ValueError:
                continue
            if DTE_RANGE[0] <= dte <= DTE_RANGE[1]:
                candidates.append((exp_s, dte))
        if not candidates:
            out["note"] = f"no FXY expiry inside {DTE_RANGE} DTE"
            return out

        best = None
        for exp_s, dte in candidates:
            try:
                calls = tk.option_chain(exp_s).calls
            except Exception as e:
                out["note"] = f"chain fetch failed: {str(e)[:60]}"
                continue
            near = calls[
                (calls.strike >= spot * (1 - ATM_BAND))
                & (calls.strike <= spot * (1 + ATM_BAND))
                & (calls.openInterest.fillna(0) >= OI_FLOOR)
                & (calls.impliedVolatility.notna())
            ]
            oi = int(near.openInterest.sum()) if len(near) else 0
            if len(near) and (best is None or oi > best["oi"]):
                iv = float((near.impliedVolatility * near.openInterest).sum()
                           / near.openInterest.sum()) * 100.0
                best = {"exp": exp_s, "dte": dte, "iv": iv, "n": len(near), "oi": oi}
        if best is None:
            out["note"] = f"no near-ATM call passes OI>={OI_FLOOR} in {DTE_RANGE} DTE (thin-strike guard held)"
            return out
        out.update({"expiry": best["exp"], "dte": best["dte"],
                    "atm_call_iv": round(best["iv"], 1), "n_strikes": best["n"],
                    "iv_rv10": round(best["iv"] / rv10, 2) if rv10 else None})
        # Off-RTH staleness stamp (scope §4: chain trustworthy intraday only)
        now_et = datetime.now(ET)
        if not (9 <= now_et.hour < 16) or now_et.weekday() >= 5:
            out["note"] = "STALE quotes (off-RTH pull) — confirm intraday before acting on the IV leg"
    except Exception as e:
        out["note"] = f"IV leg unavailable: {str(e)[:80]}"
    return out


def classify(rv: dict, iv: dict) -> tuple[str, list[str]]:
    p90, p95 = rv["ladder"]["p90"], rv["ladder"]["p95"]
    lines = []
    if rv["rv10"] >= p95:
        state = "FIRE"
        lines.append(f"🔴 FIRE: 10d RV {rv['rv10']}% >= p95 {p95}% — carry-unwind canary. "
                     f"ROUTE: outbox to SAM + PROME same session (KB-VIO-102 / Aug-2024 replay class).")
    elif rv["rv10"] >= p90:
        state = "WATCH"
        lines.append(f"🟠 WATCH: 10d RV {rv['rv10']}% >= p90 {p90}% — carry stress building. "
                     f"ROUTE: note in NEXUS_BRIEF cross-domain.")
    else:
        state = "CALM"
        lines.append(f"🟢 CALM: 10d RV {rv['rv10']}% (p{rv['rv10_pctile']} of 3y) vs WATCH {p90}% / FIRE {p95}%.")
    r = iv.get("iv_rv10")
    if r is not None:
        if rv["rv10"] > (iv.get("atm_call_iv") or 0):
            lines.append(f"🔴 RV THROUGH IV ({rv['rv10']}% > {iv['atm_call_iv']}%) — unwind-underway signature (Aug-2024 class).")
        elif r >= IV_EVENT_PRICED:
            lines.append(f"🟡 IV/RV {r}x >= {IV_EVENT_PRICED}x — options carrying an event premium the realized leg can't see.")
        else:
            lines.append(f"IV/RV {r}x — no outsized event premium (collapse toward 1x post-event w/o an RV spike = risk passed).")
    return state, lines


def append_log(rv: dict, iv: dict, state: str) -> str:
    DAILY_LOG.parent.mkdir(parents=True, exist_ok=True)
    if not DAILY_LOG.exists():
        DAILY_LOG.write_text("\t".join(TSV_COLS) + "\n", encoding="utf-8")
    existing = DAILY_LOG.read_text(encoding="utf-8").splitlines()
    if any(line.startswith(rv["asof"] + "\t") for line in existing[1:]):
        return f"already has a row for {rv['asof']}"
    row = [rv["asof"], rv["jpy_close"], rv["rv10"], rv["rv20"], rv["rv10_pctile"],
           rv["ladder"]["p90"], rv["ladder"]["p95"], iv.get("fxy_spot"),
           iv.get("expiry"), iv.get("atm_call_iv"), iv.get("iv_rv10"),
           state, iv.get("note") or "-",
           datetime.now(timezone.utc).isoformat(timespec="seconds")]
    with DAILY_LOG.open("a", encoding="utf-8") as f:
        f.write("\t".join(str(x) if x is not None else "-" for x in row) + "\n")
    return f"✓ appended {rv['asof']} row to workbook/JPY_VOL.tsv"


def main() -> int:
    ap = argparse.ArgumentParser(description="JPY carry-vol canary (RV spine + FXY IV confirm)")
    ap.add_argument("--boot", action="store_true", help="collapsed boot output")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--no-log", action="store_true", help="skip the TSV append")
    args = ap.parse_args()

    try:
        rv = pull_realized()
    except Exception as e:
        print(f"⚠️ JPY VOL: realized leg FAILED ({e}) — no silent pass, investigate")
        return 1
    iv = pull_fxy_iv(rv["rv10"])
    state, verdict_lines = classify(rv, iv)
    log_note = "" if args.no_log else append_log(rv, iv, state)

    if args.json:
        print(json.dumps({"rv": rv, "iv": iv, "state": state, "log": log_note}, indent=2))
        return 0

    print(f"JPY VOL [{rv['asof']}]: USDJPY {rv['jpy_close']} · RV10 {rv['rv10']}% · RV20 {rv['rv20']}% "
          f"· pctile p{rv['rv10_pctile']} · state {state}")
    for line in verdict_lines:
        print(line)
    if iv.get("atm_call_iv") is not None:
        stale = f" ⚠️ {iv['note']}" if iv.get("note") else ""
        print(f"FXY confirm leg: spot {iv['fxy_spot']} · {iv['expiry']} ({iv['dte']} DTE) "
              f"OI-weighted near-ATM call IV {iv['atm_call_iv']}% ({iv['n_strikes']} strikes, OI>={OI_FLOOR}){stale}")
    elif iv.get("note"):
        print(f"⚠️ FXY confirm leg: {iv['note']}")
    if not args.boot:
        lad = rv["ladder"]
        anchors = f"3y max {rv['max']['value']}% ({rv['max']['date']})"
        if rv["aug2024_peak"]:
            anchors += f" · Aug-2024 carry-unwind peak {rv['aug2024_peak']['value']}% ({rv['aug2024_peak']['date']})"
        print(f"Ladder (re-derived, n={rv['n_obs']} from {rv['window_start']}): "
              f"p50 {lad['p50']} · p75 {lad['p75']} · p90 {lad['p90']} WATCH · "
              f"p95 {lad['p95']} FIRE · p99 {lad['p99']} — {anchors}")
    if log_note:
        print(log_note)
    return 0


if __name__ == "__main__":
    sys.exit(main())
