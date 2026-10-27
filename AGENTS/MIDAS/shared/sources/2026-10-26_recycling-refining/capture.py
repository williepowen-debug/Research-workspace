from pathlib import Path
from curl_cffi import requests
from bs4 import BeautifulSoup
import json,hashlib,datetime
base=Path(__file__).parent
sources={
'sibanye_h1.html':'https://www.sec.gov/Archives/edgar/data/1786909/000162828026059701/form6-kh137.htm',
'umicore_h1.html':'https://www.umicore.de/en/media/half-year-results-2026/',
'valterra_rns.html':'https://www.investegate.co.uk/announcement/rns/valterra-platinum-limited--valt/third-quarter-production-report/9837887',
'silver_survey.pdf':'https://silverinstitute.org/wp-content/uploads/2026/04/World-Silver-Survey-2026.pdf'}
manifest=[]
for name,url in sources.items():
 try:
  r=requests.get(url,impersonate='chrome',timeout=45)
  record={'file':name,'url':url,'status':r.status_code,'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'bytes':len(r.content),'sha256':hashlib.sha256(r.content).hexdigest()}
  if r.status_code==200:
   (base/name).write_bytes(r.content)
   if name.endswith('.html'):
    soup=BeautifulSoup(r.content,'html.parser')
    for tag in soup(['script','style']):tag.decompose()
    (base/name.replace('.html','.txt')).write_text(soup.get_text('\n',strip=True))
  manifest.append(record)
 except Exception as e:manifest.append({'file':name,'url':url,'error':str(e)})
 print(manifest[-1])
(base/'capture.json').write_text(json.dumps(manifest,indent=2)+'\n')
