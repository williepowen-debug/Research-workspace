#!/usr/bin/env python3
"""DM sovereign long-end cross-section — BOND's standing series (Will-ruled 8/10 forum scope).

Built 2026-09-01. Until today this instrument existed only as an ad hoc 8/20 pull
(`analysis/2026-08-20_cross-section_horizon-instability.md`); the scope text has said
"standing series at BOND's own primaries" since 8/10 and nothing on any surface said
it was not one. SAM's 8/20 ask is what found that, and the 9/3 deliverable is what
forces it to be a tool.

FOUR PRIMARY LEGS, each at the issuer:
  US 10Y  DGS10                                    FRED        daily
  EA 10Y  B.U2.EUR.4F.G_N_A.SV_C_YM.SR_10Y (AAA)   ECB SDW     daily
  UK 10Y  IUDMNPY (nominal par)                    BoE IADB    daily
  JP 10Y  historical/jgbcme_all.csv + jgbcme.csv      MOF         daily

THREE DEFECTS THIS FILE ENCODES SO THEY CANNOT RECUR — every one cost this desk a
false reading, and every one presented as "the source is unavailable":
  (1) MOF `historical/jgbcme_all.csv` ENDS AT THE PRIOR MONTH (and it lives under
      /historical/ -- the flat path 404s, which is defect (3) again). A last-value-carried-forward
      lookup against it alone silently produced JP delta = +0.0bp for EVERY August
      window and rendered those as real "Japan didn't move" readings. The two files
      are merged, and STALE_ENDPOINT_DAYS refuses any delta whose endpoint falls
      back more than 4 calendar days instead of quietly carrying one.
  (2) BoE IADB returns HTTP 302 with ZERO BYTES unless redirects are followed --
      which reads exactly like a refusal. urllib follows by default; the guard is
      the empty-payload check, not the status code.
  (3) The RBA leg was reported "not found" off `f2.1-data.csv` (MONTHLY, series
      FCMYGBAG10) when the daily file is `f2-data.csv` (FCMYGBAG10D). AU is not in
      this tool's core set for that reason -- it is a weekly-published file and the
      4 core legs are all daily. n=4 of this desk's claimed-unavailability-is-a-
      path-artifact class.

REPORTING RULE (8/20, non-negotiable): report RANK and MEDIAN beside the
min-across-legs bound, NEVER the min alone. On the 8/12->8/18 data the bound scored
4.8 of Japan's 7.8bp as idiosyncratic WHILE JAPAN SAT BELOW THE DM MEDIAN -- bound
and rank pointed opposite ways on the same data. min-across-legs is a crude LOWER
BOUND, not a factor decomposition; a true PC1 on n=4 would be dominated by the US,
the very leg being netted out.
"""
import csv, io, json, os, sys, time, urllib.request, urllib.error
from datetime import date, datetime, timedelta

REPO = __import__("subprocess").check_output(["git","rev-parse","--show-toplevel"],
                                             cwd=os.path.dirname(os.path.abspath(__file__))).decode().strip()
sys.path.insert(0, os.path.join(REPO, "FORGE/tools/market-data"))

STALE_ENDPOINT_DAYS = 4
UA = {"User-Agent": "Mozilla/5.0 (BOND/dm_cross_section)"}


def _get(url, timeout=45):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        body = r.read()
    if not body:                      # defect (2): 302-with-0-bytes reads like refusal
        raise RuntimeError(f"EMPTY payload from {url[:80]} (redirect/robots?)")
    return body.decode("utf-8", "replace")


def leg_us():
    import fetch
    for f in __import__("glob").glob(os.path.join(REPO, "FORGE/tools/market-data/.cache/fred_DGS10*.json")):
        os.remove(f)
    d = fetch.fred_fetch("DGS10", limit=400)
    rows = d["observations"] if isinstance(d, dict) else d
    out = {}
    for o in rows:
        dt = o["date"] if isinstance(o, dict) else o[0]
        v = o["value"] if isinstance(o, dict) else o[1]
        if v not in (".", "", None):
            out[dt] = float(v)
    return out


def leg_ea():
    url = ("https://data-api.ecb.europa.eu/service/data/YC/"
           "B.U2.EUR.4F.G_N_A.SV_C_YM.SR_10Y?format=csvdata&startPeriod=2026-06-01")
    out = {}
    for row in csv.DictReader(io.StringIO(_get(url))):
        try:
            out[row["TIME_PERIOD"]] = float(row["OBS_VALUE"])
        except (KeyError, ValueError):
            pass
    return out


def leg_uk():
    url = ("https://www.bankofengland.co.uk/boeapps/iadb/fromshowcolumns.asp?"
           "csv.x=yes&Datefrom=01/Jun/2026&Dateto=now&SeriesCodes=IUDMNPY"
           "&CSVF=TN&UsingCodes=Y&VPD=Y&VFD=N")
    out = {}
    for row in csv.reader(io.StringIO(_get(url))):
        if len(row) < 2:
            continue
        try:
            d = datetime.strptime(row[0].strip(), "%d %b %Y").date().isoformat()
            out[d] = float(row[1])
        except ValueError:
            continue
    return out


def leg_jp():
    """defect (1): the _all file ends at the prior month. MERGE, never carry forward."""
    out, seen = {}, []
    for name in ("historical/jgbcme_all.csv", "jgbcme.csv"):
        try:
            txt = _get(f"https://www.mof.go.jp/english/policy/jgbs/reference/interest_rate/{name}")
        except Exception as e:
            print(f"   [jp] {name}: {e}", file=sys.stderr)
            continue
        hdr, n = None, 0
        for row in csv.reader(io.StringIO(txt)):
            if not row:
                continue
            if row[0].strip().lower().startswith("date"):
                hdr = [c.strip() for c in row]
                continue
            if hdr is None or "10Y" not in hdr:
                continue
            try:
                y, m, d = row[0].split("/")
                iso = f"{int(y)+1988:04d}-{int(m):02d}-{int(d):02d}" if int(y) < 1000 \
                      else f"{int(y):04d}-{int(m):02d}-{int(d):02d}"
                out[iso] = float(row[hdr.index("10Y")])
                n += 1
            except (ValueError, IndexError):
                continue
        seen.append(f"{name}:{n}")
    print(f"   [jp] merged {' + '.join(seen)}", file=sys.stderr)
    return out


def asof(series, target):
    """Latest obs at or before target. Returns (date, value, fallback_days)."""
    t = date.fromisoformat(target)
    cands = [d for d in series if date.fromisoformat(d) <= t]
    if not cands:
        return None, None, None
    d = max(cands)
    return d, series[d], (t - date.fromisoformat(d)).days


def coverage(series, start, end):
    """Observation COUNT inside the window -- the check the endpoint guard cannot make.

    STALE_ENDPOINT_DAYS only asks whether a leg's ENDPOINT falls back. It says nothing
    about how densely the leg is observed BETWEEN the endpoints, and a two-point delta
    reads identically off 15 observations and off 2. Unequal density is a property of
    the SET, not of any member, so no per-series freshness check can see it -- the same
    shape as the coverage-artifact bound this tool already warns about (KB-BND-207).

    Prompted by SAM 2026-09-01: a derived ledger inherited a hole from its source
    ledger, looked contiguous, and reported nothing. An absent row is invisible to a
    range check, to a cross-source compare, and to a reader who knows the number.
    """
    return sum(1 for d in series if start <= d <= end)


def main():
    start = sys.argv[1] if len(sys.argv) > 1 else "2026-08-13"
    end = sys.argv[2] if len(sys.argv) > 2 else date.today().isoformat()
    print(f"[dm_cross_section] window {start} -> {end}   (run {datetime.now():%Y-%m-%d %H:%M} local)\n")

    legs, errs = {}, {}
    for name, fn in (("US 10Y", leg_us), ("EA AAA 10Y", leg_ea),
                     ("UK 10Y", leg_uk), ("JP 10Y", leg_jp)):
        try:
            legs[name] = fn()
        except Exception as e:
            errs[name] = str(e)

    rows, stale = [], []
    for name, s in legs.items():
        d0, v0, _ = asof(s, start)
        d1, v1, fb = asof(s, end)
        if v0 is None or v1 is None:
            errs[name] = "no observation in range"
            continue
        if fb is not None and fb > STALE_ENDPOINT_DAYS:
            stale.append(f"{name}: endpoint {d1} falls back {fb}d from {end}")
        rows.append((name, d0, v0, d1, v1, round((v1 - v0) * 100, 1), fb,
                     coverage(s, start, end)))

    print(f"{'Leg':<12}{'start':<13}{'value':>7}   {'end':<13}{'value':>7}   "
          f"{'delta bp':>9}  {'lag':>4}  {'obs':>4}")
    for n, d0, v0, d1, v1, dl, fb, nobs in rows:
        print(f"{n:<12}{d0:<13}{v0:>7.3f}   {d1:<13}{v1:>7.3f}   {dl:>+9.1f}  "
              f"{str(fb)+'d':>4}  {nobs:>4}")

    # DENSITY — unequal observation counts make a two-point delta not like-for-like
    if len(rows) > 1:
        counts = [r[7] for r in rows]
        lo, hi = min(counts), max(counts)
        if hi and lo < 0.6 * hi:
            thin = [f"{r[0]} ({r[7]} obs)" for r in rows if r[7] < 0.6 * hi]
            print(f"\n⚠️ UNEQUAL COVERAGE INSIDE THE WINDOW — densest leg has {hi} obs, "
                  f"thinnest {lo}.")
            print(f"   Thin: {', '.join(thin)}")
            print("   A two-point delta reads IDENTICALLY off 15 observations and off 2.")
            print("   Matched endpoints do NOT make legs like-for-like if their interior")
            print("   density differs — treat a thin leg's delta as lower-confidence and")
            print("   NEVER let it set a min/max bound (that is the KB-BND-207 artifact).")

    if errs:
        print("\n🔴 LEGS THAT DID NOT RESOLVE (a missing leg is NOT a zero):")
        for n, e in errs.items():
            print(f"   {n}: {e}")
    if stale:
        print(f"\n⚠️ STALE ENDPOINT (> {STALE_ENDPOINT_DAYS}d) — delta reported but do NOT treat like-for-like:")
        for s in stale:
            print(f"   {s}")

    if len(rows) < 2:
        print("\n🔴 fewer than 2 legs — no cross-sectional statement possible.")
        return 2

    ds = sorted(r[5] for r in rows)
    med = ds[len(ds) // 2] if len(ds) % 2 else (ds[len(ds) // 2 - 1] + ds[len(ds) // 2]) / 2
    ordering = " > ".join(r[0] for r in sorted(rows, key=lambda r: -r[5]))

    print(f"\n== CROSS-SECTION (n={len(rows)} legs) ==")
    print(f"   ordering            : {ordering}   ⚠️ RANK IS HORIZON-UNSTABLE — quote the window {start}→{end} in the SAME sentence as any rank (SAM 9/1: 4 windows, JP ranked 4/4, 3/4, 3/4 and 1/4)")
    print(f"   DM median delta     : {med:+.1f}bp")
    print(f"   min-across-legs     : {min(ds):+.1f}bp   ⚠️ a crude LOWER BOUND, NOT a factor decomposition")
    print(f"   spread (max-min)    : {max(ds)-min(ds):.1f}bp")
    same = all(d > 0 for d in ds) or all(d < 0 for d in ds)
    print(f"   common DIRECTION    : {'YES — every leg same sign' if same else 'NO — legs disagree in sign'}")
    for n, _, _, _, _, dl, _, _ in rows:
        rank = sorted(ds, reverse=True).index(dl) + 1
        print(f"     {n:<12} {dl:>+7.1f}bp   rank {rank}/{len(ds)}   "
              f"{'ABOVE' if dl > med else 'BELOW' if dl < med else 'AT'} DM median")
    print("\n⚠️ REPORT RANK + MEDIAN BESIDE THE BOUND, NEVER THE BOUND ALONE (8/20 rule).")
    print("   On 8/12→8/18 the bound scored 4.8 of Japan's 7.8bp idiosyncratic WHILE")
    print("   Japan sat BELOW the DM median — bound and rank pointed opposite ways.")
    print("⚠️ RANK IS HORIZON-UNSTABLE: 7 one-week windows gave 7 DISTINCT orderings,")
    print("   every sovereign spanning a rank spread of 3. Quote the horizon with the rank.")
    return 1 if (errs or stale) else 0


if __name__ == "__main__":
    sys.exit(main())
