"""Holdings validation, replication vs ETF, and the Study-6 'separate removal' numbers (non-additive) + sequential/Shapley."""
import warnings; warnings.filterwarnings('ignore')
import itertools
from math import factorial
from replicate import *

etf = adj['KBWB'].pct_change(); kre = adj['KRE'].pct_change()
S = pd.Timestamp('2026-07-31')
win = lambda s, a=BASE, b=END: s.loc[(s.index > a) & (s.index <= b)]
u8, v8, na8 = nport(); u10, v10, na10 = invesco()
fee = 0.0035 / 252   # 497K summary prospectus 12/19/2025: total annual operating expenses 0.35%

print('=== 1. Holdings files vs market prices ===')
print('N-PORT 8/31 units x Yahoo close vs reported valUSD, max abs rel err: %.5f' % ((u8 * close.loc['2026-08-31', TK]) / v8 - 1).abs().max())
print('Invesco 10/30 units x Yahoo close vs marketValueBase, max abs rel err: %.2e' % ((u10 * close.loc['2026-10-30', TK]) / v10 - 1).abs().max())
print('Equity share of net assets: 8/31 %.4f, 10/30 %.4f' % (v8.sum() / na8, v10.sum() / na10))

print('\n=== 2. Unit sets are KBW index-share sets (weights at rebalance reference dates) ===')
for u, nm, d in [(u8, 'N-PORT 8/31 units', '2026-05-29'), (u10, 'Invesco 10/30 units', '2026-08-31')]:
    mv = u * close.loc[d, TK]; w = (100 * mv / mv.sum()).sort_values(ascending=False)
    print(f'{nm} priced at {d}: top5 {w.iloc[:5].round(3).tolist()}  next8 {w.iloc[5:13].round(3).tolist()}')

print('\n=== 3. Replication vs actual ETF (63 sessions, base close 8/3) ===')
K = port_returns(TK, start=pd.Timestamp('2026-05-29'))
e, k = win(etf), win(K)
print('sessions', len(k))
print('KBWB ETF TR %.3f | price-only %.3f | reconstructed gross %.3f | net of 0.35%% %.3f' % (
    100 * cum(e), 100 * cum(win(close['KBWB'].pct_change())), 100 * cum(k), 100 * cum(k - fee)))
print('KRE TR %.3f | price-only %.3f' % (100 * cum(win(kre)), 100 * cum(win(close['KRE'].pct_change()))))
d = e - k
print('daily corr %.5f, TE %.2f bp/day, mean diff %.2f bp/day, max |diff| %.1f bp' % (np.corrcoef(e, k)[0, 1], 1e4 * d.std(), 1e4 * d.mean(), 1e4 * d.abs().max()))
for a, b, nport_tr in [('2026-06-30', '2026-07-31', 3.30177500), ('2026-07-31', '2026-08-31', -0.73111500)]:
    a, b = pd.Timestamp(a), pd.Timestamp(b); n = len(win(K, a, b))
    print(f'Month to {b.date()}: reconstructed gross {100*cum(win(K,a,b)):.3f}, net {100*cum(win(K,a,b)-fee):.3f}, N-PORT NAV TR {nport_tr:.3f}, ETF mkt TR {100*cum(win(etf,a,b)):.3f}')
print('Switch-date test (units change after close of date):')
for sw in ['2026-08-31', '2026-09-11', '2026-09-17', '2026-09-18', '2026-09-21', '2026-09-25', '2026-10-30']:
    r = port_returns(TK, switch=pd.Timestamp(sw), start=S); dd = win(etf) - win(r)
    print(f'  {sw}: TE {1e4*dd.std():.2f} bp/d, cum {100*cum(win(r)):.3f}')

print('\n=== 4. Study-6 separate removals (each group removed alone, remaining units kept) ===')
G = {'BAC': ['BAC'], 'GS+MS': ['GS', 'MS'], 'JPM+C': ['JPM', 'C']}
CM5 = ['JPM', 'BAC', 'GS', 'MS', 'C']
kE = cum(win(etf)); kR = cum(win(port_returns(TK, start=S)))
memo = {}
def X(gs):
    key = tuple(sorted(gs))
    if key not in memo:
        ex = sum([G[g] for g in gs], [])
        memo[key] = cum(win(port_returns([t for t in TK if t not in ex], start=S))) if gs else kR
    return memo[key]
for g in G:
    print(f'  remove {g:6s}: ex-return {100*X([g]):.3f}  effect vs ETF {100*(X([g])-kE):.3f}  vs reconstructed {100*(X([g])-kR):.3f}')
xa = X(list(G))
print(f'  remove ALL5 : ex-return {100*xa:.3f}  effect vs ETF {100*(xa-kE):.3f}  vs reconstructed {100*(xa-kR):.3f}')
print('  sum of separate effects: vs ETF %.3f, vs reconstructed %.3f' % (100 * sum(X([g]) - kE for g in G), 100 * sum(X([g]) - kR for g in G)))
print('  Study 6 reported: 1.04 + 0.78 - 0.37 = 1.45 vs joint 1.81')
print('\nSequential (order-dependent) removal, vs reconstructed:')
for order in itertools.permutations(G):
    prev = kR; steps = []
    for i in range(3):
        cur = X(list(order[:i + 1])); steps.append(round(100 * (cur - prev), 3)); prev = cur
    print('  ', order, steps, round(sum(steps), 3))
sh = {}
for g in G:
    others = [x for x in G if x != g]; v = 0
    for r in range(3):
        for sub in itertools.combinations(others, r):
            v += factorial(r) * factorial(2 - r) / factorial(3) * (X(list(sub) + [g]) - X(list(sub)))
    sh[g] = 100 * v
print('Shapley (vs reconstructed):', {g: round(v, 3) for g, v in sh.items()}, 'sum', round(sum(sh.values()), 3))
# closed-form bridge (single-period approximation using average weights)
W = win(weights_prev(TK, start=S)).mean()
wg = {g: W[v].sum() for g, v in G.items()}; Wt = sum(wg.values())
bridge = sum((X([g]) - kR) * (1 - wg[g]) for g in G) / (1 - Wt)
print('Bridge: sum E_G(1-w_G)/(1-W) = %.3f (avg weights %s, W=%.3f) vs exact joint %.3f' % (100 * bridge, {g: round(100 * v, 2) for g, v in wg.items()}, 100 * Wt, 100 * (xa - kR)))

print('\n=== 5. KRE NAV total return (SSGA NAV history) ===')
nav = pd.read_excel(ROOT + '/data/kre_nav.xlsx', skiprows=3)[['Date', 'NAV']].dropna()
nav['Date'] = pd.to_datetime(nav['Date'], format='%d-%b-%Y', errors='coerce')
nav = nav.dropna().set_index('Date')['NAV'].astype(float).sort_index().loc['2026-08-03':'2026-10-30']
trn = ((nav + div['KRE'].reindex(nav.index).fillna(0)) / nav.shift(1) - 1).dropna()
print('KRE NAV TR 8/3->10/30 %.3f (sessions %d); 10/14->10/30 %.3f' % (100 * ((1 + trn).prod() - 1), len(trn), 100 * ((1 + trn.loc['2026-10-15':]).prod() - 1)))
print('NAV-basis gap estimate: KRE NAV TR minus reconstructed-net KBWB = %.3f' % (100 * ((1 + trn).prod() - 1) - 100 * cum(k - fee)))
