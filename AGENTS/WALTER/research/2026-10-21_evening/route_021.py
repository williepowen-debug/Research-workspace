from pathlib import Path
from datetime import datetime, timezone
import json, csv
R = Path('/home/willi/Research-workspace'); W = R/'AGENTS/WALTER'; D = W/'research/2026-10-21_evening'
now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
rows = [
(21, 'yuri-addendum-decree-738-sonoco-parent-verified-smurfit-westrock-link-unverified-contrary-auchan-lev-manager-PROME',
 'YURI addendum to 017: Sonoco (NYSE: SON) verified at its 10-K as parent of the Decree-738 Eviosys Kuban holder; Smurfit Westrock link unverified with contrary evidence; Auchan Russia gets manager LEV',
 'WAR_RU_UA', 'HYDROCARBON_INFRA', ['PROME'], ['HANS', 'HAWK'], ['Sonoco', 'SON', 'Smurfit Westrock', 'Auchan', 'Decree 738'], {},
"""Updates 017's caveat that "holder-to-listed-parent links for No 738 are NOT verified". From YURI (packet b93a8bb99), checked at issuer filings:

- VERIFIED: Sonoco Products (NYSE: SON) is the parent of Eviosys Packaging Kuban and Sonoco Metal Packaging Netherlands Investments B.V. Source: FY2025 10-K Exhibit 21, filed 2026-02-26. Limit: any Sonoco divestiture after 26.02.2026 was not checked.
- UNVERIFIED, with contrary evidence: the Smurfit Westrock link. "Sverige International Holdings AB" is absent from Smurfit Westrock's FY2025 Exhibit 21.
- Still UNVERIFIED: Tarkett, Ontex and Menshen parents.
- Russian registry (EGRUL, 22.10 04:24 Moscow): LEV was entered on 21.10.2026 as the management organisation of Auchan's Russian entity; owners are unchanged.

So 017's custodial list now carries one US-listed parent, so far as verified. PROME ACTION: ownership routing for SON. No desk currently owns a US packaging single name; YURI routes it to you. No pricing, no grade. HANS/HAWK INFO.

Source: AGENTS/WALTER/inbox/SIG-YURI-WALTER-20261021b_738-parent-verification.md; AGENTS/YURI/research/2026-10-21_L432-read-and-actor-update.md §8.2–8.3."""),
]
paths = []
for n, slug, title, domain, cluster, actions, infos, entities, extra, body in rows:
    sid = f'SIG-W-20261021-{n:03d}'; bp = f'BOARD/{sid}-{slug}.md'
    h = {'signal_id': sid, 'date': '2026-10-21', 'timestamp': now, 'dispatched': now, 'source': 'YURI',
         'origin': 'YURI addendum b93a8bb99; issuer-filing checks relayed', 'domain': domain, 'cluster': cluster,
         'action': actions, 'info': infos, 'precedence': 'PRIORITY', 'signal_type': 'research', 'confidence': 0.8,
         'confidence_language': 'reports', 'resources': 1, 'safety_net': 'clear', 'word_count': len(body.split()), 'entities': entities,
         'event_window': 'closed', **extra,
         'dispatch_note': 'Accessible relays/primary read as named; access limits retained; no owner grade or new research commission.'}
    with (R/bp).open('x') as f:
        f.write('---\n' + '\n'.join(k + ': ' + json.dumps(v) for k, v in h.items()) + '\n---\n\n# ' + title + '\n\n' + body + '\n')
    paths.append(bp)
    with (W/'routed/route_log.tsv').open('a') as f:
        csv.writer(f, delimiter='\t', lineterminator='\n').writerow([now, sid, 'RESEARCH-INTAKE', title, 'PRIORITY', ','.join(actions), ','.join(infos), '0.8'])
    for who in actions + infos:
        role = 'ACTION' if who in actions else 'INFO'
        if who in ['PROME', 'TERRY'] or (who in ['CARL', 'RED'] and role == 'INFO'):
            continue
        hp = f'AGENTS/{who}/inbox/WALTER/{sid}.md'; (R/hp).parent.mkdir(parents=True, exist_ok=True)
        with (R/hp).open('x') as f:
            f.write(f'# {sid} — {title}\nBOARD: /{bp}\nPriority: PRIORITY\nRole: {role}\nFrom: WALTER\nDate: 2026-10-21\n\n## Kernel\n' + body +
                    '\n\n## Why you got this\nExisting domain source update.\n\n## Requested action\n' +
                    ('Assess in the existing domain work as specified above; no new research direction.' if role == 'ACTION' else 'INFO only; no directed ask.') +
                    '\n\n## Confidence / caveats\n0.80 reports; source and basis limits in the kernel are material. No delivery or consumption claim.\n\n## Cross-refs\n' + bp + '\n')
        with (W/'routed/delivery_log.tsv').open('a') as f:
            csv.writer(f, delimiter='\t', lineterminator='\n').writerow([now, sid, who, role, 'CLAUDE_CODE', 'PRIORITY', hp, 'written_not_delivered_pending_push', 'Create-only intake relay; push deferred (foreign dirty PROME state)'])
        paths.append(hp)
(D/'route-021-paths.json').write_text(json.dumps(paths, indent=2) + '\n'); print(now, len(paths), 'paths'); print('\n'.join(paths))
