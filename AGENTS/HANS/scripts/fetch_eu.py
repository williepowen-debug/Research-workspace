#!/usr/bin/env python3
"""
HANS European primary-source fetcher — ECB Data Portal (+ optional GIE AGSI+).

WHY THIS EXISTS: on 2026-08-28 this desk reported that the Bund, EGB spreads and
EU storage were "not auto-pullable" and would stay manual. That was WRONG — it
was a claim about yfinance, not about the world. The ECB Data Portal serves the
euro-area yield curve DAILY and per-country 10Y yields MONTHLY, with NO API KEY.
Checking the primary before declaring an instrument unreachable is the lesson.
  [[finding_unfetched_is_not_unavailable]]

SOURCES, all primary:
  ECB Data Portal  data-api.ecb.europa.eu   no key      daily + monthly
  GIE AGSI+        agsi.gie.eu/api          FREE key    daily storage
                   -> set AGSI_API_KEY in FORGE/tools/market-data/.env

STILL UNREACHABLE and honestly named (do not let this file imply coverage):
  UK gilt 10Y/30Y — no free DAILY source found. FRED IRLTLT01GBM156N is MONTHLY
  and lagged ~2 months (Jun-2026 = 4.796 vs an Aug TE print of 5.1548), so it is
  a cross-check, NOT a level. HANS-T-06 / T-13 stay manual.
"""
import csv, io, json, os, sys, urllib.request
from pathlib import Path

ECB = "https://data-api.ecb.europa.eu/service/data"
TIMEOUT = 25
# euro-area AAA spot curve — the standard daily Bund proxy
AAA10Y = "YC/B.U2.EUR.4F.G_N_A.SV_C_YM.SR_10Y"
# long-term rate for convergence purposes, per country (MONTHLY)
CTRY = {c: f"IRS/M.{c}.L.L40.CI.0000.EUR.N.Z" for c in ("DE", "IT", "FR", "ES")}


def _get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "HANS/1.0"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return r.read().decode("utf-8", "replace")


def ecb(series, n=1):
    """Return [(period, value)] most-recent-first, or [] on any failure."""
    try:
        raw = _get(f"{ECB}/{series}?lastNObservations={n}&format=csvdata")
        rows = list(csv.DictReader(io.StringIO(raw)))
        out = [(r["TIME_PERIOD"], float(r["OBS_VALUE"])) for r in rows if r.get("OBS_VALUE")]
        return sorted(out, reverse=True)
    except Exception:
        return []


def agsi_eu():
    """EU aggregate storage fill %. Needs a FREE key; returns None without one."""
    key = os.environ.get("AGSI_API_KEY", "")
    if not key:
        env = Path(__file__).resolve().parents[3] / "FORGE/tools/market-data/.env"
        if env.exists():
            for line in env.read_text().splitlines():
                if line.startswith("AGSI_API_KEY="):
                    key = line.split("=", 1)[1].strip()
    if not key:
        return None, "no AGSI_API_KEY — free signup at agsi.gie.eu/account"
    try:
        req = urllib.request.Request("https://agsi.gie.eu/api?country=EU&size=1",
                                     headers={"x-key": key, "User-Agent": "HANS/1.0"})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            d = json.load(r)
        rec = (d.get("data") or [{}])[0]
        return (rec.get("gasDayStart"), float(rec.get("full"))), None
    except Exception as e:
        return None, f"AGSI pull failed: {str(e)[:60]}"


def main():
    print("\n  EUROPEAN PRIMARY PULL — ECB Data Portal (keyless) + GIE AGSI+")

    aaa = ecb(AAA10Y, 2)
    if aaa:
        d, v = aaa[0]
        prev = f"  (prev {aaa[1][1]:.3f} on {aaa[1][0]})" if len(aaa) > 1 else ""
        em = "🔴" if v > 4.50 else "🟠" if v > 3.75 else "🟡" if v > 3.00 else "🟢"
        print(f"  {em} Euro-area AAA 10Y   {v:6.3f}%  [{d}]{prev}   HANS-T-05 bands 3.00/3.75/4.50")
        print(f"     ⚠️  AAA CURVE, not Germany specifically — a proxy. Referent stated on purpose.")
    else:
        print("  ⚠️  Euro-area AAA 10Y — PULL FAILED (reported, not skipped)")

    de = ecb(CTRY["DE"])
    print("\n  Per-country 10Y (MONTHLY convergence series) + spreads vs DE:")
    if de:
        dd, dv = de[0]
        print(f"     DE {dv:6.3f}%  [{dd}]")
        for c in ("IT", "FR", "ES"):
            r = ecb(CTRY[c])
            if not r:
                print(f"     {c} — PULL FAILED")
                continue
            cd, cv = r[0]
            sp = (cv - dv) * 100
            note = ""
            if c == "IT": note = "  T-09 spread leg (>200bp)"
            if c == "FR": note = "  T-10 spread leg (>100bp)"
            print(f"     {c} {cv:6.3f}%  [{cd}]   spread {sp:6.1f}bp{note}")
        print("     ⚠️  MONTHLY. Lags a daily print by weeks — cross-check, not a live level.")
    else:
        print("     ⚠️  DE base leg PULL FAILED — spreads not computed (never computed off a stale base)")

    st, err = agsi_eu()
    print("\n  EU gas storage (GIE AGSI+):")
    if st:
        print(f"     {st[1]:.2f}% full  [gas day {st[0]}]   HANS-T-08 measures the GAP to the 5-yr norm, not this level")
    else:
        print(f"     🔑 {err}")

    print("\n  🔴 STILL MANUAL — named so this file cannot imply coverage:")
    print("     UK 10Y / 30Y gilt (HANS-T-06 / T-13) — no free DAILY source found.")
    print("     FRED IRLTLT01GBM156N is monthly and ~2mo lagged: a cross-check, not a level.\n")


if __name__ == "__main__":
    sys.exit(main())
