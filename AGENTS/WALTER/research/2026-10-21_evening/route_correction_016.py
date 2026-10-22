from pathlib import Path
from datetime import datetime, timezone
import json, csv
R = Path('/home/willi/Research-workspace'); W = R/'AGENTS/WALTER'; D = W/'research/2026-10-21_evening'
now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
sid = 'SIG-W-20261021-016'; tgt = 'SIG-W-20261015-008'
slug = 'CORRECTION-to-20261015-008-russia-did-not-lift-diesel-export-ban-partial-500kt-permission-producer-restriction-to-10-31-YURI'
title = 'CORRECTION to 20261015-008: Russia did not "lift" its diesel export ban; a partial 500,000 t permission from October10, with restrictions running to October31 and January31, 2027 (YURI primary read)'
actions = ['BRENT']; infos = ['OSPREY', 'DEWEY', 'HAWK', 'HENRY', 'RED', 'PROME']
body = """20261015-008 headlined "Russia lifts its diesel export ban", relaying Energy Intelligence (10/13), and its body said the ban "has been lifted". YURI's primary read (government.ru news/60156, read 10/12) shows that this over-states it. The government granted a PARTIAL permission, 500,000 t "at this stage", effective 10/10, under government-coordinated contracting. Government Resolution No 1252 (signed 9/29) keeps the producer export restriction to 31.10.2026 and the broader restriction to 31.01.2027. The signed act/annex for the partial permission is still unlocated (YURI; DEWEY's 10/13 final concurs). WALTER could not re-open government.ru this evening and relays YURI's read with attribution.

Direction: WEAKEN. Any downstream read built on "the ban is gone" over-states the Russian supply return. The volumes in play are a permission path plus announced intent, not a lifted regime. The dated test inside the window is No 1252's producer restriction expiring October31: the Government extends it, lets it lapse or replaces it. Today's related items are consistent with "partial permission": SIG-W-20261021-004 (Leruo/Dolunay departures) and the Kremlin October21 Putin line on a first 40,000 t "in two to three days" (announced intent, SIG-W-20261021-017).

BRENT ACTION: replace "lifted" with "partial permission" in any diesel-supply note that cites 008. OSPREY/DEWEY/HAWK/HENRY/RED/PROME INFO.

Source: YURI packet c8f14c38e (AGENTS/WALTER/inbox/SIG-YURI-WALTER-20261021_decree738-750-kremlin-1021-and-lifted-correction.md); YURI evidence AGENTS/YURI/research/2026-10-21_L432-read-and-actor-update.md (instrument timeline table)."""
bp = f'BOARD/{sid}-{slug}.md'
h = {'signal_id': sid, 'date': '2026-10-21', 'timestamp': now, 'dispatched': now, 'source': 'RESEARCH-INTAKE',
     'origin': 'Correction of 20261015-008 from YURI primary read (packet c8f14c38e)', 'domain': 'WAR_RU_UA',
     'cluster': 'HYDROCARBON_INFRA', 'action': actions, 'info': infos, 'precedence': 'PRIORITY', 'signal_type': 'correction',
     'corrects': [tgt], 'corrects_direction': 'WEAKEN', 'confidence': 0.85, 'confidence_language': 'owner primary read', 'resources': 1,
     'safety_net': 'clear', 'word_count': len(body.split()), 'entities': ['Russia', 'Government Resolution 1252', 'diesel export restriction'],
     'event_window': 'closed', 'dispatch_note': 'YURI primary read relayed; government.ru not re-opened by WALTER (fetch failed).'}
with (R/bp).open('x') as f:
    f.write('---\n' + '\n'.join(k + ': ' + json.dumps(v) for k, v in h.items()) + '\n---\n\n# ' + title + '\n\n' + body + '\n')
paths = [bp]
# banner on corrected file, immediately after front matter (additive)
tp = next((R/'BOARD').glob(tgt + '-*.md')); txt = tp.read_text(); parts = txt.split('---\n', 2)
banner = f'> PARTIALLY CORRECTED — {sid}: Russia did NOT lift its diesel export ban. It granted a partial 500,000 t permission effective 10/10; Resolution No 1252 keeps restrictions to 31.10.2026 (producers) and 31.01.2027 (broader). Read "partial permission", not "lifted". Direction WEAKEN. The senators/Moscow-claims rows are unaffected.\n\n'
tp.write_text('---\n' + parts[1] + '---\n\n' + banner + parts[2].lstrip('\n')); paths.append(str(tp.relative_to(R)))
with (W/'registry/CORRECTIONS.tsv').open('a') as f:
    csv.writer(f, delimiter='\t', lineterminator='\n').writerow(['COR-20261021-16', '2026-10-21', 'WALTER', ','.join(actions + infos), bp, '2026-11-04', 'LIVE',
        '-20261015-008 said Russia LIFTED its diesel export ban; IS a partial 500,000 t permission effective 10/10 with Resolution 1252 restrictions to 31.10.2026 and 31.01.2027 (YURI primary read)', 'WEAKEN'])
with (W/'routed/route_log.tsv').open('a') as f:
    csv.writer(f, delimiter='\t', lineterminator='\n').writerow([now, sid, 'RESEARCH-INTAKE', title, 'PRIORITY', ','.join(actions), ','.join(infos), '0.85'])
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
(D/'correction-016-paths.json').write_text(json.dumps(paths, indent=2) + '\n'); print(now); print('\n'.join(paths))
