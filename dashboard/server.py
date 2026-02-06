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

# SEC EDGAR watchlist - banks we're tracking
SEC_WATCHLIST = {
    "VLY": {"cik": "0000714310", "name": "Valley National Bancorp"},
    "WAL": {"cik": "0001212545", "name": "Western Alliance Bancorporation"},
    "EGBN": {"cik": "0001050441", "name": "Eagle Bancorp Inc"},
    "ZION": {"cik": "0000109380", "name": "Zions Bancorporation"},
    "CFG": {"cik": "0000759944", "name": "Citizens Financial Group"},
    "FLG": {"cik": "0001033012", "name": "Flagstar Bancorp Inc"},
}

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

# Google Trends cache
trends_cache = {
    "data": None,
    "timestamp": 0,
    "ttl": 86400  # 24 hours - trends don't change fast
}

# SEC filings cache
sec_cache = {
    "data": None,
    "timestamp": 0,
    "ttl": 1800  # 30 min - filings can drop anytime
}

# Track seen filings to avoid duplicate alerts
seen_filings = set()

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

def fetch_treasury_auctions():
    """Fetch recent Treasury auction results from TreasuryDirect"""
    now = time.time()
    
    # Return cached data if fresh  
    if trends_cache["data"] and (now - trends_cache["timestamp"]) < trends_cache["ttl"]:
        return trends_cache["data"]
    
    auction_data = {
        "auctions": [],
        "updated": None
    }
    
    try:
        # TreasuryDirect API for completed auctions
        url = "https://www.treasurydirect.gov/TA_WS/securities/auctioned?format=json&pagesize=15"
        
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        )
        
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            
            for record in data:
                # Only include notes/bonds (not bills) for meaningful BTC analysis
                sec_type = record.get("securityType", "")
                term = record.get("securityTerm", "")
                
                btc = record.get("bidToCoverRatio", "")
                high_yield = record.get("highYield", "") or record.get("highInvestmentRate", "")
                
                auction = {
                    "security_type": sec_type,
                    "security_term": term,
                    "auction_date": record.get("auctionDate", "")[:10] if record.get("auctionDate") else "",
                    "high_yield": high_yield,
                    "bid_to_cover": btc,
                    "type": record.get("type", ""),
                }
                auction_data["auctions"].append(auction)
                
    except Exception as e:
        print(f"[Treasury] Fetch error: {e}")
    
    auction_data["updated"] = time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())
    
    # Cache it (reusing trends_cache)
    trends_cache["data"] = auction_data  
    trends_cache["timestamp"] = now
    
    return auction_data

def fetch_sec_filings():
    """Fetch recent SEC filings for watchlist companies"""
    global seen_filings
    now = time.time()
    
    # Return cached data if fresh
    if sec_cache["data"] and (now - sec_cache["timestamp"]) < sec_cache["ttl"]:
        return sec_cache["data"]
    
    sec_data = {
        "filings": [],
        "updated": None
    }
    
    for ticker, info in SEC_WATCHLIST.items():
        try:
            cik = info["cik"].lstrip("0")  # API wants CIK without leading zeros for URL
            url = f"https://data.sec.gov/submissions/CIK{info['cik']}.json"
            
            req = urllib.request.Request(
                url,
                headers={
                    "User-Agent": "PROME-Dashboard research-alerts@example.com",
                    "Accept": "application/json"
                }
            )
            
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode())
                
                company_name = data.get("name", info["name"])
                recent = data.get("filings", {}).get("recent", {})
                
                forms = recent.get("form", [])
                dates = recent.get("filingDate", [])
                accessions = recent.get("accessionNumber", [])
                descriptions = recent.get("primaryDocument", [])
                
                # Get last 10 filings
                for i in range(min(10, len(forms))):
                    form_type = forms[i]
                    filing_date = dates[i]
                    accession = accessions[i]
                    doc = descriptions[i] if i < len(descriptions) else ""
                    
                    # Filter to important forms
                    important_forms = ["10-K", "10-Q", "8-K", "4", "SC 13G", "SC 13D", "DEF 14A"]
                    if not any(form_type.startswith(f) for f in important_forms):
                        continue
                    
                    filing_id = f"{ticker}_{accession}"
                    filing_url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession.replace('-', '')}/{doc}"
                    
                    filing = {
                        "ticker": ticker,
                        "company": company_name,
                        "form": form_type,
                        "date": filing_date,
                        "accession": accession,
                        "url": filing_url,
                        "id": filing_id
                    }
                    
                    sec_data["filings"].append(filing)
                    
                    # Alert on new filings (10-K, 10-Q, 8-K only)
                    if filing_id not in seen_filings and form_type in ["10-K", "10-Q", "8-K"]:
                        seen_filings.add(filing_id)
                        # Only alert if filing is from last 7 days
                        try:
                            from datetime import datetime, timedelta
                            filing_dt = datetime.strptime(filing_date, "%Y-%m-%d")
                            if datetime.now() - filing_dt < timedelta(days=7):
                                add_alert(
                                    alert_type="sec",
                                    severity="warning" if form_type == "8-K" else "info",
                                    message=f"{ticker} filed {form_type}: {company_name}",
                                    value=filing_date
                                )
                        except:
                            pass
                            
        except Exception as e:
            print(f"[SEC] {ticker} fetch error: {e}")
    
    # Sort by date descending
    sec_data["filings"].sort(key=lambda x: x["date"], reverse=True)
    sec_data["updated"] = time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())
    
    # Cache it
    sec_cache["data"] = sec_data
    sec_cache["timestamp"] = now
    
    return sec_data

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
        
        # API endpoint to get Treasury auction data
        if parsed.path == '/api/treasury':
            try:
                treasury_data = fetch_treasury_auctions()
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps(treasury_data).encode('utf-8'))
            except Exception as e:
                self.send_error(500, str(e))
            return
        
        # API endpoint to get SEC filings
        if parsed.path == '/api/sec':
            try:
                sec_data = fetch_sec_filings()
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps(sec_data).encode('utf-8'))
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
        
        # API endpoint to get agent statuses (dynamically parsed from STATUS.md)
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
                    ('CORAL', 'AGENTS/REGINALD/sub-agents/CORAL/STATUS.md'),
                    ('BROCK', 'AGENTS/REGINALD/sub-agents/BROCK/STATUS.md'),
                    ('CREED', 'AGENTS/REGINALD/CREED/STATUS.md'),
                ]
                
                for name, path in agents:
                    full_path = os.path.join(WORKSPACE, path)
                    status = 'UNKNOWN'
                    if os.path.exists(full_path):
                        with open(full_path, 'r') as f:
                            content = f.read(500)  # Read first 500 chars
                            # Check for status indicators (order matters - most severe first)
                            if '🔴' in content:
                                status = 'RED'
                            elif 'CRITICAL' in content.upper():
                                status = 'RED'
                            elif '🟠' in content:
                                status = 'ORANGE'
                            elif 'ELEVATED' in content.upper() or 'ORANGE' in content.upper():
                                status = 'ORANGE'
                            elif '🟡' in content:
                                status = 'YELLOW'
                            elif 'YELLOW' in content.upper():
                                status = 'YELLOW'
                            elif '🟢' in content:
                                status = 'GREEN'
                            elif 'GREEN' in content.upper():
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
