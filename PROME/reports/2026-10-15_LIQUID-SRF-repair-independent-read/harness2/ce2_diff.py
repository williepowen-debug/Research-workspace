"""Differential: HEAD (ws) vs pre-fix (prefix) on ORDINARY inputs. Usage: python ce2_diff.py <S>. Mocked fetch, scratch-only writes."""
import sys, json, random, re, importlib.util, tempfile, shutil
from datetime import date, timedelta
from pathlib import Path
from unittest import mock
S = Path(sys.argv[1])
sys.path.insert(0, str(S / 'ws/AGENTS/LIQUID/scripts'))
def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m; spec.loader.exec_module(m); return m
W_new = load('hw_new', S / 'ws/AGENTS/LIQUID/scripts/hy_oas_watch.py')
W_old = load('hw_old', S / 'prefix/AGENTS/LIQUID/scripts/hy_oas_watch.py')
B_new = load('boot_new', S / 'ws/AGENTS/LIQUID/scripts/boot.py')
B_old = load('boot_old', S / 'prefix/AGENTS/LIQUID/scripts/boot.py')
import fetch
rng = random.Random(20261015)
BDAYS = [date(2026, 6, 26) + timedelta(d) for d in range(0, 111) if (date(2026, 6, 26) + timedelta(d)).weekday() < 5]
def val(): return f'{rng.randint(240, 300) / 100:.2f}'
def series(n, dot=0.05, order=None):
    ds = sorted(rng.sample(BDAYS, n))
    rows = [{'date': d.isoformat(), 'value': '.' if rng.random() < dot else val()} for d in ds]
    order = order or rng.choice(['asc', 'desc', 'shuffle'])
    if order == 'desc': rows.reverse()
    elif order == 'shuffle': rng.shuffle(rows)
    return rows
def fp(mod, rows):
    with mock.patch.object(fetch, '_retry_request', return_value={'observations': rows}):
        return mod._first_published(100)

# A. _first_published on ordinary distinct-date responses
diffA = 0; N = 5000
for _ in range(N):
    r = series(rng.randint(0, len(BDAYS)))
    if fp(W_new, r) != fp(W_old, r): diffA += 1
print(f'A _first_published ordinary distinct dates: {N} trials, outputs differing: {diffA}')
# B. same with ONE duplicated date injected
newNone = oldNone = 0; N = 2000
for _ in range(N):
    r = series(rng.randint(1, len(BDAYS))); dup = dict(rng.choice(r)); dup['value'] = rng.choice([dup['value'], val()]); r.insert(rng.randint(0, len(r)), dup)
    newNone += fp(W_new, r) is None; oldNone += fp(W_old, r) is None
print(f'B one repeated date injected: {N} trials, HEAD refused {newNone}, pre-fix refused {oldNone}')

# C/D. fred_series
def fs(mod, rows):
    with mock.patch.object(mod, 'fred_fetch', return_value=rows):
        return mod.fred_series('X')
cnt = {'C_ordinary': [0, 0], 'D_nonnum_not_head': [0, 0], 'D_nonnum_head': [0, 0], 'D_head_value_differs': [0, 0]}
for _ in range(5000):
    rows = [r for r in series(rng.randint(1, 6), dot=0, order='desc')]          # fetch.py shape: '.' dropped, newest-first
    cnt['C_ordinary'][0] += 1; cnt['C_ordinary'][1] += fs(B_new, rows) != fs(B_old, rows)
    if len(rows) > 1:
        bad = [dict(r) for r in rows]; k = rng.randint(1, len(bad) - 1); bad[k]['value'] = rng.choice(['ND', '', 'n/a', None])
        cnt['D_nonnum_not_head'][0] += 1; cnt['D_nonnum_not_head'][1] += fs(B_new, bad) != fs(B_old, bad)
        bad2 = [dict(r) for r in rows]; bad2[0]['value'] = 'ND'
        a, b = fs(B_new, bad2), fs(B_old, bad2)
        cnt['D_nonnum_head'][0] += 1; cnt['D_nonnum_head'][1] += a != b
        cnt['D_head_value_differs'][0] += 1; cnt['D_head_value_differs'][1] += (a[0], a[2], a[3]) != (b[0], b[2], b[3])
for k, (n, d) in cnt.items(): print(f'{k}: {n} trials, differing: {d}')

# E. full main() on ordinary multi-run scenarios (distinct dates), both versions into separate scratch dirs
def norm(t): return re.sub(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2} ?[A-Z]*  ', 'TS  ', t)
def setup(mod, root):
    alerts = root / 'alerts'; alerts.mkdir(parents=True); (root / 'inbox').mkdir()
    sig = root / 'SIGNALS.md'; sig.write_text('| Date | From | To | Priority | Signal |\n|---|---|---|---|---|\n')
    for k, v in dict(WORKSPACE=root, ALERTDIR=alerts, ALOG=alerts/'HY_OAS_ALERTS.log', RLOG=alerts/'watch.log',
                     STATE=alerts/'HY_OAS_STATE', PROME_INBOX=root/'inbox', SIGNALS=sig).items(): setattr(mod, k, v)
def outputs(mod):
    st = json.loads(mod.STATE.read_text()); st.pop('checked', None)
    pk = {f.name: f.read_text() for f in mod.PROME_INBOX.glob('*')}
    return st, pk, mod.SIGNALS.read_text(), norm(mod.ALOG.read_text() if mod.ALOG.exists() else ''), norm(mod.RLOG.read_text())
base = Path(tempfile.mkdtemp(dir=S, prefix='diffE-')); diffE = fired = 0; N = 400
for i in range(N):
    full = sorted(rng.sample(BDAYS, rng.randint(3, 40)))
    vals = [{'date': d.isoformat(), 'value': val()} for d in full]
    prev = rng.choice([{}, {'zone': 'green', 'sev': 0, 'obs_date': full[0].isoformat()},
                       {'zone': 'yellow', 'sev': 1, 'obs_date': full[0].isoformat()}])
    roots = []
    for tag, mod in (('n', W_new), ('o', W_old)):
        root = base / f'{i}{tag}'; setup(mod, root); roots.append(root)
        if prev: mod.STATE.write_text(json.dumps(prev))
    for k in range(rng.randint(1, 4)):                     # successive daily runs, frontier advancing
        cut = max(1, len(vals) - rng.randint(0, 3) + k)
        frontier = vals[:cut]; latest = [dict(v) for v in reversed(frontier[-10:])]
        for mod in (W_new, W_old):
            setup_root = mod.WORKSPACE
            with mock.patch.object(fetch, 'fred_fetch', return_value=latest), \
                 mock.patch.object(fetch, '_retry_request', return_value={'observations': list(frontier)}), \
                 mock.patch.object(sys, 'argv', ['x']):
                mod.main()
    # re-point and compare
    on = []; 
    for tag, mod in (('n', W_new), ('o', W_old)):
        root = base / f'{i}{tag}'
        for k2, v2 in dict(WORKSPACE=root, ALERTDIR=root/'alerts', ALOG=root/'alerts/HY_OAS_ALERTS.log', RLOG=root/'alerts/watch.log',
                           STATE=root/'alerts/HY_OAS_STATE', PROME_INBOX=root/'inbox', SIGNALS=root/'SIGNALS.md').items(): setattr(mod, k2, v2)
        on.append(outputs(mod))
    if on[0] != on[1]: diffE += 1
    fired += bool(on[0][1])
print(f'E full main() multi-run ordinary scenarios: {N}, with any packet: {fired}, outputs differing HEAD vs pre-fix: {diffE}')
shutil.rmtree(base)
