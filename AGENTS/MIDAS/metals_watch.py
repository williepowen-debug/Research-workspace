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

SCOPE (per SCRATCH.md 2026-07-11 pickup, PAT-041 — wire the cadence durably
at build time): real yield (FRED DFII10) + gold/silver/copper/platinum/
palladium spot (COMEX futures primary: GC=F/SI=F/HG=F/PL=F/PA=F; ETF proxies
GLD/SLV/CPER/PPLT/PALL as a secondary cross-check row) + gold/silver ratio
(GSR, computed off futures) + an M1 divergence classifier (gold trend vs
real-yield trend over a trailing ~90-day window — CONVERGE = real-rate-
consistent / debasement premium NOT confirmed this window; DIVERGE = gold
holding/rising through rising real yields / premium confirmed this window).

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

OUT OF SCOPE (documented gaps, not silently dropped):
  - CFTC COT (gold/silver/copper net positioning) — weekly cadence (Fri
    release, Tue data), not a daily-pull fit for this script. Pulled manually
    this session via the CFTC Socrata API (see STATUS.md baseline + KB rows);
    a future increment could wire a weekly-cadence COT leg here.
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
import statistics
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

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
FRONT_MONTHS = {"GC=F": "GCZ26.CMX", "SI=F": "SIZ26.CMX", "HG=F": "HGZ26.CMX",
                "PL=F": "PLV26.NYM", "PA=F": "PAZ26.NYM"}
# A pointer carrying under this share of the explicit month's volume is DYING.
DYING_VOL_SHARE = 0.05


def check_contract_identity(front_months=None):
    """Is each `=F` pointer sitting on the liquid front month, or a dying one?

    Returns (rows, flags). `rows` is one tuple per pointer:
        (pointer, front, asof_date, ptr_vol, front_vol, ptr_close, front_close,
         spread_pct, state)
    `state` is DYING / OK / UNKNOWN. `flags` lists the DYING pointers.

    Fail-LOUD: a pointer whose history cannot be pulled is UNKNOWN and is listed,
    never silently treated as OK. An absent discriminator is not a clean bill."""
    front_months = FRONT_MONTHS if front_months is None else front_months
    rows, flags = [], []
    for ptr, front in front_months.items():
        try:
            hist = fetch.price_history([ptr, front], days=12)
            a, b = hist.get(ptr, {}), hist.get(front, {})
            if "error" in a or "error" in b:
                raise ValueError(f"{a.get('error') or b.get('error')}")
            ah, bh = a["history"], b["history"]
            if len(ah) < 2 or len(bh) < 2:
                raise ValueError("fewer than 2 bars — cannot use the PRIOR session")
            # RULE 1: the PRIOR settled session, never the newest (duplicated) bar.
            ar, br = ah[-2], bh[-2]
            if ar["date"] != br["date"]:
                raise ValueError(f"prior-session dates disagree: {ar['date']} vs {br['date']}")
            pv, fv = ar["volume"], br["volume"]
            spread = ((ar["close"] - br["close"]) / br["close"] * 100) if br["close"] else float("nan")
            if fv <= 0:
                state = "UNKNOWN"
            elif pv < DYING_VOL_SHARE * fv:
                state = "DYING"
            else:
                state = "OK"
            rows.append((ptr, front, ar["date"], pv, fv, ar["close"], br["close"], spread, state))
            if state != "OK":
                flags.append(ptr)
        except Exception as e:
            rows.append((ptr, front, None, None, None, None, None, None, f"UNKNOWN ({e})"))
            flags.append(ptr)
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
        print(f"\n  REAL YIELD (FRED DFII10, T+1 publication lag):")
        print(f"    Latest: {latest_y['value']} [{latest_y['date']}]")
        print(f"    ~90d prior: {target_y['value']} [{target_y['date']}]")
    except Exception as e:
        failures.append(f"DFII10: {e}")
        print(f"\n  ERROR real-yield fetch FAILED: {e}", file=sys.stderr)

    # --- 2. Futures spot (primary) ---
    fut = None
    try:
        fut = read_spot(FUTURES)
        print(f"\n  METALS SPOT — COMEX futures (yfinance, weekend/holiday = last close):")
        for t, label in FUTURES.items():
            d = fut.get(t, {})
            if "error" in d:
                print(f"    {t:<8} {label:<14} ERROR: {d['error']}")
            else:
                print(f"    {t:<8} {label:<14} ${d['price']:>10,.2f}  chg {d['change_pct']:+.2f}%  (prev ${d['prev']:,.2f})")
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
    dying_pointers = []
    try:
        ci_rows, dying_pointers = check_contract_identity()
        print(f"\n  CONTRACT IDENTITY — `=F` pointer vs explicit front month "
              f"(graded on the PRIOR settled session; the newest futures bar's volume is duplicated):")
        for ptr, front, dt, pv, fv, pc, fc, sp, state in ci_rows:
            if dt is None:
                print(f"    {ptr:<6} vs {front:<11} {state}")
            else:
                print(f"    {ptr:<6} vs {front:<11} [{dt}]  vol {pv:>9,d} vs {fv:>9,d} "
                      f"({100.0 * pv / fv if fv else float('nan'):5.2f}%)  "
                      f"${pc:>9,.2f} vs ${fc:>9,.2f}  spread {sp:+.2f}%  -> {state}")
        if dying_pointers:
            print(f"    ⛔ {len(dying_pointers)} pointer(s) NOT on the front month: {', '.join(dying_pointers)}"
                  f" — quote the EXPLICIT month, never the `=F` level, and never a cross-roll delta.")
    except Exception as e:
        failures.append(f"contract-identity: {e}")
        print(f"\n  ERROR contract-identity guard FAILED: {e}", file=sys.stderr)

    # --- 4. Gold/silver ratio (off futures) ---
    gsr = None
    gsr_band = None
    if fut and "error" not in fut.get("GC=F", {"error": 1}) and "error" not in fut.get("SI=F", {"error": 1}):
        gsr = fut["GC=F"]["price"] / fut["SI=F"]["price"]
        gsr_band = ("RED" if gsr >= GSR_RED else
                    "ORANGE" if gsr >= GSR_ORANGE else
                    "YELLOW" if gsr >= GSR_YELLOW else "benign")
        print(f"\n  GOLD/SILVER RATIO: {gsr:.2f}  (bands: Y{GSR_YELLOW}/O{GSR_ORANGE}/R{GSR_RED} — currently {gsr_band})")
    else:
        failures.append("GSR: could not compute (gold or silver futures leg failed)")
        print(f"\n  ERROR GSR not computed — gold/silver futures leg failed", file=sys.stderr)

    # --- 5. M1 divergence classifier ---
    divergence_state = None
    if latest_y and target_y and fut and "error" not in fut.get("GC=F", {"error": 1}):
        try:
            y_chg_bp = (float(latest_y["value"]) - float(target_y["value"])) * 100
            # need gold closes for the SAME dates the yield leg uses
            hist = fetch.price_history(["GC=F"], days=140)["GC=F"]
            if "error" in hist:
                raise ValueError(hist["error"])
            bars = [b for b in hist["history"] if b.get("close") is not None]
            if not bars:
                raise ValueError("no usable GC=F bars")

            def close_asof(target_date):
                """Settled close ON target_date, else the nearest PRIOR bar.

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
                    raise ValueError(f"no GC=F bar at or before {target_date}")
                b = prior[-1]
                return b["close"], b["date"]

            gold_now, gold_now_date = close_asof(latest_y["date"])
            gold_then, gold_then_date = close_asof(target_y["date"])
            gold_chg_pct = (gold_now - gold_then) / gold_then * 100

            # decision margin: how far the call sits from the sign boundary it
            # turns on, expressed against this window's own daily noise. A state
            # decided inside 1 sigma is a coin flip with a label (L-29).
            rets = []
            for a, b in zip(bars, bars[1:]):
                if a["close"]:
                    rets.append((b["close"] - a["close"]) / a["close"] * 100)
            sigma = (statistics.stdev(rets) if len(rets) > 2 else float("nan"))
            inside_noise = (sigma == sigma) and abs(gold_chg_pct) < sigma
            if y_chg_bp > 0 and gold_chg_pct < 0:
                divergence_state = "CONVERGE (real-rate-consistent — yields up, gold down; debasement premium NOT confirmed this window)"
            elif y_chg_bp > 0 and gold_chg_pct >= 0:
                divergence_state = "DIVERGE (debasement premium LIVE — yields up, gold holding/up)"
            elif y_chg_bp <= 0 and gold_chg_pct > 0:
                divergence_state = "CLASSIC (yields down, gold up — expected inverse relationship)"
            else:
                divergence_state = "BOTH-DOWN (unusual — yields down AND gold down; check liquidity/USD confound)"
            print(f"\n  M1 DIVERGENCE CHECK (trailing ~90d, INTERVAL-MATCHED on both legs):")
            print(f"    DFII10:      {target_y['value']} [{target_y['date']}] -> "
                  f"{latest_y['value']} [{latest_y['date']}]  ({y_chg_bp:+.0f}bp)")
            print(f"    Gold (GC=F): ${gold_then:,.2f} [{gold_then_date}] -> "
                  f"${gold_now:,.2f} [{gold_now_date}]  ({gold_chg_pct:+.2f}%)  "
                  f"[settled closes, NOT the live quote — L-29]")
            if gold_now_date != latest_y["date"] or gold_then_date != target_y["date"]:
                print("    ⚠️ leg dates differ (nearest prior settled bar used) — "
                      "compare the bracketed dates before reading the state")
            print(f"    State: {divergence_state}")
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
    if latest_y and fut and "error" not in fut.get("GC=F", {"error": 1}):
        try:
            from datetime import date as _d
            obs_y = [o for o in fetch.fred_fetch("DFII10", limit=60)
                     if o.get("value") not in (None, "", ".")]
            latest_d = _d.fromisoformat(obs_y[0]["date"])
            y_then = next((o for o in obs_y
                           if (latest_d - _d.fromisoformat(o["date"])).days >= 21), None)
            hist3 = fetch.price_history(["GC=F"], days=30)["GC=F"]
            if "error" in hist3:
                raise ValueError(hist3["error"])
            rows3 = [r for r in hist3["history"]
                     if (latest_d - _d.fromisoformat(r["date"])).days >= 21]
            if y_then and rows3:
                g_then, g_then_d = rows3[-1]["close"], rows3[-1]["date"]
                # SETTLED close as-of the yield leg's date — never the live quote.
                # Same FIX/rationale as the 90d leg (KB-061 / L-29), and it matters
                # MORE here: this is the REGISTERED kill-cond #3 window, its state
                # trips rc and feeds the kill rail.
                #
                # ⛔ CORRECTION 2026-09-02 (KB-096, L-45). The lines that stood here
                # claimed settled+prior-bar "keeps both legs on one contract and one
                # calendar." THAT WAS FALSE AND IT CERTIFIED THE DEFECT AS FIXED.
                # Settling the bar cures the IN-FLIGHT defect (L-29) only. It cannot
                # cure the CROSS-CONTRACT one, because `GC=F` IS the roll: it is a
                # continuous ticker whose underlying contract changes inside a 21d
                # window, so both endpoints can be settled and still be different
                # contracts. Measured on 2026-09-02: this leg read GC=F 4,361.80
                # [8/10, vol 1,303] -> 4,431.10 [8/31, vol 360] = +1.59%, both of them
                # thin dying-contract prints, against same-contract GCZ26 +1.398% and
                # no-roll GLD +1.461%. The 8/23 fix relocated the constraint and
                # reported it removed. ⇒ GLD now ARBITRATES the state decision (it
                # never rolls — STATUS standing warning ②); GC=F is printed for
                # continuity and a divergence >0.50pp is reported as roll contamination.
                _bars3 = [b for b in hist3["history"] if b.get("close") is not None]
                _prior3 = [b for b in _bars3 if b["date"] <= latest_y["date"]]
                if not _prior3:
                    raise ValueError(f"no GC=F bar at or before {latest_y['date']}")
                g_now, g_now_d = _prior3[-1]["close"], _prior3[-1]["date"]
                dy_bp = (float(latest_y["value"]) - float(y_then["value"])) * 100
                dg_pct = (g_now - g_then) / g_then * 100

                # --- ROLL ARBITER: GLD never rolls, so it grades the same window ---
                dg_arb, arb_src, roll_note = dg_pct, "GC=F", None
                try:
                    _hg = fetch.price_history(["GLD"], days=30)["GLD"]
                    if "error" not in _hg:
                        _gb = [b for b in _hg["history"] if b.get("close") is not None]
                        _gthen = [b for b in _gb
                                  if (latest_d - _d.fromisoformat(b["date"])).days >= 21]
                        _gnow = [b for b in _gb if b["date"] <= latest_y["date"]]
                        if _gthen and _gnow:
                            _a, _b = _gthen[-1]["close"], _gnow[-1]["close"]
                            dg_gld = (_b - _a) / _a * 100
                            dg_arb, arb_src = dg_gld, "GLD (no-roll arbiter)"
                            if abs(dg_gld - dg_pct) > 0.50:
                                roll_note = (f"ROLL CONTAMINATION — GC=F {dg_pct:+.2f}% vs "
                                             f"GLD {dg_gld:+.2f}% differ by "
                                             f"{abs(dg_gld - dg_pct):.2f}pp; GC=F endpoints "
                                             f"are not one contract. STATE GRADED ON GLD.")
                except Exception as _e:                       # arbiter is advisory
                    roll_note = f"GLD arbiter unavailable ({_e}) — GC=F ungraded for roll"

                # the registered shape is graded on the ARBITER, never on GC=F alone
                dg_pct = dg_arb
                if dy_bp > 0 and dg_pct > 0:
                    kc3_state = ("KILL-COND-#3 SHAPE PRESENT (gold UP through RISING real "
                                 "yields over 3wk = debasement-premium reassertion) — REVIEW/escalate")
                elif dy_bp <= 0 and dg_pct > 0:
                    kc3_state = ("classic inverse over 3wk (yields down, gold up) — but CHECK MAGNITUDE: "
                                 f"empirical beta ~-0.05%/bp means {dy_bp:+.0f}bp explains only "
                                 f"{abs(-0.0513 * dy_bp):.2f}% of the {dg_pct:+.1f}% move")
                else:
                    kc3_state = "no kill-cond-#3 shape (gold flat/down over 3wk)"
                print(f"\n  M1 KILL-COND-#3 WINDOW (registered 3-WEEK test, INTERVAL-MATCHED):")
                print(f"    DFII10:      {y_then['value']} [{y_then['date']}] -> "
                      f"{latest_y['value']} [{latest_y['date']}]  ({dy_bp:+.0f}bp)")
                print(f"    Gold (GC=F): ${g_then:,.2f} [{g_then_d}] -> "
                      f"${g_now:,.2f} [{g_now_d}]  ({(g_now - g_then) / g_then * 100:+.2f}%)  "
                      f"[settled closes, NOT the live quote — L-29]")
                print(f"    Gold graded on: {arb_src}  ({dg_pct:+.2f}%)")
                if roll_note:
                    print(f"    ⛔ {roll_note}")
                # A 3-week yield move inside noise cannot support "RISING real yields"
                if 0 < dy_bp < 5:
                    print(f"    ⚠️  YIELD LEG INSIDE NOISE — {dy_bp:+.0f}bp over 3wk is not "
                          f"a rising-yield regime; the SHAPE test passes on a sign, not a move. "
                          f"Do not read as decoupling without a yield move that clears ~5bp.")
                print(f"    State: {kc3_state}")
            else:
                failures.append("kc3-window: insufficient history")
        except Exception as e:
            failures.append(f"kc3-window: {e}")
            print(f"\n  ERROR kill-cond-#3 window FAILED: {e}", file=sys.stderr)

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
            direction = "FALLING (drawing down)" if lme_drawdown_pct < -3 else "flat/rising"
            print(f"    vs 2yr median {median_2yr:,.0f} t (n={n_win}): {lme_vs_median_pct:+.1f}%  ->  band {lme_band}")
            print(f"    band context: Y+{LME_YELLOW}/O+{LME_ORANGE}/R+{LME_RED}% vs median; but the RED demand-collapse")
            print(f"    fire needs the CONJUNCTION (copper -20% AND inv +100%) — inventory {direction}, price UP = NOT firing")
        except Exception as be:
            failures.append(f"LME-baseline: {be}")
            print(f"    2yr-median baseline UNAVAILABLE: {be}", file=sys.stderr)
    except Exception as e:
        failures.append(f"LME-stocks: {e}")
        print(f"\n  ERROR LME copper stocks scrape FAILED: {e}", file=sys.stderr)

    print(f"\n  NOTE: CFTC COT (weekly cadence) and copper-vs-200dma (I1) are NOT wired "
          f"into this script — documented gaps, see file header + STATUS.md.")

    # --- Verdict (always printed; failed legs say so, never fabricated) ---
    y_s = f"DFII10 {latest_y['value']} [{latest_y['date']}]" if latest_y else "real-yield FETCH-FAIL"
    g_s = (f"gold ${fut['GC=F']['price']:,.2f}" if fut and "error" not in fut.get("GC=F", {"error": 1}) else "gold FETCH-FAIL")
    gsr_s = f"GSR {gsr:.2f} ({gsr_band})" if gsr else "GSR FETCH-FAIL"
    div_s = divergence_state or "divergence FETCH-FAIL"
    kc3_s = f" · KC#3(3wk): {kc3_state}" if kc3_state else ""
    lme_s = (f"LME Cu {lme_latest[1]:,}t{f' ({lme_vs_median_pct:+.0f}% vs 2yr-med, {lme_band})' if lme_band else ''} [{lme_latest[0]}]"
             if lme_latest else "LME Cu FETCH-FAIL")
    print(f"\n  Metals leg: {y_s} · {g_s} · {gsr_s} · {lme_s} · M1: {div_s}{kc3_s}\n")

    if dying_pointers:
        print(f"  ⛔ CONTRACT IDENTITY: {len(dying_pointers)} `=F` pointer(s) off the front month "
              f"({', '.join(dying_pointers)}) — every level printed above for those is the WRONG CONTRACT.")

    rc = 0
    if failures:
        print(f"  metals_watch.py: {len(failures)} leg(s) FAILED: {'; '.join(failures)}", file=sys.stderr)
        rc = 2
    elif (dying_pointers
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
