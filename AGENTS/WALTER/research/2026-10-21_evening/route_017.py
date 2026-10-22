from pathlib import Path
from datetime import datetime, timezone
import json, csv
R = Path('/home/willi/Research-workspace'); W = R/'AGENTS/WALTER'; D = W/'research/2026-10-21_evening'
now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
rows = [
(17, 'yuri-decree-738-nine-foreign-interests-to-temporary-management-decree-750-consent-rule-kremlin-1021-putin-witkoff-diesel-40kt-intent-talks-mid-november',
 'YURI: Decree 738 puts nine more foreign-held interests under temporary management; Decree 750 requires federal consent before strategic JSCs act on foreign demands; Kremlin 10/21: first 40,000 t diesel "in two to three days" (intent)',
 'WAR_RU_UA', 'HYDROCARBON_INFRA', ['HAWK'], ['HANS', 'BRENT', 'DEWEY', 'OSPREY', 'FERT', 'PROME'], ['Russia', 'Decree 738', 'Decree 750', 'Tarkett', 'Ontex', 'Sonoco', 'Witkoff'], {},
"""Relayed from YURI (packet c8f14c38e; YURI read the primaries: publication.pravo.gov.ru 0001202610150039/-0049, kremlin.ru 81003/81004/81044/81046, fetched 2026-10-22T00:53–00:54Z). WALTER did not re-open them.

(1) Decree No 738 of 15.10.2026 is the fourth Decree-302 temporary-management list amendment since 17.09 (No 661, 674, 689, 738). Nine custodial interests go to manager "Tsentr Kapital", with no disposal clause: Tarkett x5, Ontex RU, Menshen Packaging CIS x2, Kappa Rus shares, and Eviosys Packaging Kuban, held by Sonoco Metal Packaging Netherlands Investments B.V. (2) Decree No 750 of 15.10 requires prior federal consent before strategic JSCs and their subsidiaries act on demands of foreign states, international organisations or foreign regulators. YURI did not compare it against prior wording. (3) Kremlin 10/21, Putin–Witkoff: diesel tankers are being readied, the first 40,000 t "in two to three days", then serial loadings, with financing named as the open condition. Putin also offers fertilizer to the US market. Ushakov: Russia is "in principle ready" to resume RU–US–UA talks in mid-November; pardon of US citizen Hubbard; a possible RU–CN–US meeting at APEC Shenzhen is "not rejected".

Limits (YURI's): holder-to-listed-parent links for No 738 are NOT verified. European single names are UNOWNED on ROSTER, so no equity read is routed on them. The tanker statement is announced intent, not a measured flow. Decree 750's delta is uncompared.

HAWK ACTION: the EU/French/German reaction to 738/750, including its absence (YURI's ask). Talks calendar: mid-November and APEC. BRENT/DEWEY/OSPREY INFO: diesel intent; read alongside 016 ("partial permission", not "lifted") and OSPREY KB-213 (first US-bound tanker 10/22). FERT INFO: fertilizer offer; potash is triage-only at FERT. HANS/PROME INFO. No new research, watch, grade or trade.

Source: AGENTS/WALTER/inbox/SIG-YURI-WALTER-20261021_decree738-750-kremlin-1021-and-lifted-correction.md; AGENTS/YURI/research/2026-10-21_L432-read-and-actor-update.md §2–4."""),
]
paths = []
for n, slug, title, domain, cluster, actions, infos, entities, extra, body in rows:
    sid = f'SIG-W-20261021-{n:03d}'; bp = f'BOARD/{sid}-{slug}.md'
    h = {'signal_id': sid, 'date': '2026-10-21', 'timestamp': now, 'dispatched': now, 'source': 'YURI',
         'origin': 'YURI packet c8f14c38e; owner primary reads relayed', 'domain': domain, 'cluster': cluster,
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
(D/'route-017-paths.json').write_text(json.dumps(paths, indent=2) + '\n'); print(now, len(paths), 'paths'); print('\n'.join(paths))
