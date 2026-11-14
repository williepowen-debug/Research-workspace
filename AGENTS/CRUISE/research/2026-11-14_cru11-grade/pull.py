"""CRU-11 grade evidence pull (L606). Pinned source: yfinance download(auto_adjust=False)["Adj Close"];
cross-check: FORGE/tools/market-data/fetch.py price --history (same vendor, Yahoo). Also CCL raw closes for WQ-670 re-read."""
import json, subprocess, datetime, yfinance as yf
out = {"retrieved_at": subprocess.check_output(["date", "-Iseconds"]).decode().strip()}
d = yf.download(["NCLH", "RCL", "CCL", "SPY"], start="2026-09-30", end="2026-11-15", auto_adjust=False, progress=False)
out["yfinance_adj_close"] = {t: {str(i.date()): round(float(v), 4) for i, v in d["Adj Close"][t].items()} for t in ["NCLH", "RCL"]}
out["yfinance_raw_close"] = {t: {str(i.date()): round(float(v), 4) for i, v in d["Close"][t].items()} for t in ["NCLH", "RCL", "CCL", "SPY"]}
out["dividends_after_2026-09-30"] = {t: {str(i.date()): float(v) for i, v in yf.Ticker(t).dividends.items() if str(i.date()) > "2026-09-30"} for t in ["NCLH", "RCL", "CCL"]}
fx = json.loads(subprocess.check_output(["python3", "FORGE/tools/market-data/fetch.py", "price", "NCLH", "RCL", "CCL", "--history", "40", "--json"], stderr=subprocess.DEVNULL))
out["fetch_py_close"] = {t: {r["date"]: r["close"] for r in fx[t]["history"]} for t in ["NCLH", "RCL", "CCL"]}
a = out["yfinance_adj_close"]; B, E = "2026-10-02", "2026-11-13"
n = a["NCLH"][E] / a["NCLH"][B] - 1; r = a["RCL"][E] / a["RCL"][B] - 1
f = out["fetch_py_close"]; nf = f["NCLH"][E] / f["NCLH"][B] - 1; rf = f["RCL"][E] / f["RCL"][B] - 1
sessions = [k for k in a["NCLH"] if B < k <= E]
out["grade"] = {"base": B, "window_close": E, "in_window_sessions_after_base": len(sessions),
  "NCLH_TR_cum_pp": round(n * 100, 4), "RCL_TR_cum_pp": round(r * 100, 4), "spread_pp": round((n - r) * 100, 4),
  "fetch_py_spread_pp": round((nf - rf) * 100, 4), "threshold_pp": -5.0,
  "verdict": "CONFIRMED" if (n - r) * 100 <= -5 else "FAILED"}
json.dump(out, open("AGENTS/CRUISE/research/2026-11-14_cru11-grade/evidence.json", "w"), indent=1)
print(json.dumps(out["grade"], indent=1)); print(out["dividends_after_2026-09-30"]); print(out["retrieved_at"])
