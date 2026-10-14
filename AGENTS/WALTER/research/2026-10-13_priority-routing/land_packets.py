"""Land only the hash-reviewed, create-only routing packet manifest; never Git."""
import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
manifest = json.loads((HERE/'packet-manifest.json').read_text())
routes = json.loads((HERE/'prepared-routes.json').read_text())
for row in manifest['files']:
    relative = Path(row['path'])
    if relative.is_absolute() or '..' in relative.parts:
        raise SystemExit('REFUSE: non-relative packet path')
    allowed = ((relative.parts[0]=='BOARD' and len(relative.parts)==2) or
               (relative.parts[0]=='AGENTS' and relative.parts[2:4]==('inbox','WALTER') and len(relative.parts)==5))
    if not allowed:
        raise SystemExit('REFUSE: packet path outside reviewed routing scope')
    data=(HERE/'packets'/relative).read_bytes()
    if hashlib.sha256(data).hexdigest()!=row['sha256']:
        raise SystemExit('REFUSE: changed packet bytes')
    if (ROOT/relative).exists():
        raise SystemExit('REFUSE: existing destination '+str(relative))
now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
for row in manifest['files']:
    dest=ROOT/row['path']
    dest.parent.mkdir(parents=True,exist_ok=True)
    with dest.open('xb') as handle:
        handle.write((HERE/'packets'/row['path']).read_bytes())
with (ROOT/'AGENTS/WALTER/routed/route_log.tsv').open('a') as handle:
    writer=csv.writer(handle,delimiter='\t',lineterminator='\n')
    for r in routes:
        writer.writerow([now,r['signal_id'],r['origin'],r['title'],'PRIORITY',','.join(r['action']),','.join(r['info']),str(r['confidence'])])
with (ROOT/'AGENTS/WALTER/routed/delivery_log.tsv').open('a') as handle:
    writer=csv.writer(handle,delimiter='\t',lineterminator='\n')
    for r in routes:
        for role,names in [('ACTION',r['action']),('INFO',r['info'])]:
            for name in names:
                if name in ('PROME','TERRY') or name in ('CARL','RED') and role=='INFO':continue
                writer.writerow([now,r['signal_id'],name,role,'CLAUDE_CODE','PRIORITY',f'AGENTS/{name}/inbox/WALTER/{r["signal_id"]}.md','written_not_delivered_pending_push','Runtime-neutral packet; legacy platform token. Fleet liveness UNKNOWN except observed foreign writers. Consumption unverified.'])
(HERE/'landing-receipt.json').write_text(json.dumps({'landed_at':now,'signals':len(routes),'handoffs':len(manifest['files'])-len(routes),'files':manifest['files'],'state':'written_not_delivered_pending_push'},indent=2)+'\n')
print(f'Landed {len(routes)} BOARD packets and {len(manifest["files"])-len(routes)} handoffs; not committed/published/consumed.')
