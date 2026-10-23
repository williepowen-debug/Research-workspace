#!/usr/bin/env python3
"""KRE/QQQ transition signature — HENRY, 2026-10-23 (PROME-spawned, Will-directed, read-only research).

Run from the repository root:
    .venv/bin/python PROME/reports/2026-10-23_kre-qqq-transition-signature/build.py [--cache DIR] [--asof YYYY-MM-DD]

Pulls (live, at run time):
  yfinance auto-adjusted daily closes: KRE, QQQ, ^TNX, ^VIX (vendor closes, not exchange-official)
  FRED fredgraph.csv: BAMLH0A0HYM2 (live window only, ICE licence truncates to ~3y), DGS10, VIXCLS (cross-checks)
Reads (repo, read-only): AGENTS/VIOLET/workbook/hy_oas_fred.csv — FROZEN 2026-07-11 archived FRED pull of
  BAMLH0A0HYM2 1996-12-31 → 2026-04-09; spliced with the live FRED window (overlap must agree exactly or the run stops).
Writes: episodes.csv beside this file; markdown tables to stdout (REPORT.md tables are pasted from that stdout).

Definitions (fixed before results were computed; see REPORT.md § Method):
  joint-decline qualifying day t : KRE and QQQ close-to-close return t → t+60 sessions both ≤ −10%
  episode                         : first qualifying day after a gap of > 60 sessions (reproduces PROME's nine)
  anchor A                        : the episode's first qualifying day (PROME's cluster start)
  anchor B ("snap")               : close of the equal-weight KRE+QQQ basket high in [A−20, A+40] sessions
  day 0 = anchor close; "before" = days −10..−1 (+ day 0 levels); "of" = days +1..+10
"""
import argparse, io, os, sys, time, urllib.request
import numpy as np, pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
H = 60          # outcome horizon, sessions
DROP = -0.10    # both legs
ALARM_WIN = 20  # signal must be followed by a qualifying day within this many sessions
EVT = dict(corr_jump=0.20, ratio_dd=-0.04, tnx_move=0.15, vix_jump=3.0, oas_jump=0.30)

def fred(series, cache):
    p = os.path.join(cache, f'fred_{series}.csv') if cache else None
    if p and os.path.exists(p):
        txt = open(p).read()
    else:
        for k in range(4):
            try:
                txt = urllib.request.urlopen(f'https://fred.stlouisfed.org/graph/fredgraph.csv?id={series}', timeout=60).read().decode()
                break
            except Exception as e:
                print(f'# FRED retry {series}: {e}', file=sys.stderr); time.sleep(3)
        if p: open(p, 'w').write(txt)
    s = pd.read_csv(io.StringIO(txt), parse_dates=[0], na_values='.')
    s = s.set_index(s.columns[0]).iloc[:, 0].dropna()
    return s

def yfin(cache):
    p = os.path.join(cache, 'yf.csv') if cache else None
    if p and os.path.exists(p):
        return pd.read_csv(p, index_col=0, parse_dates=True)
    import yfinance as yf
    out = {}
    for t in ['KRE', 'QQQ', '^TNX', '^VIX']:
        for k in range(6):
            try:
                d = yf.download(t, start='2005-06-01', auto_adjust=True, progress=False, threads=False)
                if d is not None and len(d) > 100:
                    c = d['Close']; out[t] = c.iloc[:, 0] if hasattr(c, 'columns') else c; break
            except Exception as e:
                print(f'# yfinance retry {t}: {e}', file=sys.stderr)
            time.sleep(3)
        if t not in out: sys.exit(f'yfinance failed for {t}')
    df = pd.DataFrame(out); df.index.name = 'Date'
    if p: df.to_csv(p)
    return df

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--cache'); ap.add_argument('--asof', default='2026-10-22')
    ap.add_argument('--intraday', default='2026-10-23', help='bar treated as provisional intraday (scored separately)')
    a = ap.parse_args()
    if a.cache: os.makedirs(a.cache, exist_ok=True)
    raw = yfin(a.cache)
    hy_old = pd.read_csv(os.path.join(ROOT, 'AGENTS/VIOLET/workbook/hy_oas_fred.csv'), comment='#', parse_dates=[0], na_values='.')
    hy_old = hy_old.set_index(hy_old.columns[0]).iloc[:, 0].dropna()
    hy_new = fred('BAMLH0A0HYM2', a.cache)
    ov = pd.concat([hy_old, hy_new], axis=1).dropna()
    if len(ov) and (ov.iloc[:, 0] - ov.iloc[:, 1]).abs().max() > 1e-9: sys.exit('HY OAS splice disagrees on overlap')
    hy = pd.concat([hy_old[hy_old.index < hy_new.index[0]], hy_new])
    dgs10 = fred('DGS10', a.cache); vixcls = fred('VIXCLS', a.cache)

    full = raw.dropna(subset=['KRE', 'QQQ']).copy()
    full['HY'] = hy.reindex(full.index).ffill(limit=3)
    df = full[full.index <= a.asof].copy()                     # definitive closes
    r = df[['KRE', 'QQQ']].pct_change()
    df['rK'], df['rQ'] = r.KRE, r.QQQ
    df['c20'] = r.KRE.rolling(20).corr(r.QQQ)
    df['gap'] = (r.KRE - r.QQQ) * 100
    df['ratio'] = df.KRE / df.QQQ
    df['rdd'] = df.ratio / df.ratio.rolling(20).max() - 1
    df['tnx5'] = df['^TNX'].diff(5); df['vix5'] = df['^VIX'].diff(5); df['hy10'] = df.HY.diff(10)
    df['both1'] = (r.KRE <= -0.01) & (r.QQQ <= -0.01)
    n = len(df); ix = df.index
    k, q = df.KRE.values, df.QQQ.values
    ok = np.full(n, np.nan)
    for i in range(n - H):
        ok[i] = float(k[i + H] / k[i] - 1 <= DROP and q[i + H] / q[i] - 1 <= DROP)
    df['qual'] = ok
    qi = np.where(ok == 1)[0]
    starts = [qi[0]] + [b for x, b in zip(qi[:-1], qi[1:]) if b - x > H]
    print(f'# rows {n} {ix[0].date()} → {ix[-1].date()} · qualifying days {len(qi)} · episodes {len(starts)}: ' + ', '.join(str(ix[s].date()) for s in starts))

    # anchors
    eps = []
    for s in starts:
        lo, hi = max(0, s - 20), min(n - 1, s + 40)
        bask = (df.KRE.iloc[lo:hi + 1] / k[s] + df.QQQ.iloc[lo:hi + 1] / q[s]) / 2
        eps.append((str(ix[s].date()), s, ix.get_loc(bask.idxmax())))
    # July→Aug 2024 analog: basket high in [2024-07-01, 2024-08-05] (hand-chosen window — not a mechanical episode)
    seg = df.loc['2024-07-01':'2024-08-05']
    bask = (seg.KRE / seg.KRE.iloc[0] + seg.QQQ / seg.QQQ.iloc[0]) / 2
    j24 = ix.get_loc(bask.idxmax())
    eps.append(('2024-07 analog', j24, j24))

    def onset(col_bool, j, lo=-20, hi=10):
        """first session offset in [lo,hi] where condition turns true (false the session before)."""
        for o in range(lo, hi + 1):
            t = j + o
            if 0 < t < n and bool(col_bool.iloc[t]) and not bool(col_bool.iloc[t - 1]):
                return o
        return None
    conds = {
        'a_corr_jump': (df.c20 - df.c20.shift(5)) >= EVT['corr_jump'],
        'b_ratio_dd': df.rdd <= EVT['ratio_dd'],
        'c_tnx_move': df.tnx5.abs() >= EVT['tnx_move'],
        'd_vix_jump': df.vix5 >= EVT['vix_jump'],
        'e_oas_jump': df.hy10 >= EVT['oas_jump'],
        'f_both1': df.both1,
    }
    rows = []
    for name, s, jb in eps:
        for anc, j in (('A', s), ('B', jb)):
            if name.startswith('2024-07') and anc == 'A': continue
            g = lambda c, o: df[c].iloc[j + o] if 0 <= j + o < n else np.nan
            row = dict(episode=name, anchor=anc, day0=str(ix[j].date()), offset_vs_A=j - s,
                       kre_pre10=k[j] / k[j - 10] - 1, qqq_pre10=q[j] / q[j - 10] - 1,
                       kre_in10=k[j + 10] / k[j] - 1, qqq_in10=q[j + 10] / q[j] - 1,
                       c20_m10=g('c20', -10), c20_m5=g('c20', -5), c20_0=g('c20', 0), c20_p5=g('c20', 5), c20_p10=g('c20', 10),
                       c20_slope_pre=g('c20', 0) - g('c20', -10), c20_min_pre=df.c20.iloc[j - 10:j + 1].min(),
                       gap_mean_pre=df.gap.iloc[j - 9:j + 1].mean(), gap_mean_in=df.gap.iloc[j + 1:j + 11].mean(),
                       opp_pre=float((np.sign(df.rK.iloc[j - 9:j + 1]) != np.sign(df.rQ.iloc[j - 9:j + 1])).mean()),
                       opp_in=float((np.sign(df.rK.iloc[j + 1:j + 11]) != np.sign(df.rQ.iloc[j + 1:j + 11])).mean()),
                       rdd_m10=g('rdd', -10), rdd_0=g('rdd', 0), rdd_p10=g('rdd', 10),
                       tnx_0=g('^TNX', 0), tnx5_0=g('tnx5', 0), tnx5_p5=g('tnx5', 5), tnx_chg_pre10=g('^TNX', 0) - g('^TNX', -10), tnx_chg_in10=g('^TNX', 10) - g('^TNX', 0),
                       vix_0=g('^VIX', 0), vix5_0=g('vix5', 0), vix5_p5=g('vix5', 5), vix_p10=g('^VIX', 10),
                       hy_0=g('HY', 0), hy10_0=g('hy10', 0), hy10_p10=g('hy10', 10))
            fb = [o for o in range(-10, 11) if 0 <= j + o < n and df.both1.iloc[j + o]]
            row['first_both1_offset'] = fb[0] if fb else np.nan
            row['first_both1_date'] = str(ix[j + fb[0]].date()) if fb else ''
            row['c20_on_first_both1'] = df.c20.iloc[j + fb[0]] if fb else np.nan
            fb_in = [o for o in fb if o >= 1]
            row['first_both1_in_offset'] = fb_in[0] if fb_in else np.nan
            row['c20_prior_day_first_both1'] = df.c20.iloc[j + fb[0] - 1] if fb else np.nan
            for c, b in conds.items():
                row['onset_' + c] = onset(b, j)
            dd = df.index[j]
            row['dgs10_minus_tnx_0'] = (dgs10.get(dd, np.nan) - df['^TNX'].iloc[j])
            row['vixcls_minus_vix_0'] = (vixcls.get(dd, np.nan) - df['^VIX'].iloc[j])
            rows.append(row)
    E = pd.DataFrame(rows)
    E.to_csv(os.path.join(HERE, 'episodes.csv'), index=False, float_format='%.4f')

    # ---------- tables ----------
    def pct(x): return '' if pd.isna(x) else f'{x*100:+.1f}%'
    def f2(x): return '' if pd.isna(x) else f'{x:+.2f}'
    def lv(x, d=2): return '' if pd.isna(x) else f'{x:.{d}f}'
    for anc in ('B', 'A'):
        S = E[E.anchor == anc] if anc == 'A' else E[(E.anchor == 'B')]
        print(f'\n### Table {anc}1 — anchor {anc}: returns and correlation path (day 0 = anchor close)')
        print('| Episode | Day 0 | vs A | KRE −10→0 | QQQ −10→0 | KRE 0→+10 | QQQ 0→+10 | c20 −10 | c20 −5 | c20 0 | c20 +5 | c20 +10 | slope −10→0 | opp-sign pre / in |')
        print('|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|')
        for _, x in S.iterrows():
            print(f"| {x.episode} | {x.day0} | {x.offset_vs_A:+d} | {pct(x.kre_pre10)} | {pct(x.qqq_pre10)} | {pct(x.kre_in10)} | {pct(x.qqq_in10)} | {f2(x.c20_m10)} | {f2(x.c20_m5)} | {f2(x.c20_0)} | {f2(x.c20_p5)} | {f2(x.c20_p10)} | {f2(x.c20_slope_pre)} | {x.opp_pre*100:.0f}% / {x.opp_in*100:.0f}% |")
        print(f'\n### Table {anc}2 — anchor {anc}: gap, ratio, rates, VIX, HY OAS, first joint −1% day')
        print('| Episode | gap pre (pp/d) | gap in | ratio DD −10 / 0 / +10 | 10y day0 | 10y Δ5 day0 | 10y Δ −10→0 / 0→+10 | VIX day0 | VIX Δ5 day0 / +5 | HY OAS day0 | HY Δ10 day0 / +10 (bp) | first both ≤−1% (offset, date, c20 that day) |')
        print('|---|---:|---:|---|---:|---:|---|---:|---|---:|---|---|')
        for _, x in S.iterrows():
            fb = '' if pd.isna(x.first_both1_offset) else f"{int(x.first_both1_offset):+d}, {x.first_both1_date}, {f2(x.c20_on_first_both1)}"
            print(f"| {x.episode} | {x.gap_mean_pre:+.2f} | {x.gap_mean_in:+.2f} | {pct(x.rdd_m10)} / {pct(x.rdd_0)} / {pct(x.rdd_p10)} | {lv(x.tnx_0)} | {f2(x.tnx5_0)} | {f2(x.tnx_chg_pre10)} / {f2(x.tnx_chg_in10)} | {lv(x.vix_0,1)} | {f2(x.vix5_0)} / {f2(x.vix5_p5)} | {lv(x.hy_0)} | {x.hy10_0*100:+.0f} / {x.hy10_p10*100:+.0f} | {fb} |")
        print(f'\n### Table {anc}3 — anchor {anc}: event onsets (session offset vs day 0, searched −20..+10; blank = no onset in range)')
        cols = [c for c in E.columns if c.startswith('onset_')]
        print('| Episode | ' + ' | '.join(c.replace('onset_', '') for c in cols) + ' | first |')
        print('|---|' + '---:|' * len(cols) + '---|')
        firsts = {}
        for _, x in S.iterrows():
            vals = {c: x[c] for c in cols if not pd.isna(x[c])}
            m = min(vals.values()) if vals else None
            fs = [c.replace('onset_', '') for c, v in vals.items() if v == m]
            for f in fs: firsts[f] = firsts.get(f, 0) + 1
            print(f'| {x.episode} | ' + ' | '.join('' if pd.isna(x[c]) else f'{int(x[c]):+d}' for c in cols) + f" | {', '.join(fs)} |")
        S9 = S[S.episode != '2024-07 analog']
        print(f'\n# anchor {anc} first-mover counts (ties count for each, nine episodes + analog): {firsts}')
        for c in cols:
            v = S9[c].dropna()
            print(f'# anchor {anc} {c}: onset in range {len(v)}/9 · median {v.median() if len(v) else float("nan"):+.1f} · ≤0 (before/at day 0) {int((v<=0).sum())}/9')
        print(f'# anchor {anc} medians (nine): c20 −10 {S9.c20_m10.median():+.2f} · c20 0 {S9.c20_0.median():+.2f} · c20 +10 {S9.c20_p10.median():+.2f} · slope {S9.c20_slope_pre.median():+.2f} · min pre {S9.c20_min_pre.median():+.2f} · rdd0 {S9.rdd_0.median()*100:+.1f}% · tnx5 day0 {S9.tnx5_0.median():+.2f} · tnx Δ0→+10 {S9.tnx_chg_in10.median():+.2f} · vix0 {S9.vix_0.median():.1f} · vix5 day0 {S9.vix5_0.median():+.2f} · hy10 day0 {S9.hy10_0.median()*100:+.0f}bp · hy10 +10 {S9.hy10_p10.median()*100:+.0f}bp · first both1 offset {S9.first_both1_offset.median():+.0f}')
        print(f'# anchor {anc} cross-check max |DGS10−^TNX| on day 0: {E[E.anchor==anc].dgs10_minus_tnx_0.abs().max():.3f} pts · max |VIXCLS−^VIX| {E[E.anchor==anc].vixcls_minus_vix_0.abs().max():.3f}')

    # ---------- in/out of joint-decline windows (reproduce PROME's first cut) ----------
    inwin = np.zeros(n, bool)
    for i in qi: inwin[i:i + H + 1] = True
    c20v = df.c20.values; opp = (np.sign(df.rK) != np.sign(df.rQ)).values
    valid = ~np.isnan(c20v)
    print(f'\n# reproduce: c20 mean inside qualifying windows {np.nanmean(c20v[inwin & valid]):+.2f} vs outside {np.nanmean(c20v[~inwin & valid]):+.2f} · opposite-sign days {opp[inwin][1:].mean()*100:.0f}% vs {opp[~inwin][1:].mean()*100:.0f}% · lag-1 xcorr KRE(t)~QQQ(t-1) {df.rK.corr(df.rQ.shift(1)):+.3f} · QQQ(t)~KRE(t-1) {df.rQ.corr(df.rK.shift(1)):+.3f}')

    # ---------- signal backtest ----------
    c = df.c20
    sig = {
        'S1 c20 crosses up through 0 after ≤−0.20 in prior 20': (c > 0) & (c.shift(1) <= 0) & (c.rolling(20).min().shift(1) <= -0.20),
        'S2 both ≤−1% day with prior-day c20 ≤ 0': df.both1 & (c.shift(1) <= 0),
        'S3 both ≤−1% day (any)': df.both1,
        'S4 VIX Δ5 ≥ +3 and 10y Δ5 ≤ −0.15': (df.vix5 >= 3) & (df.tnx5 <= -0.15),
        'S5 HY OAS Δ10 ≥ +30bp': df.hy10 >= 0.30,
        'S6 c20 Δ5 ≥ +0.20 and both legs down over 5 sessions': ((c - c.shift(5)) >= 0.20) & (df.KRE.pct_change(5) < 0) & (df.QQQ.pct_change(5) < 0),
        'S7 ratio DD ≤ −4% and QQQ 5-session ≤ −3%': (df.rdd <= -0.04) & (df.QQQ.pct_change(5) <= -0.03),
        'S8 S6 and VIX Δ5 ≥ +3': ((c - c.shift(5)) >= 0.20) & (df.KRE.pct_change(5) < 0) & (df.QQQ.pct_change(5) < 0) & (df.vix5 >= 3),
        # post-hoc, fitted to the signature found above (in-sample by construction):
        'S9 [post-hoc] VIX ≤ 16, ratio DD ≤ −4%, c20 ≥ +0.40': (df['^VIX'] <= 16) & (df.rdd <= -0.04) & (c >= 0.40),
        'S10 [post-hoc] HY OAS Δ20 ≥ +40bp and VIX ≥ 18': (df.HY.diff(20) >= 0.40) & (df['^VIX'] >= 18),
        'S11 [post-hoc] both below 200-day average and c20 ≥ +0.40': (df.KRE < df.KRE.rolling(200).mean()) & (df.QQQ < df.QQQ.rolling(200).mean()) & (c >= 0.40),
        'S12 [post-hoc] KRE 10-session ≥ +4% while QQQ 10-session ≤ −3% (banks bid, tech sold)': (df.KRE.pct_change(10) >= 0.04) & (df.QQQ.pct_change(10) <= -0.03),
    }
    # base rate of each event onset in a random window of the same width used for the episodes
    print('\n### Table N — null check: share of ALL sessions whose [t−20, t+10] window (anchor-B search range) contains an onset')
    print('| Event | Episodes with onset in range (B) | Episodes with onset ≤ day 0 (B) | Random-window share with onset in [−20,+10] | Random-window share with onset in [−20,0] |')
    print('|---|---|---|---:|---:|')
    for cn, b in conds.items():
        b = b.fillna(False)
        on = (b & ~b.shift(1, fill_value=False)).astype(int)
        w31 = on.rolling(31).max().shift(-10)   # window t−20..t+10
        w21 = on.rolling(21).max()              # window t−20..t
        Bv = E[(E.anchor == 'B') & (E.episode != '2024-07 analog')]['onset_' + cn]
        print(f'| {cn} | {Bv.notna().sum()}/9 | {int((Bv <= 0).sum())}/9 | {w31.mean()*100:.0f}% | {w21.mean()*100:.0f}% |')
    fut = pd.Series(ok, index=ix)
    hitwin = fut[::-1].rolling(ALARM_WIN + 1, min_periods=ALARM_WIN + 1).max()[::-1]   # any qualifying day in [t, t+20]
    resolv = pd.Series(np.arange(n) <= n - 1 - H - ALARM_WIN, index=ix)
    base = hitwin[resolv & c.notna()].mean()
    print(f'\n### Table S — early-warning candidates, full history {ix[20].date()} → outcome-resolvable through {ix[n-1-H-ALARM_WIN].date()} (alarm = first fire after 20 quiet sessions; hit = a qualifying day within the next 20 sessions). Base rate of a hit on a random day: {base*100:.1f}%')
    print('| Signal | Alarms (resolved) | Hits | False positives | Precision | Lift vs base | Episodes warned (alarm in [B−20, B]) | Pending alarms (unresolved) | Fires 2026-09-25→' + a.asof + ' |')
    print('|---|---:|---:|---:|---:|---:|---|---|---|')
    sigrows = {}
    for nm, b in sig.items():
        b = b.fillna(False).values
        alarms = []; last = -999
        for t in range(n):
            if b[t] and t - last > ALARM_WIN: alarms.append(t)
            if b[t]: last = t
        res = [t for t in alarms if resolv.iloc[t]]
        hits = [t for t in res if hitwin.iloc[t] == 1]
        warned = []
        for name, s, jb in eps[:-1]:
            if any(jb - 20 <= t <= jb for t in alarms): warned.append(name[:7])
        pend = [str(ix[t].date()) for t in alarms if not resolv.iloc[t]]
        recent = [str(ix[t].date()) for t in range(n) if b[t] and ix[t] >= pd.Timestamp('2026-09-25')]
        prec = len(hits) / len(res) if res else float('nan')
        sigrows[nm] = (res, hits)
        print(f"| {nm} | {len(res)} | {len(hits)} | {len(res)-len(hits)} | {prec*100:.0f}% | {prec/base:.1f}× | {len(warned)}/9 {','.join(warned)} | {', '.join(pend) or '—'} | {', '.join(recent) or '—'} |")
    # ---------- current regime ----------
    print('\n### Table C — current regime (definitive closes through ' + a.asof + ')')
    t = n - 1
    tail = df.iloc[-25:]
    print('| Date | KRE | QQQ | KRE d | QQQ d | gap pp | c20 | ratio DD | 10y | 10y Δ5 | VIX | VIX Δ5 | HY OAS | HY Δ10 bp | both ≤−1% |')
    print('|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|')
    for d, x in tail.iterrows():
        print(f"| {d.date()} | {x.KRE:.2f} | {x.QQQ:.2f} | {pct(x.rK)} | {pct(x.rQ)} | {x.gap:+.2f} | {f2(x.c20)} | {pct(x.rdd)} | {x['^TNX']:.3f} | {f2(x.tnx5)} | {x['^VIX']:.2f} | {f2(x.vix5)} | {lv(x.HY)} | {'' if pd.isna(x.hy10) else f'{x.hy10*100:+.0f}'} | {'YES' if x.both1 else ''} |")
    since = df.loc['2026-09-25':]
    print(f"# since 2026-09-25 ({len(since)} sessions to {a.asof}): opposite-sign {(np.sign(since.rK)!=np.sign(since.rQ)).mean()*100:.0f}% · c20 range {since.c20.min():+.2f} to {since.c20.max():+.2f} · c20 ≤ 0 sessions {(since.c20<=0).sum()} · KRE {since.KRE.iloc[-1]/df.KRE.loc[:'2026-09-24'].iloc[-1]-1:+.1%} QQQ {since.QQQ.iloc[-1]/df.QQQ.loc[:'2026-09-24'].iloc[-1]-1:+.1%}")
    hist = df.loc['2024-01-01':, 'c20'].dropna()
    print(f"# c20 {a.asof} {df.c20.iloc[-1]:+.4f}: percentile since 2024 {(hist < df.c20.iloc[-1]).mean()*100:.1f} · since 2006 {(df.c20.dropna() < df.c20.iloc[-1]).mean()*100:.1f}")
    # current vs the anchor-B day-0 signature (range of the nine, and the 2024-07 analog)
    B9 = E[(E.anchor == 'B') & (E.episode != '2024-07 analog')]; A24 = E[E.episode == '2024-07 analog'].iloc[0]
    x = df.iloc[-1]
    cur = dict(c20_0=x.c20, c20_slope_pre=x.c20 - df.c20.iloc[-11], rdd_0=x.rdd, qqq_pre10=df.QQQ.iloc[-1] / df.QQQ.iloc[-11] - 1,
               kre_pre10=df.KRE.iloc[-1] / df.KRE.iloc[-11] - 1, tnx5_0=x.tnx5, tnx_chg_pre10=x['^TNX'] - df['^TNX'].iloc[-11],
               vix_0=x['^VIX'], vix5_0=x.vix5, hy_0=x.HY, hy10_0=x.hy10,
               opp_pre=float((np.sign(df.rK.iloc[-10:]) != np.sign(df.rQ.iloc[-10:])).mean()))
    print(f'\n### Table V — {a.asof} close vs the nine anchor-B day-0 readings')
    print('| Measure | Nine: min | median | max | 2024-07 analog | Current | Inside the nine\'s range? |')
    print('|---|---:|---:|---:|---:|---:|---|')
    inside = 0
    for m, v in cur.items():
        lo_, md, hi_ = B9[m].min(), B9[m].median(), B9[m].max()
        ins = lo_ <= v <= hi_; inside += ins
        print(f'| {m} | {lo_:+.3f} | {md:+.3f} | {hi_:+.3f} | {A24[m]:+.3f} | {v:+.3f} | {"yes" if ins else "NO"} |')
    print(f'# inside the nine-episode range on {inside} of {len(cur)} measures')
    # intraday provisional bar
    if pd.Timestamp(a.intraday) in full.index:
        f2_ = full[full.index <= a.intraday]; rr = f2_[['KRE', 'QQQ']].pct_change()
        cc = rr.KRE.rolling(20).corr(rr.QQQ)
        print(f"# PROVISIONAL intraday {a.intraday} (yfinance bar at pull time): KRE {f2_.KRE.iloc[-1]:.2f} ({rr.KRE.iloc[-1]*100:+.2f}%) QQQ {f2_.QQQ.iloc[-1]:.2f} ({rr.QQQ.iloc[-1]*100:+.2f}%) 10y {f2_['^TNX'].iloc[-1]:.3f} VIX {f2_['^VIX'].iloc[-1]:.2f} → c20 would be {cc.iloc[-1]:+.3f}")

if __name__ == '__main__':
    main()
