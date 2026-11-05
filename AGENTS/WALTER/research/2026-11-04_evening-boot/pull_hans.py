import sys,json,concurrent.futures
from pathlib import Path
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/HANS/scripts');import fetch_eu as f
out={}
fs={'ecb_aaa10':lambda:f.ecb(f.AAA10Y,7),'boe10':lambda:f.boe('IUDMNPY'),'agsi':f.agsi_eu}
with concurrent.futures.ThreadPoolExecutor() as ex:
 for k,v in zip(fs,ex.map(lambda fn:fn(),fs.values())):out[k]=v
if out['agsi'][0]:out['norm']=f.agsi_norm(out['agsi'][0][0])
Path('research/2026-11-04_evening-boot/hans-observations.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
