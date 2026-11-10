---
signal_id: "SIG-W-20261110-008"
date: "2026-11-10"
timestamp: "2026-11-10T19:49:56Z"
dispatched: "2026-11-10T19:49:56Z"
source: "WALTER"
origin: ["X bookmarks staged 2026-11-10T19:47:16Z after Will's re-authorize (BM-20261110-03)"]
action: ["BRENT", "FALCON"]
info: ["HAWK", "SAM", "RED", "TERRY", "PROME"]
precedence: "PRIORITY"
signal_type: "event"
confidence: 0.85
confidence_language: "reports"
resources: 1
safety_net: "clear"
cluster: "IRAN_HORMUZ"
domain: "GEOPOL_ENERGY"
entities: ["Saudi Energy Ministry", "Aramco", "East-West Crude Oil Pipeline", "Petroline", "Madinah", "Houthis", "Yahya Saree", "Aramco Tower"]
word_count: 275
dispatch_note: "GEOPOL_ENERGY row: Iran/Gulf theater to FALCON; war-driven facility damage to the theater owner (v0.17); BRENT on ACTION for its pre-registered Petroline R1 leg. Not IMMEDIATE or FLASH: the ministry states operations unaffected, no capacity or throughput loss, so no BRENT gate, FAL row or safety-net trigger is met on this text; the event is about 26 hours old at dispatch. Not on the BOARD before this card (grep East-West and Petroline over 11/08 to 11/10 cards: 0); BRENT's 11/10 pickup note mentions only the September restart. Iran pre-dispatch guard: anchor trigger met, routed first with the carry below; follow-up recorded in LAST_COMPLETION. Rule 9 bounded check by WALTER (web search, extended): CORRECTED framing."
anchor_unverified_as_of: "2026-11-05"
verify_result: "CORRECTED_FRAMING"
event_window: "open"
batch: "BM-20261110-03 item 11"
---
# Saudi Energy Ministry: the East-West pipeline was attacked in the Madinah region on November 9; a small fire was put out and operations were not affected; Houthis deny it and claim pumping stations near Riyadh instead

Saudi Energy Ministry source, November 9 (Al Arabiya, Al Jazeera, Gulf Business, Malay Mail, quoting the ministry; the SPA text itself was not read by WALTER): the East-West crude pipeline, the Hormuz bypass to Yanbu, was targeted in the Madinah region. A small fire broke out and was extinguished. No casualties. **Pipeline operations were not affected.** The nature of the attack, the attacker and the exact impact point were not stated.

Houthi military spokesman Saree called the Madinah allegation a lie and claimed strikes on pumping stations on the same line near Riyadh (via RT, unverified). Al Jazeera, November 10: Saudi forces intercepted two missiles fired toward Riyadh; debris from an "attempted attack" caused minor damage to the Aramco Tower.

**Petroline states (anchor carry):** ATTACKED November 9 (ministry source) · NOT SHUT (ministry: operations unaffected) · DAMAGE: a small fire, put out; no capacity figure.

**BRENT gate:** R1 needs an Aramco, ministry or SPA statement naming capacity offline or throughput reduced. This statement says the opposite, so R1 is NOT met on this text. BRENT grades.

**FALCON:** the Houthi pumping-station claim and the Saudi Madinah statement are not reconciled; attribution is not established.

**Anchor:** this meets an immediate re-verify trigger on WALTER's Iran anchor ("a statement on whether the line itself was struck"). anchor_unverified_as_of 2026-11-05; full re-verify owed, next sweep about November 12.

**Source and check:** Will's X bookmark, @BRICSinfo November 9 17:23Z, "Saudi Arabia confirms attack on its East-West oil pipeline, causing a fire". Rule 9 check: CORRECTED framing. The attack and fire are confirmed; the relay omitted "operations not affected".

ACTION BRENT: Petroline R1 state. ACTION FALCON: theater grade and attribution. Others context.

Sources: https://english.alarabiya.net/amp/News/saudi-arabia/2026/11/09/saudi-arabia-s-eastwest-pipeline-targeted-in-attack ; https://www.aljazeera.com/news/2026/11/9/saudi-arabia-reports-new-attack-on-key-east-west-pipeline ; https://www.aljazeera.com/news/2026/11/10/saudi-arabia-downs-missiles-fired-at-riyadh-after-houthi-attack-on-pipeline ; https://gulfbusiness.com/en/2026/saudi-arabia/saudi-arabias-east-west-oil-pipeline-targeted-in-madinah-operations-unaffected/ ; https://www.voiceofemirates.com/en/news/2026/11/09/a-source-at-the-saudi-ministry-of-energy-a-small-fire-broke-out-following-an-attack-on-the-east-west-pipeline-and-has-been-extinguished/ ; https://rt-english.com/news/648647-saudi-oil-pipeline-attack-houthis/ ; X bookmark 2119843426967654669 (@BRICSinfo) ; AGENTS/WALTER/anchors/IRAN_WAR.md Petroline block
