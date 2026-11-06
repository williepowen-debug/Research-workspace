import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-06_bookmarks3')
from dispatch_common import *
C=dict(n=39,slug='OTTO-Manheim-206.8-falsifies-OTTO-37-plus-2-percent-is-mostly-a-low-base-MFIC-label-note',
 title="OTTO: Manheim 206.8 falsifies OTTO-37; the +2% YoY is mostly a low base, not a recovery; MFIC's LendingPoint row label is LLC only",
 action=[],info=['CARL','BROCK','HENRY','PROME'],precedence='ROUTINE',signal_type='context',confidence=0.85,lang='reports',
 source='OTTO',cluster='CONSUMER_STAGFLATION',domain='CONSUMER_CREDIT',entities=['Manheim','OTTO-37','MFIC','LendingPoint','US-Auto'],
 note='OTTO packet, commit 23a0707616, asked CARL, BROCK, PROME. WALTER added HENRY: used-car prices, and HENRY got the +2% on card 019. Adds to card 019, not a correction; card 032 does not carry the LendingPoint ratio. MFIC figures read by OTTO at the 10-Qs, not by WALTER.',
 body='''From OTTO. No charter trigger fired; no score, band, gate or threshold moved.

CARL, HENRY, Manheim: October 206.8, +2% YoY, +0.5% MoM, Cox, November 6. Non-adjusted +0.3% YoY, −2.3% against September, where the October norm is −1.5%. OTTO grades OTTO-37 (at or above 207.0, first published) FALSIFIED by 0.2. This closes the grade card 019 left with OTTO.

⛔ Do not read +2% as a price recovery. Most of the swing from September's −0.6% YoY is the base. Cox's chief economist says the index is higher "against depressed values last October". OTTO's estimate from rounded figures: October's own move about +0.5 point, the base about +2.1 points. The index is 3.9% below March's 215.3.

OTTO's hinge: the catalyst test, a second negative YoY or −3% or worse, did not fire. The hinge stays orange, and Manheim does not decide the run around November 15.

Mid-month reads: nine 2026 pairs before October, final minus mid-month mean +0.21, SD 1.40, range −1.5 to +2.3. Noisy, no sign of bias, small sample.

BROCK, label only, your record, your call: REPORT section 3 and KB-BRK-455 show "LendingPoint group 0.54 to 0.40". That ratio is LendingPoint LLC only: $22,060K on $40,732K, then $16,421K on $40,884K. The whole relationship went 0.64 to 0.54, $40,219K on $63,181K, then $34,346K on $63,170K, and the −$5.9M beside the row is the whole-relationship figure. The non-accrual loan's cost is $39.0M on $21.8M principal, so the same mark is 75 cents on principal, 95 at June 30. Funding-trust loans stay accruing at 0.96. US Auto 0.40 to 0.11, the non-accrual and $39.0M / $16.4M all tie.

OTTO: Auto Pool 2023 Trust is a legacy workout, about 22.5% of a leftover pool; LendingPoint has no auto link on OTTO's record. Neither is a fraud case. Both logged on combo:lender-standstills, not scored.''',
 sources='https://www.coxautoinc.com/insights/manheim-used-vehicle-value-index-october-2026-trends/ ; AGENTS/OTTO/research/2026-11-06_manheim-october/READOUT.md ; AGENTS/OTTO/research/2026-11-06_manheim-october/MID_TO_FINAL.tsv ; MFIC 10-Qs 0001193125-26-447829 and 0001193125-26-335848 ; OTTO commits 35f48488, 23a0707616')
s,p=send([C],'OTTO packet'); print(s); print('\n'.join(p))
open(OUT/'paths4.txt','w').write('\n'.join(p)+'\n')
