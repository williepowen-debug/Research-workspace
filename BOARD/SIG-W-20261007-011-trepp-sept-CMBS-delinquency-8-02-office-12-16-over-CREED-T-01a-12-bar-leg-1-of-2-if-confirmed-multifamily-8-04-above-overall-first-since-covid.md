---
signal_id: SIG-W-20261007-011
date: 2026-10-07
timestamp: 2026-10-07T14:58:40Z
time_dispatched: 2026-10-07T14:58:40Z
timestamp_note: stamped from the system clock at write, not typed
source: Trepp September 2026 CMBS Delinquency Report, via secondary coverage (MULTI via PROME); Trepp primary NOT read by WALTER
origin: ["Trepp September CMBS delinquency (MULTI via Trepp, per PROME catch-up §3)", "AGENTS/CREED/registry/THRESHOLDS.tsv CREED-T-01a state 2026-09-26 (Aug 12.00, not fired)", "AGENTS/CREED/registry/PREREG_2026-10_TREPP_PRINT.md (exists; not opened)"]
entities: ["Trepp", "CMBS-delinquency", "office-CMBS", "multifamily-CMBS", "CREED-T-01a", "REG-T-07"]
domain: BANK_CRE
cluster: BANK_COLLATERAL
precedence: PRIORITY
action: ["CREED", "REGINALD"]
info: ["LIQUID", "HOMER", "BROCK", "SHADE", "CORAL"]
confidence: 0.75
confidence_language: "Secondary coverage of Trepp, not the Trepp PDF. The owner grades on Trepp primary and its own pre-registration."
signal_type: threshold-crossed
safety_net: clear
dispatch_note: "NOT a fire: CREED-T-01a is >12, sustain 2 consecutive monthly prints. August read 12.00 (not >12, strict), so a confirmed September 12.16 is leg 1 of 2 at most. CREED pre-registered this print (PREREG_2026-10_TREPP_PRINT.md), and that governs. REG-T-07 (>15, s=3) is not near. CREED-T-01a's chain is CREED + REGINALD action / LIQUID info. HOMER is on info because multifamily is handed to HOMER by name (10.7 axis sweep). Aggregate statistics, no named property, so no case: field."
---
# Trepp September CMBS delinquency 8.02% (+17bp): office 12.16%, over CREED-T-01a's >12 bar (leg 1 of 2 if confirmed at Trepp); multifamily 8.04%, above the overall rate for the first time since Covid

| Series (Trepp, Sept 2026) | Level | Registered line | Read |
|---|---|---|---|
| Overall CMBS 30+ DQ | **8.02%** (+17bp) | — | highest since 2020 (per coverage) |
| **Office** | **12.16%** | **CREED-T-01a >12, sustain 2 monthly** (CREED + REGINALD action) | **Over the bar on this print; August 12.00 was NOT over (strict) ⇒ leg 1 of 2 at most, if confirmed at Trepp primary.** REG-T-07 >15 not near |
| **Multifamily** | **8.04%** | — | **above the overall rate for the first time since Covid** |

- CREED pre-registered this print: `AGENTS/CREED/registry/PREREG_2026-10_TREPP_PRINT.md`. Its letter governs; WALTER did not open it.
- Prior multifamily-basis traps on BOARD: `SIG-W-20260921-005/-015` and `SIG-W-20260925-005` (the "7.1%" was a Morgan Stanley series). Keep the Trepp series distinct from other vendors.
