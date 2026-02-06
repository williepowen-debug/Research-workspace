#!/usr/bin/env python3
"""
PROME Dashboard Server
Simple HTTP server that serves the dashboard and provides API access to workspace files.
"""

import http.server
import socketserver
import json
import os
import urllib.request
import time
from urllib.parse import urlparse, parse_qs

PORT = 8080
WORKSPACE = "/home/moltbot/.openclaw/workspace"
ALERTS_FILE = os.path.join(WORKSPACE, "dashboard", "alerts.json")
FRED_API_KEY = "8ce3f08db56f151f54221a0dd12b63de"
BLS_API_KEY = "28cc34af39834eb2a4d85d3119f72077"

# Telegram alerting - direct bot API
TELEGRAM_BOT_TOKEN = "8533568512:AAEf4FwstJbg0GE0FcEB-w96I9hJokPuY8k"
TELEGRAM_CHAT_ID = "8463631023"  # Will's Telegram ID

# Price cache (avoid hammering APIs)
price_cache = {
    "data": None,
    "timestamp": 0,
    "ttl": 300  # 5 minutes
}

# FRED data cache (longer TTL - economic data doesn't change intraday)
fred_cache = {
    "data": None,
    "timestamp": 0,
    "ttl": 3600  # 1 hour
}

# BLS data cache
bls_cache = {
    "data": None,
    "timestamp": 0,
    "ttl": 3600  # 1 hour
}

# Alert tracking
last_breach_state = {}

# FRED series we care about
FRED_SERIES = {
    "ICSA": {"name": "Initial Claims", "threshold": 250000, "direction": "above", "format": "thousands"},
    "CCSA": {"name": "Continuing Claims", "threshold": 2000000, "direction": "above", "format": "thousands"},
    "JTSJOL": {"name": "JOLTS Job Openings", "threshold": 7000, "direction": "below", "format": "thousands"},
    "TEMPHELPS": {"name": "Temp Employment", "threshold": None, "direction": None, "format": "thousands"},
    "UNRATE": {"name": "Unemployment Rate", "threshold": 5.0, "direction": "above", "format": "percent"},
    "PAYEMS": {"name": "Nonfarm Payrolls", "threshold": None, "direction": None, "format": "thousands"},
}

def fetch_fred_data():
    """Fetch economic data from FRED API"""
    now = time.time()
    
    # Return cached data if fresh
    if fred_cache["data"] and (now - fred_cache["timestamp"]) < fred_cache["ttl"]:
        return fred_cache["data"]
    
    fred_data = {
        "series": {},
        "updated": None
    }
    
    for series_id, config in FRED_SERIES.items():
        try:
            url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={FRED_API_KEY}&file_type=json&sort_order=desc&limit=5"
            req = urllib.request.Request(url, headers={"User-Agent": "PROME-Dashboard/1.0"})
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode())
                observations = data.get("observations", [])
                
                if observations:
                    # Get latest non-empty value
                    latest = None
                    prev = None
                    for i, obs in enumerate(observations):
                        if obs.get("value") and obs["value"] != ".":
                            if latest is None:
                                latest = obs
                            elif prev is None:
                                prev = obs
                                break
                    
                    if latest:
                        value = float(latest["value"])
                        prev_value = float(prev["value"]) if prev and prev["value"] != "." else None
                        change = None
                        if prev_value is not None:
                            change = value - prev_value
                        
                        fred_data["series"][series_id] = {
                            "name": config["name"],
                            "value": value,
                            "previous": prev_value,
                            "change": change,
                            "date": latest["date"],
                            "threshold": config["threshold"],
                            "direction": config["direction"],
                            "format": config["format"],
                            "breached": check_fred_breach(value, config)
                        }
        except Exception as e:
            print(f"[FRED] {series_id} fetch error: {e}")
            fred_data["series"][series_id] = {"error": str(e), "name": config["name"]}
    
    fred_data["updated"] = time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())
    
    # Cache it
    fred_cache["data"] = fred_data
    fred_cache["timestamp"] = now
    
    # Check for alert-worthy changes
    check_fred_alerts(fred_data)
    
    return fred_data

# BLS series we care about
# CES = Current Employment Statistics (establishment survey)
# Series ID format: CES + adjustment + supersector + industry + data_type
BLS_SERIES = {
    "CES0500000001": {"name": "Total Private Employment", "format": "thousands"},
    "CES6056132001": {"name": "Temp Help Services", "format": "thousands"},  # Key leading indicator
    "CES3000000001": {"name": "Manufacturing Employment", "format": "thousands"},
    "CES4200000001": {"name": "Retail Trade Employment", "format": "thousands"},
    "CES6500000001": {"name": "Healthcare Employment", "format": "thousands"},
    "CES2000000001": {"name": "Construction Employment", "format": "thousands"},
    "CES5500000001": {"name": "Financial Activities", "format": "thousands"},
    "LNS14000000": {"name": "Unemployment Rate (BLS)", "format": "percent"},
}

def fetch_bls_data():
    """Fetch employment data from BLS API"""
    now = time.time()
    
    # Return cached data if fresh
    if bls_cache["data"] and (now - bls_cache["timestamp"]) < bls_cache["ttl"]:
        return bls_cache["data"]
    
    bls_data = {
        "series": {},
        "updated": None
    }
    
    try:
        # BLS API v2 - can fetch multiple series at once
        import datetime
        current_year = datetime.datetime.now().year
        
        payload = json.dumps({
            "seriesid": list(BLS_SERIES.keys()),
            "startyear": str(current_year - 1),
            "endyear": str(current_year),
            "registrationkey": BLS_API_KEY
        }).encode('utf-8')
        
        req = urllib.request.Request(
            "https://api.bls.gov/publicAPI/v2/timeseries/data/",
            data=payload,
            headers={
                "Content-Type": "application/json",
                "User-Agent": "PROME-Dashboard/1.0"
            },
            method="POST"
        )
        
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
            
            if data.get("status") == "REQUEST_SUCCEEDED":
                for series in data.get("Results", {}).get("series", []):
                    series_id = series.get("seriesID")
                    config = BLS_SERIES.get(series_id, {})
                    observations = series.get("data", [])
                    
                    if observations:
                        # BLS returns most recent first
                        latest = observations[0]
                        prev = observations[1] if len(observations) > 1 else None
                        
                        value = float(latest.get("value", 0))
                        prev_value = float(prev.get("value", 0)) if prev else None
                        change = value - prev_value if prev_value else None
                        
                        # Calculate YoY change if we have enough data
                        yoy_change = None
                        for obs in observations:
                            if obs.get("year") == str(current_year - 1) and obs.get("period") == latest.get("period"):
                                yoy_value = float(obs.get("value", 0))
                                yoy_change = value - yoy_value
                                break
                        
                        bls_data["series"][series_id] = {
                            "name": config.get("name", series_id),
                            "value": value,
                            "previous": prev_value,
                            "change": change,
                            "yoy_change": yoy_change,
                            "period": f"{latest.get('periodName', '')} {latest.get('year', '')}",
                            "format": config.get("format", "thousands")
                        }
            else:
                print(f"[BLS] API error: {data.get('message', 'Unknown error')}")
                
    except Exception as e:
        print(f"[BLS] Fetch error: {e}")
    
    bls_data["updated"] = time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())
    
    # Cache it
    bls_cache["data"] = bls_data
    bls_cache["timestamp"] = now
    
    return bls_data

def check_fred_breach(value, config):
    """Check if a FRED value breaches its threshold"""
    if config["threshold"] is None:
        return False
    if config["direction"] == "above":
        return value > config["threshold"]
    elif config["direction"] == "below":
        return value < config["threshold"]
    return False

def check_fred_alerts(fred_data):
    """Generate alerts for FRED threshold breaches"""
    global last_breach_state
    
    for series_id, data in fred_data["series"].items():
        if "error" in data:
            continue
        
        key = f"fred_{series_id}"
        breached = data.get("breached", False)
        prev_breached = last_breach_state.get(key, False)
        
        if breached and not prev_breached:
            value = data["value"]
            threshold = data["threshold"]
            name = data["name"]
            
            if data["format"] == "thousands":
                value_str = f"{value/1000:.0f}K" if value >= 1000 else f"{value:.0f}"
                thresh_str = f"{threshold/1000:.0f}K" if threshold >= 1000 else f"{threshold:.0f}"
            else:
                value_str = f"{value:.1f}%"
                thresh_str = f"{threshold:.1f}%"
            
            add_alert(
                alert_type="fred",
                severity="critical" if series_id in ["ICSA", "UNRATE"] else "warning",
                message=f"{name} breached threshold: {value_str} (threshold: {thresh_str})",
                value=value,
                threshold=threshold
            )
        
        last_breach_state[key] = breached

def send_telegram_alert(message, severity="warning"):
    """Send alert to Telegram via Bot API"""
    try:
        # Add emoji based on severity
        emoji = {"critical": "🚨", "warning": "⚠️", "info": "ℹ️", "success": "✅"}.get(severity, "📊")
        full_message = f"{emoji} *PROME Alert*\n\n{message}"
        
        # Use Telegram Bot API directly
        payload = json.dumps({
            "chat_id": TELEGRAM_CHAT_ID,
            "text": full_message,
            "parse_mode": "Markdown"
        }).encode('utf-8')
        
        req = urllib.request.Request(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        
        with urllib.request.urlopen(req, timeout=10) as resp:
            result = json.loads(resp.read().decode())
            if result.get("ok"):
                print(f"[Telegram] Alert sent: {message[:50]}...")
                return True
            else:
                print(f"[Telegram] API error: {result}")
                return False
    except Exception as e:
        print(f"[Telegram] Failed to send alert: {e}")
        return False

def load_alerts():
    """Load alerts from file"""
    if os.path.exists(ALERTS_FILE):
        try:
            with open(ALERTS_FILE, 'r') as f:
                return json.load(f)
        except:
            return []
    return []

def save_alerts(alerts):
    """Save alerts to file"""
    # Keep only last 100 alerts
    alerts = alerts[-100:]
    with open(ALERTS_FILE, 'w') as f:
        json.dump(alerts, f, indent=2)

def add_alert(alert_type, severity, message, value=None, threshold=None, notify=True):
    """Add a new alert"""
    alerts = load_alerts()
    alert = {
        "id": int(time.time() * 1000),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
        "type": alert_type,
        "severity": severity,  # critical, warning, info, success
        "message": message,
        "value": value,
        "threshold": threshold
    }
    alerts.append(alert)
    save_alerts(alerts)
    print(f"[Alert] {severity.upper()}: {message}")
    
    # Send to Telegram for critical and warning alerts
    if notify and severity in ["critical", "warning"]:
        send_telegram_alert(message, severity)
    
    return alert

def check_thresholds(prices):
    """Check prices against thresholds and generate alerts"""
    global last_breach_state
    
    checks = [
        ("KRE", "below", "KRE dropped below ${threshold} (Position target approaching)"),
        ("VIX", "above", "VIX spiked above {threshold} (Fear elevated)"),
        ("BTC", "below", "BTC dropped below ${threshold} (Liquidity warning)"),
        ("USDJPY", "above", "USD/JPY broke above {threshold} (SAM threshold breached)"),
        ("TNX", "above", "10Y Treasury yield above {threshold}% (Restrictive)"),
        ("HYG", "below", "HYG dropped below ${threshold} (Credit stress signal)"),
    ]
    
    for symbol, direction, msg_template in checks:
        if symbol not in prices or prices[symbol]["value"] is None:
            continue
        
        value = prices[symbol]["value"]
        threshold = prices[symbol]["threshold"]
        
        if threshold is None:
            continue
        
        # Determine if currently breached
        if direction == "below":
            breached = value < threshold
        else:
            breached = value > threshold
        
        # Check if state changed
        prev_breached = last_breach_state.get(symbol, False)
        
        if breached and not prev_breached:
            # New breach - alert!
            msg = msg_template.format(threshold=threshold)
            add_alert(
                alert_type="threshold",
                severity="warning" if symbol not in ["VIX", "USDJPY"] else "critical",
                message=msg,
                value=value,
                threshold=threshold
            )
        elif not breached and prev_breached:
            # Recovered
            add_alert(
                alert_type="threshold",
                severity="info",
                message=f"{symbol} recovered (now {value}, threshold was {threshold})",
                value=value,
                threshold=threshold
            )
        
        last_breach_state[symbol] = breached

def fetch_prices():
    """Fetch current prices from free APIs"""
    now = time.time()
    
    # Return cached data if fresh
    if price_cache["data"] and (now - price_cache["timestamp"]) < price_cache["ttl"]:
        return price_cache["data"]
    
    prices = {
        "KRE": {"value": None, "threshold": 65, "direction": "below"},
        "VIX": {"value": None, "threshold": 25, "direction": "above"},
        "BTC": {"value": None, "threshold": 60000, "direction": "below"},
        "USDJPY": {"value": None, "threshold": 160, "direction": "above"},
        "TNX": {"value": None, "threshold": 5.0, "direction": "above"},  # 10Y Treasury yield
        "HYG": {"value": None, "threshold": 75, "direction": "below"},   # HY bond ETF (proxy for spreads)
        "SPY": {"value": None, "threshold": None, "direction": None},    # Context
        "GLD": {"value": None, "threshold": None, "direction": None},    # Risk-off indicator
        "updated": None
    }
    
    # Fetch BTC from CoinGecko (free, no auth)
    try:
        req = urllib.request.Request(
            "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd",
            headers={"User-Agent": "PROME-Dashboard/1.0"}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            prices["BTC"]["value"] = data.get("bitcoin", {}).get("usd")
    except Exception as e:
        print(f"[Prices] BTC fetch error: {e}")
    
    # Fetch from Yahoo Finance
    for symbol, key in [("KRE", "KRE"), ("^VIX", "VIX"), ("USDJPY=X", "USDJPY"), ("^TNX", "TNX"), ("HYG", "HYG"), ("SPY", "SPY"), ("GLD", "GLD")]:
        try:
            url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?interval=1d&range=1d"
            req = urllib.request.Request(url, headers={"User-Agent": "PROME-Dashboard/1.0"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode())
                price = data.get("chart", {}).get("result", [{}])[0].get("meta", {}).get("regularMarketPrice")
                prices[key]["value"] = round(price, 2) if price else None
        except Exception as e:
            print(f"[Prices] {symbol} fetch error: {e}")
    
    prices["updated"] = time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())
    
    # Cache it
    price_cache["data"] = prices
    price_cache["timestamp"] = now
    
    # Check thresholds and generate alerts
    check_thresholds(prices)
    
    return prices

class DashboardHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(os.path.abspath(__file__)), **kwargs)
    
    def do_GET(self):
        parsed = urlparse(self.path)
        
        # API endpoint to read workspace files
        if parsed.path == '/api/file':
            params = parse_qs(parsed.query)
            if 'path' not in params:
                self.send_error(400, 'Missing path parameter')
                return
            
            file_path = params['path'][0]
            full_path = os.path.join(WORKSPACE, file_path)
            
            # Security: ensure path stays within workspace
            real_path = os.path.realpath(full_path)
            if not real_path.startswith(os.path.realpath(WORKSPACE)):
                self.send_error(403, 'Path outside workspace')
                return
            
            if not os.path.exists(real_path):
                self.send_error(404, 'File not found')
                return
            
            try:
                with open(real_path, 'r') as f:
                    content = f.read()
                
                self.send_response(200)
                self.send_header('Content-type', 'text/plain; charset=utf-8')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(content.encode('utf-8'))
            except Exception as e:
                self.send_error(500, str(e))
            return
        
        # API endpoint to get live prices
        if parsed.path == '/api/prices':
            try:
                prices = fetch_prices()
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps(prices).encode('utf-8'))
            except Exception as e:
                self.send_error(500, str(e))
            return
        
        # API endpoint to get BLS employment data
        if parsed.path == '/api/bls':
            try:
                bls_data = fetch_bls_data()
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps(bls_data).encode('utf-8'))
            except Exception as e:
                self.send_error(500, str(e))
            return
        
        # API endpoint to get FRED economic data
        if parsed.path == '/api/fred':
            try:
                fred_data = fetch_fred_data()
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps(fred_data).encode('utf-8'))
            except Exception as e:
                self.send_error(500, str(e))
            return
        
        # API endpoint to get alerts
        if parsed.path == '/api/alerts':
            try:
                params = parse_qs(parsed.query)
                limit = int(params.get('limit', [50])[0])
                alerts = load_alerts()
                # Return most recent first
                alerts = list(reversed(alerts[-limit:]))
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps(alerts).encode('utf-8'))
            except Exception as e:
                self.send_error(500, str(e))
            return
        
        # API endpoint to add manual alert
        if parsed.path == '/api/alerts/add':
            params = parse_qs(parsed.query)
            msg = params.get('message', ['Manual alert'])[0]
            severity = params.get('severity', ['info'])[0]
            alert = add_alert(
                alert_type="manual",
                severity=severity,
                message=msg
            )
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(alert).encode('utf-8'))
            return
        
        # API endpoint to get agent statuses
        if parsed.path == '/api/agents':
            try:
                agents_data = []
                agents = [
                    ('LABOR', 'AGENTS/LABOR/STATUS.md'),
                    ('CARL', 'AGENTS/CARL/STATUS.md'),
                    ('HENRY', 'AGENTS/HENRY/STATUS.md'),
                    ('SAM', 'AGENTS/SAM/STATUS.md'),
                    ('REGINALD', 'AGENTS/REGINALD/STATUS.md'),
                    ('LIQUID', 'AGENTS/LIQUID/STATUS.md'),
                    ('MARCO', 'AGENTS/MARCO/STATUS.md'),
                    ('OTTO', 'AGENTS/OTTO/STATUS.md'),
                ]
                
                for name, path in agents:
                    full_path = os.path.join(WORKSPACE, path)
                    status = 'UNKNOWN'
                    if os.path.exists(full_path):
                        with open(full_path, 'r') as f:
                            content = f.read(500)  # Read first 500 chars
                            if '🔴' in content or 'RED' in content or 'CRITICAL' in content:
                                status = 'RED'
                            elif '🟠' in content or 'ORANGE' in content or 'ELEVATED' in content:
                                status = 'ORANGE'
                            elif '🟡' in content or 'YELLOW' in content:
                                status = 'YELLOW'
                            elif '🟢' in content or 'GREEN' in content:
                                status = 'GREEN'
                    
                    agents_data.append({'name': name, 'status': status, 'file': path})
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps(agents_data).encode('utf-8'))
            except Exception as e:
                self.send_error(500, str(e))
            return
        
        # Serve static files
        return super().do_GET()
    
    def log_message(self, format, *args):
        print(f"[Dashboard] {args[0]}")

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

def main():
    # Bind to all interfaces so Tailscale can reach it
    with ReusableTCPServer(("0.0.0.0", PORT), DashboardHandler) as httpd:
        print(f"PROME Dashboard running at http://127.0.0.1:{PORT}")
        print(f"Workspace: {WORKSPACE}")
        print("Press Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down...")

if __name__ == "__main__":
    main()
