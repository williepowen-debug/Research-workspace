#!/usr/bin/env python3
"""C3 winter reads, computed fresh every run (no stored prices).

Band (Will-ruled 10/10, KB-195): trailing 30-day Mid Atlantic / E N Central HDD vs 1991-2020;
  graded only on windows ending Dec 30 - Feb 28.
Step to 4 (Will-ruled 11/23, WQ-736, KB-311): Henry Hub spot >= 1.5x the median of the prior 60 trading days
  on 3 straight trading days, Nov 1 - Mar 31, AND a CONUS 7-day HDD window >= +10% ending on the third
  price day or up to 7 days earlier. In-sample level; only fires from 2026-11-23 forward count.
Usage: c3_winter_grade.py <cache dir> [--series]   (cache dir holds the 1991-2020 archive; current files re-pulled)
Prints a read; AEOLUS grades. --series prints SERIES.tsv rows for regime/workbook.
"""
import sys, os, csv, io, datetime as dt, statistics as st, urllib.request, urllib.error
CACHE = sys.argv[1]; os.makedirs(CACHE, exist_ok=True)
BASE = 'https://ftp.cpc.ncep.noaa.gov/htdocs/degree_days/weighted/daily_data/%d/Population.Heating.txt'
def get(u): return urllib.request.urlopen(u, timeout=90).read().decode()
now = dt.date.today(); H = {}
def load(txt):
    hdr = None
    for l in txt.splitlines():
        if l.startswith('Region|'): hdr = l.split('|')[1:]
        elif hdr and '|' in l:
            p = l.split('|')
            for k, v in zip(hdr, p[1:]): H[(p[0].strip(), dt.datetime.strptime(k.strip(), '%Y%m%d').date())] = float(v)
for y in list(range(1990, 2021)):
    f = os.path.join(CACHE, f'{y}.txt')
    if not os.path.exists(f): open(f, 'w').write(get(BASE % y))
    load(open(f).read())
for y in (now.year - 1, now.year): load(get(BASE % y))
last = max(d for r, d in H if r == 'CONUS')
NORM = {}
def norm(reg, d):
    k = (reg, d.month, d.day)
    if k not in NORM:
        v = [H[(reg, dt.date(y, d.month, d.day))] for y in range(1991, 2021)]
        NORM[k] = st.mean(v)
    return NORM[k]
def win(reg, end, n):
    ds = [end - dt.timedelta(i) for i in range(n)]; ds = [d for d in ds if (d.month, d.day) != (2, 29)]
    if any((reg, d) not in H for d in ds): return None
    o = sum(H[(reg, d)] for d in ds); b = sum(norm(reg, d) for d in ds)
    return o, b, 100 * (o / b - 1)
print(f'HDD file complete through {last}')
out = []
for reg, name, n, key in (('2', 'Middle Atlantic', 30, 'hdd_30d_midatl'), ('3', 'E N Central', 30, 'hdd_30d_enc'), ('CONUS', 'CONUS', 7, 'hdd_7d_conus')):
    o, b, p = win(reg, last, n); print(f'{name:<16}{n:>3}d obs {o:6.0f} norm {b:7.1f} dev {p:+.1f}%'); out.append((key, p, o, b))
in_w = last >= dt.date(last.year, 12, 30) or last <= dt.date(last.year, 2, 28)
print('band grading window (Dec 30 - Feb 28):', 'OPEN' if in_w else 'CLOSED, report only')
P = []
for r in csv.reader(io.StringIO(get('https://fred.stlouisfed.org/graph/fredgraph.csv?id=DHHNGSP'))):
    try: P.append((dt.date.fromisoformat(r[0]), float(r[1])))
    except (ValueError, IndexError): pass
run = 0; fires = []
for i in range(len(P) - 40, len(P)):
    d, p = P[i]; m = st.median(x for _, x in P[i - 60:i]); run = run + 1 if p >= 1.5 * m else 0
    if run >= 3 and (d.month >= 11 or d.month <= 3) and d >= dt.date(2026, 11, 23):
        w = [win('CONUS', d - dt.timedelta(j), 7) for j in range(8)]; c = max((x[2] for x in w if x), default=None)
        fires.append((d, p, c, 'MET' if c is not None and c >= 10 else ('HDD MISSING' if any(x is None for x in w) else 'price only')))
m = st.median(x for _, x in P[-60:])
print(f'Henry Hub spot {P[-1][0]} {P[-1][1]:.2f}; line for the next day {1.5 * m:.2f} (1.5 x {m:.2f}); run {run}')
print('WQ-736 leg:', fires if fires else 'NOT MET')
if '--series' in sys.argv:
    s = dt.datetime.now().strftime('%Y-%m-%d %H:%M ET')
    for k, p, o, b in out: print('\t'.join([str(last), k, f'{p:.1f}', 'pct_vs_1991-2020', 'CPC-DD-POP-HDD', s, f'obs {o:.0f} norm {b:.1f} HDD; window ends this date; derived 1991-2020 normal']))
