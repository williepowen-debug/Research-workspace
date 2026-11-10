import sys
sys.path.insert(0, '/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-10_desktop-boot')
from dispatch_common import *

CARDS = [
dict(n=7, slug='FERT-NASS-November-corn-179.6-cut-with-no-fertilizer-cause-October-food-at-home-0.4-beef-led-not-grain',
 title='FERT: NASS November corn yield cut to 179.6 bu/acre with no fertilizer cause, planting channel stays shut; October food at home +0.4% reaches FERT\'s line but is beef-led, cereals flat',
 body="""FERT's grade (fe00b8dfcf; packet e883ae6873; DOCKET L761, T3 for L579). Card frozen November 9.

**T8, NASS Crop Production November** (ESMIS crop1126.txt, released November 10, PRIMARY, read by FERT 13:07 ET): US corn yield 179.6 bu/acre (−1.6 vs October 181.2; −6.9 vs 2025), production 15,893,419 thousand bu (−0.88% vs October), area unchanged, soybeans a record 53.3. Zero fertilizer, nitrogen or nutrient mentions. Grade: planting channel CONFIRMED shut; FL-FERT-05 stays REFUTED; the cut is UNATTRIBUTED. Largest state cuts: Illinois 208→200, Michigan 180→170; Minnesota rose 195→204.

**T3, October CPI food at home** (BLS, PRIMARY): +0.4% m/m SA as published (+0.443% index-derived); 12-month not published. Beef +0.9, snacks +1.0, dairy +0.6, cereals and bakery 0.0. HENRY's "food +0.47%" on card 001 is total food, not food at home.

**Moves FERT applied from its card:** V6 1→2 (convergence 16/40); VX-FERT-06 reads ORANGE on its own band (one month in 0.4–0.6; RED needs two consecutive months at +0.4 or more). FERT records that the composition disagrees: not grain-led, no fertilizer causation established.

**Open with PROME, not WALTER:** FERT's transmission close rule is written two ways (per-month below +0.4 vs the two-print G4 test); October blocks a November close under one reading only. FERT asks for a ruling before the November CPI on December 10. FERT has not applied either reading.

FERT already sent CARL and HENRY their packets (6967246081, 6f6c215032, 273ae0e98b). This card carries the rest of the FERT_INPUTS line.

No directed ask; owners log.""",
 sources="AGENTS/FERT/workbook/GRADING_CARD_2026-11-10_NASS-CPI.md (fe00b8dfcf) ; AGENTS/FERT/workbook/KB.tsv KB-FERT-137, 138 ; PROME/inbox/2026-11-10_from-FERT_L761-T8-NASS-graded-T3-October-CPI-L579.md (e883ae6873)",
 action=[], info=['AEOLUS', 'MARCO', 'RED', 'PROME'],
 precedence='ROUTINE', signal_type='research', confidence=0.9, lang='confirmed',
 cluster='INFLATION_TRANSMISSION', domain='FERT_INPUTS', entities=['USDA NASS', 'Crop Production November 2026', 'BLS', 'CPI food at home'],
 note="Owner-completed calendar release (step 7i row was UNKNOWN at the 16:44Z cutoff; FERT graded and pushed after). FERT_INPUTS row: owner FERT, backup CARL; info CARL, AEOLUS, MARCO, RED. CARL and HENRY hold FERT's own packets, so neither is on this card (no duplicate). PROME holds FERT's packet and reads the BOARD. Full dispatch, not a note, because FERT moved V6 and VX-FERT-06 on its card. ROUTINE: the channel grade is a refutation and no RED, REGINALD, CREED or HANS row keys on it. Figures relayed from FERT's committed card and packet; WALTER did not re-pull NASS or BLS.",
 extra=dict(event_window='closed')),
]

stamp, paths = send(CARDS, 'FERT owner grade fe00b8dfcf and packet e883ae6873 (step 7i UNKNOWN row L761, routed while holding)')
print(stamp)
print('\n'.join(paths))
