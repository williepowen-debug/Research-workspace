"""PMMS 30Y minus Treasury 10Y par: same-date (publication Thursday) vs survey-matched
(latest close strictly before the PMMS date) against VX-BND-17's 180-230bp band.
Run from AGENTS/BOND with .venv python. PMMS from FRED MORTGAGE30US via rates_context._fred."""
import sys, csv, datetime as dt, statistics, os
sys.path.insert(0, 'monitors')
import rates_context as rc
here = os.path.dirname(os.path.abspath(__file__))
ust = {}
for f in ('treasury_par_2025.csv', 'treasury_par_2026_read-2026-11-16.csv'):
    for r in csv.DictReader(open(os.path.join(here, f))):
        ust[dt.datetime.strptime(r['Date'], '%m/%d/%Y').date()] = float(r['10 Yr'])
days = sorted(ust)
st = lambda x: 'IN' if 180 <= x <= 230 else ('HI' if x > 230 else 'LO')
rows = []
for ds, mv in rc._fred("MORTGAGE30US", 120):
    d = dt.date.fromisoformat(ds)
    if d <= days[0]:
        continue
    a = max(x for x in days if x <= d); b = max(x for x in days if x < d)
    sd = round(mv * 100 - ust[a] * 100); sm = round(mv * 100 - ust[b] * 100)
    rows.append((ds, mv, str(a), sd, str(b), sm, st(sd), st(sm)))
print("PMMS date | PMMS | same-date 10Y date | spread | matched 10Y date | spread | state same | state matched")
for r in rows:
    flag = '  <-- states differ' if r[6] != r[7] else ''
    print(' | '.join(map(str, r)) + flag)
g = [r[5] - r[3] for r in rows]
print(f"weeks {len(rows)}; state disagreements {sum(r[6] != r[7] for r in rows)}; matched minus same-date median {statistics.median(g)} mean {statistics.mean(g):.1f} min {min(g)} max {max(g)}")
for y in ('2025', '2026'):
    print(y, 'out of band: same-date', [(r[0], r[3]) for r in rows if r[0][:4] == y and r[6] != 'IN'],
          '| matched', [(r[0], r[5]) for r in rows if r[0][:4] == y and r[7] != 'IN'])
