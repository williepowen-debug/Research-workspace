import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-05_morning')
from dispatch_common import *
CARDS=[
dict(n=24,slug='Paraguay-President-Pena-resigns-over-Ueno-Bank-Congress-must-accept',
 title="Paraguay's President Peña resigns over the Ueno Bank collapse; Congress must still accept it; no US exposure established",
 action=['LIQUID'],info=['SAM','REGINALD','BROCK','RED','PROME'],precedence='IMMEDIATE',signal_type='catalyst',confidence=0.85,lang='reports',
 cluster='BANK_COLLATERAL',domain='FUNDING_LIQUIDITY',entities=['Ueno-Bank','Banco-Central-del-Paraguay','Pena','Paraguay'],
 body='''Update to 013 and 069. AP (Will's bookmark, posted 16:40Z), US News and NBC reprints, CNN and Bloomberg all report Peña resigned November 5, announcing it by video on X.

Only Asunción Times' body was read: "I have made the decision to submit my resignation as President of the Republic." It says Congress must now consider it, and most members signal they will accept. So: announced, not yet accepted. Effective date and successor NOT read. AP, CNN and US News refused retrieval; the AP points below come from a search summary: large protests, an apology without accepting responsibility, eight Ueno executives detained including founder Miguel Vázquez.

Why it matters: BCP opened resolution November 2 and the president fell three days later, so a failed bank has become a political event. Paraguay bonds, the guaraní and regional spillover NOT read. No US exposure established.

KILL as stated: "It's now all gone" (069: guarantee ₲228.3M per depositor). "Largest bank", "60%" and "half" stay unsourced, no denominator read.

ACTION LIQUID: integrate; say whether a sovereign or currency channel reaches your book. SAM: context on the EM carry row.''',
 sources='X 2118382854325363063 (AP) ; https://asunciontimes.com/paraguay-news/national-news/santiago-pena-resigns-as-president-of-paraguay-following-ueno-bank-collapse/ ; https://www.usnews.com/news/world/articles/2026-11-05/paraguay-president-santiago-pena-resigns-following-bank-collapse ; https://www.cnn.com/2026/11/05/americas/president-paraguay-resigns-latam-intl ; https://www.bloomberg.com/news/articles/2026-11-05/paraguay-s-pena-resigns-amid-ueno-bank-crisis-abc-reports-mw3qgdu9 ; BOARD/SIG-W-20261104-069-Ueno-bank-fund-transmission.md',
 note='Bookmarks 1, 2, 3 of BM batch; 2 and 3 folded with their claims marked. Direct AP fetch refused (403, then fetch-proxy refusal); no evasion. Search-summary points are labelled as such. IMMEDIATE on fast decay and state change, not on any US channel.'),
dict(n=25,slug='REGINALD-late-loan-scan-Preferred-Flagstar-Citizens-not-a-sector-signal',source='REGINALD',
 title='REGINALD late-loan scan: Preferred Bank multifamily 30–89 days late doubled, Flagstar and Citizens rose; not a sector signal',
 action=['CREED','HOMER'],info=['FLG','BROCK','LIQUID','RED'],precedence='PRIORITY',signal_type='research',confidence=0.85,lang='confirms',
 cluster='BANK_COLLATERAL',domain='BANK_CRE',entities=['PFBC','Preferred-Bank','FLG','Flagstar','CFG','Citizens','NexBank'],
 body='''REGINALD, one-time scan, 139 banks, own FFIEC pull, June 30 to September 30. Loans 30–89 days late:

Preferred Bank (PFBC, Los Angeles, $7.8B): multifamily $62.8M to $143.1M, 26.5% of a $540.6M book. Not in the release or call. Problem loans $166.0M including a $56.6M held-for-sale loan; the release's $109.4M excludes it. CET1 11.26%. No loss recorded.

Flagstar: multifamily $233M to $392M, 1.5% of class; $344M a year earlier, so the bucket has been high before. Total 90+ accruing $51M to $107M.

Citizens: non-owner CRE $29M to $194M, nearly all 30–59 days.

NexBank (private, Dallas): multifamily $24.9M to $75.2M, 8.6% of class.

Do NOT relay as a run, capital problem, fraud, sector signal, Southern California read-through or "only these banks". Cause unknown. 30–89 is the noisiest bucket; consumer loans unscanned; most banks under about $10B absent. Preferred's 10-Q (~November 7–10, ESTIMATE) and Flagstar's 10-Q decide.

ACTION CREED, HOMER: context for your multifamily and mixed-use books only. No gate, trigger or trade. FLG and TERRY have REGINALD's direct packets.''',
 sources='AGENTS/WALTER/inbox/processed/2026-11-05_from-REGINALD_PFBC-multifamily-late-loans.md ; AGENTS/WALTER/inbox/processed/2026-11-05_from-REGINALD_late-loan-scan-routing.md ; AGENTS/REGINALD/reports/2026-11-05_late-loan-scan.md ; AGENTS/REGINALD/reports/2026-11-05_PFBC_and_open-threads.md',
 note='Two owner packets folded into one card, route-as-judged with their do-not-relay lines kept. REGINALD is owner and source, so not on the info line. FLG cc under the multi-bank rule; no convergence fire, no prior FLG or PFBC card in the window. No named property, so no case field. GIBBS not added: Citizens is outside the 16.'),
]
print(send(CARDS,'WALTER midday boot / X bookmarks / REGINALD packets')[0])
