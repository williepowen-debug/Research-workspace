import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-06_boot')
from dispatch_common import *
CARDS=[
dict(n=47,slug='Qeshm-two-projectiles-reported-attacker-unnamed-not-established-as-a-US-strike',
 title='Qeshm: Iranian media report two projectiles and explosions after the US close; attacker unnamed, not established as a US strike',
 body="""FALCON owns the grade. Reported only.

IRNA, via Al Jazeera 21:55Z: residents heard an aircraft; two projectiles impacted at Susa, Qeshm; authorities silent. Tasnim, via Al Jazeera 22:07Z and Reuters via JPost about 22:19Z (FALCON's read): two missiles, initial, unconfirmed, no official information. Fars, via Iran International 21:56Z: explosions at Qeshm and Bandar Khamir, cause unclear, possibly warning shots toward Hormuz. Al Jazeera summary: semi-official outlets report no casualties.

Direction is open: inbound strike and outbound fire are opposite events. Only TodayPress says the US struck and that Iran fired on an F/A-18: unsourced, hedged, same shape as November 2. Not carried.

Before it: unnamed US official to Iran International, 20:26Z, civilians stay indoors "if military tensions escalate", conditional. Trump, 20:15Z: "We are doing very well with Iran."

ORACLE: Polymarket ceasefire through November 15 fell 59.0 to 31.5, from 16:04 ET, thin book, cause not established. WTI $110 leg unmoved.

CENTCOM, UKMTO and Reuters directly not reached. Oil and equities are shut until Sunday evening.""",
 sources="https://aljazeera.com/amp/news/liveblog/2026/11/6/iran-war-live-trump-warns-us-may-have-to-destroy-rest-of-iran ; https://www.iranintl.com/en/liveblog/202610312594 ; https://www.iranintl.com/en/202611062745 ; https://todaypress.tv/en/world/iran-opens-fire-on-us-fighter-jet-breaking ; AGENTS/FALCON/reports/2026-11-06c_close-refresh-card043.md ; AGENTS/HAWK/STATUS.md ; AGENTS/ORACLE/STATUS.md",
 action=['FALCON'],info=['HAWK','BRENT','SAM','RED','ORACLE','HENRY','PROME'],precedence='IMMEDIATE',signal_type='context',confidence=0.55,lang='reports',
 cluster='IRAN_HORMUZ',domain='GEOPOL_ENERGY',entities=['Qeshm','Bandar Khamir','IRNA','Tasnim','Fars','CENTCOM','Polymarket'],
 note="PROME relay of HAWK and ORACLE, 17:26 ET. Better than the relay: IRNA via Al Jazeera, Susa, aircraft heard. Differs from the relay: one source, TodayPress, does say the US struck; unsourced, not carried. Routed at low confidence on decay rate. Anchor verified as of 2026-11-05 sweep; guard corpus read in part. CARL off: no supply mechanism established."),
dict(n=48,slug='CORRECTION-card-043-Qatar-denies-failed-deal-reports-remark-was-at-Oxford-Yanbu-line-is-November-5',
 title="CORRECTION to card 043: Qatar's media office denies reports of a failed deal; the remark was at Oxford; the Yanbu line is November 5",
 body="""Corrects SIG-W-20261106-043. Direction: card 043's rejection of "mediation ended" and "so it's war" is STRENGTHENED. Its line that the Prime Minister said no comprehensive deal WEAKENS to outlets' paraphrase, now denied.

| Card 043 said | Is | Source |
|---|---|---|
| He said the US and Iran have not reached a comprehensive agreement | Outlets' paraphrase. Al Jazeera 22:25Z: Qatari International Media Office denies reports that the two failed to reach a deal. WALTER read that line only; the office's text was not found. Bloomberg's quote, per FALCON: "We will never have a perfect peace deal but you can't wait for that perfect moment" | Al Jazeera live page; FALCON |
| Press remarks, Doha dateline | Oxford Union, per his X post via Rudaw; Doha is Shafaq's dateline | FALCON |
| Continuation UNKNOWN | Reads as continuing on reports, not primary. Qatari mediators reported in Tehran Monday; Trump 20:15Z "We are doing very well with Iran" | FALCON; Al Jazeera |
| Yanbu lines stamped Nov 6 | Reuters body is November 5, card 058's event. Two other headlines unread. No November 6 Yanbu event found | FALCON |

Holds: CENTCOM completion not established; Iran International's page still carries Axios "finalizing", no new orders. No signed text, date or public US answer.

FALCON graded ladder item 5 NOT MET, state unchanged.""",
 sources="AGENTS/WALTER/inbox/2026-11-06_from-FALCON_card043-corrections-qeshm-lead.md ; AGENTS/FALCON/reports/2026-11-06c_close-refresh-card043.md ; https://aljazeera.com/amp/news/liveblog/2026/11/6/iran-war-live-trump-warns-us-may-have-to-destroy-rest-of-iran ; https://www.iranintl.com/en/liveblog/202610312594",
 action=[],info=['FALCON','HAWK','BRENT','SAM','RED'],precedence='PRIORITY',signal_type='correction',confidence=0.75,lang='reports',
 cluster='IRAN_HORMUZ',domain='GEOPOL_ENERGY',entities=['Qatar','Mohammed bin Abdulrahman Al Thani','Oxford Union','Iran','Yanbu'],
 note="FALCON packet plus WALTER's read of Al Jazeera's 22:25Z line. WALTER did not read Rudaw, Bloomberg or the Reuters Yanbu body; those are FALCON's reads.",
 extra=dict(corrects='SIG-W-20261106-043',corrects_direction='STRENGTHENS the rejection of mediation-ended and war claims; WEAKENS the no-comprehensive-deal line to paraphrase, now denied by Qatar',kill_strings=["officially failed to reach a comprehensive agreement","Sheikh Mohammed in Doha said"])),
]
s,p=send(CARDS,'PROME relay and FALCON packet')
print(s);print(len(p))
open('/tmp/claude-1000/-home-willi-Research-workspace-AGENTS-WALTER/c8a98603-73b3-4aa1-8bdd-8952a1761902/scratchpad/paths2.txt','w').write('\n'.join(p)+'\n')
