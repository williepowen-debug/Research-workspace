"""Frozen source revision + real four target rows; writes only a temporary copy."""
import argparse
import datetime as dt
import importlib.util
import json
from pathlib import Path
import sys
import tempfile

root=Path(sys.argv[1]);sys.path.insert(0,str(root/'scripts'))
import orch_time as t
import orch_log as w
spec=importlib.util.spec_from_file_location('oc',root/'PROME/tools/orch_closeout.py')
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
now=dt.datetime.now(dt.timezone.utc)
source=(root/'PROME/state/ORCH_LOG.tsv').read_bytes()
targets=[source.decode().splitlines()[i-1].split('\t') for i in (1140,1141,1142,1200)]
with tempfile.TemporaryDirectory() as d:
    ledger=Path(d)/'ledger.tsv';view=Path(d)/'view.md';ledger.write_bytes(source)
    before=c.evaluate(ledger,now.astimezone(t.ET).date(),now=now)[0]
    for original in targets:
        data=t.payload(original,t.CLOSEOUT)
        correction=dict(target=t.key(original),owner=data['owner'],session_id=data['session_id'],
                        replacement='UNKNOWN',recorded_at=now.isoformat(),reason='L748 explicit historical invalidation; exact event time unknown')
        row={x:'' for x in w.COLS}
        row.update(date=now.astimezone(t.ET).date().isoformat(),desk=original[1],tier=original[2],touch='CLOSE',
                   trigger='time invalidation '+t.key(original),delivered='TIME-CORRECTION (original time UNKNOWN)',notes=t.MARKER+json.dumps(correction))
        assert w.append(argparse.Namespace(**row),str(ledger),str(view))==0
    after=c.evaluate(ledger,now.astimezone(t.ET).date(),now=now)[0]
    assert ledger.read_bytes().startswith(source)
    assert len(w.check(str(ledger),True)[1])==len(w.check(str(root/'PROME/state/ORCH_LOG.tsv'),True)[1])+4
    selected=[r for r in after if r['key'] in {t.key(x) for x in targets}]
    assert len(selected)==4 and all(r['state']=='UNKNOWN' and r['time_status']=='INVALIDATED-UNKNOWN' for r in selected)
    assert all(r['touch']!='CLOSE' for r in after)
    print(json.dumps(dict(original_bytes_preserved=True,appended=4,original_obligations_invalidated=selected,
                         before_count=len(before),after_count=len(after),live_ledger_unchanged=(root/'PROME/state/ORCH_LOG.tsv').read_bytes()==source),indent=2))
