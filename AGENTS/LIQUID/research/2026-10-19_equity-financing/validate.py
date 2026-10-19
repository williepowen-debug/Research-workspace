"""Read-only checks of this bounded research artifact, not a monitor or a causal test."""
from pathlib import Path
from datetime import date
from decimal import Decimal
import csv
import hashlib
import json
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
checks = []


def check(label, ok):
    checks.append((label, bool(ok)))
    print(('PASS ' if ok else 'FAIL ') + label)


calc = json.loads((HERE / 'calculations.json').read_text())
n = calc['NCLH']
D = lambda x: Decimal(str(x))
check('NCLH proceeds minus principal uses = -1.8 before other costs',
      D(n['net_proceeds_before_expenses']) - sum(map(D, [n['old_bond_face'], n['revolver_repayment'], n['eca_prepayment']])) == D(n['cash_before_premiums_fees_accruals']) == Decimal('-1.8'))
check('NCLH marginal nominal room = 691.3, not cash',
      D(n['commitment_after']) - D(n['commitment_before']) + D(n['revolver_repayment']) == D(n['nominal_room_increment_before_other_changes']) == Decimal('691.3'))
check('NCLH new annual coupon = 83.125',
      D(n['new_face']) * D(n['new_coupon_pct']) / 100 == D(n['new_annual_coupon']) == Decimal('83.125'))
check('NCLH same-principal hypothetical coupon increase = 13.78125',
      D(n['old_bond_face']) * (D(n['new_coupon_pct']) - D(n['old_coupon_pct'])) / 100 == D(n['same_principal_hypothetical_annual_coupon_increase']) == Decimal('13.78125'))
v = calc['VZ']
check('VZ displayed expense and total-interest changes round to issuer figures',
      round((D(v['h1_interest_expense_2026']) / D(v['h1_interest_expense_2025']) - 1) * 100, 1) == Decimal('20.0')
      and round((D(v['h1_total_debt_interest_2026']) / D(v['h1_total_debt_interest_2025']) - 1) * 100, 1) == Decimal('16.0'))
check('T transaction cash contribution is 8500, not a September cash balance',
      calc['T']['approximate_acquisition_price'] - calc['T']['two_year_draw'] - calc['T']['day364_draw'] == 8500
      and calc['T']['synthetic_september_cash'] == 'UNKNOWN')

rows = list(csv.DictReader((HERE / 'maturities.tsv').open(), delimiter='\t'))
check('30 dated selected instruments, not complete obligations', len(rows) == calc['maturity_rows'] == 30)
for row in rows:
    maturity = date.fromisoformat(row['contractual_maturity'])
    window = ('PRE_FORMATION' if maturity <= date(2026, 9, 18) else
              'WITHIN_12M' if maturity <= date(2027, 9, 18) else
              'MONTHS_13_24' if maturity <= date(2028, 9, 18) else 'AFTER_24M')
    check(row['issuer'] + '/' + row['instrument'] + '/' + str(maturity) + ': window/unit/vintage',
          window == row['window_from_2026_09_18']
          and row['unit'] == 'millions_native_face'
          and row['first_publication_at'] == 'UNKNOWN'
          and row['balance_date'] == '2026-06-30')
check('VZ September21,2028 excluded from 24-month window',
      next(r for r in rows if r['issuer'] == 'VZ' and r['contractual_maturity'] == '2028-09-21')['window_from_2026_09_18'] == 'AFTER_24M')
receipt = json.loads((HERE / 'vz-pdf-receipt.json').read_text())
check('VZ frozen primary PDF hash matches successful capture',
      receipt['valid_pdf'] and hashlib.sha256((HERE / 'vz-debt-20260630.pdf').read_bytes()).hexdigest() == receipt['sha256'])
baseline = json.loads((HERE / 'state-baseline.json').read_text())
status = (ROOT / 'AGENTS/LIQUID/STATUS.md').read_text()
gates = '\n'.join(s for s in status.splitlines() if s.startswith('| **GATE'))
check('Five gate rows byte-stable', len(gates.splitlines()) == baseline['gate_count'] == 5
      and hashlib.sha256(gates.encode()).hexdigest() == baseline['gate_rows_sha256'])
check('All captured workbook files unchanged', all(
    hashlib.sha256((ROOT / filename).read_bytes()).hexdigest() == expected
    for filename, expected in baseline['workbook_files'].items()))
check('X1 restriction and STATUS line cap retained', "X1 CLOSED / DON'T-SIZE" in status and len(status.splitlines()) < 250)
for num in range(15, 19):
    sig = f'SIG-W-20261019-{num:03d}'
    result = subprocess.run(['rg', '-F', sig, str(ROOT / 'AGENTS/LIQUID/board_log.tsv')], capture_output=True, text=True)
    check(sig + ': one acted row and processed handoff', result.returncode == 0
          and len(result.stdout.splitlines()) == 1 and '\tacted\tINBOX_WALTER\t' in result.stdout
          and (ROOT / f'AGENTS/LIQUID/inbox/WALTER/processed/{sig}.md').exists()
          and not (ROOT / f'AGENTS/LIQUID/inbox/WALTER/{sig}.md').exists())
print(f'{sum(ok for _, ok in checks)}/{len(checks)} research checks passed. Source completeness and causal attribution are not certified.')
raise SystemExit(0 if all(ok for _, ok in checks) else 1)
