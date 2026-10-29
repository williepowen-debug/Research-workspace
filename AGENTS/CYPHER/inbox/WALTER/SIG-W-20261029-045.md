---
signal_id: "SIG-W-20261029-045"
date: "2026-10-29"
timestamp: "2026-10-29T19:39:22Z"
dispatched: "2026-10-29T19:39:22Z"
source: "x-bookmark (Will) @PolymarketTrade 2115874609014726842 (company account) + @FinanceLancelot 2115875276789887456"
origin: ["x-bookmark 2115874609014726842 @PolymarketTrade 2026-10-29T18:33Z", "x-bookmark 2115875276789887456 @FinanceLancelot 2026-10-29T18:35Z", "thedefiant.io / forklog.com (June 2026 precedent, search results)"]
domain: "CYBER"
cluster: "CYBER"
action: ["CYPHER"]
info: ["ORACLE", "PROME", "RED"]
precedence: "PRIORITY"
signal_type: "context"
confidence: 0.8
confidence_language: "Halt and third-party compromise from Polymarket's own account (primary for what it says); 'accounts drained' is user reports relayed by one account, size unknown; no news coverage indexed at 15:4x ET"
entities: ["Polymarket"]
resources: 2
safety_net: "clear"
event_window: "closed"
word_count: 158
dispatch_note: "Will bookmarks (2). BOARD grep: no Polymarket hack card. NO-OWNER class (crypto/prediction-market platform) per v0.48: CYPHER action, PROME info. ORACLE info because Polymarket is its price source: halted trading and drained accounts make today's odds unreliable. Delivery and consumption separate."
---
# Polymarket (international platform) halted trading 10/29 after one of its third-party providers was compromised; it says affected users will be made whole. Users report drained accounts. Second vendor-route incident since June

- **Polymarket's own account (@PolymarketTrade, 18:33Z 10/29):** "One of our 3rd party providers was compromised"; referred to law enforcement; "Anyone who has been impacted will be made whole"; trading on Polymarket.com **temporarily halted**. The US-regulated platform is not mentioned.
- **User reports (@FinanceLancelot, 18:35Z):** accounts "being drained of funds". Count and dollar size **unknown**; no news report indexed yet.
- **Precedent (June 25–26, 2026, secondary):** a compromised vendor injected a malicious script into Polymarket's website; about $3M stolen from fewer than 15 accounts; smart contracts and back-end untouched. A May incident involved a leaked wallet key. Whether today repeats the June route is **not established**.

**Why it matters:** ORACLE reads Polymarket odds as a fleet input. While trading is halted, and if accounts were drained, today's prices are not a clean crowd read. Small direct money channel otherwise.

ACTION CYPHER: open or decline an incident row (no-owner class). Info: ORACLE (treat 10/29 Polymarket prints with care), PROME, RED.
