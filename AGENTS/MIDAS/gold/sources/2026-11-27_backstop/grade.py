"""D:L1113 backstop grade, 2026-11-27 (PROME prome-80): MIDAS-11 and MIDAS-17 formally on the issuer row, the WQ-451 classes for
11/18-11/25 with issuer tonnes, the WQ-451 section 5 three-month trust line, L2 stress-day count. Frozen parameters copied, not re-fit:
beta -0.1526 %/bp, sd 1.402, stress = S&P <= -1.0% OR VIX >= +2.0 pts, DXY -0.20% (letter gold/research/2026-10-23_WQ451-decomposition-letter.md).
Issuer file: GLD_issuer_archive.xlsx, ONE request 2026-11-27 18:01 UTC, honest client research-bot/1.0 (probe_access.json), HTTP 200.
Real yields: PRIMARY Treasury CSV captured today; the 11/20 value is also checked against the 11/23 first-published capture.
Reads saved files only. The 11/27 market rows are a half-day session read about 13:04 ET and are excluded from every class."""
from pathlib import Path
import json, pandas as pd
P = Path(__file__).resolve().parent
B, SD = -0.1526, 1.402
H = json.loads((P/'fetch_history.json').read_text())
def ser(t, last='2026-11-25'):
    s = pd.Series({pd.Timestamp(r['date']): r['close'] for r in H[t]['history']}).sort_index()
    return s[s.index <= last]
iss = pd.read_excel(P/'GLD_issuer_archive.xlsx', sheet_name='US GLD Historical Archive')
iss.columns = [str(c).strip() for c in iss.columns]
iss['Date'] = pd.to_datetime(iss['Date'], format='%d-%b-%Y', errors='coerce'); iss = iss.dropna(subset=['Date']).sort_values('Date').set_index('Date')
for c in ['Closing Price','Tonnes of Gold','Ounces of Gold per Share']: iss[c] = pd.to_numeric(iss[c], errors='coerce')
iss = iss.dropna(subset=['Closing Price'])
ipx, t, opsh = iss['Closing Price'], iss['Tonnes of Gold'], iss['Ounces of Gold per Share']
real = pd.read_csv(P/'treasury_real.csv', parse_dates=['Date']).set_index('Date').sort_index()['10 YR']
real23 = pd.read_csv(P.parent/'2026-11-23_1120_grade/treasury_real.csv', parse_dates=['Date']).set_index('Date').sort_index()['10 YR']
nom = pd.read_csv(P/'treasury_nominal.csv', parse_dates=['Date']).set_index('Date').sort_index()
spx, vix, dxy, g = ser('^GSPC'), ser('^VIX'), ser('DX-Y.NYB'), ser('GLD')
print('issuer last', ipx.index[-1].date(), ipx.iloc[-1], '| real last', real.index[-1].date(), real.iloc[-1])
print('=== baselines and identity checks')
print('issuer 10/19 close', ipx['2026-10-19'], '(frozen 379.69) | 10/22 close', ipx['2026-10-22'], '(frozen 369.00)')
print('real 11/20: today', real['2026-11-20'], '| first published (11/23 capture)', real23['2026-11-20'], '| 10/22', real['2026-10-22'], '(frozen 2.64)')
ov = pd.concat([ipx, g], axis=1, keys=['issuer','mirror']).loc['2026-11-18':'2026-11-25'].dropna(); ov['diff'] = (ov.mirror-ov.issuer).round(2)
print('issuer vs MIRROR 11/18..11/25 max |diff|', ov['diff'].abs().max(), 'n', len(ov))
r = opsh['2026-10-19':'2026-11-20']; print('oz/share 10/19', r.iloc[0], '-> 11/20', r.iloc[-1], 'max daily change', round(r.diff().abs().max(), 8), '(fee accrual only if tiny and monotone):', bool((r.diff().dropna() <= 0).all()))
print('=== MIDAS-11 (issuer 11/20 close, 2dp, vs 379.69; NONPOSITIVE owns equality)')
c = round(float(ipx['2026-11-20']), 2); print('close', c, '->', 'NONPOSITIVE = HIT' if c <= 379.69 else 'UP = MISS', '| margin', round(c-379.69, 2), '| return', round(100*(c/379.69-1), 2), '%')
print('=== MIDAS-17 (residual = 100*(GLD/369.00-1) - (-0.1526*100*(real-2.64)), 2dp)')
rv = float(real23['2026-11-20']); res = round(100*(c/369.00-1) - (B*100*(rv-2.64)), 2)
print('GLD ret', round(100*(c/369.00-1), 2), '% | real', rv, '| implied', round(B*100*(rv-2.64), 2), '| residual', res, '->', 'HIT' if res > 0 else 'MISS')
print('=== WQ-451 classes 11/18..11/25 (issuer close + tonnes, PRIMARY real, MIRROR S&P/VIX/DXY)')
idx = [d for d in ipx['2026-11-17':'2026-11-25'].index]
rows = []
for a, b in zip(idx[:-1], idx[1:]):
    gl = 100*(ipx[b]/ipx[a]-1); dr = round(100*(real[b]-real[a])); imp = B*dr; e = gl-imp; dt = round(t[b]-t[a], 2)
    sp = 100*(spx[b]/spx[a]-1); dv = vix[b]-vix[a]; dx = 100*(dxy[b]/dxy[a]-1); st = bool(sp <= -1.0 or dv >= 2.0)
    if abs(e) <= SD: k = 'RATE'
    elif e < -SD and st and dt < 0: k = 'LIQUIDATION'
    elif e > SD and st and dx > -0.20: k = 'HAVEN' + ('' if dt > 0 else ' (confirmation leg: tonnes not up)')
    elif e > SD and not st and dx <= -0.20: k = 'DE-DOLLAR proxy'
    else: k = 'UNEXPLAINED-' + ('DOWN' if e < 0 else 'UP')
    rows.append(dict(date=str(b.date()), gld=ipx[b], gld_pct=round(gl,2), tonnes=t[b], d_tonnes=dt, real10=real[b], d_real_bp=dr, implied=round(imp,2), e=round(e,2), e_sd=round(e/SD,2),
        d_nom2y_bp=round(100*(nom['2 Yr'][b]-nom['2 Yr'][a])), spx_pct=round(sp,2), dvix=round(dv,2), dxy=round(dxy[b],2), dxy_pct=round(dx,2), stress=st, cls=k))
df = pd.DataFrame(rows); df.to_csv(P/'wq451_applied.csv', index=False); print(df.to_string(index=False))
print('=== L2 stress days after 10/22')
older = pd.concat([pd.read_csv(f)[['date','stress','gld_pct','cls']] for f in [P.parents[2]/'shared/sources/2026-11-06_L819_grade/wq451_applied.csv',
    P.parent/'2026-11-11_1110_grade/wq451_applied.csv', P.parent/'2026-11-14_1111-1113_grade/wq451_applied.csv', P.parent/'2026-11-18_close_grade/wq451_applied.csv']])
allc = pd.concat([older, df[['date','stress','gld_pct','cls']]]).drop_duplicates('date', keep='last').sort_values('date'); allc = allc[allc.date > '2026-10-22']
s = allc[allc.stress == True]; n, up = len(s), int((s.gld_pct > 0).sum())
print('stress days', n, 'GLD up on', up, list(zip(s.date, s.gld_pct)))
print('LIQUIDATION days after 10/22:', list(allc[allc.cls.str.startswith('LIQUIDATION')].date))
print('=== WQ-451 section 5 three-month lines')
tt = t['2026-10-22':]; below = tt[tt < 1035.70]
print('trust 10/22', t['2026-10-22'], '| min', tt.min(), tt.idxmin().date(), '| first issuer row < 1,035.70 t:', below.index[0].date() if len(below) else None, below.iloc[0] if len(below) else '')
print('trust path 11/17..11/25', {str(k.date()): v for k, v in t['2026-11-17':'2026-11-25'].items()}, '| since 9/30 implied 1,055.70:', round(t.iloc[-1]-1055.70, 2))
rr = real['2026-10-22':]; print('real 10Y >= 3.00 prints since 10/22:', int((rr >= 3.00).sum()), 'max', rr.max())
dd = dxy['2026-10-22':]; print('DXY >= 105 closes since 10/22:', int((dd >= 105).sum()), 'max', round(dd.max(), 2))
print('=== L3 daily proxy (3+ DE-DOLLAR days before 11/30 AND tonnes rise over the same period): tonnes 10/22 -> 11/25', round(t['2026-11-25']-t['2026-10-22'], 2))
print('=== band legs d200 / dd252 at 11/25 close (MIRROR)')
for name in ['SLV','PPLT','PALL','GLD','CPER']:
    cc = ser(name); d = (cc/cc.rolling(200).mean()-1)*100; d2 = (cc/cc.rolling(252, min_periods=200).max()-1)*100
    print(name, cc.iloc[-1], 'd200', round(float(d.iloc[-1]), 2), 'dd252', round(float(d2.iloc[-1]), 2))
print('GSR 11/25 Dec', round(ser('GCZ26.CMX').iloc[-1]/ser('SIZ26.CMX').iloc[-1], 2), '| Feb/Mar', round(ser('GCG27.CMX').iloc[-1]/ser('SIH27.CMX').iloc[-1], 2))
hg = ser('HGH27.CMX'); print('HGH27 11/25', hg.iloc[-1], 'vs 200d', round(100*(hg.iloc[-1]/hg.rolling(200).mean().iloc[-1]-1), 2), '% | QoQ (63 sessions)', round(100*(hg.iloc[-1]/hg.iloc[-64]-1), 2), '%')
print('GCG27 11/25 vs $3,317 shelf', round(100*(ser('GCG27.CMX').iloc[-1]/3317-1), 2), '% | GCZ26', round(100*(ser('GCZ26.CMX').iloc[-1]/3317-1), 2), '%')
print('=== named-contract volumes (lead check), last 3 rows')
for a, b in [('GCZ26.CMX','GCG27.CMX'), ('SIZ26.CMX','SIH27.CMX'), ('HGZ26.CMX','HGH27.CMX'), ('PAZ26.NYM','PAH27.NYM')]:
    va = {r['date']: r['volume'] for r in H[a]['history'][-3:]}; vb = {r['date']: r['volume'] for r in H[b]['history'][-3:]}
    print(a, va, '|', b, vb)
print('=== 11/27 half-day rows (about 13:04 ET, NOT closes) vs 11/25 close')
for n in ['GLD','SLV','PPLT','PALL','CPER','GCG27.CMX','GCZ26.CMX','SIH27.CMX','PLF27.NYM','PAH27.NYM','HGH27.CMX','DX-Y.NYB','^GSPC','^VIX','^TNX','JPY=X']:
    a = ser(n, '2026-11-27'); print(n, a.index[-1].date(), a.iloc[-1], 'vs', a.index[-2].date(), a.iloc[-2], round(100*(a.iloc[-1]/a.iloc[-2]-1), 2), '%')
