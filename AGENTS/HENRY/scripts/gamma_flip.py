#!/usr/bin/env python3
"""
gamma_flip.py — compute the SPX dealer-gamma flip (zero-gamma level) from the
LIVE ^SPX options chain via yfinance + Black-Scholes gamma. No paywalled
provider (SpotGamma/FlashAlpha) required — a FREE-TIER estimator (validated
2026-07-17 vs FlashAlpha/zerogex: flip within 20-34pts, walls exact-match).

boot.py imports compute_gamma_flip() for its (b) GAMMA section (14d horizon,
fast); run this script standalone for the definitive 35d read.

Method
------
- Pull ^SPX option chains for all expirations <= HORIZON_DAYS (near-term gamma
  dominates the flip); filter OI>0, sane IV (0.03-2.5), strikes within band of spot.
- BSM gamma per contract (r=4.5%, q=1.3% SPX div yield), gamma from yfinance IV.
- Dealer convention (standard SpotGamma-style naive): dealers LONG call gamma (+),
  SHORT put gamma (-). Net GEX(S) = sum_calls - sum_puts, in $ per 1% move.
- Zero-gamma FLIP = spot where Net GEX(S) crosses zero (grid + linear interp).
- Call/put walls = strikes with max gamma-weighted OI.

CAVEAT (state when citing): the ABSOLUTE $B depends on the dealer-positioning
assumption (real books differ; vendors apply proprietary adjustments — this is a
FREE-TIER proxy, NOT SpotGamma-grade). The FLIP LEVEL and the SIGN are the robust
reads; don't trust the exact level within ~30-40pts of a crossing.

Usage: .venv/bin/python3 AGENTS/HENRY/scripts/gamma_flip.py [--days N | --both]
           [--asof YYYY-MM-DD] [--underlying SPX|QQQ|NDX] [--spot PRICE] [--publish [--note TEXT]]

--underlying (2026-10-29, Will-directed): QQQ and NDX use the same naive dealer
convention on their own Cboe chains. QQQ is an American-style ETF option and only
part of Nasdaq-100 dealer gamma (NDX options and NQ futures carry the rest) — a
QQQ read is a partial map, read it beside NDX. SPX stays the default; boot.py is
unchanged.
--spot: evaluate the chain at a given underlying price instead of Cboe's
current_price (which includes extended-hours trading after the close).
--publish (2026-10-29): PUBLISHED.tsv is written ONLY when asked. Before this,
every run rewrote the day's rows — including reads nobody published — and dropped
the basis notes a hand-recorded row carried. --note appends a basis note.
"""
import sys, math, json, re, urllib.request
from datetime import date, datetime
from pathlib import Path
from collections import defaultdict

# A healthy <=35d ^SPX pull is thousands of contracts (6,206 on 7/17, 4,900 at 14d).
# Below this the chain is too degraded to locate a flip — see the thin-chain guard.
MIN_CONTRACTS = 400


def _isnan(x):
    """True for NaN. Note `x or 0` does NOT catch NaN (NaN is truthy) — the 7/23 bug."""
    try:
        return math.isnan(float(x))
    except (TypeError, ValueError):
        return True

R, Q = 0.045, 0.013
HORIZON_DAYS = 35


def npdf(x):
    return math.exp(-0.5 * x * x) / math.sqrt(2 * math.pi)


def bsm_gamma(S, K, T, sig, q=Q):
    if T <= 0 or sig <= 0 or S <= 0 or K <= 0:
        return 0.0
    d1 = (math.log(S / K) + (R - q + 0.5 * sig * sig) * T) / (sig * math.sqrt(T))
    return math.exp(-q * T) * npdf(d1) / (S * sig * math.sqrt(T))


CBOE_URL = "https://cdn.cboe.com/api/global/delayed_quotes/options/{}.json"
# Per-underlying config. q = dividend yield; step = flip-search grid in index points;
# prefix = PUBLISHED.tsv metric prefix (SPX keeps the historical bare names).
UNDERLYINGS = {
    "SPX": {"cboe": "_SPX", "occ": r"SPXW?", "yf": "^SPX", "q": Q, "step": 5, "prefix": ""},
    "QQQ": {"cboe": "QQQ", "occ": r"QQQ", "yf": "QQQ", "q": 0.006, "step": 0.5, "prefix": "qqq_"},
    "NDX": {"cboe": "_NDX", "occ": r"NDXP?", "yf": "^NDX", "q": 0.007, "step": 20, "prefix": "ndx_"},
}


def _occ_re(u):
    return re.compile(r"^" + UNDERLYINGS[u]["occ"] + r"(\d{2})(\d{2})(\d{2})([CP])(\d{8})$")


def _fetch_cboe(today, horizon, band, underlying="SPX"):
    """PRIMARY source: CBOE delayed-quote chain (the exchange itself).

    Added 7/23 after yfinance's `openInterest` field went to ZERO for ~97% of the
    ^SPX chain (7,278 of 7,514 rows) while volume and IV stayed populated — a
    field-level provider outage, NOT the "degraded IV feed" first diagnosed.
    CBOE carries real OI (21.1K rows, ~21.7M contracts) and is exchange-primary,
    so it is now preferred over yfinance rather than merely a fallback.

    NOTE: volume is NOT a substitute for open interest. GEX weights by the STOCK
    of outstanding contracts dealers must hedge; volume is one session's FLOW
    (heavily 0DTE churn). Weighting by volume yields a number shaped like a GEX
    that is not one — do not add that as a fallback.

    Returns (spot, opts, err).
    """
    try:
        req = urllib.request.Request(CBOE_URL.format(UNDERLYINGS[underlying]["cboe"]), headers={"User-Agent": "Mozilla/5.0 (research)"})
        payload = json.load(urllib.request.urlopen(req, timeout=90))["data"]
    except Exception as e:  # noqa: BLE001
        return None, None, f"cboe fetch failed: {e}"
    spot = float(payload.get("current_price") or payload.get("close") or 0)
    if not spot:
        return None, None, "cboe returned no underlying price"
    opts = []
    occ = _occ_re(underlying)
    for o in payload.get("options", []):
        m = occ.match(o.get("option", ""))
        if not m:
            continue
        yy, mm, dd, cp, k = m.groups()
        T = (date(2000 + int(yy), int(mm), int(dd)) - today).days / 365.0
        if T <= 0 or T > horizon / 365.0:
            continue
        oi = o.get("open_interest") or 0
        iv = o.get("iv") or 0
        K = int(k) / 1000.0
        if _isnan(K) or _isnan(oi) or _isnan(iv):
            continue
        if oi <= 0 or not (0.03 < iv < 2.5):
            continue
        if not ((1 - band) * spot < K < (1 + band) * spot):
            continue
        opts.append((K, T, iv, oi, cp))
    return spot, opts, None


def compute_gamma_flip(asof=None, horizon=HORIZON_DAYS, band=0.25, source="auto",
                       underlying="SPX", spot_override=None):
    """Compute the SPX dealer-gamma flip from the live SPX chain.

    source: "auto" (CBOE first, yfinance fallback) | "cboe" | "yfinance".

    Returns a dict {spot, flip, flips, gex_at_spot, regime, call_wall, put_wall,
    n_contracts, source, horizon, band, asof} — or {'error': msg} on any failure
    (never raises, so boot.py can degrade gracefully).
    """
    today = datetime.strptime(asof, "%Y-%m-%d").date() if asof else date.today()
    used = None
    opts = []
    spot = None
    errs = []

    if source in ("auto", "cboe"):
        spot, opts, err = _fetch_cboe(today, horizon, band, underlying)
        if err:
            errs.append(err)
        elif len(opts) >= MIN_CONTRACTS:
            used = "cboe"
        else:
            errs.append(f"cboe chain thin: {len(opts)} usable")
    if used is None and source in ("auto", "yfinance"):
        spot_y, opts_y, err = _fetch_yfinance(today, horizon, band, underlying)
        if err:
            errs.append(err)
        else:
            spot, opts, used = spot_y, opts_y, "yfinance"
    if used is None:
        return {"error": "; ".join(errs) or "no usable source"}

    feed_spot = spot
    if spot_override:
        spot = float(spot_override)
    r = _finish(spot, opts, used, horizon, band, today, underlying)
    if "error" not in r:
        r["feed_spot"] = feed_spot
    return r


def _fetch_yfinance(today, horizon, band, underlying="SPX"):
    """Fallback source. Returns (spot, opts, err)."""
    try:
        import yfinance as yf
    except Exception as e:  # noqa: BLE001
        return None, None, f"yfinance import failed: {e}"
    try:
        t = yf.Ticker(UNDERLYINGS[underlying]["yf"])
        spot = t.fast_info["lastPrice"]
        exps = t.options
    except Exception as e:  # noqa: BLE001
        return None, None, f"chain fetch failed: {e}"
    if not spot or not exps:
        return None, None, "no spot/expirations from yfinance"

    opts = []
    for exp in exps:
        y, m, d = map(int, exp.split("-"))
        T = (date(y, m, d) - today).days / 365.0
        if T <= 0 or T > horizon / 365.0:
            continue
        try:
            ch = t.option_chain(exp)
        except Exception:  # noqa: BLE001
            continue
        for df, typ in ((ch.calls, "C"), (ch.puts, "P")):
            for _, r in df.iterrows():
                K = r["strike"]; oi = r["openInterest"] or 0; iv = r["impliedVolatility"] or 0
                # NaN guard (7/23 bug): `x or 0` does NOT catch NaN — NaN is truthy, and
                # `NaN <= 0` is False, so NaN OI used to survive this filter and poison the
                # GEX sum. A NaN g0 then read as POSITIVE in boot.py (`g0 < 0`) and NEGATIVE
                # in the CLI (`g0 > 0`) — same number, opposite labels — while max() over an
                # all-NaN wall dict returned an arbitrary strike (put wall above call wall).
                # Fail loud on missing data; never emit a confident number built on NaN.
                if _isnan(K) or _isnan(oi) or _isnan(iv):
                    continue
                if oi <= 0 or not (0.03 < iv < 2.5):
                    continue
                if not ((1 - band) * spot < K < (1 + band) * spot):
                    continue
                opts.append((K, T, iv, oi, typ))
    return spot, opts, None


def _wall_margin(d):
    """Fractional gap between the #1 and #2 strike in a gamma-weighted-OI dict.

    Returns None if there is no runner-up. A small margin means max() is
    breaking a near-tie arbitrarily and the winner must NOT be published as
    a single strike — report the band. See the near-tie guard below.
    """
    if not d or len(d) < 2:
        return None
    top = sorted(d.values(), reverse=True)[:2]
    return (top[0] - top[1]) / top[0] if top[0] else None


NEAR_TIE = 0.10  # <10% between #1 and #2 = a coin flip, not a wall


def _finish(spot, opts, used, horizon, band, today, underlying="SPX"):
    """Shared math: net GEX, zero-gamma flip, call/put walls."""
    q, step = UNDERLYINGS[underlying]["q"], UNDERLYINGS[underlying]["step"]
    if not opts:
        return {"error": "no usable contracts after filtering"}
    # Thin-chain guard (7/23): a healthy <=35d pull is thousands of contracts
    # (6,967 via CBOE on 7/23; 6,206 via yfinance on 7/17). Refuse to emit rather
    # than publish a flip located off a residue.
    if len(opts) < MIN_CONTRACTS:
        return {"error": f"chain too thin: {len(opts)} usable contracts "
                         f"(< {MIN_CONTRACTS}) from {used} — no gamma read this run"}

    def net_gex(S):
        g = 0.0
        for K, T, iv, oi, typ in opts:
            gam = bsm_gamma(S, K, T, iv, q) * oi * 100 * S * S * 0.01
            g += gam if typ == "C" else -gam
        return g

    g0 = net_gex(spot)
    if _isnan(g0):
        return {"error": "net GEX computed as NaN — refusing to emit a regime call"}
    lo, n = spot * 0.90, int(spot * 0.20 / step)
    vals = [(S, net_gex(S)) for S in (round(lo + i * step, 2) for i in range(n))]
    flips = []
    for (S1, v1), (S2, v2) in zip(vals, vals[1:]):
        if v1 == 0 or (v1 < 0) != (v2 < 0):
            flips.append(S1 + (0 - v1) * (S2 - S1) / (v2 - v1))

    cg, pg = defaultdict(float), defaultdict(float)
    for K, T, iv, oi, typ in opts:
        w = bsm_gamma(spot, K, T, iv, q) * oi
        (cg if typ == "C" else pg)[K] += w

    return {
        "spot": spot,
        "flip": flips[0] if flips else None,
        "flips": flips,
        "gex_at_spot": g0,
        "regime": "NEGATIVE" if g0 < 0 else "POSITIVE",
        "call_wall": max(cg, key=cg.get) if cg else None,
        "put_wall": max(pg, key=pg.get) if pg else None,
        # Near-tie guard (7/23): gamma-weighted walls are often a statistical
        # coin-flip between adjacent round strikes — on 7/23 the 35d put wall was
        # 7,500 (117.6) vs 7,300 (114.3), a 3% gap that max() broke arbitrarily and
        # that I published as fact. Independent trackers all read 7,300-7,400.
        # Expose the runners-up so a near-tie is visible rather than hidden.
        "call_wall_top3": sorted(cg, key=cg.get, reverse=True)[:3] if cg else [],
        "put_wall_top3": sorted(pg, key=pg.get, reverse=True)[:3] if pg else [],
        # ...and the #1-vs-#2 margins, so a caller can TEST for a near-tie
        # instead of eyeballing the ladder. <10% = the arg-max is a coin flip.
        "call_wall_margin": _wall_margin(cg),
        "put_wall_margin": _wall_margin(pg),
        "n_contracts": len(opts),
        "source": used,
        "horizon": horizon,
        "band": band,
        "asof": today.isoformat(),
        "underlying": underlying,
    }


def _flag(name, default):
    if name in sys.argv:
        return sys.argv[sys.argv.index(name) + 1]
    return default


def cross_horizon_check(r14, r35):
    """Audit-E2 guard (built 2026-10-21; gap logged 7/29). The near-tie guard only
    compares #1 vs #2 WITHIN a horizon; on 7/29 the 14d read gave walls 7,500/7,300
    while the 35d gave a 7,000 = 7,000 tie, and no wall was publishable. Rule, per
    wall: the same #1 strike at BOTH horizons = publishable (quote a band at any
    horizon where it is a near-tie); different #1 strikes = WITHHOLD that wall.
    A regime-sign disagreement is reported, never averaged away.
    Returns {"walls": {"call": (verdict, text), "put": (...)}, "sign_agree": bool}."""
    out = {"walls": {}, "sign_agree": r14["regime"] == r35["regime"]}
    # Put == call at either horizon is the 7/23 structural impossibility; _print_read
    # flags it per horizon, but until 2026-10-29 this check still printed PUBLISH for
    # the put side (first QQQ read: 35d put == call == 720). Withhold it here too.
    same = [h for h, r in (("14d", r14), ("35d", r35))
            if r.get("put_wall") is not None and r.get("put_wall") == r.get("call_wall")]
    for key in ("call", "put"):
        w14, w35 = r14.get(f"{key}_wall"), r35.get(f"{key}_wall")
        if key == "put" and same:
            out["walls"][key] = ("WITHHOLD", f"put wall == call wall at {', '.join(same)} — put side UNRESOLVED")
            continue
        if w14 is None or w35 is None or w14 != w35:
            out["walls"][key] = ("WITHHOLD", f"14d {w14:,.0f} vs 35d {w35:,.0f} — horizons disagree"
                                 if w14 is not None and w35 is not None else "missing at one horizon")
            continue
        bands = []
        for h, r in (("14d", r14), ("35d", r35)):
            m = r.get(f"{key}_wall_margin")
            if m is not None and m < NEAR_TIE:
                top = sorted((r.get(f"{key}_wall_top3") or [])[:2])
                bands.append(f"{h} near-tie band {'-'.join(f'{s:,.0f}' for s in top)}")
        out["walls"][key] = ("PUBLISH", f"{w14:,.0f} at both horizons"
                             + (f" ({'; '.join(bands)})" if bands else " (clean at both)"))
    return out


def _print_read(r, horizon):
    spot, flips = r["spot"], r["flips"]
    u = r.get("underlying", "SPX")
    print(f"===== {u} GAMMA FLIP  (asof {r['asof']}, <= {horizon}d, "
          f"{r['n_contracts']:,} contracts, src={r.get('source','?')}) =====")
    fs = r.get("feed_spot")
    print(f"  {u} spot        {spot:,.2f}"
          + (f"   (--spot override; feed price {fs:,.2f})" if fs is not None and abs(fs - spot) > 1e-9 else ""))
    print(f"  Net GEX @ spot  {r['gex_at_spot']/1e9:+.1f} $B/1%   -> "
          f"{'POSITIVE (dealers dampen)' if r['gex_at_spot'] > 0 else 'NEGATIVE (dealers AMPLIFY)'}")
    print(f"  Zero-gamma FLIP {'  '.join(f'~{f:,.0f}' for f in flips) if flips else 'none in +/-10% band'}")
    if flips:
        rel = spot - flips[0]
        print(f"                  spot is {rel:+,.0f} pts {'BELOW (neg-gamma)' if rel < 0 else 'ABOVE (pos-gamma)'} the flip")
    cw, pw = r["call_wall"], r["put_wall"]
    # Near-tie guard, SURFACED (7/28): the 7/23 fix computed the runners-up but
    # never printed them, so on 7/28 the 35d run again emitted put wall == call
    # wall == 7,500 with no visible warning. A guard the operator can't see is
    # not a guard. Print the margin, and refuse to state a bare strike on a tie.
    for label, wall, key in (("Call", cw, "call"), ("Put", pw, "put")):
        margin = r.get(f"{key}_wall_margin")
        top3 = r.get(f"{key}_wall_top3") or []
        tie = margin is not None and margin < NEAR_TIE
        line = f"  {label} wall       {wall:,.0f}"
        if tie:
            band_str = "-".join(f"{s:,.0f}" for s in sorted(top3[:2]))
            line += (f"  ⚠️ NEAR-TIE ({margin*100:.0f}% over #2) —"
                     f" report the BAND {band_str}, not this strike")
        elif margin is not None:
            line += f"  (clean #1, +{margin*100:.0f}% over #2)"
        if label == "Put" and wall and spot < wall and not tie:
            line += f"  <- {u} BELOW put wall (intensified downside feedback)"
        print(line)
    if cw and pw and cw == pw:
        print("  ⚠️⚠️ PUT WALL == CALL WALL — structurally impossible as stated;"
              " treat the put side as UNRESOLVED at this horizon (see LESSONS 7/23).")
    print("  (FREE-TIER proxy: absolute $B assumes long-call/short-put dealer gamma; the FLIP + sign are the robust reads)")


def main():
    asof = _flag("--asof", None)
    u = _flag("--underlying", "SPX").upper()
    if u not in UNDERLYINGS:
        print(f"gamma_flip: unknown --underlying {u} (choose {', '.join(UNDERLYINGS)})")
        return 2
    spot = _flag("--spot", None)
    pub = "--publish" in sys.argv
    note = _flag("--note", "")
    kw = {"underlying": u, "spot_override": spot}
    if "--both" in sys.argv:
        reads = {}
        for h in (14, 35):
            r = compute_gamma_flip(asof=asof, horizon=h, **kw)
            if "error" in r:
                print(f"gamma_flip {h}d: {r['error']}")
                print("  ⛔ CROSS-HORIZON CHECK CANNOT-EVALUATE — one horizon failed; publish no wall.")
                return 1
            _print_read(r, h)
            if pub:
                _publish(r, h, note)
            reads[h] = r
            print()
        x = cross_horizon_check(reads[14], reads[35])
        f14, f35 = reads[14]["flip"], reads[35]["flip"]
        band = f"{min(f14, f35):,.0f}-{max(f14, f35):,.0f}" if f14 and f35 else "n/a"
        print("===== CROSS-HORIZON CHECK (audit E2) =====")
        print(f"  Flip band       {band}  (14d ~{f14:,.0f} · 35d ~{f35:,.0f})" if f14 and f35
              else "  Flip band       n/a — a horizon has no flip in the +/-10% band")
        print(f"  Regime          14d {reads[14]['regime']} · 35d {reads[35]['regime']}"
              + ("" if x["sign_agree"] else "  ⚠️ SIGN DISAGREES — report both, call no regime"))
        for key in ("call", "put"):
            verdict, text = x["walls"][key]
            mark = "✓" if verdict == "PUBLISH" else "⛔"
            print(f"  {key.capitalize():5s} wall      {mark} {verdict}: {text}")
        print("  PUBLISHED.tsv " + ("UPDATED (--publish)" if pub else "NOT written (pass --publish to record this read)"))
        return 0
    horizon = int(_flag("--days", HORIZON_DAYS))
    r = compute_gamma_flip(asof=asof, horizon=horizon, **kw)
    if "error" in r:
        print(f"gamma_flip: {r['error']}")
        return 1
    _print_read(r, horizon)
    if pub:
        _publish(r, horizon, note)
    print("  PUBLISHED.tsv " + ("UPDATED (--publish)" if pub else "NOT written (pass --publish to record this read)"))
    if horizon != 14 and horizon != 35:
        return 0
    print("  (Walls: one horizon only. Run `gamma_flip.py --both` for the cross-horizon check before publishing a wall.)")
    return 0


# ── PUBLISHED.tsv ledger (7/28) ───────────────────────────────────────
# Numbers this desk publishes get wired into OTHER agents' gates. VIOLET
# carried the 7/23 flip as a live thesis-kill for five days while this script
# refreshed it twice. The consumer check that finds those stale copies is
# cheap; what was missing was any record of WHAT was superseded and WHEN.
# So the estimator records its own output, and boot.py runs the check off
# this ledger automatically — a boot check, not a remembered ritual
# ([[finding_mechanize_the_cap_not_the_ritual]]).
# One row per (metric, day): re-running intraday updates the day's row rather
# than appending noise.
PUBLISHED_TSV = Path(__file__).resolve().parent.parent / "workbook" / "PUBLISHED.tsv"
PUBLISH_HEADER = "metric\tvalue\tasof\tnote"


def _publish(r, horizon, note=""):
    """Record today's flip + net GEX. Never raises — telemetry must not break a read.
    Called only under --publish (2026-10-29)."""
    try:
        if not r or r.get("error") or not r.get("flip"):
            return
        today = str(r.get("asof") or date.today())
        pre = UNDERLYINGS[r.get("underlying", "SPX")]["prefix"]
        tail = f" ({note})" if note else ""
        rows = [
            (f"{pre}gamma_flip_{horizon}d", f"{r['flip']:.2f}" if pre == "qqq_" else f"{r['flip']:.0f}",
             f"{r.get('source','?')} {r.get('n_contracts','?')} contracts{tail}"),
            (f"{pre}net_gex_{horizon}d_Bn", f"{r['gex_at_spot']/1e9:.1f}", f"$B per 1%{tail}"),
        ]
        existing = []
        if PUBLISHED_TSV.exists():
            existing = [l for l in PUBLISHED_TSV.read_text().strip().split("\n") if l.strip()]
        header = existing[0] if existing else PUBLISH_HEADER
        body = [l for l in existing[1:]]
        for metric, value, note in rows:
            body = [l for l in body
                    if not (l.startswith(f"{metric}\t") and f"\t{today}\t" in l)]
            body.append(f"{metric}\t{value}\t{today}\t{note}")
        PUBLISHED_TSV.parent.mkdir(parents=True, exist_ok=True)
        PUBLISHED_TSV.write_text("\n".join([header] + body) + "\n")
    except Exception:
        pass


if __name__ == "__main__":
    sys.exit(main())
