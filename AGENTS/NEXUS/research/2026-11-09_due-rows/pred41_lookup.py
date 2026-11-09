"""PRED-41 lookup (DOCKET L575). Pre-written 2026-11-09; run after the NY Fed HHDC Q3-2026 release (11/10 11:00 ET).
Usage: .venv/bin/python -I AGENTS/NEXUS/research/2026-11-09_due-rows/pred41_lookup.py [quarter=2026Q3] [download_dir]
Instrument: HHD_C_Report_<Q>.xlsx, sheet 'Page 14 Data' (New Seriously Delinquent Balances by Loan Type, % of balance),
column 'CC', row 'YY:Qn'. Letter (PREDICTIONS_MONITOR PRED-41): anchor Q2-26 6.97; >= 7.47 HIT; <= 6.47 MISS; else this
print is strictly inside and grades NO-VERDICT only if no later print crosses (first crossing among Q3-26, Q4-26 governs).
Verified 2026-11-09 against the Q2 workbook: 25:Q4 7.1293, 26:Q1 7.10, 26:Q2 6.97 (matches the letter's 7.13 -> 7.10 -> 6.97).
Grade at the PUBLISHED value (2 dp as printed in the workbook cell); compare with the letter's edges exactly."""
import sys, os, urllib.request, openpyxl
q = sys.argv[1] if len(sys.argv) > 1 else '2026Q3'
d = sys.argv[2] if len(sys.argv) > 2 else '.'
url = f'https://www.newyorkfed.org/medialibrary/interactives/householdcredit/data/xls/HHD_C_Report_{q}.xlsx'
path = os.path.join(d, os.path.basename(url))
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=60) as r, open(path, 'wb') as f:
    f.write(r.read())
wb = openpyxl.load_workbook(path, data_only=True)
ws = wb['Page 14 Data']
rows = list(ws.iter_rows(values_only=True))
hdr = next(r for r in rows if r and 'CC' in r)
cc = hdr.index('CC')
label = f"{q[2:4]}:{q[4:]}"
series = [(r[0], r[cc]) for r in rows if r and isinstance(r[0], str) and ':Q' in r[0]]
for lab, v in series[-4:]:
    print(lab, v)
val = dict(series).get(label)
if val is None:
    sys.exit(f'NO CELL for {label}: release not out or layout changed; do not grade')
v = round(float(val), 2)
branch = 'HIT (>= 7.47)' if v >= 7.47 else 'MISS (<= 6.47)' if v <= 6.47 else 'INSIDE BAND (6.47, 7.47): no crossing on this print'
print(f'PRED-41 {label} CC new-seriously-delinquent = {v} -> {branch}; vintage {q}; Q2 in this vintage = {dict(series).get("26:Q2")}')
