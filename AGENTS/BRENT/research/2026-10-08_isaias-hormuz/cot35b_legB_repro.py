"""Re-reproduce GATE-BRENT-COT-35B Leg-B base 4.909% (read-only; moves nothing).
Inputs: CFTC fut_disagg_txt_{2024,2025,2026}.zip (https://www.cftc.gov/files/dea/history/), unzipped to y{YEAR}/f_year.txt in cwd.
Leg B = M_Money_Positions_Short_All (field 15) / Open_Interest_All (field 8) x 100, futures-only, market matched by NAME
'WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE' (code 067651). Base = median of the 104 weekly obs ending 2026-08-04 inclusive."""
import pandas as pd
from decimal import Decimal, ROUND_HALF_UP
d = pd.concat([pd.read_csv(f'y{y}/f_year.txt', low_memory=False) for y in (2024, 2025, 2026)])
m = d[d['Market_and_Exchange_Names'].str.strip() == 'WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE'].copy()
m['date'] = pd.to_datetime(m['Report_Date_as_YYYY-MM-DD']); m = m.drop_duplicates('date').sort_values('date')
w = m[m.date <= '2026-08-04'].tail(104)
v = sorted(Decimal(int(s)) * 100 / Decimal(int(o)) for s, o in zip(w['M_Money_Positions_Short_All'], w['Open_Interest_All']))
med = (v[51] + v[52]) / 2
print(len(w), w.date.min().date(), w.date.max().date(), med, med.quantize(Decimal('0.001'), ROUND_HALF_UP))
