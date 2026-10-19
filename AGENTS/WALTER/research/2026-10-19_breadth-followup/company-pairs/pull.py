from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
import subprocess,json,hashlib,urllib.parse
D=Path(__file__).resolve().parent;(D/'raw').mkdir(exist_ok=True)
symbols=['DG','DLTR','HD','LOW','VZ','T','TMUS','DUK','SO','SPY']
items=[(s+'.json','https://query1.finance.yahoo.com/v8/finance/chart/'+s+'?range=1y&interval=1d&events=div%2Csplits&includeAdjustedClose=true') for s in symbols]
items += [('DUK.htm','https://www.sec.gov/Archives/edgar/data/20290/000132616026000040/duk-20260630.htm'),
          ('SO.htm','https://www.sec.gov/Archives/edgar/data/92122/000009212226000054/so-20260630.htm')]
def pull(x):
    name,url=x;p=subprocess.run(['curl','-sS','-L','--max-time','18','-A','Mozilla/5.0',url],capture_output=True)
    (D/'raw'/name).write_bytes(p.stdout)
    return {'name':name,'url':url,'rc':p.returncode,'bytes':len(p.stdout),'sha256':hashlib.sha256(p.stdout).hexdigest(),'retrieved':datetime.now(timezone.utc).isoformat()}
with ThreadPoolExecutor(max_workers=4) as ex:receipt=list(ex.map(pull,items))
(D/'source-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print([(x['name'],x['rc'],x['bytes']) for x in receipt])
