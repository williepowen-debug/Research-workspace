---
signal_id: "SIG-W-20261118-012"
date: "2026-11-18"
timestamp: "2026-11-18T21:17:31Z"
dispatched: "2026-11-18T21:17:31Z"
source: "ZHAO packet (840e69003e), KB-ZHAO-289; Treasury TIC slt_table3.txt re-fetched by WALTER 2026-11-18T21:16:50Z"
origin: ["AGENTS/ZHAO/outbox/2026-11-18_from-ZHAO_to-LIQUID-HANS-SAM-MIDAS-TERRY_september-tic.md (840e69003e)", "PROME relay 16:19 ET (route request; PROME read the China row itself at 16:17 ET)", "WALTER fetch of Treasury slt_table3.txt 21:16:50Z"]
action: []
info: ["LIQUID", "HANS", "SAM", "MIDAS", "BOND", "ZHAO", "PROME"]
precedence: "PRIORITY"
signal_type: "research"
confidence: 0.95
confidence_language: "publisher table read by the owner and matched row by row by WALTER; interpretation is the owners'"
resources: 1
safety_net: "clear"
cluster: "FED_FRAMEWORK"
domain: "UST_FOREIGN"
entities: ["Treasury International Capital", "slt_table3", "China", "Belgium", "Japan", "Korea", "Foreign Official", "ZHA-22", "WQ-451", "KB-ZHAO-289"]
word_count: 371
dispatch_note: "ZHAO's proposed recipients (LIQUID, HANS, SAM, MIDAS, TERRY) plus BOND, a Treasury-demand reader that was on the last TIC-class card (20261112-007 info set), plus ZHAO as source and PROME INFO by BOARD. No directed ask in the packet, so ACTION is empty; interpretation of the official line stays with SAM and LIQUID. TERRY BOARD-only. PRIORITY because it grades registered rows (ZHA-22, MIDAS L3-TIC, LIQUID's China <$650B standing condition)."
event_window: "closed"
---
# September TIC (Treasury, Nov 18 16:00 ET; ZHAO grade): foreign-official Treasury holdings fell $80.9B (fourth monthly fall) while officials were net BUYERS of long-term Treasuries (+$27.6B); the fall is price (-$68.1B valuation) and bills (-$23.7B); China LT net -$3.5B, holdings $563.9B (lowest since 2020-01); Belgium above $500B for the first time; ZHAO: no card, no investment implication

# September TIC: official holdings fall $80.9B on price and bills while officials buy coupons

**Source:** ZHAO packet `AGENTS/ZHAO/outbox/2026-11-18_from-ZHAO_to-LIQUID-HANS-SAM-MIDAS-TERRY_september-tic.md` (840e69003e; record KB-ZHAO-289; ZHA-22 graded YES). **WALTER check:** Treasury `slt_table3.txt` fetched 2026-11-18T21:16:50Z (HTTP 200). The September rows for China, Japan, Korea, Belgium, Grand Total and Foreign Official all match ZHAO's figures. All figures are $M, first published, for September 2026.

| Line | September | August | Owner note |
|---|---|---|---|
| **Foreign official holdings** | **3,674,654** | 3,755,570 | **-80,916**, the 4th monthly fall in a row |
| Foreign official net: total / LT / ST | +3,962 / **+27,617** / -23,655 | -24,161 / +18,053 / -42,214 | LT valuation -68,082: officials **bought** coupons; the holdings fall is price and bills |
| China, Mainland holdings | 563,935 | 590,729 | -26,794; lowest since the table starts (2020-01); 4th month under $650B |
| China net: total / LT / ST | -13,123 / -3,457 / -9,666 | -9,605 / -4,828 / -4,777 | LT valuation -11,607 (about 43% of the fall is price); Q3 -35,350, under the $50B a quarter send |
| Belgium holdings / net | **507,857** / +16,444 | 490,508 / -47 | **First print above $500B**. A custody-hub level only: rho with China net +0.048 (n=44), so no China inference |
| Japan holdings / net | 1,063,137 / -7,986 | 1,068,283 / -37,020 | SAM's |
| Korea holdings / net | 139,852 / +8,839 | 134,150 / +2,334 | Buying |
| Grand total net (LT) | +84,267 (+80,766) | +60,824 (+108,603) | Private LT +53,149 |

**MIDAS (WQ-451 L3-TIC):** the sign of the official-holdings change is negative. ⚠️ The same sector bought $27.6B net of coupons. Whether that supports a de-dollarisation leg is SAM's and LIQUID's interpretation, not ZHAO's and not WALTER's. MIDAS already holds the figure (its D:L821 grade cites it).

**TERRY (BOARD-only):** ZHAO's tradeability read: **no card, and no investment implication.** China's coupon selling is under 5% of all-foreign coupon buying in the month (+$80.8B). The data is 7 weeks old. It would change on a month in which official LT net turns negative together with China, or a China quarter beyond -$50B. Off-SAFE entities are invisible to TIC.
