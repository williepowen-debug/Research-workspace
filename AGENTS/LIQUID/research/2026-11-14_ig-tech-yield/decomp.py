import json,sys
SP=sys.argv[1]
def load(s):
    d=json.load(open(f'{SP}/fred/{s}.json'))
    return {x['date']:float(x['value']) for x in d['observations'] if x['value']!='.'}
S={s:load(s) for s in ['BAMLC0A0CM','BAMLC0A0CMEY','BAMLC0A0CMSYTW','BAMLC0A4CBBB','BAMLC0A4CBBBEY','BAMLC0A3CA','BAMLC0A3CAEY','BAMLC7A0C1015Y','BAMLC7A0C1015YEY','BAMLC8A0C15PY','BAMLC8A0C15PYEY','BAMLC4A0C710Y','BAMLC4A0C710YEY','DGS10','DGS7','DGS30','DBAA','DAAA','HQMCB10YR','HQMCB30YR']}
def at(s,d):
    ks=sorted(k for k in S[s] if k<=d); return ks[-1],S[s][ks[-1]]
last='2026-11-12'
# highest-since checks
for s in ['BAMLC0A0CMSYTW','BAMLC0A0CMEY','BAMLC0A4CBBBEY','BAMLC0A3CAEY','BAMLC4A0C710YEY','BAMLC7A0C1015YEY','BAMLC8A0C15PYEY','BAMLC0A0CM','DGS10','DGS30','DBAA','DAAA']:
    v=S[s][last]; prior=[k for k in S[s] if k<last and S[s][k]>=v]
    mx=max((S[s][k],k) for k in S[s] if k<last)
    print(f"{s:18} {last} {v:5.2f} | last >= this before: {max(prior) if prior else 'none in window (starts '+min(S[s])+')'} | window max {mx[0]} on {mx[1]}")
print()
for s in ['HQMCB10YR','HQMCB30YR']:
    v=S[s]['2026-10-01']; prior=[k for k in S[s] if k<'2026-10-01' and S[s][k]>=v]
    print(s,'Oct-2026',v,'last month >= before:',max(prior) if prior else None)
# 2026 min of IG YTW and date
y26={k:v for k,v in S['BAMLC0A0CMEY'].items() if k>='2026-01-01'}
mn=min((v,k) for k,v in y26.items()); print('\nIG EY 2026 min',mn)
bases=['2025-11-12','2025-12-31',mn[1],'2026-09-30','2026-10-31','2026-11-05']
def row(o,e,base):
    bd,ey0=at(e,base); _,oas0=at(o,base); ey1=S[e][last]; oas1=S[o][last]
    dy=(ey1-ey0)*100; ds=(oas1-oas0)*100; dr=dy-ds
    return f"{bd}: yield {ey0:.2f}->{ey1:.2f} = {dy:+.0f} bp | spread {oas0*100:.0f}->{oas1*100:.0f} = {ds:+.0f} | rate leg (yield−spread) {dr:+.0f} | spread share {ds/dy*100 if dy else 0:.0f}%"
for name,o,e in [('IG all','BAMLC0A0CM','BAMLC0A0CMEY'),('IG 7-10y','BAMLC4A0C710Y','BAMLC4A0C710YEY'),('IG 10-15y','BAMLC7A0C1015Y','BAMLC7A0C1015YEY'),('IG 15y+','BAMLC8A0C15PY','BAMLC8A0C15PYEY'),('BBB','BAMLC0A4CBBB','BAMLC0A4CBBBEY'),('A','BAMLC0A3CA','BAMLC0A3CAEY')]:
    print('\n'+name)
    for b in bases: print('  ',row(o,e,b))
print('\nTreasuries')
for b in bases:
    print(' ',b, ' '.join(f"{s} {at(s,b)[1]:.2f}->{S[s][last]:.2f} ({(S[s][last]-at(s,b)[1])*100:+.0f})" for s in ['DGS7','DGS10','DGS30']))
# recent daily path
print('\nrecent daily')
for k in sorted(S['BAMLC0A0CMEY'])[-12:]:
    print(k, 'IG EY',S['BAMLC0A0CMEY'][k],'OAS',S['BAMLC0A0CM'][k],'15+EY',S['BAMLC8A0C15PYEY'].get(k),'OAS15+',S['BAMLC8A0C15PY'].get(k),'DGS10',S['DGS10'].get(k),'DBAA',S['DBAA'].get(k))
