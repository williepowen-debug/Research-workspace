#!/usr/bin/env python3
"""
TERRY Snapshot — price/relative-strength context for trade construction.

Purpose: give Terry enough deterministic market context to discuss entries,
levels, relative strength, and data freshness without pretending to have a full
charting terminal or option chain.

Examples:
  python3 AGENTS/TERRY/scripts/snapshot.py WAL KRE --benchmark KRE --days 30 --stress
  python3 AGENTS/TERRY/scripts/snapshot.py TLT FXY --benchmark SPY --days 60
  python3 AGENTS/TERRY/scripts/snapshot.py --selftest

Notes:
- Prices/history come from FORGE/tools/market-data/fetch.py (yfinance wrapper).
- FRED stress values are dated observations, not live prints.
- Option-chain data is NOT fetched here; Terry must use POSITION_INTAKE / chain fields.
"""

from __future__ import annotations

import argparse
import math
import os
import sys
from datetime import datetime
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
TERRY_DIR = SCRIPTS_DIR.parent
WORKSPACE = SCRIPTS_DIR.parents[2]
FETCH_DIR = WORKSPACE / "FORGE" / "tools" / "market-data"
VENV_PY = WORKSPACE / ".venv" / "bin" / "python3"
sys.path.insert(0, str(FETCH_DIR))

# NB: this guard covers a MISSING/BROKEN fetch.py only. It does NOT cover a
# missing yfinance — fetch.py imports yfinance lazily INSIDE its functions, so
# this import succeeds on base python and the dep blows up later, at call time.
# That gap is what _ensure_deps_or_reexec() below exists to close; do not read
# this try/except as covering deps (it was doing exactly that until 2026-07-30).
try:
    from fetch import fred_fetch, price_fetch, price_history
except Exception as e:  # pragma: no cover
    print(f"FATAL: cannot import FORGE market-data fetch.py from {FETCH_DIR}: {e}")
    sys.exit(2)


def _ensure_deps_or_reexec() -> None:
    """venv self-heal — same pattern as paper_book_mark.py / chain_fetch.py.

    Ported 2026-07-30 after a fleet-wide sweep found this script broken on its
    OWN BOOT-documented invocation (CLAUDE.md BOOT step 11, the *preferred*
    path for pulling live prices before citing any level — rule #4).

    Why the try/except above did not catch it: fetch.py imports yfinance lazily
    inside price_fetch/price_history, so `from fetch import ...` succeeds on
    base python and the ModuleNotFoundError surfaces at CALL time as a raw
    traceback. The guard was positioned to catch import failure and the real
    failure was somewhere else entirely — it read as protection while
    protecting nothing (finding_test_the_guard_not_just_the_guarded).

    No safe degraded output exists here: this tool's entire job is returning
    live prices, so when the heal is unavailable it exits NON-ZERO with the fix
    on screen rather than printing anything that could be mistaken for a quote.

    Not called on --selftest: that path needs no yfinance. ⚠️ It is **not fully
    offline** — it ends with a FRED reachability probe — but that probe is
    non-fatal and SKIPS without a credential, so --selftest stays runnable on
    base python and on a clone with no .env. *(Corrected 2026-07-30: this line
    previously claimed the path was "offline", which was simply false — the
    selftest made a live FRED call. Docstring-says-X-but-code-does-Y is the
    exact class I flagged on positions_from_forge.py the same morning.)*
    """
    try:
        import yfinance  # noqa: F401  # deps present -> nothing to do
        return
    except ModuleNotFoundError:
        pass
    # NB: do NOT gate on sys.executable != VENV_PY — the venv's python3 is a
    # symlink to the system python, so .resolve() collapses them and the guard
    # would falsely block re-exec. The env flag is the loop-breaker.
    if not os.environ.get("_SNAP_VENV_REEXEC") and VENV_PY.exists():
        os.environ["_SNAP_VENV_REEXEC"] = "1"
        os.execv(str(VENV_PY), [str(VENV_PY), *sys.argv])
    already = " (re-exec under the venv already tried)" if os.environ.get("_SNAP_VENV_REEXEC") else ""
    print(
        f"FATAL: yfinance is not importable, so NO live price can be fetched{already}.\n"
        f"  Expected venv: {VENV_PY} (exists={VENV_PY.exists()})\n"
        f"  Fix: {VENV_PY} -m pip install yfinance\n"
        "  No prices are printed — do NOT cite any level from this run (rule #4).",
        file=sys.stderr,
    )
    raise SystemExit(2)

DEFAULT_BENCHMARKS = {
    "WAL": "KRE", "OZK": "KRE", "KRE": "SPY", "XLF": "SPY",
    "HYG": "SPY", "JNK": "SPY", "BIZD": "SPY", "APO": "SPY", "ARES": "SPY",
    "TLT": "SPY", "FXY": "SPY", "BZ=F": "USO", "CL=F": "USO",
}

FRED_STRESS = [
    ("BAMLH0A0HYM2", "HY OAS", 100, "bps"),
    ("BAMLH0A3HYC", "CCC OAS", 100, "bps"),
    ("DGS10", "10Y", 1, "%"),
]


def fmt_pct(x):
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return "N/A"
    return f"{x:+.2f}%"


def hist_stats(rows):
    """Rows are chronological from fetch.price_history; compute simple chart stats.

    ⚠️ COVERAGE IS PART OF THE RESULT (added 2026-08-18, WALTER SIG-W-20260813-002).
    Every stat below is an EXTREME or a WINDOW MEAN, and both are corrupted SILENTLY
    by a hole in the series:
      - max()/min() silently EXCLUDE the extreme if its bar is missing,
      - range_loc is derived from that high/low, so a wrong range makes a wrong verdict,
      - ma20/ma50 divide by the SURVIVING count, so the mean is arithmetically right
        while the WINDOW IS MISLABELLED - "20d MA" can span 25 calendar days.
    So we now return n_rows / n_bars / n_nulls / first_date / last_date and let the
    caller refuse to render a verdict it cannot stand behind. We do NOT interpolate
    and we do NOT guess: an unmarkable series is reported UNMARKED, never fabricated.
    """
    if not rows:
        return {}
    n_rows = len(rows)
    usable = [r for r in rows if r.get("close") is not None]
    closes = [float(r["close"]) for r in usable]
    if not closes:
        return dict(n_rows=n_rows, n_bars=0, n_nulls=n_rows)
    first, last = closes[0], closes[-1]
    high, low = max(closes), min(closes)
    ret = ((last - first) / first * 100) if first else None
    # simple location within range: 0=low, 100=high
    loc = ((last - low) / (high - low) * 100) if high != low else 50.0
    ma20 = sum(closes[-20:]) / min(20, len(closes))
    ma50 = sum(closes[-50:]) / min(50, len(closes))
    return dict(first=first, last=last, high=high, low=low, return_pct=ret, range_loc=loc,
                ma20=ma20, ma50=ma50,
                n_rows=n_rows, n_bars=len(closes), n_nulls=n_rows - len(closes),
                first_date=usable[0].get("date"), last_date=usable[-1].get("date"))


# --- Coverage guard -------------------------------------------------------
# 🔴 THE DEFECT THIS EXISTS FOR, reproduced on this box 2026-08-18:
# two IDENTICAL price_history() calls seconds apart returned ^TNX with 18 bars and
# then 60 bars (IEF: 59 then 60) for the same 60-day request. The short pull carries
# NO nulls - the bars are simply ABSENT - so a `close is None` check cannot see it.
# Consequence on a live card: the full 60-bar 10Y series has min 4.37; the truncated
# 18-bar window has min 4.60. A "has the 10Y closed below 4.50?" read off the short
# series returns NO with full confidence. TRY-FIRE-004's disarm line is 10Y < 4.50.
# (Registered grading is FRED DGS10, a different fetch path, so the GATE is insulated
# - the exposure is every range/extreme/sustain read taken off the yfinance path.)
#
# METHOD: THE BATCH IS ITS OWN CONTROL. Comparing bar counts across tickers in one
# pull needs no holiday calendar and no per-symbol expectation - it directly catches
# "one symbol came back short." An absolute floor backstops single-ticker pulls.
SHORT_REL = 0.90   # short if under 90% of the best-covered ticker in the same pull
SHORT_ABS = 0.80   # short if under 80% of the trading days the lookback implies


def coverage_flags(histories, days):
    """Return {ticker: (n_bars, n_nulls, flag)}. flag: '' | 'SHORT' | 'NULLS' | 'NONE'."""
    stats = {}
    for tk, h in histories.items():
        rows = (h or {}).get("history") or []
        st = hist_stats(rows)
        stats[tk] = (st.get("n_bars", 0), st.get("n_nulls", 0))
    if not stats:
        return {}
    best = max((b for b, _ in stats.values()), default=0)
    implied = max(1, int(round(days * 252.0 / 365.0)))
    out = {}
    for tk, (bars, nulls) in stats.items():
        if bars == 0:
            flag = "NONE"
        elif (best and bars < SHORT_REL * best) or bars < SHORT_ABS * implied:
            flag = "SHORT"
        elif nulls:
            flag = "NULLS"
        else:
            flag = ""
        out[tk] = (bars, nulls, flag)
    return out


def marker_for_location(loc):
    if loc is None:
        return "?"
    if loc >= 80:
        return "near range high"
    if loc <= 20:
        return "near range low"
    return "mid-range"


def stress_rows():
    out = []
    for sid, label, mult, unit in FRED_STRESS:
        obs = fred_fetch(sid, limit=2)
        if not obs or "error" in obs[0]:
            out.append((label, "ERR", "", obs[0].get("error", "no data") if obs else "no data"))
            continue
        try:
            val = float(obs[0]["value"]) * mult
            disp = f"{val:.0f}{unit}" if unit == "bps" else f"{val:.2f}{unit}"
        except Exception:
            disp = str(obs[0].get("value"))
        out.append((label, disp, obs[0]["date"], "FRED observation date"))
    return out


def run(args):
    tickers = [t.upper() for t in args.tickers]
    if not tickers:
        print("No tickers supplied. Try: snapshot.py WAL KRE --benchmark KRE")
        return 1

    benchmark = (args.benchmark or DEFAULT_BENCHMARKS.get(tickers[0]) or "SPY").upper()
    fetch_tickers = sorted(set(tickers + [benchmark]))

    print(f"TERRY snapshot — {datetime.now().strftime('%Y-%m-%d %H:%M local')}")
    print(f"Tickers: {', '.join(tickers)} | Benchmark: {benchmark} | Lookback: {args.days}d")
    print("Data: yfinance via FORGE fetch.py; option-chain NOT included.\n")

    prices = price_fetch(fetch_tickers)
    histories = price_history(fetch_tickers, days=args.days)
    bench_stats = hist_stats(histories.get(benchmark, {}).get("history", []))
    bench_ret = bench_stats.get("return_pct")
    cov = coverage_flags(histories, args.days)

    # Printed ALWAYS, not only on defect: a check that speaks only on failure trains
    # the reader to treat silence as health. Coverage is stated so it can be reviewed.
    implied = max(1, int(round(args.days * 252.0 / 365.0)))
    bad = {t: v for t, v in cov.items() if v[2]}
    line = "  ".join(f"{t}:{v[0]}" + (f"/{v[2]}" if v[2] else "") for t, v in sorted(cov.items()))
    print(f"DATA COVERAGE (bars returned; ~{implied} trading days implied by {args.days}d)")
    print(f"  {line}")
    if bad:
        print("  \u26a0 SHORT/NULL SERIES — range, extremes and MA verdicts are SUPPRESSED for these.")
        print("    Non-deterministic truncation is a KNOWN live defect (WALTER SIG-W-20260813-002;")
        print("    reproduced here 2026-08-18: ^TNX 18 bars then 60 on identical back-to-back calls).")
        print("    RE-RUN before citing any level off an affected symbol. Do NOT interpolate.")
    print()

    print("PRICE / TAPE")
    print("Ticker     Price      Day chg   Lookback  Rel vs bench   Range loc     Key range")
    print("---------  ---------  --------  --------  -------------  ------------  ----------------")
    for t in tickers:
        p = prices.get(t, {})
        h = histories.get(t, {})
        if "error" in p or "error" in h:
            print(f"{t:<9}  ERROR     {str(p.get('error') or h.get('error'))[:70]}")
            continue
        st = hist_stats(h.get("history", []))
        ret = st.get("return_pct")
        rel = (ret - bench_ret) if ret is not None and bench_ret is not None and t != benchmark else None
        loc = st.get("range_loc")
        range_txt = f"{st.get('low', 0):.2f}–{st.get('high', 0):.2f}" if st else "N/A"
        # SUPPRESS the derived verdicts on a short/holed series rather than print a
        # confident wrong one. The PRICE is still fine (a separate live quote call);
        # it is the range-derived reads that the missing bars corrupt.
        tflag = cov.get(t, (0, 0, ""))[2]
        if tflag:
            loc = None
            range_txt = f"[{tflag} {cov.get(t, (0,))[0]}b]"
        price = p.get("price")
        price_txt = f"{price:.2f}" if isinstance(price, (int, float)) else "N/A"
        day = fmt_pct(p.get("change_pct"))
        print(f"{t:<9}  {price_txt:>9}  {day:>8}  {fmt_pct(ret):>8}  {fmt_pct(rel):>13}  {marker_for_location(loc):<12}  {range_txt}")

    if benchmark not in tickers:
        st = bench_stats
        print(f"\nBenchmark {benchmark}: {fmt_pct(bench_ret)} over {args.days}d; range {st.get('low', 0):.2f}–{st.get('high', 0):.2f}" if st else f"\nBenchmark {benchmark}: unavailable")

    print("\nTERRY READ PROMPTS")
    print("- Entry quality: avoid chasing if price is near range extreme without fresh catalyst.")
    print("- Invalidation: use nearby support/resistance or thesis/tape break; do not hide behind macro narrative.")
    print("- Options: chain still required (bid/ask, OI/volume, IV, delta, theta, expected move).")

    if args.stress:
        print("\nCREDIT / RATES BACKDROP")
        for label, val, d, note in stress_rows():
            print(f"- {label}: {val}" + (f" [{d}]" if d else "") + f" — {note}")
    return 0


def _fred_credential_present() -> bool:
    """Is a FRED key discoverable at all? (shell env, or the unversioned .env
    that FORGE fetch.py loads for itself). Used to tell 'no credential here'
    apart from 'credential present and the call is broken' — different verdicts."""
    if os.environ.get("FRED_API_KEY"):
        return True
    try:
        return "FRED_API_KEY" in (WORKSPACE / ".env").read_text()
    except OSError:
        return False


def selftest():
    """Offline structural checks ALWAYS; the FRED probe is separate and SKIPS
    when no credential exists.

    ⚠️ **FIXED 2026-07-30 (RAV review).** This was a single `assert` on a **live**
    `fred_fetch()` call, so `--selftest` silently depended on **network + an
    UNVERSIONED, machine-local credential** (`.env`). It passed on this desktop
    and died with a bare `AssertionError: FRED selftest failed: HTTP Error 400`
    on a clone without the key — **a code-correctness check failing for reasons
    that have nothing to do with the code.** Under serial multi-machine that
    means the laptop can report a perfectly good tool as broken, and the
    argparse help ("Validate imports/FRED access") contradicted the docstring I
    had just written claiming this path was offline.
    (`finding_unversioned_local_secret_fails_silently`.)

    Three outcomes now, and the middle one is the point:
      · structural failure                  -> FAIL (real defect)
      · FRED unreachable, NO credential     -> SKIP (environment, not a defect)
      · FRED unreachable, credential PRESENT-> FAIL (real defect)
    """
    assert FETCH_DIR.exists(), f"missing fetch dir: {FETCH_DIR}"
    assert (FETCH_DIR / "fetch.py").exists(), "missing fetch.py"
    for fn in (fred_fetch, price_fetch, price_history):
        assert callable(fn), f"imported symbol not callable: {fn!r}"
    print("snapshot.py SELFTEST: PASS (offline structural — imports + fetch.py reachable)")

    have_key = _fred_credential_present()
    try:
        rows = fred_fetch("BAMLH0A0HYM2", limit=1)
        ok = bool(rows) and "error" not in rows[0]
    except Exception as e:  # network down, DNS, etc.
        rows, ok = [{"error": repr(e)}], False

    if ok:
        print("  FRED probe: ✓ reachable")
        return 0
    if not have_key:
        print("  FRED probe: ⏭ SKIPPED — no FRED_API_KEY in env or .env. "
              "NOT a code defect; --stress will print ERR rows on this machine "
              "and NO stress value may be cited from it (rule #4).")
        return 0
    print(f"  FRED probe: 🔴 FAIL — a credential IS present but the call errored: {rows}",
          file=sys.stderr)
    return 1


def main():
    ap = argparse.ArgumentParser(description="TERRY price/relative-strength snapshot")
    ap.add_argument("tickers", nargs="*", help="Tickers/instruments, e.g. WAL KRE TLT")
    ap.add_argument("--benchmark", "-b", help="Relative-strength benchmark (default inferred, often SPY/KRE)")
    ap.add_argument("--days", type=int, default=30, help="Lookback days for simple range/return stats")
    ap.add_argument("--stress", action="store_true", help="Include HY/CCC/10Y FRED backdrop")
    ap.add_argument("--selftest", action="store_true",
                    help="Offline structural check (always) + a FRED reachability probe that SKIPS without a credential")
    args = ap.parse_args()
    if args.selftest:
        return selftest()      # structural part is offline; FRED probe is non-fatal without a key
    _ensure_deps_or_reexec()   # venv self-heal before ANY live price fetch
    return run(args)


if __name__ == "__main__":
    raise SystemExit(main())
