import csv
S={}
for r in csv.reader(open('fao.csv',encoding='utf-8-sig')):
    if len(r)>4 and len(r[0])==7 and r[0][4]=='-':S[r[0]]=float(r[4])
K=sorted(S);print(len(K),K[0],K[-1])
yy={k:S[k]/S[f"{int(k[:4])-1}{k[4:]}"]-1 for k in K if f"{int(k[:4])-1}{k[4:]}" in S}
m3={K[i]:S[K[i]]/S[K[i-3]]-1 for i in range(3,len(K))}
print('last6 yy',[(k,S[k],round(100*yy[k],1),round(100*m3[k],1)) for k in K[-8:]])
def ep(D,th,n):
    out=[];run=0;inn=False;miss=0
    for k in sorted(D):
        if D[k]>=th:
            run+=1;miss=0
            if run>=n and not inn:out.append(k);inn=True
        else:
            run=0;miss+=1
            if miss>=3:inn=False
    return out
N=len({k[:4] for k in yy})
for th in(.15,.20,.25,.30):
    for n in(1,2,3):
        e=ep(yy,th,n);print('yy',th,n,len(e),e,'yrs',len({k[:4] for k in yy if yy[k]>=th}))
for th in(.10,.15,.20):
    for n in (1,2):print('3m',th,n,ep(m3,th,n))
# implied levels for next prints
for k in('2026-11','2026-12','2027-01','2027-02','2027-03'):
    b=S.get(f"{int(k[:4])-1}{k[4:]}");print(k,'year-ago',b,'+20%',b and round(b*1.2,1),'+25%',b and round(b*1.25,1))
