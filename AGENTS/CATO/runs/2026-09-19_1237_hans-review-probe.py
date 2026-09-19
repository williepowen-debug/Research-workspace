#!/usr/bin/env python3
"""Pinned offline counterexamples; mutates only a temporary HANS snapshot.

PASS reproduces reviewed behavior, not repaired behavior. Ancillary repository
paths are read-through symlinks for the owner's path/history checks.
"""
import contextlib
import importlib
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
REV = 'd87c26f3bdff4ef194080a03e4e8de81b8089a41'

with tempfile.TemporaryDirectory(prefix='cato-hans-review-') as temp:
    repo = Path(temp)
    blob = subprocess.check_output(['git', 'archive', REV, 'AGENTS/HANS'], cwd=ROOT)
    with tarfile.open(fileobj=io.BytesIO(blob)) as arc:
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
    print('Pinned HANS revision:', REV)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    tests = subprocess.run([sys.executable, '-B', str(hans / 'scripts/test_hans.py')],
                           cwd=repo, env=env, text=True, capture_output=True)
    print('OWNER SUITE rc=', tests.returncode)
    print('\n'.join((tests.stdout + tests.stderr).splitlines()[-8:]))
    assert tests.returncode == 0
    assert da.audit() == []
    print('CONTROL: owner suite and unmodified doc audit pass in isolated copy')

    status = hans / 'STATUS.md'
    original = status.read_text()
    def prose(line):
        try:
            status.write_text(original + '\n' + line + '\n')
            return [x for x in da.audit() if x[0].startswith('C9-')]
        finally:
            status.write_text(original)

    assert prose('EU storage gap to the 5-yr norm stands at -19.7pp.')
    print('CONTROL C9 catches plain retired storage level')
    for line in [
        'Euro-area HICP is currently 3.3%.',
        'The current BoE Bank Rate is 4.50%.',
        'EU storage gap is currently −19.7pp.',
        'EU storage gap is -19.7pp; policy was unchanged today.',
        'EU storage gap is -19.7pp → this remains a winter risk.',
    ]:
        assert prose(line) == []
        print('C9 MISS:', line)
    stale = [line for line in original.splitlines()
             if 'storage −19.7pp' in line]
    print('ACTUAL STALE PROSE:', stale)
    assert stale

    ml = hans / 'workbook/ML.tsv'
    orig_ml = ml.read_text()
    lines = orig_ml.splitlines()
    ids = [line.split('\t')[0] for line in lines[1:]]
    from collections import Counter
    counts = Counter(ids)
    row = next(line for line in lines[1:] if counts[line.split('\t')[0]] == 1
               and line.split('\t')[0].split('-')[-1].isdigit()
               and int(line.split('\t')[0].split('-')[-1]) < 400)
    try:
        ml.write_text(orig_ml.rstrip('\n') + '\n' + row + '\n')
        findings, info = da._audit_full()
        assert not [x for x in findings if x[0] == 'C12-ID-DUPLICATE']
        print('C12 MISS: newly duplicated previously unique old ID', row.split('\t')[0])
        print([x for x in info if x[0] == 'C12-LEGACY-DUP'])
    finally:
        ml.write_text(orig_ml)

    pred = hans / 'workbook/PREDICTIONS.tsv'
    orig_pred = pred.read_text()
    try:
        pred.write_text(orig_pred.rstrip('\n') + '\n' + orig_pred.splitlines()[-1] + '\n')
        assert not [x for x in da.audit() if x[0] == 'C12-ID-DUPLICATE']
        print('C12 PERIMETER: duplicate prediction ID also passes (PREDICTIONS not scanned)')
    finally:
        pred.write_text(orig_pred)

    try:
        status.write_text(original + '\n## Morning work\nI added a feed today.\n')
        assert not [x for x in da.audit() if x[0].startswith('C14-')]
        print('C14 LIMIT: session narrative under Morning work is not detected')
    finally:
        status.write_text(original)

    # All external sources mocked: isolate BoE basis, parser and freshness behavior.
    def primary(boe_value=5.51, boe_day='18 Sep 2026'):
        def ecb(series, n=1):
            return [('2026-09-18', 2.5)]
        with patch.object(fe, 'ecb', ecb), \
             patch.object(fe, 'agsi_eu', lambda: (('2026-09-17', 69.06, '0.22'), None)), \
             patch.object(fe, 'agsi_norm', lambda day: (85.054, 85.67, 5,
                 [(2021,71.26),(2022,85.67),(2023,93.87),(2024,93.38),(2025,81.09)])), \
             patch.object(fe, 'boe', lambda code: (boe_day, boe_value)), \
             contextlib.redirect_stdout(io.StringIO()):
            return fe.main()
    result = primary()
    assert 'HANS-T-06' in result['breached']
    print('BOE BASIS: par=5.51 generates benchmark T-06 breach; benchmark input never read')
    result = primary(5.24, '07 Sep 2026')
    assert result['failures'] == []
    print('BOE FRESHNESS: 12-day-old observation accepted with failures=[] (printed age only)')
    for payload in ['DATE,IUDBEDR\n18 Sep 2026,5.51\n',
                    'DATE,IUDMNPY\nnot-a-date,5.51\n',
                    'DATE,IUDMNPY\n18 Sep 2026,NaN\n']:
        with patch.object(fe.urllib.request, 'urlopen', lambda *a, **k: io.BytesIO(payload.encode())):
            got = fe.boe('IUDMNPY')
        assert got is not None
        print('BOE INVALID ACCEPTED:', repr(payload), '->', got)

    values = {2021:71.26,2022:85.67,2023:93.87,2024:93.38,2025:81.09}
    def norm(omit=(), wrong_date=False, nonfinite=False):
        def fake(req, **kw):
            day = req.full_url.split('date=')[1]
            yr = int(day[:4])
            rows = [] if yr in omit else [{'gasDayStart':'2020-01-01' if wrong_date else day,
                         'full':'NaN' if nonfinite else values[yr]}]
            return io.BytesIO(json.dumps({'data':rows}).encode())
        with patch.object(fe, '_agsi_key', lambda: 'offline-fixture'), \
             patch.object(fe.urllib.request, 'urlopen', fake):
            return fe.agsi_norm('2026-09-17')
    assert abs(norm()[0] - 85.054) < 1e-9
    partial = norm(omit=(2023,))
    assert partial[2] == 4 and 69.06-partial[0] > -15
    print('STORAGE STILL OPEN: 4-year norm accepted; gap=', round(69.06-partial[0], 4))
    assert norm(omit=(2023,2024))[0] is None
    assert norm(wrong_date=True)[2] == 5
    assert math.isnan(norm(nonfinite=True)[0])
    print('STORAGE STILL OPEN: wrong dates and NaN accepted; three-year control rejects')

    for bad_rc in (2, -15):
        def fake_run(cmd, cwd):
            advisory = any(str(a).endswith(('consumer_check.py','ledger_staleness.py')) for a in cmd)
            return (bad_rc, 'synthetic execution failure') if advisory else (0, 'control OK')
        with patch.object(cc, 'run', fake_run), contextlib.redirect_stdout(io.StringIO()) as out:
            rc = cc.main()
        assert rc == 0
        print('CLOSEOUT STILL OPEN: child rc=', bad_rc, 'runner rc=', rc,
              [x.strip() for x in out.getvalue().splitlines() if 'MECHANICAL:' in x])
    # HNS-07 rule (d) mistakes an observed maximum for a physical upper bound.
    fill, days, past_max, possible_future = 79.0, 4, 0.20, 0.25
    assert fill + days * past_max < 80 and fill + days * possible_future >= 80
    print('HNS-07 EARLY-MISS COUNTEREXAMPLE: 79% + 4*historical-max(0.20)=79.8%;')
    print('a new 0.25pp/day pace reaches 80%; no registered physical bound forbids it')
    print('PASS: all reviewed counterexamples reproduced; no shared owner files edited')
