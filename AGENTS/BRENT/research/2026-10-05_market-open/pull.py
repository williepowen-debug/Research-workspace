"""One-sitting data capture; diagnostic only, no registered state mutations."""
import concurrent.futures as cf
import json, sys
from pathlib import Path
from datetime import datetime, timezone
base=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(base/'scripts'))
import yfinance as yf
from thresholds import quote_record
from composites import tanker_snapshot, checked_legs
from eia_weekly import fetch_live_metrics
if '--supplemental' in sys.argv:
 from thresholds import fred_fetch
 from instrument_check import BROWSER_UA
 import urllib.request
 series=['DCOILBRENTEU','DCOILWTICO','DHHNGSP','GASREGW','GASDESW','BAMLH0A0HYM2']
 result={'retrieved_utc':datetime.now(timezone.utc).isoformat(),'fred':dict(cf.ThreadPoolExecutor(max_workers=6).map(lambda s:(s,fred_fetch(s,3)),series))}
 try:
  req=urllib.request.Request('https://agsi.gie.eu/api/data/eu',headers={'User-Agent':BROWSER_UA})
  with urllib.request.urlopen(req,timeout=30) as r: body=json.load(r)
  if body.get('error') or not body.get('total') or not body.get('data'): raise ValueError('GIE empty/error payload')
  result['gie']={'source':'https://agsi.gie.eu/api/data/eu','latest':body['data'][:3]}
 except Exception as e: result['gie']={'error':str(e)}
 p=Path(__file__).with_name('supplemental.json');p.write_text(json.dumps(result,indent=2,default=str));print(json.dumps(result,indent=2,default=str));sys.exit()
symbols=['BZZ26.NYM','BZF27.NYM','BZG27.NYM','CLX26.NYM','CLZ26.NYM','HOX26.NYM','HOZ26.NYM','RBX26.NYM','NGX26.NYM','USO','VLO','MPC','XLE','STNG','FRO','DHT','LNG','VG']
def pull(sym):
 try:
  q=yf.Ticker(sym).info
  r=quote_record(q)
  r['expireDate']=q.get('expireDate')
  r['bid']=q.get('bid');r['ask']=q.get('ask')
  return sym,r
 except Exception as e: return sym,{'state':'UNGRADED','error':type(e).__name__+': '+str(e)}
quotes=dict(cf.ThreadPoolExecutor(max_workers=6).map(pull,symbols))
result={'retrieved_utc':datetime.now(timezone.utc).isoformat(),'quotes':quotes,'tanker':tanker_snapshot(quotes),'spreads':{}}
for name,legs,weights in [('brent_dec_feb',['BZZ26.NYM','BZG27.NYM'],[1,-1]),('brent_dec_jan',['BZZ26.NYM','BZF27.NYM'],[1,-1]),('dec_wti_brent',['CLZ26.NYM','BZZ26.NYM'],[1,-1]),('nov_ulsd_wti',['HOX26.NYM','CLX26.NYM'],[42,-1]),('dec_ulsd_wti',['HOZ26.NYM','CLZ26.NYM'],[42,-1]),('nov_rbob_wti',['RBX26.NYM','CLX26.NYM'],[42,-1])]:
 problems,stamps=checked_legs(quotes,legs)
 result['spreads'][name]={'legs':legs,'problems':problems,'value':None if problems else sum(quotes[s]['price']*w for s,w in zip(legs,weights)),'basis':'vendor timestamped quotes, not settlement; maximum skew 300s'}
try: result['eia']=fetch_live_metrics()
except Exception as e: result['eia']={'error':str(e)}
try:
 calls=yf.Ticker('USO').option_chain('2026-10-09').calls
 result['uso_oct09_150c']=calls[calls.strike==150].to_dict(orient='records')
except Exception as e: result['uso_oct09_150c']={'error':str(e)}
p=Path(__file__).with_name('snapshot.json');p.write_text(json.dumps(result,indent=2,default=str))
print(p)
for sym,q in quotes.items():print(sym,q.get('price'),q.get('chg'),q.get('date'),q.get('expireDate'),q.get('state'),q.get('reason') or q.get('error') or '')
print(json.dumps({k:result[k] for k in ['spreads','uso_oct09_150c','eia']},indent=2,default=str))
