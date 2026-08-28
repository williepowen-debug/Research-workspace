#!/usr/bin/env python3
"""
OFR STFM + NY Fed Primary-Dealer pull — the funding-microstructure primaries FRED does NOT carry.

WHY THIS EXISTS
FRED covers the funding RATE side well (SOFR/SOFR99/IORB/EFFR/RRPONTSYD). It does NOT
carry the dealer-side plumbing — GCF interdealer repo rates, DVP/tri-party segments, or
settlement fails. That is the segment where a dealer-side squeeze shows up FIRST, and it
was the load-bearing gap under the 2026-07-16 funding-gate calibration verdict
(`output/2026-07-16_funding-gate-calibration.md`), which had to rest on the SOFR
distribution alone. Built 2026-07-16, Will-greenlit (BACKLOG build gate, 2nd hit).

Usage:
  python3 ofr_stfm.py gate                       # the 07b funding-gate view (start here)
  python3 ofr_stfm.py rates [--start D] [--csv]  # GCF / DVP / tri-party average rates
  python3 ofr_stfm.py fails [--start D] [--csv]  # Treasury dealer financing fails (NY Fed)
  python3 ofr_stfm.py series MNEMONIC [--csv]    # any OFR series (e.g. REPO-GCF_AR_TOT-F)
  python3 ofr_stfm.py pd KEYID [--csv]           # any NY Fed PD series (e.g. PDFTD-USTET)
  python3 ofr_stfm.py catalog [FILTER]           # list OFR repo series ids

SOURCES (both public, no key, verified live 2026-07-16)
  OFR   https://data.financialresearch.gov/v1/series/dataset?dataset=repo   [PRIMARY]
  NYFed https://markets.newyorkfed.org/api/pd/get/<KEYID>.json              [PRIMARY]

OFR MNEMONIC GRAMMAR:  REPO-<SEGMENT>_<METRIC>_<BUCKET>-<VINTAGE>
  SEGMENT : GCF (interdealer — the squeeze tell) | DVP (bilateral) | TRI / TRIV1 (tri-party)
  METRIC  : AR (average rate, %) | OV (outstanding volume) | TV (transaction volume)
  BUCKET  : TOT (total) | AG (agency) | T (Treasury) | G30/LE30/B27/B830/OO/CORD (tenor/other)
  VINTAGE : F = Final | P = Preliminary   <-- NOT interchangeable; see below

⚠️ TRAPS ENCODED HERE (each cost a debugging cycle; do not re-learn them)
  * VINTAGE: -F (Final) and -P (Preliminary) are different vintages of the same series.
    Recent dates usually exist ONLY as -P. This module reports which vintage answered.
    Never mix them silently in one series.
  * NY Fed `.../get/all/timeseries/<KEYID>.json` returns HTTP 200 with an EMPTY array.
    A silent-empty, not an error. Use `.../get/<KEYID>.json` (full history from 2013).
  * OFR `/v1/metadata/datasets` needs an auth token ("Missing Authentication Token");
    `/v1/series/dataset?dataset=repo` does NOT. Use the latter.
  * OFR returns nulls inside the series (holidays) — dropped, never coerced to 0.
  * The OFR dataset call ships all 164 series (~MBs); it is cached per-process here.

UNITS: OFR rates = Percent. NY Fed fails = $ MILLIONS (43736 == $43.7bn).
"""

import json, sys, time, urllib.request, gzip

OFR_DATASET = "https://data.financialresearch.gov/v1/series/dataset?dataset=repo"
NYFED_PD = "https://markets.newyorkfed.org/api/pd/get/{}.json"
_UA = {"User-Agent": "DEWEY-research/1.0 (research agent; contact via repo)",
       "Accept-Encoding": "gzip"}

# The 07b gate view. GCF first: interdealer is where a dealer-side squeeze shows FIRST.
GATE_RATES = [
    ("REPO-GCF_AR_TOT", "GCF total (interdealer — squeeze tell)"),
    ("REPO-DVP_AR_TOT", "DVP total (bilateral)"),
    ("REPO-TRI_AR_TOT", "Tri-party total"),
]
GATE_FAILS = [
    ("PDFTD-USTET", "UST (ex-TIPS) dealer financing FAILS TO DELIVER"),
    ("PDFTR-USTET", "UST (ex-TIPS) dealer financing FAILS TO RECEIVE"),
]

_cache = {}


def _get(url, retries=3, timeout=90):
    """GET with retry + gzip. OFR/NY-Fed drop connections routinely."""
    last = None
    for i in range(retries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=_UA),
                                        timeout=timeout) as r:
                raw = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    raw = gzip.decompress(raw)
                return json.loads(raw)
        except Exception as e:                       # noqa: BLE001 — retry anything transient
            last = e
            if i < retries - 1:
                time.sleep(1.5 * (i + 1))
    raise RuntimeError(f"GET failed after {retries} tries: {url} ({last})")


def _ofr_all():
    """The whole repo dataset (164 series). Cached — it is multi-MB."""
    if "ofr" not in _cache:
        _cache["ofr"] = _get(OFR_DATASET).get("timeseries", {})
    return _cache["ofr"]


def ofr_series(mnemonic, start=None):
    """One OFR series -> [(date, value)]. Nulls (holidays) dropped, not zero-filled."""
    ts = _ofr_all().get(mnemonic)
    if ts is None:
        raise KeyError(f"OFR series not found: {mnemonic} (try: ofr_stfm.py catalog)")
    rows = ts.get("timeseries", {}).get("aggregation", [])
    out = [(d, v) for d, v in rows if v is not None]
    if start:
        out = [r for r in out if r[0] >= start]
    return out


def ofr_series_auto(base, start=None):
    """Resolve a vintage-less base ('REPO-GCF_AR_TOT') -> (rows, vintage_label).

    SPLICED: authoritative Final history + the Preliminary tail after Final ends.

    Why: Final is authoritative but LAGS ~3.5 months (verified 2026-07-16: -F ended
    2026-03-31 while -P was current to 2026-07-14). Preferring Final alone silently
    serves 3-month-old data as "latest" — a staleness trap. Preferring Preliminary
    alone throws away the revised/authoritative history. So: Final where it exists,
    Preliminary only beyond it, and the label always says which you got.
    """
    final = prelim = []
    try:
        final = ofr_series(base + "-F")
    except KeyError:
        pass
    try:
        prelim = ofr_series(base + "-P")
    except KeyError:
        pass
    if not final and not prelim:
        return [], "NOT FOUND"
    if not final:
        rows, label = prelim, "Preliminary"
    elif not prelim:
        rows, label = final, "Final"
    else:
        cut = final[-1][0]
        tail = [r for r in prelim if r[0] > cut]
        rows = final + tail
        label = (f"Final→{cut}, then Preliminary ({len(tail)} obs)"
                 if tail else "Final")
    if start:
        rows = [r for r in rows if r[0] >= start]
    return rows, label


def nyfed_pd(keyid, start=None):
    """One NY Fed primary-dealer series -> [(date, value)]. Weekly, $ millions."""
    d = _get(NYFED_PD.format(keyid))
    rows = d.get("pd", {}).get("timeseries", [])
    if not rows:
        raise RuntimeError(
            f"NY Fed returned EMPTY for {keyid}. Note: the /get/all/timeseries/ path "
            f"returns 200-with-empty; this module uses /get/<KEYID>.json.")
    out = [(r["asofdate"], float(r["value"]))
           for r in rows if r.get("value") not in (None, "", "*")]
    if start:
        out = [r for r in out if r[0] >= start]
    return out


def _fmt(rows, csv, label=None, unit=""):
    if csv:
        print("date,value")
        for d, v in rows:
            print(f"{d},{v}")
    else:
        if label:
            print(f"\n=== {label} ({len(rows)} obs){unit} ===")
        for d, v in rows[-12:]:
            print(f"  {d}  {v}")


def cmd_gate(args):
    """The 07b funding-gate view: dealer-side plumbing, latest readings + context."""
    print("=" * 74)
    print("FUNDING-GATE DEALER-SIDE VIEW — the leg FRED cannot reach")
    print("  Gate spec (07b): acute SOFR99-IORB >= +30bps AND non-calendar,")
    print("  scoped to FUNDING-ORIGIN seizures only. GCF is the earliest dealer tell.")
    print("=" * 74)

    ok = err = 0

    print("\n-- OFR repo average rates (%) --")
    lat = {}
    for base, desc in GATE_RATES:
        try:
            rows, vint = ofr_series_auto(base)
            if not rows:
                print(f"  {base:<20} NO DATA")
                err += 1
                continue
            d, v = rows[-1]
            prev = rows[-6][1] if len(rows) > 5 else None
            chg = f"{(v - prev) * 100:+.0f}bp/5d" if prev is not None else "n/a"
            lat[base] = v
            ok += 1
            print(f"  {base:<20} {v:>6.2f}%  as-of {d}  [{vint}]  {chg:>12}   {desc}")
        except Exception as e:                        # noqa: BLE001
            err += 1
            print(f"  {base:<20} ERROR: {e}")

    if "REPO-GCF_AR_TOT" in lat and "REPO-TRI_AR_TOT" in lat:
        sp = (lat["REPO-GCF_AR_TOT"] - lat["REPO-TRI_AR_TOT"]) * 100
        print(f"\n  >> GCF - TriParty = {sp:+.0f}bp  "
              f"(dealer-side premium; widens FIRST in a collateral squeeze)")

    print("\n-- NY Fed dealer financing fails ($mn, weekly) --")
    for keyid, desc in GATE_FAILS:
        try:
            rows = nyfed_pd(keyid)
            d, v = rows[-1]
            prev = rows[-2][1] if len(rows) > 1 else None
            chg = f"{(v - prev) / prev * 100:+.0f}% w/w" if prev else "n/a"
            ok += 1
            print(f"  {keyid:<14} ${v:>12,.0f}mn  as-of {d}  {chg:>10}   {desc}")
        except Exception as e:                        # noqa: BLE001
            err += 1
            print(f"  {keyid:<14} ERROR: {e}")

    print("\n  NOTE: fails are WEEKLY (Wed) and lag — diagnostic, not pre-emptive.")
    print("  Pair with FRED SOFR99-IORB (fred_pull.py) for the acute leg.\n")

    # FAIL LOUD: a gate view that reached NOTHING must not exit 0. A caller (or a
    # cron) reads rc=0 as "gate checked, nothing to see" — which is exactly the
    # false all-clear this tool exists to prevent. Routed by DAEDALUS 2026-08-17
    # (SFG sweep §8 rule 3, residual 2); fixed 2026-08-27.
    total = ok + err
    print(f"  [gate] {ok}/{total} series retrieved, {err} error(s).")
    if ok == 0 and total:
        sys.stderr.write(
            "GATE UNAVAILABLE: every series errored — this is a TOOL/NETWORK failure, "
            "NOT a quiet funding market. Do not read it as an all-clear.\n")
        return 1
    if err:
        sys.stderr.write(f"WARNING: {err} of {total} series unavailable — "
                         "the gate view is PARTIAL; say so if you cite it.\n")
    return 0


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        return
    cmd = a[0]
    csv = "--csv" in a
    start = a[a.index("--start") + 1] if "--start" in a else None

    if cmd == "gate":
        return cmd_gate(a)
    elif cmd == "rates":
        for base, desc in GATE_RATES:
            rows, vint = ofr_series_auto(base, start)
            _fmt(rows, csv, f"{base} [{vint}] — {desc}", "  unit: Percent")
    elif cmd == "fails":
        for keyid, desc in GATE_FAILS:
            _fmt(nyfed_pd(keyid, start), csv, f"{keyid} — {desc}", "  unit: $ millions")
    elif cmd == "series" and len(a) > 1:
        base = a[1]
        if base.endswith(("-F", "-P")):
            _fmt(ofr_series(base, start), csv, base, "  unit: see grammar in --help")
        else:
            rows, vint = ofr_series_auto(base, start)
            _fmt(rows, csv, f"{base} [{vint}]")
    elif cmd == "pd" and len(a) > 1:
        _fmt(nyfed_pd(a[1], start), csv, a[1], "  unit: $ millions")
    elif cmd == "catalog":
        filt = a[1].upper() if len(a) > 1 and not a[1].startswith("--") else ""
        ids = sorted(k for k in _ofr_all() if filt in k.upper())
        print(f"=== OFR repo series ({len(ids)} match{'ing ' + filt if filt else ''}) ===")
        for k in ids:
            print(" ", k)
    else:
        print(__doc__)


if __name__ == "__main__":
    sys.exit(main() or 0)
