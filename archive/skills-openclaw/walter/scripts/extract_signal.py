#!/usr/bin/env python3
"""
Signal extraction helper for signal-router agent.
Parses various input formats and extracts structured signal data.
"""

import sys
import json
import re
from datetime import datetime
from pathlib import Path

def extract_from_text(text: str) -> dict:
    """Extract signal data from text article."""
    signal = {
        "source": None,
        "date": None,
        "headline": None,
        "key_data": [],
        "quotes": [],
        "tickers": [],
        "thesis_relevance": []
    }
    
    # Extract tickers (uppercase 2-5 letters in parentheses or after $)
    ticker_pattern = r'\b([A-Z]{2,5})\b|\$([A-Z]{2,5})'
    matches = re.findall(ticker_pattern, text)
    signal["tickers"] = list(set([m[0] or m[1] for m in matches]))
    
    # Extract percentages and basis points
    pct_pattern = r'(\d+\.?\d*)\s*(bps?|basis points?|%)'
    for match in re.finditer(pct_pattern, text, re.IGNORECASE):
        signal["key_data"].append(f"{match.group(1)}{match.group(2)}")
    
    # Extract dollar amounts with context
    dollar_pattern = r'\$([\d,]+\.?\d*)\s*(million|billion|trillion)?'
    for match in re.finditer(dollar_pattern, text, re.IGNORECASE):
        amt = match.group(1)
        unit = match.group(2) or ""
        signal["key_data"].append(f"${amt} {unit}".strip())
    
    # Look for thesis keywords
    thesis_keywords = {
        "private credit": "PC stress",
        "BDC": "PC stress",
        "CLO": "PC stress",
        "gate": "PC stress",
        "redemption": "PC stress",
        "regional bank": "Bank stress",
        "CRE": "CRE stress",
        "refinancing": "CRE stress",
        "mortgage": "Housing",
        "home price": "Housing",
        "Brent": "Energy",
        "WTI": "Energy",
        "Hormuz": "Geopolitical",
        "JPY": "Japan",
        "BOJ": "Japan",
        "China": "Capital flows",
        "TIC": "Capital flows",
        "claims": "Labor",
        "NFP": "Labor",
        "unemployment": "Labor"
    }
    
    text_lower = text.lower()
    for keyword, theme in thesis_keywords.items():
        if keyword.lower() in text_lower:
            signal["thesis_relevance"].append(theme)
    
    signal["thesis_relevance"] = list(set(signal["thesis_relevance"]))
    
    return signal

def classify_priority(signal: dict) -> str:
    """Classify signal priority based on content."""
    text = json.dumps(signal).lower()
    
    # Critical thresholds
    critical_patterns = [
        r'hy oas.*>\s*320',
        r'ccc oas.*>\s*1000',
        r'brent.*>\s*100',
        r'gate.*\d+%',
        r'insolvent',
        r'failure',
        r'collapse',
        r'war.*escalat',
        r'ceasefire.*rejected'
    ]
    
    for pattern in critical_patterns:
        if re.search(pattern, text):
            return "🔴"
    
    # Important patterns
    important_patterns = [
        r'earnings',
        r'q[1-4].*202[56]',
        r'claims.*\d+k',
        r'nfp.*\d+k',
        r'default',
        r'delinquenc',
        r'allowance',
        r'reserve'
    ]
    
    for pattern in important_patterns:
        if re.search(pattern, text):
            return "🟡"
    
    return "🟢"

def suggest_agents(signal: dict) -> list:
    """Suggest which agents should receive this signal."""
    agents = set()
    themes = signal.get("thesis_relevance", [])
    
    theme_agents = {
        "PC stress": ["BROCK", "SHADE", "LIQUID"],
        "Bank stress": ["REGINALD", "LIQUID"],
        "CRE stress": ["REGINALD", "BROCK", "LIQUID"],
        "Housing": ["CARL"],
        "Energy": ["BRENT", "HAWK", "HENRY"],
        "Geopolitical": ["HAWK", "BRENT"],
        "Japan": ["SAM", "LIQUID"],
        "Capital flows": ["ZHAO", "LIQUID"],
        "Labor": ["LABOR", "HENRY"]
    }
    
    for theme in themes:
        if theme in theme_agents:
            agents.update(theme_agents[theme])
    
    return sorted(list(agents))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: extract_signal.py <text_file>")
        sys.exit(1)
    
    text_file = Path(sys.argv[1])
    if not text_file.exists():
        print(f"Error: File not found: {text_file}")
        sys.exit(1)
    
    text = text_file.read_text()
    signal = extract_from_text(text)
    signal["priority"] = classify_priority(signal)
    signal["suggested_agents"] = suggest_agents(signal)
    
    print(json.dumps(signal, indent=2))
