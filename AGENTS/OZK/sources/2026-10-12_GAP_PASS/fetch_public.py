import sys, json, hashlib, datetime, io
from pathlib import Path
import requests
from pdfminer.high_level import extract_text
from html.parser import HTMLParser
class Text(HTMLParser):
 def __init__(self): super().__init__(); self.parts=[]; self.skip=0
 def handle_starttag(self,t,a):
  if t in ('script','style'): self.skip+=1
 def handle_endtag(self,t):
  if t in ('script','style'): self.skip=max(0,self.skip-1)
 def handle_data(self,d):
  if not self.skip and d.strip(): self.parts.append(d.strip())
root=Path(__file__).parent
items=json.loads(Path(sys.argv[1]).read_text())
for label,url in items:
 stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
 receipt={'label':label,'requested_url':url,'read_utc':stamp}
 try:
  r=requests.get(url,headers={'User-Agent':'Mozilla/5.0 public research'},timeout=25)
  suffix='.pdf' if r.content.startswith(b'%PDF') else '.html'
  path=root/(label+suffix); path.write_bytes(r.content)
  receipt.update(status=r.status_code,final_url=r.url,bytes=len(r.content),sha256=hashlib.sha256(r.content).hexdigest(),file=path.name)
  if r.status_code==200:
   if suffix=='.pdf': txt=extract_text(io.BytesIO(r.content))
   else:
    parser=Text(); parser.feed(r.text); txt='\n'.join(parser.parts)
   (root/(label+'.txt')).write_text(txt)
 except Exception as e: receipt['error']=type(e).__name__+': '+str(e)
 with (root/'FETCH_RECEIPTS.jsonl').open('a') as f: f.write(json.dumps(receipt)+'\n')
 print(json.dumps({k:v for k,v in receipt.items() if k in ('label','status','bytes','error')}),flush=True)
