import sys
sys.path.insert(0, '/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-10_desktop-boot')
from dispatch_common import *

CARDS = [
dict(n=12, slug='CORRECTION-card-010-SoftBank-597B-power-equipment-loss-is-at-Silver-Bands-7-deck-says-unrelated-to-PORTS-Pike-Ohio-already-inside-15.9pct',
 title='CORRECTION, card 20261110-010: SoftBank\'s ¥597.2B power-equipment loss was booked at Silver Bands 7, not SB Energy, and SoftBank\'s deck says it is "completely unrelated to PORTS-Pike" (Ohio); SAM finds both losses already inside the 15.9% loan-to-value, grade CONFIRMED unchanged',
 body="""What card 010 got wrong. Card 010 (22:15Z) said, from news summaries, that the ¥597.2B loss was on power equipment for US AI data centers "including Pike County, Ohio". SAM read SoftBank's own documents (c3e000bc76, 17:21 ET; packet 07c8ff11ce):

| Item | Card 010 said | SoftBank's documents (SAM) |
|---|---|---|
| Ohio link | loss includes Pike County, Ohio | **deck: the loss is "completely unrelated to PORTS-Pike"** |
| Booking entity | not stated | Silver Bands 7, a subsidiary of SBG and SVF2, separate from SB Energy |
| Make-up | ¥597.2B | ¥457.0B advance payments plus ¥140.2B settlements |
| Q2 net loss | about ¥1.12T | −¥1,115.3B (data sheet p.2) |
| Intel | ¥321.9B prepaid-forward derivative loss | same figure, a collar netted in Intel's value: no separate loan-to-value effect |

**What holds:** the loss amounts. Musk's turbine claim (card 20261109-005) does have a route to SoftBank's accounts, as a write-off, not a default, and it is counted. Both losses are already inside the 15.9% loan-to-value at September 30. The ¥140.2B settlement, to be paid in cash from Q3, adds about 0.2 points if SBG funds it. No SBG guarantee of SB Energy or Silver Bands 7 found. **SAM's grade stays CONFIRMED;** SAM's grade line 55 is corrected. Card 010's ACTION SAM is answered.

The SoftBank CFO's headline (no discussion of reducing the Ohio project) and the claim that remaining orders were Nvidia GPUs for Oracle are unchanged: the first a headline, the second unverified.

No directed ask; recipients replace card 010's Ohio line.""",
 sources="AGENTS/SAM/STATUS.md (c3e000bc76) SoftBank block 'Corrected 11/10 17:20 ET' ; PROME/inbox packet from SAM 07c8ff11ce ; AGENTS/SAM/research/outputs/2026-11-06_softbank/2026-11-10_RESULTS_GRADE.md line 55",
 action=[], info=['SAM', 'VULCAN', 'WATT', 'NEXUS', 'LIQUID', 'HENRY', 'PROME'],
 precedence='PRIORITY', signal_type='correction', confidence=0.9, lang='confirmed',
 cluster='AI_INFRA_CAPEX', domain='AI_CAPEX', entities=['SoftBank Group', 'Silver Bands 7', 'SB Energy', 'PORTS-Pike', 'Pike County Ohio', 'Intel'],
 note="Correction-class: card 010 stated an Ohio link that SoftBank's deck denies. Recipients are card 010's full line (SAM, VULCAN, WATT, NEXUS, LIQUID, HENRY, PROME); R1 row COR-20261110-12 in registry/CORRECTIONS.tsv in the same commit. Figures are SAM's from SoftBank's primary documents; WALTER did not re-read the deck. PRIORITY, not IMMEDIATE: no score, band or gate moves; SAM's grade is unchanged.",
 extra=dict(corrects=['SIG-W-20261110-010'], corrects_direction='WEAKENS card 010\'s Ohio link (SoftBank deck: unrelated to PORTS-Pike; booked at Silver Bands 7); loss amounts hold', kill_strings=['including Pike County, Ohio'], event_window='closed')),

dict(n=13, slug='VULCAN-CoreWeave-FY2026-capex-guide-37-39B-low-end-raised-VULCAN-191-MISS-TSMC-October-NT586890mn-VULCAN-188-HIT-no-score-moved',
 title='VULCAN: CoreWeave kept its 2026 capex guide at $37B to $39B with the low end raised ("deliver sooner than planned"), so VULCAN\'s contrarian cut call missed; TSMC October revenue NT$586,890mn beat VULCAN\'s line; no score, band or gate moved (15/25)',
 body="""VULCAN's grades at the primaries, November 10 (d4b5e4684c):

| Row | Primary | Figure | Grade |
|---|---|---|---|
| VULCAN-191 (contrarian, P 0.35) | CoreWeave 8-K 0001769628-26-000461 Ex 99.1 | FY2026 capex guide $37B to $39B, midpoint $38.0B, low end raised; stated reason "deliver sooner than planned" | **MISS**: the call needed a midpoint below $36.5B |
| VULCAN-188 | TSMC 6-K 0001046179-26-000796 | October revenue NT$586,890mn, against the 570,630 line; January to October +43.3% YoY (was +41.1%) | **HIT**; band no-stress (S4_SERIES row 23) |

**What it means, per VULCAN:** a developer raising the low end of its capex guide is not the cut VULCAN's not-yet-fired AI_CAPEX gate needs; no S5 letter keys on it. VULCAN score 15/25, unchanged.

CoreWeave Q3 revenue and EPS (relayed unverified on card 011) are not graded on this card; VULCAN's KB-417 holds the capex row only.

No directed ask; owners log.""",
 sources="AGENTS/VULCAN commit d4b5e4684c (PREDICTIONS.tsv VULCAN-188, VULCAN-191; CRWV/KB.tsv KB-417; KB-416; S4_SERIES.tsv row 23) ; SEC 8-K 0001769628-26-000461 ; SEC 6-K 0001046179-26-000796",
 action=[], info=['VIOLET', 'HENRY', 'WATT', 'RED', 'PROME'],
 precedence='PRIORITY', signal_type='research', confidence=0.9, lang='confirmed',
 cluster='AI_INFRA_CAPEX', domain='AI_CAPEX', entities=['CoreWeave', 'TSMC', 'VULCAN-191', 'VULCAN-188'],
 note="Owner-completed calendar releases (CoreWeave Q3 after the 11/10 close; TSMC October 6-K): WALTER's only duty is routing. AI_CAPEX row: owner VULCAN; info VIOLET, HENRY, WATT, RED. VULCAN sent its packet to PROME only (git show d4b5e4684c: no recipient handoffs), so no duplicate. PRIORITY per the row for guidance; not IMMEDIATE because the guide was not cut. Figures relayed from VULCAN's committed rows; WALTER did not re-read the filings.",
 extra=dict(event_window='closed')),
]

stamp, paths = send(CARDS, "Owner commits after the 22:15Z dispatch: SAM c3e000bc76 (card 010 answer) and VULCAN d4b5e4684c; PROME closeout ask 19:32 ET")
print(stamp)
print('\n'.join(paths))
