"""Model backtest of KRE/QQQ put strategies (TERRY, 2026-10-23).

Options are PRICED BY MODEL (Black-Scholes, no skew), not historical quotes:
  KRE IV = KRE_SCALE x VIX, QQQ IV = QQQ_SCALE x VXN (scales calibrated loosely on 10/23 quotes).
Each leg holds a put struck OTM_PCT below spot at purchase with DTE_NEW calendar days; rolled
(sell old, buy new) when DTE < ROLL_DTE. Friction = FRIC[leg] of premium on every buy and sell.
Fractional contracts (results are % of budget; real QQQ puts do not fit a $500 card).
"""
import sys, math
import pandas as pd

PX = sys.argv[1]
KRE_SCALE, QQQ_SCALE = float(sys.argv[2]) if len(sys.argv) > 2 else 1.35, float(sys.argv[3]) if len(sys.argv) > 3 else 0.88
OTM_PCT, DTE_NEW, ROLL_DTE, R = 0.03, 60, 21, 0.04
FRIC = {'KRE': 0.05, 'QQQ': 0.01}

d = pd.read_csv(PX, index_col=0, parse_dates=True).dropna(subset=['KRE', 'QQQ'])
d[['^VIX', '^VXN']] = d[['^VIX', '^VXN']].ffill()

def N(x): return 0.5 * (1 + math.erf(x / math.sqrt(2)))
def put(S, K, T, v):
    if T <= 0: return max(K - S, 0.0)
    d1 = (math.log(S / K) + (R + v * v / 2) * T) / (v * math.sqrt(T)); d2 = d1 - v * math.sqrt(T)
    return K * math.exp(-R * T) * N(-d2) - S * N(-d1)
def iv(row, leg): return KRE_SCALE * row['^VIX'] / 100 if leg == 'KRE' else QQQ_SCALE * row['^VXN'] / 100

class Leg:
    def __init__(s, name): s.name, s.n, s.K, s.exp = name, 0.0, None, None
    def price(s, day, row):
        if s.n == 0: return 0.0
        return put(row[s.name], s.K, (s.exp - day).days / 365, iv(row, s.name))
    def value(s, day, row): return s.n * s.price(day, row)
    def buy(s, day, row, cash):
        """spend `cash` on new puts (fresh strike/expiry if flat, else add to current line); returns friction paid"""
        if cash <= 0: return 0.0
        if s.n == 0:
            s.K, s.exp = row[s.name] * (1 - OTM_PCT), day + pd.Timedelta(days=DTE_NEW)
        p = s.price(day, row) if s.n else put(row[s.name], s.K, DTE_NEW / 365, iv(row, s.name))
        cost = p * (1 + FRIC[s.name]); s.n += cash / cost
        return cash - cash / (1 + FRIC[s.name])
    def sell(s, day, row, frac):
        q = s.n * frac; p = s.price(day, row); s.n -= q
        if s.n < 1e-9: s.n = 0.0
        gross = q * p; return gross * (1 - FRIC[s.name]), gross * FRIC[s.name]
    def maybe_roll(s, day, row):
        if s.n and (s.exp - day).days < ROLL_DTE:
            cash, f1 = s.sell(day, row, 1.0); f2 = s.buy(day, row, cash); return f1 + f2, 1
        return 0.0, 0

def run(start, mode, budget=1000.0):
    w = d.loc[start:]; days = list(w.index)
    L = {'KRE': Leg('KRE'), 'QQQ': Leg('QQQ')}
    cash, fric, trades = 0.0, 0.0, 0
    row0 = w.iloc[0]
    for k in L: fric += L[k].buy(days[0], row0, budget / 2); trades += 1
    ref_ratio = row0.KRE / row0.QQQ
    basis = {k: budget / 2 for k in L}
    parked_from, extreme = None, None
    prev = row0
    for day in days[1:]:
        row = w.loc[day]
        for k in L:
            f, t = L[k].maybe_roll(day, row); fric += f; trades += 2 * t
        ratio = row.KRE / row.QQQ
        green = {k: row[k] > prev[k] for k in L}
        if mode == 'rebalance':  # "sell buy sell buy": back to 50/50 whenever the ratio moves >=3% since last swap
            if abs(ratio / ref_ratio - 1) >= 0.03:
                v = {k: L[k].value(day, row) for k in L}; tgt = (v['KRE'] + v['QQQ']) / 2
                win = max(v, key=v.get); lose = 'KRE' if win == 'QQQ' else 'QQQ'
                if v[win] > tgt and v[win] > 0:
                    proceeds, f = L[win].sell(day, row, (v[win] - tgt) / v[win]); fric += f
                    fric += L[lose].buy(day, row, proceeds); trades += 2
                ref_ratio = ratio
        elif mode == 'harvest':  # harvest half at +50% on own red day; park; redeploy to other leg on the turn + its green day
            for k in L:
                v = L[k].value(day, row)
                if parked_from is None and L[k].n and v >= 1.5 * basis[k] and not green[k]:
                    proceeds, f = L[k].sell(day, row, 0.5); fric += f; cash += proceeds; trades += 1
                    basis[k] *= 0.5; parked_from, extreme = k, ratio
            if parked_from:
                other = 'KRE' if parked_from == 'QQQ' else 'QQQ'
                # ratio rising = banks winning; harvested leg QQQ => wait for ratio to fall 3% from its max
                if parked_from == 'QQQ':
                    extreme = max(extreme, ratio); turned = ratio <= extreme * 0.97
                else:
                    extreme = min(extreme, ratio); turned = ratio >= extreme * 1.03
                if turned and green[other] and cash > 0:
                    fric += L[other].buy(day, row, cash); basis[other] += cash; cash = 0.0; trades += 1; parked_from = None
        prev = row
    last = days[-1]; rowL = w.loc[last]
    vals = {k: L[k].value(last, rowL) for k in L}
    return {'start': days[0].date(), 'end': last.date(), 'bars': len(days), 'mode': mode,
            'KRE_leg': round(vals['KRE']), 'QQQ_leg': round(vals['QQQ']), 'cash': round(cash),
            'total': round(vals['KRE'] + vals['QQQ'] + cash), 'pnl_pct': round((vals['KRE'] + vals['QQQ'] + cash) / budget * 100 - 100, 1),
            'trades': trades, 'friction': round(fric)}

def single(start, leg, budget=1000.0):
    w = d.loc[start:]; days = list(w.index); L = Leg(leg); fric = L.buy(days[0], w.iloc[0], budget)
    for day in days[1:]: fric += L.maybe_roll(day, w.loc[day])[0]
    v = L.value(days[-1], w.loc[days[-1]])
    return round(v / budget * 100 - 100, 1)

if __name__ == '__main__':
    print(f'IV scales: KRE {KRE_SCALE} x VIX, QQQ {QQQ_SCALE} x VXN; bars in file {len(d)}')
    rows = []
    for s in ['2026-07-01', '2026-08-24', '2026-09-23', '2026-10-06', '2026-10-15']:
        for m in ['hold', 'rebalance', 'harvest']:
            rows.append(run(s, m))
        rows[-1]['all_KRE_pct'] = single(s, 'KRE'); rows[-1]['all_QQQ_pct'] = single(s, 'QQQ')
        u = d.loc[s:]; rows[-1]['KRE_px'] = round((u.KRE.iloc[-1] / u.KRE.iloc[0] - 1) * 100, 1); rows[-1]['QQQ_px'] = round((u.QQQ.iloc[-1] / u.QQQ.iloc[0] - 1) * 100, 1)
    print(pd.DataFrame(rows).fillna('').to_string(index=False))
