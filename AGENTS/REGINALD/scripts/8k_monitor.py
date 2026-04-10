#!/usr/bin/env python3
"""
REGINALD 8-K Filing Monitor
Queries SEC EDGAR for new 8-K filings from thesis banks.
Catches: credit events, management changes, capital raises, dividend changes.

Usage:
  .venv/bin/python3 AGENTS/REGINALD/scripts/8k_monitor.py
  .venv/bin/python3 AGENTS/REGINALD/scripts/8k_monitor.py --days 30
"""

import urllib.request
import json
import re
import sys
from datetime import datetime, timedelta

# Issuer CIKs (same as insider.py)
TARGETS = {
    "WAL": {"cik": "1212545", "name": "Western Alliance Bancorporation"},
    "OZK": {"cik": "1569650", "name": "Bank OZK"},
    "EGBN": {"cik": "1050441", "name": "Eagle Bancorp Inc"},
    "ZION": {"cik": "109380", "name": "Zions Bancorporation"},
    "VLY": {"cik": "74260", "name": "Valley National Bancorp"},
}

# 8-K item numbers and their significance
ITEM_FLAGS = {
    "1.01": ("🔴", "Entry into Material Agreement"),
    "1.02": ("🔴", "Termination of Material Agreement"),
    "1.03": ("🟠", "Bankruptcy/Receivership"),
    "2.01": ("🟠", "Completion of Acquisition/Disposition"),
    "2.02": ("🔴", "Results of Operations (EARNINGS)"),
    "2.03": ("🟠", "Creation of Direct Financial Obligation"),
    "2.04": ("🔴", "Triggering Events / Default"),
    "2.05": ("🔴", "Costs of Exit/Restructuring"),
    "2.06": ("🔴", "Material Impairments"),
    "3.01": ("🟠", "Delisting/Transfer"),
    "3.03": ("🟠", "Material Modification of Rights"),
    "4.01": ("🟠", "Changes in Auditor"),
    "4.02": ("🔴", "Non-Reliance on Financial Statements"),
    "5.01": ("🟠", "Changes in Control"),
    "5.02": ("🔴", "Departure/Appointment of Officers"),
    "5.03": ("🟠", "Amendments to Articles/Bylaws"),
    "5.07": ("⚪", "Shareholder Vote"),
    "7.01": ("⚪", "Regulation FD Disclosure"),
    "8.01": ("⚪", "Other Events"),
    "9.01": ("⚪", "Financial Statements/Exhibits"),
}

HEADERS = {
    "User-Agent": "REGINALD-Research research@example.com",
}


def fetch_text(url):
    """Fetch URL and return text."""
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        resp = urllib.request.urlopen(req, timeout=15)
        return resp.read().decode("utf-8")
    except Exception:
        return None


def get_8k_filings(cik, days=7):
    """Get recent 8-K filings from EDGAR company filings Atom feed."""
    url = (
        f"https://www.sec.gov/cgi-bin/browse-edgar?"
        f"action=getcompany&CIK={cik}&type=8-K&dateb=&owner=exclude"
        f"&count=20&action=getcompany&output=atom"
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
        form_m = re.search(r"<filing-type>([^<]+)</filing-type>", entry)
        title_m = re.search(r"<title[^>]*>([^<]+)</title>", entry)

        if date_m:
            fdate = date_m.group(1)
            if fdate >= cutoff:
                results.append({
                    "date": fdate,
                    "form": form_m.group(1) if form_m else "8-K",
                    "index_url": href_m.group(1) if href_m else "",
                    "title": title_m.group(1) if title_m else "",
                })

    return results


def parse_8k_items(index_url):
    """Try to extract 8-K item numbers from the filing index page."""
    text = fetch_text(index_url)
    if not text:
        return []

    items = []
    # Look for item references in the filing
    item_matches = re.findall(r"Item\s+(\d+\.\d+)", text, re.IGNORECASE)
    for item_num in item_matches:
        if item_num not in items:
            items.append(item_num)
    return items


def main():
    days = 7
    if "--days" in sys.argv:
        idx = sys.argv.index("--days")
        if idx + 1 < len(sys.argv):
            days = int(sys.argv[idx + 1])

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"\n{'='*70}")
    print(f"  REGINALD 8-K Monitor — {now} (last {days} days)")
    print(f"{'='*70}")

    any_critical = False
    total_filings = 0

    for ticker, info in TARGETS.items():
        cik = info["cik"]
        name = info["name"]
        print(f"\n  {ticker} ({name})")
        print(f"  {'-'*50}")

        filings = get_8k_filings(cik, days=days)
        if not filings:
            print(f"  No 8-K filings in last {days} days.")
            continue

        total_filings += len(filings)

        for filing in filings:
            items = parse_8k_items(filing["index_url"]) if filing["index_url"] else []
            import time
            time.sleep(0.12)  # EDGAR rate limit

            # Determine highest severity
            severity = "⚪"
            item_details = []
            for item_num in items:
                flag_info = ITEM_FLAGS.get(item_num, ("⚪", f"Item {item_num}"))
                item_details.append(f"{flag_info[0]} {item_num}: {flag_info[1]}")
                if flag_info[0] == "🔴":
                    severity = "🔴"
                    any_critical = True
                elif flag_info[0] == "🟠" and severity != "🔴":
                    severity = "🟠"

            print(f"  {severity} {filing['date']}  {filing['form']}")
            if item_details:
                for detail in item_details:
                    print(f"       {detail}")
            else:
                print(f"       (no item details parsed)")

    if total_filings == 0:
        print(f"\n  ✅ No 8-K filings across any thesis name in last {days} days.")
    elif not any_critical:
        print(f"\n  ℹ️  {total_filings} filing(s) found — none critical.")
    else:
        print(f"\n  🔴 CRITICAL 8-K filing(s) detected — review immediately.")

    print()


if __name__ == "__main__":
    main()
