"""One-shot regular-session bar check, not a standing collector or official close."""
from pathlib import Path
from datetime import datetime,timezone
from zoneinfo import ZoneInfo
from concurrent.futures import ThreadPoolExecutor
import subprocess,json,hashlib,urllib.parse,statistics
D=Path(__file__).resolve().parent;P=D.parent.parent/'2026-10-19_breadth';NY=ZoneInfo('America/New_York')
(D/'close-raw').mkdir(exist_ok=True)
u=json.loads((P/'universe.json').read_text());syms=[x['ticker'] for x in u['rows']]
def f(item):
    i,ss=item;url='https://query1.finance.yahoo.com/v7/finance/spark?'+urllib.parse.urlencode({'symbols':','.join(ss),'range':'5d','interval':'1d','includePrePost':'false'})
    p=subprocess.run(['curl','-sS','-L','--max-time','18','-A','Mozilla/5.0',url],capture_output=True);b=p.stdout;(D/'close-raw'/f'{i:02d}.json').write_bytes(b)
    rec={'batch':i,'url':url,'rc':p.returncode,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'retrieved':datetime.now(timezone.utc).isoformat()}
    try:result=json.loads(b)['spark']['result']
    except Exception as e:result=[];rec['error']=str(e)
    return rec,result
items=[(i,syms[k:k+20]) for i,k in enumerate(range(0,len(syms),20))]
with ThreadPoolExecutor(max_workers=4) as ex:out=list(ex.map(f,items))
rows=[]
for rec,rr in out:
    for x in rr:
        z=x['response'][0];m=z['meta'];bars={datetime.fromtimestamp(t,NY).date().isoformat():v for t,v in zip(z['timestamp'],z['indicators']['quote'][0]['close']) if v is not None}
        if all(d in bars for d in ['2026-10-16','2026-10-19']):
            rows.append({'symbol':x['symbol'],'friday':bars['2026-10-16'],'monday':bars['2026-10-19'],
                         'return_pct':100*(bars['2026-10-19']/bars['2026-10-16']-1),
                         'quote_clock':datetime.fromtimestamp(m['regularMarketTime'],NY).isoformat(),
                         'exchange_timezone':m.get('exchangeTimezoneName')})
ret=[x['return_pct'] for x in rows]
summary={'retrieved':datetime.now(timezone.utc).isoformat(),'expected':503,'covered':len(rows),
         'up':sum(v>0 for v in ret),'down':sum(v<0 for v in ret),'flat':sum(v==0 for v in ret),
         'median_raw_return_pct':statistics.median(ret) if ret else None,
         'quote_clock_min':min((x['quote_clock'] for x in rows),default=None),
         'quote_clock_max':max((x['quote_clock'] for x in rows),default=None),
         'limits':'Post-close retrieval of vendor daily regular-session bars; not official exchange/index close certification. Current SPY holding security lines, not historical constituent census. Stale quote clocks remain explicit; no claim every price last traded exactly16:00.'}
(D/'close-source-receipt.json').write_text(json.dumps([r for r,z in out],indent=2)+'\n')
(D/'close-snapshot.json').write_text(json.dumps({'summary':summary,'rows':rows},indent=2)+'\n');print(json.dumps(summary,indent=2))
