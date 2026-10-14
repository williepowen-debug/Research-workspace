from pathlib import Path
import csv,json,hashlib,sys,datetime
ROOT=Path(__file__).resolve().parents[5];p=ROOT/'AGENTS/REGINALD/domain/sources/2026-10-13_bounded-securities-screen';sys.path.insert(0,str(ROOT/'AGENTS/REGINALD/scripts'));import mi3_cohort_screen as m
fields={'equity':'3210','assets':'2170','liabilities':'2948','minority':'3000','afs_cost':'1772','afs_fv':'1773','htm_cost':'1754','htm_fv':'1771','aoci':'B530','pledged':'0416','goodwill':'3163','intangibles':'JF76','other_borrowed':'3190','repo':'B995','cash_noninterest':'0081','cash_interest':'0071'}
extract=[];rows=[];checks=[]
def data(tk,q):
 rr=list(csv.DictReader((p/'raw'/f'{tk}_{q}.sdf').read_text().splitlines(),delimiter=';'));return {r['MDRM #']:r for r in rr}
def value(d,code,prefixes=('RCFD','RCON')):
 for pre in prefixes:
  k=pre+code
  if k in d:
   try:return float(d[k]['Value'].rstrip('%')),k
   except ValueError:return None,k
 return None,''
def sumv(d,keys):
 v=[]
 for k in keys:
  if k not in d:return None
  v.append(float(d[k]['Value']))
 return sum(v)
def ratio(a,b):return 100*a/b if a is not None and b is not None and b>0 else None
for tk,rssd,name,_ in m.COHORT:
 ds=[data(tk,q) for q in ['3-31-2026','6-30-2026']];nums=[]
 for q,d in zip(['2026-03-31','2026-06-30'],ds):
  n={}
  for f,c in fields.items():
   v,k=value(d,c);n[f]=v
   if k:extract.append({'ticker':tk,'quarter':q,**d[k]})
  for f,k in {'deposits_dom':'RCON2200','nib_dom':'RCON6631','ib_dom':'RCON6636','uninsured':'RCON5597','brokered':'RCON2365','reciprocal':'RCONJH83','fed_funds':'RCONB993','income_ytd':'RIAD4340','deposit_interest_ytd':'RIAD4073'}.items():
   n[f]=float(d[k]['Value']) if k in d else None
   if k in d:extract.append({'ticker':tk,'quarter':q,**d[k]})
  n['fhlb']=sum(value(d,'F0'+str(x))[0] for x in [55,56,57,58]) if all(value(d,'F0'+str(x))[0] is not None for x in [55,56,57,58]) else None
  for c in ['F055','F056','F057','F058']:
   _,k=value(d,c)
   if k:extract.append({'ticker':tk,'quarter':q,**d[k]})
  n['opt'],k=value(d,'P838',('RCOA','RCFA','RCON','RCFD'))
  if k:extract.append({'ticker':tk,'quarter':q,**d[k]})
  nums.append(n)
 a,b=nums
 assert all(b[f] is not None for f in ['equity','assets','liabilities','afs_cost','afs_fv','htm_cost','htm_fv'])
 assert b['equity']>0
 residual=b['assets']-b['liabilities']-(b['minority'] or 0)-b['equity'];assert abs(residual)<=2,(tk,residual)
 fv=b['afs_fv']+b['htm_fv'];gap=b['afs_cost']-b['afs_fv']+b['htm_cost']-b['htm_fv'];te=b['equity']-b['goodwill']-b['intangibles'] if b['goodwill'] is not None and b['intangibles'] is not None else None
 r={'ticker':tk,'rssd':rssd,'entity':name,'as_of':'2026-06-30',**{k+'_k':v for k,v in b.items() if k!='opt'},'aoci_opt_out':b['opt'],'tangible_equity_simple_k':te,'securities_fv_k':fv,'securities_fv_to_equity_x':fv/b['equity'],'existing_pretax_net_gap_k':gap,'existing_gap_pct_equity':ratio(gap,b['equity']),'aoci_pct_equity':ratio(b['aoci'],b['equity']),'uninsured_pct_dom_deposits':ratio(b['uninsured'],b['deposits_dom']),'brokered_pct_dom_deposits':ratio(b['brokered'],b['deposits_dom']),'pledged_pct_securities_carrying':ratio(b['pledged'],b['afs_fv']+b['htm_cost']),'deposit_change_qoq_pct':ratio(b['deposits_dom']-a['deposits_dom'],a['deposits_dom']),'nib_change_qoq_pct':ratio(b['nib_dom']-a['nib_dom'],a['nib_dom']),'fhlb_change_qoq_k':b['fhlb']-a['fhlb'] if a['fhlb'] is not None and b['fhlb'] is not None else None,'q2_net_income_k':b['income_ytd']-a['income_ytd'] if a['income_ytd'] is not None and b['income_ytd'] is not None else None,'duration_needed_20pct_equity_60bp':.2/(.006*fv/b['equity'])}
 for bp in [60,90]:
  for dur in [3,5]:
   loss=fv*dur*bp/10000;r[f'incremental_gross_{bp}bp_D{dur}_k']=loss;r[f'incremental_gross_{bp}bp_D{dur}_pct_equity']=ratio(loss,b['equity']);r[f'incremental_aftertax25_{bp}bp_D{dur}_pct_equity']=ratio(loss*.75,b['equity'])
  r[f'afs_aftertax25_{bp}bp_D5_k']=b['afs_fv']*5*bp/10000*.75
 rows.append(r);checks.append({'ticker':tk,'accounting_identity_residual_k':residual,'security_loss_identity':'AFS_cost-AFS_FV + HTM_cost-HTM_FV','missing_fields':[k for k,v in b.items() if v is None]})
# Cross-check reused June security figures without altering any frozen file.
prior=list(csv.DictReader([x for x in (ROOT/'AGENTS/REGINALD/workbook/AOCI_COHORT_2026Q2.tsv').read_text().splitlines() if not x.startswith('#')],delimiter='\t'))
for r in rows:
 old=next(x for x in prior if x['tk']==r['ticker']);c=next(c for c in checks if c['ticker']==r['ticker']);c['prior_security_differences_k']={k:r[new]-float(old[oldk]) for k,new,oldk in [('AFS_FV','afs_fv_k','afs_fv'),('HTM_cost','htm_cost_k','htm_ac'),('AFS_gap','existing_pretax_net_gap_k','afs_u')] if k!='AFS_gap'}
overlay_path=p/'disclosure-overlay.json'
if overlay_path.exists():
    overlays=json.loads(overlay_path.read_text())
    for row in rows: row.update(overlays[row['ticker']])
for name,rr in [('screen.tsv',rows),('primary-extract.tsv',extract)]:
 with (p/name).open('w') as f:
  w=csv.DictWriter(f,fieldnames=list(rr[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rr)
(p/'validation.json').write_text(json.dumps({'as_of':'2026-06-30','coverage':len(rows),'checks':checks,'sensitivity':'unhedged fixed-book first-order scenarios, NOT estimates of actual net bank losses','tax':'25% usable tax benefit is assumption, pre-tax ratios primary','scope':'GAAP bank equity denominator, not CET1, common or holding-company equity'},indent=2)+'\n')
for r in sorted(rows,key=lambda r:-r['securities_fv_to_equity_x']):print(r['ticker'],'E',round(r['equity_k']/1e6,3),'sec/E',round(r['securities_fv_to_equity_x'],2),'existing',round(r['existing_gap_pct_equity'],1),'new60D5',round(r['incremental_gross_60bp_D5_pct_equity'],1),'new90D5',round(r['incremental_gross_90bp_D5_pct_equity'],1),'D20',round(r['duration_needed_20pct_equity_60bp'],1),'deposit',round(r['deposit_change_qoq_pct'],1),'nib',round(r['nib_change_qoq_pct'],1),'FHLBdeltaM',round(r['fhlb_change_qoq_k']/1000,1),'pledged',round(r['pledged_pct_securities_carrying'],1))
