import statistics as s
P={}
for l in open('pst.txt'):
    if l[:4]=='0080':P[int(l[6:10])]=[float(x) for x in l[10:].split()]
def djf(y):
    a=P.get(y-1);b=P.get(y)
    return None if not a or not b or min(a[11],b[0],b[1])<0 else round(a[11]+b[0]+b[1],2)
A={y:djf(y) for y in range(1951,2027)};A={k:v for k,v in A.items() if v is not None}
B=sorted(A[y] for y in range(1991,2021));C=sorted(A.values())
print(len(A),'1991-2020 mean',round(s.mean(B),2),'upper-third line 1991-2020 (21st of 30 rank, next value)',B[19],B[20],'| 1951-2026 n',len(C),C[int(len(C)*2/3)-1],C[int(len(C)*2/3)])
SE=[1958,1973,1983,1992,1998,2016,2024];print([(y,A[y],A[y]>=B[20]) for y in SE],sum(A[y]>=B[20] for y in SE))
print('all years >= line',sum(v>=B[20] for v in A.values()),'/',len(A),'since 1991',sum(A[y]>=B[20] for y in range(1991,2027)),'/36')
nov={y:P[y][10] for y in P if 1950<=y<=2025};w=sorted(nov.values())[-12:];W=[y for y in nov if nov[y]>=w[0]];print('wettest 12 Novembers -> DJF wet third',sum(A.get(y+1,0)>=B[20] for y in W),'/',len([y for y in W if y+1 in A]))
