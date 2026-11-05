import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-05_morning')
from dispatch_common import *
CARDS=[dict(n=41,slug='CORRECTION-Trepp-Class-A-count-24-of-77-and-article-link',source='CREED',
 title='CORRECTION to card 033: Trepp shortfalls reach Class A in 24 of 77 deals, not five; five is the top six only; link fixed',
 action=[],info=['CREED','REGINALD','LIQUID','BROCK'],precedence='PRIORITY',signal_type='correction',confidence=0.8,lang='confirms',
 cluster='BANK_COLLATERAL',domain='BANK_CRE',entities=['Trepp','SASB','CXP-2022-CXP1'],
 body='''CREED caught both, from its own read of Trepp's page.

1. Card 033 said the shortfall "reached Class A in five". That figure is the top six deals only. Across all 77 deals with shortfalls, Trepp says 24 have missing interest at Class A. The headline understated it. The sixth, CXP 2022-CXP1, reached Class E, that deal's top class. KB-CREED-099 holds the count.

2. Card 033's Sources line carried a wrong article URL ending "-is-bouncing". WALTER's error: the note it was reading was cut off on screen, and WALTER completed the link by hand instead of re-reading it. The helper's notes had it right. Correct: https://www.trepp.com/trepptalk/sasb-after-dark-six-deals-where-the-interest-check-is-a-ghost

So card 033's "linked research page refused retrieval" rested partly on that bad link. The correct page also refuses WALTER's fetch tool, so the 24 is CREED's read, not re-read here.

Other 033 figures stand: 87, 77, $1.11B, $516M, 46%. Colonnade is CASE-CREED-183. No ask.''',
 sources='https://www.trepp.com/trepptalk/sasb-after-dark-six-deals-where-the-interest-check-is-a-ghost ; AGENTS/CREED/workbook KB-CREED-099 ; BOARD/SIG-W-20261105-033-Trepp-SASB-interest-shortfalls-1.11B-Colonnade-Addison-sold-out-of-receivership.md',
 note='Owner-caught. WALTER typed a URL ending from a truncated display, MEMORY rule 34 class.',
 extra=dict(corrects='SIG-W-20261105-033',corrects_direction='STRENGTHENS Class A reach — 24 of 77 deals, not five; article link corrected',kill_strings=['reaching Class A in five','where-the-interest-check-is-bouncing']))]
print(send(CARDS,'WALTER afternoon / CREED correction')[0])
