"""Reproducible conditional diagnostics; no forecast, valuation target or scored rule."""
from pathlib import Path
import json,csv,hashlib
from decimal import Decimal as D

BASE=Path(__file__).resolve().parent
q={'nii':796.9,'noninterest':198.8,'op_ex_deposit':404.1,'deposit_expense':179.2,'total_expense':583.3,'ppnr':412.4,'provision':80.4,'pretax':332.0,'tax':63.2,'nci':7.1,'preferred':3.2,'awards':3.3,'shares':108.0,'eps':2.36,'earning_assets':91661.0}
current=json.loads((BASE/'current-consensus.json').read_text())
assert current['sources']['info']['symbol']=='WAL'
eps=current['sources']['earnings_estimate']
rev=current['sources']['revenue_estimate']
R=rev['+1y']['avg']/1e6/4
tax=.19; shares=108.; deductions=13.6
def annual_eps(revenue,expenses,provision,rate=tax,nshares=shares):
    return 4*((revenue-expenses-provision)*(1-rate)-deductions)/nshares
def required_pretax(target,rate=tax,nshares=shares):
    return (target*nshares/4+deductions)/(1-rate)
def expense_ceiling(target,provision,rate=tax,nshares=shares):
    return R-provision-required_pretax(target,rate,nshares)
target=11.
scenarios=[]
for growth,provision in [(0.02,80.4),(.05,80.4),(.05,100),(.10,100)]:
    expense=q['total_expense']*(1+growth)
    scenarios.append({'cost_growth_vs_Q2':growth,'quarter_revenue_M':R,'quarter_expense_M':expense,'quarter_provision_M':provision,'annual_eps':annual_eps(R,expense,provision)})
volume_only_ECR=214.3*(31.6/29.4)*(91/90)
data={
 'basis':'2027 average quarter against Q2-2026; 19pct tax,108M diluted shares,$13.6M quarterly NCI/preferred/award deductions unless stated. Revenue vendor basis unharmonized; no retrieved component analyst model.',
 'Q2_parent':q,
 'consensus':{'FY26_EPS':eps['0y']['avg'],'FY27_EPS':eps['+1y']['avg'],'FY26_revenue_M':rev['0y']['avg']/1e6,'FY27_revenue_M':rev['+1y']['avg']/1e6,'EPS_growth_pct':100*(eps['+1y']['avg']/eps['0y']['avg']-1),'revenue_growth_pct':100*(rev['+1y']['avg']/rev['0y']['avg']-1),'FY27_estimate_vs_90day_pct':100*(eps['+1y']['avg']/current['sources']['eps_trend']['+1y']['90daysAgo']-1),'quarter_revenue_M':R},
 'budget':{'target_EPS':target,'required_pretax_M':required_pretax(target),'expense_ceiling_provision80_4_M':expense_ceiling(target,80.4),'expense_growth_ceiling_provision80_4_pct':100*(expense_ceiling(target,80.4)/583.3-1),'expense_ceiling_provision86_M':expense_ceiling(target,86),'expense_growth_ceiling_provision86_pct':100*(expense_ceiling(target,86)/583.3-1),'expense_ceiling_at_vendor_EPS80_4_M':expense_ceiling(eps['+1y']['avg'],80.4),'expense_ceiling_shares106_provision80_4_M':expense_ceiling(target,80.4,nshares=106),'expense_ceiling_tax17_provision80_4_M':expense_ceiling(target,80.4,rate=.17),'expense_ceiling_tax21_provision80_4_M':expense_ceiling(target,80.4,rate=.21)},
 'scenarios':scenarios,
 'ECR':{'Q1_total_M':214.3,'Q2_total_M':234.2,'Q1_average_balance_B':29.4,'Q2_average_balance_B':31.6,'Q2_end_balance_B':29.9,'Q1_all_in_annualized_cost_pct':100*214.3/29400*365/90,'Q2_all_in_annualized_cost_pct':100*234.2/31600*365/91,'Q2_at_Q1_per_day_per_dollar_M':volume_only_ECR,'calendar_and_balance_explained_share_of_change_pct':100*(volume_only_ECR-214.3)/(234.2-214.3),'remaining_rate_mix_rounding_M':234.2-volume_only_ECR,'balance_at29_9_B_same_unit_cost_saving_per91day_quarter_M':234.2*(1-29.9/31.6),'NII_change_less_ECR_change_outside_NII_M':(796.9-766.3)-((234.2-214.3)-(52.5-48.7)),'no_double_count_PPNR_check_M':(796.9+52.5)+(198.8+8.4)-404.1-234.2-5.9},
 'mortgage':{'Q1_origination_sale_M':72.7,'Q2_origination_sale_M':53.4,'Q1_net_servicing_M':-1.3,'Q2_net_servicing_M':31.3,'Q1_reported_total_M':71.4,'Q2_reported_total_M':84.7,'Q2_MSR_fair_value_M':12.,'Q2_MSR_hedge_income_M':-10.8,'Q2_MSR_mark_plus_hedge_M':1.2,'Q2_contractual_servicing_ancillary_fees_M':80.1,'Q2_early_payoff_fee_M':4.9,'Q2_MSR_cashflow_realization_M':-54.,'Q2_MSR_sale_loss_M':-3.5,'partial_servicing_bridge_M':80.1+4.9+12-54-10.8-3.5,'partial_bridge_residual_other_rounding_M':31.3-(80.1+4.9+12-54-10.8-3.5),'Q2_production_B':16.2,'Q2_lock_volume_B':17.7,'Q2_GOS_bp':29.,'Q1_GOS_bp':37.,'Q2_GOS_vs_Q1_pct':100*(29/37-1)},
 'credit_and_base_effect':{'Q1_total_provision_M':213.2,'Q1_LAM_incremental_provision_M':126.4,'Q1_Cantor_chargeoff_existing_reserve_M':26.1,'Q1_security_sales_gain_M':50.5,'Q1_GAAP_EPS':1.65,'Q1_issuer_adjusted_EPS':2.22,'Q1_issuer_adjustment_EPS':.57,'FY26_if_GAAP_vendor_then_one_Q1_adjustment_EPS':eps['0y']['avg']+.57,'FY27_growth_on_that_conditional_base_pct':100*(eps['+1y']['avg']/(eps['0y']['avg']+.57)-1),'warning':'Apply the conditional FY26 adjustment only if vendor annual basis is proven GAAP; otherwise could double count. Quarterly rounded EPS subtraction is approximate.'},
 'limitations':['No analyst NII/expense/provision/share/tax forecasts; EPS/revenue panels differ, bases/update dates unknown.','Four identical quarters average a forecast year; not Q3 targets.','Expense growth compares FY27-average-quarter to Q2-2026; not growth over FY26 consensus.','Conditional sensitivities do not estimate expected losses, funded commitments or price-implied beliefs.','ECR unit costs use rounded aggregate balances,actual90/91-day denominators,and varying populations; not same-customer betas or a price-only decomposition.','Mortgage partial bridge residual is other/rounding not assumed cash earnings; marks plus hedges are net,not separate losses.'],
}
# Independent Decimal reverse check and reconciliation identities.
pd=(D('11')*D('108')/D('4')+D('13.6'))/D('.81')
assert abs(float(pd)-data['budget']['required_pretax_M'])<1e-9
assert abs(q['nii']+q['noninterest']-q['total_expense']-q['provision']-q['pretax'])<1e-8
assert abs(data['ECR']['no_double_count_PPNR_check_M']-q['ppnr'])<1e-8
assert abs(52.5+8.4+173.3-234.2)<1e-8
assert abs(48.7+8.3+157.3-214.3)<1e-8
assert abs(annual_eps(R,expense_ceiling(target,80.4),80.4)-target)<1e-8
source_claims=[]
tables=json.loads((BASE/'Q2_10Q-tables.json').read_text())
for idx in [14,31,55,59,72,73,98,103,107,110,134]:
    source_claims.append({'source':'Q2 preserved issuer10Q','url':'https://www.sec.gov/Archives/edgar/data/1212545/000162828026051418/wal-20260630.htm','zero_based_HTML_table':idx,'text':tables[idx]})
(BASE/'primary-claim-extracts.json').write_text(json.dumps(source_claims,indent=2)+'\n')
(BASE/'calculations.json').write_text(json.dumps(data,indent=2)+'\n')
with (BASE/'conditional-cost-credit-scenarios.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=list(scenarios[0]),lineterminator='\n');w.writeheader();w.writerows(scenarios)
print(json.dumps({k:v for k,v in data.items() if k not in ['Q2_parent','limitations']},indent=2))
print('PASS: Decimal reverse,EPS target,PPNR,all three ECR channels; no primary-source identity substitutes for accuracy')
