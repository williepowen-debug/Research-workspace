"""Offline arithmetic from TERRY's quoted inputs; no market-data certification."""
from math import erf, exp, log, sqrt


def normal(x):
    return (1 + erf(x / sqrt(2))) / 2


def put(spot, strike, days, vol):
    t = days / 365
    d1 = (log(spot / strike) + (0.04 + vol**2 / 2) * t) / (vol * sqrt(t))
    d2 = d1 - vol * sqrt(t)
    return strike * exp(-0.04 * t) * normal(-d2) - spot * normal(-d1)


down_moves = [-0.32, -1.23, -3.98, -4.31, -4.87]
for expiry, days, ask in [('Oct16', 17, 0.81), ('Nov20', 52, 1.21)]:
    for vol in [0.40, 0.45, 0.50, 0.55]:
        values = [put(21.84 * (1 + move / 100), 21, days, vol) for move in down_moves]
        ev = (sum(values) / len(values) / ask - 1) * 100
        print(f'CCL {expiry} 21P post-IV={vol:.0%}: down-five mean return {ev:+.3f}%')

spot, strike, premium = 14.12, 14, 1.35
breakeven = strike - premium
hypothetical_spot = spot * 0.89
intrinsic = max(strike - hypothetical_spot, 0)
print(f'NCLH 14P expiration breakeven: ${breakeven:.4f}; decline {(1-breakeven/spot)*100:.6f}%')
print(f'NCLH hypothetical 11% decline: spot ${hypothetical_spot:.4f}; intrinsic ${intrinsic:.4f}; gross expiry return {(intrinsic/premium-1)*100:+.6f}%')
print('Limits: owner inputs, equal historical weights, flat pre-event spot, BS screening marks; no fills or predictive EV verified.')
