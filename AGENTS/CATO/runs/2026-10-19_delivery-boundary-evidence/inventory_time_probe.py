"""Independent DB3 chronology probe; all ledger writes use a temporary directory."""
import datetime as dt
import importlib.util
import json
from pathlib import Path
import sys
import tempfile

source = Path(sys.argv[1])
spec = importlib.util.spec_from_file_location('cato_inventory_probe', source)
oc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(oc)
day = dt.date(2026, 10, 19)
now = dt.datetime.fromisoformat('2026-10-19T18:45:00+00:00')
evidence = dict(owner='PROME', session_id='session-A',
                touch_at='2026-10-19T10:00:00-04:00',
                observed_at='2026-10-19T10:05:00-04:00',
                state='ASKED_RECEIPT', ask='actual ask', receipt='actual receipt')
row = ['2026-10-19', 'ARGUS', '1', '1', 'independent check', '0', '0', '0',
       oc.MARKER + json.dumps(evidence), '0', '0', '0', '0']
results = []
with tempfile.TemporaryDirectory(prefix='cato-db3-') as directory:
    path = Path(directory) / 'log.tsv'
    path.write_text('\n'.join(['\t'.join(oc.HEADER), '\t'.join(row)]) + '\n')
    for observed_at, expected_nonpass in [('2026-10-19T09:00:00-04:00', True),
                                          ('2026-10-19T10:01:00-04:00', False)]:
        inventory = dict(complete=True, session_ids=['session-A'],
                         expected_keys=[oc.touch_key(row)],
                         evidence='actual native inventory', observed_at=observed_at)
        try:
            rows, issues = oc.evaluate(path, day, now=now, session_inventory=inventory)
            nonpass = bool(issues or any(r['state'] == 'UNKNOWN' for r in rows))
        except ValueError as error:
            nonpass, issues = True, [str(error)]
        results.append(dict(inventory_at=observed_at, launch_at=evidence['touch_at'],
                            receipt_at=evidence['observed_at'], nonpass=nonpass,
                            expected_nonpass=expected_nonpass, issues=issues))
print(json.dumps(results, indent=2))
sys.exit(0 if all(r['nonpass'] == r['expected_nonpass'] for r in results) else 1)
