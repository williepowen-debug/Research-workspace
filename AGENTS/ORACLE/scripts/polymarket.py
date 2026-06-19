#!/usr/bin/env python3
"""ORACLE prediction-market fetcher — Polymarket Gamma API (public, no auth).

Usage:
  python3 polymarket.py search "<query>" [-n N]   # discover markets + slugs
  python3 polymarket.py market <slug>             # one market, full detail
  python3 polymarket.py event  <slug>             # grouped event (multi-outcome)
  python3 polymarket.py pull [--log] [--json]     # fetch everything in watchlist.tsv

Design notes:
  - outcomePrices[Yes] IS the market-implied probability (0-1).
  - oneDayPriceChange / oneWeekPriceChange give deltas without local history.
  - THIN-LIQUIDITY GUARDRAIL (memory: finding_thin_liquidity_prediction_market_discipline):
    a single print on a low-volume contract is NOT a "hold". Markets below the
    liquidity/volume floor are flagged `thin=True` so downstream never marks on one print.
  - `pull --log` appends a timestamped row per market to workbook/ODDS_LOG.tsv (the
    machine-readable time series). KB.tsv stays the 13-col knowledge base for claims.
"""
import sys, os, json, argparse, datetime
import requests

GAMMA = "https://gamma-api.polymarket.com"
HERE = os.path.dirname(os.path.abspath(__file__))
ORACLE_DIR = os.path.dirname(HERE)                      # AGENTS/ORACLE
WATCHLIST = os.path.join(ORACLE_DIR, "watchlist.tsv")
ODDS_LOG = os.path.join(ORACLE_DIR, "workbook", "ODDS_LOG.tsv")

THIN_LIQUIDITY = 5000.0   # USD order-book depth — below this a single $5-50K bet moves 5-10pp
THIN_VOLUME = 5000.0      # USD lifetime volume floor


def _get(path, params=None, tries=3):
    last = None
    for _ in range(tries):
        try:
            r = requests.get(GAMMA + path, params=params, timeout=25)
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
    """Normalize a Gamma market object into ORACLE's fields."""
    outs, prices = m.get("outcomes"), m.get("outcomePrices")
    try:
        outs = json.loads(outs) if isinstance(outs, str) else (outs or [])
    except json.JSONDecodeError:
        outs = []
    try:
        prs = [float(p) for p in (json.loads(prices) if isinstance(prices, str) else (prices or []))]
    except (json.JSONDecodeError, TypeError, ValueError):
        prs = []
    yes = None
    if outs and prs:
        for o, p in zip(outs, prs):
            if str(o).strip().lower() == "yes":
                yes = p
                break
        if yes is None:
            yes = prs[0]
    liq = _f(m.get("liquidityNum"))
    if liq is None:
        liq = _f(m.get("liquidity"))
    vol = _f(m.get("volumeNum"))
    if vol is None:
        vol = _f(m.get("volume"))
    thin = (liq is not None and liq < THIN_LIQUIDITY) or (vol is not None and vol < THIN_VOLUME)
    end = (m.get("endDate") or "")[:10]
    days_left = None
    if end:
        try:
            days_left = (datetime.date.fromisoformat(end) - datetime.date.today()).days
        except ValueError:
            days_left = None
    resolved = bool(m.get("closed")) or (days_left is not None and days_left < 0)
    expiring = days_left is not None and 0 <= days_left <= 7
    return {
        "question": m.get("question"),
        "slug": m.get("slug"),
        "yes": yes,
        "outcomes": list(zip(outs, prs)) if outs and prs else [],
        "volume": vol,
        "liquidity": liq,
        "d1": _f(m.get("oneDayPriceChange")),
        "d7": _f(m.get("oneWeekPriceChange")),
        "end": end,
        "days_left": days_left,
        "active": m.get("active"),
        "closed": m.get("closed"),
        "thin": thin,
        "resolved": resolved,
        "expiring": expiring,
    }


def market_by_slug(slug):
    d = _get("/markets", {"slug": slug})
    return parse_market(d[0]) if d else None


def event_by_slug(slug):
    d = _get("/events", {"slug": slug})
    if not d:
        return None
    e = d[0]
    return {
        "title": e.get("title"),
        "slug": e.get("slug"),
        "volume": _f(e.get("volume")),
        "markets": [parse_market(mm) for mm in e.get("markets", [])],
    }


def search(q, n=6):
    d = _get("/public-search", {"q": q, "limit_per_type": n, "events_status": "active"})
    return d.get("events", []) if isinstance(d, dict) else []


# ---------- formatting ----------
def _pct(x):
    return "  —  " if x is None else f"{x*100:5.1f}%"


def _delta(x):
    if x is None:
        return "   —  "
    return f"{x*100:+5.1f}"


def _money(x):
    if x is None:
        return "—"
    for u, d in ((1e9, "B"), (1e6, "M"), (1e3, "K")):
        if abs(x) >= u:
            return f"${x/u:.1f}{d}"
    return f"${x:.0f}"


def fmt_row(label, m, tier=""):
    flag = " ⚠thin" if m.get("thin") else ""
    if m.get("resolved"):
        flag += " ⛔RESOLVED"
    elif m.get("expiring"):
        flag += f" ⏳{m['days_left']}d"
    return (f"{label[:34]:34} {tier:5} {_pct(m['yes'])}  Δ1d {_delta(m['d1'])}  Δ7d {_delta(m['d7'])}  "
            f"vol {_money(m['volume']):>7}  liq {_money(m['liquidity']):>7}  ends {m['end']}{flag}")


# ---------- commands ----------
def cmd_search(args):
    for e in search(args.query, args.n):
        mk = e.get("markets", [])
        print(f"\n▸ {e.get('title')}  [{_money(_f(e.get('volume')))}]  slug={e.get('slug')}")
        for m in mk[:6]:
            pm = parse_market(m)
            print(f"    {_pct(pm['yes'])}  {(pm['question'] or '')[:60]:60}  slug={pm['slug']}")


def cmd_market(args):
    m = market_by_slug(args.slug)
    if not m:
        print("not found"); return
    print(json.dumps(m, indent=2) if args.json else fmt_row(m["question"] or m["slug"], m))


def cmd_event(args):
    e = event_by_slug(args.slug)
    if not e:
        print("not found"); return
    print(f"▸ {e['title']}  [{_money(e['volume'])}]")
    for m in sorted(e["markets"], key=lambda x: (x["yes"] or 0), reverse=True):
        q = (m["question"] or m["slug"])[:60]
        print(f"   {_pct(m['yes'])}  Δ7d {_delta(m['d7'])}  {q:60} vol {_money(m['volume']):>7} liq {_money(m['liquidity']):>7}  slug={m['slug']}")


def _read_watchlist():
    rows = []
    if not os.path.exists(WATCHLIST):
        return rows
    with open(WATCHLIST) as fh:
        for line in fh:
            line = line.rstrip("\n")
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < 3:
                continue
            rows.append({"label": parts[0], "type": parts[1], "slug": parts[2],
                         "tier": parts[3] if len(parts) > 3 else "",
                         "route": parts[4] if len(parts) > 4 else ""})
    return rows


def cmd_pull(args):
    wl = _read_watchlist()
    if not wl:
        print(f"watchlist empty/missing: {WATCHLIST}"); return
    ts = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%MZ")
    logrows, out = [], []
    for w in wl:
        try:
            if w["type"] == "event":
                e = event_by_slug(w["slug"])
                mkts = e["markets"] if e else []
                top = sorted(mkts, key=lambda x: (x["yes"] or 0), reverse=True)[:1]
                for m in top:
                    out.append((w["label"] + " (top)", m, w["tier"]))
                    logrows.append((ts, w["slug"], w["label"], w["tier"], m))
            else:
                m = market_by_slug(w["slug"])
                if m:
                    out.append((w["label"], m, w["tier"]))
                    logrows.append((ts, w["slug"], w["label"], w["tier"], m))
        except Exception as e:  # noqa: BLE001
            print(f"  ! {w['label']}: {e}")
    if args.json:
        print(json.dumps([{"label": l, **m} for l, m, _ in out], indent=2));
    else:
        print(f"\nORACLE pull @ {ts}\n" + "-" * 118)
        for l, m, t in sorted(out, key=lambda r: r[2]):
            print(fmt_row(l, m, t))
        exp = [(l, m) for l, m, _ in out if m.get("resolved") or m.get("expiring")]
        if exp:
            print("\n⚠ watchlist maintenance — re-search replacements (see MAINTENANCE.md):")
            for l, m in exp:
                state = "RESOLVED — replace now" if m.get("resolved") else f"resolves in {m['days_left']}d"
                print(f"   - {l}: {state} (end {m['end']})")
    if args.log:
        new = not os.path.exists(ODDS_LOG)
        os.makedirs(os.path.dirname(ODDS_LOG), exist_ok=True)
        with open(ODDS_LOG, "a") as fh:
            if new:
                fh.write("ts\tslug\tlabel\ttier\tyes_prob\tvolume\tliquidity\td1\td7\tend\tthin\n")
            for ts_, slug, label, tier, m in logrows:
                fh.write("\t".join(str(x) for x in [
                    ts_, slug, label, tier, m["yes"], m["volume"], m["liquidity"],
                    m["d1"], m["d7"], m["end"], m["thin"]]) + "\n")
        print(f"\nlogged {len(logrows)} rows → {ODDS_LOG}")


def main():
    ap = argparse.ArgumentParser(description="ORACLE Polymarket fetcher")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search"); s.add_argument("query"); s.add_argument("-n", type=int, default=6); s.set_defaults(fn=cmd_search)
    s = sub.add_parser("market"); s.add_argument("slug"); s.add_argument("--json", action="store_true"); s.set_defaults(fn=cmd_market)
    s = sub.add_parser("event"); s.add_argument("slug"); s.set_defaults(fn=cmd_event)
    s = sub.add_parser("pull"); s.add_argument("--log", action="store_true"); s.add_argument("--json", action="store_true"); s.set_defaults(fn=cmd_pull)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
