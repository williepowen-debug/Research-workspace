"""Reproduce XLE descriptive statistics and explicitly conditional option scenarios.

No subjective probabilities, forecasts, broker quotes, or trade instructions are
produced. FRED spot endpoints are matched to the US equity session grid without
forward filling. Multi-day rolling windows overlap; the separate block sample
uses disjoint return intervals anchored at the last available oil observation.
"""
import json
import math
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent


def american_call(spot, days, sigma, rate, dividend=0.385, ex_days=12, steps=600):
    """CRR escrowed-dividend approximation; risky stock excludes PV(cash dividend).

    Early exercise compares to actual stock including remaining PV dividend.
    Volatility belongs to escrowed stock. This is a sensitivity model, not an
    exact local-volatility solution for a stock with discrete cash dividends.
    """
    if days <= 0:
        return max(spot - 65.0, 0.0)
    t = days / 365.0
    ex = ex_days / 365.0
    div = dividend if 0 < ex_days < days else 0.0
    base = spot - div * math.exp(-rate * ex)
    dt = t / steps
    u = math.exp(sigma * math.sqrt(dt))
    d = 1 / u
    p = (math.exp(rate * dt) - d) / (u - d)
    assert 0 < p < 1 and base > 0
    disc = math.exp(-rate * dt)
    j = np.arange(steps + 1)
    values = np.maximum(base * u ** (2 * j - steps) - 65, 0)
    for i in range(steps - 1, -1, -1):
        values = disc * (p * values[1:] + (1-p) * values[:-1])
        remaining = div * math.exp(-rate * (ex-i*dt)) if i*dt < ex else 0.0
        stocks = base * u ** (2*np.arange(i+1)-i) + remaining
        values = np.maximum(values, stocks-65)
    return float(values[0])


def summarize(frame):
    if frame.empty:
        return {'n': 0}
    return {'n': len(frame), 'xle_mean_pct': 100*frame.XLE.mean(),
            'xle_median_pct': 100*frame.XLE.median(),
            'xle_up_pct': 100*(frame.XLE > 0).mean(),
            'oil_mean_pct': 100*frame.OIL.mean()}


def main():
    equity = {s: pd.read_csv(ROOT/(s+'.csv'), index_col='date', parse_dates=True)
              for s in ['XLE','XOM','CVX','SPY','USO']}
    index = equity['XLE'].index
    integrity = {}
    for name, frame in equity.items():
        assert frame.index.is_unique and frame.index.is_monotonic_increasing
        assert frame.index.equals(index), name + ' calendar mismatch'
        assert frame[['Close','Adj Close']].notna().all().all()
        assert (frame[['Close','Adj Close']] > 0).all().all()
        assert index[-1].date() == date(2026,9,8)
        integrity[name] = {'first': str(index[0].date()), 'last': str(index[-1].date()),
            'observations': len(frame), 'largest_abs_adjusted_daily_return_pct':
            100*frame['Adj Close'].pct_change(fill_method=None).abs().max()}
    prices = pd.DataFrame({s: frame['Adj Close'] for s,frame in equity.items()})
    price_only = equity['XLE']['Close']
    oil = {s: pd.read_csv(ROOT/(s+'.csv'), index_col='date', parse_dates=True,
                         na_values=['.'])[s] for s in ['DCOILBRENTEU','DCOILWTICO']}
    results = []
    for series, oil_prices in oil.items():
        oil_grid = oil_prices.reindex(index)
        last = oil_grid.last_valid_index()
        end_position = index.get_loc(last)
        for horizon in [1,5,15]:
            returns = prices.pct_change(horizon, fill_method=None)
            returns['OIL'] = oil_grid.pct_change(horizon, fill_method=None)
            returns['XLE_PRICE'] = price_only.pct_change(horizon, fill_method=None)
            # Both endpoints must lie within the designated regime.
            starts = pd.Series(index,index=index).shift(horizon)
            for regime, mask in [
                ('all', pd.Series(True,index=index)),
                ('before_2026_02_27', pd.Series(index < '2026-02-27',index=index)),
                ('since_2026_02_27', starts >= pd.Timestamp('2026-02-27'))]:
                sample = returns.loc[mask].dropna()
                blocks = returns.iloc[list(range(end_position,horizon-1,-horizon))].sort_index()
                blocks = blocks.loc[mask.reindex(blocks.index)].dropna()
                x = np.column_stack([np.ones(len(sample)),sample.OIL,sample.SPY])
                coefficients = np.linalg.lstsq(x,sample.XLE,rcond=None)[0]
                r = {'series':series,'horizon_sessions':horizon,'regime':regime,
                    'first_end':str(sample.index[0].date()),'last_end':str(sample.index[-1].date()),
                    'all':summarize(sample), 'oil_up':summarize(sample[sample.OIL>0]),
                    'oil_up_spy_down':summarize(sample[(sample.OIL>0)&(sample.SPY<0)]),
                    'oil_up_at_least_5pct':summarize(sample[sample.OIL>=0.05]),
                    'nonoverlap_oil_up':summarize(blocks[blocks.OIL>0]),
                    'nonoverlap_all':summarize(blocks),
                    'oil_correlation':sample.XLE.corr(sample.OIL),
                    'regression_oil_beta':float(coefficients[1]),
                    'regression_spy_beta':float(coefficients[2]),
                    'xle_price_quantiles_pct':{str(q):100*sample.XLE_PRICE.quantile(q)
                        for q in [.1,.25,.5,.75,.9]},
                    'xle_total_return_minus_price_mean_pp':100*(sample.XLE-sample.XLE_PRICE).mean()}
                results.append(r)
    recent = []
    for horizon in [1,5,15]:
        recent.append({'sessions':horizon,'start':str(index[-1-horizon].date()),
                       'end':str(index[-1].date()),
                       **{s:100*(f['Adj Close'].iloc[-1]/f['Adj Close'].iloc[-1-horizon]-1)
                          for s,f in equity.items()}})
    realized = {str(n):100*np.log(prices.XLE/prices.XLE.shift(1)).tail(n).std(ddof=1)*np.sqrt(252)
                for n in [20,60,126]}
    rates = pd.read_csv(ROOT/'DGS1MO.csv',na_values=['.']).dropna()
    rate = float(rates.DGS1MO.iloc[-1])/100
    # Unsynchronized public underlying and user screenshot: CONDITIONAL only.
    spot, reference = 65.81, 1.92
    low, high = .01, 1.5
    for _ in range(40):
        mid = (low+high)/2
        if american_call(spot,21,mid,rate) < reference:
            low = mid
        else:
            high = mid
    fitted = (low+high)/2
    scenarios=[]
    for day, days, exdays in [('2026-09-16',14,5),('2026-09-23',7,-2),('2026-09-30',0,-9)]:
        for s in [63,64,65,65.81,66,66.5,67,68,70]:
            for sigma in [.20,fitted,.35] if days else [fitted]:
                value = american_call(s,days,sigma,rate,ex_days=exdays)
                scenarios.append({'date':day,'spot':s,'sigma':sigma,'pair_model_value':200*value,
                                  'difference_vs_384_reference':200*(value-reference)})
    pd.DataFrame(scenarios).to_csv(ROOT/'scenarios.csv',index=False)
    step_prices={str(n):american_call(spot,21,fitted,rate,steps=n) for n in [400,600,1200]}
    assert max(step_prices.values())-min(step_prices.values()) < .02
    assert american_call(64,0,.25,rate) == 0
    assert american_call(68,0,.25,rate)*200 == 600
    assert american_call(spot,21,.35,rate) > american_call(spot,21,.20,rate)
    assert american_call(spot,21,.25,rate,dividend=0) > american_call(spot,21,.25,rate)
    assert american_call(spot+1,21,.25,rate) > american_call(spot,21,.25,rate)
    options={'conditional_spot':spot,'screenshot_reference_premium':reference,
        'observed_executable_bid':None,'observed_valid_xle_iv':None,
        'assumed_dividend':.385,'scheduled_ex_date':'2026-09-21',
        'rate_proxy':rate,'rate_date':rates.date.iloc[-1],
        'conditional_fitted_escrowed_stock_iv':fitted,
        'pair_one_calendar_day_decay_fixed_spot_iv':200*(american_call(spot,20,fitted,rate,ex_days=11)-reference),
        'pair_delta_dollars_per_one_dollar_spot_approx':100*(american_call(spot+.10,21,fitted,rate)-american_call(spot-.10,21,fitted,rate))/.10,
        'pair_vega_dollars_per_one_vol_point_approx':200*(american_call(spot,21,fitted+.005,rate)-american_call(spot,21,fitted-.005,rate)),
        'dividend_sensitivity_per_option_fixed_iv':{str(d):american_call(spot,21,fitted,rate,dividend=d) for d in [.30,.385,.50]},
        'steps_convergence':step_prices,
        'expiry_equal_value_spot':65+reference,
        'expiry_required_gain_pct':100*((65+reference)/spot-1)}
    out={'integrity':integrity,'statistics':results,'recent_equity_returns_pct':recent,
         'realized_annualized_vol_pct':realized,'conditional_option_model':options,
         'verification':'PASS: equity grids, dates, positive prices; expiry payoffs, model monotonicity, convergence'}
    (ROOT/'results.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'recent_equity_returns_pct':recent,'realized_vol_pct':realized,
                      'conditional_option_model':options,'verification':out['verification']},indent=2))


if __name__ == '__main__':
    main()
