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


# ---------------------------------------------------------------------------
# Quote sanity (added 2026-08-04)
# ---------------------------------------------------------------------------

# Flag codes, terse enough for a table column.
FLAG_LOCK    = "LOCK"    # bid == ask, both > 0 — a locked market cannot persist in a real book
FLAG_XSD     = "XSD"     # bid > ask — crossed, definitionally broken
FLAG_DEAD    = "DEAD"    # bid == 0 and ask == 0 — no market at all
FLAG_NOBID   = "NOBID"   # bid == 0, ask > 0 — you cannot SELL this leg at any price
FLAG_NONMONO = "NONMONO" # violates strike monotonicity vs an adjacent same-type strike
FLAG_DIRINC  = "DIRINC"  # mark moved OPPOSITE the printed spot between two --no-cache pulls

# Defects that make a row unusable for computing a net debit. NONMONO is
# deliberately NOT here — see the docstring below.
HARD_FLAGS = {FLAG_LOCK, FLAG_XSD, FLAG_DEAD, FLAG_NOBID}

# ⛔ DIRINC is deliberately NOT in HARD_FLAGS, and the reason is the same one that keeps
# NONMONO advisory. Every member of HARD_FLAGS is a DEFINITIONALLY BROKEN quote — locked,
# crossed, dead, or unsellable. You cannot transact it, full stop. DIRINC is different in
# kind: it is EVIDENCE that the quote reflects an older market state, not proof the quote
# is unusable, and a long option's mark can legitimately fall while spot rises if IV drops
# enough. Making it fatal would mean one ordinary vol move blocks a fire, and the cheapest
# remedy would be "pull again until it passes" — a guard whose cheapest remedy is a bad
# action buys nothing (the CHECK I lesson in ledger_sweep.py, applied here).
# ⛔ AND THE DEEPER REASON: a flag cannot recover the true bid. See STALE-QUOTE DOCTRINE
# in display() — the real fix is where the fire-time price comes FROM, not a louder tool.


WATCH_PATH = CACHE_DIR / "quote_watch.json"
DIRINC_SPOT_NOISE_FLOOR = 0.0005   # 0.05% of spot — below this a spot "move" is tick noise


def _watch_load():
    try:
        return json.loads(WATCH_PATH.read_text())
    except Exception:
        return {}


def _watch_save(d):
    try:
        CACHE_DIR.mkdir(exist_ok=True)
        WATCH_PATH.write_text(json.dumps(d))
    except Exception:
        pass   # a broken observation store must never break a quote pull


def _watch_key(ticker, expiry, r):
    return f"{ticker}|{expiry}|{r['type']}|{r['strike']}"


def add_direction_flags(rows, ticker, expiry, spot):
    """Compare this pull against the LAST --no-cache pull of the same contract.

    A long call's mark must not fall while spot rises (and a put's must not rise);
    delta has a sign. When it does, the bid/ask is reflecting an older market state
    than the printed spot. This exists because yfinance furnishes NO bid/ask
    timestamp at all — only `lastTradeDate`, which is the last EXECUTED TRADE, a
    different quantity that can be fresh while the quote is stale. Arithmetic on
    successive pulls is the ONLY staleness signal available.

    ⚠️ Fires from the SECOND --no-cache pull of a contract onward. A first-ever pull
    has nothing to compare against and will show clean — stated, not hidden.
    """
    if spot is None:
        return rows, []
    watch = _watch_load()
    hits, updated = [], dict(watch)
    for r in rows:
        if r["mark"] is None or r["strike"] is None:
            continue
        key = _watch_key(ticker, expiry, r)
        prev = watch.get(key)
        updated[key] = {"ts": datetime.now().isoformat(), "spot": spot, "mark": r["mark"]}
        if not prev or prev.get("spot") is None or prev.get("mark") is None:
            continue
        d_spot = spot - prev["spot"]
        d_mark = r["mark"] - prev["mark"]
        if abs(d_spot) <= abs(spot) * DIRINC_SPOT_NOISE_FLOOR or d_mark == 0:
            continue
        want = (1 if d_spot > 0 else -1) * (1 if r["type"] == "C" else -1)
        got = 1 if d_mark > 0 else -1
        if want != got:
            r["quote_flag"] = list(r.get("quote_flag") or []) + [FLAG_DIRINC]
            hits.append({"strike": r["strike"], "type": r["type"], "d_spot": d_spot,
                         "d_mark": d_mark, "prev_ts": prev.get("ts")})
    _watch_save(updated)
    return rows, hits


def add_quote_flags(rows):
    """Annotate each row with `quote_flag` — the guard that did not exist on 2026-08-04.

    ⚠️ **WHY THIS EXISTS, stated plainly so nobody weakens it later.** On 8/4 the
    USO Oct-16 130C returned `bid 5.70 / ask 5.70 / spread 0.00%` on two
    consecutive live pulls. It was caught **by eye**, and only because the number
    was needed for a live gate. Had it been graded, the desk would have published
    a net debit of `$1.25 / 25.0%` — right verdict, wrong number, and
    unreproducible by anyone re-pulling five minutes later.

    ★ **THE TRAP IS THAT THE DEFECT RENDERS AS THE BEST-LOOKING QUOTE ON THE
    BOARD.** `Sprd% = 0.00` is the most attractive cell in the table. Every other
    liquidity heuristic this tool has — wide-spread flag, thin-OI flag — reads a
    locked quote as *ideal*. A guard that only flags WIDE spreads is blind by
    construction to the failure where the spread is impossibly NARROW.

    **Failure direction is deliberate: per-row and loud, not whole-pull fatal.**
    A 58-row chain routinely contains a dead strike somewhere; exiting non-zero on
    any defect would make the tool unusable at fire time and it would get bypassed,
    which is worse than no guard. Use `--legs` to make it fatal for the strikes you
    are actually transacting (that is the fire-time invocation).

    **NONMONO is ADVISORY, not hard, and that is a real judgement:** adjacent-strike
    violations are *normal* in an illiquid strip (the same USO chain had several
    among strikes nobody would trade). Making it fatal would produce exactly the
    cry-wolf alarm that `mark_asof`'s "⚠ STALE 10bd" became — an alarm firing on the
    book's normal state stops being read. It is reported because it CORROBORATES a
    hard flag: the 130C was both LOCK **and** bid-equal to the 129C, and two
    independent grounds is what made the call obvious.
    """
    for r in rows:
        r["quote_flag"] = []

    for r in rows:
        bid, ask = r.get("bid"), r.get("ask")
        if bid is None or ask is None:
            continue
        if bid > ask:
            r["quote_flag"].append(FLAG_XSD)
        elif bid == ask and bid > 0:
            r["quote_flag"].append(FLAG_LOCK)
        if bid == 0 and ask == 0:
            r["quote_flag"].append(FLAG_DEAD)
        elif bid == 0 and ask > 0:
            r["quote_flag"].append(FLAG_NOBID)

    # Strike monotonicity, per option type. Calls fall as strike rises; puts rise.
    # Rows with no market at all are excluded — comparing against a 0/0 strike
    # manufactures violations rather than finding them.
    for tletter in {r.get("type") for r in rows}:
        chain = [r for r in rows
                 if r.get("type") == tletter
                 and r.get("strike") is not None
                 and r.get("bid") is not None and r.get("ask") is not None
                 and not (r["bid"] == 0 and r["ask"] == 0)]
        chain.sort(key=lambda r: r["strike"])
        for lo, hi in zip(chain, chain[1:]):
            if tletter == "C":
                bad = (hi["bid"] > lo["bid"]) or (hi["ask"] > lo["ask"])
            elif tletter == "P":
                bad = (hi["bid"] < lo["bid"]) or (hi["ask"] < lo["ask"])
            else:
                continue
            if bad:
                for r in (lo, hi):
                    if FLAG_NONMONO not in r["quote_flag"]:
                        r["quote_flag"].append(FLAG_NONMONO)
    return rows


def flag_str(r):
    return ",".join(r.get("quote_flag") or []) or "-"


def has_hard_defect(r):
    return bool(HARD_FLAGS.intersection(r.get("quote_flag") or []))


def fmt(x, dp=2):
    return "N/A" if x is None else f"{x:.{dp}f}"


def display(ticker, expiry, opt_type, spot, spot_asof, rows, meta, wide_pct, thin_oi, dir_hits=None):
    today = datetime.now().strftime("%Y-%m-%d")
    print("TERRY live option-chain fetch")
    print("=============================")
    print("Data only — no broker access, no execution recommendation.\n")
    print(f"Underlying: {ticker}  Spot: {fmt(spot)} (as-of {spot_asof})")
    print(f"Expiry: {expiry}  Type: {opt_type or 'all'}  Rows: {len(rows)}")
    print("Greeks (Delta/Theta): N/A — yfinance does not provide them.\n")
    print("Strike   Mny%    T  Bid    Ask    Mark   Sprd%   IV%     Vol    OI     Flag      LastTrade")
    print("-------  ------  -  -----  -----  -----  ------  ------  -----  -----  --------  ----------------")
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
              f"{fmt(r['volume'],0):>5}  {fmt(r['open_interest'],0):>5}  "
              f"{flag_str(r):<8}  {r.get('last_trade') or 'N/A'}")
    print("\nTERRY liquidity flags")
    print(f"- Wide spread rows >{wide_pct:.0f}% of mark: {len(wide)}")
    print(f"- Thin OI rows <{thin_oi:.0f} OI: {len(thin)}")

    # ---- Quote sanity (2026-08-04) -------------------------------------
    # The wide-spread flag above is blind, BY CONSTRUCTION, to the failure where
    # the spread is impossibly NARROW. That is the whole reason this block exists.
    counts = {}
    for r in rows:
        for f in (r.get("quote_flag") or []):
            counts[f] = counts.get(f, 0) + 1
    hard = [r for r in rows if has_hard_defect(r)]
    print("\nTERRY quote sanity")
    if not counts:
        print("  ✓ no quote defects: no locked, crossed, dead or no-bid rows; strike monotonicity holds")
    else:
        for code in (FLAG_XSD, FLAG_LOCK, FLAG_DEAD, FLAG_NOBID, FLAG_NONMONO):
            if code in counts:
                mark = "🔴" if code in HARD_FLAGS else "⚠️ "
                print(f"  {mark} {code:<8} {counts[code]:>3} row(s)")
        if hard:
            print(f"  🔴 {len(hard)} row(s) carry a HARD defect and MUST NOT be used to compute a net debit:")
            for r in hard[:12]:
                print(f"       {fmt(r['strike']):>7} {r['type']}  bid {fmt(r['bid'])} / ask {fmt(r['ask'])}"
                      f"  [{flag_str(r)}]")
            if len(hard) > 12:
                print(f"       … and {len(hard)-12} more")
        if FLAG_LOCK in counts:
            print("  ⛔ A `0.00%` SPREAD IS A REJECT, NOT A TIGHT MARKET. Re-pull before grading.")
        if FLAG_NONMONO in counts:
            rate = counts[FLAG_NONMONO] / len(rows) * 100 if rows else 0.0
            print(f"     NONMONO base rate: {counts[FLAG_NONMONO]}/{len(rows)} rows = {rate:.0f}% "
                  f"of the displayed strip.")
            print("     ⚠️  It flags BOTH sides of an inverted pair and does NOT say which one is "
                  "wrong — usually the one with the OLDER lastTradeDate. Check that before blaming "
                  "a strike.")
            if rate >= 25:
                print(f"     🟠 CHAIN-QUALITY READ: at {rate:.0f}% the STRIP is broadly unreliable, "
                      "not any one strike. Trust high-OI / round-number strikes and re-pull anything "
                      "else before it carries a number.")
            else:
                print("     (ADVISORY only — adjacent-strike noise is normal in an illiquid strip; "
                      "it earns its keep as CORROBORATION of a hard flag.)")
    # Freshness guard (rule #4)
    latest = meta.get("latest_trade")
    if latest and not latest.startswith(today):
        print(f"\n⚠️  FRESHNESS: freshest trade in set = {latest} (NOT today {today}). "
              f"Marks may be stale (after-hours/weekend). Re-confirm live broker marks before any fill.")
    else:
        print(f"\nFreshness: freshest trade in set = {latest or 'N/A'} (fetch {datetime.now().strftime('%Y-%m-%d %H:%M')}).")
    # ═══ STALE-QUOTE DOCTRINE — unconditional, because it is ALWAYS true ═══
    # Added 2026-09-11 after this tool reported the XLE Sep-30 65C at bid 1.66 while the
    # BROKER showed 1.51 x 53 at a comparable moment: ~10% optimistic ON THE SIDE YOU
    # TRANSACT, in the direction that FLATTERS a sale. Investigated the same session:
    #   * yfinance/Yahoo expose NO bid/ask timestamp and NO delay flag for an option leg.
    #     The raw payload carries neither -- MEASURED against the live JSON, not assumed.
    #   * The UNDERLYING quote DOES carry `exchangeDataDelayedBy: 0` + `regularMarketTime`,
    #     and the printed spot tested real-time to within ~1 min. The asymmetry is the
    #     finding: spot is declared and timestamped, the option quote is NEITHER.
    #   * `lastTradeDate` is the last EXECUTED TRADE. It is a DIFFERENT QUANTITY from quote
    #     age and can be fresh while the quote is stale. The old freshness line compared it
    #     to a DATE, so it could not see intraday staleness of ANY magnitude, by construction.
    #   * Lag is CONFIRMED materially nonzero (sign violations appear in this tool's OWN
    #     successive outputs, needing no external data). Magnitude order ~15 min is
    #     PLAUSIBLE on single-session evidence and is NOT a measured constant -- do not
    #     cite it as one.
    print("\n⚠️  BID/ASK AGE IS UNKNOWN AND UNKNOWABLE FROM THIS FEED.")
    print("   The spot above is Yahoo-declared real-time. The option bid/ask carries NO")
    print("   timestamp and no delay flag, and is NOT proven contemporaneous with it.")
    print("   ⛔ THESE ARE SCREENING MARKS, NOT FIRE-TIME MARKS. Take the price you")
    print("      actually transact on from the BROKER chain. (2026-09-11: this tool read")
    print("      ~10% high on the bid vs the broker, on the side being sold.)")
    if dir_hits:
        print(f"\n🔴 DIRINC — {len(dir_hits)} row(s) moved OPPOSITE the printed spot since the last --no-cache pull:")
        for h in dir_hits[:6]:
            print(f"     {h['strike']:>8} {h['type']}  spot {h['d_spot']:+.3f} but mark {h['d_mark']:+.3f}"
                  f"  [prev pull {(h['prev_ts'] or '')[11:19]}]")
        print("     Delta has a sign; this is the shape of a quote reflecting an OLDER market state.")
        print("     ⚠️  ADVISORY, never fatal — an IV move can do this legitimately. It is evidence,")
        print("        not proof, and a flag cannot recover the true bid. Go to the broker.")
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

    # Flags are computed on the FULL chain, before windowing — monotonicity needs
    # a row's true neighbours, not whichever ones survived a ±window filter.
    rows = add_quote_flags(rows)
    rows = add_moneyness(rows, spot)
    # Direction-consistency only means anything on a FRESH pull — comparing a cached
    # payload against the stored observation would diff a row against itself.
    dir_hits = []
    if args.no_cache:
        rows, dir_hits = add_direction_flags(rows, ticker, args.expiry, spot)

    # --legs is checked against the full chain too, so a leg outside the display
    # window is still gated rather than silently reported "not found".
    leg_rows, leg_missing = [], []
    if args.legs:
        for k in args.legs:
            hit = [r for r in rows if r["strike"] is not None and abs(r["strike"] - k) < 1e-9]
            if hit:
                leg_rows.extend(hit)
            else:
                leg_missing.append(k)

    rows = apply_window(rows, spot, args.window, args.min_oi)
    if args.limit:
        rows = rows[: args.limit]

    if args.json:
        print(json.dumps({
            "ticker": ticker, "expiry": args.expiry, "type": opt_type,
            "spot": spot, "spot_asof": spot_asof, "fetch_ts": datetime.now().isoformat(),
            "latest_trade": meta.get("latest_trade"), "rows": rows,
            "legs_checked": [r["strike"] for r in leg_rows],
            "legs_missing": leg_missing,
            "legs_defective": [{"strike": r["strike"], "type": r["type"],
                                "bid": r["bid"], "ask": r["ask"],
                                "quote_flag": r["quote_flag"]}
                               for r in leg_rows if has_hard_defect(r)],
        }, indent=2))
    else:
        display(ticker, args.expiry, opt_type, spot, spot_asof, rows, meta,
                args.wide_spread_pct, args.thin_oi, dir_hits)

    # ---- Fire-time leg gate --------------------------------------------
    # Chain-wide defects are advisory (a 58-row chain routinely has a dead strike
    # nobody would trade). The legs you are ABOUT TO TRANSACT are not advisory.
    if args.legs:
        bad = [r for r in leg_rows if has_hard_defect(r)]
        if not args.json:
            print("\nTERRY leg gate (--legs)")
            for r in leg_rows:
                state = "🔴 DEFECTIVE" if has_hard_defect(r) else "✓ usable"
                print(f"  {state:<13} {fmt(r['strike']):>7} {r['type']}  "
                      f"bid {fmt(r['bid'])} / ask {fmt(r['ask'])}  [{flag_str(r)}]")
            for k in leg_missing:
                print(f"  🔴 NOT LISTED  {k:>7}     — strike absent from this expiry")
        if bad or leg_missing:
            if not args.json:
                print("\n⛔ EXIT 2 — a requested leg is unusable. DO NOT compute a net debit "
                      "off this pull. Re-pull; if it persists, the leg is untradeable and that "
                      "is a NO TRADE, not a number to work around.")
            return 2
        if not args.json:
            print("  ⇒ all requested legs carry usable two-sided quotes.")
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
    # ------------------------------------------------------------------
    # QUOTE SANITY (2026-08-04) — synthetic bad-row injection.
    # Same standard as positions_from_forge.py: assert the guard FIRES on
    # injected defects, not merely that clean input stays clean. A guard whose
    # only evidence is a passing run on good data has never been tested.
    # ------------------------------------------------------------------
    def _mk(strike, bid, ask, t="C"):
        return {"strike": strike, "type": t, "bid": bid, "ask": ask,
                "mark": (bid + ask) / 2, "spread_pct": None}

    # (a) NO FALSE POSITIVES — a clean, strictly-monotone call strip flags nothing.
    clean = add_quote_flags([_mk(125, 6.10, 6.95), _mk(130, 5.65, 5.75), _mk(135, 4.35, 4.85)])
    assert all(not r["quote_flag"] for r in clean), \
        f"false positive on a clean strip: {[(r['strike'], r['quote_flag']) for r in clean]}"

    # (b) ★ THE 2026-08-04 REGRESSION — the exact rows that caused this guard to
    #     be written. USO Oct-16 130C came back bid == ask == 5.70.
    uso = add_quote_flags([_mk(129, 5.70, 6.15), _mk(130, 5.70, 5.70), _mk(131, 4.90, 5.75)])
    lock_row = [r for r in uso if r["strike"] == 130][0]
    assert FLAG_LOCK in lock_row["quote_flag"], \
        f"THE 8/4 DEFECT WENT UNDETECTED: {lock_row['quote_flag']}"
    assert has_hard_defect(lock_row), "a locked quote must be a HARD defect"
    # ★ THE GUARD CORRECTED ITS AUTHOR, and the correction is the useful part.
    # On 8/4 I reported the 130C as failing on two independent grounds: locked,
    # AND "violating strike monotonicity because its BID equalled the 129C BID."
    # I expected this assertion to prove the second ground was weak — equal
    # adjacent bids are a FLAT SPOT on a price grid, not an inversion. It failed,
    # because the row IS non-monotone for a reason I had not spotted:
    #     130C ask 5.70  <  131C ask 5.75
    # A HIGHER-strike call cannot ASK MORE than a lower-strike one. The locked
    # 5.70 dragged the ask artificially low, and the inversion shows up one strike
    # ABOVE, on the opposite side of the market from where I was looking.
    # ⇒ Two independent grounds was the right conclusion, reached on the wrong
    #   pair and the wrong side. Corrected at the claim site, not quietly.
    assert FLAG_NONMONO in lock_row["quote_flag"], \
        "the 8/4 row is non-monotone on the ASK vs the 131C — corroboration, by design"

    # (b2) ... and the flat-spot property I *thought* I was testing above, pinned
    #      separately: equal bids with a sane ask ladder must stay silent, or the
    #      flag cries wolf on every coarsely quoted strip.
    flat = add_quote_flags([_mk(129, 5.70, 6.15), _mk(130, 5.70, 6.10)])
    assert all(FLAG_NONMONO not in r["quote_flag"] for r in flat), \
        f"a flat spot must not read as an inversion: {[(r['strike'], r['quote_flag']) for r in flat]}"

    # (c) A genuine inversion DOES fire: 132C bidding above 131C.
    inv = add_quote_flags([_mk(131, 4.90, 5.75), _mk(132, 5.40, 5.90)])
    assert all(FLAG_NONMONO in r["quote_flag"] for r in inv), \
        f"call inversion missed: {[(r['strike'], r['quote_flag']) for r in inv]}"
    # ... and in the opposite direction for puts, which rise with strike.
    pinv = add_quote_flags([_mk(70, 2.00, 2.10, "P"), _mk(75, 1.50, 1.60, "P")])
    assert all(FLAG_NONMONO in r["quote_flag"] for r in pinv), "put inversion missed"

    # (d) crossed / dead / no-bid
    xsd = add_quote_flags([_mk(100, 3.50, 3.20)])[0]
    assert FLAG_XSD in xsd["quote_flag"] and has_hard_defect(xsd), xsd["quote_flag"]
    dead = add_quote_flags([_mk(200, 0.0, 0.0)])[0]
    assert FLAG_DEAD in dead["quote_flag"] and has_hard_defect(dead), dead["quote_flag"]
    nobid = add_quote_flags([_mk(200, 0.0, 4.30)])[0]
    assert FLAG_NOBID in nobid["quote_flag"] and has_hard_defect(nobid), nobid["quote_flag"]
    assert FLAG_DEAD not in nobid["quote_flag"], "no-bid must not also read as dead"

    # (e) A dead strike must not manufacture monotonicity violations in its
    #     neighbours — that would be the guard generating its own findings.
    withdead = add_quote_flags([_mk(125, 6.10, 6.95), _mk(127, 0.0, 0.0), _mk(130, 5.65, 5.75)])
    for r in withdead:
        if r["strike"] != 127:
            assert FLAG_NONMONO not in r["quote_flag"], \
                f"dead strike {127} manufactured a violation at {r['strike']}"

    # (f) NONMONO alone must NOT be a hard defect — it is advisory by design.
    assert not has_hard_defect(inv[0]), "NONMONO alone must not block a net-debit computation"

    # ---- (g) DIRECTION-CONSISTENCY (FLAG_DIRINC), added 2026-09-11 -----------
    # An untested guard is not a guard. Each case below was verified to FAIL when the
    # detector is disabled, so these assert behaviour, not merely absence of a crash.
    import tempfile as _tf
    global WATCH_PATH
    _saved_watch = WATCH_PATH
    _dirbad = []
    try:
        with _tf.TemporaryDirectory() as _td:
            def _pull(ticker, expiry, spot, strike, typ, mark):
                """One synthetic --no-cache pull of a single contract."""
                rws = [{"strike": strike, "type": typ, "mark": mark, "quote_flag": []}]
                rws, hits = add_direction_flags(rws, ticker, expiry, spot)
                return rws[0], hits

            def _case(name, typ, s0, m0, s1, m1, want_flag):
                WATCH_PATH_LOCAL = Path(_td) / f"w_{name}.json"
                globals()["WATCH_PATH"] = WATCH_PATH_LOCAL
                r0, h0 = _pull("T", "E", s0, 100.0, typ, m0)
                if h0:
                    _dirbad.append(f"{name}: first-ever pull flagged — nothing to compare against")
                if FLAG_DIRINC in (r0.get("quote_flag") or []):
                    _dirbad.append(f"{name}: first pull carried DIRINC")
                r1, h1 = _pull("T", "E", s1, 100.0, typ, m1)
                got = FLAG_DIRINC in (r1.get("quote_flag") or [])
                if got != want_flag:
                    _dirbad.append(f"{name}: DIRINC={got}, want {want_flag}")

            # a CALL's mark must not fall while spot rises
            _case("call_up_mark_down",  "C", 100.0, 2.00, 101.0, 1.80, True)
            _case("call_up_mark_up",    "C", 100.0, 2.00, 101.0, 2.20, False)
            # a PUT's mark SHOULD fall while spot rises — the mirror must not false-fire
            _case("put_up_mark_down",   "P", 100.0, 2.00, 101.0, 1.80, False)
            _case("put_up_mark_up",     "P", 100.0, 2.00, 101.0, 2.20, True)
            _case("call_down_mark_up",  "C", 100.0, 2.00,  99.0, 2.20, True)
            _case("put_down_mark_down", "P", 100.0, 2.00,  99.0, 1.80, True)
            # noise floor: a 0.01% spot tick must NOT arm the test at all
            _case("below_noise_floor",  "C", 100.0, 2.00, 100.01, 1.80, False)
            # ★ PERMANENT REGRESSION — the live 2026-09-11 XLE Sep-30 65C incident.
            # The tool's OWN successive outputs: spot 65.42 -> 65.32 (DOWN) while the
            # call bid went 1.62 -> 1.66 (UP). This needs no lag model and no external
            # data; it is the single strongest piece of evidence in the investigation.
            _case("XLE_65C_2026_09_11", "C", 65.42, 1.62, 65.32, 1.66, True)
    finally:
        globals()["WATCH_PATH"] = _saved_watch
    if _dirbad:
        raise AssertionError("DIRINC selftest FAILED: " + "; ".join(_dirbad))

    # DIRINC must never be a hard defect — parity with the NONMONO decision.
    assert FLAG_DIRINC not in HARD_FLAGS, \
        "DIRINC became a HARD flag — one ordinary IV move would now block a fire"

    print("  direction-consistency: 8 cases PASS "
          "(call/put x spot-up/down / noise-floor silence / first-pull silence / "
          "XLE-65C 2026-09-11 live regression / advisory-not-hard)")

    print("  quote-sanity: 7 injection cases PASS "
          "(clean-strip / 8-4 LOCK+ASK-INVERSION regression / flat-spot silence / "
          "call+put inversion / xsd+dead+nobid / dead-neighbour isolation / advisory-vs-hard)")

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
    ap.add_argument("--legs", type=lambda s: [float(x) for x in s.replace(" ", "").split(",") if x],
                    help="comma-separated strikes you intend to transact, e.g. --legs 125,130. "
                         "EXITS 2 if any is locked/crossed/dead/no-bid or absent. The fire-time form.")
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
