#!/usr/bin/env python3
"""
OTTO Extension Unwind Proxy Monitor
Tracks alternative signals that proxy for extension unwind risk.
When lenders stop extending loans, these signals spike.

Signals:
- Repo market volumes (liquidity stress)
- Warehouse line tightening (bank pullbacks)
- Employment verification delays (immigration enforcement)
- State-level vehicle registration data (repo proxy)

Appends to workbook TSV and prints composite risk score.

Usage:
  python3 extension_proxy.py          # full run
  python3 extension_proxy.py --print  # print latest only
"""

import urllib.request
import json
import sys
import os
from datetime import datetime
from pathlib import Path

OTTO_DIR = Path(__file__).resolve().parent.parent
WORKBOOK = OTTO_DIR / 'workbook'
PROXY_TSV = WORKBOOK / 'EXTENSION_PROXY.tsv'

# FRED series for repo market
FRED_SERIES = {
    'REPO_VOL': 'RRPONTSYD',  # Overnight reverse repo volume
    'SOFR': 'SOFR',           # Secured overnight financing rate
    'SOFR_VOL': 'SOFRVOL',    # SOFR volume
}

# News search terms for warehouse tightening
WAREHOUSE_TERMS = [
    'warehouse line',
    'asset-based lending',
    'subprime auto',
    'tightening',
    'pulled back',
    'reduced exposure'
]

# States with high subprime auto + immigration enforcement
STRESS_STATES = ['MS', 'LA', 'GA', 'TX', 'FL', 'AL', 'SC']


def fetch_fred_data(series_id):
    """Fetch latest data from FRED (placeholder - needs API key)."""
    # In production: use FRED API with key
    # For now, return placeholder
    return None


def calculate_repo_stress():
    """
    Calculate repo market stress indicator.
    High volumes + rate spikes = liquidity stress = extension unwind risk.
    """
    # Placeholder - would fetch actual FRED data
    # Returns 0-100 score
    
    # Logic:
    # - SOFR volume > 90th percentile = +30 points
    # - SOFR rate > 5.5% = +30 points
    # - Reverse repo volume spike = +40 points
    
    return {
        'repo_score': 0,  # Placeholder
        'sofr_rate': None,
        'sofr_vol': None,
        'repo_vol': None,
        'note': 'FRED API key required for live data'
    }


def check_warehouse_tightening():
    """
    Check for warehouse line tightening news.
    Banks pulling back = subprime lenders can't extend = forced repo.
    """
    # Placeholder - would search news APIs
    # Key sources: Bloomberg, Reuters, Auto Finance News
    
    recent_signals = [
        # Example format:
        # {'date': '2026-04-10', 'bank': 'Barclays', 'action': 'pulled back on ABL'}
    ]
    
    return {
        'warehouse_score': len(recent_signals) * 20,  # 20 points per signal
        'signals': recent_signals,
        'note': 'Manual news search required'
    }


def check_employment_verification():
    """
    Check for employment verification delays.
    Immigration enforcement = payroll delays = can't verify income = no extensions.
    """
    # Placeholder - would check DOL data, E-Verify metrics
    # Source: USCIS E-Verify reports, state labor departments
    
    return {
        'ev_score': 0,
        'ev_delays': [],
        'note': 'DOL/USCIS data integration pending'
    }


def check_state_registrations():
    """
    Check state vehicle registration data for repo proxy.
    Declining registrations + high DQ = repos increasing.
    """
    # Placeholder - would scrape state DMV data
    # Key: TX, FL, GA monthly registration reports
    
    return {
        'registration_score': 0,
        'state_data': {},
        'note': 'State DMV data integration pending'
    }


def calculate_composite_risk(repo, warehouse, ev, registration):
    """Calculate composite extension unwind risk score (0-100)."""
    weights = {
        'repo': 0.30,
        'warehouse': 0.35,
        'ev': 0.20,
        'registration': 0.15
    }
    
    composite = (
        repo['repo_score'] * weights['repo'] +
        warehouse['warehouse_score'] * weights['warehouse'] +
        ev['ev_score'] * weights['ev'] +
        registration['registration_score'] * weights['registration']
    )
    
    return min(100, max(0, composite))


def get_risk_level(score):
    """Convert score to risk level."""
    if score < 25:
        return '🟢 LOW'
    elif score < 50:
        return '🟡 MODERATE'
    elif score < 75:
        return '🟠 ELEVATED'
    else:
        return '🔴 CRITICAL'


def append_to_tsv(data):
    """Append proxy data to TSV."""
    WORKBOOK.mkdir(parents=True, exist_ok=True)
    
    header = 'date\tcomposite_score\trisk_level\trepo_score\twarehouse_score\tev_score\tregistration_score\tnotes\n'
    
    file_exists = PROXY_TSV.exists()
    with open(PROXY_TSV, 'a', encoding='utf-8') as f:
        if not file_exists:
            f.write(header)
        
        notes = f"Repo: {data['repo']['note']}; Warehouse: {data['warehouse']['note']}"
        
        f.write(f"{data['date']}\t{data['composite']:.1f}\t{data['risk_level']}\t"
               f"{data['repo']['repo_score']}\t{data['warehouse']['warehouse_score']}\t"
               f"{data['ev']['ev_score']}\t{data['registration']['registration_score']}\t"
               f"{notes}\n")


def print_summary():
    """Print latest proxy scores."""
    if not PROXY_TSV.exists():
        print("No proxy data found. Run without --print first.")
        return
    
    print("\n" + "="*80)
    print("OTTO EXTENSION UNWIND PROXY — Latest Reading")
    print("="*80)
    
    with open(PROXY_TSV, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    if len(lines) <= 1:
        print("No data recorded yet.")
        return
    
    # Get latest
    latest = lines[-1].strip().split('\t')
    if len(latest) >= 8:
        print(f"\nDate: {latest[0]}")
        print(f"Composite Score: {latest[1]} {latest[2]}")
        print(f"\nComponent Scores:")
        print(f"  Repo Market:        {latest[3]}/100")
        print(f"  Warehouse Tightening: {latest[4]}/100")
        print(f"  Employment Verification: {latest[5]}/100")
        print(f"  State Registrations: {latest[6]}/100")
        print(f"\nNotes: {latest[7]}")
    
    print("\n" + "="*80)
    print("\nInterpretation:")
    print("  🟢 <25:   Extensions likely continuing")
    print("  🟡 25-50: Early warning — watch for bank commentary")
    print("  🟠 50-75: Tightening underway — extension unwind likely")
    print("  🔴 >75:   Full unwind in progress — losses crystallizing")
    print("="*80)


def main():
    if '--print' in sys.argv:
        print_summary()
        return
    
    print("OTTO Extension Unwind Proxy Monitor")
    print("="*50)
    
    today = datetime.now().strftime('%Y-%m-%d')
    
    print("\nFetching repo market data...")
    repo = calculate_repo_stress()
    print(f"  Repo stress score: {repo['repo_score']}/100")
    
    print("\nChecking warehouse tightening...")
    warehouse = check_warehouse_tightening()
    print(f"  Warehouse score: {warehouse['warehouse_score']}/100")
    print(f"  Signals found: {len(warehouse['signals'])}")
    
    print("\nChecking employment verification...")
    ev = check_employment_verification()
    print(f"  EV score: {ev['ev_score']}/100")
    
    print("\nChecking state registrations...")
    registration = check_state_registrations()
    print(f"  Registration score: {registration['registration_score']}/100")
    
    composite = calculate_composite_risk(repo, warehouse, ev, registration)
    risk_level = get_risk_level(composite)
    
    data = {
        'date': today,
        'composite': composite,
        'risk_level': risk_level,
        'repo': repo,
        'warehouse': warehouse,
        'ev': ev,
        'registration': registration
    }
    
    append_to_tsv(data)
    print(f"\n✓ Appended to {PROXY_TSV}")
    
    print_summary()
    
    print(f"\n⚠ This script uses placeholder data.")
    print(f"To activate: Add FRED API key, news search integration, DOL data feeds.")


if __name__ == '__main__':
    main()
