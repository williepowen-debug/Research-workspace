from pathlib import Path
import json,hashlib
p=Path(__file__).resolve().parent
loans=[
 {'case':'PG apartments','bridge_id':'WOB-REG-008','balance':56.0,'q1_grade':'SPECIAL_MENTION','q2_grade':'SUBSTANDARD','q1_maturity':'2026-04-21','q2_maturity':'2026-08-21','q2_dscr':.63,'dscr_date':'2026-04-30','appraisal':63.7,'appraisal_date':'2026-03-09','outcome':'UNKNOWN'},
 {'case':'Montgomery storage','bridge_id':'WOB-REG-013','balance':56.196,'q1_grade':'SPECIAL_MENTION','q2_grade':'SPECIAL_MENTION','q2_maturity':'2026-08-10','q2_dscr':.93,'dscr_date':'2026-03-31','appraisal':77.7,'appraisal_date':'2022-07-27','outcome':'UNKNOWN'},
 {'case':'Fairfax office','bridge_id':'WOB-REG-009','balance':22.072,'q1_grade':'SUBSTANDARD','q2_grade':'SUBSTANDARD','q1_maturity':'2026-06-25','q2_maturity':'2026-09-25','q2_dscr':.74,'dscr_date':'2026-03-31','appraisal':23,'appraisal_date':'2026-04-02','outcome':'UNKNOWN'},
 {'case':'Anne Arundel storage','bridge_id':'WOB-REG-014','balance':14.996,'q1_grade':'SPECIAL_MENTION','q2_grade':'SUBSTANDARD','q2_maturity':'2026-09-30','q2_dscr':.26,'dscr_date':'2026-03-31','appraisal':19.58,'appraisal_date':'2022-06-13','outcome':'UNKNOWN'}]
# Manually transcribed from visually inspected Q2 slide25 and Q1 slide27.
# Loans remain June-baseline exposures, not new October balance observations.
inputs={'opening_nonaccrual':128.761,'inflows':36.038,'paydowns':14.658,'chargeoffs':24.982,'hfs_transfers':14.035,'ending_nonaccrual':111.124}
x=inputs
assert abs(x['opening_nonaccrual']+x['inflows']-x['paydowns']-x['chargeoffs']-x['hfs_transfers']-x['ending_nonaccrual'])<1e-8
outflows=x['paydowns']+x['chargeoffs']+x['hfs_transfers']
scenarios=[]
for decline in [0,.10,.20]:
 value=63.7*(1-decline);net=value*(1-.08);gap=max(0,56-net)
 scenarios.append({'appraisal_decline_assumption':decline,'sale_cost_assumption':.08,'gross_sale_value':value,'net_sale_value':net,'gross_shortfall_before_existing_recognition':gap})
# THESE ARE NOT LOAN-LOSS FORECASTS. Priority, other claims, cash support,
# prior loan-level allowances and appraised-value realization are unverified.
verified=[]
for receipt_name in ['retrieval.json','extra-retrieval.json']:
 for r in json.loads((p/receipt_name).read_text()):
  if r.get('status')!=200:continue
  ext='json' if r['id']=='SEC-submissions' else 'jpg' if r['url'].endswith('.jpg') else 'pdf' if r['url'].endswith('.pdf') else 'html'
  f=p/(r['id']+'.'+ext);assert hashlib.sha256(f.read_bytes()).hexdigest()==r['sha256'];verified.append(f.name)
res={'loans':loans,'q2_nonaccrual_bridge':inputs,'gross_nonaccrual_outflows':outflows,'paydown_share_of_gross_outflows':x['paydowns']/outflows,'chargeoff_and_transfer_share':(x['chargeoffs']+x['hfs_transfers'])/outflows,'pg_sale_scenarios_not_forecasts':scenarios,'pg_decline_to_exhaust_appraisal_cushion_with_8pct_costs':1-56/(63.7*.92),'verified_downloads':verified}
(p/'calculations.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
