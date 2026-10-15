"""Reader-devised counterexamples for hy_oas_watch.py. Usage: python ce_watch.py <ws-root> <case>
All destinations are per-case dirs under the scratch runs/ folder; fetch is mocked; run under unshare -rn."""
import json, sys, shutil
from pathlib import Path
from unittest import mock

WS = Path(sys.argv[1]).resolve(); CASE = sys.argv[2]
TAG = WS.name
sys.path.insert(0, str(WS / 'AGENTS/LIQUID/scripts'))
import hy_oas_watch as w
import fetch

RUNS = Path(__file__).resolve().parents[1] / 'runs' / f'{TAG}-{CASE}'
if RUNS.exists(): shutil.rmtree(RUNS)
alerts = RUNS / 'alerts'; alerts.mkdir(parents=True)
inbox = RUNS / 'inbox'; inbox.mkdir()
signals = RUNS / 'SIGNALS.md'
signals.write_text('| Date | From | To | Priority | Signal |\n|---|---|---|---|---|\n| 2026-10-01 | OTHER | PROME | 🟡 | foreign row |\n')
P = dict(WORKSPACE=RUNS, ALERTDIR=alerts, ALOG=alerts/'HY_OAS_ALERTS.log', RLOG=alerts/'watch.log',
         STATE=alerts/'HY_OAS_STATE', PROME_INBOX=inbox, SIGNALS=signals)
for k, v in P.items(): setattr(w, k, v)

def obs(*pairs): return [{'date': d, 'value': v} for d, v in pairs]
def run(latest, first):
    with mock.patch.object(fetch, 'fred_fetch', return_value=latest), \
         mock.patch.object(fetch, '_retry_request', return_value=first), \
         mock.patch.object(sys, 'argv', ['hy_oas_watch.py']):
        return w.main()
def snap(label):
    pk = {f.name: f.read_text() for f in inbox.glob('*UNATTENDED*')}
    st = json.loads(w.STATE.read_text()) if w.STATE.exists() else {}
    sig_rows = [l for l in signals.read_text().splitlines() if '| LIQUID |' in l]
    print(f'--- {label}')
    print('  rc/state:', {k: st.get(k) for k in ('zone','bps','sub260','obs_date','kill_met_on','delivered')})
    print('  packets:', {n: [l for l in t.splitlines() if l.startswith('**Signal') or l.startswith('**Current')] for n, t in pk.items()})
    print('  SIGNALS LIQUID rows:', len(sig_rows))
    for r in sig_rows: print('    ', r[:150].replace('\n',' '), '...')
    wl = w.RLOG.read_text().splitlines() if w.RLOG.exists() else []
    print('  watch.log tail:', [l.split('  ',1)[-1][:110] for l in wl[-4:]])
    return st, pk, sig_rows

G = {'zone': 'green', 'sev': 0, 'obs_date': '2026-07-01'}

if CASE == 'dup_obs':
    # CE1: first-published feed carries the SAME observation date twice (a duplicated / re-vintaged row).
    # Only ONE distinct sub-260 close exists (07-03); the prior close 07-02 is 270.
    w.STATE.write_text(json.dumps(G))
    rc = run(obs(('2026-07-03', '2.59')),
             {'observations': obs(('2026-07-01', '2.72'), ('2026-07-02', '2.70'), ('2026-07-03', '2.59'), ('2026-07-03', '2.59'))})
    print('rc', rc); snap('duplicated 07-03 row, one distinct sub-260 close')

elif CASE == 'dup_obs_distinct_dates_control':
    w.STATE.write_text(json.dumps(G))
    rc = run(obs(('2026-07-03', '2.59')),
             {'observations': obs(('2026-07-01', '2.72'), ('2026-07-02', '2.70'), ('2026-07-03', '2.59'))})
    print('rc', rc); snap('control: no duplicate')

elif CASE == 'dest_fail':
    # CE2: destination failure DURING delivery of a two-event fire: SIGNALS append raises after the 1st row.
    w.STATE.write_text(json.dumps({'zone': 'green', 'sev': 0, 'obs_date': '2026-10-13'}))
    first = {'observations': obs(('2026-07-01', '2.59'), ('2026-07-02', '2.58'), ('2026-10-14', '2.90'))}
    real_row = w._signals_row; calls = {'n': 0}
    def flaky(line, d):
        calls['n'] += 1
        if calls['n'] == 2: raise OSError(28, 'No space left on device (synthetic)')
        return real_row(line, d)
    with mock.patch.object(w, '_signals_row', side_effect=flaky):
        rc = run(obs(('2026-10-14', '2.90')), first)
    print('rc', rc); snap('run 1: SIGNALS fails after first row')
    rc = run(obs(('2026-10-14', '2.90')), first)       # destination healthy again, same observation
    print('rc', rc); snap('run 2: same obs, destination healthy')
    rc = run(obs(('2026-10-15', '2.91')), {'observations': first['observations'] + obs(('2026-10-15', '2.91'))})
    print('rc', rc); snap('run 3: next day')

elif CASE == 'concurrent':
    # CE3: two overlapping runs (timer + manual) both read the same prior state before either writes it.
    prev = {'zone': 'green', 'sev': 0, 'obs_date': '2026-10-13'}
    w.STATE.write_text(json.dumps(prev))
    first = {'observations': obs(('2026-07-01', '2.59'), ('2026-07-02', '2.58'), ('2026-10-14', '2.90'))}
    rc1 = run(obs(('2026-10-14', '2.90')), first)
    w.STATE.write_text(json.dumps(prev))   # interleaving: process B read STATE before A wrote it
    rc2 = run(obs(('2026-10-14', '2.90')), first)
    print('rc', rc1, rc2); snap('two interleaved runs, same observation')

elif CASE == 'fp_ahead':
    # CE4: first-published frontier AHEAD of the latest-revised quote (latest still on 07-02, fp already has 07-03).
    w.STATE.write_text(json.dumps(G))
    rc = run(obs(('2026-07-02', '2.59')),
             {'observations': obs(('2026-07-01', '2.70'), ('2026-07-02', '2.59'), ('2026-07-03', '2.58'))})
    print('rc', rc); st, pk, rows = snap('fp frontier 07-03 ahead of latest 07-02')
    for t in pk.values():
        for l in t.splitlines():
            if 'LATE ALERT' in l: print('  packet line:', l[:260])

elif CASE == 'halfbp':
    # CE8: sub-bp first-published values (hypothetical precision change) at the strict <260 boundary
    for v in ('2.594', '2.595', '2.596', '2.599'):
        w.STATE.write_text(json.dumps(G))
        for f in inbox.glob('*UNATTENDED*'): f.unlink()
        rc = run(obs(('2026-07-03', v)), {'observations': obs(('2026-07-02', '2.59'), ('2026-07-03', v))})
        st = json.loads(w.STATE.read_text())
        print(f'  fp 07-03={v} -> raw {float(v)*100!r}bp, sub260={st["sub260"]}, kill_met_on={st.get("kill_met_on")}')

if CASE == 'fp_ahead_ordinary':
    # CE4b: fp frontier one day AHEAD and the first pair ends exactly on the stale latest date.
    w.STATE.write_text(json.dumps(G))
    rc = run(obs(('2026-07-03', '2.58')),
             {'observations': obs(('2026-07-01', '2.70'), ('2026-07-02', '2.59'), ('2026-07-03', '2.58'), ('2026-07-06', '2.57'))})
    print('rc', rc); st, pk, rows = snap('fp has 07-06=257 while latest quote is 07-03=258')
    for t in pk.values():
        for l in t.splitlines():
            if l.startswith('- 🚨'): print('  packet line:', l[:170])
