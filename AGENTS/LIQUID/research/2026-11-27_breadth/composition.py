"""Composition of the HY widening in HYG's own holdings (LIQUID 2026-11-27, RED ask 2 on D:L1279).

Usage: python3 -I composition.py OLD.xls[.gz] OLD_UST.csv OLD_DATE NEW.xls[.gz] NEW_UST.csv NEW_DATE
Marks are BlackRock's evaluated vendor prices, not TRACE trades. Spread = yield to worst minus the
Treasury par curve interpolated at the bond's own modified duration (approximate, NOT OAS, KB-LIQ-165).
HYG carries no ratings: the 'BB-like' bucket is a START-SPREAD proxy (bonds whose start spread sits in
the BB band), never the ICE BB index itself. Weighted by NEW market value."""
import re, csv, sys, gzip, statistics as st

def load(p):
    t = (gzip.open if p.endswith('.gz') else open)(p, 'rt', encoding='utf-8-sig', errors='replace').read()
    ws = re.search(r'<ss:Worksheet ss:Name="Holdings"(.*?)</ss:Worksheet>', t, re.S)
    t = ws.group(1) if ws else t
    R = [[x.replace('&amp;', '&') for x in re.findall(r'<ss:Data[^>]*>(.*?)</ss:Data>', r, re.S)]
         for r in re.findall(r'<ss:Row[^>]*>(.*?)</ss:Row>', t, re.S)]
    asof = next((r[1] for r in R if r[:1] == ['Fund Holdings as of'] and len(r) > 1), '?')
    i = next(k for k, r in enumerate(R) if r[:1] == ['Name'] and 'Yield to Worst (%)' in r)
    H = R[i]; out = {}
    for r in R[i + 1:]:
        if len(r) != len(H): break
        d = dict(zip(H, r))
        if d['Asset Class'] != 'Fixed Income': continue
        try:
            v = dict(px=float(d['Price']), ytw=float(d['Yield to Worst (%)']), dur=float(d['Mod. Duration']),
                     mv=float(d['Market Value']), sec=d['Sector'], name=d['Name'].replace(' 144A', '').replace(' RegS', ''))
        except ValueError:
            continue
        out[(v['name'], d['Coupon (%)'], d['Maturity'])] = v
    return asof, out

T = {'1 Mo': 1/12, '3 Mo': .25, '6 Mo': .5, '1 Yr': 1, '2 Yr': 2, '3 Yr': 3, '5 Yr': 5, '7 Yr': 7, '10 Yr': 10}
def curve(p, date):
    for r in csv.DictReader(open(p)):
        if r['Date'] == date: return sorted((T[k], float(r[k])) for k in T)
    raise SystemExit('no curve ' + date)
def itp(c, x):
    if x <= c[0][0]: return c[0][1]
    for (a, ya), (b, yb) in zip(c, c[1:]):
        if a <= x <= b: return ya + (yb - ya) * (x - a) / (b - a)
    return c[-1][1]

AI = ('COREWEAVE', 'APPLIED DIGITAL', 'APLD', 'CIPHER', 'TERAWULF', 'IREN', 'CORE SCIENTIFIC', 'GALAXY DIGITAL',
      'VANTAGE DATA', 'ALIGNED DATA', 'SWITCH', 'CYRUSONE', 'QTS', 'STACK INFRA', 'COLOGIX', 'DATABANK', 'FLEXENTIAL',
      'EDGECONNEX', 'NEBIUS', 'LAMBDA', 'CRUSOE', 'WULF', 'HUT 8', 'BITDEER', 'MERIDIAN ARC', 'PROJECT JUPITER')

oa, A = load(sys.argv[1]); ca = curve(sys.argv[2], sys.argv[3])
ob, B = load(sys.argv[4]); cb = curve(sys.argv[5], sys.argv[6])
sp = lambda v, c: 100 * (v['ytw'] - itp(c, v['dur']))
com = [k for k in set(A) & set(B) if 0.5 <= B[k]['dur'] <= 12 and A[k]['ytw'] < 30 and B[k]['ytw'] < 30]
print(f'files: {oa} -> {ob}; bonds {len(A)} / {len(B)}; common, duration 0.5-12, YTW<30: {len(com)}')
rows = [(k, B[k]['mv'], sp(A[k], ca), sp(B[k], cb) - sp(A[k], ca)) for k in com]
isai = lambda k: k[0].upper().startswith(AI) or any(a in k[0].upper() for a in ('COREWEAVE', 'DATA CENTER', 'DATACENTER'))

def report(label, rs):
    W = sum(r[1] for r in rs); tot = sum(r[1] * r[3] for r in rs) / W
    print(f'\n== {label}: n {len(rs)}, MV ${W/1e9:.2f}B, MV-weighted spread change {tot:+.1f} bp, '
          f'median {st.median(r[3] for r in rs):+.0f} bp')
    by = {}
    for r in rs: by.setdefault(B[r[0]]['sec'], []).append(r)
    print('| Sector | n | MV share | wtd chg bp | share of the widening |')
    for s, v in sorted(by.items(), key=lambda p: -sum(r[1] * r[3] for r in p[1])):
        w = sum(r[1] for r in v); c = sum(r[1] * r[3] for r in v)
        print(f'| {s} | {len(v)} | {100*w/W:.1f}% | {c/w:+.1f} | {100*c/(tot*W):.1f}% |')
    a = [r for r in rs if isai(r[0])]
    if a:
        w = sum(r[1] for r in a); c = sum(r[1] * r[3] for r in a)
        print(f'| AI / data-centre NAMED issuers | {len(a)} | {100*w/W:.1f}% | {c/w:+.1f} | {100*c/(tot*W):.1f}% |')
        for r in sorted(a, key=lambda r: -r[3])[:12]:
            print(f'    {r[0][0]} {r[0][1]}% {r[0][2]}: start {r[2]:.0f}, chg {r[3]:+.0f}, MV ${r[1]/1e6:.0f}M')
    iss = {}
    for r in rs: iss.setdefault(r[0][0], []).append(r)
    top = sorted(iss.items(), key=lambda p: -sum(r[1] * r[3] for r in p[1]))[:10]
    print('  top 10 issuers by contribution (bp of the bucket change):')
    for n, v in top:
        print(f'    {n} [{B[v[0][0]]["sec"]}]: {sum(r[1]*r[3] for r in v)/W:+.2f} bp of {tot:+.1f}; own wtd chg {sum(r[1]*r[3] for r in v)/sum(r[1] for r in v):+.0f}')
    ex = [r for r in rs if not isai(r[0]) and B[r[0]]['sec'] != 'Technology']
    w = sum(r[1] for r in ex)
    print(f'  EX Technology sector AND ex named AI issuers: n {len(ex)}, wtd chg {sum(r[1]*r[3] for r in ex)/w:+.1f} bp, '
          f'median {st.median(r[3] for r in ex):+.0f}; share of bonds wider: {100*sum(r[3] > 0 for r in ex)/len(ex):.0f}%')

report('ALL HYG common bonds', rows)
lo, hi = float(sys.argv[7]) if len(sys.argv) > 7 else 100, float(sys.argv[8]) if len(sys.argv) > 8 else 260
report(f'BB-like proxy: start spread {lo:.0f}-{hi:.0f} bp', [r for r in rows if lo <= r[2] <= hi])

# --- BB-rated membership (added same session): argv[9] = an iShares HYBB fund file (BB-rated, ICE BB
# constrained index). HYG bonds whose (name, coupon, maturity) appear in HYBB on ITS date are BB-rated on
# that date; their HYG two-date spread change is the BB composition read. Membership is as of the HYBB
# file date only (a bond downgraded out of BB before that date is missed; one upgraded in is included).
if len(sys.argv) > 9:
    hb, H = load(sys.argv[9])
    bb = [r for r in rows if r[0] in H]
    print(f'\nHYBB file {hb}: {len(H)} bonds; matched in HYG common set: {len(bb)}')
    report('BB-RATED (in HYBB) HYG bonds', bb)
    W = sum(v['mv'] for v in H.values())
    by = {}
    for k, v in H.items(): by[v['sec']] = by.get(v['sec'], 0) + v['mv']
    print('\nHYBB own sector weights (MV, its file date):', ', '.join(f'{s} {100*w/W:.1f}%' for s, w in sorted(by.items(), key=lambda p: -p[1])[:8]))
    ai = [(k, v) for k, v in H.items() if isai(k)]
    print('HYBB named AI / data-centre issuers:', ', '.join(f'{k[0]} {100*v["mv"]/W:.2f}%' for k, v in ai) or 'none')
    iss = {}
    for k, v in H.items(): iss[k[0]] = iss.get(k[0], 0) + v['mv']
    print('HYBB top 12 issuers:', ', '.join(f'{n} {100*w/W:.2f}%' for n, w in sorted(iss.items(), key=lambda p: -p[1])[:12]))
