"""Screenshot arithmetic with Decimal; no order or current quote assumptions."""
import csv
import json
from datetime import date
from decimal import Decimal as D
from pathlib import Path

ROOT=Path(__file__).resolve().parent
rows=list(csv.DictReader((ROOT/'snapshot.csv').open()))
cash=D('17489.02'); total=D('38510.00')
for r in rows:
    for field in ['quantity','display_price','value','basis','open_gain','daily_gain']:
        r[field]=D(r[field])
    assert r['value']-r['basis']==r['open_gain'],r['position']
    multiplier=100 if r['type'] in ['call','put'] else 1
    assert abs(r['quantity']*r['display_price']*multiplier-r['value'])<=D('.01'),r['position']
assert sum(r['value'] for r in rows)+cash==total
assert sum(r['open_gain'] for r in rows)==D('2053.32')
assert sum(r['daily_gain'] for r in rows)==D('319.11')
groups={'Cash':{'value':cash,'basis':cash,'gain':D(0)}}
for r in rows:
    g=groups.setdefault(r['group'],{'value':D(0),'basis':D(0),'gain':D(0)})
    g['value']+=r['value'];g['basis']+=r['basis'];g['gain']+=r['open_gain']
for g in groups.values():g['weight_pct']=100*g['value']/total
options=[r for r in rows if r['type'] in ['put','call']]
next_expiry=[r for r in options if r['expiry']<='2026-09-30']
managed=[r for r in rows if r['position'] in ['XLE 65 call','TLT 85 put','QQQ 715 put']]
post_cash=cash+sum(r['value'] for r in managed)
out={'basis':'Supplied positions screenshot; capture timestamp/account header not visible. Values are displayed marks, not executable quotes.',
     'cash':cash,'account_total':total,'invested_value':total-cash,
     'groups':groups,'options_value':sum(r['value'] for r in options),
     'options_basis':sum(r['basis'] for r in options),'options_gain':sum(r['open_gain'] for r in options),
     'options_value_pct':100*sum(r['value'] for r in options)/total,
     'options_by_sep30_value':sum(r['value'] for r in next_expiry),
     'options_by_sep30_contracts':sum(r['quantity'] for r in next_expiry),
     'remaining_sep_value_after_three_hypothetical_sales':sum(r['value'] for r in next_expiry if r not in managed),
     'hypothetical_cash_after_XLE_TLT85_QQQ_sold_at_image_marks':post_cash,
     'hypothetical_cash_weight_pct':100*post_cash/total,
     'energy_gold_apple_pct_invested':100*sum(groups[g]['value'] for g in ['Energy','Gold','Apple'])/(total-cash),
     'day_energy_gain':sum(r['daily_gain'] for r in rows if r['group']=='Energy'),
     'share_only_stress_10pct_down':{s:next(r['value'] for r in rows if r['symbol']==s and r['type']=='shares')*D('-.10') for s in ['AAPL','GLD','USO']},
     'uso_call_intrinsic_at_image_underlying':D('148.6275')-135,
     'uso_call_extrinsic_at_image_underlying':D('16.80')-(D('148.6275')-135),
     'verification':'PASS: all displayed row P/L, price x quantity within one cent, total, aggregate open P/L and daily P/L reconcile.'}
(ROOT/'summary.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
print(json.dumps(out,indent=2,default=str))
