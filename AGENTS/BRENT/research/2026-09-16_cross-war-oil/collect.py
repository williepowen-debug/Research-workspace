"""Bounded dated market/EIA snapshot for the commissioned reassessment."""
import sys, json, urllib.request, hashlib
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
sys.path.insert(0, str(ROOT / 'FORGE/tools/market-data'))
import fetch
import yfinance as yf

def now(): return datetime.now(timezone.utc).isoformat()
if '--aligned' in sys.argv:
    data=[]
    for sym in ['BZX26.NYM','BZF27.NYM','CLX26.NYM','HOX26.NYM','RBX26.NYM']:
        t=yf.Ticker(sym)
        h=t.history(period='1d',interval='1m',auto_adjust=False)
        data.append({'symbol':sym,'retrieved_at':now(),'bars':[{'date':str(i),'close':float(r['Close'])} for i,r in h.iterrows()]})
    (OUT/'aligned.json').write_text(json.dumps(data,indent=2)+'\n')
    print('Saved intraday bars; use common timestamps only.')
    raise SystemExit(0)
if '--sources' in sys.argv:
    from bs4 import BeautifulSoup
    sources={
        'fed':'https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm',
        'reuters-oil':'https://www.marketscreener.com/news/oil-falls-as-us-crude-inventories-rise-despite-saudi-supply-concerns-ce785bd2d980f225',
        'russia-flows':'https://www.ttnews.com/articles/russia-boosts-oil-flows',
        'saudi-restart':'https://www.ttnews.com/articles/saudis-seek-resume-half-key-oil-pipeline-within-days',
        'syzran':'https://www.ukrinform.net/rubric-ato/4164723-russias-syzran-and-saratov-oil-refineries-halt-operations-after-drone-attacks-reuters.html',
        'diesel-refineries':'https://kyivindependent.com/ukraines-drone-strikes-force-russias-6-largest-diesel-refineries-to-halt-or-slash-output-reuters-reports/',
        'yasref':'https://www.yasref.com/about-us',
        'imo':'https://www.imo.org/en/mediacentre/hottopics/pages/middle-east-strait-of-hormuz.aspx',
    }
    records=[]
    for name,url in sources.items():
        r={'url':url,'retrieved_at':now()}
        try:
            with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=30) as response:
                b=response.read();r.update(status=response.status,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
                soup=BeautifulSoup(b,'html.parser')
                for tag in soup(['script','style','nav','footer']):tag.decompose()
                (OUT/(name+'.txt')).write_text(soup.get_text('\n',strip=True))
        except Exception as e:r['error']=str(e)
        records.append(r)
    (OUT/'source-retrieval.json').write_text(json.dumps(records,indent=2)+'\n')
    print('Saved source retrieval receipts.')
    raise SystemExit(0)
if '--eia' in sys.argv:
    requests = [('WCSSTUS1','petroleum/stoc/wstk',4),('WCESTUS1','petroleum/stoc/wstk',4),
                ('W_EPC0_SAX_YCUOK_MBBL','petroleum/stoc/wstk',4),('WGTSTUS1','petroleum/stoc/wstk',4),
                ('WDISTUS1','petroleum/stoc/wstk',4),('WPULEUS3','petroleum/pnp/wiup',4),
                ('WGFUPUS2','petroleum/cons/wpsup',60),('WKJUPUS2','petroleum/cons/wpsup',60)]
    data=[{'series':s,'route':r,'retrieved_at':now(),'response':fetch.eia_fetch(s,route=r,limit=n)} for s,r,n in requests]
    (OUT/'eia-api.json').write_text(json.dumps(data,indent=2,default=str)+'\n')
    print('Saved EIA primary responses; dates and units require review.')
    raise SystemExit(0)
symbols = ['BZX26.NYM','BZF27.NYM','CLV26.NYM','CLX26.NYM','CLZ26.NYM',
           'HOV26.NYM','HOX26.NYM','HOZ26.NYM','RBV26.NYM','RBX26.NYM','RBZ26.NYM',
           'USO','VLO','MPC','PSX','BWET','BDRY','DX-Y.NYB','BZ=F','CL=F','HO=F','RB=F']
def quote(sym):
    r={'symbol':sym,'retrieved_at':now()}
    try:
        t=yf.Ticker(sym)
        h=t.history(start='2026-09-09', end='2026-09-17', auto_adjust=False)
        r['bars']=[{'date':str(i), **{k:float(v) for k,v in row.items()}} for i,row in h.iterrows()]
        meta=t.get_history_metadata()
        r['metadata']={k:meta.get(k) for k in ['symbol','shortName','longName','regularMarketPrice','regularMarketTime','exchangeName','expireDate','currency','dataGranularity']}
    except Exception as e: r['error']=str(e)
    return r
with ThreadPoolExecutor(max_workers=4) as pool:
    quotes=list(pool.map(quote,symbols))
(OUT/'quotes.json').write_text(json.dumps(quotes,indent=2,default=str)+'\n')
records=[]
for name,url in [('table1.csv','https://ir.eia.gov/wpsr/table1.csv'),('table9.csv','https://ir.eia.gov/wpsr/table9.csv'),('summary.pdf','https://ir.eia.gov/wpsr/wpsrsummary.pdf')]:
    r={'file':name,'url':url,'retrieved_at':now()}
    try:
        with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=30) as response:
            b=response.read(); (OUT/name).write_bytes(b)
            r.update(status=response.status,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
    except Exception as e:r['error']=str(e)
    records.append(r)
(OUT/'retrieval.json').write_text(json.dumps(records,indent=2)+'\n')
try:
    t=yf.Ticker('USO'); chain=t.option_chain('2026-09-16')
    calls=chain.calls[chain.calls['strike']==165]
    opt={'retrieved_at':now(),'underlying':chain.underlying,'calls':calls.to_dict(orient='records'), 'quote_timestamp':'UNKNOWN; lastTradeDate is not quote time; holdings not verified'}
except Exception as e:opt={'retrieved_at':now(),'error':str(e)}
(OUT/'uso-option.json').write_text(json.dumps(opt,indent=2,default=str)+'\n')
print('Saved dated snapshots; inspect source dates before use.')
