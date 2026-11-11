import sys
sys.path.insert(0, '/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-11_boot')
from dispatch_common import *

CARDS = [
dict(n=5, slug='Iran-full-sweep-Nov-11-no-ladder-fire-Petroline-targeted-not-shut-Qeshm-hits-Nov-6-and-8-UKMTO-3-sank-unnamed-Hormuz-27-transits-floor-Abqaiq-intercept-not-refound',
 title='Iran full sweep, November 11: no ladder item fired; Petroline "targeted", not shut, attacker unknown; more Qeshm hits reported November 6 and 8 with no CENTCOM text; UKMTO reportedly counts 3 ships sunk in the week to November 4, unnamed; Hormuz 27 transits November 2 to 8 (floor); the November 8 Abqaiq intercept could not be re-found',
 body="""Full war-state sweep, window November 5 01:44Z to November 11 13:55Z (Rule 9 helper; evidence only, FALCON grades). Full file: AGENTS/WALTER/research/2026-11-11_iran-full-sweep/SWEEP.md.

| Item | State |
|---|---|
| Petroline, November 9 | SPA word "targeted"; small fire; operations unaffected; line itself struck NOT-FOUND; attacker NOT ESTABLISHED; no force-majeure declaration |
| Qeshm | 11/6 night: Trump "minor strikes" (tape). 11/8 night: Iranian official says "US projectiles"; Fars first said warning shots. No CENTCOM text for either |
| Production-class hit | None found. South Pars Phase 14 platform fire 11/10: gas leak or mishap per Fars, no attack named. Khor Mor (Iraqi Kurdistan) drone hit 11/8, output halted, snippet only |
| **Abqaiq intercept** (anchor note from card 20261108) | **Not re-found** in Khaleej Times 11/8 or Reuters: unverified, not disproved |
| Sinkings | UKMTO weekly per Argus: 11 attacked, 3 sank, week to 11/4, unnamed (UKMTO page 403). Mapping to SELAT STORM and AL JUSUFI unproven. No confirmed mine |
| New hulls | VELOS SAPPHIRE (1 killed, 11/4); 199-26 near Khasab 11/7; 201-26 near Lima 11/10; ADNOC L&S vessel 11/10 (operator confirms); "Fujairah Energy" 11/10 (name single-source) |
| Hormuz counts | PortWatch 27 transits 11/2 to 11/8 = 4.4% of the 88/day baseline, a FLOOR (WALTER re-pulled the primary: daily 2, 4, 5, 5, 6, 2, 3). Kpler Hormuz 10.5 mb/d since 10/1 vs 13.5 pre-war. The only "near pre-war" figure is Kpler Gulf crude including bypass routes, not Hormuz |
| Diplomacy | Oman call 11/5, no framework or date. Rubio 11/9: some Iranian conditions "outrageous and ridiculous" (words, not a formal reply). Rezaei 11/10: talks claims "a pure lie". No signed text; mediated through Qatar |

**Anchor updated** (header, next sweep about November 18). FALCON's November 11 letter is recorded under ladder item 1: an Iranian facility hit moves no FALCON rung.

**Limits.** ukmto.org, opec.org, sabq.org and Bloomberg returned 403; UKMTO warnings 192-26 to 200-26 mostly unseen; the SPA original was not read; the search index lags for November 9 to 11.

**Ask, FALCON:** census and ladder read of the UKMTO three-sunk count, the November 8 Qeshm attribution, Khor Mor's class, and whether the anchor's Abqaiq intercept line should stand.""",
 sources="AGENTS/WALTER/research/2026-11-11_iran-full-sweep/SWEEP.md (sources S1 to S38 with URLs) ; PortWatch Daily_Chokepoints_Data FeatureServer queried by WALTER 2026-11-11 ; AGENTS/FALCON/reports/2026-11-11_weekly-review-gate001-card008.md section 3 (8290c92b32)",
 action=['FALCON'], info=['BRENT', 'HAWK', 'SAM', 'RED', 'TERRY', 'PROME'],
 precedence='PRIORITY', signal_type='research', confidence=0.7, lang='reports',
 cluster='IRAN_HORMUZ', domain='GEOPOL_ENERGY', entities=['Iran', 'Saudi Arabia', 'East-West pipeline', 'Qeshm', 'South Pars', 'Khor Mor', 'Abqaiq', 'VELOS SAPPHIRE', 'ADNOC L&S', 'Fujairah Energy', 'UKMTO', 'PortWatch', 'Kpler'],
 note="Owed full sweep (anchor re-verify trigger met 11/10 by card 20261110-008; 7-day cadence due 11/12). GEOPOL_ENERGY Iran theater: FALCON action; HAWK, BRENT, SAM info; RED and TERRY info (USO held; no new tradeable figure beyond card 001). Guards applied: ADD#24 (Petroline three states; capacity not loss), ADD#25 (no force majeure without a declaration), ADD#20 (no 'ceasefire'), the 88/day denominator and ~140 mis-cite, date traps (Yanbu September, Kharg March, Mayuree Naree March). PRIORITY: no ladder item or registered gate fired.",
 extra=dict(event_window='open')),
]

stamp, paths = send(CARDS, "WALTER Rule 9 full Iran sweep helper, 2026-11-11 (owed duty, LAST_COMPLETION resume 1)")
print(stamp)
print('\n'.join(paths))
