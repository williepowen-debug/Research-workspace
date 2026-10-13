# Expanded reference — one-off static calculation evidence

Design041cfdfb5 precedes the calculation.

```python
from pathlib import Path
import csv,json,math,hashlib,datetime,subprocess

desk=Path('/home/willi/Research-workspace/AGENTS/MIDAS')
out=desk/'sources/2026-10-12_m1-expanded'
with (out/'GLD.csv').open() as f:
    reader=csv.DictReader(f);date_column=reader.fieldnames[0]
    grows=[dict(r,**{'':r[date_column]}) for r in reader]
assert len({r[''] for r in grows})==len(grows)
grows=sorted(grows,key=lambda r:r[''])
assert not [r for r in grows if any(float(r.get(k,0))!=0 for k in ['Dividends','Stock Splits','Capital Gains'])]
g={r['']:float(r['Close']) for r in grows}
gp={b['']:a[''] for a,b in zip(grows,grows[1:])}
latest=json.loads((out/'DFII10_latest.json').read_text())
assert not any('error' in r for r in latest)
y={r['date']:float(r['value']) for r in latest if r['value']!='.'}
ydates=sorted(y)
yp={b:a for a,b in zip(ydates,ydates[1:])}
pairs=[dict(date=d,ret=100*(g[d]/g[gp[d]]-1),dy_bp=round(100*(y[d]-y[yp[d]]),8),
            gld_prior_date=gp[d],dfii10_prior_date=yp[d])
       for d in sorted(gp.keys()&yp.keys()) if d<='2026-10-08']
fp={}
for path in sorted(out.glob('DFII10_first_20*.json')):
    data=json.loads(path.read_text())['response']
    assert not data.get('error'),(path,data.get('error'))
    for r in data.get('observations',[]):
        if r['value']!='.':
            assert r['date'] not in fp
            fp[r['date']]=dict(value=float(r['value']),first_published=r['realtime_start'])
used_dates={d for r in pairs for d in [r['date'],r['dfii10_prior_date']]}
missing=sorted(d for d in used_dates if d not in fp)
revisions=[dict(date=d,latest=y[d],first=fp[d]['value'],first_published=fp[d]['first_published'])
           for d in sorted(used_dates&fp.keys()) if y[d]!=fp[d]['value']]
old=list(csv.DictReader((desk/'sources/2026-10-12_review/GLD_DFII10_pairs.csv').open()))
new={r['date']:r for r in pairs}
old_same_dates=all(r[''] in new for r in old)
max_old_ret=max(abs(float(r['ret'])-new[r['']]['ret']) for r in old if r[''] in new)
max_old_dy=max(abs(float(r['dy_bp'])-new[r['']]['dy_bp']) for r in old if r[''] in new)
assert old_same_dates and max_old_ret<1e-12 and max_old_dy==0

def beta(rows):
    xm=math.fsum(r['dy_bp'] for r in rows)/len(rows)
    rm=math.fsum(r['ret'] for r in rows)/len(rows)
    den=math.fsum((r['dy_bp']-xm)**2 for r in rows)
    assert den>0
    return round(math.fsum((r['dy_bp']-xm)*(r['ret']-rm) for r in rows)/den,6)

roll={i:beta(pairs[i-119:i+1]) for i in range(119,len(pairs))}
anchors=[dict(index=i,date=pairs[i]['date'],endpoint=pairs[i+20]['date'],start_beta=roll[i],
              endpoint_beta=roll[i+20],eligible=roll[i]<-.08,outcome='B' if roll[i+20]>=-.08 else 'A')
         for i in range(119,len(pairs)-20)]
phase=next(i for i,r in enumerate(pairs) if r['date']=='2024-01-03')+119
episodes=[];supports=[]
for r in anchors:
    i=r['index']
    if (i-phase)%141:continue
    block=pairs[i-119:i+21]
    gs={d for b in block for d in [b['date'],b['gld_prior_date']]}
    ys={d for b in block for d in [b['date'],b['dfii10_prior_date']]}
    for a,b in supports:assert not(gs&a) and not(ys&b)
    supports.append((gs,ys))
    episodes.append(dict(**r,support_start=min(gs|ys),support_end=max(gs|ys),raw_support_disjoint=True))
assert [r['date'] for r in episodes if r['date']>='2024-01-01']==['2024-06-25','2025-01-21','2025-08-13','2026-03-10']

def counts(rows):
    answer={}
    for name,eligible in [('below_flip',True),('at_or_above',False)]:
        a=[r for r in rows if r['eligible']==eligible]
        hits=sum(r['outcome']=='B' for r in a)
        answer[name]=dict(n=len(a),A=len(a)-hits,B=hits,B_frequency=hits/len(a) if a else None)
    return answer

def write(name,rows):
    with (out/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
write('pairs.csv',pairs);write('anchors.csv',anchors);write('disjoint_episodes.csv',episodes)
summary=dict(calculated_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    design_commit='041cfdfb5',pairs=len(pairs),first=pairs[0]['date'],last=pairs[-1]['date'],
    parameters=dict(window=120,horizon=20,flip=-.08,grid='phase anchored on old2024 first pair+119;141-step both directions',phase_index=phase),
    old_690_pairs_reconcile=True,max_old_ret_error=max_old_ret,max_old_dy_error=max_old_dy,
    overlapping_anchors=len(anchors),overlapping_counts=counts(anchors),
    disjoint_episodes=len(episodes),disjoint_counts=counts(episodes),original_four_episodes_preserved=True,
    alfred_used_level_dates=len(used_dates),alfred_missing=missing,latest_vs_first_differences=revisions,
    vintage_limit='First-published per-observation comparison is not a set of historic latest-carried 120-row endpoint snapshots; GLD is a single later Yahoo capture.',
    forward_probability='UNASSIGNED pending regime/endpoint-vintage review; disjoint support does not establish independent macro episodes',
    input_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in out.iterdir() if p.suffix=='.json' or p.name=='GLD.csv'})
(out/'reference.json').write_text(json.dumps(summary,indent=2)+'\n')
(out/'calculation.md').write_text('# Expanded reference — one-off static calculation evidence\n\nDesign041cfdfb5 precedes the calculation.\n\n```python\n'+Path(__file__).read_text()+'\n```\n')
print(json.dumps({k:v for k,v in summary.items() if k not in ['input_sha256','latest_vs_first_differences']},indent=2))
print('First/latest changed observations:',len(revisions))
print('Eligible disjoint episodes:')
for r in episodes:
    if r['eligible']:print(json.dumps(r))

```
