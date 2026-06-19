---
signal_id: SIG-W-20260618-006
dispatched: 2026-06-18T23:55:00Z
origin: Will Telegram legal-headline triage (msgs 2366-2368, 2026-06-18 ~23:49 UTC) — "should we investigate any of these?"
source: Holland & Knight (6/16/2026, "U.S. Banking Agencies Propose New Rules to Reduce Regulatory Capital Requirements for Banks") = comment-deadline recap of the OCC/FRB/FDIC joint proposal of 2026-03-19 (comment deadline 2026-06-18)
signal_type: thesis-frame
domain: BANK_CRE
cluster: FED_FRAMEWORK
cluster_secondary: BANK_COLLATERAL
signal_role: cluster_mediating
precedence: PRIORITY
to: REGINALD
info: [RED, LIQUID, BROCK, HENRY]
confidence: 0.90
verify_verdict: CORRECTED-FRAMING (substance CONFIRMED 0.92; date-framing corrected — proposed 2026-03-19, comment deadline 2026-06-18, NOT a fresh June proposal as the H&K headline reads)
verify_method: WebSearch primary — FDIC/Fed/OCC joint release 2026-03-19 (bcreg20260319a) + Federal Register 2026-05959 + Holland & Knight memo + Banking Dive/American Banker + federalreserve.gov/barr20260606a + Fed June 2026 S&R Report + Bowman testimony 6/4. Sub-agent verify-research agent_id ae3cab8f2bc58beea, ~$0.05
---

# US banking agencies cutting bank capital requirements (3 interconnected rules) — the relief REACHES THE REGIONAL COHORT; Barr dissents

## Substance (verify-research CONFIRMED 0.92; CORRECTED-FRAMING on date)

**Framing correction first:** this is NOT a fresh June proposal. OCC + FRB + FDIC jointly **proposed the package 2026-03-19**; the **comment deadline is today, 2026-06-18** — which is the news peg the law-firm recaps (Holland & Knight et al.) are hanging on. Not previously dispatched to the BOARD, and the substance is load-bearing.

**Three interconnected rules (FDIC/Fed/OCC primary + H&K):**
1. **Expanded Risk-Based Approach (ERBA) for Category I/II** — the Basel III "Endgame" RE-PROPOSAL, superseding the July 2023 framework. **~4.8% CET1 cut for GSIBs.**
2. **Revised Standardized Approach for Category III/IV + smaller** — eliminates MSA deductions; mandatory AOCI inclusion for >$100B banks (5-yr phase-in). **~5.2% CET1 relief for Cat III/IV regionals; ~7.8% for community banks.**
3. **GSIB surcharge recalibration** (Method 2 + eSLR tied to 50% of Method-1 surcharge) — **~40bps / ~$23B aggregate / ~10% surcharge cut. GSIB-only.**

**🔑 LOAD-BEARING FINDING — the relief reaches REGIONAL banks, not just GSIBs.** Rule 2 gives the **Category III/IV tier (~$100B-700B assets — the KRE/WAL/OZK/regional cohort) ~5.2% CET1 relief** plus the AOCI phase-in. This is system-wide capital-standard relief, NOT a GSIB-only eSLR story. (Could not independently confirm the exact $23B aggregate on primary — H&K-sourced, plausible.)

**The deregulation-vs-stability debate is clean and real (both sides primary-confirmed):**
- **Barr (Fed Governor), 6/6/2026 speech (American University):** the current deregulation is the **"most significant since 2008"**; warns it will make the system "less robust… when the bill comes due, we will all pay the price"; urged TIGHTER (not looser) rules to manage **nonbank/NDFI risk**. (federalreserve.gov/barr20260606a)
- **Fed June 2026 Supervision & Regulation Report + Bowman testimony 6/4:** banking system **"sound and resilient,"** strong capital ratios + liquidity buffers — the official all-clear.

## Source confirmation (2026-06-19 — Will pasted the full Holland & Knight text post-dispatch)

The full H&K alert confirms the verify-research figures VERBATIM and adds detail:
- **CET1 relief exact match:** "up to an estimated **4.8 percent for Category I and II GSIB** organizations, **5.2 percent for Category III and IV regional** banking organizations, and **7.8 percent for community** banking organizations." → the routed numbers are now primary-source-exact, not just verify-research.
- **Not pure one-way deregulation — a re-regulation tucked inside:** Bowman frames it as "modernize"; the proposals **bring mortgage origination & servicing BACK within the Agencies' regulatory perimeter** — a partial offset to the capital relief REGINALD should weigh (perimeter EXPANSION on mortgage activities while capital requirements FALL).
- **Mechanics:** formally rescinds the 2023 Basel III Endgame Framework; eliminates the Cat I/II **Dual-Stack / Advanced-Approaches** calculation → single **ERBA** (standardized credit / equity / operational / market / CVA risk); 3 NPRs combined **>1,500 pages**, touching nearly every section of the capital rules.
- **Outlook (H&K verbatim):** less-stringent capital = "greater balance sheet flexibility… increased lending, strategic investments, **share buybacks and acquisition considerations**" — confirms the cohort-tailwind read + the M&A/consolidation angle (pairs the FCBM signal SIG-W-20260618-005).

**Full H&K text — additional load-bearing detail (Will pasted parts 2-5, msgs 2373-2376):**
- 🔑 **AOCI inclusion for Cat III/IV = the catch on the regional relief.** The Revised Standardized Approach will REQUIRE Cat III/IV (>$100B — the WAL/KRE/OZK tier) to **include AOCI in CET1** (5-yr phase-in); currently only Cat I/II do. AOCI inclusion generally REDUCES CET1 and is the **exact SVB-2023 mechanism** (unrealized securities losses flow to capital). Landing as the Fed flips cut→HIKE → for the regional cohort the headline "~5.2% relief" is partly clawed back through the most rate-sensitive channel. **This tilts the regional-cohort read toward the bear/stability side, not the tailwind.** (Tell: SA decrease ~8.6% covered DIs / ~6.8% covered HCs is "assuming no AOCI impact" — AOCI is the offset.)
- **ERBA is OPT-IN for regionals.** ERBA is mandatory only for Cat I/II GSIBs; Cat III/IV are NOT obligated (may opt-in for risk-sensitivity on mortgage/corporate/retail). The 5.2% Cat III/IV relief comes via the **Standardized Approach**, not ERBA.
- **MSA deduction → 250% risk weight** (eliminates the punitive 10%/25%-of-CET1 threshold deduction) — explicitly "to promote mortgage origination & servicing by banks"; Bowman: "reduce incentives for traditional lending… to migrate outside the regulated banking sector" (the perimeter point, with mechanism).
- **GSIB-side partial offsets:** NEW explicit **operational-risk charge** (RWA = 12.5× Business Indicator Component ≈ 8% capital charge — first time, Cat I/II) + NEW explicit **CVA-risk charge** (Cat I/II + ≥$1T-notional-derivative books) ADD capital for GSIBs, offsetting part of their 4.8%. Securitization: SEC-SA replaces SSFA; 100% RW floor on senior tranches of **nonperforming-loan** securitizations; credit-enhancing interest-only strips deducted from CET1. Market-risk threshold raised $1B→$5B trading assets (fewer firms covered).
- **Off-balance-sheet:** non-unconditionally-cancelable commitments now uniform **40% CCF** (was 20%/50% by maturity); "highest-drawn-over-24-months" exposure method for no-preset-limit commitments (most pertinent to Cat III); unconditionally-cancelable stay 0%.
- 🔴 **Barr's dissent is FORMAL + concrete:** FRB voted **6-1, Barr the sole dissent**; he disputes Bowman's "modest deviations" framing and charges the proposals carry **"over 20 material downward deviations" from BCBS agreed-upon minimum capital requirements** — a much stronger adversarial anchor than the 6/6 speech alone. Final-rule shape depends on comment-period feedback (comments due 6/18).

## Why it matters — cluster_mediating, cuts both ways

This is genuinely **cluster_mediating** — it's the regulatory hinge under the bull/bear bank debate:

- **Near-term TAILWIND (bull / counter to the short):** ~5.2% CET1 relief for the regional cohort is real capital headroom — more buyback/lending/M&A capacity. It's the **regulatory leg of the "deregulation tailwind"** that the bank-equity rally + the FCBM regional-bank-revival narrative (SIG-W-20260618-005, same session) explicitly rest on. Pairs with the IAT regional-bank +33.4% trailing-12mo tape (killed-but-logged this session).
- **Longer-term AMPLIFIER (bear / systemic):** a thinner capital cushion going INTO a credit cycle where office-CRE / NDFI / hidden-CRE are deteriorating is exactly Barr's "when the bill comes due" point. Capital relief doesn't fix credit quality — it removes buffer against it. This compounds the **oversight-capacity scissor** already on the board (SIG-W-20260511-013 FDIC/Fed supervision STAFF cuts 30%) and the **NDFI breakout** (SIG-W-20260511-014/-026/-029 — $1.4T NDFI, Barr's named nonbank risk).

**Regime-timing note:** the relief lands as the Fed flipped **cut→HIKE 6/17** — capital relief easing while rates tighten is a mixed regime for the cohort (relief on capital, pressure on credit/funding).

## Recipients

- **REGINALD (action):** bank-capital is your lane; ~5.2% Cat III/IV relief directly affects the WAL/OZK/KRE cohort's capital math (buyback capacity, CET1 headroom, the Bear-medium probability mass). Comment deadline today; final rule is the forward catalyst.
- **RED (info, auto-cc cluster_mediating + CORRECTED-FRAMING):** the adversarial pairing — Barr's 6/6 "bill comes due" dissent vs. the dereg push vs. Bowman/S&R "banks sound." Steelman both: does capital relief earn weight against a credit-quality short, or is it the setup Barr's warning describes?
- **LIQUID (info):** financial-stability / funding — thinner system-wide capital + Barr's nonbank-risk flag.
- **BROCK (info):** Barr explicitly named **nonbank/NDFI risk** — the PC/BDC fragility you track is the other half of his warning.
- **HENRY (info):** the deregulation tailwind that's underpinned the bank-equity rally + the cut→HIKE regime tension.

## Source framing

Holland & Knight (credible law firm) is the recap source; the proposal + magnitudes are FDIC/Fed/OCC-primary-confirmed. The only correction is the date ("new June proposal" → 3/19 proposal, 6/18 deadline). Barr + S&R report both primary-confirmed.

## AIGs / cross-refs

- BOARD: SIG-W-20260618-005 (FCBM regional-bank-revival — deregulation tailwind, same session), SIG-W-20260511-013 (FDIC/Fed supervision STAFF cuts — oversight scissor), SIG-W-20260511-014/-026/-029 (NDFI breakout — Barr's named nonbank risk), SIG-W-20260522-005 (Waller pivot — Fed regime), SIG-W-20260426-001 (Fed operating-framework shift)
- This session's killed-but-logged IAT regional-bank +33.4% tape (kill_log 6/18)
- ROUTING_TABLE BANK_CRE → REGINALD action ("capital rules" in BANK_CRE domain)

## Provenance

- Intake: Will Telegram legal-headline triage (msgs 2366-2368, "should we investigate any of these?"), 2026-06-18 ~23:49 UTC. WALTER triaged ~24 headlines across the dump; this capital-rule cluster (#2 + Barr #11 + S&R #8) was the only dispatch-worthy item — rest killed/monitor (EU/UK prudential plumbing, fraud-education, Colorado usury + Illinois interchange litigation = monitor, no ruling).
- Pipeline: BOARD-grep novel (no prior capital-rule-rollback dispatch) → Phase 1.5 verify-research (regulatory substance + magnitude + who-benefits) → CORRECTED-FRAMING 0.90 → dispatch
- Verify-research sub-agent: WebSearch primary sweep, ~$0.05, agent_id ae3cab8f2bc58beea
