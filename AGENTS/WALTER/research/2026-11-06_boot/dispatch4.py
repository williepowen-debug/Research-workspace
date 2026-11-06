import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-06_boot')
from dispatch_common import *
CARDS=[
dict(n=13,slug='LIQUID-Gate-069-L4-fired-Nov-5-tier-rule-broadens-index-credit-moved-with-AI',
 title='LIQUID: Gate 069 L4 fired on November 5, tier rule broadens; first day index credit moved with the AI cohort',
 action=['VULCAN','VIOLET'],info=['NEXUS','PROME','RED','HENRY','BROCK'],precedence='PRIORITY',signal_type='pattern-match',confidence=0.9,lang='confirms',
 cluster='AI_INFRA_CAPEX',domain='FUNDING_LIQUIDITY',entities=['GATE-LIQ-069','IREN','NBIS','APLD','CRWV'],
 body='''LIQUID owner grade, first-published [November 5], read 10:10 ET November 6. HY 348 (+16), IG 93 (+2), BBB 116 (+3), BB 213 (+14), B 367 (+16), CCC 1,320 (+23).

Gate 069 L4 FIRED for the session: IREN 18.03 from 21.71, −16.95%, with HY +16 against the +5 line. NBIS −14.94%, APLD −14.69% and CRWV −9.83% did not meet. L1 not fired: BB 213, 7 bp under 220. L4 already fired October 14, so this is a new observation of a counted leg; the gate stood 2 of 2 and no new consequence attaches.

Tier rule BROADENS on the daily clause, replacing REVERSES [November 4]. HY over 320 first-published run: 6 observations.

Why it matters, LIQUID's words: on November 4 the cohort fell 7–11% and index credit tightened; on November 5 BB took its largest move of the set. Cause not established.

⚠️ Funding did not move: SOFR99−IORB +10 bp, SRF $0, RRP $0.12B [November 5]. Not a measured financing restriction. Tier reads are not issuer-count breadth. IREN's results came after that close, so the fall preceded them; IREN is about +17.9% intraday today, vendor, which does not change the grade. LIQUID says card 004's bond tables grade no LIQUID line.

VULCAN, VIOLET: LIQUID's send row names your S1/S5 and Path-B reads.''',
 sources='AGENTS/WALTER/inbox/processed/2026-11-06_from-LIQUID_ROUTE-069-L4-fired-nov5-and-tier-broadens.md ; AGENTS/LIQUID/research/2026-11-05_live-catchup/REPORT.md',
 note='Step 7g recheck. LIQUID named VULCAN, VIOLET, NEXUS, PROME. No gate level changed. Adds to card 012, which left Gate 069 to LIQUID.'),
dict(n=14,slug='Cable-One-NYSE-non-compliance-convertible-put-cross-default-chain-springing-maturity',
 title='Cable One 10-Q, added to card 064: below NYSE listing standard; issuer traces delisting to a convertible put and cross-default',
 action=[],info=['LIQUID','RED','PROME'],precedence='PRIORITY',signal_type='research',confidence=0.9,lang='confirms',
 cluster='PC_STRESS',domain='PRIVATE_CREDIT',entities=['CABO','Cable-One','CoBank','NYSE-802.01B'],
 body='''BROCK, 10-Q at primary, adds what card 064 lacks. No threshold fired.

Listing: "we are not in compliance with the continued listing standards under Section 802.01B". Equity −$86.3M at September 30, and BROCK's check puts the 30-day average market cap at $49.1M against $50M. A plan is intended. No-cure floor: $15M average, $2.64 a share. Vendor intraday $4.26 to $4.43, about −14% to −17%.

Chain, issuer's words: delisting could trigger a "fundamental change"; holders are expected to put the $345.0M 2028 convertibles at par; "we may be unable to satisfy the repurchase obligation"; event of default; cross-default under the credit agreement.

Term Loan B-2/B-3, $959.2M, moves from October 30, 2029 to May 3, 2028 if more than $150M of Term Loan B-4 is outstanding that day.

⚠️ Non-compliance is not delisting. No NYSE notice or Item 3.01 8-K on the feed at 10:15 ET. "Going concern" and "substantial doubt" do not appear; 12-month liquidity stated adequate, covenants met September 30. BROCK's inference: that window ends about November 5, 2027, 7 days before MBI's maturity, so its comfort is limited. Not a filing, default or acceleration. BROCK's L876 grade: BLOCKED-BY-ORDER, FINAL on the 10-Q; the order is unread.''',
 sources='AGENTS/WALTER/inbox/processed/SIG-BROCK-WALTER-20261106-001-cabo-nyse-noncompliance-convertible-chain.md ; https://www.sec.gov/Archives/edgar/data/1632127/000163212726000038/cabo-20260930.htm ; AGENTS/BROCK/research/2026-11-06_hy-print-cabo/REPORT.md',
 note='BROCK packet, card 064 did not carry these. Recipients of 064 less BROCK. Card 064 said the risk sections were read whole and carried neither fact: a WALTER miss.'),
dict(n=15,slug='CORRECTION-Capcom-11.7M-is-a-2026-event-not-2020-recirculation',
 title='CORRECTION to card 20261023-045: Capcom confirmed a 2026 event; "likely 2020 recirculation" was wrong',
 action=[],info=['CYPHER','REGINALD','SHADE','VULCAN','RED'],precedence='ROUTINE',signal_type='correction',confidence=0.9,lang='confirms',
 cluster='CYBER',domain='CYBER',entities=['Capcom','CYB-INC-030'],
 body='''Card SIG-W-20261023-045's title said the Capcom 11.7M claim was "likely 2020 recirculation". CYPHER reports that was its own read and it was wrong.

Capcom's notice of October 22, a day before that card: 11,774,247 records worldwide, email and account metadata. 196 passwords changed without authorization; 19 of those had e-Capcom pages read, Japan, update October 23. Cards not included. No link to PHP2Shell on any evidence; attack method not published.

Direction: strengthens the event, changes no money read. Game publisher, no financial channel. CYPHER ledger CYB-INC-030.''',
 sources='AGENTS/WALTER/inbox/processed/2026-11-06_from-CYPHER_capcom-card-045-correction.md ; https://www.capcom.co.jp/ir/english/news/html/e261022.html',
 note='CYPHER packet. Recipients of the corrected card. Capcom notice read by CYPHER, not WALTER.',
 extra=dict(corrects='SIG-W-20261023-045',corrects_direction='STRENGTHENS — event confirmed 2026',kill_strings=['likely 2020 recirculation'])),
]
s,p=send(CARDS,'WALTER boot step 7g recheck')
print(s);print(len(p));open('/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-06_boot/paths4.txt','w').write('\n'.join(p)+'\n')
