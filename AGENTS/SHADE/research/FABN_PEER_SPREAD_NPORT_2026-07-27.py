#!/usr/bin/env python3
"""SHADE — independent FABN peer-spread canary from NPORT-P holder marks.

WHY: the canary (Athene 5Y FABN T+123, +43-48bp vs peers) comes from Athene's OWN
investor deck, which picks its own peer set (CRBG/EQH/PFG). That is an
incentive-flagged source. This rebuilds the peer-relative penalty from primary
holder filings with a SHADE-chosen peer set.

DESIGN — the thing that makes it valid: restrict to funds that hold BOTH Athene
Global Funding AND at least one peer FABN program in the SAME filing (same fund,
same valuation date, same pricing vendor). Cross-issuer level differences from
pricing methodology then cancel, and what is left is issuer credit.

Spread = YTM(price, coupon, maturity) - matched-tenor Treasury (FRED, at period end).
Systematic YTM-approximation error largely cancels in the PEER DIFFERENCE at matched tenor.
"""
import json, re, time, sys, urllib.request, gzip, collections, datetime, statistics

UA = "SHADE Research williepowen@gmail.com"

ISSUERS = {
    "ATHENE":     r"Athene Global Funding",
    "MASSMUTUAL": r"MassMutual Global Funding",
    "METTOWER":   r"Met Tower Global Funding",
    "PRICOA":     r"Pricoa Global Funding",
    "GLOBALATL":  r"GA Global Funding",
    "COREBRIDGE": r"Corebridge Global Funding",
    "NYLIFE":     r"New York Life Global Funding",
}
PEERS = [k for k in ISSUERS if k != "ATHENE"]
MAX_FILINGS = int(sys.argv[1]) if len(sys.argv) > 1 else 120
# 2026-08-28 rerun: the enumeration window was hardcoded to the 2026-05-01..07-27
# vintage. Parameterised so a window is an explicit, stamped input rather than a
# silent constant. Defaults are the 6/30-period window (filed ~Jul-Aug 2026).
START_DT = sys.argv[2] if len(sys.argv) > 2 else "2026-07-01"
END_DT   = sys.argv[3] if len(sys.argv) > 3 else "2026-08-28"


def get(url, raw=False, tries=4):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip, deflate"})
            with urllib.request.urlopen(req, timeout=45) as r:
                data = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    data = gzip.decompress(data)
                return data if raw else data.decode("utf-8", "replace")
        except Exception:
            if i == tries - 1:
                return None
            time.sleep(0.7 * (i + 1))


# ---------- 1. enumerate candidate filings (those naming Athene Global Funding) ----------
print("[1] enumerating NPORT-P filings holding Athene Global Funding ...", flush=True)
filings = {}
# DEFECT FIX 3 (DAEDALUS SFG sweep 2026-08-17): the original `if not raw: break`
# truncated enumeration silently — a fetch failure and "no more results" were the
# same exit, with no count. §2 already reported "{bad} fetch failures"; that honest
# form is extended here. enum_truncated counts pages LOST to failure, and is
# reported at the end so a short filing set can never look complete.
enum_truncated = 0
enum_exhausted = False
for frm in range(0, 300, 10):
    u = ("https://efts.sec.gov/LATEST/search-index?q=%22Athene+Global+Funding%22"
         f"&forms=NPORT-P&startdt={START_DT}&enddt={END_DT}&from={frm}")
    raw = get(u)
    if not raw:
        enum_truncated += 1
        print(f"    [1!] page from={frm}: FETCH FAILED — enumeration truncated", flush=True)
        break
    try:
        hits = json.loads(raw)["hits"]["hits"]
    except Exception:
        enum_truncated += 1
        print(f"    [1!] page from={frm}: PARSE FAILED — enumeration truncated", flush=True)
        break
    if not hits:
        enum_exhausted = True
        break
    for h in hits:
        acc, doc = h["_id"].split(":")
        s = h["_source"]
        filings[acc] = (s["ciks"][0], s.get("period_ending"), s["display_names"][0])
    time.sleep(0.12)
    if len(filings) >= MAX_FILINGS:
        break
print(f"    {len(filings)} filings"
      f" | enumeration {'EXHAUSTED (complete to the query bound)' if enum_exhausted else 'STOPPED EARLY'}"
      f" | pages lost to failure: {enum_truncated}"
      f"{'  ⚠️ FILING SET IS INCOMPLETE — do not read counts as a population' if enum_truncated else ''}",
      flush=True)

# ---------- 2. pull each filing, extract the 7 issuers' debt holdings ----------
HOLD = re.compile(r"<invstOrSec>(.*?)</invstOrSec>", re.S)
def tag(blob, t):
    m = re.search(rf"<{t}>(.*?)</{t}>", blob, re.S)
    return m.group(1).strip() if m else None

rows = []
bad = 0
for n, (acc, (cik, period, name)) in enumerate(sorted(filings.items())[:MAX_FILINGS], 1):
    nod = acc.replace("-", "")
    xml = get(f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{nod}/primary_doc.xml")
    if not xml:
        bad += 1
        continue
    for blob in HOLD.findall(xml):
        nm = (tag(blob, "name") or "") + " " + (tag(blob, "title") or "")
        who = next((k for k, pat in ISSUERS.items() if re.search(pat, nm, re.I)), None)
        if not who:
            continue
        bal, val = tag(blob, "balance"), tag(blob, "valUSD")
        mat, cpn = tag(blob, "maturityDt"), tag(blob, "annualizedRt")
        units = tag(blob, "units")
        if not (bal and val and mat and cpn):
            continue
        try:
            bal, val, cpn = float(bal), float(val), float(cpn)
        except ValueError:
            continue
        if units and units != "PA":      # principal amount only
            continue
        if bal <= 0 or val <= 0:
            continue
        rows.append(dict(acc=acc, cik=cik, fund=name, period=period, issuer=who,
                         cusip=(tag(blob, "cusip") or "").strip(),
                         par=bal, val=val, price=100.0 * val / bal,
                         coupon=cpn, maturity=mat[:10]))
    if n % 20 == 0:
        print(f"    {n}/{min(len(filings),MAX_FILINGS)} filings, {len(rows)} holdings", flush=True)
    time.sleep(0.10)
print(f"[2] {len(rows)} raw holdings, {bad} fetch failures", flush=True)

# ---------- 3. dedup, sanity-filter, compute YTM ----------
seen, clean = set(), []
for r in rows:
    k = (r["cik"], r["cusip"], r["maturity"], r["period"])
    if k in seen:
        continue
    seen.add(k)
    if not (60 < r["price"] < 140):        # drop unit/par mismatches
        continue
    clean.append(r)

def ytm(price, coupon_pct, years, freq=2):
    """Bisection YTM. price per 100 par, coupon in pct, years to maturity."""
    if years <= 0.05:
        return None
    c = coupon_pct / freq
    n = max(1, int(round(years * freq)))
    lo, hi = -0.5, 60.0
    for _ in range(200):
        mid = (lo + hi) / 2
        d = mid / 100.0 / freq
        pv = sum(c / (1 + d) ** i for i in range(1, n + 1)) + 100.0 / (1 + d) ** n
        if pv > price:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

for r in clean:
    try:
        pe = datetime.date.fromisoformat(r["period"])
        md = datetime.date.fromisoformat(r["maturity"])
    except Exception:
        r["yrs"] = None
        continue
    r["yrs"] = (md - pe).days / 365.25
    r["ytm"] = ytm(r["price"], r["coupon"], r["yrs"]) if r["yrs"] and r["yrs"] > 0.05 else None

clean = [r for r in clean if r.get("ytm") is not None and 0 < r["ytm"] < 25 and r["yrs"] < 31]
print(f"[3] {len(clean)} priced holdings after dedup/sanity", flush=True)

# ---------- 4. matched-fund restriction: fund must hold ATHENE + >=1 peer ----------
byfund = collections.defaultdict(set)
for r in clean:
    byfund[(r["cik"], r["period"])].add(r["issuer"])
matched = {f for f, iss in byfund.items() if "ATHENE" in iss and (iss & set(PEERS))}
mrows = [r for r in clean if (r["cik"], r["period"]) in matched]
print(f"[4] {len(matched)} matched funds (hold Athene AND >=1 peer); {len(mrows)} holdings", flush=True)

# ---------- 5. Treasury curve at each period end (FRED) ----------
import os
FRED = {2: "DGS2", 3: "DGS3", 5: "DGS5", 7: "DGS7", 10: "DGS10", 20: "DGS20", 30: "DGS30"}
key = os.environ.get("FRED_API_KEY", "")
if not key:
    for pth in ("/home/willi/Research-workspace/.env", "/home/willi/Research-workspace/FORGE/tools/market-data/.env"):
        try:
            for line in open(pth):
                if "FRED" in line and "=" in line:
                    key = line.split("=", 1)[1].strip().strip('"\'')
        except OSError:
            pass
curve = {}
# DEFECT FIX 1/2 support (DAEDALUS SFG sweep 2026-08-17):
#   curve_asof[period] = the date the curve values ACTUALLY came from (may lag the period).
#   MIN_TENORS / REQUIRED_TENORS = the emptiness test replacement. 5Y and 7Y bracket the
#   deliverable "5Y FABN" tenor; without both, a 5-7y spread is an extrapolation dressed
#   as an interpolation. 2 and 10 anchor the short and long ends of the bracket.
curve_asof = {}
MIN_TENORS = 5
REQUIRED_TENORS = (2, 5, 7, 10)
periods = sorted({r["period"] for r in mrows})
for pe in periods:
    curve[pe] = {}
    for t, sid in FRED.items():
        u = (f"https://api.stlouisfed.org/fred/series/observations?series_id={sid}"
             f"&api_key={key}&file_type=json&observation_start={pe}&observation_end={pe}")
        raw = get(u)
        try:
            obs = json.loads(raw)["observations"]
            v = float(obs[0]["value"])
            curve[pe][t] = v
        except Exception:
            pass
        time.sleep(0.08)
    # DEFECT FIX 2 (DAEDALUS SFG sweep 2026-08-17): the original test was
    # `if not curve[pe]` — EMPTY only. A PARTIAL curve (say only DGS2 and DGS30
    # landing) passed it, the fallback never fired, and tsy() then interpolated a
    # 7Y benchmark BETWEEN THE 2Y AND THE 30Y POINT. Require a minimum tenor set.
    if len(curve[pe]) < MIN_TENORS or not (set(REQUIRED_TENORS) <= set(curve[pe])):
        d0 = datetime.date.fromisoformat(pe)
        for back in range(1, 6):
            d = (d0 - datetime.timedelta(days=back)).isoformat()
            trial = {}
            for t, sid in FRED.items():
                u = (f"https://api.stlouisfed.org/fred/series/observations?series_id={sid}"
                     f"&api_key={key}&file_type=json&observation_start={d}&observation_end={d}")
                raw = get(u)
                try:
                    trial[t] = float(json.loads(raw)["observations"][0]["value"])
                except Exception:
                    pass
            if len(trial) >= MIN_TENORS and set(REQUIRED_TENORS) <= set(trial):
                curve[pe] = trial
                curve_asof[pe] = d          # DEFECT FIX 1: record WHICH DATE this curve is
                break
    # DEFECT FIX 1 (DAEDALUS SFG sweep 2026-08-17): the original printed the PERIOD
    # as the key and never the curve's own date, so `[5] curve 2026-06-30: {...}`
    # rendered identically whether the values were from 6/30 or 6/25, and the
    # printed penalty inherited the backfill silently. Stamp the source date.
    _asof = curve_asof.get(pe, pe)
    _lag = (datetime.date.fromisoformat(pe) - datetime.date.fromisoformat(_asof)).days
    _ok = len(curve[pe]) >= MIN_TENORS and set(REQUIRED_TENORS) <= set(curve[pe])
    print(f"[5] period {pe} | curve as-of {_asof}"
          f"{f' (BACKFILLED {_lag}d)' if _lag else ' (exact)'}"
          f" | tenors {sorted(curve[pe])}"
          f" | {'OK' if _ok else '⚠️ BELOW MINIMUM TENOR SET — interpolation refused'}"
          f": {curve[pe]}", flush=True)
    if not _ok:
        curve[pe] = {}   # refuse to serve an under-specified curve to tsy()

MAX_BRACKET = 5   # years; 3->5, 5->7, 7->10 are fine, 2->30 is not
def tsy(pe, yrs):
    c = curve.get(pe) or {}
    if not c:
        return None
    ts = sorted(c)
    lo = max([t for t in ts if t <= yrs], default=ts[0])
    hi = min([t for t in ts if t >= yrs], default=ts[-1])
    if lo == hi:
        return c[lo]
    # DEFECT FIX 2 (cont.): never interpolate across a bracket wider than MAX_BRACKET
    # years. A 2y-to-30y "interpolation" for a 7y bond is not a benchmark.
    if (hi - lo) > MAX_BRACKET:
        return None
    w = (yrs - lo) / (hi - lo)
    return c[lo] * (1 - w) + c[hi] * w

for r in mrows:
    b = tsy(r["period"], r["yrs"])
    r["spread"] = (r["ytm"] - b) * 100 if b is not None else None
mrows = [r for r in mrows if r.get("spread") is not None and -50 < r["spread"] < 800]

# ---------- 6. report ----------
def bucket(y):
    return "0-3y" if y < 3 else "3-6y" if y < 6 else "6-11y" if y < 11 else "11y+"

print("\n" + "=" * 78)
print("FABN PEER-RELATIVE SPREAD — NPORT-P holder marks, matched funds only")
print(f"periods: {periods} | matched funds: {len(matched)} | holdings: {len(mrows)}")
print("=" * 78)
agg = collections.defaultdict(list)
for r in mrows:
    agg[(bucket(r["yrs"]), r["issuer"])].append(r["spread"])

for b in ["0-3y", "3-6y", "6-11y", "11y+"]:
    present = [(i, v) for (bb, i), v in agg.items() if bb == b and len(v) >= 2]
    if not present:
        continue
    print(f"\n--- {b} ---")
    ath = None
    peer_pool = []
    for i, v in sorted(present, key=lambda x: -statistics.median(x[1])):
        med = statistics.median(v)
        print(f"   {i:<11} n={len(v):<4} median T+{med:6.1f}bp   (min {min(v):6.1f} / max {max(v):6.1f})")
        if i == "ATHENE":
            ath = med
        else:
            peer_pool += v
    if ath is not None and peer_pool:
        pm = statistics.median(peer_pool)
        print(f"   >>> ATHENE PEER PENALTY: {ath - pm:+.1f}bp  (peer median T+{pm:.1f}, n={len(peer_pool)})")

out = "/home/willi/Research-workspace/AGENTS/SHADE/research/FABN_PEER_SPREAD_NPORT_2026-07-27.json"
# DEFECT FIX 1b (found 2026-08-28 while committing the rerun): fix 1 stamped the
# PRINTED curve but not the SAVED artifact — and the run log is gitignored (*.log),
# so the backfill provenance would have survived only in an uncommitted file. The
# same defect one layer down. Persist curve_asof and the window with the results.
json.dump({"periods": periods, "curve": curve, "curve_asof": curve_asof,
           "window": {"start": START_DT, "end": END_DT},
           "enum_truncated": enum_truncated, "enum_exhausted": enum_exhausted,
           "n_matched_funds": len(matched),
           "rows": mrows}, open(out, "w"), indent=1)
print(f"\nwrote {out}")
