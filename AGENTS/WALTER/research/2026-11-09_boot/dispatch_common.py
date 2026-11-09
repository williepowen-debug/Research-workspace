import csv, datetime, json
from pathlib import Path
ROOT = Path('/home/willi/Research-workspace')
W = ROOT / 'AGENTS/WALTER'
OUT = W / 'research/2026-11-09_boot'
NO_HANDOFF_ANY = {'TERRY', 'PROME'}
NO_HANDOFF_INFO = {'CARL', 'RED'}
def send(cards, origin):
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    paths = []
    for d in cards:
        sid = f"SIG-W-20261109-{d['n']:03d}"
        rel = f"BOARD/{sid}-{d['slug']}.md"
        p = ROOT / rel
        assert not p.exists(), p
        body = '# ' + d['title'] + '\n\n' + d['body'] + '\n\nSources: ' + d['sources'] + '\n'
        wc = len(d['body'].split())
        assert wc <= (200 if d['precedence'] in ('FLASH','IMMEDIATE') else 500), (sid, wc)
        conf = d['confidence']
        h = dict(signal_id=sid, date='2026-11-09', timestamp=stamp, dispatched=stamp, source=d.get('source','WALTER'), origin=[origin],
                 action=d['action'], info=d['info'], precedence=d['precedence'], signal_type=d['signal_type'],
                 confidence=conf, confidence_language=d.get('lang','reports'), resources=1, safety_net=d.get('safety_net','clear'),
                 cluster=d['cluster'], domain=d['domain'], entities=d['entities'], word_count=wc,
                 dispatch_note=d['note'], **d.get('extra', {}))
        p.write_text('---\n' + ''.join(k + ': ' + json.dumps(v) + '\n' for k, v in h.items()) + '---\n' + body)
        paths.append(rel)
        with (W / 'routed/route_log.tsv').open('a') as f:
            csv.writer(f, delimiter='\t', lineterminator='\n').writerow(
                [stamp, sid, origin, d['title'], d['precedence'], ','.join(d['action']), ','.join(d['info']), conf])
        for role, names in (('ACTION', d['action']), ('INFO', d['info'])):
            for name in names:
                if name in NO_HANDOFF_ANY or (role == 'INFO' and name in NO_HANDOFF_INFO):
                    continue
                hr = f'AGENTS/{name}/inbox/WALTER/{sid}.md'
                hp = ROOT / hr
                assert not hp.exists(), hp
                hp.parent.mkdir(parents=True, exist_ok=True)
                ask = 'Apply only the owner work named above; no new study or launch authorized.' if role == 'ACTION' else 'Context only; no directed ask.'
                hp.write_text(
                    f"# {sid} — {d['title']}\nBOARD: /{rel}\nPriority: {d['precedence']}\nRole: {role}\nFrom: WALTER\nDate: 2026-11-09\n\n"
                    f"## Kernel\n{d['body']}\n\n## Why you got this\n{name}: {role} on the canonical recipient line.\n\n"
                    f"## Requested action\n{ask}\n\n## Confidence / caveats\n{conf}; source dates and limits retained above. Written is not delivered or consumed.\n\n"
                    f"## Cross-refs\n/{rel}\nSources: {d['sources']}\n")
                paths.append(hr)
                with (W / 'routed/delivery_log.tsv').open('a') as f:
                    csv.writer(f, delimiter='\t', lineterminator='\n').writerow(
                        [stamp, sid, name, role, 'CC', d['precedence'], hr, 'written_not_delivered_pending_push',
                         'Claude-authored; publication and owner consumption unverified.'])
    return stamp, paths
