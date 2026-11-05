"""One-session capture for Will's 2026-11-05 09:42 ET catch-up, not a monitor."""
import sys,json,concurrent.futures,datetime,pathlib
sys.path.insert(0,'FORGE/tools/market-data')
from fetch import fred_fetch_vintage
P=pathlib.Path(__file__).parent
ids=['BAMLH0A0HYM2','BAMLC0A0CM','BAMLC0A4CBBB','BAMLH0A1HYBB','BAMLH0A2HYB','BAMLH0A3HYC','SOFR','SOFR1','SOFR75','SOFR99','IORB','EFFR','EFFR75','RPONTTLD','WRESBAL','WTREGEN','PDPOSCSBND-G10','PDPOSCSBND-G5L10']
def one(s):
 try:
  r=fred_fetch_vintage(s,limit=40,basis='first-published',observation_start='2026-09-01')
 except Exception as e:
  return s,{'exc':repr(e)},[]
 (P/(s+'.json')).write_text(json.dumps(r,indent=2)+'\n')
 return s,{k:r.get(k) for k in ['error','short','missing','under_limit']},r.get('rows',[])[:3]
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as e:
 for x in e.map(one,ids): print(json.dumps(x),flush=True)
import yfinance as yf
px=yf.download(['CRWV','IREN','APLD','NBIS','^MOVE','^VIX'],start='2026-09-01',auto_adjust=False,progress=False)['Close']
eq={t:{d.strftime('%Y-%m-%d'):float(v) for d,v in px[t].dropna().items()} for t in px.columns}
(P/'raw_closes.json').write_text(json.dumps(eq,indent=2)+'\n')
(P/'capture_time.txt').write_text(datetime.datetime.now(datetime.timezone.utc).isoformat()+'\n')
print({t:(max(v),v[max(v)]) for t,v in eq.items()},flush=True)
