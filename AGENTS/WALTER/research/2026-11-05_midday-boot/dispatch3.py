import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-05_morning')
from dispatch_common import *
CARDS=[
dict(n=27,slug='HENRY-midday-support-walls-broken-gamma-negative-all-three',source='HENRY',
 title='HENRY 12:39 ET: published support walls broke on S&P, QQQ and Nasdaq-100; gamma negative on all three; not closes',
 action=[],info=['PROME','VIOLET','LIQUID','VULCAN','RED','TERRY','NEXUS'],precedence='IMMEDIATE',signal_type='research',confidence=0.8,lang='confirms',
 cluster='POSITIONING_VALUATION',domain='MARKET_VOL',entities=['SPX','QQQ','NDX','VIX','HYG'],
 body='''HENRY, answering FLASH 016 and 017, late by its own account; replaces card 020's walls. Cboe chains read 12:39 ET, vendor intraday, not closes. Open interest inferred; marks about 15 minutes delayed; sign and flip robust, dollars assumption-dependent. Some walls withheld by HENRY.

S&P 7,409.50 (−3.63%), flip about 7,675 / 7,678, net gamma per 1% −$38.6B / −$70.5B (14d/35d). QQQ 654.00 (−5.48%), flip about 697 / 701. Nasdaq-100 26,888.56 (−5.45%), flip about 28,350 / 28,442.

Why it matters: dealer hedging still adds to moves, and no clean S&P support stands above its 200-day (about 7,323, 1.2% away). QQQ and Nasdaq-100 trade about 3.8–3.9% under theirs. S&P red line 7,037.04 is 5.0% lower. HENRY's profile shows amplification peaking near 7,300–7,350, shape only.

Vol-control VIX >23–24 met (24.50, 12:40 ET); short-term CTA trigger met since November 4. Medium and long triggers have no sourced level. No dollar flow sizes.

Limits: credit not confirmed either way; HYG −0.41%, last cash HY 332 [November 4]. Cause not established. No probability, threshold or trade changed.

Close grade after 16:20 ET; first chain with today's positioning is pre-open November 6.''',
 sources='AGENTS/WALTER/inbox/processed/2026-11-05_from-HENRY_midday-gamma-support-walls-broken-index-mechanics.md ; AGENTS/HENRY/research/2026-11-05_midday/',
 note='Owner signal, route-as-judged; HENRY asked for PROME. PROME takes INFO only (scanner rejects ACTION), plus a doorbell to the live session. Vol-regime broadcast stays VIOLET\'s. Tree of IDs: updates 020, answers 005, 014, 016, 017.'),
dict(n=28,slug='REGINALD-Preferred-Bank-late-loans-newly-late-real-but-contained',source='REGINALD',
 title='REGINALD: about $137M of Preferred Bank late multifamily is newly late; working read real but contained',
 action=['CREED','HOMER'],info=['BROCK','LIQUID','RED'],precedence='PRIORITY',signal_type='research',confidence=0.8,lang='confirms',
 cluster='BANK_COLLATERAL',domain='BANK_CRE',entities=['PFBC','Preferred-Bank'],
 body='''Update to card 025. REGINALD checked outside research at primary. About $137M of the $143.1M late multifamily [September 30] is newly late; the older roughly $57M was one class at March 31, likely the $56.7M mixed-use loan (inferred).

Working read, REGINALD's: real but contained. Own base rates: 5 of 7 resolved jumps since 2015 migrated, charge-offs at most $9.0M. Peers 0–0.7%. CET1 reaches 10% only at about $134M pre-tax loss.

Do NOT relay as a sector signal, fraud at the new loans, or a capital problem. No public source names the late borrowers. Q3 10-Q about November 7–10 (ESTIMATE), at the FDIC, not the SEC.

ACTION CREED, HOMER: context only. No gate, trigger or trade.''',
 sources='AGENTS/WALTER/inbox/processed/2026-11-05_from-REGINALD_PFBC-outside-research-checked.md ; AGENTS/REGINALD/reports/2026-11-05_PFBC_deep-research-verification.md',
 note='Owner packet, route-as-judged. Figures are REGINALD\'s, not re-pulled. Single-name, so FLG not added.'),
]
print(send(CARDS,'WALTER midday inbox recheck / HENRY and REGINALD packets')[0])
