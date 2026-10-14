"""Prepare reviewed WALTER routing artifacts inside WALTER; no publication/Git."""
import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
plan = json.loads((HERE / 'route-plan.json').read_text())
plan.append({
    'slug': 'wood-river-fcc-report-primary-event-and-output-unverified',
    'title': 'Wood River FCC issue reported October13; original wire, duration and lost output unverified',
    'domain': 'OIL_ENERGY', 'cluster': 'HYDROCARBON_INFRA',
    'action': ['BRENT'], 'info': ['HENRY', 'RED', 'PROME'],
    'entities': ['Phillips-66', 'PSX', 'Wood-River'],
    'origin': 'October13 Newsquawk/FirstSquawk-attributed Reuters feed; bounded verify-research',
    'confidence': 0.45,
    'body': "October13 secondary feeds report a catalytic-cracker issue at Phillips66's Wood River refinery. Newsquawk's page publishes20:03UTC and names feed19:43UTC; MarketFlux traces its event claim to FirstSquawk15:43ET, attributed to Reuters sources. Shared provenance is possible; these are not independent witnesses. Original Reuters text/operator-event confirmation were not recovered in the bounded verification.\n\nCHANGE: a dated own-site operating-risk lead relevant to the existing PSX earnings-capture comparison. No onset, unit number, shutdown, restart date, duration or lost throughput is established. The quoted355,000b/d is plant capacity, not lost output. Operator process background distinguishes gasoline-oriented FCC from middle-distillate hydrocracking; diesel loss remains unmeasured. Operator's2025Q4 note also supersedes the repost's old50/50 ownership with100% consolidation fromOctober1,2025.\n\nVerification verdict INDETERMINATE on event/severity; corrected framing on capacity, product and ownership. BRENT owns whether later operational evidence changes WAIT. No outage total, earnings loss, trade recommendation or new study follows from this pointer.",
    'sources': [
        {'date': '2026-10-13', 'url': 'https://www.newsquawk.com/headlines/phillips-66-psx-355000-bpd-refinery-in-roxana-illinois-having-issues-with-catalytic-cracker-unit-according-to-reports-citing-sources', 'basis': 'Secondary feed report only;20:03UTC publication/19:43UTC feed'},
        {'date': '2022-09-22', 'url': 'https://www.phillips66.com/newsroom/hydrocracker-upgrade-boosts-wood-river/', 'basis': 'Operator process background only; not current unit status'},
        {'date': 'FY2025 Q4', 'url': 'https://s22.q4cdn.com/128149789/files/doc_financials/2025/q4/Phillips-66-Fourth-Quarter-2025-Earnings-Release-FINAL.pdf', 'basis': 'Operator basis-of-presentation note:100% consolidation fromOctober1,2025'}
    ],
    'ask': 'BRENT: assess this qualified operating-risk lead in the existing PSX asset/earnings comparison. Keep lost output and duration UNKNOWN. Do not count plant capacity as an outage or infer a diesel loss.',
    'refs': ['AGENTS/WALTER/research/2026-10-13_priority-routing/refinery-verify.md', 'AGENTS/BRENT/research/2026-10-13_energy-wait/REPORT.md'],
})

existing = list((ROOT / 'BOARD').glob('SIG-W-20261013-*.md'))
if existing:
    raise SystemExit('REFUSE: October13 BOARD IDs now exist; recheck ID allocation before preparing.')
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
stage = HERE / 'packets'
files = []
for n, row in enumerate(plan, 1):
    sid = f'SIG-W-20261013-{n:03d}'
    path = f'BOARD/{sid}-{row["slug"]}.md'
    source_lines = '\n'.join(f'- [{s["date"]}: {s["basis"]}]({s["url"]})' for s in row['sources'])
    body = f'# {row["title"]}\n\n## Signal\n\n{row["body"]}\n\n## Source\n\n{source_lines}\n\nRetrieved/checked {stamp}.\n\n## Requested action\n\n{row["ask"]}\n\n## Cross-refs\n\n' + '\n'.join('- '+x for x in row['refs'])+'\n'
    header = {'signal_id': sid, 'precedence': 'PRIORITY', 'timestamp': stamp,
              'source': 'WALTER', 'origin': row['origin'], 'to': row['action'],
              'info': row['info'], 'action': row['action'], 'domain': row['domain'],
              'signal_type': 'research', 'confidence': row['confidence'],
              'confidence_language': ('confirmed' if row['confidence'] >= .9 else
                                      'reports' if row['confidence'] >= .75 else
                                      'assessed' if row['confidence'] >= .5 else 'unconfirmed'),
              'resources': 1, 'safety_net': 'clear', 'word_count': len(body.split()),
              'cluster': row['cluster'], 'entities': row['entities'],
              'event_window': 'closed', 'dispatched': stamp,
              'dispatch_note': 'New bounded source inputs; owner grades retained. Fleet visibility UNKNOWN; no dark-owner inference. Publication pending; consumption unverified.'}
    if n == 6:
        header['dispatch_note'] += ' Verify-research verdict INDETERMINATE event; CORRECTED-FRAMING capacity/product/ownership; original wire unavailable.'
    text = '---\n'+'\n'.join(k+': '+json.dumps(v) for k,v in header.items())+'\n---\n\n'+body
    p = stage/path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)
    files.append({'path': path, 'sha256': hashlib.sha256(text.encode()).hexdigest()})
    for role, names in [('ACTION',row['action']),('INFO',row['info'])]:
        for recipient in names:
            if recipient in ('PROME','TERRY') or recipient in ('CARL','RED') and role == 'INFO':
                continue
            target = f'AGENTS/{recipient}/inbox/WALTER/{sid}.md'
            handoff = (f'# {sid} — {row["title"]}\nBOARD: /{path}\nPriority: PRIORITY\nRole: {role}\nFrom: WALTER\nDate: 2026-10-13\n'
                       f'## Kernel\n{row["body"]}\n## Why you got this\n{recipient}: {row["domain"]} evidence in the existing owner work; see source and basis below.\n'
                       f'## Requested action\n'+(row['ask'] if role == 'ACTION' else 'Information only; no recipient-directed work requested.')+'\n'
                       f'## Confidence / caveats\n{row["confidence"]}; source/measurement limits retained above. Written pending commit/publication; consumption unverified.\n'
                       '## Source\n'+source_lines+'\n## Cross-refs\n'+'\n'.join('- '+x for x in row['refs'])+'\n')
            p = stage/target
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(handoff)
            files.append({'path':target,'sha256':hashlib.sha256(handoff.encode()).hexdigest()})
    row.update(signal_id=sid, board_path=path, timestamp=stamp)
(HERE/'prepared-routes.json').write_text(json.dumps(plan,indent=2)+'\n')
(HERE/'packet-manifest.json').write_text(json.dumps({'prepared_at':stamp,'files':files},indent=2)+'\n')
print(f'Prepared {len(plan)} BOARD signals and {len(files)-len(plan)} create-only handoffs; nothing published.')
