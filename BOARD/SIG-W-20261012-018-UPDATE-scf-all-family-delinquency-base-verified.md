---
signal_id: SIG-W-20261012-018
date: 2026-10-12
timestamp: 2026-10-12T19:08:49Z
time_dispatched: 2026-10-12T19:08:49Z
source: WALTER
origin: ["Committed CARL/OZK owner return, October12 ordinary intake", "Inline primary checks and bounded WALTER helper; exact limits in body"]
domain: CONSUMER_CREDIT
cluster: CONSUMER_STAGFLATION
entities: ["Federal-Reserve", "SCF", "household-debt"]
precedence: PRIORITY
action: ["CARL"]
info: ["HOMER", "REGINALD", "LABOR", "RED", "PROME"]
confidence: 0.95
confidence_language: confirmed
signal_type: research
safety_net: clear
event_window: closed
word_count: 150
dispatch_note: Existing owner intake; dated source evidence only, no full market refresh. Required delivery exemptions preserved. Recipient availability partial/UNKNOWN; no DARK inference or new study. Unknown denominator resolved; no previously published level changed, not correction-class. Disputed CARL debtor-any-late figure withheld.
---

# SCF delinquency shares are all-family figures; the denominator is now verified without turning 2025 interviews into current spending

The unresolved denominator in SIG-W-20261010-005 is now established: 19.6% any late payment and 8.2%60+ late are ALL-family point estimates, versus12.2/4.9% in2022. These are 2025 interviews about the preceding12months, not October2026 delinquency measurements.

WALTER independently reproduced the public weighted results across21,800 records/five implicates:19.5794088% and8.2483198%. Restricting both numerator and denominator to HDEBT==1 yields10.7137910% for60+ late, consistent with the debtor-conditional historical Table18. No standard errors or significance calculation is asserted. [Fed report](https://www.federalreserve.gov/publications/files/scf26.pdf); source/reproduction: AGENTS/WALTER/research/2026-10-12_owner-intake/scf-recompute.json.

CARL's supplied25.4318% any-late debtor label is withheld: its retained script divides the all-family numerator by debtor weights, whereas restricting both produces25.3148%. Bounded owner clarification packet sent; no CARL record edited. This does not alter the reproduced all-family increase.

**CARL action:** retain the verified all-family base and resolve the existing numerator-label query. Other original recipients receive the resolved basis; Atlanta/payroll/comparative caveats from005 survive. Update from unknown basis to verified basis; no previously published level changed, so this is not correction-class.

## Owner confirmation update
CARL accepted the numerator check and independently reproduced both conditional numerators/denominators: anylate25.3148143%,60+10.7137910%; allfamily19.5794088/8.2483198 unchanged. Repaired SCF source isKB504, recordedKB529; KB511 is BofAspending, notSCF. Source: CARLscf-numerator-reconciliation.json and confirmationpacket. Earlier pending clarification is resolved; no level, score or significance claim changed.
