#!/usr/bin/env python3
"""
HENRY Status Refresh Script
Updates STATUS.md header and Market Data table from MARKET_DATA.tsv

Usage:
  python3 scripts/refresh_status.py              # update STATUS.md
  python3 scripts/refresh_status.py --dry-run    # preview changes
"""

import re
import sys
from datetime import datetime
from pathlib import Path

HENRY_DIR = Path(__file__).resolve().parent.parent
STATUS_MD = HENRY_DIR / "STATUS.md"
DATA_TSV = HENRY_DIR / "workbook" / "MARKET_DATA.tsv"


def get_latest_data():
    """Read the latest row from MARKET_DATA.tsv."""
    if not DATA_TSV.exists():
        print(f"Error: {DATA_TSV} not found", file=sys.stderr)
        return None
    
    lines = DATA_TSV.read_text().strip().split("\n")
    if len(lines) < 2:
        print("Error: No data rows found", file=sys.stderr)
        return None
    
    headers = lines[0].split("\t")
    latest = lines[-1].split("\t")
    
    return dict(zip(headers, latest))


def format_header(data):
    """Format the header line for STATUS.md."""
    vix = data.get("VIX", "?")
    brent = data.get("Brent", "?")
    hy = data.get("HY_OAS", "?")
    
    # Truncate decimals for clean header
    try:
        vix = f"{float(vix):.2f}"
    except:
        pass
    try:
        brent = f"{float(brent):.2f}"
    except:
        pass
    try:
        hy = f"{float(hy):.0f}"
    except:
        pass
    
    return f"**Signal Status:** 🟡 COMPLACENCY TRAP — **VIX {vix}, Brent ${brent}, HY OAS {hy}** | CPI 3.3% YoY locks Fed | **Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M ET')}"


def update_market_data_table(content, data):
    """Update the Market Data table in STATUS.md."""
    # Update the date in the header
    today = datetime.now().strftime("%b %d, %Y")
    content = re.sub(r"(## MARKET DATA — )[^\n]*", r"\1" + today, content)
    
    # Find the Market Data section
    pattern = r"(## MARKET DATA.*\n\n\| Metric \| Value \| Δ vs Prior \| Source \| Status \|\n\|--------\|-------\|------------\|--------\|--------\|)\n((?:\|.*\|\n)+)"
    
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        print("Warning: Could not find Market Data table", file=sys.stderr)
        return content
    
    # Determine status emojis based on values
    try:
        brent_val = float(data.get('Brent', 0))
        brent_emoji = '🔴' if brent_val > 100 else '🟡' if brent_val > 85 else '🟢'
    except:
        brent_emoji = '🟡'
    
    try:
        gas_val = float(data.get('Gas', 0))
        gas_emoji = '🔴' if gas_val > 4.0 else '🟡' if gas_val > 3.5 else '🟢'
    except:
        gas_emoji = '🟡'
    
    try:
        hy_val = float(data.get('HY_OAS', 0))
        hy_emoji = '🔴' if hy_val > 320 else '🟡' if hy_val > 300 else '🟢'
    except:
        hy_emoji = '🟡'
    
    try:
        ccc_val = float(data.get('CCC_OAS', 0))
        ccc_emoji = '🔴' if ccc_val > 1000 else '🟡' if ccc_val > 900 else '🟢'
    except:
        ccc_emoji = '🟡'
    
    try:
        apo_val = float(data.get('APO', 0))
        apo_emoji = '🔴' if apo_val < 110 else '🟡'
    except:
        apo_emoji = '🟡'
    
    # Build new table rows
    rows = [
        "| SPX | ~5,400* | — | Live | 🟡 |",
        f"| VIX | **{data.get('VIX', '?')}** | — | Live | 🟡 Compressed |",
        f"| Brent | **${data.get('Brent', '?')}** | — | Live | {brent_emoji} |",
        f"| Gas (AAA) | **${data.get('Gas', '?')}** | — | Live | {gas_emoji} |",
        f"| 10Y Yield | {data.get('10Y_Yield', '?')}% | — | Live | 🟡 |",
        f"| USD/JPY | **{data.get('USDJPY', '?')}** | — | Live | 🔴 |",
        f"| HY OAS | **{data.get('HY_OAS', '?')}bps** | — | FRED | {hy_emoji} |",
        f"| CCC OAS | **{data.get('CCC_OAS', '?')}bps** | — | FRED | {ccc_emoji} |",
        f"| KRE | ${data.get('KRE', '?')} | — | Live | 🟡 |",
        f"| APO | ${data.get('APO', '?')} | — | Live | {apo_emoji} |",
    ]
    
    new_table = match.group(1) + "\n" + "\n".join(rows) + "\n"
    
    return content[:match.start()] + new_table + content[match.end():]


def update_header(content, data):
    """Update the header line in STATUS.md."""
    new_header = format_header(data)
    
    # Replace the first line (Signal Status line)
    pattern = r"^\*\*Signal Status:\*\*.*$"
    return re.sub(pattern, new_header, content, count=1, flags=re.MULTILINE)


def main():
    dry_run = "--dry-run" in sys.argv
    
    # Read latest data
    data = get_latest_data()
    if not data:
        sys.exit(1)
    
    # Read current STATUS.md
    if not STATUS_MD.exists():
        print(f"Error: {STATUS_MD} not found", file=sys.stderr)
        sys.exit(1)
    
    content = STATUS_MD.read_text()
    
    # Update content
    content = update_header(content, data)
    content = update_market_data_table(content, data)
    
    if dry_run:
        print("=== DRY RUN ===")
        print("New header:")
        print(format_header(data))
        print("\nFirst 50 lines of updated file:")
        print("\n".join(content.split("\n")[:50]))
    else:
        # Write back
        STATUS_MD.write_text(content)
        print(f"Updated {STATUS_MD}")
        print(f"New header: {format_header(data)}")


if __name__ == "__main__":
    main()
