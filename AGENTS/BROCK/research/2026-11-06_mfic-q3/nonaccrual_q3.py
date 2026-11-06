# Non-accrual tabulation from SOI footnote 14, MFIC 9/30 vs 6/30. Run from a directory holding mfic_q3.htm and mfic_q2.htm. Parser check: cost share ties to 4.6% and 7.9%.
import re,sys,html,collections,json
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/BROCK/research/2026-10-23_bdc-software-exposure/scripts')
from rows import rows
res={}
NUM=re.compile(r'^[\d,]+(\.\d+)?$')
def val(c): return 0.0 if c in('—','-','–') else float(c.replace(',',''))
for t in ['mfic_q3','mfic_q2']:
    out=list(rows(t+'.htm'))
    end=next(i for i,(tx,ff) in enumerate(out) if any(c.lower().startswith('total investments') for c in tx) and ff)
    ent=None; g=collections.defaultdict(lambda:[0.0,0.0]); bad=[]
    for tx,ff in out[:end]:
        if not tx: continue
        if not re.match(r'(First Lien|Second Lien|Unsecured|Subordinated|Preferred|Common|Warrant|Structured|Secured Debt|Total)',tx[0]): ent=tx[0]
        j=' '.join(tx)
        if not re.search(r'\(\s*14\s*\)',j) or not ff: continue
        # numeric/dash cells, keep order, drop footnote cells and rates/dates
        cells=[c for c in tx if (NUM.match(c) or c in('—','–'))]
        if len(cells)<2: bad.append(tx); continue
        cost,fv=val(cells[-2]),val(cells[-1])
        g[re.sub(r'\s*\(\d+\)','',ent)[:44]][0]+=cost; g[re.sub(r'\s*\(\d+\)','',ent)[:44]][1]+=fv
    res[t]=g
    print(t,'NA entities',len(g),'cost',round(sum(v[0] for v in g.values())/1e3,1),'fv',round(sum(v[1] for v in g.values())/1e3,1),'unparsed',len(bad))
new=set(res['mfic_q3'])-set(res['mfic_q2']); gone=set(res['mfic_q2'])-set(res['mfic_q3'])
print('NEW'); [print('  ',k,[round(x/1e3,1) for x in res['mfic_q3'][k]]) for k in sorted(new,key=lambda k:-res['mfic_q3'][k][0])]
print('GONE'); [print('  ',k,[round(x/1e3,1) for x in res['mfic_q2'][k]]) for k in sorted(gone,key=lambda k:-res['mfic_q2'][k][0])]
print('BOTH'); [print('  ',k,[round(x/1e3,1) for x in res['mfic_q2'][k]],'->',[round(x/1e3,1) for x in res['mfic_q3'][k]]) for k in sorted(set(res['mfic_q2'])&set(res['mfic_q3']))]
