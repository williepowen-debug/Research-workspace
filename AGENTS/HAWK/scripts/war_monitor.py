#!/usr/bin/env python3
"""
HAWK War Monitor — Daily War Developments & Scenario Tracker

Performs web search for latest Iran war news and outputs signal summary
with scenario probability shifts (D/B/C framework).

Usage:
  .venv/bin/python3 AGENTS/HAWK/scripts/war_monitor.py
  .venv/bin/python3 AGENTS/HAWK/scripts/war_monitor.py --save    # write to workbook
"""

import sys
import subprocess
import argparse
from datetime import datetime
from pathlib import Path

HAWK_DIR = Path(__file__).resolve().parent.parent
WORKBOOK = HAWK_DIR / "workbook"
WORKBOOK.mkdir(exist_ok=True)

# Current scenario baseline
SCENARIO_BASELINE = {"D": 82, "C": 12, "B": 6}
CEASEFIRE_START = datetime(2026, 4, 12).date()


def run_web_search(query, limit=5):
    """Run web_search using Google News RSS feeds.
    
    Returns search results or empty string on error.
    Handles API errors gracefully with timeout protection.
    """
    try:
        import urllib.request
        import urllib.parse
        import ssl
        import re
        from xml.etree import ElementTree as ET
        
        # Use Google News RSS feed
        encoded_query = urllib.parse.quote(query)
        url = f"https://news.google.com/rss/search?q={encoded_query}&hl=en-US&gl=US&ceid=US:en"
        
        ctx = ssl.create_default_context()
        req = urllib.request.Request(
            url,
            headers={
                'User-Agent': 'Mozilla/5.0 (compatible; HAWK/1.0; +research)'
            }
        )
        
        with urllib.request.urlopen(req, timeout=10, context=ctx) as response:
            xml_data = response.read().decode('utf-8', errors='ignore')
            
            # Parse RSS XML
            root = ET.fromstring(xml_data)
            
            # Find all items
            items = root.findall('.//item')
            
            results = []
            for item in items[:limit]:
                title = item.find('title')
                description = item.find('description')
                pub_date = item.find('pubDate')
                
                title_text = title.text if title is not None else ""
                desc_text = description.text if description is not None else ""
                
                # Clean HTML from description
                if desc_text:
                    desc_text = re.sub(r'<[^>]+>', ' ', desc_text)
                    desc_text = re.sub(r'\s+', ' ', desc_text).strip()
                
                if title_text:
                    results.append(f"{title_text}: {desc_text[:150]}" if desc_text else title_text)
            
            if results:
                return f"Search: {query}\n" + "\n".join(f"- {r}" for r in results)
            
            return ""
    except urllib.error.URLError:
        return ""
    except Exception:
        return ""


def fetch_rss_feed(url, limit=5):
    """Fetch and parse an RSS feed directly."""
    try:
        import urllib.request
        import ssl
        import re
        from xml.etree import ElementTree as ET
        
        ctx = ssl.create_default_context()
        req = urllib.request.Request(
            url,
            headers={
                'User-Agent': 'Mozilla/5.0 (compatible; HAWK/1.0; +research)'
            }
        )
        
        with urllib.request.urlopen(req, timeout=10, context=ctx) as response:
            xml_data = response.read().decode('utf-8', errors='ignore')
            
            # Parse RSS XML
            root = ET.fromstring(xml_data)
            
            # Find all items
            items = root.findall('.//item')
            
            results = []
            for item in items[:limit]:
                title = item.find('title')
                description = item.find('description')
                
                title_text = title.text if title is not None else ""
                desc_text = description.text if description is not None else ""
                
                # Clean HTML from description
                if desc_text:
                    desc_text = re.sub(r'<[^>]+>', ' ', desc_text)
                    desc_text = re.sub(r'\s+', ' ', desc_text).strip()
                
                if title_text:
                    results.append(f"{title_text}: {desc_text[:150]}" if desc_text else title_text)
            
            return results
    except Exception:
        return []


def search_war_news():
    """Search for latest war developments using multiple sources."""
    results = []
    
    # Try Google News RSS for key queries
    queries = [
        "Israel Iran war",
        "Houthi Red Sea",
        "Hormuz Strait"
    ]
    
    for query in queries:
        output = run_web_search(query)
        if output:
            results.append((query, output))
    
    # Also try direct RSS feeds
    rss_feeds = [
        ("BBC World", "http://feeds.bbci.co.uk/news/world/rss.xml"),
        ("Reuters", "http://feeds.reuters.com/reuters/worldnews"),
    ]
    
    for name, url in rss_feeds:
        feed_results = fetch_rss_feed(url, limit=3)
        if feed_results:
            # Filter for relevant keywords
            relevant = []
            keywords = ['iran', 'israel', 'gaza', 'houthi', 'yemen', 'red sea', 'hormuz', 'missile', 'strike']
            for item in feed_results:
                item_lower = item.lower()
                if any(kw in item_lower for kw in keywords):
                    relevant.append(item)
            if relevant:
                results.append((name, "\n".join(f"- {r}" for r in relevant)))
    
    return results


def analyze_signals(news_results):
    """Analyze news for scenario signals."""
    signals = []
    
    # Combine all text for analysis
    all_text = " ".join([r[1] for r in news_results]).lower()
    
    # Escalation signals (increase D)
    escalation_keywords = [
        "strike", "attack", "missile", "drone", "explosion", "damage",
        "casualties", "killed", "destroyed", "retaliation", "escalation"
    ]
    
    # De-escalation signals (increase B)
    deescalation_keywords = [
        "ceasefire", "talks", "negotiation", "agreement", "deal",
        "diplomatic", "mediation", "prisoner exchange", "progress"
    ]
    
    # Stability signals (neutral/ongoing)
    stability_keywords = [
        "holding", "stable", "quiet", "no incidents", "stand-down",
        "compliance", "monitoring"
    ]
    
    escalation_count = sum(1 for k in escalation_keywords if k in all_text)
    deescalation_count = sum(1 for k in deescalation_keywords if k in all_text)
    stability_count = sum(1 for k in stability_keywords if k in all_text)
    
    # Generate signals
    if escalation_count > 2:
        signals.append({
            "type": "🔴",
            "signal": "Escalation indicators detected",
            "impact": "D +5-10%",
            "details": f"Keywords: {escalation_count} escalation mentions"
        })
    
    if deescalation_count > 2:
        signals.append({
            "type": "🟢",
            "signal": "Diplomatic progress indicators",
            "impact": "B +5%",
            "details": f"Keywords: {deescalation_count} de-escalation mentions"
        })
    
    if stability_count > 1 or (escalation_count == 0 and deescalation_count < 2):
        signals.append({
            "type": "🟡",
            "signal": "Ceasefire holding, no major incidents",
            "impact": "D unchanged",
            "details": "Status quo maintained"
        })
    
    return signals


def calculate_scenario_shift(signals):
    """Calculate scenario probability shifts based on signals."""
    new_scenario = SCENARIO_BASELINE.copy()
    
    for sig in signals:
        if "D +" in sig["impact"]:
            # Extract number
            try:
                shift = int(sig["impact"].split("+")[1].split("%")[0])
                new_scenario["D"] = min(95, new_scenario["D"] + shift)
                new_scenario["C"] = max(0, new_scenario["C"] - shift // 2)
                new_scenario["B"] = max(0, new_scenario["B"] - shift // 2)
            except:
                pass
        elif "B +" in sig["impact"]:
            try:
                shift = int(sig["impact"].split("+")[1].split("%")[0])
                new_scenario["B"] = min(20, new_scenario["B"] + shift)
                new_scenario["D"] = max(60, new_scenario["D"] - shift)
            except:
                pass
    
    return new_scenario


def save_war_log(signals, scenario):
    """Log to WAR_LOG.md."""
    log_path = WORKBOOK / "WAR_LOG.md"
    today = datetime.now().strftime("%Y-%m-%d")
    
    with open(log_path, "a") as f:
        f.write(f"\n## {today}\n\n")
        f.write(f"**Scenario:** D {scenario['D']}% / C {scenario['C']}% / B {scenario['B']}%\n\n")
        f.write("**Signals:**\n")
        for sig in signals:
            f.write(f"- {sig['type']} {sig['signal']}\n")
        f.write("\n")


def save_scenario_history(scenario):
    """Log to SCENARIO_HISTORY.tsv."""
    tsv_path = WORKBOOK / "SCENARIO_HISTORY.tsv"
    today = datetime.now().strftime("%Y-%m-%d")
    
    if not tsv_path.exists():
        with open(tsv_path, "w") as f:
            f.write("date\tD_pct\tC_pct\tB_pct\ttrigger_event\n")
    
    with open(tsv_path, "a") as f:
        f.write(f"{today}\t{scenario['D']}\t{scenario['C']}\t{scenario['B']}\tauto_scan\n")


def main():
    parser = argparse.ArgumentParser(description="HAWK war monitor")
    parser.add_argument("--save", action="store_true", help="Save to workbook")
    args = parser.parse_args()
    
    today = datetime.now()
    today_date = today.date()
    now = today.strftime("%Y-%m-%d %H:%M ET")
    
    # Calculate war day and ceasefire day
    war_start = datetime(2026, 3, 1).date()  # Approximate war start
    war_day = (today_date - war_start).days
    ceasefire_day = (today_date - CEASEFIRE_START).days if today_date >= CEASEFIRE_START else 0
    
    print(f"\n{'='*70}")
    print(f"  HAWK War Monitor — {now}")
    print(f"{'='*70}")
    
    print(f"\n  War Day: {war_day} | Ceasefire Day: {ceasefire_day} (Apr 12-13)")
    print(f"  Baseline Scenario: D {SCENARIO_BASELINE['D']}% / C {SCENARIO_BASELINE['C']}% / B {SCENARIO_BASELINE['B']}%")
    
    # Search for news
    print(f"\n  🔍 Scanning for developments...")
    news_results = search_war_news()
    
    if not news_results:
        print("  ⚠️  No search results available (network or API issue)")
        signals = [{
            "type": "⚠️",
            "signal": "Search unavailable — manual review required",
            "impact": "No change",
            "details": "Network or API error"
        }]
    else:
        signals = analyze_signals(news_results)
    
    # Calculate new scenario
    new_scenario = calculate_scenario_shift(signals)
    
    # Output signals
    print(f"\n  SIGNAL SUMMARY (last 24h)")
    print(f"  {'-'*60}")
    
    if signals:
        for sig in signals:
            print(f"  {sig['type']} {sig['signal']}")
            print(f"     Impact: {sig['impact']}")
            if sig.get('details'):
                print(f"     Details: {sig['details']}")
    else:
        print("  🟡 No significant developments reported")
    
    # Scenario shifts
    print(f"\n  SCENARIO PROBABILITY SHIFTS")
    print(f"  {'-'*60}")
    
    for scenario in ["D", "C", "B"]:
        old = SCENARIO_BASELINE[scenario]
        new = new_scenario[scenario]
        delta = new - old
        
        if delta > 0:
            change = f"↑ +{delta}%"
        elif delta < 0:
            change = f"↓ {delta}%"
        else:
            change = "→ unchanged"
        
        emoji = "🔴" if scenario == "D" else "🟡" if scenario == "C" else "🟢"
        print(f"  {emoji} {scenario}: {old}% → {new}% ({change})")
    
    # Interpretation
    print(f"\n  INTERPRETATION")
    print(f"  {'-'*60}")
    
    if new_scenario["D"] > SCENARIO_BASELINE["D"]:
        print("  🔴 Escalation risk elevated — monitor for kinetic incidents")
    elif new_scenario["B"] > SCENARIO_BASELINE["B"]:
        print("  🟢 De-escalation momentum — watch for deal framework")
    else:
        print("  🟡 Status quo holding — ceasefire fragile but intact")
    
    # Alerts
    print(f"\n  ALERTS")
    print(f"  {'-'*60}")
    
    alerts = []
    if any(s["type"] == "🔴" for s in signals):
        alerts.append("🔴 Kinetic incident reported — immediate reassessment required")
    if ceasefire_day >= 25:
        alerts.append(f"🟡 May 12 checkpoint approaching ({30-ceasefire_day} days)")
    
    if alerts:
        for alert in alerts:
            print(f"  {alert}")
    else:
        print("  ✅ No active alerts")
    
    # Save if requested
    if args.save:
        save_war_log(signals, new_scenario)
        save_scenario_history(new_scenario)
        print(f"\n  💾 Logged to workbook/WAR_LOG.md and SCENARIO_HISTORY.tsv")
    
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
