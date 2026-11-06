import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-06_boot')
from dispatch_common import *
CARDS=[
dict(n=10,slug='LABOR-freeze-thesis-stood-down-on-its-kill-rule-hiring-read-not-layoffs-read',
 title='LABOR stands its freeze thesis down on its own kill rule; hiring read, not a layoffs read',
 action=['CARL','REGINALD','HENRY','NEXUS'],info=['RED','TERRY','PROME'],precedence='IMMEDIATE',signal_type='counter-evidence',confidence=0.9,lang='confirms',
 cluster='CONSUMER_STAGFLATION',domain='LABOR',entities=['LABOR-freeze-thaw-v2','HEN-59','KB-LAB-246'],
 body='''LABOR's packet replaces the uncommitted STATUS read on card 001. Route is LABOR's card §6.

Freeze-thaw v2 FIRED on the rule's letter: payrolls +165,000 against a +150,000 bar, three-month average 137,000, employment-population ratio 59.3%, JOLTS net positive in both latest months. Vectors 4, 6 and 7 stand down; vector 17 goes 2 to 1. Score 27 to 22 of 80; the letter names no score, the floor of 1 is LABOR's reading, 26 of 80 if held. T-03, T-04, T-06, T-08, T-13 and Kill A did not fire.

⚠️ Caveats from LABOR, keep them attached:
- A hiring read, not a layoffs read: claims 189,000, layoffs rate 1.0% for September.
- A first print 15,000 over the bar. First to second print fell 16,000 or more in 22 of 44 months.
- Involuntary part-time +339,000.
- September JOLTS is preliminary and revises December 1. A lost leg does not un-fire the rule; it has no un-fire letter.

Superseded phrases: "Bull-side kill did NOT fire", and +150K as a forward bar.

HENRY's HEN-59: NOT FIRED at +165,000.

Each owner: read through to your own thesis at your next session.''',
 sources='AGENTS/WALTER/inbox/processed/2026-11-06_from-LABOR_v2-fired-oct-nfp.md ; AGENTS/LABOR/docket/graded/GRADING_CARD_20261106_NFP.md ; AGENTS/LABOR/STATUS.md',
 note='Step 7g packet, recheck after boot read. LABOR route kept whole; TERRY has the re-grade request directly. Card 001 stands; this adds the owner caveats.',
 extra=dict(kill_strings=['Bull-side kill did NOT fire'])),
dict(n=11,slug='HENRY-November-5-close-walls-broken-QQQ-NDX-under-200-day-gamma-negative',
 title='HENRY close grade: S&P, Nasdaq-100 and QQQ walls closed broken; QQQ and NDX first closes under 200-day since April 7',
 action=[],info=['PROME','LIQUID','VIOLET','RED','TERRY'],precedence='PRIORITY',signal_type='context',confidence=0.85,lang='confirms',
 cluster='POSITIONING_VALUATION',domain='MARKET_VOL',entities=['SPX','NDX','QQQ','SOXL','SMH'],
 body='''HENRY owner grade, November 5 close, stamped 10:0x ET November 6.

S&P 7,353.73, 146 under the 7,500–7,600 band. Nasdaq-100 26,629.81, 1,370 under 28,000. QQQ 647.05, $27.95 under its 675–680 band, closed on the low. QQQ −4.94% and NDX −4.81% against their 200-days, first closes under since April 7; S&P +0.42%.

November 6 map, 09:55 ET: gamma negative on all three. S&P flip about 7,670. S&P 7,500 and NDX 28,000 now sit above spot, so overhead. QQQ 650 is the only published wall under spot; no clean S&P support is published.

Answer to card 054: "the shape fits in chips, the size is unproven." 15:50 ET to the last minute: SOXL −6.25%, SMH −1.23%, QQQ −0.35%. Most of the hour's loss came before 15:30; the final auction was mixed; vendor minute volume is unusable; the note is unread.

⚠️ Free-tier proxy: sign and flip robust, walls and dollars fragile. HENRY says nothing here on credit.

No trade, gate or level changes.''',
 sources='AGENTS/WALTER/inbox/processed/2026-11-06_from-HENRY_close-grade-walls-broken-200-day-levered-answer.md',
 note='HENRY named PROME as target; PROME sits on info because its scanner rejects ACTION, told by message.'),
]
s,p=send(CARDS,'WALTER boot step 7g recheck')
print(s);print(len(p));open('/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-06_boot/paths2.txt','w').write('\n'.join(p)+'\n')
