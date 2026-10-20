import sys,json,hashlib
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/tools')
from test_x_bookmarks_workflow import Workflow,x,w

def run(name, probe):
    f=Workflow('test_501_resumes_after_actual_review_mark'); f.setUp()
    try: probe(f); print('PASS',name)
    finally: f.doCleanup = getattr(f,'doCleanups'); f.doCleanups()

def snapshot(f):
    return {p.name:p.read_bytes() for p in f.root.glob('*.json')}

def reorder(f):
    f.make_items(501);f.main();v=w.read_json(x._pending_path());v['ids'].reverse();w.atomic_json(x._pending_path(),v)
    r=f.review();before=snapshot(f)
    try:f.main('--mark','--review',str(r));raise AssertionError('accepted reordered IDs')
    except SystemExit as e:assert 'binding' in str(e)
    assert snapshot(f)==before

def all_missing(f):
    f.make_items(501);f.main();v=w.read_json(x._pending_path())
    # A parsed, syntactically valid modern stage loses its optional metadata.
    w.atomic_json(x._pending_path(),{k:v[k] for k in ('ids','staged_at')})
    before=snapshot(f)
    try:f.main('--mark');raise AssertionError('accepted metadata downgrade')
    except SystemExit as e:assert 'binding' in str(e)
    assert snapshot(f)==before and x.load_seen()['consumed']==[]
    f.main();f.mark();f.main();f.mark();assert len(x.load_seen()['consumed'])==501

def stage_crash(f):
    f.make_items(501);f.main();r=f.review();before=x.load_seen()
    original=w.atomic_json
    def broken(path,val):
        if Path(path)==x._pending_path():raise OSError('crash before new pending')
        return original(path,val)
    with patch.object(w,'atomic_json',side_effect=broken):
        try:f.main();raise AssertionError('no crash')
        except OSError:pass
    try:f.main('--mark','--review',str(r));raise AssertionError('accepted stale pending/proposal')
    except SystemExit as e:assert 'missing/changed' in str(e)
    assert x.load_seen()==before
    f.main();f.mark();f.main();f.mark();assert len(x.load_seen()['consumed'])==501

def zero_new_crash(f):
    f.make_items(1001);x.save_seen({'consumed':[str(i) for i in range(1000)],'pilot_start_id':None})
    with patch.object(w,'commit_checkpoint',side_effect=OSError('zero-new checkpoint interrupted')):
        try:f.main();raise AssertionError('no crash')
        except OSError:pass
    assert not x.load_seen()['scan_complete']
    f.main();f.main();f.main();assert x.load_pending()==['1000'];f.mark();assert len(x.load_seen()['consumed'])==1001

def cursor_corrupt(f):
    f.main();r=f.review();p=w.path_for(x.SEEN,'next_token');p.write_bytes(b'\xffbroken')
    before=snapshot(f)
    try:f.main('--mark','--review',str(r));raise AssertionError('accepted invalid bytes')
    except SystemExit as e:assert 'missing/changed' in str(e)
    assert snapshot(f)==before

for name,p in [('reordered-exact-IDs',reorder),('metadata-loss-legacy-downgrade',all_missing),('proposal-write-before-pending-crash',stage_crash),('zero-new-interrupted-checkpoint',zero_new_crash),('non-UTF8-proposal',cursor_corrupt)]:run(name,p)


def legacy_compat(f):
    x.save_pending(['genuine-old']); f.main('--mark')
    assert x.load_seen()['consumed']==['genuine-old']
    f.make_items(501);f.main();f.mark()
    x.save_pending([])
    before=snapshot(f);rc,_=f.main('--mark');assert rc==0 and snapshot(f)==before
    x.save_pending(['ambiguous-old'])
    w.path_for(x.SEEN,'next_token').write_text('not-valid-json')
    before=snapshot(f)
    try:f.main('--mark');raise AssertionError('accepted ambiguous legacy with corrupt proposal')
    except SystemExit as e:assert 'binding' in str(e)
    assert snapshot(f)==before and 'ambiguous-old' not in x.load_seen()['consumed']
    f.main();f.mark();assert '500' in x.load_seen()['consumed']
run('legacy-compatible-empty-noop-and-corrupt-sidecar-recovery',legacy_compat)
