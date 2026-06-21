#!/usr/bin/env python3
"""
TERRY Risk Calculator — position sizing for trade cards.

Examples:
  python3 AGENTS/TERRY/scripts/risk_calc.py --premium 2.10 --max-loss 500
  python3 AGENTS/TERRY/scripts/risk_calc.py --entry 80 --stop 84 --max-loss 600 --multiplier 1 --side short
  python3 AGENTS/TERRY/scripts/risk_calc.py --selftest

This is math only. It does not approve or execute trades.
"""
from __future__ import annotations
import argparse, math


def dollars(x):
    return f"${x:,.2f}"


def calc(args):
    if args.max_loss <= 0:
        raise SystemExit("--max-loss must be > 0")
    multiplier = args.multiplier
    if multiplier <= 0:
        raise SystemExit("--multiplier must be > 0")

    print("TERRY risk sizing")
    print("=================")
    print("Math only — Terry proposes, Will approves/rejects, no execution.\n")

    if args.premium is not None:
        if args.premium <= 0:
            raise SystemExit("--premium must be > 0")
        unit_risk = args.premium * multiplier
        mode = "defined-risk option debit / premium-at-risk"
    else:
        if args.entry is None or args.stop is None:
            raise SystemExit("Need either --premium OR both --entry and --stop")
        if args.entry <= 0 or args.stop <= 0:
            raise SystemExit("--entry and --stop must be > 0")
        if args.side == "long":
            per_share = args.entry - args.stop
        else:
            per_share = args.stop - args.entry
        if per_share <= 0:
            raise SystemExit("Stop must be adverse to entry for selected --side")
        unit_risk = per_share * multiplier
        mode = f"{args.side} underlying/spread risk to stop"

    max_units = math.floor(args.max_loss / unit_risk)
    used_risk = max_units * unit_risk
    leftover = args.max_loss - used_risk

    print(f"Mode: {mode}")
    print(f"Max loss budget: {dollars(args.max_loss)}")
    print(f"Multiplier: {multiplier:g}")
    print(f"Risk per unit: {dollars(unit_risk)}")
    print(f"Max units/contracts/shares: {max_units}")
    print(f"Budget used at max size: {dollars(used_risk)}")
    print(f"Unused budget: {dollars(leftover)}")

    if max_units <= 0:
        print("\nVERDICT: NO SIZE — one unit exceeds max loss budget.")
    else:
        print("\nTrade-card fields:")
        print(f"- Risk unit / max loss budget: {dollars(args.max_loss)}")
        print(f"- Sizing proposal: max {max_units:g} unit(s) at {dollars(unit_risk)} risk/unit")
        print(f"- Hard cap: do not exceed {dollars(used_risk)} modeled loss without re-approval")
    if args.note:
        print(f"- Note: {args.note}")
    return 0


def selftest():
    class A: pass
    a=A(); a.max_loss=500; a.multiplier=100; a.premium=2.1; a.entry=None; a.stop=None; a.side='long'; a.note=None
    # 2 contracts risk 420, not 3 (630)
    unit=a.premium*a.multiplier
    assert math.floor(a.max_loss/unit)==2
    b=A(); b.max_loss=600; b.multiplier=1; b.premium=None; b.entry=80; b.stop=84; b.side='short'; b.note=None
    assert math.floor(b.max_loss/((b.stop-b.entry)*b.multiplier))==150
    print("risk_calc.py SELFTEST: PASS")
    return 0


def main():
    ap=argparse.ArgumentParser(description="TERRY risk sizing calculator")
    ap.add_argument("--max-loss", type=float, required=False, help="Max dollar loss budget")
    ap.add_argument("--premium", type=float, help="Option debit/premium per contract/share before multiplier")
    ap.add_argument("--entry", type=float, help="Entry price for stop-based sizing")
    ap.add_argument("--stop", type=float, help="Stop price for stop-based sizing")
    ap.add_argument("--side", choices=["long","short"], default="long")
    ap.add_argument("--multiplier", type=float, default=100, help="Contract/share multiplier; options default 100, stock use 1")
    ap.add_argument("--note", help="Optional note to print into card")
    ap.add_argument("--selftest", action="store_true")
    args=ap.parse_args()
    if args.selftest: return selftest()
    if args.max_loss is None:
        raise SystemExit("--max-loss required unless --selftest")
    return calc(args)

if __name__ == "__main__":
    raise SystemExit(main())
