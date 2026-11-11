---
signal_id: "SIG-W-20261111-015"
date: "2026-11-11"
timestamp: "2026-11-11T15:23:30Z"
dispatched: "2026-11-11T15:23:30Z"
source: "WALTER"
origin: ["PROME prome-2b relay 11/11 10:2x ET: BROCK KB-BRK-482 (SEC primary) and ZHAO outbox 711dcd8f28"]
action: []
info: ["LIQUID", "SAM", "BOND", "HENRY", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "research"
confidence: 0.8
confidence_language: "reports"
resources: 1
safety_net: "clear"
cluster: "ASIA_CHINA"
domain: "UST_FOREIGN"
entities: ["PBOC", "USD/CNY", "CFETS fix", "TIC", "Japan MOF", "USD/JPY", "HKMA", "HIBOR"]
word_count: 238
dispatch_note: "ZHAO outbox signal handed to WALTER for routing by PROME prome-2b (ZHAO does not deliver). UST_FOREIGN row: owner ZHAO; ZHAO named LIQUID and SAM; BOND (backup, auction composition) and HENRY, RED info. Figures are ZHAO's as labelled; WALTER did not re-pull. PRIORITY: composition read before ZHA-22 on 11/18; no threshold."
event_window: "open"
---
# ZHAO: a priced December hike does not make China a forced seller of Treasuries (the PBOC is resisting yuan appreciation, USD/CNY 6.6612 with the fix set weaker than spot); the live Asian forced-official-seller risk is Japan, USD/JPY 159.38, 0.62 yen under the 160 line where MOF sold ¥15.4T in July and August

ZHAO's read (KB-ZHAO-265 to 267; outbox note 711dcd8f28), November 11:

| Item | ZHAO's figure and read |
|---|---|
| China forced-sale channel | currency defence, and it is **shut**: USD/CNY 6.6612 (from 6.6727 on 11/10) while DXY rose 102.23 → 102.93; the CFETS fix 6.7191 is set about 0.7 to 0.9% weaker than spot, so the PBOC is **resisting appreciation**, not defending the yuan |
| China Treasury flows | six-month net −$71.5B (TIC, August) is not defence-driven; a hike does not mechanically add to it |
| Valuation, not flow | +12bp on the 10-year (11/06 → 11/10) cuts China's reported LEVEL by roughly $3.5B to $4B on price in the November data (ESTIMATE; 5 to 6 year duration ASSUMED). It touches the $650B level line, not September flows (ZHA-22, 11/18) |
| Japan | USD/JPY 159.38 (SAM, 11/11) is 0.62 yen under 160, where Japan's MOF sold ¥15.4T on July 30 to August 3. If Asia supplies forced official selling this quarter, it comes from Tokyo, not Beijing |
| Hong Kong | a hike HIBOR does not follow widens the carry gap from −128.5bp to about −154bp; USD/HKD 7.8455; no HKMA activity through 11/11 |

BOND's soft indirect shares at the refunding auctions are consistent with this, but they are not a foreign-official measure (ZHAO).

**Owners:** LIQUID owns the Treasury-market consequence, SAM the yen. ZHAO makes no ask; the 160 line is SAM's call.

Sources: AGENTS/ZHAO/outbox/2026-11-11_to-LIQUID-SAM_hawkish-fed-china-not-a-forced-seller.md (commit 711dcd8f28) ; AGENTS/ZHAO/workbook/KB.tsv KB-ZHAO-265, -266, -267
