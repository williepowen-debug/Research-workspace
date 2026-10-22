from pathlib import Path
from datetime import datetime, timezone
import json, csv
R = Path('/home/willi/Research-workspace'); W = R/'AGENTS/WALTER'; D = W/'research/2026-10-21_evening'
now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
rows = [
(12, 'ukmto-174-to-180-mapped-to-imo-names-al-dasma-is-the-bukha-event-not-two-hulls-soyia-is-al-faw-FALCON',
 'UKMTO 174-26 to 180-26 mapped to IMO names: AL DASMA is the 10/21 Bukha event (179-26), not two hulls; Al-Faw is SOYIA (180-26)',
 'WAR_IRAN_GULF', 'IRAN_HORMUZ', ['FALCON'], ['HAWK', 'BRENT', 'PROME'], ['UKMTO', 'ST3', 'LOYALTY', 'AL KHARSAAH', 'JIF BARRACUDA', 'AL DASMA', 'SOYIA'],
 {'anchor_unverified_as_of': '2026-10-15'},
"""FALCON requested this pull (VESSELS gap). A WALTER read-only helper mapped the seven UKMTO products issued after 173-26 up to 2026-10-22T00:43Z. UKMTO's own text names no hull, and ukmto.org plus every per-number PDF returned 403, so every name is NAMED-BY-SECONDARY: the IMO incident board, NAVAREA IX, Clearwater and wires.

174-26 ST3 (IMO 9220964), projectile, 68 NM NE Al Jubayl, 16 Oct. 175-26 LOYALTY (9182306), RPG from a small boat, 78 NM NE Al Jubayl, 16 Oct 1922Z. 176-26 AL KHARSAAH (9360881), LNG tanker, skiff shots exchanged, Gulf of Aden 17 Oct; Clearwater only, bearing SW vs SE conflict. 177-26 JIF BARRACUDA (9345506), tug, NE Khor Fakkan, 18 Oct; FALCON's inference is upgraded to named-by-secondary. 178-26 ADVISORY, tanker "interaction" ~121 NM E of Duqm, 19 Oct, hull UNKNOWN. 179-26 AL DASMA (9653446), ~11 NM W Bukha, fire out. 180-26 SOYIA (9263916), ~30 NM SE Al Faw, event 20 Oct 1830Z, reported late.

Count consequence: FALCON's "AL DASMA struck 10/20" and the "10/21 tanker off Bukha" are very probably ONE event (179-26). NAVAREA 393/26 matches the UKMTO clock and offset; do not count two hulls. The date is unresolved: UKMTO says 21 Oct 0145Z, IMO/NAVAREA 396/26 say 20 Oct. No 181-26 had appeared. The "at least 10 vessels attacked in 7 days to 10/17" figure carried in -20261018-002 has no UKMTO text located; treat it as relayed. Unnumbered items (Basrah STS four projectiles, IRGC mine claims 20-21 Oct) have no UKMTO number or named hull and stay CLAIM/industry-only.

FALCON ACTION: reconcile VI-0078/0079 and the AL DASMA row against 179/180, keeping the date conflict open. HAWK/BRENT/PROME INFO. No grade, gate or count is set by WALTER.

Evidence: AGENTS/WALTER/research/2026-10-21_evening/ukmto-174-onward.md (table, lead verdicts, gaps, source access log)."""),
]
paths = []
for n, slug, title, domain, cluster, actions, infos, entities, extra, body in rows:
    sid = f'SIG-W-20261021-{n:03d}'; bp = f'BOARD/{sid}-{slug}.md'
    h = {'signal_id': sid, 'date': '2026-10-21', 'timestamp': now, 'dispatched': now, 'source': 'RESEARCH-INTAKE',
         'origin': 'October21 lane 4e5ec36; dated source bodies read by WALTER October21 evening ET', 'domain': domain, 'cluster': cluster,
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
(D/'route-012-paths.json').write_text(json.dumps(paths, indent=2) + '\n'); print(now, len(paths), 'paths'); print('\n'.join(paths))
