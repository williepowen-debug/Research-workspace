import json, sys, math
import yfinance as yf
import numpy as np
gov=["KSS","NWL","NCLH","AMC","JBLU"]; sens=["HTZ","WOOF","HLF","BALY"]
tick=["SPY"]+gov+sens
data={}
for t in tick:
    h=yf.Ticker(t).history(start="2026-02-20", end="2026-10-15", auto_adjust=True).sort_index()
    data[t]={d.strftime("%Y-%m-%d"):float(c) for d,c in zip(h.index,h["Close"]) if not math.isnan(c)}
json.dump(data,open(sys.argv[1],"w"))
for t in tick:
    ds=sorted(data[t]); print(t,len(ds),ds[0] if ds else None,ds[-1] if ds else None)
