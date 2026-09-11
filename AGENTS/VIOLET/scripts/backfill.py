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


def backfill_spot(days: int, rows: dict[str, dict],
                  cboe_hist: dict[str, dict[str, float]] | None = None,
                  cboe_failed: set[str] | None = None) -> int:
    """PROVISIONAL spot pass — yfinance. NOT a writer of record for the six columns.

    ⚠️ WRITE AUTHORITY IS SCOPED (2026-09-06, WQ-188 fix ①; Codex HIGH). Before
    this change this pass ran FIRST and unconditionally, and the CBOE pass that
    followed could be skipped on a fetch failure while `main` still saved and
    exited 0. Codex's in-memory case: `skew` 151.58 SETTLE in the ledger,
    yfinance serving 149.00, CBOE 503 ⇒ 149.00 written, the `SETTLE` stamp
    RETAINED, rc=0. **The repair could silently undo itself on the next run**,
    on the ledger every `^SKEW` sustain count is derived from.

    🔑 The fix removes a WRITER rather than adding a CHECKER. A checker would
    have to run after the damage and be believed; scoping authority means the
    bad write cannot happen. Per-column rule, evaluated against THIS run:

      · CBOE series FAILED      -> yfinance may not touch that column at all.
                                   The existing (CBOE-verified) cell is preserved.
      · CBOE OK, has a value    -> yfinance defers; the CBOE pass writes it.
      · CBOE OK, has NO value   -> yfinance may write it PROVISIONALLY, but ONLY
                                   into a BLANK cell on a row that is not already
                                   stamped SETTLE. This is the legitimate residue:
                                   today's not-yet-settled session, and any date
                                   CBOE does not cover.
                                   Never stamped SETTLE (see backfill_spot_cboe).

    ⚠️ THE LAST TWO CLAUSES ARE THE 2ND-PASS FIX (Codex, WQ-188 follow-up,
    PROME-verified at L158-165). The v1 gate withheld yfinance ONLY when the
    column had FAILED or when CBOE HELD A VALUE for that date. A valid CBOE CSV
    that simply LACKS the target date satisfied neither, so the write fell
    through — and because `basis` is a ROW-level stamp that this pass never
    clears, the fallback landed in a row still labelled SETTLE. Codex's case:
    ledger `skew` 151.58 SETTLE, CBOE 200-with-valid-CSV-but-no-9/4-row,
    yfinance 149.00 ⇒ 149.00 written, SETTLE retained, rc=0.
    🔑 v1 scoped authority by WHAT CBOE SAID and left the DESTINATION unguarded;
    a write gate has to be a claim about the cell it lands in, not only about the
    source it came from. So: **yfinance may fill a blank, and may never overwrite,
    and may never touch a SETTLE row at all.** Nothing this pass writes can end up
    under an authoritative label — which is stronger than demoting the label
    afterwards, and needs no new token
    [[finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction]].

    ⚠️ A `provisional_rows` out-parameter lived here in the 2nd pass so the CBOE
    pass could refuse to stamp those rows. IT IS REMOVED: per-run memory failed on
    the SECOND run (the provisional cell is on disk, nothing new is written, the
    set is empty). `backfill_spot_cboe` now reads the invariant off the row itself
    and needs no bookkeeping from here. Kept as one guard, not two — a strictly
    weaker second guard only manufactures the impression of depth.

    Passing neither `cboe_hist` nor `cboe_failed` restores the old unscoped
    behaviour and is left only for direct callers/tests; `main` always scopes.
    """
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

    failed = set(cboe_failed or ())
    scoped = cboe_hist is not None
    touched = 0
    provisional = 0
    withheld_failed = 0
    deferred_cboe = 0
    withheld_settle = 0
    withheld_occupied = 0
    for d, series in df.iterrows():
        d_str = d.isoformat()
        row = rows.get(d_str, {"date": d_str})
        changed = False
        # --- destination gate (WQ-188 2nd pass): a SETTLE row is CBOE-verified
        # and closed to this pass entirely. Nothing yfinance writes may ever sit
        # under an authoritative label, by construction rather than by cleanup.
        row_is_settle = str(row.get("basis", "") or "").strip().upper() == "SETTLE"
        for key in TICKERS:
            if key in hist and not pd.isna(series.get(key)):
                # --- write-authority gate (WQ-188 fix ①) ---
                if key in failed:
                    withheld_failed += 1
                    continue
                if cboe_hist is not None and cboe_hist.get(key, {}).get(d_str) is not None:
                    deferred_cboe += 1
                    continue
                # --- destination gate (WQ-188 fix ②, Codex 2nd pass) ---
                if scoped and row_is_settle:
                    withheld_settle += 1
                    continue
                if scoped and str(row.get(key, "") or "").strip():
                    withheld_occupied += 1
                    continue
                val = round(float(series[key]), 4)
                if str(row.get(key, "")) != str(val):
                    row[key] = val
                    changed = True
                    provisional += 1
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
    if cboe_hist is not None or failed:
        print(f"  yfinance (provisional): {provisional} cell(s) written where CBOE "
              f"publishes nothing, {deferred_cboe} deferred to CBOE, "
              f"{withheld_failed} WITHHELD (CBOE series failed this run), "
              f"{withheld_settle} WITHHELD (row already basis=SETTLE), "
              f"{withheld_occupied} WITHHELD (cell already holds a value — no overwrite)")
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


def fetch_cboe_history(sym: str) -> tuple[dict[str, float], bool]:
    """One CBOE daily-prices CSV -> ({iso_date: close}, ok).

    ⚠️ THE SECOND RETURN VALUE IS THE WHOLE POINT (added 2026-09-06, WQ-188 fix ①).
    This used to return a bare dict and signal failure with `{}` — which is the
    SAME value a successful fetch of an empty file returns, so the caller could
    not tell "CBOE says nothing here" from "CBOE did not answer". That ambiguity
    is what let the run fail OPEN: a 503 looked like an empty result, the pass
    was skipped, yfinance's values stood, and the run exited 0. `ok` is False
    ONLY for a transport/HTTP/parse failure — an authoritative empty answer is
    (`{}`, True). Callers must gate WRITE AUTHORITY on `ok`, never on truthiness.

    ⚠️ THE STRUCTURE CHECK BELOW IS THE HALF THE 2026-09-06 AM FIX MISSED, AND THE
    DOCSTRING ABOVE ASSERTED IT BEFORE THE CODE DID (Codex 2nd pass, WQ-188
    follow-up, PROME-verified). "`ok` is False ... for a ... parse failure" was
    written as a guarantee while NO parse check existed: an HTTP-200 body of HTML
    (a CDN error page, a captive portal, a redirect stub) yields zero rows with a
    `DATE` key, and the loop below simply skips them all and returns ({}, True) —
    *the identical value an authoritative empty answer returns*. So the sentinel
    collision I closed on the TRANSPORT axis was still wide open on the CONTENT
    axis, one layer down: the column never enters `failed`, yfinance keeps write
    authority, and `main()` exits 0. **I fixed the half the failure report named
    and the docstring then certified the half it did not**
    [[finding_a_correction_pass_is_unreviewed_work]].
    ⇒ Validate the SHAPE of a 200, not just its status: a real daily-prices CSV
    has a DATE column plus CLOSE (OHLC indices) or a column named for the index
    (VVIX/SKEW) — verified live 2026-09-06 against all six endpoints. Anything
    else is a parse failure and fails CLOSED. A well-formed CSV with a valid
    header and no data rows is still ({}, True): that is a real empty answer.
    """
    try:
        r = requests.get(CBOE_HISTORY_URL.format(sym=sym), timeout=30,
                         headers={"User-Agent": "Mozilla/5.0"})
    except requests.RequestException as e:
        print(f"    ⚠ CBOE {sym}: request FAILED ({type(e).__name__}) — NOT used this run")
        return {}, False
    if r.status_code != 200:
        print(f"    ⚠ CBOE {sym}: HTTP {r.status_code} — NOT used this run")
        return {}, False
    reader = csv.DictReader(io.StringIO(r.text))
    fields = [f.strip() for f in (reader.fieldnames or []) if f]
    if "DATE" not in fields and "Date" not in fields:
        print(f"    ⚠ CBOE {sym}: HTTP 200 but body is NOT a daily-prices CSV "
              f"(no DATE column; header={fields[:4]}) — parse FAILURE, NOT used this run")
        return {}, False
    if "CLOSE" not in fields and sym not in fields:
        print(f"    ⚠ CBOE {sym}: HTTP 200 but no CLOSE/{sym} value column "
              f"(header={fields[:6]}) — parse FAILURE, NOT used this run")
        return {}, False
    out: dict[str, float] = {}
    for row in reader:
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
    return out, True


def fetch_all_cboe() -> tuple[dict[str, dict[str, float]], set[str]]:
    """Fetch all six CBOE series up front. -> (hist_by_column, failed_columns).

    Fetched BEFORE the yfinance pass so that yfinance's write authority can be
    scoped by what CBOE actually confirmed this run — see backfill_spot().
    """
    print("  Fetching CBOE daily-prices CSVs (publisher of record) for "
          f"{list(CBOE_SERIES.values())}")
    hist: dict[str, dict[str, float]] = {}
    failed: set[str] = set()
    for col, sym in CBOE_SERIES.items():
        data, ok = fetch_cboe_history(sym)
        hist[col] = data
        if not ok:
            failed.add(col)
    return hist, failed


def backfill_spot_cboe(rows: dict[str, dict], today: str | None = None,
                       hist: dict[str, dict[str, float]] | None = None,
                       failed: set[str] | None = None) -> dict[str, int]:
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
    if hist is None:
        hist, fetch_failed = fetch_all_cboe()
        failed = fetch_failed if failed is None else (set(failed) | fetch_failed)
    failed = set(failed or ())
    if failed:
        # ⚠️ NOT "yfinance stands". A failed series means this column is
        # UNVERIFIABLE this run, so nothing writes it — the previously verified
        # value is preserved and `main` exits non-zero. The old branch here
        # printed "CBOE pass SKIPPED (yfinance stands)", returned zeros, and let
        # `main` save and exit 0; that is the fail-open Codex found (WQ-188 ①).
        print(f"  🔴 CBOE INCOMPLETE — {len(failed)} of {len(CBOE_SERIES)} series "
              f"unavailable: {sorted(failed)}")
        print("     Those columns are NOT written by anything this run; "
              "previously verified values are PRESERVED.")

    # ── CREATE missing sessions ───────────────────────────────────────────
    # ⚠️ ADDED 2026-09-11. This pass UPDATED rows and never CREATED them, so a
    # ledger gap could not self-heal even when CBOE held the data: the merge loop
    # below iterates `rows.items()`, and a date absent from `rows` was never
    # looked at. On 2026-09-06 a `--spot-only` run over a three-session hole
    # touched 27 rows, added 0, and reported "2,496 cells agreed" — a clean
    # verdict over a gap it structurally could not see. It is the exact partner
    # of the `vx_daily_gapcheck.py` span defect (KB-VIO-273): one instrument
    # could not DETECT a trailing gap, this one could not REPAIR it, and fixing
    # either alone leaves the hole.
    #
    # A row is created ONLY for a CBOE TRUE SESSION — VIX published *and* at
    # least one companion — which is the same discriminator the gapcheck uses and
    # is what keeps the 14 holiday phantoms (orphan VIX) out of the ledger. The
    # window is bounded by the ledger's own first row and CBOE's publication
    # frontier: this heals gaps, it never extends history backwards and never
    # invents a session ahead of the publisher.
    #
    # Skeletons are EMPTY. Everything downstream then does the real work: the
    # merge loop fills each spot column from CBOE, the derived ratios follow
    # their inputs, `regime` is computed, and the stateless all-columns-confirmed
    # test stamps `basis=SETTLE`. m1m2 columns are left BLANK — a blank is the
    # absence of a claim, and the T-1-vs-same-day convention hazard is unresolved.
    created: list[str] = []
    if not failed and rows:
        companion_cols = [c for c in CBOE_SERIES if c != "vix"]
        lo_led = min(rows)
        frontier = max((d for d in hist["vix"]
                        if any(hist.get(c, {}).get(d) is not None
                               for c in companion_cols)), default=None)
        if frontier is not None:
            for d_str in sorted(hist["vix"]):
                if not (lo_led <= d_str <= frontier) or d_str in rows:
                    continue
                if not any(hist.get(c, {}).get(d_str) is not None
                           for c in companion_cols):
                    continue  # orphan VIX = holiday phantom, never create
                rows[d_str] = {"date": d_str}
                created.append(d_str)
    if created:
        print(f"  🆕 CREATED {len(created)} missing session row(s) CBOE published "
              f"and the ledger lacked: {', '.join(created)}")
        print("     (filled from CBOE below; m1m2 left BLANK by convention)")

    filled = corrected = agreed = settle_stamped = 0
    settle_withheld_provisional = 0
    corrections: list[str] = []
    for d_str, row in rows.items():
        for col in CBOE_SERIES:
            if col in failed:
                continue
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

        # A completed session CBOE has published is a SETTLE by construction —
        # but ONLY when EVERY spot column the label covers was confirmed by CBOE
        # for that date. `basis` is a ROW-level claim, so a row holding even one
        # unverified column must not be stamped: that stamp is what made Codex's
        # case dangerous rather than merely wrong (149.00 carrying a SETTLE label).
        #
        # ⚠️ THIS TEST IS STATELESS ON PURPOSE, AND THAT IS THE 3RD-PASS FIX.
        # The 2nd pass gated on `d_str in provisional_rows` — a set built during
        # THIS run. It held on run 1 and FAILED ON RUN 2 (Codex, reproduced here):
        # the provisional 149.00 is on disk, the destination gate correctly
        # PRESERVES it, so no new provisional write is recorded, the set is empty
        # — and the stamp condition then only asked whether CBOE had `vix`. Result:
        # run 1 leaves basis blank, run 2 stamps SETTLE over the mirror value.
        # 🔑 A GUARD WHOSE MEMORY IS SHORTER THAN THE STATE IT GUARDS FAILS ON THE
        # SECOND RUN. The state (a provisional cell) is PERSISTENT; the evidence
        # for it was per-run. The fix is not to persist the bookkeeping but to
        # stop needing it: read the invariant off the ROW ITSELF, which is where
        # the state actually lives.
        # ⚠️ AND THE COMMENT ABOVE ALREADY STATED THIS INVARIANT ("every column
        # ... confirmed by CBOE") WHILE THE CODE CHECKED ONLY `vix` — the second
        # time in one day that a comment in this file certified what the code did
        # not do (cf. fetch_cboe_history's "parse failure" docstring).
        #
        # Per column: CBOE confirmed it for this date, OR the cell is blank.
        # A blank is safe — it is the absence of a claim, not a mirror value.
        # This also gives RECOVERY for free: once CBOE publishes the missing
        # series, its pass overwrites the provisional value above and every
        # column becomes confirmed, so the row settles legitimately.
        if not failed and d_str < today and hist["vix"].get(d_str) is not None:
            unconfirmed = [c for c in CBOE_SERIES
                           if hist.get(c, {}).get(d_str) is None
                           and str(row.get(c, "") or "").strip()]
            if unconfirmed:
                settle_withheld_provisional += 1
                continue
            if str(row.get("basis", "") or "").strip() != "SETTLE":
                row["basis"] = "SETTLE"
                settle_stamped += 1

    print(f"  CBOE: {agreed} cell(s) agreed, {filled} blank(s) filled, "
          f"{corrected} CORRECTED, {settle_stamped} row(s) stamped SETTLE, "
          f"{settle_withheld_provisional} row(s) NOT stamped (hold an "
          f"unconfirmed cell)")
    if corrections:
        print(f"  🔴 {len(corrections)} VALUE CORRECTION(S) — ledger was wrong, CBOE wins:")
        for line in corrections:
            print(line)
    return {"filled": filled, "corrected": len(corrections),
            "agreed": agreed, "settle_stamped": settle_stamped,
            "settle_withheld_provisional": settle_withheld_provisional,
            "created": len(created)}


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

    cboe_failed: set[str] = set()
    if not args.m1m2_only:
        # CBOE IS FETCHED FIRST so that yfinance's write authority can be scoped
        # by what the publisher of record actually confirmed THIS RUN. The old
        # order (yfinance writes -> CBOE corrects) meant a CBOE failure left
        # yfinance's writes standing, which is the fail-open (WQ-188 ①).
        print("\n[1a] Fetching CBOE (publisher of record) BEFORE any write...")
        cboe_hist, cboe_failed = fetch_all_cboe()

        print(f"\n[1b] yfinance provisional pass ({args.spot_days} days)...")
        touched = backfill_spot(args.spot_days, rows,
                                cboe_hist=cboe_hist, cboe_failed=cboe_failed)
        print(f"  touched {touched} rows")

        print("\n[1c] Writing spot columns from CBOE (authoritative)...")
        backfill_spot_cboe(rows, hist=cboe_hist, failed=cboe_failed)

    if not args.spot_only:
        print(f"\n[2/2] Backfilling M1:M2 steepness ({args.m1m2_days} trading days)...")
        touched = backfill_m1m2(args.m1m2_days, rows, allow=args.allow_m1m2)
        print(f"  touched {touched} rows")

    write_merged(header, rows)
    print(f"\n✓ wrote {len(rows)} rows to {DAILY_LOG}")

    # LOUD, NON-ZERO, AND NAMED. A partial refresh is not a success: the six
    # spot columns are the basis of every graded ^SKEW sustain claim, so a run
    # that could not reach the publisher of record must say so in its exit code,
    # not only in scrollback that nobody reads. Values on disk are the ones CBOE
    # previously verified — safe, but STALE, and the caller has to know which.
    if cboe_failed:
        print(f"\n🔴 BACKFILL INCOMPLETE — CBOE unavailable for "
              f"{len(cboe_failed)} of {len(CBOE_SERIES)} series: {sorted(cboe_failed)}")
        print("   Those columns were NOT refreshed and NOT overwritten; "
              "no basis=SETTLE was stamped this run. Re-run when CBOE is reachable.")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
