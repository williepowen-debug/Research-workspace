"""Bounded research arithmetic, not a grader or forecast generator. Run from any cwd."""
from pathlib import Path
from decimal import Decimal as D
import hashlib,json,re
from bs4 import BeautifulSoup
BASE=Path(__file__).resolve().parent
DESK=BASE.parents[2]

def delta(a,b):return float(D(str(b))-D(str(a)))
def pct(a,b):return float((D(str(b))/D(str(a))-1)*100)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
# Transcribed from visually inspected JM p6, WPIC pp19-20, Silver printed p9.
models={
 'JM_Pd_May14_koz':{'primary_2025':6589,'primary_2026F':6032,'recycling_2025':3135,'recycling_2026F':3427,'demand_2025':10140,'demand_2026F':9245,'balance_2025':-416,'balance_2026F':214},
 'JM_Pt_May14_koz':{'primary_2025':5557,'primary_2026F':5455,'recycling_2025':1547,'recycling_2026F':1576,'demand_2025':8019,'demand_2026F':7402,'balance_2025':-915,'balance_2026F':-371},
 'WPIC_Pt_Sept9_koz':{'primary_2025':5561,'primary_2026F':5551,'recycling_2025':1669,'recycling_2026F':1802,'demand_2025':8671,'demand_2026F':7089,'balance_2025':-1440,'balance_2026F':265},
 'Silver_April_Moz':{'primary_2025':846.6,'primary_2026F':844.1,'recycling_2025':197.6,'recycling_2026F':211.3,'hedging_2025':44.7,'hedging_2026F':10.0,'official_2025':1.5,'official_2026F':1.0,'demand_2025':1130.6,'demand_2026F':1112.6,'balance_2025':-40.3,'balance_2026F':-46.3}}
for key,m in models.items():
 growth=delta(m['recycling_2025'],m['recycling_2026F'])
 m['recycling_growth']=growth
 m['recycling_growth_pct']=pct(m['recycling_2025'],m['recycling_2026F'])
 m['primary_change']=delta(m['primary_2025'],m['primary_2026F'])
 m['demand_change']=delta(m['demand_2025'],m['demand_2026F'])
 # Sensitivity only: source headline balance, same-vintage recycling flat at 2025; all else fixed.
 m['flat_recycling_balance_sensitivity']=delta(growth,m['balance_2026F'])
 total=m['primary_2026F']+m['recycling_2026F']+m.get('hedging_2026F',0)+m.get('official_2026F',0)
 m['balance_recomputed_from_rounded_rows']=round(total-m['demand_2026F'],3)
 assert abs(m['balance_recomputed_from_rounded_rows']-m['balance_2026F'])<=1.001
assert models['JM_Pd_May14_koz']['flat_recycling_balance_sensitivity']==-78
assert models['WPIC_Pt_Sept9_koz']['flat_recycling_balance_sensitivity']==132
assert models['Silver_April_Moz']['flat_recycling_balance_sensitivity']==-60
val={
 'unit':'koz, 5E+Au except individual Pt/Pd; owned refined and sales exclude tolling',
 'Q3_2026':{'M_and_C':804.3,'own_mined':511.9,'POC':292.4,'refined':576.9,'sales':683.3,'Pt_refined':259.2,'Pd_refined':187.7,'Pt_sales':295.1,'Pd_sales':214.7,'toll_refined':209.2},
 'Q3_2025':{'M_and_C':855.1,'own_mined':539.6,'POC':315.5,'refined':981.5,'sales':936.8,'Pt_refined':440.3,'Pd_refined':310.4},
 'nine_months_2026':{'M_and_C':2323.2,'own_mined':1523.7,'POC':799.5,'refined':2318.8,'sales':2420.3,'Pt_refined':1100.8,'Pd_refined':706.7,'Pt_sales':1114.1,'Pd_sales':729.2},
 'nine_months_2025':{'M_and_C':2320.4,'own_mined':1465.7,'POC':854.7,'refined':2372.6,'sales':2412.1,'Pt_refined':1065.4,'Pd_refined':738.6}}
for period,old in [('Q3_2026','Q3_2025'),('nine_months_2026','nine_months_2025')]:
 now=val[period]
 assert abs(now['own_mined']+now['POC']-now['M_and_C'])<0.11
 now['YoY_pct']={k:pct(v,now[k]) for k,v in val[old].items()}
 now['sales_minus_owned_refined_proxy']=delta(now['refined'],now['sales'])
 now['Pt_sales_minus_owned_refined_proxy']=delta(now['Pt_refined'],now['Pt_sales'])
 now['Pd_sales_minus_owned_refined_proxy']=delta(now['Pd_refined'],now['Pd_sales'])
val['Q4_required_to_guidance']={k:{'low':delta(val['nine_months_2026'][k],3000),'mid':delta(val['nine_months_2026'][k],3200),'high':delta(val['nine_months_2026'][k],3400)} for k in ['refined','M_and_C']}
# Check table fields against archived issuer-distributed RNS, excluding Investegate's AI preamble.
soup=BeautifulSoup((BASE/'valterra_rns.html').read_text(),'html.parser')
tables=[' '.join(t.stripped_strings) for t in soup.find_all('table')]
refined=next(t for t in tables if '1,100.8' in t and len(t)<19000)
for fragment in ['259.2 486.9 354.7','187.7 285.1 234.0','2,318.8 2,372.6','2,420.3 2,412.1','1,100.8 1,065.4','706.7 738.6']:
 assert fragment in refined,fragment
sib={'period':'H1 2026 versus H1 2025; ounces recycled and sold excluding mixed scrap; consolidation differs', 'gold_2025':63992,'gold_2026':95188,'five_PGM_2025':155375,'five_PGM_2026':194926,'silver_2025':932712,'silver_2026':2498226,'total_2025':1152079,'total_2026':2788340}
for yr in ['2025','2026']:assert sum(sib[f'{m}_{yr}'] for m in ['gold','five_PGM','silver'])==sib[f'total_{yr}']
sib['silver_share_of_total_ounce_growth_pct']=100*delta(sib['silver_2025'],sib['silver_2026'])/delta(sib['total_2025'],sib['total_2026'])
gold={'unit':'tonnes; WGC estimated Q2 2026 versus Q2 2025','recycling_2025':346.7,'recycling_2026':326.1,'change_t':delta(346.7,326.1),'change_pct':pct(346.7,326.1)}
wpic_actual={'unit':'koz; WPIC September9 estimates of Q2 2026 realized period','recycling':466,'recycling_prior_year':429,'auto':374,'auto_prior_year':319,'jewellery':68,'jewellery_prior_year':90,'industrial':23,'industrial_prior_year':20,'note':'Components round to 465, not headline 466; preserve published rounding.'}
frozen={'workbook/PREDICTIONS.tsv':'67775106a453b5e1503c2c8b3fb3f1948355954e529583858db68b2e21c463aa','CLAUDE.md':'612756081ee84f0750908c6daed066b6cb2f8c39c07999827ab3fb2a2cceb198','palladium/research/2026-10-23_nornickel-9M-read-setup.md':'af8232d1df1da7bbaac7e2d3f9f40a8efa68ae293e0e8d639d94fcdecb24b2b6','gold/research/2026-10-23_WQ451-decomposition-letter.md':'c41c635417f40e66b963ce33a903ab6b5225a93e59977e3a84c8f7df62e316ea'}
for path,want in frozen.items():assert sha(DESK/path)==want,path
inherited=['sources/2026-10-12_thesis-test/jm_may2026_report.pdf','sources/2026-10-12_thesis-test/wpic_q2_2026.pdf','shared/sources/2026-10-26_coverage-gaps/wgc_q2_supply.html','shared/sources/2026-10-26_coverage-gaps/valterra_q3.html','shared/sources/2026-10-26_L701-settlement/issuer_full.pdf']
result={'models':models,'valterra':val,'sibanye':sib,'gold':gold,'wpic_actual':wpic_actual,'inherited_sources_sha256':{p:sha(DESK/p) for p in inherited},'frozen_sha256':frozen,'visual_review':['JM printed p6','WPIC printed pp19-20','Silver printed p9 / PDF page11'],'boundary':'All flat-recycling figures are ceteris-paribus sensitivities, not new forecasts. No blending models or adding closed-loop returns.'}
(BASE/'calculations.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'checks':'PASS','Pd_flat_recycling_koz':-78,'WPIC_Pt_flat_recycling_koz':132,'silver_flat_recycling_Moz':-60,'Valterra_Q4_required':val['Q4_required_to_guidance'],'frozen_files':len(frozen)},indent=2))
