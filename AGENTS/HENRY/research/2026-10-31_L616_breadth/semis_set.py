#!/usr/bin/env python3
"""L616 breadth — define the S&P 500 semiconductor set from yfinance industry labels.
Scope: S&P 500 members in the XLK (GICS Information Technology) file. Writes semis.json.
Yahoo industry labels are Yahoo's (Morningstar-style), not GICS sub-industries — stated.
Run: .venv/bin/python3 -I <this> <research_dir>
"""
import sys, os, csv, json, time
import yfinance as yf
R = sys.argv[1]
uni = list(csv.DictReader(open(os.path.join(R, "universe.csv"))))
it = [u["yf_ticker"] for u in uni if u["index"] == "SP500" and u["gics_sector"] == "Information Technology"]
lab, err = {}, []
for t in it:
    for a in range(3):
        try:
            info = yf.Ticker(t).info
            lab[t] = info.get("industry")
            break
        except Exception as e:  # noqa: BLE001
            time.sleep(2)
    else:
        err.append(t)
SEMI = {"Semiconductors", "Semiconductor Equipment & Materials"}
semis = sorted(t for t, i in lab.items() if i in SEMI)
json.dump({"source": "yfinance Ticker.info['industry'], pulled 2026-10-31", "scope": "S&P 500 GICS IT members",
           "labels": lab, "errors": err, "semis_sp500": semis}, open(os.path.join(R, "semis.json"), "w"), indent=1)
print(len(it), "IT names; labelled", len(lab), "errors", err)
print("semis:", len(semis), semis)
from collections import Counter
print(Counter(lab.values()).most_common())
