import json,glob,os,sys,collections,datetime
root=os.path.expanduser('~/.claude/projects')
since=sys.argv[1]; until=sys.argv[2]
tot=collections.Counter(); out=collections.Counter(); sess=collections.defaultdict(set); msgs=collections.Counter(); seen=set()
for d in sorted(os.listdir(root)):
    if not d.startswith('-home-willi-Research-workspace'): continue
    name=d.replace('-home-willi-Research-workspace','').replace('-AGENTS-','').strip('-') or 'ROOT'
    for f in glob.glob(os.path.join(root,d,'**','*.jsonl'),recursive=True):
        try:
            if os.path.getmtime(f)<datetime.datetime.fromisoformat(since).timestamp(): continue
            for line in open(f,encoding='utf-8',errors='replace'):
                if '"usage"' not in line: continue
                try: o=json.loads(line)
                except: continue
                ts=o.get('timestamp','')
                if not(since<=ts[:10]<=until): continue
                m=o.get('message') or {}
                u=m.get('usage')
                if not isinstance(u,dict): continue
                k=m.get('id') or o.get('uuid')
                if k in seen: continue
                seen.add(k)
                i=u.get('input_tokens',0)+u.get('cache_creation_input_tokens',0)
                c=u.get('cache_read_input_tokens',0)
                x=u.get('output_tokens',0)
                tot[name]+=i+x; out[name]+=x; msgs[name]+=1; sess[name].add(o.get('sessionId'))
                tot['_cacheread_'+name]+=c
        except Exception as e: pass
names=[n for n in tot if not n.startswith('_cacheread_')]
T=sum(tot[n] for n in names); C=sum(tot['_cacheread_'+n] for n in names)
print('window',since,until,'msgs',sum(msgs.values()),'fresh+out',T,'cacheread',C)
for n in sorted(names,key=lambda n:-(tot[n]+tot['_cacheread_'+n])):
    print(f"{n:10s} sess {len(sess[n]):4d} msgs {msgs[n]:6d} fresh+out {tot[n]:12,d} {tot[n]/T:6.1%}  cacheread {tot['_cacheread_'+n]:14,d} {tot['_cacheread_'+n]/C:6.1%}")
