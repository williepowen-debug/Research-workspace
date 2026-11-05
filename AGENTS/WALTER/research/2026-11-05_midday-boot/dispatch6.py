import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-05_morning')
from dispatch_common import *
CARDS=[dict(n=38,slug='CORRECTION-Preferred-Bank-base-rates-10Q-date-and-inferred-label',source='REGINALD',
 title='CORRECTION to cards 025 and 028: Preferred Bank base rates restated, 10-Q most likely November 9, "$137M newly late" is inferred',
 action=[],info=['CREED','HOMER','BROCK','LIQUID','FLG','RED'],precedence='PRIORITY',signal_type='correction',confidence=0.85,lang='confirms',
 cluster='BANK_COLLATERAL',domain='BANK_CRE',entities=['PFBC','Preferred-Bank'],
 body='''REGINALD corrects its own two packets; WALTER carried them in 025 and 028.

1. "About $137M newly late" is INFERRED. The reported rise is +$80.3M, $62.8M to $143.1M, on REGINALD's FFIEC pull.

2. "5 of 7 jumps migrated" was all loans with overlapping episodes. Correct: about 3 of 5 episodes; multifamily only, 2 of 3 reached nonaccrual.

3. Peers at more than 10%, excluding Preferred: 9 bank-quarters at 4 banks; both conversions are CFG Bank. This replaces 028's "Peers 0–0.7%".

4. Q3 10-Q most likely Monday November 9, not about November 7–10.

Conclusion unchanged: real but contained. No ask; owner's figures, not re-pulled.''',
 sources='AGENTS/WALTER/inbox/processed/2026-11-05_from-REGINALD_PFBC-correction.md ; AGENTS/REGINALD/reports/2026-11-05_PFBC_deep-research-verification.md',
 note='Owner correction of its own packets. CFG Bank is not Citizens.',
 extra=dict(corrects='SIG-W-20261105-028 SIG-W-20261105-025',corrects_direction='WEAKENS "$137M newly late" and "5 of 7 migrated" — reported rise $80.3M; 3 of 5 episodes; conclusion unchanged',
            kill_strings=['5 of 7 resolved jumps since 2015 migrated','About $137M of the $143.1M late multifamily is newly late'])),]
print(send(CARDS,'WALTER afternoon inbox recheck / REGINALD correction')[0])
