"""Land hash-reviewed create-only packet manifest, own route/delivery and correction rows."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json,hashlib
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3]
m=json.loads((HERE/'packet-manifest.json').read_text());rs=json.loads((HERE/'prepared-routes.json').read_text())
for x in m['files']:
 p=Path(x['path']);valid=(not p.is_absolute() and '..' not in p.parts and ((p.parts[0]=='BOARD' and len(p.parts)==2) or (p.parts[0]=='AGENTS' and p.parts[2:4]==('inbox','WALTER') and len(p.parts)==5)))
 if not valid:raise SystemExit('Refuse path outside reviewed packet scope')
 b=(HERE/'.cache/packets'/p).read_bytes()
 if hashlib.sha256(b).hexdigest()!=x['sha256']:raise SystemExit('Refuse changed packet bytes')
 if (ROOT/p).exists():raise SystemExit('Refuse existing destination: '+str(p))
reg=ROOT/'AGENTS/WALTER/registry/CORRECTIONS.tsv'
if 'COR-20261013-16\t' in reg.read_text():raise SystemExit('Refuse existing correction ID')
now=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
for x in m['files']:
 p=ROOT/x['path'];p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('xb') as h:h.write((HERE/'.cache/packets'/x['path']).read_bytes())
with (ROOT/'AGENTS/WALTER/routed/route_log.tsv').open('a') as h:
 wr=csv.writer(h,delimiter='\t',lineterminator='\n')
 for r in rs:wr.writerow([now,r['signal_id'],'x-bookmark Will-authorized October13 snapshot',r['title'],'PRIORITY',','.join(r['action']),','.join(r['info']),r['confidence']])
with (ROOT/'AGENTS/WALTER/routed/delivery_log.tsv').open('a') as h:
 wr=csv.writer(h,delimiter='\t',lineterminator='\n')
 for r in rs:
  for role,names in [('ACTION',r['action']),('INFO',r['info'])]:
   for n in names:
    if n in ['PROME','RED','TERRY'] or n=='CARL' and role=='INFO':continue
    wr.writerow([now,r['signal_id'],n,role,'CLAUDE_CODE','PRIORITY',f'AGENTS/{n}/inbox/WALTER/{r["signal_id"]}.md','written_not_delivered_pending_push','Runtime-neutral own packet; legacy schema platform token. Fleet liveness UNKNOWN; no recipient consumption inferred.'])
r=next(x for x in rs if x.get('signal_type')=='correction')
with reg.open('a') as h:csv.writer(h,delimiter='\t',lineterminator='\n').writerow(['COR-20261013-16','2026-10-13','WALTER',','.join(r['action']+r['info']),r['board_path'],'2026-10-27','LIVE','EXTERNAL LHMacro/LIQUID said TGA880.3B Wednesday; IS885.783B point balance (H.4.1Oct8Table1;880.253B weekly average); conditional45days rounding holds, funding consequence ungraded','HOLD'])
(HERE/'landing-receipt.json').write_text(json.dumps({'landed_at':now,'signals':len(rs),'handoffs':len(m['files'])-len(rs),'files':m['files'],'state':'written_not_delivered_pending_push','correction_register_id':'COR-20261013-16'},indent=2)+'\n')
print(f'Landed{len(rs)}signals/{len(m["files"])-len(rs)}handoffs;1R1row. Not committed, published or marked.')
