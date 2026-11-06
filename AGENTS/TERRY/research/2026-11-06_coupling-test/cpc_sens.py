import glob,re,json,statistics as st
from cpc_test import read,MA,EN
A=json.load(open('data/ao_pass.json')); an={int(k):v for k,v in A['anom'].items()}; cut=A['cold_cut']; ao=set(A['pass_card_read'])
files={re.search(r'(\d{8})',p).group(1):p for p in glob.glob('data/cpc/*.zip')}
v2=lambda o:(sum(o[c][0]=='B' for c in MA)>=2 and sum(o[c][0]=='B' for c in EN)>=2)
v3=lambda o:all(o[c][0]=='B' for c in MA+EN)
for name,f in (('2of3',v2),('all6',v3)):
  for md in ('1127','1128','1129','1130','1201','1202','1203'):
    R={}
    for y in range(2012,2026):
        c=sorted(d for d in files if d[:4]==str(y) and d[4:]<=md and d[4:]>='1120')
        if c: R[y]=f(read(files[c[-1]]))
    P=[y for y in R if R[y]]; F=[y for y in R if not R[y]]
    print(name,md,f'pass {len(P)}/{len(R)} {P} mean {st.mean(an[y] for y in P) if P else 0:+.2f} cold {sum(an[y]<=cut for y in P)} | fail mean {st.mean(an[y] for y in F):+.2f} cold {sum(an[y]<=cut for y in F)}/{len(F)}')
# 2 of the last 3 daily issues through 12/3
R={}
for y in range(2012,2026):
    c=sorted(d for d in files if d[:4]==str(y) and '1120'<=d[4:]<='1203')[-3:]
    R[y]=sum(v2(read(files[d])) for d in c)>=2
P=[y for y in R if R[y]]; F=[y for y in R if not R[y]]
print('2of3 cities, 2 of last 3 issues',P,f'mean {st.mean(an[y] for y in P):+.2f} cold {sum(an[y]<=cut for y in P)}/{len(P)} | fail {st.mean(an[y] for y in F):+.2f} cold {sum(an[y]<=cut for y in F)}/{len(F)}')
