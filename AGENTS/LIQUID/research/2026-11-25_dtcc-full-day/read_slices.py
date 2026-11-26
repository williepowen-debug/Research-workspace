#!/usr/bin/env python3
# read_slices.py SLICE_DIR [OUT_CSV] (LIQUID 2026-11-25, D:L1290 Part B): all DTCC PPD SEC intraday credit slices for one day ->
# CoreWeave, SoftBank (JPY, 1% discount rate), Oracle, Alphabet, SpaceX conventional spreads via crwv_cds_grade.conv_spread.
# Cancels matched by trade ID across ALL rows; names matched in both name fields.
import sys, glob, zipfile, io, csv, re, datetime as dt
sys.path.insert(0, '/home/willi/Research-workspace/AGENTS/LIQUID/scripts')
import crwv_cds_grade as g
D = dt.date
rows = []
for f in sorted(glob.glob(sys.argv[1] + '/*.zip'), key=lambda p: int(re.findall(r'_(\d+)\.zip', p)[0])):
    n = int(re.findall(r'_(\d+)\.zip', f)[0])
    z = zipfile.ZipFile(f)
    for r in csv.DictReader(io.TextIOWrapper(z.open(z.namelist()[0]), encoding='utf-8', errors='replace')):
        r['_slice'] = n; rows.append(r)
print('rows', len(rows)); LASTCOL = list(rows[0].keys())[-2]; print('lastcol', LASTCOL)
NAMES = {'COREWEAVE': 0.04, 'SOFTBANK': 0.01, 'ORACLE': 0.04, 'ALPHABET': 0.04, 'SPACE EXPLORATION': 0.04}
NM = lambda x: ((x.get("Underlying Asset Name") or "") + " | " + (x.get(LASTCOL) or "")).upper()
for key, r_disc in NAMES.items():
    NM = lambda x: ((x.get('Underlying Asset Name') or '') + ' | ' + (x.get(LASTCOL) or '')).upper()
    cw = [x for x in rows if key in NM(x)]
    live = {}; dead = {}; 
    for x in cw:
        if x['Action type'] == 'NEWT': live.setdefault(x['Dissemination Identifier'], x)
    for x in cw:
        o = x['Original Dissemination Identifier']
        if o in live and x['Action type'] in ('CORR', 'MODI'): live[o] = dict(x, _corr='CORR')
    for x in rows:
        if x['Action type'] in ('CANC', 'ERRO', 'TERM', 'EROR'): dead[x['Original Dissemination Identifier']] = (x['Action type'], x['_slice'])
    acts = sorted(set(x['Action type'] for x in cw))
    print(f'\n== {key}: {len(cw)} rows, actions {acts}, live NEWT {len(live)}, cancels {len(dead)}')
    for i, x in sorted(live.items(), key=lambda p: p[1]['Execution Timestamp']):
        n = x['Notional amount-Leg 1']; ccy = x.get('Notional currency-Leg 1', '')
        flags = []
        if i in dead: flags.append('DEAD:%s@%s' % dead[i])
        if '+' in n: flags.append('CAPPED')
        if x['Non-standardized term indicator'] != 'FALSE': flags.append('NONSTD')
        if x['Package indicator'] not in ('FALSE', 'false', ''): flags.append('PKG')
        try:
            mat = D.fromisoformat(x['Expiration Date']); trade = D.fromisoformat(x['Execution Timestamp'][:10])
        except Exception:
            print('  bad date', i); continue
        if trade != D(2026, 11, 25): flags.append('LATE:' + str(trade))
        if mat.day != 20: flags.append('NONIMM')
        yrs = (mat - trade).days / 365.25
        try:
            notl = float(n.replace(',', '').replace('+', '')); c = float(x['Fixed rate-Leg 1']); U = float(x['Other payment amount']) / notl
            assert x['Other payment type'] == 'UFRO'
            if yrs < 0.6: raise ValueError('short')
            s = g.conv_spread(U, c, trade, mat, r=r_disc) * 1e4; sd = g.conv_spread(U, c, trade, mat, r=r_disc, dirty=True) * 1e4
            lvl = f'{s:5.0f} (dirty {sd:5.0f})'
        except Exception as e:
            lvl = f'no level ({type(e).__name__}) cpn {x["Fixed rate-Leg 1"]} upf {x["Other payment amount"]}'
        print(f"  {x['Execution Timestamp'][:16]}Z s{x['_slice']} id {i} mat {mat} ({yrs:.1f}y) {ccy} {n:>11} {lvl} {','.join(flags)} {x.get('_corr','')} {x.get('Platform identifier','')}")

# Evidence dump (2026-11-25): every row for the five names plus every cancel row that names one of their trade IDs.
if len(sys.argv) > 2:
    keep = [x for x in rows if any(k in NM(x) for k in NAMES)]
    ids = {x['Dissemination Identifier'] for x in keep}
    keep += [x for x in rows if x['Action type'] in ('CANC', 'ERRO', 'TERM', 'EROR') and x['Original Dissemination Identifier'] in ids and x not in keep]
    with open(sys.argv[2], 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); [w.writerow(x) for x in keep]
    print('wrote', len(keep), 'rows to', sys.argv[2])
