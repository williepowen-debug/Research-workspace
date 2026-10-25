"""Reproducible same-date SOI extraction; candidate matching never certifies loan identity."""
import argparse,collections,csv,html,itertools,json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('--inputs',required=True);ap.add_argument('--out',required=True);a=ap.parse_args()
repo=Path(__file__).resolve().parents[4];sys.path.insert(0,str(repo/'AGENTS/BROCK/research/2026-10-23_bdc-software-exposure/scripts'))
from rows import rows
from soi import industry_map,SOFT
out=Path(a.out);out.mkdir(exist_ok=True,parents=True)
local=lambda tag:tag.rsplit('}',1)[-1]
def name(t,id):
 if t=='HTGC':
  id=re.sub(r'^(Debt|Equity|Warrant) Investments, [^,]+, ','',id)
  id=re.split(r', (?:Senior Secured|Subordinated|Preferred|Common|Warrant)',id)[0]
 else:id=id.split(' | ')[0]
 id=html.unescape(id);id=re.sub(r'\s+\d+$','',id)
 id=re.split(r'\s*\((?:f/k/a|fka|dba|formerly|AKA)',id,flags=re.I)[0]
 id=re.sub(r'[^a-z0-9 ]',' ',id.lower());ws=id.split()
 while ws and ws[-1] in {'inc','incorporated','llc','ltd','limited','corp','corporation','lp','plc'}:ws.pop()
 return ' '.join(ws)
def terms(id,text):
 q=(id+' '+text).lower()
 tier='unknown'
 for pat,v in [(r'second.lien','second_lien'),(r'first.lien','first_lien'),(r'one stop|unitranche','unitranche'),(r'subordinated','subordinated'),(r'senior secured','senior_secured')]:
  if re.search(pat,q):tier=v;break
 ms=re.findall(r'\b(\d{1,2})/(20\d{2})\b',text)
 if ms:mat=f'{ms[-1][1]}-{int(ms[-1][0]):02}'
 else:
  m=re.search(r'\b(Jan\w*|Feb\w*|Mar\w*|Apr\w*|May|Jun\w*|Jul\w*|Aug\w*|Sep\w*|Oct\w*|Nov\w*|Dec\w*)[ .]+(20\d{2})',id,re.I)
  mat=f'{m[2]}-{["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"].index(m[1][:3].lower())+1:02}' if m else ''
 base='SOFR' if re.search(r'\b(?:s|sf|sofr)\s*\+|sofr',q) else 'PRIME' if re.search(r'prime|\bp\s*\+',q) else 'SONIA' if re.search(r'sonia|\bsa\s*\+',q) else 'EURIBOR' if re.search(r'euribor|\be\s*\+',q) else 'unknown'
 return tier,mat,base
allpos=[];summary=[];commitments=[];facts_by_t={}
for t,paths in json.loads(Path(a.inputs).read_text()).items():
 root=ET.parse(paths['xml']).getroot();contexts={};units={};current=set()
 for e in root:
  if local(e.tag)=='unit':units[e.attrib['id']]=' '.join(x.text or '' for x in e.iter() if local(x.tag)=='measure').split(':')[-1].upper()
  if local(e.tag)!='context':continue
  ins=e.find('.//{*}instant');typed=[x for x in e.iter() if local(x.tag)=='typedMember' and x.attrib.get('dimension','').endswith(':InvestmentIdentifierAxis')]
  dims=[x.attrib.get('dimension','') for x in e.iter() if local(x.tag) in ['typedMember','explicitMember']]
  if ins is not None and ins.text=='2026-06-30':current.add(e.attrib['id'])
  if ins is not None and ins.text=='2026-06-30' and typed and len(dims)==1:contexts[e.attrib['id']]=''.join(typed[0].itertext()).strip()
 facts=collections.defaultdict(dict)
 for e in root:
  c=e.attrib.get('contextRef');tag=local(e.tag)
  if c not in contexts:continue
  if e.text is None:continue
  try:v=float(e.text)
  except ValueError:continue
  if tag in facts[c] and facts[c][tag]!=v:raise ValueError((t,c,tag,'conflicting facts'))
  facts[c][tag]=v
  if tag=='InvestmentOwnedBalancePrincipalAmount':facts[c]['currency']=units.get(e.attrib.get('unitRef'),e.attrib.get('unitRef','').upper())
 mp,order=industry_map(paths['html'],t);rowmap={};k=0;boundary=None
 for texts,ff in rows(paths['html']):
  if ff:k+=1
  # Grand total of the FIRST SOI, not later JV look-through/roll-forward tables.
  label=texts[0].lower().replace('—','-') if texts else ''
  grand=(label=='total investments' or label.startswith('total investments-') or label.startswith('total investments in securities') or label.startswith('total portfolio investments, cash'))
  if t=='HTGC':grand=label.startswith('total investments before cash')
  if k>100 and grand:
   boundary=k;break
  for tag,c in ff:
   # GBDC tags 15 unique security rows by industry/affiliation/type, without an InvestmentIdentifier axis.
   if t=='GBDC' and c in current and c not in contexts and tag.endswith(':InvestmentOwnedAtFairValue') and texts and re.match('[A-Za-z]',texts[0]) and not texts[0].lower().startswith(('total','subtotal','non-controlled','controlled')):
    contexts[c]=re.sub(r'\([^)]*\)|[+*]','',texts[0]).strip();rowmap[c]=texts
   if c in contexts and tag.endswith(':InvestmentOwnedAtFairValue'):rowmap.setdefault(c,texts)
 # Reload numerical facts to include the audited GBDC security contexts recovered above.
 for e in root:
  c=e.attrib.get('contextRef');tag=local(e.tag)
  if c not in contexts or e.text is None:continue
  try:v=float(e.text)
  except ValueError:continue
  facts[c][tag]=v
  if tag=='InvestmentOwnedBalancePrincipalAmount':facts[c]['currency']=units.get(e.attrib.get('unitRef'),e.attrib.get('unitRef','').upper())
 pos=[]
 for c,id in contexts.items():
  f=facts[c];tr=rowmap.get(c)
  if 'InvestmentCompanyFinancialCommitmentToInvesteeFutureAmount' in f:
   commitments.append({'ticker':t,'ctx':c,'borrower':name(t,id),'id':html.unescape(id),'unfunded':f['InvestmentCompanyFinancialCommitmentToInvesteeFutureAmount']})
  if 'InvestmentOwnedAtFairValue' not in f or tr is None:continue
  if t=='HTGC' and re.search(r', Total ',id):continue
  text=' | '.join(tr);fv=f['InvestmentOwnedAtFairValue'];cost=f.get('InvestmentOwnedAtCost',0);par=f.get('InvestmentOwnedBalancePrincipalAmount',0);cur=f.get('currency','')
  soft=bool(mp.get(c) and re.fullmatch(SOFT[t],mp[c]));tier,mat,base=terms(id,text)
  explicit_unfunded=t=='FSK' and any(re.search(r'\(x\)',z) for z in tr[:3]) or t=='GBDC' and any(re.search(r'\(6\)',z) for z in tr[:3])
  state='unfunded' if explicit_unfunded else 'funded_debt' if par>0 else 'no_positive_principal'
  if mp.get(c)=='Cash and Cash Equivalents' or 'money market fund' in id.lower():state='cash_equivalent'
  r={'ticker':t,'ctx':c,'id':html.unescape(id),'borrower':name(t,id),'industry':mp.get(c),'software':soft,'state':state,'currency':cur,'par':par,'cost':cost,'fv':fv,'mark':fv/par if par>0 else None,'tier':tier,'maturity':mat,'base':base,'spread':f.get('InvestmentBasisSpreadVariableRate'),'floor':f.get('InvestmentInterestRateFloor'),'pik':f.get('InvestmentInterestRatePaidInKind',0),'row':tr}
  pos.append(r);allpos.append(r)
 core=[r for r in pos if r['software'] and r['state']=='funded_debt' and r['currency']=='USD']
 other=[r for r in pos if r['software'] and r['state']=='funded_debt' and r['currency']!='USD']
 def stats(rr):
  par=sum(r['par'] for r in rr);fv=sum(r['fv'] for r in rr)
  return {'n':len(rr),'par_m':par/1e6,'fv_m':fv/1e6,'mark_pct':100*fv/par if par else None,'below80_par_pct':100*sum(r['par'] for r in rr if r['mark']<.8)/par if par else None,'below90_par_pct':100*sum(r['par'] for r in rr if r['mark']<.9)/par if par else None,'pik_bearing_fv_pct':100*sum(r['fv'] for r in rr if r['pik']>0)/fv if fv else None}
 summary.append({'ticker':t,'soi_boundary_factrow':boundary,'positions':len(pos),'all_fv_m':sum(r['fv'] for r in pos)/1e6,'software_all_fv_m':sum(r['fv'] for r in pos if r['software'])/1e6,'software_usd_funded':stats(core),'software_other_currency_funded':{c:{'n':len([r for r in other if r['currency']==c]),'fv_usd_m':sum(r['fv'] for r in other if r['currency']==c)/1e6,'cost_usd_m':sum(r['cost'] for r in other if r['currency']==c)/1e6,'par_native_m':sum(r['par'] for r in other if r['currency']==c)/1e6,'mark':'NOT_COMPUTED_NO_FX_CONVERSION'} for c in sorted({r['currency'] for r in other})},'software_unfunded_rows':sum(r['software'] and r['state']=='unfunded' for r in pos),'unfunded_tagged_m':sum(r['unfunded'] for r in commitments if r['ticker']==t)/1e6})
 print(t,json.dumps(summary[-1]))
(out/'positions.json').write_text(json.dumps(allpos,indent=2)+'\n');(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');(out/'commitments.json').write_text(json.dumps(commitments,indent=2)+'\n')
# Full-name borrower overlap is deliberately a candidate set, not a matched tranche result.
groups=collections.defaultdict(list)
for r in allpos:
 if r['state']=='funded_debt' and r['currency']=='USD':groups[r['borrower']].append(r)
pairs=[];strict=[]
for borrower,rr in groups.items():
 ticks={r['ticker'] for r in rr}
 if len(ticks)<2 or not any(r['software'] for r in rr):continue
 agg={t:[r for r in rr if r['ticker']==t] for t in ticks};agg={t:r for t,r in agg.items() if sum(x['par'] for x in r)>2e6}
 for t,u in itertools.combinations(sorted(agg),2):
  x,y=agg[t],agg[u];xp=sum(r['par'] for r in x);yp=sum(r['par'] for r in y);xm=sum(r['fv'] for r in x)/xp;ym=sum(r['fv'] for r in y)/yp
  pairs.append({'borrower':borrower,'a':t,'b':u,'a_mark':100*xm,'b_mark':100*ym,'gap_pp':100*(xm-ym),'a_par_m':xp/1e6,'b_par_m':yp/1e6,'both_software':any(r['software'] for r in x) and any(r['software'] for r in y)})
  for v,w in itertools.product(x,y):
   key=lambda r:(r['tier'],r['maturity'],r['base'],r['spread'])
   if key(v)!=key(w) or v['tier']=='unknown' or not v['maturity'] or v['base']=='unknown' or v['spread'] is None:continue
   strict.append({'borrower':borrower,'a':t,'b':u,'a_ctx':v['ctx'],'b_ctx':w['ctx'],'a_id':v['id'],'b_id':w['id'],'tier':v['tier'],'maturity':v['maturity'],'base':v['base'],'spread':v['spread'],'a_mark':100*v['mark'],'b_mark':100*w['mark'],'gap_pp':100*(v['mark']-w['mark']),'a_par_m':v['par']/1e6,'b_par_m':w['par']/1e6,'both_software':v['software'] and w['software']})
(out/'borrower_pairs.json').write_text(json.dumps(pairs,indent=2)+'\n');(out/'same_disclosed_terms_candidates.json').write_text(json.dumps(strict,indent=2)+'\n')
print('Borrower pairs',len(pairs),'names',len({x['borrower'] for x in pairs}),'same-disclosed-terms candidates',len(strict))

# Independent issuer total checks: main SOI rows and separately disclosed bridges (USD millions).
by={x['ticker']:x for x in summary}
obdc_commit_ctx={x['ctx'] for x in commitments if x['ticker']=='OBDC'}
# Re-read current OBDC facts; commitment set above is typed and date-filtered.
rt=ET.parse(json.loads(Path(a.inputs).read_text())['OBDC']['xml']).getroot()
obdc_unfunded_fv=sum(float(e.text) for e in rt if local(e.tag)=='InvestmentOwnedAtFairValue' and e.attrib.get('contextRef') in obdc_commit_ctx and e.text)/1e6
cash_bxsl=sum(r['fv'] for r in allpos if r['ticker']=='BXSL' and r['state']=='cash_equivalent')/1e6
bridges={'ARCC':(0,29349.3),'BXSL':(-cash_bxsl,13364.295),'FSK':(-1111.0,11418.1),'GBDC':(0,8196.353),'HTGC':(0,4583.870),'OBDC':(obdc_unfunded_fv,14955.049)}
checks=[]
for t,(adj,target) in bridges.items():
 actual=by[t]['all_fv_m']+adj;delta=actual-target
 checks.append(dict(ticker=t,extracted_fv_m=by[t]['all_fv_m'],bridge_m=adj,reconciled_fv_m=actual,issuer_investments_fv_m=target,difference_m=delta))
 if abs(delta)>.00001:raise ValueError(('ISSUER_TIE_FAILED',t,delta))
(out/'reconciliation.json').write_text(json.dumps(checks,indent=2)+'\n')
fields=['ticker','ctx','id','borrower','industry','software','state','currency','par','cost','fv','mark','tier','maturity','base','spread','floor','pik']
with (out/'positions.csv').open('w',newline='') as fp:
 wr=csv.DictWriter(fp,fieldnames=fields,extrasaction='ignore');wr.writeheader();wr.writerows(allpos)
print('All six issuer investment FV totals reconciled.')
