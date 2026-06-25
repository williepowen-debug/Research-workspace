---
signal_id: SIG-W-20260624-007
dispatched: 2026-06-25T02:20:00Z
origin: Will-Telegram image batch 2026-06-24 (batch 3) — Finance News @ftfinancenews "US banks would lose $700bn in economic crash, Fed stress tests find"
source: FT @ftfinancenews relaying FT.com; underlying = Federal Reserve 2026 DFAST results (press release bcreg20260624a, 6/24 4pm EDT)
signal_type: catalyst
domain: BANK_CAPITAL
cluster: BANK_COLLATERAL
cluster_secondary: FED_FRAMEWORK
signal_role: counter_evidence
narrative_channel: n/a
precedence: PRIORITY
to: REGINALD
info: [BROCK, LIQUID, RED]
confidence: 0.88
verify_verdict: CORRECTED-FRAMING — verify-research agent a39395bb against the Fed DFAST press release + CNBC + Bloomberg. The "$700bn loss" headline buries the lede: the banks PASSED comfortably.
verify_method: WebSearch/WebFetch verify-research ($0.05). Primary Fed release confirms; specifics filled (pass/fail, CET1 drawdown, scenario severity, SCB-freeze, regional-coverage caveat).
routing_note: BANK_CAPITAL → REGINALD action per ROUTING_TABLE; BROCK (NDFI/PC) / LIQUID / RED info. signal_role counter_evidence (bull-counter to the regional-bank short). cluster BANK_COLLATERAL (bank capital/regulatory); cluster_secondary FED_FRAMEWORK (extends the bank-capital-deregulation thread SIG-W-20260618-006). **Load-bearing caveat: DFAST covers the 32 LARGE banks only — the small/mid regionals (KRE/WAL/OZK tier) that drive REGINALD's short are NOT tested.**
---

# Fed DFAST 2026: $708bn projected losses but ALL 32 banks PASS (CET1 −1.6pp) + SCB freeze = capital-return tailwind — bull-counter to the bank short, but regionals weren't tested

**One line:** The Fed's 2026 stress test (DFAST, released 6/24 4pm EDT) projects **$708bn** in losses under the severely-adverse scenario (unemployment→10%, CRE −39%, home prices −30%) — but **all 32 banks passed**, aggregate CET1 fell only **1.6pp (12.8%→11.2% trough, rebounding to 12.7%)**, and with **stress capital buffers frozen until 2027** (methodology rework), the results clear the way for buybacks/dividends. The FT "would lose $700bn" headline is the scary framing of a comfortably-passed test.

> **GRADE: verify-research, CORRECTED-FRAMING 0.88.** Primary Fed release. **Bull case dominates** — passed comfortably + scenario not toughened under the deregulation-leaning Fed + SCB-freeze capital-return tailwind = a counter to a regional-bank short, NOT support for it. **BUT the load-bearing caveat: DFAST tests only the 32 LARGE banks; the small/mid regionals (KRE/WAL/OZK tier) that drive REGINALD's thesis are largely NOT tested** — so this de-risks the big banks without speaking to the regional-stress thesis directly.

## Verify verdict block

**CONFIRMED + specifics:**
- **Event (0.95):** Fed 2026 DFAST, 6/24 4pm EDT (bcreg20260624a). $708bn+ total projected loan losses (FT rounded to "$700bn"). Loss mix ~$200bn cards / $160bn C&I / $75bn CRE.
- **Pass (0.95):** all 32 banks stayed above minimum CET1; aggregate CET1 −1.6pp (12.8%→11.2% trough → 12.7% rebound). Comfortable cushion.
- **Scenario (0.85):** Fed says "similar in severity" to 2025, but higher starting unemployment (smaller jump) + already-low home prices (smaller decline) + trimmed commodity/oil global-market shock = effectively milder in places; capital decline slightly larger than 2025 (higher loan losses).
- **Capital return (0.90):** results do NOT change capital requirements — **SCBs frozen until 2027** pending methodology rework (averaging/transparency). Big banks + some regionals (Regions $3bn buyback, Zions, Prosperity) returning capital. No KRE/WAL/OZK-tier name flagged weak (because not in the 32).

**CORRECTED-FRAMING:**
- "$700bn loss" → it's $708bn, and the buried lede is the PASS + the capital-return tailwind. Bull-counter, not bear.

## Per-recipient genuine delta

### → REGINALD (ACTION) — bull-counter to the bank short, but read the coverage caveat
1. **The dominant frame is bullish-for-banks** (counter to your thesis): 32 banks passed with a small 1.6pp CET1 drawdown; the Warsh-Fed did NOT toughen the scenario; SCBs frozen to 2027 = a buyback/dividend tailwind across the big banks. This is the deregulation-capital-return leg compounding SIG-W-20260618-006.
2. **But it does NOT refute your regional short:** DFAST tests only the 32 LARGE banks. **The KRE/WAL/OZK small/mid-regional tier that drives your thesis is largely NOT in the test** — so "banks passed" de-risks the GSIBs/big-regionals, not the cohort you're short. Don't let the headline talk you out of the regional-specific stress (CRE-DQ-by-tier, SBCF/AMTB leading-creep). The test's own CRE −39% / $75bn-CRE-loss scenario actually underscores the CRE channel you track.
3. Net: a genuine bull-counter datapoint to log on the kill-list (capital-return tailwind for the sector), with the explicit scope caveat that your idiosyncratic-regional bear sits below the tested universe.

### → BROCK (INFO) — NDFI/PC angle
The stress test is bank-only; it does NOT capture the $1.8T private-credit / NDFI exposure that Barr (6/6) and Lee Robinson (SIG-W-20260624-009 same batch) flag as the unmeasured risk. "Banks passed" + "PC/NDFI untested" = the exact oversight-gap scissor — the resilience headline is for the regulated core, not your shadow-credit lane.

### → LIQUID (INFO)
SCB-freeze + capital-return clearance = more bank buybacks/dividends = a (mild) liquidity/flows tailwind at the index level, against the same-day risk-off tape. Bank capital is ample (CET1 11.2% trough), not the stress vector right now.

### → RED (INFO, counter_evidence)
Steelman: bull = "banks passed comfortably, scenario eased, capital-return cleared = bank resilience confirmed, bear-thesis headwind"; bear = "$708bn loss bigger than 2025, CRE/card concentration, AND the test conveniently excludes the small regionals where the actual stress thesis lives + ignores the $1.8T PC/NDFI exposure = a resilience theater for the tested core." The scope-exclusion is the key both-sides hinge.

## Sources
- Federal Reserve 2026 DFAST press release (bcreg20260624a), 6/24/2026 4pm EDT.
- CNBC "Fed stress test: U.S. banks can withstand $708B in losses" 6/24; Bloomberg "Big Banks Pass Fed Stress Test, Paving Way for Payouts" 6/24; FT.com.
- Verify agent: a39395bb9773840e9. Pairs with SIG-W-20260618-006 (bank-capital deregulation).
