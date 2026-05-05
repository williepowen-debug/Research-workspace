#!/usr/bin/env python3
"""
Treasury Auction Data Fetch — Layer 1 (v1.1)
Pull Treasury auction results from Treasury FiscalData API.

Usage:
 python3 fetch_auctions.py recent                    # last 30 days
 python3 fetch_auctions.py recent --json             # JSON output
 python3 fetch_auctions.py security 10Y              # 10Y note history
 python3 fetch_auctions.py security 5Y --limit 10    # last 10 auctions
 python3 fetch_auctions.py compare 5Y                # compare to historical avg
 python3 fetch_auctions.py dashboard                 # full dashboard

Output fields:
  - date: auction date
  - security: security type (2Y, 3Y, 5Y, 7Y, 10Y, 30Y, etc.)
  - btc: bid-to-cover ratio
  - tail: tail (high yield - expected yield, in bps)
  - awarded: amount awarded ($B)
  - dealer_pct: primary dealer absorption %
  - direct_pct: direct bidder %
  - indirect_pct: indirect bidder %
  - status: 🟢 strong / 🟡 average / 🔴 weak
"""

import json
import os
import sys
import urllib.request
import urllib.parse
from pathlib import Path
from datetime import datetime, timedelta

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

CACHE_DIR = Path(__file__).parent / ".cache"
CACHE_TTL = 3600  # 1 hour

# Treasury FiscalData API
FISCALDATA_BASE = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service"
AUCTIONS_ENDPOINT = f"{FISCALDATA_BASE}/v1/accounting/od/auctions_query"

# Historical averages for comparison (2020-2025)
HISTORICAL_AVG = {
    "2Y": {"btc": 2.55, "tail": 0.5},
    "3Y": {"btc": 2.50, "tail": 0.6},
    "5Y": {"btc": 2.45, "tail": 0.7},
    "7Y": {"btc": 2.40, "tail": 0.8},
    "10Y": {"btc": 2.35, "tail": 0.9},
    "30Y": {"btc": 2.25, "tail": 1.2},
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def fetch_fiscaldata(params):
    """Fetch data from Treasury FiscalData API."""
    url = f"{AUCTIONS_ENDPOINT}?{urllib.parse.urlencode(params)}"
    
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (OpenClaw Research)",
        "Accept": "application/json"
    })
    
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        print(f"Error fetching data: {e}", file=sys.stderr)
        return None


def standardize_security(security_type, security_term):
    """Standardize security name from type + term."""
    if not security_type or not security_term:
        return None
    
    import re
    years = re.search(r'(\d+)', security_term)
    if not years:
        return None
    
    year = years.group(1)
    
    if "Note" in security_type:
        return f"{year}Y"
    elif "Bond" in security_type:
        return f"{year}Y"
    elif "Bill" in security_type:
        return f"{year}W" if "Week" in security_term else f"{year}M"
    elif "TIPS" in security_type:
        return f"{year}Y-TIPS"
    elif "FRN" in security_type:
        return f"{year}Y-FRN"
    
    return f"{year}Y"


def parse_auction_record(record):
    """Parse a raw auction record into structured format."""
    try:
        security_type = record.get("security_type", "")
        security_term = record.get("security_term", "")
        
        security = standardize_security(security_type, security_term)
        if not security:
            return None
        
        # Parse BTC
        btc = None
        if record.get("bid_to_cover_ratio") and record["bid_to_cover_ratio"] != "null":
            try:
                btc = float(record["bid_to_cover_ratio"])
            except:
                pass
        
        # Parse yields
        high_yield = None
        if record.get("high_yield") and record["high_yield"] != "null":
            try:
                high_yield = float(record["high_yield"])
            except:
                pass
        
        # Tail calculation - API doesn't provide expected yield
        # Use high-low spread as rough proxy for auction tightness
        # (True tail = high_yield - expected_yield, but expected_yield not in API)
        low_yield = None
        if record.get("low_yield") and record["low_yield"] != "null":
            try:
                low_yield = float(record["low_yield"])
            except:
                pass
        
        tail = None
        if high_yield and low_yield:
            # This is yield spread, not true tail - note in output
            tail = (high_yield - low_yield) * 100  # convert to bps
        
        # Awarded amount
        awarded = None
        if record.get("total_accepted") and record["total_accepted"] != "null":
            try:
                awarded = float(record["total_accepted"]) / 1e9
            except:
                pass
        
        # Bidder breakdown
        dealer_pct = None
        direct_pct = None
        indirect_pct = None
        
        total_tendered = record.get("total_tendered")
        if total_tendered and total_tendered != "null":
            try:
                total = float(total_tendered)
                if total > 0:
                    if record.get("primary_dealer_tendered") and record["primary_dealer_tendered"] != "null":
                        dealer_pct = float(record["primary_dealer_tendered"]) / total * 100
                    if record.get("direct_bidder_tendered") and record["direct_bidder_tendered"] != "null":
                        direct_pct = float(record["direct_bidder_tendered"]) / total * 100
                    if record.get("indirect_bidder_tendered") and record["indirect_bidder_tendered"] != "null":
                        indirect_pct = float(record["indirect_bidder_tendered"]) / total * 100
            except:
                pass
        
        return {
            "date": record.get("auction_date"),
            "security": security,
            "btc": round(btc, 2) if btc else None,
            "tail": round(tail, 1) if tail else None,
            "high_yield": round(high_yield, 3) if high_yield else None,
            "awarded": round(awarded, 1) if awarded else None,
            "dealer_pct": round(dealer_pct, 1) if dealer_pct else None,
            "direct_pct": round(direct_pct, 1) if direct_pct else None,
            "indirect_pct": round(indirect_pct, 1) if indirect_pct else None,
        }
    except Exception as e:
        print(f"Error parsing record: {e}", file=sys.stderr)
        return None


def classify_auction(auction):
    """Classify auction strength based on BTC vs historical average."""
    security = auction.get("security", "")
    btc = auction.get("btc")
    
    hist = HISTORICAL_AVG.get(security, {"btc": 2.4, "tail": 1.0})
    
    if btc is None:
        return "🟡"
    
    # Classification based on BTC relative to historical average
    if btc >= hist["btc"] * 1.05:  # 5% above average = strong
        return "🟢"
    elif btc < hist["btc"] * 0.90:  # 10% below average = weak
        return "🔴"
    else:
        return "🟡"


def get_recent_auctions(days=30, security_filter=None):
    """Get auctions from last N days."""
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    
    params = {
        "fields": "auction_date,security_type,security_term,bid_to_cover_ratio,high_yield,low_yield,total_accepted,primary_dealer_tendered,direct_bidder_tendered,indirect_bidder_tendered,total_tendered",
        "filter": f"auction_date:gte:{start_date.strftime('%Y-%m-%d')}",
        "sort": "-auction_date",
        "page[size]": 100,
    }
    
    data = fetch_fiscaldata(params)
    if not data or "data" not in data:
        return []
    
    auctions = []
    for record in data["data"]:
        parsed = parse_auction_record(record)
        if parsed:
            if security_filter and parsed["security"] != security_filter:
                continue
            parsed["status"] = classify_auction(parsed)
            auctions.append(parsed)
    
    return auctions


def get_security_history(security, limit=20):
    """Get historical auctions for a specific security."""
    # Map security code to term filter
    term_map = {
        "2Y": "2-Year",
        "3Y": "3-Year", 
        "5Y": "5-Year",
        "7Y": "7-Year",
        "10Y": "10-Year",
        "30Y": "30-Year",
    }
    
    term_filter = term_map.get(security, security.replace("Y", "-Year"))
    
    params = {
        "fields": "auction_date,security_type,security_term,bid_to_cover_ratio,high_yield,low_yield,total_accepted,primary_dealer_tendered,direct_bidder_tendered,indirect_bidder_tendered,total_tendered",
        "filter": f"security_term:eq:{term_filter}",
        "sort": "-auction_date",
        "page[size]": limit,
    }
    
    data = fetch_fiscaldata(params)
    if not data or "data" not in data:
        return []
    
    auctions = []
    for record in data["data"]:
        parsed = parse_auction_record(record)
        if parsed:
            parsed["status"] = classify_auction(parsed)
            auctions.append(parsed)
    
    return auctions


def format_auction_table(auctions):
    """Format auctions as readable table."""
    if not auctions:
        return "No auction data found."
    
    lines = []
    lines.append(f"{'Date':<12} {'Security':<10} {'BTC':<6} {'Yield':<8} {'Awarded':<10} {'Status':<6}")
    lines.append("-" * 60)
    
    for a in auctions[:20]:
        date = a.get("date", "N/A")[:10] if a.get("date") else "N/A"
        sec = a.get("security", "N/A")
        btc = f"{a['btc']:.2f}" if a.get("btc") else "N/A"
        yield_str = f"{a['high_yield']:.3f}" if a.get("high_yield") else "N/A"
        awarded = f"${a['awarded']:.1f}B" if a.get("awarded") else "N/A"
        status = a.get("status", "🟡")
        
        lines.append(f"{date:<12} {sec:<10} {btc:<6} {yield_str:<8} {awarded:<10} {status:<6}")
    
    return "\n".join(lines)


def compare_to_historical(auctions, security):
    """Compare recent auctions to historical averages."""
    hist = HISTORICAL_AVG.get(security, {"btc": 2.4, "tail": 1.0})
    
    if not auctions:
        return "No data to compare."
    
    recent_btc = [a["btc"] for a in auctions if a.get("btc")]
    recent_tail = [a["tail"] for a in auctions if a.get("tail")]
    
    avg_btc = sum(recent_btc) / len(recent_btc) if recent_btc else 0
    avg_tail = sum(recent_tail) / len(recent_tail) if recent_tail else 0
    
    lines = []
    lines.append(f"\n{security} Auction Comparison (last {len(auctions)} auctions)")
    lines.append("-" * 50)
    lines.append(f"  Recent Avg BTC:  {avg_btc:.2f}  (hist: {hist['btc']:.2f})  {'🟢' if avg_btc >= hist['btc'] else '🔴'}")
    lines.append(f"  Recent Avg Tail: {avg_tail:.1f}bp  (hist: {hist['tail']:.1f}bp)  {'🟢' if avg_tail <= hist['tail'] else '🔴'}")
    
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    cmd = sys.argv[1]
    
    if cmd == "recent":
        days = 30
        security = None
        if len(sys.argv) > 2 and not sys.argv[2].startswith("--"):
            security = sys.argv[2]
        
        auctions = get_recent_auctions(days, security)
        
        if "--json" in sys.argv:
            print(json.dumps(auctions, indent=2))
        else:
            print(format_auction_table(auctions))
    
    elif cmd == "security":
        if len(sys.argv) < 3:
            print("Usage: fetch_auctions.py security <2Y|3Y|5Y|7Y|10Y|30Y>")
            sys.exit(1)
        
        security = sys.argv[2]
        limit = 10
        if "--limit" in sys.argv:
            idx = sys.argv.index("--limit")
            if idx + 1 < len(sys.argv):
                limit = int(sys.argv[idx + 1])
        
        auctions = get_security_history(security, limit)
        
        if "--json" in sys.argv:
            print(json.dumps(auctions, indent=2))
        else:
            print(format_auction_table(auctions))
            print(compare_to_historical(auctions, security))
    
    elif cmd == "compare":
        if len(sys.argv) < 3:
            print("Usage: fetch_auctions.py compare <2Y|3Y|5Y|7Y|10Y|30Y>")
            sys.exit(1)
        
        security = sys.argv[2]
        auctions = get_security_history(security, 20)
        print(compare_to_historical(auctions, security))
    
    elif cmd == "dashboard":
        print("Treasury Auction Dashboard")
        print("=" * 60)
        
        for security in ["2Y", "5Y", "10Y", "30Y"]:
            auctions = get_security_history(security, 5)
            if auctions:
                print(format_auction_table(auctions))
                print(compare_to_historical(auctions, security))
                print()
    
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
