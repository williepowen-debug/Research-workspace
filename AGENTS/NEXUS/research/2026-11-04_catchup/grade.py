"""Reproduce this dated catch-up from saved inputs; no network or owner writes."""
import csv
import json
from decimal import Decimal
from pathlib import Path

P = Path(__file__).resolve().parent
def units(value):
    number = Decimal(str(value)) * 100
    assert number == number.to_integral_value(), value
    return int(number)
def series(sid, prefix='fp'):
    data = json.loads((P/'fred'/f'{prefix}_{sid}.json').read_text())
    assert not data.get('error') and not data.get('short'), data
    return {r['date']: units(r['value']) for r in data.get('rows', data.get('observations', [])) if r['value'] != '.'}
ids = dict(HY='BAMLH0A0HYM2', CCC='BAMLH0A3HYC', BB='BAMLH0A1HYBB', B='BAMLH0A2HYB', IG='BAMLC0A0CM')
data = {k:series(v) for k,v in ids.items()}
dates = sorted(set(data['HY']) & set(data['CCC']))
cells=[]; previous=None
for day in dates:
    current={k:v[day] for k,v in data.items() if day in v}
    carry = previous is not None and all(previous.get(k)==v for k,v in current.items())
    if day >= '2026-10-19': cells.append(dict(date=day, **current, carry=carry))
    previous=current
anchor=next(c for c in cells if c['date']=='2026-10-19')
assert (anchor['HY'],anchor['CCC'],anchor['IG'])==(329,1310,87)
def credit_grade(rows, a):
    up=down=0; out=[]; fire=None
    for c in rows:
        if c['date']<=a['date'] or c['carry']:continue
        n=len(out)+1
        if n>15:break
        up=up+1 if c['HY']>=a['HY']+10 else 0
        down=down+1 if c['HY']<=a['HY']-10 else 0
        if not fire and (up>=3 or (down>=3 and c['CCC']<=a['CCC'])):
            fire=dict(date=c['date'],n=n,branch='UP' if up>=3 else 'DOWN',IG_delta=c['IG']-a['IG'])
        out.append(dict(c,n=n,up=up,down=down))
    return dict(cells=out,fire=fire)
l16=credit_grade(cells,anchor)
# First-read ledger is the authoritative prior vintage, not a re-fetch substitution.
ledger=list(csv.DictReader((P.parents[1]/'analysis/WQ342_grading_log.tsv').open(),delimiter='\t'))
prior={r['obs_date']:r for r in ledger if r['event'] in ['ANCHOR_FIRST_READ','CELL'] and r['window']=='1'}
prior_mismatches=[]
for c in cells:
    if c['date'] in prior:
        for k in ids:
            saved=prior[c['date']].get(k+'_bp')
            if saved and int(saved)!=c[k]:prior_mismatches.append([c['date'],k,saved,c[k]])
assert not prior_mismatches, prior_mismatches
latest={k:series(ids[k],'latest') for k in ['HY','CCC']}
vintage_diffs=[]; revised=[]
for c in cells:
    r=dict(c)
    for k in latest:
        assert c['date'] in latest[k]
        r[k]=latest[k][c['date']]
        if r[k]!=c[k]:vintage_diffs.append([c['date'],k,c[k],r[k]])
    revised.append(r)
assert not vintage_diffs, vintage_diffs
latest_grade=credit_grade(revised,next(c for c in revised if c['date']=='2026-10-19'))
assert latest_grade['fire']==l16['fire']
def runs(rows, low, high, count=2):
    u=d=0; fire=None; out=[]
    for day,v in rows:
        u=u+1 if v>=high else 0;d=d+1 if v<=low else 0
        if fire is None and (u>=count or d>=count):fire=dict(date=day,branch='UP' if u>=count else 'DOWN')
        out.append(dict(date=day,value=v,up=u,down=d))
    return dict(cells=out,fire=fire)
m07=runs(sorted((d,v) for d,v in data['IG'].items() if '2026-10-08'<d<='2026-11-05'),71,93)
# Generic high edge means DOWN for the counterevidence letter.
if m07['fire']:m07['fire']['letter_branch']='DOWN' if m07['fire']['branch']=='UP' else 'UP'
dfii=series('DFII10'); real=[]
for r in csv.DictReader((P/'real.csv').open()):
    m,d,y=r['Date'].split('/');day=f'{y}-{int(m):02}-{int(d):02}'
    if '2026-10-16'<day:real.append((day,dfii.get(day,units(r['10 YR']))))
l13=runs(sorted(real)[:15],264,284,5)
l13['basis']='FRED first-published governs overlapping dates; Treasury 10YR permitted early copy for later dates'
l13['fred_latest']=max(dfii)
l13['treasury_only']=[d for d,v in real if d not in dfii]
m01=runs(sorted((d,v) for d,v in data['HY'].items() if '2026-10-08'<d<='2026-11-05'),280,350)
claims=json.loads((P/'fred/fp_ICSA.json').read_text())['rows']
m01['claims_first_print']=claims[:3]
assert all(int(r['value'])<230000 for r in claims[:3])
assert m01['fire'] is None
kre=json.loads((P/'KRE_VENDOR.json').read_text())['KRE']['history']
# Retrieval is before November4 close. Today's evolving bar is never a settled cell.
m05=runs([(r['date'],units(r['close'])) for r in kre if '2026-10-08'<r['date']<='2026-11-03'],6402,7516)
vix=series('VIXCLS');m04=runs(sorted((d,v) for d,v in vix.items() if '2026-10-23'<d<='2026-11-20'),1645,2245)
u=d=0; fire=None; out=[]
for c in cells:
    if c['date']<='2026-10-23' or c['carry']:continue
    u=u+1 if c['B']>=358 and c['CCC']>=1416 else 0
    d=d+1 if c['B']<=328 and c['CCC']<=1296 else 0
    if fire is None and (u>=2 or d>=2):fire=dict(date=c['date'],branch='UP' if u>=2 else 'DOWN')
    out.append(dict(date=c['date'],B=c['B'],CCC=c['CCC'],up=u,down=d))
sofr=json.loads((P/'nyfed_sofr_history.json').read_text())['refRates'];iorb=series('IORB')
funding=[dict(date=r['effectiveDate'],SOFR=units(r['percentRate']),IORB=iorb[r['effectiveDate']],gap_bp=units(r['percentRate'])-iorb[r['effectiveDate']],tail_gap_bp=units(r['percentPercentile99'])-iorb[r['effectiveDate']]) for r in sofr if r['effectiveDate'] in ['2026-10-08','2026-10-30','2026-11-02','2026-11-03']]
assert l16['fire']==dict(date='2026-11-03',n=11,branch='UP',IG_delta=6)
assert m07['fire']['date']=='2026-11-02' and m07['fire']['letter_branch']=='DOWN'
assert l13['fire'] is None and len(l13['cells'])==12 and l13['cells'][-1]['down']==0
assert not m05['fire'] and not m04['fire'] and fire is None
assert runs([('a',93),('b',93)],71,93)['fire']['date']=='b'
assert runs([('a',93),('b',92)],71,93)['fire'] is None
result=dict(L16=l16,L16_latest_vintage=latest_grade['fire'],vintage_diffs=vintage_diffs,prior_first_read_mismatches=prior_mismatches,L13=l13,M01=m01,M05=m05,M07=m07,M04b=m04,M08b=dict(cells=out,fire=fire),funding=funding,split_before=[20,47,33],split_after=[26,41,33],M07_conf_before=79,M07_historical_grade=75)
(P/'GRADES.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['L16_latest_vintage','vintage_diffs','funding','split_after']},indent=2))
print('L13 latest',l13['cells'][-1], 'M07',m07['fire'],'M05 last',m05['cells'][-1])
