#!/usr/bin/env python3
"""Convert MARCO ML.tsv to KB.tsv format"""

import csv
import re

def map_category(domain):
    """Map ML domain to MARCO KB category"""
    domain_upper = domain.upper()
    if any(x in domain_upper for x in ['IVF', 'TOURISM', 'VISITOR']):
        return 'TOURISM'
    elif any(x in domain_upper for x in ['WFD', 'WORKFORCE', 'LAT', 'EMPLOYMENT']):
        return 'WORKFORCE'
    elif any(x in domain_upper for x in ['IMG', 'MIG', 'MIGRATION', 'DOMESTIC']):
        return 'MIGRATION'
    elif any(x in domain_upper for x in ['BDR', 'BORDER', 'CROSS']):
        return 'BORDER'
    elif any(x in domain_upper for x in ['AGR', 'H2A', 'FARM', 'AGRICULTURE']):
        return 'AGRICULTURE'
    elif any(x in domain_upper for x in ['TX', 'CA', 'AZ', 'NV', 'FL', 'HOUSING', 'REAL ESTATE']):
        return 'HOUSING'
    elif any(x in domain_upper for x in ['ENF', 'ENFORCEMENT']):
        return 'ENFORCEMENT'
    elif any(x in domain_upper for x in ['REM', 'REMITTANCE']):
        return 'REMITTANCES'
    else:
        return 'MIGRATION'

def map_confidence(conf_str):
    """Map percentage confidence to A1-C3 scale"""
    # Remove % sign and convert to int
    conf_clean = conf_str.replace('%', '').strip()
    try:
        conf = int(conf_clean)
    except:
        return 'B1'  # default
    
    if conf >= 90:
        return 'A1'
    elif conf >= 80:
        return 'A2'
    elif conf >= 70:
        return 'A3'
    elif conf >= 60:
        return 'B1'
    else:
        return 'C3'

def map_source(source_str):
    """Map source to standard tags"""
    source_upper = source_str.upper()
    if 'BLS' in source_upper:
        return 'BLS'
    elif 'FRED' in source_upper:
        return 'FRED'
    elif 'CENSUS' in source_upper or 'ACS' in source_upper:
        return 'CENSUS'
    elif 'WSJ' in source_upper or 'WALL STREET' in source_upper:
        return 'WSJ'
    elif 'REUTERS' in source_upper:
        return 'REUTERS'
    elif 'BLOOMBERG' in source_upper:
        return 'BLOOMBERG'
    elif 'FT' in source_upper or 'FINANCIAL TIMES' in source_upper:
        return 'FT'
    elif 'NYT' in source_upper or 'NEW YORK TIMES' in source_upper:
        return 'NYT'
    elif 'STATCAN' in source_upper or 'STATISTICS CANADA' in source_upper:
        return 'STATCAN'
    elif 'DOL' in source_upper or 'ETA' in source_upper or 'OFLC' in source_upper:
        return 'DOL'
    elif 'BANXICO' in source_upper:
        return 'BANXICO'
    elif 'CBP' in source_upper:
        return 'CBP'
    elif 'ICE' in source_upper:
        return 'ICE'
    elif 'TSA' in source_upper:
        return 'TSA'
    elif 'DHS' in source_upper:
        return 'DHS'
    elif 'USDA' in source_upper or 'NASS' in source_upper:
        return 'USDA'
    elif 'NFIB' in source_upper:
        return 'NFIB'
    elif 'ADP' in source_upper:
        return 'ADP'
    elif 'BEA' in source_upper:
        return 'BEA'
    else:
        return 'VARIOUS'

def truncate_key_fact(desc, analysis, max_len=250):
    """Combine description and analysis, truncate to max length"""
    combined = f"{desc} {analysis}".strip()
    if len(combined) <= max_len:
        return combined
    # Try to truncate at sentence boundary
    truncated = combined[:max_len]
    last_period = truncated.rfind('.')
    if last_period > max_len * 0.7:  # If we can get at least 70% of max_len with complete sentence
        return truncated[:last_period + 1]
    return truncated + "..."

def main():
    import sys
    
    # Check for batch argument
    batch = sys.argv[1] if len(sys.argv) > 1 else 'all'
    
    # Read ML.tsv
    ml_entries = []
    with open('workbook/ML.tsv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            ml_entries.append(row)
    
    # Sort by ID
    ml_entries.sort(key=lambda x: x['ID'])
    
    # Select batch
    if batch == 'first':
        selected = ml_entries[:35]
        mode = 'w'  # Write new file
    elif batch == 'second':
        selected = ml_entries[35:]
        mode = 'a'  # Append to existing
    else:
        selected = ml_entries
        mode = 'w'
    
    # Create or append to KB.tsv
    with open('workbook/KB.tsv', mode, newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='\t', lineterminator='\n')
        
        # Write header only if creating new file
        if mode == 'w':
            writer.writerow(['ID', 'Date', 'Category', 'Topic', 'Key_Fact', 'Confidence', 'Source', 'Notes'])
        
        for entry in selected:
            kb_id = entry['ID'].replace('ML-', 'KB-MARCO-')
            date = entry['Created']
            category = map_category(entry['Domain'])
            topic = entry['Title']
            key_fact = truncate_key_fact(entry['Description'], entry['Analysis'])
            confidence = map_confidence(entry['Confidence'])
            source = map_source(entry['Source'])
            notes = entry.get('Notes', '')
            
            writer.writerow([kb_id, date, category, topic, key_fact, confidence, source, notes])
    
    print(f"{'Created' if mode == 'w' else 'Appended'} KB.tsv with {len(selected)} entries (batch: {batch})")

if __name__ == '__main__':
    main()
