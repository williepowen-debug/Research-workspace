"""Aggregate FL DOR NAL rolls: parcels whose owner mailing address is in Canada.
Usage: python3 -I nal_canada.py OUT.json ZIP [ZIP...]"""
import csv, io, json, re, sys, zipfile, collections
PROV = {'ON','QC','BC','AB','MB','SK','NS','NB','NL','PE','YT','NT','NU','ONTARIO','QUEBEC','BRITISH COLUMBIA','ALBERTA','MANITOBA','SASKATCHEWAN','NOVA SCOTIA','NEW BRUNSWICK','NEWFOUNDLAND','PRINCE EDWARD ISLAND'}
PC = re.compile(r'\b[A-Z]\d[A-Z]\s?\d[A-Z]\d\b')
RES = {'000':'vacant residential','001':'single family','002':'mobile home','003':'multifamily 10+','004':'condominium','005':'cooperative','006':'retirement home','007':'misc residential','008':'multifamily <10','009':'residential common area'}
def num(x):
    try: return float(x)
    except: return 0.0
out = {}
for zp in sys.argv[2:]:
    z = zipfile.ZipFile(zp); name = [n for n in z.namelist() if n.lower().endswith('.csv')][0]
    f = io.TextIOWrapper(z.open(name), encoding='latin-1', newline='')
    r = csv.DictReader(f)
    c = collections.defaultdict(lambda: collections.Counter())
    prov = collections.Counter(); rule = collections.Counter(); onlypc = 0; onlystate = 0; rows = 0; yr = set()
    for row in r:
        rows += 1; yr.add(row['ASMNT_YR'])
        uc = row['DOR_UC'].strip().zfill(3)
        isres = uc in RES
        st = row['OWN_STATE'].strip().upper()
        blob = ' '.join(row[k] for k in ('OWN_ADDR1','OWN_ADDR2','OWN_CITY','OWN_ZIPCD')).upper()
        bystate = st == 'CANADA'; byprov = st in PROV; rule[('state=CANADA' if bystate else 'state=province' if byprov else None)] += 1; bystate = bystate or byprov; bypc = bool(PC.search(blob)) and st in ('', 'CANADA') 
        if bystate and not PC.search(blob): onlystate += 1
        if bypc and not bystate: onlypc += 1
        can = bystate or bypc
        jv = num(row['JV']); hm = num(row['JV_HMSTD'])
        key = 'all'
        c[key]['parcels'] += 1; c[key]['jv'] += jv
        if isres:
            c['res']['parcels'] += 1; c['res']['jv'] += jv
            if hm == 0:
                c['res_nonhmstd']['parcels'] += 1; c['res_nonhmstd']['jv'] += jv
        if can:
            c['can_all']['parcels'] += 1; c['can_all']['jv'] += jv
            if isres:
                c['can_res']['parcels'] += 1; c['can_res']['jv'] += jv
                c['can_res_uc_'+RES[uc]]['parcels'] += 1; c['can_res_uc_'+RES[uc]]['jv'] += jv
                if hm > 0: c['can_res_hmstd']['parcels'] += 1
            m = re.search(r'\b(ON|QC|BC|AB|MB|SK|NS|NB|NL|PE|YT|NT|NU)\b\s*$', row['OWN_CITY'].strip().upper())
            prov[st if st in PROV else (m.group(1) if m else '?')] += 1
    out[name] = {'zip': zp.split('/')[-1], 'rows': rows, 'assessment_years': sorted(yr),
                 'cells': {k: dict(v) for k, v in c.items()},
                 'canada_by_province_city_suffix': dict(prov.most_common()),
                 'match_rule_counts': {str(k): v for k, v in rule.items() if k}, 'canada_state_without_postcode': onlystate, 'canada_postcode_without_state': onlypc}
    print(name, rows, dict(c['can_res']), file=sys.stderr)
json.dump(out, open(sys.argv[1], 'w'), indent=1)
