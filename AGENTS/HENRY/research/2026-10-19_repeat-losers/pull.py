import requests,json,pathlib,concurrent.futures,datetime,time,shutil
P=pathlib.Path(__file__).resolve().parent;root=P.parents[3]
u=root/'AGENTS/WALTER/research/2026-10-19_breadth/universe.json';sector=root/'AGENTS/HENRY/research/2026-10-19_catchup/quality-screen-stocks.csv'
shutil.copyfile(u,P/'universe.json');shutil.copyfile(sector,P/'sector-map.csv')
d=json.loads(u.read_text());print(type(d['rows'][0]),d['rows'][0],flush=True)
symbols=[r['ticker'] if 'ticker' in r else r['symbol'] for r in d['rows']];symbols+=['SPY','RSP','QQQ','QQEW','IWM','XLB','XLC','XLE','XLF','XLI','XLK','XLP','XLRE','XLU','XLV','XLY'];symbols=list(dict.fromkeys(symbols))
def get(s):
 url='https://query1.finance.yahoo.com/v8/finance/chart/'+s+'?range=1y&interval=1d&events=div%2Csplits&includeAdjustedClose=true';stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
 try:
  r=requests.get(url,headers={'User-Agent':'Mozilla/5.0'},timeout=20);(P/'raw'/('chart-'+s+'.json')).write_bytes(r.content);out=dict(symbol=s,url=url,requested_at=stamp,status=r.status_code,bytes=len(r.content))
  if r.status_code==200:
   z=r.json()['chart']['result'][0];out['bars']=len(z.get('timestamp',[]));out['vendor_quote_time']=z['meta'].get('regularMarketTime')
  return out
 except Exception as e:return dict(symbol=s,url=url,requested_at=stamp,error=str(e))
out=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 for r in ex.map(get,symbols):
  out.append(r)
  if len(out)%50==0: print(len(out),'/',len(symbols),'pulls',flush=True)
(P/'pull-receipts.json').write_text(json.dumps(out,indent=2)+'\n');print('DONE',len(out),'successful',sum(x.get('status')==200 for x in out),flush=True)
