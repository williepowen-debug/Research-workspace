import sys
sys.path.insert(0,'/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-05_morning')
from dispatch_common import *
CARDS=[
dict(n=20,slug='HENRY-put-walls-broken-gamma-negative-SOXX-print-unusable',source='HENRY',
 title='HENRY: put walls broke at the open, gamma negative on SPX, QQQ and NDX; do not quote SOXX today',
 action=[],info=['VIOLET','LIQUID','VULCAN','RED','PROME'],precedence='PRIORITY',signal_type='research',confidence=0.8,
 cluster='POSITIONING_VALUATION',domain='MARKET_VOL',entities=['SPX','QQQ','NDX','SOXX','SMH'],
 body='''HENRY packet, stamped 09:49 ET, intraday, routed about 2.5 hours later; levels below have since moved further. QQQ broke the 680 put wall about 09:30–09:35, NDX broke 28,000, SPX broke 7,600. None is a close.

Cboe chains read 09:48 ET. Net gamma per 1%: SPX −$32.4B / −$53.3B (14d/35d), flip about 7,693 / 7,696. QQQ −$3.7B / −$6.4B, flip about 702 / 706. NDX −$1.0B / −$2.0B, flip about 28,495 / 28,566. Free-tier proxy: sign and flip robust, dollars assumption-dependent. Some walls withheld by HENRY. Open interest vintage inferred.

Why it matters: negative gamma means dealer hedging adds to moves rather than damping them, which fits today's acceleration. Reported drivers, none established.

INSTRUMENT WARNING: SOXX printed 450.41 to about 141 on the vendor with no split listed; treat as an unconfirmed share-count change, not −68.7%. Do not quote SOXX percent today.

Cboe IV is zero for about 15 minutes after 09:30 ET; HENRY fixed gamma_flip.py to refuse that read.''',
 sources='AGENTS/WALTER/inbox/processed/2026-11-05_from-HENRY_put-walls-broken-intraday-gamma-negative-all-three.md ; AGENTS/HENRY/research/2026-11-05_catchup/',
 note='Owner packet, route-as-judged. No ACTION line: HENRY owns it and is live. Sat in the inbox until the 11:16 ET check; latency is WALTER\'s.'),
dict(n=21,slug='LIQUID-November-4-credit-grades-REVERSES-predates-today',source='LIQUID',
 title='LIQUID: November 4 credit grades REVERSES, replacing BROADENS in 076 for that date; says nothing about today',
 action=[],info=['HENRY','REGINALD','BROCK','VIOLET','NEXUS','RED','PROME'],precedence='PRIORITY',signal_type='research',confidence=0.9,lang='confirms',
 cluster='BANK_COLLATERAL',domain='FUNDING_LIQUIDITY',entities=['HY-OAS','CCC','GATE-LIQ-069','GATE-LIQ-076','GATE-LIQ-079'],
 body='''LIQUID, first-published [November 4]: HY 332 (−8), IG 91, BBB 113, BB 199 (−4), B 351 (−11), CCC 1,297 (−19) bp. The September 25 ordered rule grades REVERSES (CCC ≤ −9 and B ≤ −4). BROADENS in card 20261104-076 described observations through November 3 and is superseded for November 4 only; that card stays correct for its dates.

Limits: one print, not a trend. HY >320 run continues at 5 observations. No gate changed: HY-REKILL 0 of 2; 069 2-of-2 with L1 and L4 not fired; 072 not fired; 076 not met 1 of 3, W2 unpublished; 079 not armed at +12 bp [November 4]. Tier reads are not issuer-count breadth.

Index credit tightened on the session the AI cohort fell 7–11%, so that stress had not reached index credit on November 4. Cause not established.

This says NOTHING about November 5: card 017's selloff comes after this print. Cash spreads for today publish tomorrow.''',
 sources='AGENTS/WALTER/inbox/processed/2026-11-05_from-LIQUID_november-4-credit-reverses.md ; AGENTS/LIQUID/research/2026-11-05_live-catchup/REPORT.md',
 note='Owner signal. Same print as card 009; this adds the tier grade and gate states. Not a correction of 076.'),
dict(n=22,slug='Fed-Barkin-sees-hikes-ahead-Hammack-restrictive-rates-headlines',
 title='Fed speakers: Barkin sees hikes ahead at a gradual pace; Hammack says restrictive rates are needed',
 action=['HENRY'],info=['BOND','CARL','RED'],precedence='PRIORITY',signal_type='context',confidence=0.6,
 cluster='FED_FRAMEWORK',domain='MACRO_INFLATION',entities=['Federal-Reserve','Barkin','Hammack','Bank-of-England'],
 body='''Headlines only, November 5, bodies unread: CNBC 14:29Z, "Barkin sees interest rate hikes ahead, but at a gradual pace". Bloomberg and Quartz 15:41Z, "Hammack says restrictive rates needed to cool inflation". Reuters 14:06Z, "BoE joins the rate hike club, Australia may be done already".

Why it matters: hawkish talk arrived the same morning equities sold off and the 10-year fell to about 4.83%. The bond market is not pricing what these headlines say; that is a tension, not a finding. Rate level, path and any market pricing NOT read here. Search returned older Barkin and Hammack items, so wording rests on the headlines alone. Barkin's voter status was not checked at a primary.

Check before relaying: the exact quote and date.

ACTION HENRY: read both against the December meeting and your path; Friday payrolls come first.''',
 sources='Google News titles, 2026-11-05 ; https://www.cnbc.com/',
 note='No card held these. Low confidence by design: headline-only, single morning. ORACLE owns priced odds if needed.'),
dict(n=23,slug='Iran-tanker-tally-grows-in-headlines-still-claim-only',
 title='Iran tally grows to five tankers and a tug in headlines; still claim-only, no neutral confirmation',
 action=['FALCON'],info=['BRENT','HAWK','RED'],precedence='PRIORITY',signal_type='context',confidence=0.5,
 cluster='IRAN_HORMUZ',domain='GEOPOL_ENERGY',entities=['IRGC','Hormuz','UKMTO'],
 body='''Update to card 007, headlines only, bodies unread: Free Malaysia Today 15:53Z, "Iran says 5 tankers, tugboat caught fire in Hormuz". NST 15:45Z, "Three more tankers damaged in Hormuz as Iran steps up pressure on Trump". Straits Times 15:17Z, "Tankers hit in Hormuz as Iran keeps up pressure after US vote". Quantum 11:49Z, "Tanker hit near Qatar as Iran claims more Hormuz attacks".

The count is Iran's. It may include earlier claims or overlap with card 007; no names or positions seen. No neutrally confirmed mine, no confirmed sinking, at sources reached. ukmto.org remains blocked.

KILL as current: KAVOMALEAS and ACHELOOS, which a search returned beside these; both are July 2026 (Maritime Optima July 21, Container News July 20).

Brent January 96.99 at 11:17 ET, vendor, not a settle; no source ties the price to these claims.

ACTION FALCON: reconcile against census; no WALTER grade.''',
 sources='Google News titles 2026-11-05 ; https://maritimeoptima.com/maritime-news/dynacom-vlcc-acheloos-reportedly-struck-in-strait-of-hormuz-as-kavomaleas-continues-to-burn ; https://container-news.com/dynacom-managed-tanker-catches-fire-after-projectile-strike-near-strait-of-hormuz/',
 note='Bounded headline check, anchor clock unchanged. Re-search per MEMORY rule 40 on a routed state-dependent story.',
 extra={'kill_note':'KAVOMALEAS and ACHELOOS are July 2026, not November'}),
]
print(send(CARDS,'WALTER pre-close routing check / owner packets / headline pass')[0])
