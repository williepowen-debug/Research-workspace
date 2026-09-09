import json, urllib.request, urllib.parse
from pathlib import Path
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from concurrent.futures import ThreadPoolExecutor
root=Path('/home/willi/Research-workspace/AGENTS/BRENT/research/2026-09-09_morning')
root.mkdir(exist_ok=True)
et=ZoneInfo('America/New_York')
symbols=['BZX26.NYM','BZZ26.NYM','BZF27.NYM','CLV26.NYM','CLX26.NYM','HOX26.NYM','RBX26.NYM','USO','XLE','XOP','EOG','XOM','CVX','LNG','STNG','NG=F']
def fetch(symbol):
 url='https://query1.finance.yahoo.com/v8/finance/chart/'+urllib.parse.quote(symbol,safe='')+'?range=5d&interval=1d'
 row={'symbol':symbol,'source_url':url,'retrieved_at':datetime.now(timezone.utc).isoformat()}
 try:
  raw=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=25).read()
  (root/(symbol.replace('=','_')+'.json')).write_bytes(raw)
  data=json.loads(raw)['chart']['result'][0];meta=data['meta'];q=data['indicators']['quote'][0]
  bars=[{'date':datetime.fromtimestamp(t,et).strftime('%Y-%m-%d'),'close':c,'timestamp':t} for t,c in zip(data.get('timestamp',[]),q.get('close',[])) if c is not None]
  quote_dt=datetime.fromtimestamp(meta['regularMarketTime'],et)
  prior=[b for b in bars if b['date']<quote_dt.strftime('%Y-%m-%d')]
  prev=prior[-1] if prior else None
  row.update(name=meta.get('shortName') or meta.get('longName'),exchange=meta.get('exchangeName'),currency=meta.get('currency'),price=meta.get('regularMarketPrice'),quote_time_et=quote_dt.isoformat(),prior_daily_bar=prev,chart_previous_close=meta.get('chartPreviousClose'),previous_close=meta.get('previousClose'),bars=bars)
  if prev: row['change_pct_vs_prior_vendor_bar']=(row['price']/prev['close']-1)*100
 except Exception as e: row['error']=str(e)
 return row
with ThreadPoolExecutor(max_workers=6) as pool: rows=list(pool.map(fetch,symbols))
(root/'quotes.json').write_text(json.dumps(rows,indent=2))
for r in rows:
 print(json.dumps({k:v for k,v in r.items() if k not in ('bars','source_url')},ensure_ascii=False))
