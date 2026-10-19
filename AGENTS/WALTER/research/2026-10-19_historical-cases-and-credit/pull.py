from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
import json,subprocess,hashlib
D=Path(__file__).resolve().parent;(D/'raw').mkdir(exist_ok=True)
items=[(s+'.json','https://query1.finance.yahoo.com/v8/finance/chart/'+s+'?range=1y&interval=1d&events=div%2Csplits&includeAdjustedClose=true') for s in ['RCL','NCLH','CCL','CMCSA','CHTR','SPY','RSP','IWM','XLY','XLC']]
items += [('murphy2007.html','https://articles.stockcharts.com/article/members-analysis-20071009-1/'),('pring2015.html','https://articles.stockcharts.com/article/members-articles-pring-2015-08-recent-quiet-market-action-continues-to-mask-deteriorating-breadth/'),('rbc2023.pdf','https://institutional.rbcgam.com/documents/en/common/article/market-update-june-2-2023.pdf'),('sp2024.pdf','https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202406.pdf'),('lpl2023.pdf','https://www.lpl.com/content/dam/lpl-www/documents/asset-library/weekly-market-commentary-06052023.pdf')]
def get(x):
 name,url=x;p=subprocess.run(['curl','-sS','-L','--max-time','18','-A','Mozilla/5.0',url],capture_output=True);b=p.stdout;(D/'raw'/name).write_bytes(b)
 r={'name':name,'url':url,'rc':p.returncode,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'retrieved':datetime.now(timezone.utc).isoformat()}
 if name.endswith('.json'):
  try:r['bars']=len(json.loads(b)['chart']['result'][0]['timestamp'])
  except Exception as e:r['error']=type(e).__name__
 if name.endswith('.pdf'):r['pdf_magic_valid']=b.startswith(b'%PDF')
 return r
with ThreadPoolExecutor(max_workers=4) as ex:r=list(ex.map(get,items))
(D/'source-receipt.json').write_text(json.dumps(r,indent=2)+'\n');print([(x['name'],x['bytes'],x.get('bars'),x.get('pdf_magic_valid')) for x in r])
