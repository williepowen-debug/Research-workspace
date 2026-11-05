import csv, datetime, json
from pathlib import Path

ROOT = Path('/home/willi/Research-workspace')
W = ROOT / 'AGENTS/WALTER'
OUT = W / 'research/2026-11-04_evening-boot'
ORIGIN = 'WALTER evening boot / vendor bars / CNBC primary read'
# Pull-complete: no handoff for INFO to CARL/RED; TERRY and PROME never get one.
NO_HANDOFF_ANY = {'TERRY', 'PROME'}
NO_HANDOFF_INFO = {'CARL', 'RED'}

CARDS = [
    dict(
        n=77,
        slug='held-VLO-December-crack-below-exit-line',
        title='December ULSD crack estimates sit below the held-VLO $90.16 exit line on November 2 and 4',
        action=['TERRY', 'HENRY', 'BRENT'],
        info=['PROME', 'RED'],
        precedence='FLASH',
        signal_type='position-risk',
        confidence=0.8,
        cluster='IRAN_HORMUZ',
        domain='OIL_ENERGY',
        entities=['VLO', 'GATE-TERRY-VLO-HELD-01', 'HEN-46', 'HOZ26', 'CLZ26'],
        body='''Matched HOZ26x42 minus CLZ26, source 3 ESTIMATE (14:28-14:30 ET one-minute VWAP): November 2 $89.28, November 3 $94.29, November 4 $88.54. GATE-TERRY-VLO-HELD-01 leg A is a settlement below $90.16. Neither date is within $0.15 of the line.

November 2 vendor daily row $89.25 (HO 4.4216, CL 96.46) agrees within $0.03; its CL matches CNBC's implied close. The November 4 vendor row is the evening session (606 lots), unusable; the window CL 88.12 matches CNBC's $88.12 close. Official CME settlements NOT read.

WALTER has NOT graded the gate. No grade of either date was found; TERRY's carried reading is October 28.

ACTION TERRY: grade leg A for both dates, including what a November 2 fire means after November 3's $94.29, and write any recommendation. ACTION BRENT: supply settlements if reachable. ACTION HENRY: confirm the line and basis. The gate covers the one share filled at $412; the other two remain unresolved (D-78). Will decides; no order implied.''',
        sources='research/2026-11-04_evening-boot/crack-window-vwap.json ; crack-contracts.json ; https://www.cnbc.com/2026/11/03/oil-prices-climb-after-us-reportedly-strikes-irans-qeshm-island.html ; https://www.cnbc.com/2026/11/04/oil-price-iran-war-us-election-strait-hormuz.html',
        note='Estimate only, not a gate grade. Rule 12 Will alert carried in active session. TERRY and PROME receive through PROME orchestration, no TERRY inbox.',
        extra={},
    ),
    dict(
        n=78,
        slug='oil-falls-on-deal-hopes-no-reopening-established',
        title='Oil falls about 9% and VIX 20% on deal hopes; no deal or reopening established',
        action=['BRENT', 'FALCON', 'VIOLET', 'TERRY'],
        info=['HENRY', 'LIQUID', 'SAM', 'HAWK', 'NEXUS', 'RED', 'PROME'],
        precedence='IMMEDIATE',
        signal_type='position-risk',
        confidence=0.8,
        cluster='IRAN_HORMUZ',
        domain='OIL_ENERGY',
        entities=['Brent', 'WTI', 'VIX', 'USO', 'Hormuz', 'Vance'],
        body='''CNBC: November 4 Brent settled $94.62 (-8.7%) and WTI $88.12 (-8.3%), from $103.60 and $96.09; contract months unnamed. Oil also fell over 7% November 2. Vendor: S&P 7,688.62 (+1.58%), VIX 16.61 (-20.3%), USO 145.41, VLO 365.34.

Reported drivers, none established as cause: CNBC says Trump told the FT he has no immediate plans to strike Iran; Vance posted "The reason we lost is the war"; Lipow says the election suggests Trump may deal. Qatar is mediating; Iran's spokesman November 3 rejected "diplomacy based on coercion". CIBC: possibly overdone. Rapidan: odds still favor escalation.

NOT established: signed deal, reopening, US acceptance, transit recovery. Search-summary lines ("reopen within two days", flows near pre-war, four tankers mined) are UNVERIFIED; the primary lacks them. FT body unread. Full sweep running.

ACTION BRENT/FALCON: reassess marks. ACTION VIOLET: vol regime; RED-FT-06 exit run resets if VIXCLS confirms. ACTION TERRY: USO exposure. First settle at or below $95 of CARL's five-session line; no fire.''',
        sources='https://www.cnbc.com/2026/11/04/oil-price-iran-war-us-election-strait-hormuz.html ; https://www.cnbc.com/2026/11/03/oil-prices-climb-after-us-reportedly-strikes-irans-qeshm-island.html ; FT locator unread https://www.ft.com/content/b526f876-810a-4e74-8b8d-4ffca04b29c7',
        note='Routed before the full sweep per decay-rate precedence; causal language is reported, not graded. CARL dropped: Brent five-session line not met.',
        extra={'anchor_unverified_as_of': '2026-10-29', 'narrative_channel': 'potus'},
    ),
]


def main():
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    paths = []
    for d in CARDS:
        sid = f"SIG-W-20261104-{d['n']:03d}"
        rel = f"BOARD/{sid}-{d['slug']}.md"
        p = ROOT / rel
        assert not p.exists(), p
        body = '# ' + d['title'] + '\n\n' + d['body'] + '\n\nSources: ' + d['sources'] + '\n'
        wc = len(d['body'].split())
        assert wc <= 200, (sid, wc)
        conf = d['confidence']
        h = dict(
            signal_id=sid, timestamp=stamp, dispatched=stamp, source='WALTER', origin=[ORIGIN],
            action=d['action'], info=d['info'], precedence=d['precedence'], signal_type=d['signal_type'],
            confidence=conf, confidence_language='reports', resources=1, safety_net='clear',
            cluster=d['cluster'], domain=d['domain'], entities=d['entities'], word_count=wc,
            dispatch_note=d['note'], **d['extra'],
        )
        p.write_text('---\n' + ''.join(k + ': ' + json.dumps(v) + '\n' for k, v in h.items()) + '---\n' + body)
        paths.append(rel)
        with (W / 'routed/route_log.tsv').open('a') as f:
            csv.writer(f, delimiter='\t', lineterminator='\n').writerow(
                [stamp, sid, ORIGIN, d['title'], d['precedence'], ','.join(d['action']), ','.join(d['info']), conf])
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
                    f"# {sid} — {d['title']}\nBOARD: /{rel}\nPriority: {d['precedence']}\nRole: {role}\nFrom: WALTER\nDate: 2026-11-04\n\n"
                    f"## Kernel\n{d['body']}\n\n## Why you got this\n{name}: {role} on the canonical recipient line.\n\n"
                    f"## Requested action\n{ask}\n\n## Confidence / caveats\n{conf}; source dates and limits retained above. Written is not delivered or consumed.\n\n"
                    f"## Cross-refs\n/{rel}\nSources: {d['sources']}\n")
                paths.append(hr)
                with (W / 'routed/delivery_log.tsv').open('a') as f:
                    csv.writer(f, delimiter='\t', lineterminator='\n').writerow(
                        [stamp, sid, name, role, 'CC', d['precedence'], hr, 'written_not_delivered_pending_push',
                         'Claude-authored; publication and owner consumption unverified.'])
    (OUT / 'dispatch-paths.json').write_text(json.dumps(paths, indent=2) + '\n')
    print(stamp, len(CARDS), 'cards', len(paths) - len(CARDS), 'handoffs')


if __name__ == '__main__':
    main()
