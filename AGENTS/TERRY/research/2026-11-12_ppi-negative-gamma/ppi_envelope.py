import os, json, urllib.request, statistics as st
from pathlib import Path
envp=Path("/home/willi/Research-workspace/FORGE/tools/market-data/.env")
for line in envp.read_text().splitlines():
    if "=" in line and not line.strip().startswith("#"):
        k,v=line.split("=",1); os.environ.setdefault(k.strip(),v.strip().strip('"'))
key=os.environ["FRED_API_KEY"]
url=f"https://api.stlouisfed.org/fred/release/dates?release_id=46&realtime_start=2023-01-01&realtime_end=2026-11-12&sort_order=asc&include_release_dates_with_no_data=false&api_key={key}&file_type=json"
d=json.load(urllib.request.urlopen(url,timeout=30))
dates=[x["date"] for x in d["release_dates"]]
print("FRED release 46 dates:",len(dates),dates[0],"..",dates[-1])
import yfinance as yf
h=yf.Ticker("SPY").history(start="2022-12-15",end="2026-11-13",interval="1d",auto_adjust=False)
h.index=h.index.strftime("%Y-%m-%d")
idx=list(h.index)
print("SPY bars:",len(idx))
rows=[]
allcc=[]
for i in range(1,len(idx)):
    pc=h["Close"].iloc[i-1]; o=h["Open"].iloc[i]; c=h["Close"].iloc[i]; hi=h["High"].iloc[i]; lo=h["Low"].iloc[i]
    rec=(idx[i],abs(o/pc-1)*100,abs(c/pc-1)*100,abs(c/o-1)*100,(hi-lo)/pc*100)
    allcc.append(rec)
    if idx[i] in dates: rows.append(rec)
print("PPI days matched:",len(rows),"of",len(dates))
def summ(name,vals):
    v=sorted(vals); n=len(v)
    print(f"{name}: n={n} median={st.median(v):.2f}% mean={st.mean(v):.2f}% p75={v[int(.75*n)]:.2f}% p90={v[int(.9*n)]:.2f}% max={v[-1]:.2f}%  share>=0.73%={sum(x>=0.73 for x in v)/n:.0%}")
for j,lab in [(1,"gap |open/prevclose|"),(2,"close-to-close |c/pc|"),(3,"open-to-close |c/o|"),(4,"range (h-l)/pc")]:
    summ("PPI "+lab,[r[j] for r in rows]); summ("ALL "+lab,[r[j] for r in allcc])
print("last 8 PPI days:")
for r in rows[-8:]: print("  ",r[0],"gap %.2f cc %.2f oc %.2f range %.2f"%r[1:])
