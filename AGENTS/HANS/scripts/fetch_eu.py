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
        # ⚠️ `country=EU` returns total=0 — there is NO 'EU' country code. The EU
        # aggregate is `type=EU` (equivalently /api/data/eu). Found 2026-08-28 by
        # testing rather than assuming; the wrong form fails SILENTLY with an empty
        # data array and a 200, which reads as "no data today" rather than "wrong query".
        req = urllib.request.Request("https://agsi.gie.eu/api?type=EU&size=1",
                                     headers={"x-key": key, "User-Agent": "HANS/1.0"})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            d = json.load(r)
        recs = d.get("data") or []
        if not recs:
            return None, "AGSI returned an EMPTY data array (query form wrong, or gas day unpublished)"
        rec = recs[0]
        if rec.get("full") in (None, "", "-"):
            return None, f"AGSI gas day {rec.get('gasDayStart')} has no 'full' value yet (D+1 lag)"
        return (rec.get("gasDayStart"), float(rec["full"]), rec.get("trend")), None
    except Exception as e:
        return None, f"AGSI pull failed: {str(e)[:60]}"


def main():
    """Prints the report AND returns structured status so a caller can act on it.

    Returns {"observations": [...], "failures": [str], "breached": [threshold_id]}
    ⚠️ ADDED 2026-08-28 on review: this function previously ONLY printed. boot.py
    therefore could not see ECB/AGSI failures or breaches, so a run with working
    Yahoo and FAILED European primaries would exit 0 CLEAN while the screen said
    PULL FAILED — exit semantics advertising a wider perimeter than they checked.
    [[finding_instrument_reports_clean_against_the_wrong_reference]]
    """
    obs, failures, breached = [], [], []
    print("\n  EUROPEAN PRIMARY PULL — ECB Data Portal (keyless) + GIE AGSI+")

    aaa = ecb(AAA10Y, 2)
    if aaa:
        d, v = aaa[0]
        prev = f"  (prev {aaa[1][1]:.3f} on {aaa[1][0]})" if len(aaa) > 1 else ""
        em = "🔴" if v > 4.50 else "🟠" if v > 3.75 else "🟡" if v > 3.00 else "🟢"
        print(f"  {em} Euro-area AAA 10Y   {v:6.3f}%  [{d}]{prev}   HANS-T-05 bands 3.00/3.75/4.50")
        print(f"     ⚠️  AAA CURVE, not Germany specifically — a proxy. Referent stated on purpose.")
        obs.append(("HANS-T-05", v, d))
        if v > 3.00:
            breached.append("HANS-T-05")
    else:
        print("  ⚠️  Euro-area AAA 10Y — PULL FAILED (reported, not skipped)")
        failures.append("ECB euro-area AAA 10Y")

    de = ecb(CTRY["DE"])
    print("\n  Per-country 10Y (MONTHLY convergence series) + spreads vs DE:")
    if de:
        dd, dv = de[0]
        print(f"     DE {dv:6.3f}%  [{dd}]")
        for c in ("IT", "FR", "ES"):
            r = ecb(CTRY[c])
            if not r:
                print(f"     {c} — PULL FAILED")
                failures.append(f"ECB {c} 10Y")
                continue
            cd, cv = r[0]
            sp = (cv - dv) * 100
            note = ""
            # COMPOUND rows: T-09/T-10 need BOTH the spread leg AND the level leg.
            # A single leg is NOT a breach — recording that correctly matters, because
            # reporting one leg as a fire is how a compound gate gets simplified away.
            if c == "IT":
                note = "  T-09 spread>200 AND BTP>5.50"
                if sp > 200 and cv > 5.50: breached.append("HANS-T-09")
            if c == "FR":
                note = "  T-10 spread>100 AND OAT>4.50"
                if sp > 100 and cv > 4.50: breached.append("HANS-T-10")
            obs.append((f"{c}-10Y", cv, cd))
            print(f"     {c} {cv:6.3f}%  [{cd}]   spread {sp:6.1f}bp{note}")
        print("     ⚠️  MONTHLY. Lags a daily print by weeks — cross-check, not a live level.")
    else:
        print("     ⚠️  DE base leg PULL FAILED — spreads not computed (never computed off a stale base)")
        failures.append("ECB DE 10Y (base leg — spreads not computed)")

    st, err = agsi_eu()
    print("\n  EU gas storage (GIE AGSI+):")
    if st:
        NORM = 82.0  # 5-yr seasonal norm for this date [GEF, 2026-08-28]
        gap = st[1] - NORM
        em = "🔴" if gap < -25 else "🟠" if gap < -15 else "🟢"
        try:
            tr = f" trend {float(st[2]):+.2f}pp/d"
        except (TypeError, ValueError):
            tr = ""   # AGSI returns trend as a STRING and sometimes empty — coerce, never assume
        print(f"     {st[1]:.2f}% full  [gas day {st[0]}]{tr}   ✅ PRIMARY (GIE AGSI+)")
        print(f"  {em} GAP TO 5-YR NORM {gap:+.1f}pp  (vs {NORM:.1f}% norm)   HANS-T-08 bands -15 orange / -25 red")
        print(f"     ⚠️ PERIMETER MISMATCH, STATED: fill is AGSI primary; the {NORM:.1f}% norm is from GEF,")
        print(f"        a DIFFERENT source whose EU member-set may differ. The GAP is therefore a")
        print(f"        CROSS-SOURCE derivation. Proper fix: compute the norm from AGSI history.")
        obs.append(("HANS-T-08", gap, st[0]))
        if gap < -15:
            breached.append("HANS-T-08")
    else:
        print(f"     🔑 {err}")
        failures.append(f"AGSI+ EU storage ({err[:40]})")

    print("\n  🔴 STILL MANUAL — named so this file cannot imply coverage:")
    print("     UK 10Y / 30Y gilt (HANS-T-06 / T-13) — no free DAILY source found.")
    print("     FRED IRLTLT01GBM156N is monthly and ~2mo lagged: a cross-check, not a level.\n")
    return {"observations": obs, "failures": failures, "breached": breached}


if __name__ == "__main__":
    _r = main()
    sys.exit(1 if _r["failures"] else 0)
