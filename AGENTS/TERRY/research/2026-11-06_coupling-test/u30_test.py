import csv,datetime as dt,json,statistics as st,collections
U=collections.defaultdict(dict)
for r in csv.DictReader(open('data/ncep_u60.tsv'),delimiter='\t'):
    U[int(r['hpa'])][dt.date.fromisoformat(r['date'])]=float(r['u_zonal_60N'])
A=json.load(open('data/ao_pass.json')); an={int(k):v for k,v in A['anom'].items()}; cut=A['cold_cut']; ao=set(A['pass_card_read'])
yrs=[y for y in range(1950,2026) if dt.date(y,11,6) in U[10]]; print("years",len(yrs))
for hp in (10,30):
    c=[st.mean(U[hp][dt.date(y,11,d)] for d in range(1,8)) for y in range(1991,2021)]
    print(hp,'hPa 60N, Nov 1-7 mean, 1991-2020 climatology',round(st.mean(c),2),'sd',round(st.pstdev(c),2),'min',round(min(c),2))
    c=[U[hp][dt.date(y,11,6)] for y in yrs]
    print('   Nov-6 value 1950-2025: mean',round(st.mean(c),2),'sd',round(st.pstdev(c),2),'lowest 5',sorted((round(v,2),y) for v,y in zip(c,yrs))[:5])
def days(hp,y,a,b,th=0):
    d=dt.date(y,*a); e=dt.date(y,*b); o=[]
    while d<=e:
        if d in U[hp] and U[hp][d]<th: o.append(d)
        d+=dt.timedelta(1)
    return o
print('2026 reads:',[(str(k),hp,v) for hp in (10,30) for k,v in sorted(U[hp].items()) if k.year==2026][-12:])
R10=[y for y in yrs if days(10,y,(11,7),(12,3))]; R30=[y for y in yrs if days(30,y,(11,7),(12,3))]
print('u<0 inside 11/07-12/03 1950-2025: 10 hPa',R10,'30 hPa',R30)
R10e=[y for y in yrs if days(10,y,(11,1),(12,15))]; R30e=[y for y in yrs if days(30,y,(11,1),(12,15))]
print('u<0 inside 11/01-12/15: 10 hPa',R10e,'30 hPa',R30e)
for th in (2,5,8):
    Y=[y for y in yrs if days(30,y,(11,7),(12,3),th)]
    a=[an[y] for y in Y]; f=[an[y] for y in yrs if y not in Y]
    print(f'30 hPa u<{th} any day 11/07-12/03: {len(Y)}/{len(yrs)} {Y if len(Y)<14 else ""} mean {st.mean(a):+.2f}F cold {sum(v<=cut for v in a)}/{len(a)} | not: {st.mean(f):+.2f}F cold {sum(v<=cut for v in f)}/{len(f)}')
