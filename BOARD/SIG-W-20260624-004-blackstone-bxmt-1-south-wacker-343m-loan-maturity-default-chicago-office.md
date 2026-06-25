---
signal_id: SIG-W-20260624-004
dispatched: 2026-06-25T01:50:00Z
origin: Will-Telegram image batch 2026-06-24 (batch 2) — Tobias Maximus @tmaxftw quoting Bloomberg @business (~6/24) "A Blackstone loan on an office tower in Chicago's financial center has gone into default"
source: Bloomberg @business (6/24) re BXMT $343M loan on 1 South Wacker; verify-corroborated by Crain's Chicago + The Real Deal Chicago (6/24)
signal_type: catalyst
domain: CRE
cluster: BANK_COLLATERAL
cluster_secondary: PC_STRESS
signal_role: primary_substance
narrative_channel: n/a
precedence: PRIORITY
to: CREED
info: [REGINALD, BROCK, RED]
confidence: 0.85
verify_verdict: CORRECTED-FRAMING — verify-research agent ae6086fd against Crain's + The Real Deal + Bloomberg + Trepp. The material correction: **Blackstone is the LENDER (BXMT), not the building owner.**
verify_method: WebSearch/WebFetch verify-research ($0.05). Event CONFIRMED + specifics filled (tower, loan size, default type, occupancy); the "Blackstone loan defaulted" headline ambiguity resolved → Blackstone Mortgage Trust originated the loan; the BORROWER defaulted.
routing_note: national CRE/CMBS market-stress → CREED action per ROUTING_TABLE v0.12; REGINALD (bank-CRE) / BROCK (BXMT = Blackstone-affiliated CRE mortgage-REIT lender — elevated relevance, this is a BXMT credit event too) / RED info. cluster BANK_COLLATERAL (office distress); cluster_secondary PC_STRESS (mortgage-REIT/alt-lender credit). primary_substance (confirmed marquee event; the nuance is already-priced-trend not leading-edge).
---

# Blackstone Mortgage Trust's $343M loan on 1 South Wacker (Chicago) hits maturity default — marquee office datapoint, but Blackstone is the LENDER not the owner

**One line:** **Blackstone Mortgage Trust (BXMT) originated a $343M loan on 1 South Wacker Drive** (40-story Helmut Jahn tower, Chicago Loop financial district); the loan hit **maturity default on 6/9** when the borrower (601W Companies, bought 2018-19 ~$310M) didn't repay. ~$159M is securitized in CMBS; building 73% occupied; on BXMT's watchlist since 2022 (<2% of portfolio). The Bloomberg headline reads as "a Blackstone loan defaulted" — correct, but **Blackstone is the LENDER here, not the building owner** (a common misread).

> **GRADE: verify-research, CORRECTED-FRAMING 0.85.** Real, current, marquee-name. The lender-vs-borrower clarification is the framing that must travel. Nested in a structural office-distress wave (national office CMBS DQ 11.71% / office special-servicing 16.73%, Trepp Mar-2026; Chicago CBD vacancy ~27%) — confirms the trend grinding on, **already-priced more than leading-edge.**

## Verify verdict block

**CONFIRMED + specifics filled:**
- **Building/loan (0.90):** 1 South Wacker Drive, 40-story / 1.2M sq ft; BXMT $343M loan; borrower 601W Companies; ~$159M securitized into CMBS, rest balance-sheet.
- **Default type (0.90):** MATURITY default (loan matured 6/9, principal not repaid). Not yet a confirmed special-servicing transfer.
- **Context (0.85):** occupancy 73%; nearby comp 175 W. Jackson sold for $41M = 87% markdown from $306M pre-Covid (no published 1 S. Wacker appraisal mark yet); Chicago CBD vacancy ~27%; BXMT shares −3.7% to $17.48 on the news.

**CORRECTED-FRAMING:**
- **Blackstone = LENDER (BXMT originated the loan), NOT the borrower/owner.** The owner that defaulted is 601W Companies. The signal is a BXMT *credit event* (a loan on its book going bad) AND an office-CRE *collateral* event — route both lenses, but don't say "Blackstone's building defaulted."

## Per-recipient genuine delta

### → CREED (ACTION) — national CRE/CMBS feed; your domain
1. Marquee Chicago Loop office maturity default — 1 S. Wacker, $343M BXMT loan, borrower 601W can't refi/repay at maturity. ~$159M in CMBS = watch the special-servicing transfer + any appraisal reduction (ARA) when it lands.
2. **Read it as trend-confirmation, not a new leading edge:** it sits inside office CMBS DQ 11.71% / special-servicing 16.73% (Trepp Mar-2026) + Chicago CBD ~27% vacancy. The marquee-name (Blackstone-affiliated lender) is what makes it headline-worthy, not a new mechanism.
3. The "maturity default" type matters — it's a refi-wall failure (borrower can't refinance at current rates/values), the dominant office-CMBS default mode. Track whether 601W gets an extension/modification (extend-and-pretend) or it goes to liquidation.

### → REGINALD (INFO) — bank-CRE cross-reference
Office maturity defaults at this scale feed the bank/CRE-collateral picture you track, but this is a CMBS/mortgage-REIT loan (BXMT), not a regional-bank-held loan — cross-reference, not a bank-level tripwire. Relevant to the broader "office values tumbled → refi wall" backdrop behind your CRE-DQ-by-tier read.

### → BROCK (INFO) — BXMT credit event (your alt-lender/mortgage-REIT lane)
This is a Blackstone Mortgage Trust credit event: a $343M loan on its book in maturity default (on watchlist since 2022, <2% of portfolio, but BXMT −3.7% on the news). Office-CRE losses landing on a marquee alt-lender's balance sheet = the mortgage-REIT analog to your BDC-NAV-mark thread. Watch BXMT's reserve build / dividend coverage if office defaults accelerate.

### → RED (INFO)
The Tobias Maximus framing ("all these CRE losses will hit the economy → reduced credit/lending → much lower rates, $TLT") is the recession-transmission/bull-duration read — note it connects to the same-day TLT bid (SIG-W-20260624-002). Steelman: real refi-wall stress vs already-priced/contained (single watchlist loan, <2% of BXMT, trend long known). Lender-not-borrower correction is the framing discipline.

## Sources
- Crain's Chicago Business 6/24/2026; The Real Deal Chicago 6/24/2026; Bloomberg 6/24/2026 (BXMT $343M 1 S. Wacker default).
- Trepp via CommercialSearch Mar-2026 (office CMBS DQ 11.71% / special-servicing 16.73%).
- Verify agent: ae6086fd1494a32fd.
