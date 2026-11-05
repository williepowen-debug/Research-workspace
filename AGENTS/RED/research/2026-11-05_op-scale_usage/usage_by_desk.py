import json,glob,os,re,collections,datetime,sys
root=os.path.expanduser('~/.claude/projects')
since,until=sys.argv[1],sys.argv[2]
DESKS="PROME WALTER TERRY RED HENRY LIQUID VIOLET SAM BOND ZHAO VULCAN BROCK REGINALD DEWEY BRENT AEOLUS NEXUS WAL OZK FLG MIDAS FALCON CARL LABOR HAWK MARCO ORACLE CORAL SHADE WATT OSPREY HOMER YURI CRUISE FERT GIBBS CYPHER ISHM CREED HANS OTTO DAEDALUS RAV CATO".split()
T=collections.Counter(); C=collections.Counter(); seen={}; S=collections.defaultdict(set)
rx=re.compile(r'(?:You are|you are) ('+'|'.join(DESKS)+r')\b|AGENTS/('+'|'.join(DESKS)+r')/CLAUDE\.md')
def desk_of(path,d):
    # first user text
    try:
        with open(path,encoding='utf-8',errors='replace') as fh:
            for i,l in enumerate(fh):
                if i>12: break
                if '"role":"user"' not in l and '"type":"user"' not in l: continue
                try:o=json.loads(l)
                except: continue
                c=(o.get('message') or {}).get('content')
                if isinstance(c,list): c=' '.join(x.get('text','') for x in c if isinstance(x,dict))
                if not isinstance(c,str): continue
                m=rx.search(c[:4000])
                if m: return m[1] or m[2]
    except: pass
    return None
for d in sorted(os.listdir(root)):
    if not d.startswith('-home-willi-Research-workspace'): continue
    name=d.replace('-home-willi-Research-workspace','').replace('-AGENTS-','').strip('-') or 'ROOT'
    for f in glob.glob(os.path.join(root,d,'**','*.jsonl'),recursive=True):
        if os.path.getmtime(f)<datetime.datetime.fromisoformat(since).timestamp(): continue
        sub='/subagents/' in f
        who=name
        tag=''
        if sub or name=='PROME':
            w=desk_of(f,d)
            if w and w!=name: who=w; tag='spawned-from-'+name
            elif sub:
                who=name+'+reader'
        for line in open(f,encoding='utf-8',errors='replace'):
            if '"usage"' not in line: continue
            try:o=json.loads(line)
            except: continue
            ts=o.get('timestamp','')
            if not(since<=ts[:10]<=until): continue
            m=o.get('message') or {}; u=m.get('usage')
            if not isinstance(u,dict): continue
            k=m.get('id') or o.get('uuid')
            # A message can span several transcript lines with growing output_tokens:
            # keep the LAST line per message id, so output is not undercounted.
            seen[k]=(who,f,u)
for k,(who,f,u) in seen.items():
    T[who]+=u.get('input_tokens',0)+u.get('cache_creation_input_tokens',0)+u.get('output_tokens',0)
    C[who]+=u.get('cache_read_input_tokens',0)
    S[who].add(f)
sT=sum(T.values()); sC=sum(C.values())
print('CLAUDE',since,until,'fresh+out',f'{sT:,}','cacheread',f'{sC:,}')
for n in sorted(T,key=lambda n:-(T[n]+C[n])):
    print(f"{n:16s} files {len(S[n]):4d} fresh+out {T[n]:12,d} {T[n]/sT:6.1%} cacheread {C[n]:14,d} {C[n]/sC:6.1%} all {(T[n]+C[n])/(sT+sC):6.1%}")
json.dump({'T':T,'C':C},open(sys.argv[3],'w'))
# Codex
X=collections.Counter(); XC=collections.Counter(); XF=collections.Counter()
for f in glob.glob(os.path.expanduser('~/.codex/sessions/2026/*/*/*.jsonl')):
    day=f.split('/sessions/')[1][:10].replace('/','-')
    if not(since<=day<=until): continue
    cwd=None; last=None
    for l in open(f,encoding='utf-8',errors='replace'):
        if cwd is None and '"cwd"' in l[:6000]:
            m=re.search(r'"cwd":"([^"]+)"',l)
            if m: cwd=m[1]
        if '"total_token_usage"' in l:
            m=re.search(r'"total_token_usage":\{"input_tokens":(\d+),"cached_input_tokens":(\d+).*?"output_tokens":(\d+)',l)
            if m: last=tuple(map(int,m.groups()))
    if not last: continue
    n=(cwd or '?').replace('/home/willi/Research-workspace','').replace('/AGENTS/','').strip('/') or 'ROOT'
    X[n]+=last[0]-last[1]+last[2]; XC[n]+=last[1]; XF[n]+=1
print('CODEX fresh+out',f'{sum(X.values()):,}','cached',f'{sum(XC.values()):,}')
for n,v in X.most_common(40):
    print(f"{n:30s} rollouts {XF[n]:4d} fresh+out {v:12,d} {v/max(1,sum(X.values())):6.1%} cached {XC[n]:13,d}")
