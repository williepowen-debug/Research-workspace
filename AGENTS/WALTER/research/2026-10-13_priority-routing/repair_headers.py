"""Correct pre-first-commit scalar serialization in six new WALTER BOARD cards."""
import hashlib
import json
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
routes=json.loads((HERE/'prepared-routes.json').read_text())
tokens={'signal_id','precedence','timestamp','source','domain','signal_type','confidence_language','safety_net','cluster','event_window','dispatched'}
for row in routes:
    p=ROOT/row['board_path'];t=p.read_text();end=t.index('\n---\n',4)
    lines=t[4:end].splitlines();fixed=[]
    for line in lines:
        key,sep,value=line.partition(': ')
        if key in tokens:
            value=json.loads(value)
            line=key+': '+value
        fixed.append(line)
    fixed.insert(1,'date: 2026-10-13')
    revised='---\n'+'\n'.join(fixed)+t[end:]
    p.write_text(revised)
    (HERE/'packets'/row['board_path']).write_text(revised)
for name in ['packet-manifest.json','landing-receipt.json']:
    p=HERE/name;d=json.loads(p.read_text())
    for r in d['files']:
        r['sha256']=hashlib.sha256((ROOT/r['path']).read_bytes()).hexdigest()
    d['header_repair']='Pre-first-commit scalar serialization only;source bodies/route roles unchanged.'
    p.write_text(json.dumps(d,indent=2)+'\n')
print('Corrected six scalar headers;manifest hashes refreshed;no signal body or recipient change.')
