#!/usr/bin/env python3
"""
REGINALD Insider Activity Monitor
Queries SEC EDGAR company filings API for recent Form 4 filings.
Flags open market purchases (code P) — thesis challenge signal.

Usage:
  .venv/bin/python3 AGENTS/REGINALD/scripts/insider.py
  .venv/bin/python3 AGENTS/REGINALD/scripts/insider.py --days 30
"""

import urllib.request
import json
import sys
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
import time

# Issuer CIKs for thesis banks (used in the company filings endpoint)
TARGETS = {
    "WAL": {"cik": "1212545", "name": "Western Alliance Bancorporation"},
    "OZK": {"cik": "1569650", "name": "Bank OZK"},
    "EGBN": {"cik": "1050441", "name": "Eagle Bancorp Inc"},
}

# Transaction codes
BULLISH_CODES = {"P"}  # Open market purchase — thesis challenge
BEARISH_CODES = {"S"}  # Open market sale — confirms thesis
NOISE_CODES = {"F", "M", "A", "D", "G", "J", "K", "U", "W", "Z"}

HEADERS = {
    "User-Agent": "REGINALD-Research williepowen@gmail.com",
    "Accept": "application/json",
}


# ⚠️ FETCH TELEMETRY (added 2026-08-20, DAEDALUS silent-fallback-green sweep 8/17).
# The bare `except: return None` below used to render a TOTAL EDGAR OUTAGE as
# "✅ No open market insider purchases" at rc=0 — on the one detector whose NULL
# state is load-bearing evidence FOR staying short. A thesis-challenge instrument
# that cannot fail visibly is worse than no instrument.
# [[finding_verification_zero_is_ambiguous]] · [[finding_fail_loud_on_incomplete_data]]
FETCH_OK = 0
FETCH_FAIL = 0
LAST_ERRORS = []


def fetch_text(url, attempts=3):
    """Fetch URL and return text. Records success/failure so an outage cannot read as an absence.

    Retries transient failures: EDGAR read-timeouts were observed on 2 of 3 runs on
    2026-08-20 and were turning whole names into a false 'no filings'. A retry is
    NOT a way to hide failure - a genuine outage still exhausts attempts and COUNTS.
    """
    global FETCH_OK, FETCH_FAIL
    last = None
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            resp = urllib.request.urlopen(req, timeout=25)
            body = resp.read().decode("utf-8")
            FETCH_OK += 1
            return body
        except Exception as e:                  # noqa: BLE001 - deliberate, and COUNTED
            last = e
            if i < attempts - 1:
                time.sleep(1.5 * (i + 1))       # back off; EDGAR rate-limits
    FETCH_FAIL += 1
    if len(LAST_ERRORS) < 5:
        LAST_ERRORS.append(f"{type(last).__name__}: {last} <- {url[:90]} (after {attempts} attempts)")
    return None


def get_form4_filings(cik, days=14):
    """Get recent Form 4 filings via EDGAR company filings Atom feed."""
    url = (
        f"https://www.sec.gov/cgi-bin/browse-edgar?"
        f"action=getcompany&CIK={cik}&type=4&dateb=&owner=include"
        f"&count=40&action=getcompany&output=atom"
    )
    text = fetch_text(url)
    if not text:
        return []

    cutoff = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    results = []

    entries = re.findall(r"<entry>(.*?)</entry>", text, re.DOTALL)
    for entry in entries:
        date_m = re.search(r"<filing-date>([^<]+)</filing-date>", entry)
        href_m = re.search(r"<filing-href>([^<]+)</filing-href>", entry)
        if date_m and href_m:
            fdate = date_m.group(1)
            if fdate >= cutoff:
                results.append({
                    "date": fdate,
                    "index_url": href_m.group(1),
                })

    return results


def find_xml_in_index(index_url):
    """Fetch the filing index page and find the XML document URL."""
    text = fetch_text(index_url)
    if not text:
        return None

    # Look for the XML file link in the index page
    # Pattern: /Archives/edgar/data/CIK/ACCESSION/filename.xml
    matches = re.findall(r'href="(/Archives/edgar/data/[^"]+\.xml)"', text)

    # ⚠️ BUG FIXED 2026-08-20. The old condition was
    #     if "form4" in m.lower() or "wk-" in m.lower() or "xslF345" not in m:
    # whose FIRST clause matches the XSL-RENDERED path
    # (/xslF345X06/wk-form4_*.xml), which serves **HTML**, not XML. ET.fromstring
    # then raised, parse returned None, and the caller counted that as "Routine" —
    # so EVERY Form 4 rendered as "All routine (RSU settlements...)", a specific
    # factual claim about documents nobody had read. 11 of 11 filings were
    # unparsed on 2026-08-20 with ZERO fetch failures.
    # The raw XML is the sibling WITHOUT the /xsl.../ path segment. Order matters:
    # reject xsl FIRST, then prefer a form4-looking name.
    raw = [m for m in matches if "/xsl" not in m.lower()]
    for m in raw:
        if "form4" in m.lower() or "wk-" in m.lower():
            return f"https://www.sec.gov{m}"
    if raw:
        return f"https://www.sec.gov{raw[0]}"
    return None      # NEVER fall back to an xsl/HTML link - it cannot parse as XML


def parse_form4_xml(xml_url):
    """Parse a Form 4 XML for reporter name and transactions."""
    text = fetch_text(xml_url)
    if not text:
        return None

    transactions = []
    try:
        root = ET.fromstring(text)

        # Find reporter name
        reporter = ""
        for elem in root.iter():
            tag = elem.tag.split("}")[-1] if "}" in elem.tag else elem.tag
            if tag == "rptOwnerName":
                reporter = (elem.text or "").strip()
                break

        # Parse non-derivative and derivative transactions
        for elem in root.iter():
            tag = elem.tag.split("}")[-1] if "}" in elem.tag else elem.tag
            if tag in ("nonDerivativeTransaction", "derivativeTransaction"):
                code = ""
                shares = ""
                price = ""
                for child in elem.iter():
                    ctag = child.tag.split("}")[-1] if "}" in child.tag else child.tag
                    if ctag == "transactionCode":
                        code = (child.text or "").strip()
                    if ctag == "transactionShares":
                        for v in child.iter():
                            vtag = v.tag.split("}")[-1] if "}" in v.tag else v.tag
                            if vtag == "value":
                                shares = (v.text or "").strip()
                                break
                    if ctag == "transactionPricePerShare":
                        for v in child.iter():
                            vtag = v.tag.split("}")[-1] if "}" in v.tag else v.tag
                            if vtag == "value":
                                price = (v.text or "").strip()
                                break
                if code:
                    transactions.append({
                        "reporter": reporter,
                        "code": code,
                        "shares": shares,
                        "price": price,
                    })
    except ET.ParseError:
        return None

    return transactions


def main():
    days = 14
    if "--days" in sys.argv:
        idx = sys.argv.index("--days")
        if idx + 1 < len(sys.argv):
            days = int(sys.argv[idx + 1])

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"\n{'='*70}")
    print(f"  REGINALD Insider Monitor — {now} (last {days} days)")
    print(f"{'='*70}")

    any_purchases = False
    names_unknown = []          # names with NO usable read - never fold into a clean verdict

    for ticker, info in TARGETS.items():
        cik = info["cik"]
        name = info["name"]
        print(f"\n  {ticker} ({name})")
        print(f"  {'-'*50}")

        _fail_before = FETCH_FAIL
        filings = get_form4_filings(cik, days=days)
        if not filings:
            if FETCH_FAIL > _fail_before:
                # ★ THIS IS THE LOAD-BEARING CASE. "No filings" and "could not ask" are
                # OPPOSITE epistemic states that used to render IDENTICALLY. Caught live
                # 2026-08-20 on WAL (CIK 1212545) — the very first run after the fix.
                print(f"  🔴 UNKNOWN — EDGAR fetch FAILED for this name. This is NOT 'no filings'.")
                names_unknown.append(ticker)
            else:
                print(f"  No Form 4 filings in last {days} days.")
            continue

        total_purchases = 0
        total_sales = 0
        total_noise = 0
        total_unparsed = 0          # parse/fetch failures — NOT routine activity
        purchase_details = []
        sale_details = []
        reporters_seen = set()

        for filing in filings[:25]:  # cap to avoid rate limits
            xml_url = find_xml_in_index(filing["index_url"])
            time.sleep(0.12)  # EDGAR rate limit

            if not xml_url:
                total_unparsed += 1     # was counted as "Routine" — inflated noise, deflated buys
                continue

            txns = parse_form4_xml(xml_url)
            time.sleep(0.12)

            if not txns:
                total_unparsed += 1     # was counted as "Routine"
                continue

            for txn in txns:
                code = txn["code"].upper()
                reporters_seen.add(txn["reporter"])
                if code in BULLISH_CODES:
                    total_purchases += 1
                    purchase_details.append({
                        "date": filing["date"],
                        "reporter": txn["reporter"],
                        "shares": txn["shares"],
                        "price": txn["price"],
                    })
                elif code in BEARISH_CODES:
                    total_sales += 1
                    sale_details.append({
                        "date": filing["date"],
                        "reporter": txn["reporter"],
                        "shares": txn["shares"],
                        "price": txn["price"],
                    })
                else:
                    total_noise += 1

        # Summary
        reporters_str = ", ".join(sorted(reporters_seen)[:5])
        if len(reporters_seen) > 5:
            reporters_str += f" +{len(reporters_seen)-5} more"
        print(f"  Filings: {len(filings)} | Buys: {total_purchases} | Sales: {total_sales} | "
              f"Routine: {total_noise} | Unparsed: {total_unparsed}")
        if reporters_seen:
            print(f"  Reporters: {reporters_str}")

        if total_purchases > 0:
            any_purchases = True
            print(f"  🔴🔴 OPEN MARKET PURCHASES DETECTED — THESIS CHALLENGE")
            for p in purchase_details:
                shares_str = f"{float(p['shares']):,.0f}" if p["shares"] else "?"
                price_str = f"${float(p['price']):.2f}" if p["price"] else "?"
                print(f"     {p['date']}  {p['reporter']}  {shares_str} shares @ {price_str}")

        if total_sales > 0:
            print(f"  📉 Open market sales:")
            for s in sale_details[:5]:
                shares_str = f"{float(s['shares']):,.0f}" if s["shares"] else "?"
                price_str = f"${float(s['price']):.2f}" if s["price"] else "?"
                print(f"     {s['date']}  {s['reporter']}  {shares_str} shares @ {price_str}")

        if total_purchases == 0 and total_sales == 0 and filings:
            if total_noise == 0 and total_unparsed:
                # Every filing failed to parse: "all routine" would be a claim about
                # documents nobody read. Caught live 2026-08-20 on EGBN (2 of 2 unparsed).
                print(f"  🔴 UNKNOWN — all {total_unparsed} filing(s) UNPARSED. No routine/conviction "
                      f"verdict is available for this name.")
                names_unknown.append(ticker)
            else:
                print(f"  All routine (RSU settlements, tax withholdings, awards). No conviction signals.")

    # ⚠️ COVERAGE FIRST — a verdict is only as good as the scope it certifies.
    print(f"\n  fetched {FETCH_OK} ok / {FETCH_FAIL} failed")
    if FETCH_OK == 0:
        print("  🔴 SCAN FAILED — ZERO successful EDGAR fetches. This is NOT 'no insider buying';")
        print("     it is NO DATA. Do not read the absence of an alert as evidence.")
        for e in LAST_ERRORS:
            print(f"     {e}")
        print()
        sys.exit(1)
    if FETCH_FAIL:
        print(f"  ⚠️  PARTIAL SCAN — {FETCH_FAIL} fetch failure(s); the verdict below covers only what was fetched.")
        for e in LAST_ERRORS:
            print(f"     {e}")

    if names_unknown:
        print(f"  🔴 NO USABLE READ for: {', '.join(names_unknown)} — excluded from the verdict below.")
    if not any_purchases:
        covered = [t for t in TARGETS if t not in names_unknown]
        print(f"\n  ✅ No open market insider purchases across {len(covered)} of {len(TARGETS)} names "
              f"({', '.join(covered) if covered else 'NONE'}).")
    else:
        print(f"\n  🔴 ALERT: Insider buying detected — review before maintaining short thesis.")

    print()
    if FETCH_FAIL or names_unknown:
        sys.exit(1)


if __name__ == "__main__":
    main()
