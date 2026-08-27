#!/usr/bin/env python3
"""
SAM MOF Weekly Foreign Securities Flow Monitor
Fetches Japan MOF's weekly "International Transactions in Securities" CSV.
Tracks Japanese residents' net acquisition/disposition of foreign long-term
debt securities — the key signal for life-insurer repatriation.

Source: https://www.mof.go.jp/policy/international_policy/reference/itn_transactions_in_securities/week.csv
Format: Shift-JIS encoded CSV (mixed Japanese + English headers)
Unit:   100 million yen (億円)
Update: Weekly, usually Thursday JST (prior week ending Saturday)

Key column (by position):
  col 0: Period (e.g., "2026.3.29~4.4")
  col 6: Long-term debt securities, Net (Portfolio Investment Assets)
         → positive = Japan buying foreign LT bonds
         → negative = Japan selling (repatriation signal)
  col 7: Subtotal Net (equity + LT debt)
  col 10: Short-term debt Net
  col 11: Total Net (all portfolio investment assets, ex-liabilities)

Alerts (based on 4-week rolling of LT debt Net, calibrated to THESIS
scenario bucket midpoints at USDJPY ~150):
  🔴 CRISIS    net selling > ¥14T / 4 weeks (THESIS crisis case $100B+/mo)
  🟠 STRESS    net selling > ¥3.5T / 4 weeks (THESIS stress case $25-40B/mo)
  🟡 ELEVATED  net selling > ¥1.4T / 4 weeks (above THESIS base case $7-10B/mo)

Appends to workbook/MOF_FLOWS.tsv.

Usage:
  .venv/bin/python3 AGENTS/SAM/scripts/mof_flows.py
  .venv/bin/python3 AGENTS/SAM/scripts/mof_flows.py --weeks 12
"""

import sys
import urllib.request
from datetime import datetime
from pathlib import Path

SAM_DIR = Path(__file__).resolve().parent.parent
WORKBOOK = SAM_DIR / "workbook"
FLOWS_TSV = WORKBOOK / "MOF_FLOWS.tsv"

MOF_CSV_URL = "https://www.mof.go.jp/policy/international_policy/reference/itn_transactions_in_securities/week.csv"
HEADERS = {"User-Agent": "Mozilla/5.0 (SAM-Research)"}

# Unit: 100M yen. 1 "oku" = ¥100,000,000. ¥1T = 10,000 units.
OKU_PER_TRILLION = 10000

# 4-week rolling thresholds — calibrated to THESIS.md Channel 1 scenario buckets:
#   Base case:   $7-10B/mo  ≈ ¥1-1.5T/mo  ≈ up to ¥1.4T per 4 weeks
#   Stress case: $25-40B/mo ≈ ¥3.75-6T/mo ≈ ¥3.5-5.5T per 4 weeks
#   Crisis case: $100-165B/mo ≈ ¥15-25T/mo ≈ ¥14T+ per 4 weeks
# (Assumes USDJPY ~150 for conversion)
ELEVATED_4W = 14000   # ¥1.4T — above THESIS base case upper bound
STRESS_4W   = 35000   # ¥3.5T — entering THESIS stress case range
CRISIS_4W   = 140000  # ¥14T — entering THESIS crisis case range

# SAM's own registered WEEKLY bar (CLAUDE.md § KEY THRESHOLDS: 'MOF weekly LT-debt net
# >¥1.5T selling => stress flow at weekly level'). Kept SEPARATE from the 4W ladder on
# purpose: the 4W ladder is a ROLLING-SUM instrument and cannot see a single-week extreme
# that a buying window absorbs. See the 2026-08-27 instrument-defect note below.
WEEKLY_SELL_BAR = 15000  # ¥1.5T

# Cols 1-7 are the OUTWARD leg (residents buying/selling FOREIGN securities) and are
# FROZEN in position -- appended columns go at the END so positional readers keep working.
# Cols 8-12 added 2026-08-27: the INWARD leg (non-residents buying/selling JAPANESE
# securities), MOF CSV section 2. The script parsed only section 1 for its whole life, so
# the corroborating half of every repatriation read was invisible -- see the 8/27 finding.
TSV_HEADER = ("Period\tEquity_Net_oku\tLT_Debt_Net_oku\tSubtotal_Net_oku\tShort_Debt_Net_oku\t"
              "Total_Net_oku\tLT_Debt_Net_T_yen\t"
              "In_Equity_Net_oku\tIn_LT_Debt_Net_oku\tIn_Subtotal_Net_oku\tIn_Short_Debt_Net_oku\tIn_Total_Net_oku\n")


def fetch_mof_csv():
    """Fetch MOF weekly CSV. Returns decoded text or None.

    MOF uses CP932 (Japanese government standard extension of Shift-JIS).
    Some byte sequences fail strict shift_jis but work in cp932.
    """
    try:
        req = urllib.request.Request(MOF_CSV_URL, headers=HEADERS)
        # 10s (not 30s): fail fast on a slow/dead MOF endpoint rather than
        # hanging ~30s and eating boot.py's 60s per-script budget. Cached TSV
        # holds last-known flows; a FAIL here is an honest "couldn't refresh".
        with urllib.request.urlopen(req, timeout=10) as resp:
            raw = resp.read()
            return raw.decode("cp932", errors="replace")
    except Exception as e:
        print(f"  ERROR fetching MOF CSV: {e}")
        return None


def parse_mof_csv(text):
    """
    Parse MOF weekly CSV. Returns list of dicts ordered by period ascending.

    Row format (after headers, using full-width Japanese separators):
      "2026．3．29～4．4", "35,041 ", "20,666 ", "14,374 ", "105,539 ",
      "130,162 ", "-24,624 ", "-10,249 ", ...
      col 0: period (Japanese full-width dot "．" and tilde "～")
      col 1-3: Assets Equity acq/disp/net
      col 4-6: Assets LT-debt acq/disp/net   ← col 6 is our key metric
      col 7:   Assets Subtotal Net
      col 8-10: Assets Short-term acq/disp/net
      col 11:  Assets Total Net
      col 12-22: Liabilities side
    """
    import csv as csvmod
    import re as remod

    rows = []
    reader = csvmod.reader(text.splitlines())
    # Pattern: starts with 4-digit year + full-width/half-width dot + digit + ...
    # Must contain the full-width tilde (～) or half-width tilde (~) separating weeks
    period_re = remod.compile(r"^\d{4}[．.]\d+[．.]\d+[～~]")

    for fields in reader:
        if not fields or not fields[0]:
            continue
        period = fields[0].strip()
        if not period_re.match(period):
            continue
        if len(fields) < 12:
            continue

        def num(s):
            try:
                return int(s.replace(",", "").strip())
            except (ValueError, AttributeError):
                return None

        row = {
            "period": period,
            "equity_net": num(fields[3]),
            "lt_debt_net": num(fields[6]),
            "subtotal_net": num(fields[7]),
            "short_debt_net": num(fields[10]),
            "total_net": num(fields[11]),
            # INWARD leg (MOF CSV section 2, 対内証券投資). Index mapping is the outward
            # mapping +11 and was VERIFIED 2026-08-27 by internal consistency on all 1,129
            # rows (subtotal == equity + LT), with the outward leg as a passing control.
            "in_equity_net": num(fields[14]),
            "in_lt_debt_net": num(fields[17]),
            "in_subtotal_net": num(fields[18]),
            "in_short_debt_net": num(fields[21]),
            "in_total_net": num(fields[22]),
        }
        if row["lt_debt_net"] is None:
            continue
        rows.append(row)

    return rows


def fmt_oku_as_yen(oku):
    """Format 100M-yen units as ¥XT or ¥XB string."""
    yen = oku * 1e8
    if abs(yen) >= 1e12:
        return f"¥{yen/1e12:+,.2f}T"
    elif abs(yen) >= 1e9:
        return f"¥{yen/1e9:+,.1f}B"
    else:
        return f"¥{yen/1e6:+,.0f}M"


def fmt_oku_as_usd(oku, usdjpy=150.0):
    """Format 100M-yen as approximate USD."""
    yen = oku * 1e8
    usd = yen / usdjpy
    if abs(usd) >= 1e9:
        return f"~${usd/1e9:+,.1f}B"
    else:
        return f"~${usd/1e6:+,.0f}M"


def append_tsv(rows):
    """Append rows to TSV idempotently (key: period)."""
    existing = set()
    if FLOWS_TSV.exists():
        with open(FLOWS_TSV) as f:
            next(f, None)
            for line in f:
                parts = line.strip().split("\t")
                if parts:
                    existing.add(parts[0])
    else:
        with open(FLOWS_TSV, "w") as f:
            f.write(TSV_HEADER)

    appended = 0
    with open(FLOWS_TSV, "a") as f:
        for r in rows:
            if r["period"] in existing:
                continue
            lt_t = (r["lt_debt_net"] * 1e8) / 1e12 if r["lt_debt_net"] is not None else 0
            f.write(
                f"{r['period']}\t"
                f"{r.get('equity_net', '')}\t"
                f"{r['lt_debt_net']}\t"
                f"{r.get('subtotal_net', '')}\t"
                f"{r.get('short_debt_net', '')}\t"
                f"{r.get('total_net', '')}\t"
                f"{lt_t:.3f}\t"
                f"{r.get('in_equity_net', '')}\t"
                f"{r.get('in_lt_debt_net', '')}\t"
                f"{r.get('in_subtotal_net', '')}\t"
                f"{r.get('in_short_debt_net', '')}\t"
                f"{r.get('in_total_net', '')}\n"
            )
            appended += 1
    return appended


def check_revisions(rows):
    """Compare stored (first-print) values against the live source.

    FOUND 2026-08-27: MOF REVISES this series after first publication, and append_tsv is
    idempotent BY PERIOD -- so a revised week is never re-read and the TSV silently keeps
    the first print forever. Measured that day: 14 of 1,129 LT rows differed, ALL in 2026,
    largest revision Y22B (1.4% of that week). Materiality was tested and EVERY conclusion
    drawn that day held identically on live values (rank 10/1129, 28 trips, 2.48% base
    rate, subtotal+total rank 3) -- real defect, immaterial outcome.

    Cols 1-7 are deliberately NOT auto-corrected: they are the FIRST-PRINT audit trail, and
    past grades must stay reproducible against what was believed at grading time. This
    function makes the drift VISIBLE instead of silent; overwriting is a judgment call.
    """
    if not FLOWS_TSV.exists():
        print("  no TSV yet — nothing to check")
        return 0
    stored = {}
    with open(FLOWS_TSV) as f:
        next(f, None)
        for line in f:
            p = line.rstrip("\n").split("\t")
            if len(p) > 2 and p[2]:
                stored[p[0]] = int(p[2])
    diffs = [(r["period"], stored[r["period"]], r["lt_debt_net"])
             for r in rows
             if r["period"] in stored and r["lt_debt_net"] is not None
             and stored[r["period"]] != r["lt_debt_net"]]
    print(f"\n  REVISION CHECK — stored first-print vs live source")
    print(f"  {'-'*60}")
    if not diffs:
        print(f"  🟢 no revisions ({len(stored)} rows compared)")
        return 0
    worst = max(abs(b - a) for _, a, b in diffs)
    print(f"  🟡 {len(diffs)} of {len(stored)} rows revised since first print "
          f"({100*len(diffs)/len(stored):.1f}%); largest {fmt_oku_as_yen(worst)}")
    for per, a, b in diffs[-8:]:
        print(f"     {per.strip():<20} stored {a:>8} -> live {b:>8}  ({fmt_oku_as_yen(b-a)})")
    print(f"  ⚠️  Cols 1-7 are the FIRST-PRINT audit trail and are NOT auto-corrected.")
    print(f"     Re-check materiality before citing a rank or base rate off stored values.")
    return len(diffs)


def main():
    weeks = 8

    if "--check-revisions" in sys.argv:
        check_revisions(parse_mof_csv(fetch_mof_csv()))
        return 0

    if "--weeks" in sys.argv:
        idx = sys.argv.index("--weeks")
        if idx + 1 < len(sys.argv):
            weeks = int(sys.argv[idx + 1])

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"\n{'='*70}")
    print(f"  SAM MOF Weekly Foreign Securities Flows — {now}")
    print(f"{'='*70}")

    text = fetch_mof_csv()
    if not text:
        print("\n  ERROR: MOF CSV fetch failed.")
        return 1

    rows = parse_mof_csv(text)
    if not rows:
        print("\n  ERROR: MOF CSV parse empty.")
        return 1

    latest = rows[-1]
    print(f"\n  Source: MOF ITS (authoritative)")
    print(f"  Latest period: {latest['period']}")
    print(f"  Total weeks available: {len(rows)}")

    # Latest week detail
    print(f"\n  LATEST WEEK — FOREIGN ASSET FLOWS (Japan residents)")
    print(f"  {'-'*60}")
    print(f"  Equity net:          {fmt_oku_as_yen(latest.get('equity_net') or 0)}")
    print(f"  LT debt net:         {fmt_oku_as_yen(latest['lt_debt_net'])}  {fmt_oku_as_usd(latest['lt_debt_net'])}")
    print(f"  Short-term debt net: {fmt_oku_as_yen(latest.get('short_debt_net') or 0)}")
    print(f"  Subtotal net:        {fmt_oku_as_yen(latest.get('subtotal_net') or 0)}")
    print(f"  Total net:           {fmt_oku_as_yen(latest.get('total_net') or 0)}")

    # INWARD leg — added 2026-08-27. The script parsed only MOF CSV section 1 (outward)
    # for its entire life, so the CORROBORATING half of every repatriation read was
    # invisible: "residents sold foreign bonds" could never be checked against "did
    # non-residents buy Japanese ones?" Both legs pointing the same way is a much
    # stronger read than either alone, and it was one column-offset away the whole time.
    if latest.get("in_lt_debt_net") is not None:
        in_lt = latest["in_lt_debt_net"]
        out_lt = latest["lt_debt_net"]
        print(f"\n  INWARD — non-residents buying/selling JAPANESE securities")
        print(f"  {'-'*60}")
        print(f"  Equity net:          {fmt_oku_as_yen(latest.get('in_equity_net') or 0)}")
        print(f"  LT debt net (JGBs):  {fmt_oku_as_yen(in_lt)}")
        print(f"  Total net:           {fmt_oku_as_yen(latest.get('in_total_net') or 0)}")
        if -out_lt > WEEKLY_SELL_BAR and in_lt > 0:
            print(f"  ⚪ BOTH DURATION LEGS POINT AT JGBs THIS WEEK — residents sold foreign LT")
            print(f"     debt through the weekly bar AND non-residents bought Japanese LT debt.")
            print(f"  ⛔ DO NOT READ THIS AS CORROBORATION. Joint base rate 19/1,129 = 1.68%")
            print(f"     LOOKS striking and is NOT: P(outward trips)=2.48% x P(inward>0)=57.22%")
            print(f"     = 1.42% IF INDEPENDENT, so the observed 1.68% is a lift of just 1.19x")
            print(f"     (conditional 67.9% vs 57.2% unconditional, one-sided binomial p=0.172).")
            print(f"     The joint rate is small almost ENTIRELY because the OUTWARD leg is rare;")
            print(f"     the conjunction adds ~nothing to its own legs. Charge raised by RED")
            print(f"     2026-08-27 and CONFIRMED against my own data the same session.")
            print(f"  ⚠️ Near-independence also refutes 'one impulse seen at both ends' — a single")
            print(f"     repatriation impulse would co-occur FAR above chance. Neither 'two")
            print(f"     witnesses' nor 'one witness twice' is supported. Report the co-occurrence")
            print(f"     as a DESCRIPTION, never as evidence, and read MAGNITUDES not signs.")

    # ---------------------------------------------------------------------
    # WEEKLY ALERT — independent of the 4W ladder by design.
    #
    # INSTRUMENT DEFECT FOUND 2026-08-27 (class: rolling-sum instrument blind to a
    # single-period extreme). Week 2026.8.16~8.22 printed LT-debt -¥1.978T -- the 10th
    # most negative week in 1,129 back to 2005, and the 3rd most negative on both the
    # equity+LT and total measures -- and this script printed "🟢 Net BUYING — no
    # repatriation signal", because the ONLY alert path was keyed on the 4-week rolling
    # (+¥1.264T, still buy-side after three buying weeks absorbed it).
    #
    # SAM's registered threshold is keyed on the WEEK; the alert was keyed on the SUM.
    # A green light structurally could not fire SAM's own registered signal.
    # This check is deliberately NOT nested inside the `len(rows) >= 4` block and NOT
    # an elif of the 4W ladder: both would re-inherit the blindness being fixed.
    # ---------------------------------------------------------------------
    week_lt = latest["lt_debt_net"]
    print(f"\n  WEEKLY ALERT (SAM registered bar: >{fmt_oku_as_yen(-WEEKLY_SELL_BAR)} selling in ONE week)")
    print(f"  {'-'*60}")
    if -week_lt > WEEKLY_SELL_BAR:
        print(f"  🟠 WEEKLY SELL BAR TRIPPED — {fmt_oku_as_yen(week_lt)} LT-debt net selling")
        print(f"     → Registered consequence: signal LIQUID (cross-agent bar) + PROME.")
        print(f"     ⚠️  Yen-POSITIVE / UST-demand-NEGATIVE direction. ONE week, foreign LT debt")
        print(f"        GLOBALLY (not USTs-specific).")
        print(f"     ⛔ Does NOT re-open Channel 1: its re-add bar is a direct foreign-SALES")
        print(f"        print across >=2 consecutive windows at >=2 institutions.")
    elif week_lt < 0:
        print(f"  ⚪ Weekly net selling {fmt_oku_as_yen(week_lt)} — inside the ¥1.5T bar")
    else:
        print(f"  🟢 Weekly net buying {fmt_oku_as_yen(week_lt)} — bar not applicable")

    # 4-week and 12-week rolling LT debt
    if len(rows) >= 4:
        last_4 = sum(r["lt_debt_net"] for r in rows[-4:])
        print(f"\n  ROLLING LT-DEBT NET (key repatriation signal)")
        print(f"  {'-'*60}")
        print(f"  4-week rolling:   {fmt_oku_as_yen(last_4)}  {fmt_oku_as_usd(last_4)}")

        if len(rows) >= 12:
            last_12 = sum(r["lt_debt_net"] for r in rows[-12:])
            print(f"  12-week rolling:  {fmt_oku_as_yen(last_12)}  {fmt_oku_as_usd(last_12)}")
            avg_week = last_12 / 12
            print(f"  12-week avg/week: {fmt_oku_as_yen(avg_week)}")

        # Alert classification (based on 4-week net selling, THESIS-calibrated)
        net_selling_4w = -last_4  # positive = selling
        print(f"\n  ALERT STATUS (vs THESIS Channel 1 scenario buckets)")
        print(f"  {'-'*60}")
        if net_selling_4w > CRISIS_4W:
            print(f"  🔴 CRISIS CASE — 4W selling > ¥14T ($100B+/mo): {fmt_oku_as_yen(-net_selling_4w)}")
            print(f"     → Escalate to LIQUID, PROME. Rebalance thesis weights.")
        elif net_selling_4w > STRESS_4W:
            print(f"  🟠 STRESS CASE — 4W selling > ¥3.5T ($25-40B/mo): {fmt_oku_as_yen(-net_selling_4w)}")
            print(f"     → Signal LIQUID. Watch next release for confirmation.")
        elif net_selling_4w > ELEVATED_4W:
            print(f"  🟡 ELEVATED — 4W selling > ¥1.4T (above base case upper): {fmt_oku_as_yen(-net_selling_4w)}")
            print(f"     → Base case upper breached. Monitor trajectory.")
        elif net_selling_4w > 0:
            print(f"  ⚪ Base case pace — {fmt_oku_as_yen(-net_selling_4w)} net selling")
        else:
            print(f"  🟢 4W rolling net BUYING — no repatriation signal ON THE 4W INSTRUMENT")
            print(f"     ⚠️  Scope: this line is silent about the LATEST WEEK — see WEEKLY ALERT above.")

    # Recent history
    print(f"\n  RECENT HISTORY (last {min(weeks, len(rows))} weeks — LT debt net)")
    print(f"  {'-'*60}")
    for r in rows[-weeks:]:
        val = r["lt_debt_net"]
        bar_len = min(40, abs(val) // 500)  # 500 oku = ¥50B per char
        bar = ("█" * bar_len) if val < 0 else ("░" * bar_len)
        side = "SELL" if val < 0 else "BUY"
        print(f"  {r['period']:<18}  {side}  {fmt_oku_as_yen(val):>10}  {bar}")

    # Append to TSV
    appended = append_tsv(rows)
    if appended > 0:
        print(f"\n  Appended {appended} row(s) to MOF_FLOWS.tsv")
    else:
        print(f"\n  TSV already current")

    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
