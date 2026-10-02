---
signal_id: SIG-W-20261002-019
date: 2026-10-02
timestamp: 2026-10-02T18:30:13Z
time_dispatched: 2026-10-02T18:30:13Z
timestamp_note: stamped from the system clock at write, not typed
source: Will (terminal screenshot, Sam Koppelman / Hunterbrook X posts)
origin: ["hntrbrk.com/breaking-news/lennar-millrose, 2026-10-02 11:00 ET (Termine, Ahn, Koppelman, Spendley, Cera), read via WebFetch ~18:2xZ", "Investing.com / Benzinga 10/02: LEN falls after the report (headlines)"]
domain: BANK_CRE
cluster: CONSUMER_STAGFLATION
entities: ["Lennar", "LEN", "Millrose-Properties", "MRP", "Hunterbrook-Capital"]
confidence: 0.78
confidence_language: "reports"
signal_type: research
safety_net: clear
verdict: "Hunterbrook (10/02 11:00 ET; Hunterbrook Capital is SHORT LEN and MRP): Lennar sold 700+ finished homes (~$200M) to Millrose, the land REIT it spun off, in about a month, across 51 counties in 15 states, at least 136 in Florida. At least 356 purchases fell in the last week of Lennar's fiscal quarter, which Lennar's delivery target beat by just 340 homes. Millrose amended its agreements 8/27 to buy and RENT finished homes, after filings said it would have no tenants. Neither company answered substantively. LEN $79.86 (-2.75%), MRP $24.67 (-2.12%) at 14:2x ET."
precedence: PRIORITY
action: ["HOMER"]
info: ["CORAL", "CARL", "REGINALD", "BROCK", "RED"]
dispatch_note: "Housing carve-out: national builder/asset-market -> HOMER action, CARL + REGINALD info. Axis sweep (10.7): geography -> CORAL info (136 FL homes; FL top priority; national story, not FL-specific on its face). BROCK info: Millrose's ~5% yield vs its borrowing cost (REIT leverage). Domain BANK_CRE is the nearest code for housing (no HOUSING code; open question -1001-025). HOMER IN-FLIGHT as homer-1002 (ORCH_INFLIGHT re-read 18:29Z). Will batch BM-20261002-04 item 2. RED pull-complete."
---
# Hunterbrook (short LEN and MRP): Lennar sold 700+ homes, about $200M, to its own spinoff Millrose in about a month. 356 of the sales fell in the last week of the quarter, and Lennar met its delivery target by 340 homes.

**Short version:** Hunterbrook published an investigation on **10/02 at 11:00 ET.** It found that **Lennar sold more than 700 finished homes (~$200M) to Millrose Properties**, the land REIT Lennar spun off last year, **in about a month**, across **51 counties in 15 states, at least 136 in Florida.** **At least 356 of those purchases fell in the final week of Lennar's fiscal quarter.** Lennar beat the bottom of its delivery forecast by **just 340 homes, the only one of its five homebuilding targets it met.** On **8/27** Millrose and Lennar subsidiaries **amended their agreements so Millrose can buy finished homes and rent them out.** Millrose's annual report had said it would **not "have any tenants or occupants."** Hunterbrook estimates Millrose earns **~5% a year** on the houses after property costs, **before interest**, i.e. less than it pays to borrow. **Neither company answered substantively.**

| | |
|---|---|
| Homes / value | 700+ / ~$200M, ~1 month |
| Spread | 51 counties, 15 states, **≥136 in Florida** |
| Quarter-end | ≥356 purchases in the final week vs a **340-home** margin over the delivery-forecast floor |
| Structure change | 8/27 amendment: Millrose may buy and rent finished homes |
| Economics | ~5% gross yield after property costs, before interest (Hunterbrook estimate) |
| Market 10/02, 14:2x ET | **LEN $79.86 (−2.75%) · MRP $24.67 (−2.12%)** |

**So what:** If it holds up, part of America's largest builder's quarter-end **"demand" was its own affiliate** buying unsold inventory and renting it out. That is a **demand-quality** signal on new homes (HOMER's builder-inventory read: `SIG-W-20260621-013`, builder inventory ~9 months, near 2008). The **Florida leg (≥136 homes)** puts it in CORAL's geography.

## Caveats
- ⚠️ **The publisher has a position: "Hunterbrook Capital is short $MRP, short $LEN, and long a basket of comparable securities."** It is an advocacy investigation with a financial interest. The deed records it cites are checkable, and the inference about quarter-end delivery targets is Hunterbrook's.
- The "340-home margin" compares Hunterbrook's count with Lennar's guidance floor. **Lennar's own accounting of affiliate sales is not seen here.**
- WALTER read Hunterbrook's article via a fetch summary, not the deed records. The ≥136 Florida count is Hunterbrook's minimum.

## Exposure
No LEN or MRP in Will's position record (FORGE mirror, 10/01).

## Requested action
**HOMER:** read it as demand quality: how much of the delivery beat was affiliate buying. Check it against your builder-inventory read and Lennar's next disclosure. CORAL (FL leg), CARL, REGINALD, BROCK (Millrose leverage), RED: information.
