"""Write one BOARD card + create-only handoffs + route/delivery rows from a JSON spec. Usage: dispatch.py spec.json"""
import json, sys, subprocess, re
from datetime import datetime, timezone
from pathlib import Path
ROOT = Path('/home/willi/Research-workspace')
EXEMPT_INFO = {'RED', 'PROME', 'TERRY', 'CARL'}   # pull-complete: INFO via BOARD ID-diff
NO_HANDOFF_ACTION = {'PROME', 'TERRY'}
s = json.load(open(sys.argv[1]))
ts = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
sid = s['id']; slug = s['slug']
card = ROOT / 'BOARD' / f'{sid}-{slug}.md'
assert not card.exists() and not list((ROOT/'BOARD').glob(sid+'-*')), 'card id exists'
q = lambda v: json.dumps(v, ensure_ascii=False)
body = s['body'].strip() + '\n'
wc = len(body.split())
fm = ['---', f'signal_id: {q(sid)}', f'date: "2026-10-30"', f'timestamp: {q(ts)}', f'dispatched: {q(ts)}',
      f'source: {q(s["source"])}', f'origin: {q(s["origin"])}', f'domain: {q(s["domain"])}', f'cluster: {q(s["cluster"])}']
if s.get('cluster_secondary'): fm.append(f'cluster_secondary: {q(s["cluster_secondary"])}')
fm += [f'signal_role: {q(s.get("signal_role","primary_substance"))}', f'action: {q(s["action"])}', f'info: {q(s["info"])}',
       f'precedence: {q(s["precedence"])}', f'signal_type: {q(s["signal_type"])}', f'confidence: {s["confidence"]}',
       f'confidence_language: {q(s["confidence_language"])}', f'entities: {q(s["entities"])}', f'resources: {len(s["origin"])}',
       f'safety_net: {q(s.get("safety_net","not-triggered"))}', 'event_window: "closed"', f'word_count: {wc}',
       f'dispatch_note: {q(s["dispatch_note"])}', '---']
card.write_text('\n'.join(fm) + '\n' + body)
paths = [str(card.relative_to(ROOT))]
rows = []
for role, names in (('ACTION', s['action']), ('INFO', s['info'])):
    for r in names:
        if role == 'INFO' and r in EXEMPT_INFO: continue
        if role == 'ACTION' and r in NO_HANDOFF_ACTION: continue
        h = ROOT / 'AGENTS' / r / 'inbox' / 'WALTER' / f'{sid}.md'
        h.parent.mkdir(parents=True, exist_ok=True)
        assert not h.exists(), f'handoff exists {h}'
        ask = s['asks'].get(r, 'For context; no action requested.')
        why = s.get('why', {}).get(r, s.get('why_default', 'In your routing lane.'))
        h.write_text(f"# {sid} — {s['title']}\nBOARD: /{paths[0]}\nPriority: {s['precedence']}\nRole: {role}\nFrom: WALTER\nDate: 2026-10-30\n\n## Kernel\n\n{s['kernel']}\n\n## Why you got this\n\n{why}\n\n## Requested action\n\n{ask}\n\n## Confidence / caveats\n\n{s['caveat']}\n")
        paths.append(str(h.relative_to(ROOT)))
        rows.append('\t'.join([ts, sid, r, role, 'CLAUDE_CODE', s['precedence'], str(h.relative_to(ROOT)), 'written_not_delivered_pending_push',
                               s['dnote'] + '; metadata platform token is legacy schema, not verified recipient runtime. No current owner receipt.']))
with open(ROOT/'AGENTS/WALTER/routed/delivery_log.tsv', 'a', encoding='utf-8', newline='\n') as f:
    for r in rows: f.write(r + '\n')
with open(ROOT/'AGENTS/WALTER/routed/route_log.tsv', 'a', encoding='utf-8', newline='\n') as f:
    f.write('\t'.join([ts, sid, s['route_origin'], s['route_summary'], s['precedence'], ','.join(s['action']), ','.join(s['info']), str(s['confidence'])]) + '\n')
print(ts, wc, ' '.join(paths))
