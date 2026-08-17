#!/usr/bin/env python3
"""
SAM FXY Options Monitor
Pulls FXY options chains via yfinance for the next 4 expiries.
Computes put/call OI, P/C ratio, top strikes, and flags OI building in the
thesis strike zone ($58-65 — where thesis confirmation play sits).
Appends snapshot to workbook/FXY_OPTIONS.tsv for historical tracking.

Usage:
  .venv/bin/python3 AGENTS/SAM/scripts/fxy_options.py
  .venv/bin/python3 AGENTS/SAM/scripts/fxy_options.py --print   # print latest from TSV
  .venv/bin/python3 AGENTS/SAM/scripts/fxy_options.py --expiries 6
"""

import sys
import math
from datetime import datetime, date
from pathlib import Path

try:
    import yfinance as yf
except ImportError:
    print("  ERROR: yfinance not installed.")
    sys.exit(1)

SAM_DIR = Path(__file__).resolve().parent.parent
WORKBOOK = SAM_DIR / "workbook"
FXY_TSV = WORKBOOK / "FXY_OPTIONS.tsv"

# Thesis strike zone — where FXY thesis plays out
# Stop at $55.05, entry ~$57.36, target $60-62, upper target $65
THESIS_ZONE_LOW = 58.0
THESIS_ZONE_HIGH = 65.0

# Vol-proxy parameters (CVOL/RR proxy computed from the FXY chain)
RFR = 0.0          # risk-free proxy for BS delta classification; r≈0 is fine for a proxy
TARGET_DTE = 30    # headline IV/RR is the expiry nearest this (mirrors CVOL's 30d horizon)

# --- Self-calibration + provenance parameters ---------------------------------
# The FXY-proxy RR has no meaningful absolute scale (it runs ~10x steeper than OTC
# USD/JPY RR), so a raw number can't be read against the framework's OTC thresholds.
# We instead calibrate each reading against its OWN trailing history. These three
# constants govern that. NOTE: values marked [RECONSTRUCTED] are SAM-reviewable —
# the original (crashed) session's exact choices were not recoverable; see commit msg.
METHOD_VER = "fxy-proxy-v1"   # provenance tag for the compute_iv_skew math. Bump on any
                              # methodology change; calibration only mixes same-version
                              # readings so a method change can't silently corrupt the series.
MIN_HISTORY = 8               # prior readings required before self-calibration activates
                              # (matches the "building history (n/8)" floor from the spec).
CALIB_WINDOW_DAYS = 60        # trailing window for the RR mean/stdev ("60-day average").

TSV_HEADER = (
    "Date\tExpiry\tTotal_Put_OI\tTotal_Call_OI\tPC_Ratio\tThesis_Zone_Call_OI\t"
    "Top_Put_Strike\tTop_Put_OI\tTop_Call_Strike\tTop_Call_OI\tTop5_Puts\tTop5_Calls\t"
    "ATM_IV_pct\tRR25_USDJPY\tMethod_Ver\tVol_Quality\n"
)
NUM_COLS = 16  # column count after the self-calibration / provenance migration


# --------------------------------------------------------------------------
# Vol proxy: ATM IV (CVOL proxy) + 25-delta risk reversal (USD/JPY convention)
#
# SIGN CONVENTION — read carefully:
#   FXY moves INVERSELY to USD/JPY (FXY up = yen up = USD/JPY down).
#   So a USD/JPY put ≈ an FXY call.  Therefore:
#       USD/JPY 25d RR  =  IV(USDJPY 25d call) − IV(USDJPY 25d put)
#                       ≈  IV(FXY 25d put)     − IV(FXY 25d call)
#   We report the USD/JPY convention so it plugs into VOL_OPTIONS_FRAMEWORK.md:
#       NEGATIVE RR = puts richer = yen-strength crash protection bid = THESIS firing.
# --------------------------------------------------------------------------

def _norm_cdf(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def _valid_iv(v):
    """yfinance IV is a decimal (0.10 = 10%). Reject NaN and insane values."""
    return v == v and 0.001 < v < 3.0


def _bs_delta(opt_type, S, K, T, iv):
    """Black-Scholes delta (American FXY options approximated as European — fine for
    25-delta strike classification on a proxy)."""
    if S <= 0 or K <= 0 or T <= 0 or iv <= 0:
        return None
    d1 = (math.log(S / K) + (RFR + 0.5 * iv * iv) * T) / (iv * math.sqrt(T))
    return _norm_cdf(d1) if opt_type == "call" else _norm_cdf(d1) - 1.0


def compute_iv_skew(calls, puts, spot, dte):
    """Return (atm_iv_pct, rr25_usdjpy, note). Degrades gracefully to (None, None, reason)
    so it can NEVER break the OI pull / boot sweep."""
    if spot is None or spot <= 0 or not dte or dte <= 0:
        return None, None, "no spot/dte"
    T = dte / 365.0

    # --- ATM IV: IV at the strike nearest spot, averaged across call+put ---
    atm_iv = None
    try:
        ivs = []
        for df in (calls, puts):
            if "impliedVolatility" not in df.columns or "strike" not in df.columns:
                continue
            v = df[df["impliedVolatility"].apply(_valid_iv)].reset_index(drop=True)
            if len(v):
                i = (v["strike"] - spot).abs().idxmin()
                ivs.append(float(v.loc[i, "impliedVolatility"]))
        if ivs:
            atm_iv = sum(ivs) / len(ivs)
    except Exception:
        atm_iv = None

    # --- 25-delta RR (USD/JPY convention = FXY put IV − FXY call IV) ---
    rr = None
    note = ""
    try:
        def _otm(df, side):
            v = df[df["impliedVolatility"].apply(_valid_iv)].copy()
            if "openInterest" in v.columns:
                v = v[v["openInterest"] > 0]
            v = v[(v["strike"] >= spot)] if side == "call" else v[(v["strike"] <= spot)]
            v = v.reset_index(drop=True)
            if not len(v):
                return None
            v["delta"] = v.apply(
                lambda r: _bs_delta(side, spot, r["strike"], T, r["impliedVolatility"]), axis=1
            )
            v = v.dropna(subset=["delta"]).reset_index(drop=True)
            if not len(v):
                return None
            target = 0.25 if side == "call" else -0.25
            i = (v["delta"] - target).abs().idxmin()
            return v.loc[i]

        call25 = _otm(calls, "call")
        put25 = _otm(puts, "put")
        if call25 is not None and put25 is not None:
            rr = (float(put25["impliedVolatility"]) - float(call25["impliedVolatility"])) * 100.0
            if abs(call25["delta"] - 0.25) > 0.12 or abs(put25["delta"] + 0.25) > 0.12:
                note = "approx (thin wings)"
        else:
            note = "RR n/a (thin wings)"
    except Exception:
        note = "RR calc error"

    return (
        round(atm_iv * 100.0, 2) if atm_iv is not None else None,
        round(rr, 2) if rr is not None else None,
        note,
    )


def _iv_flag(iv_pct):
    """Framework CVOL thresholds (VOL_OPTIONS_FRAMEWORK.md §1)."""
    if iv_pct is None:
        return ""
    if iv_pct < 10:
        return "🟢 carry-grind"
    if iv_pct < 12:
        return "🟡 early shift"
    if iv_pct < 15:
        return "🟠 event premium"
    if iv_pct < 18:
        return "🟠 elevated"
    return "🔴 stress"


# A 25-delta risk reversal is quoted in VOL POINTS. Real OTC USD/JPY RR lives within
# roughly +/-3 vols; an ETF proxy runs structurally steeper, but double-digit values mean
# one wing was priced off a stale/absent/one-tick quote, not that skew is extreme.
# Above this the number is NON-PHYSICAL and must not be read for direction at all.
# Chosen deliberately loose (~2x the widest defensible ETF skew) so it removes garbage,
# not signal. Provenance: SAM 2026-08-04, after the proxy printed Aug-21 +3.42 -> -77.0
# -> -32.18 and Sep-18 -24.66 -> -5.66 -> +19.95 on three consecutive sessions --
# the SIGN itself flipped daily, so KB-183's "read the sign, not the level" had no
# signal left to read, yet every one of those readings was graded "ok"/"approx".
RR_IMPLAUSIBLE_ABS = 10.0


def rr_is_readable(rr):
    """True only if rr is present AND physically plausible. The old code conflated
    'computable' with 'trustworthy' -- that is the whole defect this closes."""
    return rr is not None and abs(rr) <= RR_IMPLAUSIBLE_ABS


def _rr_flag(rr):
    """SIGN/direction interpretation only. NOTE: FXY ETF option skew runs structurally
    much steeper than USD/JPY OTC RR, so the framework's absolute OTC thresholds
    (-0.3/-0.7 = stress) DO NOT transfer to this proxy. Track the trend vs its own
    history; here we only read the sign + which side is bid.
    Refuses to emit ANY direction when the value is non-physical -- printing
    'calls bid' off a -77 vol reading is worse than printing nothing."""
    if rr is None:
        return ""
    if not rr_is_readable(rr):
        return (f"UNREADABLE - |RR| {abs(rr):.1f} > {RR_IMPLAUSIBLE_ABS:.0f} vols is "
                f"non-physical (thin/stale wing). NO directional read. Price off the live chain")
    if rr <= -0.5:
        return "↓ FXY calls bid = yen-strength demand (thesis-side)"
    if rr < 0.5:
        return "→ ~symmetric skew"
    return "↑ FXY puts bid = yen-weakness demand (counter-thesis)"


def _vol_quality(atm_iv_pct, rr25, note):
    """Provenance quality grade for one reading — gates what feeds self-calibration.
    [RECONSTRUCTED buckets — SAM-reviewable] Derived from what compute_iv_skew returned:
      ok      — both ATM IV and a clean RR present
      approx  — RR present but wings were thin / interpolated (note says approx/thin)
      rr_na   — ATM IV present but RR couldn't be computed (no usable wings)
      none    — no usable vol data at all
    Calibration counts only 'ok' (and 'approx') readings; 'rr_na'/'none' never pollute
    the trailing series."""
    n = (note or "").lower()
    if rr25 is not None:
        # Plausibility gate BEFORE the thin/approx grade: a non-physical magnitude is a
        # data defect, not a lower-confidence reading, and must never reach calibration.
        if not rr_is_readable(rr25):
            return "rr_implausible"
        return "approx" if ("approx" in n or "thin" in n) else "ok"
    if atm_iv_pct is not None:
        return "rr_na"
    return "none"


# Quality grades admissible into the trailing RR series.
# NB "rr_implausible" is deliberately EXCLUDED -- it is a defect grade, not a weak one.
CALIB_OK_QUALITY = ("ok", "approx")


def _headline_rr_series(window_days=CALIB_WINDOW_DAYS, method_ver=METHOD_VER):
    """Build the trailing headline-RR series from the TSV — ONE reading per date.

    For each date we keep the expiry whose days-to-expiry (recomputed from Date/Expiry)
    is nearest TARGET_DTE, mirroring the live headline pick. A reading is admitted only
    if it (a) carries the current Method_Ver (so a methodology change can't contaminate
    the series), (b) has an admissible Vol_Quality, and (c) falls within window_days of
    the most recent dated row. Returns an ordered list of (date_str, rr) — oldest first.
    """
    if not FXY_TSV.exists():
        return []
    lines = FXY_TSV.read_text().splitlines()
    if len(lines) < 2:
        return []

    # date -> (best_dte_gap, rr) for the headline expiry on that date
    best = {}
    all_dates = []
    for ln in lines[1:]:
        if not ln.strip():
            continue
        cols = ln.split("\t")
        while len(cols) < NUM_COLS:
            cols.append("")
        d_str, exp_str = cols[0], cols[1]
        rr_str, mver, qual = cols[13], cols[14], cols[15]
        if mver != method_ver or qual not in CALIB_OK_QUALITY or not rr_str:
            continue
        try:
            d = datetime.strptime(d_str, "%Y-%m-%d").date()
            e = datetime.strptime(exp_str, "%Y-%m-%d").date()
            rr = float(rr_str)
        except Exception:
            continue
        gap = abs((e - d).days - TARGET_DTE)
        if d_str not in best or gap < best[d_str][0]:
            best[d_str] = (gap, rr)
        all_dates.append(d)

    if not best:
        return []

    latest = max(all_dates)
    series = []
    for d_str in sorted(best):
        d = datetime.strptime(d_str, "%Y-%m-%d").date()
        if (latest - d).days <= window_days:
            series.append((d_str, best[d_str][1]))
    return series


def calibrate_rr(current_date, current_rr):
    """Self-calibrate the current headline RR against its own trailing history.

    Returns a dict the printer can render directly. While history is short it reports
    progress ("building history (n/8)"); once MIN_HISTORY priors exist it reports the
    z-score and raw deviation of today's RR vs the trailing mean. The load-bearing read
    is DIRECTION: a z far below 0 = RR more negative than its own norm (yen-strength /
    call demand intensifying, thesis-side); a z above 0 = RR moving toward zero
    (long-yen positioning UNWINDING — the genuine early-warning the spec called out)."""
    if current_rr is None:
        return {"state": "no_reading"}

    # Priors = trailing series EXCLUDING any row already stamped for today (avoid self-count).
    series = [(d, rr) for (d, rr) in _headline_rr_series() if d != current_date]
    n = len(series)
    if n < MIN_HISTORY:
        return {"state": "building", "n": n, "need": MIN_HISTORY}

    vals = [rr for _, rr in series]
    mean = sum(vals) / n
    var = sum((v - mean) ** 2 for v in vals) / (n - 1)  # sample stdev
    sd = math.sqrt(var)
    delta = current_rr - mean
    z = delta / sd if sd > 0 else 0.0

    if z <= -1.0:
        interp = "↓↓ RR well below own norm — yen-strength demand intensifying (thesis-side)"
    elif z < -0.5:
        interp = "↓ RR below own norm — leaning thesis-side"
    elif z <= 0.5:
        interp = "→ RR in line with own norm"
    elif z < 1.0:
        interp = "↑ RR above own norm — drifting toward zero (positioning easing)"
    else:
        interp = "↑↑ RR well above own norm — long-yen positioning UNWINDING (early-warning)"

    return {
        "state": "calibrated", "n": n, "mean": mean, "sd": sd,
        "delta": delta, "z": z, "interp": interp,
    }


def get_fxy_options(num_expiries=4):
    """Fetch FXY options data for next N expiries. Returns list of dicts."""
    try:
        t = yf.Ticker("FXY")
        expiries = t.options
        if not expiries:
            return [], None, None

        # ⚠️ SPOT PROVENANCE (added 2026-08-17, DAEDALUS SFG sweep ACTION 4).
        # `spot` is not decoration — it anchors WHICH STRIKES get read: the ATM IV
        # pick (`(strike - spot).abs().idxmin()`) and the 25-delta wing selection
        # (`_bs_delta(side, spot, ...)`). This chain silently degrades
        # regularMarketPrice → previousClose (a DIFFERENT SESSION) → history 1d,
        # each behind a bare except; a stale spot therefore re-anchors the read and
        # ATM IV / 25d RR still print clean lines with a directional thesis-side
        # verdict, unmarked, rc=0. The 8/4 value-layer guards the VALUE
        # (rr_is_readable / RR_IMPLAUSIBLE_ABS); nothing guarded the INPUT.
        # Track which leg answered so the caller can refuse the directional read.
        current_price = None
        spot_source = None
        try:
            info = t.info
            if info.get("regularMarketPrice"):
                current_price = info.get("regularMarketPrice")
                spot_source = "regularMarketPrice"   # live — directional read OK
            elif info.get("previousClose"):
                current_price = info.get("previousClose")
                spot_source = "previousClose"        # STALE: prior session
        except Exception:
            pass
        if not current_price:  # fallback if .info is flaky — needed for ATM/delta
            try:
                current_price = float(t.history(period="1d")["Close"].iloc[-1])
                spot_source = "history_1d"           # STALE: last daily close
            except Exception:
                pass
    except Exception as e:
        print(f"  ERROR fetching FXY options: {e}")
        return [], None, None

    today = date.today()

    results = []
    for expiry in expiries[:num_expiries]:
        try:
            chain = t.option_chain(expiry)
            puts = chain.puts
            calls = chain.calls

            total_put_oi = int(puts["openInterest"].sum()) if "openInterest" in puts.columns else 0
            total_call_oi = int(calls["openInterest"].sum()) if "openInterest" in calls.columns else 0

            # Thesis zone call OI — bullish positioning in our target range
            zone_call_oi = 0
            if "openInterest" in calls.columns and "strike" in calls.columns:
                zone_mask = (calls["strike"] >= THESIS_ZONE_LOW) & (calls["strike"] <= THESIS_ZONE_HIGH)
                zone_call_oi = int(calls.loc[zone_mask, "openInterest"].sum())

            # ⚠️ None, NOT a 999.0 sentinel (fixed 2026-08-17, DAEDALUS SFG sweep
            # ACTION 3). An empty call-OI DENOMINATOR means the chain gave us
            # nothing to divide by — that is a data ABSENCE. The old 999.0 sentinel
            # flowed straight into the "🔴 Put-heavy (bearish)" branch below, so
            # "we got no data" rendered as the most bearish reading the script can
            # produce, and one such row (2026-06-21: puts 0 / calls 0 / PC 999.0)
            # is live in FXY_OPTIONS.tsv. Same class as the jgb_auctions and
            # cpi_japan defects: absence rendering as evidence.
            pc_ratio = round(total_put_oi / total_call_oi, 2) if total_call_oi > 0 else None

            # Vol proxy: ATM IV + 25d RR for this expiry (fail-safe — never raises)
            try:
                dte = (datetime.strptime(expiry, "%Y-%m-%d").date() - today).days
            except Exception:
                dte = None
            atm_iv_pct, rr25, iv_note = compute_iv_skew(calls, puts, current_price, dte)

            # Top 5 puts and calls by OI
            top_puts = []
            if "openInterest" in puts.columns and len(puts) > 0:
                sorted_puts = puts.sort_values("openInterest", ascending=False).head(5)
                for _, row in sorted_puts.iterrows():
                    oi = int(row["openInterest"]) if row["openInterest"] == row["openInterest"] else 0
                    if oi > 0:
                        top_puts.append((row["strike"], oi))

            top_calls = []
            if "openInterest" in calls.columns and len(calls) > 0:
                sorted_calls = calls.sort_values("openInterest", ascending=False).head(5)
                for _, row in sorted_calls.iterrows():
                    oi = int(row["openInterest"]) if row["openInterest"] == row["openInterest"] else 0
                    if oi > 0:
                        top_calls.append((row["strike"], oi))

            results.append({
                "expiry": expiry,
                "dte": dte,
                "total_put_oi": total_put_oi,
                "total_call_oi": total_call_oi,
                "pc_ratio": pc_ratio,
                "zone_call_oi": zone_call_oi,
                "top_put": top_puts[0] if top_puts else (0, 0),
                "top_call": top_calls[0] if top_calls else (0, 0),
                "top5_puts": top_puts,
                "top5_calls": top_calls,
                "atm_iv_pct": atm_iv_pct,
                "rr25": rr25,
                "iv_note": iv_note,
            })
        except Exception:
            continue

    return results, current_price, spot_source


def _ensure_schema():
    """Migrate older TSV rows up to the current 16-col schema. Handles both the
    pre-vol-proxy (12-col) layout and the 14-col vol-proxy layout, padding to 16.
    Also backfills provenance on any row that already has an RR but predates the
    Method_Ver/Vol_Quality columns: such a reading was, by definition, produced by
    the only method that existed (the current one), so we stamp METHOD_VER and grade
    its quality so it becomes admissible to self-calibration. Idempotent."""
    if not FXY_TSV.exists():
        return
    lines = FXY_TSV.read_text().splitlines()
    if not lines or lines[0] == TSV_HEADER.strip():
        return  # already migrated (or empty)
    new_lines = [TSV_HEADER.strip()]
    for ln in lines[1:]:
        if not ln.strip():
            continue
        cols = ln.split("\t")
        while len(cols) < NUM_COLS:
            cols.append("")  # pad ATM_IV_pct / RR25 / Method_Ver / Vol_Quality
        # Backfill provenance for legacy rows that carry vol data but no version tag.
        if cols[13] and not cols[14]:
            cols[14] = METHOD_VER
        if (cols[12] or cols[13]) and not cols[15]:
            iv = float(cols[12]) if cols[12] else None
            rr = float(cols[13]) if cols[13] else None
            cols[15] = _vol_quality(iv, rr, "")
        new_lines.append("\t".join(cols))
    FXY_TSV.write_text("\n".join(new_lines) + "\n")


def _row_for(date_str, d):
    """Build the 16-col TSV row (list) for one expiry's data."""
    puts_str = "; ".join(f"${s:.0f}={oi}" for s, oi in d["top5_puts"])
    calls_str = "; ".join(f"${s:.0f}={oi}" for s, oi in d["top5_calls"])
    iv = d.get("atm_iv_pct")
    rr = d.get("rr25")
    iv_str = "" if iv is None else f"{iv}"
    rr_str = "" if rr is None else f"{rr}"
    quality = _vol_quality(iv, rr, d.get("iv_note"))
    # Method_Ver is only meaningful once we actually computed a vol reading.
    method = METHOD_VER if (iv is not None or rr is not None) else ""
    return [
        date_str, d["expiry"], str(d["total_put_oi"]), str(d["total_call_oi"]),
        ("NA" if d["pc_ratio"] is None else str(d["pc_ratio"])),
        str(d["zone_call_oi"]), str(d["top_put"][0]), str(d["top_put"][1]),
        str(d["top_call"][0]), str(d["top_call"][1]), puts_str, calls_str, iv_str, rr_str,
        method, quality,
    ]


def append_tsv(date_str, data_list):
    """Upsert today's options data into the TSV: add new (date, expiry) rows, and
    backfill ATM_IV/RR on an existing row when it's blank and we now have values.
    Idempotent — re-running the same day won't duplicate, and self-heals partial pulls."""
    _ensure_schema()
    rows = []          # ordered list of column-lists
    index = {}         # (date, expiry) -> position in rows
    if FXY_TSV.exists():
        for line in FXY_TSV.read_text().splitlines()[1:]:
            if not line.strip():
                continue
            cols = line.split("\t")
            while len(cols) < NUM_COLS:
                cols.append("")
            index[(cols[0], cols[1])] = len(rows)
            rows.append(cols)

    changed = 0
    for d in data_list:
        key = (date_str, d["expiry"])
        new_cols = _row_for(date_str, d)
        if key in index:
            cur = rows[index[key]]
            # backfill IV (12) / RR (13) / Method_Ver (14) / Vol_Quality (15) if
            # currently blank and now available (self-heals partial earlier pulls).
            upgraded = False
            for ci in (12, 13, 14, 15):
                if not cur[ci] and new_cols[ci]:
                    cur[ci] = new_cols[ci]
                    upgraded = True
            if upgraded:
                changed += 1
        else:
            index[key] = len(rows)
            rows.append(new_cols)
            changed += 1

    with open(FXY_TSV, "w") as f:
        f.write(TSV_HEADER)
        for cols in rows:
            f.write("\t".join(cols) + "\n")
    return changed


def print_from_tsv():
    """Print latest TSV snapshot."""
    if not FXY_TSV.exists():
        print(f"  No {FXY_TSV.name} yet.")
        return
    with open(FXY_TSV) as f:
        print(f.read())


def main():
    if "--print" in sys.argv:
        print_from_tsv()
        return 0

    num_expiries = 4
    if "--expiries" in sys.argv:
        idx = sys.argv.index("--expiries")
        if idx + 1 < len(sys.argv):
            num_expiries = int(sys.argv[idx + 1])

    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")

    print(f"\n{'='*70}")
    print(f"  SAM FXY Options Monitor — {now.strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*70}")

    data, current_price, spot_source = get_fxy_options(num_expiries=num_expiries)
    if not data:
        print("\n  ERROR: No FXY options data available.")
        return 1

    # Spot provenance is printed, not assumed (ACTION 4). `spot` decides WHICH
    # strikes the ATM IV and 25d RR are read off, so a fallback-sourced spot
    # silently re-anchors the whole vol block.
    _SPOT_LABEL = {"regularMarketPrice": "live", "previousClose": "PRIOR SESSION CLOSE",
                   "history_1d": "LAST DAILY CLOSE"}
    spot_is_live = (spot_source == "regularMarketPrice")
    if current_price:
        src = _SPOT_LABEL.get(spot_source, "UNKNOWN SOURCE")
        print(f"\n  FXY spot: ${current_price:.2f}   [source: {src}]")
        if not spot_is_live:
            print(f"  ⚠️  SPOT CAME OFF THE FALLBACK CHAIN ({src}) — it anchors the ATM "
                  f"strike and the 25d wings, so the vol block below is computed against "
                  f"a stale reference. Levels are indicative; the RR DIRECTIONAL read is "
                  f"suppressed.")
    print(f"  Thesis strike zone: ${THESIS_ZONE_LOW:.0f}–${THESIS_ZONE_HIGH:.0f} (target $60-62)")
    print(f"  Expiries scanned: {len(data)}")

    # Aggregate view
    total_puts = sum(d["total_put_oi"] for d in data)
    total_calls = sum(d["total_call_oi"] for d in data)
    total_zone_calls = sum(d["zone_call_oi"] for d in data)
    agg_pc = round(total_puts / total_calls, 2) if total_calls > 0 else None
    zone_pct = (total_zone_calls / total_calls * 100) if total_calls > 0 else 0

    print(f"\n  {'AGGREGATE'}")
    print(f"  {'-'*60}")
    print(f"  Total Put OI:          {total_puts:>10,}")
    print(f"  Total Call OI:         {total_calls:>10,}")
    if agg_pc is None:
        # ⚠️ NO directional verdict off an empty denominator (ACTION 3). The old
        # code substituted 999.0 here and fell through to "🔴 Put-heavy (bearish)",
        # printing the script's most bearish reading precisely when it had no data.
        print(f"  P/C Ratio:             {'UNAVAILABLE':>10}")
        print(f"  🔴 NO CALL OI — the denominator is empty. This is a DATA GAP, "
              f"NOT a bearish signal. Do not read positioning off this run.")
        unavailable = True
    else:
        unavailable = False
        print(f"  P/C Ratio:             {agg_pc:>10.2f}x", end="")
        if agg_pc < 0.5:
            print("  🟢 Call-heavy (bullish)")
        elif agg_pc < 1.0:
            print("  🟢 Modestly bullish")
        elif agg_pc < 1.5:
            print("  ⚪ Balanced")
        else:
            print("  🔴 Put-heavy (bearish)")
    print(f"  Thesis-zone Call OI:   {total_zone_calls:>10,}  ({zone_pct:.1f}% of total call OI)")
    if zone_pct > 25:
        print(f"  🟢 Meaningful positioning in ${THESIS_ZONE_LOW:.0f}-${THESIS_ZONE_HIGH:.0f} zone")

    # --- VOL PROXY headline: expiry nearest TARGET_DTE (mirrors CVOL 30d) ---
    dated = [d for d in data if d.get("dte")]
    headline = min(dated, key=lambda d: abs(d["dte"] - TARGET_DTE)) if dated else None
    if headline:
        iv = headline.get("atm_iv_pct")
        rr = headline.get("rr25")
        note = headline.get("iv_note") or ""
        print(f"\n  VOL PROXY (FXY-derived; {headline['expiry']}, ~{headline['dte']}d)")
        print(f"  {'-'*60}")
        iv_disp = f"{iv:.2f}%" if iv is not None else "n/a"
        rr_disp = f"{rr:+.2f}" if rr is not None else "n/a"
        print(f"  ATM IV (CVOL proxy):   {iv_disp:>10}  {_iv_flag(iv)}")
        if spot_is_live:
            print(f"  25d RR (USDJPY-conv):  {rr_disp:>10}  {_rr_flag(rr)}")
        else:
            # ACTION 4: print the NUMBER (it is still the computed value) but refuse
            # the thesis-side DIRECTIONAL verdict — the wings were selected against a
            # stale spot, which is exactly what decides whether the sign is meaningful.
            print(f"  25d RR (USDJPY-conv):  {rr_disp:>10}  ⚠️ DIRECTION NOT READABLE "
                  f"(spot off fallback chain)")
        if note:
            print(f"  ⚠️  {note}")
        print(f"  (proxy: FXY ETF options ≠ CME CVOL / OTC RR — compare to own history)")

        # --- Self-calibration: read RR against its OWN trailing history ----------
        # Wrapped fail-safe: this script is 1 of 9 in the boot sweep — the self-cal
        # read must NEVER break the brief if the TSV history is malformed.
        try:
            cal = calibrate_rr(date_str, rr)
            if cal["state"] == "building":
                remaining = cal["need"] - cal["n"]
                print(f"  Self-cal:              building history ({cal['n']}/{cal['need']}) — "
                      f"{remaining} more reading(s) until z-score activates")
            elif cal["state"] == "calibrated":
                print(f"  Self-cal ({cal['n']} priors, mean {cal['mean']:+.2f}, σ {cal['sd']:.2f}):  "
                      f"z={cal['z']:+.2f}  (Δ {cal['delta']:+.2f} vs norm)")
                # ⚠️ SIBLING OF THE RR VERDICT ABOVE — `cal['interp']` is a SECOND
                # thesis-side directional read ("yen-strength demand intensifying"),
                # computed off the same stale-spot-anchored wings. Suppressing only
                # the first verdict would have left this one printing unmarked.
                # (Caught by the ACTION-4 regression test, not by inspection.)
                if spot_is_live:
                    print(f"     {cal['interp']}")
                else:
                    print(f"     ⚠️ z-score shown, INTERPRETATION SUPPRESSED — spot off "
                          f"the fallback chain, so the wings this RR was read from are "
                          f"anchored to a stale reference.")
        except Exception:
            pass  # self-cal is a read-only enhancement; never let it break the sweep

    # Per-expiry
    print(f"\n  {'PER EXPIRY'}")
    print(f"  {'-'*60}")
    for d in data:
        dte_disp = f", ~{d['dte']}d" if d.get("dte") else ""
        pc_disp = ("P/C UNAVAILABLE — no call OI" if d["pc_ratio"] is None
                   else f"P/C {d['pc_ratio']:.2f}x")
        print(f"\n  {d['expiry']}{dte_disp}  ({pc_disp})")
        print(f"     Puts: {d['total_put_oi']:>7,}  Calls: {d['total_call_oi']:>7,}  Zone-call: {d['zone_call_oi']:>6,}")
        iv = d.get("atm_iv_pct"); rr = d.get("rr25")
        if iv is not None or rr is not None:
            iv_d = f"{iv:.2f}%" if iv is not None else "n/a"
            rr_d = f"{rr:+.2f}" if rr is not None else "n/a"
            print(f"     ATM IV: {iv_d}   25d RR: {rr_d}")
        if d["top5_puts"]:
            puts_str = ", ".join(f"${s:.0f}={oi}" for s, oi in d["top5_puts"][:3])
            print(f"     Top puts:  {puts_str}")
        if d["top5_calls"]:
            calls_str = ", ".join(f"${s:.0f}={oi}" for s, oi in d["top5_calls"][:3])
            print(f"     Top calls: {calls_str}")

    # Upsert to TSV (adds new rows, backfills IV/RR on existing blank rows)
    changed = append_tsv(date_str, data)
    if changed > 0:
        print(f"\n  Wrote/updated {changed} row(s) in FXY_OPTIONS.tsv")
    else:
        print(f"\n  TSV already current for {date_str} — no change")

    print()
    # Nonzero rc so boot surfaces an empty-denominator run instead of rendering it
    # beside a green ✅ (ACTION 3). The rows are still written — with PC_Ratio="NA",
    # never a sentinel — so the ledger records the gap as a gap.
    if unavailable:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
