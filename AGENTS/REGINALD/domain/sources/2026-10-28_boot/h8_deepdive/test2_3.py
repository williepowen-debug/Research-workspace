"""REGINALD 2026-10-28 — Test 2 (does "borrowing up + deposits down" have a track record?) and
Test 3 (what kind of deposits are small banks gaining?).

PRE-REGISTERED (written 2026-10-28 ~23:00 ET, before any outcome below was computed):
Data: Fed H.8 small domestically chartered commercial banks, SA weekly (FRED H8B3094NSMA borrowings,
DPSSCBW027SBOG deposits), 1985-04 to 2026-10-14.
  B6 = 6-week % change in borrowings; D6 = 6-week % change in deposits.
  DANGER  ("2022 pattern"): B6 >= +5% and D6 <= 0.
  HEALTHY (surge with deposits rising): B6 >= +5% and D6 > 0.
  Robustness: the same two with B6 >= +8%.
Episodes: first qualifying week of a cluster; a new episode starts only after >182 days with no
qualifying week. Release lag: data week end + 9 days (H.8 Friday release of the following week).
Outcomes:
  (a) KRE minus SPY return, 63 and 126 trading days from the first close on/after release
      (episodes from 2006-07; yfinance adjusted closes).
  (b) FDIC bank failures in the 52 weeks after release (episodes from 2000-10; FDIC failed-bank list),
      vs the unconditional distribution over all weeks.
  (c) Small-bank deposits over the 13 weeks after the signal week (descriptive).
Verdict rule: DANGER "has a track record" only if BOTH hold: median 3m excess return is >= 3pp below
the unconditional median, AND mean 52-week failures exceed the unconditional mean. Otherwise "no
evidence of a track record". Small n is reported, never upgraded to proof.
Caveat fixed in advance: H.8 levels carry structure breaks (bank mergers, failures, small/large
reclassification); a single-week jump can masquerade as a deposit change.
"""
import json, pandas as pd, numpy as np, yfinance as yf

df = pd.read_pickle('df.pkl')
d = json.load(open('h8_fred.json'))
B6 = df.b.pct_change(6) * 100
D6 = df.dep.pct_change(6) * 100

kre_j = json.load(open('kre.json'))
kre = pd.Series([v for _, v in kre_j['rows']], index=pd.to_datetime([a for a, _ in kre_j['rows']]))
spy = yf.download('SPY', start='2006-06-01', progress=False, auto_adjust=True)['Close']
spy = spy.iloc[:, 0] if hasattr(spy, 'columns') else spy
spy = spy[spy.index < pd.Timestamp('2026-10-28')]

f = pd.read_csv('fdic_failures.csv', encoding='latin-1')
f.columns = [c.strip().strip('\xa0').strip('�').strip() for c in f.columns]
datecol = [c for c in f.columns if c.lower().startswith('closing')][0]
fail = pd.to_datetime(f[datecol].str.strip(), format='%d-%b-%y')
fail = fail[fail <= pd.Timestamp('2026-10-28')]


def fwd(series, t, n):
    i = series.index.searchsorted(t)
    if i + n >= len(series):
        return np.nan
    return (series.iloc[i + n] / series.iloc[i] - 1) * 100


def failures_next52(t):
    if t + pd.Timedelta(weeks=52) > pd.Timestamp('2026-10-28'):
        return np.nan
    return int(((fail > t) & (fail <= t + pd.Timedelta(weeks=52))).sum())


def episodes(mask):
    hits = mask[mask].index
    eps, last = [], None
    for t in hits:
        if last is None or (t - last).days > 182:
            eps.append(t)
        last = t
    return eps


def table(eps):
    rows = []
    for t in eps:
        rel = t + pd.Timedelta(days=9)
        j = df.index.get_loc(t)
        r = {'week': t.date(), 'B6%': round(B6[t], 1), 'D6%': round(D6[t], 1),
             'bor/assets%': round(df.b[t] / df.ta[t] * 100, 1)}
        for n, lab in [(63, '3m'), (126, '6m')]:
            if rel >= pd.Timestamp('2006-07-01'):
                a, b = fwd(kre, rel, n), fwd(spy, rel, n)
                r['xs' + lab] = round(a - b, 1) if a == a and b == b else np.nan
            else:
                r['xs' + lab] = np.nan
        r['fail52w'] = failures_next52(rel) if rel >= pd.Timestamp('2000-10-15') else np.nan
        r['dep+13w%'] = round((df.dep.iloc[j + 13] / df.dep.iloc[j] - 1) * 100, 1) if j + 13 < len(df) else np.nan
        rows.append(r)
    return pd.DataFrame(rows)


# unconditional baselines
wk = df.index[(df.index >= '2006-07-01')]
xs3 = np.array([fwd(kre, t + pd.Timedelta(days=9), 63) - fwd(spy, t + pd.Timedelta(days=9), 63) for t in wk])
xs3 = xs3[~np.isnan(xs3)]
wf = df.index[(df.index >= '2000-10-15')]
f52 = np.array([failures_next52(t + pd.Timedelta(days=9)) for t in wf], dtype=float)
f52 = f52[~np.isnan(f52)]
f52_ex = np.array([failures_next52(t + pd.Timedelta(days=9)) for t in wf if not (pd.Timestamp('2008-01-01') <= t <= pd.Timestamp('2011-12-31'))], dtype=float)
f52_ex = f52_ex[~np.isnan(f52_ex)]
print(f"UNCONDITIONAL: KRE-SPY 3m median {np.median(xs3):+.1f} (n={len(xs3)} weekly, overlapping); "
      f"52w failures mean {f52.mean():.1f}, median {np.median(f52):.0f} (n={len(f52)}); ex-2008-11 mean {f52_ex.mean():.1f}")

res = {}
for thr in [5, 8]:
    for name, m in [('DANGER', (B6 >= thr) & (D6 <= 0)), ('HEALTHY', (B6 >= thr) & (D6 > 0))]:
        eps = episodes(m.fillna(False))
        t = table(eps)
        res[(name, thr)] = t
        print(f"\n== {name} (B6 >= +{thr}%, D6 {'<= 0' if name=='DANGER' else '> 0'}): {len(eps)} episodes since 1985")
        print(t.to_string(index=False))
        x3 = t['xs3m'].dropna(); fl = t['fail52w'].dropna()
        print(f"   median xs3m {x3.median():+.1f} (n={len(x3)}; share<0 {((x3<0).mean()*100 if len(x3) else float('nan')):.0f}%) | "
              f"mean fail52w {fl.mean():.1f} (n={len(fl)})")

t5 = res[('DANGER', 5)]
x3 = t5['xs3m'].dropna(); fl = t5['fail52w'].dropna()
c1 = len(x3) > 0 and x3.median() <= np.median(xs3) - 3
c2 = len(fl) > 0 and fl.mean() > f52.mean()
print(f"\nVERDICT (pre-registered, B6>=5%): returns leg {'MET' if c1 else 'NOT MET'}; failures leg {'MET' if c2 else 'NOT MET'} -> "
      f"{'TRACK RECORD (small n)' if c1 and c2 else 'NO EVIDENCE OF A TRACK RECORD'}")
print(f"NOW [{df.index[-1].date()}]: B6 {B6.iloc[-1]:+.1f}%, D6 {D6.iloc[-1]:+.1f}% -> "
      f"{'DANGER' if D6.iloc[-1] <= 0 else 'HEALTHY'} pattern")

# ---------------- Test 3: deposit mix ----------------
print("\n================ TEST 3: deposit mix (small banks, SA $B) ================")
ltd = df.ltd
oth = df.dep - df.ltd
for a, b in [('2026-07-15', '2026-10-14'), ('2026-09-02', '2026-10-14')]:
    A, Z = pd.Timestamp(a), pd.Timestamp(b)
    print(f"  {a} -> {b}: deposits {df.dep[Z]-df.dep[A]:+.1f} | large time {ltd[Z]-ltd[A]:+.1f} ({(ltd[Z]/ltd[A]-1)*100:+.1f}%) | "
          f"other (core) {oth[Z]-oth[A]:+.1f} ({(oth[Z]/oth[A]-1)*100:+.1f}%)")
share = (ltd / df.dep * 100).dropna()
print(f"  large-time share of deposits now {share.iloc[-1]:.2f}%; pctile since 2009-07 {(share<share.iloc[-1]).mean()*100:.0f}th; "
      f"2021 low {share.loc['2021'].min():.2f}%, 2023-24 high {share.loc['2023':'2024'].max():.2f}%")
L6 = ltd.pct_change(6) * 100; O6 = oth.pct_change(6) * 100
print(f"  6w growth now: large time {L6.iloc[-1]:+.2f}%, other {O6.iloc[-1]:+.2f}%")
for per in ['2022-06-15', '2022-09-14', '2022-12-14', '2023-03-01']:
    t = pd.Timestamp(per); i = df.index.searchsorted(t); t = df.index[i]
    print(f"  2022-23 comparison {t.date()}: 6w large time {L6[t]:+.2f}%, other {O6[t]:+.2f}%, B6 {B6[t]:+.1f}%")
o6 = O6.loc['2009-07':].dropna()
print(f"  'other' 6w growth pctile now (since 2009-07): {(o6<O6.iloc[-1]).mean()*100:.0f}th")
