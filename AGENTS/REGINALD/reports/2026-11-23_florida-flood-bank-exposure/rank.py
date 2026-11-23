import json
agg=json.load(open('agg.json'))
fin={str(r['data']['CERT']):r['data'] for r in json.load(open('fin0630.json'))['data']}
out=[]
for c,(info,a) in agg.items():
    f=fin.get(c)
    if not f or not f.get('DEP'): continue
    A=a.get('A',0);B=a.get('B',0);N=a.get('N',0)
    dep=f['DEP']; cap=(f.get('RBCT1J') or 0)+(f.get('RBCT2') or 0)
    cre=sum((f.get(k) or 0) for k in ('LNRECONS','LNREMULT','LNRENROT','LNCOMRE'))
    cons=f.get('LNRECONS') or 0
    nd=f.get('P3ASSET',0)+f.get('P9ASSET',0)+f.get('NAASSET',0)
    out.append(dict(cert=c,name=info[0],hq=info[2],asset=f['ASSET']/1e6,dep=dep/1e6,A=A/1e6,An=a.get('An',0),B=B/1e6,Bn=a.get('Bn',0),N=N/1e6,FL=a.get('FL',0)/1e6,
      shA=A/dep,shB=B/dep,shAB=(A+B)/dep,cre_cap=cre/cap if cap else None,cons_cap=cons/cap if cap else None,
      mf_cap=(f.get('LNREMULT') or 0)/cap if cap else None,cre=cre/1e6,cap=cap/1e6,pd=nd/ (f.get('LNLSGR') or 1)))
json.dump(out,open('ranked.json','w'))
def show(rows,title):
    print('==',title)
    for r in rows:
        print(f"{r['cert']:>6} {r['name'][:30]:30} {r['hq']} A{r['asset']:7.1f} dep{r['dep']:7.2f} | basin ${r['A']:.2f}B({r['An']}) {r['shA']*100:5.1f}% | SE ${r['B']:.2f}B({r['Bn']}) {r['shB']*100:5.1f}% | both {r['shAB']*100:5.1f}% | CRE/cap {r['cre_cap']*100 if r['cre_cap'] else 0:5.0f}% cons/cap {r['cons_cap']*100 if r['cons_cap'] else 0:4.0f}% MF/cap {r['mf_cap']*100 if r['mf_cap'] else 0:4.0f}% | PD+NA/loans {r['pd']*100:4.2f}%")
big=[r for r in out if r['A']+r['B']>=0.5]
show(sorted(big,key=lambda r:-r['shAB'])[:40],'>= $0.5B in flood+watch counties, by share of total deposits')
show(sorted([r for r in out if r['A']>=0.1],key=lambda r:-r['shA'])[:25],'basin >= $0.1B, by basin share')
