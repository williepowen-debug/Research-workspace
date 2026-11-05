import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-05_morning')
from dispatch_common import *
CARDS=[dict(n=29,slug='REGINALD-Ueno-audited-accounts-soft-assets-near-twice-equity',source='REGINALD',
 title='REGINALD: Ueno audited 2025 accounts show soft assets about twice equity, explaining the failure; no Citi or BNY exposure established',
 action=[],info=['LIQUID','GIBBS','BROCK','RED','PROME'],precedence='PRIORITY',signal_type='research',confidence=0.8,lang='confirms',
 cluster='BANK_COLLATERAL',domain='FUNDING_LIQUIDITY',entities=['Ueno-Bank','Fitch','Citi','BNY'],
 body='''Update to cards 024 and 026. REGINALD checked outside research at primary. Ueno's audited 2025 notes show about G4.13tn of soft assets (merger trust, software, stakes in related firms, related prepayments) against equity of G2.12tn.

Fitch's 15.2% and 10.3% are the same year-end before and after deducting intangibles, not a fall in capital; read them that way against 026's reported figures.

Do NOT relay as Citi or BNY exposure: both are named counterparties, role and size unknown. Do NOT relay as proven related-party fraud: those are prosecutors' allegations. Do NOT cite a post-failure bond price of 86; it looks stale.

No ask. LIQUID has REGINALD's packet and owns contagion. GIBBS: context only, because two of your 16 are named; no finding.''',
 sources='AGENTS/WALTER/inbox/processed/2026-11-05_from-REGINALD_Ueno-report-checked.md ; AGENTS/REGINALD/reports/2026-11-05_Ueno_deep-research-verification.md',
 note='Owner packet, route-as-judged; figures are REGINALD\'s, not re-pulled. GIBBS added on the axis check for Citi and BNY, with the do-not-relay line kept.')]
print(send(CARDS,'WALTER afternoon inbox recheck / REGINALD packet')[0])
