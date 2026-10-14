"""One-off source capture for Will's authorized WAL earnings-path test; not a monitor."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import json, hashlib, subprocess, sys
from bs4 import BeautifulSoup

ROOT = Path('/home/willi/Research-workspace')
DEST = Path(__file__).resolve().parent
ET = ZoneInfo('America/New_York')

def dump(name, data):
    (DEST/name).write_text(json.dumps(data, indent=2, default=str)+'\n')

def extract_existing():
    manifest=[]
    for key, rel in [('Q2_10Q','AGENTS/WAL/sources/q2_2026/wal-20260630.htm'),
                     ('Q1_10Q','AGENTS/WAL/sources/q1_2026/wal-20260331.htm'),
                     ('Q1_release','AGENTS/WAL/sources/q1_2026/WAL-Q1-2026-Press-Release.htm'),
                     ('investor_day','AGENTS/WAL/sources/investor_day_2026/deck_raw.htm')]:
        p=ROOT/rel
        raw=p.read_bytes()
        if key=='Q2_10Q':
            assert hashlib.sha256(raw).hexdigest()=='63f0a86758850f7c833bfe111d86dbd7bb9810b0ea6ce0550cc841e0b66ad85f'
        soup=BeautifulSoup(raw,'html.parser')
        for el in soup(['script','style']): el.decompose()
        text=soup.get_text(' ',strip=True)
        (DEST/(key+'-text.txt')).write_text(text)
        tables=[t.get_text(' ',strip=True) for t in soup.find_all('table')]
        dump(key+'-tables.json',tables)
        manifest.append({'key':key,'original':rel,'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'text_chars':len(text),'tables':len(tables),'verification':'locally preserved issuer source, read-only reuse, not fresh retrieval'})
    dump('reused-primary-manifest.json',manifest)
    print(json.dumps(manifest,indent=2))

def retrieve():
    import yfinance as yf
    ticker=yf.Ticker('WAL')
    out={'retrieved_start_ET':datetime.now(ET).isoformat(),'symbol':'WAL','sources':{},'errors':{}}
    for name,call in [('info',lambda:ticker.get_info()),('earnings_estimate',lambda:ticker.get_earnings_estimate()),
                      ('revenue_estimate',lambda:ticker.get_revenue_estimate()),('eps_trend',lambda:ticker.get_eps_trend()),
                      ('eps_revisions',lambda:ticker.get_eps_revisions())]:
        try:
            value=call()
            out['sources'][name]=value.to_dict(orient='index') if hasattr(value,'to_dict') else value
            print(name,'OK',flush=True)
        except Exception as exc:
            out['errors'][name]=str(exc)
            print(name,'FAILED',type(exc).__name__,flush=True)
    urls={
        'nasdaq_earnings_forecast':'https://api.nasdaq.com/api/analyst/WAL/earnings-forecast',
        'Q2_deck':'https://www.sec.gov/Archives/edgar/data/1212545/000162828026049001/walq22026earningspresent.htm',
        'Q2_release':'https://www.sec.gov/Archives/edgar/data/1212545/000162828026049001/pressrelease-6302026.htm',
    }
    for key,url in urls.items():
        suffix='.json' if key.startswith('nasdaq') else '.htm'
        path=DEST/(key+suffix)
        r=subprocess.run(['curl','-L','--max-time','35','--retry','0','-sS','-A','Research desk research@example.com','-H','Accept: application/json,text/html','-o',str(path),'-w','%{http_code}',url],capture_output=True,text=True)
        receipt={'url':url,'http_status':r.stdout.strip(),'returncode':r.returncode,'retrieved_ET':datetime.now(ET).isoformat(),'error':r.stderr[:600]}
        if r.returncode==0 and receipt['http_status']=='200':
            raw=path.read_bytes(); receipt.update(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
            if suffix=='.json':
                try: out['sources'][key]=json.loads(raw)
                except Exception as exc: out['errors'][key]='Unparseable JSON: '+str(exc)
            else:
                soup=BeautifulSoup(raw,'html.parser')
                text=soup.get_text(' ',strip=True)
                (DEST/(key+'-text.txt')).write_text(text)
                receipt['identity_present']='Western Alliance' in text or 'WESTERN ALLIANCE' in text
        else: out['errors'][key]=receipt
        dump(key+'-retrieval.json',receipt)
        print(key,receipt['http_status'],flush=True)
    out['retrieved_end_ET']=datetime.now(ET).isoformat()
    dump('current-consensus.json',out)
    compact={k:v for k,v in out['sources'].items() if k!='info'}
    info=out['sources'].get('info',{})
    compact['quote']={k:info.get(k) for k in ['symbol','longName','regularMarketPrice','regularMarketTime','exchangeDataDelayedBy','marketState','forwardEps']}
    compact['errors']=out['errors']
    dump('current-consensus-compact.json',compact)
    print(json.dumps(compact,indent=2),flush=True)

if __name__=='__main__':
    if '--nasdaq-retry' in sys.argv:
        url='https://api.nasdaq.com/api/analyst/WAL/earnings-forecast'
        path=DEST/'nasdaq_earnings_forecast_http1.json'
        r=subprocess.run(['curl','--http1.1','-L','--max-time','35','--retry','0','-sS','-A','Mozilla/5.0','-H','Accept: application/json','-o',str(path),'-w','%{http_code}',url],capture_output=True,text=True)
        receipt={'url':url,'http_status':r.stdout.strip(),'returncode':r.returncode,'retrieved_ET':datetime.now(ET).isoformat(),'error':r.stderr[:600],'attempt':'one bounded HTTP/1.1 retry after HTTP/2 protocol failure'}
        if r.returncode==0 and receipt['http_status']=='200':
            data=json.loads(path.read_text())
            assert data['data']['symbol'].upper()=='WAL'
            receipt['sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
            print(json.dumps(data,indent=2))
        dump('nasdaq-http1-retrieval.json',receipt)
        print(json.dumps(receipt,indent=2))
    elif '--retrieve' in sys.argv: retrieve()
    else: extract_existing()
