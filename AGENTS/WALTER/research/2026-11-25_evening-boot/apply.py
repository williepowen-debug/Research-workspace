import subprocess,datetime
from pathlib import Path
now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
p=Path('AGENTS/WALTER/REGISTRY.tsv'); L=p.read_bytes().decode().split('\n')
new={'DAEDALUS':('2026-11-25','**Last Updated: 2026-11-25 15:05 ET — Will "go" 14:51 ET: L1193 correction, late scorecard, wiring run 5, prose-remedy census 3. Laptop, Claude Code Opus 5.5. … Mirror from owner header, refreshed '+now+'.'),
'AEOLUS':('2026-11-25','Last Updated:** 2026-11-25 14:41 ET (PROME due-row wake, D:L1256 owed #23: NorCal observed tides, KB-334…337; cards 025/029/030 drained; no score moved). … Mirror from owner header, refreshed '+now+'.')}
for i,l in enumerate(L):
    c=l.split('\t')
    if c[0] in new: c[-2],c[-1]=new[c[0]]; L[i]='\t'.join(c)
p.write_bytes('\n'.join(L).encode())
d=Path('AGENTS/WALTER/registry/DOORBELL_LOG.tsv')
with d.open('ab') as f: f.write(('2026-11-25\tCORAL\tSIG-W-20261125-037\tNONE\tL1-UNKNOWN\tNO\tNA\tNA\tNA\t\tAbsent from ListAgents 16:09 ET (liquid-bd, homer-e8, daedalus-b6, prome-77, nexus-99, reginald-9a, henry-7d, violet-29); UNKNOWN by 9b. CORAL already holds AEOLUS packet d9e9e20756; PROME SCRATCH carries the 6.4 forecast. Wake order is PROME\'s.\n').encode())
