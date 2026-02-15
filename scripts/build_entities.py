#!/usr/bin/env python3
"""
Build ENTITIES.md — Cross-Agent Entity Index

Scans all agent workbooks and identifies which entities are tracked where.
Helps identify cross-agent transmission paths.

Usage: python3 scripts/build_entities.py
"""

import csv
from pathlib import Path
from collections import defaultdict
from datetime import datetime

WORKSPACE = Path(__file__).parent.parent

# Define key entities to track
ENTITIES = {
    'Carvana': ['carvana', 'bridgecrest', 'drivetime', 'garcia', 'cvna'],
    'Ally': ['ally financial', 'ally bank', 'ally '],
    'Tricolor': ['tricolor', 'daniel chu', 'goodgame'],
    'FirstBrands': ['first brands', 'james brothers', 'patrick james', 'de luca'],
    'PrimaLend': ['primalend', 'jensen'],
    'Exeter': ['exeter finance', 'exeter '],
    'Westlake': ['westlake'],
    'CPS': ['consumer portfolio services', 'cpss', ' cps '],
    'Lendbuzz': ['lendbuzz', 'lbzz'],
    'SAFCO': ['safco'],
    'Japan': ['japan', 'boj', 'jgb', 'shunto', 'takaichi', 'yen', 'jpy'],
    'China': ['china', 'pboc', 'belgium', 'lgfv', 'vanke', 'evergrande'],
    'Florida': ['florida', ' fl ', 'condo', 'citizens insurance', 'palm beach', 'miami'],
    'Texas': ['texas', ' tx ', 'laredo', 'mcallen', 'border'],
    'KRE': ['kre', 'regional bank'],
    'SSB': ['ssb', 'southstate'],
    'VIX': ['vix', 'volatility'],
    'HYG': ['hyg', 'high yield'],
}

# Agent workbook paths
AGENT_PATHS = {
    'OTTO': 'AGENTS/OTTO/workbook',
    'CARL': 'AGENTS/CARL/workbook',
    'LABOR': 'AGENTS/LABOR/workbook',
    'HENRY': 'AGENTS/HENRY/workbook',
    'SAM': 'AGENTS/SAM/workbook',
    'LIQUID': 'AGENTS/LIQUID/workbook',
    'MARCO': 'AGENTS/MARCO/workbook',
    'REGINALD': 'AGENTS/REGINALD/workbook',
    'BROCK': 'AGENTS/REGINALD/sub-agents/BROCK/workbook',
    'CORAL': 'AGENTS/REGINALD/sub-agents/CORAL/workbook',
    'CREED': 'AGENTS/REGINALD/sub-agents/CREED/workbook',
    'TEX': 'AGENTS/REGINALD/sub-agents/TEX/workbook',
    'ZHAO': 'AGENTS/ZHAO/workbook',
    'HANS': 'AGENTS/HANS/workbook',
}

def scan_workbook(filepath, entity_keywords):
    """Scan a workbook for entity mentions, return matching entry IDs."""
    matches = []
    if not filepath.exists():
        return matches
    
    try:
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f, delimiter='\t')
            for row in reader:
                text = ' '.join(str(v).lower() for v in row.values())
                for keyword in entity_keywords:
                    if keyword.lower() in text:
                        entry_id = row.get('ID', row.get('Vector_ID', '?'))
                        matches.append(entry_id)
                        break
    except Exception as e:
        pass
    
    return matches

def main():
    # Build entity index
    entity_index = defaultdict(lambda: defaultdict(list))

    for agent, path in AGENT_PATHS.items():
        agent_dir = WORKSPACE / path
        if not agent_dir.exists():
            continue
        
        for workbook in ['VX.tsv', 'ML.tsv', 'FL.tsv', 'FLOW.tsv']:
            filepath = agent_dir / workbook
            if not filepath.exists():
                continue
            
            for entity, keywords in ENTITIES.items():
                matches = scan_workbook(filepath, keywords)
                if matches:
                    entity_index[entity][agent].extend([(workbook, m) for m in matches])

    # Generate ENTITIES.md
    today = datetime.now().strftime('%Y-%m-%d')
    output = f"""# ENTITIES.md — Cross-Agent Entity Index

*Auto-generated cross-reference. Which agents track which entities.*

**Last Updated:** {today}
**Entities Tracked:** {len([e for e in ENTITIES if e in entity_index])}

---

"""

    for entity in sorted(ENTITIES.keys()):
        if entity not in entity_index:
            continue
        
        agents = entity_index[entity]
        total_refs = sum(len(refs) for refs in agents.values())
        
        output += f"## {entity}\n\n"
        output += f"**Total References:** {total_refs} across {len(agents)} agents\n\n"
        
        for agent in sorted(agents.keys()):
            refs = agents[agent]
            # Group by workbook
            by_wb = defaultdict(list)
            for wb, ref_id in refs:
                by_wb[wb].append(ref_id)
            
            ref_strs = []
            for wb, ids in sorted(by_wb.items()):
                if len(ids) <= 3:
                    ref_strs.append(f"{wb}: {', '.join(ids)}")
                else:
                    ref_strs.append(f"{wb}: {len(ids)} entries")
            
            output += f"- **{agent}:** {'; '.join(ref_strs)}\n"
        
        output += "\n---\n\n"

    output += """## Usage

**Find all Carvana references:**
```bash
grep -ri "carvana" AGENTS/*/workbook/*.tsv
```

**Find cross-agent connections:**
Look for entities that appear in multiple agents — these are transmission paths.

**Key Cross-Agent Entities:**
- **Carvana** → OTTO (fraud) + CARL (consumer) + REGINALD (Ally exposure)
- **Japan** → SAM (macro) + LIQUID (UST) + HENRY (vol)
- **Florida** → CORAL (insurance) + CREED (CRE) + CARL (consumer)
- **Ally** → OTTO (Carvana exposure) + REGINALD (bank stress)

---

*Regenerate with: `python3 scripts/build_entities.py`*
"""

    # Write file
    with open(WORKSPACE / 'ENTITIES.md', 'w') as f:
        f.write(output)

    print(f"Generated ENTITIES.md with {len(entity_index)} entities")
    for entity, agents in sorted(entity_index.items(), key=lambda x: -sum(len(v) for v in x[1].values()))[:10]:
        total = sum(len(v) for v in agents.values())
        print(f"  {entity}: {total} refs across {len(agents)} agents")

if __name__ == '__main__':
    main()
