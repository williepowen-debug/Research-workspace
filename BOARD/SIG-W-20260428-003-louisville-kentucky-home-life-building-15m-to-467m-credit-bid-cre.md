---
signal_id: SIG-W-20260428-003
precedence: PRIORITY
timestamp: 2026-04-28T13:10:00Z
source: WALTER
origin: "Will Telegram image 2026-04-28 12:43 UTC (msg 1112) — Nightingale Associates @FCNightingale verified X post citing Louisville Courier Journal article on Kentucky Home Life Building lender takeback. Photo of building included in post."

to: REGINALD (ACTION — BANK_CRE primary)
info: BROCK, LIQUID, RED, NEXUS, PROME
group: CREDIT_CHAIN
dispatched: 2026-04-28T13:10:00Z
dispatch_note: "Specific lender-takeback transaction with hard mark-down number. Kentucky Home Life Building, Louisville KY (274,000 sqft, built 1912) purchased $15M in 2021 → taken by lender Fosco LLC via $4.67M credit bid 2026 = ~69% peak-to-credit-bid value erasure. ~$12.23M owed (two mortgages + unpaid taxes + code enforcement liens) well above the credit bid — implies $7.5M+ loss on the secured side. Vacant, boarded up, vandalism + security issues. REGINALD primary — bank-collateral-compression cluster node. Pairs with SIG-026-009 Baltimore CRE 29% properties / 28.7% avg + SIG-024-005 office vacancy 20.2% + SIG-026-002 residential housing weakening + SIG-026-014 Phoenix/Denver multi-family corrected-framing. Bank-collateral cluster now 5+ nodes Apr 24-28. Caveats: NOT WAL/OZK direct exposure — Fosco LLC is the lender entity, not a regional-bank constituent (likely a non-bank credit fund or distressed-debt LLC); sample-of-one not pattern; 1912 vintage building has structural-condition discount baked in beyond pure CRE-cycle markdown. Confidence 0.85 — Louisville Courier Journal primary, specific dollar figures, traceable. PRIORITY because bank-collateral compression cluster is active and this is a clean concrete data point illustrating current credit-bid-vs-debt math at lender takeback."

signal_type: pattern-match
confidence: 0.85
confidence_language: assesses
resources: 0
safety_net: clear

word_count: 320

# cluster backfilled 2026-06-10 from INDEX section placement (pre-v0.7 signal; cluster field added to FORMAT_SPEC 2026-05-05)
cluster: BANK_COLLATERAL
---

## Signal

Louisville Courier Journal via @FCNightingale (Nightingale Associates verified):

- **Property:** Kentucky Home Life Building, Louisville KY
- **Status:** Taken by lender Fosco LLC via **$4.67M credit bid**
- **Prior price:** Purchased **$15M in 2021** → ~**69% peak-to-credit-bid value erasure**
- **Debt outstanding (Feb 2026):** **~$12.23M** owed between two mortgages + unpaid taxes + code enforcement liens — well above the $4.67M credit bid
- **Implied lender loss on secured side:** ≥$7.5M
- **Physical condition:** Vacant, boarded up, vandalism + security issues
- **Specs:** 274,000 sqft, built 1912

## Relevance

- **REGINALD (ACTION — BANK_CRE):** Primary domain. Specific lender-takeback transaction with hard mark-down number — illustrates current credit-bid-vs-debt math at lender takeback events. **Bank-collateral-compression cluster node** — pairs with SIG-026-009 Baltimore CRE -29% properties / -28.7% avg + SIG-024-005 office vacancy 20.2% + SIG-026-002 residential housing weakening + SIG-026-014 Phoenix/Denver multi-family. Cluster now 5+ nodes Apr 24-28.
- **BROCK (info — backup):** CRE-CDO / non-bank credit fund angle — Fosco LLC is a non-regional-bank lender entity, illustrative of the non-bank distressed-debt market for older urban CRE.
- **LIQUID (info):** CRE markdown contributes to credit-conditions assessment.
- **RED (info — adversarial):**
  - Bull rebuttal: 1912-vintage building has heavy structural-condition discount baked in — the 69% mark-down conflates CRE-cycle markdown with deferred-maintenance/conversion-economics markdown. Sample-of-one not pattern.
  - Counter: Even discounted for structural-condition, $15M (2021) → $4.67M (2026) on a 274K sqft Class B/C urban core asset is illustrative of the broader Class B/C CRE cycle — and the $12.23M debt > $4.67M credit bid math (≥$7.5M secured loss) is real lender pain.
- **NEXUS (info):** Cluster classification for bank-collateral-compression overdue.

## Caveats

- **Fosco LLC = non-bank lender entity** (likely distressed-debt fund or credit LLC), NOT a KRE constituent — direct regional-bank-CRE-exposure inference does NOT apply.
- **1912-vintage building** has structural-condition / deferred-maintenance discount baked in beyond pure CRE-cycle markdown.
- **Sample-of-one** — single-property transaction, not aggregate pattern.
- Louisville-specific market dynamics (Class B/C office cycle, downtown Louisville vacancy) may not generalize.
- Source layer: @FCNightingale curator → Louisville Courier Journal primary; LCJ is established local journalism.
- Confidence 0.85 — primary sourcing, specific dollar figures, traceable to LCJ article.

## Source

- Will Telegram image 2026-04-28 12:43 UTC (msg 1112)
- Nightingale Associates @FCNightingale verified X post
- Primary: Louisville Courier Journal article on Kentucky Home Life Building lender takeback
- Cluster cross-references: SIG-026-009, SIG-024-005, SIG-026-002, SIG-026-014
