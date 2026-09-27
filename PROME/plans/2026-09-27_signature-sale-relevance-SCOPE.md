# Signature Bank loan sale — relevance to FLG: bounded scope (2026-09-27, Sun 17:4x ET)

**Origin:** CATO's review of the CRE → bank synthesis (relayed by Will 17:39 ET): *"scope a bounded Signature-sale investigation for CREED and FLG. Establish what was sold, the transaction structure, and which FLG exposures it can inform before treating the headline sale discount as a loan-loss assumption."* **Status: SCOPED, NOT DISPATCHED** — dispatch waits for Will's word (he reserved new research until after the first synthesis). Parent: `PROME/reports/2026-09-27_cre-to-bank-transmission-SYNTHESIS.md` §8 item 4.

## The question
Can the FDIC's 2023 sale of Signature Bank's CRE / rent-regulated loans inform any FLG loss assumption — and if so, which pool, on what basis, and with what adjustment? **Nothing about the sale is asserted here from memory; establishing it is the task.**

## Legs
| Owner | Establish, from primary FDIC disclosures (press releases, sale/offering documents, transaction terms) |
|---|---|
| **CREED** | (1) **What was sold:** loan count, balance, property types, NYC rent-regulated share, geography, performing vs non-performing, vintage, lien position. (2) **Transaction structure:** outright sale vs joint venture; any equity the FDIC retained; any seller financing; how the reported price was computed (of what balance, on what date). (3) **What the headline number measures** — a clearing price, a price net of retained upside, a financed price — and whether it can be read as a loss rate at all. (4) Six-dimension transfer grade (type · market · vintage · appraisal date · lien · performing vs defaulted) against each FLG pool below. |
| **FLG** | Map CREED's grade onto FLG's own pools, one row per pool, with what FLG's filings disclose about each pool's composition. Say for each: INFORMS (with the adjustment needed) · PARTIAL · DOES NOT INFORM. |

**FLG pools to grade, individually (10-Q basis 6/30/26, from REGINALD's bridge b93e3ac58):** MF nonaccrual NYC ≥50% rent-regulated $1,737M · MF criticized NYC rent-regulated $2,665M · MF pass NYC rent-regulated $4,089M · MF nonaccrual other $395M · MF criticized other $4,274M · CRE nonaccrual $471M · CRE criticized $1,367M. The expectation to TEST, not assume: relevance is likeliest for the NYC rent-regulated pools and least likely for the CRE pools.

## Bounds
- Primary FDIC disclosures + FLG's own filings; secondary press only to locate a primary. Unavailable evidence is flagged to PROME as soon as it is hit.
- **No loss rate, score, threshold, tool or trade changes.** A proposed change to a bridge loss rate goes to REGINALD (bridge owner) and comes back to Will separately.
- Delivery contract as in `PROME/plans/2026-09-27_cre-to-bank-loss-transmission-PLAN.md`: OBSERVED / SCENARIO ASSUMPTIONS / UNKNOWNS, cited; the next observation that would change the conclusion; file committed in the desk's own dir; `SendMessage` PROME the path + commit as the final action. CREED delivers first; FLG maps from CREED's file (they may message each other directly).
