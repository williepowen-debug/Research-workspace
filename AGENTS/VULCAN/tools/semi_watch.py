#!/usr/bin/env python3
"""
semi_watch.py — VULCAN S2 instrument: retain a memory-cycle series.

WHY THIS EXISTS (2026-08-03): S2 was upgraded to score 3 while VULCAN held
*zero* retained history for it. The 8/3 spot levels were a POINT, not a trend
(`finding_owned_surface_without_a_ledger_destroys_history`). A channel whose
live read lives only in a rewritten STATUS has no history at all.

WHAT IT RECORDS  -> workbook/S2_SERIES.tsv (append-only, one row per run)
  1. DRAM spot   — TrendForce public spot tracker (DDR5 / DDR4 session averages)
  2. The equity cross-section that IS the S2 leading indicator (KB-048):
     memory (MU/SNDK/WDC/STX) + semicap (KLAC/LRCX/AMAT) + foundry (TSM)
     vs AI-compute (NVDA/AVGO) and QQQ.

⚠️ DESIGN NOTES — read before changing:
  * The cross-section is deliberately CONSTITUENT-level, not index-level.
    Semis entered this earnings season priced for DISPERSION (KB-067), and an
    index-only read understates the move — SOXX fell 0.55% on 8/3 while its
    constituents split 13-26%. Do NOT "simplify" this to SOXX.
  * Contract prices are NOT scraped. They are quarterly, LTA-governed and
    forecast-revised (KB-049/055); they belong in KB.tsv with a source, not in
    an automated series that would imply a daily cadence they don't have.
  * ⚠️ THE SPREAD COLUMN HAS A BASIS AND YOU MUST QUOTE IT (added 2026-08-21).
    `spread_aicompute_minus_memory_pp` is computed on a CALENDAR one-month window,
    RAW closes, memory = MU/SNDK/WDC/STX. Those three choices are not neutral:
    on 2026-08-21 the semicap-minus-memory spread read -5.78pp (this construction),
    -4.04pp with SNDK dropped, and -1.92pp on 21 TRADING days with adjusted closes.
    THE SAME DAY, THREE DEFENSIBLE READINGS OF "ONE MONTH", 3.86pp APART.
    A spread quoted without its construction reports the analyst's choice, not the
    market — L-17's cousin (unspecified BASIS rather than extremum-anchored WINDOW).
    ⚠️ AND BEFORE CALLING ANY DIVERGENCE A FINDING, BASE-RATE IT: semicap-vs-memory
    divergence >=5pp on a rolling month occurs on 55.4% of days since 2005 (KB-105).
    A coin-flip event discriminates nothing.
  * FAIL LOUD. A spot fetch that breaks writes `ERR:<reason>`, never a blank
    and never a stale carry-forward (`finding_silent_blank_evades_review`,
    `finding_plausible_stale_value_evades_review`).
  * Vintage is CONTENT-derived (`asof_utc` written into the row), never mtime
    — git sync restamps mtime (`finding_mtime_is_corrupted_by_git_sync`).

USAGE
  python3 AGENTS/VULCAN/tools/semi_watch.py            # fetch + append a row
  python3 AGENTS/VULCAN/tools/semi_watch.py --dry-run  # print, do not write
  python3 AGENTS/VULCAN/tools/semi_watch.py --show 10  # last N retained rows

EXIT CODES:  0 = row written (or shown) · 1 = partial (some legs ERR) · 2 = total failure
"""

from __future__ import annotations

import argparse
import datetime as _dt
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
AGENT_DIR = os.path.dirname(HERE)
REPO_ROOT = os.path.dirname(os.path.dirname(AGENT_DIR))
SERIES = os.path.join(AGENT_DIR, "workbook", "S2_SERIES.tsv")


def _reexec_under_venv() -> None:
    """Re-exec under the repo venv if this interpreter lacks yfinance.

    ⚠️ 2026-08-13: the equity cross-section — the ENTIRE leading-indicator leg,
    and the evidence S2's score-3 rests on — silently degraded to 8x
    `ERR:yfinance-missing` because yfinance lives ONLY in `.venv/`, while this
    file's own USAGE block, boot.py's printed recipe and CLAUDE.md all said bare
    `python3`. The instrument failed loud (as designed) and the RECIPE was wrong,
    so a correct-looking run wrote a row with no equity leg in it. Fixing the
    three doc strings is not enough — the next reader invokes it from memory or
    from a spawn packet. Make the tool itself immune to how it is called.
    """
    try:
        import yfinance  # noqa: F401
        return
    except ImportError:
        pass
    venv_py = os.path.join(REPO_ROOT, ".venv", "bin", "python")
    if os.environ.get("VULCAN_SEMI_WATCH_REEXEC") or not os.path.exists(venv_py):
        return  # already retried, or no venv — fall through and ERR loudly
    os.environ["VULCAN_SEMI_WATCH_REEXEC"] = "1"
    os.execv(venv_py, [venv_py, os.path.abspath(__file__)] + sys.argv[1:])


_reexec_under_venv()

SPOT_URL = "https://www.trendforce.com/price/dram/dram_spot"

# constituent cross-section — see KB-048 / KB-067
MEMORY = ["MU", "SNDK", "WDC", "STX"]
SEMICAP = ["KLAC", "LRCX", "AMAT"]
FOUNDRY = ["TSM"]
AICOMPUTE = ["NVDA", "AVGO"]
BENCH = ["QQQ", "SOXX"]
TICKERS = MEMORY + SEMICAP + FOUNDRY + AICOMPUTE + BENCH

COLUMNS = [
    "asof_utc", "trade_date",
    "ddr5_spot_avg", "ddr5_chg_pct", "ddr4_spot_avg", "ddr4_chg_pct", "spot_asof",
    "memory_1mo_pct", "semicap_1mo_pct", "foundry_1mo_pct",
    "aicompute_1mo_pct", "qqq_1mo_pct", "soxx_1mo_pct",
    "spread_aicompute_minus_memory_pp",
    "per_ticker_1mo_pct", "notes",
]


def _err(msg: str) -> str:
    return "ERR:" + re.sub(r"\s+", " ", str(msg))[:120]


# ---------------------------------------------------------------- spot leg
def fetch_spot() -> dict:
    """TrendForce public spot page. Fails loud; never carries a stale value."""
    out = {"ddr5_spot_avg": "", "ddr5_chg_pct": "", "ddr4_spot_avg": "",
           "ddr4_chg_pct": "", "spot_asof": ""}
    try:
        import urllib.request
        req = urllib.request.Request(
            SPOT_URL, headers={"User-Agent": "Mozilla/5.0 (VULCAN research instrument)"})
        with urllib.request.urlopen(req, timeout=45) as r:
            html = r.read().decode("utf-8", "replace")
    except Exception as e:                                   # noqa: BLE001
        for k in out:
            out[k] = _err(f"fetch {type(e).__name__}")
        return out

    # as-of comes from the page's own JSON-LD dateModified, before tag-stripping
    m = re.search(r'"dateModified"\s*:\s*"([^"]+)"', html)
    out["spot_asof"] = m.group(1) if m else _err("no-asof")

    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"&#?\w+;", " ", text)          # numeric entities too (▲ is &#9650;)
    text = re.sub(r"\s+", " ", text)

    def grab(product: str) -> tuple[str, str]:
        """
        Row layout on the public tracker is positional:
            <high> <low> <high> <low> <AVERAGE> [arrow] <pct> %
        The session average is therefore index 4 — NOT index 2, which is the
        repeated HIGH and is what an earlier version of this parser returned
        ($67.00 instead of $51.33 on 2026-08-03). A wrong-but-plausible number
        is worse than an error, so the average is VALIDATED against the range
        it must sit inside; any layout change fails LOUD instead of silently
        returning the wrong field.
        """
        m = re.search(re.escape(product), text, re.I)
        if not m:
            return _err("product-miss"), _err("product-miss")
        seg = text[m.end(): m.end() + 200]
        nums = re.findall(r"\d+\.\d+", seg)
        if len(nums) < 5:
            return _err(f"only-{len(nums)}-numbers"), _err("no-pct")
        hi, lo, avg = float(nums[0]), float(nums[1]), float(nums[4])
        if not (lo <= avg <= hi) or hi <= 0:
            # layout drifted — refuse to guess
            return _err(f"avg-{avg}-outside-range-{lo}-{hi}"), _err("unvalidated")
        pct = re.search(r"(-?\d+\.\d+)\s*%", seg)
        return f"{avg:.2f}", (pct.group(1) if pct else _err("no-pct"))

    # anchor on the FULL product string — "DDR5 16Gb" alone also matches the eTT row
    out["ddr5_spot_avg"], out["ddr5_chg_pct"] = grab("DDR5 16Gb (2Gx8) 4800/5600")
    out["ddr4_spot_avg"], out["ddr4_chg_pct"] = grab("DDR4 16Gb (2Gx8) 3200")
    return out


# -------------------------------------------------------------- equity leg
def fetch_cross_section() -> tuple[dict, str]:
    """1-month % change per ticker + group means. Uses the repo venv's yfinance."""
    try:
        import yfinance as yf
    except ImportError:
        return {}, _err("yfinance-missing")
    try:
        df = yf.download(TICKERS, period="1mo", progress=False,
                         auto_adjust=True)["Close"].dropna(how="all")
        if df.empty or len(df) < 5:
            return {}, _err(f"thin-history rows={len(df)}")
        df = df.dropna(axis=1, how="any")
        first, last = df.iloc[0], df.iloc[-1]
        chg = ((last / first - 1.0) * 100).round(2)
        return {"per": {t: float(chg[t]) for t in df.columns},
                "window": f"{df.index[0].date()}->{df.index[-1].date()}"}, ""
    except Exception as e:                                    # noqa: BLE001
        return {}, _err(f"{type(e).__name__} {e}")


def _mean(per: dict, group: list) -> str:
    vals = [per[t] for t in group if t in per]
    return str(round(sum(vals) / len(vals), 2)) if vals else _err("no-members")


# ------------------------------------------------------------------- main
def build_row() -> tuple[dict, int]:
    now = _dt.datetime.now(_dt.timezone.utc)
    row = {c: "" for c in COLUMNS}
    row["asof_utc"] = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    row["trade_date"] = now.strftime("%Y-%m-%d")

    spot = fetch_spot()
    row.update(spot)

    xs, xerr = fetch_cross_section()
    notes = []
    if xerr or not xs:
        for c in ("memory_1mo_pct", "semicap_1mo_pct", "foundry_1mo_pct",
                  "aicompute_1mo_pct", "qqq_1mo_pct", "soxx_1mo_pct",
                  "spread_aicompute_minus_memory_pp", "per_ticker_1mo_pct"):
            row[c] = xerr or _err("no-data")
    else:
        per = xs["per"]
        row["memory_1mo_pct"] = _mean(per, MEMORY)
        row["semicap_1mo_pct"] = _mean(per, SEMICAP)
        row["foundry_1mo_pct"] = _mean(per, FOUNDRY)
        row["aicompute_1mo_pct"] = _mean(per, AICOMPUTE)
        row["qqq_1mo_pct"] = str(per.get("QQQ", _err("missing")))
        row["soxx_1mo_pct"] = str(per.get("SOXX", _err("missing")))
        try:
            row["spread_aicompute_minus_memory_pp"] = str(
                round(float(row["aicompute_1mo_pct"]) - float(row["memory_1mo_pct"]), 2))
        except ValueError:
            row["spread_aicompute_minus_memory_pp"] = _err("uncomputable")
        row["per_ticker_1mo_pct"] = ";".join(f"{t}:{per[t]}" for t in sorted(per))
        notes.append(f"window={xs['window']}")

    n_err = sum(1 for v in row.values() if str(v).startswith("ERR:"))
    if n_err:
        notes.append(f"{n_err}_field_errors")
    row["notes"] = " ".join(notes) if notes else "ok"
    rc = 0 if n_err == 0 else (2 if n_err >= len(COLUMNS) - 3 else 1)
    return row, rc


def append(row: dict) -> None:
    new = not os.path.exists(SERIES)
    os.makedirs(os.path.dirname(SERIES), exist_ok=True)
    with open(SERIES, "a", encoding="utf-8") as f:
        if new:
            f.write("\t".join(COLUMNS) + "\n")
        f.write("\t".join(str(row[c]).replace("\t", " ") for c in COLUMNS) + "\n")


def show(n: int) -> int:
    if not os.path.exists(SERIES):
        print("  no series yet — run without --show to write the first row.")
        return 0
    rows = open(SERIES, encoding="utf-8").read().rstrip("\n").split("\n")
    print(f"  {SERIES}  ({len(rows) - 1} retained rows)")
    hdr = rows[0].split("\t")
    keep = ["trade_date", "ddr5_spot_avg", "ddr4_spot_avg", "memory_1mo_pct",
            "semicap_1mo_pct", "aicompute_1mo_pct", "spread_aicompute_minus_memory_pp"]
    idx = [hdr.index(k) for k in keep if k in hdr]
    print("  " + " | ".join(f"{hdr[i]:>12.12}" for i in idx))
    for line in rows[1:][-n:]:
        c = line.split("\t")
        print("  " + " | ".join(f"{c[i]:>12.12}" if i < len(c) else " " * 12 for i in idx))
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="VULCAN S2 memory-cycle series")
    ap.add_argument("--dry-run", action="store_true", help="print, do not append")
    ap.add_argument("--show", type=int, metavar="N", help="show last N retained rows")
    a = ap.parse_args()

    if a.show is not None:
        return show(a.show)

    print("=" * 72)
    print("  VULCAN semi_watch — S2 memory-cycle series")
    print("=" * 72)
    row, rc = build_row()
    for c in COLUMNS:
        if c == "per_ticker_1mo_pct":
            continue
        flag = "  ⚠️" if str(row[c]).startswith("ERR:") else ""
        print(f"  {c:38} {row[c]}{flag}")
    if row.get("per_ticker_1mo_pct") and not str(row["per_ticker_1mo_pct"]).startswith("ERR:"):
        print(f"  {'per_ticker_1mo_pct':38} {row['per_ticker_1mo_pct']}")

    if a.dry_run:
        print("\n  --dry-run: nothing written.")
    else:
        append(row)
        print(f"\n  appended -> {os.path.relpath(SERIES, AGENT_DIR)}")

    print({0: "  OK — all legs fetched.",
           1: "  PARTIAL — some legs ERR (recorded as ERR:, never blank).",
           2: "  FAILED — nearly all legs ERR; do NOT read this row as data."}[rc])
    return rc


if __name__ == "__main__":
    sys.exit(main())
