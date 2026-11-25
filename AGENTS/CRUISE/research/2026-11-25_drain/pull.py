"""2026-11-25 drain evidence: pinned raw closes (yfinance auto_adjust=False) for VX-CRU-01, and EDGAR
submissions for CCL, RCL, NCLH since 2026-11-16 (L715 reversal window closed Mon 11/23)."""
import json, subprocess, sys, urllib.request, yfinance as yf
sys.path.insert(0, "scripts")
from sec_contact import sec_ua
out = {"retrieved_at": subprocess.check_output(["date", "-Iseconds"]).decode().strip()}
d = yf.download(["CCL", "RCL", "NCLH", "SPY", "RSP"], start="2026-11-13", end="2026-11-26", auto_adjust=False, progress=False)
out["raw_close"] = {t: {str(i.date()): round(float(v), 4) for i, v in d["Close"][t].items()} for t in ["CCL", "RCL", "NCLH", "SPY", "RSP"]}
out["dividends_after_2026-11-13"] = {t: {str(i.date()): float(v) for i, v in yf.Ticker(t).dividends.items() if str(i.date()) > "2026-11-13"} for t in ["CCL", "RCL", "NCLH"]}
REF = 33.99
out["vx_cru_01"] = {k: {"close": v, "pct": round((v / REF - 1) * 100, 2),
    "cell": "GREEN(1)" if v > 30.591 else ("YELLOW(2)" if v > 27.192 else ("ORANGE(3)" if v > 22.0935 else "RED(4)"))}
    for k, v in out["raw_close"]["CCL"].items()}
ciks = {"CCL": "0000815097", "RCL": "0000884887", "NCLH": "0001513761"}
out["edgar"] = {}
for t, c in ciks.items():
    r = urllib.request.Request(f"https://data.sec.gov/submissions/CIK{c}.json", headers={"User-Agent": sec_ua(), "Accept-Encoding": "identity"})
    j = json.load(urllib.request.urlopen(r, timeout=30))
    f = j["filings"]["recent"]
    out["edgar"][t] = [(f["filingDate"][i], f["form"][i], f["accessionNumber"][i], f.get("items", [""] * 999)[i], f["primaryDocument"][i])
                       for i in range(len(f["form"])) if f["filingDate"][i] >= "2026-11-14"]
json.dump(out, open("AGENTS/CRUISE/research/2026-11-25_drain/evidence.json", "w"), indent=1)
print(out["retrieved_at"])
for k, v in out["vx_cru_01"].items(): print("CCL", k, v)
for t in ["RCL", "NCLH", "SPY", "RSP"]: print(t, out["raw_close"][t])
print(out["dividends_after_2026-11-13"])
for t, v in out["edgar"].items():
    print(t, len(v)); [print("   ", x) for x in v]
