"""One-session evidence capture for Will's existing credit follow-through, not a monitor."""
import sys,json,concurrent.futures,datetime, pathlib
sys.path.insert(0,'FORGE/tools/market-data')
from fetch import fred_fetch_vintage
P=pathlib.Path(__file__).parent
ids=['BAMLH0A0HYM2','BAMLC0A0CM','BAMLH0A1HYBB','BAMLH0A2HYB','BAMLH0A3HYC','SOFR','SOFR1','SOFR75','SOFR99','IORB','EFFR','EFFR75','RPONTTLD','WRESBAL','WTREGEN']
def one(s):
 r=fred_fetch_vintage(s,limit=40,basis='first-published',observation_start='2026-09-01')
 (P/(s+'.json')).write_text(json.dumps(r,indent=2)+'\n')
 return s,{k:r.get(k) for k in ['error','short','missing','under_limit']},r['rows'][:7]
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as e:
 for result in e.map(one,ids): print(json.dumps(result),flush=True)
import yfinance as yf
px=yf.download(['CRWV','IREN','APLD','NBIS','^MOVE','^VIX'],start='2026-09-01',end='2026-11-05',auto_adjust=False,progress=False)['Close']
eq={t:{d.strftime('%Y-%m-%d'):float(v) for d,v in px[t].dropna().items()} for t in px.columns}
(P/'raw_closes.json').write_text(json.dumps(eq,indent=2)+'\n')
(P/'capture_time.txt').write_text(datetime.datetime.now(datetime.timezone.utc).isoformat()+'\n')
print('raw closes saved', {t:max(v) for t,v in eq.items()},flush=True)
