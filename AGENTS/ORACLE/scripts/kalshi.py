#!/usr/bin/env python3
"""ORACLE Kalshi fetcher — Kalshi trade-api v2 (RSA-PSS signed; read-only use).

Kalshi is the CFTC-regulated US exchange — an independent real-money source that
corroborates Polymarket and fills the VIX/vol + S&P-range + macro gaps. ORACLE
uses it for MARKET DATA ONLY (no order placement — credential is read-only by use).

Creds (NEVER in the repo): env KALSHI_KEY_ID / KALSHI_PRIVATE_KEY_PATH, else
~/.config/kalshi/{key_id.txt, private_key.pem}. Private key is chmod 600.

Usage:
  python3 kalshi.py status                         # exchange status (connectivity)
  python3 kalshi.py search "<query>"  [-n N] [--pages P]  # keyword scan, full open-event universe by default
  python3 kalshi.py market <ticker>   [--json]     # one market, full detail
  python3 kalshi.py event  <event_ticker>          # event + its markets (multi-outcome)
  python3 kalshi.py series [--category Economics]   # list series (discovery)
  python3 kalshi.py pull  [--log] [--json]          # fetch everything in kalshi_watchlist.tsv

Notes:
  - Kalshi prices are in CENTS (0-100). yes_prob = last_price/100 (fallback bid/ask mid).
  - volume/open_interest are contract counts; liquidity is in cents (resting order $ * 100).
  - signing: base64( RSA-PSS-SHA256( timestamp_ms + METHOD + path ) ), salt = digest len.
"""
import sys, os, json, time, base64, argparse, datetime
import requests
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

BASE = "https://api.elections.kalshi.com/trade-api/v2"
HERE = os.path.dirname(os.path.abspath(__file__))
ORACLE_DIR = os.path.dirname(HERE)
WATCHLIST = os.path.join(ORACLE_DIR, "kalshi_watchlist.tsv")
# Separate log from Polymarket's ODDS_LOG — different native fields (OI, cents) and
# schema; a unified platform-tagged log can come later if cross-platform joins are needed.
KALSHI_LOG = os.path.join(ORACLE_DIR, "workbook", "KALSHI_ODDS_LOG.tsv")

CRED_DIR = os.environ.get("KALSHI_CRED_DIR", os.path.expanduser("~/.config/kalshi"))
KEY_ID = os.environ.get("KALSHI_KEY_ID") or open(os.path.join(CRED_DIR, "key_id.txt")).read().strip()
_PK_PATH = os.environ.get("KALSHI_PRIVATE_KEY_PATH", os.path.join(CRED_DIR, "private_key.pem"))
_PK = serialization.load_pem_private_key(open(_PK_PATH, "rb").read(), password=None)

THIN_VOLUME = 5000      # contracts — below this a single bet moves the print


def _sign(ts, method, path):
    msg = f"{ts}{method}{path}".encode()
    sig = _PK.sign(msg,
                   padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                               salt_length=hashes.SHA256().digest_size),
                   hashes.SHA256())
    return base64.b64encode(sig).decode()


def _get(path, params=None, tries=3):
    """Signed GET. `path` includes /trade-api/v2; signature excludes query string."""
    full = "/trade-api/v2" + path
    last = None
    for _ in range(tries):
        try:
            ts = str(int(time.time() * 1000))
            headers = {"KALSHI-ACCESS-KEY": KEY_ID,
                       "KALSHI-ACCESS-TIMESTAMP": ts,
                       "KALSHI-ACCESS-SIGNATURE": _sign(ts, "GET", full)}
            r = requests.get(BASE + path, headers=headers, params=params, timeout=25)
            r.raise_for_status()
            return r.json()
        except Exception as e:  # noqa: BLE001
            last = e
    raise last


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def parse_market(m):
    """Normalize a Kalshi market object into ORACLE fields.

    Live API uses *_dollars (already 0-1) and *_fp (fixed-point counts); we fall
    back to legacy cent-denominated names for resilience. yes/bid/ask are 0-1.
    """
    last = _f(m.get("last_price_dollars"))
    if last is None and _f(m.get("last_price")) is not None:
        last = _f(m.get("last_price")) / 100.0
    bid = _f(m.get("yes_bid_dollars"))
    if bid is None and _f(m.get("yes_bid")) is not None:
        bid = _f(m.get("yes_bid")) / 100.0
    ask = _f(m.get("yes_ask_dollars"))
    if ask is None and _f(m.get("yes_ask")) is not None:
        ask = _f(m.get("yes_ask")) / 100.0
    mid = (bid + ask) / 2.0 if (bid is not None and ask is not None) else None
    # prefer last trade if it's a real (>0) print; else the book mid.
    # DAEDALUS SFG 8/17 ACTION 1: Kalshi represents "never traded" as the literal
    # sentinel last_price_dollars="0.0000", not a missing field -- the old fallback
    # `last if last is not None else mid` let that sentinel through as yes=0.0,
    # which prints/logs as a real 0.0% probability for a market with NO book and NO
    # trade history. A missing book is not a zero-probability event: if there is
    # neither a real (>0) last trade NOR a real (>0) resting-book mid, yes=None
    # (renders as "--" via _pct; callers already filter `yes is not None`).
    if last and last > 0:
        yes = last
    elif mid and mid > 0:
        yes = mid
    else:
        yes = None
    prev = _f(m.get("previous_price_dollars"))
    d_prev = ((yes - prev) * 100.0) if (yes is not None and prev is not None) else None
    vol = _f(m.get("volume_fp"))
    vol = vol if vol is not None else _f(m.get("volume"))
    v24 = _f(m.get("volume_24h_fp"))
    v24 = v24 if v24 is not None else _f(m.get("volume_24h"))
    oi = _f(m.get("open_interest_fp"))
    oi = oi if oi is not None else _f(m.get("open_interest"))
    liq = _f(m.get("liquidity_dollars"))
    if liq is None and _f(m.get("liquidity")) is not None:
        liq = _f(m.get("liquidity")) / 100.0
    close = (m.get("close_time") or "")[:10]
    days_left = None
    if close:
        try:
            days_left = (datetime.date.fromisoformat(close) - datetime.date.today()).days
        except ValueError:
            days_left = None
    status = m.get("status")
    # Kalshi depth proxy: open interest (contracts). Thin if OI low AND no resting liq.
    thin = (oi or 0) < 1000 and (liq or 0) < 1000
    return {
        "ticker": m.get("ticker"),
        "title": m.get("title") or m.get("yes_sub_title") or m.get("no_sub_title"),
        "sub": m.get("yes_sub_title") or m.get("no_sub_title"),
        "yes": yes,
        "yes_bid": bid, "yes_ask": ask,
        "spread": (ask - bid) if (bid is not None and ask is not None) else None,
        "mid": mid,
        "d_prev": d_prev,
        "volume": vol, "volume_24h": v24,
        "open_interest": oi,
        "liquidity": liq,  # dollars
        "close": close, "days_left": days_left,
        "status": status,
        "thin": thin,
        "event_ticker": m.get("event_ticker"),
    }


# ---------- formatting ----------
def _pct(x):
    return "  —  " if x is None else f"{x*100:5.1f}%"


def _money(x):
    if x is None:
        return "—"
    for u, d in ((1e9, "B"), (1e6, "M"), (1e3, "K")):
        if abs(x) >= u:
            return f"${x/u:.1f}{d}"
    return f"${x:.0f}"


def _num(x):
    if x is None:
        return "—"
    for u, d in ((1e6, "M"), (1e3, "K")):
        if abs(x) >= u:
            return f"{x/u:.1f}{d}"
    return f"{x:.0f}"


def fmt_row(label, m, tier=""):
    flag = " ⚠thin" if m.get("thin") else ""
    st = m.get("status")
    if st and st != "active":
        flag += f" [{st}]"
    if m.get("days_left") is not None and 0 <= m["days_left"] <= 7:
        flag += f" ⏳{m['days_left']}d"
    sp = m.get("spread")
    spread = f"sp{sp*100:.0f}¢" if sp is not None else "sp —"
    # WIDE-BOOK MID DISCLOSURE (added 2026-08-27, tool-verification pass).
    # parse_market prefers the LAST trade over the book mid. On a tight book that is
    # right. On a WIDE one it is a citation trap: a single lift of the offer prints
    # at the ask and becomes the headline number. Live instance that prompted this --
    # KXCBDECISIONJAPAN-26SEP17-H25 read last 92.0% on a 87/92 book (mid 89.5%) with
    # 797 contracts of 24h volume. ORACLE's own KB-ORC-069 already ruled "cite the MID,
    # never the last" for exactly this market family, and the tool did not surface the
    # mid at all -- the rule lived in a KB row while every dashboard line contradicted it.
    # Display-only: the logged yes_prob is deliberately unchanged so the time series
    # stays continuous (a mid/last basis switch mid-series would be its own defect).
    mid = m.get("mid")
    yes = m.get("yes")
    # v1 of this flag fired on every [finalized] row: a settled market has no book
    # (bid 0 / ask 100), so "mid" is a meaningless 50.0. Flagging dead rows would train
    # readers to ignore the marker on the live ones it exists for. Suppressed on a
    # degenerate/absent book (spread >= 99c) and on any non-active status.
    _book_ok = sp is not None and 0.03 <= sp < 0.99
    _live = (st is None or st == "active")
    if (_book_ok and _live and mid is not None and yes is not None
            and abs(yes - mid) >= 0.01):
        spread += f" ⚠mid {mid*100:.1f}"
    dp = m.get("d_prev")
    dprev = f"{dp:+5.1f}" if dp is not None else "  —  "
    return (f"{label[:32]:32} {tier:4} {_pct(m['yes'])}  Δp {dprev}  {spread:15}  "
            f"vol {_num(m['volume']):>6}  OI {_num(m['open_interest']):>6}  "
            f"liq {_money(m['liquidity']):>7}  {m['close']}{flag}")


# ---------- commands ----------
def cmd_status(args):
    d = _get("/exchange/status")
    print("Kalshi exchange status:", json.dumps(d))


def cmd_market(args):
    d = _get(f"/markets/{args.ticker}")
    m = d.get("market", d)
    if args.json:
        print(json.dumps(m, indent=2)); return
    print(fmt_row(m.get("title") or args.ticker, parse_market(m)))
    pm = parse_market(m)
    print(f"  ticker={pm['ticker']}  event={pm['event_ticker']}  bid/ask={pm['yes_bid']}/{pm['yes_ask']}¢  status={pm['status']}")


def markets_for_event(event_ticker):
    """Full market objects (with live _dollars fields) for an event — the nested
    markets in /events are lightweight and omit prices, so we go via /markets."""
    d = _get("/markets", params={"event_ticker": event_ticker})
    return [parse_market(mm) for mm in d.get("markets", [])]


def cmd_event(args):
    mkts = [x for x in markets_for_event(args.event) if x["yes"] is not None]
    print(f"▸ {args.event}  ({len(mkts)} markets)")
    for pm in sorted(mkts, key=lambda r: -(r["yes"] or 0)):
        print("   " + fmt_row(pm["sub"] or pm["title"] or pm["ticker"], pm) + f"  [{pm['ticker']}]")


def cmd_series(args):
    params = {"limit": 200}
    if args.category:
        params["category"] = args.category
    d = _get("/series/", params=params)
    ser = d.get("series", d) if isinstance(d, dict) else d
    for s in (ser or []):
        print(f"{s.get('ticker',''):20} {s.get('category','')[:16]:16} {s.get('title','')[:70]}")


def cmd_search(args):
    """Keyword scan over open events (paginated via /events, exhaustive by default).

    FIXED 2026-08-18 (flagged 8/17 as "the false-negative machine", two coverage
    misses in two sessions before the fix landed). Root cause was NOT the status
    filter -- `status=open` correctly returns `status:"active"` markets when
    scoped to a known event/series (verified against KXFED-26SEP). The real
    defect: a flat, unscoped `/markets?status=open` scan is dominated by Kalshi's
    auto-generated multivariate/combinatorial ("MVE shard") parlay markets, which
    outnumber ordinary markets so heavily that a real term (BOJ, "interest rate")
    never surfaced within any practical page cap -- confirmed empirically: 80,000
    raw markets scanned via the old path with zero hits on a market known to be
    live. `/events?status=open` is NOT polluted by that firehose (0 MVE-shard
    events found in a sample scan) and the full open-event universe is small
    enough to exhaust outright: 10,359 events / 200 per page = 52 pages, confirmed
    by a full paginated count on 2026-08-18. Default `--pages` is set well above
    that so a normal run certifies full coverage rather than needing a bigger cap
    guessed after the fact.

    FAILS LOUD: prints whether the scan reached the end of the open-event universe
    (coverage CERTIFIED) or hit the page cap first (coverage NOT CERTIFIED -- a
    zero result is then unverified, not a confirmed absence) and exits non-zero
    in the uncertified case so a caller can't mistake a capped scan for a clean one.
    """
    q = args.query.lower()
    found, cursor, pages, events_seen = [], None, 0, 0
    exhausted = False
    while pages < args.pages:
        params = {"status": "open", "limit": 200, "with_nested_markets": "true"}
        if cursor:
            params["cursor"] = cursor
        d = _get("/events", params=params)
        evs = d.get("events", [])
        events_seen += len(evs)
        for e in evs:
            ehay = f"{e.get('title','')} {e.get('sub_title','')} {e.get('event_ticker','')} {e.get('series_ticker','')} {e.get('category','')}".lower()
            for m in e.get("markets", []):
                hay = f"{ehay} {m.get('title','')} {m.get('subtitle','')} {m.get('yes_sub_title','')} {m.get('ticker','')}".lower()
                if q in hay:
                    found.append(parse_market(m))
        cursor = d.get("cursor")
        pages += 1
        if not cursor or not evs:
            exhausted = True
            break
    found.sort(key=lambda r: -(r["volume"] or 0))
    if exhausted:
        print(f"'{args.query}' — {len(found)} markets  ({events_seen} events scanned, {pages} pages — "
              f"FULL open-event universe, coverage CERTIFIED):\n")
    else:
        print(f"⚠️  '{args.query}' — {len(found)} markets found so far, but COVERAGE NOT CERTIFIED: "
              f"hit the --pages {args.pages} cap after {events_seen} events with more remaining. "
              f"A zero here is NOT a verified absence — rerun with a higher --pages or check a "
              f"control term known to be populated.\n")
    for pm in found[:args.n]:
        print(fmt_row(pm["title"] or pm["ticker"], pm) + f"   [{pm['ticker']}]")
    if not exhausted:
        sys.exit(2)


def cmd_pull(args):
    if not os.path.exists(WATCHLIST):
        print(f"no watchlist at {WATCHLIST}"); return
    ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    print(f"ORACLE Kalshi pull @ {ts}\n" + "-" * 110)
    attempted = 0   # watchlist rows parsed (M)
    fetched = 0     # rows that returned data, incl. no-book/NA rows (N)
    errored = 0     # rows that raised or returned no data at all
    rows_out = []
    with open(WATCHLIST) as f:
        for ln in f:
            ln = ln.rstrip("\n")
            if not ln.strip() or ln.startswith("#"):
                continue
            parts = ln.split("\t")
            if len(parts) < 4:
                continue
            attempted += 1
            label, kind, ticker, tier = parts[0], parts[1], parts[2], parts[3]
            route = parts[4] if len(parts) > 4 else ""
            try:
                if kind == "event":
                    mkts = markets_for_event(ticker)
                    ranked = [x for x in mkts if x["yes"] is not None]
                    pm = max(ranked, key=lambda r: r["yes"]) if ranked else None
                    sub = " (top)"
                else:
                    dd = _get(f"/markets/{ticker}")
                    pm = parse_market(dd.get("market", dd)); sub = ""
                if pm is None:
                    print(f"{label[:34]:34} {tier:4}  (no data)"); errored += 1; continue
                print(fmt_row(label + sub, pm, tier))
                rows_out.append((ts, "Kalshi", label, ticker, tier, pm))
                fetched += 1
            except Exception as e:  # noqa: BLE001
                print(f"{label[:34]:34} {tier:4}  ERR {e}"); errored += 1
    # DAEDALUS SFG 8/17 ACTION 2: a bare "logged N rows" cannot distinguish 12-of-12
    # from 12-of-18 -- always state fetched-of-attempted (+ error count) so a
    # downstream reader can tell success from silent shortfall without re-running.
    print(f"\nfetched {fetched}-of-{attempted}" + (f"  ({errored} errored/no-data)" if errored else ""))
    if args.log and rows_out:
        new = not os.path.exists(KALSHI_LOG)
        with open(KALSHI_LOG, "a") as fo:
            if new:
                fo.write("ts\tticker\tlabel\ttier\tyes_prob\tvolume\topen_interest\tliquidity\td_prev\tclose\n")
            for ts_, plat, label, tick, tier, pm in rows_out:
                dpv = pm.get("d_prev")
                dpv = round(dpv, 1) if dpv is not None else ""
                # ACTION 1 continuation: a no-book market now parses with yes=None
                # (see parse_market) -- write it to the ledger as NA, never as the
                # Python string "None" and never as a fabricated 0.0.
                yv = pm["yes"] if pm["yes"] is not None else "NA"
                fo.write(f"{ts_}\t{tick}\t{label}\t{tier}\t{yv}\t{pm['volume']}\t"
                         f"{pm['open_interest']}\t{pm['liquidity']}\t{dpv}\t{pm['close']}\n")
        print(f"logged {len(rows_out)} rows -> {KALSHI_LOG}")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("status"); s.set_defaults(fn=cmd_status)
    s = sub.add_parser("market"); s.add_argument("ticker"); s.add_argument("--json", action="store_true"); s.set_defaults(fn=cmd_market)
    s = sub.add_parser("event"); s.add_argument("event"); s.set_defaults(fn=cmd_event)
    s = sub.add_parser("series"); s.add_argument("--category"); s.set_defaults(fn=cmd_series)
    s = sub.add_parser("search"); s.add_argument("query"); s.add_argument("-n", type=int, default=12); s.add_argument("--pages", type=int, default=70); s.set_defaults(fn=cmd_search)
    s = sub.add_parser("pull"); s.add_argument("--log", action="store_true"); s.add_argument("--json", action="store_true"); s.set_defaults(fn=cmd_pull)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
