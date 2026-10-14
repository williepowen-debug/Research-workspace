"""Reproduce conditional WAL EPS bridges; this is not a forecast or grader."""
from pathlib import Path
import json, hashlib
from bs4 import BeautifulSoup

WAL = Path(__file__).resolve().parents[1]
TAX, SHARES, DEDUCTIONS = .19, 108., 13.6
cases = {
    'reported_Q2_at_assumed_tax': [796.9, 198.8, 404.1, 179.2, 80.4],
    'Q2_gain_screen': [796.9, 183., 404.1, 179.2, 80.4],
    'conditional_11_support': [876.9, 193., 424.1, 176.2, 86.],
    'conditional_8_pressure': [781.9, 183., 412.1, 184.2, 85.4],
}
results = {}
for name, (nii, income, operating, deposits, provision) in cases.items():
    ppnr = nii + income - operating - deposits
    pretax = ppnr - provision
    results[name] = dict(nii=nii, noninterest_income=income,
        operating_ex_deposit_costs=operating, deposit_cost_expense=deposits,
        provision=provision, ppnr=ppnr, pretax=pretax,
        annual_eps=4*(pretax*(1-TAX)-DEDUCTIONS)/SHARES)
base = results['Q2_gain_screen']['pretax']
target = lambda eps, shares: (eps*shares/4+DEDUCTIONS)/(1-TAX)
receipt = {
    'analysis_date_ET':'2026-10-14', 'source_quarter':'2026-06-30',
    'units':'USD millions except EPS, ratios and basis points',
    'formula':'annual_EPS = 4*((NII + noninterest_income - operating_ex_deposit_costs - deposit_cost_expense - provision)*(1-tax) - NCI - preferred_dividends - participating_awards)/diluted_shares',
    'assumptions':{'tax':TAX,'diluted_shares_M':SHARES,
        'quarterly_NCI_M':7.1,'preferred_dividends_M':3.2,'participating_awards_M':3.3,
        'annualization':'four identical quarters, no seasonality or transition timing'},
    'observed_Q2':{'GAAP_EPS':2.36,'common_income_M':258.5,'ordinary_earnings_M':255.2,
        'actual_tax_M':63.2,'actual_pretax_M':332.,'gain_screen_removed_M':15.8,
        'security_sales_gain_M':3.,'net_FV_gain_adjustments_M':12.8,
        'equity_investment_income_retained_M':11.9},
    'results':results,
    'required_quarterly_pretax':{'EPS11_108Mshares':target(11,108),
        'EPS11_minus_gain_screen':target(11,108)-base,
        'EPS8_108Mshares':target(8,108),
        'EPS8_minus_gain_screen':target(8,108)-base,
        'EPS11_106Mshares':target(11,106),
        'EPS11_106M_minus_gain_screen':target(11,106)-base,
        'EPS11_05_minus_EPS8':target(11.05,108)-target(8,108)},
    'sensitivities':{
        'annual_EPS_per_10M_quarterly_pretax':10*(1-TAX)*4/SHARES,
        'quarter_EPS_per_10M_one_time_new_provision':10*(1-TAX)/SHARES,
        'annual_EPS_if_also_remove_11_9M_equity_income':results['Q2_gain_screen']['annual_eps']-11.9*(1-TAX)*4/SHARES,
        'annual_EPS_per_10bp_net_yield_on_fixed_91661M_earning_assets':91661*.001*(1-TAX)/SHARES,
        'NII_if_6pct_growth_only_M':796.9*1.06,
        'extra_quarter_NII_to_876_9M_after_6pct_growth_M':876.9-796.9*1.06,
        'equivalent_extra_yield_bp_after_6pct_growth':(876.9-796.9*1.06)*4/(91661*1.06)*10000,
        'quarter_EPS_if_99M_is_incremental_new_provision':99*(1-TAX)/SHARES},
    'source_SHA256':hashlib.sha256((WAL/'sources/q2_2026/wal-20260630.htm').read_bytes()).hexdigest(),
    'limitations':['conditional component mixes are WAL judgments, not analyst models',
        '19pct assumed tax approximates actual 63.2/332; GAAP EPS and rounding differ',
        'gain removal is a screen, not issuer adjusted EPS or proof the gains will not recur',
        'charge-offs can use existing allowance and are not automatically incremental provision',
        'ECR/referral reductions already enter NII and fees; do not subtract twice'],
}
for p, value in [('Q2_GRADING_FRAME_2026-07-21.md',None),('PREPRINT_RECON_2026-07-17.md',None),('Q3_PRINT_GRADING_FRAME_2026-09-24.md',None),('Q3_10Q_GRADING_FRAME_2026-09-24.md',None),('THESIS.md',None),('SCENARIOS.md',None),('workbook/PREDICTIONS.tsv',None)]:
    prior=json.loads((WAL/'sources/2026-10-13_preprint-expectations_calculation-receipt.json').read_text())['frozen_and_canonical_SHA256'][p]
    assert hashlib.sha256((WAL/p).read_bytes()).hexdigest()==prior,p
assert abs(results['conditional_11_support']['annual_eps']-11)<.01
assert abs(results['conditional_8_pressure']['annual_eps']-8)<.01
out=WAL/'sources/followup_2026-10-13'
out.joinpath('earnings_bridge_2026-10-14.json').write_text(json.dumps(receipt,indent=2)+'\n')
soup=BeautifulSoup((WAL/'sources/q2_2026/wal-20260630.htm').read_text(),'html.parser')
tables=soup.find_all('table')
extract=['# Q2 earnings-bridge primary extract — read October 14, 2026', '',
    'SEC accession 0001628280-26-051418; filed July31; quarter June30. USD millions except per-share amounts. Zero-based HTML table indexes; source hash in calculation receipt.', '',
    'https://www.sec.gov/Archives/edgar/data/1212545/000162828026051418/wal-20260630.htm']
selected={14:'Income statement',73:'EPS numerator and diluted shares',107:'Q2 average balance and yield'}
for i,t in enumerate(tables):
    text=t.get_text(' ',strip=True)
    if 'Total earnings credit and referral costs' in text and '234.2' in text:
        selected[i]='Earnings-credit/referral income statement classification'
for i,label in selected.items():
    extract.extend(['',f'## {label} — table {i}','','```text',tables[i].get_text(' ',strip=True),'```'])
out.joinpath('Q2_earnings_primary_extract.md').write_text('\n'.join(extract)+'\n')
print(json.dumps({'cases':results,'required':receipt['required_quarterly_pretax'],'checks':'arithmetic and seven preserved-file hashes passed'},indent=2))
