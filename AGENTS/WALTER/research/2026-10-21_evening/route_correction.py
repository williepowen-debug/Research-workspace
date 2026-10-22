from pathlib import Path
from datetime import datetime, timezone
import json, csv
R = Path('/home/willi/Research-workspace'); W = R/'AGENTS/WALTER'; D = W/'research/2026-10-21_evening'
now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
sid = 'SIG-W-20261021-010'; tgt = 'SIG-W-20261021-008'
slug = 'CORRECTION-to-20261021-008-car-mart-reprieve-now-runs-to-11-01-per-10-21-8k-plus-5m-incremental-loan-and-abs-redeemed-sale-talk-report-holds'
title = "CORRECTION to 008: Car-Mart's lender reprieve now runs to November1 (October21 8-K), with $5M new term loans and its 2024-2 ABS redeemed; the sale-talk report holds"
actions = ['BROCK', 'OTTO']; infos = ['LIQUID', 'CARL', 'PROME']
body = '''008 said the lender reprieve runs "through October22" and pointed to tomorrow's read as the deadline. That was the October20 Bloomberg figure. It is superseded. Car-Mart's 8-K filed October21 (accession 0001171843-26-006742, read by WALTER at sec.gov) says that on October20 the agent and lenders extended the Scheduled Termination Date, and the temporary minimum-liquidity and Collateral Coverage Ratio relief, from October22 through November1, 2026 (the "Current Extension").

The same filing reports a Second Amendment dated October15: $5.0M of incremental term loans, $200,000 of fees. On October20 ACM Auto Trust 2024-2 redeemed its notes and about $92M of receivables were released from the trust. Exhibit 10.1 (rate/covenant terms) was not read by WALTER.

Direction: WEAKEN. The October22 deadline urgency in 008 no longer holds. The Bloomberg sale-talk report (Chapter 11 sale or shareholder vote, no decision) is not contradicted by the filing and still holds. PROME packeted BROCK on this 8-K at 20:21 ET (commit 3fa7383b2), before 008 published. This record links the BOARD copy; it does not replace PROME's packet. Per PROME, CRMT closed $0.66 (-16.46%) October21 (fetch.py, 20:16 ET); WALTER did not re-pull it.

BROCK ACTION: grade L652/L740 at the document as PROME's packet asks; treat 008's October22 date as superseded. OTTO ACTION: the V9 standstill vector's next date is November1, after BROCK's grade. LIQUID/CARL/PROME INFO.

Source: https://www.sec.gov/Archives/edgar/data/799850/000117184326006742/f8k_102126.htm (main document, read); PROME packet commit 3fa7383b2.'''
bp = f'BOARD/{sid}-{slug}.md'
h = {'signal_id': sid, 'date': '2026-10-21', 'timestamp': now, 'dispatched': now, 'source': 'RESEARCH-INTAKE',
     'origin': 'Correction of 008 after PROME packet 3fa7383b2; 8-K main document read by WALTER', 'domain': 'SUBPRIME_AUTO',
     'cluster': 'CONSUMER_STAGFLATION', 'action': actions, 'info': infos, 'precedence': 'PRIORITY', 'signal_type': 'correction',
     'corrects': [tgt], 'corrects_direction': 'WEAKEN', 'confidence': 0.9, 'confidence_language': 'filing states', 'resources': 1,
     'safety_net': 'clear', 'word_count': len(body.split()), 'entities': ["America's Car-Mart", 'CRMT', 'Silver Point Finance', 'ACM Auto Trust 2024-2'],
     'event_window': 'closed', 'dispatch_note': '8-K main document read; Exhibit 10.1 unread; no owner grade.'}
with (R/bp).open('x') as f:
    f.write('---\n' + '\n'.join(k + ': ' + json.dumps(v) for k, v in h.items()) + '\n---\n\n# ' + title + '\n\n' + body + '\n')
paths = [bp]
# banner on corrected file, immediately after front matter (additive)
tp = next((R/'BOARD').glob(tgt + '-*.md')); txt = tp.read_text(); parts = txt.split('---\n', 2)
banner = f'> PARTIALLY CORRECTED — {sid}: the "reprieve through October22" date is superseded; the October21 8-K extends relief to November1 (agreed October20), adds $5M term loans, and reports the 2024-2 ABS redeemed. Direction WEAKEN for deadline urgency; the sale-talk report holds.\n\n'
tp.write_text('---\n' + parts[1] + '---\n\n' + banner + parts[2].lstrip('\n')); paths.append(str(tp.relative_to(R)))
with (W/'registry/CORRECTIONS.tsv').open('a') as f:
    csv.writer(f, delimiter='\t', lineterminator='\n').writerow(['COR-20261021-10', '2026-10-21', 'WALTER', ','.join(actions + infos), bp, '2026-11-04', 'LIVE',
        '-008 said Car-Mart lender reprieve through October22; IS through November1 per October21 8-K (agreed October20), plus $5M incremental term loans and 2024-2 ABS redeemed; sale-talk report holds', 'WEAKEN'])
with (W/'routed/route_log.tsv').open('a') as f:
    csv.writer(f, delimiter='\t', lineterminator='\n').writerow([now, sid, 'RESEARCH-INTAKE', title, 'PRIORITY', ','.join(actions), ','.join(infos), '0.9'])
for who in actions + infos:
    role = 'ACTION' if who in actions else 'INFO'
    if who in ['PROME', 'TERRY'] or (who in ['CARL', 'RED'] and role == 'INFO'):
        continue
    hp = f'AGENTS/{who}/inbox/WALTER/{sid}.md'
    with (R/hp).open('x') as f:
        f.write(f'# {sid} — {title}\nBOARD: /{bp}\nPriority: PRIORITY\nRole: {role}\nFrom: WALTER\nDate: 2026-10-21\nCorrects: {tgt}\n\n## Kernel\n' + body +
                '\n\n## Requested action\n' + ('As specified above; no new research direction.' if role == 'ACTION' else 'INFO only; no directed ask.') + '\n\n## Cross-refs\n' + bp + '\n')
    with (W/'routed/delivery_log.tsv').open('a') as f:
        csv.writer(f, delimiter='\t', lineterminator='\n').writerow([now, sid, who, role, 'CLAUDE_CODE', 'PRIORITY', hp, 'written_not_delivered_pending_push', 'Correction relay; push deferred (foreign dirty work)'])
    paths.append(hp)
(D/'correction-paths.json').write_text(json.dumps(paths, indent=2) + '\n'); print(now); print('\n'.join(paths))
