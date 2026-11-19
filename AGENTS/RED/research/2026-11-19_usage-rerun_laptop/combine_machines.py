# S68 2026-11-19 (WQ-714): add per-desk fresh+out from the desktop and laptop outputs of the same window.
# Parsing is tier_rollup.py's own regexes; machines are additive (transcripts are local to each box).
import re,sys
def load(p):
    L=open(p,encoding='utf-8').read().splitlines(); i=[k for k,l in enumerate(L) if l.startswith('CODEX')][0]; t={}
    for l in L[1:i]:
        m=re.match(r'(\S+)\s+files\s+\d+ fresh\+out\s+([\d,]+)',l)
        if m: n=m[1].replace('+reader',''); t[n]=t.get(n,0)+int(m[2].replace(',',''))
    for l in L[i+1:]:
        m=re.match(r'(.+?)\s+rollouts\s+\d+ fresh\+out\s+([\d,]+)',l)
        if m: n=m[1].strip(); t[n]=t.get(n,0)+int(m[2].replace(',',''))
    return t
d,l=load(sys.argv[1]),load(sys.argv[2]); F=sum(d.values())+sum(l.values())
print('desktop',f'{sum(d.values()):,}','laptop',f'{sum(l.values()):,}','combined',f'{F:,}')
tot={n:d.get(n,0)+l.get(n,0) for n in set(d)|set(l)}
for n in ['PROME','WALTER','DAEDALUS','RED','NEXUS','CATO']: print(f'{n:9s} {tot.get(n,0):13,d} {tot.get(n,0)/F:6.1%}')
print('top:',' · '.join(f'{n} {v/F:.1%}' for n,v in sorted(tot.items(),key=lambda x:-x[1])[:10]))
