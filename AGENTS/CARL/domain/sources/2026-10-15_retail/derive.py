import sys, json
import pandas as pd
xlsx, outp = sys.argv[1], sys.argv[2]
cpi = json.loads(sys.argv[3])  # {"FAH":[cur,yago],"FAFH":[cur,yago],"APP":[cur,yago]}
s = pd.read_excel(xlsx, sheet_name='Table 1.', header=None)
hdr = ' '.join(str(v) for v in s.iloc[84].tolist() if str(v) != 'nan')
lab = {}
for i in range(10, 68):
    code = str(s.iloc[i, 0]).strip(); name = str(s.iloc[i, 1]).strip()
    vals = list(s.iloc[i, 9:14])
    if all(str(v) == 'nan' for v in vals): continue
    key = code if code != 'nan' else name[:30]
    lab[key] = vals
def g(k):
    for kk, v in lab.items():
        if kk.startswith(k): return v
    raise KeyError(k)
# SA columns: [cur(a), prev(p), prev2(r), yago(r), yago_prev(r)]
tot = g('total'); retail = g('Retail'); mv = g('441'); bld = g('supplies dealers'); gas = g('447'); fs = g('722')
fb = g('445'); gm = g('452'); clo = g('stores ……'); nonstore = g('454')
def num(v): return float(v)
def ctrl(j): return num(tot[j]) - num(mv[j]) - num(bld[j]) - num(gas[j]) - num(fs[j])
pct = lambda a, b: 100 * (a / b - 1)
out = {
 'source_line': hdr,
 'headline_mom': pct(num(tot[0]), num(tot[1])),
 'headline_prev_mom': pct(num(tot[1]), num(tot[2])),
 'headline_yoy': pct(num(tot[0]), num(tot[3])),
 'ex_auto_mom': pct(num(tot[0]) - num(mv[0]), num(tot[1]) - num(mv[1])),
 'ex_auto_gas_mom': pct(num(tot[0]) - num(mv[0]) - num(gas[0]), num(tot[1]) - num(mv[1]) - num(gas[1])),
 'gas_mom': pct(num(gas[0]), num(gas[1])),
 'control_levels': [ctrl(0), ctrl(1), ctrl(2), ctrl(3)],
 'control_mom': pct(ctrl(0), ctrl(1)),
 'control_prev_mom': pct(ctrl(1), ctrl(2)),
 'control_yoy': pct(ctrl(0), ctrl(3)),
 'control_ex_nonstore_mom': pct(ctrl(0) - num(nonstore[0]), ctrl(1) - num(nonstore[1])),
 'T1a_grocery_real_yoy': pct(num(fb[0]) / num(fb[3]), cpi['FAH'][0] / cpi['FAH'][1]),
 'T1a_restaurant_real_yoy': pct(num(fs[0]) / num(fs[3]), cpi['FAFH'][0] / cpi['FAFH'][1]),
 'T1b_gm_share_yago': 100 * num(gm[3]) / num(retail[3]),
 'T1b_gm_share_prev': 100 * num(gm[1]) / num(retail[1]),
 'T1b_gm_share_cur': 100 * num(gm[0]) / num(retail[0]),
 'T1c_apparel_real_yoy': pct(num(clo[0]) / num(clo[3]), cpi['APP'][0] / cpi['APP'][1]),
 'raw': {k: [str(x) for x in v] for k, v in lab.items()},
}
out['T1a_spread_pp'] = out['T1a_grocery_real_yoy'] - out['T1a_restaurant_real_yoy']
json.dump(out, open(outp, 'w'), indent=1)
for k, v in out.items():
    if k not in ('raw',): print(k, v)
