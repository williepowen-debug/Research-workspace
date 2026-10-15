---
signal_id: SIG-W-20261008-050
date: 2026-10-08
timestamp: 2026-10-09T00:43:59Z
time_dispatched: 2026-10-09T00:43:59Z
timestamp_note: "stamped from the wall clock in the same process as the write (MEMORY #34)"
source: "WALTER evening sweep 10/8 (agent C, d3-d4); resolves the -040 hold on Wymore 360"
origin: ["BMO 2024-5C8 Mortgage Trust 10-D Ex-99.1 (filed 2026-10-02), primary", "JPMCC 2017-JP7 10-D Ex-99.1 (filed 2026-09-28), primary", "Morningstar Credit via Connect CRE (snippet only)", "AGENTS/WALTER/research/2026-10-08_evening-sweep/C_markets-credit-fed-asia.md"]
domain: BANK_CRE
cluster: BANK_COLLATERAL
case: ["The Wymore 360, Altamonte Springs FL", "St. Luke's Office, Allentown PA"]
entities: ["BMO 2024-5C8", "CWCapital", "JPMCC 2017-JP7", "CSAIL 2017-C8", "Intel"]
precedence: ROUTINE
action: ["CORAL", "CREED"]
info: ["HOMER", "REGINALD"]
confidence: 0.9
confidence_language: "servicer data and comments read from the trusts' 10-D exhibits; the St. Luke's total and Intel cause are snippet-only"
signal_type: research
safety_net: clear
event_window: closed
word_count: 249
dispatch_note: "Named-case feed (ROUTING_CARVEOUTS: CREED). Wymore 360: FL (CORAL action), multifamily (HOMER info). St. Luke's: office CMBS (CREED action). Neither event is new tonight (transfers 8/11 and 8/13); what is new is primary confirmation. Discharges LAST_COMPLETION FOLLOW-UP 2 (Wymore held at grade C pending EDGAR)."
---

# CRE cases confirmed at the trust filings: The Wymore 360 (Altamonte Springs FL, $33M multifamily) is in special servicing with foreclosure as the strategy; St. Luke's Office (Allentown PA) transferred for imminent default after Intel left

**1. The Wymore 360, Altamonte Springs FL. Resolves the hold WALTER put on this lead.** Source: BMO 2024-5C8 Mortgage Trust 10-D, filed 10/2 (Ex-99.1, primary).
- **Loan:** $33.0M, interest-only, 6.839%, matures 11/06/2029. 200-unit multifamily property, built 1973, renovated 2024. Appraised $46.5M (5/2024).
- **Status:** paid through 07/06/26, one month delinquent. **Transferred to special servicing 08/11/26 for payment default.** Resolution strategy code 2 = **foreclosure**. DSCR **0.65x** (6/30/26); 89.5% occupied (July).
- **Servicer comment:** *"Borrower noted in the initial discussions that they wanted to work with the special servicer on a transition of the property."* The trust-level special servicer is CWCapital (replaced Greystone 7/29); not confirmed for this loan.

**2. St. Luke's Office, Allentown PA.** Source: JPMCC 2017-JP7 10-D, filed 9/28 (Ex-99.1, primary).
- **Transferred 08/13/26** for *"imminent default due to cash flow issues"*; strategy to be determined.
- This trust's piece is $14.47M of a reported $43.4M split with CSAIL 2017-C8 (snippet).
- Paid through 08/06/26 (current), DSCR 1.30x (6/30/26), matures 05/06/2027.
- Cause per Morningstar (snippet): **Intel**, the second-largest tenant (24% of space), left in 2026.

**Neither event is new tonight; the primary confirmation is.** **CORAL (action):** Florida multifamily case. **CREED (action):** both cases to the case ledger; St. Luke's is office CMBS. **HOMER / REGINALD (info).** Sweep record: `AGENTS/WALTER/research/2026-10-08_evening-sweep/C_markets-credit-fed-asia.md` (d3–d4).
