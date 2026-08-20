#!/usr/bin/env python3
"""
REGINALD KRE Float Monitor
Tracks KRE shares outstanding via yfinance (totalAssets / NAV).
Compares against last known value to detect AP redemption activity.

Usage:
  .venv/bin/python3 AGENTS/REGINALD/scripts/kre_float.py
"""

import json
import sys
from datetime import datetime
from pathlib import Path

try:
    import yfinance as yf
except ImportError:
    print("  ERROR: yfinance not installed. Run: pip install yfinance")
    sys.exit(1)

REGINALD_DIR = Path(__file__).resolve().parent.parent
STATE_FILE = REGINALD_DIR / "scripts" / ".kre_float_state.json"


def get_kre_shares():
    """Compute KRE shares outstanding from totalAssets / NAV."""
    try:
        kre = yf.Ticker("KRE")
        info = kre.info
        total_assets = info.get("totalAssets")
        nav = info.get("navPrice")
        price = info.get("regularMarketPrice") or info.get("previousClose")

        if total_assets and nav and nav > 0:
            shares = total_assets / nav
            return {
                "shares": round(shares),
                "total_assets": total_assets,
                "nav": nav,
                "price": price,
            }
    except Exception as e:
        print(f"  ERROR: {e}")
    return None


def load_state():
    """Load last known state from file."""
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE) as f:
                return json.load(f)
        except Exception as e:
            # A CORRUPT state file used to render byte-identical to a genuine first run —
            # silently skipping the shrinkage verdict this script exists to produce.
            print(f"\n  ⚠️  STATE FILE UNREADABLE ({type(e).__name__}: {e})")
            print(f"     {STATE_FILE}")
            print("     This is NOT a first run. The shrinkage comparison is being SKIPPED,")
            print("     and the baseline below will overwrite the prior reading.")
            return "UNREADABLE"
    return None


def save_state(data):
    """Save current state to file."""
    try:
        with open(STATE_FILE, "w") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"  WARNING: Could not save state: {e}")


def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"\n{'='*70}")
    print(f"  REGINALD KRE Float Monitor — {now}")
    print(f"{'='*70}")

    current = get_kre_shares()
    if not current:
        print("\n  ERROR: Could not fetch KRE data.")
        # ⚠️ MUST exit nonzero: the boot wrapper keys "✅ KRE Float OK" on the RETURN CODE,
        # so a bare `return` printed a loud error in the body and a GREEN tick in the summary.
        # (DAEDALUS silent-fallback-green sweep 2026-08-17; fixed 2026-08-20.)
        sys.exit(1)

    shares_m = current["shares"] / 1e6
    aum_b = current["total_assets"] / 1e9

    print(f"\n  KRE Shares Outstanding: {shares_m:.2f}M")
    print(f"  Total Assets (AUM):     ${aum_b:.2f}B")
    print(f"  NAV:                    ${current['nav']:.2f}")
    if current["price"]:
        premium = (current["price"] / current["nav"] - 1) * 100
        print(f"  Price:                  ${current['price']:.2f}  ({premium:+.2f}% to NAV)")

    # Compare against last known
    prev = load_state()
    if prev and prev.get("shares"):
        prev_shares_m = prev["shares"] / 1e6
        chg = (current["shares"] - prev["shares"]) / prev["shares"] * 100
        delta = current["shares"] - prev["shares"]
        prev_date = prev.get("date", "unknown")

        print(f"\n  vs. last reading ({prev_date}):")
        print(f"  Previous:  {prev_shares_m:.2f}M")
        print(f"  Change:    {delta/1e6:+.2f}M  ({chg:+.1f}%)")

        if chg < -3:
            print(f"\n  🔴 SIGNIFICANT SHRINKAGE — AP redemption accelerating")
            print(f"     {abs(delta/1e6):.2f}M shares redeemed since {prev_date}")
        elif chg < -1:
            print(f"\n  🟠 Moderate outflows — AP redemption continuing")
        elif chg > 3:
            print(f"\n  🟢 SIGNIFICANT GROWTH — creations outpacing redemptions")
        else:
            print(f"\n  ⚪ Roughly flat")
    else:
        if prev == "UNREADABLE":
            print(f"\n  ⚠️  Re-baselining after an UNREADABLE state file — NOT a first reading.")
        else:
            print(f"\n  First reading — saving as baseline.")

    # Reference: known historical levels
    print(f"\n  Reference levels:")
    print(f"    Mar 2026 peak: ~56.9M shares")
    print(f"    Current:       {shares_m:.2f}M  ({(shares_m/56.9 - 1)*100:+.1f}% from Mar peak)")

    # Save state
    save_state({
        "date": datetime.now().strftime("%Y-%m-%d"),
        "shares": current["shares"],
        "total_assets": current["total_assets"],
        "nav": current["nav"],
        "price": current["price"],
    })

    print()


if __name__ == "__main__":
    main()
