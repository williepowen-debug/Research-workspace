import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-06_bookmarks3')
from dispatch_common import *
import glob

all_paths=[]

C035=dict(n=35,slug='CORRECTION-equity-put-call-November-5-is-0.89-not-1.05-not-a-range-high',
 title='CORRECTION to card 033: equity put/call on November 5 is 0.89, not 1.05; not a range high and not above Liberation Day',
 action=[],info=['HENRY','VIOLET','RED'],precedence='ROUTINE',signal_type='correction',confidence=0.9,lang='reports',
 cluster='POSITIONING_VALUATION',domain='MARKET_VOL',entities=['CPCE','Cboe'],
 note='VIOLET packet, commit a83d5b679a. WALTER read the Cboe file for November 5 and April 3, 2025 and VIOLET output file; StockCharts not reread. Scope is card 033 HENRY, VIOLET, RED line only.',
 extra=dict(corrects='SIG-W-20261106-033',
  corrects_direction='WEAKENS — range-high and above-Liberation-Day readings withdrawn; reading is still high and doubled in a day',
  kill_strings=['put/call 1.05','top of its 2024–26 range','higher than Liberation Day']),
 body='''Figure from VIOLET; WALTER confirmed it at the Cboe file.

Cboe daily options file, November 5: equity put/call 0.89, puts 2,430,016 ÷ calls 2,719,490 = 0.8936. VIOLET reports StockCharts `$CPCE` now also shows 0.89, from 0.44 the session before; WALTER did not reread that chart. Card 033's 1.05 came from a chart post at 17:07 ET and no longer stands. Why they differ is not established. An early value later replaced is VIOLET's likely reading; it cannot see the vendor's revisions. Cboe total put/call was 1.06, possibly coincidence.

What falls:
- Top of the 2024–26 range: 0.89 ranks 11th of 716 Cboe sessions, January 2, 2024 to November 5.
- Above Liberation Day: Cboe printed 1.02 on April 3, 2025.
- Spikes above 1.0: 0.89 is under 1.0.

What holds: 0.89 is high, percentile 97.5 of 3,623 Cboe sessions since June 11, 2012, and it doubled in a day.

"Spikes come near lows", VIOLET's test, exploratory, cases cluster in 2022–23. First close at or above 0.89 after a 20-session gap, 35 finished cases: S&P higher 20 sessions later in 28 (80%, against 68% of all sessions), median +2.4% against +1.5%. But 15 of 35 closed more than 1% lower within 20 sessions. Worst case is this exact reading: 0.89 on March 6, 2020, then −24.7% within 11 sessions. At 1.0 or above, 11 of 17 fell that way (65%, against 58% of all sessions).

Moves no score or gate.''',
 sources='https://cdn.cboe.com/data/us/options/market_statistics/daily/2026-11-05_daily_options ; https://cdn.cboe.com/data/us/options/market_statistics/daily/2025-04-03_daily_options ; AGENTS/VIOLET/research/2026-11-06_close/putcall_output.txt ; AGENTS/WALTER/inbox/processed/2026-11-06_from-VIOLET_ROUTE-card-033-equity-put-call-is-0.89-not-1.05.md')

C036=dict(n=36,slug='CORRECTION-SoftBank-13-percent-leverage-is-a-June-30-figure-SAM-estimate-about-21.5-percent-now',
 title="CORRECTION to card 030: SoftBank's 13% leverage is a June 30 figure; SAM estimates about 21.5% now, and the 25% limit is its own ceiling",
 action=[],info=['VULCAN','SAM','LIQUID','BROCK','ZHAO','HENRY','RED','PROME'],precedence='PRIORITY',signal_type='correction',confidence=0.75,lang='reports',
 cluster='AI_INFRA_CAPEX',domain='AI_CAPEX',entities=['SoftBank','Arm','OpenAI'],
 note='SAM packet, commit 87f84f9d84, left the call to WALTER; a dated figure superseded by a current one is correction class. WALTER read SAM read and table, not SoftBank primaries. No handoff to SAM beyond the normal card.',
 extra=dict(corrects='SIG-W-20261106-030',
  corrects_direction="WEAKENS — card's quoted buffer overstated; marginal-funder reading holds",
  kill_strings=['leverage 13% against a 25% limit']),
 body='''SAM read card 030's unchecked figures at SoftBank's own documents. WALTER read SAM's work, not those documents.

- Leverage: 13.0% is true at June 30 only, Arm $354.57. Arm is about $172. SAM estimates about 21.5%, range 20–24%. That is SAM's estimate, not SoftBank's number. It assumes the planned $10B SVF2 loan was drawn and holds other SVF values at June 30, and those listed holdings have probably fallen. Monetizations since June 30 are unknown and would lower it. On SAM's base case 25% is reached near Arm $118; across its cases, $101 to $150.
- The 25% is SoftBank's own ceiling, not a covenant.
- OpenAI: $55B funded at July 31, $65B planned, SoftBank's SVF deck. That fits the NYT's roughly $65B.
- Debt added $40.4B: still unchecked.
- Card 003, results "next week": Tuesday November 10, 15:30 JST, 01:30 ET.

⛔ That report's headline leverage will be as of September 30. SAM's September 30 cases run 13.7% to 16.5%, before the October tranche. Do not relay it as today's level.

What holds: card 030's marginal-funder reading. SAM says the check itself is immaterial, +0.07 to +0.20 points of leverage. Round terms stay anonymous and with VULCAN.

Card 003 owner grade from SAM: not a Japan-led carry unwind; offshore funding unmeasured.

No grade moved here.''',
 sources='AGENTS/SAM/research/outputs/2026-11-06_softbank/SOFTBANK_CHECK_READ.md ; AGENTS/WALTER/inbox/processed/2026-11-06_from-SAM_card030-unchecked-figures.md ; SAM commit 838a525a40')

C037=dict(n=37,slug='CORRECTION-Oracle-CDS-above-288-bp-305-on-November-5-3.25-percent-untested-for-today-IREN-funded-scope',
 title="CORRECTION to card 029: Oracle CDS was 305 bp on November 5, above the card's 288; today's file is unread; IREN's \"funded\" covers only 0.3 GW",
 action=[],info=['VULCAN','LIQUID','BROCK','HENRY','RED','PROME'],precedence='PRIORITY',signal_type='correction',confidence=0.8,lang='reports',
 cluster='AI_INFRA_CAPEX',domain='AI_CAPEX',entities=['Oracle-Corp','ORCL','IREN','DTCC'],
 note='LIQUID packet, commit a2abb1c8ba, arrived 14:20 ET and sat unread in inbox until 15:31 ET. WALTER read LIQUID report sections 15.7 and 15.8, not DTCC files or IREN filings.',
 extra=dict(corrects='SIG-W-20261106-029',
  corrects_direction="WEAKENS — card's 288 bp understated the level and 3.25% is unsupported only through November 5; IREN 'weeks, not lost' holds",
  kill_strings=['NONE — 288 bp stays true for October 15; only its use as the latest level falls']),
 body='''From LIQUID's ACTION read. WALTER read LIQUID's report, not the DTCC files or filings.

Oracle 5-year CDS, December 2031, DTCC: 292 bp November 4 and 305 bp November 5, disseminated. Converted 290 to 311, last 306 at 21:47Z, approximations.

Card 029 set a 3.25% claim against 288 bp on October 15. That date is right, but it was not the latest level or the high. The gap to 325 was about 20 bp on November 5, not 37.

"3.25%": unsupported through November 5. Today is untested, not refuted; the November 6 file publishes about 20:15 ET. "Record" is not established either way. The undated 315 bp report stays unverified.

IREN: card 029 carried "fully contracted and funded". "Funded" covers only the 0.3 GW program behind the $4B run-rate, subject to funding conditions, escrow release and availability periods. Of $15B remaining capex, $6B, 40%, has no commitment and is "subject to market conditions". That is about 65% of IREN's market value at $21.63, Yahoo intraday. GPU paper outside the Microsoft contract cost 9.0% to 9.51%, against 5.96% with Microsoft behind it.

What holds: nothing LIQUID read shows financing refused, and $6B is not the money behind the $4B run-rate. "Weeks, not lost" stands. ORCL closed $115.16 November 5, −0.72% against $116.

No gate moved. LIQUID notes IREN's call and Bloomberg's Oracle article remain unread.''',
 sources='AGENTS/LIQUID/research/2026-11-05_live-catchup/REPORT.md sections 15.8 and the card 029 table ; AGENTS/WALTER/inbox/processed/2026-11-06_from-LIQUID_ROUTE-q3-bdc-card-final-oracle-cds.md')

C038=dict(n=38,slug='LIQUID-Q3-BDC-card-final-no-verdict-line-met-in-full',
 title='LIQUID: Q3 BDC card final; no verdict line met in full, MIXED in part; grades mark direction only, grants no X1 half',
 action=[],info=['REGINALD','CARL','BROCK','NEXUS'],precedence='ROUTINE',signal_type='context',confidence=0.85,lang='reports',
 source='LIQUID',cluster='PC_STRESS',domain='PRIVATE_CREDIT',entities=['MAIN','GSBD','FSK','ARCC','BXSL','OBDC'],
 note='LIQUID ROUTE packet, commit a2abb1c8ba, arrived 14:20 ET, routed 15:35 ET. REGINALD and CARL are on the card MIXED route, marked partial.',
 body='''LIQUID's pre-registered Q3 card is final on MAIN's 10-Q, accepted 11:46 ET November 6. No gate fired.

MAIN, as of September 30: NAV $34.22 from $33.92, +0.88%; FV/Cost 1.1697 from 1.1551; non-accruals 0.9% of fair value, 3.5% at cost; regular dividend held. LIQUID's caution, its own reading: a ratio above 1 mostly reflects holdings above cost, so this rise is weak evidence on debt marks.

| Verdict | State |
|---|---|
| CONFIRM | Closed on all three routes |
| REFUTE | Not met: BXSL, GSBD and MAIN FV/Cost moved outside ±0.5 pt, GSBD non-accruals rose, P/NAV fell on all six |
| MIXED | Met in part only: GSBD marked down while MAIN and ARCC held, but FSK did not mark down (NAV −0.11%, FV/Cost up) |

GSBD, September 30: NAV $11.70 from $12.06; FV/Cost 0.9195 from 0.9368; non-accruals 4.2% of fair value from 2.9%.

⛔ The card grades mark direction only. It has no manager comparator, so it cannot satisfy the wrapper half of X1. No X1 half, no sizing, no fire.

REGINALD, CARL: on the card's MIXED route, marked partial. Context only.''',
 sources='AGENTS/LIQUID/workbook/BDC_MARK_CONVERGENCE_MONITOR.md ; AGENTS/LIQUID/research/2026-11-05_live-catchup/REPORT.md sections 15.4 and 15.7 ; AGENTS/WALTER/inbox/processed/2026-11-06_from-LIQUID_ROUTE-q3-bdc-card-final-oracle-cds.md')

for card,origin in ((C035,'VIOLET packet'),(C036,'SAM packet'),(C037,'LIQUID packet'),(C038,'LIQUID packet')):
    s,p=send([card],origin); all_paths+=p

def banner(sig, text):
    f=glob.glob(str(ROOT/f'BOARD/{sig}-*.md')); assert len(f)==1,(sig,f)
    t=Path(f[0]).read_text(); assert t.startswith('---\n')
    end=t.index('\n---\n',4)+5
    line='\n> '+text+' Original text preserved below.\n'
    assert text not in t
    Path(f[0]).write_text(t[:end]+line+t[end:])
    all_paths.append('BOARD/'+Path(f[0]).name)

banner('SIG-W-20261023-045','**Correction, November 6 — SIG-W-20261106-015:** Capcom confirmed a 2026 event; "likely 2020 recirculation" was wrong.')
banner('SIG-W-20261106-018','**Correction, November 6 — SIG-W-20261106-020:** the incident was at 2200 UTC November 5, not November 6 (UKMTO 197-26), and IMO lists one seafarer fatality, not one missing.')
banner('SIG-W-20261106-023','**Correction, November 6 — SIG-W-20261106-027:** this card cited only a benign precedent. An Apache was lost off Oman June 8, tied to an Iranian drone by a US initial inquiry, search text only. Cause here is still unknown.')
banner('SIG-W-20261106-029','**Corrections, November 6 — SIG-W-20261106-034 and -037:** Reuters places the Microsoft wind-down inside a larger reassessment of cloud partnerships, so it is not only older capacity. Oracle CDS was 305 bp on November 5, above the 288 bp here, and 3.25% is untested for today. IREN\'s "funded" covers only 0.3 GW.')
banner('SIG-W-20261106-030','**Correction, November 6 — SIG-W-20261106-036:** SoftBank\'s 13% leverage is a June 30 figure. SAM estimates about 21.5% now, range 20–24%, an estimate and not SoftBank\'s number. The 25% is its own ceiling, not a covenant.')
banner('SIG-W-20261106-033','**Correction, November 6 — SIG-W-20261106-035:** equity put/call on November 5 is 0.89, Cboe, not 1.05. It is not a 2024–26 range high and is below Liberation Day\'s 1.02. Other lines stand.')

reg=W/'registry/CORRECTIONS.tsv'
raw=reg.read_bytes(); assert b'\r\n' not in raw
txt=raw.decode()
for cid in ('COR-20261106-27','COR-20261106-34'):
    lines=txt.split('\n')
    for i,l in enumerate(lines):
        if l.startswith(cid+'\t'):
            c=l.split('\t'); assert len(c)==9 and c[8]=='HOLD',c; c[8]='WEAKEN'; lines[i]='\t'.join(c)
    txt='\n'.join(lines)
if not txt.endswith('\n'): txt+='\n'
def row(n,targets,slug,summary):
    return '\t'.join([f'COR-20261106-{n}','2026-11-06','WALTER',targets,f'BOARD/SIG-W-20261106-0{n}-{slug}.md','2026-11-20','LIVE',summary,'WEAKEN'])+'\n'
txt+=row(35,'VULCAN,HENRY,VIOLET,RED,LABOR,FERT,BRENT,HANS,OTTO,ORACLE,CORAL,SAM,CYPHER',C035['slug'],'SIG-W-20261106-033 said equity put/call 1.05 at the top of its 2024-26 range; IS 0.89 (Cboe daily file, November 5), rank 11 of 716, below 1.02 on April 3, 2025; high reading and one-day doubling hold')
txt+=row(36,'VULCAN,SAM,LIQUID,BROCK,ZHAO,HENRY,RED,PROME',C036['slug'],'SIG-W-20261106-030 said leverage 13% against a 25% limit, unchecked; IS 13.0% at June 30 only, about 21.5% now, range 20-24% (SAM estimate, not SoftBank), 25% an own ceiling; marginal-funder reading holds')
txt+=row(37,'VULCAN,LIQUID,BROCK,HENRY,RED,PROME',C037['slug'],'SIG-W-20261106-029 said Oracle CDS 288 bp October 15 against a 3.25% claim, and IREN fully funded; IS 305 bp November 5 (DTCC disseminated), November 6 unread, funded covers 0.3 GW only; weeks not lost holds')
reg.write_text(txt)
all_paths.append('AGENTS/WALTER/registry/CORRECTIONS.tsv')

print('\n'.join(all_paths))
open(OUT/'paths3.txt','w').write('\n'.join(all_paths)+'\n')
