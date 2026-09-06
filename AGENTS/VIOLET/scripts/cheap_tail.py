#!/usr/bin/env python3
"""VIOLET Cheap-Tail Window alert — surfaces the OPERATOR decision, never trades.

Built 2026-07-23 (Will-directed, after the 7/10 post-mortem). Closes the gap the
7/10→7/23 episode exposed: VIOLET's vol framework had only a CONFIRMATION gate
(GATE-VIO-116 / KB-VIO-123) that fires LATE by design, and no instrument that
flags the CHEAP-TAIL window — the complacency floor where owning convex tails is
cheapest. On 7/10 (VIX 15.03, VVIX 87.28, SKEW 144.27, CPI 4d / FOMC 19d out) the
window was open and nobody put it in front of the operator. This alert does that.

DESIGN PRINCIPLE — this is an ALERT, not a trade rule and not a gate. It does NOT
auto-execute. When the window opens it surfaces a vehicle menu and says "your
call." It is deliberately CONSERVATIVE (all four legs required to fire) to avoid
the premium-donation trap: a setup-triggered *mandate* bleeds theta through the
persistent complacency regimes (R12 ran 222 td). The catalyst leg (L4) is what
event-BOXES any tail so it isn't open-ended theta.

  L1  VVIX cheap        VVIX <= VVIX_CHEAP (default 90) — the vol-of-vol tax is
                        at its lowest; the one time VIX options aren't overpriced.
  L2  VIX complacency   VIX  <= VIX_LOW   (default 16) — spot vol at the floor.
  L3  SKEW divergence   SKEW >= SKEW_ELEV (default 140) — crash protection stays
                        expensive while spot vol is cheap = the coiled spring
                        (the canonical "elevated" line; 145 misses the deepest
                        complacency days — 7/10 SKEW was 144.27).
  L4  event-boxed       nearest HIGH/MEDIUM catalyst <= CATALYST_WINDOW_D
                        (default 21 cal days) — so the tail is bounded to a dated
                        event, not open-ended premium bleed.

  4/4 -> 🟣 OPEN     window open; surface vehicle menu + operator decision.
  3/4 -> 🟡 ARMING   one leg away; name the missing leg (early visibility).
  <=2 -> ⚪ DORMANT  not close.

WHY IT'S NOT A CONTRADICTION of "don't chase / VIX is coincident": the confirmation
gate (KB-VIO-123) answers "is the crack real?" and fires late on the INDEPENDENT
channels. This alert answers a different question — "is the tail cheap enough to
own AHEAD of a dated event?" — and fires at the complacency floor. Buying the
cheap tail on the SETUP (defined-risk, event-boxed) is a distinct, legitimate play
from buying vol on the CONFIRMATION (which is a peak-marker entry, KB-VIO-034).
The operator chooses whether to run it; the alert only makes the window legible.

Vehicle discipline on OPEN: prefer rates-vol/TLT convexity (no VIX-futures
roll-down) or VIX call SPREADS (cap the contango bleed) over outright VIX calls.
Route PROME -> TERRY (construction) -> Will [Approve]. Never auto-executed.

UPSERTS one row per date into workbook/CHEAP_TAIL.tsv: a re-run for the same
date UPDATES that row (state changes are reported loudly) rather than skipping it.
Was first-write-wins, which froze the day at its earliest read — KB-VIO-160.

Usage:
  .venv/bin/python3 AGENTS/VIOLET/scripts/cheap_tail.py            # full report
  .venv/bin/python3 AGENTS/VIOLET/scripts/cheap_tail.py --boot     # collapsed
  .venv/bin/python3 AGENTS/VIOLET/scripts/cheap_tail.py --backtest # historical fire-rate
  .venv/bin/python3 AGENTS/VIOLET/scripts/cheap_tail.py --json
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone, date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
VIOLET_DIR = SCRIPT_DIR.parent
DAILY_LOG = VIOLET_DIR / "workbook" / "CHEAP_TAIL.tsv"
CATALYSTS = VIOLET_DIR / "workbook" / "CATALYSTS.tsv"

sys.path.insert(0, str(SCRIPT_DIR))
from _daily_log import upsert_row, describe  # noqa: E402

# Default lines (tunable via CLI). Absolute levels — interpretable and the ones
# the operator reasons in; percentiles are shown alongside for context.
VVIX_CHEAP = 90.0     # L1 — vol-of-vol tax lowest
VIX_LOW = 16.0        # L2 — complacency floor
SKEW_ELEV = 140.0     # L3 — elevated-tail / divergence line (canonical)
CATALYST_WINDOW_D = 21  # L4 — dated HIGH/MEDIUM catalyst within N calendar days
CATALYST_IMPACTS = {"HIGH", "MEDIUM"}

LADDER_PS = (5, 10, 20, 50)

TSV_COLS = ["date", "vix", "vvix", "skew", "vix_pctile", "vvix_pctile",
            "skew_pctile", "cat_days", "cat_event", "legs_met", "state",
            "note", "stamp_utc"]


CBOE_COLS = {"vix": "VIX", "vvix": "VVIX", "skew": "SKEW"}


def _pull_yf(cols: list[str]):
    """PROVISIONAL fallback only. Returns {col: Series}; a column may be absent."""
    import yfinance as yf

    out = {}
    for col in cols:
        try:
            s = yf.Ticker(f"^{CBOE_COLS[col]}").history(
                period="max", auto_adjust=False)["Close"].dropna()
            if len(s):
                s.index = s.index.tz_localize(None)
                out[col] = s
        except Exception as e:  # noqa: BLE001 — a fallback must not mask the primary failure
            print(f"    ⚠ yfinance ^{CBOE_COLS[col]} fallback also failed: {type(e).__name__}")
    return out


def pull() -> dict:
    """Read VIX/VVIX/SKEW from CBOE — the PUBLISHER OF RECORD — not from a mirror.

    ⚠️ WHY THIS CHANGED (2026-09-06, WQ-188 fix ②). This function read all three
    series from yfinance, and it is the input to the ONLY 🟣 OPEN operator-decision
    surface this desk publishes. Two things made that untenable on the same day:

      · RED's `boot.py` graded RED-FT-10 off yfinance `^SKEW` — the source FT-10's
        own basis clause disqualifies IN WRITING — and printed a flat red FIRING
        at every boot 9/3→9/6. 🔑 **It was invisible precisely BECAUSE the two
        series agreed.** Agreement is not verification; it is the condition under
        which a wiring defect survives.
      · yfinance has two measured `^SKEW` defect modes against CBOE — omission and
        wrong value (RED base-rated 2/253; VIOLET's own 416-row reconcile found
        the wrong-value instance at 2025-12-24). Repairing VX_DAILY.tsv did NOT
        protect this read, because `pull()` fetches at RUN TIME and never touches
        the ledger — the at-the-moment-of-use read is its own exposure.

    CBOE is primary. yfinance survives ONLY as a fallback that MARKS the output
    PROVISIONAL and says which column it stood in for — never silently. A tool
    with no trail defaults to OVERSTATING: it displays absence of data as
    confirmation. `[[finding_adoption_is_not_validation]]`
    """
    import pandas as pd

    sys.path.insert(0, str(SCRIPT_DIR))
    from backfill import fetch_cboe_history  # noqa: E402 — same-desk publisher path

    series, provisional = {}, []
    for col, sym in CBOE_COLS.items():
        data, ok = fetch_cboe_history(sym)
        if ok and data:
            s = pd.Series(data)
            s.index = pd.to_datetime(s.index)
            series[col] = s.sort_index()
        else:
            provisional.append(col)

    if provisional:
        # LOUD. The value still gets produced — an operator surface that goes
        # dark on a CDN hiccup is worse than one that is labelled — but it is
        # labelled at every level: stdout, the returned dict, and the TSV note.
        print(f"  ⚠️ CHEAP-TAIL PROVISIONAL — CBOE unavailable for {provisional}; "
              f"falling back to yfinance for those column(s). "
              f"Do NOT grade or act on a provisional read.")
        series.update(_pull_yf(provisional))

    missing = [c for c in CBOE_COLS if c not in series]
    if missing:
        raise RuntimeError(f"no source served {missing} — CBOE and yfinance both failed")
    if len(series["vix"]) < 500:
        raise RuntimeError(f"^VIX history too short ({len(series['vix'])} rows)")

    df = pd.DataFrame(series).dropna()

    def pct(series, val):
        return round(float((series <= val).mean() * 100.0), 1)

    def ladder(s):
        return {f"p{p}": round(float(s.quantile(p / 100.0)), 2) for p in LADDER_PS}

    last = df.iloc[-1]
    return {
        "asof": str(df.index[-1].date()),
        "source": "yfinance-PROVISIONAL:" + ",".join(provisional) if provisional else "CBOE",
        "provisional": provisional,
        "vix": round(float(last["vix"]), 2),
        "vvix": round(float(last["vvix"]), 2),
        "skew": round(float(last["skew"]), 2),
        "vix_pctile": pct(df["vix"], last["vix"]),
        "vvix_pctile": pct(df["vvix"], last["vvix"]),
        "skew_pctile": pct(df["skew"], last["skew"]),
        "vix_ladder": ladder(df["vix"]),
        "vvix_ladder": ladder(df["vvix"]),
        "n_obs": int(len(df)),
        "window_start": str(df.index[0].date()),
        "_df": df,  # retained for --backtest only
    }


def nearest_catalyst(today: date | None = None) -> tuple[int | None, str]:
    """Days to the nearest future HIGH/MEDIUM catalyst in CATALYSTS.tsv."""
    if today is None:
        today = datetime.now().date()
    if not CATALYSTS.exists():
        return None, "(CATALYSTS.tsv missing)"
    best_days, best_event = None, "-"
    for line in CATALYSTS.read_text(encoding="utf-8").splitlines()[1:]:
        parts = line.split("\t")
        if len(parts) < 5:
            continue
        d_str, event, _typ, _dom, impact = parts[0], parts[1], parts[2], parts[3], parts[4]
        if impact.strip().upper() not in CATALYST_IMPACTS:
            continue
        try:
            d = datetime.strptime(d_str.strip(), "%Y-%m-%d").date()
        except ValueError:
            continue
        days = (d - today).days
        if days < 0:
            continue
        if best_days is None or days < best_days:
            best_days, best_event = days, event.strip()
    return best_days, best_event


def classify(d: dict, cat_days: int | None, cat_event: str,
             vvix_cheap: float, vix_low: float, skew_elev: float,
             cat_window: int) -> tuple[str, int, list[str], list[str]]:
    l1 = d["vvix"] <= vvix_cheap
    l2 = d["vix"] <= vix_low
    l3 = d["skew"] >= skew_elev
    l4 = cat_days is not None and cat_days <= cat_window
    legs = [
        ("VVIX cheap", l1, f"VVIX {d['vvix']} (p{d['vvix_pctile']}) {'<=' if l1 else '>'} {vvix_cheap}"),
        ("VIX complacency", l2, f"VIX {d['vix']} (p{d['vix_pctile']}) {'<=' if l2 else '>'} {vix_low}"),
        ("SKEW divergence", l3, f"SKEW {d['skew']} (p{d['skew_pctile']}) {'>=' if l3 else '<'} {skew_elev}"),
        ("event-boxed", l4, (f"nearest HIGH/MED catalyst {cat_days}d ({cat_event}) "
                             f"{'<=' if l4 else '>'} {cat_window}d" if cat_days is not None
                             else "no dated HIGH/MED catalyst found")),
    ]
    met = sum(1 for _, ok, _ in legs if ok)
    scorecard = [f"    {'✅' if ok else '⬜'} L{i+1} {name}: {desc}"
                 for i, (name, ok, desc) in enumerate(legs)]

    if met == 4:
        state = "OPEN"
    elif met == 3:
        state = "ARMING"
    else:
        state = "DORMANT"
    return state, met, scorecard, [name for name, ok, _ in legs if not ok]


VEHICLE_MENU = [
    "  🟣 CHEAP-TAIL WINDOW OPEN — the complacency floor + a dated catalyst; convex tails are cheap here.",
    "     This is an OPERATOR DECISION, not a trade and not a gate — VIOLET does not execute.",
    "     Vehicle discipline (best carry first):",
    "       1. Rates-vol / TLT convexity — no VIX-futures roll-down; check overlap with any live 004-class leg first (double-count risk).",
    "       2. VIX call SPREADS (not outright calls) — caps the contango roll-down bleed; defined risk.",
    "       3. SPX/index put structures — HENRY/TERRY domain; flag, don't build here.",
    "     Sizing: small, defined-risk, EVENT-BOXED — take it off after the catalyst if the tail doesn't fire.",
    "     Distinct from the CONFIRMATION gate (KB-VIO-123): that fires late on independent channels; THIS is a setup-entry while vol is cheap.",
    "     Route: PROME -> TERRY (construction) -> Will [Approve]. Log the decision (taken or passed) on the alert.",
]


def append_log(d: dict, cat_days, cat_event, met: int, state: str, note: str,
               supersede: bool = True) -> str:
    """UPSERT today's row (KB-VIO-160) — see scripts/_daily_log.py.

    Was first-write-wins: legs met/lost intraday (SKEW crossing 140, VVIX
    crossing 90) could never update the day's row once boot had written it.
    """
    row = [d["asof"], d["vix"], d["vvix"], d["skew"], d["vix_pctile"],
           d["vvix_pctile"], d["skew_pctile"],
           cat_days if cat_days is not None else "-", cat_event, f"{met}/4",
           state, note or "-", datetime.now(timezone.utc).isoformat(timespec="seconds")]
    status, changes = upsert_row(DAILY_LOG, TSV_COLS, row, supersede=supersede)
    return describe(status, d["asof"], changes, "CHEAP_TAIL.tsv")


def backtest(d: dict, vvix_cheap: float, vix_low: float, skew_elev: float) -> list[str]:
    """Historical frequency of the 3 MARKET legs (L1+L2+L3). The catalyst leg
    (L4) can't be reconstructed historically, so this is the UPPER BOUND on the
    fire rate — it proves the market-side setup is rare, not a bleed machine."""
    df = d["_df"]
    mask = (df["vvix"] <= vvix_cheap) & (df["vix"] <= vix_low) & (df["skew"] >= skew_elev)
    hits = df[mask]
    n, total = len(hits), len(df)
    lines = [
        f"  BACKTEST — 3 market legs (VVIX<={vvix_cheap} & VIX<={vix_low} & SKEW>={skew_elev}), n={total} from {d['window_start']}:",
        f"    fired {n} days ({round(100.0*n/total,2)}% of history) — UPPER BOUND (L4 catalyst leg not backtestable).",
    ]
    if n:
        # collapse consecutive fire-days into episodes
        idx = hits.index.to_list()
        episodes, start, prev = [], idx[0], idx[0]
        for t in idx[1:]:
            if (t - prev).days > 7:
                episodes.append((start, prev))
                start = t
            prev = t
        episodes.append((start, prev))
        lines.append(f"    {len(episodes)} distinct episodes (>7d gaps). Most recent 6:")
        for a, b in episodes[-6:]:
            sub = hits.loc[a:b]
            lines.append(f"      {a.date()}→{b.date()} ({len(sub)}d): "
                         f"VIX {sub['vix'].min():.1f}-{sub['vix'].max():.1f} · "
                         f"VVIX {sub['vvix'].min():.0f}-{sub['vvix'].max():.0f} · SKEW {sub['skew'].max():.0f}")
    return lines


def main() -> int:
    ap = argparse.ArgumentParser(description="VIOLET cheap-tail window alert (operator decision surface)")
    ap.add_argument("--boot", action="store_true", help="collapsed boot output")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--backtest", action="store_true", help="historical fire-rate of the market legs")
    ap.add_argument("--no-log", action="store_true", help="skip the TSV append")
    ap.add_argument("--no-supersede", action="store_true",
                    help="do not update an existing row for today; report the divergence instead")
    ap.add_argument("--vvix", type=float, default=VVIX_CHEAP)
    ap.add_argument("--vix", type=float, default=VIX_LOW)
    ap.add_argument("--skew", type=float, default=SKEW_ELEV)
    ap.add_argument("--window", type=int, default=CATALYST_WINDOW_D)
    args = ap.parse_args()

    try:
        d = pull()
    except Exception as e:
        print(f"⚠️ CHEAP-TAIL: pull FAILED ({e}) — no silent pass, investigate")
        return 1

    cat_days, cat_event = nearest_catalyst()
    state, met, scorecard, missing = classify(
        d, cat_days, cat_event, args.vvix, args.vix, args.skew, args.window)
    note = ("window open" if state == "OPEN"
            else f"missing: {', '.join(missing)}" if missing else "-")
    # The provenance rides ON THE ROW, not only in scrollback. A row read back
    # next week cannot tell a CBOE-sourced state from a fallback one otherwise,
    # and this is the ledger behind an operator-decision surface.
    if d.get("provisional"):
        note = f"{note} [PROVISIONAL src=yfinance:{','.join(d['provisional'])}]"
    log_note = "" if args.no_log else append_log(d, cat_days, cat_event, met, state, note, supersede=not args.no_supersede)

    if args.json:
        d.pop("_df", None)
        print(json.dumps({"data": d, "cat_days": cat_days, "cat_event": cat_event,
                          "legs_met": f"{met}/4", "state": state, "missing": missing,
                          "log": log_note}, indent=2, default=str))
        return 0

    icon = {"OPEN": "🟣", "ARMING": "🟡", "DORMANT": "⚪"}[state]
    src = "" if d.get("source") == "CBOE" else f" ⚠️ {d.get('source')}"
    print(f"CHEAP-TAIL [{d['asof']}]: {icon} {state} ({met}/4) · "
          f"VIX {d['vix']} · VVIX {d['vvix']} · SKEW {d['skew']} · "
          f"nearest HIGH/MED catalyst {cat_days}d ({cat_event}){src}")
    for line in scorecard:
        print(line)
    if state == "OPEN":
        for line in VEHICLE_MENU:
            print(line)
    elif state == "ARMING":
        print(f"  🟡 ARMING — one leg from open; missing: {', '.join(missing)}. Watch daily.")
    if args.backtest and not args.boot:
        for line in backtest(d, args.vvix, args.vix, args.skew):
            print(line)
    if not args.boot and state == "DORMANT":
        print(f"  ⚪ DORMANT — cheap-tail window closed. Lines: VVIX<={args.vvix} · VIX<={args.vix} · "
              f"SKEW>={args.skew} · catalyst<={args.window}d.")
    if log_note:
        print(f"  {log_note}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
