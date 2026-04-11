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
from datetime import datetime
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

TSV_HEADER = "Date\tExpiry\tTotal_Put_OI\tTotal_Call_OI\tPC_Ratio\tThesis_Zone_Call_OI\tTop_Put_Strike\tTop_Put_OI\tTop_Call_Strike\tTop_Call_OI\tTop5_Puts\tTop5_Calls\n"


def get_fxy_options(num_expiries=4):
    """Fetch FXY options data for next N expiries. Returns list of dicts."""
    try:
        t = yf.Ticker("FXY")
        expiries = t.options
        if not expiries:
            return [], None

        current_price = None
        try:
            info = t.info
            current_price = info.get("regularMarketPrice") or info.get("previousClose")
        except Exception:
            pass
    except Exception as e:
        print(f"  ERROR fetching FXY options: {e}")
        return [], None

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

            pc_ratio = round(total_put_oi / total_call_oi, 2) if total_call_oi > 0 else 999.0

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
                "total_put_oi": total_put_oi,
                "total_call_oi": total_call_oi,
                "pc_ratio": pc_ratio,
                "zone_call_oi": zone_call_oi,
                "top_put": top_puts[0] if top_puts else (0, 0),
                "top_call": top_calls[0] if top_calls else (0, 0),
                "top5_puts": top_puts,
                "top5_calls": top_calls,
            })
        except Exception:
            continue

    return results, current_price


def append_tsv(date_str, data_list):
    """Append today's options data to TSV if not already present."""
    existing = set()
    if FXY_TSV.exists():
        with open(FXY_TSV) as f:
            for line in f:
                parts = line.strip().split("\t")
                if len(parts) >= 2:
                    existing.add((parts[0], parts[1]))
    else:
        with open(FXY_TSV, "w") as f:
            f.write(TSV_HEADER)

    appended = 0
    with open(FXY_TSV, "a") as f:
        for d in data_list:
            key = (date_str, d["expiry"])
            if key in existing:
                continue
            puts_str = "; ".join(f"${s:.0f}={oi}" for s, oi in d["top5_puts"])
            calls_str = "; ".join(f"${s:.0f}={oi}" for s, oi in d["top5_calls"])
            f.write(
                f"{date_str}\t{d['expiry']}\t{d['total_put_oi']}\t{d['total_call_oi']}\t"
                f"{d['pc_ratio']}\t{d['zone_call_oi']}\t{d['top_put'][0]}\t{d['top_put'][1]}\t"
                f"{d['top_call'][0]}\t{d['top_call'][1]}\t{puts_str}\t{calls_str}\n"
            )
            appended += 1
    return appended


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

    data, current_price = get_fxy_options(num_expiries=num_expiries)
    if not data:
        print("\n  ERROR: No FXY options data available.")
        return 1

    if current_price:
        print(f"\n  FXY spot: ${current_price:.2f}")
    print(f"  Thesis strike zone: ${THESIS_ZONE_LOW:.0f}–${THESIS_ZONE_HIGH:.0f} (target $60-62)")
    print(f"  Expiries scanned: {len(data)}")

    # Aggregate view
    total_puts = sum(d["total_put_oi"] for d in data)
    total_calls = sum(d["total_call_oi"] for d in data)
    total_zone_calls = sum(d["zone_call_oi"] for d in data)
    agg_pc = round(total_puts / total_calls, 2) if total_calls > 0 else 999.0
    zone_pct = (total_zone_calls / total_calls * 100) if total_calls > 0 else 0

    print(f"\n  {'AGGREGATE'}")
    print(f"  {'-'*60}")
    print(f"  Total Put OI:          {total_puts:>10,}")
    print(f"  Total Call OI:         {total_calls:>10,}")
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

    # Per-expiry
    print(f"\n  {'PER EXPIRY'}")
    print(f"  {'-'*60}")
    for d in data:
        print(f"\n  {d['expiry']}  (P/C {d['pc_ratio']:.2f}x)")
        print(f"     Puts: {d['total_put_oi']:>7,}  Calls: {d['total_call_oi']:>7,}  Zone-call: {d['zone_call_oi']:>6,}")
        if d["top5_puts"]:
            puts_str = ", ".join(f"${s:.0f}={oi}" for s, oi in d["top5_puts"][:3])
            print(f"     Top puts:  {puts_str}")
        if d["top5_calls"]:
            calls_str = ", ".join(f"${s:.0f}={oi}" for s, oi in d["top5_calls"][:3])
            print(f"     Top calls: {calls_str}")

    # Append to TSV
    appended = append_tsv(date_str, data)
    if appended > 0:
        print(f"\n  Appended {appended} row(s) to FXY_OPTIONS.tsv")
    else:
        print(f"\n  TSV already has data for {date_str} — no append")

    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
