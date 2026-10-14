from pathlib import Path
import json,subprocess,concurrent.futures,hashlib,datetime,re
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[5]; out=ROOT/'AGENTS/REGINALD/domain/sources/2026-10-13_bounded-securities-screen'; raw=out/'raw'
banks={'WAL':1212545,'EGBN':1050441,'ZION':109380,'SSB':764038,'CFG':759944,'BKU':1504008,'SBCF':730708,'AMTB':1734342,'FLG':910073,'MTB':36270,'HBAN':49196,'VLY':714310,'CUBI':1488813}
def get(url):
 r=subprocess.run(['curl','--max-time','35','-s','--fail-with-body','-A','REGINALD-Research williepowen@gmail.com',url],capture_output=True)
 if r.returncode: raise ValueError(f'curl_rc_{r.returncode}')
 return r.stdout

def task(item):
 tk,cik=item;rec={'ticker':tk,'cik':cik,'scope':'complete original HTML saved; securities, hedges, liquidity, funding and market-risk sections for targeted verification'}
 try:
  d=json.loads(get(f'https://data.sec.gov/submissions/CIK{cik:010d}.json'));assert int(d['cik'])==cik
  rec['filer_name']=d['name'];r=d['filings']['recent'];inds=[i for i,x in enumerate(r['form']) if x in ['10-Q','10-Q/A'] and r['reportDate'][i]=='2026-06-30'];assert inds
  i=inds[0];a=r['accessionNumber'][i];doc=r['primaryDocument'][i];url=f'https://www.sec.gov/Archives/edgar/data/{cik}/{a.replace("-","")}/{doc}'
  b=get(url);html=b.decode('utf8','replace');assert '2026' in html
  (raw/f'{tk}_Q2.html').write_text(html)
  soup=BeautifulSoup(html,'html.parser')
  for x in soup(['script','style','ix:header']):x.decompose()
  txt=soup.get_text(' ',strip=True);txt=re.sub(r'\s+',' ',txt)
  (raw/f'{tk}_Q2.txt').write_text(txt)
  rec.update(status='FRESH',url=url,accession=a,filed=r['filingDate'][i],sha256=hashlib.sha256(b).hexdigest(),bytes=len(b),text_bytes=len(txt))
 except Exception as e:rec.update(status='FAILED',reason=str(e) if isinstance(e,(ValueError,AssertionError)) else type(e).__name__)
 return rec
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:res=list(ex.map(task,banks.items()))
(out/'filing-retrieval.json').write_text(json.dumps({'retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'receipts':res},indent=2)+'\n')
for r in res:print(r['ticker'],r['status'],r.get('filer_name',''),r.get('accession',''),r.get('reason',''))
