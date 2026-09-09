"""Dated offline evidence extractor; not a live monitor or forecast grader.

Usage: .venv/bin/python <this file> workbook.xlsx --vintage 'August 2026'
Requires installed openpyxl. Rejects missing/mismatched metadata and cells.
"""
import argparse
import hashlib
import json
from decimal import Decimal
from pathlib import Path

import openpyxl


def extract(path, vintage, year):
    workbook = openpyxl.load_workbook(path, data_only=True, read_only=True)
    try:
        rows = list(workbook['3dtab'].iter_rows(values_only=True))
        titles = [str(v) for row in rows[:6] for v in row
                  if isinstance(v, str) and 'Short-Term Energy Outlook' in v]
        if len(titles) != 1 or titles[0].rsplit(' - ', 1)[-1].strip() != vintage:
            raise ValueError(f'Expected vintage {vintage!r}; found {titles!r}')
        month_rows = [i for i, row in enumerate(rows)
                      if 'Jan' in row and 'Dec' in row and 'Apr' in row]
        if len(month_rows) != 1 or month_rows[0] == 0:
            raise ValueError('Ambiguous or missing month/year header')
        mi = month_rows[0]
        columns, current_year = {}, None
        for j, month in enumerate(rows[mi]):
            y = rows[mi - 1][j]
            if isinstance(y, (int, float)) and 1900 <= y <= 2200:
                current_year = int(y)
            if current_year == year and month in ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'):
                if month in columns:
                    raise ValueError(f'Duplicate {year} {month}')
                columns[month] = j
        if len(columns) != 6:
            raise ValueError(f'Incomplete {year} first-half columns')
        series = {}
        for key in ('cops_opec', 'cops_opec_r05'):
            matches = [row for row in rows if row[0] == key]
            if len(matches) != 1:
                raise ValueError(f'Missing/duplicate series {key}')
            row = matches[0]
            values = {}
            for month, j in columns.items():
                value = row[j]
                if isinstance(value, bool) or not isinstance(value, (int, float)):
                    raise ValueError(f'Missing/nonnumeric {key} {month}')
                number = Decimal(str(value))
                if not number.is_finite():
                    raise ValueError(f'Nonfinite {key} {month}')
                values[month] = number
            series[key] = {
                'monthly_mbd': {k: str(v) for k, v in values.items()},
                'q2_simple_monthly_mean_mbd': str(sum(values[m] for m in ('Apr', 'May', 'Jun')) / 3),
            }
        return {'vintage': vintage, 'year': year, 'title': titles[0],
                'workbook_sha256': hashlib.sha256(Path(path).read_bytes()).hexdigest(),
                'sheet': '3dtab', 'series': series,
                'verdict': 'NOT_GRADED',
                'basis': 'simple mean of three monthly observations; not a day-weighted API quarter'}
    finally:
        workbook.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('workbook', type=Path)
    parser.add_argument('--vintage', required=True)
    parser.add_argument('--year', type=int, default=2027)
    args = parser.parse_args()
    try:
        print(json.dumps(extract(args.workbook, args.vintage, args.year), indent=2))
    except (ValueError, KeyError, OSError) as exc:
        parser.exit(2, f'EXTRACTION FAILED: {exc}\n')
