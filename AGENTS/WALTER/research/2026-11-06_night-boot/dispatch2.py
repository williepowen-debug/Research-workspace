import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-06_boot')
from dispatch_common import *
CARDS=[dict(n=55,slug='Polymarket-ceasefire-legs-second-spike-to-about-99-implied-strike-snapped-back-about-74-no-new-strike-report-found',
 title='Polymarket ceasefire legs spiked again, about 99 implied strike at the low, back to about 74; no new strike report found; NBC: advisers urge action within eight weeks',
 body="""FALCON owns the event grade; priced odds are ORACLE's. Prices settle nothing.

ORACLE live books, November 7 00:51:40Z, moving by the minute: ceasefire through November 15 25.0/27.4, from 48.0 at 23:34Z and a 1.2 trade low about 00:2xZ. November 30 20.9/26.9; December 31 6.2/8.9. Implied another US strike by November 15 about 74, was about 52. Quote ranges. Do not cite 3.8, 4.9 or 1.9, stale Gamma prices. Touch size $0 to $77 in 35 of 36 readings. No leg closed; unresolved is not all-clear. WTI $110 November, invade and war odds flat, Gamma 00:48Z, may lag.

Not found: any report of a new US strike, across ORACLE's three searches and Iran International through 00:36Z. Cause not established.

Nearby, not a proven cause: NBC, 18:16 ET (23:16Z), Kube and Lubold: some advisers told Trump his window for major combat is closing; act within eight weeks, before the new Congress; two US officials. Visible text states no decision; body paywalled. State Department Middle East alert 00:13Z via Iran International, alert text unread.

ACTION FALCON: check CENTCOM and wires for any event behind this; no grade off prices.""",
 sources="AGENTS/WALTER/inbox/processed/2026-11-06_from-ORACLE_ceasefire-legs-second-spike-and-snapback.md ; AGENTS/ORACLE/research/2026-11-06_ceasefire-break.md ; https://www.nbcnews.com/politics/national-security/trump-briefed-narrow-window-new-military-campaign-iran-rcna607879 ; https://www.iranintl.com/en/liveblog/202610312594",
 action=['FALCON'],info=['HAWK','BRENT','SAM','RED','ORACLE','HENRY','PROME'],precedence='IMMEDIATE',signal_type='context',confidence=0.65,lang='reports',
 cluster='IRAN_HORMUZ',domain='GEOPOL_ENERGY',entities=['Polymarket','Qeshm','NBC','State Department','Trump','CENTCOM'],
 note="ORACLE packet 7de38dd855; odds cited at ORACLE's dated read, WALTER did not read the books. NBC stamp is the page's own; ORACLE's 00:36Z is Iran International's relay time, so NBC preceded the fall. 'All options available at any time' not carried: not in NBC's visible text, relay only. Standing Worldwide Caution dates July 20; whether the 00:13Z alert is new text is unread. Updates card 053's market line; no error, so not a correction. Anchor verified as of the 2026-11-05 sweep; guards read whole this session. CARL off.")]
s,p=send(CARDS,'ORACLE packet')
print(s);print('\n'.join(p))
open('/tmp/claude-1000/-home-willi-Research-workspace-AGENTS-WALTER/02c65a65-5423-4aed-b69b-ff746949e545/scratchpad/paths2.txt','w').write('\n'.join(p)+'\n')
