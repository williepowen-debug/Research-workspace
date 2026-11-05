import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-05_morning')
from dispatch_common import *
CARDS=[dict(n=17,slug='FLASH-selloff-broadens-to-banks-VIX-25-WAL-under-78-credit-ETFs-calm',
 title='FLASH — Selloff broadens past AI into banks: S&P −3.4%, VIX 25.8, WAL under 78 intraday; credit ETFs still calm',
 action=['LIQUID','VIOLET','HENRY','REGINALD'],info=['GIBBS','WAL','BROCK','VULCAN','RED','TERRY','NEXUS','PROME'],precedence='FLASH',signal_type='threshold-crossed',confidence=0.85,lang='vendor intraday reads',
 cluster='POSITIONING_VALUATION',domain='MARKET_VOL',entities=['SPX','QQQ','SMH','VIX','VIX9D','VIX3M','GS','MS','JPM','WAL','KRE','HYG','LQD'],
 safety_net='TRIGGERED: VIX +9.15 intraday, 25.76 at 16:04:39Z versus VIXCLS 16.61 [Nov 4]; Broad Market Stress row; FILTER_SPEC Pre-Gate bypass, duplicates included',
 body='''Updates card 016, whose "banks and credit proxies not confirming" no longer holds for banks. Vendor intraday 11:04 ET, not closes.

S&P 7,424.21 (−3.44%), Dow 52,075 (−2.40%), QQQ 651.73 (−5.81%), IWM −3.16%, SMH −10.54%, NVDA −8.73%. CNBC: Nasdaq in correction, Dow down over 1,000.

VIX 25.76, +9.15. Term structure inverted at the front: VIX9D 29.00 over VIX 25.76 over VIX3M 24.01. VVIX 123.81.

Banks: GS −7.75%, MS −7.10%, JPM −4.23%, BAC −2.47%, XLF −1.88%, KRE −0.65%. WAL 76.39 (−3.60%), under REG-T-02's 78 intraday; the row grades the close, and an existing fired cycle with no exit makes a sub-78 close a re-entry, not a new fire.

Credit still calm on proxies only: HYG −0.39%, JNK −0.42%, LQD +0.11%. No cash spread for today exists yet. 10Y 4.85%, down; gold +0.41%; bitcoin −5.75%.

Cause NOT established. Investing.com reports traders watching circuit-breaker levels; S&P is far from the −7% level. No forced-selling or funding report found.

ACTION LIQUID: funding and credit read. VIOLET: term structure. HENRY: gamma. REGINALD: bank tape, WAL at close.''',
 sources='research/2026-11-05_morning/tape-1105.json ; https://www.cnbc.com/ ; Investing.com headline 2026-11-05 16:01Z',
 note='FLASH duplicates permitted by the bypass; sent because 016 understated the bank leg within 35 minutes. Will alerted in the active session. Goes by the Broad Market Stress row. Fast tape: numbers will be stale quickly. The 016 sentence was true at its 10:29 ET read.')]
print(send(CARDS,'WALTER live read / FORGE fetch.py vendor / CNBC headlines')[0])
