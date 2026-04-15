#!/usr/bin/env python3
"""
OTTO ABS Issuance Tracker
Monitors subprime auto ABS issuance, spreads, and rating actions.
Flags shelf halts, spread widening, and downgrades.

Data sources:
- KBRA U.S. Auto Loan ABS Indices (public)
- S&P Global Auto ABS Tracker (public)
- Fitch Auto ABS Indices (public)
- Moody's ABS research (public)

Appends to workbook TSV and prints trend summary.

Usage:
  python3 abs_issuance_tracker.py          # full run
  python3 abs_issuance_tracker.py --print  # print latest only
"""

import urllib.request
import re
import sys
from datetime import datetime
from pathlib import Path

OTTO_DIR = Path(__file__).resolve().parent.parent
WORKBOOK = OTTO_DIR / 'workbook'
ISSUANCE_TSV = WORKBOOK / 'ABS_ISSUANCE.tsv'

# Major subprime ABS issuers to track
ISSUERS = [
    'Santander', 'Ally', 'Wells Fargo', 'Capital One', 'Carvana',
    'DriveTime', 'Westlake', 'Exeter', 'CPS', 'AmeriCredit',
    'Flagship', 'Lendbuzz', 'SAFCO'
]

# Rating agencies to monitor
AGENCIES = ['KBRA', 'S&P', 'Fitch', 'Moody\'s']


def fetch_kbra_data():
    """Fetch KBRA auto ABS indices (placeholder)."""
    # URL: https://www.kbra.com/us/products/autoloanabs
    # Would scrape or use API if available
    return {
        'source': 'KBRA',
        'data': None,
        'note': 'Manual check required - kbra.com'
    }


def fetch_sp_global_data():
    """Fetch S&P Global auto ABS tracker (placeholder)."""
    # URL: https://www.spglobal.com/ratings/en/research-insights/sector-specific
    return {
        'source': 'S&P Global',
        'data': None,
        'note': 'Manual check required - spglobal.com'
    }


def fetch_fitch_data():
    """Fetch Fitch auto ABS indices (placeholder)."""
    # URL: https://www.fitchratings.com/sector/abs
    return {
        'source': 'Fitch',
        'data': None,
        'note': 'Manual check required - fitchratings.com'
    }


def check_shelf_halts():
    """Check for ABS shelf halts or pauses."""
    # Historical reference: Santander 2023 halt
    # Would search news, SEC filings, rating agency reports
    
    return {
        'halts': [],  # {'issuer': 'XXX', 'date': 'YYYY-MM-DD', 'reason': '...'}
        'note': 'Manual monitoring required'
    }


def check_rating_actions():
    """Check for rating downgrades or negative outlooks."""
    # Would scrape rating agency websites
    
    return {
        'downgrades': [],  # {'issuer': 'XXX', 'date': 'YYYY-MM-DD', 'action': '...'}
        'negative_outlook': [],
        'note': 'Manual check of KBRA, S&P, Fitch, Moodys required'
    }


def check_new_issuance():
    """Check for new ABS deals priced."""
    # Would monitor ABS market data
    
    return {
        'deals': [],  # {'issuer': 'XXX', 'date': 'YYYY-MM-DD', 'size': '100M', 'spread': '150bps'}
        'note': 'Manual check of market data required'
    }


def calculate_issuance_trend(new_deals, historical_volume):
    """Calculate YoY issuance trend."""
    # S&P forecast: 4% drop in 2026 ($122B vs $127B)
    return {
        'forecast': -4,  # %
        'actual_ytd': None,  # Would calculate from deals
        'note': 'S&P forecast: $122B (-4% YoY)'
    }


def append_to_tsv(data):
    """Append issuance data to TSV."""
    WORKBOOK.mkdir(parents=True, exist_ok=True)
    
    header = 'date\ttotal_deals_ytd\ttotal_volume_ytd\tshelf_halts\tdowngrades\tnegative_outlooks\tspread_trend\tnotes\n'
    
    file_exists = ISSUANCE_TSV.exists()
    with open(ISSUANCE_TSV, 'a', encoding='utf-8') as f:
        if not file_exists:
            f.write(header)
        
        halts = len(data['shelf_halts']['halts'])
        downgrades = len(data['rating_actions']['downgrades'])
        outlooks = len(data['rating_actions']['negative_outlook'])
        
        notes = f"New deals: {len(data['new_issuance']['deals'])}; "
        notes += f"Trend: {data['trend']['note']}"
        
        f.write(f"{data['date']}\t{data['deal_count']}\t{data['volume']}\t"
               f"{halts}\t{downgrades}\t{outlooks}\t{data['spread_trend']}\t{notes}\n")


def print_summary():
    """Print latest issuance summary."""
    if not ISSUANCE_TSV.exists():
        print("No issuance data found. Run without --print first.")
        return
    
    print("\n" + "="*80)
    print("OTTO ABS ISSUANCE TRACKER — Latest Reading")
    print("="*80)
    
    with open(ISSUANCE_TSV, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    if len(lines) <= 1:
        print("No data recorded yet.")
        return
    
    # Get latest
    latest = lines[-1].strip().split('\t')
    if len(latest) >= 8:
        print(f"\nDate: {latest[0]}")
        print(f"YTD Deals: {latest[1]}")
        print(f"YTD Volume: {latest[2]}")
        print(f"Shelf Halts: {latest[3]}")
        print(f"Downgrades: {latest[4]}")
        print(f"Negative Outlooks: {latest[5]}")
        print(f"Spread Trend: {latest[6]}")
        print(f"\nNotes: {latest[7]}")
    
    print("\n" + "="*80)
    print("\nKey Levels to Watch:")
    print("  • Any shelf halt = 🔴 (OTTO-07 prediction)")
    print("  • BBB spreads >250bps = 🔴 (OTTO-05 prediction)")
    print("  • 3+ downgrades in 30 days = 🟠")
    print("  • Issuance volume down >10% YoY = 🟠")
    print("="*80)


def main():
    if '--print' in sys.argv:
        print_summary()
        return
    
    print("OTTO ABS Issuance Tracker")
    print("="*50)
    
    today = datetime.now().strftime('%Y-%m-%d')
    
    print("\nFetching KBRA data...")
    kbra = fetch_kbra_data()
    print(f"  Status: {kbra['note']}")
    
    print("\nFetching S&P Global data...")
    sp = fetch_sp_global_data()
    print(f"  Status: {sp['note']}")
    
    print("\nFetching Fitch data...")
    fitch = fetch_fitch_data()
    print(f"  Status: {fitch['note']}")
    
    print("\nChecking for shelf halts...")
    halts = check_shelf_halts()
    print(f"  Halts found: {len(halts['halts'])}")
    
    print("\nChecking rating actions...")
    ratings = check_rating_actions()
    print(f"  Downgrades: {len(ratings['downgrades'])}")
    print(f"  Negative outlooks: {len(ratings['negative_outlook'])}")
    
    print("\nChecking new issuance...")
    new = check_new_issuance()
    print(f"  New deals: {len(new['deals'])}")
    
    trend = calculate_issuance_trend(new, None)
    print(f"  Trend: {trend['note']}")
    
    data = {
        'date': today,
        'deal_count': len(new['deals']),
        'volume': 'TBD',  # Would calculate from deals
        'shelf_halts': halts,
        'rating_actions': ratings,
        'new_issuance': new,
        'trend': trend,
        'spread_trend': 'TBD'  # Would calculate from indices
    }
    
    append_to_tsv(data)
    print(f"\n✓ Appended to {ISSUANCE_TSV}")
    
    print_summary()
    
    print("\n⚠ This script uses placeholder data.")
    print("To activate: Add web scraping for KBRA, S&P, Fitch, or manual data entry.")
    print("\nManual checklist for OTTO operator:")
    print("  [ ] Check kbra.com for auto ABS indices")
    print("  [ ] Check spglobal.com for auto ABS tracker")
    print("  [ ] Check fitchratings.com for auto ABS")
    print("  [ ] Search 'shelf halt subprime auto ABS'")
    print("  [ ] Search 'downgrade subprime auto ABS'")


if __name__ == '__main__':
    main()
