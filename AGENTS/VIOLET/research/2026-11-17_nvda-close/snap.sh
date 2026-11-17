#!/usr/bin/env bash
# Snapshot Cboe VIX complex quotes + CFE VX futures quotes + NVDA/ES (yfinance) with wall-clock stamp.
# Usage: bash snap.sh <label>   (writes snaps/<stamp>_<label>.json and prints a summary)
set -u
D="$(cd "$(dirname "$0")" && pwd)"; ROOT="$(git -C "$D" rev-parse --show-toplevel)"
STAMP=$(date +%Y%m%dT%H%M%S%z); OUT="$D/snaps/${STAMP}_${1:-snap}"
mkdir -p "$OUT"
for s in _VIX _VIX9D _VIX3M _VIX6M _VVIX _SKEW _COR1M; do
  curl -sL "https://cdn.cboe.com/api/global/delayed_quotes/quotes/$s.json" > "$OUT/$s.json"; done
curl -sL "https://www.cboe.com/us/futures/api/get_quotes_combined/?symbol=VX&rootsymbol=null" > "$OUT/VX_futures.json"
"$ROOT/.venv/bin/python3" - "$OUT" <<'PY' 2>/dev/null
import sys,json,os
o=sys.argv[1]
print("fetched_at", os.path.basename(o))
for s in ['_VIX','_VIX9D','_VIX3M','_VIX6M','_VVIX','_SKEW','_COR1M']:
    try:
        d=json.load(open(f"{o}/{s}.json"))['data']
        print(f"{s:7} {d.get('current_price')} prev {d.get('prev_day_close')} hi {d.get('high')} lo {d.get('low')} ltt {d.get('last_trade_time')}")
    except Exception as e: print(s,'ERR',e)
try:
    for r in json.load(open(f"{o}/VX_futures.json"))['data']:
        if r['symbol'] in ('VX/X6','VX/Z6','VX/F7','VX/G7') or (r['symbol'].startswith('VX47') ):
            print(f"{r['symbol']:9} exp {r['expiration']} last {r['last_price']} hi {r['high']} lo {r['low']} prev_close {r['prev_close']} settle {r['settlement']} prev_settle {r['prev_settlement']} vol {r['volume']}")
except Exception as e: print('VX ERR',e)
import yfinance as yf
out={}
for t in ['NVDA','ES=F']:
    try:
        h=yf.Ticker(t).history(period='1d',interval='1m',prepost=True)
        out[t]=(str(h.index[-1]), round(float(h['Close'].iloc[-1]),2))
    except Exception as e: out[t]=('ERR',str(e))
print("yfinance", out)
json.dump(out,open(f"{o}/yf.json","w"))
PY
