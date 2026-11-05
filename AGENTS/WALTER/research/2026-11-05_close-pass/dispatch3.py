import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-05_morning')
from dispatch_common import *
CARDS=[dict(n=61,slug='CORRECTION-Cable-One-release-raises-Chapter-11-possibility',
 title='CORRECTION to card 059: Cable One\'s release says it may need Chapter 11 if financing fails; card omitted it',
 action=[],info=['BROCK','LIQUID','RED','PROME'],precedence='PRIORITY',signal_type='correction',confidence=0.95,lang='confirms',
 cluster='PC_STRESS',domain='PRIVATE_CREDIT',entities=['CABO','Cable-One','MBI'],
 body='''Card 059 quoted the covenant language and left out the sentence that matters most. Exhibit 99.1, read at SEC: if the company is "unable to consummate a financing transaction and address near-term debt maturities on acceptable terms or at all, or if a default occurs under its debt instruments that it is unable to timely cure, it may become necessary for the Company to seek relief under Chapter 11 of the U.S. Bankruptcy Code."

It also intends to hold MBI separate from the rest of its operations if the acquisition closes.

BROCK caught it (KB-BRK-436): the Chapter 11 language is new since Q2, liquidity is called insufficient for 2027–28 maturities, and a dissolved order no longer means a close. No going-concern line in the release. The 10-Q is due by November 9.

This is a stated conditional, not a filing or a default. Rest of 059 stands.''',
 sources='https://www.sec.gov/Archives/edgar/data/1632127/000163212726000036/a2026q3-pressrelease.htm ; AGENTS/BROCK/STATUS.md',
 note='WALTER keyword read of the exhibit missed it; found on BROCK\'s closeout header.',
 extra=dict(corrects='SIG-W-20261105-059',corrects_direction='STRENGTHENS financing risk — release raises Chapter 11 if financing fails',kill_strings=[]))]
print(send(CARDS,'WALTER closeout / primary re-read')[0])
