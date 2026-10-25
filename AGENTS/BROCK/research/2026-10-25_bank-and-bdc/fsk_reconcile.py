import sys,json,re,collections
from pathlib import Path
import argparse
ap=argparse.ArgumentParser()
ap.add_argument('--html',required=True)
ap.add_argument('--xml',required=True)
ap.add_argument('--output',required=True)
a=ap.parse_args()
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'2026-10-23_bdc-software-exposure/scripts'))
from rows import rows
from soi import load_xbrl
ctx,facts=load_xbrl(a.xml,'2026-06-30')
seen=set();positions=[]
for texts,fs in rows(a.html):
 for name,c in fs:
  if not name.endswith(':InvestmentOwnedAtFairValue') or c not in ctx or c in seen:continue
  ident,dims=ctx[c]
  if ' | ' not in ident or re.search(r'\bTotal\b',ident):continue
  # Current-period source rows only; prior-period contexts not in ctx.
  seen.add(c)
  ind=texts[2] if len(texts)>2 else None
  if ind!='Software & Services':continue
  f=facts[c]
  if 'InvestmentOwnedBalancePrincipalAmount' not in f:continue
  par=f['InvestmentOwnedBalancePrincipalAmount'] if f.get('par_unit')=='usd' else f.get('InvestmentOwnedAtCost',0)
  if par<=0:continue
  positions.append(dict(ctx=c,id=ident,unfunded=any(re.search(r'\(x\)',v) for v in texts[:3]),fv=f.get('InvestmentOwnedAtFairValue',0),cost=f.get('InvestmentOwnedAtCost',0),par=par,source_row=texts))
def stat(rr):
 par=sum(x['par'] for x in rr);fv=sum(x['fv'] for x in rr);cost=sum(x['cost'] for x in rr)
 return {'n':len(rr),'par_m':par/1e6,'fv_m':fv/1e6,'cost_m':cost/1e6,'mark':100*fv/par,'below80_par_share':100*sum(x['par'] for x in rr if x['fv']/x['par']<.8)/par,'below90_par_share':100*sum(x['par'] for x in rr if x['fv']/x['par']<.9)/par}
gross=stat(positions);funded=stat([x for x in positions if not x['unfunded']]);u=stat([x for x in positions if x['unfunded']])
res={'gross':gross,'funded':funded,'unfunded':u,'rows':positions,'bridge_m':{'first_lien':1069.9,'subordinated':7.9,'asset_based_finance':33.2,'total_unfunded':1111.0,'money_market':15.4,'original_gap':1126.4,'gross_sections_cost':13715.8,'gross_sections_fv':12529.1,'balance_cost':12604.8,'balance_fv':11418.1}}
Path(a.output).write_text(json.dumps(res,indent=2))
print(json.dumps({k:v for k,v in res.items() if k!='rows'},indent=2))
print('unfunded rows sample',[(x['id'][:60],x['fv']/1e6) for x in positions if x['unfunded']][:4])
assert abs(13715.8-1111.0-12604.8)<1e-6
assert abs(12529.1-1111.0-11418.1)<1e-6
