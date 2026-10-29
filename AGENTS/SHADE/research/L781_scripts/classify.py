import json, collections, sys
d=json.load(open(sys.argv[1]))
H=[h for h in d['holdings'] if h.get('line') and h['line']<'2000000000' and h['line']>='1000000000']
print('holdings in ABS', len(H), 'sum', sum(h['bacv'] for h in H))
rc=collections.Counter(h['rcode'] for h in H); print('rcode counts', rc)
rcb=collections.defaultdict(int)
for h in H: rcb[h['rcode']]+=h['bacv']
print('rcode BACV', dict(rcb))
sy=collections.Counter(h['sym'] for h in H); print('sym counts', sy)
agency={'1019999999','1029999999','1039999999','1049999999'}
nsl={'1319999999','1329999999','1339999999','1349999999'}
nonfin_full={'1719999999','1729999999','1739999999'}
aff={'1129999999'}  # inside 1899999999 affiliated total
def psym(s):
    for t in s.split():
        if t in ('PL','PLGI','Z') or t.startswith('RT') or t.startswith('ND'): return True
    return False
B=collections.defaultdict(int); N=collections.Counter(); why=collections.defaultdict(int)
for h in H:
    if h['rcode']=='R': b='C'
    elif h['line'] in agency: b='L'
    else:
        flags=[]
        if h['line'] in aff: flags.append('affiliated')
        if psym(h['sym']): flags.append('svo:'+h['sym'])
        if h['line'] in nsl: flags.append('NSL')
        if h['line'] in nonfin_full: flags.append('nonfin-full')
        if h['rcode'] in ('M','O'): flags.append('rcode'+h['rcode'])
        b='P' if flags else 'U'
        if flags: why[flags[0].split(':')[0]]+=h['bacv']
    h['bucket']=b; B[b]+=h['bacv']; N[b]+=1
print('buckets', dict(B), dict(N)); print('P first-flag split', dict(why))
byline=collections.defaultdict(lambda: collections.defaultdict(int))
for h in H: byline[h['line']][h['bucket']]+=h['bacv']
for k in sorted(byline): print(k, dict(byline[k]))
json.dump(H,open(sys.argv[2],'w'))
