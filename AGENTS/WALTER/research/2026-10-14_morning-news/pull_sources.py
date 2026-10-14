"""Bounded read-only morning source pull; all saved output is WALTER-owned."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import importlib.util
import json
import datetime
import requests

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
URLS = {
    "cpi": "https://www.bls.gov/news.release/cpi.nr0.htm",
    "realearnings": "https://www.bls.gov/news.release/realer.nr0.htm",
    "iea": "https://www.iea.org/reports/oil-market-report-october-2026",
    "asml": "https://www.asml.com/en/news/press-releases/2026/q3-2026-financial-results",
    "bac": "https://investor.bankofamerica.com/regulatory-and-other-filings/select-sec-filings/content/0000070858-26-000481/bac09302026ex991.htm",
    "ms": "https://www.morganstanley.com/about-us-ir/shareholder/3q2026.pdf",
    "skew": "https://cdn.cboe.com/api/global/us_indices/daily_prices/SKEW_History.csv",
    "wages_chart": "https://pbs.twimg.com/media/HUmO5sAWkAED2o5.png",
    "cpi_chart1": "https://pbs.twimg.com/media/HUl7KyBXEAAj8gb.png",
    "cpi_chart2": "https://pbs.twimg.com/media/HUl7UUDWMAAecO6.png",
}

def pull(item):
    key, url = item
    try:
        r = requests.get(url, timeout=25, headers={"User-Agent": "Mozilla/5.0"})
        suffix = ".png" if key.endswith("chart") or key.startswith("cpi_chart") else ".pdf" if key == "ms" else ".csv" if key == "skew" else ".html"
        (OUT / (key + suffix)).write_bytes(r.content)
        return {"key": key, "url": url, "status": r.status_code, "bytes": len(r.content)}
    except Exception as e:
        return {"key": key, "url": url, "error": str(e)}

results = list(ThreadPoolExecutor(max_workers=8).map(pull, URLS.items()))
(OUT / "http-receipt.json").write_text(json.dumps({"retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "results": results}, indent=2))
print(json.dumps(results, indent=2))
if any("Failed to resolve" in r.get("error", "") for r in results):
    raise SystemExit(2)
spec = importlib.util.spec_from_file_location("walter_morning_fetch", ROOT / "FORGE/tools/market-data/fetch.py")
fetch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fetch)
series = ["BAMLH0A0HYM2", "BAMLH0A3HYC", "VIXCLS", "T5YIFR", "DFII10", "DGS30", "DGS10", "DGS5", "DGS20", "DGS2", "T10YIE", "SOFR", "IORB", "ICSA"]
def fred(s):
    try:
        return s, fetch.fred_fetch(s, limit=9)
    except Exception as e:
        return s, {"error": str(e)}
market = {"retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "fred": dict(ThreadPoolExecutor(max_workers=7).map(fred, series))}
try:
    market["prices"] = fetch.price_fetch(["QQQ", "SPY", "KRE", "WAL", "OZK", "^VIX", "USO", "TLT", "BZZ26", "RBZ26", "HOZ26"])
except Exception as e:
    market["prices"] = {"error": str(e)}
(OUT / "market.json").write_text(json.dumps(market, indent=2, default=str))
print("Saved market.json; dates and contract identities require review.")
