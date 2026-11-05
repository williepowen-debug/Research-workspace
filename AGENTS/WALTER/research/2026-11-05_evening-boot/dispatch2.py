import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-05_morning')
from dispatch_common import *
CARDS=[
dict(n=65,slug='CORRECTION-Reuters-ties-Nov-5-oil-rise-to-tanker-attacks-held-headlines-closed',
 title='CORRECTION to cards 007, 056, 058: Reuters ties the November 5 oil rise to tanker attacks; two held Iran headlines closed',
 action=[],info=['FALCON','BRENT','HAWK','SAM','NEXUS','RED','HENRY','TERRY','PROME'],precedence='PRIORITY',signal_type='correction',confidence=0.85,lang='reports',
 cluster='IRAN_HORMUZ',domain='OIL_ENERGY',entities=['VELOS-SAPPHIRE','BZF27','CLZ26','Yanbu','Hormuz'],
 body='''Cards 007, 056 and 058 said no source tied the price move to those events. Reuters' settle story, read tonight, now says Brent settled over $3 higher as new tanker attacks fed supply worries. One wire, a reported cause. Gelber and Associates, quoted there, adds caution about pricing normal flows too early.

The Yanbu alert appears in that story with no stated price link. The Qatar proposal item is 15:17 ET, after the 14:30 ET settle, so the settle did not price it.

Marks, BRENT [EST], no exchange page read: January Brent $98.29 (+$3.67), December WTI $90.52 (+$2.40). These replace the 98.44 and 98.57 vendor reads. Evening prints above that are next-session.

Held headlines closed:
- "Iran Opens Hormuz to China and India": CLAIM-ONLY. One lawmaker, 11/3, four countries; no ship or procedure; OilPrice body unread. Not a reopening, no state change.
- Lloyd's "Seafarer killed": same event as 007, now named VELOS SAPPHIRE, per FALCON. Lloyd's standfirst says killed; IMO says one missing. Conflict carried. Census stays 7.

⛔ Reuters "Oil settles $3 higher on Yanbu disruption" is September 15. Same shape as November 5.''',
 sources='https://ca.finance.yahoo.com/news/oil-falls-fourth-day-expectations-045943628.html ; AGENTS/BRENT/research/2026-11-05_evening-rows/NOTE.md ; AGENTS/FALCON/STATUS.md ; https://thedailyguardian.com/business/oil-settles-3-higher-on-yanbu-disruption-saudi-cargo-cancellations-757391/',
 note='BRENT packet 7185ea347b; Reuters and the September 15 date read by WALTER. Guards visited. Lloyd\'s and IMO not read by WALTER; owner reads.',
 extra=dict(corrects='SIG-W-20261105-007',corrects_direction='STRENGTHENS tanker-attack price link, reported cause only; also amends 056 and 058',kill_strings=['Oil settles $3 higher on Yanbu disruption'])),
dict(n=66,slug='OTTO-Exeter-recovery-fourth-pool-below-28-noisy-series',
 title='OTTO: Exeter recovery, fourth pool re-crossed 28% in September; one month on a noisy series',
 action=['CARL'],info=['RED','BROCK','REGINALD','PROME'],precedence='PRIORITY',signal_type='threshold-crossed',confidence=0.8,lang='confirms',
 cluster='CONSUMER_STAGFLATION',domain='CONSUMER_CREDIT',entities=['Exeter','EART','CACC','CPSS'],
 source='OTTO',
 body='''OTTO's recovery trigger fired on Exeter 10-D filings, September collections. EART 2022-2 19.14%, 2022-3 15.70%, 2023-1 21.04%, 2024-1 26.51%. August: 25.17, 24.58, 24.79, 29.78. 2024-1 is the new crossing, so all four sit below 28%; three below 25%. WALTER spot-checked these cells at OTTO's readout, not the filings.

Limits: a re-crossing, not a first. One month: January's mean of 19.2% rebounded to 27.8%. Six-month means are flat to slightly up on all four. A level test; no skip default or borrower cause. $2.6M to $5.6M liquidated per deal.

Same filings: 60+ delinquency worse year on year on all four; extensions rose, still below about 7% a year ago.

OTTO corrects its own test: Severity-Divergence compares two months against a 12-month noise floor. Preview +16.12pp severity, NO VERDICT; August's REFUTE stands, but "severity did not move" must carry this limit. Not support for the Invisible Exit.

Additions at primary: Credit Acceptance's $291.2M is $106.0M ordinary plus $185.2M methodology, and the company had "observed small but consistent quarterly underperformance". Not a realized shortfall. CPS auction recovery 32.0% vs 28.7%, different definition.

ACTION CARL: update your trigger table.''',
 sources='AGENTS/OTTO/research/2026-11-05_catchup/READOUT.md ; AGENTS/WALTER/inbox/processed/SIG-OTTO-WALTER-20261105-exeter-recovery-recrossing-and-lender-reads.md',
 note='OTTO packet routed with its limits as asked. RED info is pull-complete. Adds to 20261104-008 and 20261031-018; no correction of either.'),
dict(n=67,slug='OTTO-Tricolor-Rule-2004-names-Ares-AllianceBernstein-First-Brands-trial-motion',
 title='OTTO: Tricolor trustee discovery names Ares and AllianceBernstein as lenders; First Brands trial date under motion',
 action=['BROCK'],info=['REGINALD','WAL','RED','PROME'],precedence='PRIORITY',signal_type='research',confidence=0.75,lang='reports',
 cluster='PC_STRESS',domain='PRIVATE_CREDIT',entities=['Tricolor','Ares','AllianceBernstein','First-Brands','MTB'],
 source='OTTO',
 body='''OTTO's docket steward read these; OTTO did not re-read them. WALTER matched the quotes at its memory file, not the dockets.

Tricolor: the trustee has about 24 Rule 2004 motions, not one thread. Dkt 1297, filed July 8: Ares Agent Services "served as the administrative agent and collateral agent for certain Tricolor-related warehouse lending facilities"; Ares Management managed affiliated lenders. Dkt 1356, filed July 31: an AllianceBernstein fund "was one of Tricolor's lenders."

⚠️ Rule 2004 is discovery, not an accusation. Neither filing says either party did wrong or was defrauded. Withdrawn motions against other parties clear no one.

First Brands: criminal case moved to Judge Caproni November 3, reason unstated. Patrick James moved November 5 to adjourn trial from February 9 to June 21, 2027; government opposes; no ruling. His filing's "new investigative fronts" and "more than one hundred financial institutions" are an advocate's words, naming nobody. Chapter 7 limited wind-down operation granted to March 31, 2027.

M&T Q3 10-Q: no exit language for Wilmington Trust; losses possible, not estimable. REGINALD and WAL own sizing.

Coverage: newest 30 docket entries; not a negative.

ACTION BROCK: was any Ares-managed public vehicle among the lenders?''',
 sources='AGENTS/OTTO/docket/WINTERKORN_MEMORY.md ; AGENTS/WALTER/inbox/processed/SIG-OTTO-WALTER-20261105-tricolor-rule-2004-names-and-first-brands-trial.md',
 note='OTTO packet routed with its limits as asked. Sourcing limit leads the card.'),
]
s,p=send(CARDS,'WALTER evening inbox step 7g')
print(s);print('\n'.join(p))
