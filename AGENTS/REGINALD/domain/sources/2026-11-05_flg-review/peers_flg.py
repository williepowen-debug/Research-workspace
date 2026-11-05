"""One-time FLG peer and episode checks. FDIC BankFind 2010-6/30/26, banks >= $15B, multifamily book >= $2B. FLG (cert 16022) excluded from peer cells.
Rule fixed before results: event = multifamily 30-89 up >=50% q/q and >=$50M and >=1.0% of book. Convert = rise in multifamily nonaccrual + net charge-offs over 2 quarters >= 50% of the 30-89 balance. Cured = 30-89 under half AND conversion under 25%.
Usage (repo root): python3 peers_flg.py OUTDIR"""
import json,urllib.request,urllib.parse,sys,time
out=sys.argv[1]
F="CERT,NAMEFULL,REPDTE,ASSET,LNREMULT,P3REMULT,NAREMULT,NTREMULT,P9REMULT"
def q(flt):
    u="https://api.fdic.gov/banks/financials?"+urllib.parse.urlencode(dict(filters=flt,fields=F,limit=10000,format="json"))
    for k in range(3):
        try:
            return [x['data'] for x in json.loads(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=90).read())['data']]
        except Exception as e: time.sleep(2); err=e
    raise err
A=[]
for y in range(2010,2027):
    for d in('0331','0630','0930','1231'):
        r=f"{y}{d}"
        if r>'20260630': break
        A+=q(f"REPDTE:{r} AND ASSET:[15000000 TO *]")
json.dump(A,open(out+'/peers15b.json','w'))
by={}
for r in A: by.setdefault(r['CERT'],{})[str(r['REPDTE'])]=r
Q=sorted({str(r['REPDTE']) for r in A}); idx={q:i for i,q in enumerate(Q)}
FLG=[c for c,m in by.items() if any('FLAGSTAR BANK' in str(r.get('NAMEFULL','')).upper() and r.get('ASSET',0)>50000000 for r in m.values())]
print('FLG certs',FLG, [by[c][max(by[c])]['NAMEFULL'] for c in FLG])
ev=[]
for c,m in by.items():
    if c in FLG: continue
    for q_,r in m.items():
        i=idx[q_]
        if i==0 or Q[i-1] not in m: continue
        p=m[Q[i-1]]; b=r.get('LNREMULT') or 0
        if b<2000000: continue
        a,l=p.get('P3REMULT') or 0,r.get('P3REMULT') or 0
        if l-a>=50000 and (a==0 or (l-a)/a>=.5) and l/b>=.01:
            if i+2>=len(Q) or Q[i+2] not in m: ev.append((r['NAMEFULL'][:28],q_,round(a/1e3),round(l/1e3),round(100*l/b,2),None,None)); continue
            x=m[Q[i+2]]; na=(x.get('NAREMULT') or 0)-(r.get('NAREMULT') or 0)
            nco=0
            for j in(i+1,i+2):
                cur=(m.get(Q[j]) or {}).get('NTREMULT') or 0; pr=(m.get(Q[j-1]) or {}).get('NTREMULT') or 0
                nco+=cur-pr if Q[j][:4]==Q[j-1][:4] else cur
            ev.append((r['NAMEFULL'][:28],q_,round(a/1e3),round(l/1e3),round(100*l/b,2),round((na+nco)/l,2),(x.get('P3REMULT') or 0)<.5*l))
for e in sorted(ev,key=lambda e:e[1]): print(e)
g=[e for e in ev if e[5] is not None]
print('peer events',len(ev),'banks',len({e[0] for e in ev}),'graded',len(g),'conv>=50%',sum(e[5]>=.5 for e in g),'cured',sum(e[6] and e[5]<.25 for e in g))
# latest share among big MF lenders 6/30/26
L=sorted([(m[Q[-1]]['NAMEFULL'][:30],round(m[Q[-1]]['LNREMULT']/1e6,1),round(100*(m[Q[-1]].get('P3REMULT') or 0)/m[Q[-1]]['LNREMULT'],2),round(100*(m[Q[-1]].get('NAREMULT') or 0)/m[Q[-1]]['LNREMULT'],2)) for c,m in by.items() if Q[-1] in m and (m[Q[-1]].get('LNREMULT') or 0)>=3000000],key=lambda x:-x[1])
print('6/30/26 name, MF $B, late %, NA %'); [print(' ',x) for x in L[:22]]
