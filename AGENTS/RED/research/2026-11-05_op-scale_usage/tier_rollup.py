import re
D='AGENTS/RED/research/2026-11-05_op-scale_usage/usage_output_2026-11-05.txt'
L=open(D,encoding='utf-8').read().splitlines()
i=[k for k,l in enumerate(L) if l.startswith('CODEX')][0]
C={};K={}
for l in L[1:i]:
    m=re.match(r'(\S+)\s+files\s+\d+ fresh\+out\s+([\d,]+)\s+\S+ cacheread\s+([\d,]+)',l)
    if m:
        n=m[1].replace('+reader',''); a=C.setdefault(n,[0,0]); a[0]+=int(m[2].replace(',','')); a[1]+=int(m[3].replace(',',''))
for l in L[i+1:]:
    m=re.match(r'(.+?)\s+rollouts\s+\d+ fresh\+out\s+([\d,]+)\s+\S+ cached\s+([\d,]+)',l)
    if m: K[m[1].strip()]=[int(m[2].replace(',','')),int(m[3].replace(',',''))]
tiers={'Standing 4':"PROME WALTER TERRY RED",'On-call 13':"HENRY LIQUID VIOLET SAM BOND ZHAO VULCAN BROCK REGINALD DEWEY BRENT AEOLUS NEXUS",'On-call hold 5':"WAL OZK FLG MIDAS FALCON",'Dormant 19':"CARL LABOR HAWK MARCO ORACLE CORAL SHADE WATT OSPREY HOMER YURI CRUISE FERT GIBBS CYPHER ISHM CREED HANS OTTO",'Outside the 41':"DAEDALUS CATO RAV"}
F=sum(v[0] for v in C.values())+sum(v[0] for v in K.values()); A=F+sum(v[1] for v in C.values())+sum(v[1] for v in K.values())
print('combined fresh+output',f'{F:,}','all tokens incl cache',f'{A:,}')
for t,ns in tiers.items():
    f=sum(C.get(n,[0,0])[0]+K.get(n,[0,0])[0] for n in ns.split()); a=f+sum(C.get(n,[0,0])[1]+K.get(n,[0,0])[1] for n in ns.split())
    print(f'{t:16s} fresh+output {f:13,d} {f/F:6.1%}   all {a/A:6.1%}')
tot={n:C.get(n,[0,0])[0]+K.get(n,[0,0])[0] for n in set(C)|set(K)}
print('top:',' · '.join(f'{n} {v/F:.1%}' for n,v in sorted(tot.items(),key=lambda x:-x[1])[:14]))
print('RED',f"{tot['RED']/F:.1%}",'residual ROOT/home',f"{(tot.get('ROOT',0)+tot.get('home/willi',0))/F:.2%}")
