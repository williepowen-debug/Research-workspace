"""Read-only bounded replay: candidate titles for human capital-event review, not routing."""
from pathlib import Path
import json,re,hashlib
LANE=Path('/home/willi/Research-Intake'); OUT=Path(__file__).parent
DAYS=['2026-10-01','2026-10-05','2026-10-06','2026-10-07','2026-11-02','2026-11-03','2026-11-04']
ENTITIES={'Carnival Corp','Royal Caribbean','Norwegian Cruise'}
PATTERN=re.compile(r'\b(?:notes? offering|bond offering|commercial paper|credit facilit(?:y|ies)|revolver|refinanc\w*|debt financ\w*|loan|stake|joint venture|acquisition|tender offer|debt exchange)\b',re.I)
def candidate(x):
 return x.get('classification')=='KNOWN' and x.get('entity') in ENTITIES and 'CRUISE' in x.get('agents',[]) and bool(PATTERN.search(x.get('title','')))
rows=[];counts=[];sources=[]
for day in DAYS:
 p=LANE/'data'/day/'news.json';data=p.read_bytes();items=json.loads(data)['items'];own=[x for x in items if 'CRUISE' in x.get('agents',[])];known=[x for x in own if x.get('classification')=='KNOWN'];matches=[]
 for i,x in enumerate(items):
  if candidate(x):rows.append({'day':day,'index':i,'title':x['title'],'source_date':x.get('date'),'entity':x.get('entity'),'classification':x.get('classification')});matches.append(i)
 counts.append({'day':day,'cruise_rows':len(own),'known_rows':len(known),'candidate_indices':matches});sources.append({'path':str(p),'sha256':hashlib.sha256(data).hexdigest()})
(OUT/'cruise-sample.json').write_text(json.dumps({'rule':PATTERN.pattern,'counts':counts,'candidates':rows,'sources':sources},indent=2)+'\n')
print(json.dumps({'counts':counts,'candidates':rows},indent=2))
