#!/usr/bin/env python3
"""Migrate BRENT KB.tsv from 6-column to 9-column schema."""

import csv
import re
import sys

INPUT = "/home/moltbot/.openclaw/workspace/AGENTS/BRENT/workbook/KB.tsv"
OUTPUT = "/home/moltbot/.openclaw/workspace/AGENTS/BRENT/workbook/KB_new.tsv"

# Group normalization map
GROUP_MAP = {
    "Hormuz": "HORMUZ",
    "Hormuz Historical": "HORMUZ",
    "Storage": "STORAGE",
    "OPEC+": "OPEC_UNWIND",
    "OPEC+ Unwind": "OPEC_UNWIND",
    "OPEC Spare Capacity": "OPEC_SPARE",
    "OPEC Policy": "OPEC_UNWIND",
    "Shale": "SHALE",
    "Tankers": "TANKERS",
    "Russia": "RUSSIA",
    "SPR": "SPR",
    "Cushing": "CUSHING",
    "Crack Spreads": "CRACK_SPREADS",
    "Crack Spreads / Jet Fuel": "CRACK_SPREADS",
    "Insurance": "HORMUZ",
    "Two-Phase": "PHASE_THESIS",
    "NFP": "MACRO",
    "Iran": "HORMUZ",
    "Positions": "POSITIONS",
    "Gas Prices": "PUMP_PRICES",
    "War": "WAR",
    "LNG": "LNG",
    "LNG/JKM": "LNG",
    "LNG/TTF": "LNG",
    "LNG/HH": "LNG",
    "LNG/Qatar": "LNG",
    "LNG/Freight": "LNG",
    "LNG/Cheniere": "LNG_CHENIERE",
    "LNG/Venture Global": "LNG_VG",
    "Demand Destruction": "DEMAND_DESTRUCTION",
    "Refinery Utilization": "REFINERY",
    "Pump Prices": "PUMP_PRICES",
    "STNG Earnings Model": "TANKERS",
    "STNG Exit Trigger": "TANKERS",
    "Macro Transmission": "MACRO_TRANSMISSION",
    "Energy Credit": "ENERGY_CREDIT",
    "Bypass Infrastructure": "BYPASS",
    "Sulphur Chain": "SULPHUR_CHAIN",
    "Sulphur Chain — UAE Dominance": "SULPHUR_CHAIN",
    "Sulphur Chain — No Alternative Suppliers": "SULPHUR_CHAIN",
    "Sulphur Chain — Acid Inventory Illusion": "SULPHUR_CHAIN",
    "Sulphur Chain — Kuwait Al-Zour Overstatement": "SULPHUR_CHAIN",
    "Sulphur Chain — SX-EW Cost Structure": "SULPHUR_CHAIN",
    "Sulphur Chain Timeline": "SULPHUR_CHAIN",
    "Sulphur → Copper/Cobalt Chain": "SULPHUR_COPPER",
    "Trade Signal — Copper": "SULPHUR_COPPER",
    "Taiwan LNG Vulnerability": "TAIWAN",
    "Taiwan Semiconductor Fragility": "TAIWAN",
    "Taiwan Grid — Nuclear Zero": "TAIWAN",
    "Taiwan Grid — Shortfall Scenarios": "TAIWAN",
    "Taiwan — TSMC Wafer Risk and Inventory Depletion": "TAIWAN",
    "Semiconductor Supply Chain Bottlenecks": "TAIWAN",
    "Secondary Chains — Fertilizer": "SECONDARY_CHAINS",
    "Secondary Chains — LPT/Transformer Bottleneck": "SECONDARY_CHAINS",
    "Secondary Chains — EM Sovereign Stress": "SECONDARY_CHAINS",
    "SPR Physical Constraints": "SPR",
}


def extract_entity(row_id, topic, fact, notes):
    """Extract the most specific entity/noun from the fact."""
    # Explicit mappings for known rows
    entity_map = {
        "KB-BRT-001": "Hormuz Strait",
        "KB-BRT-002": "Kuwait",
        "KB-BRT-003": "UAE",
        "KB-BRT-004": "Gulf States",
        "KB-BRT-005": "OPEC+",
        "KB-BRT-006": "US Shale",
        "KB-BRT-007": "Maersk",
        "KB-BRT-008": "Hormuz Strait",
        "KB-BRT-009": "Russia Shadow Fleet",
        "KB-BRT-010": "Russia",
        "KB-BRT-011": "US SPR",
        "KB-BRT-012": "Cushing",
        "KB-BRT-013": "Crack Spreads",
        "KB-BRT-014": "P&I Clubs",
        "KB-BRT-015": "Phase Thesis",
        "KB-BRT-016": "NFP / Brent",
        "KB-BRT-017": "Iran",
        "KB-BRT-018": "USO / STNG",
        "KB-BRT-019": "Pump Prices",
        "KB-BRT-020": "Iran War",
        "KB-BRT-021": "Qatar LNG / Japan",
        "KB-BRT-022": "Demand Destruction",
        "KB-BRT-023": "Pump Price Lag",
        "KB-BRT-024": "Demand Threshold",
        "KB-BRT-025": "EIA Data",
        "KB-BRT-026": "Airlines",
        "KB-BRT-027": "ATA / Ceridian",
        "KB-BRT-028": "OPEC+ Cuts",
        "KB-BRT-029": "OPEC+ Ramp",
        "KB-BRT-030": "Phase 2 Timing",
        "KB-BRT-031": "Saudi Arabia",
        "KB-BRT-032": "Kuwait Infrastructure",
        "KB-BRT-033": "OPEC+ Capacity Gap",
        "KB-BRT-034": "EV Inelasticity",
        "KB-BRT-035": "Iraq / Russia / Kazakhstan",
        "KB-BRT-036": "JKM",
        "KB-BRT-037": "TTF",
        "KB-BRT-038": "Henry Hub",
        "KB-BRT-039": "QatarEnergy",
        "KB-BRT-040": "ME LNG Exports",
        "KB-BRT-041": "LNG Freight",
        "KB-BRT-042": "Cheniere",
        "KB-BRT-043": "Cheniere",
        "KB-BRT-044": "Venture Global",
        "KB-BRT-045": "US Rig Count",
        "KB-BRT-046": "DUC Inventory",
        "KB-BRT-047": "US Production",
        "KB-BRT-048": "Permian Basin",
        "KB-BRT-049": "Shale Response",
        "KB-BRT-050": "Permian Operators",
        "KB-BRT-051": "HY Energy OAS",
        "KB-BRT-052": "HY Energy OAS",
        "KB-BRT-053": "OXY",
        "KB-BRT-054": "E&P Credit",
        "KB-BRT-055": "HY Energy OAS",
        "KB-BRT-056": "HY Energy Index",
        "KB-BRT-057": "OPEC+ Spare",
        "KB-BRT-058": "Saudi / UAE Spare",
        "KB-BRT-059": "Rapid Deployment",
        "KB-BRT-060": "Iraq",
        "KB-BRT-061": "Russia",
        "KB-BRT-062": "Petroline",
        "KB-BRT-063": "Yanbu Terminal",
        "KB-BRT-064": "ADCOP / Fujairah",
        "KB-BRT-065": "Kirkuk-Ceyhan",
        "KB-BRT-066": "Bypass Total",
        "KB-BRT-067": "US Refineries",
        "KB-BRT-068": "Gulf Coast Crack",
        "KB-BRT-069": "Jet Fuel Crack",
        "KB-BRT-070": "Pump Prices",
        "KB-BRT-071": "STNG",
        "KB-BRT-072": "STNG",
        "KB-BRT-073": "STNG",
        "KB-BRT-074": "Texas Banks 1986",
        "KB-BRT-075": "Hormuz Insurance",
        "KB-BRT-076": "Oil Shock Sequence",
        "KB-BRT-077": "Fed Policy",
        "KB-BRT-078": "Regional Banks 2014",
        "KB-BRT-079": "OPEC+ Mar Meeting",
        "KB-BRT-080": "Gulf Sulphur",
        "KB-BRT-081": "Qatar Ras Laffan",
        "KB-BRT-082": "H2SO4 Prices",
        "KB-BRT-083": "DRC / Zambia Copper",
        "KB-BRT-084": "Kamoa-Kakula",
        "KB-BRT-085": "Acid Timeline",
        "KB-BRT-086": "CPER Trade",
        "KB-BRT-087": "Taiwan LNG",
        "KB-BRT-088": "TSMC / SEMI F47",
        "KB-BRT-089": "ABF Substrates",
        "KB-BRT-090": "US SPR",
        "KB-BRT-091": "SPR Caverns",
        "KB-BRT-092": "Gulf Fertilizer",
        "KB-BRT-093": "LPT / Transformers",
        "KB-BRT-094": "Egypt / Turkey / Pakistan",
        "KB-BRT-095": "UAE Sulphur",
        "KB-BRT-096": "Alt Suppliers",
        "KB-BRT-097": "H2SO4 Stockpiling",
        "KB-BRT-098": "Kuwait Al-Zour",
        "KB-BRT-099": "SX-EW Mines",
        "KB-BRT-100": "Taiwan Nuclear",
        "KB-BRT-101": "Taiwan Grid",
        "KB-BRT-102": "TSMC Fab 18",
    }
    return entity_map.get(row_id, "")


def extract_status(fact, notes, source):
    """Infer status from content."""
    combined = (fact + " " + notes + " " + source).upper()
    
    if "UNVERIFIED" in combined or "X POST" in source.upper():
        # Check if it was later sourced/confirmed
        if "SOURCED" in combined or "CONFIRMED" in combined:
            if "CONFIRMED" in combined:
                return "CONFIRMED"
            return "ACTIVE"
        return "UNVERIFIED"
    if "CONFIRMED" in combined or "[CONF]" in combined:
        return "CONFIRMED"
    if "CORRECTION" in combined or "CORRECTED" in combined:
        return "CORRECTED"
    if "OBSOLETE" in combined:
        return "OBSOLETE"
    if "STALE" in combined:
        return "STALE"
    return "ACTIVE"


def extract_vectors(notes):
    """Pull out prediction refs (BRT-XX) and cross-agent links from notes."""
    vectors = []
    
    # Find BRT prediction references
    brt_refs = re.findall(r'BRT-\d+', notes)
    vectors.extend(brt_refs)
    
    # Find VX references
    vx_refs = re.findall(r'VX-BRT-\d+', notes)
    vectors.extend(vx_refs)
    
    # Find cross-agent references
    cross_agents = re.findall(r'Cross-agent:\s*(\w+)', notes)
    for agent in cross_agents:
        vectors.append(f"→{agent}")
    
    # Find vector references like "Phase 2" 
    if "Phase 2" in notes or "Phase 2" in notes:
        if "BRT-15" not in vectors:
            pass  # Don't add generic phase refs
    
    # Deduplicate while preserving order
    seen = set()
    unique = []
    for v in vectors:
        if v not in seen:
            seen.add(v)
            unique.append(v)
    
    return ", ".join(unique) if unique else ""


def clean_notes(notes, vectors_extracted):
    """Remove vector references that were extracted, keep the rest."""
    cleaned = notes
    # Remove "Cross-agent: X owns Y impact" phrases since agent is in Vectors
    cleaned = re.sub(r'Cross-agent:\s*\w+\s*(owns\s+)?[^.;]*[.;]?\s*', '', cleaned)
    # Don't strip BRT/VX refs from notes — they provide context alongside the extracted vectors
    return cleaned.strip()


def main():
    with open(INPUT, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        rows = list(reader)
    
    print(f"Read {len(rows)} rows from {INPUT}")
    
    new_rows = []
    unmapped_groups = set()
    
    for row in rows:
        row_id = row['ID'].strip()
        date = row['DATE'].strip()
        topic = row['TOPIC'].strip()
        fact = row['FACT'].strip()
        source = row['SOURCE'].strip()
        notes = row['NOTES'].strip() if row.get('NOTES') else ""
        
        # Group
        group = GROUP_MAP.get(topic)
        if not group:
            unmapped_groups.add(topic)
            # Fallback: uppercase + underscore
            group = topic.upper().replace(" ", "_").replace("/", "_").replace("—", "").replace("–", "").strip("_")
        
        # Entity
        entity = extract_entity(row_id, topic, fact, notes)
        
        # Status
        status = extract_status(fact, notes, source)
        
        # Vectors
        vectors = extract_vectors(notes)
        
        # Clean notes
        cleaned_notes = clean_notes(notes, vectors)
        
        new_rows.append({
            'ID': row_id,
            'Date': date,
            'Group': group,
            'Entity': entity,
            'Fact': fact,
            'Source': source,
            'Status': status,
            'Vectors': vectors,
            'Notes': cleaned_notes,
        })
    
    if unmapped_groups:
        print(f"WARNING: Unmapped topics (used fallback): {unmapped_groups}")
    
    # Write output
    fieldnames = ['ID', 'Date', 'Group', 'Entity', 'Fact', 'Source', 'Status', 'Vectors', 'Notes']
    with open(OUTPUT, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        writer.writerows(new_rows)
    
    print(f"Wrote {len(new_rows)} rows to {OUTPUT}")
    
    # Print spot checks
    print("\n=== SPOT CHECK: First 3 rows ===")
    for r in new_rows[:3]:
        print(f"\n{r['ID']} | {r['Group']} | {r['Entity']} | Status={r['Status']}")
        print(f"  Fact: {r['Fact'][:100]}...")
        print(f"  Vectors: {r['Vectors']}")
        print(f"  Notes: {r['Notes'][:100]}...")
    
    print("\n=== SPOT CHECK: Last 3 rows ===")
    for r in new_rows[-3:]:
        print(f"\n{r['ID']} | {r['Group']} | {r['Entity']} | Status={r['Status']}")
        print(f"  Fact: {r['Fact'][:100]}...")
        print(f"  Vectors: {r['Vectors']}")
        print(f"  Notes: {r['Notes'][:100]}...")
    
    # Print middle sample
    mid = len(new_rows) // 2
    print(f"\n=== SPOT CHECK: Middle rows ({mid-1} to {mid+1}) ===")
    for r in new_rows[mid-1:mid+2]:
        print(f"\n{r['ID']} | {r['Group']} | {r['Entity']} | Status={r['Status']}")
        print(f"  Fact: {r['Fact'][:100]}...")
        print(f"  Vectors: {r['Vectors']}")
        print(f"  Notes: {r['Notes'][:100]}...")
    
    # Status distribution
    from collections import Counter
    status_counts = Counter(r['Status'] for r in new_rows)
    print(f"\n=== STATUS DISTRIBUTION ===")
    for s, c in status_counts.most_common():
        print(f"  {s}: {c}")
    
    # Group distribution
    group_counts = Counter(r['Group'] for r in new_rows)
    print(f"\n=== GROUP DISTRIBUTION ===")
    for g, c in sorted(group_counts.items()):
        print(f"  {g}: {c}")


if __name__ == "__main__":
    main()
