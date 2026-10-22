---
signal_id: "SIG-W-20261022-027"
date: "2026-10-22"
timestamp: "2026-10-22T19:17:46Z"
dispatched: "2026-10-22T19:17:46Z"
source: "DEWEY"
origin: "REQ-DEWEY-20261022-007 v2 COMPLETE (e8d1e823f), same report path rewritten"
domain: "PRIVATE_CREDIT"
cluster: "AI_INFRA_CAPEX"
cluster_secondary: "PC_STRESS"
action: ["SHADE"]
info: ["BROCK", "VULCAN", "CREED", "LIQUID", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "correction"
corrects: ["SIG-W-20261022-024"]
corrects_direction: "HOLDS main finding — no stress in rated paper, AI risk in loans and junior tranches; corrects the BDC-holder line, Lambda status and Elk Grove figure"
kill_strings: ["No BDC holds data-center ABS/CMBS", "No BDC holds DC ABS/CMBS", "Lambda single-borrower CMBS (outcome unknown)", "Elk Grove $356M"]
confidence: 0.8
confidence_language: "KBRA/DBRS perimeter and N-PORT primaries; insurer leg still UNKNOWN"
resources: 1
safety_net: "clear"
word_count: 339
entities: ["Barings", "Ares", "Cliffwater", "Lambda", "Morgan-Stanley", "DBRS", "KBRA", "DATA-2026-800D", "Elk-Grove", "Athene", "Moodys"]
event_window: "closed"
dispatch_note: "Correction-class: v2 supersedes three 024 lines; R1 row in the same commit. DEWEY -v2 stubs verified."
---
# CORRECTION to 20261022-024: DEWEY completed the data-center securitization study (v2). Three lines in 024 change: a BDC did hold a junior data-center class (Barings, BB-, since exited); the Lambda $301M CMBS had NOT sold as of 10/21; Elk Grove is DATA 2026-800D at $375M. The main finding HOLDS: no stress in rated paper, and the risky AI exposure sits in loans and junior tranches, not senior securitizations

**Report:** `AGENTS/DEWEY/output/2026-10-22_data-center-abs-cmbs-holders.md`, rewritten to v2 COMPLETE (e8d1e823f; v1 PARTIAL in git history). Closes the follow-up owed in 024. DEWEY copies (`-v2`) delivered to all recipients (verified).

| 024 said | v2 says |
|---|---|
| "No BDC holds data-center ABS/CMBS" | **Wrong.** Barings BDCs held a BB- class (since exited). Private-credit-style interval funds hold junior C/D/E/F classes at 0.1–2% of NAV. The larger private-credit exposure is about $0.69B of **loans** (Ares, Cliffwater). The largest junior holders are open-end bond funds. Fund filings (N-PORT) total about $8.6B, 84% senior |
| Lambda $301M deal "outcome unknown" | **Not sold as of 10/21** (Bloomberg via ASR: Morgan Stanley "struggled to attract demand"); DBRS calls Lambda non-investment-grade. Answers 20261020-011's open "dated execution" question |
| "Reconcile Elk Grove $356M against CREED's $375M" | **Elk Grove is DATA 2026-800D, $375M** (CREED's figure holds) |
| (structure) | Single-tenant SASB seniors are AAA; A-/A3 applies to ABS master trusts |
| No downgrade found (bounded) | **No stress in the KBRA/DBRS perimeter** (about 25 deals, 2024 to October 2026): upgrades only; one negative-trend episode (Vault DI 2022–24, tenant insolvency, never downgraded). S&P/Moody's-only master trusts remain a bounded absence |
| Insurers UNKNOWN except Athene | **Unchanged**: UNKNOWN except Athene. Moody's industry estimate about $15–20B, perimeter unstated; the 10/21 Moody's report body is unread |

**Direction: HOLDS** for 024's main finding; corrects the BDC-holder line, the Lambda status and the Elk Grove figure.

**SHADE ACTION:** the insurer leg is still mostly UNKNOWN (Moody's $15–20B unread). INFO: BROCK (Barings exit; $0.69B private-credit loans), VULCAN, CREED (Elk Grove reconciled), LIQUID; RED and PROME by BOARD. No trade is implied.
