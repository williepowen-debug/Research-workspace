#!/usr/bin/env python3
"""Build EGBN loan-level tables transcribed from Eagle's earnings decks (REGINALD, 2026-10-22).

Values are transcribed by hand from the issuer's slides (Q2 slide 25 text copy; Q3 slides 20/21 images).
Each list is checked against the issuer's printed subtotal. Tolerance 2 ($K) because Eagle's own printed
subtotals do not foot exactly: Q2 SM rows sum 260,628 vs printed 260,627; Q3 SM 160,501 vs 160,500; Q3 SUB rows
277,674 vs printed 277,676 (every row re-read at 2x zoom 2026-10-22); and printed Q3 SM+SUB 438,176 vs printed
grand total 438,175. Rows are transcribed as printed; the subtotal gaps are the issuer's rounding.
Run from this folder: python3 build_loan_tables.py   (rc 0 = all subtotal checks pass)
"""
import csv

TOL_K = 2
H = ['quarter_end', 'list', 'row', 'loan_track_id', 'desk_row_id', 'collateral', 'loan_type', 'location',
     'balance_k', 'maturity', 'ltv', 'appraised_value_k', 'appraisal_date', 'dscr', 'dscr_date', 'nonaccrual',
     'valuation_since_column', 'qoq_marker_or_note', 'source']
S2 = 'Eagle Q2 2026 deck slide 25 (8-K acc 0001050441-26-000088); text copy sources/2026-10-20_EGBN_cash-outcome/Q2-deck.txt'
S3 = 'Eagle Q3 2026 deck slide 20 (8-K acc 0001050441-26-000110); image sources/2026-10-22_Q3_8K/deck_020.jpg'

# (list, row, track_id, desk_row_id, collateral, loan_type, location, balance_k, maturity, ltv,
#  appraised_k, appraisal_date, dscr, dscr_date, nonaccrual, valuation_since, marker/note)
Q2 = [
    ('SM', 1, 'L01', 'WOB-REG-013', 'Storage Facility', 'CRE', 'Montgomery', 56196, '2026-08-10', '72%', 77700, '2022-07-27', '0.93', '2026-03-31', 'No', 'No', ''),
    ('SM', 2, 'L02', '', 'Apartment Building', 'CRE', 'Washington DC', 42854, '2026-10-27', '58%', 74000, '2025-09-30', '0.67', '2026-03-31', 'No', 'Yes', ''),
    ('SM', 3, 'L03', '', 'Apartment Building', 'CRE', 'Other US', 36375, '2026-11-30', '70%', 51900, '2021-09-29', '0.89', '2026-03-31', 'No', 'No', ''),
    ('SM', 4, 'L04', '', 'Hotel/Motel', 'CRE', 'Washington DC', 35875, '2029-12-23', '69%', 52100, '2024-10-07', '0.81', '2026-03-31', 'No', 'No', ''),
    ('SM', 5, 'L05', '', 'Mixed Use: Predominantly Commercial', 'CRE', 'Montgomery', 27722, '2026-10-27', '53%', 52600, '2021-10-18', '0.76', '2025-12-31', 'No', 'No', ''),
    ('SM', 6, 'L06', '', 'Education', 'CRE', 'Montgomery', 16500, '2030-01-10', '88%', 18800, '2024-11-04', '1.75', '2026-03-31', 'No', 'No', ''),
    ('SM', 7, 'L07', '', 'Industrial', 'C&I', 'Other US', 12400, '2027-02-26', '', '', '', '0.97', '2025-12-31', 'No', 'No', ''),
    ('SM', 8, 'L08', '', 'Industrial', 'C&I', 'Other US', 11325, '2028-08-29', '32%', 35362, '2024-01-17', '0.97', '2025-12-31', 'No', 'No', ''),
    ('SM', 9, 'L09', '', 'Office', 'CRE', 'Washington DC', 10827, '2026-11-10', '47%', 22949, '2026-03-18', '1.26', '2026-03-31', 'No', 'Yes', ''),
    ('SM', 10, 'L10', '', 'Church', 'C&I', 'Prince William', 10554, '2029-06-10', '54%', 19500, '2022-02-04', '0.64', '2025-12-31', 'No', 'No', ''),
    ('SUB', 1, 'L11', 'WOB-REG-008', 'Apartment Building', 'CRE', "Prince George's", 56000, '2026-08-21', '88%', 63700, '2026-03-09', '0.63', '2026-04-30', 'No', 'Yes', ''),
    ('SUB', 2, 'L12', '', 'Apartment Building', 'CRE', 'Montgomery', 50474, '2031-08-31', '74%', 67800, '2025-11-25', '0.80', '2025-09-30', 'No', 'Yes', ''),
    ('SUB', 3, 'L13', '', 'Apartment Building', 'CRE', 'Washington DC', 35431, '2026-05-16', '47%', 75900, '2025-11-13', '0.97', '2026-03-31', 'No', 'Yes', 'Paid off in full post 6/30/2026 (deck footnote 5)'),
    ('SUB', 4, 'L14', '', 'Apartment Building', 'CRE', 'Washington DC', 26053, '2027-09-29', '84%', 31000, '2021-01-08', '0.82', '2026-03-31', 'No', 'No', ''),
    ('SUB', 5, 'L15', 'WOB-REG-009', 'Office', 'CRE', 'Fairfax', 22072, '2026-09-25', '96%', 23000, '2026-04-02', '0.74', '2026-03-31', 'No', 'Yes', ''),
    ('SUB', 6, 'L16', '', 'Apartment Building', 'CRE', 'Washington DC', 20521, '2026-12-30', '84%', 24500, '2026-06-13', '0.15', '2026-03-31', 'No', 'Yes', ''),
    ('SUB', 7, 'L17', '', 'Office', 'CRE', 'Fairfax', 18502, '2026-02-28', '76%', 24300, '2025-09-05', '1.00', '2026-03-31', 'Yes #1', 'Yes', ''),
    ('SUB', 8, 'L18', '', 'Mixed Use: Predominantly Commercial', 'CRE', 'Washington DC', 15858, '2031-08-11', '154%', 10300, '2026-04-13', '1.19', '2025-12-31', 'No', 'Yes', ''),
    ('SUB', 9, 'L19', '', 'Office', 'CRE', 'Washington DC', 15828, '2030-08-01', '40%', 38500, '2026-02-04', '0.68', '2025-06-30', 'Yes #2', 'Yes', ''),
    ('SUB', 10, 'L20', 'WOB-REG-014', 'Storage Facility', 'CRE', 'Anne Arundel', 14996, '2026-09-30', '77%', 19580, '2022-06-13', '0.26', '2026-03-31', 'No', 'No', ''),
    ('SUB', 11, 'L21', '', 'Apartment Building', 'CRE', 'Washington DC', 10904, '2027-05-04', '57%', 19100, '2025-09-24', '1.00', '2025-12-31', 'Yes #3', 'Yes', ''),
    ('SUB', 12, 'L22', '', 'Condo', 'CRE', 'Alexandria', 10639, '2026-06-13', '20%', 53400, '2024-11-23', '1.00', '2025-12-31', 'No', 'No', ''),
]
Q3 = [
    ('SM', 1, 'L01', 'WOB-REG-013', 'Storage Facility', 'CRE', 'Montgomery', 56062, '2027-02-10', '72%', 77700, '2022-07-27', '0.90', '2026-06-30', 'No', 'No', 'Maturity extended from 2026-08-10'),
    ('SM', 2, 'L02', '', 'Apartment Building', 'CRE', 'Washington DC', 42685, '2026-10-27', '61%', 70000, '2026-08-17', '0.63', '2026-06-30', 'No', 'Yes', 'New appraisal 74,000 -> 70,000'),
    ('SM', 3, 'L05', '', 'Mixed Use: Predominantly Commercial', 'CRE', 'Montgomery', 27722, '2026-10-27', '53%', 52600, '2021-10-18', '0.75', '2026-06-30', 'No', 'No', ''),
    ('SM', 4, 'L23', '', 'Hotel/Motel', 'CRE', 'Other US', 12525, '2027-02-17', '24%', 52400, '2024-01-20', '0.93', '2026-06-30', 'No', 'In Process', 'New'),
    ('SM', 5, 'L24', '', 'All Business Assets', 'C&I', 'Other US', 11058, '2027-12-08', 'N/A', 'N/A', 'N/A', '1.33', '2026-06-30', 'No', 'N/A', 'New'),
    ('SM', 6, 'L10', '', 'Church', 'C&I', 'Prince William', 10449, '2029-06-10', '54%', 19500, '2022-02-04', '0.00', '2026-06-30', 'No', 'In Process', ''),
    ('SUB', 1, 'L11', 'WOB-REG-008', 'Apartment Building', 'CRE', "Prince George's", 56000, '2026-12-21', '88%', 63700, '2026-03-09', '0.74', '2026-08-31', 'Yes #1', 'Yes', 'Maturity re-extended from 2026-08-21; moved to nonaccrual'),
    ('SUB', 2, 'L12', '', 'Apartment Building', 'CRE', 'Montgomery', 50322, '2031-08-31', '74%', 67800, '2025-11-25', '0.86', '2026-06-30', 'No', 'Yes', ''),
    ('SUB', 3, 'L04', '', 'Hotel/Motel', 'CRE', 'Washington DC', 35774, '2029-12-23', '69%', 52100, '2024-10-07', '0.81', '2026-06-30', 'No', 'In Process', 'Downgrade (from SM)'),
    ('SUB', 4, 'L14', '', 'Apartment Building', 'CRE', 'Washington DC', 25921, '2027-09-29', '97%', 26700, '2026-08-13', '0.83', '2026-06-30', 'No', 'Yes', 'New appraisal 31,000 -> 26,700'),
    ('SUB', 5, 'L16', '', 'Apartment Building', 'CRE', 'Washington DC', 20474, '2026-12-30', '152%', 13500, '2026-06-13', '0.24', '2026-06-30', 'No', 'Yes', 'Same appraisal date as Q2 but value 24,500 -> 13,500; still accruing'),
    ('SUB', 6, 'L17', '', 'Office', 'CRE', 'Fairfax', 18502, '2026-02-28', '70%', 26600, '2026-09-21', '(0.56)', '2026-06-30', 'Yes #2', 'Yes', 'Matured 2026-02-28, still outstanding; new appraisal 24,300 -> 26,600'),
    ('SUB', 7, 'L06', '', 'Education', 'CRE', 'Montgomery', 16500, '2030-01-10', '88%', 18800, '2024-11-04', '1.75', '2026-06-30', 'No', 'In Process', 'Downgrade (from SM)'),
    ('SUB', 8, 'L18', '', 'Mixed Use: Predominantly Commercial', 'CRE', 'Washington DC', 15768, '2031-08-11', '153%', 10279, '2026-04-13', '1.12', '2026-06-30', 'No', 'Yes', ''),
    ('SUB', 9, 'L19', '', 'Office', 'CRE', 'Washington DC', 15493, '2030-08-01', '43%', 36400, '2026-05-27', '0.68', '2026-06-30', 'Yes #3', 'Yes', ''),
    ('SUB', 10, 'L07', '', 'Industrial', 'C&I', 'Other US', 11920, '2027-02-26', 'N/A', 'N/A', 'N/A', '(1.00)', '2026-08-31', 'No', 'N/A', 'Downgrade (from SM)'),
    ('SUB', 11, 'L08', '', 'Industrial', 'C&I', 'Other US', 11000, '2028-08-29', '23%', 47200, '2026-06-23', '(1.00)', '2026-08-31', 'No', 'Yes', 'Downgrade (from SM)'),
]
PRINTED = {('2026-06-30', 'SM'): 260627, ('2026-06-30', 'SUB'): 297278,
           ('2026-09-30', 'SM'): 160500, ('2026-09-30', 'SUB'): 277676}

TOP25 = [  # Q3 deck slide 21, 9/30/2026
    ('Apartment Building with Retail/Commercial Space', 'Construction CRE', 'Montgomery', 94000, '1.4%', 'Pass', '2026-12-23', 168000, '2022-11-14', '56%', '6.50', 'V', 'No'),
    ('Apartment Building with Retail/Commercial Space', 'Construction CRE', 'Montgomery', 88497, '1.3%', 'Pass', '2026-11-30', 151000, '2023-05-09', '59%', '6.92', 'V', 'No'),
    ('Apartment Building', 'Income Producing CRE', 'Falls Church City', 88052, '1.3%', 'Pass', '2026-12-23', 185600, '2022-11-14', '47%', '6.46', 'V', 'No'),
    ('CCRC Skilled Nursing', 'Owner Occupied CRE', "Prince George's", 82466, '1.3%', 'Pass', '2027-12-31', 148500, '2025-12-12', '56%', '6.52', 'V', 'No'),
    ('Pledged Non-Marketable Securities', 'C&I', 'Other US', 80500, '1.2%', 'Pass', '2029-05-15', 'N/A', 'N/A', 'N/A', '8.13', 'V', 'No'),
    ('Data Center Income Producing', 'Construction CRE', 'Loudoun', 75000, '1.1%', 'Pass', '2027-04-26', 138696, '2023-03-07', '54%', '6.90', 'V', 'No'),
    ('N/A', 'C&I', 'Washington DC', 75000, '1.1%', 'Pass', '2029-08-10', 'N/A', 'N/A', 'N/A', '5.42', 'V', 'No'),
    ('Land', 'C&I', 'Loudoun', 68000, '1.0%', 'Pass', '2029-09-28', 293000, '2026-02-17', '23%', '7.63', 'V', 'No'),
    ('Mixed Use: Predominantly Residential', 'Income Producing CRE', 'Washington DC', 63300, '1.0%', 'Pass', '2029-09-06', 81900, '2026-06-29', '77%', '5.92', 'V', 'No'),
    ('Mixed Use: Predominantly Commercial', 'C&I', 'Other US', 61191, '0.9%', 'Pass', '2028-08-31', 'N/A', 'N/A', 'N/A', '5.20', 'F', 'No'),
    ('Office', 'Income Producing CRE', 'Washington DC', 61031, '0.9%', 'Pass', '2028-03-31', 108000, '2022-11-08', '57%', '5.50', 'F', 'No'),
    ('CCRC Skilled Nursing', 'Owner Occupied CRE', 'Virginia Beach City', 60243, '0.9%', 'Pass', '2028-10-30', 133149, '2025-07-27', '45%', '6.46', 'V', 'No'),
    ('Office', 'Income Producing CRE', 'Montgomery', 60000, '0.9%', 'Pass', '2028-09-05', 75200, '2024-12-31', '80%', '6.00', 'F', 'No'),
    ('Hotel Near Major University', 'Income Producing CRE', "Prince George's", 59000, '0.9%', 'Pass', '2027-04-01', 77300, '2025-03-03', '76%', '6.46', 'V', 'No'),
    ('Storage Facility', 'Income Producing CRE', 'Montgomery', 56062, '0.9%', 'Criticized', '2027-02-10', 77700, '2022-07-27', '72%', '6.25', 'F', 'No'),
    ('Apartment Building', 'Income Producing CRE', "Prince George's", 56000, '0.9%', 'Classified', '2026-12-21', 63700, '2026-03-09', '88%', '7.40', 'V', 'Yes'),
    ('CCRC Assisted-Living', 'Income Producing CRE', 'Washington DC', 54998, '0.8%', 'Pass', '2026-12-29', 85000, '2026-08-17', '65%', '6.75', 'V', 'No'),
    ('Apartment Building', 'Income Producing CRE', 'Chesterfield', 53732, '0.8%', 'Pass', '2027-03-07', 110000, '2025-06-12', '49%', '6.71', 'V', 'No'),
    ('Education', 'Owner Occupied / C&I', 'Washington DC', 53251, '0.8%', 'Pass', '2052-11-10', 64050, '2022-09-06', '83%', '3.78', 'V', 'No'),
    ('Industrial', 'Construction CRE', 'Prince William', 52961, '0.8%', 'Pass', '2026-11-30', 115200, '2022-09-15', '46%', '5.80', 'V', 'No'),
    ('Hotel/Motel', 'Income Producing CRE', 'Washington DC', 51136, '0.8%', 'Pass', '2028-09-17', 83000, '2018-08-17', '62%', '6.19', 'F', 'No'),
    ('Apartment Building', 'Income Producing CRE', 'Montgomery', 50322, '0.8%', 'Classified', '2031-08-31', 67800, '2025-11-25', '74%', '6.34', 'F', 'No'),
    ('Apartment Building', 'Income Producing CRE', 'Washington DC', 50000, '0.8%', 'Pass', '2027-05-18', 204000, '2023-02-28', '25%', '6.52', 'V', 'No'),
    ('SC-Skilled Nursing Uncovered', 'Owner Occupied CRE', 'Other US', 50000, '0.8%', 'Pass', '2029-03-31', 78031, '2026-01-09', '64%', '6.21', 'V', 'No'),
    ('CCRC Skilled Nursing', 'Owner Occupied CRE', 'Other US', 48932, '0.7%', 'Pass', '2029-07-28', 83333, '2024-10-16', '59%', '6.46', 'V', 'No'),
]
TOP25_PRINTED = 1593675


def main():
    for q, rows in (('2026-06-30', Q2), ('2026-09-30', Q3)):
        for lst in ('SM', 'SUB'):
            got = sum(r[7] for r in rows if r[0] == lst)
            want = PRINTED[(q, lst)]
            assert abs(got - want) <= TOL_K, (q, lst, got, want)
            print(f'{q} {lst}: rows sum {got:,} vs printed {want:,} (diff {got - want:+d}) OK')
    assert abs(sum(r[3] for r in TOP25) - TOP25_PRINTED) <= TOL_K
    print(f'top-25 sum {sum(r[3] for r in TOP25):,} vs printed {TOP25_PRINTED:,} OK')

    with open('EGBN_criticized_over10M_by_quarter.tsv', 'w', newline='') as f:
        f.write('# EGBN criticized/classified loans above $10M as printed in the earnings deck ($K). Built by build_loan_tables.py; '
                'row sums checked against printed subtotals within 2 ($K); issuer subtotals do not foot exactly (see script docstring).\n'
                '# loan_track_id = REGINALD cross-quarter match (collateral + location + balance + maturity); Eagle publishes no loan IDs. '
                'Q2 L03/L09/L13/L15/L20/L21/L22 are absent from the Q3 >$10M lists; only L13 has a disclosed destination (paid off).\n')
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(H)
        for q, rows, src in (('2026-06-30', Q2, S2), ('2026-09-30', Q3, S3)):
            for r in rows:
                w.writerow([q, r[0], r[1], r[2], r[3]] + list(r[4:]) + [src])
    with open('EGBN_top25_loans_2026Q3.tsv', 'w', newline='') as f:
        f.write('# EGBN top-25 loans at 2026-09-30 (24.3% of total loans; weighted-average rate 6.39%), Q3 deck slide 21, '
                'acc 0001050441-26-000110 ($K). Built by build_loan_tables.py; total checked against printed 1,593,675.\n')
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['rank', 'collateral', 'loan_type', 'location', 'balance_k', 'pct_total_loans', 'risk_rating', 'maturity',
                    'appraised_value_k', 'appraisal_date', 'ltv', 'rate_pct', 'fixed_variable', 'nonaccrual'])
        for i, r in enumerate(TOP25, 1):
            w.writerow([i] + list(r))
    print('wrote EGBN_criticized_over10M_by_quarter.tsv and EGBN_top25_loans_2026Q3.tsv')


if __name__ == '__main__':
    main()
