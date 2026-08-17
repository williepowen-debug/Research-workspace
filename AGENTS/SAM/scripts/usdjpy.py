#!/usr/bin/env python3
"""
SAM USDJPY History + At-a-Glance Summary

Fetches USDJPY=X daily OHLC from Yahoo Finance, maintains workbook/USDJPY.tsv
(5Y rolling), and prints a compact summary block: current level, recent
ranges (30d/90d/52wk), and days since last intraday touch of key levels.

Source: Yahoo Finance via yfinance (USDJPY=X)

Reference levels (matched to THESIS KEY THRESHOLDS):
  160  Historic MOF strike zone (Apr30/May6 2026); live playbook zone 162-163, disorder-not-level (CH-011)
  155  Phase 2 carry unwind onset
  150  Psychological / mid-cycle
  145  Forced unwind / unhedged positions underwater
  140  Aug 2024 post-unwind low / structural floor

"Touch" semantics: directional. For levels ABOVE current close (yen-weak side),
days since HIGH reached up to level (e.g., last time we hit intervention zone).
For levels BELOW current close (yen-strong side), days since LOW reached down
to level (e.g., last time yen was that strong). Always asks "when did we last
touch this level from the current side?"

Usage:
  .venv/bin/python3 AGENTS/SAM/scripts/usdjpy.py              # refresh + summary
  .venv/bin/python3 AGENTS/SAM/scripts/usdjpy.py --summary    # summary only
  .venv/bin/python3 AGENTS/SAM/scripts/usdjpy.py --refresh    # refresh only
"""

import sys
from datetime import date, datetime, timedelta
from pathlib import Path

SAM_DIR = Path(__file__).resolve().parent.parent
WORKBOOK = SAM_DIR / "workbook"
USDJPY_TSV = WORKBOOK / "USDJPY.tsv"

TSV_HEADER = "Date\tOpen\tHigh\tLow\tClose\n"

# Reference levels matched to THESIS KEY THRESHOLDS table
REFERENCE_LEVELS = [
    (160, "MOF historic-strike zone"),
    (155, "Phase 2 onset"),
    (150, "Psychological"),
    (145, "Forced unwind"),
    (140, "Aug 2024 low"),
]

# Touch tolerance — within this many yen counts as a touch of the level.
# Reason: strict ≥/≤ comparison failed May 6 (low 155.05 missed 155 as a Phase 2 touch).
# 0.10y captures near-touches without losing precision on the 5y-range thresholds.
TOUCH_TOLERANCE = 0.10

# Intraday-range alert thresholds (high - low for a single trading day).
# Calibrated against MOF intervention events:
#   Apr 30 2026: 5.15y range (¥5.48T intervention)
#   May 6 2026:  2.84y range (¥4.3T intervention)
# Normal USDJPY daily range is 0.5-1.5y. >2.5y is a stress event.
INTRADAY_RANGE_WARN = 2.5      # 🟠 stress event — investigate
INTRADAY_RANGE_CRIT = 4.0      # 🔴 intervention-grade move

# Confirmed MOF intervention episodes (public record). Touches near these
# dates get a MOF marker; touches NOT near these dates = "no MOF" (level was
# hit naturally without policy response).
# Format: (date, label_compact, size_trillion_yen_or_None, actor)
# Labels use MonYYYY (e.g. "May2026") — never "May26", which mis-reads as a
# day-of-month ("May 26"); that exact mis-parse propagated on 2026-06-09.
#
# `actor` added 2026-08-03: this stopped being a MOF-only list on 7/31, when the US
# TREASURY bought yen. Marking a US operation "MOF" would be a category error, and the
# distinction is load-bearing — SAM's registered discriminator for the 7/31 session was
# the BOJ current-account Tanshi gap, which reads JAPANESE fiscal factors and is
# therefore structurally incapable of seeing a US-side op. A null print there would have
# graded a confirmed intervention as "no op." Keep the sovereign explicit.
#
# `size` is None where no figure is official — never fabricate one (root rule #3).
MOF_INTERVENTIONS = [
    ("2022-09-22", "Sep2022", 2.84, "MOF"),  # first since 1998; USDJPY 145 → 140
    ("2022-10-21", "Oct2022", 6.35, "MOF"),  # stealth Oct 21-24; combined Q4 2022 ¥9.2T
    ("2024-04-29", "Apr2024", 5.5, "MOF"),   # first 2024 act; USDJPY 160.17 peak
    ("2024-05-01", "May2024", 4.3, "MOF"),   # second 2024 act; combined Apr/May ¥9.8T
    ("2024-07-11", "Jul2024", 5.5, "MOF"),   # pre-Aug 2024 unwind
    ("2026-04-30", "Apr2026", 5.48, "MOF"),  # post Apr 28 BOJ hawkish hold; USDJPY 160.70 peak → 155.55 intraday low (5.15y range); first since Jul 2024
    ("2026-05-06", "May2026", 4.3, "MOF"),   # Golden Week round; intraday low 155.05 (2.84y range); combined Apr/May ~¥10T (~$63.5B) — largest since 2022 per BofA
    # --- the Jul-30/31 round (added 2026-08-03) ---
    # 7/30: occurrence Reuters source-confirmed (NY session); ~¥8.45T is a BLOOMBERG
    #       ESTIMATE off the BOJ projection gap, NOT a MOF figure. Hard confirm ~Aug-31
    #       (MOF monthly, Jul-30→Aug-27 window). Size left None deliberately.
    #       SAM's own detector grades it INTERVENTION-GRADE (5.82y intraday range).
    ("2026-07-30", "Jul2026", None, "MOF"),
    # 7/31: US TREASURY, not MOF. NY Fed sold EUROS for yen on Treasury's own account
    #       through Goldman Sachs + Morgan Stanley. Officially confirmed by BOTH
    #       governments (Bessent statement 8/2 ~19:00 ET); first joint US-Japan
    #       yen-buying intervention in over a decade, executed under the September 2025
    #       Joint Statement of the two finance ministers. Reuters photographed Bessent's
    #       notepad reading "$5-10 bil" — INTENDED scale, not an executed amount, so
    #       size stays None. Whether MOF *also* acted on 7/31 is still open.
    ("2026-07-31", "Jul2026", None, "USTreasury"),
]
INTERVENTION_WINDOW_DAYS = 3  # touch date within ±N days of intervention = match

# ---------------------------------------------------------------------------
# SOURCE-INTEGRITY LAYER (added 2026-08-03, Will-directed)
#
# Why this exists. The 2026-08-02 fix stopped the script appending bars it KNEW
# were partial (the local-vs-index timezone bug). It gave the script no way to
# notice a bar that is SILENTLY TRUNCATED but looks final — and yfinance's daily
# FX bars are exactly that. Measured against hourly ground truth over the last 45
# sessions: 7 rows understate the true range by >0.30y, one (2026-07-31) by 1.487y
# — recorded 2.168y against a true 3.655y, on a session now confirmed to contain a
# US Treasury yen-buying intervention. The bias is SYSTEMATICALLY DIRECTIONAL: the
# daily bar almost always UNDER-states. For a detector whose entire job is to fire
# on large ranges, that is a false-negative-biased instrument — the worst direction.
#
# The signature is visible in the raw data: Open ≈ Close on nearly every row
# (7/28 163.792/163.771, 7/29 163.858/163.864, 7/31 160.179/160.183). Yahoo's daily
# FX "Close" is a bar-boundary snapshot, not the session's last trade.
#
# Three layers, because fixing only the first would have left the next defect
# equally invisible and equally permanent:
#   L1  Derive sessions from HOURLY bars, not the daily series (fetch_hourly_sessions).
#   L2  UPSERT recent rows instead of append-only, so a bad row can heal on the next
#       boot. Append-only + idempotent-by-date made every bad row PERMANENT — a
#       re-pull could not fix it, which is why the 8/2 repair silently regressed the
#       very next day. See auto-memory finding_partial_record_written_as_final_never_heals.
#   L3  A DISAGREEMENT alarm, not a freshness check. A staleness check compares
#       mtime and happily passes a fresh-but-false row, so it cannot see this class
#       at all; what catches it is two instruments disagreeing. That is literally how
#       the 8/2 bug was found — one module printed 157.22 and another 160.71, and the
#       disagreement was the only free alarm. See finding_freshness_check_cannot_catch_a_fresh_lie.
#
# Session convention: LONDON CALENDAR DAY. Chosen empirically, not by preference —
# it reproduces the existing 5y series most closely (median |range diff| 0.071y vs
# 0.089y for an ET-calendar grouping) AND recovers the independently-verified
# 2026-07-31 close of 157.40 (confirmed three ways: investing.com 157.3950, the live
# quote, and yfinance's own previousClose field). Continuity with the existing date
# labels is preserved; no historical re-labelling.
# ---------------------------------------------------------------------------

SESSION_TZ = "Europe/London"   # yfinance labels USDJPY=X bars in London time
REVISION_WINDOW_DAYS = 10      # L2: rows this recent are recomputed + overwritten each run
                               #     override for a one-off backfill: --revise-window N
                               #     (L3 surfaces pre-fix truncated rows OLDER than this window;
                               #      they cannot self-heal until the window is widened once)
HOURLY_LOOKBACK_DAYS = 60      # L1/L3: hourly window pulled for revision + audit
REVISION_EPSILON = 0.005       # yen; below this a difference is rounding, not a revision
RANGE_DISAGREEMENT_ALARM = 0.30  # L3: daily-vs-hourly range gap that trips the alarm
FLAT_BAR_EPSILON = 0.02        # L3: |Open-Close| under this = a suspect "flat" bar
FLAT_BAR_FRACTION_ALARM = 0.60   # L3: share of recent flat bars that trips the class alarm


def fetch_yfinance(period="5y"):
    """Fetch USDJPY=X OHLC from yfinance. Returns DataFrame or None."""
    try:
        import yfinance as yf
        ticker = yf.Ticker("USDJPY=X")
        df = ticker.history(period=period, interval="1d", auto_adjust=False)
        if df.empty:
            return None
        return df
    except Exception as e:
        print(f"  ERROR fetching from yfinance: {e}")
        return None


def fetch_hourly_sessions(days=HOURLY_LOOKBACK_DAYS):
    """L1 — derive daily sessions from HOURLY bars instead of trusting the daily series.

    Groups 1h bars by LONDON calendar date (see SOURCE-INTEGRITY note) and aggregates
    O/H/L/C ourselves. Returns {date_str: (open, high, low, close)} or {} on failure.

    The current (incomplete) session is dropped — same reasoning as the daily path.
    Hourly history is bounded (~730d) while the workbook is 5Y, but that is not a
    limitation in practice: every consumer of this file reads a RECENT window (the
    5-day intraday-range alert, the 30/90/365d range lines), so the series only needs
    to be hourly-accurate where hourly exists. Deep history stays on the daily source.
    """
    try:
        import yfinance as yf
        h = yf.Ticker("USDJPY=X").history(period=f"{days}d", interval="1h")
        if h.empty:
            # ⚠️ Was a SILENT `return {}` until 2026-08-17 (DAEDALUS SFG sweep addendum 2;
            # verified at source). The exception path below already printed; this one did
            # not — and an empty frame is the MORE likely yfinance failure, since it is
            # what a rate-limit or an out-of-range window returns without raising.
            # The cost is specific and ironic: `hourly` is the ONLY input to the L3
            # disagreement alarm, and L3 is this file's own stated "only free alarm" for
            # truncated daily bars (see the L3 note above — a freshness check is blind to
            # that class by construction). So a quiet empty here DISABLES THE GUARD
            # rather than the data, and the run still exits 0 looking fully checked.
            print("  ⚠️  hourly fetch returned an EMPTY frame (no exception) — "
                  "falling back to daily bars only")
            return {}
        h = h.copy()
        h.index = h.index.tz_convert(SESSION_TZ)
        today_str = datetime.now(h.index.tz).strftime("%Y-%m-%d")

        sessions = {}
        for day, chunk in h.groupby(h.index.strftime("%Y-%m-%d")):
            if day >= today_str:      # current session still printing
                continue
            chunk = chunk.sort_index()
            o, hi = float(chunk["Open"].iloc[0]), float(chunk["High"].max())
            lo, cl = float(chunk["Low"].min()), float(chunk["Close"].iloc[-1])
            if any(v != v for v in (o, hi, lo, cl)):   # NaN guard
                continue
            sessions[day] = (o, hi, lo, cl)
        return sessions
    except Exception as e:
        print(f"  ⚠️  hourly fetch failed ({e}) — falling back to daily bars only")
        return {}


def write_tsv(rows):
    """Atomically rewrite the TSV from `rows` (list of dicts, any order).

    Atomic (temp + os.replace) because L2 rewrites rather than appends, and this
    file lives in a shared repo — a half-written ledger is worse than a stale one.
    """
    import os, tempfile
    rows = sorted(rows, key=lambda r: r["date"])
    fd, tmp = tempfile.mkstemp(dir=str(WORKBOOK), prefix=".USDJPY.", suffix=".tmp")
    try:
        with os.fdopen(fd, "w") as f:
            f.write(TSV_HEADER)
            for r in rows:
                f.write(f"{r['date']}\t{r['open']:.4f}\t{r['high']:.4f}"
                        f"\t{r['low']:.4f}\t{r['close']:.4f}\n")
        os.replace(tmp, USDJPY_TSV)
    except Exception:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise


def load_tsv():
    """Load existing TSV into list of dicts ordered by date asc. [] if missing."""
    if not USDJPY_TSV.exists():
        return []
    rows = []
    with open(USDJPY_TSV) as f:
        next(f, None)  # skip header
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if len(parts) >= 5:
                try:
                    rows.append({
                        "date": parts[0],
                        "open": float(parts[1]),
                        "high": float(parts[2]),
                        "low": float(parts[3]),
                        "close": float(parts[4]),
                    })
                except ValueError:
                    pass
    rows.sort(key=lambda r: r["date"])
    return rows


def merge_and_write(df, hourly=None):
    """L2 — UPSERT fully-closed sessions into the TSV. Skips today (intraday partial).

    Two-pass:
      1. APPEND any date missing from the file (daily source — this is what keeps 5Y
         of history alive beyond the hourly window).
      2. REVISE the last REVISION_WINDOW_DAYS: recompute from `hourly` and OVERWRITE
         where the stored row disagrees. This is the layer that matters. The old
         append-only/idempotent-by-date behaviour made every bad row PERMANENT — a
         re-pull could not correct it, so the 8/2 repair regressed the next day when
         the same source handed back the same truncated bar. Rows older than the
         window are frozen (hourly can't reach them, and silent deep-history churn
         would be worse than the defect).

    Returns (appended, revised, revision_details).
    """
    hourly = hourly or {}
    existing = {r["date"]: r for r in load_tsv()}
    if not USDJPY_TSV.exists():
        with open(USDJPY_TSV, "w") as f:
            f.write(TSV_HEADER)

    # Derive "today" in the INDEX's own timezone, not local time. yfinance labels
    # USDJPY=X bars in Europe/London; comparing them against a local (Eastern) date
    # meant any boot run after ~19:00 ET saw the next London-day's few-hours-old
    # partial bar as "not today" and appended it as final. Idempotent-by-date then
    # made it permanent. That wrote truncated bars for 10 of the last 60 sessions —
    # every one under-stating the range — including 2026-07-30, recorded as a 0.33y
    # day when the true range was 5.74y (largest yen move since Dec-2023, suspected
    # MOF op). The intraday-range alert below is the disorder detector gating the MOF
    # strike-watch, so the failure was silent and FALSE-NEGATIVE.
    idx_tz = getattr(df.index, "tz", None)
    today_str = datetime.now(idx_tz).strftime("%Y-%m-%d")

    # ---- pass 1: append dates the file has never seen (daily source) ----
    appended = 0
    for ts, row in df.iterrows():
        date_str = ts.strftime("%Y-%m-%d")
        if date_str in existing:
            continue
        # Skip today AND anything later — USDJPY=X trades 24/5, so the current bar is
        # an intraday partial. Let it land in TSV tomorrow when the day is fully closed.
        if date_str >= today_str:
            continue
        # NaN check (yfinance can return NaN rows for non-trading days)
        vals = [row["Open"], row["High"], row["Low"], row["Close"]]
        if any(v != v for v in vals):  # NaN != NaN
            continue
        # Prefer the hourly-derived session even on first write, so a new row never
        # enters the ledger truncated in the first place.
        if date_str in hourly:
            o, hi, lo, cl = hourly[date_str]
        else:
            o, hi, lo, cl = vals
        existing[date_str] = {"date": date_str, "open": o, "high": hi,
                              "low": lo, "close": cl}
        appended += 1

    # ---- pass 2: revise the recent window against hourly truth ----
    cutoff = (date.today() - timedelta(days=REVISION_WINDOW_DAYS)).isoformat()
    revisions = []
    for date_str, (o, hi, lo, cl) in sorted(hourly.items()):
        if date_str < cutoff or date_str not in existing:
            continue
        cur = existing[date_str]
        deltas = [abs(cur["open"] - o), abs(cur["high"] - hi),
                  abs(cur["low"] - lo), abs(cur["close"] - cl)]
        if max(deltas) <= REVISION_EPSILON:
            continue
        old_range, new_range = cur["high"] - cur["low"], hi - lo
        revisions.append((date_str, old_range, new_range,
                          cur["close"], cl))
        existing[date_str] = {"date": date_str, "open": o, "high": hi,
                              "low": lo, "close": cl}

    if appended or revisions:
        write_tsv(list(existing.values()))

    return appended, len(revisions), revisions


def audit_source_quality(rows, hourly):
    """L3 — a DISAGREEMENT alarm, not a freshness check.

    A staleness check compares mtime and passes a fresh-but-false row, so it is blind
    to this entire class. Two independent instruments disagreeing is what catches it.

    Two tests:
      (a) per-row: stored range vs hourly-derived range beyond RANGE_DISAGREEMENT_ALARM.
      (b) class-level: the Open≈Close signature. A single flat bar is unremarkable;
          a SUSTAINED majority of flat bars means the source is snapshotting the
          bar boundary rather than reporting the session, which is the root defect.
          Checking the class rather than the row is what makes this durable — it will
          fire on the NEXT variant of this bug, not just the one already found.

    Prints alarms; returns True if anything tripped.
    """
    tripped = False
    by_date = {r["date"]: r for r in rows}

    if hourly:
        gaps = []
        for date_str, (_o, hi, lo, _cl) in hourly.items():
            r = by_date.get(date_str)
            if not r:
                continue
            gap = (hi - lo) - (r["high"] - r["low"])
            if abs(gap) > RANGE_DISAGREEMENT_ALARM:
                gaps.append((date_str, r["high"] - r["low"], hi - lo, gap))
        if gaps:
            tripped = True
            gaps.sort(key=lambda g: -abs(g[3]))
            print(f"  🔴 SOURCE DISAGREEMENT: {len(gaps)} session(s) where the stored "
                  f"range differs from hourly by >{RANGE_DISAGREEMENT_ALARM}y")
            for d, stored, true_r, gap in gaps[:5]:
                direction = "UNDER" if gap > 0 else "OVER"
                print(f"      {d}  stored {stored:.2f}y vs hourly {true_r:.2f}y "
                      f"({gap:+.2f}y — stored {direction}-states)")
            print("      → rows inside the revision window self-heal on this run; "
                  "older rows need a manual pass.")
    else:
        # ⚠️ Test (a) requires the hourly series; with no hourly data it does not run.
        # Saying so is the whole point: an un-evaluated alarm and a passed alarm printed
        # identically before 2026-08-17, so a session could read "no disagreement found"
        # off a check that never executed. A guard that cannot report its own
        # non-execution is a guard you cannot rely on.
        # (Class: a check certifies its SCOPE, not your capability —
        # [[finding_verification_zero_is_ambiguous]].)
        print("  ⚠️  hourly cross-check UNAVAILABLE — L3 test (a), the per-row range "
              "DISAGREEMENT alarm, was NOT EVALUATED this run.")
        print("      → this is the primary guard against truncated daily bars, and a "
              "freshness check cannot substitute for it. Absence of an alarm below is "
              "NOT evidence the rows agree. Test (b) still ran.")

    recent = sorted(rows, key=lambda r: r["date"])[-20:]
    if len(recent) >= 10:
        flat = [r for r in recent
                if abs(r["open"] - r["close"]) < FLAT_BAR_EPSILON
                and (r["high"] - r["low"]) > 0.20]
        frac = len(flat) / len(recent)
        if frac >= FLAT_BAR_FRACTION_ALARM:
            tripped = True
            print(f"  🔴 BAR-BOUNDARY SIGNATURE: {len(flat)}/{len(recent)} recent rows "
                  f"have Open≈Close while ranging >0.20y ({frac:.0%}).")
            print("      → the source is snapshotting the bar boundary, not reporting "
                  "the session close. Same class as the 2026-07-31 defect.")

    return tripped


def color_for_price(close):
    """Color marker reflecting yen-weakness state (FXY-long position lens)."""
    if close >= 160:
        return "🔴"  # intervention zone
    if close >= 156:
        return "🟠"  # close to intervention, fuel accumulating
    if close >= 150:
        return "🟡"  # active range
    return "🟢"      # thesis playing out


def print_summary(rows):
    """Print compact summary block (2 marker-prefixed lines for boot collapse)."""
    if not rows:
        print("  ⚠️  USDJPY.tsv is empty — run --refresh first")
        return

    rows = sorted(rows, key=lambda r: r["date"])  # defensive: key on max-date, not file last-row (fixes Jun-16 out-of-order-append mis-report)
    latest = rows[-1]
    today = date.today()
    latest_date = date.fromisoformat(latest["date"])
    days_since_latest = (today - latest_date).days

    def date_n_days_ago(n):
        return today - timedelta(days=n)

    def range_for_window(days):
        cutoff = date_n_days_ago(days)
        windowed = [r for r in rows if date.fromisoformat(r["date"]) >= cutoff]
        if not windowed:
            return None, None
        return min(r["low"] for r in windowed), max(r["high"] for r in windowed)

    r30 = range_for_window(30)
    r90 = range_for_window(90)
    r52w = range_for_window(365)

    current = latest["close"]

    # 5-trading-day delta (one trading week) — direction/velocity context
    if len(rows) >= 6:
        delta_5d = current - rows[-6]["close"]
    else:
        delta_5d = None

    def days_since_level(level):
        """Directional touch — looks at HIGH for above-current levels,
        LOW for below-current levels. Uses TOUCH_TOLERANCE band so near-touches
        register (e.g., May 6 low 155.05 counts as a touch of 155).
        Returns (days, touch_date_str) or (None, None) if never touched in window."""
        for r in reversed(rows):
            if level >= current:
                if r["high"] >= level - TOUCH_TOLERANCE:
                    td = date.fromisoformat(r["date"])
                    return (today - td).days, r["date"]
            else:
                if r["low"] <= level + TOUCH_TOLERANCE:
                    td = date.fromisoformat(r["date"])
                    return (today - td).days, r["date"]
        return None, None

    def mof_marker(touch_date_str):
        """Returns '<actor> <label>' if touch is within window of an intervention,
        else 'no op'. Returns '' if touch_date_str is None.

        Names the ACTOR rather than assuming MOF — since 2026-07-31 the list contains
        a US Treasury operation, and collapsing the two sovereigns would hide exactly
        the distinction that matters for which confirmation instrument applies.
        Where several actors intervened inside the window, all are named.
        """
        if not touch_date_str:
            return ""
        td = date.fromisoformat(touch_date_str)
        hits = []
        for iv_date_str, label, _size, actor in MOF_INTERVENTIONS:
            iv_d = date.fromisoformat(iv_date_str)
            if abs((td - iv_d).days) <= INTERVENTION_WINDOW_DAYS:
                tag = f"{actor} {label}"
                if tag not in hits:
                    hits.append(tag)
        return " + ".join(hits) if hits else "no op"

    color = color_for_price(current)
    stale_tag = f" (STALE +{days_since_latest}d)" if days_since_latest > 3 else ""
    trend_tag = f" (5d: {delta_5d:+.1f})" if delta_5d is not None else ""

    line1 = (
        f"  {color} USDJPY {current:.2f}{trend_tag}{stale_tag} | "
        f"30d: {r30[0]:.1f}-{r30[1]:.1f} | "
        f"90d: {r90[0]:.1f}-{r90[1]:.1f} | "
        f"52wk: {r52w[0]:.1f}-{r52w[1]:.1f}"
    )
    print(line1)

    # Format: "level → Nd, MOF state" — arrow disambiguates level from days count
    touch_parts = []
    for level, _name in REFERENCE_LEVELS:
        days, touch_date_str = days_since_level(level)
        if days is None:
            touch_parts.append(f"{level} → n/a")
        else:
            marker = mof_marker(touch_date_str)
            touch_parts.append(f"{level} → {days}d, {marker}")
    line2 = f"  {color} Days since touch: " + " | ".join(touch_parts)
    print(line2)

    # Intraday-range alert — flag single-day high-low moves that suggest
    # intervention or capitulation. Apr 30 2026 misread as "Tokyo session reprice"
    # because close-to-close looked tame (intraday range was 5.15y = MOF intervention).
    recent = rows[-5:] if len(rows) >= 5 else rows
    ranges = [(r["date"], r["high"] - r["low"]) for r in recent]
    max_date, max_range = max(ranges, key=lambda x: x[1])
    latest_range = rows[-1]["high"] - rows[-1]["low"]

    range_marker = "🟢"
    range_note = "normal daily range"
    if max_range >= INTRADAY_RANGE_CRIT:
        range_marker = "🔴"
        range_note = f"INTERVENTION-GRADE move {max_date} ({max_range:.2f}y intraday range)"
    elif max_range >= INTRADAY_RANGE_WARN:
        range_marker = "🟠"
        range_note = f"stress-event move {max_date} ({max_range:.2f}y intraday range — investigate)"

    print(f"  {range_marker} Intraday range (5d max): {max_range:.2f}y on {max_date} | latest: {latest_range:.2f}y | {range_note}")


def main():
    global REVISION_WINDOW_DAYS

    summary_only = "--summary" in sys.argv
    refresh_only = "--refresh" in sys.argv

    # One-off backfill hatch. L3 audits the full hourly lookback but L2 only
    # rewrites inside REVISION_WINDOW_DAYS, so rows older than the window get
    # reported every run and never repaired. Widening the window is a deliberate
    # act (it rewrites history), so it is a flag, not a default.
    if "--revise-window" in sys.argv:
        i = sys.argv.index("--revise-window")
        if i + 1 >= len(sys.argv):
            print("  ⚠️  --revise-window needs a value in days")
            return 2
        try:
            REVISION_WINDOW_DAYS = int(sys.argv[i + 1])
        except ValueError:
            print(f"  ⚠️  --revise-window: '{sys.argv[i + 1]}' is not an integer")
            return 2
        if REVISION_WINDOW_DAYS > HOURLY_LOOKBACK_DAYS:
            print(f"  ⚠️  --revise-window {REVISION_WINDOW_DAYS}d exceeds the "
                  f"{HOURLY_LOOKBACK_DAYS}d hourly lookback — rows older than "
                  f"the lookback have no hourly truth to revise against")

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"\n{'='*70}")
    print(f"  SAM USDJPY Monitor — {now}")
    print(f"{'='*70}\n")

    hourly = {}
    if not summary_only:
        hourly = fetch_hourly_sessions()          # L1
        df = fetch_yfinance(period="5y")
        if df is None:
            print("  ⚠️  yfinance fetch failed — falling back to cached TSV")
        else:
            appended, revised, revisions = merge_and_write(df, hourly)   # L2
            bits = []
            if appended:
                bits.append(f"appended {appended} new row(s)")
            if revised:
                bits.append(f"REVISED {revised} row(s) against hourly")
            print(f"  ✓ USDJPY.tsv — {', '.join(bits) if bits else 'up to date'}")
            for d, old_r, new_r, old_c, new_c in revisions:
                print(f"      ↻ {d}: range {old_r:.2f}y → {new_r:.2f}y | "
                      f"close {old_c:.3f} → {new_c:.3f}")
            if hourly:
                print(f"  ✓ hourly cross-check: {len(hourly)} session(s) "
                      f"(revision window {REVISION_WINDOW_DAYS}d)")

    if not refresh_only:
        rows = load_tsv()
        if not rows:
            print("  ⚠️  USDJPY.tsv empty or missing")
            return 1
        print()
        print_summary(rows)
        audit_source_quality(rows, hourly)         # L3

    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
