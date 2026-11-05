import json,sys
d=sys.argv[1]
P=sorted(json.load(open(d+'/pf.json')),key=lambda r:r['REPDTE'])
P.append(dict(REPDTE='20260930',P3ASSET=213231,NAASSET=159758,NTLNLS=None))
# YTD NTLNLS -> quarterly
for i,r in enumerate(P):
    y=str(r['REPDTE'])[:4]; prev=P[i-1] if i else None
    if r['NTLNLS'] is None: r['nco']=-8; continue
    r['nco']=r['NTLNLS']-(prev['NTLNLS'] if prev and str(prev['REPDTE'])[:4]==y else 0)
ev=[]
for i in range(1,len(P)-2+2):
    if i>=len(P): break
    a,b=P[i-1]['P3ASSET'],P[i]['P3ASSET']
    for thr in (1,):
        pass
    if b-a>=20000 and (a==0 or (b-a)/a>=.5):
        j=P[i+1:i+3]; na=[x['NAASSET'] for x in j]
        up=(max(na)-P[i]['NAASSET'])/1e3 if na else None
        nco=sum(x['nco'] for x in j)/1e3 if j else None
        ev.append((str(P[i]['REPDTE']),round(a/1e3,1),round(b/1e3,1),'NA',round(P[i]['NAASSET']/1e3,1),'->',[round(x/1e3,1) for x in na],'NAup',None if up is None else round(up,1),'NCO2q',None if nco is None else round(nco,1),'jump',round((b-a)/1e3,1),'comparable',None if up is None else up+(nco or 0)>=0.5*(b-a)/1e3))
for e in ev: print(e)
print('events +50% and +$20M:',len(ev),'resolved',sum(e[-1] is not None for e in ev),'comparable(>=50% of jump)',sum(e[-1] is True for e in ev))
print('max NCO 2q window after any event',max([e[10] for e in ev if e[10] is not None]))
# cross section
A=json.load(open(d+'/peers.json'))
by={}
for r in A: by.setdefault(r['CERT'],{})[str(r['REPDTE'])]=r
Q=sorted({str(r['REPDTE']) for r in A})
idx={q:i for i,q in enumerate(Q)}
for lo,lab in ((.05,'>5%'),(.10,'>10%')):
    E=[]
    for c,m in by.items():
        for q,r in m.items():
            if (r.get('LNREMULT') or 0)<100000: continue
            sh=(r.get('P3REMULT') or 0)/r['LNREMULT']
            if sh<=lo: continue
            i=idx[q]
            if i+2>=len(Q): E.append(('open',r,sh)); continue
            n=m.get(Q[i+2])
            if not n: E.append(('gone',r,sh)); continue
            late=r['P3REMULT']; naup=(n.get('NAREMULT') or 0)-(r.get('NAREMULT') or 0)
            cumnco=sum(((m.get(Q[j]) or {}).get('NTREMULT') or 0)-((m.get(Q[j-1]) or {}).get('NTREMULT') or 0) if Q[j][:4]==Q[j-1][:4] else ((m.get(Q[j]) or {}).get('NTREMULT') or 0) for j in (i+1,i+2))
            conv=(naup+cumnco)/late
            cured=(n.get('P3REMULT') or 0)<0.5*late and conv<0.25
            E.append(('ok',r,sh,conv,cured))
    ok=[e for e in E if e[0]=='ok']
    print(lab,'bank-quarters',len(E),'banks',len({e[1]['CERT'] for e in E}),'gradable',len(ok),'conv>=50%',sum(e[3]>=.5 for e in ok),'cured',sum(e[4] for e in ok))
    if lo==.10:
        for e in sorted(E,key=lambda e:-e[2])[:8]: print('   ',e[1]['NAMEFULL'][:30],e[1]['REPDTE'],round(e[2]*100,1),e[0],round(e[3],2) if e[0]=='ok' else '')
