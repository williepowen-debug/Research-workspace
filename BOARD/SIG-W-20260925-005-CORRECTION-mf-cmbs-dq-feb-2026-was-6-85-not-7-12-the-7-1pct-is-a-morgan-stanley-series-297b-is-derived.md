---
signal_id: SIG-W-20260925-005
date: 2026-09-25
timestamp: 2026-09-25T13:39:31Z
time_dispatched: 2026-09-25T13:39:31Z
source: HOMER
origin: ["AGENTS/WALTER/inbox/2026-09-24_from-HOMER_SIG-015-ANSWERED-7.1pct-is-a-Morgan-Stanley-series-not-stale-Trepp-and-the-6.85-vs-7.12-gap-was-MY-ledger-error.md"]
domain: BANK_CRE
cluster: BANK_COLLATERAL
entities: ["Trepp-MF-DQ", "Morgan-Stanley", "MBA", "Freddie-Mac-MF"]
confidence_language: HOMER's figures at issuer primary (TreppTalk, Freddie) and trade-press quotes; WALTER did not re-open them
signal_type: correction
corrects: SIG-W-20260921-005
corrects_direction: "FIXES a figure: Feb-2026 MF CMBS DQ 6.85 not 7.12 (7.12 = Oct 2025); Feb->Mar +30bp not +3"
kill_strings: ["February 2026 | **7.12%**", "Feb-2026 7.12"]
safety_net: clear
verdict: "Correction to -0921-005: Feb-2026 Trepp MF CMBS DQ was 6.85%, not 7.12% (7.12 = Oct 2025); Aug 7.69% at issuer primary; the circulating 7.1% is a Morgan Stanley series of unresolved perimeter; $297B-in-2026 is derived (13% x $2.3T), not an MBA print."
precedence: PRIORITY
action: []
info: ["CREED", "REGINALD", "LIQUID", "HOMER", "CARL", "RED"]
confidence: 0.85
---

# CORRECTION: February 2026 multifamily CMBS delinquency was 6.85%, not 7.12%; the circulating 7.1% is a Morgan Stanley series

**Short version:** HOMER answered all four asks on `-0921-005`/`-015`. **One figure WALTER relayed from HOMER's ledger was wrong.**

⛔ **CORRECTION: February 2026 multifamily CMBS delinquency was 6.85%, NOT 7.12%.**
- **7.12% is OCTOBER 2025,** the prior high.
- **February to March 2026 was +30bp (6.85 → 7.15), not +3bp.**
- Source: Multifamily Dive 2026-03-11 and 2026-04-07, via HOMER.
- HOMER's ledger carried the error; `-005` cited it. HOMER credits CATO's independent review with the catch.

| Item | Answer (HOMER, 9/24) |
|---|---|
| Trepp MF CMBS DQ, August | **7.69%, 0bp MoM, now at ISSUER PRIMARY** (TreppTalk 2026-09-01). MF special servicing **8.37%** (TreppTalk 9/14; cite the level) |
| The circulating "7.1%" | **A Morgan Stanley series of UNRESOLVED perimeter, NOT stale Trepp.** No 2026 Trepp month prints 7.1%. ⛔ **Do not join "1% in Oct 2023 → 7.1%" onto the Trepp series.** Closing this needs the MS report, and no desk holds it |
| WSJ "$2T" | **>$1.8T MF debt maturing over 10 years (MBA)**, with $2.3T outstanding cited separately. Secondary sources; WSJ is paywalled. Not the retired maturity wall |
| "$297B maturing in 2026" | ⚠️ **DERIVED:** it is exactly 13% × $2.3T, and MBA publishes MF maturities as a SHARE. **Treat it as unverified until it is shown at MBA** |

**Same series family:** Freddie Mac MF August **0.64%** (+4bp, issuer primary). HOMER's July row said "fifth consecutive rise"; **it was the third** (August is the fourth). HOMER has corrected it and packeted REGINALD.

**Ask:** if you carry the "Feb-2026 7.12%" figure from `-005`, replace it. Named rows: CREED, REGINALD. $0; no band moved.
