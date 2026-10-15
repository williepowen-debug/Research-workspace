"""Read #2 reader-devised CE1-class counterexamples for hy_oas_watch.py.
Usage: python ce2_watch.py <ws-root> <case>. Destinations = scratch runs2/; fetch mocked; run under unshare -rn."""
import json, sys, shutil
from pathlib import Path
from unittest import mock

WS = Path(sys.argv[1]).resolve(); CASE = sys.argv[2]
sys.path.insert(0, str(WS / 'AGENTS/LIQUID/scripts'))
import hy_oas_watch as w
import fetch

RUNS = Path(__file__).resolve().parents[1] / 'runs2' / f'{WS.name}-{CASE}'
if RUNS.exists(): shutil.rmtree(RUNS)
alerts = RUNS / 'alerts'; alerts.mkdir(parents=True)
inbox = RUNS / 'inbox'; inbox.mkdir()
signals = RUNS / 'SIGNALS.md'
signals.write_text('| Date | From | To | Priority | Signal |\n|---|---|---|---|---|\n| 2026-10-01 | OTHER | PROME | 🟡 | foreign row |\n')
for k, v in dict(WORKSPACE=RUNS, ALERTDIR=alerts, ALOG=alerts/'HY_OAS_ALERTS.log', RLOG=alerts/'watch.log',
                 STATE=alerts/'HY_OAS_STATE', PROME_INBOX=inbox, SIGNALS=signals).items():
    setattr(w, k, v)

def obs(*pairs): return [{'date': d, 'value': v} for d, v in pairs]
def run(latest, first):
    with mock.patch.object(fetch, 'fred_fetch', return_value=latest), \
         mock.patch.object(fetch, '_retry_request', return_value=first), \
         mock.patch.object(sys, 'argv', ['hy_oas_watch.py']):
        return w.main()
def fp_direct(first):
    with mock.patch.object(fetch, '_retry_request', return_value=first):
        return w._first_published(100)
def snap(label):
    st = json.loads(w.STATE.read_text()) if w.STATE.exists() else {}
    pk = {f.name: [l for l in f.read_text().splitlines() if l.startswith('**Signal')] for f in inbox.glob('*UNATTENDED*')}
    rows = [l[:120] for l in signals.read_text().splitlines() if '| LIQUID |' in l]
    wl = [l.split('  ', 1)[-1][:100] for l in (w.RLOG.read_text().splitlines() if w.RLOG.exists() else [])]
    alog = w.ALOG.read_text().count('\n') if w.ALOG.exists() else 0
    print(f'--- {label}')
    print('  state:', {k: st.get(k) for k in ('zone', 'bps', 'sub260', 'obs_date', 'kill_met_on', 'delivered')})
    print('  packets:', pk)
    print('  SIGNALS LIQUID rows:', len(rows), rows)
    print('  alert-log lines:', alog, '| watch.log:', wl[-3:])

G = {'zone': 'green', 'sev': 0, 'obs_date': '2026-07-01'}

if CASE == 'N1_dup_elsewhere_suppresses_then_recovers':
    # Repeated date with DIFFERENT, NON-sub-260 values (06-29) while a GENUINE distinct-date kill pair exists
    # (07-02, 07-03). Acceptance #8: whole response refused -> no kill this run. Then the feed is clean next day:
    # does the recovery path raise the kill with its ORIGINAL date (not swallowed, not re-dated)?
    w.STATE.write_text(json.dumps(G))
    first1 = {'observations': obs(('2026-06-29', '2.72'), ('2026-06-29', '2.75'), ('2026-07-01', '2.70'),
                                  ('2026-07-02', '2.59'), ('2026-07-03', '2.59'))}
    print('direct _first_published:', fp_direct(first1))
    print('rc', run(obs(('2026-07-03', '2.59')), first1)); snap('run 1: dup on 06-29 + genuine pair 07-02/07-03')
    first2 = {'observations': obs(('2026-06-29', '2.72'), ('2026-07-01', '2.70'), ('2026-07-02', '2.59'),
                                  ('2026-07-03', '2.59'), ('2026-07-06', '2.61'))}
    print('rc', run(obs(('2026-07-06', '2.61')), first2)); snap('run 2 (next day): clean feed, latest 07-06=261')
    print('rc', run(obs(('2026-07-06', '2.61')), first2)); snap('run 3: rerun same obs (idempotency)')

elif CASE == 'N2_out_of_order_distinct':
    for lab, rows in (('259/270/259 shuffled', (('2026-07-03', '2.59'), ('2026-07-01', '2.59'), ('2026-07-02', '2.70'))),
                      ('270/259/259 shuffled', (('2026-07-03', '2.59'), ('2026-07-01', '2.70'), ('2026-07-02', '2.59')))):
        w.STATE.write_text(json.dumps(G))
        for f in inbox.glob('*UNATTENDED*'): f.unlink()
        print('direct:', fp_direct({'observations': obs(*rows)}))
        print('rc', run(obs(('2026-07-03', '2.59')), {'observations': obs(*rows)})); snap(lab)

elif CASE == 'N3_dup_before_gate_window':
    # Duplicate dated BEFORE GATE_REGISTERED (endpoint ignoring observation_start AND output_type).
    w.STATE.write_text(json.dumps(G))
    first = {'observations': obs(('2026-06-20', '2.70'), ('2026-06-20', '2.71'), ('2026-07-01', '2.70'),
                                 ('2026-07-02', '2.59'), ('2026-07-03', '2.59'))}
    print('rc', run(obs(('2026-07-03', '2.59')), first)); snap('dup outside the kill window + genuine pair')

elif CASE == 'N4_empty_and_dot_dups':
    for lab, first in (('empty observations', {'observations': []}),
                       ('dup date both "."', {'observations': obs(('2026-07-02', '.'), ('2026-07-02', '.'), ('2026-07-01', '2.59'), ('2026-07-03', '2.59'))}),
                       ('dup date "." + numeric', {'observations': obs(('2026-07-01', '2.70'), ('2026-07-02', '2.59'), ('2026-07-03', '.'), ('2026-07-03', '2.59'))})):
        w.STATE.write_text(json.dumps(G))
        print('direct:', fp_direct(first))
        print('rc', run(obs(('2026-07-03', '2.59')), first)); snap(lab)

elif CASE == 'N5_noncanonical_date_string':
    # SAME observation date written two ways. Dedup is keyed on the raw string -> not seen as a repeat.
    for lab, alt in (('trailing space', '2026-07-03 '), ('ISO datetime', '2026-07-03T00:00:00'), ('unpadded', '2026-7-03')):
        w.STATE.write_text(json.dumps(G))
        for f in inbox.glob('*UNATTENDED*'): f.unlink()
        first = {'observations': obs(('2026-07-01', '2.72'), ('2026-07-02', '2.70'), ('2026-07-03', '2.59'), (alt, '2.59'))}
        print('direct:', fp_direct(first))
        print('rc', run(obs(('2026-07-03', '2.59')), first)); snap(f'one distinct sub-260 close, duplicate written as {alt!r}')

elif CASE == 'N6_dup_after_kill_already_recorded':
    # Terminal marker already set and delivered; the next run's feed carries a duplicate -> marker must survive.
    prev = dict(G, kill_met_on='2026-07-03', delivered=['🚨 KILL-LEVEL MET (NOT a |2026-07-03'])
    w.STATE.write_text(json.dumps(prev))
    first = {'observations': obs(('2026-07-02', '2.59'), ('2026-07-03', '2.59'), ('2026-07-03', '2.59'), ('2026-07-06', '2.58'))}
    print('rc', run(obs(('2026-07-06', '2.58')), first)); snap('prior kill marker + duplicated feed')

elif CASE == 'N7_missing_date_keys':
    for lab, rows in (('two rows without a date key', [{'value': '2.59'}, {'value': '2.59'}, {'date': '2026-07-03', 'value': '2.59'}]),
                      ('one numeric row without a date key', [{'date': '2026-07-02', 'value': '2.59'}, {'value': '2.59'}, {'date': '2026-07-03', 'value': '2.59'}]),
                      ('one "." row without a date key', [{'date': '2026-07-02', 'value': '2.59'}, {'value': '.'}, {'date': '2026-07-03', 'value': '2.59'}])):
        w.STATE.write_text(json.dumps(G))
        for f in inbox.glob('*UNATTENDED*'): f.unlink()
        print('direct:', fp_direct({'observations': rows}))
        print('rc', run(obs(('2026-07-03', '2.59')), {'observations': rows})); snap(lab)

elif CASE == 'N8_dup_with_escalation':
    # Escalation side must be unchanged when the kill side is refused.
    w.STATE.write_text(json.dumps({'zone': 'green', 'sev': 0, 'obs_date': '2026-10-13'}))
    first = {'observations': obs(('2026-10-13', '2.70'), ('2026-10-14', '2.90'), ('2026-10-14', '2.90'))}
    print('rc', run(obs(('2026-10-14', '2.90')), first)); snap('escalation to red + duplicated fp row')

elif CASE == 'N5b_single_malformed_date_reorders':
    # No duplicate at all: ONE resetting close (270) carries a non-ISO date string. String sort moves it
    # after every ISO date, so 07-01 (259) and 07-03 (259) become adjacent across the reset.
    w.STATE.write_text(json.dumps(G))
    first = {'observations': obs(('2026-06-30', '2.72'), ('2026-07-01', '2.59'), ('2026-7-02', '2.70'), ('2026-07-03', '2.59'))}
    print('direct:', fp_direct(first))
    print('rc', run(obs(('2026-07-03', '2.59')), first)); snap('07-02 reset close dated "2026-7-02"')

elif CASE == 'N5c_malformed_date_next_day':
    w.STATE.write_text(json.dumps(G))
    first = {'observations': obs(('2026-06-30', '2.72'), ('2026-07-01', '2.59'), ('2026-7-02', '2.70'), ('2026-07-03', '2.59'))}
    print('rc', run(obs(('2026-07-03', '2.59')), first)); snap('day 1 (as N5b)')
    first2 = {'observations': first['observations'] + obs(('2026-07-06', '2.65'))}
    print('rc', run(obs(('2026-07-06', '2.65')), first2)); snap('day 2: 07-06=265 appended')
