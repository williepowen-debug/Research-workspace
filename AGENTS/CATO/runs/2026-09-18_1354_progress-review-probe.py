#!/usr/bin/env python3
"""Pinned historical reproductions, NOT repair acceptance tests. Offline; temp writes only."""
import contextlib, io, subprocess, sys, tempfile, types
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
REV='2cb5401fa'
sys.dont_write_bytecode=True
sys.path.insert(0,str(ROOT/'PROME/tools'))
def load(name,path):
    m=types.ModuleType(name); m.__file__=str(ROOT/path); sys.modules[name]=m
    exec(compile(subprocess.check_output(['git','show',REV+':'+path],cwd=ROOT),m.__file__,'exec'),m.__dict__)
    return m
h=load('pinned_guard','PROME/tools/hooks/commit_subject_guard.py')
for prefix in ['', 'echo ', 'command -v ', 'env printf %s ', 'timeout 1 echo ']:
    verdict=h.diagnose(prefix+'git commit -m "'+'x'*101+'"')[0]
    print('HOOK',repr(prefix),verdict)
    assert verdict==('allow' if prefix=='echo ' else 'block')
w=load('pinned_willq','PROME/tools/willq_view.py')
g=load('pinned_gate','PROME/tools/prome_gate.py')
d=load('pinned_deck','PROME/tools/decision_deck.py')
b=load('pinned_brief','PROME/tools/will_brief.py')
qhead='# fixture\n**Last reconciled:** 2026-09-18\n## OPEN\n| # | Item | Type | Needed by | Since | PROME rec | Notes |\n|---|---|---|---|---|---|---|\n'
with tempfile.TemporaryDirectory() as td:
    root=Path(td); (root/'PROME').mkdir();g.ROOT=b.ROOT=root
    text=qhead+'| 900 | Example | RULE | 2026-02-30 | 9/18 | rec | note |\n'
    (root/'PROME/WILL_QUEUE.md').write_text(text)
    print('INVALID DATE willq',w.parse_open(text)[0]['due'])
    print('INVALID DATE deck',d.parse_open(text)[0]['by'])
    print('INVALID DATE brief',b.parse_actions()[0][0]['due'])
    try: g.check_will_queue()
    except ValueError as e: print('INVALID DATE gate',type(e).__name__,str(e))
    else: raise AssertionError('expected historical exception')
    text=qhead+'| 900 | CLOSED old item | RULE | 2026-09-19 | 9/18 | rec | note |\n| 901 | Live | RULE | 2026-09-19 | 9/18 | rec | note |\n'
    (root/'PROME/WILL_QUEUE.md').write_text(text)
    print('CLOSED willq',[x['n'] for x in w.parse_open(text)])
    print('CLOSED deck',[x['n'] for x in d.parse_open(text)])
    print('CLOSED brief',[x['n'] for x in b.parse_actions()[0]])
    cot=load('pinned_cot','AGENTS/BRENT/scripts/cot_grade.py')
    row=['0']*15; row[0]=cot.MARKET; row[2]='2026-09-08';row[3]='067651';row[7]='1939911';row[13]='218960';row[14]='107230'
    cot.fetch_raw=lambda:','.join(row)+'\n'
    ledger=root/'ledger.tsv'
    for label,entry in [('healthy','2026-09-08\t107229\t218960\t1939911\n'),('corrupt','2026-09-08\tBAD\t218960\t1939911\n')]:
        ledger.write_text(entry); sys.argv=['fixture','--expect','2026-09-08','--ledger',str(ledger),'--no-record']
        out=io.StringIO()
        with contextlib.redirect_stdout(out):rc=cot.main()
        print('COT',label,'rc',rc,'warning', 'unparseable' in out.getvalue())
        assert rc==(4 if label=='healthy' else 0)
print('Historical reproductions complete. Do not treat this exit 0 as repair confirmation.')

# Later SAM diagnostic committed during this review; pin its table separately.
import csv, statistics, math
text=subprocess.check_output(['git','show','2f674c8c4:AGENTS/SAM/workbook/TRADE_BALANCE.tsv'],cwd=ROOT,text=True)
rows={}
for r in csv.DictReader(io.StringIO(text),delimiter='\t'): rows[r['Month']]=r
rows=[rows[k] for k in sorted(rows)]
levels=[float(r['Brent_avg_lag']) for r in rows]; landed=[float(r['Crude_USD_bbl']) for r in rows]
dev=[(u/b-1)*100 for u,b in zip(landed,levels)]
momentum=[levels[i]/levels[i-1]-1 for i in range(1,len(levels))]
print('SAM latest-row-per-month n',len(rows),'momentum correlation',statistics.correlation(dev[1:],momentum),'wedge-level correlation',statistics.correlation([u-b for u,b in zip(landed,levels)],levels))
for high in [True,False]:
    ix=[i for i,r in enumerate(rows) if (float(r['ME_Crude_Vol_kKL'])/float(r['Crude_Vol_kKL'])>=.85)==high]
    print('SAM highME',high,'n',len(ix),'mean%',statistics.mean(dev[i] for i in ix),'meanUSD',statistics.mean(landed[i]-levels[i] for i in ix))
print('Illustrative iid Fisher95 for reported r=.07 n16',[round(math.tanh(math.atanh(.07)+s*1.96/math.sqrt(13)),3) for s in [-1,1]])
