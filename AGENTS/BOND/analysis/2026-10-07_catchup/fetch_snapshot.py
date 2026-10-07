from pathlib import Path
import sys,json,csv,io,datetime as dt,urllib.request,contextlib
from zoneinfo import ZoneInfo
BASE=Path(__file__).resolve().parents[2]
OUT=Path(__file__).parent/'raw'
OUT.mkdir(parents=True,exist_ok=True)
sys.path.insert(0,str(BASE/'monitors'))
sys.path.insert(0,str(BASE.parents[1]/'FORGE/tools/market-data'))
import grade_auction as ga,fetch
manifest={'captured_et':dt.datetime.now(ZoneInfo('America/New_York')).isoformat(),'sources':{},'gaps':{}}
def save(name,x): (OUT/name).write_text(json.dumps(x,indent=2,default=str)+'\n')
def get(url):
 with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 BOND research'}),timeout=45) as r:return r.read()
original=ga._get
def recorded(url):
 x=original(url);name='ta_ws_'+('frn' if 'type=FRN' in url else 'auctioned')+'.json';save(name,x);manifest['sources'][name]=url;return x
ga._get=recorded
try:
 with (OUT/'auction_audit.txt').open('w') as f,contextlib.redirect_stdout(f),contextlib.redirect_stderr(f): rows=ga.load()
 grades=[]
 for date,cusip,bar,alt,oldmin,oldmax,cover in [('2026-10-06','91282CRQ6',58.90,None,56.50,19.50,2.54),('2026-10-07','91282CRF0',65.05,66.32,63.95,13.38,2.39)]:
  r=next(x for x in rows if x['date']==date and x['cusip']==cusip)
  b=ga.bench(rows,r['term'],False,date,12)
  grades.append({'print':r,'benchmark':b,'frozen':{'Iprime':bar,'alt':alt,'old_min':oldmin,'old_max':oldmax,'cover':cover},'grade':{'Iprime':r['ind']<bar,'alt':None if alt is None else r['ind']<alt,'old':r['ind']<oldmin and r['dlr']>oldmax,'cover':r['btc']<cover,'downgrade_qualifies':r['ind']>=b['ind']['median'] and r['dlr']<=b['dlr']['median']},'margins':{'Iprime_pp':r['ind']-bar,'alt_pp':None if alt is None else r['ind']-alt,'old_ind_pp':r['ind']-oldmin,'old_dlr_pp':r['dlr']-oldmax,'cover':r['btc']-cover}})
 save('auction_grades.json',grades)
except Exception as e:manifest['gaps']['auctions']=str(e)
for kind in ['daily_treasury_yield_curve','daily_treasury_real_yield_curve']:
 try:
  url='https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type='+kind+'&_format=csv'
  body=get(url);(OUT/(kind+'.csv')).write_bytes(body);manifest['sources'][kind]=url
  rows=list(csv.DictReader(io.StringIO(body.decode())));rows.sort(key=lambda r:dt.datetime.strptime(r['Date'],'%m/%d/%Y'))
  save(kind+'_recent.json',rows[-6:])
 except Exception as e:manifest['gaps'][kind]=str(e)
for sid in ['BAMLH0A0HYM2','BAMLH0A3HYC','BAMLC0A0CM','BAMLC0A4CBBB','BAMLH0A1HYBB','BAMLH0A2HYB','SOFR','IORB','EFFR']:
 try:save(sid+'.json',fetch.fred_fetch(sid,limit=10))
 except Exception as e:manifest['gaps'][sid]=str(e)
for name,url in {
 'nbim.html':'https://www.nbim.no/en/news-and-insights/submissions-to-ministry/2026/the-government-pension-fund-global--analyses-and-assessments-of-the-investment-strategy-for-bonds/',
 'ministry.html':'https://www.regjeringen.no/en/topics/the-economy/the-government-pension-fund/eksterne-rapporter-og-brev/id2358366/',
}.items():
 try:(OUT/name).write_bytes(get(url));manifest['sources'][name]=url
 except Exception as e:manifest['gaps'][name]=str(e)
save('manifest.json',manifest)
print(json.dumps(manifest,indent=2))
