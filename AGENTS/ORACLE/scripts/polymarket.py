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
import sys, os, json, argparse, datetime, re
import requests

GAMMA = "https://gamma-api.polymarket.com"
CLOB = "https://clob.polymarket.com"
HERE = os.path.dirname(os.path.abspath(__file__))
ORACLE_DIR = os.path.dirname(HERE)                      # AGENTS/ORACLE
WATCHLIST = os.path.join(ORACLE_DIR, "watchlist.tsv")
ODDS_LOG = os.path.join(ORACLE_DIR, "workbook", "ODDS_LOG.tsv")
HISTORY = os.path.join(ORACLE_DIR, "workbook", "HISTORY.tsv")  # full daily series (CLOB backfill)

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
    toks = m.get("clobTokenIds")
    try:
        toks = json.loads(toks) if isinstance(toks, str) else (toks or [])
    except json.JSONDecodeError:
        toks = []
    end = (m.get("endDate") or "")[:10]
    days_left = None
    if end:
        try:
            days_left = (datetime.date.fromisoformat(end) - datetime.date.today()).days
        except ValueError:
            days_left = None
    # Trust the authoritative `closed` flag — NOT a past endDate. Some live markets
    # (e.g. distribution-event rungs) carry stale endDate metadata in the past while
    # closed=False/active=True and still trading; inferring resolved from days_left<0
    # false-flags those (caught 2026-06-22: China-GDP, unemployment-ladder rungs).
    resolved = bool(m.get("closed"))
    stale_end = (not resolved) and (days_left is not None and days_left < 0)  # past date but still open
    expiring = (not resolved) and days_left is not None and 0 <= days_left <= 7
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
        "stale_end": stale_end,
        "yes_token": toks[0] if toks else None,   # clobTokenIds[0] == YES outcome
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
    elif m.get("stale_end"):
        flag += " ⏮stale-date"   # endDate in the past but still open — ignore the date
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


def clob_history(token, fidelity=1440):
    """Daily YES-price series for a CLOB token. Returns [(date, prob), ...] oldest-first."""
    if not token:
        return []
    # prices-history lives on the CLOB host, not Gamma — call directly
    last = d = None
    for _ in range(3):
        try:
            r = requests.get(CLOB + "/prices-history",
                             params={"market": token, "interval": "max", "fidelity": fidelity}, timeout=25)
            r.raise_for_status()
            d = r.json()
            break
        except Exception as e:  # noqa: BLE001
            last = e; d = None
    if d is None:
        raise last
    out = []
    for p in d.get("history", []):
        try:
            day = datetime.datetime.utcfromtimestamp(p["t"]).strftime("%Y-%m-%d")
            out.append((day, float(p["p"])))
        except (KeyError, TypeError, ValueError):
            continue
    return out


def _spark(series, width=24):
    """ASCII sparkline of a (date,prob) series, sampled to `width` columns, scaled 0-100%."""
    blocks = "▁▂▃▄▅▆▇█"
    vals = [p for _, p in series]
    if not vals:
        return ""
    if len(vals) > width:
        step = len(vals) / width
        vals = [vals[min(len(vals) - 1, int(i * step))] for i in range(width)]
    return "".join(blocks[min(7, max(0, int(round(v * 7))))] for v in vals)  # 0-1 -> 0-7


def _val_days_ago(series, n):
    """Prob at the point nearest `n` days before the last point; None if series too short."""
    if not series:
        return None
    last_day = datetime.date.fromisoformat(series[-1][0])
    target = last_day - datetime.timedelta(days=n)
    best = None
    for day, p in series:
        d = datetime.date.fromisoformat(day)
        if d <= target:
            best = p
    return best


def _traj_stats(series):
    if not series:
        return None
    now = series[-1][1]
    lo = min(p for _, p in series); hi = max(p for _, p in series)
    return {
        "now": now, "created": series[0][1], "created_day": series[0][0],
        "d7": _val_days_ago(series, 7), "d30": _val_days_ago(series, 30), "d90": _val_days_ago(series, 90),
        "lo": lo, "hi": hi, "n": len(series),
        # spiky = wide range AND current sits near the low end (round-tripped)
        "spiky": (hi - lo) > 0.40 and (now - lo) < 0.15,
    }


def cmd_history(args):
    """Backfill + render full daily trajectory for every watchlist market (CLOB prices-history)."""
    wl = _read_watchlist()
    if not wl:
        print(f"watchlist empty/missing: {WATCHLIST}"); return
    rows, allseries = [], []
    for w in wl:
        try:
            if w["type"] == "event":
                e = event_by_slug(w["slug"]); mkts = e["markets"] if e else []
                m = sorted(mkts, key=lambda x: (x["yes"] or 0), reverse=True)[:1]
                m = m[0] if m else None
            else:
                m = market_by_slug(w["slug"])
            if not m or not m.get("yes_token"):
                print(f"  ! {w['label']}: no token"); continue
            series = clob_history(m["yes_token"])
            if not series:
                print(f"  ! {w['label']}: no history"); continue
            s = _traj_stats(series)
            rows.append((w["label"], w["tier"], s, series))
            for day, p in series:
                allseries.append((w["slug"], w["label"], day, p))
        except Exception as e:  # noqa: BLE001
            print(f"  ! {w['label']}: {e}")

    def pp(x):
        return "  — " if x is None else f"{x*100:4.0f}"
    print(f"\nORACLE trajectory — CLOB daily history  (now | Δ30d | Δ90d | since-create | range | spark)\n" + "-" * 110)
    for label, tier, s, series in sorted(rows, key=lambda r: r[1]):
        d30 = None if s["d30"] is None else (s["now"] - s["d30"]) * 100
        d90 = None if s["d90"] is None else (s["now"] - s["d90"]) * 100
        dcr = (s["now"] - s["created"]) * 100
        flag = " ⚡spiky/round-trip" if s["spiky"] else ""
        print(f"{label[:30]:30} {tier:3} {pp(s['now'])}% "
              f"Δ30d {'  — ' if d30 is None else f'{d30:+4.0f}'} "
              f"Δ90d {'  — ' if d90 is None else f'{d90:+4.0f}'} "
              f"since {dcr:+4.0f}({s['created_day'][2:]})  "
              f"[{pp(s['lo'])}-{pp(s['hi'])}] {_spark(series)}{flag}")
    if args.write:
        os.makedirs(os.path.dirname(HISTORY), exist_ok=True)
        with open(HISTORY, "w") as fh:
            fh.write("slug\tlabel\tdate\tyes_prob\n")
            for slug, label, day, p in allseries:
                fh.write(f"{slug}\t{label}\t{day}\t{p}\n")
        print(f"\nwrote {len(allseries)} daily rows ({len(rows)} markets) → {HISTORY}")


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


_ONDATE_RE = re.compile(
    r"\bon\s+(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s+\d{1,2}\b", re.I)


def _is_daily_ondate(mkts):
    """True for a genuine daily 'on <Month> <day>?' event series (Iran-shipping,
    Gulf-state), where each leg is an INDEPENDENT single-day question. Distinguishes
    them from by-date CUMULATIVE ladders ('...by July 31?') and distribution/component
    events (CPI/unemployment rungs), which must keep the modal-leg behavior."""
    return sum(1 for m in mkts
               if m.get("question") and _ONDATE_RE.search(m["question"])) >= 3


def _select_event_leg(mkts):
    """Pick the representative leg for an event-type watchlist entry.

    - Daily on-date series -> the CURRENT (today, else nearest-upcoming, else
      nearest-past) UNRESOLVED leg. Fixes the display quirk where an old settled
      100%-YES leg was chosen by max-probability, hiding the live daily tempo
      (surfaced 2026-07-24: Iran-vs-Gulf-State read ⛔RESOLVED while today's leg
      was live at ~47%). Returns suffix ' (current)'.
    - Everything else (by-date cumulative, distribution/component, undated) ->
      the modal (max-probability) leg, ' (top)'. Unchanged behavior.

    Returns (market_or_None, label_suffix)."""
    if not mkts:
        return None, ""
    if _is_daily_ondate(mkts):
        live = [m for m in mkts
                if not m.get("resolved") and m.get("days_left") is not None]
        if live:
            pick = min(live, key=lambda m: (0 if m["days_left"] >= 0 else 1,
                                            abs(m["days_left"])))
            pick["_daily"] = True  # suppress the always-expiring maintenance flag
            return pick, " (current)"
        # all legs resolved -> fall through so the RESOLVED maintenance flag fires
    return max(mkts, key=lambda x: (x["yes"] or 0)), " (top)"


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
                m, suf = _select_event_leg(mkts)
                if m:
                    out.append((w["label"] + suf, m, w["tier"]))
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
        exp = [(l, m) for l, m, _ in out
               if (m.get("resolved") or m.get("expiring")) and not m.get("_daily")]
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


# --- `movers` discovery: macro/finance/geopolitics filter; skip sports/elections noise ---
MOVERS_INCLUDE = (
    "fed", "interest rate", "rate cut", "rate hike", "inflation", "cpi", "pce", "recession", "gdp",
    "unemploy", "jobless", "payroll", "bank", "bailout", "default", "debt ceiling", "treasury", "yield",
    "credit", "powell", "tariff", "trade deal", "trade war", "trump", "economy", "stock", "s&p", "sp 500",
    "nasdaq", "dow", "vix", "gold", "silver", "oil", "wti", "brent", "opec", "bitcoin", "btc", "ethereum",
    "eth", "crypto", "microstrategy", "mstr", "china", "taiwan", "russia", "ukraine", "iran", "israel",
    "north korea", "venezuela", "nuclear", "ceasefire", "war", "strike", "hormuz", "invade", "shutdown",
    "supreme court", "greenland", "gaza", "hezbollah", "houthi", "nato", "sanction", "fannie", "freddie",
    "moody", "downgrade", "emergency", "quantitative", "mortgage", "housing", "layoff", "hurricane",
    "dollar", "yuan", "yen", "copper", "opec", "saudi", "fed funds",
)
MOVERS_EXCLUDE = (
    "world cup", "fifa", "win the", "super bowl", " nba", " nfl", " mlb", " nhl", "premier league",
    "champions league", "ballon", "mvp", "grand prix", " f1 ", "tennis", "golf", "ufc", "boxing",
    "olympic", "oscar", "grammy", "album", "movie", "box office", "rotten tomato", "nobel",
    "time person", " vs ", " vs.", "epstein", "nomination", "prime minister", "president of",
    "presidential election", "speaker of", "mayor", "governor", "senate seat", "parliament",
    "coach", "manager", "up or down", "up/down",  # daily coin-flip direction bets = noise
    # daily/sports/misc noise that leaked through --all (matched against question + slug):
    "temperature", "rainfall", "win by", "o/u", "total games", "games total", "the fight",
    " rounds", "earthquake", "trailer", "npb", "cs2-", "atp-", "wta-", "-lol-", "dota",
)


def cmd_movers(args):
    """Discover the biggest-moving markets we are NOT already tracking. Queries Gamma
    ordered directly by price-change (catches news-reactive movers regardless of lifetime
    volume), filters to our domain, excludes sports/elections, and flags near-resolve
    (likely-mechanical) convergence so it doesn't read as signal."""
    known = {w["slug"] for w in _read_watchlist()}
    rows, seen = {}, set()
    for field in ("oneDayPriceChange", "oneWeekPriceChange"):
        for asc in ("false", "true"):
            try:
                d = _get("/markets", {"closed": "false", "active": "true",
                                      "order": field, "ascending": asc, "limit": args.scan})
            except Exception:  # noqa: BLE001
                continue
            for m in (d or []):
                slug = m.get("slug") or ""
                if not slug or slug in seen:
                    continue
                if slug in known and not args.tracked:
                    continue
                q = (m.get("question") or "").lower()
                # check EXCLUDE against question + slug (sports/esports markets often have a
                # generic question like "O/U 1.5 Rounds" — the league is only in the slug)
                hay = q + " " + slug.lower().replace("-", " ")
                if any(x.replace("-", " ") in hay for x in MOVERS_EXCLUDE):
                    continue
                if not args.all and not any(x in q for x in MOVERS_INCLUDE):
                    continue
                pm = parse_market(m)
                if pm["yes"] is None:
                    continue
                if (pm["liquidity"] or 0) < args.min_liq and (pm["volume"] or 0) < args.min_vol:
                    continue
                mv = max(abs(pm["d1"] or 0), abs(pm["d7"] or 0))
                if mv < args.min / 100.0:
                    continue
                seen.add(slug)
                rows[slug] = (mv, pm)
    ranked = sorted(rows.values(), key=lambda r: -r[0])
    scope = "ALL non-sports" if args.all else "domain (macro/finance/geopolitics)"
    print(f"Polymarket movers — {scope}; ≥{args.min:g}pp 1d|7d; liq≥${args.min_liq/1000:.0f}K or vol≥${args.min_vol/1000:.0f}K"
          + ("; incl. tracked" if args.tracked else "; excl. tracked") + f"  [{len(ranked)} hits]\n")
    print(f"{'YES':>6} {'Δ1d':>6} {'Δ7d':>6} {'vol':>7} {'liq':>7}  question  [slug]")
    print("-" * 124)
    for mv, pm in ranked[:args.top]:
        flag = ""
        if pm.get("resolved"):
            flag = " ⛔res"
        elif pm.get("days_left") is not None and 0 <= pm["days_left"] <= 3:
            flag = f" ⚙{pm['days_left']}d"   # near-resolve → likely mechanical convergence, not signal
        print(f"{_pct(pm['yes'])} {_delta(pm['d1'])} {_delta(pm['d7'])} "
              f"{_money(pm['volume']):>7} {_money(pm['liquidity']):>7}  "
              f"{(pm['question'] or '')[:60]}{flag}  [{(pm['slug'] or '')[:40]}]")
    if not ranked:
        print("(no movers cleared the filters — try --min 3, --all, or --tracked)")
    elif not args.all:
        print("\n⚙ = resolves ≤3d (likely mechanical convergence, eyeball not signal). "
              "--all drops the domain filter · --tracked includes watchlist markets.")


# --- `coverage` sweep: the INVERSE of `movers`. movers ranks by price-CHANGE (blind to
#     slow-repricing deep markets); coverage ranks the full active universe by DEPTH
#     (liquidity/volume, movement-agnostic) and subtracts what we already track, to surface
#     large real-money markets on themes we don't cover yet. Built 2026-07-22 after a $2.3M
#     CLARITY-Act market drifted for weeks uncaught (see MAINTENANCE). Review-only: it
#     NOMINATES themes for a human to confirm + route + pin — it never auto-pins (novelty
#     markets are deep, so auto-pinning would bloat the watchlist). ---
COVERAGE_EXCLUDE = (
    "jesus", "christ", "second coming", "rapture", "the bible", "antichrist",
    "alien", "ufo", "extraterrestrial", "bigfoot", "loch ness", "nessie", "ghost",
    "champions photo", "wc champions", "person of the year", "time person",
    "gta", "grand theft", "taylor swift", "kanye", "pregnant", "divorce", "engaged",
)


def cmd_coverage(args):
    """Coverage sweep: surface the DEEPEST active markets we do NOT already track, ranked by
    liquidity (movement-agnostic), so slow-repricing deep markets on un-tracked themes don't
    stay invisible the way the CLARITY Act did. Excludes sports/novelty; review-only —
    NOMINATE for a human to confirm relevance + pin, never auto-pin."""
    known = {w["slug"] for w in _read_watchlist()}
    seen, rows = set(), {}
    for field in ("liquidityNum", "volumeNum"):
        try:
            d = _get("/markets", {"closed": "false", "active": "true",
                                  "order": field, "ascending": "false", "limit": args.scan})
        except Exception:  # noqa: BLE001
            continue
        for m in (d or []):
            slug = m.get("slug") or ""
            if not slug or slug in seen:
                continue
            if slug in known and not args.tracked:
                continue
            q = (m.get("question") or "").lower()
            hay = q + " " + slug.lower().replace("-", " ")
            if any(x.replace("-", " ") in hay for x in MOVERS_EXCLUDE + COVERAGE_EXCLUDE):
                continue
            # coverage deliberately does NOT apply MOVERS_INCLUDE by default — the whole point
            # is to find themes OUTSIDE our known keyword set. --domain restricts to known ones.
            if args.domain and not any(x in q for x in MOVERS_INCLUDE):
                continue
            pm = parse_market(m)
            if pm["yes"] is None or pm["resolved"]:
                continue
            if (pm["liquidity"] or 0) < args.min_liq:
                continue
            seen.add(slug)
            rows[slug] = pm
    ranked = sorted(rows.values(), key=lambda p: -(p["liquidity"] or 0))
    scope = "domain keywords only" if args.domain else "ALL themes (ex-sports/novelty)"
    print(f"Polymarket COVERAGE sweep — un-tracked active markets, {scope}; liq≥${args.min_liq/1000:.0f}K"
          + ("; incl. tracked" if args.tracked else "") + f"  [{len(ranked)} hits]\n")
    print(f"{'liq':>8} {'vol':>9} {'YES':>6} {'Δ7d':>6}  {'ends':>10}  question  [slug]")
    print("-" * 128)
    for pm in ranked[:args.top]:
        flag = ""
        if pm.get("days_left") is not None and 0 <= pm["days_left"] <= 3:
            flag = f" ⚙{pm['days_left']}d"   # near-resolve → mechanical, not a real coverage gap
        print(f"{_money(pm['liquidity']):>8} {_money(pm['volume']):>9} {_pct(pm['yes'])} {_delta(pm['d7'])}  "
              f"{(pm['end'] or '—'):>10}  {(pm['question'] or '')[:52]}{flag}  [{(pm['slug'] or '')[:36]}]")
    if not ranked:
        print("(nothing un-tracked cleared the liquidity floor — try --min-liq 10000)")
    else:
        print("\nReview-only: NOMINATE new themes → confirm relevance w/ the owning agent → pin. "
              "Never auto-pin (novelty markets are deep). --domain restricts to known keywords · --tracked includes pinned.")


def main():
    ap = argparse.ArgumentParser(description="ORACLE Polymarket fetcher")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search"); s.add_argument("query"); s.add_argument("-n", type=int, default=6); s.set_defaults(fn=cmd_search)
    s = sub.add_parser("market"); s.add_argument("slug"); s.add_argument("--json", action="store_true"); s.set_defaults(fn=cmd_market)
    s = sub.add_parser("event"); s.add_argument("slug"); s.set_defaults(fn=cmd_event)
    s = sub.add_parser("pull"); s.add_argument("--log", action="store_true"); s.add_argument("--json", action="store_true"); s.set_defaults(fn=cmd_pull)
    s = sub.add_parser("history"); s.add_argument("--write", action="store_true"); s.set_defaults(fn=cmd_history)
    s = sub.add_parser("movers")
    s.add_argument("--min", type=float, default=5.0, help="min 1d|7d move in pp (default 5)")
    s.add_argument("--top", type=int, default=30, help="rows to show (default 30)")
    s.add_argument("--scan", type=int, default=250, help="markets per Gamma query (default 250)")
    s.add_argument("--min-liq", type=float, default=5000.0, dest="min_liq")
    s.add_argument("--min-vol", type=float, default=30000.0, dest="min_vol")
    s.add_argument("--all", action="store_true", help="drop the domain filter (still skips sports/elections)")
    s.add_argument("--tracked", action="store_true", help="include markets already in watchlist")
    s.set_defaults(fn=cmd_movers)
    s = sub.add_parser("coverage", help="INVERSE of movers: deepest UN-tracked markets by liquidity (find new themes)")
    s.add_argument("--min-liq", type=float, default=25000.0, dest="min_liq", help="liquidity floor (default $25K)")
    s.add_argument("--top", type=int, default=30, help="rows to show (default 30)")
    s.add_argument("--scan", type=int, default=400, help="markets per Gamma query (default 400)")
    s.add_argument("--domain", action="store_true", help="restrict to known domain keywords (default: ALL themes)")
    s.add_argument("--tracked", action="store_true", help="include markets already in watchlist")
    s.set_defaults(fn=cmd_coverage)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
