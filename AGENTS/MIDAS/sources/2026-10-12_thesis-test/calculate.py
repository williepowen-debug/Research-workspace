"""Static evidence audit for Will's October12 bounded thesis test; no monitor."""
from pathlib import Path
import hashlib
import json

B = Path(__file__).resolve().parent

def pct(current, prior):
    return (current / prior - 1) * 100

# Manually transcribed from PRIMARY CADA September2026 charts3/4/6/7,
# viewed directly. Unit: wan vehicles (10,000). Comparators are the prior-
# September levels PRINTED IN THIS VINTAGE, not the October2025 first release.
current = dict(production=259.0, wholesale=254.9, retail=161.8, exports=91.7,
               bev_production=110.6, bev_wholesale=112.6, bev_retail=76.5,
               bev_exports=33.8, nev_retail=108.4, nev_wholesale=166.6,
               phev_wholesale=42.3, erev_wholesale=11.7)
prior = dict(production=285.0, wholesale=279.9, retail=224.7, exports=52.8,
             bev_production=95.3, bev_wholesale=95.2, bev_retail=83.5,
             bev_exports=14.0, nev_retail=130.2, nev_wholesale=149.6,
             phev_wholesale=42.3, erev_wholesale=12.2)
first_2025 = dict(production=283.8, wholesale=280.3, retail=224.1,
                  bev_wholesale=94.7, phev_wholesale=42.4, erev_wholesale=12.9)

out = {
    'unit': 'wan vehicles = 10,000 vehicles',
    'scope': 'narrow passenger: sedans/MPV/SUV; exports include whole vehicles and CKD',
    'source': 'CADA/CPCA September2026 charts3/4/6/7; source monthly report initial draft',
    'current_sep2026': current, 'sep2025_comparators_in_sep2026_vintage': prior,
    'sep2025_first_release_oct13_2025': first_2025,
    'reported_rates_pct': {'production': -9.1, 'wholesale': -8.9, 'retail': -28.0,
                           'conventional_fuel_domestic_retail_includes_HEV': -43,
                           'pure_fuel_domestic_retail': -49, 'ordinary_HEV_domestic_retail': 25},
    'rounded_table_rate_recalculations_pct': {k:pct(current[k], prior[k]) for k in current if k in prior},
    'cross_vintage_rate_recalculations_pct': {k:pct(current[k], first_2025[k]) for k in first_2025},
    'series_limits': ['Rounded table levels need not reproduce issuer percentages exactly.',
                      'Older releases retain their as-published vintage; current charts revise prior bases.',
                      'September2026 chart7 prior EREV production prints1.2wan, inconsistent with NEV total and13.3% rate; excluded, not silently repaired.'],
    'current_vintage_persistence': {
        'retail_yoy_pct_Jan_to_Sep': [-13.9,-25.4,-15.0,-21.5,-22.1,-23.2,-20.9,-23.6,-28.0],
        'wholesale_yoy_pct_Jan_to_Sep': [-6.2,-14.3,-1.6,-4.0,-4.5,-5.7,-0.2,-5.1,-8.9],
        'retail_YTD_yoy_pct': -21.7, 'production_YTD_yoy_pct': -5.5,
        'production_yoy_pct_Jul_Aug_Sep_from_each_release': [-1.6,-4.5,-9.1],
        'conventional_fuel_retail_yoy_pct_Jul_Aug_Sep_from_each_release': [-41,-40,-43],
        'vintage_note': 'September chart revises August wholesale to235.8wan/-5.1%; August first release235.3wan/-5.3%. Older releases preserved, not mixed.'
    }
}
for stage in ['production', 'wholesale', 'retail', 'exports']:
    a = current[stage] - current['bev_' + stage]
    z = prior[stage] - prior['bev_' + stage]
    # Four rounded levels have +/-0.05wan uncertainty apiece. This is a
    # rounding envelope only, not a statistical or revision confidence band.
    out['non_BEV_' + stage + '_proxy'] = {
        'current_wan': a, 'prior_wan': z, 'yoy_pct': pct(a,z),
        'rounding_only_yoy_pct_bounds': [pct(a-.1,z+.1), pct(a+.1,z-.1)],
        'limit': 'Residual vehicle proxy, not observed catalyst installations or PGM demand; commercial vehicles excluded; CKD fitment origin uncertain for exports.'
    }
out['domestic_wholesale_residual'] = {
    'current_wan': current['wholesale'] - current['exports'],
    'prior_wan': prior['wholesale'] - prior['exports'],
    'limit': 'Wholesale less exports arithmetic; not retail demand or an independent series.'
}
out['conventional_fuel_retail_residual'] = {
    'current_wan': current['retail']-current['nev_retail'],
    'prior_wan': prior['retail']-prior['nev_retail'],
    'yoy_pct': pct(current['retail']-current['nev_retail'],prior['retail']-prior['nev_retail']),
    'limit': 'Issuer separately prints53wan and-43% at coarser precision; non-NEV includes ordinary HEV.'
}
out['bev_wholesale_share_pct'] = current['bev_wholesale']/current['wholesale']*100
out['component_identities'] = {
    'current_nev_wholesale_sum_wan': current['bev_wholesale']+current['phev_wholesale']+current['erev_wholesale'],
    'current_nev_wholesale_total_wan': current['nev_wholesale'],
    'prior_nev_wholesale_sum_wan': prior['bev_wholesale']+prior['phev_wholesale']+prior['erev_wholesale'],
    'prior_nev_wholesale_total_wan': prior['nev_wholesale'],
    'chart7_bad_prior_nev_production_component_sum_wan': 95.3+44.3+1.2,
    'chart7_prior_nev_production_total_wan': 150.8,
    'erev_production_yoy_excluded': True
}
assert abs(out['component_identities']['current_nev_wholesale_sum_wan']-current['nev_wholesale']) < 1e-8
assert abs(out['component_identities']['prior_nev_wholesale_sum_wan']-prior['nev_wholesale']) <= .10000001
assert abs(out['rounded_table_rate_recalculations_pct']['production']+9.1) < .05
assert abs(out['rounded_table_rate_recalculations_pct']['wholesale']+8.9) < .05
curve = json.loads((B/'silver_curve_capture.json').read_text())
out['silver_calendar_spread'] = {}
for day in ['2026-09-30','2026-10-09']:
    near = curve['histories']['SIZ26.CMX']['points'][day]
    far = curve['histories']['SIH27.CMX']['points'][day]
    assert near['close'] > 0 and far['close'] > 0 and near['volume'] > 0 and far['volume'] > 0
    out['silver_calendar_spread'][day] = {
        'SIZ26_Dec2026_USD_oz': near['close'], 'SIH27_Mar2027_USD_oz': far['close'],
        'Mar_minus_Dec_USD_oz': far['close']-near['close'],
        'Mar_premium_pct': (far['close']/near['close']-1)*100,
        'basis': 'MIRROR unadjusted daily vendor Close, not certified settlement; same-date named contracts',
        'limit': 'Distant US calendar spread includes carry/rates/storage/regional basis; not London spot availability or an implied lease-rate measurement.'
    }
out['JM_May2026_2025_demand_mix'] = {
    'Pd_auto_koz':8227,'Pd_total_koz':10140,'Pd_auto_share_pct':8227/10140*100,
    'Pt_auto_koz':3329,'Pt_total_koz':8019,'Pt_auto_share_pct':3329/8019*100,
    'basis':'PRIMARY JM May2026 report tables printedp27/29, 2025 estimates; wider automotive scope than CPCA passenger cars.'
}
out['thesis_dispositions'] = {
    'platinum_overall_2026_surplus_longer_term_supply_constraint': 'UNCHANGED; automotive rebound support WEAKENED',
    'palladium_supply_tightening_only': 'WEAKENED',
    'silver_depletion_only': 'WEAKENED',
    'silver_available_supply_tightness': 'UNCHANGED / UNRESOLVED',
    'gold': 'UNCHANGED; no new conclusion-changing evidence sought',
    'copper': 'UNCHANGED; supply restraint remains distinct from demand strength'
}
(B/'audit_calculations.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:v for k,v in out.items() if k.startswith('non_BEV_') or k in ['silver_calendar_spread','JM_May2026_2025_demand_mix']},indent=2))
