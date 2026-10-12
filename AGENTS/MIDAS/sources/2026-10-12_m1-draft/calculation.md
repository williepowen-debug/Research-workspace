# One-off historical calculation evidence

Static record of the single calculation, run from /tmp after design commit ad1c2f443. This is supporting evidence, not an installed tool, monitor or pipeline. Standard library only.

```python
from pathlib import Path
import csv, json, math, hashlib, datetime

desk = Path('/home/willi/Research-workspace/AGENTS/MIDAS')
src = desk / 'sources/2026-10-12_review'
out = desk / 'sources/2026-10-12_m1-draft'
out.mkdir(exist_ok=True)
draft = desk / 'analysis/2026-10-12_M1-successor-DRAFT.md'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
manifest = {n: sha(src/n) for n in ['GLD.csv','DFII10.json','GLD_DFII10_pairs.csv','summary.json']}
draft_sha = sha(draft)
with (src/'GLD.csv').open() as f:
    gr = list(csv.DictReader(f))
assert len({r[''] for r in gr}) == len(gr)
gr = sorted((r for r in gr if r[''] <= '2026-10-09'), key=lambda r:r[''])
yr = json.loads((src/'DFII10.json').read_text())
assert len({r['date'] for r in yr}) == len(yr)
yr = sorted((r for r in yr if r['date'] <= '2026-10-09' and r['value'] != '.'), key=lambda r:r['date'])
g = {r['']:float(r['Close']) for r in gr}
y = {r['date']:float(r['value']) for r in yr}
gp = {b['']:a[''] for a,b in zip(gr,gr[1:])}
yp = {b['date']:a['date'] for a,b in zip(yr,yr[1:])}
actions = [r for r in gr if any(float(r[k]) != 0 for k in ['Dividends','Stock Splits','Capital Gains'])]
assert not actions, 'raw-close corporate-action discontinuity'
pairs = []
for d in sorted(gp.keys() & yp.keys()):
    ret = 100*(g[d]/g[gp[d]]-1)
    x = round(100*(y[d]-y[yp[d]]),8)
    assert math.isfinite(ret) and math.isfinite(x)
    pairs.append(dict(date=d,ret=ret,dy_bp=x,gld_prior_date=gp[d],dfii10_prior_date=yp[d],
                      same_start_date=gp[d]==yp[d],gld_close=g[d],gld_prior_close=g[gp[d]],
                      dfii10=y[d],dfii10_prior=y[yp[d]]))
with (src/'GLD_DFII10_pairs.csv').open() as f:
    saved = list(csv.DictReader(f))
assert [r['date'] for r in pairs] == [r[''] for r in saved]
ret_err = max(abs(a['ret']-float(b['ret'])) for a,b in zip(pairs,saved))
x_err = max(abs(a['dy_bp']-float(b['dy_bp'])) for a,b in zip(pairs,saved))
assert ret_err < 1e-12 and x_err == 0

def beta(rows):
    xm = math.fsum(r['dy_bp'] for r in rows)/len(rows)
    rm = math.fsum(r['ret'] for r in rows)/len(rows)
    den = math.fsum((r['dy_bp']-xm)**2 for r in rows)
    if den == 0: return None
    return math.fsum((r['dy_bp']-xm)*(r['ret']-rm) for r in rows)/den

window, horizon, flip = 120, 20, -0.080000
roll = {}
rolling = []
for i in range(window-1,len(pairs)):
    b = beta(pairs[i-window+1:i+1])
    assert b is not None
    roll[i] = round(b,6)
    rolling.append(dict(pair_index=i,date=pairs[i]['date'],start=pairs[i-window+1]['date'],
                        n=window,beta_unrounded=b,beta_binding=roll[i],flip_met=roll[i]>=flip))
anchors = []
for i in range(window-1,len(pairs)-horizon):
    eligible = roll[i] < flip
    anchors.append(dict(pair_index=i,date=pairs[i]['date'],endpoint_index=i+horizon,
                        endpoint=pairs[i+horizon]['date'],start_beta=roll[i],
                        endpoint_beta=roll[i+horizon],eligible=eligible,
                        outcome='B' if roll[i+horizon]>=flip else 'A'))

def count(rows):
    answer = {}
    for state, predicate in [('starting_below',lambda r:r['eligible']),('starting_at_or_above',lambda r:not r['eligible'])]:
        a = [r for r in rows if predicate(r)]
        hits = sum(r['outcome']=='B' for r in a)
        answer[state] = dict(n=len(a),A=len(a)-hits,B=hits,B_frequency=hits/len(a) if a else None)
    return answer

by_index = {r['pair_index']:r for r in anchors}
episodes, support_sets = [], []
for i in range(window-1,len(pairs)-horizon,window+horizon+1):
    block = pairs[i-window+1:i+horizon+1]
    gs = {r[k] for r in block for k in ['date','gld_prior_date']}
    ys = {r[k] for r in block for k in ['date','dfii10_prior_date']}
    for old_g,old_y in support_sets:
        assert not (gs & old_g) and not (ys & old_y), 'shared raw input support'
    support_sets.append((gs,ys))
    episodes.append(dict(**by_index[i],episode=len(episodes)+1,input_pairs=len(block),
                         first_pair=block[0]['date'],last_pair=block[-1]['date'],
                         gld_support_start=min(gs),gld_support_end=max(gs),gld_levels=len(gs),
                         dfii10_support_start=min(ys),dfii10_support_end=max(ys),dfii10_levels=len(ys)))

# Construction checks: these are synthetic branch/tie reachability, not more fitted alternatives.
construction = {}
for name, slope, expected in [('below',-.10,'A'),('tie',-.08,'B'),('above',-.05,'B')]:
    b = round(beta([dict(dy_bp=float(i),ret=slope*i) for i in range(120)]),6)
    result = 'B' if b>=flip else 'A'
    assert result == expected
    construction[name] = dict(beta=b,outcome=result,pass_check=True)
assert beta([dict(dy_bp=1.,ret=float(i)) for i in range(120)]) is None
construction['zero_variance'] = 'STUCK'

def write_csv(name,rows):
    with (out/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

write_csv('pair_audit.csv',pairs)
write_csv('rolling_beta.csv',rolling)
write_csv('anchors.csv',anchors)
write_csv('disjoint_episodes.csv',episodes)
summary = dict(calculated_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    design_commit='ad1c2f443',design_sha256_before_calculation=draft_sha,
    input_sha256=manifest,input_capture=json.loads((src/'summary.json').read_text())['retrieved_at'],
    reference_vintage='latest revised as saved October 12; not historic real-time vintages',
    parameters=dict(window=window,horizon=horizon,flip=flip,beta_round_decimals=6,
                    dy_bp_round_decimals=8,disjoint_grid='119 + 141k, zero-based'),
    pairs=dict(n=len(pairs),first=pairs[0]['date'],last=pairs[-1]['date'],
               different_interval_starts=sum(not r['same_start_date'] for r in pairs),
               corporate_actions=len(actions),return_reconstruction_max_error=ret_err,
               yield_reconstruction_max_error=x_err),
    rolling_endpoints=len(rolling),overlapping_anchor_count=len(anchors),
    overlapping_counts=count(anchors),disjoint_episode_count=len(episodes),
    disjoint_counts=count(episodes),raw_level_support_disjoint=True,
    statistically_independent_macro_episodes='UNKNOWN; disjoint input support is not independence',
    forward_probability='UNASSIGNED; short revised history and few disjoint episodes',
    construction_checks=construction)
(out/'reference.json').write_text(json.dumps(summary,indent=2)+'\n')
(out/'calculation.md').write_text('# One-off historical calculation evidence\n\n'
    'Static record of the single calculation, run from /tmp after design commit ad1c2f443. '
    'This is supporting evidence, not an installed tool, monitor or pipeline. Standard library only.\n\n'
    '```python\n'+Path(__file__).read_text()+'\n```\n')
print(json.dumps(summary,indent=2))
print('DISJOINT EPISODES')
for r in episodes: print(json.dumps(r))

```
