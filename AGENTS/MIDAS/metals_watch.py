#!/usr/bin/env python3
"""
metals_watch.py — MIDAS boot-time instrument: real yield + metals spot + GSR
+ M1 divergence flag.

Built 2026-07-12 (first real session, Will-directed priority build). Thin
wrapper over the shared FORGE market-data client (FORGE/tools/market-data/
fetch.py) — imported by absolute self-location, per WATT/power_watch.py's
precedent (see that file's header + FORGE README "shared client" note). If
fetch.py itself needs extending, that is a FORGE edit — flag to PROME, don't
fork it here.

SCOPE: real yield (FRED DFII10 MIRROR, latest-revised) + named gold/silver/
copper/platinum/palladium vendor daily bars. FRONT_MONTHS supplies the exact
contracts; GC=F/SI=F/HG=F/PL=F/PA=F are diagnostic pointers only. The newest
futures history row is excluded because its volume is duplicated. Vendor
Close is not a certified exchange settlement. ETF proxies are a secondary
quote row. GSR binds to same-date, same-delivery-month named contracts. The
M1 divergence classifier uses one named gold contract throughout (gold trend vs
real-yield trend over a trailing ~90-day window — CONVERGE = real-rate-
consistent; DIVERGE = gold holding/rising through rising real yields).
These sign patterns do not identify a debasement premium or a regime change.

LME COPPER INVENTORY LEG (round-2 2026-07-12; BASELINE DEFINED round-3):
westmetall.com publishes the LME copper stock series (daily) in a plain
server-rendered HTML table — scraped with a browser UA, fail-loud. Closes the
"no free LME source" wall (CME warehouseStockAPI 403'd; LME.com vendor-gated).
Round-3: the CLAUDE.md threshold "+X% vs normal" now grades against a DEFINED
baseline — the trailing-2yr rolling MEDIAN of daily LME stock (read_lme_copper_
baseline pulls current + 2 prior years via westmetall &year= pages). As of
2026-07-12: 2yr median ~239,400 t (n=507); latest 306,500 t [7/10] = +28% =
just into the Yellow band (+25%) — but the RED demand-collapse fire needs the
CONJUNCTION (copper -20% AND inv +100%), and inventory is FALLING off the 4/15
peak while price is UP, so it is NOT firing. Cross-check: westmetall LME cash
$13,408.50/t [7/10] vs COMEX HG=F $6.28/lb=$13,845/t (~3% premium, consistent).

POLARITY — FLIPPED 2026-07-17 (both catalyst tests resolved, M1 v2 SURVIVED):
The polarity was FROZEN (CONVERGE=REVIEW) through the two M1 v2 catalyst tests.
Both resolved this week and v2 survived: MIDAS-03 (CPI 7/14) — gold stayed
re-coupled to real rates (yields near series-high 2.36 [7/13], gold capped/fell
over the CPI week, no debasement-premium reassertion) = v2-consistent; MIDAS-04
(China GDP 4.3% miss, NBS 7/15) — gold did NOT do a haven spike on the miss
(GC=F -0.42% on 7/15), copper held (no I1 fire) = v2 not falsified. Per the
Will-approved conditional, the polarity is now INVERTED: CONVERGE (gold
re-coupled, moving inversely to real rates) = the EXPECTED/quiet baseline (rc=0);
DIVERGE (gold holding/rising THROUGH rising real yields = premium reassertion,
v2 kill-cond #3) = the REVIEW trigger (rc=1). See the verdict block + SCRATCH.md.

OUT OF SCOPE FOR THIS SCRIPT:
  - CFTC COT is checked by separate gold and Ag/Pt/Pd boot legs. Copper
    positioning remains manual. Do not mistake separation for absent wiring.
  - Copper vs 200dma (I1 threshold table) — needs a 200-trading-day history
    pull; scoped OUT of this first increment (kept to the SCRATCH-specified
    spot+yield+GSR legs). Computed manually this session (see STATUS.md);
    candidate next increment.

Exit codes: 0 = quiet · 1 = REVIEW (GSR band crossed, OR M1 = DIVERGE — gold
holding/rising THROUGH rising real yields = debasement-premium reassertion;
post the 2026-07-17 polarity flip, CONVERGE [gold re-coupled/inverse to real
rates] is the QUIET baseline and no longer trips REVIEW) · 2 = a leg failed
(fail-LOUD, never fabricated — a missing leg prints ERROR and is excluded from
the verdict, it is never silently treated as zero/neutral).

Usage (self-locating, works from any cwd):
  python3 /home/willi/Research-workspace/AGENTS/MIDAS/metals_watch.py
"""

import re
import math
import statistics
import sys
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

# Self-locate the shared FORGE client regardless of cwd.
# This file lives at AGENTS/MIDAS/metals_watch.py -> parents[2] == repo root.
_FORGE_MD = Path(__file__).resolve().parents[2] / "FORGE" / "tools" / "market-data"
sys.path.insert(0, str(_FORGE_MD))
import fetch  # noqa: E402

FUTURES = {"GC=F": "Gold fut", "SI=F": "Silver fut", "HG=F": "Copper fut",
           "PL=F": "Platinum fut", "PA=F": "Palladium fut"}
ETF_PROXIES = {"GLD": "Gold ETF", "SLV": "Silver ETF", "CPER": "Copper ETF",
               "PPLT": "Platinum ETF", "PALL": "Palladium ETF"}

# --- Contract-identity guard (KB-112, L-50; PROME ruling 2026-09-05 + 2026-09-10
# route (i): a LOCAL volume pull, because FORGE `fetch.py price` returns no volume
# field — 7th instance of KB-047. When `fetch.py` gains one, this may be retired.)
#
# Every `=F` pointer above is a CONTINUOUS pointer, and the vendor leaves it on a
# DYING contract for weeks: at the 9/4 2026 settles `GC=F` traded 16 lots against
# `GCZ26`'s 209,167, and all five pointers were on expiring months (level spreads
# 0.27%-1.30%). The discriminator is VOLUME, not price.
#
# ⛔ TWO RULES BOUGHT BY PUBLISHED ERRORS, both encoded below:
#   1. NEVER identify a contract from the NEWEST futures bar. The vendor duplicates
#      the prior session's volume into the latest futures row only, and it self-heals
#      on the next session's pull (9/1 GCZ26 read 152,216 on 9/2, 198,560 on 9/5;
#      re-confirmed 9/11: the 9/10 row carried 9/9's volume on all five months).
#      => grade on the PRIOR settled session's row, index -2.
#   2. The explicit front month is HAND-MAINTAINED and must be rolled by a human.
#      A stale map does not fail loudly on its own — it just stops discriminating —
#      so the guard prints the map's month with every verdict.
#      ROLL LOG: PL PLV26 -> PLF27 on 2026-10-01 (volume crossed 9/25: PLF27 20,612 vs
#      PLV26 16,740; by 9/29 PLV26 1,005 vs PLF27 21,847, and PL=F had followed PLV26,
#      so the stale map graded a DYING contract "OK" at 100% share — the failure above).
#      REVIEW 2026-10-23 (prior row 10/22, mapped vs next month volume): GCZ26 149,523 vs
#      GCG27 9,773 · SIZ26 33,192 vs SIH27 3,108 · HGZ26 37,443 vs HGH27 8,700 · PLF27
#      17,237 vs PLJ27 1,283 · PAZ26 6,880 vs PAH27 377 -> map unchanged. Dec contracts
#      roll before late-November first notice; watch HG (lead only 4.3x).
FRONT_MONTHS = {"GC=F": "GCZ26.CMX", "SI=F": "SIZ26.CMX", "HG=F": "HGZ26.CMX",
                "PL=F": "PLF27.NYM", "PA=F": "PAZ26.NYM"}
FRONT_MONTHS_REVIEW_ON = "2026-10-30"  # chosen weekly maintenance date, not an expiry
MAX_PRIOR_BAR_AGE_DAYS = 7  # source freshness bound, not a market alarm level
# A pointer carrying under this share of the explicit month's volume is DYING.
DYING_VOL_SHARE = 0.05


def contract_month(ticker):
    """Read a named futures delivery month; never infer the current liquid month."""
    match = re.search(r"([FGHJKMNQUVXZ])(\d{2})(?:\.|$)", ticker)
    if not match:
        raise ValueError(f"unnamed delivery month: {ticker}")
    return 2000 + int(match[2]), "FGHJKMNQUVXZ".index(match[1]) + 1


def contract_map_review(today=None):
    """Administrative weekly review, independent of the market's alarm bands."""
    today = today or datetime.now(ZoneInfo("America/New_York")).date()
    notes = []
    if today >= date.fromisoformat(FRONT_MONTHS_REVIEW_ON):
        notes.append(f"Mapped contracts need the owner review dated {FRONT_MONTHS_REVIEW_ON}.")
    for ptr, front in FRONT_MONTHS.items():
        try:
            if (today.year, today.month) > contract_month(front):
                notes.append(f"{ptr}: mapped delivery month has passed ({front}); do not grade this contract.")
        except ValueError as exc:
            notes.append(str(exc))
    return notes


def _prior_vendor_bar(data):
    """Conservative T+1 bar. Exclude the newest row's duplicated volume."""
    if "error" in data:
        raise ValueError(data["error"])
    bars = data.get("history", [])
    if len(bars) < 2:
        raise ValueError("fewer than two bars; prior vendor row unavailable")
    dates = [date.fromisoformat(b["date"]) for b in bars]
    if any(a >= b for a, b in zip(dates, dates[1:])):
        raise ValueError("vendor bar dates are duplicate or unordered")
    bar = bars[-2]
    if not math.isfinite(float(bar["close"])) or bar["close"] <= 0:
        raise ValueError("prior vendor Close is not a positive finite value")
    return bar


def read_contract_history(tickers, days=12):
    """Keep native futures tick precision for the binding ratio/volume snapshot.

    FORGE price_history rounds every Close to two decimals. That rounds away
    silver/copper ticks; the narrow local adapter retains vendor Close and
    Volume without changing the shared client. Long-window gold/GLD history
    still uses FORGE. No settlement certification is implied.
    """
    import yfinance as yf
    result = {}
    for ticker in tickers:
        try:
            frame = yf.Ticker(ticker).history(period=f"{days}d", auto_adjust=False).sort_index()
            if frame.empty or frame["Close"].isna().any():
                raise ValueError("empty history or a null Close; no prior-row certification")
            result[ticker] = {"history": [dict(date=str(idx.date()), close=float(row["Close"]),
                                               volume=int(row["Volume"])) for idx, row in frame.iterrows()]}
        except Exception as exc:
            result[ticker] = {"error": str(exc)}
    return result


def read_contract_snapshot(front_months=None, history=None, today=None):
    """Bind prices to named contracts; pointers are diagnostic only.

    A failed pointer cannot replace a named-contract price. A failed named
    contract is UNKNOWN even when its pointer happens to return a quote.
    """
    front_months = FRONT_MONTHS if front_months is None else front_months
    today = today or datetime.now(ZoneInfo("America/New_York")).date()
    if history is None:
        history = read_contract_history(list(dict.fromkeys([*front_months, *front_months.values()])), days=12)
    primary, rows, flags = {}, [], []
    for ptr, front in front_months.items():
        b = history.get(front, {"error": "named-contract history absent"})
        try:
            if not front.startswith(ptr.split("=")[0]):
                raise ValueError(f"contract does not identify the expected metal: {ptr} -> {front}")
            if (today.year, today.month) > contract_month(front):
                raise ValueError(f"mapped contract month has passed: {front}")
            br = _prior_vendor_bar(b)
            if date.fromisoformat(br["date"]) > today:
                raise ValueError("prior vendor bar is future-dated")
            if (today - date.fromisoformat(br["date"])).days > MAX_PRIOR_BAR_AGE_DAYS:
                raise ValueError(f"prior vendor bar is older than {MAX_PRIOR_BAR_AGE_DAYS} calendar days")
            if br.get("volume", 0) <= 0:
                raise ValueError("named-contract prior volume is absent or zero")
            previous = b["history"][-3]["close"] if len(b["history"]) >= 3 else None
            primary[ptr] = dict(contract=front, date=br["date"], price=br["close"],
                                prev=previous, volume=br["volume"],
                                change_pct=(br["close"] / previous - 1) * 100 if previous else None)
        except (ValueError, KeyError, TypeError) as exc:
            primary[ptr] = dict(contract=front, error=str(exc))
        try:
            a = history.get(ptr, {"error": "pointer history absent"})
            ar, br = _prior_vendor_bar(a), _prior_vendor_bar(b)
            if ar["date"] != br["date"]:
                raise ValueError(f"prior-row dates disagree: {ar['date']} vs {br['date']}")
            pv, fv = ar["volume"], br["volume"]
            spread = (ar["close"] / br["close"] - 1) * 100
            state = "UNKNOWN" if fv <= 0 else ("DYING" if pv < DYING_VOL_SHARE * fv else "OK")
            rows.append((ptr, front, ar["date"], pv, fv, ar["close"], br["close"], spread, state))
            if state != "OK":
                flags.append(ptr)
        except (ValueError, KeyError, TypeError) as exc:
            rows.append((ptr, front, None, None, None, None, None, None, f"UNKNOWN ({exc})"))
            flags.append(ptr)
    return primary, rows, flags


def primary_gsr(primary):
    """Same-date, same-delivery-month USD/oz ratio from named contracts only."""
    g, s = primary.get("GC=F", {}), primary.get("SI=F", {})
    if "error" in g or "error" in s or not g or not s:
        raise ValueError("named gold or silver contract is unavailable")
    if g["date"] != s["date"]:
        raise ValueError(f"gold/silver dates disagree: {g['date']} vs {s['date']}")
    if contract_month(g["contract"]) != contract_month(s["contract"]):
        raise ValueError("gold/silver delivery months disagree; no GSR band grade")
    return g["price"] / s["price"]


def copper_conjunction_context(inventory_pct):
    """Report the measured inventory leg without manufacturing a price leg."""
    state = "REACHED" if inventory_pct >= LME_RED else "CLEAR"
    return (f"Inventory leg {state}: {inventory_pct:+.1f}% vs dated median; boundary +{LME_RED}%. "
            "Copper price leg UNMEASURED here; the full price/inventory conjunction is not graded.")


def measure_three_week(obs, gld_history, end):
    """The existing endpoint shape requires GLD; never fall back to a roll."""
    if "error" in gld_history:
        raise ValueError(f"GLD arbiter unavailable: {gld_history['error']}")
    obs = sorted((o for o in obs if o.get("value") not in (None, "", ".") and o["date"] <= end),
                 key=lambda o: o["date"], reverse=True)
    if not obs:
        raise ValueError("no DFII10 observation by the named ending date")
    latest_y = obs[0]
    latest_d = date.fromisoformat(latest_y["date"])
    y_then = next((o for o in obs if (latest_d - date.fromisoformat(o["date"])).days >= 21), None)
    if y_then is None:
        raise ValueError("fewer than 21 calendar days of yield history")
    bars = gld_history.get("history", [])

    def price_asof(dt):
        prior = [b for b in bars if b["date"] <= dt]
        if not prior:
            raise ValueError(f"GLD has no bar at or before {dt}")
        b = max(prior, key=lambda b: b["date"])
        if not math.isfinite(float(b["close"])) or b["close"] <= 0:
            raise ValueError(f"GLD Close is invalid on {b['date']}")
        return b

    a, b = price_asof(y_then["date"]), price_asof(latest_y["date"])
    dy_bp = round((float(latest_y["value"]) - float(y_then["value"])) * 100)
    return dict(latest_y=latest_y, y_then=y_then, gld_start=a, gld_end=b,
                dy_bp=dy_bp, return_pct=(b["close"] / a["close"] - 1) * 100)


def measure_weekly_shape(obs, gld_history, end, calendar_as_of=None):
    """Apply the already-ruled three-Friday-interval endpoint basis (L-12).

    Non-publication days use the last common observation by that Friday.
    Print the actual common dates; do not call a four-week-old row a close.
    """
    if "error" in gld_history:
        raise ValueError(f"GLD arbiter unavailable: {gld_history['error']}")
    yields = {o['date']: o for o in obs if o.get('value') not in (None, '', '.') and o['date'] <= end}
    prices = {b['date']: b for b in gld_history.get('history', []) if b.get('close') is not None}
    common = sorted(yields.keys() & prices.keys())
    # The Friday clock belongs to the capture, not the latest published yield.
    # A Friday with a missing publication uses its prior common observation.
    end_date = date.fromisoformat(calendar_as_of or end)
    friday = end_date - timedelta(days=(end_date.weekday() - 4) % 7)
    points = []
    for offset in [21, 14, 7, 0]:
        nominal = friday - timedelta(days=offset)
        available = [d for d in common if d <= nominal.isoformat()]
        if not available:
            raise ValueError(f"no common GLD/DFII10 observation by Friday {nominal}")
        actual = available[-1]
        if (nominal - date.fromisoformat(actual)).days > MAX_PRIOR_BAR_AGE_DAYS:
            raise ValueError(f"common observation by Friday {nominal} is stale")
        price = prices[actual]['close']
        if not math.isfinite(float(price)) or price <= 0:
            raise ValueError(f"invalid GLD Close on {actual}")
        points.append(dict(friday=nominal.isoformat(),date=actual,yield_pct=float(yields[actual]['value']),gld=price))
    if len({p['date'] for p in points}) != 4:
        raise ValueError("four distinct weekly endpoint observations are required")
    dy_bp = round((points[-1]['yield_pct'] - points[0]['yield_pct']) * 100)
    ret = (points[-1]['gld'] / points[0]['gld'] - 1) * 100
    weeks = [dict(start=a['date'],end=b['date'],dy_bp=round((b['yield_pct']-a['yield_pct'])*100),
                  return_pct=(b['gld']/a['gld']-1)*100,
                  joint_up=b['yield_pct']>a['yield_pct'] and b['gld']>a['gld']) for a,b in zip(points,points[1:])]
    return dict(points=points,dy_bp=dy_bp,return_pct=ret,weekly_signs=weeks,
                endpoint_shape=dy_bp>0 and ret>0,weekly_continuous=all(w['joint_up'] for w in weeks))


def check_contract_identity(front_months=None):
    """Is each `=F` pointer sitting on the liquid front month, or a dying one?

    Returns (rows, flags). `rows` is one tuple per pointer:
        (pointer, front, asof_date, ptr_vol, front_vol, ptr_close, front_close,
         spread_pct, state)
    `state` is DYING / OK / UNKNOWN. `flags` lists the DYING pointers.

    Fail-LOUD: a pointer whose history cannot be pulled is UNKNOWN and is listed,
    never silently treated as OK. An absent discriminator is not a clean bill."""
    _, rows, flags = read_contract_snapshot(front_months)
    return rows, flags


# GSR bands (MIDAS CLAUDE.md THRESHOLDS table)
GSR_YELLOW, GSR_ORANGE, GSR_RED = 85, 90, 95

WESTMETALL_CU_URL = ("https://www.westmetall.com/en/markdaten.php"
                     "?action=table&field=LME_Cu_cash")
BROWSER_UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

# LME copper inventory bands (MIDAS CLAUDE.md THRESHOLDS: "+X% vs normal").
# "normal" is now DEFINED (round-3, KB-018) as the trailing-2yr rolling MEDIAN
# of daily LME stock — not an undefined baseline. Bands per the CLAUDE.md table.
LME_YELLOW, LME_ORANGE, LME_RED = 25, 50, 100  # % above the 2-yr median


def _parse_westmetall_table(html):
    """Extract [(datetime, tonnes)] from a westmetall LME_Cu table page.
    Only rows matching 'DD. Month YYYY' with a numeric stock cell — anything
    else is skipped, never guessed."""
    out = []
    for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", html, re.S):
        cells = [re.sub(r"<[^>]+>", "", c).strip()
                 for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", tr, re.S)]
        if len(cells) == 4 and re.match(r"\d{2}\.\s", cells[0]):
            try:
                dt = datetime.strptime(cells[0], "%d. %B %Y")
                out.append((dt, cells[0], int(cells[3].replace(",", ""))))
            except ValueError:
                continue
    return out


def _fetch_westmetall(url):
    req = urllib.request.Request(url, headers={"User-Agent": BROWSER_UA})
    with urllib.request.urlopen(req, timeout=25) as r:
        return r.read().decode("utf-8", errors="replace")


def read_lme_copper_baseline():
    """Trailing-2yr median baseline for LME copper stock. Fetches the current
    table plus the two prior calendar years (westmetall &year= pages), builds
    a daily series, and returns (median_2yr, n_obs_in_window, latest_dt).
    Fail-loud: raises if the combined series is too short to define a baseline.
    Best-effort on the history legs — if a prior-year page fails, it degrades
    to whatever depth it got AND flags it, rather than silently under-sampling
    (caller sees n_obs and can judge)."""
    latest_year = datetime.now().year
    combined = []
    fetched_years = []
    for yr in (latest_year, latest_year - 1, latest_year - 2):
        url = WESTMETALL_CU_URL + (f"&year={yr}" if yr != latest_year else "")
        try:
            combined += _parse_westmetall_table(_fetch_westmetall(url))
            fetched_years.append(yr)
        except Exception:
            continue  # degrade, don't fail the whole baseline on one bad year
    if len(combined) < 60:
        raise ValueError(f"LME baseline: only {len(combined)} obs across "
                         f"years {fetched_years} — insufficient for a 2yr median")
    combined.sort(key=lambda t: t[0])
    latest_dt = combined[-1][0]
    cutoff = latest_dt.timestamp() - 730 * 86400
    window = [v for dt, _, v in combined if dt.timestamp() >= cutoff]
    return statistics.median(window), len(window), latest_dt


def read_lme_copper_stocks():
    """LME copper warehouse stocks (tonnes) scraped from westmetall.com's
    public daily table (columns: date | cash | 3-month | stock). Returns
    (rows_newest_first, latest, oldest) where each row = (date_str, tonnes).
    Fail-loud: raises on HTTP failure or if the table shape isn't recognized
    (never fabricates a value)."""
    html = _fetch_westmetall(WESTMETALL_CU_URL)
    trs = re.findall(r"<tr[^>]*>(.*?)</tr>", html, re.S)
    data = []
    for tr in trs:
        cells = [re.sub(r"<[^>]+>", "", c).strip()
                 for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", tr, re.S)]
        if len(cells) == 4 and re.match(r"\d{2}\.\s", cells[0]):
            try:
                data.append((cells[0], int(cells[3].replace(",", ""))))
            except ValueError:
                continue  # non-numeric stock cell (header/blank) — skip, don't guess
    if len(data) < 5:
        raise ValueError(f"westmetall LME table parse got only {len(data)} rows — "
                         f"layout may have changed, check {WESTMETALL_CU_URL}")
    return data, data[0], data[-1]


def read_real_yield():
    """Latest DFII10 + a ~90-calendar-day-prior print for the divergence calc.
    Fail-loud: raises if fetch.py returns an error row or too few observations."""
    obs = fetch.fred_fetch("DFII10", limit=100)
    if obs and "error" in obs[0]:
        raise ValueError(f"FRED DFII10 fetch failed: {obs[0]['error']}")
    if len(obs) < 2:
        raise ValueError(f"FRED DFII10: too few observations ({len(obs)})")
    latest = obs[0]  # newest-first
    target = None
    # obs is newest->oldest; find first obs whose date is <= 90 days before latest
    from datetime import date as _date
    latest_d = _date.fromisoformat(latest["date"])
    for o in obs:
        d = _date.fromisoformat(o["date"])
        if (latest_d - d).days >= 88:
            target = o
            break
    if target is None:
        target = obs[-1]  # fall back to oldest available
    return latest, target


def read_spot(tickers_map):
    """price_fetch wrapper — raises if EVERY ticker errored (total fetch failure);
    partial failures are reported per-ticker (fail-loud, not silently dropped)."""
    results = fetch.price_fetch(list(tickers_map.keys()))
    if all("error" in d for d in results.values()):
        raise ValueError(f"ALL spot tickers failed: {results}")
    return results


def main():
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print(f"{'=' * 72}\n  METALS WATCH — fetched {now_utc}\n{'=' * 72}")

    failures = []

    # --- 1. Real yield (FRED DFII10) ---
    latest_y = target_y = None
    try:
        latest_y, target_y = read_real_yield()
        print(f"\n  REAL YIELD (FRED DFII10 MIRROR, latest-revised; T+1 publication lag):")
        print(f"    Latest: {latest_y['value']} [{latest_y['date']}]")
        print(f"    ~90d prior: {target_y['value']} [{target_y['date']}]")
    except Exception as e:
        failures.append(f"DFII10: {e}")
        print(f"\n  ERROR real-yield fetch FAILED: {e}", file=sys.stderr)

    # --- 2. Named-contract vendor bars (primary); pointers never bind a grade ---
    fut = None
    dying_pointers = []
    ci_rows = []
    map_notes = contract_map_review()
    try:
        fut, ci_rows, dying_pointers = read_contract_snapshot()
        print("\n  METALS — named futures, MIRROR vendor daily Close; newest row excluded.")
        print("    These bars are not certified exchange settlements. Units: USD/oz; copper USD/lb.")
        for t, label in FUTURES.items():
            d = fut.get(t, {})
            if "error" in d:
                failures.append(f"named-{t}: {d['error']}")
                print(f"    {d['contract']:<12} {label:<14} UNKNOWN: {d['error']}")
            else:
                delta = f"{d['change_pct']:+.2f}%" if d['change_pct'] is not None else "UNMEASURED"
                print(f"    {d['contract']:<12} {label:<14} ${d['price']:>10,.3f} [{d['date']}]  prior-bar change {delta}")
    except Exception as e:
        failures.append(f"futures: {e}")
        print(f"\n  ERROR futures spot fetch FAILED: {e}", file=sys.stderr)

    # --- 3. ETF proxy spot (secondary cross-check) ---
    etf = None
    try:
        etf = read_spot(ETF_PROXIES)
        print(f"\n  METALS SPOT — ETF proxies (secondary cross-check, NOT 1:1 unit-matched to futures):")
        for t, label in ETF_PROXIES.items():
            d = etf.get(t, {})
            if "error" in d:
                print(f"    {t:<8} {label:<14} ERROR: {d['error']}")
            else:
                print(f"    {t:<8} {label:<14} ${d['price']:>10,.2f}  chg {d['change_pct']:+.2f}%  (prev ${d['prev']:,.2f})")
    except Exception as e:
        failures.append(f"etf: {e}")
        print(f"\n  ERROR ETF proxy spot fetch FAILED: {e}", file=sys.stderr)

    # --- 3b. Contract-identity guard (KB-112) — are the `=F` pointers alive? ---
    try:
        print(f"\n  CONTRACT IDENTITY — `=F` pointer vs explicit front month "
              f"(prior vendor row; the newest futures row's volume is duplicated):")
        for ptr, front, dt, pv, fv, pc, fc, sp, state in ci_rows:
            if dt is None:
                print(f"    {ptr:<6} vs {front:<11} {state}")
            else:
                print(f"    {ptr:<6} vs {front:<11} [{dt}]  vol {pv:>9,d} vs {fv:>9,d} "
                      f"({100.0 * pv / fv if fv else float('nan'):5.2f}%)  "
                      f"${pc:>9,.2f} vs ${fc:>9,.2f}  spread {sp:+.2f}%  -> {state}")
        if dying_pointers:
            print(f"    ⛔ {len(dying_pointers)} pointer(s) NOT on the front month: {', '.join(dying_pointers)}"
                  " — pointer prices are excluded from primary prices and GSR.")
        for note in map_notes:
            print(f"    ⚠️ CONTRACT MAP REVIEW: {note}")
    except Exception as e:
        failures.append(f"contract-identity: {e}")
        print(f"\n  ERROR contract-identity guard FAILED: {e}", file=sys.stderr)

    # --- 4. Binding gold/silver ratio: same-date, same-month named futures ---
    gsr = None
    gsr_band = None
    try:
        gsr = primary_gsr(fut or {})
        gsr_band = ("RED" if gsr >= GSR_RED else
                    "ORANGE" if gsr >= GSR_ORANGE else
                    "YELLOW" if gsr >= GSR_YELLOW else "benign")
        g, s = fut["GC=F"], fut["SI=F"]
        print(f"\n  GOLD/SILVER RATIO: {gsr:.2f} [{g['date']}]  "
              f"{g['contract']}/{s['contract']} (MIRROR vendor Close)")
        print(f"    Bands unchanged: Y{GSR_YELLOW}/O{GSR_ORANGE}/R{GSR_RED}; current {gsr_band}.")
    except (ValueError, KeyError, ZeroDivisionError) as exc:
        failures.append(f"GSR: {exc}")
        print(f"\n  ERROR GSR not graded: {exc}", file=sys.stderr)

    # --- 5. M1 divergence classifier ---
    divergence_state = None
    gold_bars = None
    gld_long_history = None
    basis_sensitive = False
    if latest_y and target_y and fut and "error" not in fut.get("GC=F", {"error": 1}):
        try:
            y_chg_bp = (float(latest_y["value"]) - float(target_y["value"])) * 100
            # need gold closes for the SAME dates the yield leg uses
            gold_contract = fut["GC=F"]["contract"]
            long_history = fetch.price_history([gold_contract, "GLD"], days=140)
            hist = long_history[gold_contract]
            gld_long_history = long_history.get("GLD")
            if "error" in hist:
                raise ValueError(hist["error"])
            bars = [b for b in hist["history"] if b.get("close") is not None]
            gold_bars = bars
            if not bars:
                raise ValueError(f"no usable {gold_contract} bars")

            def close_asof(target_date):
                """Vendor Close ON target_date, else the nearest PRIOR bar.

                FIX 2026-08-23 (KB-061 / L-29). This used to read the LIVE quote
                (`fut["GC=F"]["price"]`) for the end of the window while LABELLING
                the window with the yield leg's FRED date. Past the 18:00 ET Globex
                roll that live quote is an in-flight bar for the NEXT trade date, so
                the two legs were read up to four days apart under one date label —
                and because the 90d endpoints sit ~0.1% apart, a $9.50 move in an
                unsettled bar flipped the classifier DIVERGE->CONVERGE inside a
                single closed-market session. Never pair a T+1 series against a live
                quote; match the interval on BOTH legs and say so.
                """
                prior = [b for b in bars if b["date"] <= target_date]
                if not prior:
                    raise ValueError(f"no {gold_contract} bar at or before {target_date}")
                b = prior[-1]
                return b["close"], b["date"]

            gold_now, gold_now_date = close_asof(latest_y["date"])
            gold_then, gold_then_date = close_asof(target_y["date"])
            gold_chg_pct = (gold_now - gold_then) / gold_then * 100

            # decision margin: how far the call sits from the sign boundary it
            # turns on, expressed against this window's own daily noise. A state
            # decided inside 1 sigma is a coin flip with a label (L-29).
            rets = []
            completed_bars = [b for b in bars if b["date"] <= latest_y["date"]]
            for a, b in zip(completed_bars, completed_bars[1:]):
                if a["close"]:
                    rets.append((b["close"] - a["close"]) / a["close"] * 100)
            sigma = (statistics.stdev(rets) if len(rets) > 2 else float("nan"))
            inside_noise = (sigma == sigma) and abs(gold_chg_pct) < sigma
            if y_chg_bp > 0 and gold_chg_pct < 0:
                divergence_state = "CONVERGE (real-rate-consistent pattern — yields up, gold down; mechanism unidentified)"
            elif y_chg_bp > 0 and gold_chg_pct >= 0:
                divergence_state = "DIVERGE (yields up, gold holding/up; mechanism unidentified)"
            elif y_chg_bp <= 0 and gold_chg_pct > 0:
                divergence_state = "CLASSIC (yields down, gold up — expected inverse relationship)"
            else:
                divergence_state = "BOTH-DOWN (unusual — yields down AND gold down; check liquidity/USD confound)"
            print(f"\n  M1 DIVERGENCE CHECK (trailing ~90d, INTERVAL-MATCHED on both legs):")
            print(f"    DFII10:      {target_y['value']} [{target_y['date']}] -> "
                  f"{latest_y['value']} [{latest_y['date']}]  ({y_chg_bp:+.0f}bp)")
            print(f"    Gold ({gold_contract}): ${gold_then:,.2f} [{gold_then_date}] -> "
                  f"${gold_now:,.2f} [{gold_now_date}]  ({gold_chg_pct:+.2f}%)  "
                  "[MIRROR vendor daily Close; uncertified settlement]")
            if gold_now_date != latest_y["date"] or gold_then_date != target_y["date"]:
                print("    ⚠️ leg dates differ (nearest prior vendor bar used) — "
                      "compare the bracketed dates before reading the state")
            print(f"    State: {divergence_state}")
            if gld_long_history and "error" not in gld_long_history:
                ga = [b for b in gld_long_history['history'] if b['date']<=target_y['date']]
                gb = [b for b in gld_long_history['history'] if b['date']<=latest_y['date']]
                if ga and gb:
                    gld_change = (gb[-1]['close']/ga[-1]['close']-1)*100
                    basis_sensitive = (gld_change >= 0) != (gold_chg_pct >= 0)
                    print(f"    No-roll GLD cross-check: {gld_change:+.2f}% [{ga[-1]['date']}->{gb[-1]['date']}].")
                    if basis_sensitive:
                        print("    ⚠️ BASIS SENSITIVE: named gold and GLD have opposite signs; do not infer a regime change.")
                else:
                    print("    GLD90d cross-check UNMEASURED: endpoint history unavailable.")
            else:
                print("    GLD90d cross-check UNMEASURED: source unavailable.")
            if sigma == sigma:
                print(f"    decided by: |{gold_chg_pct:+.2f}%| vs a 0.00% sign boundary; "
                      f"window daily sigma {sigma:.2f}%"
                      + ("  ⚠️ MARGIN INSIDE 1-SIGMA NOISE — do NOT read as a state change"
                         if inside_noise else "  (margin exceeds 1-sigma)"))
        except Exception as e:
            failures.append(f"divergence-calc: {e}")
            print(f"\n  ERROR divergence classifier FAILED: {e}", file=sys.stderr)
    else:
        failures.append("divergence-calc: missing real-yield or gold leg")

    # --- 5b. M1 kill-condition #3 window (3-WEEK / 21d) — added 2026-08-07 ---
    # WHY: leg 5's window is a FIXED trailing ~90d. Registered v2 kill-cond #3
    # (THESIS.md:51) is "gold rises through RISING real yields sustained 3+ WEEKS".
    # A 90d lookback is ~4x the detection window, so a 3-week decoupling at the
    # END of the window is arithmetically invisible — leg 5 returned CONVERGE
    # (rc=0) on 2026-08-07 while the registered 3-week test was firing
    # (gold +9.7% / DFII10 +12bp, 7/17->8/7). That is a FALSE NEGATIVE in the
    # exact trigger the 7/17 polarity flip made this script's whole job.
    # This leg is NOT a new threshold: 3+wk is the already-registered,
    # Will-approved spec. It makes the instrument match the spec. (LESSON L-11)
    kc3_state = None
    if latest_y:
        try:
            obs_y = fetch.fred_fetch("DFII10", limit=60)
            gld_history = gld_long_history or fetch.price_history(["GLD"], days=42).get("GLD", {"error": "missing GLD history"})
            captured = datetime.now(ZoneInfo("America/New_York"))
            calendar_as_of = captured.date()
            if captured.weekday() == 4 and captured.hour < 16:
                calendar_as_of -= timedelta(days=1)
            weekly = measure_weekly_shape(obs_y, gld_history, latest_y["date"],
                                          calendar_as_of.isoformat())
            dy_bp, dg_pct = weekly["dy_bp"], weekly["return_pct"]
            if weekly['endpoint_shape']:
                kc3_state = "KILL-COND-#3 SHAPE PRESENT (gold up through rising real yields over three weekly intervals) — REVIEW; mechanism unidentified"
            elif dy_bp <= 0 and dg_pct > 0:
                kc3_state = "classic inverse over three weekly intervals; mechanism unidentified"
            else:
                kc3_state = "no kill-cond-#3 endpoint shape on the ruled weekly basis"
            a, b = weekly['points'][0], weekly['points'][-1]
            print("\n  M1 KILL-COND-#3 (RULED Friday-as-of endpoints, three weekly intervals):")
            print(f"    DFII10: {a['yield_pct']:.2f} [{a['date']}] -> {b['yield_pct']:.2f} [{b['date']}] ({dy_bp:+.0f}bp)")
            print(f"    GLD: ${a['gld']:,.2f} [{a['date']}] -> ${b['gld']:,.2f} [{b['date']}] ({dg_pct:+.2f}%)")
            print("    Gold graded on GLD, MIRROR vendor daily Close; no futures-roll fallback.")
            for w in weekly['weekly_signs']:
                print(f"    Weekly joint-up {w['start']}->{w['end']}: {w['joint_up']} ({w['dy_bp']:+.0f}bp / {w['return_pct']:+.2f}%).")
            print(f"    Endpoint shape {weekly['endpoint_shape']}; weekly-continuous {weekly['weekly_continuous']} (DECLINED alternative, no grading effect).")
            for point in weekly['points']:
                if point['friday'] != point['date']:
                    print(f"    Friday {point['friday']} uses common observation {point['date']} across non-publication days.")
            if gold_bars:
                ga = [r for r in gold_bars if r['date']<=a['date']]
                gb = [r for r in gold_bars if r['date']<=b['date']]
                if ga and gb:
                    q = (gb[-1]['close']/ga[-1]['close']-1)*100
                    print(f"    Named-contract cross-check {gold_contract}: {q:+.2f}% [{ga[-1]['date']}->{gb[-1]['date']}]; GLD remains binding.")
            daily = measure_three_week(obs_y, gld_history, latest_y['date'])
            print(f"    Rolling21-calendar-day diagnostic: {daily['dy_bp']:+.0f}bp / {daily['return_pct']:+.2f}% (not the ruled weekly grade).")
            print("    Magnitude attribution UNMEASURED: no current same-window empirical model fitted by this script.")
            if 0 < dy_bp < 5:
                print(f"    ⚠️ YIELD LEG INSIDE NOISE: {dy_bp:+.0f}bp; endpoint shape passes on a sign, not a move.")
            print(f"    State: {kc3_state}")
        except Exception as exc:
            failures.append(f"kc3-window: {exc}")
            print(f"\n  ERROR kill-cond-#3 window UNKNOWN: {exc}", file=sys.stderr)
    else:
        failures.append("kc3-window: missing real-yield observations")

    # --- 6. LME copper stocks (I1 inventory leg — westmetall scrape) ---
    lme_latest = None
    lme_band = None
    lme_vs_median_pct = None
    try:
        rows, lme_latest, lme_oldest = read_lme_copper_stocks()
        peak = max(rows, key=lambda t: t[1])
        lme_drawdown_pct = (lme_latest[1] - peak[1]) / peak[1] * 100
        print(f"\n  LME COPPER STOCKS (westmetall.com scrape, LME data, business-daily):")
        print(f"    Latest: {lme_latest[1]:,} t  [{lme_latest[0]}]")
        print(f"    Span peak: {peak[1]:,} t [{peak[0]}]  (latest = {lme_drawdown_pct:+.1f}% vs peak, {'falling' if lme_drawdown_pct < 0 else 'at/near peak'})")
        # Baseline: trailing-2yr rolling median (defined 'normal', KB-018)
        try:
            median_2yr, n_win, _ = read_lme_copper_baseline()
            lme_vs_median_pct = (lme_latest[1] - median_2yr) / median_2yr * 100
            lme_band = ("RED" if lme_vs_median_pct >= LME_RED else
                        "ORANGE" if lme_vs_median_pct >= LME_ORANGE else
                        "YELLOW" if lme_vs_median_pct >= LME_YELLOW else "benign")
            print(f"    vs 2yr median {median_2yr:,.0f} t (n={n_win}): {lme_vs_median_pct:+.1f}%  ->  band {lme_band}")
            print(f"    band context: Y+{LME_YELLOW}/O+{LME_ORANGE}/R+{LME_RED}% vs median; but the RED demand-collapse")
            print("    fire needs copper -20% AND inventory +100%.")
            print(f"    {copper_conjunction_context(lme_vs_median_pct)}")
        except Exception as be:
            failures.append(f"LME-baseline: {be}")
            print(f"    2yr-median baseline UNAVAILABLE: {be}", file=sys.stderr)
    except Exception as e:
        failures.append(f"LME-stocks: {e}")
        print(f"\n  ERROR LME copper stocks scrape FAILED: {e}", file=sys.stderr)

    print("\n  NOTE: gold and Ag/Pt/Pd COT freshness run in separate boot legs. "
          "Copper price history/conjunction remains UNMEASURED in this script.")

    # --- Verdict (always printed; failed legs say so, never fabricated) ---
    y_s = f"DFII10 {latest_y['value']} [{latest_y['date']}]" if latest_y else "real-yield FETCH-FAIL"
    g_s = (f"gold {fut['GC=F']['contract']} ${fut['GC=F']['price']:,.2f} [{fut['GC=F']['date']}]"
           if fut and "error" not in fut.get("GC=F", {"error": 1}) else "gold FETCH-FAIL")
    gsr_s = f"GSR {gsr:.2f} ({gsr_band})" if gsr else "GSR FETCH-FAIL"
    div_s = divergence_state or "divergence FETCH-FAIL"
    kc3_s = f" · KC#3(3wk): {kc3_state}" if kc3_state else ""
    lme_s = (f"LME Cu {lme_latest[1]:,}t{f' ({lme_vs_median_pct:+.0f}% vs 2yr-med, {lme_band})' if lme_band else ''} [{lme_latest[0]}]"
             if lme_latest else "LME Cu FETCH-FAIL")
    print(f"\n  Metals leg: {y_s} · {g_s} · {gsr_s} · {lme_s} · M1: {div_s}{kc3_s}\n")

    if dying_pointers:
        print(f"  ⛔ CONTRACT IDENTITY: {len(dying_pointers)} `=F` pointer(s) off the front month "
              f"({', '.join(dying_pointers)}) — primary prices and GSR use named contracts.")

    rc = 0
    if failures:
        print(f"  metals_watch.py: {len(failures)} leg(s) FAILED: {'; '.join(failures)}", file=sys.stderr)
        rc = 2
    elif (dying_pointers or map_notes or basis_sensitive or lme_band == "RED"
          # 2026-09-11: a pointer off the front month is a REVIEW condition, not a
          # fetch failure — the fetch SUCCEEDED and returned the wrong object, which
          # is worse (it prints a plausible number). rc=1 so the operator re-reads
          # the level before quoting it.
          or gsr_band in ("YELLOW", "ORANGE", "RED")
          or (divergence_state and divergence_state.startswith("DIVERGE"))
          # 2026-08-07: the registered 3-week kill-cond-#3 window now also trips
          # REVIEW. Without this, the 90d leg alone gates rc and returns 0 while
          # the actual registered test fires (see leg 5b comment).
          or (kc3_state and kc3_state.startswith("KILL-COND-#3 SHAPE PRESENT"))):
        # POLARITY FLIPPED 2026-07-17 (both M1 v2 catalyst tests resolved, v2
        # SURVIVED — MIDAS-03 CPI 7/14 + MIDAS-04 China-GDP 7/15; see header block
        # + SCRATCH.md). CONVERGE (gold re-coupled, inverse to real rates) is now
        # the EXPECTED/quiet baseline and no longer trips REVIEW. DIVERGE (gold
        # holding/rising THROUGH rising real yields = debasement-premium
        # reassertion, v2 kill-cond #3) is the alarm — REVIEW so the operator
        # eyeballs it and considers escalating BOND/LIQUID.
        rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main())
