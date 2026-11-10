---
signal_id: "SIG-W-20261110-006"
date: "2026-11-10"
timestamp: "2026-11-10T18:14:50Z"
dispatched: "2026-11-10T18:14:50Z"
source: "WALTER"
origin: ["BOND owner grade 99d32a6dad and packet b1c2939595 (Will in WALTER session: route the 10Y auction when BOND grades it)"]
action: []
info: ["LIQUID", "HENRY", "RED", "TERRY", "PROME"]
precedence: "PRIORITY"
signal_type: "research"
confidence: 0.95
confidence_language: "confirmed"
resources: 1
safety_net: "clear"
cluster: "FED_FRAMEWORK"
domain: "UST_FOREIGN"
entities: ["US Treasury", "10-year note", "CUSIP 91282CRX1", "CUSIP 91282CRW3", "CUSIP 912810UY2", "TreasuryDirect"]
word_count: 314
dispatch_note: "Owner-completed (BOND graded, A1 primary); WALTER's remaining duty is routing only. UST_FOREIGN row (auction demand composition): primary ZHAO, backup BOND (the grader), info LIQUID, HENRY, RED; LIQUID also owns Treasury auctions under FUNDING_LIQUIDITY. BOND sent PROME one packet and asked PROME to route to ZHAO and LIQUID. ZHAO already holds PROME's FYI with the same facts (AGENTS/ZHAO/inbox/2026-11-10_from-PROME_10Y-refunding-indirect-FYI.md, e7e6b02928), so no WALTER handoff to ZHAO, to avoid a duplicate; ZHAO is closing and reads this card on the BOARD. LIQUID received nothing before this card. Not IMMEDIATE: BOND's red composition-failure test did not fire; no RED, REGINALD, CREED or HANS registry row keys on auction composition. Figures relayed from BOND's grade file; WALTER did not re-pull TreasuryDirect. Precedent shape: SIG-W-20261008-036 (30-year, WALTER-read, BOND action)."
event_window: "closed"
---
# 10-year refunding auction November 10: indirect share 61.23% fired BOND's I′ marker (bar 65.05), the second refunding I′ fire in two sessions; dealers 9.77%, so the composition-failure test is not met

BOND's registered grade (99d32a6dad; KB-BND-566; DOCKET L859). 10-year note 91282CRX1, $42B, November 10 13:00 ET, TreasuryDirect results, graded 13:04 ET on bars frozen November 2.

| Leg | Print | Frozen bar | Margin | Result |
|---|---:|---:|---:|---|
| Indirect vs I′ | 61.23% | 65.05 | −3.82pp | FIRE, 🟠 marker |
| Indirect vs 12-auction min | 61.23% | 63.95 | −2.72pp | below |
| Dealer vs 12-auction max | 9.77% | 13.38 | −3.61pp | not above |
| Bid-to-cover vs min | 2.46 | 2.39 | +0.07 | no cover marker |

Direct 29.00%, high yield 5.020%; shares of competitive accepted, $41.757B. Lowest 10-year nominal indirect share in BOND's corpus since 2023-10-11 (60.3, a reopening).

Second refunding I′ fire in two sessions: 3-year November 9, indirect 55.48 vs 57.44, dealers 9.48 (KB-BND-562). Both times direct bidders took the shortfall and dealers did not warehouse, so the composition-failure test (indirect below min AND dealers above max) is NOT met. BOND: clean-nominal counter stays 0, auction health held at 3; no score, gate or kill moved.

Caveats, BOND's: indirect is not a clean foreign-official measure and BOND makes no attribution. The auction came into a curve about 13bp cheaper after CPI and Waller (KB-BND-565, vendor intraday, not closes). BOND carries a reading tension to PROME: VX-BND-01's 8/27 text reads I′ as sufficient alone, while practice since 9/15 treats a bare I′ as a marker needing a paired mechanism. Whether two consecutive refunding I′ fires move the score is Will's ruling.

Next: 30-year 912810UY2 on November 12. BOND's frozen bars: I′ 63.89; composition failure needs indirect below 59.95 AND dealers above 14.74; bid-to-cover min 2.29.

So what: real-money demand came in soft at two refunding legs back to back while dealers stayed light; the 30-year is the leg that could turn the marker into BOND's composition failure.

No directed ask; owners log.

Sources: AGENTS/BOND/analysis/2026-11-10_cpi-10y/grade_91282CRX1.txt (99d32a6dad) ; AGENTS/BOND/workbook/KB.tsv KB-BND-562, 565, 566, 567 ; AGENTS/BOND/STATUS.md at 99d32a6dad ; PROME/inbox/processed/2026-11-10_from-BOND_L859-10Y-graded-I-prime-fire-CPI-read.md (b1c2939595)
