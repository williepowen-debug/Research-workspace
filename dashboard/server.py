#!/usr/bin/env python3
"""
PROME Dashboard Server — v2 (Segment 1 rebuild)
All content parsed dynamically from workspace files. Zero hardcoded data.
"""

import http.server
import socketserver
import json
import os
import re
import urllib.request
import time
from urllib.parse import urlparse, parse_qs

PORT = 8080
WORKSPACE = "/home/moltbot/.openclaw/workspace"

# Import config.py from market-data tools
import sys as _sys
_sys.path.insert(0, os.path.join(WORKSPACE, "FORGE/tools/market-data"))
from config import SERIES as STRESS_SERIES, classify as stress_classify, get_emoji as stress_emoji, format_value as stress_format
ALERTS_FILE = os.path.join(WORKSPACE, "dashboard", "alerts.json")
SUBAGENT_LOG_FILE = os.path.join(WORKSPACE, "dashboard", "subagent_log.json")
FRED_API_KEY = "8ce3f08db56f151f54221a0dd12b63de"
BLS_API_KEY = "28cc34af39834eb2a4d85d3119f72077"

TELEGRAM_BOT_TOKEN = "***REMOVED***:***REMOVED***"
TELEGRAM_CHAT_ID = "8463631023"

# ============================================================
# CACHING INFRASTRUCTURE
# ============================================================

def make_cache(ttl=300):
    return {"data": None, "timestamp": 0, "ttl": ttl}

price_cache = make_cache(300)       # 5 min
fred_cache = make_cache(3600)       # 1 hr
bls_cache = make_cache(3600)        # 1 hr
treasury_cache = make_cache(86400)  # 24 hr
sec_cache = make_cache(1800)        # 30 min
status_cache = make_cache(30)       # 30 sec — workspace files change often
agent_cache = {}                    # per-agent, 30 sec each

def cache_fresh(cache):
    return cache["data"] is not None and (time.time() - cache["timestamp"]) < cache["ttl"]

def cache_set(cache, data):
    cache["data"] = data
    cache["timestamp"] = time.time()
    return data

# ============================================================
# ALERT SYSTEM (kept from v1)
# ============================================================

BREACH_STATE_FILE = os.path.join(WORKSPACE, "dashboard", "breach_state.json")
SEEN_FILINGS_FILE = os.path.join(WORKSPACE, "dashboard", "seen_filings.json")

def load_json_file(path, default=None):
    if default is None:
        default = {}
    if os.path.exists(path):
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except:
            pass
    return default

def save_json_file(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def load_alerts():
    return load_json_file(ALERTS_FILE, [])

def save_alerts(alerts):
    save_json_file(ALERTS_FILE, alerts[-100:])

def add_alert(alert_type, severity, message, value=None, threshold=None, notify=True):
    alerts = load_alerts()
    alert = {
        "id": int(time.time() * 1000),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
        "type": alert_type,
        "severity": severity,
        "message": message,
        "value": value,
        "threshold": threshold,
    }
    alerts.append(alert)
    save_alerts(alerts)
    if notify and severity in ["critical", "warning"]:
        send_telegram_alert(message, severity)
    return alert

def send_telegram_alert(message, severity="warning"):
    try:
        emoji = {"critical": "🚨", "warning": "⚠️", "info": "ℹ️"}.get(severity, "📊")
        payload = json.dumps({
            "chat_id": TELEGRAM_CHAT_ID,
            "text": f"{emoji} *PROME Alert*\n\n{message}",
            "parse_mode": "Markdown",
        }).encode()
        req = urllib.request.Request(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
            data=payload, headers={"Content-Type": "application/json"}, method="POST",
        )
        urllib.request.urlopen(req, timeout=10)
    except Exception as e:
        print(f"[Telegram] Failed: {e}")

# Subagent log (kept from v1)
def load_subagent_log():
    return load_json_file(SUBAGENT_LOG_FILE, [])

def save_subagent_log(log):
    save_json_file(SUBAGENT_LOG_FILE, log[-50:])

def add_subagent_entry(agent_id, task, status="running", result=None, session_key=None, runtime_sec=None):
    log = load_subagent_log()
    entry = {
        "id": session_key or f"{agent_id}_{int(time.time()*1000)}",
        "agent": agent_id, "task": task[:200], "status": status,
        "result": result[:500] if result else None,
        "runtime_sec": runtime_sec,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
        "session_key": session_key,
    }
    updated = False
    for i, ex in enumerate(log):
        if ex.get("session_key") == session_key and session_key:
            log[i] = entry
            updated = True
            break
    if not updated:
        log.append(entry)
    save_subagent_log(log)
    return entry

# ============================================================
# MARKDOWN TABLE PARSER
# ============================================================

def parse_md_table(text):
    """Parse a markdown table into list of dicts. Returns [] if no table found."""
    lines = [l.strip() for l in text.strip().split('\n') if l.strip()]
    if len(lines) < 2:
        return []
    # Find header row (first line with |)
    header_idx = None
    for i, line in enumerate(lines):
        if '|' in line and not all(c in '|-: ' for c in line):
            header_idx = i
            break
    if header_idx is None:
        return []
    headers = [h.strip() for h in lines[header_idx].split('|') if h.strip()]
    rows = []
    for line in lines[header_idx + 1:]:
        if all(c in '|-: ' for c in line):
            continue  # separator
        if '|' not in line:
            break  # end of table
        cells = [c.strip() for c in line.split('|')]
        # Remove empty first/last from leading/trailing |
        if cells and cells[0] == '':
            cells = cells[1:]
        if cells and cells[-1] == '':
            cells = cells[:-1]
        if len(cells) >= len(headers):
            rows.append(dict(zip(headers, cells[:len(headers)])))
        elif cells:
            # Pad with empty strings
            padded = cells + [''] * (len(headers) - len(cells))
            rows.append(dict(zip(headers, padded)))
    return rows

def extract_section(text, heading, next_heading_level=2):
    """Extract content between a heading and the next heading of same or higher level."""
    # Match ## Heading or ### Heading etc
    pattern = rf'^(#{{{next_heading_level}}})\s+{re.escape(heading)}\s*$'
    lines = text.split('\n')
    start = None
    for i, line in enumerate(lines):
        if re.match(pattern, line.strip(), re.IGNORECASE):
            start = i + 1
            break
    if start is None:
        # Try fuzzy match
        heading_lower = heading.lower()
        for i, line in enumerate(lines):
            stripped = line.strip().lstrip('#').strip()
            if heading_lower in stripped.lower():
                start = i + 1
                break
    if start is None:
        return None
    # Find end
    end = len(lines)
    for i in range(start, len(lines)):
        line = lines[i].strip()
        if line.startswith('#') and not line.startswith('###' + '#'):
            # Check if same or higher level heading
            level = len(line) - len(line.lstrip('#'))
            if level <= next_heading_level:
                end = i
                break
    return '\n'.join(lines[start:end])

# ============================================================
# STATUS.MD PARSERS
# ============================================================

def read_file(path):
    full = os.path.join(WORKSPACE, path) if not path.startswith('/') else path
    try:
        with open(full, 'r') as f:
            return f.read()
    except:
        return None

def parse_status():
    """Parse PROME/STATUS.md — cached."""
    if cache_fresh(status_cache):
        return status_cache["data"]
    
    text = read_file("PROME/STATUS.md")
    if not text:
        return cache_set(status_cache, {"error": "STATUS.md not found"})
    
    result = {
        "updated": None,
        "headline": None,
        "last_context": None,
        "agents": [],
        "positions": {},
        "convictions": [],
        "catalysts": [],
        "pending": [],
        "scenarios": [],
        "hamilton": None,
        "cross_agent": [],
        "taiwan_lng": [],
        "fertilizer": [],
        "exit_rules": [],
    }
    
    # Updated timestamp
    m = re.search(r'\*\*Updated:\*\*\s*(.+?)$', text, re.MULTILINE)
    if m:
        result["updated"] = m.group(1).strip()
    
    # Headline (the big red line)
    m = re.search(r'^##\s+(.+)$', text, re.MULTILINE)
    if m:
        result["headline"] = m.group(1).strip().replace('🔴', '🔴').strip()
    
    # Last context
    m = re.search(r'\*\*Last context:\*\*\s*(.+?)(?:\n\n|\n##)', text, re.DOTALL)
    if m:
        result["last_context"] = m.group(1).strip()
    
    # Agents table
    agents_section = extract_section(text, "Agents")
    if agents_section:
        result["agents"] = parse_md_table(agents_section)
    
    # Positions — parse the structured subsections
    pos_section = extract_section(text, "Positions")
    if pos_section:
        result["positions"] = parse_positions(pos_section)
    
    # Convictions table
    conv_section = extract_section(text, "Convictions")
    if conv_section:
        result["convictions"] = parse_md_table(conv_section)
    
    # Catalysts/dates table
    dates_section = extract_section(text, "Dates")
    if dates_section:
        result["catalysts"] = parse_md_table(dates_section)
    
    # Pending table
    pending_section = extract_section(text, "Pending")
    if pending_section:
        result["pending"] = parse_md_table(pending_section)
    
    # Scenarios table
    scenarios_section = extract_section(text, "Scenario C — Current Probabilities")
    if scenarios_section:
        result["scenarios"] = parse_md_table(scenarios_section)
    
    # Hamilton quick ref
    hamilton_section = extract_section(text, "Hamilton Quick Ref")
    if hamilton_section:
        result["hamilton"] = hamilton_section.strip()
    
    # Cross-agent matrix
    cross_section = extract_section(text, "Cross-Agent Matrix")
    if cross_section:
        result["cross_agent"] = parse_md_table(cross_section)
    
    # Taiwan LNG
    taiwan_section = extract_section(text, "Taiwan LNG Critical Path", 2)
    if taiwan_section:
        result["taiwan_lng"] = parse_md_table(taiwan_section)
        # Extract TSMC chain
        tsmc_match = re.search(r'```\n(Hormuz closure.*?)```', taiwan_section, re.DOTALL)
        if tsmc_match:
            result["tsmc_chain"] = tsmc_match.group(1).strip()
        # Escalation indicators
        esc_match = re.search(r'Escalation indicators.*?:\*\*\n(.*?)(?:\n\n|\n---|\Z)', taiwan_section, re.DOTALL)
        if esc_match:
            result["taiwan_escalation"] = [l.strip().lstrip('- ') for l in esc_match.group(1).strip().split('\n') if l.strip().startswith('-')]
    
    # Fertilizer
    fert_section = extract_section(text, "Fertilizer Shortage Calendar", 2)
    if fert_section:
        result["fertilizer"] = parse_md_table(fert_section)
        # Extract the feedback loop
        loop_match = re.search(r'```\n(Fertilizer shortage.*?)```', fert_section, re.DOTALL)
        if loop_match:
            result["fertilizer_loop"] = loop_match.group(1).strip()
        # Extract header stat
        header_match = re.search(r'\*\*(.+?urea.+?)\*\*', fert_section)
        if header_match:
            result["fertilizer_header"] = header_match.group(1)
    
    # Exit rules
    exit_section = extract_section(text, "Exit Rules", 2)
    if exit_section:
        result["exit_rules"] = parse_md_table(exit_section)
        # Current template
        tmpl = re.search(r'Current template:\s*(\w+)', exit_section)
        if tmpl:
            result["exit_template"] = tmpl.group(1)
        # Extract scenario A protocol
        proto_a = re.search(r'Scenario A exit protocol.*?:\*\*\n(.*?)(?=\n\*\*Scenario C|\n\n---|\Z)', exit_section, re.DOTALL)
        if proto_a:
            result["exit_protocol_a"] = [l.strip().lstrip('- ') for l in proto_a.group(1).strip().split('\n') if l.strip().startswith('-')]
        proto_c = re.search(r'Scenario C exit.*?:\*\*\n(.*?)(?:\n\n---|\n\n##|\Z)', exit_section, re.DOTALL)
        if proto_c:
            result["exit_protocol_c"] = [l.strip().lstrip('- ') for l in proto_c.group(1).strip().split('\n') if l.strip().startswith('-')]
    
    # Scenario C duration
    dur_match = re.search(r'Scenario C duration revision.*?\*\*(.+?)\*\*', text)
    if dur_match:
        result["scenario_c_duration"] = dur_match.group(1)
    
    return cache_set(status_cache, result)


def parse_positions(text):
    """Parse the free-form positions section into structured data."""
    positions = {
        "groups": [],
        "raw": text.strip(),
    }
    
    # Parse each ### subsection as a position group
    current_group = None
    for line in text.split('\n'):
        line = line.strip()
        if line.startswith('### '):
            if current_group:
                positions["groups"].append(current_group)
            header = line[4:]
            current_group = {"name": header, "lines": [], "entries": []}
        elif current_group and line and not line.startswith('---'):
            current_group["lines"].append(line)
            # Multiple patterns for position entries:
            # Pattern A: $67P×1 +104% (strike×qty before expiry)
            # Pattern B: $88P May×2 +82% (strike expiry×qty)
            # Pattern C: Sep×2 $60P +107% (expiry×qty strike)
            # Pattern D: $42.5P May×1 +6% (decimal strike)
            # Pattern E: $250P Jun×1 +84%
            
            # Unified: find all chunks that contain $STRIKE, an expiry month, a qty, and a P/L
            # First try: $STRIKEPx MONTH×QTY PNL or MONTH×QTY $STRIKEP PNL
            entries = re.findall(
                r'(\$[\d.]+[PC])(?:×(\d+))?\s*'
                r'((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*)?'
                r'(?:×(\d+))?\s*'
                r'([+-][\d.]+%)',
                line
            )
            for strike, qty1, expiry, qty2, pnl in entries:
                qty = int(qty1 or qty2 or 1)
                current_group["entries"].append({
                    "strike": strike, "expiry": expiry or "", "qty": qty, "pnl": pnl,
                })
            
            # Also try reversed: MONTH×QTY $STRIKEP PNL (e.g. "Sep×2 $60P +107%")
            rev_entries = re.findall(
                r'((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*)×(\d+)\s+'
                r'(\$[\d.]+[PC])\s+([+-][\d.]+%)',
                line
            )
            for expiry, qty, strike, pnl in rev_entries:
                # Avoid duplicates — check if this strike+pnl combo already added
                if not any(e["strike"] == strike and e["pnl"] == pnl for e in current_group["entries"]):
                    current_group["entries"].append({
                        "strike": strike, "expiry": expiry, "qty": int(qty), "pnl": pnl,
                    })
    if current_group:
        positions["groups"].append(current_group)
    
    return positions


# ============================================================
# AGENT STATUS PARSER
# ============================================================

AGENT_LABELS = {
    "LABOR": "Employment/Claims",
    "CARL": "Consumer Credit",
    "HENRY": "Market Structure",
    "SAM": "Japan/BOJ/JGB",
    "REGINALD": "Regional Banks",
    "LIQUID": "Funding/Treasury",
    "MARCO": "Migration/Labor",
    "OTTO": "Auto/Consumer DQ",
    "BROCK": "BDC/Private Credit",
    "HAWK": "Geopolitical/Military",
    "BRENT": "Oil/Energy",
    "ZHAO": "China/Capital Flows",
    "HANS": "Europe (US Lens)",
    "SHADE": "PE-Insurance-Captive",
    "NEXUS": "Cross-Agent Synthesis",
    "RED": "Adversarial Analysis",
    "DARWIN": "System Evolution",
}

def get_agent_path(name):
    """Get the STATUS.md path for an agent."""
    name = name.upper()
    path = os.path.join(WORKSPACE, "AGENTS", name, "STATUS.md")
    if os.path.exists(path):
        return path
    return None

def parse_agent_status(name):
    """Parse an individual agent's STATUS.md."""
    name = name.upper()
    
    cache_key = name
    if cache_key in agent_cache and cache_fresh(agent_cache[cache_key]):
        return agent_cache[cache_key]["data"]
    
    path = get_agent_path(name)
    if not path:
        return {"error": f"Agent {name} not found"}
    
    try:
        with open(path, 'r') as f:
            text = f.read()
    except:
        return {"error": f"Could not read {name}/STATUS.md"}
    
    result = {
        "name": name,
        "label": AGENT_LABELS.get(name, ""),
        "status": "unknown",
        "status_line": "",
        "updated": "",
        "header_lines": [],
        "tables": [],
        "full_text": text[:15000],  # Cap at 15KB for API response
    }
    
    # Parse first line for status
    first_line = text.split('\n')[0] if text else ""
    result["status_line"] = first_line
    
    # Extract update time
    m = re.search(r'\*\*Last Updated:\*\*\s*([^|*]+)', text)
    if m:
        result["updated"] = m.group(1).strip()
    
    # Extract status level
    m = re.search(r'\*\*(?:Overall\s+|Signal\s+)?Status:\*\*\s*(.+?)(?:\n|$)', text)
    if m:
        status_text = m.group(1)
        if '🔴🔴🔴' in status_text or 'TRIPLE' in status_text.upper():
            result["status"] = "red3"
        elif '🔴🔴' in status_text or 'CRITICAL' in status_text.upper():
            result["status"] = "red"
        elif '🔴' in status_text:
            result["status"] = "red"
        elif '🟠' in status_text or 'ORANGE' in status_text.upper() or 'ELEVATED' in status_text.upper():
            result["status"] = "orange"
        elif '🟡' in status_text or 'YELLOW' in status_text.upper():
            result["status"] = "yellow"
        elif '🟢' in status_text or 'GREEN' in status_text.upper():
            result["status"] = "green"
    
    # Grab header lines (first ~10 non-empty lines for quick summary)
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    result["header_lines"] = lines[:15]
    
    # Find all tables
    table_blocks = re.findall(r'(\|[^\n]+\|\n\|[-| :]+\|\n(?:\|[^\n]+\|\n)*)', text)
    for block in table_blocks:
        parsed = parse_md_table(block)
        if parsed:
            result["tables"].append(parsed)
    
    # Cache it
    if cache_key not in agent_cache:
        agent_cache[cache_key] = make_cache(30)
    cache_set(agent_cache[cache_key], result)
    
    return result

def list_all_agents():
    """List all agents with their status from PROME/STATUS.md agent table + filesystem."""
    status_data = parse_status()
    agents_from_status = {}
    for row in status_data.get("agents", []):
        name = row.get("Agent", "").strip()
        if name:
            agents_from_status[name] = {
                "name": name,
                "status_emoji": row.get("St", ""),
                "key_state": row.get("Key State", ""),
                "updated": row.get("Upd", ""),
                "label": AGENT_LABELS.get(name, ""),
            }
    
    # Also check filesystem for agents not in the table
    agents_dir = os.path.join(WORKSPACE, "AGENTS")
    if os.path.isdir(agents_dir):
        for d in sorted(os.listdir(agents_dir)):
            full = os.path.join(agents_dir, d, "STATUS.md")
            if os.path.isfile(full) and d.upper() not in agents_from_status:
                agents_from_status[d.upper()] = {
                    "name": d.upper(),
                    "status_emoji": "",
                    "key_state": "",
                    "updated": "",
                    "label": AGENT_LABELS.get(d.upper(), ""),
                }
    
    return list(agents_from_status.values())

# ============================================================
# PRICE FETCHER (extended with oil)
# ============================================================

# Build PRICE_SYMBOLS from config.py + display-only extras
# Thresholds come from config.py; extras (SPY, GLD, etc.) are display-only
def _build_price_symbols():
    symbols = {}
    # Pull thresholds from config.py for price-sourced series
    for s in STRESS_SERIES:
        if s["source"] == "price":
            ticker_key = s["id"].replace("=F", "").replace("=X", "").replace("^", "")
            direction = "above" if s["direction"] == "higher_worse" else "below"
            # Use red boundary as threshold
            red = s["red"]
            threshold = red[0] if red[0] is not None else red[1]
            symbols[ticker_key] = {
                "yahoo": s["id"],
                "threshold": threshold,
                "direction": direction,
                "label": s["name"],
            }
    # Display-only extras (no thresholds — not in config.py)
    for key, yahoo, label in [
        ("SPY", "SPY", "S&P 500"), ("IWM", "IWM", "Russell 2000"),
        ("GLD", "GLD", "Gold"), ("HYG", "HYG", "HY Bond ETF"),
        ("CL", "CL=F", "WTI Crude"), ("UNG", "UNG", "Nat Gas ETF"),
    ]:
        if key not in symbols:
            symbols[key] = {"yahoo": yahoo, "threshold": None, "label": label}
    return symbols

PRICE_SYMBOLS = _build_price_symbols()

last_breach_state = load_json_file(BREACH_STATE_FILE, {})

def fetch_prices():
    global last_breach_state
    if cache_fresh(price_cache):
        return price_cache["data"]
    
    prices = {}
    for key, cfg in PRICE_SYMBOLS.items():
        prices[key] = {
            "value": None,
            "threshold": cfg.get("threshold"),
            "direction": cfg.get("direction"),
            "label": cfg.get("label", key),
        }
        try:
            url = f"https://query1.finance.yahoo.com/v8/finance/chart/{cfg['yahoo']}?interval=1d&range=1d"
            req = urllib.request.Request(url, headers={"User-Agent": "PROME-Dashboard/2.0"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode())
                price = data.get("chart", {}).get("result", [{}])[0].get("meta", {}).get("regularMarketPrice")
                prices[key]["value"] = round(price, 2) if price else None
        except Exception as e:
            print(f"[Prices] {key} error: {e}")
    
    prices["_updated"] = time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())
    
    # Check thresholds
    for key, data in prices.items():
        if key.startswith('_') or not isinstance(data, dict):
            continue
        if data.get("threshold") is None or data.get("value") is None:
            continue
        val, thresh, direction = data["value"], data["threshold"], data.get("direction")
        breached = (direction == "below" and val < thresh) or (direction == "above" and val > thresh)
        prev = last_breach_state.get(key, False)
        if breached and not prev:
            add_alert("threshold", "warning", f"{key} breached {thresh} (now {val})", val, thresh)
        elif not breached and prev:
            add_alert("threshold", "info", f"{key} recovered (now {val}, threshold {thresh})", val, thresh)
        last_breach_state[key] = breached
    save_json_file(BREACH_STATE_FILE, last_breach_state)
    
    return cache_set(price_cache, prices)

# ============================================================
# FRED / BLS / TREASURY / SEC (kept from v1, condensed)
# ============================================================

# Build FRED_SERIES from config.py + display-only extras
def _build_fred_series():
    series = {}
    for s in STRESS_SERIES:
        if s["source"] == "fred":
            direction = "above" if s["direction"] == "higher_worse" else "below"
            red = s["red"]
            threshold = red[0] if red[0] is not None else red[1]
            # Apply multiplier to threshold if needed (OAS stored in bps, FRED returns %)
            mult = s.get("multiply", 1)
            if mult != 1:
                threshold = threshold / mult  # compare in FRED's native units
            fmt = "thousands" if threshold and threshold > 10000 else "percent"
            series[s["id"]] = {
                "name": s["name"], "threshold": threshold,
                "direction": direction, "format": fmt,
            }
    # Display-only extras not in config.py
    for sid, name, fmt in [
        ("JTSJOL", "JOLTS Job Openings", "thousands"),
        ("UNRATE", "Unemployment Rate", "percent"),
        ("U6RATE", "U-6 Underemployment", "percent"),
        ("PAYEMS", "Nonfarm Payrolls", "thousands"),
        ("RRPONTSYD", "RRP Balance", "billions"),
    ]:
        if sid not in series:
            series[sid] = {"name": name, "threshold": None, "direction": None, "format": fmt}
    return series

FRED_SERIES = _build_fred_series()

def fetch_fred_data():
    if cache_fresh(fred_cache):
        return fred_cache["data"]
    
    fred_data = {"series": {}, "updated": None}
    for series_id, config in FRED_SERIES.items():
        try:
            url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={FRED_API_KEY}&file_type=json&sort_order=desc&limit=5"
            req = urllib.request.Request(url, headers={"User-Agent": "PROME-Dashboard/2.0"})
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode())
                obs = data.get("observations", [])
                latest = prev = None
                for o in obs:
                    if o.get("value") and o["value"] != ".":
                        if latest is None:
                            latest = o
                        elif prev is None:
                            prev = o
                            break
                if latest:
                    value = float(latest["value"])
                    prev_val = float(prev["value"]) if prev and prev["value"] != "." else None
                    breached = False
                    if config["threshold"] is not None:
                        if config["direction"] == "above":
                            breached = value > config["threshold"]
                        elif config["direction"] == "below":
                            breached = value < config["threshold"]
                    fred_data["series"][series_id] = {
                        "name": config["name"], "value": value,
                        "previous": prev_val,
                        "change": value - prev_val if prev_val else None,
                        "date": latest["date"],
                        "threshold": config["threshold"],
                        "direction": config["direction"],
                        "format": config["format"],
                        "breached": breached,
                    }
        except Exception as e:
            fred_data["series"][series_id] = {"error": str(e), "name": config["name"]}
    
    fred_data["updated"] = time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())
    return cache_set(fred_cache, fred_data)

BLS_SERIES = {
    "CES0500000001": {"name": "Total Private Employment", "format": "thousands"},
    "CES6056132001": {"name": "Temp Help Services", "format": "thousands"},
    "CES3000000001": {"name": "Manufacturing Employment", "format": "thousands"},
    "CES4200000001": {"name": "Retail Trade Employment", "format": "thousands"},
    "CES2000000001": {"name": "Construction Employment", "format": "thousands"},
    "CES5500000001": {"name": "Financial Activities", "format": "thousands"},
}

def fetch_bls_data():
    if cache_fresh(bls_cache):
        return bls_cache["data"]
    
    bls_data = {"series": {}, "updated": None}
    try:
        import datetime
        year = datetime.datetime.now().year
        payload = json.dumps({
            "seriesid": list(BLS_SERIES.keys()),
            "startyear": str(year - 1), "endyear": str(year),
            "registrationkey": BLS_API_KEY,
        }).encode()
        req = urllib.request.Request(
            "https://api.bls.gov/publicAPI/v2/timeseries/data/",
            data=payload, headers={"Content-Type": "application/json", "User-Agent": "PROME-Dashboard/2.0"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
            if data.get("status") == "REQUEST_SUCCEEDED":
                for series in data.get("Results", {}).get("series", []):
                    sid = series.get("seriesID")
                    cfg = BLS_SERIES.get(sid, {})
                    obs = series.get("data", [])
                    if obs:
                        val = float(obs[0].get("value", 0))
                        prev_val = float(obs[1].get("value", 0)) if len(obs) > 1 else None
                        bls_data["series"][sid] = {
                            "name": cfg.get("name", sid), "value": val,
                            "previous": prev_val,
                            "change": val - prev_val if prev_val else None,
                            "period": f"{obs[0].get('periodName', '')} {obs[0].get('year', '')}",
                            "format": cfg.get("format", "thousands"),
                        }
    except Exception as e:
        print(f"[BLS] Fetch error: {e}")
    bls_data["updated"] = time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())
    return cache_set(bls_cache, bls_data)

def fetch_treasury_auctions():
    if cache_fresh(treasury_cache):
        return treasury_cache["data"]
    result = {"auctions": [], "updated": None}
    try:
        url = "https://www.treasurydirect.gov/TA_WS/securities/auctioned?format=json&pagesize=15"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            for rec in data:
                result["auctions"].append({
                    "security_type": rec.get("securityType", ""),
                    "security_term": rec.get("securityTerm", ""),
                    "auction_date": (rec.get("auctionDate") or "")[:10],
                    "high_yield": rec.get("highYield", "") or rec.get("highInvestmentRate", ""),
                    "bid_to_cover": rec.get("bidToCoverRatio", ""),
                })
    except Exception as e:
        print(f"[Treasury] error: {e}")
    result["updated"] = time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())
    return cache_set(treasury_cache, result)

SEC_WATCHLIST = {
    "WAL": {"cik": "0001212545", "name": "Western Alliance"},
    "OZK": {"cik": "0001569650", "name": "Bank OZK"},
    "EGBN": {"cik": "0001050441", "name": "Eagle Bancorp"},
    "ZION": {"cik": "0000109380", "name": "Zions Bancorporation"},
    "FLG": {"cik": "0001033012", "name": "Flagstar Financial"},
    "APO": {"cik": "0001411494", "name": "Apollo Global Management"},
}

seen_filings = set(load_json_file(SEEN_FILINGS_FILE, []))

def fetch_sec_filings():
    global seen_filings
    if cache_fresh(sec_cache):
        return sec_cache["data"]
    
    result = {"filings": [], "updated": None}
    for ticker, info in SEC_WATCHLIST.items():
        try:
            url = f"https://data.sec.gov/submissions/CIK{info['cik']}.json"
            req = urllib.request.Request(url, headers={
                "User-Agent": "PROME-Dashboard research@example.com", "Accept": "application/json",
            })
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode())
                recent = data.get("filings", {}).get("recent", {})
                forms = recent.get("form", [])
                dates = recent.get("filingDate", [])
                accessions = recent.get("accessionNumber", [])
                docs = recent.get("primaryDocument", [])
                important = ["10-K", "10-Q", "8-K", "4", "SC 13G", "SC 13D"]
                for i in range(min(10, len(forms))):
                    if not any(forms[i].startswith(f) for f in important):
                        continue
                    cik = info["cik"].lstrip("0")
                    doc = docs[i] if i < len(docs) else ""
                    fid = f"{ticker}_{accessions[i]}"
                    result["filings"].append({
                        "ticker": ticker, "form": forms[i], "date": dates[i],
                        "url": f"https://www.sec.gov/Archives/edgar/data/{cik}/{accessions[i].replace('-','')}/{doc}",
                    })
                    if fid not in seen_filings and forms[i] in ["10-K", "10-Q", "8-K"]:
                        seen_filings.add(fid)
                        save_json_file(SEEN_FILINGS_FILE, list(seen_filings))
        except Exception as e:
            print(f"[SEC] {ticker}: {e}")
    
    result["filings"].sort(key=lambda x: x["date"], reverse=True)
    result["updated"] = time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())
    return cache_set(sec_cache, result)

# ============================================================
# PREDICTIONS PARSER (kept from v1)
# ============================================================

def parse_predictions():
    result = {
        "calibration": {"total": 0, "correct": 0, "partial": 0, "wrong": 0, "accuracy": 0},
        "imminent": [], "approaching": [], "by_agent": {}, "resolved": [],
        "updated": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
    }
    
    monitor = read_file("PROME/PREDICTIONS_MONITOR.md")
    if monitor:
        # Parse imminent
        m = re.search(r'## 🔴 IMMINENT.*?\n\n\|.*?\n\|[-|\s]+\n(.*?)\n\n', monitor, re.DOTALL)
        if m:
            for line in m.group(1).strip().split('\n'):
                parts = [p.strip() for p in line.split('|')[1:-1]]
                if len(parts) >= 6:
                    result["imminent"].append({
                        "id": parts[0].replace('**',''), "prediction": parts[1],
                        "current": parts[2], "target": parts[3],
                        "gap": parts[4].replace('**',''), "eta": parts[5],
                        "agent": parts[6] if len(parts) > 6 else "",
                    })
        # Parse approaching
        m = re.search(r'## 🟡 APPROACHING.*?\n\n\|.*?\n\|[-|\s]+\n(.*?)\n\n', monitor, re.DOTALL)
        if m:
            for line in m.group(1).strip().split('\n'):
                parts = [p.strip() for p in line.split('|')[1:-1]]
                if len(parts) >= 6:
                    result["approaching"].append({
                        "id": parts[0], "prediction": parts[1],
                        "current": parts[2], "target": parts[3],
                        "gap": parts[4], "eta": parts[5],
                        "agent": parts[6] if len(parts) > 6 else "",
                    })
    
    predictions = read_file("PREDICTIONS.md")
    if predictions:
        # Resolved
        resolved_section = re.search(r'## RECENTLY RESOLVED\n(.*?)(?=\n## [A-Z]|\n---\n\n## |\Z)', predictions, re.DOTALL)
        if resolved_section:
            tables = re.findall(r'\|.*?\n\|[-|\s]+\n(.*?)(?=\n\n|\n###|\Z)', resolved_section.group(1), re.DOTALL)
            for table in tables:
                for line in table.strip().split('\n'):
                    if not line.strip().startswith('|'):
                        continue
                    parts = [p.strip() for p in line.split('|')[1:-1]]
                    if len(parts) >= 3:
                        result["resolved"].append({
                            "id": parts[0].replace('**',''), "prediction": parts[1],
                            "result": parts[2],
                            "confidence": parts[3] if len(parts) > 3 else "",
                            "notes": parts[4] if len(parts) > 4 else "",
                        })
                        result["calibration"]["total"] += 1
                        if '✅' in parts[2]:
                            result["calibration"]["correct"] += 1
                        elif '❌' in parts[2]:
                            result["calibration"]["wrong"] += 1
                        elif '⚠️' in parts[2]:
                            result["calibration"]["partial"] += 0.5
                            result["calibration"]["correct"] += 0.5
        
        if result["calibration"]["total"] > 0:
            result["calibration"]["accuracy"] = round(
                result["calibration"]["correct"] / result["calibration"]["total"] * 100, 1
            )
        
        # By agent
        for agent in ["LABOR","CARL","REGINALD","BROCK","SAM","LIQUID","MARCO","HENRY","OTTO","PROME","ZHAO","HAWK","BRENT"]:
            pat = rf'### {agent}\n\|.*?\n\|[-|\s]+\n(.*?)(?=\n\n### |\n\n---|\Z)'
            m = re.search(pat, predictions, re.DOTALL)
            if m:
                preds = []
                for line in m.group(1).strip().split('\n'):
                    if not line.strip() or line.startswith('|--'):
                        continue
                    parts = [p.strip() for p in line.split('|')[1:-1]]
                    if len(parts) >= 5:
                        preds.append({
                            "id": parts[0], "prediction": parts[1],
                            "timeframe": parts[2], "confidence": parts[3],
                            "status": parts[4],
                        })
                if preds:
                    result["by_agent"][agent] = preds
    
    return result

# ============================================================
# STRESS DASHBOARD (from config.py)
# ============================================================

stress_cache = make_cache(300)  # 5 min

def fetch_stress_dashboard():
    """Fetch all series from config.py, classify each, return structured data."""
    if cache_fresh(stress_cache):
        return stress_cache["data"]

    results = []
    for s in STRESS_SERIES:
        entry = {
            "name": s["name"],
            "agent": s["agent"],
            "tier": s["tier"],
            "value": None,
            "zone": "unknown",
            "emoji": "⚪",
            "notes": s.get("notes", ""),
        }

        try:
            if s["source"] == "price":
                url = f"https://query1.finance.yahoo.com/v8/finance/chart/{s['id']}?interval=1d&range=1d"
                req = urllib.request.Request(url, headers={"User-Agent": "PROME-Dashboard/2.0"})
                with urllib.request.urlopen(req, timeout=10) as resp:
                    data = json.loads(resp.read().decode())
                    price = data.get("chart", {}).get("result", [{}])[0].get("meta", {}).get("regularMarketPrice")
                    entry["value"] = round(price, 2) if price else None

            elif s["source"] == "fred":
                url = f"https://api.stlouisfed.org/fred/series/observations?series_id={s['id']}&api_key={FRED_API_KEY}&file_type=json&sort_order=desc&limit=1"
                req = urllib.request.Request(url, headers={"User-Agent": "PROME-Dashboard/2.0"})
                with urllib.request.urlopen(req, timeout=15) as resp:
                    data = json.loads(resp.read().decode())
                    obs = data.get("observations", [])
                    if obs and obs[0].get("value") != ".":
                        entry["value"] = float(obs[0]["value"]) * s.get("multiply", 1)
                        entry["date"] = obs[0]["date"]
        except Exception as e:
            entry["error"] = str(e)

        if entry["value"] is not None:
            entry["zone"] = stress_classify(entry["value"], s)
            entry["emoji"] = stress_emoji(entry["zone"])
            entry["formatted"] = stress_format(entry["value"], s)

        # Shadow adjustment
        shadow = s.get("shadow_adj")
        if shadow and entry["value"] is not None:
            entry["shadow"] = {
                "label": shadow["label"],
                "value": entry["value"] + shadow["add"],
            }

        results.append(entry)

    reds = sum(1 for r in results if r["zone"] == "red")
    yellows = sum(1 for r in results if r["zone"] == "yellow")
    greens = sum(1 for r in results if r["zone"] == "green")

    # Weighted score (Tier 1 = 2pts, Tier 2 = 1pt)
    score = sum(2 if r["tier"] == 1 else 1 for r in results if r["zone"] == "red")
    if score >= 6:
        level = "CRITICAL"
    elif score >= 4:
        level = "ELEVATED"
    elif score >= 2:
        level = "WATCH"
    else:
        level = "CALM"

    output = {
        "series": results,
        "summary": {"red": reds, "yellow": yellows, "green": greens, "score": score, "level": level},
        "updated": time.strftime("%Y-%m-%d %H:%M:%S ET", time.localtime()),
    }
    return cache_set(stress_cache, output)


# ============================================================
# HTTP HANDLER
# ============================================================

class DashboardHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(os.path.abspath(__file__)), **kwargs)
    
    def send_json(self, data, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data, default=str).encode())
    
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        params = parse_qs(parsed.query)
        
        # ---- NEW DYNAMIC ENDPOINTS ----
        
        # Full status (positions, scenarios, catalysts, agents, etc)
        if path == '/api/status':
            self.send_json(parse_status())
            return
        
        # Positions only
        if path == '/api/positions':
            data = parse_status()
            self.send_json(data.get("positions", {}))
            return
        
        # Scenarios only
        if path == '/api/scenarios':
            data = parse_status()
            self.send_json(data.get("scenarios", []))
            return
        
        # Catalysts/dates only
        if path == '/api/catalysts':
            data = parse_status()
            self.send_json(data.get("catalysts", []))
            return
        
        # Convictions
        if path == '/api/convictions':
            data = parse_status()
            self.send_json(data.get("convictions", []))
            return
        
        # Pending actions
        if path == '/api/pending':
            data = parse_status()
            self.send_json(data.get("pending", []))
            return
        
        # Energy/War aggregate endpoint
        if path == '/api/energy':
            data = parse_status()
            energy = {
                "scenarios": data.get("scenarios", []),
                "hamilton": data.get("hamilton"),
                "taiwan_lng": data.get("taiwan_lng", []),
                "tsmc_chain": data.get("tsmc_chain"),
                "taiwan_escalation": data.get("taiwan_escalation", []),
                "fertilizer": data.get("fertilizer", []),
                "fertilizer_header": data.get("fertilizer_header"),
                "fertilizer_loop": data.get("fertilizer_loop"),
                "exit_rules": data.get("exit_rules", []),
                "exit_template": data.get("exit_template"),
                "exit_protocol_a": data.get("exit_protocol_a", []),
                "exit_protocol_c": data.get("exit_protocol_c", []),
                "scenario_c_duration": data.get("scenario_c_duration"),
                "cross_agent": data.get("cross_agent", []),
                "headline": data.get("headline"),
            }
            # Add HAWK and BRENT agent summaries
            for agent_name in ["HAWK", "BRENT", "SAM", "LIQUID"]:
                agent_data = parse_agent_status(agent_name)
                if agent_data and not agent_data.get("error"):
                    energy[f"agent_{agent_name.lower()}"] = {
                        "status": agent_data.get("status"),
                        "updated": agent_data.get("updated"),
                        "header_lines": agent_data.get("header_lines", [])[:10],
                    }
            # Add oil prices
            prices = fetch_prices()
            energy["brent"] = prices.get("BZ", {}).get("value")
            energy["wti"] = prices.get("CL", {}).get("value")
            energy["ung"] = prices.get("UNG", {}).get("value")
            self.send_json(energy)
            return
        
        # All agents summary
        if path == '/api/agents':
            self.send_json(list_all_agents())
            return
        
        # Individual agent detail
        if path.startswith('/api/agent/'):
            name = path.split('/')[-1]
            self.send_json(parse_agent_status(name))
            return
        
        # News sweep latest results
        if path == '/api/news':
            news_json = os.path.join(WORKSPACE, "FORGE/tools/news-sweep/latest.json")
            if os.path.exists(news_json):
                with open(news_json, "r") as f:
                    try:
                        self.send_json(json.load(f))
                    except json.JSONDecodeError:
                        self.send_json({"error": "Invalid JSON in latest.json"})
            else:
                self.send_json({"error": "No sweep data yet. Run: python3 FORGE/tools/news-sweep/sweep.py"})
            return

        # Stress dashboard (from config.py thresholds)
        if path == '/api/stress':
            stress_data = fetch_stress_dashboard()
            self.send_json(stress_data)
            return
        
        # ---- EXISTING ENDPOINTS ----
        
        if path == '/api/prices':
            self.send_json(fetch_prices())
            return
        
        if path == '/api/fred':
            self.send_json(fetch_fred_data())
            return
        
        if path == '/api/bls':
            self.send_json(fetch_bls_data())
            return
        
        if path == '/api/treasury':
            self.send_json(fetch_treasury_auctions())
            return
        
        if path == '/api/sec':
            self.send_json(fetch_sec_filings())
            return
        
        if path == '/api/predictions':
            self.send_json(parse_predictions())
            return
        
        if path == '/api/alerts':
            limit = int(params.get('limit', [50])[0])
            alerts = list(reversed(load_alerts()[-limit:]))
            self.send_json(alerts)
            return
        
        if path == '/api/alerts/add':
            msg = params.get('message', ['Manual alert'])[0]
            sev = params.get('severity', ['info'])[0]
            self.send_json(add_alert("manual", sev, msg))
            return
        
        if path == '/api/subagents':
            limit = int(params.get('limit', [20])[0])
            log = list(reversed(load_subagent_log()[-limit:]))
            self.send_json(log)
            return
        
        if path == '/api/subagents/log':
            agent_id = params.get('agent', [None])[0]
            task = params.get('task', [None])[0]
            if not agent_id or not task:
                self.send_json({"error": "Missing agent or task"}, 400)
                return
            entry = add_subagent_entry(
                agent_id, task,
                status=params.get('status', ['running'])[0],
                result=params.get('result', [None])[0],
                session_key=params.get('session_key', [None])[0],
                runtime_sec=float(params['runtime'][0]) if 'runtime' in params else None,
            )
            self.send_json(entry)
            return
        
        # Raw file access (kept for backward compat)
        if path == '/api/file':
            if 'path' not in params:
                self.send_json({"error": "Missing path"}, 400)
                return
            file_path = params['path'][0]
            full_path = os.path.join(WORKSPACE, file_path)
            real_path = os.path.realpath(full_path)
            if not real_path.startswith(os.path.realpath(WORKSPACE)):
                self.send_json({"error": "Outside workspace"}, 403)
                return
            content = read_file(real_path)
            if content is None:
                self.send_json({"error": "Not found"}, 404)
                return
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(content.encode())
            return
        
        # API index
        if path == '/api':
            self.send_json({
                "endpoints": [
                    "/api/status", "/api/positions", "/api/scenarios",
                    "/api/catalysts", "/api/convictions", "/api/pending",
                    "/api/agents", "/api/agent/{name}", "/api/energy",
                    "/api/stress",
                    "/api/prices", "/api/fred", "/api/bls",
                    "/api/treasury", "/api/sec", "/api/predictions",
                    "/api/alerts", "/api/subagents", "/api/file?path=...",
                ],
                "version": "2.0",
            })
            return
        
        # Static files
        return super().do_GET()
    
    def log_message(self, fmt, *args):
        print(f"[Dashboard] {args[0]}")

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

def main():
    with ReusableTCPServer(("0.0.0.0", PORT), DashboardHandler) as httpd:
        print(f"PROME Dashboard v2 running at http://0.0.0.0:{PORT}")
        print(f"Workspace: {WORKSPACE}")
        print(f"API index: http://localhost:{PORT}/api")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down...")

if __name__ == "__main__":
    main()
