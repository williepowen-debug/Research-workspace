#!/usr/bin/env python3
"""VIOLET OVX canary — oil-vol → equity-vol transmission gauge (KB-VIO-081 class).

Built 2026-07-17 (Will-approved canary-map build, PROME-relayed). Closes the
Tier-2 "instrumented but UNCALIBRATED" hole in CANARY_MAP.md — the OVX row that
went dark through the entire 7/1-7/8 war week.

VIOLET owns the TRANSMISSION read (oil-vol → equity-vol), NOT the oil-vol level
(BRENT/HAWK own oil substance). So the PRIMARY fire instrument is the OVX/VIX
RATIO, not the OVX level: the ratio isolates oil-vol *leading* equity-vol from a
broad co-move where both are stressed.

  PRIMARY  OVX/VIX ratio — WATCH p90 / FIRE p95 (percentile-anchored, RE-DERIVED
           each run over the FULL ^OVX history 2007-, never hardcoded).
  FLOOR    OVX level >= p75 — a fire requires oil-vol genuinely elevated, else a
           low-VIX print alone inflates the ratio (a VIX-artifact, not transmission).
  CONTEXT  OVX level pctile + OVX-VIX gap pctile.

Analog-scan calibration (the registered-but-never-run scan, threads-sweep item 8):
  Abqaiq 2019-09       OVX 48.6 (p84) ratio 3.31 (p96) VIX 14.7 — PURE oil shock,
                       calm equity vol: the ratio caught it, the level understated it.
  Ukraine 2022-02/03   OVX 78.9 (p97) ratio 2.16 (p66) VIX 36.5 — BROAD co-move:
                       the ratio correctly REFUSED it (oil not leading, both stressed).
  Israel-Iran 2024-04  OVX 35.6 (p51) ratio 1.85 (p44) — contained, correct non-fire.
  Israel-Iran 2025-06  OVX 71.6 (p96) ratio 3.31 (p96) VIX 21.6 — strong oil-led, fired.
The ratio discriminates oil-LED (Abqaiq / II-2025) from broad co-moves (Ukraine).

Route on fire: this is a CONTEXT canary, not an action-gate — → BRENT/HAWK
reference + NEXUS_BRIEF cross-domain line (VIOLET owns only the transmission read).

Appends one row per date to workbook/OVX.tsv (idempotent per day).

Usage:
  .venv/bin/python3 AGENTS/VIOLET/scripts/ovx.py           # full report
  .venv/bin/python3 AGENTS/VIOLET/scripts/ovx.py --boot    # collapsed
  .venv/bin/python3 AGENTS/VIOLET/scripts/ovx.py --json
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
VIOLET_DIR = SCRIPT_DIR.parent
DAILY_LOG = VIOLET_DIR / "workbook" / "OVX.tsv"

LEVEL_FLOOR_PCTILE = 75   # oil-vol must be >= this pctile for a transmission fire
LADDER_PS = (50, 75, 90, 95, 99)

TSV_COLS = ["date", "ovx", "vix", "gap", "ratio", "ovx_pctile", "ratio_pctile",
            "gap_pctile", "p90_ratio", "p95_ratio", "p75_level", "p90_level",
            "state", "note", "stamp_utc"]

# Analog anchors (peak-in-window from the 2026-07-17 build scan; reference only).
ANALOGS = [
    ("Abqaiq 2019-09", 48.6, 3.31, "pure oil shock, calm equity vol — ratio caught it"),
    ("Ukraine 2022-03", 78.9, 2.16, "broad co-move — ratio REFUSED (oil not leading)"),
    ("Israel-Iran 2025-06", 71.6, 3.31, "strong oil-led — fired"),
]


def pull() -> dict:
    import math
    import yfinance as yf
    import pandas as pd

    ovx = yf.Ticker("^OVX").history(period="max", auto_adjust=False)["Close"].dropna()
    vix = yf.Ticker("^VIX").history(period="max", auto_adjust=False)["Close"].dropna()
    if ovx is None or len(ovx) < 500:
        raise RuntimeError(f"^OVX history too short ({0 if ovx is None else len(ovx)} rows)")
    ovx.index = ovx.index.tz_localize(None)
    vix.index = vix.index.tz_localize(None)
    df = pd.DataFrame({"ovx": ovx, "vix": vix}).dropna()
    df["gap"] = df.ovx - df.vix
    df["ratio"] = df.ovx / df.vix

    def ladder(s):
        return {f"p{p}": round(float(s.quantile(p / 100.0)), 2) for p in LADDER_PS}

    last = df.iloc[-1]
    return {
        "asof": str(df.index[-1].date()),
        "ovx": round(float(last.ovx), 2),
        "vix": round(float(last.vix), 2),
        "gap": round(float(last.gap), 2),
        "ratio": round(float(last.ratio), 2),
        "ovx_pctile": round(float((df.ovx <= last.ovx).mean() * 100.0), 1),
        "ratio_pctile": round(float((df.ratio <= last.ratio).mean() * 100.0), 1),
        "gap_pctile": round(float((df.gap <= last.gap).mean() * 100.0), 1),
        "level_ladder": ladder(df.ovx),
        "gap_ladder": ladder(df.gap),
        "ratio_ladder": ladder(df.ratio),
        "n_obs": int(len(df)),
        "window_start": str(df.index[0].date()),
    }


def classify(d: dict) -> tuple[str, list[str]]:
    rl, ll = d["ratio_ladder"], d["level_ladder"]
    p90r, p95r = rl["p90"], rl["p95"]
    p75l, p90l = ll["p75"], ll["p90"]
    ratio, ovx = d["ratio"], d["ovx"]
    lines = []

    oil_elevated = ovx >= p75l
    if ratio >= p95r and oil_elevated:
        state = "FIRE"
        lines.append(f"🔴 FIRE: OVX/VIX ratio {ratio} >= p95 {p95r} (oil-vol {ovx} at p{d['ovx_pctile']} >= p75 {p75l}) "
                     f"— oil-vol→equity-vol transmission channel LOADED (Abqaiq / II-2025 class). "
                     f"ROUTE: BRENT/HAWK reference + NEXUS_BRIEF cross-domain (context canary, not an action-gate).")
    elif ratio >= p90r and oil_elevated:
        state = "WATCH"
        lines.append(f"🟠 WATCH: OVX/VIX ratio {ratio} >= p90 {p90r} (oil-vol {ovx} p{d['ovx_pctile']}) "
                     f"— transmission channel building. ROUTE: NEXUS_BRIEF cross-domain note.")
    else:
        state = "CALM"
        lines.append(f"🟢 CALM: OVX/VIX ratio {ratio} (p{d['ratio_pctile']}) vs WATCH {p90r} / FIRE {p95r}; "
                     f"oil-vol {ovx} (p{d['ovx_pctile']}).")

    # discriminator notes
    if ovx >= p90l and ratio < p90r:
        lines.append(f"⚠️ BROAD CO-MOVE: oil-vol elevated (p{d['ovx_pctile']}) but ratio {ratio} < WATCH {p90r} "
                     f"— equity-vol co-moving, oil NOT leading (Ukraine-2022 class; transmission read is NO-FIRE).")
    if ratio >= p90r and not oil_elevated:
        lines.append(f"⚠️ RATIO ARTIFACT: ratio {ratio} elevated but oil-vol {ovx} < p75 {p75l} "
                     f"— inflated by low equity-vol, not elevated oil-vol; NOT a transmission signal.")
    return state, lines


def append_log(d: dict, state: str, note: str) -> str:
    DAILY_LOG.parent.mkdir(parents=True, exist_ok=True)
    if not DAILY_LOG.exists():
        DAILY_LOG.write_text("\t".join(TSV_COLS) + "\n", encoding="utf-8")
    existing = DAILY_LOG.read_text(encoding="utf-8").splitlines()
    if any(line.startswith(d["asof"] + "\t") for line in existing[1:]):
        return f"already has a row for {d['asof']}"
    row = [d["asof"], d["ovx"], d["vix"], d["gap"], d["ratio"], d["ovx_pctile"],
           d["ratio_pctile"], d["gap_pctile"], d["ratio_ladder"]["p90"],
           d["ratio_ladder"]["p95"], d["level_ladder"]["p75"], d["level_ladder"]["p90"],
           state, note or "-", datetime.now(timezone.utc).isoformat(timespec="seconds")]
    with DAILY_LOG.open("a", encoding="utf-8") as f:
        f.write("\t".join(str(x) for x in row) + "\n")
    return f"✓ appended {d['asof']} row to workbook/OVX.tsv"


def main() -> int:
    ap = argparse.ArgumentParser(description="OVX oil-vol→equity-vol transmission canary")
    ap.add_argument("--boot", action="store_true", help="collapsed boot output")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--no-log", action="store_true", help="skip the TSV append")
    args = ap.parse_args()

    try:
        d = pull()
    except Exception as e:
        print(f"⚠️ OVX: pull FAILED ({e}) — no silent pass, investigate")
        return 1
    state, verdict_lines = classify(d)
    note = " | ".join(l for l in verdict_lines[1:]) if len(verdict_lines) > 1 else "-"
    log_note = "" if args.no_log else append_log(d, state, note)

    if args.json:
        print(json.dumps({"data": d, "state": state, "log": log_note}, indent=2))
        return 0

    print(f"OVX [{d['asof']}]: OVX {d['ovx']} (p{d['ovx_pctile']}) · VIX {d['vix']} · "
          f"gap {d['gap']} (p{d['gap_pctile']}) · OVX/VIX {d['ratio']} (p{d['ratio_pctile']}) · state {state}")
    for line in verdict_lines:
        print(line)
    if not args.boot:
        rl, ll, gl = d["ratio_ladder"], d["level_ladder"], d["gap_ladder"]
        print(f"Ratio ladder (re-derived, n={d['n_obs']} from {d['window_start']}): "
              f"p50 {rl['p50']} · p90 {rl['p90']} WATCH · p95 {rl['p95']} FIRE · p99 {rl['p99']}")
        print(f"Level ladder: p50 {ll['p50']} · p75 {ll['p75']} FLOOR · p90 {ll['p90']} · p95 {ll['p95']} · p99 {ll['p99']}")
        print(f"Gap ladder:   p50 {gl['p50']} · p90 {gl['p90']} · p95 {gl['p95']} · p99 {gl['p99']}")
        print("Analog anchors: " + " ; ".join(f"{n} OVX {o}/ratio {r} ({why})" for n, o, r, why in ANALOGS))
    if log_note:
        print(log_note)
    return 0


if __name__ == "__main__":
    sys.exit(main())
