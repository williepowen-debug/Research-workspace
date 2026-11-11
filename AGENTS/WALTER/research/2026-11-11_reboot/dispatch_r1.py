import sys, csv, datetime, json
from pathlib import Path
ROOT = Path('/home/willi/Research-workspace')
W = ROOT / 'AGENTS/WALTER'
NO_HANDOFF_ANY = {'TERRY', 'PROME'}
NO_HANDOFF_INFO = {'CARL', 'RED'}

def send(cards):
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    paths = []
    for d in cards:
        sid = f"SIG-W-20261111-{d['n']:03d}"
        rel = f"BOARD/{sid}-{d['slug']}.md"
        p = ROOT / rel
        assert not p.exists(), p
        body = '# ' + d['title'] + '\n\n' + d['body'] + '\n\nSources: ' + d['sources'] + '\n'
        wc = len(d['body'].split())
        assert wc <= (200 if d['precedence'] in ('FLASH', 'IMMEDIATE') else 500), (sid, wc)
        h = dict(signal_id=sid, date='2026-11-11', timestamp=stamp, dispatched=stamp, source=d.get('source', 'WALTER'),
                 origin=[d['origin']], action=d['action'], info=d['info'], precedence=d['precedence'],
                 signal_type=d['signal_type'], confidence=d['confidence'], confidence_language=d.get('lang', 'reports'),
                 resources=1, safety_net='clear', cluster=d['cluster'], domain=d['domain'], entities=d['entities'],
                 word_count=wc, dispatch_note=d['note'], **d.get('extra', {}))
        p.write_text('---\n' + ''.join(k + ': ' + json.dumps(v) + '\n' for k, v in h.items()) + '---\n' + body)
        paths.append(rel)
        with (W / 'routed/route_log.tsv').open('a') as f:
            csv.writer(f, delimiter='\t', lineterminator='\n').writerow(
                [stamp, sid, d['origin'], d['title'], d['precedence'], ','.join(d['action']), ','.join(d['info']), d['confidence']])
        for role, names in (('ACTION', d['action']), ('INFO', d['info'])):
            for name in names:
                if name in NO_HANDOFF_ANY or (role == 'INFO' and name in NO_HANDOFF_INFO):
                    continue
                if name in d.get('owner_delivered', set()):
                    continue  # DEWEY wrote the create-only copy (CHECKLIST 2.8b step 4); no duplicate
                hr = f'AGENTS/{name}/inbox/WALTER/{sid}.md'
                hp = ROOT / hr
                assert not hp.exists(), hp
                hp.parent.mkdir(parents=True, exist_ok=True)
                ask = d.get('asks', {}).get(name) or ('Apply only the owner work named above; no new study or launch authorized.' if role == 'ACTION' else 'Context only; no directed ask.')
                hp.write_text(
                    f"# {sid} — {d['title']}\nBOARD: /{rel}\nPriority: {d['precedence']}\nRole: {role}\nFrom: WALTER\nDate: 2026-11-11\n\n"
                    f"## Kernel\n{d['body']}\n\n## Why you got this\n{name}: {role} on the canonical recipient line.\n\n"
                    f"## Requested action\n{ask}\n\n## Confidence / caveats\n{d['confidence']}; source dates and limits retained above. Written is not delivered or consumed.\n\n"
                    f"## Cross-refs\n/{rel}\nSources: {d['sources']}\n")
                paths.append(hr)
                with (W / 'routed/delivery_log.tsv').open('a') as f:
                    csv.writer(f, delimiter='\t', lineterminator='\n').writerow(
                        [stamp, sid, name, role, 'CC', d['precedence'], hr, 'written_not_delivered_pending_push',
                         'Claude-authored; publication and owner consumption unverified.'])
    return stamp, paths

CARDS = [
dict(n=16, slug='MARCO-ENR-02-SUSTAINED-CPI-airline-fares-plus-23.27pct-2yr-October-plus-26.36pct-September-energy-to-fare-stage-live-Spirit-co-driver-national-not-Florida',
 title="MARCO ENR-02 SUSTAINED: CPI airline fares +23.27% over two years in October and +26.36% in September, both above MARCO's +20.0% line; the energy-to-airfare stage of MARCO's Florida channel is live into the winter booking window; Spirit's May liquidation is a co-driver; national series, Florida demand not graded",
 body="""MARCO's pre-registered `ENR-02` (letter of 9/24) graded SUSTAINED on its second leg (KB-MARCO-ENR-38):

| Series | BLS CPI-U Airline fares, US city average, NSA, `CUUR0000SETG01` |
|---|---|
| October 2026 vs October 2024 | 327.822 vs 265.939 = **+23.27%** (no October 2025 value, 2025 lapse) |
| September 2026 vs September 2024 | 315.948 vs 250.03 = +26.36% (leg 1, graded 10/14) |
| September → October | +3.76% NSA (2013–24 median +3.34%) |

**Registered consequence:** the energy-to-Florida channel is live at the fare stage going into the winter 2026–27 booking window.

**Spirit confound, verbatim from MARCO:** "Not all fuel: Spirit's 5/2 liquidation is a co-driver after May (April +20.71% predates it). National series, not FL. The FL-demand stage is not graded here."

**Not established:** any Florida visitor or dollar decline; Florida airport demand stays CONFOUNDED. Fare stage only.

**Asks:** CARL — fold into the consumer and inflation read; REGINALD — Florida-bank tourism exposure at the fare stage only. TERRY already has MARCO's tradeability packet (c6c2d14dca).""",
 sources="AGENTS/WALTER/inbox/2026-11-11_from-MARCO_ENR-02-sustained-for-REGINALD-CARL.md (c39c07201c) ; AGENTS/MARCO/workbook/KB.tsv KB-MARCO-ENR-38 ; BLS data.bls.gov series CUUR0000SETG01, read by MARCO 11/11 about 10:25 ET (WALTER's BLS API call refused 15:34:57Z, daily limit; ratio 327.822/265.939 reproduced by WALTER)",
 origin='MARCO packet 11/11 (registered ENR-02 fire)', source='MARCO',
 action=['CARL', 'REGINALD'], info=['CORAL', 'HENRY', 'RED', 'TERRY'],
 precedence='IMMEDIATE', signal_type='threshold-crossed', confidence=0.85, lang='reports',
 cluster='CONSUMER_STAGFLATION', domain='MACRO_INFLATION', entities=['MARCO ENR-02', 'CPI airline fares', 'CUUR0000SETG01', 'Spirit Airlines', 'Florida'],
 note="Owner-registered threshold (MARCO ENR-02) graded SUSTAINED by its owner; MARCO asked WALTER to route to REGINALD and CARL under the 9/24 letter. MACRO_INFLATION row: CARL action; REGINALD action per the registered consequence; CORAL info under the Florida carve-out (channel is Florida's, demand stage not graded); HENRY, RED info. TERRY BOARD-only (MARCO sent TERRY directly). threshold-crossed default IMMEDIATE (OVERLAYS By Signal Type); not a WALTER-scanned registry, no WALTER fire-log row. Figures are MARCO's read of data.bls.gov; WALTER's BLS API call hit the daily limit, arithmetic reproduced.",
 extra=dict(threshold_ref='MARCO ENR-02 (AGENTS/MARCO/workbook/FLOW FLOW-ENR-01)', event_window='open')),

dict(n=17, slug='DEWEY-Citi-completes-modified-card-peer-check-North-America-30plus-share-18.59-to-19.08pct-does-not-reproduce-Capital-One-jump',
 title="DEWEY research-output: Citi completes the modified-card peer comparison; Citi North America's 30+ day delinquent share of modified card loans rose 18.59% to 19.08% (+0.49 pp) June to September, so Citi does not reproduce Capital One's roughly 7.9-point jump; all six peers stay within about one point; Capital One's cause still UNKNOWN",
 body="""DEWEY research-output, DOCKET L923 under Will's four-lender approval (reaffirmed November 4 21:12 ET); report `AGENTS/DEWEY/output/2026-11-11_citi-modified-card-peer-completion.md`, commit e14527103e. Continues card SIG-W-20261104-080.

**Verdict:** Citi does not reproduce Capital One's Q3 jump in the delinquent share of recently modified card loans.

| Citi North America cards, $M | June 30 | September 30 |
|---|---:|---:|
| Modified group outstanding | 1,555 | 1,630 |
| 30–89 days past due | 185 | 210 |
| 90+ days past due | 104 | 101 |
| 30+ share (derived) | 18.59% | 19.08% (+0.49 pp) |
| Q3 new modifications | 452 (Q2) | 541 (+19.7% q/q, +15.8% y/y vs 467) |
| Modified then defaulted in quarter (60+ dpd at Citi) | 87 (Q2) | 93 |

Outside North America kept separate ($36M to $38M, 16.67% to 15.79%).

**DEWEY's limits, kept:** Citi's perimeter includes Canada and Puerto Rico, not Capital One's domestic book; Citi re-ages modified loans to current, so the share reflects program mechanics as well as repayment; these are rolling 12-month groups, not the same borrowers; definitions differ by issuer, so **do not rank share levels as a credit-quality league table**. The other five peers are carried from November 4, not re-pulled. More modifications at Citi means assistance needs are not flat.

**Do not relay as:** proof only Capital One has stress, modification-caused deterioration, hidden delinquency, a pooled default rate, or a trade recommendation.

**Per recipient:** CARL — the Citi leg of your peer comparison is complete; cause interpretation stays yours. TERRY — tradeability read under Will's standing direction; a reasoned NO CARD is an answer (your Capital One NO CARD, 6283242a8c, predates this). GIBBS — Citi and Capital One are in your 16; context only.""",
 sources="AGENTS/DEWEY/output/2026-11-11_citi-modified-card-peer-completion.md (e14527103e) ; Citi Q3 2026 10-Q Note 12 p.139 https://www.sec.gov/Archives/edgar/data/831001/000083100126000056/c-20260930.htm (via DEWEY's hashed extract research/2026-11-11_citi/20260930-tables.json, sha256 4bf538c7…, table 169) ; Citi Q2 2026 10-Q ; BOARD/SIG-W-20261104-080",
 origin='DEWEY research-output / DOCKET L923', source='DEWEY',
 action=['CARL', 'TERRY'], info=['GIBBS', 'RED'], owner_delivered={'CARL', 'TERRY'},
 precedence='PRIORITY', signal_type='research', confidence=0.9, lang='reports',
 cluster='CONSUMER_STAGFLATION', domain='CONSUMER_CREDIT', entities=['Citi', 'Citigroup', 'Capital One', 'COF', 'modified card loans', 'DOCKET L923'],
 note="Phase 2.8b return. Quality gate: Citi table 169 row (1,630 / 1,319 / 210 / 101) checked in DEWEY's hashed extract of the SEC 10-Q (WALTER's own SEC fetch refused 403 with a generic agent; Will's identifier not used, MEMORY #59); 311/1,630 = 19.08% and 289/1,555 = 18.59% reproduced. No conflict with CARL or TERRY records (TERRY's Capital One NO CARD predates this). DEWEY wrote the CARL and TERRY copies; GIBBS backfilled INFO; RED INFO by BOARD diff. Not a WALTER-flagged ledger row (DOCKET L923).",
 extra=dict(verify_verdict='VERIFIED-PRIMARY', deep_research_ref='DOCKET L923', disposition='DELIVERED', event_window='closed')),

dict(n=18, slug='DEWEY-003R-PARTIAL-six-bank-Q3-noncurrent-up-and-coverage-down-at-all-six-full-band-rerun-still-open-EGBN-residual-open',
 title="DEWEY research-output, PARTIAL (REQ-DEWEY-20261022-003R): at the original six banks, Q3 Call Reports show noncurrent loans up and allowance coverage down at all six (EagleBank 88.48% to 67.20%); the full historical-band placement is NOT computed; EagleBank's exact bridge and the old Valley 131%→117% relay stay open",
 body="""DEWEY research-output, PARTIAL; report `AGENTS/DEWEY/output/2026-11-11_003R-six-bank-refresh-partial.md`, commit e14527103e. 003R stays PARTIAL.

**Verdict:** the original six-bank pattern persists into Q3 on a consistent bank-level basis. Descriptive, not predictive; REGINALD's October 30 zero standalone predictive weight is not re-graded.

| Bank (Call Report, bank-level) | Coverage June → September | Noncurrent / loans |
|---|---|---|
| SouthState | 213.79% → 199.66% | 0.535% → 0.563% |
| Valley | 123.27% → 109.75% | 0.912% → 0.994% |
| Huntington | 160.30% → 148.59% | 1.060% → 1.124% |
| EagleBank | 88.48% → 67.20% | 2.052% → 2.733% |
| BankUnited | 53.88% → 50.92% | 1.687% → 1.826% |
| Zions | 224.15% → 204.28% | 0.472% → 0.506% |

Noncurrent = nonaccrual + 90+ accruing; coverage = allowance / noncurrent.

**Reconciliations:** EagleBank's 88.5% vs the issuer's 109% is mainly held-for-sale nonaccrual the issuer excludes ($25.6M June, $13.5M September; issuer 109% and 73%); residuals of $0.191M and $0.201M remain, larger than rounding — exact bridge OPEN. Valley: 123.27% reproduces; the old approximately 131% → 117% relay is not reproduced on any definition and must not be cited as a reconciled series.

**Still open:** the Q3 full-population percentile placement and trigger. FDIC BankFind returned 0 Q3 rows; FFIEC lists 4,267 of 4,268 filers, so "Q3 unavailable" is false. FFIEC bulk files usually post 45 days after quarter-end (November 14), a schedule not a promise.

**Limits:** six banks, not all regional banks (REGINALD's ten-bank read had 3 counterexamples); guaranteed loans not adjusted; bank vs parent scopes differ.

**Do not relay as:** 003R completed, all regional banks worsening, Q3 reports unavailable, falling coverage predicting losses, or an exact EagleBank reconciliation.

**Per recipient:** REGINALD — consume the six-bank refresh and the definition limits. TERRY — tradeability within these limits; no coverage-based predictive claim is authorized. GIBBS, CREED, WAL, OZK, FLG, RED — information.""",
 sources="AGENTS/DEWEY/output/2026-11-11_003R-six-bank-refresh-partial.md (e14527103e) ; FFIEC CDR RetrieveFacsimile, 12 SDF responses retrieved by DEWEY 11/11 (research/2026-11-11_003R/six-bank-primary-rows.json) ; Eagle Bancorp 10-Qs 0001050441-26-000096, -000113 ; AGENTS/REGINALD/reports/2026-10-30_L801/REPORT.md, 2026-11-06_VLY-EGBN_10Q_reads.md",
 origin='DEWEY research-output / REQ-DEWEY-20261022-003R (PARTIAL)', source='DEWEY',
 action=['REGINALD', 'TERRY'], info=['GIBBS', 'CREED', 'WAL', 'OZK', 'FLG', 'RED'],
 owner_delivered={'REGINALD', 'GIBBS', 'CREED', 'WAL', 'OZK', 'FLG', 'RED', 'TERRY'},
 precedence='PRIORITY', signal_type='research', confidence=0.85, lang='reports',
 cluster='BANK_COLLATERAL', domain='BANK_CRE', entities=['SouthState', 'Valley National', 'VLY', 'Huntington', 'HBAN', 'EagleBank', 'EGBN', 'BankUnited', 'Zions', 'ZION', 'FFIEC', 'REQ-DEWEY-20261022-003R'],
 note="Phase 2.8b PARTIAL return. Quality gate: EagleBank June row checked in DEWEY's saved FFIEC SDF rows (RCON1403 136,915 + RCON1407 0; RCON3123 121,141; RCON2122 6,672,098 → 88.48% and 2.052% reproduced). No conflict with REGINALD's October 30 and November 6 records; DEWEY's report cites both. DEWEY wrote all eight copies; WALTER writes BOARD and route_log only. Ledger row stays PARTIAL with this delivery recorded.",
 extra=dict(verify_verdict='VERIFIED-PRIMARY', deep_research_ref='REQ-DEWEY-20261022-003R', disposition='DELIVERED-PARTIAL', event_window='open')),

dict(n=19, slug='Anthropic-reportedly-told-analysts-it-will-not-extend-SpaceX-Colossus-compute-contract-past-mid-2027-unconfirmed-analyst-notes-relay',
 title="Anthropic reportedly told sell-side analysts it will not extend its SpaceX (Colossus) compute contract beyond mid-2027; source is analyst-meeting notes relayed on X, unconfirmed by either company; SpaceX's filed terms already allow 90-day cancellation after initial periods ending January and March 2027",
 body="""**The claim** (Will's bookmark: @liquidtrading, 12:28Z 11/11, "JUST IN: Anthropic says contract with SpaceX will not be extended beyond the middle of next year"). WALTER traced it: sell-side meeting notes posted by @jukan05 on Wednesday, relayed by Tesla North; **neither Anthropic nor SpaceX has confirmed it**. Not a company statement.

**What the record already holds:**

| Item | Basis |
|---|---|
| Initial non-cancelable periods end January 2027 and March 2027, then 90-day notice | press summaries of SpaceX's S-1/A (WALTER did not open the filing) |
| Musk, May 28: a 180-day lease with mutual 90-day cancellation, short term at SpaceX's request | Reuters via US News, Yahoo |
| Earlier framing of about $1.25bn a month for three years through May 2029 | press, contradicted by Musk; unverified |
| SpaceX's separate binding commitment for about a $40B Apollo-financed GPU master lease, closing by year-end, leases from H1 2027 | SpaceX 8-K, VULCAN KB-VULCAN-296, -372 |

**Why it may matter:** if Anthropic is SpaceX's largest compute customer, a mid-2027 exit lands as the Apollo-financed GPU leases begin. That pairing is WALTER's inference, not a reported link.

**Asks:** VULCAN — does a mid-2027 non-renewal change your AI-capex read, and does SpaceX's IPO record name Anthropic's share of revenue? BROCK — context for the Apollo GPU-lease financing leg.

Verdict INDETERMINATE: one relayed analyst note.""",
 sources="X bookmark 2120493963467505740 (@liquidtrading, 2026-11-11T12:28:52Z) ; https://teslanorth.com/2026/11/11/anthropic-spacex-compute-contract-mid-2027/ (relays @jukan05 notes) ; https://money.usnews.com/investing/news/articles/2026-05-28/musk-says-spacex-did-not-commit-to-long-term-colossus-lease-with-anthropic ; https://techcrunch.com/2026/05/28/how-long-is-anthropics-lease-with-spacex-opinions-vary/ ; SpaceX S-1/A https://www.sec.gov/Archives/edgar/data/0001181412/000162828026039276/spaceexplorationtechnologi.htm (not opened) ; AGENTS/VULCAN/workbook/KB.tsv KB-VULCAN-296, -372",
 origin='X bookmark 2120493963467505740 (@liquidtrading)', source='WALTER',
 action=['VULCAN'], info=['BROCK', 'HENRY', 'RED'],
 precedence='PRIORITY', signal_type='context', confidence=0.4, lang='reportedly',
 cluster='AI_INFRA_CAPEX', domain='AI_CAPEX', entities=['Anthropic', 'SpaceX', 'Colossus', 'Apollo', 'jukan05', 'liquidtrading'],
 note="Will bookmark. Dup grep: SpaceX on 20261105-047 (Apollo GPU lease sell-down) and VULCAN KB-296/-372; this non-extension claim is not on the BOARD. Rule 9 trigger (secondhand primary): WALTER's two searches traced it to sell-side meeting notes (@jukan05) relayed by Tesla North; no company confirmation found. A search summary's dating of an October 30 report as older than May was rejected (search-summary layer). AI_CAPEX substance → VULCAN; financing leg → BROCK info (AI-capex carve-out). PRIORITY: unconfirmed, no registered gate.",
 extra=dict(verify_research_verdict='INDETERMINATE', event_window='open')),
]

if __name__ == '__main__':
    stamp, paths = send(CARDS)
    print(stamp)
    print('\n'.join(paths))
