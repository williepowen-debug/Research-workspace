import statistics as s,re
P={}
def load(f,codes,w):
    for l in open(f):
        k=l[:w]+(l[3] if w==3 else '')
        if k in codes:
            q=6;y=int(l[q:q+4]);P.setdefault(codes[k],{})[y]=[float(x) for x in l[10:].split()]
load('pst.txt',{'0080':'FL','0040':'CA'},3)
load('pdv.txt',{'0804':'FL-d4 SouthCentral','0803':'FL-d3 NorthCentral','0805':'FL-d5 Everglades/SW','0806':'FL-d6 LowerEast','0404':'CA-d4 CentralCoast','0405':'CA-d5 SanJoaquin','0406':'CA-d6 SouthCoast','0401':'CA-d1 NorthCoast'},4)
O={}
for l in open('../acp/oni.txt'):
    p=l.split()
    if p and p[0]=='DJF':O[int(p[1])]=float(p[3])
def ssn(r,y):
    a=P[r].get(y-1);b=P[r].get(y)
    if not a or not b:return None
    v=[a[11],b[0],b[1]]
    return None if min(v)<0 else sum(v)
def ssn5(r,y):
    a=P[r].get(y-1);b=P[r].get(y);v=[a[10],a[11],b[0],b[1],b[2]] if a and b else [-1]
    return None if min(v)<0 else sum(v)
SE=[y for y in O if O[y]>=1.5];VS=[y for y in O if O[y]>=2.0];print('strong',SE)
for r in P:
    for nm,f in(('DJF',ssn),('Nov-Mar',ssn5)):
        A={y:f(r,y) for y in range(1951,2027)};A={k:v for k,v in A.items() if v is not None}
        n=s.mean(A[y] for y in range(1991,2021));srt=sorted(A.values())
        u=srt[int(len(srt)*2/3)];t10=srt[int(len(srt)*.9)]
        g=[y for y in SE if y in A]
        neu=[y for y in A if y in O and abs(O[y])<.5]
        print(f'{r:20}{nm:8} norm {n:5.1f} strongEN',[(y,round(100*A[y]/n)) for y in g],'med',round(100*s.median(A[y] for y in g)/n),'topthird',sum(A[y]>=u for y in g),'/',len(g),'top10%',sum(A[y]>=t10 for y in g),'| neutral topthird',sum(A[y]>=u for y in neu),'/',len(neu))
