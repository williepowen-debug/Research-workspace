#!/usr/bin/env python3
"""
Stale Detection Script for Agent Workbooks
Flags entries where Last_Updated > THRESHOLD days ago.

Usage: python3 stale_check.py [--days 7] [--agent OTTO]
"""

import csv
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

# Configuration
WORKSPACE = Path(__file__).parent.parent
THRESHOLD_DAYS = 7

# Workbook files to check (relative to agent folder)
# Note: ML.tsv excluded — dates are historical event dates, not update dates
WORKBOOKS = {
    'VX.tsv': 'Last_Updated',
    'FL.tsv': 'Last_Validated',
    # 'ML.tsv': 'Date',  # Excluded: historical log
}

# Agent folders to scan
AGENTS = [
    'AGENTS/OTTO',
    'AGENTS/CARL',
    'AGENTS/LABOR',
    'AGENTS/HENRY',
    'AGENTS/SAM',
    'AGENTS/LIQUID',
    'AGENTS/MARCO',
    'AGENTS/REGINALD',
    'AGENTS/REGINALD/sub-agents/BROCK',
    'AGENTS/REGINALD/sub-agents/CORAL',
    'AGENTS/REGINALD/sub-agents/CREED',
    'AGENTS/REGINALD/sub-agents/TEX',
    'AGENTS/REGINALD/sub-agents/RENO',
]

def parse_date(date_str):
    """Try to parse various date formats."""
    if not date_str or date_str in ['Ongoing', 'TBD', '-', 'N/A']:
        return None
    
    # Try common formats
    formats = [
        '%Y-%m-%d',
        '%Y-%m',
        '%Y',
        '%Y-%m-%d %H:%M',
    ]
    
    # Clean up date string
    date_str = date_str.strip().split()[0]  # Take first part if datetime
    
    for fmt in formats:
        try:
            return datetime.strptime(date_str[:len(fmt.replace('%', '').replace('-', '').replace(' ', ''))], fmt)
        except:
            continue
    
    # Try extracting year-month-day pattern
    import re
    match = re.search(r'(\d{4})-(\d{2})-(\d{2})', date_str)
    if match:
        try:
            return datetime(int(match.group(1)), int(match.group(2)), int(match.group(3)))
        except:
            pass
    
    return None

def check_workbook(filepath, date_column, threshold_days, today):
    """Check a single workbook for stale entries."""
    stale = []
    
    if not filepath.exists():
        return stale
    
    try:
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f, delimiter='\t')
            
            if date_column not in reader.fieldnames:
                return stale
            
            for row in reader:
                date_str = row.get(date_column, '')
                parsed = parse_date(date_str)
                
                if parsed:
                    age = (today - parsed).days
                    if age > threshold_days:
                        stale.append({
                            'id': row.get('ID', row.get('Vector_ID', '?')),
                            'date': date_str,
                            'age_days': age,
                            'name': row.get('Name', row.get('Catalyst', row.get('Observation', '')))[:50],
                        })
    except Exception as e:
        print(f"  Error reading {filepath}: {e}", file=sys.stderr)
    
    return stale

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Check for stale workbook entries')
    parser.add_argument('--days', type=int, default=THRESHOLD_DAYS, help='Threshold days (default: 7)')
    parser.add_argument('--agent', type=str, help='Specific agent to check (e.g., OTTO)')
    args = parser.parse_args()
    
    today = datetime.now()
    threshold = args.days
    total_stale = 0
    
    print(f"=== STALE CHECK (>{threshold} days) ===")
    print(f"Date: {today.strftime('%Y-%m-%d')}")
    print()
    
    agents_to_check = AGENTS
    if args.agent:
        agents_to_check = [a for a in AGENTS if args.agent.upper() in a.upper()]
    
    for agent_path in agents_to_check:
        agent_dir = WORKSPACE / agent_path / 'workbook'
        
        if not agent_dir.exists():
            continue
        
        agent_name = agent_path.split('/')[-1]
        agent_stale = []
        
        for workbook, date_col in WORKBOOKS.items():
            filepath = agent_dir / workbook
            stale = check_workbook(filepath, date_col, threshold, today)
            
            for s in stale:
                s['workbook'] = workbook
            
            agent_stale.extend(stale)
        
        if agent_stale:
            print(f"📁 {agent_name}: {len(agent_stale)} stale entries")
            for s in sorted(agent_stale, key=lambda x: -x['age_days'])[:5]:
                print(f"   • {s['workbook']} {s['id']}: {s['age_days']}d old — {s['name']}...")
            if len(agent_stale) > 5:
                print(f"   ... and {len(agent_stale) - 5} more")
            print()
            total_stale += len(agent_stale)
    
    print(f"=== TOTAL: {total_stale} stale entries ===")
    
    if total_stale == 0:
        print("✅ All entries fresh!")
    elif total_stale < 10:
        print("🟡 Minor staleness — review when convenient")
    else:
        print("🟠 Significant staleness — consider update sweep")
    
    return total_stale

if __name__ == '__main__':
    sys.exit(0 if main() < 50 else 1)
