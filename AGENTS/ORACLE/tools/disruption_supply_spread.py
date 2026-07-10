#!/usr/bin/env python3
"""
ORACLE — Disruption-vs-Supply Spread (Iran/Hormuz axis)

Formula (per OPEN_THREADS_2026-07-09.md #3 "Threads to Pull" — ORACLE's own
proposed standing build):

    spread_pp = P(US blockade on Iran, top/farthest leg)  -  P(WTI hits $100, current month, war premium)

Rationale: ~8 tracked markets on the Iran/Hormuz axis (Hormuz-normal,
ships-transit ladder, 0-ships closure, US blockade) are all repricing the
7/7-7/8 truce collapse as a SHIPPING/TRANSIT disruption. Meanwhile the oil
supply-shock proxy (WTI $100, "war premium") has stayed near-dead. The gap
between "crowd prices disruption" and "crowd prices supply loss" is exactly
the fleet's own two-root framing (transit/diesel-export disruption vs
barrels-lost) collapsed into one number. A widening spread = disruption
repricing without supply fear (current regime, 2026-07-09: ~45pp). A
COLLAPSING spread = either the blockade cools OR oil supply catches up —
either is HAWK/BRENT's regime-flip tripwire (see OPEN_THREADS #3).

Inputs (both pulled from workbook/ODDS_LOG.tsv, the Polymarket machine time
series written by scripts/polymarket.py pull --log):
  - blockade leg: most recent row whose slug starts with
    "us-announces-blockade-on-iran" (family-prefix match survives slug
    rollover across resolution windows)
  - WTI $100 leg: most recent row whose slug starts with "will-wti-reach-100-in-"
    AND label contains "war premium" (this auto-rolls month to month — Jun
    market ages out once a fresher Jul/Aug pull exists)

Both legs are required to come from the SAME calendar day's pull (same date
prefix on ts) unless --allow-stale is passed, otherwise the script warns
and marks the reading STALE-PAIRED rather than silently mixing two different
pull sessions.

Output: prints the spread and appends one row to
workbook/DISRUPTION_SUPPLY_SPREAD.tsv (ts, blockade_prob, blockade_liq,
wti100_slug, wti100_prob, wti100_liq, spread_pp, note).

Update cadence: run once per ORACLE session after `polymarket.py pull --log`
(same cadence as the rest of the closeout write-back). Stdlib only.

Usage:
  python3 tools/disruption_supply_spread.py            # compute + log
  python3 tools/disruption_supply_spread.py --dry-run   # compute, don't write
  python3 tools/disruption_supply_spread.py --allow-stale
"""
import argparse
import csv
import datetime
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ORACLE_DIR = os.path.dirname(HERE)
ODDS_LOG = os.path.join(ORACLE_DIR, "workbook", "ODDS_LOG.tsv")
OUT_LOG = os.path.join(ORACLE_DIR, "workbook", "DISRUPTION_SUPPLY_SPREAD.tsv")

BLOCKADE_PREFIX = "us-announces-blockade-on-iran"
WTI100_PREFIX = "will-wti-reach-100-in-"
WTI100_LABEL_MUST_CONTAIN = "war premium"

OUT_HEADER = ["ts", "blockade_slug", "blockade_prob", "blockade_liq",
              "wti100_slug", "wti100_prob", "wti100_liq", "spread_pp", "note"]


def _latest_matching(rows, slug_pred, label_pred=None):
    """Latest row (by ts string, which sorts lexically = chronologically for
    the ISO 8601 Z-suffixed timestamps this fetcher writes) matching slug_pred
    (and label_pred if given)."""
    matches = [r for r in rows if slug_pred(r["slug"])
               and (label_pred is None or label_pred(r["label"]))]
    if not matches:
        return None
    return max(matches, key=lambda r: r["ts"])


def load_odds_log():
    if not os.path.exists(ODDS_LOG):
        raise SystemExit(f"no ODDS_LOG at {ODDS_LOG} — run polymarket.py pull --log first")
    with open(ODDS_LOG, newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="compute + print only, don't write")
    ap.add_argument("--allow-stale", action="store_true",
                     help="allow blockade/WTI legs from different pull days")
    args = ap.parse_args()

    rows = load_odds_log()

    blockade = _latest_matching(rows, lambda s: s.startswith(BLOCKADE_PREFIX))
    wti100 = _latest_matching(
        rows,
        lambda s: s.startswith(WTI100_PREFIX),
        lambda label: WTI100_LABEL_MUST_CONTAIN in label.lower(),
    )

    if blockade is None:
        raise SystemExit(f"no ODDS_LOG row found for blockade slug prefix '{BLOCKADE_PREFIX}' — check watchlist/pin")
    if wti100 is None:
        raise SystemExit(f"no ODDS_LOG row found for WTI $100 war-premium market — check watchlist/pin")

    blockade_day = blockade["ts"][:10]
    wti100_day = wti100["ts"][:10]
    note = ""
    if blockade_day != wti100_day and not args.allow_stale:
        note = f"STALE-PAIRED: blockade pull {blockade['ts']} vs WTI100 pull {wti100['ts']} — different days, re-pull both before trusting this reading"
        print(f"WARNING: {note}")

    blockade_prob = float(blockade["yes_prob"]) * 100
    wti100_prob = float(wti100["yes_prob"]) * 100
    spread_pp = blockade_prob - wti100_prob

    ts_now = max(blockade["ts"], wti100["ts"])

    print(f"Disruption-vs-Supply spread — {ts_now}")
    print(f"  Disruption leg: US blockade on Iran (top leg)  {blockade_prob:.1f}%  "
          f"(liq ${float(blockade['liquidity']):,.0f}, slug={blockade['slug']}, pulled {blockade['ts']})")
    print(f"  Supply leg:     WTI hits $100 war-premium      {wti100_prob:.1f}%  "
          f"(liq ${float(wti100['liquidity']):,.0f}, slug={wti100['slug']}, pulled {wti100['ts']})")
    print(f"  Spread = {blockade_prob:.1f} - {wti100_prob:.1f} = {spread_pp:+.1f}pp")
    if note:
        print(f"  NOTE: {note}")

    if args.dry_run:
        return

    write_header = not os.path.exists(OUT_LOG)
    with open(OUT_LOG, "a", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        if write_header:
            w.writerow(OUT_HEADER)
        w.writerow([ts_now, blockade["slug"], f"{blockade_prob:.2f}", blockade["liquidity"],
                    wti100["slug"], f"{wti100_prob:.2f}", wti100["liquidity"],
                    f"{spread_pp:.2f}", note])
    print(f"  logged -> {os.path.relpath(OUT_LOG, ORACLE_DIR)}")


if __name__ == "__main__":
    main()
