import sys, io, contextlib, importlib.util
spec=importlib.util.spec_from_file_location('w','/home/willi/Research-workspace/AGENTS/VIOLET/scripts/writeback_order_check.py')
w=importlib.util.module_from_spec(spec); spec.loader.exec_module(w)
def run(ts):
    w.effective_ts=lambda n: ts[n]
    sys.argv=['x','--quiet']; buf=io.StringIO()
    with contextlib.redirect_stdout(buf): rc=w.main()
    return rc, buf.getvalue()
orig_prov=w.brief_provenance
w.brief_provenance=lambda: []
base={'STATUS.md':(1000,'s'),'NEXUS_BRIEF.md':(1000,'b'),'SCRATCH.md':(1000,'c'),'PROME/inbox/*_from-VIOLET_*.md':(1000,'m')}
# T1 brief lags only -> rc 0 + advisory
t=dict(base); t['NEXUS_BRIEF.md']=(500,'old'); rc,o=run(t); assert rc==0 and 'EXEMPT' in o and 'WQ-719' in o, o; print('T1 brief lag exempt, advisory printed: PASS')
# T2 SCRATCH lags -> rc 1
t=dict(base); t['SCRATCH.md']=(500,'old'); rc,o=run(t); assert rc==1 and 'ORDERING BREACH' in o; print('T2 SCRATCH lag still blocks: PASS')
# T3 memo missing -> rc 1
t=dict(base); t['PROME/inbox/*_from-VIOLET_*.md']=(0,'MISSING'); rc,o=run(t); assert rc==1; print('T3 missing memo still blocks: PASS')
# T4 pin naming no STATUS revision -> red (stub git)
w.brief_provenance=orig_prov
w.effective_ts=lambda n: base[n]
real_git=w._git
def fake(*a):
    if a[0]=='status': return ''
    if a[0]=='log' and '-30' in a: return 'aaaaaaa\nbbbbbbb'
    if a[0]=='log' and '%h' in a[-3] if len(a)>2 else False: return 'aaaaaaa'
    if a[0]=='log' and '%ct' in ' '.join(a): return '1700000000'
    if a[0]=='log': return 'aaaaaaa'
    return ''
w._git=fake
import pathlib
txt='**As of:** 2023-11-14 17:00 ET | **STATUS commit:** `{}`.'
orig_read=pathlib.Path.read_text
pathlib.Path.read_text=lambda self,encoding=None: txt.format(PIN)
PIN='ccccccc'; out=w.brief_provenance(); assert any('NOT among the last 30' in x for x in out), out; print('T4 unresolved pin still red: PASS')
PIN='bbbbbbb'; out=w.brief_provenance(); assert not any('cites' in x for x in out), out; print('T5 older resolvable pin no longer red (WQ-719): PASS')
