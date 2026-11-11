import csv, re, sys
from pathlib import Path
R=Path('/home/willi/Research-workspace'); W=R/'AGENTS/WALTER'
rows=list(csv.reader((W/'REGISTRY.tsv').open(), delimiter='\t'))
hdr=rows[0]; iU=hdr.index('Updated'); iF=hdr.index('Focus'); iA=hdr.index('Agent')
TODAY='2026-11-11'; changed=[]
for r in rows[1:]:
    if len(r)<=iF: continue
    a=r[iA]; f=R/'PROME/STATUS.md' if a=='PROME' else R/f'AGENTS/{a}/STATUS.md'
    if not f.exists() or a=='WALTER': continue
    lines=f.read_text(errors='replace').splitlines()[:12]
    best=None; bl=None
    for ln in lines:
        for d in re.findall(r'20\d\d-\d\d-\d\d', ln):
            if d<=TODAY and (best is None or d>best): best=d; bl=ln
    if not best or best<=r[iU]: continue
    s=re.sub(r'[*>#`]|★','',bl).strip(); s=re.sub(r'\s+',' ',s)[:220].rstrip()
    old=r[iU]; r[iU]=best; r[iF]=s+' … Mirror from owner header, refreshed 2026-11-11T15:39:33Z.'
    changed.append(f'{a}: {old} -> {best}')
if '--write' in sys.argv:
    with (W/'REGISTRY.tsv').open('w', newline='') as fh:
        csv.writer(fh, delimiter='\t', lineterminator='\n', quoting=csv.QUOTE_MINIMAL).writerows(rows)
print(len(changed),'rows'); print('\n'.join(changed))
