#!/usr/bin/env python3
"""
REGINALD Insider Activity Monitor
Queries SEC EDGAR company filings API for recent Form 4 filings.
Flags open market purchases (code P) — thesis challenge signal.

Usage:
  .venv/bin/python3 AGENTS/REGINALD/scripts/insider.py
  .venv/bin/python3 AGENTS/REGINALD/scripts/insider.py --days 30
  .venv/bin/python3 AGENTS/REGINALD/scripts/insider.py --selftest   # fixtures, no network

Exit: 0 = every covered name read, no open-market purchase · 1 = purchase(s) detected ·
      2 = INCOMPLETE — a name failed, did not parse, is UNREAD or UNCOVERED; never an all-clear.

Repair 2026-10-09 (Will's bounded pass): OZK was queried at the SEC (CIK 1569650), where it has
filed nothing since 2017 — "No Form 4 filings" for OZK was clean by construction. OZK now reads
the FDIC disclosure list (the OZK desk's route). FLG, AMTB, CFG and CUBI were not covered.
A response whose issuer name does not match the bank is PARSE, never "no filings".
"""

import urllib.request
import json
import sys
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
import time

# Will 2026-10-09 earnings-read priority banks. A name here with no TARGETS route = UNCOVERED.
PRIORITY = ("CFG", "CUBI", "EGBN", "FLG", "OZK", "AMTB", "WAL")

# CIKs verified against SEC company_tickers.json 2026-10-09; `match` must appear in the feed's
# <conformed-name>. OZK files with the FDIC (cert 110), not the SEC.
TARGETS = {
    "CFG":  {"route": "sec", "cik": "759944",  "name": "Citizens Financial Group", "match": "CITIZENS FINANCIAL"},
    "CUBI": {"route": "sec", "cik": "1488813", "name": "Customers Bancorp", "match": "CUSTOMERS BANCORP"},
    "EGBN": {"route": "sec", "cik": "1050441", "name": "Eagle Bancorp Inc", "match": "EAGLE BANCORP"},
    "FLG":  {"route": "sec", "cik": "910073",  "name": "Flagstar Bank, N.A.", "match": "FLAGSTAR"},
    "OZK":  {"route": "fdic", "cert": 110,     "name": "Bank OZK", "match": "Bank OZK"},
    "AMTB": {"route": "sec", "cik": "1734342", "name": "Amerant Bancorp", "match": "AMERANT"},
    "WAL":  {"route": "sec", "cik": "1212545", "name": "Western Alliance Bancorporation", "match": "WESTERN ALLIANCE"},
}
FDIC_DISCL = "https://securitiesfilings.fdicconnect.fdic.gov/api/instdiscl"
FDIC_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"
FDIC_MIN_ROWS = 440   # cert 110 list held 471 disclosures on 2026-10-09 and only grows

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


def fetch_text(url, attempts=3, headers=None):
    """Fetch URL and return text. Records success/failure so an outage cannot read as an absence.

    Retries transient failures: EDGAR read-timeouts were observed on 2 of 3 runs on
    2026-08-20 and were turning whole names into a false 'no filings'. A retry is
    NOT a way to hide failure - a genuine outage still exhausts attempts and COUNTS.
    """
    global FETCH_OK, FETCH_FAIL
    last = None
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers=headers or HEADERS)
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


def grade_form4_feed(text, info, days, today):
    """Pure verdict on an EDGAR issuer atom feed -> (state, filings, msg). No network."""
    if text is None:
        return "FAILED", [], "request failed"
    if "<feed" not in text or "<company-info>" not in text:
        return "PARSE", [], "response is not an EDGAR company atom feed"
    m = re.search(r"<conformed-name>([^<]+)</conformed-name>", text)
    name = m.group(1).strip() if m else ""
    if info["match"].upper() not in name.upper():
        return "PARSE", [], f"identity mismatch: CIK {info['cik']} is '{name or '?'}', expected '{info['match']}'"
    cutoff = (today - timedelta(days=days)).isoformat()
    results = []
    for entry in re.findall(r"<entry>(.*?)</entry>", text, re.DOTALL):
        date_m = re.search(r"<filing-date>([^<]+)</filing-date>", entry)
        href_m = re.search(r"<filing-href>([^<]+)</filing-href>", entry)
        if not (date_m and href_m):
            return "PARSE", [], "an entry lacks <filing-date> or <filing-href>"
        if date_m.group(1) >= cutoff:
            results.append({"date": date_m.group(1), "index_url": href_m.group(1)})
    return ("FOUND" if results else "CLEAR"), results, f"'{name}'"


def get_form4_filings(info, days=14):
    """Recent Form 4 filings via the EDGAR issuer atom feed -> (state, filings, msg)."""
    url = (
        f"https://www.sec.gov/cgi-bin/browse-edgar?"
        f"action=getcompany&CIK={info['cik']}&type=4&dateb=&owner=include"
        f"&count=40&action=getcompany&output=atom"
    )
    return grade_form4_feed(fetch_text(url), info, days, datetime.now().date())


def grade_fdic_list(rows, days, today, min_rows=FDIC_MIN_ROWS):
    """Pure verdict on the FDIC cert-110 disclosure list -> (state, in_window, msg)."""
    if not isinstance(rows, list):
        return "PARSE", [], f"response is {type(rows).__name__}, not a list"
    if len(rows) < min_rows:
        return "PARSE", [], f"only {len(rows)} disclosures returned (floor {min_rows}) — incomplete"
    bad = [r for r in rows if not isinstance(r, dict) or not isinstance(r.get("disclID"), int)
           or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(r.get("disclPubDate") or ""))]
    if bad:
        return "PARSE", [], f"{len(bad)} row(s) lack an integer disclID or a disclPubDate"
    if any(r.get("cert") != 110 for r in rows):   # identity by cert: pre-2017 rows read 'Bank of the Ozarks'
        return "PARSE", [], "a row is not FDIC cert 110 (Bank OZK) — wrong list"
    cutoff = (today - timedelta(days=days)).isoformat()
    win = sorted((r for r in rows if r["disclPubDate"] >= cutoff), key=lambda r: r["disclPubDate"])
    newest = max(r["disclPubDate"] for r in rows)
    if not win:
        return "CLEAR", [], f"FDIC cert 110: {len(rows)} disclosures, none published since {cutoff} (newest {newest})"
    return "UNREAD", win, (f"FDIC cert 110: {len(win)} Form {'/'.join(sorted({str(r.get('disclTypeCode')) for r in win}))} "
                           f"since {cutoff} — FDIC gives A/D (acquired/disposed) or a PDF, NOT the purchase code; read each")


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
    if "--selftest" in sys.argv:
        sys.exit(selftest())
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

    for ticker in PRIORITY:
        if ticker not in TARGETS:
            print(f"\n  {ticker}\n  {'-'*50}\n  🔴 UNCOVERED — priority bank with no route configured. NO VERDICT.")
            names_unknown.append(ticker)

    for ticker, info in TARGETS.items():
        name = info["name"]
        print(f"\n  {ticker} ({name}) — " + (f"SEC CIK {info['cik']}" if info["route"] == "sec" else f"FDIC cert {info['cert']}"))
        print(f"  {'-'*50}")

        if info["route"] == "fdic":
            body = fetch_text(f"{FDIC_DISCL}/cert/{info['cert']}", headers={"User-Agent": FDIC_UA})
            try:
                rows = json.loads(body) if body is not None else None
            except ValueError:
                rows = "unparseable"
            if body is None:
                state, win, msg = "FAILED", [], "request failed"
            else:
                state, win, msg = grade_fdic_list(rows, days, datetime.now().date())
            print(f"  {'✅' if state == 'CLEAR' else '🔴'} {state}: {msg}")
            for r in win:
                print(f"     {r['disclPubDate']}  Form {r.get('disclTypeCode')}  "
                      f"{r.get('indvFirstName', '')} {r.get('indvLastName', '')}  -> {FDIC_DISCL}/{r['disclID']}")
            if state != "CLEAR":
                names_unknown.append(ticker)
            continue

        # ★ "No filings" and "could not ask" are OPPOSITE epistemic states that used to render
        # IDENTICALLY (caught 2026-08-20 on WAL); a WRONG issuer is a third (caught 2026-10-09).
        state, filings, msg = get_form4_filings(info, days=days)
        if state in ("FAILED", "PARSE"):
            print(f"  🔴 {state} — {msg}. This is NOT 'no filings'. NO VERDICT.")
            names_unknown.append(ticker)
            continue
        if not filings:
            print(f"  ✅ No Form 4 filings in last {days} days ({msg}).")
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
        sys.exit(2)
    if FETCH_FAIL:
        print(f"  ⚠️  PARTIAL SCAN — {FETCH_FAIL} fetch failure(s); the verdict below covers only what was fetched.")
        for e in LAST_ERRORS:
            print(f"     {e}")

    if names_unknown:
        print(f"  🔴 NO VERDICT for: {', '.join(names_unknown)} (failed / unparsed / UNREAD / UNCOVERED).")
    covered = [t for t in TARGETS if t not in names_unknown]
    if any_purchases:
        print(f"\n  🔴 ALERT: Insider buying detected — review before maintaining short thesis.")
    elif names_unknown or FETCH_FAIL:
        print(f"\n  ⚠️  INCOMPLETE — no open-market purchase among the names read "
              f"({', '.join(covered) if covered else 'NONE'}); this is NOT an all-clear.")
    else:
        print(f"\n  ✅ No open market insider purchases across all {len(TARGETS)} names "
              f"({', '.join(covered)}).")

    print()
    if any_purchases:
        sys.exit(1)
    if FETCH_FAIL or names_unknown:
        sys.exit(2)


def selftest():
    from datetime import date
    today = date(2026, 10, 9)
    wal = TARGETS["WAL"]

    def feed(name, dates):
        e = "".join(f"<entry><filing-date>{d}</filing-date><filing-href>u</filing-href></entry>" for d in dates)
        return f"<feed><company-info><conformed-name>{name}</conformed-name></company-info>{e}</feed>"

    row = lambda i, d: {"disclID": i, "disclPubDate": d, "disclTypeCode": "4", "instName": "Bank OZK", "cert": 110}
    base = [row(i, "2026-08-14") for i in range(3)]
    cases = [
        ("sec: valid feed, none in window -> CLEAR", grade_form4_feed(feed("WESTERN ALLIANCE BANCORPORATION", ["2026-08-01"]), wal, 14, today)[0], "CLEAR"),
        ("sec: request failed -> FAILED", grade_form4_feed(None, wal, 14, today)[0], "FAILED"),
        ("sec: HTML error page -> PARSE", grade_form4_feed("<html>503</html>", wal, 14, today)[0], "PARSE"),
        ("sec: wrong issuer at CIK -> PARSE", grade_form4_feed(feed("OLD REPUBLIC INTERNATIONAL CORP", []), wal, 14, today)[0], "PARSE"),
        ("sec: filing in window -> FOUND", grade_form4_feed(feed("WESTERN ALLIANCE BANCORPORATION", ["2026-10-05"]), wal, 14, today)[0], "FOUND"),
        ("fdic: error body -> PARSE", grade_fdic_list({"Message": "error"}, 14, today, min_rows=3)[0], "PARSE"),
        ("fdic: truncated list -> PARSE", grade_fdic_list(base[:1], 14, today, min_rows=3)[0], "PARSE"),
        ("fdic: valid, none in window -> CLEAR", grade_fdic_list(base, 14, today, min_rows=3)[0], "CLEAR"),
        ("fdic: Form 4 in window -> UNREAD (no purchase code at FDIC)", grade_fdic_list(base + [row(9, "2026-10-01")], 14, today, min_rows=3)[0], "UNREAD"),
        ("fdic: other issuer's row -> PARSE", grade_fdic_list(base + [dict(row(9, "2026-08-01"), cert=999)], 14, today, min_rows=3)[0], "PARSE"),
        ("fdic: pre-2017 name, same cert -> CLEAR", grade_fdic_list(base + [dict(row(9, "2016-01-04"), instName="Bank of the Ozarks")], 14, today, min_rows=3)[0], "CLEAR"),
    ]
    fails = 0
    for name, got, want in cases:
        ok = got == want
        fails += not ok
        print(f"  {'PASS' if ok else 'FAIL'}  {got:<7} (want {want})  {name}")
    print(f"INSIDER SELFTEST {'PASS' if not fails else 'FAIL'}: {len(cases) - fails}/{len(cases)}")
    return 1 if fails else 0


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:  # a crash must not exit 0 or collide with rc 1 ALERT
        print(f"INSIDER 2 INCOMPLETE: internal error ({type(e).__name__}: {e}) — no verdict")
        sys.exit(2)
