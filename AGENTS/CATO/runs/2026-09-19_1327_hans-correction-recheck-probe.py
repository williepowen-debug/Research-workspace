#!/usr/bin/env python3
"""Pinned repair review: isolated HANS writes, offline injected source payloads.

Assertions describe verified repairs AND reproduced residual defects, labelled below.
Ancillary repo files/history are read-through symlinks; this is not a hermetic suite.
"""
import contextlib
import csv
import io
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import tarfile
import tempfile
from unittest.mock import patch

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[3]
REV = '3cad378f06b76ab4d5db375ce8e76298f5948478'

with tempfile.TemporaryDirectory(prefix='cato-hans-recheck-') as tmp:
    repo = Path(tmp)
    data = subprocess.check_output(['git', 'archive', REV, 'AGENTS/HANS'], cwd=ROOT)
    with tarfile.open(fileobj=io.BytesIO(data)) as arc:
        arc.extractall(repo, filter='data')
    for child in ROOT.iterdir():
        if child.name != 'AGENTS':
            (repo / child.name).symlink_to(child, target_is_directory=child.is_dir())
    for child in (ROOT / 'AGENTS').iterdir():
        if child.name != 'HANS':
            (repo / 'AGENTS' / child.name).symlink_to(child, target_is_directory=child.is_dir())
    hans = repo / 'AGENTS/HANS'
    sys.path.insert(0, str(hans / 'scripts'))
    import doc_audit as da
    import fetch_eu as fe
    import closeout_check as cc
    print('HANS PIN', REV)
    print('Ancillary root HEAD', subprocess.check_output(
        ['git','rev-parse','HEAD'], cwd=ROOT, text=True).strip())
    suite = subprocess.run([sys.executable, '-B', str(hans/'scripts/test_hans.py')],
                           cwd=repo, env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1'),
                           capture_output=True, text=True)
    print('OWNER SUITE rc', suite.returncode)
    print('\n'.join((suite.stdout+suite.stderr).splitlines()[-6:]))
    assert suite.returncode == 0
    assert da.audit() == []
    print('CONTROL: unmodified doc_audit has zero blocking findings')

    # Only the UK series varies; all other sources are offline control values.
    def primary(boe_value=5.51, boe_day='18 Sep 2026', fill=69.06, mean=85.054):
        with patch.object(fe, 'ecb', lambda *a, **k: [('2026-09-18', 2.5)]), \
             patch.object(fe, 'agsi_eu', lambda: (('2026-09-17', fill, '0.22'), None)), \
             patch.object(fe, 'agsi_norm', lambda day: (mean,85.67,5,
                  [(2021,71.26),(2022,85.67),(2023,93.87),(2024,93.38),(2025,81.09)])), \
             patch.object(fe, 'boe', lambda code: (boe_day,boe_value)), \
             contextlib.redirect_stdout(io.StringIO()) as output:
            result=fe.main()
        return result, output.getvalue()
    for v in (5.49,5.51):
        result, _=primary(v)
        assert 'HANS-T-06' not in result['breached']
        assert bool(result['failures']) == (v > 5.5)
    print('REPAIRED: par above/below 5.50 never creates canonical T-06 breach; above requests attention')
    result,_=primary(5.24,'07 Sep 2026')
    assert not result['failures']
    print('OPEN BoE: original 12-day-old observation still yields failures=[]')
    for name, payload, rejected in [
        ('wrong series','DATE,IUDBEDR\n18 Sep 2026,5.51\n',True),
        ('invalid date','DATE,IUDMNPY\nnot-a-date,5.51\n',True),
        ('NaN','DATE,IUDMNPY\n18 Sep 2026,NaN\n',True),
        ('infinity','DATE,IUDMNPY\n18 Sep 2026,inf\n',True),
        ('future date','DATE,IUDMNPY\n01 Jan 2099,5.51\n',False),
        ('unsorted dates','DATE,IUDMNPY\n18 Sep 2026,5.51\n07 Sep 2026,5.24\n',False),
    ]:
        with patch.object(fe.urllib.request,'urlopen',lambda *a,**k: io.BytesIO(payload.encode())):
            got=fe.boe('IUDMNPY')
        assert (got is None) == rejected
        print('REPAIRED' if rejected else 'OPEN', 'BoE',name,repr(got))

    values={2021:71.26,2022:85.67,2023:93.87,2024:93.38,2025:81.09}
    def norm(omit=(), wrong_date=False, value=None):
        def reply(req,**kw):
            day=req.full_url.split('date=')[1]
            y=int(day[:4])
            records=[] if y in omit else [{'gasDayStart':'2020-01-01' if wrong_date else day,
                                          'full':values[y] if value is None else value}]
            return io.BytesIO(json.dumps({'data':records}).encode())
        with patch.object(fe,'_agsi_key',lambda:'offline-fixture'), \
             patch.object(fe.urllib.request,'urlopen',reply):
            return fe.agsi_norm('2026-09-17')
    assert abs(norm()[0]-85.054)<1e-9
    assert norm(omit=(2023,))[0] is None
    print('REPAIRED: complete 5-year mean 85.054; original 4-year fixture now refuses a norm')
    assert norm(wrong_date=True)[2] == 5
    assert math.isnan(norm(value='NaN')[0])
    assert norm(value='101')[0] == 101
    print('OPEN storage: wrong observation dates, NaN, and 101% fill all accepted as a full 5-year norm')
    for name,fill,mean in [('current fill',math.nan,85.054),('historical norm',69.06,math.nan)]:
        result,out=primary(5.24,fill=fill,mean=mean)
        assert not result['failures'] and 'HANS-T-08' not in result['breached']
        assert '🟢 GAP TO 5-YR NORM +nanpp' in out
        print('OPEN storage:',name,'NaN => green gap, failures=[], no T-08 breach')
    with patch.object(fe,'_agsi_key',lambda:'offline-fixture'), \
         patch.object(fe.urllib.request,'urlopen',lambda *a,**k: io.BytesIO(
             b'{"data":[{"gasDayStart":"2026-09-17","full":"NaN"}]}')):
        current,err=fe.agsi_eu()
    assert err is None and math.isnan(current[1])
    print('OPEN storage: actual current-feed parser accepts NaN without error')

    # Reproduce real interpreter return codes, rather than assigning invented semantics.
    errors = [
        ('traceback',cc.run([sys.executable,'-c','raise RuntimeError("fixture crash")'],repo)),
        ('missing script',cc.run([sys.executable,str(repo/'nonexistent-child.py')],repo)),
        ('real consumer invalid option',cc.run([sys.executable,str(ROOT/'scripts/consumer_check.py'),
                                              '--cato-nonexistent-option'],ROOT)),
        ('explicit rc3',(3,'fixture rc3')),
        ('signal',(-15,'fixture SIGTERM')),
    ]
    for name,(child_rc,child_out) in errors:
        def fake_run(cmd,cwd):
            selected=any(str(x).endswith(('consumer_check.py','ledger_staleness.py')) for x in cmd)
            return (child_rc,child_out) if selected else (0,'control OK')
        with patch.object(cc,'run',fake_run),contextlib.redirect_stdout(io.StringIO()) as output:
            rc=cc.main()
        assert rc == (0 if child_rc in (1,2) else 1)
        print('OPEN' if rc==0 else 'REPAIRED','runner',name,'child',child_rc,'runner',rc,
              next(x.strip() for x in output.getvalue().splitlines() if 'MECHANICAL:' in x))

    status=hans/'STATUS.md'
    orig=status.read_text()
    def prose(line):
        try:
            status.write_text(orig+'\n'+line+'\n')
            findings,notes=da._audit_full()
            return [(c,m) for c,m in findings+notes if c.startswith('C9-') and 'SKIP' not in c]
        finally:
            status.write_text(orig)
    cases=[
        ('Euro-area HICP is currently 3.3%.',True),
        ('EU storage gap is currently −19.7pp.',True),
        ('EU storage gap is -19.7pp → this remains a winter risk.',True),
        ('EU storage gap is -19.7pp; '+('other text. '*15)+'policy was unchanged.',True),
        ('EU storage gap is -19.7pp; policy was unchanged today.',False),
        ('The current BoE Bank Rate is 4.50%.',False),
        ('EU storage gap is -19.7 percentage points.',False),
    ]
    for line,detect in cases:
        hits=prose(line)
        # Filter out the unchanged base-file short-number notes.
        hits=[(c,m) for c,m in hits if f'STATUS.md:{len(orig.splitlines())+2} ' in m]
        assert bool(hits)==detect,(line,hits)
        print('REPAIRED' if detect else 'OPEN','C9',repr(line[:95]),[c for c,_ in hits])

    ml=hans/'workbook/ML.tsv'
    saved=ml.read_text()
    for ident,detect in [('ML-HANS-001',True),('ML-HANS-004',False)]:
        row=next(x for x in saved.splitlines() if x.startswith(ident+'\t'))
        try:
            ml.write_text(saved.rstrip('\n')+'\n'+row+'\n')
            findings,notes=da._audit_full()
            caught=any(c=='C12-ID-DUPLICATE' for c,_ in findings)
            assert caught==detect
            print('REPAIRED' if caught else 'OPEN','C12 append another',ident,
                  [m for c,m in notes if c=='C12-LEGACY-DUP'])
        finally:
            ml.write_text(saved)
    pred=hans/'workbook/PREDICTIONS.tsv'
    saved=pred.read_text()
    try:
        pred.write_text(saved.rstrip('\n')+'\n'+saved.splitlines()[-1]+'\n')
        assert not any(c=='C12-ID-DUPLICATE' for c,_ in da.audit())
        print('OPEN C12: original duplicate prediction-ID fixture still undetected')
    finally:
        pred.write_text(saved)
    book=list(csv.DictReader(io.StringIO(saved),delimiter='\t'))
    n=next(r['Notes'] for r in book if r['Pred_ID']=='HNS-07')
    assert 'WITHDRAWN' in n[n.index('(d)'):n.index('ARITHMETIC KILL')]
    assert 'THERE IS NO EARLY' in n
    print('REPAIRED HNS-07: canonical rule d is withdrawn before its quoted instruction')
    assert 'NO material rise in cost-of-risk' in orig
    assert 'see §SESSION 4' in orig
    assert '2026-10-01 · 10-15 · 10-25' in orig
    print('REPAIRED HNS-09 outcome restored; HNS-07 dates in docket. OPEN stale section pointer persists')
    print('DONE: all assertions matched; no shared HANS files edited')
