---
signal_id: SIG-W-20260521-008
precedence: PRIORITY
timestamp: 2026-05-21T23:30:30Z
source: WALTER
origin: "REGINALD 2026-05-17 commit `1b37fccc` WAL Investor Day 5/12 post-mortem; WAL Investor Day public presentation + Q&A 2026-05-12; primary mgmt commentary on 25-35bps NCO guide + Q1 ex-fraud 39bps + deposit costs $650-700M"

to: REGINALD (ACTION)
info: BROCK, LIQUID, HENRY, RED, NEXUS, PROME

signal_type: catalyst
confidence: 0.85
confidence_language: confirmed
resources: 0
safety_net: clear

word_count: ~280

cluster: BANK_COLLATERAL
signal_role: cluster_mediating
event_window: closed

verify_research_verdict: CONFIRMED (REGINALD STATUS post-mortem + V2.1 → V2.1.1 revision commit 1b37fccc; WAL Investor Day is institutional-primary public event)
mark_context: backdated archive — event 5/12 (Investor Day), REGINALD shipped post-mortem 5/17, WALTER dispatch 5/21. 9-day lag from event to BOARD archive. Reads as separate-event from B1 fire (companion SIG-W-20260521-007) which surfaced via 10-Q drill 5/21 — both inform REGINALD's V2.1 → V2.2 progression but the WAL Investor Day B3 fire predates B1 and is the prior calibration step.
---

# WAL Investor Day 5/12 — Bucket E B3 Fired: Mgmt Held 25-35bps NCO Guide Despite Q1 ex-Fraud 39bps + Deposit Costs $650-700M

**Event (2026-05-12 WAL Investor Day, REGINALD post-mortem commit `1b37fccc` 5/17):** WAL management held its **25-35bps NCO guidance for FY26** at Investor Day **despite** Q1 ex-fraud NCO already running at **39bps** (above the high end of the guide) **AND** disclosed full-year deposit cost run-rate of **$650-700M**. REGINALD's Bucket E B3 falsifier — mgmt-credibility-on-NCO-guide — **FIRED** on the gap between actuals + costs and the held forward guide.

## Substance

- **B3 falsifier mechanism = mgmt-credibility-on-forward-guide vs realized-cost-stack.** REGINALD pre-registered B3 as: if mgmt holds NCO guide while realized NCO + deposit costs imply the guide is structurally unreachable, the gap is itself the signal. 39bps Q1 ex-fraud > 35bps high-end + $650-700M deposit cost run-rate makes the 25-35bps guide structurally optimistic; management's choice to hold rather than revise carries information.
- **V2.1 → V2.1.1 minor revision (post-Investor-Day):** Bear-slow 23% → 27%; REG-25 55% → 65%+. The reweight precedes V2.2 (which added the B1 fire 5/21). Two-step progression: 5/12 B3 (mgmt-credibility) → 5/21 B1 ($99M sponsor walk-away). Companion SIG-W-20260521-007 captures the B1 step.
- **Same calendar day SSB $95P + WAL $75P expired** May 15 — POSITIONS 8 → 7. The 5/12 Investor Day was the pre-event trigger window for the 5/15 expiry pile; mgmt-credibility hit didn't move the tape enough to rescue the puts.
- **Cross-reference to RED Session 12 stagflation-on-tape thread.** RED's 5/12 verdict via sub-agent: HOLD bear thesis (mgmt soft-deflective on fraud-bridge; tape rejected reset WAL 3 consecutive sub-$78 closes; REG-T-02 sustained 2 sessions per RED tally). RED + REGINALD converged on Investor-Day-was-not-clearing-event.

## Routing rationale

- **REGINALD action** (cluster owner; already shipped post-mortem; documentation surface)
- **BROCK info** (PC_STRESS cross-cluster; bank-credit-quality vs guide mechanism)
- **LIQUID info** (credit-stress consumer-credit-bank transmission)
- **HENRY info** (Fed-cut / bank-stress macro framework)
- **RED info** (cluster_mediating; Session 12 stagflation-on-tape integration already done)
- **NEXUS info** (cluster classification)
- **PROME info**

## Pre-registered watches (forward-flag)

- **Q2 NCO print late July:** if NCO comes in 30-35bps range (within guide), B3 reverses partially; if 40+bps, B3 fully confirmed and Bear-medium probability gains share.
- **Deposit-cost trajectory Q2:** $650-700M run-rate vs Q2 actual — if Q2 deposit cost exceeds Q1 rate, NIM compression hits the guide from the cost side.
- **OZK Q2 read-across:** IQHQ-style sponsor walk-away precedent from OZK Q1 — if OZK Q2 surfaces similar pattern, sponsor-walk-away as cohort-mechanism vs idiosyncratic-event hardens.

---

*WALTER backfill dispatch (BANK_COLLATERAL silence 5/12-5/20 closing pass 2/4). Threshold scan: no new FALSIFICATION fires. Companion: SIG-W-20260521-007 (B1 fire 5/21 successor-step).*
