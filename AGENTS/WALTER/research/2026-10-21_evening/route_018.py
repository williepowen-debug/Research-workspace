from pathlib import Path
from datetime import datetime, timezone
import json, csv
R = Path('/home/willi/Research-workspace'); W = R/'AGENTS/WALTER'; D = W/'research/2026-10-21_evening'
now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
rows = [
(18, 'softbank-9984-down-25pct-oct8-to-oct22-vendor-closes-ai-financing-stress-bookmark-claim-checked-VULCAN-SAM',
 'SoftBank (9984.T) fell from ¥6,040 (Oct 8) to ¥4,505 (Oct 22 close), about -25%; the bookmark claim checks on price, its $164B debt figure is unverified',
 'AI_CAPEX', 'AI_INFRA_CAPEX', ['VULCAN'], ['SAM', 'LIQUID', 'HENRY', 'PROME'], ['SoftBank', '9984.T', 'OpenAI'], {},
"""Will-bookmarked post (Bull Theory, October19): "SoftBank's debt crisis is growing… down -25% in just the last 7 trading sessions… $164 billion in debt as of June 2026". WALTER checked price only. Vendor daily closes (yfinance 9984.T, Tokyo session): 10/08 ¥6,040 · 10/09 ¥5,803 · 10/13 ¥5,310 · 10/14 ¥5,351 · 10/15 ¥4,852 · 10/16 ¥4,944 · 10/19 ¥4,845 · 10/20 ¥4,554 · 10/21 ¥4,622 · 10/22 ¥4,505. That is -25.4% over 10/08→10/22, and -16.5% over the 7 sessions 10/09→10/19 the post likely means. The direction and rough magnitude hold; the exact "7-session -25%" depends on the window.

The $164B June debt figure and the interest-cost line are UNVERIFIED (truncated post; no filing read). Background (search, September): a 9/14 drop of 13% after AI-lab safety remarks; ~$11B bonds 9/21 to fund the OpenAI payment; reports that lenders declined an OpenAI-stake-collateral loan. All are secondary.

VULCAN ACTION: S5 (AI-infra financing) is the natural home. Does a >25% drawdown in the largest leveraged AI-equity holdco change any registered leg? Per SAM's own KB (June), SoftBank stress transmits via equities and credit, not sovereign bonds. SAM/LIQUID/HENRY/PROME INFO.

Source: bookmark 2112031408600621159 (public oEmbed text; chart image not read); vendor closes pulled 2026-10-22T01:3xZ, not exchange-certified."""),
(19, 'edmunds-q3-record-21point2pct-new-car-payments-over-1000-avg-787-84-month-loans-25point5pct-OTTO-CARL',
 'Edmunds Q3: a record 21.2% of financed new-car buyers pay $1,000+/month (19.1% a year ago); average payment $787; 84-month-plus loans 25.5%',
 'SUBPRIME_AUTO', 'CONSUMER_STAGFLATION', ['OTTO'], ['CARL', 'LIQUID', 'PROME'], ['Edmunds', 'auto loans'], {},
"""Will-bookmarked post (unusual_whales via CNBC, October18), checked against multiple outlets reporting Edmunds' Q3 2026 data. 21.2% of financed new-vehicle purchases carried payments of $1,000+ per month: a record, against 20.3% in Q2 and 19.1% in Q3 2025. Motor1 prints 21.1% in one passage. The average new-car payment is $787 (Q2 $777, Q3 2025 $756). Loans of 84+ months are 25.5% of financed new purchases. Lifetime interest is a record $9,938; average APR 7.0%. Used-vehicle buyers at $1,000+ are 6.5%, also a record. The post's "69% took loans of six years or longer" was not matched to an Edmunds line.

A second bookmark (unusual_whales, October19) cites Reuters for "$1.7T auto loan market headed for a crash" and "1 in 5 Americans behind on at least one loan, highest since 2010". The Reuters piece was not located or read, so that framing stays unverified. Do not route it as Reuters' finding.

OTTO ACTION: affordability/term-stretch leg, new-car prime-heavy perimeter (not a subprime delinquency print). CARL/LIQUID/PROME INFO.

Source: Edmunds Q3 coverage via https://www.click2houston.com/news/local/2026/10/19/new-car-payments-hit-record-787-a-month-as-buyers-take-on-longer-loans-report-finds/ and autoremarketing/motor1 relays (search results); Edmunds' own release not opened."""),
(20, 'jefferies-iphone-18-pro-demand-weakening-delivery-times-resale-second-sign-after-parts-cut-VULCAN',
 'Jefferies (via unusual_whales, October19): iPhone 18 Pro/Pro Max demand weakening on shorter delivery times and falling resale prices; a second soft-demand sign after the reported parts cut',
 'AI_CAPEX', 'AI_INFRA_CAPEX', ['VULCAN'], ['HENRY', 'PROME'], ['Apple', 'Jefferies', 'iPhone 18'], {},
"""Will-bookmarked post (unusual_whales, October19, truncated): Jefferies says demand for iPhone 18 Pro and Pro Max is weakening; the tells are shorter delivery lead times and falling resale prices. The post calls it the second soft-demand sign this month, after reports that Apple told suppliers to cut production of some parts. VULCAN already carries that parts cut as KB-VULCAN-205 (>=15% iPhone 18 Pro cut, single-sourced relay). The Jefferies note itself was not read; this is a relay of a sell-side read.

VULCAN INFO-plus: a possible n+1 on the handset-demand leg feeding memory demand (KB-205/221: Samsung MX component cut). It is not independent confirmation until the Jefferies note or the lead-time data are read. HENRY/PROME INFO.

Source: bookmark 2112186254729384413 (public oEmbed text)."""),
]
paths = []
for n, slug, title, domain, cluster, actions, infos, entities, extra, body in rows:
    sid = f'SIG-W-20261021-{n:03d}'; bp = f'BOARD/{sid}-{slug}.md'
    h = {'signal_id': sid, 'date': '2026-10-21', 'timestamp': now, 'dispatched': now, 'source': 'X_BOOKMARKS',
         'origin': 'Bookmark batches 12-16 (stage 94), public oEmbed text; claims checked by WALTER', 'domain': domain, 'cluster': cluster,
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
(D/'route-018-paths.json').write_text(json.dumps(paths, indent=2) + '\n'); print(now, len(paths), 'paths'); print('\n'.join(paths))
