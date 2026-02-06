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

# Price cache (avoid hammering APIs)
price_cache = {
    "data": None,
    "timestamp": 0,
    "ttl": 300  # 5 minutes
}

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

def main():
    # Bind to all interfaces so Tailscale can reach it
    with socketserver.TCPServer(("0.0.0.0", PORT), DashboardHandler) as httpd:
        print(f"PROME Dashboard running at http://127.0.0.1:{PORT}")
        print(f"Workspace: {WORKSPACE}")
        print("Press Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down...")

if __name__ == "__main__":
    main()
