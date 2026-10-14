from pathlib import Path
import requests,datetime,json,hashlib,concurrent.futures
from bs4 import BeautifulSoup
from io import BytesIO
from pypdf import PdfReader
base=Path(__file__).parent
urls={
'jpm_release':'https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/quarterly-earnings/2026/3rd-quarter/6c1f8114-1be4-4174-8292-f75bbb59bc21.pdf',
'jpm_deck':'https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/quarterly-earnings/2026/3rd-quarter/2b5b9a7e-a968-4985-94ad-5fa949a08d1c.pdf',
'jpm_supplement':'https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/quarterly-earnings/2026/3rd-quarter/c89c7479-82df-4c9f-a7be-957956430abd.pdf',
'citi_call':'https://www.citigroup.com/rcs/citigpa/storage/public/Earnings/Q32026/3q26-citigroup-earnings-transcript.pdf',
'citi_8k':'https://www.citigroup.com/rcs/citigpa/storage/public/Earnings/Q32026/3q26-earnings-8-k-10-13-26.pdf',
'wfc_release':'https://www.sec.gov/Archives/edgar/data/72971/000007297126000318/wfc3qer10-13x26ex991xrelea.htm',
'wfc_supplement':'https://www.sec.gov/Archives/edgar/data/72971/000007297126000318/wfc3qer10-13x26ex992xsuppl.htm',
'fsk_10q':'https://www.sec.gov/Archives/edgar/data/1422183/000162828026053783/fsk-20260630.htm',
'crmt_submissions':'https://data.sec.gov/submissions/CIK0000799850.json',
'fsk_submissions':'https://data.sec.gov/submissions/CIK0001422183.json',
'jpm_events':'https://www.jpmorganchase.com/ir/events',
'wfc_ir':'https://www.wellsfargo.com/about/investor-relations/quarterly-earnings/'
}
def fetch(item):
 k,u=item; m={'key':k,'url':u,'retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  r=requests.get(u,timeout=40,headers={'User-Agent':'Research evidence review contact research@example.com'})
  m.update(status=r.status_code,bytes=len(r.content),sha256=hashlib.sha256(r.content).hexdigest())
  if r.status_code!=200:return m
  ext='pdf' if r.content.startswith(b'%PDF') else 'json' if k.endswith('submissions') else 'html'
  (base/(k+'.'+ext)).write_bytes(r.content)
  if ext=='pdf': t='\n'.join('\n[PDF page '+str(i+1)+']\n'+(p.extract_text() or '') for i,p in enumerate(PdfReader(BytesIO(r.content)).pages))
  elif ext=='html':t=BeautifulSoup(r.content,'html.parser').get_text(' ',strip=True)
  else:t=r.text
  (base/(k+'.txt')).write_text(t);m['text_chars']=len(t)
 except Exception as e:m['error']=str(e)
 return m
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool: results=list(pool.map(fetch,urls.items()))
(base/'retrieval.json').write_text(json.dumps(results,indent=2))
for r in results:print(r['key'],r.get('status'),r.get('bytes'),r.get('error',''))
