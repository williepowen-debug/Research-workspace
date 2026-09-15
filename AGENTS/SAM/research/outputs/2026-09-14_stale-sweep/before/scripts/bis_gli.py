#!/usr/bin/env python3
"""BIS Global Liquidity Indicators — YEN CREDIT TO NON-RESIDENTS.

WHY THIS EXISTS
---------------
On 2026-08-20 SAM opened a v2.0 candidate whose central argument was a SCALE
claim: the all-time-record CFTC speculative yen short (¥2.35T ≈ $14.8B) was too
small to set the yen's level. §5 of that candidate named its own killer in
writing, BEFORE any data existed:

    "At $14.8B the arithmetic holds; at $300-500B it INVERTS and §3 collapses."

This series is what settles it. Measured the same day at 2026-Q1:
**¥65.83T = $414.9B** of JPY-denominated credit to non-bank borrowers OUTSIDE
Japan -- 28x the futures proxy, which captures ~3.5% of it. K1 FIRED and §2 died.

A hand-pull is not an instrument. This script exists so the number is
REPRODUCIBLE and TRACKED, per SAM's own rule that a load-bearing figure must be
reproducible ([[finding_loadbearing_number_must_be_reproducible]]).

⚠️ WHAT THIS SERIES IS NOT -- the caveats are load-bearing and must travel:
  * NOT "the yen carry trade." It is yen-denominated BORROWING by non-banks
    abroad, which includes trade finance, funding by firms with yen revenue, and
    euroyen/samurai issuance with no carry motive  =>  an UPPER BOUND on this
    channel.
  * It EXCLUDES FX SWAPS ENTIRELY -- the dominant carry vehicle -- so it is also
    INCOMPLETE in the other direction.
  * It is a STOCK, not a position that must be unwound.
  => Decisive on ORDER OF MAGNITUDE, which is all §5 asked of it.
     NEVER cite it as a measurement of carry positioning.

Source: BIS SDMX RESTful API, stats.bis.org/api/v1 (no auth). QUARTERLY, ~1
quarter lag. (SAM's 2026-08-20 morning framing of "semi-annual and heavily
lagged" was wrong on BOTH counts.)

Two-clock by design: the BIS observation period is stored separately from
pulled_at, so a stale source cannot masquerade as fresh data.
Idempotent by (period, series_id).
"""
import csv
import io
import os
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TSV = ROOT / "AGENTS" / "SAM" / "workbook" / "BIS_GLI.tsv"
API = "https://stats.bis.org/api/v1/data/WS_GLI/all/all?lastNObservations=1&format=csv"
UA = "Mozilla/5.0 (SAM research agent; williepowen@gmail.com)"

COLUMNS = ["period", "series_id", "label", "value_jpy_tn", "value_usd_bn",
           "borrowers_cty", "instrument", "source", "basis", "pulled_at"]

# The series that answer the scale question. Matched on TITLE substrings because
# BIS dimension codes for the "outside Japan" aggregate are not self-documenting.
WANTED = [
    ("JPY_CREDIT_NONBANK_EXJP", "credit (bank loans & debt securities) to non-bank borrowers located outs",
     "loans+debt_secs"),
    ("JPY_LOANS_NONBANK_EXJP", "bank loans to non-bank borrowers located outside japan", "bank_loans"),
    ("JPY_DEBTSEC_NONBANK_EXJP", "international debt securities issued by non-bank borrowers located outsi",
     "intl_debt_secs"),
]
# Unit sanity anchor: JPY credit to the Japanese GOVERNMENT should read ~¥1,280T.
# If it does not, the UNIT_MULT interpretation is wrong and every figure below is
# wrong by 10^n. This check is why the 2026-08-20 number could be trusted.
ANCHOR_TITLE = "credit to borrowers in japan (government)"
ANCHOR_MIN_TN, ANCHOR_MAX_TN = 900, 1800


def fetch():
    req = urllib.request.Request(API, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as r:
        if r.status != 200:
            sys.exit(f"  🔴 BIS API returned {r.status} — NOT writing")
        return r.read().decode("utf-8", errors="replace")


def main():
    fx = float(os.environ.get("SAM_USDJPY", "158.65"))
    rows = list(csv.DictReader(io.StringIO(fetch())))
    jpy = [r for r in rows if r.get("CURR_DENOM") == "JPY" and r.get("UNIT_MEASURE") == "JPY"]
    if not jpy:
        sys.exit("  🔴 no JPY/JPY-unit rows returned — schema change? NOT writing")

    def find(sub):
        for r in jpy:
            if sub in (r.get("TITLE") or "").lower():
                return r
        return None

    # --- unit anchor, fail LOUD rather than write a figure wrong by 10^n ---
    a = find(ANCHOR_TITLE)
    if not a:
        sys.exit("  🔴 unit-anchor series (JPY credit to Japan government) missing — NOT writing")
    a_tn = float(a["OBS_VALUE"]) * 10 ** int(a["UNIT_MULT"]) / 1e12
    if not (ANCHOR_MIN_TN <= a_tn <= ANCHOR_MAX_TN):
        sys.exit(f"  🔴 UNIT ANCHOR FAILED: JPY credit to Japan govt = ¥{a_tn:,.0f}T, "
                 f"expected ¥{ANCHOR_MIN_TN}-{ANCHOR_MAX_TN}T. UNIT_MULT misread — NOT writing.")
    print(f"  ✓ unit anchor OK: JPY credit to Japan govt = ¥{a_tn:,.0f}T (~¥1,280T expected)")

    existing = set()
    if TSV.exists():
        with TSV.open(encoding="utf-8") as fh:
            for r in csv.DictReader(fh, delimiter="\t"):
                existing.add((r["period"], r["series_id"]))

    pulled = datetime.now().strftime("%Y-%m-%dT%H:%M")
    new, shown = [], {}
    for sid, sub, instr in WANTED:
        r = find(sub)
        if not r:
            print(f"  ⚠️  series not found: {sid} — skipped (NOT written as zero)")
            continue
        tn = float(r["OBS_VALUE"]) * 10 ** int(r["UNIT_MULT"]) / 1e12
        bn = tn * 1e12 / fx / 1e9
        shown[sid] = (r["TIME_PERIOD"], tn, bn)
        key = (r["TIME_PERIOD"], sid)
        if key in existing:
            continue
        new.append([r["TIME_PERIOD"], sid, (r.get("TITLE") or "")[:120],
                    f"{tn:.2f}", f"{bn:.1f}", r.get("BORROWERS_CTY", ""), instr,
                    "BIS WS_GLI (stats.bis.org/api/v1)", "stock, quarterly", pulled])

    print(f"\n  BIS Global Liquidity Indicators — JPY credit to non-residents")
    for sid, (per, tn, bn) in shown.items():
        print(f"    {per}  {sid:<26} ¥{tn:7.2f}T  = ${bn:7.1f}B")
    if "JPY_CREDIT_NONBANK_EXJP" in shown:
        per, tn, bn = shown["JPY_CREDIT_NONBANK_EXJP"]
        peak_bn = 188_077 * 12_500_000 / fx / 1e9
        print(f"\n    vs CFTC peak futures short  ${peak_bn:,.1f}B  ⇒  ratio {tn*1e12/(188_077*12_500_000):,.0f}x")
        print(f"    ⚠️  NOT the carry trade: upper bound on this channel, EXCLUDES FX swaps, "
              f"is a STOCK. Order-of-magnitude only.")

    if not TSV.exists():
        TSV.write_text("\t".join(COLUMNS) + "\n", encoding="utf-8")
    if new:
        with TSV.open("a", encoding="utf-8", newline="") as fh:
            csv.writer(fh, delimiter="\t", lineterminator="\n").writerows(new)
        print(f"\n  ✓ appended {len(new)} row(s) to BIS_GLI.tsv")
    else:
        print(f"\n  ✓ BIS_GLI.tsv already current for {list(shown.values())[0][0] if shown else 'n/a'}")


if __name__ == "__main__":
    main()
