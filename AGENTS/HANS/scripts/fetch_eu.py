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


def _agsi_key():
    key = os.environ.get("AGSI_API_KEY", "")
    if not key:
        # DUPLICATE PATH-WALK: the SAME .env is resolved with the SAME parents[3] depth in
        # pmi_ism_lead_test.py. They agree today and would diverge on a REFACTOR (one script moving a
        # level), NOT at the moment of failure — graded LOW severity on the 2026-09-19
        # divergence sweep for exactly that reason, and left in place rather than coupled
        # through a shared module for one path. If you move either script, fix BOTH.
        env = Path(__file__).resolve().parents[3] / "FORGE/tools/market-data/.env"
        if env.exists():
            for line in env.read_text().splitlines():
                if line.startswith("AGSI_API_KEY="):
                    key = line.split("=", 1)[1].strip()
    return key


def agsi_eu():
    """EU aggregate storage fill %. Needs a FREE key; returns None without one."""
    # ONE key path for the whole module. This block used to be duplicated here and in
    # _agsi_key(), which is two resolution orders that can silently diverge — caught
    # 2026-09-19 when an injection test poisoned the env var and only ONE of the two
    # callers saw it. [[finding_guard_correctness_and_wiring_are_independent]]
    key = _agsi_key()
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
            # 🔴 THREE causes produce this identical 200 + empty array, and one of them is
            # a DEAD KEY. Verified by negative control 2026-09-19 (PROME probe, reproduced
            # here): real key -> 1 rec · WRONG key -> 0 rec · NO header -> 0 rec. A rejected
            # key is shape-identical to an unpublished gas day, so silent expiry produces
            # EXACTLY the message that means "come back tomorrow" — and a desk would defer
            # its checkpoint, correctly by the letter, forever.
            return None, f"AGSI returned an EMPTY data array — {_agsi_why_empty(key)}"
        rec = recs[0]
        if rec.get("full") in (None, "", "-"):
            # ⚠️ OPEN QUESTION (PROME 2026-09-19, NOT established): the newest gas day on
            # Saturday 09-19 was 09-17 = D+2, not the D+1 this comment has always claimed.
            # A weekend publication schedule explains it equally well and ONE Saturday
            # observation cannot separate the two. CHECK ON A WEEKDAY. If still D+2 then,
            # this comment is wrong and anything keyed to D+1 freshness is a day optimistic.
            return None, f"AGSI gas day {rec.get('gasDayStart')} has no 'full' value yet (lag D+1, possibly D+2 — unresolved)"
        return (rec.get("gasDayStart"), float(rec["full"]), rec.get("trend")), None
    except Exception as e:
        return None, f"AGSI pull failed: {str(e)[:60]}"


# ⚑ EMPTY-KEY DISCRIMINATOR — re-check by 2026-12-19.
# GIE quirk, established by negative control on 2026-09-19 and reproduced independently:
# an x-key header PRESENT but set to the EMPTY STRING returns DATA, while a WRONG key and
# an ABSENT header both return an empty array. That asymmetry is the only signal available
# that separates "my key was rejected" from "this gas day is not published yet".
#
# ⚠️ IT IS VENDOR-QUIRK-DEPENDENT AND THAT IS STATED HERE ON PURPOSE. If GIE tightens the
# empty-key path this probe returns empty always, and we report NO_DATA for a dead key —
# i.e. it reverts to the status quo ante. FAILS IN THE SAFE DIRECTION (no worse than having
# no probe), never toward a false "your key is fine".
#
# 🔴 METHOD NOTE, because it nearly cost the finding: the FIRST attempt to reproduce this
# used `curl -H "x-key: "`, which makes curl DROP THE HEADER ENTIRELY (0 on the wire) — so
# it silently tested the ABSENT case and "disproved" a control that is real. The correct
# curl form is `-H "x-key;"`; urllib with "" sends it faithfully. An empty result is a
# claim about YOUR REQUEST until the client is varied.
# [[finding_negative_reachability_is_a_claim_about_your_request]]
def _agsi_why_empty(key):
    """On an empty 200 from a real key: was the KEY rejected, or is there no data?

    Returns a human cause string. Never raises — this runs on an error path.
    """
    try:
        req = urllib.request.Request("https://agsi.gie.eu/api?type=EU&size=1",
                                     headers={"x-key": "", "User-Agent": "HANS/1.0"})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            probe_recs = (json.load(r).get("data") or [])
    except Exception as e:
        return (f"cause UNDETERMINED (discriminator probe failed: {str(e)[:40]}). "
                "Treat as BLIND, not as 'no data yet'")
    if probe_recs:
        return ("🔴 KEY REJECTED — the empty-key probe DID return data, so the gas day HAS "
                "published and the credential is the problem. Rotate it at agsi.gie.eu/account. "
                "⛔ This is NOT 'come back tomorrow'")
    return ("gas day genuinely unpublished, OR the query form is wrong (type=EU, not country=EU). "
            "Key validity NOT implicated: the empty-key probe also returned nothing. "
            "⚠️ If GIE has tightened the empty-key path this probe can no longer discriminate "
            "(re-check due 2026-12-19) — in that case a dead key also lands here")


def agsi_norm(gas_day, years=5):
    """5-yr seasonal norm for THIS gas day, computed from AGSI's OWN history.

    🔴 THIS EXISTS BECAUSE THE PREVIOUS NORM WAS A HARDCODED 82.0 FROM GEF, FROZEN ON
    2026-08-28 AND APPLIED TO EVERY LATER DATE. Two independent defects in one constant:
      (a) CROSS-SOURCE — an AGSI fill minus a GEF norm is a gap neither source vouches for;
      (b) FROZEN SEASONAL — the true norm RISES through the injection season (85.05% on
          09-17 vs the carried 82.0), so a frozen constant makes the gap read BETTER as
          the season advances. That is a FAIL-OPEN drift: the alarm quietly relaxes with
          time, which is the direction a storage alarm must never fail in.
    Measured 2026-09-19: frozen 82.0 gave -12.9pp; AGSI-native gives -15.99pp. The band
    is -15. The stale constant had the fire on the wrong side of its own threshold.

    Returns (norm_mean, norm_median, n_years, [(year, full)]) or (None, None, 0, reason).
    ⛔ FAIL-CLOSED: on fewer than `years-1` usable years it returns None and the CALLER
    MUST PRINT NO GAP. It must never fall back to a constant — falling back is exactly
    the trade (loud-and-safe -> silent-and-certifying) this function was written to end.
    """
    key = _agsi_key()
    if not key:
        return None, None, 0, "no AGSI_API_KEY"
    try:
        y0, md = int(gas_day[:4]), gas_day[5:10]
    except (ValueError, TypeError, IndexError):
        return None, None, 0, f"unparseable gas day {gas_day!r}"
    got = []
    for y in range(y0 - years, y0):
        try:
            req = urllib.request.Request(
                f"https://agsi.gie.eu/api?type=EU&date={y}-{md}",
                headers={"x-key": key, "User-Agent": "HANS/1.0"})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                recs = (json.load(r).get("data") or [])
            if recs and recs[0].get("full") not in (None, "", "-"):
                got.append((y, float(recs[0]["full"])))
        except Exception:
            continue          # one missing year is survivable; the quorum test below is not
    if len(got) < years - 1:
        why = "" if got else " — ZERO years returned, which on this API is the DEAD-KEY shape, not flaky history"
        return None, None, len(got), f"only {len(got)}/{years} historical years reachable{why}"
    vals = sorted(v for _, v in got)
    n = len(vals)
    mean = sum(vals) / n
    median = vals[n // 2] if n % 2 else (vals[n // 2 - 1] + vals[n // 2]) / 2
    return mean, median, n, got


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
        try:
            tr = f" trend {float(st[2]):+.2f}pp/d"
        except (TypeError, ValueError):
            tr = ""   # AGSI returns trend as a STRING and sometimes empty — coerce, never assume
        print(f"     {st[1]:.2f}% full  [gas day {st[0]}]{tr}   ✅ PRIMARY (GIE AGSI+)")

        mean, median, nyr, meta = agsi_norm(st[0])
        if mean is None:
            # ⛔ FAIL-CLOSED: no norm => NO GAP PRINTED. Never fall back to a constant.
            print(f"     ⛔ 5-YR NORM NOT COMPUTED ({meta}) — NO GAP REPORTED THIS RUN.")
            print(f"        The gap is HANS-T-08's whole metric, so a missing norm is a BLIND row,")
            print(f"        not a quiet one. The fire's state is UNCHANGED — a blind day can never")
            print(f"        close it (registry exit clause, 2026-09-19).")
            failures.append("AGSI 5-yr norm (gap not computed — fail-closed)")
        else:
            gap = st[1] - mean
            em = "🔴" if gap <= -25 else "🟠" if gap <= -15 else "🟢"
            print(f"  {em} GAP TO 5-YR NORM {gap:+.2f}pp  (vs {mean:.2f}% norm)   HANS-T-08 bands -15 orange / -25 red")
            print(f"     ✅ SINGLE-SOURCE: fill AND norm both GIE AGSI+, same gas day {st[0][5:]} "
                  f"across {nyr} prior years {[y for y, _ in meta]}.")
            spread = abs(mean - median)
            if spread > 2.0:
                print(f"     ⚠️ norm mean {mean:.2f} vs median {median:.2f} differ by {spread:.2f}pp "
                      f"— the 5-yr window is SKEWED; gap on the median basis is {st[1]-median:+.2f}pp.")
            obs.append(("HANS-T-08", gap, st[0]))
            if gap <= -15:
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
