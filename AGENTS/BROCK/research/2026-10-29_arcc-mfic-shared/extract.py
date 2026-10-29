"""Extract per-position 6/30/2026 SOI facts from a BDC XBRL instance.

usage: python3 -I extract.py <instance.xml> <instant YYYY-MM-DD> <out.json>
One record per context whose only dimension is InvestmentIdentifierAxis (typed member).
Records keep the issuer's identifier string verbatim; no matching happens here.
"""
import json, sys, collections
import xml.etree.ElementTree as ET

path, instant, out = sys.argv[1:4]
local = lambda t: t.rsplit('}', 1)[-1]
root = ET.parse(path).getroot()
units, ctx = {}, {}
for e in root:
    tag = local(e.tag)
    if tag == 'unit':
        units[e.attrib['id']] = ' '.join(x.text or '' for x in e.iter() if local(x.tag) == 'measure').split(':')[-1].upper()
    if tag != 'context':
        continue
    ins = e.find('.//{*}instant')
    dims = [x for x in e.iter() if local(x.tag) in ('typedMember', 'explicitMember')]
    if ins is None or ins.text != instant or len(dims) != 1:
        continue
    d = dims[0]
    if local(d.tag) == 'typedMember' and d.attrib.get('dimension', '').endswith('InvestmentIdentifierAxis'):
        ctx[e.attrib['id']] = ''.join(d.itertext()).strip()
WANT = {'InvestmentOwnedAtFairValue': 'fv', 'InvestmentOwnedAtCost': 'cost',
        'InvestmentOwnedBalancePrincipalAmount': 'par',
        'InvestmentCompanyFinancialCommitmentToInvesteeFutureAmount': 'unfunded'}
recs = collections.defaultdict(dict)
for e in root:
    c = e.attrib.get('contextRef')
    if c not in ctx or local(e.tag) not in WANT or e.text is None:
        continue
    try:
        v = float(e.text)
    except ValueError:
        continue
    k = WANT[local(e.tag)]
    if k in recs[c] and recs[c][k] != v:
        raise ValueError(('conflicting fact', c, k))
    recs[c][k] = v
    if k == 'par':
        recs[c]['par_unit'] = units.get(e.attrib.get('unitRef'), e.attrib.get('unitRef', ''))
rows = [dict(ctx=c, id=ctx[c], **f) for c, f in recs.items()]
json.dump(rows, open(out, 'w'), indent=0)
fv = sum(r.get('fv', 0) for r in rows)
print(f'{path}: {len(rows)} position contexts, FV sum {fv/1e6:,.1f}M, with par {sum(1 for r in rows if "par" in r)}')
