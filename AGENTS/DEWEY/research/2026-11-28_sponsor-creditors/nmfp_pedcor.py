"""Leg 2 helper: list Pedcor-named holdings in money-market fund N-MFP/N-MFP2/N-MFP3 filings (EDGAR full text + XML parse).
Run from repo root: python3 AGENTS/DEWEY/research/2026-11-28_sponsor-creditors/nmfp_pedcor.py <outdir>  (a failed fetch prints FETCH-FAIL and is skipped)
Prints one line per (filing, Pedcor holding): fund filer, report date, issuer/title, CUSIP, principal/value,
demand-feature issuer, guarantor, enhancement provider. SEC declared-contact client string (scripts/sec_contact.py).
"""
import sys, json, re, time, urllib.request, urllib.parse, os
sys.path.append('scripts'); from sec_contact import sec_ua
UA = sec_ua("Research DEWEY {}"); OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
def get(url):
    for a in range(3):
        try: return urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=120).read().decode('utf-8', 'replace')
        except Exception as e: time.sleep(2)
    print('FETCH-FAIL', url, file=sys.stderr); return ''
def fts(q, forms, s, e, frm=0):
    p = {'q': q, 'dateRange': 'custom', 'startdt': s, 'enddt': e, 'from': frm, 'forms': forms}
    return json.loads(get('https://efts.sec.gov/LATEST/search-index?' + urllib.parse.urlencode(p)))
hits = []
for forms in ('N-MFP', 'N-MFP2', 'N-MFP3'):
    frm = 0
    while True:
        j = fts('"Pedcor"', forms, '2010-01-01', '2026-11-28', frm); hh = j['hits']['hits']; hits += hh
        frm += len(hh)
        if not hh or frm >= j['hits']['total']['value']: break
seen = set(); rows = []
for x in hits:
    acc, fn = x['_id'].split(':'); cik = x['_source']['ciks'][0]
    if (acc, fn) in seen or not fn.endswith('.xml'): continue
    seen.add((acc, fn))
    t = get(f'https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace("-", "")}/{fn}'); time.sleep(0.25)
    rep = (re.search(r'<reportDate>(.*?)</reportDate>', t) or re.search(r'<(?:\w+:)?reportDate>(.*?)<', t) or [None, ''])[1]
    for b in re.split(r'<scheduleOfPortfolioSecuritiesInfo>', t)[1:]:
        if 'PEDCOR' not in b.upper(): continue
        g = lambda tag: '; '.join(re.sub(r'\s+', ' ', m) for m in re.findall(rf'<{tag}>(.*?)</{tag}>', b, re.S))
        rows.append(dict(file_date=x['_source']['file_date'], form=x['_source']['form'], filer=x['_source']['display_names'][0][:50], acc=acc,
                         report_date=rep, issuer=g('nameOfIssuer'), title=g('titleOfIssuer')[:160], cusip=g('CUSIPMember'),
                         value=g('includingValueOfAnySponsorSupport') or g('availableForSaleSecuritiesValue') or g('amortizedCost') or g('valueOfSecurity'),
                         demand=g('identityOfDemandFeatureIssuer'), guarantor=g('identityOfGuarantor'), enh=g('identityOfEnhancementProvider')))
json.dump(rows, open(f'{OUT}/nmfp_pedcor_rows.json', 'w'), indent=1)
print(len(seen), 'filings parsed,', len(rows), 'Pedcor holding rows')
