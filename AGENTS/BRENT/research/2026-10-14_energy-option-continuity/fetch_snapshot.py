"""Bounded vendor screening snapshot; no owner caches or trading actions."""
import datetime as dt
import json
import pathlib
import yfinance as yf

OUT = pathlib.Path(__file__).resolve().parent
ASOF = dt.date(2026, 10, 14)
result = {"retrieved_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
          "source": "Yahoo Finance via yfinance; screening only; bid/ask timestamps unavailable",
          "symbols": {}}
for symbol in ["USO", "BNO", "VLO", "MPC", "PSX"]:
    item = {}
    result["symbols"][symbol] = item
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.get_info()
        item["quote"] = {key: info.get(key) for key in [
            "regularMarketPrice", "regularMarketPreviousClose", "regularMarketTime",
            "regularMarketChangePercent", "bid", "ask", "bidSize", "askSize",
            "exchangeDataDelayedBy", "currency", "marketState"]}
        expiries = list(ticker.options or [])
        item["expiries"] = expiries
        eligible = [exp for exp in expiries if 60 <= (dt.date.fromisoformat(exp)-ASOF).days <= 90]
        # One eligible expiry per instrument; Jan15 BNO is comparison only if no eligible expiry.
        selected = ["2026-12-18"] if "2026-12-18" in eligible else eligible[:1]
        if symbol == "BNO" and not selected and "2027-01-15" in expiries:
            selected = ["2027-01-15"]
        item["eligible_expiries_60_90_dte"] = eligible
        item["chains"] = {}
        for expiry in selected:
            chain = ticker.option_chain(expiry)
            item["chains"][expiry] = json.loads(chain.calls.to_json(orient="records", date_format="iso"))
        print(symbol, "spot", item["quote"], "eligible", eligible, "selected", selected, flush=True)
    except Exception as exc:
        item["error"] = repr(exc)
        print(symbol, "ERROR", repr(exc), flush=True)
    (OUT / "vendor-snapshot.json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n")
