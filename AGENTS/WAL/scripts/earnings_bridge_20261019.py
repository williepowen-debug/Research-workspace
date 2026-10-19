#!/usr/bin/env python3
"""Issuer-only bridge; literal guidance arithmetic is conditional, not an EPS forecast."""
from pathlib import Path
from decimal import Decimal as D
import hashlib
import json
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[3]
DESK = ROOT / 'AGENTS/WAL'
OUT = DESK / 'research/2026-10-19_earnings-bridge.json'
Q3 = DESK / 'sources/2026-10-19_Q3/pressrelease-9302026.htm'
FY = DESK / 'sources/2026-10-19_earnings-bridge/pressrelease-12312025.htm'


def table(path, index):
    soup = BeautifulSoup(path.read_bytes(), 'html.parser')
    rows = {}
    for tr in soup.find_all('table')[index].find_all('tr'):
        cells = [x.get_text(' ', strip=True) for x in tr.find_all(['td', 'th'], recursive=False)]
        cells = [x for x in cells if x and x not in ('$', '%')]
        if len(cells) < 2:
            continue
        try:
            vals = [D(x.replace(',', '').replace('(', '-').replace(')', '').replace('—', '0')) for x in cells[1:]]
        except Exception:
            continue
        rows[cells[0]] = vals
    return rows


q = table(Q3, 9)  # Q3, Q2, Q1, Q4'25, Q3'25; CURRENT reclassification
y = table(Q3, 8)  # Q3'26, Q3'25, 9M'26, 9M'25
f = table(FY, 12)  # Q4'25, Q4'24, FY25, FY24
e = table(Q3, 17)
z = D('0')
checks = []


def check(name, a, b):
    assert a == b, (name, a, b)
    checks.append({'check': name, 'value': str(a), 'pass': True})


fee_labels = ['Commercial banking income and related fees',
              'Net gain on mortgage loan origination and sale activities',
              'Net loan servicing revenue (loss)', 'Gain on sales of investment securities',
              'Income from bank owned life insurance', 'Fair value gain (loss) adjustments, net',
              'Income from equity investments', 'Other']
# 'Other' occurs twice. Read the fee Other explicitly before the expense section.
def fee_other():
    soup = BeautifulSoup(Q3.read_bytes(), 'html.parser')
    in_fees = False
    for tr in soup.find_all('table')[9].find_all('tr'):
        c = [x.get_text(' ', strip=True) for x in tr.find_all(['td', 'th'], recursive=False)]
        c = [x for x in c if x and x not in ('$', '%')]
        if c and c[0] == 'Non-interest income:':
            in_fees = True
        if in_fees and c and c[0] == 'Other' and len(c) == 6:
            return [D(v) for v in c[1:]]
    raise AssertionError('Fee Other missing')


q['Fee Other'] = fee_other()
fee_labels[-1] = 'Fee Other'
expense_labels = ['Salaries and employee benefits', 'Deposit costs', 'Data processing',
                  "Legal, professional, and directors' fees", 'Insurance', 'Occupancy',
                  'Loan servicing expenses', 'Business development and marketing',
                  'Loan acquisition and origination expenses', 'Other']
for i, quarter in enumerate(('Q3', 'Q2', 'Q1')):
    check(quarter + ' fee components', sum((q[k][i] for k in fee_labels), z), q['Total non-interest income'][i])
    check(quarter + ' expense components', sum((q[k][i] for k in expense_labels), z), q['Total non-interest expense'][i])
    check(quarter + ' pretax identity', q['Net interest income'][i] + q['Total non-interest income'][i]
          - q['Total non-interest expense'][i] - q['Provision for credit losses'][i], q['Income before income taxes'][i])
    check(quarter + ' tax identity', q['Income before income taxes'][i] - q['Income tax expense'][i], q['Net income'][i])
    check(quarter + ' ECR components', sum((e[k][i] for k in ['Interest income (1)',
          'Commercial banking income and related fees (1)', 'Deposit costs (2)']), z), e['Total earnings credit and referral costs'][i])
for label in ('Net interest income', 'Total non-interest income', 'Total non-interest expense',
              'Deposit costs', 'Provision for credit losses', 'Income before income taxes', 'Income tax expense'):
    check('9M tie ' + label, sum(q[label][:3], z), y[label][2])


def delta(label):
    return q[label][0] - q[label][1]


pretax_bridge = {'NII': delta('Net interest income')}
pretax_bridge.update({k: delta(k) for k in fee_labels})
pretax_bridge.update({'Expense: ' + k: -delta(k) for k in expense_labels})
pretax_bridge['Provision'] = -delta('Provision for credit losses')
check('Detailed pretax bridge', sum(pretax_bridge.values(), z), delta('Income before income taxes'))
check('Net income increase', delta('Income before income taxes') - delta('Income tax expense'), delta('Net income'))
screen = []
for i in (0, 1):
    gains = q['Gain on sales of investment securities'][i] + q['Fair value gain (loss) adjustments, net'][i]
    ppnr = q['Net interest income'][i] + q['Total non-interest income'][i] - q['Total non-interest expense'][i]
    screen.append({'quarter': 'Q3' if i == 0 else 'Q2', 'reported_ppnr': ppnr,
                   'excluded_visible_gain_lines': gains, 'screen_ppnr': ppnr - gains,
                   'screen_pretax': ppnr - gains - q['Provision for credit losses'][i]})
check('Screen plus visible gains reconciles pretax change',
      screen[0]['screen_pretax'] - screen[1]['screen_pretax']
      + screen[0]['excluded_visible_gain_lines'] - screen[1]['excluded_visible_gain_lines'],
      delta('Income before income taxes'))

base = {k: f[k][2] for k in ('Net interest income', 'Total non-interest income', 'Total non-interest expense', 'Deposit costs')}
check('FY25 exact expense base', base['Total non-interest expense'] - base['Deposit costs'], D('1481.2'))


def residual(label, low, high, adjustment=z):
    return [base[label] * (1 + D(low)) - (y[label][2] - adjustment),
            base[label] * (1 + D(high)) - (y[label][2] - adjustment)]


guided = {
    'NII_prior_literal': residual('Net interest income', '.12', '.14'),
    'NII_revised_literal': residual('Net interest income', '.11', '.12'),
    'fees_prior_GAAP_literal': residual('Total non-interest income', '.13', '.17'),
    'fees_revised_GAAP_literal': residual('Total non-interest income', '.18', '.21'),
    'fees_revised_IF_2026_YTD_excludes_Q1_gain_only': residual('Total non-interest income', '.18', '.21', D('50.5')),
    'expense_prior_literal': residual('Total non-interest expense', '.07', '.11'),
    'expense_revised_literal': residual('Total non-interest expense', '.07', '.10'),
    'expense_ex_deposit': [D('1600') - (y['Total non-interest expense'][2] - y['Deposit costs'][2]),
                           D('1650') - (y['Total non-interest expense'][2] - y['Deposit costs'][2])],
    'deposit_expense_prior': [D('650') - y['Deposit costs'][2], D('700') - y['Deposit costs'][2]],
    'deposit_expense_revised': [D('650') - y['Deposit costs'][2], D('675') - y['Deposit costs'][2]],
}
midpoint_changes = {
    'NII': base['Net interest income'] * (D('.115') - D('.13')),
    'fees': base['Total non-interest income'] * (D('.195') - D('.15')),
    'expense_profit_effect': -base['Total non-interest expense'] * (D('.085') - D('.09')),
}
midpoint_changes['pretax_total'] = sum(midpoint_changes.values(), z)
midpoint_changes['component_expense_alternative_pretax'] = midpoint_changes['NII'] + midpoint_changes['fees'] + D('12.5')
q3_ex = q['Total non-interest expense'][0] - q['Deposit costs'][0]
q4_cost_drop = [q3_ex - v for v in reversed(guided['expense_ex_deposit'])]
tax_catchup = D('.19') * y['Income before income taxes'][2] - y['Income tax expense'][2]
# The sensitivity does not claim ECR savings or other line changes are independent.
sensitivity = {'pretax_change': D('10'), 'tax_assumption': D('.19'),
               'diluted_shares_assumption': q['Diluted shares'][0],
               'quarterly_EPS_change_approx': D('10') * D('.81') / q['Diluted shares'][0]}

protected = json.loads((DESK / 'research/2026-10-19_Q3-full-read-validation.json').read_text())['protected_unchanged']
protected.update({str((DESK / p).relative_to(ROOT)): hashlib.sha256((DESK / p).read_bytes()).hexdigest()
                  for p in ('research/2026-10-19_Q3_STAGE1_GRADE.md', 'research/2026-10-19_Q3_FULL_READ.md', 'POSITIONS.md')})
for path, sha in protected.items():
    assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == sha, path
result = {
    'units': 'USD millions except EPS; Decimal calculations, printed source precision',
    'source_tables_zero_based': {'Q3_quarters': 9, 'Q3_YTD': 8, 'ECR': 17, 'FY25': 12, 'guidance': 'EX99.2 slide17 visually checked'},
    'source_sha256': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in [Q3, FY]},
    'quarter_inputs': q, 'YTD_inputs': y, 'FY25_exact_bases': base, 'ECR_inputs': e,
    'pretax_bridge': pretax_bridge, 'visible_line_screen_NOT_normalized_EPS': screen,
    'Q4_guidance_residuals_CONDITIONAL': guided,
    'guide_midpoint_profit_effect_CONDITIONAL': midpoint_changes,
    'Q4_ex_deposit_cost_decline_required_IF_same_basis': q4_cost_drop,
    'Q4_tax_IF_full_year_19pct': {'formula': '0.19 * Q4 pretax + catchup', 'catchup': tax_catchup},
    'sensitivity_NOT_forecast': sensitivity,
    'checks': checks, 'protected_unchanged': protected,
    'unknowns': ['Guide accounting basis and normalization/exclusions not explicitly reconciled',
                 'Q3 MSR cash flow, valuation, hedge and expense attribution',
                 'Compensation cost persistence / Q4 cost step-down composition',
                 'Q4 provision, tax benefits, shares and award allocation are not EPS guidance'],
}
OUT.write_text(json.dumps(result, indent=2, default=str) + '\n')
print(json.dumps({k: result[k] for k in ['FY25_exact_bases', 'pretax_bridge',
      'visible_line_screen_NOT_normalized_EPS', 'Q4_guidance_residuals_CONDITIONAL',
      'guide_midpoint_profit_effect_CONDITIONAL', 'Q4_ex_deposit_cost_decline_required_IF_same_basis',
      'Q4_tax_IF_full_year_19pct', 'sensitivity_NOT_forecast']}, indent=2, default=str))
print(f'{len(checks)} accounting checks passed; {len(protected)} protected files unchanged.')
