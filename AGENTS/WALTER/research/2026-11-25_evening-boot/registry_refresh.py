import subprocess,re,datetime
from pathlib import Path
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
ch=subprocess.run(['git','log','--since=2026-11-25T19:04:00Z','--format=','--name-only','--','AGENTS/*/STATUS.md'],capture_output=True,text=True).stdout.split()
desks=sorted({p.split('/')[1] for p in ch} - {'WALTER'})
p=Path('AGENTS/WALTER/REGISTRY.tsv'); L=p.read_text().split('\n'); done=[]
for d in desks:
    s=Path(f'AGENTS/{d}/STATUS.md').read_text().split('\n')[:40]
    lead=next((l for l in s if re.search(r'(Updated|Last owner update|Last real data refresh|Record maintained|Last written|CURRENT STATE)',l,re.I)),None)
    if not lead: done.append(d+':NO-LEAD'); continue
    lead=re.sub(r'^[#>*\s]+','',lead).replace('\t',' ')
    m=re.search(r'2026-11-2\d',lead); dt=m.group(0) if m else None
    for i,l in enumerate(L):
        c=l.split('\t')
        if c[0]==d:
            if dt: c[-2]=dt
            c[-1]=lead[:230]+' … Mirror from owner header, refreshed '+now+'.'
            L[i]='\t'.join(c); done.append(d+':'+(dt or 'nodate'))
p.write_text('\n'.join(L)); print(now,done)
