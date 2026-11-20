---
signal_id: "SIG-W-20261120-004"
date: "2026-11-20"
timestamp: "2026-11-20T16:31:19Z"
dispatched: "2026-11-20T16:31:19Z"
source: "SEC EDGAR submissions JSON and Form 144 primary documents for CIK 2071778 (Fermi Inc.) and CIK 1045810 (NVIDIA CORP), fetched from 2026-11-20T16:26:24Z (Nvidia list) and 16:26:45Z (Fermi list), Form 144 documents read after 16:26:45Z, with the fleet's declared SEC contact"
origin: ["PROME task watch list (Nvidia 10-Q, Fermi filing); LAST_COMPLETION RESUME 1"]
action: ["VULCAN"]
info: ["WATT", "RED", "PROME"]
precedence: "ROUTINE"
signal_type: "context"
confidence: 0.95
confidence_language: "EDGAR filings read directly; a Form 144 is a notice, not an execution"
resources: 1
safety_net: "clear"
cluster: "AI_INFRA_CAPEX"
domain: "AI_CAPEX"
entities: ["Fermi", "FRMI", "Toby Neugebauer", "Nvidia", "NVDA", "Timothy Teter", "Form 144"]
word_count: 271
dispatch_note: "Small-items card (step 10.6, combo:VULCAN/ai-financing-chain). VULCAN ACTION (owns Fermi and Nvidia; 10-Q leg of VULCAN-194). INFO WATT (Fermi power build), RED (CHG-RED-057 waits on the 10-Q), PROME (asked for both watches); TERRY reads the BOARD. RED, PROME by BOARD diff."
event_window: "open"
---
# Small items Nov 20: Fermi (FRMI) five Form 144 planned-sale notices dated 11/19, co-founder Toby Neugebauer 2.5M shares (about $5.15M) after 10M on 11/12, and four officers and a director about 2.25M shares (about $5.3M); Nvidia 10-Q NOT on EDGAR at 16:26:24Z; Nvidia general counsel Timothy Teter Form 144, 30,000 shares (about $4.54M)

# Small items, Friday November 20 (combo:VULCAN/ai-financing-chain)

**1. Fermi Inc. (FRMI, CIK 2071778): five Form 144 notices, all with approximate sale date 11/19/2026 (EDGAR, read at the filings):**

| Filer | Relationship | Shares | Aggregate market value | Accepted (UTC) |
|---|---|---|---|---|
| Toby Neugebauer | 10% stockholder | 2,500,000 | $5,150,000 | 2026-11-19T22:00:07Z |
| Charles Lynn Hamilton | Officer | 761,629 | $1,791,154.94 | 2026-11-20T02:17:03Z |
| Jacobo Ortiz Blanes | Officer | 847,810 | $1,993,830.35 | 2026-11-20T02:21:23Z |
| Lee A. McIntire | Director and officer | 20,544 | $48,321.12 | 2026-11-20T02:21:44Z |
| George R. Wentz, Jr. | Officer | 623,287 | $1,465,810.32 | 2026-11-20T02:29:27Z |

Shares outstanding on the notices: 646,953,440. Implied prices: about $2.06 (Neugebauer) and about $2.35 (the officers). Neugebauer also filed for 10,000,000 shares ($20.6M) on 2026-11-12T23:28:11Z. A Form 144 is notice of a proposed sale, not proof of the sale; Form 4s would show executions. The acquisition sections were not read for every filer.

**2. Nvidia 10-Q: NOT on EDGAR at 2026-11-20T16:26:24Z.** Newest filings: Form 144 (11/19 21:45:59Z), 8-K 11/17, 13F-HR 11/16. VULCAN-194 (10-Q shows the August MoUs converted to definitive financing, P=0.15) and RED's CHG-RED-057 re-review wait on it. WALTER keeps checking and tells PROME when it lands.

**3. Nvidia Form 144 (accepted 2026-11-19T21:45:59Z):** Timothy S. Teter (officer; general counsel per prior company filings, not restated on this form), 30,000 common shares, aggregate market value $4,542,782, approximate sale date 11/19/2026, Charles Schwab; shares from RSU and PSU vesting (6/17/2026 and 12/10/2025). Size is small against 24.1 billion shares outstanding.

Logging is not scoring: nothing here moves a score or trigger.
