import os,sys,json,csv,io,urllib.request
from pathlib import Path
HERE=Path(__file__).resolve().parent
os.environ['FORGE_CACHE_DIR']=str(HERE/'.cache')
sys.path.insert(0,'/home/willi/Research-workspace/FORGE/tools/market-data')
import fetch
fetch.AUDIT_LOG=HERE/'audit.txt'
for s in ('BAMLH0A0HYM2','BAMLH0A3HYC','VIXCLS','T5YIFR','SOFR'):
    try: print(s,fetch.fred_fetch(s,3)[:3],flush=True)
    except Exception as e: print(s,'ERR',type(e).__name__,flush=True)
for n in ('VIX','SKEW'):
    t=urllib.request.urlopen(urllib.request.Request(f'https://cdn.cboe.com/api/global/us_indices/daily_prices/{n}_History.csv',headers={'User-Agent':'Mozilla/5.0'}),timeout=30).read().decode('utf-8-sig')
    print(n,t.strip().split('\n')[-2:],flush=True)
for sym,cls in (('WAL','stocks'),('KRE','etf')):
    r=urllib.request.urlopen(urllib.request.Request(f'https://api.nasdaq.com/api/quote/{sym}/historical?assetclass={cls}&fromdate=2026-11-03&limit=3&todate=2026-11-06',headers={'User-Agent':'Mozilla/5.0','Accept':'application/json'}),timeout=25).read()
    print(sym,[(x['date'],x['close']) for x in json.loads(r)['data']['tradesTable']['rows'][:2]],flush=True)
r=fetch.price_fetch(['^VIX','KRE','WAL','HYG','SPY','QQQ','BZF27.NYM','CLZ26.NYM'])
print({k:(v.get('price'),v.get('change_pct')) if isinstance(v,dict) else v for k,v in r.items()},flush=True)
