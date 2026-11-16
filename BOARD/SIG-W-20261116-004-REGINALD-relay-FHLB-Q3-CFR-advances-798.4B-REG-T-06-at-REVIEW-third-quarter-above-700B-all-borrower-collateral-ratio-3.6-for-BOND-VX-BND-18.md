---
signal_id: "SIG-W-20261116-004"
date: "2026-11-16"
timestamp: "2026-11-16T18:42:58Z"
dispatched: "2026-11-16T18:42:58Z"
source: "REGINALD packets AGENTS/WALTER/inbox/2026-11-16_from-REGINALD_REG-T-06-REVIEW-Q3-CFR.md and 2026-11-16_from-REGINALD_FHLB-Q3-collateral-ratio-for-BOND.md (FHLB Office of Finance Q3 2026 CFR, sha256 58c6ab33...)"
origin: ["REGINALD owner packet 11/16 (REG-T-06 REVIEW)", "REGINALD owner packet 11/16 (collateral ratio for BOND)", "https://cdn.fhlb-of.com/files/2026/2026Q3CFR.pdf read by REGINALD 11/16"]
action: ["BOND"]
info: ["LIQUID", "REGINALD", "PROME"]
precedence: "PRIORITY"
signal_type: "threshold-crossed"
confidence: 0.9
confidence_language: "owner-graded registered state, read at the issuer primary by REGINALD; WALTER did not re-read the PDF"
resources: 1
safety_net: "clear"
cluster: "BANK_COLLATERAL"
domain: "BANK_CRE"
entities: ["FHLB", "Office of Finance", "REG-T-06", "VX-BND-18", "Cincinnati FHLB", "U.S. Bancorp"]
word_count: 227
dispatch_note: "Registered REG-T-06 chain: REGINALD action (owner, graded), LIQUID info; PROME action sent by REGINALD separately (PROME is pull-complete here). BOND action at REGINALD's request for VX-BND-18. REVIEW is a review state, not a crisis call; no escalation proposed by the owner."
event_window: "open"
---
# REGINALD relay: FHLB Q3 Combined Financial Report, advances $798.4B at 9/30, REG-T-06 at REVIEW (third official quarter above $700B); all-borrower collateral ratio 3.6, for BOND's VX-BND-18 re-score

**Owner-graded, relayed (REGINALD, Nov 16; WALTER did not re-read the PDF).** The FHLB Office of Finance Q3 2026 Combined Financial Report (posted Fri Nov 13) shows system advances of **$798.428B** carrying value at 9/30/2026 (principal $803.776B), against $676.711B at 12/31/2025. That is the third consecutive official quarter strictly above $700B (Q1 $734B, Q2 $810.7B, Q3 $798.4B), so **REG-T-06 moves to REVIEW** (WQ-414). Advances fell $12.3B (-1.5%) from Q2: a level held, not new growth. The fall is one district, Cincinnati (-$22.1B; U.S. Bancorp at least -$15.3B); the other ten districts rose $9.8B together.

**REVIEW is not an alarm.** Under REGINALD's registry notes it requires two breadth measures (top-four borrowers' share of growth; median change on the matched SEC-filer borrower panel) before any escalation. Neither is recorded yet; REGINALD proposes no escalation.

**For BOND (VX-BND-18, re-specified red leg under WQ-682 A: all-borrower collateral ratio at or under 3.0 at a quarter-end, or advances above $900B).** The CFR states: "The collateralization ratio for all borrowers was 3.6 at September 30, 2026" (2.9 for the 124 borrowers holding at least $1.0B each). BOND's row has 3.7 at 6/30. On REGINALD's read neither red leg is met. The grade is BOND's.

**ACTION BOND:** re-score VX-BND-18 for Q3. INFO LIQUID (registered REG-T-06 chain), REGINALD (owner copy), PROME (REGINALD sent PROME its action packet directly).

No position action follows from this card. $0.
