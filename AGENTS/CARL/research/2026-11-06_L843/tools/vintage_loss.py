#!/usr/bin/env python3
"""ALLY consumer-auto cumulative gross charge-offs by origination year at matched seasoning.
Every input is transcribed from an SEC filing named in the comment. $ millions. Run from research/2026-11-06_L843."""
# gross charge-offs by origination year, consumer automotive
G={ # (vintage, window): $M
 (2023,'9M23'):97,   # 10-Q 9/30/23 Note: nine months ended 9/30/23
 (2023,'FY23'):225,  # 10-K 2023; repeated 10-Q 9/30/24, 10-K 2024
 (2023,'9M24'):567,  # 10-Q 9/30/24
 (2023,'FY24'):779,  # 10-K 2024
 (2023,'9M25'):574,  # 10-Q 9/30/25
 (2023,'FY25'):747,  # 10-K 2025
 (2023,'9M26'):421,  # 10-Q 9/30/26
 (2024,'9M24'):65,(2024,'FY24'):160,(2024,'9M25'):405,(2024,'FY25'):564,(2024,'9M26'):449,
 (2025,'9M25'):65,(2025,'FY25'):168,(2025,'9M26'):520,
 (2026,'9M26'):105,
}
# retail originations = used retail + new retail (MD&A table, excludes lease)
O={2023:{'9M':19598+8570,'FY':25813+11310},2024:{'9M':18562+7744,'FY':24542+11057},2025:{'9M':20143+9170,'FY':26871+12369},2026:{'9M':24066+11660}}
# on-book balance of the vintage at first 9/30 and first 12/31 (origination-year credit quality tables)
B={2023:{'9M':24964,'FY':31450},2024:{'9M':23931,'FY':30919},2025:{'9M':26611,'FY':34282},2026:{'9M':32362}}
# Age points. Y+0 Sep = cum through 9/30 of origination year, etc.
def cum(v,pt):
    y=v
    if pt=='Sep Y+0': return G.get((v,f'9M{str(y)[2:]}'))
    if pt=='Dec Y+0': return G.get((v,f'FY{str(y)[2:]}'))
    if pt=='Sep Y+1':
        a=G.get((v,f'FY{str(y)[2:]}'));b=G.get((v,f'9M{str(y+1)[2:]}'));return None if a is None or b is None else a+b
    if pt=='Dec Y+1':
        a=G.get((v,f'FY{str(y)[2:]}'));b=G.get((v,f'FY{str(y+1)[2:]}'));return None if a is None or b is None else a+b
    if pt=='Sep Y+2':
        a=cum(v,'Dec Y+1');b=G.get((v,f'9M{str(y+2)[2:]}'));return None if a is None or b is None else a+b
    if pt=='Dec Y+2':
        a=cum(v,'Dec Y+1');b=G.get((v,f'FY{str(y+2)[2:]}'));return None if a is None or b is None else a+b
    if pt=='Sep Y+3':
        a=cum(v,'Dec Y+2');b=G.get((v,f'9M{str(y+3)[2:]}'));return None if a is None or b is None else a+b
pts=['Sep Y+0','Dec Y+0','Sep Y+1','Dec Y+1','Sep Y+2','Dec Y+2','Sep Y+3']
print('Originations 9M/FY:',O); print('9M share of FY:',{v:round(O[v]['9M']/O[v]['FY'],4) for v in (2023,2024,2025)})
print('\nA. cumulative gross charge-offs / full-year retail originations (Sep Y+0 uses 9M originations), %')
print('age\t'+'\t'.join(str(v) for v in O))
tab={}
for p in pts:
    row=[]
    for v in O:
        c=cum(v,p)
        d=O[v]['9M'] if p=='Sep Y+0' else O[v].get('FY')
        r=None if c is None or d is None else 100*c/d
        tab[(v,p)]=r; row.append('' if r is None else f'{r:.3f}')
    print(p,*row,sep='\t')
print('\nB. same numerator / on-book balance at first 9/30 (Sep Y+0) or first 12/31, %')
tb={}
for p in pts:
    row=[]
    for v in O:
        c=cum(v,p)
        d=B[v]['9M'] if p=='Sep Y+0' else B[v].get('FY')
        r=None if c is None or d is None else 100*c/d
        tb[(v,p)]=r; row.append('' if r is None else f'{r:.3f}')
    print(p,*row,sep='\t')
print('\nC. gaps to FY2023 at the same age, bp')
for v,p in [(2025,'Sep Y+0'),(2025,'Dec Y+0'),(2025,'Sep Y+1'),(2026,'Sep Y+0'),(2024,'Sep Y+0'),(2024,'Dec Y+0'),(2024,'Sep Y+1'),(2024,'Dec Y+1'),(2024,'Sep Y+2')]:
    print(v,p,'orig basis %+.1f'%(100*(tab[(v,p)]-tab[(2023,p)])),'bal basis %+.1f'%(100*(tb[(v,p)]-tb[(2023,p)])))
print('\nD. FY2025 v FY2024 at same age, bp')
for p in ('Sep Y+0','Dec Y+0','Sep Y+1'): print(p,'%+.1f'%(100*(tab[(2025,p)]-tab[(2024,p)])))
print('FY2026 v FY2025 Sep Y+0 %+.1f; v FY2024 %+.1f'%(100*(tab[(2026,'Sep Y+0')]-tab[(2025,'Sep Y+0')]),100*(tab[(2026,'Sep Y+0')]-tab[(2024,'Sep Y+0')])))
# E. extreme bound: every off-balance-sheet net loss 2025 + 9M26 assigned to FY2025, none to FY2023
wl=104+17+118+10   # 10-K 2025 and 10-Q 9/30/26 off-balance-sheet tables: whole-loan + securitization net credit losses, auto
v25=(cum(2025,'Sep Y+1')+wl)/O[2025]['FY']*100
print('\nE. extreme bound: +$%dM all to FY2025: %.3f%%, gap to FY2023 %+.1f bp'%(wl,v25,100*(v25-tab[(2023,'Sep Y+1')])))
# F. lifetime scale: share of FY2023 realized to date reached at Sep Y+1
print('F. FY2023 Sep Y+1 / latest Sep Y+3 cum: %.3f'%(tab[(2023,'Sep Y+1')]/tab[(2023,'Sep Y+3')]))
print('   A +50 bp gap at Sep Y+3 maps to about +%.0f bp at Sep Y+1 if proportional'%(50*tab[(2023,'Sep Y+1')]/tab[(2023,'Sep Y+3')]))
