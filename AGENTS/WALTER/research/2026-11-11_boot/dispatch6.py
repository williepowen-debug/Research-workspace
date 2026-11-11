import sys
sys.path.insert(0, '/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-11_boot')
from dispatch_common import *

YREC = "AGENTS/YURI/research/2026-11-11_L772_YUR-006_GRADE-and-catchup.md (commit 8389e02f8b) ; PROME/inbox/processed/2026-11-11_from-YURI_catchup-YUR-006-HIT-JTI-custody.md"

CARDS = [
dict(n=9, slug='Russia-puts-all-seven-Japan-Tobacco-JTI-companies-under-state-temporary-management-decrees-817-and-832-no-sale-clause-JT-2914-down-28.4pct',
 title='Russia put all seven Japan Tobacco (JTI) companies in Russia under state "temporary management" by decrees №817 (November 5) and №832 (November 6), read in full by YURI; no sale or transfer clause; Japan Tobacco (2914.T) is down 28.4% since, with two locked limit-down sessions; the custody track ran on through the week the US–Russia–Ukraine talks opened',
 body="""**At the primary** (YURI, pravo.gov.ru bodies and kremlin.ru notices, read November 11):

| Decree | Published | What it adds to the Decree-302 temporary-management list |
|---|---|---|
| №817 | November 5 | JTI Donskoy Tabak, JTI Yelets (all three holders), Kres Neva, Petro |
| №832 | November 6 | Pereslavl-Tabak (100% of shares), JTI Innovative Products, JTI Russia (the parent-level company) |

Manager: АО «Промышленные активы» (which of several companies by that name is not identified). **Neither decree has a sale, buyer or transfer clause:** custody of the shares, not seizure of ownership, on the text. YURI graded its prediction YUR-006 a HIT (Brier 0.09).

**Market** (vendor daily bars, Tokyo): 2914.T ¥7,769 (November 5) → ¥6,269 (−19.3%, locked limit-down) → ¥5,269 (−16.0%, locked again) → ¥5,500 → **¥5,562** (November 11). **−28.4%** from the November 5 close.

**Press relays, not read at Japan Tobacco or the Tokyo exchange:** Russia is about 10% of JT revenue and about 25% of adjusted operating profit; Japan's Ministry of Finance owns 37.55% of JT; JT says Russian operations continue; Finance Minister Katayama protested on November 6 and asked for withdrawal.

**Why it matters:** this is the first Decree-302 action against a Japanese company whose largest shareholder is the Japanese state. Putin signed №832 the day he announced the US–Russia–Ukraine talks in the UAE (opened November 10, press). YURI's dated call (YUR-C01, falsifier by November 28: an act removing a JTI interest or naming a buyer) is that the custody track runs independently of the negotiation track.

**Limits:** six days old when it reached WALTER (YURI's catch-up found it November 11; no desk surface held it). The 28.4% fall against a relayed 25% profit share is YURI's inference that the market prices about a total loss of the Russian business. Not a WALTER figure. No registered threshold.

No directed ask; owners log. TERRY already has it from PROME.""",
 sources=YREC + " ; pravo.gov.ru publication eo 0001202611050002 (№817) and 0001202611060040 (№832) ; kremlin.ru/acts/news/81186 and 81193 ; vendor 2914.T daily bars via YURI 2026-11-11 09:40 ET",
 action=[], info=['SAM', 'HAWK', 'HANS', 'OSPREY', 'RED', 'TERRY', 'PROME'],
 precedence='PRIORITY', signal_type='research', confidence=0.85, lang='confirmed',
 cluster='MISC', domain='RU_STATE_ACTOR', entities=['Japan Tobacco', 'JTI', '2914.T', 'JAPAY', 'Decree 302', 'Decree 817', 'Decree 832', 'Promyshlennye Aktivy', 'Japan Ministry of Finance'],
 note="YURI catch-up finding relayed by PROME prome-2b 09:4x ET (YURI under a one-packet limit, no SIG file). RU_STATE_ACTOR row: YURI owns and has graded; info HAWK, OSPREY, PROME, RED; SAM added (Japan; whether SAM's carry/BOJ charter covers a sovereign-held equity is DAEDALUS's call, so info, no ask); HANS added (European corporate exposure to the same custody track). Decree texts primary-read by YURI; market and stake figures as labelled. PRIORITY: no threshold; the event is six days old.",
 extra=dict(event_window='open')),

dict(n=10, slug='Russia-export-controls-decree-1443-three-month-ban-benzene-toluene-xylenes-phenol-outside-EAEU-and-1457-fertilizer-export-quotas-above-18.8-Mt-Dec-to-May',
 title='Russia export controls, read at government.ru by YURI: Resolution №1443 (October 31) bans exports of benzene, toluene, o- and p-xylene and phenol outside the EAEU for three months; Resolution №1457 (November 5) sets fertilizer export quotas above 18.8 Mt for December 1, 2026 to May 31, 2027',
 body="""| Instrument | Terms | For |
|---|---|---|
| **Resolution №1443, October 31** (government.ru/docs/60327) | Three-month ban on exports of coal- and petroleum-derived benzene, toluene, o-xylene, p-xylene and phenol outside the Eurasian Economic Union. Exempt: transit, humanitarian aid, Svalbard | BRENT (products, aromatics) |
| **Resolution №1457, November 5** (government.ru/docs/60376) | Fertilizer export quotas outside the EAEU, December 1, 2026 to May 31, 2027: total above 18.8 Mt; nitrogen above 11.3 Mt (ammonium nitrate above 2.3 Mt); complex fertilizers above 7.5 Mt | FERT |

**Already on the board:** card 20261105-060 carried a LIGA headline that Russia banned petrochemical feedstock exports, unread. This card supplies the instrument, its scope and its length.

**YURI's read:** №1457 is a routine renewal of the seasonal quota. It is not a potash item; potash stays triage-only at FERT in any case.

No directed ask; owners log.""",
 sources=YREC + " ; government.ru/docs/60327 (№1443) ; government.ru/docs/60376 (№1457) ; BOARD/SIG-W-20261105-060",
 action=[], info=['BRENT', 'FERT', 'OSPREY', 'PROME'],
 precedence='ROUTINE', signal_type='context', confidence=0.85, lang='confirmed',
 cluster='HYDROCARBON_INFRA', domain='RU_STATE_ACTOR', entities=['Russia', 'Resolution 1443', 'Resolution 1457', 'benzene', 'toluene', 'xylene', 'phenol', 'fertilizer export quota', 'EAEU'],
 note="YURI catch-up instruments relayed by PROME. Export instruments are RU_STATE_ACTOR (YURI holds the decision); consequence owners BRENT (aromatics) and FERT (quotas); OSPREY info (Russian product flows). ROUTINE: a renewal and a short product ban, no registered threshold. Card 20261105-060's headline is now primary-backed.",
 extra=dict(updates=['SIG-W-20261105-060'], event_window='closed')),
]

stamp, paths = send(CARDS, "PROME prome-2b relay 11/11 of YURI catch-up (8389e02f8b)")
print(stamp)
print('\n'.join(paths))
