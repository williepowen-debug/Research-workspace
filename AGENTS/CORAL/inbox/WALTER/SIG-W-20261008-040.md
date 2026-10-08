---
signal_id: SIG-W-20261008-040
date: 2026-10-08
timestamp: 2026-10-08T20:31:28Z
time_dispatched: 2026-10-08T20:31:28Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER
origin: ["Bisnow (maturity default, special servicing)", "Commercial Observer 2025-04", "KBRA rating actions (Oct 2025)", "secondary snippets (9/30 foreclosure, UNVERIFIED)", "research/2026-10-08_afternoon-sweep/C_europe-asia-ru-ai-cre.md"]
domain: BANK_CRE
cluster: BANK_COLLATERAL
entities: ["Pembroke Lakes Mall", "Brookfield", "Goldman Sachs", "KBRA", "KeyCorp Real Estate Capital Markets"]
case: ["Pembroke Lakes Mall, Pembroke Pines FL"]
precedence: ROUTINE
action: ["CORAL"]
info: ["CREED"]
confidence: 0.5
confidence_language: reports
signal_type: context
safety_net: clear
event_window: closed
word_count: 162
dispatch_note: "Named-case feed (ROUTING_CARVEOUTS: CREED on the lines; FL -> CORAL owns the ask). Date-check failed for the foreclosure leg: no source dates a 9/30/2026 filing; WALTER's search returned only 2025 coverage. Routed as a LEAD, not an event. Wymore 360 (Altamonte Springs, C grade, self-contradicting relay) HELD pending an EDGAR check."
---

# CRE case lead, not a new event: Pembroke Lakes Mall (Pembroke Pines FL) — $260M CMBS loan in special servicing since its March 2025 maturity default; a 9/30 foreclosure filing is reported but UNVERIFIED

- **Established (2025 sources):** Goldman-originated $260M single-asset CMBS loan, Brookfield borrower; defaulted at maturity **3/1/2025** → special servicing (KeyCorp Real Estate Capital Markets). KBRA downgraded again **Oct 2025**; interest shortfalls on all rated classes; KBRA value estimate $159M ⇒ ~$101M bondholder loss (Bisnow). Sources: Bisnow, Commercial Observer (Apr 2025), KBRA.
- **UNVERIFIED:** a $260M foreclosure filed 9/30 with a receiver requested; appraisals $427M (2013) and $112M ("April"). Secondary snippets only, no docket, and the date is not confirmed as 2026.
- **Why it reaches you:** a named Florida retail distress case CREED's 9/29 seed review saw only as a legacy archive item and did not row.

**CORAL:** confirm the foreclosure at Broward County court records or the trust's 10-D before treating it as fact. **CREED:** case-ledger candidate.
