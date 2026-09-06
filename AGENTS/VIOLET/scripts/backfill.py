#!/usr/bin/env python3
"""VIOLET Backfill — populate VX_DAILY.tsv with historical data.

Pulls:
  - yfinance daily history for ^VIX, ^VIX3M, ^VIX6M, ^VVIX, ^SKEW (default 90 days)
  - CBOE VX futures settlement CSV for each trading day (default 30 days)

Merges into workbook/VX_DAILY.tsv. Rows keyed by date; existing rows are
updated (not duplicated), preserving columns the backfill doesn't touch.

⚠️  M1:M2 CONVENTION HAZARD — UNRESOLVED (VIOLET 6/13, Orc). The m1m2 path here
    writes SAME-DAY settlement keyed to the row date and does NOT stamp
    m1m2_settle_date. thresholds.py writes m1m2 as T-1 (prior settle) WITH the
    stamp. The two conventions DISAGREE. It would inject same-day/unstamped
    values into a T-1 series, and the skip-if-present guard only protects cells
    that ALREADY hold a value — the ~79 currently-blank m1m2 cells are NOT
    protected by it.

    HARD GATE (VIOLET 6/14, per Orc verification): the m1m2 path is now BLOCKED
    in code, not just the docstring. backfill_m1m2() early-returns unless the
    caller passes --allow-m1m2; the default `backfill.py` run does spot only.
    The warning is no longer warn-and-proceed. `--spot-only` is always safe.
    See MAINTENANCE.md (#4 convention decision).

Usage:
  .venv/bin/python3 AGENTS/VIOLET/scripts/backfill.py                # spot only (m1m2 gated off)
  .venv/bin/python3 AGENTS/VIOLET/scripts/backfill.py --spot-only    # spot only, explicit
  .venv/bin/python3 AGENTS/VIOLET/scripts/backfill.py --spot-days 180
  # m1m2 path: requires --allow-m1m2 AND the convention decision — BLOCKED by default
"""
from __future__ import annotations

import argparse
import csv
import io
import sys
import time
from datetime import date, datetime, timedelta
from pathlib import Path

import requests

SCRIPT_DIR = Path(__file__).resolve().parent
VIOLET_DIR = SCRIPT_DIR.parent
WORKSPACE = VIOLET_DIR.parent.parent
DAILY_LOG = VIOLET_DIR / "workbook" / "VX_DAILY.tsv"

TICKERS = {"vix": "^VIX", "vix9d": "^VIX9D", "vix3m": "^VIX3M", "vix6m": "^VIX6M", "vvix": "^VVIX", "skew": "^SKEW"}
CBOE_URL = "https://www.cboe.com/us/futures/market_statistics/settlement/csv/"
ROLL_WINDOW = 5


def load_existing() -> tuple[list[str], dict[str, dict]]:
    """Return (header, {date: row_dict})."""
    if not DAILY_LOG.exists():
        raise FileNotFoundError(DAILY_LOG)
    with open(DAILY_LOG) as f:
        reader = csv.DictReader(f, delimiter="\t")
        rows = {r["date"]: r for r in reader if r.get("date")}
        header = reader.fieldnames or []
    return header, rows


def write_merged(header: list[str], rows: dict[str, dict]):
    sorted_dates = sorted(rows.keys())
    with open(DAILY_LOG, "w") as f:
        f.write("\t".join(header) + "\n")
        for d in sorted_dates:
            row = rows[d]
            f.write("\t".join(str(row.get(col, "") or "") for col in header) + "\n")


def determine_regime(vix: float | None) -> str:
    if vix is None:
        return "UNKNOWN"
    if vix < 15: return "COMPLACENCY"
    if vix < 20: return "LOW_VOL"
    if vix < 30: return "RISING_VOL"
    if vix < 40: return "HIGH_VOL"
    return "CRASH"


def backfill_spot(days: int, rows: dict[str, dict]) -> int:
    import yfinance as yf
    import pandas as pd

    period = f"{max(days + 10, 30)}d"
    print(f"  Fetching yfinance history ({period}) for {list(TICKERS.values())}")
    hist = {}
    for key, sym in TICKERS.items():
        tk = yf.Ticker(sym)
        df = tk.history(period=period, auto_adjust=False)
        if df.empty:
            print(f"    ⚠ {sym}: empty history")
            continue
        # Normalize each Series's index to plain date BEFORE concat — tz-aware
        # DatetimeIndex types can differ subtly between tickers, which causes
        # pd.concat(axis=1) to emit two rows per date (one per ticker) instead
        # of one merged row. .date() before concat collapses them correctly.
        s = df["Close"]
        s.index = [d.date() if hasattr(d, "date") else d for d in s.index]
        hist[key] = s

    if "vix" not in hist:
        print("  ✗ cannot backfill: no VIX history")
        return 0

    # Combine into aligned date index
    df = pd.concat(hist, axis=1).dropna(how="all")
    # Holiday guard: yfinance ^VIX sometimes carries forward on US market holidays
    # (e.g. Memorial Day) while companion tickers correctly skip. Require at least
    # ONE companion index (^VIX3M/^VVIX/^SKEW) — on a true holiday ALL of them skip.
    # (Was ^VIX3M-only, which silently dropped real trading days whenever Yahoo's
    # ^VIX3M daily history lagged — it ran 7/18-7/23/2026 behind while ^VVIX/^SKEW
    # were current, eating the 7/20-7/24 rows. Relaxed 2026-07-25.)
    companions = [c for c in ("vix3m", "vvix", "skew") if c in df.columns]
    if companions:
        df = df[df[companions].notna().any(axis=1)]

    touched = 0
    for d, series in df.iterrows():
        d_str = d.isoformat()
        row = rows.get(d_str, {"date": d_str})
        changed = False
        for key in TICKERS:
            if key in hist and not pd.isna(series.get(key)):
                val = round(float(series[key]), 4)
                if str(row.get(key, "")) != str(val):
                    row[key] = val
                    changed = True
        # Recompute derived columns when we have both
        vix = row.get("vix")
        vix3m = row.get("vix3m")
        vix9d = row.get("vix9d")
        if vix and vix3m:
            try:
                row["vix3m_vix_ratio"] = round(float(vix3m) / float(vix), 4)
                changed = True
            except (ValueError, ZeroDivisionError):
                pass
        if vix and vix9d:
            try:
                row["vix9d_vix_ratio"] = round(float(vix9d) / float(vix), 4)
                changed = True
            except (ValueError, ZeroDivisionError):
                pass
        if vix:
            try:
                row["regime"] = determine_regime(float(vix))
            except ValueError:
                pass
        if changed:
            rows[d_str] = row
            touched += 1
    return touched


def fetch_cboe_settlement(query_date: date) -> list[dict]:
    r = requests.get(
        CBOE_URL, params={"dt": query_date.isoformat()},
        headers={"User-Agent": "Mozilla/5.0", "Referer": "https://www.cboe.com/"},
        timeout=15,
    )
    if r.status_code != 200:
        return []
    reader = csv.DictReader(io.StringIO(r.text))
    out = []
    for row in reader:
        if row.get("Product") != "VX":
            continue
        sym = row["Symbol"]
        # Standard monthlies only: VX/XN (no digits between VX and /)
        prefix = sym.split("/")[0] if "/" in sym else sym
        if prefix != "VX":
            continue
        try:
            out.append({
                "symbol": sym,
                "expiration": datetime.strptime(row["Expiration Date"], "%Y-%m-%d").date(),
                "price": float(row["Price"]),
            })
        except (ValueError, KeyError):
            pass
    out.sort(key=lambda r: r["expiration"])
    return out


def compute_m1m2(contracts: list[dict], as_of: date) -> tuple[float | None, float | None, str, str]:
    live = [c for c in contracts if c["expiration"] > as_of]
    if len(live) < 2:
        return None, None, "", ""
    m1, m2 = live[0], live[1]
    strict = (m2["price"] - m1["price"]) / m1["price"] * 100
    dte = (m1["expiration"] - as_of).days
    if dte < ROLL_WINDOW and len(live) >= 3:
        m3 = live[2]
        adj = (m3["price"] - m2["price"]) / m2["price"] * 100
        return round(strict, 3), round(adj, 3), m2["symbol"], m3["symbol"]
    return round(strict, 3), round(strict, 3), m1["symbol"], m2["symbol"]
    # 3dp, matching FORGE vix_futures.compute_steepness (which thresholds.py writes
    # through). Was 4dp — the two agreed on the number but disagreed on precision,
    # so a naive equality check between a backfilled cell and a thresholds-written
    # one reported a MISMATCH that did not exist (7.4965 vs 7.497). Uniform
    # precision removes a false-difference trap from the column. 0.001% is far
    # finer than the KB-VIO-025 bands (5.6 / 8.99).


def backfill_m1m2(days: int, rows: dict[str, dict], pause_s: float = 0.5, allow: bool = False) -> int:
    # GATE LIFTED 2026-07-27 — open decision #4 is CLOSED. History, so nobody has
    # to re-derive this: the 6/14 hard gate existed because this path wrote
    # SAME-DAY *and UNSTAMPED* m1m2 while thresholds.py wrote T-1, so the two tools
    # silently disagreed about one column and a reader had to guess which
    # convention a cell followed.
    #
    # Both halves are now gone. (a) This path stamps `m1m2_settle_date` (above), so
    # every cell it writes SAYS which settlement it is. (b) thresholds.py no longer
    # has a fixed T-1 convention to disagree with — post-settle runs now resolve
    # SAME-DAY (KB-VIO-130 fix), so the series is legitimately mixed and always has
    # been going to be.
    #
    # The resolution is therefore option (a) from decision #4, in its strongest
    # form: THE SERIES IS SELF-DESCRIBING. The convention is not "T-1" or
    # "same-day" — it is "read `m1m2_settle_date`", which is KB-VIO-092-proof
    # because no reader ever has to assume. `--allow-m1m2` is still ACCEPTED so
    # existing invocations keep working, but it is now a no-op.
    if allow:
        print("  ℹ️  --allow-m1m2 is a no-op since 2026-07-27 (decision #4 closed); "
              "the gate it overrode is gone.")
    print("  ℹ️  m1m2 backfill writes SAME-DAY values, each STAMPED with its own")
    print("      m1m2_settle_date. Legacy pre-2026-06-10 cells remain unstamped.")
    today = date.today()
    touched = 0
    requested = 0
    skipped_existing = 0
    for i in range(days + 1):
        d = today - timedelta(days=i)
        # Skip weekends
        if d.weekday() >= 5:
            continue
        d_str = d.isoformat()
        row = rows.get(d_str, {"date": d_str})
        if row.get("m1m2_adj_pct") not in (None, "", 0, "0"):
            skipped_existing += 1
            continue
        requested += 1
        try:
            contracts = fetch_cboe_settlement(d)
        except Exception as e:
            print(f"    ✗ {d_str}: {e}")
            continue
        if not contracts:
            continue
        strict, adj, m1s, m2s = compute_m1m2(contracts, d)
        if adj is None:
            continue
        row["m1m2_strict_pct"] = strict
        row["m1m2_adj_pct"] = adj
        row["m1_symbol"] = m1s
        row["m2_symbol"] = m2s
        # STAMP THE SETTLEMENT'S OWN DATE (added 2026-07-27 — this is what closed
        # open decision #4). The value above is fetched FOR date `d` and computed
        # with as_of=`d`, so it is genuinely SAME-DAY; the defect was never the
        # number, it was that the row did not SAY so. An unstamped cell forces the
        # reader to assume a convention, which is the KB-VIO-092 failure class.
        row["m1m2_settle_date"] = d_str
        rows[d_str] = row
        touched += 1
        time.sleep(pause_s)
    print(f"  CBOE: requested {requested} dates, touched {touched}, skipped {skipped_existing} (already present)")
    return touched


CBOE_HISTORY_URL = "https://cdn.cboe.com/api/global/us_indices/daily_prices/{sym}_History.csv"

# CBOE daily-prices CSVs — one per index, the PUBLISHER OF RECORD for all six
# spot columns. Free, complete, no key. Column layouts differ: the OHLC indices
# carry DATE,OPEN,HIGH,LOW,CLOSE; VVIX and SKEW carry DATE,<NAME>.
CBOE_SERIES = {
    "vix": "VIX", "vix9d": "VIX9D", "vix3m": "VIX3M",
    "vix6m": "VIX6M", "vvix": "VVIX", "skew": "SKEW",
}
CBOE_TOL = 0.005  # cents-level; anything larger is a real disagreement


def fetch_cboe_history(sym: str) -> dict[str, float]:
    """One CBOE daily-prices CSV -> {iso_date: close}. Empty dict on any failure."""
    r = requests.get(CBOE_HISTORY_URL.format(sym=sym), timeout=30,
                     headers={"User-Agent": "Mozilla/5.0"})
    if r.status_code != 200:
        print(f"    ⚠ CBOE {sym}: HTTP {r.status_code} — NOT used this run")
        return {}
    out: dict[str, float] = {}
    for row in csv.DictReader(io.StringIO(r.text)):
        d = row.get("DATE") or row.get("Date")
        if not d:
            continue
        # OHLC indices expose CLOSE; VVIX/SKEW expose a column named for the index.
        raw = row.get("CLOSE") or row.get(sym)
        try:
            if "/" in d:
                dd = datetime.strptime(d, "%m/%d/%Y").date().isoformat()
            else:
                dd = datetime.strptime(d, "%Y-%m-%d").date().isoformat()
            out[dd] = round(float(raw), 4)
        except (ValueError, KeyError, TypeError):
            continue
    return out


def backfill_spot_cboe(rows: dict[str, dict], today: str | None = None) -> dict[str, int]:
    """AUTHORITATIVE spot pass — CBOE daily-prices CSVs for all six columns.

    CBOE is the publisher of record for every index in this ledger, so this pass
    both FILLS blanks and CORRECTS disagreements, and prints every correction it
    makes. That is the difference from the VIX9D-only path this replaces, which
    filled blanks ONLY — and that skip-if-present guard is precisely why nine bad
    cells survived every prior backfill: a cell that already held a (wrong) value
    was protected from the source that could fix it. Same shape as the m1m2 hazard
    already flagged in this module's docstring.

    Two defect mechanisms it repairs, both measured 2026-09-06 against the full
    416-row ledger:

      ① TICK CONTAMINATION (7 of 9 bad cells). An intraday tick written as the
         daily row and never superseded by the settle. All seven sat on three of
         the ledger's five TICK-basis rows (2026-07-31, 08-10, 08-27).
      ② COLUMN TRANSPOSITION (1 cell, 2026-02-06). VIX3M's close (20.37) was
         written into BOTH vix and vix3m, yielding vix3m_vix_ratio == 1.0000 —
         a manufactured FLAT CURVE on a session whose true ratio was 1.147.
         Inversion is VIOLET's 🔴 peak-marker broadcast to LIQUID/HENRY, so a
         fill artifact had manufactured a cross-agent trigger reading. The other
         28 rows at ratio <= 1.05 (incl. the whole March-2026 inversion cluster)
         reconcile to CBOE EXACTLY — the class is real, this instance was not.
      (The 9th: skew 2025-12-24, ledger 160.53 vs CBOE 161.30 — the yfinance
       wrong-value mode RED base-rated at 2/253. See "clears vs bounds" below.)

    🔑 WHY THIS CLEARS THE `^SKEW` BACK-SWEEP RED SCOPED AS "BOUND, NEVER CLEAR":
    that scoping was correct for the method it described — a completeness/bar-count
    check over yfinance, which cannot see a WRONG value and cannot see an omission
    that has since healed. Reconciling against the PUBLISHER OF RECORD is a
    different operation: it compares every cell to the authority rather than
    checking the mirror against itself, so both of RED's defect modes fall out of
    the same pass. The limit that remains is narrower and worth stating — this
    clears the ledger AS OF THIS RUN against CBOE; it says nothing about a future
    CBOE revision, and nothing about columns CBOE does not publish (m1m2*).

    `basis` is stamped SETTLE for any completed past session CBOE confirms — the
    daily-prices CSV *is* the settle, so a row sourced from it is a settle by
    construction. This is what closes the standing "EOD settle never logged"
    boot warning on TICK rows that were never superseded.
    """
    if today is None:
        today = date.today().isoformat()
    print("  Fetching CBOE daily-prices CSVs (publisher of record) for "
          f"{list(CBOE_SERIES.values())}")
    hist = {col: fetch_cboe_history(sym) for col, sym in CBOE_SERIES.items()}
    if not hist.get("vix"):
        print("  ✗ CBOE VIX history unavailable — CBOE pass SKIPPED (yfinance stands)")
        return {"filled": 0, "corrected": 0, "agreed": 0, "settle_stamped": 0}

    filled = corrected = agreed = settle_stamped = 0
    corrections: list[str] = []
    for d_str, row in rows.items():
        for col in CBOE_SERIES:
            ref = hist[col].get(d_str)
            if ref is None:
                continue
            raw = str(row.get(col, "") or "").strip()
            if not raw:
                row[col] = ref
                filled += 1
                continue
            try:
                cur = float(raw)
            except ValueError:
                row[col] = ref
                corrected += 1
                corrections.append(f"     {d_str}  {col:6s} unparseable {raw!r} -> {ref}")
                continue
            if abs(cur - ref) <= CBOE_TOL:
                agreed += 1
            else:
                row[col] = ref
                corrected += 1
                corrections.append(
                    f"     {d_str}  {col:6s} {cur:>9.2f} -> {ref:>9.2f}  ({cur - ref:+.2f})")

        # Derived columns follow their inputs, never the other way round.
        vix = str(row.get("vix", "") or "").strip()
        for num, out in (("vix3m", "vix3m_vix_ratio"), ("vix9d", "vix9d_vix_ratio")):
            n = str(row.get(num, "") or "").strip()
            if vix and n:
                try:
                    row[out] = round(float(n) / float(vix), 4)
                except (ValueError, ZeroDivisionError):
                    pass
        if vix:
            try:
                row["regime"] = determine_regime(float(vix))
            except ValueError:
                pass

        # A completed session CBOE has published is a SETTLE by construction.
        if d_str < today and hist["vix"].get(d_str) is not None:
            if str(row.get("basis", "") or "").strip() != "SETTLE":
                row["basis"] = "SETTLE"
                settle_stamped += 1

    print(f"  CBOE: {agreed} cell(s) agreed, {filled} blank(s) filled, "
          f"{corrected} CORRECTED, {settle_stamped} row(s) stamped SETTLE")
    if corrections:
        print(f"  🔴 {len(corrections)} VALUE CORRECTION(S) — ledger was wrong, CBOE wins:")
        for line in corrections:
            print(line)
    return {"filled": filled, "corrected": len(corrections),
            "agreed": agreed, "settle_stamped": settle_stamped}


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--spot-days", type=int, default=90)
    p.add_argument("--m1m2-days", type=int, default=30)
    p.add_argument("--spot-only", action="store_true")
    p.add_argument("--m1m2-only", action="store_true")
    p.add_argument("--allow-m1m2", action="store_true",
                   help="Override the m1m2 hard gate (convention unresolved — see docstring/MAINTENANCE #4)")
    args = p.parse_args(argv)

    header, rows = load_existing()
    print(f"Loaded {len(rows)} existing rows from {DAILY_LOG.name}")

    if not args.m1m2_only:
        print(f"\n[1/2] Backfilling spot history ({args.spot_days} days)...")
        touched = backfill_spot(args.spot_days, rows)
        print(f"  touched {touched} rows")
        # CBOE runs SECOND and WINS. yfinance is the fast recent-history path;
        # CBOE is the publisher of record and is authoritative on every cell it
        # publishes. Same precedence pattern this desk already ratified for MOVE
        # (investing.com PRIMARY, yfinance cross-check only, KB-VIO-177).
        print("\n[1b] Reconciling spot columns against CBOE (publisher of record)...")
        backfill_spot_cboe(rows)

    if not args.spot_only:
        print(f"\n[2/2] Backfilling M1:M2 steepness ({args.m1m2_days} trading days)...")
        touched = backfill_m1m2(args.m1m2_days, rows, allow=args.allow_m1m2)
        print(f"  touched {touched} rows")

    write_merged(header, rows)
    print(f"\n✓ wrote {len(rows)} rows to {DAILY_LOG}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
