"""11/18-11/20 gold on the frozen WQ-451 classifier + MIDAS-11/13/17 + L819 L1/L2 (2026-11-23, PROME prome-77, D:L1113 + D:L819).
Shape copied from ../2026-11-18_close_grade/grade.py; frozen parameters copied, not re-fit: beta -0.1526 %/bp, sd 1.402,
stress = S&P <= -1.0% OR VIX >= +2.0 pts, DXY -0.20%. Letter gold/research/2026-10-23_WQ451-decomposition-letter.md (a35faa6f8).
SOURCE CHANGE, disclosed: the SPDR issuer archive refused this session's plain client (HTTP 403, access.json) and is not asked again.
Issuer rows held: through 11/17 in ../2026-11-18_close_grade/GLD_issuer_archive.xlsx (that capture used a browser-impersonating client,
disallowed under the rule as PROME restated it 11/23). GLD 11/18-11/20 closes here are MIRROR (FORGE fetch.py, yfinance); tonnes after 11/17 UNKNOWN.
Real/nominal yields: PRIMARY Treasury CSVs captured here. Reads only saved files. The newest market row (11/23, intraday) is excluded."""
from pathlib import Path
import json, pandas as pd
P = Path(__file__).resolve().parent
B, SD = -0.1526, 1.402
H = json.loads((P/'fetch_history.json').read_text())
def ser(t):
    s = pd.Series({pd.Timestamp(r['date']): r['close'] for r in H[t]['history']}).sort_index()
    return s[s.index <= '2026-11-20']   # 11/23 row is an intraday quote, excluded
iss = pd.read_excel(P.parent/'2026-11-18_close_grade/GLD_issuer_archive.xlsx', sheet_name='US GLD Historical Archive')
iss.columns = [str(c).strip() for c in iss.columns]
iss['Date'] = pd.to_datetime(iss['Date'], format='%d-%b-%Y', errors='coerce'); iss = iss.dropna(subset=['Date']).sort_values('Date').set_index('Date')
for c in ['Closing Price','Tonnes of Gold']: iss[c] = pd.to_numeric(iss[c], errors='coerce')
ipx, t = iss['Closing Price'], iss['Tonnes of Gold']
real = pd.read_csv(P/'treasury_real.csv', parse_dates=['Date']).set_index('Date').sort_index()['10 YR']
nom = pd.read_csv(P/'treasury_nominal.csv', parse_dates=['Date']).set_index('Date').sort_index()
g, spx, vix, dxy = ser('GLD'), ser('^GSPC'), ser('^VIX'), ser('DX-Y.NYB')
print('issuer last', ipx.index[-1].date(), '| real last', real.index[-1].date(), real.iloc[-1], '| MIRROR GLD last', g.index[-1].date(), g.iloc[-1])
print('=== issuer vs MIRROR GLD close, overlap 10/22..11/17 (2dp)')
ov = pd.concat([ipx, g], axis=1, keys=['issuer','mirror']).loc['2026-10-22':'2026-11-17'].dropna()
ov['diff'] = (ov.mirror - ov.issuer).round(2); print('max |diff|', ov['diff'].abs().max(), 'n', len(ov))
print('=== daily classes 11/18..11/20 (GLD MIRROR close; issuer close used for the 11/17 base)')
px = pd.concat([ipx[:'2026-11-17'], g['2026-11-18':]])
rows = []
for a, b in zip(px.index[:-1], px.index[1:]):
    if b < pd.Timestamp('2026-11-18'): continue
    gl = 100*(px[b]/px[a]-1); dr = round(100*(real[b]-real[a])); imp = B*dr; e = gl-imp
    sp = 100*(spx[b]/spx[a]-1); dv = vix[b]-vix[a]; dx = 100*(dxy[b]/dxy[a]-1); st = bool(sp <= -1.0 or dv >= 2.0)
    if abs(e) <= SD: c = 'RATE'
    elif e < -SD and st: c = 'LIQUIDATION-candidate (tonnes UNKNOWN: issuer archive refused)'
    elif e > SD and st and dx > -0.20: c = 'HAVEN-candidate (tonnes UNKNOWN)'
    elif e > SD and not st and dx <= -0.20: c = 'DE-DOLLAR proxy'
    else: c = 'UNEXPLAINED-' + ('DOWN' if e < 0 else 'UP')
    rows.append(dict(date=str(b.date()), gld=round(px[b],2), gld_pct=round(gl,2), real10=real[b], d_real_bp=dr, implied=round(imp,2), e=round(e,2), e_sd=round(e/SD,2),
        d_nom2y_bp=round(100*(nom['2 Yr'][b]-nom['2 Yr'][a])), d_nom10y_bp=round(100*(nom['10 Yr'][b]-nom['10 Yr'][a])), spx_pct=round(sp,2), dvix=round(dv,2),
        dxy=round(dxy[b],2), dxy_pct=round(dx,2), stress=st, cls=c))
df = pd.DataFrame(rows); df.to_csv(P/'wq451_applied.csv', index=False); print(df.to_string(index=False))
print('=== L2 stress days after 10/22 (prior files + this one)')
prior = pd.read_csv(P.parent/'2026-11-18_close_grade/wq451_applied.csv')[['date','stress','gld_pct','cls']]
older = pd.concat([pd.read_csv(f)[['date','stress','gld_pct','cls']] for f in [P.parents[2]/'shared/sources/2026-11-06_L819_grade/wq451_applied.csv',
    P.parent/'2026-11-11_1110_grade/wq451_applied.csv', P.parent/'2026-11-14_1111-1113_grade/wq451_applied.csv']])
allc = pd.concat([older, prior, df[['date','stress','gld_pct','cls']]]).drop_duplicates('date', keep='last').sort_values('date')
allc = allc[allc.date > '2026-10-22']
s = allc[allc.stress == True]; n, up = len(s), int((s.gld_pct > 0).sum())
print('stress days', n, 'GLD up on', up, list(zip(s.date, s.gld_pct)))
print('falsification needs >= 6 up of 10; max reachable =', up + (10-n), '->', 'UNREACHABLE: claim cannot be falsified' if up + (10-n) < 6 else 'still reachable')
print('=== WQ-451 section 5 lines (1-month horizon ended 11/20)')
print('GLD 11/20', px.iloc[-1], 'vs 10/19 ref 379.69:', round(100*(px.iloc[-1]/379.69-1),2), '%; 1m down line 360.71 crossed')
rr = real['2026-10-22':]; print('real 10Y >= 3.00 prints since 10/22:', int((rr >= 3.00).sum()), 'max', rr.max(), rr.idxmax().date())
dd = dxy['2026-10-22':]; print('DXY >= 105 closes since 10/22:', int((dd >= 105).sum()), 'max', round(dd.max(),2))
print('trust last issuer row', ipx.index[-1].date(), t.iloc[-1], 't; 3m line 1035.70; since 10/22', round(t.iloc[-1]-t['2026-10-22'],2))
print('=== MIDAS-11/13/17')
c1120 = g['2026-11-20']; print('GLD 11/20 MIRROR', c1120, '(issuer row not retrievable)')
print('MIDAS-11: NONPOSITIVE if <= 379.69 ->', 'NONPOSITIVE (HIT side)' if round(c1120,2) <= 379.69 else 'UP (MISS side)', 'margin', round(c1120-379.69,2))
w = ipx['2026-10-26':'2026-11-17']; print('MIDAS-13: max issuer close 10/26..11/17', w.max(), w.idxmax().date(), '>= 378.95 ->', w.max() >= 378.95,
      '| MIRROR 11/09', g['2026-11-09'], '| MIRROR max 11/18..11/20', g['2026-11-18':].max())
res = 100*(c1120/369.00-1) - (B*100*(real['2026-11-20']-2.64))
print('MIDAS-17: GLD', round(100*(c1120/369.00-1),2), '% ; real 2.64 ->', real['2026-11-20'], '; residual', round(res,2), '->', 'HIT' if round(res,2) > 0 else 'MISS')
need = 369.00*(1 + (B*100*(real['2026-11-20']-2.64))/100); print('   GLD close needed for a HIT at that real yield: >', round(need,2))
print('=== band legs d200 / dd252 at 11/20 (MIRROR)')
for name in ['SLV','PPLT','PALL']:
    c = ser(name); d = (c/c.rolling(200).mean()-1)*100; d2 = (c/c.rolling(252, min_periods=200).max()-1)*100
    print(name, c.iloc[-1], {str(k.date()): round(float(v),2) for k, v in d.iloc[-4:].items()}, 'dd252', round(float(d2.iloc[-1]),2))
for n in ['GCZ26.CMX','SIZ26.CMX','PLF27.NYM','PAZ26.NYM','HGZ26.CMX']:
    c = ser(n); print(n, {str(k.date()): v for k, v in c.iloc[-4:].items()})
print('GSR 11/20', round(ser('GCZ26.CMX').iloc[-1]/ser('SIZ26.CMX').iloc[-1],2), '| GCZ26 vs $3,317 shelf', round(100*(ser('GCZ26.CMX').iloc[-1]/3317-1),2), '%')
print('=== cross-asset 11/18..11/20 % (MIRROR)')
for n in ['^GSPC','QQQ','SLV','PPLT','PALL','CPER','DX-Y.NYB']:
    c = ser(n); print(n, {str(k.date()): round(100*(c[k]/c.shift(1)[k]-1),2) for k in c.index[-3:]})
