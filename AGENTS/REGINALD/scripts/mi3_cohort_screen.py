#!/usr/bin/env python3
"""MI3 (hidden-CRE) cohort screen — FFIEC CDR REST/JWT, RetrieveFacsimile/SDF.

Numerator : RCON2746 — "Loans to finance commercial real estate, construction,
            and land development activities (NOT secured by real estate) included
            in Schedule RC-C part I, items 4 AND 9, column B" (schedule RCCI, line M3).
Denominators (both reported — see finding_normalization_choice_picks_opposite_winners):
  V1  (legacy screen basis) : RCON1766                 = RC-C item 4 (C&I loans)
  V1a (uniform full basis)  : RCON1766 + item 9 total  = the numerator's OWN stated parent

⚠️  V1a != V1 fence: MI3 is CRE *not secured by RE*. Secured office books
    (WAL office, OZK RESG) are a separate object and are NOT measured here.

Usage: python3 mi3_cohort_screen.py            (uses cache in /tmp/mi3/fac)
Creds: FORGE/tools/market-data/.env  (FFIEC_CDR_USERNAME, FFIEC_CDR_TOKEN)
Trap:  header is literally "Authentication:", not "Authorization:".
       python-urllib default UA is 403'd by the Azure WAF -> use curl.
"""
import base64
import csv
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True,
                           text=True, check=True).stdout.strip())
ENV = ROOT / "FORGE/tools/market-data/.env"
CACHE = Path("/tmp/mi3/fac")
BASE = "https://ffieccdr.azure-api.us/public"

# Cohort: my watchlist + every name the legacy v1 screen scored + the clean benchmarks.
# RSSDs resolved from RetrievePanelOfReporters 6/30/2026 (bank-level filers, not holdcos).
COHORT = [
    ("OZK",  107244,  "BANK OZK"),
    ("WAL",  3138146, "WESTERN ALLIANCE BANK"),
    ("EGBN", 2652092, "EAGLEBANK"),
    ("ZION", 276579,  "ZIONS BANCORPORATION, N.A."),
    ("SSB",  1929247, "SOUTHSTATE BANK, N.A."),
    ("CFG",  3303298, "CITIZENS BANK, N.A."),
    ("BKU",  3938186, "BANKUNITED, N.A."),
    ("SBCF", 34537,   "SEACOAST NATIONAL BANK"),
    ("AMTB", 83638,   "AMERANT BANK, N.A."),
    ("FLG",  694904,  "FLAGSTAR BANK, N.A."),
    ("MTB",  501105,  "MANUFACTURERS AND TRADERS TRUST"),
    ("HBAN", 12311,   "HUNTINGTON NATIONAL BANK"),
    ("VLY",  229801,  "VALLEY NATIONAL BANK"),
    ("CUBI", 2354985, "CUSTOMERS BANK"),
]

QUARTERS = ["6/30/2025", "12/31/2025", "3/31/2026", "6/30/2026"]

# RC-C part I line items (column B / RCON series, domestic offices)
# ⚠️ INSTRUMENT RESOLUTION (finding_registry_names_a_concept_tool_resolves_an_instrument).
# "Item 4" and "item 9" are CONCEPTS; the MDRM that carries them depends on the FORM:
#   FFIEC 041/051 (domestic-only filers): RCON series, item-4 and item-9b TOTALS printed.
#   FFIEC 031 (filers with foreign offices, e.g. CFG/MTB/HBAN/FLG/VLY/AMTB): RCFD series,
#     and the item-4 / item-9b TOTAL lines are NOT printed — only their 4a/4b, 9b1/9b2 parts.
# So each figure is resolved by fallback chain and the BASIS ACTUALLY USED is recorded per row.
PREFIXES = ("RCON", "RCFD")    # domestic-office preferred, consolidated fallback
NUM_CODES = ["2746"]                       # Memo item 3 (numerator)
I4_TOTAL = ["1766"]                        # item 4 total  C&I
I4_PARTS = ["1763", "1764"]                # item 4.a + 4.b (031 filers)
I9A_CODES = ["J454"]                       # item 9.a NDFI loans
I9B_TOTAL = ["J464"]                       # item 9.b total other loans
I9B_PARTS = ["1545", "J451"]               # item 9.b(1) + 9.b(2) (031 filers)
TOTAL_CODES = ["2122"]                     # item 12 total loans+leases HFI+HFS
ASSET_CODES = ["2170"]                     # total balance-sheet assets (provenance)


def creds():
    env = {}
    with open(ENV) as fh:
        for line in fh:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    u, t = env.get("FFIEC_CDR_USERNAME"), env.get("FFIEC_CDR_TOKEN")
    if not u or not t:
        sys.exit("FFIEC_CDR_USERNAME / FFIEC_CDR_TOKEN missing from " + str(ENV))
    return u, t


def facsimile(user, token, rssd, period):
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / f"{rssd}_{period.replace('/', '-')}.sdf"
    if path.exists() and path.stat().st_size > 1000:
        return path.read_text(errors="replace")
    cmd = [
        "curl", "-s", "--fail-with-body", "-H", f"UserID: {user}",
        "-H", f"Authentication: Bearer {token}",
        "-H", "Content-Type: application/json",
        "-H", "dataSeries: Call",
        "-H", f"reportingPeriodEndDate: {period}",
        "-H", "fiIDType: ID_RSSD", "-H", f"fiID: {rssd}",
        "-H", "facsimileFormat: SDF",
        f"{BASE}/RetrieveFacsimile",
    ]
    r = subprocess.run(cmd, capture_output=True, text=True)
    body = r.stdout
    if r.returncode != 0 or len(body) < 1000 or body.lstrip().startswith("{"):
        return None
    # The REST service returns the SDF as a base64 payload inside a JSON string.
    try:
        text = base64.b64decode(json.loads(body)).decode("utf-8", errors="replace")
    except Exception:
        return None
    if "MDRM" not in text.splitlines()[0]:
        return None
    path.write_text(text)
    return text


def parse(sdf):
    """SDF header: Call Date;Bank RSSD;MDRM #;Value;Last Update;Short Def;Schedule;Line."""
    out = {}
    for line in sdf.splitlines():
        f = line.split(";")
        if len(f) < 4:
            continue
        mdrm, val = f[2].strip(), f[3].strip()
        if not mdrm or not val:
            continue
        try:
            out[mdrm] = int(float(val))
        except ValueError:
            continue
    return out


def pick(d, codes, prefixes=PREFIXES):
    """Return (value, mdrm_used). Sums multi-code chains; None if ANY part absent.
    Never coerces a missing part to 0 — zero != unknown (audit convention 2026-08-12)."""
    for p in prefixes:
        keys = [p + c for c in codes]
        if all(k in d for k in keys):
            return sum(d[k] for k in keys), "+".join(keys)
    return None, ""


def main():
    user, token = creds()
    rows = []
    for tic, rssd, name in COHORT:
        for q in QUARTERS:
            sdf = facsimile(user, token, rssd, q)
            if sdf is None:
                rows.append(dict(ticker=tic, rssd=rssd, name=name, quarter=q,
                                 status="PULL-FAILED"))
                print(f"  !! {tic} {q}: pull failed", file=sys.stderr)
                continue
            d = parse(sdf)
            num, num_src = pick(d, NUM_CODES)
            i4, i4_src = pick(d, I4_TOTAL)
            if i4 is None:
                i4, i4_src = pick(d, I4_PARTS)
            i9a, i9a_src = pick(d, I9A_CODES)
            i9b, i9b_src = pick(d, I9B_TOTAL)
            if i9b is None:
                i9b, i9b_src = pick(d, I9B_PARTS)
            i9 = None if (i9a is None or i9b is None) else i9a + i9b
            total, _ = pick(d, TOTAL_CODES)
            assets, _ = pick(d, ASSET_CODES)
            rec = dict(ticker=tic, rssd=rssd, name=name, quarter=q,
                       mi3_k=num, item4_k=i4, item9a_k=i9a, item9b_k=i9b, item9_k=i9,
                       total_loans_k=total, total_assets_k=assets,
                       num_mdrm=num_src, denom_v1_mdrm=i4_src,
                       denom_v1a_mdrm=("|".join(x for x in (i4_src, i9a_src, i9b_src) if x)
                                       if i9 is not None else ""))
            # zero != unknown != not-applicable (fleet audit convention 2026-08-12)
            if num is None:
                rec["status"] = "NOT-REPORTED"
            elif i4 is None:
                rec["status"] = "DENOM-MISSING"
            else:
                rec["status"] = "OK" if i9 is not None else "OK-V1-ONLY"
                rec["v1_pct"] = round(100.0 * num / i4, 2) if i4 else None
                if i9 is not None and (i4 + i9):
                    rec["v1a_pct"] = round(100.0 * num / (i4 + i9), 2)
            rows.append(rec)
            print(f"  {tic:5s} {q:10s} {rec['status']:13s} MI3={num} i4={i4} i9={i9} "
                  f"v1={rec.get('v1_pct')} v1a={rec.get('v1a_pct')}", file=sys.stderr)

    cols = ["ticker", "rssd", "name", "quarter", "status", "mi3_k", "item4_k",
            "item9a_k", "item9b_k", "item9_k", "v1_pct", "v1a_pct",
            "total_loans_k", "total_assets_k", "num_mdrm", "denom_v1_mdrm",
            "denom_v1a_mdrm"]
    out = ROOT / "AGENTS/REGINALD/workbook/MI3_COHORT.tsv"
    tmp = out.with_suffix(".tmp")
    with open(tmp, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)
    os.replace(tmp, out)
    print(f"wrote {out} ({len(rows)} rows)")


if __name__ == "__main__":
    main()
