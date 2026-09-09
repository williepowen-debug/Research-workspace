"""Reproduce snapshot arithmetic and local sensitivities; no trade signals."""
import json
from decimal import Decimal as D
from pathlib import Path

ROOT = Path(__file__).resolve().parent
q = json.loads((ROOT / 'quote-extract.json').read_text())['call']
shares, spot, call_mark, account = D(37), D('148.6275'), D('16.80'), D(38510)
share_value = D('5499.21')  # Broker rounds position value to cents.
call_value = call_mark * 100
combined = share_value + call_value
short_now, short_before = D(9967247), D(14054826)
result = {
    'screenshot': {
        'shares': shares, 'spot': spot, 'shares_value': share_value,
        'call_value': call_value, 'combined_value': combined,
        'account_weight_pct': combined / account * 100,
        'combined_open_gain': D('974.94') + D('969.34'),
        'call_intrinsic_value': (spot - 135) * 100,
        'call_time_value': call_value - (spot - 135) * 100,
        'fall_to_135_pct': (1 - 135 / spot) * 100,
        'shares_giveback_at_135': (spot - 135) * shares,
        'shares_loss_if_down_10pct': share_value / 10,
        'expiry_price_matching_16_80_sale_before_costs': D(135) + call_mark,
    },
    'delayed_quote_sensitivity': {
        'bid_value': D(str(q['bid'])) * 100,
        'ask_value': D(str(q['ask'])) * 100,
        'mid_value': (D(str(q['bid'])) + D(str(q['ask']))) * 50,
        'call_share_equivalent': D(str(q['delta'])) * 100,
        'combined_share_equivalent': shares + D(str(q['delta'])) * 100,
        'call_theta_dollars_per_day': D(str(q['theta'])) * 100,
        'call_vega_dollars_per_vol_point': D(str(q['vega'])) * 100,
    },
    'short_interest': {
        'settlement_date': '2026-08-14', 'prior_settlement_date': '2026-07-31',
        'shares': short_now, 'prior_shares': short_before,
        'change_pct': (short_now / short_before - 1) * 100,
        'days_to_cover_using_same_row_volume': short_now / D(5624548),
    },
}
assert combined == D('7179.21')
assert result['screenshot']['combined_open_gain'] == D('1944.28')
assert D(str(q['bid'])) > 0 and D(str(q['ask'])) >= D(str(q['bid']))
assert D(0) <= D(str(q['delta'])) <= D(1)
assert q['option'] == 'USO261016C00135000'
(ROOT / 'summary.json').write_text(json.dumps(result, indent=2, default=str) + '\n')
print(json.dumps(result, indent=2, default=str))
