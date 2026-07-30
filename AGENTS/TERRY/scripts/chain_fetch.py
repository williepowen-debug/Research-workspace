#!/usr/bin/env python3
"""
TERRY Live Option-Chain Fetcher.

Pulls a live option chain (yfinance) and prints strike/bid/ask/mark/spread%/IV/
volume/OI plus a moneyness column, filtered to a window around spot. Output
columns MIRROR chain_parse.py so a fetched chain and a pasted broker chain look
identical to downstream trade-card workflows.

This is data only. It does NOT recommend or execute trades. Every actionable
output still requires Will approval (RISK_SCORING.md).

Examples:
  python3 AGENTS/TERRY/scripts/chain_fetch.py TLT                       # list expiries, exit
  python3 AGENTS/TERRY/scripts/chain_fetch.py TLT 2027-03-19 --type put
  python3 AGENTS/TERRY/scripts/chain_fetch.py WAL 2026-09-18 --type put --window 0.20
  python3 AGENTS/TERRY/scripts/chain_fetch.py TLT 2027-03-19 --type put --json --no-cache
  python3 AGENTS/TERRY/scripts/chain_fetch.py --selftest

Notes / known limits (READ THESE — rule #4, finding_option_marks_need_live_chain):
- yfinance provides IV but NOT delta/theta (greeks absent) -> those columns are N/A.
- Option marks go stale after-hours / weekends. Output stamps the fetch time, the
  spot as-of, and each row's lastTradeDate, and WARNS when the freshest trade in
  the displayed set is not "today". Re-confirm live broker marks before any fill.
- Short ~120s cache by default; use --no-cache at fire-time for a guaranteed live pull.
- yfinance lives in the repo market-data venv, not base python. This script
  SELF-HEALS (re-execs under .venv) so the bare `python3 ...` invocations above
  and in CLAUDE.md BOOT 11-13 work as documented. If the venv is missing it
  fails LOUD with the fix, never a raw ModuleNotFoundError traceback.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
CACHE_DIR = SCRIPTS_DIR / ".cache"
CACHE_TTL = 120  # seconds; chains move — short TTL, bypass with --no-cache
VENV_PY = SCRIPTS_DIR.parents[2] / ".venv" / "bin" / "python3"


def _ensure_deps_or_reexec() -> None:
    """venv self-heal — same pattern as paper_book_mark.py's _ensure_deps_or_reexec
    (adopted 2026-07-20), ported here 2026-07-30 after a bare
    `python3 ... chain_fetch.py TLT 2026-09-30 --type put` died on
    ModuleNotFoundError: yfinance at a live desk boot.

    yfinance lives in the repo market-data venv, not base python, so every
    invocation form documented in this file's own Examples block and in
    CLAUDE.md BOOT 11-13 was broken. If deps are missing AND the venv exists,
    re-exec this same command under it so the pull 'just works' regardless of
    how it was invoked.

    DIVERGENCE FROM paper_book_mark.py, deliberate: that tool degrades to
    UNMARKED when the self-heal cannot run, because a missing mark is a valid
    (and safe) output for a shadow book. This tool has no safe degraded output
    — it exists only to return live marks — so when the heal is unavailable it
    exits NON-ZERO with the fix on screen. A fire-time tool must never fail as
    a raw traceback, and must never return anything a caller could mistake for
    a chain (finding_fail_loud_on_incomplete_data; RISK_RULES Non-Negotiable #3).

    Not called on --selftest: that path is fully offline and never imports
    yfinance, so it stays runnable on base python.
    """
    try:
        import yfinance  # noqa: F401  # deps present -> nothing to do
        return
    except ModuleNotFoundError:
        pass
    # NB: do NOT gate on sys.executable != VENV_PY — the venv's python3 is a
    # symlink to the system python, so .resolve() collapses them and the guard
    # would falsely block re-exec. The env flag is the loop-breaker.
    if not os.environ.get("_CF_VENV_REEXEC") and VENV_PY.exists():
        os.environ["_CF_VENV_REEXEC"] = "1"
        os.execv(str(VENV_PY), [str(VENV_PY), *sys.argv])
    already = " (re-exec under the venv already tried)" if os.environ.get("_CF_VENV_REEXEC") else ""
    print(
        f"FATAL: yfinance is not importable, so NO live chain can be fetched{already}.\n"
        f"  Expected venv: {VENV_PY} (exists={VENV_PY.exists()})\n"
        f"  Fix: {VENV_PY} -m pip install yfinance\n"
        "  No chain is printed and no marks are emitted — re-confirm broker marks "
        "directly before any fill (rule #4).",
        file=sys.stderr,
    )
    raise SystemExit(2)


# ---------------------------------------------------------------------------
# Cache (mirrors fetch.py's tiny json-file pattern)
# ---------------------------------------------------------------------------

def _cache_path(key):
    CACHE_DIR.mkdir(exist_ok=True)
    safe = key.replace("/", "_").replace("^", "_").replace("=", "_").replace(":", "_")
    return CACHE_DIR / f"chain_{safe}.json"


def _cache_get(key):
    p = _cache_path(key)
    if not p.exists():
        return None
    try:
        data = json.loads(p.read_text())
    except (json.JSONDecodeError, OSError):
        return None
    if time.time() - data.get("ts", 0) > CACHE_TTL:
        return None
    return data.get("val")


def _cache_set(key, val):
    try:
        _cache_path(key).write_text(json.dumps({"ts": time.time(), "val": val}))
    except OSError:
        pass


# ---------------------------------------------------------------------------
# Fetch
# ---------------------------------------------------------------------------

def fetch_spot(ticker):
    """Live spot via yfinance fast_info (same source as fetch.py)."""
    import yfinance as yf
    tk = yf.Ticker(ticker)
    info = tk.fast_info
    return float(info["lastPrice"])


def list_expiries(ticker):
    import yfinance as yf
    return list(yf.Ticker(ticker).options or [])


def fetch_chain(ticker, expiry, opt_type):
    """Return (rows, meta). rows = list of dicts mirroring chain_parse.py schema.
    opt_type in {'put','call', None}. Greeks (delta/theta) are unavailable from
    yfinance and are emitted as None."""
    import yfinance as yf
    tk = yf.Ticker(ticker)
    chain = tk.option_chain(expiry)

    frames = []
    if opt_type in (None, "put"):
        frames.append(("P", chain.puts))
    if opt_type in (None, "call"):
        frames.append(("C", chain.calls))

    rows = []
    latest_trade = None
    for tletter, df in frames:
        for _, r in df.iterrows():
            bid = _f(r.get("bid"))
            ask = _f(r.get("ask"))
            last = _f(r.get("lastPrice"))
            mark = (bid + ask) / 2 if (bid is not None and ask is not None) else None
            spread = (ask - bid) if (bid is not None and ask is not None) else None
            spread_pct = (spread / mark * 100) if (spread is not None and mark) else None
            iv = _f(r.get("impliedVolatility"))
            iv_pct = iv * 100 if iv is not None else None  # yfinance IV is a fraction
            ltd = r.get("lastTradeDate")
            ltd_str = _ts_str(ltd)
            if ltd_str and (latest_trade is None or ltd_str > latest_trade):
                latest_trade = ltd_str
            rows.append({
                "strike": _f(r.get("strike")),
                "type": tletter,
                "expiry": expiry,
                "bid": bid, "ask": ask, "mark": mark, "last": last,
                "delta": None, "theta": None,            # yfinance does not provide greeks
                "iv": round(iv_pct, 2) if iv_pct is not None else None,
                "volume": _f(r.get("volume")),
                "open_interest": _f(r.get("openInterest")),
                "spread_pct": round(spread_pct, 2) if spread_pct is not None else None,
                "last_trade": ltd_str,
                "in_the_money": bool(r.get("inTheMoney")) if r.get("inTheMoney") is not None else None,
            })
    meta = {"latest_trade": latest_trade}
    return rows, meta


def _f(x):
    if x is None:
        return None
    try:
        v = float(x)
        if v != v:  # NaN
            return None
        return v
    except (TypeError, ValueError):
        return None


def _ts_str(x):
    """Normalize a pandas/py datetime to **LOCAL** 'YYYY-MM-DD HH:MM' or None.

    ⚠️ **TZ BUG FIXED 2026-07-30 (RAV review).** yfinance returns `lastTradeDate`
    **tz-aware in UTC**. This formatted it directly, which printed UTC wall-clock
    **unlabeled, beside a LOCAL fetch stamp** — so output read
    `freshest trade 17:08 (fetch 14:51)`, i.e. a trade in the *future*.

    Cosmetic only until you follow it into `run()`: the freshness check does
    `latest.startswith(today)` where **`today` is LOCAL**. Comparing a
    UTC-derived date against a local date means that **between ~20:00 ET and
    midnight the UTC date is already tomorrow**, so a trade that happened
    **today** fails the check and fires a spurious *"NOT today — marks may be
    stale"* warning. That is a **fire-time freshness guard misfiring in the
    evening**, and a staleness alarm that cries wolf on the normal state stops
    being read — the same failure PB-0004's mark_asof had.

    Converting to local **here** fixes display and comparison in one place,
    because everything downstream consumes this function's output.
    """
    if x is None:
        return None
    try:
        if hasattr(x, "strftime"):
            # ⚠️ yfinance hands back a pandas.Timestamp, NOT a datetime, and
            # pandas.Timestamp.astimezone() requires a tz argument — calling it
            # bare raises TypeError('tz_convert() takes exactly 2 positional
            # arguments'). That was swallowed by the except below and every
            # timestamp silently became N/A. Normalize to a plain datetime
            # FIRST, then convert. (Caught by regression on the live path; my
            # first selftest stub used a bare datetime and so never exercised
            # the real type — finding_test_the_guard_not_just_the_guarded.)
            if hasattr(x, "to_pydatetime"):
                x = x.to_pydatetime()
            # tz-aware (yfinance UTC) -> local; naive values pass through as-is
            if getattr(x, "tzinfo", None) is not None:
                x = x.astimezone()
            return x.strftime("%Y-%m-%d %H:%M")
        return str(x)[:16]
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Filter + display
# ---------------------------------------------------------------------------

def apply_window(rows, spot, window, min_oi):
    if spot and window:
        lo, hi = spot * (1 - window), spot * (1 + window)
        rows = [r for r in rows if r["strike"] is not None and lo <= r["strike"] <= hi]
    if min_oi is not None:
        rows = [r for r in rows if (r["open_interest"] or 0) >= min_oi]
    return sorted(rows, key=lambda r: (r["type"], r["strike"] if r["strike"] is not None else 0))


def add_moneyness(rows, spot):
    for r in rows:
        if spot and r["strike"] is not None:
            r["moneyness_pct"] = round((r["strike"] - spot) / spot * 100, 1)
        else:
            r["moneyness_pct"] = None
    return rows


def fmt(x, dp=2):
    return "N/A" if x is None else f"{x:.{dp}f}"


def display(ticker, expiry, opt_type, spot, spot_asof, rows, meta, wide_pct, thin_oi):
    today = datetime.now().strftime("%Y-%m-%d")
    print("TERRY live option-chain fetch")
    print("=============================")
    print("Data only — no broker access, no execution recommendation.\n")
    print(f"Underlying: {ticker}  Spot: {fmt(spot)} (as-of {spot_asof})")
    print(f"Expiry: {expiry}  Type: {opt_type or 'all'}  Rows: {len(rows)}")
    print("Greeks (Delta/Theta): N/A — yfinance does not provide them.\n")
    print("Strike   Mny%    T  Bid    Ask    Mark   Sprd%   IV%     Vol    OI     LastTrade")
    print("-------  ------  -  -----  -----  -----  ------  ------  -----  -----  ----------------")
    wide = []
    thin = []
    for r in rows:
        if r["spread_pct"] is not None and r["spread_pct"] > wide_pct:
            wide.append(r)
        if (r["open_interest"] or 0) < thin_oi:
            thin.append(r)
        print(f"{fmt(r['strike']):>7}  {fmt(r.get('moneyness_pct'),1):>6}  {r['type']:<1}  "
              f"{fmt(r['bid']):>5}  {fmt(r['ask']):>5}  {fmt(r['mark']):>5}  "
              f"{fmt(r['spread_pct']):>6}  {fmt(r['iv']):>6}  "
              f"{fmt(r['volume'],0):>5}  {fmt(r['open_interest'],0):>5}  {r.get('last_trade') or 'N/A'}")
    print("\nTERRY liquidity flags")
    print(f"- Wide spread rows >{wide_pct:.0f}% of mark: {len(wide)}")
    print(f"- Thin OI rows <{thin_oi:.0f} OI: {len(thin)}")
    # Freshness guard (rule #4)
    latest = meta.get("latest_trade")
    if latest and not latest.startswith(today):
        print(f"\n⚠️  FRESHNESS: freshest trade in set = {latest} (NOT today {today}). "
              f"Marks may be stale (after-hours/weekend). Re-confirm live broker marks before any fill.")
    else:
        print(f"\nFreshness: freshest trade in set = {latest or 'N/A'} (fetch {datetime.now().strftime('%Y-%m-%d %H:%M')}).")
    print("Trade-card reminder: feed these into a fire card's LIVE-MARKS block; execution still requires Will approval.")


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

def run(args):
    ticker = args.ticker.upper()
    opt_type = ({"c": "call", "p": "put"}.get(args.type, args.type)) if args.type else None

    if not args.expiry:
        exps = list_expiries(ticker)
        if args.json:
            print(json.dumps({"ticker": ticker, "expiries": exps}, indent=2))
        else:
            print(f"{ticker} available expiries ({len(exps)}):")
            for e in exps:
                print(f"  {e}")
            print("\nRe-run with an expiry, e.g.:")
            print(f"  python3 {Path(__file__).name} {ticker} {exps[0] if exps else 'YYYY-MM-DD'} --type put")
        return 0

    cache_key = f"{ticker}_{args.expiry}_{opt_type or 'all'}"
    cached = None if args.no_cache else _cache_get(cache_key)
    if cached:
        spot = cached["spot"]
        spot_asof = cached["spot_asof"] + " (cached)"
        rows = cached["rows"]
        meta = cached["meta"]
    else:
        spot = args.spot if args.spot is not None else fetch_spot(ticker)
        spot_asof = datetime.now().strftime("%Y-%m-%d %H:%M")
        rows, meta = fetch_chain(ticker, args.expiry, opt_type)
        _cache_set(cache_key, {"spot": spot, "spot_asof": spot_asof, "rows": rows, "meta": meta})

    rows = add_moneyness(rows, spot)
    rows = apply_window(rows, spot, args.window, args.min_oi)
    if args.limit:
        rows = rows[: args.limit]

    if args.json:
        print(json.dumps({
            "ticker": ticker, "expiry": args.expiry, "type": opt_type,
            "spot": spot, "spot_asof": spot_asof, "fetch_ts": datetime.now().isoformat(),
            "latest_trade": meta.get("latest_trade"), "rows": rows,
        }, indent=2))
    else:
        display(ticker, args.expiry, opt_type, spot, spot_asof, rows, meta,
                args.wide_spread_pct, args.thin_oi)
    return 0


# ---------------------------------------------------------------------------
# Self-test (offline — no network)
# ---------------------------------------------------------------------------

def selftest():
    # Offline stub mirroring yfinance option_chain().puts row shape.
    stub = [
        {"strike": 80.0, "bid": 0.78, "ask": 0.82, "lastPrice": 0.80, "impliedVolatility": 0.105,
         "volume": 120, "openInterest": 38245, "inTheMoney": False,
         "lastTradeDate": datetime(2027, 1, 4, 15, 30, tzinfo=timezone.utc)},
        {"strike": 85.0, "bid": 2.12, "ask": 2.17, "lastPrice": 2.15, "impliedVolatility": 0.108,
         "volume": 60, "openInterest": 502, "inTheMoney": False,
         "lastTradeDate": datetime(2027, 1, 4, 15, 31, tzinfo=timezone.utc)},
    ]

    # Inline the per-row transform (mirror of fetch_chain's body) so the test is network-free.
    rows = []
    latest_trade = None
    for r in stub:
        bid, ask, last = _f(r["bid"]), _f(r["ask"]), _f(r["lastPrice"])
        mark = (bid + ask) / 2
        spread_pct = (ask - bid) / mark * 100
        iv_pct = _f(r["impliedVolatility"]) * 100
        ltd = _ts_str(r["lastTradeDate"])
        if ltd and (latest_trade is None or ltd > latest_trade):
            latest_trade = ltd
        rows.append({
            "strike": _f(r["strike"]), "type": "P", "expiry": "2027-03-19",
            "bid": bid, "ask": ask, "mark": mark, "last": last,
            "delta": None, "theta": None, "iv": round(iv_pct, 2),
            "volume": _f(r["volume"]), "open_interest": _f(r["openInterest"]),
            "spread_pct": round(spread_pct, 2), "last_trade": ltd,
        })

    spot = 87.21
    rows = add_moneyness(rows, spot)
    rows = apply_window(rows, spot, 0.15, None)

    assert len(rows) == 2, f"expected 2 rows, got {len(rows)}"
    assert rows[0]["mark"] == 0.80, rows[0]["mark"]
    assert rows[0]["delta"] is None and rows[0]["theta"] is None, "greeks must be N/A"
    assert rows[0]["iv"] == 10.50, rows[0]["iv"]            # 0.105 -> 10.50%
    assert round(rows[1]["spread_pct"], 2) == 2.33, rows[1]["spread_pct"]  # (2.17-2.12)/2.145
    assert rows[0]["moneyness_pct"] == round((80 - 87.21) / 87.21 * 100, 1), rows[0]["moneyness_pct"]
    # window ±15% of 87.21 = [74.13, 100.29] keeps both 80 & 85
    assert all(74.13 <= r["strike"] <= 100.29 for r in rows)
    # TZ GUARD (RAV 2026-07-30): stub lastTradeDate is tz-aware UTC 15:30/15:31.
    # _ts_str must convert to LOCAL, or the freshness check compares a UTC date
    # against a local `today` and misfires in the evening. Assert the conversion
    # actually happened rather than trusting the docstring — this is the guard
    # that would have caught the bug (finding_test_the_guard_not_just_the_guarded).
    # ★ DETERMINISTIC tz proof (RAV 2026-07-30). The _local() helper below calls the
    # SAME astimezone() as the code under test, so on a UTC-configured box its
    # assertions pass even if the conversion were a NO-OP — a tautology, and the
    # 5th "guard aimed slightly off its target" of the day, inside the very test
    # written to close the 4th. Pin a KNOWN non-UTC zone so the conversion is
    # provable by wall-clock on ANY box. 2027-01-04 is EST (UTC-5), no DST ambiguity.
    if hasattr(time, "tzset"):
        _tz_before = os.environ.get("TZ")
        try:
            os.environ["TZ"] = "America/New_York"
            time.tzset()
            _got = _ts_str(datetime(2027, 1, 4, 15, 30, tzinfo=timezone.utc))
            assert _got == "2027-01-04 10:30", (
                f"UTC->local conversion NOT applied (pinned America/New_York): got {_got}, want 2027-01-04 10:30")
            _naive = datetime(2027, 1, 4, 15, 30, tzinfo=timezone.utc).strftime("%Y-%m-%d %H:%M")
            assert _got != _naive, "conversion produced the naive UTC render — the original bug"
        finally:
            if _tz_before is None:
                os.environ.pop("TZ", None)
            else:
                os.environ["TZ"] = _tz_before
            time.tzset()
    else:
        print("  ⚠️  time.tzset() unavailable — tz conversion proven only against this box's local zone")

    def _local(h, m):
        return datetime(2027, 1, 4, h, m, tzinfo=timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M")
    assert rows[0]["last_trade"] == _local(15, 30), (
        f"lastTradeDate not converted to local: got {rows[0]['last_trade']}, want {_local(15, 30)}")
    assert latest_trade == _local(15, 31), (
        f"latest_trade must be the local-converted max: got {latest_trade}, want {_local(15, 31)}")
    # ★ Exercise the REAL type. yfinance yields pandas.Timestamp, whose
    # .astimezone() raises bare — the stub above is a plain datetime and passed
    # while the live path silently returned N/A for every timestamp. Skipped
    # (loudly) when pandas is absent, since --selftest must run on base python.
    try:
        import pandas as pd
    except ModuleNotFoundError:
        print("  ⚠️  pandas absent — pandas.Timestamp tz path NOT exercised "
              "(run under .venv to cover it)")
    else:
        _pts = _ts_str(pd.Timestamp("2027-01-04 15:30", tz="UTC"))
        assert _pts == _local(15, 30), (
            f"pandas.Timestamp not converted to local: got {_pts}, want {_local(15, 30)}")
        assert _ts_str(pd.Timestamp("2027-01-04 15:30")) == "2027-01-04 15:30", \
            "tz-naive Timestamp must pass through unchanged"
    print("chain_fetch.py SELFTEST: PASS")
    print(f"  rows={len(rows)} mark0={rows[0]['mark']} iv0={rows[0]['iv']}% "
          f"spread1={rows[1]['spread_pct']}% mny0={rows[0]['moneyness_pct']}% greeks=N/A latest_trade={latest_trade}")
    return 0


def main():
    ap = argparse.ArgumentParser(description="TERRY live option-chain fetcher (yfinance)")
    ap.add_argument("ticker", nargs="?", help="underlying ticker, e.g. TLT")
    ap.add_argument("expiry", nargs="?", help="expiry YYYY-MM-DD; omit to list available expiries")
    ap.add_argument("--type", choices=["put", "call", "p", "c"], help="filter to puts or calls")
    ap.add_argument("--window", type=float, default=0.15, help="±fraction of spot to keep (default 0.15)")
    ap.add_argument("--spot", type=float, help="override live spot (for moneyness)")
    ap.add_argument("--min-oi", type=float, help="drop rows below this open interest")
    ap.add_argument("--limit", type=int, default=0, help="cap displayed rows (0 = no cap)")
    ap.add_argument("--wide-spread-pct", type=float, default=15.0)
    ap.add_argument("--thin-oi", type=float, default=100.0)
    ap.add_argument("--no-cache", action="store_true", help="force a live pull (fire-time)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()          # offline — stays runnable on base python
    if not args.ticker:
        ap.error("ticker required unless --selftest")
    _ensure_deps_or_reexec()       # venv self-heal before ANY live fetch
    return run(args)


if __name__ == "__main__":
    raise SystemExit(main())
