# Candidate (c): CPC 8-14 day temperature outlook category at six named cities, from the archived shapefiles.
import zipfile, glob, struct, re, json, collections, statistics as st
PTS={'Philadelphia':(-75.16,39.95),'New York':(-74.01,40.71),'Pittsburgh':(-80.00,40.44),
     'Chicago':(-87.63,41.88),'Detroit':(-83.05,42.33),'Columbus':(-83.00,39.96)}
MA=['Philadelphia','New York','Pittsburgh']; EN=['Chicago','Detroit','Columbus']
def dbf(b):
    n,hl,rl=struct.unpack('<xxxxIHH',b[:12]); F=[]; off=1
    for i in range(32,hl-1,32):
        F.append((b[i:i+11].split(b'\0')[0].decode(),off,b[i+16])); off+=b[i+16]
    R=[]
    for r in range(n):
        rec=b[hl+r*rl:hl+(r+1)*rl]
        R.append({k:rec[o:o+w].decode('latin1').strip() for k,o,w in F})
    return R
def shp(b):
    o=100; P=[]
    while o<len(b):
        num,ln=struct.unpack('>II',b[o:o+8]); o+=8; c=b[o:o+ln*2]; o+=ln*2
        t=struct.unpack('<i',c[:4])[0]
        if t!=5: P.append([]); continue
        np_,npt=struct.unpack('<ii',c[36:44]); parts=list(struct.unpack('<%di'%np_,c[44:44+4*np_]))
        xy=struct.unpack('<%dd'%(2*npt),c[44+4*np_:44+4*np_+16*npt])
        pts=[(xy[2*i],xy[2*i+1]) for i in range(npt)]
        P.append([pts[parts[i]:(parts[i+1] if i+1<np_ else npt)] for i in range(np_)])
    return P
def inside(x,y,rings):
    c=False
    for r in rings:
        for i in range(len(r)-1):
            (x1,y1),(x2,y2)=r[i],r[i+1]
            if (y1>y)!=(y2>y) and x<(x2-x1)*(y-y1)/(y2-y1)+x1: c=not c
    return c
def area(rings):
    return sum(abs(sum(r[i][0]*r[i+1][1]-r[i+1][0]*r[i][1] for i in range(len(r)-1)))/2 for r in rings)
def read(p):
    z=zipfile.ZipFile(p); N=z.namelist()
    R=dbf(z.read([x for x in N if x.endswith('.dbf')][0])); G=shp(z.read([x for x in N if x.endswith('.shp')][0]))
    out={}
    for name,(x,y) in PTS.items():
        hit=[(area(g),r) for r,g in zip(R,G) if g and inside(x,y,g)]
        if hit:
            r=min(hit,key=lambda h:h[0])[1]; out[name]=(r.get('Cat','')[:1],float(r['Prob']))
        else: out[name]=('N',0.0)
    return out
if __name__=='__main__':
    print('control 20261105',read('data/cpc/814temp_20261105.zip'))
    A=json.load(open('data/ao_pass.json')); an={int(k):v for k,v in A['anom'].items()}; cut=A['cold_cut']; ao=set(A['pass_card_read'])
    Y=collections.defaultdict(list)
    bad=0
    for p in sorted(glob.glob('data/cpc/*.zip')):
        d=re.search(r'(\d{8})',p).group(1)
        if d=='20261105': continue
        try: Y[int(d[:4])].append((d,read(p)))
        except Exception as e: bad+=1
    print('years',len(Y),'issues',sum(map(len,Y.values())),'unreadable',bad)
    def v2(o): # at least 2 of 3 cities below normal in both divisions
        return sum(o[c][0]=='B' for c in MA)>=2 and sum(o[c][0]=='B' for c in EN)>=2
    def v3(o): return all(o[c][0]=='B' for c in MA+EN)
    print('year issues v2-issues v3-issues first_v2 ao dj_anom cold')
    res={}
    for y in sorted(Y):
        I=Y[y]; a=[d for d,o in I if v2(o)]; b=[d for d,o in I if v3(o)]
        res[y]=dict(n=len(I),v2=len(a),v3=len(b),first=a[0] if a else None)
        print(y,len(I),len(a),len(b),a[0] if a else '-', 'AO' if y in ao else '--', f'{an[y]:+.2f}', 'COLD' if an[y]<=cut else '')
    for nm,k,mn in [('v2 any issue','v2',1),('v2 2+ issues','v2',2),('v3 any issue','v3',1)]:
        P=[y for y in res if res[y][k]>=mn]; F=[y for y in res if res[y][k]<mn]
        f=lambda L:(f'{st.mean(an[y] for y in L):+.2f}F cold {sum(an[y]<=cut for y in L)}/{len(L)}') if L else 'none'
        print(nm,f'pass {len(P)}/{len(res)}: {f(P)} | fail: {f(F)}')
        Q=[y for y in P if y in ao]; print('   with AO run too:',Q,f(Q))
    json.dump(res,open('data/cpc_res.json','w'))
