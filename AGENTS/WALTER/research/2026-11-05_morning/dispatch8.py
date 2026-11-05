import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-05_morning')
from dispatch_common import *
CARDS=[
dict(n=18,slug='CF-primary-half-of-Gulf-urea-exports-out-37-percent-Europe-ammonia-offline',
 title='CF primary: about half of Gulf urea exports got out; 37% of European ammonia capacity offline or reduced',
 action=['FERT'],info=['BRENT','HANS','CARL'],precedence='PRIORITY',signal_type='research',confidence=0.9,lang='confirms',
 cluster='INFLATION_TRANSMISSION',domain='FERT_INPUTS',entities=['CF','urea','ammonia','Trinidad','India','China','Yazoo-City'],
 body='''Updates card 004, now from the full 8-K exhibit, November 4. Management estimates, not measured data.

Only about half of average Middle East urea exports have left the Persian Gulf since the conflict began; supply expected to stay below pre-conflict levels. An estimated 37% of Europe's nameplate ammonia capacity was offline or reduced in October; about 35% of Trinidad's ammonia capacity is being permanently shut. Chinese urea exports projected 2–4 million tons above 2025. India expected to import over 10 million tons of urea in 2026. Channel inventory described as low.

This replaces 004's stale China line, which came from the Q2 call. Still no numeric Q4 guide in the release.

Own numbers: nine-month volumes −5% on lower AN, ammonia and UAN; excluding the lost Yazoo City volume, about flat. Outage from the November 2025 incident is ongoing. Gas cost $3.63/MMBtu versus $3.34. Buyback $890 million done, about $1.11 billion left.

CF sells into this tightness, so these estimates carry its interest. Today's 11:00 ET call not heard.

ACTION FERT: L578 grade; test the 37% against your Yara row, 270,000 t curtailment run rate.''',
 sources='https://www.sec.gov/Archives/edgar/data/0001324404/000132440426000023/cf-11042026_ex991xearnings.htm ; research/2026-11-05_morning/cf-ex991.txt ; AGENTS/FERT/STATUS.md',
 note='Supersedes the excerpt basis of 004. Read at primary after SEC access returned. HANS added: European gas-to-ammonia channel.'),
dict(n=19,slug='EIA-storage-3801-Bcf-plus-77',
 title='US gas storage 3,801 Bcf, +77, 1.4% above five-year average',
 action=[],info=['BRENT','AEOLUS'],precedence='ROUTINE',signal_type='context',confidence=0.95,lang='confirms',
 cluster='HYDROCARBON_INFRA',domain='OIL_ENERGY',entities=['EIA','natural-gas','UNG'],
 body='''EIA Weekly Natural Gas Storage Report, released November 5, week ending October 30, Lower 48: 3,801 Bcf, net +77 from 3,724. That is 2.8% below 3,910 a year ago and 1.4% above the 2021–25 average of 3,747. Consensus not read. UNG 9.38 (+1.13%) vendor intraday, 11:08 ET, below the $10.40 void line. Context only; no owner grade made here.''',
 sources='https://ir.eia.gov/ngs/wngsr.json',
 note='7i row closed. FORGE eia_fetch returned empty for this series; EIA release JSON used.'),
]
print(send(CARDS,'WALTER November 5 calendar catch-up / SEC and EIA primaries')[0])
