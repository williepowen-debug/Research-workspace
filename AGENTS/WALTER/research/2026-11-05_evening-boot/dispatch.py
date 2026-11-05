import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-05_morning')
from dispatch_common import *
CARDS=[
dict(n=62,slug='CORRECTION-Abrigo-wording-data-taken-not-stated',
 title='CORRECTION to card 060: Abrigo called it a data security incident; whether data was taken is not stated',
 action=[],info=['CYPHER','REGINALD','GIBBS','CREED','BRENT','VULCAN','OSPREY'],precedence='ROUTINE',signal_type='correction',confidence=0.85,lang='reports',
 cluster='CYBER',domain='CYBER',entities=['Abrigo','Sageworks'],
 body='''Card 060 said "confirmed data incident". That reads as if data was taken, and the record does not say so.

Company wording, per American Banker November 2 and the status page as held on CYB-INC-060: a "data security incident" involving unauthorized access. Whether data was taken: not stated. Secondary source.

This is the open question on CYPHER's row; a yes would go to REGINALD and GIBBS. CYPHER asked for the fix.

Rest of 060 stands, including that nothing ties Abrigo to Arkéa's provider.''',
 sources='AGENTS/WALTER/inbox/2026-11-05_from-CYPHER_card-060-abrigo-wording.md ; AGENTS/CYPHER/STATUS.md',
 note='CYPHER packet 11/05; WALTER wording overstated the secondary. All recipients of 060 included.',
 extra=dict(corrects='SIG-W-20261105-060',corrects_direction='WEAKENS — data loss not established',kill_strings=['confirmed data incident'])),
dict(n=63,slug='Ready-Capital-Q3-book-6.44-dividend-0.01-non-performing-CRE',
 title='Ready Capital Q3: book $6.44 (−5.7%), distributable loss $0.53, dividend $0.01, $954M non-performing CRE',
 action=['CREED'],info=['REGINALD','LIQUID','HOMER'],precedence='PRIORITY',signal_type='research',confidence=0.9,lang='confirms',
 cluster='BANK_COLLATERAL',domain='BANK_CRE',entities=['RC','Ready-Capital','CREED-T-08b'],
 body='''Ready Capital 8-K, accepted 17:04 ET November 5, release and supplement read.

Q3: GAAP loss $(0.40) a share, net loss $62.2M. Distributable loss $(0.53); $(0.21) before realized losses. Book $6.44 against $6.83 at June 30, −5.7%. Dividend declared $0.01; $0.125 in Q3 2025.

Realized losses on sale of investments $53.9M. About 4.8% of opening common book on my arithmetic: $6.83 times 165.2M September shares; June shares unread. The book bridge shows only $(0.14) net of allowance reversals. Whether this meets the WQ-620 5% term is CREED's grade.

Non-performing CRE: 42 loans, $954M principal, $833M carry, 72.7% 60+ days. $719M of expected exits are Q3 2027 or later. Performing: 98 loans, $1.27B.

Liquidity: $157M cash, $606M unencumbered assets, recourse leverage 1.5x. $350M 4.50% notes retired; $225M 10.00% notes due 2031 issued. CEO says the November repayment retires all 2026 corporate maturities.

CREED: this fills the RC row. STWD and ACRE report November 6. The call is 08:30 ET, the same minute as payrolls; unheard.''',
 sources='https://www.sec.gov/Archives/edgar/data/1527590/000162828026071156/readycapital-exhibit991.htm ; https://www.sec.gov/Archives/edgar/data/1527590/000162828026071156/readycapital-supplementa.htm',
 note='Step 7i: filed after the 21:37Z cutoff. Multifamily is 83% of performing collateral, HOMER added on the axis check. 10-Q not filed.'),
dict(n=64,slug='Cable-One-10-Q-MBI-GTCR-breach-letter-TRO-hearing-November-13',
 title='Cable One 10-Q: GTCR and MBI allege breach, may intervene November 6; TRO hearing November 13; no going-concern doubt stated',
 action=['BROCK'],info=['LIQUID','RED','PROME'],precedence='PRIORITY',signal_type='research',confidence=0.92,lang='confirms',
 cluster='PC_STRESS',domain='PRIVATE_CREDIT',entities=['CABO','Cable-One','MBI','Mega-Broadband','CoBank','GTCR'],
 body='''Cable One's Q3 10-Q was accepted 17:15 ET November 5, ahead of the November 9 limit. Liquidity, litigation and risk sections read whole; the rest not.

New against cards 059 and 061:
- November 2 letter: MBI and GTCR allege Cable One breached by failing to use reasonable best efforts to fight CoBank's action. They may seek to intervene as soon as November 6. Cable One calls the claims meritless.
- Hearing on the restraining order: November 13.
- A separate group of creditors has threatened claims like CoBank's.
- Cable One need not close while the order stands. It says it could pay in full, but intends to pair payment with financing.
- Term-loan exchange offer: about 34% accepted, not consummated.

Maturities its liquidity will not cover: MBI $916.2M November 2027 if closed; $1.05B drawn revolver February 2028; $345M convertibles March 2028; $694.3M Term Loan B-4 May 2028.

Limits: Chapter 11 sentence repeated, conditional. The words "going concern" and "substantial doubt" do not appear. 12-month liquidity called adequate; covenants met at September 30. This is not a filing or default.

BROCK: L876 can now grade on the 10-Q.''',
 sources='https://www.sec.gov/Archives/edgar/data/1632127/000163212726000038/cabo-20260930.htm',
 note='Step 7i: filed after the 21:37Z cutoff. Cards 059 and 061 said 10-Q due by November 9; now filed.'),
]
s,p=send(CARDS,'WALTER evening boot step 7g and 7i')
print(s);print('\n'.join(p))
