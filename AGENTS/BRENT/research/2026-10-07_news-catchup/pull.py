"""BRENT 2026-10-07 news-catchup reader: vendor quotes (yfinance, NOT CME settles) + Nov ULSD crack
settle-window proxy (14:28-14:30 ET 1-min volume-weighted, HOX26*42 - CLX26). Writes snapshot.json beside this file."""
import json, datetime, pathlib
import yfinance as yf, pandas as pd
out = {"retrieved_et": datetime.datetime.now(datetime.timezone.utc).astimezone(__import__("zoneinfo").ZoneInfo("America/New_York")).isoformat(), "quotes": {}, "crack_window": {}}
for t in ["BZZ26.NYM", "BZF27.NYM", "BZG27.NYM", "CLX26.NYM", "CLZ26.NYM", "HOX26.NYM", "RBX26.NYM", "USO", "VLO"]:
    try:
        h = yf.Ticker(t).history(period="1d", interval="1m", auto_adjust=False).tz_convert("America/New_York")
        out["quotes"][t] = {"last": round(float(h.Close.iloc[-1]), 4), "bar_et": h.index[-1].isoformat()}
    except Exception as e:
        out["quotes"][t] = {"error": str(e)}
ho = yf.Ticker("HOX26.NYM").history(period="5d", interval="1m", auto_adjust=False).tz_convert("America/New_York")
cl = yf.Ticker("CLX26.NYM").history(period="5d", interval="1m", auto_adjust=False).tz_convert("America/New_York")
def vw(df):
    return float((df.Close * df.Volume).sum() / df.Volume.sum()) if df.Volume.sum() > 0 else float(df.Close.mean())
for d in sorted(set(ho.index.strftime("%Y-%m-%d"))):
    hw = ho[ho.index.strftime("%Y-%m-%d") == d].between_time("14:28", "14:30")
    cw = cl[cl.index.strftime("%Y-%m-%d") == d].between_time("14:28", "14:30")
    if len(hw) and len(cw):
        out["crack_window"][d] = {"HO_vwap": round(vw(hw), 4), "CL_vwap": round(vw(cw), 3), "crack": round(vw(hw) * 42 - vw(cw), 2), "bars": [len(hw), len(cw)]}
p = pathlib.Path(__file__).with_name("snapshot.json")
p.write_text(json.dumps(out, indent=1))
print(json.dumps(out, indent=1))
