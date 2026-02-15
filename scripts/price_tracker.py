#!/usr/bin/env python3
"""
Price Tracker — Real-time data feeds for key tickers and metrics.

Fetches:
- Stock prices (CVNA, ALLY, KRE, SSB, IWM, HYG)
- Treasury yields (10Y, 30Y)
- VIX
- Economic data from FRED

PREREQUISITES:
  pip install yfinance           # For stock prices
  export FRED_API_KEY=xxx        # For FRED data (free at fred.stlouisfed.org)

Usage: 
  python3 scripts/price_tracker.py              # Full update
  python3 scripts/price_tracker.py --prices     # Just prices
  python3 scripts/price_tracker.py --fred       # Just FRED data

Output: Updates workspace/data/market_snapshot.json
"""

import json
import sys
from datetime import datetime
from pathlib import Path

WORKSPACE = Path(__file__).parent.parent

# Tickers to track
TICKERS = {
    # Position-related
    'KRE': 'SPDR S&P Regional Banking ETF',
    'SSB': 'SouthState Corp',
    'IWM': 'iShares Russell 2000 ETF',
    'HYG': 'iShares iBoxx High Yield Corporate Bond ETF',
    
    # OTTO-related
    'CVNA': 'Carvana',
    'ALLY': 'Ally Financial',
    'CACC': 'Credit Acceptance Corp',
    
    # Market
    '^VIX': 'CBOE Volatility Index',
    '^TNX': '10-Year Treasury Yield',
    '^TYX': '30-Year Treasury Yield',
    'SPY': 'S&P 500 ETF',
    'QQQ': 'Nasdaq 100 ETF',
    
    # Japan
    'FXY': 'Invesco CurrencyShares Japanese Yen Trust',
    'EWJ': 'iShares MSCI Japan ETF',
}

# FRED series to track
FRED_SERIES = {
    'ICSA': 'Initial Claims',
    'CCSA': 'Continued Claims',
    'UNRATE': 'Unemployment Rate',
    'CPIAUCSL': 'CPI',
    'DFF': 'Fed Funds Rate',
    'DGS10': '10Y Treasury',
    'BAMLH0A0HYM2': 'HY OAS',
}

def fetch_yahoo_price(ticker):
    """Fetch current price from Yahoo Finance using yfinance library."""
    try:
        import yfinance as yf
        
        stock = yf.Ticker(ticker)
        data = stock.history(period='1d')
        
        if not data.empty:
            return float(data['Close'].iloc[-1])
    except ImportError:
        print("  yfinance not installed. Run: pip install yfinance", file=sys.stderr)
        return None
    except Exception as e:
        print(f"  Error fetching {ticker}: {e}", file=sys.stderr)
    
    return None

def fetch_fred_data(series_id, api_key=None):
    """Fetch latest value from FRED (requires API key for full functionality)."""
    # Without API key, return None (user needs to set up FRED_API_KEY)
    if not api_key:
        return None
    
    try:
        import urllib.request
        import json as j
        
        url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={api_key}&file_type=json&sort_order=desc&limit=1"
        
        with urllib.request.urlopen(url, timeout=10) as response:
            data = j.loads(response.read().decode('utf-8'))
        
        if data.get('observations'):
            obs = data['observations'][0]
            return {
                'value': float(obs['value']) if obs['value'] != '.' else None,
                'date': obs['date']
            }
    except Exception as e:
        print(f"  Error fetching FRED {series_id}: {e}", file=sys.stderr)
    
    return None

def main():
    import argparse
    import os
    
    parser = argparse.ArgumentParser(description='Fetch market data')
    parser.add_argument('--prices', action='store_true', help='Fetch stock prices only')
    parser.add_argument('--fred', action='store_true', help='Fetch FRED data only')
    args = parser.parse_args()
    
    fetch_prices = not args.fred or args.prices
    fetch_fred = not args.prices or args.fred
    
    # Output directory
    data_dir = WORKSPACE / 'data'
    data_dir.mkdir(exist_ok=True)
    
    snapshot = {
        'timestamp': datetime.now().isoformat(),
        'prices': {},
        'fred': {},
    }
    
    # Fetch stock prices
    if fetch_prices:
        print("Fetching stock prices...")
        for ticker, name in TICKERS.items():
            price = fetch_yahoo_price(ticker)
            if price:
                snapshot['prices'][ticker] = {
                    'price': price,
                    'name': name,
                }
                print(f"  {ticker}: ${price:.2f}")
            else:
                print(f"  {ticker}: FAILED")
    
    # Fetch FRED data
    if fetch_fred:
        fred_api_key = os.environ.get('FRED_API_KEY')
        if fred_api_key:
            print("\nFetching FRED data...")
            for series_id, name in FRED_SERIES.items():
                data = fetch_fred_data(series_id, fred_api_key)
                if data:
                    snapshot['fred'][series_id] = {
                        **data,
                        'name': name,
                    }
                    print(f"  {series_id}: {data['value']}")
        else:
            print("\nFRED_API_KEY not set — skipping FRED data")
            print("  Get a free key at: https://fred.stlouisfed.org/docs/api/api_key.html")
    
    # Save snapshot
    output_file = data_dir / 'market_snapshot.json'
    with open(output_file, 'w') as f:
        json.dump(snapshot, f, indent=2)
    
    print(f"\nSnapshot saved to: {output_file}")
    
    # Also output key metrics for quick view
    print("\n=== KEY METRICS ===")
    if 'CVNA' in snapshot['prices']:
        print(f"CVNA: ${snapshot['prices']['CVNA']['price']:.2f}")
    if 'KRE' in snapshot['prices']:
        print(f"KRE:  ${snapshot['prices']['KRE']['price']:.2f}")
    if '^VIX' in snapshot['prices']:
        print(f"VIX:  {snapshot['prices']['^VIX']['price']:.2f}")

if __name__ == '__main__':
    main()
