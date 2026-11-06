import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-06_boot')
from dispatch_common import *
CARDS=[
dict(n=12,slug='HY-348-November-5-plus-16-CCC-1320-no-FLASH-REG-T-04-2bp-away-WQ-615-344-line-crossed',
 title='HY 348 [Nov 5], +16 bp, below the +25 FLASH line; over TERRY\'s 344 line, 2 bp under REG-T-04',
 action=['LIQUID','RED','TERRY'],info=['REGINALD','VIOLET','BROCK','HENRY','PROME'],precedence='IMMEDIATE',signal_type='threshold-crossed',confidence=0.95,lang='confirms',
 cluster='BANK_COLLATERAL',domain='FUNDING_LIQUIDITY',entities=['BAMLH0A0HYM2','BAMLH0A3HYC','BAMLH0A1HYBB','REG-T-04','RED-FT-02','WQ-615','GATE-LIQ-069','HYG'],
 body='''FRED posted 15:12Z, first-published read: HY 348 bp [November 5], from 332. CCC 1,320, +23. BB 213, +14. This is the first credit print carrying the November 5 selloff.

No safety-net FLASH: +16 bp against the +25 line, 357 not reached.

By registered line, WALTER's read; each owner grades:
- REG-T-04, strict >350 ×3: not met, 0 of 3, 2 bp away. Near-trigger watch. REG-T-03 and RED-FT-02: existing fires, re-entries, exits 0 of 5 and 0 of 3.
- RED-FT-07: CCC 1,320, existing state. RED-FT-06: VIXCLS 28.18 is 1 of 5 toward exit. RED-FT-10: SKEW 149.37, no exit.
- WQ-615 T1(a), one first-published close over 344: 348 reads over it. TERRY grades. Entry still needs a first green HYG day by December 4; size and limit stay on TERRY's card, and the order is Will's. WQ-513 at REG-T-04 stays unmet.
- LIQUID Gate 069, 337 or wider on this print: LIQUID grades with official closes.
- VIOLET credit-flat test, at or under 351: 348, exploratory, moves no gate.

LIQUID, RED, TERRY: grade your lines today. TERRY's row says a grade over 344 needs a same-day session.''',
 sources='FRED BAMLH0A0HYM2, BAMLH0A3HYC, BAMLH0A1HYBB, VIXCLS pulled 2026-11-06 15:12Z, first-published flag from fetch.py ; Cboe SKEW_History.csv ; PROME/DOCKET.tsv rows of 2026-11-06',
 note='Step 6c. HY single-session +16 bp, clear of safety net. ICE series, November 5 is a session. REG-T-04 within 5% one-sided from 332.5. TERRY BOARD-only, doorbell by message.'),
]
s,p=send(CARDS,'WALTER boot step 6c')
print(s);print(len(p));open('/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-06_boot/paths3.txt','w').write('\n'.join(p)+'\n')
