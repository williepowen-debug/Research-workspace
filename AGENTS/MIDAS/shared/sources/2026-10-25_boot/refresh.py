"""One dated catch-up capture; no grading or canonical-state writes."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import urllib.request
import pandas as pd
import yfinance as yf

HERE = Path(__file__).resolve().parent
out = {"captured_at": datetime.now(timezone.utc).isoformat(), "series": {}, "sources": {}}
tickers = ["GLD", "SLV", "PPLT", "PALL", "CPER", "GCZ26.CMX", "SIZ26.CMX",
           "PLF27.NYM", "PAZ26.NYM", "HGZ26.CMX", "DX-Y.NYB", "^GSPC", "^VIX"]
for ticker in tickers:
    try:
        frame = yf.Ticker(ticker).history(start="2025-01-01", end="2026-10-24", auto_adjust=False)
        assert not frame.empty, ticker
        frame.index = pd.to_datetime(frame.index).tz_localize(None).normalize()
        frame.to_csv(HERE / (ticker.replace("^", "") + ".csv"))
        s = frame.Close.dropna()
        assert str(s.index[-1].date()) == "2026-10-23", (ticker, s.index[-1])
        row = {"date": "2026-10-23", "close": float(s.iloc[-1]),
               "day_pct": float(100 * (s.iloc[-1] / s.iloc[-2] - 1)),
               "oct19_pct": float(100 * (s.iloc[-1] / s.loc["2026-10-19"] - 1))}
        if ticker in ["SLV", "PPLT", "PALL"]:
            d200 = 100 * (s / s.rolling(200).mean() - 1)
            dd252 = 100 * (s / s.rolling(252).max() - 1)
            ts = {"SLV": [-5, -12, -20], "PPLT": [-10, -15, -20], "PALL": [-12, -20, -25]}[ticker]
            row.update(d200=float(d200.iloc[-1]), dd252=float(dd252.iloc[-1]),
                       T_level=max([1] + [i for i, v in enumerate(ts, 2) if d200.iloc[-1] <= v]),
                       S_level=3 if d200.iloc[-1] >= 40 else 2 if d200.iloc[-1] >= 30 else 1,
                       crossings_since_oct22={"T": [v for v in ts if d200.iloc[-2] > v >= d200.iloc[-1]],
                           "C": [v for v in ([-20, -30] if ticker == "PPLT" else [-20, -30, -40])
                                 if dd252.iloc[-2] > v >= dd252.iloc[-1]]})
        if ".CMX" in ticker or ".NYM" in ticker:
            row["basis"] = "Newest vendor row: diagnostic ONLY; excluded by standing futures guard; uncertified settlement"
        else:
            row["basis"] = "Yahoo MIRROR unadjusted completed daily Close"
        out["series"][ticker] = row
    except Exception as exc:
        out["series"][ticker] = {"error": str(exc)}

urls = {
 "GLD_issuer_archive.xlsx": "https://api.spdrgoldshares.com/api/v1/historical-archive?exchange=NYSE&lang=en&product=gld",
 "treasury_real_curve.csv": "https://home.treasury.gov/resource-center-data-chart-center/interest-rates/pages/xml?data=daily_treasury_real_yield_curve&field_tdr_date_value=2026",
 "teck_hvc.html": "https://www.teck.com/news/news-releases/2026/teck-provides-update-on-highland-valley-copper-operations",
}
for filename, url in urls.items():
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=35) as response:
            body = response.read()
        (HERE / filename).write_bytes(body)
        out["sources"][filename] = {"url": url, "bytes": len(body), "sha256": hashlib.sha256(body).hexdigest()}
    except Exception as exc:
        out["sources"][filename] = {"url": url, "error": str(exc)}
(HERE / "capture.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
