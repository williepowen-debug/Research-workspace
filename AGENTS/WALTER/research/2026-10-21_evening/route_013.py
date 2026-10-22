from pathlib import Path
from datetime import datetime, timezone
import json, csv
R = Path('/home/willi/Research-workspace'); W = R/'AGENTS/WALTER'; D = W/'research/2026-10-21_evening'
now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
rows = [
(13, 'eagle-bancorp-q3-npa-166m-from-113m-one-loan-is-76pct-of-inflows-provision-2point8m-nco-0point25pct-RED-REGINALD',
 'Eagle Bancorp Q3 (October21 8-K): nonperforming assets $166.0M from $113.1M, 76% of inflows from one loan; provision $2.8M vs $21.4M; NCO 0.25% vs 2.78%',
 'BANK_EARNINGS', 'BANK_COLLATERAL', ['RED', 'REGINALD'], ['LIQUID', 'CREED', 'PROME'], ['EGBN', 'Eagle Bancorp', 'EagleBank'], {},
"""From Eagle's Q3 2026 release (8-K Exhibit 99.1, accession 0001050441-26-000110, accepted October21 20:26Z, read at sec.gov): net income $24.2M / $0.79, versus Q2 $6.9M / $0.23. Almost all of the increase is the lower provision: $2.8M versus $21.4M. PPNR fell to $23.8M from $29.1M.

Asset quality moved in two directions. Nonperforming assets rose $52.9M to $166.0M (1.75% of assets) from $113.1M (1.17%). Of the $73.7M of NPL inflows, 76.0% came from a single loan migration; the release does not name the loan, property type or location. Net charge-offs fell to 0.25% annualized from 2.78%. Substandard plus special mention fell to $648.4M from $759.6M. The allowance ratio is 1.84% (from 1.83%): specific reserves are up, and the office overlay was released, with performing office coverage at 4.86% from 7.22%. CRE concentration is 245.8% from 267.6%.

Balance sheet: loans $6.6B (-1.4% q/q, income-producing CRE lower, purchased residential mortgages higher); deposits $8.0B (-$151.1M, -1.8%); brokered deposits -$348.0M; NIM 2.60% from 2.52%. CET1 14.99%. Dividend $0.01.

RED ACTION: grade CHG-027 after the October22 10:00 ET call, as PROME registered (L35). REGINALD ACTION: integrate into the Q3 cohort (EGBN ranks second in your list). The one-loan NPA jump plus the office-reserve release is the item to test on the call. LIQUID/CREED/PROME INFO. No named property, so no CREED case entry (10.8 needs a named asset).

Source: https://www.sec.gov/Archives/edgar/data/1050441/000105044126000110/finalegbnerq3-2026xearni.htm . Investor deck exhibit not read; call not yet held."""),
(14, 'southwest-q3-adj-eps-0point66-unit-revenue-plus21point6pct-fuel-3point92-q4-fuel-assumed-4point55-HENRY',
 'Southwest Q3 (October21 8-K): adjusted EPS $0.66 vs $0.50–0.75 guide; unit revenue +21.6%; fuel $3.92/gal, Q4 assumed ~$4.55',
 'VOL', 'CONSUMER_STAGFLATION', ['HENRY'], ['BRENT', 'PROME'], ['LUV', 'Southwest Airlines'], {},
"""From Southwest's Q3 2026 release (8-K Exhibit 99.1, accepted October21 20:16Z, read at sec.gov): net income $270M / $0.55 diluted; adjusted $328M / $0.66. July guidance was $0.50–0.75. Operating revenue was $8.4B (+21.2%), a Q3 record; unit revenue +21.6%, an all-time record and above guidance; adjusted operating margin 5.4% (+4.8 points y/y).

Fuel: $3.92/gal in Q3 versus a $3.70–3.75 assumption; fuel expense +$821M y/y, a $1.08 headwind to adjusted EPS. Q4 fuel is assumed at ~$4.55/gal (forward curve as of October15, including taxes and $0.05 hedge premium). Capacity: 2026 growth ~1.2%, cut from ~1.5%. Liquidity $5.6B; gross leverage 1.9x; 2026 net capex $2.5–2.75B. Capital Markets Day March2, 2027. No full-year EPS update was located in the read sections.

HENRY ACTION: resolve the terminal claim at this print (STATUS: claim resolves at LUV October21 after close; call October22 10:00 ET), per your own ledger. BRENT/PROME INFO: an airline is pricing Q4 jet fuel ~16% above Q3 actual off the October15 curve. That is an issuer assumption, not a BRENT grade.

Source: https://www.sec.gov/Archives/edgar/data/92380/000009238026000104/er-9302026xerdoc.htm ."""),
(15, 'meta-q3-capex-34point91b-2026-capex-135-145b-narrowed-up-fcf-minus-2point12b-9point89b-legal-charge-class-c-nonvoting-recap-VULCAN',
 'Meta Q3 (October21 8-K): capex $34.91B; 2026 capex $135–145B (low end raised); free cash flow −$2.12B; $9.89B legal charge; new non-voting Class C stock dividend',
 'AI_CAPEX', 'AI_INFRA_CAPEX', ['VULCAN'], ['HENRY', 'VIOLET', 'WATT', 'LIQUID', 'PROME'], ['META', 'Meta Platforms'], {},
"""From Meta's Q3 2026 release (8-K Exhibit 99.1, accession 0001628280-26-066700, accepted October21 20:03Z, read at sec.gov): revenue $64.60B (+26%); operating margin 20% versus 40%, including a $9.89B charge for the 52-attorney-general teen-mental-health settlement (up to ~$18.59B total). Ex-charge, EPS is $7.40 versus $3.83 reported.

AI-capex legs: Q3 capex including finance-lease principal was $34.91B. 2026 capex guidance is $135–145B, narrowed from $130–145B, so the low end rose $5B. Operating cash flow was $32.79B; free cash flow was -$2.12B. Cash and securities $82.45B. Full-year 2026 expenses are $175–179B. Q4 revenue is guided $73–76B. For 2027, the release gives no revenue or capex number, only "sustain strong overall revenue growth"; Reality Labs losses are guided ~$15B. Headcount is down 15% y/y. WALTER found no 2027 capex sentence, which is not the same as the call having none.

Separately (Item 1.01): the board approved, and holders approved by written consent October20, a new non-voting Class C common stock. Each A and B share receives a one-time 1:1 Class C stock dividend once the restated charter is effective January19, 2027. A Founder Alignment Agreement staples 80% of Zuckerberg's Class C sales to matching A/B sales or conversions. This is a governance/float item, not a financing event. A PRE 14C information statement was filed the same day and was not read.

VULCAN ACTION: S5/S1 legs per your rules (PROME cites S5, WQ-464): capex guide direction, the negative FCF quarter, and whether any financing is disclosed in the 10-Q or call. HENRY/VIOLET/WATT/LIQUID/PROME INFO.

Source: https://www.sec.gov/Archives/edgar/data/1326801/000162828026066700/meta-09302026xexhibit991.htm and meta-20261019.htm (Item 1.01)."""),
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
(D/'route-013-paths.json').write_text(json.dumps(paths, indent=2) + '\n'); print(now, len(paths), 'paths'); print('\n'.join(paths))
