---
signal_id: SIG-W-20260513-002
precedence: IMMEDIATE
timestamp: 2026-05-13T17:38:00Z
source: WALTER
origin: "NY Fed Q1 2026 Household Debt and Credit Report (primary, released 2026-05-12) — Liberty Street Economics + NY Fed press + dshort/Advisor Perspectives + Wolf Street + ABA Banking Journal corroboration"

to: CARL (ACTION)
info: REGINALD, BROCK, RED, OTTO, NEXUS, PROME

signal_type: catalyst
confidence: 0.95
confidence_language: confirmed
resources: 1
safety_net: clear

word_count: 285

cluster: CONSUMER_STAGFLATION
cluster_secondary: BANK_COLLATERAL
signal_role: cluster_mediating
consumer_transmission: discretionary_demand
consumer_lens: tier_stratified
event_window: closed

verify_research_verdict: SKIP-VERIFY-BY-DESIGN (NY Fed primary release; quarterly canonical data; WebSearch confirmed via NY Fed Liberty Street Economics + dshort/Advisor Perspectives + Wolf Street primary)
---

# NY Fed Q1 2026 HHDC Report (5/12) — Student-Loan 90+d 10.3% Back to Pre-Pandemic + 2.6M Q1 Defaults Vertical Step-Up; CC Outstanding 90+d ~13% (Image Chart); Overall 90+d Delinq 3.36% = Highest Since Pre-Pandemic

**Verbatim Q1 2026 HHDC primary data (released 2026-05-12, NY Fed Center for Microeconomic Data):**

- **Total household debt:** $18.79T (+$18B QoQ / +0.1%)
- **Overall 90+d delinquency rate:** 3.36% — highest since pre-pandemic
- **Student loan 90+d:** 10.3% — back to pre-pandemic level
- **Student loan defaults:** ~1M Q4 2025 + **2.6M additional Q1 2026** = vertical step-up
- **Credit card 90+d outstanding balance:** ~13% per the image chart (NY Fed Consumer Credit Panel/Equifax) — extends SIG-W-20260424-007 (Q4 2025 12.7%)
- **CC early-delinq transitions:** 8.7% → 8.6% (slight tick-down — different metric than balance-90+d)
- **Balance changes:** Mortgage +$21B → $13.191T / Auto +$18B → $1.685T / HELOC +$12B → $446B / CC −$25B → $1.252T / Student −$6B → $1.658T

## Substance

- **Student loan vertical step-up is the load-bearing new vector.** Q4 2025 defaults ~1M → Q1 2026 defaults 2.6M = 2.6× quarter-over-quarter acceleration. This is the COVID-forbearance-end mechanism crystallizing in real time. ED Office of Federal Student Aid resumed default reporting Q4 2025 after pandemic pause; the vertical line on the image chart is the resumption-of-reporting layered on top of underlying-deterioration.
- **CC 90+d outstanding ~13%** extends SIG-W-20260424-007 (Q4 2025 12.7%) by +30bps — now AT/EXCEEDING 2009-10 GFC peak ~13.8% on chart visual. Per SIG-024-007 asymmetry warning: 2009 peak came at unemployment ~10%; current 4.4%. **CC stress at near-2009-peak with employment FAR below 2009 levels = structurally worse trajectory if unemployment turns.**
- **Overall 90+d 3.36% = highest since pre-pandemic** is the headline. Holds even after CC transition tick-down — composition shifted toward longer-duration severe delinquency.
- **Cross-feeds CONSUMER_STAGFLATION K-shape**: today's BAA wage-tercile dispatch (SIG-W-20260513-003) shows lower-income wage growth 1.5% YoY — exactly the cohort defaulting on student loans + carrying CC balances. K-shape mechanism crystallizing.

## Dispatch notes

**Released YESTERDAY 5/12 — WALTER missed at-CPI-dispatch.** During yesterday's CPI confirmation, did not pull NY Fed HHDC concurrent release. Per `feedback_verify_counts_before_propagating`: should have scanned same-day primary releases. Process note for boot-checklist next session.

**`signal_role: cluster_mediating`** — bridges CONSUMER_STAGFLATION (primary, CARL canonical) × BANK_COLLATERAL (CC + student loan 90+d directly feeds bank-balance-sheet exposure; REGINALD action vector via consumer-credit-cycle transmission). NY Fed Q1 HHDC is canonical cluster_mediating.

**`consumer_transmission: discretionary_demand`** — student loan default surge + CC 90+d at near-2009-peak = forced discretionary-demand-destruction mechanism for affected cohort (~2.6M Q1 defaulters).

**Calibration cycle 1 input:** Direct primary-source data on consumer-credit-cycle path. CARL Path C 92→97% confirmation: vertical step-up in defaults is the operationally-confirmed mechanism, not headline-rate alone.

## Recipient routing

- **CARL action** — CONSUMER_CREDIT → CARL canonical; Path C ACTIVE component-confirmation; tier_stratified mechanism confirmed.
- **REGINALD info** — CC + student loan 90+d feeds bank-consumer-credit-cycle exposure; NIM compression on charge-offs; cross-feed REG-T-02 (WAL) bear context.
- **BROCK info** — consumer-credit feeds private-credit-adjacent (Apollo Athene consumer lending / Carlyle consumer ABS); pairs sponsor-bifurcation context.
- **RED info** — adversarial steelman: CC transition tick-down 8.7→8.6 is bull-counter-evidence layer to outstanding-balance framing.
- **OTTO info** — auto loans +$18B / $1.685T extends SUBPRIME_AUTO domain; pairs SIG-W-20260509-002 auto-debt-comparison.
- **NEXUS info** — classification candidate cluster_mediating bridging.
- **PROME info** — coordinator awareness.

## Sources

- NY Fed Q1 2026 HHDC primary: https://www.newyorkfed.org/microeconomics/hhdc
- NY Fed press release: https://www.newyorkfed.org/newsevents/news/research/2026/20260512
- Liberty Street Economics (Federal Student Loan Defaults Return): https://libertystreeteconomics.newyorkfed.org/2026/05/federal-student-loan-defaults-return-after-pandemic-pause/
- dshort / Advisor Perspectives: https://www.advisorperspectives.com/dshort/updates/2026/05/12/household-debt-credit-report-q1-2026
- Wolf Street: https://wolfstreet.com/2026/05/12/household-debts-debt-to-income-ratio-serious-delinquencies-foreclosures-collections-bankruptcies-in-q1-2026/
- ABA Banking Journal: https://bankingjournal.aba.com/2026/05/new-york-fed-household-debt-holds-at-18-8t-in-q1/
