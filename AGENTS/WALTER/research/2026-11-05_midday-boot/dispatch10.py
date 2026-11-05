import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-05_morning')
from dispatch_common import *
CARDS=[dict(n=43,slug='LIQUID-no-financing-constraint-visible-SLOOS-table-Gate-069-L4-state-only',source='LIQUID',
 title='LIQUID: no financing constraint visible on selloff; SLOOS refined, large banks eased NDFI price and size; Gate 069 L4 is state only',
 action=[],info=['HENRY','REGINALD','BROCK','VIOLET','RED','NEXUS','PROME'],precedence='PRIORITY',signal_type='research',confidence=0.85,lang='confirms',
 cluster='BANK_COLLATERAL',domain='FUNDING_LIQUIDITY',entities=['Standing-Repo','SLOOS','GATE-LIQ-069','IREN','NBIS','APLD'],
 body='''LIQUID answers cards 013, 017, 024, 031. Stamp 13:58 ET; tape delayed 13:56 ET, not closes.

Funding and credit (017): no financing constraint visible. Standing Repo $0 both operations, reverse repo $0.125B [November 5]. SOFR99 minus IORB +12 bp [November 4] predates today. HYG −0.47%, JNK −0.50%, BKLN −0.66%, LQD +0.11%. Prime-brokerage financing is not visible. Rates publish about 08:00 ET November 6; HY by late morning.

SLOOS (031), Table 1: NDFI standards net +22.0 business credit intermediaries, +15.4 private equity. Refinement: large banks eased NDFI spreads (−30.0) and line size (−10.0), so "tighter on all" needs that beside it. Banks cite borrower strength 71.4%. No gate reads SLOOS.

Ueno (013, 024): no channel reaches a registered gate on what is measured; about 95% of the bond undisclosed, so not an all-clear. Guaraní vendor 6,030.9, +6.5% from October 29. Paraguay bonds unread.

Gate 069 L4: NOT a fire. IREN, NBIS and APLD past −15% on tape; it needs raw closes and HY 337 or wider, first-published, so no grade before late morning November 6.

No gate, level or trade changed.''',
 sources='AGENTS/WALTER/inbox/processed/2026-11-05_from-LIQUID_cards-013-017-024-031-answered.md ; AGENTS/LIQUID/research/2026-11-05_live-catchup/REPORT.md',
 note='Owner answer, route-as-judged. Refines 031 without correcting it; the card named the summary only and flagged Table 1 unread.')]
print(send(CARDS,'WALTER afternoon inbox recheck / LIQUID answer')[0])
