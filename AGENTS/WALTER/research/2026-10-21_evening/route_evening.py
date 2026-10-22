from pathlib import Path
from datetime import datetime, timezone
import json, csv
R = Path('/home/willi/Research-workspace'); W = R/'AGENTS/WALTER'; D = W/'research/2026-10-21_evening'
now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
rows = [
(7, 'saudi-moe-shaybah-drone-intercepted-debris-kills-two-outside-perimeter-operations-unaffected-houthi-yanbu-shaybah-claims-CLAIM-ONLY-FALCON-BRENT',
 'Saudi MoE: drone aimed at a Shaybah field facility intercepted October21; debris killed two outside the perimeter, operations unaffected',
 'WAR_IRAN_GULF', 'IRAN_HORMUZ', ['FALCON', 'BRENT'], ['HENRY', 'RED', 'PROME'], ['Saudi Ministry of Energy', 'Aramco', 'Shaybah', 'Yanbu', 'Houthis'],
 {'anchor_unverified_as_of': '2026-10-15'},
'''The Saudi Ministry of Energy said on October21 (morning, local time) that air defences INTERCEPTED a drone aimed at a facility at Aramco's Shaybah oil field. Falling debris set fire to a contractor vehicle OUTSIDE the facility perimeter; two residents (one Filipino, one Nepali) were killed and two (one Pakistani, one Indian) injured. The ministry said field operations were not affected and named no attacker. Two independent relays of the same ministry statement were read: AAP (with AP/DPA material, first published 2026-10-22 8:05am page-local time) and SBS News (2026-10-22 06:37 page-local time). The ministry text itself and Saudi Gazette were not readable (402/403).

What this is not: an intercept with debris outside the perimeter is not, on the ministry wording, a hostile strike on the production facility. WALTER does not grade FAL-01 or the production rung D85->92 (FALCON's letter: counting source confirming BOTH a hostile strike AND a production-class facility). Guards applied: carry INTERCEPTED, never "struck" (intercepted->struck retelling class); do not merge with the August 2019 Shaybah attack, which recirculates in search results.

Separate, earlier and CLAIM-ONLY: TASS (Doha dateline October19, via Saree's Telegram) reports Houthi claims of six operations in 48 hours, including Aramco facilities in Yanbu and fires at Shaybah, plus Riyadh, Abha and Khamis Mushait. No Saudi confirmation found for those claims. A lane headline on October21 14:18Z ("Aramco's Yanbu site said to be without damage", Breakingthenews.net) was not readable; body and basis unknown. Do not merge the October19 claim with the October21 ministry event.

FALCON ACTION: grade the October21 Shaybah event against the production rung and the casualty ratchet (two killed). FALCON's own 7-day mark review was due October21; its STATUS was last updated October14. BRENT ACTION: supply relevance, given operations reported unaffected. HENRY/RED/PROME INFO. No fresh full theater sweep was done here; last full sweep 2026-10-15, next due ~10/22.

Source: RESEARCH-INTAKE October21 lane (Yanbu headline) led to WALTER search. Read: https://www.illawarramercury.com.au/story/9373075/two-killed-after-drone-intercepted-near-saudi-oil-field/ ; https://news.sbs.co.kr/english/article.do?news_id=N1008809301 ; https://tass.com/world/2204325 .'''),
(8, 'car-mart-sale-talks-bloomberg-chapter-11-or-shareholder-vote-lender-reprieve-through-10-22-explains-10-20-drop-BROCK-OTTO',
 "Bloomberg October20: America's Car-Mart and lenders negotiating a sale via Chapter 11 or a shareholder vote; reprieve runs through October22",
 'SUBPRIME_AUTO', 'CONSUMER_STAGFLATION', ['BROCK', 'OTTO'], ['LIQUID', 'CARL', 'PROME'], ["America's Car-Mart", 'CRMT', 'Silver Point Capital'], {},
'''Bloomberg reported on October20 (Yahoo syndication stamped 15:53 ET; byline Luke Juricic) that America's Car-Mart (CRMT) and its lenders are negotiating a sale that would keep the dealer operating. The two structures under discussion are a court-supervised Chapter 11 sale or a traditional shareholder vote. Talks are ongoing and no decision has been made, per people familiar. Lenders granted another weeklong reprieve through October22. The report restates the June default on the $300M Silver Point term loan. No buyer is named and no company comment is carried.

Why it matters now: BROCK STATUS (October21 08:59 ET) records CRMT at $0.79, down 26.17% on October20, with "no filing explains it". This report, published during that session (shares down ~16% intraday at the time), is a plausible news explanation. WALTER does not establish that it caused the move. The reprieve date is tomorrow's existing BROCK read (seventh-bridge STD, L740).

BROCK ACTION: fold the sale-talk report into the October22 CRMT read. Keep reported talks separate from any filing; a Chapter 11 path is reported as one option, not a decision. OTTO ACTION: the V9 lender-standstill vector; OTTO re-colours only after BROCK's grade, per its own rule. LIQUID/CARL/PROME INFO.

Source: RESEARCH-INTAKE October21 lane (Automotive News/Bloomberg Law headlines). Read: https://finance.yahoo.com/markets/stocks/articles/america-car-mart-sale-talks-195309013.html (Bloomberg syndication). The original Bloomberg article was not read directly; the EDGAR feed was not re-checked for an October21 8-K.'''),
(9, 'zions-q3-nco-3m-0point02pct-classified-down-204m-cre-nonaccrual-up-q2-eps-was-visa-gain-REGINALD',
 'Zions Q3 (October19 8-K): net charge-offs $3M (0.02%), classified loans down $204M, CRE nonaccrual up to $40M; Q2 EPS was inflated by securities gains',
 'BANK_EARNINGS', 'BANK_COLLATERAL', ['REGINALD'], ['LIQUID', 'RED', 'PROME'], ['ZION', 'Zions Bancorporation'], {},
'''From Zions' Q3 2026 earnings release (8-K Exhibit 99.1, released October19, read at sec.gov): net earnings $262M / diluted EPS $1.78, versus Q2 $452M / $3.05 and Q3 2025 $221M / $1.48. The sequential drop is mostly Q2's $269M of securities gains (Visa Class B-1 sale, SBIC marks); Q3 securities were a $4M loss. Do not read the EPS fall as credit deterioration.

Credit: net charge-offs $3M (0.02% annualized), versus $9M (0.06%) in Q2. Nonperforming assets $315M (0.50%), versus $298M (0.48%). Classified loans $2.1B (3.40%), down $204M from Q2, mainly lower classified CRE from payoffs. The allowance ratio is 1.11% (Q2 1.13%) with an $8M provision benefit; part of the allowance decline was lower CRE-specific reserves. CRE nonaccrual is $40M, up from $34M. Total deposits are $77.9B (+$1.3B q/q); noninterest-bearing deposits are $26.4B (+1% q/q). NIM is 3.23% (Q2 3.27%). Loans are flat on payoffs and competition. The release has no specific office disclosure.

REGINALD ACTION: integrate into the existing Q3 regional cohort (ZION is in REGINALD's ranked list). One mild adverse item: CRE nonaccrual up while the CRE allowance was released. This is clean-credit counterevidence for the quarter, not a cohort verdict. WAL's own Q3 is already on BOARD (SIG-W-20261019-019..021). LIQUID/RED/PROME INFO.

Source: RESEARCH-INTAKE critical 8-K (ZION, October19, items 2.02/9.01). Read: https://www.sec.gov/Archives/edgar/data/0000109380/000010938026000125/exh991earningsrelease20260.htm . Call transcript not read.'''),
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
(D/'route-paths.json').write_text(json.dumps(paths, indent=2) + '\n'); print(now, len(paths), 'paths'); print('\n'.join(paths))
