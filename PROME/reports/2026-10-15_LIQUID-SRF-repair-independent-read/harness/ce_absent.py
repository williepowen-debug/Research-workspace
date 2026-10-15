import json, sys
sys.argv = [sys.argv[0], sys.argv[1], 'absent']
exec(open(__file__.replace('ce_absent.py','ce_watch.py')).read().split("G = {'zone'")[0])
signals.unlink()   # destination absent on the fire run
w.STATE.write_text(json.dumps({'zone': 'yellow', 'sev': 1, 'obs_date': '2026-10-13'}))
print('rc', run(obs(('2026-10-14', '2.90')), {'observations': obs(('2026-10-14', '2.90'))})); snap_signals = None
print('  watch.log:', [l.split('  ',1)[-1][:90] for l in w.RLOG.read_text().splitlines()])
print('  state.delivered:', json.loads(w.STATE.read_text()).get('delivered'))
signals.write_text('| Date | From | To | Priority | Signal |\n|---|---|---|---|---|\n')   # destination restored
print('rc', run(obs(('2026-10-14', '2.90')), {'observations': obs(('2026-10-14', '2.90'))}))
print('  SIGNALS LIQUID rows after restore + rerun:', sum('| LIQUID |' in l for l in signals.read_text().splitlines()))
