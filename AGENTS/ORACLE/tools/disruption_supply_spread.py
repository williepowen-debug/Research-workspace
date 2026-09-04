#!/usr/bin/env python3
"""
ORACLE — Disruption-vs-Supply Spread (Iran/Hormuz axis)

    spread_pp = P(PortWatch does NOT print a 7dMA >=60 transits/day by Dec 31)
              -  P(WTI hits $100, war premium)

  !! LABEL CORRECTED 2026-09-04 (PortWatch war-regime sweep; PROME 8/17 ask). THE MATH AND THE
     SERIES ARE UNCHANGED -- ONLY THE LABEL WAS WRONG, and it was wrong in a way that mattered.
     This tool called its first leg "P(Hormuz transit disruption persists)". Read at the primary
     (Polymarket resolution text, 2026-09-04), the pinned market resolves YES only if
     "IMF Portwatch publishes a 7-day moving average of transit calls ... equal to or above 60",
     and the SAME text says "Ships not reported by IMF Portwatch will not be considered" and
     that a divergence between PortWatch and alternative sources is explicitly NOT grounds for
     correction. So the leg is a forecast of an INSTRUMENT'S PRINT, not of the strait.
     That distinction is live, not pedantic: BRENT measured a war-regime coverage defect in
     PortWatch (n_tanker>0 AND capacity_tanker=0 on 0 of 424 pre-crisis days vs 19 of 113
     war-regime tanker-days) with external corroboration (a third-party AIS vendor putting ~58%
     of a week's Hormuz transits DARK). If PortWatch undercounts, P(it prints >=60) is LOWER
     than P(the strait actually normalises), so this leg -- and therefore the SPREAD -- reads
     WIDER than the crowd's real disruption-vs-supply split. A wide spread is the reassuring
     reading ("premium, not shortage"), so THE BIAS POINTS AT THE COMFORTABLE ANSWER.
     NO REGIME BUMP: the slug, the arithmetic and the comparability are untouched, so old rows
     remain chartable against new ones. Only the disruption_label column changes text.
     ASYMMETRY WORTH KNOWING: the SUPPLY leg is a PRICE market and carries no PortWatch
     exposure at all -- so the two legs of this spread rest on different epistemic bases and
     only one of them is impeached.

WHAT IT MEASURES
The crowd is pricing two DIFFERENT things on the Iran/Hormuz axis, and the gap
between them is the signal:
  - DISRUPTION  — "ships can't move normally"  (transit harassment, re-routing,
    convoying). Reversible. Prices a RISK PREMIUM.
  - SUPPLY LOSS — "barrels stop existing"      (production/refining/export
    infrastructure destroyed or a true chokepoint closure). NOT reversible on
    the same timescale.

A WIDE spread = disruption is repriced but supply fear is absent → the move is
premium, not shortage (regime as of 2026-07-17, ~40pp). A COLLAPSING spread =
supply fear is catching up to disruption → the regime is flipping from "price
story" to "supply story". That flip is HAWK/BRENT/FALCON's tripwire. Note the
spread can also collapse benignly (disruption easing) — always read WHICH leg
moved, which is why both legs are logged, never just the spread.

  v2 REBUILD 2026-07-17 — the v1 disruption leg (P(US blockade on Iran)) RESOLVED
  YES: the US announced a blockade 7/13, in effect 7/14 16:00 ET. A resolved leg
  is pinned at 100% forever, so v1 measured a constant minus a variable and
  crashed on the drained-liquidity null. v1 rows are retained under
  regime='v1-blockade' and are NOT comparable to v2 rows (different disruption
  leg) — do not chart them as one continuous series.

  LEG CHOICE (v2) — why NOT the 0-ships closure proxy:
  A full Hormuz closure means barrels genuinely stop. That is a SUPPLY event, so
  putting it on the disruption side would invert the thing this tool exists to
  measure. It is logged as a CONTEXT column (closure_prob) instead: it is the
  bridge between the two regimes and the cleanest single escalation tell, but it
  is not the disruption leg.

INPUTS (from workbook/ODDS_LOG.tsv, written by scripts/polymarket.py pull --log)
  - disruption leg: "Hormuz traffic normal by Dec 31", INVERTED (1 - P(normal)).
    Deepest market on the axis (~$5.3M vol / ~$258K liq, 2026-07-17) and dated
    Dec-31 so it does not roll mid-regime. Inverted so the leg reads in the
    "more disruption = higher number" direction, same sign as the supply leg.
  - supply leg: WTI $100 war premium, current month.
    !! MONTH-ROLL (owed action): the WTI leg is month-stamped and auto-rolls by
    family prefix ONLY once a fresher month's market is pinned in watchlist.tsv
    and pulled. When the front month turns over, RE-PIN the new month's WTI $100
    market or this leg silently ages out. Guarded below: a supply leg staler than
    --max-leg-age-days (default 3) vs the disruption leg is a hard exit.
  - context: 0-ships Hormuz closure proxy (not part of the arithmetic).

Both legs must come from the SAME calendar day's pull unless --allow-stale;
otherwise the reading is marked STALE-PAIRED. Resolved/illiquid legs hard-exit
rather than silently logging a garbage spread (a resolved leg is the exact
failure that killed v1).

Output: appends one row to workbook/DISRUPTION_SUPPLY_SPREAD.tsv.
Cadence: run once per ORACLE session, after `polymarket.py pull --log`.
Stdlib only.

Usage:
  python3 tools/disruption_supply_spread.py             # compute + log
  python3 tools/disruption_supply_spread.py --dry-run   # compute, don't write
  python3 tools/disruption_supply_spread.py --allow-stale
"""
import argparse
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ORACLE_DIR = os.path.dirname(HERE)
ODDS_LOG = os.path.join(ORACLE_DIR, "workbook", "ODDS_LOG.tsv")
OUT_LOG = os.path.join(ORACLE_DIR, "workbook", "DISRUPTION_SUPPLY_SPREAD.tsv")

# Family prefixes — survive slug rollover across resolution windows.
DISRUPTION_PREFIX = "strait-of-hormuz-traffic-returns-to-normal-by-december"
SUPPLY_PREFIX = "will-wti-reach-100-in-"
SUPPLY_LABEL_MUST_CONTAIN = "war premium"
CLOSURE_PREFIX = "0-ships-transit-hormuz"

# A leg at/above this is settling or settled — its price is no longer a forecast.
RESOLVED_PROB = 0.99
# Below this, a single small bet moves the print; ORACLE's standing thin-liq bar.
THIN_LIQ = 5000.0

REGIME = "v4-sep-wti-supply-leg"  # bumped 2026-08-27 on August→September WTI-$100 roll. The August leg exited at 0.8% (5 days-to-touch left); September entered at 22.5% (full month). ⚠️ THAT 21.7pp STEP IS THE ROLL, NOT A REPRICING — the spread mechanically narrows ~+66.7 → ~+45 on the swap alone. NEVER chart v4 against v3. Prior bump 2026-07-31 (July→August, same structural reason: a fresh month-start contract has more days-to-touch and is structurally higher).

OUT_HEADER = ["ts", "regime",
              "disruption_slug", "disruption_label", "disruption_prob", "disruption_liq",
              "supply_slug", "supply_prob", "supply_liq",
              "closure_prob", "spread_pp", "note"]


def _f(val):
    """ODDS_LOG writes a literal 'None' for drained/absent liquidity."""
    if val is None or val in ("", "None"):
        return None
    try:
        return float(val)
    except ValueError:
        return None


def _fmt_liq(val):
    f = _f(val)
    return "n/a (drained)" if f is None else f"${f:,.0f}"


def _latest_matching(rows, slug_pred, label_pred=None):
    """Latest row by ts (ISO-8601 Z sorts lexically = chronologically)."""
    matches = [r for r in rows if slug_pred(r["slug"])
               and (label_pred is None or label_pred(r["label"]))]
    return max(matches, key=lambda r: r["ts"]) if matches else None


def _check_leg_live(row, name):
    """A resolved or liquidity-drained leg is not a forecast. Fail loud — this is
    exactly how v1 died (blockade leg resolved, spread became meaningless)."""
    prob = _f(row["yes_prob"])
    if prob is None:
        raise SystemExit(f"{name} leg has unreadable yes_prob={row['yes_prob']!r} (slug={row['slug']})")
    liq = _f(row["liquidity"])
    if prob >= RESOLVED_PROB or liq is None:
        raise SystemExit(
            f"{name} leg looks RESOLVED/settled — prob={prob:.3f}, liq={_fmt_liq(row['liquidity'])}, "
            f"slug={row['slug']}\n"
            f"  A resolved leg is pinned forever and makes the spread meaningless.\n"
            f"  Re-pin a live market in watchlist.tsv and bump the prefix in this script "
            f"(and bump REGIME so the old rows stay non-comparable)."
        )
    return prob, liq


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="compute + print only, don't write")
    ap.add_argument("--allow-stale", action="store_true",
                    help="allow disruption/supply legs from different pull days")
    ap.add_argument("--max-leg-age-days", type=int, default=3,
                    help="hard-exit if the supply leg is older than this vs the disruption leg "
                         "(catches a silently un-rolled WTI month)")
    args = ap.parse_args()

    if not os.path.exists(ODDS_LOG):
        raise SystemExit(f"no ODDS_LOG at {ODDS_LOG} — run polymarket.py pull --log first")
    with open(ODDS_LOG, newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))

    disruption = _latest_matching(rows, lambda s: s.startswith(DISRUPTION_PREFIX))
    supply = _latest_matching(
        rows,
        lambda s: s.startswith(SUPPLY_PREFIX),
        lambda label: SUPPLY_LABEL_MUST_CONTAIN in label.lower(),
    )
    closure = _latest_matching(rows, lambda s: s.startswith(CLOSURE_PREFIX))

    if disruption is None:
        raise SystemExit(f"no ODDS_LOG row for disruption prefix '{DISRUPTION_PREFIX}' — check watchlist/pin")
    if supply is None:
        raise SystemExit(f"no ODDS_LOG row for WTI $100 war-premium market — check watchlist/pin "
                         f"(month-roll? see MONTH-ROLL note in this file's docstring)")

    normal_prob, disruption_liq = _check_leg_live(disruption, "disruption (Hormuz-normal)")
    supply_prob_raw, supply_liq = _check_leg_live(supply, "supply (WTI $100)")

    # INVERT: the market asks P(traffic NORMAL); we want P(disruption persists).
    disruption_prob = (1.0 - normal_prob) * 100
    supply_prob = supply_prob_raw * 100
    spread_pp = disruption_prob - supply_prob

    # CONTEXT COLUMN GUARD (added 2026-08-27) — the closure event is a by-DATE LADDER and
    # ODDS_LOG stores only its "top = highest-prob" leg. Once an early rung settles, that
    # rung is pinned at 100% forever and becomes the top leg, so this column silently
    # reported a DEAD JULY-31 RUNG as the live closure tail from 2026-08-09 through
    # 2026-08-27 (six consecutive sessions at 100.00; last honest value 10.50 on 08-02).
    # The RESOLVED_PROB guard already existed and was correct -- it had simply never been
    # WIRED to this column, only to the two arithmetic legs (`finding_guard_correctness_
    # _and_wiring_are_independent`). A settled rung is now SUPPRESSED AND MARKED rather
    # than logged as a live probability: a marked gap stays readable, a stale 100% does not.
    # Live rungs on 2026-08-27 for reference: by-Aug-31 11.1%, by-Sep-30 26.0% (read via
    # `polymarket.py search "0 ships transit hormuz"`, not available from the top-leg log).
    closure_prob = (_f(closure["yes_prob"]) * 100) if closure else None
    closure_stale = closure_prob is not None and closure_prob >= RESOLVED_PROB * 100
    if closure_stale:
        closure_prob = None

    notes = []
    d_day, s_day = disruption["ts"][:10], supply["ts"][:10]
    if d_day != s_day:
        delta_days = abs((_date(d_day) - _date(s_day)).days)
        msg = (f"STALE-PAIRED: disruption pull {disruption['ts']} vs supply pull {supply['ts']} "
               f"({delta_days}d apart) — re-pull both before trusting this reading")
        if delta_days > args.max_leg_age_days and not args.allow_stale:
            raise SystemExit(
                f"{msg}\n  Legs are >{args.max_leg_age_days}d apart — likely an un-rolled WTI month. "
                f"Re-pin the current-month WTI $100 market, or pass --allow-stale to override.")
        if not args.allow_stale:
            notes.append(msg)
            print(f"WARNING: {msg}")
    for row, nm in ((disruption, "disruption"), (supply, "supply")):
        liq = _f(row["liquidity"])
        if liq is not None and liq < THIN_LIQ:
            n = f"THIN: {nm} leg liq ${liq:,.0f} < ${THIN_LIQ:,.0f} — do not mark on one print (≥3-day re-check)"
            notes.append(n)
            print(f"WARNING: {n}")
    note = " | ".join(notes)

    ts_now = max(disruption["ts"], supply["ts"])

    print(f"Disruption-vs-Supply spread — {ts_now}  [{REGIME}]")
    print(f"  Disruption leg: P(PortWatch 7dMA stays <60/day)     {disruption_prob:5.1f}%   "
          f"(= 100 - {normal_prob * 100:.1f}% normal-by-Dec31; liq {_fmt_liq(disruption['liquidity'])})")
    print("     ^ NOT 'disruption persists' — this leg grades on an IMF PortWatch PRINT, and "
          "PortWatch's war-regime\n       coverage is impeached (BRENT 8/17, ext. corroboration "
          "8/20). Undercount ⇒ this leg, and the\n       spread, read WIDE. Do not quote it as a "
          "throughput or disruption probability.")
    print(f"  Supply leg:     WTI $100 war premium                {supply_prob:5.1f}%   "
          f"(liq {_fmt_liq(supply['liquidity'])}, slug={supply['slug']})")
    print(f"  Spread = {disruption_prob:.1f} - {supply_prob:.1f} = {spread_pp:+.1f}pp")
    if closure_stale:
        print("  [context] Hormuz 0-ships closure tail: SUPPRESSED — top leg is a SETTLED rung "
              "(by-date ladder artifact), not a live tail. Read live rungs via "
              "`polymarket.py search \"0 ships transit hormuz\"`.")
    if closure_prob is not None:
        print(f"  [context] Hormuz 0-ships closure tail: {closure_prob:.1f}%  "
              f"(bridge between regimes — NOT in the arithmetic)")
    print(f"  Read: WIDE = premium not shortage · COLLAPSING = supply fear catching up (check WHICH leg moved)")
    if note:
        print(f"  NOTE: {note}")

    if args.dry_run:
        return

    write_header = not os.path.exists(OUT_LOG)
    with open(OUT_LOG, "a", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        if write_header:
            w.writerow(OUT_HEADER)
        w.writerow([ts_now, REGIME,
                    disruption["slug"], "P(PortWatch 7dMA <60/day) [1 - normal-by-Dec31; resolves on the IMF PortWatch PRINT, not throughput]",
                    f"{disruption_prob:.2f}", disruption["liquidity"],
                    supply["slug"], f"{supply_prob:.2f}", supply["liquidity"],
                    (f"{closure_prob:.2f}" if closure_prob is not None
                     else ("SETTLED-LEG-SUPPRESSED" if closure_stale else "")),
                    f"{spread_pp:.2f}", note])
    print(f"  logged -> {os.path.relpath(OUT_LOG, ORACLE_DIR)}")


def _date(s):
    import datetime
    return datetime.date.fromisoformat(s)


if __name__ == "__main__":
    main()
