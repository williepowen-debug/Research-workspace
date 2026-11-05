import json,sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-05_morning')
from dispatch_common import *
CARDS=[
dict(n=1,slug='BoE-raises-Bank-Rate-to-4-percent-8-1-CPI-seen-near-5',
 title='Bank of England raises Bank Rate 25 bp to 4%, 8–1, and now expects CPI around 5% by mid-2027',
 action=['HANS','BOND'],info=['LIQUID','REGINALD','CARL','RED','PROME'],precedence='IMMEDIATE',signal_type='catalyst',confidence=0.97,lang='confirms',
 cluster='INFLATION_TRANSMISSION',domain='EUROPE_MACRO',entities=['Bank-of-England','Bank-Rate','UK-gilts','HANS-T-06','HANS-T-13','HANS-T-17'],
 body='''BoE primary, November 5: the MPC voted 8–1 to raise Bank Rate 0.25 points to 4%; one member voted for 4.25% (Trading Economics names Mann, secondary). Bank Rate table: 3.75% since December 18, 2025, 4.00% from November 5, 2026; Trading Economics calls it the first rise since August 2023.

Statement: UK CPI 3.5% in September, expected around 5% by the middle of next year, then falling. "Limited evidence" of knock-on effects on other prices and wages, but pipeline pressure "now sufficient". Activity stronger than expected. "Not on a pre-set path."

Gilts, Trading Economics over-the-counter, intraday November 5, not closes: 10Y 5.15% (−1 bp), below HANS-T-06 >5.50; 30Y 5.59% (+1 bp), below HANS-T-13 >6.00. Neither inside a 5% watch band. HANS-T-17 core 2.8% [September] unchanged by this decision.

NOT READ: Monetary Policy Report body and full minutes vote names; DMO remit. No HANS grade made here.

ACTION HANS: grade the decision against T-06, T-13, T-17 and the look-through read. ACTION BOND: time-critical gilt limit stands; read any long-end reaction.''',
 sources='https://www.bankofengland.co.uk/monetary-policy-summary-and-minutes/2026/november-2026 ; https://www.bankofengland.co.uk/boeapps/database/Bank-Rate.asp ; https://tradingeconomics.com/united-kingdom/interest-rate ; https://tradingeconomics.com/united-kingdom/government-bond-yield ; https://tradingeconomics.com/united-kingdom/30-year-bond-yield',
 note='Calendar catch-up 7i, published 12:00Z. Primary statement read through paragraph 2 of the minutes. Gilt levels are intraday screens, not closes. Precedence follows the catalyst type and the October 29 ECB card. HANS STATUS dated October 29; no owner read assumed.'),
dict(n=2,slug='October-job-cuts-three-year-low-claims-189K-productivity-3.6',
 title='October job cuts lowest for the month since 2023; claims 189,000; Q3 productivity +3.6% and unit labor costs −0.7%',
 action=['LABOR','CARL'],info=['HENRY','RED'],precedence='IMMEDIATE',signal_type='catalyst',confidence=0.95,lang='confirms',
 cluster='CONSUMER_STAGFLATION',domain='LABOR',entities=['Challenger','ICSA','CCSA','OPHNFB','RED-FT-05','REG-T-05','T-09'],
 body='''Challenger primary, November 5: 43,994 October cuts, +2% from 43,281, −71% from 153,074; lowest October since 36,836 in 2023, below the 56,348 2015–2025 October average. Year to date 617,189, −44%. AI cited 1,265, lowest month this year (2.9% of October, WALTER arithmetic); 121,401 year to date, about 20%. Market/Economic Conditions 16,407, 37%, now the leading 2026 reason. Demand Downturn 21,347 year to date, +145%. Seasonal hiring plans 470,400, +26%, led by Amazon 300,000, still below 660,150 in 2024. Microsoft's voluntary offers to 60,000 are NOT in the total.

Labor Department advance, November 5: initial claims 189,000 week ending October 31; prior revised 194,000 to 195,000; four-week average 194,750. Continuing 1,718,000 week ending October 24, +23,000. RED-FT-05 >250,000 and REG-T-05 >300,000 not fired.

BLS via FRED, Q3 first read: nonfarm productivity +3.6% annualized (Q2 2.1%); unit labor costs −0.7% (Q2 1.9%). BLS release page refused; consensus not read.

ACTION LABOR: grade frozen cards GRADING_CARD_20261105_Challenger and _claims before Friday payrolls. ACTION CARL: consumer read.''',
 sources='https://www.challengergray.com/blog/october-layoffs-at-three-year-low-seasonal-hiring-plans-up-26/ ; https://www.dol.gov/ui/data.pdf ; FRED ICSA, CCSA, PRS85006092, PRS85006112 pulled 2026-11-05',
 note='Calendar catch-up 7i. One card for one morning labor read. WALTER did not open or pre-grade the frozen cards. A low-fire reading is not a hiring reading; LABOR owns that distinction. Labor intake LOOSE window through November 6.'),
dict(n=3,slug='NREF-Q3-book-value-falls-5.2-percent-dividend-held',
 title='NREF Q3 book value falls 5.2% to $17.63; dividend held at $0.50 on Q4 earnings guidance below it',
 action=['CREED'],info=['REGINALD','LIQUID'],precedence='PRIORITY',signal_type='research',confidence=0.9,lang='confirms',
 cluster='BANK_COLLATERAL',domain='BANK_CRE',entities=['NREF','CREED-T-08b','NexPoint-Real-Estate-Finance'],
 body='''NexPoint Real Estate Finance 8-K exhibits, November 5, read through a helper at sec.gov. Book value per share $17.63 at September 30 versus $18.60 at June 30, −5.2%. Q3 net loss to common $12.2 million, $0.65 per share; Q2 earned $5.4 million. Total net loss $0.9 million.

The gap is mostly marks: the reconciliation adds back $21.9 million of unrealized losses (implied; the exhibit does not state it as a loss). Provision only $0.46 million. No charge-off, impairment, non-accrual or watch-list line disclosed; absence from the exhibits is not a clean book.

Earnings available for distribution $0.52 per share, covering the $0.50 dividend. Q4 guide midpoint about $0.42, coverage 0.84x; cash available midpoint about $0.55, 1.10x. Stock 17.0% below book on November 4 per the company.

Exhibit quirks: midpoints differ by $0.002 between exhibits; the $0.65 divides by 18,848 shares labelled diluted, while the reconciliation shows 54,479.

NO dividend cut. Registered T-08b needs multi-name cuts AND realized cohort erosion; NREF is marks, not realized. ACTION CREED: add to the Q3 census beside STWD and ACRE November 6.''',
 sources='https://www.sec.gov/Archives/edgar/data/0001786248/000119312526448417/nref-ex99_1.htm ; https://www.sec.gov/Archives/edgar/data/0001786248/000119312526448417/nref-ex99_2.htm',
 note='7i named release. CREED launch needs Will permission; handoff waits at the desk. WALTER did not grade T-08b. Owner census 5 of 11 as of October 30 per LAST_COMPLETION; registry cell still reads 4 of 11.'),
dict(n=4,slug='CF-Q3-earnings-nitrogen-tight-owner-wake-due',
 title='CF Q3 adjusted EBITDA $833M versus $667M; owner FERT has not read it',
 action=['FERT'],info=['CARL','BRENT'],precedence='PRIORITY',signal_type='research',confidence=0.75,
 cluster='CONSUMER_STAGFLATION',domain='FERT_INPUTS',entities=['CF','CF-Industries','Yazoo-City'],
 body='''CF Industries Q3 release, November 4 after the close; excerpt through search of the 8-K exhibit, full exhibit not opened. Q3 net earnings $436 million, $2.87 per diluted share; adjusted EBITDA $833 million versus $667 million; net sales $1,860 million versus $1,659 million. Nine months: net earnings $1.78 billion including about $170 million litigation gain, adjusted EBITDA $3.01 billion, volumes −5% with an extended Yazoo City outage. Mid-cycle outlook raised to about $2.9 billion EBITDA, $1.7 billion free cash flow.

Call November 5 11:00 ET, not heard. No Q4 guide found in the excerpt. China comment found was from the Q2 call and is not current.

ACTION FERT: DOCKET L578 wake, read guidance against the China-supply return; L760 Pink Sheet holds beside it. Route any surprise through PROME. FERT's last refresh is November 2.''',
 sources='https://www.sec.gov/Archives/edgar/data/0001324404/000132440426000023/cf-11042026_ex991xearnings.htm',
 note='7i release after the intake cutoff. Secondary excerpt, confidence lowered. Decision on spawning FERT is PROME.'),
]
print(send(CARDS,'WALTER November 5 morning pass / primary reads')[0]); 
