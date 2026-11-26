#!/usr/bin/env python3
"""
Brevard County Clerk (AcclaimWeb) monthly COUNTS: lis pendens by plaintiff type,
and mortgages recorded to HUD (FHA partial claims) by amount band.

Built 2026-11-26 for REQ-DEWEY-20261123-001 (report
output/2026-11-26_florida-county-distress-counts-pilot.md); kept in scripts/ on
Will's word 2026-11-26 15:39 ET so the monthly re-pull (DOCKET L1296) counts
exactly as the baseline did. Stdlib only. No schedule: run by hand.

GUARDRAILS (from the request; do not loosen):
  - COUNTS ONLY. No party name, parcel, address, book/page or instrument number
    is written anywhere; rows are counted in memory and discarded.
  - Client name research-bot/1.0 (WQ-735). A challenge page, CAPTCHA text or a
    non-200 STOPS the run with a message; never retry under another name.
  - The site's disclaimer is an accuracy and statutory-rights notice (read
    2026-11-26); it does not bar automated use. Re-read it if it changes.
  - One-second spacing between requests.

Usage:
  python3 brevard_counts.py lp  2026-12            # one month -> TSV on stdout
  python3 brevard_counts.py lp  2024-11 2026-12    # a range
  python3 brevard_counts.py hud 2026-12

Definitions (changing any of these breaks comparability with the baseline):
  lp   document types 99,100 = LIS PENDENS (LP), (LP1); plaintiff = DirectName,
       classed by the ASSOC, GOV, LENDER keyword rules below, in that order;
       everything else is "other" (individuals, unrecognised LLCs, trusts).
  hud  document types 106,158,159,161,170,118 (MORTGAGE, the three tax-exempt
       mortgage types, DEED/MORTGAGE COMBO, MODIFIED MORTGAGE); HUD = grantee
       (IndirectName) matching the HUD rule; banded by recorded Consideration
       at $150,000 (partial-claim-sized vs reverse-mortgage-sized).
  A month is a calendar month of RECORD date. The latest month is partial
  until the clerk finishes indexing (about a week).
"""
import sys, re, json, time, calendar, http.cookiejar, urllib.request, urllib.parse, collections

B = "https://vaclmweb1.brevardclerk.us/AcclaimWeb"
UA = "research-bot/1.0"
LP = "99,100"                        # LIS PENDENS (LP), (LP1)
MTG = "106,158,159,161,170,118"      # M, MTGEX, MTGDOCEX, MTGINTEX, DMTG, MM
HUD = re.compile(r"HOUSING\s*(AND|&)?\s*URBAN|SECRETARY\s*OF\s*HOUSING|^HUD\b|\bH\s*U\s*D\b")
ASSOC = re.compile(r"ASSOC|HOMEOWNER|CONDOMINIUM|\bHOA\b|PROPERTY OWNERS|COMMUNITY|\bCLUB\b|VILLAGE|ESTATES OF|MASTER")
GOV = re.compile(r"COUNTY|CITY OF|STATE OF|UNITED STATES|SECRETARY|TOWN OF|DISTRICT")
LENDER = re.compile(r"BANK|MORTGAGE|LOAN|LENDING|CREDIT UNION|FEDERAL|FINANCIAL|FINANCE|SERVIC|TRUST|SAVINGS|FUNDING|CAPITAL|NATIONSTAR|MR COOPER|ROCKET|PENNYMAC|FREEDOM|LAKEVIEW|CARRINGTON|NEWREZ|SHELLPOINT|MIDFIRST|FANNIE|FREDDIE|GINNIE|U S BANK|WELLS|CHASE|TRUIST|REGIONS|CITI|HSBC|DEUTSCHE|WILMINGTON|BANKERS|ROUNDPOINT|SELECT PORTFOLIO|SPECIALIZED|VILLAGE CAPITAL|PLANET HOME|GUILD|CROSSCOUNTRY|LOANCARE|DITECH|OCWEN|ONEMAIN")

cj = http.cookiejar.CookieJar()
op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
op.addheaders = [("User-Agent", UA)]


def req(path, data=None, ajax=False):
    h = {"X-Requested-With": "XMLHttpRequest"} if ajax else {}
    body = urllib.parse.urlencode(data).encode() if data is not None else None
    for i in range(3):
        try:
            r = op.open(urllib.request.Request(B + path, data=body, headers=h), timeout=90)
            t = r.read().decode("utf-8", "ignore")
            if r.status != 200 or "cf-mitigated" in t or "Just a moment" in t or "captcha" in t.lower():
                sys.exit(f"STOP: {path} status {r.status} or challenge text")
            return t
        except urllib.error.HTTPError as e:
            sys.exit(f"STOP: {path} HTTP {e.code}")
        except Exception as e:
            if i == 2:
                sys.exit(f"STOP: {path} {e!r} after 3 tries")
            time.sleep(5 * (i + 1))


def start():
    req("/search/Disclaimer?st=/AcclaimWeb/search/SearchTypeDocType", {"disclaimer": "true"})
    req("/search/SearchTypeDocType")


def month_rows(codes, y, m, d0=1, d1=None):
    d1 = d1 or calendar.monthrange(y, m)[1]
    req("/search/SearchTypeDocType?Length=6", {"DocTypes": codes, "DocTypesDisplay": "", "DateRangeList": "",
        "RecordDateFrom": f"{m}/{d0}/{y}", "RecordDateTo": f"{m}/{d1}/{y}"}, ajax=True)
    rows, page, total = [], 1, None
    while True:
        d = json.loads(req("/Search/GridResults", {"page": page, "size": 500}, ajax=True))
        total = d["total"]; rows += d["data"]
        if len(rows) >= total or not d["data"]:
            break
        page += 1; time.sleep(1)
    ids = {r["TransactionItemId"] for r in rows}
    return rows, total, len(ids)


def classify(name):
    n = (name or "").upper()
    if ASSOC.search(n): return "association"
    if GOV.search(n): return "government"
    if LENDER.search(n): return "lender"
    return "other"


def months(a, b):
    y, m = map(int, a.split("-")); y2, m2 = map(int, b.split("-"))
    while (y, m) <= (y2, m2):
        yield y, m
        m += 1
        if m == 13: y, m = y + 1, 1


if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] not in ("lp", "hud"):
        sys.exit("usage: brevard_counts.py lp|hud YYYY-MM [YYYY-MM]")
    mode, a = sys.argv[1], sys.argv[2]
    b = sys.argv[3] if len(sys.argv) > 3 else a
    start()
    if mode == "lp":
        print("month\ttotal\tunique_docs\tlender\tassociation\tgovernment\tother")
        for y, m in months(a, b):
            rows, total, uniq = month_rows(LP, y, m)
            c = collections.Counter(classify(r.get("DirectName")) for r in rows)
            print(f"{y}-{m:02d}\t{total}\t{uniq}\t{c['lender']}\t{c['association']}\t{c['government']}\t{c['other']}", flush=True)
            time.sleep(1)
    elif mode == "hud":
        print("month\tmortgage_docs\thud_docs\thud_le_150k\thud_gt_150k\thud_zero\thud_median_le_150k\thud_by_doctype")
        for y, m in months(a, b):
            rows, total, uniq = month_rows(MTG, y, m)
            hud = [r for r in rows if HUD.search((r.get("IndirectName") or "").upper())]
            hd = {r["TransactionItemId"]: r["DocTypeDescription"] for r in hud}
            amt = {r["TransactionItemId"]: float(str(r.get("Consideration") or 0).replace(",", "").replace("$", "") or 0) for r in hud}
            le = sorted(v for v in amt.values() if 0 < v <= 150000)
            gt = sum(1 for v in amt.values() if v > 150000); z = sum(1 for v in amt.values() if v == 0)
            med = le[len(le) // 2] if le else 0
            print(f"{y}-{m:02d}\t{uniq}\t{len(hd)}\t{len(le)}\t{gt}\t{z}\t{med:.0f}\t{dict(collections.Counter(hd.values()))}", flush=True)
            time.sleep(1)
