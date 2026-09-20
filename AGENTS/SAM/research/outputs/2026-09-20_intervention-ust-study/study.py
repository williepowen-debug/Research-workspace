#!/usr/bin/env python3
"""UST behaviour around the five 2026 MOF yen-buying operations.

REPRODUCIBLE ARTIFACT — written 2026-09-20 after CATO correctly noted the
original table was run inline and saved nowhere, so no reader could reproduce it.

Op dates: MOF per-operation disclosure (feio/quarter/2026_2Qe.html) for Apr/May;
Jul-30/31 are the two operation DAYS inside the Jul-30->Aug-26 reporting window
(per-op split not published until ~Nov-9).

READ THE LIMITS IN THE REPORT BEFORE CITING ANY NUMBER HERE.
"""
import yfinance as yf, pandas as pd, numpy as np, json, sys

OPS = ['2026-04-30','2026-05-04','2026-05-06','2026-07-30','2026-07-31']
HOR = (1,2,3,5)

def main():
    d = yf.download(['TLT','^TNX','^TYX'], start='2026-01-01', end='2026-09-19',
                    interval='1d', progress=False, auto_adjust=True)['Close'].dropna(how='all')
    idx = list(d.index.date)
    def fwd(col, day, n):
        ds = pd.Timestamp(day).date()
        cand = [k for k,x in enumerate(idx) if x >= ds]
        if not cand or cand[0]+n >= len(d): return None
        i = cand[0]; a,b = d[col].iloc[i], d[col].iloc[i+n]
        return (b-a)/a*100 if col=='TLT' else (b-a)*100

    out = {'ops': OPS, 'n_sessions': len(d), 'tlt_pct': {}, 'y30_bp': {}}
    for label,col,fmt in (('tlt_pct','TLT','%.2f'),('y30_bp','^TYX','%.1f')):
        for h in HOR:
            out[label][f'+{h}d'] = {o:(fwd(col,o,h)) for o in OPS}
    t = d['TLT'].dropna(); y = d['^TYX'].dropna()
    out['baseline'] = {
      'tlt_3d_mean': float(((t.shift(-3)/t-1).dropna()*100).mean()),
      'tlt_3d_sd':   float(((t.shift(-3)/t-1).dropna()*100).std()),
      'y30_3d_mean': float(((y.shift(-3)-y).dropna()*100).mean()),
      'y30_3d_sd':   float(((y.shift(-3)-y).dropna()*100).std()),
      'n': int(len((t.shift(-3)/t-1).dropna())),
    }
    v3 = [x for x in out['y30_bp']['+3d'].values() if x is not None]
    out['y30_3d_op_mean'] = float(np.mean(v3))
    out['y30_3d_se_nominal'] = float(out['baseline']['y30_3d_sd']/np.sqrt(len(v3)))
    out['CAVEAT_se_overstates_precision'] = (
        "Apr-30/May-4/May-6 sit within 5 business days, so their +3d and +5d windows "
        "OVERLAP. The 5 observations are NOT independent; effectively ~2 campaigns. "
        "The nominal SE above assumes independence and is therefore TOO SMALL. "
        "This study cannot support a significance claim in either direction.")
    print(json.dumps(out, indent=2, default=str))
    return out

if __name__ == '__main__':
    main()
